# IT9 P4b group B: decision criteria (written 2026-10-30 after the raw acquisition ran but BEFORE any of its rows was read)

Scientist-b3. The acquisition script `qualify_p4b_b.py run` had completed (117 attempts; only the file `raw_store.json.gz` and the logs existed); no row, label text, trial hit or expression value had been opened when this file was written. Not medical advice.

Decision classes (per candidate): DROP (decisive datum named), KEEP-AS-PROPOSAL (next experiment, readout, control, falsifier), REFERENCE-ONLY, INCONCLUSIVE (exact missing datum).

* DROP requires at least one of: (a) the identity or target mapping behind the proposal fails on inspection (the compound does not act on the proposing target); (b) the edge that produced the proposal is not a record in neural-relevant, non-text-mined evidence AND the target is not expressed in the relevant neural cell types; (c) a labelled boxed warning or exposure fact that excludes use in the intended population without a stated route round it (for a proposal that is not a reference).
* KEEP-AS-PROPOSAL requires all of: the compound acts on the proposing target with at least one measured value of assay type B (binding or functional) in ChEMBL with a stated species; the proposing edge has a curated or experimentally referenced record (not only text-mined) OR the target is a direct enzyme/receptor of the compound; the target gene is detected in a brain cell type in HPA (nCPM or nTPM at least 1); and a discriminating readout in a WWOX-deficient system is definable.
* REFERENCE-ONLY: compound already carded or named as a control; the edge is not the reason it is kept.
* INCONCLUSIVE: a datum that could change the class is absent (not negative), and the missing datum is named.
* Edge plausibility is graded: CURATED_PHYSICAL (SIGNOR causal statement with references), TEXT_MINED_TF (ExTRI/CollecTRI-only), AGGREGATE_TF (TRRUST/DoRothEA with references), and CONTEXT_FREE flagged when the records carry no cell/tissue qualifier; the OmniPath record carries no tissue, so context is judged from the references' abstracts or from the expression of the pair in HPA, with depth stated.
* Biological promise, depth of evidence, feasibility and priority are four separate fields and are not combined.
* A trial registry hit is a count of registered studies, never a result. Absent data, service error and negative result are written as three states.
