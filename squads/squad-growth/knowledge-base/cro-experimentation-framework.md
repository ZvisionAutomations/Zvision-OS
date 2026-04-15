# Knowledge Base: CRO Experimentation Framework

## Experimentation Hierarchy

### 1. Observation → Hypothesis → Experiment → Learning
```
DATA SOURCES:
  Analytics → Heatmaps → Session Recordings → Surveys → User Tests
      │
      ▼
INSIGHT:
  "Users on mobile abandon cart at payment step (68% drop-off)"
      │
      ▼
HYPOTHESIS:
  "If we add Apple Pay to mobile checkout,
   then conversion rate will increase by 15%,
   because reducing payment friction addresses the #1 drop-off reason"
      │
      ▼
EXPERIMENT:
  A/B test: Control (current) vs Variant (Apple Pay added)
  Sample: 5,000 users per variant, 14-day duration
      │
      ▼
LEARNING:
  Result + next hypothesis → Knowledge Base
```

## Hypothesis Framework

### ICE Scoring
```
Score = Impact × Confidence × Ease (each 1-10)

Impact:     How much will this move the metric? (1=minimal, 10=massive)
Confidence: How sure are we this will work? (1=guess, 10=proven)
Ease:       How easy is it to implement? (1=months, 10=hours)
```

### RICE Scoring (for larger teams)
```
Score = (Reach × Impact × Confidence) / Effort

Reach:      Users affected per quarter
Impact:     0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive)
Confidence: 100% (high), 80% (medium), 50% (low)
Effort:     Person-weeks to implement
```

### Hypothesis Template
```
HYPOTHESIS #[ID]
  Page/Flow: [where]
  Observation: [what we see in data]
  If we: [change we will make]
  Then: [expected result + metric + magnitude]
  Because: [psychological/behavioral reasoning]
  ICE Score: I[_] × C[_] × E[_] = [total]
  Primary Metric: [conversion rate, revenue, etc.]
  Secondary Metrics: [engagement, bounce, etc.]
  Guard Rails: [metrics that should NOT decrease]
```

## Statistical Foundations

### Sample Size Calculation
```
n = (Z² × p × (1-p)) / E²

Where:
  Z = Z-score (1.96 for 95% confidence)
  p = baseline conversion rate
  E = minimum detectable effect (MDE)

Practical formula:
  n per variant = 16 × p × (1-p) / MDE²

Example:
  Baseline CR = 3% (p = 0.03)
  MDE = 15% relative (0.45% absolute)
  n = 16 × 0.03 × 0.97 / 0.0045² ≈ 22,963 per variant
```

### Statistical Significance
| Concept | Threshold | Meaning |
|---------|----------|---------|
| Confidence level | 95% (α = 0.05) | 5% chance of false positive |
| Statistical power | 80% (β = 0.20) | 20% chance of false negative |
| p-value | < 0.05 | Reject null hypothesis |
| MDE | 10-20% relative | Minimum meaningful change |

### Common Pitfalls
| Pitfall | Problem | Prevention |
|---------|---------|-----------|
| Peeking | Checking results too early | Pre-set duration, use sequential testing |
| Multiple testing | Testing many variants inflates false positives | Bonferroni correction |
| Simpson's Paradox | Aggregate hides segment-level effects | Always segment results |
| Novelty effect | Users react to newness, not improvement | Run for 2+ weeks |
| Selection bias | Non-random assignment | Use proper randomization |
| Survivorship bias | Only analyzing completers | Intent-to-treat analysis |

## Test Types

### A/B Test
- **What:** Two variants (control vs treatment)
- **When:** Clear hypothesis, one variable change
- **Duration:** Until statistical significance
- **Traffic:** 50/50 split

### A/B/n Test
- **What:** Multiple variants (3-5 max)
- **When:** Testing different approaches
- **Caution:** Need more traffic (sample size per variant)

### Multivariate Test (MVT)
- **What:** Multiple elements changed simultaneously
- **When:** Optimizing combinations (headline × image × CTA)
- **Requirement:** Very high traffic volume

### Split URL Test
- **What:** Different pages/URLs entirely
- **When:** Major redesigns, different flows
- **Implementation:** Server-side redirect

### Bandit Testing
- **What:** Dynamically allocates more traffic to winning variant
- **When:** Short campaigns, e-commerce promotions
- **Trade-off:** Less statistical rigor, more revenue

## CRO Audit Framework

### Quantitative Analysis
| Source | What to Look For |
|--------|-----------------|
| GA4 Funnel | Drop-off points per stage |
| GA4 Path | Common user paths vs ideal path |
| Heatmaps | Click distribution, scroll depth |
| Session Recordings | Rage clicks, u-turns, confusion |
| Form Analytics | Field-level abandonment |
| Speed Metrics | LCP, INP correlation with conversion |

### Qualitative Analysis
| Method | What to Learn |
|--------|-------------|
| User surveys | Why did you not complete X? |
| Exit surveys | What stopped you today? |
| User tests | Task completion observation |
| Customer interviews | Deep understanding of barriers |
| Support tickets | Common complaints and confusion |
| Review mining | Competitor reviews for friction insights |

### Heuristic Evaluation (LIFT Model)
| Factor | Question | Priority |
|--------|---------|----------|
| Value proposition | Is the value clear and compelling? | Highest |
| Relevance | Does this match what brought the user here? | High |
| Clarity | Is the message/action crystal clear? | High |
| Urgency | Is there reason to act now? | Medium |
| Anxiety | Are there trust/security concerns? | Medium |
| Distraction | Are there competing actions/elements? | Medium |

## Experiment Lifecycle

### 1. Discovery (Week 1)
- Review analytics data
- Conduct heuristic evaluation
- Prioritize opportunities

### 2. Hypothesis (Week 2)
- Write formal hypotheses
- Score with ICE/RICE
- Select top 2-3 for sprint

### 3. Design (Week 2-3)
- Create mockups/wireframes
- Get stakeholder alignment
- Technical feasibility check

### 4. Implementation (Week 3-4)
- Build variants in testing tool
- QA across devices/browsers
- Validate tracking

### 5. Execution (Week 4-6+)
- Launch experiment
- Monitor for data quality issues
- DO NOT peek at results

### 6. Analysis (End of test)
- Statistical significance check
- Segment analysis
- Revenue impact calculation

### 7. Documentation (Post-test)
- Record in experiment knowledge base
- Share learnings
- Generate next hypotheses

## Tools Reference
| Category | Tools |
|----------|-------|
| A/B Testing | Optimizely, VWO, Google Optimize (sunset), AB Tasty |
| Heatmaps | Hotjar, FullStory, Microsoft Clarity (free) |
| Surveys | Hotjar, Typeform, SurveyMonkey |
| Analytics | GA4, Amplitude, Mixpanel |
| Session Recording | FullStory, Hotjar, LogRocket |
| Statistical | Evan Miller calculator, AB Test Guide, Statsig |
