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

Crítico na fase 2 — quando Paperclip orquestrar squads em paralelo para múltiplos
clientes, cada request mal otimizado multiplica o custo por número de clientes.

Implementar no bridge HTTP entre Paperclip e AIOS Core:
- Classificar intent da task antes de carregar o squad
- Carregar só os agentes do squad relevante, não os 156
- Prunar histórico de conversas longas antes de passar contexto

## Status
🔴 Pendente — implementar na Fase 2
