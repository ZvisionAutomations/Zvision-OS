# ZVISION LANDING — SECURITY AUDIT REPORT

**Data:** 2026-03-31
**Target:** Zvision Landing Page — `zvision-landing.vercel.app`
**Stack:** Vanilla HTML/CSS/JS (static) + Vercel Edge Function (`/api/contact.js`)
**Auditor:** Cybersecurity Squad — Cyber Chief / Security Engineer

---

## FINDINGS

---

### [CRÍTICO] Rate Limiting Ausente em `/api/contact`

**Risco:** Qualquer atacante (ou bot) podia enviar POST requests ilimitados ao endpoint
sem qualquer controle de frequência. Isso permite:
- Flood de notificações no Telegram do operador (DoS operacional)
- Spam massivo de leads falsos no pipeline de vendas
- Esgotamento de quota da Telegram Bot API

**Evidência:** O arquivo `api/contact.js` original não continha nenhum mecanismo de
rate limiting. Nenhuma verificação de IP, timestamp ou contador de requisições.

**Fix aplicado:** Rate limiting in-memory por IP: máximo 5 requisições por janela de
60 segundos. Requisições excedentes retornam HTTP 429 com header `Retry-After: 60`.

**Status: FIXED** — `api/contact.js` L4–22

---

### [CRÍTICO] Ausência de Sanitização de Input

**Risco:** Strings brutas enviadas pelo usuário eram concatenadas diretamente na
mensagem do Telegram sem qualquer limpeza. Embora o Telegram não execute JavaScript,
os vetores de risco incluem:
- Injeção de Markdown no Telegram (negrito/links não autorizados na mensagem)
- Payload de controle (`\r\n` injection) que manipula o formato da mensagem
- Strings excessivamente longas causando falhas na API do Telegram (limite de 4096 chars)
- Preparação de superfície para payloads mais complexos no futuro

**Evidência:** Linha 39–49 do `api/contact.js` original: `${nome}`, `${email}`, etc.
interpolados diretamente sem qualquer escape ou limite de comprimento.

**Fix aplicado:** Função `sanitize()` que:
- Remove caracteres de controle (U+0000–U+001F exceto newlines permitidos)
- Escapa `<` e `>` para `&lt;` / `&gt;`
- Trunca por campo: nome (100), email (254), empresa (200), mensagem (1000)

**Status: FIXED** — `api/contact.js` L24–32

---

### [ALTO] HTTP Security Headers Ausentes

**Risco:** Sem headers de segurança, o site estava vulnerável a:
- **Clickjacking** (X-Frame-Options / CSP `frame-ancestors` ausentes): qualquer
  site pode embedar a landing em um `<iframe>` para enganar usuários
- **MIME sniffing** (X-Content-Type-Options ausente): browsers podem interpretar
  respostas com tipos MIME incorretos
- **Data leakage via Referer** (Referrer-Policy ausente): URLs completas enviadas
  a terceiros (Google Fonts, etc.)
- **Feature abuse** (Permissions-Policy ausente): acesso não declarado a câmera,
  microfone, geolocalização
- **XSS via script injection** (CSP ausente): sem restrição de origens de scripts

**Evidência:** `vercel.json` original continha apenas `{ "framework": null }`.

**Fix aplicado:** Headers adicionados via `vercel.json` para todas as rotas `(.*)`:
- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()`
- `Cross-Origin-Opener-Policy: same-origin`
- `Content-Security-Policy`: restringe scripts a `'self' + 'unsafe-inline'`,
  estilos a `'self' + fonts.googleapis.com`, fontes a `fonts.gstatic.com`,
  conexões a `'self'`, e bloqueia framing via `frame-ancestors 'none'`

**Status: FIXED** — `vercel.json`

---

### [ALTO] Error Responses Expondo Detalhes Internos

**Risco:** Dois tipos de leakage encontrados no handler original:
1. `{ error: 'Missing env vars' }` — confirma ao atacante que variáveis de ambiente
   estão ausentes/mal configuradas, útil para fingerprinting de configuração
2. `{ error: 'Telegram error', detail: err }` — retornava o corpo bruto da resposta
   de erro da Telegram API para o cliente, podendo expor o chat ID ou detalhes
   do token em mensagens de erro da API

**Evidência:** `api/contact.js` original L30–35 e L61–64.

**Fix aplicado:** Todas as respostas de erro internas agora retornam mensagens
genéricas: `'Service unavailable'` ou `'Invalid request'`. Nenhum detalhe interno
ou de sistemas externos é propagado ao cliente.

**Status: FIXED** — `api/contact.js` L109–115, L145–163

---

### [MÉDIO] Ausência de Campo Honeypot (Anti-bot)

**Risco:** O formulário aceitava qualquer submissão automatizada sem mecanismo
de detecção de bots. Sem CAPTCHA e sem honeypot, bots podiam submeter o formulário
livremente (até o rate limit ser atingido por IP, o que não protegia contra
múltiplos IPs distribuídos).

**Fix aplicado:** Campo `<input name="website">` invisível ao usuário via CSS
(`position:absolute; left:-9999px`), mas preenchível por bots que fazem scraping
de campos de formulário. O campo possui `tabindex="-1"` e `autocomplete="off"`.

Quando o campo `website` tem qualquer valor na requisição à API, o handler retorna
HTTP 200 silenciosamente sem encaminhar para o Telegram (não revela ao bot que
foi detectado).

**Status: FIXED** — `index.html` L2360–2365, `api/contact.js` L83–88

---

### [MÉDIO] CORS Irrestrito em `/api/contact`

**Risco:** O endpoint original não definia nenhuma política CORS. Embora browsers
bloqueiem requisições cross-origin sem CORS permissivo, a ausência de headers
explícitos:
- Não restringia origens em ambientes onde CORS não é aplicado (ex: curl, Postman,
  outros servidores)
- Não comunicava política de origem intencional

**Fix aplicado:** CORS configurado para aceitar apenas `https://zvision-landing.vercel.app`.
Preflight OPTIONS retorna 204 com headers adequados.

**Status: FIXED** — `api/contact.js` L38–50

---

### [MÉDIO] `.gitignore` Incompleto para Arquivos `.env`

**Risco:** O `.gitignore` original cobria apenas `.env.local`. Um arquivo `.env`
genérico ou `.env.production` acidentalmente criado na raiz do projeto seria
commitado ao repositório, expondo secrets.

**Fix aplicado:** `.gitignore` atualizado para cobrir `.env`, `.env.local` e
`.env.*` (todos os arquivos de ambiente).

**Status: FIXED** — `.gitignore`

---

### [BAIXO] CDN de Fontes (Google Fonts) sem SRI Hashes

**Risco:** As fontes JetBrains Mono e Space Grotesk são carregadas via
`fonts.googleapis.com` sem atributos `integrity` (Subresource Integrity).
Se o CDN for comprometido, CSS/fontes maliciosos poderiam ser injetados.

**Limitação técnica:** O Google Fonts CDN gera URLs dinâmicas com parâmetros
de cache — aplicar SRI estático é inviável com a implementação atual via `<link>`.
O risco é mitigado parcialmente pelo CSP que restringe `font-src` a
`fonts.gstatic.com` e `style-src` a `fonts.googleapis.com`.

**Status: ACCEPTED RISK** — Mitigação parcial via CSP. SRI completo exigiria
hospedar as fontes localmente.

---

### [INFO] Sem Secrets no Client-Side

**Verificação:** `grep -r "TELEGRAM|bot_token|chatid|BOT_TOKEN" . --include="*.js" --include="*.html"`

**Resultado:** Nenhuma referência a tokens ou secrets encontrada em código
client-side. `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID` existem apenas em
`api/contact.js` como `process.env.*` (server-side, Edge Function).

**Status: OK** — Nenhuma ação necessária.

---

### [INFO] Sem Console.logs em Produção

**Verificação:** Nenhum `console.log`, `console.error` ou `console.debug`
encontrado no JavaScript inline do `index.html` ou em `api/contact.js`.

**Status: OK** — Nenhuma ação necessária.

---

### [INFO] Sem Código Comentado ou Credenciais em Comentários

**Verificação:** Nenhum token, senha ou credencial encontrada em comentários
HTML ou JS.

**Status: OK** — Nenhuma ação necessária.

---

## RESUMO EXECUTIVO

| Severidade | Total | Corrigidos | Risco Aceito |
|------------|-------|------------|--------------|
| CRÍTICO    | 2     | 2          | 0            |
| ALTO       | 2     | 2          | 0            |
| MÉDIO      | 3     | 3          | 0            |
| BAIXO      | 1     | 0          | 1            |
| INFO       | 3     | —          | —            |
| **TOTAL**  | **8** | **7**      | **1**        |

Os padrões estabelecidos nesta auditoria — [[rate-limiting-padrao]], [[honeypot-pattern]] e [[headers-padrao]] — foram promovidos ao [[moc-seguranca]] como padrão obrigatório para todos os projetos [[landing-sites]] da Zvision. O único risco aceito, [[sri-google-fonts]], está documentado com mitigação via CSP.

---

## ARQUIVOS MODIFICADOS

| Arquivo | Mudanças |
|---------|----------|
| `api/contact.js` | Rate limiting, sanitização, CORS, honeypot, error hardening |
| `vercel.json` | HTTP security headers (CSP, X-Frame-Options, etc.) |
| `index.html` | Honeypot field + envio do campo no fetch payload |
| `.gitignore` | Cobertura de `.env` e `.env.*` |

---

## CHECKLIST PÓS-DEPLOY

- [ ] POST válido para `/api/contact` → mensagem chega no Telegram
- [ ] POST com campo `website` preenchido → retorna 200, SEM mensagem no Telegram
- [ ] 6 POSTs rápidos do mesmo IP → 6ª requisição retorna HTTP 429
- [ ] `curl -I https://zvision-landing.vercel.app` mostra todos os security headers
- [ ] DevTools → Network → Headers da resposta incluem CSP, X-Frame-Options, etc.
- [ ] Nenhum `console.log` visível no DevTools em produção
