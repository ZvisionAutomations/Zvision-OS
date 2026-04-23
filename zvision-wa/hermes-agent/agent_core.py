"""
HERMES Agent Core — multi-provider LLM with SOUL.md + skills + knowledge context.

Architecture inspired by NousResearch/hermes-agent:
  - SOUL.md defines the master persona
  - Skills (SKILL.md files) define specialized procedures (BDR, SDR)
  - KnowledgeBase injects relevant PDF context per message
  - Per-lead session management (session_id = phone number)

LLM routing: OpenRouter primary → Groq fallback.
"""
from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Optional

import httpx

from knowledge import KnowledgeBase, get_knowledge_base
from lead_memory import Lead, LeadState

logger = logging.getLogger(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# Models tried in order — vision models first when image is present
_OR_MODELS_TEXT = [
    "meta-llama/llama-3.3-70b-instruct:free",
    "google/gemma-4-31b-it:free",
    "google/gemma-4-26b-a4b-it:free",
]
_OR_MODELS_VISION = [
    "google/gemma-4-31b-it:free",
    "google/gemma-4-26b-a4b-it:free",
]
_GROQ_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
]

_SOUL_PATH = Path(os.getenv("SOUL_PATH", "/opt/hermes/SOUL.md"))
_SKILLS_DIR = Path(os.getenv("SKILLS_DIR", "/opt/hermes/skills"))


def _load_soul() -> str:
    try:
        return _SOUL_PATH.read_text()
    except FileNotFoundError:
        logger.warning("[agent] SOUL.md not found at %s", _SOUL_PATH)
        return "Você é um agente de vendas da Zvision Automations."


def _load_skill(state: LeadState) -> str:
    skill_map = {
        "VITOR_ACTIVE": "bdr-prospect",
        "ANA_ACTIVE": "sdr-qualify",
        "SCHEDULING": "meeting-scheduler",
        "QUALIFIED": "post-qualify",
    }
    slug = skill_map.get(state)
    if not slug:
        return ""
    skill_path = _SKILLS_DIR / slug / "SKILL.md"
    try:
        return skill_path.read_text()
    except FileNotFoundError:
        logger.warning("[agent] Skill not found: %s", skill_path)
        return ""


def build_system_prompt(
    soul: str,
    lead: Lead,
    kb_context: str,
) -> str:
    skill = _load_skill(lead.state)
    parts = [soul]

    # Current skill instructions
    if skill:
        parts.append("\n\n---\n" + skill)

    # Lead context
    lead_ctx = [f"\n\n[CONTEXTO DO LEAD]\nNome/Empresa: {lead.name}"]
    if lead.message_count > 0:
        lead_ctx.append(f"Histórico: {lead.message_count} mensagem(ns) trocada(s)")
    if lead.pain:
        lead_ctx.append(f'Dor identificada: "{lead.pain}"')
    if lead.summary:
        lead_ctx.append(f"Resumo da conversa anterior: {lead.summary}")
    lead_ctx.append(f"Estado atual: {lead.state}")
    parts.append("\n".join(lead_ctx))

    # KB knowledge injection
    if kb_context:
        parts.append(f"\n\n{kb_context}")

    return "\n".join(parts)


async def ask_llm(
    system_prompt: str,
    messages: list[dict],
    image_base64: Optional[str] = None,
    image_mime: Optional[str] = None,
) -> str:
    """
    Call LLM with multi-provider fallback: OpenRouter → Groq.
    Retries the full chain once (after 4s) before giving up.
    """
    import asyncio

    if image_base64:
        return await _call_openrouter(
            system_prompt, messages,
            models=_OR_MODELS_VISION,
            image_base64=image_base64,
            image_mime=image_mime,
        )

    for attempt in range(2):
        try:
            if OPENROUTER_API_KEY:
                try:
                    return await _call_openrouter(system_prompt, messages, models=_OR_MODELS_TEXT)
                except Exception as exc:
                    logger.warning("[agent] OpenRouter failed (%s), trying Groq...", exc)

            if GROQ_API_KEY:
                return await _call_groq(system_prompt, messages)

            raise RuntimeError("No LLM provider available")

        except Exception as exc:
            if attempt == 0:
                logger.warning("[agent] All providers failed, retrying in 4s... (%s)", exc)
                await asyncio.sleep(4)
            else:
                raise


async def _call_openrouter(
    system_prompt: str,
    history: list[dict],
    models: list[str],
    image_base64: Optional[str] = None,
    image_mime: Optional[str] = None,
) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/ZvisionAutomations/Zvision-OS",
        "X-Title": "Zvision HERMES Agent",
    }

    for model in models:
        msgs = _build_messages(system_prompt, history, image_base64, image_mime)
        payload = {"model": model, "messages": msgs, "temperature": 0.65, "max_tokens": 300, "top_p": 0.9}
        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                resp = await client.post(OPENROUTER_URL, json=payload, headers=headers)

            if resp.status_code in (429, 503):
                continue
            if resp.status_code == 404:
                continue
            if resp.status_code == 400:
                err = resp.text
                if "instruction is not enabled" in err:
                    continue
                raise RuntimeError(f"OpenRouter/{model}: HTTP 400 — {err[:200]}")

            resp.raise_for_status()
            text = resp.json()["choices"][0]["message"]["content"]
            if not text:
                raise RuntimeError("empty response")
            logger.info("[agent] OpenRouter/%s", model)
            return text.strip()

        except (httpx.HTTPStatusError, RuntimeError):
            raise
        except Exception as exc:
            logger.warning("[agent] OpenRouter/%s error: %s", model, exc)
            continue

    raise RuntimeError("OpenRouter: all models failed")


async def _call_groq(system_prompt: str, history: list[dict]) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    for model in _GROQ_MODELS:
        msgs = _build_messages(system_prompt, history)
        payload = {"model": model, "messages": msgs, "temperature": 0.65, "max_tokens": 300, "top_p": 0.9}
        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                resp = await client.post(GROQ_URL, json=payload, headers=headers)

            if resp.status_code in (429, 503):
                import asyncio
                await asyncio.sleep(2)
                continue

            resp.raise_for_status()
            text = resp.json()["choices"][0]["message"]["content"]
            if not text:
                raise RuntimeError("empty response")
            logger.info("[agent] Groq/%s", model)
            return text.strip()

        except Exception as exc:
            logger.warning("[agent] Groq/%s error: %s", model, exc)
            continue

    raise RuntimeError("Groq: all models failed")


def _build_messages(
    system_prompt: str,
    history: list[dict],
    image_base64: Optional[str] = None,
    image_mime: Optional[str] = None,
) -> list[dict]:
    msgs: list[dict] = [{"role": "system", "content": system_prompt}]
    for i, m in enumerate(history):
        role = "assistant" if m.get("role") == "model" else "user"
        if image_base64 and role == "user" and i == len(history) - 1:
            msgs.append({
                "role": role,
                "content": [
                    {"type": "text", "text": m.get("content", "") or "[imagem]"},
                    {"type": "image_url", "image_url": {"url": f"data:{image_mime or 'image/jpeg'};base64,{image_base64}"}},
                ],
            })
        else:
            content = m.get("content", "")
            # Wrap user content to prevent prompt injection (C2)
            if role == "user":
                content = f"<user_message>{content}</user_message>"
            msgs.append({"role": role, "content": content})
    return msgs


# ── High-level chat function used by main.py ─────────────────────────────────

_soul: str | None = None
_kb: KnowledgeBase | None = None


async def chat(
    lead: Lead,
    text: str,
    image_base64: Optional[str] = None,
    image_mime: Optional[str] = None,
) -> str:
    global _soul, _kb

    if _soul is None:
        _soul = _load_soul()

    if _kb is None:
        _kb = get_knowledge_base()
        await _kb.load()

    kb_chunks = _kb.search(text)
    logger.info("[kb] %d chunks encontrados para: %.40s", len(kb_chunks), text)
    kb_context = _kb.format_context(kb_chunks)
    system_prompt = build_system_prompt(_soul, lead, kb_context)

    response = await ask_llm(
        system_prompt,
        lead.context_messages(),
        image_base64,
        image_mime,
    )
    return response
