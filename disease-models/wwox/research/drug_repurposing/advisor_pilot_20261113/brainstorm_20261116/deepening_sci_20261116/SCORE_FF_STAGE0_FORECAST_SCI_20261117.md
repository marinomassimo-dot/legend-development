# Score of my independent forecast of the family-first cue, stage 0, on T7 (SCI, 2026-11-17; non-canonical; scored literally with HE's definitions; not blind; IT scores independently)

Forecast: `PREDICTIONS_FF_STAGE0_SCI_INDEPENDENT.md`, sha256 afdab1474c0154f42ffbcdf5c0291d8b6170a7bc40b0b563ff5c2990fe78405d, written and hashed 08:52:17Z before the run; I knew the T7 result, the atom and the C2M outcome and said so in it. Outputs read afterwards: `OUT_FF1.txt` (sha256 e2d92a2b...) and `OUT_FF2.txt` (f726d23c...) in HE's scratch folder `set3/ff/`; scoring definitions from `FF_STAGE0_FOR_FORECASTER.md` (b114e164...). HE's own result file was not read.
## What the two outputs contain (my reading)
* **Zinc does not appear anywhere in either output** (0 hits for zinc or Zn in FF1, 189 lines, and FF2, 117 lines): not in the MODULATORS table, not in STEP C, not in the 15 hypotheses.
* Families named. FF1: other receptor GCs, soluble guanylyl cyclase, adenylyl cyclases (transmembrane AC1-9 and soluble AC10), plus 'a further related family' the protein kinase/pseudokinase fold; PDEs, MRP4, PKG2, CFTR and NHE3 as pathway components. FF2: adenylyl cyclases, soluble guanylyl cyclase, pseudokinase and kinase-fold receptors; pathway components PDEs, MRP4/5, PKG.
* Ions listed as lowering: Ca2+ (FF1: free Ca2+ on sGC, Ca2+ on AC5/AC6, Ca2+-bound GCAPs on GC-E/F; FF2: Ca2+ on AC5/AC6, GCAP at high Ca2+). No other ion.
* MODULATORS table: about 75 pipe rows in FF1 and 59 in FF2 (my count, headers excluded). STEP C states the defect as a gain of function in both (FF2 marks it an IPOTESI from the question).
## Scored statements
| id | statement | my P | observed | ln score | coin |
|---|---|---|---|---|---|
| a-1 | LOOSE (zinc in the table as lowering) in at least one of FF1, FF2 | 0.55 | **NO** | -0.799 | -0.693 |
| a-2 | LOOSE in both | 0.25 | NO | -0.288 | -0.693 |
| b-1 | STRICT in at least one | 0.35 | NO | -0.431 | -0.693 |
| b-2 | STRICT in both | 0.10 | NO | -0.105 | -0.693 |
| c-1 | zinc in the 15 hypotheses of at least one run | 0.30 | NO | -0.357 | -0.693 |
| c-2 | zinc in the 15 as an inhibitory lever | 0.20 | NO | -0.223 | -0.693 |
| d-1 | an ion other than Mg2+, Mn2+ and zinc listed as lowering, in at least one run | 0.90 | YES (Ca2+) | -0.105 | -0.693 |
| e-1a | soluble guanylyl cyclase named as a related family | 0.95 | YES (both) | -0.051 | -0.693 |
| e-1b | adenylyl cyclases named | 0.90 | YES (both) | -0.105 | -0.693 |
| e-1c | a kinase or pseudokinase family named | 0.50 | YES (both) | -0.693 | -0.693 |
| e-1d | phosphodiesterases named as a related family | 0.30 | NO as a related family (named as pathway components in both) | -0.357 | -0.693 |
| e-1e | number of related families per run median 3 (2 to 3) | - | FF1 3 plus the kinase fold named as 'a further family' (4), FF2 3 | FF1 outside, FF2 inside | - |
| e-2 | modulators listed per run median 40 (25 to 70) | - | about 75 and 59 | FF1 above range, FF2 inside; I underestimated | - |
| f-1 | STEP C states a gain of function in both | 0.98 | YES | -0.020 | -0.693 |
| f-2 | a modulator mapped with a direction that cannot serve a gain of function | 0.10 | not scored (needs a line-by-line read of the STEP C mappings, not done) | - | - |
Twelve scored binary statements, not independent (a-1 to c-2 are six views of one event, zinc absent): **-3.53 (mine) against -8.32 (coin); for the six zinc statements alone -2.20 against -4.16**. The zinc event did not occur and I had given it 0.55 (LOOSE, at least one) and 0.35 (STRICT, at least one): the misses are small in log terms because I had leaned to 'not in both', but the direction of my lean was wrong (the family cue did not recover zinc).
## What this says
1. **The family-first cue widened the framing a lot and still did not surface zinc.** Both runs named the adenylyl cyclases, the soluble guanylyl cyclase and the pseudokinase fold, and listed 59 to 75 modulator rows; the ion modulators they listed were Ca2+ and the GCAP-Ca2+ system. Zinc is a classical adenylyl-cyclase inhibitor and a known antidiarrhoeal ion; it was not retrieved. With C2M (0 of 2 on an enumeration without zinc) and T7 (0 of 40 final statements) this is a third framing, a class-to-member step, a family cue and the corpus-bound steps, in which a tool-free model does not volunteer zinc, while HE's direct probe showed that the model knows it when asked directly.
2. **The pattern across the three trials:** zinc is kept when it is already in the input (C2M input B), is reached by none of the framings tried when it is not (C2M A, FF, T7 steps), and is known when asked directly: **retrieval of a niche inhibitory ion depends on a cue that names the ion class and a direction, not on widening the family or asking for members.** A candidate for a next stage would be a cue of that kind (for each divalent cation, say whether it raises or lowers the activity of any cyclase), at the cost of being an answer-shaped hint; whether that is a legitimate generator step or tuning on the answer is a decision for HE and ADV, not mine.
3. My own calibration: I again overestimated retrieval of what the model knows (C2M 0.80 strict; FF 0.55 loose), now twice in the same direction; the correction for any later forecast of this kind is to put the retrieval of a niche member under a broad framing below 0.3.
Limits: two runs; T7 is tuned-on and the answer is in my memory; scoring is mine and literal, IT scores independently; f-2 not scored.
