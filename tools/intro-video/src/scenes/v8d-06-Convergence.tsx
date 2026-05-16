import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, typography, FPS } from '../theme';

const ROUNDS = [
  { n: 1, findings: 4, high: 3, version: 'v0.8.2', start: 90 },
  { n: 2, findings: 3, high: 1, version: 'v0.8.3', start: 180 },
  { n: 3, findings: 1, high: 0, version: 'v0.8.4', start: 270 },
];

/** v0.8 Demo — Scene 6 — Convergence (60-75s, 450 frames). */
export const V8DConvergence: React.FC = () => {
  const frame = useCurrentFrame();
  const titleOp = interpolate(frame, [10, 40], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const summarySp = spring({ frame: frame - 360, fps: FPS, config: { mass: 0.6, damping: 14 }, from: 0, to: 1 });
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
      <div style={{ fontSize: typography.titleSize, fontWeight: 300, color: colors.text, opacity: titleOp, marginBottom: 16, letterSpacing: '-0.02em' }}>
        3 라운드 cross-model 적대적 검수
      </div>
      <div style={{ fontSize: typography.captionSize, color: colors.dim, opacity: titleOp, marginBottom: 56, fontFamily: fonts.mono }}>
        Codex GPT-5 reviews hplan v0.8.0 → v0.8.4
      </div>

      <div style={{ display: 'flex', gap: 64, fontFamily: fonts.mono }}>
        {ROUNDS.map((r) => {
          const sp = spring({ frame: frame - r.start, fps: FPS, config: { mass: 0.5, damping: 14 }, from: 0, to: 1 });
          const findingsSize = interpolate(r.findings, [0, 4], [48, 96]);
          return (
            <div key={r.n} style={{ opacity: sp, transform: `scale(${sp})`, textAlign: 'center', minWidth: 200 }}>
              <div style={{ fontSize: 16, color: colors.veryDim, letterSpacing: '0.15em', textTransform: 'uppercase' }}>
                Round {r.n}
              </div>
              <div style={{ fontSize: findingsSize, fontWeight: 200, color: r.high > 0 ? colors.bad : colors.ok, lineHeight: 1, marginTop: 12, letterSpacing: '-0.04em' }}>
                {r.findings}
              </div>
              <div style={{ fontSize: 14, color: colors.dim, marginTop: 4 }}>findings</div>
              <div style={{ marginTop: 12, fontSize: 14, color: r.high > 0 ? colors.bad : colors.veryDim }}>
                {r.high} high
              </div>
              <div style={{ marginTop: 16, fontSize: 14, color: colors.dim, fontFamily: fonts.mono }}>
                → {r.version}
              </div>
            </div>
          );
        })}
      </div>

      <div style={{ marginTop: 64, fontSize: 28, color: colors.text, opacity: summarySp, transform: `scale(${summarySp})`, letterSpacing: '-0.01em' }}>
        4 → 3 → <span style={{ color: colors.ok, fontWeight: 600 }}>1</span> · high 잔여{' '}
        <span style={{ color: colors.ok, fontWeight: 600 }}>0</span>
      </div>
    </AbsoluteFill>
  );
};
