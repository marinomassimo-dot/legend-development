# Checkpoint HE-T (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~15:35Z (context past the restart line; ADV asked for it at once)

Written for: the successor HE session. ADV asked for the handover when the 4-worker run ended. Read after `CHECKPOINT_HE_20261125_S.md` and its addendum 1; the traps of M, N, O section 3, P section 3, Q section 3, R section 3 and S section 3 still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `43ab579f-1f7c-41dd-9020-1cfa336c00dd` (worktree `he_s_20261125`, branch `task/he-s-orphan-browser-20261125`), model `claude-sonnet-5-5`, effort `high` on every turn read.
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status`. Two steps stay open on purpose: the read of section 2 item 1 and the disk survey (item 2). Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in `HE_BRIEF_TEMPLATE.txt`.
- Peers at writing: ADV `a5e6f2ad`, SCI `0d0c6dc3`, IT Orchestrator `df7283c4` (re-run ListAgents; names roll over).

## 1 Done since S; do not redo
- **Orphaned headless browsers, producer fixed** (a2b46d713, CI #2470 success): `Cdp` starts a watcher process that holds a pipe only the owner writes; end of file kills the browser's group and removes the profile. Tests SIGKILL the parent's whole group, with a fake browser and with the installed one; both failed on the old code. **The existing orphans were not touched** (operator).
- **A landing red outside its diff** (same commit): meeting recovery ordered two records of one start second by file time; the open one now ranks first. ADV: the long-open meeting record is deliberate, and ADV refreshes the root itself.
- **Card checkers** (33e2b73a1): `landing_suites.py` selects each card folder's checker for its folder and for `repurposing_bridge.py`. Mutation both ways with `safe_push.landing_check`. Limit: if a checker were already red on the tip, only its last printed line is compared.
- **Card checkers as a suite** (`framework/scripts/test_card_checkers.py`, in this landing): CI never ran the real checks of `cards_early/`.
- **CI verdict time** (`HE_CI_QUEUE_20261125.md`): the run itself (serial suites, median 58 min); a runner queue of 8 to 19 min only with 23 to 25 runs open.
- **Opt-in parallel runner** (in this landing, default off): `--jobs N` or `LEGEND_REGRESSION_JOBS`. Section 5 of the CI note holds the first pair; the repeat took 1,536 s with one red, a race inside `test_verify_run.py`, fixed in this landing (section 6). Both runs are over; nothing of HE's is still running. The trial clone is removed.
- **CI effect of the two test changes** (HE-S item 3, closed): `test_repository_surface_determinism.py` 358, 489 and 364 s in #2460, #2457, #2465 against 758 s in #2428: the change shows. `test_repurposing_view.py` 677 s in #2465 (holds the A4 change) against 687 and 942 s in runs without it: the A4 change is inside the noise in CI.
- CI #2461 success (told to ADV).

## 2 Open, in order
1. **Read after 2026-11-26 11:21Z** (ADV, in the mandate record): the refusal prediction (section 6 of `HE_CI_MINUTES_GATECACHE_20261125.md`), and **how many CI reds in that period were on suites the default selection DID run**. ADV: that number decides whether the rule stays.
2. **Disk survey** (ADV 15:15Z, report only; ADV decides the cleanup): `HE_DISK_SURVEY_20261125.md` holds the first survey (15:29Z, free 20.0 GB; 21.2 GB after HE removed its own clone). **Open:** a second survey for growth per hour, and the safe-to-remove list with its rule per item. Scripts and raw data: `files/coordination/he_disk_survey_20261125/` (`disk_survey.py OUT.json HOURS`, about 2 min; `disk_summary.py OUT.json agents.json`, agents from `claude agents --json --all`).
3. **One clean 4-worker run is owed** before the workflow line goes to the operator (none made since the race fix): a clone of main outside any dot-directory, `python3 -B scripts/run_release_regressions.py --jobs 4` under `nohup`, about 25 min.
4. CI: at 15:29Z #2475 and #2476 had run 1h08m and 1h02m, 7 runs open, none queued (within the 46 to 74 min of the note).
5. **Operator list** (ADV carries it): the one-line workflow change `LEGEND_REGRESSION_JOBS: "4"` (section 5 of the CI note); the cleanup of the orphaned browsers (list and scripts in `files/coordination/he_orphan_browsers_20261125/`; on 2026-11-25 14:16Z there were 24 orphan trees, the oldest list covers 18); the `codex/*` backup push (HE-R section 2 item 6); the patches of HE checkpoint J section 3.
6. If the operator enables the parallel runner: read `ci_runs.py times <sha>` and the step time of the first runs; a red that a serial run does not reproduce is one `RUN_ALONE` entry. The next lever would be splitting `test_repurposing_view.py`, which bounds the parallel phase.
7. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/`. The rest of HE-R section 2 items 7 and 8.

## 3 Traps met since S
- Do not edit or add a file in the worktree while your own `safe_push` waits: build and test in a separate clone under a non-hidden folder of the home (snap Chromium cannot read dot-directories).
- A suite red outside your diff at landing: read the failing test before running again.
- A new test file with a shebang needs mode +x (`test_release_surface.py`); a new `.md` widens the landing selection.

## 4 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file and any addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames; the successor renames nothing.
4. Section 2 item 2 first (free space falls toward the 15 GB trigger), then item 3.
