import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';
import { fonts } from '../theme';

interface Props {
  text: string;
  /** Frame at which typing starts (relative to the scene's own frame counter). */
  startFrame: number;
  /** Total frames the typing animation takes. */
  durationFrames: number;
  /** Show a blinking cursor at the end of the typed text. */
  showCursor?: boolean;
  fontSize?: number;
  color?: string;
  fontFamily?: string;
  style?: React.CSSProperties;
}

/**
 * Reveals text character by character between startFrame and startFrame+durationFrames.
 * After the animation completes, the full text is shown.
 */
export const TypewriterText: React.FC<Props> = ({
  text,
  startFrame,
  durationFrames,
  showCursor = false,
  fontSize,
  color,
  fontFamily = fonts.mono,
  style,
}) => {
  const frame = useCurrentFrame();
  const progress = interpolate(
    frame,
    [startFrame, startFrame + durationFrames],
    [0, text.length],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );
  const visibleText = text.slice(0, Math.floor(progress));
  const typingDone = progress >= text.length;

  return (
    <span style={{ fontFamily, fontSize, color, whiteSpace: 'pre-wrap', ...style }}>
      {visibleText}
      {showCursor && typingDone && (
        <span style={{ animation: 'blink 1s step-end infinite' }}>▌</span>
      )}
    </span>
  );
};
