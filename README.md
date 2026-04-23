<![CDATA[<div align="center">

# Zvision-OS

**O sistema operacional para quem usa Claude Code a sério.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-orange)](https://claude.ai/code)
[![Squads](https://img.shields.io/badge/Squads-23-purple)]()
[![Agents](https://img.shields.io/badge/Agents-400%2B-green)]()

Zvision-OS transforma o Claude Code em uma plataforma completa de automação com IA — 23 squads especializados, 400+ agentes prontos, roteamento inteligente e um segundo cérebro integrado.

**Você foca no problema. O sistema roteia para o especialista certo automaticamente.**

</div>

---

## O problema que resolve

Claude Code sem estrutura é um generalista que sabe tudo superficialmente.

Com Zvision-OS, você tem uma equipe completa especializada por domínio. Cada squad tem agentes com expertise profunda, bases de conhecimento, workflows e tasks executáveis — prontos para usar agora.

```
/zvision criar proposta comercial para cliente de tecnologia
```

O sistema interpreta o domínio → roteia para o `squad-commercial` → aciona o `cs-offer-designer` → entrega uma proposta estruturada com pricing, objeções mapeadas e próximos passos.

---

## Demo rápido

```bash
# Clonar e configurar
git clone https://github.com/ZvisionAutomations/zvision-OS.git
cd zvision-OS
cp .mcp.json.example .mcp.json

# Invocar o orquestrador no Claude Code
/zvision revisar segurança do código antes do deploy
/zvision criar copy para landing page B2B
/zvision analisar concorrentes e mapear oportunidades de mercado
```

| Você pede... | O sistema faz... |
|-------------|-----------------|
| `"criar proposta comercial"` | squad-commercial → cs-offer-designer |
| `"revisar segurança do código"` | squad-cybersecurity → penetration-tester |
| `"escrever copy para landing"` | squad-copy → copy-chief + direct-response-writer |
| `"analisar métricas de growth"` | squad-growth → ga-data-analyst + ga-growth-hacker |
| `"criar animação Three.js"` | squad-animations → threejs-architect + shader-artist |

---

## O que está incluído

### 23 Squads Especializados

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

### Kits Verticais

Configurações pré-montadas por segmento de mercado — 5 plugins prontos para deploy com n8n + WhatsApp + IA:

| Kit | Segmento | ROI Estimado |
|-----|----------|-------------|
| `kits/clinicas` | Clínicas e consultórios | 2-4x em 30 dias |
| `kits/imobiliarias` | Imobiliárias e corretores | 3-5x em 60 dias |
| `kits/juridico` | Escritórios jurídicos | 3-6x em 90 dias |

Cada kit inclui: agendamento inteligente, follow-up automático, captação de leads, qualificação por IA e gestão pós-venda.

### Agente WhatsApp

`zvision-wa` é um agente de vendas e atendimento pronto para WhatsApp:

- Conecta via Evolution API (self-hosted)
- LLM via OpenRouter — suporta Gemma, Llama, Mistral (modelos gratuitos)
- Transcrição de áudio via Groq
- Playbooks de SDR e vendas configuráveis
- Memória cross-sessão por lead

### Skills Prontas

| Comando | O que faz |
|---------|-----------|
| `/zvision [pedido]` | Orquestra e roteia para o squad certo |
| `/review` | Code review focado em qualidade |
| `/qa` | QA automatizado de UI |
| `/ship` | Pipeline: review → qa → deploy |
| `/investigate` | Investigação de bugs |
| `/health` | Health check do projeto |
| `/browse` | Navegação com browser |
| `/design-html` | Construção de UI em HTML/CSS/JS |
| `/vault-diario` | Captura rápida no segundo cérebro |
| `/client` | Carregar contexto completo de cliente |

---

## Início rápido

### 1. Clone o repositório

```bash
git clone https://github.com/ZvisionAutomations/zvision-OS.git
cd zvision-OS
npm install
```

### 2. Configure o Claude Code

O arquivo `CLAUDE.md` na raiz é lido automaticamente pelo Claude Code.
Ajuste os caminhos para seus projetos:

```markdown
## Projetos ativos
- zvision-os: ~/projects/zvision-os (este repo)
- seu-projeto: ~/projects/meu-projeto (configure aqui)
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
# ou no WSL:
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

Abra o Claude Code na pasta do projeto e invoque:

```
/zvision criar copy para landing page de software B2B
```

---

## Estrutura do repositório

```
zvision-OS/
├── .claude/
│   ├── commands/        Skills e agentes SINAPSE (400+ agentes)
│   ├── rules/           Regras de operação (NSN, YOLO, handoff...)
│   ├── hooks/           Token Guardian e hooks de qualidade
│   └── skills/          Skills do gstack e workflows
├── squads/              23 squads com agentes, tasks, KBs e workflows
├── kits/                Kits verticais por segmento de mercado
│   ├── clinicas/        5 plugins para saúde
│   ├── imobiliarias/    5 plugins para imobiliárias
│   └── juridico/        5 plugins para escritórios jurídicos
├── bridge/              Servidor de roteamento (Node.js, porta 3333)
├── zvision-wa/          Agente WhatsApp (Evolution API + LLM)
├── dashboard/           Interface web
├── obsidian-vault/      Segundo cérebro estruturado
│   ├── _templates/      Templates reutilizáveis
│   ├── specs/           Especificações de features
│   └── audits/          Auditorias técnicas
├── scripts/             Utilitários e scripts de manutenção
├── CLAUDE.md            Configuração central — lida automaticamente pelo Claude Code
├── SECURITY.md          Política de segurança
├── CONTRIBUTING.md      Como contribuir
└── start.sh             Script de inicialização
```

---

## Agente WhatsApp — Setup

```bash
cd zvision-wa
cp .env.example .env
# configure EVOLUTION_API_KEY, OPENROUTER_API_KEY e EVOLUTION_INSTANCE_NAME
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

> O arquivo `.mcp.json` está no `.gitignore` — nunca commite suas chaves.

---

## Stack

- **Runtime:** Node.js + WSL2
- **Frontend:** Vanilla HTML/CSS/JS
- **Agente WA:** Evolution API + OpenRouter (Gemma, Llama, Mistral)
- **Segundo cérebro:** Obsidian + MCP local
- **Deploy:** Vercel (landing), Docker (Evolution API)

---

## Contribuindo

PRs e novos squads são bem-vindos. Leia o [CONTRIBUTING.md](CONTRIBUTING.md) para começar.

Siga o protocolo: `/pwf-brainstorm` antes de qualquer feature.

---

## Segurança

Para reportar vulnerabilidades, veja [SECURITY.md](SECURITY.md).

O repositório inclui um **Token Guardian Hook** que bloqueia automaticamente commits com secrets detectados.

---

## Licença

MIT — use, modifique, distribua.

---

<div align="center">

Feito por [Zvision Automations](https://github.com/ZvisionAutomations)

**Claude Code + 23 squads + 400+ agentes = equipe completa de IA**

</div>
]]>