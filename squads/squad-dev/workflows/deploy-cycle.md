# Workflow: Deploy Cycle

Ciclo de deploy — quando o código já está pronto e aprovado.

## Pré-condições

- @quality-gate: APPROVED
- @security-dev: CLEAR

## Fases

```
Código aprovado → @devops (review final) → commit → push → verificação → Produção
```

### Fase 1: Review Final do @devops (5 min)
- `git status` — verificar arquivos
- `git diff --staged` — revisar mudanças
- Confirmar que nenhum arquivo sensível está incluído

### Fase 2: Commit e Push (2 min)
```bash
git add [arquivos específicos]
git commit -m "[tipo]: [descrição em português]"
git push origin main
```

### Fase 3: Verificação Pós-Deploy (5-10 min)
- Aguardar Vercel completar deploy (verificar dashboard)
- Acessar URL de produção
- Testar fluxo principal
- Verificar console do browser (sem erros críticos)

### Fase 4: Confirmação
- @devops reporta para @dev-orqx: "Deploy concluído — [URL]"
- Se houve issue → ver processo de Rollback em vercel-deployment-guide.md

## Tipos de Commit

| Tipo | Quando usar |
|------|-------------|
| `feat:` | Nova feature |
| `fix:` | Correção de bug |
| `refactor:` | Refatoração sem mudança de comportamento |
| `style:` | Mudanças de CSS/visual sem lógica |
| `chore:` | Dependências, configs, sem impacto no usuário |
| `docs:` | Documentação |
