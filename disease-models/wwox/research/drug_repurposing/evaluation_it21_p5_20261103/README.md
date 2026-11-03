# IT21 P5: does WWOX-specific information add anything beyond direct target search? (2026-11-03)

## 1. Decision (first)

**No advantage**, at the level the generator itself can be tested: a seed set with the WWOX genes replaced by genes of the same hub size produces seed-specific output that the real set does not exceed.
Not "no information": the test has a floor (below) and the one place where the WWOX arm sits at the edge of the decoys is partly circular.

* **Cause.** The seed-specific filter (z above 3 in three degree-matched nulls, plus the reach null) is a test against *random genes of the same degree decile*. A WWOX seed set passes it, but so does a hub-sized set of unrelated genes. Against decoys matched on the registered covariate (coarse decile, `coarse`) the real sets do stand out (empirical p 0.02 to 0.05 for Q5, Q6 expression, Q6 protein); against decoys matched on fine degree (`deg`) or on F5-admissible reach (`reach`), pooled, they do not (p 0.12 to 0.22 for seed-specific rows, 0.14 to 0.33 for eligible rows, 0.25 to 0.62 for hand-overs). Taken one design at a time the picture is the same with one exception: Q5 against `deg` alone has p 0.024; against `reach` alone p is 0.12 to 0.41. What the filter detects is that WWOX seeds are hubs, not that they are WWOX.
* **At the level of the qualified outputs the arms cannot be compared**: the generator has 0 qualified outputs (13 handed over, none qualified; P3b qualified 0 of 10 path-B proposals as `QUALIFIED_HYPOTHESIS`). What can be compared is the count of seed-specific, eligible and handed-over rows: indistinguishable from the fine-matched decoys in 5 of 5 sets.
* **Reopening condition.** Any one of: (a) a seed set whose count exceeds the 95th percentile of the `deg` and `reach` decoys in at least 3 of 5 sets (criterion C1 below) after a seed table update (D1 of the P2 README: NRF2, snRNA, glia rows) or a role-resolving measurement; (b) a qualification record that distinguishes a decoy-matched proposal from a WWOX-seeded one by a measured, WWOX-system datum; (c) a decoy design that holds biological coherence fixed (co-regulated gene sets of the same size) and still falls below the real set. Until then a WWOX-seeded proposal is a *hypothesis from a hub's neighbourhood*, to be qualified on its own merits.
* A retrospective analysis and a synthetic perturbation test the properties of a method. This one shows nothing about prospective therapeutic benefit, and "no advantage" is not evidence that any listed compound does not work. Not medical advice. The subject is the WWOX-DEE reference genotype class.

The rule below was written into `compare_arms.py` (`decide()`) before the full run. A 3-replicate pilot on two sets (Q5, Q6) had been looked at before the criteria were fixed; it already showed fine-matched decoys producing as many rows as the real sets, so the thresholds are not blind to the outcome.

## 2. The comparison and what each arm removes

IT20 compared a set with its own filtered subset (WWOX-qualified is a strict subset of external-only). This package compares different things.

| Arm | What it keeps | What it removes | Difference measured |
|---|---|---|---|
| A1 direct search on need targets, external-only | the IT20 arm E over the 23 needs (3,331 associations, 622 families, 46 need targets); direct hits on the seed genes | every WWOX observation | the reference: what a plain target list returns |
| A2 mechanistic path, WWOX seeds | P2 output: 992 seed-specific rows, 141 eligible, 32 clusters, 13 handed over (reproduced exactly by `compare_arms.py`, control in `summary_p5.json`) | nothing | what the path adds to A1 |
| A3 same generator, WWOX seed identity removed | same engine (v4), same refreshed compound side, same three IT10 nulls plus the IT11 reach null, same selection and hand-over rules; direction, level, readout level, guard tag, number of units | the identity of the seed genes. Three designs, 40 replicates each per set, 5 sets: `coarse` (random gene of the same total-degree decile, the engine's own null), `deg` (one of the 30 nearest genes in degree), `reach` (one of the 30 nearest in F5-admissible reach). A seed gene that is not a network node (KCNA2) is omitted from its decoys | what A2 has that a seed set of the same size, sign and hub size does not |
| A4 phenotype-first | the 7 interventions with a recorded WWOX-system result (IT10), and the P3b units | the graph | recovery of interventions already tested in a WWOX system, against decoys |

Replicate 0 of the decoy runner is the real set; its seed-specific list equals the committed P2 list in all 5 sets (51, 87, 286, 420, 148 rows; `decoy_arm.py control`).

## 3. Results

Decoy statistics are over 40 replicates per design and set. p is the one-sided empirical p that a decoy is at least as large as the real set (add-one rule, so the smallest possible is 0.024). Full tables: `results/counts_vs_decoys_p5.tsv`, `results/criteria_detail_p5.tsv`.

| Decision criterion (fixed before the full run) | Result |
|---|---|
| C1 real seed-specific count above the 95th percentile of `deg`+`reach` decoys in at least 3 of 5 sets | 0 of 5 (pooled p 0.12 to 0.22); real 51/87/286/420/148 against decoy medians 15/23/127/128/20 and 95th percentiles 146/146/405/525/210 |
| C2 at least half of the real eligible rows are not generic (the same compound and arm occurs in at most 5 percent of decoys in both fine designs) | 37.6 percent are not generic (88 of 141 recur in more than 5 percent of the decoys of at least one fine design). Rarity of a single compound among decoys is weak evidence anyway: every decoy produces its own, equally rare, list |
| C3 share of real seed-specific rows beyond direct search above the decoy 95th percentile in at least 3 sets | 0 of 5. 868 of 992 real rows (87.5 percent) are beyond direct search, and so are 82 to 100 percent of decoy rows |
| C4 share of rows whose main target is a need target above the decoy 95th percentile in at least 3 sets | 1 of 5 (Q4, p 0.06). 78 of 992 real rows (7.9 percent) |
| Rule | informative = C1 and C2 and (C3 or C4); no advantage = neither C1 nor C2; else inconclusive. Result: **no advantage** |

### 3.1 Proposals added beyond direct search, and relations truly new

* Beyond direct search (not a direct hit on a seed gene, not in arm E, main target not a need target): 868 of 992 real rows. Any seed set yields them; WWOX identity does not change the share (decoys 82 to 100 percent). Only 5 rows are direct hits on a seed gene, 119 are in arm E (622 families), 211 are linked to a need by the catalogue.
* The 13 hand-over rows: 12 beyond direct search; 1 (AZ960 / JAK2) sits in arm E and on a need target. Routed check (`repurposing_search.py compound`, `novelty_it21.py --registries`, never a grep of the two registries; `results/novelty_handover_p5.tsv`): 11 of 13 are named in no card or unit, neither compound nor axis, and reach no need through the catalogue's target rows; 2 (nanatinostat / HDAC5, AZ960 / JAK2) are new compounds on an axis LEGEND holds; 2 (CEP-11981, AZ960) reach a need through other targets of the compound (GSK3B derepression, neuroinflammation). "New to LEGEND" is a perimeter of this module, never a literature claim. **P8-fix correction:** 'new compound' above means new to cards and units. AZ960, CUDC-101, nanatinostat, GSK343 and CGI-1746 are earlier LEGEND threads (IT9 P3 `excluded.tsv`, IT9 P4c-d `excluded_selection_p4c_d.tsv`, IT9/IT10 candidate lists); the P2 hand-over now carries that earlier source and reason per row. **Stale input, not re-run:** `results/decoy_rows.tsv.gz` (replicate 0 and the decoy replicates) was computed on the P2 action table before the P8-fix glue/conflict sign guard; replicate 0 therefore lists 12 rows (the CRBN glue families, 4 families x 3 sets) that the corrected P2 list (980 rows) no longer has, and `test_decoy_file_replicate_zero_equals_p2_list` fails until the decoy arm is re-run (about 70 minutes, command in section 'Re-run'). The comparison with decoys is unchanged in kind; its numbers are those of the 992-row list.

### 3.2 Surviving qualification, and errors that eliminate proposals

`results/qualification_funnel_p5.tsv`, `results/error_classes_p5.tsv`.

* P2 funnel: 992 seed-specific, 309 with an identity and a small-molecule modality (upper bound: the first blocker met is counted), 141 eligible (32 clusters), 13 handed over, **0 qualified** (no P4-type run exists for the 13; "0" is the closed status vocabulary plus no run, not a negative finding).
* Earlier engine-derived records (IT9 to IT11, 32): 6 KEEP as a mechanistic experiment, 3 CONDITIONAL, 18 DROP, 5 INCONCLUSIVE. P3b (path B, compound-to-WWOX with authored handles, not this generator): 10 proposals, 5 qualified, 0 `QUALIFIED_HYPOTHESIS`, 2 KEPT_CONDITIONAL.
* Eliminated, by class (P2 counts, rows): identity 662 (DGIdb-only twins, no ChEMBL id); level 219 of the 223 guard withdrawals (139 republished copies that do not carry the level, 80 class-level records written above the gene); context 48 (reach null does not confirm) and 34 (cluster already examined); role 74 (arm has no stated benefit hypothesis); pharmacology 21 (modality) and 100 (active moiety uncertain); earlier decision 12. Most of these are properties of the catalogue and of the role table, not of WWOX.
* **The guards are not WWOX-specific either.** On the same engine with guards off (the IT9 action table rebuilt on today's catalogue; 15 replicates of `deg` and `reach`), the real sets lose 223 of 1,202 rows (18.6 percent; 15, 5, 66, 105, 32 by set, reproducing P2), and decoys lose a median 4 to 40 percent by set and design (`results/guards_effect_p5.tsv`). The guards remove a class of catalogue error wherever the generator looks.

### 3.3 Dependence on hubs, shared origins and frequent compounds

* Hubs. The real rows concentrate on few main targets (HDAC5 20 of 51 in Q2, BTK 57 of 87 in Q4, NR3C1 80 of 420 in Q6 expression); decoys concentrate on others (EGFR, NR3C1, KIT, TYK2, PTGS2). In the `reach` design 16 percent (Q5) and 38 percent (Q6 expression) of real rows sit on a main target that is also the main target in at least a quarter of the decoys (`results/hub_dependence_p5.tsv`): the hubs of the network, not of WWOX.
* Shared origins. Q5 rests on two mouse transcript contrasts (null hippocampus, P47T cerebellum), Q2 on one derivation counted once, Q4 and Q6 on one human observation each. Decoys have no origin: this cannot be tested against them. IT10/IT11 origin sensitivity moves no member of the top 8 (`generation_it10_p1_20261031/results/origin_sensitivity.tsv`).
* Frequently selected compounds. Across the five real sets 57 of 871 selected families are `opposes` in one set and `mimics` in another (6.5 percent), against a median 16.5 of 619 (2.7 percent) for `reach` decoys and 0 of 215 for `deg`: sign instability is not smaller for the WWOX seeds. The mean Jaccard overlap of the selected sets between the five seed sets is 0.013 (decoys 0.00 to 0.006 median, 95th percentile 0.02 to 0.08): compounds are not shared much across sets, as expected of distinct neighbourhoods.

### 3.4 Sensitivity to assumptions, context and sign

* Role (H_HARM 556, H_PROTECT 436): no question has a sourced role, so every row is conditional on an unknown sign. The sign changes which compounds are proposed (one arm raises the seed readout) and the two arms are opposite experiments. Nothing in the WWOX seeds resolves it.
* Null covariate. The reach null removes 1 to 18 percent of real rows (Q6 protein 148 to 121; Q6 expression 420 to 409); decoy `reach` removal is similar. The registered null alone separates real from random (C1 `coarse`), the matched ones do not: the result depends on the covariate, as IT11 found for Q6 protein.
* Context. Expression and protein versions of Q6 (one seed, MYC) give different lists; neither is the neural-cell measurement the role needs.
* The only measure where the WWOX arm lies at the edge of the decoys is re-finding compounds that LEGEND already decided or knows: 37 real rows (empirical p about 0.02 to 0.10 per set under `deg`). That is circular for 26 of them (the IT9 to IT11 records were produced by this engine on these seeds). For the 11 reference records (known WWOX-tested or control compounds; lithium appears as a Q6 `mimics` row) p is 0.05 to 0.07 under `deg` and 0.07 to 0.46 under `reach`: a hint, not a result (`results/phenotype_first_recovery_p5.tsv`: lithium is a seed-specific row in 28 percent of Q6 `reach` decoys).

### 3.5 Hypotheses leading to distinguishable experiments

The 13 hand-over rows rest on **4 role-resolving experiments** (one per question: HIF protein, GABAergic marker versus composition, cytokine protein with glia markers, matched-maturity radial-glia MYC) and 13 distinct main targets. Step 1 for every row is one template (compound versus vehicle in the WWOX-deficient system and its corrected counterpart, with a genetic perturbation of the target), which does not separate a WWOX-specific mechanism from a direct effect on the target. So the distinguishable content is the 4 step-0 measurements, and these are needed whether the compound comes from the WWOX path or from a decoy path (`results/experiments_p5.tsv`). Direct search needs the same step 0.

## 4. What the design cannot say

* Decoys are unrelated genes of the right size, sign and hub size; the real seeds are biologically coherent (co-regulated genes). A coherence-matched decoy was not built (no external data and zero spend). If coherence adds signal, this design under-credits it. This is reopening condition (c).
* The fine decoys are drawn from the 30 nearest genes; with 40 replicates the smallest p is 0.024, and a design with 100 replicates would sharpen the pooled tests but not the direction.
* `eligible` for decoys uses the P2 rules H1 to H4 and H8 with a per-set cluster key; the cap of 3 per question and hypothesis is applied per set (control on the real rows pooled by question gives 141, 32, 13).
* The 74 rows with no stated benefit hypothesis, the identity blocker, the role table and the hand-over cap are P2/IT10 design choices and are held fixed.
* Not run: a prospective test, a decoy built from other diseases' seeds, qualification of the 13, a refresh of the seed table.

## 5. Files and commands

| File | What |
|---|---|
| `decoy_arm.py` | `make`, `run`, `control`: the decoy designs and the engine runs (reuses `engine_v4`, the P2 action table, the IT9 seed tables) |
| `compare_arms.py` | per-replicate metrics, criteria, `decide()`, the tables; `run --decoys results/decoy_rows.tsv.gz` |
| `side_tables.py` | `novelty` (routed tools), `funnel`, `errors`, `experiments`, `guards` |
| `test_p5_it21.py` | tests (decision rule, decoy construction, control reproduces P2, committed results) |
| `results/` | `decoy_rows.tsv.gz` (seed-specific rows of 605 runs), `decoy_rows_guards_off.tsv.gz`, `summary_p5.json`, `counts_vs_decoys_p5.tsv`, `criteria_detail_p5.tsv`, `per_replicate_p5.tsv`, `real_rows_vs_decoy_frequency_p5.tsv`, `hub_dependence_p5.tsv`, `cross_set_and_sign_p5.tsv`, `blockers_real_vs_decoys_p5.tsv`, `phenotype_first_recovery_p5.tsv`, `novelty_handover_p5.tsv`, `qualification_funnel_p5.tsv`, `error_classes_p5.tsv`, `experiments_p5.tsv`, `guards_effect_p5.tsv` |

```
export LEGEND_CATALOG_CACHE=<root>/disease-models/wwox/research/drug_repurposing/catalog/cache
python3 decoy_arm.py run --work <scratch> --out results/decoy_rows.tsv.gz --k 40 --workers 4     # about 70 minutes, MemoryMax 8G
python3 decoy_arm.py control --rows results/decoy_rows.tsv.gz
python3 compare_arms.py run --decoys results/decoy_rows.tsv.gz --out results --k 40
python3 side_tables.py all ; python3 side_tables.py guards
python3 test_p5_it21.py
```
