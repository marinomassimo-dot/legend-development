# GCN2 versus PERK in WWOX-deficient systems: is there a measurement? (2026-10-28)

Research layer. NOT WWOX EVIDENCE of a mechanism. Question carried from the ISR need (NEED-ISR-ATTENUATION, observation O5): which eIF2 kinase, if any, drives the integrated stress response in a WWOX-deficient neural system, so that a compound search starts from a kinase and not from the pathway name.

## Verdict

**No measurement of phospho-GCN2 or phospho-PERK (or phospho-eIF2alpha) in a WWOX-deficient neural system was found.** The search was PubMed abstracts plus a targeted look at the open full text of the one closest paper; it is thin (three to four hits for WWOX with ISR/UPR terms) and supplements or preprints could hold a measurement it would not see. Absence here is "not found in this search", not "does not exist".

## What exists

| Source | System | What was measured | Reading depth |
|---|---|---|---|
| Lucas-Clarke 2026 (PMID 42909904, Drosophila) | neuronal wwox knockdown plus Abeta42 | Atf4 immunostaining up; an Ire1-Xbp1 splicing reporter flat; PERK-Atf4 is inferred by exclusion, the authors state they did not determine how WWOX acts on the pathway | repository receipts FTR-20261026-42909904-01 and -02 (existing); question-driven re-read 2026-10-28 (receipt staged `FTR-20261028-42909904-03`, partial) for this question (section below) |
| PMID 28749468 (ovarian cancer cells, paclitaxel) | WWOX re-expression, WWOX siRNA | ER-stress apoptosis with IRE1 and PERK activation; siRNA reverses it | abstract only; not neural, not WWOX-null at baseline |
| GSE156243 reanalysis (repository) | WWOX-KO organoids, transcripts | ISR target transcripts (CHAC1, TRIB3) lower than chance: a transcript-level negative in one tissue | repository record |

## Line-by-line re-read of the fly paper for this question (2026-10-28)

Targeted re-read of the Results section "Wwox knockdown in the presence of Abeta42 increases lactate concentrations via Atf4", the Figure 5 legend and the Discussion paragraphs on Atf4, PERK and GCN2, from the Europe PMC open full text. The paper already carries two full-text receipts; the question-specific re-read of 2026-10-28 is staged as a third, partial receipt (`FTR-20261028-42909904-03`), which makes no new coverage claim for sections not re-read. Findings:

- **No western blot, no phospho-eIF2alpha, no phospho-PERK, no phospho-GCN2, no puromycin incorporation, no ISRIB or kinase inhibitor, and no Gcn2 or Perk manipulation appear anywhere in the text.** The only ISR readout is Atf4 immunocytochemistry in dissected brains (Figure 5H-I): Mann-Whitney U = 0, P = 0.0022, six brains.
- **The Atf4 rise was seen only in the amyloid arm; the no-amyloid arm was not significant.** It was seen after Wwox knockdown in Abeta42-expressing flies (Mann-Whitney U = 0, P = 0.0022, 6 vs 6) and was "not observed" in LacZ-expressing Wwox knockdown flies (Supplementary Figure 5D-E, opened as legend text on 2026-10-28: t = 0.0894, P = 0.9305, 6 brains). The two arms are separate tests and no interaction test is reported, so "needs amyloid" is a difference in significance between two arms, not a demonstrated interaction, and the no-amyloid arm is not a demonstrated absence (95% interval about +/- 1.3 pooled SD).
- **"PERK-Atf4 branch" is an inference by exclusion.** The only other arm tested is an Ire1-Xbp1 splicing reporter (t = 1.365, P = 0.1954, six to nine animals): a non-significant result at that size, which does not exclude an Ire1 effect. PERK itself was not measured, and neither was GCN2.
- **The authors say so.** The Discussion: "we did not determine whether WWOX is activating this pathway directly in this study"; it then offers both PERK (by proximity) and GCN2 (by GCN1 binding) as candidate routes, which is the open question of this note.
- The Atf4-over-HIF1alpha preference rests on an unchanged Sima:GFP reporter (Figure 5F-G) and on prior literature, not on an Atf4 loss-of-function experiment in this paper.

Net: the fly paper cannot discriminate PERK from GCN2, and the Atf4 signal is context-dependent. Both statements are within what the authors claim; the point is that nothing downstream should treat PERK as measured.

## The two interaction claims in the fly paper's Discussion, traced (revised 2026-10-28, step B3)

The fly paper says WWOX "can interact in proximity with PERK" (its reference 58) and "directly binds GCN1" (its reference 56). The first version of this note checked both cited papers by keyword only and reported GCN1 as absent from reference 56. That was incomplete: the supplementary data of reference 56 were already local and hold a GCN1 row. Both papers were then read in full text with their supplementary data (details, depth and limits in [`isr_kinase_interactome_atf4_reconciliation_it4_20261028.md`](isr_kinase_interactome_atf4_reconciliation_it4_20261028.md)):

- Reference 56 (Hussain et al. 2018, WWOX interactome by tandem affinity purification-mass spectrometry in HEK293T cells with tagged full-length WWOX): GCN1 is present in the supplementary prey list (Data Sheet 2) with 2 and 8 spectra in the two replicates, interaction score 0.133, CRAPome frequency 0.16. The authors' "good candidate" line is 0.2 and their high-confidence line 0.3; GCN1 is not discussed, not validated, and no empty-vector control is described. "Directly binds GCN1" is **not supported**: it is a low-score, unvalidated co-purification. PERK, GCN2, HRI, PKR, eIF2alpha and ATF4 do not appear in the lists.
- Reference 58 (Sassano et al. 2021, PERK proximity biotinylation): the experiment is BioID with PERK-BirA* in HEK293-T cells, mock-transfected parental cells as control. WWOX is one row (3 spectra, 3 exclusive unique peptides, none in control); GCN1 is a stronger hit in the same list (10 spectra). It is a proximity-list entry: not a binding result, not an activation result.

Consequence: the mechanistic bridge from WWOX to either kinase rests on two weak interactome entries from over-expression systems and one by-exclusion inference. It orients a measurement; it does not choose a kinase. The same reading showed that the fly paper's Atf4 comparison between backgrounds is two separate two-group tests (no interaction test) and that the "no change without amyloid" arm is a non-significant result, not a demonstrated absence.

## Experiment to discriminate the kinases

The design in this note's first version (a same-lysate western with inhibitors and positive controls) is **superseded**: it did not separate kinases from basal tone, relied on inhibitors with documented selectivity problems (and on ISRIB, which acts downstream of all four kinases), and had no timing or context arms. The revised design (fly 2 x 2 with kinase arms; human isogenic knockout and rescue lines; kinase attribution by genetic interaction; pre-registered decision table) is in section 6 of the reconciliation note. Design only; nothing run.

## Consequence for the compound search

Until this is measured, ISR compounds stay `exploration_candidate`, not `consistent_mechanism_candidate`, and no kinase-specific inhibitor is prioritised. The 2026-10-28 catalogue holds no ChEMBL mechanism row for EIF2AK4; the antipsychotic rows linked to it are pharmacogenomic associations.

## Worth a full-text read (status 2026-10-28)

1. PMID 42909904 Methods and Figure 5, line by line (open access): the Atf4 and Xbp1 parts were re-read for step B3; the figure images of Supplementary Fig 5D-G were not re-opened (direction of the Xbp1 difference is not in the legend text).
2. PMID 42397075 (Brain 2026, KO and patient neural organoids): abstract only so far; the supplementary differential-expression tables are the place to look for ISR/UPR genes. Full text and supplement need a browser click (an existing open item).
3. PMID 31543760 (WWOX-silenced human neural progenitors, CAGE transcriptome): check ATF4 targets and mitochondrial genes (open access).
4. Done in step B3: the supplementary tables of reference 56 (GCN1 found, low score) and the full text of reference 58.
