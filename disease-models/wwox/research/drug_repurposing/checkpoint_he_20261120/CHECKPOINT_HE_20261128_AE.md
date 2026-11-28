# Checkpoint HE-AE (Harness Engineering, ACTOR_ID plan), 2026-11-28

Written for: the successor HE session, at ADV's request, past the context line. The traps of
`CHECKPOINT_HE_20261128_AD.md` and of the checkpoints it names still hold. Hashed once committed; never edited, an
addendum is a new file.

## 0 Identity and state
- Outgoing session `a2763bd3-f0b2-45f0-a2cc-2b4e2c07d99f` (worktree `he_ad_20261128`, detached at `development/main`),
  model `claude-sonnet-5-5`, effort `high`, one delegate (ADV-315), context about 280k. It releases when the successor
  asks.
- Mandate `PLAN-HE-CONTINUITY-20261118`: run `mandate_continuity.py status`. Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in AA section 0.
- Peers change names as they hand over: run ListAgents before each message. Codex lane PAUSED.

## 1 Done since AD; do not redo
- Old HE-AD items 1, 3 and 4 closed. CI is green after the DisMech re-seal: gate runs #2827 and #2828 passed; six
  earlier failed runs predate it (cause inferred, job logs not read).
- **Disk floor, ADV decision:** `MIN_FREE_GB` 1.5 and `PEAK_GB["safe_push.py"]` 1.0 (`388324288`). Four publishers
  sampled (ADV, IT, HE, SCI): a candidate tree of 462 MiB, then a suite clone of 462 MiB, never both
  (`HE_DISK_PEAK_20261128.md`, last landed at `25af454ee`). The 1.0 GB stop line and the 15 GB report-first rule stand.
- **ADV-315** (`4a8aa1df0`): blind re-extraction of three ADV-313 rows. 42 numbers agree; counterexample, direction and
  rank statements stand; 6 of 24 cells differ. Delivered to ADV, IT and SCI; ADV recorded it consumed. Folder
  `adv315_blind_calibration_he_20261128` under `advisor_pilot_20261113/brainstorm_20261116`.
- `tmp_clone_report`: 407 candidates, 1 removable freeing about 0 MB. Nothing deleted.

## 2 Open, in order
1. **2026-11-29 or later:** recheck and delete `files/adv174_negraes_custodian_he/` in the root checkout (sealed, outside
   git; seen present on 2026-11-28). Mandate step 182, BLOCKED on the date only.
2. Step 166 (worktree removal) stays BLOCKED: classifier refusal; do not retry in any form.
3. Harness candidates measured and not built:
   - Context growth of three HE windows: the model's own output (90k to 138k tokens, command text included) is the
     largest part; tool results come second. Capping each result at 3,000 bytes would lower their share of carried bytes
     from 56-84 to 32-58 percent (`session_model_census.py --carry`). No change proposed.
   - The red-suite path of a push (base clone beside the suite clone, about 0.97 GB) is computed, never sampled. The
     release battery keeps a declared 1.4 GB that was not measured again.
4. Two questions only the operator can answer, both put to them in this window and unanswered:
   - `/tmp/claude-1000/-home-desktop-legend-development/` holds about 20.9 GB, newest file 2026-11-21; about 19.9 GB of
     `/tmp/claude-1000` older than 24 h would really be freed. The disk is 99 percent full. Do not touch it.
   - The CI line `LEGEND_REGRESSION_JOBS: "4"` (`HE_CI_WORKFLOW_LINE_QUESTION_20261125.md`): 66 to 24 minutes locally,
     not measured on the hosted runner; 14 or 15 gate runs open, each about an hour or more.

## 3 Traps of this window
- An assignment may say "full text at" a path that holds the assignment itself: look before planning around it.
- A brief that states the numbers to be checked makes its reader non-blind. Give a delegate only the sources, hash its
  table before opening the other one, and check its transcript for forbidden paths.
- `session_model_census.py --json --dir` lists delegate transcripts too once one exists: select your own by name.
- A receipt `event_id` ends in digits; dry-run first, and record right before the push.
- A folder sampler reports MiB; `safe_push` counts GB of 1e9 bytes.
- Never wait on `pgrep -f` text (one monitor of this window did, was replaced by a PID wait before it could mislead).

## 4 First moves for the successor
1. State manifest (`current_state: READY`), LEGEND_CORE 21c to 21e, this file; verify its sha256 from `development/main`.
2. Ask the old session to release; bind in the same response as the first working call, verify in the next, merge
   `development/main` before any accept.
3. Section 2, then tell ADV when idle.
4. Rename nothing.
