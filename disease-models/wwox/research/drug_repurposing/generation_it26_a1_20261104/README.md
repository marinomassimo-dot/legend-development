# IT26 A1: stage tables with nine more withheld pairs and identity route R4 (results_s7)

Non-canonical. Not medical advice. Nothing here is a finding; a hypothesis stays conditional and `qualified = no`.

## What was done
1. **Exclusions** (`generation_it21_p2_20261103/source_exclusions_it24.tsv`, now 21 pairs): rabeprazole to FGFR1, FGFR2, FGFR3, FLT1, FLT4, KDR (a drug-side alias collision: the DGIdb rabeprazole and lucitanib nodes both carry the code E-3810, and the six MyCancerGenome rows are lucitanib's FGFR/VEGFR profile) and fexagratinib to AKT1, AKT2, AKT3 (the DGIdb concept iuphar.ligand:7707 carries the alias AZD5363, capivasertib). Evidence in `source_check_it26_20261104/` and `alias_scan_it26_a2_20261104/`. Action table 19,908 to 19,899 pairs.
2. **Engine re-run** on the refreshed table (`run_v4.py ... --reach --reach-sets Q8_expression_tiersAB`, as in IT25; the engine directory is not committed).
3. **Route R4** (`identity_gsrs_it26_a1_20261104/identity_r4_it26.tsv`, 19 families confirmed by a second actor) read by `run_generation_it21.py` (`load_identity_r4`): identity (has_chembl, modality) for the family, never a merge.
4. **propose** with the production path wrote `results_s7/`. A control run with the R4 file moved aside isolates the two causes (control = S7a, not committed): S6 to S7a is the exclusions alone; S7a to S7 is R4 alone.

## Result (`stage_diff.tsv`, `stage_diff_summary.json`)
| | S6 | S7 |
|---|---|---|
| proposals | 996 | 994 |
| eligible for hand-over | 215 | 220 |
| hand-overs | 15 | 15 (the same 15) |

* **Exclusions (S6 to S7a):** rabeprazole FGFR3, fexagratinib AKT1 and AKT2 leave; fexagratinib now appears at its real main target FGFR3 (a ChEMBL-type FGFR inhibitor, not a new signal). Eighteen rows move by at most 0.002 in a z score (the engine's normalisation changes slightly when pairs leave).
* **R4 (S7a to S7):** 20 proposal rows of 19 families change identity. Five become eligible (pivaloyloxymethylbutyrate and 4-phenylbutyric acid at HDAC5, idronoxil at XIAP, tazemetostat at EZH2 in Q5 and Q8) and none is handed over: each sits in a mechanism cluster whose slot is already held (HDAC5: one hand-over of 12 eligible; XIAP: one of 3; EZH2: Q5 none of 4, Q8 one of 4 and already held). The other families, mostly BTK inhibitors and ATR inhibitors, leave `identity_not_resolved` and meet their next, previously hidden blocker (`shared_premise_contradicted`, `arm_has_no_stated_benefit_hypothesis`, `modality_protein_or_peptide_not_small_molecule` for PX-478, whose ChEMBL record is typed peptide-like by the catalogue). That is the same set of blockers as for any identified compound, not new evidence.
* **Not evidence:** idronoxil at XIAP rests on a listing-only claim (ClearityFoundationClinicalTrial) that the wide listing rule would withhold (`alias_scan_it26_a2_20261104/README.md`: 26 of the 996 proposals have a listing-only main-target pair; none is a hand-over). Becoming eligible is a consequence of an identity, not a better hypothesis.

## Not done
No downstream script was moved to `results_s7` (the dashboard and ranking read `results_p4`, frozen on purpose). The LINCS top-20 recheck was not re-run with the 19 new keys. Weak-label wording of the IT25 trial is superseded for these rows by the second actor's structure check, but the UNII's provenance is not independent of G-SRS (verifier's caveat).
