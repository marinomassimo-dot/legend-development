# IT44 P8: what the path produced for S12 (astrocytic K+ buffering), and the precise point where it stopped

Non-canonical working note. Not medical advice. Frame before the search: `relation_s12_frame_it44.md`. Mechanism path unchanged (`s12/`); activity path `activity_search.py`.

## Result
* **Mechanism path (7 rows, 5 molecules):** every row is a blocker or a gating inhibitor of Kir4.1 or Kir4.1/5.1 (a divalent cation, a monovalent cation, a tricyclic, a research Kir4.1 blocker and the proton): all EXCLUDED for an enhancement relation, as they should be. **No activator or enhancer is in the held tables.** SCI43's statement ("no activator in the catalogue") is confirmed for Kir4.1 on the mechanism rows, and unlike S11 there is no opener family to fall back on.
* **Activity path: did not run.** KCNJ10 and KCNJ16 have no target in the cached ChEMBL target index (that file holds only targets linked to a curated mechanism), so the manifest records both as `UNRESOLVED_IN_CACHED_INDEX`. **This is the precise stopping point: target resolution, not the absence of compounds.** Harness's resolver by UniProt accession (HE44) is the implementable fix; IT44 adopts it when it is on `main`, then reruns this relation (the reopen condition).

## Conditional comparison (what the output is)
No candidate and no nomination. The rows give the **discriminator**, not the lever: a Kir4.1 blocker (the research blocker or the tricyclic, with their other targets named as limits) should worsen or leave unchanged the bursts according to rival (a) and the astrocyte being the compartment; a blocker whose effect is the same in a neuron-only manipulation points to a neuronal Kir2-type or Kir5.1 action (the blockers act on heteromers). Premise unresolved: extracellular K+ during bursts has not been measured, and the compartments are not separated in the sources. Stop criterion: stop if extracellular K+ in the slice is not raised during bursts.

## Origin classification
Known in WWOX: no. Known in the repository: the KH4 action and its "no activator" statement (SCI43). New combination for LEGEND: a discriminator role for catalogue blockers of an enhancement question (the engine's excluded rows reused as controls, as in S10). No novelty claimed.

## Honest limits
One cell type of the question only; the research blocker's selectivity was not read; the tricyclic's many other targets are not listed here; no primary paper was read for any of the five molecules.

## Addendum (2026-11-11): the exact resolver adopted, and what it said
`activity_search.py` now adds HE44's `target_activity.resolve_targets` to the cached index (exact ChEMBL targets by UniProt accession, with a state per symbol). Run for S12 it returned **READ_ERROR for KCNJ10 and KCNJ16**: the public target-by-accession endpoint answered HTTP 500 (a direct request, a minute apart, gave the same answer): a service error, not an absence. S12 therefore stays unread on the activity side; the manifest records `READ_ERROR`, so nothing reads it as "no compounds". Reopen condition: the endpoint answers; rerun `activity_search.py --relations relations_s12_it44.tsv`. The mechanism-path result above is unchanged.
