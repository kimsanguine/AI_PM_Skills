# ethan-agent-pm-skills
> AI 에이전트를 기획하고 운영하는 PM을 위한 오픈소스 스킬셋

**작성일**: 2026-03-06  
**작성자**: 클로 (with 이든)  
**상태**: 🟡 기획 중

---

## 📌 프로젝트 개요

### 한 줄 정의
> PM 20년의 암묵지를 AI 에이전트 스킬셋으로 변환한 오픈소스 프로젝트

### 포지셔닝
| | pm-skills (phuryn) | **ethan-agent-pm-skills** |
|---|---|---|
| 대상 | 일반 PM | AI 에이전트를 만드는 PM |
| 철학 | PM + AI 도구 | PM + AI 에이전트 설계/운영 |
| 기반 | Marty Cagan, Teresa Torres | 에이전트 오케스트레이션 + PM 암묵지 |
| 플랫폼 | Claude Code / Cowork | OpenClaw + Claude Code (듀얼) |
| 고유 자산 | 없음 | PM-ENGINE-MEMORY (TK 시리즈) |

### 타겟 유저
- AI 에이전트를 제품으로 만들고 싶은 PM
- 100 Agents 같은 에이전트 오케스트레이션을 기획하는 사람
- AI 에이전트 스타트업의 초기 팀

---

## 🏗️ 플러그인 구조 (5개)

### Plugin 1: `pm-agent-discovery`
> 어떤 에이전트를 만들어야 하는지 발굴하는 스킬

**Commands**
- `/agent-discover` — 에이전트 기회 발굴 (문제 공간 → 에이전트 솔루션 매핑)
- `/agent-assumptions` — 에이전트 아이디어의 리스크 가정 식별 및 우선순위
- `/agent-cost-model` — 에이전트 운영 비용 시뮬레이션 (토큰 × 호출 수 × 모델)

**Skills**
- `agent-opportunity-tree` — 에이전트 버전의 Opportunity Solution Tree
- `build-or-buy` — 직접 구축 vs 외부 솔루션 의사결정 프레임워크
- `human-in-loop-design` — 어디에 인간 개입을 넣을지 설계
- `agent-assumption-map` — Value / Feasibility / Reliability / Ethics 4축 리스크 매핑

---

### Plugin 2: `pm-agent-strategy`
> 에이전트 시스템의 방향과 수익 구조를 설계하는 스킬

**Commands**
- `/orchestration-pattern` — 단일 / 병렬 / 체인 / 계층 중 최적 패턴 선택
- `/agent-business-model` — 에이전트 수익 구조 설계 (구독 / 매출 공유 / 사용량 과금)
- `/agent-moat` — 에이전트 차별화 전략 (데이터 / 워크플로우 / 도메인 지식)

**Skills**
- `prometheus-atlas-pattern` — 계층형 오케스트레이터 설계 패턴
- `model-router` — 작업 유형별 모델 자동 선택 전략
- `memory-architecture` — 에이전트 메모리 구조 설계 (단기/장기/절차적)
- `agent-portfolio` — 100 Agents 스타일 에이전트 포트폴리오 관리

---

### Plugin 3: `pm-agent-execution`
> 에이전트 PRD 작성부터 스프린트 운영까지

**Commands**
- `/write-agent-prd` — 에이전트 전용 PRD (일반 PRD와 다른 구조: Instruction / Tool / Memory / Trigger)
- `/agent-okr` — 에이전트 성과 지표 설계
- `/agent-sprint` — 에이전트 개발 스프린트 플래닝 (Prototype-first 방식)

**Skills**
- `agent-instruction-design` — System Prompt / Instruction 설계 원칙
- `prompt-engineering-pm` — PM 관점의 프롬프트 엔지니어링 (기술이 아닌 의도 설계)
- `context-window-budget` — 컨텍스트 윈도우 예산 계획
- `agent-prd-template` — 에이전트 PRD 표준 템플릿

---

### Plugin 4: `pm-agent-metrics`
> 에이전트 성과를 측정하고 개선하는 스킬

**Commands**
- `/agent-kpi` — 에이전트 핵심 KPI 설계 (정확도 / 비용 / 레이턴시 / 신뢰성)
- `/reliability-review` — 에이전트 신뢰성·안전성 리뷰 체크리스트
- `/cost-per-outcome` — 에이전트 ROI 계산 (비용 대비 아웃컴 측정)

**Skills**
- `latency-budget` — 에이전트 응답 시간 목표 설계
- `failure-mode-analysis` — 에이전트 실패 모드 분류 및 대응 전략
- `token-cost-tracking` — 토큰 비용 추적 및 최적화 프레임워크
- `agent-north-star` — 에이전트 North Star Metric 설계

---

### Plugin 5: `pm-engine` ⭐ (이든 고유 자산)
> PM 20년 암묵지를 에이전트 Instruction으로 변환하는 스킬

**Commands**
- `/pm-tacit-extract` — 대화/경험에서 PM 암묵지를 추출하고 TK로 구조화
- `/pm-decision-log` — 의사결정 패턴 기록 → 에이전트 Instruction 변환
- `/tk-to-instruction` — TK 시리즈를 에이전트 System Prompt로 자동 변환

**Skills**
- `tacit-knowledge-framework` — PM 암묵지 분류 체계 (Why-first / 의도 기반 설계)
- `decision-pattern-library` — 반복 의사결정 패턴 라이브러리
- `pm-engine-memory` — PM-ENGINE-MEMORY 연동 스킬

> 💡 이 플러그인은 다른 프로젝트에 없는 이든만의 차별화 자산입니다.
> PM-ENGINE-MEMORY의 TK 시리즈가 쌓일수록 이 플러그인이 강력해집니다.

---

## 🔧 기술 스택

### 듀얼 구조 (권장)

```
GitHub 공개 레포 (phuryn/pm-skills 포크)
└── 공개 스킬셋 → 브랜딩 & 커뮤니티

OpenClaw 로컬 (~/.agents/skills/)
└── 이든 전용 스킬 → 실제 워크플로우 연동
```

### 파일 구조
```
ethan-agent-pm-skills/
├── README.md
├── CONTRIBUTING.md
├── pm-agent-discovery/
│   ├── PLUGIN.md
│   └── skills/
│       ├── agent-opportunity-tree/
│       │   └── SKILL.md
│       ├── build-or-buy/
│       │   └── SKILL.md
│       └── ...
├── pm-agent-strategy/
│   └── skills/
├── pm-agent-execution/
│   └── skills/
├── pm-agent-metrics/
│   └── skills/
└── pm-engine/
    └── skills/
```

### 플랫폼 호환성
| 플랫폼 | 지원 방식 | 상태 |
|---|---|---|
| OpenClaw | `~/.agents/skills/` 네이티브 | ✅ 즉시 가능 |
| Claude Code | `claude plugin install` | 📋 구현 예정 |
| Gemini CLI | `.gemini/skills/` 복사 | 📋 구현 예정 |
| Cursor | `.cursor/skills/` 복사 | 📋 구현 예정 |

---

## 📅 로드맵

### Phase 1 — 뼈대 구축 (이번 주)
- [ ] GitHub 레포 생성 (`ethan-agent-pm-skills`)
- [ ] pm-skills 레포에서 참고할 스킬 선별
- [ ] Plugin 1 (`pm-agent-discovery`) 스킬 초안 3개 작성
- [ ] Plugin 5 (`pm-engine`) TK-001 기반 첫 스킬 작성
- [ ] OpenClaw 로컬 설치 및 테스트

### Phase 2 — 핵심 플러그인 완성 (2주차)
- [ ] Plugin 2 (`pm-agent-strategy`) 완성
- [ ] Plugin 3 (`pm-agent-execution`) 완성 — `/write-agent-prd` 포함
- [ ] GitHub 공개 레포 오픈
- [ ] LinkedIn 런칭 포스트 작성

### Phase 3 — 자동화 연결 (3~4주차)
- [ ] `one-day-one-prompt` 크론 → PM-ENGINE TK → 자동 스킬 파일 변환
- [ ] Plugin 4 (`pm-agent-metrics`) 완성
- [ ] CONTRIBUTING.md 작성 → 커뮤니티 기여 유도

### Phase 4 — 브랜딩 확장 (1달 후)
- [ ] 스킬 사용 사례 콘텐츠 시리즈 (LinkedIn 5편)
- [ ] 100 Agents 프로젝트와 연동 케이스스터디 공개
- [ ] clawhub.com 등록 검토

---

## 💡 브랜딩 전략

### GitHub 포지셔닝
```
phuryn/pm-skills     → "PM이 AI를 쓰는 방법"  (이미 있음)
ethan-agent-pm-skills → "PM이 AI 에이전트를 만드는 방법"  (없음)
```

### LinkedIn 런칭 포스트 각도
> "GPT-5.4가 Tool Search로 47% 토큰을 절감했다.
>  그런데 나는 다른 걸 봤다 — 에이전트를 '설계'하는 것이 새로운 PM 스킬이다.
>  PM 20년 암묵지를 AI 에이전트 스킬셋으로 오픈소스화했습니다."

### 타겟 커뮤니티
- AI 에이전트 빌더 (개발자 + PM)
- 국내 AI 스타트업 PM
- OpenClaw / Claude Code 사용자

---

## 📁 관련 파일
- `PM-ENGINE-MEMORY.md` — TK 시리즈 원천 소스
- `AI-BUSINESS-MEMORY.md` — 비즈니스 전략 연동
- `MEMORY.md` — 시스템 패턴 참조

---

## 🔗 참고 레포
- [phuryn/pm-skills](https://github.com/phuryn/pm-skills) — 참고 / 포크 대상 (MIT)
- [OpenClaw Skills 구조](~/.agents/skills/) — 로컬 스킬 포맷 참조
