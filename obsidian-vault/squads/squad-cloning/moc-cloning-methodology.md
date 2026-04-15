---
name: moc-cloning-methodology
squad: squad-cloning
type: moc
description: Metodologia de clonagem cognitiva — extração, síntese e ativação de digital twins
---
# Cloning Methodology

## Processo de extração
O [[cognitive-extractor]] captura o modelo mental em 3 camadas:
crenças e valores (o porquê das decisões), heurísticas e atalhos
cognitivos (como decide rapidamente), e estilo de comunicação
(como expressa o pensamento). Sem as 3 camadas, o clone é superficial.

## Síntese via Mind Synthesizer
O [[mind-synthesizer]] organiza as 3 camadas em estrutura navegável
no vault. O resultado não é um prompt — é um skill graph navegável
que o [[cognitive-extractor]] atualiza a cada nova interação.

## Ativação do clone
O clone ativado pelo [[cloning-orqx]] tem acesso ao skill graph
e simula as decisões com base nas heurísticas extraídas.
Não substitui a pessoa — é um proxy para brainstorming e
validação quando a pessoa não está disponível.

## Restrições éticas
Toda clonagem exige autorização documentada em [[obsidian-vault/decisoes/]].
O [[cloning-orqx]] bloqueia uso do clone para comunicações externas
sem aprovação explícita do original.
