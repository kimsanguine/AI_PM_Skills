---
description: "Check whether a new feature request is in scope for the current CONDITIONAL_GO gate. Cross-checks against exclusions registry, allowed_paths, and COGS model tier. Returns ALLOW / DEFER / BLOCK. Use when implementing any new feature during a CONDITIONAL_GO build phase to verify it is in scope."
argument-hint: "[feature description]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-scope-guard

개발 중 범위 이탈 차단 게이트.
새 기능 요청이 CONDITIONAL_GO 허용 범위 안에 있는지 확인합니다.

## Instructions

You are running `/hplan-scope-guard` for: **$ARGUMENTS**

### Step 1 — 영구 제외 레지스트리 확인

```bash
python3 hplan/scripts/exclusions_registry.py check "$ARGUMENTS"
```

- **COLLISION** (reopen_trigger 미충족) → 즉시 **BLOCK** 출력 후 종료
- CLEAR → 다음 단계로

### Step 2 — CONDITIONAL_GO 허용 범위 확인

```bash
python3 -c "
import json, pathlib
cp = pathlib.Path('harness/build-gate/checkpoint.json')
if not cp.exists():
    print('NO_CHECKPOINT')
else:
    d = json.loads(cp.read_text())
    decision = d.get('decision', 'GO')
    allowed = d.get('allowed_paths') or []
    conditions = d.get('conditions') or []
    print(f'DECISION={decision}')
    print(f'ALLOWED={allowed}')
    print(f'CONDITIONS={conditions}')
"
```

판단 로직:
- `decision == "GO"` → allowed_paths 제약 없음. Step 3으로.
- `decision == "CONDITIONAL_GO"` + `allowed_paths` 비어 있음 → 제약 없음. Step 3으로.
- `decision == "CONDITIONAL_GO"` + `allowed_paths` 존재 → `$ARGUMENTS`가 허용 경로와 관련성 있는지 판단.
  - 관련성 있으면 → Step 3으로.
  - 관련성 없으면 → **DEFER** 출력: "이 기능은 CONDITIONAL_GO 허용 범위 밖입니다. V2+ 또는 다음 Build Gate 이후로 이연합니다."

### Step 3 — COGS 티어 영향 확인

`$ARGUMENTS`에서 아래 신호를 탐지:
- 새 외부 API 호출 추가 (예: Gemini, GPT-4o, Anthropic, Neo4j 쿼리 증가)
- 현재 `checkpoint.json`에 없는 새 provider 또는 모델 등장
- 사용자당 호출 횟수 증가를 유발하는 피처

신호가 감지되면:
1. 현재 COGS 파라미터를 `checkpoint.json`에서 읽기
2. 새 피처가 p90 margin에 미치는 영향 추정 (정성적)
3. 영향 있으면 경고 포함 ALLOW 또는 DEFER 출력

COGS 티어 변화 없으면 → **ALLOW**.

### Step 4 — V2+ 분류

**DEFER** 판정된 기능은 다음 형식으로 기록 제안:

```
이 기능을 V2+로 분류합니다:
  기능: [feature description]
  이유: [CONDITIONAL_GO 범위 외 / COGS 영향]
  재검토 조건: [다음 Build Gate 통과 또는 특정 지표 달성]
```

사용자 확인 후 `harness/v2-backlog.md`에 추가 (파일 없으면 생성).

## Output Format

```
hplan-scope-guard — [날짜]
대상: [feature description]

레지스트리: CLEAR / COLLISION
허용 범위:  IN_SCOPE / OUT_OF_SCOPE / NO_CONSTRAINT
COGS 티어:  UNCHANGED / WARNING([예상 증가분])

판정: ALLOW / DEFER / BLOCK
이유: [한 줄]
```

## 판정 기준

| 판정 | 의미 | 다음 행동 |
|------|------|----------|
| **ALLOW** | 현재 게이트 범위 내. 구현 진행 가능 | 바로 구현 |
| **DEFER** | 범위 외 또는 COGS 영향. V2+로 이연 | `harness/v2-backlog.md`에 기록 |
| **BLOCK** | 영구 제외 레지스트리 충돌 | 구현 금지. 제외 항목 + reopen_trigger 확인 |

## 주의

- 이 커맨드는 `gate_guard.py` (파일 쓰기 전 차단)와 **다른 시점**에 동작합니다.
  - `scope-guard` = 설계 시점 (구현 전)
  - `gate_guard` = 커밋 시점 (파일 쓰기 전)
- 두 레이어가 함께 작동하면 범위 이탈을 두 번 막습니다.
