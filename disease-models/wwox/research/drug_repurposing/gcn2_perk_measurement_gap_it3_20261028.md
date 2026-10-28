# GCN2 versus PERK in WWOX-deficient systems: is there a measurement? (2026-10-28)

Research layer. NOT WWOX EVIDENCE of a mechanism. Question carried from the ISR need (NEED-ISR-ATTENUATION, observation O5): which eIF2 kinase, if any, drives the integrated stress response in a WWOX-deficient neural system, so that a compound search starts from a kinase and not from the pathway name.

## Verdict

**No measurement of phospho-GCN2 or phospho-PERK (or phospho-eIF2alpha) in a WWOX-deficient neural system was found.** The search was PubMed abstracts plus a targeted look at the open full text of the one closest paper; it is thin (three to four hits for WWOX with ISR/UPR terms) and supplements or preprints could hold a measurement it would not see. Absence here is "not found in this search", not "does not exist".

## What exists

| Source | System | What was measured | Reading depth |
|---|---|---|---|
| Lucas-Clarke 2026 (PMID 42909904, Drosophila) | neuronal wwox knockdown plus Abeta42 | Atf4 immunostaining up; an Ire1-Xbp1 splicing reporter flat; PERK-Atf4 is inferred by exclusion, the authors state they did not determine how WWOX acts on the pathway | repository receipts FTR-20261026-42909904-01 and -02 (existing); this session: full text of the Discussion and reference list searched by keyword, not re-read line by line |
| PMID 28749468 (ovarian cancer cells, paclitaxel) | WWOX re-expression, WWOX siRNA | ER-stress apoptosis with IRE1 and PERK activation; siRNA reverses it | abstract only; not neural, not WWOX-null at baseline |
| GSE156243 reanalysis (repository) | WWOX-KO organoids, transcripts | ISR target transcripts (CHAC1, TRIB3) lower than chance: a transcript-level negative in one tissue | repository record |

## The two interaction claims in the fly paper's Discussion, traced

The fly paper says WWOX "can interact in proximity with PERK" (its reference 58) and "directly binds GCN1" (its reference 56). I opened both cited papers in Europe PMC full text (keyword search only, not a line-by-line read):

- Reference 56 (Hussain et al. 2018, WWOX interactome by tandem affinity purification-mass spectrometry): the full text contains no mention of GCN1, GCN2 or EIF2AK4. If GCN1 is in that paper it is in a supplementary table that was not opened. "Directly binds" is therefore **not supported by the text of the cited paper** as far as this check can see.
- Reference 58 (Sassano et al. 2021, PERK interactome): WWOX appears once, as one row (three peptides) in a long mass-spectrometry list. That is a proximity-list entry, not a functional or activation result.

Consequence: the mechanistic bridge from WWOX to either kinase rests on two interactome list entries and one by-exclusion inference. It orients a measurement; it does not choose a kinase.

## Smallest discriminating experiment (design only, nothing run)

Same-lysate western in WWOX-KO or patient-derived neural cells and in Wwox-null brain, with a WWOX re-expression arm: phospho-GCN2 (T899) with total GCN2, phospho-PERK (T980) with total PERK, phospho-eIF2alpha (S51) with total, ATF4 protein; positive controls halofuginone or histidinol (GCN2) and thapsigargin (PERK); a GCN2 inhibitor and a PERK inhibitor to see which lowers phospho-eIF2alpha; puromycin incorporation as the functional output.
Reading: phospho-GCN2 up with phospho-PERK flat is the PARS2-like pattern; the reverse is the ER-stress pattern; both flat with ATF4 up points to a third kinase (HRI, PKR) or a non-canonical route.

## Consequence for the compound search

Until this is measured, ISR compounds stay `exploration_candidate`, not `consistent_mechanism_candidate`, and no kinase-specific inhibitor is prioritised. The 2026-10-28 catalogue holds no ChEMBL mechanism row for EIF2AK4; the antipsychotic rows linked to it are pharmacogenomic associations.

## Worth a full-text read (not done here)

1. PMID 42909904 Methods and Figure 5, line by line (open access).
2. PMID 42397075 (Brain 2026, KO and patient neural organoids): abstract only so far; the supplementary differential-expression tables are the place to look for ISR/UPR genes. Full text and supplement need a browser click (an existing open item).
3. PMID 31543760 (WWOX-silenced human neural progenitors, CAGE transcriptome): check ATF4 targets and mitochondrial genes (open access).
4. The supplementary tables of reference 56, for GCN1.
