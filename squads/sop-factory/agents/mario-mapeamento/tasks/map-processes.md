---
name: "map-processes"
description: "Mapeia os 4 processos core da Zvision usando contexto da empresa e respostas do checkpoint"
inputFile: "squads/sop-factory/output/contexto-operacional.md"
outputFile: "squads/sop-factory/output/process-maps.md"
---

# Task: Mapear os 4 Processos Core da Zvision

## Processo

1. Carregar o contexto da empresa em `_opensquad/_memory/company.md`: setor, produtos, tom, stack tecnológico
2. Carregar as respostas do checkpoint em `squads/sop-factory/output/{run_id}/contexto-operacional.md`
3. Carregar o domain-framework em `squads/sop-factory/pipeline/data/domain-framework.md`

4. Para cada um dos 4 processos abaixo, mapear:

   **Processos a mapear:**
   - Onboarding de Cliente (do contrato assinado ao primeiro fluxo em produção)
   - Entrega de Automação (do mapeamento técnico ao go-live de uma automação)
   - Entrega de Agente de IA (do briefing ao deploy de um agente conversacional)
   - Checklist de Qualidade Pré-Entrega (validação antes de qualquer entrega)

   **Para cada processo definir:**
   a. Nome do processo e objetivo (1 linha)
   b. Gatilho/input: o que inicia o processo
   c. Output final: o que é produzido ao final
   d. Fases macro (2 a 5 fases com nome curto)
   e. Para cada fase:
      - Responsável (papel funcional, nunca nome pessoal)
      - Passos (3-7 nos críticos, 1-3 nos demais)
      - Ferramenta por passo (ou `[TBD]`)
      - Output da fase
   f. Pelo menos 1 ponto de decisão go/no-go no processo
   g. Critério de conclusão do processo

5. Formatar como Markdown hierárquico com separação visual clara entre processos
6. Salvar em `squads/sop-factory/output/process-maps.md`

## Formato de Output

```markdown
# Mapas de Processo — Zvision Automation

---

# Processo 1: [Nome do Processo]

**Objetivo:** [1 linha]
**Gatilho:** [o que inicia]
**Output final:** [o que é produzido]

## Fase 1: [Nome] (Responsável: [Papel])
### Passos
- 1.1 [Passo em imperativo]
  - Ferramenta: [nome ou TBD]
  - Output: [entregável]
- 1.2 ...

> ⚠️ Ponto de decisão: [condição] → SIM: [ação] | NÃO: [ação]

**Critério de conclusão da fase:** [como verificar]

## Fase 2: ...

**Critério de conclusão do processo:** [como verificar]

---

# Processo 2: ...
```

## Quality Criteria

- [ ] Todos os 4 processos mapeados com pelo menos 2 fases cada
- [ ] Cada fase tem responsável (papel), mínimo 2 passos, output definido
- [ ] Pelo menos 1 ponto de decisão por processo
- [ ] Ferramentas identificadas por passo (ou TBD)
- [ ] Nenhum nome de pessoa como responsável
- [ ] Nível de granularidade consistente dentro de cada processo

## Veto Conditions

- Processo sem output de fase definido
- Processo sem ponto de decisão
- Nome de pessoa como responsável
- Menos de 2 fases em qualquer processo
