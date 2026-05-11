import React from 'react';
import { useCurrentFrame } from 'remotion';
import { colors } from '../theme';

interface Props {
  color?: string;
  width?: number;
  height?: number;
}

/**
 * Blinking terminal cursor — 0.5s on / 0.5s off.
 */
export const BlinkingCursor: React.FC<Props> = ({
  color = colors.text,
  width = 12,
  height = 22,
}) => {
  const frame = useCurrentFrame();
  // 30fps → 15-frame period = 0.5s
  const visible = Math.floor(frame / 15) % 2 === 0;
  return (
    <span
      style={{
        display: 'inline-block',
        width,
        height,
        backgroundColor: color,
        opacity: visible ? 1 : 0,
        marginLeft: 2,
        verticalAlign: 'middle',
      }}
    />
  );
};
