# Task: Code Review

**Agente responsável:** @quality-gate (lidera), @security-dev (se necessário)  
**Workflow:** N/A (task standalone)

## Input

```
<code_to_review>
$ARGUMENTS
</code_to_review>
```

## Processo

1. @quality-gate lê o código completo
2. Executa `code-quality-checklist.md`
3. Se há inputs externos ou integrações → acionar @security-dev
4. Emitir relatório com issues por severidade
5. Emitir veredicto final

## Formato do Relatório

```
## Code Review — [Nome do Arquivo/Feature]
Data: [data]
Revisor: @quality-gate

### Issues Encontrados

| # | Arquivo | Linha | Severidade | Descrição | Sugestão |
|---|---------|-------|-----------|-----------|----------|
| 1 | styles.css | 42 | HIGH | Cor hardcoded (#3B82F6) | Usar var(--color-primary) |
| 2 | main.js | 87 | CRITICAL | innerHTML com dado externo | Usar textContent |

### Veredicto: CHANGES_REQUIRED

Issues críticos devem ser resolvidos antes do merge.
```
