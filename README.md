<div align="center">

# Zvision-OS

**Você já tem o Claude Code. Agora dê uma equipe inteira pra ele.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-orange)](https://claude.ai/code)
[![Version](https://img.shields.io/badge/Version-2.0.0-blue)]()
[![Squads](https://img.shields.io/badge/Squads-23-purple)]()
[![Agents](https://img.shields.io/badge/Agents-300%2B-green)]()
[![Tasks](https://img.shields.io/badge/Tasks-1.400%2B-red)]()

Zvision-OS é um sistema operacional para Claude Code — 23 squads especializados, 300+ agentes e 1.400+ tasks executáveis prontas para uso.

**Você descreve o que precisa. O sistema aciona o especialista certo.**

</div>

---

## Instalação

```bash
npx github:ZvisionAutomations/zvision-OS
```

Uma linha. O instalador detecta o ambiente, copia o framework e configura tudo automaticamente.

Ou, se preferir clonar manualmente:

```bash
git clone https://github.com/ZvisionAutomations/zvision-OS.git
cd zvision-OS && npm install
```

---

## Claude Code sozinho faz tudo. O problema é que faz tudo superficialmente.

Sem estrutura, o Claude Code é um generalista: sabe de copy, segurança, produto, growth — mas sem profundidade em nenhum.

Zvision-OS resolve isso com squads especializados. Cada domínio tem agentes com expertise profunda, bases de conhecimento próprias, workflows e tasks executáveis. Copy vai para o `squad-copy`. Segurança vai para o `squad-cybersecurity`. Estratégia vai para o `squad-council`.

O orquestrador central identifica o domínio e roteia automaticamente.

```
/zvision criar proposta comercial para cliente de tecnologia
```

O sistema interpreta o domínio → aciona o `squad-commercial` → o `cs-offer-designer` entrega uma proposta com pricing estruturado, objeções mapeadas e próximos passos.

---

## Para quem é feito

- **Desenvolvedores** que usam Claude Code no dia a dia e querem resultados mais precisos por domínio
- **Fundadores e consultores** que precisam de IA especializada sem montar um time do zero
- **Agências** que querem escalar entrega com squads de IA por área (copy, design, growth, segurança)
- **Entusiastas de Claude Code** que querem explorar o que a plataforma consegue fazer com estrutura real

---

## Veja como funciona

```bash
# Após instalar, abra o Claude Code na pasta e invoque:
/zvision revisar segurança do código antes do deploy
/zvision criar copy para landing page B2B
/zvision analisar concorrentes e mapear gaps de mercado
/zvision criar animação Three.js para hero da landing
```

| Você pede... | O sistema faz... |
|-------------|-----------------|
| `"criar proposta comercial"` | squad-commercial → cs-offer-designer |
| `"revisar segurança do código"` | squad-cybersecurity → penetration-tester |
| `"escrever copy para landing"` | squad-copy → copy-chief + direct-response-writer |
| `"analisar métricas de growth"` | squad-growth → ga-data-analyst + ga-growth-hacker |
| `"criar animação Three.js"` | squad-animations → threejs-architect + shader-artist |

---

## O que vem dentro

### 23 Squads Especializados

Cada squad tem agentes, bases de conhecimento, tasks e workflows próprios — prontos para uso imediato.

| Squad | Agentes | Tasks | Domínio |
|-------|---------|-------|---------|
| `squad-dev` | 7 | 5 | Código, arquitetura, QA, DevOps |
| `squad-copy` | 14 | 81 | Copywriting, headlines, conversão |
| `squad-design` | 15 | 101 | UI/UX, design systems, componentes |
| `squad-brand` | 15 | 97 | Marca, posicionamento, identidade |
| `squad-cybersecurity` | 9 | 53 | Segurança, pentest, compliance |
| `squad-growth` | 7 | 77 | SEO, analytics, growth hacking |
| `squad-paidmedia` | 10 | 82 | Meta Ads, Google Ads, CRO |
| `squad-commercial` | 11 | 85 | Vendas, propostas, CRM |
| `squad-content` | 7 | 90 | Conteúdo, blog, social media |
| `squad-research` | 8 | 72 | Pesquisa, benchmarks, inteligência competitiva |
| `squad-product` | 7 | 75 | Discovery, roadmap, MVP |
| `squad-storytelling` | 11 | 47 | Narrativa, pitch, apresentações |
| `squad-finance` | 5 | 45 | Financeiro, pricing, ROI |
| `squad-animations` | 9 | 73 | Three.js, shaders, motion web |
| `squad-council` | 11 | 56 | Conselho estratégico, decisões |
| `squad-claude` | 10 | 49 | Claude Code mastery, MCP, automação |
| `squad-courses` | 8 | 59 | Cursos, módulos, treinamentos |
| `squad-cloning` | 9 | 54 | Digital twins, clonagem de persona |
| + 5 squads extras | — | — | Advisory Board, C-Level, Hormozi, Movement, SOP Factory |

### Governança Constitucional

Zvision-OS opera sob uma [Constituição formal](CONSTITUTION.md) com 10 artigos aplicados automaticamente por 3 hooks de enforcement em runtime:

| Hook | O que protege |
|------|--------------|
| `token-guardian.js` | Bloqueia commits com secrets detectados |
| `enforce-git-push.js` | Garante que push só ocorre por agentes autorizados |
| `enforce-story-gate.js` | Impede implementação sem story validada |

Violações são bloqueadas em runtime, não detectadas depois.

### Kits Verticais — automação pronta por segmento

Cada kit vem com 5 plugins configurados para deploy imediato via n8n + WhatsApp + IA:

| Kit | Segmento | Inclui |
|-----|----------|--------|
| `kits/clinicas` | Clínicas e consultórios | Agendamento, follow-up, captação, qualificação, pós-venda |
| `kits/imobiliarias` | Imobiliárias e corretores | Captação automatizada, qualificação por IA, gestão de leads |
| `kits/juridico` | Escritórios jurídicos | Triagem por IA, agendamento inteligente, follow-up automatizado |

### Agente WhatsApp (`zvision-wa`)

Agente de vendas completo pronto para WhatsApp. Conecta via Evolution API self-hosted, usa LLMs gratuitos via OpenRouter e mantém memória por lead entre sessões.

- **Vitor (BDR)** — prospecção outbound com hook de curiosidade
- **Ana (SDR)** — qualificação e agendamento direto no WhatsApp
- Transcrição de áudio via Groq
- Lembretes automáticos 24h e 1h antes da reunião
- Skills configuráveis por persona e estágio do funil

### Skills de Produtividade

| Comando | O que faz |
|---------|-----------|
| `/zvision [pedido]` | Roteia para o squad especializado automaticamente |
| `/review` | Code review focado em qualidade |
| `/ship` | Pipeline completo: review → qa → deploy |
| `/investigate` | Investigação profunda de bugs |
| `/health` | Health check do projeto |
| `/browse` | Navegação e testes com browser |
| `/design-html` | Construção de UI em HTML/CSS/JS |
| `/vault-diario` | Captura rápida no segundo cérebro |
| `/client` | Carrega contexto completo de cliente |

---

## Configuração

### 1. CLAUDE.md

O `CLAUDE.md` na raiz é lido automaticamente pelo Claude Code. Ajuste os caminhos para seus projetos ativos:

```markdown
## Projetos ativos
- zvision-os: ~/projects/zvision-os
- seu-projeto: ~/projects/meu-projeto
```

### 2. Credenciais (opcional)

Para ativar MCPs como Obsidian e GitHub:

```bash
cp .mcp.json.example .mcp.json
# edite .mcp.json com suas chaves de API
```

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "sua-chave-aqui",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "27124"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_seu-token-aqui"
      }
    }
  }
}
```

> `.mcp.json` está no `.gitignore` — suas credenciais nunca vão para o repositório.

### 3. Bridge de Roteamento

```bash
./start.sh
```

Bridge disponível em `http://localhost:3333`:

```bash
curl http://localhost:3333/status

curl -X POST http://localhost:3333/task \
  -H 'Content-Type: application/json' \
  -d '{"task": "criar proposta comercial para cliente de tecnologia"}'
```

### 4. Agente WhatsApp (opcional)

```bash
cd zvision-wa
cp .env.example .env
# configure: EVOLUTION_API_KEY, OPENROUTER_API_KEY, EVOLUTION_INSTANCE_NAME, CLOSER_PHONE
docker compose up -d
```

---

## Estrutura do repositório

```
zvision-OS/
├── .claude/
│   ├── commands/        Squads SINAPSE (300+ agentes via comandos)
│   ├── rules/           Regras constitucionais de operação
│   ├── hooks/           Token Guardian + enforcement hooks
│   └── skills/          Skills do gstack e workflows
├── squads/              23 squads com agentes, tasks, KBs e workflows
├── kits/                Kits verticais prontos por segmento
│   ├── clinicas/
│   ├── imobiliarias/
│   └── juridico/
├── bridge/              Servidor de roteamento inteligente (porta 3333)
├── bin/
│   └── install.js       Instalador CLI (npx)
├── zvision-wa/          Agente WhatsApp (Evolution API + LLM)
├── obsidian-vault/      Segundo cérebro estruturado
├── CLAUDE.md            Configuração central — lida automaticamente pelo Claude Code
├── CONSTITUTION.md      Governança formal do framework (10 artigos)
├── SECURITY.md          Política de disclosure responsável
├── CONTRIBUTING.md      Como contribuir
└── start.sh             Script de inicialização do Bridge
```

---

## Stack

| Camada | Tecnologia |
|--------|------------|
| Runtime | Node.js ≥ 18 |
| Frontend | Vanilla HTML/CSS/JS |
| WhatsApp | Evolution API + OpenRouter (Gemma, Llama, Mistral) |
| Segundo cérebro | Obsidian + MCP local |
| Deploy | Vercel (landing), Docker (Evolution API) |

---

## Segurança

Para reportar vulnerabilidades, consulte [SECURITY.md](SECURITY.md).

O Token Guardian Hook bloqueia automaticamente commits com secrets detectados. Ver [CONSTITUTION.md — Artigo VIII](CONSTITUTION.md) para detalhes.

---

## Contribuindo

PRs e novos squads são bem-vindos. Leia o [CONTRIBUTING.md](CONTRIBUTING.md).

Protocolo obrigatório antes de qualquer feature: `/pwf-brainstorm` → spec em `obsidian-vault/specs/` → implementação.

---

## Licença

MIT — use, modifique, distribua.

---

<div align="center">

Feito por [Zvision Automations](https://github.com/ZvisionAutomations)

**23 squads · 300+ agentes · 1.400+ tasks executáveis**

[Começar agora →](https://github.com/ZvisionAutomations/zvision-OS)

</div>
