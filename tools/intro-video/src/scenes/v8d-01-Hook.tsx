import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, typography, FPS } from '../theme';

/** v0.8 Demo — Scene 1 — Hook (0-5s, 150 frames). */
export const V8DHook: React.FC = () => {
  const frame = useCurrentFrame();
  const line1 = interpolate(frame, [10, 35], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const line2Sp = spring({ frame: frame - 70, fps: FPS, config: { mass: 0.6, damping: 14 }, from: 0, to: 1 });
  const fadeOut = interpolate(frame, [130, 150], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

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
      <div style={{ fontSize: 48, fontWeight: 300, color: colors.text, opacity: line1, letterSpacing: '-0.02em' }}>
        AI 가 코드는 만들어 줍니다.
      </div>
      <div
        style={{
          marginTop: 28,
          fontSize: 64,
          fontWeight: 600,
          color: colors.hplanRed,
          opacity: line2Sp,
          transform: `scale(${line2Sp})`,
          letterSpacing: '-0.02em',
        }}
      >
        그런데 왜 ship 후 안 팔릴까?
      </div>
    </AbsoluteFill>
  );
};
