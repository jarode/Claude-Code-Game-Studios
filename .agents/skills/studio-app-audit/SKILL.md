---
name: studio-app-audit
description: "Audit an existing application and produce a prioritized, evidence-backed improvement backlog."
---
# App Studio: app-audit

Canonical workflow: [`.claude/skills/app-audit/SKILL.md`](../../../.claude/skills/app-audit/SKILL.md).

1. Read `AGENTS.md` and the canonical `.claude/skills/app-audit/SKILL.md` completely. Apply the matching technology profile in `docs/app-studio/profiles/`, plus relevant role instructions in `.claude/agents/`.
2. Locate the **actual app repository**; validate its Git status, scripts, environment and authorization. Do not assume the Game Studios template is the app.
3. Execute each workflow stage using only available tools, recording real test outputs and evidence. Translate Claude-only tools and hooks; they are not automatically available in Codex.
4. Protect existing product behavior and user data. Avoid unwanted writes, deployments, force pushes or external messages.
5. Summarize PASS / FAIL / NOT RUN, findings, changes, test commands, and remaining manual checks.

For an app installed separately from this framework, use `scripts/install_app_studio.py` to create self-contained Codex skills without broken cross-repository links.
