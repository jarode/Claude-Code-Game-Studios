# Game Studios — Codex / ChatGPT instructions

This repository is a cross-tool game-development studio. **Do not change or delete the Claude Code integration.** Claude-specific settings and hooks under `.claude/` are NOT automatically enforced by Codex or ChatGPT.

## Source of truth
- Read `project.yaml` (and optional gitignored `project.local.yaml`) to determine engine, rigor, and project state. Do not introduce competing configuration files.
- Read `production/session-state/active.md` if present before resuming a task.
- The role profiles live in `.claude/agents/*.md`. Their responsibilities and domain guidance apply to Codex, but Claude-only frontmatter (model, allowed-tools) and subagent execution syntax do not.
- The canonical workflow implementations live in `.claude/skills/<workflow>/SKILL.md`; Codex skill bridges are in `.agents/skills/`.
- Read the relevant documents under `.claude/docs/` and the engine version in `docs/engine-reference/<engine>/VERSION.md` when applicable.
- Never assume Claude `@` imports or `!\` command interpolation are executed by Codex; resolve relevant paths and commands explicitly.

## How to work
1. Identify the user's goal and actual current project stage. Prefer short, working increments over unnecessary documentation.
2. Pick an appropriate workflow from `.agents/skills/` (or inspect its corresponding canonical Claude skill) and select relevant specialist roles from `.claude/agents/`.
3. Follow the workflow intent, dependencies, quality gates and artifact locations. Translate Claude-only `Agent`, `AskUserQuestion`, `Task`, `Read`, and `Bash` instructions into available Codex tools; never claim parallel agents ran unless they actually did.
4. Obey the collaboration protocol in `CLAUDE.md`: ask before changing project files and committing, except when the user's explicit instruction already authorizes the specific changes. Don't ask again for authorization already granted.
5. Keep all project decisions, status, artifacts and QA evidence in the canonical repository locations. Don't maintain a second studio state.
6. For UI or visual game work, run the game and inspect screenshots; a compile or parse check alone is not proof the UI works.
7. If an executable/tool/permission is missing, mark the check NOT RUN. Don't report hypothetical tests as passes.
8. Never publish, deploy, force-push, delete data, or modify secrets without explicit authorization. Protect `.env*`, credentials and personal data.

## Game engine
- Godot: inspect `project.godot`; use installed `godot --headless --path <project> --quit` for a parse/start smoke check; run a visible game session and record evidence for visual changes.
- Unity/Unreal: resolve the real project location and available build toolchains before running engine commands.
- The repository is a studio template, not itself a complete runnable game.

## Quick starts
- New studio: use `$studio-start` or ask Codex to follow `.claude/skills/start/SKILL.md`.
- Development: use `$studio-dev-story`, naming the story path.
- Review/closure: use `$studio-story-done` only after evidence has been collected.
- Full workflow catalog: see `docs/CODEX-CHATGPT.md` and `.agents/skills/`.

For plain ChatGPT (without a Codex project workspace), the same markdown roles/workflows can be read as project documents, but local commands, file edits, tests and hooks require separately available tools.