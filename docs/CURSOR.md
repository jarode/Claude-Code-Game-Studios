# Cursor integration — AI Development Studio

Cursor is an **AI-powered code editor/agent environment**, not a single foundation model. It can use different models depending on plan and configuration. Its primary benefit here is interactive, visual code editing, repo navigation and Agent-based changes; Codex CLI remains useful for repeatable terminal tasks.

## Compatibility (verified against Cursor public documentation, 2026-11-01)
- Cursor automatically discovers project `SKILL.md` in `.agents/skills/` and `.cursor/skills/`, and also supports `.claude/skills/` for compatibility.
- Cursor reads project instructions in `AGENTS.md` and project rules in `.cursor/rules/*.mdc`.
- Therefore **we do not duplicate 84 skills into another directory**. Existing `.agents/skills/studio-*/` already provide the reusable skill catalog.
- The only native Cursor addition in this repository is `.cursor/rules/ai-development-studio.mdc`, to teach Cursor when/how to select existing skills and preserve safety.
- A skill/rule is an instruction, not an enabled MCP connection, real subagent, or automated test. Claude hooks are not automatically executed by Cursor.
- Cursor model availability and included usage depend on your current subscription; inspect Cursor's settings and billing panel instead of assuming specific models/limits.

References:
- https://cursor.com/docs/skills
- https://cursor.com/docs/rules
- https://cursor.com/docs/models-and-pricing

## Starting on this studio repository
1. Open the repository in Cursor with the latest `feature/cursor-adapter` branch.
2. Cursor should discover `.cursor/rules/ai-development-studio.mdc` and the skill catalog under `.agents/skills/`.
3. In the Agent chat ask: `Use studio-app-audit to inspect my existing application in read-only mode; name the selected technology profiles and evidence.`
4. For game code ask: `Use studio-quiz-development and studio-quiz-qa to propose a test-first, bounded change.`
5. Run/inspect real test output and review the diff before a PR.
6. Cloud/background workers require separately configured access and may not receive your machine-local/global skills; use version-controlled project skills.

## Adding Cursor to existing apps
Use the normal installer from this studio:
```bash
python scripts/install_app_studio.py --target /path/to/app
python scripts/install_app_studio.py --target /path/to/app --apply
```
It already installs eight **standalone** project skills under `.agents/skills/`. Since Cursor reads those, no additional copied skill set is necessary. This branch also installs an optional scoped native Cursor rule at `.cursor/rules/ai-development-studio.mdc`; conflicts cause a safe refusal. It never overwrites an existing `AGENTS.md`, product code or Cursor rules.

## Suggested responsibilities
- **Cursor**: interactive planning/debugging, UI and scene exploration, review of changes with the developer.
- **Codex**: controlled, repeatable code changes and tests in worktrees.
- **Claude Code**: optional alternate execution environment using canonical Claude workflows.
- **ChatGPT**: product coordination, integration access, review and verification.

Don't claim model superiority without measured trials on the same task. Compare identical scopes, tests, diff size, review burden, and actual subscription consumption.

## First manual Cursor acceptance test
1. Open a clean **copy** of the `flagi-i-panstwa` repo with installed App Studio skills.
2. Confirm `studio-app-audit` is discoverable in the Cursor Agent; ask it to identify Godot 4, country dataset, current regression tests **without modifying files**.
3. Verify the agent cites existing code paths and does not add `project.yaml`.
4. Run an existing test using a configured Godot binary and capture the actual exit code.
5. On a separate branch, request the reverse-quiz behavior regression, inspect the diff, and verify the test on Windows. This is a future manual acceptance task, **not yet a verified Cursor test**.

Record PASS/FAIL/NOT RUN independently for skill discovery, read-only audit, code edit, Godot test, visual UI and mobile TTS.
