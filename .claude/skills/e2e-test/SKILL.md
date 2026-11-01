---
name: e2e-test
description: "Exercise complete user journeys across UI/API/auth roles with deterministic data and reproducible Playwright or device evidence."
user-invocable: true
---
# E2e Test — App Studio

This workflow also applies to applications outside Game Studios. It must operate on the user's actual application workspace, **not** on a generic Game Studios template. Read `docs/app-studio/README.md`, the matching technology profile(s), and relevant role files in `.claude/agents/`.

**Specialists:** e2e-automation-engineer, qa-lead, ux-designer, integration-engineer (role profiles; actual independent agent execution requires compatible orchestration).

## Sequence
1. Define user journey, actor identities, locale/device matrix, staging URL and permitted test data. Confirm no live production mutations are needed.
2. Set up isolated fixtures and cleanup. Include success, bad input, unauthorized actor, timeout/retry, and duplicate submission cases.
3. Execute browser/API/device tests with current toolchain; capture trace/screenshot/video where supported, not from guessed visuals.
4. Correlate UI assertions with backend state; verify any external notifications only on authorized test accounts.
5. Publish explicit PASS/FAIL/NOT RUN evidence with scenario IDs, commands, environment, artifacts and cleanup confirmation.

## Evidence and acceptance
- **Done when:** A reliable test suite and a concise acceptance report separating backend, UI, device and external-service validation.
- Report source revision and branch, tests executed with exit codes, environment/device/browser, artifacts, findings and gaps.
- Every item must have a verdict: **PASS**, **FAIL**, or **NOT RUN**. Do not equate a static read, mock test, unit check, headless boot or screenshot with full end-to-end acceptance.
- Protect personal data, secrets and paid/external side effects. Never invent API results, screenshot comparisons, or task completion.
- Observe project-specific `AGENTS.md`, `CLAUDE.md`, package scripts, contracts and user approvals. These skill files do not grant permissions.
- New source code or migrations require an explicitly authorized change scope; request approval for material production changes. Commits/PRs are not deployments.
- If the target repository lacks the studio structure, do not copy `project.yaml` or game-specific production folders into it. Put tests and evidence where that repository already expects them.
