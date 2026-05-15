# PROGRESS — [Product Name]

> `/hplan-build` Build Gate 출력 시 자동 생성됩니다.
> 각 마일스톤(Wx) 시작 전에 "시작 전 체크" 블록을 채우세요.
> `harness/STATE.md`의 조건 anchor와 연동됩니다.

Generated: YYYY-MM-DD
Decision: CONDITIONAL_GO | GO
Decision ID: dec-YYYY-MM-DD-XXXXX

---

## W1 — [마일스톤 이름]

> **시작 전 체크** (시작 전 모두 확인)
> - [ ] 조건: [STATE.md 조건 1] — `verified_by`: [파일 경로 — 기입 필요]
> - [ ] 기술 결정: [이 주에 결정해야 할 기술 선택]
> - [ ] COGS 추정: p50 [X]%, p90 [X]% at [N] calls/user/month
> - [ ] 블로커 해소: [이 마일스톤 진입 조건]

### 목표
- [ ] [W1에 완료할 핵심 1가지]

### 완료 기준
- 검증 파일 생성: `[verified_by path]`
- `/hplan-verify [조건 이름]` COMPLETE 판정

---

## W2 — [마일스톤 이름]

> **시작 전 체크**
> - [ ] 조건: [STATE.md 조건 2] — `verified_by`: [파일 경로]
> - [ ] W1 COMPLETE 판정 확인 (`/hplan-verify`)
> - [ ] COGS 추정 재확인 (W1 실측치 반영)

### 목표
- [ ] [W2에 완료할 핵심 1가지]

### 완료 기준
- 검증 파일 생성: `[verified_by path]`
- `/hplan-verify` COMPLETE 판정

---

## Wx — [추가 마일스톤]

> **시작 전 체크**
> - [ ] 이전 Wx COMPLETE 판정
> - [ ] STATE.md 조건 전부 ✅

---

## Build Gate 종료 조건

- [ ] 모든 Active 조건 ✅ (`/hplan-verify` COMPLETE)
- [ ] COGS sentinel 재실행 → GREEN
- [ ] 블로커 해소 전부 완료

종료 선언: `/hplan-build` 재실행으로 최종 GO 기록

---

<!-- hplan PROGRESS.md — 삭제하지 마세요 -->
<!-- STATE.md와 쌍으로 운영됩니다. STATE.md = 게이트 상태 / PROGRESS.md = 마일스톤 계획 -->
