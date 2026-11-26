# Urolithin A and mitochondrial cargo clearance in WWOX loss of function

**Data scope.** Untreated juvenile mouse Wwox neuronal-deletion cortex and hippocampus in TPM, WWOX-knockout human week-15 cerebral organoids in library CPM, and P17 mouse hippocampal nuclei in pooled assigned UMI CPM. The external comparison uses mouse retinal reporter ratios and hindlimb scores, ARPE-19 reporter puncta and cytosolic DNA foci per cell, adult mouse brain LC-MS and seizure events per animal, and adult human plasma total concentrations.

`context_policy: QUESTION_DRIVEN`. The [pretest](pretest_20261126.md) fixed 15 genes and competing predictions before inspecting the datasets. Existing analyses of [general cargo turnover](../trehalose/README.md), [polyamine routing](../spermidine/README.md) and [substrate use](../acetyl_l_carnitine/README.md) motivate a narrower question about mitochondrial clearance and replacement.

## Held WWOX comparison

PINK1 and OPA1 are lower in each of the three bulk or organoid comparisons. The sign survives every single-library omission for both genes. Control-to-KO means and library counts are as follows. [Bulk table](bulk.tsv)

| Model and unit | Control / KO | PINK1 | OPA1 |
|---|---:|---:|---:|
| Mouse cortex, TPM | 4 / 3 | 222.493 → 157.280 | 23.193 → 15.820 |
| Human week-15 cerebral organoids, CPM | 2 / 4 | 190.357 → 167.994 | 36.831 → 24.438 |
| Mouse hippocampus, TPM | 2 / 3 | 128.510 → 57.390 | 26.468 → 20.938 |

PRKN is lower in human organoids (5.759 → 4.344 CPM) and mouse hippocampus (10.137 → 8.335 TPM), with every omission negative. In mouse cortex it rises slightly (19.264 → 19.821 TPM) with omission results that cross zero. Mouse source tables list the ortholog as `Park2` (ENSMUSG00000023826), shown as PRKN in the harmonized tables. TFAM is lower in organoids and bulk hippocampus. PPARGC1A increases in cortex and organoids, with heterogeneous omission results in hippocampus. BNIP3 increases in cortex and organoids and falls in bulk hippocampus. LAMP1 falls in the two mouse tissues and rises in organoids. These different directions motivate measuring clearance, replacement and lysosomal capacity separately. [Mouse ortholog](https://www.informatics.jax.org/marker/MGI%3A1355296) · [Bulk table](bulk.tsv)

The P17 hippocampal pools weaken a cell-general interpretation. PINK1 is 13.17 → 12.47 UMI CPM in assigned excitatory nuclei, 10.29 → 12.26 in inhibitory nuclei (17 and 23 assigned gene UMIs) and 17.79 → 28.48 in astrocytic nuclei (26 and 49 gene UMIs). OPA1 is close to flat in excitatory and inhibitory pools and higher in the astrocytic pool. PRKN is stable or higher in all three. Each genotype has one pooled library. The pools do not provide independent animals or a matched cell-level replication of the bulk contrasts. Mitochondrial cargo turnover, absolute organelle abundance, mitochondrial membrane potential and respiratory reserve were not measured. [Nuclear counts and denominators](nuclei.tsv) · [GSE158682](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682) · [GSE156243](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [GSE158681](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) · [GSE158684](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684)

## Decision and replay

Keep urolithin A as a mechanistic comparator for mitochondrial quality control. Park it for an unselected pediatric WWOX trial. Reopen for measured neural exposure and a reproducible, preferential WWOX gain in native cargo clearance, absolute ATP recovery and evoked output after washout. The [external source-data audit and decision](exposure_and_disposition_20261126.md) documents three ways in which a reporter or seizure phenotype can change without demonstrating this mechanism.

Run `python3 -B replay_expression.py HELD_INPUT_DIRECTORY OUTPUT_DIRECTORY` from this folder. The input filenames and SHA-256 digests are in the [held input manifest](../creatine/inputs.tsv). The replay extracts means and log ratios on the original scales using the common WWOX loaders. Pooled CPM uses assigned cell-class UMIs as denominator and bulk omission ranges discard one library per iteration. No between-preparation pooling, significance tests on nuclei or cross-platform fold threshold was used. [Expression replay](replay_expression.py)
