# Checkpoint HE-Q (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~10:50Z

Written for: the successor HE session. Written at ADV's request (context about 300k, this window's own). Read after `CHECKPOINT_HE_20261125_P.md`; the traps of M, N, O section 3 and P section 3 still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `9229d112-45b3-4987-b285-e0e426d4bdff` (worktree `he_p_20261125`), model `claude-sonnet-5-5`, effort `high` on every turn read.
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status`. Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in `HE_BRIEF_TEMPLATE.txt`.
- Peers at writing: ADV `a5e6f2ad`, SCI `48889001`, IT Orchestrator `5fef7cc4` (re-run ListAgents; names roll over).

## 1 Done since P; do not redo
- ADV-274, red streaks counted: `HE_RED_STREAKS_ADV274_20261125.md` and its PREREG; two selector rules (batch queue on `*_current.md`; `test_repurposing_join.py CuratedLink` on the mechanism map); published 6dcfa4935. ADV consumed it.
- Main was still red on the join after IT's title/card fix (found by HE, told IT and ADV). CI #2434 (d5dcab27): failure on `test_repurposing_join.py` only.
- First per-suite CI times, #2428 (f093ab03), sent to ADV: 3385 s over 276 suites; view 996 s, surface determinism 758 s (52%); job 72 min = regression step 3750 s + gate 510 s.
- Disk report-first cleanup (ADV): one worktree removed (`he_h_20261124`, idle 26 h, integrated, clean). `tmp_clone_report`: 0 removable. Free 16 GB.

## 2 Open, in order
1. **Land the refusal, on ADV's word only**, after IT's join fix `a86667e8c` is on main (it was not at 10:49Z). Branch **`task/he-landing-refuse-20261125`**, commit `338ed811a`, local to this repository (not pushed: one branch, no backup push). `safe_push --serialize` runs the selected landing suites by default and refuses a push that turns one red.
   - ADV's conditions: refuse only a NEW failing test; the same failing tests at the remote tip print `PRE-EXISTING RED` with their names and the push goes on; the empty skip-trailer commit only with `--no-landing-suites`; the push log's first line tells every actor for one day; self-test with the three replays, a clean diff and a pre-existing red case. ADV puts it on the operator's list as its harness decision.
   - Update `NOTICE_UNTIL` (now `2026-11-26`) to one day after the real landing date.
   - Unit suite `test_safe_push.py`: 42 OK before the last message change; the `SafePushLandingSuites` class (9) re-run OK after it.
   - Replay of the new function on real landings, current selector, real suites, scratch clone: **#2353 REFUSES** on exactly the two causing suites (381 s with the base reruns); **#2404 REFUSES** on exactly the two causing suites (119 s; a first try was wrong because my script copied the selector with a 644 mode); **#2421**: `CuratedLink` red, verdict pending; **clean #2392 to #2393**: pending. If they are not in an addendum, rerun them: scratch clone at the causing run's head, copy the current `landing_suites.py` with `shutil.copyfile`, import `safe_push` with `LEGEND_SAFE_PUSH_ROOT=<clone>`, call `landing_check(<previous run sha>)`. #2420 `aee69938a` to #2421 `ab80dc739`.
   - Then `landing_suites.py`, push with the new tool, mark the BLOCKED step DONE, tell ADV.
2. After the join fix lands: send ADV the CI verdict of the first run holding it.
3. ADV's step "which suites hold the minutes, one change by minutes per risk": proposal not sent yet. Measured locally (shared host): in `test_repository_surface_determinism` the single test `test_a_stray_git_file_cannot_suppress_a_real_block` took **503 s** of about 760; it runs the full publication gate twice. Candidate change: both calls with `--cache` and `LEGEND_GATE_CACHE_FILE` in a temporary folder (the wikilink scan it asserts always runs in full). A cold/warm timing of the gate was running at writing; if no figure is in an addendum, time it. View suite per-test times were also still running.
4. Operator question, open, unanswered: one-off backup push of `codex/wwox-continuous-compounds-20261123` (313a5438a) and `codex/meeting-cross-runtime-20261123` (9807a24e8)? Without an answer they stay local.
5. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed, outside git). `files/coordination/he_root_refresh_20261125/` may go after a week unasked.
6. Disk left for owners to judge: `/tmp/it55_a` (419 MB, linked worktree whose parent is gone, 9.8 days); input folders under `/tmp` (about 4 GB); IT's task worktrees with no session of their own (`it_17b`, `it_17c`, `it_adv266`, `it_adv268`, `it_fu`): ask IT. `he_g_20261123`, `it_successor_n_20261120`, `p022b` have processes in them.
7. Operator-owned and unapplied: workflow patches (checkpoint J section 3). Pages run #120 on d5dcab27 failed: reported, not re-run. Do not edit LEGEND_CORE 21d or 21e. No `--retire-old`.

## 3 Traps met in this window
- GitHub keeps at most 10 `release regression` annotations per step: a failing-suite list can be cut; bisect locally.
- A helper named `bisect.py` shadows the stdlib module; `shutil.copy` copies the mode bits.
- The old `--landing-suites` passed a class entry as one file name (fixed on the branch).
- A red main reaches publishers as a selected suite already failing: any refusal must compare with the tip.

## 4 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file and any addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames; the successor renames nothing.
4. Section 2 items 1 to 3; then `guidance` and new ADV assignments.
