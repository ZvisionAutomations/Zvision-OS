"""AWS Polly TTS provider — PT-BR Neural voices, OGG Opus output for WhatsApp."""
from __future__ import annotations

import asyncio
import base64
import logging
import os
import re
import subprocess
import tempfile
from typing import Optional

logger = logging.getLogger(__name__)

TTS_ENABLED = os.getenv("AWS_ACCESS_KEY_ID", "") != ""
POLLY_VOICE_ID = os.getenv("POLLY_VOICE_ID", "Camila")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# PT-BR Neural voices available in AWS Polly
_PT_BR_VOICES = {"Camila", "Ricardo", "Vitoria", "Thiago"}


class PollyTTSProvider:
    """
    AWS Polly TTS → OGG Opus pipeline.
    Uses Neural engine for natural PT-BR speech.
    Converts MP3 → OGG Opus via ffmpeg (required for WhatsApp voice messages).
    """

    def __init__(self) -> None:
        self._client: object | None = None

    def _get_client(self) -> object:
        if self._client is None:
            import boto3
            self._client = boto3.client(
                "polly",
                region_name=AWS_REGION,
                aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            )
        return self._client

    async def synthesize(self, text: str) -> Optional[str]:
        """Return base64 OGG Opus string, or None on failure."""
        if not TTS_ENABLED:
            return None
        cleaned = self._clean_text(text)
        if not cleaned:
            return None

        loop = asyncio.get_event_loop()
        try:
            mp3_bytes = await loop.run_in_executor(None, self._call_polly, cleaned)
            if not mp3_bytes:
                return None
            return await loop.run_in_executor(None, self._mp3_to_ogg_base64, mp3_bytes)
        except Exception as exc:
            logger.error("[tts_polly] Error: %s", exc)
            return None

    def _call_polly(self, text: str) -> Optional[bytes]:
        from botocore.exceptions import BotoCoreError, ClientError
        client = self._get_client()
        try:
            resp = client.synthesize_speech(  # type: ignore[attr-defined]
                Text=text,
                OutputFormat="mp3",
                VoiceId=POLLY_VOICE_ID,
                Engine="neural",
                LanguageCode="pt-BR",
                TextType="text",
            )
            stream = resp.get("AudioStream")
            return stream.read() if stream else None
        except (BotoCoreError, ClientError) as exc:
            logger.error("[tts_polly] AWS error: %s", exc)
            return None

    @staticmethod
    def _mp3_to_ogg_base64(mp3_bytes: bytes) -> Optional[str]:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            f.write(mp3_bytes)
            mp3_path = f.name
        ogg_path = mp3_path.replace(".mp3", ".ogg")
        try:
            result = subprocess.run(
                [
                    "ffmpeg", "-y", "-i", mp3_path,
                    "-c:a", "libopus", "-b:a", "32k",
                    "-vbr", "on", "-application", "voip",
                    ogg_path,
                ],
                capture_output=True,
                timeout=15,
            )
            if result.returncode != 0:
                logger.error("[tts_polly] ffmpeg failed: %s", result.stderr.decode(errors="replace")[:200])
                return None
            with open(ogg_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except subprocess.TimeoutExpired:
            logger.error("[tts_polly] ffmpeg timed out")
            return None
        except FileNotFoundError:
            logger.error("[tts_polly] ffmpeg not found")
            return None
        finally:
            for p in (mp3_path, ogg_path):
                try:
                    os.unlink(p)
                except OSError:
                    pass

    @staticmethod
    def _clean_text(text: str) -> str:
        text = re.sub(r"\*([^*]+)\*", r"\1", text)
        text = re.sub(r"_([^_]+)_", r"\1", text)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        text = re.sub(r"https?://\S+", "o link", text)
        text = re.sub(
            r"[\U0001F300-\U0001FFFF\U00002600-\U000027BF\U0001F900-\U0001F9FF]",
            "",
            text,
        )
        text = re.sub(r"\s+", " ", text).strip()
        return text[:2900]


_provider: Optional[PollyTTSProvider] = None


def get_polly_provider() -> PollyTTSProvider:
    global _provider
    if _provider is None:
        _provider = PollyTTSProvider()
    return _provider


async def text_to_speech(text: str) -> Optional[str]:
    """Synthesize text to OGG Opus base64. Returns None if TTS unavailable."""
    return await get_polly_provider().synthesize(text)
