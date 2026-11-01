---
name: feature-development
description: "Implement one business feature safely in an existing app with acceptance criteria, tests, code review and a branch/PR."
user-invocable: true
---
# Feature Development — App Studio

This workflow also applies to applications outside Game Studios. It must operate on the user's actual application workspace, **not** on a generic Game Studios template. Read `docs/app-studio/README.md`, the matching technology profile(s), and relevant role files in `.claude/agents/`.

**Specialists:** product-analyst, full-stack-developer, ux-designer, e2e-automation-engineer, security-engineer (role profiles; actual independent agent execution requires compatible orchestration).

## Sequence
1. Identify exact existing repo, actor flow and smallest acceptance slice. Read original tests, project conventions and constraints; record baseline.
2. Write or extend an executable failing test where feasible. Define normal, invalid, unauthorized and repeated requests; choose fixtures and rollback plan.
3. Implement the smallest diff in the existing architecture, preserving working UX and compatibility. Seek approval if scope broadens to production policy or destructive migration.
4. Run lint/typecheck/unit, targeted integration/e2e and visual/mobile checks where available. Record actual PASS/FAIL/NOT RUN per evidence.
5. Review diff for unrelated edits, secrets and accessibility; create PR only when authorized, do not merge/deploy implicitly.

## Evidence and acceptance
- **Done when:** Code plus executable evidence for acceptance criteria, no regression in the baseline, documented limits and reviewable PR or local diff.
- Report source revision and branch, tests executed with exit codes, environment/device/browser, artifacts, findings and gaps.
- Every item must have a verdict: **PASS**, **FAIL**, or **NOT RUN**. Do not equate a static read, mock test, unit check, headless boot or screenshot with full end-to-end acceptance.
- Protect personal data, secrets and paid/external side effects. Never invent API results, screenshot comparisons, or task completion.
- Observe project-specific `AGENTS.md`, `CLAUDE.md`, package scripts, contracts and user approvals. These skill files do not grant permissions.
- New source code or migrations require an explicitly authorized change scope; request approval for material production changes. Commits/PRs are not deployments.
- If the target repository lacks the studio structure, do not copy `project.yaml` or game-specific production folders into it. Put tests and evidence where that repository already expects them.
