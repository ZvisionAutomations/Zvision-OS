---
name: landing-sites
description: Serviço de landing pages e sites — vanilla HTML/CSS/JS, Vercel, design system Zvision
---
# Landing Pages & Sites

## Stack

Todos os sites da Zvision são entregues em vanilla HTML/CSS/JS com deploy no [[vercel]] — sem framework por padrão. A decisão de não usar React ou Next.js é deliberada: sites estáticos carregam mais rápido, são mais simples de manter e têm superfície de ataque menor. O cliente recebe um arquivo que qualquer desenvolvedor entende.

## Como o [[design-squad]] e o [[gstack]] aceleram

O [[design-squad]] define estrutura visual, hierarquia e copy antes de uma linha de código ser escrita. O [[gstack]] roda QA automatizado após cada iteração — verifica console errors, performance, e que o formulário de contato está chegando no destino certo — sem precisar testar manualmente cada vez.

## Segurança embutida

Todo site entregue pela Zvision passa pelo padrão estabelecido no [[security-audit-landing-2026-03]]: [[rate-limiting-padrao]] no endpoint de contato, [[honeypot-pattern]] para bloquear bots silenciosamente, e [[headers-padrao]] via `vercel.json` cobrindo CSP, X-Frame-Options e HSTS. Isso não é opcional — está no [[checklist-qualidade-preentrega]].

## Quando oferecer junto com automação

[[landing-sites]] + [[automacao-processos]] é o combo natural para clientes que precisam capturar e qualificar leads. O formulário do site dispara uma automação que notifica o time, salva o lead no CRM, e inicia um fluxo de follow-up — tudo sem trabalho manual.

## Precificação base

- Setup único: a definir com base no escopo de páginas e integrações
- Manutenção mensal: a definir
- Regra de bolso: o valor é o cliente parar de depender de agências que demoram semanas para mudar uma linha de copy
