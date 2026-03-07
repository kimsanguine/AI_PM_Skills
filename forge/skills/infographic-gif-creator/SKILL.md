---
name: infographic-gif-creator
description: "Create animated infographics (GIF/MP4) from HTML/CSS to visualize agent architectures, workflows, and data flows. Use when you need visual explanations for stakeholder communication, documentation, or demo materials. Routes to compose-video for multi-scene final rendering."
argument-hint: "[infographic topic or data to visualize]"
---

## Core Goal
- 에이전트 아키텍처, 워크플로우, 데이터 흐름을 애니메이션 인포그래픽으로 시각화한다.
- 재현 가능한 렌더링 파이프라인으로 일관된 품질의 비주얼 에셋을 생산한다.
- 이해관계자 커뮤니케이션과 문서화에 바로 사용 가능한 포맷으로 출력한다.

---

## Trigger Gate

### Use This Skill When
- 에이전트 아키텍처를 애니메이션으로 설명해야 할 때
- 워크플로우/데이터 플로우를 시각적 에셋으로 만들어야 할 때
- 이해관계자 발표용 짧은 루프형 비주얼이 필요할 때
- 문서/README에 삽입할 GIF를 제작해야 할 때

### Route to Other Skills When
- 에이전트 데모 영상(장면+음성+자막)이면 → `agent-demo-video`
- 에이전트 아키텍처 설계 자체가 목적이면 → `3-tier` 또는 `orchestration`
- 발표 슬라이드(PPTX) 제작이면 → `pptx-ai-slide`
- 정적 이미지만 필요하면 → `gemini-image-flow`

### Boundary Checks
- 이 스킬은 HTML/CSS → GIF/MP4 렌더링 파이프라인 전용이다.
- 데이터 해석이나 분석 보고서 작성은 범위 밖이다.
- 멀티씬 장편 영상 합성은 `compose-video` 범위이다.

---

## 왜 인포그래픽 GIF인가?

에이전트 PM에게 인포그래픽 GIF는 강력한 커뮤니케이션 도구입니다.

| 상황 | 정적 이미지 | 애니메이션 GIF |
|---|---|---|
| 멀티스텝 워크플로우 설명 | 한 장에 모든 단계 표시 → 복잡 | 단계별 순차 등장 → 직관적 |
| 이해관계자 설득 | 아키텍처 다이어그램 1장 | 데이터 흐름이 움직이는 시각화 |
| README/문서 삽입 | 스크린샷 | 자동재생 GIF → 즉시 이해 |
| Slack/이메일 공유 | 첨부파일 열어야 함 | 인라인 재생 → 즉시 전달 |

### 주요 활용 사례

**1. 에이전트 아키텍처 시각화**
```
3-Tier 구조:
[사용자 입력] → [Orchestrator] → [Sub-agent A]
                               → [Sub-agent B]
                               → [Tool Call]
→ 각 계층이 순차적으로 나타나는 애니메이션
```

**2. 워크플로우 단계별 애니메이션**
```
Step 1: 트리거 감지 (Slack 메시지)
Step 2: 컨텍스트 수집 (Notion API)
Step 3: LLM 판단 (Sonnet)
Step 4: 액션 실행 (이메일 발송)
→ 각 단계가 하이라이트되며 진행
```

**3. 비용/성능 비교 차트**
```
모델별 비용 바 차트가 순차적으로 올라가는 애니메이션
Haiku: $2/월 → Sonnet: $25/월 → Opus: $150/월
```

---

## 렌더링 파이프라인

### 1단계: 장면 설계

```
장면 구성 체크리스트:
□ 전달할 핵심 메시지 1개 확정
□ 키프레임 수 결정 (권장: 3~8프레임)
□ 텍스트 최소 노출 시간 2초 확보
□ 루프 여부 결정 (시작/끝 연결성)
```

### 2단계: HTML/CSS 구현

```html
<!-- 기본 구조 예시 -->
<div class="scene" style="width:1280px; height:720px;">
  <div class="step step-1">트리거 감지</div>
  <div class="step step-2">컨텍스트 수집</div>
  <div class="step step-3">LLM 판단</div>
  <div class="step step-4">액션 실행</div>
</div>

<!-- CSS 애니메이션 -->
<style>
.step { opacity: 0; animation: fadeIn 0.5s forwards; }
.step-1 { animation-delay: 0s; }
.step-2 { animation-delay: 2s; }
.step-3 { animation-delay: 4s; }
.step-4 { animation-delay: 6s; }
</style>
```

### 3단계: 캡처 & 인코딩

**GIF 출력 (기본 설정)**
```bash
# 2-pass 인코딩으로 품질 최적화
ffmpeg -i input.mp4 -vf "fps=12,scale=1280:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i input.mp4 -i palette.png -lavfi "fps=12,scale=1280:-1:flags=lanczos[v];[v][1:v]paletteuse" output.gif
```

**MP4 출력 (기본 설정)**
```bash
ffmpeg -i input.mp4 -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r 30 output.mp4
```

### 품질 기준

| 포맷 | fps | 최대 용량 | 해상도 |
|---|---|---|---|
| GIF | 12 | 8MB | 1280px (긴 변) |
| MP4 | 30 | 50MB | 1920×1080 |

---

## Instructions

You are creating an animated infographic for: **$ARGUMENTS**

**Step 1 — 장면 설계**
- 전달할 핵심 메시지를 1문장으로 확정
- 키프레임 수와 타이밍을 결정 (텍스트 최소 2초 노출)
- 루프/비루프 결정

**Step 2 — HTML/CSS 구현**
- 애니메이션 장면을 HTML/CSS로 구현
- 브라우저에서 정상 동작 확인
- 폰트/이미지 리소스 누락 확인

**Step 3 — 캡처**
- Puppeteer/Playwright 등으로 프레임 캡처
- 프레임 누락/깜빡임 확인
- 캡처 타임라인 기록

**Step 4 — 인코딩**
- GIF: 2-pass palettegen/paletteuse 인코딩
- MP4: H.264 + CRF 18
- 용량/품질 기준 충족 확인

**Step 5 — QA & 전달**
- 루프 연결성 확인 (시작/끝 프레임 시각차 5% 이하)
- 텍스트 가독성 점검
- 출력 파일 경로와 재실행 명령 전달

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| 폰트 깨짐/누락 | 캡처 결과에서 텍스트 렌더링 이상 | 웹폰트 preload 후 1회 재캡처, 실패 시 시스템 폰트로 fallback |
| GIF 용량 8MB 초과 | 인코딩 후 파일 크기 확인 | fps를 2단계 낮추고 색상 수 조정 후 재인코딩 |
| 프레임 드랍 발생 | 캡처 프레임 수 vs 예상 프레임 수 불일치 | 캡처 해상도 한 단계 하향, 안정 렌더 후 결과 분리 보고 |
| 애니메이션 타이밍 불일치 | QA에서 텍스트 노출 2초 미달 | CSS animation-delay 재조정 후 재캡처 |

---

## Quality Gate

- [ ] 전달 메시지가 1문장으로 확정되었는가 (Yes/No)
- [ ] GIF fps 12 / MP4 fps 30 기준이 충족되는가 (Yes/No)
- [ ] GIF 용량 8MB 이하인가 (Yes/No)
- [ ] 텍스트 최소 노출 시간 2초가 확보되었는가 (Yes/No)
- [ ] 캡처/인코딩 명령이 복붙 실행 가능한 형태로 제공되는가 (Yes/No)
- [ ] 루프형일 경우 시작/끝 프레임 시각차 5% 이하인가 (Yes/No)

---

## Examples

### Good Example
**요청:** "3-Tier 에이전트 아키텍처를 설명하는 GIF 만들어줘. 사용자 입력 → Orchestrator → Sub-agent 흐름이 순차적으로 나타나게."

**왜 좋은 요청인가:**
- 시각화 대상 (3-Tier 아키텍처), 포맷 (GIF), 애니메이션 방식 (순차 등장)이 명확
- 바로 장면 설계로 진입 가능

**기대 결과:**
- 3단계 순차 등장 애니메이션 (각 2초)
- 1280×720, 12fps GIF, 약 3MB
- 루프형으로 README 삽입 가능

### Bad Example
**요청:** "에이전트 아키텍처 그림 만들어줘."

**왜 나쁜 요청인가:**
- 정적 이미지인지 애니메이션인지 불명
- 어떤 아키텍처 패턴인지 불명
- Step 1 장면 설계에서 확인 질문 필요

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- FFmpeg 인코딩: palettegen/paletteuse 2-pass는 GIF 품질 최적화 표준 기법
- 캡처 도구: Puppeteer, Playwright, 또는 브라우저 내장 캡처
