---
name: squad-animations-index
description: Entry point do Animations Squad — motion design, CSS animations, partículas, Three.js e shaders
type: index
---
# Animations Squad

O squad de animações opera com [[threejs-architect]] para 3D,
[[css-motion-artist]] para animações CSS e [[shader-artist]] para
efeitos GLSL. Todo efeito implementado é documentado em
[[moc-animations-library]] com código reutilizável.

## Agentes principais
- [[animations-orqx]] (Kinetic) — orquestrador
- [[threejs-architect]] — Three.js e WebGL
- [[css-motion-artist]] — CSS animations e Framer Motion
- [[shader-artist]] — shaders GLSL e efeitos de partículas
- [[motion-choreographer]] — timing e coreografia de UI

## Domínios
- [[moc-animations-library]] — biblioteca de efeitos prontos
- [[moc-animations-performance]] — performance e otimização
- [[moc-animations-clients]] — projetos de motion para clientes

## Quando usar este squad
Criar animações premium para landing pages, efeitos visuais
para clientes, motion design de interface. O [[squad-design]]
define o conceito; o animations squad implementa o movimento.
Constraint: Framer Motion apenas para mount/unmount complexos.
