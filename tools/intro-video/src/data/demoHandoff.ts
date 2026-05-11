import { DemoLine } from './demoEvidence';

// Scene runs 270 frames (9s at 30fps).
// Narration:
//   [0-45]   "게이트를 통과한 brief는,"
//   [45-135] "Spec-Kit, Kiro, GStack, Claude Code"
//   [135-150] short pause
//   [150-225] "어떤 코딩 도구든, 한 번에 export됩니다"

export const DEMO_HANDOFF_LINES: DemoLine[] = [
  {
    appearAt: 25,
    prompt: '❯',
    text: '/hplan-handoff brief.json --target all',
    variant: 'cmd',
  },
  {
    appearAt: 70,
    text: '✓ specs/001-product/{spec,plan,tasks}.md       → Spec-Kit',
    variant: 'ok',
  },
  {
    appearAt: 105,
    text: '✓ .kiro/specs/product/{requirements,design,tasks}.md → Kiro',
    variant: 'ok',
  },
  {
    appearAt: 140,
    text: '✓ office-hours-brief.md                         → GStack',
    variant: 'ok',
  },
  {
    appearAt: 175,
    text: '✓ AGENTS.md + CLAUDE.md                          → Claude Code',
    variant: 'ok',
  },
];
