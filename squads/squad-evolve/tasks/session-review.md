---
id: session-review
name: Session Review
agent: evolve-chief
trigger: manual | auto (sessão com 3+ tasks)
---

# Task: session-review

## Objetivo
Capturar aprendizados da sessão atual e registrar no sistema de memória do Zvision-OS.

## Inputs
- Lista de squads utilizados nesta sessão
- Tasks concluídas
- Erros encontrados e como foram resolvidos
- Padrões observados

## Protocolo de Execução

### 1. Inventário da Sessão
```
Squads usados: [lista]
Tasks concluídas: [N]
Duração estimada: [tempo]
Complexidade: baixa | média | alta
```

### 2. Para cada squad usado
Ler `squads/{squad-id}/memory.md` (se existir) e atualizar com:
- O que funcionou bem neste squad
- Friction points (o que gerou mais esforço)
- Padrões novos identificados

### 3. Registrar em session-log.md
```markdown
## Sessão #N — YYYY-MM-DD — [título descritivo]

**Squads:** [lista]
**Padrões capturados:**
- [padrão 1]
- [padrão 2]

**Próximas otimizações:**
- [otimização 1]
```

### 4. Atualizar global-patterns.md
Se padrão novo identificado que vale para múltiplos squads, adicionar em `memory/global-patterns.md`.

### 5. Atualizar evolution-metrics.md
Incrementar contador de sessões.

## Output
```
⚡ Sessão #{N} registrada
   Squads: {lista}
   Padrões capturados: {N}
   Memory files atualizados: {N}
```
