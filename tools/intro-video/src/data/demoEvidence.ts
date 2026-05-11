/**
 * Demo 1 — Evidence Gate terminal lines.
 * Each line includes the absolute frame at which it should appear (relative to scene start).
 */
export interface DemoLine {
  appearAt: number; // frames from scene start
  prompt?: string;
  text: string;
  variant: 'cmd' | 'output' | 'ok' | 'warn' | 'bad' | 'dim' | 'skillTag' | 'arrow';
}

// Scene runs 240 frames (8s at 30fps).
// Narration timing roughly:
//   [0-45]  "PRD 쓰기 전에 hplan은 이미 점유된 영역인지 자동으로 확인합니다"
//   [45-180] terminal animation
//   [180-225] "결정: hold"
//   [225-240] hold mark stays

export const DEMO_EVIDENCE_LINES: DemoLine[] = [
  {
    appearAt: 30,
    prompt: '❯',
    text: '/hplan-evidence "AI 마케팅 카피 도구"',
    variant: 'cmd',
  },
  {
    appearAt: 60,
    prompt: '→',
    text: 'exclusions check ... COLLISION (overlap 0.42)',
    variant: 'output',
  },
  {
    appearAt: 90,
    text: '   ↳ "기존 incumbent가 이미 점유"',
    variant: 'dim',
  },
  {
    appearAt: 115,
    text: '   ↳ reopen_trigger: UNMET',
    variant: 'dim',
  },
  {
    appearAt: 150,
    prompt: '→',
    text: '결정: hold ✋',
    variant: 'bad',
  },
];
