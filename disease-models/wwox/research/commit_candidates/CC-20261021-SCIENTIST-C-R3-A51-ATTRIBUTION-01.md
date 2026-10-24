# CC-20261021-SCIENTIST-C-R3-A51-ATTRIBUTION-01 — what group R3 adds to the attribution and BLOCK-1 wording of `DL-THER-089`

- **Actor:** `scientist-c` · **Task:** `REPURP-10H-R3-C-20261021`
- **Target records:** `discovery_ledger_current#DL-THER-089` (attribution and BLOCK-1 notes only). No claim is created, reversed or narrowed; no `consolidated baseline` record is touched.
- **target_wm_version:** `WM_v7.27`
- **Change class:** **MINOR, additive.**
- **Sources (all NOT WWOX EVIDENCE):** 38147624 (leukaemia mouse, A51), 40665325 (adult phase 1), 40156289 (CSNK1A1 variants, HEK-293T), 42154236 (neuronal Cdk7 knockout), 42401046 (GSK3 inhibitor, adult TLE). Receipts staged `FTR-20261021-<PMID>-01`; manifests `deepdive_manifests/PMID<PMID>.json`, all PASS.
- **Blind locator audit:** DONE for six of the papers (`page_adjudications/locator_audit_R3_20261022.md`, 129 triples: 78 supported, 46 overshoot, 4 undershoot, 1 unverifiable). The manifests were then repaired by the producer on 2026-10-22; **the repairs are unaudited** and the producer does not certify them.
- **STATUS: PROPAGATED** by `BATCH_20261019_016` on 2026-10-24 — the condition is discharged (see `## BATCH DISPOSITION`). [corrected 2026-10-24 from "**STATUS: HELD from propagation** until the repaired manifests are audited by someone other than the producer." by `BATCH_20261019_016`]
- **What survived the audit and what did not (2026-10-22):**
  - Proposed addition 1: the single-concentration selectivity (38147624 entries 5 and 19) and the D4476 comparison survive; **"the Myc protein change tracks blast percentage lane by lane" did not** (the 99 percent lane carries no Myc band; the blot is one unquantified blot with no statistic: entries 3 and 21), and the inference that the A51 effect is not carried by the CK1-alpha arm was never in the source (entry 6). The earlier flagged schedule conflict in 38147624 is **withdrawn** (entry 14). The conclusion (Myc mediation not supported, hypothesis at most) survives on narrower grounds.
  - Proposed addition 2: the HEK-293T result (beta-catenin, MYC and CCND1 up with either variant) survives (40156289 entries 6 to 8); the framing of the variants as loss-of-function is the authors' expectation ("speculated"), the cells carry no stated endogenous-CK1-alpha status and no empty-vector arm, and the family-to-variant assignment is an **unresolved source-internal conflict** between the Results text and the Fig 1B traces (entry 18). The addition stays an `IPOTESI` with a weaker premise than first written.
  - Proposed addition 3 (42154236 and 42401046) and addition 4: not among the audited papers; unaudited, not affected by this audit.
  - 40665325 (adult phase 1): no dose or tolerability claim is carried by this candidate; the table-based proportionality statements of the earlier note are withdrawn (see the repaired entries 6 and 21 and the corrected note).
- Not medical advice; no dose or suitability is carried forward.

## Proposed additions

1. **Attribution (Wnt versus MYC versus CDK) stays unresolved, and the Csnk1a1 system does not resolve it.** In 38147624 the selective effect of A51 on the double-hit blasts is seen at one of five concentrations, the CK1 inhibitor D4476 did not separate the genotypes, the Myc protein change under A51 rests on one unquantified blot with no statistic and a partial blast-burden confound (the pattern is not simply blast percentage: the 99 percent lane has no Myc band), and the Hallmark Wnt set is not up in the Csnk1a1-haploinsufficient progenitors at the panel the text cites. `INFERENZA` that the A51 effect in that system is Myc-mediated is **not supported**; `IPOTESI` at most.
2. **Direction of the CK1-alpha arm.** In 40156289 two CK1-alpha variants (expected by the authors to be loss-of-function, the cells' endogenous CK1-alpha status and any empty-vector arm not stated; the family-to-variant assignment is an unresolved conflict inside the source) raise cellular beta-catenin and MYC and CCND1 transcripts in HEK-293T. A CK1-alpha inhibitor would on that evidence be expected to push beta-catenin **up**, not down; the organoid result (Wnt-target transcripts up in the knockout, A51 "suppressing Wnt and MYC") would then have to be carried by the CDK7/9 arm. `IPOTESI`, stated as a premise to test, tag `PREMISE: INFERENZA` for the HEK result and `DEFAULT_FROM_TEXTBOOK` for the reading of A51 as a Wnt suppressor (a research target, not a foundation).
3. **BLOCK-1 gets a second and a third reason.** (a) Cdk7 loss in postmitotic cortical neurons costs dendrite and axon growth, cortical thickness and social behaviour (42154236, morphology and behaviour measured, no EEG); (b) a GSK3 inhibitor used as a Wnt activator reduced two of four remodelling markers in one adult epilepsy model and one of four in the other (42401046), so Wnt direction in neural tissue is model-dependent. Neither is an A51 experiment.
4. **Missing measurements to record as the unblocking items** (not novelty claims): brain exposure of A51; any neural readout after a CK1-alpha/CDK7/9 inhibitor at two or more doses in a young animal; a dose-by-timing series of Wnt modulation in developing cortex with progenitor, layer-neuron and electrographic endpoints.

`REVIVAL_TRIGGER` for any rejection implied above: a measurement of A51 in a neural system with an attribution control (a CDK7/9-selective arm and a CK1-alpha-selective arm).

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_016` (2026-10-24, MINOR additive, `WM_v7.27` preserved; ACTOR_ID `integrator`, task `BATCH_20261019_016`)

**The held condition is discharged, and that is the whole reason this candidate moved.** The header's own condition — *HELD from propagation until the repaired manifests are audited by someone other than the producer* — is met, and the integrator verified both audit files first-hand rather than on the coordinator's word:

- **Additions 1 and 2** rest on PMIDs 38147624 and 40156289, whose repairs were audited blind by a different auditor in `page_adjudications/locator_audit_R3_repairs_R3b_20261022.md`. All eleven repaired entries of 40156289 held; seven of the eight repaired entries of 38147624 held, the eighth (`entry 21`, a lane reading) a **minor `OVERSHOOT`** whose adverse part is a *"none visible"* at two intermediate lanes. The part addition 1 actually uses — no Myc band at the highest-burden lane, bands at the four lanes the entry names — is what the auditor **confirmed**; the entry's later restatement of the two intermediate lanes is the producer's own and unaudited, so **nothing about those two lanes was carried**.
- **Addition 3** rests on PMIDs 42154236 and 42401046, audited blind today in `page_adjudications/locator_audit_block1_sources_20261024.md`, exhaustively over both manifests: **43 triples judged, 43 `SUPPORTED`, 0 adverse, 0 unverifiable**, both named propositions `SUPPORTED AS WRITTEN`, with two anchor-level defects (a supplementary-figure numbering mix-up and a wrong ppi note) that leave every content statement verified against the files named.
- **Addition 4** is landed as what it says it is: **unblocking items, not novelty claims**, with no assertion that any of them is absent from the literature at large.

**What landed:** one dated, additive block inside `discovery_ledger_current#DL-THER-089` — attribution and BLOCK-1 notes only, pure addition, no byte of the rest of the record or the file moved (`record_scoped_edit.py replace --id "DL-THER-089"`, 14 insertions, 0 deletions). The `REVIVAL_TRIGGER` this candidate names is recorded verbatim in that block.

**Caveats carried with the claims, as commissioned:** the Cdk7 morphology result is written with **n = 3 per genotype under a one-sided Mann-Whitney whose floor is P = 0.05** and with the **one-sample-per-age-and-genotype** blots; the GSK3 arm is written as **histology and immunohistochemistry at day 14 only, no EEG and no seizure-burden endpoint**. A reader of `DL-THER-089` sees both without leaving the entry.

**Two counts of this candidate were NOT reproduced, and the audited form was written instead.** Addition 1's *"one of five concentrations"*: the audited entry names **four** concentrations, so the block says *"only one of the four concentrations the audited entry names, the highest of them"*. Addition 3's *"two of four remodelling markers"* in the unilateral model: the audited entries carry **three of four** (dispersion, migration and the contralateral cell-count increase, the ipsilateral count unchanged), so the audited enumeration was written. Neither divergence is adverse to the candidate — one is a miscount, the other conservative — and both are declared inside the landed block.

**Held, and still held:** nothing from **40665325** (adult phase 1) is carried in any form. Its dose-proportionality table entry is the one entry of that manifest the blind audit left `OVERSHOOT`, and **no dose, administration, schedule or suitability statement** exists anywhere in what this batch wrote. Every source is labelled `NOT WWOX EVIDENCE`. The **Wnt-versus-MYC-versus-CDK attribution stays unresolved** — which is this candidate's own first proposed addition — and the BLOCK-1 therapeutic-window question of `DL-THER-089` stays open.

---

### Earlier disposition (superseded by the block above, kept for the record)

**Verdict:** DEFERRED
**Batch:** `BATCH_20261019_012`

Handled by `BATCH_20261019_012` (2026-10-22, MINOR, `WM_v7.27` preserved; integrator ACTOR_ID `orchestrator` by stated assumption, task `ORCH-REPURPOSING-10H-20261021`). The candidate stays queued.

- **HELD, not landed: all four proposed additions to `DL-THER-089`** (attribution and BLOCK-1 notes). The dose-proportionality finding of the R3 line was repaired once and failed a second blind audit on four items, and its producer is repairing it again; **no dose-proportionality sentence was written into any registry or ledger**. The coordinator's corrected statement of the finding was received and is deliberately **not reproduced** in any file of this batch, so that no version of a dose-proportionality sentence exists outside the producer's repair; the failed version must not be rebuilt from this candidate's earlier text. The A51 attribution (Wnt against MYC against CDK) stays unresolved and nothing here resolves it.
- **Landed (identity only):** `PAPER` and `LIT` identity records for the R3 readings that had a receipt and no registry identity (the five sources named in the header, the others of the group, and the second wave), each saying the findings are not restated and naming the audit file that covered its manifest. `40665325` carries «no dose or tolerability claim is carried by this record».
- **Still owed:** a blind audit of the repaired manifests by someone other than the producer, then a second attempt at the attribution addition.
