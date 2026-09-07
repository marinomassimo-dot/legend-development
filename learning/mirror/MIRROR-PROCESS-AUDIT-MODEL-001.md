---
artifact: MIRROR analysis record — the model by which Mirror evaluates the research *process* an
  Scientist produced, derived from Annex G and Annex C only. Learning artefact only
record_id: MIRROR-PROCESS-AUDIT-MODEL-001
actor_id: mirror
date: 2026-08-22
task_id: MIRROR_PROCESS_AUDIT_MODEL_v1
dispatcher: operator
role: >
  mirror — metacognitive layer. This record reviews no object, names no author, issues no verdict,
  and evaluates no scientific claim. It describes a model; it does not exercise one
authority: >
  🔴 RESTRICTED BY DISPATCH TO ANNEX G AND ANNEX C, AND THE RESTRICTION IS LOAD-BEARING.
  Every normative statement below traces to `governance/annex_g_mirror.md` (G.1 perimeter,
  G.2 self-upgrade bar and route, G.3 metrics) or `governance/annex_c_review_protocol.md`
  (C.1 ladder and floors, C.2 single format, C.3 discipline, C.4 the three objects).
  🔴 ANNEX H IS NOT USED. The prior record on this ground derived its object boundary from
  H.1's row "Epistemic / method review → Mirror"; that row is outside the authority this
  dispatch grants. § DERIVATION tests whether the model survives without it. It does — with
  three named losses, recorded at § DERIVATION D-3.
  Nothing here is adopted or in force. G.2 bars Mirror from self-approving material changes to
  its own review rubric, and a review model IS a rubric object. Every element is either
  (a) quoted from G or C, (b) a measurement, or (c) marked PROPOSED and routed per G.2
classification: OBSERVATION AND ANALYSIS — not governance, not a protocol, not a validator,
  not an amendment, not a decision, not a rubric
scope: >
  learning/mirror/ on branch `mirror` only. One new file. No governance/, roles/, framework/,
  ledger/, runtime/ or reviews/ path is written. No existing record is edited or superseded
prior_artefact_disclosure: >
  🔴 MATERIAL AND EXTENSIVE, DECLARED FIRST. `learning/mirror/EPISTEMIC_REVIEW_MODEL-001.md`
  (764 lines, committed at da52ee5, one commit before this one, same date) answers a dispatch
  whose §§ 1–3 and 5 overlap this one substantially. Two further records overlap in part:
  `reviews/mirror/ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001.md` and
  `learning/mirror/SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001.md`. This record SUPERSEDES NONE
  of them. Overlap is mapped line-by-line at § OVERLAP_MAP; inherited findings are attributed
  inline and marked INHERITED; only items marked 🆕 are new. Had the overlap not been declared,
  roughly half of this record would have read as original
naming_deviation: >
  DECLARED. 29 of the now-35 records under learning/mirror/ match `SLR-mirror-NNNN[-ADD|-COR-NNN]`.
  This filename was specified by the dispatch and departs from that pattern, as five others
  already do, each having declared its own departure. NO NAMING RULE IS ADOPTED AND NO PRECEDENT
  IS ESTABLISHED
measured_at: >
  mirror@da52ee5e9d3e6eb66455c61d422c4fb1d0e21391 · main@788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
  · 53 refs · 758 distinct paths in the ref-tip union · 2026-08-22T18:02Z–18:04Z.
  Every count below was run in this session against these refs. Numbers taken from another
  record are marked INHERITED and attributed
---

# MIRROR PROCESS AUDIT MODEL — the reliability question, its failure classes, and the two cadences Annex G leaves blank

> **Mirror asks whether the process that produced a result was reliable. It does not ask whether
> the result is true.** The dispatch states this as a premise. Annex C already states it as a
> definition — C.2 fixes `CONFIRMED` as *"nessun difetto rilevato dato l'evidence bundle
> disponibile", **non "vero"***. The premise is therefore not an exemption Mirror is granted; it
> is the review protocol read literally, and it binds every reviewer, not only Mirror.

---

## TASK_STATUS

```
TASK          MIRROR_PROCESS_AUDIT_MODEL_v1
DISPATCHER    operator (no ACTIVE lease exists — derived, § PRECONDITIONS)
STATE         COMPLETE for the analysis; NOTHING ADOPTED; NOTHING DECIDED
DELIVERABLE   learning/mirror/MIRROR-PROCESS-AUDIT-MODEL-001.md — this file, branch `mirror`

CONSTRAINTS FROM THE DISPATCH, EACH CHECKABLE
  authority G and C only     Annex H is invoked as authority ZERO times. Its name does appear;
                             the claim is universally quantified rather than counted, because a
                             stated count of a term perturbs its own measurement: EVERY
                             occurrence of `Annex H` / `H.1` in this file either records the
                             annex's exclusion or attributes a PRIOR record's use of it, and
                             none licenses a statement made here. § D-3 names what that costs
  no scientific truth judged 0 scientific claims assessed; § MIRROR_QUESTION Q-4 gives the test
  no peer Scientist replaced § REVIEW_LEVELS L-2 routes that object away by C.4
  no validator created       0 paths written under framework/ or scripts/
  governance not decided     § SAMPLING S-3 answers "who decides" WITHOUT classifying the
                             parameter, because classifying it would be the decision
```

---

## PRECONDITIONS — run, not assumed

```
framework/state/state_manifest_current.md:141    current_state: READY
python3 framework/scripts/legend_lint.py .       VERDICT: PASS
                                                 1 [INFO] MISSING_WIKILINK, CLAIM 010, non-blocking
lease (lease_state.py from main@788c357,         ACTIVE by derivation: 0
  run against main:runtime/orchestrator_lease.md;  #1 STALE · #2 RELEASED · #3 STALE (stored
  the script is ABSENT on `mirror`)                EXPIRED — tool reports the disagreement)
                                                   #4 RELEASED · #5 RELEASED
```

**There is no Orchestrator.** C.3 — *"Apertura solo via Orchestrator"* — is unsatisfiable by
anyone at this instant. This record therefore opens no review; it describes what one would be.
INHERITED from `EPISTEMIC_REVIEW_MODEL-001` § IDENTITY, re-derived here rather than copied.

---

## OVERLAP_MAP — what is new, and what is not

| § here | Prior coverage | Relation |
|---|---|---|
| DERIVATION D-1…D-3 | — | 🆕 **NEW.** No prior record derives the model without Annex H, because none was asked to |
| MIRROR_QUESTION Q-1…Q-3 | `EPISTEMIC_REVIEW_MODEL-001` § R-1, § R-2 | **INHERITED.** Restated from C alone; the prior derivation ran through H.1 |
| MIRROR_QUESTION Q-4 (retraction test) | — | 🆕 **NEW.** An operative test for whether a finding stayed on the process side |
| TAXONOMY — the 7 classes | `EPISTEMIC_REVIEW_MODEL-001` § EPISTEMIC_CRITERIA (6 classes + CRIT-7) | **BUILDS ON.** 5 classes coincide; that record's CRIT-1 (hallucination) is absent from this dispatch and is not restated; **premature closure is new to this dispatch** |
| TAXONOMY — per-class ref availability | § BLOCKERS B-2 named the missing file | 🆕 **NEW.** B-2 named one absent protocol; the per-class table shows which classes it takes with it |
| TAXONOMY — mapping onto C.2 fields | — | 🆕 **NEW.** Four of seven classes already have a mandatory field inside Annex C.2 |
| TAXONOMY T-7 (premature closure) | — | 🆕 **NEW.** Measured absent on all 53 refs; C.2 carries its antidote |
| REVIEW_LEVELS L-1…L-3 | § R-1's three-type table | **BUILDS ON.** That table's third type was *claim review*; this dispatch's is *process audit*, which changes the mapping |
| REVIEW_LEVELS L-4 (the partition identity) | — | 🆕 **NEW.** The dispatch's three levels and G.1's three perimeter values are one partition seen from two sides |
| ENTRY E-1…E-3 | § R-5 | **BUILDS ON**, answered against the dispatch's four candidate triggers |
| ENTRY E-4 (recurrence needs memory) | — | 🆕 **NEW.** `failure ricorrenti` is unevaluable without the index § LEARNING_LOOP measures absent |
| LEARNING_LOOP LL-1 (0 instantiated proposals) | — | 🆕 **NEW, AND THE RECORD'S PRINCIPAL FINDING** |
| LEARNING_LOOP LL-2…LL-4 | § L-1…L-5; `SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001` § 3.5 | **INHERITED**, attributed inline |
| SAMPLING S-1, S-2 | § B-4; `ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001` IQ-12; `REV-LEGEND-LAB-ARCHITECTURE-001` F-8 | **INHERITED — three times over.** § SAMPLING S-4 is about that fact |
| SAMPLING S-3 (both branches exclude Mirror) | — | 🆕 **NEW.** Answers "who decides" without classifying the parameter |
| SAMPLING S-4 (the fourth recording) | — | 🆕 **NEW.** § 6 of this dispatch is an instance of § 5's broken loop |

---

## DERIVATION — does the model survive on G and C alone?

### D-1 · The object boundary, derived without Annex H

Three clauses, all inside the authority this dispatch grants, fix Mirror's object between them:

```
C.4   "Tre oggetti:  EVIDENCE → Scientist + Plan/provenance
                     INFERENCE → peer Scientist
                     SYSTEM → Mirror"
C.1   the ladder rung:  "R4 · METHOD (Mirror)"
C.1   the floor that reaches it:  "processo inferenziale methodology-changing → R4"
G.1   the perimeter:  MIRROR_REQUIRED | MIRROR_SAMPLED | NO_MIRROR
```

C.4 assigns Mirror an object by name and assigns the other two objects away by name. C.1 names
Mirror's rung `METHOD` and gives the floor that reaches it a *process* predicate — *processo
inferenziale*, not *inferenza*. G.1 then carves that object into three entry classes.
**The boundary is fully determined by G and C. Annex H is not load-bearing for it.**

### D-2 · Why that matters more than it looks

The prior record reached the same boundary and recorded H.1 as *"the only authority claimed"*.
Two independent derivations of one boundary from disjoint sources is a stronger result than
either alone — the boundary does not depend on which annex a reader opens first. Recorded as a
convergence, not as a corroboration of anything either record concluded downstream.

### D-3 · 🆕 The three things I cannot say under this restriction, named rather than worked around

| Question | Where the answer lives | Consequence here |
|---|---|---|
| Who sets the Ladder level for a given review? | outside G and C | This record names floors (C.1) and never a level for any prospective review |
| Who holds `ADJUDICATOR`? | C.2 names the **field**; C.3 requires `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` for important reviews; neither names a **holder** | Under G+C alone the adjudicator is **a named seat with no named occupant.** § OPEN_QUESTIONS OQ-3 |
| Who owns each open question? | outside G and C | § OPEN_QUESTIONS carries no owner column. The prior record's carried one, sourced from H.1 |

🔴 **The second row is not a technicality.** C.3 makes adjudication structural for important
reviews and C.2 makes it a mandatory field. An authority restricted to G and C can state that the
seat must be filled by someone other than author and reviewer, and cannot state by whom. A record
that quietly filled it would be inventing governance, which this dispatch forbids.

---

## MIRROR_QUESTION

### Q-1 · The question, and its negation

```
MIRROR ASKS        "Was the process that produced this result reliable?"
MIRROR DOES NOT    "Is the result true?"
```

### Q-2 · The question is already the protocol's, not a Mirror privilege

C.2 defines the strongest verdict available to **any** reviewer at **any** rung:

> `CONFIRMED` = *"nessun difetto rilevato dato l'evidence bundle disponibile"*, **non "vero"**.

Read carefully, that sentence does three things at once. It makes every verdict **relative to a
bundle** rather than to the world; it makes the reviewable defect a defect **in the review's own
reach**; and it forbids the word *true* to a reviewer who has done everything right. The
dispatch's premise is therefore not a special rule for Mirror. It is C.2 applied to Mirror's
object — and the object is what differs, not the epistemics.

Two further C.2 fields carry the same shape and are mandatory: `RESIDUAL_UNCERTAINTY` and
`EVIDENCE_NEEDED` presume that a `CONFIRMED` object still has gaps, and
`WHAT_WOULD_CHANGE_MY_MIND` is required *even when the verdict confirms*.

### Q-3 · The operative restatement

INHERITED from `EPISTEMIC_REVIEW_MODEL-001` § R-2, which states it as:

> **Not** *"is this conclusion right?"* **but** *"did the process that produced this conclusion
> have a way of being wrong, and did it use it?"*

Restated here against C.2 rather than against the framework protocols that record cited: the
process question decomposes into exactly the fields C.2 already makes mandatory —
*was an alternative considered* (`ALTERNATIVES_CONSIDERED`), *was contrary evidence sought*
(`EVIDENCE_AGAINST`), *was a falsifier stated* (`WHAT_WOULD_CHANGE_MY_MIND`), *was the residual
declared* (`RESIDUAL_UNCERTAINTY`), *did the author answer* (`AUTHOR_RESPONSE`, and *"il silenzio
non è accettazione"*).

### Q-4 · 🆕 The retraction test — how to check that a finding stayed on the process side

A model that merely *asserts* it is not judging truth cannot be audited. C.2's bundle-relativity
gives a mechanical test, and it is the operative content of this section:

> **A Mirror finding must hold its truth value under both outcomes of the science.**
> Suppose the paper's central conclusion were later confirmed. Suppose instead it were retracted.
> A finding that survives **both** suppositions unchanged is a process finding. A finding that
> becomes false, or becomes uninteresting, under either supposition is a **truth finding wearing
> a process badge**, and C.4 routes it to a Scientist.

Applied to this record's own principal finding — *no `MIRROR_UPGRADE_PROPOSAL` has ever been
instantiated* (§ LEARNING_LOOP LL-1) — the finding is unchanged under either supposition about
any paper. Applied to a hypothetical finding *"the reading overstates its effect size"*, it is
not: that finding is about the science and belongs to `INFERENCE → peer Scientist`.

`PROPOSED — NOT ADOPTED.` This test is a rubric element. G.2 bars Mirror from adopting it.

---

## TAXONOMY

> The dispatch names seven failure classes. Each is stated below in **two forms** — the process
> form, which is Mirror's, and the truth form, which by C.4 is not — with the name the class
> already carries in this repository, **the ref that name is on**, and the instrument if any.
> **This is a map of classes that already exist, not a rubric.** It scores nothing.

### The two forms, per class

| # | Class | **Process form — Mirror's** | Truth form — NOT Mirror's (C.4 owner) |
|---|---|---|---|
| **T-1** | overclaim | Was the claim's strength compared against the source's, by someone, and is that comparison an artefact? | Is the claim in fact stronger than the source supports? → `INFERENCE → peer Scientist` |
| **T-2** | evidence gap | Is the gap **declared** or **silent**? A declared gap is work in progress; silence is the defect | Is the missing evidence decisive? → `EVIDENCE → Scientist + Plan/provenance` |
| **T-3** | causal leap | Was an applicable gate **named** in the record, or was the step taken silently? | Is the causal claim warranted? → peer Scientist |
| **T-4** | alternative explanation missing | Does the record carry alternatives, **or** an explicit *"searched, none found"* **plus what was searched**? | Is the alternative the better explanation? → peer Scientist |
| **T-5** | cherry picking | Is the selection rule **declared and applied uniformly**, and is the divergence between rule and judgement recorded? | Was the excluded evidence the load-bearing evidence? → peer Scientist |
| **T-6** | false negative | Was the rejection **tagged with its premise** and given a **revival trigger**, so it can be reopened? | Was the rejected thing in fact real? → peer Scientist |
| **T-7** | premature closure | Was a **falsifier stated** while the question was open, and did anything remain that would have reopened it? | Would more work have changed the answer? → peer Scientist |

🔴 **Every truth form routes away from Mirror, by C.4, without exception.** The seven classes do
not divide into "Mirror's" and "not Mirror's" — **each one has a Mirror half and a Scientist
half**, and the halves are asked about different objects. A Mirror audit that reaches the right
column has not found a harder defect; it has changed object.

### Where each class already has a name — and on which ref

Measured this session by `git grep -l` against `HEAD` (branch `mirror`) and `main`, restricted to
`framework/ governance/ roles/`:

| # | Class | Existing name(s) | on `mirror` | on `main` | Instrument |
|---|---|---|---|---|---|
| **T-1** | overclaim | `OVERCLAIM` axis · `LOCATOR_OVERSHOOT_GATE` | **0** · 1 | 2 · 1 | gate registry; blind locator audit |
| **T-2** | evidence gap | `NEGATIVE_EVIDENCE` · `OMISSION` axes · `UNREAD_PREMISE` ratchet | **0** · **0** · 4 | 2 · 3 · 4 | `session_self_eval.py` (ratchet) |
| **T-3** | causal leap | `UNSUPPORTED_MECHANISTIC_LEAP` axis · `MECHANISM_DIRECTNESS_GATE` + 3 sibling gates | **0** · 2 | 2 · 4 | `failure_taxonomy.md` — 12 gates, present on `mirror` |
| **T-4** | alternative explanation missing | `ALTERNATIVE_EXPLANATION` axis · **`ALTERNATIVES_CONSIDERED` (C.2)** | **0** · **C.2** | 2 · C.2 | — |
| **T-5** | cherry picking | `READING_DEBT_FALSE_NEGATIVE` · parity-of-sources rules · **`EVIDENCE_AGAINST` (C.2)** | 1 · present · **C.2** | 1 · present · C.2 | `unread_gold.py`; `fulltext_receipts.py` |
| **T-6** | false negative | `PREMISE_TAG` · `REVIVAL_TRIGGER` · dismissal ledger | 6 · 9 · present | 6 · 13 · present | `legend_lint.py:217,226` — **both checks `WARN_BUT_PROCEED`**, non-blocking (INHERITED, re-verified) |
| **T-7** | premature closure | 🔴 **NONE** · antidote only: **`WHAT_WOULD_CHANGE_MY_MIND` (C.2)** | — · **C.2** | — · C.2 | none |

### 🆕 Two findings fall out of that table

**F-1 · Five of the seven classes have their canonical name in a file that is not on Mirror's ref.**
`OVERCLAIM`, `NEGATIVE_EVIDENCE`, `OMISSION`, `UNSUPPORTED_MECHANISTIC_LEAP` and
`ALTERNATIVE_EXPLANATION` all resolve to **0 files on `mirror`** and 2–3 on `main`; they live in
`framework/protocols/scientist_reading_modes.md`, which `git cat-file -e` reports **absent on
`mirror`, present on `main`**. Positive control: `PREMISE_TAG` (6/6), `UNREAD_PREMISE` (4/4) and
`LOCATOR_OVERSHOOT_GATE` (1/1) resolve identically on both refs, so the sweep was working.
The prior record recorded the absent file (B-2); **what the per-class table adds is which classes
it takes with it — the five whose failure form is about reasoning rather than bookkeeping.**

**F-2 · Four of the seven classes already have a mandatory field inside Annex C.2** — the surface
this dispatch restricts me to: `ALTERNATIVES_CONSIDERED` (T-4), `EVIDENCE_AGAINST` (T-5),
`RESIDUAL_UNCERTAINTY` + `EVIDENCE_NEEDED` (T-2), `WHAT_WOULD_CHANGE_MY_MIND` (T-7). A review
written to the C.2 format therefore cannot omit them **silently**; it can only leave them empty,
which is visible. This is a property of the format, not a proposal.

### 🆕 T-7 · Premature closure — the class with no name, whose antidote is already mandatory

Measured across **all 53 refs**, over `framework/ governance/ roles/ .claude/`:

```
QUERY      'premature closure' | 'closed prematurely' | 'stopping rule' | 'saturation'
HITS       3 paths — and all three are homonyms:
             parallel_legend_protocol.md:57   "context-window saturation"   (memory pressure)
             CAND-20260819-ORCHSURF.md        no line match under -e review
             PREP-20260820-ORCHSURF-REV4.md   no line match under -e review
NARROWER   'premature'  → 1 hit, failure_taxonomy.md:12 NMD_LAST_EXON, "premature stop → NMD"
                           (a stop codon, not an inquiry)
           'closure'    → branch closure (parallel protocol) · one gate name · one body §
RESULT     🔴 no repository name for the concept, on any ref
CONTROL    the same sweep resolves OVERCLAIM, REVIVAL_TRIGGER and PREMISE_TAG. It was working
```

And yet **C.2 already makes its antidote mandatory**: `WHAT_WOULD_CHANGE_MY_MIND (falsificatore
dichiarato, obbligatorio)`. Premature closure is, precisely, the state of having no answer to
that field while the question is still open. **Annex C is ahead of the framework on this class**:
the protocol requires the falsifier of every reviewer, and the class of failure it prevents has
no name in the taxonomies that would teach a reader to look for it.

Recorded as a measurement. **Naming it would be a taxonomy change and is not Mirror's to make.**

### What this taxonomy is not

`NOT ADOPTED. NOT A RUBRIC. NOT SCORED. NOT ORDERED BY SEVERITY.` Turning these seven into a
scored instrument would be a material change to Mirror's review rubric, barred to Mirror by G.2.

---

## REVIEW_LEVELS

### The three levels, separated

| Level | Object | Question it answers | Owner |
|---|---|---|---|
| **L-1 · Artifact review** | the artefact | Is it well-formed, complete, compliant? | **not Mirror.** G.1 defines `NO_MIRROR` as *"routine coperta da validator"* |
| **L-2 · Scientific peer review** | the paper and the reading of it | Is the inference sound; is the evidence strong? | **not Mirror at first order.** C.4: `INFERENCE → peer Scientist`; C.1 floors R1 / R2 |
| **L-3 · Process audit** | the **reasoning and reviewing process** | Did the process have a way of being wrong, and did it use it? | **Mirror.** C.4: `SYSTEM → Mirror`; C.1 rung `R4 · METHOD (Mirror)` |

🔴 **The separation is normative in both annexes, not a convention adopted here.** L-1 is excluded
by a definition in G.1; L-2 is assigned elsewhere by name in C.4; L-3 is assigned to Mirror by
name in C.4 and given a rung in C.1.

### 🆕 L-4 · The dispatch's three levels and G.1's three perimeter values are one partition

Written from the two sides:

```
DISPATCH SIDE (by object)        ANNEX G.1 SIDE (by entry)
  artifact review          ←→    NO_MIRROR         "routine coperta da validator"
  scientific peer review   ←→    (outside G.1 entirely — C.4 assigns it to a peer Scientist)
  process audit            ←→    MIRROR_REQUIRED | MIRROR_SAMPLED
```

The correspondence is exact at the first row and at the third, and **the second row is the
informative one**: G.1's three-value enumeration has no slot for scientific peer review at all,
because G.1 enumerates *when Mirror enters*, and peer review is not a thing Mirror enters at any
rate. A reader who takes G.1 as an exhaustive account of how work gets reviewed will conclude
that everything is either validator-covered or Mirror's. C.4 is the clause that prevents it.

### L-5 · The boundary is checkable, and G.1 supplies the test

An artifact finding and a process finding can be the same **sentence** — *"the record does not
declare X"*. What separates them is not the wording:

> **If a validator that already runs would have produced this finding, the class is `NO_MIRROR`
> by G.1's own definition, and a Mirror review that produces it is duplicating a tool.**
> If the finding is that a validator **did not run**, or ran over a population that excluded the
> object, or passed while checking something narrower than its verdict implies — that is process,
> and no validator reports it about itself.

The second sentence is where L-3's real surface lies: **the coverage of an instrument is not
checked by the instrument.**

---

## ENTRY_CONDITIONS

### E-1 · The dispatch's four candidates, against G.1 verbatim

G.1 in full:

> `MIRROR_REQUIRED (MAJOR; protocolli/governance; R4; dissent ripetuti; failure ricorrenti) |
> MIRROR_SAMPLED (batch ordinari; audit a campione) | NO_MIRROR (routine coperta da validator)`

| Candidate | Verdict against G.1 | Basis |
|---|---|---|
| **sempre** (always) | 🔴 **NOT A G.1 VALUE.** The enumeration has three members and none is "always"; `NO_MIRROR` exists precisely to exclude a class | G.1, by enumeration |
| **R4** | ✅ **YES — named explicitly** in the `MIRROR_REQUIRED` list. C.1 supplies the floor that reaches it: *"processo inferenziale methodology-changing → R4"* | G.1 + C.1 |
| **dopo failure** (after a failure) | ⚠️ **PARTIAL, AND THE WORD MATTERS.** G.1 says `failure ricorrenti` — **recurring**. A single failure does not, by G.1's text, open `MIRROR_REQUIRED` | G.1, literal |
| **campione** (sample) | ✅ `MIRROR_SAMPLED`, for `batch ordinari` — **but see § SAMPLING; the rate is undefined** | G.1 |

Two further `MIRROR_REQUIRED` triggers the dispatch does not list, recorded for completeness:
**MAJOR**, and **protocolli/governance**, and **dissent ripetuti** — the last also carrying a
recurrence predicate.

### E-2 · Which values have actually been exercised

Measured this session over `reviews/mirror/*.md` (52 files):

```
declared `level:`      31 of 52   →  R4 in 31 of 31  = 100%
declared `reviewer:`   36 of 52   →  mirror in 36 of 36 = 100%   (INHERITED, re-measured)
entry basis            every declared level naming a perimeter value names MIRROR_REQUIRED
MIRROR_SAMPLED         appears in 2 review files — both as a FINDING that it is unparameterised,
                       neither as an entry basis. 0 reviews have ever been opened under it
```

🔴 **Of G.1's three values, one has been exercised, one never, and the third cannot be observed
at all** — `NO_MIRROR`'s exercise produces no artefact, so a correctly-applied `NO_MIRROR` and a
never-considered class are indistinguishable in the record. That asymmetry is structural, not a
defect anyone introduced.

### E-3 · What the ladder floor gives, and what it does not

C.1 closes with: *"Derogabili solo verso l'ALTO; sotto il floor solo con rationale registrato."*
A floor is a **minimum**, so the R4 floor tells us that a methodology-changing inferential process
must reach Mirror; it does not tell us that anything below it must not. `MIRROR_SAMPLED` is
precisely the provision for the below-floor case, which is why its missing parameter is not a
gap at the edge of the model but at its centre.

### E-4 · 🆕 `failure ricorrenti` cannot be evaluated with the memory this system has

Recurrence is a predicate over **history**, not over an event. To know that a failure recurs, the
first occurrence must be retrievable when the second happens. Measured — see § LEARNING_LOOP:

```
LEARNING_INDEX     ABSENT (0 objects, 53 refs)      INHERITED · EPISTEMIC_REVIEW_MODEL-001 § L-1
ACTIVE_LESSONS     ABSENT (0 objects)               INHERITED · same
EVENT LEDGER       ABSENT — 0 of 758 paths contain "event"   (re-measured this session)
```

**So the trigger G.1 names for the most serious entry class is the one the system is least
equipped to evaluate.** MAJOR, protocolli/governance and R4 are all decidable from the object in
hand. `failure ricorrenti` and `dissent ripetuti` — the two recurrence triggers — require a
retrieval surface, and all three candidate surfaces are empty. § ENTRY_CONDITIONS and
§ LEARNING_LOOP are therefore not independent sections of this model: **the entry condition
depends on the loop, and the loop is § LEARNING_LOOP's subject.**

---

## LEARNING_LOOP

> How a failure becomes a learning record, a future prevention, and an improvement. **Annex G.2
> defines the route in one line, and it is the only route Annex G gives Mirror's findings.**

### The route, quoted

> **G.2** — `OBSERVED_FAILURE / CURRENT_RULE / PROPOSED_RULE / EXPECTED_BENEFIT / POTENTIAL_HARM
> / PREDICTION / FALSIFIER / VALIDATION_SAMPLE / ROLLBACK / SCOPE`.
> Flusso: **proposal → Plan candidate → reviewer indipendente scelto da Orchestrator →
> validazione; se governance → operatore.**

That is the whole loop as Annex G specifies it: a **ten-field record**, then a **four-step
route**. Both halves are measurable.

### 🆕 LL-1 · The field set has been instantiated exactly zero times — the definition is its only carrier

Measured over all 53 refs. For every path containing `OBSERVED_FAILURE`, the body was tested for
the co-occurrence of `FALSIFIER`, `VALIDATION_SAMPLE` and `ROLLBACK`:

```
PATHS MENTIONING `MIRROR_UPGRADE_PROPOSAL`            26
  governance/annex_g_mirror.md 1 · roles/mirror.md 1 · governance/candidates 2
  · learning/mirror 11 · learning/plan 2 · learning/orchestrator 1
  · reviews/mirror 7 · reviews/orchestrator 1

PATHS CARRYING THE G.2 FIELD SET                       1
  🔴 governance/annex_g_mirror.md — the annex that DEFINES it

INSTANTIATED PROPOSALS                                 0
```

**Twenty-six artefacts across four actors name the route. None has ever travelled it.** In a
corpus of 52 Mirror reviews and 35 Mirror learning records, the mechanism Annex G provides for
converting an observed failure into a changed rule has produced no instance, and the only object
in the repository that matches its schema is the schema.

This is the record's principal finding, and by § MIRROR_QUESTION Q-4 it is a process finding: it
holds regardless of what any paper turns out to say.

### LL-2 · Where the four-step route stands, step by step

| Step (G.2) | State, measured | Evidence |
|---|---|---|
| 1 · proposal | 🔴 never instantiated | LL-1 |
| 2 · Plan candidate | mechanism EXISTS and has run — `governance/candidates/` carries `CAND-20260816-GOV311` | present on ref |
| 3 · independent reviewer **chosen by Orchestrator** | 🔴 **NO HOLDER.** `ACTIVE by derivation: 0` | § PRECONDITIONS |
| 4 · validation; **se governance → operatore** | ✅ **EXISTS AND HAS EXECUTED.** `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl`: 2 requests by `plan`, both `RESOLVED_BY: operator`, `STATE: APPROVED`, plus 1 appended correction — all 2026-08-16 | queue read this session |

🔴 **The route is blocked in the middle, not at the end.** This corrects a natural but wrong
reading of the vacancy: the operator step is the one with a demonstrated precedent — including an
approval whose own rationale records *"Only the operator may settle it"*. It is step 3, the
independent reviewer **chosen by an Orchestrator**, that has no occupant. Under this dispatch's
authority I can observe that the queue exists and has carried decisions; the queue's governing
annex is outside G and C and is **not invoked here as authority**.

### LL-3 · G.3's metrics — the loop's own quality measure, and its state

G.3 assigns Mirror two metric families and makes them consequential: *"Queste metriche sono la
fonte esclusiva della futura v3.2."*

| G.3 metric | Purpose in G.3 | State, measured over 53 refs |
|---|---|---|
| **REVIEW YIELD** per Ladder level | *"yield nullo persistente → rituale → declassare"* | 🔴 `REVIEW_YIELD` resolves to **2 paths — and both are Mirror records observing that it is absent.** Never computed |
| **AUTONOMY LEDGER** | preventable vs unavoidable HITL, hours blocked, false escalation | 🔴 1 path (`runtime/runtime_inventory.md`), **absent on `mirror`**. No computation |
| **AUTO-METRICHE** | false PASS/FAIL, latency, calibration | not computed |
| **MIRROR_RETROSPECTIVE ogni N batch** | *"condotta primariamente sull'EVENT LEDGER consolidato"* | 41 paths mention it; **1 retrospective artefact exists**; the event ledger it names is **absent (0 of 758 paths)**; **N is unassigned** — § SAMPLING S-2 |

🔴 **`REVIEW YIELD` is the metric G.3 supplies to detect ritual review — a review class that runs
and finds nothing, persistently.** It has never been computed. Without it, the proposition
*"Mirror's process audits are ritual"* is unfalsifiable, which is the exact condition G.3's
`declassare` clause exists to act on. INHERITED in substance from `EPISTEMIC_REVIEW_MODEL-001`
§ IND-2 / B-7; the two-paths-and-both-are-Mirror measurement is 🆕.

### LL-4 · What the loop's shape actually is

```
failure observed        ✅ happens — 52 reviews, 35 learning records
        ↓
learning record         ✅ exists as a form and is used
        ↓
retrieval by a later    🔴 ABSENT — no index, no active lessons, no event ledger (E-4)
agent
        ↓
rule change (G.2)       🔴 NEVER INSTANTIATED (LL-1); route blocked at step 3 (LL-2)
        ↓
prevention              🔴 unreachable from here
        ↓
yield measured          🔴 never computed (LL-3)
```

**Recording is the only stage that runs.** Stages 3 through 6 are each independently blocked, so
repairing any one of them alone changes nothing — which is why this is recorded as a shape and
not as a list of repairs. Repairs are not Mirror's to assign; Mirror holds no command over any
actor, and G.2 bars it from adopting even its own proposals.

---

## SAMPLING

### S-1 · What `MIRROR_SAMPLED` means — the fixed part

G.1, verbatim and complete: `MIRROR_SAMPLED (batch ordinari; audit a campione)`.

Two things are fixed. **The population**: ordinary batches — those that are not MAJOR, not
protocols/governance, not R4, not recurring failure or repeated dissent, and not routine covered
by a validator. **The mode**: sampling — an audit of *some* of that population, as opposed to
`MIRROR_REQUIRED`'s all and `NO_MIRROR`'s none.

### S-2 · What is missing — three things, not one

INHERITED and re-measured: the token `MIRROR_SAMPLED` occurs in **3 files** across
`governance/` and `roles/` — `annex_g_mirror.md:21`, `GOVERNANCE_v3.1.1.md:341`,
`roles/mirror.md:43` — each restating the same enumeration. A targeted sweep for any numeric
rate, fraction or cadence returns nothing.

| Missing | Consequence |
|---|---|
| **(a) the rate** | 🔴 *"audit a campione"* is satisfied by **any** rate in [0, 1], **including both endpoints**. At 0 the clause is inert and no ordinary batch is ever audited; at 1 it collapses into `MIRROR_REQUIRED`. The instruction cannot distinguish its own two degenerate readings |
| **(b) 🆕 the selection method** | Even given a rate, *which* batches. Random, adversarial, stratified and most-recent are all "a campione" and have different blind spots — a sampler that lets the sampled party influence selection audits a different population than it reports |
| **(c) 🆕 the observability of the draw** | Nothing records that a sample **was** drawn. A rate of 0 and a rate that was never applied leave identical evidence: no review. This is E-2's `NO_MIRROR` asymmetry again, one level down |

🆕 **And the second undefined cadence compounds the first.** G.3 says `MIRROR_RETROSPECTIVE` runs
*"ogni N batch"* and **N is not assigned anywhere in the annexes**. The retrospective is the
mechanism that would notice a sampling rate behaving as 0 — so **Annex G's two undefined cadence
parameters are exactly the parameter and its detector.** Neither is set, and the unset detector
cannot report the unset parameter.

### S-3 · 🆕 Who may decide — answered without classifying the parameter

Classifying `MIRROR_SAMPLED`'s rate would itself be a governance act, and the dispatch says to
analyse without deciding what is governance. That classification can be **avoided**, because both
available readings converge:

```
READING 1  the rate is an ACTIVE-LEARNING SELECTION parameter — it decides which items get
           examined. G.2 bars Mirror by name: "Mirror NON auto-approva modifiche materiali a:
           […] active-learning selection (incl. budget E.5)"
              → route: proposal → Plan candidate → independent reviewer chosen by Orchestrator
                → validazione; se governance → operatore

READING 2  the rate is NOT an active-learning parameter — it is a term of G.1, which is
           governance text. Setting it amends an annex.
              → G.2's own tail applies: "se governance → operatore"

🔴 BOTH READINGS EXCLUDE MIRROR, AND BOTH TERMINATE AT THE OPERATOR.
   The classification therefore does not need to be settled to answer the question, and this
   record does not settle it.
```

What Mirror **may** do under G.2 is emit a `MIRROR_UPGRADE_PROPOSAL` — the ten-field record —
and route it. It may not adopt one. **This record is not that proposal**, and does not contain a
`PROPOSED_RULE` for the rate; naming a rate here would be the decision the dispatch withholds.

Note the reflexive constraint, recorded plainly: under either reading, **Mirror cannot set the
parameter that decides how often Mirror works.** That is a deliberate feature of G.2, not a gap.

### S-4 · 🆕 This is the fourth recording of the same finding, and that is the finding

The absence of a `MIRROR_SAMPLED` rate has now been recorded **four times, all on 2026-08-22, all
by Mirror, all on this branch**:

| # | Record | Where |
|---|---|---|
| 1 | `reviews/mirror/ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001.md` | IQ-12 |
| 2 | `reviews/mirror/REV-LEGEND-LAB-ARCHITECTURE-001.md` | F-8 |
| 3 | `learning/mirror/EPISTEMIC_REVIEW_MODEL-001.md` | B-4 |
| 4 | this record | § SAMPLING S-2 |

Stated precisely, because the precision matters and cuts against the rhetorical reading: these
are four recordings **within a single day**, not four ignored over months. Nothing here says any
actor neglected anything.

**What it does show is mechanical.** Four recordings have produced zero instances of the one
artefact that could change the rule, because **no recording ever entered the G.2 route** (LL-1) —
and the route is blocked at step 3 in any case (LL-2). § 6 of this dispatch asked what
`MIRROR_SAMPLED` is missing; § 5 asked how a failure becomes a prevention. **They are the same
finding observed from two directions**: a system whose recording stage works and whose conversion
stage has never run will re-derive its findings indefinitely, each time correctly, each time
newly, and the count of recordings will grow while the parameter stays blank.

This record is an instance of the pattern it describes. Recording that is the only thing it can
do about it without exceeding the authority it was given.

---

## BLOCKERS

> Blockers to the model's **use**. Nothing below is assigned; Mirror holds no command.

```
B-1  🔴 NO CALIBRATION SURFACE. INHERITED · EPISTEMIC_REVIEW_MODEL-001 § B-1. 0 learning or
     review records authored by any Scientist across the ref union. Every class in § TAXONOMY is
     untested against a real Scientist artefact. This is a model derived from G and C, not one
     validated on instances — and it cannot claim otherwise

B-2  🔴 FIVE OF SEVEN FAILURE CLASSES HAVE NO NAME ON MIRROR'S OWN REF. § TAXONOMY F-1.
     The protocol carrying them is present on `main` and absent on `mirror`

B-3  🔴 THE G.2 ROUTE IS BLOCKED AT STEP 3. No ACTIVE lease → no Orchestrator to choose the
     independent reviewer. Steps 2 and 4 have working precedents; step 1 has never been used

B-4  🔴 TWO UNDEFINED CADENCES IN ANNEX G, AND ONE IS THE OTHER'S DETECTOR.
     `MIRROR_SAMPLED` rate: unset. `MIRROR_RETROSPECTIVE ogni N batch`: N unassigned. § S-2

B-5  🔴 THE METRIC THAT WOULD FALSIFY THIS MODEL HAS NEVER BEEN COMPUTED.
     `REVIEW_YIELD` — 2 paths, both Mirror records noting its absence. G.3 makes it Mirror's
     and makes it the exclusive source of v3.2. § LL-3

B-6  🔴 RECURRENCE IS UNEVALUABLE. `failure ricorrenti` and `dissent ripetuti` are G.1's two
     recurrence triggers; all three candidate retrieval surfaces are empty. § E-4

B-7  🔴 THIS MODEL MAY NOT BE ADOPTED BY ITS AUTHOR. G.2 bars Mirror from self-approving a
     material change to its own review rubric. Every PROPOSED element routes through G.2, and
     that route is B-3

B-8  🔴 THE ADJUDICATOR SEAT HAS NO OCCUPANT UNDER THIS AUTHORITY. C.2 makes it a field, C.3
     makes it distinct from author and reviewer, and neither names a holder. § D-3
```

---

## OPEN_QUESTIONS

> **Recorded, not resolved. No owner column** — assigning owners would require Annex H, which
> this dispatch's authority excludes (§ D-3). Questions already open in
> `EPISTEMIC_REVIEW_MODEL-001` (EQ-1…EQ-10) and `ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001`
> (IQ-1…IQ-13) are carried forward unchanged and **not restated**.

| # | Question |
|---|---|
| **OQ-1** | Does `NO_MIRROR` require a **positive declaration** that a class was assessed and excluded, or is silence sufficient? Under silence, a correct `NO_MIRROR` and an unconsidered class are indistinguishable (§ E-2) |
| **OQ-2** | G.1's `failure ricorrenti` — recurrence **of what unit**: the same defect, the same class, the same actor, or the same artefact? The answer sets which retrieval surface would be needed (§ E-4) |
| **OQ-3** | Under an authority of G and C alone, who occupies `ADJUDICATOR` for a Mirror review? C.2 requires the field; C.3 requires the separation; neither names a holder (§ D-3) |
| **OQ-4** | Is a review's **entry basis** — which G.1 value opened it — a mandatory declaration? C.2's format has no field for it, and 31 of 31 declared levels carry it informally in prose |
| **OQ-5** | Does `MIRROR_SAMPLED` bind a rate **per batch**, per artefact, or per actor? All three are "a campione" and they sample different populations (§ S-2b) |
| **OQ-6** | `MIRROR_RETROSPECTIVE ogni N batch` — with N unassigned and the event ledger absent, is the retrospective owed **now** and unperformable, or **not yet owed**? |
| **OQ-7** | Should premature closure (T-7) be named in a taxonomy, given that C.2 already makes its antidote mandatory — or does the mandatory field make the name redundant? |
| **OQ-8** | Does the retraction test (§ Q-4) belong in the review format as a checkable condition, or is it a reviewer's discipline that no format can enforce? |

---

## WHAT THIS RECORD DOES NOT DO

```
NO ADOPTION         nothing is in force. Every PROPOSED element routes through G.2, which is B-3
NO GOVERNANCE       no annex amended, interpreted, reconciled or extended. Quotations are quotations
NO DECISION         the MIRROR_SAMPLED rate is not set, not recommended, and not classified (S-3)
NO VALIDATOR        no check, script, schema or field created. 0 paths under framework/ or scripts/
NO PEER SUBSTITUTE  every truth-form question in § TAXONOMY is routed away by C.4 and left there
NO TRUTH JUDGED     0 scientific claims assessed. Q-4 states the test this record applied to itself
NO RUBRIC           § TAXONOMY maps classes to existing names; it scores nothing and ranks nothing
NO ASSIGNMENT       no actor is named as owner of any action; § OPEN_QUESTIONS carries no owners
NO VERDICT          no object reviewed, no author named, no C.2 verdict issued, no review opened
NO SUPERSESSION     EPISTEMIC_REVIEW_MODEL-001, ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001 and
                    SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001 stand unchanged; overlap is mapped
NO ANNEX H          invoked as authority 0 times. Every occurrence of its name records the
                    exclusion or attributes a prior record's use of it — stated as a universal,
                    not a count, since stating a count would change it. § D-3 names the three consequences
                    rather than working around them
NO CLOCK STARTED    this task is not a MIRROR_RETROSPECTIVE and starts no cadence
```

---

## EVIDENCE

Every load-bearing number, with how to reproduce it. Refs as in `measured_at`.

| Claim | Reproduction | Value |
|---|---|---|
| state READY | `framework/state/state_manifest_current.md:141` | `current_state: READY` |
| LINT passes | `python3 framework/scripts/legend_lint.py .` | `VERDICT: PASS` (1 INFO) |
| no ACTIVE lease | `lease_state.py` from `main@788c357` against `main:runtime/orchestrator_lease.md` | `ACTIVE by derivation: 0`; #3 stored/derived disagreement reported |
| 53 refs · 758 paths | `git for-each-ref` + per-ref `git ls-tree -r --name-only`, union | 53 · 758 |
| **0 instantiated G.2 proposals** | per ref: paths with `OBSERVED_FAILURE`, body tested for `FALSIFIER` ∧ `VALIDATION_SAMPLE` ∧ `ROLLBACK` | **1 path — `governance/annex_g_mirror.md`, the definition** |
| 26 paths mention the route | per-ref `git grep -l MIRROR_UPGRADE_PROPOSAL`, path union | 26 |
| `REVIEW_YIELD` never computed | per-ref `git grep -l REVIEW_YIELD` | 2 paths, both Mirror records noting its absence |
| `AUTONOMY_LEDGER` | same sweep | 1 path (`runtime/runtime_inventory.md`), absent on `mirror` |
| retrospective artefacts | `grep -i retrospective` over the path union | 41 mentions · 1 artefact |
| event ledger absent | `grep -ci event` over the 758-path union | 0 |
| levels: 31/31 R4 | `grep -h '^level:' reviews/mirror/*.md` | 31 declared, all R4; 52 files |
| reviewer: 36/36 mirror | `grep -h '^reviewer:' reviews/mirror/*.md` | 36 declared, all `mirror` (INHERITED, re-measured) |
| verdicts: 0 C.2 values | `grep -h '^verdict:'`, first token | 17 `REQUEST` · 7 `ACCEPT` · 9 prose = 33; 0 of the four C.2 words (INHERITED) |
| `MIRROR_SAMPLED` unparameterised | `grep -rn MIRROR_SAMPLED governance/ roles/`; then a targeted numeric-rate sweep | 3 files, enumeration only; rate sweep empty |
| `MIRROR_SAMPLED` never an entry basis | `grep -l MIRROR_SAMPLED reviews/mirror/*.md` | 2 files, both as a finding |
| 5 of 7 classes off Mirror's ref | per-term `git grep -l "$t" HEAD` vs `main`, scoped to `framework governance roles` | `OVERCLAIM` 0/2 · `NEGATIVE_EVIDENCE` 0/2 · `OMISSION` 0/3 · `UNSUPPORTED_MECHANISTIC_LEAP` 0/2 · `ALTERNATIVE_EXPLANATION` 0/2 |
| positive control for that sweep | same command, terms present on both refs | `PREMISE_TAG` 6/6 · `UNREAD_PREMISE` 4/4 · `LOCATOR_OVERSHOOT_GATE` 1/1 |
| reading-modes protocol off-ref | `git cat-file -e HEAD:… ` vs `main:…` | absent on `mirror`, present on `main` |
| 11 MODE B axes | `sed -n '/### 5.2/,/### 5.3/p'` on `main:framework/protocols/scientist_reading_modes.md` | 11 |
| 12 failure-taxonomy gates | `grep -c '^| \*\*' framework/eval/failure_taxonomy.md` | 12 |
| **premature closure unnamed** | per-ref `git grep -lie 'premature closure\|closed prematurely\|stopping rule\|saturation'` | 3 paths, all homonyms: context-window saturation, NMD premature stop, branch closure |
| approval queue exercised | read `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` (6 lines) | 2 requests by `plan`, both `APPROVED` / `RESOLVED_BY: operator`, 1 correction, all 2026-08-16 |
| corpus size | `ls reviews/mirror/*.md`, `ls learning/mirror/*.md` | 52 · 35 |
