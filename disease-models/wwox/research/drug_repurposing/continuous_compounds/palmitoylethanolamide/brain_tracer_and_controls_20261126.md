# Palmitoylethanolamide · brain tracer and formulation controls

26 November 2026 · SCI_CODEX · parent-isotopologue signal in rat whole brain (pmol/g), plasma (pmol/mL), and comparison to nominal media or reporter concentrations (µmol/L)

**Decision at this checkpoint.** There is chemical evidence for the expected PEA isotopologue in rat whole-brain extract after oral ultramicronized PEA. This supports measuring a brain exposure bridge. The evidence does not identify an advantage of this formulation in brain over the nonmicronized formulation, rule out hydrolysis with reacylation, or establish glial receptor occupancy. Keep the WWOX candidate active for a lower-exposure glial comparison. [Primary rat tracer study](https://doi.org/10.3389/fphar.2018.00249)

## Matched plasma and tissue questions

Petrosino et al. treated male rats weighing 200–230 g. The tracer arm used 30 mg/kg in the reported rat study. Figure 1 compares nonmicronized and ultramicronized isotope-labeled PEA in plasma. At 5 min in healthy animals the reported means are **1.1 and 5.4 pmol/mL**, a **4.9-fold** difference from the rounded means. At 30 min the ultramicronized means are **1.2 and 22.8 pmol/mL** for healthy and carrageenan cohorts, a 19-fold difference. Brain Figure 4 depicts the healthy and carrageenan arms only within the ultramicronized formulation. It does not reproduce the plasma formulation contrast in brain. There are five rats per time point and arm. Tissue sampling is terminal, so the plotted series are cohort trajectories. Reasons for inflammation-dependent kinetics and disparate compartments are unresolved. [Methods, Results and Figs. 1 and 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC5870042/)

| Time after tracer | Healthy brain, approximate pmol/g | Carrageenan brain, approximate pmol/g |
| --- | ---: | ---: |
| 5 min | 5.9 | 4.6 |
| 15 min | 15.5 | 16.2 |
| 30 min | 5.9 | 10.5 |
| 60 min | 4.9 | 14.3 |
| 180 min | — | 4.5 |
| 360 min | — | 3.9 |

The values are visual estimates from **Fig. 4**, with about ±0.3 pmol/g placement tolerance. Healthy animals were sampled only through 60 min. An omitted later healthy bar is unobserved and gives no denominator for a late-fold contrast. The larger 15-minute bars are the largest plotted means. The primary report's within-arm tests versus baseline did not mark either 15-minute bar. At 30 min, dividing the rounded brain values by the reported plasma means gives **4.9 and 0.46 mL/g**. This is a ratio of plotted group means with different units during an evolving single-exposure time course. No paired covariance, steady-state partition or unbound ratio can be recovered. It illustrates why the larger inflammatory plasma rise cannot predict a comparable whole-brain rise. [Fig. 4 source raster](https://pmc-oa-opendata.s3.amazonaws.com/PMC5870042.1/fphar-09-00249-g0004.jpg)

The LC-APCI-MS method measures a molecular-ion mass and expected chromatographic retention time for the labeled amide. This distinguishes the parent isotopologue from a measure of pooled isotope or an analytical palmitate peak. The four labeled carbons are all on the palmitoyl chain. Cleavage followed by reformation with the labeled acyl chain remains possible. The cited collection description does not report separating capillary from parenchymal signal. Free interstitial and per-cell concentrations remain unknown. The separate paw and spinal pharmacology used 10 mg/kg and an experimental inflammatory stimulus, so a neural target-engagement fit cannot be recovered by joining those outcome data to the exposure cohort. [Original synthesis-label, collection and measurement sections](https://doi.org/10.3389/fphar.2018.00249)

## Response range for the next comparison

With the illustrative density assumption of 1 g/mL, **15.5–16.2 pmol/g** would correspond to about **15.5–16.2 nM** averaged across the processed whole tissue. This is about 190–200 times below the **3.1 µmol/L** EC50 in the reported PPAR-alpha transactivation assay. It is an exposure-scale check only. It does not include endogenous PEA, selective partition or receptor signaling amplification. A separate organotypic lesioned hippocampal-slice abstract reports a tested **0.001–1 µmol/L** range and pharmacological PPAR-alpha dependence. A primary astrocyte–neuron coculture study reports **0.1 µmol/L** exposure during an induced amyloid challenge. The reported range requires verification of exactly which endpoint changed at which exposure, duration, cellular compartment and nominal concentration. Generic injury protection is distinct from rescue of a baseline WWOX defect. [Reporter primary abstract](https://pubmed.ncbi.nlm.nih.gov/15465922/) · [Slice primary abstract](https://pubmed.ncbi.nlm.nih.gov/20221904/) · [Coculture primary abstract](https://pubmed.ncbi.nlm.nih.gov/29154284/)

**Next comparison.** Audit the low-concentration slice results and any dose-resolved response in isolated glia. Keep PPAR-alpha competence separate from PEA handling and acute insults. Require an intact-parent dose/response series with measured free or compartmental parent, native lipid flux and a functional WWOX readout. If isotope conservation is critical, label both structural moieties and also monitor single-labeled parent and the associated free breakdown products. Glial cytokine changes at higher nominal media exposure alone do not meet the evidence threshold for pediatric trial priority. [WWOX input data and hypothesis](README.md)

### Repeat the visual reconstruction

The publisher raster in the source figure link is 714 × 394 pixels, SHA-256 `bae0fe4f017c6c38c050b4e1b45f4db6ae6affa7274ea6b6e970f2da60108414`. Convert each measured bar with `24*(311-y)/300`. Divide the estimated brain value by the reported plasma mean only for matched time and arm, skipping entries marked NA. [Digitization inputs](brain_trace_digitization.tsv)
