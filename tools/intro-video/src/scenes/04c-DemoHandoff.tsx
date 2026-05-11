import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import { colors } from '../theme';
import { Terminal } from '../components/Terminal';
import { TerminalLine } from '../components/TerminalLine';
import { BilingualCaption } from '../components/BilingualCaption';
import { DEMO_HANDOFF_LINES } from '../data/demoHandoff';

/**
 * Scene 4c — Multi-target Handoff (46-55s, 270 frames).
 */
export const SceneDemoHandoff: React.FC = () => {
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
      <div
        style={{
          fontSize: 16,
          color: colors.veryDim,
          letterSpacing: 3,
          textTransform: 'uppercase',
          marginBottom: 24,
        }}
      >
        Demo 3 · Multi-target Handoff
      </div>

      <Terminal title="hplan-handoff — 1 brief → 4 ecosystems">
        {DEMO_HANDOFF_LINES.map((line) => (
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
        appearAt={200}
        disappearAt={262}
        ko="통과한 brief는 4개 코딩 ecosystem으로 1-click export"
        en="Approved brief → spec-kit / kiro / gstack / claude code in one shot"
        bottom={50}
      />
    </AbsoluteFill>
  );
};
