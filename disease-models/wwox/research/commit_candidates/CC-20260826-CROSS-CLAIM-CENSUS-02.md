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


---

## WAVE-2 READINESS (2026-09-27)

**Actor:** `scientist`, wave-2 package `seizure`, under the Orchestrator's wave-2 dispatch. **Append-only: nothing above this line was rewritten.**

**context_policy:** `SYNTHESIS` over the claim registry, by record (`registry_records.py get --id …`), never by grep over the two large registries. No source was reopened: this item adds **links**, not evidence. Prior knowledge admitted and named: this candidate, round 1 and round 3 (`…-CENSUS-03`), the current `Wikilinks` field of every claim it names.

### What was done

1. **The underspecification the triage named is decided here, as the dispatch allows:** 🔴 **`Wikilinks` field only, no prose.** A back-link in a prose field means authoring a sentence, which is not a mechanical repair and is not batchable as one; the discriminator this candidate itself proposes (`[NOT CROSS-LINKED]`) reads the **`Wikilinks` field**, so a link there is what turns the screen off. Any explanatory sentence is a separate, later, claim-scoped decision. **DEFAULTS_TAKEN:** field-only, because it is the reversible half and the half the tooling actually consumes.
2. **Measured the current state, record by record** (no grep): `CLAIM 004` links `PAPER 005 · PAPER 063 · CLAIM 003`; `CLAIM 011` links `PAPER 011` only; `CLAIM 005` links `PAPER 006` only; `CLAIM 016` links `PAPER 019 · PAPER 056 · CLAIM 035`; `CLAIM 037` links `PAPER 058 · PAPER 059 · PAPER 042 · CLAIM 005 · CLAIM 038 · CLAIM 039`. **So `CLAIM 037 → CLAIM 005` exists and `CLAIM 005 → CLAIM 037` does not**: the pair is half-linked, which the screen counts as linked in one direction and is exactly the asymmetry §1's discriminator was built to catch.
3. **The link list is made exact** below, closed under reciprocity, and restricted to the pairs this candidate and round 3 **adjudicated** — the two confirmed contradictions plus the three `RESOLVED_BY_CONTEXT` pairs whose flagging recurs every run (`005↔011` glia, `031↔033` one-patient double count, `032↔033` corroboration). Nothing ambiguous is linked.
4. **The script upgrade** (`+4` term, `[NOT CROSS-LINKED]` label) was verified present in `framework/scripts/cross_claim_contradiction_census.py`; **no harness change is proposed here.**

### Verdict: **READY_MINOR**

Canonical file, so it is still a `BATCH_COMMIT` object, but it is record-scoped, additive, and changes no proposition, status, type or source. **No locator triples are owed:** a wikilink asserts no fact about the world.

### Exact operation list (`batch_commit.py propagate`, file `claim_registry_current.md`, one atomic list)

**OP-1** · record `CLAIM 004` · `replace-within`
- **old:** `**Wikilinks:** [[paper_registry_current#PAPER 005]] · [[paper_registry_current#PAPER 063]] · [[claim_registry_current#CLAIM 003]]`
- **new:** `**Wikilinks:** [[paper_registry_current#PAPER 005]] · [[paper_registry_current#PAPER 063]] · [[claim_registry_current#CLAIM 003]] · [[claim_registry_current#CLAIM 011]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 037]]`

**OP-2** · record `CLAIM 011` · `replace-within`
- **old:** `**Wikilinks:** [[paper_registry_current#PAPER 011]]`
- **new:** `**Wikilinks:** [[paper_registry_current#PAPER 011]] · [[claim_registry_current#CLAIM 004]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 037]] · [[claim_registry_current#CLAIM 040]]`

**OP-3** · record `CLAIM 005` · `replace-within`
- **old:** `**Wikilinks:** [[paper_registry_current#PAPER 006]]`
- **new:** `**Wikilinks:** [[paper_registry_current#PAPER 006]] · [[claim_registry_current#CLAIM 004]] · [[claim_registry_current#CLAIM 011]] · [[claim_registry_current#CLAIM 016]] · [[claim_registry_current#CLAIM 037]] · [[claim_registry_current#CLAIM 040]]`
- ⚠️ **`CLAIM 005` is owned by the `m002` package this wave.** Sequence this OP after theirs, or hand it to them.

**OP-4** · record `CLAIM 016` · `replace-within`
- **old:** `**Wikilinks:** [[paper_registry_current#PAPER 019]] · [[paper_registry_current#PAPER 056]] · [[claim_registry_current#CLAIM 035]]`
- **new:** `**Wikilinks:** [[paper_registry_current#PAPER 019]] · [[paper_registry_current#PAPER 056]] · [[claim_registry_current#CLAIM 035]] · [[claim_registry_current#CLAIM 037]] · [[claim_registry_current#CLAIM 040]] · [[claim_registry_current#CLAIM 005]]`
- 🔴 **identical to OP-3 of `CC-20260826-FIVECLAIM-PACKAGE-01` (Δ6). Apply once.**

**OP-5** · record `CLAIM 037` · `replace-within`
- **old:** `**Wikilinks:** [[paper_registry_current#PAPER 058]] · [[paper_registry_current#PAPER 059]] · [[paper_registry_current#PAPER 042]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 038]] · [[claim_registry_current#CLAIM 039]]`
- **new:** `**Wikilinks:** [[paper_registry_current#PAPER 058]] · [[paper_registry_current#PAPER 059]] · [[paper_registry_current#PAPER 042]] · [[claim_registry_current#CLAIM 005]] · [[claim_registry_current#CLAIM 038]] · [[claim_registry_current#CLAIM 039]] · [[claim_registry_current#CLAIM 004]] · [[claim_registry_current#CLAIM 011]] · [[claim_registry_current#CLAIM 016]] · [[claim_registry_current#CLAIM 040]]`
- ⚠️ `CLAIM 037` is `m002`'s and is also touched by `CC-20260826-CLAIM037-01`'s OP-1 (a different line of the same record). Compose all three into one record-scoped list.

**OP-6** · record `CLAIM 031` · `replace-within` *(round 3's one-patient double count)*
- **old:** `**Wikilinks:** [[paper_registry_current#PAPER 045]] · [[paper_registry_current#PAPER 018]] · [[paper_registry_current#PAPER 011]] · [[claim_registry_current#CLAIM 001]]`
- **new:** `**Wikilinks:** [[paper_registry_current#PAPER 045]] · [[paper_registry_current#PAPER 018]] · [[paper_registry_current#PAPER 011]] · [[claim_registry_current#CLAIM 001]] · [[claim_registry_current#CLAIM 033]]`

**OP-7** · record `CLAIM 033` · `replace-within`
- **old:** `**Wikilinks:** [[paper_registry_current#PAPER 018]] · [[paper_registry_current#PAPER 040]] · [[paper_registry_current#PAPER 041]] · [[paper_registry_current#PAPER 042]] · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 030]]`
- **new:** `**Wikilinks:** [[paper_registry_current#PAPER 018]] · [[paper_registry_current#PAPER 040]] · [[paper_registry_current#PAPER 041]] · [[paper_registry_current#PAPER 042]] · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 031]] · [[claim_registry_current#CLAIM 032]]`

**OP-8** · record `CLAIM 032` · `replace-within`
- **old:** ` · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 031]]`
- **new:** ` · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 031]] · [[claim_registry_current#CLAIM 033]]`
- **executor note:** this is a suffix of `CLAIM 032`'s `Wikilinks` line; address it with the full line if `replace-within` reports ambiguity.

### What is NOT proposed

- The prose sentences round 3 wanted in `CLAIM 031`/`CLAIM 033` (*"the same single patient, counted once"*) and in `CLAIM 032`/`CLAIM 033` (the `DO_NOT_INFER` about a missense allele versus a wild-type allele). They are **real and unwritten**, they change what the claims mean, and they are **DEFERRED to a claim-scoped candidate** rather than smuggled in beside a link. 🔴 Until that lands, the double-counting risk round 3 identified is mitigated only by adjacency.
- Any LINT change. Round 1 §5's proposal is untouched here.

## BATCH DISPOSITION — `BATCH_20260927_003` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** **PROPAGATED IN PART** — `BATCH_20260927_003` (MINOR, MANUAL, `WM_v6.0` → `WM_v6.1`).

`OP-1`–`OP-8` applied: twelve claim-to-claim wikilinks on `CLAIM 004 · 005 · 011 · 016 · 031 · 032 · 033 · 037`, `Wikilinks` fields only, closed under reciprocity. Every `old` line was measured against the live records first and matched byte for byte. The `m002` sequencing warning on `CLAIM 005` and `CLAIM 037` was honoured: the wikilink ops and the Mirror ops address different lines of the same records and were composed into one atomic record-scoped list. **IN PART, deliberately:** the prose sentences round 3 wants in `CLAIM 031`/`CLAIM 033` and `CLAIM 032`/`CLAIM 033` are **not** written — they change what the claims mean and are a claim-scoped decision, so the candidate stays queued for them.

**Mirror ex-post review due** under §21e — see the batch report at `session_evaluations/2026-09-27_BATCH_20260927_003.md`.

## BATCH DISPOSITION — `BATCH_20260927_004` (2026-09-27, ACTOR_ID `scientist`), append-only

**Verdict: `PROPAGATED`.** **Closed: the residue this candidate named is written.** `BATCH_20260927_003` applied `OP-1`–`OP-8` (twelve reciprocal claim-to-claim wikilinks, fields only) and recorded itself `IN PART`, because *the prose sentences round 3 wants in `CLAIM 031`/`CLAIM 033` and `CLAIM 032`/`CLAIM 033` are not written — they change what the claims mean and are a claim-scoped decision*. Both are written in this batch, on all four records, in the wording `CC-20260826-CROSS-CLAIM-CENSUS-03` §1 adjudicated. 🔴 **The double-counting risk round 3 identified is no longer mitigated only by adjacency**: it is stated in both records that name the patient. Nothing of this candidate is owed.

**Operator authorisation, verbatim (2026-09-27, given in writing after being shown the MAJOR proposals):** *«procedi tu, ti autorizzo su tutto»*. **Mirror ex-post review due** under §21e — see `session_evaluations/2026-09-27_BATCH_20260927_004.md`.

## CORRECTION NOTE — 2026-09-28, ACTOR_ID `scientist` (package `m003`), append-only

**Nothing above this line was rewritten.** Written after the Mirror ex-post review of
`BATCH_20260927_003` (findings `M6` and `N2`), whose canonical repair is proposed in
[`CC-20260928-MIRROR003-REPAIRS-01.md`](CC-20260928-MIRROR003-REPAIRS-01.md) op `C40-1`.

**1 · The count is 23 directed links over 14 pairs, not twelve.** Counted from this candidate's own
`OP-1`…`OP-8`: `CLAIM 004` +3, `CLAIM 011` +4, `CLAIM 005` +5, `CLAIM 016` +3, `CLAIM 037` +4,
`CLAIM 031` +1, `CLAIM 032` +1, `CLAIM 033` +2 = **23 directed edges** over **14 distinct pairs**, of
which **13 were newly connected** — the fourteenth, `CLAIM 005 ↔ CLAIM 037`, already carried the
`037 → 005` direction, which §2 of this candidate itself points out. The figure *twelve* in §193, in
the BATCH DISPOSITION above, in the batch report and in the working model's `WM_v6.1` changelog is
reachable by no counting rule any of those surfaces states. The two working-model occurrences are
canonical and are repaired by ops `WM-2`/`WM-3` of the repairs candidate.

**2 · *"closed under reciprocity"* is false for exactly one of this candidate's own adjudicated
pairs.** Recomputed over the whole 41-claim `Wikilinks` graph: of the 14 pairs these ops touched, **13
are closed and one is not** — **`CLAIM 016 → CLAIM 040`**, added by `OP-4`, has no return edge
(`CLAIM 040`'s `Wikilinks`: `PAPER 011 · CLAIM 004 · 005 · 011 · 037`). This matters operationally and
not only editorially: the `[NOT CROSS-LINKED]` discriminator this candidate introduced reads the
`Wikilinks` field, so the screen this op existed to turn off **stays on** for that pair. The return
edge is added by op `C40-1` of the repairs candidate.

**3 · The other ten one-directional edges are pre-existing and are NOT repaired — recorded here as a
measurement.** The Mirror review's M6 also names `CLAIM 040 → CLAIM 004` as *"likewise left
unreciprocated"*. That is **contested**: `040 → 004` pre-existed, `004 ↔ 040` is not in this
candidate's adjudicated pair set, and `OP-1` added `011 · 005 · 037` to `CLAIM 004` and never `040`.
The full census of one-directional claim→claim edges at `a3f68b1` is:

| edge | created by `BATCH_20260927_003`? |
|---|---|
| `CLAIM 016 → CLAIM 040` | ✅ yes — `OP-4`. Repaired |
| `CLAIM 040 → CLAIM 004` | ❌ no — pre-existing, never adjudicated |
| `CLAIM 030 → 032` · `032 → 031` · `033 → 019` · `033 → 030` · `034 → 028` · `035 → 028` · `035 → 030` · `036 → 005` · `041 → 007` | ❌ no — nine pre-existing, untouched |

Closing the ten is a graph-hygiene decision for a dedicated candidate: each is a link some record
chose to make one-directionally, none was adjudicated here, and adding a back-link is an adjacency
judgement — this candidate's own rule is *"Nothing ambiguous is linked."* Treating `040 → 004`
differently from the other nine only because a reviewer named it would be the arbitrary act.
