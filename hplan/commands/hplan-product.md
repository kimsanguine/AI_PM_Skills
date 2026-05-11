---
description: "Run the hplan Product Gate — generate Opportunity Solution Tree, confirm user journey, sitemap, and design pointers before any implementation brief. Use when Evidence Gate has been approved and you need to confirm the wedge translates into a real Opportunity Tree, journey, sitemap, and design direction."
argument-hint: "[outcome statement or path to ost.json]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-product


## Instructions

You are running the **hplan Product Gate** for: **$ARGUMENTS**

### Phase 1 — Outcome
Confirm a measurable, time-bounded outcome (not "make money"). Example: "Solo PM closed-won rate +25% within 90 days".

### Phase 2 — Opportunity Solution Tree
Invoke `ost` skill. Generate `docs/OPPORTUNITY_TREE.md` with Mermaid. Verify each opportunity has evidence_count ≥ 3 strong-Push interviews from `interview-synthesis audit`.

### Phase 3 — User Journey + Sitemap
Reference `hplan/references/product-planning.md`. Confirm the journey covers Discover → Start → Core → Review → Pay with empty / loading / failed / blocked / paid / review states.

### Phase 4 — Design pointer
Reference `hplan/references/design-gate.md`. Confirm `DESIGN.md` direction exists (mood, hierarchy, component rules, state rules, mobile checklist).

### Phase 5 — Hypothesis Tree
Every solution in OST has an experiment + decision_rule.

## Output Format

Return:

1. **OST status** — `docs/OPPORTUNITY_TREE.md` generated with N opportunities and M solutions
2. **Journey + sitemap** — confirmed present (yes/no with gaps)
3. **Design pointer** — confirmed present (yes/no)
4. **Next gate** — `/hplan-build` or back to evidence/pivot
