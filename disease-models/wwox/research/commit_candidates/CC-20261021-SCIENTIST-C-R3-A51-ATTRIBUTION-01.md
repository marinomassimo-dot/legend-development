# CC-20261021-SCIENTIST-C-R3-A51-ATTRIBUTION-01 — what group R3 adds to the attribution and BLOCK-1 wording of `DL-THER-089`

- **Actor:** `scientist-c` · **Task:** `REPURP-10H-R3-C-20261021`
- **Target records:** `discovery_ledger_current#DL-THER-089` (attribution and BLOCK-1 notes only). No claim is created, reversed or narrowed; no `consolidated baseline` record is touched.
- **target_wm_version:** `WM_v7.27`
- **Change class:** **MINOR, additive.**
- **Sources (all NOT WWOX EVIDENCE):** 38147624 (leukaemia mouse, A51), 40665325 (adult phase 1), 40156289 (CSNK1A1 variants, HEK-293T), 42154236 (neuronal Cdk7 knockout), 42401046 (GSK3 inhibitor, adult TLE). Receipts staged `FTR-20261021-<PMID>-01`; manifests `deepdive_manifests/PMID<PMID>.json`, all PASS.
- **Blind locator audit:** OWED. Producer is not verifier.
- Not medical advice; no dose or suitability is carried forward.

## Proposed additions

1. **Attribution (Wnt versus MYC versus CDK) stays unresolved, and the Csnk1a1 system does not resolve it.** In 38147624 the selective effect of A51 on the double-hit blasts is seen at one of five concentrations, the CK1 inhibitor D4476 did not separate the genotypes, the Myc protein change tracks blast percentage lane by lane, and the Hallmark Wnt set is not up in the Csnk1a1-haploinsufficient progenitors at the panel the text cites. `INFERENZA` that the A51 effect in that system is Myc-mediated is **not supported**; `IPOTESI` at most.
2. **Direction of the CK1-alpha arm.** In 40156289 loss-of-function CK1-alpha variants raise cellular beta-catenin and MYC and CCND1 transcripts in HEK-293T. A CK1-alpha inhibitor would on that evidence be expected to push beta-catenin **up**, not down; the organoid result (Wnt-target transcripts up in the knockout, A51 "suppressing Wnt and MYC") would then have to be carried by the CDK7/9 arm. `IPOTESI`, stated as a premise to test, tag `PREMISE: INFERENZA` for the HEK result and `DEFAULT_FROM_TEXTBOOK` for the reading of A51 as a Wnt suppressor (a research target, not a foundation).
3. **BLOCK-1 gets a second and a third reason.** (a) Cdk7 loss in postmitotic cortical neurons costs dendrite and axon growth, cortical thickness and social behaviour (42154236, morphology and behaviour measured, no EEG); (b) a GSK3 inhibitor used as a Wnt activator reduced two of four remodelling markers in one adult epilepsy model and one of four in the other (42401046), so Wnt direction in neural tissue is model-dependent. Neither is an A51 experiment.
4. **Missing measurements to record as the unblocking items** (not novelty claims): brain exposure of A51; any neural readout after a CK1-alpha/CDK7/9 inhibitor at two or more doses in a young animal; a dose-by-timing series of Wnt modulation in developing cortex with progenitor, layer-neuron and electrographic endpoints.

`REVIVAL_TRIGGER` for any rejection implied above: a measurement of A51 in a neural system with an attribution control (a CDK7/9-selective arm and a CK1-alpha-selective arm).
