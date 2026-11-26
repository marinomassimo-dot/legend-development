# Sheet batch 4: BATCH4_NMDAR_class_ketamine_memantine_dAP5_HE_20261119.md
Each numbered unit is a sentence of the repository sheet, in order. L = line in the sheet.


## ADV-098 batch 4: NMDAR class: d-AP5 beside the pore blockers, with the voltage and Mg2+ conditions (HE, 2026-11-19)
U4.1 (L3) **One line for SCI and IT (the finding that matters most here):** the holding potential, not the receptor, moves ketamine and memantine potency by 30 to 100 times in one 2024 document (about 0.5 to 0.8 microM at -60 mV against 15 to 53 microM at -40 mV), so **no ketamine-memantine potency order is readable**, no Mg2+-matched per-subunit IC50 was found by these routes, and d-AP5 sits on a different, agonist-dependent axis: the old d-APV-before-pore-blocker precedence rests on neither the simulation (one parameter, two labels) nor on a comparable potency datum.

## COMPARABLE? (which pairs can be set side by side, and the condition that decides each number)
U4.2 (L8) **Pore blockers against each other (ketamine, memantine): comparable only within one document and one holding potential.**
U4.3 (L8) The single document that records both agents on GluN2A and GluN2B in one patch-clamp protocol (CHEMBL6083260, 2024, human receptors in HEK293 cells, L-glutamate-induced response) reads, at -60 mV: ketamine 500 nM (GluN2A) and 510 nM (GluN2B), memantine 840 nM and 780 nM; at -40 mV: ketamine 53.3 microM and 15.2 microM, memantine 28.1 microM and 25.6 microM.
U4.4 (L8) **The holding potential, not the receptor, drives the 30- to 100-fold difference** (a pore block that weakens as the membrane is depolarised).
U4.5 (L8) At -60 mV the two agents differ by less than 2-fold; at -40 mV the order of the GluN2A values reverses (ketamine weaker).
U4.6 (L8) So no order between ketamine and memantine is read: it flips with the potential.
U4.7 (L8) This also settles my batch 1 remark that "the assay decides" the memantine value in that document: the assay difference there is the holding potential (-60 against -40 mV).
U4.8 (L9) **d-AP5 against the pore blockers: not comparable as one potency.**
U4.9 (L9) d-AP5 is a competitive antagonist at the glutamate site; its Ki or IC50 depends on the agonist concentration used (not in the ChEMBL text), and the Mg2+ and voltage conditions that shape pore-blocker values do not act on it in the same way.
U4.10 (L9) The two quantities are different and **no order is read**; d-AP5 is a tool.
U4.11 (L10) **Mg2+ per subunit (SCI's request): not found by these routes.**
U4.12 (L10) No row gives an IC50 per GluN2 subunit with a stated Mg2+ concentration.
U4.13 (L10) The only text that names Mg2+ is the [3H]MK-801 or [3H]TCP binding rows ("in the presence of Mg2+"), and those do not resolve the GluN2 subunit.
U4.14 (L10) The patch-clamp texts name the holding potential but not the Mg2+ concentration.
U4.15 (L10) A Mg2+-matched per-subunit IC50 for ketamine or d-AP5 has to come from the primary papers (SCI's delegate).
U4.16 (L11) **Repeated identical values are one origin.**
U4.17 (L11) For ketamine, a Ki of 180 nM appears on 22 rows with different brain preparations and species in one 2020 document (CHEMBL4680282); it is one transcribed value, not 25 measurements.
U4.18 (L11) For d-AP5, the same numbers (280, 460, 1640, 3710 nM) appear as an EC50 in CHEMBL1133464 and as a Ki in CHEMBL1143579: the same origin.

## d-AP5 (declared identity CHEMBL84612 = 2-amino-5-phosphonopentanoic acid, D configuration read from the SMILES; ChEMBL stores it without a name)
U4.19 (L14) **Targets and potency (21 rows, 19 on the NMDA receptor or its binding site; two of the 19, 170 and 2,260 nM, equal the ratios 280/1640 and 3710/1640 and look like subunit ratios stored as Ki):** per-subunit competitive antagonist values, rat recombinant GluN1a/GluN2x in Xenopus oocytes (CHEMBL4024770): Ki 0.39 microM (GluN2A), 2.8 microM (GluN2B), 5.9 microM (GluN2C), 21 microM (GluN2D).
U4.20 (L14) Another document (CHEMBL1143579, currents evoked by glutamate and glycine): Ki 280 nM (GluN2A), 460 nM (GluN2B), 1640 nM (GluN2C), 3710 nM (GluN2D).
U4.21 (L14) **Both documents agree on the subunit order (2A strongest, 2D weakest) and differ 6-fold on GluN2B; within each document the subunits are comparable**; across documents the magnitude is not.
U4.22 (L14) Binding: IC50 177 nM ([3H]CGS-19755 displacement), 880 nM and Ki 3.83 microM (rat cortical membranes, different radioligands); a cortical wedge assay IC50 3.7 microM.
U4.23 (L15) **Selectivity:** IC50 above 100 microM at kainate and AMPA receptor binding (rat cortical membranes); `NOT_ASSESSED` otherwise.
U4.24 (L16) **Rodent exposure:** not searched in this batch beyond SCI's own request (d-APV blood-brain barrier): see the next line.
U4.25 (L17) **Label:** none (a research tool); not searched.

## Ketamine (CHEMBL742, racemic; esketamine CHEMBL395091 is a separate record and not merged)
U4.26 (L20) **Targets and potency (342 rows; 40 on NMDA receptor subunit symbols, 18 of them human):** besides the 2024 document above: human recombinant GluN1/GluN2A IC50 1.26 microM and GluN1/GluN2B 5.0 microM (calcium flux, U2OS cells, FLIPR, 2011); GluN1/GluN2A 3.3 microM (oocytes, 2014); GluN1/GluN2A 6.1 and GluN1/GluN2B 3.2 microM in an excitotoxicity assay with dexamethasone (2010); CHO calcium-flux values in a 2025 document: GluN2A 25 microM, GluN2B 6.3 microM, GluN2C 4.0 microM, GluN2D 10 microM; MK-801 displacement IC50 0.61 to 0.86 microM in rat membranes and a 10 microM IC50 for the NMDAR-mediated EPSP in rat CA1.
U4.27 (L20) The IC50 values span 0.5 to 53 microM across assays (Ki rows go down to 0.18 microM): the potential, the readout (current, calcium flux, binding) and the cell system decide.
U4.28 (L21) **Selectivity:** 135 other (target, species) entries appear outside the human subunit rows (rat NMDA receptor rows, DrugMatrix panels, receptors, transporters): reported, not selectivity; `NOT_ASSESSED`.
U4.29 (L22) **Exposure and label:** held in the ketamine lanes of the repository (`it_ketamine_lanes_20261117` and ADV-050): not re-read here; mouse brain exposure of ketamine and memantine is on SCI's next narrow round.

## Memantine
U4.30 (L25) See batch 1 for the full row list.
U4.31 (L25) The per-document holding-potential finding above replaces the batch 1 sentence about two unexplained assays in CHEMBL6083260.

## What changes for SCI's exposure-effect choice (batch 4)
U4.32 (L28) Any potency for a pore blocker needs the **holding potential stated** before it is used; at the model's depolarised states a value read at -60 mV can be 30 to 100 times too low.
U4.33 (L29) The ketamine against memantine order flips with the potential: a mapping that places one above the other from a single IC50 is not supported.
U4.34 (L30) d-AP5 sits on a different axis (competitive, agonist-dependent): in the circuit model the identical J_N perturbation (see the normalisation note) hides that difference; the data do not hide it, and they do not give a Mg2+-matched per-subunit value for either agent.
