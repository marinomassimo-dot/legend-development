# Palmitoylethanolamide in WWOX loss of function

26 November 2026 · SCI_CODEX · completed comparison · P17 mouse cortical and hippocampal TPM, week 15 human cerebral organoid CPM and mouse hippocampal assigned nuclear UMI · [prespecified question](pretest_20261126.md)

**Disposition.** Defer palmitoylethanolamide (PEA) for pediatric WWOX trial priority. Keep it as a glial lipid and receptor-competence probe. [Glial and developmental comparisons](glial_response_and_disposition_20261126.md) The WWOX screen suggests altered supply and removal with different signs across species and cell classes. It gives no unique direction for intact endogenous PEA. An indiscriminate anti-inflammatory explanation is weak in the starting neural systems. [Bulk results](contrasts.tsv) · [Nuclear counts and denominators](nuclei.tsv)

Contrast is knockout minus control mean log2(1 + abundance); the approximate range across single-library omissions follows in parentheses. It is a sensitivity analysis, not a confidence interval.

| Gene and prospective readout | P17 mouse cortex | P17 mouse hippocampus | Week 15 human cerebral organoid |
| --- | ---: | ---: | ---: |
| PPARA, receptor | −0.29 (−0.46 to −0.20) | −0.29 (−0.49 to −0.08) | +0.02 (−0.15 to +0.20) |
| RXRA, receptor partner | −0.47 (−0.73 to −0.23) | −0.51 (−0.77 to −0.33) | +0.22 (+0.13 to +0.31) |
| NAPEPLD, one route of N-acylethanolamine production | +0.07 (−0.07 to +0.25) | −0.42 (−0.49 to −0.29) | −0.46 (−0.53 to −0.36) |
| FAAH, amide hydrolysis | −0.16 (−0.37 to +0.05) | −0.74 (−0.90 to −0.45) | −0.16 (−0.24 to −0.08) |
| NAAA, lysosomal N-acylethanolamine hydrolysis | −0.43 (−0.54 to −0.32) | −1.20 (−1.33 to −0.95) | +0.00 (−0.06 to +0.04) |
| ACOX1, peroxisomal fatty-acid oxidation | −0.34 (−0.47 to −0.10) | −0.39 (−0.64 to −0.17) | +0.28 (+0.16 to +0.39) |
| CPT1A, fatty-acid transfer for mitochondrial oxidation | −0.59 (−0.75 to −0.35) | −0.30 (−0.60 to −0.02) | +0.31 (+0.18 to +0.43) |

Both bulk mouse PPARA means are low (0.50–1.37 TPM across groups). In pooled assigned mouse astrocytes, PPARA decreases **56.1 → 29.1 CPM** (82 → 50 raw UMIs) and NAPEPLD **26.0 → 9.3 CPM**. NAAA also decreases **32.2 → 13.9 CPM**, which could oppose a loss of synthesis. The receptor signal in assigned microglia totals zero and two raw UMIs across the control and knockout pools. IL1B is undetected there. These depths do not establish either absence or a microglial PPAR-alpha response. Organoid PPARA dispersion covers both directions with each group mean around 14 CPM. Human ACOX1 and CPT1A rise despite lower NAPEPLD. Transcript sign therefore cannot identify a common oxidation deficit or motivate assuming that every WWOX model is PEA deficient. [Held cortex](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682) · [Hippocampus](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) · [Organoids](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [Hippocampal nuclei](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684)

Control/knockout library counts are 4/3, 2/3 and 2/4 in cortex, hippocampus and organoid. Cortex and hippocampus should not be counted as independent mouse cohorts. The human organoids share a parental line. Each hippocampal nuclear genotype contributes one pooled sample. Nuclear CPM are class-level sums divided by total assigned-class UMI. Absolute levels of lipid, receptor protein and fatty-acid oxidation are unavailable in the held expression data. [Held input hashes](../d_mannose/inputs.tsv)

**Initial outside comparators.** The reference PPAR-alpha reporter and Ppara-deficient edema tests provide a receptor perturbation control in a peripheral model. A primary rat experiment used isotope-labeled PEA in two oral formulations and distinguished experimentally inflamed and control tissue. Quantify the intact parent, the formulation effect and compartment before connecting to reporter response. A ten-week adjunctive randomized study in 70 children aged 4–12 years in a different indication used PEA on a risperidone background. It supplies a bounded human exposure setting and cannot establish chronic neural exposure, a specific WWOX mechanism, antiseizure efficacy or compatibility with background regimens in WWOX. [PPAR-alpha primary abstract](https://pubmed.ncbi.nlm.nih.gov/15465922/) · [Rat formulation and tracer study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5870042/) · [Pediatric randomized abstract](https://pubmed.ncbi.nlm.nih.gov/29807317/)

**Discriminating prediction.** If substrate limitation drives a WWOX glial defect while receptor response remains competent, added intact PEA should restore receptor-dependent fatty-acid flux and subsequently improve evoked neural recovery in affected cultures at measured exposure. Compare same-line palmitate, carrier and receptor controls. Equal isotope transfer to generic lipids or a cytokine fall without recovery supports a rival. If PEA reaches cells but a receptor control gives little response, test receptor competence before escalating exposure. The rat tracer comparison establishes an isotopologue signal in whole brain and compares formulations in plasma. Next verify dose-resolved glial and slice responses against this exposure scale while distinguishing direct PPAR-alpha signaling and downstream effects. [Tracer comparison and replay](brain_tracer_and_controls_20261126.md) A laboratory review could change priority if it finds endogenous PEA or glial lipid flux in an existing WWOX data set.

### Replay

```sh
python3 -B disease-models/wwox/research/drug_repurposing/continuous_compounds/palmitoylethanolamide/pea_screen.py /home/desktop/legend-development/files /tmp/pea-replay
```
