# D-mannose · developmental N-glycome and precursor turnover

26 November 2026 · SCI_CODEX · context_policy: QUESTION_DRIVEN · human iPSC-derived culture and human fibroblast/serum glycan signals, with mouse fibroblast lipid-linked precursor amounts

This checkpoint asks whether more mannose-derived carbon, altered precursor turnover, and a shift in neural-lineage composition could each explain a WWOX glycan readout. The held WWOX comparisons identify GMPPB and COG pathway leads and a non-neural lectin/localization phenotype. The comparisons below test assay interpretation. [WWOX evidence](README.md) · [Tracer carbon-origin check](tracer_source_check_20261126.md)

## Human developmental and Golgi comparators

In the Kiwimagi preprint, day-14 induced glutamatergic and GABAergic cultures have **62.5% and 58.5%** high-mannose signal versus **73.5%** in undifferentiated human iPSCs. Man-5 itself moves in the opposite direction, **4.2% → 24.5% and 14.1%**, with Man-5:Man-9 ratios of **0.20, 3.50 and 1.37**. Sialylated signal also declines on differentiation, from **12.8% to 6.5% and 7.3%**. The indices are within-sample relative MALDI signals. For an illustrative linear mixture of only the two day-14 profiles, a change in relative signal weights can shift Man-5 by up to **10.4 percentage points** and sialylation by up to **0.8 percentage points**. The weights represent each population's contribution to glycan signal. They cannot be inferred from cell fractions alone. This bound applies to these two profiles only and cannot exclude other stages or cell types. [Kiwimagi et al., preprint, Table 1 and Fig. 4 caption](https://pmc.ncbi.nlm.nih.gov/articles/PMC11507760/)

Separately, fibroblast lysates from one person with confirmed COG6-CDG and control material gave **44% → 55%** oligomannose and **29% → 14%** total sialylation. Their oligomannose-to-sialylation signal ratio rose **1.52 → 3.93**, a **2.59-fold** change between samples. In serum, relative ESI signal of the main disialylated glycan fell from **55.2% to 30.1%**. This is an independent sample type and assay within the same case. It supports the direction of a late-processing control in that disease. The fibroblast and serum signals measure glycan composition and neither measures N-site occupancy. Their absolute magnitudes do not set a neural cutoff. The public deposit covers the serum RapiFluor-MS arm, rather than the fibroblast MALDI spectra used for the ratio. [Pakanová et al., §3.6](https://onlinelibrary.wiley.com/doi/10.1155/humu/7948771) · [GlycoPOST GPST000459](https://glycopost.glycosmos.org/entry/GPST000459)

The held human WWOX organoid work reports a shift in neuronal representation in the engineered knockout. WWOX comparisons should therefore pair the same lineage and stage and track cargo abundance. A rise in Man-5 in bulk can reflect the mix of cells and can occur during normal neuronal differentiation. Absolute N-site occupancy and the distribution of high-mannose and complex forms **on the same occupied site** can test a more specific WWOX maturation defect. [Steinberg et al., Fig. 2F in the held dossier](../../../fulltext_dossiers/PMID42397075_partial_locators.md)

## Early precursor turnover control

Higashidani et al. detected no rise in steady-state mannose-6-phosphate (M6P) with 500 µM extracellular mannose in the reported control and PMM2- or MPI-deficient human fibroblasts. In an extreme `Mpi`-null mouse embryonic fibroblast model, the same nominal exposure raised M6P. Comparing matched 100 and 500 µM data in their Table 1, mature lipid-linked oligosaccharide (LLO) pools retained **31.2%, 36.7% and 36.5%** in experiments 1, 3 and 4. The study's separate glycosylation experiment reported **75–77%** occupied DNase I marker at the tested exposures, and no detectable decrease by the ConA capture assay for secreted protein. Thus mature LLO pool loss and loss of protein occupancy are separable. [Higashidani et al., Table 1 and Fig. 3A–B captions](https://pmc.ncbi.nlm.nih.gov/articles/PMC2676341/)

A different fibroblast study gives a way to separate slow LLO assembly from increased loss. In PERK-null mouse embryonic fibroblasts, the authors report that experimental M6P elevation with 10 mM added mannose reduced mature LLO to **82 ± 2%** of untreated levels (**two measurements**) and increased free lumenal glycans. They also found in conventional ER stress that lower translation can lower precursor consumption by nascent cargo and mask ongoing cleavage in the steady pool. The experimental concentration and engineered background supply a mechanistic control. WWOX neural exposure, a dose threshold, and the causal link to WWOX have not been measured. [Gao et al., Figs. 5 and 7 captions and Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC3164449/)

## Predicted outcomes in a paired WWOX assay

Retain isotope-resolved M6P, mannose-1-phosphate, GDP-mannose, mature LLO, early occupancy and processing of the same cargo in stage- and lineage-matched WWOX-deficient and corrected neural material. Record total nascent cargo and its surface abundance, ATP and viability. Treat M6P as a metabolite measurement distinct from M6P residues on proteins.

| Interpretation | Observation that would distinguish it |
|---|---|
| Carbon-source substitution | Fraction of mannose-derived residue label rises while absolute occupancy and mature output stay at baseline. |
| Substrate-limited rescue | Initially low total GDP-mannose increases. Absolute occupancy and maturity recover within the matched WWOX lineage at measured exposure. |
| Downstream Golgi limitation | Donor pool and occupancy are adequate or recover. Abnormal glycoforms persist on the same occupied sites with persistent Golgi coatomer displacement. |
| Early precursor turnover | M6P rises and mature LLO drops or turns over more rapidly while corresponding labelled free glycans increase. Test whether the free glycans are consistent with lumenal cleavage versus turnover of already glycosylated cargo. A parallel occupancy or ATP loss would determine functional cost. |

A donor increase or a higher labelled fraction alone does not advance the candidate. If the matched cells show an early occupancy benefit and a persistent maturation defect, maintain the distinction and test whether either affects a neural functional readout. Known WWOX evidence remains at RNA and non-neural glycan/localization level for this question. A pediatric WWOX trial remains a low priority.

**Next checkpoint.** Identify a tractable site-resolved reference measurement in an age- or stage-matched human neural model and check whether the required specimens and measured-exposure readouts are accessible before further ranking. A review can change the decision once there is a candidate site and assay to challenge.

Run `python3 -B processing_check.py | cmp - processing_results.tsv` from this directory. The calculation uses transcribed reported percentages and pool amounts, without raw-spectrum reprocessing or inferential pooling. [Source values](processing_inputs.tsv) · [Recalculated contrasts](processing_results.tsv)
