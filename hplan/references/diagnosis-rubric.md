# Harness Planning Diagnosis Rubric

## PM Thinking

Harness Planning should sound like a PM who has operated large consumer products and now teaches builders to avoid building the wrong thing quickly.

Core beliefs:

- The AI-era bottleneck is not code generation. It is market research, problem definition, first-user discovery, PMF measurement, and acquisition.
- "AI로 만들었는데 안 팔리는가?" is the opening diagnostic question.
- Teach tool usage only inside product decisions. Every UI, auth, billing, architecture, and agent choice should reveal PM thinking.
- Build one quality SaaS, not thirty shallow experiments.
- Keep message, product, demo, counter-position, and target pain aligned.

## Inputs

- `idea`: The product, service, AI agent, marketplace, or workflow the user wants to build.
- `target`: The first user who has enough urgency to spend time or money.
- `hypothesis`: Why the user is uncomfortable now.
- `alternatives`: What the user already uses to survive the problem.
- `features`: Proposed feature list or MVP candidates.
- `interview_notes`: Recent user quotes, observed behavior, payments, manual work, switching attempts, or objections.

## Evidence Quality

Strong evidence:

- A recent concrete moment: "last Tuesday I spent 3 hours..."
- Existing spend or workaround: tools, agencies, templates, manual labor, internal scripts.
- Repetition: the same pain happens weekly or monthly.
- Switching language: what would make them leave their current workaround.
- Loss language: time, money, risk, missed revenue, reputation, compliance, opportunity cost.

Weak evidence:

- "Sounds useful."
- "I would use this someday."
- Feature wishlists without a painful event.
- Broad persona labels without recent behavior.
- Founder intuition with no named alternative.

## 100-Point Rubric

| Category | Max | What Good Looks Like |
|---|---:|---|
| ICP specificity | 20 | Behavior, context, pressure, and who pays are clear |
| Recent painful event | 15 | A recent concrete episode exists |
| Current alternative/workaround | 15 | Current tools/manual workflows are named |
| Repetition/frequency | 10 | The problem repeats often enough to matter |
| Economic pain | 15 | Time, money, risk, or opportunity loss is visible |
| Switching trigger | 10 | There is a reason to leave the current workaround |
| MVP narrowness | 10 | One workflow, not a feature pile |
| Acquisition path to first 5 users | 5 | The first five reachable people/channels are named |

Decision:

- 75+ = build, only if interview/behavior evidence and economic pain exist.
- 55-74 = interview first.
- 35-54 = pivot.
- 34 or below = hold.

## Report Shape

Use this Markdown structure:

```markdown
# Harness Planning Diagnosis

## Input
- Idea:
- Target:
- Hypothesis:
- Alternatives:
- Features:

## Build Decision
Decision (score/100)

Reason.

## Hplan Operator Lens
- ...

## Problem Brief
- ...

## ICP
- ...

## JTBD
- When ..., I want ..., so I can ...

## JTBD to Agent Spec
- Agent job:
- Success metric:
- Guardrail:

## Interview Kit
- ...

## 5-Layer Metrics
- Sean Ellis:
- TTV:
- Override Rate:
- Frustration Index:
- Agentic PMF:

## 7-Day Validation Roadmap
- Day 1:

## 14-Day Validation Roadmap
- Week 2-1:

## 60-Day Stage Gate
- W1:
- W2:

## Next Actions
- ...
```

## Build Continuation

When the user wants to continue into implementation, add:

- `PRD seed`: goal, non-goals, primary workflow, data model, success metric.
- `AGENTS.md brief`: stack, commands, environment variables, architecture notes, verification commands.
- `MVP issue list`: 5 to 8 implementation tasks that preserve the narrow workflow.

## Representative Case Patterns

Use these when the user asks for examples or when a diagnosis is too abstract.

### AI meeting notes SaaS

Weak version: "AI summarizes meetings."

Stronger direction: freelancers and agencies do not pay for summaries alone. They may pay when meeting notes become proposal drafts, follow-up emails, CRM updates, or next-step artifacts.

Validation task: offer to manually convert two real meeting notes into a proposal/follow-up package and check whether users send it.

### Academy counseling automation

Weak version: "AI chatbot for academies."

Stronger direction: missed counseling follow-up creates registration loss. The workflow should summarize inquiry context, identify urgency, and schedule follow-up for the owner or manager.

Validation task: tag 10 real counseling logs manually and ask whether the owner would pay to reduce missed follow-ups.

### Notion template market

Weak version: "AI recommends Notion templates."

Stronger direction: users buy templates but fail to adapt them. The paid job may be concierge workspace setup, not template recommendation.

Validation task: manually fix one user's Notion workspace and check whether they use it for two weeks.
