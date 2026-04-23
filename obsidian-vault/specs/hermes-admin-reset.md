# Spec: Hermes — Admin Lead Reset Endpoint

**Status:** Aprovado para implementação
**Data:** 2026-04-21
**Prioridade:** Alta — Miguel precisa resetar leads sem SSH

## Problema

Quando um lead trava em `HUMAN_HANDOFF` (ou qualquer estado indesejado durante testes),
Miguel precisa de acesso SSH à VPS para fazer o reset via docker exec.

Para a campanha de prospecção amanhã, esse fluxo de operação não é viável em produção.

## Comportamento Esperado (Acceptance Criteria)

| # | Cenário | Resultado esperado |
|---|---------|-------------------|
| AC1 | `DELETE /admin/lead/{phone}` com apikey válida | Lead deletado, HTTP 200 `{"ok": true}` |
| AC2 | `DELETE /admin/lead/{phone}` com apikey inválida | HTTP 401 |
| AC3 | `DELETE /admin/lead/{phone}` — lead não existe | HTTP 200 `{"ok": true, "existed": false}` |
| AC4 | `GET /admin/lead/{phone}` com apikey válida | HTTP 200, JSON com estado atual do lead |
| AC5 | `GET /admin/lead/{phone}` — lead não existe | HTTP 404 |
| AC6 | `GET /admin/leads` com apikey válida | HTTP 200, lista de todos os leads com estado |

## Solução

Três rotas protegidas por `_check_auth(apikey)`:
- `DELETE /admin/lead/{phone}` — deleta o arquivo JSON do lead
- `GET /admin/lead/{phone}` — retorna snapshot do estado
- `GET /admin/leads` — lista todos os leads ativos

## Arquivos afetados

- `zvision-wa/hermes-agent/main.py` — adicionar três rotas /admin
- `zvision-wa/hermes-agent/tests/test_admin_reset.py` — harness (novo)

## Segurança

- Todas as rotas protegidas por `apikey` header (mesma lógica do `_check_auth`)
- Nunca expõe dados além do que já está no lead JSON
- Logs de auditoria para cada operação admin
