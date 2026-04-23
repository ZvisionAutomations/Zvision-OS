"""
Harness — AC1..AC5 para audio content-dedup (spec hermes-audio-dedup-fix.md)
Roda com: pytest tests/test_audio_dedup.py -v
"""
import asyncio
import base64
import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

FAKE_BASE64 = base64.b64encode(b"fake ogg data").decode()
FAKE_PHONE = "5511999990099"


def _reset_content_dedup():
    import main
    main._processed_content.clear()


class TestAudioDedup:

    @pytest.mark.asyncio
    async def test_ac1_duplicate_audio_within_ttl_ignored(self):
        """AC1: mesmo áudio transcrito dentro de 10s — segundo ignorado."""
        _reset_content_dedup()
        send_calls = []

        async def fake_send_text(number, text):
            send_calls.append(text)

        mock_evolution = AsyncMock()
        mock_evolution.send_text = fake_send_text
        mock_evolution.get_media_base64 = AsyncMock(return_value=None)

        with patch("main.get_evolution_client", return_value=mock_evolution), \
             patch("main.transcribe_audio", new_callable=AsyncMock, return_value="Quero saber sobre o serviço"), \
             patch("main._handle", new_callable=AsyncMock) as mock_handle, \
             patch("main.WEBHOOK_SECRET", ""):

            import main
            # Primeira chamada
            await main._process_message(FAKE_PHONE, f"{FAKE_PHONE}@s.whatsapp.net", "Lead", "audioMessage", {}, FAKE_BASE64)
            # Segunda chamada idêntica — deve ser ignorada
            await main._process_message(FAKE_PHONE, f"{FAKE_PHONE}@s.whatsapp.net", "Lead", "audioMessage", {}, FAKE_BASE64)

        assert mock_handle.call_count == 1, f"Esperado 1 chamada a _handle, got {mock_handle.call_count}"

    @pytest.mark.asyncio
    async def test_ac2_duplicate_audio_after_ttl_processed(self):
        """AC2: mesmo áudio transcrito após TTL expirado — segundo processado."""
        _reset_content_dedup()

        with patch("main.get_evolution_client", return_value=AsyncMock()), \
             patch("main.transcribe_audio", new_callable=AsyncMock, return_value="Quero saber sobre o serviço"), \
             patch("main._handle", new_callable=AsyncMock) as mock_handle, \
             patch("main.WEBHOOK_SECRET", ""), \
             patch("main._CONTENT_DEDUP_TTL", 0.05):  # 50ms TTL para o teste

            import main
            await main._process_message(FAKE_PHONE, f"{FAKE_PHONE}@s.whatsapp.net", "Lead", "audioMessage", {}, FAKE_BASE64)
            await asyncio.sleep(0.1)  # espera TTL expirar
            await main._process_message(FAKE_PHONE, f"{FAKE_PHONE}@s.whatsapp.net", "Lead", "audioMessage", {}, FAKE_BASE64)

        assert mock_handle.call_count == 2, "Após TTL expirar, segundo áudio deve ser processado"

    @pytest.mark.asyncio
    async def test_ac3_different_audios_both_processed(self):
        """AC3: dois áudios diferentes do mesmo telefone — ambos processados."""
        _reset_content_dedup()

        transcriptions = ["Primeira mensagem de áudio", "Segunda mensagem diferente"]
        call_idx = 0

        async def rotating_transcribe(_):
            nonlocal call_idx
            t = transcriptions[call_idx % len(transcriptions)]
            call_idx += 1
            return t

        with patch("main.get_evolution_client", return_value=AsyncMock()), \
             patch("main.transcribe_audio", side_effect=rotating_transcribe), \
             patch("main._handle", new_callable=AsyncMock) as mock_handle, \
             patch("main.WEBHOOK_SECRET", ""):

            import main
            await main._process_message(FAKE_PHONE, f"{FAKE_PHONE}@s.whatsapp.net", "Lead", "audioMessage", {}, FAKE_BASE64)
            await main._process_message(FAKE_PHONE, f"{FAKE_PHONE}@s.whatsapp.net", "Lead", "audioMessage", {}, FAKE_BASE64)

        assert mock_handle.call_count == 2, "Áudios diferentes devem ambos chegar a _handle"

    @pytest.mark.asyncio
    async def test_ac4_stt_failure_no_dedup_entry(self):
        """AC4: STT falha → nada é registrado no cache de dedup."""
        _reset_content_dedup()

        with patch("main.get_evolution_client", return_value=AsyncMock()), \
             patch("main.transcribe_audio", new_callable=AsyncMock, return_value=None), \
             patch("main._handle", new_callable=AsyncMock) as mock_handle, \
             patch("main.WEBHOOK_SECRET", ""):

            import main
            await main._process_message(FAKE_PHONE, f"{FAKE_PHONE}@s.whatsapp.net", "Lead", "audioMessage", {}, FAKE_BASE64)

        import main
        assert len(main._processed_content) == 0, "Falha de STT não deve popular o cache de dedup"
        assert mock_handle.call_count == 0

    @pytest.mark.asyncio
    async def test_ac5_single_audio_processed_normally(self):
        """AC5: áudio único (sem duplicata) — processado normalmente."""
        _reset_content_dedup()

        with patch("main.get_evolution_client", return_value=AsyncMock()), \
             patch("main.transcribe_audio", new_callable=AsyncMock, return_value="Tenho interesse"), \
             patch("main._handle", new_callable=AsyncMock) as mock_handle, \
             patch("main.WEBHOOK_SECRET", ""):

            import main
            await main._process_message(FAKE_PHONE, f"{FAKE_PHONE}@s.whatsapp.net", "Lead", "audioMessage", {}, FAKE_BASE64)

        assert mock_handle.call_count == 1
