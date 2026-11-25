# Checkpoint HE-S, addendum 1 (2026-11-25, after publication)

Read with `CHECKPOINT_HE_20261125_S.md`. Where they differ, this file is the later one.

## Orphaned headless browsers (HE-S section 2 item 4)

**First increment for the successor (ADV, 2026-11-25): fix the producer, with a test that a killed parent leaves no browser.**

- Producer, from reading the code: `Cdp.__init__` in `framework/scripts/repurposing_view.py` starts Chromium with `start_new_session=True`, and only `close()` stops it. A Python process that is killed or timed out never reaches `close()`.
- ADV's suggested form: a watcher on the parent process, or a process-group kill. Not verified here, check before choosing: the Chromium found on this host is the snap one, and a Linux parent-death signal may not survive its launcher.
- The test must kill the parent of a real browser and show that no process with its profile directory is left. A test that only calls `close()` proves nothing about this.

**Cleanup of the existing trees: not done. It is on the operator's list.**

- The command that would have sent SIGTERM to the listed process identifiers was refused by Claude Code's automatic permission check (reason given: destructive or unwanted action). Nothing was signalled. Do not retry it and do not ask a peer to run it; ADV agrees.
- List and scripts, outside git: `files/coordination/he_orphan_browsers_20261125/` (`orphans_before.txt`, `candidates.json`, `orphans.py` read only, `stop_orphans.py`). 18 candidate trees, 180 processes, 847 MB proportional set size: parent gone, older than 24 h, temporary test profile, not in a live window's worktree.
- Correction to HE-S item 4: the processes this window stopped were three, all its own: 1489629 and 1490388 (its hung timing script) and 1523118 (its orphaned browser).
