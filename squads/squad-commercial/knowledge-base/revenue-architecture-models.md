# Revenue Architecture Models

## Unit Economics Fundamentals

### Customer Acquisition Cost (CAC)
```
CAC = Total Sales & Marketing Spend / New Customers Acquired

Components:
  Sales costs: salaries, commissions, tools, travel
  Marketing costs: campaigns, content, events, tools
  Overhead allocation: management, operations support

Benchmark (B2B Services):
  CAC < R$5K: Low-touch, efficient
  CAC R$5-25K: Mid-market typical
  CAC > R$25K: Enterprise, acceptable if LTV justifies

Blended vs Organic vs Paid CAC:
  Track separately to understand channel efficiency
```

### Lifetime Value (LTV)
```
LTV = ARPA × Gross Margin % × Average Customer Lifespan

Simplified:
  LTV = ARPA × Gross Margin % / Churn Rate

Example:
  ARPA: R$10K/month
  Gross Margin: 65%
  Monthly Churn: 2%
  LTV = R$10K × 0.65 / 0.02 = R$325K
```

### LTV:CAC Ratio
```
Target: ≥ 3:1 (minimum), 5:1 (healthy), >8:1 (may be underinvesting)

Interpretation:
  < 1:1  → Losing money on every customer (crisis)
  1-3:1  → Unsustainable growth
  3-5:1  → Healthy, efficient growth
  5-8:1  → Strong unit economics
  > 8:1  → Potentially underinvesting in growth
```

### CAC Payback Period
```
CAC Payback = CAC / (ARPA × Gross Margin %)

Target: < 18 months (ideal < 12)

Example:
  CAC: R$30K
  ARPA: R$5K/month
  Gross Margin: 60%
  Payback = R$30K / (R$5K × 0.60) = 10 months ✓
```

---

## SaaS / Recurring Revenue Metrics

### ARR / MRR
```
MRR = Sum of all monthly recurring revenue
ARR = MRR × 12

MRR Components:
  New MRR: From new customers this month
  Expansion MRR: Upgrades, upsells, cross-sells
  Contraction MRR: Downgrades (negative)
  Churned MRR: Cancelled customers (negative)
  Reactivation MRR: Win-backs (positive)

Net New MRR = New + Expansion + Reactivation - Contraction - Churn
```

### Net Revenue Retention (NRR)
```
NRR = (Beginning ARR + Expansion - Contraction - Churn) / Beginning ARR × 100

Target: > 110% (world-class: 120-140%)

Interpretation:
  < 80%:  Severe retention problem
  80-100%: Growing only through new logos
  100-110%: Healthy, existing base stable
  110-130%: Excellent, base growing organically
  > 130%: Exceptional (rare, often PLG + expansion)

Agency context:
  Target NRR 110-120% through scope expansion and tier upgrades
```

### Gross Revenue Retention (GRR)
```
GRR = (Beginning ARR - Contraction - Churn) / Beginning ARR × 100

Target: > 90% (cannot exceed 100% by definition)

Difference from NRR:
  GRR excludes expansion — pure retention measure
  If GRR < 85%: fix churn BEFORE investing in expansion
```

---

## Sales Efficiency Metrics

### Magic Number
```
Magic Number = (Net New ARR this quarter - Net New ARR prior quarter) × 4 / S&M Spend (prior quarter)

Annualized formula: normalizes quarterly growth to annual rate for comparison.

Interpretation:
  > 0.75: Efficient — invest more aggressively
  0.5-0.75: Acceptable — optimize before scaling
  0.25-0.5: Inefficient — fix unit economics before scaling
  < 0.25: Broken — stop scaling, diagnose fundamentals
```

### Sales Velocity
```
Sales Velocity = (Opportunities × Win Rate × ACV) / Sales Cycle Length (days)

Example:
  50 opportunities × 25% win rate × R$60K ACV / 90 days
  = R$750K / 90 = R$8,333 per day

Levers to improve:
  1. More opportunities (pipeline generation)
  2. Higher win rate (sales enablement)
  3. Larger deal size (offer design, upsell)
  4. Shorter cycle (process optimization)
```

### Pipeline Coverage
```
Pipeline Coverage = Total Weighted Pipeline / Quota

Target: 3-5x coverage

Example:
  Quota: R$500K
  Pipeline: R$2M weighted
  Coverage: 4x ✓

If coverage < 3x: Pipeline generation is the bottleneck
If coverage > 5x: May indicate poor qualification (bloated pipeline)
```

---

## Revenue Leak Analysis (Clari Framework)

### Six Categories of Revenue Leaks
| Leak Category | Description | Typical Loss | Detection |
|--------------|-------------|-------------|-----------|
| **Pipeline Leaks** | Deals slipping, going dark, or dying | 3-5% of pipeline | CRM stage aging analysis |
| **Pricing Leaks** | Excessive discounting, poor negotiation | 2-4% of revenue | Discount analysis vs list price |
| **Contracting Leaks** | Scope creep, unfavorable terms | 1-3% of margin | Contract vs proposal comparison |
| **Expansion Leaks** | Missed upsell/cross-sell opportunities | 3-5% of base ARR | Health score vs expansion rate |
| **Churn Leaks** | Preventable churn, save-play failures | 2-5% of ARR | Churn reason analysis |
| **Velocity Leaks** | Slow cycles reducing time-value of money | 1-2% of revenue | Cycle time vs benchmark |

### Total Revenue Leak
```
Industry average: ~14.9% revenue leaked (Clari research)

Revenue Leak Assessment:
  Gross Revenue: R$ __________
  Pipeline Leaks: - R$ __________ (__)%
  Pricing Leaks: - R$ __________ (__)%
  Contracting Leaks: - R$ __________ (__)%
  Expansion Leaks: - R$ __________ (__)%
  Churn Leaks: - R$ __________ (__)%
  Velocity Leaks: - R$ __________ (__)%
  ─────────────────────────────────
  Total Leakage: - R$ __________ (__)%
  Recoverable Revenue: R$ __________ (__)%
```

---

## Revenue Architecture Models

### Bow Tie Funnel (Jacco van der Kooij)
```
Traditional Funnel (one-way):
  Awareness → Interest → Decision → Purchase → END

Bow Tie Funnel (full lifecycle):
  LEFT SIDE (Acquisition):
    Awareness → Education → Selection → Purchase

  CENTER (Land):
    Contract signed — the "knot" of the bow tie

  RIGHT SIDE (Expansion):
    Onboarding → Adoption → Expansion → Advocacy

Key insight: Revenue doesn't stop at "Purchase" — the right side
of the bow tie (retention + expansion) is where most revenue lives
for recurring business models.
```

### Predictable Revenue Model (Aaron Ross)
```
Three specialized roles:
  1. SDR (Sales Development Rep): Outbound prospecting
  2. AE (Account Executive): Closing deals
  3. CSM (Customer Success Manager): Retention + expansion

Pipeline sources:
  Seeds: Referrals, word-of-mouth (highest conversion)
  Nets: Inbound marketing (medium conversion)
  Spears: Outbound prospecting (lowest conversion, most scalable)

Key principle: Separate prospecting from closing.
Never have closers doing their own prospecting.
```

### Sales Acceleration Formula (Mark Roberge)
```
Four formulas:
  1. Hiring Formula: Traits that predict success → scorecard-based hiring
  2. Training Formula: Methodology-based onboarding → predictable ramp
  3. Management Formula: Metrics-driven coaching → consistent performance
  4. Demand Gen Formula: Content-led inbound → scalable pipeline

Revenue = Headcount × Ramp × Quota × Attainment × ACV
```

---

## Forecasting Models

### Weighted Pipeline Forecast
```
For each deal:
  Weighted Value = Deal Value × Stage Probability

Stage Probabilities (typical):
  Discovery: 10%
  Qualification: 20%
  Solution Design: 40%
  Proposal: 60%
  Negotiation: 80%
  Verbal Commit: 90%

Total Forecast = Sum of all weighted values
```

### Three-Scenario Forecast
```
Conservative (60% confidence):
  Only committed deals + historical minimum new

Base (50% confidence):
  Committed + weighted pipeline + trend extrapolation

Optimistic (30% confidence):
  Base + upside deals + expansion potential

Report all three. Manage to base, plan resources for conservative.
```

## References
- Van der Kooij, J. — *Revenue Architecture* (Winning by Design)
- Ross, A. — *Predictable Revenue* (2011)
- Roberge, M. — *The Sales Acceleration Formula* (2015)
- Clari — Revenue Leak research (2023)
- Tunguz, T. & Blossom, F. — *Winning with Data* (SaaS benchmarks)
- SaaStr — Industry benchmark data
