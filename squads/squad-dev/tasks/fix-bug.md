# Task: Corrigir Bug

**Agente responsável:** @developer (diagnóstico + fix), @quality-gate (verificação), @devops (deploy)  
**Workflow:** bug-fix-cycle

## Input

```
<bug_report>
$ARGUMENTS
</bug_report>
```

## Fase 1 — Diagnóstico (@developer)

1. Reproduzir o bug localmente
2. Identificar root cause (não apenas o sintoma)
3. Documentar: qual arquivo, qual linha, qual é o comportamento atual vs esperado
4. Propor fix mínimo que resolve sem efeitos colaterais

## Fase 2 — Implementação (@developer)

1. Implementar fix focado — não refatorar código não relacionado
2. Testar: bug está corrigido
3. Testar: nada mais foi quebrado (regressão manual dos fluxos principais)
4. Documentar o fix com comentário se a causa não for óbvia

## Fase 3 — Verificação (@quality-gate)

1. Confirmar que bug está resolvido
2. Confirmar que não há regressões visíveis
3. Verificar se o fix introduz novos problemas de qualidade

## Fase 4 — Deploy (@devops)

1. `git add` (apenas arquivos do fix)
2. `git commit -m "fix: [descrição concisa do bug corrigido]"`
3. `git push origin main`
4. Verificar em produção que o bug está corrigido

## Definition of Done

- [ ] Bug reproduzido e root cause identificado
- [ ] Fix implementado de forma cirúrgica
- [ ] Nenhuma regressão introduzida
- [ ] Deploy verificado em produção
