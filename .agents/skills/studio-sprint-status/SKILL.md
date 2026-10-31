---
name: studio-sprint-status
description: "Run the Game Studios sprint-status workflow in Codex using the canonical skill specification."
---

# Studio: sprint-status

1. Read `AGENTS.md` and `project.yaml`, then read the **entire** canonical workflow: `.claude/skills/sprint-status/SKILL.md`.
2. Follow its intent and relevant referenced documentation, preserving the repository's existing status, artifact and QA conventions.
3. Interpret Claude-only tool names, hooks, `@file` imports, `!\` shell interpolation, model declarations and subagent syntax as **instructions to adapt**, not executable Codex syntax. Run referenced shell helpers only if available and safe.
4. If the workflow references an agent, read its profile in `.claude/agents/` and apply that role's standards; do not claim separate agents executed unless supported and actually used.
5. Request approval where required by the repository collaboration contract, unless the user's instruction has already authorized this exact work. Report checks as PASS, FAIL or NOT RUN with evidence.

Canonical definition: [`.claude/skills/sprint-status/SKILL.md`](../../../.claude/skills/sprint-status/SKILL.md).
