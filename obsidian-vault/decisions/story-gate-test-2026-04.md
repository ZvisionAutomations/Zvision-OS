---
name: story-gate-test-2026-04
date: 2026-04-04
status: decided
---
# Teste do Story Gate — Sprint B

## O que foi testado

Story Gate hook interceptando implementação direta sem spec.
Todos os 3 hooks testados e validados.

## Resultados

### Hook 1: Story Gate (enforce-story-gate.js)
- **Teste bloqueio:** `Write` com "adicionar campo de telefone" → `decision: block` ✅
- **Teste allow:** `Write` com "fase 1 — spec aprovada story-001" → `decision: allow` ✅
- **Comportamento:** Bloqueia quando há intenção de implementação sem marcador de spec

### Hook 2: Git Push Authority (enforce-git-push.js)
- **Teste bloqueio:** `Bash` com "git push --force origin main" → `decision: block` ✅
- **Comportamento:** Bloqueia force push, permite git push normal

### Hook 3: Token Guardian (token-guardian.js)
- **Comportamento:** Bloqueia Write/Edit com patterns de secrets (ghp_, sk-ant-, etc.)

## Comportamento correto confirmado
Story Gate bloqueia → usuário roda /pwf-brainstorm → spec é criada → trabalho é liberado

## Status
✅ Todos os hooks funcionando conforme Artigo III e IX da Constitution

## Registrado em
`.claude/settings.json` — PreToolUse hook, matcher: "*"
