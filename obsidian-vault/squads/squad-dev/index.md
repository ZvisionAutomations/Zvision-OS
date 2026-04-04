---
name: squad-dev-index
description: Entry point do Development Squad — implementação, arquitetura, QA e DevOps no Zvision-OS
type: index
---
# Development Squad

O squad de desenvolvimento opera sob a [[sinapse-constitution]] com
[[story-gate]] obrigatório — nenhum código sem spec aprovada.
Todo trabalho segue o [[psters-workflow]]: brainstorm → plan → work-plan.

## Agentes principais
- [[dev-developer]] (Pixel) — implementação de código e stories
- [[dev-architect]] (Stratum) — arquitetura e decisões técnicas
- [[dev-quality-gate]] (Litmus) — QA e quality gates
- [[dev-devops]] (Pipeline) — CI/CD, git, releases

## Domínios
- [[moc-dev-workflow]] — como o squad opera e fluxos de trabalho
- [[moc-dev-architecture]] — padrões de arquitetura do Zvision
- [[moc-dev-quality]] — critérios de qualidade e testes

## Quando usar este squad
Qualquer implementação de feature, refatoração, debug ou migration
começa aqui via [[psters-workflow]]. O [[story-gate]] garante que
nenhuma linha é escrita sem spec validada pelo [[dev-product-lead]].
