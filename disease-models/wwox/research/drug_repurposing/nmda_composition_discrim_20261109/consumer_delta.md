# Consumer delta — INV-05 narrow comparison (proposals only; nothing applied)

Task record `ORCH-IT40INV05-20261109`. Every row names the consumer file and row, the proposed change, the source and the read depth. The integrating session (IT40) decides; this package edits none of these files, no ranking, no dashboard, no need.

**Point of the generative path that should use the result.** The step that turns INV-05 into conditional hypotheses and comparators (the IT40 generation stage and the `comparators` view) should read `output/comparison.tsv` as five conditional templates (each cell carries its DATO / INFERENZA / IPOTESI label and the measurement that closes the condition) and `output/new_measurements.tsv` as the list of conditions; the investigation's `next_test` is the place where the design is read by a human.

| # | Consumer and row | Proposed change | Source and depth |
|---|---|---|---|
| 1 | `drug_repurposing/ranking_it8_p9_20261029/investigations.tsv`, INV-05, column `next_test` (the text "a d-APV arm and a GluN2B NAM arm, each at matched measured NMDAR-current reduction (two unrelated NAMs)") | Replace "two unrelated NAMs" by "one ifenprodil-site GluN2B NAM (a second NAM controls chemotype only, same site and same triheteromer ceiling), compared with d-APV only up to the NAM's measured removable share; measure the d-APV threshold x and the NAM removable fraction first". No rank movement. | 24607230 partial full text (D01–D03, D11); verifier SUPPORTED |
| 2 | `comparators_it39_20261109/output/comparators.tsv`, file lines 11 (Ro 25-6981) and 12 (ifenprodil), columns `selectivity_limits` and `what_it_does_not_separate` | Ifenprodil: add primary values (oocytes, −40 mV, 100 µM glutamate plus 50 µM glycine: GluN2B IC50 72 nM, maximum 88 percent; GluN2A unchanged at 3 µM; triheteromer IC50 450 nM, maximum 32 percent, 50 percent with 300 nM Zn2+). Both rows: "does not separate a GluN2A pool from an insensitive triheteromer pool". Ro 25-6981 stays abstract-level (maximum and conditions unread). | 24607230 partial; 9400004 abstract only |
| 3 | same file, line 13 (radiprodil), column `selectivity_limits` | State species: rat GluN1/GluN2B 82 percent maximum against rat triheteromer 45 percent (human GluN1/GluN2B 91 percent); oocyte bath had 10 µM EDTA | 40994429 Table 1, re-read for this correction (earlier staged receipt) |
| 4 | `ampa_nmda_discrim_20261108/output/hypotheses.tsv`, BH2, columns `compound_or_probe` and `discriminating_experiment` | Use the like-for-like 82 against 45 (rat); add the removable-share bound (at most 0.88 times the GluN2B diheteromer share plus 0.32 times the triheteromer share, 0.50 times the triheteromer share with Zn2+; INFERENZA); add the burst-level percent removed as a readout | 24607230, 40994429 |
| 5 | same package, `prediction_matrix.tsv`, rows M04, M05, M06 | M04: add "measure the abolition threshold x". M05: a NAM plateau below x is unresolved, not support for total gain; a left shift is composition only after the percent removed is measured at the burst. M06: TCN-201 maxima 91 / 72 / 0 percent on GluN2A / triheteromer / GluN2B, glycine 3 µM in the source; the three-share solution is fragile (near-collinear: determinant about 0.12, condition number about 32, INFERENZA; maxima are low-glycine values; tonic Zn2+ moves the NAM coefficient 0.32 to 0.50) | 24607230 Fig 2 legend and Table 1 |
| 6 | same package, `experiments.tsv`, BE2 (and `existing_module_step_reused` X1–X2) | Add arms: NAM with and without a Zn2+ chelator; equilibration time and vehicle arm; burst-level NMDAR charge; glycine/D-serine for both NAM and TCN-201 arms; d-APV series against raised glutamate (M-N2, M-N8–M-N12). Cost note stays "High" | `output/new_measurements.tsv` |
| 7 | `needs/needs.json`, NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR | Add two transfer observations (recombinant ceilings; one native visual-cortex bound with its limits) and the open-measurement list; the file format cannot hold recording conditions or a matched-effect comparison (see format limits) | 24607230, 26185009 Table 2 |
| 8 | `cards/F04_nmdar_intervention_class.card.json`, `p4_fields.functional_evidence_available` | Keep "no subunit-selective drug applied to a Wwox system"; add that the removable share of a GluN2B NAM is bounded by composition and Zn2+ (transfer) | 24607230 |
| 9 | `generation_it39_20261109/questions_it39.md` (a built surface of `build_questions.py`) | Do not edit the file; it follows `investigations.tsv`, so row 1 reaches it by regenerating | — |

## Not proposed (and why)

* No new probe row, no `bridges.tsv` or `probe_links.tsv` row: the composition and ceiling statements are not a two-gene relation (no gene–gene link invented).
* No row for an AMPA antagonist: identity unresolved; the datum that would resolve it is a primary selectivity paper plus a measured fast-EPSC block in these slices (M-N5).
* No promotion of the 30 percent native bound as a ceiling.

## Format limits (precise)

* `investigations.tsv` `next_test` is one string: it cannot hold ordered arms with separate decision rules or a "compare only up to the ceiling" condition.
* `comparators.tsv` has no field for a maximum effect or a composition-dependent ceiling; `selectivity_limits` is free text.
* `needs.json` `observed` has no field for recording conditions (Mg2+, glycine, Zn2+, temperature, pH) and `intervention_direction` allows one direction on one entity, so a matched-percent comparison cannot be expressed.

## Reads still open (unopened, none required for this delivery)

Methods of 39406518 and 21789901 (a possible NAM-sensitive fraction inside plasticity papers); full text of Fischer 1997 (Ro 25-6981 maximum and conditions); Hansen supplement (oocyte bath, pH, Zn2+ state of the 32 percent baseline); native triheteromer share papers (Stroebel; Tovar).

## Closing pass (2026-11-09): what changed after the five final edits

The verifier re-checked the five late edits against the sources (`verify/audit.md`, "Closing pass"): the radiprodil number (rat 82 against rat triheteromer 45, human 91; Table 1 of 40994429), the provenance of the Mierau value (Table 2 value, not a figure read), the native bound not being a ceiling, and the fragility of the three-share solution were supported; the duplicated label was editorial.

**Changes in the conclusions: none to the decision or to proposal 1.** Two wordings were corrected in the package, and both bear on proposals already listed:

* Proposal 5 (M06 row): the fragility reason is near-collinearity of the three-share system (determinant about 0.12, condition number about 32, INFERENZA), with two qualifiers (maxima are low-glycine values; tonic Zn2+ moves the NAM coefficient from 0.32 to 0.50). The earlier reason "three subtracted terms" is withdrawn. The advice (the GluN2A arm can be dropped) is unchanged.
* The compact table of `README.md` no longer lists "NAM curve coincident up to its ceiling" as support for H_total_gain; it is unresolved, as `output/comparison.tsv` already said. Proposals 4 and 5 (BH2, M05) already carried the unresolved reading; nothing in them changes.

**Unchanged:** proposals 1, 2, 3, 4, 6, 7, 8, 9; the numbers (88 / 32 / 50 percent, radiprodil 82 / 45 / 91, Mierau 1.18 to 0.83); the 12 new measurements; applied count 0. Minor note from the verifier, not applied: the TCN-201 triheteromer IC50 sample size is 8 in Table 1 and 10 in the Results text of 24607230; neither figure is used in this package.
