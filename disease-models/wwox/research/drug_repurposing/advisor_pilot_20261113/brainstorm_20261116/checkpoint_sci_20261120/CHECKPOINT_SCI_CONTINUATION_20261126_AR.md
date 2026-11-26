# Checkpoint AR: SCI continuation of 2026-11-26 after ADV-291 and the ADV-292 pre-registration, for the successor (resume from this file; AQ and AP only for background; hypothesis level; not medical advice; not edited once hashed)

Why: window `9bb60ab5-6592-40df-b9ef-1b98c409e96e` (claude-sonnet-5-5, effort high) reached a peak of about 365k tokens (cache-inclusive), above ADV's 280k line, when ADV-292 was assigned. ADV decided: this window freezes the PREREG and closes; the successor reads both increments.

## 0. How to resume

1. Read `CLAUDE.md`, `framework/state/state_manifest_current.md` (`current_state: READY`), sections 21c, 21d, 21e of `framework/instruction/LEGEND_CORE.md`, this file (compute its sha256 and compare with the launcher's digest; mismatch: stop and ask), then `python3 framework/scripts/mandate_continuity.py guidance`.
2. Release first, then bind: `python3 framework/scripts/mandate_watch.py released --session 9bb60ab5-6592-40df-b9ef-1b98c409e96e --task ORCH-SCI-ADV065-DEEPEN-20261118` (exit 0 = RELEASED; wait with a Monitor until-loop); then `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118` alone in its own text block in the same response as the first working tool call; verify in the next response. Own worktree on a task branch; merge `development/main` before the first `accept`.
3. Read your effort back with `session_model_census.py --json --dir <own project folder>` (must be high). Run `ListAgents`; at 2026-11-26 00:33Z: ADV - CURRENT a5e6f2ad, IT Orchestrator - CURRENT d26b0ae5, HE - CURRENT 6e20e53e.

## 1. Done in this window (on `development/main`)

* **ADV-291 DONE and consumed by ADV** (`adv291_breton_s4_s12_sci_20261126/`: RESULT and ADDENDUM1_CLOSURE; main `75981649b`). The series did not close as "nothing changes": the dossier sentence "animal-level significance in 8 of 9 for delta" (`fulltext_dossiers/PMID34634460.md` line 9, its only consumer found) is reversed (rho positive in 8 animals, p < 0.05 in 2). S4 a1 supports increased firing; S4 a2 plots knockout about 4 Hz above wild type at 60 and 80 pA against a caption p > 0.05 with no stated statistic. ADV's call: the CLAIM 021 firing sentence goes in the result's section 3.1 form, stating both facts and choosing neither. S1F is internally inconsistent: one line, never repaired by us.
* **ADV-290 correction:** the "Fig S3C" at `CC-20260826-DOSE-DECISION-TABLE-01.md` line 294 is the Obeid paper's figure, not Breton's; no change to that line (ADV and IT told; both recorded it). Read a line in its file before proposing a change to it.
* **ADV-292 accepted and pre-registered, nothing read:** `adv292_next_held_partials_sci_20261126/PREREG_ADV292_SCI_20261126.md`, sha256 `a002d131e0e19e404bfc75fac67c5deff294e228dce6b38e68e2b0efdbcfd780`, frozen 2026-11-26T00:33Z. Brief `assignments/ADV-292.md` (ADV's; it carries the correction note; if not yet on main, ADV's push brings it).

## 2. Next work, in order

1. **ADV-292 increment 1:** 39216838, 40485335, 41178115, 42268630, 41664646. **If the five give 0 strict changes, stop and tell ADV** before increment 2.
2. **ADV-292 increment 2:** 39923817 (tables only), 37946251, 40858643, 26419537, 31781019. Reserve 36282524, then 42807679. Matching rule, completion definition and predictions are in the PREREG (strict 3, range 1 to 5; rejecting observation: at most 1 of 10).
3. One receipt per record; wording to IT after its apply report; `claim_registry` only by BATCH_COMMIT after `growth_anchors`.

## 3. HELD / owed

* **Sentences owed to IT, NOT yet sent.** ADV's message said they were already with IT; this window did not send them. IT received only a notice that they come after its apply report (00:10Z) and the warning about line 294 (00:18Z). Send, after IT's apply report with SHA: ADV-289 (`adv289_breton_s3c_dapv_block_sci_20261125/`, result section 7), the washout-rule replacement sentence (`washout_rule_check_sci_20261125/`; IT carries it as a note first, ADV decides after IT's apply), ADV-290 (`adv290_breton_supplement_premise_sci_20261125/`, without the line 294 note), ADV-291 (result section 3 and addendum 1). No apply report had reached this window.
* **ADV-282** ranks 25 to 48 and the H02/A01 full pass with the second random 20: held until IT's apply report. Keep TSV rows k=2 to 20 stable until IT lands. IT also owns the n=3 Dutch replacement.
* One mandate item stays BLOCKED (the operator's papers).

## 4. Standing rules (unchanged from AQ)

Italian to the operator, files in English. No e-mail address to any service; challenge pages and 401/403/429/5xx are results; no spend; no contact with authors or outside parties; Codex PAUSED; frozen RP-045 and sealed ADV-174/175 untouched; the HE window does renames; the Obeid 2026 article (PMID 42422765) stays stopped and unopened, including its manifest and receipts. State model and effort in every delegate dispatch and read them back. Long suites and `safe_push` through `nohup bash -c '...' < /dev/null`; never commit or create a repo file while a `safe_push` runs. Before a first push of a new .md: `test_fresh_clone_reader_journey.py`, `test_documented_commands.py`, `test_link_targets.py`, `test_structured_data_integrity.py`.

## 5. Lessons of this window (memory `sci-aq-adv291-pitfalls.md`)

* A panel label is not an identifier across papers; "never opened" is a negative to search by figure label.
* A delegate cannot write a report file: ask for the text as its reply.
* A queue count is quoted only after `consumer_count.py`, the content check, the standing exclusions of earlier PREREGs and a declared-figure check (checklist bullet added).
