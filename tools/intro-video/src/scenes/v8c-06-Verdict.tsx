import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';

const VERDICTS = [
  { word: 'GO', desc: '만들어도 된다', color: 'ok' as const, start: 30 },
  { word: 'HOLD', desc: '지금은 멈춰야 한다', color: 'bad' as const, start: 90 },
  { word: 'INVESTIGATE', desc: '증거가 더 필요하다', color: 'warn' as const, start: 150 },
];

/** v0.8 Core — Scene 6 — Verdict (61-69s, 240 frames). */
export const V8CVerdict: React.FC = () => {
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [220, 240], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.bg,
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: fonts.display,
        textAlign: 'center',
        opacity: fadeOut,
      }}
    >
      <div
        style={{
          fontSize: 28,
          color: colors.veryDim,
          marginBottom: 56,
          letterSpacing: '0.05em',
          opacity: interpolate(frame, [0, 30], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }),
        }}
      >
        결과는 단순합니다.
      </div>

      <div style={{ display: 'flex', gap: 80, alignItems: 'baseline', fontFamily: fonts.mono }}>
        {VERDICTS.map((v) => {
          const sp = spring({ frame: frame - v.start, fps: FPS, config: { mass: 0.5, damping: 14 }, from: 0, to: 1 });
          return (
            <div key={v.word} style={{ opacity: sp, transform: `scale(${sp})` }}>
              <div
                style={{
                  fontSize: 64,
                  fontWeight: 700,
                  color: colors[v.color],
                  letterSpacing: '-0.02em',
                  lineHeight: 1,
                }}
              >
                {v.word}
              </div>
              <div
                style={{
                  marginTop: 16,
                  fontSize: 20,
                  color: colors.dim,
                  fontFamily: fonts.display,
                }}
              >
                {v.desc}
              </div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
