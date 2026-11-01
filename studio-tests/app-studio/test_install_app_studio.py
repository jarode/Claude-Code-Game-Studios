"""Installer and manifest tests for the App Studio extension (stdlib only)."""
import importlib.util
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("install_app_studio", ROOT / "scripts/install_app_studio.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def test_manifest_counts_and_coverage(self):
        files = installer.build_files()
        self.assertEqual(len(installer.WORKFLOWS), 8)
        self.assertEqual(len(installer.APP_ROLES), 7)
        self.assertEqual(len(installer.PROFILES), 6)
        for name in installer.WORKFLOWS:
            file = files[Path(".agents/skills") / f"studio-{name}" / "SKILL.md"]
            self.assertTrue(file.startswith(f"---\nname: studio-{name}\n"))
            self.assertIn("## Sequence", file)
            self.assertIn("PASS", file)
            self.assertNotIn("Canonical workflow: [", file)
        for name in installer.APP_ROLES + installer.SUPPORT_ROLES:
            self.assertIn(Path(".app-studio/roles") / f"{name}.md", files)
        for profile in installer.PROFILES:
            self.assertIn(Path("docs/app-studio/profiles") / profile, files)
        self.assertTrue(all(re.match(r"^[a-z0-9-]+$", name) for name in installer.WORKFLOWS))

    def test_default_is_dry_run_then_apply(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            n, total = installer.install(root)
            self.assertGreater(n, 0)
            self.assertGreater(total, 20)
            self.assertFalse((root / ".agents").exists())
            n2, total2 = installer.install(root, apply=True)
            self.assertEqual((n2, total2), (n, total))
            self.assertTrue((root / ".agents/skills/studio-app-audit/SKILL.md").is_file())
            self.assertTrue((root / "docs/app-studio/README.md").is_file())
            n3, _ = installer.install(root, apply=True)
            self.assertEqual(n3, 0)

    def test_conflict_is_non_destructive(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            p = root / ".agents/skills/studio-app-audit/SKILL.md"
            p.parent.mkdir(parents=True)
            p.write_text("user's existing content\n")
            with self.assertRaisesRegex(ValueError, "Refusing to overwrite"):
                installer.install(root, apply=True)
            self.assertEqual(p.read_text(), "user's existing content\n")
            self.assertFalse((root / "docs/app-studio").exists())

    def test_requires_existing_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "existing directory"):
                installer.install(Path(tmp) / "no-such-directory", apply=True)


if __name__ == "__main__":
    unittest.main()
