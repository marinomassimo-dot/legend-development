# Ambroxol hydrochloride in WWOX loss of function

26 November 2026 · SCI_CODEX · active comparison · P17 mouse cortical and hippocampal TPM, week 15 human organoid CPM, hippocampal assigned nuclear UMI · [prespecified question and discriminating predictions](pretest_20261126.md)

**Decision at opening.** Keep ambroxol as a test of lysosomal lipid turnover. The WWOX expression screen provides an alternative to low GBA1 expression: lysosomal delivery of enzyme could be constrained in some stages. Measure localization and activity in the same cells before assigning substrate rescue or clinical priority. If GCase protein is present but lysosomal delivery fails, more total protein would be a weak success measure. [Bulk contrasts](contrasts.tsv) · [Nuclear denominators](nuclei.tsv)

The contrast is knockout minus control mean log2(1 + abundance). Parentheses give the minimum and maximum under one-library omission. These are descriptive sensitivity ranges. The historical symbol GBA in the output corresponds to GBA1 (mouse Gba, Ensembl ENSMUSG00000028048).

| Gene and prospective readout | P17 mouse cortex | P17 mouse hippocampus | Week 15 human cerebral organoid |
| --- | ---: | ---: | ---: |
| GBA1, lysosomal glucocerebrosidase | −0.04 (−0.18 to +0.15) | +0.09 (−0.18 to +0.25) | +0.21 (+0.05 to +0.37) |
| SCARB2, GCase lysosomal transport receptor | −0.35 (−0.54 to −0.08) | −0.22 (−0.41 to −0.06) | −0.23 (−0.29 to −0.18) |
| PSAP, precursor of lysosomal GCase cofactor saposin C | −0.18 (−0.48 to +0.10) | −0.64 (−0.91 to −0.42) | +0.28 (+0.13 to +0.41) |
| LAMP1, lysosomal compartment control | −0.23 (−0.38 to −0.07) | −0.12 (−0.21 to −0.04) | +0.28 (+0.13 to +0.40) |
| TFEB, lysosomal transcriptional regulation | −0.55 (−0.80 to −0.17) | −0.01 (−0.18 to +0.15) | −0.27 (−0.31 to −0.23) |

SCARB2 moves from 153.23 to 130.62 CPM in human organoids. In the mouse hippocampal nuclear comparison, it rises in excitatory assignments (25.37 → 28.12 CPM) and inhibitory assignments (32.69 → 35.18 CPM) and declines in astrocyte assignments (52.01 → 43.59 CPM). PSAP takes these same directions in the three assignments, opposite to the fall in the hippocampal bulk for the two neuronal assignments. This motivates testing cell composition and cell-type specificity before interpreting the bulk as a cell-autonomous transport lesion. The gene set was prespecified. RNA and nuclear counts do not measure mature enzyme amount, lysosomal pH, compartmental localization or substrate turnover. [Cortex](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682) · [Hippocampus](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) · [Human organoids](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [Mouse nuclei](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684)

The control/knockout library counts are 4/3, 2/3 and 2/4 in cortex, hippocampus and organoid. The mouse bulk tissues are not independent cohorts. Organoids share a parent line. Each hippocampal genotype contributes one nuclear pool. Bulk mouse values use gene-summed transcript TPM, human library-normalized CPM and nuclei sum assigned-gene UMI over total assigned-class UMI. Use the [held input hashes](../d_mannose/inputs.tsv) and [replay script](gcase_screen.py).

**Independent precedents and limits.** LIMP-2-deficient fibroblasts recover GCase distribution and levels after LIMP-2 reconstitution. Maegawa et al. report ambroxol's pH-dependent mixed direct inhibition alongside greater GCase activity and protein after treatment of some Gaucher fibroblast genotypes. The enzyme delivery and direct occupancy arms thus require separate measurements in WWOX. A five-participant open-label neuronopathic Gaucher pilot used concurrent enzyme replacement and reported a CSF biomarker response. A randomized study in adults with Parkinson disease dementia showed no clear primary clinical outcome separation. These data anchor distinct control and exposure questions. They cannot establish neurological pediatric efficacy, long-term tolerability with antiseizure medicines or comparable cell physiology in WWOX. [LIMP-2 primary abstract](https://pubmed.ncbi.nlm.nih.gov/18022370/) · [Ambroxol biochemical abstract](https://pubmed.ncbi.nlm.nih.gov/19578116/) · [Gaucher pilot abstract](https://pubmed.ncbi.nlm.nih.gov/27042680/) · [Adult randomized trial abstract](https://pubmed.ncbi.nlm.nih.gov/40587145/)

**Next comparison.** The paired CSF countercheck shows how a change in measured extracellular activity can coexist with more protein and no measured substrate reduction. Compare acute inhibition, washout activity and intact-cell biochemical recovery at matched free exposure and pH. [Clinical compartment and fixed-pH comparison](compartment_exposure_20261126.md) In a matched WWOX preparation, test whether lower lysosomal GCase relative to whole cell is accompanied by higher native substrate and a selective, sustained response. True rescue also requires preserved evoked function. A broad lysosome/pH shift changing other hydrolases at the same exposure, or a drug effect seen only with drug present, predicts a distinct mechanism. A review could change priority if existing stage-matched WWOX lysosomal chemistry or realistic paired human exposures change what can be falsified.

### Replay

```sh
python3 -B disease-models/wwox/research/drug_repurposing/continuous_compounds/ambroxol/gcase_screen.py /home/desktop/legend-development/files /tmp/ambroxol-replay
```
