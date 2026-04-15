---
name: moc-seguranca
description: Tudo sobre segurança da Zvision — auditorias realizadas, decisões aceitas, padrões adotados
---
# Segurança

## Auditorias realizadas
- [[security-audit-landing-2026-03]] — audit completo da landing page, 10 findings, todos resolvidos

## Padrões adotados
- [[rate-limiting-padrao]] — 5 req/60s por IP, retorna 429 + Retry-After
- [[honeypot-pattern]] — campo CSS-hidden, descarte silencioso se preenchido
- [[headers-padrao]] — CSP, X-Frame-Options, XCTO, Referrer, Permissions, COOP, HSTS

## Riscos aceitos
- [[sri-google-fonts]] — SRI impraticável em CDN dinâmico, mitigado por CSP

Todo projeto novo entregue pela Zvision — especialmente [[landing-sites]] — passa pelo [[checklist-qualidade-preentrega]] antes do deploy, garantindo que o [[rate-limiting-padrao]], o [[honeypot-pattern]] e os [[headers-padrao]] estão implementados.
