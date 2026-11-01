---
name: production-incident
description: "Triage outages and data/security incidents using read-only diagnostics, safe containment plans and human-approved fixes."
user-invocable: true
---
# Production Incident — App Studio

This workflow also applies to applications outside Game Studios. It must operate on the user's actual application workspace, **not** on a generic Game Studios template. Read `docs/app-studio/README.md`, the matching technology profile(s), and relevant role files in `.claude/agents/`.

**Specialists:** devops-engineer, security-engineer, database-architect, integration-engineer, product-analyst (role profiles; actual independent agent execution requires compatible orchestration).

## Sequence
1. Record impact, affected actors, start time and severity; gather logs/health/status using *read-only* access by default.
2. Correlate recent deploys, config/migration changes, errors and external dependencies without exposing PII or credentials.
3. Form ranked hypotheses with specific supporting/contradicting evidence and low-risk verification steps.
4. Propose rollback or containment with side effects listed; obtain explicit authorization before changing production, deleting data or revoking tokens.
5. After the fix is approved and executed, verify recovery, capture timeline and add regression/monitoring action items. No claimed recovery without measurement.

## Evidence and acceptance
- **Done when:** Impact summary, evidence timeline, root-cause confidence, containment options, verified state and preventative follow-up.
- Report source revision and branch, tests executed with exit codes, environment/device/browser, artifacts, findings and gaps.
- Every item must have a verdict: **PASS**, **FAIL**, or **NOT RUN**. Do not equate a static read, mock test, unit check, headless boot or screenshot with full end-to-end acceptance.
- Protect personal data, secrets and paid/external side effects. Never invent API results, screenshot comparisons, or task completion.
- Observe project-specific `AGENTS.md`, `CLAUDE.md`, package scripts, contracts and user approvals. These skill files do not grant permissions.
- New source code or migrations require an explicitly authorized change scope; request approval for material production changes. Commits/PRs are not deployments.
- If the target repository lacks the studio structure, do not copy `project.yaml` or game-specific production folders into it. Put tests and evidence where that repository already expects them.
