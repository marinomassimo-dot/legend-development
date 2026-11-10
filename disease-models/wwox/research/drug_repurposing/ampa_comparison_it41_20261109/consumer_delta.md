# Consumer delta — IT41 package A, the AMPA comparison (proposals only; nothing applied)

Task record `ORCH-IT41-20261109`. Every row names the consumer file and row, the proposed change, the source and the read depth. The integrating session (IT41) decides; this package edits none of these files, no ranking, no dashboard, no need. Paths below are relative to `disease-models/wwox/research/drug_repurposing/`.

**Point of the generative path that should use the result.** The step that turns BE1 / IT40-Q01 into conditional hypotheses and comparators should read `output/comparison.tsv` rows C1-C3 as three conditional templates (each cell carries DATO / INFERENZA / IPOTESI and the measurement that closes the condition) and `output/new_measurements.tsv` M-A1 to M-A7 as the list of conditions; `output/names_used.tsv` is the bridge to the identity delivery of Harness (`identity_it41_20261109/`, not rebuilt here).

## What changes in the conclusions, and what does not

| Changes | Does not change |
|---|---|
| The AMPA arm is a pair of two mechanisms: a noncompetitive 2,3-benzodiazepine as verified-block tool and the competitive NBQX as independent partner; perampanel is the same pocket as the benzodiazepine (cross-check only) | BH1 and its kill condition (survival under a verified block); the order rule BE4; the need for the NMDAR-regenerative, general-drive and state rivals to stay in the matrix |
| The tissue and structure data are for GYKI 53655, the module carries GYKI 52466 kinetics (Donevan, abstract-level); two compounds, name mismatch for Harness | d-APV as the reference antagonist; the matched-effect design M08 |
| 10 µM GYKI 53655 gives 80.5-89 percent block in tissue, so the 90 percent design value is at the edge and the achieved block is a variable | The wording that abolition after AMPA block does not separate AMPAR-led from NMDAR-regenerative drive |
| The arm is "AMPA/kainate" unless the window is measured; perampanel is the weakest tool for a window | The statement that no AMPA or kainate drug has been applied to any Wwox system |
| One evoked-Up-state precedent (barrel cortex) is unfavourable to the AMPA-led reading, as transfer | The new measurements stay with the Wwox preparation |

## Proposals

| # | Consumer and row | Proposed change | Source and depth |
|---|---|---|---|
| 1 | `ampa_nmda_discrim_20261108/output/probes.tsv`, row NBQX (line 6) | Add: binding Ki 0.077 µM GluA2 and 2.6, 5.4, 3.4 µM GluK1-3, 152 µM GluK5 (radioligand, sf9 membranes, 4 C; a binding window of 34- to 70-fold, not a current); surmountability and glycine-site action stay abstract-level; no functional IC50 read; change `depth` from `use_only` to `partial (binding table read)` | 35955932 Table 1, Methods (partial full text); Sheardown abstract |
| 2 | same file, row Perampanel (line 7) | Add: same collar pocket as GYKI 53655 and CP-465,022 (structures); GluK2 IC50 58 µM against 0.89 µM GluA2 (not like-for-like: same laboratory, different protocols); kainate-evoked current at the AMPA IC50 in neurons (reused); GluK5-containing receptors at abstract level; ictal events abolished at 10 µM in human dysplasia slices (not block-verified); agonist-level IC50 shift 0.4 to 0.9 µM over 10-100 µM AMPA | 27618672, 36857176, 34653311 (partial), 25229608 (reused, re-read by the verifier), Taniguchi abstract |
| 3 | same file, row GYKI 52466 (line 8) | Keep as the prototype row, change `depth` to `abstract_only` for the kinetics (origin: Donevan 1993, not a citing paper); add a new row GYKI 53655 (name_mismatch with 52466; Harness decides the catalogue match): IC50 14.5 µM recombinant (cyclothiazide possibly present), 2.5 µM slice EPSC, 80.5 / 89 percent block at 10 µM, reversible in cingulate slices at 33-34 C, Down-state potential unchanged (-62.7 against -63.5 mV, entorhinal) | 27618672, 27838344, 35103859 (partial); 7678966, 9076748 (abstracts) |
| 4 | same package, `hypotheses.tsv`, BH1, columns `compound_or_probe` and `discriminating_experiment` | Replace "perampanel is the compound whose mechanism was read" by: verified-block tool = noncompetitive 2,3-benzodiazepine (GYKI 53655 where tissue data exist); independent partner = NBQX; perampanel = same-site cross-check with an occlusion test; name the arm AMPA/kainate; add the Digby evoked-Up-state datum as transfer (D06-D07); keep the kill condition | `output/comparison.tsv` C1-C3, D01, D04-D07 |
| 5 | same package, `prediction_matrix.tsv`, M07 and M08 | M07: replace the tool statement as in row 4 and state the achieved block as a variable (80-89 percent at 10 µM in tissue). M08: NBQX with d-APV is a comparison of two surmountable tools (shared weakness); a noncompetitive tool with d-APV is unlike tools; the agonist-level shift of perampanel is about two-fold in culture, so "non-surmountable" is graded | D02, D03, D05, D14 |
| 6 | same package, `experiments.tsv`, BE1 | Add arms and measurements M-A1 to M-A7 (block time course, NMDAR EPSC at the working concentration, intrinsic properties, block at low and high stimulation, kainate component, occlusion test, washout order); the cost note stays "Moderate" | `output/new_measurements.tsv` |
| 7 | `comparators_it39_20261109/output/comparators.tsv` | No AMPA comparator row exists for INV-05 (line 31 is perampanel for INV-10): add rows for NBQX, GYKI 53655 and perampanel with `selectivity_limits` and `what_it_does_not_separate` from rows 1-3 | `output/comparison.tsv` |
| 8 | `needs/needs.json`, NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR | Add transfer observations (block fractions of GYKI 53655 in slices; the evoked-Up-state result; no slow non-NMDA component in barrel cortex III and V) and the open-measurement list; the file format cannot hold recording conditions or a matched-effect comparison (same limit as the NMDA package) | 27838344, 35103859 |
| 9 | `cards/F04_nmdar_intervention_class.card.json`, `p4_fields.functional_evidence_available` | Keep "no subunit-selective, pore-blocking, glycine-site or AMPAR drug applied to a Wwox system"; add that the two noncompetitive AMPA tools share a pocket | 27618672, 36857176 |
| 10 | `generation_it40_20261109/next_investigations_it40.md`, A1 and A2 rows (IT40 file, unmerged) | A1 is partly answered: NBQX binding window and the structure/kinetics of the noncompetitive tools are read; the primary mechanism papers for NBQX and GYKI 52466 stay abstract-level or unreached (bot checks); A2 (identity) is Harness's. B3 (BE1) is served by `comparison.tsv` | this package |

## Not proposed (and why)

* No new probe, bridge or `probe_links.tsv` row: the statements concern tools, not a two-gene relation.
* No kainate-selective tool and no new molecule: A3 not triggered.
* No promotion of the Digby evoked-Up-state result to evidence about the Wwox burst.

## Reads still open (none required for this delivery)

Full texts of Donevan 1993, Bleakman 1996, Sheardown 1990 and Hanada 2011 (publisher bot checks; abstract-level statements only); the Yelshanskaya supplement and figures; a primary text on NBQX surmountability and glycine-site action; Hale 2024 and Taniguchi 2022 full texts; 32901915 beyond its abstract.
