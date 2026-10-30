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

**A. A candidate the rule would have resurfaced and F5 removes.** The origin-aware order applied to the IT9 tables puts the fumarates (dimethyl fumarate, monomethyl fumarate, diroximel fumarate, an NRF2 peptide) at the top of the Q5 `H_PROTECT`
list (two origins, via KEAP1 -P-> RBX1 -P-> NFKBIB -T-> TNF). IT9 P4c-d dropped exactly that chain (RBX1 joins two different E3 ligases). On v4 the chain does not exist and the fumarates leave the list: the fix is in the engine, not in a note.
The audit on the IT9 best chains: **39 of 161 multi-hop chains had an invalid junction** (Q2 10, Q5 9, Q6 20). Rerun of all seed sets under the three nulls: seed-specific and unflagged families **lost 72** (Q5 33, Q6 36, Q2 2, Q4 1) of 1,225,
**gained 49** (re-ranking under changed nulls; not validated, section 5).

**B. A different candidate to deepen (Q5, `H_HARM`, top 8).**

| Rule on | Top 8 (known to LEGEND marked *) |
|---|---|
| IT9 tables, v3 rank (what IT9 did) | JTE-151*, CD24Fc, bifonazole, L6H21, BI-2536, dual BRD4/PLK1 inhibitor, compound 6, XY-06-007 |
| IT9 tables, origin-aware | CD24Fc, bifonazole, L6H21, benziodarone, prenylamine, voclosporin, omaveloxolone, PF-03758309 |
| **v4 tables, origin-aware** | CD24Fc, bifonazole, L6H21, voclosporin, omaveloxolone, PF-03758309, JTE-151*, BI-2536 |

Benziodarone and prenylamine leave through F5 (CALM1 -P-> PPP3CA joins on a complex target); omaveloxolone (NFE2L2 -T(-)-> IL1B, a terminal transcriptional edge) and voclosporin (PPP3CA -P-> NFATC4 -T-> TNF) stay. JTE-151,
the IT9 first choice, has one origin (PMID 30290271 only) and drops from position 1 to 7. For Q2, Q4 `H_HARM`, Q6 the rules coincide because every candidate has a single origin (Q2 100 of 100 rows, Q6 150 of 150): **no change is the result there**,
and it says that the z values of those lists measure one dataset.

**C. Two hypotheses separated, a candidate kept informative (Q2).** In IT9 roxadustat was DROPPED "as a lever" because it "pushes the seeds in the disease direction by construction", which assumes the HIF-dependent shift is harmful; K01 states the
role is unresolved. Role-aware, the PHD inhibitors (roxadustat, daprodustat, desidustat) are `H_PROTECT` hypotheses (sustain a possibly adaptive response) paired with PX-478 and the HIF-1alpha lowerers as `H_HARM`, resolved by the same K01 step 0 and
arms A to C. `dispositions_Q2.tsv` marks roxadustat `REVIEW_ROLE_DEPENDENT_DROP` (the other reasons stay: the engine chain EGLN2-FOXO3 is contradicted and is not what the compound does; the label seizure signal is a SYSTEMIC development limit and
`dev_constraints.tsv` records it as not affecting an ex vivo probe; the thyromimetic action is a probe-specificity confound). Of the 32 IT9 records, exactly **one** drop depended on the role assumption; the other 31 stand, because they failed at the
provenance of the chain, the identity, or the contradiction.

**D. The graph does not find the phenotype-proven leads.** Of the 7 interventions with a signed functional result in a WWOX system, 2 are outside the method's modality (gene addition, diet), 1 has no catalogue identity (A51), **3 have no graph row at all
(ethosuximide, lithium, vigabatrin)**, 1 is scored but not seed-specific (d-APV, Q4). The graph recovered 0 of the 5 molecules in a seed-specific arm; lithium (GSK3B, Q7) is a direct hit with a zero score. This is a limit of the representation (zero signed
edges to the readout), not a statement about the molecules; the phenotype-first arm is the route by which such candidates enter generation.

## 4. Tests (`test_it10_p1.py`, 21 tests, production code, with inverses)

Junction rule on toy graphs (complex target blocks, complex source blocks, singleton junction unchanged, ends unconstrained, junction off equals v3 on the toy) and on the real network (the DMF chain exists with the filter off, and not with it on;
HIF1A to BNIP3 as a one-edge chain is kept, the XIAP two-edge chain is not); the role function (unknown keeps both arms, SOURCE_STATED withdraws, a leaning never withdraws, composition holds, a harmful role without a source is refused, the committed roles
are valid and none asserted); origins (the two deposits fold to one, one article at two levels is two, unreconstructable stays its own); phenotype-first (ethosuximide and lithium enter with NO_GRAPH_ROW, a curated extra enters); exposure (the systemic limit leaves
the probe eligible, a probe-level block is visible); and the three protected regressions (duplicated evidence, no transfer between molecules, unknown is not negative) by running the existing ranking tests. All 21 pass; the five ranking tests pass.

## 5. Limits and UNVERIFIED

* The 49 families gained by the rerun are a re-ranking effect of the changed nulls (as v2 to v3), not validated candidates; none has been through qualification.
* F5 reads a record-level flag (an alone symbol in some record). It does not know that the same complex name hides different compositions in SIGNOR; it only refuses to join on a member that appears solely inside complexes. Whether the removed chains are
  biologically wrong is not claimed, only that the join is not supported by a record that names the junction entity alone.
* Roles are all unknown: no seed states one. The role-aware arms therefore multiply hypotheses rather than choose between them; their value is the named resolving measurement and the removal of a silent assumption. A question moves to SOURCE_STATED only with a source.
* Origins are reconstructed from locator text. Two mouse models (null hippocampus, P47T cerebellum) are two origins at the experimental level; they are not evidence of WWOX specificity beyond those models. A seed row with no accession, system id or single PMID is its own origin.
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
