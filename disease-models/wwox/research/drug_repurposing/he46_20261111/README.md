# HE46 — conditions, propagation, generative capacity (Harness Engineering, 2026-11-11)

Non-canonical. Harness work: generic components and checks. Scientific meaning stays with SCI46 and IT46.

## 1. pH and temperature in the conditions reader (H1, H4)

**What was missing.** HE45 left pH and temperature out of `framework/scripts/assay_conditions.py` and said so. The comparison packages do carry them: 14 of 122 proposition cells state a pH or say it is not stated, 28 state a temperature (`decisive.tsv` of nine packages). SCI45 asked for a pH axis (consumer delta row 10; SCI45 delta rows 10 and 6 for the pH and Mg2+ axes).

**What the reader now does** (read from the wording of those cells, not a universal parser):

| Case in the packages | Reading |
|---|---|
| `pH 7.6 or 6.9 set with HCl` (a series) | `pH` values 7.6 and 6.9; agrees only with an equal series; `pH 6.9` against the series is INSUFFICIENT (one value of a series is not the series) |
| `pH 7.4` / `pH 7.3` | absolute, equal → agreement, different → documented incompatibility; never goes through the nM table |
| bath / aCSF / buffer / recording solution against pipette / internal | `pH_extracellular` and `pH_intracellular` are separate fields; a pH with no side meets the extracellular one only when the values are equal (note: "side stated on one side only"); when they differ the side may be the reason, so INSUFFICIENT, not an incompatibility |
| `pHo step (7.4 to 7.1, with 7.7)` | `pH_step` (baseline, target); never an absolute value |
| `a 0.2 pH unit fall` | `pH_delta`; never an absolute value, and a step never agrees with a difference |
| `pH 7.4 to 7.2` with no word saying range or step | left in `unplaced`: not guessed |
| `(pH not stated)`, `no Zn2+ or pH stated`, `temperature ... not in the abstract` | `NOT_STATED`; `pH not applicable` is `NOT_APPLICABLE` (kept apart; the reasons say "declared not stated" or "declared not applicable" on the other side) |
| `30-32 C`, `35 C`, `room temperature` | `temperature_C`; room temperature is read as 18-26 C and the reason says so (35 C against room temperature is documented incompatibility; 23 C against it is not decidable) |
| `Fura-2 loading 37 C`, incubation, slicing, storage | not the assay temperature: kept in `unplaced` |
| `transfer to a slice (bicarbonate buffer, 35 C, Mg2+) is untested` (glun2b D17) | a contrast clause: not applied, listed under `contrast`. The proposition inherits D09's 23 C through `As D09` |
| `As D09; 35 C`, `As D09; pH 7.4` | a local override replaces only the field the cell states |
| reference to a missing or circular proposition | named in the reasons and in `unplaced`; the pair cannot read as agreement |

**Before and after on the real tables** (`conditions_before_after.py --old-ref 142f6c5f`, same inputs for both runs):

* Compound-level `comparison_state` of the four registered comparison packages: 67 rows, **0 changed** (3 NOT_COMPARABLE, 1 CONDITIONS_INSUFFICIENT, 8 NO_POTENCY_PAIR, 55 SINGLE_OR_NONE unchanged). **No compound decision changes.** The pH axis is not exercised by any registered package: the pH-bearing propositions are in `glun2b_comparators_sci42_20261110` (no comparison table, not registered) and in `ro25_6981`, where pH 7.4 appears on both sides of every pair that carries it.
* Every pair of propositions inside each of nine decisive tables (898 pairs): 8 change state, 890 do not (`conditions_pairs_before_after.tsv`). One agreement falls to INSUFFICIENT (glun2b D08 against D11: pH 6.9 stated on one side only, previously a documented agreement the text did not support). Seven INSUFFICIENT become documented incompatibilities, all through temperature (ampa D15 at 4 C against slices at 30-34 C; chloride P01/P03 at 35 C against P08 at 32-34 C).
* So: the reader is now able to refuse a false agreement and name a temperature or pH difference, and on the tables that exist today it changes no compound decision. It is a capability for the next comparison (SCI46 is expected to bring pH and Mg2+ conditions), not a correction of an existing result.

Tests: `framework/scripts/test_assay_conditions.py` (37, 15 new, each from a wording found in the packages).

Remove: revert the commit of `assay_conditions.py` and its test; no data file depends on it, `comparison_engine.py` calls `parse`/`compare` unchanged.
