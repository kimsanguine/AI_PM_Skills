/**
 * Catppuccin Mocha — visual theme for hplan intro video.
 * Matches the existing docs/images/demo-terminal.svg palette so the video
 * and the static README SVG feel like the same product.
 */

export const colors = {
  bg: '#1e1e2e',
  titleBar: '#313244',
  surface: '#181825',
  text: '#cdd6f4',
  dim: '#a6adc8',
  veryDim: '#6c7086',
  prompt: '#89b4fa',
  skillTag: '#cba6f7',
  arrow: '#f9e2af',
  ok: '#a6e3a1',
  warn: '#f9e2af',
  bad: '#f38ba8',
  dotRed: '#f38ba8',
  dotYellow: '#f9e2af',
  dotGreen: '#a6e3a1',
  // hplan brand red
  hplanRed: '#dc2626',
  hplanRedSoft: '#f87171',
};

export const fonts = {
  mono: "'SF Mono', 'JetBrains Mono', 'Fira Code', 'Menlo', monospace",
  display: "'Inter', 'SF Pro Display', -apple-system, system-ui, sans-serif",
};

export const typography = {
  hookSize: 64,
  titleSize: 48,
  bodySize: 24,
  smallSize: 18,
  captionSize: 16,
  terminalSize: 22,
  terminalSmall: 18,
};

/**
 * Total video length is 70s at 30fps = 2100 frames.
 * Each scene exposes [startFrame, endFrame] for absolute placement.
 */
export const SCENE_TIMING = {
  hook: { start: 0, end: 180 },          // 0-6s
  problem: { start: 180, end: 600 },     // 6-20s
  solution: { start: 600, end: 840 },    // 20-28s
  demoEvidence: { start: 840, end: 1080 }, // 28-36s
  demoCogs: { start: 1080, end: 1380 },  // 36-46s
  demoHandoff: { start: 1380, end: 1650 }, // 46-55s
  lifecycle: { start: 1650, end: 1890 }, // 55-63s
  cta: { start: 1890, end: 2100 },       // 63-70s
} as const;

export const FPS = 30;
export const TOTAL_FRAMES = 2100;
