---
name: infographic-gif-creator
description: "Create animated infographics (GIF/MP4) from HTML/CSS to visualize agent architectures, workflows, and data flows. Use when you need visual explanations for stakeholder communication, documentation, or demo materials. Routes to compose-video for multi-scene final rendering."
argument-hint: "[infographic topic or data to visualize]"
allowed-tools: ["Read", "Write", "Edit", "Bash"]
model: sonnet
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
  - 예: "사용자 입력이 Orchestrator를 거쳐 3개 Sub-agent로 분기되고 결과가 통합된다"
- 키프레임 수와 타이밍을 결정 (텍스트 최소 노출: `(글자 수 ÷ 12) + 1`초)
- 루프/비루프 결정

**Step 2 — HTML/CSS 구현**
- 애니메이션 장면을 HTML/CSS로 구현 (GPU 가속: `transform`과 `opacity` 속성 우선 사용)
- 브라우저에서 정상 동작 확인
- 폰트/이미지 리소스 누락 확인 (모든 리소스 inline 또는 로컬 경로)

기본 HTML 템플릿:
```html
<div class="scene" style="width:1280px; height:720px; background:#1a1a2e; overflow:hidden;">
  <div class="step" style="opacity:0; animation: fadeIn 0.5s forwards; animation-delay:0s;">Step 1</div>
  <div class="step" style="opacity:0; animation: fadeIn 0.5s forwards; animation-delay:2s;">Step 2</div>
</div>
<style>
@keyframes fadeIn { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }
</style>
```

**Step 3 — 캡처** (우선순위 기반 방법 선택)

> **CDP beginFrame이란?** Chrome DevTools Protocol의 프레임 제어 기능. 브라우저가 비동기로 렌더링하는 대신, 명시적으로 프레임 렌더를 트리거하여 결정적(deterministic) 타이밍을 보장한다.

캡처 방법 의사결정:
```
Puppeteer ≥19.0?
├── Yes → CDP beginFrame 사용 (권장, 결정적 타이밍 보장)
│         → 프레임 드롭 없음, ±1프레임 오차
└── No
    ├── CSS animation-play-state 제어 가능?
    │   └── Yes → paused→play 트리거 방식 (대안)
    │             animation-play-state: paused → JS로 play() 트리거 후 캡처 시작
    └── No → animationend 이벤트 기반 (최후 수단)
              비결정적 타이밍, 프레임 오차 ±2-3프레임
```

Puppeteer CDP beginFrame 캡처 예시:
```javascript
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  await page.goto('file:///path/to/scene.html');
  const client = await page.target().createCDPSession();
  const totalFrames = 96; // 8초 × 12fps
  for (let i = 0; i < totalFrames; i++) {
    await client.send('HeadlessExperimental.beginFrame');
    await page.screenshot({ path: `frames/${String(i).padStart(4, '0')}.png` });
  }
  await browser.close();
})();
```

- 선택한 방법으로 프레임 캡처 실행
- 프레임 누락/깜빡임 확인 (예상 프레임 수 vs 실제 캡처 수, 오차 ±1프레임 이내)
- 캡처 타임라인 기록
- **프레임 드롭 진단**: 캡처된 프레임 수가 예상보다 적으면 (예: 96개 중 93개) → 캡처 방법 한 단계 하향 또는 해상도 축소

> **Puppeteer/Playwright 모두 사용 가능**: CDP beginFrame은 Puppeteer에서 가장 안정적이나, Playwright에서도 `page.clock` API 또는 `animation.pause()/play()` 조합으로 동등한 결과 달성 가능. 프로젝트 기존 도구에 맞춰 선택.

**Step 4 — 인코딩**

GIF (2-pass):
```bash
ffmpeg -i frames/%04d.png -vf "fps=12,scale=1280:-1:flags=lanczos,palettegen=stats_mode=diff" palette.png
ffmpeg -i frames/%04d.png -i palette.png -lavfi "fps=12,scale=1280:-1:flags=lanczos[v];[v][1:v]paletteuse=dither=sierra2" output.gif
```

MP4:
```bash
ffmpeg -i frames/%04d.png -c:v libx264 -preset medium -crf 22 -pix_fmt yuv420p -r 30 output.mp4
```

- 용량/품질 기준 충족 확인 (GIF ≤8MB, MP4 ≤50MB)
- 초과 시 단계적 최적화:
  1. fps 낮추기 (12→10→8)
  2. 해상도 축소 (1280→1024→960)
  3. 색상 수 제한 (256→128→64색, palettegen `max_colors` 옵션)
  4. gifsicle lossy 후처리: `gifsicle --lossy=20 input.gif -o output.gif` (육안 차이 거의 없음, 15-30% 추가 감소)
  5. 상세 옵션은 domain.md Section 8-f 참조

**Step 5 — QA & 전달**
- 루프 연결성 확인 (시작/끝 프레임 시각차 5% 이하)
- 텍스트 가독성 점검
- 출력 파일 경로와 재실행 명령 전달

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| 폰트 깨짐/누락 | 캡처 결과에서 텍스트 렌더링 이상 | 웹폰트 preload 후 1회 재캡처, 실패 시 시스템 폰트로 fallback |
| GIF 용량 8MB 초과 | 인코딩 후 파일 크기 확인 | fps를 2단계 낮추고 색상 수 조정 후 재인코딩 (domain.md Section 8-f 참조) |
| 프레임 드랍 발생 | 캡처 프레임 수 vs 예상 프레임 수 불일치 | 캡처 해상도 한 단계 하향, 안정 렌더 후 결과 분리 보고 |
| 애니메이션 타이밍 불일치 | QA에서 텍스트 노출 2초 미달 | CSS animation-delay 재조정 후 재캡처 |
| CSS-캡처 타이밍 동기화 실패 | 첫 프레임 공백 또는 중간 프레임 누락 | 캡처 방법 한 단계 하향 (CDP→paused/play→animationend), domain.md Section 8-a 참조 |

---

## Quality Gate

- [ ] 전달 메시지가 1문장으로 확정되었는가 (Yes/No)
- [ ] GIF fps 12 / MP4 fps 30 기준이 충족되는가 (Yes/No)
- [ ] GIF 용량 8MB 이하인가 (Yes/No)
- [ ] 텍스트 최소 노출 시간: `(글자 수 ÷ 12) + 1`초 이상 확보 (Yes/No)
- [ ] 캡처 정확도: 예상 프레임 수 대비 오차 ±1프레임 이내 (Yes/No)
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
- 설계자: AI PM Skills Contributors, 2026-03
- FFmpeg 인코딩: palettegen/paletteuse 2-pass는 GIF 품질 최적화 표준 기법
- 캡처 도구: Puppeteer, Playwright, 또는 브라우저 내장 캡처

## Contextual Knowledge (auto-loaded)

> 보조 파일이 존재할 때만 자동 로드됩니다. 파일이 없으면 건너뜁니다.

### Test Cases
!`cat references/test-cases.md 2>/dev/null || echo ""`

### Troubleshooting
!`cat references/troubleshooting.md 2>/dev/null || echo ""`

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Bad Example
!`cat examples/bad-01.md 2>/dev/null || echo ""`

### Domain Context
!`cat context/domain.md 2>/dev/null || echo ""`
