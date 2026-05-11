# Troubleshooting — gemini-image-flow 스킬

## 1) Phase 0 API 키 설정 실패 또는 환경변수 없음

**증상:**
- `GEMINI_API_KEY not found` 또는 `401 Unauthorized` 에러
- .env 파일을 생성했는데도 인식 안 됨
- 다른 터미널 세션에서는 API 키가 인식 안 됨

**확인:**
- API 키 발급: aistudio.google.com/apikey에서 실제로 발급했는가?
- 환경변수 등록: `export GEMINI_API_KEY=...` 또는 `.env` 파일에 등록했는가?
- 환경변수 확인: `echo $GEMINI_API_KEY` 명령으로 값이 출력되는가?
- 터미널 세션: 환경변수 설정 후 새 터미널을 열었는가? (기존 세션에는 적용 안 됨)

**조치:**
1. API 키 발급 재확인: https://aistudio.google.com/apikey
2. 환경변수 등록 (선택: .env 파일 vs 쉘 프로필)
   ```bash
   # 방법 1: .env 파일 (프로젝트 루트)
   echo "GEMINI_API_KEY=your_key_here" > .env

   # 방법 2: 쉘 프로필 (영구 등록)
   echo 'export GEMINI_API_KEY=your_key_here' >> ~/.zshrc  # or ~/.bashrc
   source ~/.zshrc
   ```
3. 새 터미널 열고 확인: `echo $GEMINI_API_KEY`
4. 연결 테스트: `curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY" | head -5`
   - 응답이 모델 목록이면 성공

---

## 2) Phase 4 이미지 생성 시 모델 미지원 또는 API 에러

**증상:**
- "This model does not support image generation"
- "404 Not Found" 또는 "400 Bad Request"
- Phase 4 테스트에서만 실패 (Phase 0 연결 테스트는 성공)

**확인:**
- 사용 중인 모델 ID 확인: 반드시 `-image` suffix가 있는가?
  - ❌ `gemini-2.5-flash` (텍스트 전용)
  - ✅ `gemini-2.5-flash-image-preview` (이미지 생성 지원)
- Gemini API 문서에서 현재 지원하는 이미지 모델 확인: https://ai.google.dev/gemini-api/docs/image-generation
- 모델 ID의 정확한 spelling 확인 (오타)

**조치:**
1. 모델 ID 수정: SKILL.md Phase 0-4에서 권장하는 정확한 모델 ID 확인
   ```typescript
   // Phase 4 모델 배열 수정
   const GEMINI_TIERS = {
     flash: {
       modelId: 'gemini-2.5-flash-image-preview',  // 정확한 ID 사용
       resolution: 1024,
       costPerImage: 0.039
     },
     // ...
   }
   ```
2. Phase 0 연결 테스트로 모델 목록 재확인:
   ```bash
   curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY" | grep "image"
   ```
3. API 문서 최신 확인: Gemini 모델은 자주 업데이트됨 → 2-3개월마다 최신 문서 재확인

---

## 3) 안전 필터(Safety Rating) 위반으로 이미지 생성 실패

**증상:**
- `Safety rating blocked this response`
- 프롬프트는 정상인데 특정 키워드만 걸림
- 배치 생성 중 일부 이미지만 필터링됨

**확인:**
- 프롬프트 내용에 부적절한 키워드가 있는가? (폭력, 성인 콘텐츠, 무기 등)
- Gemini의 안전 정책이 다른 플랫폼보다 더 엄격할 수 있음
- 반복된 재시도도 같은 결과일 가능성 높음 (정책 변경 없이)

**조치:**
1. 프롬프트 수정: 부적절한 키워드 제거 또는 순화
   ```
   // Bad
   "A violent scene with weapons and destruction"

   // Good
   "An action movie scene with dramatic lighting"
   ```
2. 프로젝트 설명 변경: 전체 컨텍스트를 더 순화하게 재작성
3. 일일 재시도: 때론 안전 필터는 확률적 → 다음 날 다시 시도하면 통과할 수도 있음
4. 모델 티어 변경 검토: Pro 모델은 다른 안전 정책을 적용할 수 있음 (Phase 4 참조)
5. 최악의 경우: 해당 이미지 포기 → 다른 스타일/설명으로 대체

---

## 4) 배치 생성(Phase 6) 중 API 한도 초과(429 Rate Limit)

**증상:**
- "Too many requests. Please try again later."
- 처음 10-20개는 생성되다가 갑자기 에러 발생
- 일정 시간 후 재시도하면 다시 작동

**확인:**
- Gemini API 요청 한도: 분당/일일 제한이 있는가?
- 현재 모델 티어: Flash는 일반적으로 Pro보다 한도가 낮음
- 배치 크기가 너무 큰가? (50개 한 번에 모두 요청)
- 다른 동시 요청이 있는가?

**조치:**
1. 지수 백오프(exponential backoff) 구현: 실패 시 대기 후 재시도
   ```python
   import time
   import random

   def retry_with_backoff(api_call, max_retries=5):
       for attempt in range(max_retries):
           try:
               return api_call()
           except RateLimitError:
               wait_time = (2 ** attempt) + random.uniform(0, 1)
               print(f"Rate limited. Waiting {wait_time}s...")
               time.sleep(wait_time)
   ```
2. 배치 크기 줄이기: 50개 → 10개씩 5회로 나눔 + 배치 사이 5초 대기
3. 요청 속도 조절: 비동기 요청 대신 순차 요청으로 변경
4. 모델 티어 고려: Flash 한도 부족 → Pro로 전환 검토 (비용 증가)
5. API 대시보드 확인: Google Cloud Console → Gemini API 쿼터 상태 확인

---

## 5) 프롬프트 템플릿(Phase 3)이 제대로 작동하지 않을 때

**증상:**
- "생성된 이미지가 설명과 전혀 다르게 나옵니다."
- "프롬프트 변수가 제대로 치환되지 않음"
- "템플릿이 너무 일반적이어서 결과가 일관성 없음"

**확인:**
- 프롬프트 템플릿의 동적 변수(`{projectType}`, `{description}` 등)가 올바르게 치환되는가?
- 프롬프트의 "역할 설정(role)" 부분이 명확한가?
- 프롬프트에 명확한 스타일/톤 지시(quality guideline)가 있는가?
- 기본값(defaults)이 설정되어 있는가?

**조치:**
1. 프롬프트 템플릿 체크:
   ```typescript
   // Phase 3 프롬프트 구조 재확인
   const basePrompt = `
     You are a world-class UI/UX designer.
     Create a ${projectType} design for: ${description}
     Style: ${style}
     Color: ${colorTheme}
     Platform: ${platform}
   `;
   ```
2. 변수 치환 테스트: 몇 개 샘플로 프롬프트를 직접 읽어보고 문법 확인
3. 프로젝트 유형별 세그먼트(Phase 3-2) 추가: 제네릭한 지시만으로는 부족
   ```typescript
   if (projectType === "website") {
     prompt += "Show the full page layout with header, hero, and content sections.";
   }
   ```
4. 품질 지시 강화: "high detail, professional, no watermarks" 등 구체적 기준 명시
5. 반복 테스트: 샘플 프롬프트 3개로 직접 생성해보고 결과 평가

---

## 6) 후속 파이프라인(Phase 5) sketch-to-code 연결 실패

**증상:**
- "생성된 이미지를 Claude Code로 전달하려고 하는데 포맷 오류가 나요."
- "output/ 폴더 구조가 이상해요."
- "sketch-to-code 스크립트가 최신 이미지를 인식 못 함"

**확인:**
- output/ 폴더에 생성된 이미지가 실제로 있는가?
- 이미지 파일 이름/경로가 예상과 일치하는가?
- Claude Code에 전달할 때 이미지 경로 형식이 올바른가?
- 이미지 포맷(PNG vs JPEG)이 명시되어 있는가?

**조치:**
1. output/ 폴더 구조 확인 및 정규화:
   ```
   output/
   ├── 2026-03-08-sketch-1.png
   ├── 2026-03-08-sketch-2.png
   └── index.json  # 메타데이터 (선택사항)
   ```
2. 최신 이미지 자동 감지 스크립트:
   ```bash
   # 가장 최신 이미지 찾기
   latest_image=$(ls -t output/*.png | head -1)
   echo "Using: $latest_image"
   ```
3. Claude Code 호출 형식 정확화:
   ```bash
   alias sketch-to-code='claude "Design 파일: $(ls -t output/*.png | head -1) 를 React로 구현해줘"'
   ```
4. 이미지 포맷 명시: PNG는 좋은 품질, JPEG는 더 가볍지만 손실 압축
5. Phase 5 파이프라인 문서화: 각 단계별 입출력 형식 명확히 기록

---

