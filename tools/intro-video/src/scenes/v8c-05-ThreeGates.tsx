import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';

const GATES = [
  {
    n: 1,
    name: 'Evidence Gate',
    desc: '고객 증거와 문제 강도를 확인합니다',
    detail: 'interview · rubric · scoring',
    color: 'trackBlue' as const,
    start: 60,
  },
  {
    n: 2,
    name: 'Exclusions Gate',
    desc: '과거 제외 아이디어, 검토 리스크, 경쟁 영역을 다시 확인',
    detail: 'append-only registry · fuzzy match',
    color: 'craftRose' as const,
    start: 200,
  },
  {
    n: 3,
    name: 'COGS Gate',
    desc: 'AI 사용량 · 모델 비용 · 무료 abuse · 마진 리스크 계산',
    detail: 'lognormal p50/p90 sentinel',
    color: 'hplanRed' as const,
    start: 340,
  },
];

/** v0.8 Core — Scene 5 — Three Gates (41-61s, 600 frames). */
export const V8CThreeGates: React.FC = () => {
  const frame = useCurrentFrame();
  const titleOp = interpolate(frame, [10, 40], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [580, 600], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

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
          fontSize: 40,
          color: colors.dim,
          opacity: titleOp,
          marginBottom: 56,
          letterSpacing: '-0.01em',
        }}
      >
        hplan의 핵심은{' '}
        <span style={{ color: colors.text, fontWeight: 600 }}>세 가지 Gate</span>
      </div>

      <div style={{ display: 'flex', gap: 40, alignItems: 'stretch' }}>
        {GATES.map((g) => {
          const sp = spring({ frame: frame - g.start, fps: FPS, config: { mass: 0.6, damping: 14 }, from: 0, to: 1 });
          return (
            <div
              key={g.n}
              style={{
                opacity: sp,
                transform: `scale(${sp}) translateY(${(1 - sp) * 20}px)`,
                padding: '36px 40px',
                border: `2px solid ${colors[g.color]}`,
                borderRadius: 14,
                backgroundColor: `${colors[g.color]}11`,
                width: 560,
                textAlign: 'left',
              }}
            >
              <div style={{ fontSize: 22, color: colors[g.color], fontFamily: fonts.mono, letterSpacing: '0.2em', marginBottom: 14 }}>
                GATE {g.n}
              </div>
              <div style={{ fontSize: 36, color: colors[g.color], fontWeight: 600, letterSpacing: '-0.02em' }}>
                {g.name}
              </div>
              <div style={{ marginTop: 14, fontSize: 24, color: colors.text, lineHeight: 1.5 }}>
                {g.desc}
              </div>
              <div style={{ marginTop: 16, fontSize: 22, color: colors.veryDim, fontFamily: fonts.mono }}>
                {g.detail}
              </div>
            </div>
          );
        })}
      </div>

      <div
        style={{
          marginTop: 48,
          fontSize: 26,
          color: colors.dim,
          opacity: interpolate(frame, [470, 510], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }),
          letterSpacing: '-0.01em',
        }}
      >
        이 세 가지를 통과해야 다음 단계로 갑니다.
      </div>
    </AbsoluteFill>
  );
};
