# COMMIT CANDIDATE — cross-claim census, round 2: the reciprocal-citation discriminator

**Candidate ID:** CC-20260826-CROSS-CLAIM-CENSUS-02
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** continuation of [`CC-20260826-CROSS-CLAIM-CENSUS-01`](CC-20260826-CROSS-CLAIM-CENSUS-01.md)
on high-precision signals only
**Change class:** MINOR (annotations) + one capability upgrade, already implemented in
`framework/scripts/cross_claim_contradiction_census.py`
**Batch gate:** intentionally untouched

---

## 1. The discriminator round 1 was missing

Round 1 ranked by shared entity, shared endpoint and opposing direction. It could not tell a
**contradiction nobody has looked at** from a **tension the registry has already reconciled**.

🔴 **The worked example that supplies the discriminator: `CLAIM 009` ↔ `CLAIM 034`.**
`CLAIM 034` reports that in diabetic mouse photoreceptors *more* WWOX means *more* superoxide and
siRNA knockdown **reduces** it — the opposite sign to `CLAIM 009`'s deficiency→ROS framing. The
screen flags it. **But it is not a defect**: `CLAIM 034` says in its own Summary *"La direzione è
opposta alla cornice deficienza→ROS"*, carries a three-reason non-transfer boundary, and
`CLAIM 009`'s `Source` line already lists `PAPER 054` as *"evidenza controdirezionale"*.

**They cite each other. Whoever wrote them had both open.**

Contrast `CLAIM 037` and `CLAIM 011`: they stated opposite things about the same animal for seven
weeks and **neither names the other**.

⇒ **Signal: a genuine cross-claim contradiction is characterised by the *absence* of reciprocal
citation.** Implemented as a `+4` term and a `[NOT CROSS-LINKED]` / `[cross-linked]` label.
It is cheap, mechanical, and it moved the confirmed contradiction to the **top of the ranking**.

**Reproduce:** `python3 framework/scripts/cross_claim_contradiction_census.py`
→ 39 claims · 741 possible pairs · **39 screened positive** · **32 of 39 not cross-linked**
(7 cross-linked), independently recounted by `grep -c` over the per-pair labels.

> 🔴 **Correction, same day.** The first version of this line said **26 of 39**. That number was
> **never measured** — I wrote it from impression while the tool's summary line was scrolled off,
> and the commit message carrying this candidate repeats it. The tool prints `32 of 39`, and a
> `grep -c` over the per-pair `[NOT CROSS-LINKED]` labels independently returns 32 and 7.
> **A count I did not run is an estimate wearing a measurement's clothes**, and the correction is
> recorded here rather than silently applied because the wrong figure is already in the history.

---

## 2. Adjudication, with the operator's five classes

**Nothing ambiguous is counted.** A pair reaches `TRUE_CONTRADICTION` only when no
species/region/stage/endpoint difference explains it and the surfaces have been read.

| Pair | Link | Class | Basis |
|---|---|---|---|
| **`CLAIM 004` ↔ `CLAIM 011`** *(score 18)* | ❌ | 🔴 **TRUE_CONTRADICTION** | Adjudicated at the vector map and three survival panels: [`CC-20260826-DOSE-ADJUDICATION-01`](CC-20260826-DOSE-ADJUDICATION-01.md). Matched lab, strain, promoter, serotype, transgene, WPRE status and titration method; **3–6× lower dose outperforms** |
| **`CLAIM 005`+`CLAIM 037` ↔ `CLAIM 004`+`CLAIM 011`+`CLAIM 016`** | ❌ | 🔴 **TRUE_CONTRADICTION** | A prohibition and an absence-claim against three claims recording the prohibited fact: [`CC-20260826-FIVECLAIM-PACKAGE-01`](CC-20260826-FIVECLAIM-PACKAGE-01.md) |
| **`CLAIM 006`** *(internal, vs its own source)* | n/a | 🔴 **TRUE_CONTRADICTION** | *"progressive microgliosis"* falsified by Fig 3b of PMID 36828035: [`CC-20260826-PROVENANCE-PAPER007-01`](CC-20260826-PROVENANCE-PAPER007-01.md) §3.C. **Not a pair — a claim against its own evidence**, which this census cannot see and which is recorded here so the next round looks for it |
| Obeid 2026 Fig 2B vs Fig 3B *(intra-paper)* | n/a | **NOMENCLATURE_CONFLICT** | *"rescue of lethality"* measured over a **50-day** window in one figure and a **300-day** window in the other |
| Repudi 2021 "rescues premature lethality" vs its own Fig 2C | n/a | **NOMENCLATURE_CONFLICT** | Abstract says *rescued*; the figure title says *extends life span* and the curve reaches 0 % |
| `CLAIM 009` ↔ `CLAIM 034` | ✅ | **CONTEXTUAL_DISSOCIATION** | Opposite manipulations (loss vs induction), different system, **already reconciled in both directions** |
| `CLAIM 003` ↔ `CLAIM 004` | ✅ | **CONTEXTUAL_DISSOCIATION** | Cause vs rescue on a shared source; 004's "incomplete" language is its own comparator boundary |
| `CLAIM 037` ↔ `CLAIM 038` | ✅ | **CONTEXTUAL_DISSOCIATION** | 038's seizure mention is rat-scoped and enters only as a candidate explanation for hypercatabolism |
| `CLAIM 014` ↔ `CLAIM 015` | ❌ | **CONTEXTUAL_DISSOCIATION** | 015's boundary constrains an *inference from a phrase* — the **well-formed** prohibition shape. ⚠️ Not cross-linked, but the pair is complementary, not opposed |
| `CLAIM 011` ↔ `CLAIM 031` / `CLAIM 004` ↔ `CLAIM 031` | ❌ | **CONTEXTUAL_DISSOCIATION** | Murine **gene therapy** vs human **anti-seizure drugs**. Distinct interventions and species |
| `CLAIM 005` ↔ `CLAIM 038` | ❌ | **CONTEXTUAL_DISSOCIATION** | Subsumed by the five-claim package; 038 is rat-scoped |
| `CLAIM 004` ↔ `CLAIM 005` | ❌ | *(component of the five-claim package)* | Counted **once**, there — not again here |
| `CLAIM 031`/`032`/`033` triangle | ❌ | **INSUFFICIENT** | Human survival claims sharing `PAPER 018/042/045`. Consistent monotone dose-of-function story; the flags are vocabulary artefacts. **Not counted** |
| `CLAIM 032` ↔ `CLAIM 038` | ❌ | **INSUFFICIENT** | Cross-species, different endpoints. **Not counted** |
| `CLAIM 037` ↔ `CLAIM 039` | ✅ | **CONTEXTUAL_DISSOCIATION** | Different phenotype: 039's "absent" refers to cerebellar pathology, not seizures |

### Count

| Class | Count |
|---|---|
| 🔴 `TRUE_CONTRADICTION` | **3** (two cross-claim, one claim-vs-own-source) |
| `NOMENCLATURE_CONFLICT` | **2** (both intra-paper, in the primary literature) |
| `CONTEXTUAL_DISSOCIATION` | 7 |
| `MISLOCATOR` | **0** |
| `INSUFFICIENT` | 2 |

⚠️ **`CROSS_CLAIM_CONFIRMED_COUNT = 2`** if the question is *pairs of canonical claims that
contradict each other*. **3** if `CLAIM 006`-vs-its-own-source is included. Both figures are given
because they answer different questions, and reporting one without saying which would be the
denominator error this repository keeps paying for.

---

## 3. A class the census structurally cannot see

🔴 **`CLAIM 006` is a claim contradicted by its own cited source, not by another claim.** No
pairwise screen over the claim registry can find that, because the falsifier is not in the
registry — it is a figure panel.

**Proposed, not built:** a `CLAIM_VS_SOURCE` check that, for every claim whose source has a
schema-v2 manifest with **figure-surface locators**, compares the claim's directional vocabulary
(`progressive`, `increased`, `rescued`) against the locator propositions. `CLAIM 006` says
*progressive microgliosis*; the manifest's Fig 3b locator says *flat*. That is a string-level
mismatch a script can flag.

⚠️ **Bounded honestly:** it only works where figure locators exist. Today that is a handful of
papers. **It must report `n of m claims checkable` every time**, or it reads as coverage it does
not have.

---

## 3b. Round 3 — high-precision sweep, 2026-08-26

**Filter tightened to the operator's specification:** shared **SOURCE** (a PMID or a `PAPER`
record, not merely a shared model) **+** shared model **+** shared endpoint **+** opposing
direction. This is strictly narrower than §1's screen — it asks for pairs of claims that
**rest on the same paper and disagree**.

**8 pairs pass all four conditions; 4 of the 8 are not cross-linked.** The 4 cross-linked ones
(`005↔037`, `031↔032`, `037↔038`, `037↔039`) are excluded by the §1 discriminator without
further adjudication.

### The four uncross-linked pairs, adjudicated

| Pair | Shared source | Verdict |
|---|---|---|
| `CLAIM 005` ↔ `CLAIM 038` | PMID 19936220 | **RESOLVED_BY_CONTEXT** |
| `CLAIM 011` ↔ `CLAIM 031` | `PAPER 011` | 🟡 **NEEDS_LOCATOR** |
| `CLAIM 031` ↔ `CLAIM 033` | `PAPER 018` | **RESOLVED_BY_CONTEXT** |
| `CLAIM 032` ↔ `CLAIM 033` | `PAPER 042` | **RESOLVED_BY_CONTEXT** |

**`CLAIM 005` ↔ `CLAIM 038`.** Both rest on PMID 19936220. `CLAIM 005` records that the paper
contains **no seizure measurement of any kind**; `CLAIM 038` uses it for BUN/creatinine and offers
*"seizure-driven hypercatabolism"* as one of two explanations. **No conflict:** `CLAIM 038` never
attributes a seizure measurement to that paper, tags both explanations `IPOTESI`, and states
neither has been tested.
🔴 **But it produces a downstream consequence worth recording.** `CLAIM 038`'s hypercatabolism
hypothesis, applied to the **mouse**, requires mouse seizures — which `CLAIM 005`'s current
prohibition forbids. **Δ3 of the five-claim package therefore unblocks a hypothesis that is
currently untestable by rule rather than by evidence.** That is an argument *for* the repair that
neither candidate had noticed.

**`CLAIM 011` ↔ `CLAIM 031`.** `CLAIM 031` — *"seizure control does not rescue development"* —
cites `PAPER 011` (Obeid 2026) as *"convergenza"*, alongside its primary human source. But
`PAPER 011` reports **behavioural rescue** (open field, elevated plus maze, rotarod at 3 months)
after **gene therapy**, which is not seizure control and is not obviously convergent with
"control does not rescue".
⇒ 🟡 **`NEEDS_LOCATOR`, not a contradiction.** The claim names a supporting paper **without a
locator saying which finding converges.** The likely intended reading — that gene therapy works
because it acts upstream of seizures, which *supports* the developmental-encephalopathy framing —
is coherent, but it is an inference the claim does not write down. **Proposed:** add a locator, or
demote `PAPER 011` from `Source` to context.

**`CLAIM 031`/`032`/`033`.** Human survival claims on shared sources. The `ABSENT`/`PRESENT` flags
are vocabulary artefacts of a monotone dose-of-function story that all three tell consistently.
**Not counted.**

### 🔴 Round-3 result: NO new confirmed cross-claim contradictions

**`CONFIRMED` = 0 new.** The two already confirmed (`004`↔`011`; the `005`+`037` vs
`004`+`011`+`016` cluster) were found in earlier rounds and are **not re-counted here**. The
running total is unchanged at **2 cross-claim pairs**, or 3 including `CLAIM 006`-vs-its-own-source.

**This is the intended outcome of a high-precision filter.** A sweep that returned new
contradictions every round would be measuring its own threshold, not the corpus.

---

## 4. Proposed canonical effect

1. **Add reciprocal cross-links** between the claims in each confirmed contradiction — `CLAIM 004`
   ↔ `CLAIM 011`, and `CLAIM 005`/`CLAIM 037` ↔ `CLAIM 004`/`CLAIM 011`/`CLAIM 016`. **Independent
   of whether the repairs are authorised**: a link costs nothing and would have surfaced both
   contradictions years earlier.
2. **Record the discriminator** in the LINT proposal from round 1 §5: report the pair *and its
   cross-link state*, and rank unlinked pairs first.
3. **No claim status changes** from this candidate. It routes; it does not repair.

---

## Review required

None for queueing. The confirmed contradictions carry their own authorization requirements in
their own candidates.
