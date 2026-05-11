# AI_PM_Skills — Todolist

> v1.0 기준 남은 작업 정리
> 최종 업데이트: 2026-03-07

---

## ✅ 완료 (archived)

<details>
<summary>Phase 1-3 + v1.0 (모두 완료 — 접기)</summary>

### Phase 1: 구조 마이그레이션 ✅
- [x] 5개 plugin.json 변환
- [x] 12개 command frontmatter 정리
- [x] 24개 스킬 argument-hint + description 200자+ 보강

### Phase 2: Description 최적화 ✅
- [x] 96 trigger eval queries 작성
- [x] 97.9% trigger accuracy (94/96)
- [x] opp-tree description 개선 (307→646자)

### Phase 3: 테스트 & Eval ✅
- [x] 10 evals, 54 assertions — with-skill 100% vs without-skill 88%
- [x] benchmark.json + eval-review.html

### v1.0: 구조 업그레이드 ✅
- [x] 32개 기존 스킬 v1.0 구조 적용 (Core Goal, Trigger Gate, Failure Handling, Quality Gate, Examples)
- [x] 3개 신규 스킬 생성 (infographic-gif-creator, pptx-ai-slide, agent-demo-video)
- [x] validate_plugins.py: 5 plugins, 35 skills, 12 commands, 0 errors
- [x] 문서 전체 업데이트 (README ×2, CONTRIBUTING, GUIDE-ko, CHANGELOG, progress)

</details>

---

## 🔄 Phase 4: 배포 준비

### 4.1 Git 정리 (로컬 수동 작업)
- [ ] `.git/index.lock` 해제: `rm .git/index.lock`
- [ ] 기존 PLUGIN.md 삭제: `rm -f oracle/PLUGIN.md atlas/PLUGIN.md forge/PLUGIN.md argus/PLUGIN.md muse/PLUGIN.md`
- [ ] 구 디렉토리 삭제: `rm -rf pm-agent-* pm-engine`
- [ ] 내부 기획문서 제거: `rm -f PROJECT.md REFERENCE-ANALYSIS.md`
- [ ] 임시 스크립트 제거: `rm -f cleanup-and-commit.sh`

### 4.2 plugin.json 버전 업데이트
- [ ] 5개 plugin.json version `"0.3.0"` → `"1.0.0"`
- [ ] marketplace.json version 업데이트

### 4.3 GitHub 배포
- [ ] 최종 커밋 & push
- [ ] GitHub Release 생성 (v1.0.0)

---

## ⬜ Phase 5: 지속 개선 (Post-Launch)

### 5.1 벤치마크 재측정
- [ ] 35 스킬 기준 trigger eval 재실행 (신규 3개 스킬 eval 추가 필요)
- [ ] quality eval iteration-2 실행 (필요 시)

### 5.2 모델 업데이트 대응
- [ ] Claude 모델 업데이트 시 eval 재실행
- [ ] capability uplift 스킬 vs encoded preference 스킬 분류
- [ ] 불필요해진 스킬 식별 및 아카이브

### 5.3 커뮤니티 피드백
- [ ] GitHub Issues 모니터링
- [ ] 신규 스킬 요청 수집 및 우선순위화
- [ ] 분기별 벤치마크 리포트
