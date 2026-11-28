# γ-L-glutamyl-L-cysteine in WWOX loss of function

**Data scope.** P17 neuronal-Wwox-deletion mouse cortex and hippocampus TPM, week-15 human WWOX-knockout cerebral organoid library CPM, and P17 hippocampal assigned nuclear UMI CPM with one pool per genotype. External measurements include lymphocyte GSH in adults and tissue GSH and ATP in adult mice.

[Fixed comparison and predictions](pretest_20261126.md) · [Human, mouse and molecular evidence](exposure_and_disposition_20261126.md)

## Which glutathione step could limit recovery?

| Model and control/KO libraries | Mean GSS, control → KO | Mean SLC25A39, control → KO | GCLC and GCLM joint pattern |
|---|---:|---:|---|
| Mouse cortex, 4/3, TPM | 23.86 → 25.83 | 103.16 → 70.93 | GCLC inconsistent on omissions. GCLM rises. |
| Mouse hippocampus, 2/3, TPM | 18.67 → 12.87 | 105.67 → 80.73 | Both decrease in every omission. |
| Human organoids, 2/4, library CPM | 33.66 → 37.89 | 99.61 → 84.35 | GCLC rises and GCLM falls. |

The GSS direction within each dataset survives single-library omissions. It differs by context, so bypassing GCL requires checking the remaining GSS capacity, especially in the hippocampus. The SLC25A39 fall persists in all bulk omissions, with corresponding log2(1+abundance) contrasts of −0.59, −0.49 and −0.24 in table order. SLC25A40 also declines in hippocampus, with no stable direction in the other two models. Glutathione recycling (GSR) declines in mouse cortex but rises in organoids. The earlier SLC7A11 decline reproduces across all three models. GGT1 declines in both mouse regions, while the stable GGT5 directions are opposite in cortex and organoids. Cleavage capacity, protein stability and metabolic flux remain unmeasured. [Bulk means and omission ranges](bulk.tsv) · [NAC comparator](../acetylcysteine/mechanism.md)

**Cell-context countercheck.** In the mouse hippocampal pools, SLC25A39 does not show a common decrease in the two neuronal classes. Excitatory CPM is 4.69→4.93 (58→51 assigned UMIs), inhibitory 10.90→11.20 (18→21), and astrocytic 9.58→7.55 (14→13). GSS falls in excitatory and inhibitory pools (19.39→10.73 and 18.16→11.73 CPM), and rises in astrocytes (14.37→18.02). These are descriptive summaries. Library depth, cell-class mixture and lack of replicate pools preclude a cell-specific transport conclusion. [Assigned counts](nuclei.tsv)

**Mechanistic implication.** The held comparisons motivate two separable measurements. Does the intact peptide bypass substrate limitation and support GSS-dependent GSH synthesis? Does newly made GSH also increase in the mitochondrial compartment and improve oxidative or evoked recovery? The second outcome could fail despite a positive first outcome. A direct GPX1-dependent redox response could also improve a peroxide endpoint without producing additional GSH. [Mitochondrial GSH uptake and whole-cell counterexample](https://doi.org/10.1038/s41467-022-30126-9) · [GPX1 primary study](https://doi.org/10.1038/ncomms1722)

**Decision.** Retain the intact-peptide versus cleavage comparison as a preclinical redox probe. Park for unselected pediatric WWOX trial priority. Reopen for measured parent exposure and genotype-selective, compartment-defined functional benefit.

**Replay.** From this directory run `python3 -B replay_expression.py HELD_INPUT_DIRECTORY OUTPUT_DIRECTORY`. [Input names and hashes](../creatine/inputs.tsv) · [GSE158682 cortex](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682) · [GSE158681 hippocampus](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) · [GSE156243 organoids](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [GSE158684 hippocampal nuclei](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684)
