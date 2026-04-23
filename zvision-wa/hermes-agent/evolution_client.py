"""Evolution API client — port of evolution-client.ts."""
from __future__ import annotations

import logging
import os
from typing import Any, Optional

import httpx

logger = logging.getLogger(__name__)

TIMEOUT = 10.0


class EvolutionClient:
    def __init__(
        self,
        base_url: str,
        api_key: str,
        instance_name: str,
    ) -> None:
        self._base = base_url.rstrip("/")
        self._headers = {"apikey": api_key, "Content-Type": "application/json"}
        self._instance = instance_name

    async def send_text(self, number: str, text: str) -> None:
        url = f"{self._base}/message/sendText/{self._instance}"
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            resp = await client.post(url, json={"number": number, "text": text}, headers=self._headers)
            resp.raise_for_status()

    async def send_audio(self, number: str, ogg_base64: str) -> None:
        """Send OGG Opus audio as a WhatsApp voice message."""
        url = f"{self._base}/message/sendWhatsAppAudio/{self._instance}"
        payload = {"number": number, "audio": ogg_base64, "encoding": True}
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, json=payload, headers=self._headers)
            resp.raise_for_status()

    async def get_media_base64(self, message_data: dict[str, Any]) -> Optional[str]:
        url = f"{self._base}/chat/getBase64FromMediaMessage/{self._instance}"
        payload = {"message": message_data, "convertToMp4": False}
        try:
            async with httpx.AsyncClient(timeout=TIMEOUT) as client:
                resp = await client.post(url, json=payload, headers=self._headers)
                resp.raise_for_status()
                data = resp.json()
                return data.get("base64") or None
        except Exception as exc:
            logger.error("[evolution] get_media_base64 failed: %s", exc)
            return None

    async def get_qrcode(self) -> Optional[str]:
        url = f"{self._base}/instance/connect/{self._instance}"
        try:
            async with httpx.AsyncClient(timeout=TIMEOUT) as client:
                resp = await client.get(url, headers=self._headers)
                resp.raise_for_status()
                data = resp.json()
                return data.get("base64") or data.get("qrcode") or data.get("code")
        except Exception as exc:
            logger.error("[evolution] get_qrcode failed: %s", exc)
            return None

    async def create_instance(self) -> None:
        url = f"{self._base}/instance/create"
        payload = {
            "instanceName": self._instance,
            "qrcode": True,
            "integration": "WHATSAPP-BAILEYS",
        }
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            try:
                resp = await client.post(url, json=payload, headers=self._headers)
                if resp.status_code in (400, 403, 409):
                    logger.info("[evolution] Instance already exists")
                    return
                resp.raise_for_status()
                logger.info("[evolution] Instance '%s' created", self._instance)
            except httpx.HTTPStatusError:
                raise

    async def register_webhook(self, webhook_url: str, port: int, secret: str = "") -> None:
        url = f"{self._base}/webhook/set/{self._instance}"
        webhook_cfg: dict = {
            "enabled": True,
            "url": webhook_url,
            "webhook_by_events": False,
            "webhook_base64": True,
            "events": ["MESSAGES_UPSERT", "CONNECTION_UPDATE", "QRCODE_UPDATED"],
        }
        # Send secret as apikey header so our /webhook endpoint can authenticate it
        if secret:
            webhook_cfg["headers"] = {"apikey": secret}
        payload = {"webhook": webhook_cfg}
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            resp = await client.post(url, json=payload, headers=self._headers)
            resp.raise_for_status()
            logger.info("[evolution] Webhook registered: %s", webhook_url)


def get_evolution_client() -> EvolutionClient:
    return EvolutionClient(
        base_url=os.getenv("EVOLUTION_BASE_URL", "http://evolution:8080"),
        api_key=os.getenv("EVOLUTION_API_KEY", ""),
        instance_name=os.getenv("EVOLUTION_INSTANCE_NAME", "zvision-sdr"),
    )
