# Domain Context — agent-gtm

## 1) Domain Scope

Agent Product Go-To-Market Strategy — 에이전트 제품의 시장 진입, 초기 고객 세그먼트 선정, 신뢰 구축 시퀀스를 설계하는 도메인

**적용 범위:**
- 내부 성공 사례를 외부 제품으로 확장하는 단계
- B2B SaaS 또는 엔터프라이즈 에이전트 출시 준비
- 첫 고객 세그먼트(비치헤드) 선정
- 신뢰 구축 로드맵 및 초기 3개월 계획

**제외 범위:**
- B2C 에이전트 (개인 사용자 대상)
- 이미 시장에 있는 제품의 확장 (별도 전략)
- 기술 구현 (instruction-design 스킬)

---

## 2) Primary Users

- **Founder / CEO**: 외부 출시 결정 및 첫 고객 선정
- **Product Manager**: 비치헤드 시장 분석 및 신뢰 전략 설계
- **Sales / GTM Lead**: 초기 고객 온보딩 및 신뢰 구축
- **Customer Success**: Lighthouse 고객 밀착 지원

---

## 3) Required Inputs

- **에이전트 제품명**: 외부 출시할 에이전트
- **내부 성공 사례**: 현재 검증된 고객/용도
- **타겟 가능 세그먼트 2~3개**: 팀이 생각하는 초기 타겟
- **비용 KPI**: 개발/마케팅 리소스 제약

---

## 4) Output Contract

1. **Beachhead Segment** (점수 20/25 이상)
   - 5개 평가 기준별 점수
   - 선정 근거

2. **Trust Building Sequence** (4단계)
   - Shadow Mode (기간, 성공 기준)
   - Co-pilot Mode (기간, 성공 기준)
   - Auto Mode (기간, 성공 기준)
   - Full Delegation

3. **Launch Sequence** (3단계)
   - Lighthouse: 1~3개 고객, 목표, KPI
   - Wedge: 10~30개 고객, 목표, KPI
   - Expand: 100+ 고객, 목표, KPI

4. **첫 90일 구체적 목표**
   - Lighthouse 고객 수
   - 에이전트 정확도
   - 재사용률

5. **Positioning Statement** (1문장)

6. **재검토 조건**
   - Lighthouse 이탈 신호
   - Wedge 진입 기준

---

## 5) Guardrails

- ✓ Beachhead 점수가 20점 이상인가? (5개 기준 × 4점 평균 이상)
- ✓ Trust Sequence 4단계가 각각 기간과 성공 기준을 갖고 있는가?
- ✓ Launch Phase 3단계가 고객 수, 목표, KPI를 명시하고 있는가?
- ✓ 첫 90일 목표가 정량적(정확도 > 80%, NPS > 50)인가?
- ✓ Positioning이 기술이 아닌 비즈니스 가치를 강조하는가?

---

## 6) Working Facts

**에이전트 GTM의 일반적 특성:**

| 항목 | 특징 | 참고 |
|------|------|------|
| **Lighthouse 고객** | 1~3개, 2~4주 | 무료 또는 원가 제공 |
| **신뢰 구축 기간** | 평균 8~12주 | Shadow (2주) + Co-pilot (4주) + Auto (2주) |
| **Wedge Phase** | 10~30개 고객 | 3~6개월 진행 |
| **CAC Payback** | < 6개월 | 성공 기준 |
| **NPS 기준** | Lighthouse > 60, Wedge > 40 | 에이전트 제품 특화 |

---

## 7) Fill-in Checklist

- [ ] Beachhead Segment가 5개 기준에 각각 점수를 받았고, 총 20점 이상인가?
- [ ] Trust Sequence의 4단계가 각각 기간과 성공 기준을 갖고 있는가?
- [ ] Launch Sequence의 3단계(Lighthouse/Wedge/Expand)가 고객 수, 목표, 전략, KPI를 갖고 있는가?
- [ ] 첫 90일 구체적 목표(Lighthouse 고객 수, 정확도 목표, 재사용률)가 정의되었는가?
- [ ] Positioning Statement가 작성되었고, Beachhead/Pain Point/Key Benefit/Differentiator가 명확한가?

---

## 8) 참고 사례: 에이전트 에코시스템 기반 GTM 전략

> 아래는 특정 프로덕션 환경에서의 사례입니다. 조직과 도메인에 따라 다르게 설계할 수 있습니다.

**참고:** 이 사례는 Anthropic Claude 생태계 기반입니다. OpenAI Assistants API, Google Vertex AI Agent Builder, Microsoft AutoGen 등 다른 플랫폼에서도 유사한 접근이 가능합니다.

### Anthropic의 MCP 오픈소스 전략 분석

2024년부터 Anthropic이 추진하는 **MCP (Model Context Protocol) 오픈소스 전략**(시점: 2025년 3월, 예시값)은 에이전트 시장의 주요 추세 중 하나입니다. GTM 관점에서 보면:

#### 전략의 핵심
```
1단계: MCP 표준 공개 (2024년)
   └─ "모든 AI는 동일 인터페이스로 도구 접근 가능"

2단계: 공식 MCP 서버 개발 (2024년 진행 중, 예시값)
   └─ Notion, GitHub, Google Drive, Slack 등 20+개 (참고: 시점에 따라 변동)
   └─ 개발자 부담 감소

3단계: 커뮤니티 MCP 확산 (2025~, 예상)
   └─ 기업들이 자체 MCP 서버 공개
   └─ 에코시스템 자체 성장
```

**Anthropic의 의도:**
> "도구 연결을 표준화하면, 모든 개발자가 Claude를 선택할 수밖에 없다"

---

### 에코시스템 효과: Notion, GitHub, Figma 등 주요 서비스의 MCP 서버 개발

현재 상황 (2025년 3월):

| 서비스 | MCP 서버 상태 | 제공처 | 기능 |
|------|-----------|--------|------|
| **Notion** | ✓ 공식 | Anthropic | 페이지 조회, 생성, 업데이트 |
| **GitHub** | ✓ 공식 | Anthropic | 레포 관리, PR, Issue |
| **Slack** | ✓ 커뮤니티 | Community | 메시지 전송, 채널 관리 |
| **Figma** | ✓ 커뮤니티 | Community | 디자인 조회, 리소스 접근 |
| **Google Drive** | ✓ 공식 (진행 중) | Anthropic | 파일 관리, 검색 |
| **Jira** | ✓ 커뮤니티 | Community | Issue 관리 |
| **Salesforce** | 예정 | TBD | 영업 데이터 접근 |

**의미:**
```
개발자 입장:
- 이전: "Notion 연동 필요? 직접 API 학습 + 구현"
- 이후: "Notion MCP 사용 (3줄 config 설정)"

비용 절감:
- 이전: 10개 도구 = 10개 API 학습 + 10개 인증 처리 + 버그 추적
- 이후: 10개 도구 = 1개 MCP 프로토콜 + 중앙 인증 (OAuth) + 표준 에러 처리
```

---

### 채용시장 변화: "LangChain 도구 연결" → "MCP 엔터프라이즈급 통합" 필수 역량

#### 2023년 채용 공고
```
"AI 에이전트 엔지니어 모집"

필수 스킬:
- LangChain, LlamaIndex 경험
- REST API 연동
- 비정형 도구 통합 경험
```

#### 2025년 채용 공고 (변화)
```
"AI 에이전트 엔지니어 모집"

필수 스킬:
- ✓ LangGraph 또는 LangChain 경험
- ✓ MCP 프로토콜 이해 및 구현 경험
- ✓ 엔터프라이즈 도구 통합 (Notion, GitHub, Jira 등)
- △ REST API (MCP로 추상화되므로 덜 중요)
```

**변화의 의미:**
```
순위 변화:
1위: 도구별 API → MCP 표준 프로토콜 (위상 전환)
2위: 도구별 인증 → 중앙화된 OAuth (표준화)
3위: 에러 처리 - 도구별 → MCP 표준 (일관성)

결과: "MCP를 못 하면 대기업 AI 팀 입사 어려움"
```

**채용 시장의 임금 상향 (예시값, 참고: 지역과 시점에 따라 변동):**
```
2023년 AI 에이전트 엔지니어: $120K~$150K (예시값)
2025년 MCP 경험 있는 엔지니어: $150K~$200K (+ $20K~50K 프리미엄, 예시값)

원인: MCP 표준 도입으로 경험자 부족
```

---

### GTM 관점: 표준화 플랫폼을 선점하면 에코시스템이 자연스럽게 성장

#### 강력한 네트워크 효과 (Network Effects)

```
초기 (2024년 초):
- Anthropic이 MCP 공개
- 개발자들: "뭐 이거?" (관심 낮음)

중간 (2024년 중반):
- Notion, GitHub, Figma MCP 서버 공개
- 기업들: "아, 이걸 써야 하나?" (채택 증가)
  └─ MCP 채택 회사 → 개발 시간 단축
  └─ Claude 더 많이 씀 (경쟁사 LLM 쓸 이유 없음)

후기 (2025~):
- 개발자들: "MCP 경험이 필수네" (시장 표준화)
- 신입 개발자: "MCP 먼저 배운다" (교육 커리큘럼 변화)
- 기업 채용: "MCP 경험자만" (경험자 가격 상승)
  └─ 경험자 부족 → Claude 사용자 더 증가
  └─ Claude 수요 → Anthropic 위상 강화
```

**이것이 "표준화 선점"의 파괴력:**
- USB가 PC 업계를 지배한 이유 = 표준화
- Android가 모바일 시장을 장악한 이유 = 표준화
- MCP가 AI 통합 시장을 장악할 이유 = 표준화

---

### GTM 전략 수립 시 MCP 고려사항

#### 에이전트 제품의 신뢰성과 MCP
```
기업 고객 관점:
"우리는 Notion, GitHub, Jira와 연동하는 에이전트가 필요해"

선택지 A: 직접 구축 (Function Calling)
  - 개발 기간: 3주 (도구별 API 학습, 예시값)
  - 유지보수: 매달 1~2시간 (API 변경 대응, 예시값)
  - 비용: $50K (예시값, 조직별 조정 가능)

선택지 B: MCP 기반 (표준화)
  - 개발 기간: 1주 (MCP 설정만, 예시값)
  - 유지보수: 거의 없음 (공식 MCP 서버 책임)
  - 비용: $15K (예시값, 조직별 조정 가능)

결과: 고객이 B를 선택 → 경쟁사 대비 3배 빠름 → 신뢰도 상승
```

---

### 체크리스트: MCP 에코시스템을 활용한 GTM

- [ ] **현재 에이전트가 지원해야 할 도구는?**
  - 목록 작성 (예: Notion, GitHub, Slack 등)

- [ ] **각 도구의 MCP 서버가 이미 존재하는가?**
  - 존재 → MCP 도입 (개발 시간 단축)
  - 미존재 → 커스텀 MCP 서버 개발 (우리가 선점 기회)

- [ ] **경쟁사가 MCP를 지원하는가?**
  - Yes → MCP 미지원은 차별화 불가
  - No → "MCP 지원" 자체가 차별화 포인트 (Beachhead에 어필)

- [ ] **채용 공고에 MCP 경험자를 찾고 있는가?**
  - Yes → 시장이 이미 MCP 필요성 인식
  - No → MCP 교육 예산 필요

- [ ] **첫 Lighthouse 고객의 도구 스택은?**
  - MCP 서버가 많을수록 → 구현 기간 단축 → Trust Sequence 가속화

- [ ] **Positioning에 MCP 언급이 있는가?**
  - 예: "2주 안에 Notion/GitHub/Slack 통합" (MCP 덕분)
  - 아니면: "3주 필요" (직접 구축)
