# IT30: carried limits kept whole, and the stage rebuilt from committed inputs (S11)

Non-canonical. Not medical advice. Public edition, WWOX-DEE reference genotype class.

**Problem (IT29 verifier, finding 5-i).** `run_generation_it21.py` cut `carried_limits` at 1,600 characters. 33 proposals sat exactly at the cut; in IT21P2-0019 the cut removed the clause that restricts the HDAC5 limit ("class IIa-selective compounds NOT covered"), and the repeated text before it stayed.

**Fix.** `join_limits` keeps each distinct segment once, in first-seen order, and cuts nothing. The longest limit is now 2,701 characters; no proposal lost text (every changed row is longer or equal). Showing a long limit briefly is the interface's job, not the data's.

**S11 = S10 + that fix, rebuilt from committed inputs only.** The IT29 note that the engine directory was an uncommitted scratch one is closed: the recipe below reproduces the 994 proposals and the 220 eligible / 15 hand-overs from files in the repository plus the local catalogue cache.

```
cp -r generation_it22_p1_20261103/eng_merged <engine>        # committed engine of the IT22 incremental runs
ln -s <abs>/generation_it21_p2_20261103/results/actions <engine>/actions   # symlinks are not allowed on the release surface
LEGEND_CATALOG_CACHE=<cache> python3 -B generation_it10_p1_20261031/engine_v4/run_v4.py --out <engine> --actions generation_it21_p2_20261103/results/actions --seeds-dir generation_it22_p1_20261103/inputs_it22/seeds_p1 --reach --reach-sets Q8_expression_tiersAB   # as IT25 A1
LEGEND_CATALOG_CACHE=<cache> python3 -B generation_it21_p2_20261103/run_generation_it21.py propose --engine-dir <engine> --p1-inputs generation_it22_p1_20261103/inputs_it22 --out-dir <out>
```

About 6 minutes, 4 GB cap. Two shortcuts do **not** reproduce S10 and must not be used: a fresh `run_generation_it21.py engine` gives 974 proposals and 214 eligible (it lacks the incremental seed sets), and `eng_merged` alone gives 1,000 proposals (it lacks the IT25/IT26 Q8 re-run on the refreshed action table).

**What differs from S10 (`test_stage_it30.py`).** Same 994 proposal ids, same 220 eligible, same 15 hand-overs. `carried_limits` changes in the 33 rows that were at the cut, and `target_named_in_legend_material` goes no to yes in 10 rows: that flag is corpus-dependent (it reads the cards and rankings present in the checkout) and the checkout now holds the IT29 material. Neither moves selection.

**Local-only artefact.** The catalogue cache (`LEGEND_CATALOG_CACHE`) is not distributed; without it the engine step cannot run. What stays checkable in the public checkout: `join_limits` and the committed S11 tables (`test_stage_it30.py`).
