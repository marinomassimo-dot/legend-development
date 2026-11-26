# Checkpoint AS: SCI continuation of 2026-11-26 after ADV-292, for the successor (resume from this file; AR only for background; hypothesis level; not medical advice; not edited once hashed)

Why: window `47022d33-6ac2-4d5f-b46a-7deb576ec488` (claude-sonnet-5-5, effort high read back) passed ADV's 280k line (about 325k) after both ADV-292 increments. ADV's instruction (direction round 01:20Z): write checkpoint AS at this closed increment, send path and sha256, release; ADV launches the successor.

## 0. How to resume

1. Read `CLAUDE.md`, `framework/state/state_manifest_current.md` (`current_state: READY`), sections 21c, 21d, 21e of `framework/instruction/LEGEND_CORE.md`, this file (compute its sha256 and compare with the launcher's digest; mismatch: stop and ask), then `python3 framework/scripts/mandate_continuity.py guidance`.
2. Release first, then bind: `python3 framework/scripts/mandate_watch.py released --session 47022d33-6ac2-4d5f-b46a-7deb576ec488 --task ORCH-SCI-ADV065-DEEPEN-20261118` (exit 0 = RELEASED; wait with a Monitor until-loop); then `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118` alone in its own text block in the same response as the first working tool call; verify in the next response. Own worktree on a task branch; merge `development/main` before the first `accept`.
3. Read your effort back with `session_model_census.py --json --dir <own project folder>` (must be high). Run `ListAgents` (at 2026-11-26 about 01:30Z: ADV - CURRENT a5e6f2ad, IT Orchestrator - CURRENT 6f4e0008, HE - CURRENT 888b4b03).
4. Landing note: `task_close.py` refused at the end of this window ("main must be checked out in exactly one worktree"): no worktree holds `main` (the root checkout is a detached HEAD at `dfc18ff13`). Do not repair the root checkout; publish with `safe_push.py development main --expect-sha <sha> --serialize` (see section 1) and tell HE.

## 1. Done in this window

* **ADV-292 DONE** (mandate step marked DONE; reported to ADV, which consumed it). Folder `advisor_pilot_20261113/brainstorm_20261116/adv292_next_held_partials_sci_20261126/`: `RESULT_ADV292_INC1_SCI_20261126.md`, `RESULT_ADV292_INC2_SCI_20261126.md`, `READER_NOTES_INC1/INC2`, `BLIND_SENTENCES_INC1/INC2`, `BLIND_REPORT_INC1/INC2` (verbatim), `FILES_VIEWED_ADV292_INC1/INC2` (sha256), ten receipts `FTR-20261126-<pmid>-01/02`, `PROPOSED_SENTENCES_ADV292_SCI_20261126.md`. **Strict 3 of 10 records (39216838, 40485335, 31781019), loose 7 of 10; PREREG prediction 3 (range 1 to 5) not rejected; the 0-of-5 stop rule was not triggered.** Supplement-class strict 2, figure-class strict 1. Held apart, not counted: **S2a** (blind MUST CHANGE came from my own bracket on "class"; ADD if class = 4-phenylbutyrate), **S3b** (first reader STANDS, blind ADD), **S8a** (PP3 on the SNV only; strict on the each-allele reading). Own errors are listed in both RESULT files (empty S5 block, the S2a bracket, the unmarked IXA105 bar, row extracts read as workbooks).
* **Memory:** `sci-ar-adv292-pitfalls.md` (not in git; in the project memory folder).
* Peer reports: ADV (strict and loose counts, held-apart items); IT successor 6f4e0008 (paths of the four owed sentence sets and of the ADV-292 results).

## 2. Next work, in order (ADV's direction, 01:20Z)

1. **ADV-282** ranks 25 to 48 of the queue (`adv282_null_note_control_audit_sci_20261125/queue_ordered_adv282.tsv`, 48 queued null notes ordered by `consumer_count.py`, increments of eight; calibration in `PREREG_ADV282_INC3_SCI_20261125.md` and `RESULT_ADV282_SCI_20261125.md`). IT's apply landed (development/main `49b7ac71a1f1362d976e3d640fe4ebd910754d04`): read `it25_queue_20261125/RESULT_IT26_APPLY_20261126.md` first. IT's warning for my earlier rows k=2, 8, 12 and 20: the corrected unit dropped or restated the card's lead in places; read the whole field of each row, not the tail. Then **H02/A01 full pass with the second random 20**, held for the same apply.
2. **Sentence files owed to IT**: all four were sent to IT 6f4e0008 by path (ADV-289 RESULT section 7; washout RESULT section 5; ADV-290 RESULT section 4 without the line-294 note; ADV-291 RESULT section 3 and ADDENDUM1_CLOSURE) and ADV-292 by `PROPOSED_SENTENCES_ADV292_SCI_20261126.md` (strict A1 to A3, ADD B1 to B7, held apart C). IT's reply is not yet received: do not resend; check IT's apply report before assuming they are applied. `claim_registry` and the paper registry (PAPER 219 lines) change only through BATCH_COMMIT.
3. **Proposal (ADV: "the debt is not exhausted at this consumer level"):** the remaining readable held partials at one consumer, after item 1; use the ADV-292 recipe (frozen PREREG with one matching rule; first reader on the held files; blind sentence-level reader given the sentence alone, never a bracket of mine; verify the sliced block before dispatch). Run `rank_held_partials_adv265.py`, `containment_adv265.py`, `content_check_adv280.py`, `count_adv280.py` and `consumer_count.py` first, with the standing exclusions 28151481, 28045433, 41948127, 33958783 and the records read by ADV-292 (the ten, reserve 36282524 and 42807679 unused).
4. One mandate item stays BLOCKED (the operator's papers); ADV-282 is the one other open step.

## 3. Standing rules (unchanged from AR)

Italian to the operator, files in English. No e-mail address to any service; challenge pages and 401/403/429/5xx are results; no spend; no contact with authors or outside parties; Codex PAUSED; frozen RP-045 and sealed ADV-174/175 untouched; the HE window does renames; the Obeid 2026 article (PMID 42422765) stays stopped and unopened, including its manifest and receipts. State model and effort in every delegate dispatch and read them back (the Agent tool has no effort parameter). Delegates cannot write files in the repo: ask for the text as the reply. Long suites and `safe_push` through `nohup bash -c '...' < /dev/null`; never commit or create a repo file while a `safe_push` runs. Before a first push of a new .md: `test_fresh_clone_reader_journey.py`, `test_documented_commands.py`, `test_link_targets.py`, `test_structured_data_integrity.py` (all four passed at 2c4fb9da8 for the ADV-292 files).

## 4. Lessons of this window (memory `sci-ar-adv292-pitfalls.md`)

* A bracket added to a blind sentence is an interpretation, not the repository's wording: give the sentence alone and ask for two readings.
* Print and check the length and tail of every sentence extracted for a blind packet (S5 was empty).
* A per-animal supplementary table can overturn a paper's prose ("seemed to follow"): recompute with the paper's own exclusion rule and report both readings.
* A derived row extract is not a workbook read; say so in the receipt.
* Do not `git checkout` a ledger file to undo one receipt: it drops every receipt recorded since the last commit.
