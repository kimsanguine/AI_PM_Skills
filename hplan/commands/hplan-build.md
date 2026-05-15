---
description: "Run the hplan Build Gate — execute COGS sentinel, record the decision in decision-log, and produce a handoff to your downstream coding ecosystem. Use when Evidence + Product gates are approved and you need to lock the economic model + final decision + downstream handoff."
argument-hint: "[brief.json or inline parameters]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-build

<HARD-GATE name="product">
Product Gate PASS 없이 이 게이트 진입 금지.
아래 중 하나가 없으면 즉시 STOP:
  - `harness/build-gate/decision_log.jsonl` 에 gate=product 항목
  - 또는 Journey map + Sitemap이 이 대화에 이미 제시됨

검증:
```bash
python3 hplan/scripts/decision_log.py list | grep '"gate": "product"' | tail -1
```
결과가 비어 있으면 STOP — "Product Gate 미통과. `/hplan-product` 먼저 실행하세요." 출력.
Journey map + Sitemap 없이 Build Gate PASS 선언 금지.
</HARD-GATE>

## Instructions

You are running the **hplan Build Gate** for: **$ARGUMENTS**

### Phase 1 — COGS sentinel
Invoke `cogs-sentinel` skill. Collect: provider, model, tokens_in, tokens_out, calls_per_user_month, ARPU, paid_conversion, free_abuse_multiplier. Run `scripts/cogs_sentinel.py`. Must return GREEN or CONDITIONAL_GO with named mitigations.

### Phase 2 — Decision log
Invoke `decision-log` skill to record the gate decision. Call `scripts/decision_log.py log` with project, gate=build, decision, and 2+ reasons.

### Phase 3 — Checkpoint approval + STATE.md

For `build` or `CONDITIONAL_GO`, write `harness/build-gate/checkpoint.json` with the appropriate schema so `hooks/gate_guard.py` unblocks downstream PRD/spec edits.

**schema for `build`** (full GO):
```jsonc
{
  "status": "approved",
  "decision": "GO",
  "decision_id": "dec-YYYY-MM-DD-XXXXX"
}
```

**schema for `CONDITIONAL_GO`**:
```jsonc
{
  "status": "approved",
  "decision": "CONDITIONAL_GO",
  "decision_id": "dec-YYYY-MM-DD-XXXXX",
  "conditions": ["조건1", "조건2"],
  "allowed_paths": ["specs/NNN-", "docs/DESIGN.md"],
  "required_tests": ["tests/unit/test_조건1.py"],
  "expires_at": "YYYY-MM-DD"
}
```

**CONDITIONAL_GO 시 STATE.md 자동 생성** — `harness/STATE.md`에 아래 형식으로 작성:

```markdown
# hplan STATE
gate: build
verdict: CONDITIONAL_GO
decision_id: [decision_id]
generated: [오늘 날짜]

## Active 조건 (미검증)
| 조건 | verified_by | 상태 |
|------|-------------|------|
| [조건 1] | [추후 기입] | ❌ |
| [조건 2] | [추후 기입] | ❌ |

규칙: verified_by 파일이 생기면 ✅로 갱신.
      모든 조건 ✅ 없이 다음 Build Gate 종료 선언 금지.

## 블로커 (외부 의존성)
- [미완료 항목 — USER_TASKS.md 참조]

## 다음 진입 조건
[W1 진입 요건 한 줄 — 블로커 해소 시점]
```

STATE.md 생성 후 사용자에게 안내: "`harness/STATE.md` 생성됨 — 새 세션을 열면 이 파일을 자동으로 읽어 게이트 상태를 복원합니다."

### Phase 4 — Handoff (or rollback)
- `build` / `CONDITIONAL_GO` → invoke `handoff` skill or instruct user to call `/hplan-handoff <target>`
- `pivot` / `hold` → invoke `exclusions` to record the wedge that didn't work + `reopen_trigger`

## Output Format

Return:

1. **COGS result** — GREEN / CONDITIONAL_GO / RED with p90 margin number
2. **Logged decision id** — `dec-YYYY-MM-DD-XXXXX`
3. **Checkpoint status** — written / pending
4. **Next step** — `/hplan-handoff <target>` or back to evidence/product
