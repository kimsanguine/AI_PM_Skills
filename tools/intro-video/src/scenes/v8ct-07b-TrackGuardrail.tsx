import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, typography, FPS } from '../theme';

/**
 * v0.8 Core+Track — Scene 7b — Track Guardrail (15s, 450 frames).
 * "GO 받았다 = 끝이 아닙니다 — track 이 만드는 중 가드레일"
 * v8d-03-TrackDemo 의 burnup 시각 재활용 + Build Gate ↔ Track 2-layer 메시지.
 */
export const V8CTTrackGuardrail: React.FC = () => {
  const frame = useCurrentFrame();

  // 인트로 텍스트 (0-3s)
  const introOp = interpolate(frame, [10, 60], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const introY = interpolate(frame, [10, 60], [16, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const introFade = interpolate(frame, [100, 130], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  // burnup chart (3-12s)
  const chartOp = interpolate(frame, [110, 160], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const progress = interpolate(frame, [140, 380], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const blockerSp = spring({ frame: frame - 300, fps: FPS, config: { mass: 0.6, damping: 14 }, from: 0, to: 1 });

  // closing layered message (12-15s)
  const layerOp = interpolate(frame, [370, 410], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [430, 450], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  // Burnup paths
  const chartW = 700;
  const chartH = 240;
  const xAt = (t: number) => 80 + t * chartW;
  const predY = (t: number) => 40 + (1 - t) * chartH;
  const actY = (t: number) => {
    const bump = t > 0.65 && t < 0.78 ? Math.sin(((t - 0.65) / 0.13) * Math.PI) * 24 : 0;
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
      {/* 인트로 텍스트 — 처음 3s 동안 단독 */}
      <div
        style={{
          position: 'absolute',
          top: '38%',
          opacity: introOp * introFade,
          transform: `translateY(${introY}px)`,
          textAlign: 'center',
          width: '100%',
        }}
      >
        <div style={{ fontSize: 28, color: colors.dim, marginBottom: 16, letterSpacing: '-0.01em' }}>
          GO가 나와도 끝이 아닙니다.
        </div>
        <div style={{ fontSize: 52, color: colors.text, fontWeight: 600, letterSpacing: '-0.02em' }}>
          <span style={{ color: colors.trackBlue }}>track</span> 은{' '}
          <span style={{ color: colors.hplanRed }}>진행 중</span>에도 작동하는 가드레일
        </div>
      </div>

      {/* burnup chart — 3s 후 등장 */}
      <div style={{ opacity: chartOp, marginTop: 40 }}>
        <div style={{ fontSize: 22, color: colors.dim, fontFamily: fonts.mono, marginBottom: 12, textAlign: 'center' }}>
          predicted vs actual · 7/12 tasks · 58%
        </div>
        <svg width={chartW + 100} height={chartH + 60}>
          <line x1={80} y1={40} x2={80} y2={chartH + 40} stroke={colors.veryDim} strokeWidth={1} />
          <line x1={80} y1={chartH + 40} x2={chartW + 80} y2={chartH + 40} stroke={colors.veryDim} strokeWidth={1} />
          <path d={predPath} stroke={colors.dim} strokeWidth={2} strokeDasharray="6 6" fill="none" />
          <path d={actPath} stroke={colors.trackBlue} strokeWidth={3} fill="none" />
          {blockerSp > 0 && (
            <g opacity={blockerSp}>
              <circle cx={xAt(0.72)} cy={actY(0.72)} r={12} fill={colors.bad} opacity={0.3} />
              <circle cx={xAt(0.72)} cy={actY(0.72)} r={6} fill={colors.bad} />
              <text x={xAt(0.72) + 16} y={actY(0.72) + 5} fill={colors.bad} fontSize={15} fontFamily={fonts.mono}>
                블로커 score 17 — 즉시 알림
              </text>
            </g>
          )}
          <text x={chartW - 70} y={70} fill={colors.dim} fontSize={13} fontFamily={fonts.mono}>--- predicted</text>
          <text x={chartW - 70} y={90} fill={colors.trackBlue} fontSize={13} fontFamily={fonts.mono}>━━━ actual</text>
        </svg>
      </div>

      {/* closing 2-layer 메시지 */}
      <div
        style={{
          position: 'absolute',
          bottom: 60,
          opacity: layerOp,
          textAlign: 'center',
          width: '100%',
          fontSize: 22,
          color: colors.dim,
          fontFamily: fonts.mono,
          letterSpacing: '-0.01em',
        }}
      >
        <span style={{ color: colors.hplanRed, fontWeight: 600 }}>Build Gate</span>{' '}
        는 시작 전,{' '}
        <span style={{ color: colors.trackBlue, fontWeight: 600 }}>Track</span>{' '}
        은 진행 중 — 잘못된 방향을 두 단계로 차단합니다
      </div>
    </AbsoluteFill>
  );
};
