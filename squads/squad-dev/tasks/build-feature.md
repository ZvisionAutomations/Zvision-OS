# Task: Construir Feature

**Agente responsável:** @architect, @developer, @ux-engineer, @quality-gate, @security-dev, @devops  
**Workflow:** feature-build-cycle

## Input

```
<feature_spec>
$ARGUMENTS
</feature_spec>
```

## Fase 1 — Análise de Impacto (@architect)

1. Analisar spec e identificar arquivos afetados
2. Avaliar impacto na arquitetura atual
3. Definir abordagem de implementação
4. Identificar riscos e dependências

## Fase 2 — Implementação

- Se feature tem componente visual → @ux-engineer lidera, @developer apoia com JS
- Se feature é principalmente lógica/integração → @developer lidera
- Se ambos → @architect define split de responsabilidades

## Fase 3 — Quality Gate (@quality-gate)

1. Executar checklist de qualidade
2. Verificar que feature está de acordo com a spec
3. Testar edge cases

## Fase 4 — Segurança (@security-dev)

1. Auditar se feature introduz novos riscos
2. Especial atenção se feature toca: inputs, autenticação, dados externos

## Fase 5 — Deploy (@devops)

1. `git commit -m "feat: [descrição da feature]"`
2. Deploy e verificação em produção

## Definition of Done

- [ ] Feature funciona conforme spec
- [ ] @quality-gate: APPROVED
- [ ] @security-dev: CLEAR
- [ ] Deploy verificado em produção
