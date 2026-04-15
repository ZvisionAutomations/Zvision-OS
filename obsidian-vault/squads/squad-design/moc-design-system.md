---
name: moc-design-system
squad: squad-design
type: moc
description: Design system da Zvision — tokens, componentes e padrões visuais implementados
---
# Design System Zvision

## Tokens visuais
Todas as cores são CSS variables — nunca valores crus.
O [[dx-design-system-architect]] definiu:
--color-primary, --color-accent, --color-surface, --color-text
como a base. Qualquer componente novo usa exclusivamente esses tokens.

## Tipografia
Space Grotesk para UI e marketing copy.
JetBrains Mono para código e dados. Sem exceções —
o [[dev-architect]] bloqueia qualquer PR que use outra fonte.

## Componentes implementados
Os componentes do [[zvision-crm]] foram auditados pelo [[crm-audit-2026-04]].
O [[dx-ui-designer]] mantém a biblioteca de componentes documentada
em [[obsidian-vault/specs/]] para cada nova feature.

## Padrão de animação
Framer Motion apenas para mount/unmount complexos.
CSS transitions para microinterações — mais performático
e sem dependência de runtime JavaScript pesado.
O [[squad-animations]] é chamado apenas quando a animação
não consegue ser feita em CSS puro.
