# IT24 P10 reverse test: four contrasting cases, reasons first, then what the generator did (2026-11-04)

Non-canonical research material, public edition (WWOX-DEE reference genotype class); not medical advice. Zero spend, no registration, no e-mail or contact string sent anywhere.
No existing file edited, no code edited, no ledger written, no git state changed. Method and vocabulary reused from `diagnosis_it22_p6_20261103/reverse/README.md`
(classes: OMISSION, NOT_EXECUTED, NOT_CONSUMED, JUSTIFIED_EXCLUSION, DATA_MISSING, REPRESENTATION_LIMIT). Full row-level table: `reverse_table.tsv` (15 reasons).

**Reading depth.** No paper was opened in this package, so no read receipt is claimed (`receipts/` not created). Statements about papers are those of
`source_check_it24_p1_20261104/` (two partial full texts, five abstracts, per its own receipts) and of `qualification_it9_p4c_e_20261030/`. Reasons below were rebuilt from tables
(GtoPdb release, catalogue, engine contributions, frozen rows), not from the explanation text of the hand-over.

## 0. Order and freeze
1. Chosen BEFORE analysis: B = idronoxil IT21P2-0034, because it is the one row touched by two IT24 packages (P1 withheld its CASP3 sign; P6 labelled it MULTI_POSITIVE through that same CASP3).
   Sorafenib 0035 and SAR-407899 0221 (the two P6 hand-over conflicts) are used as second cases for the P6 fix instead. C = sulfopin IT21P2-0454 (reason stated in section 3). D = panobinostat 0033.
2. `frozen/`: the forward rows (0031, 0033, 0034, 0035, 0454, 0180) from `results_p4/proposals_it21.tsv`, their hand-over rows, P6 decomposition, IT24 exclusion list and P2 identity routes, with `frozen_sha256.txt`;
   `source_sha256.txt` hashes the source tables (proposals `d62a65e2...`, hand-over `ddef8ecb...`, action table `9ceede89...`, Q2 contributions `45c5f821...`).
3. Date fact that matters: the committed engine outputs (`generation_it22_p1_20261103/eng_merged`, last commit 2026-11-03 20:21) and `results_p4` PRE-DATE the IT24 P1 action refresh (2026-11-04, commit 7b7df840).
   So every proposal row and the P6 decomposition are computed from the action table as it was before the eight listing-tier pairs were withheld.

## 1. Verdict per case
| Case | Verdict |
|---|---|
| A vorinostat 0031 (KNOWN diagnostic control from IT21, not a discovery or blind test) | Exclusion correct and unchanged (`main_target_weak_attribution`, 2769.2-fold). Two residuals: phase not carried (NOT_CONSUMED); P6 label MULTI_POSITIVE rests on 0.6 percent of mass (artefact) |
| B idronoxil 0034 | Not handed over (reach z 2.78 < 3): JUSTIFIED_EXCLUSION. IT24 P1 exclusion NOT_EXECUTED downstream (engine and P6 still count CASP3), bounded 0.34 percent and direction-safe. Phase-2 record unreachable: DATA_MISSING |
| C sulfopin 0454 | OMISSION in code: the attribution step ignores the record's own GtoPdb ligand id, so a measured PIN1 Ki 17 nM is invisible (NOT_ASSESSABLE). Hand-over effect nil because an earlier KEEP decision exists |
| D panobinostat 0033 | Exclusion of SIRT1-7 preserved at the action table (JUSTIFIED). Downstream not re-run (NOT_EXECUTED), cannot flip the row: removed mass is positive and z_reach 2.93 is already below 3 |

## 2. Case A, vorinostat IT21P2-0031 (Q2 H_HARM, chain HDAC5 -T(+)-> SLC2A1, status CONDITIONAL_H_HARM, qualified no)
Frozen digest: z_total 5.686, z_reach 3.159, top_seed_share 0.745, blocker `main_target_weak_attribution`, attribution HDAC5 Ki 3600 nM vs HDAC1 Ki 1.3 nM, seven co-potent targets, sibling `FAM:CAT:CHEMBL98` z_reach 0.128 mimics, max_phase blank.
Favourable reasons and steps (anchors in `reverse_table.tsv` A1-A6):
* A1 metabolic route (seed measured, edge inferred): step present, used, blocks hand-over. JUSTIFIED_EXCLUSION.
* A2 potent class-I targets by other chains: executed on the ChEMBL sibling; my per-target mass (`target_mass.tsv`) shows HDAC2 -68 percent, HDAC3 +32 percent of the sibling's Q2 mass, net contrary. Consumed; the reason does not survive execution.
* A3 HDAC6 stability arm: no step exists (seeds are readouts; turnover is not a seed type). REPRESENTATION_LIMIT; the card deferral stays.
* A4 approved, phase 4: `status_class` carried, `max_phase` blank. `run_generation_it21.py` l.638 takes phase only from the family's own ChEMBL source; the bridged sibling (phase 4.0) is not used. NOT_CONSUMED.
* A5 CSF exposure: no exposure input. DATA_MISSING.
Code vs agent: row fields, z values, attribution, blocker, sibling = code. Seeds' role hypothesis, card A01 deferral, the reading of the CSF datum = agent text.

## 3. Case B (idronoxil 0034) and case C (sulfopin 0454)
**B.** Frozen digest: Q2 H_HARM, chain `XIAP -P(+)-> HIF1A -T(+)-> LDHA`, 10 seed rows, top seed 19 percent, z_total 5.266, z_reach 2.78, blocker `reach_null_not_confirming`, attribution NOT_ASSESSABLE, has_chembl 0.
* B1 XIAP lowered by degradation (P1 source check: INDIRECT_QUALIFIED): the sign enters the engine; "abundance, not inhibition" is not a row field. Harmless here (not handed over); already proposed in P1 section 6.
* B2 HIF1A axis: executed; the exclusion is the reach convention (3), stated, with 2.78 a near miss. JUSTIFIED_EXCLUSION.
* B3 phase-2 clinical candidate: catalogue holds `CAT:CHEMBL1957038 IDRONOXIL` (phase 2.0, no signed targets) and the DGIdb twin `CAT:DGIDB:b34c953dc1fa` (ncit C2642 only, no structure). Same name, no structure to confirm: the never-by-name rule correctly refuses the join. DATA_MISSING.
* B4 CASP3 withheld by P1: the action table lost it, but the committed contributions still give CASP3 0.34 percent of Q2 net mass (my recomputation, `target_mass.tsv`) and P6 prints `targets_pos CASP3;XIAP`.
  Dropping the eight withheld pairs changes exactly one of the 1,000 P6 labels: idronoxil MULTI_POSITIVE -> SINGLE (`decomposition_sensitivity.tsv`; my re-implementation reproduces P6's 32/66/902).
**C.** Why sulfopin: highest-z Q6 H_HARM row (z_reach 11.13), earlier KEEP-AS-PROPOSAL (P4c-e E-06), and a favourable reason that is data, not prose: the local Guide to Pharmacology release already holds ligand 11540 with PIN1 Ki 17 nM and 211 nM.
Frozen digest: DGIdb-only record, `ids.iuphar_ligand ['11540']`, chembl null, attribution NOT_ASSESSABLE ("no ligand or no affinity in the local release"), blocker `identity_not_resolved`, earlier_decision KEEP.
Step tie: `attribution_screen_it21.family_ligands` joins ligands by a member's ChEMBL id or a merged claim-name bridge only; the concept-id ligand (IT24 P2 route R3) is never read. Running the existing `attribution()` with that ligand id
gives SINGLE_MEASURED_TARGET (PIN1 only; no comparison possible, unknown not negative). Hand-over would still stop (earlier KEEP; ChEMBL CHEMBL5397880 is not in the 19,933-molecule cache). The reason was consumed once by a person in P4c-e, not by the generator.

## 4. Case D, panobinostat IT21P2-0033 (a correct exclusion to preserve)
Frozen digest: Q2 H_HARM via HDAC5, z_reach 2.93, blocker `reach_null_not_confirming`, attribution UNMEASURED_AT_MAIN_TARGET (HDAC1 EC50 3 nM), identity R1 to `FAM:CAT:CHEMBL3545368`.
* D1 SIRT1-7 sign (one trial-table claim, `TALC`): seven rows in `withheld_rows.tsv.gz` (`listing_tier_claim_not_carried`) plus SIRT4/5/6 listed in `source_exclusions_it24.tsv`. Preserved. The source check found no sirtuin measurement; unknown, not negative.
* D2 downstream: SIRT6 still carries 1.87 percent of Q2 net mass in the contributions (P1 bounded 1.9 percent by another measure; they agree) and P6 prints `HDAC5;SIRT6;SIRT7` as favourable targets. Removing it can only lower z, so the exclusion cannot flip.
* D3 reach 2.93 vs vorinostat 3.16: a narrow margin on a convention; kept.

## 5. Fixes, each tested on a second case (none applied)
| Fix | First case | Second case, with evidence |
|---|---|---|
| F1 `family_ligands`: also use `ids.iuphar_ligand` of the record | sulfopin (SINGLE_MEASURED_TARGET) | `r3_attribution.tsv`: of 488 R3 rows, 460 gain an attribution state (159 ATTRIBUTABLE, 211 SINGLE, 20 WEAK, 16 BORDERLINE, 16 SECONDARY, 30 NOT_COMPARABLE, 8 UNMEASURED). Ss-208 (HDAC5, 575.8-fold) and Ka1010 (136.6-fold) are the same HDAC5 cluster as vorinostat and would be flagged WEAK as vorinostat is. No ranking change; annotation and a 20-row veto |
| F2 carry `max_phase` from `sibling_family` when the own value is blank | vorinostat A4 | 112 of 1,000 rows have blank phase and a sibling with one; 5 are handed over (pracinostat 0005, phase 3.0; tretinoin 0402, CHEMBL38 phase 4.0) |
| F3 P6 decomposition: read the refreshed action table (or the exclusion list) and apply a 1 percent mass floor to target counts | idronoxil B4 | floor 1 percent: CONFLICT 32 -> 9, MULTI_POSITIVE 66 -> 34; both hand-over conflicts (sorafenib 0035, SAR-407899 0221) and pracinostat/LGH-447 become SINGLE; panobinostat CONFLICT -> MULTI_POSITIVE. 5 percent: 2 conflicts, 30 multi. Labels only, no eligibility change |
Not proposed: re-running the engine for IT24 P1 (direction-safe, bounded, no second case); name-equal curation list (126 of 509 identity-blocked rows have one name-equal ChEMBL record, but name is not identity; a join needs a structure key, and idronoxil has none).
F1 has the largest reach but changes annotation only; the 20 WEAK rows are the part that changes a decision.

## 6. Hostile reading (kept separate; negatives not dropped)
* Four cases chosen for contrast, one of them (A) known; this is a probe of steps, not an estimate of how often the generator loses a reason.
* My classification of sulfopin as OMISSION changes no hand-over; if the question is "did a candidate go missing", the answer for C is no.
* F1 shows that an existing screen would run, not that its answer is right: SINGLE_MEASURED_TARGET (211 rows) means "not comparable", not "selective"; GtoPdb ligand-to-compound identity for R3 is by concept id, not independently confirmed here.
* The mass shares use each seed's strongest-walk main target (a lower bound, as P6 states); removing a target would send those seeds to the next walk, so the 0.34 and 1.87 percent are not the exact z effect.
* A2/A3/A5 rest on IT21 V1 and IT22 P6 readings I did not re-open; no paper was read here.
* The pre-IT24 timing fact (section 0.3) was read from commit dates; I did not re-run the engine to confirm numerically.

## 7. Files
`reverse_table.tsv`, `target_mass.tsv` (+`target_mass_it24_p10.py`), `decomposition_sensitivity.tsv` (+`decomposition_sensitivity_it24_p10.py`), `r3_attribution.tsv` (+`r3_attribution_it24_p10.py`), `frozen/`.
Scripts are read-only; run with `LEGEND_CATALOG_CACHE=/home/desktop/legend-development/disease-models/wwox/research/drug_repurposing/catalog/cache`.

## Integrator decisions (2026-11-04)

- **F1 applied in code** (`attribution_screen_it21.family_ligands` now also reads the record's own `ids.iuphar_ligand` when it is one unlabelled ligand; regression `test_family_ligands_use_the_records_own_concept_id_ligand_only_when_unambiguous_and_unlabelled`; 47 attribution tests and 45 generation tests pass). The committed stage tables (`generation_it22_p1_20261103/results_p4`) were NOT regenerated: they cannot be re-derived from a single documented command, so the effect stays the read-only measurement above (460 of 488 R3 rows gain an attribution state, 20 become WEAK_ATTRIBUTION) until the next generation run carries it. Code and committed tables therefore differ on purpose and the difference is stated here.
- **F2 (max_phase from the sibling family) not applied:** 112 rows, 5 handed over, annotation only; a candidate for the next generation run with the same regeneration.
- **F3 not applied to code; stated in the P6 README:** with a 1 percent mass floor the target-level conflicts fall from 32 to 9 and multi-positive from 66 to 34; both hand-over conflicts become single-target.
- **P1 downstream:** the engine contributions still carry the withheld targets (CASP3 0.34 percent, SIRT6 1.87 percent of Q2 mass); the engine was not re-run, effect bounded and direction-safe (removing the mass can only lower z; both rows are already below the reach threshold of 3).
