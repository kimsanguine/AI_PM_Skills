# ICP And Interview Gate

Use this reference for persona, ICP, JTBD, user interview design, and evidence tagging.

## Required Outputs

- ICP candidates, 3 options
- Persona / ICP card for the selected segment
- JTBD statements, 5 options
- Anti-pattern removal checklist
- Priority JTBD
- Screener questions
- Switch Interview guide
- Interview recruiting plan
- Interview Snapshot template
- Evidence table with Strong / Medium / Weak signals
- Human interview review checkpoint

## Persona / ICP Rules

Do not define persona by demographics alone.

Each ICP card must include:

- Who
- Situation
- Push
- Pull
- Habit
- Anxiety
- Current alternative
- Buying trigger
- Success outcome
- Exclusion criteria

Good ICP:

> Small team operators who handled at least 5 repeated handoff tasks in the last 30 days and currently patch the workflow with spreadsheets, templates, and manual checks.

Weak ICP:

> Busy professionals in their 20s and 30s.

## Do Not

- Do not write "users," "creators," "PMs," "small businesses," or "busy professionals" as the final ICP without a repeated behavior and buying trigger.
- Do not count demographic similarity as segment proof. Segment by situation, current workaround, frequency, and economic pain.
- Do not ask hypothetical questions such as "Would you use this?" or "Would you pay?"
- Do not treat compliments, advice, feature requests, or waitlist signups as strong evidence.
- Do not let AI interview summaries replace human review of quotes, pauses, contradictions, and switching language.
- Do not merge multiple ICPs into one persona card because the product idea sounds broad.
- Do not proceed to Product Gate when interview signals split across unrelated jobs.

## JTBD Rules

Use the form:

> When [situation], I want [motivation or job], so I can [measurable outcome].

Reject these anti-patterns:

- Solution-loaded: names the tool or feature instead of the job
- Too broad: "grow my business"
- Too small: "click the button"
- Demographic mixing: describes age/title instead of situation
- Wishlist: "I want a dashboard"

## Switch Interview

Never ask "Would you use this?"

Ask about:

- The last time the problem happened
- What triggered the search for a better solution
- What they used instead
- What made that workaround painful
- What they paid in money, time, risk, or reputation
- What would make them switch
- What they can test next week
- What made today the day they looked for or accepted a different solution

## Human + AI Interview Rule

Use AI to assist discovery, not replace discovery.

The human should personally conduct or listen to at least 5 interviews when possible. AI can transcribe, summarize, cluster, and tag signals, but the human must review quotes and evidence strength before the Product Gate.

Allowed:

- AI drafts interview questions
- AI cleans transcripts
- AI extracts quotes and JTBD signals
- AI clusters opportunities
- AI proposes evidence strength

Blocked:

- Treating AI summary alone as strong evidence
- Letting AI conduct all interviews without human review
- Counting compliments, future intent, or feature requests as strong signals
- Advancing to PRD because "interviews sounded positive"

## Interview Recruiting Plan

Require a plan for at least 50 candidates and 5 interviews.

Use this table:

| Channel | Candidate count | Search method | First message |
|---|---:|---|---|

The first message must say this is a research interview about recent workflow behavior, not product promotion.

For B2B products, include multiple stakeholders when relevant:

- User
- Buyer / budget owner
- Admin, IT, security, or legal reviewer
- Operations or support owner

If these roles differ and only one is interviewed, mark the evidence as incomplete.

## Interview Snapshot Template

```markdown
## Interview Snapshot

- Participant:
- Segment:
- Recent event:
- Current alternative:
- Frequency:
- Time or money spent:
- Existing spend:

### Push
- Trigger:
- Painful moment:

### Pull
- Desired outcome:
- What would feel better:

### Habit
- Current workflow:
- What is hard to change:

### Anxiety
- Risk or concern:
- Buying condition:

### Buying Signal
- Source/data offered:
- Preorder/payment/strong commitment:
- Signal: Strong / Medium / Weak

### Product Opportunity
- Opportunity 1:
- Opportunity 2:
- Opportunity 3:
```

## Evidence Strength

| Signal | Strong | Medium | Weak |
|---|---|---|---|
| Recency | Last 2 weeks or last 30 days | Last 1-2 months | Hypothetical or vague |
| Current alternative | Paid tool, agency, internal workflow, manual process | Free workaround with large time cost | No workaround |
| Frequency | Weekly or repeated | Monthly | One-off |
| Economic pain | Money, revenue, risk, compliance, missed opportunity | Time loss only | Mild annoyance |
| Switching | Names a condition to switch | Curious after demo | "Sounds useful" |
| Commitment | Payment, preorder, source/data, intro to buyer | Waitlist or interview | Compliment |

## Gate Decision

- 5 interviews with 3 repeated Strong signals: proceed to Product Gate.
- Problem is plausible but signals are thin: `interview`.
- Strong pain but different segment or job emerges: `pivot`.
- No recent behavior, alternative, or economic pain: `hold`.

## Pattern Limits

- 5 interviews can show a pattern; they cannot prove PMF.
- If 3 of 5 people in the same ICP mention the same Push and current workaround, continue.
- If 0-1 of 5 mention a real Push, pivot or hold.
- If signals split across multiple ICPs, narrow to one ICP and recruit again.
- Quantitative PMF claims need a larger sample and segmentation.

## Human Review Checkpoint

Before Product Gate, ask the human to approve:

- Selected ICP
- Priority JTBD
- Evidence strength tags
- Quotes that best represent the pain
- Whether to proceed, interview more, pivot, or hold
