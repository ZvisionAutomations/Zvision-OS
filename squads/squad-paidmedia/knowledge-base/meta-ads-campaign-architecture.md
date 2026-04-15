# Meta Ads Campaign Architecture

## Three-Tier Audience Architecture

### Tier 1: Cold (Prospeccao) — 60-70% do Budget
Objetivo: trazer novos usuarios que nunca interagiram com a marca.

**Audiences recomendadas (em ordem de prioridade):**
1. **Broad (sem interesses)** — confiar no algoritmo. Melhor opcao quando pixel tem 50+ conversoes/semana
2. **Lookalike 1% de purchasers** — melhor seed possivel. Min 1000 na seed, ideal 5000+
3. **Lookalike 1% de leads qualificados** — segundo melhor seed
4. **Lookalike 1-3% de website visitors** — mais escala, menos qualidade
5. **Interest stacking** — agrupar 3-5 interesses relacionados. Usar apenas quando broad nao funciona

**Quando usar Broad vs LAL vs Interest:**
- Pixel maduro (50+ conv/semana): Broad first
- Pixel intermediario (15-50 conv/semana): LAL 1% first
- Pixel novo (<15 conv/semana): Interest stacking como warmup

### Tier 2: Warm (Nurturing) — 20-30% do Budget
Objetivo: re-engajar usuarios que mostraram interesse.

**Audiences recomendadas:**
1. Website visitors all pages (30d, 60d, 90d)
2. Instagram/Facebook engagers (30d, 90d, 180d)
3. Video viewers 25%+ (ultimos 90d)
4. Page followers
5. Lead form openers sem submit

### Tier 3: Hot (Conversao) — 10-15% do Budget
Objetivo: converter usuarios com alta intencao.

**Audiences recomendadas:**
1. Add to Cart sem Purchase (7d, 14d)
2. Checkout initiation sem Purchase (7d)
3. Website visitors pagina de pricing (7d, 14d)
4. Video viewers 75%+ (ultimos 30d)
5. Engaged with ads (form openers, lead submits parciais)

### Exclusion Architecture
```
Cold → exclui Warm + Hot audiences
Warm → exclui Hot audiences
Hot → exclui purchasers recentes (se objetivo = new customers)
Global → exclui employees, existing customers (optional)
```

## CBO vs ABO Decision Matrix

| Cenario | Usar | Razao |
|---------|------|-------|
| Conta madura, 3-5 ad sets balanceados | CBO | Meta otimiza alocacao entre ad sets |
| Teste de audiences (quer gastar igual em cada) | ABO | Controlar spend por audience |
| Budget muito baixo (<$50/day total) | ABO | CBO pode concentrar em 1 ad set |
| Scaling agressivo | CBO | Meta encontra eficiencia |
| Audiences com tamanhos muito diferentes | CBO com min spend | Evitar concentracao |

**Default: CBO.** Usar ABO apenas para testes controlados.

## Campaign Consolidation Principles

### Regra dos 3-5
- Max 3-5 campanhas ativas por objetivo de conversao
- Mais campanhas = menos dados por campanha = pior otimizacao
- Consolidar campanhas com mesmo objetivo e audience tier

### Estrutura Ideal (Conversion objective)
```
Campaign 1: CONV_Cold_Purchase_[YYYY-MM]     (CBO, 60-70% budget)
  ├── Ad Set: Broad_AllGeo
  ├── Ad Set: LAL1_Purchasers
  └── Ad Set: LAL1_Leads

Campaign 2: CONV_Warm_Purchase_[YYYY-MM]     (CBO, 20-30% budget)
  ├── Ad Set: WV_AllPages_30d
  └── Ad Set: Engagers_90d

Campaign 3: CONV_Hot_Purchase_[YYYY-MM]      (CBO, 10-15% budget)
  ├── Ad Set: ATC_14d
  └── Ad Set: Checkout_7d

Campaign 4: TEST_Creative_[YYYY-MM]          (ABO, 10-15% de test budget)
  ├── Ad Set: Test_HookA_vs_HookB
  └── Ad Set: Test_Format_Video_vs_Image

Campaign 5 (opt): ASC_Shopping_[YYYY-MM]     (Advantage+ Shopping, full funnel)
```

### Anti-Patterns a Evitar
- 1 campanha por criativo (fragmentacao extrema)
- 10+ ad sets por campanha CBO (diluicao)
- Campanhas duplicadas para mesma audience
- Campanhas de Traffic para objetivo de conversao

## Naming Conventions

### Formato
```
Campaign:  [Objective]_[Tier]_[Optimization]_[YYYY-MM]
Ad Set:    [Audience-Type]_[Window/Detail]
Ad:        [Format]_[Hook-Type]_[Version]_[MMDD]
```

### Exemplos
```
Campaign:  CONV_Cold_Purchase_2026-03
Ad Set:    Broad_AllGeo
Ad:        VID_Question_v2_0316

Campaign:  CONV_Warm_Purchase_2026-03
Ad Set:    WV_AllPages_30d
Ad:        IMG_Testimonial_v1_0310

Campaign:  TEST_Creative_2026-03
Ad Set:    Test_Hook_Question-vs-Bold
Ad:        VID_Question_v1_0316
```

### Codigos de Audience
| Codigo | Significado |
|--------|-----------|
| Broad | Targeting amplo sem interesses |
| LAL1 | Lookalike 1% |
| LAL3 | Lookalike 1-3% |
| WV | Website Visitors |
| ENG | Engagers (social) |
| VV | Video Viewers |
| ATC | Add to Cart |
| IC | Initiate Checkout |
| PURCH | Purchasers |
