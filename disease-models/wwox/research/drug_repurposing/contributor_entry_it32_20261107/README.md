# Contributor entry point: replicate structure of public Wwox neuron-deletion datasets (investigation INV-15)

Anyone can do this from public pages; no repository knowledge beyond this file is needed. Not medical advice. Do not contact authors or data holders on behalf of LEGEND and do not send any personal address to any service.

**Open question (investigation INV-15, `../ranking_it8_p9_20261029/investigations_it20.tsv`).** In the neuron-targeted Wwox-deletion mouse the Pvalb transcript is lower. Is that fewer parvalbumin cells, immature identity, lower marker expression, changed intrinsic properties, changed synaptic input, or a circuit change? The first thing that limits every answer is the replicate structure: with one animal or pool per arm, nuclei are not biological replicates and several records of one series are not independent experiments.

**Task (zero spend, public sources only).** For each public expression series that contains Wwox-deleted or Wwox-knockout neural tissue (start with the accessions named in `../snrna_it13b_pv_20261031/README.md` and `../gse158684_identity_it14_p1a_20261101/README.md`, then GEO and ArrayExpress searches for Wwox neuron or interneuron deletion), fill one row of a TSV: `accession, tissue, genotype_arms, animals_per_arm_stated (number or NOT_STATED), pooled_libraries (yes/no/NOT_STATED), library_or_animal_index_in_metadata (yes/no), assay (bulk/snRNA/other), where_stated (page and sentence, at most 25 words), independent_biological_replicates (yes/no/UNDECIDABLE), note`.

**What counts as an answer, a limit and an error.** Answer: a row whose `where_stated` quotes the deposit or the paper. Limit: `NOT_STATED` or `UNDECIDABLE` with the place you looked; this is a result, not a failure. Error: inferring the number of animals from the number of records, or marking replicates independent because the records are separate.

**Data and licences.** Read the series pages and papers; do not upload third-party raw files. Quote at most 25 words per cell and give the source link. Your own table is yours to licence; if you want it used in this repository say so in the pull request.

**What LEGEND will do with it.** The table replaces the free-text replicate statements behind INV-15 and decides whether any public series can support a per-animal analysis (`IT14 P1a/P1b` tables). No claim about fewer cells or lower activity follows from it; only the replicate structure does.

**Check.** There is no automated check for the table; a reviewer opens each quoted sentence at its source.
