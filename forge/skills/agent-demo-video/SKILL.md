---
name: agent-demo-video
description: "Create demo videos for AI agents using Remotion (React-based video framework). Compose screen recordings, architecture animations, narration, and subtitles into polished demo videos. Use when showcasing agent capabilities to stakeholders, investors, or users."
argument-hint: "[agent to create demo video for]"
allowed-tools: ["Read", "Write", "Edit", "Bash"]
model: sonnet
---

## Core Goal
- 에이전트의 동작과 가치를 영상으로 설득력 있게 전달한다.
- Remotion 기반으로 재현 가능하고 수정 용이한 영상 파이프라인을 구축한다.
- 화면 녹화, 아키텍처 애니메이션, 나레이션, 자막을 하나의 영상으로 합성한다.

---

## Trigger Gate

### Use This Skill When
- 에이전트 데모 영상을 제작해야 할 때
- 투자자/이해관계자에게 에이전트 동작을 보여줘야 할 때
- 제품 랜딩페이지용 소개 영상이 필요할 때
- 에이전트 워크플로우를 시각적으로 설명하는 영상을 만들어야 할 때

### Route to Other Skills When
- 정적 슬라이드(PPTX)만 필요하면 → `pptx-ai-slide`
- 짧은 인포그래픽 GIF만 필요하면 → `infographic-gif-creator`
- 에이전트 아키텍처 설계 자체가 목적이면 → `3-tier` 또는 `orchestration`
- TTS 나레이션 생성만 필요하면 → 외부 TTS 서비스 연동

### Boundary Checks
- 이 스킬은 Remotion 기반 영상 composition 전용이다.
- 에이전트 설계/전략 수립은 범위 밖이다.
- 원천 에셋(TTS/자막/배경 이미지) 생성은 별도 도구로 처리한다.
- 최종 FFmpeg 후처리(인코딩 최적화, 포맷 변환)는 별도 파이프라인으로 분리한다.

---

## 왜 에이전트 데모 영상인가?

에이전트는 "보이지 않는 제품"입니다. 데모 영상은 이 gap을 메웁니다.

| 설명 방식 | 효과 | 한계 |
|---|---|---|
| 텍스트 설명 | 정확하지만 추상적 | 동작 흐름을 상상해야 함 |
| 스크린샷 | 결과물을 보여줌 | 과정이 보이지 않음 |
| 라이브 데모 | 가장 설득력 높음 | 실패 리스크, 재현 불가 |
| **데모 영상** | **과정+결과를 안전하게 전달** | **제작 시간 필요** |

### 데모 영상 구성 요소

```
1. Hook (0~5초)
   - "이 에이전트는 [문제]를 자동으로 해결합니다"
   - 핵심 가치 1문장

2. 문제 제시 (5~15초)
   - 현재 수동 프로세스의 고통 포인트
   - 시간/비용 낭비 시각화

3. 솔루션 데모 (15~45초)
   - 에이전트 실행 화면 (스크린 레코딩)
   - 아키텍처 오버레이 (어떤 단계에서 무엇을 하는지)
   - 결과물 하이라이트

4. 성과 (45~55초)
   - Before/After 비교 (시간, 비용, 정확도)
   - 핵심 숫자 강조

5. CTA (55~60초)
   - 다음 단계 안내
```

---

## Remotion 기반 영상 제작

### Remotion이 적합한 이유

| 기능 | Remotion | 전통 영상 편집 |
|---|---|---|
| 수정 용이성 | 코드 수정 → 즉시 재렌더 | 타임라인 재편집 필요 |
| 데이터 바인딩 | props로 동적 콘텐츠 | 수동 텍스트 교체 |
| 재현성 | Git으로 버전 관리 | 프로젝트 파일 의존 |
| 템플릿화 | 컴포넌트 재사용 | 프리셋 제한적 |

### Composition 구조

```typescript
// 기본 구조
const AgentDemo: React.FC = () => {
  return (
    <Composition
      id="agent-demo"
      component={DemoVideo}
      width={1920}
      height={1080}
      fps={30}
      durationInFrames={1800}  // 60초
    />
  );
};

// Scene 분리
const DemoVideo: React.FC = () => {
  return (
    <>
      <Sequence from={0} durationInFrames={150}>
        <HookScene />           {/* 0~5초 */}
      </Sequence>
      <Sequence from={150} durationInFrames={300}>
        <ProblemScene />        {/* 5~15초 */}
      </Sequence>
      <Sequence from={450} durationInFrames={900}>
        <DemoScene />           {/* 15~45초 */}
      </Sequence>
      <Sequence from={1350} durationInFrames={300}>
        <ResultScene />         {/* 45~55초 */}
      </Sequence>
      <Sequence from={1650} durationInFrames={150}>
        <CTAScene />            {/* 55~60초 */}
      </Sequence>
    </>
  );
};
```

### 렌더 명령

```bash
# 프리뷰
npx remotion preview src/index.ts

# 최종 렌더
npx remotion render src/index.ts agent-demo output.mp4 \
  --fps=30 --width=1920 --height=1080
```

---

## Instructions

You are creating a demo video for: **$ARGUMENTS**

**Step 1 — 스토리라인 설계**
- 에이전트의 핵심 가치를 1문장으로 정리
- 5단계 구조 (Hook → 문제 → 데모 → 성과 → CTA)에 맞춰 내용 배치
- 총 영상 길이 결정 (권장: 30~90초)

**Step 2 — Composition 설계**
- Scene별 duration을 프레임 단위로 명시
- 컴포넌트 책임 분리 (각 Scene = 독립 컴포넌트)
- 데이터 바인딩 필드 정의 (동적 콘텐츠)

**Step 3 — 타임라인 구현**
- 시퀀스/트랜지션/애니메이션 구현
- 텍스트 애니메이션: spring() 또는 interpolate() 사용
- 데이터 바인딩 null-safe 처리

**Step 4 — 에셋 통합**
- 스크린 레코딩 삽입 (있는 경우)
- 배경 음악/나레이션 싱크
- 자막 타이밍 확인

**Step 5 — 렌더 & QA**
- 1920×1080, 30fps로 렌더
- 시작/중간/끝 3구간 프레임 캡처로 QA
- 오디오-비주얼 싱크 확인
- 최종 파일 경로와 렌더 명령 전달

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| 스토리라인 불명확 | Step 1에서 핵심 가치 문장 부재 | 에이전트 PRD/OKR 참조 요청, 없으면 3개 후보 제시 |
| 렌더 실패 | Remotion 빌드 에러 | 실패 프레임 구간/원인(에셋 누락/코드 에러/메모리) 분리 보고 |
| 타임라인 불일치 | 총 duration이 예상과 ±1프레임 이상 차이 | duration 매핑표 재생성 후 1회 재렌더 |
| 오디오-비주얼 싱크 어긋남 | QA에서 음성/자막과 화면 타이밍 불일치 | 오프셋 값 계산 후 Sequence from 조정 |

---

## Quality Gate

- [ ] 스토리라인 5단계(Hook/문제/데모/성과/CTA)가 모두 포함되었는가 (5/5)
- [ ] 해상도 1920×1080, fps 30 기준이 충족되는가 (Yes/No)
- [ ] 표준 remotion render 명령이 복붙 실행 가능 형태로 제공되는가 (Yes/No)
- [ ] Scene별 duration 총합 오차가 ±1프레임 이내인가 (Yes/No)
- [ ] 샘플 QA 3구간(시작/중간/끝) 프레임 캡처가 포함되는가 (3/3)
- [ ] 데이터 바인딩 필드의 null-safe 처리가 확인되었는가 (Yes/No)

---

## Examples

### Good Example
**요청:** "고객 문의 자동 분류 에이전트 데모 영상 만들어줘. Slack에서 문의가 들어오면 자동으로 분류하고 담당자에게 배정하는 과정을 보여줘야 해. 투자자 발표용 60초."

**왜 좋은 요청인가:**
- 에이전트 (고객 문의 분류), 워크플로우 (Slack→분류→배정), 청중 (투자자), 길이 (60초)가 명확
- 바로 스토리라인 설계 진입 가능

**기대 결과:**
- 60초 데모 영상: Hook(5s)→문제(10s)→데모(30s)→성과(10s)→CTA(5s)
- Slack 메시지 수신 → 분류 판단 오버레이 → 배정 알림 시퀀스
- Before: 평균 30분 수동 분류 → After: 10초 자동 분류 비교 차트

### Bad Example
**요청:** "에이전트 영상 만들어줘."

**왜 나쁜 요청인가:**
- 어떤 에이전트인지, 무엇을 보여줄지, 누구에게 보여줄지, 길이 전부 불명
- Step 1에서 최소 3개 확인 질문 필요

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- Remotion 공식 문서: https://www.remotion.dev/docs
- 데모 영상 5단계 구조: SaaS 데모 영상 베스트 프랙티스 기반
- Before/After 패턴: Y Combinator Demo Day 발표 구조 참조
