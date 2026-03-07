---
name: biz-model
description: "Design a sustainable business model for AI agent products — pricing strategy (per-use, subscription, outcome-based), cost structure, unit economics, and value capture. Use when planning agent monetization, evaluating pricing models, or building a business case for agent development."
argument-hint: "[agent product to model]"
---

# Agent Business Model

> AI 에이전트 제품의 비즈니스 모델 설계

## 개념

에이전트 제품은 전통적 SaaS와 다른 비용 구조(사용량 기반)를 가진다. 가치 창출(value creation)과 가치 포획(value capture)을 분리해서 설계해야 한다.

## Instructions

You are designing a **business model** for an AI agent product: **$ARGUMENTS**

### Step 1 — Value Creation Analysis

Define the value the agent creates:
```
Time Saved: [hours/week] × [hourly cost] = [$/week]
Error Reduction: [error rate before] → [after] × [cost per error]
New Capability: [what was impossible before]
Scale Factor: [1 person can now do X people's work]
```

### Step 2 — Cost Structure

Map the variable cost elements:
| Cost Element | Unit | Estimated Cost | Scaling Behavior |
|-------------|------|----------------|-----------------|
| LLM API calls | per execution | $ | Linear with usage |
| External APIs | per call | $ | Linear |
| Compute/hosting | per month | $ | Step function |
| Human review | per edge case | $ | Decreasing over time |
| Data storage | per GB/month | $ | Linear |

**Key Metric**: Cost Per Execution (CPE) = Total cost ÷ Number of executions

### Step 3 — Pricing Model Selection

| Model | Best When | Risk |
|-------|-----------|------|
| **Per-execution** | Clear, countable outputs | Usage anxiety |
| **Tiered subscription** | Predictable usage patterns | Over/under provisioning |
| **Outcome-based** | Measurable business outcome | Attribution difficulty |
| **Seat-based + usage** | Team tool with variable intensity | Complexity |
| **Freemium** | Network effects, viral potential | Conversion rate |

### Step 4 — Unit Economics

Calculate the fundamental economics:
```
Revenue per Customer (monthly): $___
Cost per Customer (monthly):
  - LLM costs: $___
  - Infrastructure: $___
  - Support: $___
  - CAC amortized: $___
Gross Margin: ___%
Target Gross Margin: >70% (SaaS standard)
```

### Step 5 — Value Capture Strategy

Answer: "How much of the value created can you capture?"
- **Rule of thumb**: Charge 10-20% of value created
- **Anchor**: Compare to the cost of the human equivalent
- **Ceiling**: What alternatives exist? (competing agents, manual process, outsourcing)

### Step 6 — Moat Assessment

How defensible is this business model?
- Data moat: Does usage improve the product?
- Switching cost: How hard is it to leave?
- Network effect: Does more users = more value?
- See: `/agent-moat` for detailed moat analysis

### Output Format

Present as a Business Model Canvas adapted for agents:
```
┌─────────────────────────────────────────┐
│ Value Proposition: [what + for whom]     │
├──────────────┬──────────────────────────┤
│ Cost Structure│ Revenue Model            │
│ CPE: $___    │ Pricing: ___             │
│ Fixed: $___  │ Target ACV: $___         │
│ Margin: ___%  │ Payback: ___ months      │
└──────────────┴──────────────────────────┘
```

---

## Further Reading
- Alexander Osterwalder, *Business Model Generation* — Business Model Canvas
- Ash Maurya, *Running Lean* — Lean Canvas for startups
