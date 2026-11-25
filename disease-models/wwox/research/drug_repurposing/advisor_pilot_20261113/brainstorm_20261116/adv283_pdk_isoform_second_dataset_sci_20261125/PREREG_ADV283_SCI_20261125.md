# PREREG, ADV-283: PDK isoform pattern in a second held WWOX-deficient neural dataset (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Written and hashed before any PDK value of any dataset below was opened. What was opened before this file: the first dataset's own PDK rows (GSE156243, ADV-282 result section 7), the column names and sample names of the candidate tables, and the series summary of GSE126075. No expression value of a candidate dataset was opened.

## 1. Anchor (unit-and-n check done first)

GSE156243 (Steinberg 2021, PMID 34268881): human WiBR3-derived cerebral organoids, week 15, bulk RNA-seq, one library per replicate, 4 WWOX-knockout against 2 wild-type libraries. PDK3 1.55 times = mean CPM of the 4 knockout libraries (10.47) over mean CPM of the 2 wild-type libraries (6.77); raw counts knockout 425, 394, 455, 322, wild type 263, 194; all four knockout above both wild type; nominal P 7.39E-03, adjusted p 5.65E-02 in the authors' list. PDK1 0.78 times (all four knockout below both wild type), PDK2 0.91, PDK4 1.37 (overlapping). Two wild-type libraries: no rank test can reach two-sided P below 0.133. The anchor is a single-deposit, small-n observation, not a replicated effect.

## 2. Prediction and rejecting observation (frozen)

* **Prediction:** in the WWOX-deficient arm PDK3 is higher and PDK1 is lower than in its control arm, in a held dataset independent of GSE156243.
* **Rejecting observation (SCI's, proposed in ADV-282):** PDK3 is not higher in a second independent dataset. Operational form below: in every primary comparison where PDK3 is detected, PDK3 fails the "higher" rule. The statement "single-dataset observation" then stands for the cards and PDK3 is not carried as the relevant isoform on this evidence.
* Quantitative priors (written before reading): PDK3 meets the "higher" rule in at least one primary comparison, 35 percent; PDK3 higher and PDK1 lower together in at least one, 15 percent; no primary comparison is testable for PDK3 because it is not detected, 20 percent. The anchor is nominal in one deposit and the second systems differ (mouse tissue, a different deletion, nuclei, a CAGE promoter table), so the prediction is more likely to fail than to be supported.

## 3. Qualifying datasets, independence, and what each can say

All are held in `files/geo/` (no acquisition, no spend, no contact). Independence from GSE156243 means: different laboratory, different deposit, different biological system. Pooling across datasets is not done.

| id | tables held | species, system, age | arms and n (libraries, one per animal or culture) | measure | primary comparison |
|---|---|---|---|---|---|
| D2 GSE158681 | transcript TPM, hippocampus | mouse, in vivo hippocampus, P17 (Repudi 2021, PMID 33914858 by identical n per arm; the deposit itself states no paper) | global null KO 2 v WT 3; neuron-targeted (Synapsin-Cre, "S") KO 3 v Ctrl 2; neural stem/progenitor (nestin-Cre, "N") KO 2 v Ctrl 2 | gene TPM = sum of the transcripts of the gene (Ensembl GRCm38 r92 cdna headers, version stripped, unmapped transcripts counted and reported) | **global null KO v WT** (closest to the organoid knockout); S and N arms reported as secondary, never pooled |
| D3 GSE158682 | transcript TPM, cortex | mouse, in vivo cortex, P17, same paper and colony as D2, different tissue and animals | S KO 3 v Ctrl 4 | as D2 | S KO v Ctrl (the only arm) |
| D4 GSE126075 | gene TPM from CAGE | human neural stem cells and in vitro neurons, WWOX depletion (PMID 31543760), series summary: CAGE | hNSC 1 v WWOX-del 1; neurons 1 v WWOX-del 1 (merged tables, no replicates) | merged CAGE TPM by gene symbol | hNSC and neurons each, direction only; n of 1 per arm cannot support or fail by a rule that needs ordering across libraries, so D4 is **descriptive**: reported, never counted toward the rejecting observation |
| D5 GSE158684 | snRNA-seq filtered matrices, one control and one knockout library | mouse hippocampal nuclei, same paper | 1 v 1 library; no cell-class labels held | UMI counts of Pdk1 to Pdk4 summed over all nuclei per library, as a coverage check only | **coverage only**: reports detection (nuclei with a nonzero count, total UMI); a pseudobulk of two libraries is not a direction test |
| GSE215425 (P47T knock-in) | not held in `files/geo/` (checked 2026-11-25) | | | | cannot test; recorded, not acquired |

D2 and D3 share a paper and a colony: they are two tissues of one study, not two independent studies. Both are independent of GSE156243. The support statement therefore says "two tissues of one independent study" and never "three datasets".

## 4. Rules (frozen)

* **Detection (coverage, not direction):** a gene is *detected* in a comparison if the mean TPM of at least one arm is 1 or more. If an isoform is not detected, the verdict for that isoform is "cannot test (not detected)", never a direction and never a null. Detection is reported per isoform and arm, with the arm mean TPM.
* **Effect measure and unit:** ratio of the mean TPM of the deficient arm over the mean TPM of its control arm (gene TPM summed over transcripts), plus the per-library values, species and n per arm beside each ratio. No pseudocount, no normalisation beyond the deposit's own TPM; where a ratio would divide by zero it is reported as undefined with the numerator.
* **"Higher" rule (PDK3):** ratio 1.2 or more AND every deficient-arm library above every control-arm library. **"Lower" rule (PDK1):** ratio 1/1.2 or less AND every deficient-arm library below every control-arm library. The 1.2 is the deposit's own fold threshold in the anchor's DE list. With 2 v 3 libraries the ordering rule is the only one that does not need a distribution assumption; no P value is claimed as support.
* **Verdict per primary comparison and isoform:** SUPPORTS (rule met), FAILS TO SUPPORT (detected in the comparison, rule not met; the ratio and the ordering are stated), or CANNOT TEST (not detected, or fewer than 2 libraries in an arm).
* **Rejecting observation met** if PDK3 is detected in D2 (global KO) and D3 and FAILS TO SUPPORT in both; **partly met** if it fails in one and cannot be tested or is supported in the other (reported as such, no majority vote); **not met** if PDK3 SUPPORTS in at least one.
* PDK1 to PDK4 are all reported per comparison; PDK2 and PDK4 carry no prediction.
* **Sentence check:** one blind reader (legend-delegate, sonnet, effort high, stated and read back from the census) receives the final sentence(s) verbatim, built by script from this analysis's outputs, with the held-table paths and the mapping file path, and never this PREREG, the verdicts or the anchor's first reading. It answers MUST CHANGE / ADD / STANDS and recomputes the values from the held tables by its own script.
* **Consumers (named):** cards E03 and I01 (IT) and the dichloroacetate isozyme sheet (HE; use only what the sheet and its sources say: PDK1 1.03 mM, PDK2 0.50 mM, PDK3 5.56 mM in one assay is what the sheet records; no pharmacology from memory is added here).
* **Out of scope:** the frozen RP-045 prediction, the sealed ADV-174 and ADV-175 material, the Obeid 2026 article (classifier stop stands), any acquisition.
