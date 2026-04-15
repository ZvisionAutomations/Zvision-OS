# Product Management Frameworks Reference

## Purpose
Referencia rapida dos frameworks de PM mais utilizados pela squad, com formulas, templates e quando usar cada um.

## Strategy Frameworks

### Geoffrey Moore Vision Template
```
FOR [target customer]
WHO [statement of need]
THE [product name] IS A [product category]
THAT [key benefit, reason to buy]
UNLIKE [primary competitive alternative]
OUR PRODUCT [primary differentiation]
```

### April Dunford 5 Components (Obviously Awesome)
1. Competitive Alternatives (what would they use?)
2. Unique Attributes (what do we have?)
3. Value (so what?)
4. Target Customer Characteristics (who cares?)
5. Market Category (what frame?)

### Strategy Canvas (Blue Ocean — Kim & Mauborgne)
- Plot 6-10 value factors on X axis
- Score each competitor 1-5 on Y axis
- ERRC Grid: Eliminate / Reduce / Raise / Create

### Opportunity Solution Tree (Teresa Torres)
```
Desired Outcome (metric)
├── Opportunity (user need)
│   ├── Solution A → Experiment
│   ├── Solution B → Experiment
│   └── Solution C → Experiment
└── Opportunity (user need)
    └── Solutions → Experiments
```

## Prioritization Frameworks

### RICE Scoring (Intercom)
```
RICE Score = (Reach × Impact × Confidence) / Effort

Reach: users/quarter (actual number)
Impact: 3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal
Confidence: 100%=high, 80%=medium, 50%=low
Effort: person-months
```

### MoSCoW
- **Must Have:** System fails without it
- **Should Have:** Important but not critical
- **Could Have:** Nice to have
- **Won't Have:** Explicitly out of scope

### Kano Model
- Must-Be: Expected (absence = dissatisfaction)
- One-Dimensional: More = better (linear satisfaction)
- Attractive: Surprise delight (absence ≠ dissatisfaction)
- Indifferent: No impact
- Reverse: Causes dissatisfaction

## Goal-Setting Frameworks

### OKRs (Doerr)
```
Objective: Qualitative, inspirational
  KR 1: [metric] from [X] to [Y]
  KR 2: [metric] from [X] to [Y]
  KR 3: [metric] from [X] to [Y]

Scoring: 0.0-1.0
  0.7 = target hit (aspirational)
  0.6-0.7 = healthy average
  >0.8 = not ambitious enough
  <0.4 = execution or target issues

Mix: 60-70% committed, 30-40% aspirational
```

## Discovery Frameworks

### Continuous Discovery Habits (Teresa Torres)
- Weekly touchpoints with users
- Product Trio (PM + Design + Engineering)
- Interview → Synthesize → Map → Test → Decide
- Opportunity Solution Tree as central artifact

### Jobs-to-Be-Done (Christensen/Moesta)
```
Job Statement: "When I [situation], I want to [motivation], so I can [outcome]"
Three layers: Functional / Emotional / Social
Switch Interview: Timeline → Forces → Decision → Outcomes
Four Forces: Push (current pain) + Pull (new solution) vs Habit + Anxiety
```

### The Mom Test (Rob Fitzpatrick)
1. Talk about their life, not your idea
2. Ask about specifics in the past, not generics about the future
3. Talk less, listen more
4. Never pitch

## Delivery Frameworks

### Shape Up (Ryan Singer)
- Fixed time, variable scope
- Appetite (how much time?) not Estimate (how long?)
- Betting Table instead of backlog grooming
- 6-week cycles + 2-week cooldown
- No carry-over by default

### Sprint Capacity Formula
```
Individual Capacity = Available Days × Focus Factor × Velocity Factor
Team Capacity = Sum(Individual Capacities)
Buffer = Team Capacity × 0.10
Committable = Team Capacity - Buffer
```

## Metrics Frameworks

### AARRR Pirate Metrics (Dave McClure)
Acquisition → Activation → Retention → Revenue → Referral

### Product Health Score (Composite)
```
Score = (Product Metrics × 0.30) + (Delivery × 0.25) + (Client × 0.25) + (Strategic × 0.20)
Bands: 80-100 GREEN | 60-79 YELLOW | 40-59 ORANGE | 0-39 RED
```

### Sean Ellis PMF Test
- Survey: "How would you feel if you could no longer use [product]?"
- >40% "Very Disappointed" = PMF achieved

## Client Management Frameworks

### Dual Roadmap System
- Internal: Full detail, sprint-level, technical
- Client-Facing: Outcomes, Now/Next/Later, confidence levels

### Rich Mironov Reframe
Client says feature → PM asks 5 questions → Finds underlying problem

## Reference Authors
| Author | Framework | Book/Source |
|--------|-----------|------------|
| Teresa Torres | Continuous Discovery | Continuous Discovery Habits |
| Marty Cagan | Empowered Teams | Inspired / Empowered |
| Ryan Singer | Shape Up | Shape Up (Basecamp) |
| April Dunford | Positioning | Obviously Awesome |
| Clayton Christensen | JTBD | Competing Against Luck |
| Bob Moesta | Switch Interview | Demand-Side Sales 101 |
| John Doerr | OKRs | Measure What Matters |
| Kim & Mauborgne | Blue Ocean | Blue Ocean Strategy |
| Sean Ellis | PMF Test | Hacking Growth |
| Rob Fitzpatrick | Customer Interviews | The Mom Test |
| Rich Mironov | Agency PM | The Art of Product Management |
| Wes Bush | PLG | Product-Led Growth |
| Martin Fowler | Tech Debt | Technical Debt Quadrant |
| Janna Bastow | Roadmapping | Now/Next/Later (ProdPad) |
