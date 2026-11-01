---
name: api-integration
description: "Integrate an external API, webhook or automation with authentication, idempotency, retries and redacted test fixtures."
user-invocable: true
---
# Api Integration — App Studio

This workflow also applies to applications outside Game Studios. It must operate on the user's actual application workspace, **not** on a generic Game Studios template. Read `docs/app-studio/README.md`, the matching technology profile(s), and relevant role files in `.claude/agents/`.

**Specialists:** integration-engineer, full-stack-developer, security-engineer, database-architect (role profiles; actual independent agent execution requires compatible orchestration).

## Sequence
1. Inventory caller/callee, payload schema, authentication method, rate limits and who owns each record. Use documented API; do not guess endpoint behavior.
2. Specify request/response/error contract, signature verification, replay protection, idempotency keys and failure queues or retries.
3. Create mock/fixture test for success, 4xx/5xx, timeout, duplicate, out-of-order and missing fields; verify secrets are never logged.
4. Implement bounded timeouts, backoff and observability with redaction; guard external side effects behind test mode/feature flags.
5. Run local contract/integration tests; separately mark any real third-party round trip NOT RUN when not attempted.

## Evidence and acceptance
- **Done when:** Documented contract, safe integration code, reliable failure handling, contract tests and operational notes.
- Report source revision and branch, tests executed with exit codes, environment/device/browser, artifacts, findings and gaps.
- Every item must have a verdict: **PASS**, **FAIL**, or **NOT RUN**. Do not equate a static read, mock test, unit check, headless boot or screenshot with full end-to-end acceptance.
- Protect personal data, secrets and paid/external side effects. Never invent API results, screenshot comparisons, or task completion.
- Observe project-specific `AGENTS.md`, `CLAUDE.md`, package scripts, contracts and user approvals. These skill files do not grant permissions.
- New source code or migrations require an explicitly authorized change scope; request approval for material production changes. Commits/PRs are not deployments.
- If the target repository lacks the studio structure, do not copy `project.yaml` or game-specific production folders into it. Put tests and evidence where that repository already expects them.
