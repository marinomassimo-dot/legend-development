# IT32 P12-2: a small relation extract in the style of GO-CAM, tried on INV-16

Non-canonical. Not medical advice. Method precedent: arXiv:2608.27675 (biocuration with agents); it is not WWOX evidence and not a validation of a predictive method. This is an extract **inspired by** GO-CAM (activities, participants, context, evidence-backed relations). It is **not** a GO-CAM-conformant model and is not called one: no relation uses a verified Relation Ontology term, there is no graph store, and nothing here was checked against the GO-CAM schema.

## Question and frozen input
Does a representation that separates the biological action needed from the generic compound-target association change a proposal or the next experiment for INV-16? Input frozen at the NB-3 and NB-3b packages (`../nb3_class_iia_it32_20261107/`, `../nb3b_action_it32_20261107/`, both blind-audited and corrected) and the current INV-16 row. Decision to test: which INV-16 arm is run first and whether any compound is proposed.

## What was built
`relations.tsv`: 11 relations, each with subject kind (protein amount, catalytic activity, localisation, compound, genotype), the perturbation, the endpoint, the system, a status (observed / transferred / unknown), a source and a locator (row ids of the audited tables). Three are observed in a mammalian neural or neural-like system (R04, R05, R08) but none reads SLC2A1; the SLC2A1 relations are muscle (observed), WWOX-deficient systems (observed, in disagreement) and the HDAC5-to-SLC2A1 neural step (unknown). Nothing was inferred beyond the audited rows.

GO identifiers were resolved on 2026-11-07 against QuickGO (official EBI service), not from memory: GO:0141221, GO:0004407, GO:0005634, GO:1904659 exist and are current. The check caught a wrong recollection: GO:0046323 (D-glucose import), which I would have used, is obsolete. Existence and adequacy are separate: applying `histone deacetylase activity` to HDAC5 asserts an activity that the primary source on class IIa enzymes questions (R04, R07); the term is recorded as existing and of limited adequacy.

## Comparison with the current representation
* Ambiguity removed? The distinction between amount, catalytic activity and localisation was **already** carried by `chain.tsv` (column target_function) and by INV-16 after NB-3b. The extract adds no new separation. It adds one thing: forcing a term for each activity exposed that the natural ontology label for HDAC5 imports an enzymatic claim that class IIa evidence weakens.
* Action compatible, incompatible, indeterminate? Catalytic dependence is compatible (R04, rat neurons, other output), not shown for SLC2A1 (R09 unknown), contradicted for a paralog and an output (R06), and its readout by an inhibitor is indeterminate (R08).
* Proposal or experiment changed? No. The arm order and the engagement control were set by the audited reading (INV-16 already says so). No compound is proposed or promoted.
* Where did the advantage come from? From the reading (NB-3, NB-3b and their audits), not from the representation. The table makes the per-relation system, perturbation and endpoint queryable (for example, "no observed relation reads SLC2A1 in a neural cell") but the existing tables answer the same question.

## Outcome
No advantage in decisions; one small checking benefit (identifier resolution caught an obsolete term). A second case was not run: the brief makes it conditional on an advantage. **Not adopted:** no dependency, no GO-CAM tooling, no ontology service beyond a one-off public lookup. OLS, LinkML and AI4Curation stay candidates for a named missing function; none was needed. Reopening: a task that needs relation-level queries across many cases (for example "all observed relations in a neural system for target X") would justify trying the extract on several cards.
