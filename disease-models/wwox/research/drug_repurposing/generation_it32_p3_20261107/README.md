# IT32 P3: stage S12, proposals tied to the investigation that measures their shared premise

Non-canonical. Not medical advice. Public edition, WWOX-DEE reference genotype class.

**Problem (IT31 reach table, IT32 P1).** 20 generated proposals rest on one mechanism edge, HDAC5 raises SLC2A1 output, which traces to a single muscle knockdown study (INV-16). Twelve of the 20 are eligible for hand-over, one is handed over (the 15 hand-overs are one per mechanism cluster). Nothing in the stage rows said that a single open measurement stands behind all of them; the only trace was a free-text limit.

**Change (smallest link).** `generation_it21_p2_20261103/investigation_premises_it32.tsv` maps a mechanism-chain prefix to an investigation id (curated, not inferred from names). `run_generation_it21.py` adds the column `shared_premise_investigation` to the proposals and the hand-over table. One premise, one investigation: the 20 rows do not become 20 questions.

**Before and after (`test_stage_it32.py`).** S12 against S11: same 994 proposal ids, same 220 eligible, same 15 hand-overs, every other column identical; the new column is `INV-16` on the 20 proposals whose chain starts `HDAC5 -T(+)-> SLC2A1` and empty elsewhere. This is a bookkeeping gain (a consumer can now go from a proposal to the question that decides its premise), not a change in what is proposed and not a predictive result.

**What it does not do.** No proposal is promoted or withdrawn. The premise stays conditional: the 20 proposals are not 20 independent supports, and a measurement on one compound would not by itself transfer to the others.

**Recipe** (as `../generation_it30_p5_20261105/README.md`, with the output folder `results_s12`; about 6 minutes, 6 GB cap; needs the local catalogue cache `LEGEND_CATALOG_CACHE`, which is not distributed). The public checkout can run only `test_stage_it32.py` and the helper tests in `generation_it21_p2_20261103/test_generation_it21.py`.
