# AI_PM_Skills — Progress Log

> 각 Phase 진행 상황을 기록합니다.
> 최종 업데이트: 2026-03-06

---

## 현재 상태: v1.0 완료 → Phase 4 (배포 준비) 진행 중

| Phase | 상태 | 진행률 | 비고 |
|-------|------|--------|------|
| Phase 0: v0.3 콘텐츠 작성 | ✅ 완료 | 100% | 24 skills, 12 commands, 5 plugins |
| Phase 0.5: 리네이밍 | ✅ 완료 | 100% | Oracle/Atlas/Forge/Argus/Muse |
| Phase 1: 구조 마이그레이션 | ✅ 완료 | 100% | plugin.json + frontmatter 정리 완료 |
| Phase 2: Description 최적화 | ✅ 완료 | 100% | 97.9% trigger accuracy (94/96) |
| Phase 3: 테스트 & Eval | ✅ 완료 | 100% | with_skill 100% vs without_skill 88% (+12%) |
| **v1.0: 구조 업그레이드** | **✅ 완료** | **100%** | **35 skills + v1.0 구조 전체 적용** |
| Phase 4: 배포 준비 | 🔄 진행 중 | 50% | 문서 업데이트 완료, Git 배포 대기 |
| Phase 5: 지속 개선 | ⬜ 미시작 | 0% | Post-Launch |

---

## Phase 0: v0.3 콘텐츠 작성 ✅

**완료일:** 2026-03-06

### 작업 내역
- 5개 플러그인 생성: oracle, atlas, forge, argus, muse
- 24개 SKILL.md 작성 (한글 개념 + 영문 Instructions)
- 12개 Command 작성 (멀티스킬 체이닝 워크플로우)
- 신화 네이밍 적용 (Oracle/Atlas/Forge/Argus/Muse)
- 짧은 skill명 적용 (opp-tree, 3-tier, premortem 등)
- README.md (EN) + README-ko.md (KO) 분리
- CONTRIBUTING.md 작성
- .gitignore 작성

### 검증 결과
- 24/24 스킬 이름 일관성 통과
- 5/5 PLUGIN.md ↔ 디렉토리 매핑 일치
- 12/12 Command 파일 존재 확인

### 알려진 이슈
- 구 디렉토리 미삭제 (pm-agent-*, pm-engine) — 로컬에서 수동 삭제 필요
- PROJECT.md, REFERENCE-ANALYSIS.md 내부 기획문서 미삭제
- cleanup-and-commit.sh 임시 스크립트 미삭제

---

## Phase 0.5: 공식 스펙 갭 분석 ✅

**완료일:** 2026-03-06

### 발견된 갭

#### 🔴 구조적 문제 (3건)
1. **Plugin 매니페스트 형식 불일치**: PLUGIN.md (YAML) → .claude-plugin/plugin.json (JSON) 필요
2. **Command frontmatter 비공식 필드**: `skills:` 필드는 공식 지원 아님
3. **유용한 frontmatter 필드 미사용**: `allowed-tools`, `argument-hint`, `disable-model-invocation`

#### 🟡 개선 기회 (2건)
4. **Description 트리거 키워드 부족**: atlas/argus 계열 100~131자로 짧음, "Use when..." 패턴 필요
5. **테스트/Eval 부재**: eval pass rate, elapsed time, token usage 측정 미설정

### 참고 자료
- Claude Code Skills 공식 문서: https://code.claude.com/docs/en/skills.md
- Claude Code Plugins 스펙: https://code.claude.com/docs/en/plugins-reference.md
- Skill Creator 블로그: https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills

---

## Phase 1: 구조 마이그레이션 ✅

**완료일:** 2026-03-06

### Step 1.1: Plugin 매니페스트 변환
| 플러그인 | .claude-plugin/plugin.json | PLUGIN.md 처리 |
|----------|---------------------------|----------------|
| oracle | ✅ | ✅ deprecated 표시 (로컬 삭제 필요) |
| atlas | ✅ | ✅ deprecated 표시 (로컬 삭제 필요) |
| forge | ✅ | ✅ deprecated 표시 (로컬 삭제 필요) |
| argus | ✅ | ✅ deprecated 표시 (로컬 삭제 필요) |
| muse | ✅ | ✅ deprecated 표시 (로컬 삭제 필요) |

### Step 1.2: Command frontmatter 정리
- ✅ 12/12 command에서 비공식 `skills:` 필드 제거
- ✅ command 본문에서 스킬 참조 방식으로 전환
- ✅ description에 "Use when..." 트리거 패턴 추가

### Step 1.3: SKILL.md frontmatter 보강
| 항목 | 대상 수 | 완료 수 |
|------|---------|---------|
| argument-hint 추가 | 24 | 24 ✅ |
| description 200자+ 보강 | 11 (atlas+argus) | 11 ✅ |
| 전체 description 200자+ | 24 | 24 ✅ |

### 검증 결과
- 5/5 plugin.json valid JSON ✅
- 12/12 command frontmatter clean ✅
- 24/24 skills have argument-hint ✅
- 24/24 skills description 200+ chars ✅

### 로컬에서 수동 삭제 필요
```bash
cd ~/Documents/3_Code/Vibe/Project/260306_AgentSkills
rm -f oracle/PLUGIN.md atlas/PLUGIN.md forge/PLUGIN.md argus/PLUGIN.md muse/PLUGIN.md
```

---

## Phase 2: Description 최적화 ✅

**완료일:** 2026-03-06

### Step 2.1: Description 보강 (Phase 1에서 선완료)
- ✅ atlas 계열 6개 + argus 계열 5개 = 11개 스킬 description 200자+ 보강
- ✅ 전체 24개 스킬 "Use when..." 트리거 패턴 추가

### Step 2.2: Trigger Eval 기반 최적화

#### Eval 인프라 구축
- ✅ `evals/trigger-evals.json` — 96 queries (24 skills × 4 queries)
  - 각 스킬당 should-trigger 2개 + should-not-trigger 2개
  - 한국어/영어 혼합 쿼리, 실제 PM 시나리오 기반
- ✅ `evals/per-skill/*.json` — 스킬별 분리된 eval 파일 24개
- ✅ `evals/baseline-results.json` — 전체 baseline 결과

#### Baseline Eval 결과
| 플러그인 | 스킬 | Passed | Total | 결과 |
|----------|------|--------|-------|------|
| oracle | opp-tree | 2 | 4 | ⚠️ (개선 후 3/4) |
| oracle | assumptions | 4 | 4 | ✅ |
| oracle | build-or-buy | 4 | 4 | ✅ |
| oracle | hitl | 4 | 4 | ✅ |
| oracle | cost-sim | 4 | 4 | ✅ |
| atlas | 3-tier | 4 | 4 | ✅ |
| atlas | orchestration | 4 | 4 | ✅ |
| atlas | biz-model | 4 | 4 | ✅ |
| atlas | router | 4 | 4 | ✅ |
| atlas | memory-arch | 4 | 4 | ✅ |
| atlas | moat | 4 | 4 | ✅ |
| forge | instruction | 4 | 4 | ✅ |
| forge | prd | 4 | 4 | ✅ |
| forge | prompt | 4 | 4 | ✅ |
| forge | ctx-budget | 4 | 4 | ✅ |
| forge | okr | 4 | 4 | ✅ |
| argus | kpi | 4 | 4 | ✅ |
| argus | reliability | 4 | 4 | ✅ |
| argus | premortem | 4 | 4 | ✅ |
| argus | burn-rate | 4 | 4 | ✅ |
| argus | north-star | 4 | 4 | ✅ |
| muse | pm-framework | 4 | 4 | ✅ |
| muse | pm-decision | 4 | 4 | ✅ |
| muse | pm-engine | 4 | 4 | ✅ |
| **총합** | | **94** | **96** | **97.9%** |

#### opp-tree 개선 내역
- **Before**: "Build an Agent Opportunity Tree to structure AI agent discovery..." (307자)
- **After**: "Analyze where AI agents can add value and which tasks to automate..." (646자)
- **개선 포인트**: 범용 트리거 키워드 추가 (repetitive workflows, automation opportunities, any domain)
- **한계**: 범용 쿼리에서 trigger rate 40-67% — 스킬 발동보다 직접 답변 경향 (단독 스킬 eval 특성)

#### 실행 환경
- `claude` CLI v2.1.51 (env -u CLAUDECODE로 nesting 우회)
- `run_eval.py` from skill-creator scripts
- runs_per_query=1 (baseline), 3-5 (optimization)
- 총 소요 시간: ~7분 (baseline) + ~5분 (opp-tree iterations)

---

## Phase 3: 테스트 & Eval ✅

**완료일:** 2026-03-06

### Step 3.1: Eval 프레임워크 구축
- ✅ `evals/evals.json` — 10개 테스트 프롬프트 (5 대표 스킬 × 2 prompts)
- ✅ 5개 대표 스킬 선정: cost-sim(oracle), 3-tier(atlas), prd(forge), premortem(argus), pm-framework(muse)
- ✅ eval당 5~6개 expectations (총 54개 assertions)
- ✅ `eval-workspace/iteration-1/` 디렉토리 구조 생성

### Step 3.2: With/Without Skill 비교 실행
- ✅ 20개 eval 실행 완료 (10 evals × 2 configs)
- ✅ 병렬 실행: 4개 subagent 동시 실행으로 ~10분 완료

### Step 3.3: Grading & Benchmark

#### Benchmark 요약
| 설정 | Pass Rate (mean) | Pass Rate (range) | Time (mean) |
|------|-----------------|-------------------|-------------|
| **with_skill** | **100%** | 100%-100% | 62.1s |
| **without_skill** | **88%** | 40%-100% | 41.7s |
| **Delta** | **+12%** | — | +20.5s |

#### Eval별 상세 결과
| Eval | Skill | Plugin | With Skill | Without Skill | Delta |
|------|-------|--------|-----------|--------------|-------|
| 1. cost-sim-saas-chatbot | cost-sim | oracle | 5/5 (100%) | 5/5 (100%) | 0% |
| 2. cost-sim-doc-agent | cost-sim | oracle | 5/5 (100%) | 5/5 (100%) | 0% |
| 3. 3-tier-research-system | 3-tier | atlas | 5/5 (100%) | 3/5 (60%) | **+40%** |
| 4. 3-tier-ecommerce-ops | 3-tier | atlas | 5/5 (100%) | 4/5 (80%) | **+20%** |
| 5. prd-onboarding-agent | prd | forge | 6/6 (100%) | 6/6 (100%) | 0% |
| 6. prd-code-review-agent | prd | forge | 6/6 (100%) | 6/6 (100%) | 0% |
| 7. premortem-support-agent | premortem | argus | 6/6 (100%) | 6/6 (100%) | 0% |
| 8. premortem-content-moderation | premortem | argus | 6/6 (100%) | 6/6 (100%) | 0% |
| 9. pm-framework-scope-creep | pm-framework | muse | 5/5 (100%) | 5/5 (100%) | 0% |
| 10. pm-framework-user-research-lesson | pm-framework | muse | 5/5 (100%) | 2/5 (40%) | **+60%** |

#### 핵심 발견
1. **Capability-Gating 스킬** (without_skill에서 실패):
   - `pm-framework` (TK 유닛): 스킬 없이는 "TK unit"이 뭔지 모름 → 40% pass rate
   - `3-tier` (Prometheus-Atlas-Worker): 스킬 없이는 communication protocol, delegation strategy 누락 → 60-80%

2. **Baseline-Strong 스킬** (스킬 없이도 100%):
   - `cost-sim`: 비용 계산은 base model이 잘 처리
   - `prd`: 에이전트 PRD 구조를 base model도 합리적으로 생성
   - `premortem`: FMEA 방법론은 잘 알려진 프레임워크

3. **질적 차이** (pass rate에 미반영):
   - `cost-sim` with_skill: context accumulation cost까지 고려 (+46.6% output)
   - `3-tier` with_skill: 5.4-20.1× 더 상세한 output
   - `premortem` with_skill: 최대 +102% output depth

### Step 3.4: Eval Viewer
- ✅ `eval-workspace/iteration-1/eval-review.html` — 237KB 자기완결형 HTML viewer
- ✅ `eval-workspace/iteration-1/benchmark.json` — 구조화된 벤치마크 데이터
- ✅ 20개 `grading.json` 파일 — 개별 채점 결과

---

## v1.0: 구조 업그레이드 ✅

**완료일:** 2026-03-07

### v1.0 구조 전환
- ✅ 기존 32개 스킬 전체 v1.0 구조 적용 (Core Goal, Trigger Gate, Failure Handling, Quality Gate, Examples)
- ✅ cost-sim을 v1.0 템플릿으로 선정 → 나머지 31개에 병렬 적용
- ✅ 교육적 Concept/Instructions 콘텐츠 100% 보존 (하이브리드 구조)
- ✅ 32/32 구조 검증 통과

### 신규 스킬 3개 (forge 플러그인)
| 스킬 | 출처 | 변경 사항 |
|------|------|----------|
| `infographic-gif-creator` | Vibe/Skills → 에이전트 PM 맥락으로 재작성 | HTML/CSS → GIF/MP4 인포그래픽 파이프라인 |
| `pptx-ai-slide` | Vibe/Skills (Alan 의존성 제거) | 에이전트 프레젠테이션 덱 범용화 |
| `agent-demo-video` | Vibe/Skills remotion → 에이전트 데모 영상으로 재구성 | Remotion 기반 5단계 스토리라인 |

### 검증
- ✅ validate_plugins.py: 5 plugins, 35 skills, 12 commands, 0 errors, 0 warnings
- ✅ forge plugin.json 업데이트 (description + keywords)

### 문서 업데이트
- ✅ README.md / README-ko.md (뱃지, Status, forge 상세, File Structure, Skill Origin)
- ✅ CONTRIBUTING.md (v1.0 SKILL.md 포맷 가이드)
- ✅ GUIDE-ko.md (forge 11개, 전체 35개)
- ✅ "What Makes This Different" 섹션 6 추가 (v1.0 구조적 엄밀함)
- ✅ CHANGELOG.md 신규 작성
- ✅ progress.md v1.0 Phase 기록

---

## Phase 4: 배포 준비

**상태:** 🔄 진행 중

### 완료
- ✅ 문서 전체 업데이트

### 남은 작업
- [ ] 구 디렉토리 삭제 (pm-agent-*, pm-engine)
- [ ] 내부 기획문서 제거 (PROJECT.md, REFERENCE-ANALYSIS.md)
- [ ] `.git/index.lock` 해제 (로컬에서 수동)
- [ ] 최종 커밋 & push
- [ ] GitHub Release v1.0.0

---

## Phase 5: 지속 개선

**상태:** ⬜ 미시작

(Post-Launch)

