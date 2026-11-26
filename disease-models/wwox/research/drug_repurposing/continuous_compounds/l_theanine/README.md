# L-theanine checkpoint in WWOX loss of function

**Data scope.** P17 mouse Wwox neuronal-deletion cortex and hippocampus TPM, week-15 human WWOX-knockout cerebral organoid library CPM, and P17 mouse hippocampal pooled cell-class UMI CPM. [Fixed prediction](pretest_20261126.md)

**Opening result.** SLC38A1 falls in all three bulk models, reproducing the earlier glutamine result. SLC7A5 falls in cortex (50.22→44.85 TPM) and cerebral organoids (346.24→191.04 CPM) but rises in hippocampus (35.60→42.67 TPM). SLC7A8 rises in cortex and organoids and has an unstable hippocampal direction under omission. These regional and isoform distinctions argue for measuring the actual free compound and precursor transport before assigning the response to one transporter. They do not identify transport across the blood–brain barrier. [Bulk contrasts](bulk.tsv) · [Assigned pooled counts](nuclei.tsv)

**Disposition.** Park for unselected pediatric WWOX trial priority. The nominal rat glutamine-uptake IC₅₀ is 3.59 times the highest mean serum peak in the adult studies checked. The published mouse seizure provocations move in opposing directions, and the pediatric ADHD trial supplies exploratory actigraphy evidence. Reopen for measured free neural exposure and a selective post-activity inhibitory recovery that preserves excitatory output and constrains late recruitment. [Exposure, counterexamples and test](exposure_and_disposition_20261126.md) · [Earlier glutamine physiology](../l_glutamine/README.md)

**Replay.** Run `python3 -B replay_expression.py HELD_INPUT_DIRECTORY OUTPUT_DIRECTORY`. [Held source identifiers and hashes](../creatine/inputs.tsv)
