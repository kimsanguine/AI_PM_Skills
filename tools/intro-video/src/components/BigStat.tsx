import React from 'react';
import { useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';

interface Props {
  /** Frame at which the count starts. */
  appearAt: number;
  /** Duration (frames) of the count-up animation. */
  durationFrames?: number;
  /** Target number. */
  target: number;
  /** Label below the number (e.g., "skills"). */
  label: string;
  /** Optional suffix appended to the number (e.g., "+"). */
  suffix?: string;
  fontSize?: number;
  color?: string;
}

/**
 * Big number that counts up from 0 to `target` over `durationFrames`.
 */
export const BigStat: React.FC<Props> = ({
  appearAt,
  durationFrames = 18,
  target,
  label,
  suffix = '',
  fontSize = 96,
  color = colors.text,
}) => {
  const frame = useCurrentFrame();
  const current = Math.round(
    interpolate(frame, [appearAt, appearAt + durationFrames], [0, target], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
    })
  );
  const scale = spring({
    frame: frame - appearAt,
    fps: FPS,
    config: { mass: 0.6, damping: 12, stiffness: 220 },
  });

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        transform: `scale(${scale})`,
        fontFamily: fonts.display,
      }}
    >
      <div
        style={{
          fontSize,
          fontWeight: 800,
          color,
          lineHeight: 1,
          fontFamily: fonts.mono,
        }}
      >
        {current}
        {suffix}
      </div>
      <div
        style={{
          fontSize: fontSize * 0.22,
          fontWeight: 500,
          color: colors.dim,
          marginTop: 8,
          letterSpacing: 1,
          textTransform: 'uppercase',
        }}
      >
        {label}
      </div>
    </div>
  );
};
