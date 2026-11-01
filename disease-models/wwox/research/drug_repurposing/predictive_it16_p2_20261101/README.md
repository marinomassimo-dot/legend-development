# IT16 P2: can the module's intervention priority be scored against an outcome outside the module?

Non-canonical research material; not medical advice; computational, no benefit claim. Design: `PRE_REGISTRATION.md` (written before the run). Tool: `predictive_it16_p2.py report|evaluate` (offline; numbers in `results_report.json`, input SHA-256 inside). Dated outcomes: `outcomes_it16.tsv` (7 rows, PubMed publication dates).

> **IT17 P3 status note (2026-11-01): this IT16 analysis is a DESCRIPTIVE result, not a prospective test.** The pre-registration above is unchanged. Two defects of the scorer were verified: (a) it reads the live ranking tables, not an immutable snapshot (the 2026-10-29 commit held 30 units, rules R1 and no `member_evidence.tsv`; only the order of the 8 selected units is exact, the 69-unit pool, B1/B2 and tested flags are later); (b) it counts any published perturbation as a hit without separating result (favourable, null, contrary, undeterminable), endpoint and direction. Freeze, outcome semantics and a measured task: `../evaluation_it17_p3_20261101/README.md`.

## Result (denominators stated)

| Measure | Value |
|---|---|
| Pool / selection | 69 units; general selection = 8 |
| Selection members with a WWOX-system result already on record | 7 of 8 (all 7 units that have one) |
| Baseline B1 "list what is already tested" top 8 | the same 7 plus one arbitrary unit (62-way tie at the cut; U01 by id order); overlap with module top 8 = 7 of 8 |
| Module member not chosen by B1 | U25 apinocaltamide (no WWOX-system result; outside-WWOX mouse precedent; stated reason: first test of a coherent target hypothesis) |
| Kendall tau of module order against B1 order | 0.14 (order differs; the order is the module's group rule, not outcome-driven) |
| Context-blind B2 (outside-WWOX assertions) overlap with module top 8 | 2 of 8 |
| Generated proposals (engine output) in the pool / in the top 8 | 33 / 0; with any WWOX-system result: 0 |
| Origins behind the 7 tested units | 6 distinct papers (lithium and ethosuximide share one); 4 controlled perturbations, 2 case reports (ketogenic diet, vigabatrin), 1 paper not a perturbation of the unit by title (A51: attribution from the card family, not re-verified) |
| Results dated after the ranking's freeze (2026-10-29) | 0; PubMed entry-date census 2026-10-29 to 2026-11-01 for WWOX: 0 records |
| Pool defined by outcomes | yes: 7 of 7 tested units entered the pool through their own paper |
| Retrospective split (dev up to 2021, eval 2022 on) | dev 3 units; eval 4 units from 2 controlled-perturbation origins; invalid for prediction (pool built from the eval papers) |
| Units with no result kept as "no result" | 62 untested; the 4 units that carry a WWOX-system null/harm assertion are all among those that have a result, none inferred from absence |
| Class-level-only units (no transfer to members) | 9 of 69 have class rows only; 32 units have no member rows |
| Cost | 7 curated rows, 1 script of about 160 lines, no network in the script; one PubMed census by hand |

## What is shown
- The selection reproduces the trivial rule B1 on 7 of 8 places. What the WWOX-informed rules add to the choice is one inclusion (U25) and the order within the set. Hence for hypothesis selection the module's added value over "list what has been tested" is, on the measurable part, one unit and an ordering that cannot be scored.
- None of the 33 engine-generated proposals reaches the top 8; the generation step has not influenced the selection.
- The retrospective test cannot be read: every tested unit exists in the pool because its paper was read, so the "7 of 8 against random p = 7e-9" figure is a restatement of how the pool was built and is not evidence of prediction.

## What is not shown
- Predictive accuracy, enrichment or benefit: independent post-freeze outcomes are 0 (needed: at least 5); no WWOX-system small-molecule result exists after the module's first snapshot, and the only small-molecule WWOX-system results ever recorded (lithium, ethosuximide, d-APV) are from 2020 and 2021.
- That U25 or any untested unit would work: no outcome exists.
- Anything about NMDAR/GSK3 beyond what earlier packages hold (not reopened).

## Limit that restricts the claim
Outcomes independent of the module do not exist for this task. The freeze and the scorer are in place: when a dated third-party WWOX-system perturbation result appears, `python3 -I predictive_it16_p2.py evaluate --outcomes <tsv>` scores the frozen selection against B0/B1 and refuses a claim below 5 independent origins (exit 2).

> IT16 verification note (independent verifier, fresh context): the 7 tested units reproduce; the "about 4 independent controlled origins" are about 3 groups (the AAV9 and organoid papers share a laboratory); the A51 attribution (U10) is not confirmed by the abstract and is treated as a non-outcome; the p-value restates the ranking rule together with tested status. A publication-date query from the freeze finds one WOREE case series (PMID 42721537, not a perturbation). The conclusion stands.
