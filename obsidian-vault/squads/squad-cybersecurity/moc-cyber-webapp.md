---
name: moc-cyber-webapp
squad: squad-cybersecurity
type: moc
description: Segurança de aplicações web — OWASP Top 10, headers, RLS, rate limiting e padrões implementados
---
# Web App Security

## Padrões implementados na Zvision
O [[security-audit-landing-2026-03]] estabeleceu os padrões base:
[[rate-limiting-padrao]] com 5 req/60s por IP retornando 429,
[[honeypot-pattern]] para anti-bot sem CAPTCHA, e
[[headers-padrao]] com CSP, X-Frame-Options, HSTS e COOP.

## RLS no Supabase
O [[crm-audit-2026-04]] confirmou que toda tabela do [[zvision-crm]]
tem [[rls-policy]] com isolamento por company_id. O [[cyber-appsec]]
bloqueia qualquer migration sem RLS via [[token-guardian]] hook.

## Riscos aceitos
O [[sri-google-fonts]] foi aceito como risco baixo — SRI é impraticável
em CDN dinâmico e o CSP já mitiga o vetor principal. Documentado em
[[moc-seguranca]].

## Checklist pré-deploy
Antes de qualquer deploy em produção, o [[cyber-orqx]] executa
o checklist do [[governance-workflow]]: headers presentes, RLS ativo,
rate limiting configurado, secrets fora do código.
