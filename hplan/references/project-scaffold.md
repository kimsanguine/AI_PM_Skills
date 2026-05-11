# Project Scaffold Gate

Use this reference when the user wants hplan to initialize or standardize a product repository after the Build Gate is credible.

The scaffold must preserve the reasoning artifacts that justified implementation. It should not create an empty app shell divorced from market evidence.

## When To Use

Use this only when:

- Evidence Gate and Product Gate are credible, or
- the user explicitly wants a planning repository scaffold before implementation, or
- an existing repo needs to be reorganized around hplan artifacts.

If evidence is weak, generate only `docs/` and `harness/` planning artifacts. Do not create implementation-heavy folders as if build were approved.

## Artifact Budget

Default to the lean scaffold. The goal is fewer source-of-truth files, not a planning museum.

- `--profile lean`: one consolidated `PRODUCT_BRIEF.md` plus the core blockers: `DESIGN.md`, `UNIT_ECONOMICS.md`, `HITL_FLOW.md`, `RISK_POLICY.md`, `DECISION_LOG.md`, and build docs only when build-ready.
- `--profile full`: expands evidence, product, benchmark, metrics, launch, and readiness decisions into separate audit docs.

Use `full` when the project has multiple stakeholders, policy/cost risk, investor/customer review, or an existing team that needs separate ownership. Use `lean` for solo-builder and early validation work.

## Do Not

- Do not generate the full document set by default just because the skill can.
- Do not create `apps/`, `services/`, `packages/`, `tests/`, or `infra/` before stack and Build Gate status are clear.
- Do not put hplan outputs inside `.codex/`, `.claude/`, or `.agents/`; those are agent runtime/config folders.
- Do not create real `.env` files or commit secrets.
- Do not overwrite existing project docs unless the user explicitly passes `--force` or asks for replacement.
- Do not split a lean artifact into many files unless the split creates clearer ownership, review, or auditability.

## Scaffold Command

Use the deterministic helper when a real folder should be created:

```bash
python3 scripts/scaffold_project.py <target-dir> --mode planning --profile lean
python3 scripts/scaffold_project.py <target-dir> --mode build-ready --profile lean
python3 scripts/scaffold_project.py <target-dir> --mode build-ready --profile full
python3 scripts/scaffold_project.py <target-dir> --mode implementation --profile lean
```

- `planning`: creates planning docs and `harness/`.
- `build-ready`: adds `review/`, `scripts/`, `AGENTS.md`, `CLAUDE.md`, `.agents/skills/`, `.codex/`, `.claude/`, `.env.example`, and `.gitignore`.
- `implementation`: adds app/service/test/infra placeholder folders after stack selection.
- `lean`: keeps planning compact around `PRODUCT_BRIEF.md`.
- `full`: expands into separate evidence, product, benchmark, metrics, launch, and readiness docs.

The script skips existing files by default. Use `--force` only when the user explicitly wants templates overwritten.

## Lean Folder Structure

```text
project-root/
├── docs/
│   ├── README.md
│   ├── PRODUCT_BRIEF.md
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── HITL_FLOW.md
│   ├── DESIGN.md
│   ├── UNIT_ECONOMICS.md
│   ├── METRICS.md
│   ├── IMPLEMENTATION_READINESS.md
│   ├── RISK_POLICY.md
│   └── DECISION_LOG.md
├── harness/
│   ├── evidence/
│   ├── product-gate/
│   ├── build-gate/
│   ├── exports/
│   └── reports/
├── review/
├── scripts/
├── AGENTS.md
├── CLAUDE.md
├── .agents/
│   └── skills/
├── .codex/
│   ├── config.toml
│   ├── hooks.json
│   └── hooks/
├── .claude/
│   ├── settings.json
│   ├── hooks/
│   ├── skills/
│   └── agents/
├── .env.example
├── .gitignore
└── README.md
```

## Full Folder Structure

```text
project-root/
├── docs/
│   ├── README.md
│   ├── PRODUCT_BRIEF.md
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── DESIGN.md
│   ├── MARKET_RESEARCH.md
│   ├── COMPETITIVE_RESEARCH.md
│   ├── ICP_JTBD.md
│   ├── USER_INTERVIEWS.md
│   ├── PROBLEM_BRIEF.md
│   ├── USER_JOURNEY_MAP.md
│   ├── SITEMAP.md
│   ├── HYPOTHESIS_TREE.md
│   ├── HITL_FLOW.md
│   ├── UNIT_ECONOMICS.md
│   ├── PERFORMANCE_BENCHMARK.md
│   ├── METRICS.md
│   ├── LAUNCH_EXPERIMENT.md
│   ├── IMPLEMENTATION_READINESS.md
│   ├── RISK_POLICY.md
│   └── DECISION_LOG.md
├── harness/
│   ├── evidence/
│   ├── product-gate/
│   ├── build-gate/
│   ├── exports/
│   └── reports/
├── review/
│   ├── design-review.md
│   ├── security-privacy-review.md
│   ├── cost-review.md
│   ├── launch-review.md
│   └── qa-checklist.md
├── scripts/
│   ├── README.md
│   ├── validate_docs.sh
│   └── run_checks.sh
├── AGENTS.md
├── CLAUDE.md
├── .agents/
│   └── skills/
├── .codex/
│   ├── config.toml
│   ├── hooks.json
│   └── hooks/
│       └── README.md
├── .claude/
│   ├── settings.json
│   ├── hooks/
│   │   └── README.md
│   ├── skills/
│   │   └── README.md
│   └── agents/
├── .env.example
├── .gitignore
└── README.md
```

Add app-specific folders only after the stack is known, for example `apps/`, `services/`, `packages/`, `data/`, `tests/`, or `infra/`.

## Folder Roles

### `docs/`

Long-lived product source of truth.

Required docs:

| File | Purpose |
|---|---|
| `PRODUCT_BRIEF.md` | Lean source of truth combining market, competitors, ICP/JTBD, interviews, problem, journey, sitemap, and hypothesis tree |
| `PRD.md` | Product requirements after build gate |
| `ARCHITECTURE.md` | System boundary, services, data model, APIs, job states |
| `DESIGN.md` | Agent-readable design system and UI rules |
| `MARKET_RESEARCH.md` | Market diagnosis and market vacuum |
| `COMPETITIVE_RESEARCH.md` | Competitor and alternative research |
| `ICP_JTBD.md` | Persona, ICP, JTBD, buying trigger |
| `USER_INTERVIEWS.md` | Interview plan, snapshots, evidence table |
| `PROBLEM_BRIEF.md` | One-page problem definition |
| `USER_JOURNEY_MAP.md` | Required pre-build UX artifact |
| `SITEMAP.md` | Required pre-build route/navigation artifact |
| `HYPOTHESIS_TREE.md` | OST or hypothesis tree |
| `HITL_FLOW.md` | Human checkpoints, approval states, interview review, spec/plan/task gates |
| `UNIT_ECONOMICS.md` | Pricing, COGS, usage caps, margin guardrails |
| `PERFORMANCE_BENCHMARK.md` | Latency/quality/provider benchmarks when relevant |
| `METRICS.md` | 5-layer metrics and event plan |
| `LAUNCH_EXPERIMENT.md` | Alpha, paid signal, launch loop |
| `IMPLEMENTATION_READINESS.md` | Build blockers, architecture boundary, Go/No-Go |
| `RISK_POLICY.md` | Privacy, rights, source/data policy, retention, takedown |
| `DECISION_LOG.md` | Dated decisions and reversals |

### `harness/`

Skill-generated working outputs.

Use it for generated reports, gate outputs, intermediate exports, scoring results, and snapshots. This folder makes it clear what hplan produced versus what the product team has accepted as source of truth in `docs/`.

Recommended:

- `harness/evidence/`: interview snapshots, competitor notes, raw evidence summaries
- `harness/product-gate/`: problem briefs, journey drafts, sitemap drafts, design drafts
- `harness/build-gate/`: PRD seed, AGENTS brief, COGS reports, test matrices
- `harness/exports/`: markdown/pdf/json exports
- `harness/reports/`: dated hplan gate reports

### `review/`

Human and agent review checklists.

Use it for:

- Design review
- Security/privacy review
- Cost/COGS review
- Launch review
- QA checklist
- Payment/provider review when relevant

### Agent Runtime Folders

Keep hplan outputs separate from agent runtime configuration.

Use:

- `.agents/skills/`: optional repo-local Codex skills. Codex scans this path from the current working directory up to the repo root.
- `.codex/config.toml`: Codex project configuration.
- `.codex/hooks.json`: Codex project hook registry.
- `.codex/hooks/`: Codex-specific hook scripts or hook documentation.
- `.claude/settings.json`: Claude Code project settings, permissions, and hook definitions.
- `.claude/hooks/`: Claude-specific hook scripts.
- `.claude/skills/`: optional Claude Code project skills.
- `.claude/agents/`: optional Claude Code project subagents.

Do not put hplan generated reports in `.codex/`, `.claude/`, or `.agents/`. Generated planning outputs belong in `harness/`; accepted source-of-truth documents belong in `docs/`.

### `scripts/`

Reusable local commands.

Start small:

- `validate_docs.sh`: check required docs exist
- `run_checks.sh`: run lint/typecheck/test/build commands once stack is known

Do not add fragile scripts before the repo stack is known.

### Root Agent Files

Use both when the user works with multiple coding agents:

- `AGENTS.md`: Codex instructions, commands, repo policies, verification gates
- `CLAUDE.md`: Claude Code memory, project conventions, allowed workflows

They should agree on:

- source of truth docs
- commands
- env vars
- build gates
- forbidden actions
- privacy/cost constraints

### Config Files

- `.codex/config.toml`: Codex project configuration
- `.codex/hooks.json`: Codex hook registry
- `.claude/settings.json`: Claude Code permissions, settings, and hook registry
- `.env.example`: env var template only
- `.gitignore`: must ignore `.env`, `.claude/settings.local.json`, local outputs, temporary artifacts, caches, and private benchmark results

Never generate real `.env` secrets.

## Minimal `.codex/config.toml`

```toml
# Codex project configuration.
# Personal defaults live in ~/.codex/config.toml.

[features]
codex_hooks = true

# Optional project defaults after stack selection:
# model = "gpt-5.5"
# approval_policy = "on-request"
# sandbox_mode = "workspace-write"
```

## Minimal `.codex/hooks.json`

```json
{
  "hooks": {}
}
```

Start with empty hooks. Add deterministic hooks only after the team agrees on the commands and failure behavior.

## Minimal `.claude/settings.json`

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "hooks": {}
}
```

## Minimal `.gitignore`

```gitignore
.env
.env.*
!.env.example
.claude/settings.local.json
.codex/log/
.codex/tmp/
node_modules/
.next/
dist/
build/
__pycache__/
.pytest_cache/
.DS_Store
output/
tmp/
*.log
```

Adjust ignored outputs to the project. If outputs include private data or paid provider responses, ignore them by default.

## Scaffold Rules

- If the stack is unknown, create docs and harness first.
- If the product handles private data, include `RISK_POLICY.md` before implementation.
- If the product has variable cost, include `UNIT_ECONOMICS.md` before implementation.
- If the product promises speed, include `PERFORMANCE_BENCHMARK.md` before implementation.
- If the product has UI, include `DESIGN.md`, `USER_JOURNEY_MAP.md`, and `SITEMAP.md` before implementation.
- If the product is moving across gates, include `HITL_FLOW.md` and record human approval status before implementation.
- If the user asks for implementation, generate `AGENTS.md` and `CLAUDE.md` with the same gate rules.
- Keep `.env.example`; never create real secrets in `.env`.

## Scaffold Decision

Use:

- `PLANNING_SCAFFOLD`: evidence/product docs only
- `BUILD_READY_SCAFFOLD`: docs, harness, review, scripts, `AGENTS.md`, `CLAUDE.md`, `.agents/skills/`, `.codex/`, `.claude/`
- `IMPLEMENTATION_SCAFFOLD`: build-ready scaffold plus app/service/test folders after stack selection

If in doubt, choose `PLANNING_SCAFFOLD` with `--profile lean`.
