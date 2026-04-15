---
name: automacao-processos
description: Serviço de automação de processos com n8n, Make e Zapier — quando usar cada um, como precificar, como entregar
---
# Automação de Processos

## O que é e para quem

Automatiza fluxos repetitivos que consomem tempo operacional: notificações, integrações entre sistemas, qualificação de leads, envio de relatórios, onboarding de clientes. Indicado para empresas de 2 a 50 pessoas que ainda fazem manualmente o que poderia ser automático.

## Quando usar [[n8n]] vs [[make]] vs [[zapier]]

A escolha da ferramenta depende do perfil técnico do cliente e da complexidade do fluxo. O [[n8n]] é preferido quando o cliente tem capacidade técnica interna ou quando o fluxo é complexo e precisa de lógica customizada — é open-source, autogerenciado e sem custo por execução. O [[make]] entra quando o cliente quer interface visual sem complexidade técnica e o volume de execuções é controlado. O [[zapier]] é usado apenas quando o cliente já tem conta ativa ou quando a integração específica só existe nele — o custo por tarefa torna ele menos eficiente em escala.

## Como o [[sop-entrega-automacao]] guia a entrega

Toda entrega de automação segue o [[sop-entrega-automacao]]: levantamento de fluxo atual, mapeamento de gatilhos e ações, construção, teste com dados reais, handoff documentado. O [[checklist-qualidade-preentrega]] é obrigatório antes de entregar acesso ao cliente.

## Gatilhos de venda

O cliente está pronto para contratar quando descreve qualquer um destes sintomas: "minha equipe perde X horas por semana fazendo isso no braço", "sempre esqueço de mandar o relatório", "quando chega um lead novo, demoro para responder", "cada vez que integro dois sistemas é um pesadelo".

## Precificação base

- Setup único: a definir com base na complexidade do fluxo
- Manutenção mensal: a definir
- Regra de bolso: quanto mais o cliente economiza em hora humana, maior o valor que o serviço justifica

## Conexão com [[checklist-qualidade-preentrega]]

Nenhuma automação é entregue sem passar pelo [[checklist-qualidade-preentrega]]. Isso inclui teste de edge cases, validação de erros silenciosos, e documentação do fluxo entregue ao cliente.
