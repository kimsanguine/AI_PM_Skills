# 도메인 컨텍스트 — Infographic GIF Creator

## 1) Domain Scope

**목적**: HTML/CSS 기반 애니메이션을 GIF 또는 MP4로 변환하여 에이전트 아키텍처, 워크플로우, 시스템 플로우 등을 시각화하는 동영상 인포그래픽 생성.

**입력 형식**: HTML 파일 (CSS 애니메이션 포함), 애니메이션 설정 메타데이터 (duration, fps, scene structure)

**출력 형식**: GIF (최대 5초, 10-15fps) 또는 MP4 (H.264, 가변 해상도)

**핵심 기술 스택**:
- Frame capture: Puppeteer / Playwright
- Video encoding: FFmpeg (libx264, palettegen/paletteuse)
- HTML/CSS 렌더링: Chrome DevTools Protocol (CDP) via Puppeteer

---

## 2) Primary Users

- AI PM: 프로젝트 로드맵, 의존성 흐름, 타임라인 시각화
- 기술 팀: 시스템 아키텍처, 데이터 흐름, API 통신 시퀀스 다이어그램
- 마케팅: 제품 기능 데모, 동작 원리 설명 비디오
- 교육/문서화: 복잡한 개념의 단계별 애니메이션 설명

---

## 3) Required Inputs

| 항목 | 포맷 | 설명 |
|------|------|------|
| HTML 콘텐츠 | `.html` 파일 | CSS 애니메이션 포함된 구조 (모든 리소스 inline 또는 relative path) |
| 애니메이션 duration | 정수 (초) | CSS `animation-duration`과 일치 (예시값: 2-8초, 도메인에 따라 조정) |
| Frame rate | 정수 (fps) | 예시값: 10-15fps GIF, 24-30fps MP4 |
| 해상도 | WIDTHxHEIGHT | 예시값: 1280x720 (도메인에 따라 조정) |
| 출력 형식 | `gif` \| `mp4` | 용도에 따라 선택 |
| Scene timing data | JSON 배열 | 각 scene의 시작/끝 지점 (ms 단위) |

---

## 4) Output Contract

**GIF 출력**:
- 파일 크기: 예시값 500KB-2MB (도메인에 따라 조정)
- 색상: 256색 최적화 (palettegen + dithering)
- 루프: 자동 반복 (무한 루프)
- 프레임 정확도: ±1프레임 오차 범위

**MP4 출력**:
- 코덱: H.264 (libx264)
- CRF: 예시값 22-26 (도메인에 따라 조정)
- 비트레이트: 자동 계산 (CRF 기반)

**보증 사항**:
- 애니메이션 타이밍 정확성 (±100ms 이내)
- 모든 프레임 동기화 (CSS animation과 frame capture 정렬)
- 루프 연속성 (시작/끝 프레임 일관성)

---

## 5) Guardrails

**금지 사항**:
- 초상권 침해 가능 시각적 요소 (인물 사진, 신원 확인 정보)
- 저작권 보유 음악/효과음 (메타데이터에 저작권 표시 필수)
- 광고/마케팅 개인정보 수집

**품질 기준**:
- 텍스트 가독성: 최소 12pt 이상 (해상도 1280x720 기준)
- 색상 대비: WCAG AA 이상 (배경과 전경 명도 비율 4.5:1)
- 애니메이션 부드러움: 프레임 드롭 없음 (Puppeteer captureStream 또는 CDP beginFrame 사용)

**성능 제약**:
- HTML 페이지 로딩 시간: 예시값 3초 이내 (외부 CDN 불가, 모든 리소스 로컬)
- Puppeteer 프로세스: 메모리 제한 500MB/인스턴스
- FFmpeg 인코딩: 예시값 30초 이내 (2-5초 애니메이션 기준)

---

## 6) Working Facts (TO BE UPDATED by reviewer)

- [ ] CSS 애니메이션 vs JavaScript 애니메이션: GPU 가속은 `transform`과 `opacity` 속성에만 적용 (성능 우선)
- [ ] Puppeteer frame capture 정확도: Chrome DevTools Protocol `beginFrame`을 사용할 때 ±1프레임 오차, `waitForTimeout` 단독 사용 시 ±2-3프레임 오차
- [ ] FFmpeg 2-pass GIF 인코딩 파일 크기: 1-pass (직접 256색) 대비 2-pass (palettegen) 약 15-25% 더 작음
- [ ] Dithering 알고리즘: Bayer > Sierra > Floyd-Steinberg (파일 크기 기준, 역순은 품질)
- [ ] MP4 CRF 값: CRF 22 = 약 4-5Mbps (1280x720, 30fps), ±6 변화 시 약 2배 파일 크기 변동

---

## 7) Fill-in Checklist

- [ ] HTML 파일이 모든 외부 리소스를 인라인화하거나 상대 경로로 포함했는가?
- [ ] 애니메이션 duration이 총 씬 길이와 일치하는가?
- [ ] CSS `animation-delay` 값이 메타데이터 scene timing과 동기화되었는가?
- [ ] 해상도가 대상 플랫폼 요구사항과 일치하는가 (웹: 1280x720, 모바일: 720x1280)?
- [ ] 텍스트 콘텐츠가 읽기 시간 공식(글자 수 ÷ 12 + 1초)을 만족하는가?
- [ ] 루프 시작/끝 프레임이 시각적으로 동일한가 (또는 fade transition 적용)?
- [ ] 색상 팔레트가 256색 이내로 제한되었는가?

---

## 8) 참고 사례: HTML/CSS → GIF 렌더링 파이프라인 실전

> 다음 섹션의 모든 예시는 도메인 문제 해결을 위한 참고 사례입니다.
> 특정 수치(fps, color count, CRF)는 프로젝트별로 조정이 필요합니다.

### a) CSS 애니메이션과 프레임 캡처의 타이밍 동기화 문제 해결

**문제**: CSS animation-delay와 프레임 캡처 시작 시점 사이의 불일치로 인해 애니메이션의 중간 프레임이 누락되거나 초반 프레임이 중복 캡처됨.

**근본 원인**:
- Puppeteer의 `page.screenshot()` 또는 `page.waitForTimeout()`은 벽시간(wall-clock time)에 기반
- CSS 애니메이션은 DOM rendering cycle에 동기화되므로, 프레임 캡처 시작 시점과 CSS animation start 사이에 시간 오차 발생

**해결책**:

1. **Chrome DevTools Protocol (CDP) `beginFrame` 사용** (권장):
   ```
   Puppeteer를 통해 CDP의 HeadlessExperimental.beginFrame() 메서드에 접근.
   페이지의 setTimeout, requestAnimationFrame, CSS animation이 모두
   demand-based frame (벽시간 무관)로 전환되어 결정적(deterministic) 타이밍 보장.
   애니메이션 duration이 정확히 측정되며 프레임 드롭 없음.
   ```

2. **CSS animation을 paused 상태로 시작 → JS로 play 트리거 → 프레임 캡처 시작**:
   ```
   HTML에 초기 상태로 animation-play-state: paused; 적용.
   Puppeteer page.evaluate() 내에서 window.requestAnimationFrame()을 호출하여
   animation.play()를 트리거 (또는 CSS class 토글로 paused → running 전환).
   그 직후 frame capture loop 시작.
   이렇게 하면 첫 프레임부터 애니메이션 시작점을 일관되게 캡처 가능.
   ```

3. **animationend 이벤트 기반 대기** (Playwright):
   ```
   page.waitForFunction()을 사용하여
   window.animationComplete === true 상태를 폴링.
   animation 엘리먼트에 animationend event listener를 등록하여
   window.animationComplete = true를 설정.
   단점: 프레임 캡처 시간은 여전히 비결정적 (사용 추천 안 함).
   ```

**참고 사례 (참고 자료)**: [Puppeteer: Fast Forward Animations](https://github.com/puppeteer/puppeteer/issues/453), [Playwright: Animation Waiting](https://github.com/microsoft/playwright/issues/4055)

### b) FFmpeg 2-pass GIF 인코딩 상세

**파이프라인**:

```
Pass 1: FFmpeg palettegen 필터로 컨텐츠에 최적화된 256색 팔레트 생성
   ffmpeg -i input.mp4 -vf "fps=15,scale=1280:-1,palettegen=stats_mode=diff" palette.png

Pass 2: 생성된 팔레트를 사용하여 GIF 인코딩
   ffmpeg -i input.mp4 -i palette.png -lavfi "fps=15,scale=1280:-1[x];[x][1:v]paletteuse=dither=sierra2:diff_mode=rectangle" output.gif
```

**palettegen 옵션**:
- `stats_mode=full`: 전체 프레임 분석 (정확도 높음, 처리 시간 길음, 대규모 데이터셋 용)
- `stats_mode=diff`: 인접 프레임 간 차이만 분석 (처리 속도 빠름, 충분한 색상 다양성, 대부분의 인포그래픽 추천)

**paletteuse dithering 알고리즘** (파일 크기 기준 오름차순):
- `dither=none`: 양자화만 수행, 색상 대역 경계 보이기 쉬움 (용량 최소, 품질 최악)
- `dither=bayer`: Bayer matrix ordered dithering, 특유의 체크 패턴 (LZW로 잘 압축, 중간 품질)
  - `bayer_scale=5`: 예시값 (패턴 강도, 1-5, 높을수록 패턴 더 뚜렷)
- `dither=sierra2`: Sierra Two-Row 오류 확산 (품질 우수, 파일 크기 더 큼)

**fps와 scale 최적 조합**:
| 목표 | fps | scale | 예상 크기 | 품질 |
|------|-----|-------|---------|------|
| 초경량 (모바일) | 10 | 640:-1 | 300KB | 낮음 |
| 균형 (웹) | 12-15 | 1024:-1 또는 1280:-1 | 800KB-1.5MB | 중상 |
| 고품질 | 20-25 | 1440:-1 | 2-4MB | 높음 |

**참고 사례 (참고 자료)**: [High Quality GIF with FFmpeg](https://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html), [FFmpeg GIF Optimization](https://www.ffmpeg.media/articles/working-with-gifs-convert-optimize)

### c) MP4 인코딩 (libx264)

**권장 설정** (에이전트 아키텍처 시각화 용도):

```
ffmpeg -i input.mp4 -c:v libx264 -preset medium -crf 22 -c:a aac -b:a 128k output.mp4
```

**CRF (Constant Rate Factor) 값**:
- 범위: 0-51 (낮을수록 고품질, 높을수록 저품질)
- 권장 범위: 18-28
  - CRF 18: 시각적 무손실 (파일 크기 큼, 고화질 영상용)
  - CRF 22: 고품질 (권장, 예시값, 대부분 용도)
  - CRF 26: 중간 품질 (웹 스트리밍)
- **중요**: ±6 변화 시 비트레이트 약 2배 변동

**preset 옵션** (빠른 순서):
- `ultrafast`: 매우 빠름, 낮은 압축률
- `superfast` / `veryfast`: 빠름, 일반적 용도
- `fast` / `medium`: 균형 (medium이 기본값, 권장)
- `slow` / `slower` / `veryslow`: 느림, 최대 압축률

**참고 사례 (참고 자료)**: [CRF Guide](https://slhck.info/video/2017/02/24/crf-guide.html), [FFmpeg CRF vs Bitrate](https://www.ffmpeg.media/articles/transcoding-crf-vs-bitrate-codecs-presets)

### d) 씬 설계 원칙

**인지 부하 최소화**:
- **한 프레임당 정보 단위 1-2개**: 너무 많은 요소가 동시에 나타나면 인지 혼란 유발
  - 예: 에이전트 노드 하나씩 fade-in (각 노드 0.5-1초) > 모든 노드 동시 표시
- **텍스트 노출 시간 계산**:
  - 공식: `(글자 수 ÷ 12) + 1` (초)
  - 예: "Agent Architecture" (19글자) → (19÷12) + 1 ≈ 2.6초 최소 노출 필요
- **시각적 계층 구조**:
  - Primary (핵심 개념): 크기 큼, 밝은 색, 먼저 등장
  - Secondary (지원 정보): 중간 크기, 보조 색
  - Tertiary (레이블): 작은 크기, 흐린 색

**참고 사례 (참고 자료)**: [Animation in Infographics](https://educationalvoice.co.uk/animation-in-infographics/), [Motion Design for Data Viz](https://www.toptal.com/designers/data-visualization/mobile-data-visualization)

### e) 루프 포인트 설계

**시작/끝 프레임 시각적 일관성 확보**:
- **Hard-cut 방식**: 시작 프레임 = 끝 프레임 (완전 동일)
  - 장점: 즉시 구현 (단순)
  - 단점: 루프 지점에서 순간적 변화 감지 가능

- **Fade transition 방식**: 끝 프레임을 페이드 아웃 → 시작 프레임을 페이드 인
  - 장점: 루프 지점 자연스러움
  - 단점: 프레임 추가 필요, 더 긴 duration

- **교차 페이드** (복합 방식):
  - 마지막 씬을 중간 지점에서 분할
  - 예: [A][B][C] → [B][C][A][B]로 재배열하면 C와 A가 자연스럽게 전환
  - 수학적 보장: 시작점과 끝점의 상태가 자동 일치

**참고 사례 (참고 자료)**: [Perfectly Looped GIFs](https://blog.jitter.video/perfectly-looped-gifs/), [Seamless Loop Design](https://www.linkedin.com/advice/3/how-can-you-create-seamless-loop-animated-gif-skills-graphic-design)

### f) 용량 최적화 전략

**색상 수 제한** (palettegen 후 quantize):
| 색상 수 | 품질 | 용량 | 용도 |
|--------|------|------|------|
| 256색 | 높음 | 기본값 | 고품질 필요 시 |
| 128색 | 중상 | -20% | 균형 추천 |
| 64색 | 중간 | -40% | 단순 도형/텍스트 |
| 32색 이하 | 낮음 | -60% | 초경량 (모바일) |

**해상도 축소 및 resampling**:
- `scale=lanczos` (권장): 고품질, 처리 시간 길음 (텍스트/에지 보존 우수)
- `scale=bilinear`: 빠름, 품질 낮음 (흐릿함)
- 트레이드오프: 1280x720 → 960x540 = 약 56% 용량 감소, 품질 약간 저하

**gifsicle lossy 최적화** (마지막 단계):
```
gifsicle --lossy=20 input.gif -o output.gif
# lossy 값: 1-200, 높을수록 더 공격적 압축
# 예: 10-30 범위에서 육안 차이 거의 없음, 용량 15-30% 추가 감소
```

**전체 최적화 파이프라인 예**:
```
원본 (2-5초, 30fps, 1280x720) → fps 15 + scale 1024:-1 + palettegen(diff) + dither(sierra2)
→ gifsicle --lossy=15 → 최종 크기 약 600KB-1MB
```

**참고 사례 (참고 자료)**: [GIF Color Optimization Guide](https://fastmakergif.com/blog/gif-color-palette-optimization), [Dithering Algorithms](https://copyprogramming.com/howto/how-to-remove-dithering-from-image-which-was-in-gif-format-before)

---

## 9) 추가 참고 자료

| 주제 | 출처 |
|------|------|
| CSS Animation Timing | [MDN: animation-timing-function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function) |
| Puppeteer Frame Capture | [Medium: Puppeteer to 8K Video](https://medium.com/@BBSRGUY/from-html-to-8k-video-turning-websites-web-animations-into-cinematic-movies-with-puppeteer-34c3b6d1349f) |
| requestAnimationFrame | [MDN: Window requestAnimationFrame](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame) |
| GIF 최적화 | [FFmpeg Media: Working with GIFs](https://www.ffmpeg.media/articles/working-with-gifs-convert-optimize) |
| H.264 인코딩 | [x264 Encoder Guide](https://ffmpeg.party/guides/x264/) |
