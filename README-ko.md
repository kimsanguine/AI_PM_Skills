# AI_PM_Skills

> **PM이 AI 에이전트를 만드는 방법** — AI 에이전트를 기획하고 운영하는 PM을 위한 오픈소스 스킬셋

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![English](https://img.shields.io/badge/lang-English-blue?style=flat-square)](README.md)

---

## 왜 이 프로젝트인가?

대부분의 PM 스킬은 **"AI를 도구로 쓰는 PM"**을 돕습니다 — PRD 작성, OKR 생성, 경쟁 분석 등.

이 프로젝트는 다릅니다.

> **"AI 에이전트를 직접 만들고, 운영하고, 비즈니스로 만드는 PM을 위한 스킬셋"**

2026년, 에이전트를 만드는 PM의 병목은 코딩 능력이 아닙니다. **의도와 판단** — 어떤 에이전트를 만들지, 어떻게 설계할지, 어떻게 측정하고 방어할지입니다.

이 프로젝트는 PM 20년의 암묵지를 AI 에이전트 스킬셋으로 변환한 오픈소스 시도입니다.

---

## 시작하기

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

```bash
/discover [자동화하려는 업무]       # 에이전트 기회 발굴
/architecture [복잡한 워크플로우]    # 아키텍처 설계
/write-prd [에이전트 이름]          # PRD 작성
/health-check [에이전트 이름]       # 주간 건강 점검
```

> 스킬 파일(SKILL.md)은 표준 마크다운이므로 다른 도구에서도 사용 가능합니다.
>
> | 도구 | 스킬 (SKILL.md) | 커맨드 체이닝 |
> |-----|:---:|:---:|
> | Claude Code | ✅ | ✅ |
> | Gemini CLI | ✅ | ⚠️ 수동 |
> | Cursor | ✅ | ⚠️ 수동 |
> | Codex CLI | ✅ | ⚠️ 수동 |
> | Kiro | ✅ | ⚠️ 수동 |

---

## 일반 PM 스킬이 다루지 않는 6가지 영역

| 영역 | 하는 일 | 왜 필요한가 |
|-----|--------|-----------|
| **에이전트 경제학** | 토큰 비용 시뮬레이션, 스케일 예측, 최적화 전략 | 유저 10명에 월 $3K인 에이전트는 100명이면 $30K — 만들기 전에 모델링이 필요 |
| **멀티에이전트 아키텍처** | Prometheus-Atlas-Worker 3계층 설계, 오케스트레이션 패턴, 모델 라우팅 | 복잡한 워크플로우는 에이전트 여러 개가 협업해야지, 하나로는 안 됨 |
| **에이전트 전용 PRD** | Instruction, Tools, Triggers, Memory, Failure Handling 섹션 | 일반 PRD에는 에이전트의 실패 복구나 컨텍스트 윈도우 관리 명세가 없음 |
| **운영 신뢰성** | FMEA 기반 프리모템, SLO 설계, 에러 복구 패턴 | 에이전트의 실패는 소프트웨어와 다름 — 환각, 컨텍스트 드리프트, 비용 폭등 |
| **경쟁 해자** | 데이터 플라이휠, 프로세스 락인, 지식 해자 분석 + 안티모트 패턴 | "GPT-4를 씁니다"는 해자가 아님. 축적된 운영 데이터와 암묵지가 해자 |
| **PM 암묵지** | TK-NNN(Never-ending Nuance Network) — PM 판단을 추출·구조화·에이전트에 주입 (TK-001→TK-999) | PM 경험이 재사용 가능한 자산이 되고, TK 간 연결이 지식 그래프를 형성해 모든 에이전트를 더 똑똑하게 만듦 |

---

## 플러그인 구조

각 플러그인 이름은 그리스 신화에서 가져왔습니다. 단순한 장식이 아니라, 에이전트 제품 생명주기의 각 단계에 정확히 대응하는 원형(archetype)입니다.

| 플러그인 | 원형 | 왜 이 이름인가 |
|---------|------|--------------|
| **oracle** | 델포이의 신탁 — 무엇을 추구할지 계시하는 예언자 | 발견 단계: 어떤 에이전트를 만들지 커밋 전에 내다보기 |
| **atlas** | 아틀라스 — 세계의 구조를 떠받치는 거인 | 설계 단계: 시스템 아키텍처 결정의 무게를 지탱하기 |
| **forge** | 헤파이스토스의 대장간 — 신의 도구가 만들어지는 곳 | 실행 단계: 날것의 아이디어를 출하 가능한 명세로 벼리기 |
| **argus** | 아르고스 판옵테스 — 백 개의 눈을 가진 수호자 | 모니터링 단계: 모든 지표와 모든 실패 모드를 감시하기 |
| **muse** | 뮤즈 — 창조적 지식과 기억의 원천 | 지식 단계: 경험을 재사용 가능한 지혜로 변환하기 |

네이밍 원칙: (1) 누구든 찾아보면 바로 직관적으로 이해할 수 있는 은유, (2) CLI 네임스페이스로 동작하는 단일 단어 (`oracle/skills/cost-sim`).

### 1. `oracle` — 어떤 에이전트를 만들까?
| 스킬 | 설명 |
|------|------|
| `opp-tree` | 에이전트 Opportunity Solution Tree |
| `assumptions` | Value/Feasibility/Reliability/Ethics 4축 가정 분석 |
| `build-or-buy` | 직접 구축 vs 외부 솔루션 의사결정 |
| `hitl` | Human-in-the-loop 자동화 범위 설계 |
| `cost-sim` | 토큰 비용 시뮬레이션 |
| `agent-gtm` | 에이전트 Go-to-Market 전략 |

**Commands:** `/discover` · `/validate`

---

### 2. `atlas` — 어떤 구조로 만들까?
| 스킬 | 설명 |
|------|------|
| `3-tier` | 3계층 오케스트레이터 설계 (Prometheus-Atlas-Worker) |
| `orchestration` | Sequential/Parallel/Router/Hierarchical 패턴 선택 |
| `biz-model` | 에이전트 수익 구조 설계 |
| `router` | 작업별 LLM 모델 선택 전략 |
| `memory-arch` | 단기/장기/절차적 메모리 설계 |
| `moat` | 에이전트 경쟁 우위 분석 |
| `growth-loop` | 에이전트 데이터 플라이휠 설계 |

**Commands:** `/architecture` · `/strategy-review`

---

### 3. `forge` — 어떻게 명세하고 실행할까?
| 스킬 | 설명 |
|------|------|
| `instruction` | Instruction 7요소 설계 |
| `prd` | 에이전트 전용 PRD 템플릿 |
| `prompt` | PM 관점 프롬프트 설계 (CRISP) |
| `ctx-budget` | 컨텍스트 윈도우 토큰 예산 |
| `okr` | 2축 Agent OKR |
| `stakeholder-map` | 에이전트 도입 이해관계자 매핑 |
| `agent-plan-review` | 에이전트 설계 구현 전 4축 검증 |
| `gemini-image-flow` | AI 이미지 생성 파이프라인 설계 |

**Commands:** `/write-prd` · `/set-okr` · `/sprint`

---

### 4. `argus` — 어떻게 측정하고 개선할까?
| 스킬 | 설명 |
|------|------|
| `kpi` | 운영 건강도 + 비즈니스 임팩트 KPI |
| `reliability` | 에이전트 신뢰성 체계 점검 |
| `premortem` | 사전 실패 모드 분석 (FMEA) |
| `burn-rate` | 토큰 비용 추적 및 최적화 |
| `north-star` | North Star Metric 정의 |
| `agent-ab-test` | 에이전트 A/B 테스트 설계 및 분석 |
| `cohort` | 에이전트 코호트 분석 |
| `incident` | 에이전트 장애 대응 프로토콜 |

**Commands:** `/health-check` · `/cost-review`

---

### 5. `muse` ⭐ — PM 암묵지를 에이전트 자산으로
| 스킬 | 설명 |
|------|------|
| `pm-framework` | TK-NNN 암묵지 분류 체계 |
| `pm-decision` | 6가지 핵심 의사결정 패턴 |
| `pm-engine` | PM-ENGINE-MEMORY 인터페이스 |

**Commands:** `/extract` · `/decide` · `/tk-to-instruction`

> 프레임워크는 오픈소스, 데이터(PM-ENGINE-MEMORY.md)는 각자의 자산입니다.

---

## 벤치마크

5개 대표 스킬(플러그인당 1개)에 대해 with-skill vs without-skill eval을 실행하여 스킬이 base Claude 위에 실제로 무엇을 더하는지 측정했습니다.

| 지표 | With Skill | Without Skill | Delta |
|-----|-----------|--------------|-------|
| **Pass Rate** | **100%** | 88% | **+12%** |
| **평균 시간** | 62.1s | 41.7s | +20.5s |

10개 테스트, 54개 assertion 기반 핵심 발견:

- **역량 게이팅 스킬** — 스킬 없이는 아예 불가능. `pm-framework`(TK 유닛 구조화)은 40%로 하락, `3-tier`(Prometheus-Atlas-Worker)는 60-80%로 하락.
- **품질 증폭 스킬** — 둘 다 통과하지만 스킬이 더 깊은 output 생성. `cost-sim`은 context accumulation 비용 분석 추가(+46.6%), `premortem`은 최대 2배 더 많은 실패 모드 생성.
- **베이스라인 강세 스킬** — `prd`와 `premortem`은 어느 쪽이든 100% 통과하지만, with-skill output은 범용 PM 구조가 아닌 에이전트 특화 템플릿을 따름.

전체 벤치마크 데이터: [`eval-workspace/iteration-1/benchmark.json`](eval-workspace/iteration-1/benchmark.json)

## 현재 상태

**v0.4** — 전체 5개 플러그인 완성 (32 스킬, 12 커맨드)

| 플러그인 | 스킬 | 커맨드 | 트리거 정확도 | 상태 |
|---------|------|-------|-------------|------|
| oracle | 6 | 2 | 18/20 (90%) | ✅ 완료 |
| atlas | 7 | 2 | 24/24 (100%) | ✅ 완료 |
| forge | 8 | 3 | 20/20 (100%) | ✅ 완료 |
| argus | 8 | 2 | 20/20 (100%) | ✅ 완료 |
| muse | 3 | 3 | 12/12 (100%) | ✅ 완료 |
| **전체** | **32** | **12** | **94/96 (97.9%)** | |

---

## 기여하기

[CONTRIBUTING.md](CONTRIBUTING.md)를 확인해주세요.

---

## 만든 사람

**Sanguine Kim (이든)** — PM 20년, AI 에이전트 개발자

참고 및 영감:
- Teresa Torres — *Continuous Discovery Habits* (OST 기원)
- Anthropic — "Building Effective Agents" (멀티에이전트 패턴)
- Steve Yegge — Gas Town 병렬 에이전트 설계 원칙
- Byeonghyeok Kwak — MCP-Skills 계층 설계 원칙
- Michael Polanyi — *The Tacit Dimension* (TK-NNN 이론적 기반)

---

## 관련 프로젝트

| 레포 | 내용 | 링크 |
|------|------|------|
| **AI_PM** | PM을 위한 Claude Code 가이드 — Discovery → Definition → Delivery → Growth | [github.com/kimsanguine/AI_PM](https://github.com/kimsanguine/AI_PM) |
| **AI_PM_Skills** | 오픈소스 에이전트 스킬셋 — 5개 플러그인, 32개 스킬, 12개 커맨드 *(이 레포)* | [github.com/kimsanguine/AI_PM_Skills](https://github.com/kimsanguine/AI_PM_Skills) |

> **AI_PM**은 *왜, 어떻게*를 가르칩니다. **AI_PM_Skills**는 *바로 쓸 수 있는 도구*를 제공합니다.

---

## 라이선스

MIT — [LICENSE](LICENSE)
