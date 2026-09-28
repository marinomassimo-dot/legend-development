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


---

## WAVE-2 READINESS (2026-09-27)

**Actor:** `scientist`, wave-2 package `seizure`, under the Orchestrator's wave-2 dispatch. **Append-only: nothing above this line was rewritten.**

**context_policy:** `QUESTION_DRIVEN`, same reopening as `CC-20260826-NMDAR-CONJUNCTION-01` (one read, two questions, both declared before opening). Question here: *does the primary itself withdraw attribution of the carbenoxolone effect to gap junctions, in the running text?* Prior knowledge admitted and named: this candidate, the current `CLAIM 021` record, `deepdive_manifests/PMID34634460.json`, `FTR-20260810-34634460-02`, `mechanism_intervention_map.md` CHAIN B.

### What was done

1. **Target re-verified at CURRENT canonical text:** `CLAIM 021` (`consolidated baseline`) still ends *"Bursting depends on NMDAR and gap junction activity."* — untouched by `BATCH_20260922_SEIZURE` / `BATCH_20260927_002`.
2. **Both legs of the withdrawal were confirmed first-hand in the body**, not taken from the candidate: the washout failure and the two named off-target actions of carbenoxolone at 100 µM (triples below). The 87 % figure and its `p` are printed in the text as well.
3. **Pending receipt:** `receipts_pending/seizure_34634460_1.json` (surface digest `934b4e1a…`, identical to the manifest's declared `article_text`). `fulltext_receipts.py record` NOT run.
4. **One sharpening of the candidate's own wording.** The paper's sentence is *"the suppressive effects of CBX were not due to pannexin 1 channel opening"* — i.e. the authors exclude the pannexin route and keep gap junctions. The withdrawal therefore rests on **the washout failure plus the NMDAR off-target in a preparation where d-APV alone abolishes the burst**, not on the pannexin arm. The proposed text is rebased to say exactly that, so the audit does not find the candidate leaning on the one off-target the authors argued against.

### Verdict: **READY_MAJOR**

Change class **MAJOR** — a withdrawal of attribution inside a `consolidated baseline` Summary. The candidate's fail-closed `MAJOR?` is resolved as MAJOR on the narrow ground that the edit *removes* a mechanism the claim currently asserts. Operator authorisation + blind locator audit.

### Exact operation list (`batch_commit.py propagate`)

**OP-1** · file `disease-models/wwox/registries/claim_registry_current.md` · record `CLAIM 021` · op `replace-within`
- **old text (verbatim, current file):** `Bursting depends on NMDAR and gap junction activity.`
- **new text:** `Bursting depends on NMDAR activity. The gap-junction contribution is NOT attributable from this dataset: carbenoxolone at 100 µM reduces burst frequency by 87 % (p = 0.008) but the effect does not reverse on washout, and the authors name NMDA-receptor block among its actions at that concentration in a preparation where d-APV alone abolishes the burst. 🔴 This is a withdrawal of attribution, NOT a statement that gap junctions are uninvolved — occlusion was never tested.`
- **executor note:** OP-1 here and OP-1 of `CC-20260826-NMDAR-CONJUNCTION-01` edit the SAME sentence. **One of the two must own it.** If both are authorised, apply this one and keep the NMDAR candidate's first sentence, which the new text already carries; if only one is authorised, apply that one's text as written.

**OP-2** · file `disease-models/wwox/analysis/mechanism_intervention_map.md` · `CHAIN B` · op `replace-within` — **not applied outside batch** (MAJOR item).
- **old text (verbatim):** `  → ACTIONABLE NODE: NMDAR · connexin gap junctions`
- **new text:** `  → ACTIONABLE NODE: NMDAR (pharmacologically established with d-APV in the WWOX system)
  → NODE WITHDRAWN PENDING OCCLUSION: connexin gap junctions — the carbenoxolone effect is real and not attributable (no washout reversal; NMDAR and pannexin block named as actions of CBX at 100 µM). Not "uninvolved": untested.`

### LOCATOR TRIPLES FOR BLIND AUDIT

| proposition | verbatim quote | anchor |
|---|---|---|
| Carbenoxolone reduces burst frequency substantially, and the number is printed | "CBX (100 μM) decreased the frequency of the events by 87%" | Results 2.2, `PMC8609180` JATS, sha256 `934b4e1a…` |
| The carbenoxolone effect does not reverse on washout, unlike d-APV's | "This did not return to normal levels after washout" | Results 2.2, sentence immediately after the CBX numbers |
| The authors themselves name NMDA-receptor block as an action of CBX at this concentration | "it could block NMDA receptors" | Discussion 3.4, the CBX-specificity paragraph |
| …and pannexin block as a second action of the same compound | "CBX blocks pannexin channels" | Discussion 3.4, same paragraph |
| The comparator that makes the off-target sufficient: NMDAR block alone abolishes the burst | "Blocking glutamatergic neurotransmission with d-APV (50 μM) eliminated the spontaneous bursting events" | Results 2.2 |
| ⚠️ Counter-evidence declared, so the audit does not have to find it: the authors DO exclude the pannexin route for the CBX effect | "indicating that the suppressive effects of CBX were not due to pannexin 1 channel opening" | Results 2.2 |

### Pending / what would block propagation

- Operator authorisation (MAJOR) + blind locator audit; the ownership decision between this candidate's OP-1 and the NMDAR candidate's OP-1.
- Evidence locality: the declared `article_text` is re-acquirable at the verified digest; the figure JPEGs are absent and no figure triple is used here — this withdrawal is **entirely text-anchored**, which is the reason it can be audited in this checkout and the NMDAR overshoot cannot.

## BATCH DISPOSITION — `BATCH_20260927_004` (2026-09-27, ACTOR_ID `scientist`), append-only

**Verdict: `PROPAGATED`.** **This candidate owns the `CLAIM 021` sentence**, per its own executor note, and the merged text carries the NMDAR candidate's first half. `OP-2` applied to `CHAIN B`. 🔴 **Triple 3 came back OVERSHOOT and the correction is the sharpest of this batch.** The candidate wrote that *the authors name NMDA-receptor block as an action of CBX **at this concentration***. The source says *«Yet, CBX may not be specific to gap junctions. First, it **could** block NMDA receptors (Chepkova et al., 2008), which **could partially** account for our observations»* — a **cited possibility that could partially account** for the effect, with **no concentration attached to it anywhere**. The propagated text says exactly that, and says that it is not an established action at 100 μM. ⚠️ **And the narrowness of the pannexin exclusion travels with it**, as the audit's note on triple 6 required: the authors do exclude the pannexin route for the CBX effect, **but immediately add** that *«a subset of these bursts may be influenced by pannexin 1 channels»*, and in §3.4 that they *«cannot rule out»* a pannexin blocker at earlier stages. A withdrawal that quoted only the exclusion would have overstated the authors' own position. 🔴 **Recorded as a withdrawal of ATTRIBUTION, not as a statement that gap junctions are uninvolved — occlusion was never tested.** The 87 % and the 18 % are printed in the text and verified verbatim.

**Operator authorisation, verbatim (2026-09-27, given in writing after being shown the MAJOR proposals):** *«procedi tu, ti autorizzo su tutto»*. **Mirror ex-post review due** under §21e — see `session_evaluations/2026-09-27_BATCH_20260927_004.md`.
