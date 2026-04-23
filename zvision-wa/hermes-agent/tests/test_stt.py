"""
Harness — AC1..AC5 para STT resiliente (spec hermes-stt-fix.md)
Roda com: pytest tests/test_stt.py -v
"""
import asyncio
import base64
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest


FAKE_BASE64 = base64.b64encode(b"fake ogg audio data").decode()


def _mock_response(status: int, text: str) -> MagicMock:
    resp = MagicMock()
    resp.status_code = status
    resp.text = text
    resp.is_success = (200 <= status < 300)
    return resp


class TestSTT:

    @pytest.mark.asyncio
    async def test_ac2_retry_on_429(self):
        """AC2: Groq 429 → retry após 3s, máximo 2 tentativas."""
        responses = [
            _mock_response(429, "rate limit"),
            _mock_response(200, "Quero um site"),
        ]
        call_count = 0

        async def fake_post(*args, **kwargs):
            nonlocal call_count
            r = responses[min(call_count, len(responses) - 1)]
            call_count += 1
            return r

        with patch("stt.GROQ_API_KEY", "fake-key"), \
             patch("httpx.AsyncClient") as mock_client_cls, \
             patch("asyncio.sleep", new_callable=AsyncMock) as mock_sleep:

            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client.post = fake_post
            mock_client_cls.return_value = mock_client

            from importlib import reload
            import stt
            result = await stt.transcribe_audio(FAKE_BASE64)

        assert result == "Quero um site"
        assert call_count == 2, "Deve ter feito exatamente 2 chamadas (1 retry)"
        mock_sleep.assert_called_once()

    @pytest.mark.asyncio
    async def test_ac3_other_http_error_no_retry(self):
        """AC3: Groq 500 → sem retry, retorna None."""
        call_count = 0

        async def fake_post(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            return _mock_response(500, "internal server error")

        with patch("stt.GROQ_API_KEY", "fake-key"), \
             patch("httpx.AsyncClient") as mock_client_cls:

            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client.post = fake_post
            mock_client_cls.return_value = mock_client

            import stt
            result = await stt.transcribe_audio(FAKE_BASE64)

        assert result is None
        assert call_count == 1, "Erro 500 não deve gerar retry"

    @pytest.mark.asyncio
    async def test_ac4_empty_transcription_returns_none(self):
        """AC4: Groq retorna string vazia → None."""
        async def fake_post(*args, **kwargs):
            return _mock_response(200, "   ")

        with patch("stt.GROQ_API_KEY", "fake-key"), \
             patch("httpx.AsyncClient") as mock_client_cls:

            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client.post = fake_post
            mock_client_cls.return_value = mock_client

            import stt
            result = await stt.transcribe_audio(FAKE_BASE64)

        assert result is None

    @pytest.mark.asyncio
    async def test_ac5_no_api_key_returns_none(self):
        """AC5: sem GROQ_API_KEY → retorna None sem chamar API."""
        with patch("stt.GROQ_API_KEY", ""):
            import stt
            result = await stt.transcribe_audio(FAKE_BASE64)

        assert result is None
