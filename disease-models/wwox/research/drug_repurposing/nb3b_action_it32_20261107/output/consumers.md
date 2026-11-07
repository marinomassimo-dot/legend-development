# Consumers: what a change of premise touches (NB-3b). No shared file was edited.

Non-canonical, not medical advice. Ids are named as found in the files read; proposals are suggestions for the Orchestrator.

| Id | What touches it | Proposed change (not applied) |
|---|---|---|
| INV-16 (`ranking_it8_p9_20261029/investigations_it20.tsv`, fields next_test and decisive_uncertainty) | Controls: H3 acetylation is not an engagement readout for a class IIa enzyme; HDAC6 inhibitor is a chemotype control; class-I-only "same effect" is ambiguous; no engagement control; no second knockdown reagent; evidence_available says the one drug in the muscle paper was "reported for GLUT4 only" (the abstract is silent on GLUT1 for the drug arm) | Reword the two fields as in `controls.tsv`; add the engagement and catalytic gain-of-function arms and the HIF readout as hypothesised, not as premises |
| WO-30 (HDAC5 to SLC2A1 premise measurement, cited by INV-16) | Order of arms: step 1 knockdown with SLC2A1 protein, uptake and transcript, then rescue, then engagement, then compound | Insert the engagement step before any compound arm |
| WO-29 (potency papers, data access blocked) | The catalogue "inhibitor at HDAC5" rows are family-level, so they cannot stand in for isoform potency | Note the family-level source of the 12 rows |
| CH-IT28-HDAC5-LEVER | Verdict NARROWED is unchanged; the edge-origin line gains the sign conflict with HDAC4 papers and the abstract-level silence on GLUT1 for the drug arm | Add as a carried limit, not a veto |
| IT21P2-0006 and the 20 HDAC5 and 10 HDAC3 proposals with a carried limit (IT29 S10 `carried_limits`) | Edge basis "HDAC5 -> SLC2A1 (+)" has one muscle origin and an opposite-sign paralog literature; compounds read as class I for pracinostat-type chains | Add one clause about sign conflict; mind the 1,600-character cap |
| INV-07 (PDH axis) and NEED-PDH-PYRUVATE-AXIS | Direction of SLC2A1 is unresolved and transcript-level only; no change to its rank | None; cite the R3 list |
| INV-06 (pro-myelinating class) | No change; the HDAC3 case (R5) confirms the class-I counter-premise stays conditional | None |
| CH-IT29-CLASSIIA-CNS-MYELIN | Unchanged by this package | None |
| nb3 package (`nb3_class_iia_it32_20261107/output/README.md`) | Items 6 and 7 stand; the engagement control is an addition to item 7 | Cross-reference only |
| catalogue (`catalog/`) and `repurposing_search.py` output for HDAC5 | Family-level mechanism rows are shown as HDAC5 actions; compound X (CHEMBL3110004) absent | A display note that the target is a protein family; adding a molecule is a catalogue change for the Orchestrator |

Reopening: a neural SLC2A1 readout after HDAC5 knockdown, or a full text of PMID 22991226, would change INV-16 evidence text, WO-30 and the edge-origin line above.
