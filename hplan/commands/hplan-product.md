---
description: "Run the hplan Product Gate — generate Opportunity Solution Tree, confirm user journey, sitemap, and design pointers before any implementation brief."
argument-hint: "[outcome statement or path to ost.json]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-product

Run the **Product Gate** after Evidence Gate has been approved.

## Prerequisites

- `/hplan-evidence` returned `build` or `CONDITIONAL_GO`
- `interview-synthesis audit` shows `PROCEED_TO_PRODUCT_GATE`

## Steps

1. **Outcome** — confirm a measurable, time-bounded outcome (not "make money").
2. **Opportunity Solution Tree** — invoke `ost` skill to generate `docs/OPPORTUNITY_TREE.md` with Mermaid.
3. **User Journey Map + Sitemap** — reference `hplan/references/product-planning.md` and confirm the journey covers Discover → Start → Core → Review → Pay/Continue with empty/loading/failed/blocked/paid/review states.
4. **Design pointer** — reference `hplan/references/design-gate.md`. Don't make screens, but confirm the project has a `DESIGN.md` direction.
5. **Hypothesis Tree** — every solution in OST has an experiment + decision_rule.

## Routing

- After Product Gate passes → `/hplan-build`
- If wedge breaks → `/hplan-exclude` to record what doesn't work, then re-enter `/hplan-evidence`

## Output

- `docs/OPPORTUNITY_TREE.md` with Mermaid diagram
- Confirmation that journey/sitemap/design pointers exist
- Next gate: `/hplan-build` or pivot
