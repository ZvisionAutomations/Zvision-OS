---
id: optimize-prompt
name: Optimize Prompt
agent: evolve-optimizer (Refine)
trigger: manual | auto após 5 usos de um squad
---

# Task: optimize-prompt

## Objetivo
Analisar performance de um squad específico e propor otimizações nos prompts dos agentes.

## Inputs
- `squad_id`: ID do squad a otimizar
- Últimas N entradas do session-log referentes a este squad
- Memory file do squad: `squads/{squad-id}/memory.md`

## Protocolo

### 1. Leitura de Histórico
```
Ler: squads/{squad-id}/memory.md
Ler: squad-evolve/memory/session-log.md (filtrar pelo squad)
Identificar: padrões de friction e sucesso
```

### 2. Análise dos Agentes
Para cada agente do squad:
- O prompt atual está alinhado com os casos de uso reais?
- Há ambiguidade nas instruções?
- Falta algum comando que seria útil?
- Há comandos que nunca são usados?

### 3. Geração de Propostas
```yaml
optimization:
  squad: [squad-id]
  agent: [agent-id]
  current_issue: "[descrição do problema]"
  proposed_change: "[mudança específica no prompt]"
  expected_improvement: "[resultado esperado]"
  priority: high | medium | low
```

### 4. Validação
- Proposta não deve quebrar casos de uso existentes
- Mudança deve ser incremental (< 30% do prompt original)
- Registrar em `squads/squad-evolve/memory/optimization-queue.md`

## Output
Lista de propostas de otimização com prioridade e impacto esperado.
