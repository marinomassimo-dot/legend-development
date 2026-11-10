# Consumer delta — IT41 light queue, Wwox-loss Drosophila feasibility (proposals only; nothing applied)

Task record `ORCH-IT41-20261109`. Every row names the consumer file and row, the proposed change, the source and the read depth. The integrating session (IT41) decides; this package edits none of these files, no ranking, no dashboard, no need, no new registry. Paths are relative to `disease-models/wwox/research/drug_repurposing/`.

**Point of the generative path that should use the result.** None today: the fly question (does a rescuable Wwox-loss readout change with Nmdar1 dosage) is a feasibility statement, not an investigation. It should enter generation only as a condition on the AMPA/NMDA arm if a reproducible neuronal readout appears (`output/feasibility.tsv` FE06, FE10).

## What changes in the conclusions, and what does not

| Changes | Does not change |
|---|---|
| The 2005 radiation-sensitivity phenotype and its fly or human WWOX rescue are not carried as a Wwox-loss result (background mutations per 21075834) | Fly Wwox as a modifier of other genes' phenotypes (Idh, Sod, respiratory-complex outgrowths) |
| The two fly sleep datasets disagree on the light phase; reconcile before reproducing | The amyloid-context work and its separation from loss of function |
| A Wwox antibody and protein-absence data exist for the f04545 and Wwox1 flies | The absence of any seizure, NMJ or electrophysiology test of a Wwox-loss fly (none found) |
| The fly question is genetic (Nmdar1 dosage) with drug arms second | Every mouse-slice package (AMPA, NMDA, BNIP3) |

## Proposals

| # | Consumer and row | Proposed change | Source and depth |
|---|---|---|---|
| 1 | `modifiers_it12_p1b_20261031/usability_table.tsv`, row "Drosophila Wwox genetics (PMID 21075834, 26302329, 16007179, 26390919)" (line 15) | Keep the modifier statement; add that 16007179's radiation phenotype is superseded by 21075834 (background mutations) and that 16007179 carries an erratum; no published rescue of a Wwox-loss phenotype was found in the sources opened | 21075834 (partial), 16007179 and 26390919 (abstract only) |
| 2 | `recovery_it10_p23_20261031/paths_verdicts.tsv`, row `b_genetic_modifiers_suppressors` (line 3) | Same note: the fly rows describe modifiers of other genes' phenotypes; the 2005 rescue is not a recovery path | 21075834 |
| 3 | `batch_sci_20261105/map/open_questions_map.tsv` | If the map takes new questions: add "Does a rescuable Wwox-loss readout in the fly (sleep, lifespan) change with Nmdar1 gene dosage?" with the precondition of reconciling the two sleep genotypes; label IPOTESI; no rank | `output/feasibility.tsv` FE06, FE10-FE12 |
| 4 | `needs/needs.json`, the entry that mentions model organisms (if any) | Add the open measurement list from `output/feasibility.tsv` ("what is missing" cells); the file cannot hold genotype, sex and metric as separate fields (format limit) | `output/feasibility.tsv` |

## Not proposed (and why)

* No fly arm in any pharmacological comparison: the fly cannot discriminate GluN2A from GluN2B, AMPA from kainate at central synapses, or cortical burst firing.
* No stock request, contact or commissioning: availability is unconfirmed and external contact is out of scope.
* No transfer of amyloid-model results.

## Reads still open (none required for this delivery)

2006 erratum text; Supp Fig S1 of the 2011 paper (protein absence); stock-centre records (BDSC, FlyBase, Alliance) when reachable; full text of 16007179, 26390919 and 17395332; Marrus 2004.
