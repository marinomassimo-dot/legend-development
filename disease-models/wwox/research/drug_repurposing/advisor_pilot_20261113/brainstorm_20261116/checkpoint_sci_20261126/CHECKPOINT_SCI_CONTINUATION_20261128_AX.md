# Checkpoint AX: SCI continuation of 2026-11-28 after ADV-300 (for the successor; resume from this file; AW only for standing background; hypothesis level; not medical advice; not edited once hashed)

Why: window `919d2041-8bbc-4441-9a09-3ac9a36983b6` (claude-sonnet-5-5, effort high) passed ADV's 250k restart line during ADV-300 (about 260k at 06:39Z). ADV launches the successor.

## 0. How to resume

1. Read `CLAUDE.md`, `framework/state/state_manifest_current.md` (`current_state: READY`), sections 21c, 21d, 21e of `framework/instruction/LEGEND_CORE.md` **before the first act**, this file (sha256 from `git show origin/main:<path> | sha256sum` against the launcher's digest; mismatch: stop and ask), then `python3 framework/scripts/mandate_continuity.py guidance`.
2. Release, then bind: `python3 framework/scripts/mandate_watch.py released --session 919d2041-8bbc-4441-9a09-3ac9a36983b6 --task ORCH-SCI-ADV065-DEEPEN-20261118` in a quiet Monitor until-loop (the old window releases when asked), then `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118` alone in its own text block in the same response as the first working tool call; verify next response (exit 1 = BOUND).
3. Effort high by `session_model_census.py --json --dir <own project folder>`. `ListAgents` first (today: ADV `a5e6f2ad`, IT `54ca757b`, HE `dc4707bc`).
4. Merge `development/main` before the first `accept`.

## 1. State

* **ADV-300 closed and on main** (landed 989f0efc4): not decidable under both readings; 6 checked (5 without record 4), floor 7; 2 verified misses (records 4 and 6) under the primary reading, 1 under the other. Folder `brainstorm_20261116/adv300_catalogued_triage_open_sci_20261128/` (`RESULT_...`, `SENTENCES_FOR_IT_...` J1 to J6 with a dream addendum on J1). Six receipts `FTR-20261128-*`. Records 7 to 10 (25295115, 29845204, 30211123, 32606933) have no receipt: **no retry, no re-dispatch, no other model, no self-run**. Held XML copies: `files/fulltext/PMID*_efetch_20261128.xml`.
* ADV-297's three unchecked records (26120275, 31829254, 32931356) stay unchecked on the same terms.
* **Operator list (safety stops, 2026-11-28):** ADV-300 batch 2 (one response withheld), batch 4 (reader stopped), batch 5 (API error `[bio]`, request `req_011ChUs6s4uq8aooHZvMYKzt`); ADV-297 earlier the same day.
* Session-close skills for ADV-295 block 2, ADV-297 and ADV-300: done (`research/session_evaluations/2026-11-28_adv295_block2_sci.md`, `..._adv297_adv300_sci.md`); the takeaways went to the operator at the end of window 919d2041.
* Also done: IT's question on El Ghaleb 2021 answered (Supplementary Table S1 is held: ages 28 y 11 m and 31 y, no seizures).
* Mandate: 139 DONE, 1 BLOCKED (the operator's papers); ADV-302 **not** accepted by 919d2041.

## 7. First moves

1. **Accept ADV-302 once** (`assignments/ADV-302.md`, key `catalogued-only-records-that-already-have-a-consumer`; read the file, it governs).
2. **Step 1** (about 45 minutes, no delegate): catalogued-only records without a receipt that have at least one consumer, with file, line and unit: `consumer_count.py` as corrected by HE (17cc693bd) **plus** an independent grep including PMC ids (known case: 25662954 via PMC4374002, discovery ledger line 29; it now has a receipt, so use it only to test the grep). Every count needs both hits. Freeze before step 1 ADV's prediction: at least 6 such records; strict at least 1 of 3 read.
3. **Step 2** only if at least 3: read the three with most consumer units at depth with the ADV-282/295 recipe; matching rule frozen with time and hash first; strict = verified AND MUST CHANGE; a delegate stopped by a safeguard is recorded and counted not checked; if two of three are lost, stop and send ADV the titles and topics of the lost records.
4. Rejecting: 0 consumer-bearing records = park the tail, resume when a consumer appears, ADV changes strand; 3 read and 0 strict = park by consumer rule.
5. If no assignment is open: tell ADV and propose one held-source question with a named consumer.

## 8. Working notes

* Disk: dispatch at 1.5 GB or more, push at 2.0 GB or more, stop below 1.0 GB and tell ADV. It fell to 0.94 GB once today from concurrent `safe_push` runs. Push: copy `/home/desktop/.claude/jobs/919d2041/tmp/scripts/push_when_room.sh`, change its `cd` to your worktree, run it as `nohup bash -c "bash <script> <SHA>" < /dev/null`. `safe_push` merges main under the lock and regenerates the derived surfaces itself; keep the tree clean (no untracked file) while it waits.
* Size any frozen minimum for reader loss. Keep step reports outside folders a later reader is given. Delegates: `model` and `effort` are Agent parameters now.
* Standing rules unchanged: Italian to the operator, files in English; no address to any service; a challenge page, 401, 403, 429, 5xx or a safeguard is a result; no spend, no contact; Codex PAUSED; frozen RP-045 and sealed ADV-174/175 untouched; HE renames; PMID 42422765 unopened.

## 9. Noticed, not acted on

* Several `2026-11-28_*_scicodex.md` session evaluations are on main although Codex is recorded as PAUSED (AW section 5 told ADV about the first). Not examined.
* The launch prompt of window 919d2041 pointed to a "section 7" that AW did not have (its first move was section 1); this file numbers first moves as 7.
