# Bridge Zvision-OS v2.0

Sistema nervoso central da agência — roteamento inteligente de tarefas para squads.

## Iniciar

```bash
node bridge/index.js
```

Porta: `3333`

---

## Endpoints

### GET /status

Retorna saúde da bridge, timestamp, lista dos 22 squads e uso de memória.

```bash
curl localhost:3333/status
```

Resposta:
```json
{
  "bridge": "online",
  "version": "2.0.0",
  "timestamp": "2026-04-06T...",
  "uptime_ms": 1234,
  "port": 3333,
  "squads": {
    "total": 18,
    "list": [...]
  },
  "memory": {
    "rss_mb": "45.23",
    "heap_used_mb": "12.11",
    "heap_total_mb": "18.00"
  }
}
```

---

### GET /squads

Registry completo dos squads com keywords e status.

```bash
curl localhost:3333/squads
```

---

### POST /task

Recebe descrição de tarefa, identifica o squad correto via intent classifier e retorna contexto comprimido (~70-80% de economia de tokens).

```bash
curl -X POST localhost:3333/task \
  -H 'Content-Type: application/json' \
  -d '{"task": "criar landing page para cliente"}'
```

Resposta:
```json
{
  "squad": "squad-dev",
  "squad_name": "Development Squad",
  "invoke": null,
  "context": "Squad: Development Squad (squad-dev)\n...",
  "tokens_saved": 3410,
  "task_received": "criar landing page para cliente",
  "timestamp": "2026-04-06T..."
}
```

---

## Como funciona o intent classifier

1. Normaliza o texto da tarefa (lowercase + remove acentos)
2. Compara contra as `keywords` de cada squad no registry
3. Pontua por número de matches
4. Retorna o squad com maior score
5. Fallback: `squad-dev` quando nenhuma keyword bate

## Squads disponíveis

| ID | Nome | Invoke |
|----|------|--------|
| squad-dev | Development Squad | Claude Code direto |
| squad-cybersecurity | Cybersecurity Squad | `/cyber:agents:cyber-orqx` |
| squad-copy | Copy Squad | `/copywriting:agents:copy-orqx` |
| squad-design | Design Squad | `/digital-experience:agents:design-orqx` |
| squad-brand | Brand Squad | `/brand:agents:brand-orqx` |
| squad-paidmedia | Paid Media Squad | `/pm:agents:paidmedia-orqx` |
| squad-growth | Growth Squad | `/growth:agents:growth-orqx` |
| squad-research | Research Squad | `/research:agents:research-orqx` |
| squad-storytelling | Storytelling Squad | `/narrative:agents:storytelling-orqx` |
| squad-commercial | Commercial Squad | `/commercial:agents:commercial-orqx` |
| squad-council | Council / Advisory Board | `/council:agents:council-orqx` |
| squad-product | Product Squad | `/product:agents:product-orqx` |
| squad-animations | Animations Squad | `/ca:agents:animations-orqx` |
| squad-cloning | Cloning Squad | `/SINAPSE:agents:cloning-orqx` |
| squad-finance | Finance Squad | `/finance:agents:finance-orqx` |
| squad-content | Content Squad | `/content:agents:content-orqx` |
| squad-courses | Courses Squad | `/SINAPSE:agents:courses-orqx` |
| squad-claude | Claude Code Mastery | `/claude:agents:claude-orqx` |

## Integração com CLAUDE.md

A bridge expõe o mesmo mapeamento do `squads/registry.yaml`. Para invocar o squad retornado:

```bash
# 1. Descobre o squad
SQUAD=$(curl -s -X POST localhost:3333/task \
  -H 'Content-Type: application/json' \
  -d '{"task": "sua tarefa aqui"}' | jq -r .invoke)

# 2. Usa o invoke no Claude Code
echo "Squad recomendado: $SQUAD"
```
