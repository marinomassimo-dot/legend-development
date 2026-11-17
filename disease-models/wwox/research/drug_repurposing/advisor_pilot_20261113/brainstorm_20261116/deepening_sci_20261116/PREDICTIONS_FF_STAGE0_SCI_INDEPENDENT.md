# Independent forecast of the family-first cue, stage 0, on T7 (SCI, 2026-11-17, host clock before 09:25Z; written and hashed BEFORE the run; probabilities mine, not evidence)

**What I know when writing:** the T7 result (zinc as an inhibitory ion named in 0 of 40 final statements; once only as a supply item in a v4 enumeration block), the atom (zinc as an inhibitor of the cyclase), and **the C2M outcome (my 0.80 for zinc listed as lowering in at least one of two class-to-member runs on an enumeration without zinc was a miss: zinc was in neither output, Ca2+ and chelators were the only lowering ions; where zinc was already in the input it was kept)**. I have read `FF_STAGE0_FOR_FORECASTER.md` (sha256 b114e16438ed828d5c48251ad5392aae96092e621dbf33eeb7fad168dff5575c): the template, the composed prompt, the scoring definitions. I have seen no output and no predictions of HE.
**How the C2M lesson enters:** knowing a fact is not the same as retrieving it under a framing. The FF prompt asks, for the defective family and for EACH related family, for every substance, ion, cofactor or condition known to modulate ANY member of the family, with its direction: this widens the framing from 'the metal site of this cyclase' to 'the cyclase families', where zinc is documented as an inhibitor (adenylyl cyclases and, in older work, guanylyl cyclases) and where the model will list several ions. I therefore expect more reach than in C2M but not certainty, and I give the strict reading less than the loose one because strict also needs zinc to survive into the mapping or the hypotheses.

## Predictions (STRICT and LOOSE as defined by HE)
| id | statement | P |
|---|---|---|
| a-1 | LOOSE in at least one of FF1, FF2 (zinc in the MODULATORS table with direction lowers, any family) | **0.55** |
| a-2 | LOOSE in both | 0.25 |
| b-1 | STRICT in at least one of FF1, FF2 (LOOSE and zinc carried into the STEP C mapping or the 15 hypotheses as a lever lowering the defective cyclase) | **0.35** |
| b-2 | STRICT in both | 0.10 |
| c-1 | zinc appears in the 15 hypotheses of at least one run (any role, including a barrier-supporting role) | **0.30** |
| c-2 | zinc appears in the 15 hypotheses of at least one run as a lowering (inhibitory) lever | 0.20 |
| d-1 | an ion other than Mg2+, Mn2+ and zinc listed as lowering in the MODULATORS table of at least one run (expected: Ca2+, Cu2+, Cd2+ or Co2+) | 0.90 |
| e-1 | related families named: soluble guanylyl cyclase in at least one run 0.95; adenylyl cyclases in at least one run 0.90; a protein-kinase or pseudokinase family 0.50; phosphodiesterases as a related family 0.30; number of related families named per run median 3 (2 to 3, as asked) | as stated |
| e-2 | number of modulators listed in the MODULATORS table per run: median 40 (25 to 70) | as stated |
| f-1 | STEP C states the defect as a gain of function in both runs | 0.98 |
| f-2 | any modulator mapped with a direction that cannot serve a gain of function (an entry applied in the raising direction as a corrective) | 0.10 |
## What would change my reading
Zinc listed as lowering in the table and carried through to the hypotheses in at least one run would say that the family cue recovers the member the class framing lost: the C2M miss was a framing limit and not a memory limit. Zinc listed in the table but absent from STEP C and the hypotheses would say the cue reaches it and the mapping demotes it (a selection-side failure again, as in set 3). Zinc absent from the table in both runs would say that the model's tool-free reach for ion inhibitors is limited even when asked for every ion on every family member. Scored literally by HE and, independently, by IT; T7 is tuned-on, two runs, no claim of improvement.
