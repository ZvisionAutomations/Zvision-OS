---
name: squad-finance-index
description: Entry point do Finance Squad — budget, pricing, profitability analysis e projeção de caixa
type: index
---
# Finance Squad

O squad financeiro opera com [[profitability-analyst]] para
análise de margens, [[budget-controller]] para controle orçamentário
e [[pricing-strategist]] para estrutura de precificação. O estado
financeiro da Zvision vive em [[moc-finance-zvision]].

## Agentes principais
- [[finance-orqx]] (Ledger) — orquestrador
- [[profitability-analyst]] — análise de lucratividade por serviço
- [[budget-controller]] — controle de budget e burn rate
- [[pricing-strategist]] — estrutura de pricing e valor percebido
- [[revenue-analyst]] — análise de receita e projeções

## Domínios
- [[moc-finance-zvision]] — saúde financeira da Zvision
- [[moc-finance-pricing]] — modelo de precificação por serviço
- [[moc-finance-clients]] — análise financeira por cliente

## Quando usar este squad
Análise financeira da Zvision, projeção de caixa, análise de ROI
de projetos, validar precificação de novos serviços. O [[squad-hormozi]]
define a estrutura de oferta; o finance squad valida as margens.
