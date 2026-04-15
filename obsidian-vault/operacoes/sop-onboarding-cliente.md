---
título: SOP — Onboarding de Cliente
tipo: sop
versão: 1.0
data: 2026-04-02
status: ativo
tags: [operacoes, onboarding, cliente, sop]
---

# SOP — Onboarding de Cliente

> **Objetivo:** Integrar um novo cliente do contrato assinado até o primeiro sistema em produção com monitoramento ativo.
> **Gatilho:** Contrato assinado + primeiro pagamento confirmado.
> **Output:** Sistema em produção, cliente operando de forma autônoma, retainer mensal ativo.

## Visão Geral do Processo

| Fase | Nome | Responsável | Prazo Estimado | Output |
|------|------|-------------|----------------|--------|
| 1 | Kick-off e Discovery | CEO / Resp. de Projeto | Dia 1-2 | Discovery preenchido + acessos validados |
| 2 | Mapeamento Técnico | Engenheiro de Automação | Dia 2-5 | Spec técnica aprovada + staging ativo |
| 3 | Build e Testes | Engenheiro de Automação | Dia 5-12 | Checklist de qualidade 100% aprovado |
| 4 | Validação e Go-live | CEO + Engenheiro | Dia 12-14 | Sistema em produção + retainer ativado |

---

## Fase 1: Kick-off e Discovery (CRÍTICO)

> [!WARNING] Esta fase define o escopo de todo o projeto. Lacunas no discovery geram retrabalho em todas as fases seguintes. Não avançar sem documento de discovery preenchido e acessos validados.

### 1.1 Enviar email de boas-vindas
- **Responsável:** CEO / Responsável de Projeto
- **Prazo:** Até 48h após confirmação de pagamento
- **Ferramenta:** Gmail + template de boas-vindas
- **Output:** Email enviado + reunião de kick-off agendada
- [ ] Template personalizado com nome do cliente e data da reunião
- [ ] Link Google Meet incluído
- [ ] Agenda da reunião descrita no email

### 1.2 Conduzir reunião de kick-off
- **Responsável:** CEO / Responsável de Projeto
- **Ferramenta:** Google Meet + documento de discovery (Obsidian)
- **Output:** Documento de discovery preenchido
- [ ] Processos-alvo de automação mapeados
- [ ] Ferramentas e sistemas do cliente identificados
- [ ] Objetivos de resultado esperados documentados
- [ ] Prazo e expectativas alinhadas

> [!TIP] Enviar o documento de discovery com 24h de antecedência aumenta a qualidade da reunião. O cliente chega preparado e o tempo de discovery cai pela metade.

### 1.3 Solicitar e validar acessos
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** Checklist de acessos (email / WhatsApp Business)
- **Output:** Todos os acessos necessários validados
- [ ] Lista de acessos necessários enviada ao cliente
- [ ] Cada acesso testado (login confirmado) em staging
- [ ] Acessos pendentes registrados com prazo para liberação

> ⚠️ Ponto de decisão: Todos os acessos liberados?
> SIM: avança para Fase 2
> NÃO: aguardar liberação (prazo máximo: 5 dias úteis). Registrar bloqueio no histórico do cliente.

**Critério de conclusão:** Documento de discovery preenchido + todos os acessos testados e confirmados.

---

## Fase 2: Mapeamento Técnico (CRÍTICO)

> [!WARNING] A spec técnica aprovada pelo cliente é o único documento que autoriza o início do build. Iniciar sem aprovação gera retrabalho garantido.

### 2.1 Elaborar spec técnica
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** n8n (rascunho de fluxo) + documento de discovery
- **Output:** Spec técnica com fluxos, integrações e estimativa de complexidade
- [ ] Todos os fluxos de automação mapeados no documento
- [ ] Integrações necessárias listadas com requisitos de API/credenciais
- [ ] Complexidade estimada por fluxo
- [ ] Riscos técnicos identificados

### 2.2 Validar spec com o cliente
- **Responsável:** CEO + Engenheiro
- **Ferramenta:** Google Meet ou WhatsApp Business
- **Output:** Spec aprovada com ajustes documentados
- [ ] Spec apresentada ao cliente
- [ ] Aprovação formal registrada (email ou WhatsApp)
- [ ] Ajustes solicitados incorporados

### 2.3 Criar ambiente de staging
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** AWS, Supabase, n8n
- **Output:** Ambiente de staging configurado e funcional
- [ ] Instância n8n de staging ativa
- [ ] Banco de dados Supabase de staging configurado
- [ ] Conexões com sistemas do cliente em staging testadas

> ⚠️ Ponto de decisão: Spec técnica aprovada pelo cliente?
> SIM: avança para Fase 3
> NÃO: revisar spec e agendar nova validação (máximo 1 ciclo incluído no escopo).

**Critério de conclusão:** Spec técnica aprovada pelo cliente + ambiente de staging ativo.

---

## Fase 3: Build e Testes

### 3.1 Desenvolver os fluxos conforme spec
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** n8n, Claude Code, AWS, Supabase
- **Output:** Fluxos implementados em staging

### 3.2 Executar testes com dados reais
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** n8n (logs de execução), Supabase
- **Output:** Relatório de testes com resultado por caso de uso
- [ ] Casos de sucesso testados e aprovados
- [ ] Cenários de erro testados e tratados
- [ ] Fallbacks funcionando conforme spec

### 3.3 Executar Checklist de Qualidade Pré-Entrega
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** [[checklist-qualidade-preentrega]]
- **Output:** Checklist 100% aprovado

> ⚠️ Ponto de decisão: Checklist 100% aprovado?
> SIM: avança para Fase 4
> NÃO: corrigir itens reprovados e reexecutar checklist.

**Critério de conclusão:** Checklist de qualidade 100% aprovado com dados reais do cliente.

---

## Fase 4: Validação com Cliente e Go-live

### 4.1 Conduzir demo de validação
- **Responsável:** CEO + Engenheiro
- **Ferramenta:** Google Meet + sistema em staging
- **Output:** Aprovação formal do cliente

### 4.2 Deploy em produção
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** AWS, n8n, Supabase (produção)
- **Output:** Sistema rodando em produção

### 4.3 Entregar documentação e acessos ao cliente
- **Responsável:** CEO / Responsável de Projeto
- **Ferramenta:** Obsidian (guia de uso) + email
- **Output:** Cliente com acesso e documentação de uso em mãos
- [ ] Guia de uso enviado ao cliente
- [ ] Acessos de produção transferidos / configurados para o cliente
- [ ] Canal de suporte explicado

### 4.4 Ativar monitoramento e alertas
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** AWS CloudWatch, n8n (logs)
- **Output:** Alertas configurados para falhas críticas
- [ ] Alertas de erro crítico ativados
- [ ] Canal de recebimento de alertas configurado (email / WhatsApp)

**Critério de conclusão:** Sistema em produção + cliente operando de forma autônoma + retainer mensal ativado.

---

## Ferramentas e Integrações

| Ferramenta | Uso no processo |
|------------|----------------|
| Gmail | Email de boas-vindas e comunicações formais |
| Google Meet | Reuniões de kick-off, validação de spec e demo |
| WhatsApp Business | Comunicação ágil com o cliente |
| n8n | Build e execução dos fluxos de automação |
| Claude Code | Desenvolvimento de lógica customizada |
| AWS | Infraestrutura de staging e produção |
| Supabase | Banco de dados dos sistemas entregues |
| AWS CloudWatch | Monitoramento e alertas em produção |
| Obsidian | Documentação interna (discovery, spec, guia de uso) |

---

## Histórico de Versões

| Versão | Data | Autor | Mudança |
|--------|------|-------|---------|
| 1.0 | 2026-04-02 | SOP Factory | Versão inicial |
