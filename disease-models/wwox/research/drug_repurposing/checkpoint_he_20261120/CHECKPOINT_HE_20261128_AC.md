# Checkpoint HE-AC (Harness Engineering, ACTOR_ID plan), 2026-11-28, written at the context line

Written for: the successor HE session. The traps of `CHECKPOINT_HE_20261128_AB.md` and of the checkpoints it names still
hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `c396c807-056c-4163-bd93-2a7ecf2c2886` (worktree `he_ab_20261128`), model `claude-sonnet-5-5`, effort
  `high`, no delegate, context 309k when first measured (past ADV's 250k line; measure it early).
- Mandate `PLAN-HE-CONTINUITY-20261118`: run `mandate_continuity.py status`. Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in AA section 0.
- Peers: ADV `a5e6f2ad`, SCI `919d2041`, IT Orchestrator `54ca757b` (re-run ListAgents). Codex lane PAUSED.

## 1 Done in this window; do not redo
- ADV-301: 0 true of 15 flags in five lane briefs (`briefcheck_adv301_he_20261128/`); consumed by ADV.
- ADV-306: no Wwox callosal deposit; two LATENCY-ONLY deposits (`callosal_recordings_adv306_he_20261128/`); consumed.
- ADV-307: Rictor deposit, slope against early recruitment INDETERMINATE (`rictor_slope_adv307_he_20261128/`); consumed.
- Predecessor worktree `he_aa_20261128` removed by ADV.

## 2 Open, in order
1. ADV-304 blind recompute (HE as the different reader), when IT asks; IT was told to ask the successor.
2. M01 copied-sentence check, when IT's tazemetostat sentence reaches a card on main (not seen at 06:45Z).
3. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed custodian folder, outside git).
4. Step 168 arm B. Arm A is recorded in `files/coordination/adv-codex-loop/HE_TOKEN_YIELD_RESULT.md`: #2774, #2775,
   #2777 all success; call-and-character measure only, tokens not attributable.
5. The BLOCKED worktree-removal step stays as it is (classifier; do not retry).
- Candidate, not built: run `test_release_surface.py` before a push queues for the lock (one refusal today cost the queue
  wait and a 97 s lock hold; how often it happens is not measured).

## 2b What filled the context (measured on this transcript at 312k, 138 responses, about 26 minutes)
Birth 60k. Characters: Bash results 224k, Bash inputs 141k (long heredoc scripts and drafts), user and system text 105k,
Read 26k, messages sent 17k; 125k output tokens. This is the second HE window past 300k inside an hour or two: write
analysis code to files once, print head or tail summaries only, one source window per question, and measure the context
after the first assignment.

## 3 Traps met
- A new `.py` with a shebang but no executable bit reds `test_release_surface.py`; `safe_push` refuses after the queue.
- Nothing may be written in the worktree while a `safe_push` waits for the lock: draft in the job tmp folder.
- Availability searches: abbreviations, and the article's data statement before a negative.
- Dryad downloads answer 401; the public Zenodo copy of an older deposit serves the same bytes.

## 4 Disk
About 2.0 to 3.2 GB free; unchanged decision items for the operator are in AB section 5. Nothing deleted by this window
except its own downloads.

## 5 First moves for the successor
1. State manifest (`current_state: READY`), LEGEND_CORE 21c to 21e, this file; verify its sha256 from `development/main`.
2. Bind, verify in the next response, merge `development/main` before the first accept.
3. Section 2, then tell ADV when idle.
4. Rename nothing.
