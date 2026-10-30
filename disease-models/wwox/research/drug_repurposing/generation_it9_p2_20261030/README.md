# IT9 P2: a seed-based generation engine that uses the WWOX-loss inputs (function and sensitivity proof)

Scientist-b, 2026-10-30. **Exploratory, computational. Not medical advice. Proves that the method runs, reads its seeds and reacts to them; it does not prove that any proposed
compound would help anyone** (no compound-response measurement in a WWOX-deficient system exists to test that against; IT6 P3, IT7 P0a, IT8 P4). Reference genotype class: a WWOX-DEE genotype class; no individual-level record.
Nothing here edits a registry, ledger, current file, card or need. Pre-registration: `PRE_REGISTRATION.md` (committed before any run; Amendments 1 and 2 are disclosed there with what had been seen).

## 1. Decision (first)

| Question | Answer |
|---|---|
| Is there a simplest method that really uses the selected WWOX inputs to propose compounds? | **Yes: signed K-hop propagation of the seed vector over the IT7 signed network, scored against each compound family's signed target actions** (`seed_engine.py`). Seeds keep level and direction; uncertain direction runs as two conditional arms with an exact range. Output per compound: compatible action (opposes or mimics), conditional flag, and per-seed contribution. |
| Do the seeds enter the computation (T1) and does the direction logic behave (T5)? | **Yes.** T1 passed on 7 of 8 seed sets, T5 on 8 of 8 (the failure of T1 is one set whose only defined seed is inert, section 4). Zero seeds gives exactly zero; scores scale linearly; per-seed contributions sum to the score to 1e-17; flipping all signs negates every score (Spearman -1.0); flipping one seed changes exactly the compounds it influences. |
| Is the result seed-specific (T2)? | **Mostly yes against random seeds, not demonstrated for signs.** Against 1000 degree-matched random seed sets the median Spearman with the real ranking is 0.03 to 0.17 and the top-100 overlap median 0 to 2 (criterion: 0.50 and 20) in every set under both null variants. The registered sign-shuffle criterion is **not met** in 3 sets (all defined seeds share one direction, the shuffle is the identity). Registered T2 verdict: PASS in 5 of 8 sets, FAIL in 3 (section 4). |
| Identity or answer-in-construction (T3)? | **No identity driver found; one leakage case caught.** Firewall enforced at load (tested). Rankings are stable across catalogue source groups (ChEMBL-only vs all rows rho 0.995; non-ChEMBL vs all 0.994) and across the normalisation choice (0.99998). The leakage test flagged dichloroacetate in the Q2 and provisional sets (RECOVERED_ONLY_VIA_OWN_TARGET): its position is entirely its own target PDK1 being a seed, and flips from the 99.98th to the 0.02nd percentile with the assumed PDK1 direction. |
| Does it add information relative to the direct target search (T4)? | **Depends on the seed set, and mostly yes where the seeds are not themselves drug targets.** Net-only proposals that the direct search cannot give and that exceed degree-matched chance (z > 3): Q5 expression 82/100 (52 under the in-degree null), Q4 protein 88/100 (30 under the in-degree null), Q2 expression 66/100 (86 by the z-ranking in the in-degree null, 22 by raw Q, so raw-Q ranking depends on the null); **none** (NONE) for Q1, Q3 and Q4 expression, and for the provisional set. Rank correlation with the direct search is about 0 (-0.0003 to 0.012) because the direct search is almost empty (4 to 133 families per set). |
| Is the signature route informative? | **Only for Q3** (rho progenitor-like vs neuron-like 0.275 and 0.25 against random-readout p95 0.23; the ISR direction is unresolved so both arms are conditional, and this is a shared transcriptional axis, not WWOX evidence). Not informative for Q1, Q2, Q4, Q5 and the provisional set. |
| External resources? | Trial results in section 6: nothing to adopt; Open Targets reproduces what the catalogue already holds; MATRIX scores still carry no licence. |

What this means for the mandate: the grammar problem named by IT8 P4 (condition 2b) is solved in the narrow sense that the WWOX data now enter as seeds and demonstrably move the scores. Whether the
resulting proposals are of any use is **not** established and cannot be from these tests.

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
| Examined with a non-zero score in some arm (per set) | 2,190 (Q1) / 4,935 (Q2) / 4,962 (Q3) / 2,859 (Q4 expr) / 2,927 (Q4 prot) / 5,187 (Q5 expr) / 2,979 (Q5 prot) / 5,709 (provisional) |
| Signature route: families with a neural-lineage LINCS signature (phase I, via catalogue structure key) | 848 (421 with both context classes) |

2,381 distinct signed target symbols; 1,887 (79 percent) are in the graph. The unmapped list is `results/unmapped_targets_*.tsv` (alias errors can be checked there; not audited against HGNC here: UNVERIFIED).

## 4. Test results (criteria fixed in `PRE_REGISTRATION.md`; `results/tests_summary.tsv`, one row per set and null variant; `results/tests_<set>[_indeg].json`)

Eight seed sets: the PROVISIONAL set (15 units from the IT7 P1 subnetwork, used to build the engine before P1 existed) and seven P1 sets. Two null variants: registered total-degree matching and the Amendment 2 in-degree matching. 1000 nulls per test.

| Set (units, defined) | T1 | T2 (a,b,c) | T3 identity | T4 (raw Q / Z) | T5 |
|---|---|---|---|---|---|
| provisional (15, 6) | pass | **FAIL**: (b) shuffle 0.92 (5 up, 1 down) | pass | NONE / NONE | pass |
| Q1 protein (1, 1) | pass | pass (b not testable, 1 seed) | pass | NONE / NONE | pass |
| Q2 expression (17, 15) | pass | **FAIL**: (b) degenerate, all defined seeds up | pass | ADDS / ADDS (in-degree null: LIMITED / ADDS) | pass |
| Q3 expression (17, 1) | pass | pass (b not testable) | pass | NONE / NONE | pass |
| Q4 expression (3, 2) | pass | pass | pass | NONE / NONE | pass |
| Q4 protein (4, 4) | pass | **FAIL**: (b) degenerate, all down | pass | ADDS / ADDS | pass |
| Q5 expression (3, 2) | pass | pass | pass | ADDS / ADDS | pass |
| Q5 protein (2, 1) | **fail (d)**: the only defined seed (AIF1) is not in the network and is no compound's target | pass | pass | NONE (0 proposals) | pass |

Reading the failures as registered, not rescued (Amendment 2.2 and 2.3): a set whose defined seeds all share one direction cannot show that the sign matters through the shuffle; T5(b) (all-sign flip, exactly negated) is the sign test that remains and passes everywhere. The provisional set fails T2(b) with 5 up and 1 down because the single down seed (PDK1, level 0.10) hardly moves the ranking (flipping it keeps the top-100 identical). Q5 protein has nothing to propose.

Other numbers: seed-specific (|z| > 3 against the random seed sets) families per set 0 (Q1), 158 (Q2), 0 (Q3), 179 (Q4 expr), 100 (Q4 prot), 84 (Q5 expr), 33 (Q5 prot), 54 (provisional) of the non-zero families. The NET-Z arm fails the registered Spearman criterion in every set under the total-degree null (median 0.65 to 0.95) and passes the top-100 criterion in nearly all: its bulk is ordered by -mean/SD for the unconnected families, a deterministic structure shared by real and null; the top end is what matters and is specific. Seed-free baseline: the Spearman between |Q| and the reach of an all-ones seed is 0.09 to 0.39, i.e. network position explains part, not most, of the ranking.

Reproduce: `python3 run_battery.py --seeds-dir seeds_p1 --extra seeds_provisional.tsv --actions results --out results` (about 9 min on 4 shared cores).

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
| LINCS (GSE92742 level 5) | `seed_sig_arm.py` | run on all 8 sets (section 1, signature row). SigCom LINCS metadata API answered HTTP 200; not queried further (the local level 5 extract is the complete form of the same data). |

## 7. Running it on a declared universe (for P3)

```
export LEGEND_CATALOG_CACHE=<root>/disease-models/wwox/research/drug_repurposing/catalog/cache
python3 seed_engine.py build-actions --out results                       # only if the catalogue changed (5 s)
python3 p1_adapter.py --p1 <P1 folder> --out seeds_p1                    # seed tables per question and level
python3 seed_engine.py run --seeds seeds_p1/Q2_expression_tiersAB.tsv --actions results --label q2 --out results --universe universe.tsv
python3 seed_engine.py tests --seeds seeds_p1/Q2_expression_tiersAB.tsv --actions results --label q2 --out results [--match indeg]
python3 seed_engine.py explain --seeds ... --actions results --family FAM:CAT:CHEMBL306823
python3 seed_sig_arm.py --seeds ... --geo <GSE92742 dir> --cache <dir with extract.npy> --catalog ../catalog/catalog.jsonl.gz --label q2 --out results
```
`--universe` takes family ids (one per line, or a TSV with a `family_id` column). `funnel_<label>.json` reports catalogued, resolved-identity, usable, in-graph, declared-universe, examined and non-zero counts. `proposals_<label>.tsv.gz` holds, per examined family with a non-zero score, Z_ind_robust, Z_full_robust, Q (full, indirect, direct, both conditional arms), the compatible action, the uncertain-seed mass, direct-hit and WWOX-regulator flags and proximity. `contributions_<label>.tsv` names, per family and seed, the direction of the seed, the hop-0 and hop 1-3 contribution and the target carrying most of it (shown for the top and bottom 100 families by Z and for direct hits; use `explain` for any other family). Uncertain-direction seeds are shown in their + arm; the sign of their contribution flips in the - arm.

## 7a. Reserved-row check (Amendment 3; `reserved_check.py`, `results/reserved_check.tsv`)

Of the 17 reserved P1 rows, 7 are gene-level (WWOX, LDHA, CACNA1G, PANX1, GFAP, MYC, CTNNB1); the other 10 (GO, STATE:) have no gene representation and cannot be checked. **No reserved row is in any seed table.** Shared genes (a reserved response on a gene that is also an observed seed): WWOX (Q1), LDHA (Q2), GFAP (Q5 protein); these are different observations (loss state vs intervention response), reported, not leakage. The ethosuximide/T-type gene CACNA1G is a seed in no set; the 4 or fewer examined families acting on it rank 328 to 2,837 (of 2,892 to 5,187 proposals): the held-out answer is not recovered and is not claimed to be. Nothing is fed back.

## 8. Files

`PRE_REGISTRATION.md` (with Amendments 1 and 2) · `seed_engine.py` · `p1_adapter.py` · `provisional_seeds.py` · `seed_sig_arm.py` · `run_battery.py` · `summarize_tests.py` · `external_trials.py` · `reserved_check.py` · `test_seed_engine.py` (positive checks on a hand-computed graph) · `seeds_provisional.tsv` · `seeds_p1/` (7 sets, manifest, adapter counts) · `results/` (family tables, proposals, contributions, funnels, tests JSON and summary, null summaries, unmapped targets, signature arm, external trial).

## 9. UNVERIFIED and honest limits

* P1 was merged final after the runs; regenerated seed tables are identical (checked by diff). If P1 changes again, rerun `p1_adapter.py` and `run_battery.py`.
* Target symbols were not audited against HGNC (21 percent are not in the network: absent genes or alias mismatches, not distinguished). Mouse seeds rely on HGNC's single-link ortholog field.
* Equal level weights; tier A and B seeds mixed (human neural and non-human neural); a set (e.g. Q2 expression) contains both a gene seed and a process seed that includes it, which double-counts that gene.
* Tests prove function and sensitivity on 7 small seed sets (1 to 17 units) and one provisional set; with so few seeds the sign shuffle has no power in 4 of 8 sets.
* The provisional-set results were seen before Amendments 1 and 2; the P1-set runs used the amended criteria but the amendments were motivated by the first P1 run (disclosed in Amendment 2).
* No paper was read; no read receipt is staged. Registry, ledger and current files untouched.

## 10. For the batch path

Record: this folder as research material (IT9 P2); the corrected-grammar statement "WWOX-loss seeds enter a signed-propagation engine and move scores, with exact attribution" as a method note, not a claim; the failed T2(b) and T1(d) criteria as limits of the seed sets; no registry, card or need change is proposed.
