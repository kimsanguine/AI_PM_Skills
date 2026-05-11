import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import { colors } from '../theme';
import { Terminal } from '../components/Terminal';
import { TerminalLine } from '../components/TerminalLine';
import { BilingualCaption } from '../components/BilingualCaption';
import { DEMO_COGS_LINES } from '../data/demoCogs';

/**
 * Scene 4b — COGS Sentinel demo (36-46s, 300 frames). HERO SCENE.
 */
export const SceneDemoCogs: React.FC = () => {
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
        Demo 2 · COGS Sentinel — Hero
      </div>

      <Terminal title="hplan-cogs — deterministic p50/p90 margin">
        {DEMO_COGS_LINES.map((line) => (
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
        appearAt={195}
        disappearAt={290}
        ko="p90 마진이 음수 — 출시했으면 적자"
        en="p90 margin negative — would have lost money at scale"
        bottom={50}
      />
    </AbsoluteFill>
  );
};
