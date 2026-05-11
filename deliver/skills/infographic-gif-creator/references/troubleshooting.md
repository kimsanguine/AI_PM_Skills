# Troubleshooting — infographic-gif-creator 스킬

## 1) 프레임 캡처 실패 또는 프레임 드롭 발생

**증상:**
- "캡처되는 프레임 수가 96개여야 하는데 92개만 나왔어요."
- "스크린샷 첫 몇 개가 공백으로 나옵니다."
- "특정 프레임에서 애니메이션이 깜빡이거나 건너뜁니다."

**확인:**
- 캡처 방법 확인: CDP beginFrame / CSS animation-play-state / animationend 중 어떤 방식 사용?
- Puppeteer 버전: 19.0 이상인가? (beginFrame 사용 가능)
- 예상 프레임 수 vs 실제 캡처 수 차이: ±1프레임 이내인가 아니면 2프레임 이상?
- 해상도/fps 설정: 너무 높으면 브라우저 렌더링 성능 저하

**조치:**
1. 프레임 드롭 원인 파악:
   ```bash
   # 예상 프레임 수 계산
   expected_frames=$(echo "duration_seconds * fps" | bc)  # 예: 8초 × 12fps = 96
   actual_frames=$(ls frames/*.png | wc -l)
   echo "Expected: $expected_frames, Actual: $actual_frames"
   ```
2. 캡처 방법 단계별 하향:
   - Puppeteer ≥19.0 + CDP beginFrame → 다른 환경에서 테스트
   - CSS animation-play-state 제어 방식으로 전환 (paused→play)
   - 최후 수단: animationend 이벤트 기반 (타이밍 오차 감수)
3. 해상도/fps 낮추기로 렌더링 안정성 확보:
   - 1280×720, 12fps → 1024×576, 10fps로 재시도
4. HTML/CSS 재점검: animation-delay가 정확한가? 중간에 애니메이션이 끝나지는 않나?

---

## 2) 생성된 GIF 파일이 8MB를 초과할 때

**증상:**
- GIF 파일이 12MB, 15MB 등 너무 큼
- 용량 제약 플랫폼(Slack, 이메일)에 업로드 불가
- 다운로드/재생이 느림

**확인:**
- 현재 GIF 설정: fps, 해상도, 색상 수 확인
- 압축 알고리즘: palettegen dither 방식 (sierra2 vs bayer 등)
- gifsicle lossy 적용 여부
- 1회 시도한 최적화 방법

**조치:**
1. 단계별 최적화 (도메인 파일 Section 8-f 참고):
   ```bash
   # 1단계: fps 낮추기 (12 → 10 → 8)
   ffmpeg -i frames/%04d.png -vf "fps=10,scale=1280:-1" -c:v copy output_v1.gif

   # 2단계: 해상도 축소 (1280 → 1024 → 960)
   ffmpeg -i frames/%04d.png -vf "fps=12,scale=1024:-1" output_v2.gif

   # 3단계: 색상 제한 (256 → 128 → 64)
   ffmpeg -i frames/%04d.png -vf "fps=12,palettegen=max_colors=128" palette.png
   ffmpeg -i frames/%04d.png -i palette.png -lavfi "[v][1:v]paletteuse" output_v3.gif

   # 4단계: gifsicle lossy (무손실 대비 15-30% 추가 감소)
   gifsicle --lossy=20 input.gif -o output_lossy.gif
   ```
2. 각 단계마다 파일 크기 확인 → 목표(8MB) 달성 후 중단
3. 품질 vs 크기 트레이드오프:
   - fps 낮추기: 부드러움 감소 ↓
   - 해상도 축소: 선명도 감소 ↓
   - 색상 제한: 색감 손상 가능 ↓
   - gifsicle lossy: 육안 차이 거의 없음 (가장 추천)

---

## 3) 애니메이션 타이밍이 불일치하거나 지연되는 경우

**증상:**
- "텍스트가 너무 빨리 지나가서 못 읽어요."
- "각 단계 사이의 전환이 끊어진 것처럼 느껴져요."
- "1초 딜레이를 설정했는데 실제로는 더 길어요."

**확인:**
- 텍스트 최소 노출 시간: `(글자 수 ÷ 12) + 1초` 공식 적용했는가?
- CSS animation-delay 값: 프레임 단위인가 밀리초인가? (혼동 가능)
- 캡처 방식의 타이밍 오차: ±2-3프레임 오차가 있는가?
- 전체 duration과 캡처 프레임 수: 일치하는가?

**조치:**
1. 타이밍 공식 재확인:
   - 100글자 텍스트 → (100 ÷ 12) + 1 = 9.3초 필요
   - fps=12 → 9.3초 = 111프레임 필요
2. CSS animation-delay 재계산 (프레임 → 밀리초):
   ```css
   .step-1 { animation-delay: 0s; }       /* 0프레임 */
   .step-2 { animation-delay: 2s; }       /* 24프레임 at 12fps */
   .step-3 { animation-delay: 4s; }       /* 48프레임 */
   ```
3. 각 프레임의 예상 타이밍 주석 추가:
   ```typescript
   <Sequence from={0} durationInFrames={96}>      {/* 0~8초 */}
   ```
4. 재캡처 후 프레임 구간별로 육안 검토 (처음/중간/끝)

---

## 4) 폰트가 깨지거나 누락된 경우

**증상:**
- "텍스트가 사각형이나 물음표로 보입니다."
- "특정 폰트를 지정했는데 기본 폰트로 렌더됩니다."
- "웹폰트가 로드되지 않았어요."

**확인:**
- HTML의 `<link>` 또는 `@import` 폰트 선언 확인
- 폰트 파일의 절대 경로/상대 경로가 맞는가?
- Puppeteer가 폰트 로드를 기다리는 시간 충분한가?

**조치:**
1. 웹폰트 preload 추가:
   ```html
   <link rel="preload" as="font" href="./fonts/Roboto-Bold.woff2" type="font/woff2">
   <style>
     @font-face {
       font-family: 'Roboto';
       src: url('./fonts/Roboto-Bold.woff2') format('woff2');
     }
     body { font-family: 'Roboto', sans-serif; }
   </style>
   ```
2. Puppeteer 대기 시간 증가:
   ```javascript
   await page.goto('file:///path/to/scene.html', { waitUntil: 'networkidle2' });
   await new Promise(r => setTimeout(r, 2000)); // 추가 대기
   ```
3. 실패 시 폰트를 시스템 폰트로 fallback:
   ```css
   body { font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
   ```
4. 1회 재캡처 후 폰트 렌더링 확인

---

## 5) 루프형 GIF에서 시작/끝 연결이 어색할 때

**증상:**
- "GIF가 반복될 때마다 깜빡거리거나 끊어집니다."
- "마지막 프레임과 첫 번째 프레임이 너무 달라요."
- "루프가 자연스럽지 않습니다."

**확인:**
- 시작 프레임과 끝 프레임의 시각차: 5% 이내?
- CSS animation이 마지막에 원래 상태로 돌아가는가?
- 전체 duration과 animation-duration이 일치하는가?

**조치:**
1. 루프 연속성 설계: 마지막 1-2초에서 시작 상태로 돌아가기
   ```css
   @keyframes loop {
     0% { transform: translateX(0); }       /* 시작 */
     85% { transform: translateX(100px); }  /* 최고점 */
     100% { transform: translateX(0); }     /* 끝 = 시작과 동일 */
   }
   .element { animation: loop 8s infinite; }
   ```
2. 시작/끝 프레임 비교:
   - 첫 번째 캡처 프레임과 마지막 캡처 프레임의 스크린샷 육안 비교
   - 색상, 위치, 텍스트 모두 일치해야 함
3. 시각차 5% 이내 확인:
   - 예: 100프레임 GIF → 시각차 ≤ 5프레임
4. 재캡처 및 QA 재점검

---

