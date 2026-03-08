# Test Cases — gemini-image-flow 스킬

## 1) Trigger Tests

### Should Trigger (5)

1. "Gemini API를 쓰는 이미지 생성 파이프라인을 설계해 줄 수 있어? UI/UX 디자인부터 코드 구현까지 자동화하려고 해."
   - 이유: 플랫폼(Gemini) 명시, 파이프라인 목표(UI 설계→코드) 명확 → Phase 0~7 전체 설계 가능

2. "We need to create a workflow for automatically generating product mockups from text descriptions. Should we use Gemini Flash or Pro?"
   - 이유: 워크플로우(텍스트→이미지), 모델 선택 질문 → Phase 4 모델 티어 전략 설계 진입

3. "마케팅팀이 소셜 미디어 배너를 매주 50개씩 자동으로 만들어야 해. Gemini로 가능할까?"
   - 이유: 반복 작업(배치), 플랫폼(Gemini), 개수(50개) 제시 → Phase 6 비용 모델링 + 배치 설계

4. "현재 Gemini 플래시로 프로토타입을 만들고 있어. 최종 산출물은 고품질로 가야 하는데, Flash에서 Pro로 업그레이드하는 파이프라인을 설계해 줄 수 있어?"
   - 이유: 모델 티어 전환 요청 명시 → Phase 4 티어 전략 + Phase 6 비용 최적화

5. "생성된 이미지를 React 코드로 자동 구현하는 sketch-to-code 파이프라인을 Gemini와 함께 만들려고 해."
   - 이유: 후속 파이프라인(sketch→code) 요청 → Phase 5 파이프라인 연결 설계

### Should NOT Trigger (5)

1. "이미지 프롬프트 문장을 더 좋게 다듬어 줄 수 있어?"
   - 올바른 라우팅: 프롬프트 최적화 → `forge/prompt` (CRISP 프레임워크)

2. "우리 이미지 생성 비용을 시뮬레이션해 줄 수 있어? Flash vs Pro 모델로 1년 예상 비용이 뭘까요?"
   - 올바른 라우팅: 비용 분석 전문 → `oracle/cost-sim`

3. "Gemini 외에도 DALL-E, Midjourney와 비교해서 가장 저렴한 옵션을 추천해 줄 수 있어?"
   - 올바른 라우팅: 멀티 플랫폼 비교 → `build-or-buy` 또는 `atlas/router`

4. "생성된 이미지가 안전 필터에 자주 걸려요. 프롬프트를 우회할 수 있는 방법이 있을까요?"
   - 올바른 라우팅: 안전 정책은 우회 불가 (ethics boundary)

5. "정적 이미지 하나만 필요해요. 복잡한 파이프라인 없이 한 번에 만들어 줄 수 있어요?"
   - 올바른 라우팅: 일회성 생성 요청 → Gemini API 직접 호출 (스킬 불필요) 또는 `gemini-image-flow` 범위 밖

## 2) Edge Cases

### 경계 사례 (5)

1. **Phase 0 API 키 발급/환경변수 설정을 건너뛴 경우**
   - 입력: "코드는 준비됐는데 Phase 0이 뭐예요? 바로 이미지를 생성할 수 있지 않을까요?"
   - 예상 행동: Phase 0 강제 → 키 발급/설정 완료 없이 진행 불가 (SKILL.md Boundary Checks 명시)
   - 근거: Phase 0 누락 = Phase 4 렌더링에서 401/403 에러 반드시 발생 → 사전 검증 필수

2. **선택한 모델이 이미지 생성을 지원하지 않는 경우**
   - 입력: "gemini-2.5-flash 모델로 이미지를 생성했는데 'does not support image generation' 에러가 나요."
   - 예상 행동: 모델 ID 확인 → `-image` 변형(gemini-2.5-flash-image) 사용으로 수정 → Phase 7 테스트 재실행
   - 근거: Gemini API에서 이미지 지원 모델이 제한적 → 모델 선택 시 반드시 `-image` suffix 확인

3. **인텐트 수집(Phase 2) 중 사용자가 모든 질문을 건너뛰려는 경우**
   - 입력: "질문 없이 바로 생성만 하고 싶어요. --quick 플래그를 쓰면 되나요?"
   - 예상 행동: --quick 플래그 지원 명시 → 모든 기본값으로 즉시 생성 시작
   - 근거: Phase 2는 사용자 의도 수집이지 필수가 아님 → --quick 프리셋은 필요한 선택지

4. **배치 생성(Phase 6) 중 일부 이미지는 안전 필터에 걸리는 경우**
   - 입력: "50개 이미지 배치를 만들었는데 3개가 '안전 필터 위반'이에요. 다시 생성할까요?"
   - 예상 행동: 실패한 3개 이미지의 프롬프트 내용 분석 → "부적절한 키워드 제거" 또는 "프로젝트 설명 수정" 제안 → 수정 후 재생성
   - 근거: 안전 필터는 정책이므로 우회 불가 → 프롬프트 자체를 온건하게 재작성이 유일한 해결책

5. **생성된 이미지를 sketch-to-code 파이프라인(Phase 5)으로 넘길 때 포맷/해상도 미스매치**
   - 입력: "생성된 PNG 이미지를 Claude Code에 전달했는데 포맷 오류가 나요."
   - 예상 행동: output/ 폴더 구조 확인 → 이미지 경로/포맷(PNG vs JPEG) 명시 → sketch-to-code 파이프라인 입력 형식 정확화
   - 근거: Phase 5 파이프라인 연결은 선택사항이지만, 구현하면 파일 인터페이스 정의 필수

---

