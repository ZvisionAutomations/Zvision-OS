# SPEC — Zvision-OS Fase 2: Orquestração Autônoma
# Para execução via Claude Code
# Versão: 1.0.0

## CONTEXTO

Você é o executor da Fase 2 do Zvision-OS. O sistema já tem:
- 22 squads canônicos em `/mnt/c/Users/Lenovo/Documents/zvision-OS/squads/`
- Bridge v2.0 rodando na porta 3333 (classificador de intent)
- Vault Obsidian em `/mnt/c/Users/Lenovo/Documents/zvision-OS/obsidian-vault/`
- Node.js v24.13.1 instalado

O objetivo desta fase é: **squads rodando em background, Miguel aprova tickets, eles executam — sem Claude Code aberto o tempo todo.**

---

## REGRAS DE EXECUÇÃO

1. **Leia esta spec inteira antes de escrever qualquer código**
2. **Execute uma tarefa por vez, na ordem definida**
3. **Após cada tarefa, confirme o resultado antes de avançar**
4. **Se encontrar erro, tente resolver. Se não conseguir em 2 tentativas, documente e pule para a próxima tarefa**
5. **Nunca delete arquivos sem fazer backup primeiro**
6. **Documente cada decisão no vault: `/mnt/c/Users/Lenovo/Documents/zvision-OS/obsidian-vault/fase2-log.md`**

---

## TAREFA 1 — Atualizar o Bridge com os 22 squads canônicos

**Objetivo:** O `bridge/index.js` atual tem 18 squads e mapeia errado os legados. Precisa refletir os 22 squads reais.

**Arquivo alvo:** `/mnt/c/Users/Lenovo/Documents/zvision-OS/bridge/index.js`

**O que fazer:**
1. Fazer backup: copiar `index.js` para `index.js.bak`
2. Atualizar o array `SQUADS` para incluir todos os 22 squads canônicos:
   - Manter os 18 existentes
   - Adicionar: `advisory-board`, `c-level-squad`, `hormozi-squad`, `movement`, `sop-factory`
3. Atualizar o `LEGACY_MAP` — remover mapeamentos incorretos:
   - `hormozi-squad` não mapeia mais para `squad-commercial` (é canônico agora)
   - `advisory-board` não mapeia mais para `squad-council` (é canônico agora)
   - `c-level-squad` não mapeia mais para `squad-product` (é canônico agora)
   - `movement` não mapeia mais para `squad-storytelling` (é canônico agora)
   - `sop-factory` não mapeia mais para `squad-dev` (é canônico agora)
4. Adicionar os 5 novos squads com keywords relevantes:

```
advisory-board: keywords = ['visão', 'longo prazo', 'board', 'decisão estratégica', 'investimento', 'fundador', 'dalio', 'naval', 'munger', 'thiel', 'hoffman']
c-level-squad: keywords = ['ceo', 'cto', 'cmo', 'coo', 'executivo', 'c-level', 'liderança', 'empresa', 'estrutura organizacional']
hormozi-squad: keywords = ['hormozi', 'oferta irresistível', 'leads', 'escala', 'retenção', 'pricing', 'modelo de negócio', 'aquisição', 'upsell', 'downsell']
movement: keywords = ['movimento', 'manifesto', 'impacto', 'causa', 'cultura', 'identidade de movimento', 'fenomenologia']
sop-factory: keywords = ['sop', 'processo', 'procedimento', 'documentação', 'manual', 'padronização', 'operacional', 'fábrica de sop']
```

5. Testar o bridge:
```bash
cd /mnt/c/Users/Lenovo/Documents/zvision-OS
node bridge/index.js &
sleep 2
curl http://localhost:3333/status
curl http://localhost:3333/squads | grep -c '"id"'
curl -X POST http://localhost:3333/task -H "Content-Type: application/json" -d '{"task": "preciso estruturar uma oferta irresistível para meu cliente"}'
kill %1
```

**Critério de sucesso:** `/squads` retorna 22 squads. POST `/task` com "oferta irresistível" roteia para `hormozi-squad`.

---

## TAREFA 2 — Instalar o Paperclip

**Objetivo:** Instalar o Paperclip como orquestrador central (Layer 3).

**O que fazer:**
1. Verificar se já está instalado:
```bash
npx paperclipai --version 2>/dev/null || echo "não instalado"
```

2. Se não instalado, instalar:
```bash
cd /mnt/c/Users/Lenovo/Documents/zvision-OS
npx paperclipai onboard --yes
```

3. Verificar se subiu:
```bash
curl http://localhost:3100/health 2>/dev/null || echo "não rodando"
```

4. Se precisar rodar manualmente:
```bash
cd /mnt/c/Users/Lenovo/Documents/zvision-OS
npx paperclipai start &
sleep 5
curl http://localhost:3100/health
```

**Critério de sucesso:** `curl http://localhost:3100/health` retorna status online.

---

## TAREFA 3 — Configurar os squads principais no Paperclip

**Objetivo:** Registrar os 5 squads mais importantes como agentes no Paperclip para validar a integração.

**Squads prioritários para configurar primeiro:**
1. `squad-commercial` — prospecção e vendas
2. `squad-copy` — produção de copy para clientes
3. `squad-content` — conteúdo
4. `hormozi-squad` — ofertas e escala
5. `advisory-board` — decisões estratégicas

**O que fazer:**
1. Verificar onde o Paperclip armazena configuração de agentes:
```bash
ls ~/.paperclip/ 2>/dev/null || ls /mnt/c/Users/Lenovo/Documents/zvision-OS/.paperclip/ 2>/dev/null
```

2. Para cada squad prioritário, criar um arquivo de configuração de agente no formato AGENTS.md do Paperclip. Consultar a documentação em:
```bash
cat /mnt/c/Users/Lenovo/Documents/zvision-OS/node_modules/paperclipai/AGENTS.md 2>/dev/null | head -100
```

3. Criar a empresa Zvision no Paperclip via CLI ou API:
```bash
npx paperclipai company create --name "Zvision" --goal "Agência de automação que entrega projetos completos para clientes usando squads de IA especializados"
```

4. Registrar cada squad prioritário como agente:
```bash
# Exemplo para squad-commercial
npx paperclipai agent create \
  --company "Zvision" \
  --name "Commercial Squad" \
  --role "Pipeline comercial, prospecção, qualificação de leads e estruturação de propostas" \
  --invoke "/commercial:agents:commercial-orqx"
```

**Critério de sucesso:** Os 5 squads aparecem no dashboard do Paperclip em `http://localhost:3100`.

---

## TAREFA 4 — Conectar o Bridge ao Paperclip

**Objetivo:** O bridge classifica o intent e passa para o Paperclip executar. Paperclip despacha para o squad correto.

**O que fazer:**
1. Adicionar endpoint `/dispatch` no bridge que:
   - Recebe a task
   - Classifica o squad via `classifyIntent()`
   - Faz POST para `http://localhost:3100/api/tasks` com o squad e contexto
   - Retorna o ticket ID do Paperclip

2. O payload para o Paperclip deve ser:
```json
{
  "company": "Zvision",
  "agent": "<squad_id>",
  "task": "<task_original>",
  "context": "<context_comprimido_do_bridge>",
  "priority": "normal"
}
```

3. Testar o fluxo completo:
```bash
curl -X POST http://localhost:3333/dispatch \
  -H "Content-Type: application/json" \
  -d '{"task": "criar proposta comercial para cliente de e-commerce"}'
```

**Critério de sucesso:** O comando acima cria um ticket no Paperclip e retorna o ticket ID.

---

## TAREFA 5 — Criar script de boot do sistema

**Objetivo:** Um único comando para subir tudo.

**Arquivo:** `/mnt/c/Users/Lenovo/Documents/zvision-OS/start.sh`

**Conteúdo:**
```bash
#!/bin/bash
echo "🚀 Iniciando Zvision-OS..."

# Kill processos anteriores nas portas
fuser -k 3333/tcp 2>/dev/null
fuser -k 3100/tcp 2>/dev/null

# Subir Paperclip
echo "→ Subindo Paperclip (porta 3100)..."
cd /mnt/c/Users/Lenovo/Documents/zvision-OS
npx paperclipai start &
PAPERCLIP_PID=$!
sleep 5

# Verificar Paperclip
if curl -s http://localhost:3100/health > /dev/null; then
  echo "✅ Paperclip online"
else
  echo "❌ Paperclip falhou"
  exit 1
fi

# Subir Bridge
echo "→ Subindo Bridge (porta 3333)..."
node bridge/index.js &
BRIDGE_PID=$!
sleep 2

# Verificar Bridge
if curl -s http://localhost:3333/status > /dev/null; then
  echo "✅ Bridge online"
else
  echo "❌ Bridge falhou"
  exit 1
fi

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║   Zvision-OS — SISTEMA OPERACIONAL       ║"
echo "║                                          ║"
echo "║   Paperclip:  http://localhost:3100      ║"
echo "║   Bridge:     http://localhost:3333      ║"
echo "║   Squads:     22 canônicos               ║"
echo "╚══════════════════════════════════════════╝"
```

Tornar executável:
```bash
chmod +x /mnt/c/Users/Lenovo/Documents/zvision-OS/start.sh
```

**Critério de sucesso:** `bash start.sh` sobe tudo sem erro.

---

## TAREFA 6 — Documentar no Vault

**Arquivo:** `/mnt/c/Users/Lenovo/Documents/zvision-OS/obsidian-vault/fase2-log.md`

**Criar com:**
- Data de execução
- Status de cada tarefa (✅ / ❌ / ⚠️ parcial)
- Problemas encontrados e como foram resolvidos
- Próximos passos para a Fase 3

---

## ORDEM DE EXECUÇÃO

```
Tarefa 1 → Tarefa 2 → Tarefa 3 → Tarefa 4 → Tarefa 5 → Tarefa 6
```

Não pule tarefas. Se uma falhar parcialmente, documente e continue.

---

## AO TERMINAR

Reportar para Miguel:
1. Status de cada tarefa
2. URLs funcionando
3. Comando para testar o fluxo completo
4. O que ficou pendente e por quê
