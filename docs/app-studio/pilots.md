# App Studio pilots

## Pilot A — Flagi i państwa (Godot quiz)
**Repository:** `jarode/flagi-i-panstwa`. Existing tests: `tests/test_dataset.py`, `tests/FlagQuizSmoke.gd`, and on feature PR #1 `tests/QuizAnswerRegression.gd`. User verified manual play in related Godot projects, but device TTS still needs separate testing.

**Purpose:** Use `studio-app-audit` and `studio-e2e-test` to check that a single answer can score once, quiz answers are unique and 195 flags match records; protect mobile layout, Polish TTS and saved progress.

**Baseline from previous run (2026-11-01):** 195 countries/flags passed; new scoring regression PASS in Linux/Windows Godot 4.6.2 on PR branch; GitHub Actions passed. This is not a claim that PR #1 was merged or that Android TTS was tested.

**New acceptance evidence:** test result and exit code, list of 3 answer choices, correct + double-click + wrong-to-correct retry, restart and progress save, Android TTS manual test explicitly NOT RUN until performed. Preserve app engine.

## Pilot B — DJ SOS (Cloudflare Workers/Pages + Supabase)
**Repository:** `jarode/dj-sos`. Current `package.json` defines `npm run check`, `npm run test:smoke`, `npm run build:pages-preview`; CI runs local Worker, auth/geo/offers/privacy smoke and build.

**Purpose:** Use `studio-app-audit`, `studio-e2e-test`, `studio-database-migration` and `studio-deployment-check` to complete organizer → SOS → matching DJ → offer → select/accept with two authenticated test accounts, including RLS and Web Push.

**Safety:** First audit is read-only. Never send bulk email, modify production Supabase, assume device push from HTTP 200, or deploy Cloudflare without separate authorization. If authenticated test accounts are unavailable in the test environment, mark authenticated E2E **NOT RUN**.

**Acceptance evidence needed:** explicit actors, test-only IDs, runtime logs with PII masked, selection state and transaction rollback/cleanup; screen/browser behavior as separate evidence, physical push delivery separately checked.

## Pilot C — Bitrix24 / business automation
Use `studio-api-integration` and `studio-privacy-compliance-reviewer` *role* for webhook dedupe, paging, idempotent updates and audit logs. Test on fixtures or sandbox first; do not update real HR/order records without permission.

## Prioritization
1. Make the installer and 84-skill validation green.
2. Run `studio-app-audit` against `flagi-i-panstwa` and `dj-sos` with evidence and no changes to production.
3. Pick the smallest isolated regression and write a test-first PR.
4. Only after review, consider release checklist or broader automation.
