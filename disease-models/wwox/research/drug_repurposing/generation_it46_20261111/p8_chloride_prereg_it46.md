# IT46 P8: the same RNA sample asked a different question (GABA and chloride genes), predictions fixed before the run

Non-canonical working note. RNA class means (FPKM) only; not channel number, current or share; no claim on WWOX; no compound. Written before the genes were extracted; inputs are the local GEO tables already hashed for SCI44 (mouse GSE52564 cell classes, human GSE73721 groups). Convention as in `cell_context.py` (floor 1 FPKM, 3-fold).

Predictions (mouse P7 neurons against the best other class; the human neuron sample is one sample):
| Gene | Prediction |
|---|---|
| Slc12a5 (KCC2) | NEURON_ENRICHED |
| Slc12a2 (NKCC1) | not neuron-enriched (OTHER_ENRICHED or SHARED) |
| Slc6a1 (GAT-1) | SHARED between neurons and astrocytes |
| Abat (GABA-T) | not neuron-enriched (glial or shared) |
| Gabra1, Gabrb3, Gabrg2 | NEURON_ENRICHED |
| Gad1 | NEURON_ENRICHED |
What the result is for: relations S5 (GABA-A modulation), S6 (NKCC1/KCC2) and S7 (GABA reuptake or transaminase block) have target genes with no held cell-class row; `cell_context` returns NOT_IN_TABLE for all of them. This changes only that coverage; the S7 result (written with NOT_IN_TABLE) is not rewritten: the context join is reported as having added nothing **on the day of the case**.
