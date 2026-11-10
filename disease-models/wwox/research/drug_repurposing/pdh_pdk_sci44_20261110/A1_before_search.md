# SCI44 package A, A1 — the PDH/PDK premise and the frame, written before any new search (2026-11-10)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI / ESPANSIONE. Task record `ledger/tasks/orchestrator/ORCH-SCI44-20261110.json`. A later change to this file is a dated addendum, not an edit.

## S0 — order of the packages, and why

* **State found.** `main` = 380a4ee3 (SCI43 landed). IT43 consumed the SCI43 delivery in c82a1bff (consumer rows 1-7 and 11 applied, 26 receipts recorded, ledger 1,599), so no SCI43 hand-off is open on the IT43 side. IT44 (task `ORCH-ROADMAP-IT44-20261110`, branch task/it44, queue P0-P9) owns the shared consumers; its folder `generation_it44_20261110` holds a relation search (`relations_s3.tsv`, `activity_search.py`) and touches neither PDK nor Ro 25-6981. `open_questions_map.tsv` still lists IT43-Q01 as OPEN (Ro 25-6981, task/it43). The SCI43 residue that is mine, not IT43's, is package C (eight producer-read rows, the juvenile layer II/III Ba2+ share).
* **Order kept: A (PDH/PDK), then B (Ro 25-6981), then C.** Reason, as a change expected in the research: IT43-Q02 (kinase isoform by cell type) is the only open question whose answer rewrites rows the engine already produced (the isoform rows of AZD7545 and VER-246608 and the design of the premise measurement) and it can be settled largely by reading processed public tables; B closes a single compound's tier and C only moves a premise of one INV-18 arm. A is also the one where an apparent lever may be inert or counter-productive, so the frame must be written first.

## Decision this package can change

1. Whether the S9 lever (PDK inhibition) keeps a **cell-type- and isoform-resolved** premise measurement (amount and phosphorylation at three E1 sites, activity before and after dephosphorylation, four kinase transcripts) or a generic one — i.e. whether the premise sample must be sorted or at least carry cell-type markers.
2. Which row of the typed inhibitors the premise would exercise: a pan-isoform reference (dichloroacetate), a second chemotype with four isoform rows (VER-246608), or an isoform-biased probe (AZD7545), and whether any of them is the wrong tool for the isoform a given cell expresses.
3. Whether an alternative action (substrate supply, phosphatase side, enzyme cofactor, pyruvate transport, lactate side, genetic arm) is the better *first* arm than a kinase inhibitor.

## What is measured, what is inferred (from the held records; nothing re-read)

| Layer | State | Label |
|---|---|---|
| Observation in WWOX | glycolytic signature (non-neural, organoid); kinase transcript **not up** in the KO organoid (PDK1 not up, PDHA1 up; six libraries, age-confounded); one PDH activity measurement, **non-neural** fibroblast pool, partial depletion, n not stated: no difference, lactate up, PDK transcript up in one condition; fly lactate/Ldh up only with Abeta42; ketogenic diet response in 3 of 5 individuals (lactate 2.4 to 3.3 mmol/L in one). No PDH amount, phosphorylation, flux or lactate/pyruvate pair in a neural WWOX-deficient system | DATO (metabolic_inv07_20261107) |
| Mechanism | PDK/PDP phosphorylation limits PDH; one phospho-site gives neither activity nor the responsible kinase; PDK1 alone phosphorylates all three E1 sites in vitro (abstract) | DATO abstract + INFERENZA |
| Isoforms and cells | not read in any held record; IT43-Q02 | open |
| Compound action | AZD7545 PDK1 pIC50 7.43, PDK2 8.19 (one assay, abstract names no isoform or species; PDK3/PDK4 unknown); VER-246608 pIC50 7.46/7.08/7.40/7.04 (a different assay); dichloroacetate one family record, no isoform | DATO as recorded, primary not read |
| Functional effect | none in a WWOX preparation; the one randomised human trial of the reference (mitochondrial disease) was stopped early for peripheral nerve toxicity (abstract) | DATO abstract |

Expression of a kinase transcript, phosphorylation of PDH, lactate and flux are **four different measures**; none is used here as a proxy for another.

## Competing explanations (from the earlier package, regrouped for the lever question)

* **H-A. Phosphorylation-limited PDH in the affected cell** (the premise of the lever). Inhibition would raise PDH activity.
* **H-B. PDH not limited; the glycolytic shift is compensatory or consequential** (supply, redox, activity, culture state). Inhibition adds load or does nothing; the kinase transcript fall would be the cell's own correction.
* **H-C. A lactate-side or transport-side change independent of PDH** (LDH, MCT, mitochondrial pyruvate carrier). A kinase lever is mis-aimed.
* **H-D. Cell-type division of labour.** The affected compartment is a glycolytic lactate exporter (astrocyte or oligodendrocyte-lineage supply role) while neurons oxidise: lowering PDK where lactate export is needed removes a function; raising it in neurons does nothing.
* **H-E. Isoform mismatch.** The relevant cell expresses an isoform that the available inhibitors act on weakly, or on which they have never been tested (unknown is not zero).

## Fixed before searching: what each result would favour

| Result of the reading | Moves |
|---|---|
| Neurons, OPC/oligodendrocytes and astrocytes express different dominant kinases (for example neurons PDK2-dominant, glia PDK4-dominant) | H-D and H-E up; premise sample must be cell-resolved; isoform rows decide the tool per cell |
| One isoform (the broad one) dominates every cell class | premise measurement need not be sorted for isoform reasons; pan or PDK2-biased tool is coherent across cells; H-E down |
| The relevant cell class expresses only isoforms on which the inhibitors have no tested row | lever drops to "no tested tool", not refuted; a genetic arm replaces a compound arm |
| Transcript present but protein absent or at the noise floor | expression does not make the lever plausible for that cell; RNA is not abundance |
| AZD7545/VER-246608 primary papers show tested species/constructs differ from human, or show activation of one isoform | a "typed inhibitor" row becomes species- or isoform-limited; possibility of **worsening** is documented rather than assumed |
| Mechanistic literature (outside WWOX) shows PDK induction is compensatory in neurons under stress, or that PDH phosphorylation protects against excitotoxic load | H-B up; inhibition becomes a risk arm (a negative control for harm), not a benefit arm |

## What would make PDK inhibition inert for this question

* PDH already unrestrained in the affected cell (the available transcript sign points this way).
* The relevant cell is not the one that expresses a kinase the tool reaches.
* The lactate change is explained by an LDH or redox change that PDH state does not touch.
* Neurons depend on glycolytic ATP at the moment of burst and PDH acceleration does not change that (a functional, not a biochemical, outcome; no source needed to state it as an open point).

## Possibility of worsening a compensatory response (stated, not assumed)

Releasing PDH increases pyruvate entry into the mitochondrion: more NADH and potentially more reactive oxygen species and a heavier load on a respiratory chain with an unmeasured limit (INV-07 explanation: downstream respiratory limit); less lactate export to partner cells; and a documented peripheral nerve toxicity of the reference in one human trial. A recollection to be checked in the reading, **not a datum**: at least one lipoamide-site tool (AZD7545 class) is described in structural work as having isoform-dependent effects, possibly activating one isoform under some conditions; this is an unverified background statement and is only a reason to ask the producer which isoforms were tested and with what result.

## Predictions fixed before any new reading (priors, recorded so they can fail)

Written from background knowledge, unverified; to be scored in A2:
* P1. PDK2 is detected in all four cell classes (neurons, astrocytes, oligodendrocyte-lineage, microglia) at the highest or near-highest level among the four kinases.
* P2. PDK3 is the lowest or absent in cortical cell classes.
* P3. PDK4 is higher in astrocytes (or endothelium) than in neurons.
* P4. PDK1 in cortical cells at physiological conditions is low relative to PDK2.
* P5. Where RNA and protein are both available for the same cell class, the rank order of the four kinases is not identical.

## Alternative actions to be written in A4 before any new compound name

Written now so the search cannot choose the frame: (a) lower the kinase activity (the S9 route); (b) raise the phosphatase side (PDP) or its calcium dependence; (c) supply a PDH-bypassing substrate or fuel (the ketogenic route, ketone bodies, acetate; a substrate-supply question, not a PDH defect); (d) enzyme cofactors and cofactor handling (thiamine, lipoate, CoA and NAD+ availability); (e) mitochondrial pyruvate transport; (f) the lactate side (LDH, MCT) if lactate-driven harm is shown; (g) a genetic arm (isoform-selective knockdown) that tells which kinase the cell uses before any compound; (h) upstream drivers of the kinase (HIF-linked induction, INV-19). Each gets action, context, premise, counter-evidence, refuting experiment, state against LEGEND (A4).

## What no further literature search can resolve (stated now)

Whether PDH is phosphorylation-limited in a WWOX-deficient neural cell, whether the glycolytic shift is cause or compensation, and whether any PDH acceleration helps a functional outcome. These need the premise measurement (INV-07 step 2, sharing lysates with INV-19) and a functional readout; they are not commissioned here.

## Addendum 2026-11-10 (after A2-A4 and both verifications; the text above is unchanged)
* **Priors scored:** P1, P2 and P4 failed; P3 and P5 held (`output/priors_scored.tsv`, re-checked by the verifier from its own extraction). The frame's explanation H-D (cell-type division of labour) and H-E (isoform mismatch) rose, as written in the outcome table; the premise sample must be cell-resolved.
* **Frame statement withdrawn:** "a recollection ... AZD7545 class may activate an isoform under some conditions" was only a recollection; it is now a measured fact for the core-free kinase (PDK3 10-fold, PDK4 2.8-fold stimulation; core-bound PDK1 and PDK3 inhibited), with PDK2 unmeasured.
* **Alternative actions (a-h):** (a) done; (b) phosphatase activation: no tool reached by the relation path or by name; (c) fuel/ketone: tested as a control (triheptanoin) and as KATP/GIRK/A-type coupling (BHB); (d) cofactors: nothing found by name in neural cells beyond a PDH-deficient mouse acetate rescue (abstract); (e) pyruvate transport: UK5099 read; (f) lactate side: oxamate, stiripentol, astrocytic Ldha read; (g) genetic arm: kept as the reference of the design; (h) HIF upstream stays with INV-19.
* **The link opened by verification:** lactate-closed KATP (PH4). It was not in the frame; it came from the verifier's counter-example to the producer's absence claim.
