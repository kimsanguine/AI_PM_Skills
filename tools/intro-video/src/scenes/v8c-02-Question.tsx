import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';

/** v0.8 Core — Scene 2 — Question (10-18s, 240 frames). WHETHER vs HOW. */
export const V8CQuestion: React.FC = () => {
  const frame = useCurrentFrame();
  const introOp = interpolate(frame, [10, 50], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const howOp = interpolate(frame, [60, 100], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const howDim = interpolate(frame, [140, 170], [1, 0.3], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const whetherSp = spring({ frame: frame - 130, fps: FPS, config: { mass: 0.6, damping: 14 }, from: 0, to: 1 });
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
          opacity: introOp,
          letterSpacing: '0.02em',
          marginBottom: 40,
        }}
      >
        PM 에게 더 중요한 질문은 따로 있습니다.
      </div>

      <div
        style={{
          fontSize: 48,
          color: colors.dim,
          opacity: howOp * howDim,
          fontWeight: 300,
          letterSpacing: '-0.02em',
          textDecoration: howDim < 0.5 ? 'line-through' : 'none',
          transition: 'text-decoration 0.3s',
        }}
      >
        "어떻게 만들까?" 가 아니라
      </div>

      <div
        style={{
          marginTop: 32,
          fontSize: 72,
          color: colors.hplanRed,
          opacity: whetherSp,
          transform: `scale(${whetherSp})`,
          fontWeight: 700,
          letterSpacing: '-0.03em',
        }}
      >
        "이걸 만들어도 되는가?"
      </div>
    </AbsoluteFill>
  );
};
