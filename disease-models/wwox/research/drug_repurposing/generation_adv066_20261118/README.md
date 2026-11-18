# ADV-066 — the day's pharmacological comparison as generator packages; INV-04 and INV-09 in the generator; a real BEFORE and AFTER

Non-canonical working note (IT, 2026-11-18). Not medical advice; no dose, schedule, route, recommendation or spend. Reference genotype class only; no individual-level data. Ranking order is research value, not efficacy. The order digest of the ranking is unchanged (`ff38fcaa61295a5a`); no card, need, tier or direction was touched, and `ranking.json`, the views and the translations are byte-identical to the landed tree.

## Answer first

1. **Registered and read.** The two packages of the day (INV-04 ethosuximide and the T-type thread; INV-09 lithium, the GSK-3 thread and the regimen) are registered in `hypothesis_packages.tsv` (four manifest rows, a hypotheses row and a comparison row for each) and the generator now reads them. Eight conditional-proposal rows are appended to `conditional_proposals_packages_it47.tsv` (34 to 42; the 34 earlier rows are byte-identical and in the same positions), and a new function `comparison_rows()` returns the registered by-endpoint comparison rows (10) and the package's decisive propositions (21) verbatim into two new files. `hypothesis_package.py check`: OK (158 rows over 23 manifest packages).
2. **BEFORE and AFTER, blind readers, criteria hashed first: NO DIFFERENCE on both threads by the rule fixed in advance.** INV-04: BEFORE met 3 of K1 to K5, AFTER 4 (+1). INV-09: BEFORE 2, AFTER 4 (+2; +1 if the one borderline credit, K3 for the INV-09 AFTER reader, is withdrawn). The rule needed +3. No harm in either AFTER. My pre-registered prediction (IMPROVED 0.70 and 0.55) was wrong, and the reason is in section 4.
3. **What a reader writes differently with the packages (K1 and K4, observed; not a score).** The AFTER readers state, endpoint by endpoint, which candidate or class is more promising and at which evidence level (provoked seizure, acute rescue, chronic control, development; paediatric exposure for lithium; the KCC2 branch against an NKCC1 blocker "on evidence level only"), and both say the Kasahara 2019 datum is withdrawn. The BEFORE readers state that the material ranks nothing. That is a better formulation of a comparison. It is not a new prediction: **no reader, in either arm, produced a new discriminating outcome pattern (K2)**.
4. **The BEFORE arm already carried the day's wording.** The stored investigation rows for INV-04 and INV-09 were updated earlier today (IT57: the published effect cannot power the interaction, wild type near the floor, a pilot first, the rat age floor, no T-type or GSK-3 measurement in a WWOX system, the 0.7 and 1.43 margin) and that wording was already in the BEFORE text. K3, K4 and K5 were therefore largely met by both arms; the packages add K1 and little else. I had not weighed that when I wrote the prediction.
5. **Two defects of my own found and repaired before landing** (section 2): the generator wrote "mapping drafted by HE and read by the owners (SCI, PRESIDIO-001, 2026-11-14)" onto my eight rows, which is false provenance for a mapping I wrote; and my first run interleaved the new INV-09 rows into the middle of the earlier file, which three earlier suites pin.
6. **ONE battery is still owed and is not mine to start alone.** Targeted suites pass (section 5). The full battery on the final tree is coordinated with HE, who decides who runs it after this change lands.

## 1. What was registered (`../comparison_adv066_20261118/`)

| Package folder | Layout | Contents |
|---|---|---|
| `inv04_ethosuximide_age_assay/output/` | HB1 layout | hypotheses E1 to E4 (knockout-selective, age-limited, general, T-type route); comparison rows C-EP1 to C-EP7 by endpoint; new measurements M-1 to M-8; decisive propositions D01 to D12 (D10, Kasahara 2019, stated as withdrawn) |
| `inv09_lithium_gsk3_regimen/output/` | HB1 layout | hypotheses L1 to L4 (general, GSK-3-specific, regimen artefact, conditional development cohort); comparison rows C-GS1 to C-GS3; new measurements M-1 to M-4; decisive propositions D01 to D09 (D09 stated as withdrawn) |

Roles in the manifest: `hypotheses_only` for the hypotheses and `pharmacological_comparison` for the comparison rows. Nothing is nominated, ranked or given a dose; "more promising" is a statement about evidence level and testability in the package's own words.

## 2. The generator change (`../generation_it40_20261109/conditional_proposals.py`)

* `PKG_MAP` entries for the two packages (observation, relation, context, action, compound, competing, expected, measure, reopen mapped to the package's own columns; the premise slot is empty by design because `mechanism_and_missing_bridge` carries premise and relation; `sign` is `unknown` for every row). New key `mapping_note` carries the true provenance: "mapping drafted by IT with the rows (ADV-066, 2026-11-18); no second owner has read it and no blind reader has tested the mapping". The earlier maps keep the earlier text, unchanged.
* `LATE_PACKAGES`: the two packages are read in a second pass after every earlier package, so the rows already produced keep their position and the new ones are appended (INV-09 L1 to L4, then INV-04 E1 to E4).
* `comparison_rows()` is a consumer of its own. `INVS` governs only the physiological hypothesis packages (`record_for`); adding INV-04 or INV-09 to it produces 0 rows (tested), which is why the comparison needed a reader of its own. Rows are returned verbatim from `hypothesis_package.comparison_for`; a missing cell is written "not stated by the package", never completed.
* New files: `conditional_comparison_adv066.tsv` (10 rows), `conditional_decisive_adv066.tsv` (21 rows). `conditional_proposals_it40.tsv` and `conditional_design_steps_it50.tsv` are unchanged.

Found during the work (INFERENZA from the code, repaired): `mapping_unconfirmed=True` appends a fixed sentence naming HE and the owners; on my first run it was printed on all eight new rows. The reader test did not see it (the views carry no `nomination` column), so the readers' material is unaffected; the four AFTER and BEFORE views were rebuilt from the corrected generator and are byte-identical to those the readers read.

## 3. The reader test

* **Pre-registration** (`PREREG_ADV066_READER_TEST.md`, `READER_TASK.txt`): criteria K1 to K5, harms H1 to H6, outcome rule, subjective prediction. Hash printed in the session at 21:25:43 UTC, before the first reader request (21:25:57); the same hash is in `SHA256SUMS_ADV066.txt`.
* **Material** (`views/`, built by the inline script saved as `build_views_adv066.py`; the pre-registration calls it `build_views.py`): BEFORE = the stored investigation row plus every generator row for that investigation before the change (INV-04: none; INV-09: five); AFTER = the same plus the generator rows of the registered package, the comparison rows and the decisive propositions. Sizes: INV-04 2 KB and 33 KB; INV-09 18 KB and 40 KB.
* **Readers:** four fresh `legend-delegate` agents, one per file, one pass, no tool beyond reading the file and the task text, blind to the pre-registration and to each other. Requested: sonnet, effort medium. Read back from the agent transcripts: model `claude-sonnet-5-5` for all four; the request carried `effort: xhigh`, not medium. Reports are the verbatim hand-backs (`readers/`), 388 to 426 words (the task asked for at most 300: the criteria were scored on content, not length).

| Thread | Arm | K1 | K2 | K3 | K4 | K5 | Met | Harms |
|---|---|---|---|---|---|---|---|---|
| INV-04 | BEFORE | no | no | yes | yes | yes | 3 | none |
| INV-04 | AFTER | yes | no | yes | yes | yes | 4 | none |
| INV-09 | BEFORE | no | no | no | yes | yes | 2 | none |
| INV-09 | AFTER | yes | no | yes (borderline) | yes | yes | 4 | none |

Outcome by the fixed rule (IMPROVED needs +3 and no harm): INV-04 NO DIFFERENCE (+1); INV-09 NO DIFFERENCE (+2, or +1 without the borderline K3). Anchors per cell: `scoring_adv066.tsv`. The result does not depend on any single borderline call: INV-04 would need BEFORE to lose two of K3, K4, K5 to reach +3.

## 4. Four things kept apart

1. **What the reader writes differently.** AFTER: by-endpoint "more promising" statements with evidence level (INV-04 four endpoints; INV-09 paediatric exposure and development); the Kasahara 2019 datum named as withdrawn (both AFTER readers; neither BEFORE reader had it); extra measurements taken from the package (a Cav3 readout in Wwox-null thalamic neurons, a video-EEG subset, a wild-type age series to P28, a bootstrap over litters; E_GABA by perforated patch, p-Ser9 with total GSK-3 and a kinase readout in the same treated animals); material from the other thread reaching the INV-09 reader ("the same pilot as INV-04"; "ethosuximide goes first as a design order, not as efficacy"). BEFORE: a sound design already (pilot, interaction term, age series, assay-sensitivity panel, selective T-type blocker; for INV-09 isoform knock-down, epistasis constructs, an inositol add-back arm) and the statement that the material ranks nothing.
2. **Better formulation of a comparison or of an experiment?** Of the comparison, yes (K1). Of the experiment, only in part: the AFTER design adds measurements, and the BEFORE design was already complete on the points the criteria score.
3. **Predictive capacity.** None is claimed. Four readers, one pass each, one model; the rule was built to say "no difference" unless the gain is large.
4. **What the generator still cannot produce (K2).** A new outcome pattern that separates two competing explanations, with a margin. The packages hold explanations (E1 to E4, L1 to L4) and the "outcome favourable / contrary / unresolved" cells, and the readers returned them as design items, not as predictions. The generator maps and returns what a package states; it does not generate the discriminating prediction. Where that prediction is needed it must come from a package author or a reader with a question, and K2 stays the open criterion for the next round.

## 5. Limits and what passed

* AFTER inputs are 33 and 40 KB against 300-word answers: a reader cannot use all of it, and a reader's omission is not evidence that a row is not useful. Two readers per arm are not a sample.
* The mapping is unconfirmed (no second owner, no blind test of the mapping itself): it is stated on every new row.
* BEFORE is "the current generator output with the stored investigation rows as they stand today", as ADV asked, not the state before today's IT57 wording; the wording itself was tested separately and landed earlier (`../generation_it57_20261118/`, 0 of 8 against 8 of 8).
* The comparison rows are not an input of any ranking, card, need or direction; nothing here changes one.
* Passed on this tree (targeted, not the battery): `test_comparison_rows_adv066.py` (9, new), `test_stage_it40.py` (12), `test_aggravation_sign_he65.py` (4), `test_design_rows_he50.py` (32), `test_stage_it47.py` (9), `test_stage_it49.py` (6), `test_stage_it50.py` (4), `test_ladder.py` (9), `framework/scripts/test_hypothesis_package.py` (60), `scripts/test_legend_commit.py` (16), `scripts/test_structured_data_integrity.py` (5), `scripts/test_tool_routing.py` (7); `hypothesis_package.py check` OK. Three earlier suites needed their counts and order extended (it47: the 16-row count excludes the two new packages and INV-04 joins the set; it49: 34 to 42; it50: eight rows appended last), each with a dated comment as HE53 and HE66 did; no assertion was loosened, and the 34 earlier rows are still pinned byte for byte by the new test.
* Not run here: the full battery (HE's coordination), CI on the effective revision (checked after landing with `ci_runs.py`).

## 6. Consumers and what comes next

* Consumers of the rows: the conditional-proposal files above (read by the question dossiers and by any reader of the generator output); no view or ranking reads them yet. Whether the by-endpoint rows should reach the dashboard is a design question for HE and ADV, not decided here.
* Executable now (no laboratory): a second reader pass on INV-04 and INV-09 with K2 as the only criterion and a request for the outcome pattern per explanation, using the E and L rows; or a package author's pass that writes those patterns into `outcome_favourable` and `outcome_contrary` per explanation.
* Laboratory: the pilot of the provoked-seizure design and the T-type, Cav3, E_GABA and GSK-3 readouts named by the packages' new-measurement rows (`new_measurements.tsv` of each package). Nothing here was measured.

## Files

`PREREG_ADV066_READER_TEST.md`, `READER_TASK.txt`, `views/` (four reader inputs), `build_views_adv066.py` (as run), `readers/` (four hand-backs), `scoring_adv066.tsv`, `SHA256SUMS_ADV066.txt`.
