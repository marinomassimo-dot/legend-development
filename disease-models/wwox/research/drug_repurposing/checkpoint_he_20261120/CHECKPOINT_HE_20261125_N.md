# Checkpoint HE-N (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~05:45Z

Written for: the successor HE session. Written above 360k context at ADV's request. Read after `CHECKPOINT_HE_20261125_M.md` and its addendum; M section 3 (traps) still holds, and M section 2 items 1 and 3 are closed here. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status` for the counts. Never write `MANDATE_STATE: COMPLETE`.
- Outgoing session `9884af3f-28a6-4ca5-99d0-77239ef08663` (worktree `he_m_20261125`), model `claude-sonnet-5-5`, effort `high` on every turn.
- Operator rules unchanged from checkpoint K section 0. Reply to the operator in Italian, write files in English.

## 1 Done since M; do not redo
- Campaign home (M section 2 item 1): `assign` and `deliver` refuse when the checkout is behind main on an input, and `strategic_advisor.py refresh` brings the home current (5e37a5f18); `refresh` re-appends local-only assignment rows after the fast-forward (b63c22e61). Advisor role file and skill reworded. ADV accepted the review.
- Checkout-behind lines in `tick` and `mandate_watch` (M item 3): 35e355c40.
- ADV's first real dirty-root `refresh` (05:16Z): 9e32fd307 to 5d0aa3aca, 3 files already on main replaced with copies, nothing kept; no re-append case has occurred yet.
- ADV-258 weekly notice sweep: the existing `epmc_notice_sweep.py` extended with `--catalogue`, called weekly by `scout_daily.py`; a869a52b6 (also repairs a red `test_documented_commands` caused by the assignment brief). Live run 05:13Z equals SCI's 29 rows. One proposed flag, not applied: PMID 19357348 (notice 42583763); ADV forwarded it to the next harvest.
- Flow flag: 'TAKEN, no output' is no longer raised once a recipient record holds a DONE step with the id (ADV-226).
- `safe_push.py --landing-suites`: opt-in, prints each selected suite's result before the gate, never refuses on a red one. It holds the landing lock while the suites run.

## 2 Open, in order
1. CI #2353 (f0daa021) concluded failure on two other suites, `test_candidate_tree_freshness.py` and `test_ranking_it8.py`; the closed-world red is gone. Cause: 385eb88c9 (HE ADV-245) changed `needs.json` without regenerating the ranking. `--regenerate-derived` could not repair it (it committed `ranking.json` and left `unit_inputs.tsv` dirty): fixed after this checkpoint's first draft, same landing as this file. Main passed both suites locally at ff53de07b; read the CI verdict of that line (`ci_runs.py status ff53de07b`) and send it to ADV.
2. The weekly notice sweep ran from cron at 05:32Z and wrote its state; nothing to do. Asked ADV, unanswered when written: make regeneration the default under `safe_push --serialize` (`--no-regenerate-derived` to opt out), because without the flag nothing checks the ranking.
3. Pages run #116 on f0daa021 ended in failure: operator-reserved, reported to ADV, not re-run.
4. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed, outside git).
5. `files/coordination/he_root_refresh_20261125/` may go once nobody has asked for it for a week.
6. No retirement of old windows without asking ADV. No `--retire-old`.
7. Operator-owned and unapplied: workflow patches (checkpoint J section 3). Do not edit LEGEND_CORE 21d or 21e.
8. Disk 21 GB free at 05:12Z; below 15 GB, report-first cleanup.

## 3 Traps met in this window
- `git show origin/main:<path>` before `git fetch origin` gives an empty hash: a stale ref, not a mismatch.
- An assignment brief naming a not-yet-written script with its folder turns `scripts/test_documented_commands.py` red on main.
- Before building an ADV tool, search `framework/scripts/README.md` for the question: `epmc_notice_sweep.py` already existed.
- Europe PMC gave 503 and read timeouts for about an hour; the catalogue pass then took 11 minutes.
- Importing a module from a tool writes `__pycache__` into the tree that `safe_push` is about to judge: set `sys.dont_write_bytecode` around the import.
- A generator can rewrite files its declaration does not list; compare what it dirtied, not what is declared.
- Landing suites run with `bash -e` stop at the first red: rerun the whole list after a fix.

## 4 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file, then M and its addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response. Merge `development/main` before the first `accept`.
3. The old window releases and renames; the successor renames nothing of its own.
4. Section 2 items 1 and 2; then `guidance`, `debt_report.py`, new ADV assignments. With none, tell ADV and propose a measured upgrade. Before every push: `landing_suites.py`, then `safe_push.py development main --expect-sha <sha> --serialize`.
