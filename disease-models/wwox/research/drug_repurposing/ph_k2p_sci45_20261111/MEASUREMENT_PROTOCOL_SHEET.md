# SCI45 action 3 — minimal measurement as a research-design sheet (2026-11-11)

Non-canonical. A design to discuss with a laboratory, **not a commission, not a protocol approved for execution, not a prescription**; no animal or human treatment is proposed; slices only. Labels DATO / INFERENZA / IPOTESI. It reuses the preparation of the Wwox paper (neuron-specific Syn-Cre deletion, acute slices, layer II/III pyramidal neurons, P13-P17, 35 C; internal 135 K-gluconate, 10 HEPES pH 7.2-7.3, 0.5 EGTA, 2 Na2ATP; ACSF 25 mM HCO3-, 10 glucose, 3.5 K+; audit A1.15) and the K-branch ladder of SCI43 (steps 0, 1, 5), so that the new measurements add three arms to cells that are recorded anyway.

## Purpose and the decision it changes
Whether interstitial pHo differs between genotypes at the recording depth (step 1), and whether a pH-sensitive current per pF differs (step 2), decides: the K2P-by-pH arm (stop below 0.1 unit; a partial contributor at 0.2 unit or more: size checks of SCI45); the pH state for the GluN2B comparison (SCI42 M01); and the sign question of the next package (K2P versus NMDAR and ASIC). Conclusion rules are in `output/outcome_matrix.tsv` O1-O8.

## What is fixed before the first slice (per day, per animal)
| Item | Record | Why |
|---|---|---|
| Animal | genotype, age (day), litter, sex; the animal is the statistical unit | slices and cells are nested |
| ACSF | batch, HCO3- (25 mM), gas mix (O2/CO2 fractions), **bath pH measured at the chamber inlet and outlet**, temperature at the recording site, flow rate | the Methods give neither bath pH nor gas fractions |
| Slice | thickness, time since cutting, **depth of each recorded cell below the surface** | 0.24 unit depth gradient, steeper at 35-37 C |
| pHo at depth | ion-selective microelectrode (or ratiometric extracellular dye) at the cell depth and at the surface, before and after the recording, same slice | step 1 |
| Pipette | the internal of the Wwox paper unchanged for the whole-cell arm; for the perforated-patch arm an ATP-free pore-forming internal; pHi-buffer stated | pHi is clamped by 10 mM HEPES in whole-cell |
| Blinding | scoring blind to genotype and to condition; condition order randomised within animal | |

## Arms (same cells where possible)
1. **Capacitance and selection rule** (SCI43 step 0), synaptic blockers and TTX for the intrinsic arms (SCI43 step 1). Not redone here.
2. **pHo step per cell**: baseline bath pH, then a step to a lower pH (about 0.3 unit; a smaller second step for the dose-response shape) and back, plus one step in the alkaline direction; hold and Rin/rest at a stated potential; current at -60 and -75 mV; pHo at depth recorded during the step. Whole-cell (pHi clamped) and, in sibling cells, perforated patch.
3. **Tool arms at two pHo**, difference current per pF: a TASK-1 probe (ML365) at a concentration chosen inside its measured TASK-1/TASK-3 window (0.016 vs 0.99 uM, QPatch, pH 7.4), a family-level comparator (PK-THPP) and the Ba2+ concentration pair of SCI43 step 2b; each at both pHo, each with washout and a time-matched vehicle. No TREK-1-selective tool is qualified; ONO-TR-772 enters only after a primary read of its pH behaviour (not measured in the paper).
4. **Network readout in the same slices** (separate sweep, synapses intact): burst incidence and, if the preparation allows, the NMDAR-dependent component at each pHo, because an acid shift may act on NMDAR as well as on K2P (sign question). Not used as proof of cause.

## Analysis rules fixed in advance
* Primary quantities: pHo difference between genotypes at the recording depth; pH-sensitive current per pF by genotype; Rin genotype difference at each pHo (occlusion); tool effect per pF by genotype and pHo.
* Thresholds: pHo difference below 0.1 unit stops the pH route; a pH-sensitive current per pF equal in the genotypes with a difference in pHo is outcome O4; and so on as in the outcome matrix. A tool whose effect at pH 7.1 differs from that at 7.4 in wild type only is not read as target engagement until a second scaffold repeats it (O6).
* Mixed model with animal as the random effect; the numbers of animals needed are a feasibility question for the laboratory (P13-P17 window), not a logical one.

## What the measurement cannot show
That a pH difference is metabolic; that lactate is raised; that closing or opening a K2P channel helps any outcome; that a tool's target is altered in Wwox; anything about a systemic or clinical intervention.

## Pre-existing items it does not repeat
PDK, KATP share, chloride, Table 1 arithmetic, the Ro 25-6981 work, the 15 RNA predictions.
