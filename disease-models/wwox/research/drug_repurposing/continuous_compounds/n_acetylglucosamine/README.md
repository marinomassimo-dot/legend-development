# N-acetylglucosamine opening comparison in WWOX loss of function

**Data scope.** P17 neuronal Wwox-deletion mouse cortex and hippocampus gene-summed TPM, human WWOX-null week-15 cerebral organoid library CPM and pooled P17 mouse hippocampal single-nucleus UMI CPM by marker-assigned class. [Prespecified comparison](pretest_20261127.md)

**Bulk comparison.** MGAT1 RNA declined in cortex (35.80→19.19 TPM), hippocampus (28.70→15.19 TPM) and organoids (120.71→113.82 CPM), with direction retained through every single-library omission. The organoid difference is small. MGAT5 fell in both mouse tissues and rose in organoids (75.17→134.89 CPM) under every omission. UAP1 fell in both mouse tissues and rose modestly in organoids. No shared donor or distal-branch deficit is established by this panel. [Fixed bulk contrasts](bulk.tsv)

**Composition check.** Bulk hippocampal PDGFRA RNA fell (20.96→13.01 TPM), but the assigned OPC pool showed an increase (198.86→290.36 CPM). In the same pooled OPC fraction MGAT1 fell (13.18→9.47 CPM), with 12 MGAT1 UMIs in each pool against a larger total UMI denominator in knockout. These are one pool per genotype and the RNA contrasts cannot resolve receptor surface residency, branch occupancy, lineage kinetics or whether the effect is cell-autonomous. [Assigned nuclei](nuclei.tsv)

**Disposition.** Park for an unselected pediatric WWOX trial. Tracing supports delivery of labeled carbon to a brain nucleotide-sugar pool. The four-week mouse injury comparison increases both myelinated profiles and total profiles, with little change in the derived proportion. Reopen for measured neural engagement at an attainable exposure, increased first-sheath formation and restored conduction. [Tracer, comparator and decision](exposure_and_branching_20261127.md)

Run `python3 -B replay_expression.py PATH_TO_FILES OUTPUT_DIRECTORY` to reproduce both tables. [Held input identifiers and hashes](../creatine/inputs.tsv)
