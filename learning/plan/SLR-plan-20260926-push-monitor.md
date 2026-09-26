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

The daily publication check marked every dirty worktree `UNPUBLISHED`, including detached
test worktrees with local fixtures. It now reports dirty branch worktrees as actionable
and lists dirty detached worktrees in a separate field for inspection. A real-Git test
proves both cases and the status change after branch work is cleaned.

The Harness Engineering contract still listed every push as operator-reserved. Its
wording now points to §21d's development-repository push exception; the canonical rule
remains in `LEGEND_CORE.md`.

## Learning and impact

Git's `worktree list --porcelain` carries branch attachment explicitly. A publication
monitor should use that information before converting dirt into a task alert, while
retaining detached dirt as observable state. The change reduces a false daily alert
without hiding a detached checkout.

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

- Keep detached dirt visible but outside `UNPUBLISHED`; the alternative of ignoring it
  entirely would hide possible unique material. Revert the script, test and README hunk
  if this classification proves wrong.
- Correct only the stale role pointer; the alternative of copying the push procedure
  into the role would create a second rule home. Revert the role hunk if §21d changes.
- No other actor was consulted; §21e makes this an ordinary T0 Harness change.

No scientific current file, reading status or inference was changed.
