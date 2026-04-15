# Zvision-OS

**O sistema operacional para quem usa Claude Code a sério.**

Zvision-OS transforma o Claude Code em uma plataforma completa de automação com IA — 23 squads especializados, 400+ agentes prontos, roteamento inteligente e um segundo cérebro integrado.

Você foca no problema. O sistema roteia para o especialista certo automaticamente.

---

## O que é isso

Um framework de configuração para Claude Code que instala:

- **23 squads** de agentes especializados por domínio (dev, copy, design, segurança, growth, finanças...)
- **400+ agentes** com expertise profunda em cada área
- **Bridge de roteamento** que interpreta linguagem natural e delega para o squad correto
- **Sistema de skills** com workflows prontos (`/review`, `/ship`, `/qa`, `/investigate`...)
- **Vault Obsidian** estruturado como segundo cérebro conectado aos squads
- **Agente WhatsApp** com LLM via OpenRouter + Evolution API

---

## Por que usar

Claude Code sem estrutura é um generalista.
Com Zvision-OS, você tem uma equipe completa.

| Você pede... | O sistema faz... |
|-------------|-----------------|
| "criar proposta comercial" | Roteia para squad-commercial → cs-offer-designer |
| "revisar segurança do código" | Roteia para squad-cybersecurity → penetration-tester |
| "escrever copy para landing" | Roteia para squad-copy → copy-chief + direct-response-writer |
| "analisar métricas de growth" | Roteia para squad-growth → ga-data-analyst + ga-growth-hacker |

---

## Squads disponíveis

| Squad | Agentes | Domínio |
|-------|---------|---------|
| `squad-dev` | 7 | Código, arquitetura, QA, DevOps |
| `squad-copy` | 14 | Copywriting, headlines, conversão |
| `squad-design` | 15 | UI/UX, design systems, componentes |
| `squad-brand` | 15 | Marca, posicionamento, identidade |
| `squad-cybersecurity` | 9 | Segurança, pentest, compliance |
| `squad-growth` | 7 | SEO, analytics, growth hacking |
| `squad-paidmedia` | 10 | Meta Ads, Google Ads, CRO |
| `squad-commercial` | 11 | Vendas, propostas, CRM |
| `squad-content` | 7 | Conteúdo, blog, social media |
| `squad-research` | 8 | Pesquisa, benchmarks, inteligência |
| `squad-product` | 7 | Discovery, roadmap, MVP |
| `squad-storytelling` | 11 | Narrativa, pitch, apresentações |
| `squad-finance` | 5 | Financeiro, pricing, ROI |
| `squad-animations` | 9 | Three.js, shaders, motion web |
| `squad-council` | 11 | Conselho estratégico, decisões |
| `squad-claude` | 10 | Claude Code, MCP, automação |
| `squad-courses` | 8 | Cursos, módulos, treinamentos |
| `squad-cloning` | 9 | Digital twins, clonagem de persona |
| + 5 squads extras | — | Advisory, C-Level, Hormozi, Movement, SOP |

---

## Stack

- **Runtime:** Node.js + WSL2
- **Frontend:** Vanilla HTML/CSS/JS
- **Agente WA:** Evolution API + OpenRouter (Gemma, Llama, Mistral)
- **Segundo cérebro:** Obsidian + MCP local
- **Deploy:** Vercel (landing), Docker (Evolution API)

---

## Início rápido

### 1. Clone o repositório

```bash
git clone https://github.com/ZvisionAutomations/zvision-os.git
cd zvision-os
npm install
```

### 2. Configure o Claude Code

O arquivo `CLAUDE.md` na raiz é lido automaticamente pelo Claude Code.
Ajuste os caminhos dos projetos para sua máquina:

```markdown
## Projetos ativos
- zvision-landing: ~/projects/zvision-landing
- zvision-os: ~/projects/zvision-os
```

### 3. Configure as credenciais (MCP)

Copie o template e preencha com suas chaves:

```bash
cp .mcp.json.example .mcp.json
# edite .mcp.json com suas chaves de API
```

### 4. Suba o Bridge

```bash
./start.sh
# ou para WSL:
./start-zvision.sh
```

O Bridge sobe na porta `3333`. Teste:

```bash
curl http://localhost:3333/status
curl -X POST http://localhost:3333/task \
  -H 'Content-Type: application/json' \
  -d '{"task": "criar proposta comercial para cliente de tecnologia"}'
```

### 5. Use o orquestrador no Claude Code

```
/zvision criar copy para landing page de software B2B
```

O sistema identifica o domínio, roteia para o squad correto e executa.

---

## Estrutura do repositório

```
zvision-os/
├── .claude/
│   ├── commands/        Skills e agentes SINAPSE
│   ├── rules/           Regras de operação (NSN, YOLO, handoff...)
│   └── skills/          Skills do gstack e workflows
├── squads/              23 squads com agentes, tasks e KBs
├── bridge/              Servidor de roteamento (Node.js, porta 3333)
├── zvision-wa/          Agente WhatsApp (Evolution API + LLM)
├── dashboard/           Interface web (Phaser + Vite)
├── obsidian-vault/      Segundo cérebro estruturado
│   ├── _templates/      Templates reutilizáveis
│   ├── specs/           Especificações de features
│   ├── audits/          Auditorias técnicas
│   └── projetos/        Trabalho ativo
├── skills/              Skills instaláveis (Apify, etc.)
├── CLAUDE.md            Configuração central do Claude Code
└── start.sh             Script de inicialização
```

---

## Skills disponíveis

Comandos prontos para usar no Claude Code:

| Comando | O que faz |
|---------|-----------|
| `/zvision [pedido]` | Orquestra e roteia para o squad certo |
| `/review` | Code review focado em qualidade |
| `/qa` | QA automatizado de UI |
| `/ship` | Pipeline completo: review → qa → deploy |
| `/investigate` | Investigação de bugs |
| `/health` | Health check do projeto |
| `/browse` | Navegação e interação com browser |
| `/design-html` | Construção de UI em HTML/CSS/JS |
| `/vault-diario` | Captura rápida no segundo cérebro |
| `/vault-deal` | Registrar negócio no vault |
| `/client` | Carregar contexto completo de cliente |

---

## Agente WhatsApp

O `zvision-wa` é um agente de vendas e atendimento para WhatsApp:

- Conecta via Evolution API (self-hosted)
- LLM via OpenRouter (suporta Gemma, Llama, Mistral — gratuitos)
- Suporte a áudio (transcrição via Groq), imagem e texto
- Configurável com playbooks de vendas e SDR

```bash
cd zvision-wa
cp .env.example .env
# configure EVOLUTION_API_KEY e OPENROUTER_API_KEY
docker compose up -d
```

---

## Configuração MCP

Crie `.mcp.json` a partir do template:

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

O arquivo `.mcp.json` está no `.gitignore` — nunca commite suas chaves.

---

## Contribuindo

PRs são bem-vindos. Estrutura básica para novos squads e agents em `squads/`.

Siga o protocolo: `/pwf-brainstorm` antes de qualquer feature.

---

## Licença

MIT — use, modifique, distribua.

---

Feito por [Zvision Automations](https://github.com/ZvisionAutomations) · São Paulo, BR
