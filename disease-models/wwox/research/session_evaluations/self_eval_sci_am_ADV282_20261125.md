# Self-evaluation - SCI window AM, ADV-282 (positive-control audit of the queued null-wording card notes, ranks 1 to 16), 2026-11-25

## Scope and executable verdict

- Session: ADV-282, increments 1 and 2 of the ordered queue (14 rows audited; two rows not audited after a classifier stop). Actor `orchestrator` (SCI), session ae0002e7, `claude-sonnet-5-5`, effort high. Two delegates, one active at a time: blind sentence readers, `legend-delegate`, asked sonnet and high, read back from each transcript census: 23 of 23 and 60 of 60 turns `claude-sonnet-5-5` at `high`.
- Receipts: none written (targeted null checks, not completed reads). `session_self_eval.py`: PASS. Receipt verification OK (2,851 chained, tail anchored). Structural LINT: no block. Landing: see the push line in the result of the session.

## Content diagnosis

| Dimension | Answer | Grade | Debt or correction |
|---|---|---|---|
| Rule fixed before the sources | PREREG per increment, calibrated on loose 4 of 9; written before any source of its rows was opened | strong | increment 1 was scored against ranges for eight rows with six audited |
| Order | HE's `consumer_count.py` by script; the PMID extraction was wrong on the first run (dates, DOI digits, PMC ids) and fixed before use | adequate | queue ordering is by study, not by row |
| Source reading | six rows from one deposit recomputed per library from the Salmon table; printed ratios reproduced; figures rendered with hashes; one route result (Hussain 2019 figure not held) recorded | strong | the GSE150123 direction checks are the blind reader's only |
| Blind check | Sentence files built by script; readers saw no class; verdicts reconciled row by row | strong | one reader per increment; I re-derived only the headline defects (G6PD, the confirmed gene values, Fig 1F by eye) |
| First reader under-grades | first reader MUST CHANGE 2 of 6, blind 4 of 6; ADD or MUST CHANGE 6 of 6 on both | strong (honest) | same pattern as ADV-280 and ADV-281: the defect sits in the compressed description |
| Prediction calibration | strict within range; loose 0 of 14 by the first reader and 5 of 14 by the blind reader (the rejecting observation depends on the matching rule) | adequate | both readers' classes reported |
| Safety classifier stop | not retried, not rephrased; reported to ADV and recorded in the result | strong | two rows queued, on the operator list |

Two statements in my first draft of the RESULT were written from memory and corrected before landing against the first-reading tables (which figure I had viewed; a LDH/PDH range I had not recorded).

## Upgrade (the answer, not the promise)

Two checklist lines added to `PRE_READ_CHECKLIST_ADV276_SCI_20261125.md` in the same commit (re-search a list for every gene a sentence names and state its cut and units; a "clean dissociation" or "wild-type-like" label names its time point and assay). A RESULT is built from the first-reading tables, not from memory: re-check every number against them before it is written.

## Addendum: ADV-283 (same window, PDK isoform pattern in a second held dataset)

PREREG (hash 6854b24d, 2026-11-25T20:23Z) frozen before any value of a candidate table was opened; rules (detection is coverage, ratio 1.2 and every-library ordering, no pooling) applied by script; rejecting observation met (PDK3 0.689 hippocampal null, 1.020 cortex). One blind reader (sonnet 5.5, high, 15 of 15 turns) found two MUST CHANGE sentences: S2 stated no criterion for "higher" and S3 compared CAGE columns on different scales (the PREREG had only called D4 descriptive for n of 1; the unequal column totals were found by the reader and verified by me). Grade: strong on the frozen rule; adequate on the dataset check (a column-sum look before the PREREG would have classed D4 as unusable). Upgrade: before any cross-dataset comparison, print column totals of every merged expression table and state the scale in the PREREG; a "pattern absent" sentence names its criterion and the nearest nominal case.
