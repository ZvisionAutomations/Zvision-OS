# Output Examples — SOP Factory

## Exemplo 1: SOP de Onboarding de Cliente (estrutura completa)

```markdown
---
título: SOP — Onboarding de Cliente
tipo: sop
versão: 1.0
data: 2026-04-01
status: ativo
responsavel: CEO
tags: [operacoes, onboarding, cliente, sop]
---

# SOP — Onboarding de Cliente

> **Objetivo:** Integrar novos clientes do contrato assinado até o primeiro fluxo em produção.
> **Gatilho:** Contrato assinado + primeiro pagamento confirmado.
> **Output:** Cliente ativo com automação rodando e acesso ao painel configurado.

## Visão Geral do Processo

| Fase | Nome | Responsável | Prazo | Output |
|------|------|-------------|-------|--------|
| 1 | Kick-off | CEO | Dia 1-2 | Discovery preenchido |
| 2 | Mapeamento técnico | Engenheiro de Automação | Dia 2-5 | Spec técnica aprovada |
| 3 | Configuração | Engenheiro de Automação | Dia 5-10 | Ambiente de staging |
| 4 | Validação | CEO + Cliente | Dia 10-12 | Aprovação do cliente |
| 5 | Go-live | Engenheiro de Automação | Dia 12-14 | Produção ativa |

---

## Fase 1: Kick-off (CRÍTICO)

> [!WARNING] Esta fase define o escopo de todo o projeto. Gaps no discovery geram retrabalho em todas as fases seguintes.

### 1.1 Email de boas-vindas
- **Responsável:** CEO
- **Prazo:** Até 4h após confirmação de pagamento
- **Ferramenta:** Gmail + template `onboarding-welcome`
- **Output:** Email enviado, reunião agendada em até 48h

- [ ] Template personalizado com nome do cliente e serviço contratado
- [ ] Link de reunião incluído (Google Meet)
- [ ] Documento de discovery anexado para preenchimento prévio

> [!TIP] Enviar o documento de discovery com 24h de antecedência melhora qualidade da reunião em ~40%.

### 1.2 Reunião de Kick-off
- **Responsável:** CEO
- **Duração:** 60-90 minutos
- **Ferramenta:** Google Meet + documento de discovery compartilhado
- **Output:** Documento de discovery preenchido e validado

- [ ] Objetivo do projeto confirmado com o cliente
- [ ] Processos-alvo identificados (mínimo 2)
- [ ] Acesso às ferramentas do cliente solicitado formalmente
- [ ] Próximos passos e timeline comunicados

> **Ponto de decisão:** Escopo é claro e viável? → **SIM:** avança para Fase 2 | **NÃO:** agenda call de refinamento antes de prosseguir

---

## Fase 2: Mapeamento Técnico

### 2.1 Solicitação de acessos
- Responsável: Engenheiro de Automação
- Ferramenta: Email / formulário de acessos
- Output: Lista de acessos confirmados ou pendências documentadas

### 2.2 Análise técnica do processo
- Responsável: Engenheiro de Automação
- Ferramenta: Obsidian + diagrama de fluxo
- Output: Spec técnica em formato Markdown

> **Ponto de decisão:** Spec aprovada pelo CEO? → **SIM:** avança | **NÃO:** revisar com cliente

---

## Histórico de Versões

| Versão | Data | Autor | Mudanças |
|--------|------|-------|---------|
| 1.0 | 2026-04-01 | Miguel | Criação inicial |
```

---

## Exemplo 2: Checklist de Qualidade Pré-Entrega (estrutura completa)

```markdown
---
título: Checklist — Qualidade Pré-Entrega
tipo: checklist
versão: 1.0
data: 2026-04-01
status: ativo
tags: [operacoes, qualidade, checklist, entrega, obrigatorio]
---

# Checklist de Qualidade Pré-Entrega

> **Uso:** Executar obrigatoriamente antes de qualquer entrega ao cliente.
> **Quem executa:** Engenheiro responsável pelo projeto.
> **Critério de aprovação:** 100% dos itens [OBRIGATÓRIO] marcados.

---

## Bloco 1: Funcionalidade

- [ ] **[OBRIGATÓRIO]** Todos os fluxos testados com dados reais (não mock)
- [ ] **[OBRIGATÓRIO]** Cenários de erro testados: input inválido, timeout, API fora do ar
- [ ] **[OBRIGATÓRIO]** Integrações com sistemas do cliente validadas em staging
- [ ] **[OBRIGATÓRIO]** Sem erros críticos nos logs das últimas 24h de teste
- [ ] **[OPCIONAL]** Performance sob carga testada (requisito: < 2s por transação)

## Bloco 2: Segurança

- [ ] **[OBRIGATÓRIO]** Credenciais armazenadas em variáveis de ambiente (nunca hardcoded)
- [ ] **[OBRIGATÓRIO]** Acesso ao painel restrito por autenticação
- [ ] **[OPCIONAL]** Rate limiting configurado em APIs públicas

## Bloco 3: Documentação

- [ ] **[OBRIGATÓRIO]** README do projeto atualizado com instruções de uso
- [ ] **[OBRIGATÓRIO]** Credenciais de acesso entregues de forma segura ao cliente
- [ ] **[OPCIONAL]** Vídeo de demonstração gravado (recomendado para automações complexas)

## Bloco 4: Comunicação com o Cliente

- [ ] **[OBRIGATÓRIO]** Email de entrega redigido e revisado
- [ ] **[OBRIGATÓRIO]** Data/hora de go-live alinhada com o cliente
- [ ] **[OBRIGATÓRIO]** Canal de suporte pós-entrega comunicado

---

> [!WARNING] Nenhuma entrega sai sem 100% dos itens [OBRIGATÓRIO] marcados. Em caso de dúvida, escalar para o CEO antes do go-live.

## Histórico de Versões

| Versão | Data | Autor | Mudanças |
|--------|------|-------|---------|
| 1.0 | 2026-04-01 | Miguel | Criação inicial |
```
