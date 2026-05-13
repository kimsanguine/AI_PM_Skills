---
name: pptx-ai-slide
description: "Route PPTX requests to the right engine (mckinsey for 30+ lecture decks, hifidelity for image-heavy pitches ≤10 slides, html-qa for mid-size minimal/editorial decks with auto QA, video for video-to-slide preprocessing) and produce pitch decks, architecture overviews, stakeholder updates, or demo presentations. Use when translating agent designs into compelling visual narratives. Routes to agent-demo-video for video conversion."
argument-hint: "[presentation topic or agent to present]"
allowed-tools: ["Read", "Write", "Edit", "Bash"]
model: sonnet
---

## Core Goal
- 에이전트 프로젝트의 핵심 가치를 시각적 스토리로 전환한다.
- 슬라이드 구조와 메시지 밀도를 청중에 맞게 최적화한다.
- 발표 직후 바로 사용 가능한 완성도 높은 PPTX를 산출한다.

---

## Trigger Gate

### Use This Skill When
- 에이전트 프로젝트의 피치 덱/발표 자료를 만들어야 할 때
- 아키텍처/워크플로우를 슬라이드로 설명해야 할 때
- 이해관계자 업데이트용 프레젠테이션이 필요할 때
- 에이전트 데모 발표 자료를 구성해야 할 때

### Route to Other Skills When
- 슬라이드를 영상으로 변환해야 하면 → `agent-demo-video`
- 에이전트 아키텍처 설계 자체가 목적이면 → `3-tier` 또는 `orchestration`
- 이해관계자 커뮤니케이션 전략이면 → `stakeholder-map`
- 인포그래픽 GIF/애니메이션이면 → `infographic-gif-creator`

### Boundary Checks
- 이 스킬은 PPTX 결과물 제작에 집중한다. 에이전트 설계나 전략 수립은 범위 밖이다.
- 발표 스크립트 작성은 보조적으로 포함하되, 주 산출물은 PPTX이다.
- 템플릿 마스터 레이아웃을 임의로 훼손하지 않는다.

---

## 에이전트 프레젠테이션 패턴

에이전트 프로젝트의 발표는 일반 제품과 다른 구조가 필요합니다.

### 피치 덱 구조 (권장)

| 순서 | 슬라이드 | 핵심 질문 |
|---|---|---|
| 1 | 문제 정의 | 사람이 수동으로 하고 있는 비효율은? |
| 2 | 솔루션 | 에이전트가 어떻게 해결하는가? |
| 3 | 아키텍처 | 시스템은 어떻게 동작하는가? |
| 4 | 데모/워크플로우 | 실제로 어떻게 보이는가? |
| 5 | HITL 설계 | 사람은 어디에 개입하는가? |
| 6 | 비용/ROI | 얼마나 절감되는가? |
| 7 | 리스크 & 완화 | 잘못되면 어떻게 되는가? |
| 8 | 로드맵 | 다음 단계는? |

### 청중별 슬라이드 밀도

| 청중 | 권장 슬라이드 수 | 메시지 밀도 | 포커스 |
|---|---|---|---|
| C-Level | 5~8장 | 낮음 (1메시지/장) | 비즈니스 임팩트, ROI |
| PM/기획팀 | 8~12장 | 중간 | 워크플로우, HITL, 로드맵 |
| 엔지니어링 | 10~15장 | 높음 | 아키텍처, 시퀀스, 기술 스택 |
| 투자자 | 10~12장 | 중간 | 시장, 차별화, 비전 |

### 슬라이드 디자인 원칙

```
원칙 1: 1슬라이드 = 1메시지
  - 핵심 문장 1개 + 지원 비주얼
  - 본문 bullet 최대 5개

원칙 2: 다이어그램 > 텍스트
  - 아키텍처는 반드시 다이어그램으로
  - 워크플로우는 순서도로

원칙 3: 숫자로 설득
  - "빠릅니다" → "처리 시간 80% 단축"
  - "저렴합니다" → "월 $25로 운영"

원칙 4: HITL 슬라이드 필수
  - 에이전트 발표에서 가장 자주 받는 질문: "사람은 어디에?"
  - 반드시 1장 이상 할애
```

---

## 엔진 라우팅 (v0.7.0+)

> 단일 PPTX 생성 방식은 청중/규모/스타일에 맞지 않을 때가 많다.
> **입력 신호 → 4개 엔진 중 하나로 라우팅**하는 결정 트리를 따른다.
> 각 엔진은 다른 도구 체인을 가지며 트레이드오프가 명확히 다르다.

### 엔진 카탈로그

| 엔진 | 적합 케이스 | 도구 체인 | 강점 | 약점 |
|---|---|---|---|---|
| **mckinsey** | 30+장 강의/대량 자료, 컨설팅 톤 | PptxGenJS / Node.js | 디자인 결정론, 일관성, 속도 | 슬라이드별 커스터마이즈 약함 |
| **hifidelity** | 1~10장 투자 피치, 슬라이드별 이미지 | Imagen 4.0 + 슬라이드 디자이너 파이프라인 | 비주얼 임팩트, 연구급 폴리시 | 이미지 비용·시간 큼 |
| **html-qa** | 5~25장 미니멀/에디토리얼, QA 필수 | HTML-first + Playwright PDF + 100점 루브릭 | 슬라이드별 디자인 자유도 + 자동 QA | 30+장은 비효율 |
| **video** | 영상(YouTube/mp4) → 슬라이드 | Whisper 전사 + 섹션화 + 체이닝 | 음성 자산 재활용 | 후속 엔진 체이닝 필수 (단독 사용 불가) |

### 라우팅 결정 트리

```
입력 = 영상 URL/mp4?
  → video 엔진 (전사 → 구조화 brief → html-qa 또는 mckinsey 체인)
  STOP

장수 ≥ 30 또는 강의/리포트 시리즈?
  → mckinsey 엔진
  STOP

장수 ≤ 10 AND (투자 피치 / 연구 / 슬라이드별 이미지 필수)?
  → hifidelity 엔진
  STOP

그 외 (5~25장, 일반 미니멀/에디토리얼, QA 필요):
  → html-qa 엔진  ← 디폴트
```

### Boundary

- **이 스킬은 라우터 + 단일-스킬 fallback**이다. 4엔진은 외부 도구 체인이므로
  hplan은 라우팅 결정과 입력 명세를 책임지고, 실제 생성은 사용자의
  설치된 PPT 도구 체인이 수행한다.
- 엔진 미설치 환경에서는 PptxGenJS 기반 단일 흐름으로 fallback한다.

---

## Instructions

You are creating a presentation for: **$ARGUMENTS**

**Step 0 — 엔진 선택** (v0.7.0+)
- 위 결정 트리로 엔진 1개 선정
- 선택 근거를 한 줄로 명시 (예: "장수 35 + 강의 시리즈 → mckinsey")
- 영상 입력이면 video → 후속 엔진 체이닝까지 명시

**Step 1 — 요구 정렬**
- 발표 목적/청중/시간을 확인
- 핵심 메시지 3개 이내로 압축
- 슬라이드 수 결정 (청중별 권장치 참조)

**Step 2 — 구조 설계**
- 피치 덱 구조 또는 커스텀 구조 선택
- 슬라이드별 핵심 메시지 1줄 배치
- 다이어그램 필요 슬라이드 식별

**Step 3 — 콘텐츠 매핑**
- 원본 콘텐츠를 슬라이드 단위로 배치
- 표/차트/다이어그램 규격 확정
- 외부 소스 콘텐츠 출처 기록

**Step 4 — PPTX 반영**
- 레이아웃 유지 상태로 내용 반영
- 정렬/폰트/간격 점검
- 텍스트 overflow 0건 확인

**Step 5 — QA & 전달**
- 오탈자, 레이아웃, 해상도 점검
- 발표 흐름 점검 (스토리 연결성)
- 최종 파일 경로와 변경 요약 제공

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| 청중/목적 불명확 | Step 1에서 필수 입력 누락 | 청중 유형 4가지 제시 후 선택 요청 |
| 텍스트 overflow 발생 | 슬라이드 렌더링 시 텍스트 박스 넘침 | 슬라이드 분할안 제시, 1메시지/장 원칙 재적용 |
| 아키텍처 다이어그램 누락 | 기술 슬라이드에 텍스트만 존재 | Mermaid 또는 SVG 다이어그램 자동 생성 제안 |
| HITL 슬라이드 미포함 | 최종 QA에서 HITL 섹션 없음 | "사람 개입 지점" 슬라이드 1장 추가 권고 |

---

## Quality Gate

- [ ] 1슬라이드 1메시지 원칙이 유지되는가 (Yes/No)
- [ ] 청중별 권장 슬라이드 수 범위 이내인가 (Yes/No)
- [ ] 텍스트 overflow가 0건인가 (Yes/No)
- [ ] 아키텍처/워크플로우 슬라이드에 다이어그램이 포함되었는가 (Yes/No)
- [ ] HITL 설계 슬라이드가 1장 이상 포함되었는가 (Yes/No)
- [ ] 변경 슬라이드 번호와 최종 파일 경로가 제공되는가 (Yes/No)

---

## Examples

### Good Example
**요청:** "고객 문의 자동 분류 에이전트를 C-Level에 피칭할 발표자료 만들어줘. 핵심은 비용 절감과 응답 속도 개선이야. 7장 이내로."

**왜 좋은 요청인가:**
- 에이전트 (고객 문의 분류), 청중 (C-Level), 핵심 메시지 (비용/속도), 분량 (7장)이 명확
- 바로 구조 설계로 진입 가능

**기대 결과:**
- 7장 피치 덱: 문제→솔루션→아키텍처→데모→비용ROI→HITL→로드맵
- 비용 비교 차트, 응답 시간 비교 표 포함
- HITL 슬라이드에 에스컬레이션 플로우 다이어그램

### Bad Example
**요청:** "발표자료 만들어줘."

**왜 나쁜 요청인가:**
- 발표 주제, 청중, 분량, 핵심 메시지 전부 불명
- Step 1에서 최소 3개 확인 질문 필요

---

### 참고
- 설계자: AI PM Skills Contributors, 2026-03
- 피치 덱 구조: Y Combinator / a16z 발표 구조 참조 + 에이전트 특화 (HITL/비용) 추가
- 1슬라이드 1메시지: Garr Reynolds "Presentation Zen" 원칙 적용

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
