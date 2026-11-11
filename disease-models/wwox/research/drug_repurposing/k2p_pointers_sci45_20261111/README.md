# SCI45 queue Q1 — primary sources of the K2P tool pointers and the TREK-1 pH slope (2026-11-11)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference; no claim on WWOX; no compound is promoted. Labels DATO / INFERENZA / IPOTESI. One producer (sonnet/medium, 87 turns) and one narrow blind verifier V6 (sonnet/high, 73 turns); no substantive error found, minor corrections annotated (`output/apply_v6_corrections.py`). Paths relative to this folder.

## Answer first

1. **The one potent TREK-1 inhibitor pointer, ONO-TR-772 (40365404), is a TREK-1/TREK-2 dual inhibitor with an unreconciled potency, no pH series and no neuronal data.** Values in the source: 15 nM (abstract, human manual patch clamp), 67 nM (mouse), 0.26 uM (Tl+ flux, CHO), 0.15 uM (QPatch). The paper's own ">67-fold" equals 10 uM / 0.15 uM, so a reader should carry **0.15-0.26 uM**; the catalogue's 15 nM (pIC50 7.82) labelled Rat is the human headline and the species label is unsupported. Selectivity by concentration-response covers TREK-2 (equipotent) and TASK-3, TRESK, TWIK-2 (above 10 uM); TASK-1 (17 percent) and TASK-2 are single 10 uM points, TRAAK is activated (41 percent); Kir2.2 52, KCNQ1/E1 47, hERG 38 percent at 10 uM; binding off-targets (A3, L-type Ca, Na site 2) have Ki 0.48-2.6 uM. The only in vivo datum is a mouse novel-object-recognition effect; the estimated unbound brain level (5.3 nM) is below the mouse patch-clamp IC50. **Role: probe-pointer, conditional; not usable as a TREK-1-selective tool.**
2. **TASK-1 pointers are thin.** AVE1231: human TASK-1 IC50 0.2 uM (supplement, oocytes, +40 mV, 20-22 C, pH 7.4 only, no other channel measured); its main-text points (26 percent at 245 nM, 81 percent at 10 uM) imply an IC50 near 1.2 uM (INFERENZA, unexplained by the paper). KU124: IC50 1.38 +/- 0.65 uM, Tl+ assay, no plateau, no selectivity, species not stated. Cpd8l: abstract only (IC50 0.81 uM, OGD/R cortical neuron protection falls when TREK-1 is silenced; full text 403, not retried). ML365 (package P1) remains the best-documented TASK-1 over TASK-3 probe.
3. **A TREK-1 activator pointer, ONO-2920632**, is TREK-2-preferring (human Tl+ EC50 TREK-2 0.30, TREK-1 2.8 uM); the pH of the assays is not stated and no acid-pHo test exists. It cannot yet serve as a restorability probe for an acid-closed channel.
4. **No tool of this family has been tested at more than one pH** in the sources read (now also ONO-TR-772, ONO-2920632, AVE1231, KU124): the tool-by-pH interaction of hypothesis KP4 remains unmeasured for every tool.
5. **The TREK-1 Hill slope is not stated in any reachable full text** and no source reaches 30-37 C. The new datum is the **residual current**: Bagriantsev 2011 (21765396, Supp Table S1; found by the verifier) reports pK 7.51 and Imin 0.25. It changes the P1 size check (`../ph_k2p_sci45_20261111/size_check_imin.tsv`): with Imin 0.25 no sourced parameter set reaches the 28 percent loss through pHo-closed TREK-1.

## What was examined

Producer, partial full text (5): 40365404 (main, SI text and Tables S2, S3), 39981749 (main, SI text, erratum), 40635742, 31001961 (open-access PDF and supplement), 41104520 (a follow-up found by name; method and ancillary pharmacology). Abstract only (4): 40040241 (403), 19667202, 18474599 (403), 27129242. Verifier: the same decisive rows at partial full text, plus 21765396. Unreachable, not retried by another route: ACS (Cpd8l), jbc.org (Cohen 2008), PMC PDF and NCBI XML (Sandoz 2009, Lengyel 2016), Wiley (2026 BJP TREK-1/TASK-4 paper). Verifier route deviations: none.

## Catalogue label check (D12, verified)

ONO-TR-772 15 nM labelled Rat (paper: human; QPatch 0.15 uM); KU124 labelled Human (the paper does not state the species); Cpd8l label cannot be checked. These labels live in the activity-path output; the typed role of a pointer should not carry them.

## Verification

Evidence rows: 13 checked, 9 correct, 4 minor defects (species wording in E02, E03; E08 a composite of two cells; E12 not verbatim). Decisive rows: D02-D05, D08, D09, D11, D12 SUPPORTED; D10 PARTLY (basal flux is the producer's reading; abstract >91-fold vs Results >150-fold); D01, D06, D07 spot-checked. Receipts: 5 producer (`-86`), 7 verifier (`-85`), staged in `research/receipt_staging/sci45q` and `sci45qv`, valid under `staged_receipt_check.py --check-doi`, none recorded. Producer under-claimed figures as `captions_only` in four receipts although its notes record images viewed (harmless).

## Limits

A single manual-patch-clamp value 17-fold below the Tl+ value cannot be decided between unit slip and assay difference from the SI. Cpd8l is abstract level. No tool here has neuronal electrophysiology on rest, Rin or pH.

## Files

`BRIEF_Q1.md`, `VERIFIER_BRIEF_V6.md`; `output/` (pointers, trek1_ph_slope, decisive, evidence, queries, figure notes, receipts, `apply_v6_corrections.py`); `verify/`; `consumer_delta.md`; `COST_NOTE.md`.
