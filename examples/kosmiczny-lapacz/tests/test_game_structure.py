"""Deterministic smoke checks for the standalone example's source structure."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class GameStructureTests(unittest.TestCase):
    def test_project_has_main_scene_and_expected_viewport(self):
        project = (ROOT / "project.godot").read_text(encoding="utf-8")
        self.assertIn('run/main_scene="res://main.tscn"', project)
        self.assertIn("window/size/viewport_width=1280", project)
        self.assertIn("window/size/viewport_height=720", project)

    def test_scene_uses_local_game_script(self):
        scene = (ROOT / "main.tscn").read_text(encoding="utf-8")
        self.assertIn('path="res://game.gd"', scene)

    def test_game_has_requested_loop_and_controls(self):
        game = (ROOT / "game.gd").read_text(encoding="utf-8")
        for required in (
            "const INITIAL_LIVES: int = 3",
            "KEY_W", "KEY_A", "KEY_S", "KEY_D",
            "KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT",
            "_spawn_asteroid", "_spawn_star", "_start_game",
            "_game_state = &\"game_over\"", "_score += 10",
            "Naciśnij ENTER", "KONIEC GRY",
        ):
            with self.subTest(required=required):
                self.assertIn(required, game)


if __name__ == "__main__":
    unittest.main()