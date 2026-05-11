import React from 'react';
import { Composition } from 'remotion';
import { HplanIntro16x9 } from './compositions/HplanIntro16x9';
import { HplanIntro1x1 } from './compositions/HplanIntro1x1';
import { HplanIntro9x16 } from './compositions/HplanIntro9x16';
import { FPS, TOTAL_FRAMES } from './theme';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="HplanIntro16x9"
        component={HplanIntro16x9}
        durationInFrames={TOTAL_FRAMES}
        fps={FPS}
        width={1920}
        height={1080}
      />
      <Composition
        id="HplanIntro1x1"
        component={HplanIntro1x1}
        durationInFrames={TOTAL_FRAMES}
        fps={FPS}
        width={1080}
        height={1080}
      />
      <Composition
        id="HplanIntro9x16"
        component={HplanIntro9x16}
        durationInFrames={TOTAL_FRAMES}
        fps={FPS}
        width={1080}
        height={1920}
      />
    </>
  );
};
