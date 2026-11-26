# L-theanine opening checkpoint in WWOX loss of function

**Data scope.** P17 mouse Wwox neuronal-deletion cortex and hippocampus TPM, week-15 human WWOX-knockout cerebral organoid library CPM, and P17 mouse hippocampal pooled cell-class UMI CPM. [Fixed prediction](pretest_20261126.md)

**Opening result.** SLC38A1 falls in all three bulk models, reproducing the earlier glutamine result. SLC7A5 falls in cortex (50.22→44.85 TPM) and cerebral organoids (346.24→191.04 CPM) but rises in hippocampus (35.60→42.67 TPM). SLC7A8 rises in cortex and organoids and has an unstable hippocampal direction under omission. These regional and isoform distinctions argue for measuring the actual free compound and precursor transport before assigning the response to one transporter. They do not identify transport across the blood–brain barrier. [Bulk contrasts](bulk.tsv) · [Assigned pooled counts](nuclei.tsv)

**Next check.** Compare the original free L-theanine exposure ranges and transport effects in neurons, astrocytes and progenitors with human total and free parent kinetics where available. Separate the precursor response from pediatric sleep, actigraphy, arousal and timing. The decision remains open. [Earlier glutamine physiology](../l_glutamine/README.md)

**Replay.** Run `python3 -B replay_expression.py HELD_INPUT_DIRECTORY OUTPUT_DIRECTORY`. [Held source identifiers and hashes](../creatine/inputs.tsv)
