# Checkpoint HE-AA (Harness Engineering, ACTOR_ID plan), 2026-11-28, written at ADV's request

Written for: the successor HE session. The traps of `CHECKPOINT_HE_20261126_Z.md` and the checkpoints it names still hold.
Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `888b4b03-f8d1-42d1-b0d0-22fb994aeaa0` (worktree `he_z_20261126`, branch `task/he-z-20261126`), model
  `claude-sonnet-5-5`, effort `high`; peak context about 308k with one compaction.
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status`. The CI-red read and
  ADV-293 are DONE with evidence; one step remains, 168: read the HE token-yield brief
  (`files/coordination/adv-codex-loop/HE_TOKEN_YIELD_PILOT_20261128.md`) at the first normal resumption after the weekly quota reset.
  Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in `HE_BRIEF_TEMPLATE.txt` and Z section 0: no spend, no contact
  with authors, never send the operator e-mail to a service, Codex PAUSED (do not wake or touch its processes), a classifier denial is
  not retried in another form, workflow patches and the Pages workflow operator-reserved, never commit while a safe_push waits.
- Peers at writing: ADV `a5e6f2ad`, SCI `fc428159` (successor, worktree sci_av), IT Orchestrator `54ca757b` (re-run ListAgents).

## 1 Done in this window; do not redo (all on main unless marked local)
1. **ADV-293** blind check of the eight unchecked ADV-098 sheets: six blind readers, every error verified by HE: **34 of 305 strict
   (11.1 percent, exact CI 7.8 to 15.2), class T 23 of 185 (12.4)**; the bar recorded by ADV for RP-005 is 11.1 overall and 12.4 on
   held-row units. Result: `advisor_pilot_20261113/adv098_agent_sheets_he_20261119/blindcheck_adv293_he_20261126/RESULT_ADV293_HE_20261126.md`.
   One corrected line reaches a card: M01 tazemetostat; the sentence file for IT is `IT_SENTENCE_M01_tazemetostat_exposure_20261126.md`.
   Recipe rules 6, 7 and 8 added to `RECIPE_pull_activities.txt`.
2. **ADV-296** scan for "negative beside an unread citation": the frozen method REJECTED (misses a known case); the post-hoc V2 found 5 of 20
   by blind read, none a clean new error; script discarded, note kept (`negcheck_adv296_he_20261126/RESULT_ADV296_HE_20261126.md`).
3. **CI-red read** (history only): 0 gate failures in 152 runs since 2026-11-26 11:21Z (52 percent before); 18 Pages-workflow failures,
   operator-reserved, logs need auth (`HE_CI_RED_READ_20261128.md`).
4. **ADV-299** (disk): trace and leak fix: `disk_adv299_he_20261128/RESULT_ADV299_HE_20261128.md`. The swings are the landing gate's own
   clones (sawtooth of 0.5 to 0.9 GB), the Codex rollout writes a steady 13 MB per minute underneath. New tools: `disk_writer_trace.py`
   (+ test), `browser_scratch.py` (+ test; `Browser` test class now removes its profile). COMMITS b6c8601e5 and 3f576e5b3 may still be LOCAL:
   check `git log development/main..HEAD` first; push once df shows 2.0 GB.
5. Pushed this window: ab1ad408a, a3ea24914, 8c1b6783e. ADV renamed the SCI windows itself (my rename was classifier-denied; not retried).

## 2 Open, in order (queued, none started)
1. Push the local commits (df at least 2.0 GB; `safe_push --serialize`; never `--no-landing-suites`).
2. **Micro-upgrade `task_close.py` refusing when no worktree holds main** (output under 1 MB), after the push.
3. **Recount-script check:** the eligible/completable recount of the four adv265/adv280 scripts (`rank_held_partials_adv265.py`,
   `containment_adv265.py`, `count_adv280.py`, `content_check_adv280.py`) has no single tested script; `consumer_count.py` does NOT cover it.
   Low priority; read before building (ADV's call).
4. **2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/`** (sealed custodian folder; operator rule stands).
5. Step 168 (token-yield brief) after the quota reset. Copied-sentence check on the next card-changing landing (IT's M01 edit when it lands).
6. Standing: the gate cache, the 4-worker CI line and the workflow patches stay operator-reserved; the Pages failures are theirs.

## 3 Disk: what the operator decides (report-first; nothing was deleted by HE)
Free space swung between 0.5 and 3.0 GB all day; `safe_push` needs 2.0 GB. Measured 2026-11-28 (unique inodes, du):
1. `files/geo/GSE92742/...Level5_COMPZ...gctx.gz` **19.9 GB** (the archive; the 21.8 GB `.gctx` beside it is what scripts read; the `.gz` is the only
   copy checkable against `GSE92742_SHA512SUMS.txt.gz`): the single biggest lever.
2. uv cache and the q230p `.venv` (about 7.7 GB, from 11-26). 3. `~/legend_browser_tmp`: 247 stale `tmp*` profiles (1.7 GB; deletion was classifier-refused for ADV).
4. `~/.claude/jobs` scratch: about 1.9 GB of identifiable old downloads (5fef7cc4 adv275 data, 961aabbb s.zip, 9945c156 cellosaurus, others; sizes in the 11-28 message to ADV).
5. 28 orphan headless Chromium processes (about 2 GB memory; 22 older than 66 h, 4 started after my watcher with no watcher alive: amiloride x2, eeg-verify x2; launcher outside the repository).
6. The Codex app-server (pid 500783) rollout, 587 MB and growing; Codex stays PAUSED. 7. Worktree removal (operator file `HE_WORKTREE_REMOVAL_FOR_OPERATOR_20261126.md`, classifier-stopped; not to be run by anyone).

## 4 Traps met in this window
- New file with a shebang and no execute bit fails `test_release_surface` and refuses the landing: write new scripts without a shebang.
- A new tool needs a README row; a module with no `__main__` goes in the library-module table, else `test_tool_routing` fails.
- A frozen PREREG method that misses a known case is REJECTED; a post-hoc variant that fits the known cases is not a validation.
- Do not commit while a safe_push waits; the gate refuses under 2.0 GB free and a refusal is not retried with a bypass.
- A reader's MUST CHANGE is verified from the original before it counts; regrade judgement calls openly (U4.1, U12.8, U12.62, U11.16).
- Blind readers cannot see the repository: UNSETTLED is not "OK"; count only assessable units.

## 5 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE sections 21c to 21e, this file.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response; merge `development/main` before the first accept.
3. The launcher renames; the successor renames nothing. 4. Section 2 item 1, then 2.
