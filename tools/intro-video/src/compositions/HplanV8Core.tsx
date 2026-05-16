import React from 'react';
import { AbsoluteFill, Sequence } from 'remotion';
import { V8C_TIMING, colors } from '../theme';
import { V8CHook } from '../scenes/v8c-01-Hook';
import { V8CQuestion } from '../scenes/v8c-02-Question';
import { V8CSolution } from '../scenes/v8c-03-Solution';
import { V8CSixQuestions } from '../scenes/v8c-04-SixQuestions';
import { V8CThreeGates } from '../scenes/v8c-05-ThreeGates';
import { V8CVerdict } from '../scenes/v8c-06-Verdict';
import { V8CWhyMatters } from '../scenes/v8c-07-WhyMatters';
import { V8CStage0 } from '../scenes/v8c-08-Stage0';

const len = (k: keyof typeof V8C_TIMING): number => {
  const t = V8C_TIMING[k];
  return t.end - t.start;
};

/**
 * v0.8 Core — 84s, hplan 본질 (Build Gate · WHETHER vs HOW · Evidence/Exclusions/COGS) 위주.
 * 사용자 narration script 충실 (Ethan 톤).
 */
export const HplanV8Core: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: colors.bg }}>
      <Sequence from={V8C_TIMING.hook.start} durationInFrames={len('hook')}>
        <V8CHook />
      </Sequence>
      <Sequence from={V8C_TIMING.question.start} durationInFrames={len('question')}>
        <V8CQuestion />
      </Sequence>
      <Sequence from={V8C_TIMING.solution.start} durationInFrames={len('solution')}>
        <V8CSolution />
      </Sequence>
      <Sequence from={V8C_TIMING.sixQuestions.start} durationInFrames={len('sixQuestions')}>
        <V8CSixQuestions />
      </Sequence>
      <Sequence from={V8C_TIMING.threeGates.start} durationInFrames={len('threeGates')}>
        <V8CThreeGates />
      </Sequence>
      <Sequence from={V8C_TIMING.verdict.start} durationInFrames={len('verdict')}>
        <V8CVerdict />
      </Sequence>
      <Sequence from={V8C_TIMING.whyMatters.start} durationInFrames={len('whyMatters')}>
        <V8CWhyMatters />
      </Sequence>
      <Sequence from={V8C_TIMING.stage0.start} durationInFrames={len('stage0')}>
        <V8CStage0 />
      </Sequence>
    </AbsoluteFill>
  );
};
