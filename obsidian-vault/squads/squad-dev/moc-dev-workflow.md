---
name: moc-dev-workflow
squad: squad-dev
type: moc
description: Fluxos de trabalho do Development Squad — Story Development Cycle, QA Loop e Spec Pipeline
---
# Dev Workflow

## Story Development Cycle (fluxo principal)
Todo desenvolvimento começa com o [[dev-sprint-lead]] criando a story,
que passa por validação do [[dev-product-lead]] antes de liberar
o [[dev-developer]] para implementar. O [[dev-quality-gate]] roda
7 quality checks com verdict PASS/FAIL antes do [[dev-devops]] fazer push.

## QA Loop
Quando o [[dev-quality-gate]] retorna REJECT, o [[dev-developer]]
corrige e re-submete — máximo 5 iterações automáticas antes de
escalar para Miguel (Board).

## Spec Pipeline
Features complexas passam pelo [[spec-pipeline]] antes da implementação:
Requisitos → Arquitetura → Pesquisa → Spec → Critique → Plan.
O [[dev-analyst]] conduz a pesquisa, o [[dev-architect]] valida.

## Ferramentas do squad
O [[psters-workflow]] governa toda execução com os comandos
/pwf-brainstorm → /pwf-plan → /pwf-work-plan → /pwf-review.
O [[gstack]] complementa com /review (Staff Engineer) e /qa (browser real).
