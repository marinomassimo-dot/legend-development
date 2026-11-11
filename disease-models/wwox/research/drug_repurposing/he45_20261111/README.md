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
