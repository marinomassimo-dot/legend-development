# ADV-247 independence wording placed (IT, 2026-11-25)

Actor `orchestrator` (IT). Hypothesis level; reference genotype class; nothing is medical advice. Source of the wording: SCI, `brainstorm_20261116/adv247_independence_audit_sci_20261125/` section 4 and `independence_adv247.tsv` (relayed by SCI at ADV's request; peer message, not operator authority). No value, grade, rank or status changes.

## 1. What was placed (ordinary route)

| Limit | Where | How |
|---|---|---|
| P47T regions: the libraries come from the same mice | cards K01, J01, L01 (packet `not_known`, cards rebuilt); INV-16 (clause) | one sentence per place |
| Hippocampal bulk arms of 2 or 3 libraries, one mouse per library not stated | cards J01, F03; INV-06, INV-15 | idem |
| Single-nucleus: one dataset per genotype, animals not stated, nuclei not replicates | INV-15 | clause (SCI's own correction of "one pool per genotype") |
| shRNA: one population per arm in one cell line, the two stages not independent knockdowns | card I01; INV-02 | idem |
| Organoid clone and batch limit (ADV-244, already placed for K01, D01, D02, M01, E02, I01, E01, E03, F01, INV-16) | **added** for the other organoid consumers in SCI's table: cards F02, F03, F04, J01, L01; INV-02, INV-06, INV-07, INV-08, INV-19 | same text as the first placement |

INV clauses are translated (it, fr, es, de); views and shareable package regenerated.

## 2. Not placed, and why

* **H1 / T19 and T20 (Hussain neurosphere RNA-seq).** The consumers I found are frozen generation inputs (`generation_it9_p1_20261030/seeds.tsv` and `build_seeds.py`, `generation_it22_p1_20261103/inputs_it22*/seeds.tsv`, rows S129 to S131: GRIN2C, KCNA2, GRM3). Editing a frozen seed table would change a run's input, so the wording "neurosphere libraries not tied to individual pups" is carried here and in the candidate, not in those files. If ADV wants a live consumer, the open-question map or `functional_it13_p3a_20261031/README.md` is the place; say which.
* **RP-008, RP-017, RP-019, RP-033, RP-038 (portfolio rows):** ADV's to patch.
* **CLAIM 002, 005, 007, 014:** claim text only through a candidate: `commit_candidates/CC-20261125-ORCHESTRATOR-ADV247-INDEPENDENCE-01.md`.
* **M1 and M2, M5, M7 consumers** that are not cards or investigations in the table (carried inferences with no card row of their own): nothing to edit.

## 3. Checked before placing

* The same-mice statement: SCI's GEO sample-title read plus ADV-233's per-animal analysis, where the same animal ids (M6, F8) rank first and second across regions, are consistent with it. I did not re-open GEO.
* Single-nucleus and hippocampal unit gaps: restate my identity table of 1 November (`gse158684_identity_it14_p1a_20261101`) and are not new facts, as SCI says.
* Not re-read by me: the paper legends for the n values quoted in SCI's table.

## 4. Files

`apply_adv247_wording_it_20261125.py` (idempotent; marker "[IT 2026-11-25, ADV-247" and the ADV-244 marker).
