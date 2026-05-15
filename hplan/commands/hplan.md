---
description: "Run the full hplan build gate in one command — exclusions collision check + evidence rubric + COGS analysis — and return a single GO / HOLD / INVESTIGATE verdict with 3-line reason. Use when a PM or founder has a new product idea and wants the fastest WHETHER answer before committing any further time."
argument-hint: "[idea description]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan — Build Gate Orchestrator

Single entry point for the hplan WHETHER gate. Chains all three checks and returns a final verdict. No prior gate knowledge required.

## Instructions

You are running the **hplan Build Gate** for: **$ARGUMENTS**

Execute these steps in sequence. Stop early if a gate fails — do not run downstream gates on a HOLD.

---

### Step 1 — Exclusions Collision Check

```bash
python3 hplan/scripts/exclusions_registry.py check "$ARGUMENTS"
```

**If COLLISION detected:**
- Show the matched exclusion entry: date, reason, `reopen_trigger`
- Check whether the `reopen_trigger` condition is met given the current idea
- If **NOT met** → output final verdict immediately:

  ```
  VERDICT: HOLD
  Reason:  Prior exclusion applies — [matched entry reason]
  Trigger: [reopen_trigger text] — not met
  Gate:    EXCLUSIONS
  ```

  Stop. Do not proceed to Step 2.

- If **met** → note "reopen_trigger MET — continuing to evidence check"

---

### Step 2 — Evidence Rubric Score

Score the idea against the 7-criterion rubric. Use only information available in the user's message; do not assume details not provided.

| Criterion | Max pts | Score | Notes |
|-----------|---------|-------|-------|
| ICP specificity (named segment with behavior, not "SMBs") | 15 | | |
| Recent painful event (within 3 months, user-reported) | 15 | | |
| Workaround evidence (users already doing something manual) | 15 | | |
| Repetition evidence (same complaint heard 3+ times) | 15 | | |
| Economic pain quantified (time × frequency × cost) | 15 | | |
| MVP narrowness (one workflow, not a platform) | 15 | | |
| Acquisition path defined (first 10 customers, not "go viral") | 10 | | |

**Score interpretation:**
- **80–100**: Strong — proceed to Step 3
- **60–79**: Conditional — flag the weakest criteria, proceed to Step 3
- **< 60**: HOLD — insufficient evidence. Output verdict now:

  ```
  VERDICT: HOLD
  Reason:  Evidence score [X]/100 — below 60 threshold. Weakest: [criterion]
  Next:    Run /hplan-evidence for a full rubric + interview synthesis
  Gate:    EVIDENCE
  ```

  Stop.

---

### Step 3 — COGS Gate

Run the COGS sentinel only if a pricing signal is available in the idea description (e.g., target price, provider model, usage pattern). If no pricing signal exists, note "COGS: no pricing input — skipping" and proceed to Step 4 with a CONDITIONAL note.

```bash
python3 hplan/scripts/cogs_sentinel.py
```

Interpret result:
- **GREEN** (p50 ≥ 60%, p90 ≥ 40%): Economics confirmed
- **CONDITIONAL_GO** (p50 ≥ 40%, p90 ≥ 20%): Flag pricing risk, continue
- **RED**: HOLD — COGS unworkable at current pricing. Output verdict:

  ```
  VERDICT: HOLD
  Reason:  COGS RED — p90 margin below threshold at current pricing
  Next:    Run /hplan-cogs with adjusted --arpu or --tokens-in to find GREEN scenario
  Gate:    COGS
  ```

  Stop.

---

### Step 4 — Final Verdict

Output a 4-line verdict block:

```
VERDICT: GO / HOLD / INVESTIGATE

Reason:  [1-line summary of the deciding factor]
Next:    [Concrete next action]
Gate:    [Which gate was decisive: EXCLUSIONS / EVIDENCE / COGS / ALL-PASS]
```

**GO** — All 3 gates pass. Suggest `/hplan-product` to begin full product brief.

**HOLD** — Any gate fails (already output in Steps 1–3).

**INVESTIGATE** — CONDITIONAL_GO on COGS, or evidence score 60–79, or COGS skipped due to no pricing signal. Suggest the specific gate command to run next.

---

## Notes

This command is the fastest WHETHER answer. For deeper analysis, follow with:
- `/hplan-evidence` — full 100-point rubric with interview synthesis ingestion
- `/hplan-cogs` — detailed COGS with custom provider pricing inputs
- `/hplan-product` — full product brief (requires GO verdict first)
- `/hplan-handoff` — export to Spec-Kit / Kiro / Claude Code after GO

All decisions are logged to `harness/build-gate/decision_log.jsonl` automatically when the underlying scripts run.
