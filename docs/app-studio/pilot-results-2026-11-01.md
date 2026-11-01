# App Studio — pilot execution report (2026-11-01)

These results were obtained against **isolated local clones**, not against production or the original application working trees. All framework roles/skills were installed additively into these clones with `scripts/install_app_studio.py --apply`. **No merge, deploy, production database mutation or customer message occurred.**

## Execution matrix

| Check | Target | Evidence and outcome |
|---|---|---|
| Adapter validation | Game Studios branch `feature/ai-development-studio` | `python3 studio-tests/codex/validate_adapters.py` — **PASS**, 84 canonical skills matched to 84 adapters |
| Safe installer tests | Game Studios branch | `python3 -m unittest discover -s studio-tests/app-studio -p 'test_*.py' -v` — **PASS** (dry-run, apply, idempotency, conflict handling and manifest coverage) |
| Hosted CI | Game Studios branch, commit `5ddfb6b` | **PASS**, [GitHub Actions run 41289533518](https://github.com/jarode/Claude-Code-Game-Studios/actions/runs/41289533518) |
| Install | `jarode/flagi-i-panstwa` / `feature/quiz-qa-first-test` | Preview then apply — 31 new files, 0 product source/config overwrites; new untracked skills/docs expected |
| Dataset | Flagi pilot | `python3 tests/test_dataset.py` — **PASS**: 195 states/flags, 30 easy, 165 hard |
| Godot scoring regression | Flagi pilot | Godot 4.6.2 `--headless --path . --script res://tests/QuizAnswerRegression.gd` — **PASS**, `QUIZ_ANSWER_REGRESSION_PASS`, exit 0 |
| Install | `jarode/dj-sos` / `main` | Apply — 31 new files, 0 product source/config overwrites |
| Existing checks | DJ SOS pilot | `npm ci --ignore-scripts --no-audit --no-fund`; `npm run check` — **PASS**, 156/156 Node tests (exit 0) |
| Codex App Studio audit | Both pilot clones | **PASS** for read-only invocation and generation of evidence-backed backlog; no product source edits |
| Real UI/authenticated E2E | Both pilot clones | **NOT RUN** in this pilot |
| Real mobile TTS / closed-app Web Push | Device-dependent | **NOT RUN** in this pilot |

**Precision:** `npm run check` was independently executed by the pilot setup runner. The subsequent **read-only Codex audit** did not rerun it; its own report correctly marks `npm run check` NOT RUN *within that separate audit*. Similar distinction applies to the existing Godot smoke suites.

## Pilot A — Flagi i państwa

**Read-only audit:** on `feature/quiz-qa-first-test` commit `6a0b80c` using installed `studio-app-audit`.

**Findings, supported by source locations:**
1. **High — reverse quiz regression gap:** `tests/QuizAnswerRegression.gd` covers standard direction; `scripts/road_signs/QuizScreen.gd` implements reverse options as icons. `tests/FlagQuizSmoke.gd` checks reverse setup but not full selection/scoring/finish. **Proposed first story:** deterministic reverse-direction scoring, wrong answer and duplicate-tap regression (no new gameplay).
2. **High — Android speech evidence gap:** `scripts/app/App.gd` handles TTS and voice selection. Device test should confirm Polish speech, manual/automatic reading, interrupted speech and missing-voice fallback.
3. **Medium — dataset edge cases:** `tests/test_dataset.py` should cover every canonical country ID, valid `similar` references, unknown IDs, empty/short option pools and exactly one correct answer.
4. **Medium — narrow viewport UI:** inspect 320/390 px layouts for both quiz directions, using actual device or screenshot evidence.
5. **Medium — persistence:** verify `user://flagi_progress.json` survives app restart and best-score logic remains correct.

**Required acceptance before release:** automated reverse-mode PASS; separate device TTS + visual PASS; progress storage tests, marked NOT RUN until executed.

## Pilot B — DJ SOS

**Read-only audit:** on `main` commit `c31097a` using installed `studio-app-audit`; Cloudflare and Supabase profiles selected.

**Findings, supported by source locations:**
1. **High — authenticated organizer/DJ/third-user E2E:** `docs/45_MASTER_PLAN_20261031.md` and `docs/42_E2E_BROWSER_STAGE1_STATUS.md` still list real two-account end-to-end verification as open. Code has offer selection, messaging, auth/permissions and transaction tests. Reuse those, do not rebuild them.
2. **High — withdrawal and confirmation/decline on real sessions:** `src/beta-online.js`, `test/organizer-withdraw-offer.test.mjs`; static/unit coverage is not yet browser or persisted-state evidence across roles.
3. **High — physical Web Push:** `test/web-push.test.mjs`, `test/push-dispatch-eligibility.test.mjs` and `docs/55_E2E_MOBILE_ACCEPTANCE_PLAN.md` define eligibility and test plan; physical delivery/click through remains NOT RUN in this pilot.
4. **Medium — Realtime reconnection:** `src/beta-online.js` subscribes to SOS and offers; reconnect/visibility behavior needs an observed test, not a static-only conclusion.

**Required acceptance:** approved staging accounts, tagged/cleaned QA records, actual browser role flows, API/DB/RLS evidence, and physically observed Push, each with separate PASS/FAIL/NOT RUN status. Production sends, migrations and releases remain out of scope without explicit approval.

## Proposed next controlled PRs
1. `flagi-i-panstwa`: add reverse-quiz behavior regression; run Godot 4.6.2, follow with mobile TTS test.
2. `dj-sos`: introduce an isolated authenticated E2E runbook/test harness around existing offer flow; no credentials in repo, no production writes.
3. Keep App Studio's CI green and document the role/skill selection in one short onboarding command per app.

## Limitations
This report does not imply that all 84 workflows have been executed, that multiple independent AI agents ran, or that native Claude hooks are available to Codex. A standalone skill is instruction; the actual runtime requires installed tools and granted access.
