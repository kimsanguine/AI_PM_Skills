#!/usr/bin/env python3
"""Generate 8 narration audio clips for the hplan intro video via Gemini TTS.

Requirements:
    pip install google-genai
    Set environment variable GEMINI_API_KEY (or pass --api-key)

Voice A/B testing:
    VOICE=Charon python3 generate_narration.py    # deep authoritative (1st pick)
    VOICE=Kore   python3 generate_narration.py    # clear professional
    VOICE=Aoede  python3 generate_narration.py    # warm

Output:
    Writes WAV files to ../public/audio/narration/{slug}.wav

Post-processing (smaller file size):
    for f in public/audio/narration/*.wav; do
        ffmpeg -i "$f" -codec:a libmp3lame -qscale:a 4 "${f%.wav}.mp3"
        rm "$f"
    done
"""
from __future__ import annotations

import argparse
import os
import sys
import wave
from pathlib import Path


SCENES: dict[str, str] = {
    "01-hook": "Claude Code로 만든 SaaS. 6개월 뒤, 안 팔립니다.",
    "02-problem": (
        "AI 도구는 빠르게 만들어줍니다. "
        "그런데, 정말 만들어야 할지는 누구도 묻지 않습니다. "
        "무엇을, 왜, 누가, 어떻게. "
        "이 네 가지가 비어있는 채로 코드를 씁니다. "
        "문제는 코딩이 아닙니다. 시장조사와 문제정의입니다."
    ),
    "03-solution": (
        "에이치플랜. Harness Planning. "
        "AI 코딩 도구의 거친 동력에 방향을 부여하는, 사전 계획입니다."
    ),
    "04a-evidence": (
        "PRD 쓰기 전에, hplan은 이미 점유된 영역인지 자동으로 확인합니다. "
        "결정: 보류."
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
        "에이치플랜, 디스커버, 아키텍트, 딜리버, 메저, 런."
    ),
    "06-cta": (
        "30분 안에, 6개월을 막을 수 있습니다. "
        "에이치플랜. GitHub에서 검색하세요."
    ),
}

STYLE_INSTRUCTION = (
    "Read the following Korean text in a calm, authoritative, lecturer-like tone. "
    "Speak at a 1.0x natural pace. Emphasize key terms (마진, 음수, 결정, hplan) slightly. "
    "Pause briefly at sentence breaks. Sound like a senior PM with 20 years of experience "
    "who is teaching a single-founder workshop."
)


def generate(voice: str, api_key: str, out_dir: Path) -> None:
    """Generate all 8 scene narrations using Gemini TTS."""
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        sys.exit("ERROR: pip install google-genai")

    client = genai.Client(api_key=api_key)
    out_dir.mkdir(parents=True, exist_ok=True)

    for slug, text in SCENES.items():
        print(f"  → generating {slug} (voice={voice})...")
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=f"{STYLE_INSTRUCTION}\n\n{text}",
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=voice,
                        )
                    )
                ),
            ),
        )
        # Gemini TTS returns 24kHz mono PCM as inline_data.data (bytes)
        audio_data = response.candidates[0].content.parts[0].inline_data.data
        wav_path = out_dir / f"{slug}.wav"
        with wave.open(str(wav_path), "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(24000)
            wf.writeframes(audio_data)
        size_kb = wav_path.stat().st_size // 1024
        print(f"      → {wav_path.name}  ({size_kb} KB)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--voice",
        default=os.environ.get("VOICE", "Charon"),
        help="Gemini TTS voice name. Default: Charon. Try Kore or Aoede for A/B.",
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("GEMINI_API_KEY"),
        help="Gemini API key. Default: $GEMINI_API_KEY env var.",
    )
    parser.add_argument(
        "--out",
        default=str(Path(__file__).resolve().parent.parent / "public" / "audio" / "narration"),
        help="Output directory for .wav files.",
    )
    args = parser.parse_args()

    if not args.api_key:
        sys.exit("ERROR: GEMINI_API_KEY not set (export it or pass --api-key).")

    print(f"\nGenerating 8 scenes with voice='{args.voice}' → {args.out}\n")
    generate(args.voice, args.api_key, Path(args.out))
    print("\nDone. Next steps:")
    print("  1. (optional) Convert WAV → MP3 to shrink file size:")
    print("     cd public/audio/narration")
    print(
        "     for f in *.wav; do ffmpeg -i \"$f\" -codec:a libmp3lame -qscale:a 4 \"${f%.wav}.mp3\"; done"
    )
    print("  2. Uncomment the <Audio> imports in src/compositions/HplanIntro16x9.tsx")
    print("  3. Run `npm run dev` to preview the synced video.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
