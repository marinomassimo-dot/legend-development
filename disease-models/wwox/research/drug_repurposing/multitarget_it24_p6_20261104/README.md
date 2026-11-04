# IT24 P6: does a multi-target view see what the single displayed chain hides? (feasibility and first comparison, 2026-11-04)

Non-canonical. Not medical advice. Read-only over the IT22 engine outputs (`generation_it22_p1_20261103/eng_merged`, final stage table `results_p4`); no engine, table or ranking was changed.

## What was found first (it changes the question)

The engine score is already a signed sum over seeds and over every admissible walk from **every** target of a family (`dispose_it10.explain`); only the *displayed* chain is one walk. So a compound is not
"credited through one target" in the calculation; the target structure is hidden in the presentation. The useful comparison is therefore: decompose the existing calculation by target and ask what the single chain conceals.

## Method (`multitarget_feasibility_it24.py`)

Per seed set and family: net contribution per main target (the target of each seed's strongest walk, so a lower bound on the targets involved), read in the oppose orientation (H_HARM) and flipped for mimic (H_PROTECT).
Kinds: SINGLE_TARGET; MULTI_POSITIVE (two or more targets net-favourable; overlap of the seeds they reach: REDUNDANT / PARTLY_OVERLAPPING / COMPLEMENTARY); CONFLICT_BETWEEN_TARGETS (one target favourable, another net-contrary, in ONE compound);
NO_POSITIVE_TARGET. No score was added: favourable and contrary targets stay separate and no net number is formed.
Output: `target_decomposition.tsv` (all seed sets, both orientations), `proposals_decomposed.tsv` (the 1,000 final proposals), `summary.json`.

## Results

| Measure | Value |
|---|---|
| Final proposals (1,000): SINGLE_TARGET / MULTI_POSITIVE / CONFLICT_BETWEEN_TARGETS | 902 / 66 / 32 |
| Conflicts between targets of one compound whose row-level `contrary_seed_share` is at most 10 percent | 32 of 32: the existing contrary-evidence column never shows them |
| Hand-overs (16): single / multi-positive / conflict | 10 / 4 / 2 |
| Hand-over multi-positive | pracinostat (HDAC3, HDAC5), LGH-447 (PIM1, PIM2), ravoxertinib (MAPK1, MAPK3), tretinoin (NR2C2, RARB), all COMPLEMENTARY by the seeds reached; PIM1/2 and MAPK1/3 are paralogs, so independence of those pairs is NOT established |
| Hand-over conflicts | sorafenib (H_PROTECT: CDK8, CDK19, ZHX2 favourable, BRAF contrary); SAR-407899 (ROCK2 favourable, ROCK1 contrary; paralogs) |

## Reading

- A target-level conflict was invisible before for every one of the 32 rows. For two hand-overs it is now a stated limit (sorafenib, SAR-407899); it does not change eligibility because these were decided on other grounds.
- Multi-positive structure exists but is small (66 of 1,000) and half of the hand-over cases are paralog pairs; no row is promoted for having more targets (no target-count reward).
- This is a coverage and presentation gain. It is not a prediction of benefit and not a measure of accuracy.
- Limits: main-target only (a lower bound); no measured potency or exposure is used in the decomposition (typed pharmacology stays in the IT22 attribution columns); the comparison against a true multi-protein docking or profile method needs a source that is not available (IT23 CANDO result).

Reproduce: `python3 multitarget_feasibility_it24.py --eng ../generation_it22_p1_20261103/eng_merged --out .`
