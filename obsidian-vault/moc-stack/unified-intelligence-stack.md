---
name: unified-intelligence-stack
description: Arquitetura unificada do Zvision-OS — todos os squads, agentes e protocolos em um sistema coerente
---
# Unified Intelligence Stack

O Zvision-OS opera com 17 squads SINAPSE + squads legados e 300+ agentes organizados
em camadas, com intent classifier no bridge e protocolo Psters como padrão de trabalho.

## Sprint A — Completo (Abr 2026)

### O que foi instalado
- **SINAPSE AI v9.2.0** — 17 squads, 150+ agentes via `/SINAPSE:agents:`
- **Psters Workflow** — protocolo de desenvolvimento via `/pwf-*` commands
- **registry.yaml** — mapeamento unificado de todos os squads
- **intent-classifier.js** — roteamento zero-token na bridge
- **CLAUDE.md** — atualizado com todos os sistemas e protocolos

### Squads instalados via SINAPSE

| Squad | Agentes | Tasks | Invoke |
|-------|---------|-------|--------|
| squad-brand | 15 | 97 | `/brand:agents:brand-orqx` |
| squad-commercial | 11 | 85 | `/commercial:agents:commercial-orqx` |
| squad-content | 7 | 90 | `/content:agents:content-orqx` |
| squad-copy | 14 | 81 | `/copywriting:agents:copy-orqx` |
| squad-animations | 9 | 73 | `/ca:agents:animations-orqx` |
| squad-design | 15 | 101 | `/digital-experience:agents:design-orqx` |
| squad-finance | 5 | 45 | `/finance:agents:finance-orqx` |
| squad-growth | 7 | 77 | `/growth:agents:growth-orqx` |
| squad-paidmedia | 10 | 82 | `/pm:agents:paidmedia-orqx` |
| squad-product | 7 | 75 | `/product:agents:product-orqx` |
| squad-research | 8 | 72 | `/research:agents:research-orqx` |
| squad-claude | 10 | 49 | `/claude:agents:claude-orqx` |
| squad-council | 11 | 56 | `/council:agents:council-orqx` |
| squad-storytelling | 11 | 47 | `/narrative:agents:storytelling-orqx` |
| squad-cybersecurity | 9 | 53 | `/cyber:agents:cyber-orqx` |
| squad-cloning | 9 | 54 | `/SINAPSE:agents:cloning-orqx` |
| squad-courses | 8 | 59 | `/SINAPSE:agents:courses-orqx` |

## As Camadas do Sistema

1. **Protocol** — [[psters-workflow]]: `/pwf-brainstorm → /pwf-plan → /pwf-work-plan → /pwf-review → /pwf-commit-changes`
2. **Orchestration** — [[paperclip]] como CEO da empresa de agentes (localhost:3100)
3. **Intent Routing** — [[bridge-http]] + intent-classifier.js (zero tokens, keyword matching)
4. **Squad Registry** — [[registry]] em `squads/registry.yaml`
5. **Squad Awareness** — `.claude/rules/squad-awareness.md` (gerado pelo SINAPSE)
6. **Memory** — [[obsidian-vault]] como skill graph compartilhado

## Protocolo de trabalho

Todo trabalho segue o [[psters-workflow]]:
```
/pwf-brainstorm → /pwf-plan → /pwf-work-plan → /pwf-review → /pwf-commit-changes
```

Nenhum código é escrito sem brainstorm/plan prévio.

## Notas técnicas

- SINAPSE instalado via `npm install sinapse-ai --save-dev` + cópia manual de `.sinapse-ai/` e `squads/`
- Wizard interativo do SINAPSE não funciona sem TTY real — workaround: instalar diretamente
- Psters clonado de GitHub e commands copiados manualmente para `.claude/commands/psters/`
- Intent classifier em `~/aios-core/bridge/intent-classifier.js` — 18 squads mapeados

## Links

- [[fase2-arquitetura]] — infraestrutura base (Paperclip + Bridge)
- [[bridge-http]] — bridge HTTP que usa o intent-classifier
- [[paperclip]] — orquestrador de agentes
