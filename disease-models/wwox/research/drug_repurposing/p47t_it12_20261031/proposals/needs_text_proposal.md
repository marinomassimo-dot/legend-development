# Proposal (not applied): text for `needs/needs.json` entries NEED-PDH-PYRUVATE-AXIS and NEED-LACTATE-LDH, and a note for card L01

## NEED-PDH-PYRUVATE-AXIS (`observed` / `counter_evidence`)

Add to `observed`: "P47T knock-in adult brain (GSE215425, 5 v 5 animals; IT12 P2-P47T): hallmark HYPOXIA and GLYCOLYSIS gene sets enriched in PFC, cortex and hippocampus (transcripts; carried by glycolytic enzyme genes, +0.1 to +0.6 log2 for Aldoa, Pgk1, Pfkp, Pkm, Hk2, Ldha); no HIF-selective pattern (Bhlhe40, Ndrg1 lower; Ddit4, Ankrd37, Egln3 flat); Hif1a, Epas1 transcripts flat or lower; marked heterogeneity between animals with an activity signature in two of five mutants."

Add to `counter_evidence`: "The selective hypoxia-response pattern of the human organoid (ADM, HK2, P4HA1, SLC2A1, BHLHE40, ANKRD37, EGLN3, DDIT4 up; PGK1, ALDOA, ENO1, PKM, PFKP, NDRG1 flat) is not reproduced in adult P47T forebrain or in the four P17 deletion contrasts; the glycolytic enzyme genes that are flat in the organoid are modestly higher in P47T."

`notes`: "No HIF protein, activity, lactate or oxygen-condition datum exists for any mammalian WWOX-deficient neural tissue; the P47T datum is a transcript observation in a seizing, gliotic, partial-loss brain and cannot separate a WWOX-specific HIF effect from activity or composition."

## NEED-LACTATE-LDH

Add one sentence to `observed`: "P47T forebrain: Ldha +0.4 to +0.6 log2, Ldhb -0.1 to -0.2 (IT7 readout genes, observation only; transcripts)." No change to the intervention direction.

## Card L01 (NRF2): note only, no decision change

In `functional_evidence_available`, after the sentence on the REACTIVE_OXYGEN_SPECIES_PATHWAY set, add: "Direction: enriched (positive NES; Fig 9c bar about 2.0, cerebellum, 4 v 3 animals); in the deposit the set is enriched in cerebellum only (my re-run: NES 2.1; forebrain about 1.1), with a leading edge of Prdx, Gpx, Sod1, Cat genes plus Mbp (oligodendrocyte score higher there). The NRF2 target transcripts Hmox1 and Srxn1 are modestly higher in all four regions (+0.3 to +0.7 log2), Nqo1 is mixed, Gclm and Txnrd1 flat; across animals the NRF2 target score tracks the astrocyte marker score (Spearman 0.56 to 0.88 in forebrain). A transcript set containing NRF2 targets still cannot separate raised ROS from a raised NRF2 response, and composition is not excluded." This bears on the L01 sub-question "adaptive activation versus insufficient compensation": the in-vivo partial-loss datum leans to higher NRF2-target transcripts, the organoid (NFE2L2, NQO1 lower, HMOX1, SRXN1 higher) is mixed; both remain transcripts and both composition-confounded; no change in L01 selection or priority is proposed.

## Receipts proposed (the orchestrator records them; none written here)

* FULLTEXT_READ_RECEIPT candidate for PMC10835625 (Europe PMC fullTextXML, 2026-10-31): Results 2.8, 2.9, Methods 4.14 and legends of Figs 6, 8, 9 read in full; Figures 8 and 9 viewed as images and measured; supplements read as listed in premises.tsv P4. sha256 of the XML in `raw_hashes_it12.tsv`.
* Dataset receipt candidate for GSE215425 (counts, series matrix, SOFT; sha256 in `raw_hashes_it12.tsv`).
