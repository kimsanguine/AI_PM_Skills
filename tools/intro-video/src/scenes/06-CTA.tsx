import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, FPS } from '../theme';
import { TypewriterText } from '../components/TypewriterText';
import { BlinkingCursor } from '../components/BlinkingCursor';

/**
 * Scene 6 — CTA (63-70s, 210 frames).
 * Install command types out → URL + tagline → final logo + URL.
 */
export const SceneCTA: React.FC = () => {
  const frame = useCurrentFrame();
  const fadeIn = interpolate(frame, [0, 18], [0, 1], { extrapolateRight: 'clamp' });

  // Install command types frames 15-75 (~2s)
  const installStart = 15;
  const installDuration = 60;

  // Tagline appears at frame 100
  const taglineOpacity = interpolate(frame, [100, 130], [0, 1], { extrapolateRight: 'clamp' });
  const taglineScale = spring({
    frame: frame - 100,
    fps: FPS,
    config: { mass: 0.7, damping: 12, stiffness: 200 },
    from: 0.85,
    to: 1,
  });

  // URL at frame 145
  const urlOpacity = interpolate(frame, [145, 175], [0, 1], { extrapolateRight: 'clamp' });

  // Star nudge at frame 175
  const starOpacity = interpolate(frame, [175, 195], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.bg,
        fontFamily: fonts.display,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 60,
        opacity: fadeIn,
      }}
    >
      {/* Install command (typing effect) */}
      <div
        style={{
          fontSize: 28,
          fontFamily: fonts.mono,
          color: colors.text,
          marginBottom: 56,
        }}
      >
        <span style={{ color: colors.prompt }}>❯</span>{' '}
        <TypewriterText
          text="/plugin marketplace add kimsanguine/hplan"
          startFrame={installStart}
          durationFrames={installDuration}
          fontSize={28}
          color={colors.text}
        />
        {frame > installStart + installDuration && <BlinkingCursor color={colors.text} />}
      </div>

      {/* Main tagline */}
      <div
        style={{
          opacity: taglineOpacity,
          transform: `scale(${taglineScale})`,
          textAlign: 'center',
        }}
      >
        <div
          style={{
            fontSize: 64,
            fontWeight: 900,
            color: colors.ok,
            letterSpacing: '-0.02em',
            lineHeight: 1.15,
          }}
        >
          30분 안에, 6개월을 막다
        </div>
        <div
          style={{
            fontSize: 22,
            color: colors.dim,
            marginTop: 16,
            fontWeight: 500,
          }}
        >
          30 minutes to save 6 months.
        </div>
      </div>

      {/* URL */}
      <div
        style={{
          marginTop: 56,
          fontSize: 28,
          fontFamily: fonts.mono,
          color: colors.prompt,
          opacity: urlOpacity,
        }}
      >
        github.com/kimsanguine/hplan
      </div>

      {/* Star nudge */}
      <div
        style={{
          position: 'absolute',
          bottom: 60,
          fontSize: 18,
          color: colors.veryDim,
          opacity: starOpacity,
          fontWeight: 500,
        }}
      >
        ⭐ Star to remember when you need it
      </div>
    </AbsoluteFill>
  );
};
