---
name: agentes-ia
description: Serviço de agentes de IA customizados — arquitetura, entrega e diferencial da Zvision
---
# Agentes de IA

## O que diferencia um agente de uma automação simples

Uma automação executa um fluxo fixo: gatilho → ação → fim. Um agente toma decisões: lê contexto, escolhe o próximo passo, persiste memória entre sessões, escala ou recua conforme o resultado. O cliente contrata um agente quando o problema não é "fazer X sempre que Y acontece", mas "resolver Z da melhor forma possível dado o contexto atual".

## Quando o [[sop-entrega-agente-ia]] é ativado

Assim que a proposta é aceita, o [[sop-entrega-agente-ia]] entra em operação: define arquitetura, configura memória, testa comportamento com cenários reais, documenta o handoff. Sem esse protocolo, entrega vira improvisação.

## Stack técnica

O agente conversa com o cliente via Claude, acessado através da [[anthropic-api]]. A memória institucional — histórico de decisões, contexto de clientes, padrões aprendidos — fica no [[obsidian-vault]], que se torna ativo do cliente ao final do projeto. A orquestração de múltiplos agentes em paralelo é feita pelo [[paperclip]], com roteamento eficiente via [[bridge-http]].

## Gatilhos de venda

O cliente descreve o padrão antes de reconhecê-lo: "precisaria de alguém que soubesse tudo sobre minha empresa e me respondesse na hora", "meu time perde tempo buscando informação que já existe em algum lugar", "quero que quando um cliente pergunte algo, a resposta venha consistente, não dependa de quem atende".

## Como o [[brain-scott]] e o [[gstack]] aceleram a entrega

O [[brain-scott]] estrutura o desenvolvimento em stories com critérios de aceitação — cada agente é um projeto com épico, roadmap e QA. O [[gstack]] automatiza os testes de UI e comportamento, garantindo que o agente funciona como esperado antes de ir para o cliente.

## Precificação base

- Setup único: a definir com base na complexidade do agente e número de integrações
- Manutenção mensal: a definir
- Regra de bolso: agentes substituem função parcial de uma pessoa — o ticket deve refletir isso
