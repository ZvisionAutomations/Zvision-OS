---
name: zvision
description: >
  Orquestrador central do Zvision-OS. Exibe boot screen, roteia pedidos em
  linguagem natural para o squad correto via keywords do registry.yaml, e
  aplica NSN mode globalmente.
argument-hint: "[pedido em linguagem natural]"
---

# Zvision-OS — Orquestrador Central

## Boot Screen

Ao invocar `/zvision` (sem argumentos ou com argumentos), SEMPRE exibir primeiro:

```
╔══════════════════════════════════════════╗
║  ZVISION-OS v2.0 — ONLINE                ║
║  23 squads · 400+ agentes                ║
║  Vault: conectado ✓                      ║
║  Paperclip: localhost:3100               ║
║  Bridge: localhost:3300                  ║
║  Cliente ativo: [verificar contexto]     ║
╚══════════════════════════════════════════╝
Zvision pronto. O que precisa ser feito?
```

No campo "Cliente ativo": exibir nome do cliente se `/client` foi usado nesta sessão, caso contrário "nenhum".

## Input

<zvision_input>
$ARGUMENTS
</zvision_input>

## Roteamento Inteligente

### Se argumentos vazios:
Exibir boot screen e aguardar input do usuário.

### Se há argumentos (pedido em linguagem natural):

1. **Ler** o pedido do usuário
2. **Consultar** `squads/registry.yaml` — identificar squad pelos keywords
3. **Regra de match:**
   - 1 squad match claro → invocar orquestrador diretamente
   - 2-3 squads possíveis → listar e perguntar qual
   - Nenhum match → listar squads disponíveis e pedir refinamento

4. **Invocar** o orquestrador do squad identificado com:
   - O pedido original do usuário
   - Contexto do cliente ativo (se houver)
   - Instrução de NSN mode

5. **Formato de invocação:**
   ```
   Roteando para [Squad Name] (@[orquestrador])...
   
   [Invocação do agente com contexto completo]
   ```

## Mapa de Roteamento Rápido

| Pedido contém... | Squad | Invocar |
|-----------------|-------|---------|
| site, landing, código, html, css, js, deploy, bug | squad-dev | `/dev:agents:dev-orqx` |
| copy, texto, headline, email, CTA | squad-copy | `/copywriting:agents:copy-orqx` |
| design, interface, ux, ui, visual | squad-design | `/digital-experience:agents:design-orqx` |
| marca, branding, posicionamento | squad-brand | `/brand:agents:brand-orqx` |
| tráfego, ads, meta, google, campanha | squad-paidmedia | `/pm:agents:paidmedia-orqx` |
| growth, seo, analytics, conversão | squad-growth | `/growth:agents:growth-orqx` |
| pesquisa, mercado, benchmark | squad-research | `/research:agents:research-orqx` |
| narrativa, storytelling, pitch | squad-storytelling | `/narrative:agents:storytelling-orqx` |
| oferta, venda, proposta, lead | squad-commercial | `/commercial:agents:commercial-orqx` |
| decisão, conselho, prioridade | squad-council | `/council:agents:council-orqx` |
| financeiro, budget, caixa, ROI | squad-finance | `/finance:agents:finance-orqx` |
| conteúdo, blog, social, instagram | squad-content | `/content:agents:content-orqx` |
| segurança, pentest, audit, OWASP | squad-cybersecurity | `/cyber:agents:cyber-orqx` |
| animação, motion, threejs, shader | squad-animations | `/ca:agents:animations-orqx` |
| produto, roadmap, discovery, mvp | squad-product | `/product:agents:product-orqx` |
| curso, treinamento, módulo | squad-courses | `/SINAPSE:agents:courses-orqx` |
| claude code, mcp, hook, skill | squad-claude | `/claude:agents:claude-orqx` |
| estratégia, board, visão longo prazo | advisory-board | `/council:agents:board-chair` |
| ceo, cto, cmo, executivo | c-level-squad | `/council:agents:vision-chief` |
| clone, persona, digital twin | squad-cloning | `/SINAPSE:agents:cloning-orqx` |
| hormozi, oferta, escala, modelo de negócio | hormozi-squad | (invocar @hormozi-chief) |
| movimento, manifesto, causa, cultura | movement | (invocar @movement-chief) |
| sop, processo, procedimento | sop-factory | (invocar @sop-chief) |

## NSN Mode Global

Este orquestrador aplica NSN Mode (`.claude/rules/nsn-mode.md`) globalmente:
- Nenhum squad pode responder "não consigo" sem tentar 3+ alternativas
- Máximo 5 ciclos antes de escalar com contexto documentado

## YOLO Mode

Se o usuário digitar `/yolo` antes ou junto do pedido:
- Ativar YOLO mode para a sessão (`.claude/rules/yolo-mode.md`)
- Confirmar: "⚡ YOLO mode ativado. Executando sem confirmações nesta sessão."
- Passar flag YOLO para o squad invocado

## Comandos Especiais

| Comando | Ação |
|---------|------|
| `/zvision squads` | Listar todos os 23 squads com descrição |
| `/zvision status` | Status de Paperclip (localhost:3100) e Bridge (localhost:3300) |
| `/zvision client` | Alias para `/client` |
| `/zvision yolo` | Ativar YOLO mode |
