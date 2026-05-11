import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';

/**
 * Scene 3 — Solution intro (20-28s, 240 frames).
 * hplan logo + Harness Planning meaning + Ethan authority line.
 */
export const SceneSolution: React.FC = () => {
  const frame = useCurrentFrame();

  // Logo enters at frame 5
  const logoScale = spring({
    frame: frame - 5,
    fps: FPS,
    config: { mass: 0.7, damping: 13, stiffness: 200 },
    from: 0.5,
    to: 1,
  });
  const logoOpacity = interpolate(frame, [5, 25], [0, 1], { extrapolateRight: 'clamp' });

  // Subtitle "Harness Planning" at frame 35
  const subOpacity = interpolate(frame, [35, 55], [0, 1], { extrapolateRight: 'clamp' });

  // Meaning paragraph at frame 75
  const meaningOpacity = interpolate(frame, [75, 105], [0, 1], { extrapolateRight: 'clamp' });

  // Authority line at frame 150
  const authorityOpacity = interpolate(frame, [150, 180], [0, 1], { extrapolateRight: 'clamp' });
  const authorityY = interpolate(frame, [150, 180], [12, 0], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.bg,
        fontFamily: fonts.display,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 60,
        textAlign: 'center',
      }}
    >
      {/* hplan logo */}
      <div
        style={{
          opacity: logoOpacity,
          transform: `scale(${logoScale})`,
          display: 'flex',
          alignItems: 'baseline',
          gap: 16,
        }}
      >
        <div
          style={{
            fontSize: 120,
            fontWeight: 900,
            color: colors.text,
            fontFamily: fonts.mono,
            letterSpacing: '-0.04em',
            lineHeight: 1,
          }}
        >
          hplan
        </div>
        <div style={{ fontSize: 64 }}>🐎</div>
      </div>

      {/* Subtitle */}
      <div
        style={{
          fontSize: 32,
          color: colors.skillTag,
          marginTop: 16,
          opacity: subOpacity,
          fontWeight: 600,
          letterSpacing: '0.04em',
        }}
      >
        Harness Planning
      </div>

      {/* Meaning */}
      <div
        style={{
          fontSize: 26,
          color: colors.text,
          marginTop: 56,
          opacity: meaningOpacity,
          lineHeight: 1.5,
          fontWeight: 500,
          maxWidth: 920,
        }}
      >
        AI 코딩 도구의 거친 동력에 <br />
        <span style={{ color: colors.ok, fontWeight: 700 }}>방향을 부여하는 사전 계획</span>입니다.
      </div>

      <div
        style={{
          fontSize: 16,
          color: colors.veryDim,
          marginTop: 12,
          opacity: meaningOpacity,
        }}
      >
        Direction for the raw power of AI coding tools.
      </div>

      {/* Authority line */}
      <div
        style={{
          position: 'absolute',
          bottom: 70,
          fontSize: 18,
          color: colors.dim,
          opacity: authorityOpacity,
          transform: `translateY(${authorityY}px)`,
          fontWeight: 500,
          letterSpacing: '0.02em',
        }}
      >
        LINE Wallet 1.8억 · 카카오 · 네이버 · 삼성카드 · CJ · 이스트소프트 PM
      </div>
    </AbsoluteFill>
  );
};
