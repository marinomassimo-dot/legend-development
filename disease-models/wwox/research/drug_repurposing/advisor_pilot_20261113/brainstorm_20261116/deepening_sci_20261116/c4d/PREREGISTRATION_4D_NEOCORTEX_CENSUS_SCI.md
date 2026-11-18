# Candidate [4d]: a single-nucleus or sorted-nuclei reference from the BURSTING region (neocortex): selection rule and readout, written and hashed BEFORE any search result or series metadata was read (SCI, 2026-11-17 02:5xZ; non-canonical; hypothesis level; not medical advice)

**Unit and region (first line):** the target is rodent NEOCORTEX, single-nucleus or single-cell or sorted-nuclei RNA-seq; unit = the nucleus (or the sorted-sample if only sorted fractions exist); the n of animals is recorded for every series from its metadata.
Why: [4b] and [4c] are S-line hippocampus at P17, a region that does not burst in slices; the bursting region (neocortex) has no single-nucleus table held. The census answers whether a per-neuron reading exists there.

## Selection rule (applied to series metadata only, in this order)
A series qualifies if ALL hold, read from title, summary, overall design, sample table, platform:
1. Mouse or rat; tissue neocortex (cortex, prefrontal, somatosensory, motor, frontal; not hippocampus, not whole brain); a sequencing-based single-nucleus, single-cell or sorted-nuclei RNA-seq with a count matrix or per-sample counts downloadable by FTP or E-utilities (no interactive challenge route; if only an interactive page serves it, the series is PARKED with the trigger 'a route without a challenge').
2. A contrast with controls in the same series (genotype, treatment or time point).
3. Priority of the model, strictly in this order: (i) a Wwox-deficient model (null, conditional, P47T or other); (ii) otherwise a model with a documented spontaneous or evoked seizure or bursting phenotype in the neocortex (a genetic epilepsy line or a chemical or kindling model) at a postnatal age stated in the metadata; (iii) otherwise nothing qualifies and the census reports 'none'.
4. Within a priority class: the age closest to P17 (for chronic adult models, the stated chronic stage of at least 21 days), then the larger number of animals per group, then the earlier accession.
The number of animals per group is read from the metadata (sample table) and stated; if the metadata do not allow it, the series is reported with 'animals per group not stated'.

## Readout if a series qualifies (fixed now; predictions registered before any count file is opened, in a second file with its digest)
The classification of [4b] (marker-set argmax, same sets); excitatory-neuron nuclei; Gabrd, Slc12a2, Scn1a (inhibitory nuclei), Gabrg2, Wwox (if the model is Wwox-deficient): log2 fold of the contrast over control, bootstrap over nuclei (pseudo-replicated unless animal identity is recoverable from barcode suffixes or sample columns, in which case a per-animal pseudobulk 95% bootstrap is also given); readable if at least 30 nuclei of the class express the gene in each group. No significance is claimed. If the best qualifying series is a seizure model (priority ii), its result is a CONSEQUENCE reference for neocortex, not a Wwox statement.
## Limits
Metadata-level census; absence by one search route is not absence (a second route is run: a different query family and the geo series of the Wwox GEO accessions already known to the repository); the ranking is by metadata only.
