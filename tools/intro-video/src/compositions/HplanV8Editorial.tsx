import React from 'react';
import { AbsoluteFill, Sequence } from 'remotion';
import { V8E_TIMING, colors } from '../theme';
import { V8EHook } from '../scenes/v8e-01-Hook';
import { V8ERespect } from '../scenes/v8e-02-Respect';
import { V8ELifecycle } from '../scenes/v8e-03-Lifecycle';
import { V8ECTA } from '../scenes/v8e-04-CTA';

const len = (k: keyof typeof V8E_TIMING): number => {
  const t = V8E_TIMING[k];
  return t.end - t.start;
};

/**
 * v0.8 Editorial — 60s, 메시지 위주.
 * Hook → Respect (영상 5번 통찰) → Lifecycle 9-stage → CTA.
 */
export const HplanV8Editorial: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: colors.bg }}>
      <Sequence from={V8E_TIMING.hook.start} durationInFrames={len('hook')}>
        <V8EHook />
      </Sequence>
      <Sequence from={V8E_TIMING.respect.start} durationInFrames={len('respect')}>
        <V8ERespect />
      </Sequence>
      <Sequence from={V8E_TIMING.lifecycle.start} durationInFrames={len('lifecycle')}>
        <V8ELifecycle />
      </Sequence>
      <Sequence from={V8E_TIMING.cta.start} durationInFrames={len('cta')}>
        <V8ECTA />
      </Sequence>
    </AbsoluteFill>
  );
};
