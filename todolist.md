# AI_PM_Skills — Improvement Todolist

> 공식 Claude Skill/Plugin 스펙 + Skill Creator 블로그 기반 개선 계획
> 작성일: 2026-03-06

---

## Phase 1: 구조 마이그레이션 (Plugin Spec 준수)

### 1.1 Plugin 매니페스트 변환
- [x] `oracle/PLUGIN.md` → `oracle/.claude-plugin/plugin.json` 변환
- [x] `atlas/PLUGIN.md` → `atlas/.claude-plugin/plugin.json` 변환
- [x] `forge/PLUGIN.md` → `forge/.claude-plugin/plugin.json` 변환
- [x] `argus/PLUGIN.md` → `argus/.claude-plugin/plugin.json` 변환
- [x] `muse/PLUGIN.md` → `muse/.claude-plugin/plugin.json` 변환
- [ ] 기존 PLUGIN.md 파일 삭제 (로컬에서 수동 삭제 필요)

### 1.2 Command frontmatter 정리
- [x] 비공식 `skills:` 필드 제거 (12개 command 파일)
- [x] 공식 지원 필드만 유지: `name`, `description`
- [x] command 내부에서 스킬 참조 방식을 본문 Instructions으로 이동

### 1.3 SKILL.md frontmatter 보강
- [x] `$ARGUMENTS` 사용 스킬에 `argument-hint` 필드 추가 (24/24)
- [x] atlas/argus 계열 description 200자+ 보강 (11/11)
- [ ] 수동 전용 스킬에 `disable-model-invocation: true` 검토 (Phase 3에서 eval 후 판단)

---

## Phase 2: Description 최적화 (트리거 정확도)

### 2.1 Description 보강 — 짧은 description 수정
- [x] atlas 계열 6개 스킬 description 보강 (Phase 1에서 완료)
- [x] argus 계열 5개 스킬 description 보강 (Phase 1에서 완료)
- [x] 모든 description에 "Use when..." 트리거 패턴 추가 (Phase 1에서 완료)

### 2.2 Description 최적화 루프 (Skill Creator 도구 활용)
- [x] 스킬별 trigger eval queries 작성 — 96 queries (24 skills × 4 each)
- [x] `run_eval.py`로 baseline eval 실행 — **97.9% (94/96)** 통과
- [x] 유일한 실패 스킬 `opp-tree` description 개선 (307자 → 646자)
- [x] 최적화된 description 적용 및 before/after 비교
- [ ] (Optional) `run_loop.py` 전체 최적화 — ANTHROPIC_API_KEY 필요, 로컬에서 실행 권장

---

## Phase 3: 테스트 & Eval 프레임워크

### 3.1 Eval 기반 구축
- [x] `evals/evals.json` 생성 — 5 대표 스킬 × 2 prompts = 10 evals, 54 assertions
- [x] 각 테스트에 expected_output + expectations 기술
- [x] workspace 디렉토리 구조 설정 (`eval-workspace/iteration-1/`)

### 3.2 테스트 실행 & 평가
- [x] 스킬별 with-skill / without-skill 병렬 실행 (20 runs 완료)
- [x] grading 실행 — 20개 grading.json 생성
- [x] benchmark.json 생성 — with_skill 100% vs without_skill 88% (+12%)
- [x] eval-viewer HTML 생성 (eval-review.html, 237KB)

### 3.3 반복 개선
- [ ] 유저 피드백 기반 스킬 개선 (필요 시)
- [ ] iteration-2 실행 및 비교 (필요 시)

---

## Phase 4: 배포 준비

### 4.1 패키징
- [ ] 각 플러그인 `.skill` 파일로 패키징
- [ ] 설치 테스트 (로컬 Claude Code 환경)

### 4.2 GitHub 배포
- [ ] 구 디렉토리 삭제 (pm-agent-*, pm-engine)
- [ ] 내부 기획문서 제거 (PROJECT.md, REFERENCE-ANALYSIS.md)
- [ ] 최종 커밋 & push
- [ ] GitHub Release 생성 (v1.0.0)

### 4.3 문서 최종 검수
- [ ] README.md 공식 스펙 반영 업데이트
- [ ] README-ko.md 동기화
- [ ] CONTRIBUTING.md에 eval 가이드 추가

---

## Phase 5: 지속 개선 (Post-Launch)

### 5.1 모델 업데이트 대응
- [ ] Claude 모델 업데이트 시 eval 재실행
- [ ] capability uplift 스킬 vs encoded preference 스킬 분류
- [ ] 불필요해진 스킬 식별 및 아카이브

### 5.2 커뮤니티 피드백
- [ ] GitHub Issues 모니터링
- [ ] 신규 스킬 요청 수집 및 우선순위화
- [ ] 분기별 벤치마크 리포트

