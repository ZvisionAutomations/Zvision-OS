"""
Zvision HERMES Agent — FastAPI webhook server.
Receives Evolution API events, routes through HERMES agent core, replies via Evolution.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import os
import re
import time
from collections import deque
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI, Header, HTTPException, Request, Response
from fastapi.responses import JSONResponse

import agent_core
import calendar_client
from evolution_client import EvolutionClient, get_evolution_client
from knowledge import get_knowledge_base
from lead_memory import Lead, LeadStateManager
from reminders import run_reminder_loop
from stt import transcribe_audio
from tts_polly import text_to_speech

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

PORT = int(os.getenv("PORT", "3400"))
MIGUEL_PHONE = os.getenv("MIGUEL_PHONE", "")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "")
GOOGLE_CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "")

# Trigger phrase Ana uses when lead is qualified and calendar is enabled
_SCHEDULE_TRIGGER = "vou verificar os horários"
MAX_MESSAGES = 40
MAX_AUDIO_B64_LEN = 22_000_000  # ~16MB decoded
MAX_TEXT_LEN = 2_000

# Per-phone rate limiting: 10 messages per 60s (C4)
_RATE_LIMIT = 10
_RATE_WINDOW = 60.0
_rate_buckets: dict[str, deque] = {}

# Dedup camada 1: por msg_id (H3)
_processed_ids: dict[str, float] = {}
_MSG_TTL = 60.0
_MAX_DEDUP = 10_000

# Dedup camada 2: por conteúdo — cobre webhooks duplicados com IDs distintos
_processed_content: dict[str, float] = {}
_CONTENT_DEDUP_TTL = 10.0  # segundos — janela para considerar duplicata


def _content_dedup_check(phone: str, text: str) -> bool:
    """Retorna True se o conteúdo já foi processado dentro da janela TTL."""
    now = time.monotonic()
    key = hashlib.md5(f"{phone}:{text.strip().lower()}".encode()).hexdigest()
    # Limpa entradas expiradas
    expired = [k for k, ts in _processed_content.items() if now - ts > _CONTENT_DEDUP_TTL]
    for k in expired:
        _processed_content.pop(k, None)
    if key in _processed_content:
        return True
    _processed_content[key] = now
    return False

# Per-lead async locks with guard (C3)
_locks_guard = asyncio.Lock()
_lead_locks: dict[str, asyncio.Lock] = {}

lead_mgr = LeadStateManager()
last_qr: str | None = None

# Patterns that indicate LLM broke persona (H5)
_IA_REVEAL_PATTERNS = re.compile(
    r"(sou uma? (ia|intelig[eê]ncia artificial|bot|rob[oô]|modelo|llm)|"
    r"como (modelo|ia|llm)|n[aã]o sou humano|artificial intelligence|"
    r"openrouter|groq|llama|gemma|claude|gpt)",
    re.IGNORECASE,
)
_IA_FALLBACK = "Tô focada em te ajudar aqui. Me conta: qual é o maior gargalo da sua operação hoje?"


def _mask(phone: str) -> str:
    return phone[:4] + "****" + phone[-2:] if len(phone) >= 6 else "****"


def _check_rate(phone: str) -> bool:
    now = time.monotonic()
    if phone not in _rate_buckets:
        _rate_buckets[phone] = deque()
    bucket = _rate_buckets[phone]
    while bucket and now - bucket[0] > _RATE_WINDOW:
        bucket.popleft()
    if len(bucket) >= _RATE_LIMIT:
        return False
    bucket.append(now)
    return True


async def _get_lock(phone: str) -> asyncio.Lock:
    async with _locks_guard:
        if phone not in _lead_locks:
            _lead_locks[phone] = asyncio.Lock()
        return _lead_locks[phone]


def _check_auth(apikey: str) -> None:
    if WEBHOOK_SECRET and apikey != WEBHOOK_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")


@asynccontextmanager
async def lifespan(_app: FastAPI):
    kb = get_knowledge_base()
    await kb.load()

    if MIGUEL_PHONE and not re.match(r"^\d{10,15}$", MIGUEL_PHONE):
        logger.warning("[init] MIGUEL_PHONE format suspicious: %s", _mask(MIGUEL_PHONE))

    evolution = get_evolution_client()
    try:
        await evolution.create_instance()
        webhook_url = f"http://hermes-agent:{PORT}/webhook"
        await evolution.register_webhook(webhook_url, PORT, WEBHOOK_SECRET)
    except Exception as exc:
        logger.warning("[init] Evolution setup skipped: %s", exc)

    if GOOGLE_CALENDAR_ID and calendar_client.is_enabled():
        asyncio.create_task(run_reminder_loop(evolution))
        logger.info("[init] Reminder loop started (Google Calendar enabled)")
    else:
        logger.info("[init] Google Calendar not configured — reminders disabled")

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()}


# ── Webhook ───────────────────────────────────────────────────────────────────

@app.post("/webhook")
async def webhook(request: Request, apikey: str = Header(default="", alias="apikey")):
    # Silent 200 on auth fail — avoid leaking info to scanners (C1)
    if WEBHOOK_SECRET and apikey != WEBHOOK_SECRET:
        return Response(status_code=200)

    try:
        body: dict[str, Any] = await request.json()
    except Exception:
        return Response(status_code=200)

    event = body.get("event", "")

    if event == "QRCODE_UPDATED":
        global last_qr
        last_qr = (body.get("data") or {}).get("qrcode", {}).get("base64")
        return Response(status_code=200)

    if event not in ("messages.upsert", "MESSAGES_UPSERT"):
        return Response(status_code=200)

    data = body.get("data") or {}
    if not isinstance(data, dict):
        return Response(status_code=200)

    key = data.get("key") or {}
    if not isinstance(key, dict):
        return Response(status_code=200)

    if key.get("fromMe"):
        return Response(status_code=200)

    remote_jid: str = key.get("remoteJid", "")
    if "@g.us" in remote_jid:
        return Response(status_code=200)

    msg_id = key.get("id", "")
    _clean_dedup()
    if msg_id and msg_id in _processed_ids:
        return Response(status_code=200)
    if msg_id:
        _processed_ids[msg_id] = time.monotonic()

    phone = remote_jid.split("@")[0]

    if not _check_rate(phone):
        logger.warning("[webhook] Rate limit: %s", _mask(phone))
        return Response(status_code=200)

    sender_name: str = data.get("pushName") or phone
    message_type: str = data.get("messageType") or ""
    message: dict = data.get("message") or {}
    if not isinstance(message, dict):
        message = {}
    media_base64: str = data.get("base64") or ""

    # Audio size guard before spawning task (C6)
    if message_type == "audioMessage" and len(media_base64) > MAX_AUDIO_B64_LEN:
        logger.warning("[webhook] Audio too large from %s", _mask(phone))
        return Response(status_code=200)

    asyncio.create_task(
        _process_message(phone, remote_jid, sender_name, message_type, message, media_base64)
    )
    return Response(status_code=200)


async def _process_message(
    phone: str,
    remote_jid: str,
    sender_name: str,
    message_type: str,
    message: dict,
    media_base64: str,
) -> None:
    evolution = get_evolution_client()

    try:
        if message_type == "audioMessage":
            if not media_base64:
                msg_data = {"key": {"remoteJid": remote_jid}, "message": message, "messageType": message_type}
                media_base64 = await evolution.get_media_base64(msg_data) or ""
            if not media_base64:
                await evolution.send_text(remote_jid, "Recebi seu áudio, mas não consegui processar agora. Pode me escrever? 😊")
                return
            if len(media_base64) > MAX_AUDIO_B64_LEN:
                await evolution.send_text(remote_jid, "Áudio muito longo! Pode me escrever? 😊")
                return
            text = await transcribe_audio(media_base64)
            if not text:
                await evolution.send_text(remote_jid, "Recebi seu áudio, mas não consegui transcrever agora. Pode me escrever? 😊")
                return
            if _content_dedup_check(phone, text):
                logger.info("[webhook] Audio content-dedup: %s ignorado", _mask(phone))
                return
            logger.info("[webhook] Audio from %s: %d chars", _mask(phone), len(text))
            await _handle(phone, remote_jid, sender_name, text, evolution, input_was_audio=True)
            return

        if message_type == "imageMessage":
            img = message.get("imageMessage") or {}
            caption: str = img.get("caption") or ""
            mime: str = (img.get("mimetype") or "image/jpeg").split(";")[0]
            await _handle(
                phone, remote_jid, sender_name,
                caption or "[imagem]", evolution,
                image_base64=media_base64 or None,
                image_mime=mime,
            )
            return

        if message_type == "stickerMessage":
            await _handle(phone, remote_jid, sender_name, "[sticker]", evolution)
            return

        if message_type in ("videoMessage", "documentMessage"):
            await evolution.send_text(remote_jid, "Recebi seu arquivo! Processo texto, áudio e imagens — pode me descrever o que precisa? 😊")
            return

        text = (
            message.get("conversation")
            or (message.get("extendedTextMessage") or {}).get("text")
            or ""
        )
        if text.strip():
            text = text[:MAX_TEXT_LEN]
            if _content_dedup_check(phone, text):
                logger.info("[webhook] Content-dedup: %s ignorado", _mask(phone))
                return
            await _handle(phone, remote_jid, sender_name, text, evolution)

    except Exception as exc:
        logger.error("[webhook] Error from %s: %s", _mask(phone), exc)


async def _handle(
    phone: str,
    remote_jid: str,
    sender_name: str,
    text: str,
    evolution: EvolutionClient,
    input_was_audio: bool = False,
    image_base64: str | None = None,
    image_mime: str | None = None,
) -> None:
    lock = await _get_lock(phone)
    async with lock:
        await _handle_locked(
            phone, remote_jid, sender_name, text, evolution,
            input_was_audio, image_base64, image_mime,
        )


async def _handle_locked(
    phone: str,
    remote_jid: str,
    sender_name: str,
    text: str,
    evolution: EvolutionClient,
    input_was_audio: bool = False,
    image_base64: str | None = None,
    image_mime: str | None = None,
) -> None:
    lead = lead_mgr.get_or_create_inbound(phone, sender_name)

    if lead.state == "HUMAN_HANDOFF":
        # H2: Re-engage after 48h silence if lead messages again
        if not lead_mgr.check_handoff_reopen(lead):
            logger.info("[handler] %s ignored (HUMAN_HANDOFF)", _mask(phone))
            return

    if lead.state == "QUALIFIED":
        pass  # Allow Ana to follow up — meeting may not be booked yet

    if lead.state == "NOT_QUALIFIED":
        if not lead_mgr.check_re_engagement(lead):
            return

    lead.last_seen_at = datetime.now(timezone.utc).isoformat()

    if lead.message_count >= MAX_MESSAGES:
        logger.warning("[handler] %s hit message limit", _mask(phone))
        if not lead.handoff_sent:
            await _trigger_handoff(lead, phone, remote_jid, evolution)
        return

    if lead_mgr.wants_human(text) and not lead.handoff_sent:
        await _trigger_handoff(lead, phone, remote_jid, evolution)
        return

    content = f"[imagem] {text}".strip() if image_base64 else text
    lead.messages.append({"role": "user", "content": content})
    lead.message_count += 1

    # ── SCHEDULING: deterministic handler, no LLM needed ────────────────────
    if lead.state == "SCHEDULING":
        response = await _process_scheduling(lead, text, remote_jid, evolution)
        if response:
            lead.messages.append({"role": "model", "content": response})
            lead_mgr.store.save(lead)
            if input_was_audio:
                audio = await text_to_speech(response)
                if audio:
                    try:
                        await evolution.send_audio(remote_jid, audio)
                        return
                    except Exception as exc:
                        logger.warning("[handler] sendAudio failed (%s), fallback to text", exc)
            await evolution.send_text(remote_jid, response)
        return

    try:
        response = await agent_core.chat(lead, text, image_base64, image_mime)
        logger.info("[handler] Response for %s (%s)", _mask(phone), lead.state)
    except Exception as exc:
        logger.error("[handler] LLM error for %s: %s", _mask(phone), exc)
        return

    # H5: Post-filter IA revelation
    if _IA_REVEAL_PATTERNS.search(response):
        logger.warning("[handler] IA reveal detected for %s — using fallback", _mask(phone))
        response = _IA_FALLBACK

    # ── Detect scheduling trigger from Ana ───────────────────────────────────
    if (
        _SCHEDULE_TRIGGER in response.lower()
        and lead.state == "ANA_ACTIVE"
        and calendar_client.is_enabled()
    ):
        lead.state = "SCHEDULING"
        lead.scheduling_step = "need_contact"
        response = "Perfeito! Me passa seu nome completo e e-mail pra confirmar o horário do Miguel."
        lead.messages.append({"role": "model", "content": response})
        lead_mgr.store.save(lead)
        if input_was_audio:
            audio = await text_to_speech(response)
            if audio:
                try:
                    await evolution.send_audio(remote_jid, audio)
                    return
                except Exception as exc:
                    logger.warning("[handler] sendAudio failed (%s), fallback to text", exc)
        await evolution.send_text(remote_jid, response)
        return

    lead_mgr.process_state_transition(lead, response)

    if lead_mgr.is_handoff_response(response) and not lead.handoff_sent:
        await _trigger_handoff(lead, phone, remote_jid, evolution)
        return

    lead.messages.append({"role": "model", "content": response})
    lead_mgr.store.save(lead)

    if input_was_audio:
        audio = await text_to_speech(response)
        if audio:
            try:
                await evolution.send_audio(remote_jid, audio)
                return
            except Exception as exc:
                logger.warning("[handler] sendAudio failed (%s), falling back to text", exc)
    await evolution.send_text(remote_jid, response)


def _extract_email(text: str) -> str | None:
    match = re.search(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", text)
    return match.group(0).lower() if match else None


def _extract_slot_choice(text: str, max_choice: int) -> int | None:
    m = re.search(r"\b([1-9])\b", text)
    if m:
        n = int(m.group(1))
        if 1 <= n <= max_choice:
            return n
    # Handle ordinals in Portuguese
    ordinals = {"primeiro": 1, "primeira": 1, "segundo": 2, "segunda": 2, "terceiro": 3, "terceira": 3}
    lower = text.lower()
    for word, num in ordinals.items():
        if word in lower and num <= max_choice:
            return num
    return None


async def _process_scheduling(
    lead: Lead,
    text: str,
    remote_jid: str,
    evolution: EvolutionClient,
) -> str | None:
    """
    Deterministic handler for the SCHEDULING state.
    Returns the message to send, or None if nothing should be sent.
    """
    from datetime import timedelta, timezone as tz

    step = lead.scheduling_step

    # ── Step 1: waiting for email ────────────────────────────────────────────
    if step == "need_contact":
        email = _extract_email(text)
        if not email:
            return "Pode me confirmar o e-mail? Preciso pra enviar o convite da reunião."

        lead.email = email
        try:
            slots = await asyncio.to_thread(calendar_client.get_available_slots, 3, 3)
        except Exception as exc:
            logger.error("[scheduling] get_available_slots failed: %s", exc)
            return "Tive um problema ao buscar os horários. Pode tentar de novo em instantes?"

        if not slots:
            lead.state = "QUALIFIED"
            lead.scheduling_step = ""
            return (
                "Não encontrei horários disponíveis nos próximos dias. "
                "O Miguel vai te chamar diretamente pra agendar!"
            )

        lead.slots_cache = slots
        lead.scheduling_step = "awaiting_slot"

        lines = ["Ótimo! Aqui os horários disponíveis:\n"]
        for i, slot in enumerate(slots, 1):
            lines.append(f"{i}. {slot['label']}")
        lines.append("\nQual funciona melhor?")
        return "\n".join(lines)

    # ── Step 2: waiting for slot selection ───────────────────────────────────
    if step == "awaiting_slot":
        if not lead.slots_cache:
            lead.scheduling_step = "need_contact"
            return "Me passa seu e-mail pra confirmar o horário do Miguel."

        choice = _extract_slot_choice(text, len(lead.slots_cache))
        if choice is None:
            count = len(lead.slots_cache)
            return f"Me diz o número da opção — {' ou '.join(str(i) for i in range(1, count + 1))}."

        slot = lead.slots_cache[choice - 1]

        try:
            event_id, meet_link = await asyncio.to_thread(
                calendar_client.create_booking,
                lead.name, lead.email, lead.id,
                slot["start_iso"], slot["end_iso"],
                lead.pain or "",
            )
        except Exception as exc:
            logger.error("[scheduling] create_booking failed: %s", exc)
            return "Tive um problema ao confirmar. Me diz a opção de horário novamente?"

        lead.booking_id = event_id
        lead.meeting_at = slot["start_iso"]
        lead.scheduling_step = "confirmed"
        lead.state = "QUALIFIED"

        # Notify Miguel
        if MIGUEL_PHONE:
            pain_clean = re.sub(r"[*_\[\]`]", "", lead.pain or "não identificada")[:200]
            summary = "\n".join([
                "📅 *Briefing agendado*",
                "",
                f"*Lead:* {lead.name}",
                f"*Número:* {lead.id}",
                f"*E-mail:* {lead.email}",
                f"*Horário:* {slot['label']}",
                f"*Necessidade:* {pain_clean}",
                f"*Meet:* {meet_link or 'pendente'}",
            ])
            try:
                await evolution.send_text(MIGUEL_PHONE, summary)
            except Exception as exc:
                logger.error("[scheduling] Failed to notify Miguel: %s", exc)

        meet_info = f"\n\nLink da reunião: {meet_link}" if meet_link else ""
        return (
            f"Agendado! Briefing {slot['label']} com o Miguel. "
            f"Você vai receber o convite no e-mail {lead.email}.{meet_info}"
        )

    # ── Confirmed: nurturing handled by post-qualify skill ───────────────────
    return None


async def _trigger_handoff(
    lead: Lead,
    phone: str,
    remote_jid: str,
    evolution: EvolutionClient,
) -> None:
    await evolution.send_text(remote_jid, "Deixa eu chamar o Miguel diretamente, um segundo.")

    if MIGUEL_PHONE:
        # H7: Sanitize pain field — strip markdown, limit length
        pain_raw = lead.pain or "não identificada ainda"
        pain = re.sub(r"[*_\[\]`]", "", pain_raw)[:200].replace("\n", " ")
        summary = "\n".join([
            "🔔 *Novo lead para você fechar*",
            "",
            f"*Contato:* {lead.name}",
            f"*Número:* {phone}",
            f"*Dor revelada (frase do lead):* {pain}",
            f"*Mensagens trocadas:* {lead.message_count}",
            f"*Estado anterior:* {lead.state}",
            "",
            "Responda diretamente nesse número.",
        ])
        try:
            await evolution.send_text(MIGUEL_PHONE, summary)
            logger.info("[handoff] Miguel notified about lead %s", lead.name[:20])
        except Exception as exc:
            logger.error("[handoff] Failed to notify Miguel: %s", exc)
    else:
        logger.warning("[handoff] MIGUEL_PHONE not set")

    lead.state = "HUMAN_HANDOFF"
    lead.handoff_sent = True
    lead_mgr.store.save(lead)


# ── QR Code ───────────────────────────────────────────────────────────────────

@app.get("/qrcode")
async def qrcode(apikey: str = Header(default="", alias="apikey")):
    _check_auth(apikey)
    if last_qr is None:
        return JSONResponse(status_code=404, content={"error": "QR code not available yet"})
    return {"qrcode": last_qr}


# ── Outbound ──────────────────────────────────────────────────────────────────

@app.post("/outbound")
async def outbound(request: Request, apikey: str = Header(default="", alias="apikey")):
    _check_auth(apikey)

    body = await request.json()
    phone: str = body.get("phone", "")
    business_name: str = body.get("businessName", "")

    # C5: Validate phone (digits only, 10-15 chars)
    if not re.match(r"^\d{10,15}$", phone):
        return JSONResponse(status_code=400, content={"error": "phone must be 10-15 digits only"})
    if not business_name:
        return JSONResponse(status_code=400, content={"error": "Required: businessName"})

    # C2: Sanitize business_name against prompt injection
    business_name = re.sub(r"[\[\]\n\r]", " ", business_name[:100]).strip()

    evolution = get_evolution_client()
    try:
        await _initiate_outbound(phone, business_name, evolution)
        return {"ok": True, "message": f"Vitor initiated with {business_name} ({_mask(phone)})"}
    except Exception as exc:
        logger.error("[outbound] Error: %s", exc)
        return JSONResponse(status_code=500, content={"error": str(exc)})


@app.post("/outbound/bulk")
async def outbound_bulk(request: Request, apikey: str = Header(default="", alias="apikey")):
    _check_auth(apikey)

    body = await request.json()
    leads: list[dict] = body.get("leads") or []
    if not leads:
        return JSONResponse(status_code=400, content={"error": "Required: leads (array)"})

    async def _bulk():
        evolution = get_evolution_client()
        for item in leads:
            p = item.get("phone", "")
            bn = item.get("businessName", "")
            if not re.match(r"^\d{10,15}$", p):
                logger.warning("[bulk] Invalid phone skipped")
                continue
            bn = re.sub(r"[\[\]\n\r]", " ", bn[:100]).strip()
            try:
                await _initiate_outbound(p, bn, evolution)
                await asyncio.sleep(2.5)
            except Exception as exc:
                logger.error("[bulk] Error for %s: %s", _mask(p), exc)
        logger.info("[bulk] Done: %d leads", len(leads))

    asyncio.create_task(_bulk())
    return {"ok": True, "message": f"Processing {len(leads)} leads in background..."}


async def _initiate_outbound(phone: str, business_name: str, evolution: EvolutionClient) -> None:
    lead = lead_mgr.create_outbound(phone, business_name)
    if lead is None:
        return

    seed = f'[SISTEMA] Inicie a prospecção com o responsável da empresa <empresa>{business_name}</empresa>. Gere apenas a primeira mensagem de abertura.'
    seed_messages = [{"role": "user", "content": seed}]
    lead.messages = seed_messages
    try:
        opening = await agent_core.chat(lead, seed)
    except Exception as exc:
        logger.error("[outbound] LLM error for %s: %s", _mask(phone), exc)
        return

    lead.messages = [{"role": "model", "content": opening}]
    lead.message_count = 1
    lead_mgr.store.save(lead)
    await evolution.send_text(phone, opening)
    logger.info("[outbound] Vitor initiated with %s (%s)", business_name[:30], _mask(phone))


# ── Admin ─────────────────────────────────────────────────────────────────────

@app.delete("/admin/lead/{phone}")
async def admin_delete_lead(phone: str, apikey: str = Header(default="", alias="apikey")):
    _check_auth(apikey)
    path = lead_mgr.store._path(phone)
    existed = path.exists()
    if existed:
        path.unlink(missing_ok=True)
        logger.info("[admin] Lead deleted: %s", _mask(phone))
    return {"ok": True, "existed": existed}


@app.get("/admin/lead/{phone}")
async def admin_get_lead(phone: str, apikey: str = Header(default="", alias="apikey")):
    _check_auth(apikey)
    lead = lead_mgr.store.get(phone)
    if lead is None:
        return JSONResponse(status_code=404, content={"error": "Lead not found"})
    d = lead.to_dict()
    d["messages"] = []  # never expose message history via admin API
    return d


@app.get("/admin/leads")
async def admin_list_leads(apikey: str = Header(default="", alias="apikey")):
    _check_auth(apikey)
    data_dir = lead_mgr.store._path("x").parent
    results = []
    for f in sorted(data_dir.glob("*.json")):
        try:
            d = json.loads(f.read_text())
            results.append({
                "phone": d.get("id", f.stem),
                "name": d.get("name", ""),
                "state": d.get("state", ""),
                "message_count": d.get("messageCount", 0),
                "last_seen_at": d.get("lastSeenAt", ""),
            })
        except Exception:
            continue
    return results


# ── Dedup helpers ─────────────────────────────────────────────────────────────

def _clean_dedup() -> None:
    now = time.monotonic()
    if len(_processed_ids) > _MAX_DEDUP:
        cutoff = now - _MSG_TTL
        for k in [k for k, t in _processed_ids.items() if t < cutoff]:
            del _processed_ids[k]
    else:
        for k in [k for k, t in _processed_ids.items() if now - t > _MSG_TTL]:
            del _processed_ids[k]


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, log_level="info")
