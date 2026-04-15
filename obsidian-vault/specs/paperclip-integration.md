---
name: paperclip-integration
description: Spec de integração dos 23 squads do Zvision-OS com o Paperclip (localhost:3100)
type: spec
status: draft
created: 2026-04-10
---
# Spec: Integração Paperclip × Squads Zvision-OS

> **Status:** Spec aprovada — NÃO implementar ainda.
> **Escopo:** Documentar como cada squad mapeia para o Paperclip como "employee".

## Visão Geral

O [[Paperclip]] (rodando em localhost:3100) é o sistema de orquestração de tasks
da Zvision. Cada squad do [[Zvision-OS]] mapeia para um ou mais "employees" no
Paperclip, permitindo que tasks sejam dispatched, monitoradas e cobradas via
heartbeat automatizado.

## Hierarquia de Employees

```
C-Level Squad (c-level-squad)
├── Advisory Board (advisory-board)
├── Council Squad (squad-council)
└── [Squads Operacionais]
    ├── Squad Dev (squad-dev) ← base técnica
    ├── Squad Design (squad-design)
    ├── Squad Copy (squad-copy)
    ├── Squad Brand (squad-brand)
    ├── Squad Content (squad-content)
    ├── Squad Research (squad-research)
    ├── Squad Commercial (squad-commercial)
    ├── Squad Growth (squad-growth)
    ├── Squad Paid Media (squad-paidmedia)
    ├── Squad Finance (squad-finance)
    ├── Squad Product (squad-product)
    ├── Squad Cybersecurity (squad-cybersecurity)
    ├── Squad Storytelling (squad-storytelling)
    ├── Squad Animations (squad-animations)
    ├── Squad Courses (squad-courses)
    ├── Squad Claude (squad-claude)
    ├── Squad Cloning (squad-cloning)
    ├── Hormozi Squad (hormozi-squad)
    ├── Movement (movement)
    └── SOP Factory (sop-factory)
```

## Mapeamento Squad → Employee

### Tier 1 — Estratégia (heartbeat: 1×/semana)

| Squad | Employee ID | Orquestrador | Budget Padrão | Heartbeat |
|-------|-------------|-------------|--------------|-----------|
| c-level-squad | emp-c-level | @vision-chief | R$500/task | Semanal |
| advisory-board | emp-advisory | @board-chair | R$300/task | Semanal |
| squad-council | emp-council | @council-orqx | R$200/task | Semanal |
| hormozi-squad | emp-hormozi | @hormozi-chief | R$400/task | Quinzenal |

### Tier 2 — Operacional Core (heartbeat: 3×/semana)

| Squad | Employee ID | Orquestrador | Budget Padrão | Heartbeat |
|-------|-------------|-------------|--------------|-----------|
| squad-copy | emp-copy | @copy-orqx | R$200/task | 3×/semana |
| squad-design | emp-design | @design-orqx | R$250/task | 3×/semana |
| squad-brand | emp-brand | @brand-orqx | R$300/task | 3×/semana |
| squad-commercial | emp-commercial | @commercial-orqx | R$150/task | 3×/semana |
| squad-content | emp-content | @content-orqx | R$100/task | 3×/semana |
| squad-research | emp-research | @research-orqx | R$150/task | 3×/semana |

### Tier 3 — Operacional Especializado (heartbeat: 2×/semana)

| Squad | Employee ID | Orquestrador | Budget Padrão | Heartbeat |
|-------|-------------|-------------|--------------|-----------|
| squad-dev | emp-dev | @dev-orqx | R$300/task | 2×/semana |
| squad-paidmedia | emp-paidmedia | @paidmedia-orqx | R$200/task | 2×/semana |
| squad-growth | emp-growth | @growth-orqx | R$150/task | 2×/semana |
| squad-product | emp-product | @product-orqx | R$150/task | 2×/semana |
| squad-finance | emp-finance | @finance-orqx | R$100/task | 2×/semana |
| squad-cybersecurity | emp-cyber | @cyber-orqx | R$350/task | 2×/semana |
| squad-storytelling | emp-storytelling | @storytelling-orqx | R$150/task | Semanal |
| squad-animations | emp-animations | @animations-orqx | R$400/task | Quinzenal |
| squad-courses | emp-courses | @courses-orqx | R$200/task | Quinzenal |
| squad-claude | emp-claude | @claude-orqx | R$100/task | 3×/semana |

### Tier 4 — Especialistas (heartbeat: sob demanda)

| Squad | Employee ID | Orquestrador | Budget Padrão | Heartbeat |
|-------|-------------|-------------|--------------|-----------|
| squad-cloning | emp-cloning | @cloning-orqx | R$500/task | Sob demanda |
| movement | emp-movement | @movement-chief | R$200/task | Mensal |
| sop-factory | emp-sop | @sop-chief | R$150/task | Sob demanda |

## Protocolo de Task Dispatch

### Como uma task chega a um squad via Paperclip:

```
1. Usuário ou sistema cria task no Paperclip
   → POST localhost:3100/tasks { squad_id, description, priority, budget }

2. Bridge (localhost:3300) recebe a task
   → Intent classifier identifica squad pelos keywords
   → Roteia para o orquestrador correto

3. Orquestrador do squad executa via Claude Code
   → Lê a task do Paperclip
   → Delega para especialistas internos
   → Executa com NSN mode ativo

4. Squad reporta resultado de volta ao Paperclip
   → PUT localhost:3100/tasks/{id} { status: "completed", output, time_spent }

5. Heartbeat registra conclusão
   → Paperclip atualiza status do employee
   → Billing automático pelo budget da task
```

### Formato de Task no Paperclip

```json
{
  "id": "task-uuid",
  "squad_id": "squad-dev",
  "employee_id": "emp-dev",
  "title": "Criar landing page para [cliente]",
  "description": "...",
  "priority": "high | medium | low",
  "budget": 300,
  "status": "pending | in_progress | completed | blocked",
  "created_at": "2026-04-10T00:00:00Z",
  "deadline": "2026-04-15T00:00:00Z",
  "context": {
    "client": "NomeCliente",
    "briefing_path": "obsidian-vault/clientes/NomeCliente/briefing.md"
  },
  "output": null
}
```

## Heartbeat Schedule

O heartbeat é um processo automático que verifica o estado de cada employee:

```
Heartbeat de squad-dev (2×/semana — segundas e quintas):
1. Verificar tasks pending atribuídas ao emp-dev
2. Para cada task: notificar @dev-orqx via Bridge
3. @dev-orqx delega execução
4. Atualizar status no Paperclip
5. Reportar summary: tasks completed, time spent, issues
```

### Schedule de Heartbeat por Tier

| Tier | Frequência | Dias | Hora |
|------|-----------|------|------|
| 1 — Estratégia | Semanal | Segunda | 09:00 |
| 2 — Operacional Core | 3×/semana | Seg/Qua/Sex | 08:00 |
| 3 — Operacional Especializado | 2×/semana | Seg/Qui | 08:00 |
| 4 — Especialistas | Sob demanda | — | — |

## Budget por Squad

### Critérios de Precificação

| Critério | Fator |
|---------|-------|
| Complexidade técnica | +50% para squads com stack complexa (animations, cybersecurity) |
| Tempo médio de task | Base calculada em R$100/hora estimada |
| Especialização | Premium para squads únicos (cloning, animations) |

### Limites de Budget

```
Por task:
- Tier 1: R$200-R$500
- Tier 2: R$100-R$300
- Tier 3: R$100-R$400
- Tier 4: R$150-R$500

Por mês por squad:
- Tier 1: R$2.000-R$5.000
- Tier 2: R$1.000-R$3.000
- Tier 3: R$500-R$2.000
- Tier 4: R$300-R$1.500
```

## Integração com Bridge (localhost:3300)

O Bridge é o intermediário entre o Paperclip e os squads:

```
Paperclip → Bridge → Intent Classifier → Squad Orquestrador
                  ↓
           registry.yaml (keywords)
```

### Endpoints do Bridge relevantes:

- `GET /status` — Status de todos os employees/squads
- `POST /task` — Despachar task para squad específico
- `GET /task/:id` — Status de task específica
- `GET /squads` — Listar squads disponíveis com capacidade

## Próximos Passos (pós-spec)

1. Configurar employees no Paperclip para cada squad (23 entries)
2. Atualizar Bridge para mapear employee_id → squad_id
3. Implementar heartbeat automático (cron job via WSL2)
4. Testar fluxo completo com squad-dev (task simples de landing page)
5. Rollout gradual: squad-dev → squad-copy → restantes
