---
name: "write-sop-automation-delivery"
description: "Escreve o SOP de Entrega de Automação em Markdown para Obsidian"
inputFile: "squads/sop-factory/output/process-maps.md"
outputFile: "squads/sop-factory/output/sops/sop-entrega-automacao.md"
---

# Task: Escrever SOP de Entrega de Automação

## Processo

1. Carregar o mapa do processo "Entrega de Automação" de `process-maps.md`
2. Carregar tom e contexto da Zvision de `_opensquad/_memory/company.md`

3. Escrever o documento `sop-entrega-automacao.md` com estrutura híbrida:
   - Frontmatter YAML completo
   - Resumo executivo (objetivo, gatilho, output)
   - Tabela de visão geral de fases
   - Detalhamento das fases críticas com checkboxes
   - Callouts nos pontos críticos de qualidade e go-live
   - Seção de ferramentas
   - Tabela de histórico de versões

4. Salvar em `squads/sop-factory/output/sops/sop-entrega-automacao.md`

## Formato de Output

Seguir a mesma estrutura do SOP de Onboarding, adaptado para o processo de Entrega de Automação.

Frontmatter:
```yaml
título: SOP — Entrega de Automação
tipo: sop
versão: 1.0
data: [hoje]
status: ativo
tags: [operacoes, entrega, automacao, sop]
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
