---
name: fase2-arquitetura
description: Arquitetura da Fase 2 — Paperclip + SynkraAI AIOX + Bridge HTTP no Windows/Git Bash
---
# Fase 2 — Arquitetura

## Componentes

- [[paperclip]] — empresa (org chart, tickets, governance) → localhost:3100
- [[aios-core]] — runtime AIOX clonado → C:\Users\Lenovo\aios-core
- [[bridge-http]] — cola entre os dois → localhost:3300

## Como iniciar

```bash
# Git Bash
bash ~/start-zvision.sh

# Ou Windows
start-zvision.bat
```

## Como usar

```bash
# Executar squad via bridge (intent automático)
curl -X POST http://localhost:3300/execute \
  -H "Content-Type: application/json" \
  -d '{"task": "sua task aqui"}'

# Squad específico
curl -X POST http://localhost:3300/execute \
  -H "Content-Type: application/json" \
  -d '{"task": "sua task", "squad": "cybersecurity"}'
```

## Intent Classification (zero tokens gastos na triagem)

| Palavra-chave | Squad ativado |
|---|---|
| segurança / audit / pentest / vulnerabilidade | cybersecurity |
| copy / texto / headline / email | copy-squad |
| design / interface / ux / ui | design-squad |
| tráfego / ads / campanha / anuncio | traffic-masters |
| dados / analytics / métrica / dashboard | data-squad |
| marca / branding / identidade | brand-squad |
| estratégia / decisão / planejamento | c-level-squad |
| escala / oferta / preço | hormozi-squad |
| história / narrativa / roteiro | storytelling |
| processo / sop / operação | sop-factory |

## Squads disponíveis (13)

advisory-board, brand-squad, c-level-squad, claude-code-mastery, copy-squad, cybersecurity, data-squad, design-squad, hormozi-squad, movement, sop-factory, storytelling, traffic-masters

## Portas

| Serviço | Porta | Health check |
|---|---|---|
| Paperclip | 3100 | `curl localhost:3100/api/health` |
| Bridge | 3300 | `curl localhost:3300/health` |
| Squads | — | `curl localhost:3300/squads` |

## Empresa no Paperclip

- **Nome:** Zvision Automations
- **Company ID:** bc135976-9ab0-4b76-b376-3e3d462e24f1
- **Agent ID:** a447bee8-9ad5-4c54-b056-cbb25e301f88 (Zvision Squads Bridge)
- **UI:** http://localhost:3100

## Caminhos no sistema

| Componente | Caminho |
|---|---|
| Paperclip install | C:\Users\Lenovo\paperclip-zvision |
| Paperclip data | C:\Users\Lenovo\paperclip-zvision\.paperclip |
| AIOX Core | C:\Users\Lenovo\aios-core |
| Bridge | C:\Users\Lenovo\aios-core\bridge\index.js |
| Script start | C:\Users\Lenovo\start-zvision.sh / .bat |

## Fase 5

Migrar Paperclip + Bridge para servidor externo (Zeabur ou Railway).
AIOX Core escala horizontalmente com múltiplos workers por cliente.

## Status
✅ Operacional desde 2026-04-03
