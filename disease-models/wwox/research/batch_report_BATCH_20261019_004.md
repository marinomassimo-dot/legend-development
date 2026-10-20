# BATCH COMMIT REPORT — BATCH_20261019_004

> Metabolic batch 2026-10-19, reading-debt candidates: the HELD-partial re-reads of WWOX-direct papers (Scientist C) and the two WWOX-direct reading-debt waves (Scientist D). Integrator: ACTOR_ID `orchestrator` (stated assumption), task `ORCH-METABOLIC-BATCH-20261019`, operator authorisation, operator away. **Not medical advice.**

## Summary

- Type: MANUAL (the backlog threshold of 5 was also met). Pre-flight LINT: `WARN`, 0 BLOCK. Post-propagation LINT: `WARN`, 0 BLOCK (the warnings are the standing `UNLINKED_SUPPORT` and `POSSIBLE_CONTRAST` set; none names a record of this batch).
- WM version: `WM_v7.22` -> `WM_v7.23` (MINOR; one bump per batch; the rule requires it because evidence-boundary text of `CLAIM 009` changed and the registry gained records).
- Commit candidates: 3 on scope, **3 PROPAGATED**, 0 deferred, 0 superseded, 0 merged. Conflicts: 0. The candidate `CC-20261019-SCIENTIST-C-HELD-01`, DEFERRED by `BATCH_20261019_003` because its ten receipts were not in the ledger, is propagated now (ledger 624 at `1a08d784`).
- Snapshot: `backup/20261020_batch004` (not committed); pre-batch commit `2c748358c231e83f186e95fa3e337b6faa70fef8`. One restore of the paper registry (a plain `git checkout --` before anything was staged, base equal to the snapshot) was used to redo the insertion after the same separator defect as in `BATCH_20261019_003` (no blank line between the last inserted `---` and `CORPUS-STUB-181`); the op text now ends with a blank line.
- No claim was created or reversed; no `Status`, `Type` or `Summary` changed anywhere. `FULL_FALLBACK`: none; every op list was accepted by the record-scoped editor on the first dry run (one working-model anchor was corrected from `preamble` to the section heading before the dry run succeeded).

## FILES TO CREATE

- `disease-models/wwox/research/batch_report_BATCH_20261019_004.md` (this report).
- `backup/20261020_batch004/` (snapshot; not committed).

## FILES TO UPDATE

| File | Propagation |
|---|---|
| `registries/paper_registry_current.md` | 14 new `PAPER` records (`PAPER 356`-`369`) after `PAPER 355`; "Promoted to" line on the ten placeholders they replace (`CORPUS P229`, `P283`, `P341`, `P353`, `P357`, `CORPUS-STUB-019`, `032`, `034`, `045`, `121`; kept as history); reading-update notes on `PAPER 022`, `023`, `118`, `129`, `130`, `149`, `156`, `204` and on the reading record `CORPUS-STUB-109` |
| `registries/literature_tracking_log_current.md` | 4 new `LIT` records (`LIT-0648`-`0651`); `LIT-0046`, `0058`, `0060`, `0069`, `0140`, `0229`, `0283`, `0341`, `0353`, `0357` promoted to `processed` with a Status note |
| `registries/claim_registry_current.md` | `CLAIM 009` evidence-boundary wave note (status and type unchanged) |
| `registries/working_model_current.md` | `Version` and `Last update` lines |
| `registries/working_model_history.md` | `Last update` note and `Changelog` row (written with `record_scoped_edit.py`) |
| `research/full_text_queue_current.md` | `FT-090` status line: closed by a complete reading, with the landing |
| `research/discovery_ledger_current.md` | new section with `DL-MECH-151`-`162` (12 staged leads) |
| `research/metabolic_batch_selection_20261019.md` | the wrong label in the `33958783` row corrected in place with the old wording quoted |
| `framework/state/state_manifest_current.md`, `state_history.md`, `growth_anchors.jsonl` | WM version, last-batch fields, `batch_20261019_004_scope` / `_candidates`, growth delta (+14 papers, +4 literature) |
| 3 candidates | append-only `## BATCH DISPOSITION` block (3 PROPAGATED; the earlier DEFERRED block on the HELD candidate stays above it) |
| derived surfaces | `coverage_report`, `batch_queue`, `pathograph` (inventory and export) and `reading_state` regenerated from the committed inputs |

## FILES UNCHANGED

`disease_model.md`, `meta_*`, `research_*_current.md`, biomarker, endpoint and therapeutic files, the dismissal ledger, the receipt ledger (624 chained, untouched by this batch), the DisMech sidecar (no sealed claim touched: `CLAIM 009` is not one of `016`/`024`/`035`), `surface_census.md` (a dated photograph of a gitignored directory; regenerating it here would record peers' files; not regenerated, as in `BATCH_20261019_003`).

## CHANGE LOG

1. **Registry debt.** Every PMID of the debt wave now has a `PAPER` and a `LIT` record: 14 papers (D01-D14 renumbered `PAPER 356`-`369` from `registry_records.py catalog`, `PAPER` max 355, `LIT` max 0647). Identity was authored from the PubMed record (E-utilities summary, 2026-10-20) and checked against each receipt's study identifiers; the evidence depth, receipt, artefact path and full sha256 come from the ledger event; partial depths state what the receipt's `coverage` map leaves unread.
2. **Correction of the candidate's registry-state column.** The first candidate reported Hsu 2009, Lee 2017 and Lee 2021 as having no record, and each had a corpus placeholder and a `LIT` record. Ten of the fourteen papers are therefore promotions of placeholders (Hsu 2009, Huang 2018, Lee 2017, Huang 2016, Lee 2021, Tabarki 2015, Hsu 2016, Zhang 2012, Cheng 2016 and Ekizoglu 2015); only Chen 2018, Hong 2007, Lin 2011 and Lee 2015 had none and received new `LIT` numbers.
3. **`CLAIM 009` wave note.** The mitochondrial-localisation leg of the secondary literature resolves to single-laboratory observations in T-leukaemia lines under a pharmacological stimulus, with overexpression or dominant-negative constructs and no Wwox-null cell; the retinal, MPP+, Zfra/cytochrome c and Drosophila primaries stay unread. The study identifiers of the candidate's op text were replaced by `PAPER` numbers (the note links `PAPER 357`, `361`, `362`, which carry `CLAIM 009` as an annotation-only link).
4. **Figure and supplement debts closed** (reading-update notes; the superseded sentence of each Evidence depth line is named, not overwritten): `PAPER 129` (fat layer and surface temperature that cannot be separated from runting), `023` (glucose-uptake sign is condition-specific), `118` (main figures read; no oxidative-phosphorylation row), `022` (one un-normalised redox curve), `130` (Figure 6 and Supplementary Figure 8), `149` (complete reading), `156` (an LDLR panel), `CORPUS-STUB-109` (a printed odds ratio outside its own interval).
5. **Parkinson's disease dementia, not Alzheimer's disease** (`PAPER 204`). The registry records (`PAPER 197`, `PAPER 204`, `LIT-0493`) already carried the right disease; the wrong phrase "AD progression signal" lived only in the metabolic batch selection file and is corrected there with the old wording quoted (§7.2 form). The record also states that "the WWOX locus" of that paper is two signals about 240 kb apart, the stronger one in discovery not replicating.
6. **`FT-090`** closed by the complete reading of the commentary (a restatement of three reports; no metabolic phenotype).

## Parked (not propagated), with the reason

- Oxygen candidate (`CC-20261019-SCIENTIST-C-H4-01`, already dispositioned in `BATCH_20261019_003`): the `CLAIM 009` scope note and `CLAIM 025` support mention and the section 4 reading debts carry no op text; they stay parked. Adrenergic candidate: the optional catecholamine working-model note has no op text.
- HELD candidate: the RL-003 next-action proposal (a research line is not one of the four current files), the uptake-readout rule and the `CLAIM 025` no-change line (claim-level proposals without op text); Gao 2025 and Chong 2023 access routes stay with the operator.
- Debt candidates: the wishlists of papers with no lawful body (15 + 6) and the queue-entry list carry no op text.
- Candidates of Scientist A (H1/H2 and the `PLASMA` pair) were out of scope and stay queued for a later batch.
- Informational: the Scientist C recommendation to regenerate the HELD rows of the selection files is not acted on here.

## DEFAULTS_TAKEN

1. **Transferability grade** T3 and clinical relevance LOW for every new record (the candidates grade none per paper); the integrator's grade, stated in each record. The two reviews and the commentary are graded as the primaries are, with their secondary-source status in the Source type.
2. **Primary pathway** P5 only where the paper speaks to mitochondria, metabolism or redox (Hong, Lin, Huang 2016, Huang 2018, Lee 2021, Zhang); "oncology / tumor suppressor biology" for the cancer and signalling papers, as the placeholders already read; one human-spectrum label for the commentary.
3. **`CLAIM 009` links.** The three papers named in the wave note carry the claim as "annotation only"; the others carry none.
4. **Scale.** The paper registry grew by about 28 KB; no new acknowledgement was recorded (the tool re-raises the sharding question at +25 percent over the acknowledged anchor).
5. **`current_state` stayed `READY`** during the batch (concurrent landings); the snapshot and the clean base carried the protection.
6. **`surface_census.md` not regenerated** (see FILES UNCHANGED).

## DECISIONS_TAKEN

- A study identifier appears only in `Identifier` lines of registry records and in this report's tables; the claim note and the research-layer text name papers by `PAPER` number so that no claim names a paper whose `Claim links` does not name it.
- The registry text of the HELD reading updates states each depth as the new receipt states it; the supplementary reading of the Parkinson's-disease-dementia paper is recorded as the receipt records it (captions only, because Supplementary Figures 1-3 and 5 were not viewed as images), although the Scientist read Supplementary Tables 3-5, Supplementary Data 1 and Supplementary Figure 4.
- No parent-side term is paired with a variant anywhere in the new text; `public_release_gate.py` was run.

## Verification

`legend_lint.py`: `WARN`, 0 BLOCK. `fulltext_receipts.py verify`: OK, 624 chained (untouched by this batch). `growth_anchors.py check`: PASS (papers 359, corpus 376, literature 632, unread premises 0). `public_release_gate.py`: PASS, 0 BLOCKS. The full release battery was not run (the Orchestrator runs it).
