---
name: client
description: >
  Gerencia contexto de cliente ativo — carrega, cria, lista e fecha sessões de cliente.
  Integra com obsidian-vault/clientes/ e passa contexto para squads.
argument-hint: "[NomeCliente | new NomeCliente | list | close]"
---

# Client Mode — Contexto de Cliente

## Input

<client_command>
$ARGUMENTS
</client_command>

## Subcomandos

### `/client [NomeCliente]` — Carregar cliente

1. Busca `obsidian-vault/clientes/` por pasta que match (fuzzy) o nome fornecido
2. Se encontrado:
   - Lê `briefing.md` (contexto, segmento, objetivo, stack)
   - Lê `historico.md` (últimas 20 linhas — sessões anteriores)
   - Lê `projetos.md` (projetos ativos)
3. Define cliente ativo na sessão
4. Identifica squad relevante pelos keywords do segmento do cliente
5. Confirma:
   ```
   ✓ Cliente: [NomeCliente]
   ✓ Segmento: [segmento do briefing]
   ✓ Squad relevante: [squad identificado]
   ✓ Projetos ativos: [lista de projetos]
   
   Contexto carregado. O que precisa ser feito para [NomeCliente]?
   ```
6. Se não encontrado: "Cliente '[nome]' não encontrado. Use `/client list` para ver clientes ou `/client new [nome]` para criar."

---

### `/client new [NomeCliente]` — Criar novo cliente

1. Criar diretório `obsidian-vault/clientes/[NomeCliente]/`
2. Criar `briefing.md`:
   ```markdown
   ---
   name: [NomeCliente]
   status: ativo
   created: [data de hoje]
   segmento: [preencher]
   squad_principal: [preencher]
   ---
   # Briefing — [NomeCliente]
   
   ## Empresa
   - **Nome:** [NomeCliente]
   - **Segmento:** [ex: imobiliária, clínica, e-commerce]
   - **Tamanho:** [ex: pequena empresa, startup, solopreneur]
   
   ## Problema Principal
   [Qual a dor ou objetivo que trouxe o cliente para a Zvision?]
   
   ## Objetivo do Projeto
   [O que precisa ser entregue?]
   
   ## Stack / Restrições Técnicas
   [HTML/CSS/JS? WordPress? Plataforma específica?]
   
   ## Decisões Tomadas
   [Decisões estratégicas ou técnicas já definidas]
   
   ## Pessoas
   - **Contato principal:** [nome e cargo]
   - **Decisor:** [quem aprova]
   ```
3. Criar `historico.md`:
   ```markdown
   # Histórico de Sessões — [NomeCliente]
   
   <!-- Sessões adicionadas automaticamente pelo /client close -->
   ```
4. Criar `projetos.md`:
   ```markdown
   # Projetos — [NomeCliente]
   
   ## Ativos
   
   ## Concluídos
   ```
5. Confirmar:
   ```
   ✓ Cliente [NomeCliente] criado.
   Preencha o briefing em: obsidian-vault/clientes/[NomeCliente]/briefing.md
   
   Quer que eu abra o briefing para preenchimento agora?
   ```

---

### `/client list` — Listar clientes

1. Listar todos os diretórios em `obsidian-vault/clientes/`
2. Para cada um, ler metadata do `briefing.md` (status, segmento)
3. Exibir:
   ```
   Clientes cadastrados:
   
   ● [NomeCliente1] — [segmento] — ativo
   ● [NomeCliente2] — [segmento] — ativo
   ○ [NomeCliente3] — [segmento] — arquivo
   
   Total: [N] clientes
   ```
   (● = ativo, ○ = arquivo/inativo)

---

### `/client close` — Fechar sessão

1. Se nenhum cliente ativo: "Nenhum cliente ativo nesta sessão."
2. Gerar resumo da sessão:
   ```markdown
   ## Sessão [data e hora]
   
   **Squads utilizados:** [lista dos squads invocados nesta sessão]
   **Entregas:**
   - [o que foi produzido / decidido]
   
   **Decisões:**
   - [decisões tomadas nesta sessão]
   
   **Próximas ações:**
   - [o que ficou pendente]
   ```
3. Fazer append no `obsidian-vault/clientes/[NomeCliente]/historico.md`
4. Remover cliente ativo do contexto da sessão
5. Confirmar:
   ```
   ✓ Sessão de [NomeCliente] fechada e salva em historico.md
   
   Resumo salvo:
   [exibir resumo gerado]
   ```

## Integração com /zvision

Quando um cliente está ativo via `/client`, o orquestrador `/zvision` automaticamente:
- Passa o briefing do cliente para o squad invocado
- Inclui histórico relevante no contexto
- Prioriza o squad_principal definido no briefing

## Regra de Contexto

Com cliente ativo, QUALQUER pedido ao `/zvision` recebe como contexto adicional:
```
[Contexto de Cliente Ativo]
Cliente: [NomeCliente]
Segmento: [segmento]
Objetivo: [objetivo principal do briefing]
```
