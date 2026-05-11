# Human In The Loop Flow

Use this reference on every hplan run. hplan is not an autopilot PRD generator. It is a decision support skill that keeps the human responsible for market judgment, interview learning, product taste, cost risk, and build approval.

## Core Principle

AI can search, summarize, cluster, draft, score, and propose. The human must approve the interpretation before the next gate.

Never advance from Evidence Gate to Product Gate or from Product Gate to Build Gate without a visible human checkpoint.

## Do Not

- Do not treat human-in-the-loop as a final approval checkbox after the agent has already decided.
- Do not ask the human vague open-ended questions when a narrow gate decision is needed.
- Do not advance when the human has not approved the competitor set, evidence strength, problem definition, design direction, COGS, and build status.
- Do not let AI optimism override unresolved cost, privacy, rights, or policy blockers.
- Do not bury disagreement. If the human rejects or changes the synthesis, record the change and update the artifacts.
- Do not use AI-conducted interviews as strong evidence unless the human reviews transcripts, quotes, and source context.
- Do not collapse `WAITING_FOR_HUMAN`, `NEEDS_MORE_EVIDENCE`, and `APPROVED_BY_HUMAN` into one generic status.

## What The Human Must Own

The human owns:

- Target market choice
- Competitor set acceptance
- Interview recruiting and at least 5 real customer conversations or equivalent strong behavior evidence
- Evidence strength judgment
- Problem definition
- Primary ICP/JTBD selection
- Journey map and sitemap acceptance
- Design direction and taste bar
- COGS assumptions, usage caps, and gross margin risk
- Privacy/rights policy judgment
- Build / interview / pivot / hold decision

AI may assist with all of the above, but should not silently decide them.

## Human Checkpoint Format

At every checkpoint, output this block:

```markdown
## Human Checkpoint: [Gate Name]

Decision needed:

Recommended decision:

Options:
- A. 
- B. 
- C. 

Evidence:
- Strong:
- Medium:
- Weak:

Main risk:

If you choose A, next step:
If you choose B, next step:
If you choose C, next step:
```

Keep checkpoint options concrete. Do not ask broad questions like "What do you want to do?" Ask for a narrow decision.

## Gate 0. Intake Checkpoint

Before starting research, clarify:

- Product idea in one sentence
- Target user guess
- Paid outcome guess
- Market or country focus
- Known competitors or alternatives
- Constraints: time, budget, stack, data/privacy, launch deadline

If the user gives too little input, produce an Assumption Board and ask the human to confirm or correct it.

## Gate 1. Evidence Checkpoint

After market and competitor research, the human must approve:

- Competitor / alternative list
- Market vacuum
- "What not to build"
- Counter position
- Interview target segment
- Interview kit

Do not treat AI market synthesis as user evidence. It only creates research hypotheses.

### Interview HITL Rule

The human should personally conduct or listen to at least 5 interviews when possible. AI can transcribe and summarize, but the human must review salient quotes and update the evidence table.

Allowed AI assistance:

- Recruiting list draft
- Interview script
- Transcript cleanup
- Quote extraction
- Signal tagging
- Opportunity clustering

Not allowed:

- Fully outsourcing all customer learning to AI interviews without human review
- Using AI summary alone as strong evidence
- Treating compliments, future intent, or feature wishlists as build-ready

## Gate 2. Product Checkpoint

After evidence synthesis, the human must approve:

- Problem Brief
- Primary ICP/JTBD
- User Journey Map
- Sitemap
- Design direction
- OST or Hypothesis Tree
- Productive outcome / MPO

If the human disagrees with the synthesis, return to evidence. Do not paper over disagreement with a polished PRD.

## Gate 3. Build Checkpoint

Before PRD seed, AGENTS.md brief, architecture, or scaffold:

- COGS and gross margin risk must be reviewed
- Usage and payment boundaries must be reviewed
- Privacy/rights policy must be reviewed
- Latency/quality benchmark must be reviewed when relevant
- Implementation readiness must be reviewed

If any blocker is unresolved, output `CONDITIONAL_GO`, `interview`, `pivot`, or `hold`.

## Spec Driven HITL Flow

When implementation becomes appropriate, use human approval gates:

```text
Problem Brief
  -> review-problem gate, human approve
PRD seed / Spec
  -> review-spec gate, human approve
Plan / Architecture
  -> review-plan gate, human approve
Tasks
  -> review-tasks gate, human approve
Implementation
  -> review-implementation gate, human inspect
Launch
  -> review-metrics gate, human decide proceed/pivot/hold
```

If approval is missing, stop with `WAITING_FOR_HUMAN` and list the smallest decision needed.

## Evidence Pattern Rules

Use these as decision aids:

- 5 interviews can reveal a repeated pattern, not prove PMF.
- 5 interviews with 3 repeated strong Push signals can justify Product Gate.
- 5 interviews with 0 repeated Push signals should trigger pivot or hold.
- PMF score needs a larger sample; do not claim PMF from 5 interviews.
- For B2B, interview user, buyer, admin/security, and operations stakeholders when relevant.

## Output States

Use these HITL states:

- `READY_FOR_HUMAN_REVIEW`
- `WAITING_FOR_HUMAN`
- `APPROVED_BY_HUMAN`
- `REJECTED_BY_HUMAN`
- `NEEDS_MORE_EVIDENCE`
- `SAFE_TO_DRAFT_NEXT_GATE`

## Trace Artifacts

Preserve decision history:

- `docs/HITL_FLOW.md`: accepted human checkpoint plan and approval rules
- `docs/DECISION_LOG.md`: dated decisions and reversals
- `harness/reports/`: generated gate reports
- `harness/evidence/`: interview snapshots and evidence notes
- `review/`: final human/agent review checklists
