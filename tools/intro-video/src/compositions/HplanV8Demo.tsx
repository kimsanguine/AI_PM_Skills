import React from 'react';
import { AbsoluteFill, Sequence } from 'remotion';
import { V8D_TIMING, colors } from '../theme';
import { V8DHook } from '../scenes/v8d-01-Hook';
import { V8DTwoGaps } from '../scenes/v8d-02-TwoGaps';
import { V8DTrackDemo } from '../scenes/v8d-03-TrackDemo';
import { V8DCraftDemo } from '../scenes/v8d-04-CraftDemo';
import { V8DLifecycle } from '../scenes/v8d-05-Lifecycle';
import { V8DConvergence } from '../scenes/v8d-06-Convergence';
import { V8DCTA } from '../scenes/v8d-07-CTA';

const len = (k: keyof typeof V8D_TIMING): number => {
  const t = V8D_TIMING[k];
  return t.end - t.start;
};

/**
 * v0.8 Demo — 90s, 시스템·데모 위주.
 * Hook → TwoGaps → TrackDemo (burnup) → CraftDemo (60/30/10) → Lifecycle 9-stage → Convergence 4→3→1 → CTA.
 */
export const HplanV8Demo: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: colors.bg }}>
      <Sequence from={V8D_TIMING.hook.start} durationInFrames={len('hook')}>
        <V8DHook />
      </Sequence>
      <Sequence from={V8D_TIMING.twoGaps.start} durationInFrames={len('twoGaps')}>
        <V8DTwoGaps />
      </Sequence>
      <Sequence from={V8D_TIMING.trackDemo.start} durationInFrames={len('trackDemo')}>
        <V8DTrackDemo />
      </Sequence>
      <Sequence from={V8D_TIMING.craftDemo.start} durationInFrames={len('craftDemo')}>
        <V8DCraftDemo />
      </Sequence>
      <Sequence from={V8D_TIMING.lifecycle.start} durationInFrames={len('lifecycle')}>
        <V8DLifecycle />
      </Sequence>
      <Sequence from={V8D_TIMING.convergence.start} durationInFrames={len('convergence')}>
        <V8DConvergence />
      </Sequence>
      <Sequence from={V8D_TIMING.cta.start} durationInFrames={len('cta')}>
        <V8DCTA />
      </Sequence>
    </AbsoluteFill>
  );
};
