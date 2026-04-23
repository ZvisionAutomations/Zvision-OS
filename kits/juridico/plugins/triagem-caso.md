# Plugin: Triagem Inteligente de Casos

## O que faz
IA qualifica e classifica casos recebidos por área do direito e probabilidade de êxito.

## Fluxo de Triagem
`
Potencial cliente entra em contato (WhatsApp/formulário)
  → IA coleta: resumo do caso, documentos disponíveis, urgência
  → Classifica: área do direito + sub-área
  → Avalia: probabilidade de êxito (baixa/média/alta)
  → Calcula: estimativa de valor de honorários
  → Distribui: para o advogado especialista correto
  → Agenda: consulta inicial (se aprovado)
`

## Agentes Zvision
- @lex (juridico-chief) — classifica área do direito
- @forum (contencioso) — avalia probabilidade de êxito
- @sócio / @labore / @consumidor — especialistas por área

## Output
- Relatório de triagem (área, probabilidade, complexidade, honorários estimados)
- Recomendação: aceitar, recusar, ou solicitar mais informações
