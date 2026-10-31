# ChatGPT and Codex compatibility

This fork keeps Claude Code intact while providing a Codex-compatible entry point.

## Supported and unsupported

| Feature | Claude Code | Codex | ChatGPT chat |
|---|---|---|---|
| Project instructions | `CLAUDE.md` | `AGENTS.md` | Read supplied project files or connected GitHub |
| Studio workflows | `.claude/skills/*` | `.agents/skills/studio-*` bridges | Ask to execute a named workflow using available tools |
| 49 studio roles | Claude subagents | Reuse role profiles; delegate only when supported | Simulate role review sequentially |
| 15 lifecycle hooks | Native via `.claude/settings.json` | **Not installed by this adapter** | Not supported natively |
| File-based config and docs | Supported | Supported | Supported when files accessible |
| Build, tests, QA screenshots | Local tools | Local tools when available | Only with access to execution/browser tools |

**Important:** A Codex skill bridge is not a native Claude command and does not magically install Claude hooks. Existing shell helpers may be called manually after reviewing their scope. Do not run destructive scripts solely because a Claude skill requests them.

## Start with Codex

1. Clone the fork locally and open **the repository root** in Codex CLI or an editor with Codex.
2. Read `AGENTS.md` and choose `$studio-start`; or ask: "Follow the studio-start skill; inspect my project and propose the next step."
3. To implement an existing story use `$studio-dev-story` with its path; for acceptance use `$studio-story-done`.
4. Codex skill discovery can vary with client/version: if a skill is not displayed, explicitly ask Codex to read its `.agents/skills/studio-*/SKILL.md` file.
5. Use Godot/Unity/Unreal only after setting `project.yaml` through the existing workflow.

## Use from ChatGPT

Connect GitHub and reference this repository. Ask: "Read AGENTS.md, the corresponding .claude/skills/<name>/SKILL.md, and role files needed for this task, then follow the workflow." ChatGPT can coordinate repository edits through its GitHub connector, but a local build/test requires a tool with access to the engine and working tree. The skills do not automatically appear as ChatGPT slash commands or installed plugins.

## Mapping

- `.claude/agents/<role>.md`: role profile, not a guarantee a separate agent is launched.
- `.claude/skills/<name>/SKILL.md`: canonical workflow; keep edits here rather than maintaining divergent copies.
- `.agents/skills/studio-<name>/SKILL.md`: thin Codex adapter, including pointers to the canonical skill.
- `.claude/settings.json`: Claude-only hooks and permission semantics. Codex's own sandbox/approval policy applies separately.
- `CLAUDE.md`: Claude project setup, complemented rather than replaced by `AGENTS.md`.

## Smoke checks

Check that all bridges point to an existing canonical skill, inspect the diff to ensure Claude files were not altered, and run one workflow such as `studio-start` in a real Codex session. No runtime interoperability should be claimed until validated in that environment.

## Compatibility development

New workflows should be implemented once under `.claude/skills/` and exposed via a small adapter under `.agents/skills/`. Avoid copying long workflow bodies. Document any Claude-only syntax that needs a Codex substitute.