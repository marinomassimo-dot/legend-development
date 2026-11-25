# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV279-WORDING-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (checkpoint 21, section 1) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin:** SCI, ADV-279 increments 1 and 2 (`advisor_pilot_20261113/brainstorm_20261116/adv279_next_ten_held_partials_sci_20261125/`).
**Status:** see the batch disposition at the end.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Items 1 to 5 and 7 to 9 concern other diseases or systems: NOT WWOX EVIDENCE.

## 1 · CHANGE CLASS (stated before any apply)
**MINOR.** Wording only. No claim created, reversed or promoted; no status, grade, direction or ranking change.

## 2 · Who checked what
* **The five strict findings (items 1, 2, 5, 6, 7) were re-derived by IT** from the held files on 2026-11-25 (hashes equal to SCI's list): text search and S2 figure and response to reviewers (33914734); Supplementary Figure 3 and the unedited blots (42875792); Supplementary Figure 12 (30266908); whole-XML search (34359949); the fit table of Supplementary Figure 6B and the text (37275776). All five hold, with the limits below. Receipts `FTR-20261125-<pmid>-02`, depth `queried_not_full_read`.
* **Search behind item 6**, 2026-11-25, on `files/fulltext/PMID34359949_Hsu2021_PMC.xml` (sha256 prefix 9a5985d0ce548f3f): every paragraph, caption, title and table cell; sentences containing «tau» and one of `SDR|short-chain|direct|bind|interact` (9 hits, reference titles excluded); whole-text patterns `directly binding Tau` (1), `By direct binding` (1), `direct(ly)? bind...tau` (1), `tau...direct` (1), `SDR...tau` (3), `tau...SDR` (2).
* **One blind verifier** (sonnet, effort high) on the statements that reach the current files (items 1 and 6): `it_adv279_verify_20261125/`. It rejected the old wording and the abstract-only negative, and added limits now carried: the yeast-lysate attempt is only in the response to reviewers; no wild-type activity is reported for the E. coli assay; the Results and the Discussion disagree on the Pichia report; the second section-7 sentence does not name tau as the bound partner; section 10.3 also speaks of binding tau.
* **Loose items 3, 4, 8, 9** are applied as SCI's reading, checked by SCI's blind delegate on facts, **not re-derived by IT**.

## 3 · Applied by the ordinary route (own commit)
| Item | PMID | Where | One line |
|---|---|---|---|
| 1 | 33914734 | cards A02, A05; mechanism-intervention map; `HYP-20260709-08` update; evidence-graph label; `repurposing_10h_scientist-a_20261021.md`; note on `broad_recovery_it6_p6_20261029/README.md`; `test_repurposing_join.py` (it pinned the old sentence) | activity of the accumulated protein **not measured**, not «no measurable activity» |
| 2 | 42875792 | card A02; the same report | HIKESHI protein return weakly shown |
| 3 | 28749468 | `DL-MECH-023` | supplementary PERK panel does not show induction |
| 4 | 37781246 | `DL-MECH-054` | drivers in two of four lines, opposite sign |
| 5 | 30266908 | card A01 `DR-A01-008` | sorbitol effect not established; trehalose carries the arm |
| 6 | 34359949 | dossier `PMID34359949.md` | the «zero times in the body» negative is false |
| 7 | 37275776 | card `EB-ETX-01`; `drug_repurposing/README.md` | wild-type GIRK1/2 about 1.2 mM, above the band; 0.55 mM is the K78R variant |
| 8 | 37248434 | `DL-MECH-115` | binding retained with Y33R; equality not measured |
| 9 | 36278433 | card E02 `DR-E02-006` | source data give 95 days, not 97, for the treated arm; two doses stated |

## 4 · For the batch (current files)
* `CLAIM 043`, leg L7 of the Summary.
* `PAPER 141`, first part of Role.
* `PAPER 434`, the 2026-10-29 reading update.
* `LIT-0706`, Note.

**`CLAIM 011` is not changed.** SCI listed it as a consumer of item 4; its only sentence citing PMID 37781246 is about proliferation in one of four glioblastoma lines and says nothing about HSF2BP or POLE4 (read in place, 2026-11-25).

## 5 · What is left as it stands
Dated snapshot artefacts that quote the old A02 text (`p5/cells.json`, `p5/tables_deep.md`), the IT6 P6 card copy (noted in its README) and the generated pathograph rows are not rewritten. The deepdive manifest of PMID 34359949 keeps its old proposition; the dossier note supersedes it. A dream-pass line from SCI (of card A02's three precedents only the CBS mouse work, not re-read here, still carries an activity measurement in either direction) changes no ranking.

## BATCH DISPOSITION — `BATCH_20261125_006` (2026-11-25, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED. Section 3 landed by the ordinary route in the commit before the batch; section 4 by `batch_commit.py propagate`, record-scoped, 5 ops on `CLAIM 043`, `PAPER 141`, `PAPER 434` (two) and `LIT-0706`. Change class restated: MINOR. `WM_v7.29` preserved.
