# Note for INV-15: what the glial Wwox signal changes, and what it does not

Non-canonical, not medical advice. Written by the pilot Orchestrator after the independent audit (`verify/audit_nb4.md`). Reference genotype class only. Nothing in a shared consumer was changed; this is the text the integrator may use.

**What changes.**
1. Wording. Write the deletion as "neuron-targeted by design (Synapsin-Cre), with a lower Wwox transcript also in glia-annotated nuclei of one pool". Do not write "neuron-restricted" (not established at transcript level, not refuted) and do not write "glial loss" (no cell count was measured; a lower transcript is not fewer cells, less protein or less activity).
2. The glial fall is a reading with several non-exclusive contributors: lower transcript in the annotated class (shown, one pool), class definition and detectability, ambient RNA (a minor share of the control signal on p1b's assumed soup fractions), recombination beyond the expected cells (open), change of state or composition (compatible). `explanations.tsv` holds the table; none is isolated by these data.
3. New for the premise itself: a later direct characterisation of the Cre line (PMID 35966957, read by the auditor, secondary description) reports reporter in about a third of neurons, so the neuronal deletion may be mosaic, and the fraction in parvalbumin cells is not known from any source read. The depth is the auditor's, no receipt is staged. A per-animal PV measurement must therefore carry its own recombination read-out (tdTomato or genotype in the PV cells), beside cell number, identity and maturation.
4. The pooled Pvalb transcript cannot be assigned to cell-autonomous loss in PV cells from this deposit; this was already INV-15's premise and is unchanged.

**What stays the same.** One pool per arm, no library or animal index, paper n = 1 per arm; nuclei are not replicates; raw reads still `hup` (re-checked 2026-11-07, one query); the nucleus-level route stays closed; INV-15 remains a per-animal measurement; rank is not changed by this note.

**Next step justified (one, bounded, zero spend).** Open the held supplement figures that the paper cites for the recombination check (Supplementary Fig 1C-D) and look for any tdTomato panel; so far only legends were read. If a panel shows reporter in astrocytes or oligodendrocyte-lineage cells, reading (d) gains support; if it does not, (d) stays open, not excluded.

**Not justified.** Re-clustering, re-annotation or rule variants on the same two matrices; glial differential expression with nuclei as replicates; any statement of a PV-interneuron defect; any drug inference. Re-query the eight SRX at each session (cheap) and test barcode overlap only if reads appear.

**Open and not run in the pilot.** The GLT-1 neuronal-deletion paper (PMID 25834045) as a counter-row for (d); full text of PMID 16419044, 11297510 and 35966957; glia-restricted Cre lines in the same paper.
