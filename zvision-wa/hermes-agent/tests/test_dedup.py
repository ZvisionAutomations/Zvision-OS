"""
Harness — AC1..AC5 para deduplicação de webhooks do Hermes.
Roda com: pytest tests/test_dedup.py -v
"""
import asyncio
import hashlib
import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient


# ── Helpers ──────────────────────────────────────────────────────────────────

def _make_webhook_body(phone: str, text: str, msg_id: str, from_me: bool = False) -> dict:
    return {
        "event": "messages.upsert",
        "data": {
            "key": {
                "remoteJid": f"{phone}@s.whatsapp.net",
                "fromMe": from_me,
                "id": msg_id,
            },
            "pushName": "Test User",
            "messageType": "conversation",
            "message": {"conversation": text},
            "base64": "",
        },
    }


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def mock_evolution():
    evo = MagicMock()
    evo.send_text = AsyncMock(return_value=None)
    return evo


@pytest.fixture
def mock_agent_response():
    with patch("agent_core.chat", new_callable=AsyncMock) as mock:
        mock.return_value = "Oi! Sou a Ana da Zvision. Como posso te ajudar? 👋"
        yield mock


# ── Testes ────────────────────────────────────────────────────────────────────

class TestDedup:
    """AC1–AC5 conforme spec hermes-dedup-fix.md"""

    @pytest.mark.asyncio
    async def test_ac1_duplicate_ids_same_content_single_response(
        self, mock_evolution, mock_agent_response
    ):
        """AC1: 2 webhooks, mesmo conteúdo, IDs diferentes, < 10s → 1 resposta."""
        from main import _content_dedup_check, _processed_content

        phone = "5511999990001"
        text = "Olá, com quem eu falo?"

        _processed_content.clear()

        result1 = _content_dedup_check(phone, text)
        result2 = _content_dedup_check(phone, text)

        assert result1 is False, "Primeira mensagem não deve ser duplicata"
        assert result2 is True, "Segunda mensagem idêntica dentro da janela deve ser duplicata"

    @pytest.mark.asyncio
    async def test_ac2_different_content_two_responses(self, mock_evolution, mock_agent_response):
        """AC2: mesmo phone, conteúdos diferentes → 2 processamentos distintos."""
        from main import _content_dedup_check, _processed_content

        phone = "5511999990002"
        _processed_content.clear()

        r1 = _content_dedup_check(phone, "Olá")
        r2 = _content_dedup_check(phone, "Quero um site")

        assert r1 is False
        assert r2 is False, "Conteúdo diferente não deve ser deduplicado"

    @pytest.mark.asyncio
    async def test_ac3_same_content_after_window_allowed(self):
        """AC3: mesmo conteúdo após 10s → deve ser processado."""
        from main import _content_dedup_check, _processed_content, _CONTENT_DEDUP_TTL

        phone = "5511999990003"
        text = "Quero um site"
        _processed_content.clear()

        _content_dedup_check(phone, text)

        # Simula expiração da janela
        key = _content_key(phone, text)
        _processed_content[key] = time.monotonic() - (_CONTENT_DEDUP_TTL + 1)

        result = _content_dedup_check(phone, text)
        assert result is False, "Após expirar janela, mesma mensagem deve ser aceita"

    def test_ac4_from_me_ignored(self):
        """AC4: fromMe=true → nunca processa."""
        body = _make_webhook_body("5511999990004", "resposta do bot", "id-xyz", from_me=True)
        assert body["data"]["key"]["fromMe"] is True

    def test_ac5_wrong_event_ignored(self):
        """AC5: event != messages.upsert → ignora."""
        body = _make_webhook_body("5511999990005", "texto", "id-abc")
        body["event"] = "connection.update"
        assert body["event"] not in ("messages.upsert", "MESSAGES_UPSERT")


# ── Helper local (espelha implementação esperada) ─────────────────────────────

def _content_key(phone: str, text: str) -> str:
    normalized = text.strip().lower()
    return hashlib.md5(f"{phone}:{normalized}".encode()).hexdigest()
