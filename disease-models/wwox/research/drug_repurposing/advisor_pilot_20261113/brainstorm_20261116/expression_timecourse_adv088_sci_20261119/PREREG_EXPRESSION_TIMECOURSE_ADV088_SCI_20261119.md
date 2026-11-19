# Pre-registration (frozen before any value is downloaded or counted): when do the PV, chloride, late-maturing and myelin markers switch on? (ADV-088, SCI, 2026-11-19; hypothesis level; no dose; reference genotype class only; not medical advice; this file is not edited once hashed: any change goes into a dated addendum file)

## 0. Question and decision
Set the assay ages of ordering-page rows 4 and 6 (P14, P17, P21) against a measured onset of marker expression in unaffected tissue, instead of the unchecked sentence "PV protein appears around the second postnatal week" (SCI's row-6 refinement, 2026-11-19), and say whether the PV, chloride and myelin stage confound of ADV-068 and ADV-070 can be placed in time.

## 1. What was checked before this file (no count was made)
Held files: `files/geo/` holds GSE52564 (one age), GSE73721, GSE126075, GSE150123, GSE156243, GSE158681 to GSE158684, GSE92742, HPA single nuclei: none is a developmental time course of whole neocortex. The corpus analysis note `analysis/wwox_postnatal_svz_expression_20260922.md` records BrainSpan as unreachable on that day and joins WWOX to BrainSpan only through the prenatal 8 to 37 week paper. A GEO listing search (titles only) found no wild-type whole-cortex series with P7, P14 and P21 together and replicates; the nearest series are cell-class specific (GSE233255, oligodendrocyte lineage by layer at P7, P14, P30, P90; GSE331310, excitatory translatome P7, P14, P21; GSE333340, SST cells P10, P15, P30) or adult-spaced (GSE292102 and GSE292221 at weeks 1, 7, 14).

## 2. Deposits (named now; a change is a dated addendum, hashed before its counts)
* **D1, mouse:** Cardoso-Moreira et al. 2019 organ time series, ArrayExpress E-MTAB-6798, file `Mouse.RPKM.txt` with the sample sheet `E-MTAB-6798.sdrf.txt`. Tissue rows labelled Brain (whole brain or forebrain as labelled), ages 0 days, 3 days, 2 weeks, 4 weeks and 9 weeks postnatal (P0, P3, P14, P28, P63). Replicates and sexes as the sample sheet gives them. **No P7, P17 or P21 exist in D1**: ages between P14 and P28 are interpolated only, and the note says so.
* **D2, human:** BrainSpan developmental transcriptome, RNA-seq gene-level RPKM (the file the download page names "RNA-Seq Gencode v10 summarized to genes"), neocortical regions only, all donors from 8 post-conception weeks to adulthood.
* **Not used for the onset question:** GSE233255 (myelin set within oligodendrocyte-lineage cells only; may be added as a dated addendum for the myelin set).

## 3. Markers (fixed here)
* Target: **Wwox**.
* GABAergic and PV: **Pvalb, Gad1, Gad2, Sst, Vip, Lhx6, Nkx2-1**.
* Chloride: **Slc12a5** (KCC2) and **Slc12a2** (NKCC1); the ratio Slc12a5 / Slc12a2.
* Late-maturing neuronal set: **Kcnc1, Syt2, Acan, Gabra1** and the ratio Gabra1 / Gabra2.
* Myelin set: **Mbp, Plp1, Mog, Mobp, Mag, Cnp**.
* Human symbols are the upper-case forms (PVALB and so on). A gene absent from a deposit is reported absent, not dropped.

## 4. Unit and definitions
* Unit: log2(RPKM + 1) per sample as the deposit gives it; no re-normalisation. Per age: the mean of the samples at that age (per-sample values and n are listed beside it).
* **Plateau** of a gene (mouse): the mean over P28 and P63. **Fraction of plateau at age a** = (mean RPKM at a) / (plateau mean RPKM), computed on the linear RPKM scale; the log2 values are shown for reading only.
* Human: the plateau is the mean over donors aged 10 years and older in neocortex; postnatal ages are shown in years as the deposit gives them, per donor; no bins are invented beyond the deposit's own ages.
* **Onset age** of a gene: the first age at which the fraction of plateau is at least 0.5 (half-maximal); with D1 the answer is an interval between two sampled ages, never a single day.

## 5. Predictions written before the count (so that they can fail)
1. Pvalb is below 0.6 of plateau at P14 and at or above 0.8 at P28 (the rising phase spans P14 to P28).
2. Gad1 and Gad2 are at or above 0.7 of plateau by P14 (GABA synthesis precedes PV maturation).
3. The ratio Slc12a5 / Slc12a2 at P14 is at least twice its value at P3.
4. The myelin genes (Mbp, Plp1, Mog, Mobp, Mag) are below 0.5 of plateau at P14, so the myelin rise overlaps the PV rise.
5. No prediction is made for Wwox (the pattern is reported).

## 6. The rejecting observation (ADV's, fixed here) and the other readings
* **Reject:** **Pvalb at or above 0.8 of plateau at P14 in D1** (onset already complete before P14). Then the P14 slice is **not** a maturation-delay window for PV, and reading (b) of row 6 (delayed marker onset) loses its purpose at P14: the lineage-reporter design would keep its loss (a) and state or circuit (c, d) readings, and the earliest informative age would have to be earlier than P14 (D1 samples P3: check P3 and P0).
* **Partial:** Pvalb between 0.6 and 0.8 at P14: P14 sits at the end of the rise; P14 stays but P17 and P21 add little; say so.
* **Support:** Pvalb below 0.6 at P14 and at or above 0.8 at P28: P14, P17 and P21 all lie on the rising phase (P17 and P21 interpolated).
* **Confound placement:** if the half-maximal intervals of Pvalb, Slc12a5 / Slc12a2 and the myelin genes all fall between P14 and P28, the P17 bulk deposits of ADV-068 and ADV-070 sit on the rising phase of all three, and a stage difference could produce a PV, chloride or myelin difference at P17 with no knockout effect on the cells; if they fall in different intervals, say which is first. The deposit cannot separate them within an interval.

## 7. What the deposits cannot tell (stated before the count)
Transcript, not protein (PV protein accumulation lags the transcript by an unknown interval); bulk tissue, so cell composition and cell maturation are mixed (a rising bulk Pvalb is a number of cells and a level per cell together); whole brain or forebrain as labelled in D1, not neocortex layers; one outbred mouse strain in D1; sexes pooled as the sheet gives them; no P7, P17 or P21 in D1; human ages are donors, not a longitudinal series.

## 8. Cost and method
No delegate (the analysis is small). Plain clients only; a challenge is a stop; no contact data sent. Findings to IT and ADV; nothing applied.
