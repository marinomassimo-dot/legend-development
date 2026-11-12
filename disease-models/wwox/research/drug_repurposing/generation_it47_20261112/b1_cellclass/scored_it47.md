# IT47 queue B1: scoring of the cell-class extraction (predictions in `prereg_it47.md`, committed before the run)

Non-canonical working note. RNA class means (FPKM); not channel number, current, protein or function; no claim on WWOX; no compound. Inputs: the same hash-recorded GEO tables as SCI44 and IT46 (`input_digests_it47.tsv`; copied from the producer's scratch directory into the untracked local store, not downloaded). Extraction: `targets_expression.py` (a copy of the SCI44 script with a new gene list). Convention: floor 1 FPKM, 3-fold (`cell_context.py`).

## Predictions against results (mouse P7 neurons against the best other class; human is one neuron sample)
| Gene | Predicted | Mouse | Human sample | Score |
|---|---|---|---|---|
| Grin1 | neuron-enriched | neuron-enriched (63.50 against OPC 16.02) | not detected | held |
| Grin2a | neuron-enriched | **not detected (0.76)** | neuron-enriched (25.30) | **miss** |
| Grin2b | neuron-enriched | neuron-enriched (2.98 against microglia 0.84; low) | neuron-enriched | held |
| Gria1 | neuron-enriched | neuron-enriched (52.64) | neuron-enriched | held |
| Gria2 | neuron-enriched | **shared: astrocytes 167.22 against neurons 57.50** | shared | **miss** |
| Gria3, Gria4 | not neuron-enriched | OPC 54.65 against 4.52; OPC 37.82 against 22.15 | neuron-enriched in the sample | held (mouse) |
| Grik2 | neuron-enriched | **shared (8.68 against oligodendrocyte lineage 15.98)** | neuron-enriched | **miss** |
| Gjd2 | neuron-enriched or not detected | neuron-enriched (3.24 against 0.29) | not detected | held |
| Panx1 | not neuron-enriched | shared (25.74 against 37.21) | enriched elsewhere | held |
| Pdk1, Pdk2, Pdk3, Pdk4 | none neuron-enriched | shared, shared, enriched elsewhere, enriched elsewhere (astrocytes 63.70 against 2.17) | none | held |
| Hcn4 | not detected | **neuron-enriched (16.81 against 0.36)** | not detected | **miss** |
| Kcnq4 | not detected | **shared (5.24 against astrocytes 6.21)** | not detected | **miss** |
| Kcnj16 | not neuron-enriched | enriched elsewhere (0.25 against OPC 7.02) | enriched elsewhere | held |
**12 of 17 held, 5 missed.** The misses are as informative as the hits: Gria2 and Grik2 are not neuron-enriched in the mouse class means (astrocytic Gria2 is a known pattern, which I did not apply); Hcn4 is read at 16.81 FPKM in mouse neurons and at a level below the floor in the one human sample (a species or sample difference, not resolved here); Grin2a is below the floor in P7 mouse neurons and high in the human sample (age or class composition); Kcnq4 is shared.
## What it changes (INFERENZA; RNA, small n, one age per class)
`relation_context_summary.py` recounted: of 75 relation-gene pairs, **12 are neuron-attributable, 63 are not assignable to neurons, 0 are unknown**; 17 of 19 relations have at least one target that cannot be assigned to neurons; 2 relations have every target attributable. The coverage gap is closed; the reading is **not** that most targets are non-neuronal: "not assignable" counts shared, enriched elsewhere, not detected and table disagreement alike, and the classes are different ages. Kv7: KCNQ5 is neuron-enriched in both tables (mouse 9.40 against 0.98; human sample 15.00), KCNQ4 shared in mouse and not detected in the human sample, so the earlier statement that KCNQ4 and KCNQ5 were not queried is superseded (dated update on V10 and INV-18). HCN: Hcn3 and Hcn4 are neuron-enriched in mouse (16.17 and 16.81); the human sample reads Hcn4 below the floor and Hcn3 shared.
## Limits
P7 mouse neurons and P17 oligodendrocyte-lineage classes (two pools each) and one human neuron sample; purified-class carry-over; RNA is not protein or function; no ranking, direction or need was changed.
