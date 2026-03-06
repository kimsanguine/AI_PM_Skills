# ethan-agent-pm-skills

> **PM이 AI 에이전트를 만드는 방법** — AI 에이전트를 기획하고 운영하는 PM을 위한 오픈소스 스킬셋

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![Status](https://img.shields.io/badge/Status-Phase%201-blue?style=flat-square)]()

---

## 왜 이 프로젝트인가?

[phuryn/pm-skills](https://github.com/phuryn/pm-skills) 같은 훌륭한 PM 스킬 마켓플레이스가 있습니다.  
하지만 그 65개 스킬 전부는 **"AI 도구를 쓰는 PM"** 을 위한 것입니다.

지금 우리에게 필요한 건 다릅니다.

> **"AI 에이전트를 직접 만들고, 운영하고, 비즈니스로 만드는 PM을 위한 스킬셋"**

2026년, 에이전트를 만드는 PM의 병목은 코딩 능력이 아닙니다.  
**어떤 에이전트를 만들지, 어떻게 설계할지, 어떻게 측정할지** — 의도와 판단의 문제입니다.

이 프로젝트는 PM 20년의 암묵지를 AI 에이전트 스킬셋으로 변환한 오픈소스 시도입니다.

---

## 시작하기

```bash
# 에이전트 기회 발굴
/agent-discover [자동화하려는 업무]

# 에이전트 설계
/agent-instruction-design [에이전트 이름]

# 오케스트레이션 패턴 선택
/orchestration-pattern [복잡한 작업]

# 빌드 vs 바이 결정
/build-or-buy [만들려는 기능]
```

---

## phuryn/pm-skills와 무엇이 다른가?

| | phuryn/pm-skills | ethan-agent-pm-skills |
|---|---|---|
| **대상** | AI 도구를 쓰는 PM | AI 에이전트를 만드는 PM |
| **철학** | 좋은 PM 문서 빠르게 만들기 | 옳은 에이전트를 의도적으로 설계하기 |
| **차별화 축** | 프레임워크 라이브러리 | Reliability · Ethics · Cost 포함 |
| **고유 자산** | 외부 저자 프레임워크 | PM-ENGINE (운영자 암묵지 축적) |
| **언어** | 영어 | 한국어 + 영어 |
| **규모** | 65개 스킬 | 25개 집중 스킬 |

두 프로젝트는 경쟁 관계가 아닙니다.  
phuryn/pm-skills는 **일반 PM 도구**, 이 프로젝트는 **에이전트 PM 도구**입니다.

---

## 플러그인 구조

### 1. `pm-agent-discovery` — 어떤 에이전트를 만들까?
| 스킬 | 설명 | 소스 |
|---|---|---|
| `agent-opportunity-tree` | 에이전트 버전의 Opportunity Solution Tree | 🟢 적응 |
| `agent-assumption-map` | Value/Feasibility/Reliability/Ethics 4축 가정 분석 | 🟢 적응 |
| `build-or-buy` | 직접 구축 vs 외부 솔루션 의사결정 | 🔴 신규 |
| `human-in-loop-design` | 자동화 범위와 인간 개입 설계 | 🔴 신규 |
| `agent-cost-model` | 토큰 비용 시뮬레이션 | 🔴 신규 |

**Commands:** `/agent-discover` · `/agent-assumptions` · `/build-or-buy`

---

### 2. `pm-agent-strategy` — 어떤 구조로 만들까?
| 스킬 | 설명 | 소스 |
|---|---|---|
| `prometheus-atlas-pattern` | 3계층 오케스트레이터 설계 | 🔴 신규 |
| `orchestration-pattern` | 단일/병렬/체인/계층 패턴 선택 | 🔴 신규 |
| `agent-business-model` | 에이전트 수익 구조 설계 | 🟡 적응 |
| `model-router` | 작업 유형별 모델 선택 전략 | 🔴 신규 |
| `memory-architecture` | 단기/장기/절차적 메모리 설계 | 🔴 신규 |
| `agent-moat` | 에이전트 차별화 전략 | 🔴 신규 |

**Commands:** `/orchestration-pattern` · `/agent-business-model` · `/agent-moat`

---

### 3. `pm-agent-execution` — 어떻게 명세하고 실행할까?
| 스킬 | 설명 | 소스 |
|---|---|---|
| `agent-instruction-design` | Instruction 7요소 설계 | 🔴 신규 |
| `agent-prd-template` | 에이전트 전용 PRD 템플릿 | 🟡 적응 |
| `prompt-engineering-pm` | PM 관점의 프롬프트 설계 | 🔴 신규 |
| `context-window-budget` | 컨텍스트 윈도우 예산 계획 | 🔴 신규 |
| `agent-okr` | 에이전트 성과 지표 OKR | 🟡 적응 |

**Commands:** `/write-agent-prd` · `/agent-okr` · `/agent-sprint`

---

### 4. `pm-agent-metrics` — 어떻게 측정하고 개선할까?
| 스킬 | 설명 | 소스 |
|---|---|---|
| `agent-kpi` | 정확도/비용/레이턴시/신뢰성 KPI | 🟡 적응 |
| `reliability-review` | 에이전트 신뢰성·안전성 체크리스트 | 🔴 신규 |
| `failure-mode-analysis` | 에이전트 실패 모드 분류 | 🔴 신규 |
| `token-cost-tracking` | 토큰 비용 추적 및 최적화 | 🔴 신규 |
| `agent-north-star` | 에이전트 North Star Metric | 🟡 적응 |

**Commands:** `/agent-kpi` · `/reliability-review` · `/cost-per-outcome`

---

### 5. `pm-engine` ⭐ — PM 암묵지를 에이전트 자산으로
| 스킬 | 설명 | 소스 |
|---|---|---|
| `tacit-knowledge-framework` | PM 암묵지 분류 체계 | 🔴 신규 |
| `decision-pattern-library` | 반복 의사결정 패턴 라이브러리 | 🔴 신규 |
| `pm-engine-memory` | PM-ENGINE-MEMORY 연동 | 🔴 신규 |

**Commands:** `/pm-tacit-extract` · `/pm-decision-log` · `/tk-to-instruction`

> 💡 이 플러그인은 다른 어떤 PM 스킬 마켓플레이스에도 없습니다.
> 운영자의 20년 경험이 쌓일수록 강력해지는 살아있는 플러그인입니다.

---

## 스킬 소스 분류

| 분류 | 수 | 설명 |
|---|---|---|
| 🟢 적응 (phuryn 구조 참고) | 3개 | 프레임워크 유지, 에이전트 맥락 전환 |
| 🟡 50%+ 재작성 | 7개 | 일부 참고, 에이전트 특화 내용 다수 추가 |
| 🔴 신규 제작 | 15개 | phuryn에 없는 에이전트 특화 영역 |

전체의 **60%가 신규 제작** — 이것이 이 프로젝트의 차별화 근거입니다.

---

## 설치

### OpenClaw
```bash
# skills 폴더에 플러그인 복사
cp -r pm-agent-discovery ~/.agents/skills/
cp -r pm-agent-strategy ~/.agents/skills/
cp -r pm-agent-execution ~/.agents/skills/
cp -r pm-agent-metrics ~/.agents/skills/
cp -r pm-engine ~/.agents/skills/
```

### Claude Code (준비 중)
```bash
claude plugin marketplace add [repo-url]
```

### 다른 AI 도구 (Gemini CLI, Cursor, Codex CLI)
```bash
# 예시: Gemini CLI
for plugin in pm-agent-*/; do
  cp -r "$plugin/skills/"* ~/.gemini/skills/ 2>/dev/null
done
```

---

## 현재 상태 (Phase 1)

**완료된 스킬 (5개):**
- ✅ `agent-opportunity-tree` — 에이전트 기회 발굴 OST
- ✅ `agent-assumption-map` — 4축 가정 분석
- ✅ `build-or-buy` — 빌드 vs 바이 의사결정
- ✅ `agent-instruction-design` — Instruction 7요소 설계
- ✅ `prometheus-atlas-pattern` — 3계층 오케스트레이터 패턴

**Phase 2 (진행 예정):**
- `orchestration-pattern`, `agent-business-model`, `agent-moat`, `model-router`, `memory-architecture`

**Phase 3 (자동화 연결):**
- `one-day-one-prompt` 크론 → PM-ENGINE TK → 자동 스킬 변환

---

## 기여하기

[CONTRIBUTING.md](CONTRIBUTING.md) ← 준비 중

새로운 스킬 아이디어, 기존 스킬 개선, 번역(영어↔한국어) 모두 환영합니다.

---

## 만든 사람

**Sanguine Kim (이든)** — PM 20년, AI 에이전트 개발자  
100 Agents 프로젝트 진행 중 | OpenClaw 기반 에이전트 오케스트레이션 시스템 운영

참고 및 영감:
- [phuryn/pm-skills](https://github.com/phuryn/pm-skills) — MIT, 구조 설계 참고
- Teresa Torres — Continuous Discovery Habits (OST 원형)
- Byeonghyeok Kwak — MCP-Skills 계층 설계 원칙
- Steve Yegge — Gas Town 병렬 에이전트 설계 원칙

---

## 라이선스

MIT — [LICENSE](LICENSE)
