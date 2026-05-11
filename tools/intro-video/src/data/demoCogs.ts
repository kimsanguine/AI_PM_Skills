import { DemoLine } from './demoEvidence';

// Scene runs 300 frames (10s at 30fps) — the hero demo.
// Narration:
//   [0-45]   "가격을 정하기 전에"
//   [45-135] "p50, p90 마진을 실제 숫자로 계산합니다"
//   [135-180] pause / numbers reveal
//   [180-240] "무료 사용자 abuse까지 포함하면 음수"
//   [240-285] "이 자리에서, 멈춥니다"

export const DEMO_COGS_LINES: DemoLine[] = [
  {
    appearAt: 25,
    prompt: '❯',
    text: '/hplan-cogs --model sonnet --tokens 8000 --calls 120 --arpu 19',
    variant: 'cmd',
  },
  {
    appearAt: 75,
    text: '  per-call cost p50:       $0.054',
    variant: 'output',
  },
  {
    appearAt: 105,
    text: '  monthly COGS p50:        $6.63      margin 64%',
    variant: 'output',
  },
  {
    appearAt: 135,
    text: '  monthly COGS p90:        $13.90     margin 25%  ⚠',
    variant: 'warn',
  },
  {
    appearAt: 180,
    text: '  with free-user abuse:                          −1961%  ✗',
    variant: 'bad',
  },
  {
    appearAt: 225,
    prompt: '→',
    text: '결정: RED 🚫',
    variant: 'bad',
  },
];
