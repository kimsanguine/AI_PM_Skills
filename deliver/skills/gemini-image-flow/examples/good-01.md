# Good Example — gemini-image-flow 스킬

## 사용자 요청

"Gemini를 이용한 UI/디자인 자동 생성 파이프라인을 설계해줄래? 사용자가 프로젝트 설명을 입력하면, 이미지가 생성되고, 그 이미지를 React 코드로 변환하는 sketch-to-code 파이프라인까지."

## 승인 이유

- Gemini 기반 이미지 생성 파이프라인 엔드투엔드 설계 필요
- Phase 0(API 준비)부터 Phase 7(테스트)까지 체계적 구성
- Flash/Pro 모델 티어 선택 및 비용 최적화

## 예상 처리

1. Phase 0: API 환경 준비 (키 발급, 환경변수, 연결 테스트)
2. Phase 1: 파이프라인 아키텍처 설계
3. Phase 2: 인텐트 수집 (CLI 질문 흐름, --quick 프리셋)
4. Phase 3: 프롬프트 템플릿 (기본 + 프로젝트별 세그먼트)
5. Phase 4: Gemini API 설정 (Flash vs Pro, 에러 처리)
6. Phase 5: 후속 파이프라인 (sketch-to-code 정의)
7. Phase 7: 테스트 시나리오 (T1~T8)

## 최종 결과물

프로토타입부터 프로덕션까지 일관성 있게 구현 가능한 Gemini 이미지 생성 파이프라인
