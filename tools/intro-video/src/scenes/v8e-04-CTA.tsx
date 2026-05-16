import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, typography, FPS } from '../theme';

/**
 * v0.8 Editorial — Scene 4 — CTA (50-60s, 300 frames).
 * "62 skills · 9 plugins · v0.8.4"
 */
export const V8ECTA: React.FC = () => {
  const frame = useCurrentFrame();

  const numbersOpacity = interpolate(frame, [20, 60], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const versionSp = spring({
    frame: frame - 100,
    fps: FPS,
    config: { mass: 0.6, damping: 14 },
    from: 0,
    to: 1,
  });

  const repoOpacity = interpolate(frame, [160, 200], [0, 1], {
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
      }}
    >
      <div
        style={{
          display: 'flex',
          gap: 80,
          alignItems: 'baseline',
          opacity: numbersOpacity,
        }}
      >
        <Stat n="62" label="skills" color={colors.text} />
        <Stat n="9" label="plugins" color={colors.craftRose} />
        <Stat n="26" label="commands" color={colors.trackBlue} />
      </div>

      <div
        style={{
          marginTop: 64,
          fontSize: typography.titleSize,
          fontWeight: 600,
          color: colors.text,
          opacity: versionSp,
          transform: `scale(${versionSp})`,
          letterSpacing: '-0.02em',
        }}
      >
        v0.8.4 — <span style={{ color: colors.craftRose }}>build to ship</span>,
        closed.
      </div>

      <div
        style={{
          marginTop: 40,
          fontSize: 20,
          color: colors.dim,
          fontFamily: fonts.mono,
          opacity: repoOpacity,
        }}
      >
        github.com/kimsanguine/hplan
      </div>
    </AbsoluteFill>
  );
};

const Stat: React.FC<{ n: string; label: string; color: string }> = ({
  n,
  label,
  color,
}) => (
  <div>
    <div style={{ fontSize: 144, fontWeight: 200, color, lineHeight: 1, letterSpacing: '-0.04em' }}>
      {n}
    </div>
    <div
      style={{
        fontSize: 18,
        color: colors.veryDim,
        fontFamily: fonts.mono,
        marginTop: 12,
        letterSpacing: '0.15em',
        textTransform: 'uppercase',
      }}
    >
      {label}
    </div>
  </div>
);
