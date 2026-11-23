# Ganaxolone premise in an independent Wwox partial-loss model

**Decision.** In adult P47T mice, the positive myelin-challenge signature previously seen in a pool of Wwox-null microglia fails to transfer to whole hippocampus. This cohort provides no isolated microglia for a cell-specific replication. A tissue-sampling issue also weakens interpretation of the apparent opposite effect. Four independent choroid plexus markers covary with that hippocampal score. Accounting for their expression moves the P47T contrast from −0.286 to −0.035. This finding changes how we would evaluate the candidate drug: localize substrate and response in identified microglia before treating a bulk-tissue signal as a pharmacological premise. None of the mice in this reanalysis received ganaxolone.

## Question and units of observation

The original signature comprised 25 genes induced and 25 suppressed after exposing microglia to myelin in culture. The earlier Wwox neuronal deletion gave a negative whole-hippocampus score and a positive score in one microglial pool per genotype. This study tests whether the trained program recurs across genotypes and whether an anatomical difference can explain an apparent regional effect. The new cohort carries the P47T partial-loss allele that models SCAR12. Its animals are 150–280 days old. These features limit extrapolation to early severe WWOX deficiency. [Previous dossier](../ganaxolone_20261123/README.md) · [P47T study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10835625/) · [GSE215425](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE215425)

The [initial prediction](prediction.md) was fixed at dcd281564. The score for each library is mean log2(CPM + 1) of the up arm minus that of the down arm. We compared P47T with WT within sex and averaged the two differences. This avoids weighting the average according to unequal sex proportions. The deposited titles identify 3 male/2 female WT and 2 male/3 female P47T for the three forebrain regions. The available cerebella are 2 male/2 female WT and 1 male/2 female P47T. The same animal contributes tissue to several regions. We retained the sample identities from the deposit, checked their region and genotype against the series matrix, and made no estimate of a sex-by-genotype biological interaction. [Library-level values and animal identities](results/libraries.tsv)

| Region | Animals, P47T/WT | Myelin-challenge score change | Female / male contrast | Generic microglial marker change |
|---|---:|---:|---:|---:|
| Hippocampus, primary | 5/5 | −0.286 | +0.042 / −0.614 | +0.274 |
| Prefrontal cortex | 5/5 | +0.011 | +0.092 / −0.069 | +0.339 |
| Parietal cortex | 5/5 | +0.121 | +0.108 / +0.133 | +0.322 |
| Cerebellum | 3/4 | −0.076 | −0.038 / −0.115 | +0.705 |

All 50 genes were represented. The hippocampal contrast stayed negative on omitting each animal (−0.495 to −0.077). The four generic markers are Aif1, C1qa, C1qb and Tyrobp. Their expression may reflect cell abundance, activation or both. The particularly large cerebellar change alongside a flat-to-negative challenge score illustrates why a general increase in microglial markers cannot stand in for response to myelin. [Regional contrasts and sensitivities](results/panels.tsv)

## Which alternative explains the hippocampal score?

**Cell-type expression profiles.** We compared each target gene with genes of similar baseline expression across seven independently purified cortical cell classes. Twenty-three genes per arm could be matched. In hippocampus their observed contrast was −0.279, whereas the middle 95% of the 2,000 reference-panel effects was −0.205 to +0.066. This benchmark alone would make the decrease look unusual. In parietal cortex the matched target score was +0.134, close to the prespecified 95th percentile of +0.137. The reference omits choroid plexus epithelium and comes from younger cortex. These draws describe sensitivity to the choice of genes and do not supply biological replicates. [Purified-cell data](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52564) · [Benchmarks](results/benchmarks.tsv) · [Neighbor choices](results/neighbors.tsv)

**Anatomical control.** The hippocampal change came chiefly from increased expression of the arm normally suppressed by myelin. Its largest increases included Ttr (+1.863) and Col3a1 (+1.245). This motivated a [separately declared post hoc check](choroid_sensitivity.md). The four independent markers Aqp1, Prlr, Kcne2 and Folr1 were all higher in P47T hippocampus (+1.26 to +1.94). None appears in the challenge signature. The marker index correlated with Ttr at 0.96 after removing the four sex/genotype group means. Dissection studies have documented that adjacent choroid plexus can contribute RNA to hippocampal samples. A genuine genotype effect in this compartment could produce a similar association. [Independent evidence for the marker choice](https://doi.org/10.1371/journal.pone.0142195) · [Experimental validation of hippocampal dissection](https://pubmed.ncbi.nlm.nih.gov/35741684/) · [Marker estimates](results/choroid_markers.tsv)

| Hippocampal outcome | P47T effect | Adjusted for independent choroid index | Adjusted range on omitting one animal |
|---|---:|---:|---:|
| All 50 genes | −0.286 | −0.035 | −0.665 to +0.137 |
| Omit Ttr | −0.223 | −0.048 | −0.724 to +0.127 |
| Omit Ttr and Col3a1 | −0.182 | −0.027 | −0.629 to +0.121 |

The adjusted fit uses five residual degrees of freedom. Its wide leave-one-out range makes the size and even direction of the residual uncertain. Removing Ttr and Col3a1 alone leaves a negative difference. Including the independent marker index substantially attenuates it even after omitting both genes. Thus a seven-cell reference can miss the relevant anatomical alternative in this dataset. [Models](results/choroid.tsv) · [Individual marker measurements](results/choroid_libraries.tsv)

**Scope of this explanation.** Removing Ttr and Col3a1 from the trained signature left the positive myelin responses intact in APOE3, APOE4 and wild-type microglia (+1.79, +1.57 and +0.97). In the younger neuron-specific Wwox deletion, adding the four-marker index moved the complete hippocampal estimate from −0.279 to −0.327, with its leave-one-out range crossing zero. In the acquired day-14 kainate hippocampus the analogous change was −0.191 to −0.256. These separate checks restrict the anatomical explanation to the adult P47T observation. They give no evidence that the earlier microglial pool signal itself was a dissection artefact. [Original-context recalculations](results/original_contexts.tsv)

## Implication for drug repurposing

The hippocampal result fails the primary prediction. The parietal result is a regional lead of modest magnitude; its direction is shared by the small sex strata. The measurements that could change the decision are intracellular myelin cargo per identified microglial cell, clearance over time, and formation of new myelin in comparable regions with documented sampling boundaries. To implicate ganaxolone specifically, these outcomes must change with drug exposure in a WWOX model when network suppression is matched. A decline in general microglial markers or in seizure frequency alone would leave this mechanism unresolved.

## Reproduce

Use the GEO processed count table and sample matrix from GSE215425, the 14 deposited purified-cell spreadsheets from GSE52564, and the original frozen signature. Python 3, NumPy and xlrd are required. The optional transfer check also uses the [GSE171280 source matrix](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE171280), and the tissue files already listed in the [original dossier](../ganaxolone_20261123/README.md). Code, derived per-library and gene-level results, and input hashes are included. Original third-party matrices remain with their depositors. No additional full-paper reading is claimed for this calculation. [Inputs](results/inputs.sha256)

```bash
python3 analyze.py "$FILES" ../ganaxolone_20261123/results/signature.tsv results
python3 choroid.py "$FILES" ../ganaxolone_20261123/results/signature.tsv results
python3 transfer_check.py "$FILES" "$TRAINING" ../ganaxolone_20261123 results
```
