---
paths: **/*
---

# Sinapse — Orchestration Rules

> **CRITICAL:** This project has specialized AI agent squads installed. When a user request falls within a domain covered by a squad, you MUST delegate to the appropriate specialist agent instead of handling it yourself.

## Delegation Rule

When a user request matches a squad domain (see table below):
1. **Acknowledge** the domain is covered by a specialized squad
2. **Recommend** activating the squad's orchestrator or specialist agent
3. **Provide** the invocation command (e.g., `/ca:agents:ca-orchestrator`)
4. **Do NOT** handle the request yourself if a dedicated agent exists

**Exception:** If the user explicitly asks you to handle it anyway, proceed — but note the specialized squad exists.

## Squads Instaladas

| Squad | Capacidade |
|-------|-----------|
| `squad-animations` | 9 agents, 73 tasks, 14 KBs, 5 workflows |
| `squad-brand` | 15 agents, 97 tasks, 20 KBs, 4 workflows |
| `squad-claude` | 10 agents, 49 tasks, 5 KBs, 2 workflows |
| `squad-cloning` | 9 agents, 54 tasks, 9 KBs, 6 workflows |
| `squad-commercial` | 11 agents, 85 tasks, 13 KBs, 6 workflows |
| `squad-content` | 7 agents, 90 tasks, 19 KBs, 6 workflows |
| `squad-copy` | 14 agents, 81 tasks, 16 KBs, 6 workflows |
| `squad-council` | 11 agents, 56 tasks, 3 KBs, 2 workflows |
| `squad-courses` | 8 agents, 59 tasks, 10 KBs, 6 workflows |
| `squad-cybersecurity` | 9 agents, 53 tasks, 3 KBs, 2 workflows |
| `squad-design` | 15 agents, 101 tasks, 13 KBs, 6 workflows |
| `squad-finance` | 5 agents, 45 tasks, 8 KBs, 4 workflows |
| `squad-growth` | 7 agents, 77 tasks, 12 KBs, 6 workflows |
| `squad-paidmedia` | 10 agents, 82 tasks, 14 KBs, 5 workflows |
| `squad-product` | 7 agents, 75 tasks, 11 KBs, 6 workflows |
| `squad-research` | 8 agents, 72 tasks, 13 KBs, 6 workflows |
| `squad-storytelling` | 11 agents, 47 tasks, 4 KBs, 2 workflows |


## Mapa de Delegacao por Dominio

| Dominio | Squad | Agente Lead | Invocacao |
|---------|-------|-------------|-----------|
| Branding e identidade visual | squad-brand | brand-orchestrator (Meridian) | `/brand:agents:brand-orchestrator` |
| Vendas e estrategia comercial | squad-commercial | cs-orchestrator (Pipeline) | `/commercial:agents:cs-orchestrator` |
| Conteudo e editorial | squad-content | content-orchestrator | `/content:agents:content-orchestrator` |
| Copywriting e persuasao | squad-copy | copy-strategist (Quill) | `/copywriting:agents:copy-strategist` |
| Animacoes web, Three.js, shaders, motion | squad-animations | ca-orchestrator (Kinetic) | `/ca:agents:ca-orchestrator` |
| UX/UI e experiencia digital | squad-design | dx-orchestrator (Nexus) | `/digital-experience:agents:dx-orchestrator` |
| Inteligencia financeira e pricing | squad-finance | fi-orchestrator (Ledger) | `/finance:agents:fi-orchestrator` |
| Growth organico, SEO e analytics | squad-growth | ga-orchestrator (Catalyst) | `/growth:agents:ga-orchestrator` |
| Midia paga (Meta Ads, Google Ads, CRO) | squad-paidmedia | pm-orchestrator (Apex) | `/pm:agents:pm-orchestrator` |
| Produto e discovery | squad-product | ps-orchestrator (Vector) | `/product:agents:ps-orchestrator` |
| Pesquisa e inteligencia competitiva | squad-research | research-orchestrator (Prism) | `/research:agents:research-orchestrator` |
| Claude Code mastery e automacao | squad-claude | cm-orchestrator (Orion) | `/claude:agents:cm-orchestrator` |
| Conselho estrategico e modelos mentais | squad-council | council-orchestrator (Zenith) | `/council:agents:council-orchestrator` |
| Narrativa, storytelling e pitch | squad-storytelling | narrative-orchestrator (Arc) | `/narrative:agents:narrative-orchestrator` |
| Seguranca cibernetica e compliance | squad-cybersecurity | cyber-orchestrator (Fortress) | `/cyber:agents:cyber-orchestrator` |

## Quando Delegar

| Situacao | Squad |
|----------|-------|
| Animacao/motion/Three.js/shader | squad-animations |
| Copy/headline/persuasao | squad-copy |
| Branding/identidade/logo | squad-brand |
| Pesquisa/benchmark/analise competitiva | squad-research |
| Conteudo/editorial/blog/social media | squad-content |
| UX/UI/design system/wireframe | squad-design |
| Growth/SEO/analytics/metricas organicas | squad-growth |
| Vendas/proposta/pitch/CRM | squad-commercial |
| Financeiro/pricing/P&L/budget | squad-finance |
| Midia paga/Meta Ads/Google Ads/CRO | squad-paidmedia |
| Produto/discovery/roadmap | squad-product |
| Claude Code/prompt engineering/MCP | squad-claude |
| Conselho estrategico/modelos mentais/decisao | squad-council |
| Storytelling/narrativa/pitch/apresentacao | squad-storytelling |
| Seguranca/pentest/compliance/incident response | squad-cybersecurity |

## Handoff Protocol

1. **Identificar** o dominio do pedido
2. **Informar** qual squad cobre e como invocar: `/{prefix}:agents:{agent-id}`
3. **Fornecer contexto** do handoff se necessario
4. Squads sao **autonomas** — o orchestrator coordena internamente
5. Squads possuem **knowledge bases**, **tasks** e **workflows** proprios em `./squads/{squad-name}/`
