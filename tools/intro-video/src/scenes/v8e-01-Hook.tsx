import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import { colors, fonts, typography } from '../theme';

/**
 * v0.8 Editorial — Scene 1 — Hook (0-8s, 240 frames).
 * "AI 는 기능을 만들어 줍니다."
 */
export const V8EHook: React.FC = () => {
  const frame = useCurrentFrame();

  const line1Opacity = interpolate(frame, [20, 50], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const line1Y = interpolate(frame, [20, 50], [16, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const accentOpacity = interpolate(frame, [110, 140], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const accentScale = interpolate(frame, [110, 150], [0.92, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const fadeOut = interpolate(frame, [220, 240], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

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
          fontSize: typography.hookSize,
          fontWeight: 300,
          color: colors.text,
          opacity: line1Opacity,
          transform: `translateY(${line1Y}px)`,
          letterSpacing: '-0.02em',
        }}
      >
        AI 는 기능을 만들어 줍니다.
      </div>
      <div
        style={{
          marginTop: 32,
          fontSize: typography.titleSize,
          fontWeight: 600,
          color: colors.craftRose,
          opacity: accentOpacity,
          transform: `scale(${accentScale})`,
          letterSpacing: '-0.01em',
        }}
      >
        그런데 이 존중은 누가 넣을까요?
      </div>
    </AbsoluteFill>
  );
};
