# BATCH COMMIT REPORT — BATCH_20261019_006

> Metabolic batch 2026-10-19, wave 4 (groups W1 and W2 of Scientists B, C and D) together with the repairs of the Mirror review of `BATCH_20261019_003` to `_005` (`mirror_review_BATCH_20261019_003_005.md`, M1 to M8). Integrator: ACTOR_ID `orchestrator` (stated assumption), task `ORCH-METABOLIC-BATCH-20261019`, operator authorisation, operator away. **Not medical advice.**

## Summary

- Type: MANUAL. Pre-flight LINT: `BLOCK_BATCH_COMMIT` (seven `ORPHAN_COMPLETE_READ`: the complete readings of Scientist D had no registry record), discharged by this batch. Post-propagation LINT: `WARN`, 0 BLOCK (the standing `UNLINKED_SUPPORT` and `POSSIBLE_CONTRAST` set; none names a record of this batch).
- WM version: `WM_v7.24` -> `WM_v7.25` (MINOR; one bump per batch; the registries gained 27 + 19 records and several lead and claim notes changed).
- Commit candidates: the three on scope A, **3 PROPAGATED**, 0 deferred, 0 superseded, 0 merged. No other `CC-20261019-*` on main lacked a disposition block (the 28 others are dispositioned; `CC-20261019-SCIENTIST-C-HELD-01` was propagated by `_004`). `CC-20261019-SCIENTISTD-DEBT-02` received an append-only follow-up block (its three resumes now reach the registry). Receipts: 680 chained (untouched; the 26 wave-4 receipts were recorded by the Orchestrator at `82694810`).
- Snapshot: `backup/20261020_batch006` (not committed); pre-batch commit `98b0a58b0ba742eb8b177a0b2b001efc96ddd3d2`; drift check FRESH. No restore was used.
- No claim was created or reversed; no `Status`, `Type` or `Summary` changed anywhere. `FULL_FALLBACK`: none; every op list (paper registry 35 ops, literature log 42, claim registry 2, working model 2, working-model history 2, discovery ledger 5, full-text queue 3) was accepted by the record-scoped editor on the first dry run.

## FILES TO CREATE

- `disease-models/wwox/research/batch_report_BATCH_20261019_006.md` (this report).
- `backup/20261020_batch006/` (snapshot; not committed).

## FILES TO UPDATE

| File | Propagation |
|---|---|
| `registries/paper_registry_current.md` | 27 new `PAPER` records (`PAPER 400`-`426`) after `PAPER 399`; "Promoted to" line on seven placeholders (`CORPUS-STUB-052`, `-009`, `-173`, `-100`, `CORPUS P289`, `P316`, `P270`), kept as history; depth lines of `PAPER 140` and `PAPER 148` raised to complete (earlier partial receipts kept visible); `PAPER 015` depth line carries its receipts (M8); `PAPER 387` "by term query" (M7); `PAPER 383` wording and grade; the transferability scale stated once in the header (M5) and 19 class-level records re-graded T3 -> T4 (`PAPER 340`-`346`, `350`, `370`-`372`, `384`-`386`, `389`, `390`, `392`-`394`), each saying so |
| `registries/literature_tracking_log_current.md` | 19 new `LIT` records (`LIT-0680`-`0698`); `LIT-0076`, `0036`, `0189`, `0121`, `0289`, `0316`, `0270` promoted to `processed`; `LIT-EX-006` gains a status note (status kept); the 19 matching grade lines follow the re-grade |
| `registries/claim_registry_current.md` | `CLAIM 009`: the 2026-10-20 wave note moved verbatim to its own `Evidence boundary` line (M1; declared `reflow`); `CLAIM 028`: "opposite sign" replaced by "a different direction ... compared at title level only, readouts not commensurate" (M6; status and type untouched) |
| `registries/working_model_current.md`, `working_model_history.md` | `Version`, `Last update`; history note and changelog row (the latter written with `record_scoped_edit.py`) |
| `research/discovery_ledger_current.md` | `DL-MECH-117`, `139`, `145`, `148` narrowed (M2, M3, M4); `DL-MECH-163`-`169` appended (seven `IPOTESI`) |
| `research/full_text_queue_current.md` | `FT-115` retired as a confirmed negative with the wording "no patient-level data" and the old wording quoted; `FT-201` queued (Surana 2020, the infantile-spasms cohort cited by the early-infantile series) |
| `research/wave4_batch_selection_20261019.md`, `research/batch_report_BATCH_20261019_005.md`, `research/mirror_review_BATCH_20261019_003_005.md` | selection row of Agarwala 2023 corrected in place with the old word quoted; the `_005` parent-side sentence narrowed to "in the registry records" (M8); two Mirror lines reworded (see Decisions) |
| `framework/state/state_manifest_current.md`, `state_history.md`, `growth_anchors.jsonl` | WM version, last-batch fields, `batch_20261019_006_scope` / `_candidates`; growth `+27` papers, `+19` literature; scale acknowledgement renewed |
| 4 candidates | append-only `## BATCH DISPOSITION` blocks (3 PROPAGATED; a follow-up block on `DEBT-02`) |
| derived surfaces | `coverage_report`, `batch_queue`, `pathograph` (inventory and export) and `reading_state` regenerated from the committed inputs |

## FILES UNCHANGED

`disease_model.md`, `meta_*`, `research_*_current.md`, biomarker, endpoint and therapeutic files, the dismissal ledger, the receipt ledger (680, untouched), the DisMech sidecar (no sealed claim touched), the deep-dive manifests (see Verification: the provenance ceiling), `surface_census.md`, `legend_activity_log.md` (not shipped in this edition).

## CHANGE LOG

1. **Registry debt.** Every study of wave 4 has a `PAPER` and a `LIT` record. Identity from the PubMed record (E-utilities summary, 2026-10-20) and checked against each receipt's study identifiers; depth, receipt, artefact path and full sha256 from the ledger event; unread or absent sections as the receipt's `coverage` map states. Numbering continues after `PAPER 399` and `LIT-0679`; the candidates' placeholders were renumbered (`W01`-`W08` of scientist-c to `PAPER 411`-`418`, of scientist-d to `PAPER 418`-`425`).
2. **What wave 4 says.** No WWOX-deficient evidence on temperature, liver steatosis, bone, one-carbon and amino acids, kidney, vitamin B6, folate, biotin, branched-chain amino acids, carnitine or bile acids. The WWOX-direct papers are tumour genomics, tumour genetics, cell-death assays or a method; in the one temperature assay WWOX loss protects. Twelve records are substitutes labelled NOT WWOX EVIDENCE.
3. **Agarwala 2023 (`PAPER 425`).** Registered as a WWOX-direct clinical series for its three WWOX case rows (3 of 80 recruited, 3 of 53 diagnoses), grade T2 with the gap stated; the limits are in the record (outcomes by aetiological group so none for the WWOX cases; single-centre, referral-biased, not an incidence; the deletion found by array is an inference from the Methods). It is not a pure substitute and not a genotype-phenotype corpus entry.
4. **Scientist-d's reading of the folate-transport report** (withdrawn, duplicate) is not registered; scientist-c owns the receipt (`PAPER 418`).
5. **Scope C.** `PAPER 140` and `PAPER 148` depth lines raised to `complete_fulltext_read` (receipts `-02` and `-03`, with the supplement now read; the stale "unretrievable supplement" sentence is marked superseded and the stale Genotype/model phrase fixed). The third study had only a corpus placeholder and no `PAPER` record (the task said three PAPER records; it was two): it lands as `PAPER 426`, promoted from `CORPUS P270`. `test_batch_queue.py` is green (51 tests); `READ_NOT_REGISTERED` is empty.

## Mirror repairs, each checked against its source first

M1 confirmed (the note sat at the end of the `Summary` line; the earlier wave-13 sentences in the same line are left). M2 confirmed against `PAPER 266`: no WWOX-HIF1A correlation is reported for TCGA; the lead now covers the leukocyte series only. M3 confirmed against `PAPER 325` ("when") and `PAPER 318` (no epinephrine-alone group; shock-only sampled at 15 minutes after dying): "stay" replaced by the measured 60-minute state plus the caveat. M4 confirmed: `PAPER 148` and `PAPER 152` report WWOX-mTOR association and raised phospho-mTOR on over-expression in cancer cells; the premise now says no record measures mTORC1 signalling in a Wwox-deficient neuron. M5: lighter route taken (see Decisions). M6 confirmed: `PAPER 383` says the comparison was at registry-title level. M7, M8 applied. **Mirror was not wrong on any item.** M9 (sharding) is not repaired here; see Scale.

## Parked (not propagated), with the reason

- Claim-level axis statements of the C candidate (section 3) and the "no change" lines for `CLAIM 025` and `RL-003`: no op text, no registry target; the records themselves carry the negatives.
- The three WWOX case rows of Agarwala 2023 in a genotype-phenotype corpus: no WWOX-specific outcome, and the shared earlier-cohort citation needs `FT-201`.
- The three parked B readings (no lawful body), and the manifests' gene-direct reference debts (no identifier in the screened entries).
- Scientist-d's staged lead "a normal genetic result must not stand in for a vitamin trial" (the wave note's fourth; absent from the candidate; screening advice, not a lead).
- Remaining third-party transmission wording in dossiers and the Scientist A wave file: retained on purpose (published third-party facts).

## DEFAULTS_TAKEN

1. **Numbering.** `PAPER 400`-`426` in the order B, C, D, then the scope-C resume; `LIT-0680`-`0698` for the 19 records without a `LIT`; promoted records keep their `LIT` and `LIT-EX-006` its status.
2. **Grades.** New records follow the scale now stated in the header: T2 for human WWOX case rows (Agarwala), T3 for WWOX measured outside a neural loss-of-function system, T4 for everything labelled NOT WWOX EVIDENCE and for records where WWOX is a list entry or a count (Kilic, Schatz, Rushing).
3. **Pathway, model, clinical relevance** assigned by the integrator and stated in each record; clinical relevance LOW for WWOX-direct records and BACKGROUND (non-WWOX) for substitutes.
4. **Claim links:** none for any new record; no claim cites a wave-4 paper.
5. **Leads.** `DL-MECH-163`-`169` (three of C, four of D); C's fourth is carried from an earlier candidate and not re-appended; all `IPOTESI`.
6. **Scale: the deferral was renewed** (`GA-...-scale_ack`): the papers registry went from 1,468,825 to 1,539,001 bytes (anchor 1,211,399; re-raise point 1,514,249), and `growth_anchors.py record` refuses without it. Records were not compacted below what they need to carry their negatives.

## DECISIONS_TAKEN

- **M5, lighter route.** One scale (T1 to T4) in the registry header, and a flat rule for class-level substitutes (always T4): that makes the grade stop carrying noise for them instead of re-reading 89 records. 19 substitutes were re-graded T3 -> T4 and Shin 2023 T4 -> T3 (WWOX-direct, non-neural); the 14 records of `_004` and Hong 2009 were already T3 and stay. Records outside 311 to 399 were not re-read.
- **Public release gate.** The Mirror's own review file (lines 92 and 118) and my first rewording of the `_005` sentence each tripped a BLOCK (parent-side terms next to a published patient). I reworded those three sentences to "transmission wording" / "carrier status", changing no finding; the Mirror file belongs to the Mirror, so this is flagged here. The gate is PASS.
- Study identifiers appear only in `Identifier` lines, receipt ids, paths and the queue entry; no parent-side term is paired with a variant in the new text.
- The disposition blocks were written by the integrator; the candidates' locator triples were audited blind by their Scientists (no mandatory trigger) and not rerun here.

## Verification

`legend_lint.py`: `WARN`, 0 BLOCK. `fulltext_receipts.py verify`: OK, 680 chained (untouched). `growth_anchors.py check`: PASS (papers 416, corpus 376, literature 679, unread premises 0). `public_release_gate.py`: PASS, 0 BLOCKS. `test_batch_queue.py` 51 OK, `test_build_evidence_index.py` 11 OK, `test_pathograph.py` 32 OK. **`test_manifest_receipt_provenance.py` FAILS and is not caused by this batch** (it reads only manifests and the ledger): measured 28 non-conforming against the ceiling 15, 14 of them manifests declaring a 2026-10-19/20 receipt that is not the producer (resumes and re-reads). The repoint tool would repair seven (`19918364`, `24008736`, `26302329`, `31340538`, `32581702`, `34634460`, `39416860`), refuses six with ARTIFACT DIVERGENCE, and `25779665` is UNKNOWN_EVENT (the manifest names `FTR-20261019-25779665-01`, the ledger holds `FTR-20261020-25779665-01`). Nothing was repaired and the ceiling file was not edited. The full release battery was not run (the Orchestrator runs it).

## Scale (Mirror M9)

The papers registry is 1,539,001 bytes, 27 percent over the anchor; the next 40-record batch adds about 100 KB. Acknowledged as a second deferral; the sharding decision is reserved to the operator and should be put to them now.
