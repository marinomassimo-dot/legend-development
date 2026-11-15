# WO-32 remainder: class IIa HDAC RNA along the oligodendrocyte lineage (IT, 2026-11-15)

Non-canonical working note. Not medical advice; no dose, schedule or route; no compound nominated. Reference genotype class only. No ranking, need, candidate state or frozen package edited. RNA is not protein or function; a value below the floor is unknown at the protein level, not shown absent. Predictions frozen in commit a3f645d42 (2026-11-15T13:29:02Z) before the extraction was run.

## Answer first
In the held mouse RNA table (GSE52564, FPKM, two replicates per class), **all four class IIa genes are detectable in the oligodendrocyte lineage; none is oligodendrocyte-enriched.** Hdac5 is high everywhere (OPC 18.6, newly formed 29.7, myelinating 39.3; neurons 50.6, the highest); Hdac7 is 4.5 / 3.2 / 1.9 in the three lineage classes (endothelial 24.9, astrocytes 14.1, neurons 13.7); Hdac9 2.4 / 1.7 / 1.7 (astrocytes 4.4, neurons 3.6); Hdac4 2.8 / 1.3 / 0.9 (neurons 4.0, astrocytes 4.0). In the held human table (GSE73721, adult cortex groups) the oligodendrocyte group is below the 1.0 floor for HDAC4 (0.84), HDAC5 (0.34) and HDAC7 (0.10) and above it only for HDAC9 (2.90; neurons 12.60). **So the "nothing found" null on class IIa in myelin is not explained by absent RNA in the mouse lineage; whether human oligodendrocytes express them is a different, lower reading** (species and age differ: mouse P17 sorted classes, human adult cortex groups). This is an RNA answer for the second half of WO-32; the neuron/axon half was closed in IT32.

## Prediction scores (`prediction_frozen.md`)
| | Prediction | Result |
|---|---|---|
| F1 | Hdac7 below the floor in the three lineage classes; endothelial highest | **MISSED on the floor** (4.47, 3.15, 1.89 in mouse), HELD on endothelial highest (24.94); human oligodendrocyte group 0.10 is below the floor |
| F2 | Hdac9 below the floor in at least two lineage classes | **MISSED** (2.35, 1.72, 1.71 in mouse) |
| F3 | Hdac4 or Hdac5 reaches the floor in at least one lineage class | HELD (Hdac5 18.6-39.3; Hdac4 2.8 in OPC) |
| F4 | no class IIa gene enriched 3-fold in the lineage; at most one neuron-enriched | HELD (no gene is 3-fold over the best other class in any lineage class; none neuron-enriched either) |
| F5 | the RNA does not support expression at a level relevant to a myelin lever | **MISSED as worded** for mouse (expression is present); what the RNA cannot support is any lever claim, because expression is not function and the human adult group is low |
Two of five predictions missed in the direction of more expression than I expected; the human reading is closer to the prediction than the mouse one.

## What this does not do
It does not read any paper; a Europe PMC census (abstract-level, full-text-matching query) returned 278 hits for HDAC9 and 215 for HDAC7 with oligodendrocyte or myelination terms, most not about oligodendrocytes (disc degeneration, glioblastoma, astrocyte reactivity, reviews); none was opened. The literature half of WO-32 (a verified bounded null for class IIa in myelin) is therefore not done; the RNA answer does not substitute for it. Limits: two replicates per mouse class, no replicate count printed for the human groups, sorted-cell RNA of different ages and species, joint 1.0 floor and 3-fold rule of `generation_it46_20261111/cell_context.py` as in HE50; inputs digested in `input_digests.tsv` (copied from HE50; the extraction wrote the two tables here unchanged: `targets_expression.py --genes HDAC4,HDAC5,HDAC7,HDAC9 --prefix wo32_classiia`).
