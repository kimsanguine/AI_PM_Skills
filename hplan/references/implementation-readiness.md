# Implementation Readiness Gate

Use this reference when moving from planning into implementation. It generalizes product implementation gates for AI, SaaS, media, data, workflow, and marketplace products.

## Required Outputs

- Implementation status: `GO`, `CONDITIONAL_GO`, `HOLD`, or `NO_GO`
- Technical architecture boundary
- Core services and what each service does not do
- Data model sketch
- API endpoint list
- Job states and failure states
- Transaction rules
- Rights / source / data policy
- Latency / quality benchmark plan when speed, live behavior, or provider quality matters
- Review-ready public page checklist
- Implementation order
- Human approval gates
- Go / No-Go gate

## Implementation Status

Use this language:

- `GO`: evidence, product, economics, policy, architecture, and tests are ready.
- `CONDITIONAL_GO`: implementation can start only on narrow blockers or prototype paths.
- `HOLD`: missing blocker prevents responsible implementation.
- `NO_GO`: product should not be implemented in current shape.

Never call a product `GO` when COGS, usage limits, rights/policy, or payment state are unresolved.
Never call a speed-sensitive product `GO` when latency, quality, fallback, and privacy/consent paths are unmeasured.
Never call a product `GO` when the human has not approved the Problem Brief, PRD/spec, implementation plan, task list, and launch metric gate.

## Do Not

- Do not start implementation because the PRD looks polished. Gate status, evidence, economics, and human approval matter more than document polish.
- Do not create implementation-heavy folders, services, or app shells when the product is still in Evidence Gate.
- Do not add paid workflows before billing status, usage enforcement, idempotent webhooks, and failure states are defined.
- Do not process user data, private documents, media, contacts, scraped content, or customer records before rights, consent, retention, deletion, and takedown rules exist.
- Do not let UI code trigger expensive jobs directly without auth, policy, usage, and queue boundaries.
- Do not mark a feature complete if blocked, failed, usage-limited, review-required, payment-required, and policy-blocked states are missing.
- Do not skip review-ready public pages for paid or data-handling launches.

## Architecture Boundary

Define each service and its non-responsibilities.

Use this table:

| Service | Owns | Does not own |
|---|---|---|

Important boundaries:

- UI starts workflows and shows state; it does not directly charge usage.
- API checks auth/plan and creates jobs; it does not run long jobs inline.
- Worker runs expensive/slow jobs; it does not decide billing status.
- Billing handler syncs provider status; it does not enforce usage.
- Usage meter enforces allowance; it does not act as the payment provider.
- COGS tracker records cost; it does not automatically change pricing.

## Job States

Every expensive or async workflow needs explicit states.

Use:

```text
input_created
→ processing_queued
→ processing_completed
→ user_reviewed
→ output_queued
→ output_succeeded
→ paid_outcome_succeeded
```

Define product-specific states and include failure states such as:

- `input_blocked`
- `policy_blocked`
- `usage_blocked`
- `schema_invalid`
- `processing_failed`
- `output_failed`
- `payment_required`

## Transaction Rules

Write transaction rules before implementation.

Include:

- Which event decrements allowance
- Which event records COGS
- Which event creates a retry
- Which event prevents job creation
- How webhook idempotency works
- How provider/internal status mismatch is reconciled

Default:

- Charge usage only after the paid outcome succeeds.
- Failed jobs record cost and failure reason but do not decrement customer allowance.
- Usage-blocked requests do not create expensive jobs.
- Payment webhooks update plan/status but do not directly mutate usage counters.

## Rights / Source / Data Policy

If users upload, import, process, publish, or transform content or data, define policy before build.

Required:

- Allowed inputs
- Disallowed inputs
- User confirmation copy
- Pre-action guardrails
- Output safety rules
- Deletion / retention policy
- Takedown or dispute flow when relevant
- Legal pages or policy links for public launch

Classify input policy:

| Policy class | Meaning | External provider use |
|---|---|---|
| `synthetic` | fake/demo/test data | allowed |
| `owned` | user owns or has rights | allowed after confirmation |
| `approved` | beta/customer explicitly approves test processing | allowed with record |
| `private` | confidential or not approved for external processing | blocked or local-only |

Policy-sensitive examples:

- Media source ownership
- Customer data or private documents
- Contact lists
- Financial or health data
- Third-party scraped content
- Generated content that may be published

## Review-Ready Public Pages

For paid products or products handling user data, define public trust pages before live checkout.

Required:

| Route | Purpose | Required content |
|---|---|---|
| `/` | Product landing | Product, pricing, policy, support |
| `/app` or product preview | Workflow preview | Core workflow, limits, account state |
| `/terms` | Terms | Scope, user responsibility, prohibited use, billing |
| `/privacy` | Privacy | Collected data, providers, retention, deletion |
| `/refund` or `/billing-policy` | Refund/cancel | Cancellation, refund, add-on policy |
| support/contact | Support | Email or contact path |

Payment review check:

- Pricing names the real usage unit.
- Policy-sensitive inputs are explained before checkout or import.
- Support email is visible.
- Checkout success URL and webhook URL are defined.
- Product can be understood without login.

## Performance / Quality Readiness

If the product promise includes fast, real-time, live, instant, immediate, high-accuracy, or provider-dependent output, define:

- Latency budget by artifact
- Maximum acceptable wait time
- Benchmark paths: text/input-only baseline, full processing path, live/incremental path if relevant
- Provider benchmark matrix
- Quality gates
- Fallback policy
- UX policy for waiting, partial results, uncertainty, and background work

Do not make the slowest artifact block the first useful artifact. Prefer staged results: first useful artifact, then richer artifact, then final export or report.

## Implementation Order

Use blocker-first order:

1. Core pipeline proof or workflow skeleton
2. Structured output/schema validation
3. Usage and policy enforcement
4. Billing/webhook mock tests
5. Latency / quality benchmark when speed or provider quality matters
6. COGS measurement
7. Alpha launch loop
8. Design-system-based UI polish
9. Public review pages and legal/trust surface

## Spec-Driven Human Approval Gates

Use these gates once implementation becomes appropriate:

| Gate | Human reviews | Output state |
|---|---|---|
| `review-problem` | Problem Brief, ICP/JTBD, MPO | `APPROVED_BY_HUMAN` or `NEEDS_MORE_EVIDENCE` |
| `review-spec` | PRD seed, Agent Spec, acceptance criteria | `APPROVED_BY_HUMAN` or `WAITING_FOR_HUMAN` |
| `review-plan` | Architecture, data model, policy, COGS, benchmark plan | `APPROVED_BY_HUMAN` or `CONDITIONAL_GO` |
| `review-tasks` | Task list, sequencing, test matrix | `APPROVED_BY_HUMAN` or `REWORK_TASKS` |
| `review-implementation` | Working product, visible states, cost/policy enforcement | `GO`, `CONDITIONAL_GO`, or `NO_GO` |
| `review-metrics` | First users, activation, quality, revenue, cost | `PROCEED`, `PIVOT`, or `HOLD` |

If a gate is missing approval, stop and output the smallest concrete decision needed.

## Human Override Rule

If AI confidence and human judgment conflict, record the conflict in `docs/DECISION_LOG.md`.

Default:

- Human can override AI only with a written reason.
- AI can challenge human optimism when evidence is weak, but should not silently advance.
- If cost, privacy, or policy risk is unresolved, the safest state is `CONDITIONAL_GO` or `HOLD`.

## Go / No-Go Gate

| Gate | Proceed | Pivot | Hold / Kill |
|---|---|---|---|
| Product | Users complete the MPO | Heavy override or quality issue | Users do not provide inputs/source/data |
| Revenue | Paid signal exists | Price/allowance needs adjustment | No payment behavior |
| COGS | Unit cost within target | Cost near limit | Cost breaks margin |
| Ops | Failure rate acceptable | Queue/retry needs work | Stable output not possible |
| Policy | User rights/data flow is clear | Needs legal copy refinement | Policy risk blocks launch |
| Performance | SLA and quality gates pass | Needs routing/fallback/staged UX | Product promise is not credible |

If any gate is missing, output `CONDITIONAL_GO` with blockers instead of a clean build recommendation.
