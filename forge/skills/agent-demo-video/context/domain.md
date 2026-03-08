# Domain Context — agent-demo-video 스킬

## 1) Domain Scope

**이 스킬이 소유하는 영역:**
- Remotion 기반 데모 영상 Composition 설계
- 스토리라인 구조 (Hook → 문제 → 데모 → 성과 → CTA)
- Scene별 컴포넌트와 타이밍 설정
- 렌더 명령 및 QA

**이 스킬이 소유하지 않는 영역:**
- 스크린 레코딩 기술적 구현 (별도 도구 사용)
- TTS 나레이션 생성 (외부 TTS 서비스)
- 원천 에셋(배경음, 이미지) 생성

## 2) Primary Users

- **PM/마케팅**: 에이전트 설득 영상 필요
- **투자자 관계**: 데모 영상으로 가치 전달
- **개발자**: 에이전트 동작 시각화

## 3) Required Inputs

**필수 입력:**
1. 에이전트 이름/설명
2. 스토리라인 (또는 핵심 메시지 3개)
3. 청중과 영상 길이
4. 스크린 레코딩 또는 시각화 소재

**선택 입력:**
- 나레이션 스크립트
- 배경음 파일

## 4) Output Contract

**산출물:**
- Remotion Composition 코드
- Scene별 duration(프레임 단위)
- 렌더 명령 (npx remotion render...)
- QA 샘플 프레임 (시작/중간/끝)

| 항목 | 보증 |
|------|------|
| 스토리라인 | 5단계 모두 포함 |
| 해상도/fps | 1920×1080, 30fps |
| Duration | 총합 오차 ±1프레임 |
| QA 프레임 | 3구간 샘플 |

## 5) Guardrails

**라우팅 규칙:**
- 정적 슬라이드만 필요 → `pptx-ai-slide`
- 짧은 GIF → `infographic-gif-creator`
- 에이전트 아키텍처 설계 → `atlas/orchestration`

**품질 기준:**
- 1920×1080, 30fps 필수
- 샘플 QA 3구간 필수
- 데이터 바인딩 null-safe 처리

## 6) Working Facts

**데모 영상 5단계 구조:**

| 단계 | 시간 | 내용 | 목표 |
|------|------|------|------|
| Hook | 0~5s | "이 에이전트는 문제를 자동으로 해결" | 관심 끌기 |
| Problem | 5~15s | 현재 수동 프로세스의 고통 포인트 | 필요성 확인 |
| Demo | 15~45s | 에이전트 실행 + 아키텍처 오버레이 | 동작 설명 |
| Impact | 45~55s | Before/After 비교 (숫자 강조) | 성과 입증 |
| CTA | 55~60s | 다음 단계 안내 | 행동 유도 |

**Remotion Composition 기본 구조:**

| 항목 | 설정 |
|------|------|
| fps | 30 |
| 해상도 | 1920×1080 |
| 길이 | 60초 = 1800프레임 |
| 프레임 계산 | 초 × 30 = 프레임 수 |

**TO BE UPDATED by reviewer:**
- 조직별 영상 길이 표준 (30초? 60초? 90초?)
- Scene 구성 패턴 (Hook 필수? 또는 문제 먼저?)
- 데이터 바인딩 템플릿

## 7) Fill-in Checklist

- [ ] 스토리라인 5단계(Hook/문제/데모/성과/CTA)가 모두 포함되었는가?
- [ ] 해상도 1920×1080, fps 30이 설정되었는가?
- [ ] Scene별 duration이 프레임 단위로 명시되었는가?
- [ ] Remotion render 명령이 복붙 실행 가능 형태로 제공되었는가?
- [ ] Duration 총합이 ±1프레임 오차 이내인가?
- [ ] QA 샘플 프레임(시작/중간/끝) 3구간이 포함되었는가?
- [ ] 데이터 바인딩(props)의 null-safe 처리가 확인되었는가?
