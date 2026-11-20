# ADV-095 unit A3 pre-registration, frozen before any per-cell-type value of this analysis is opened: is the replicated activity-regulated transcript deficit neuron-specific, and does it track the oligodendrocyte-lineage deficit across contrasts? (SCI, 2026-11-19; hypothesis level; held data only; no dose, no recommendation; reference genotype class only; not medical advice)

## Question
Unit A's unbiased replicated list put activity-regulated and immediate-early transcripts lower in the knockout in both the human organoid and the mouse cortex after adjustment (EGR1, FOS, KLF2 among the leaders), and per-animal in the cortex the mature-oligodendrocyte score followed the immediate-early panel (rank correlation 0.89, genotype-confounded). ADV authorised a branch: the myelin deficit as a non-cell-autonomous consequence of lower neuronal activity-dependent signalling, with a neuronal activity-dependent pharmacological route as a broad alternative to the oligodendrocyte class. This pre-registered step is its first and cheapest test, and it carries ADV's stop rule.

## Data (held)
* **Nuclei** (GSE158684, P17 hippocampus, one pool per arm; nuclei are not replicates; no p-value; descriptive): per-nucleus log2(CPM+1) of an activity panel, per cell class.
* **Bulk per animal** (GSE158682 cortex 3 v 4; GSE158681 hippocampus S 3 v 2, N 2 v 2, null 2 v 3) and **organoid** (GSE156243): the same panel, raw shift R and stage-adjusted shift A1 (unit A method), as the second deposit.

## Registered panels (mouse symbols; human by upper case; fixed now; not taken from these data)
ACT (immediate-early and activity-regulated): Fos, Fosb, Npas4, Arc, Egr1, Egr2, Egr4, Junb, Nr4a1, Bdnf, Btg2, Dusp1 (the ADV-070 panel, unchanged). NEURON_CTRL (neuronal reference not expected to be activity-regulated): Snap25, Rbfox3, Syt1, Stmn2, Tubb3, Map2. Cell classes in nuclei and their markers as registered in unit A2 (excitatory Slc17a7, Camk2a, Satb2; inhibitory Gad1, Gad2, Slc32a1; astrocyte Aqp4, Aldh1l1, Slc1a2; microglia Cx3cr1, P2ry12, Csf1r; the five lineage stages as in A2), assignment by the largest class score divided by its 99th percentile, unassigned below 0.2 (uncalibrated; the same procedure and thresholds as A2, so the classes are the same nuclei).

## Quantities
1. **Per class, per arm:** mean per-nucleus ACT score (mean of log2(CPM+1) over the panel genes detected in that class), number of nuclei, and the knockout minus control difference; the same for NEURON_CTRL as a reference for global per-nucleus depth effects.
2. **Neuron specificity reading:** the ACT difference in the excitatory class, the inhibitory class, and the glial classes (astrocyte, microglia, OPC, mature lineage) separately, with the NEURON_CTRL difference as a depth control.
3. **Second deposit:** ACT R and A1 per bulk contrast and in the organoid (stage-adjusted exactly as in unit A; cortex leave-one-animal-out; hippocampal and organoid rows descriptive).
4. **Across-contrast coupling (descriptive, four mouse contrasts):** the ACT shift against the mature-oligodendrocyte (M3a) shift, raw and adjusted, with the organoid ACT shift shown beside (the organoid has no oligodendrocyte lineage).

## Rules and stop rule (ADV's, fixed now; thresholds not calibrated)
* **Neuron-specific** if the excitatory-class ACT difference is at most -0.3 and the mean of the glial classes (astrocyte, microglia, OPC) is above -0.15, with the NEURON_CTRL difference in the excitatory class within 0.2 of zero. **Global** (not neuron-specific; read as a sampling-state, time-of-death, handling or depth effect) if the glial classes are also at most -0.3 or the NEURON_CTRL difference moves similarly. Otherwise **undecided**.
* **Replicated in a second deposit after adjustment** if ACT A1 is at most -0.3 in the cortex with every leave-one-animal-out fit negative **and** in the organoid with the same sign.
* **STOP THE BRANCH** (ADV) if the deficit is not neuron-specific in the nuclei, or is not replicated in the second deposit after adjustment, or no agent class has target, exposure and endpoint data after one round. The first two are decided here; the third by a later round only if the first two pass.
* If both pass, the next step is one delegate round on neuronal-activity classes (TrkB agonists, neuregulin-ERBB4 modulators, AMPA-receptor potentiators) with the same fields as the oligodendrocyte-class unit; if either fails, the branch is closed with its reason and nothing is run.

## Alternative explanations carried to the result (each with what would speak for it)
Sampling state or time of death (the whole panel moves in every cell type, including glia and the depth control); seizure history or sedation at sampling (the panel lower in neurons but unrelated to the stage and oligodendrocyte genes across animals); dissection or regional carry-over (follows the choroid and regional panel across animals); a shared stage effect (the late-stage covariate explains the panel shift after adjustment); ambient RNA (the glial classes carry the same panel at the level expected from the neuronal pool).

## What this cannot show
Causation between neuronal activity and oligodendrocyte maturation; whether the panel reflects activity or tissue state; protein, electrical activity or myelin ultrastructure; independence beyond one origin per species; any pharmacological effect.

## Decision it changes (stated before the run)
Pass: the neuronal-activity route is opened as a second broad pharmacological route beside the oligodendrocyte class, with a one-round agent evidence unit. Fail: the branch is closed and the oligodendrocyte-class unit remains the only broad route under test, with the non-cell-autonomy reading kept as an explanation without a route.
