import React from 'react';
import { HplanIntro16x9 } from './HplanIntro16x9';

/**
 * 1080×1080 square — X / LinkedIn feed.
 * Reuses the 16:9 composition but renders into a square canvas with letterboxing.
 * Compositions in Root.tsx set the canvas size; this component just wraps.
 */
export const HplanIntro1x1: React.FC = () => {
  return <HplanIntro16x9 />;
};
