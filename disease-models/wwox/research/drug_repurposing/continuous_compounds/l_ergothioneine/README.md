# L-ergothioneine in WWOX loss of function

26 November 2026 · SCI_CODEX · P17 mouse cortical and hippocampal TPM, week 15 human cerebral organoid CPM and mouse hippocampal assigned nuclear UMI · [prespecified comparison](pretest_20261126.md)

**Decision at opening.** Keep purified L-ergothioneine active as a transporter-dependent redox hypothesis. The WWOX comparison supports measuring intake into individual cell types. Human organoid and mouse pooled neuronal directions differ, so neither a conserved uptake gain nor a generic uptake deficit follows. [Bulk contrasts](contrasts.tsv) · [Nuclear counts](nuclei.tsv)

Contrast is knockout minus control mean log2(1 + abundance). Parentheses give the approximate single-library omission range. These are descriptive sensitivity limits.

| Gene and prospective readout | P17 mouse cortex | P17 mouse hippocampus | Week 15 human cerebral organoid |
| --- | ---: | ---: | ---: |
| SLC22A4, OCTN1 | −0.16 (−0.33 to −0.04) | +0.07 (−0.27 to +0.38) | +0.28 (+0.18 to +0.38) |
| SLC22A15, alternate uptake route | +0.10 (+0.03 to +0.25) | −0.09 (−0.24 to +0.02) | +0.45 (+0.25 to +0.65) |
| SLC22A5, carnitine transport comparator | −0.65 (−0.80 to −0.56) | −0.87 (−1.02 to −0.71) | +0.71 (+0.68 to +0.77) |
| PRDX3, mitochondrial peroxide handling | −0.37 (−0.54 to −0.20) | −0.68 (−0.94 to −0.43) | +0.35 (+0.20 to +0.51) |
| GPX4, lipid peroxide control | −0.14 (−0.24 to +0.04) | −0.74 (−1.09 to −0.42) | −0.42 (−0.62 to −0.21) |

Human organoid SLC22A4 means increase **0.28 → 0.57 CPM** and SLC22A15 **0.88 → 1.60 CPM**, on low absolute abundance. SLC22A5 rises more strongly in organoids despite falling in both mouse bulk tissues. This cautions against assuming a substrate-specific transcriptional response. In the pooled mouse excitatory assignment, SLC22A4 falls **7.51 → 4.16 CPM** (93 → 43 raw UMIs) and SLC22A15 **16.73 → 13.14 CPM**. In assigned astrocytes, SLC22A4 is approximately stable (**22.58 → 22.66 CPM**) while SLC22A15 falls (**15.74 → 12.20 CPM**). The two microglial transporter signals are only zero to three UMIs per genotype and cannot establish lack of uptake. These data nominate an excitatory-versus-astrocyte exposure check. Assay different mitochondrial and lipid-peroxide endpoints if PRDX3 and GPX4 show different baselines. RNA abundance does not establish transporter protein, flux, subcellular delivery or enzymatic redox capacity. [Cortex](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682) · [Hippocampus](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) · [Cerebral organoids](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [Mouse nuclei](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684)

Mouse bulk cortex and hippocampus have 4/3 and 2/3 control/knockout libraries, with no independent-cohort inference between regions. The human organoids have 2/4 libraries from a shared parental line. Each assigned hippocampal nucleus group contributes one pool per genotype. Mouse bulk is gene-summed transcript TPM, human values are input-library CPM, and nuclear values are the class-summed transcript UMIs divided by total assigned class UMIs. [Held input hashes](../d_mannose/inputs.tsv)

**Independent comparators.** The human SLC22A15 expression-system study compared multiple SLC22 family members and reported ergothioneine uptake by SLC22A4 and SLC22A15. This supplies an assay and a transporter-discrimination control, without defining neural abundance or barrier transport. In a five-person human biospecimen study, reported group means were **107.4 ng/mL plasma** versus **1,285 ng/mL in erythrocytes**, a ratio of means of about **12**. The erythrocyte variation was large and this is not a subject-matched ratio, a supplementation estimate or a brain measurement. An oral pure-compound study in healthy humans monitored circulating retention. An oral mouse tissue study measured parent by LC-MS/MS and found whole-brain exposure alongside greater concentrations in blood and liver. Assess sampling, normalization, background diet, vascular contribution and the number of timed observations before inferring a central exposure bridge. Pediatric and co-medication data remain unresolved. [Primary SLC22A15 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7839234/) · [Paired sample assay abstract](https://pubmed.ncbi.nlm.nih.gov/23494799/) · [Human pure-compound abstract](https://pubmed.ncbi.nlm.nih.gov/27488221/) · [Mouse tissue abstract](https://pubmed.ncbi.nlm.nih.gov/29371632/)

**Prediction and next step.** In matched WWOX and corrected cells, a carrier-dependent rescue should require labeled intracellular parent and restore evoked function with lower native redox damage. Use activity-matched extracellular quenching, transporter perturbation, fraction purity and the carnitine comparator. A higher blood or whole-cell signal with unchanged mitochondrial and circuit recovery favors sequestration, a different compartment or a separate rate limit. The cortex comparison now constrains residual blood as an explanation in selected samples, with lower apparent affinity for SLC22A15 in a separate assay. Next verify the human plasma and erythrocyte time course and developmental fraction-specific CNS data. [Transport, cortex and blood controls](transport_and_cortex_20261126.md) A review could change priority if it retrieves measured ergothioneine in an existing WWOX neural data set or a credible developmental unbound-central exposure comparison.

### Replay

```sh
python3 -B disease-models/wwox/research/drug_repurposing/continuous_compounds/l_ergothioneine/uptake_screen.py /home/desktop/legend-development/files /tmp/ergothioneine-replay
```
