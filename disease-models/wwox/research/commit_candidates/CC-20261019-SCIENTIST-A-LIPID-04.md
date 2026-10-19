# CC-20261019-SCIENTIST-A-LIPID-04 — very-long-chain sphingolipid, VLCFA and peroxisome comparators of group G1

`context_policy: QUESTION_DRIVEN`. **Author:** ACTOR_ID `scientist-a`, metabolic batch G1, 2026-10-19, task `METAB-G1-A-20261019`.
**Status:** `PROPOSED — NOT PROPAGATED`. **Change class: MINOR** (identity records of non-WWOX comparators; no claim touched; one proposed method note for RL-003). `target_wm_version`: next MINOR after the integrator's current value.
**Nothing here is medical advice.** Numbering is provisional. Every paper in this candidate has the word WWOX zero times unless stated; records are comparators and must carry that fact.

## 1 · Landings (this file grows by section as the lot proceeds)

| # | Source | Receipt (staged) | Landing proposed |
|---|---|---|---|
| 1 | PMID 41715204 (Sun 2026, J Transl Med, CerS2 conditional knockout, very-long-chain sphingolipids and myelination) | `FTR-20261019-41715204-01` (partial: supplementary video not inspected) | New `PAPER` record (none exists), type murine mechanistic comparator, T3, relevance LOW (WWOX absent) |

## 2 · Record content (source 1)

What it measures: brain lipidomics, imaging, proteomics, EM and culture assays in CNS and oligodendrocyte-lineage CerS2 knockout mice. WWOX: zero occurrences.

Note text to carry:
🔴 **A comparator and a design template, not WWOX evidence.** Cell-of-origin differs from the recorded WWOX myelin defect: here the oligodendrocyte-lineage deletion suffices, whereas CLAIM 003 records WWOX hypomyelination as non-cell-autonomous after neuronal deletion and CLAIM 005's boundary records astrocyte and oligodendrocyte Wwox deletions as negative. The microdomain step rests on a cholesterol-depletion experiment (beta-cyclodextrin, about 40 percent, flat across 50 and 250 uM) that does not remove very-long-chain sphingolipids. P20 EM has two animals in one arm and the plotted group sizes are the reverse of the legend. Whole-brain proteomics (deposited table) shows GFAP about 3.2-fold up, undiscussed in the paper. Supplementary video not inspected.

## 3 · Method note proposed for the myelin line (no claim change)

If a Wwox-null or P47T brain lipidomics is ever run for question 1 of the metabolic batch, the species to read are C16-C18 versus C22-C24 ceramides, sphingomyelins, hexosylceramides and sulfatides, white-matter imaging, and raft-fraction lipids at P20; a neuron-OPC co-culture with independently genotyped partners separates cell-autonomous from non-cell-autonomous action. IPOTESI; no such measurement exists in the repository.

## 4 · What must NOT be written

- No statement that WWOX loss alters very-long-chain sphingolipids, ceramide chain length or cholesterol in brain or myelin.
- No claim link; no individual-level content.

## 5 · Registry statements to re-check at integration

None existing for this PMID. CLAIM 003 and CLAIM 005 are unchanged.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. Hypomyelination at P20 | EM images revealed significant reductions in both the number and thickness (g-ratio) of myelin sheaths in cKO-nestin mice as early as P20. | Results, section 2, `files/fulltext/PMID41715204_Sun2026_PMC.xml`
2. Beta-cyclodextrin effect described as severe | Addition of 50 μM β-CD to wild-type co-cultures severely impaired myelination (Fig. 6C), and a higher dose at 250 μM showed no additive effect (Fig. 6D). | Results, section 6, same artefact
3. Causal link incomplete | We acknowledge that a definitive causal link requires supplementation with purified individual VLC species, but this remains technically challenging due to difficulties in isolating specific VLC sphingolipids (e.g., distinct ceramides). | Results, section 7, same artefact
4. P20 sample sizes in the legend | (C) The g-ratio of myelin sheath in P20 mice corpus callosum, n = 4 for Ctrl, n = 2 for cKO-nestin mice. | Figure 2 legend, same artefact
5. GFAP up in the whole-brain proteome | Gfap coverage 74.4: LFQ CKO 18655000000 18549000000 14626000000 15183000000 \| WT 6816800000 4273900000 3985400000 5758200000 \| ratio CKO over WT 3.22 | `files/fulltext/PMID41715204_Sun2026_supplement/Table3_myelin_proteins_derivation.txt` (aggregate derivation of the deposited proteomics spreadsheet)
