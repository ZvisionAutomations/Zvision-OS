---
título: SOP — Entrega de Agente de IA
tipo: sop
versão: 1.0
data: 2026-04-02
status: ativo
tags: [operacoes, entrega, agente-ia, sop]
---

# SOP — Entrega de Agente de IA

> **Objetivo:** Desenvolver e entregar um agente de IA conversacional do briefing ao deploy em produção.
> **Gatilho:** Briefing do agente aprovado pelo cliente (ou demanda dentro de retainer ativo).
> **Output:** Agente em produção respondendo corretamente nos canais definidos, estável por 48h.

## Visão Geral do Processo

| Fase | Nome | Responsável | Prazo Estimado | Output |
|------|------|-------------|----------------|--------|
| 1 | Design do Agente | Engenheiro + CEO | Dia 1-3 | Briefing e mapa conversacional aprovados |
| 2 | Build do Agente | Engenheiro de Automação | Dia 3-10 | Agente testado em staging |
| 3 | Validação e Deploy | Engenheiro + CEO | Dia 10-12 | Agente em produção estável por 48h |

---

## Fase 1: Design do Agente (CRÍTICO)

> [!WARNING] O briefing aprovado pelo cliente é a constituição do agente. Qualquer desvio de escopo ou tom durante o build gera retrabalho de prompt e reteste completo. Definir e aprovar antes de buildar.

### 1.1 Definir persona, objetivo e escopo
- **Responsável:** CEO + Engenheiro de Automação
- **Ferramenta:** Obsidian (documento de briefing)
- **Output:** Briefing do agente preenchido
- [ ] Nome e persona do agente definidos (tom, estilo de linguagem)
- [ ] Objetivo principal definido (atendimento, vendas, suporte, operacional)
- [ ] Escopo definido: o que o agente FAZ e o que ele NÃO FAZ
- [ ] Idioma e horário de operação definidos

### 1.2 Mapear fluxos conversacionais
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** Obsidian (diagrama de fluxo conversacional)
- **Output:** Mapa de conversas com ramos principais, condicionais e fallbacks
- [ ] Fluxo de entrada (primeiro contato) mapeado
- [ ] Pelo menos 3 jornadas completas mapeadas (casos de uso principais)
- [ ] Fallback definido: o que acontece quando o agente não sabe responder
- [ ] Handoff para humano definido: quando e como transferir

### 1.3 Definir integrações técnicas
- **Responsável:** Engenheiro de Automação
- **Output:** Lista de integrações com requisitos técnicos
- [ ] Canal de comunicação definido (WhatsApp Business, web, outro)
- [ ] Base de conhecimento identificada (FAQ, documentos, Supabase)
- [ ] Integrações com sistemas do cliente mapeadas (CRM, calendário, etc.)

### 1.4 Validar briefing com o cliente
- **Responsável:** CEO
- **Ferramenta:** Google Meet / WhatsApp Business
- **Output:** Briefing aprovado formalmente pelo cliente
- [ ] Briefing apresentado e ajustes incorporados
- [ ] Aprovação registrada (email ou WhatsApp)

> ⚠️ Ponto de decisão: Briefing e mapa conversacional aprovados pelo cliente?
> SIM: avança para Fase 2
> NÃO: revisar e reagendar validação (máximo 1 ciclo no escopo).

**Critério de conclusão:** Briefing aprovado + mapa conversacional completo + integrações mapeadas.

---

## Fase 2: Build do Agente

### 2.1 Configurar o modelo de IA e prompts base
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** Claude Code, API Anthropic
- **Output:** Agente respondendo ao prompt base conforme briefing
- [ ] System prompt construído com persona, escopo e restrições
- [ ] Respostas de abertura e fechamento de conversa definidas
- [ ] Prompt testado com 5 inputs representativos

### 2.2 Integrar base de conhecimento
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** Supabase (embeddings / RAG), n8n
- **Output:** Agente consultando base de conhecimento do cliente
- [ ] Base de conhecimento indexada no Supabase
- [ ] Busca por similaridade testada com perguntas reais do cliente
- [ ] Qualidade das respostas com contexto validada

### 2.3 Implementar integração de canal
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** WhatsApp Business API, n8n, Supabase
- **Output:** Agente recebendo e respondendo no canal definido
- [ ] Webhook do canal configurado e testado
- [ ] Mensagens chegando corretamente no n8n
- [ ] Respostas sendo enviadas de volta ao canal

### 2.4 Testar casos de uso mapeados
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** Canal de staging + interface de teste
- **Output:** Relatório de testes por caso de uso
- [ ] Todos os ramos do mapa conversacional testados
- [ ] Fallback funcionando para perguntas fora do escopo
- [ ] Handoff para humano funcionando corretamente
- [ ] Comportamento com inputs inesperados validado

**Critério de conclusão:** Todos os casos de uso testados com resultados dentro dos critérios de qualidade.

---

## Fase 3: Validação e Deploy

### 3.1 Executar Checklist de Qualidade Pré-Entrega
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** [[checklist-qualidade-preentrega]]
- **Output:** Checklist 100% aprovado

### 3.2 Demo com cliente em staging
- **Responsável:** CEO + Engenheiro
- **Ferramenta:** Canal de staging (WhatsApp ou web)
- **Output:** Aprovação formal do cliente
- [ ] Demo realizada no canal que o cliente vai usar em produção
- [ ] Feedback do cliente coletado e incorporado
- [ ] Aprovação registrada

### 3.3 Deploy em produção
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** AWS, n8n, WhatsApp Business API (produção)
- **Output:** Agente ativo no canal de produção
- [ ] Variáveis de ambiente de produção configuradas
- [ ] Primeira interação em produção monitorada em tempo real

### 3.4 Monitorar primeiras 48h
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** AWS CloudWatch, logs do n8n, Supabase
- **Output:** Confirmação de estabilidade e qualidade das respostas
- [ ] Taxa de fallback dentro do aceitável (referencia: abaixo de 20%)
- [ ] Nenhum erro crítico de integração nas primeiras 48h
- [ ] Pelo menos 10 conversas reais revisadas manualmente

> ⚠️ Ponto de decisão: Primeiras 48h estáveis com qualidade aceitável?
> SIM: entrega concluída, documentar e comunicar cliente
> NÃO: investigar causa raiz, corrigir, reiniciar monitoramento de 48h.

**Critério de conclusão:** Agente em produção estável por 48h + cliente satisfeito + documentação interna do agente registrada.

---

## Ferramentas e Integrações

| Ferramenta | Uso no processo |
|------------|----------------|
| Claude Code | Desenvolvimento do agente e lógica de prompts |
| API Anthropic | Modelo de IA do agente |
| n8n | Orquestração de integrações e fluxos do agente |
| WhatsApp Business API | Canal de comunicação do agente |
| Supabase | Base de conhecimento (RAG) e logs |
| AWS | Infraestrutura e hosting |
| AWS CloudWatch | Monitoramento em produção |
| Obsidian | Briefing, mapa conversacional e documentação |

---

## Histórico de Versões

| Versão | Data | Autor | Mudança |
|--------|------|-------|---------|
| 1.0 | 2026-04-02 | SOP Factory | Versão inicial |
