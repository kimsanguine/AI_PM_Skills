import React from 'react';
import { AbsoluteFill, Sequence } from 'remotion';
import { V8CT_TIMING, colors } from '../theme';
import { V8CHook } from '../scenes/v8c-01-Hook';
import { V8CQuestion } from '../scenes/v8c-02-Question';
import { V8CSolution } from '../scenes/v8c-03-Solution';
import { V8CSixQuestions } from '../scenes/v8c-04-SixQuestions';
import { V8CThreeGates } from '../scenes/v8c-05-ThreeGates';
import { V8CVerdict } from '../scenes/v8c-06-Verdict';
import { V8CTTrackGuardrail } from '../scenes/v8ct-07b-TrackGuardrail';
import { V8CWhyMatters } from '../scenes/v8c-07-WhyMatters';
import { V8CStage0 } from '../scenes/v8c-08-Stage0';

const len = (k: keyof typeof V8CT_TIMING): number => {
  const t = V8CT_TIMING[k];
  return t.end - t.start;
};

/**
 * v0.8 Core + Track — 99s.
 * C 안 8 scene + TrackGuardrail (만드는 중 가드레일) 1 scene 추가.
 * Build Gate (만들기 전) + Track (만드는 중) = 2-layer 안전망.
 */
export const HplanV8CoreTrack: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: colors.bg }}>
      <Sequence from={V8CT_TIMING.hook.start} durationInFrames={len('hook')}>
        <V8CHook />
      </Sequence>
      <Sequence from={V8CT_TIMING.question.start} durationInFrames={len('question')}>
        <V8CQuestion />
      </Sequence>
      <Sequence from={V8CT_TIMING.solution.start} durationInFrames={len('solution')}>
        <V8CSolution />
      </Sequence>
      <Sequence from={V8CT_TIMING.sixQuestions.start} durationInFrames={len('sixQuestions')}>
        <V8CSixQuestions />
      </Sequence>
      <Sequence from={V8CT_TIMING.threeGates.start} durationInFrames={len('threeGates')}>
        <V8CThreeGates />
      </Sequence>
      <Sequence from={V8CT_TIMING.verdict.start} durationInFrames={len('verdict')}>
        <V8CVerdict />
      </Sequence>
      <Sequence from={V8CT_TIMING.trackGuardrail.start} durationInFrames={len('trackGuardrail')}>
        <V8CTTrackGuardrail />
      </Sequence>
      <Sequence from={V8CT_TIMING.whyMatters.start} durationInFrames={len('whyMatters')}>
        <V8CWhyMatters />
      </Sequence>
      <Sequence from={V8CT_TIMING.stage0.start} durationInFrames={len('stage0')}>
        <V8CStage0 />
      </Sequence>
    </AbsoluteFill>
  );
};
