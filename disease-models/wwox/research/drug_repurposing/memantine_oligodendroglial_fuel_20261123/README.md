# Memantine, oligodendroglial NMDA currents and metabolic support of axons

context_policy: QUESTION_DRIVEN. SCI_CODEX, 2026-11-23. Targeted interrogation of reported current fits, optic nerve study arms, and Figure 4A,D. No complete reading credit claimed. Only derived summaries and original code are distributed.

## Decision

Keep a conditional white-matter mechanism open in both directions. Prolonged exposure to 1 µM memantine blocked NMDA current in mature rodent oligodendrocytes. Separate mouse data show that loss of oligodendroglial NMDA signaling costs axons some ability to recover using glucose. Lactate largely closed that deficit. The missing link is whether sustained drug exposure at measured free concentrations changes the same process in WWOX-deficient tissue.

## What direct drug testing establishes

In P12 rat callosal slices, recorded at 23 °C in magnesium-free bath to maximize NMDA current, after one minute of pre-exposure, two reported concentration-response fits predict 1.82% and 9.33% block at 1 µM. After two hours at 1 µM, the investigators measured 70 ± 7% and 56 ± 10% suppression of the NMDA-evoked current with Cs and K internal solutions, respectively. At 0.36 µM, an adult CSF reference used elsewhere in this cycle, the brief-exposure fits predict 0.66% and 3.78%. A sustained concentration–response curve at or below 0.36 µM remains unknown. CSF and free concentration at an oligodendrocyte membrane are different quantities. [Bakiri et al., Fig. 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC2863073/)

In a separate P28 rat optic nerve assay at 33 °C and 1 mM magnesium, the low-concentration condition combined pre-exposure to 1 µM memantine with 25 µM NBQX during 20 minutes of ischemia. The prolonged 1 µM monotherapy comparator is missing. Acute 300 µM memantine alone failed to improve conduction recovery. Starting the tested blocker combinations during reperfusion also failed to show significant protection. These controls limit any inference of direct white-matter protection by memantine alone. [Bakiri et al., Figs. 4–5](https://pmc.ncbi.nlm.nih.gov/articles/PMC2863073/)

## New analysis of the competing fuel mechanism

Saab et al. compared optic nerves from mice with or without a conditional oligodendroglial deletion of Grin1 after an hour without oxygen or glucose. The readout was the area of the compound action potential, normalized to baseline. Their glucose-recovery comparison included 12 mutant and 11 control nerves (reported p=0.0046). Lactate recovery included six mutant and eight control nerves. The article reports a time-course comparison between fuels within mutants. We estimated the additional contrast between genotypes across fuels. The two fuels were 10 mM glucose and 20 mM lactate, matched in carbon equivalents only. [Saab et al., Fig. 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC9084537/)

| Recording minutes | Glucose, control | Glucose, mutant | Lactate, control | Lactate, mutant | Change in mutant-minus-control gap with lactate, points of baseline |
|---|---:|---:|---:|---:|---:|
| 40–50, before injury | 1.008 | 0.997 | 0.999 | 0.999 | +1.10 |
| 130–140 | 0.318 | 0.176 | 0.337 | 0.312 | +11.71 |
| 200–210 | 0.347 | 0.187 | 0.350 | 0.349 | +15.96 |
| 220–230 | 0.340 | 0.165 | 0.343 | 0.351 | +18.26 |
| 230–240, primary late window | 0.339 | 0.174 | 0.343 | 0.357 | +17.88 |

At 230–240 minutes the mutant-minus-control gap was −16.5 points on glucose and +1.4 points on lactate. Subtracting the pre-injury contrast gives a descriptive +16.8 points. The group-average time series establish an effect-size estimate conditional on the published preparations. No individual trajectory, genotype-by-fuel confidence interval, paired-nerve assignment, or equivalence margin can be recovered here. The disease model and the drug were both absent from this experiment. [Saab et al., Fig. 4A,D and caption](https://pmc.ncbi.nlm.nih.gov/articles/PMC9084537/)

Panels and windows were selected after visual inspection and before numerical extraction. The script calibrates each panel against its own ticks and recovers the centers of the vector error bars at half-minute intervals. Each window uses 21 plotted times per curve. Repeated time points carry no additional biological replication. Source SHA-256 is checked at run time. To reproduce, run `python3 analyze.py <source-PDF>` with PyMuPDF (tested 1.28.2) and compare to results.tsv. [Institutional source PDF, page 125](https://systemsneuroscience.uni-goettingen.de/dl/Oligodendroglial%20NMDA%20Receptors%20Regulate%20Glucose.pdf)

## Which observation could reverse the interpretation?

In Wwox-null mice, neuronal WWOX restoration improved both blood glucose and myelination. This provides a reason to consider energy supply and demand jointly. It leaves local extracellular glucose and the direction of oligodendroglial flux unresolved. In the comparator study, NMDA stimulation increased surface GLUT1 and release of labeled lactate from glucose. Acute exposure to other NMDA antagonists starting 30 minutes before oxygen-glucose deprivation did not visibly reproduce the genetic defect. Developmental NR1 deletion, chronic partial drug block, and acute excitotoxic injury can therefore give different outcomes. [Repudi et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC8649866/) · [Saab et al., Figs. 1, 4 and S6](https://pmc.ncbi.nlm.nih.gov/articles/PMC9084537/)

The discriminating comparison measures axonal conduction or ATP, oligodendroglial surface GLUT1, and labeled glucose-to-lactate transfer in a WWOX-deficient myelinated preparation and an isogenic control. Compare vehicle and memantine alone at measured free exposure, match axonal firing and baseline myelination, separate insult from recovery, and vary the recovery substrate. Unchanged glial uptake with improved axonal survival across fuels favors an injury-protection mechanism. A sustained loss of uptake and conduction on glucose with recovery on lactate favors a fuel-delivery cost. A shared response in the corrected and deficient preparations weakens WWOX specificity. A lactate-only benefit without glial measurements cannot identify the cellular source or exclude direct axonal use.

An independent direct drug experiment makes the choice of cell type consequential. In healthy cortical neurons, 10 µM memantine increased glucose consumption during glucose refeeding. In adult female mice systemic exposure increased prefrontal 2-deoxyglucose uptake. The untreated tissue measurements spanned 0.05–3.7 pmol/µg protein across five experiments, and the investigators normalized within experiment. A whole-tissue increase could thus coexist with lower transport in a specific glial compartment. These results at another exposure do not establish the sign in WWOX. [Fidilio et al., Figs. 1–2](https://pmc.ncbi.nlm.nih.gov/articles/PMC13739058/)
