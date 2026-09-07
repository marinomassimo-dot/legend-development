# COMMIT CANDIDATE — NMDAR: upgrade the conjunction actually demonstrated, and only that one

**Candidate ID:** CC-20260826-NMDAR-CONJUNCTION-01
**Status:** proposed — not integrated, not committed
**Base head:** `b80ae8b`
**Receipts:** `FTR-20260810-34634460-02` (`complete_fulltext_read`, PMID 34634460, 21 verbatim
locators, several image-anchored). Receipt depth re-verified this session against
`registries/fulltext_read_receipts.jsonl`; ledger verifies `OK: 128 chained receipt(s)`.
**Author:** scientist-b

> 🔗 **Deliberately separate from `CC-20260826-GAPJUNCTION-ATTRIBUTION-01`.** Both edit the same
> sentence of `CLAIM 021`. They are kept apart because a reviewer can accept this upgrade on the
> strength of the d-APV result and independently refuse the gap-junction withdrawal — the two rest
> on different evidence and fail for different reasons. **Neither presupposes the other.**

---

**CURRENT_TARGET**

`claim_registry_current.md#CLAIM 021` (`consolidated baseline`), Summary, final clause:

> *"**Bursting depends on NMDAR and gap junction activity.**"*

One sentence, two nodes, one verb, no pharmacology, no direction, no magnitude.

**PROPOSED_DELTA**

Replace the **NMDAR half** with:

> *"NMDAR blockade (d-APV) **abolishes** the pathological burst in the `Wwox` S-KO neocortical slice
> at P13–P17 — a pharmacological dependence established **inside** the WWOX-deficient system — with
> a **~1.85× overshoot on washout**."*

And in the map: `CHAIN B` **T2 → T1 for the tool compound only**, recording explicitly that
**memantine has never been given to a WWOX system**.

*(The gap-junction half is the separate candidate. If that one is refused, this delta still stands
and the sentence simply retains its original gap-junction clause.)*

**CHANGE_CLASS:** **MAJOR?** → Mirror, fail-closed. `CLAIM 021` is `consolidated baseline`. This half
**strengthens** the claim rather than weakening it, which is precisely why the classification is
arguable and therefore not mine: under Annex H.1 a doubtful MAJOR is Mirror's call.

**CANONICAL_TARGETS:** `claim_registry_current.md#CLAIM 021` — **one of the four scientific current
files; `BATCH_COMMIT` only.** Secondary: `mechanism_intervention_map.md` `CHAIN B` / `R-02`.

**DIRECT_EVIDENCE**

d-APV takes normalized burst frequency from **1.0 to zero** (Figure 3D-d1, image-read at 6× from
native pixels). On washout, frequency returns to **~1.85×** baseline — recorded, unexplained, and
directly relevant to any chronic-blockade proposal.

**LOCATORS**

`deepdive_manifests/PMID34634460.json`, receipt `FTR-20260810-34634460-02`, `complete_fulltext_read`,
21 verbatim locators.

🔴 **The map's `E-1` was already discharged when the map was written.** The map lists as its
*"highest-value, lowest-cost open item"* a re-read of PMID 34634460 to determine whether the
dependence was established pharmacologically. **The re-read existed, with a complete-read receipt
ten days older than the map, and it was.** The claim's one-verb sentence is what allowed that:
*"depends on"* is compatible with correlation, and the actual result is an abolition.

**TRANSFER_BOUNDARY**

- GRIN2A in the burst-suppression cohort (`DL-MECH-002`) — **T3**.
- Memantine's approved use in other CNS indications — **T5**.
- **Neither carries the upgrade.** The upgrade attaches to the **d-APV conjunction**, not to the
  drug class, and **memantine does not move**: it has still never been given to a WWOX system.
  **The gap is one compound wide, not one experiment wide.** `R-02` remains
  `PROMISING_BUT_MECHANISTIC_GAP`.

⚠️ **Four interpretation risks, recorded rather than resolved:**
1. recordings are **P13–P17** in animals dying at 3–4 weeks; the authors write the stage *"may mimic
   a **late-stage** disorder of WWOX"*;
2. acute *ex vivo* slice ≠ chronic *in vivo*;
3. chronic NMDAR blockade in a developing brain removes a signal required for activity-dependent
   maturation — the process WWOX loss already impairs;
4. 🆕 the *in vivo* hyperexcitability recordings in the sister paper are made **under ketamine, an
   NMDA antagonist** (`deepdive_manifests/PMID34747138.json` entry 13: *"the between-group contrast
   stands; the absolute firing rates are not those of an awake brain"*). Not a contradiction —
   different drug, dose, preparation and endpoint — but a coincidence to resolve by design, not by
   assumption. `PREMISE: INFERENZA`.

**THERAPEUTIC_EFFECT**

The strongest circuit-level conjunction in the portfolio, and it costs nothing to record — the
experiment is already done and in the repository. **It does not promote memantine.**

**REVIEW_REQUIRED:** **Mirror** (MAJOR? classification, fail-closed) → Plan (integration) →
Orchestrator (batch).

**HUMAN_GATE:** operator approval if Mirror classifies MAJOR — per Annex H.1, MAJOR approval is the
operator's.

---

**REVIVAL_TRIGGER** *(for the half that does **not** move — `R-02`, which stays gated)*

*Promote `R-02` when **memantine itself** — not d-APV — reduces burst frequency and phase–amplitude
coupling dose-dependently in a WWOX-deficient system **with isogenic parental and W-AAV-rescue lines
as internal comparators**, and a **chronic** arm shows that the maturation cost of sustained NMDAR
blockade does not exceed the network benefit.*

**Target WM:** MINOR bump if committed (claim modification, no reversal) — declared at batch time.
**Batch gate:** intentionally untouched.
