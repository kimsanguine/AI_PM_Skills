import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import { colors, fonts, typography } from '../theme';

const TOOLS = [
  { name: 'Cursor', sub: '주말 안에 프로토타입', start: 90 },
  { name: 'Claude Code', sub: '밤새 첫 버전 구현', start: 150 },
  { name: 'Spec tools', sub: '한 시간에 PRD + 설계', start: 210 },
];

/** v0.8 Core — Scene 1 — Hook (0-10s, 300 frames). */
export const V8CHook: React.FC = () => {
  const frame = useCurrentFrame();
  const titleOp = interpolate(frame, [10, 60], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const titleY = interpolate(frame, [10, 60], [16, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
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
      <div
        style={{
          fontSize: 56,
          fontWeight: 300,
          color: colors.text,
          opacity: titleOp,
          transform: `translateY(${titleY}px)`,
          letterSpacing: '-0.02em',
          marginBottom: 64,
          textAlign: 'center',
        }}
      >
        AI 코딩 도구는 이제{' '}
        <span style={{ color: colors.trackBlue, fontWeight: 600 }}>충분히 빠릅니다</span>.
      </div>

      <div style={{ display: 'flex', gap: 48, fontFamily: fonts.mono }}>
        {TOOLS.map((t) => {
          const op = interpolate(frame, [t.start, t.start + 40], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
          const y = interpolate(frame, [t.start, t.start + 40], [20, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
          return (
            <div
              key={t.name}
              style={{
                opacity: op,
                transform: `translateY(${y}px)`,
                padding: '24px 32px',
                border: `1.5px solid ${colors.veryDim}`,
                borderRadius: 10,
                textAlign: 'center',
                minWidth: 280,
                backgroundColor: colors.surface,
              }}
            >
              <div style={{ fontSize: 26, fontWeight: 600, color: colors.text }}>{t.name}</div>
              <div style={{ fontSize: 16, color: colors.dim, marginTop: 8 }}>{t.sub}</div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
