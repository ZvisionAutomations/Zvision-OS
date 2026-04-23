# Plugin: Gerador de Contratos Imobiliários

## O que faz
Gera contratos de compra, venda e locação com cláusulas automáticas por estado brasileiro.

## Tipos de Contratos
- Compromisso de Compra e Venda
- Contrato de Locação Residencial (Lei 8.245/91)
- Contrato de Locação Comercial
- Procuração Imobiliária
- Contrato de Prestação de Serviços (Corretor)

## Fluxo
`
Dados do negócio coletados (partes, imóvel, valor, condições)
  → IA seleciona template correto por estado + tipo
  → Preenche todas as cláusulas automaticamente
  → Validação jurídica básica (@clausula)
  → PDF gerado e enviado via WhatsApp/email
  → Registro em CRM
`

## Agentes Zvision
- @clausula (contratos) — valida cláusulas e sugere ajustes
- @datum (LGPD) — garante conformidade de dados pessoais no contrato

## LGPD
Todos os contratos incluem cláusula de tratamento de dados pessoais conforme LGPD.

## Output
- Contrato em PDF pronto para assinatura
- Versão Word editável para ajustes manuais
