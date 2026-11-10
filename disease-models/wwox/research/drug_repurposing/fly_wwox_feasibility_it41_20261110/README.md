# IT41 light queue — a Wwox-loss model in Drosophila: public feasibility, the phenotype to verify first, and the one question the fly could ask (2026-11-10)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference. Reference genotype class only. A question and a preliminary feasibility, not a commissioning of experiments; no external contact, spend or registration. One producer, one independent blind verifier, one recheck of the substantive corrections. Task record `ledger/tasks/orchestrator/ORCH-IT41-20261109.json`. Nothing here reopens the AMPA, NMDA or BNIP3 packages.

## Decision this changes (labels: DATO / INFERENZA / IPOTESI)

* **The fly is a feasible but unverified loss-of-function system, and its first task is to reconcile two sleep datasets, not to reproduce one.** DATO (partial full text): the only quantified loss readout is sleep, in two genotypes from two laboratories that point in opposite directions on the light-phase metrics each paper reports. The f04545 hypomorph (BL18783, mRNA about 7 percent, whole-fly qPCR; males, one control, no rescue; 39952983) shows less day sleep and shorter day bouts and more night sleep; neuronal or glial TRiP knockdown (BDSC 51747; 42909904) shows longer light-phase sleep episodes and a higher active-to-inactive probability, a shorter lifespan (neuronal 57 to 42 days, glial 74 to 70 days) and no significant climbing effect at low power. INFERENZA: the metrics differ, so the comparison needs one pipeline, one background and one sex before anything else.
* **No published rescue of any Wwox-loss phenotype was found in the sources opened.** DATO: the 2005 report of a radiation-sensitive Wwox mutant rescued by fly or human WWOX (16007179, abstract only, with an erratum on record) is superseded: a later paper from the same group states that background mutations, not the targeted Wwox mutations, caused that phenotype (21075834, partial full text; its Introduction); Wwox1 homozygotes are viable and fertile. The only human WWOX arm published is an overexpression against amyloid toxicity, not a rescue of loss.
* **The amyloid and tau work is a different question and is not transferred.** DATO: Wwox knockdown worsens a transgenic Abeta42 toxicity and upregulation helps only with the transgene (CRISPRa tested without amyloid; the fly and human WWOX constructs tested only with Abeta42); none of this is a Wwox-loss phenotype.
* **Do not assume an epileptic phenotype.** No source tested seizure-like behaviour, mechanical-shock sensitivity, neuromuscular-junction physiology or any neuronal electrophysiology in a Wwox-loss fly (none found; abstract-level search strings, repeated by the verifier; a 2020 review of developmental and epileptic encephalopathy in Drosophila says the same up to 2020). The absence of a gross phenotype is not the absence of any studyable function: finer readouts with source support are lifespan, sleep architecture, wing-vein ROS (neuronal knockdown), the Egr/TNF eye modifier and Scrib-clone elimination (stress-dependent, with the genotype of the opposite sign to the amyloid context).
* **Resources are named in papers, none is confirmed as held.** DATO: identifiers are printed for the hypomorph, three RNAi lines (VDRC v22536 and 108350, BDSC 51747), CRISPRa lines, drivers and reporters; `confirmed_in_source` 14 rows, `catalogue_entry_only` 7, `not_found` 2 (`output/resources.tsv`). UAS-dWwox and UAS-hWWOX are labelled "this study" with no repository number; BDSC returned 403, the Alliance 429 and FlyBase an empty shell, none retried by another route. A Wwox antibody exists (anti-C-DmWWOX, Western and immunostaining) and adult protein is reported absent in Wwox1 and f04545 (the 2011 paper; its Supplementary Fig S1 unseen), while endogenous protein in imaginal discs is too low to detect.
* **A variant comparison is limited.** DATO/INFERENZA (the verifier re-aligned the proteins itself): overall identity 50.0 percent (67 percent positives); P47 to P42, R54 to R49, S14 to S9 and the catalytic Y293 to Y288 are conserved; G372 to S367 and Y33 to C28 are not; the N-terminus is gapped and low confidence. A human missense change is testable only as a human WWOX transgene in a null background.
* **The pharmacological question the fly could ask (IPOTESI):** if a Wwox-loss behavioural readout is reproduced and rescued, does it change with Nmdar1 gene dosage? Genetic reduction first (a 2 by 2 epistasis design, Wwox null against control), APV or MK-801 only as a second arm; the confounds are that Nmdar1 knockdown and MK-801 themselves lower fly sleep and that the one effective MK-801 amount killed 3 of 16 flies in the dose-finding series. DATO: the larval NMJ receptors are non-NMDA (AMPA-like) and the fly has a single NR2 and an Mg2+ block; INFERENZA: the fly cannot discriminate GluN2A from GluN2B, AMPA from kainate at central synapses, cortical burst firing, or a drug effect on a human variant. The mitochondrial and hypoxia axis was not chosen as the question.

## Status of the deliverables (nothing applied to a consumer)

| Layer | State |
|---|---|
| Sources newly read, with receipts | 11 staged in `research/receipt_staging/it41c/` (copies in `output/receipts/`), all pass `staged_receipt_check.py --check-doi`, none recorded: partial full text for 26023770 (Nmdar1 and sleep), 22681692 (fly NMDAR, Mg block), 26596173 (larval NMJ receptors, receptor statement only), 21075834 (Idh and Wwox, background mutations); partial re-reads of held sources for the fly questions only (42909904, 39952983, 26302329, 34210081); abstract only: 16007179, 26390919, 17395332 |
| Not reached | stock-centre records (BDSC 403, FlyBase empty shell, Alliance 429); 2006 erratum text; 2011 paper Supp Fig S1; Marrus 2004 full text; full texts of 16007179, 26390919, 17395332 |
| Verifier (first pass) | 12 propositions: 8 supported, 4 partly (D04, D06, D07, D11), 0 unverifiable; one clause not supported (the 2005 radiation phenotype as a current datum); 35 evidence quotes verbatim, 6 defective notes; three substantive errors: the superseded 2005 phenotype, "no protein detection" false as written, the sleep datasets' disagreement unstated. All corrected. |
| Verifier (recheck) | 12 of 14 substantive items fixed; two residuals (an unscoped absence wording, a metric comparison to be marked INFERENZA) and two editorial leftovers fixed by the Orchestrator |
| Delivered tables | `output/decisive.tsv` (12), `output/resources.tsv` (23), `output/feasibility.tsv` (12), `output/evidence.tsv` (40), `output/figure_notes.tsv` (7), `output/queries.tsv` (13) |
| Proposals | `consumer_delta.md`: 4 rows; applied: 0 |

## Counter-evidence and limits

* The fly has one hypomorph with one control and two knockdown datasets whose metrics differ; no rescue of the loss readouts exists.
* A genetic interaction with Nmdar1 would show that the readout depends on that receptor in the fly, not that WWOX deficiency alters NMDAR in human neurons.
* Absence claims are perimeter statements ("none found"), not proofs of absence.
* Stock availability is not confirmed; no stock centre or author was contacted.

## Novelty

* `new_to_legend`: the 2005 radiation rescue is superseded by a background-mutation statement; the two fly sleep datasets point in opposite directions on the light phase; an antibody and protein-absence data exist for the f04545 and Wwox1 flies; the conservation map of the human catalytic and phosphorylation residues in the fly protein. Literature novelty: not assessed.
* `already_in_legend`: the amyloid-context work and the fly Wwox as a modifier of other genes (`modifiers_it12_p1b_20261031/`, `recovery_it10_p23_20261031/`).
* No compound proposed.

## Queries run

13 rows in `output/queries.tsv` (PubMed tool, Europe PMC REST, NCBI efetch PMC, the open-data bucket, stock-centre pages recorded as unreachable and not retried).
