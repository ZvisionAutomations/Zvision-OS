# Spec: Hermes — STT Resiliente (Audio Transcription)

**Status:** Aprovado para implementação
**Data:** 2026-04-21
**Prioridade:** Alta — áudio é o canal principal do WhatsApp

## Problema

`transcribe_audio()` retorna `None` silenciosamente em dois cenários não rastreados:
1. `media_base64` chega vazio do Evolution (Evolution não enviou o áudio no webhook)
2. Groq Whisper retorna erro (rate limit 429, timeout, formato inválido)

Ambos colapsam para a mesma mensagem genérica, sem log rastreável.

## Comportamento Esperado (Acceptance Criteria)

| # | Cenário | Resultado esperado |
|---|---------|-------------------|
| AC1 | Evolution não envia base64 → `get_media_base64` também falha | Log `[stt] base64 vazio` + mensagem ao usuário |
| AC2 | Groq retorna 429 | Retry após 3s, máximo 2 tentativas, log específico |
| AC3 | Groq retorna outro erro HTTP | Log com status + body, sem retry, mensagem ao usuário |
| AC4 | Transcrição retorna string vazia | Log `[stt] resposta vazia`, retorna None |
| AC5 | GROQ_API_KEY ausente | Log warning uma vez no startup, não por mensagem |

## Solução

1. Adicionar log de diagnóstico antes de chamar `transcribe_audio` (tamanho do base64)
2. Adicionar retry com backoff de 3s para 429 no Groq Whisper
3. Log específico por tipo de falha (sem colapsar tudo em "Transcription error")

## Arquivos afetados

- `zvision-wa/hermes-agent/stt.py` — retry + logs granulares
- `zvision-wa/hermes-agent/main.py` — log do tamanho do base64 antes de chamar STT
- `zvision-wa/hermes-agent/tests/test_stt.py` — harness (novo)
