# IT44 independent reader: S11 premises (brief)

You are an independent reader (sonnet, high effort, one delegate, no sub-delegation). You do NOT see the search engine's verdicts and must not look for them: do not read `s11/`, `pointers_it44.tsv`, `summary_it44.tsv`, `entity_roles_it44.tsv`, `relation_s11_frame_it44.md` or any search_rows/molecules/verdict file. Work from primary sources (PubMed tools, PMC when reachable) and the public ChEMBL REST activity endpoint for the two ids named below.
Rules: zero spend; do not send, search for or store any e-mail address or contact detail; no service that asks for a contact address. Not medical advice. Write only `generation_it44_20261110/verify_s11/VERDICTS.md`. Quote the words you rely on; say NOT_REACHED when a source is not reached (unknown is not negative). Keep under 200 lines; report your tool-call count.

Context (one paragraph, no verdicts): a juvenile cortical neuron has a higher input resistance in a mutant; one hypothesis is a lost resting K+ conductance that is sensitive to extracellular Ba2+, assumed to be carried by Kir2-type or K2P-type channels.

## Questions
1. **Ba2+ sensitivity of K2P channels.** For TREK-1 (KCNK2), TREK-2 (KCNK10), TRAAK (KCNK4), TASK-1 (KCNK3), TASK-3 (KCNK9), TWIK-1 (KCNK1) and THIK-1 (KCNK13): is the current blocked by extracellular Ba2+ at 50-200 micromolar? Give the reported block (percent or IC50), concentration, system and PMID for each channel you can reach. State clearly where a source says "insensitive".
2. **Kir2 activators.** Is there a published small-molecule activator (opener) of Kir2.1, Kir2.2 or Kir2.3 (KCNJ2, KCNJ12, KCNJ4)? Name each with its source and what it was measured on. If none is reached, say what you searched.
3. **Riluzole on K2P.** Evidence that riluzole activates TREK-1 and TRAAK (EC50 or percent, system, PMID); its other documented actions on neuronal targets (e.g. sodium channels, glutamate release) and at what concentrations relative to the K2P effect.
4. **BL-1249 and fenamates.** What is BL-1249's reported target selectivity among K2P and other K channels; is flufenamic acid itself reported to activate TREK channels (EC50, source)?
5. **Two ChEMBL activity rows.** Using the public ChEMBL REST activity endpoint, read the activity record(s) of molecule CHEMBL744 (riluzole) on target CHEMBL1914276 and of CHEMBL23588 (flufenamic acid) on the same target: report standard_type, value, units, assay_type, assay organism, assay description and document; say whether the record establishes activation, inhibition or neither.
6. **Any other published K2P or Kir activator** that a source describes as acting in cortical pyramidal neurons (slice or culture), with the effect on input resistance or resting potential if reported.

## Output
`VERDICTS.md`: one table per question, each cell with SUPPORTED / CORRECTED / NOT_REACHED and the quoted words; then a ranked list of what an investigator proposing "add a Ba2+-sensitive resting K+ conductance with an opener" most needs to know.
