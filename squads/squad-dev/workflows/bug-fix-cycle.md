# Workflow: Bug Fix Cycle

Ciclo de correção de bug — diagnóstico cirúrgico, fix focado, deploy.

## Fases

```
Bug Report → @developer (diagnóstico + fix) → @quality-gate → @devops → Produção
```

### Fase 1: Diagnóstico (5-15 min)
**Agente:** @developer
- Reproduzir o bug
- Identificar root cause (arquivo, linha, comportamento)
- Documentar: expected vs actual

### Fase 2: Fix (variável)
**Agente:** @developer
- Implementar fix mínimo e focado
- Testar: bug resolvido
- Testar: sem regressões nos fluxos principais
- Não aproveitar para refatorar código não relacionado

### Fase 3: Verificação (10-15 min)
**Agente:** @quality-gate
- Confirmar bug resolvido
- Verificar ausência de regressões
- Veredicto: APPROVED / CHANGES_REQUIRED

### Fase 4: Deploy (10 min)
**Agente:** @devops
- `git commit -m "fix: [descrição concisa]"`
- Push e verificação em produção

## Regra do Bug Fix

Fix cirúrgico: corrige exatamente o problema reportado, nada mais.
Se durante o diagnóstico encontrar outros bugs → documentar como novo bug report separado, não corrigir no mesmo PR.
