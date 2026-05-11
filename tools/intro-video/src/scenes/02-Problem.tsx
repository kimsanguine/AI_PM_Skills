import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';

interface Capability {
  ko: string;
  en: string;
}

const CAPABILITIES: Capability[] = [
  { ko: '무엇을 만들지', en: 'Discovery' },
  { ko: '왜 진짜 페인인가', en: 'Validation' },
  { ko: '내가 만든 게 가치 있나', en: 'PMF / Eval' },
  { ko: '첫 사용자 어떻게', en: 'Acquisition' },
];

/**
 * Scene 2 — Problem (6-20s, 420 frames).
 * 4 PM-thinking gaps appear sequentially → final punchline:
 * "코딩이 아니라 — 시장조사와 문제정의입니다"
 */
export const SceneProblem: React.FC = () => {
  const frame = useCurrentFrame();

  // 4 capabilities appear at frames 30, 75, 120, 165
  const capAppearFrames = [30, 75, 120, 165];

  // Conclusion appears at frame 270
  const conclusionAt = 270;
  const conclusionOpacity = interpolate(frame, [conclusionAt, conclusionAt + 18], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const conclusionScale = spring({
    frame: frame - conclusionAt,
    fps: FPS,
    config: { mass: 0.6, damping: 12, stiffness: 200 },
    from: 0.85,
    to: 1,
  });

  // Pre-conclusion line: "이 네 가지가 비어있는 채로 코드를 씁니다"
  const subAt = 220;
  const subOpacity = interpolate(frame, [subAt, subAt + 18], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Capabilities should fade out as conclusion appears (visual focus shift)
  const capFadeOut = interpolate(frame, [conclusionAt - 10, conclusionAt + 12], [1, 0.18], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.bg,
        fontFamily: fonts.display,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        padding: 60,
      }}
    >
      {/* Header label */}
      <div
        style={{
          fontSize: 18,
          color: colors.veryDim,
          marginBottom: 40,
          letterSpacing: 2,
          textTransform: 'uppercase',
          opacity: interpolate(frame, [10, 30], [0, 1], { extrapolateRight: 'clamp' }),
        }}
      >
        AI 시대 — 비개발자가 빌딩에 뛰어들 때 부족해진 4가지
      </div>

      {/* 4 capability cards in 2×2 grid */}
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: 24,
          maxWidth: 1100,
          opacity: capFadeOut,
        }}
      >
        {CAPABILITIES.map((cap, idx) => {
          const appearAt = capAppearFrames[idx];
          const scale = spring({
            frame: frame - appearAt,
            fps: FPS,
            config: { mass: 0.5, damping: 12, stiffness: 200 },
            from: 0.7,
            to: 1,
          });
          const opacity = interpolate(frame, [appearAt, appearAt + 12], [0, 1], {
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          });
          return (
            <div
              key={cap.ko}
              style={{
                padding: '24px 32px',
                backgroundColor: colors.surface,
                borderRadius: 14,
                border: `2px solid ${colors.titleBar}`,
                opacity,
                transform: `scale(${scale})`,
              }}
            >
              <div
                style={{
                  fontSize: 14,
                  color: colors.veryDim,
                  marginBottom: 8,
                  fontFamily: fonts.mono,
                }}
              >
                {String(idx + 1).padStart(2, '0')} · {cap.en}
              </div>
              <div
                style={{
                  fontSize: 30,
                  fontWeight: 700,
                  color: colors.text,
                }}
              >
                {cap.ko}
              </div>
            </div>
          );
        })}
      </div>

      {/* Sub line — bridge */}
      <div
        style={{
          fontSize: 20,
          color: colors.dim,
          marginTop: 32,
          opacity: subOpacity,
          fontStyle: 'italic',
        }}
      >
        이 네 가지가 비어있는 채로 코드를 씁니다.
      </div>

      {/* Final conclusion */}
      <div
        style={{
          marginTop: 40,
          textAlign: 'center',
          opacity: conclusionOpacity,
          transform: `scale(${conclusionScale})`,
        }}
      >
        <div
          style={{
            fontSize: 48,
            fontWeight: 800,
            color: colors.text,
            lineHeight: 1.25,
          }}
        >
          문제는 코딩이 아닙니다.
          <br />
          <span style={{ color: colors.ok }}>시장조사와 문제정의입니다.</span>
        </div>
        <div
          style={{
            fontSize: 18,
            color: colors.veryDim,
            marginTop: 16,
            fontWeight: 500,
          }}
        >
          The bottleneck isn't code. It's market research + problem definition.
        </div>
      </div>
    </AbsoluteFill>
  );
};
