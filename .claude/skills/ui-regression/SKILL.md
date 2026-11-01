---
name: ui-regression
description: "Validate responsive layouts, interactions and accessibility against existing UI using grounded screenshots and interaction tests."
user-invocable: true
---
# Ui Regression — App Studio

This workflow also applies to applications outside Game Studios. It must operate on the user's actual application workspace, **not** on a generic Game Studios template. Read `docs/app-studio/README.md`, the matching technology profile(s), and relevant role files in `.claude/agents/`.

**Specialists:** ux-designer, ui-programmer, accessibility-specialist, e2e-automation-engineer (role profiles; actual independent agent execution requires compatible orchestration).

## Sequence
1. Identify approved existing design baseline and exact viewport breakpoints; don't redesign UI while measuring regression.
2. Capture *real* before screenshots when available, including mobile and desktop, and list visible critical controls and routes.
3. Implement or run Playwright/desktop/device interaction assertions; check keyboard/focus, contrast, overflow, text zoom, errors and long labels.
4. Compare after screenshots and interactions; distinguish harmless pixel differences from broken functional state. Inspect console/runtime errors.
5. Summarize observable changes, attach real artifacts and flag unverifiable manual accessibility/device steps as NOT RUN.

## Evidence and acceptance
- **Done when:** Viewport matrix, screenshot or trace references, interaction PASS/FAIL and unresolved manual checks.
- Report source revision and branch, tests executed with exit codes, environment/device/browser, artifacts, findings and gaps.
- Every item must have a verdict: **PASS**, **FAIL**, or **NOT RUN**. Do not equate a static read, mock test, unit check, headless boot or screenshot with full end-to-end acceptance.
- Protect personal data, secrets and paid/external side effects. Never invent API results, screenshot comparisons, or task completion.
- Observe project-specific `AGENTS.md`, `CLAUDE.md`, package scripts, contracts and user approvals. These skill files do not grant permissions.
- New source code or migrations require an explicitly authorized change scope; request approval for material production changes. Commits/PRs are not deployments.
- If the target repository lacks the studio structure, do not copy `project.yaml` or game-specific production folders into it. Put tests and evidence where that repository already expects them.
