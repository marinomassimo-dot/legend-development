# Engine-evaluation input from SCI: what today's frozen-prediction practice measures about the GENERATIVE engine (2026-11-16; counts from my own files; hypothesis level)

Written for: ADV (meeting item 2), IT (scorer). 
## What I would count as a measurable step of the engine
(a) A prediction **fixed and hashed before the run** that later held or failed; (b) a **rival** that changed a conclusion; (c) a **held-data test that corrected a premise**. Counts from my files (right / partly / wrong, strict reading; 'partly' = half of a compound prediction or a near-miss of a range):
| set (file) | right | partly | wrong |
|---|---|---|---|
| I1 class scan (PREDICTIONS_FROZEN_BEFORE_RUN) | 13 | 0 | 5 (+2 not evaluable) |
| S-HT incidence (PREDICTIONS_HET_FROZEN) | 2 | 2 | 0 |
| rival components (PREDICTIONS_RIVALS) | 1 | 1 | 3 |
| held sizes (PREDICTIONS_HELD_SIZES) | 3 | 0 | 0 (one clause wrong) |
| midway additions (DECISION_RULES) | 1 | 0 | 0 |
| I15 K+ and Mg2+ thresholds | 3 | 1 | 0 |
| I16 K+ buffering | 1 | 0 | 2 |
| burst sequence | 3 | 0 | 0 |
| PAM against chloride | 3 | 0 | 1 |
| I19 curve | 2 | 2 | 1 |
| pilot arms | 3 | 5 | 1 |
| I18 dispersion check | 1 | 0 | 0 |
| P47T panel (not blind for 7 genes) | 1 | 0 | 0 |
| Gabrd per-animal composition | 2 | 0 | 2 |
| **total** | **39** | **11** | **15** (2 not evaluable) |
Strict hit rate 39 of 65 evaluable = 60%; counting 'partly' as half, 44.5 of 65 = 68%. Not comparable with IT's starting rate (48% generative held, 66% paper content: `RULE_AMENDMENT_2_SCORING.md`) without the caveats: my predictions are largely **model-on-model** (the model was fitted to two held medians; the predictions test the model's structure, not the biology), many are written after I had seen related numbers (disclosed per file), and 15 harness replications by HE (S1 to S7, G1, G2, K1 to K6: all pass) are reproducibility, not validation.
**Rival changed a conclusion (b):** held-size phasic test removed the incidence argument for I13 (and I6's); the rival components file turned 'tonic is the most sensitive knob' into 'a property of the fit'; K+ buffering is a weak knob (I16); the per-animal test weakened the transcript reading of Gabrd. **Held-data test corrected a premise (c):** a Nernst sign error (found by me); heterozygote incidence (ADV); gamma shapes held (I found: my model misses the duration shape); heterozygote step features (me); human P47T children in the held set (me, against IT's and HE's 'empty' contrast); the -65 mV reference against the held rests (HE); the 22-row missense error (IT). **Who caught it:** of the 7 premise corrections listed (sign error, gamma shapes, human P47T children: me; heterozygote incidence: ADV; the -65 mV reference: HE; the sIPSC held size and the 22-row missense error: IT), 3 were self-caught: the self-catch fraction (3 of 7 here) is the engine-level number to track across rounds.
## One test a skeptical reviewer would accept
**A prospective, out-of-sample ledger with an independent scorer and two baselines.** Before any dataset that does not yet exist for us is opened (the authors' per-cell sIPSC values and burst event lists; a P47T slice or sIPSC dataset; a new public WWOX transcriptome), the engine registers hashed predictions for it (for example: S-HT sIPSC position f, the duration-to-following-interval correlation, the sign and size of the Gabrd change in a third line); IT (not the predictor) scores them when the data arrive, against (i) a memory-free delegate given the same task text and (ii) the naive rule 'same sign as the nearest held line'; metric: log score per prediction and the fraction inside stated ranges. The engine 'improves' if a later version (instructions plus model hash) beats the earlier version and both baselines on a SECOND such dataset not used to change the engine. A single day's counts above cannot show improvement; only version-to-version prospective comparison can.
