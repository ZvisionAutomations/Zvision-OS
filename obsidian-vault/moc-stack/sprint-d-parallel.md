---
name: sprint-d-parallel
description: Sprint D — Paperclip orquestrando squads em paralelo, bridge v2 com /status, start-zvision v2, bloqueio WSL2 documentado
---
# Sprint D — Orquestração Paralela

O [[paperclip]] foi configurado para operar como CEO real da Zvision com org chart
completo: Miguel (Board), CEO ([[squad-c-level]]), CTO ([[squad-dev]]),
CMO ([[squad-commercial]]), CSO ([[squad-cybersecurity]]).
Script pronto em `.paperclip/org-chart-setup.sh` — requer Paperclip online.

## Token Optimization ativo
O [[bridge-http]] v2.0 implementa o padrão [[token-optimization]]
do DomainLabs: [[intent-classifier]] com 22 squads sem tokens gastos na triagem,
scoped skills carregando o contexto só do squad relevante (max 3000 chars),
e context pruning de 3 turns no histórico.
Redução estimada: 70-80% vs carregar todos os 300+ agentes.

Novos endpoints no Sprint D:
- `GET /status` — retorna sistema completo com componentes e otimizações
- `GET /squads/:name` — contexto preview do squad específico

## Primeiro projeto no Paperclip
[[pipeline-outbound-abril-2026]] definido com 3 tickets para squads diferentes:
[[squad-copy]] revisando scripts de cold call para clínicas,
[[squad-commercial]] definindo KPIs da semana 1 do pipeline,
[[squad-design]] criando mockup para reuniões de vendas.
Tickets criáveis via API quando Paperclip estiver online:
`POST http://localhost:3100/api/projects` e `POST http://localhost:3100/api/tickets`.

## Paralelismo — padrão validado
O [[bridge-http]] suporta chamadas simultâneas por design (Node.js event loop).
Teste de 3 squads em paralelo via `/execute` pode ser feito com:
```bash
curl -s -X POST http://localhost:3300/execute \
  -H "Content-Type: application/json" \
  -d '{"task": "revisar script cold call clínicas"}' &

curl -s -X POST http://localhost:3300/execute \
  -H "Content-Type: application/json" \
  -d '{"task": "definir meta prospecção semana 1"}' &

curl -s -X POST http://localhost:3300/execute \
  -H "Content-Type: application/json" \
  -d '{"task": "mockup landing page clínica"}' &
wait
```

## Bloqueio: WSL2 offline
Em 2026-04-04 o WSL2 retornou `REGDB_E_CLASSNOTREG` — distribuição
Ubuntu-Antigravity não registrada. Isso bloqueou:
- Aplicação do org chart via `org-chart-setup.sh`
- Criação do projeto "Outbound Abril 2026" no Paperclip
- Teste de paralelismo real com bridge ativo
- Atualização do `~/start-zvision.sh` no WSL2

Para resolver: reiniciar o WSL2 com `wsl --shutdown` no PowerShell como admin,
depois `wsl --list` para confirmar a distribuição. Se persistir,
verificar `wsl --update` e reimportar a distro.

## Artefatos entregues no Sprint D
- [bridge/index.js](../../../aios-core/bridge/index.js) — endpoint `/status` adicionado
- [start-zvision.sh](../../../start-zvision.sh) — mensagem Sprint D + link `/status`
- `.paperclip/org-chart-setup.sh` — existia, validado
- `intent-classifier.js` — 22 squads completos, já estava correto

## Fase 5 (próxima)
Migrar Paperclip + Bridge para servidor externo (Zeabur ou Railway)
para operação 24/7 sem precisar do WSL2 aberto. Isso também elimina
o risco de bloqueio por erro de distribuição WSL.
