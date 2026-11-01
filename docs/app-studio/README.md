# AI Development Studio (App Studio)

Non-destructive extension of Claude Code Game Studios for existing web, mobile, SaaS and integration products.

## Editor integration
Cursor reads the same project skills under `.agents/skills/`. See [Cursor setup and acceptance checklist](../CURSOR.md). No duplicated skill set is required.

## What exists
- **Game Studio remains intact:** 49 legacy game roles, 76 legacy/canonical workflows (including the 2 educational quiz additions).
- **App Studio adds:** 7 application-specific roles, 8 new canonical workflows, 8 Codex bridges and 6 technology profiles. Total after this extension: **56 role files and 84 canonical skills**.
- A Claude role file is an instruction profile, **not a running autonomous agent**. A Codex adapter does not activate Claude hooks or enable tools the environment lacks.
- Neither Codex nor ChatGPT can bypass repository/tool permissions; all work must be performed through connected/installed tools.

## Select the workflow by intent

| Objective | Skill | Specialist focus |
|---|---|---|
| Inspect and prioritize | `app-audit` | Product, architecture, QA |
| Add a feature | `feature-development` | Full stack, UX, tests |
| Connect services | `api-integration` | Integration, security |
| Change schema or RLS | `database-migration` | Database, security, privacy |
| Check customer journey | `e2e-test` | QA automation |
| Protect the frontend | `ui-regression` | UX, accessibility, device |
| Prepare release | `deployment-check` | DevOps, release, rollback |
| Resolve incidents | `production-incident` | Read-only triage first |

For quiz apps use `quiz-development` and `quiz-qa` alongside these workflows.

## Profile selection
Choose based on evidence in the target repo, not guesses: `profiles/godot-quiz.md`, `nextjs-web.md`, `cloudflare-workers-pages.md`, `supabase-postgres.md`, `react-native-expo.md`, `bitrix24-n8n.md`. More than one profile may apply; e.g. a Cloudflare Worker + Supabase app needs both.

## Use on an existing repo (important)
From the root of this studio repository, preview installation:
```sh
python scripts/install_app_studio.py --target /path/to/my-app
```
Apply the explicit, additive installation:
```sh
python scripts/install_app_studio.py --target /path/to/my-app --apply
```
It copies **self-contained** Codex/Cursor skills, app roles, technology profiles and a native Cursor project rule. It does **not** touch the target's `AGENTS.md`, `project.yaml`, existing skills, existing Cursor rules or `.claude/settings.json`, and refuses overwrites. Run in a throwaway branch/worktree and review `git diff` before committing. For Claude skills, use the studio repository directly or copy the canonical workflows deliberately; installation does not promise automatic Claude hook behavior.

In Codex from the target application root:
> Use `$studio-app-audit`, inspect this existing repository, run read-only tests, and produce a prioritized first story with evidence.

For a feature:
> Use `$studio-feature-development` on the selected issue, preserve existing code and UI, write tests, and prepare a reviewable PR.

If a local Codex client doesn't discover installed skills automatically, ask it to read the file `.agents/skills/studio-app-audit/SKILL.md` directly.

## Release safety gate
For each story record: source branch/commit, scope and approvals, expected behavior, tests with commands and exit codes, independent environment where applicable, authenticated/unauthenticated behavior, privacy/security impact, rollback and cleanup. Mark each test **PASS**, **FAIL** or **NOT RUN**. A check with missing evidence is NOT RUN, not PASS.

Production deployment, DB changes, payments, real notifications and customer/HR data writes require separate explicit authorization. A green CI run is **not** approval to release.

## Pilot work
See `docs/app-studio/pilots.md`. Keep pilot reports truthful and grounded in the *current* target repository; do not assume old reports remain current.
