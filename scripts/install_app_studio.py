#!/usr/bin/env python3
"""Safely install self-contained App Studio Codex skills into an existing app.

Preview by default; --apply writes only missing files, refusing conflicts.
Does not modify AGENTS.md, project.yaml, existing skills, Claude settings, or app code.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

SOURCE_ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = (
    "app-audit", "feature-development", "api-integration", "database-migration",
    "e2e-test", "ui-regression", "deployment-check", "production-incident",
)
APP_ROLES = (
    "product-analyst", "full-stack-developer", "database-architect",
    "mobile-developer", "integration-engineer", "e2e-automation-engineer",
    "privacy-compliance-reviewer",
)
SUPPORT_ROLES = (
    "security-engineer", "technical-director", "ux-designer", "ui-programmer",
    "accessibility-specialist", "qa-lead", "release-manager", "devops-engineer",
)
PROFILES = (
    "godot-quiz.md", "nextjs-web.md", "cloudflare-workers-pages.md",
    "supabase-postgres.md", "react-native-expo.md", "bitrix24-n8n.md",
)


def build_files() -> dict[Path, str]:
    """Build all installable files from canonical source; no duplicate workflow source."""
    output: dict[Path, str] = {}
    for name in WORKFLOWS:
        src = SOURCE_ROOT / ".claude" / "skills" / name / "SKILL.md"
        original = src.read_text(encoding="utf-8")
        match = re.match(r"\A---\n.*?\n---\n", original, re.DOTALL)
        if not match:
            raise ValueError(f"Missing skill frontmatter: {src}")
        body = original[match.end():]
        body = body.replace(".claude/agents/", ".app-studio/roles/")
        header = (
            f"---\nname: studio-{name}\n"
            f"description: \"App Studio workflow: {name.replace('-', ' ')} for existing applications\"\n"
            "---\n"
        )
        output[Path(".agents/skills") / f"studio-{name}" / "SKILL.md"] = (
            header + "\n" + body +
            "\n\n## Standalone installation\n"
            "Skill source: AI Development Studio. Role documents are in "
            "\`.app-studio/roles/\`; technology guides in \`docs/app-studio/profiles/\`. "
            "Do not require the Game Studios template or its project.yaml.\n"
        ).replace("\\`", "`")
    for name in APP_ROLES + SUPPORT_ROLES:
        src = SOURCE_ROOT / ".claude" / "agents" / f"{name}.md"
        output[Path(".app-studio/roles") / f"{name}.md"] = src.read_text(encoding="utf-8")
    docs = SOURCE_ROOT / "docs" / "app-studio"
    for file in docs.rglob("*.md"):
        output[file.relative_to(SOURCE_ROOT)] = file.read_text(encoding="utf-8")
    return output


def install(target: Path, apply: bool = False) -> tuple[int, int]:
    target = target.expanduser().resolve()
    if not target.is_dir():
        raise ValueError(f"Target must be an existing directory: {target}")
    if target == SOURCE_ROOT:
        raise ValueError("Cannot install App Studio into the source framework itself")
    files = build_files()
    # Preflight all paths BEFORE touching any file: no partial overwrite on conflicts.
    conflicts = []
    updates = []
    for rel, content in files.items():
        dest = target / rel
        if dest.is_symlink() or any(parent.is_symlink() for parent in dest.parents if parent != target and target in parent.parents):
            conflicts.append(rel)
        elif dest.exists():
            if not dest.is_file() or dest.read_text(encoding="utf-8") != content:
                conflicts.append(rel)
        else:
            updates.append((dest, content))
    if conflicts:
        raise ValueError("Refusing to overwrite existing files: " + ", ".join(map(str, conflicts)))
    action = "WRITE" if apply else "PREVIEW"
    for dest, content in updates:
        print(f"{action} {dest.relative_to(target)}")
        if apply:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
    print(f"{len(updates)} new file(s); {len(files) - len(updates)} already identical; mode={'apply' if apply else 'dry-run'}")
    return len(updates), len(files)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True, help="Existing app root")
    parser.add_argument("--apply", action="store_true", help="Actually create the missing files")
    args = parser.parse_args(argv)
    try:
        install(args.target, apply=args.apply)
    except (ValueError, OSError) as err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
