# IT25 A1: stage tables regenerated with the source checks, F1 and F2 (results_s6)

Non-canonical. Not medical advice. Nothing here is a finding; a hypothesis stays conditional and `qualified = no`.

## What was done
1. **Control first.** `run_generation_it21.py propose` on the committed engine output (`generation_it22_p1_20261103/eng_merged`, amended inputs `inputs_it22`) with the CURRENT code reproduces `results_s5` exactly for the hand-over, the mechanism clusters, the carried decisions and the summary; only the `attribution_*` columns differ, and that is F1. (`--no-v1` is NOT the control for the committed tables: it switches the identity bridge off and reproduces the IT21 P2 tables.)
2. **Exclusions.** Four pairs from `source_check_it25_a2_20261104` were added to `generation_it21_p2_20261103/source_exclusions_it24.tsv` (the file keeps its IT24 name; its `ref` column names the check): sorafenib and regorafenib to ZHX2 (an alias artefact), pictilisib and buparlisib to PIK3C3 (the primary paper states they do not inhibit Vps34). Three further pairs are UNKNOWN and are NOT excluded: a pair is withheld only when a source check has read and named it. Action table: 19,912 to 19,908 pairs; the eight IT24 pairs were already out.
3. **Engine re-run** on the refreshed table: `run_v4.py --out DIR --actions DIR --seeds-dir inputs_it22/seeds_p1 --reach --reach-sets Q8_expression_tiersAB` (about 10 min, MemoryMax 8G). Six of eight `candidates_Q*.tsv` are byte-identical to `eng_merged`, so the engine is deterministic. Q2 changes as expected; Q4 differs only in the `NPY_SIGN_CONTESTED` guard tag (a tag the committed Q4 engine files predate; scores are the same). Across all 39 contribution files, the rows that differ belong to six families and no other (`engine_effect_it25.tsv`). The engine directory itself is not committed (regenerable by the command above, 3.2 MB).
4. **F2** (IT24 reverse-test item): `run_generation_it21.py` now reads a blank `max_phase` from the sibling family the identity bridge names, and writes `max_phase_source` (`own`, `sibling_family`, or blank). 108 of 1,000 rows gained a phase; annotation only.
5. **propose** with the production path (F1 and F2 on) wrote `results_s6/`.

## Result (`stage_diff.tsv`, `stage_diff_summary.json`)
| | S5 | S6 |
|---|---|---|
| proposals | 1,000 | 996 |
| hand-overs | 16 | 15 |
| eligible | 216 | 215 |

* **Left the table (4):** sorafenib (the Q2 hand-over IT21P2-0035) and regorafenib (Q2), pictilisib and buparlisib (Q6, never eligible). Their sign rested on a listing row, not on a measurement. Sorafenib leaves the hand-over and nothing replaces it.
* **Moved (2):** panobinostat z_reach 2.93 to 3.16 and idronoxil 2.78 to 3.38, both above the reach convention of 3, because the unsupported contrary signs from the IT24 P1 check were withheld. This is a threshold crossed by REMOVING data, not new evidence for either compound. Panobinostat becomes eligible but sits in the cluster of pracinostat, which already holds the slot; idronoxil is still blocked, now by `identity_not_resolved` (the G-SRS trial returns a firm structure for it, but that route is not consumed by the generator).
* **F1:** assessable attribution states rise from 247 to 711 rows; WEAK_ATTRIBUTION rows from 7 to 27. No blocker and no eligibility changes through attribution.
* **F2:** 108 rows gain a phase from the sibling family; no selection changes.
* No ranking position and no dashboard text reads these tables, so none changed.

## Limits
* S6 is one regeneration by one producer; the independent check of the exclusions is the primary-source reading in A2, itself abstract-level for five of the papers.
* The `NPY_SIGN_CONTESTED` tag difference in Q4 is a pre-existing inconsistency between the committed Q4 engine files and the current guards; it moves no score.
* Downstream scripts that still read `results_p4` (`freeze_current_method.py`, `harm_context_it23.py`, `reproduce_ecKG_wwox.py`, the IT24 P10 scripts) are frozen on purpose and were not switched.

Reproduce the diff: `python3 stage_diff_it25.py`. Tests: `python3 test_stage_it25.py` (7), and `generation_it21_p2_20261103/test_generation_it21.py` (45) still pass.
