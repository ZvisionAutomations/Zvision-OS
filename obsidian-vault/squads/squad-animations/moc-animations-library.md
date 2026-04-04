---
name: moc-animations-library
squad: squad-animations
type: moc
description: Biblioteca de efeitos de animação prontos para reutilização — CSS, Three.js e particles
---
# Animations Library

## Princípio de reutilização
O [[threejs-architect]] e o [[css-motion-artist]] documentam cada
efeito implementado aqui para reutilização. Antes de criar uma
nova animação, o [[squad-dev]] consulta esta biblioteca —
IDS principle: REUSE > ADAPT > CREATE.

## Efeitos CSS prontos
Fade in com slide (mount/unmount de modais), scroll-triggered reveal,
hover com depth effect, skeleton loading. Todos implementados
como CSS custom properties para fácil customização via [[moc-design-system]].

## Performance como critério
O [[animation-performance-engineer]] valida que todo efeito
roda em 60fps em mobile mid-range. Qualquer animação que cause
layout thrash ou force repaint em cada frame é rejeitada.

## Quando chamar o squad-animations
O [[squad-dev]] chama este squad quando a animação não consegue
ser resolvida com CSS transitions. Efeitos de partículas,
3D, shaders e timeline complexas são domínio deste squad.
