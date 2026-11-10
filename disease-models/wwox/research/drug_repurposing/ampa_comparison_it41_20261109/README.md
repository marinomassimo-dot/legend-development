# IT41 package A — the AMPA comparison: which tools, which pairing, what the result can and cannot separate (2026-11-09)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference. Reference genotype class only. One package, one producer, one independent blind verifier, one recheck of the substantive corrections. Task record `ledger/tasks/orchestrator/ORCH-IT41-20261109.json`. Design fixed before the search: `A1_design_before_search.md`. Built on `ampa_nmda_discrim_20261108/` (BH1, BE1, M07, M08) and `nmda_composition_discrim_20261109/`; nothing there is changed here.

## Decision this changes (labels: DATO / INFERENZA / IPOTESI)

* **The AMPA arm is a pair of two mechanisms, and perampanel is not the second one.** DATO (structures, GluA2; 27618672, 36857176): perampanel, GYKI 53655 and CP-465,022 occupy the same collar pocket with inhibitor-specific contacts. INFERENZA: a noncompetitive 2,3-benzodiazepine plus perampanel is one site seen twice (the same lesson as the ifenprodil-site NAMs); the independent partner is the competitive NBQX (agonist site; class knowledge, no primary text on surmountability read). Perampanel stays as a same-site cross-check (occlusion test M-A6), not as a second line of evidence.
* **The "GYKI 52466" of the module is not the compound the tissue and structure data are for.** DATO: every slice and structure paper read (27618672, 27838344, 35103859) uses GYKI 53655 (also written GYKI-53655, LY300168 in the Bleakman abstract); the GYKI 52466 kinetics carried in `probes.tsv` (k_on 1.6e5 per M per s, k_off 3.2 per s) belong to Donevan 1993 for GYKI 52466 and are abstract-level here. The catalogue record named "Gyki53784" is neither (Harness identity delivery; not rebuilt here). The arm therefore names GYKI 53655 where tissue data exist and carries the 52466 values as a separate, abstract-level row.
* **The verified-block tool does not reach a near-complete block at 10 µM in tissue.** DATO (27838344, mouse slices): 10 µM GYKI 53655 removed 80.5 percent (entorhinal, n = 5) and 89 percent (barrel cortex layer V, n = 5) of the evoked peak, IC50 2.5 µM; about 94 percent was reached at a higher concentration in entorhinal layer III (n = 3). The "about 90 percent" survival threshold of BH1 is therefore a design value at the edge of what the tool does at 10 µM; the achieved block is a variable (M-A1).
* **The nearest tissue precedent is unfavourable to an AMPA-led reading, with limits.** DATO (27838344 Fig 5, transfer): evoked Up states of mouse barrel cortex layer V persisted under 10 µM GYKI 53655 (n = 5) and were abolished by 50 µM d-AP5 applied afterwards in the same cells. INFERENZA: the Up states were evoked by a pulse the authors say supplied depolarisation, the block was verified in other cells, and spontaneous Up states were not tested; it does not settle AMPAR dependence of spontaneous bursts.
* **Name the arm "AMPA/kainate" unless the window is measured in the preparation.** DATO: NBQX binding Ki 0.077 µM at GluA2 and 2.6, 5.4, 3.4 µM at GluK1-3 (35955932, radioligand, sf9 membranes, 4 C; a window of about 34- to 70-fold by arithmetic, binding not current); perampanel inhibits GluK2 at 58 µM and, at abstract level, GluK5-containing receptors at AMPA-comparable potency, and in neurons kainate-evoked current at the AMPA IC50 (25229608 reused): it is the weakest arm for a window. DATO (abstract only): 2,3-benzodiazepines inhibit GluR5/GluR6 kainate currents less than 30 percent at 100 µM (Bleakman).
* **Surmountability is a graded property, not a binary one.** DATO (25229608 as re-read by the audit): perampanel's AMPA IC50 shifted 0.4 to 0.9 µM over 10-100 µM AMPA, about two-fold, with equal block across kainate levels. INFERENZA: the noncompetitive tools are largely, not entirely, insensitive to agonist level in culture; NBQX and d-APV (both competitive) share the weakness that glutamate rises inside a burst, so a coincident NBQX/d-APV curve cannot be read as equal need, whereas noncompetitive-versus-d-APV is a comparison of unlike tools.
* **A3 not triggered; no new molecule.** No known option is shown unable to meet the five demonstrations of A1 (kainate "stated as not separated" is allowed; NMDAR neutrality and block fraction are preparation measurements). The verifier checked this against the five demonstrations; the producer's stated premise was partly wrong (a higher concentration was tested) and was corrected. No search by missing property was run.

## Status of the deliverables (nothing applied to a consumer)

| Layer | State |
|---|---|
| Sources newly read, with receipts | 6 staged in `research/receipt_staging/it41a/` (copies in `output/receipts/`), all pass `staged_receipt_check.py --check-doi`, none recorded: 27618672 Yelshanskaya 2016 (text), 27838344 Digby 2017 (Fig 5 viewed), 35103859 Dominguez-Sala 2022 (Fig 6 viewed), 36857176 Gangwar 2023 (Fig 4 viewed), 35955932 Chalupnik 2022 (Table 1, Methods), 34653311 perampanel in human cortical dysplasia slices (perampanel results only); all partial full text |
| Reused, no new receipt | 25229608 Chen 2014 perampanel in culture (earlier staged receipt; agonist-level figures re-read by the verifier) |
| Abstract only | Donevan 1993 (7678966), Bleakman 1996 (9076748), Hanada 2011 (21635236), Sheardown 1990 (2154034), Taniguchi 2022, Yamada 1996, Potschka 1998, Hale 2024, 32901915: used only for what an abstract states, labelled abstract_only |
| Not reached | full texts of Donevan, Bleakman, Sheardown, Hanada: bot check or 403 at the publisher in the producer's plain-curl attempt and again in the verifier's own attempt, not retried by another route; Yelshanskaya figures and supplement (no open image route) |
| Verifier (first pass) | 16 propositions: 9 supported, 7 partly, 0 not supported; 40 evidence rows, 3 defective; substantive errors: a false "different laboratories", abstracts unused for items called unverified, an incomplete perimeter for perampanel in slices, surmountability resting on a test of other properties, and a stale "higher concentration not tested". All corrected. |
| Verifier (recheck) | 11 of 11 substantive rows correct, three cosmetic leftovers (a depth cell, a table-versus-text concentration inconsistency inside Chen 2014, a unit printed as "um" in the Hanada abstract), fixed by the Orchestrator |
| Delivered tables | `output/decisive.tsv` (20), `output/comparison.tsv` (3), `output/new_measurements.tsv` (7), `output/names_used.tsv` (22), `output/evidence.tsv` (52), `output/figure_notes.tsv` (6), `output/queries.tsv` (21) |
| Proposals | `consumer_delta.md`: 10 rows; applied: 0 |

## The compact comparison (full cells: `output/comparison.tsv`)

| Row | Tool and identity | Documented action and limit | Strengthens the AMPA-led reading | Weakens it | Unresolved |
|---|---|---|---|---|---|
| C2 | GYKI 53655 (noncompetitive; name mismatch with 52466 for Harness) | IC50 14.5 µM recombinant, 2.5 µM slice EPSC; 80.5-89 percent block at 10 µM; reversible in the cingulate slice at 33-34 C; no verified block with a burst readout in any slice paper read | bursts persist at a measured block above about 90 percent in the same medium | n/a: abolition is not separating | persistence at 80-90 percent; kainate window; NMDAR neutrality in the preparation |
| C1 | NBQX (competitive; primary text unreached for surmountability and glycine site) | binding window of 34- to 70-fold over GluK1-3, no functional IC50 read | same persistence under a verified block | abolition is expected under NMDAR-regenerative and general-drive explanations too | surmountability numbers; glycine-site action; kainate in the preparation |
| C3 | perampanel (same pocket as C2; weakest for a kainate window) | IC50 0.89 µM GluA2; slow culture kinetics; abolished ictal events at 10 µM in human dysplasia slices in high K+, low Mg2+ (not block-verified) | agreement with C2 at matched block tests the compound, not the mechanism | disagreement points to a site-external or kainate action | tissue kinetics and washout |

Reading rule (INFERENZA): bursts persisting under a verified near-complete block remove the AMPA-led reading for this preparation; bursts abolished do not separate AMPAR-led from NMDAR-regenerative drive, general loss of drive, or a presynaptic loss, because AMPA block can remove the depolarisation that relieves the Mg2+ block. The order is: AMPA tool to a measured steady block, d-APV only if bursts persist, matched curves against d-APV on two metrics with a release-reducing control (M08).

## What public sources resolve, and what needs a new experiment

Resolved from public sources (recombinant, culture, other regions and ages, partial full text): that the 2,3-benzodiazepines and perampanel share a pocket; potencies and block fractions of GYKI 53655 in two mouse slice preparations; NBQX binding window; perampanel kainate behaviour; one evoked-Up-state precedent. **Not resolvable from literature, to be measured in the Wwox slice** (`output/new_measurements.tsv`): fast-EPSC block fraction and time to steady state in the burst-recording medium (M-A1); NMDAR EPSC at the working concentration (M-A2); resting potential, input resistance and spike width under the tool (M-A3); block fraction at low and high stimulation (M-A4); the kainate-receptor part (M-A5); the occlusion test (M-A6); washout order (M-A7). Other literature does not stand in for these.

## Counter-evidence and limits

* The Digby Up-state result favours the NMDAR-regenerative reading in barrel cortex, but it is evoked and its block was verified in other cells.
* Perampanel abolished ictal events in human dysplasia slices (34653311), which says the drug acts on burst-like events in tissue, not that the block was verified or that the Wwox burst is AMPAR-led.
* A burst response to an AMPA tool does not show that the receptor is altered in Wwox.
* The 65-fold GluK2/GluA2 perampanel contrast is not like-for-like (same laboratory, different protocols and modulators).
* The medium of Digby's Up-state work (3.5 mM K+, 1 mM Mg2+) is the nearest to the Wwox incubation medium among the sources read; the recording Mg2+ of the Wwox slice is unstated.

## Novelty

* `new_to_legend`: the same-pocket status of perampanel and the 2,3-benzodiazepine as a design constraint for the pairing; the GYKI 52466 / 53655 name mismatch inside the module's AMPA arm; the measured binding window of NBQX; the evoked-Up-state precedent. Literature novelty: not assessed.
* `already_in_legend`: BH1 and its kill condition, perampanel culture kinetics, the surmountability concern for d-APV, the kainate gap (AB14).
* No new molecule (A3 not triggered; checked by the verifier against the five demonstrations).

## Queries run

21 rows in `output/queries.tsv` (Europe PMC REST, NCBI efetch PMC, PubMed tool, the open-data bucket, plain-curl publisher attempts recorded as unreachable and not retried).
