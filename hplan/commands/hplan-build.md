---
description: "Run the hplan Build Gate — execute COGS sentinel, record the decision in decision-log, and produce a handoff to your downstream coding ecosystem. Use when Evidence + Product gates are approved and you need to lock the economic model + final decision + downstream handoff."
argument-hint: "[brief.json or inline parameters]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-build


## Instructions

You are running the **hplan Build Gate** for: **$ARGUMENTS**

### Phase 1 — COGS sentinel
Invoke `cogs-sentinel` skill. Collect: provider, model, tokens_in, tokens_out, calls_per_user_month, ARPU, paid_conversion, free_abuse_multiplier. Run `scripts/cogs_sentinel.py`. Must return GREEN or CONDITIONAL_GO with named mitigations.

### Phase 2 — Decision log
Invoke `decision-log` skill to record the gate decision. Call `scripts/decision_log.py log` with project, gate=build, decision, and 2+ reasons.

### Phase 3 — Checkpoint approval
For `build` or `CONDITIONAL_GO`, write `harness/build-gate/checkpoint.json` with `status: "approved"` so the PreToolUse hook (`hooks/gate_guard.py`) unblocks downstream PRD/spec edits.

### Phase 4 — Handoff (or rollback)
- `build` / `CONDITIONAL_GO` → invoke `handoff` skill or instruct user to call `/hplan-handoff <target>`
- `pivot` / `hold` → invoke `exclusions` to record the wedge that didn't work + `reopen_trigger`

## Output Format

Return:

1. **COGS result** — GREEN / CONDITIONAL_GO / RED with p90 margin number
2. **Logged decision id** — `dec-YYYY-MM-DD-XXXXX`
3. **Checkpoint status** — written / pending
4. **Next step** — `/hplan-handoff <target>` or back to evidence/product
