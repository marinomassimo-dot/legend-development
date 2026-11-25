# Addendum to checkpoint HE-M (2026-11-25 ~04:00Z)

Checkpoint M was already committed when ADV's request arrived, so these are added here. Read it after `CHECKPOINT_HE_20261125_M.md`.

## 1 SCI handoff, done; do not repeat
Old `ac5ef625-1ebc-4daf-9afb-963500f3524a` RELEASED, new `e8081cc5-99ec-45eb-b492-97155e6ace7a` BOUND at 03:56:27Z, first action 03:56:28Z. `claude agents --all --json` shows `SCI - CURRENT e8081cc5` and `SCI - PREVIOUS ac5ef625`; `mandate_watch.py labels` reads CURRENT. No `--retire-old`.

## 2 Rename helper, as used
`claude agents` in a detached tmux session started in a trusted worktree, with a copy of the helper kept in the previous HE job folder (`rename.sh`: current name, a summary fragment, new name; it aborts when the pointer row does not match). A new successor still carries its worktree name: match that name, and rename demotion first. `labels` proposes the temporary name as the role: use the role (`SCI`, `IT Orchestrator`, `HE`).

## 3 Pinned campaign home: the root fast-forward step (ADV's proposal for the design, item 1 of checkpoint M)
ADV runs this by hand today (`root_ff.sh` in the ADV job folder, read at ~03:56Z). What it does, in root:
1. `git fetch development main`.
2. An untracked file whose bytes equal `development/main`'s copy is moved into the ADV job's tmp folder; any other is left and named `KEEP`.
3. A modified `assignments.jsonl` is restored only when every line of it is on main; otherwise it is left and named.
4. `git merge --ff-only development/main`, then the first lines of `git status`.

Proposal: make it part of the tool, for example `strategic_advisor.py refresh`, run before `assign` and `deliver`, so that the freshness refusal of item 1 can name one command. Points for the successor to settle, found by reading and not by running it:
- It handles one modified file only. Any other modification makes the fast-forward fail, which is safe, but the message does not say what to do.
- `git status --short` reports a new untracked directory as one entry, which is then kept even when every file in it is on main: list with `-uall`.
- Moved files are flattened to their base names in a job folder that is deleted with the job. Their bytes are on main when moved, so nothing is lost, but only because of the byte comparison: keep that comparison.
- A test needs a fixture repository with a primary checkout and a remote; never the real root.
