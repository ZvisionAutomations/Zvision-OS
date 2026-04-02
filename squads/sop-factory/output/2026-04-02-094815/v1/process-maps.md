# Mapas de Processo — Zvision Automation

> Versão: 1.0 | Data: 2026-04-02 | Gerado por: Mário Mapeamento (SOP Factory)

---

# Processo 1: Onboarding de Cliente

**Objetivo:** Integrar um novo cliente do contrato assinado até o primeiro sistema em produção e monitoramento ativo.
**Gatilho:** Contrato assinado + primeiro pagamento confirmado
**Output final:** Sistema rodando em produção com cliente operando de forma autônoma e retainer mensal ativo

## Fase 1: Kick-off e Discovery (Responsável: CEO / Responsável de Projeto)

**Passos:**
- 1.1 Enviar email de boas-vindas com agenda da reunião de kick-off
  - Ferramenta: Gmail + template de boas-vindas
  - Output: Reunião agendada (prazo: até 48h após pagamento)
- 1.2 Conduzir reunião de kick-off com o cliente
  - Ferramenta: Google Meet + documento de discovery (Obsidian/Notion)
  - Output: Documento de discovery preenchido com processos-alvo, ferramentas do cliente, objetivos de automação
- 1.3 Solicitar acessos às ferramentas do cliente
  - Ferramenta: Checklist de acessos (email/WhatsApp)
  - Output: Lista de acessos recebidos vs. pendentes documentada
- 1.4 Validar acessos recebidos
  - Ferramenta: Supabase, AWS, n8n (ambientes de staging)
  - Output: Confirmação de acesso a todas as plataformas necessárias

> ⚠️ Ponto de decisão: Todos os acessos necessários liberados?
> SIM: avança para Fase 2
> NÃO: aguarda liberação (máximo 5 dias úteis) e registra bloqueio no histórico do cliente

**Critério de conclusão da fase:** Documento de discovery preenchido + todos os acessos validados

---

## Fase 2: Mapeamento Técnico (Responsável: Engenheiro de Automação)

**Passos:**
- 2.1 Analisar processos mapeados no discovery e definir escopo técnico
  - Ferramenta: Documento de discovery + n8n (rascunho de fluxo)
  - Output: Spec técnica com fluxos a automatizar, integrações necessárias, estimativa de complexidade
- 2.2 Validar spec técnica com o cliente
  - Ferramenta: Google Meet ou WhatsApp
  - Output: Spec aprovada com ajustes documentados
- 2.3 Criar ambiente de staging
  - Ferramenta: AWS, Supabase, n8n
  - Output: Ambiente de staging configurado e funcionando

> ⚠️ Ponto de decisão: Spec técnica aprovada pelo cliente?
> SIM: avança para Fase 3
> NÃO: revisa spec e agenda nova validação (máximo 1 ciclo de revisão incluído no escopo)

**Critério de conclusão da fase:** Spec técnica aprovada + ambiente de staging ativo

---

## Fase 3: Build e Testes (Responsável: Engenheiro de Automação)

**Passos:**
- 3.1 Desenvolver os fluxos de automação conforme spec aprovada
  - Ferramenta: n8n, Claude Code, AWS, Supabase
  - Output: Fluxos implementados em staging
- 3.2 Executar testes com dados reais do cliente
  - Ferramenta: n8n (logs), Supabase (dados)
  - Output: Relatório de testes com casos de sucesso e erro
- 3.3 Executar checklist de qualidade pré-entrega
  - Ferramenta: Checklist de Qualidade Pré-Entrega (SOP interno)
  - Output: Checklist 100% completo

> ⚠️ Ponto de decisão: Checklist de qualidade 100% aprovado?
> SIM: avança para Fase 4
> NÃO: corrige itens reprovados e reexecuta checklist

**Critério de conclusão da fase:** Checklist de qualidade 100% aprovado com dados reais

---

## Fase 4: Validação com Cliente e Go-live (Responsável: CEO + Engenheiro)

**Passos:**
- 4.1 Agendar demo de validação com o cliente
  - Ferramenta: Google Meet
  - Output: Demo agendada
- 4.2 Conduzir demo e coletar aprovação
  - Ferramenta: Google Meet + sistema em staging
  - Output: Aprovação formal do cliente (email ou WhatsApp registrado)
- 4.3 Realizar deploy em produção
  - Ferramenta: AWS, n8n, Supabase
  - Output: Sistema rodando em produção
- 4.4 Entregar documentação e acesso ao cliente
  - Ferramenta: Obsidian/Notion (docs) + email
  - Output: Cliente com acesso e documentação de uso entregue
- 4.5 Ativar monitoramento e alertas
  - Ferramenta: AWS CloudWatch, n8n (logs ativos)
  - Output: Alertas configurados para falhas críticas

**Critério de conclusão da fase:** Sistema em produção + cliente operando de forma autônoma + retainer mensal ativado

**Critério de conclusão do processo:** Cliente com sistema em produção, documentação entregue, monitoramento ativo e primeiro mês de retainer contratado

---

# Processo 2: Entrega de Automação

**Objetivo:** Desenvolver e entregar uma automação de processo (fluxo n8n ou sistema similar) do mapeamento técnico ao go-live em produção.
**Gatilho:** Spec técnica aprovada pelo cliente (ou demanda de novo fluxo dentro de retainer ativo)
**Output final:** Automação rodando em produção com documentação e monitoramento

## Fase 1: Análise e Design do Fluxo (Responsável: Engenheiro de Automação)

**Passos:**
- 1.1 Analisar o processo a ser automatizado (inputs, outputs, regras de negócio)
  - Ferramenta: Documento de discovery / spec do cliente
  - Output: Diagrama de fluxo com todas as condições e ramificações documentadas
- 1.2 Identificar integrações necessárias (APIs, webhooks, bancos de dados)
  - Ferramenta: Documentação das plataformas do cliente, Supabase, AWS
  - Output: Lista de integrações com credenciais necessárias
- 1.3 Validar diagrama de fluxo com CEO antes de iniciar build
  - Ferramenta: WhatsApp / email
  - Output: Diagrama aprovado internamente

> ⚠️ Ponto de decisão: Diagrama aprovado internamente?
> SIM: avança para Fase 2
> NÃO: revisa diagrama (máximo 1 ciclo interno antes de pedir esclarecimento ao cliente)

**Critério de conclusão da fase:** Diagrama de fluxo aprovado + integrações mapeadas

---

## Fase 2: Build (Responsável: Engenheiro de Automação)

**Passos:**
- 2.1 Configurar conexões e credenciais em staging
  - Ferramenta: n8n, Supabase, AWS
  - Output: Conexões testadas e funcionando em staging
- 2.2 Implementar o fluxo conforme diagrama
  - Ferramenta: n8n, Claude Code
  - Output: Fluxo implementado com tratamento de erros
- 2.3 Testar com dados reais (casos felizes e de erro)
  - Ferramenta: n8n (logs de execução), Supabase
  - Output: Relatório de testes com resultado por caso

**Critério de conclusão da fase:** Todos os casos de teste executados com resultado esperado

---

## Fase 3: Revisão e Deploy (Responsável: Engenheiro de Automação + CEO)

**Passos:**
- 3.1 Executar checklist de qualidade pré-entrega
  - Ferramenta: Checklist de Qualidade Pré-Entrega
  - Output: Checklist 100% aprovado
- 3.2 Realizar deploy em produção
  - Ferramenta: AWS, n8n, Supabase (ambiente de produção)
  - Output: Fluxo ativo em produção
- 3.3 Monitorar primeiras 24h após deploy
  - Ferramenta: AWS CloudWatch, n8n (logs)
  - Output: Confirmação de estabilidade em produção
- 3.4 Documentar a automação entregue
  - Ferramenta: Obsidian (pasta clientes ou operações)
  - Output: Documentação interna do fluxo (para manutenção futura)

> ⚠️ Ponto de decisão: Primeiras 24h estáveis sem erros críticos?
> SIM: entrega concluída, comunicar cliente
> NÃO: investigar causa raiz e corrigir antes de comunicar conclusão

**Critério de conclusão do processo:** Fluxo em produção estável por 24h + cliente comunicado + documentação interna registrada

---

# Processo 3: Entrega de Agente de IA

**Objetivo:** Desenvolver e entregar um agente de IA conversacional (atendimento, vendas, suporte ou operacional) do briefing ao deploy em produção.
**Gatilho:** Briefing do agente aprovado pelo cliente ou demanda dentro de retainer ativo
**Output final:** Agente em produção respondendo corretamente nos canais definidos

## Fase 1: Design do Agente (Responsável: Engenheiro de Automação + CEO)

**Passos:**
- 1.1 Definir persona, objetivo e escopo do agente
  - Ferramenta: Obsidian (documento de briefing)
  - Output: Briefing do agente (persona, tom, objetivos, limites do escopo)
- 1.2 Mapear fluxos conversacionais e casos de uso
  - Ferramenta: Obsidian / diagrama de fluxo
  - Output: Mapa de conversas com ramos principais e fallbacks
- 1.3 Definir integrações necessárias (CRM, WhatsApp, base de conhecimento)
  - Ferramenta: Supabase, WhatsApp Business API, n8n
  - Output: Lista de integrações com requisitos técnicos
- 1.4 Validar briefing e mapa conversacional com cliente
  - Ferramenta: Google Meet / WhatsApp
  - Output: Briefing aprovado pelo cliente

> ⚠️ Ponto de decisão: Briefing e mapa conversacional aprovados pelo cliente?
> SIM: avança para Fase 2
> NÃO: revisa e reagenda validação (máximo 1 ciclo de revisão no escopo)

**Critério de conclusão da fase:** Briefing aprovado + mapa conversacional definido

---

## Fase 2: Build do Agente (Responsável: Engenheiro de Automação)

**Passos:**
- 2.1 Configurar o modelo de IA e prompts base
  - Ferramenta: Claude Code, API Anthropic / OpenAI
  - Output: Agente respondendo ao prompt base corretamente
- 2.2 Integrar base de conhecimento ou dados do cliente
  - Ferramenta: Supabase (embeddings / RAG), n8n
  - Output: Agente com acesso à base de conhecimento do cliente
- 2.3 Implementar integrações de canal (WhatsApp, CRM, etc.)
  - Ferramenta: WhatsApp Business API, n8n, Supabase
  - Output: Agente recebendo e respondendo mensagens no canal definido
- 2.4 Testar casos de uso mapeados (casos felizes, bordas e fallbacks)
  - Ferramenta: WhatsApp (staging) / interface de teste
  - Output: Relatório de testes por caso de uso

**Critério de conclusão da fase:** Todos os casos de uso testados com resultados dentro dos critérios de qualidade

---

## Fase 3: Validação e Deploy (Responsável: Engenheiro + CEO)

**Passos:**
- 3.1 Executar checklist de qualidade pré-entrega
  - Ferramenta: Checklist de Qualidade Pré-Entrega
  - Output: Checklist 100% aprovado
- 3.2 Conduzir demo com cliente no canal de produção (staging)
  - Ferramenta: WhatsApp Business (staging) / interface demo
  - Output: Aprovação formal do cliente
- 3.3 Realizar deploy em produção
  - Ferramenta: AWS, n8n, WhatsApp Business API (produção)
  - Output: Agente ativo no canal de produção
- 3.4 Monitorar primeiras 48h em produção
  - Ferramenta: AWS CloudWatch, logs do n8n, Supabase
  - Output: Confirmação de estabilidade e qualidade das respostas

> ⚠️ Ponto de decisão: Primeiras 48h estáveis com qualidade de respostas aceitável?
> SIM: entrega concluída, documentar e comunicar cliente
> NÃO: investigar causa raiz, corrigir, reiniciar monitoramento

**Critério de conclusão do processo:** Agente em produção estável por 48h + cliente satisfeito + documentação interna do agente registrada

---

# Processo 4: Checklist de Qualidade Pré-Entrega

**Objetivo:** Validar que qualquer sistema (automação ou agente de IA) atende aos critérios mínimos de qualidade antes de ser apresentado ao cliente ou colocado em produção.
**Gatilho:** Conclusão da fase de build e testes internos (antes de qualquer demo ou deploy em produção)
**Output final:** Checklist 100% aprovado como gate de liberação para entrega

## Fase 1: Verificação Técnica (Responsável: Engenheiro de Automação)

**Passos:**
- 1.1 Testar todos os fluxos com dados reais (não dados mock ou fictícios)
  - Ferramenta: n8n (execuções reais), Supabase (dados de staging do cliente)
  - Output: Logs de execução com status de sucesso por fluxo
- 1.2 Testar cenários de erro e fallbacks
  - Ferramenta: n8n, logs de erro
  - Output: Confirmação de que erros são tratados graciosamente (sem crash, sem dado perdido)
- 1.3 Validar integrações com sistemas do cliente em staging
  - Ferramenta: Ambiente de staging, APIs do cliente
  - Output: Todas as integrações respondendo corretamente
- 1.4 Verificar segurança: credenciais armazenadas em variáveis de ambiente, sem hardcode
  - Ferramenta: Revisão de código / n8n (environment variables)
  - Output: Confirmação de que nenhuma credencial está exposta no código

> ⚠️ Ponto de decisão: Algum item crítico falhando?
> NÃO: avança para Fase 2
> SIM: corrigir e reexecutar checklist do início

**Critério de conclusão da fase:** Todos os itens técnicos verificados sem falha crítica

---

## Fase 2: Verificação de Documentação e Comunicação (Responsável: CEO / Responsável de Projeto)

**Passos:**
- 2.1 Confirmar que a documentação interna do sistema está atualizada
  - Ferramenta: Obsidian (operacoes/ ou clientes/)
  - Output: Doc interna atualizada com fluxos entregues
- 2.2 Preparar material de handoff para o cliente (se aplicável)
  - Ferramenta: Obsidian / Google Docs
  - Output: Guia de uso ou manual básico pronto
- 2.3 Agendar demo ou comunicar entrega ao cliente
  - Ferramenta: WhatsApp Business / email
  - Output: Demo agendada ou comunicação de conclusão enviada

**Critério de conclusão da fase:** Documentação interna atualizada + cliente comunicado

**Critério de conclusão do processo:** Checklist 100% aprovado (todos os itens das 2 fases concluídos) — sistema liberado para demo ou deploy em produção
