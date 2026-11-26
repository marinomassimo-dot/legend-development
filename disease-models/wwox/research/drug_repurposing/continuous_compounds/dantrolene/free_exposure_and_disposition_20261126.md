# Dantrolene sodium · free-exposure comparison and disposition

26 November 2026 · SCI_CODEX · context_policy: QUESTION_DRIVEN

**Disposition.** Parked for an unselected pediatric WWOX trial. Retained as a compartment-specific calcium probe. The result that could change this decision is selective rescue of abnormal late ER calcium release in WWOX-deficient intact neurons at a measured free exposure, with preserved physiological mitochondrial calcium, ATP recovery and inhibitory recruitment at matched evoked drive. Require a separate quantitative bridge to attainable central free exposure before reconsidering any pediatric trial priority. [WWOX RNA and discriminating comparison](README.md)

## Rat brain, CSF and blood

| Comparison | Value | Basis |
|---|---:|---|
| Rat unbound brain-to-plasma ratio, Kodaira reference | 0.0297 | Brain-slice-based estimate, as reported in Cui Table 4 and Ball Table S10 |
| Rat unbound brain-to-plasma ratio, Cui study | 0.061 | Brain-homogenate-based estimate, Table 4 |
| Rat total brain-to-muscle ratio, Cui study | 0.19 | Separate compartment pair, Table 4 |
| Rat free CSF-to-free plasma ratio, Kodaira reference | 0.0838 | Ball Table S10 reported comparator |
| Rat model, brain-to-plasma and CSF-to-plasma ratios | 0.144 and 0.037 | Ball Table S10 model results |

The two reported brain-based estimates differ about **2.05-fold**. In the Kodaira reference values transcribed by Ball, the CSF ratio is **2.82 times** the brain ratio. Ball's predicted brain ratio overshoots the reference **4.85-fold**, while its predicted CSF ratio is **2.26-fold below** the reference. Both brain estimates incorporate an in vitro tissue-binding determination. These comparisons show the sensitivity to the matrix and method even within rat studies. The primary Kodaira abstract was checked. Exact dantrolene values attributed to Kodaira come through the two open-access papers and count once. A separate rat study reported a 3.3-fold increase in total brain-to-plasma ratio with Bcrp loss. It supports a transporter effect in rats and supplies no human unbound brain ratio. [Cui et al., §2.4 and Table 4](https://doi.org/10.3390/pharmaceutics11110595) · [Ball et al., §3.3 and supplementary Table S10](https://pmc.ncbi.nlm.nih.gov/articles/PMC3978528/) · [Kodaira et al., primary abstract](https://pubmed.ncbi.nlm.nih.gov/21934030/) · [Fuchs et al., primary abstract](https://pubmed.ncbi.nlm.nih.gov/25053619/)

## Reproducible unit and partition check

EMA's in vitro formulation study found **94.9% binding** in pooled human plasma at the 6 µg/mL test concentration. The separate historical oral volunteer result was **1.24 ± 0.32 µg/mL** total plasma peak. FDA Table 2 reports **9.0 ± 4.6 µg/mL** after a single acute intravenous exposure in healthy volunteers. The pediatric acute IV primary abstract gave **whole-blood** concentrations in ten children aged 2–7 years, so no plasma-free conversion was made. These examples describe different study populations and matrices. [EMA assessment, CLS4_0069_0001](https://www.ema.europa.eu/en/documents/assessment-report/agilus-epar-public-assessment-report_en.pdf) · [Oral study, primary abstract](https://pubmed.ncbi.nlm.nih.gov/499321/) · [FDA RYANODEX label, §12.3 Table 2](https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/205579s011lbl.pdf) · [Pediatric IV, primary abstract](https://pubmed.ncbi.nlm.nih.gov/2929999/)

For replay, multiply the total parent mass concentration in µg/mL by `1000 × assumed_fu_plasma / 314.25` to express the conditional free plasma value in µM, using the parent mass and assuming the reports express parent analyte mass. A salt-mass basis would lower the converted number. Hold `fu_plasma = 0.051` fixed across the two examples as a sensitivity calculation. Multiplying by an assumed `Kp,uu` gives the simple cross-matrix check below. Neither the binding fraction at each human peak nor a human `Kp,uu` was measured in these records. An acute peak need not coincide with peak brain exposure and a rat ratio cannot be used as a clinical prediction. [Exact inputs and products](free_exposure_scenarios.tsv) · [Parent molecular mass](https://pubchem.ncbi.nlm.nih.gov/compound/6914273)

| Example | Conditional free plasma, µM | Rat slice ratio product, µM | Rat homogenate ratio product, µM | Unity partition product, µM |
|---|---:|---:|---:|---:|
| Adult single oral | 0.201 | 0.0060 | 0.0123 | 0.201 |
| Adult acute IV | 1.461 | 0.0434 | 0.0891 | 1.461 |

The two historical neural examples used **10 µM nominal**. The nominal bath concentration is a point of comparison and gives no intact-neural potency threshold. It differs from measured extracellular free drug and from intracellular unbound drug at a release channel. There is no concentration–response and parent-plus-metabolite exposure linkage here to justify a smaller effective value, rule out one, or convert the gap into a dose. The oral Wolfram experience supplies a small pediatric tolerability comparator in a distinct disorder. Fatigue, weakness and potential liver toxicity matter for interpreting a neurodevelopmental endpoint. [WFS1 cells and oral Wolfram cohort](wfs1_translation_20261126.md) · [Native neuronal comparator and mouse AUC audit](native_calcium_and_exposure_20261126.md) · [DailyMed oral label](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=57b4eec1-49e1-432c-95ae-0fe36e32d64b)

**Open check.** Independent reproduction of the Wang workbook column mismatch was requested through laboratory coordination. At this checkpoint no reply was available. A correction could change the route-specific mouse interpretation. Trial prioritization still depends on genotype-selective response, measured free exposure and preserved physiological function.
