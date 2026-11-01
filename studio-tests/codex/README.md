# Codex compatibility checks

Run `python studio-tests/codex/validate_adapters.py` from anywhere (Python 3.9+).
This checks that every canonical workflow has one valid Codex adapter, its YAML frontmatter and relative Markdown links, and that the entrypoint documentation exists. A matching count does **not** imply that all Claude-specific commands are executable in Codex.

GitHub Actions runs the same offline check on PRs and relevant pushes.

## Manual integration smoke test

The following requires **Codex CLI** and a working directory containing the project; these tests cannot be replaced by static checks.

1. Run `codex` from the project root. Check that `AGENTS.md` is loaded and `$studio-start` appears as a skill (or refer to its file path).
2. Ask the studio to inspect a freshly initialized **throwaway Godot 4 game project**. Confirm that it reads `project.yaml`, detects the stage and asks the user before writing project files.
3. Implement a tiny UI story via `$studio-dev-story`. Verify engine execution and capture a screenshot; do not mark visual acceptance PASS on parsing alone.
4. Use `$studio-story-done` to check acceptance evidence and status changes.
5. Run original Claude Code workflow separately and confirm its hooks remain operational.
6. Record observed commands, exit codes, screenshots and failures in your local QA documentation.

**Explicit limitations:** Claude `PreToolUse`/`PostToolUse` hooks and `Agent` tool calls are not automatically ported. This integration provides reuse of specifications and skill discovery, not feature-identical execution.
