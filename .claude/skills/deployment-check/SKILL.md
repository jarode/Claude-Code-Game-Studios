---
name: deployment-check
description: "Assess pre-release readiness and rollback without silently publishing any app, migration or messages to production."
user-invocable: true
---
# Deployment Check — App Studio

This workflow also applies to applications outside Game Studios. It must operate on the user's actual application workspace, **not** on a generic Game Studios template. Read `docs/app-studio/README.md`, the matching technology profile(s), and relevant role files in `.claude/agents/`.

**Specialists:** release-manager, devops-engineer, security-engineer, e2e-automation-engineer (role profiles; actual independent agent execution requires compatible orchestration).

## Sequence
1. Verify target environment, protected branch, commit SHA, tests, required approvals and exact deployment artifact.
2. Inspect build/lint/test status, secrets/config presence (names only), migration ordering, environment drift and third-party dependencies.
3. Define smoke checks for health, auth, core workflow, logs and Web Push/email if involved; distinguish dry-run from real send.
4. Document migration/backward compatibility, rollback steps, backup verification and monitoring thresholds.
5. Return READY/BLOCKED/NOT ASSESSED with evidence. Never execute production deploy, merge, payment or mass send without explicit instruction.

## Evidence and acceptance
- **Done when:** A clear release decision package with blockers, evidence, rollback and post-release monitoring plan.
- Report source revision and branch, tests executed with exit codes, environment/device/browser, artifacts, findings and gaps.
- Every item must have a verdict: **PASS**, **FAIL**, or **NOT RUN**. Do not equate a static read, mock test, unit check, headless boot or screenshot with full end-to-end acceptance.
- Protect personal data, secrets and paid/external side effects. Never invent API results, screenshot comparisons, or task completion.
- Observe project-specific `AGENTS.md`, `CLAUDE.md`, package scripts, contracts and user approvals. These skill files do not grant permissions.
- New source code or migrations require an explicitly authorized change scope; request approval for material production changes. Commits/PRs are not deployments.
- If the target repository lacks the studio structure, do not copy `project.yaml` or game-specific production folders into it. Put tests and evidence where that repository already expects them.
