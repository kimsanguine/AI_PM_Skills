# 좋은 예제 — Memory Architecture

## 사용자 요청
"우리 PM 어시스턴트 에이전트가 같은 사용자와 여러 세션에 걸쳐 대화할 때, 지난번 그 사용자의 결정 과정이나 선호도를 기억했으면 좋겠어."

## 승인 이유
- 에이전트가 여러 실행(세션)에서 일관된 행동 필요
- 사용자별 선호도와 과거 상담 내용 기억 필요
- 각 상호작용에서 배우고 개선되어야 함

## 예상 처리
1. 메모리 유형 분류: Working, Episodic, Semantic, Procedural 매핑
2. 저장소 선택: Episodic은 PostgreSQL, Semantic은 Vector DB 추천
3. 검색 전략: 최신 상호작용 우선, 관련성 기반 랭킹
4. 메모리 예산: 컨텍스트 윈도우 대비 30% 이하로 제한
5. 라이프사이클: 새 → 활성 → 아카이브 → 콜드 스토리지 단계 정의

## 처리 결과 예시
```
메모리 아키텍처:
┌──────────────────────────────┐
│ Working: 현재 대화 컨텍스트  │ (100K 토큰, 고정)
│ Episodic: PostgreSQL         │ ("2주 전 회의에서...")
│ Semantic: Vector DB          │ (PM 프레임워크, 최적 사례)
│ Procedural: Markdown 스킬    │ (월말 보고서 작성 프로세스)
└──────────────────────────────┘

검색: 사용자 질문 → Episodic(user_id 필터) → 상위 3개 반환 → 컨텍스트 주입
메모리 예산: 200K 토큰 중 60K (30%) 할당
```

## LangGraph 기반 메모리 패턴 Good Example

### 세션 구조

PM 어시스턴트 에이전트가 동일 사용자와 여러 세션에서 대화하는 시나리오:

```
세션 1 (3일 전)
├─ 사용자: "OKR 프레임워크 소개해줘"
├─ 에이전트: OKR 정의, 예시, 템플릿 제공
├─ 메모리 저장:
│  ├─ Episodic: "사용자가 OKR 처음 배움"
│  └─ Semantic: "OKR 정의, 템플릿" (재사용 가능)
└─ 세션 종료

세션 2 (1일 전)
├─ 사용자: "우리 팀 Q1 OKR 작성 도와줄래?"
├─ [Memory 미들웨어] 자동 검색:
│  ├─ Episodic: "3일 전에 OKR 배웠음" 주입
│  ├─ Semantic: "OKR 템플릿" 주입
│  └─ Procedural: "OKR 작성 가이드" 주입
├─ 에이전트: (메모리 강화된 상태로) "이전에 OKR 배우셨죠.
│            우리 팀에 맞게 커스터마이징해봅시다"
└─ 메모리 저장:
   ├─ Episodic: "사용자 팀 Q1 OKR 초안 작성"
   └─ Semantic: "사용자 팀 특성" (조직 구조, 팀 규모 등)

세션 3 (현재)
├─ 사용자: "어제 작성한 OKR에서 Objective 3번을 수정해야 돼"
├─ [Memory 미들웨어] 자동 검색:
│  ├─ Episodic: Top 3
│  │  1. "어제 OKR 작성" (최신, 가중치 높음)
│  │  2. "3일 전 OKR 배움"
│  │  3. "OKR 피드백 받음"
│  ├─ Semantic: 관련 OKR 템플릿, 모범 사례
│  └─ Procedural: OKR 수정 절차
├─ 에이전트: (어제 작업 메모리 참고 + 현재 요청으로)
│            "어제 작성한 Objective 3번을 업데이트하겠습니다.
│             [상세 수정]"
└─ 메모리 업데이트:
   ├─ Episodic: "OKR Objective 3 수정"
   └─ Semantic: "사용자 선호도" (간단명료한 표현 선호 등)
```

### 메모리 저장소 설정 (config.yaml)

```yaml
memory:
  # Episodic: 과거 상호작용 저장
  episodic:
    backend: "postgresql"
    table: "episodic_memory"
    schema:
      id: str
      thread_id: str
      user_id: str
      content: str
      tags: list[str]  # ["OKR", "session_2", "high_importance"]
      created_at: datetime
      relevance_score: float  # 검색 순위용
      expires_at: datetime  # 12개월 후 자동 아카이브

  # Semantic: 도메인 지식/개념
  semantic:
    backend: "vector_db"  # Pinecone, Weaviate, etc.
    collection: "pm_knowledge"
    embedding_model: "text-embedding-3-small"
    schema:
      id: str
      user_id: str  # 사용자 특화 정보
      content: str
      category: str  # "OKR", "prioritization", "roadmap"
      embedding: list[float]
      updated_at: datetime

  # Procedural: 워크플로우/프로세스
  procedural:
    backend: "file"  # Markdown 스킬로 관리
    path: "skills/procedures/"
    schema:
      id: str
      name: str  # "okr_writing_guide.md"
      version: str
      user_id: str  # 개인화된 프로세스
      updated_at: datetime

  # Working: 현재 스레드 상태
  working:
    backend: "memory"  # ThreadState에만 존재
    max_messages: 50  # 최근 50개 메시지만 보관
```

### Memory Extraction 로직

```python
# 각 턴마다 자동으로 실행
class MemoryExtractionMiddleware:
    def extract_from_interaction(self, thread_state: ThreadState):
        last_user_msg = thread_state.messages[-2]  # 마지막 사용자 메시지
        last_agent_msg = thread_state.messages[-1]  # 마지막 에이전트 응답

        # 1. Episodic 추출 (이 상호작용 기록)
        episodic_entry = {
            "thread_id": thread_state.thread_id,
            "user_id": thread_state.user_id,
            "content": f"User: {last_user_msg}\nAgent: {last_agent_msg}",
            "tags": self.extract_tags(last_user_msg),  # ["OKR", "수정"]
            "importance": self.score_importance(last_agent_msg),  # 0-1
            "expires_at": now + timedelta(days=365)
        }
        episodic_memory.insert(episodic_entry)

        # 2. Semantic 추출 (재사용 가능한 지식)
        if "OKR" in episodic_entry["tags"]:
            semantic_entry = {
                "user_id": thread_state.user_id,
                "content": extract_concepts(last_agent_msg),
                "category": "OKR",
                "embedding": embed(semantic_entry["content"])
            }
            semantic_memory.upsert(semantic_entry)

        # 3. Procedural 업데이트 (필요 시)
        if detected_process_improvement(thread_state):
            update_procedure(thread_state.user_id, ...)
```

### Summarization 자동 활성화

```python
class SummarizationMiddleware:
    def check_trigger(self, thread_state: ThreadState):
        # 조건 1: 토큰 초과
        if token_count(thread_state.messages) > 100000:
            self.summarize(thread_state, "token_limit")

        # 조건 2: 턴 수 초과
        if len(thread_state.messages) > 50:
            self.summarize(thread_state, "interaction_count")

    def summarize(self, thread_state: ThreadState, reason: str):
        # 최근 10턴은 보존, 그 이전은 요약
        recent = thread_state.messages[-10:]
        old = thread_state.messages[:-10]

        summary = llm.invoke(
            model="gpt-3.5-turbo",  # 가벼운 모델
            prompt=f"""다음 대화를 요약하세요:
            {format_messages(old)}

            요약 형식: 핵심 결정, 행동항목, 패턴"""
        )

        # 아카이브 저장
        episodic_memory.insert({
            "content": summary,
            "tags": ["archived_summary"],
            "importance": 0.3  # 낮은 우선도 (최신이 아님)
        })

        # ThreadState 업데이트
        thread_state.messages = recent + [
            Message(role="system", content=f"[Summary]\n{summary}")
        ]
```

### Thread-Isolated 메모리 검색

```python
class MemoryMiddleware:
    def search(self, thread_state: ThreadState, query: str):
        # 모든 검색은 자동으로 현재 스레드 필터 적용
        episodic_results = episodic_memory.search(
            query,
            filters={
                "user_id": thread_state.user_id,  # 자동 필터 1
                "thread_id": thread_state.thread_id,  # 자동 필터 2
                "expires_at": {"$gt": now}  # 만료된 것 제외
            },
            top_k=5,
            sort_by="relevance_score DESC, created_at DESC"  # 최신 우선
        )

        semantic_results = semantic_memory.search(
            query,
            filters={"user_id": thread_state.user_id},  # 사용자 개인화
            top_k=3
        )

        # 3. 프롬프트 주입
        system_prompt = f"""
당신은 PM 어시스턴트입니다. 아래 메모리를 참고하여 응답하세요:

## 최근 상호작용 (Episodic)
{format_results(episodic_results)}

## 도메인 지식 (Semantic)
{format_results(semantic_results)}

## 워크플로우
{load_procedure(thread_state.user_id)}
"""
        return system_prompt
```

### 예상 성과

| 지표 | 목표 | 달성 방법 |
|-----|-----|---------|
| 세션 연속성 | 80% | Episodic 메모리 (최근 3개월) |
| 응답 개인화 | 90% | Semantic 메모리 + 사용자 필터 |
| 토큰 효율 | 30% 할당 | Summarization으로 압축 |
| 메모리 모순 | <2% | 버전 타임스탐프 + 최신 우선 |
| 격리 안전성 | 100% | ThreadState + 자동 필터 |
