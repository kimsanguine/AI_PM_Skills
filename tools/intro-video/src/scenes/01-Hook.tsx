import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';

/**
 * Scene 1 — Hook (0-6s, 180 frames).
 * "Claude Code로 만든 SaaS. 6개월 뒤, 안 팔립니다."
 */
export const SceneHook: React.FC = () => {
  const frame = useCurrentFrame();

  // Line 1 appears at frame 30 (1s), fully visible by frame 50
  const line1Opacity = interpolate(frame, [30, 50], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const line1Y = interpolate(frame, [30, 50], [12, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Line 2 appears at frame 90 (3s)
  const line2Opacity = interpolate(frame, [90, 120], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const line2Y = interpolate(frame, [90, 120], [12, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Red flash on line 2 — "안 팔립니다"
  const redPulse = spring({
    frame: frame - 120,
    fps: FPS,
    config: { mass: 0.6, damping: 14 },
    from: 0,
    to: 1,
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.bg,
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: fonts.display,
        textAlign: 'center',
      }}
    >
      <div
        style={{
          fontSize: 52,
          fontWeight: 700,
          color: colors.dim,
          opacity: line1Opacity,
          transform: `translateY(${line1Y}px)`,
          marginBottom: 24,
        }}
      >
        Claude Code로 만든 SaaS.
      </div>
      <div
        style={{
          fontSize: 64,
          fontWeight: 800,
          color: interpolate(redPulse, [0, 1], [
            // start gray, transition to red
            0,
            1,
          ]) > 0.3 ? colors.bad : colors.text,
          opacity: line2Opacity,
          transform: `translateY(${line2Y}px) scale(${interpolate(redPulse, [0, 1], [1, 1.04])})`,
          letterSpacing: '-0.02em',
        }}
      >
        6개월 뒤, 안 팔립니다.
      </div>

      {/* English subtitle at the bottom */}
      <div
        style={{
          position: 'absolute',
          bottom: 80,
          fontSize: 18,
          color: colors.veryDim,
          fontWeight: 500,
          opacity: line2Opacity,
        }}
      >
        Built it with Claude Code. 6 months later — no buyers.
      </div>
    </AbsoluteFill>
  );
};
