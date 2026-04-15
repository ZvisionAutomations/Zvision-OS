---
name: "write-sop-onboarding"
description: "Escreve o SOP de Onboarding de Cliente em Markdown para Obsidian"
inputFile: "squads/sop-factory/output/process-maps.md"
outputFile: "squads/sop-factory/output/sops/sop-onboarding-cliente.md"
---

# Task: Escrever SOP de Onboarding de Cliente

## Processo

1. Carregar o mapa do processo "Onboarding de Cliente" de `process-maps.md`
2. Carregar tom e contexto da Zvision de `_opensquad/_memory/company.md`
3. Carregar exemplos de output de `squads/sop-factory/pipeline/data/output-examples.md`

4. Escrever o documento `sop-onboarding-cliente.md` com estrutura híbrida:
   - Frontmatter YAML completo
   - Resumo executivo (objetivo, gatilho, output)
   - Tabela de visão geral de fases
   - Detalhamento das fases críticas (Fase 1 e 2: detalhe completo com checkboxes)
   - Fases secundárias em formato compacto (lista numerada simples)
   - Callouts `> [!WARNING]` e `> [!TIP]` nos pontos críticos
   - Seção de ferramentas e integrações
   - Tabela de histórico de versões

5. Salvar em `squads/sop-factory/output/sops/sop-onboarding-cliente.md`

## Formato de Output

```markdown
---
título: SOP — Onboarding de Cliente
tipo: sop
versão: 1.0
data: [hoje]
status: ativo
tags: [operacoes, onboarding, cliente, sop]
---

# SOP — Onboarding de Cliente

> **Objetivo:** [1 linha]
> **Gatilho:** [o que inicia]
> **Output:** [o que é produzido ao final]

## Visão Geral do Processo

| Fase | Nome | Responsável | Prazo Estimado | Output |
|------|------|-------------|----------------|--------|
| 1 | ... | ... | ... | ... |

---

## Fase 1: [Nome] (CRÍTICO)

> [!WARNING] [alerta crítico]

### 1.1 [Passo]
- **Responsável:** [papel]
- **Ferramenta:** [nome]
- **Output:** [entregável]
- [ ] [item de validação]

...

## Ferramentas e Integrações

| Ferramenta | Uso no processo |
|------------|----------------|
| ... | ... |

---

## Histórico de Versões

| Versão | Data | Autor | Mudança |
|--------|------|-------|---------|
| 1.0 | [hoje] | SOP Factory | Versão inicial |
```

## Quality Criteria

- [ ] Frontmatter YAML completo (título, tipo, versão, data, status, tags)
- [ ] Resumo executivo presente (objetivo, gatilho, output)
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
