---
description: "Run the hplan Evidence Gate end-to-end — score idea against 100-point rubric, ingest interview synthesis, check exclusions registry."
argument-hint: "[idea description or path to JSON]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-evidence

Run the full **Evidence Gate** sequence:

1. **Check exclusions registry first** — if the idea collides with a previous "Do Not Build" entry, surface the collision and confirm `reopen_trigger` is met before proceeding.
2. **Structure the input** — collect `idea`, `target`, `hypothesis`, `alternatives`, `features`, `interview_notes` from the user message ($ARGUMENTS).
3. **Score with the 100-point rubric** — invoke `evidence-rubric` skill (which runs `scripts/generate_report.py`).
4. **If interviews are thin** — invoke `interview-synthesis` skill to either import AI-clustered output or guide a fresh interview cycle.
5. **Decide**:
   - `build` + 2+ interview lines + economic pain → proceed to `/hplan-product`
   - `interview` → run `interview-synthesis` until 5/3 strong-Push pattern
   - `pivot` / `hold` → log via `decision-log` skill and consider adding to `exclusions`

## Use This Command When

- A PM or founder pitches an idea and you need to check whether it's ready for PRD work
- Before invoking any spec-driven coding workflow (Spec-Kit, Kiro, GStack, Superpowers)
- When the user says "let's build X" but evidence is unclear

## Boundary

Do not proceed to Product Gate or write any PRD-shaped artifact until:
- 5 interviews tagged with strong-Push for 3+ distinct persons
- Economic pain keyword present in evidence
- No active exclusion collision (or `reopen_trigger` satisfied)

## Output

A short report with:
- exclusions verdict
- 100-point score + breakdown
- interview-synthesis audit
- next gate suggestion (`/hplan-product`, more interviews, or stop)
