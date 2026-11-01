---
name: quiz-qa
description: "Audit and test an existing educational quiz: data correctness, answer generation, scoring, retries, audio/TTS, UI accessibility, persistence and Godot run checks."
user-invocable: true
---
# Quiz QA — behavior before appearances

Do not call a quiz tested merely because it starts or its source contains a matching string. Detect broken rules and prove results with executable tests.

## Required matrix

| Area | Minimum evidence |
|---|---|
| Dataset | unique IDs, correct asset paths, complete required translations, no duplicate/blank options |
| Questions | every generated question has exactly one valid answer; no duplicate choices; both normal and reverse modes |
| Scoring | correct scores once, wrong scores zero, repeated clicks/calls cannot rescore, transition cannot skip or double-save |
| Round lifecycle | start, progress, finish, replay, exit, empty and short sets |
| Persistence | one completed record per round, stable old save schema, no accidental personal data |
| Accessibility | audio/TTS works when supported, graceful fallback when unavailable, visible focus and accessible controls |
| UI and devices | mobile aspect ratios, long names, missing assets, no clipping or layout overflow |
| Regression | launch existing app; run its pre-existing tests before and after the edit |

## Method
1. Inspect code/state and list current tests. Run baseline. Check full project engine version, runtime and real input state.
2. Design positive, negative, boundary and re-entry cases. Reproduce at least one important failure with a deterministic test; a test that merely greps code does not establish behavior.
3. Execute with Godot's GDScript test runner, GUT, GdUnit4, or focused built-in SceneTree scripts. Mock or disable TTS and persistence side effects when testing pure quiz behavior.
4. If an editor scene is rendered, check with an actual screenshot or user playtest. Treat headless tests separately.
5. Every outcome: PASS, FAIL, or NOT RUN, with test names, outputs and exact commands. Report limitations (especially TTS on Linux, which may need Windows/Android verification). Never equate absent engine with a successful test.

### First useful regression for repeated answer
After the first selection locks the question, invoking the scoring handler again (even with a different choice) must leave score, displayed feedback and recorded completion count unchanged. Check separately that re-entering a new quiz unlocks the new question.

If the user already authorized the exact code changes, continue without redundant requests; do not modify an unrelated project or publish to production.
