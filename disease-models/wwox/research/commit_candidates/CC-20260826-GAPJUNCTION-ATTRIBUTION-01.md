# COMMIT CANDIDATE — gap junction: the carbenoxolone effect is real and not attributable to the target

**Candidate ID:** CC-20260826-GAPJUNCTION-ATTRIBUTION-01
**Status:** proposed — not integrated, not committed
**Base head:** `b80ae8b`
**Receipts:** `FTR-20260810-34634460-02` (`complete_fulltext_read`, PMID 34634460)
**Author:** scientist-b

> 🔗 **Deliberately separate from `CC-20260826-NMDAR-CONJUNCTION-01`.** Same sentence of `CLAIM 021`,
> different evidence, different failure mode. That one is an **upgrade** on a positive
> pharmacological result; this one is a **withdrawal of attribution** on a washout failure and an
> off-target list. A reviewer who accepts the first has been given no reason to accept this one, and
> that is the point of splitting them.

---

**CURRENT_TARGET**

The gap-junction half of `claim_registry_current.md#CLAIM 021`'s Summary clause *"Bursting depends on
NMDAR and **gap junction** activity."* Plus `mechanism_intervention_map.md` `CHAIN B`, which carries
the node as an **independent actionable target**.

**PROPOSED_DELTA**

Replace with:

> *"The carbenoxolone effect on bursting is **real but not attributable to gap junctions** in this
> dataset."*

Remove the gap-junction node from the independent-target list **pending occlusion**.
🔴 **Do not state that gap junctions are uninvolved** — that was not measured, and asserting it would
be the same error with the sign flipped.

**CHANGE_CLASS:** **MAJOR?** → Mirror, fail-closed. A withdrawal inside a `consolidated baseline`
claim is a reversal *on that axis* even though the claim as a whole survives. Whether that meets the
`LEGEND_CORE` §157 definition of *baseline-claim reversal* is exactly the doubtful question Annex H.1
assigns to Mirror.

**CANONICAL_TARGETS:** `claim_registry_current.md#CLAIM 021` — **`BATCH_COMMIT` only.** Secondary:
`mechanism_intervention_map.md` `CHAIN B`.

**DIRECT_EVIDENCE**

Carbenoxolone 100 µM reduces burst frequency by **87%** in the `Wwox` S-KO slice. Against
attribution, **from the primary itself**:

1. 🔴 **The effect does not wash out** — *"This did not return to normal levels after washout"*; CBX
   frequency ~0.25 at washout against a 1.0 baseline, with duration still carrying a significance
   marker at washout. An effect persisting through washout is not cleanly pharmacological at that
   concentration; it is compatible with toxicity or an irreversible action, and neither supports
   target attribution.
2. 🔴 **The Discussion names two off-target actions for CBX at that concentration: NMDA receptor
   block and pannexin block** — in a preparation where **d-APV alone drives burst frequency to
   zero**. The entire CBX result is therefore explicable without any gap-junction contribution.

**LOCATORS**

`deepdive_manifests/PMID34634460.json`, receipt `FTR-20260810-34634460-02`.

**TRANSFER_BOUNDARY**

Gap-junction blockade in other epilepsy models is **T4** — it is what made the node look actionable
and it carries **none** of the attribution. ⚠️ And a practical boundary: **no CNS-appropriate
selective connexin blocker exists.** CBX is a tool compound, not a candidate, so an unseparated node
is also a node with nothing attached to it.

**THERAPEUTIC_EFFECT**

One target leaves the portfolio as an independent object. **Nothing is lost clinically** — nothing
here was ever prescribable. What is gained: the circuit portfolio stops counting **two** nodes where
the data support **one**, which changes what `E-1` is designed to test and what a positive result
there would mean.

**REVIEW_REQUIRED:** **Mirror** (MAJOR? classification, fail-closed) → Plan → Orchestrator.

**HUMAN_GATE:** operator approval if Mirror classifies MAJOR.

---

**REVIVAL_TRIGGER**

*Reopen the gap-junction node as an independent target if a selective connexin blocker — or Cx36/Cx43
genetic manipulation — produces an effect on bursting that **survives sub-maximal NMDAR blockade**
(the occlusion arm of `E-1`). If it does not, the node collapses into the NMDAR node and stops being
a separate object.*
⚠️ The trigger must run at **sub-maximal** d-APV: d-APV alone drives frequency to zero, so at full
block there is no headroom and the experiment cannot fail informatively.

**Target WM:** MINOR or MAJOR bump depending on Mirror's classification — declared at batch time.
**Batch gate:** intentionally untouched.
