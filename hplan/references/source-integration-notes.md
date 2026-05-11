# Source Integration Notes

This is a maintenance note, not a normal hplan execution reference.

Source reviewed:

`/Users/sanguinekim/Documents/[준비중] 패캠_하네스플래닝/Part1_시장조사_강의자료_연계_v2.6.md`

Purpose:

- Explain what was adapted into the generic hplan skill.
- Explain what was intentionally not adapted because it is course-specific, person-specific, product-specific, time-sensitive, or too implementation-specific.
- Protect the skill from accidentally becoming tied to one sample project.

## Adaptation Principle

The source document is rich but heavily tied to a specific course, instructor positioning, and example product narrative. hplan only adopts patterns that generalize to real product planning:

- market vacuum before build
- competitor and alternative research
- behavior-based ICP/persona
- JTBD and Switch/Mom Test interview discipline
- problem definition before PRD
- user journey map and sitemap before implementation
- design gate before UI
- COGS and usage boundaries before paid build
- metrics and launch experiments before scale
- human-in-the-loop approval before each gate

hplan does not adopt fixed product names, course positioning, authority claims, prices, timelines, or local market claims as defaults.

## Reflected In hplan

| Source idea | How it was reflected | hplan files |
|---|---|---|
| "코딩 자동화는 넘치지만 시장조사/문제정의가 병목" | hplan's default stance is to slow down premature building and require market evidence, competitor research, interviews, problem definition, and Product Gate approval before PRD. | `SKILL.md`, `market-research.md`, `product-planning.md` |
| Market abundance vs market vacuum | Added Market Diagnosis Pattern and Market Vacuum Stress Test: abundant market, remaining user blockage, current alternatives, paid outcome, and narrow wedge. | `market-research.md` |
| Counter-position as a core differentiator | Added 3 counter-position options: local/niche wedge, outcome/workflow wedge, economic/operational wedge. | `market-research.md` |
| "가르치지 않는 것" / explicit exclusions | Generalized into "What Not To Build" and cross-gate Do Not sections. The skill now requires saying what the product will not build, teach, automate, own, or promise. | `SKILL.md`, `market-research.md`, `icp-interview.md`, `product-planning.md`, `unit-economics.md`, `metrics-launch.md`, `performance-benchmark.md`, `implementation-readiness.md`, `human-in-loop.md`, `project-scaffold.md`, `design-gate.md` |
| Target should not be everyone | Persona and ICP rules reject demographic-only personas and require situation, Push, Pull, Habit, Anxiety, current workaround, buying trigger, and exclusion criteria. | `icp-interview.md`, `SKILL.md` |
| ICP -> JTBD -> interview flow | Evidence Gate requires ICP candidates, JTBD statements, screener questions, Switch Interview guide, recruiting plan, interview snapshots, and evidence tagging. | `icp-interview.md`, `SKILL.md` |
| Mom Test / Switch Interview discipline | Interview rules reject "Would you use this?" and focus on last occurrence, current workaround, switching trigger, time/money/risk cost, and next-week testability. | `icp-interview.md`, `human-in-loop.md` |
| Minimum 5 interviews | hplan requires a plan for at least 5 interviews or equivalent strong behavior evidence. It also states that 5 interviews can reveal a pattern, not prove PMF. | `SKILL.md`, `icp-interview.md`, `human-in-loop.md` |
| AI should assist discovery, not replace customer learning | Added Human + AI Interview Rule and Human Evidence Checkpoint. AI can transcribe, summarize, cluster, and tag; human must review quotes and evidence. | `icp-interview.md`, `human-in-loop.md`, `SKILL.md` |
| Interview evidence strength | Added Strong / Medium / Weak evidence table using recency, current alternative, frequency, economic pain, switching condition, and commitment. | `icp-interview.md` |
| Problem definition as a gate | hplan requires Problem Brief before journey, sitemap, design, PRD, and build. | `product-planning.md`, `SKILL.md` |
| User journey map and sitemap before implementation | Added explicit Product Gate requirement. These are not post-build cleanup docs. | `product-planning.md`, `design-gate.md`, `implementation-readiness.md`, `project-scaffold.md`, `SKILL.md` |
| OST / hypothesis tree | Added Outcome, opportunities, solution candidates, assumptions, tests, and decision criteria. Hypotheses must include market, product, revenue, and operational risk where relevant. | `product-planning.md`, `scripts/scaffold_project.py` |
| JTBD to Agent Spec | Added a conversion table from JTBD to agent job, questions, output, success metric, and human review. | `product-planning.md` |
| "1개 깊이" instead of many shallow projects | Generalized into "one paid outcome or one agent job" for MVP scope. | `SKILL.md`, `product-planning.md`, `metrics-launch.md` |
| Every implementation choice should carry product judgment | hplan makes design, cost, performance, policy, and architecture part of the Build Gate rather than isolated engineering tasks. | `SKILL.md`, `design-gate.md`, `unit-economics.md`, `implementation-readiness.md`, `performance-benchmark.md` |
| Design direction must guide actual UI work | Added Design Gate with product mood, screen hierarchy, visual principles, component rules, state rules, mobile verification, and reference-stack usage. | `design-gate.md`, `SKILL.md` |
| Design references and inspiration stack | Incorporated the user's requested design reference stack: 21st.dev, transitions.dev, Refero Styles, open-design, Montage Design System, diagram-design, Font of Web, Logo System, UXSnaps. | `design-gate.md` |
| AI product UI must expose trust | Added rules for confidence, evidence, fallback, risk, human override, usage, cost, policy, and latency states. | `design-gate.md`, `implementation-readiness.md`, `performance-benchmark.md` |
| Pricing and payment cannot be separated from cost | Added COGS gate, net revenue formula, target gross margin, allowed COGS, usage allowance, free-user abuse model, and economics decision. | `unit-economics.md`, `SKILL.md` |
| Payment provider vs usage meter split | Added explicit responsibility boundary: checkout/subscription status belongs to provider; usage allowance/blocking/charge belongs to app DB. | `unit-economics.md`, `implementation-readiness.md` |
| AI wrapper cost risk | Added cost unit separation: source import, model call, analysis run, render, storage, retry, export, agent task, paid usage unit. | `unit-economics.md` |
| Provider routing by cost/quality/speed | Added provider policy and routing table; cheapest provider is only acceptable if it clears quality, latency, privacy, and margin gates. | `unit-economics.md`, `performance-benchmark.md` |
| Need for eval and downstream quality | Added quality gates for evidence, numeric/entity correctness, schema validity, action/decision completeness, friction, and cost. | `metrics-launch.md`, `performance-benchmark.md` |
| 5-layer metrics | Reflected as Sean Ellis/must-have, TTV, Override Rate, Frustration Index, Indispensability/Repeat MPO, plus revenue and COGS where paid usage exists. | `metrics-launch.md` |
| First 5 / 10 / 30 user milestones | Generalized into a milestone ladder. First 5 identifies wedge, first 10 tests pattern outside closest network, first 30 checks monetization/retention. | `metrics-launch.md` |
| Launch experiment before scale | Added alpha target, screener, build-in-public calendar, paid signal ladder, funnel, success metrics, and 14-day schedule. | `metrics-launch.md` |
| PRD should not be first artifact | `SKILL.md` now blocks PRD seed, AGENTS.md brief, issue list, and architecture until Evidence Gate and Product Gate are credible. | `SKILL.md` |
| Agent-ready implementation brief | Build Gate includes Agent Spec/workflow spec, AGENTS.md brief, MVP issue list, acceptance criteria, test matrix, and implementation readiness. | `SKILL.md`, `implementation-readiness.md`, `project-scaffold.md` |
| Human approval gates | Added Human In The Loop Flow with review-problem, review-spec, review-plan, review-tasks, review-implementation, and review-metrics. | `human-in-loop.md`, `SKILL.md`, `scripts/scaffold_project.py` |
| Repo scaffold for real usage | Added deterministic scaffold generator and repo structure with `docs/`, `harness/`, `review/`, `scripts/`, `AGENTS.md`, `CLAUDE.md`, `.codex/`, `.claude/`, `.agents/skills/`, `.env.example`, `.gitignore`. | `project-scaffold.md`, `scripts/scaffold_project.py`, `README.md` |
| Planning output can become too heavy | Added `--profile lean` and `--profile full`. Lean consolidates product evidence in `PRODUCT_BRIEF.md`; full expands audit docs only when useful. | `scripts/scaffold_project.py`, `project-scaffold.md`, `README.md`, `SKILL.md` |
| GStack-style agent review inspiration | Reflected as Build Gate review checklists, implementation readiness, performance benchmark, and later competitive comparison. | `implementation-readiness.md`, `performance-benchmark.md`, `competitive-landscape-superpowers-gstack.md` |

## Partially Reflected

| Source idea | What was kept | What was changed |
|---|---|---|
| 60-day live-build rhythm | Kept the idea of staged discovery/build/launch and 14-60 day review cycles. | hplan does not hard-code a 60-day course timeline. It uses gate readiness and first 5/10/30 milestones instead. |
| "PM 사고 + 빌딩 + 수익화" integrated positioning | Kept the integration of product judgment, implementation readiness, and monetization. | Removed course positioning and turned it into Product Build Gate workflow. |
| Specific sub-personas from the course source | Kept behavior-based segmentation logic. | Removed named course/audience categories and requires project-specific ICP creation. |
| Payment provider examples such as PortOne/Toss/Stripe | Kept payment/usage boundary and provider comparison logic. | Did not hard-code provider recommendations, fees, code, or local payment assumptions. Current provider research is required per project. |
| Korean/local market wedge | Kept local/niche wedge as one valid counter-position axis. | Did not assume Korea is always the market or that local language is always the winning wedge. |
| AI Discovery Skill building | Kept the idea that discovery can be assisted by skills/scripts. | hplan itself remains one skill with references and deterministic helpers; it does not create four separate discovery skills by default. |
| PMF and Sean Ellis score | Kept Sean Ellis/must-have as one metrics layer. | hplan refuses to call PMF from 5 interviews or early enthusiasm. It requires segmentation and launch metrics. |
| Build-in-public and acquisition | Kept launch experiment and recruiting messages. | Did not include a content calendar or community growth playbook as core hplan behavior. |
| Spec Kit / AGENTS.md orientation | Kept spec-driven agent brief and AGENTS.md scaffolding. | Did not require one specific agent host, framework, or spec format. |
| Performance/eval examples | Kept benchmark and quality gate patterns. | Did not embed specific LangGraph, slide-generation, AEO/GEO, or provider implementation code. |

## Not Reflected

| Source material | Why it was not reflected |
|---|---|
| Course identity, FastCampus mapping, 25-lesson curriculum, OT hooks, chapter allocation | hplan is a real-use planning/build gate skill, not course material. |
| Instructor-specific authority claims, career narrative, LINE/Kakao/Naver/Samsung/CJ/Eastsoft references | These are personal positioning assets, not reusable skill behavior. |
| PMFlow as the default product name or default example | hplan must stay product-agnostic. PMFlow-specific facts are not embedded in normal workflow. |
| Fixed price such as KRW 19,000/month | Pricing must be derived from customer willingness, competitor prices, payment fees, usage caps, and COGS per project. |
| Fixed target such as 30 paying users or exact MRR | hplan uses first 5/10/30 milestones as evidence ladder, not a universal revenue target. |
| Specific public market claims that may change, such as competitor status, user counts, or market closures | These are time-sensitive. hplan requires browsing and citations when current facts matter. |
| Exact external case claims around Lenny, Claire Vo, Marc Lou, Cat Wu, Pieter Levels, or local Korean SaaS examples | Useful inspiration, but not safe to hard-code into a generic skill. They belong in project-specific research. |
| Full PortOne/Toss/Next.js/Supabase payment code | Implementation-specific and likely to age. hplan keeps payment boundary and COGS rules instead. |
| LangGraph code walkthrough and AI slide generation implementation | Too specific for a generic product planning skill. Reflected only as benchmark/provider/workflow concepts. |
| AEO/GEO content strategy and SEO playbooks | Adjacent to launch/acquisition but not part of hplan's core build gate. Use a separate SEO/GEO skill when needed. |
| Community, open chat, course funnel, and personal branding strategy | Not part of product readiness gate. |
| "30 projects vs 1 deep SaaS" as a direct course comparison | Generalized into "one paid outcome or one agent job" to avoid course competitor language. |
| Exact named tool list as assumptions: Cursor, Claude Code, Replit, Lovable, Bolt, etc. | hplan may reference coding agents when relevant, but it does not assume one build tool or market category. |
| Claims such as "AI writes 90% of code" | Potentially time-sensitive and not necessary for hplan decisions. If used in market research, browse and cite current source. |

## Improvements Added Beyond The Source

- Lean/full scaffold profiles to avoid excessive file creation.
- `PRODUCT_BRIEF.md` as a compact source-of-truth option.
- Explicit `.codex/`, `.claude/`, and `.agents/skills/` separation.
- Human checkpoint status vocabulary: `READY_FOR_HUMAN_REVIEW`, `WAITING_FOR_HUMAN`, `APPROVED_BY_HUMAN`, `NEEDS_MORE_EVIDENCE`, `SAFE_TO_DRAFT_NEXT_GATE`.
- Performance benchmark gate with separate input-only, full-processing, live/incremental, and fallback paths.
- Review-ready public pages for paid/data-handling products.
- Rights/source/data policy before implementation.
- Cross-gate "Do Not" rules in every major reference, not only design.
- Competitive landscape note comparing hplan with Superpowers and GStack.

## Remaining Deliberate Gaps

- hplan does not yet ship a multi-skill suite. It remains one skill with references to preserve gate order.
- hplan does not yet include an automated interview repository parser. It provides templates and evidence rules.
- hplan does not yet implement a real COGS calculator across provider APIs. It provides formulas and measurement templates.
- hplan does not browse automatically from scripts. Browsing is an agent behavior when current competitor, pricing, or market facts are needed.
- hplan does not enforce repo hooks by default. It scaffolds conservative hook placeholders only.

## Maintenance Rule

When future source material is reviewed, adapt only the reusable method. Do not embed a course, person, exact product, current market claim, or one-off stack choice into normal hplan behavior unless the user explicitly wants a project-specific fork.
