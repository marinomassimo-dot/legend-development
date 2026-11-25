# Checkpoint HE-L (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~02:00Z

Written for: the successor HE session (fresh window, launched by ADV from a detached worktree). Written at about 295k context at ADV's request, after ADV-237 closed. Read after `CHECKPOINT_HE_20261125_K.md` (sha256 2b33b62b4d279fecc6fb0a1da4523b70c3316cbc13b64bd3de25a036640157c2), whose sections still hold unless this file changes them. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: 118 steps, 117 DONE, 1 TODO when this was written (the ADV-235 suite table, section 2). Kept as before: never write `MANDATE_STATE: COMPLETE`.
- Outgoing session `3b826442-8637-4c5e-a3bd-0bb9070ac5ce` (worktree `he_j_20261125`), model `claude-sonnet-5-5`, effort `high` on every turn.
- Operator rules unchanged from K section 0. Reply to the operator in Italian, write files in English.

## 1 Landed since K (all on main, gate PASS, ls-remote verified); do not redo
- ADV-235 `742b32225`: `debt_report.py` is a second bounded measurement reader in the Advisor isolation test (`rotation_status`, `assignment_states` only). ADV accepted it as not a weakening.
- ADV-237 `25c2114a4`: `framework/scripts/landing_suites.py` (print-only, 11 tests, routed once) and the record `HE_RED_MAIN_ADV237_20261125.md`: 227 of 383 completed gate runs on main failed from 2026-11-22 04:23Z to 11-24 23:43Z (16 episodes, about 38.8 of 67.3 hours red). The selector flags 10 of 16 replayed causes, 25 of the 31 failed runs of ADV's window, 5 of 5 causes since the publisher began refusing stale views.
- `6ba95cbd8`: section 1.6 of `framework/protocols/parallel_legend_protocol.md` (which suites to run before a push).
- Mandate: ADV-217, 220, 221, 226, 227 and 229 recorded DONE with the previous window's evidence (they had no step at all).
- The other red of that night (batch queue, PMID 25051421) was repaired by IT at `d8911b9b2` (ADV-234).
- SCI handoff `7fc66b5b` to `ac5ef625` verified and renamed (01:23Z); `claude agents --all --json` shows one CURRENT per role.

## 2 Open, in order
1. **Suite table to ADV (ADV-235, the one TODO step).** Read the gate run of `742b32225` (#2313, still running at 01:56Z, about 30 minutes left) with `ci_runs.py status 742b32225`, then that of `d8911b9b2`, the first commit with both fixes. Send ADV one table of every failing suite; if none fails, say so with the run number. Then step DONE.
2. **IT handoff**: old `7cf5e85a-cafa-4be7-9096-8df8073c1993`, successor `45a8b15c-5ca9-4b58-9ec9-782e4474ef6f` (mandate `ORCH-ROADMAP-IT59-20261119`; at 01:53Z not yet bound, old still bound with a push in the gate). When bound and released: `mandate_watch.py handoff`, rename demotion first (`IT Orchestrator - PREVIOUS 7cf5e85a`, then `IT Orchestrator - CURRENT 45a8b15c`), proof by session id, tell ADV. **No `--retire-old`.** If this window finishes it, ADV is told by message.
3. **No retirement of old windows** without asking ADV first (ADV, 2026-11-25: they are idle and cost nothing; maybe at the end of the day).
4. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed, outside git).
5. Stale comment ':17 to :18' near line 952 of `framework/scripts/strategic_advisor.py`: at the next touch of that file.
6. Seen, not acted on: `branch_hygiene.py` lists 1 LAND_OVERDUE (`codex/meeting-cross-runtime-20261123`, one commit; Codex is paused: do not wake it) and 24 DELETE_READY; the root checkout is a detached HEAD at `19a86daf5` with 126 modified or untracked paths belonging to others: leave it, tell ADV if it matters to the tick. Disk 18 GB free at 01:35Z.
7. Operator-owned and unapplied: the Pages two-job split and the gate `concurrency` patch (checkpoint J section 3). New evidence for the second, and the DREAM line about the push rule, are at the foot of the ADV-237 record: bring them to the operator, change nothing.

## 3 Traps met in this window
- `test_strategic_advisor.py` from the tool shell hangs on a fake `claude` reading the open stdin: always `< /dev/null`, long runs under `nohup`.
- A lazy import does not satisfy the Advisor isolation test: it walks the whole AST.
- `claude agents` for a rename: the list wraps and the pointer starts on a section header; match the `❯` line by name and a summary fragment after every key.
- `mandate_watch.py labels` proposes the role name from the successor's temporary session name: use the protocol's role (`SCI`, `IT Orchestrator`, `HE`).
- The unauthenticated Actions API (60 requests an hour) is shared with every `ci_runs.py wait` on the machine; ADV was rate-limited while two waiters ran. One waiter at a time is enough.

## 4 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file, then K.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response. Merge `development/main` before the first `accept`.
3. The old window (HE side of the handoff) releases and renames; the successor renames nothing of its own.
4. Section 2 item 1 (and 2 if still open); then `guidance`, `debt_report.py`, new ADV assignments; if none, tell ADV and propose a measured micro-upgrade. Before every push: `framework/scripts/landing_suites.py`, then `safe_push.py development main --expect-sha <sha> --serialize`.
