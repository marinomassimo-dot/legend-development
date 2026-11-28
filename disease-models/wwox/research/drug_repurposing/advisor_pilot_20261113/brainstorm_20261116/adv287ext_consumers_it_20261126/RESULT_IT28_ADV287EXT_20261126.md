# IT28, 2026-11-26: ADV-287 extension (H02, A01, random 20) and HE's ADV-293 M01 sentence applied to the cards

Hypothesis level; reference genotype class only; nothing here is medical advice. Inputs: SCI's `RESULT_ADV287EXT_SCI_20261126.md` (sections 2, 3 and 4; main 6851f57b1) and HE's `IT_SENTENCE_M01_tazemetostat_exposure_20261126.md` (main 8637c9d78).
Text: `edits_287ext_it28.py` (28 fragment replacements, each old fragment unique in its field); `apply_287ext_it28.py`; packets `BLIND_PACKET_{H,A,R,M}_287EXT_IT28.txt`; reports as delivered `VERIFIER_REPORT_AS_DELIVERED_{H,A,R,M}_287EXT_IT28.txt`.

## Applied (11 card packets: A01, A02, A03, D01, E04, F01, H02, J01, L01, M01, P11)
| Kind | Items |
|---|---|
| SCI section 2, verified MUST CHANGE | H02-26 (label names no study; PMID 19054414 abstract level only), A01-04 (per-panel Guiberson 2018 values), R-34 (Fabry GLA assays differ), R-37 (nuclear-to-cytosolic beta-catenin about 1.7 fold, Steinberg 2021 Fig 4E) |
| SCI section 3, held apart | R-35 (E04: Chong 2023 reports a ketogenic response in 3 of 5, patients 1, 2 and 4; lactate range unfound in the held chunks), A01-03 (for G544D), R-24 (A02) |
| SCI section 4, ADD | H02-03, H02-05, H02-17, H02-29, A01-08, A01-11, A01-13, A01-14, A01-15, A01-16, R-04, R-05, R-06, R-07, R-08, R-11, R-19, R-29 (R-01 already carried HMOX1, SRXN1 and GSR) |
| HE, ADV-293 | M01 tazemetostat exposure clause |
Not applied: H02-10 (not assessable), A01-09 (no wording given), R-33 and R-39, H02-12 and the other not-assessable items; DA-H02-001 notes outside the 59 (not audited).

## Blind rounds (legend-delegate, sonnet, effort high stated and read back: 14, 28, 76 and 3 turns)
Packets carried the new fragment in its field and the whole held sources, never a card or a result file. Reader R disclosed that a grep on the named supplement folder also printed a repository reading note; no verdict rests on it.
* H (5 blocks): 5 STANDS (two optional ADD: label wording softened to "gives the figures without naming a publication"; the 218 further exclusions of the Wan 2022 cohort added).
* A (5 blocks): 1 MUST CHANGE (A01-13 closing sentence: "Shows ... which butyrate does not engage" said more than the source and the butyrate half is not in it), 2 ADD (A01-08 and A01-16: neuron wild type rose about 1.3, n = 5; A01-13: the two comparisons named, 749.41 against 1341.01 and the tabulated rows, two sham in the tables against three in the Methods; "dose" for "exposure level"), 3 STANDS with precision notes (not in neurons became "no significance mark"; soluble range 1.7 to 2.4).
* R (12 blocks): 1 MUST CHANGE (R-07: "not wild-type-like" contradicted the authors' text for SCAR12), 8 ADD (R-34, R-37, R-35, R-24, R-29, R-19 and the adjoining clauses of R-04, R-11, R-05), 3 STANDS (R-06 with one UNSETTLED, R-08 with 16 dots counted, R-04 fragment).
* M (1 block): ADD, "one measured ratio exists" softened to "the abstract reports one ratio"; dose, time point and n are not in the abstract.
* First-composition rate for ADV-286 (this set was built from SCI-verified inputs): MUST CHANGE 2 of 23 blocks (9 percent); any required change (MUST CHANGE or ADD) 11 of 23 (48 percent). SCI's sampling band for corrected cards (4 of 49, 8 percent) is the right comparator for the first figure; the two are not one measure.
* The folds after the blind round were not blind-checked a second time (stated limit). A first reader could not see the vigabatrin label text (not held in this checkout): the label clause stands on SCI's verification of the held sibling labels.

## Checks
`check_cards.py` 30 packets 0 problems; join, coverage, ranking (order digest `ff38fcaa61295a5a` unmoved), view trio in every language for both editions, i18n collect, shareable package. No BATCH_COMMIT (cards only, as IT26 and the first IT28 batch); no ledger, WM or claim change.
