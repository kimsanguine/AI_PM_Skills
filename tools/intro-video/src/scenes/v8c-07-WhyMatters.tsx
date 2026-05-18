import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';

/** v0.8 Core — Scene 7 — Why Matters (69-79s, 300 frames). */
export const V8CWhyMatters: React.FC = () => {
  const frame = useCurrentFrame();
  const line1 = interpolate(frame, [10, 60], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const line2 = interpolate(frame, [90, 140], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const dangerSp = spring({ frame: frame - 180, fps: FPS, config: { mass: 0.6, damping: 14 }, from: 0, to: 1 });
  const fadeOut = interpolate(frame, [280, 300], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.bg,
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: fonts.display,
        textAlign: 'center',
        padding: '0 120px',
        opacity: fadeOut,
      }}
    >
      <div
        style={{
          fontSize: 40,
          color: colors.dim,
          opacity: line1,
          letterSpacing: '-0.01em',
          maxWidth: 1400,
          lineHeight: 1.4,
        }}
      >
        AI 시대에는{' '}
        <span style={{ color: colors.text, fontWeight: 600 }}>만드는 속도가 병목이 아닙니다</span>.
      </div>

      <div
        style={{
          marginTop: 32,
          fontSize: 32,
          color: colors.dim,
          opacity: line2,
          letterSpacing: '-0.01em',
          maxWidth: 1300,
          lineHeight: 1.5,
        }}
      >
        오히려 너무 빨리 만들 수 있기 때문에,
      </div>

      <div
        style={{
          marginTop: 24,
          fontSize: 52,
          fontWeight: 700,
          color: colors.hplanRed,
          opacity: dangerSp,
          transform: `scale(${dangerSp})`,
          letterSpacing: '-0.02em',
          maxWidth: 1400,
          lineHeight: 1.3,
        }}
      >
        잘못된 것을 더 빨리 만들 위험이 커졌습니다.
      </div>
    </AbsoluteFill>
  );
};
