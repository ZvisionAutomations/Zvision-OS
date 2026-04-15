# Deploy Checklist — Squad Dev

Executado por @devops antes de qualquer push para produção.

## Pré-Deploy

- [ ] @quality-gate emitiu veredicto `APPROVED` ou `APPROVED_WITH_NOTES`
- [ ] @security-dev emitiu veredicto `CLEAR` ou `WARNINGS` (nunca `BLOCKED`)
- [ ] Todos os arquivos necessários estão no staging (`git status` revisado)
- [ ] Sem arquivos `.env` ou de secrets no staging
- [ ] Mensagem de commit descritiva em português (formato: `tipo: descrição`)

## Git

- [ ] `git diff --staged` revisado — apenas mudanças esperadas
- [ ] Branch correta selecionada (`main` para produção, feature branch para preview)
- [ ] Sem conflitos de merge pendentes

## Vercel

- [ ] Variáveis de ambiente configuradas no Vercel dashboard (não em código)
- [ ] Build passa localmente antes de fazer push (`vercel dev` ou build manual)
- [ ] Domínio correto configurado para o deploy

## Pós-Deploy

- [ ] URL de produção acessível após deploy
- [ ] Funcionalidades críticas testadas na URL de produção
- [ ] Console do browser sem erros críticos
- [ ] Formulários e CTAs funcionando em produção
- [ ] Layout responsivo verificado (mobile e desktop)

## Rollback (se necessário)

- [ ] Identificar commit do deploy anterior: `git log --oneline -5`
- [ ] Reverter via Vercel dashboard (Deployments → Promote anterior)
- [ ] Ou: `git revert HEAD` → push → aguardar novo deploy
- [ ] Comunicar problema e solução ao @dev-orqx

---

**Aprovação final:** @devops confirma deploy bem-sucedido e documenta no histórico do projeto.
