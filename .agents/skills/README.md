# Codex workflow adapters

Each `studio-*` directory holds a thin Codex skill adapter that points to a canonical workflow under `.claude/skills/`. The canonical file contains the full specification; do not copy/paste it into a separate forked workflow. See `AGENTS.md` and `docs/CODEX-CHATGPT.md`.

## App Studio
The 8 app workflows also have thin adapters here. For use in a **different repository**, run `scripts/install_app_studio.py --target /path/to/app` (preview) then `--apply`; the installer creates **self-contained** Codex skills rather than cross-repo Markdown links. See `docs/app-studio/README.md`.
