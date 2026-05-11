# Competitive Landscape: Superpowers, GStack, hplan

This reference is for positioning hplan against adjacent agent skill/workflow systems. It is not part of the normal product gate unless the user asks about hplan's own strategy.

Last reviewed: 2026-05-11

## Sources

| Product | Source | Notes |
|---|---|---|
| Superpowers | https://github.com/obra/superpowers | Primary GitHub README. Describes Superpowers as a software development methodology for coding agents, with composable skills, planning, TDD, review, and verification. |
| Superpowers Marketplace | https://github.com/obra/superpowers-marketplace | Marketplace listing. Describes core plugin, commands, skills search, and session-start context injection. |
| GStack site | https://gstack.lol/ | Official-looking product site. Describes GStack as an ordered workflow for Claude Code, Codex, and compatible agents. |
| GStack GitHub | https://github.com/garrytan/gstack | Primary repository. Describes roles, setup, supported hosts, and skill list. |

Counts such as number of skills, specialists, stars, forks, and commands are version-sensitive. Verify current numbers before using them in public-facing copy.

## One-Line Positioning

| System | Best short description | Main center of gravity |
|---|---|---|
| Superpowers | A disciplined software development methodology for coding agents. | Make the agent follow better engineering process: brainstorm, plan, TDD, debug, review, verify. |
| GStack | A role-based virtual software team for agent-driven delivery. | Make one agent behave like a product/engineering/design/QA/release team through ordered slash-command roles. |
| hplan | A Product Build Gate skill before implementation starts. | Decide whether a product should be built at all, using evidence, interviews, UX planning, design gate, COGS, and human approval. |

## Workflow Comparison

| Dimension | Superpowers | GStack | hplan |
|---|---|---|---|
| Primary question | "How do we build this correctly?" | "How do we run this sprint like a software team?" | "Should we build this, and under what constraints?" |
| Start point | User has a coding task, feature, bug, or rough spec. | User has a product/feature idea or branch needing delivery discipline. | User has an idea, product direction, or early evidence but build readiness is uncertain. |
| Core flow | Brainstorm -> design approval -> worktree -> plan -> TDD/subagents -> review -> finish branch. | Think -> Plan -> Build -> Review -> Test -> Ship -> Reflect. | Evidence Gate -> Product Gate -> Build Gate -> implementation brief. |
| Evidence standard | Design/spec approval and verification evidence. | Role-based pressure testing, review, browser QA, release evidence. | Competitor research, alternative research, interviews, problem definition, ICP/JTBD, COGS, metrics, human checkpoints. |
| Human role | Approves design chunks, reviews plans, decides branch finish path. | Approves product/plan decisions and uses specialist commands. | Owns market judgment, evidence strength, product taste, COGS risk, and gate decisions. |
| Product discovery depth | Useful brainstorming, but not a mandatory market-validation system. | Strong product challenge through office-hours and CEO/design reviews, but not a full research/interview gate. | Mandatory market diagnosis, competitor research, interviews or strong behavior evidence, and problem definition before PRD. |
| Design | Indirect; depends on task and downstream coding skill. | Explicit design review/consultation/design-html capabilities. | Design Gate before UI: reference stack, mood, hierarchy, component/state rules, mobile QA, AI trust states. |
| Economics | Not core. | Not core, though plans may discuss scope and product tradeoffs. | Core build blocker: COGS, gross margin, usage caps, free-user abuse, payment/usage boundary. |
| QA / verification | Strong TDD, debugging, review, verification before completion. | Strong browser QA, review, release, and sprint hygiene. | Defines required tests and readiness; does not replace downstream code QA tools. |
| Multi-agent execution | Subagent-driven development and worktrees. | Conductor/parallel sprints and specialist role commands. | Not a multi-agent executor. It can produce briefs that feed those systems. |
| Output artifact style | Plans, tests, reviews, branch finish decisions. | Design docs, plan reviews, QA reports, release artifacts. | Market diagnosis, evidence table, journey map, sitemap, design guidelines, COGS, metrics, PRD seed, AGENTS/CLAUDE briefs. |
| Best downstream pairing | Use after hplan Build Gate for TDD implementation and review. | Use after hplan Build Gate for sprint execution, design review, browser QA, and ship. | Use before Superpowers/GStack to prevent building an unvalidated product. |

## Superpowers Analysis

### What Superpowers Does Well

- Strong engineering discipline. It pushes agents toward design approval, implementation planning, true red/green TDD, debugging discipline, code review, and verification.
- Composable skills. The workflow can route into brainstorming, writing plans, executing plans, TDD, systematic debugging, worktrees, subagent development, code review, and branch finishing.
- Broad host support. The README describes support across Claude Code, Codex CLI/App, Gemini CLI, OpenCode, Cursor, Factory Droid, and GitHub Copilot CLI.
- Skill invocation discipline. The ecosystem focuses on getting the agent to actually use relevant skills instead of improvising.
- Good fit after a problem is accepted. Once hplan has created a credible PRD seed and implementation brief, Superpowers is a strong downstream build method.

### Superpowers Gaps Relative To hplan

- It is not primarily a market discovery or customer evidence system.
- It does not require competitor research, alternative mapping, user interviews, or evidence strength tagging before implementation.
- It does not make COGS, usage caps, gross margin, or free-user abuse first-class build blockers.
- It can improve the quality of a plan, but it does not by itself prove the product should exist.
- It is optimized for software correctness and delivery discipline, not product differentiation and monetization viability.

### What hplan Should Borrow

- Strict "no unsupported progress" posture: evidence before claims.
- Clear skill routing and activation language.
- Verification-before-completion mindset.
- Separate execution helpers instead of rewriting deterministic routines in prompts.
- Human checkpoints at design/plan boundaries.

### What hplan Should Not Copy

- Do not become a general coding methodology.
- Do not require TDD or implementation steps during Evidence Gate.
- Do not optimize for autonomous coding before human market judgment.
- Do not split into many skills if that lets users bypass Evidence Gate and jump to PRD.

## GStack Analysis

### What GStack Does Well

- Role clarity. It gives the agent explicit "brains" such as office hours, CEO review, engineering review, design review, QA, security, release, and retro.
- Ordered delivery loop. Its public positioning emphasizes reframing the problem, locking the plan, reviewing code, running browser QA, shipping cleanly, and learning from the sprint.
- Product pushback. `/office-hours` and `/plan-ceo-review` are useful patterns for challenging weak scope and finding a stronger wedge.
- Browser QA and release discipline. `/qa`, `/review`, and `/ship` address the common failure where agent-written code looks done but is not user-tested.
- Cross-host direction. Public docs mention Claude Code, Codex, and compatible agents.

### GStack Gaps Relative To hplan

- Its product challenge is strong, but it is still mostly a delivery system. It does not force an evidence sequence of competitor research -> user interviews -> ICP/JTBD -> journey/sitemap -> COGS before PRD.
- It can pressure-test a plan, but it does not require real user interviews or behavior evidence as a hard gate.
- It has role breadth, which can create operational complexity for early solo validation.
- It focuses more on "team standards for shipping" than "economic validity of the thing being shipped."
- Public counts and descriptions vary across sources and versions, so hplan should avoid copying numerical claims into core docs.

### What hplan Should Borrow

- Role-style review prompts can improve gate quality: founder challenge, engineering review, design review, QA review, security review.
- Ordered sprint language is useful after Build Gate.
- Browser QA and design-review expectations should be downstream checks for UI products.
- The idea that every step should feed the next artifact is strong: hplan should preserve evidence -> product -> build traceability.

### What hplan Should Not Copy

- Do not make dozens of commands required for a first planning run.
- Do not prioritize parallel sprints before the product's market and economics are credible.
- Do not treat founder/CEO taste as a substitute for customer behavior evidence.
- Do not make browser QA part of Evidence Gate; it belongs after implementation starts.

## hplan's Distinct Wedge

hplan's wedge is upstream of both systems:

```text
Superpowers and GStack improve how agents build.
hplan decides whether the thing deserves to be built.
```

The hard differences:

- Mandatory competitor and alternative research.
- Mandatory user interviews or strong behavior evidence.
- Persona/ICP based on behavior, Push/Pull/Habit/Anxiety, current workaround, and buying trigger.
- Problem definition before PRD.
- User journey map and sitemap before implementation.
- Design Gate before UI.
- COGS and gross margin as build blockers.
- Usage/payment boundary before paid or variable-cost workflows.
- Human-in-the-loop checkpoints at Evidence, Product, Build, Spec, Implementation, and Launch gates.
- Lean/full scaffold profile to avoid document sprawl.

## Recommended hplan Improvements

### 1. Position hplan As Pre-Sprint, Not Anti-Sprint

hplan should not compete with Superpowers or GStack on implementation discipline. It should feed them.

Recommended language:

> Use hplan before Superpowers or GStack. hplan produces the evidence-backed brief; downstream coding workflows execute and verify the build.

### 2. Add Downstream Compatibility Notes

When Build Gate is approved, hplan should produce:

- `AGENTS.md` for Codex.
- `CLAUDE.md` for Claude Code.
- A short "handoff to implementation workflow" section:
  - for Superpowers: use the PRD seed with brainstorming/writing-plans/TDD/review.
  - for GStack: start with `/office-hours` or `/autoplan`, then `/review`, `/qa`, and `/ship`.

### 3. Keep The Lean Artifact Budget

GStack and Superpowers both encourage richer process. hplan should counterbalance this with artifact discipline:

- Default `--profile lean`.
- Expand to `--profile full` only when separate review ownership is needed.
- Keep `PRODUCT_BRIEF.md` as the first source of truth.

### 4. Make Human Checkpoints More Concrete

Borrow the role-based clarity from GStack but keep hplan's decision vocabulary:

- Evidence reviewer: accept/reject competitor set and interview target.
- Product reviewer: accept/reject problem, ICP/JTBD, journey, sitemap, design direction.
- Economics reviewer: accept/reject COGS, price, allowance, and abuse risk.
- Build reviewer: build/interview/pivot/hold.

### 5. Add A "Do Not Build" Gate Report

hplan should create a visible "not building" section in every report:

- What not to build now.
- Why it is excluded.
- What evidence would reopen it.
- Which competitor/alternative already owns it.

### 6. Treat COGS As hplan's Signature Differentiator

Neither Superpowers nor GStack is primarily an economic gate. hplan should lean into:

- unit cost separation
- p90 COGS measurement
- free-user abuse modeling
- success-only usage charge rules
- provider routing by cost/quality/speed/privacy
- gross margin decision states

### 7. Keep hplan One Skill For v1

Do not split hplan into many skills yet. The moment `hplan-prd` exists as a separate trigger, users and agents will be tempted to skip Evidence Gate.

Recommended v1 structure:

```text
hplan
├── Evidence Gate
├── Product Gate
└── Build Gate
```

Possible later split only after the gate router is strong:

```text
hplan-router
├── hplan-evidence
├── hplan-product
└── hplan-build
```

## Comparison Summary

| Recommendation | Reason |
|---|---|
| Do not copy Superpowers/GStack wholesale. | They solve delivery discipline more than product evidence. |
| Borrow their process rigor. | hplan benefits from explicit checkpoints, role clarity, and verification. |
| Stay upstream. | hplan's strongest value is preventing polished execution of weak ideas. |
| Make economic gates visible. | COGS and usage caps are a stronger differentiator for paid AI products. |
| Keep scaffold lean by default. | Product planning should create clarity, not file clutter. |
| Support handoff into them. | hplan can become the missing pre-build gate for both ecosystems. |

## Final Position

hplan should be the **Product Build Gate** that runs before software delivery frameworks:

```text
hplan:
  Is this worth building?
  Who is it for?
  What pain is proven?
  What should we not build?
  Can the unit economics work?
  What must the human approve?

Superpowers / GStack:
  Now build it with discipline.
  Test it.
  Review it.
  QA it.
  Ship it.
```

That separation is the durable wedge.
