---
step: 5
name: "Revisão de Qualidade"
type: agent
agent: renata-revisao
execution: inline
inputFile: "squads/sop-factory/output/sops/"
outputFile: "squads/sop-factory/output/review-report.md"
on_reject: 4
---

# Revisão de Qualidade

**Agente:** Renata Revisão (🔍)
**Input:** 4 SOPs em output/sops/
**Output:** review-report.md com veredito por documento

## Instrução

Avaliar cada um dos 4 documentos produzidos por Sofia SOP contra 5 dimensões (nota 1-10 com justificativa):

1. **Completude** — todos os passos, responsáveis, outputs e ferramentas presentes?
2. **Clareza operacional** — qualquer colaborador consegue executar sem pedir ajuda?
3. **Precisão contextual** — usa terminologia, ferramentas e papéis reais da Zvision?
4. **Formatação Obsidian** — frontmatter, callouts, checkboxes, estrutura correta?
5. **Acionabilidade** — passos são executáveis imediatamente, sem gaps?

**Veredito por documento:**
- APROVADO: média >= 7 e nenhuma dimensão < 4
- REVISÃO NECESSÁRIA: média < 7 ou qualquer dimensão < 4

Para critérios com nota < 7: fornecer localização exata + instrução de correção.

Compilar relatório final com sumário executivo (X aprovados / Y precisam revisão).

## Veto Conditions

- Qualquer documento sem veredito claro (APROVADO ou REVISÃO NECESSÁRIA)
- Critério com nota < 7 sem localização exata e instrução de correção
- Relatório sem sumário executivo
