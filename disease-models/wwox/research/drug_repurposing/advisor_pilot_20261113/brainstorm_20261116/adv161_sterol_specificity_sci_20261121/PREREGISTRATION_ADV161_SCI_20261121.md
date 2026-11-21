# ADV-161 pre-registration: can the thyroid-dependent maturation programme move the sterol transcript set? (SCI successor Y, 2026-11-21; hypothesis level; adjacent evidence only; no dose; no contact; no e-mail address to any service; reference genotype class only; not medical advice)

Fixed BEFORE any gene row of Hochbaum Table S1 or S2 was read. What had been read when this was written: the Hochbaum et al. 2024 article text from Europe PMC fullTextXML (PMC11455614; Results on oligodendrocytes, snRNA-seq and differential-expression Methods); the GEO series record (GSE271421); the file listing of the PMC open-data bucket; and only the STRUCTURE of Table S1 (header, list of cell subtypes, rows per subtype, maximum adjusted p per subtype) and of Table S2 (header and the first two rows, both astrocyte). The first two data rows of Table S1 are L2/3 IT neuron genes and not part of any set below.

## Question
Is the sterol (cholesterol-synthesis) transcript signal specific enough to separate two candidate mechanisms in INV-06 and INV-12 (ISR-dependent glial maturation against a neuron-dependent or ISR-independent route), or does the neighbouring thyroid-dependent maturation programme (T3) move the same genes in OPC and oligodendrocyte states?

## Source and route record
* Hochbaum et al. 2024 (PMID 39178853, DOI 10.1016/j.cell.2024.07.041, PMC11455614, open access). Author-hosted PDF: TLS verification fails (host-name mismatch); no insecure flag used; route closed. PMC page route: proof-of-work challenge page (not solved). Europe PMC supplementaryFiles: 0-byte MMC2. Publisher page: Cloudflare challenge (403). Reached: Europe PMC fullTextXML (article), PMC open-data bucket (Supplementary Tables S1 = MMC1, S2 = MMC2, S4 = MMC4, MMC3 pdf), GEO series record (only `GSE271421_RAW.tar`, no processed table; not downloaded), Harvard Dataverse listing (behaviour, electrophysiology and MoSeq tables only; no snRNA table).
* Table S1 = per-cell-subtype differential expression, T3 against vehicle, endogenous cohort only (n = 4 animals per condition, adult males, T3 2.5 days, M2 frontal cortex). It lists genes with adjusted P below 0.05 only: a THRESHOLDED table, so a gene absent from a subtype is "not reported", never a zero. No table in the supplement holds the receptor-perturbation (DN-THR and WT-THR) differential expression; that cohort (2 to 3 mice per genotype, neurons only transduced) exists as figures and in the per-cell collection, which is not a compact table, so it is OUT OF SCOPE here and stays a separate cohort (no pooling).
* The test unit in Table S1 is the pseudocell (about 30 nuclei per sample, limma-trend, blocked by sample); the animal is the unit of the authors' `robScore_logFC` (fraction of sample pairs, T3 against vehicle, agreeing in direction). I will not recompute any animal-level p; I report the authors' adjusted P, `robScore_logFC` and `pctExpr` as printed, and treat `robScore_logFC` as the animal-level support (a TRG, in the authors' own definition, needs adjusted P < 0.05 and |robScore_logFC| >= 0.5).

## Gene sets (fixed now from canonical biology, not from any dataset)
* **A, core cholesterol biosynthesis (SREBP2 pathway), 19 genes:** Hmgcs1, Hmgcr, Mvk, Pmvk, Mvd, Idi1, Fdps, Fdft1, Sqle, Lss, Cyp51, Tm7sf2, Msmo1, Nsdhl, Hsd17b7, Dhcr24, Ebp, Sc5d, Dhcr7.
* **B, sterol regulators and SREBP2 targets, 7 genes:** Srebf2, Scap, Insig1, Ldlr, Pcsk9, Stard4, Acat2.
* **C, maturation baseline (mature-oligodendrocyte and myelin programme), 14 genes:** Mbp, Plp1, Mog, Mag, Mobp, Cnp, Opalin, Cldn11, Ugt8a, Gpr37, Enpp6, Tcf7l2, Bcas1, Fyn.
* **T, T3 responsiveness controls, 4 genes:** Hr, Klf9, Dio3, Ier5.
* Named states: OPC, Oligo.Enpp6_2 (immature oligodendrocytes), Oligo.Opalin_2 (mature). Oligo.Opalin_1 and Oligo.Opalin_4 are read for completeness (2 and 6 listed genes; too thin to decide). Astrocyte states are read only as a comparison context. Neuronal states give one descriptive line (cross-state distribution of set A).

## Readings and predictions (fixed)
* **N (non-specific):** T3 moves the sterol set in the glial states, so a sterol shift in a glial state cannot tell an ISR-dependent from a thyroid-like maturation shift.
* **S (specific):** T3 does not move the sterol set in the glial states while it moves set C or the controls T, so the sterol set separates a maturation programme from the sterol readout.
* P1: set T (at least Hr or Klf9) is listed in at least one named state (the state responded and the table covers it).
* P2: set C is listed in Oligo.Enpp6_2 or OPC (the maturation programme is moved by T3, as the authors state).
* P3 (my expectation, not a wish): sterol genes are not enriched among T3 targets in oligodendrocyte states, i.e. S holds at table coverage. I would not be surprised by N, because mature oligodendrocytes make cholesterol and T3 is a metabolic hormone in the liver.

## Decision rules (fixed; a gene counts only with adjusted P < 0.05 and |robScore_logFC| >= 0.5, in one named state)
1. **REMOVES the sterol score as a discriminator:** three or more genes of set A with the same sign in one named state, or two of A plus two of B with the same sign. The base rate is about 0.2 set-A genes expected by chance in the largest named state (157 listed genes), so three same-sign genes is not chance. Direction is reported with the verdict: up means T3 would mimic release of a maturation block; down would mimic a lock. Either removes the discriminator for mechanism separation.
2. **PARTIAL, keep only as an exploratory marker with a stated warning:** one or two genes of A in a named state, or any A or B gene with the opposite sign to the rest in the same state.
3. **KEEP as an exploratory discriminator of T3 against ISR in adult cortex:** zero genes of A and B in all three named states AND set T satisfied (P1). Stated with its limit: absence from a thresholded table at n = 4 animals and a pseudocell test is "not reported moved", not "unmoved".
4. **SCOPED STOP:** set T is not listed in any named state (coverage not shown comparable), or Table S1 cannot be read.
5. Descriptive only, no rule: set C coverage and direction against set A; the glial gene-ontology terms in Table S2 (a sterol or cholesterol term present or absent; absent is not zero).

## Limits stated now
Adult male frontal cortex, systemic T3 for 2.5 days, n = 4 per condition: ADJACENT evidence, not neonatal WWOX and not the VWM tissue of Lin 2025. Percent detection (`pctExpr`) is never read as expression. No ranking delta from abundance. No assay recommendation and no treatment claim. Even a clear overlap is a warning about marker specificity and a comparator-selection clue, not a transfer of effect.

## Rejecting observation (named in advance)
A per-animal slice (not compact; not downloaded) that shows the set-A genes moving under T3 in OPC or oligodendrocyte nuclei, against an empty Table S1 result, would reverse rule 3; the same slice showing no movement against a rule 1 result would reverse rule 1 (the table lists what passed a threshold on pseudocells, which can be driven by a few animals).

## Consumer
IT (INV-06 and INV-12 wording in `ranking_it8_p9_20261029/investigations.tsv`), through ADV. A result with no consumer is dropped.
