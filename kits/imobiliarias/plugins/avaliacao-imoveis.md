# Plugin: Avaliador de Imóveis com IA

## O que faz
Avaliação de mercado automática usando dados reais de portais imobiliários.

## Fontes de Dados
- Mercado Livre Imóveis
- ZAP Imóveis
- Viva Real
- Dados de IPTU públicos (onde disponível)

## MCP
- **EXA** (mcp__docker-gateway__web_search_exa) — busca comparativos em tempo real
- **Apify** (mcp__docker-gateway__call-actor) — scraping de portais para dados de mercado

## Entregável
`
Relatório de Avaliação — [endereço]
- Valor médio de mercado: R$ X
- Faixa: R$ Y — R$ Z
- Comparativos: [N imóveis similares na região]
- Tendência de mercado: [subindo/estável/caindo]
- Recomendação de preço de venda/locação
`

## Agentes Zvision
- @oracle (intelligence-chief) — orquestra pesquisa de mercado
- @harvest + @radar — coleta e análise de dados
