# Workflow: Feature Build Cycle

Ciclo completo de construção de feature — do brief ao deploy em produção.

## Fases

```
Brief → @architect → @ux-engineer/@developer → @quality-gate → @security-dev → @devops → Produção
```

### Fase 1: Arquitetura (15-30 min)
**Agente:** @architect
- Analisar requisitos e definir escopo técnico
- Definir estrutura de arquivos e componentes
- Documentar decisões e passar brief para implementadores

### Fase 2: Implementação (variável)
**Agentes:** @ux-engineer + @developer (conforme necessidade)
- @ux-engineer: HTML/CSS, componentes visuais
- @developer: JavaScript, lógica, integrações
- Handoff documentado entre os dois quando aplicável

### Fase 3: Quality Gate (15-30 min)
**Agente:** @quality-gate
- Executar code-quality-checklist.md
- Emitir veredicto: APPROVED / CHANGES_REQUIRED
- Se CHANGES_REQUIRED → retornar para Fase 2

### Fase 4: Security Review (10-20 min)
**Agente:** @security-dev
- Auditoria focada nos arquivos modificados
- Executar owasp checklist relevante
- Emitir veredicto: CLEAR / BLOCKED
- Se BLOCKED → retornar para @developer com issue específico

### Fase 5: Deploy (10-15 min)
**Agente:** @devops
- Executar deploy-checklist.md
- Commit, push, verificação em produção
- Reportar resultado para @dev-orqx

## Critérios de Avanço de Fase

| De → Para | Critério |
|-----------|---------|
| Fase 1 → 2 | @architect entregou brief com estrutura definida |
| Fase 2 → 3 | Implementação completa, testada manualmente |
| Fase 3 → 4 | @quality-gate: APPROVED (ou APPROVED_WITH_NOTES) |
| Fase 4 → 5 | @security-dev: CLEAR (ou WARNINGS) |
| Fase 5 → Concluído | @devops confirmou deploy em produção |

## Abortar Ciclo

Se qualquer fase retorna BLOCKED ou CHANGES_REQUIRED por mais de 2 iterações → escalar para @dev-orqx para decisão.
