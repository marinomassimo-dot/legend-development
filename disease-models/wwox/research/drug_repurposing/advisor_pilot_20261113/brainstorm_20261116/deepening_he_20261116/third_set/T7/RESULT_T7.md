# T7 (GC-C zinc; TUNED-ON): run record and result — RETRODICTION BY ABSENCE FROM THE CORPUS, NOT BY DATE (HE; 2026-11-17; non-canonical; not medical advice)

**TUNED-ON.** Written for: ADV (and SCI for its independent forecast). Frozen: `../FREEZE_THIRD_SET_PART_B.md` (sha256 8920ac510a50d9e918f0ace03128bf310ce22faebecce42e9a788a217c7afb47) and `../AMENDMENT_B1.md`; Part A v2 sha256 6473ea02…; briefs `../briefs3/SHA256_BRIEFS.txt`. Nothing of T9 is read into this record.
## Runs (REDUCED-SEQUENTIAL: v3 and v4, two replicates each, no baseline; sonnet, `legend-deepdive`, one at a time)
| step | tokens | tool calls | path audit from the transcript |
|---|---|---|---|
| v3 stage 1 A / B | 26,246 / 22,674 | none | zero file-tool calls |
| v3 stage 2 A / B | 104,953 / 103,921 | 12 Read, 1 Glob, 22 Grep / 10 Read, 1 Glob, 27 Grep | only the cut and the one S1 file |
| v4 stage 1 A / B | 28,279 / 30,399 | none | zero file-tool calls |
| v4 stage 2 A / B | 124,535 / 116,618 | 8 Read, 1 Glob, 25 Grep / 12 Read, 1 Glob, 29 Grep | only the cut and the one S1 file |
| blind reader (Z01-Z40, seed 20261201; key hashed first) | 30,655 | 2 | read only its input |
Total **588,280 tokens** (estimate about 600k); no usage-limit message. The earlier selection probe and audit for this target (18,440 and 18,315) are counted in M070. Reports verbatim in this folder; sha256 prefixes: `V3_S1_A` 168b1873, `V3_S2_A` b59df3b1, `V3_S1_B` ba5fb6f0, `V3_S2_B` 585bbad0, `V4_S1_A` 6dee1133, `V4_S2_A` b0efad0e, `V4_S1_B` ed28bbeb, `V4_S2_B` 985cbf1f, reader answer `READER.txt` fce7edd6; blind input 37bfa8f7…, key `blind_key.json` 7aaa70e4f554d3d877132f12f08d3cb97da8c5cd4d56d2c8607f084d66654f28 (hashed before the reader ran); my first pass `MY_FIRST_PASS_T7.md` b5dc76ac… (written before the reader's answer and without arm labels).
Builder notes: the blind input was built with the set-2 builder plus two extra tail patterns ('CAVEATS', 'Operational note'); eleven stage-1 tokens in the final-ten texts were replaced by 'a rival'. Two arms (v3, v4) x two runs x ten = 40 hypotheses.
## Result (blind reader, unblinded through the key)
| condition | QS strict (zinc, inhibition, cGMP and barrier) | QL loose (any metal or cofactor lever) | QC class (reported only; void for the decision) |
|---|---|---|---|
| v3 A / B | 0 / 0 | 0 / 0 | 0 / 0 |
| v4 A / B | 0 / 0 | 0 / 0 | 0 / 0 |
Totals 0 / 0 / 0 of 40. My first pass (keyword census 0 of 40, strict 0, loose 0, class 0) agrees. The reader rejected two ATP-pocket hypotheses as not a metal ion.
**Reading: a ZINC MISS under v4 with the axis named in the template, the outcome ADV called the stronger finding.** v4 did not recover the case it was written for. Predictions committed first: v4 reaches the strict atom in at least one replicate 30 percent (did not occur); v3 10 percent (did not occur).
## QY (A2): where the metal-ion class and zinc were lost (scored by me from the printed files; not blind)
| point | v4 run A | v4 run B | v3 runs |
|---|---|---|---|
| ENUMERATION block: metal-ion class | yes (axis a: 'Mg2+/Mn2+ metal site and metal identity') | yes (axis a: 'Divalent metal: Mg2+ versus Mn2+') | no enumeration |
| ENUMERATION block: zinc | no | **yes (axis d, 'Vitamin A, zinc', as a supply item, no mechanism)** | – |
| the 15 of stage 1: a metal-ion hypothesis | yes (H2, Mn2+/Mg2+ composition via transporter dosage) | yes (H9, metal and redox gating, Mg2+ import reduction) | none |
| the 15 of stage 1: zinc | no | no | no |
| final ten of stage 2: a metal-ion hypothesis | no (S1-2 'not kept') | no (S1-9 'not kept') | none |
Reading (QY): v4's enumeration DID surface the metal-ion class in both runs and zinc once (as one item of a supply list); stage 1 carried a metal-ion hypothesis in both runs, but never zinc: the two metal levers were Mn2+/Mg2+ composition as a DRIVER of the cyclase with the lever LOWERING the metal (transporter dosage reduction, Mg2+ import reduction), the right polarity for a gain-of-function defect; what neither named was a metal that INHIBITS the cyclase (zinc), that is a different metal acting as an inhibitor rather than a driver; stage 2 dropped the metal-ion hypothesis in both runs ('OUTSIDE, not kept', the corpus has 0 hits for the metal terms in this context). So the failure is on the selection side twice (enumeration-to-fifteen: zinc dropped; fifteen-to-ten: the metal lever dropped), not an enumeration failure for the class: 'the corpus step demotes' for the class, and 'stage 1 composition' for zinc. The axis was named in the template, so by A1 class-level credit is void; this QY is the diagnosis, not a credit.
## QX (A2/A3): axes covered, with the fixed keyword lists of `axis_coverage.py` (noisy: its catalytic-axis words 'nucleotide' and 'hydrolysis' match PDE and cGMP text in this target)
Final ten, axes named per run (of 7): v3 5 and 4 (mean 4.5); v4 6 and 6 (mean 6.0). The 15 of stage 1: v3 6 and 6; v4 6 and 7; the ENUMERATION blocks of both v4 runs name all 7. So v4 does widen the axis spread of the final ten by about 1.5 axes (as predicted, 85 percent), and the catalytic axis count is inflated by cGMP wording; the one metal-specific measure is the QS/QL/QC above, 0 of 40.
## What it says, and what not
On a TUNED-ON ion target the enumeration step surfaces the class and the corpus step discards it; the strict lever (zinc, inhibition of the cyclase) is reached by no condition. This is one target in a domain the corpus is silent on (so stage 2 classified every hypothesis outside and 'not stated'), abstract-only atoms, two replicates; the miss is informative about stage 2 (the 'keep at least three outside' rule did not protect a metal lever that stage 1 listed) and uninformative about whether v4 beats v3 (no atom reached by either). The frozen rule needs BOTH absent-axis targets; T9 follows, and the harm check on T5 runs only if v4 reaches a strict atom on T9.
Limits: not blind for QX and QY (mine, mechanical); the QX keyword lists are crude; the question audit passed at T7 but 'direct inhibition' is entailed by the wording; the model knows zinc as an antidiarrheal and a general cyclase inhibitor (probe), so the miss is not for lack of the idea in memory.

Dated correction 2026-11-17 (HE): my message to ADV after T7 described both stage-1 metal hypotheses as 'more metal helps the cyclase' framings; reading the texts again, both lower the driving metal (A: Slc39a8/Slc30a10 dosage or TRPM6/7 haploinsufficiency; B: reduce Mg2+ import), so the polarity of those two levers serves the gain-of-function defect. The gap is the identity of the metal (an inhibitory metal), not the direction of the lever.
