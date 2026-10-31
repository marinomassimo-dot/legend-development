# IT10 P1: four changes to the generation path, driven by matching_guidance_v3.md

Orchestrator, task `ORCH-ROADMAP-IT10-20261031`, branch `task/it10-p1` (from main `e7a56ef8`). Exploratory, computational. **Not medical advice. A compatible action of a context-free signed network is
not a predicted benefit; a conditional hypothesis is not a recommendation; association is not modulation and modulation is not rescue.** Reference genotype: a WWOX-DEE genotype class; no individual-level record.
Nothing here edits a card, a need, the ranking, a registry or the receipt ledger; the edits this work implies are in section 8.

## 0. Which principles of the guide were in the calculation, and which only in annotations (the diagnosis)

| Guide principle (section) | State at the end of IT9 | Where it acted |
|---|---|---|
| Typed edges, identity of targets, active moiety (sections 3, 7; IT9 v3 filters F1 to F3) | **in the calculation** (`seed_engine_v3.py`, `build_actions_v3.py`) | decides what scores |
| Seed level and direction; uncertain direction gives conditional arms; guard tags (section 5) | **in the calculation** (`seed_engine.py`) | decides what scores |
| Observed direction vs interpreted role: harmful, protective, mixed, composition, unknown (section 5) | **absent**: `seeds.tsv` has no role column and none of the 65 usable seeds states a role (text scan for protective, adaptive, harmful, compensat, detriment, deleterious, beneficial, pathogenic, causal: 0 hits). The P1 question table holds the conditional hypotheses A and B in prose (`questions.tsv`), but P2 to P4 never read them: every `opposes` row was treated as the goal and every `mimics` row as a direction control, i.e. the role was silently assumed harmful | **annotation only, and in prose** |
| Convergence needs independent origins (section 7) | **absent**: PX-478's z comes from 15 seed rows that are one pair of human deposits | **annotation only** ("contributing seeds" columns) |
| Phenotypic recovery enters even without a mechanism or a graph path (logic 8, section 6) | **absent**: the engine can only return what scores; 0 of the 5 molecules with a signed functional result in a WWOX system is a seed-specific graph candidate | **not represented** |
| Research priority vs development requirements (section 8) | in the ranking and the pilot cards; **not in the generator output** | annotation only |
| Chains join only at the same entity (symbol is not identity, section 7) | **partly**: compound side done (F2); **network side not**: complex records are split into members, so two different complexes sharing a member are chained (disclosed unaudited in IT9 P4c-d) | **missing** |

## 1. Decision (first)

| Question | Answer |
|---|---|
| Does the change alter generation or the disposition of candidates relative to IT9? | **Yes, in four places** (below). Each has an executable before/after (section 3) and a test with its inverse. |
| Is a new engine built? | **No.** `engine_v4/seed_engine_v4.py` loads v3 and replaces two names (about 100 lines); `dispose_it10.py` reads the v3/v4 candidate tables; `--junction off` reproduces the v3 proposal table byte for byte (checked on Q5, 2,867 rows). |
| What does it NOT show? | No compound is shown active in a WWOX system. A conditional hypothesis is a research question with its role-resolving measurement. The lists below are not qualified. |

## 2. The four changes

1. **Role-aware arms (matching_guidance 1.2, 5).** `question_roles.tsv` makes the role of each question's change an explicit, sourced input (`role_status` closed vocabulary, `role_basis` SOURCE_STATED or NONE;
   a harmful or protective role without a source is refused by the loader). For roles unknown or mixed (all seven questions today) the `opposes` rows become `H_HARM` hypotheses (conditional on the change being harmful) and the `mimics` rows
   `H_PROTECT` hypotheses (conditional on it being protective: sustain or amplify the response; not "disease direction by construction"); both are kept, each with the measurement that resolves the role (`resolving_measure`).
   An arm is withdrawn only when the role is SOURCE_STATED; a curator leaning orders arms and never withdraws one. Composition-confounded changes hold both arms.
2. **Origin-aware convergence (guide 7).** Contributing seed rows are folded to evidence origins where the origin is reconstructable (accession or system id in the locator; PMID plus readout level otherwise; the two human deposits
   fold to one; one article at two readout levels stays two; an unreconstructable origin stays its own and is flagged). Not deduplicated by PMID alone. The deepening order is by origins first, then the v3 rank.
3. **Phenotype-first entry (logic 8).** `phenotype_first.tsv` admits every intervention with a signed functional result in a WWOX system (ranking `member_evidence.tsv`) plus curated extras
   (`phenotype_first_extra.tsv`), whatever the graph returns; `graph_status` is computed and reported, never required.
4. **Member junction F5 (engine v4).** A chain a to b to c is admissible only if b is a singleton in both records (some record of a to b has b alone as target, some record of b to c has b alone as source). The end nodes are unconstrained.
   Also: a systemic-development limit (`dev_constraints.tsv`, each row sourced to an IT9 file) is reported beside, not instead of, the ex vivo probe eligibility.

## 3. Executable before and after

Run: `python3 dispose_it10.py run` (reads `results_v4/`, compares with the IT9 v3 tables). Files: `results/deepening_candidates.tsv`, `results/dispositions_Q*.tsv`, `results/v3_vs_v4_counts.tsv`, `results/v3_specific_lost_in_v4.tsv`.

**A. A chain IT9 dropped by hand is now removed by the engine.** IT9 P4c-d dropped KEAP1 -P-> RBX1 -P-> NFKBIB -T-> TNF for dimethyl fumarate because RBX1 joins two different E3 ligases, and noted that other chains were not audited. On v4 that chain does not exist (test on the real network); the fumarates sit at ranks 2 to 5 of the unfiltered Q5 `H_PROTECT` origin list (Neoceptin-3 first) and leave it.
The audit on the IT9 best chains: **39 of 161 opposes/mimics rows (20 of 65 distinct question-chain pairs) had an invalid junction** (rows: Q2 10, Q5 9, Q6 20). Rerun of all seed sets under the three nulls: seed-specific and unflagged families **lost 72** (Q5 33, Q6 36, Q2 2, Q4 1) of 1,225,
**gained 49** (z-threshold crossings caused by the changed null spread: the gained rows have a median |Q_net_ind| of 0.0008 against 0.0059 for the kept rows, some cross by a hair; read them as noise, not signal, section 5). The adm null still uses the v3 degree and is not junction-aware.

**B. Which candidates to deepen (Q5, `H_HARM`, top 8).**

| Rule on | Top 8 (known to LEGEND marked *) |
|---|---|
| IT9 tables, v3 rank (what IT9 did) | JTE-151*, CD24Fc, bifonazole, L6H21, BI-2536, dual BRD4/PLK1 inhibitor, compound 6, XY-06-007 |
| IT9 tables, origin-aware | JTE-151*, ALRT-1550, benziodarone, prenylamine, voclosporin, omaveloxolone, PF-03758309, CD24Fc |
| **v4 tables, origin-aware** | JTE-151*, ALRT-1550, voclosporin, omaveloxolone, PF-03758309, CD24Fc, bifonazole, L6H21 |

Benziodarone and prenylamine leave through F5 (CALM1 -P-> PPP3CA joins on a complex target). Origins: a seed row can cite two articles; S085 (TNF) cites the null hippocampus and the P47T cerebellum, but the null-hippocampus
Tnf-a increase is not significant at the source (PMC7104842 Results 3.3: "Il6 significant at p < .05"; verified 2026-10-31), so `origin_overrides.tsv` removes that origin and S085 keeps the P47T one. The effect of the origin rule is modest and
threshold-dependent (a seed row counts when it carries 10 percent of the strongest contribution; at 0.25 and above voclosporin leaves the top 8): in Q5 `H_HARM` 5 of 50 candidates have two origins, in Q5 `H_PROTECT` 15 of 25.
For Q2, Q4 `H_HARM` and Q6 the rules coincide in the tables because every candidate has a single origin (Q2 75 of 75 opposes/mimics rows, Q6 150 of 150). That result rests on a declared judgement: the two human deposits (GSE156243 organoid, GSE126075 hNPC) are folded to one
origin because they were read with one method and one derivation; counted as two, Q2 would also have two origins for every candidate. The top-8 Q5 `H_PROTECT` list on v4 is a single mechanism class (FGFR inhibitors), not eight independent leads.

**C. Two hypotheses separated, a candidate kept informative (Q2).** In IT9 roxadustat was DROPPED "as a lever" because it "pushes the seeds in the disease direction by construction", which assumes the HIF-dependent shift is harmful; K01 states the
role is unresolved. Role-aware, the PHD inhibitors (roxadustat, daprodustat, desidustat) are `H_PROTECT` hypotheses (sustain a possibly adaptive response) paired with PX-478 and the HIF-1alpha lowerers as `H_HARM`, resolved by the same K01 step 0 and
arms A to C. `dispositions_Q2.tsv` marks roxadustat `REVIEW_ROLE_DEPENDENT_REASON` (the other reasons stay: the engine chain EGLN2-FOXO3 is contradicted and is not what the compound does; the label seizure signal is a SYSTEMIC development limit and
`dev_constraints.tsv` records it as not affecting an ex vivo probe; the thyromimetic action is a probe-specificity confound). `it9_role_dependent_reasons.tsv` lists the IT9 drops whose stated reasons include the role assumption: **roxadustat** (sole stated reason of direction) and **harmine** (one of several reasons: MAO-A selectivity, psychoactivity; its MYC mimics direction is the role-dependent one and the other reasons stand). The remaining drops were read for
their stated reasons (provenance of the chain, identity, contradiction) and are not reopened; this classification is by the IT9 reason text, not recomputed.

**D. The graph does not find the phenotype-proven leads.** Of the 7 interventions with a recorded WWOX-system result (admission rule: `tested_in_wwox_system = yes`; sign, depth and readout are carried as columns, and several results are null, mixed or abstract-level), 2 are outside the method's modality (gene addition, diet), 1 has no catalogue identity (A51), **2 have no graph row
(ethosuximide, vigabatrin)**, d-APV is a direct hit with a zero score (Q4; its own family, status derived per member), and lithium has name twins (carbonate, citrate) that are scored but never seed-specific (Q2, Q5, Q6) and are direct hits with zero score on GSK3B (Q7). The graph recovered 0 of the 5 molecules in a seed-specific arm. This is a limit of the representation (zero signed
edges to the readout), not a statement about the molecules; the phenotype-first arm is the route by which such candidates enter generation.

> **Correction, IT11 (2026-10-31).** The sentence "the graph recovered 0 of the 5 molecules in a seed-specific arm" is wrong as written: `phenotype_first()` read the truncated candidate tables (top 50 opposes / 25 mimics per set). Read from the full seed-specific list, **lithium is a seed-specific `mimics` hit in Q6 expression under all three nulls** (four name-twin families, rank 67 to 70 of 232; z -12.1 / -8.9 / -6.4; the hit is MYC expression in a human seed through GSK3A -P-> NOTCH1 -T-> MYC, a single-gene set, and not the lead's mouse seizure readout, which lithium also lowered in wild-type panels). d-APV's "zero" is the indirect part only: it is a direct hit in the Q4 direct-search arm (Q_direct -0.5). Ethosuximide and vigabatrin have no path to any seed (sink nodes / not network nodes). See `coverage_it11_p21_20261031/`.

## 4. Tests (`test_it10_p1.py`, 31 tests, production code, with inverses)

Junction rule on toy graphs (complex target blocks, complex source blocks, singleton junction unchanged, ends unconstrained, junction off equals v3 on the toy) and on the real network (the DMF chain exists with the filter off, and not with it on;
HIF1A to BNIP3 as a one-edge chain is kept, the XIAP two-edge chain is not); the role function (unknown keeps both arms, SOURCE_STATED withdraws, a leaning never withdraws, composition holds, a harmful role without a source is refused, the committed roles
are valid and none asserted); origins (the two deposits fold to one, one article at two levels is two, unreconstructable stays its own); phenotype-first (ethosuximide and lithium enter with NO_GRAPH_ROW, a curated extra enters); exposure (the systemic limit leaves
the probe eligible, a probe-level block is visible); and the three protected regressions (duplicated evidence, no transfer between molecules, unknown is not negative) by running the existing ranking tests. All pass; the five ranking tests pass. The hostile review (independent oracle for the influence, 5,811 expression and 5,708 protein pairs: 0 mismatches) mutated the engine: 8 mutations were caught, 4 were not; the revision adds tests for protein level, `with_signs`, flag aggregation (OR over records), a three-edge chain, one-edge chains from complex sources, and a toy consistency check of `best_chain` against the influence, and the OR-to-AND and first-hop-channel mutations are now caught (checked by hand).

## 5. Limits and UNVERIFIED

* The 49 families gained by the rerun are a re-ranking effect of the changed nulls (as v2 to v3), not validated candidates; none has been through qualification.
* F5 reads a record-level flag (an alone symbol in some record). It does not know that the same complex name hides different compositions in SIGNOR; it only refuses to join on a member that appears solely inside complexes. Whether the removed chains are
  biologically wrong is not claimed, only that the join is not supported by a record that names the junction entity alone.
* Roles are all unknown: no seed states one. The role-aware arms therefore multiply hypotheses rather than choose between them; their value is the named resolving measurement and the removal of a silent assumption. A question moves to SOURCE_STATED only with a source.
* Origins are reconstructed from locator text. Two mouse models (null hippocampus, P47T cerebellum) are two origins at the experimental level; they are not evidence of WWOX specificity beyond those models. A seed row with no accession, system id or single PMID is its own origin.
* Review findings kept as limits: the best chain is the single maximum-weight chain while the score is a signed sum (pre-existing); proximity and `dist_to_set` ignore F5; `adm_indeg` is the v3 degree. `dev_constraints.tsv` column `affects_ex_vivo_probe` is the author's judgement; the facts match the cited IT9 files (reviewer-checked); `question_roles.tsv` prose for Q4, Q6, Q7 no longer says an arm is not a lever (the code keeps those arms conditional, with a risk note).
* The v3 `selftest` subcommand fails on 3-tuple toy edges (`seed_engine_v3.py selftest`, pre-existing, unreported; classified: unused by the pipeline, replaced by the tests above); not changed.
* `dev_constraints.tsv` rows are transcribed from IT9 files (cited per row); they were not re-verified at the label source here.
* The engine reruns took 2 min (30 seed-set by null runs) plus 1.7 min for the tables; `dispose_it10.py` 0.3 s.

## 6. Commands

```
export LEGEND_CATALOG_CACHE=<root>/disease-models/wwox/research/drug_repurposing/catalog/cache
python3 engine_v4/run_v4.py --out results_v4                 # v4 engine, three nulls, candidate tables (--junction off reproduces v3)
python3 compare_v3_v4.py                                     # lost / gained seed-specific families
python3 dispose_it10.py run                                  # dispositions, origins, deepening comparison, phenotype-first
python3 test_it10_p1.py
```

## 7. Files

`question_roles.tsv` · `dev_constraints.tsv` · `dispose_it10.py` · `engine_v4/seed_engine_v4.py`, `engine_v4/run_v4.py` · `compare_v3_v4.py` · `test_it10_p1.py` · `results_v4/` (proposal and contribution tables, candidate tables) ·
`results/` (dispositions, deepening_candidates, phenotype_first, v3_vs_v4_counts, v3_specific_lost_in_v4, disposition_counts, summary.json). One change to IT9 code: `generation_it9_p2_20261030/v3/make_candidates_v3.py` accepts `--engine PATH` (default unchanged).

## 8. For the batch path

Record the folder as IT10 P1 research material and the method note "the generation path keeps the role of the observed change as a sourced input (all unknown today), folds convergence to evidence origins, admits phenotype-first interventions without a graph row, and joins chains only at
singleton entities (v4); one IT9 drop (roxadustat) depended on the role assumption and is reopened as a conditional probe hypothesis". No registry, card or need edit is proposed by this package; the P2 packages propose theirs.

## 9. IT11 P1 addendum (engine coherence; 2026-10-30/31, Orchestrator, task ORCH-ROADMAP-IT11-20261031)

Read before formulating: this README, the v4 engine and `dispose_it10.py`, the hostile-review findings of IT10. Each item below was classified before any change.

| Item | Verified finding | Intervention | Effect on decisions |
|---|---|---|---|
| P1.1 score vs shown chain | The score is a signed sum over seeds and, per seed, over every admissible walk; the chain shown is the single strongest walk of the strongest seed. The signed walk sum equals the influence the score uses (test: 5 real pairs plus 240 random pairs at both levels with the filter on and off; the hostile review found that the first version stopped a walk at its first arrival at the seed and so missed walks that pass through the seed and return, up to 20 percent in `--mode all`; fixed, with a toy test; the 56 pairs behind the shipped rows were already exact). `best_chain` still stops at the seed: the shown chain is a walk that does not revisit it. Of the 375 opposes/mimics rows of the Q2/Q4/Q5/Q6 candidate tables (top 50 / 25 per set; 10 of them are not seed-specific), 51 are `PARTIAL_EXAMPLE` (Q2 32, Q5 6, Q6 13): in Q2 the strongest seed carries a median 74 percent but for PX-478 only 11 percent of the gross contribution (15 equal seed rows of one origin); in Q6 13 rows have more than 10 percent of the pair's walk mass opposing the net. At pair level no row has its strongest walk below half of the pair's mass. | `Graph4.walks`/`walk_summary` and eight columns in `dispositions_Q*.tsv` (`chain_note`, `top_seed_share`, `contrary_seed_share`, `chain_pair_walks/share`, `chain_contrary_walks`); `explain_summary.tsv`; no new explainability system. A walk is arithmetic, not a confirmed mechanism. | No ranking change. A reader of the PX-478 row now sees that the shown chain is one of many seed contributions; one dominant chain explains Q4/Q5/most Q6 rows. |
| P1.2 F5, proximity, nulls | Proximity columns (`prox_*`) use the reference topology (every edge, no mode, no F5): a different question from the admissible score. The shortest reference path is shorter than the admissible chain in 13 of 365 rows and equal in 352: a legitimate distinct measure, kept and named here, not removed. The null covariate (v3 admissible in-degree) matches the first hop only; a reach-matched null (null genes matched on the number of nodes with an F5-admissible walk to them, `--match reach`) agrees (Spearman of z 0.912 to 0.985; 'reach-matched' means matched within decile bins of the reach, which is coarse: at protein level 5,508 of 8,769 genes have zero reach and the top expression bin spans reach 221 to 964) and removes from the 3-null specific list: Q2 6 of 67, Q4 2 of 88, Q5 7 of 354, Q6 expression 14 of 540, **Q6 protein 44 of 180** (single MYC seed; median effect of the removed rows is lower than that of the kept rows in every set, 0.0003 to 0.03 against 0.0009 to 0.064). | `--match reach` in the v4 engine; `compare_nulls_it11.py`; `reach_null_z` column in the dispositions. `--junction off` still reproduces v3 byte for byte (Q5 rechecked after the IT11 changes). | Effect size and threshold sensitivity are read apart: expression lists are stable; the Q6 protein list is covariate-sensitive, not only threshold-sensitive (a quarter of its rows leaves, and only 2 of the 44 have a reach z between 2.5 and 3), so its rows need qualification before any reading. Families gained by a change of null are not promising by crossing a threshold. |
| P1.3 origins | The doubtful choices were varied (`origin_sensitivity_it11.py`): the two human deposits kept as two origins (A), threshold 0.05 (C) and 0.25 (D). The variant 'levels of one article merged' was dropped as NOT APPLICABLE: the engine refuses mixed readout levels in a run, so the seeds contributing to a family share one level and a merge cannot act (it was vacuous in the first version). | none needed | 22 of 24 top-8 lists identical to the default; Q5 H_HARM at 0.05 (3 of 8 change) and Q4 H_PROTECT at 0.25 (1 of 8) differ. A changes the origin count of 75 of 375 rows (every Q2 row would have two origins) but the top-8 lists are preserved partly by construction (tied candidates keep their order); C changes 14 rows and D 6. |
| P1.4 selftest | Classified: **fixture incompatibility** (the v2 selftest builds an untyped 3-tuple toy graph that the typed Graph3 cannot read), not a production regression and not an obsolete command; the v2 selftest still passes. | v3 `selftest3` on a typed toy graph, keeping the v2 hand-computed answers and adding edge-type controls (a P edge into an expression seed and a T-first chain must score 0); v4 inherits it | `selftest --mode all` now FAILS; the review found the protein-level rule had no control, so a protein control (P chain scores, T edge into a protein seed and a T-first chain score 0) was added and a mutation that lets T edges into the protein hops is now caught. `selftest` does not test F5 (that is in `JunctionRule`). Tests for both. |

`chain_note` has a third class, `DIRECT_OR_MIXED`, for rows whose strongest seed is reached mostly by the compound's own target (none among the 375 shipped rows).

Tests: `test_it10_p1.py` 43 tests. Lithium: the 'rank 67 to 70 of 232' of the correction in section 3D is the position among the 232 seed-specific mimics rows, which count the four name-twin families four times; it is one compound with one chain. Files added: `compare_nulls_it11.py`, `origin_sensitivity_it11.py`, `results_v4_reach/`, `results/{explain_summary,null_sensitivity,origin_sensitivity}.tsv`.
