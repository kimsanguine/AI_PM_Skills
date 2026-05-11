import React from 'react';
import { colors, fonts } from '../theme';

interface Props {
  title?: string;
  width?: number | string;
  height?: number | string;
  children: React.ReactNode;
}

/**
 * macOS-style terminal frame with title bar + 3 traffic-light dots.
 */
export const Terminal: React.FC<Props> = ({
  title = 'hplan — Product Build Gate Demo',
  width = '92%',
  height = 'auto',
  children,
}) => {
  return (
    <div
      style={{
        width,
        height,
        backgroundColor: colors.bg,
        borderRadius: 16,
        boxShadow: '0 20px 60px rgba(0, 0, 0, 0.5)',
        overflow: 'hidden',
        fontFamily: fonts.mono,
        color: colors.text,
      }}
    >
      {/* Title bar */}
      <div
        style={{
          height: 36,
          backgroundColor: colors.titleBar,
          display: 'flex',
          alignItems: 'center',
          padding: '0 16px',
          gap: 8,
          position: 'relative',
        }}
      >
        <div style={dotStyle(colors.dotRed)} />
        <div style={dotStyle(colors.dotYellow)} />
        <div style={dotStyle(colors.dotGreen)} />
        <div
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            textAlign: 'center',
            fontSize: 14,
            color: colors.text,
            pointerEvents: 'none',
          }}
        >
          {title}
        </div>
      </div>
      {/* Body */}
      <div style={{ padding: '32px 36px', minHeight: 200 }}>{children}</div>
    </div>
  );
};

const dotStyle = (color: string): React.CSSProperties => ({
  width: 12,
  height: 12,
  borderRadius: '50%',
  backgroundColor: color,
});
