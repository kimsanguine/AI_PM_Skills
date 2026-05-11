import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';

interface Props {
  /** Frame the caption appears (relative to scene). */
  appearAt: number;
  /** Frame the caption fades out (relative to scene). */
  disappearAt: number;
  /** Korean line (primary, larger). */
  ko: string;
  /** English line (subtitle). */
  en?: string;
  /** Bottom offset in px. */
  bottom?: number;
}

/**
 * Bilingual caption rendered as an overlay near the bottom of the frame.
 * Korean line is primary (slightly larger); English is secondary.
 */
export const BilingualCaption: React.FC<Props> = ({
  appearAt,
  disappearAt,
  ko,
  en,
  bottom = 80,
}) => {
  const frame = useCurrentFrame();

  const enterProgress = spring({
    frame: frame - appearAt,
    fps: FPS,
    config: { mass: 1, damping: 200 },
  });
  const exitProgress = interpolate(
    frame,
    [disappearAt - 8, disappearAt],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );
  const opacity = Math.min(enterProgress, exitProgress);
  const translateY = interpolate(enterProgress, [0, 1], [12, 0]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: 'flex-end',
        alignItems: 'center',
        pointerEvents: 'none',
        opacity,
        transform: `translateY(${translateY}px)`,
      }}
    >
      <div
        style={{
          marginBottom: bottom,
          textAlign: 'center',
          maxWidth: '85%',
          padding: '16px 28px',
          backgroundColor: 'rgba(24, 24, 37, 0.78)',
          borderRadius: 12,
          backdropFilter: 'blur(4px)',
        }}
      >
        <div
          style={{
            fontFamily: fonts.display,
            fontSize: 28,
            fontWeight: 600,
            color: colors.text,
            lineHeight: 1.4,
          }}
        >
          {ko}
        </div>
        {en && (
          <div
            style={{
              fontFamily: fonts.display,
              fontSize: 16,
              color: colors.dim,
              marginTop: 6,
              lineHeight: 1.4,
            }}
          >
            {en}
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};
