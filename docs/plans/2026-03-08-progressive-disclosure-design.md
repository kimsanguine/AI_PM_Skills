# Progressive Disclosure 설계 — AgentSkills 실행 품질 향상

> 작성일: 2026-03-08
> 상태: Approved
> 작성자: Claude

---

## 1. 목표

기존 Skills 폴더(`~/3_Code/Vibe/Skills/`)의 Progressive Disclosure 전략을 AgentSkills 35개 스킬에 적용하여 **스킬 실행 품질을 향상**한다.

- 기존 SKILL.md 본문은 건드리지 않는다
- 보조 파일은 `!command`로 on-demand 로딩하여 토큰 효율을 유지한다
- 보조 파일이 없으면 기존과 동일하게 동작한다 (graceful degradation)

---

## 2. 보조 파일 5종 표준

### 2.1 `examples/good-01.md` (~20줄)

```markdown
# Good Example — {skill-name}

## 사용자 요청
"구체적인 사용자 발화 예시"

## 승인 이유
- 이 스킬의 Trigger Gate에 정확히 부합하는 이유 2~3줄

## 예상 처리
1. 스킬이 수행할 첫 번째 단계
2. 두 번째 단계
3. 예상 산출물
```

**역할**: 스킬이 "이렇게 동작해야 한다"는 golden path. Claude가 모호한 요청을 받았을 때 이 패턴에 맞춰 행동.

### 2.2 `examples/bad-01.md` (~15줄)

```markdown
# Bad Example — {skill-name}

## 사용자 요청
"이 스킬이 처리하면 안 되는 발화 예시"

## 거절 이유
- 스킬 경계를 벗어나는 이유

## 올바른 라우팅
- {정확한 대안 스킬 이름}으로 라우팅

## 수정 방향
- 요청을 이 스킬에 맞게 바꾸려면 어떻게 해야 하는지
```

**역할**: 트리거 오발동 방지. 유사 스킬 간 경계 구분.

### 2.3 `context/domain.md` (~30줄)

```markdown
# Domain Context — {skill-name}

## 1) Domain Scope
## 2) Primary Users
## 3) Required Inputs
## 4) Output Contract
## 5) Guardrails
## 6) Working Facts (수시 업데이트)
## 7) Fill-in Checklist
```

**역할**: 스킬이 암묵적으로 알아야 하는 도메인 지식. "왜 이런 결정을 했는가"의 배경 정보.

### 2.4 `references/test-cases.md` (~40줄)

```markdown
# Test Cases — {skill-name}

## 1) Trigger Tests
### Should Trigger (5)
### Should NOT Trigger (5)

## 2) Functional Tests (Given-When-Then) (3)

## 3) Error Cases (2)

## 4) With/Without Skill 비교 (1)
```

**역할**: `evals/per-skill/*.json`의 human-readable 버전. 스킬 실행 중 Claude가 참조하는 가이드.

### 2.5 `references/troubleshooting.md` (~20줄)

```markdown
# Troubleshooting — {skill-name}

## 1) {증상}
- 증상: ...
- 확인: ...
- 조치: ...
```

**역할**: 스킬 실행 중 자주 발생하는 문제 2~4개와 해결법.

---

## 3. 35개 스킬 등급 분류

### Tier 1 — Full (12개): 5종 전체

| Plugin | Skill | 핵심 사유 |
|--------|-------|-----------|
| forge | prd | command 체이닝, instruction 경계 충돌 |
| forge | instruction | prd 경계 충돌, 에이전트 설계 핵심 |
| forge | prompt | instruction과 범위 혼동 |
| forge | agent-plan-review | premortem 역할 구분 |
| forge | stakeholder-map | 도메인 컨텍스트 의존도 높음 |
| forge | pptx-ai-slide | 목적별 정보-디자인 밸런스, 딥리서치 스펙, 템플릿 체계 |
| oracle | assumptions | build-or-buy 겹침 |
| oracle | cost-sim | burn-rate 경계 충돌 |
| oracle | build-or-buy | assumptions 겹침, 6축 평가 |
| argus | premortem | agent-plan-review 역할 구분 |
| argus | reliability | premortem 경계 충돌 |
| muse | pm-engine | TK 추출 워크플로우 |

### Tier 2 — Standard (19개): examples + context

| Plugin | Skill | 핵심 사유 |
|--------|-------|-----------|
| oracle | opp-tree | /discover 체이닝 |
| oracle | hitl | 도메인 의존 |
| oracle | agent-gtm | GTM 전략 맥락 |
| forge | okr | /set-okr 체이닝 |
| forge | ctx-budget | 토큰 관리 도메인 |
| forge | gemini-image-flow | 파이프라인 아키텍처 |
| forge | agent-demo-video | 필수 정보/금지사항 도메인 규칙 |
| forge | infographic-gif-creator | 채널별 사이즈/배치/텍스트 규칙 |
| atlas | orchestration | 멀티에이전트 도메인 |
| atlas | memory-arch | 메모리 설계 도메인 |
| atlas | router | 라우팅 패턴 도메인 |
| atlas | growth-loop | 그로스 전략 도메인 |
| atlas | moat | 경쟁우위 분석 도메인 |
| atlas | 3-tier | 레이어 설계 도메인 컨텍스트 |
| atlas | biz-model | AI SaaS 비즈니스 모델 맥락 |
| argus | cohort | 데이터 분석 맥락 |
| argus | incident | 운영 도메인 |
| muse | pm-decision | 의사결정 프레임워크 맥락 |
| muse | pm-framework | 프레임워크 맥락별 선택 기준 |

### Tier 3 — Lite (4개): examples만

| Plugin | Skill | 사유 |
|--------|-------|------|
| argus | kpi | 지표 정의, 입력→출력 정형화 |
| argus | north-star | 단일 메트릭 도출, 경계 명확 |
| argus | burn-rate | 수치 계산 중심, 도메인 맥락 최소 |
| argus | agent-ab-test | 실험 설계 패턴 정형화 |

### 파일 수 요약

| 등급 | 스킬 수 | 스킬당 파일 | 총 신규 파일 |
|------|---------|------------|-------------|
| Tier 1 | 12 | 5 | 60 |
| Tier 2 | 19 | 3 | 57 |
| Tier 3 | 4 | 2 | 8 |
| **합계** | **35** | — | **125개** |

---

## 4. SKILL.md 로딩 패턴

기존 SKILL.md 본문 하단에 `## Contextual Knowledge (auto-loaded)` 섹션 추가.

### Tier 1

```markdown
## Contextual Knowledge (auto-loaded)

> 보조 파일이 존재할 때만 자동 로드됩니다. 파일이 없으면 건너뜁니다.

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Bad Example
!`cat examples/bad-01.md 2>/dev/null || echo ""`

### Domain Context
!`cat context/domain.md 2>/dev/null || echo ""`

### Test Cases
!`cat references/test-cases.md 2>/dev/null || echo ""`

### Troubleshooting
!`cat references/troubleshooting.md 2>/dev/null || echo ""`
```

### Tier 2

Good Example + Bad Example + Domain Context (3종)

### Tier 3

Good Example + Bad Example (2종)

---

## 5. 콘텐츠 생성 전략

### Step 1: 템플릿 + 디렉토리 생성 (자동)

35개 스킬에 Tier별 디렉토리 구조와 빈 템플릿 파일 생성.

### Step 2: SKILL.md에서 콘텐츠 자동 추출 (Claude 에이전트)

| 파일 | 추출 소스 | 자동화 가능성 |
|------|-----------|-------------|
| good-01.md | Trigger Gate → "Use This Skill When" + Examples | 90% |
| bad-01.md | Trigger Gate → "Route to Other Skills When" + Boundary | 90% |
| domain.md | Core Goal + Trigger Gate + Quality Gate | 70% |
| test-cases.md | evals/per-skill/*.json + Functional Tests | 80% |
| troubleshooting.md | Failure Handling 섹션 | 75% |

### Step 3: 사람 검수 + 도메인 지식 보강

- 실제 운영 경험 기반 예시 보강
- Working Facts (경쟁사, 시장 수치) 업데이트
- 채널/목적별 규칙 (pptx, infographic 등)
- 암묵지 반영

---

## 6. 실행 순서 (5 Sprints)

| Sprint | 범위 | 스킬 수 | 신규 파일 | 작업 |
|--------|------|---------|-----------|------|
| S1 | 파일럿 Tier 1 핵심 3개 | 3 | 15 | prd, instruction, cost-sim |
| S2 | Tier 1 나머지 | 9 | 45 | prompt ~ pm-engine |
| S3 | Tier 2 forge + oracle | 10 | 30 | 콘텐츠 스킬 포함 |
| S4 | Tier 2 atlas + argus + muse | 9 | 27 | 아키텍처 + 운영 |
| S5 | Tier 3 + 전체 검증 | 4 | 8 | Lite + eval 회귀 |

---

## 7. 설계 원칙

1. **기존 SKILL.md 본문 불변** — 하단에 로딩 블록만 추가
2. **Graceful degradation** — 보조 파일 없으면 기존과 동일 동작
3. **토큰 효율** — `!command` on-demand 로딩, 기본 +0 토큰
4. **점진적 품질 향상** — 파일 추가 시점부터 효과 발동
5. **기존 evals 호환** — 트리거 정확도 회귀 없음
