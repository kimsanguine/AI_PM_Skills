import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, typography, FPS } from '../theme';

/** v0.8 Demo — Scene 3 — Track Demo (15-30s, 450 frames). 가짜 burnup chart. */
export const V8DTrackDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const titleOp = interpolate(frame, [10, 40], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const chartOp = interpolate(frame, [50, 120], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  // Burnup line — predicted (straight) vs actual (curved with bump)
  const progress = interpolate(frame, [80, 380], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const blockerSp = spring({ frame: frame - 280, fps: FPS, config: { mass: 0.6, damping: 14 }, from: 0, to: 1 });
  const fadeOut = interpolate(frame, [430, 450], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  // Generate predicted vs actual paths
  const chartW = 800;
  const chartH = 320;
  const xAt = (t: number) => 80 + t * chartW;
  const predY = (t: number) => 40 + (1 - t) * chartH;
  // actual: slower at start, bumps around t=0.7 (blocker)
  const actY = (t: number) => {
    const bump = t > 0.65 && t < 0.78 ? Math.sin((t - 0.65) / 0.13 * Math.PI) * 30 : 0;
    return 40 + (1 - Math.pow(t, 1.3)) * chartH + bump;
  };

  const predPath = [...Array(50)].map((_, i) => {
    const t = (i / 49) * progress;
    return `${i === 0 ? 'M' : 'L'} ${xAt(t)} ${predY(t)}`;
  }).join(' ');
  const actPath = [...Array(50)].map((_, i) => {
    const t = (i / 49) * progress;
    return `${i === 0 ? 'M' : 'L'} ${xAt(t)} ${actY(t)}`;
  }).join(' ');

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
      <div style={{ fontSize: typography.titleSize, fontWeight: 300, color: colors.trackBlue, opacity: titleOp, marginBottom: 16, letterSpacing: '-0.02em' }}>
        <span style={{ color: colors.text }}>track</span> — predicted vs actual burnup
      </div>
      <div style={{ fontSize: typography.captionSize, color: colors.dim, opacity: titleOp, marginBottom: 32, fontFamily: fonts.mono }}>
        feature: user-auth-v2 · 7/12 tasks · 58%
      </div>

      <svg width={chartW + 100} height={chartH + 80} style={{ opacity: chartOp }}>
        {/* Axes */}
        <line x1={80} y1={40} x2={80} y2={chartH + 40} stroke={colors.veryDim} strokeWidth={1} />
        <line x1={80} y1={chartH + 40} x2={chartW + 80} y2={chartH + 40} stroke={colors.veryDim} strokeWidth={1} />
        {/* Predicted (dashed) */}
        <path d={predPath} stroke={colors.dim} strokeWidth={2} strokeDasharray="6 6" fill="none" />
        {/* Actual */}
        <path d={actPath} stroke={colors.trackBlue} strokeWidth={3} fill="none" />
        {/* Blocker marker */}
        {blockerSp > 0 && (
          <g opacity={blockerSp}>
            <circle cx={xAt(0.72)} cy={actY(0.72)} r={12} fill={colors.bad} opacity={0.3} />
            <circle cx={xAt(0.72)} cy={actY(0.72)} r={6} fill={colors.bad} />
            <text x={xAt(0.72) + 20} y={actY(0.72) + 5} fill={colors.bad} fontSize={16} fontFamily={fonts.mono}>
              T-008 blocker (score 17)
            </text>
          </g>
        )}
        {/* Legend */}
        <text x={chartW - 80} y={70} fill={colors.dim} fontSize={14} fontFamily={fonts.mono}>--- predicted</text>
        <text x={chartW - 80} y={92} fill={colors.trackBlue} fontSize={14} fontFamily={fonts.mono}>━━━ actual</text>
      </svg>

      <div style={{ marginTop: 24, fontFamily: fonts.mono, fontSize: 18, color: colors.dim, opacity: blockerSp }}>
        7 event-driven triggers · blocker score ≥ 8 → 자동 보고
      </div>
    </AbsoluteFill>
  );
};
