# Code Quality Checklist — Squad Dev

Use antes de qualquer merge ou deploy. @quality-gate é responsável pela execução.

## HTML

- [ ] HTML5 semântico: `section`, `article`, `nav`, `header`, `footer`, `main` usados corretamente
- [ ] Meta tags presentes: `charset`, `viewport`, `description`, `og:title`, `og:description`
- [ ] Imagens com atributo `alt` descritivo (não `alt=""` para imagens com conteúdo)
- [ ] Formulários com `label` associado a cada `input` (via `for`/`id`)
- [ ] Hierarquia de headings correta (H1 único por página, H2-H6 em sequência lógica)
- [ ] Links com texto descritivo (não "clique aqui" ou "saiba mais")

## CSS

- [ ] Nenhum valor de cor hardcoded — apenas `var(--color-*)`
- [ ] Nenhum valor de espaçamento hardcoded — apenas `var(--space-*)`
- [ ] Nenhum valor de tipografia hardcoded — apenas `var(--font-size-*)`, `var(--font-weight-*)`
- [ ] Mobile-first: breakpoints adicionam estilos (não sobrescrevem mobile)
- [ ] Sem `!important` sem justificativa documentada
- [ ] Sem `float` para layout (usar flexbox ou grid)
- [ ] Sem seletores de ID para estilo (apenas classes)

## JavaScript

- [ ] Sem `var` — apenas `const` e `let`
- [ ] Sem `innerHTML` com dados externos (usar `textContent` ou `DOMPurify`)
- [ ] Sem `eval()`
- [ ] Async/await em vez de callbacks aninhados
- [ ] Tratamento de erro em todas as operações async (`try/catch`)
- [ ] Event listeners removidos quando elemento é destruído
- [ ] Sem console.log() esquecido no código de produção

## Segurança (pré-auditoria do @security-dev)

- [ ] Sem API keys ou secrets no código
- [ ] Sem dados sensíveis em variáveis client-side acessíveis
- [ ] Inputs de usuário não usados diretamente em queries ou innerHTML
- [ ] CORS configurado corretamente (se aplicável)

## Acessibilidade

- [ ] Contraste de cores: mínimo 4.5:1 para texto normal, 3:1 para texto grande
- [ ] Focus ring visível em todos os elementos interativos
- [ ] Navegação por teclado funcional (Tab, Enter, Escape)
- [ ] `aria-label` ou `aria-labelledby` em elementos sem texto visível
- [ ] Skip link para conteúdo principal

## Performance

- [ ] Imagens com `loading="lazy"` (exceto above-the-fold)
- [ ] Scripts com `defer` ou `async` quando possível
- [ ] CSS crítico inline (above-the-fold) ou carregado sem bloquear render
- [ ] Sem imports desnecessários

## Código Geral

- [ ] Sem código comentado (dead code) — se não usa, remove
- [ ] Funções com nomes que descrevem o que fazem
- [ ] Variáveis com nomes descritivos (sem `x`, `temp`, `data` genéricos)
- [ ] Sem código duplicado que poderia ser função/componente

---

**Veredicto:**
- `APPROVED` — todos os itens CRITICAL marcados
- `APPROVED_WITH_NOTES` — apenas LOW/MEDIUM pendentes
- `CHANGES_REQUIRED` — qualquer item HIGH/CRITICAL não marcado
