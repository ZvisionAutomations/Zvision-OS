---
name: "write-sop-agent-delivery"
description: "Escreve o SOP de Entrega de Agente de IA em Markdown para Obsidian"
inputFile: "squads/sop-factory/output/process-maps.md"
outputFile: "squads/sop-factory/output/sops/sop-entrega-agente-ia.md"
---

# Task: Escrever SOP de Entrega de Agente de IA

## Processo

1. Carregar o mapa do processo "Entrega de Agente de IA" de `process-maps.md`
2. Carregar tom e contexto da Zvision de `_opensquad/_memory/company.md`

3. Escrever o documento `sop-entrega-agente-ia.md` com estrutura híbrida:
   - Frontmatter YAML completo
   - Resumo executivo (objetivo, gatilho, output)
   - Tabela de visão geral de fases
   - Detalhamento das fases críticas (design do agente, testes, deploy)
   - Callouts nos pontos de decisão e critérios de qualidade do agente
   - Seção de ferramentas (LLMs, plataformas de deploy, integrações)
   - Tabela de histórico de versões

4. Salvar em `squads/sop-factory/output/sops/sop-entrega-agente-ia.md`

## Formato de Output

Seguir a mesma estrutura dos outros SOPs, adaptado para o processo de Entrega de Agente de IA.

Frontmatter:
```yaml
título: SOP — Entrega de Agente de IA
tipo: sop
versão: 1.0
data: [hoje]
status: ativo
tags: [operacoes, entrega, agente-ia, sop]
```

## Quality Criteria

- [ ] Frontmatter YAML completo
- [ ] Resumo executivo presente
- [ ] Tabela de visão geral de fases
- [ ] Pelo menos 1 callout Obsidian
- [ ] Checkboxes nos passos de validação
- [ ] Tom imperativo em todos os passos
- [ ] Sem em dashes no texto corrido
- [ ] Tabela de histórico de versões

## Veto Conditions

- Documento sem frontmatter YAML
- Documento sem tabela de visão geral
- Passos em passivo ("deve ser feito")
- Uso de em dashes (—) no texto corrido
