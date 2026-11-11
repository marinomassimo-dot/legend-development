# HE45 — correct comparisons, evidence selection, real cost

Working record of the Harness mandate HE45 (generic components, comparison semantics, readers, cost measures). Scientific regeneration belongs to IT45, pharmacological and biological readings to SCI45.

## 1. Conditions in comparisons (H1, H2)

**Reproduced on the landed code** (`generation_it43_20261110/comparison_engine.py` at 3f8f17fb): `conditions()` knew system, holding potential and glycine only. ATP, scaffold and any other solute were not read, so every ATP pair was compatible; the unknown system was the label `other`, equal to itself.
**Reproduced on the IT44 candidate** (`task/it44` 8edf3852, not landed): ATP read as the bare number of `N mM|uM ATP`, so `1 mM` and `1 uM` were equal and `1 mM` and `1000 uM` differed; a field stated on one side only was compatible; two unrecognised preparations were both `other`.

**Fix.** One implementation, `framework/scripts/assay_conditions.py` (+ `test_assay_conditions.py`, 21 tests), reusing the unit table of `measurement.py`. `comparison_engine.compare_props` calls it; the earlier `conditions` function and its tuple are gone, `comparable()` remains as a thin wrapper. Three answers: `DOCUMENTED_AGREEMENT`, `DOCUMENTED_INCOMPATIBILITY`, `INSUFFICIENT`. In the engine's `comparison_state`: `COMPARABLE` (documented agreement on every pair), `NOT_COMPARABLE: …` (unchanged prefix), new `CONDITIONS_INSUFFICIENT: <pair: what is missing>`, and `NO_POTENCY_PAIR` where the old code printed `COMPARABLE` for any compound with two propositions even when no pair was examined. The role is derived as before: insufficient information names a premise and blocks nothing.

Real wording first (50 condition cells of the 25 decisive tables on `task/it44`): `u`/`µ`/`μ` (only `uM` occurs today), decimal point, ranges (`50-100 uM glutamate`, `-70 to +20 mV`), several conditions in one cell (`3 uM glutamate and 3 uM glycine`), `Mg2+-free`, `… not stated`, `As D01; glycine 3 uM` (references resolved; the referenced system stays, the cell's own values override), drug concentrations that are not assay conditions (`30 uM cyclothiazide`), a negated system (`no neuron datum`), a number between two solutes (left unplaced, not guessed). No structured conditions column exists in any package: the free text is the only source, kept as the provenance in `differ`/`one_sided` (original wording shown). Not read: temperature, pH, buffer salts other than Mg/Ca/Zn/EDTA.

Composition and scaffold (H2): receptor subunits (`GluN2A–D`, `NR2x` → `GluN2x`, `GluA1–4`, `GluK1–5`, `triheteromer`) and the PDH core scaffold (`core_free`, `core_bound`, a contrast sentence names both) are fields; a cell naming several values overlaps rather than equals, so it is `INSUFFICIENT`, not agreement.

**Before/after over five packages** (`comparison_before_after.tsv`, 87 compound rows, inputs `task/it44@8edf3852`, earlier engine `3f8f17fb`; script `comparison_before_after.py`):

| | before | after |
|---|---|---|
| AZD7545 (D01 core-bound, D04 system unrecognised) | COMPARABLE | CONDITIONS_INSUFFICIENT: scaffold stated on one side only |
| VER-246608 (D05 5 uM ATP, D06 none) | COMPARABLE | CONDITIONS_INSUFFICIENT: ATP stated on one side only |
| 9 compounds with two propositions and no potency pair | COMPARABLE | NO_POTENCY_PAIR |
| the 2 NOT_COMPARABLE (Ro 25-6981, ro25 and glun2b packages) | NOT_COMPARABLE | NOT_COMPARABLE (unchanged) |

Limit: these five packages contain no pair that differs only in ATP unit; the `1 mM`/`1 uM` cases are covered by tests, not by a present package row. Nothing in the old output was a documented agreement that is now wrong; the changes remove agreement that was never documented.

## 2. Loader `hypothesis_package.load_comparison` with `engine/` (H3) — checked on `task/it44@8edf3852` (not landed)

Six cases on synthetic packages (a temporary directory, not in the repository), run against IT44's version of the loader:

| Case | Result on the candidate | Verdict |
|---|---|---|
| historical package, `output/` only | `output/` read, same rows as before | unchanged |
| comparison in `engine/`, no `output/comparison.tsv` | `engine/` read | works (the real SCI44 package A) |
| `comparison.tsv` missing everywhere | raw `FileNotFoundError` from `load_all()`: every package fails, no state, no diagnosis | **defect** |
| `new_measurements.tsv` missing | same raw `FileNotFoundError` | **defect** |
| empty / header-only `comparison.tsv` | rows = {} silently; `check` passes | **defect**: an empty file reads as "no comparison rows" |
| `output/` and `engine/` both hold a `comparison.tsv` | `output/` wins silently, even when the two differ; if `output/` is header-only and `engine/` is full, the empty one wins | **defect**: a silent choice that changes the data |

Also: `decisive.tsv` is read from the chosen folder only, so a package whose `engine/` lacks it gets `dec` = {} without notice. The manifest already names the folder per package, so a declared choice costs no new structure: the manifest `dir` may point at `.../engine` itself (the flat-folder branch of the original loader already handles it), and no probing is then needed.

## 3. Volume, aggregates, roles, cache of the activity path (H4–H6) — on `task/it44@8edf3852`

* **`FLOOD`** exists as README wording only. The mechanism is `DEPOSIT = 200` / `SCREEN_DEPOSIT` plus the `TRUNCATED` state. In IT44's three runs (S3, S11, diff) `SCREEN_DEPOSIT` hid no molecule with a catalogue status (every document above 200 molecules has no PubMed id): left unchanged.
* **The real flood is one activity type.** ChEMBL target CHEMBL1075094 (NFE2L2), 2026-11-11, release ChEMBL_37: 93,391 rows in IT44's five types, of which 92,628 `Potency` (qHTS AC50 depositions) and 763 dose-response (7 IC50, 755 EC50, 1 Kd). The cap of 5 pages x 1000 rows made every molecule of that target `TRUNCATED`: 151 catalogue-status molecules (94 approved, 48 clinical candidates) were withheld from the pointers, S10 listed none. The four dose-response types alone read COMPLETE (763 rows, 7 requests): 726 molecules, 7 with a catalogue record (bardoxolone methyl, dimethyl fumarate, monomethyl fumarate, sulforaphane, curcumin, resveratrol, halofuginone). Three are already held by the mechanism path (bardoxolone methyl, dimethyl fumarate, monomethyl fumarate); four are new to the S10 listing. They stay `ACTIVITY_ONLY` pointers: reporter-assay EC50 on the NFE2L2 target record is not a mechanism, sulforaphane, curcumin and resveratrol are frequent hitters, nothing here is favourable.
* **`best_nM`** (minimum over every row of a molecule) pools types, targets, organisms and assay types: 225 of 359 S3 molecules pool more than one (type, target, organism, assay) group, 53 of 6,275 in the large run pool more than one quantity type; no source row is kept. Nothing ranks on it today. `measurement.summarise()` gives the range per comparable group with the row of its lowest value.
* **Role fallback.** `entity_roles.role_of` returns `candidate` when no rule matches; 197 of 349 role rows get it by default (104 synthetic organic with no catalogue status, 84 `no_status_statement`, 5 `phase_unknown`, 4 natural products) and 95 of the 195 engine-`CANDIDATE` rows carry the role only by default. `eval_it44.py` repeats the fallback at the consumption point (`roles.get(..., {}).get("role", "candidate")`: a molecule absent from the table counts as a drug candidate). The existing vocabulary has `unqualified_entity`.
* **Cache.** `activity_search.fetch` caches `p{page}.json` per target only. Reproduced with a fake endpoint: a run with `--types IC50` followed by a run with five types reads the IC50 page and reports `COMPLETE` with one network call in total. The adapter cache built in HE44 keys on the full URL (target, types, limit, offset, molecule), keeps only successful validated responses and reads `chembl_db_version` on each query.

## 4. DREAM (H8)

* New result: the NFE2L2 volume finding (section 3). Chain: reporter EC50 rows of known activators on the NFE2L2 target record (observation) -> proposed relation: pointers to primary sources for NEED-REDOX-NRF2 / INV-08 (`WO-36`) -> competing explanations: KEAP1 modification or stress response rather than NFE2L2 binding; frequent-hitter behaviour; cell-line reporter artefact -> discriminating measurement: the open question's genetic arm first (isogenic WWOX-deficient against corrected cells, NFE2L2 knockdown) -> consumer: `pointers_it44.tsv` S10 (empty until the type split). Kind: three **already known but unused** (their EC50 rows were hidden), four **new combination in the repository**; no literature novelty claimed.
* Retrieval test on a new question ("which Nrf2 activators with a measured human EC50 are in the catalogue, and where do they touch WWOX?"): two helper calls (`dream_pass.py pairs NFE2L2 WWOX`, `consumers`) and three greps of the catalogue, the S10 molecule table and `open_questions_map.tsv` led to the originals (axis_it10 candidates, DL-MECH-153, WO-36) without reading the corpus.
* Revival triggers: the dismissal ledger holds no NRF2 or fumarate dismissal; none fired.
* Conditions left "unknown" in consumers: `CONDITIONS_INSUFFICIENT` now names the missing field per pair (AZD7545 scaffold, VER-246608 ATP); the ledger text of the PDH cards was not rewritten.
