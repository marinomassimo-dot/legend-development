# Self-evaluation - SCI window AK, ADV-280 (next ten readable held records), 2026-11-25

## Scope and executable verdict

- Batch/session: ADV-280, ten held records in two increments of five (36926521, 37804316, 41570991, 41706892, 10.1101/2025.05.01.651195; 35883580, 38378758, 38443647, 38731820, 38740822). Actor `orchestrator` (SCI), `claude-sonnet-5-5`, effort high. Landed at `65e1ff7da` (increment 1 at `8e5c17ba8`).
- Complete-read receipt IDs: none; ten partial receipts `FTR-20261125-<id>-01` (36926521, 37804316, 41570991, 41706892, PPR1015434, 35883580, 38378758, 38443647, 38731820, 38740822), `evidence_depth: queried_not_full_read`.
- `session_self_eval.py`: PASS ("every complete read has landed and every declared output resolves"); the declared gaps it prints are older manifests, none in this batch.
- Per-study manifests: not applicable (no complete read).
- Receipt verification: OK, 2,846 chained receipts, tail anchored.
- Structural LINT: no BLOCK_SYSTEM or BLOCK_BATCH_COMMIT, exit 0.
- Local verdict: PASS. Workspace and global verdict: `safe_push` gate PASS and 11 landing suites, 0 turned red.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full text, figures, tables, supplements | Every figure image of the class opened, every supplement page rendered and seen, workbooks parsed and counts recomputed (50 of 61, 6 of 12, the Dataset S1 differential counts); three videos not watched (no tool); peer-review files searched only | partial | videos in 37804316 and 35883580; receipt for 37804316 kept at supplementary `not_read` |
| Main message and original contribution | Strict 2 of 10 (a card parenthesis on assay type and concentrations; a ledger lineage line), loose 9 of 10, no reversal | strong | the strict 3rd item (AFG3L2 first clause) left to IT |
| Hidden gold beyond keywords | Pixel profile of the western strip; Supp Fig 1F against the main figure; the NAA 24 h against 16 h; the glial lifespan contradiction in the preprint | strong | |
| Source parity | All ten papers are other systems; the one WWOX record (36926521) treated at genotype level | strong | |
| Team type, field density, observation vs interpretation | Image readings labelled as such; delegate verdicts kept apart from the reader's grading | strong | |
| DATO / INFERENZA / IPOTESI separation | Each proposed wording says what is measured and what is inferred (for example function loss of the six abundant pathogenic variants) | strong | |
| Existing claims touched | CLAIM 033 reserve (stands, with additions), card E01 two items, card E02 DR-E02-006 and -007, DL-MECH-058, card A02 DR-A02-002, R1 premise 0 | strong | none applied here: IT owns the registries |
| Multi-hop and corpus cross-query | Null-wording scan of the cards (10 of 190 notes, 1 with a control), proposed as ADV-281 | partial | adopted by ADV |

## Persistence diagnosis

- Durable ledger/registry IDs: result files, PREREG, sentence and report files, receipts and hash tables, all under `adv280_next_ten_held_partials_sci_20261125/`; wording sent to IT twice (the second corrects the first) and a report to ADV.
- Reading queue/debt: the 36 remaining held records stay queued; ADV rotates the strand.
- Dossier and commit candidate: none (wording for IT's `BATCH_COMMIT`).
- Receipt source fingerprint, coverage and supplement state: sha256 of each source XML; coverage per class stated in each receipt's basis; the 37804316 supplementary class deliberately `not_read`.
- Can a future run distinguish full text from abstract only? Yes: every receipt says `queried_not_full_read` and names the classes read.

## Process and capability diagnosis

- Skills/gates/patterns used: PREREG first (with ranges), blind second readings (two delegates, sonnet, effort high stated in the prompt), pre-read checklist of ADV-276/279, receipts through the validated writer, views regenerated, `safe_push --serialize`.
- Plausible skills deliberately declined: `legend-locator-audit` (no consolidated claim moved by SCI; wording goes to IT), `legend-discovery-method` (no new-claim wording).
- Failures, retries, concurrency: (1) first-pass grading by fact gave strict 0 of 10 and a first version of the increment-1 result landed with strict 0 of 5; (2) HE's join fix moved the consumer counts after the pre-registration (35883580 halved, two records without true consumers); (3) the shell resets cwd after `cd` into the root checkout; (4) `ugrep` complexity limits on long patterns.
- What caught each failure before an overclaim: (1) a second blind delegate given the sentences, then my own re-check of the Methods and legends; (2) HE and ADV messages; (3), (4) the tool output.
- Disease-agnostic micro-upgrade shipped: four checks added to `PRE_READ_CHECKLIST_ADV276_SCI_20261125.md` (the blind reader gets the sentence; a description of the source's own assays repeated from memory; a null needs its activity check; measure a faint band on a small strip).
- Regression/evidence: the checklist text carries the batch's examples; ADV-281 is built on the same rule (PREREG with sentence-given blind reader).
- Residual risk and next decisive action: strict items found only by sentence-level checking suggest the first reader under-grades in general; the next batch (ADV-281) puts the sentence to the blind reader from the start.

## Attribution census

```
ATTRIBUTION_CENSUS
incidents: 4
machine: 1   blind_auditor: 1   peer: 1   self: 1
severity_high: 2   of which self: 1
undetected_known: 0
```

Incidents: (1) strict items missed by the first-pass fact-level grading and landed as strict 0 of 5 in the first version of the increment-1 result: caught by the second blind delegate that was given the sentences, then re-verified by me on the held files; `blind_auditor`, severity high (it reached a landed file, corrected in the next commit); (2) a stale remainder count (36, not 41) and consumer joins fixed after the pre-registration: caught by HE and ADV; `peer`; (3) a shell working directory reset after a `cd` into the root checkout and `ugrep` complexity limits: `machine`; (4) the first blind reader called the faint band of the Colin western "not a band", which would have changed the CLAIM 033 wording: refused after a pixel profile of the held image (a shallow dip in every column block), `self`, severity high because it would have reached the record.
