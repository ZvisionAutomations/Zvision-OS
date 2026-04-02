# Anti-Patterns — SOP Factory

## Armadilhas no Mapeamento de Processos

### 1. Mapear o processo ideal, não o real
**Problema:** O mapa documenta como o processo *deveria* funcionar, não como *funciona hoje*.
**Consequência:** Na operação real, colaboradores ignoram o SOP porque não reflete a realidade.
**Solução:** Mapear exatamente o processo executável hoje, marcar melhorias futuras com `(v2.0)`.

### 2. Usar nomes de pessoas como responsáveis
**Problema:** "João faz o kick-off" em vez de "CEO / Responsável de Projeto faz o kick-off".
**Consequência:** Quando João sai, o processo quebra ou precisa ser reescrito.
**Solução:** Sempre usar papéis funcionais. Nomes pessoais nunca aparecem em SOPs.

### 3. Fases sem output definido
**Problema:** "Fase 2: Análise técnica" sem entregável específico.
**Consequência:** Ninguém sabe quando a fase terminou. Projetos ficam "em análise" indefinidamente.
**Solução:** Todo output de fase é um artefato concreto: documento, lista, email enviado, acesso confirmado.

### 4. Decisões implícitas no fluxo
**Problema:** O processo avança de Fase 2 para Fase 3 sem nenhum gate de validação.
**Consequência:** Erros da fase anterior chegam às fases seguintes — retrabalho caro no final.
**Solução:** Todo processo tem pelo menos 1 ponto de decisão explícito com condição go/no-go.

### 5. Granularidade inconsistente
**Problema:** Fase 1 tem 8 sub-passos detalhados, Fase 3 tem "fazer o deploy" como passo único.
**Consequência:** O colaborador tem guia para os momentos errados e fica sem guia nos críticos.
**Solução:** Calibrar o nível de detalhe: pontos críticos têm mais detalhe, etapas simples ficam compactas.

---

## Armadilhas na Escrita de SOPs

### 6. SOPs como texto corrido (sem estrutura visual)
**Problema:** Parágrafos descrevendo o processo em prosa.
**Consequência:** Ninguém lê documentação operacional em formato de artigo. SOPs são executados, não lidos.
**Solução:** Usar tabelas, listas numeradas, checkboxes e callouts. Zero parágrafos em passos de processo.

### 7. Omitir o frontmatter YAML
**Problema:** Documento sem metadados de versão, status e tags.
**Consequência:** Obsidian não indexa nem relaciona o documento. Sem versão, não há rastreabilidade.
**Solução:** Todo SOP começa com frontmatter YAML completo.

### 8. Linguagem passiva nos passos
**Problema:** "O contrato deve ser enviado" / "O cliente deverá ser notificado".
**Consequência:** Ambiguidade sobre quem faz o quê. Em operação sob pressão, etapas são puladas.
**Solução:** Imperativo direto com responsável explícito: "CEO envia contrato" / "Engenheiro notifica cliente".

### 9. Checklists sem distinção obrigatório/opcional
**Problema:** Lista plana de 20 itens sem hierarquia de criticidade.
**Consequência:** Colaboradores marcam "quase tudo" e entregam com gaps críticos.
**Solução:** Usar `[OBRIGATÓRIO]` e `[OPCIONAL]` explicitamente. Aprovação exige 100% dos obrigatórios.

---

## Armadilhas na Revisão de SOPs

### 10. Aprovar por pressão de prazo
**Problema:** SOP com gaps críticos recebe aprovação porque "está bom o suficiente".
**Consequência:** Colaboradores encontram os gaps na operação real — em momento de pior impacto.
**Solução:** Critério de aprovação não negocia. Gaps documentados = REVISÃO NECESSÁRIA, sem exceção.

### 11. Feedback vago
**Problema:** "Melhorar a clareza da Fase 3" sem especificar o quê está confuso.
**Consequência:** Sofia SOP reescreve sem saber o que mudar — risco de piorar.
**Solução:** Toda correção obrigatória especifica: localização + problema + sugestão de reescrita.
