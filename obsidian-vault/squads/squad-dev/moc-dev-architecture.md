---
name: moc-dev-architecture
squad: squad-dev
type: moc
description: Padrões de arquitetura do Zvision — stack técnica, decisões e constraints absolutas
---
# Dev Architecture

## Stack do Zvision CRM
O [[zvision-crm]] usa Next.js com App Router, TypeScript strict
e Supabase como backend. O [[dev-architect]] garante que toda nova
feature respeita o [[multi-tenant-pattern]] com company_id em todas
as tabelas e [[rls-policy]] de isolamento obrigatório.

## Stack da Landing Page
O [[zvision-landing]] é vanilla HTML/CSS/JS sem dependências externas,
deployado no Vercel. A simplicidade é intencional — cada dependência
é um vetor de ataque e um ponto de falha.

## Constraints absolutas
O [[dev-architect]] bloqueia qualquer PR que viole:
zero TypeScript any, apenas CSS variables (nunca valores crus de cor),
fontes exclusivas Space Grotesk + JetBrains Mono, e
Framer Motion apenas para mount/unmount complexos.

## Infraestrutura de IA
O [[paperclip]] (localhost:3100) orquestra os agentes,
o [[bridge-http]] (localhost:3300) usa o [[intent-classifier]]
para rotear requests zero-token para o squad correto.
