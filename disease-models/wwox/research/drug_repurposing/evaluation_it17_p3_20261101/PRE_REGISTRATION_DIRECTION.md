# IT17 P3 pre-registration: direction of action, module relation against an independent curated source

Written 2026-11-01 before `direction_task.py` was run. Non-canonical research material; not medical advice; a computational check, not a benefit claim. Public edition, WWOX-DEE genotype class, no individual-level record.

## Why this task (utility, cost, verifiability)
The module's ranking and cards use "documented action direction" (for example "directionally_compatible_documented_action") to judge whether an intervention moves a need the right way. The direction comes from the catalogue's ChEMBL curated mechanisms. If those directions disagree with an independent curated source, the stored direction is a weak link; if they agree, that one component can be relied on technically. The data are local (catalogue, Guide to PHARMACOLOGY release 2026.3.1 in the cache), the second source is curated independently of the first, cost is minutes and no network. It is a component capability only.

## Task and level of claim
Task: for a human target and a compound that both sources describe, does the module's stored direction (ChEMBL curated mechanism: decreases / increases target activity) equal the independent source's direction? Level: **technical correctness of one stored field**. It says nothing about matching quality (which compound is a candidate for WWOX), hypothesis generation, biological prediction or benefit, and none of those is claimed from it.

## Units, labels, ground truth
- Unit: pair (parent ChEMBL compound id, human UniProt target). Module side: direct (not inherited) `ChEMBL curated mechanism` rows with organism Homo sapiens in `catalog/catalog.jsonl.gz`. Independent side: GtoPdb `interactions.csv` (Target Species Human) joined through `ligands.csv` ChEMBL ID. Join on parent compound and UniProt, never on names.
- Coarse label, fixed before looking at evaluation compounds: DECREASE (inhibitor, antagonist, blocker, negative modulators, inverse agonist, antisense/RNAi inhibitor) or INCREASE (agonist, partial agonist, activator, opener, positive modulators). Everything else (binding agent, generic modulator, enzyme, degrader, vaccine, GtoPdb Binding/Neutral/Mixed) is NO DIRECTION and is unresolved, never an error and never a success. The exact tables are in `direction_task.py` and may change only through the amendment log below, on dev compounds only.
- A side with two determinate opposite classes for the pair is CONFLICT (unresolved, counted). A pair with no GtoPdb counterpart is unresolved (coverage), not a disagreement.
- Shared origin: a pair is flagged shared-reference when the ChEMBL mechanism references and the GtoPdb PubMed IDs share a PMID. The primary result includes them and the independent-reference-only result excludes them; both are reported.

## Split (no contamination)
By compound, deterministic: first hex digit of sha256(parent ChEMBL id) in 0-7 is DEV, 8-f is EVAL. DEV is used to fix the label tables and to train the baselines; EVAL compounds are not read out until the lock below. No parameter is fitted for the module (its label is stored, not predicted), so DEV serves for the mapping and the baselines only.

## Baselines
- B0 most-frequent GtoPdb label in DEV determinate pairs.
- B1 per-target majority GtoPdb label in DEV (B0 when the target is unseen in DEV). B1 uses independent-source labels of other compounds on the same target, so it is a hard baseline the module has to beat.

## Measures
On EVAL determinate pairs: accuracy of module, B0, B1 with Wilson 95% interval; module-right/B1-wrong against B1-right/module-wrong with a two-sided exact sign test; number of discordant pairs (retained, listed). Unresolved counts by reason (no counterpart, no direction on either side, conflict). Descriptive subset: pairs whose compound is linked to a module card (`catalog/card_links.json`), over DEV plus EVAL, small by construction and not a test. Cost: wall time, source rows, network calls (0).

## Decision rules (stated before running)
- "Technical correctness of the stored direction" is stated when EVAL accuracy has a lower interval bound of at least 0.90 on at least 100 determinate pairs; otherwise the figure is reported with its interval and no such statement is made.
- "Added value over B1" is stated only if the module's accuracy exceeds B1's by at least 5 points and the paired sign test gives p below 0.05. Otherwise the result is written as "no added value over B1 measured". This is an acceptable outcome.
- Unresolved pairs are not folded into the denominator as errors. If unresolved pairs exceed half of the EVAL pairs with a counterpart, the coverage limit is reported next to every accuracy figure.
- Not shown by this task whatever the numbers: that any compound helps in WWOX deficiency, that the direction is the beneficial direction for WWOX, or anything about NMDAR/GSK3 interaction (not reopened).

## Amendment log (dev only)
1. Dev run 1 (2026-11-01, before any EVAL read-out): 1 003 determinate DEV pairs, 15 discordant; 7 of the 15 involve a partial agonist on one side (a partial agonist raises activity from baseline but antagonises a full agonist, so its direction is ambiguous by definition). Amendment: PARTIAL AGONIST (ChEMBL) and Partial agonist (GtoPdb action) moved from INCREASE to NO DIRECTION in both sources. Reason is the pharmacological definition, applied to both sides alike; it removes pairs from the denominator (they are reported as unresolved), it does not add any. The other 8 dev discordances (agonist vs antagonist labels on the same pair) are left as they are.

## Lock before evaluation
Locked 2026-11-01 before the EVAL command: `direction_task.py` sha256 09b2ab6ac74900ac029bed3b399bc0189ed45dcaa8ab9462f38a8cd8f80753fe (after amendment 1); this file and the script are committed on the task branch before EVAL is run, and `results_direction.json` records the script and input digests actually used. Any later change to the script or the mapping invalidates the EVAL result and must be reported as a new, separate analysis.

## Post-lock note (2026-11-01)
The first EVAL command stopped on a parsing error in the card-link subset only (some `card_links.json` link entries carry `catalogue_id` and no `chembl_id`) before printing or writing anything. The parser line was fixed (use `catalogue_id` when `chembl_id` is absent); the mapping tables, split, baselines and metric code were not touched. The executed script therefore has sha256 e814abbfc91274439e361393e1babc167e5f32ae776594dfed61eaa638c02c46 (recorded in `results_direction.json`), not the locked digest above; the difference is that one line.
