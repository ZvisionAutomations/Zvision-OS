# Task: Criar Landing Page

**Agente responsável:** @dev-orqx (orquestra), @architect, @ux-engineer, @developer, @quality-gate, @security-dev, @devops  
**Workflow:** feature-build-cycle

## Input

```
<landing_brief>
$ARGUMENTS
</landing_brief>
```

## Fase 1 — Arquitetura (@architect)

1. Analisar brief e definir:
   - Seções da página (hero, benefícios, prova social, CTA, FAQ, etc.)
   - Estrutura de arquivos (`index.html`, `css/styles.css`, `js/main.js`)
   - Assets necessários (imagens, fontes, ícones)
   - Integrações (formulário de contato, analytics, pixel de remarketing)
2. Documentar estrutura e passar para @ux-engineer

## Fase 2 — HTML/CSS (@ux-engineer)

1. Criar `index.html` com HTML semântico completo
2. Definir design tokens em `:root` (CSS variables)
3. Implementar layout mobile-first
4. Garantir acessibilidade (headings, alt, aria, contraste)
5. Passar para @developer para JS e integrações

## Fase 3 — JavaScript e Integrações (@developer)

1. Implementar interatividade (menu mobile, smooth scroll, animações)
2. Implementar formulário com validação client + fetch para API
3. Adicionar analytics/pixel se necessário
4. Testar manualmente no browser (Chrome + Firefox + mobile)

## Fase 4 — Quality Gate (@quality-gate)

1. Executar `code-quality-checklist.md` completo
2. Verificar responsivo em 3 breakpoints (mobile/tablet/desktop)
3. Verificar acessibilidade (teclado, contraste, screen reader básico)
4. Emitir veredicto: APPROVED / CHANGES_REQUIRED

## Fase 5 — Segurança (@security-dev)

1. Verificar secrets expostos
2. Verificar XSS risks (innerHTML com dados externos)
3. Verificar formulários validados server-side
4. Emitir veredicto: CLEAR / BLOCKED

## Fase 6 — Deploy (@devops)

1. Executar `deploy-checklist.md`
2. `git add` (arquivos específicos)
3. `git commit -m "feat: criar landing page [nome-cliente]"`
4. `git push origin main`
5. Verificar URL de produção após deploy

## Definition of Done

- [ ] Landing page acessível na URL de produção
- [ ] Funciona em mobile, tablet e desktop
- [ ] Formulário de contato envia corretamente
- [ ] @quality-gate: APPROVED
- [ ] @security-dev: CLEAR
- [ ] @devops: deploy verificado
