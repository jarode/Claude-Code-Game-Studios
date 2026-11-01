---
name: database-migration
description: "Plan and implement safe database schema/RLS migration with backward compatibility, role tests and rollback evidence."
user-invocable: true
---
# Database Migration — App Studio

This workflow also applies to applications outside Game Studios. It must operate on the user's actual application workspace, **not** on a generic Game Studios template. Read `docs/app-studio/README.md`, the matching technology profile(s), and relevant role files in `.claude/agents/`.

**Specialists:** database-architect, security-engineer, full-stack-developer, privacy-compliance-reviewer (role profiles; actual independent agent execution requires compatible orchestration).

## Sequence
1. Inspect current schema and every relevant migration; find dependent APIs, roles, service credentials, retention and table size.
2. Write explicit expand/backfill/contract plan, constraints/indexes and rollback or forward-fix. Mark destructive steps as requiring approval.
3. Generate migration on a feature branch only. Use deterministic fixtures and separate local/staging database; never run against production implicitly.
4. Test anonymous, owner, non-owner, admin and service-role access plus concurrency/idempotency where applicable. Check security-invoker and RLS boundaries.
5. Run local migration up + schema validation and compatible-code tests. Report data-loss risk, locks and unresolved deployment sequencing.

## Evidence and acceptance
- **Done when:** Versioned migration, role matrix, test evidence and an executable rollout/rollback plan, not an unverified promise.
- Report source revision and branch, tests executed with exit codes, environment/device/browser, artifacts, findings and gaps.
- Every item must have a verdict: **PASS**, **FAIL**, or **NOT RUN**. Do not equate a static read, mock test, unit check, headless boot or screenshot with full end-to-end acceptance.
- Protect personal data, secrets and paid/external side effects. Never invent API results, screenshot comparisons, or task completion.
- Observe project-specific `AGENTS.md`, `CLAUDE.md`, package scripts, contracts and user approvals. These skill files do not grant permissions.
- New source code or migrations require an explicitly authorized change scope; request approval for material production changes. Commits/PRs are not deployments.
- If the target repository lacks the studio structure, do not copy `project.yaml` or game-specific production folders into it. Put tests and evidence where that repository already expects them.
