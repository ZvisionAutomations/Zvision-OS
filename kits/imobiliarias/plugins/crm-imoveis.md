# Plugin: CRM Inteligente para Imóveis

## O que faz
Pipeline de vendas com qualificação automática de compradores e locatários via IA.

## Fluxo Principal
`
Lead entra (WhatsApp/Portal/Ads)
  → IA coleta: tipo, valor, bairro, urgência, forma de pagamento
  → Score de qualificação (0-100)
  → Score >= 70: alerta imediato para corretor
  → Score < 70: nutrir com conteúdo automatizado
  → Follow-up automático em 24h/72h/7d se sem resposta
`

## Integrações
- WhatsApp Business API (n8n)
- Google Sheets / Notion (CRM leve)
- ZAP Imóveis, Viva Real, OLX (via webhook)

## Setup
1. Configurar webhook nos portais
2. Conectar WhatsApp via n8n
3. Definir critérios de qualificação com o cliente
4. Treinar IA com as perguntas do corretor ideal

## MCP Necessário
Nenhum — operação nativa via n8n
