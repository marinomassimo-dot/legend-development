# IT47 P4: new case fixed before execution (the GSK3 / eIF2B hypotheses package, INV-09 lithium)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Written and committed **before the rows of the package were read** (I had seen its column names, its folder listing and the INV-09 and INV-02 cards).

## Question and selection
Question: for the lithium thread (INV-09, need NEED-GSK3B-DEREPRESSION), does the generator, once it consumes the package's hypotheses and the cell context, give a conditional proposal and a next experiment that the earlier path did not, and are they right?
Rule fixed here, applied once: among the hypothesis packages that exist but were not used to design the P1 mapping (the mapping was built on ph_k2p_sci45 and nrf2_inv08), take the one of a different investigation and mechanism family. Candidates: the SCI43 K-branch package and the HCN package (both INV-18, the family the mapping was built beside); `gsk3_eif2b_20261107` (5 hypotheses, not in the manifest; its README names INV-02 once and its subject is GSK3 / lithium, INV-09). → **gsk3_eif2b**. It needs one manifest row (role hypotheses_only, INV-09: the subject; the choice between INV-02 and INV-09 is recorded here, Harness left it to the Orchestrator) and a mapping chosen from its column names alone, written below before any row is read.
## Inputs (digests, first 16 hex of SHA-256)
`gsk3_eif2b_20261107/output/hypotheses.tsv` 1337829b98967eb3; `ranking_it8_p9_20261029/investigations_it20.tsv` 53fd3b32a4b9e438; `generation_it46_20261111/ladder_it46.tsv` 235821cd1b7a2d37; `generation_it46_20261111/cell_context_it46.tsv` 1d71ea6aa37f5b3d.
## Mapping (from the column names alone)
columns: hyp_id, statement_IPOTESI, compound_or_tool, documented_action_on_the_node, tool_or_candidate, context, benefit_if_true, refuted_or_replaced_by, requires_first, source_rows.
observation and source ← benefit_if_true is **not** an observation; the package has no observation cell → "not stated by the package" with source_rows; relation ← statement_IPOTESI; context ← context; action ← documented_action_on_the_node (+ compound_or_tool kept apart, named not ranked; tool_or_candidate states which); unresolved premise ← requires_first; competing explanations ← refuted_or_replaced_by plus the other rows; discriminating measure ← requires_first; expected result ← benefit_if_true. Direction: none stated unless the package says so.
## Arms (same data for each)
1. **Simple target search:** the catalogue's curated mechanism rows for GSK3B and GSK3A (and IMPA1, IMPA2, EIF2B1-5 if the package names them).
2. **Previous path:** what the generator and the INV-09 card gave before IT47 for this thread (no conditional proposal row; the card's next test).
3. **New path:** the package rows consumed with the mapping above, the cell-class context join, and the ladder.
## Expected difference (before the rows are read)
(a) five conditional rows with a stated premise and measure; (b) the new path adds at least one `requires_first` item that the INV-09 card does not carry; (c) the context join adds **nothing** (GSK3B, IMPA1/2 and EIF2B* are in no held cell-class table); (d) no compound is nominated and no direction is asserted.
## Outcomes that count as no value
The package rows add no premise or measure beyond the INV-09 card; the mapping reads a cell wrongly (a wrong link); the independent reader finds a decisive proposition unsupported and the new path carried it; the new path changes no next experiment.
## Independent reference
Not the engine's labels. A blind reader (sonnet, high; no recursion), with access to the originals, receives the decisive propositions of the package (the documented action of each tool on its node, the stated context, the "requires first" items) **without** my conclusions and returns SUPPORTED / UNSUPPORTED / PARTLY / NOT_REACHED with locators. The catalogue `modality` field is the reference for the roles of the named tools (agree / disagree / NO_REFERENCE). A known compound recovered retrospectively shows coverage; a new combination in the repository shows no novelty against the literature; neither shows predictive capacity.
## Measures
useful conditional proposals (by the reader); wrong links; premises made explicit; change of the next experiment (text difference against the card); observable cost and time.
