---
name: parallel-team
description: "Plan a parallel agent team for independent tasks — partition work into ≥2 worktree-isolated branches, dispatch agents concurrently, and merge with conflict-prevention rules. Use when ≥2 tasks share zero file overlap, when wall-clock time matters, or when superpowers:dispatching-parallel-agents skill is invoked. Distinct from architect/orchestration (runtime parallelism) and harness-design (full build orchestration)."
argument-hint: "[task list to parallelize]"
allowed-tools: ["Read", "Write", "Edit", "Bash"]
model: sonnet
---

## Core Goal

- 독립적으로 분리 가능한 ≥2 작업을 **병렬 에이전트 팀**으로 처리한다.
- 각 에이전트는 **worktree 격리**로 충돌 방지.
- 동일 파일 수정 작업은 병렬 금지 (직렬화).

---

## Trigger Gate

### Use This Skill When
- 독립 작업 ≥2개 (파일 겹침 없음)
- Wall-clock 시간 단축이 가치 있을 때
- `superpowers:dispatching-parallel-agents` 스킬 호출 시
- 같은 디렉토리 변경 없는 다중 모듈 작업

### Route to Other Skills When
- 단일 작업 또는 순차 의존 → `deliver/harness-design`
- 발견→PRD→구현 전체 → `deliver/build-loop`
- 런타임 병렬 (에이전트 실행 시) → `architect/orchestration` Parallel 패턴

### Boundary Checks
- 같은 파일을 두 작업이 수정하면 병렬 금지
- 의존 그래프가 있으면 (A 끝나야 B 시작) 병렬 금지
- 단일 작업은 worktree 격리 비용 > 이득

---

## Instructions

You are partitioning: **$ARGUMENTS**

**Step 1 — 작업 분해**
- 입력 요청을 N개 작업으로 분해
- 각 작업의 입출력·수정 파일 명시

**Step 2 — 독립성 검증**
- 작업 쌍 (Ai, Aj)별 파일 충돌 확인
- 충돌 있으면 직렬화 또는 병합 책임 명시

**Step 3 — Worktree 배치**
- 각 독립 작업 = 1개 worktree
- 경로: `.worktrees/<task-name>`
- 베이스: 공통 시작 브랜치 (`main` 또는 직전 통합 브랜치)
- `.gitignore`에 `.worktrees/` 추가

**Step 4 — 디스패치**
- 한 메시지에서 N개 에이전트 동시 호출
- 각 에이전트에 `isolation: "worktree"` 파라미터
- 각 에이전트는 자기 worktree에서만 작업

**Step 5 — 병합 전략**
- 모든 worktree 완료 → 순차 머지 (충돌 0건이어야 함)
- 충돌 발생 시 분해가 잘못됨 → Step 1 재실행

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| 작업 분해가 같은 파일 수정 | Step 2에서 충돌 검출 | 직렬화 또는 분해 재설계 |
| `.worktrees` 미존재 | 디렉토리 부재 | 자동 생성 + `.gitignore` 추가 |
| 머지 시 충돌 발생 | git merge conflict | Step 1 재검토 — 독립성 잘못 평가됨 |
| 한 에이전트 실패 | 1개 worktree 실패 | 해당만 재시도, 다른 worktree는 그대로 유지 |

---

## Quality Gate

- [ ] 작업 ≥2개, 모두 파일 충돌 없음
- [ ] 각 작업이 별도 worktree에 격리되었는가
- [ ] `.gitignore`에 `.worktrees/` 포함
- [ ] 모든 에이전트 호출에 `isolation: "worktree"` 명시
- [ ] 머지 전략이 명시되었는가

---

## Examples

### Good Example
**입력:** "백엔드 API 3개(인증/주문/배송) 추가. 라우터·핸들러·테스트 분리되어 있어."

**기대 출력:**
- 작업 A: 인증 (`src/auth/*`)
- 작업 B: 주문 (`src/order/*`)
- 작업 C: 배송 (`src/shipping/*`)
- 충돌 검증: 0건
- worktree:
  - `.worktrees/auth`
  - `.worktrees/order`
  - `.worktrees/shipping`
- 3개 에이전트 동시 디스패치 (단일 메시지)
- 머지 순서: auth → order → shipping (의미 의존도 순)

### Bad Example
**입력:** "main.py 리팩터링하고 거기에 새 함수 3개 추가."

**왜 나쁜가:**
- 한 파일(`main.py`)에서 3개 작업이 모두 충돌
- 병렬 부적합 → 직렬 처리 권고

---

## Contextual Knowledge (auto-loaded)

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Worktree Patterns
!`cat references/worktree-patterns.md 2>/dev/null || echo ""`
