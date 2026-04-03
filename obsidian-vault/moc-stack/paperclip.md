---
name: paperclip
description: Orquestrador de agentes — org chart, tickets, governance, audit log
---
# Paperclip

Plataforma open-source de orquestração de times de agentes IA.
Você é o board. Aprova tickets, os squads executam.

## Papel na Zvision

O Paperclip é o centro de comando: recebe tasks via interface web ou API, delega para os squads via [[bridge-http]], e registra audit log de tudo que foi executado. O controle de orçamento de tokens por agente trabalha em conjunto com o [[token-optimization]] implementado no [[bridge-http]] — juntos, garantem que escalar para múltiplos clientes não explode o custo.

- Recebe tasks via interface web ou API
- Delega para os squads via [[bridge-http]]
- Registra audit log de tudo que foi executado
- Controla orçamento de tokens por agente
- Org chart visual da empresa com todos os agentes

## Acesso

- UI: http://localhost:3100
- API: http://localhost:3100/api/health

## IDs

- Company ID: `bc135976-9ab0-4b76-b376-3e3d462e24f1`
- Agent (Bridge): `a447bee8-9ad5-4c54-b056-cbb25e301f88`

## Instalação

```
C:\Users\Lenovo\paperclip-zvision\
  node_modules\        ← binários
  .paperclip\          ← data dir (postgres embedded, config, logs)
  company-package\     ← package de import da Zvision
```

## Comandos úteis

```bash
# Iniciar
cd C:\Users\Lenovo\paperclip-zvision
node_modules\.bin\paperclipai run --data-dir .\.paperclip

# Listar empresas
node_modules\.bin\paperclipai company list --data-dir .\.paperclip

# Listar agentes
node_modules\.bin\paperclipai agent list --data-dir .\.paperclip

# Status
node_modules\.bin\paperclipai doctor --data-dir .\.paperclip
```

## Referência

https://github.com/paperclipai/paperclip

## Status
✅ Instalado e operacional — v2026.325.0
