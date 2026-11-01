---
name: quiz-development
description: "Develop or extend an existing educational quiz, especially in Godot, without replacing the underlying game engine or breaking accessibility, data, progress, or other quiz modules."
user-invocable: true
---
# Educational Quiz Development

Use for a user-owned quiz app or an educational minigame. A quiz is a legitimate game workflow; adapt game roles to instructional correctness rather than combat/physics.

## 1. Protect the existing product
- Locate the real repository, root `project.godot`, existing QA, Git branch, engine version, and dependencies. Inspect `git status` before writing. No destructive cleanup of existing work.
- Read `project.yaml` if this repo uses CCGS. If not, do **not** insert unrelated CCGS configuration into another engine.
- Read `.claude/agents/game-designer.md`, `.claude/agents/lead-programmer.md`, `.claude/agents/godot-specialist.md` (when applicable), `.claude/agents/accessibility-specialist.md`, and `.claude/agents/qa-tester.md` on demand for the task. Use the real engine and language.
- Preserve the user's shared quiz engine, original gameplay and UX, names/translations, saved progress format, offline content and audio/TTS; prefer the smallest focused change.

## 2. Define a small story and proof
- Identify the user-visible behavior to change, an acceptance criterion and regression risk.
- Write a **failing behavior test first** whenever feasible. Favor deterministic randomness/fixtures over flaky timing tests.
- When building multiple-choice questions, assert exactly one correct answer, distinct options, plausible distractors from the same class, and no repeated options. Check both question direction modes.
- Never invent educational facts. Use documented content provenance and consider localization and age appropriateness.

## 3. Implement and verify
- Change one behavior at a time on a fresh branch/worktree or separate sandbox. Don't reset or overwrite unrelated user changes.
- Run the original tests and the new targeted behavior test. For Godot use the actual executable and the root project with `--headless --editor --quit` then a scene/test runner when available.
- Check touch UI, accessibility, audio/TTS, navigation and persistence for regressions.
- For visible changes capture a real game screenshot/observation; a headless exit code is **not** a visual test.

## 4. Report
Present paths, exact commands + exits, PASS/FAIL/NOT RUN, and next manual checks. Commit/PR only when authorized. Keep completed artifacts and evidence within the project, not in a parallel studio state. Invoke `quiz-qa` before declaring the work complete.
