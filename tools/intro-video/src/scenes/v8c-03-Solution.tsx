import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';

/** v0.8 Core — Scene 3 — Solution (18-26s, 240 frames). */
export const V8CSolution: React.FC = () => {
  const frame = useCurrentFrame();
  const logoSp = spring({ frame: frame - 20, fps: FPS, config: { mass: 0.6, damping: 14 }, from: 0, to: 1 });
  const tagOp = interpolate(frame, [60, 110], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const subOp = interpolate(frame, [130, 180], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
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
          fontSize: 120,
          fontWeight: 700,
          color: colors.hplanRed,
          opacity: logoSp,
          transform: `scale(${logoSp})`,
          letterSpacing: '-0.04em',
          fontFamily: fonts.mono,
        }}
      >
        hplan
      </div>

      <div
        style={{
          marginTop: 24,
          fontSize: 44,
          color: colors.text,
          opacity: tagOp,
          fontWeight: 300,
          letterSpacing: '-0.02em',
        }}
      >
        Product Build Gate
      </div>

      <div
        style={{
          marginTop: 56,
          fontSize: 22,
          color: colors.dim,
          opacity: subOp,
          letterSpacing: '-0.01em',
          maxWidth: 1200,
          lineHeight: 1.5,
        }}
      >
        AI 개발 도구가{' '}
        <span style={{ color: colors.trackBlue, fontWeight: 600 }}>HOW</span> 를 빠르게 만든다면,
        <br />
        hplan 은 그 전에{' '}
        <span style={{ color: colors.hplanRed, fontWeight: 600 }}>WHETHER</span> 를 검증합니다.
      </div>
    </AbsoluteFill>
  );
};
