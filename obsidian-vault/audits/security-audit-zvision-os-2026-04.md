# ZVISION OS -- SECURITY AUDIT REPORT

**Data:** 2026-04-03
**Target:** Zvision OS -- Segundo Cerebro da Agencia
**Repositorio:** `ZvisionAutomations/Zvision-OS` (GitHub)
**Stack:** Node.js, Playwright, Vite/React (dashboard), Obsidian Vault, Claude Agent Skills
**Auditor:** Cybersecurity Squad -- Cyber Chief
**Classificacao:** CONFIDENCIAL

---

## SUMARIO EXECUTIVO

Esta auditoria identificou **14 findings** no repositorio Zvision OS. Os problemas mais criticos envolvem **credenciais expostas no historico do Git que foram enviadas para o GitHub**, um `.gitignore` completamente inoperante devido a encoding incorreto, e chaves criptograficas privadas commitadas no repositorio.

O risco principal e **comprometimento imediato de contas GitHub e acesso nao autorizado ao vault Obsidian** caso o repositorio seja publico ou compartilhado.

---

## FINDINGS

---

### [F01] [CRITICO] GitHub Personal Access Tokens Expostos no Historico Git

**Risco:** Dois GitHub PATs (Personal Access Tokens) diferentes foram commitados ao repositorio e empurrados para o remote `origin` (GitHub). Qualquer pessoa com acesso ao repositorio (incluindo caso seja publico) pode extrair estes tokens e obter acesso total a conta GitHub do proprietario, incluindo:
- Leitura/escrita em todos os repositorios
- Criacao/exclusao de repositorios
- Acesso a configuracoes da organizacao
- Potencial lateral movement para outros servicos conectados via GitHub OAuth

**Evidencia:**

Token 1 (commit `63a6308`, arquivo `.mcp.json`):
```
ghp_[REDACTED — token revogado]
```

Token 2 (arquivo `.mcp.json` atual, working tree):
```
ghp_[REDACTED — token revogado]
```

Ambos os tokens existem no historico Git, que foi empurrado para:
```
origin: https://github.com/ZvisionAutomations/Zvision-OS.git
```

**Remediacao IMEDIATA (fazer AGORA):**
1. Revogar AMBOS os tokens imediatamente em https://github.com/settings/tokens
2. Gerar um novo token com escopos minimos necessarios
3. Verificar logs de acesso do GitHub para uso nao autorizado: https://github.com/settings/security-log
4. O token NÃO pode ser removido apenas com `git rm` -- ele permanece no historico. E necessario reescrever o historico com `git filter-repo` ou `BFG Repo Cleaner`, OU tornar o repositorio privado imediatamente

**Severidade:** CRITICO -- Acesso imediato possivel

---

### [F02] [CRITICO] Obsidian REST API Key Exposta no Historico Git

**Risco:** A API key do plugin Obsidian Local REST API esta commitada tanto no arquivo `.mcp.json` quanto no arquivo de configuracao do plugin `obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/data.json`. Esta chave permite acesso completo ao vault Obsidian via API REST (leitura, escrita, exclusao de notas).

**Evidencia:**

Arquivo: `.mcp.json` (linha 7) e `data.json` (linha 5):
```
200a98a2612e1a5cfbbffa206ff71158c9813de07006746a2b8aec61aba4589f
```

O plugin esta configurado com `"enableInsecureServer": true` (linha 4 de `data.json`), o que significa que aceita conexoes HTTP sem TLS na porta 27123, alem de HTTPS na porta 27124.

**Remediacao:**
1. Gerar nova API key no plugin Obsidian Local REST API
2. Desabilitar o servidor inseguro: setar `"enableInsecureServer": false`
3. Remover `data.json` do Git tracking: `git rm --cached obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/data.json`
4. Adicionar ao `.gitignore`: `obsidian-vault/.obsidian/plugins/*/data.json`

**Severidade:** CRITICO -- Acesso ao vault (dados da agencia)

---

### [F03] [CRITICO] Chave Privada RSA Commitada no Repositorio

**Risco:** O arquivo `obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/data.json` contem uma chave privada RSA completa (2048-bit) usada para TLS pelo plugin Obsidian REST API. Com esta chave, um atacante pode:
- Descriptografar trafego TLS capturado para o plugin
- Realizar ataques man-in-the-middle ao se passar pelo servidor
- Assinar dados como se fosse o servidor

**Evidencia:**

Arquivo: `obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/data.json` (linhas 8-9):
```
"privateKey": "-----BEGIN RSA PRIVATE KEY-----\r\nMIIEogIBAAKCAQEAt9Tv+H5hM5t9..."
```

O certificado, chave publica e chave privada estao todos commitados no mesmo arquivo.

**Remediacao:**
1. Regenerar o par de chaves do plugin (o plugin faz isso automaticamente ao remover o campo `crypto` do `data.json`)
2. Remover `data.json` do tracking do Git (coberto por F02)
3. Considerar que qualquer trafego TLS anterior pode ter sido interceptado se alguem teve acesso a esta chave

**Severidade:** CRITICO -- Compromete integridade TLS

---

### [F04] [CRITICO] .gitignore Completamente Inoperante (UTF-16 Encoding)

**Risco:** O arquivo `.gitignore` esta codificado em UTF-16 Little Endian (com BOM). O Git so reconhece `.gitignore` em UTF-8. Isso significa que **NENHUMA regra de ignore esta funcionando**. Todos os arquivos que deveriam ser ignorados (`.mcp.json`, `.env`, `node_modules/`, etc.) podem ser acidentalmente adicionados ao staging e commitados.

**Evidencia:**

```
$ file .gitignore
.gitignore: Unicode text, UTF-16, little-endian text, with CRLF line terminators

$ git check-ignore .mcp.json
(exit code 1 -- NAO IGNORADO)

$ git check-ignore .env
(exit code 1 -- NAO IGNORADO)

$ git check-ignore node_modules/
(exit code 1 -- NAO IGNORADO)
```

Conteudo pretendido do `.gitignore` (3 linhas, nenhuma sendo respeitada):
```
.claude/skills/gstack/bin/
.claude/skills/browse/dist/
.mcp.json
```

**Remediacao IMEDIATA:**
1. Recriar `.gitignore` em UTF-8 com todas as regras necessarias (ver recomendacao em F09)
2. Verificar se arquivos sensiveis foram commitados inadvertidamente
3. Executar `git rm --cached` nos arquivos que deveriam ter sido ignorados

**Severidade:** CRITICO -- Eliminacao completa da primeira linha de defesa contra commits de segredos

---

### [F05] [ALTO] node_modules/ Commitado no Repositorio (605 arquivos)

**Risco:** O diretorio `node_modules/` inteiro (605 arquivos do Playwright) esta commitado no repositorio e empurrado para o GitHub. Isso causa:
- Aumento massivo do tamanho do repositorio
- Possibilidade de supply chain attack se alguem modificar arquivos em node_modules/ diretamente
- Dificuldade em auditar dependencias (alteracoes em node_modules nao sao rastreadas como dependencias)
- Qualquer vulnerabilidade nas dependencias fica "congelada" no repositorio ate remocao manual

**Evidencia:**
```
$ git ls-files --cached | grep -c "node_modules/"
605
```

Inclui binarios do Playwright, shell scripts de instalacao, arquivos de configuracao.

**Remediacao:**
1. Corrigir `.gitignore` primeiro (F04)
2. Adicionar `node_modules/` ao `.gitignore`
3. Executar: `git rm -r --cached node_modules/`
4. Commit e push

**Severidade:** ALTO -- Supply chain risk + repo bloat

---

### [F06] [ALTO] Obsidian Plugin Files Commitados com Dados Sensiveis

**Risco:** O diretorio `.obsidian/` contem 10 arquivos commitados, incluindo o plugin `obsidian-local-rest-api` com seu `data.json` (que contem API key e chave privada RSA -- coberto em F02/F03). Alem disso, arquivos como `workspace.json` podem vazar informacoes sobre a estrutura de trabalho do usuario.

**Evidencia:**
```
$ git ls-files --cached | grep "\.obsidian/"
obsidian-vault/.obsidian/app.json
obsidian-vault/.obsidian/appearance.json
obsidian-vault/.obsidian/community-plugins.json
obsidian-vault/.obsidian/core-plugins.json
obsidian-vault/.obsidian/graph.json
obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/data.json    <-- CRITICO
obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/main.js      <-- 58,848 linhas
obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/manifest.json
obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/styles.css
obsidian-vault/.obsidian/workspace.json
```

**Remediacao:**
1. Adicionar ao `.gitignore`:
   ```
   obsidian-vault/.obsidian/workspace.json
   obsidian-vault/.obsidian/plugins/*/data.json
   ```
2. Avaliar se `main.js` (58K linhas) precisa estar no repo ou pode ser instalado via Obsidian
3. `git rm --cached` nos arquivos sensiveis

**Severidade:** ALTO -- Dados sensiveis em plugin config

---

### [F07] [ALTO] Servidor Obsidian REST API Inseguro Habilitado

**Risco:** O plugin Obsidian Local REST API esta configurado com `"enableInsecureServer": true`, o que habilita um servidor HTTP (sem TLS) na porta 27123. Qualquer processo local ou atacante com acesso a rede pode acessar o vault Obsidian inteiro sem criptografia de transporte.

**Evidencia:**

Arquivo: `obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/data.json` (linhas 3-4):
```json
"insecurePort": 27123,
"enableInsecureServer": true,
```

**Remediacao:**
1. Alterar `"enableInsecureServer"` para `false` no `data.json` do plugin
2. Garantir que apenas HTTPS (porta 27124) seja usado para acesso
3. Considerar firewall local para restringir acesso a porta 27124

**Severidade:** ALTO -- Acesso ao vault sem criptografia

---

### [F08] [ALTO] Dois Tokens GitHub Distintos Indicam Possivel Rotacao Sem Revogacao

**Risco:** O repositorio contem dois tokens GitHub PAT diferentes em commits distintos:
- Token 1 em commit `63a6308` (mais antigo)
- Token 2 no arquivo atual (mais recente)

Isso sugere que o Token 1 foi substituido pelo Token 2, mas o Token 1 provavelmente NAO foi revogado. Se o Token 1 ainda estiver ativo, e um vetor de acesso adicional.

**Evidencia:** Ver F01.

**Remediacao:**
1. Verificar status de ambos os tokens em https://github.com/settings/tokens
2. Revogar qualquer token que ainda esteja ativo
3. Implementar rotacao regular de tokens com revogacao do token antigo

**Severidade:** ALTO -- Multiplos vetores de acesso potencialmente ativos

---

### [F09] [ALTO] .gitignore Incompleto (Faltam Regras Essenciais)

**Risco:** Mesmo que o encoding seja corrigido (F04), o `.gitignore` atual so contem 3 regras. Faltam regras criticas para:
- `.env` e variacoes (`.env.local`, `.env.*`)
- `node_modules/`
- Configuracoes do Obsidian com dados sensiveis
- Arquivos de sistema operacional (`.DS_Store`, `Thumbs.db`)
- Logs e arquivos temporarios
- Diretorio de build do dashboard

**Remediacao:**

O `.gitignore` deve ser recriado em UTF-8 com no minimo:
```
# Dependencies
node_modules/

# Environment variables
.env
.env.*
.env.local

# MCP config with secrets
.mcp.json

# Obsidian sensitive files
obsidian-vault/.obsidian/workspace.json
obsidian-vault/.obsidian/plugins/*/data.json

# Build outputs
.claude/skills/gstack/bin/
.claude/skills/browse/dist/
dashboard/dist/

# OS files
.DS_Store
Thumbs.db
desktop.ini

# Logs
*.log

# IDE
.idea/
.vscode/
*.swp
*.swo

# Browser profiles
_opensquad/_browser_profile/
```

**Severidade:** ALTO -- Falha sistemica de controle de segredos

---

### [F10] [MEDIO] Dashboard WebSocket Sem Autenticacao

**Risco:** O endpoint WebSocket `/__squads_ws` no dashboard (Vite dev server) nao implementa nenhuma forma de autenticacao ou autorizacao. Qualquer cliente que possa alcancar o servidor pode:
- Receber snapshots do estado de todos os squads
- Receber updates em tempo real das operacoes
- Potencialmente injetar dados maliciosos se houver handlers de mensagens bidirecionais

**Evidencia:**

Arquivo: `dashboard/src/plugin/squadWatcher.ts` (linhas 141-158):
```typescript
(server.httpServer as Server).on("upgrade", (req, socket, head) => {
    if (req.url === "/__squads_ws") {
        wss.handleUpgrade(req, socket, head, (ws) => {
            wss.emit("connection", ws, req);
        });
    }
});

wss.on("connection", async (ws) => {
    // No authentication check
    const snap = await buildSnapshot(squadsDir);
    ws.send(JSON.stringify(snap));
});
```

O endpoint REST `/api/snapshot` (linha 166) tambem nao tem autenticacao.

**Atenuante:** O dashboard e um servidor de desenvolvimento local (Vite dev), nao exposto em producao. O risco e relevante apenas em redes nao confiadas.

**Remediacao:**
1. Adicionar token de autenticacao ao WebSocket handshake
2. Validar origem das conexoes
3. Se exposto em rede, adicionar header de autorizacao ao endpoint REST

**Severidade:** MEDIO -- Risco em redes compartilhadas

---

### [F11] [MEDIO] Dependencias do Dashboard com CVEs Conhecidas

**Risco:** O `npm audit` do dashboard identificou 2 vulnerabilidades em dependencias:

| Pacote | Severidade | CVE | Descricao |
|--------|-----------|-----|-----------|
| `picomatch` 4.0.0-4.0.3 | HIGH | GHSA-c2c7-rcm5-vvqj | ReDoS via extglob quantifiers |
| `yaml` 2.0.0-2.8.2 | MODERATE | GHSA-48c2-rrv3-qjmp | Stack Overflow via deeply nested YAML |

A vulnerabilidade do `yaml` e particularmente relevante porque o `squadWatcher.ts` usa a biblioteca `yaml` para parsear arquivos `squad.yaml` do filesystem (linha 9, 40).

**Evidencia:**
```
$ cd dashboard && npm audit
2 vulnerabilities (1 moderate, 1 high)
```

**Remediacao:**
1. Executar `cd dashboard && npm audit fix`
2. Verificar compatibilidade apos update
3. Adicionar `npm audit` como step de CI/CD

**Severidade:** MEDIO -- Vulnerabilidades exploraveis em dependencias

---

### [F12] [MEDIO] Dados de Negocio em Repositorio Git Publico (Potencial)

**Risco:** O repositorio contem informacoes de negocio da agencia commitadas e empurradas para o GitHub:
- SOPs operacionais completos (`obsidian-vault/operacoes/`)
- Perfil completo da empresa (`_opensquad/_memory/company.md`)
- URLs de producao (landing, CRM)
- Stack tecnologico detalhado
- Processos de onboarding de clientes
- Definicoes de agentes e workflows internos (416 arquivos em `squads/`)
- Audit reports com findings de seguranca anteriores

Se o repositorio for publico, toda esta informacao e acessivel a concorrentes e atacantes.

**Evidencia:**
- `_opensquad/_memory/company.md` -- Perfil completo: nome, fundador, URLs, stack, modelo de negocio
- `obsidian-vault/operacoes/sop-onboarding-cliente.md` -- Processo interno de onboarding
- `obsidian-vault/audits/security-audit-landing-2026-03.md` -- Findings de seguranca corrigidos

**Remediacao:**
1. Se o repositorio for publico: tornar PRIVADO imediatamente
2. Avaliar se dados operacionais devem estar no mesmo repositorio que o codigo
3. Considerar separar vault/operacoes em repositorio independente e privado

**Severidade:** MEDIO -- Exposicao de inteligencia de negocio

---

### [F13] [BAIXO] Obsidian Plugin main.js Commitado (58K linhas)

**Risco:** O arquivo `main.js` do plugin Obsidian Local REST API tem 58,848 linhas e esta commitado no repositorio. Isso aumenta o tamanho do repo desnecessariamente e dificulta code review (mudancas nesse arquivo seriam dificeis de auditar). O plugin deveria ser instalado via Obsidian Community Plugins, nao versionado manualmente.

**Evidencia:**
```
$ wc -l obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/main.js
58848
```

**Remediacao:**
1. Adicionar `obsidian-vault/.obsidian/plugins/*/main.js` ao `.gitignore`
2. `git rm --cached obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/main.js`
3. Documentar plugins necessarios em um README para reinstalacao manual

**Severidade:** BAIXO -- Bloat + auditabilidade

---

### [F14] [INFO] Informacoes de Negocio em Logs Commitados

**Risco:** O arquivo `_opensquad/logs/cli.log` esta commitado e contem timestamps de operacoes. Embora nao contenha dados sensiveis atualmente, logs commitados podem acumular informacoes uteis para atacantes ao longo do tempo.

**Evidencia:**

Arquivo: `_opensquad/logs/cli.log`:
```json
{"timestamp":"2026-04-01T14:28:03.836Z","action":"init","details":{"language":"Portugues (Brasil)","ides":"antigravity"}}
```

**Remediacao:**
1. Adicionar `_opensquad/logs/` ao `.gitignore`
2. `git rm --cached _opensquad/logs/cli.log`

**Severidade:** INFO -- Informacao operacional em logs

---

## RESUMO EXECUTIVO

| Severidade | Total | Descricao |
|------------|-------|-----------|
| CRITICO    | 4     | Tokens GitHub expostos, API key + RSA key commitados, .gitignore inoperante |
| ALTO       | 5     | node_modules commitado, plugin data exposto, servidor inseguro, .gitignore incompleto, tokens nao revogados |
| MEDIO      | 3     | WebSocket sem auth, CVEs em deps, dados de negocio expostos |
| BAIXO      | 1     | Plugin JS commitado desnecessariamente |
| INFO       | 1     | Logs operacionais commitados |
| **TOTAL**  | **14** | |

---

## PLANO DE REMEDIACAO PRIORITIZADO

### Fase 1: IMEDIATO (fazer AGORA -- hoje)

| # | Acao | Finding | Tempo |
|---|------|---------|-------|
| 1 | Revogar AMBOS os GitHub tokens | F01, F08 | 2 min |
| 2 | Verificar security log do GitHub para uso nao autorizado | F01 | 5 min |
| 3 | Tornar o repositorio PRIVADO (se publico) | F01, F12 | 1 min |
| 4 | Regenerar API key do Obsidian REST API | F02 | 2 min |

### Fase 2: URGENTE (fazer HOJE)

| # | Acao | Finding | Tempo |
|---|------|---------|-------|
| 5 | Recriar `.gitignore` em UTF-8 com regras completas | F04, F09 | 10 min |
| 6 | `git rm --cached` em: node_modules/, .obsidian/plugins/*/data.json, .obsidian/plugins/*/main.js, _opensquad/logs/ | F05, F06, F13, F14 | 5 min |
| 7 | Desabilitar servidor HTTP inseguro do Obsidian plugin | F07 | 2 min |
| 8 | `cd dashboard && npm audit fix` | F11 | 2 min |

### Fase 3: LIMPEZA DE HISTORICO (esta semana)

| # | Acao | Finding | Tempo |
|---|------|---------|-------|
| 9 | Usar `git filter-repo` ou `BFG Repo Cleaner` para remover tokens e chaves do historico | F01, F02, F03 | 30 min |
| 10 | Force push do historico limpo | F01, F02, F03 | 5 min |
| 11 | Notificar qualquer colaborador para re-clonar o repositorio | F01 | 5 min |

### Fase 4: HARDENING (proxima semana)

| # | Acao | Finding | Tempo |
|---|------|---------|-------|
| 12 | Adicionar pre-commit hook para detectar secrets (ex: `git-secrets`, `detect-secrets`, `gitleaks`) | Todos | 30 min |
| 13 | Implementar autenticacao no WebSocket do dashboard | F10 | 2h |
| 14 | Configurar GitHub secret scanning alerts | F01 | 10 min |
| 15 | Mover .mcp.json para fora do repositorio (ex: `~/.config/zvision/mcp.json`) | F01, F02 | 15 min |

---

## PONTOS POSITIVOS

1. **npm audit limpo** no root package.json (0 vulnerabilidades)
2. **Nenhum PII real** (CPF, email, telefone de clientes) no vault -- apenas templates e SOPs
3. **Dashboard sem XSS vectors** -- nenhum uso de innerHTML, dangerouslySetInnerHTML, ou document.write
4. **Dashboard sem code injection** -- nenhum uso de eval(), Function(), ou child_process
5. **Audit anterior da landing page** (2026-03-31) bem executada com 7 findings corrigidos
6. **Plano de seguranca do CRM** ja documentado com checklist priorizada (F-series)
7. **.env.example** com placeholders, nao com valores reais
8. **.npmrc com ignore-scripts=true** -- previne execucao automatica de post-install scripts (supply chain defense)

---

## NOTAS TECNICAS

1. **Sobre a limpeza de historico Git:** O `git filter-repo` e preferivel ao `BFG Repo Cleaner` por ser mantido ativamente e mais preciso. Comando exemplo:
   ```bash
   git filter-repo --path .mcp.json --invert-paths
   git filter-repo --path obsidian-vault/.obsidian/plugins/obsidian-local-rest-api/data.json --invert-paths
   ```
   **ATENCAO:** Isso reescreve TODO o historico. Colaboradores precisarao re-clonar.

2. **Sobre o .gitignore UTF-16:** Isso provavelmente aconteceu porque o arquivo foi criado ou editado por uma ferramenta Windows que usa UTF-16 como encoding padrao (ex: PowerShell `Set-Content`, Notepad em versoes antigas). Recriar em UTF-8 sem BOM.

3. **Sobre os tokens no Git history:** Mesmo apos `git rm --cached .mcp.json`, os tokens permanecem acessiveis via `git show <commit>:.mcp.json`. A unica solucao definitiva e reescrever o historico OU revogar os tokens (que e o mais importante).

---

**Cyber Chief** -- Zvision Cybersecurity Squad
**Proxima revisao:** Apos execucao da Fase 2 de remediacao
