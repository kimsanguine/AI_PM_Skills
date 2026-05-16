import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import { colors, fonts, typography } from '../theme';

const SECTIONS = [
  { key: 'three_second_rule', value: '"5분에 슬라이드 만드는 AI"', start: 90 },
  { key: 'next_action', value: '"무료로 시작" — 단 1개', start: 165 },
  { key: 'social_proof', value: '"26M 사용자가 만든 팀"', start: 240 },
  { key: 'hierarchy_rules', value: '60 / 30 / 10 · max 7 elements', start: 315 },
  { key: 'motion_language', value: 'hover 200ms · cubic-bezier', start: 390 },
];

/**
 * v0.8 Editorial — Scene 2 — Respect (8-25s, 510 frames).
 * 영상 5번 통찰 인용 + RESPECT.md 5 섹션 fade-in.
 */
export const V8ERespect: React.FC = () => {
  const frame = useCurrentFrame();

  const quoteOpacity = interpolate(frame, [10, 60], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const quoteY = interpolate(frame, [10, 60], [20, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const fadeOut = interpolate(frame, [490, 510], [1, 0], {
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
        padding: '0 120px',
        opacity: fadeOut,
      }}
    >
      <div
        style={{
          fontSize: 56,
          fontWeight: 300,
          color: colors.text,
          opacity: quoteOpacity,
          transform: `translateY(${quoteY}px)`,
          textAlign: 'center',
          lineHeight: 1.3,
          letterSpacing: '-0.02em',
          maxWidth: 1400,
        }}
      >
        "이 존중은{' '}
        <span style={{ color: colors.craftRose, fontWeight: 600 }}>사람</span>이
        넣는 겁니다."
      </div>
      <div
        style={{
          marginTop: 24,
          fontSize: typography.captionSize,
          color: colors.veryDim,
          letterSpacing: '0.1em',
          opacity: quoteOpacity,
        }}
      >
        — UX 심리학 5번 원칙
      </div>

      <div
        style={{
          marginTop: 72,
          display: 'flex',
          flexDirection: 'column',
          gap: 18,
          fontFamily: fonts.mono,
          fontSize: 22,
          minWidth: 720,
        }}
      >
        {SECTIONS.map((s) => {
          const opacity = interpolate(
            frame,
            [s.start, s.start + 30],
            [0, 1],
            { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
          );
          const x = interpolate(
            frame,
            [s.start, s.start + 30],
            [-12, 0],
            { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
          );
          return (
            <div
              key={s.key}
              style={{
                opacity,
                transform: `translateX(${x}px)`,
                display: 'flex',
                gap: 24,
                alignItems: 'baseline',
              }}
            >
              <span style={{ color: colors.craftRose, fontWeight: 500 }}>
                {s.key}:
              </span>
              <span style={{ color: colors.text }}>{s.value}</span>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
