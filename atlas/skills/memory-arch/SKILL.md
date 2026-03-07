---
name: memory-arch
description: "Design an agent memory system — working memory, episodic memory, semantic memory, and procedural memory. Use when building agents that need to remember context across sessions, learn from interactions, or maintain persistent knowledge. Covers storage strategy, retrieval patterns, and context management."
argument-hint: "[agent requiring persistence]"
---

# Memory Architecture

> 에이전트 메모리 시스템 설계 — 단기 컨텍스트, 장기 저장, 검색 전략

## 개념

에이전트의 지능은 메모리에서 나온다. 단일 실행의 컨텍스트 윈도우를 넘어서, 실행 간 학습과 기억을 유지하는 메모리 아키텍처가 에이전트의 진화를 가능하게 한다.

## Instructions

You are designing a **memory architecture** for: **$ARGUMENTS**

### Step 1 — Memory Type Classification

| Memory Type | Scope | Storage | Example |
|------------|-------|---------|---------|
| **Working Memory** | Single execution | Context window | Current task instructions, user input |
| **Episodic Memory** | Across executions | File/DB | "Last time user X asked about Y, they preferred Z format" |
| **Semantic Memory** | Permanent knowledge | Embeddings/DB | Domain knowledge, best practices, TK entries |
| **Procedural Memory** | How-to knowledge | Instructions/Skills | Workflow patterns, prompt templates |

### Step 2 — What to Remember

For each agent interaction, decide:
```
Always Store:
- User preferences and corrections
- Successful output patterns
- Error cases and resolutions
- Key decisions and reasoning

Never Store:
- Sensitive personal data (unless explicitly needed)
- Temporary calculation artifacts
- Redundant information already in semantic memory
```

### Step 3 — Storage Architecture

Choose the storage layer:

| Approach | Best For | Complexity | Cost |
|----------|----------|------------|------|
| **File-based** (Markdown) | Simple agents, personal use | Low | Free |
| **Vector DB** (Pinecone, Chroma) | Semantic search over large corpus | Medium | $$ |
| **Structured DB** (PostgreSQL) | Relational data, complex queries | Medium | $ |
| **Hybrid** (File + Vector) | Best retrieval + human-readable | High | $$ |

### Step 4 — Retrieval Strategy

Design how the agent finds relevant memories:

```
Retrieval Pipeline:
1. Extract query from current context
2. Search relevant memory stores:
   - Recency: recent interactions first
   - Relevance: semantic similarity
   - Importance: priority-tagged memories
3. Rank and select top-K memories
4. Inject into context window (within budget)
```

### Step 5 — Memory Budget

Allocate context window for memory:
```
Total Context Window: [tokens]
├── System Prompt: [tokens] (fixed)
├── Memory Injection: [tokens] (variable)
│   ├── User preferences: [tokens]
│   ├── Relevant past interactions: [tokens]
│   └── Domain knowledge: [tokens]
├── Current Input: [tokens] (variable)
└── Output Reserve: [tokens] (fixed)
```

**Rule**: Memory injection should not exceed 30% of available context

### Step 6 — Memory Lifecycle

Define how memories age:
```
New Memory → Active (immediate access)
  → after 30 days unused → Archive (lower priority retrieval)
  → after 90 days unused → Cold Storage (manual retrieval only)
  → contradicted by newer info → Deprecated (flagged, not deleted)
```

### Output

Present the memory architecture:
```
┌─────────────────────────────────────┐
│ Agent: [name]                        │
├──────────┬──────────────────────────┤
│ Working  │ Context window management │
│ Episodic │ [storage choice]          │
│ Semantic │ [storage choice]          │
│ Procedural│ Skills/Instructions      │
├──────────┴──────────────────────────┤
│ Retrieval: [strategy]                │
│ Budget: [X tokens for memory]        │
│ Lifecycle: [aging policy]            │
└─────────────────────────────────────┘
```

---

## Further Reading
- LangChain Memory Documentation — Memory pattern implementations
- Letta (formerly MemGPT) — Long-term memory architecture for agents
