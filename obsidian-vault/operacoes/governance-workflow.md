---
name: governance-workflow
description: Fluxo de aprovação obrigatório para qualquer trabalho no Zvision-OS
---
# Governance Workflow

Nenhum trabalho acontece sem passar por este fluxo.
Governado pela [[sinapse-constitution]] com Story Gate ativo desde Sprint B (2026-04).

## Fluxo para features novas

```
Miguel (ideia)
    ↓
/pwf-brainstorm
    ↓ shape da ideia, constraints, trade-offs
/pwf-plan
    ↓ fases executáveis com critérios claros
@product-lead *validate
    ↓ story aprovada (status: Ready)
STORY GATE LIBERADO
    ↓
/pwf-work-plan (fase 1)
    ↓
/pwf-review
    ↓ findings corrigidos
/pwf-work-plan (fase 2)
    ↓
... (repete por fase)
    ↓
/hm-engineer (antes de qualquer deploy)
    ↓
/cso (se tiver componente de segurança)
    ↓
@devops *push
    ↓
Miguel aprova PR
    ↓
Deploy em produção
```

## Fluxo para trabalho de squad (copy, design, etc)

```
Miguel (pedido)
    ↓
Intent Classifier → squad correto
    ↓
Squad executa
    ↓
Output documentado no vault
    ↓
Miguel revisa e aprova
```

## Quem aprova o quê

| Decisão | Aprovador |
|---------|-----------|
| Qualquer feature nova | /pwf-brainstorm + Miguel |
| Story de desenvolvimento | @product-lead |
| Arquitetura técnica | Zvision CTO (Paperclip) |
| Deploy em produção | Miguel + /hm-engineer |
| Auditoria de segurança | Zvision CSO (Paperclip) |
| Materiais de marketing | Miguel |
| Decisão estratégica | Advisory Board + Miguel |

## Comandos do protocolo Psters

| Comando | Quando usar |
|---------|-------------|
| /pwf-brainstorm | SEMPRE primeiro — toda feature |
| /pwf-plan | Converte brainstorm em fases |
| /pwf-work-plan | Executa uma fase por vez |
| /pwf-work | Fixes pequenos fora de plano |
| /pwf-review | Review antes de commitar |
| /pwf-doc | Atualiza documentação técnica |
| /pwf-commit-changes | Commits bem estruturados |

## Story Gate

Ativo desde: Sprint B (2026-04)
Artigo III da Constitution — NON-NEGOTIABLE
Hook: `.claude/hooks/enforce-story-gate.js`

Se você ver: `⛔ STORY GATE ATIVO`
Solução: comece com `/pwf-brainstorm`

## Paperclip Org Chart

| Papel | Agente | Responsabilidade |
|-------|--------|-----------------|
| Board | Miguel (humano) | Aprovações finais, direção estratégica |
| CEO | Zvision CEO | Valida features de alto impacto |
| CTO | Zvision CTO | Aprova arquitetura e merges |
| CMO | Zvision CMO | Aprova materiais de marketing |
| CSO | Zvision CSO | Audita segurança, aprova deploys |

Para ativar o Paperclip: `bash .paperclip/org-chart-setup.sh` (requer WSL2 + Paperclip online)
