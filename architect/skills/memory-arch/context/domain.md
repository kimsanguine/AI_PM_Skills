# 도메인 컨텍스트 — Memory Architecture

## 1) Domain Scope
에이전트가 **세션 간 기억을 유지**하고 **학습**하기 위한 메모리 시스템 설계 영역.
- 포함: Working Memory, Episodic Memory, Semantic Memory, Procedural Memory 구축
- 포함: 저장소 선택, 검색 전략, 컨텍스트 윈도우 관리
- 제외: 개별 세션 내 컨텍스트 관리, 프롬프트 설계, 데이터베이스 인프라 구축

## 2) Primary Users
- **에이전트 설계자**: 메모리 아키텍처 선택
- **PM**: 에이전트가 기억해야 할 정보 정의
- **엔지니어**: 메모리 저장소 및 검색 구현

## 3) Required Inputs
- 에이전트가 기억해야 할 정보 유형:
  - 사용자 선호도/과거 결정
  - 도메인 지식
  - 성공/실패 패턴
  - 워크플로우 프로세스
- 컨텍스트 윈도우 크기
- 검색 속도 요구사항
- 메모리 격리 필요성 (사용자별, 팀별 등)

## 4) Output Contract
- **메모리 계층 설계**:
  - Working: 현재 세션 컨텍스트 관리
  - Episodic: 과거 상호작용 저장소 선택
  - Semantic: 지식 저장소 선택
  - Procedural: 워크플로우 저장소 선택
- **검색 전략**: Recency, Relevance, Importance 우선순위
- **메모리 예산**: 컨텍스트 윈도우 대비 할당 비율
- **라이프사이클**: 메모리 노화 정책 (활성 → 아카이브 → 콜드)

## 5) Guardrails
- 메모리 주입이 컨텍스트 윈도우를 초과하면 안 됨 (30% 이하 권장)
- 사용자 격리 로직 필수 (공유 메모리의 경우)
- 메모리 모순 감지 및 버전 관리 체계 구축
- 민감한 개인정보는 명시적 동의 후 저장

## 6) Working Facts (TO BE UPDATED by reviewer)
- [ ] Vector DB 검색 지연시간: 평균 200-500ms (예시값, 환경에 따라 다름)
- [ ] 메모리 컨텍스트 주입 최적 범위: 20K-60K 토큰 (예시값, 모델마다 다름)
- [ ] 메모리 모순의 실무 발생률: 약 5-10% (예시값, 명시적 버전 관리 필요)
- [ ] Episodic 메모리 활용률: 최신 3개월만 약 40% (예시값, 도메인에 따라 조정)

## 7) Fill-in Checklist

### 메모리 유형 분류
- [ ] Working Memory: 현재 세션 컨텍스트
- [ ] Episodic Memory: 저장소 선택 및 검색 방식
- [ ] Semantic Memory: 저장소 선택 및 인덱싱 전략
- [ ] Procedural Memory: 저장소 선택 및 버전 관리

### 저장소 선택 정당화
- [ ] File-based: 비용, 복잡도, 검색 속도 평가
- [ ] Vector DB: 유사도 검색 필요 여부 확인
- [ ] Structured DB: 관계형 쿼리 필요 여부 확인
- [ ] Hybrid: 여러 저장소 조합 타당성 검토

### 메모리 예산 계산
- [ ] 컨텍스트 윈도우 크기: ____ 토큰
- [ ] 메모리 할당: 30% = ____ 토큰
- [ ] 각 메모리 유형별 할당: Working __%, Episodic __%, Semantic __%, Procedural __%

### 검색 전략 명시
- [ ] Recency: 최신 __개월 우선
- [ ] Relevance: 유사도/키워드 필터링
- [ ] Importance: 태그/우선도 기반 정렬

### 라이프사이클 정의
- [ ] 활성 단계: 새로 생성 후 __일
- [ ] 아카이브: __일 미사용 후
- [ ] 콜드 스토리지: __일 미사용 후
- [ ] 삭제 정책: Deprecated 메모리 처리

### Quality Gate
- [ ] 모든 메모리 유형이 명확한 저장소에 할당되었는가?
- [ ] 저장소 선택이 사용 패턴과 일치하는가?
- [ ] 메모리 예산이 컨텍스트 윈도우를 초과하지 않는가?
- [ ] 사용자 격리 로직이 구현되었는가? (필요한 경우)
- [ ] 메모리 모순 해결 방안이 정의되었는가?

## 8) 참고 사례: LangGraph 기반 메모리 시스템

> 아래는 특정 프로덕션 환경에서의 사례입니다. 조직과 도메인에 따라 다르게 설계할 수 있습니다.

### Memory Extraction → Queue → Prompts 3단계 구조

LangGraph 기반 프로덕션 에이전트의 메모리 시스템은 다음 3단계로 작동합니다:

```
[사용자 상호작용]
    ↓
[Memory Extraction]
  → ThreadState에서 대화 내용 추출
  → 중요도 분류 (High/Medium/Low)
  → 메모리 유형 태그 (Episodic/Semantic/Procedural)
    ↓
[Memory Queue]
  → 추출된 메모리를 큐에 추가
  → 저장소별로 그룹화 (PostgreSQL, Vector DB, File)
  → 배치 처리 (비동기)
    ↓
[Memory Prompts]
  → 리더 에이전트의 시스템 프롬프트에 메모리 주입
  → 검색 결과 Top K (기본값 5개) 선택
  → 컨텍스트 윈도우 내에서 우선순위 정렬
    ↓
[리더 에이전트 실행]
  (메모리 강화된 컨텍스트로 의사결정)
```

**설계 의도**: 메모리 추출과 프롬프트 주입을 분리함으로써 메모리 저장소의 변경이 에이전트 로직에 영향을 주지 않습니다. 또한 queue 방식으로 인해 높은 쓰기 부하를 버틸 수 있습니다.

### Summarization 미들웨어: 토큰 관리 자동화

프로덕션 시스템은 **Summarization 미들웨어**를 통해 긴 대화를 자동으로 압축합니다:

```yaml
# config.yaml의 middleware 설정 (예시값, 도메인에 따라 조정)
summarization:
  enabled: true
  triggers:
    - type: "token_limit"
      threshold: 100000  # 100K 토큰 초과 시 (예시값)
      action: "summarize"
    - type: "interaction_count"
      threshold: 50  # 50턴 이상 대화 (예시값)
      action: "summarize"

  summarizer_model: "gpt-3.5-turbo"  # 가벼운 모델로 요약

  summary_format: "bullet_points"  # 요약 형식

  archive_strategy:
    keep_last_k: 10  # 최근 10턴은 전체 보존 (예시값)
    compress_older: true  # 그 이상은 요약본으로 변환
```

**동작 흐름**:
1. 매 턴마다 현재 대화 토큰 수 계산
2. 임계값 초과 시 자동 trigger
3. 경량 모델 (Haiku/3.5-turbo)로 요약 생성
4. 요약본은 Semantic 메모리에 저장
5. 원본 대화는 아카이브 (콜드 스토리지 이동)

**효과**:
- 초기 100K 토큰 → 요약 후 20K 토큰 (80% 압축)
- 리더 에이전트는 항상 최신 10턴 + 압축 요약으로 작동
- 비용: 추가 요약 API 호출 1회 (~$0.01) vs 대화 비용 절감 ($0.50+)

### 메모리 라이프사이클: 생성부터 만료까지

메모리 관리의 전체 흐름:

**1. 생성 (Creation)**
- 사용자 상호작용에서 새로운 메모리 추출
- 메모리 유형 태그 지정 (Episodic/Semantic/Procedural)
- 중요도 점수 부여

**2. 인덱싱 (Indexing)**
- 저장소별로 메모리 저장 (PostgreSQL, Vector DB, File)
- 벡터 임베딩 생성 (의미 검색용)
- 메타데이터 등록 (생성시간, 태그, 신뢰도)

**3. 검색 (Retrieval)**
- 사용자 쿼리와 유사한 메모리 조회
- Recency/Relevance/Importance 우선순위 적용
- 컨텍스트 윈도우 내에서 Top K 선택

**4. 업데이트 (Update)**
- 모순되는 정보 감지 시 버전 관리
- 메모리 신뢰도 점수 조정 (사용 빈도, 검증 결과)
- 필요시 메모리 병합 또는 분리

**5. 만료/정리 (Expiration/Cleanup)**
- 미사용 메모리: 활성 기간 후 아카이브 (예시: 3개월)
- 오래된 아카이브: 콜드 스토리지 이동 (예시: 12개월)
- Deprecated 메모리: 명시적 삭제 또는 마킹

**라이프사이클 정책 (예시값, 도메인에 따라 조정)**:
```
신규 메모리 생성
    ↓
3개월간 활성 상태 (자주 검색됨)
    ↓
미사용 시 아카이브 (콜드 스토리지)
    ↓
12개월 후 삭제 또는 영구 보존 검토
```

### Thread-Isolated State: 멀티 세션 격리

프로덕션 시스템의 ThreadState 스키마:

```python
class ThreadState:
    """각 대화 스레드는 완전히 격리된 상태를 가짐"""

    # 기본 정보
    thread_id: str  # 고유 ID (user_id + session_timestamp)
    user_id: str  # 사용자 식별자

    # 대화 상태
    messages: list[Message]  # 현재 턴의 메시지만 (메모리는 별도)

    # 메모리 참조
    episodic_memory_ids: list[str]  # "에피소드 1", "에피소드 2", ...
    semantic_memory_ids: list[str]  # "개념 A", "개념 B", ...

    # 실행 상태
    subagent_calls: int  # 서브에이전트 호출 횟수 (제한 검사용)
    middleware_state: dict  # 미들웨어가 저장한 임시 상태

    # 메타데이터
    created_at: datetime
    last_activity: datetime
    metadata: dict  # 사용자 정의 필드
```

**격리 전략**:
- 각 thread는 독립적 메모리 범위 (user_id + thread_id로 필터링)
- 메모리 검색 시 자동으로 현재 thread의 메모리만 반환
- 다른 사용자/세션의 데이터는 접근 불가
- Subagent Limit 미들웨어가 thread별로 호출 횟수 추적

```python
# 메모리 검색 자동 격리
def search_memory(query: str, thread_state: ThreadState):
    results = memory_db.search(
        query,
        filter={
            "user_id": thread_state.user_id,  # 자동 필터
            "thread_id": thread_state.thread_id  # 자동 필터
        },
        top_k=5
    )
    return results
```

### 적용 교훈: 에이전트 메모리 설계의 3가지 계층

| 계층 | 특성 | 저장소 | 라이프사이클 |
|-----|------|-------|----------|
| **Working** | 현재 대화만 | ThreadState (메모리) | 세션 종료 시 삭제 |
| **Episodic** | "지난 3번 대화" | PostgreSQL + Vector | 활성 3개월, 아카이브 12개월 |
| **Semantic** | "우리 회사의 PM 프레임" | Vector DB (임베딩) | 무기한 보존 (업데이트) |
| **Procedural** | "월말 보고서 작성 프로세스" | File (Markdown 스킬) | 버전 관리 |

**프로덕션 환경에서의 실제 배분 (예시값, 도메인에 따라 조정)**:
- Working: 20K 토큰 (고정, 현재 대화)
- Episodic: 30K 토큰 (가변, 최근 상호작용)
- Semantic: 15K 토큰 (가변, 개념/도메인 지식)
- Procedural: 5K 토큰 (가변, 워크플로우)
- **총 70K 토큰** (200K 컨텍스트 윈도우의 35%)

**실무 적용 팁**:

1. **Summarization 언제 활성화할까?**
   - 매일 10회 이상 장시간 대화 → 필수
   - 주 1회, 단편적 질문만 → 불필요
   - 비용 vs 품질 트레이드오프 존재 (프로덕션 환경에서는 기본 활성화)

2. **메모리 모순이 생기면?**
   - Episodic 메모리에 버전 타임스탬프 추가
   - 최신 메모리만 시스템 프롬프트에 주입
   - 이전 버전은 아카이브 (질문받을 때만 검색)

3. **격리 실패하면?**
   - Thread ID 생성 로직 재검토
   - 메모리 검색 필터 자동 추가
   - 멀티테넌트 환경에서는 user_id 필터 필수 (프로덕션 환경에서는 자동)

---

## 선택적 개선사항: 메모리 검색 고도화

메모리 검색 성능을 더욱 개선하려면 여러 전략 중 도메인에 맞는 방식을 선택할 수 있습니다:

**검색 전략 옵션**:
- **벡터 유사도 검색 (Vector Similarity)**: 의미 기반 유사도 (가장 광범위하게 사용)
- **BM25**: 키워드 기반 검색 (정확한 용어 매칭 필요 시)
- **TF-IDF**: 문서 단어 중요도 기반 검색
- **하이브리드 검색 (Hybrid)**: 벡터 + 키워드 결합

아래는 **TF-IDF 기반 개선** 사례입니다.

### 기존 문제: Confidence만으로는 무관한 사실까지 주입된다

기존 메모리 검색 방식:

```
[메모리 저장소 검색]
    ↓
[Top K 선택 기준: confidence score만 사용]
    예) confidence > 0.8인 모든 메모리
    ↓
[문제 발생]
    사용자: "React 성능 최적화 관련해서 물어볼 거야"
    검색된 메모리:
    - Fact 1: "React hook 사용법" (confidence: 0.85)
    - Fact 2: "우리 팀의 저녁 회의 시간" (confidence: 0.80)
    - Fact 3: "Python Django 설정" (confidence: 0.79)

    → 프롬프트에 주입되는 메모리:
      "React hook, 저녁 회의, Django 설정..."

    결과: "왜 Django 얘기가 나와?"
```

**근본 원인:** Confidence는 메모리의 "신뢰도"이지, "현재 질문과의 관련성"이 아님.

---

### 해결책: TF-IDF + Cosine Similarity 기반 혼합 점수

#### 개념
- **TF-IDF (Term Frequency-Inverse Document Frequency)**
  - 문서(메모리)에서 특정 단어가 얼마나 중요한가를 측정
  - 자주 나오는 단어 (예: "the") 는 낮은 가중치
  - 드물지만 의미 있는 단어는 높은 가중치

- **Cosine Similarity**
  - 사용자 질문과 메모리 사이의 "각도" 유사도 측정
  - 0 ~ 1 사이의 값 (1이 완벽 일치)

#### 수식
```
Final Score = (Similarity × 0.6) + (Confidence × 0.4)

예시:
Fact A (React 성능 최적화):
  - Similarity: 0.85 (질문과 관련도 높음)
  - Confidence: 0.75 (신뢰도 중간)
  - Final Score: 0.85 × 0.6 + 0.75 × 0.4 = 0.51 + 0.30 = 0.81

Fact B (Django 설정):
  - Similarity: 0.20 (질문과 관련도 낮음)
  - Confidence: 0.90 (신뢰도 높음)
  - Final Score: 0.20 × 0.6 + 0.90 × 0.4 = 0.12 + 0.36 = 0.48

결과: Fact A (0.81) > Fact B (0.48) → Fact A만 주입됨
```

**가중치 설명:**
- Similarity 60%: "질문과의 관련성"을 더 중요하게 봄
- Confidence 40%: "신뢰도"도 고려하되, 관련성이 없으면 의미 없음

#### 구현 (프로덕션 패턴)
```python
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def search_memory_with_tf_idf(
    user_query: str,
    memory_facts: list[dict],  # [{"text": "...", "confidence": 0.8}, ...]
    top_k: int = 5,
    similarity_weight: float = 0.6,
    confidence_weight: float = 0.4
) -> list[dict]:
    """TF-IDF + 신뢰도 혼합 점수로 메모리 검색"""

    # 1단계: TF-IDF 벡터화
    vectorizer = TfidfVectorizer(max_features=100)
    all_texts = [f["text"] for f in memory_facts] + [user_query]
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # 2단계: 유사도 계산 (마지막 행이 user_query)
    query_vector = tfidf_matrix[-1]
    fact_vectors = tfidf_matrix[:-1]
    similarities = cosine_similarity(query_vector, fact_vectors).flatten()

    # 3단계: 최종 점수 계산
    final_scores = []
    for i, fact in enumerate(memory_facts):
        similarity = similarities[i]
        confidence = fact.get("confidence", 0.5)

        final_score = (similarity * similarity_weight +
                      confidence * confidence_weight)

        final_scores.append({
            "fact": fact,
            "similarity": similarity,
            "confidence": confidence,
            "final_score": final_score
        })

    # 4단계: Top K 선택 (final_score 기준)
    ranked = sorted(final_scores, key=lambda x: x["final_score"], reverse=True)
    return ranked[:top_k]
```

**실무 적용 효과:**
```
이전 (Confidence만):
- 검색: "React 성능" → 10개 메모리 중 8개 반환 (많음)
- 프롬프트 오염: 무관한 메모리도 섞임
- 토큰 낭비: 불필요한 메모리에 토큰 사용

이후 (TF-IDF + Confidence):
- 검색: "React 성능" → 10개 중 3개만 반환 (정확함)
- 프롬프트 정제: 관련 있는 메모리만 주입
- 토큰 효율: 같은 정보를 적은 토큰으로 전달
```

---

### 정확한 토큰 카운팅: Tiktoken 도입

#### 기존 문제
```
대략적 계산: max_chars = max_tokens × 4
예) max_tokens = 100K
    → max_chars = 400K (부정확)

실제 상황:
- 한글: 자음/모음이 1토큰? 전체 글자가 1토큰?
- 마크다운: "#" 기호도 토큰 계산?
- 코드: 들여쓰기는?

결과: 메모리를 충분히 주입했다고 생각했는데
      실제로는 토큰 초과 → 컨텍스트 윈도우 error
```

#### Tiktoken을 이용한 정확한 카운팅
```python
import tiktoken

# encoding 선택 (cl100k_base는 gpt-3.5, gpt-4 등 대부분의 OpenAI 모델)
encoding = tiktoken.get_encoding("cl100k_base")

# Anthropic Claude 모델용
encoding = tiktoken.encoding_for_model("claude-3-sonnet-20240229")

# 정확한 토큰 카운트
text = "사용자의 질문과 메모리를 합치면 몇 토큰일까?"
token_count = len(encoding.encode(text))
print(f"정확한 토큰 수: {token_count}")  # 예: 27 tokens
```

**프로덕션 환경에서 적용한 방식:**
```python
class MemoryBudgetManager:
    def __init__(self, max_tokens: int = 200000, memory_allocation: float = 0.35):
        self.encoding = tiktoken.get_encoding("cl100k_base")
        self.max_tokens = max_tokens
        self.memory_budget = int(max_tokens * memory_allocation)  # 70K tokens (예시값)

    def add_memory(self, memory_text: str) -> bool:
        """메모리를 추가할 때마다 정확한 토큰 계산"""
        tokens_needed = len(self.encoding.encode(memory_text))

        if tokens_needed <= self.remaining_budget:
            self.remaining_budget -= tokens_needed
            return True
        else:
            # 예: "메모리 추가 불가 (남은 예산: 5K, 필요: 8K)"
            return False

    def get_remaining_budget(self) -> int:
        return self.remaining_budget
```

**효과:**
```
이전 (근사값):
- 메모리 예산 설정: max_chars = 400K (부정확)
- 결과: 간헐적으로 "token limit exceeded" 에러

이후 (정확한 tiktoken):
- 메모리 예산 설정: memory_budget = 70K (정확)
- 결과: 항상 안정적 (에러 0)
- 보너스: 메모리 추가 전에 "이건 들어갈까?" 미리 판단
```

---

### 적용 교훈: "메모리 아키텍처에서 'Relevance > Confidence' 원칙"

#### 원칙의 의미
```
순위 1위: Relevance (관련성)
  - "이 메모리가 지금 질문과 얼마나 관련 있는가?"
  - 가중치: 60%
  - 이유: 무관한 메모리는 신뢰도가 높아도 방해만 됨

순위 2위: Confidence (신뢰도)
  - "이 메모리가 얼마나 신뢰할 수 있는가?"
  - 가중치: 40%
  - 이유: 관련 있지만 신뢰도 낮으면 프롬프트에서 주의 표시
```

#### 실무 판단 기준
| 상황 | 메모리 주입? | 이유 |
|-----|-----------|------|
| Relevance 높음 + Confidence 높음 | ✓ 필수 주입 | 완벽한 메모리 |
| Relevance 높음 + Confidence 낮음 | △ 주의 표시 후 주입 | "이 정보는 확실하지 않습니다" 표기 |
| Relevance 낮음 + Confidence 높음 | ✗ 제외 | 무관하면 높은 신뢰도도 쓸모 없음 |
| Relevance 낮음 + Confidence 낮음 | ✗ 제외 | 당연히 제외 |

---

### 체크리스트: 메모리 개선사항 적용 확인

- [ ] **현재 메모리 검색이 confidence 기반인가?**
  - Yes → TF-IDF 혼합 점수 도입 검토

- [ ] **토큰 카운팅이 근사값(max_chars × 4)인가?**
  - Yes → tiktoken 도입으로 정확도 향상

- [ ] **메모리 주입 후 프롬프트에 무관한 정보가 섞여 있는가?**
  - Yes → TF-IDF 가중치 조정 (similarity_weight 증가)

- [ ] **간헐적으로 "token limit exceeded" 에러가 나는가?**
  - Yes → tiktoken으로 정확한 예산 관리 필수

- [ ] **메모리 검색 결과의 Relevance 점수를 추적하는가?**
  - No → TF-IDF 도입 시 자동 추적됨

- [ ] **메모리 추가 전에 "예산이 충분할까?" 판단하는가?**
  - No → MemoryBudgetManager로 자동화 가능
