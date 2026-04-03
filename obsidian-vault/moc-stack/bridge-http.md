---
name: bridge-http
description: Bridge HTTP entre Paperclip e squads Zvision — intent classifier + scoped skills + context pruning
---
# Bridge HTTP

Cola técnica entre o Paperclip (empresa) e os squads do Zvision-OS.

## Localização

`C:\Users\Lenovo\aios-core\bridge\index.js`

## O que faz

1. Recebe task do Paperclip via `POST /execute`
2. Classifica intent por palavras-chave (0 tokens gastos)
3. Carrega só o contexto do squad relevante (scoped skills)
4. Poda o histórico para máximo 3 turnos
5. Executa via `claude -p` (stdin pipe)
6. Retorna resultado + squad usado para o Paperclip
7. Fallback gracioso se claude CLI não disponível

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/execute` | Executa squad (intent auto ou explícito) |
| `GET` | `/health` | Status do bridge |
| `GET` | `/squads` | Lista squads disponíveis |
| `GET` | `/squads/:name` | Preview do contexto de um squad |

## Payload de execute

```json
{
  "task": "preciso de uma auditoria de segurança no CRM",
  "squad": "cybersecurity",    // opcional — auto-classificado se omitido
  "context": ["turno 1", "turno 2"]  // opcional — histórico
}
```

## Resultado

Redução estimada de 70-80% de tokens vs carregar todos os squads.
Referência: [[token-optimization]]

## Instalação

```
C:\Users\Lenovo\aios-core\bridge\
  index.js       ← servidor Express
  package.json   ← só Express como dep
  node_modules\
```

## Status
✅ Instalado e operacional — v2.0.0 em localhost:3300
