import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import { colors, fonts, typography } from '../theme';

/** v0.8 Demo — Scene 2 — Two Gaps (5-15s, 300 frames). */
export const V8DTwoGaps: React.FC = () => {
  const frame = useCurrentFrame();
  const titleOp = interpolate(frame, [10, 40], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const arrowOp = interpolate(frame, [60, 120], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const gap1Op = interpolate(frame, [130, 170], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const gap2Op = interpolate(frame, [200, 240], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [280, 300], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.bg,
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: fonts.display,
        opacity: fadeOut,
      }}
    >
      <div style={{ fontSize: typography.titleSize, fontWeight: 300, color: colors.text, opacity: titleOp, marginBottom: 64, letterSpacing: '-0.02em' }}>
        build → ship 사이, 2개 빈 공간
      </div>
      <div style={{ display: 'flex', gap: 24, alignItems: 'center', fontFamily: fonts.mono, fontSize: 28 }}>
        <Pill label="build" color={colors.dim} opacity={titleOp} />
        <Arrow opacity={arrowOp} />
        <Gap label="진행률 가시성?" sub="prompt-level" color={colors.trackBlue} opacity={gap1Op} />
        <Arrow opacity={arrowOp} />
        <Gap label="사용자 존중?" sub="UI/UX 디자인" color={colors.craftRose} opacity={gap2Op} />
        <Arrow opacity={arrowOp} />
        <Pill label="ship" color={colors.dim} opacity={titleOp} />
      </div>
    </AbsoluteFill>
  );
};

const Pill: React.FC<{ label: string; color: string; opacity: number }> = ({ label, color, opacity }) => (
  <div style={{ opacity, padding: '14px 24px', border: `2px solid ${color}`, borderRadius: 8, color }}>
    {label}
  </div>
);

const Gap: React.FC<{ label: string; sub: string; color: string; opacity: number }> = ({ label, sub, color, opacity }) => (
  <div style={{ opacity, padding: '14px 24px', border: `2px dashed ${color}`, borderRadius: 8, textAlign: 'center', backgroundColor: `${color}11` }}>
    <div style={{ color, fontSize: 24, fontWeight: 600 }}>{label}</div>
    <div style={{ color: colors.veryDim, fontSize: 14, marginTop: 4 }}>{sub}</div>
  </div>
);

const Arrow: React.FC<{ opacity: number }> = ({ opacity }) => (
  <span style={{ color: colors.veryDim, fontSize: 28, opacity }}>→</span>
);
