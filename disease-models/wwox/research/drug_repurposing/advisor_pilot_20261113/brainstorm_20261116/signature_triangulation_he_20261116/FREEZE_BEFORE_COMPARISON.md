# Signature triangulation (HE): ranking and expectation, frozen BEFORE any comparison with the matrix or the observed ordering

Written for: ADV, IT and SCI. Non-canonical; mechanism classes only; no dose, no recommendation. Held tables only; no query was made. Committed before `triangulate.py` exists.

**Not blind.** I have seen the frozen matrix scores (F1) and IT's scoring of the sealed extraction (and I computed their concordance). I also read the per-signature valproic acid scores in the held table earlier today (LEAP file, H-HE-3). So this freeze records an expectation, not a prediction made in ignorance.

## The signature ranking (from `signature_ranking.py`, files `signature_rows.tsv` and `signature_ranking.tsv` in this folder)
Measure: share of a class's signatures with opposition_score > 0 (the signature moves the WWOX-loss glycolysis/lactate module the opposite way), minus the base rate of the SAME context over all signatures of the held table. Base rates: neuron-like contexts 0.503 over 451 signatures; progenitor-like 0.516 over 788. Primary context: neuron-like (NEU, evaluation contexts); progenitor-like is reported beside it.
Neuron-like ranking, highest opposition first:
1. sodium_channel (carbamazepine, lamotrigine): 2 of 3 signatures opposing, effect +0.163
1. steroid_acth (dexamethasone, mapping confidence low): 2 of 3, +0.163 (tied with sodium_channel)
3. carbonic_anhydrase_multitarget (zonisamide, confidence medium): 1 of 2, -0.003
4. valproate_type (valproic acid): 0 of 4, -0.503 (aligned-tail p 0.061; the only class with a tail below 0.1)
Not mapped to a rule class (listed, not ranked): riluzole, nimodipine. Classes with a signature row: 4 of the 15 (v1) classes; 4 of the 19 (v2) columns.

## Stated expectation (one line, fixed now)
I expect little or no agreement: against the frozen matrix F1 (per-thread sodium 9, valproate 9, carbonic-anhydrase 6, steroid 0) a concordance near 0.5 on at most 5 classifiable pairs, with valproate placed top-tied in the matrix and last here; against IT's observed ordering at most one classifiable pair (carbonic-anhydrase and steroid are the only classes both cover), probably tied, so not scorable.

## What would make this a non-result
Fewer than 3 shared classes, or fewer than 10 classifiable pairs, is declared uninformative in advance (the same bar as the class-level test); n of 2 to 4 signatures per class and one dose (10 uM) cannot carry a class effect.
