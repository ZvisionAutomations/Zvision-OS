---
id: squad-health
name: Squad Health Check
agent: evolve-monitor (Pulse)
trigger: manual | /zvision status
---

# Task: squad-health

## Objetivo
Verificar saúde e performance de todos os 27 squads do Zvision-OS.

## Health Metrics por Squad

Para cada squad em `squads/registry.yaml`:

```yaml
health_check:
  squad_id: [id]
  memory_file: exists | missing
  agents_count: [N]
  last_session: [data ou "nunca usado"]
  friction_score: 0-10 (baseado em session logs)
  status: healthy | needs-attention | stale
```

## Critérios de Status

| Status | Critério |
|--------|---------|
| `healthy` | Usado nas últimas 5 sessões, friction score < 4 |
| `needs-attention` | Friction score >= 4 ou memory file desatualizado |
| `stale` | Nunca usado ou não usado em 20+ sessões |
| `new` | Criado mas ainda não testado |

## Output

```
⚡ Squad Health Report — Zvision-OS NEXUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Healthy (N squads):
  squad-dev, squad-copy, squad-brand...

⚠ Needs Attention (N squads):
  squad-X: friction score 7/10 — [motivo]

🆕 New - Not Yet Tested (N squads):
  squad-arte, squad-evolve, squad-juridico...

📦 Stale (N squads):
  squad-X: último uso há 20+ sessões

Recomendação: [próximas ações]
```
