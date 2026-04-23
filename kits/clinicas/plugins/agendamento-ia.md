# Plugin: Agendamento Inteligente com IA

## O que faz
Pacientes agendam via WhatsApp 24/7 com IA — sem secretária para horários simples.

## Fluxo
`
Paciente envia "quero agendar" no WhatsApp
  → IA pergunta: especialidade, plano ou particular, preferência de horário
  → Consulta agenda (Google Calendar ou sistema da clínica)
  → Oferece 3 opções de horário
  → Confirma agendamento
  → Envia confirmação + instruções de preparo
  → Agenda confirmação automática para 48h antes
`

## Integrações
- WhatsApp Cloud API
- Google Calendar / Calendly
- n8n (orquestração)

## MCP
Nenhum — operação via n8n + APIs nativas
