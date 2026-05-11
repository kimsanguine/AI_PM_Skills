# Product Planning Gate

Use this reference after market and interview evidence exist.

## Required Outputs

- Problem Brief
- User Journey Map
- Sitemap
- Opportunity Solution Tree or Hypothesis Tree
- Core differentiation / wedge
- Productive outcome / MPO
- Proceed / Pivot / Hold criteria
- Inputs for Agent Spec or workflow spec
- Human Product Checkpoint

## Problem Brief

Use this compact shape:

```markdown
## Problem Brief

- User:
- Situation:
- Current workaround:
- Pain:
- Economic consequence:
- Switching trigger:
- Productive outcome:
- MVP boundary:
- Evidence:
```

The Problem Brief must use evidence from competitor research or interviews. If the evidence is missing, mark it as missing instead of inventing confidence.

## Do Not

- Do not write a PRD seed before the Problem Brief, primary ICP/JTBD, user journey map, sitemap, and design direction are approved.
- Do not turn every interview request into scope. Map requests to opportunities first, then choose the smallest productive outcome.
- Do not define the MVP as a list of screens. Define the paid outcome, review step, failure state, and usage boundary.
- Do not create a sitemap after implementation as documentation cleanup. It is a pre-build artifact.
- Do not create a user journey map that only shows happy paths. Include blocked, failed, review, payment, and return moments.
- Do not convert JTBD into an Agent Spec unless the job is narrow enough for an agent to ask questions, produce output, and be evaluated.
- Do not hide tradeoffs. Every Product Gate should name what is intentionally excluded from the first build.

## User Journey Map

Required before implementation.

Use this table:

| Stage | User question | User action | Product response | Success signal | UX risk |
|---|---|---|---|---|---|

The journey must include:

- Arrival or acquisition context
- First value moment
- Core workflow
- Review / override / trust step if AI is involved
- Payment or usage limit moment if monetized
- Failure or blocked state
- Return / repeat-use moment

## Sitemap

Required before implementation.

Use this compact structure:

```text
/
├── Home / positioning
├── Core workflow
├── Result / report / output
├── Pricing or upgrade path
├── Account / project history if needed
└── Legal / support / settings if needed
```

Include API routes only when the product already needs backend behavior.

## OST / Hypothesis Tree

Start from outcome, not features.

Use:

- Outcome
- Opportunities from interviews
- Solution candidates
- Assumptions
- Tests
- Decision criteria

Hypothesis tree must include market, product, revenue, and operational hypotheses when relevant.

## Productive Outcome / MPO

For AI agent or workflow products, define the Minimum Productive Outcome before writing PRD.

Use:

```markdown
## MPO

- User starts with:
- Product must complete:
- User-visible proof of completion:
- Quality bar:
- Human review step:
- Paid outcome boundary:
- Failure state:
```

The MPO is stronger than "MVP feature exists." It asks whether the product completes a user outcome.

## JTBD To Agent Spec

Convert JTBD into an Agent Spec only after human approval.

Use:

| JTBD | Agent job | Questions agent asks | Output | Success metric | Human review |
|---|---|---|---|---|---|
| When..., I want..., so I can... |  |  |  |  |  |

Do not build an agent around a vague job. If the JTBD cannot become a clear agent job, return to interviews.

## Proceed / Pivot / Hold Criteria

Use this table:

| Decision | Criteria | Next action |
|---|---|---|
| Proceed | Evidence and economics support one narrow workflow | Build Gate |
| Pivot ICP | Same problem, different buyer or segment | Rewrite ICP/JTBD |
| Pivot Product | Same segment, different job or workflow | Rewrite outcome |
| Pivot Pricing | Pain exists but price/COGS/allowance breaks | Rework economics |
| Hold | Weak evidence and weak economics | Stop implementation |

## Human Product Checkpoint

Before Build Gate, ask the human to approve:

- Problem Brief
- Primary ICP/JTBD
- MPO
- Journey map
- Sitemap
- Design direction
- OST/Hypothesis Tree
- Proceed / Pivot / Hold decision

If the human rejects or changes the problem definition, update the Product Gate artifacts before drafting PRD seed or AGENTS.md.

## Build Gate Input

Only pass to Build Gate when these are present:

- Narrow productive outcome
- Primary ICP and JTBD
- User journey map
- Sitemap
- Design direction
- COGS risk list
- Acceptance criteria candidate
