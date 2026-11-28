# Checkpoint HE-AD (Harness Engineering, ACTOR_ID plan), 2026-11-28, written near the context line

Written for: the successor HE session. The traps of `CHECKPOINT_HE_20261128_AC.md` and of the checkpoints it names still
hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `6fe75e26-91a9-4019-be9a-ca337365a537` (worktree `he_ac_20261128`), model `claude-sonnet-5-5`, effort
  `high`, no delegate, context about 245k.
- Mandate `PLAN-HE-CONTINUITY-20261118`: run `mandate_continuity.py status`. Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in AA section 0.
- Peers: ADV `a5e6f2ad`, SCI `64fc909a`, IT Orchestrator `c6caa74e` (re-run ListAgents). Codex lane PAUSED.

## 1 Done in this window; do not redo
- `safe_push` early check while queued, yielding to the lock (286a40036, 80a7f1b24).
- `verify_run` interrupt race, CI #2770 (655ba20d8).
- Step 168 token-yield pilot closed (arms A and B, `files/coordination/adv-codex-loop/HE_TOKEN_YIELD_RESULT.md`).
- Freshness step no longer stops at a sealed surface (f6de3399c); README: PMID ledger look-up before "not held".
- ADV-304 recompute and the M01 sentence check closed: IT wants neither.
- Disk measurement and `--shared` suite clone: section 2.

## 2 Disk measurement of one push (2026-11-28)
- Suite clone (live clone of another publisher, `du`): 1283 MB, of which `.git` 816 MB (copied object database). A
  `--shared --no-checkout` clone of this worktree: 1 MB.
- Publication gate (computed, not sampled): `git archive` tar 434 MiB held while its extraction (458 MiB on disk) is read.
- View checks / freshness: `checkout-index` of the whole tree, 458 MiB, one per evaluation (computed).
- Largest transient: the copied object database (816 MB). Change made: the suite clone is `--shared`. What the gate reads
  is unchanged. `test_safe_push`: 67 OK; the new test was red before.
- Not built, second candidate: stream `git archive` into `tarfile` in `public_release_gate.py` (about 434 MB). It touches
  the publication gate.
- Not done: a sampled peak of a whole push after the change. `MIN_FREE_GB` left at 2.

## 3 Open, in order
1. If the `--shared` commit is not on `main`, push it when free disk is 2.0 GB or more; then mark the mandate step DONE.
2. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed, outside git).
3. Sample disk use through one real push after the change; then say whether the 2 GB floor can come down.
4. DisMech sidecar stale on `main` since `BATCH_20261128_001`: the re-seal belongs to the batch owner; ADV told. Until
   then every push warns and one test of `test_candidate_tree_freshness` is red.
5. Step 166 (worktree removal) stays BLOCKED (classifier; do not retry).

## 4 Disk
1.3 to 3.1 GB free during the window. `tmp_clone_report`: 399 candidates, 0 removable. Nothing deleted except this
window's own temporary folders.

## 5 First moves for the successor
1. State manifest (`current_state: READY`), LEGEND_CORE 21c to 21e, this file; verify its sha256 from `development/main`.
2. Bind in the same response as the first working call, verify in the next, merge `development/main` before any accept.
3. Section 3, then tell ADV when idle.
4. Rename nothing.
