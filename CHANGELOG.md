# Changelog

Todas as mudanças notáveis neste projeto são documentadas aqui.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [1.1.0] — 2026-04-22

### Adicionado
- **Kits Verticais** — 3 kits pré-configurados por segmento (clínicas, imobiliárias, jurídico), cada um com 5 plugins prontos para deploy
- **SECURITY.md** — política de segurança e canal de disclosure responsável
- **CONTRIBUTING.md** — guia completo para contribuições
- **Templates GitHub** — issue templates e PR template para padronizar contribuições
- **Token Guardian Hook** — bloqueia automaticamente commits com secrets hardcoded

### Alterado
- CLAUDE.md: removidas referências a projetos privados, tornando o template genérico e reutilizável
- README.md: seção de setup simplificada e mais clara
- `squads/squad-claude/agents/`: paths de dependências atualizados para estrutura do Zvision-OS

### Segurança
- Removidas todas as referências a projetos e repositórios privados dos arquivos rastreados
- `.mcp.json` confirmado no `.gitignore` — nunca exposto no repositório

---

## [1.0.0] — 2026-04-15

### Adicionado
- **Release inicial open source** — repositório público com histórico limpo
- 23 squads especializados com 400+ agentes prontos
- Bridge de roteamento (`/zvision`) com interpretação de linguagem natural
- Sistema de skills com `/review`, `/ship`, `/qa`, `/investigate` e mais 20+ comandos
- Vault Obsidian estruturado como segundo cérebro conectado aos squads
- Agente WhatsApp (`zvision-wa`) com Evolution API + OpenRouter
- Dashboard web (Phaser + Vite)
- Hooks de qualidade: Token Guardian, pre-commit verification
- NSN Mode e YOLO Mode para execução autônoma de agentes
- `.mcp.json.example` como template seguro de configuração

### Squads incluídos
`squad-dev`, `squad-copy`, `squad-design`, `squad-brand`, `squad-cybersecurity`,
`squad-growth`, `squad-paidmedia`, `squad-commercial`, `squad-content`,
`squad-research`, `squad-product`, `squad-storytelling`, `squad-finance`,
`squad-animations`, `squad-council`, `squad-claude`, `squad-courses`,
`squad-cloning`, `advisory-board`, `c-level-squad`, `hormozi-squad`,
`movement`, `sop-factory`
