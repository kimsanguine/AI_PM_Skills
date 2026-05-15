---
description: "Run the hplan Product Gate — generate Opportunity Solution Tree, confirm user journey, sitemap, and design pointers before any implementation brief. Use when Evidence Gate has been approved and you need to confirm the wedge translates into a real Opportunity Tree, journey, sitemap, and design direction."
argument-hint: "[outcome statement or path to ost.json]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-product

<HARD-GATE name="evidence">
Evidence Gate PASS 없이 이 게이트 진입 금지.
아래 중 하나가 없으면 즉시 STOP:
  - `harness/build-gate/decision_log.jsonl` 에 gate=evidence 항목
  - 또는 인터뷰 3건 이상 / 행동 증거가 이미 이 대화에 제시됨

예외 허용 (Evidence Gate 인풋으로 제한):
  경쟁사 분석 · 고객 프로파일링 · AI persona 초안 · 시장 리서치
  단, 이 결과물은 Evidence Gate를 자동 통과시키지 않는다.
  인터뷰 또는 행동 증거 없이 Gate PASS 선언 금지.

검증:
```bash
python3 hplan/scripts/decision_log.py list | grep '"gate": "evidence"' | grep '"decision"' | tail -1
```
결과가 비어 있으면 STOP — "Evidence Gate 미통과. `/hplan-evidence <idea>` 먼저 실행하세요." 출력.
</HARD-GATE>

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
