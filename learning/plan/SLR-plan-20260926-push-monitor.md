---
record_type: SESSION_LEARNING_REVIEW
date: 2026-09-26
actor_id: plan
role: Harness Engineering
runtime: Codex
task: task/he-push-monitor
classification: MICRO_UPGRADE
scope: development publication monitoring and role routing
status: LOCAL
---

# Development push monitor: distinguish task work from scratch state

## Work completed, problem, solution

The daily publication check marked every dirty worktree `UNPUBLISHED` without showing
whether it was a task branch or detached. It now lists the two groups separately for
inspection; both retain the alert because detached work may be unique. A real-Git test
proves both cases after branch work is cleaned.

The Harness Engineering contract still listed every push as operator-reserved. Its
wording now points to §21d's development-repository push exception; the canonical rule
remains in `LEGEND_CORE.md`.

## Learning and impact

Git's `worktree list --porcelain` carries branch attachment explicitly. A publication
monitor should report that information so an actor can identify a detached test fixture
quickly. Branch attachment alone cannot prove that detached changes are disposable,
so the overall alert remains conservative.

`LEARNING_INDEX` was checked before filing and is still absent (`ANNEX_INDEX.md` marks it
pending). This record has no `LEARNING_ID`, confirmation class or promotion claim; it is
one local observation and implemented micro-upgrade.

## Evidence and verification

- `framework/scripts/test_daily_push_check.py`: 5 tests pass, including named and detached
  worktrees in a disposable real Git repository.
- `scripts/test_release_surface.py`: 11 tests pass; `scripts/test_tool_routing.py`: 7 pass.
- `legend_lint.py .`: WARN, no BLOCK; `fulltext_receipts.py verify`: 236 chained receipts OK.
- The full fresh-clone regression comparison and exact-SHA publication gate are recorded
  in the session closure report after the final commit.

## Decisions taken

- Keep detached dirt visible and within `UNPUBLISHED`; the first implementation removed
  the alert based on detachment alone, which could hide unique material. Revert the script,
  test and README hunk if separate reporting proves unhelpful.
- Correct only the stale role pointer; the alternative of copying the push procedure
  into the role would create a second rule home. Revert the role hunk if §21d changes.
- No other actor was consulted; §21e makes this an ordinary T0 Harness change.

No scientific current file, reading status or inference was changed.
