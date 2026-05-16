import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, typography, FPS } from '../theme';

/** v0.8 Demo — Scene 7 — CTA (75-90s, 450 frames). */
export const V8DCTA: React.FC = () => {
  const frame = useCurrentFrame();
  const numbersOp = interpolate(frame, [20, 80], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const versionSp = spring({ frame: frame - 150, fps: FPS, config: { mass: 0.6, damping: 14 }, from: 0, to: 1 });
  const taglineOp = interpolate(frame, [240, 290], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const repoOp = interpolate(frame, [320, 380], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

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
      <div style={{ display: 'flex', gap: 80, alignItems: 'baseline', opacity: numbersOp }}>
        <Stat n="62" label="skills" color={colors.text} />
        <Stat n="9" label="plugins" color={colors.craftRose} />
        <Stat n="26" label="commands" color={colors.trackBlue} />
      </div>

      <div style={{ marginTop: 56, fontSize: 52, fontWeight: 600, color: colors.text, opacity: versionSp, transform: `scale(${versionSp})`, letterSpacing: '-0.02em' }}>
        v0.8.4 ready
      </div>

      <div style={{ marginTop: 32, fontSize: 22, color: colors.dim, opacity: taglineOp, letterSpacing: '-0.01em', maxWidth: 1200 }}>
        prompt-level progress · user-respect enforcement · Rule 5 결정론
      </div>

      <div style={{ marginTop: 48, fontSize: 20, color: colors.veryDim, fontFamily: fonts.mono, opacity: repoOp }}>
        github.com/kimsanguine/hplan
      </div>
    </AbsoluteFill>
  );
};

const Stat: React.FC<{ n: string; label: string; color: string }> = ({ n, label, color }) => (
  <div>
    <div style={{ fontSize: 144, fontWeight: 200, color, lineHeight: 1, letterSpacing: '-0.04em' }}>{n}</div>
    <div style={{ fontSize: 16, color: colors.veryDim, fontFamily: fonts.mono, marginTop: 12, letterSpacing: '0.15em', textTransform: 'uppercase' }}>
      {label}
    </div>
  </div>
);
