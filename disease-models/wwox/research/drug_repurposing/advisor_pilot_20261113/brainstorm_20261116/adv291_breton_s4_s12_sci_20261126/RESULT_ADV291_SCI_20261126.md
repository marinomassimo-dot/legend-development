# RESULT ADV-291 (SCI, window 9bb60ab5, 2026-11-26 UTC; hypothesis level; not medical advice; reference genotype class only): the Breton 2021 S4 figure behind the CLAIM 021 firing sentence, and supplement images S1 and S2

Source: Breton et al. 2021, PMID 34634460; mouse, neuron-specific Wwox knockout (S-KO), heterozygote (S-HT), wild type (S-WT); neocortical slices P13 to P17. Held bytes: `files/supplement/PMID34634460_r2/` (`image1.tiff` = S1, `image2.tiff` = S2, `image4.tiff` = S4; mapping from the docx relationship order and file hashes).

PREREG: `PREREG_ADV291_SCI_20261126.md`, sha256 `38b269993f6f225c26205effadbb6fabf1e6650ae6d282370b38593642b9a340`, frozen 2026-11-26T00:11:49Z (commit `448b25bae`) before any of the three images was opened by this window. My read: `SCI_FIGURE_READ_ADV291.md`, sha256 `8ed230e5deff1b4cefdc06d0445c994563ecf26b1715bf29617d6733ac0bc506`, saved at 00:17Z before the blind reader reported. Blind reader: one `legend-delegate`, `claude-sonnet-5-5`, effort high on all 16 turns (asked sonnet/high); brief `VERIFIER_BRIEF_ADV291.md` (sha256 `d2e6a1406e59adb6aa16f1d7f6a157176e84aa2c7dcb59ce6570b39b5655b66b`); report `VERIFIER_REPORT_AS_DELIVERED_ADV291.txt` (sha256 `e0086e493c067e98f3cebf7ab07d928f6b9a6391e03dfe5810dc6d18b6965526`). The reader's own file write was refused by the Write tool, so the text is the one it handed back, copied from its transcript.

## 0. Answer

* **The series does not close as "nothing changes".** The frozen rejecting observation needs S1 and S2 to carry no sentence that must change; the dossier sentence on S1G is reversed (C1), by my read and by the blind reader's. This holds whatever one decides about S4.
* **S4, raw current (a1): the figure supports "increased firing".** Both reads agree.
* **S4, current referred to rheobase (a2): the plotted points do not obviously agree with the caption's own "p > 0.05 for all combinations".** Knockout lies about 4 Hz above wild type at 60 and 80 pA. What a2 plots is not stated. The figure alone cannot decide, and two verdicts follow (section 2).
* **Two corrections to earlier SCI statements** (section 4), one of which would have written a wrong n into a dose record.

## 1. S4 values (mine / blind), Hz, mean +/- bar half length

n from Table 1, cells/animals: S-WT 13/5, S-HT 15/6, S-KO 40/15. The tests are per cell (inference from the printed n); no per-animal value or animal-level test is recoverable.

| panel, x pA | S-WT | S-HT | S-KO |
|---|---|---|---|
| a1 80 (star) | 3.0 / 2.95 | 9.3 / 9.25 | 10.4 / 10.45 |
| a1 100 (star) | 6.0 / 6.00 | 12.4 / 12.35 | 14.0 / 13.95 |
| a1 120 (star) | 9.9 / 9.90 | 15.4 / 15.4 | 17.5 / 17.55 |
| a1 140 (star) | 13.2 / 13.25 | 18.6 / 18.5 | 21.0 / 21.05 |
| a2 20 | 4.06 / 4.0 | 8.15 / 8.0 | 5.99 / 6.0 |
| a2 40 | 10.1 / 9.9 | about 12 / 12.1 | 11.9 / 11.9 |
| a2 60 | 12.07 +/- 1.1 / 12.0 +/- 1.1 | 16 / 16.0 | 16.0 +/- 0.9 / 16.0 +/- 0.9 |
| a2 80 | 16.0 +/- 1.2 / 16.0 +/- 1.25 | 17.9 / 18.0 | 20.0 +/- 1.2 / 20.0 +/- 1.1 |
| a2 100 | 22.0 / 22 | 20.0 / 20.0 | 22.0 / 22.0 |

All other steps are in the two files. Interneurons (b1, b2): no group difference exceeds one combined bar (both reads). At the starred a1 steps the heterozygote lies within one combined bar of the knockout (both reads; marginal at 140 pA): the figure does not show the raw-current excess to be specific to homozygous loss. WT has no a2 point above 100 pA that either read could use.

**The a2 oddity, seen independently by both:** the a2 values sit within about 0.15 Hz of even numbers. With 500 ms pulses one spike is 2 Hz. Means over 13 to 40 cells would not be expected on that grid, so a2 may plot medians or counts; the caption's "mean +/- standard error" sentence closes a1 only.

## 2. Verdicts

| sentence | mine | blind | note |
|---|---|---|---|
| F-a (CLAIM 021 update (a), the firing sentence) | MUST CHANGE if a2 bars are SEM; ADD if the caption's null is authoritative | MUST CHANGE; UNCHANGED if bars are not SEM, or the caption's null is accepted | both readings kept, not merged |
| F-b (Summary, "increased firing") | UNCHANGED if bars are SEM; MUST CHANGE if the caption's null is accepted | UNCHANGED; if null accepted MUST CHANGE (strict) or ADD | the two sentences move in opposite directions under the two readings |
| C1 (`fulltext_dossiers/PMID34634460.md` line 9) | "8 of 9 significance" reversed | **MUST CHANGE**; "delta" UNSETTLED | agreed |
| C2 (`ampa_nmda_discrim_20261108/output/figure_notes.tsv` FB08) | "a2 the three curves overlap" contradicted by the pixels | **MUST CHANGE** on a2; 0 mV and a1 ADD | agreed; 380 pA is a scale bar, not an event size |
| C3 (`openscientist_retest_20261108` evidence row, "whole-cell recordings separate") | in context (the intrinsic-property cohort) not contradicted | MUST CHANGE if unqualified; UNSETTLED if narrow | not adjudicated; closed package row, no change proposed |
| C4 (`inhibitory_defect_sci47` design review, "separate cells") | several hundred pA holds | same; "separate cells" UNSETTLED | no change |
| C5 (Summary, "increased phase-amplitude coupling") | S1 has no wild-type panel | UNSETTLED from S1 | no change |

**What the earlier reads concluded, against the CLAIM 021 sentence** (ADV asked): `membrane_hypotheses_20261108` (audit row A1.13: four asterisks in a1, none in a2; observation O09: slope unchanged) and FB08 ("a2 the three curves overlap") both agree with the sentence. Neither measured the a2 points. The two pixel reads of this unit do not support "overlap" at 20 to 80 pA. So the earlier agreement does not close the question, and the rejecting observation fails on C1 anyway.

## 3. Proposed sentences (text only; nothing edited; claim_registry goes through BATCH_COMMIT; to IT after its apply report)

1. **CLAIM 021 update (a)**, replace "which rests partly on Supplementary Fig S4 (not held), so the source is internally mixed on firing" by: "which rests partly on Supplementary Fig. S4 (held; read 2026-11-26): at the same raw injected current knockout pyramidal neurons fire more than wild type (a1, asterisks at 80, 100, 120 and 140 pA; about 14 against 6 Hz at 100 pA; Table 1 n 40 cells/15 animals against 13/5; heterozygotes about 12 Hz). With current referred to rheobase (a2) the caption reports p > 0.05 at every step, yet the plotted knockout points lie about 4 Hz above wild type at 60 and 80 pA; what a2 plots is not stated and the figure cannot settle it. The source is internally mixed on firing."
2. **CLAIM 021 update (d)**, "Supplementary Table S1 is not held, so the two are not reconciled here" -> "Supplementary Table S1 (held; noted 2026-11-26) gives CBX duration medians 0.66 to 0.54 s (18 percent), a different statistic from the Fig. 3D bar."
3. **CLAIM 021 wave note**, "(Supplementary Fig S3, not held)" -> "(Supplementary Fig. S3; held, noted 2026-11-26; S3C read in ADV-289: d-APV leaves about 0.4 of baseline at 100 uA)."
4. **ADV-046 Part A line 31**: dated note "Supplementary Fig. S3 is held (noted 2026-11-26); S3B shows the evoked delayed response in both genotypes."
5. **Dossier line 9**, replace "animal-level significance in 8 of 9 for delta" by: "per animal (S1G, n = 9) rho is positive in 8 and negative in 1, and p < 0.05 in 2 (animal 1 positive, animal 3 negative), which is what the caption's 'no significant correlation or negative correlation in 8/9' says; S1G names no frequency band."
6. **FB08** (dated correction, closed package record): "a2: heterozygote and knockout lie above wild type at 20 to 80 pA past rheobase in the plotted points (about 4 Hz at 60 and 80 pA); the caption reports p > 0.05."

**No change:** `CC-20260826-DOSE-DECISION-TABLE-01.md` line 294 (section 4).

## 4. Corrections to what SCI said before

* **ADV-290 was wrong on the dose-decision candidate, and the ADV-291 brief inherited it.** The "Fig S3C age and n" at that file's line 294 is Obeid 2026's figure (the file itself sets "Repudi Fig 2G" against "Obeid Fig S3C" at lines 99 to 101), not Breton's S3C. ADV-290's note "the S3C n is printed (6 slices, 3 animals)" is false there and must not be applied. Sent to ADV and IT during this unit; ADV adopted it and IT recorded that line 294 stays unchanged. I opened no Obeid source.
* **"S4 was read only as a caption" (ADV-290, checkpoint AQ) was wrong**, and so was the PREREG's "no earlier SCI window records reading them" as a premise of novelty: the S4 image had been viewed on 2026-11-07/08 (FB08, A1.13), S2 by FB08, and S1 by FB08 and by the full-text dossier work of 2026-10-19. I found this by the frozen grep, after saving my read; the blind reader saw none of those records' verdicts, only the quoted sentences.

## 5. Source observations (no repository sentence rests on them)

* **S1F is internally inconsistent.** The caption gives rho = -0.1201, p = 0.5674, n = 41, Pearson. The drawn fit line rises; and for r = -0.1201 with n = 41 the two-sided p is 0.4545 (recomputed; S1D's 0.1283 with n = 102 gives 0.1988, as printed). The reader's digitisation of 39 of the 41 dots gave r about +0.15.
* **S4 a2 against its caption**: a candidate author question (what a2 plots, and the test behind "p > 0.05"). Not sent; no contact.
* If the a2 offset were real it would be an intrinsic-gain difference past rheobase, in heterozygote and knockout, beside their higher input resistance (Table 1: about 143 against 103 Mohm). This is a hypothesis only, not tested here, and the a2 statistic is unidentified.

## 6. DEFAULTS_TAKEN and limits

* DEFAULT: the two readings of F-a are both reported; choosing between them changes claim wording and is left to ADV.
* DEFAULT: C1 to C5 are my selection from 145 grep lines that cite the source on the same line; my filter skipped delegate reports, verbatim files, audit and verify folders, triple files, corpus seeds and python files, so a sentence living only there is not covered. Grep scope: `disease-models/wwox/` and `framework/`, md, tsv, txt, py files that mention the PMID, the author or CLAIM 021.
* Low-resolution rasters; read error about +/- 0.2 Hz. "Over combined bar" is a screen, not a test. S2 prints no genotype, cell count or animal count.
* Nothing here concerns a human or a treatment.

## CORRECTION 2026-11-26 (SCI successor; own file; ADV and IT's second blind check)

"The dossier sentence on S1G is reversed" (summary, item C1) is not right as a headline. The paper's own Results say "For the delta range, 8/9 subjects showed significant coupling" by the authors' criterion; S1G's animal-level rho is positive in 8 of 9 animals with p < 0.05 in 2 (animal 1 positive, animal 3 negative). The two statistics differ and the dossier line mixes them without a label: **ambiguous, not reversed.** Read C1 and section 3 item 5 as: label which statistic is which (authors' criterion 8 of 9 for delta; S1G animal-level p < 0.05 in 2 of 9; S1G names no band). Also: S4 a1's test unit is not stated and the caption's "mean +/- standard error" does stand in the a1 entry (IT's R5). IT applies its own wording to the dossier and CLAIM 021 (claim_registry only through BATCH_COMMIT).
