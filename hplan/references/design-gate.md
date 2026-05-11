# Design Gate

Use this reference before UI or frontend implementation. It is adapted from the hplan product design standard.

## Design Reference Stack

Use the following references as design inputs. Do not copy them blindly. Extract design DNA, then translate it into the product's own interface.

| Source | URL | Use for | Do not use for |
|---|---|---|---|
| 21st.dev | https://21st.dev/ | AI agent UI patterns, component ideas, marketplace-style interaction references | Replacing product strategy with prebuilt components |
| transitions.dev | https://transitions.dev/ | CSS/React transitions for meaningful state changes, onboarding motion, panel transitions | Decorative motion that slows core workflows |
| Refero Styles | https://lnkd.in/gPUfBdnw | Brand/URL-based design references, style DNA, DESIGN.md-style extraction | Copying another brand, palette, or layout |
| open-design | https://lnkd.in/gPpJq99W | Local design generation, image/slide ideation, CLI-assisted visual exploration | Treating generated visuals as final without QA |
| Montage Design System | https://lnkd.in/gmeam5u9 | Korean product-grade typography, component density, patterns, accessibility inspiration | Copying Wanted's brand identity |
| diagram-design | https://lnkd.in/gm6HhARd | Editorial diagrams in HTML/SVG, non-Mermaid product/process visuals | Decorative diagrams that do not clarify decisions |
| Font of Web | https://fontofweb.com/ | Typography and real-web font inspiration | Random font changes without hierarchy rules |
| Logo System | https://logosystem.co/ | Wordmark, symbol, and animated logo reference during brand exploration | Premature logo work before positioning is clear |
| UXSnaps | https://www.uxsnaps.com/ | Real app UX patterns, onboarding, paywall, settings, empty states, flows | Copying flows without adapting to this product's job |

When a URL has changed or the user asks for current examples, browse the web and cite the references used.

## Reference Application Workflow

Before UI implementation:

1. Pick 2-4 references from the stack based on the screen type.
2. Extract mood, information density, typography, color role, component pattern, state handling, and motion use.
3. Decide what to adopt, adapt, and reject.
4. Write the Design Guidelines output before code.
5. If implementing, verify desktop and mobile screenshots against the guidelines.

Recommended pairings:

- AI agent workspace: 21st.dev + Refero Styles + UXSnaps
- Dashboard or operational SaaS: Montage Design System + UXSnaps + Refero Styles
- Landing or positioning page: Refero Styles + Font of Web + Logo System
- Interactive workflow: 21st.dev + transitions.dev + UXSnaps
- Methodology or process explanation: diagram-design + Refero Styles

## Product-Specific DESIGN.md Pattern

For any serious app, produce or update a root-level `DESIGN.md` before implementation. This file is the agent-readable design system for future coding agents.

Minimum sections:

- Visual theme and atmosphere
- Color palette and semantic roles
- Typography roles
- Component styling rules
- Layout principles
- Depth/elevation rules
- Do / Do not
- Responsive behavior
- Motion and interaction
- Agent prompt guide for future UI generation
- Page-level design targets
- CSS token starter when useful

Treat this as a build artifact, not a moodboard.

## AI Product Design Principles

When the product uses AI to generate, classify, recommend, transform, or publish output:

- The primary object should be the interface. For media tools, the preview/output is the visual anchor, not decoration.
- AI confidence must be inspectable: show reason, evidence, confidence, fallback, risk note, or review requirement.
- Human override is a first-class action: expose editable fields for the parts that affect trust and quality.
- Usage is product UX: plan, remaining usage, limits, next reset, and blocked reasons must be visible before expensive actions.
- Never blur cost units in UI copy. Use the real unit: export, source import, analysis run, render, minute, seat, project, or resolved task.
- Policy-sensitive flows must expose user responsibility at the point of action, not only in legal pages.
- Speed must be visible when speed is part of the value proposition: show current step, ETA, completed artifacts, next artifact, and fallback action.
- Evidence should be one click away for generated claims, summaries, recommendations, proposals, decisions, or commitments.
- Primary outcome first: show the artifact the user needs immediately before secondary or slower artifacts.
- Consent is part of intake when data may leave the user's device, organization, or private environment.

## Required Outputs

- Product mood
- Screen hierarchy
- Visual principles
- Design tokens or palette direction
- Component rules
- State rules
- Mobile verification checklist
- Design risks
- References used and how each affected the design
- Product-specific `DESIGN.md` outline or update notes when implementation is likely

## Required Design Questions

Answer these before implementation:

- What should the product feel like?
- What should it not feel like?
- What is the first screen's point of view?
- Which user decision must be visually prioritized?
- What evidence or status must be legible?
- What should happen on mobile?
- Which design references were used?
- What was intentionally rejected from those references?
- What is the primary visual object or decision object?
- Which AI confidence, evidence, risk, and override states must be visible?
- Which usage, cost, plan, or policy states must be visible before action?
- Which latency/processing states must be visible?
- Which primary artifact should appear first, and which artifacts may continue in the background?

## Design Direction Template

```markdown
## Design Guidelines

### References Used
| Reference | What we borrow | What we reject |
|---|---|---|

### Product Mood
- Should feel like:
- Should not feel like:

### Screen Hierarchy
1.
2.
3.

### Visual Principles
- Product first, not decoration:
- Evidence/status legibility:
- Density:
- Trust and reviewability:
- AI confidence:
- Human override:
- Usage/cost visibility:
- Policy-sensitive moments:
- Speed/latency visibility:
- Evidence access:

### Components
- Buttons:
- Forms:
- Cards/tables:
- Charts:
- Primary output/preview:
- Usage/cost meter:
- Evidence/risk panel:
- Processing timeline:
- Consent/intake control:
- Modals/toasts:
- Empty/loading/error states:

### State Rules
- Active:
- Completed:
- Disabled:
- Warning:
- Blocked:
- Paid/locked:

### Mobile Verification
- First screen:
- Core workflow:
- Result screen:
- Pricing/CTA:

### DESIGN.md Update
- Sections to create/update:
- Tokens:
- Page targets:
```

## Do Not

- Do not start from a generic landing page when the user asked for an app, tool, dashboard, or product workflow.
- Do not use visible in-app text to explain the UI's design choices, visual style, or keyboard shortcuts unless the product itself needs that instruction.
- Do not use decorative gradients, blobs, mock glass, or oversized cards to compensate for weak product hierarchy.
- Do not copy a reference site's brand, exact palette, spacing, logo, or layout.
- Do not introduce a design system without mapping it to the product's actual states and workflows.
- Do not use motion from transitions.dev unless it clarifies state change, progression, or spatial relationship.
- Do not use diagrams unless they clarify a decision, workflow, architecture, or causal relationship.
- Do not choose fonts from Font of Web without defining display, heading, body, label, caption, and data-value roles.
- Do not design logos from Logo System before positioning and counter-position are stable.
- Do not hide paywalls, usage limits, blocked states, errors, review-required states, or COGS-sensitive actions.
- Do not add new routes, tabs, phases, or pricing surfaces without updating sitemap and user journey map.
- Do not ship desktop-only polish. Mobile overlap, overflow, and CTA visibility must be checked.
- Do not let AI-generated output skip evidence, confidence, risk, or override UI.
- Do not say a usage unit vaguely. Avoid "videos," "tasks," or "credits" when the actual paid unit is narrower.
- Do not present a loading spinner as the whole processing UX when the user is waiting on a meaningful business outcome.
- Do not make the slowest secondary artifact block the first useful artifact.
- Do not send private or policy-sensitive inputs to an external provider without a visible consent/control state.

## UI Quality Rules

- Make the core workflow the first usable experience, not a generic marketing page.
- Do not let decorative visuals compete with the user's decision.
- Use clear hierarchy for decision, score, next action, cost, or risk.
- Do not hide warnings or usage limits behind vague copy.
- For AI products, show review, override, confidence, or risk states where needed.
- For paid products, make usage boundaries and plan limits explicit.
- Text must not overflow cards, buttons, tabs, or mobile layouts.

## hplan-Specific Design Bar

When designing hplan itself, check:

- `docs/design.md`
- `docs/sitemap.md`
- `docs/user-journey-map.md`

Any new route, tab, phase, export, diagnosis step, pricing surface, or service loop must update these documents first.

## Design Decision

If design direction is missing, return `HOLD_DESIGN_GATE` and ask for or produce the missing design guideline before implementation.
