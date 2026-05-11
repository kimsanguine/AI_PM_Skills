import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import { colors } from '../theme';
import { Terminal } from '../components/Terminal';
import { TerminalLine } from '../components/TerminalLine';
import { BilingualCaption } from '../components/BilingualCaption';
import { DEMO_EVIDENCE_LINES } from '../data/demoEvidence';

/**
 * Scene 4a — Evidence Gate demo (28-36s, 240 frames).
 */
export const SceneDemoEvidence: React.FC = () => {
  const frame = useCurrentFrame();
  const fadeIn = interpolate(frame, [0, 18], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.bg,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '80px 60px',
        opacity: fadeIn,
      }}
    >
      {/* Scene label */}
      <div
        style={{
          fontSize: 16,
          color: colors.veryDim,
          letterSpacing: 3,
          textTransform: 'uppercase',
          marginBottom: 24,
        }}
      >
        Demo 1 · Evidence Gate
      </div>

      <Terminal title="hplan-evidence — collision check">
        {DEMO_EVIDENCE_LINES.map((line) => (
          <TerminalLine
            key={`${line.appearAt}-${line.text}`}
            appearAt={line.appearAt}
            prompt={line.prompt}
            variant={line.variant}
          >
            {line.text}
          </TerminalLine>
        ))}
      </Terminal>

      <BilingualCaption
        appearAt={160}
        disappearAt={235}
        ko="이미 점유된 영역 — PRD 쓰기 전에 자동 차단"
        en="Territory already taken — auto-blocked before any PRD"
        bottom={50}
      />
    </AbsoluteFill>
  );
};
