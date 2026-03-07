# AI_PM_Skills

> AI 에이전트를 기획하고, 만들고, 운영하는 PM을 위한 오픈소스 스킬셋

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-32-blue?style=flat-square)]()
[![Plugins](https://img.shields.io/badge/plugins-5-purple?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![English](https://img.shields.io/badge/lang-English-blue?style=flat-square)](README.md)

<p align="center">
  <img src="docs/images/plugin-lifecycle.svg" alt="에이전트 프로덕트 라이프사이클" width="800"/>
</p>

```bash
/discover 고객 상담 업무를 자동화하고 싶어
/architecture 다국어 FAQ 자동응답 + 에스컬레이션 에이전트
/write-prd 고객 상담 자동응답 에이전트
/health-check 상담 에이전트 주간 점검
/extract "고객이 긴급이라고 하면 80%는 진짜 긴급이 아니었다"
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
│   │   └── gemini-image-flow/SKILL.md#   이미지 생성 파이프라인
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

### Claude Cowork (GUI — CLI 불필요)

1. **Cowork**를 열고 새 세션을 시작하세요
2. 사이드바에서 **Plugins**를 클릭
3. `AI_PM_Skills`를 검색
4. **Install** 클릭 — 5개 플러그인이 한번에 설치됩니다

<!-- TODO: GitHub 업로드 후 설치 GIF 추가 -->
<!-- ![설치 데모](docs/images/install-cowork.gif) -->

### Claude Code (CLI)

```bash
# 마켓플레이스 설치 (5개 플러그인 한번에)
claude plugin marketplace add kimsanguine/AI_PM_Skills

# 또는 개별 설치
claude plugin add oracle/    # 발견
claude plugin add atlas/     # 설계
claude plugin add forge/     # 실행
claude plugin add argus/     # 운영
claude plugin add muse/      # 학습
```

어떤 에이전트를 만들지 아직 모르겠다면 → `oracle`만 먼저 설치하세요.
이미 뭘 만들지 정했다면 → `forge`부터 시작하세요.

### 다른 AI 도구

| 도구 | 스킬 | 커맨드 | 사용법 |
|------|:----:|:------:|-------|
| **Gemini CLI** | ✅ | ⚠️ 수동 | `.gemini/skills/`에 복사 |
| **Cursor** | ✅ | ⚠️ 수동 | `.cursor/skills/`에 복사 |
| **Codex CLI** | ✅ | ⚠️ 수동 | `.codex/skills/`에 복사 |
| **Kiro** | ✅ | ⚠️ 수동 | `.kiro/skills/`에 복사 |

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
| `opp-tree` | 기회 트리 작성 | "뭘 자동화하면 좋을까?" |
| `assumptions` | 4축 가정 검증 (가치/실현성/신뢰성/윤리) | "이거 진짜 만들어도 되나?" |
| `build-or-buy` | 직접 구축 vs 외부 솔루션 판단 | "사서 쓸까 직접 만들까?" |
| `hitl` | Human-in-the-Loop 범위 설정 | "어디까지 자동화하고 어디서 사람이 개입?" |
| `cost-sim` | 토큰 비용 시뮬레이션 | "한 달에 얼마 들어?" |
| `agent-gtm` | Go-to-Market 전략 | "출시를 어떻게 해야 하지?" |

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
| `3-tier` | 3계층 멀티에이전트 설계 | "에이전트 여러 개를 어떻게 엮지?" |
| `orchestration` | 오케스트레이션 패턴 선택 | "Sequential? Parallel? Router?" |
| `biz-model` | 수익 모델 설계 | "이걸로 어떻게 돈 벌지?" |
| `router` | LLM 모델 라우팅 | "이 작업에 Haiku? Sonnet? Opus?" |
| `memory-arch` | 메모리 아키텍처 | "대화 기록을 어떻게 관리하지?" |
| `moat` | 경쟁 해자 분석 | "경쟁사가 따라오면 어쩌지?" |
| `growth-loop` | 데이터 플라이휠 설계 | "사용할수록 똑똑해지게 만들려면?" |

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
<summary><strong>3. forge</strong> — 어떻게 명세하고 만들까? <code>(8 skills, 3 commands)</code></summary>

| 스킬 | 하는 일 | 이럴 때 쓰세요 |
|------|--------|-------------|
| `instruction` | 인스트럭션 7요소 설계 | "에이전트한테 뭐라고 말해줘야 하지?" |
| `prd` | 에이전트 전용 PRD | "기획서를 어떤 형식으로 쓰지?" |
| `prompt` | PM 관점 프롬프트 설계 (CRISP) | "프롬프트를 어떻게 잘 짜지?" |
| `ctx-budget` | 컨텍스트 윈도우 예산 | "128K 토큰을 어떻게 배분하지?" |
| `okr` | 에이전트 OKR | "성공 기준을 어떻게 잡지?" |
| `stakeholder-map` | 이해관계자 매핑 | "누가 찬성하고 누가 막지?" |
| `agent-plan-review` | 구현 전 4축 검증 + Mermaid | "이 설계 괜찮은지 구현 전에 봐줘" |
| `gemini-image-flow` | 이미지 생성 파이프라인 | "이미지 생성 에이전트를 어떻게 만들지?" |

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
| `kpi` | 운영+비즈니스 KPI | "어떤 지표를 봐야 하지?" |
| `reliability` | 신뢰성 점검 | "에이전트가 엉뚱한 답을 하면?" |
| `premortem` | 실패 모드 분석 (FMEA) | "출시 전에 뭐가 터질 수 있지?" |
| `burn-rate` | 비용 추적/최적화 | "비용이 왜 이렇게 늘었지?" |
| `north-star` | North Star Metric | "궁극적 성공 지표는?" |
| `agent-ab-test` | A/B 테스트 | "프롬프트 변경 효과가 진짜야?" |
| `cohort` | 코호트 분석 | "버전별 성능이 어떻게 변하지?" |
| `incident` | 장애 대응 프로토콜 | "에이전트가 터졌는데 어떻게 하지?" |

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
| `pm-framework` | TK-NNN 암묵지 분류 | "내 경험을 체계적으로 정리하고 싶어" |
| `pm-decision` | 6가지 의사결정 패턴 | "이 상황에서 어떻게 판단하지?" |
| `pm-engine` | PM-ENGINE-MEMORY 인터페이스 | "축적된 TK를 에이전트에 주입하고 싶어" |

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

---

## 스킬 출처

| 유형 | 개수 | 설명 |
|------|-----|------|
| 🟢 적용 | 3 | 기존 PM 프레임워크(OST, FMEA)를 에이전트 맥락에 맞게 재구성 |
| 🟡 확장 | 6 | 일반 PM 개념에 에이전트 전용 차원을 대폭 추가 |
| 🔴 신규 | 23 | 에이전트 전용 영역 — 다른 PM 스킬셋에 없는 것들 |

**72%가 오리지널 작업입니다.**

---

## 현재 상태

**v0.4** — 전체 5개 플러그인 완성 (32 스킬, 12 커맨드)

| 플러그인 | 스킬 | 커맨드 | 트리거 정확도 | 상태 |
|---------|------|-------|-------------|------|
| oracle | 6 | 2 | 18/20 (90%) | ✅ |
| atlas | 7 | 2 | 24/24 (100%) | ✅ |
| forge | 8 | 3 | 20/20 (100%) | ✅ |
| argus | 8 | 2 | 20/20 (100%) | ✅ |
| muse | 3 | 3 | 12/12 (100%) | ✅ |
| **전체** | **32** | **12** | **94/96 (97.9%)** | |

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
