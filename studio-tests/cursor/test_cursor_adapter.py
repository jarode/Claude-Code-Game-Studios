"""Check Cursor's native bridge without duplicating the skills catalog."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]

class CursorIntegration(unittest.TestCase):
    def test_native_rule_and_shared_agents(self):
        text = (ROOT / ".cursor/rules/ai-development-studio.mdc").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertRegex(text, r"(?m)^alwaysApply: true$")
        self.assertIn("AGENTS.md", text)
        self.assertIn(".agents/skills/", text)
        self.assertIn("Claude hooks", text)
        self.assertTrue((ROOT / "AGENTS.md").is_file())

    def test_reuse_existing_catalog_not_duplicate(self):
        codex = list((ROOT / ".agents/skills").glob("studio-*/SKILL.md"))
        self.assertEqual(len(codex), 84)
        self.assertEqual(list((ROOT / ".cursor").rglob("SKILL.md")), [])
        self.assertEqual(len(list((ROOT / ".cursor/rules").glob("*.mdc"))), 1)

    def test_cursor_doc_and_installer_install_rule(self):
        doc = (ROOT / "docs/CURSOR.md").read_text(encoding="utf-8")
        self.assertIn("not yet a verified Cursor test", doc)
        source = (ROOT / "scripts/install_app_studio.py").read_text(encoding="utf-8")
        self.assertIn('Cursor', source)
        self.assertIn('ai-development-studio.mdc', source)

if __name__ == "__main__":
    unittest.main()
