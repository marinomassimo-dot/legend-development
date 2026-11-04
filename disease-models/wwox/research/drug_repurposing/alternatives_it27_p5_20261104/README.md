# IT27 P5: representatives and alternatives inside four mechanism clusters (2026-11-04)

Non-canonical research material. Not medical advice. Nothing here qualifies a hypothesis; every row stays `CONDITIONAL_*` and `qualified = no`.
Read-only over code and tables (stage tables `generation_it26_a1_20261104/results_s7`, `run_generation_it21.py`). Zero spend; no contact string sent to any service. PubMed was read at abstract level only (stated per source below); the ChEMBL REST service returned HTTP 500 on 2026-11-04, so ChEMBL values come from the repository's own records and cache.
Reproduce: `LEGEND_CATALOG_CACHE=<catalog cache> python3 -I build_p5_it27.py` (calls `order_key` and `select_handoff` unchanged; asserts that it reproduces the 15 committed hand-over ids).

## Verdicts

| Cluster | Representative today | Outcome | Cap blocks a useful test? | Visible alternatives enough? |
|---|---|---|---|---|
| Q2 H_HARM **HDAC5** (12 eligible of 20) | Pracinostat | **Different representatives for different contexts or experiments.** The order picks pracinostat by a unique minimum, but the term that separates it (zmin 4.76 v 3.16 to 3.27) is a property of the family's signed target set, not potency or selectivity at HDAC5. A class IIa-selective probe (TMP269) is the only member that separates class IIa from class I inhibition; HDAC6-selective SS-208 and KA1010 are natural negative controls. All three are identity-blocked. | No (H6 uses 2 of 3 slots; H5 does not stop the experiment, whose discriminating element is the genetic HDAC5 control). The blocker is data: TMP269 identity. | Yes, if each alternative carries its class or blocker (M4) |
| Q2 H_HARM **XIAP** (3 eligible of 8) | ASTX-660 | **Tie not resolvable.** ASTX-660, xevinapant and idronoxil tie exactly on all six order terms; ASTX-660 is first by input order. Measures are IC50, Ki and Kd (not comparable) and no member is XIAP-selective (all cIAP-preferring or balanced). Idronoxil: no comparison permitted. | No | Yes |
| **EZH2** Q8 (4 eligible) and Q5 (4 eligible) | Q8 GSK2816126; Q5 none | **Tie not resolvable on exported data.** Q8: GSK2816126, tazemetostat, mevrometostat tie exactly. Potency does not separate them (IC50 9.9 v 11 nM, different documents; mevrometostat is Ki). Adds to the GSK343 qualification only in two ways: the named "second chemotype" role is open to three agents, and tazemetostat has a GtoPdb value that no family joins. | Q5: cap plus work-done demotion keep EZH2 out, but Q8 represents it and the Q5 test is specified in the GSK343 record: no useful test is blocked | Yes |
| Q5 H_HARM **ROCK2** (4 eligible of 20), contrast cluster | SAR-407899 (free base) | **Alternative preferable for a specific investigation:** belumosudil for ROCK2 v ROCK1 attribution (ROCK2 IC50 105 v 102 nM, equal; ROCK1 24,000 v 276 nM, about 230-fold v 2.7-fold). For a pan-ROCK question the two are equivalent. | No (rank 1 of Q5 H_HARM) | Partly: named, selectivity not shown |

Why ROCK2 as the fourth cluster: it is the one representative whose tied alternatives differ by two orders of magnitude in the measure the hypothesis needs (isoform attribution), at equal potency at the main target and with an engine-recorded ROCK1 contrary signal (P6 `CONFLICT_BETWEEN_TARGETS`). Higher z, more targets or more annotations played no part in it.

## (a) Reconstruction and the three-way check (documented rule, code, exported tables)

`order_key` (code) is `(cluster_work_done, seed_support_limited, UNMEASURED_AT_MAIN_TARGET, -n_origins, chain_edges, -zmin)`; `select_handoff` keeps, per (question, hypothesis, main target), the row with the smallest key (strict `<`, so the first of an exact tie) and then at most three clusters per (question, hypothesis). Per-row components: `order_key_reconstruction_it27p5.tsv`.

* HDAC5: all 12 eligible rows have k1=0, k2=1; abexinostat, panobinostat and valproic acid have k3=1 and rank last; the nine others have 1 origin, 1 edge; zmin separates them: pracinostat 4.76, then 3.27 (valproic acid, pivaloyloxymethylbutyrate, 4-phenylbutyric acid), 3.17, 3.16. Unique winner.
* XIAP: three rows, identical keys (zmin 3.38313). EZH2 Q8: four rows (three names), identical keys (zmin 3.7755). ROCK2: four rows, identical keys (zmin 4.29).
* EZH2 Q5: identical keys but k1=1 (GSK343 KEPT_CONDITIONAL, "work already done"), so the cluster ranks 10th of 11 behind unworked clusters and the cap of 3 is filled by ROCK2, PIM2, PTPRB.

**Mismatches** (`mismatch_findings_it27p5.tsv`; sensitivity in `rule_variants_it27p5.tsv`):
1. **H5 text omits three of the six terms** (k1, k2, k3); k1 and k2 are described elsewhere (H8, IT22 README), k3 only in the docstring. Dropping k1-k3 would let EZH2 Q5 in and PTPRB out.
2. **"the smallest |z|"** reads as ascending; the code takes the larger smallest-|z|. Read as ascending, HDAC5's representative becomes Quisinostat and two more representatives and 5 to 6 clusters change.
3. **Ties are not documented or exported.** 7 of the 15 hand-overs sit in an exact tie; the winner is the first in the in-memory row order (equal to proposal-id order in the committed table). Reversing the order changes 9 representatives (6 genuine, 3 case-twin flips); a name-ordered tie-break changes 4. The 15 ids and the 15 clusters are unchanged only because the committed order is fixed. The HDAC5 representative is robust; XIAP, EZH2 Q8 and ROCK2 are not.
4. `REASON_LABELS["mechanism_cluster_selection"]` is defined but exported nowhere: `handoff_blocker` is empty for the 11 non-selected eligible HDAC5 rows and `alternatives_same_mechanism` has names only.
5. "Salt twins count once" holds for selection, not for `n_eligible` (families, not names: EZH2 shows 4 for 3 names).
6. IT26 A1 README says the EZH2 Q5 "slot is already held"; `handed_over` is 0 there (wording, see above).
7. Data joins, not rule text: tazemetostat (EZH2 IC50 11 nM, GtoPdb ligand 7011, ref 23620515) and martinostat (HDAC5 352 nM, ref 25203558) have values in the cache but read NOT_ASSESSABLE; TMP269 has CHEMBL3110004 in `catalog/ligand_reconciliation_not_merged.tsv` and an R3 structure, yet `has_chembl = 0`.
Reconstruction check: variant V0 reproduces exactly the 15 committed hand-over ids.

## (b) Alternatives classified (`alternatives_classification_it27p5.tsv`, 76 rows over HDAC5, XIAP, EZH2 Q8, EZH2 Q5, ROCK2)

* **HDAC5, 20 families.** Capacity or order only (11): 4-phenylbutyric acid, pivaloyloxymethylbutyrate, CUDC-101, trichostatin A, belinostat, dacinostat, givinostat, quisinostat (ranked lower on zmin), valproic acid, abexinostat, panobinostat (k3, no HDAC5 value). Of these CUDC-101 (EGFR 2.4 and HER2 15.7 nM more potent than HDAC5 11.4 nM), valproic acid and 4-phenylbutyric acid also differ in action. Scientifically excluded: nanatinostat (own record, molecule-specific), vorinostat (attribution screen, a convention). Modality typing: romidepsin. Missing identity (5): TMP269, SS-208, KA1010, scriptaid, martinostat.
* **XIAP, 8.** Tie (xevinapant, idronoxil); missing identity (SM-122, SM-337, AZD5582, BV-6); modality typing (GDC-0152). Idronoxil keeps its limit: identity firm via R4 (CID 219100, CHEMBL1957038), the XIAP pair rests on a listing-only DGIdb claim, no affinity, pharmacology unresolved.
* **EZH2 Q8, 14 names.** Tie (tazemetostat, mevrometostat); worked earlier (GSK343, priority only); missing identity (nine, including the dual EZH1/2 valemetostat and tulmimetostat). Q5: the same, with the four eligible names demoted by k1 and the cap.
* **ROCK2 Q5, 20.** Tie (belumosudil, fasudil, ripasudil); missing identity (the rest).

## (c) Comparison (`comparison_it27p5.tsv`)

* **HDAC5 pracinostat discordance** (`pracinostat_hdac5_discordance_it27p5.tsv`): IC50 at HDAC5 is 47 nM in the GtoPdb release (reference 20197387, SB939 originator paper, S*BIO 2010) and 5,113 nM in ChEMBL document CHEMBL4706478 (29360358, J Med Chem 2018, class IIa fluorogenic substrate, HDAC4/7/9/11 also above 10,000 nM there); Ki is 21 nM in a third document (25637120). Same measure type disagrees 109-fold; the two IC50 documents share a Singapore lineage (author overlap), so they are not independent. Both IC50 rows agree at HDAC1 (49 v 50 nM). Not averaged; not reconciled; the idea that the class IIa assay design explains it is a hypothesis (neither methods section was read); nothing is carried to other class members. Abstracts only for 20197387, 25637120 and 29360358.
* **HDAC5 within one document (Ki, 20139990):** HDAC5 is 200 to 2,800 times weaker than HDAC1 for belinostat, givinostat, dacinostat, scriptaid, trichostatin A and vorinostat: a secondary action for these. Pracinostat's own Ki is flat (HDAC5 21, HDAC1 28 nM) but its IC50 panel is not; the profile of the class cannot be inferred from either.
* **Independence:** all HDAC5 members share one seed origin and one muscle-knockdown edge reference; the evidence behind the hypothesis does not discriminate between them.
* **XIAP:** every antagonist is cIAP-preferring (ASTX-660 12.7x, xevinapant 35x, SM-122 26x, SM-337 17x) or balanced (AZD5582 1x); the measures are BIR3 or BIR2-BIR3 binding, not the post-translational XIAP to HIF1A edge of the chain. A compound result cannot be assigned to XIAP rather than cIAP1/2; the genetic XIAP perturbation already in the handoff is what discriminates.
* **EZH2:** Q5 and Q8 are two experiments (EZH2 to IL6/TNF, mouse, two origins, sign contested by its own reference; EZH2 to NFE2L2, human deposits, one origin, adjusted p above alpha), not two representatives. Dual EZH1/EZH2 agents are a different-action subclass flagged highest-risk for the myelin axis.
* **Exposure:** no CNS exposure datum for any member of any of the four clusters was found in the repository; absent is not low. All potency rows are cell-free.

## Proposed changes (not applied; none alters an order term)

1. Export, per alternative, its class or blocker (`ELIGIBLE`, `identity_not_resolved`, tie, and so on) in `handoff_it21.tsv`. Measure: the table is derivable from the stage tables (this package did it); 15 ids unchanged.
2. State and export the tie rule and a `tied_with` column. Measure: V4 (reversed input) changes 0 representatives; today 9.
3. Add an informational `more_selective_eligible_alternative` column (same measure type, fold at least 10x lower). Measure: fires in 2 of 15 (ROCK2; RARB), 0 for HDAC5, XIAP, EZH2.
4. TMP269 identity row to an R4-type file after a second-actor structure check; tazemetostat GtoPdb join (held item G6). Measure: HDAC5 n_eligible 12 to 13, hand-over unchanged; tazemetostat NOT_ASSESSABLE to SINGLE_MEASURED_TARGET.
No capacity cap (H5, H6) needs to change for any of the four clusters.

## Sources (identifiers)

Repository: `generation_it26_a1_20261104/results_s7/*.tsv`; `generation_it21_p2_20261103/run_generation_it21.py` (lines 372-376, 550-568); `generation_it22_p1_20261103/data_conflicts_it22.tsv`; `qualification_it22_p4_20261103/batch1/{README.md,qualification_it22_p4_b1.tsv,typed_potency_it22_p4_b1.tsv,receipts/FTR-20261103-29360358-01.json}`; `qualification_it21_p4a_20261103/README.md`; `multitarget_it24_p6_20261104/`; `identity_it24_p2_20261104/`; `identity_gsrs_it26_a1_20261104/`; `alias_scan_it26_a2_20261104/README.md`; `catalog/cache/gtopdb/interactions.csv`; `catalog/ligand_reconciliation_not_merged.tsv`; `relations_it23_p2_20261103/novelty.tsv`; `cases_it23_p1_20261103/frozen_current_method.tsv`; `diagnosis_it22_p6_20261103/reverse/README.md`.
Literature by PMID (as recorded in GtoPdb or ChEMBL; abstract only where stated, otherwise not read): 20197387, 29360358, 25637120, 20139990, 23524983, 20143778, 19861438, 21080647, 27222932, 31414801, 25203558, 22991226, 19597037, 18832915, 24502505, 21145740, 24320998, 22413863, 19049347, 21443232, 18022362, 23051747, 22904200, 23620515, 29211475, 28741798. The statement that class IIa HDACs act largely as scaffolds is background knowledge, not verified here.
