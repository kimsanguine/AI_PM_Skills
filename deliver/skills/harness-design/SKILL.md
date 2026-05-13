---
name: harness-design
description: "Design the build harness for an agent project — a 4+ agent team, an autonomous Ralph Loop, dry-run + backup gates, and pending-input batching. Use when scope crosses a single PR's worth of work, when implementation requires iterative self-correction, or when the user has approved 'autonomous mode' (ralph loop) with question-free batching. Strictly distinct from architect/orchestration which designs the runtime system, not the build process."
argument-hint: "[project or feature to build]"
allowed-tools: ["Read", "Write", "Edit"]
model: sonnet
---

## Core Goal

- 빌드 자체의 **하네스(harness)**를 설계한다 — 누가, 어떤 순서로, 어떤 안전망과 함께 코드를 짤지.
- 4명 이상의 에이전트 팀 + Ralph Loop 자율 모드 + 백업 + dry-run + pending-input 배치를 표준화.
- 큰 스코프의 작업이 사람 1명의 1세션으로 완성되지 않을 때 적용.

---

## 하네스 5요소

| 요소 | 역할 | 표준 패턴 |
|---|---|---|
| **Team** | ≥4명 에이전트 (Lead + Builder + Reviewer + Verifier) | 역할별 SKILL 분리, worktree 격리 |
| **Loop** | Ralph Loop 자율 반복 | 1회 실패 → 즉시 중단, 3회 성공 → 다음 단계 |
| **Backup** | 변경 전 스냅샷 | git branch + 디렉토리 tar |
| **Dry-run** | 실제 적용 전 plan diff | `--dry-run` 플래그 표준 |
| **Pending-input batching** | 질문 모아 한 번에 결정 | 자율 모드에서 질문 금지, batch 결정 |

---

## Trigger Gate

### Use This Skill When
- 스코프가 한 PR 이상이고, 여러 모듈/디렉토리 수정
- 자기 수정 반복이 필요한 작업(빌드 → 테스트 → 수정 → 재빌드)
- 사용자가 "ralph loop로 진행", "자율 모드" 등으로 자율 실행 승인
- 4명 이상 에이전트가 협업해야 효율적

### Route to Other Skills When
- 독립 태스크 ≥2 → `deliver/parallel-team` (worktree 분기)
- 발견→PRD→구현 전체 루프면 → `deliver/build-loop`
- 런타임 에이전트 아키텍처는 → `architect/orchestration`
- 단일 에이전트 PRD는 → `deliver/prd`

### Boundary Checks
- 단일 파일 수정·1시간 이내 작업은 하네스 과중 — 직접 작업
- "팀"은 런타임 에이전트가 아니라 **빌드 시 협업 에이전트**임을 분리

---

## Instructions

You are designing a harness for: **$ARGUMENTS**

**Step 1 — 스코프 점검**
- 1 PR 이내인가? → 하네스 불필요, 직접 작업
- N개 모듈 이상이면 하네스 적용

**Step 2 — Team 편성**
- Lead 1명 (조율 + 결정)
- Builder ≥2명 (병렬 가능 시 worktree 격리)
- Reviewer 1명 (코드 리뷰 + 일관성)
- Verifier 1명 (테스트 + smoke run)

**Step 3 — Loop 설계**
- 반복 단위: "구현 → 테스트 → 자기 검토 → 다음"
- 자율 모드: 1회 실패 즉시 중단 + 사용자 알림
- 3회 연속 성공: 자동 다음 단계 진입

**Step 4 — Safety Gates**
- 시작 전 `git branch backup/<task>` + `tar -czf backup-<ts>.tgz`
- 변경 전 모든 변환은 `--dry-run` 출력으로 사용자 확인
- 자율 모드에서 사용자 결정 필요 항목은 `pending_inputs.md`에 누적

**Step 5 — 종료 조건**
- 완성 정의: 테스트 통과 + Reviewer OK + Verifier OK
- 미해결 pending_inputs는 사용자에게 한 번에 전달

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| 자율 모드에서 결정 막힘 | 1회 실패 발생 | 즉시 중단 + pending_inputs 요약 사용자에게 |
| 백업 누락 | 변경 시작 전 backup 미생성 | 작업 차단 + git branch + tar 강제 |
| Builder 두 명이 같은 파일 수정 | worktree 미사용 | parallel-team 스킬 라우팅 |
| Loop가 무한 회전 | 같은 실패 ≥2회 | 자동 중단 + 사용자 호출 |

---

## Quality Gate

- [ ] Team 4명 이상이 명시되었는가 (역할별)
- [ ] Loop 반복 단위·종료 조건이 명시되었는가
- [ ] 백업 + dry-run 게이트가 적용되었는가
- [ ] pending_inputs 누적 위치가 정의되었는가
- [ ] 자율 모드에서 질문 금지 규칙이 명시되었는가

---

## Examples

### Good Example
**입력:** "랜딩 페이지 디자인 시스템 5개 컴포넌트 + 다크모드 + 12개 페이지 갱신. ralph loop로 진행."

**기대 출력:**
- Team: Lead + Builder×3 (컴포넌트/다크모드/페이지) + Reviewer + Verifier
- 3개 Builder는 worktree 격리 (`.worktrees/comp`, `/dark`, `/pages`)
- Loop: 구현 → 단위 테스트 → 시각 검사 (Playwright) → 다음
- 백업: `git branch backup/landing-redesign` + `tar landing-snapshot-{ts}.tgz`
- pending_inputs: `.claude/pending_inputs.md`에 누적, 종료 시 한 번에 전달

### Bad Example
**입력:** "한 줄 typo 고쳐."

**왜 나쁜가:**
- 스코프 단일 라인 → 하네스 과중
- 직접 Edit으로 끝낼 작업

---

## Contextual Knowledge (auto-loaded)

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Ralph Loop Spec
!`cat references/ralph-loop-spec.md 2>/dev/null || echo ""`
