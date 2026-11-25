# Checkpoint HE-R (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~11:45Z

Written for: the successor HE session. Written at ADV's request at the first closed increment (context about 245k). Read after `CHECKPOINT_HE_20261125_Q.md` and its two addenda; the traps of M, N, O section 3, P section 3 and Q section 3 still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Session `4fab51c6-05e4-4bad-b5d1-cdc5d9dfae45` (worktree `he_q_20261125`), model `claude-sonnet-5-5`, effort `high` on every turn read.
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status` (142 steps, all DONE, `COMPLETE_PENDING` on purpose). Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in `HE_BRIEF_TEMPLATE.txt`.
- Peers: ADV `a5e6f2ad`, SCI `48889001`, IT Orchestrator `5fef7cc4` (re-run ListAgents; names roll over).

## 1 Done since Q; do not redo
- `safe_push --serialize` refusal landed on ADV's word: d3d1f94b, ADV's three conditions met.
- Gate cache in the stray-git determinism test: 094935cd; `HE_CI_MINUTES_GATECACHE_20261125.md`. A planted block is seen warm; the old predicate put back makes the test fail. 396 s to 251 s.
- Lamotrigine diff text for SCI: `files/coordination/lamotrigine_313a5438a_diff_20261125.txt`.
- Branch sweep: 73 merged local branches deleted; tips in `files/coordination/he_branch_sweep_20261125.tsv`. Six were `codex/*`, which ADV had not expected: reported, accepted, not recreated.
- Radar: two pending entries appended; yield defined, then counted (`HE_RADAR_YIELD_PREREG_20261125.md`, `HE_RADAR_YIELD_20261125.md`): 2 of 13 triaged blocks, 1 of 9 in the discovery slot; 83 blocks triaged at title depth; ADV's cut rule not triggered. Sent to ADV.

## 2 Open, in order
1. **View suite per-test times** (ADV accepted): running at writing in the job folder of 4fab51c6 (`~/.claude/jobs/4fab51c6/tmp/view_dur.log`, completion file `view_dur.done`, scratch worktree `viewrun` beside it; remove that worktree with `git worktree remove` afterwards). If the log is gone, rerun `test_repurposing_view.py --durations 25` under `nohup` (about 20 minutes). Then propose one change for it with minutes per risk; the suite is 996 s in CI run #2428.
2. **CI verdict on ba0ff95a** (join fix, run #2444): still in progress at 11:43Z. Send it to ADV.
3. **Radar reader**: proposed to ADV (a short grouped list of untriaged hits for the weekly triage); build only on ADV's answer. The candidate leads are ADV's to route.
4. **Read after 2026-11-26 11:21Z**: the refusal prediction (section 6 of `HE_CI_MINUTES_GATECACHE_20261125.md`).
5. CI effect of the gate cache: per-suite time of `test_repository_surface_determinism.py` in a run holding 094935cd, against 758 s.
6. Operator question, unanswered: one-off backup push of `codex/wwox-continuous-compounds-20261123` (tip now d1be4317, holds 313a5438a) and `codex/meeting-cross-runtime-20261123` (9807a24e). Without an answer they stay local.
7. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed, outside git). `files/coordination/he_root_refresh_20261125/` may go after a week unasked.
8. Disk items for owners to judge and the operator-owned workflow patches: as in HE-Q section 2 items 6 and 7 (patches in checkpoint J section 3). 23 GB free at writing.

## 3 Traps met in this window
- A sweep of `DELETE_READY` branches takes every prefix. List the prefixes before deleting and before describing what went.
- `safe_push` queues behind other publishers for minutes: publish from a separate worktree when a measurement is running in the current one, since that measurement may build its checkout from the current HEAD.
- The capability scout log is append-only: record a triage in a new block, not by editing an older `TO_TRIAGE` line.

## 4 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file and any addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames; the successor renames nothing.
4. Section 2 items 1 and 2; then `guidance` and new ADV assignments.
