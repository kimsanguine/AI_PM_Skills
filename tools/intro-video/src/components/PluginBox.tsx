import React from 'react';
import { useCurrentFrame, spring, interpolate } from 'remotion';
import { fonts, FPS } from '../theme';

interface Props {
  /** Frame at which this box enters (relative to scene). */
  appearAt: number;
  /** Plugin label. */
  name: string;
  /** Lifecycle phase label below the name. */
  phase: string;
  /** "7 skills" sub-label. */
  count: string;
  /** Hex color for the box background. */
  color: string;
  /** Subtle border color (slightly darker). */
  borderColor?: string;
  /** Mark as flagship with ⭐. */
  flagship?: boolean;
  /** Box dimensions. */
  width?: number;
  height?: number;
}

/**
 * Single lifecycle stage box. Animates in with a spring scale + fade.
 */
export const PluginBox: React.FC<Props> = ({
  appearAt,
  name,
  phase,
  count,
  color,
  borderColor,
  flagship = false,
  width = 180,
  height = 130,
}) => {
  const frame = useCurrentFrame();
  const scale = spring({
    frame: frame - appearAt,
    fps: FPS,
    config: { mass: 0.6, damping: 12, stiffness: 220 },
    from: 0.5,
    to: 1,
  });
  const opacity = interpolate(frame, [appearAt, appearAt + 10], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        width,
        height,
        backgroundColor: color,
        border: borderColor ? `2px solid ${borderColor}` : 'none',
        borderRadius: 14,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 4,
        opacity,
        transform: `scale(${scale})`,
        boxShadow: '0 10px 28px rgba(0, 0, 0, 0.35)',
        fontFamily: fonts.display,
      }}
    >
      <div
        style={{
          fontSize: 22,
          fontWeight: 700,
          color: 'white',
        }}
      >
        {name} {flagship && '⭐'}
      </div>
      <div
        style={{
          fontSize: 14,
          color: 'rgba(255, 255, 255, 0.88)',
        }}
      >
        {phase}
      </div>
      <div
        style={{
          fontSize: 13,
          color: 'rgba(255, 255, 255, 0.74)',
          marginTop: 4,
        }}
      >
        {count}
      </div>
    </div>
  );
};
