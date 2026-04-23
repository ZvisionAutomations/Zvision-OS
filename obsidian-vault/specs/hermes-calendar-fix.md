# Spec: Hermes — Calendar Booking sem conferenceData

**Status:** Aprovado para implementação
**Data:** 2026-04-21
**Prioridade:** Alta — bloqueia agendamento de calls

## Problema

`create_booking()` falha com HTTP 400 `Invalid conference type value`.

Service accounts em Gmail pessoal não podem criar Google Meet links.
`hangoutsMeet` requer Domain-Wide Delegation, disponível apenas em Google Workspace.

## Comportamento Esperado (Acceptance Criteria)

| # | Cenário | Resultado esperado |
|---|---------|-------------------|
| AC1 | Booking chamado com email + slot válido | Evento criado no Google Calendar sem erro |
| AC2 | `meet_link` retornado | `None` (sem Meet link — limitação do Gmail pessoal) |
| AC3 | Mensagem ao lead | "Agendado! Briefing [slot] com o Miguel. Você vai receber confirmação." |
| AC4 | Notificação para Miguel | Enviada via WhatsApp com dados do lead |
| AC5 | Evento visível no Calendar | Sim, com nome/telefone/dor do lead na descrição |

## Solução

Remover `conferenceData` do corpo do evento e ajustar `conferenceDataVersion=0`.
O `meet_link` fica `None` — a mensagem de confirmação já trata esse caso.

Se quiser Meet link no futuro: migrar para OAuth2 com refresh token do dono do calendário.

## Arquivos afetados

- `zvision-wa/hermes-agent/calendar_client.py` — remover conferenceData
- `zvision-wa/hermes-agent/tests/test_calendar.py` — harness (novo)
