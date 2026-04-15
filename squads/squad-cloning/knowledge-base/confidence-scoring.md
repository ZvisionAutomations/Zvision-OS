# Confidence Scoring — Metodologia de Calculo

> Como calcular, interpretar e aplicar o confidence score de um clone cognitivo.

---

## Formula

```
Confidence = (direct × 1.0 + inferred × 0.7 + hypothesis × 0.3) / total_extractions × 100
```

Onde:
- **direct** = numero de extracoes tagadas [DIRETO]
- **inferred** = numero de extracoes tagadas [INFERIDO]
- **hypothesis** = numero de extracoes tagadas [HIPOTESE]
- **total_extractions** = direct + inferred + hypothesis

---

## Tags de Confianca

### [DIRETO] — Peso 1.0
Citacao literal da propria pessoa, transcricao direta.
- Palavras exatas da pessoa em video, audio, texto
- Citacao entre aspas de livro/artigo proprio
- Screenshot/link direto do conteudo original

**Exemplo:** "Minha regra numero 1: nunca gaste mais em ads do que 30% da receita do mes anterior" — Gary Vee, podcast EP 234

### [INFERIDO] — Peso 0.7
Padrao observado em 3+ fontes independentes.
- Mesmo conceito explicado de formas diferentes em fontes distintas
- Comportamento consistente observado em multiplos contextos
- Principio que transparece em acoes documentadas

**Exemplo:** [INFERIDO] Russell Brunson prioriza 'story-driven selling' — mencionado em DotCom Secrets (cap 4), Expert Secrets (cap 7), e 3 episodios do Marketing Secrets podcast.

### [HIPOTESE] — Peso 0.3
Extraido de 1 unica fonte ou inferido de contexto limitado.
- Mencionado apenas uma vez
- Inferido de uma acao/exemplo especifico
- Extrapolacao do analista (precisa validacao)

**Exemplo:** [HIPOTESE] Parece preferir launches em Janeiro/Setembro baseado em 2 exemplos — necessita mais dados.

---

## Thresholds

| Score | Classificacao | Tier elegivel | Acao |
|-------|--------------|--------------|------|
| ≥85% | Alta confianca | Tier 3 (Full Clone) | Clone completo |
| 75-84% | Boa confianca | Tier 2 (Consultant) | Clone com agente |
| 60-74% | Moderada | Tier 1 (KB-only) | Apenas KBs |
| <60% | Insuficiente | Nenhum | NAO gerar clone |

---

## Calculo por Layer

O score geral e uma media, mas e util calcular por layer:

| Layer | Peso no score geral | Justificativa |
|-------|-------------------|---------------|
| L1: Mental Models | 25% | Core do pensamento |
| L2: Heuristics | 25% | Core das decisoes |
| L3: Workflows | 20% | Metodologia pratica |
| L4: Communication | 15% | Estilo (menos critico) |
| L5: Meta-patterns | 15% | Emergente (depende de volume) |

**Red flag:** Se L1 ou L2 < 60% mas L4 > 85%, o clone pode "soar" como a pessoa mas nao "pensar" como ela. Isso e perigoso — priorize core layers.

---

## Principio de Honestidade

**NUNCA inventar o que nao foi extraido.**

- Se nao encontrou mental models suficientes: documente como gap, nao invente
- Se uma heuristic parece obvia mas nao foi dita: marque como [HIPOTESE]
- Se terceiros atribuem algo a pessoa mas ela nunca disse: marque como [HIPOTESE]
- Se ha duvida entre [INFERIDO] e [HIPOTESE]: use [HIPOTESE]

O objetivo e fidelidade, nao completude. Um clone parcial honesto e mais util que um clone completo fabricado.

---

## Calibracao

Para calibrar o scoring:
1. Comece com extracoes [DIRETO] (baseline de alta confianca)
2. Adicione [INFERIDO] apenas com 3+ fontes de suporte
3. Use [HIPOTESE] para tudo o mais
4. Revise: algum [INFERIDO] deveria ser [HIPOTESE]?
5. Recalcule
6. Se score surpreende (muito alto ou baixo), revise tags
