---
name: token-optimization
description: Técnicas para reduzir consumo de tokens em agentes de IA — scoped skills, intent classification, context pruning
---
# Token Optimization

Referência: artigo DomainLabs — redução de 80% de custo com scoped skills e tool filters.
@browser: https://www.domainlabs.dev/blog/agent-guides/reduce-token-spend-skills-filters

## Princípios

- [[scoped-skills]] — carregar só os agentes/tools relevantes para a tarefa, não todos
- [[intent-classification]] — filtro de palavras-chave antes de chamar qualquer LLM (0 tokens)
- [[context-pruning]] — manter só as últimas 5-10 trocas no histórico, não a sessão inteira
- [[compressed-prompts]] — system prompts concisos, sem verbosidade

## Números reais (caso DomainLabs)

Antes: 7.600 tokens por request (32 tools + histórico completo + prompt verboso)
Depois: 1.350 tokens por request — redução de 82%
Impacto: 73-80% menos custo, 50% mais rápido, 5-10% mais preciso

## Quando aplicar na Zvision

Crítico na fase 2 — quando o [[paperclip]] orquestrar squads em paralelo para múltiplos clientes, cada request mal otimizado multiplica o custo por número de clientes.

O [[bridge-http]] é onde esses princípios vivem na prática: o [[intent-classification]] acontece antes de qualquer chamada LLM, e o [[scoped-skills]] garante que apenas o squad relevante é carregado — não todos os 156 agentes. O [[context-pruning]] limita o histórico a 3 turnos antes de passar contexto para o [[aios-core]].

## Status
🔴 Pendente — implementar na Fase 2
