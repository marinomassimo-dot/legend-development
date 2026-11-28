# Checkpoint HE-AI (Harness Engineering, ACTOR_ID plan), 2026-11-28 about 15:50Z

Written for: the successor HE session (ADV launches it). Written at context peak 229k, under the 250k line, because the next item is dated tomorrow.
The traps of `CHECKPOINT_HE_20261128_AH.md` and of the checkpoints it names still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `c72e94ee-5ec7-4dc4-bb36-3117b93c509f` (worktree `he_ah_20261128`), model `claude-sonnet-5-5`, effort `high`. It stays open
  until the successor is bound, then releases with the line `MANDATE_RELEASED: PLAN-HE-CONTINUITY-20261118` (the task id is required).
- Mandate `PLAN-HE-CONTINUITY-20261118`: 197 steps, 195 DONE, 2 BLOCKED (166 classifier, 182 dated). `status` says ALL_BLOCKED; never write COMPLETE.
- Reply to the operator in Italian, write files in English. Codex lane PAUSED. Peer names change: run ListAgents before each message.

## 1 Done in this window; do not redo (all on `development/main`)
- AH item 1: CI #2897 completed success (reported by AG, not re-read).
- `541f55793`: `mandate_watch.py released` names a malformed release line and the line to write (ADV accepted).
- ADV-331 (`42f371257`): blind read of PMID 36828035 blood chemistry. ADV accepted it.
- ADV-336 (`d9a51f3da`): blind image read, Repudi Supp Fig 1A-C and Steinberg uncropped Supp Fig 1K. Sent to IT39 and ADV; acceptance not yet seen.

## 2 Open, in order
1. **2026-11-29 or later:** recheck and delete `files/adv174_negraes_custodian_he/` in the root checkout (sealed, outside git; 7 files on 2026-11-28).
   Step 182, BLOCKED on the date only. The outgoing session armed a wake for 00:01Z that ends with its session: arm your own.
2. **Worktree removal is frozen** (ADV, 2026-11-28) until the operator decides; obey `branch_hygiene.py --removal`. Step 166 stays BLOCKED.
3. **Disk:** 9.1 GB free (96%) at 15:48Z, 12 GB at 14:48Z; below the 15 GB report line. Nothing removed; cause of the 3 GB drop not measured.
4. ADV sends data tasks only with a named consumer. If idle after item 1, tell ADV.

## 3 Traps of this window
- One recorded receipt stales ranking.json, coverage_report.md, reading_state.md and the repurposing view. Order: record, commit, regenerate those
  (`repurposing_view.py run && run --source shareable && package && i18n --what collect`), commit, `safe_push`.
- If main moved with another receipt: merge, `git checkout --theirs` the conflicting ledger, manifest and generated files, record the saved receipt
  JSONs again, regenerate. A script of that sequence took one pass.
- Image reads without PIL: `pdfimages`/`pdftoppm` to PPM, numpy profiles, a 10-line PNG writer for enlarged crops
  (`advisor_pilot_20261113/brainstorm_20261116/adv336_blind_antibody_he_20261128/band_profile.py.txt`). Identify an unlabelled ladder band on a full membrane first.
- Memory note: `he-ah-successor-pitfalls` (indexed).

## 4 First moves for the successor
1. State manifest (`current_state: READY`), LEGEND_CORE 21c to 21e, this file; verify its sha256 from `development/main` after `git fetch development main`.
2. Ask the old session (c72e94ee) to release; bind in the same response as the first working call, verify in the next, merge `development/main` before any accept.
3. Section 2. Rename nothing.
