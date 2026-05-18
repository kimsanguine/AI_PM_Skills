import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import { colors, fonts } from '../theme';

const QUESTIONS = [
  '고객이 정말 이 문제를 겪고 있는가?',
  '실제 증거가 충분한가?',
  '이미 우리가 죽였던 아이디어는 아닌가?',
  '경쟁사가 이미 장악한 영역은 아닌가?',
  'AI 사용량과 COGS를 고려해도 사업성이 있는가?',
  '지금 PRD를 써도 되는 상태인가?',
];

/** v0.8 Core — Scene 4 — Six Questions (26-41s, 450 frames). */
export const V8CSixQuestions: React.FC = () => {
  const frame = useCurrentFrame();
  const titleOp = interpolate(frame, [10, 50], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
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
      <div
        style={{
          fontSize: 40,
          color: colors.dim,
          opacity: titleOp,
          marginBottom: 56,
          letterSpacing: '-0.01em',
        }}
      >
        만들기 전에 멈춰서 묻습니다.
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 22, maxWidth: 1100 }}>
        {QUESTIONS.map((q, i) => {
          const start = 80 + i * 45;
          const op = interpolate(frame, [start, start + 30], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
          const x = interpolate(frame, [start, start + 30], [-16, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
          return (
            <div
              key={i}
              style={{
                opacity: op,
                transform: `translateX(${x}px)`,
                fontSize: 30,
                color: colors.text,
                display: 'flex',
                gap: 20,
                alignItems: 'baseline',
                letterSpacing: '-0.01em',
              }}
            >
              <span style={{ color: colors.hplanRed, fontWeight: 700, fontFamily: fonts.mono }}>•</span>
              {q}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
