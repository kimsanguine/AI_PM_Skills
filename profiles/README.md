# profiles/ — 운영자 개인 인스턴스 격리

> hplan 스킬은 **범용 패턴**이고, profile은 **개인 운영 데이터**다.
> 두 레이어를 분리해 hplan은 공개·재사용 가능, profile은 개인·gitignored.

## 디렉토리 구조

```
profiles/
├── README.md           # 이 파일
├── _template/          # 새 profile을 만들 때 복사 시작점
│   ├── agent-fleet.yaml
│   ├── scorecard-weights.yaml
│   ├── pptx-engines.yaml
│   └── ralph-loop.yaml
└── your-name/           # 운영자 본인 인스턴스 (gitignore 권장)
    └── ...
```

## 사용 패턴

1. `_template/`를 복사해 자신의 이름으로 폴더 생성 (`profiles/<your-name>/`)
2. 각 yaml을 본인 운영 데이터로 채움
3. `.gitignore`에 `profiles/<your-name>/` 추가 (또는 글로벌 `profiles/*` + `!profiles/_template`)
4. hplan 스킬은 yaml 경로를 인자로 받아 개인 데이터로 동작 가능

## 왜 분리하는가

| 레이어 | 예시 | 가시성 |
|---|---|---|
| **hplan skill (공개)** | `operate/scorecard-5axis` — 5축 가중치 계산 로직 | 공개·재사용 |
| **profile (개인)** | `your-name/scorecard-weights.yaml` — Cost 35 / Reliability 25 ... | 개인·gitignored |

이 분리로 hplan은 외부 사용자에게 "노이즈 없는 범용 툴킷"으로 보이고,
운영자 본인은 자기 컨텍스트를 yaml 한 줄 변경으로 갈아낄 수 있다.
