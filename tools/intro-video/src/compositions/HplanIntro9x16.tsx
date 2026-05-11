import React from 'react';
import { HplanIntro16x9 } from './HplanIntro16x9';

/**
 * 1080×1920 vertical — Shorts / Reels / TikTok.
 * Reuses the 16:9 composition; canvas size is set in Root.tsx.
 */
export const HplanIntro9x16: React.FC = () => {
  return <HplanIntro16x9 />;
};
