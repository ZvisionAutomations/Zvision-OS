# ZVISION CRM — PLANO DE AUDITORIA DE SEGURANCA

**Data:** 2026-04-03
**Target:** Zvision CRM (em desenvolvimento)
**Stack esperada:** Vanilla HTML/CSS/JS, Node.js, Vercel, WSL2 (alinhado com stack da agencia)
**Auditor:** Cybersecurity Squad — Cyber Chief
**Urgencia:** MEDIUM — sistema em desenvolvimento, sem exposicao ativa
**Status:** PRE-AUDIT PLAN — aguardando codigo disponivel para execucao

---

## 1. MAPA DE SUPERFICIE DE ATAQUE

Um CRM concentra os ativos mais criticos de uma agencia: dados de clientes, pipeline de vendas, comunicacoes internas e integracoes com ferramentas externas. A superficie de ataque esperada:

### 1.1 Autenticacao e Sessoes

| Vetor | Risco | Severidade |
|-------|-------|------------|
| Brute force em login | Acesso nao autorizado a contas | [CRITICO] |
| Ausencia de MFA | Comprometimento por credential stuffing | [CRITICO] |
| Sessoes sem expiracao | Sessao hijacking em maquinas compartilhadas | [ALTO] |
| Tokens JWT mal configurados (sem rotacao, sem expiracao curta) | Reutilizacao de token roubado | [ALTO] |
| Password reset flow inseguro | Account takeover via link previsivel | [ALTO] |
| Session fixation | Reutilizacao de session ID pre-autenticacao | [MEDIO] |

### 1.2 Autorizacao e Controle de Acesso

| Vetor | Risco | Severidade |
|-------|-------|------------|
| IDOR (Insecure Direct Object Reference) | Acesso a dados de clientes de outros usuarios | [CRITICO] |
| Falta de RBAC (Role-Based Access Control) | Usuarios com privilegio excessivo | [ALTO] |
| Privilege escalation vertical | Usuario comum acessa funcoes de admin | [CRITICO] |
| Privilege escalation horizontal | Usuario A acessa dados do usuario B | [CRITICO] |
| Endpoints de API sem autorizacao | Acesso direto via curl/Postman sem token | [CRITICO] |

### 1.3 Dados de Clientes (PII)

| Vetor | Risco | Severidade |
|-------|-------|------------|
| Dados em trânsito sem TLS | Interceptacao de nomes, emails, telefones | [CRITICO] |
| Dados em repouso sem criptografia | Exposicao em caso de breach do DB | [ALTO] |
| Logs contendo PII | Vazamento via logs de erro ou debug | [ALTO] |
| Export/download de dados sem controle | Exfiltracao massiva por insider | [ALTO] |
| Backups sem criptografia | Acesso a dumps de banco em texto claro | [MEDIO] |

### 1.4 Endpoints e APIs

| Vetor | Risco | Severidade |
|-------|-------|------------|
| Injecao SQL/NoSQL | Leitura/escrita arbitraria no banco | [CRITICO] |
| Mass assignment | Modificacao de campos protegidos via payload | [ALTO] |
| API sem rate limiting | DoS, brute force, scraping | [ALTO] |
| SSRF (Server-Side Request Forgery) | Acesso a recursos internos via API | [ALTO] |
| CORS permissivo | Cross-origin request de dominios maliciosos | [MEDIO] |
| Falta de validacao de content-type | Upload de payloads maliciosos | [MEDIO] |

### 1.5 Integracoes Externas

| Vetor | Risco | Severidade |
|-------|-------|------------|
| Webhooks sem validacao de assinatura | Injecao de dados falsos | [ALTO] |
| API keys hardcoded no client-side | Exfiltracao de credenciais | [CRITICO] |
| OAuth misconfiguration | Token theft, open redirect | [ALTO] |
| Dependencia de terceiros sem auditoria | Supply chain attack | [MEDIO] |
| Telegram Bot API token exposto | Controle do bot, leitura de mensagens | [CRITICO] |

### 1.6 Infraestrutura e Deploy

| Vetor | Risco | Severidade |
|-------|-------|------------|
| Environment variables expostas | Acesso a secrets via source control | [CRITICO] |
| Vercel preview deploys publicos | Acesso a versoes de staging com dados reais | [ALTO] |
| Ausencia de WAF | Ataques automatizados sem filtragem | [MEDIO] |
| DNS takeover em subdominios | Phishing usando dominio da agencia | [ALTO] |

---

## 2. CHECKLIST PRIORIZADA DE AUDITORIA

Organizada por severidade. Cada item sera verificado quando o codigo estiver disponivel.

### [CRITICO] — Bloqueia lancamento

- [ ] **AUTH-001** Autenticacao implementada com hashing seguro (bcrypt/argon2, nunca MD5/SHA1)
- [ ] **AUTH-002** Rate limiting em endpoint de login (max 5 tentativas/15min por IP+usuario)
- [ ] **AUTH-003** Tokens de sessao/JWT com expiracao curta (<= 15min access, <= 7d refresh)
- [ ] **AUTH-004** Password reset com tokens unicos, single-use, com expiracao (<= 30min)
- [ ] **AUTHZ-001** Toda operacao de leitura/escrita valida ownership (anti-IDOR)
- [ ] **AUTHZ-002** Endpoints de API exigem autenticacao — nenhum endpoint aberto sem intencao explicita
- [ ] **AUTHZ-003** Privilege escalation testada: usuario nao-admin nao acessa rotas de admin
- [ ] **DATA-001** HTTPS obrigatorio em todas as rotas (HSTS com max-age >= 31536000)
- [ ] **DATA-002** Nenhuma secret (API key, token, password) no repositorio (git history incluso)
- [ ] **INJ-001** Inputs sanitizados em todas as operacoes de banco (queries parametrizadas obrigatorias)
- [ ] **INJ-002** XSS prevenido: output encoding em todo dado renderizado no frontend
- [ ] **INT-001** Nenhuma API key ou token exposta no client-side JavaScript

### [ALTO] — Corrigir antes de produção

- [ ] **AUTH-005** MFA disponivel (pelo menos TOTP) para contas de admin
- [ ] **AUTH-006** Logout efetivo: invalida sessao no servidor, nao apenas client-side
- [ ] **AUTHZ-004** RBAC implementado: roles definidas (admin, operador, viewer)
- [ ] **DATA-003** PII criptografada em repouso (campo-level ou disk-level encryption)
- [ ] **DATA-004** Logs nao contem PII (email, telefone, dados de pagamento)
- [ ] **DATA-005** Export de dados requer autenticacao + audit trail
- [ ] **API-001** Rate limiting global em todas as APIs (padrao: 60 req/min por IP autenticado)
- [ ] **API-002** CORS restrito a origens conhecidas (dominio de producao apenas)
- [ ] **API-003** Validacao de content-type em todos os endpoints que aceitam body
- [ ] **API-004** Mass assignment prevenido: whitelist explicita de campos aceitos
- [ ] **HDR-001** Security headers aplicados (CSP, X-Frame-Options, XCTO, Referrer-Policy, Permissions-Policy, COOP)
- [ ] **INT-002** Webhooks recebidos validam assinatura (HMAC ou equivalente)
- [ ] **INT-003** OAuth flows usam state parameter + PKCE
- [ ] **ERR-001** Error responses nao expõem stack traces, SQL, ou detalhes internos
- [ ] **INF-001** Preview deploys protegidos por autenticacao ou IP whitelist
- [ ] **INF-002** DNS entries auditadas — nenhum subdomain dangling

### [MEDIO] — Corrigir no sprint seguinte

- [ ] **AUTH-007** Session fixation prevenida: novo session ID apos login
- [ ] **AUTH-008** Politica de senhas: minimo 12 chars, verificacao contra listas de senhas comprometidas (HaveIBeenPwned API)
- [ ] **DATA-006** Backups criptografados com chave separada do ambiente de producao
- [ ] **API-005** Paginacao obrigatoria em endpoints que retornam listas (max 100 items/page)
- [ ] **API-006** Campos sensiveis omitidos de respostas de listagem (ex: password hash nunca retorna)
- [ ] **LOG-001** Audit trail implementado: login, logout, CRUD em dados de clientes, alteracao de permissoes
- [ ] **LOG-002** Logs armazenados separadamente do banco principal (nao apagaveis pelo app)
- [ ] **DEP-001** npm audit / Snyk executado: zero vulnerabilidades CRITICAL/HIGH em dependencias
- [ ] **DEP-002** Lockfile (package-lock.json) commitado e respeitado no deploy
- [ ] **CORS-001** Preflight OPTIONS retorna 204 com headers corretos
- [ ] **BOT-001** Formularios publicos com honeypot pattern (replicar landing page)

### [BAIXO] — Backlog de melhoria continua

- [ ] **HDR-002** Subresource Integrity (SRI) em scripts e estilos externos
- [ ] **AUTH-009** Login throttling progressivo (delay exponencial apos falhas)
- [ ] **LOG-003** Alertas automaticos para padroes anomalos (multiplas falhas de login, export massivo)
- [ ] **API-007** Versionamento de API para evitar breaking changes em integracoes
- [ ] **DOC-001** Documentacao de seguranca: threat model, data flow diagram, politica de resposta a incidentes
- [ ] **SEC-001** Security.txt publicado em /.well-known/security.txt
- [ ] **SEC-002** Penetration test agendado para pos-lancamento (routing: @georgia-weidman)

---

## 3. PERGUNTAS PARA O DESENVOLVEDOR

Estas perguntas precisam ser respondidas antes de executar a auditoria completa. Sem isso, qualquer analise sera incompleta.

### Stack e Arquitetura

1. **Banco de dados:** Qual DB sera usado? (Supabase/PostgreSQL, MongoDB, outro?) — Impacta diretamente o tipo de injecao a testar e as politicas de RLS
2. **Autenticacao:** Sera propria (JWT, sessions) ou via provider (Supabase Auth, Auth0, Clerk)? — Define se vamos auditar implementacao ou configuracao
3. **Framework backend:** Express puro, Next.js API routes, Vercel Edge Functions, ou outro? — Cada um tem vetores diferentes
4. **Frontend:** SPA (React, Vue) ou server-rendered? Vanilla JS como a landing? — Afeta vetores de XSS e CSRF
5. **Hosting:** Vercel (como a landing), ou infra diferente? VPS proprio? — Define superficie de infraestrutura

### Dados e Compliance

6. **Quais dados de clientes serao armazenados?** (nome, email, telefone, CNPJ, dados financeiros, contratos?) — Define classificacao de dados e requisitos de criptografia
7. **Existem requisitos de LGPD?** (consentimento, direito a exclusao, portabilidade) — Pode exigir funcionalidades especificas
8. **Quem tera acesso ao CRM?** (apenas Miguel, time futuro, clientes?) — Define modelo de autorizacao necessario

### Integracoes

9. **Quais integracoes externas estao planejadas?** (Telegram, WhatsApp, email, Stripe, N8N, Make?) — Cada integracao e uma superficie de ataque adicional
10. **Webhooks serao recebidos de terceiros?** — Requer validacao de assinatura
11. **O CRM tera API publica ou apenas uso interno?** — API publica exige documentacao, rate limiting agressivo, e versionamento

### Deploy e Operacoes

12. **Ambientes separados (dev/staging/prod)?** — Dados de producao nunca devem existir em staging
13. **CI/CD pipeline planejado?** — Oportunidade de inserir security gates automaticos
14. **Monitoramento e logging ja planejados?** — Essencial para deteccao de incidentes

---

## 4. QUICK WINS IMEDIATOS

Padroes ja validados na audit da landing page que devem ser replicados no CRM desde o commit zero. Nao esperar a auditoria — implementar agora.

### 4.1 Replicar da Landing (validado em 2026-03-31)

| Padrao | Implementacao | Referencia |
|--------|--------------|------------|
| **Rate Limiting** | In-memory por IP, 5 req/60s, retorna 429 + Retry-After | `api/contact.js` L4-22 |
| **Sanitizacao de Input** | Funcao `sanitize()`: remove control chars, escapa `<>`, trunca por campo | `api/contact.js` L24-32 |
| **Honeypot Anti-bot** | Campo `website` CSS-hidden, descarte silencioso com HTTP 200 | `index.html` L2360-2365 |
| **Security Headers** | CSP, X-Frame-Options: DENY, XCTO: nosniff, Referrer-Policy, Permissions-Policy, COOP, HSTS | `vercel.json` headers config |
| **CORS Restrito** | Apenas origem de producao, preflight 204 | `api/contact.js` L38-50 |
| **Error Hardening** | Mensagens genericas, zero detalhes internos | `api/contact.js` L109-115 |
| **.gitignore Completo** | `.env`, `.env.local`, `.env.*` cobertos | `.gitignore` |
| **Zero Secrets Client-Side** | Nenhum token/key em codigo frontend | Verificado via grep |

### 4.2 Adicionais para CRM (nao existiam na landing pois era site estatico)

| Padrao | Implementacao | Prioridade |
|--------|--------------|------------|
| **CSRF Protection** | Token anti-CSRF em todo formulario que modifica estado | [CRITICO] |
| **Helmet.js** (se Express) | Middleware que configura todos os security headers automaticamente | [ALTO] |
| **bcrypt para passwords** | Custo >= 12 rounds, nunca armazenar texto claro | [CRITICO] |
| **Queries parametrizadas** | Nunca concatenar input em SQL/queries — usar prepared statements | [CRITICO] |
| **HttpOnly + Secure + SameSite cookies** | Sessoes inacessiveis via JavaScript, enviadas apenas em HTTPS | [CRITICO] |
| **Content-Type validation** | Rejeitar requests com content-type inesperado | [ALTO] |
| **Request body size limit** | Max 1MB para JSON, configuravel para uploads | [ALTO] |
| **Audit logging desde dia 1** | Log de login/logout/CRUD com timestamp + user ID + IP | [ALTO] |

---

## 5. ROUTING DE ESPECIALISTAS

Quando o codigo estiver disponivel, a auditoria completa sera executada com a seguinte distribuicao:

```
HANDOFF para @jim-manico

Contexto: CRM da agencia em desenvolvimento. Armazena dados de clientes (PII).
          Precisa de code audit completo focado em OWASP Top 10 + ASVS.
Urgencia: HIGH (quando codigo disponivel)
Assets: Dados de clientes, credenciais, pipeline de vendas
Acao: Executar audit-app-security.md completo com foco em autenticacao,
      autorizacao, injecao, e protecao de dados.
```

```
HANDOFF para @georgia-weidman

Contexto: CRM da agencia pos-deploy. Validar que as remediações do code audit
          realmente funcionam em ambiente real.
Urgencia: HIGH (pos-deploy em staging)
Assets: Superficie web exposta, endpoints de API
Acao: Pentest focado em autenticacao, IDOR, e endpoints de API.
      Validar rate limiting, CORS, e session management.
```

```
HANDOFF para @omar-santos

Contexto: CRM armazena dados de clientes brasileiros.
          LGPD pode ser aplicavel dependendo do volume e tipo de dados.
Urgencia: MEDIUM
Assets: Processos de coleta, armazenamento, e exclusao de dados
Acao: Avaliar requisitos de compliance LGPD e recomendar controles minimos.
```

---

## 6. TIMELINE DE EXECUCAO

| Fase | Gatilho | Responsavel | Entregavel |
|------|---------|-------------|------------|
| **Pre-dev** (AGORA) | Plano aprovado | Cyber Chief | Este documento |
| **Quick wins** | Primeiro commit do CRM | Desenvolvedor | Security headers, sanitizacao, .gitignore |
| **Threat model** | Arquitetura definida | @jim-manico | STRIDE analysis, data flow diagram |
| **Code audit** | MVP funcional | @jim-manico | Findings report com CVSS |
| **Pentest staging** | Deploy em staging | @georgia-weidman | Pentest report |
| **Compliance check** | Pre-lancamento | @omar-santos | LGPD compliance assessment |
| **Pentest producao** | 30 dias pos-lancamento | @georgia-weidman | Revalidacao |

---

## NOTAS

- Este plano assume stack alinhada com o padrao da agencia (Vanilla/Node/Vercel). Se o CRM usar stack diferente (ex: Next.js, Supabase), os vetores de ataque mudam e o plano sera atualizado.
- A auditoria da landing page (2026-03-31) encontrou 7 findings corrigidos e 1 risco aceito. O CRM, por lidar com autenticacao e dados de clientes, tera uma superficie de ataque significativamente maior.
- Nenhum item deste plano substitui um pentest real. O pentest sera agendado quando houver ambiente acessivel.

---

**Cyber Chief** — Zvision Cybersecurity Squad
**Classificacao:** CONFIDENCIAL — Uso interno Zvision Automations
