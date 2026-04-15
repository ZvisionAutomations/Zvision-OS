---
name: "review-sops"
description: "Revisa os 4 documentos produzidos por Sofia SOP e entrega relatório com veredito por documento"
inputFile: "squads/sop-factory/output/sops/"
outputFile: "squads/sop-factory/output/review-report.md"
---

# Task: Revisar os 4 SOPs

## Processo

1. Carregar `squads/sop-factory/pipeline/data/quality-criteria.md` como fonte da verdade
2. Carregar `squads/sop-factory/pipeline/data/domain-framework.md` para contexto de domínio

3. Para cada um dos 4 documentos em `output/sops/`:
   - `sop-onboarding-cliente.md`
   - `sop-entrega-automacao.md`
   - `sop-entrega-agente-ia.md`
   - `checklist-qualidade-preentrega.md`

   a. Ler o documento completo antes de avaliar qualquer critério
   b. Avaliar as 5 dimensões (nota 1-10 com justificativa):
      - **Completude:** todos os passos, responsáveis, outputs e ferramentas presentes?
      - **Clareza operacional:** qualquer colaborador consegue executar sem pedir ajuda?
      - **Precisão contextual:** usa terminologia, ferramentas e papéis reais da Zvision?
      - **Formatação Obsidian:** frontmatter, callouts, checkboxes, estrutura correta?
      - **Acionabilidade:** passos são executáveis imediatamente, sem gaps?
   c. Calcular média
   d. Aplicar veredito:
      - APROVADO: média >= 7 e nenhuma dimensão < 4
      - REVISÃO NECESSÁRIA: média < 7 ou qualquer dimensão < 4
   e. Para critérios com nota < 7: fornecer localização exata + instrução de correção

4. Compilar `review-report.md` com:
   - Sumário executivo (X aprovados / Y precisam revisão + próximos passos)
   - Avaliação completa por documento
   - Path to approval para documentos com REVISÃO NECESSÁRIA

## Formato de Output

```markdown
# Relatório de Revisão — SOP Factory

**Data:** [hoje]
**Revisora:** Renata Revisão

## Sumário Executivo

[N] documentos aprovados / [N] precisam revisão.

[Próximos passos se houver revisões necessárias]

---

## 1. SOP — Onboarding de Cliente

**Pontos fortes:** [pelo menos 1]

| Dimensão | Nota | Justificativa |
|----------|------|---------------|
| Completude | X/10 | ... |
| Clareza operacional | X/10 | ... |
| Precisão contextual | X/10 | ... |
| Formatação Obsidian | X/10 | ... |
| Acionabilidade | X/10 | ... |
| **Média** | **X.X/10** | |

**Veredito: APROVADO / REVISÃO NECESSÁRIA**

[Se REVISÃO NECESSÁRIA:]
### Correções Obrigatórias
- Correção obrigatória: [Localização exata] — [problema] → [instrução de correção]

### Sugestões
- Sugestão: [Localização] — [melhoria não-bloqueante]

[Se REVISÃO NECESSÁRIA:]
### Path to Approval
[Lista de ações específicas para aprovação]

---

## 2. SOP — Entrega de Automação
...
```

## Quality Criteria

- [ ] Todos os 4 documentos avaliados nas 5 dimensões com nota e justificativa
- [ ] Todo critério com nota < 7 tem localização exata + instrução de correção
- [ ] Veredito claro (APROVADO ou REVISÃO NECESSÁRIA) por documento
- [ ] Sumário executivo com contagem e próximos passos
- [ ] Pelo menos 1 ponto forte por documento
- [ ] Prefixos "Correção obrigatória:" e "Sugestão:" usados consistentemente

## Veto Conditions

- Qualquer documento sem veredito claro
- Critério com nota < 7 sem localização exata e instrução de correção
- Relatório sem sumário executivo
