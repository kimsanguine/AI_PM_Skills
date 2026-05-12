import React from 'react';
import { AbsoluteFill, Sequence, Audio, staticFile } from 'remotion';
import { SCENE_TIMING } from '../theme';
import { SceneHook } from '../scenes/01-Hook';
import { SceneProblem } from '../scenes/02-Problem';
import { SceneSolution } from '../scenes/03-Solution';
import { SceneDemoEvidence } from '../scenes/04a-DemoEvidence';
import { SceneDemoCogs } from '../scenes/04b-DemoCogs';
import { SceneDemoHandoff } from '../scenes/04c-DemoHandoff';
import { SceneLifecycle } from '../scenes/05-Lifecycle';
import { SceneCTA } from '../scenes/06-CTA';

const len = (k: keyof typeof SCENE_TIMING): number => {
  const t = SCENE_TIMING[k];
  return t.end - t.start;
};

/**
 * Main 16:9 composition — primary README embed.
 */
export const HplanIntro16x9: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: '#1e1e2e' }}>
      {/* Scene sequence */}
      <Sequence from={SCENE_TIMING.hook.start} durationInFrames={len('hook')}>
        <SceneHook />
      </Sequence>
      <Sequence from={SCENE_TIMING.problem.start} durationInFrames={len('problem')}>
        <SceneProblem />
      </Sequence>
      <Sequence from={SCENE_TIMING.solution.start} durationInFrames={len('solution')}>
        <SceneSolution />
      </Sequence>
      <Sequence
        from={SCENE_TIMING.demoEvidence.start}
        durationInFrames={len('demoEvidence')}
      >
        <SceneDemoEvidence />
      </Sequence>
      <Sequence from={SCENE_TIMING.demoCogs.start} durationInFrames={len('demoCogs')}>
        <SceneDemoCogs />
      </Sequence>
      <Sequence
        from={SCENE_TIMING.demoHandoff.start}
        durationInFrames={len('demoHandoff')}
      >
        <SceneDemoHandoff />
      </Sequence>
      <Sequence from={SCENE_TIMING.lifecycle.start} durationInFrames={len('lifecycle')}>
        <SceneLifecycle />
      </Sequence>
      <Sequence from={SCENE_TIMING.cta.start} durationInFrames={len('cta')}>
        <SceneCTA />
      </Sequence>

      {/* Narration audio — generated via scripts/generate_narration.py (Gemini TTS, Charon voice, 1.2x atempo) */}
      <Sequence from={SCENE_TIMING.hook.start}>
        <Audio src={staticFile('audio/narration/01-hook.mp3')} />
      </Sequence>
      <Sequence from={SCENE_TIMING.problem.start}>
        <Audio src={staticFile('audio/narration/02-problem.mp3')} />
      </Sequence>
      <Sequence from={SCENE_TIMING.solution.start}>
        <Audio src={staticFile('audio/narration/03-solution.mp3')} />
      </Sequence>
      <Sequence from={SCENE_TIMING.demoEvidence.start}>
        <Audio src={staticFile('audio/narration/04a-evidence.mp3')} />
      </Sequence>
      <Sequence from={SCENE_TIMING.demoCogs.start}>
        <Audio src={staticFile('audio/narration/04b-cogs.mp3')} />
      </Sequence>
      <Sequence from={SCENE_TIMING.demoHandoff.start}>
        <Audio src={staticFile('audio/narration/04c-handoff.mp3')} />
      </Sequence>
      <Sequence from={SCENE_TIMING.lifecycle.start}>
        <Audio src={staticFile('audio/narration/05-lifecycle.mp3')} />
      </Sequence>
      <Sequence from={SCENE_TIMING.cta.start}>
        <Audio src={staticFile('audio/narration/06-cta.mp3')} />
      </Sequence>
      {/* BGM — ffmpeg-synthesized A-minor ambient pad, mixed at -18dB under narration */}
      <Audio src={staticFile('audio/bgm.mp3')} volume={0.12} />
    </AbsoluteFill>
  );
};
