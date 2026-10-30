# IT9 P2: a seed-based generation engine that uses the WWOX-loss inputs (function and sensitivity proof)

Scientist-b, 2026-10-30. **Exploratory, computational. Not medical advice. Proves that the method runs, reads its seeds and reacts to them; it does not prove that any proposed
compound would help anyone** (no compound-response measurement in a WWOX-deficient system exists to test that against; IT6 P3, IT7 P0a, IT8 P4). Reference genotype class: a WWOX-DEE genotype class; no individual-level record.
Nothing here edits a registry, ledger, current file, card or need. Pre-registration: `PRE_REGISTRATION.md` (committed before any run; Amendments 1 and 2 are disclosed there with what had been seen).

## 1. Decision (first) - results on P1 v2 (seeds.tsv sha256 76952333..., 131 rows, 65 usable)

| Question | Answer |
|---|---|
| Is there a simplest method that really uses the selected WWOX inputs to propose compounds? | **Yes: signed K-hop propagation of the seed vector over the IT7 signed network, scored against each compound family's signed target actions** (`seed_engine.py`). Seeds keep level and direction; uncertain direction (and every guard-forced uncertain seed) runs as two conditional arms with an exact range. Output: compatible action (opposes or mimics, never benefit), the contributing seed, hop and target. |
| Do the seeds enter (T1) and does direction logic behave (T5)? | **Yes.** T1 and T5 pass in all 10 v2 seed sets and the provisional set (T1(d) is vacuous for sets with no defined seed: Q1 expression, Q3, Q7; reported as vacuous). Zero seeds gives exactly 0; linear in level; contributions sum to the score (1e-17); all-sign flip negates; one-seed flip changes exactly the compounds it influences. |
| Guards (T6, new) | **Pass in all sets.** `guard_tag` is read mechanically: ISR_SIGN_UNRESOLVED units are forced to uncertain direction (Q3: 0 defined seeds; the one ISR gene with a stated direction, PSAT1, now enters only as a conditional arm; ignoring the guard changes the scores, max |diff| 0.0053); IT7_READOUT6, ISR_SIGN_UNRESOLVED and HELD_OUT_ENDPOINT units never enter the signature arm (Q2: 16 of 17 units excluded; Q3: all excluded, no signature run). Unit tests `test_seed_engine.py` fail if a guard is ignored. |
| Seed-specific (T2)? | **Against random seeds yes everywhere** (median Spearman with the real ranking -0.10 to 0.15, top-100 overlap median 0 to 5 vs criteria 0.50 and 20). The registered T2 verdict is PASS in 7 of 10 v2 sets and FAIL in 3: Q2 and Q4 expression fail the sign-shuffle criterion (all defined seeds share one direction; the shuffle is the identity), Q7 fails the decoy criterion by a hair (0.504 vs 0.50); the provisional set also fails the shuffle. Reported as registered. |
| Identity / answer-in-construction (T3)? | **No identity driver found**; dichloroacetate is again flagged in Q2 (RECOVERED_ONLY_VIA_OWN_TARGET: PDK1 is a seed and its target; the result flips with the assumed PDK1 direction). Reserved rows: none is a seed row (section 7a). |
| Adds information over the direct search (T4)? | **Where the seeds are not themselves drug targets, mostly yes**, but several outcomes depend on the null: Q5 expression ADDS in both; Q6 ADDS in both; Q4 protein ADDS in both; Q2 ADDS by z-ranking in both nulls (raw Q: ADDS total / LIMITED in-degree); Q4 expression ADDS under the total-degree null and NONE under the in-degree null (depends on the null); NONE for Q1, Q3, Q7 and the provisional set. |
| Signature route | **Not informative in any v2 set** (Q3 was informative in v1 only through the ISR rows, now excluded by the guard; no eligible seeds). |
| P3 hand-over | `results/candidates_Q1..Q7.tsv` (section 7b), `results/per_question_counts.tsv`, command in section 7. |

Per-question counts (families; `results/per_question_counts.tsv`; examined = M-net-usable families with a target in the graph, 12,560 in every set):

| Seed set | Seed units (defined) | Non-zero in some arm | Seed-specific, raw-Q z>3 (total / in-degree null) | Z_ind_robust >3 in both nulls (opposes) | Z_ind_robust <-3 in both (mimics) |
|---|---|---:|---|---:|---:|
| Q1 expression, tier A,B,C | 1 (0) | 2,190 | 0 / 0 | 0 | 0 |
| Q1 protein, tier A,B,C | 1 (1) | 2,190 | 0 / 0 | 0 | 0 |
| Q2 expression | 17 (15) | 4,935 | 158 / 85 | 53 | 71 |
| Q3 expression | 17 (0) | 4,962 | 0 / 2 | 0 | 0 |
| Q4 expression | 4 (4) | 2,701 | 151 / 92 | 0 | 0 |
| Q4 protein | 2 (2) | 2,828 | 61 / 2 | 47 | 5 |
| Q5 expression | 3 (3) | 5,187 | 84 / 92 | 115 | 45 |
| Q6 (expression and protein: the same MYC seed) | 1 (1) | 3,219 | 188 / 245 | 332 | 159 |
| Q7 phospho | 1 (0) | 4,235 | 359 / 501 | 0 | 0 |

(Q5 protein of v1 no longer exists: its rows are cell-count or area `pathology` rows, which are not gene-level seeds; the Q1 sets exist only with tier C, because v2 has no tier A or B gene-level Q1 row. Q7 raw-Q z counts are large because GSK3B is a hub; with 0 defined seeds there is no robust proposal.)

What this means: the WWOX data enter as seeds and move the scores with exact attribution. The proposals are direction compatibilities from a context-free regulatory network; whether any is useful is not established and cannot be from these tests.

## 2. Method (what the engine does)

* **Seeds** (`seeds_p1/*.tsv`, made by `p1_adapter.py` from the IT9 P1 table; sha256 of the P1 `seeds.tsv`: 726dd2a1... when first read, 65817737581eb7b73bcbbdb87a640285f7aa389d3c357c03df992c49a903022e in the final merged P1; the seed tables produced from the two are byte-identical, so no result changed): gene seeds with direction and level; process seeds only where P1 lists members (level spread as 1/sqrt(n)); one set per question and readout level, **levels are never merged** (the engine refuses mixed levels). P1 gives no magnitude, so every level is 1.0 (equal weights; stated, not a finding). `unchanged` rows are null observations, not seeds. Mouse rows enter only through an HGNC ortholog link.
* **Network**: the IT7 external signed network (70,461 edges, 8,769 genes; read from `network_comparison_it7_p3_20261029/inputs`), K = 3, damping 0.5, 1/out-degree weights. Context-free.
* **Compounds**: family table `results/family_actions.tsv.gz` rebuilt from the catalogue (`build-actions`): per family and gene, mean sign of the usable signed actions (IT7 P2 rule). Unit norm over the family's targets. Conflicting up/down on one gene drops the gene (5 dropped).
* **Score** Q = - sum over target genes of (action x influence of the seeds). Q > 0: the compound's predicted effect on the seed genes opposes the seed change; Q < 0: mimics. Arms: NET-IND (hops 1 to 3, primary), NET-FULL (adds hop 0), DIRECT (hop 0 only, signed), DIRECT-ANY (any catalogue target row on a seed gene, unsigned), INTERACTOR (target among the 7 network regulators of WWOX), PROX (unsigned proximity with degree-matched null; proximity only), NET-Z (Q minus the mean of 500 degree-matched random seed sets over their SD, Amendment 1).
* **Compatible action is not benefit.** Seeds are transcript, protein or state observations; the network edges are regulatory edges; a hop-0 hit assumes transcript direction is activity direction. The `readout_level` column travels with every seed and contribution.

## 3. Denominators (unit: families, i.e. catalogue records joined by parent/InChIKey block; not distinct drugs)

| Step | Families |
|---|---:|
| Catalogued | 40,268 |
| Resolved identity (ChEMBL-linked; the rest are source-only records, never merged on name) | 16,475 |
| Usable by the method (documented signed action on a human target with stable id) | 13,379 |
| ... of which with a gene symbol (72 have none, e.g. RNAi agents) | 13,307 |
| ... of which with at least one target in the network graph (**examined**) | 12,560 |
| Examined with a non-zero score in some arm | per set in section 1 (2,190 to 5,187; provisional 5,709) |
| Signature route: families with a neural-lineage LINCS signature (phase I, via catalogue structure key) | 848 (421 with both context classes) |

2,381 distinct signed target symbols; 1,887 (79 percent) are in the graph. The unmapped list is `results/unmapped_targets_*.tsv` (alias errors can be checked there; not audited against HGNC here: UNVERIFIED).

## 4. Test results (criteria fixed in `PRE_REGISTRATION.md` incl. Amendments 1-4; `results/tests_summary.tsv`, one row per set and null variant; `results/tests_<set>[_indeg].json`)

Eleven seed sets (ten v2 sets and the provisional one) under two nulls (registered total-degree; Amendment 2 in-degree), 1000 nulls per test. Verdict columns are in `results/per_question_counts.tsv` (T1, T2, T4 under both nulls, T5, T6). Honest points:
* T2(b) is applied as registered. It is degenerate or failing when the defined seeds share one sign (Q2 expression 15 up; Q4 expression 4 down) and the provisional set (5 up, 1 down). Q7 fails T2(c) with Spearman 0.504 against the decoy (limit 0.50).
* T1(d) is vacuous where no seed is defined (Q1 expression, Q3, Q7); stated, not counted as support.
* The NET-Z arm fails the registered Spearman criterion in most sets under the total-degree null and passes the top-100 criterion; the bulk ordering of unconnected families is a deterministic artefact (-mean/SD).
* T4 outcomes that differ between the two nulls are reported as "depends on the null" (Q2 raw Q; Q4 expression).
* T6 was first coded to compare the U+ arm only, which cannot differ when a unit changes from defined-up to uncertain; the test bug was found on the first Q3 run, fixed (compare the defined-only and U- arms), and Q3 was re-run. No criterion was changed.
* v1 results (superseded by v2; kept in git history of this folder at commit 8a49d2a3): T1/T5 8 of 8 passed; T4 ADDS for Q2, Q4 protein, Q5 expression.

Reproduce: `python3 run_battery.py --seeds-dir seeds_p1 --extra seeds_provisional.tsv --actions results --out results` (about 17 min on 4 shared cores), then the `seed_sig_arm.py`, `reserved_check.py` and `make_candidates.py` commands of section 7.

## 5. What the engine can and cannot do

Can: take any seed table that passes the load rules; propose compounds whose signed target actions oppose or mimic the seed state through up to three regulatory hops; say which seed, which hop and which target produced each score (`contributions_<set>.tsv`, `explain`); report conditional proposals where the seed direction is unknown, with the exact range over all sign assignments; separate hub effects from seed-specific effects by a degree-matched null; run unchanged on a declared universe.

Cannot: say that a compound helps (every score is a direction compatibility; PRE_REGISTRATION section 5); tell protein, transcript and function apart inside the network (one regulatory level); use tissue or cell context (the network is generic); use magnitude (P1 supplies none); use compound potency, exposure or brain reach; score compounds with no gene-symbol target (72 usable families) or no signed action (the other 26,889 families); represent state, GO-term and metabolite seeds without members (counted in `seeds_p1/adapter_counts.json`: for example Q4 has 5 and Q3 has 5 such rows); be evaluated against truth (the held-out intervention data are excluded and no WWOX-deficient compound response exists). Top lists are dominated by multi-target and hub-adjacent compounds unless read through the Z columns.

## 6. External resources: TRIAL results (2026-10-30; only gene symbols or Ensembl ids were sent anywhere)

| Resource | Trial | Result |
|---|---|---|
| Open Targets Platform (GraphQL, public, no key; release 26.09) | `external_trials.py`: 42 seed genes, drugs and clinical candidates per gene vs the catalogue's hits on the same gene (`results/external_trial_open_targets.tsv`) | 42 of 42 genes resolved. 175 gene-drug pairs; 139 (79 percent) match a catalogue family by ChEMBL id (the rest are child salts or forms inside other families). No source the catalogue lacks; no sign of action in this field. **Verdict: USED AS INPUT ALREADY in substance (ChEMBL lineage); not adopted as a separate input.** WWOX itself has 0 drug candidates. |
| Every Cure MATRIX scores | HuggingFace dataset metadata read 2026-10-30 | revision d6b121bf... unchanged since the 2026-10-26 trial, `license` still absent. Not reusable or redistributable until stated; the 2026-10-26 trial found the WOREE node statistically close to sibling nodes. **Verdict: NOT AVAILABLE for reuse (no licence); nothing re-run.** |
| TxGNN | no new trial | the 2026-10-26 outcome stands (legacy stack, explorer 503, no deployment checkpoint). Not repeated: a trial would need the Python 3.8 + DGL 0.5.2 stack and the graph build, which is installing a framework to emulate a brand. **Verdict: NOT RUN (cost out of proportion; reason on record, not a WATCH).** |
| DGIdb / ChEMBL / GtoPdb | already the compound input | used. |
| LINCS (GSE92742 level 5) | `seed_sig_arm.py` | run on the v2 sets (section 1, signature row). SigCom LINCS metadata API answered HTTP 200; not queried further (the local level 5 extract is the complete form of the same data). |

## 7. Running it on a declared universe (for P3)

```
export LEGEND_CATALOG_CACHE=<root>/disease-models/wwox/research/drug_repurposing/catalog/cache
python3 seed_engine.py build-actions --out results                       # only if the catalogue changed (5 s)
python3 p1_adapter.py --p1 <P1 folder> --out seeds_p1                    # seed tables per question and level
python3 seed_engine.py run --seeds seeds_p1/Q2_expression_tiersAB.tsv --actions results --label q2 --out results --universe universe.tsv
python3 seed_engine.py tests --seeds seeds_p1/Q2_expression_tiersAB.tsv --actions results --label q2 --out results [--match indeg]
python3 seed_engine.py explain --seeds ... --actions results --family FAM:CAT:CHEMBL306823
python3 reserved_check.py --p1 <P1 folder> --seeds-dir seeds_p1 --actions results --results results --out results/reserved_check.tsv
python3 make_candidates.py --seeds-dir seeds_p1 --results results --actions results --out results      # candidate tables (needs run for each set, total and indeg)
python3 seed_sig_arm.py --seeds ... --geo <GSE92742 dir> --cache <dir with extract.npy> --catalog ../catalog/catalog.jsonl.gz --label q2 --out results
```
`--universe` takes family ids (one per line, or a TSV with a `family_id` column). `funnel_<label>.json` reports catalogued, resolved-identity, usable, in-graph, declared-universe, examined and non-zero counts. `proposals_<label>.tsv.gz` holds, per examined family with a non-zero score, Z_ind_robust, Z_full_robust, Q (full, indirect, direct, both conditional arms), the compatible action, the uncertain-seed mass, direct-hit and WWOX-regulator flags and proximity. `contributions_<label>.tsv` names, per family and seed, the direction of the seed, the hop-0 and hop 1-3 contribution and the target carrying most of it (shown for the top and bottom 100 families by Z and for direct hits; use `explain` for any other family). Uncertain-direction seeds are shown in their + arm; the sign of their contribution flips in the - arm.

## 7a. Reserved-row check (Amendment 3; `reserved_check.py`, `results/reserved_check.tsv`; rerun on v2)

26 reserved rows in v2; the gene-level ones name WWOX, LDHA, CACNA1G, PANX1, GFAP, AIF1, GAD1, MYC, CTNNB1 (others are GO or STATE rows with no gene representation and cannot be checked). **No reserved row is in any seed table.** Genes shared between a reserved response and an observed seed: WWOX (Q1), LDHA (Q2), GAD1 (Q4 protein), MYC (Q6; reserved MYC is a drug response, the Q6 seed is the loss state, direction by presence only). CACNA1G (ethosuximide target) is a seed in no set; the 4 or fewer examined families on it rank 285 to 3,059 of 2,701 to 5,187 proposals: the held-out answer is not recovered and is not claimed. MYC-targeting families (21 in the Q6 proposals) rank from 47: non-independent of the MYC seed. Nothing is fed back.

## 7b. Candidate tables for P3 (`make_candidates.py`, `results/candidates_Q1.tsv` ... `Q7.tsv`)

Per question and set: arm `opposes` (top 50 by Z_ind_robust, Z > 0), `mimics` (25 most negative), `direct_search` (families with any catalogue action on a seed gene, up to 50). Columns: family, name, Z under the total and the in-degree null, `seed_specific_both_nulls` (z > 3 in both), Q_net_ind (a score, not a ranking key), compatible action (direction compatibility only), conditional flag, also found by the direct search, the top two contributing seeds as `seed|gene|seed direction|hop|main target|contribution`, and `evaluation_forbidden_on` (guard tags). Q1 expression, Q3 and Q7 have no robust (Z) proposals because their seeds are all uncertain; only the direct-search arm is filled. Rows are families, not distinct drugs (salts and duplicates appear as separate families).

## 8. Files

`PRE_REGISTRATION.md` (with Amendments 1 and 2) · `seed_engine.py` · `p1_adapter.py` · `provisional_seeds.py` · `seed_sig_arm.py` · `run_battery.py` · `summarize_tests.py` · `external_trials.py` · `reserved_check.py` · `make_candidates.py` · `test_seed_engine.py` (positive checks on a hand-computed graph) · `seeds_provisional.tsv` · `seeds_p1/` (10 sets, manifest, adapter counts for tiers A,B and A,B,C) · `results/` (family tables, proposals, contributions, funnels, tests JSON and summary, null summaries, unmapped targets, signature arm, external trial).

## 9. UNVERIFIED and honest limits

* P1 v2 (sha256 76952333...) is the version used. If P1 changes again, rerun `p1_adapter.py` and `run_battery.py`.
* Target symbols were not audited against HGNC (21 percent are not in the network: absent genes or alias mismatches, not distinguished). Mouse seeds rely on HGNC's single-link ortholog field.
* Equal level weights; tier A and B seeds mixed (human neural and non-human neural); a set (e.g. Q2 expression) contains both a gene seed and a process seed that includes it, which double-counts that gene.
* Tests prove function and sensitivity on 10 small seed sets (1 to 17 units) and one provisional set; with so few seeds the sign shuffle has no power in most sets.
* The provisional-set results were seen before Amendments 1 and 2; Amendment 4 (guards, level rules for pathology and phospho rows, Q1 tier C) was written before the v2 run, after seeing only the adapter's set list.
* Phospho and pathology-count rows are not turned into gene activity (conditional or excluded); this loses the Q7 GSK3B direction and the cell-count rows by design.
* No paper was read; no read receipt is staged. Registry, ledger and current files untouched.

## 10. For the batch path

Record: this folder as research material (IT9 P2); the corrected-grammar statement "WWOX-loss seeds enter a signed-propagation engine and move scores, with exact attribution" as a method note, not a claim; the failed T2(b) and T1(d) criteria as limits of the seed sets; no registry, card or need change is proposed.
