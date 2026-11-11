# SCI45 package P1 — pH, K2P conductances (TASK-1, TASK-3, TREK-1) and the instruments that separate the explanations (2026-11-11)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference; no claim on WWOX; no compound is promoted. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI / ESPANSIONE. Task record `ledger/tasks/orchestrator/ORCH-SCI45-20261111.json`. One producer (sonnet/medium, 95 turns), one blind verifier (sonnet/high, 104 turns), sequential; the substantive verifier finding was rechecked by the Orchestrator in the source text. Paths are relative to this folder.

## Answer first

**What became possible.** The DREAM chain (raised lactate, lower pH, closed TASK-3, higher Rin and depolarised rest) is now a *measured* chain with its weakest links named, and it narrows to one testable route.
1. **TASK-3 is not the pH sensor in the range a slice can reach** (recombinant pH50 6.3-6.5; 6.8-7.0 only in two abstracts). The coda's TASK-3 link (KP2) is refuted as quantitatively sufficient.
2. **The route that survives is a closed TREK-1 (and, less likely, TASK-1) pool**, and only under stated conditions: interstitial pHo lower in the knock-out by about 0.2-0.3 unit, a TREK-1 pool near half of the conductance, and a steep pH response. The size check (`size_check_*.tsv`) gives the threshold: with the one fitted TREK-1 slope (about 0.7) or slope 1 the published pair is **not** reached at 0.3 unit; with slope 2 it is reached at 0.2-0.3.
3. **The lactate-to-pH step is demoted**: perfused tissue pHo moves little with activity, the slice has a larger depth gradient than any activity transient, no source reports pHo after a physiological lactate rise, and an intracellular acidification is clamped by the 10 mM HEPES pipette of the published recordings and would, for TREK-1, open rather than close the channel.
4. **The decision rule for the shared pH measurement**: the tissue-pH record already proposed for the GluN2B comparison (SCI42 M01) becomes the premise of a K2P arm *only if* it shows a genotype difference of about 0.2 unit or more at the recording depth; below 0.1 unit the pH route is dropped by the size check, and the measurement keeps its GluN2B role.
5. **A tool-by-pH interaction is the discriminating pharmacology** (KP4): a TASK-1 probe (ML365) and a family-level comparator (PK-THPP) at two pHo with the genotypes side by side. No tool in the literature read was tested at more than one pH, and no tool has a measured TREK-1 selectivity.

**What remains to be shown in the chain:** (a) that interstitial pHo differs between genotypes in the recorded slice; (b) that lactate is raised in the Wwox slice at all; (c) that a pH-sensitive current per pF differs by genotype; (d) that any of it is more than a consequence of bursting. None of these is observed in WWOX. Steps 1-2 of the chain are not observed in a neural WWOX preparation, step 3 is unmeasured, steps 5-6 are documented in other preparations.

## The chain after the reading (`output/premises.tsv`)

| Step | State |
|---|---|
| 1 metabolic state, 2 lactate and pyruvate | observed elsewhere / not observed in the preparation (unchanged from SCI44) |
| 3 lactate to pHo | **demoted**: hypothesised, not supported at physiological loads, not excluded (bounded absence at abstract level) |
| 3b lactate to pHi | documented elsewhere (10 mM lactate: pHi -0.05 to -0.07); clamped in the published whole-cell recordings |
| 4 conditions | documented in the Wwox Methods: 25 mM HCO3-, 35 C, 10 mM HEPES and 2 mM ATP in the pipette; bath pH value not stated |
| 5 channels | documented elsewhere, recombinant (pH50 table below); native juvenile cortex: one layer V datum |
| 6 resistance, rest, network | constrained by the size check; quantitatively marginal |
| 7 compound | documented elsewhere; none tested in the preparation |

## pH sensitivity and contexts (verified; `output/ph_sensitivity.tsv`, `verify/recompute_ph.tsv`)

| Channel | Extracellular pH | Intracellular pH | Contexts |
|---|---|---|---|
| TASK-1 | closed by acid; pH50 7.30 (murine oocyte, 22.5 C, 2 mM K+, free Imin), 7.40 (human oocyte, 20-22 C, +40 mV), 6.57-6.66 (murine, 70 mM K+, slope 1 imposed). Remaining fraction relative to alkaline: 0.50-0.87 at 7.4, 0.39-0.81 at 7.2, 0.28-0.73 at 7.0 | not reached | the 0.7 unit gap between labs is not resolved (K+, species, normalisation) |
| TASK-3 | closed by acid; pH50 6.29 (murine) and 6.47 (human); nearly flat from 7.4 to 7.0 | not reached | 6.8-7.0 in two abstracts (mammalian/native) |
| TREK-1 | closed by acid; pH50 7.51 (poor fit, slope about 0.7); native human TM cells (cell line and primary): pHo 7.4 to 6.0 lowers outward current to 0.67 | opened by acid: EC50 5.9, Hill 2.3 (giant patches); about 0.3 percent open at pHi 7.0 | counter-statement: acid enhances a TREK-like current in mouse hippocampal astrocytes after Kir4.1 block (abstract) |

Native: adult rat brainstem (34-36 C, HCO3- bath, HEPES pipette): pHo 7.4 to 6.8 removes about 42 pA, 14 of 18 cells; juvenile (P9-15) mouse **layer V** pyramidal neurons: pH-sensitive current at -60 mV 51.7 vs 31.1 pA in the TASK-1/3 double knock-out, holding current 26 percent smaller, RMP -75.1 vs -71.1 mV (room temperature, 1.4 unit step); adult S1 layers 2-4, TREK1-/-: Rin 121.4 to 257.2 MOhm (persistent-firing class). **No layer II/III juvenile pH response was found** (bounded absence, V05, V06, V09, V12).

## Tools (`output/tools_roles.tsv`, `output/tools.tsv`)

ML365 probe (TASK-1 over TASK-3, 62-100 fold, CHO, pH 7.4 only; TREK-1 and heteromer untested); PK-THPP and A1899 family-level comparators (about 10 fold); spadin excluded as a TREK-1 tool until replicated; Zn2+ a conditional TASK-3 discriminator (abstract). The unchanged catalogue path holds **none of the four by target** (the same blind spot as azetukalner); it holds pointers to qualify: ONO-TR-772 (TREK-1 inhibitor, pIC50 7.82), Cpd8l, KU124, AVE1231, and AMPK activators with a TASK-3 inhibitor row of doubtful potency (`search/`). Identifiers are PubChem name matches, not structure-checked.

## Hypotheses, experiment, outcomes

`output/hypotheses.tsv` KP1-KP5; `output/experiment_ladder.tsv` (pHo record at the recording depth; pHo step per cell in whole-cell and perforated patch; tool arms at two pHo; the SCI43 steps 0-1 and 5 reused); `output/outcome_matrix.tsv` O1-O8 (favoured interpretation, alternative, decision changed, what cannot be concluded). The design is research design, not a commission.

## Priors (S1, scored by the verifier from its own reading; `output/answers.md`)

P1 partly held (the TASK-1/TASK-3 gap holds, the ranges failed); P2 held for pHo, pHi undecidable; P3 partly (the extracellular half failed: acid closes TREK-1); P4 held literally for layer II/III, failed in spirit (Yao 2017, layer V); P5 undecidable for TREK-1 (untested), ML365 reaches 100 fold on TASK-3; P6 partly (activity transients small; depth gradient and ischaemia not); P7 partly failed (lactate-to-pHi data exist in perfused slices).

## Verification

Producer: 14 sources newly read at partial full text, 21 abstract-level; the verifier checked 63 rows: 51 correct, 12 defective; 42 of 42 evidence quotes verbatim; 13 of 13 receipt fingerprints recompute. Substantive findings (`output/CORRECTIONS_V5.tsv`): the juvenile cortical absence (Yao 2017, rechecked by the Orchestrator in the text), the lactate-to-pHo absence (Walz and Harold 1990; Roberts 1998, abstract level), Rin and RMP present in Labbaf (error class extended), the slice depth gradient omitted, the recompute model (modified Hill with free Imin), TREK-1 counter-statements. **Route flags for the integrator:** the producer tried two more routes for Duprat 1997 after a PMC bot check (nothing used); the verifier read 15282272 through the Europe PMC abstract record after an NCBI throttle (a second API for the same article; the row it supports stays abstract level). Receipts: 14 producer (`-88`) and 13 verifier (`-87`) staged in `research/receipt_staging/sci45` and `sci45v`, valid under `staged_receipt_check.py --check-doi`, none recorded.

## Size check (software; `SIZE_CHECK_PREREGISTRATION.md`, `size_check.py`, `size_check_pools.py`)

Preregistered grid (run 1) and a dated addendum with the verified pH50 set and slopes 0.7, 1, 2 (run 2). Predictions: S1 (TASK-3 L below 0.01) **failed** (0.044 at share 0.5, 0.116 with pH50 6.9); S2, S3 and S4 held. With pools from native knock-outs (addendum, INFERENZA): TASK-1/3 pool 0.26, maximum loss 0.18 at the highest pH50, slope 2 and 0.3 unit; TREK-1 pool 0.53, loss 0.29-0.37 only at slope 2 (0.2 unit from baseline 7.2; 0.3 unit from 7.2 or 7.4), at most 0.21 at slope 1 and 0.3 unit. A threshold, not an estimate: it says what a pH change must be, not what it is.

## What no further literature can resolve

pHo and pHi of the recorded slice by genotype; pH-sensitive current per pF in layer II/III; lactate in the Wwox slice; the Hill slope of TREK-1 at 35 C; the tools' own pH dependence. These need the measurements of the ladder.

## Novelty (three levels)

Known relation, unused by the module: TREK-1 knock-out doubles Rin in adult S1 neurons; TASK-1/3 knock-out removes a quarter of the holding current in juvenile layer V; acid closes TREK-1. New combination for LEGEND: the size check against the Wwox pair, the occlusion/tool-by-pH design, the pH measurement as a shared premise with a stopping threshold. Acquired now: verified pH50 ranges, native pools, tool selectivity table, catalogue blind spot. Novelty against the literature: not asserted (perimeter: PubMed tool and Europe PMC REST, 2026-11-11, `output/queries.tsv`, `verify/queries_verifier.tsv`).

## Files

`S0_S1_before_search.md`; `BRIEF_P.md`, `VERIFIER_BRIEF_V5.md`; `output/` (producer tables with annotated corrections, `premises.tsv`, `hypotheses.tsv`, `tools_roles.tsv`, `experiment_ladder.tsv`, `outcome_matrix.tsv`, `CORRECTIONS_V5.tsv`, `apply_v5_corrections.py`, `receipts/`); `verify/` (audit, verdicts, recompute, receipts); `search/` (unchanged action-search output for KCNK2/3/9); `SIZE_CHECK_PREREGISTRATION.md`, `size_check*.py/tsv`; `build_tables.py`; `consumer_delta.md`; `COST_NOTE.md`.
