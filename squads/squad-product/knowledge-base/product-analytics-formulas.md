# Product Analytics Formulas Reference

## Purpose
Referencia de formulas padronizadas para calculo de metricas de produto. Usar estas definicoes garante consistencia entre clientes e reports.

## Acquisition Metrics
```
Signup Rate = New Signups / Unique Visitors × 100
CAC = Total Marketing Spend / New Customers Acquired
Viral Coefficient (K) = Invitations per User × Conversion per Invitation
Payback Period = CAC / Monthly Revenue per Customer (months)
Channel Mix = Signups from Channel X / Total Signups × 100
```

## Activation Metrics
```
Activation Rate = Users who reached Aha Moment / Total Signups × 100
Time to Value (TTV) = Median(Aha Timestamp - Signup Timestamp)
Onboarding Completion = Users who completed onboarding / Users who started × 100
Setup Success Rate = Users with complete setup / Total new users × 100
```

## Engagement Metrics
```
DAU = Unique users who performed core action in last 24h
WAU = Unique users who performed core action in last 7 days
MAU = Unique users who performed core action in last 30 days
DAU/MAU Ratio = DAU / MAU (>0.25 excellent, 0.15-0.25 good, <0.15 concerning)
Stickiness = DAU / WAU (or DAU/MAU)
Session Frequency = Total Sessions / Unique Users (per period)
Session Duration = Avg(session_end - session_start)
Feature Adoption = Users of Feature X / Total Active Users × 100
Depth of Engagement = Core Actions per Session (avg)
```

## Retention Metrics
```
Classic Retention (Day N) = Users active on Day N / Cohort Size × 100
Rolling Retention = Users active within N-day window / Cohort Size × 100
Churn Rate (Monthly) = Customers Lost / Customers at Start × 100
Net Revenue Retention = (Start MRR + Expansion - Contraction - Churn) / Start MRR × 100
Logo Retention = (Customers Start - Churned) / Customers Start × 100
Resurrection Rate = Previously Churned who Returned / Total Churned × 100
```

## Revenue Metrics
```
MRR = Sum of all active monthly subscriptions
ARR = MRR × 12
ARPU = Total Revenue / Total Active Users
ARPPU = Total Revenue / Paying Users Only
LTV = ARPU × Average Customer Lifetime (months)
LTV/CAC = LTV / CAC (target: >3x)
Quick Ratio = (New MRR + Expansion MRR) / (Contraction + Churn MRR)
  >4 excellent | 2-4 good | <2 leaky bucket
Expansion Revenue Rate = Expansion MRR / Starting MRR × 100
```

## Product Health Composite
```
Health Score = (Product × 0.30) + (Delivery × 0.25) + (Client × 0.25) + (Strategic × 0.20)

Product Sub-Score:
  Activation Rate (25%) + D30 Retention (25%) + Feature Adoption (20%) + NPS (15%) + Error Rate (15%)

Delivery Sub-Score:
  Velocity Consistency (30%) + Deploy Frequency (25%) + Bug Escape (25%) + Debt Ratio (20%)

Client Sub-Score:
  CSAT (35%) + On-time Delivery (30%) + Scope Creep (20%) + Comms Quality (15%)

Strategic Sub-Score:
  OKR Progress (40%) + Roadmap Completion (30%) + Discovery Velocity (30%)

Bands: 80-100 GREEN | 60-79 YELLOW | 40-59 ORANGE | 0-39 RED
```

## PLG Metrics
```
PQL Score = (Behavioral × 0.7) + (Firmographic × 0.3)
Natural Rate of Revenue = Self-serve Revenue / Total New Revenue × 100
Product-Driven Expansion = Usage-triggered Expansion / Total Expansion × 100
```

## Sprint & Delivery Metrics
```
Sprint Velocity = Sum of story points COMPLETED in sprint
Completion Rate = Points Completed / Points Committed × 100
Unplanned Ratio = Unplanned Points / Total Points × 100
Velocity CV = σ / Mean × 100 (predictability: <15% good, 15-25% ok, >25% volatile)
Tech Debt Ratio = Time to Fix All Debt / Time to Rebuild
```

## Experiment Metrics
```
Sample Size = (Z_α/2 + Z_β)² × [p1(1-p1) + p2(1-p2)] / (p2-p1)²
  Z_α/2 = 1.96 (95% confidence)
  Z_β = 0.84 (80% power)

Statistical Significance: p < 0.05
Bonferroni Correction: α_adjusted = 0.05 / number_of_tests
```

## Satisfaction Metrics
```
NPS = % Promoters (9-10) - % Detractors (0-6)
  Range: -100 to +100
  Good: >0 | Great: >50 | Excellent: >70

CSAT = Satisfied Responses / Total Responses × 100
CES = Sum of Effort Scores / Total Responses (lower = better)
```

## Benchmarks
| Metric | Average SaaS | Top SaaS | Source |
|--------|-------------|----------|--------|
| D1 Retention | 35% | 50% | Lenny Rachitsky |
| D7 Retention | 20% | 35% | Lenny Rachitsky |
| D30 Retention | 12% | 25% | Lenny Rachitsky |
| Activation Rate | 20-40% | 40-60% | OpenView |
| NPS | 20-30 | 50+ | Bain |
| DAU/MAU | 10-15% | 25%+ | a16z |
| LTV/CAC | 3x | 5x+ | SaaS benchmarks |
| Quick Ratio | 2-3 | 4+ | Mamoon Hamid |
| Net Revenue Retention | 100-110% | 120%+ | KeyBanc |
