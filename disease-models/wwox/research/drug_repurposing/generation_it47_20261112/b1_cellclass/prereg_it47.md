# IT47 queue B1: cell-class rows for the targets that have none (predictions fixed before the run)

Non-canonical working note. RNA class means (FPKM); not channel number, current, protein or function; no claim on WWOX; no compound. Written and committed before the genes were extracted.

**Why.** `relation_context_summary.py` (DREAM, IT47) found 48 relation-gene pairs (30 distinct genes) with no row in any held cell-class table: GJD2, GRIA1-4, GRIK1-5, GRIN1, GRIN2A-D, HCN3, HCN4, KCNJ4, KCNJ12, KCNJ16, KCNK4, KCNK10, KCNK13, KCNQ4, KCNQ5, PANX1, PDK1-4.
**Inputs.** The same two hash-recorded GEO tables as SCI44/IT46 (mouse GSE52564 cell classes, human GSE73721 groups), copied from the producer's scratch directory into the local data store `files/geo/` (untracked) with the digests in `input_digests_it47.tsv`; no download. Extraction by a copy of the SCI44 script with a new gene list. Convention as in `cell_context.py` (floor 1 FPKM, 3-fold).
**Predictions** (mouse P7 neurons against the best other class; "either" means both outcomes are accepted as held):
| Gene(s) | Prediction |
|---|---|
| Grin1, Grin2a, Grin2b | NEURON_ENRICHED |
| Gria1, Gria2 | NEURON_ENRICHED |
| Gria3, Gria4 | not NEURON_ENRICHED (shared or elsewhere) |
| Grik2 | NEURON_ENRICHED |
| Gjd2 | NEURON_ENRICHED or NOT_DETECTED (either) |
| Panx1 | not NEURON_ENRICHED |
| Pdk1, Pdk2, Pdk3, Pdk4 | none NEURON_ENRICHED |
| Hcn4 | NOT_DETECTED |
| Kcnq4 | NOT_DETECTED |
| Kcnj16 | not NEURON_ENRICHED (astrocytic) |
**What changes if it holds or fails.** Only the `cell_context` coverage and the counts of `relation_context_summary.py`; no ranking, direction or need. Scored in `scored_it47.md` with the misses stated.
