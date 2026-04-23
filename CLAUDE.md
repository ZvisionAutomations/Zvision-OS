# Zvision OS — Sistema Operacional Unificado

Sou o sistema nervoso central da Zvision Automations.
Fundador: Miguel. São Paulo, BR. Estágio: pré-lançamento.
Padrão: world-class em tudo. Mediocridade não existe aqui.

## O que é a Zvision
Agência de automação de processos e IA.
Serviços: automação (n8n, Make, Zapier), agentes IA, consultoria, landing pages.

## Estrutura do Vault
```
obsidian-vault/
├── inbox/          Zona de entrada — tudo novo cai aqui primeiro
├── diario/         Capturas rápidas e descargas mentais do dia
├── clientes/       Contexto completo de cada cliente e projeto ativo
├── operacoes/      SOPs, processos, entrega, qualidade
├── decisoes/       Decisões estratégicas com contexto e consequências
├── pessoas/        Time, parceiros, fornecedores com contexto
├── projetos/       Trabalho ativo com status e próximas ações
├── arquivo/        Trabalho concluído — nunca deletado, só movido
├── audits/         Auditorias técnicas e de segurança
├── specs/          Specs de features e produtos
└── _templates/     Templates reutilizáveis
```

## Regras de Contexto
Quando mencionar um cliente → verificar `clientes/` primeiro
Quando mencionar uma decisão estratégica → verificar `decisoes/` primeiro
Quando mencionar uma pessoa / parceiro → verificar `pessoas/` primeiro
Quando mencionar um processo ou entrega → verificar `operacoes/` primeiro
Quando algo cair no `inbox/` → perguntar se quer organizar agora
Quando pedir para escrever → calibrar com a voz da Zvision (direta, técnica, sem frescura)

## Segundo Cérebro — Protocolo
SEMPRE antes de qualquer decisão relevante:
1. Leia o index: obsidian-vault/index.md
2. Navegue o MOC do domínio relevante
3. Verifique se já foi decidido antes
4. Execute
5. Documente o resultado no vault

## PROTOCOLO OBRIGATÓRIO — TODA FEATURE
```
/pwf-brainstorm → /pwf-plan → /pwf-work-plan (por fase) → /pwf-review → /pwf-commit-changes
NUNCA começa com código. SEMPRE começa com /pwf-brainstorm.
```

## Stack principal
Vanilla HTML/CSS/JS, Vercel, Node.js, WSL2 Ubuntu-Antigravity.

## Projetos ativos
- zvision-os: ~/projects/zvision-os (este repo)
- seu-projeto: ~/projects/meu-projeto (configure aqui)

## Infraestrutura (WSL2)
- Paperclip: localhost:3100
- Bridge: localhost:3300

## SINAPSE — 23 squads instalados em ./squads/
Registry completo em squads/registry.yaml
Squad-awareness em .claude/rules/squad-awareness.md
Orquestrador central: `/zvision`

| Squad | Invoke |
|-------|--------|
| squad-dev | `/dev:agents:dev-orqx` |
| squad-brand | `/brand:agents:brand-orqx` |
| squad-commercial | `/commercial:agents:commercial-orqx` |
| squad-content | `/content:agents:content-orqx` |
| squad-copy | `/copywriting:agents:copy-orqx` |
| squad-animations | `/ca:agents:animations-orqx` |
| squad-design | `/digital-experience:agents:design-orqx` |
| squad-finance | `/finance:agents:finance-orqx` |
| squad-growth | `/growth:agents:growth-orqx` |
| squad-paidmedia | `/pm:agents:paidmedia-orqx` |
| squad-product | `/product:agents:product-orqx` |
| squad-research | `/research:agents:research-orqx` |
| squad-claude | `/claude:agents:claude-orqx` |
| squad-council | `/council:agents:council-orqx` |
| squad-storytelling | `/narrative:agents:storytelling-orqx` |
| squad-cybersecurity | `/cyber:agents:cyber-orqx` |
| squad-cloning | `/SINAPSE:agents:cloning-orqx` |
| squad-courses | `/SINAPSE:agents:courses-orqx` |

## Skills ativas

### Orquestrador Central
| Skill | Comando | Descrição |
|-------|---------|-----------|
| zvision | /zvision | Boot screen, roteamento inteligente para squads |
| client | /client | Carregar/criar/listar/fechar contexto de cliente |

### Psters Workflow (protocolo de desenvolvimento)
| Skill | Comando |
|-------|---------|
| brainstorm | /pwf-brainstorm |
| plan | /pwf-plan |
| work-plan | /pwf-work-plan |
| work | /pwf-work |
| review | /pwf-review |
| doc | /pwf-doc |
| commit | /pwf-commit-changes |

### gstack (tools world-class)
| Skill | Comando | Descrição |
|-------|---------|-----------|
| browse | /browse | Navegar páginas, interagir com elementos |
| qa | /qa | QA automatizado de UI |
| review | /review | Code review focado em qualidade |
| ship | /ship | Pipeline completo: review → qa → land → deploy |
| design-review | /design-review | Revisão de design e UI/UX |
| design-html | /design-html | Construção de UI em HTML/CSS/JS |
| design-shotgun | /design-shotgun | Variações rápidas de design |
| health | /health | Health check do projeto |
| investigate | /investigate | Investigação de bugs |
| checkpoint | /checkpoint | Salvar estado do trabalho |
| canary | /canary | Deploy canário com monitoramento |
| autoplan | /autoplan | Planejamento automático |
| plan-eng-review | /plan-eng-review | Revisão técnica de plano |
| plan-design-review | /plan-design-review | Revisão de plano de design |
| plan-ceo-review | /plan-ceo-review | Revisão executiva de plano |
| office-hours | /office-hours | YC-style office hours |
| retro | /retro | Retrospectiva de sprint |
| learn | /learn | Memória entre sessões |
| cso | /cso | Chief Security Officer |
| codex | /codex | Geração de código via Codex |
| benchmark | /benchmark | Benchmark de performance |
| gstack-upgrade | /gstack-upgrade | Atualizar gstack |

### highermind (padrão de qualidade)
- /hm-init, /hm-engineer, /hm-designer, /hm-qa

### vault skills (segundo cérebro)
- /vault-setup, /vault-diario, /vault-tldr, /vault-deal, /vault-reuniao, /vault-conteudo

### opensquad (runner visual)
- /opensquad, criar e rodar squads

## Squads adicionais (ainda ativos)
Os squads em ./squads/ incluem também:
- advisory-board, c-level-squad, hormozi-squad, movement, sop-factory
- Squads legados migrados em squads/_archive/

Ver squads/squads.md para contexto completo.

## Regras inegociáveis
- Zero TypeScript any
- Apenas CSS variables — nunca valores crus de cor
- Nunca commita em produção sem /hm-engineer
- Nunca cria feature sem spec em obsidian-vault/specs/
- Toda decisão relevante vai para obsidian-vault/decisoes/
- Toda audit vai para obsidian-vault/audits/
- Todo cliente → obsidian-vault/clientes/

## NSN Mode (Never Say Never)
Nenhum squad pode responder "não consigo" sem tentar 3+ alternativas. Máximo 5 ciclos antes de escalar. Ver .claude/rules/nsn-mode.md.

## YOLO Mode
Ativado via `/yolo` — executa sem confirmação nesta sessão. Não persiste. Ver .claude/rules/yolo-mode.md.

## Client Mode
`/client [Nome]` — carrega contexto completo de um cliente do vault.
`/client new [Nome]` — cria novo cliente. `/client list` — lista. `/client close` — fecha e salva sessão.
Ver .claude/commands/client.md.

## SKILL GRAPH NAVIGATION (OBRIGATÓRIO)

Antes de qualquer trabalho de squad, navega o grafo:

1. Identifica o squad pelo domínio da task (ver registry.yaml)
2. Lê o index do squad: obsidian-vault/squads/[squad-id]/index.md
3. Navega os MOCs relevantes via wikilinks inline
4. Carrega apenas os nodes necessários para a task
5. Executa com contexto do domínio carregado
6. Documenta o resultado no node correto do vault

Grafos disponíveis em obsidian-vault/squads/ (22 índices):
squad-dev, squad-cybersecurity, squad-copy, squad-design, squad-brand,
squad-paidmedia, squad-growth, squad-research, squad-storytelling,
squad-commercial, squad-council, squad-product, squad-animations,
squad-cloning, squad-finance, squad-content, squad-courses, squad-claude,
squad-hormozi, squad-movement, squad-advisory, squad-c-level

Regra de ouro dos wikilinks (NUNCA violar):
WIKILINKS SEMPRE inline na prosa — nunca em listas soltas no final.

Correto: "O [[squad-copy]] domina headlines usando o framework
[[before-after-bridge]] calibrado para o [[publico-alvo-zvision]]."

Errado: "Ver também: [[squad-copy]], [[before-after-bridge]]"

Depois de qualquer entrega:
- Atualiza o node relevante com o que foi aprendido
- Adiciona wikilinks inline para conectar ao grafo
- O vault fica mais inteligente a cada sessão
