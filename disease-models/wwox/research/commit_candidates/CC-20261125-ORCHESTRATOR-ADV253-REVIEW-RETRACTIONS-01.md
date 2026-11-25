# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV253-REVIEW-RETRACTIONS-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-253 wording, relayed by SCI at ADV's request; a peer message, not operator authority) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the finding:** `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv253_retraction_consumers_sci_20261125/RESULT_ADV253_RETRACTION_CONSUMERS_SCI_20261125.md` §§ 3, 4 and 6 (SCI, one reader: the review's Figure 3 legend, text and reference list, and the retracted article's figures). IT checked in PubMed (2026-11-25) that PMIDs 19357348, 15240510, 26041563, 25447306 carry the Retracted Publication type and that the notices for 19357348 and 15240510 are PMIDs 42583763 (2026-08-12) and 42713750 (2026-09-09); IT did not re-read the review.
**Status:** PROPAGATED (`BATCH_20261125_004`; see the BATCH DISPOSITION block at the foot). No registry file is edited by this act. Ordinary-route lines (discovery ledger `DL-MECH-025`, the two analysis censuses, `CC-20261019-SCIENTIST-C-H4-01`) were placed the same day and are not part of this candidate.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** Narrows one over-stated sentence («the review reuses its data and dependencies») in five places. The exclusion of the review, the absence of any baseline claim that depends on it, and every status stay as they are.

## 2 · Proposed replacement (English; the old phrase, then the new)
Old (working model line 81 and `disease_model.md` line 33): "…and the review (PMID 28045433) reuses its data and dependencies." / "…and a review (PMID 28045433) reuses its data/dependencies."
New: "…and review PMID 28045433 cites five retracted articles of its own group (25447306, 19357348, 26041563, 28151481, 15240510). Its Fig 3B cites the protocol of retracted PMID 28151481 and gives the same decitabine value for Wwox (0.2x); its blot images, Beclin-1 and p62 were not found in that article. Not usable as support for any of it."
Note on the date: "retracted in 2022" is right for 28151481 only; 25447306 was retracted in 2020 (notice 32746981, per SCI); 19357348 and 15240510 in 2026.

| Record | Change |
|---|---|
| `working_model_current.md`, Integrity exclusion line | the replacement above |
| `disease_model.md`, Integrity exclusion line | the replacement above (narrative view of the same sentence) |
| `paper_registry_current.md` `CORPUS-STUB-061`, Note | append: "Correction 2026-11-25 (ADV-253): the review cites five retracted articles of its own group (25447306, 19357348, 26041563, 28151481, 15240510); its Fig 3B cites the protocol of 28151481 and gives the same decitabine value for Wwox (0.2x); its blot images, Beclin-1 and p62 were not found in that article. 'Riusa dati del primario' therefore holds for one value, not for the figure. Status unchanged." |
| `literature_tracking_log_current.md` `LIT-0085`, Note | the same sentence |
| `literature_tracking_log_current.md` `LIT-0401`, Note | replace "reuses data from this source and is therefore" with "cites this source and gives its decitabine value for Wwox, and four other retracted articles of its group, and is therefore" |

## 3 · What this does NOT do
No status, flag, next-action or claim-link change; no promotion; nothing about any person's conduct; the batch-queue flag for PMID 19357348 is not hand-edited: `batch_queue.md` is generated from the dated PubMed seed snapshot (`_integrity` in `framework/scripts/batch_queue.py` reads the publication type), so the row stays unflagged (notice 42583763, 2026-08-12, newer than the 2026-08-06 snapshot) until the next `pubmed_corpus_harvest` snapshot is registered, which carries the Retracted Publication type. SCI's ADV-256 rows (a) 19357348 and (b) 28386169 (Retraction Watch duplicate-publication removal, no PubMed or Europe PMC mark: audit only) are therefore a note for that harvest, not an edit; rows (c) are correction annotations with no hold. No consumer of 19357348 was found by SCI.

## 4 · Statements for the blind check at propagation time
1. The review's Figure 3 legend cites reference 64 (PMID 28151481) for panel B; the text cites it for the HGF/Met down-regulation.
2. The review's reference list contains 25447306 (ref 41), 19357348 (ref 42), 26041563 (ref 58), 28151481 (ref 64) and 15240510 (ref 78), all marked retracted in PubMed.
3. In the open XML and figures of PMID 28151481, Wwox under decitabine is a bar chart (Fig 6a) of about 0.2; no Beclin-1 or p62 blot appears.

## 5 · Blind check and the wording that propagates (IT, batch 2, 2026-11-25)
Statements 1 and 2 (the review's Figure 3 legend and reference list): call A, SUPPORTED (`drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_batch2_verify_20261125/VERIFIER_REPORT_AS_DELIVERED_BATCH2A_IT_20261125.md`; the delegate was told not to check retraction status). Statement 3 and the retraction types: call E (`VERIFIER_REPORT_AS_DELIVERED_BATCH2E_IT_20261125.md`): the five originals carry the Retracted Publication type; notices: 25447306 32746981 (2020-07-23), 26041563 32799870 (2020-08-15), 28151481 35680840 (2022-06-09), 19357348 42583763 (2026-08-12), 15240510 42713750 (2026-09-09). In PMID 28151481 the decitabine result on Wwox is a bar chart (Fig 6a, 1833 breast-carcinoma cells in vitro, three experiments, about 0.2 of control read from the image); in its xenograft IHC (Fig 7a) Wwox increases under decitabine; no Beclin-1 or p62 appears in the text or in the blots of Figures 4, 5b, 6 and 8c (Figures 1, 2, 3, 7 and the supplements not viewed). **Stays out:** «its Fig 3B gives the same decitabine value for Wwox (0.2x)» (the review's own figure value was not re-read by a second reader).
**Replacement sentence (working model and `disease_model.md`):** «...and review PMID 28045433 cites five retracted articles of its own group (25447306, 19357348, 26041563, 28151481, 15240510) and cites 28151481 for its Figure 3B decitabine experiment on Wwox; in that article the decitabine result on Wwox protein is a bar chart of about 0.2 of control in vitro, and no Beclin-1 or p62 blot was found in its text or in the blots viewed. Not usable as support for any of it.»
**Registry notes (`CORPUS-STUB-061`, `LIT-0085`, `LIT-0401`):** the same, with the dates above («retracted in 2022» holds for 28151481 only; 25447306 and 26041563 in 2020; 19357348 and 15240510 in 2026).

## BATCH DISPOSITION — `BATCH_20261125_004` (2026-11-25, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED (verified remainder)

1 `replace-within` op on `working_model_current.md` (Metabolic branch refinement, integrity line), 1 on `paper_registry_current.md` (CORPUS-STUB-061), 2 on `literature_tracking_log_current.md` (LIT-0085, LIT-0401); `disease_model.md` by the ordinary route. **Change class restated: MINOR.** **Blind check:** calls A and E of batch 2: statements 1 and 2 SUPPORTED (call A), statement 3 SUPPORTED with a coverage limit (Figures 4, 5b, 6 and 8c viewed; the others and the supplements not), notices and dates read from PubMed (call E). **Left out:** the clause that the review's Fig 3B gives the same decitabine value (0.2x), which no second reader re-read.
