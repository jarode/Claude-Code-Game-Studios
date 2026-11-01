---
name: studio-e2e-test
description: "Verify user journeys across roles, UI, API and devices with reproducible evidence."
---
# App Studio: e2e-test

Canonical workflow: [`.claude/skills/e2e-test/SKILL.md`](../../../.claude/skills/e2e-test/SKILL.md).

1. Read `AGENTS.md` and the canonical `.claude/skills/e2e-test/SKILL.md` completely. Apply the matching technology profile in `docs/app-studio/profiles/`, plus relevant role instructions in `.claude/agents/`.
2. Locate the **actual app repository**; validate its Git status, scripts, environment and authorization. Do not assume the Game Studios template is the app.
3. Execute each workflow stage using only available tools, recording real test outputs and evidence. Translate Claude-only tools and hooks; they are not automatically available in Codex.
4. Protect existing product behavior and user data. Avoid unwanted writes, deployments, force pushes or external messages.
5. Summarize PASS / FAIL / NOT RUN, findings, changes, test commands, and remaining manual checks.

For an app installed separately from this framework, use `scripts/install_app_studio.py` to create self-contained Codex skills without broken cross-repository links.
