"""Groq Whisper STT — resiliente com retry em 429."""
from __future__ import annotations

import asyncio
import base64
import io
import logging
import os

import httpx

logger = logging.getLogger(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_WHISPER_URL = "https://api.groq.com/openai/v1/audio/transcriptions"
_MAX_RETRIES = 2
_RETRY_DELAY = 3.0


async def transcribe_audio(base64_audio: str) -> str | None:
    """
    Transcreve áudio OGG/Opus base64 (formato WhatsApp) para texto em português.
    Retry automático em 429. Retorna None se falhar após todas as tentativas.
    """
    if not GROQ_API_KEY:
        logger.warning("[stt] GROQ_API_KEY não configurada")
        return None

    try:
        audio_bytes = base64.b64decode(base64_audio)
    except Exception as exc:
        logger.error("[stt] base64 inválido: %s", exc)
        return None

    logger.info("[stt] Transcrevendo %d bytes de áudio", len(audio_bytes))

    for attempt in range(_MAX_RETRIES):
        try:
            files = {
                "file": ("audio.ogg", io.BytesIO(audio_bytes), "audio/ogg"),
                "model": (None, "whisper-large-v3-turbo"),
                "language": (None, "pt"),
                "response_format": (None, "text"),
            }
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}

            async with httpx.AsyncClient(timeout=30.0) as client:
                resp = await client.post(GROQ_WHISPER_URL, headers=headers, files=files)

            if resp.status_code == 429:
                logger.warning("[stt] Groq 429 rate limit (tentativa %d/%d)", attempt + 1, _MAX_RETRIES)
                if attempt < _MAX_RETRIES - 1:
                    await asyncio.sleep(_RETRY_DELAY)
                    continue
                logger.error("[stt] Groq 429 após %d tentativas — desistindo", _MAX_RETRIES)
                return None

            if not resp.is_success:
                logger.error("[stt] Groq erro %d: %s", resp.status_code, resp.text[:200])
                return None

            text = resp.text.strip()
            if not text:
                logger.warning("[stt] Groq retornou transcrição vazia")
                return None

            logger.info("[stt] Transcrito (%d chars): \"%s...\"", len(text), text[:60])
            return text

        except Exception as exc:
            logger.error("[stt] Erro na tentativa %d: %s", attempt + 1, exc)
            if attempt < _MAX_RETRIES - 1:
                await asyncio.sleep(_RETRY_DELAY)
            else:
                return None

    return None
