# Spec: Hermes — Audio Dedup Fix

**Status:** Aprovado para implementação
**Data:** 2026-04-21
**Prioridade:** Alta — bloqueia UX de prospecção outbound

## Problema

Evolution API envia webhooks duplicados para mensagens de áudio (mesmo áudio, `key.id` diferente).
O content-dedup (camada 2) protege mensagens de texto, mas **não** protege o path de áudio.

Resultado: o mesmo áudio dispara duas chamadas STT → duas respostas idênticas para o lead.

## Comportamento Esperado (Acceptance Criteria)

| # | Cenário | Resultado esperado |
|---|---------|-------------------|
| AC1 | Áudio transcrito chega duplicado dentro de 10s | Segundo webhook ignorado (log "Audio content-dedup") |
| AC2 | Áudio transcrito chega duplicado após 10s | Segundo webhook processado normalmente (TTL expirado) |
| AC3 | Dois áudios diferentes do mesmo telefone | Ambos processados |
| AC4 | STT falha → sem transcrição | Sem registro no dedup (nada para deduplicar) |
| AC5 | Áudio único (sem duplicata) | Processado normalmente, sem efeito colateral |

## Solução

No path de áudio em `_process_message()`, após STT bem-sucedido, aplicar
`_content_dedup_check(phone, text)` **antes** de chamar `_handle()`.

Se dedup retornar `True`, logar e retornar sem enviar resposta.

## Arquivos afetados

- `zvision-wa/hermes-agent/main.py` — inserir dedup check no audio path
- `zvision-wa/hermes-agent/tests/test_audio_dedup.py` — harness (novo)

## Invariante crítica

O dedup NÃO deve ser aplicado antes do STT — só após transcrição.
Áudios com falha de STT não devem contaminar o cache de dedup.
