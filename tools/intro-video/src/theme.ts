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
 * Total video length is 84s at 30fps = 2520 frames.
 * v0.6.1: extended from 70s to 84s after first Gemini TTS render produced
 * narration longer than initial budget. Sped narration 1.2x via ffmpeg atempo
 * and reset scene durations to fit each clip + small visual buffer.
 *
 * Each scene exposes [startFrame, endFrame] for absolute placement.
 */
export const SCENE_TIMING = {
  hook: { start: 0, end: 180 },             // 0-6s   (narration 5.0s + 1s buffer)
  problem: { start: 180, end: 750 },        // 6-25s  (narration 17.8s + 1.2s buffer)
  solution: { start: 750, end: 990 },       // 25-33s (narration 6.4s + 1.6s buffer)
  demoEvidence: { start: 990, end: 1260 },  // 33-42s (narration 7.1s + 1.9s buffer)
  demoCogs: { start: 1260, end: 1680 },     // 42-56s (narration 12.3s + 1.7s buffer)
  demoHandoff: { start: 1680, end: 1950 },  // 56-65s (narration 8.3s + 0.7s buffer)
  lifecycle: { start: 1950, end: 2310 },    // 65-77s (narration 11.2s + 0.8s buffer)
  cta: { start: 2310, end: 2520 },          // 77-84s (narration 5.0s + 2s buffer)
} as const;

export const FPS = 30;
export const TOTAL_FRAMES = 2520;
