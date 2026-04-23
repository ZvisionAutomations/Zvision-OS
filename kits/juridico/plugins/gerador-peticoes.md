# Plugin: Gerador de Peições & Documentos

## O que faz
Gera minutas de petições, contratos e notificações baseado no briefing do caso.

## Documentos Suportados
- Petição inicial (todas as áreas)
- Contestação e réplica
- Recurso de Apelação
- Agravo de Instrumento
- Contratos e aditivos
- Notificações extrajudiciais
- Procurações

## Fluxo
`
Advogado faz briefing do caso (fatos + pedidos + fundamentos)
  → IA seleciona estrutura correta por tipo de ação
  → Pesquisa jurisprudência relevante (via EXA)
  → Gera minuta estruturada com fundamentação legal
  → Advogado revisa e personaliza
  → Versão final em DOCX/PDF
`

## MCP
- **EXA** (mcp__docker-gateway__web_search_exa) — busca jurisprudência atualizada

## Agentes Zvision
- @forum (contencioso) — estrutura processual
- @clausula (contratos) — cláusulas contratuais
- @sage (squad-copy) — clareza e argumentação
