# ADV-095 proteostasis and HSP70-type premise screen in the held P47T hypomorph tables: result (SCI successor, 2026-11-20; hypothesis level; evidence, not a gate; no dose; not medical advice)

Registered text: `PREREGISTRATION_PROTEOSTASIS_SCREEN_P47T_FROZEN_BEFORE_ANY_VALUE_SCI_20261120.md` (sha256 04168139622376cb0e2f367eefc48dd6dd2cd34ad02540b82051d12a15db5ef7), committed first (4e9a76ca7fd8), then the script (8867c1d887a8), then one run (about five minutes; `out_proteostasis/`: set summary, per-gene table, verdicts). Held data: GSE215425 processed counts, Wwox P47T/P47T against WT/WT, PFC 5 v 5, HPC 5 v 5, parietal cortex (CTX) 5 v 5, cerebellum (CB) 4 v 3; mixed sex (covariate), age not stated in the series text, unit of replication the animal. The table carries 107 duplicated gene symbols (first occurrence used).

## Registered verdict
**`NOT_SUPPORTED_T` for all five sets in the cerebral regions.** No heat-shock, HSP70-type, UPR, autophagy-lysosome or proteasome load premise is supported in the P47T cerebral tissue by this rule.

| Set | PFC | HPC | CTX | Reading |
|---|---|---|---|---|
| HSR (heat-shock response) | flat (raw -1.43 SD, inside the null band) | flat | flat (raw +1.27 SD) | not engaged; signs differ across regions; the inducible members Hspa1a, Hspa1b and Dnajb1 are lower in the prefrontal cortex while Hsph1, Hsp90aa1 and Bag3 are higher |
| HSP70_CONSTITUTIVE | flat | flat | flat | flat |
| ER_CHAPERONE_UPR | flat | SHIFT_UP (raw +0.78 SD) but adjusted sign differs | flat | region-specific, does not survive the composition adjustment |
| AUTOPHAGY_LYSOSOME | flat | flat | flat | flat |
| PROTEASOME | flat | SHIFT_UP (raw +0.84 SD), adjusted sign differs | SHIFT_UP (raw +2.70 SD), adjusted sign same | one region meets the rule, the rule needs two |
Cerebellum (reported separately): HSR flat, HSP70_CONSTITUTIVE flat; UPR chaperones SHIFT_UP (raw +1.77 SD), autophagy-lysosome SHIFT_UP (+2.70 SD) and proteasome SHIFT_UP (+1.48 SD), all three with the adjusted sign the same.

## Reading, with limits
- **Cerebral cortex and hippocampus:** no transcript-level evidence that the proteostasis machinery is engaged in the hypomorph. This is not evidence of no load: protein-level heat-shock induction can be post-transcriptional, the null bands are wide at n = 5 per arm with mixed sex and unknown age, and the inducible HSP70 genes are activity-responsive (a possible reason for their lower prefrontal values, not tested).
- **Cerebellum (post hoc, labelled; not a registered verdict):** the three secondary sets rise together with the adjusted sign unchanged, in the region where Purkinje cell loss is reported for this line; the composition covariates used here (astroglial, microglial, neuronal markers) do not include a Purkinje or granule cell score, and n is 4 against 3. A load signature that accompanies degeneration is one reading; a composition change is the other; the screen cannot separate them.
- **Interpretation of the registered rule (before the run, not after):** for `HSP70_CONSTITUTIVE` and `PROTEASOME` the registered text defined "supported" through the heat-shock and UPR sets only; the script reports a shift in two regions as `SHIFT_REPORTED` for those two. No region pair triggered it.
- **What it changes for the programme:** a chaperone or proteostasis route for a missense hypomorph class has no transcript premise in the P47T cerebral tissue; it is not excluded (protein-level and cerebellar signals remain open), and it does not speak to the Q230P-class allele (a different missense, a different domain). It adds no candidate and removes none.

## Not done
No protein-level data; no agent or exposure comparison; no age-resolved series (the phenotype is progressive and the age of these brains is not in the series text I read). Interpretation hypothesis level only.
