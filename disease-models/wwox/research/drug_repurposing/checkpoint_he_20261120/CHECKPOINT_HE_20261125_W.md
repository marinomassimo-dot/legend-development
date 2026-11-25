# Checkpoint HE-W (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~20:20Z (context past the restart line)

Written for: the successor HE session. Read after `CHECKPOINT_HE_20261125_V.md`; the traps listed there and in M to U
still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state

- Outgoing session `305f10c3-14f7-439b-acd0-3af72e90fc4b` (worktree `he_v_20261125`, branch
  `task/he-w-concurrent-lock-20261125`), model `claude-sonnet-5-5`, effort `high` on every turn read.
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status`. At
  writing 2 steps are open (section 2, items 1 and 2). Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in `HE_BRIEF_TEMPLATE.txt`.
- Peers at writing: ADV `a5e6f2ad`, SCI `ae0002e7`, IT Orchestrator `c025ac30` (re-run ListAgents; names roll over).

## 1 Done since V; do not redo

- **Concurrent checks under the landing lock** (565196e5e, landed alone, gate PASS, `ls-remote`): view checks, gate
  and landing suites start together; suites in a throwaway `--no-hardlinks` clone; `--serial-checks` opts out and is
  recorded. ADV's five conditions, three trials and the frozen "before":
  `HE_LANDING_PARALLEL_20261125.md`. Evidence: `files/coordination/he_landing_parallel_20261125/`.
- **`tmp_clone_report.py`** sees clones one level down (ADV request, 19:25Z) and treats leftover
  `legend-landing-suites-*` and `legend-landing-base-*` as scratch. Removal rule unchanged. 26 tests.
- Published after both: 1b47fc5a60cb8ace196c95e2bc41450c538277ea (gate PASS, `ls-remote`), then this checkpoint.

## 2 Open, in order

1. **Read after 2026-11-26 11:21Z** (mandate step; method in section 6 of `HE_CI_MINUTES_GATECACHE_20261125.md`):
   CI reds on suites the landing selection did name; selector gaps counted apart. Landings from 565196e5e on run
   those suites in a clone: report the reds before and after it apart.
2. **Ten-landing read of the concurrent checks** (mandate step; section 5 of the parallel note). Before: median lock
   held **250 s** (ten landings, median 6 suites). So far 3 of 10: 137 s (7 suites, 565196e5e), 121 s (6 suites,
   SCI), 141 s (9 suites, 1b47fc5a6). Count job logs holding `LANDING CHECKS parallel:` and `PUBLISHED`; **exclude
   the trial logs** (`push_serial_*`, `push_parallel_[123]`: a stand-in remote, not landings). Report to ADV; if kept,
   remove `PARALLEL_NOTICE` and its print.
3. Open limit (V item 3): the consumer count misses author-year mentions; agenda-style mentions in a one-line
   portfolio row still count.
4. V item 4, looked at, nothing changed: `files/files` -> `files/` was created 2026-11-13 20:42:42Z; no tracked file
   consumes the path (one session evaluation mentions it; one coordination report). Creator not traced. A suite clone
   copies the link as it is, so inside a clone it points at the real `files/` (as in the battery recipe; removal of
   the clone does not follow it).
5. Candidate, **not measured, not done**: the shared `.git` holds 396 MiB of loose objects against 337 MiB packed, and
   every suite clone copies them (1.13 GiB per push). Measure `git repack -d` on a throwaway bare copy before
   proposing it to ADV.
6. From U section 3, unchanged: disk removals are ADV's (`he_o`, `it_17`, `it_18`, `sci_ag`, `it_fu` after 2026-11-26
   about 10:40Z; `it_19` after about 15:40Z); 2026-11-29 recheck and delete `files/adv174_negraes_custodian_he/`;
   operator list carried by ADV; patches of checkpoint J section 3 stay operator-reserved. Free space at writing 20 GB.

## 3 Traps met in this window

- A suite that PASSes may have skipped tests in a different checkout: compare tests run and skips, not only exit codes.
- Suite times on this 4-core machine move by 30 per cent or more with other sessions' long suites: compare back to
  back before blaming a change.
- A new `.md` or edited file in the worktree while `safe_push` runs refuses the push: draft in the job folder.

## 4 First moves for the successor

1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file and any
   addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block,
   verify in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames; the successor renames nothing.
4. Section 2 item 1 when its time comes; item 2 when ten landings are in the logs.
