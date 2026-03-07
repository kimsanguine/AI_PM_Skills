# AI_PM_Skills

> AI 에이전트를 기획하고, 만들고, 운영하는 PM을 위한 오픈소스 스킬셋

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-35-blue?style=flat-square)]()
[![Plugins](https://img.shields.io/badge/plugins-5-purple?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![English](https://img.shields.io/badge/lang-English-blue?style=flat-square)](README.md)

<p align="center">
  <img src="docs/images/plugin-lifecycle.svg" alt="에이전트 프로덕트 라이프사이클" width="800"/>
</p>

```bash
/discover 고객 상담 업무를 자동화하고 싶어
/architecture 다국어 FAQ 자동응답 + 에스컬레이션 에이전트를 구성해줘.
/write-prd 고객 문의 중에서 검토할 신규 우선 기능를 개발해보자.
/health-check 상담 에이전트 주간 점검을 진행해줘
/extract "고객이 긴급이라고 하면 80%는 진짜 긴급이 아니다"
```

---

## 이 프로젝트가 풀려는 문제

2026년, PM에게 "에이전트 만들어봐"라는 요구가 쏟아집니다. 문제는 기존 PM 스킬이 이 상황에 맞지 않다는 거예요.

일반 PM 스킬은 **AI를 도구로 쓰는 법**을 알려줍니다 — PRD를 빠르게 쓰고, OKR을 생성하고, 경쟁사를 분석하는 식으로요. 하지만 **에이전트를 제품으로 만드는 PM**이 부딪히는 질문은 다릅니다.

- "이 에이전트를 1,000명이 쓰면 토큰 비용이 한 달에 얼마야?"
- "에이전트가 환각을 일으키면 어떻게 복구하지?"
- "에이전트 여러 개를 어떻게 엮어야 하지?"
- "내가 3개월 운영하면서 배운 판단 기준을 어떻게 에이전트에 넣지?"

이 프로젝트는 그 질문들에 대한 답을 스킬로 만들었습니다.

---

## 다른 PM 스킬과 뭐가 다른가?

### 1. 에이전트 빌딩 관점의 스킬

일반 PM 스킬이 "PRD를 잘 쓰는 법"을 다룬다면, 이 스킬셋은 "에이전트 PRD에 실패 복구, 컨텍스트 윈도우 관리, 도구 권한을 어떻게 명세하는가"를 다룹니다. 에이전트를 만드는 PM이 실제로 부딪히는 의사결정 — 멀티에이전트 오케스트레이션, 모델 라우팅, 메모리 아키텍처, 비용 스케일링 — 에 특화되어 있습니다.

### 2. 만들기 전에 검증하고, 만들 때 참고하는 도구

| 도구 | 하는 일 |
|------|--------|
| **Build vs Buy** | 직접 만들지 사서 쓸지, 6개 축으로 비교해서 결정 |
| **Reliability/Ethics 4축 가정 검증** | 가치뿐 아니라 신뢰성과 윤리까지 검증한 뒤에 만들기 시작 |
| **Human-in-the-Loop 설계** | 어디서 사람이 개입하고 어디서 에이전트에 맡길지 경계를 그림 |
| **토큰 비용 시뮬레이션** | 유저 10명→100명→1,000명 스케일 시 월 비용을 미리 계산 |
| **구현 전 4축 검증** | 설계가 끝나고 코딩에 들어가기 직전, 4축(가치·실현성·신뢰성·윤리)으로 마지막 점검 + Mermaid 시각화 |
| **이미지 생성 파이프라인** | Gemini 이미지 생성 에이전트를 만들 때 참고할 수 있는 레퍼런스 아키텍처 |

### 3. 운영자의 암묵지가 쌓이는 구조

대부분의 스킬은 1회성입니다. 쓰고 나면 끝이에요. `muse` 플러그인은 다릅니다. PM이 운영하면서 축적한 판단 기준을 TK(Tacit Knowledge) 유닛으로 구조화하고, 그걸 에이전트 인스트럭션에 주입합니다. 쓸수록 에이전트가 더 똑똑해지고, 그 지식은 PM 개인의 자산으로 남습니다.

### 4. Claude 최신 규격 준수

```
marketplace.json          ← Claude Code 마켓플레이스 스키마
evals/evals.json          ← 품질 Eval (10 tests, 54 assertions)
evals/trigger-evals.json  ← 트리거 정확도 Eval (96 queries)
evals/per-skill/*.json    ← 스킬별 개별 Eval
plugin.json (×5)          ← 플러그인 매니페스트
```

마켓플레이스 JSON 스키마, 플러그인 매니페스트, Eval 시스템까지 Claude Code의 공식 규격을 따릅니다. `validate_plugins.py`로 구조 검증도 자동화되어 있어요.

### 5. MCP vs Skills 레이어 가이드

에이전트를 만들다 보면 "이건 MCP 서버로 만들어야 하나, 스킬로 만들어야 하나?"라는 질문이 생깁니다. 이 스킬셋은 설계 단계에서 외부 API 연결(MCP)과 도메인 지식(Skills)을 어떻게 나누고 조합할지를 가이드합니다.

### 6. 콘텐츠 구조적 엄밀함

모든 스킬이 일관된 콘텐츠 구조를 따릅니다: **Core Goal → Trigger Gate → Failure Handling → Quality Gate → Examples**. Trigger Gate(Use / Route / Boundary)로 정확한 스킬이 정확한 상황에서 발동합니다. Failure Handling 테이블은 실패 모드별 감지 방법과 대안을 다룹니다. Quality Gate는 결과물 전달 전 셀프 점검입니다. 이건 포맷팅이 아니라, 프롬프트와 프로덕션급 스킬의 차이입니다.

> 이 콘텐츠 구조는 Claude의 "Skills 2.0" 플랫폼 규격과는 별개의 레이어입니다. 아래 [스킬의 내부 구조](#스킬의-내부-구조)에서 2개 레이어의 관계를 설명합니다.

---

## 어떻게 작동하나요?

<p align="center">
  <img src="docs/images/how-it-works.svg" alt="작동 원리 — Skills, Commands, Plugins" width="700"/>
</p>

**Skills** — 빌딩 블록입니다. 작업을 설명하면 맞는 스킬이 자동으로 로드됩니다.

**Commands** — 여러 스킬을 체이닝하는 워크플로우입니다. `/write-prd`를 입력하면 리서치 → 아키텍처 → 명세 작성이 순서대로 실행됩니다.

**Plugins** — 설치 단위입니다. 하나만 설치하거나 다섯 개 모두 설치할 수 있습니다.

```
Plugin (oracle)
  ├── Skills: opp-tree, assumptions, build-or-buy, hitl, cost-sim, agent-gtm
  └── Commands: /discover, /validate
```

> 스킬 파일(SKILL.md)은 표준 마크다운입니다. Gemini CLI, Cursor, Codex CLI, Kiro에서도 사용 가능합니다.

---

## 스킬의 내부 구조

### 자동 호출 원리

스킬은 직접 이름을 불러서 쓰는 게 아닙니다. **자연어로 작업을 설명하면, Claude가 각 SKILL.md의 `description` 필드를 매칭해서 가장 적합한 스킬을 자동 로드**합니다.

```
사용자: "에이전트가 환각을 일으키면 어떻게 복구하지?"
         ↓
Claude: description 매칭 → reliability 스킬 자동 로드
         ↓
스킬:   Trigger Gate 확인 → 조건 충족 → 스킬 실행
```

트리거 정확도는 96개 쿼리 기준 **97.9%** 입니다. 각 스킬의 `description`은 200자 이상으로, "Use when..." 패턴으로 발동 조건을 명시합니다.

### SKILL.md 콘텐츠 구조

모든 35개 스킬은 동일한 콘텐츠 구조를 따릅니다:

```
┌─────────────────────────────────────────────┐
│  Frontmatter                                │
│  - name, description (200자+), argument-hint│
├─────────────────────────────────────────────┤
│  Core Goal          ← 1-2문장 목적          │
├─────────────────────────────────────────────┤
│  Trigger Gate                               │
│  - Use: 이 스킬을 써야 할 때               │
│  - Route: 다른 스킬로 보내야 할 때          │
│  - Boundary: 이 스킬의 범위 밖인 것         │
├─────────────────────────────────────────────┤
│  개념 설명 + 실행 절차   ← 본문 콘텐츠      │
├─────────────────────────────────────────────┤
│  Failure Handling                           │
│  - 실패 모드 │ 감지 방법 │ 대안 (테이블)     │
├─────────────────────────────────────────────┤
│  Quality Gate        ← 전달 전 체크리스트    │
├─────────────────────────────────────────────┤
│  Examples            ← 좋은/나쁜 출력 신호   │
└─────────────────────────────────────────────┘
```

**Trigger Gate**가 핵심입니다. Use/Route/Boundary 3가지 조건으로 "이 스킬이 맞는지, 다른 스킬로 보내야 하는지, 아예 범위 밖인지"를 판단합니다. 이 구조 덕분에 스킬 간 충돌 없이 정확한 스킬이 정확한 상황에서 발동합니다.

### 커맨드 체이닝

커맨드(`/write-prd`, `/discover` 등)는 여러 스킬을 순서대로 엮는 워크플로우입니다.

```
/discover 고객 상담 자동화
  ① opp-tree     → 기회 매핑
  ② assumptions  → 가정 검증
  ③ build-or-buy → 실현성 스코어링
  → 종합 리포트 출력
```

| 커맨드 | 체이닝되는 스킬 | 플러그인 |
|--------|---------------|---------|
| `/discover` | opp-tree → assumptions → build-or-buy | oracle |
| `/validate` | assumptions → hitl → cost-sim | oracle |
| `/architecture` | orchestration → 3-tier → memory-arch | atlas |
| `/strategy-review` | moat → biz-model → growth-loop | atlas |
| `/write-prd` | prd → instruction → ctx-budget | forge |
| `/set-okr` | okr → kpi → north-star | forge+argus |
| `/sprint` | stakeholder-map → agent-plan-review | forge |
| `/health-check` | kpi → reliability → burn-rate | argus |
| `/cost-review` | burn-rate → cost-sim → router | argus+oracle+atlas |
| `/extract` | pm-framework (TK 포착) | muse |
| `/decide` | pm-decision (패턴 매칭) | muse |
| `/tk-to-instruction` | pm-engine → instruction | muse+forge |

> 커맨드는 Claude Code 전용입니다. 다른 도구에서는 스킬만 개별 사용 가능합니다.

### 플랫폼 규격과 콘텐츠 구조 — 2개 레이어

AI_PM_Skills는 두 개의 독립된 레이어로 구성됩니다.

```
┌─ Platform Layer (Skills 2.0 규격) ──────────────────────────┐
│  Claude Code가 정의한 스킬 플랫폼 규격                        │
│  frontmatter · auto-invocation · subagent · hooks            │
│  marketplace · evals · plugin directory structure             │
├─ Content Layer (AI_PM_Skills 콘텐츠 구조) ──────────────────┤
│  이 프로젝트가 정의한 스킬 콘텐츠 설계 패턴                    │
│  Core Goal → Trigger Gate → Failure Handling                 │
│  → Quality Gate → Examples                                   │
└──────────────────────────────────────────────────────────────┘
```

**Platform Layer**는 Claude Code가 스킬을 *발견하고 실행하는 방법*을 정의합니다. YAML frontmatter 스키마, 디렉토리 구조, `description` 기반 자동 호출 메커니즘이 여기에 해당합니다. 이 규격은 Claude Code가 제공하며, 2025년 Skills 1.0에서 2026년 Skills 2.0으로 진화했습니다.

**Content Layer**는 스킬 안에 *무엇을 담느냐*의 문제입니다. 같은 플랫폼 위에서도 Trigger Gate 없이 만들면 스킬 간 충돌이 나고, Failure Handling 없이 만들면 프로덕션에서 문제가 생깁니다. AI_PM_Skills의 콘텐츠 구조(Core Goal → Trigger Gate → ... → Examples)는 이 레이어의 설계 패턴이며, 이 프로젝트 고유의 기여입니다.

> 혼동 방지: 문서에서 "Skills 2.0"은 Claude Code의 **플랫폼 규격**을, "콘텐츠 구조"는 AI_PM_Skills의 **스킬 설계 패턴**을 지칭합니다.

### Skills 1.0 vs Skills 2.0 — AI_PM_Skills가 활용하는 것

Claude Code의 스킬 플랫폼은 Skills 1.0(2025)에서 Skills 2.0(2026)으로 진화했습니다. AI_PM_Skills는 Skills 2.0 규격 위에서 동작하며, 다음 기능을 활용합니다.

| 기능 | Skills 1.0 (2025) | Skills 2.0 (2026) | AI_PM_Skills 활용 |
|------|-------------------|-------------------|-------------------|
| **스킬 위치** | `.claude/commands/` | `.claude/skills/` + 플러그인 디렉토리 | ✅ 5개 플러그인 디렉토리 구조 |
| **Frontmatter** | 없음 (단순 마크다운) | `name`, `description`, `argument-hint`, `allowed-tools`, `context` 등 | ✅ `name`, `description` (200자+), `argument-hint`, `context`, `allowed-tools` |
| **자동 호출** | ❌ 명시적 `/` 커맨드만 | ✅ `description` 매칭으로 자동 로드 | ✅ 96개 쿼리 97.9% 정확도 |
| **커맨드 통합** | 커맨드와 스킬 분리 | 커맨드가 스킬 시스템에 통합 | ✅ 12개 커맨드 |
| **변수 치환** | ❌ | `$ARGUMENTS`, `${CLAUDE_SKILL_DIR}` 등 | ✅ 모든 커맨드에서 `$ARGUMENTS` 사용 |
| **서브에이전트** | ❌ | `context: fork`로 격리 실행 | ✅ 5개 리뷰/분석 스킬 (`premortem`, `agent-plan-review`, `reliability`, `cohort`, `agent-ab-test`) |
| **도구 제한** | ❌ | `allowed-tools`로 사용 도구 제한 | ✅ 35개 전체 스킬 — 3등급 분류 (Read/Write · +WebSearch · +Edit/Bash) |
| **마켓플레이스** | ❌ | `marketplace.json` 스키마 | ✅ 마켓플레이스 등록 |
| **Eval 시스템** | ❌ | `evals.json` 스키마 | ✅ 10 tests, 54 assertions |
| **모델 지정** | ❌ | `model` 필드로 실행 모델 선택 | ✅ 35개 전체 스킬 `model: sonnet` 기본값 (사용자 변경 가능) |
| **동적 주입** | ❌ | `` !`command` ``로 실행 시 외부 데이터 주입 | ✅ 5개 핵심 스킬 — 프로젝트 메모리 + PM 도구(Linear/GitHub) 자동 연동 |
| **Hooks** | ❌ | `hooks`로 스킬 라이프사이클 이벤트 처리 | ✅ 5개 핵심 스킬 — Stop 시 Quality Gate 검증 스크립트 실행 |

> ⚠️ `hooks`는 플러그인 내 스킬에서 트리거되지 않는 알려진 이슈가 있습니다 ([#17688](https://github.com/anthropics/claude-code/issues/17688)). 스펙 준수 상태로 구현되어 있으며, 이슈 해결 시 자동 작동합니다.

---

## 파일 구조

```
AI_PM_Skills/
├── .claude-plugin/
│   └── marketplace.json              # 마켓플레이스 등록 정보
│
├── oracle/                           # 발견 — 어떤 에이전트를 만들까?
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── opp-tree/SKILL.md         #   기회 트리
│   │   ├── assumptions/SKILL.md      #   4축 가정 검증
│   │   ├── build-or-buy/SKILL.md     #   Build vs Buy 의사결정
│   │   ├── hitl/SKILL.md             #   Human-in-the-Loop 범위
│   │   ├── cost-sim/SKILL.md         #   토큰 비용 시뮬레이션
│   │   └── agent-gtm/SKILL.md        #   Go-to-Market 전략
│   └── commands/
│       ├── discover.md               #   /discover
│       └── validate.md               #   /validate
│
├── atlas/                            # 설계 — 어떤 구조로 만들까?
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── 3-tier/SKILL.md           #   3계층 멀티에이전트 설계
│   │   ├── orchestration/SKILL.md    #   오케스트레이션 패턴
│   │   ├── biz-model/SKILL.md        #   수익 모델 설계
│   │   ├── router/SKILL.md           #   LLM 모델 라우팅
│   │   ├── memory-arch/SKILL.md      #   메모리 아키텍처
│   │   ├── moat/SKILL.md             #   경쟁 해자 분석
│   │   └── growth-loop/SKILL.md      #   데이터 플라이휠
│   └── commands/
│       ├── architecture.md           #   /architecture
│       └── strategy-review.md        #   /strategy-review
│
├── forge/                            # 실행 — 어떻게 명세하고 만들까?
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── instruction/SKILL.md      #   인스트럭션 7요소 설계
│   │   ├── prd/SKILL.md              #   에이전트 전용 PRD
│   │   ├── prompt/SKILL.md           #   프롬프트 설계 (CRISP)
│   │   ├── ctx-budget/SKILL.md       #   컨텍스트 윈도우 예산
│   │   ├── okr/SKILL.md              #   에이전트 OKR
│   │   ├── stakeholder-map/SKILL.md  #   이해관계자 매핑
│   │   ├── agent-plan-review/SKILL.md#   구현 전 4축 검증
│   │   ├── gemini-image-flow/SKILL.md#   이미지 생성 파이프라인
│   │   ├── infographic-gif-creator/SKILL.md  # 인포그래픽 GIF/MP4
│   │   ├── pptx-ai-slide/SKILL.md     #   에이전트 프레젠테이션
│   │   └── agent-demo-video/SKILL.md   #   에이전트 데모 영상
│   └── commands/
│       ├── write-prd.md              #   /write-prd
│       ├── set-okr.md                #   /set-okr
│       └── sprint.md                 #   /sprint
│
├── argus/                            # 운영 — 어떻게 측정하고 개선할까?
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── kpi/SKILL.md              #   운영+비즈니스 KPI
│   │   ├── reliability/SKILL.md      #   신뢰성 점검
│   │   ├── premortem/SKILL.md        #   실패 모드 분석 (FMEA)
│   │   ├── burn-rate/SKILL.md        #   비용 추적/최적화
│   │   ├── north-star/SKILL.md       #   North Star Metric
│   │   ├── agent-ab-test/SKILL.md    #   A/B 테스트
│   │   ├── cohort/SKILL.md           #   코호트 분석
│   │   └── incident/SKILL.md         #   장애 대응 프로토콜
│   └── commands/
│       ├── health-check.md           #   /health-check
│       └── cost-review.md            #   /cost-review
│
├── muse/                             # 학습 — PM 암묵지를 에이전트 자산으로
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── pm-framework/SKILL.md     #   TK-NNN 암묵지 분류
│   │   ├── pm-decision/SKILL.md      #   의사결정 패턴
│   │   └── pm-engine/SKILL.md        #   PM-ENGINE-MEMORY
│   └── commands/
│       ├── extract.md                #   /extract
│       ├── decide.md                 #   /decide
│       └── tk-to-instruction.md      #   /tk-to-instruction
│
├── evals/                            # Eval 시스템
│   ├── evals.json                    #   품질 Eval (10 tests, 54 assertions)
│   ├── trigger-evals.json            #   트리거 정확도 (96 queries)
│   └── per-skill/                    #   스킬별 개별 Eval
│
├── eval-workspace/                   # Eval 실행 결과 + 벤치마크
├── docs/images/                      # 다이어그램, 스크린샷
├── validate_plugins.py               # 구조 자동 검증 스크립트
├── GUIDE-ko.md                       # 시나리오별 사용 가이드
├── CONTRIBUTING.md                   # 기여 가이드
└── LICENSE                           # MIT
```

---

## 설치하기

### 방법 1: GitHub에서 마켓플레이스 등록 (권장)

Claude Code에서 `/plugin` 명령어로 마켓플레이스를 등록한 뒤, 개별 플러그인을 설치합니다.

```bash
# 1단계: 마켓플레이스 등록
/plugin marketplace add kimsanguine/AI_PM_Skills

# 2단계: 개별 플러그인 설치
/plugin install oracle@kimsanguine-AI_PM_Skills
/plugin install atlas@kimsanguine-AI_PM_Skills
/plugin install forge@kimsanguine-AI_PM_Skills
/plugin install argus@kimsanguine-AI_PM_Skills
/plugin install muse@kimsanguine-AI_PM_Skills
```

> 설치 후 Claude Code를 재시작하면 스킬이 자동으로 로드됩니다.

### 방법 2: 로컬에 클론해서 직접 로드

GitHub에서 다운로드한 뒤 `--plugin-dir` 플래그로 직접 로드합니다.

```bash
# 레포 클론
git clone https://github.com/kimsanguine/AI_PM_Skills.git

# 개별 플러그인 로드 (원하는 것만)
claude --plugin-dir ./AI_PM_Skills/oracle
claude --plugin-dir ./AI_PM_Skills/forge

# 또는 전체 로드
claude --plugin-dir ./AI_PM_Skills/oracle \
       --plugin-dir ./AI_PM_Skills/atlas \
       --plugin-dir ./AI_PM_Skills/forge \
       --plugin-dir ./AI_PM_Skills/argus \
       --plugin-dir ./AI_PM_Skills/muse
```

어떤 에이전트를 만들지 아직 모르겠다면 → `oracle`만 먼저 설치하세요.
이미 뭘 만들지 정했다면 → `forge`부터 시작하세요.

### 다른 AI 도구

스킬 파일(SKILL.md)은 표준 마크다운이라 Claude Code 외 도구에서도 사용 가능합니다. 커맨드 체이닝(`/write-prd` 등)은 Claude Code 전용입니다.

| 도구 | 스킬 | 커맨드 | 사용법 |
|------|:----:|:------:|-------|
| **Gemini CLI** | ✅ | ❌ | `.gemini/skills/`에 복사 |
| **Cursor** | ✅ | ❌ | `.cursor/skills/`에 복사 |
| **Codex CLI** | ✅ | ❌ | `.codex/skills/`에 복사 |
| **Kiro** | ✅ | ❌ | `.kiro/skills/`에 복사 |

```bash
# 전체 스킬을 다른 도구에 복사
for plugin in oracle atlas forge argus muse; do
  cp -r "$plugin/skills/"* ~/.gemini/skills/ 2>/dev/null
done
```

---

## 플러그인 상세

<details>
<summary><strong>1. oracle</strong> — 어떤 에이전트를 만들까? <code>(6 skills, 2 commands)</code></summary>

| 스킬 | 하는 일 | 이럴 때 쓰세요 |
|------|--------|-------------|
| `opp-tree` | 반복 빈도·자동화 적합성·판단 의존도 기준으로 기회 트리를 만들고 우선순위 매김 | "팀에 자동화 후보가 10개인데 뭐부터 해야 하지?" |
| `assumptions` | 가치/실현성/신뢰성/윤리 4축으로 가정을 뽑고, 2일 내 검증 실험 설계 | "이 에이전트 만들기 전에 가장 위험한 가정이 뭐지?" |
| `build-or-buy` | 차별화·속도·비용·커스텀·유지보수·도메인 6개 축 스코어링으로 Build/Buy/No-code 판단 | "Intercom 봇 vs 직접 만든 에이전트, 어떤 게 나아?" |
| `hitl` | 되돌림 가능성×오류 영향 2축 매트릭스로 자동화 레벨(1-5)과 에스컬레이션 트리거 설정 | "환불 결정은 에이전트가 해도 되나, 사람이 봐야 하나?" |
| `cost-sim` | 모델별 토큰 단가×호출 패턴으로 1→10→100→1,000 유저 시나리오 월비용 시뮬레이션 | "Sonnet으로 하루 500건 처리하면 한 달에 얼마야?" |
| `agent-gtm` | 비치헤드 세그먼트 5기준 스코어링 + Shadow→Co-pilot→Auto→Delegation 신뢰 구축 시퀀스 | "B2B 고객사에 이 에이전트를 어떤 순서로 풀어야 하지?" |

**커맨드:** `/discover` · `/validate`

**사용 예시:**
```
"고객 온보딩 플로우를 자동화하고 싶은데, 에이전트를 만들 가치가 있을까?"
→ build-or-buy 스킬이 자동 로드

/discover 고객 지원 워크플로우
→ 기회 매핑 → 가정 검증 → 타당성 스코어링 순서로 실행
```

</details>

<details>
<summary><strong>2. atlas</strong> — 어떤 구조로 만들까? <code>(7 skills, 2 commands)</code></summary>

| 스킬 | 하는 일 | 이럴 때 쓰세요 |
|------|--------|-------------|
| `3-tier` | Prometheus(전략)→Atlas(조율)→Worker(실행) 3계층 역할·통신·위임 설계 | "에이전트 5개를 엮어야 하는데 누가 뭘 관장하지?" |
| `orchestration` | Sequential/Parallel/Router/Hierarchical 패턴 비교 후 지연·에러·비용 기준 선택 | "문서 처리 파이프라인을 직렬로 할지 병렬로 할지?" |
| `biz-model` | 건당/구독/성과 기반 가격 설계 + 변동비 구조 분석으로 >70% 마진 달성 | "에이전트 API 콜당 과금 vs 월정액, 뭐가 나아?" |
| `router` | 작업 복잡도별 T1-T4 모델 자동 분배 + 폴백 체인으로 40-80% 비용 절감 | "간단한 FAQ는 Haiku, 복잡한 분석은 Opus — 자동 라우팅?" |
| `memory-arch` | Working/Episodic/Semantic/Procedural 4종 메모리 설계 + 토큰 한도 내 검색 전략 | "어제 대화 맥락을 오늘 세션에서 어떻게 불러오지?" |
| `moat` | 데이터 플라이휠·워크플로우 종속·네트워크 효과·전환비용·전문화·브랜드 6종 해자 진단 | "경쟁사가 GPT 기반으로 비슷한 거 만들면 뭘로 방어하지?" |
| `growth-loop` | 사용→데이터→개선→재사용 루프 설계 + 콜드스타트 해결 + 반(反)루프 식별 | "유저가 쓸수록 추천이 정확해지는 구조를 어떻게 만들지?" |

**커맨드:** `/architecture` · `/strategy-review`

**사용 예시:**
```
"이 에이전트가 5가지 작업 유형을 처리해야 하는데, 어떤 아키텍처가 좋을까?"
→ orchestration 스킬이 자동 로드

/architecture 멀티스텝 문서 처리 파이프라인
→ 패턴 선택 → 계층 구조 설계 → 메모리 아키텍처 계획
```

</details>

<details>
<summary><strong>3. forge</strong> — 어떻게 명세하고 만들까? <code>(11 skills, 3 commands)</code></summary>

| 스킬 | 하는 일 | 이럴 때 쓰세요 |
|------|--------|-------------|
| `instruction` | Role/Context/Goal/Tools/Memory/Output/Failure 7요소 + 최소 권한 원칙 적용 | "에이전트 시스템 프롬프트에 뭘 넣고 뭘 빼야 하지?" |
| `prd` | 인스트럭션/도구/메모리/트리거/출력/실패 복구 7섹션 에이전트 전용 명세서 | "일반 PRD 말고, 환각 복구·도구 권한까지 담긴 기획서?" |
| `prompt` | CRISP(Context/Role/Instruction/Scope/Parameters) + Why-First 원칙 + 7대 실패 패턴 회피 | "프롬프트가 길어질수록 에이전트가 이상하게 행동해" |
| `ctx-budget` | 파일별 토큰 소비 추정 → 필수/조건부/제외 분류 → 70% 임계치 경고 | "RAG 문서 5개 + 대화 히스토리를 128K에 어떻게 넣지?" |
| `okr` | 비즈니스 임팩트(시간·비용·에러 절감) + 운영 건강(정확도·비용·신뢰성) 2축 OKR + 필수 비용 KR | "에이전트 성공을 '정확도 95%'만으로 측정해도 되나?" |
| `stakeholder-map` | Power-Interest 매트릭스 + 유형별 블로커 대응 전략 + 내부 챔피언 육성 | "법무팀이 에이전트 도입을 반대하는데 어떻게 설득하지?" |
| `agent-plan-review` | 스코프/아키텍처/인스트럭션/신뢰성 4축 검증 + 실패 모드 매트릭스(5+종) + Mermaid 시각화 | "코딩 시작 전에 이 설계의 구멍을 찾아줘" |
| `gemini-image-flow` | Gemini API Phase 0-7 단계별 이미지 생성 파이프라인 + 모델 티어 선택(Flash/Pro) | "스케치→코드, 이미지→마케팅 소재 파이프라인을 만들고 싶어" |
| `infographic-gif-creator` | 에이전트 아키텍처·워크플로우·데이터 흐름을 HTML/CSS→GIF/MP4 애니메이션으로 변환 | "멀티에이전트 구조를 경영진에게 1분 애니메이션으로 보여줘" |
| `pptx-ai-slide` | 에이전트 프로젝트를 스토리 기반 슬라이드로 변환 (피치/리뷰/투자자용) | "다음 주 이사회에서 이 에이전트를 10장 슬라이드로 설명해야 해" |
| `agent-demo-video` | 화면 녹화+아키텍처 애니메이션+나레이션+자막을 Remotion으로 합성 | "비개발자 이해관계자에게 에이전트가 뭘 하는지 영상으로 보여줘" |

**커맨드:** `/write-prd` · `/set-okr` · `/sprint`

**사용 예시:**
```
"회의 요약 에이전트의 PRD를 작성해줘"
→ prd 스킬 로드 (실패 복구, 컨텍스트 관리, 도구 권한 등 에이전트 전용 섹션 포함)

/write-prd 고객 지원 에스컬레이션 에이전트
→ 요구사항 수집 → 인스트럭션 설계 → 에이전트 PRD 출력
```

</details>

<details>
<summary><strong>4. argus</strong> — 어떻게 측정하고 개선할까? <code>(8 skills, 2 commands)</code></summary>

| 스킬 | 하는 일 | 이럴 때 쓰세요 |
|------|--------|-------------|
| `kpi` | 운영 5-7개(지연시간/성공률/에러율) + 비즈니스(완료율/만족도/건당비용) 지표 정의 + 선행·후행 분류 | "에이전트 대시보드에 어떤 지표를 넣어야 하지?" |
| `reliability` | P95/P99 최악 시나리오 정량화 + 입력/모델/연동 유형별 안전장치 + SLA 등급(Basic→Critical) 설정 | "에이전트가 100건 중 3건 환각인데, 이게 허용 범위야?" |
| `premortem` | 심각도×발생확률×탐지난이도 RPN 스코어로 10-15개 실패 모드 사전 식별 + 분기 재점검 | "출시 전에 '이건 터지면 안 되는데' 리스트를 만들어줘" |
| `burn-rate` | 모델별·작업유형별·유저세그먼트별 토큰 비용 시각화 + 스파이크 감지 + 월 예산 상한 알림 | "지난주 대비 토큰 비용 40% 증가 — 원인이 뭐야?" |
| `north-star` | 실행가능·측정가능·책임자·방향성·실현가능 5기준으로 단일 핵심 지표 선정 + 반(反)지표 설정 | "KPI가 8개인데 팀이 뭘 최우선으로 봐야 할지 모르겠어" |
| `agent-ab-test` | MDE(최소 탐지 효과) 산출 + 동시 실행(순차 아님) + LLM 비결정성 통제 + p-value 검증 | "프롬프트 A vs B 중 뭐가 나은지 통계적으로 확인하고 싶어" |
| `cohort` | 배포 코호트별 4주+ 관측 + 샘플≥100 + 외부 변수 통제로 버전간 성능 변화 추적 | "v2.1로 올렸는데 이전 버전보다 정말 나아졌어?" |
| `incident` | 사일런트 실패 감지 + 심각도 분류 + 피해 범위 차단 + 5 Whys(3회+) 포스트모템 | "에이전트가 30분째 응답이 없는데 알림도 안 왔어" |

**커맨드:** `/health-check` · `/cost-review`

**사용 예시:**
```
"이번 주 토큰 비용이 40% 뛰었는데, 뭐가 문제야?"
→ burn-rate 스킬 로드 (비용 분석 + 최적화 방안)

/health-check 온보딩 에이전트
→ KPI 리뷰 → 신뢰성 점검 → 비용 이상 감지 → 주간 요약
```

</details>

<details>
<summary><strong>5. muse ⭐</strong> — PM 암묵지를 에이전트 자산으로 <code>(3 skills, 3 commands)</code></summary>

| 스킬 | 하는 일 | 이럴 때 쓰세요 |
|------|--------|-------------|
| `pm-framework` | 경험 속 판단 기준을 TK-NNN 유닛으로 구조화 (활성/비활성 조건 포함) + 지식 그래프 연결 | "3년간 에이전트 운영하면서 배운 것들이 머릿속에만 있어" |
| `pm-decision` | 반복되는 PM 의사결정 상황의 맥락·판단 기준·알려진 실패를 패턴 라이브러리로 축적 | "이 상황은 예전에도 겪었는데, 그때 왜 그렇게 결정했더라?" |
| `pm-engine` | TK 지식 그래프를 에이전트가 실행 중 동적 참조 + 하루 1TK 자동 추출 + 인스트럭션 자동 갱신 | "내가 축적한 운영 노하우를 에이전트가 알아서 활용하게 만들고 싶어" |

**커맨드:** `/extract` · `/decide` · `/tk-to-instruction`

**사용 예시:**
```
/extract "에이전트 PRD 리뷰할 때 실패 모드 섹션에 환각 복구가 있는지 항상 확인한다"
→ TK 포착 → 분류 → 지식 그래프에 연결

/tk-to-instruction 온보딩 에이전트
→ 관련 TK 유닛 탐색 → 에이전트 인스트럭션으로 변환
```

> 프레임워크는 오픈소스, 데이터(PM-ENGINE-MEMORY.md)는 각자의 자산입니다.

</details>

---

## 벤치마크

스킬이 실제로 효과가 있는지 10개 테스트(54개 검증 항목)로 측정했습니다.

| | 스킬 사용 | 스킬 미사용 | 차이 |
|---|---------|----------|-----|
| **검증 통과율** | **100%** | 88% | **+12%** |
| **평균 실행 시간** | 62초 | 42초 | +20초 |

- **역량 게이팅** — 스킬 없이는 아예 수행 불가. `pm-framework`(TK 유닛 구조화)은 40%, `3-tier`(멀티에이전트 설계)는 60-80%로 하락.
- **품질 증폭** — 둘 다 통과하지만 스킬이 더 깊은 결과. `cost-sim`은 +46.6% 출력, `premortem`은 2배 더 많은 실패 모드.
- **에이전트 특화** — `prd`와 `premortem`은 어느 쪽이든 통과하지만, 스킬 사용 시 범용 PM 구조 대신 에이전트 특화 템플릿 생성.

전체 데이터: [`eval-workspace/iteration-1/benchmark.json`](eval-workspace/iteration-1/benchmark.json)

> **참고:** 벤치마크는 32개 스킬(v0.4) 기준입니다. 35개 스킬 + v1.0 구조 기준 재측정은 다음 iteration에서 진행 예정입니다.

---

## 스킬 출처

| 유형 | 개수 | 설명 |
|------|-----|------|
| 🟢 적용 | 3 | 기존 PM 프레임워크(OST, FMEA)를 에이전트 맥락에 맞게 재구성 |
| 🟡 확장 | 6 | 일반 PM 개념에 에이전트 전용 차원을 대폭 추가 |
| 🔴 신규 | 26 | 에이전트 전용 영역 — 다른 PM 스킬셋에 없는 것들 |

**74%가 오리지널 작업입니다.**

---

## 현재 상태

**v1.0** — 전체 5개 플러그인 완성 (35 스킬, 12 커맨드) + v1.0 구조 업그레이드

| 플러그인 | 스킬 | 커맨드 | 트리거 정확도 | 상태 |
|---------|------|-------|-------------|------|
| oracle | 6 | 2 | 18/20 (90%) | ✅ |
| atlas | 7 | 2 | 24/24 (100%) | ✅ |
| forge | 11 | 3 | 20/20 (100%) | ✅ |
| argus | 8 | 2 | 20/20 (100%) | ✅ |
| muse | 3 | 3 | 12/12 (100%) | ✅ |
| **전체** | **35** | **12** | **94/96 (97.9%)** | |

---

## 기여하기

[CONTRIBUTING.md](CONTRIBUTING.md)를 확인해주세요. 새 스킬, 기존 스킬 개선, 번역 모두 환영합니다.

---

## 만든 사람

**Sanguine Kim (이든)** — PM 20년차, AI 에이전트 빌더

참고한 사람과 자료:
- Teresa Torres — *Continuous Discovery Habits*
- Anthropic — "Building Effective Agents"
- Steve Yegge — Gas Town 병렬 에이전트 설계
- Byeonghyeok Kwak — MCP-Skills 계층 설계
- Michael Polanyi — *The Tacit Dimension*

---

## 관련 프로젝트

| 레포 | 성격 | 링크 |
|------|------|------|
| **AI_PM** | PM을 위한 Claude Code 가이드 (배우기) | [github.com/kimsanguine/AI_PM](https://github.com/kimsanguine/AI_PM) |
| **AI_PM_Skills** | 바로 쓸 수 있는 에이전트 스킬셋 (도구) | *(이 레포)* |

> **AI_PM**으로 배우고, **AI_PM_Skills**로 만드세요.

---

## 라이선스

MIT — [LICENSE](LICENSE)
