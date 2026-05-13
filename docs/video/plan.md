# hplan Intro Video — Remotion Production Plan

> 70-second README intro video built with Remotion.dev
> Target: 한국 1인 메이커 / PM / 솔로 창업자 (primary), global GitHub visitor (secondary)
> Status: Pre-production · Locked
> Last updated: 2026-05-11

## 1. Locked decisions

| Item | Choice |
|---|---|
| Language | 한국어 narration + 영어 자막 1줄 (bilingual on-screen) |
| Duration | 70 seconds |
| Audio | **Gemini TTS** (`gemini-2.5-flash-preview-tts`, Korean) + ambient BGM |
| Style | Catppuccin Mocha dark, monospace, terminal-driven |
| Renders | 1920×1080 (16:9, README primary) + 1080×1080 (social) + 1080×1920 (Shorts) |

## 2. 6-scene Storyboard

```
0s ────── 6s ────── 20s ─── 28s ── 36s ── 46s ── 55s ─── 63s ── 70s
  Hook       Problem    Sol.   Demo1  Demo2  Demo3  Cycle    CTA
```

| Scene | Time | Length | Purpose |
|---|---|---|---|
| 1. Hook | 0–6s | 6s | 통증 자극 — "Cursor로 만든 SaaS, 6개월 뒤" |
| 2. Problem | 6–20s | 14s | 4가지 PM 능력 부재 → "코딩이 아니라 시장조사·문제정의" |
| 3. Solution | 20–28s | 8s | hplan = Harness Planning 정의 |
| 4a. Demo Evidence | 28–36s | 8s | exclusions COLLISION → hold |
| 4b. Demo COGS | 36–46s | 10s | p50/p90 마진 → RED |
| 4c. Demo Handoff | 46–55s | 9s | 4 ecosystem export |
| 5. Lifecycle | 55–63s | 8s | 6 plugin 라이프사이클 reveal |
| 6. CTA | 63–70s | 7s | install command + URL |

## 3. Korean narration script

### Scene 1 — Hook (0–6s)

```
[1.5s 무음 — black screen]
"Claude Code로 만든 SaaS." [2s]
(0.5s pause)
"6개월 뒤, 안 팔립니다." [2s]
```

**On-screen 자막**: "Built it with Claude Code. 6 months later — no buyers."

### Scene 2 — Problem (6–20s)

```
"AI 도구는 빠르게 만들어줍니다." [2.5s]
"그런데, 정말 만들어야 할지는 누구도 묻지 않습니다." [3.5s]
(0.5s pause)
"무엇을, 왜, 누가, 어떻게." [2.5s]
"이 네 가지가 비어있는 채로 코드를 씁니다." [3s]
(1s pause)
"문제는 코딩이 아닙니다. 시장조사와 문제정의입니다." [2s]
```

**On-screen 자막 (영어)**: "The bottleneck isn't code. It's market research + problem definition."

### Scene 3 — Solution intro (20–28s)

```
"hplan. Harness Planning." [2s]
"AI 코딩 도구의 거친 동력에 방향을 부여하는," [3s]
"사전 계획입니다." [1.5s]
(0.5s pause for authority line on screen)
```

**On-screen authority line**: "LINE Wallet 1.8억 · 카카오·네이버 · 삼성카드·CJ·이스트소프트 PM이 만들었습니다"

**영어 자막**: "Direction for the raw power of AI coding tools."

### Scene 4a — Demo Evidence Gate (28–36s)

```
"PRD 쓰기 전에," [1.5s]
"hplan은 이미 점유된 영역인지 자동으로 확인합니다." [3.5s]
(1s pause — terminal 결과 표시)
"결정: hold." [1s]
```

**Terminal animation**:
```
❯ /hplan-evidence "AI 마케팅 카피 도구"
   exclusions check ... COLLISION (overlap 0.42)
   ↳ "기존 incumbent가 이미 점유"
   ↳ reopen_trigger: UNMET
→ 결정: hold ✋
```

### Scene 4b — Demo COGS Sentinel (36–46s)

```
"가격을 정하기 전에," [1.5s]
"p50, p90 마진을 실제 숫자로 계산합니다." [3s]
(1.5s pause — 숫자 reveal)
"무료 사용자 abuse까지 포함하면 음수." [2s]
(1s pause)
"이 자리에서, 멈춥니다." [1.5s]
```

**Terminal animation**:
```
❯ /hplan-cogs --model sonnet --tokens 8000 --calls 120 --arpu 19
   per-call cost p50: $0.054
   monthly COGS p50: $6.63       margin 64%
   monthly COGS p90: $13.90      margin 25%  ⚠
   with free-user abuse:                    -1961%  ✗
→ 결정: RED 🚫
```

### Scene 4c — Demo Multi-target Handoff (46–55s)

```
"게이트를 통과한 brief는," [1.5s]
"Spec-Kit, Kiro, GStack, Claude Code." [3s]
(0.5s)
"어떤 코딩 도구든, 한 번에 export됩니다." [2.5s]
```

**Terminal animation**:
```
❯ /hplan-handoff brief.json --target all
✓ specs/001-product/{spec,plan,tasks}.md   → Spec-Kit
✓ .kiro/specs/product/                       → Kiro
✓ office-hours-brief.md                      → GStack
✓ AGENTS.md + CLAUDE.md                      → Claude Code
```

### Scene 5 — Lifecycle (55–63s)

```
"여섯 플러그인. 마흔세 개 스킬." [2s]
"PM 표준 라이프사이클 전체를 덮습니다." [3s]
(1s pause)
"hplan, discover, architect, deliver, measure, learn." [2s]
```

**On-screen**: 7 plugin 박스 sequential animation with arrows. Big stat: "**7 plugins · 50 skills · 18 commands**"

### Scene 6 — CTA (63–70s)

```
(1s pause — install command 타이핑)
"30분 안에, 6개월을 막을 수 있습니다." [2.5s]
(0.5s pause)
"hplan." [0.5s]
"GitHub에서 검색하세요." [2s]
```

**On-screen**:
```
❯ /plugin marketplace add kimsanguine/hplan
```
URL: `github.com/kimsanguine/hplan`
Tagline: "⭐ Star to remember when you need it"

## 4. Narration statistics

| Metric | Value |
|---|---|
| Total video length | 70s |
| Actual narration time | ~57s (81%) |
| Silence / pause | ~13s (19%) |
| Korean characters total | ~318 |
| Speech rate | ~335 char/min (slightly upbeat) |
| TTS provider | **Gemini API** (`gemini-2.5-flash-preview-tts`) |
| Voice | `Charon` (deep, authoritative) — *primary candidate, A/B with `Kore` and `Aoede`* |
| Style prompt | "차분하고 권위감 있는 톤으로, 1.0배 속도, 핵심 단어는 살짝 강조해서 천천히" |

## 5. Visual theme — Catppuccin Mocha

```typescript
// src/theme.ts
export const theme = {
  bg: '#1e1e2e',         // base background
  titleBar: '#313244',   // terminal title bar
  text: '#cdd6f4',       // primary text
  dim: '#a6adc8',        // secondary text
  veryDim: '#6c7086',    // tertiary text
  prompt: '#89b4fa',     // ❯ blue
  skillTag: '#cba6f7',   // skill names purple
  arrow: '#f9e2af',      // → yellow
  ok: '#a6e3a1',         // ✓ green
  warn: '#f9e2af',       // ⚠ yellow
  bad: '#f38ba8',        // ✗ red
  dotRed: '#f38ba8',
  dotYellow: '#f9e2af',
  dotGreen: '#a6e3a1',
};

export const fonts = {
  mono: "'SF Mono', 'JetBrains Mono', 'Fira Code', monospace",
  hookSize: 60,
  bodySize: 24,
  captionSize: 16,
};
```

## 6. Remotion project structure

```
hplan-intro-video/
├── package.json                     # remotion + @remotion/transitions + react
├── remotion.config.ts
├── src/
│   ├── Root.tsx                     # 3 Compositions (16:9, 1:1, 9:16)
│   ├── compositions/
│   │   ├── HplanIntro16x9.tsx       # main 1920×1080
│   │   ├── HplanIntro1x1.tsx        # 1080×1080 social
│   │   └── HplanIntro9x16.tsx       # 1080×1920 Shorts
│   ├── scenes/
│   │   ├── 01-Hook.tsx              # 0–6s (180 frames @ 30fps)
│   │   ├── 02-Problem.tsx           # 6–20s (420 frames)
│   │   ├── 03-Solution.tsx          # 20–28s (240 frames)
│   │   ├── 04a-DemoEvidence.tsx     # 28–36s (240 frames)
│   │   ├── 04b-DemoCogs.tsx         # 36–46s (300 frames)
│   │   ├── 04c-DemoHandoff.tsx      # 46–55s (270 frames)
│   │   ├── 05-Lifecycle.tsx         # 55–63s (240 frames)
│   │   └── 06-CTA.tsx               # 63–70s (210 frames)
│   ├── components/
│   │   ├── Terminal.tsx             # title bar + 3 dots
│   │   ├── TerminalLine.tsx         # prompt + cmd + output
│   │   ├── TypewriterText.tsx       # 타이핑 effect via useCurrentFrame
│   │   ├── PluginBox.tsx            # lifecycle box (6 colors)
│   │   ├── BigStat.tsx              # 큰 숫자 카운트업
│   │   ├── BlinkingCursor.tsx
│   │   └── BilingualCaption.tsx     # 한국어 + 영어 자막
│   ├── data/
│   │   ├── lifecycle.ts             # 6 plugin metadata
│   │   ├── demo-evidence.ts         # demo 1 script lines
│   │   ├── demo-cogs.ts             # demo 2 script lines
│   │   └── demo-handoff.ts          # demo 3 script lines
│   ├── theme.ts                     # Catppuccin palette
│   └── audio.ts                     # narration segment mapping
├── public/
│   └── audio/
│       ├── narration/
│       │   ├── 01-hook.mp3          # 4s
│       │   ├── 02-problem.mp3       # 13.5s
│       │   ├── 03-solution.mp3      # 6.5s
│       │   ├── 04a-evidence.mp3     # 6s
│       │   ├── 04b-cogs.mp3         # 8s
│       │   ├── 04c-handoff.mp3      # 7s
│       │   ├── 05-lifecycle.mp3     # 7s
│       │   └── 06-cta.mp3           # 5s
│       └── bgm.mp3                  # 70s ambient, -18dB
└── out/
    ├── intro-16x9.mp4
    ├── intro-1x1.mp4
    ├── intro-9x16.mp4
    └── intro.gif (optional fallback)
```

## 7. TTS production workflow — Gemini API

Programmatic narration via Gemini TTS — same `GEMINI_API_KEY` 환경변수 재활용 (사용자가 다른 hplan 프로젝트에서 이미 보유).

### 7.1 Why Gemini TTS

| 강점 | 설명 |
|---|---|
| **자연어 style 제어** | 보이스 톤을 prompt로 지시 가능 ("차분하고 권위감 있게, 핵심 단어는 강조") — Naver Clova 같은 fixed-voice GUI보다 정교 |
| **30+ prebuilt voices** | Charon (deep authoritative), Kore (clear professional), Aoede (warm), Puck (upbeat) 등 — A/B 테스트 쉬움 |
| **한국어 native 지원** | gemini-2.5-flash/pro-preview-tts 모두 한국어 자연스러움 |
| **Programmatic** | 8개 scene을 한 Python script로 일괄 생성 + iterate. 톤·voice 바꿔서 재생성도 수초 |
| **이미 보유한 API key** | hplan/.env.example에 GEMINI_API_KEY 이미 정의 — 추가 결제 없이 진행 |

### 7.2 생성 script

`scripts/generate_narration.py` 를 만들어 8개 scene을 일괄 생성:

```python
#!/usr/bin/env python3
"""Generate 8 narration audio clips for hplan intro video via Gemini TTS."""
import os
import wave
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

SCENES = {
    "01-hook": "Claude Code로 만든 SaaS. 6개월 뒤, 안 팔립니다.",
    "02-problem": (
        "AI 도구는 빠르게 만들어줍니다. "
        "그런데, 정말 만들어야 할지는 누구도 묻지 않습니다. "
        "무엇을, 왜, 누가, 어떻게. "
        "이 네 가지가 비어있는 채로 코드를 씁니다. "
        "문제는 코딩이 아닙니다. 시장조사와 문제정의입니다."
    ),
    "03-solution": (
        "hplan. Harness Planning. "
        "AI 코딩 도구의 거친 동력에 방향을 부여하는, 사전 계획입니다."
    ),
    "04a-evidence": (
        "PRD 쓰기 전에, hplan은 이미 점유된 영역인지 자동으로 확인합니다. "
        "결정: hold."
    ),
    "04b-cogs": (
        "가격을 정하기 전에, p50, p90 마진을 실제 숫자로 계산합니다. "
        "무료 사용자 abuse까지 포함하면 음수. "
        "이 자리에서, 멈춥니다."
    ),
    "04c-handoff": (
        "게이트를 통과한 brief는, "
        "Spec-Kit, Kiro, GStack, Claude Code. "
        "어떤 코딩 도구든, 한 번에 export됩니다."
    ),
    "05-lifecycle": (
        "여섯 플러그인. 마흔세 개 스킬. "
        "PM 표준 라이프사이클 전체를 덮습니다. "
        "hplan, discover, architect, deliver, measure, learn."
    ),
    "06-cta": (
        "30분 안에, 6개월을 막을 수 있습니다. "
        "hplan. GitHub에서 검색하세요."
    ),
}

STYLE_INSTRUCTION = (
    "Read the following in Korean with a calm, authoritative, lecturer-like tone. "
    "Speak at a 1.0x natural pace. Emphasize key terms slightly but never shout. "
    "Pause briefly at sentence breaks. Sound like a senior PM with 20 years experience."
)

VOICE = "Charon"   # deep authoritative; A/B with "Kore" or "Aoede"

out_dir = Path("public/audio/narration")
out_dir.mkdir(parents=True, exist_ok=True)

for slug, text in SCENES.items():
    print(f"Generating {slug}...")
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=f"{STYLE_INSTRUCTION}\n\n{text}",
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=VOICE)
                )
            ),
        ),
    )
    # Gemini TTS returns 24kHz mono PCM as base64
    audio_data = response.candidates[0].content.parts[0].inline_data.data
    wav_path = out_dir / f"{slug}.wav"
    with wave.open(str(wav_path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(audio_data)
    print(f"  → {wav_path}")

print("\nDone. Next: convert wav → mp3 with ffmpeg for smaller file size.")
print("  for f in public/audio/narration/*.wav; do ffmpeg -i \"$f\" \"${f%.wav}.mp3\"; done")
```

### 7.3 Voice A/B 절차

세 후보 voice로 동일 script 생성 후 인간 청취:

```bash
# Charon — deep authoritative (1순위 추천)
VOICE=Charon python3 scripts/generate_narration.py
# Kore — clear professional
VOICE=Kore python3 scripts/generate_narration.py
# Aoede — warm
VOICE=Aoede python3 scripts/generate_narration.py
```

각각 Scene 3 (Solution intro) 만 들어보고 권위 source line — "LINE Wallet 1.8억, 카카오·네이버, 삼성카드·CJ·이스트소프트" — 발음 자연스러움 기준으로 결정.

### 7.4 발음 보정 (필요 시)

Gemini TTS는 자연어 prompt로 보정 가능. 'p50, p90'이 자연스럽지 않으면:

```python
STYLE_INSTRUCTION = (
    "... When you encounter 'p50' or 'p90', pronounce them as "
    "'pee fifty' and 'pee ninety' clearly in English without pause. "
    "When you encounter 'hplan', pronounce as 'aitch-plan' clearly."
)
```

또는 phonetic substitution을 script 자체에 적용:
- `p50` → `피오십` (Korean) 또는 `pee fifty` (English)
- `hplan` → `에이치플랜`

### 7.5 BGM

Pixabay Music 또는 YouTube Audio Library에서 "ambient electronic, calm, 70-90s" 검색. CC0 또는 attribution-free 트랙 선택. Remotion에서 volume 0.15 (~-16dB) 로 narration 밑에 깔기.

## 8. Implementation roadmap (~10 hours)

| Phase | Tasks | Time |
|---|---|---|
| **P1. Setup** | `create-remotion-app`, theme.ts, Terminal/TypewriterText components | 1-2h |
| **P2. Scene 1-3** | Hook + Problem + Solution (text-driven, 비교적 simple) | 2-3h |
| **P3. Scene 4 demos** | 3개 터미널 데모 (핵심, 타이핑 effect + 색상 reveal) | 3-4h |
| **P4. Scene 5-6** | Lifecycle (PluginBox × 6) + CTA | 1.5h |
| **P5. Audio sync** | Narration TTS export + Audio component integration + BGM | 1h |
| **P6. Render + format** | 3 aspect ratios, file size optimize | 30min |
| **P7. README embed** | GitHub video asset upload + README markdown | 30min |
| **Total** | | **~10h** |

## 9. Render commands

```bash
# Setup
npx create-remotion-app hplan-intro --template react
cd hplan-intro
npm install @remotion/transitions @remotion/google-fonts @remotion/lambda

# Development (live preview)
npx remotion preview

# Render — 3 formats in parallel
npx remotion render HplanIntro16x9 out/intro-16x9.mp4 --concurrency=4
npx remotion render HplanIntro1x1  out/intro-1x1.mp4  --concurrency=4
npx remotion render HplanIntro9x16 out/intro-9x16.mp4 --concurrency=4

# Optional GIF fallback
npx remotion render HplanIntro16x9 out/intro.gif --image-format=jpeg --gif --width=1280
```

## 10. README embed snippet

```markdown
<!-- README.md 최상단 (badge 위) -->
<p align="center">
  <video src="https://github.com/user-attachments/assets/xxx/intro-16x9.mp4"
         autoplay loop muted playsinline width="800">
    <img src="docs/video/intro.gif" alt="hplan intro" />
  </video>
</p>
```

GitHub video assets는 10MB limit. mp4가 그 이상이면:
- 1280×720으로 downscale render
- 또는 YouTube에 upload 후 thumbnail + link embed
- 또는 GIF fallback (8-15MB)

## 11. Open questions

- [ ] BGM 트랙 최종 선택 (사용자 취향 — calm electronic / lo-fi / minimal piano 중)
- [ ] Gemini TTS voice A/B — `Charon` vs `Kore` vs `Aoede` 중 hplan brand voice에 어느 게 맞는지 청취 비교
- [ ] 'p50, p90', 'hplan' 발음이 자연스러운지 — 필요 시 phonetic substitution 또는 style prompt 보정
- [ ] GitHub video asset 업로드 vs YouTube embed 결정 (mp4 10MB 한도)
- [ ] 영어 dubbing 별도 버전 제작 여부 — 같은 Gemini TTS로 영어 voice 생성하면 ~1시간 추가 작업으로 글로벌 audience 커버 가능
