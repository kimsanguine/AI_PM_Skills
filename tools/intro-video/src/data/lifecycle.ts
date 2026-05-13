/**
 * 7 plugins in lifecycle order — used by Scene 5.
 * v0.7: operate plugin added; deliver count updated to 15.
 */
import { colors } from '../theme';

export interface LifecycleStage {
  name: string;
  phase: string;
  count: string;
  color: string;
  borderColor?: string;
  flagship?: boolean;
}

export const LIFECYCLE: LifecycleStage[] = [
  {
    name: 'hplan',
    phase: 'Gate',
    count: '7 skills',
    color: colors.hplanRedSoft,
    borderColor: colors.hplanRed,
    flagship: true,
  },
  {
    name: 'discover',
    phase: 'Discovery',
    count: '6 skills',
    color: '#6366f1',
  },
  {
    name: 'architect',
    phase: 'Architecture',
    count: '7 skills',
    color: '#8b5cf6',
  },
  {
    name: 'deliver',
    phase: 'Delivery',
    count: '15 skills',
    color: '#f59e0b',
  },
  {
    name: 'measure',
    phase: 'Measurement',
    count: '8 skills',
    color: '#10b981',
  },
  {
    name: 'learn',
    phase: 'Learning',
    count: '3 skills',
    color: '#ec4899',
  },
  {
    name: 'operate',
    phase: 'Operations',
    count: '4 skills',
    color: '#0ea5e9',
  },
];
