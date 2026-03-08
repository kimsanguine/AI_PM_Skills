# Troubleshooting — agent-demo-video 스킬

## 1) 스토리라인이 불명확하거나 단편적일 때

**증상:**
- "이 스토리라인으로 영상을 만들었는데 뭔가 중간에 떨어진 느낌이에요."
- "Hook과 Problem은 있는데 Solution이 너무 짧습니다."
- "투자자들이 이 영상에서 value proposition을 못 알아주는 것 같아요."

**확인:**
- 5단계(Hook/Problem/Demo/Result/CTA) 구조가 모두 포함되었는가?
- 각 단계가 명확한 전환점(transition)을 가지고 있는가?
- Hook에서 제시한 "문제"가 Problem 단계에서 구체적으로 설명되는가?
- Solution(Demo) 단계에서 에이전트의 역할이 명확하게 드러나는가?

**조치:**
1. 요청자에게 이 질문 3개를 던지기: "이 에이전트의 핵심 가치는 무엇인가?", "사용 전/후 비교는?", "시청자에게 전달해야 할 메시지 1개는?"
2. 스토리라인의 각 단계별 시간 배분 재조정 (보통 Problem 단계를 과하게 길게 → 데모 시간 부족)
3. Before/After 수치(시간 절감, 오류 감소, 비용 절감) 명시 → Result 단계에 하드 숫자 추가
4. 최종 CTA 명확화: "이 에이전트를 어떻게 만나나?", "다음은 무엇인가?"

---

## 2) Remotion 렌더 실패 또는 에러 발생

**증상:**
- `npx remotion render` 명령 실행 후 "Error: component not found" 또는 "Cannot read properties of undefined"
- 빌드는 성공하는데 특정 씬만 렌더링 실패
- 메모리 부족으로 렌더링 중단 (특히 고해상도)

**확인:**
- 콘솔 에러 메시지에서 실패 지점(프레임 번호)과 원인 파악
- TypeScript 컴파일이 성공했는가? (`npx tsc --noEmit`)
- 모든 컴포넌트가 정의되어 있는가? (import 누락 확인)
- 동적 데이터(props)가 undefined로 전달되고 있지 않은가?

**조치:**
1. 에러 메시지의 프레임 번호 확인 → "어느 씬에서 실패했는가" 파악
2. 해당 씬의 코드 재검토: props 기본값 설정, null-safety 확인
   ```typescript
   // Bad
   <Text>{scene.title}</Text>  // scene이 undefined면 에러

   // Good
   <Text>{scene?.title || "Default Title"}</Text>
   ```
3. 해상도 낮춰서 재렌더 시도 (1920×1080 → 1280×720) → 메모리 문제 진단
4. 특정 에셋(이미지, 폰트) 누락 확인 → 로컬 경로 또는 base64 inline으로 변경
5. 재렌더 후에도 실패 시, 해당 씬을 임시로 주석 처리해서 다른 씬이 렌더되는지 확인

---

## 3) 타이밍 불일치 또는 프레임 드롭

**증상:**
- "렌더된 영상에서 텍스트가 너무 빨리 지나가거나 너무 오래 남아있어요."
- "자막과 나레이션이 5프레임 밀려 있습니다."
- "애니메이션이 프레임을 건너뛴 것처럼 끊어 보입니다."

**확인:**
- 설정된 fps와 duration이 예상과 일치하는가?
- Sequence의 `from`과 `durationInFrames`의 합이 전체 영상 길이와 일치하는가?
- CSS animation-delay 값이 프레임으로 올바르게 변환되었는가? (1초 = fps × 1, 기본 30fps면 30프레임)
- 오디오 트랙의 길이가 영상 길이와 일치하는가?

**조치:**
1. 타이밍 계산 재검토: `duration_in_frames ÷ fps = 초 단위`로 환산해서 확인
   - 예: fps=30, 5초 → 150프레임
2. 각 Sequence의 duration을 명시적으로 계산해서 주석 추가
   ```typescript
   <Sequence from={0} durationInFrames={150}>        {/* 0~5초 */}
   <Sequence from={150} durationInFrames={300}>      {/* 5~15초 */}
   // ... 합계 확인
   ```
3. 오디오 싱크 문제면, 오프셋 계산해서 `<Audio src="..." startFrom={frame_offset} />` 조정
4. 프레임 드롭이 심하면, fps 낮추기 (30→24 또는 24→20) 시도 → 부드러움과 파일 크기 트레이드오프

---

## 4) 데이터 바인딩 또는 props 전달 오류

**증상:**
- "매번 다른 에이전트 결과(생성된 텍스트, 이미지)를 넣으려는데 자동화할 수 없어요."
- "props가 제대로 전달되지 않아 영상에 동적 콘텐츠가 안 보입니다."
- "프로덕션 배포 시 데이터가 들어갈 자리를 어떻게 남겨둘지 모르겠어요."

**확인:**
- Composition에 정의된 props 인터페이스가 명확한가?
- 각 props의 기본값(default)이 설정되어 있는가?
- 컴포넌트 내부에서 props 사용 시 null 체크가 있는가?
- npx remotion render 명령에서 props 매핑 방식이 정의되었는가?

**조치:**
1. Props 인터페이스를 명시적으로 정의하고 기본값 설정
   ```typescript
   interface DemoProps {
     agentName: string;
     problemStatement: string;
     resultTime: number;
     resultCost: number;
   }

   export const AgentDemo: React.FC<DemoProps> = ({
     agentName = "Default Agent",
     problemStatement = "Problem to solve",
     resultTime = 0,
     resultCost = 0,
   }) => { ... }
   ```
2. 렌더 명령에서 props 전달 방식 문서화
   ```bash
   npx remotion render src/index.ts agent-demo output.mp4 \
     --props='{"agentName":"Customer Classifier","resultTime":300,"resultCost":45}' \
     --fps=30 --width=1920 --height=1080
   ```
3. 동적 이미지/비디오 삽입 시 파일 경로를 props로 받아 `<Img src={imagePath} />` 처리
4. 테스트용 샘플 데이터셋 prepare → 동일한 props로 여러 번 렌더 실행해서 재현성 확인

---

## 5) 해상도, 포맷, 또는 최적화 문제

**증상:**
- "렌더된 영상이 픽셀이 떨어져 보입니다. 고해상도로 못 하나요?"
- "MP4 파일 크기가 200MB인데 너무 커요."
- "투자자에게 보낼 공유 링크 형식이 뭐예요?"

**확인:**
- 렌더 명령에 사용된 해상도와 fps 값
- 최종 컨테이너 포맷(MP4 vs GIF vs WebM)
- FFmpeg 인코딩 옵션 (preset, crf 값)
- 대상 플랫폼 (웹 플레이어, Slack, 이메일 등) 제약

**조치:**
1. 고해상도 필요 시, 1920×1080, 30fps 기본 설정 유지 후 최종 FFmpeg 인코딩에서만 최적화
   ```bash
   ffmpeg -i output.mp4 -c:v libx264 -preset slow -crf 23 -pix_fmt yuv420p output_optimized.mp4
   ```
   - crf 값 낮을수록 품질 높음 (default 28, 추천 18-23)
   - preset 옵션: ultrafast/superfast/veryfast/faster/fast/medium/slow/slower (slow=최고품질, 시간 증가)
2. 파일 크기 감소: crf 값 높이기(23→25→27) 또는 해상도 낮추기(1920→1440)
3. 플랫폼별 포맷 권장
   - 웹: MP4 (H.264 코덱) + 모바일 최적화 crf 25-28
   - Slack: MP4 + 파일 크기 <50MB
   - 이메일: MP4 또는 GIF + 파일 크기 <10MB (GIF는 품질 저하 감수)
   - 랜딩 페이지 배경: WebM (VP8/VP9) + 무음 + 루프 설정
4. 공유 방식: 로컬 MP4 대신 YouTube/Vimeo 업로드 후 embed → 해상도 유연성 + 재생 호환성

---

