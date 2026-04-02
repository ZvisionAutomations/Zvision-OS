---
título: Checklist — Qualidade Pré-Entrega
tipo: checklist
versão: 1.0
data: 2026-04-02
status: ativo
tags: [operacoes, qualidade, checklist, entrega]
---

# Checklist de Qualidade Pré-Entrega

> **Uso:** Executar obrigatoriamente antes de qualquer demo ou deploy em produção.
> **Quem executa:** Engenheiro responsável pelo projeto.
> **Critério de liberação:** 100% dos itens [OBRIGATÓRIO] marcados. Itens [OPCIONAL] são recomendados mas não bloqueiam.

---

## Bloco 1: Funcionalidade

> [!WARNING] Nenhum sistema vai para produção sem dados reais. Testes com dados mock não valem como validação de entrega.

- [ ] **[OBRIGATÓRIO]** Todos os fluxos testados com dados reais do cliente (não mock ou ficticios)
- [ ] **[OBRIGATÓRIO]** Cenários de erro testados e tratados graciosamente (sem crash, sem dado perdido)
- [ ] **[OBRIGATÓRIO]** Todas as integrações com sistemas do cliente validadas em staging
- [ ] **[OBRIGATÓRIO]** Comportamento com inputs inesperados validado (o sistema falha bem?)
- [ ] **[OPCIONAL]** Performance sob carga testada (se o volume de uso for alto)
- [ ] **[OPCIONAL]** Tempo de resposta medido e dentro do aceitável para o caso de uso

---

## Bloco 2: Segurança

> [!WARNING] Credenciais hardcoded são risco de segurança imediato. Revisar antes de qualquer commit ou deploy.

- [ ] **[OBRIGATÓRIO]** Nenhuma credencial hardcoded no código ou configuração (usar variáveis de ambiente)
- [ ] **[OBRIGATÓRIO]** Credenciais de staging distintas das de produção (nunca usar as mesmas)
- [ ] **[OBRIGATÓRIO]** Acessos de produção documentados e armazenados de forma segura
- [ ] **[OPCIONAL]** Dados sensíveis do cliente criptografados em trânsito e em repouso

---

## Bloco 3: Documentação

- [ ] **[OBRIGATÓRIO]** Documentação interna do sistema atualizada (Obsidian: clientes/ ou operacoes/)
- [ ] **[OBRIGATÓRIO]** Diagrama ou descrição do fluxo final salvo (difere do diagrama de design se houve mudanças)
- [ ] **[OBRIGATÓRIO]** Dependências e integrações documentadas (quais APIs, tabelas, webhooks)
- [ ] **[OPCIONAL]** Guia básico de troubleshooting documentado (top 3 erros mais prováveis + solução)
- [ ] **[OPCIONAL]** Guia de uso preparado para o cliente (se o cliente vai operar o sistema)

---

## Bloco 4: Comunicação com Cliente

- [ ] **[OBRIGATÓRIO]** Demo agendada com o cliente antes do go-live em produção
- [ ] **[OBRIGATÓRIO]** Canal de suporte pós-entrega explicado ao cliente (WhatsApp, email)
- [ ] **[OPCIONAL]** Material de handoff preparado (documentação de uso para o time do cliente)

---

## Bloco 5: Go-live

> [!TIP] Nunca fazer deploy em produção em sexta-feira à tarde ou véspera de feriado. Problemas acontecem e a janela de resposta precisa ser ampla.

- [ ] **[OBRIGATÓRIO]** Variáveis de ambiente de produção configuradas e distintas de staging
- [ ] **[OBRIGATÓRIO]** Monitoramento ativo configurado (AWS CloudWatch, logs n8n)
- [ ] **[OBRIGATÓRIO]** Alertas de erro crítico ativados com canal de recebimento definido
- [ ] **[OBRIGATÓRIO]** Plano de rollback definido: como reverter se algo der errado em produção
- [ ] **[OPCIONAL]** Deploy realizado em horário de baixo tráfego (se aplicável ao caso do cliente)

---

## Aprovação Final

| Campo | Valor |
|-------|-------|
| Projeto | |
| Engenheiro responsável | |
| Data de execução | |
| Todos os itens [OBRIGATÓRIO] marcados? | SIM / NÃO |
| Sistema liberado para produção? | SIM / NÃO |
| Observações | |

> [!WARNING] Sistema com qualquer item [OBRIGATÓRIO] desmarcado NÃO está liberado para produção. Registrar a pendência e corrigir antes de prosseguir.

---

## Histórico de Versões

| Versão | Data | Autor | Mudança |
|--------|------|-------|---------|
| 1.0 | 2026-04-02 | SOP Factory | Versão inicial |
