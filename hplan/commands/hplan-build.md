---
description: "Run the hplan Build Gate — execute COGS sentinel, record the decision in decision-log, and produce a handoff to your downstream coding ecosystem."
argument-hint: "[brief.json or inline parameters]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-build

Run the **Build Gate** after Evidence + Product Gates have been approved.

## Prerequisites

- `/hplan-evidence` returned `build`
- `/hplan-product` produced `docs/OPPORTUNITY_TREE.md`
- COGS scenario hypothesis (provider, model, tokens, calls/user, ARPU)

## Steps

1. **COGS sentinel** — invoke `cogs-sentinel` skill. Must return GREEN or CONDITIONAL_GO with explicit mitigations.
2. **Decision log** — invoke `decision-log` skill to record the gate decision (`build`, `CONDITIONAL_GO`, `pivot`, `hold`).
3. **If decision is `build` or `CONDITIONAL_GO`** — invoke `handoff` skill to export to your chosen downstream target (`/hplan-handoff` may be used directly).
4. **If `pivot` or `hold`** — invoke `exclusions` to record the wedge that didn't work + the `reopen_trigger`.

## Mandatory Gate Output

Build Gate must include:
- COGS sentinel result (GREEN / CONDITIONAL_GO / RED) with p90 margin number
- Decision recorded in `harness/decisions.jsonl`
- For `build`: `harness/build-gate/checkpoint.json` with `status: "approved"` (this unblocks the PreToolUse hook)

## Output

- `harness/build-gate/cogs_report.md`
- New entry in `harness/decisions.jsonl`
- Next step: `/hplan-handoff <target>` to export
