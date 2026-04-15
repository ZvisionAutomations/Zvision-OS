---
título: SOP — Entrega de Automação
tipo: sop
versão: 1.0
data: 2026-04-02
status: ativo
tags: [operacoes, entrega, automacao, sop]
---

# SOP — Entrega de Automação

> **Objetivo:** Desenvolver e entregar uma automação de processo do design técnico ao go-live em produção.
> **Gatilho:** Spec técnica aprovada pelo cliente (ou demanda de novo fluxo dentro de retainer ativo).
> **Output:** Automação rodando em produção com documentação interna e monitoramento ativo.

## Visão Geral do Processo

| Fase | Nome | Responsável | Prazo Estimado | Output |
|------|------|-------------|----------------|--------|
| 1 | Análise e Design do Fluxo | Engenheiro de Automação | Dia 1-2 | Diagrama de fluxo aprovado internamente |
| 2 | Build | Engenheiro de Automação | Dia 2-8 | Fluxo testado com dados reais |
| 3 | Revisão e Deploy | Engenheiro + CEO | Dia 8-10 | Fluxo em produção estável por 24h |

---

## Fase 1: Análise e Design do Fluxo (CRÍTICO)

> [!WARNING] Construir sem diagrama aprovado é a causa mais comum de retrabalho. Todo fluxo tem ramificações que só aparecem no papel. Mapear antes de buildar.

### 1.1 Analisar o processo a ser automatizado
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** Spec do cliente / documento de discovery
- **Output:** Diagrama de fluxo com inputs, outputs, condições e ramificações
- [ ] Gatilho do fluxo definido (webhook, schedule, evento manual)
- [ ] Todos os ramos de decisão mapeados (incluindo cenários de erro)
- [ ] Dados de entrada e saída de cada etapa documentados

### 1.2 Identificar integrações necessárias
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** Documentação das plataformas do cliente
- **Output:** Lista de integrações com credenciais necessárias
- [ ] APIs necessárias identificadas (endpoints, autenticação, rate limits)
- [ ] Acesso ao Supabase / AWS definido (tabelas, permissões)
- [ ] Credenciais necessárias solicitadas ao cliente se ainda não disponíveis

### 1.3 Validar diagrama internamente
- **Responsável:** CEO
- **Ferramenta:** WhatsApp / email interno
- **Output:** Diagrama aprovado internamente antes de iniciar build

> ⚠️ Ponto de decisão: Diagrama aprovado internamente?
> SIM: avança para Fase 2
> NÃO: revisar diagrama (máximo 1 ciclo). Se a lacuna for do cliente, agendar alinhamento.

**Critério de conclusão:** Diagrama de fluxo validado + integrações mapeadas + credenciais disponíveis.

---

## Fase 2: Build

### 2.1 Configurar conexões e credenciais em staging
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** n8n, Supabase, AWS
- **Output:** Todas as conexões testadas e funcionando em staging
- [ ] Credenciais armazenadas como variáveis de ambiente (sem hardcode)
- [ ] Conexão com cada API testada com chamada real

### 2.2 Implementar o fluxo conforme diagrama
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** n8n, Claude Code
- **Output:** Fluxo implementado com tratamento de erros em cada etapa
- [ ] Lógica implementada conforme diagrama aprovado
- [ ] Tratamento de erro em cada nó (sem falha silenciosa)
- [ ] Logs descritivos em pontos críticos do fluxo

### 2.3 Testar com dados reais
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** n8n (logs de execução), Supabase
- **Output:** Todos os casos de uso testados com resultado esperado
- [ ] Caso de sucesso executado com dados reais
- [ ] Cenário de erro forçado e tratado corretamente
- [ ] Fallback funcionando sem perda de dados

**Critério de conclusão:** Todos os casos de teste executados com resultado esperado.

---

## Fase 3: Revisão e Deploy

### 3.1 Executar Checklist de Qualidade Pré-Entrega
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** [[checklist-qualidade-preentrega]]
- **Output:** Checklist 100% aprovado

### 3.2 Deploy em produção
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** AWS, n8n, Supabase (produção)
- **Output:** Fluxo ativo em produção
- [ ] Variáveis de ambiente de produção configuradas (distintas de staging)
- [ ] Fluxo ativado e primeira execução monitorada

### 3.3 Monitorar primeiras 24h
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** AWS CloudWatch, n8n (logs)
- **Output:** Confirmação de estabilidade em produção
- [ ] Nenhum erro crítico nas primeiras 24h
- [ ] Performance dentro do esperado

### 3.4 Documentar internamente
- **Responsável:** Engenheiro de Automação
- **Ferramenta:** Obsidian (clientes/ ou operacoes/)
- **Output:** Documentação interna do fluxo para manutenção futura
- [ ] Diagrama final do fluxo salvo
- [ ] Credenciais e dependências documentadas
- [ ] Troubleshooting básico documentado

> ⚠️ Ponto de decisão: Primeiras 24h estáveis sem erro crítico?
> SIM: entrega concluída, comunicar cliente
> NÃO: investigar causa raiz, corrigir, reiniciar monitoramento de 24h.

**Critério de conclusão:** Fluxo em produção estável por 24h + cliente comunicado + documentação interna registrada.

---

## Ferramentas e Integrações

| Ferramenta | Uso no processo |
|------------|----------------|
| n8n | Build, execução e monitoramento dos fluxos |
| Claude Code | Desenvolvimento de lógica customizada e scripts |
| AWS | Infraestrutura e hosting em produção |
| Supabase | Banco de dados dos fluxos |
| AWS CloudWatch | Monitoramento e alertas em produção |
| WhatsApp Business | Comunicação de status com cliente |

---

## Histórico de Versões

| Versão | Data | Autor | Mudança |
|--------|------|-------|---------|
| 1.0 | 2026-04-02 | SOP Factory | Versão inicial |
