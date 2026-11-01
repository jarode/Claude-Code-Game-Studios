---
name: app-audit
description: "Audit an existing web, mobile, SaaS, Godot or integration repository and produce a risk-ranked modernization plan without modifying product code."
user-invocable: true
---
# App Audit — App Studio

This workflow also applies to applications outside Game Studios. It must operate on the user's actual application workspace, **not** on a generic Game Studios template. Read `docs/app-studio/README.md`, the matching technology profile(s), and relevant role files in `.claude/agents/`.

**Specialists:** product-analyst, technical-director, full-stack-developer, database-architect, security-engineer, e2e-automation-engineer (role profiles; actual independent agent execution requires compatible orchestration).

## Sequence
1. Locate the *actual* target repository; inspect Git status, recent commits, running environment, READMEs and build scripts. Do not mistake framework template for product source.
2. Map frontend/backend, database and external dependencies. Identify user roles, critical journeys, secrets exposure risk and existing test coverage. Mark unknowns explicitly.
3. Run available read-only checks or fixture-only tests; record exit codes, date, runtime, command, warning and coverage gaps.
4. Rank findings by user impact, severity, effort and regression risk; separate defects demonstrated from hypotheses.
5. Produce a smallest-first backlog with baseline evidence and suggested first PR. No source edits or production actions in this workflow.

## Evidence and acceptance
- **Done when:** A factual architecture map, at least three prioritized testable risks or explicit zero-findings statement, and an acceptance-ready first task.
- Report source revision and branch, tests executed with exit codes, environment/device/browser, artifacts, findings and gaps.
- Every item must have a verdict: **PASS**, **FAIL**, or **NOT RUN**. Do not equate a static read, mock test, unit check, headless boot or screenshot with full end-to-end acceptance.
- Protect personal data, secrets and paid/external side effects. Never invent API results, screenshot comparisons, or task completion.
- Observe project-specific `AGENTS.md`, `CLAUDE.md`, package scripts, contracts and user approvals. These skill files do not grant permissions.
- New source code or migrations require an explicitly authorized change scope; request approval for material production changes. Commits/PRs are not deployments.
- If the target repository lacks the studio structure, do not copy `project.yaml` or game-specific production folders into it. Put tests and evidence where that repository already expects them.
