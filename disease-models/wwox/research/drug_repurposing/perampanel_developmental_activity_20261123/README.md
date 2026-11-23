# Perampanel hypothesis revisited at an early stage of oligodendrocyte development

context_policy: QUESTION_DRIVEN. SCI_CODEX, 2026-11-23. Targeted analysis of the primary study's Fig. 5C, Fig. S5C and matching methods, caption and accession. Both figures were inspected before choosing the contrasts. The source license is CC BY-NC-ND 4.0. Only our code and original numerical summaries are redistributed. [Primary study](https://doi.org/10.1002/glia.70157)

## Decision

An early increase in the fraction of cells expressing a myelin marker can result from reducing neuronal activity in healthy cortex. This provides a concrete alternative explanation for a putative beneficial effect in hyperexcitable WWOX-deficient tissue. It also puts a limit on the interpretation. The early marker study did not determine the lasting number of surviving, myelinating cells or the amount of functional myelin.

## Two ways of reducing activity

The paper compared early mouse cortical slices from P4 pups at eight days in culture. Study arms reduced firing with tetrodotoxin (TTX) or reduced excitatory neuronal activity chemogenetically (Gi). After 48 hours, a separate arm in each comparison had also received AMPA. Counts were expressed as the fraction of Olig2-positive cells co-labeled with a marker. We quantified the means from the source figures, preserving each experimental block and its own control. Shifts below are percentage points of Olig2-positive cells.

| Treatment contrast | PDGFRα, progenitor | BCAS1, premyelinating | PLP, maturing |
|---|---:|---:|---:|
| TTX minus matched control | −31.8 | +7.6 | +16.4 |
| TTX plus AMPA minus TTX | −8.2 | +25.1 | −16.2 |
| Gi minus matched control | −2.1 | −9.0 | +23.6 |
| Gi plus AMPA minus Gi | −21.5 | +48.0 | −15.8 |
| NBQX minus its own matched control | −11.6 | +0.7 | +24.3 |

Reducing activity increased the PLP-positive fraction in both comparisons. Adding AMPA reduced it by about 16 points with either method, while raising the BCAS1-positive fraction by 25–48 points. This is compatible with a change near the transition between premyelinating and maturing cells. PLP after add-back was 5.4% versus 5.2% in the TTX block control, and 21.9% versus 14.1% in the Gi block control. The outcome of add-back depends on marker and block. The Gi and NBQX controls have near-identical summary values across all three markers. Independence between those control groups is unverified. We report each within its own comparison. No test treats the two controls or the measurements of different markers as independent replicates. [Fig. 5C](https://pmc.ncbi.nlm.nih.gov/articles/PMC13288302/) · [Fig. S5C, original supplement](https://pmc-oa-opendata.s3.amazonaws.com/PMC13288302.1/GLIA-74-0-s001.docx)

Fig. 5C reports 8–12 mice, Fig. S5C eight. The study's statistical annotations address comparisons to the specified controls. Our add-back magnitudes are descriptive. No raw paired animal or lineage trajectories were available in the material used. Marker proportions can change through survival, expression or denominator shifts. The GEO experiment pooled three Gi pups and two controls in one library per condition. A new transcriptomic significance test treating the cells as biological replicates would not resolve those alternatives. [GEO GSE329995](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE329995)

## What changes for the WWOX test?

Neither perampanel nor WWOX deficiency was included here. NBQX blocks AMPA and kainate receptors. Bath-applied AMPA can act on more than one cell type, and its effects on the network may also differ between TTX and Gi. The earlier rabbit hemorrhage experiment directly tested perampanel and found more myelin marker at a later time, while genetic loss of glial AMPA receptor subunits during development reduced surviving new oligodendrocytes. An early shift in PLP staining could therefore occur even when long-term sheath formation fails to improve. [Prior perampanel analysis and primary sources](../perampanel_20261122/README.md)

A result that would change the decision is a gain in **surviving new oligodendrocytes and functional sheaths** in the WWOX-deficient preparation after perampanel, beyond an independent intervention matched for neuronal firing. Count absolute lineage abundance and follow the early PDGFRα/BCAS1/PLP stages to stable sheath number and conduction. Repeat in an isogenic corrected preparation. If both activity-matched interventions shift early PLP similarly and the gain disappears at the functional endpoint, the early response supports activity dependence and is insufficient to prioritize perampanel for myelin rescue.

## Reproduce

Run `python3 analyze.py source.pdf supplement.docx` with PyMuPDF and NumPy, then compare to results.tsv. Input checks match the PDF and the original embedded supplement image by SHA-256. The script detects the colored bar boundaries against each calibrated vertical axis. Changes to color cutoff, within-bar read width and column position shifted an estimated mean by at most 0.35 percentage points in the tested settings. Biological and marker interpretation uncertainty are larger. [Source PDF](https://pmc-oa-opendata.s3.amazonaws.com/PMC13288302.1/PMC13288302.1.pdf) · [Supplement](https://pmc-oa-opendata.s3.amazonaws.com/PMC13288302.1/GLIA-74-0-s001.docx)
