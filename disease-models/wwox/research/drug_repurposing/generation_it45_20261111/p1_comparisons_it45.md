# IT45 P1: the comparisons that passed through the old ATP/scaffold code, kept before, recomputed after

Non-canonical working note. Not medical advice. Components: Harness HE45 (`framework/scripts/assay_conditions.py`, landed on main f3173fa8, battery on the frozen SHA 0fd43de6 PASS WITH SKIPS); consumer here: `generation_it43_20261110/comparison_engine.py` (`compare_props` calls it). IT44 had a local version of `conditions()/comparable()` that kept only the number of an ATP value; Harness reproduced three defects in it: 1 mM against 1 uM compatible, 1 mM against 1000 uM incompatible, a stated condition against a missing one compatible. The IT44 version was dropped at the merge; its aliases, reference-control reading and potency-statement regex stay.

## Before (kept)
`p1_before/compound_decisions_it43.tsv` and `p1_before/compound_decisions_inv07_it44.tsv`: the decision tables as the IT44 candidate d15894e0 produced them. They are not edited.

## After (regenerated on the merged candidate 4ce390d4, `comparison_engine.py main --inv INV-05` / `INV-07`)
| Compound (item) | Before | After | Why |
|---|---|---|---|
| VER-246608 (V13) | COMPARABLE | CONDITIONS_INSUFFICIENT: ATP stated on one side only; nothing shared beyond the system | a missing condition is neither agreement nor refutation |
| AZD7545 (V13) | NOT_COMPARABLE (core-bound against core-both) | NOT_COMPARABLE (core-bound against core-free) | still a documented incompatibility; the pair named differs because the reader now reports the first documented difference |
| oxamate, stiripentol (V15) | COMPARABLE | NO_POTENCY_PAIR | the old code printed COMPARABLE with no pair examined |
| ifenprodil (V02) | COMPARABLE | NO_POTENCY_PAIR | same |
| radiprodil (V05) | SINGLE_OR_NONE | NO_POTENCY_PAIR | only one side carries a potency statement |
| perampanel (V03), Ro 25-6981 (V18) | NOT_COMPARABLE | NOT_COMPARABLE | system / holding-potential / composition differences, now with units and composition read by the shared component |

Counts over the 27 decision rows (INV-05 20, INV-07 7): COMPARABLE 4 → 0; CONDITIONS_INSUFFICIENT 0 → 1; NO_POTENCY_PAIR 0 → 4 (one SINGLE_OR_NONE moves too); NOT_COMPARABLE 3 → 3 (unchanged membership but one reason text changed).

## What changed downstream, checked
* **Roles and tiers: 0 of 27 changed.** The role derivation does not use the comparison state beyond the premise it names.
* **Premises, experiments, relaunched questions, priorities: 0 changed.** `comparison_state` is read by no card, investigation or ranking consumer; its only readers are the two package engine checks (`pdh_pdk_sci44_20261110/engine/derived_roles_check.tsv`, `ro25_6981_sci44_20261110/engine_check.tsv`), regenerated here (6 and 4 lines differ, states only).
* What the correction removes is a **false "COMPARABLE" on four compounds** that a reader of the table could have read as a licence to rank their potencies. The effect is on the accuracy of a diagnostic column, not on a decision. Stated without inflation.

## Conditions the engine can now tell apart (tests added in `test_comparison_engine.py`)
1 mM and 1000 uM ATP: COMPARABLE (units converted); 1 mM and 1 uM: NOT_COMPARABLE; one side missing: CONDITIONS_INSUFFICIENT. Scaffold, ATP, holding potential, co-agonist and composition are read by the shared component; **pH** and receptor composition beyond the GluN2 families are not yet an axis for the cases run (SCI45 proposes a pH axis; not built here: it would be added only when a decision needs it).

## Limit found at the merge, for Harness
An enzyme assay whose system string carries none of the recognised words (oocyte, HEK, slice, neurons, purified/crystal/kinase assay…) is INSUFFICIENT even against an identical string ("human PDK1, with the E2p/E3BP core, 5 uM ATP" on both sides). My IT44 test used that string; it now says "purified human PDK1 kinase assay". The real INV-07 rows were recognised. A recombinant-enzyme system word could be added to the vocabulary; not changed here because the component is Harness's.
