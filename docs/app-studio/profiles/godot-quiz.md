# Godot 4 / educational quizzes
**Identify:** `project.godot`, Godot version, scene roots, GDScript tests, data JSON/SVG and Android exports.
**Core checks:** datasets and assets (unique IDs), exactly one correct answer, duplicate/rapid click lock, score + progress, TTS fallback, screen sizes 320/390 px and accessibility.
**Safe commands:** use installed Godot binary; `godot --headless --editor --path . --quit` for import, `godot --headless --path . --script res://tests/<existing_runner>.gd` for unit/smoke. Never invent `<existing_runner>`.
**Release gate:** actual Godot scene tests + user/device TTS, restart, offline, save/load and visual checks. Headless CLI alone cannot PASS screenshots or mobile audio.
**Known pilot:** `jarode/flagi-i-panstwa`; checks `python3 tests/test_dataset.py`, `FlagQuizSmoke.gd`, `QuizAnswerRegression.gd` (PR #1, merge state must be rechecked).
