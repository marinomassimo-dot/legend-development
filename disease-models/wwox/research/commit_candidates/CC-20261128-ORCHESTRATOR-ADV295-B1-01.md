# COMMIT CANDIDATE — CC-20261128-ORCHESTRATOR-ADV295-B1-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-295 block 1 consumers) · **Date:** 2026-11-28 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin:** SCI's ADV-295 block 1 (`drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv295_one_consumer_batch_sci_20261126/SENTENCES_FOR_IT_ADV295_BLOCK1_SCI_20261126.md`, sections A and B). **Checks:** one blind round by `legend-delegate` (sonnet, effort high stated in the dispatch and read back, 24 turns), packet and report as delivered in `adv295_consumers_it_20261126/`.
**Status:** PROPOSED, for `BATCH_20261128_001`.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** Dated wording corrections in one claim record and three discovery-ledger records; no status, grade or flag changes. DL-THER-089 clause (ii) is decision-bearing: the BLOCK-1 reason may no longer cite a model-dependent Wnt direction from Helton 2026.

## 2 · Proposed wording (old = verbatim record text)

**DL-THER-089 / 1** *Old:* «so **Wnt direction in neural tissue is model-dependent**»

*New:* «so, in this study, the direction of the Wnt-activation effect is the same in both models (Axin2 fell in the epileptogenic zone and was restored to baseline by the GSK3 inhibitor in both; remodelling was reduced in both) and only the number of remodelling markers that respond differs; a model-dependent Wnt direction is not shown by this paper (immature dentate granule cells, mouse, about 2 weeks after kainate, one dose); in the contralateral dentate gyrus Axin2 did not fall although remodelling occurred and was reduced by the drug, so Axin2 restoration does not account for every effect»

**DL-THER-089 / 2** *Old:* «(the ipsilateral count unchanged)»

*New:* «(the ipsilateral immature (POMC-GFP+) cell density, which kainate reduced markedly relative to saline controls (Fig 3E), was not significantly changed by the drug; n = 6 per group per Methods 2.8)»

**DL-THER-089 / 3** *Old:* «histology and immunohistochemistry at day 14 only»

*New:* «histology and immunohistochemistry at day 14 only for the epilepsy-model outcomes (plus a single-dose Axin2 time course at 3 h and 24 h, and body weight over the treatment period reported only as no effect, with Supplemental Figure 1)»

**DL-REPO-003 / 1** *Old:* «compounds that *«potentially increase»* WWOX expression»

*New:* «compounds *«potentially increasing»* WWOX expression»

**DL-REPO-003 / 2** *Old:* «cell type, dose, species and readout (transcript or protein) are unknown»

*New:* «cell type, dose and readout (transcript or protein) are not given in the deposited sheet (nor in the paper's main text); the species is Homo sapiens in every row of the sheet»

**DL-REPO-003 / 3** *Old:* «valproate LOWERS WWOX expression in human cells»

*New:* «valproate LOWERS WWOX expression in Homo sapiens (cell or tissue type not given; per the deposited sheet)»

**CLAIM 032 / 1** *Old:* «**Not examined:** the remaining WWOX allele (exome was done in six other patients), RNA, protein, follow-up.»

*New:* «**Not examined (as far as the paper reports):** the remaining WWOX allele; no WWOX sequence result is given. Exome sequencing was done in six selected patients, of whom four are named (P7, P16, P17, P18) and two are not; whether this patient was one of them is not stated. No RNA, protein or follow-up is reported.»

**DL-METH-118 / 1** *Old:* «the absence is DRG-specific, not article-wide»

*New:* «incidence and severity are summarised (Fig 6C) for brain only; the absence of tabulated incidence applies to every non-brain site the text lists as affected, DRG among them»

## 3 · Checks and what was changed by them
Blind round (full sources, text only, no figure images): A1 STANDS (contralateral Axin2 clause added); the ipsilateral count clause lost "about 10-fold by eye" (magnitude not in the text, Fig 3E not read); "daily body weight" was not in the text and is now "reported only as no effect"; A2a grammar fixed and the sheet-dependent clauses (A2b, A2c) stay attributed to the deposited sheet, which the blind reader could not see (SCI's two auditors verified it); B1 STANDS; B2 (portfolio, not a current file) now cites the Fig 2 legend counts and labels Table S3 as not in the text the reader had; B3 reworded "summarised (Fig 6C)". Not applied: SCI's optional ADDs for B1 (inheritance) and B3 (chain steps 2 and 4), and the first-reader-only items. One open point for SCI: the ledger line also says "Table S7" for the deposited CTD export while the paper cites Table S6 for the compound lists.

## BATCH DISPOSITION — `BATCH_20261128_001` (2026-11-28, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED as section 2 states (CLAIM 032 by `batch_commit.py propagate`, one op; the ledger by record-addressed replacements; RP-033 `next_action` fixed in `research_portfolio.tsv` outside the batch). MINOR.
