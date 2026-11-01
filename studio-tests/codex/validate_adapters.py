#!/usr/bin/env python3
"""Check that the Codex adapter maps exactly to the canonical CCGS skills.

No third-party dependencies or network access required.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / ".claude" / "skills"
BRIDGES = ROOT / ".agents" / "skills"
FRONTMATTER = re.compile(r"\A---\n(?P<content>.*?)\n---\n", re.DOTALL)
NAME = re.compile(r"^name:\s*(\S+)\s*$", re.MULTILINE)


def check() -> list[str]:
    errors = []
    canonical = {p.parent.name: p for p in CANONICAL.glob("*/SKILL.md")}
    bridges = {p.parent.name.removeprefix("studio-"): p for p in BRIDGES.glob("studio-*/SKILL.md")}

    if not canonical:
        errors.append("No canonical skills found")
    if len(canonical) != 76:
        errors.append(f"Expected 76 canonical skills, got {len(canonical)}")
    missing = sorted(set(canonical) - set(bridges))
    extra = sorted(set(bridges) - set(canonical))
    if missing:
        errors.append(f"Missing Codex adapters: {', '.join(missing)}")
    if extra:
        errors.append(f"Unexpected Codex adapters: {', '.join(extra)}")

    for name, path in sorted(bridges.items()):
        text = path.read_text(encoding="utf-8")
        front = FRONTMATTER.match(text)
        if not front:
            errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
            continue
        found_name = NAME.search(front.group("content"))
        if not found_name or found_name.group(1) != f"studio-{name}":
            errors.append(f"{path.relative_to(ROOT)}: incorrect skill name")
        target = f".claude/skills/{name}/SKILL.md"
        if target not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing canonical reference {target}")
        # Markdown links must resolve correctly from their location.
        for link in re.findall(r"\]\((\.{1,2}/[^)]+)\)", text):
            if not (path.parent / link).resolve().is_file():
                errors.append(f"{path.relative_to(ROOT)}: broken relative link {link}")
        if re.search(r"(^|\n)\s*(?:allowed-tools|model):", front.group("content")):
            errors.append(f"{path.relative_to(ROOT)}: copied Claude-only frontmatter")

    for required in ["AGENTS.md", "docs/CODEX-CHATGPT.md", ".agents/skills/README.md"]:
        if not (ROOT / required).is_file():
            errors.append(f"Missing {required}")
    return errors


if __name__ == "__main__":
    problems = check()
    for problem in problems:
        print("FAIL:", problem)
    if problems:
        sys.exit(1)
    print(f"PASS: 76 canonical skills matched to {len(bridges)} valid Codex adapters")
