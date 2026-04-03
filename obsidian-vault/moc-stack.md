---
name: moc-stack
description: Stack técnica e decisões de arquitetura da Zvision
---
# Stack Técnica

## Stack principal
- **Frontend:** Vanilla HTML/CSS/JS
- **Deploy:** Vercel
- **Backend/Scripts:** Node.js
- **Dev environment:** Windows 10 + WSL2 Ubuntu-Antigravity

## Decisões de arquitetura
_A documentar conforme surgem._

## Projetos e suas stacks
- [[zvision-landing]] — Vanilla HTML/CSS/JS, Vercel
- [[zvision-crm]] — A definir

## Fase 2 — Orquestração de Agentes
A [[fase2-arquitetura]] introduziu o [[paperclip]] como orquestrador central, conectado aos squads via [[bridge-http]] com [[token-optimization]] embutida. O [[insightfulpipe]] será ativado na Fase 3 para dar dados reais ao [[traffic-masters-squad]].
