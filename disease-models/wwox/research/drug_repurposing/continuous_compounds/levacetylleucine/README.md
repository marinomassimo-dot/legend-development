# Levacetylleucine · route switching and native fuel transfer

26 November 2026 · SCI_CODEX · first comparison · context_policy: QUESTION_DRIVEN

**Active.** Levacetylleucine has pediatric neurological indication experience and tests a delivery hypothesis beyond free L-leucine. The altered transport route potentially changes competition for lactate and delivers acetate in addition to leucine. The prespecified WWOX comparison finds the strongest shared signal at the receiving-side transporter MCT2. That signal motivates measuring native fuel transfer and withholding any claim that levacetylleucine targets MCT2. [Prespecified test and comparators](pretest_20261126.md)

## WWOX transport and product RNA

Values are KO minus control in mean log₂(1 + RNA abundance). Mouse data use gene-summed TPM in P17 cortex (4 control/3 KO) and P17 hippocampus (2/3). Week-15 human organoids use normalized counts per million (2/4, with shared lines). All 36 comparisons include single-library omissions. [Bulk values and omission ranges](contrasts.tsv) · [Input fingerprints](../d_mannose/inputs.tsv)

| RNA | Mouse cortex | Mouse hippocampus | Human organoid |
|---|---:|---:|---:|
| SLC16A1 (MCT1) | +0.145 | −0.234 | +0.005 |
| SLC16A7 (MCT2) | −0.958 | −0.933 | −0.401 |
| SLC7A5 (LAT1) | −0.147 | +0.226 | −0.860 |
| ACY1 | −0.653 | −0.807 | −0.107 |
| ACSS1 | −0.771 | −0.914 | +0.382 |
| ACSS2 | −0.618 | −0.792 | +0.015 |

SLC16A7 is the only panel member with the same nonzero direction in all models and library omissions. SLC16A1 is inconsistent, including very small organoid effects with omissions on both sides of zero. ACY1 decreases in all aggregate contrasts, with a human omission range of **−0.262 to +0.057**. SLC22A6 and SLC22A8 averages are near zero in human organoids. The observed RNA patterns leave the relevant deacetylase activity, membrane transport and acetate use open.

Across the nine assigned hippocampal nuclear classes, SLC16A7 falls **140.64 → 77.91 CPM** (2,593 → 1,292 UMIs), and every single-class omission leaves a decrease (**−65.26 to −41.25 CPM**). Excitatory and inhibitory nuclei both show decreases. SLC16A1 rises **17.57 → 35.46 CPM** (324 → 588 UMIs), and every single-class omission leaves an increase (**+12.26 to +45.08 CPM**). Newly formed oligodendrocytes have the largest observed MCT1 increase by CPM, **46.70 → 330.35 CPM** (20 → 115 UMIs). The separate bulk hippocampal direction is lower. A single nuclear pool per genotype, divergent preparation and variable recovery preclude animal-level inference, and class omission does not resolve those limits. Reproduce pooled CPM by dividing the sum of gene UMIs by the sum of all UMIs across retained classes and multiplying by one million. [Nuclear class counts and denominators](nuclei.tsv)

## Consequence for the comparative assay

Use separate isotope labels on the leucine and acetyl moieties to follow precursor, product and donor/receiver uptake. If switching delivery bypasses the limiting step, levacetylleucine should improve recovery relative to free leucine at matched extracellular exposure, and the advantage should shrink at the same intracellular free leucine. An acetate-driven response may persist at equivalent leucine and should track acetate-derived label. A donor–receiver split predicts that drug uptake can rise while native lactate transfer or axonal recovery stays weak. Measure transport in both compartments at matched pH and activity, with a no-drug MCT control. The healthy and corrected genotypes define the specificity of an effect. A direct developmental assay needs independence from an acute clinical rating in another disease. [Alternative outcomes and rejection criterion](pretest_20261126.md)

**Next.** Calibrate the primary MCT1 transport concentration and lactate interaction, compare with regulatory human total and free exposure, and check the independently reported human-neurite effect. Keep plasma, CSF, bath and intracellular substrate separate. Apply the pediatric indication and age/weight data to feasibility while testing for stage dependence. [Cell-transport primary abstract](https://pubmed.ncbi.nlm.nih.gov/34349180/) · [FDA integrated review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2024/219132Orig1s000IntegratedR.pdf) · [Neurite article, primary abstract](https://doi.org/10.3389/fimmu.2026.1866462)

Replay with `python3 -B transport_screen.py FILES OUTPUT_DIRECTORY`.
