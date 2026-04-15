---
step: 4
name: "Escrita dos SOPs"
type: agent
agent: sofia-sop
execution: inline
inputFile: "squads/sop-factory/output/process-maps.md"
outputFile: "squads/sop-factory/output/sops/"
---

# Escrita dos SOPs

**Agente:** Sofia SOP (✍️)
**Input:** process-maps.md (mapas aprovados de Mário)
**Output:** 4 arquivos .md em output/sops/

## Instrução

Com base nos mapas de processos aprovados, escrever os 4 documentos Markdown para Obsidian:

1. `sop-onboarding-cliente.md` — SOP de Onboarding de Cliente
2. `sop-entrega-automacao.md` — SOP de Entrega de Automação
3. `sop-entrega-agente-ia.md` — SOP de Entrega de Agente de IA
4. `checklist-qualidade-preentrega.md` — Checklist de Qualidade Pré-Entrega

Cada documento deve seguir a estrutura híbrida:
- Frontmatter YAML (título, tipo, versão, data, status, tags)
- Resumo executivo (objetivo, gatilho, output)
- Tabela de visão geral de fases
- Detalhamento das fases críticas
- Callouts Obsidian nos pontos de alto impacto
- Checkboxes em todos os passos de validação
- Tabela de histórico de versões no final

## Veto Conditions

- Documento sem frontmatter YAML
- Documento sem tabela de visão geral
- Documento sem pelo menos 1 callout Obsidian
- Passos escritos em passivo ("deve ser feito") — deve ser imperativo direto
- Uso de em dashes (—) no texto corrido
