# Checkpoint HE-AH (Harness Engineering, ACTOR_ID plan), 2026-11-28 about 14:10Z

Written for: the successor HE session (ADV launches it), past the context line (244k at the ADV-329 push). The traps of
`CHECKPOINT_HE_20261128_AG.md` and of the checkpoints it names still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `4441b7bf-5232-4f96-a432-2a71e111bab6` (worktree `he_ag_20261128`, branch `task/he-checkpoint-ah`), model `claude-sonnet-5-5`, effort `high`.
  It stays open until the successor is bound, then releases when asked. No delegate running; the CI monitor for run #2897 may still be armed.
- Mandate `PLAN-HE-CONTINUITY-20261118`: 195 steps, TODO 0, DONE 193, BLOCKED 2 (step 166 classifier, step 182 dated). `mandate_continuity.py status`
  says ALL_BLOCKED; never write `MANDATE_STATE: COMPLETE`. New work arrives as an ADV assignment: `mandate_continuity.py accept` with one distinct `--source` each.
- Reply to the operator in Italian, write files in English. Codex lane PAUSED. Peers change names: run ListAgents before each message
  (ADV - CURRENT a5e6f2ad, SCI - CURRENT ba384503, IT Orchestrator - CURRENT 1c914d1b at 14:00Z).

## 1 Done in this window; do not redo (all on `development/main`)
- AG items closed: bind verified; README shareable-view suites `DeepenedCasesShareable ShareableAudit It6P13Data It21P7InvestigationsContext` = 66 tests OK,
  606 s, at `36d928964`, started at load 2.4.
- **ADV-326** (`750ac814a`): blind extraction, Cheng 2020 Fig 7c and Wang 2012 Fig 1d, 1e, 4b, `brainstorm_20261116/adv326_blind_gsk3_he_20261128/TABLE_ADV326_HE.md`.
- **i18n test** (`36d928964`): `test_repurposing_view_i18n.py` read a nested section's notice as `overview`'s own (a test defect). The CI release gate ran red on it
  from #2883 to #2891; the fix is in run **#2897**, still in progress at 14:07Z. Read its conclusion (`ci_runs.py status 36d928964`); it is IT's and ADV's to know.
- **Tick cost** (`a545cb9de`): `strategic_advisor.py tick` 49-53 s to 9 s; `assignment_states` walked every task record per assignment. Output identical on 327
  assignments, 240 tests OK. Root checkout was fast-forwarded by ADV.
- **ADV-329** (`9e83bb65e`): blind reading of Repudi 2021, `brainstorm_20261116/adv329_blind_repudi_he_20261128/TABLE_ADV329_HE.md`. Text level only (no
  figure image viewed); one delegate stopped by the classifier on its first Bash call, not retried.

## 2 Open, in order
1. **CI #2897** (fix for the i18n red): read the conclusion; if red on another suite, reproduce at the merged tip before touching anything.
2. **ADV-329 gap, optional:** figure images of Repudi 2021 (weights by day, Fig 4 P values, Supp 6B direction) were not viewed. Do it only if ADV asks.
3. **2026-11-29 or later:** recheck and delete `files/adv174_negraes_custodian_he/` in the root checkout (sealed, outside git). Step 182, BLOCKED on the date only.
4. **Worktree removal is frozen** (ADV, 2026-11-28) until the operator decides; obey `branch_hygiene.py --removal`, never `git status` alone. Step 166 stays BLOCKED.
5. Operator items, not HE's to decide: the two questions of AE section 2 item 4; the two `/tmp` input folders of the paused Codex lane (2.4 GB; owner recorded in
   `CHECKPOINT_HE_20261126_Z.md`); disk is 12.5 GB free (below the 15 GB line; `tmp_clone_report.py` found about 0 MB removable at 12:50Z).
6. If ADV has no assignment: tell ADV and propose one measured micro-upgrade. Remaining measured tick time is about 9 s (`assignment_flow` 3.3 s, `assignment_states` 3.6 s, one `git fetch` 1.3 s); no further change is justified by it.

## 3 Traps of this window
- **Measure a stateful command without running it:** import the module, replace `_save_state`, refuse repository writes with `sys.addaudithook`, load old and new source with `__file__` set to the root path, alternate runs; mask minute counters when comparing outputs (`tick_time.py` pattern in memory note `he-ag-pitfalls`).
- **A test regex that spans a nested element** (`<section id=X>.*?</hN>`) can answer for the child: cut at the first nested `<section`.
- **Delegates:** the auto-mode classifier refused a delegate's Bash call (ls/mkdir plus a repository read); a delegate told to stay blind should be given a work folder and paths in the dispatch and may still be stopped. Record, do not retry; finish the reading yourself with compact scripts (term counts first, then contexts).
- **No writes to the worktree while a `safe_push` runs** (REFUSED unclean tree). `cd` in the Bash tool persists: start commands with the worktree path.
- Host quiet condition used: load below 3.0 on two samples (the machine has 4 cores); view suites wait about 35 minutes at times.
- Memory notes of the window: `he-ag-pitfalls.md` (indexed).

## 4 First moves for the successor
1. State manifest (`current_state: READY`), LEGEND_CORE 21c to 21e, this file; verify its sha256 from `development/main` after `git fetch development main`.
2. Ask the old session (4441b7bf) to release; bind in the same response as the first working call, verify in the next, merge `development/main` before any accept.
3. Section 2, then tell ADV when idle. Rename nothing.
