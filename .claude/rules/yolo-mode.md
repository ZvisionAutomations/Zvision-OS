---
paths: **/*
---

# YOLO Mode — Execução Autônoma

> **Desativado por padrão.** Ativado APENAS via `/yolo` explícito nesta sessão.

## O que é YOLO Mode

Quando ativo, agentes executam tarefas sem pedir confirmação intermediária:
- Criam arquivos sem perguntar
- Editam código diretamente
- Rodam comandos sem preview
- Fazem múltiplas mudanças em sequência

## Como Ativar

```
/yolo
```

Resposta esperada: "⚡ YOLO mode ativado. Executando sem confirmações nesta sessão."

## Como Desativar

```
/yolo off
```

Ou encerrar a sessão (YOLO não persiste entre conversas).

## Escopo da Ativação

- **Duração:** Apenas na sessão atual (não persiste)
- **Nível:** Todas as operações não-destrutivas
- **Herdado:** Todos os agentes/squads ativados nesta sessão

## O que YOLO Mode PERMITE (sem confirmação)

- Criar arquivos e diretórios
- Editar código existente
- Rodar comandos de build, test, linting
- Instalar dependências
- Criar commits
- Criar branches locais

## O que YOLO Mode NUNCA PERMITE (sempre requer confirmação)

Independente do YOLO mode estar ativo, estas ações SEMPRE pedem confirmação:

| Ação | Motivo |
|------|--------|
| `git push --force` | Irreversível, afeta repositório remoto |
| `git push` para `main` sem PR | Vai direto para produção |
| `rm -rf` sem backup | Irreversível |
| Drop de tabela de banco | Irreversível |
| Deletar arquivos que não fazem parte da task | Fora do escopo |
| Modificar `.env` de produção | Afeta sistema em produção |
| Revogar chaves de API | Afeta sistema em produção |

## Comportamento dos Agentes em YOLO Mode

**Sem YOLO (padrão):**
```
Vou criar o arquivo components/card.js. Posso prosseguir?
```

**Com YOLO ativo:**
```
[cria components/card.js diretamente sem perguntar]
✓ components/card.js criado
```

## Indicador Visual

Quando YOLO mode está ativo, agentes devem incluir `⚡` no início das respostas
para indicar que estão em modo autônomo.
