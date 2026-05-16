import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import { colors, fonts, typography, FPS } from '../theme';

const STAGES = [
  { name: 'Gate', plugin: 'hplan', count: 7, color: 'hplanRed' as const },
  { name: 'Discover', plugin: 'discover', count: 6, color: 'skillTag' as const },
  { name: 'Architect', plugin: 'architect', count: 7, color: 'skillTag' as const },
  { name: 'Deliver', plugin: 'deliver', count: 15, color: 'skillTag' as const },
  { name: 'Measure', plugin: 'measure', count: 8, color: 'skillTag' as const },
  { name: 'Learn', plugin: 'learn', count: 3, color: 'skillTag' as const },
  { name: 'Operate', plugin: 'operate', count: 4, color: 'skillTag' as const },
  { name: 'Track', plugin: 'track', count: 7, color: 'trackBlue' as const, isV8: true },
  { name: 'Craft', plugin: 'craft', count: 4, color: 'craftRose' as const, isV8: true },
];

/**
 * v0.8 Editorial — Scene 3 — Lifecycle (25-50s, 750 frames).
 * 9-stage diagram + 마지막 2 stage (track + craft) spotlight.
 */
export const V8ELifecycle: React.FC = () => {
  const frame = useCurrentFrame();

  const titleOpacity = interpolate(frame, [10, 40], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const spotlightOpacity = interpolate(frame, [450, 510], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const fadeOut = interpolate(frame, [730, 750], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.bg,
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: fonts.display,
        opacity: fadeOut,
      }}
    >
      <div
        style={{
          fontSize: typography.titleSize,
          fontWeight: 300,
          color: colors.text,
          opacity: titleOpacity,
          letterSpacing: '-0.02em',
          marginBottom: 56,
        }}
      >
        9 stages · build → ship
      </div>

      <div
        style={{
          display: 'flex',
          gap: 14,
          alignItems: 'center',
          flexWrap: 'wrap',
          justifyContent: 'center',
          maxWidth: 1700,
        }}
      >
        {STAGES.map((s, i) => {
          const appear = 80 + i * 35;
          const sp = spring({
            frame: frame - appear,
            fps: FPS,
            config: { mass: 0.5, damping: 14 },
            from: 0,
            to: 1,
          });
          const isSpotlight = s.isV8 && frame > 450;
          const glow = isSpotlight ? `0 0 24px ${colors[s.color]}` : 'none';
          const scale = isSpotlight
            ? interpolate(frame, [450, 510], [1, 1.12], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              })
            : 1;
          return (
            <React.Fragment key={s.plugin}>
              <div
                style={{
                  opacity: sp,
                  transform: `scale(${sp * scale})`,
                  padding: '14px 22px',
                  border: `2px solid ${colors[s.color]}`,
                  borderRadius: 8,
                  boxShadow: glow,
                  backgroundColor: isSpotlight ? `${colors[s.color]}22` : 'transparent',
                  textAlign: 'center',
                  minWidth: 130,
                  transition: 'background-color 0.3s',
                }}
              >
                <div
                  style={{
                    fontSize: 22,
                    fontWeight: 600,
                    color: colors[s.color],
                  }}
                >
                  {s.name}
                  {s.isV8 && (
                    <span
                      style={{
                        marginLeft: 6,
                        fontSize: 14,
                        color: colors.warn,
                      }}
                    >
                      ★
                    </span>
                  )}
                </div>
                <div
                  style={{
                    fontSize: 14,
                    color: colors.dim,
                    fontFamily: fonts.mono,
                    marginTop: 4,
                  }}
                >
                  {s.plugin} · {s.count} skills
                </div>
              </div>
              {i < STAGES.length - 1 && (
                <span
                  style={{
                    color: colors.veryDim,
                    fontSize: 24,
                    opacity: sp,
                  }}
                >
                  →
                </span>
              )}
            </React.Fragment>
          );
        })}
      </div>

      <div
        style={{
          marginTop: 56,
          fontSize: typography.bodySize,
          color: colors.dim,
          opacity: spotlightOpacity,
          letterSpacing: '-0.01em',
        }}
      >
        v0.8 추가 →{' '}
        <span style={{ color: colors.trackBlue, fontWeight: 600 }}>track</span>{' '}
        ·{' '}
        <span style={{ color: colors.craftRose, fontWeight: 600 }}>craft</span>{' '}
        가 build → ship 사이 빈 공간을 닫습니다
      </div>
    </AbsoluteFill>
  );
};
