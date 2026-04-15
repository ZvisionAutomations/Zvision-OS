---
name: zvision-os
description: Sistema operacional completo da Zvision — memória institucional, skill graphs de 22 squads, decisões e specs
---
# Zvision OS — Segundo Cérebro

A Zvision Automations é uma agência de automação e IA em pré-lançamento.
Este vault é a memória viva de tudo que foi decidido, construído e aprendido.

## REGRA DE NAVEGAÇÃO
Antes de qualquer trabalho, leia o index do squad relevante em [[squads/]].
O agente navega o grafo e carrega apenas o contexto necessário —
progressive disclosure em vez de injetar tudo no contexto.

## Domínios do negócio
- [[moc-processos]] — processos internos, SOPs, operação da agência
- [[moc-servicos]] — o que entregamos, como entregamos
- [[moc-clientes]] — pipeline, deals, contexto de cada cliente
- [[moc-stack]] — stack técnica, decisões de arquitetura
- [[moc-seguranca]] — auditorias, hardening, padrões

## Skill Graphs — 22 Squads

### Desenvolvimento e Produto
- [[squads/squad-dev/index]] — implementação, arquitetura, QA e DevOps
- [[squads/squad-product/index]] — product discovery, roadmap, C-suite virtual

### Segurança
- [[squads/squad-cybersecurity/index]] — segurança, pentest e compliance LGPD

### Marketing e Conversão
- [[squads/squad-copy/index]] — copywriting persuasivo e conversão
- [[squads/squad-brand/index]] — marca, posicionamento e identidade
- [[squads/squad-paidmedia/index]] — tráfego pago Meta e Google Ads
- [[squads/squad-growth/index]] — CRO, SEO, analytics e retenção
- [[squads/squad-content/index]] — estratégia editorial e conteúdo orgânico
- [[squads/squad-storytelling/index]] — narrativa, pitch e apresentações

### Comercial e Financeiro
- [[squads/squad-commercial/index]] — pipeline de vendas e prospecção
- [[squads/squad-hormozi/index]] — ofertas irresistíveis e $100M framework
- [[squads/squad-finance/index]] — budget, pricing e análise financeira

### Design e Experiência
- [[squads/squad-design/index]] — UI/UX, design systems e tokens
- [[squads/squad-animations/index]] — motion design, Three.js e shaders

### Inteligência e Pesquisa
- [[squads/squad-research/index]] — market analysis e inteligência competitiva
- [[squads/squad-cloning/index]] — digital twins e clonagem cognitiva
- [[squads/squad-council/index]] — conselheiros estratégicos (Dalio, Munger, Naval)
- [[squads/squad-advisory/index]] — advisory board com contexto BR

### Operação e Cultura
- [[squads/squad-c-level/index]] — C-suite virtual e visão executiva
- [[squads/squad-movement/index]] — comunidade, manifesto e cultura

### IA e Educação
- [[squads/squad-claude/index]] — Claude Code avançado, MCPs e skills
- [[squads/squad-courses/index]] — treinamentos, currículos e launch educacional

## Projetos ativos
- [[zvision-landing]] — landing page em produção (Vercel, hardened)
- [[zvision-crm]] — CRM em produção (Next.js + Supabase, auditado)
- [[zvision-os]] — este sistema operacional

## Infraestrutura de IA
O [[paperclip]] (localhost:3100) orquestra os agentes;
o [[bridge-http]] (localhost:3300) usa o [[intent-classifier]]
para rotear requests ao squad correto com zero tokens.
O [[unified-intelligence-stack]] tem a visão consolidada do sistema.

## Estado atual
Estágio: pré-lançamento.
Pipeline: [[pipeline-leads-abril-2026]] — 94 leads prontos para outbound.
Meta imediata: primeiro cliente fechado em 30 dias.
Maior ativo: infraestrutura de IA com 22 squads e 300+ agentes.

## Sprints concluídos
- [[sprint-a-unification]] — fundação e registry unificado ✅
- [[sprint-b-constitution]] — story gate e governança ✅
- [[sprint-c-skill-graphs]] — skill graphs por squad ✅ (22 grafos criados)

## Regra de ouro
Antes de executar qualquer tarefa relevante:
1. Identifica o squad pelo domínio da task
2. Lê o index: obsidian-vault/squads/[squad-id]/index.md
3. Navega os MOCs via wikilinks
4. Carrega apenas os nodes necessários
5. Executa com contexto do domínio
6. Documenta o resultado no node correto
