# Spec: Hermes — Deduplicação de Webhooks Duplicados

**Status:** Aprovado para implementação
**Data:** 2026-04-21
**Prioridade:** Crítica — afeta toda conversa de vendas

## Problema

Para cada mensagem recebida, o Hermes envia 2–3 respostas ao lead.
Evolution API envia múltiplos webhooks com `key.id` distintos para o mesmo evento.
O dedup atual usa apenas `msg_id`, que não cobre esse caso.

## Causa Raiz

Evolution gera IDs diferentes para o mesmo evento em dois cenários:
1. Retry automático após timeout do webhook
2. Atualização de status da mensagem emitida como `messages.upsert`

## Comportamento Esperado (Acceptance Criteria)

| # | Cenário | Resultado esperado |
|---|---------|-------------------|
| AC1 | 2 webhooks, mesmo conteúdo, IDs diferentes, < 10s | 1 resposta enviada |
| AC2 | 2 webhooks, conteúdo diferente, IDs diferentes | 2 respostas enviadas |
| AC3 | Mesmo conteúdo, > 10s de intervalo | 2 respostas enviadas (resend legítimo) |
| AC4 | `fromMe=true` em qualquer webhook | 0 respostas (ignorado) |
| AC5 | Webhook com `event != messages.upsert` | 0 respostas (ignorado) |

## Solução

Dedup em duas camadas:
1. **Camada 1 (existente):** `msg_id` — mantém como está
2. **Camada 2 (nova):** hash de `phone + texto_normalizado` com janela de **10 segundos**

```
content_key = hash(phone + normalize(text))
window = 10 segundos
```

Se o mesmo `content_key` chegar dentro da janela → ignorar.
Se chegar após 10s → processar (resend legítimo do usuário).

## Não está no escopo

- Dedup de áudios (content-hash de base64 seria caro)
- Dedup de imagens
- Alteração no fluxo de SCHEDULING

## Arquivos afetados

- `zvision-wa/hermes-agent/main.py` — função `webhook()` e estruturas de dedup
- `zvision-wa/hermes-agent/tests/test_dedup.py` — harness de testes (novo)
