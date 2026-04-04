---
name: squad-cybersecurity-index
description: Entry point do Cybersecurity Squad — segurança ofensiva e defensiva, pentest, compliance LGPD
type: index
---
# Cybersecurity Squad

O squad de segurança é ativado antes de todo deploy em produção
e em qualquer feature que toque dados sensíveis. Opera com
os [[owasp-top-10]] e [[stride-model]] como frameworks base.

## Agentes principais
- [[cyber-orqx]] — orquestrador, routing e diagnóstico
- [[cyber-red-team]] — pentest e análise ofensiva
- [[cyber-blue-team]] — defesa e hardening
- [[cyber-appsec]] — segurança de aplicação
- [[cyber-compliance]] — LGPD e compliance

## Domínios
- [[moc-cyber-webapp]] — segurança de aplicações web
- [[moc-cyber-infra]] — segurança de infraestrutura
- [[moc-cyber-compliance]] — LGPD e data protection

## Quando usar este squad
Obrigatório antes de qualquer deploy em produção via [[governance-workflow]].
O [[zvision-cso]] (Paperclip) aprova o relatório antes do merge.
Já executado: [[security-audit-landing-2026-03]], [[crm-audit-2026-04]].
