# Task: Deploy para Vercel

**Agente responsável:** @devops  
**Workflow:** deploy-cycle

## Input

```
<deploy_context>
$ARGUMENTS
</deploy_context>
```

## Pré-condições (obrigatório antes de iniciar)

- [ ] @quality-gate emitiu APPROVED
- [ ] @security-dev emitiu CLEAR

## Processo

1. Executar `deploy-checklist.md` completo
2. `git status` — verificar arquivos a commitar
3. `git diff --staged` — revisar mudanças
4. `git add [arquivos específicos]`
5. `git commit -m "[tipo]: [descrição]"`
6. `git push origin main`
7. Aguardar deploy no Vercel (verificar em vercel.com/dashboard)
8. Testar URL de produção
9. Reportar resultado para @dev-orqx

## Em Caso de Falha

1. Verificar logs: `vercel logs [url]`
2. Identificar erro no build ou runtime
3. Acionar @developer para fix
4. Não fazer rollback sem consultar @dev-orqx

## Definition of Done

- [ ] Deploy completo sem erros
- [ ] URL de produção acessível e funcionando
- [ ] Funcionalidades críticas verificadas em produção
