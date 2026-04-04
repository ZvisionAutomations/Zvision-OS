# Discovery Methodology Playbook

## Purpose
Guia pratico de metodologias de discovery com instrucoes de quando e como usar cada metodo.

## Core Philosophy
Discovery is a continuous habit, not a phase. The goal is to reduce risk before investing in development by gathering evidence about user needs, market context, and solution viability.

## Method Selection Guide

### By Research Question Type
| Question | Best Methods | Sample Size |
|----------|-------------|-------------|
| "Do users have this problem?" | Problem interviews, support analysis | 5-8 interviews |
| "How do users solve this today?" | Contextual inquiry, diary study | 5-8 sessions |
| "Will users use this solution?" | Prototype test, smoke test | 5-8 users |
| "Which design works better?" | A/B test, usability test | 5-8 (usability) / 1000+ (A/B) |
| "How many users are affected?" | Analytics, survey | 50+ survey / full dataset |
| "What do users value most?" | MaxDiff, conjoint, interviews | 50+ (quantitative) |

### Method Quick Reference

**User Interviews (Generative)**
- When: Understanding problems, motivations, context
- Duration: 45-60 min per session
- Sample: 5-8 per segment
- Output: Insight cards, pattern analysis
- Key rule: No pitching, follow The Mom Test

**Usability Testing (Evaluative)**
- When: Testing if a design works
- Duration: 45-60 min per session
- Sample: 5 users find ~85% of issues (Nielsen)
- Output: Task success rates, finding cards
- Key rule: Test tasks, not features

**Surveys (Quantitative)**
- When: Validating qualitative findings at scale
- Duration: <5 min to complete
- Sample: 50+ for patterns, 200+ for significance
- Output: Statistical validation, segmentation
- Key rule: Never use alone (combine with qualitative)

**Analytics Analysis**
- When: Understanding behavior patterns
- Duration: Hours of analysis
- Sample: Full user base
- Output: Funnel analysis, cohort analysis, feature usage
- Key rule: Shows WHAT, not WHY (pair with interviews)

**Prototype Testing**
- When: Validating solution before development
- Duration: 30-60 min per session
- Sample: 5-8 users
- Output: Usability findings, design recommendations
- Key rule: Test the concept, not the polish

**A/B Experiment**
- When: Measuring causal impact of change
- Duration: 1-4 weeks (depends on traffic)
- Sample: Calculated per experiment (see formula)
- Output: Statistical result, learning card
- Key rule: No peeking before planned end date

## Triangulation Framework
Always use 2+ methods to validate important findings:
```
Qualitative (WHY) + Quantitative (HOW MANY) = Strong Evidence
Behavioral (WHAT THEY DO) + Attitudinal (WHAT THEY SAY) = Complete Picture
```

## Research Ethics
- Always get informed consent
- Protect participant privacy (no PII in reports)
- Compensate participants fairly
- Be honest about purpose of research
- Allow participants to stop at any time
- Never deceive participants about product intent

## Common Pitfalls
| Pitfall | Prevention |
|---------|-----------|
| Confirmation bias | Have someone else review findings |
| Leading questions | Pilot test interview guide |
| Small sample conclusions | State confidence levels honestly |
| Recency bias | Look at patterns, not individual stories |
| Survivorship bias | Include churned/inactive users |
| Selection bias | Recruit diverse participants |
