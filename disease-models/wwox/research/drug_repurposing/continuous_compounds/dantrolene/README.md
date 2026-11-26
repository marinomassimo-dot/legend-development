# Dantrolene sodium · ER calcium release and mitochondrial recovery

26 November 2026 · SCI_CODEX · opening checkpoint · P17 mouse cortical/hippocampal RNA and week-15 human organoids, with pooled P17 hippocampal nuclear UMI counts

WWOX-deficient neural preparations show broad circuit hyperexcitability. A possible contributor is enhanced amplification from endoplasmic-reticulum (ER) calcium stores. The opposing hypothesis is poor physiological delivery of calcium to mitochondria and impaired energy recovery during firing. Dantrolene is a way to test that difference if the active channel and free exposure are relevant. The program expands to an ER-release mechanism after the carbohydrate compounds. No other compound is active. [Prespecified comparison](pretest_20261126.md) · [Human organoid study, primary abstract](https://pubmed.ncbi.nlm.nih.gov/34268881/) · [D-galactose disposition](../d_galactose/transport_and_assay_scope_20261126.md)

## Cross-model countercheck

Values are KO minus control in mean log₂(1 + abundance). The mouse estimates use gene-summed transcript TPM and the human estimates use per-million processed counts. Bulk samples are cortex **4 control/3 KO**, hippocampus **2/3**, and week-15 organoids **2/4**. Mouse cortex and hippocampus are Wwox neuronal-deletion cohorts. The human organoid libraries include shared lines. [All 30 contrasts and omission checks](contrasts.tsv) · [Held source file fingerprints](../d_mannose/inputs.tsv)

| RNA | P17 mouse cortex | P17 mouse hippocampus | Week-15 human organoids |
|---|---:|---:|---:|
| RYR1 | −0.24 | −0.14 | +0.85 |
| RYR2 | −0.38 | −0.27 | +0.19 |
| RYR3 | +1.05 | −2.59 | +0.32 |
| ITPR1 | −1.25 | −1.24 | +0.28 |
| ATP2A2 | −0.58 | +0.03 | +0.56 |
| MICU2 | −0.71 | −0.38 | −0.29 |

MICU2 is the only target with the same sign across all bulk estimates and every one-library omission. The mouse cortical RYR3 estimate is sensitive to one library (omission range **−0.04 to +1.93**). The hippocampal bulk decrease is stable (**−3.03 to −2.15**). In a separate pooled hippocampal dataset, RYR3 CPM rises in assigned excitatory (**893 → 1,071**), inhibitory (**185 → 249**) and astrocytic (**266 → 441**) nuclei. MICU2 rises by a small amount when all classified nuclei are pooled (**62.37 → 63.74 CPM**), with an inhibitory decline and an excitatory rise. None of the bulk estimates establishes a shared response of the respective protein or channel.

Across all nine assigned nuclear classes, RYR3 rises **677.17 → 808.69 CPM**. The symmetric decomposition of the **+131.52 CPM** difference assigns **+157.00 CPM** to within-class differences and **−25.48 CPM** to weights of RNA contributed by each class. The total RYR3 increase survives every single-class omission (**+116.17 to +154.51 CPM**). This sign reversal against bulk cannot be explained by simply removing one assigned class within the nuclear data. The measurements come from different preparations and denominators, with only one nuclear pool per genotype. Technical recovery, cell assignment and isoform-specific RNA abundance could contribute. [Nuclear counts](nuclei.tsv) · [Decomposition and omissions](composition.tsv) · [GSE158681](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) · [GSE158684](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684)

## Discriminating outcome

Compare ER filling, late ER release and mitochondrial calcium and ATP recovery in matched WWOX-deficient and corrected neural cultures at the same evoked electrical drive. An excessive-release mechanism predicts that dantrolene preferentially removes pathological late events **while preserving** the mitochondrial calcium response, ATP recovery and physiological recruitment. Under an insufficient-transfer mechanism, a smaller cytosolic event comes with weaker mitochondrial calcium or ATP recovery. Broad reduction in excitation and inhibitory recruitment favors generic suppression. The RNA pattern prioritizes direct compartment measurements over fixing an isoform in advance.

A primary molecular study found different dantrolene effects in RyR1, RyR2 and RyR3 systems, dependent in part on conditions. A separate striatal-neuron paper reported reduced mitochondrial calcium uptake with dantrolene in a permeabilized preparation. This is a genuine counterhypothesis to assuming that smaller cytosolic transients will improve mitochondrial energetics. It needs testing under intact neuronal activity and the relevant exposure, with an independently verified perturbation of the suspected release channel. [Isoform work, primary abstract](https://pubmed.ncbi.nlm.nih.gov/11278295/) · [Striatal-neuron uptake, primary abstract](https://pubmed.ncbi.nlm.nih.gov/24861510/)

## Pediatric boundary and next step

The current US oral dantrolene sodium capsule label has a boxed hepatotoxicity warning. Weakness and somnolence matter to a study of a developmental encephalopathy. Concomitant sedating medicines can confound circuit and behavioral readouts. Long-term safety below age five is unestablished in that label. A mouse distribution study reports brain tissue exposure after oral and intranasal delivery. That measurement alone leaves free neuronal and pediatric chronic exposure unresolved. Research status is exploratory, with no basis here to prioritize a pediatric WWOX trial. [DailyMed oral label](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=57b4eec1-49e1-432c-95ae-0fe36e32d64b) · [Mouse distribution, primary abstract](https://pubmed.ncbi.nlm.nih.gov/32160210/)

**Active.** Next compare free-exposure plausibility with the original native-neuron mitochondrial and cytosolic readouts. Check whether reduced mitochondrial calcium follows a smaller cytosolic stimulus or persists when cytosolic delivery is matched. Consider review if endpoint direction or concentration comparability changes the experimental priority.

Replay with `python3 -B calcium_screen.py FILES OUTPUT_DIRECTORY`. The bulk, nuclei and assignment inputs are identical to the [held annotated accessions and fingerprints](../d_mannose/inputs.tsv). Nuclear class-weight effects use fractions of observed UMIs and combine both directions symmetrically without treating nuclei as animal replicates.
