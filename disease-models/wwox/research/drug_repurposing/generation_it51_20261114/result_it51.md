# IT51 result: the same case after HE's link (revision a33c39a90)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Targeted check of one known limit; not an independent benchmark and not a validation of the generator. Pre-registration: `prereg_it51.md` (criteria fixed before the after-run).

## Held fixed / moved
Held: the case (CP-BH1, CP-BH2, INV-05), the package inputs, the criteria. Moved: the repository revision (bd6ff283a -> a33c39a90), which also carries HE's registration of `measurement_reconciliation_adv006_20261114` as `design_only` and the pointer column. The generator was rerun at a33c39a90 (66 design rows; 53 for ADV-006); the committed files are what it writes (no diff). Not held: the generator code revision, which is the changed variable.

## Mechanical difference
CP-BH1/CP-BH2 differ from `baseline_before_conditional_proposals_it40.tsv` in one new last column, `design_rows_same_investigation` (an INV-level pointer: 53 rows, "not linked to this hypothesis by any package"). Every other cell is byte-identical.

## Against the criteria
| Criterion | Where | Result |
|---|---|---|
| E_GABA before any GABA-A / supply arm, as conditional order, with CLAIM002 s6 | design rows M16 and M17 `interpretable_after` quote "interpretable only after mIPSC, agonist response and E_GABA place the deficit"; M05 lists CLAIM002 section 6 | met, in `conditional_design_steps_it50.tsv`, not in CP-BH1/2 |
| Both matching variables of the non-GABAergic comparator unresolved | M15 + CF23 (percent evoked charge removed versus Vm and Rin), both quotes, no side chosen | met |
| sIPSC configuration as a choice that changes reading | CF01 (native-chloride perforated versus set low-chloride whole-cell), `which_would_change_the_interpretation` present, no side chosen | met |
| Harms | two M01 kept apart (package-qualified ids, 53 unique); six genuine conflicts kept (CF01, CF03, CF04, CF05a, CF05b, CF23); no "established/demonstrated" wording; only "alpha2" is a column name in M21 (benchmark), not "alpha2-preferring"; M16 carries Synapsin-Cre layer II/III P13-17 and M14 the global/CA3 preparation, no silent transfer | none found |

## Verdict
IMPROVED IN ACCESS, NOT IN CONSUMPTION. The three statements the baseline lacked now exist as rows with their limits, but only inside the design file. CP-BH1/BH2 hold only the pointer; the packages state no link from BH1/BH2 to M15/M16/M17, and no card, decision, dashboard row or question reads the design file. Residual risk I found: CP-BH1 `experiments` cells use BE0/BE1 arms named M01, M02, M07, M08, M15 (ampa_nmda_discrim ids) while the pointer lists the ADV-006 M01..M28 in the same row; the ids are package-qualified in the design file but not in the CP row, so a reader can confuse them (the M16 of the two packages are different measurements).

## Missing step
A link from the hypothesis to the measurement authored by the package owners (a column), or a generator join on a declared key. Neither exists and neither is a mechanical choice; I did not build one. Smallest fix inside my remit: a pointer at the INV-05 investigation row and open question, with the id caveat.

## Not shown
A better prediction, a favourable compound, efficacy, or that the gain generalises to a case chosen by someone else. One case, scored by the builder; no independent reader used (no decisive proposition was newly promoted).
