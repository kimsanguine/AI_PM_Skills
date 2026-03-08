# Domain Context — gemini-image-flow 스킬

## 1) Domain Scope

**이 스킬이 소유하는 영역:**
- Gemini API 기반 이미지 생성 엔드투엔드 파이프라인 설계
- Phase 0~7 단계별 구현 계획
- 모델 티어(Flash/Pro/Pro-HD) 선택 및 비용 최적화
- 후속 파이프라인(sketch-to-code, image-to-marketing) 연결

**이 스킬이 소유하지 않는 영역:**
- Instruction 설계 (→ `forge/instruction`)
- 프롬프트 최적화 (→ `forge/prompt`)
- 비용 시뮬레이션 (→ `oracle/cost-sim`)

## 2) Primary Users

- **크리에이티브 워크플로우 설계자**: UI/디자인 자동 생성
- **개발자**: 이미지 생성 파이프라인 구현
- **PM**: 후속 파이프라인 연결 계획

## 3) Required Inputs

**필수 입력:**
1. 이미지 생성 목적 (UI/배너/로고/소셜 등)
2. 프로젝트/상황 설명
3. 후속 파이프라인 필요 여부

**선택 입력:**
- API 키 발급 여부
- 모델 선택 (Flash vs Pro)

## 4) Output Contract

**산출물:**
- Phase 0~7 완료 파이프라인 설계
- 프롬프트 템플릿 (기본 + 프로젝트별)
- 모델 티어 전략 (Flash/Pro 비용 비교)
- 후속 파이프라인 정의 (선택사항)
- 테스트 시나리오 (T1~T8)

## 5) Guardrails

**라우팅 규칙:**
- Instruction 설계 필요 → `forge/instruction`
- 프롬프트 최적화 → `forge/prompt`
- 비용 분석 → `oracle/cost-sim`

**품질 기준:**
- Phase 0은 반드시 완료 (API 환경 필수)
- 모델 ID는 구현 시점의 최신 모델 확인 필수
- 프롬프트 템플릿은 재사용성 고려

## 6) Working Facts

**Gemini 이미지 생성 모델:**

| 모델 | 모델 ID | 이미지 생성 | 무료 티어 | 비용 |
|------|---------|:---:|:---:|---:|
| Gemini 3.1 Flash Image | `gemini-3.1-flash-image-preview` | ✅ | ❌ | ~$0.045–0.15 |
| Gemini 2.5 Flash Image | `gemini-2.5-flash-image-preview` | ✅ | 제한적 | ~$0.039 |

**Phase 구조:**

| Phase | 내용 | 시간 | 산출물 |
|-------|------|------|--------|
| 0 | API 준비 | 10분 | 환경변수 설정 |
| 1 | 아키텍처 | 15분 | 파이프라인 다이어그램 |
| 2 | 인텐트 수집 | 20분 | CLI 질문 흐름 |
| 3 | 프롬프트 | 30분 | 템플릿 + 세그먼트 |
| 4 | API 설정 | 20분 | 모델 티어 + 에러 처리 |
| 5 | 후속 파이프라인 | 15분 | sketch-to-code 정의 |
| 6 | 비용 계획 | 15분 | Flash vs Pro 비용 비교 |
| 7 | 테스트 | 30분 | T1~T8 통과 |

**TO BE UPDATED by reviewer:**
- Gemini API 최신 모델 ID (월 단위로 변경)
- Flash vs Pro 비용 추정 (가격 변동)
- 안전 필터 정책 변화

## 7) Fill-in Checklist

- [ ] Phase 0 API 환경 준비 완료했는가?
- [ ] Phase 1 아키텍처 다이어그램 작성했는가?
- [ ] Phase 2 인텐트 수집(CLI 질문) 정의했는가?
- [ ] Phase 3 프롬프트 템플릿 (기본 + 프로젝트별) 완성했는가?
- [ ] Phase 4 모델 티어 전략 수립했는가?
- [ ] Phase 5 후속 파이프라인(선택사항) 정의했는가?
- [ ] Phase 6 비용 추정 (Flash vs Pro) 완료했는가?
- [ ] Phase 7 테스트 시나리오 (T1, T2, T3 최소) 통과했는가?

## 8) 참고 사례: Gemini 이미지 파이프라인 실전 설계

> **면책:** 아래 체크리스트와 기법은 2025~2026년 Gemini API 기준입니다. 모델 ID, 비용, API 동작은 변경될 수 있으므로 구현 시점에 [공식 문서](https://ai.google.dev/gemini-api/docs/models)에서 최신 정보를 확인하세요.

### a) Phase 간 전환 브릿지 체크리스트

**Phase 0 → Phase 1: API 연결 확인 후 아키텍처 설계 진입**
- [ ] `GEMINI_API_KEY` 환경변수 설정 완료
- [ ] 간단한 텍스트 API 호출 테스트 성공 (200 응답)
- [ ] 이미지 생성 API 권한 활성화 확인
- [ ] Rate limit (요청/분) 확인 및 문서화

**Phase 3 → Phase 4: 프롬프트 템플릿 완성도 검증 후 API 호출 진입 조건**
- [ ] 기본 프롬프트 템플릿 3개 이상 작성 (일반용, UI용, 로고용 등)
- [ ] 각 템플릿에 대해 최소 1회 이상 성공 응답 확인
- [ ] 부정 프롬프트(avoid, do not include) 포함 검증
- [ ] 프롬프트 길이 제한(예시값: 1000자) 확인

**Phase 4 → Phase 5: 이미지 품질 기준 통과 후 파이프라인 연결 진입 조건**
- [ ] 생성된 이미지 해상도 확인 (최소 512×512, 목표 1024×1024)
- [ ] 품질 기준: CLIP 스코어(예시값: 0.25 이상, 도메인에 따라 조정) 또는 육안 검증
- [ ] sketch-to-code 전달 시 포맷 검증 (PNG, 투명도 지원)
- [ ] 생성 시간 기준 충족 (예시값: 10초 이내, 도메인에 따라 조정)

**Phase 6 → Phase 7: 비용 예측 대비 실제 비용 비교 후 테스트 진입 조건**
- [ ] 비용 시뮬레이션 완료 (Flash 프로토타입 10회 + Pro 1회 기준)
- [ ] 실제 비용 측정: `(예측 비용 - 실제 비용) / 예측 비용 < 0.15` (허용 오차 15%)
- [ ] 월간 예산 상한 설정 (예시값: 프로젝트별로 결정, 도메인에 따라 조정)
- [ ] 비용 모니터링 대시보드 준비 (선택사항)

### b) 모델 ID 버전 관리 전략

**Gemini API의 모델 ID 변경 이력 및 preview → stable 전환 패턴**

| 날짜 | 모델명 | 모델 ID | 상태 | 비고 |
|------|--------|---------|------|------|
| 2025.08.26 | Gemini 2.5 Flash Image | `gemini-2.5-flash-image-preview` | Preview | 멀티 이미지 블렌딩 지원 |
| 2025.11.20 | Gemini 3 Pro Image | `gemini-3-pro-image-preview` | Preview | 향상된 텍스트 렌더링 |
| 2026.02.26 | Gemini 3.1 Flash Image | `gemini-3.1-flash-image-preview` | Preview | 빠른 처리, 지시 따르기 개선 |

**코드에서 모델 ID를 하드코딩하지 않는 설계**

```python
# ❌ 나쁜 예: 하드코딩
model = "gemini-3.1-flash-image-preview"

# ✅ 좋은 예: Config 기반 + 런타임 검증
CONFIG = {
    "image_generation": {
        "models": {
            "flash": os.getenv("GEMINI_IMAGE_FLASH", "gemini-3.1-flash-image-preview"),
            "pro": os.getenv("GEMINI_IMAGE_PRO", "gemini-3-pro-image-preview")
        }
    }
}

# 런타임 모델 ID 검증
def get_available_models():
    """API에서 현재 사용 가능한 모델 목록 조회"""
    response = genai.list_models()
    return [m.name for m in response if 'image' in m.name]
```

**모델 ID 변경 감지 자동화 (API 호출 시 404 → 최신 모델 자동 조회)**

```python
def call_image_generation_with_fallback(prompt, initial_model):
    """
    모델 ID 변경 감지 및 자동 폴백
    - 초기 모델 호출 시도
    - 404 응답 시 ListModels API로 최신 모델 조회
    - 재시도 (최대 1회)
    """
    try:
        return generate_image(prompt, model=initial_model)
    except NotFound as e:  # 404: model not found
        logger.warning(f"Model {initial_model} not found. Fetching latest...")
        available = get_available_models()
        # 우선순위: Flash > Pro (비용 최소화)
        latest = next((m for m in available
                       if 'flash' in m.lower() and 'image' in m.lower()),
                      available[0] if available else None)
        if latest:
            logger.info(f"Fallback to {latest}")
            return generate_image(prompt, model=latest)
        raise
```

### c) 이미지 생성 프롬프트 최적화 기법

**스타일 제어 키워드 예시**

| 스타일 | 키워드 조합 | 용도 | 품질 기준 |
|--------|----------|------|----------|
| 사진 리얼리즘 | `photorealistic, 8k quality, professional photography, studio lighting` | 제품/초상화 | 세부 표현 |
| 일러스트레이션 | `illustration, vibrant colors, artistic style, cartoon-like` | UI/마케팅 | 일관성 |
| 플랫 디자인 | `flat design, minimalist, geometric shapes, 2D style` | 아이콘/로고 | 단순성 |
| 3D 렌더링 | `3D render, octane render, cinematic lighting, volumetric` | 제품 / 개념 | 깊이감 |

**부정 프롬프트(Negative Prompt) 활용법**

```
기본 프롬프트:
"A modern minimalist logo for a AI startup, flat design,
 geometric shapes, blue and white colors"

부정 프롬프트 추가:
"avoid: text, words, low quality, blurry, deformed,
 watermark, signature, 3D effect, gradient background"
```

**해상도별 프롬프트 최적화 차이**

- **512×512**: 간단한 구성 (주요 요소 3개 이하)
- **1024×1024**: 상세한 배경 포함, 세부 사항 추가 가능
- **2048×2048**: 복잡한 장면, 많은 객체, 풍부한 텍스처 가능

> 팁: 기본 프롬프트는 모든 해상도에서 동일하게 유지하고, 세부 사항은 해상도별로 추가합니다.

### d) 비용 최적화 의사결정 트리

```
프로젝트 시작
├─ 프로토타입 단계 (2~10회 생성)?
│  └─ Flash 사용 (예시값: $0.039/image, 도메인에 따라 조정)
│     └─ 만족하는가?
│        ├─ Yes → Pro로 최종 1~3회만 (예시값: $0.12/image, 도메인에 따라 조정)
│        └─ No  → 프롬프트 조정 후 Flash로 재시도
│
├─ 배치 모드 (대량 생성, 50회 이상)?
│  └─ Batch API 활용 (비용 50% 감소)
│     ├─ 요청 병합 (24시간 내 완료 가능)
│     └─ 요청 중복 제거 (캐시 키 사용: hash(prompt))
│
├─ 실시간 생성 필수?
│  └─ Batch 불가능 → Flash로 직접 호출
│
└─ 월간 예산 상한 설정
   ├─ 작은 프로젝트 (예시값: $100/월, 도메인에 따라 조정)
   ├─ 중간 프로젝트 (예시값: $500/월, 도메인에 따라 조정)
   └─ 대형 프로젝트 (예시값: $5000/월, 도메인에 따라 조정)
      → 비용 모니터링 자동화 (일 단위 Alert)
```

**배치 할인 활용 조건 및 계산**

```python
def calculate_batch_savings(num_requests, use_batch=True):
    """
    Batch API 사용 시 비용 절감 계산
    - Flash: $0.039/image
    - Batch discount: 50%
    """
    cost_per_image = 0.039
    if use_batch:
        cost_per_image *= 0.5  # 50% 할인

    total_cost = num_requests * cost_per_image
    savings_pct = (0.5 if use_batch else 0)

    return {
        "total_requests": num_requests,
        "cost_per_image": cost_per_image,
        "total_cost": total_cost,
        "batch_discount": f"{savings_pct*100:.0f}%"
    }

# 예시: 100개 이미지 생성
result = calculate_batch_savings(100, use_batch=True)
# {'total_requests': 100, 'cost_per_image': 0.0195, 'total_cost': 1.95, 'batch_discount': '50%'}
```

### e) Sketch-to-Code 파이프라인 상세

**이미지 → Claude Code 전달 시 최적 포맷**

| 포맷 | 이점 | 단점 | 추천 상황 |
|------|------|------|----------|
| PNG | 투명도 지원, 무손실 | 파일 크기 큼 | 로고, 아이콘, UI (배경 투명) |
| JPEG | 작은 파일 크기 | 배경 흰색 고정, 손실 | 스크린샷, 와이어프레임 |
| WebP | 최적 압축 | 브라우저 호환 문제 | 프로토타입용 내부 전달 |

**해상도 권장사항:**
- **최소**: 512×512 (빠른 검증)
- **표준**: 1024×1024 (코드 생성 정확도 최고)
- **최대**: 2048×2048 (복잡한 디자인, 생성 시간 증가)

**프롬프트 구성 (Claude Code 전달 기준)**

```
Step 1: 디자인 이미지 업로드
"[이미지 첨부]"

Step 2: 기술 스택 지정
"위 디자인을 React + Tailwind CSS로 변환해주세요.
 - 컴포넌트 구조: Header, Body, Footer
 - 반응형 필수 (mobile 320px 이상)
 - 어두운 모드 지원"

Step 3: 반복 피드백
"Button 색상을 파란색으로 변경해주세요."
"마진/패딩 조정: 왼쪽 여백 20px로"
```

**디자인 충실도 검증: 원본 vs 구현 비교 방법**

```python
def validate_design_fidelity(original_image, implementation_screenshot):
    """
    생성된 이미지와 구현된 코드 비교

    검증 항목:
    1. 색상 일치도 (색상 히스토그램 비교)
    2. 레이아웃 일치도 (객체 위치 오차 < 5%)
    3. 텍스트 요소 (위치, 크기, 폰트 스타일)
    4. 간격 정확도 (패딩, 마진 오차 < 10%)
    """

    # 의사 코드 (실제 구현은 이미지 분석 라이브러리 사용)
    color_match = compare_histograms(original_image, implementation_screenshot)
    layout_match = compare_object_positions(original_image, implementation_screenshot)

    fidelity_score = (color_match * 0.4 + layout_match * 0.6)

    return {
        "fidelity_score": fidelity_score,
        "threshold_met": fidelity_score > 0.8,  # 예시값
        "color_match": color_match,
        "layout_match": layout_match
    }
```

**Sketch-to-Code 파이프라인 워크플로우**

```
1. 스케치 이미지 생성 (gemini-image-flow)
   ├─ 사용자 요구사항 → 프롬프트 변환
   ├─ Gemini API로 이미지 생성
   └─ PNG 형식으로 저장 (1024×1024)

2. Claude Code로 전달
   ├─ 이미지 업로드
   ├─ 기술 스택 지정 (React/Tailwind/Vue 등)
   └─ 초안 코드 생성

3. 반복 개선 (Phase 5 활용)
   ├─ 컬러 조정
   ├─ 레이아웃 미세 조정
   └─ 반응형 테스트

4. 충실도 검증
   ├─ 원본 이미지 vs 구현 스크린샷 비교
   ├─ 색상/레이아웃 일치도 측정
   └─ 기준 미충족 시 → Step 3으로 돌아가기

5. 최종 코드 배포
   ├─ 코드 리뷰
   └─ 프로덕션 배포
```

---

**모델 ID 참고** (구현 시점 기준 최신 모델 확인 필수)
- [Gemini API 공식 모델 페이지](https://ai.google.dev/gemini-api/docs/models)
- [릴리스 노트](https://ai.google.dev/gemini-api/docs/changelog)
- [이미지 생성 가이드](https://ai.google.dev/gemini-api/docs/image-generation)
