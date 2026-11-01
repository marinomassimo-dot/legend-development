# Comparable quantitative pharmacology (IT15 P2, 2026-11-01)

Non-canonical research material; not medical advice; a potency is not a benefit. Retrieved from ChEMBL (EMBL-EBI, CC BY-SA 3.0) through `framework/adapters/chembl.py` and from the IUPHAR/BPS Guide to Pharmacology file already held by the module; the activity values are as the sources state them.

## What was audited

The IT14 table `scout_it14_p6_20261101/selectivity_same_document.tsv` listed, per document, every target with an exact `=` value and a ratio max/min of the per-target **minimum**. IT14 identified gene symbols for ChEMBL targets (an identity join). A join of identity does not show that a complex measurement belongs to each subunit, that two values of one article are comparable, that the minimum is the best estimate, or that a ratio across unlike targets is a selectivity. Consumers: the IT14 scouting README (one paragraph quoted four of the ratios as "quantitative selectivity actually observable") and the IT14 P3 ladder (subtype statements for the GABA-A and NMDAR rungs, which cite primary papers and not this table). No ranking, card or view surface reads the table.

## Field availability (what the comparison could use)

| Field asked for | Where it exists today | State |
|---|---|---|
| assay id, document id | ChEMBL activity row; kept in `relations.tsv` ref (target;document;assay) | kept |
| target composition | gene symbols per ChEMBL target (adapter, IT14); `relations.tsv` gene column, subunits joined by `\|` | kept; now used to class single / defined complex / generic complex |
| species, cell system, assay type, free-text description, validity comment, duplicate flag | adapter output (assay context) | fetched on 2026-11-01 for apinocaltamide (24 rows) and ezogabine (32 rows) and stored as `scout_it14_p6_20261101/assay_context.tsv`; **not available** for Ro 25-6981 and ethosuximide because ChEMBL answered HTTP 500 for those two molecules on three attempts (the service answered 200 on `status.json`); not retained for the other documents |
| endpoint / measure type, unit, relation (`=`, `<`, `>`) | activity row | kept; censored and valueless rows are now listed, never converted |
| agonist concentration, holding voltage, incubation time | only inside the free-text assay description (for example "at -40 mV", "preincubated for 3 mins") | not structured; a comparison that depends on them is limited by their absence, not blocked |
| molecular identity and stereochemistry | ChEMBL ids resolve at the molecule level; stereo/parent check was not repeated here | gap, stated |
| primary origin | document id; PMID for GtoPdb rows | kept; one document is one origin |

## Change (minimal, in the existing path)

`selectivity_p6.py` was extended in place; no new engine. Per document the output now shows, for every target, n, min-max, the median and any censored or valueless rows; a composition class; a **grade** with the reasons that limit it; and the ratio between the lowest and highest target median only when the grade allows a ratio. Grades: INTERPRETABLE, LIMITED, NOT_DETERMINABLE, PANEL_NOT_SELECTIVITY (rules in the script docstring). A document spanning gene families is graded as a panel and each family with two or more targets is graded on its own. Regressions: `scout_it14_p6_20261101/test_selectivity_p6.py` (16 tests: the contrasting cases below, real assay descriptions with different stimuli, the minimum not privileged, validity comment, family and composition rules, committed output). The three existing matching fixtures (duplicated evidence, transfer between molecules, unknown turned into negative) are untouched and were not affected.

## Before and after on four real cases (`before_after.tsv`)

| Case | Before (IT14) | After (IT15) |
|---|---|---|
| 1. Informative: apinocaltamide, rat recombinant Cav3.1/3.2/3.3 (16, 13, 1.8 nM), one document, same flux format and the same stimulus | one ratio of 8.9 | INTERPRETABLE, 8.9 between the extreme subtype medians: a subtype spread inside one assay format |
| 1b. Same document, conditions differ: human Cav3.x (6.4, 18, 7.5 nM; calcium re-addition) against Cav1.2 (2,410 nM; KCl depolarisation), channels of "unknown origin" | folded into one ratio of 8,120 with seven CYP isoforms and hERG | LIMITED (stimulus differs; T-type block is state-dependent) and no ratio offered; the table keeps every value |
| 2. Same document, unlike targets: the CYP isoforms (enzyme assays with substrates) and hERG (patch clamp) | counted in the same ratio | the document is a PANEL_NOT_SELECTIVITY row; the CYP group is LIMITED (techniques differ) with no ratio: an inter-isoform spread is a liability, not a selectivity of the compound |
| 3. Complex not attributable to a subunit: Ro 25-6981 against `GRIN1\|...\|GRIN3B` (generic NMDA-receptor group, 5.6 nM) and `ADRA1A\|ADRA1B\|ADRA1D` (180 nM) | ratio 32.1 | NOT_DETERMINABLE; no ratio; a generic-group value is not a GluN2B value |
| 4. Missing or censored: apinocaltamide CYP2A6 "greater than 100,000 nM" | dropped without trace | listed as censored for the target and never a number; ethosuximide CACNA1I "greater than 5,000,000 nM" remains one censored row (single target, no pair, no row emitted) |
| Extra: ezogabine, one document, Kv7.2 930, Kv7.2/7.3 heteromer 1,720, Kv7.3 3,900, Kv7.4 1,980, Kv7.5 800 nM | ratio 4.88 | LIMITED: a defined complex is compared with its components (ratio shown with its reason) |

The first draft of this iteration graded case 1b INTERPRETABLE (377 fold); the independent review found that the assay descriptions give different stimuli, the grader gained a rule for stimulus and holding voltage, and the case moved to LIMITED. Counts of the regenerated table are derived by the script and not pinned in any test.

## What this does and does not show

* Computational capability: a stated, reproducible grade replaces an unconditioned ratio; two real cases (the Cav family and the generic NMDAR complex) change interpretation. Counts: see the table.
* Biological plausibility: unchanged. Nothing here is a measurement in a WWOX system.
* Not shown: that any compound is selective in a neuron; that a FLIPR IC50 predicts a patch-clamp effect; the subtype ratios of clobazam, N-desmethylclobazam and diazepam (not in the table; the three primary papers stay disputed).
* Open: assay context for Ro 25-6981, ethosuximide and the other documents once ChEMBL answers again (a reopen condition, not a defect of the grading); a ChEMBL offline dump was scouted and set to WATCH in `../scout_it15_p5_20261101/`.
