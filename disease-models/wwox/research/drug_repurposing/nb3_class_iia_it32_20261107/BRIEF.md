# Brief NB-3: class IIa HDACs in neural and glial cells, catalytic versus scaffold function, and the myelin literature (IT32 P4)

Read `../batch_sci_20261105/BRIEF_COMMON.md` first; it binds (open routes only, no e-mail address or contact to any service, no administered-dose numbers, depth honesty, write only in your folder, stage receipts and never record them, wording rules). `framework/protocols/delegation_budget.md` sections 2 and 7 bind you: you start no agents. Before opening any PMID check its depth in the receipt ledger (`framework/scripts/fulltext_receipts.py`); do not reread a source already read beyond abstract unless you need a named new detail. A verifier will receive only your (statement, source, locator) triples.

**Question.** (A) In neural or glial cells, is there a primary source that separates the deacetylase (catalytic) activity of a class IIa HDAC (HDAC4, HDAC5, HDAC7, HDAC9) from its scaffold, corepressor-binding or nucleocytoplasmic-shuttling function, for example with a catalytic-dead rescue, a catalytic-site mutant or a class IIa-selective inhibitor compared with knockdown? (B) Re-run the bounded search of challenge CH-IT29-CLASSIIA-CNS-MYELIN with a working PubMed route: is there a neuron-route or axon-route paper linking a class IIa HDAC to myelination or oligodendrocyte differentiation?

**Decision it can change.** Investigation INV-16 asks whether catalytic inhibition of HDAC5 reproduces HDAC5 knockdown at SLC2A1 in human neural cells; reduction of the amount of a protein is not inhibition of its catalytic activity. Answer (A) says which INV-16 step (knockdown, catalytic-dead rescue, inhibitor) already has a precedent and in which cell type, and so which step should be run first. Answer (B) turns "nothing found, count unverified" into a verified bounded null or a lead for the counter-premise on the myelin endpoint.

**Alternatives to keep open.** Catalytic and scaffold functions both matter; scaffold function dominates; the answer depends on cell type or substrate; no neural source exists. Do not choose among them in advance.

**Discriminating result sought.** A source with a catalytic-dead or catalytic-site mutant (or a selective inhibitor beside a knockdown) in a neuron, astrocyte, microglia or oligodendrocyte-lineage cell reading a transcriptional or metabolic output; for (B) the verified count of hits for the written query list and the first neuron-route paper if one exists.

**Scope and discipline.** Write the query list in `queries.tsv` BEFORE reading hits. Other genes (HDAC4, HDAC7, HDAC9) and other tissues (muscle, heart) are allowed as method precedents; their origin stays in the row and nothing is read as a direction for WWOX. "Not found in the routes searched" is reported as that, never as "does not exist". At most 10 sources beyond what the module holds; stop when answered or exhausted. Seizure control, development, network function, myelin and quality of life stay apart. No compound is promoted.

**Deliverables in `nb3_class_iia_it32_20261107/output/`:** `README.md` (answer first, at most one page, every statement DATO / INFERENZA / IPOTESI), `evidence.tsv` (row_id, paper_pmid, quantity_or_claim, cell_type_and_species, locator_quote_max25words, source_depth, bears_on (A or B), note), `queries.tsv`, `receipts/` with staged receipts (suffix `32`) and `INDEX.tsv`.

**Consumers expected.** INV-16 (`ranking_it8_p9_20261029/investigations_it20.tsv`: evidence, uncertainty and next-test sentences); open_questions_map rows WO-30 and WO-32; the challenge CH-IT29-CLASSIIA-CNS-MYELIN residue.

Final message: what you completed, what you could not reach, and the setting you ran under as you can see it.
