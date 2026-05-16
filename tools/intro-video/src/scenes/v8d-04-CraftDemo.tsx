import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, typography, FPS } from '../theme';

const RULES = [
  { k: 'fold_density', v: '5 / 7', pass: true, start: 130 },
  { k: 'color_ratio', v: '62 / 30 / 8', pass: true, start: 180 },
  { k: 'whitespace', v: '0.43 ≥ 0.4', pass: true, start: 230 },
  { k: 'cta_count', v: '1 / 1', pass: true, start: 280 },
  { k: 'WCAG_AA', v: '4.7 : 1', pass: true, start: 330 },
];

/** v0.8 Demo — Scene 4 — Craft Demo (30-45s, 450 frames). */
export const V8DCraftDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const titleOp = interpolate(frame, [10, 40], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  // 60/30/10 bar
  const barOp = interpolate(frame, [50, 110], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const bar60 = interpolate(frame, [50, 110], [0, 600], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const bar30 = interpolate(frame, [70, 130], [0, 300], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const bar10 = interpolate(frame, [90, 150], [0, 100], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  const fadeOut = interpolate(frame, [430, 450], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

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
      <div style={{ fontSize: typography.titleSize, fontWeight: 300, color: colors.craftRose, opacity: titleOp, marginBottom: 16, letterSpacing: '-0.02em' }}>
        <span style={{ color: colors.text }}>craft</span> — Playwright runtime measurement
      </div>
      <div style={{ fontSize: typography.captionSize, color: colors.dim, opacity: titleOp, marginBottom: 32, fontFamily: fonts.mono }}>
        screen: landing · viewport 1440×1080 · LLM 호출 0
      </div>

      {/* 60/30/10 color ratio bar */}
      <div style={{ display: 'flex', height: 40, opacity: barOp, borderRadius: 4, overflow: 'hidden', boxShadow: '0 0 0 1px ' + colors.veryDim }}>
        <div style={{ width: bar60, backgroundColor: colors.bg, borderRight: '1px solid ' + colors.veryDim }} />
        <div style={{ width: bar30, backgroundColor: colors.surface }} />
        <div style={{ width: bar10, backgroundColor: colors.craftRose }} />
      </div>
      <div style={{ marginTop: 8, display: 'flex', gap: 40, opacity: barOp, fontFamily: fonts.mono, fontSize: 14, color: colors.dim }}>
        <span>60% bg</span>
        <span>30% surface</span>
        <span style={{ color: colors.craftRose }}>10% CTA</span>
      </div>

      {/* 5 rules pass check */}
      <div style={{ marginTop: 48, display: 'flex', flexDirection: 'column', gap: 14, fontFamily: fonts.mono, fontSize: 22 }}>
        {RULES.map((r) => {
          const op = interpolate(frame, [r.start, r.start + 25], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
          const x = interpolate(frame, [r.start, r.start + 25], [-10, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
          return (
            <div key={r.k} style={{ opacity: op, transform: `translateX(${x}px)`, display: 'flex', gap: 20, alignItems: 'baseline', minWidth: 480 }}>
              <span style={{ color: colors.ok, width: 24 }}>✓</span>
              <span style={{ color: colors.craftRose, minWidth: 180 }}>{r.k}</span>
              <span style={{ color: colors.text }}>{r.v}</span>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
