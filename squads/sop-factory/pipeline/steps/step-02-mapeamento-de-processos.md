---
step: 2
name: "Mapeamento de Processos"
type: agent
agent: mario-mapeamento
execution: inline
inputFile: "squads/sop-factory/output/contexto-operacional.md"
outputFile: "squads/sop-factory/output/process-maps.md"
---

# Mapeamento de Processos

**Agente:** Mário Mapeamento (🗺️)
**Input:** contexto-operacional.md (respostas do checkpoint)
**Output:** process-maps.md (4 processos mapeados)

## Instrução

Com base nas respostas do contexto operacional e no perfil da Zvision Automation (company.md), mapear os 4 processos internos core:

1. **Onboarding de Cliente** — do contrato assinado até o primeiro fluxo em produção
2. **Entrega de Automação** — do mapeamento técnico ao go-live de uma automação
3. **Entrega de Agente de IA** — do briefing ao deploy de um agente conversacional
4. **Checklist de Qualidade Pré-Entrega** — processo de validação antes de qualquer entrega ao cliente

Para cada processo, mapear:
- Gatilho/input (o que inicia o processo)
- Fases macro (2-5 fases)
- Passos por fase (responsável, ferramentas, output)
- Pelo menos 1 ponto de decisão go/no-go
- Critério de conclusão do processo

## Veto Conditions

- Qualquer processo sem output de fase definido
- Qualquer processo sem pelo menos 1 ponto de decisão
- Nome de pessoa como responsável (deve ser papel/função)
- Menos de 2 fases em qualquer processo
