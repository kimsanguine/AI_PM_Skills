import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';
import { colors, fonts } from '../theme';

interface Props {
  /** Frame at which the line fades in. */
  appearAt: number;
  /** Optional prompt char (e.g., '❯'). If set, line is treated as a command. */
  prompt?: string;
  /** Output color class. */
  variant?: 'cmd' | 'output' | 'ok' | 'warn' | 'bad' | 'dim' | 'skillTag' | 'arrow';
  fontSize?: number;
  children: React.ReactNode;
  style?: React.CSSProperties;
}

const variantColor = (variant: NonNullable<Props['variant']>): string => {
  switch (variant) {
    case 'cmd':
      return colors.text;
    case 'output':
      return colors.dim;
    case 'ok':
      return colors.ok;
    case 'warn':
      return colors.warn;
    case 'bad':
      return colors.bad;
    case 'dim':
      return colors.veryDim;
    case 'skillTag':
      return colors.skillTag;
    case 'arrow':
      return colors.arrow;
  }
};

/**
 * Single terminal output line. Fades in over 6 frames starting at appearAt.
 */
export const TerminalLine: React.FC<Props> = ({
  appearAt,
  prompt,
  variant = 'output',
  fontSize = 22,
  children,
  style,
}) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [appearAt, appearAt + 6], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const translateY = interpolate(frame, [appearAt, appearAt + 8], [4, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        opacity,
        transform: `translateY(${translateY}px)`,
        fontFamily: fonts.mono,
        fontSize,
        lineHeight: 1.55,
        color: variantColor(variant),
        whiteSpace: 'pre-wrap',
        ...style,
      }}
    >
      {prompt && (
        <span style={{ color: colors.prompt, marginRight: 12 }}>{prompt}</span>
      )}
      {children}
    </div>
  );
};
