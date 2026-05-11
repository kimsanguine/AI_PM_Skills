---
description: "Run the hplan Evidence Gate end-to-end — score idea against 100-point rubric, ingest interview synthesis, check exclusions registry. Use when a PM or founder pitches an idea and you need to check whether evidence is strong enough before PRD work."
argument-hint: "[idea description or path to JSON]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-evidence


## Instructions

You are running the **hplan Evidence Gate** for: **$ARGUMENTS**

Execute these steps in sequence:

### Step 1 — Exclusion collision check
Invoke `exclusions` skill — `python3 hplan/scripts/exclusions_registry.py check "<idea>"`. If COLLISION + reopen_trigger unmet, STOP and report.

### Step 2 — Structure the input
Collect from the user message: `idea`, `target` (ICP behavior), `hypothesis`, `alternatives` (list), `features` (≤3), `interview_notes` (one per line).

### Step 3 — 100-point rubric
Invoke `evidence-rubric` skill — runs `scripts/generate_report.py`. Capture score + missing axes.

### Step 4 — Interview synthesis
If `interview_notes` is thin or `decision == "interview"`, invoke `interview-synthesis` skill to either ingest AI export OR plan fresh interviews. Audit the 5/3 strong-Push rule.

### Step 5 — Decide
- `build` + 2+ interview lines + economic pain → proceed to `/hplan-product`
- `interview` → run more interviews until 5/3 satisfied
- `pivot` / `hold` → log via `decision-log` skill and add to `exclusions`

## Output Format

Return:

1. **Exclusion verdict** — CLEAR or COLLISION (with prior id + reopen_trigger)
2. **Rubric score** — N/100 with breakdown of weak axes
3. **Interview audit** — interviews tagged, distinct strong-Push persons
4. **Decision** — `build` / `interview` / `pivot` / `hold` / `CONDITIONAL_GO`
5. **Next gate** — `/hplan-product`, more interviews, or stop
