---
artifact: MIRROR observation record — independent review without circular validation, measured
record_id: ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001
task_id: INDEPENDENT_REVIEW_PROTOCOL_ANALYSIS_v1
iteration: 1/1 (no iteration count given by the dispatch)
mode: OBSERVATION AND REVIEW METHODOLOGY ONLY
actor_id: mirror
dispatcher: operator
date: 2026-08-22
governance_version: 3.1.1 (read, not exercised)
authority_claimed: none
classification:
  - MEASUREMENT ONLY — the dispatch says "Do not solve. Measure."
  - NOT GOVERNANCE · NOT A PROTOCOL · NOT AN AMENDMENT · NOT A DECISION
  - NO IMPLEMENTATION · NO CORRECTION MEMORY CREATED
  - NOT A REVIEW under Annex C.2 — it has no OBJECT, no AUTHOR and no VERDICT, and is
    deliberately not named REV- so it is not counted as one by the census it performs
domain: >
  CONTROL_PLANE. `reviews/` is among the exhaustive CONTROL_PLANE_ROOTS at
  `main@788c357:governance/plan_defined_parameters.md:258-262`, re-measured this session.
  This file moves no CANDIDATE_CONTENT_HASH.
self_exclusion: >
  This record analyses the review system Mirror is the sole occupant of. Annex G.2 bars Mirror
  from self-approving material changes to its review rubric, learning clustering,
  active-learning selection, review-yield methodology or autonomy-classification methodology.
  Nothing here changes any of those. Every requirement in REVIEW_MODEL § 3 is traced to a
  source that already exists, or is marked NO SOURCE and left unsupplied.
---

# INDEPENDENT REVIEW WITHOUT CIRCULAR VALIDATION — measured

> **This record measures. It defines no rule, adopts no protocol, assigns no actor, opens no
> review, resolves no finding and creates no correction memory.** Where the dispatch asks for
> observational requirements (§ 3), each is traced to an existing normative source or marked as
> having none.

---

## TASK_STATUS

```
TASK_ID       INDEPENDENT_REVIEW_PROTOCOL_ANALYSIS_v1
MODE          OBSERVATION / REVIEW METHODOLOGY
STATE         COMPLETE — five study areas measured, one census built over the full review corpus
POPULATION    73 distinct artifacts under reviews/ · 72 under learning/ · 37 heads
BLOCKING      none
NOT DONE      no solution, no design, no rule, no rubric change, no correction memory,
              no adjudication, no assignment
```

**Instrument discipline.** Every negative claim below carries a positive control, after a
`NOT_FOUND`-on-every-ref sweep in the previous session turned out to be a zsh parameter-modifier
artifact rather than a fact. Controls used: `ledger/approvals/` → 21 ref-hits;
`STEELMAN` → 43 distinct files; `grep -c 'def ' legend_lint.py` → 26.

---

## IDENTITY

**From repository evidence. No authority is read from `roles/mirror.md` — that contract is
`PROPOSED` and `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (main) determines
`OPTION B — ACTIVATION_NOT_CONFIRMED` for all four contracts.**

| Fact | Measured value |
|---|---|
| Working directory | `<REPO_ROOT>/.claude/worktrees/mirror` |
| Branch | `mirror` |
| HEAD | `7a607b00159c054de9d86b75886a370aa52b41e4` |
| HEAD subject | *"The record that named the drift was addressed as a protocol before its ink dried…"*, 2026-08-22T19:08:46+0200 |
| Working tree | clean before this record |
| vs `main` | **75 ahead · 65 behind** |
| Lease | `ACTIVE by derivation: 0`, on both extant populations — 5 rows on `main`, 9 on `orchestrator` |
| `ACTOR_ID` | `mirror` — registry card `REGISTERED_PENDING_L1_L2`, all four capabilities `UNVERIFIED` |
| `SESSION_REF` | not observable, not invented |

🔴 **Standing declared, because this record's subject is the seat it is written from.** Mirror is
the sole occupant of the reviewer position measured below (39 of 39 declared reviewers). Every
finding about reviewer concentration is a finding about this actor. `roles/mirror.md` — the one
contract that would govern the reviewer — received **no verdict** in the only hostile review of
the four contracts, under the self-review prohibition. **I cannot cure that from here and do not
try.** Annex G.2's route runs through Plan and an independent reviewer chosen by Orchestrator;
there is no Orchestrator.

**Authority claimed: none.** No gate asserted, no verdict issued, no actor directed, no rule made.

---

## SURFACE_MAP

```
MEASURED_AT     2026-08-22T17:16Z … 17:34Z (session clock, UTC)
REFS            37 local heads · 4 remote · 5 tags   ·   WORKTREES 19
ARTIFACTS       73 distinct paths under reviews/   —  mirror 51 · orchestrator 15 · plan 7
                72 distinct paths under learning/  —  mirror 34 · plan 24 · orchestrator 14
                41 of the 73 are REV-* files (reviews proper)
```

### Where the review corpus lives

| ref | `reviews/` files |
|---|---|
| `mirror` | **51** |
| `orchestrator` | 14 |
| `plan-orchsurf-r4-transcription` | 7 |
| `orchestrator-surface` | 5 |
| `author-response-orch-state-reconstruction` | 4 |
| **`main`** | **3** |
| six further heads | 3 each (the same three) |

**No ref carries more than 70% of the review corpus, and the trunk carries 4%.**

### 🔴 The surface moved again, and it falsified a true statement in 8 minutes

`REV-LEGEND-LAB-ARCHITECTURE-001` recorded, verified at ~17:0xZ, that the dispatch's two named
objects returned **0 hits across 37 heads**. Both now exist:

```
learning/orchestrator/LEGEND-AGENT-COORDINATION-PROTOCOL-001.md
   orch-agent-coordination-protocol @ f8532c9   committed 19:08 local (17:08Z)   943 lines
learning/plan/SCIENTIST-PIPELINE-EXECUTION-MODEL-001.md
   plan-orchsurf-r4-transcription @ a10a11a     committed 19:02 local (17:02Z)   955 lines
```

The prior statement was true when measured and false eight minutes later. **That is the
measured half-life of a review whose `OBJECT` is not a frozen identifier** — Annex C.2 requires
`OBJECT` to be a claim id, a `CANDIDATE_CONTENT_HASH` or a directive id precisely so this cannot
happen, and no review of a `learning/` blob can satisfy it. Recorded as a property of the review
protocol, not as a correction: nothing in the earlier record needs changing.

---

## REVIEW_MODEL

### 1 · Who creates, who reviews, who adjudicates — measured, not described

Extracted from the frontmatter of all 73 artifacts under `reviews/`:

```
REVIEWER      declared in 39        mirror  39 / 39      = 100 %
AUTHOR        declared in 30        plan    25           =  83 %
                                    orchestrator  3      =  10 %
                                    other/composite 2
ADJUDICATOR   declared in 36        operator      ~29    =  81 %
                                    orchestrator   ~6    (always paired with operator HUMAN_APPROVAL)
                                    NOT ASSIGNED    1
```

🔴 **One actor holds 100% of the reviewer position across the entire history of the laboratory.**
Annex C.3 and body § 26 both require **`rotazione` (rotation), never fixed pairs**. The measured
pairing is not merely fixed — it is singular. There has never been a second reviewer.

### 2 · The ladder has six rungs and one has ever been climbed

```
LEVEL declared in 32 artifacts.   R4 : 32 / 32  = 100 %
                                  R0, R1 PEER, R2 INDEPENDENT, R3 TRIADIC, R5 CROSS-MODEL : 0
```

Mentions anywhere in a review body (a weaker test, included so the zero is not a search artifact):
`R0` 2 · `R1` 2 · `R2` 9 · `R3` 1 · `R4` 37 · `R5` 1 — and every one of those is a citation of the
ladder, not an instance of the level.

**R4 is `METHOD (Mirror)` by C.1.** So *the ladder collapsed into the one rung whose occupant is
Mirror*, and every independence route that does **not** pass through Mirror — peer review between
Scientists (R1), semi-blind independent review (R2), triadic resolution (R3), cross-model review
by Codex (R5) — has never been exercised once.

### 3 · The verdict vocabulary in use is not the verdict vocabulary in the annex

Annex C.2 fixes four values: `CONFIRMED | WEAKENED | REFINED (+REFINED_FORMULATION) | REFUTED`.
Measured `verdict:` field values across the corpus:

```
verdict: fields present                               32 of 73
  REQUEST CHANGES                                     17
  ACCEPT                                               7
  BINDING VERIFIED  2 · NOT ATTESTED  2 · ACK  1 · descriptive prose  3
  🔴 one of the four C.2 values, as the declared verdict:   0
```

The four C.2 words appear in 44 of 73 bodies — as discussion of the protocol, not as the verdict.

🔴 **Zero. Not one review in the corpus declares a C.2 verdict in its verdict field**, and that
includes `REV-LEGEND-LAB-ARCHITECTURE-001`, written by this actor ninety minutes ago: it carries
`review_id`, `level`, `reviewer`, `author` and `adjudicator` in frontmatter and puts its
`WEAKENED` / `REFINED` verdicts in a **body table**, so the field the census reads is absent. The
non-conformance is not historical and not someone else's. It was reproduced by the actor
performing this measurement, one artifact before performing it.

🔴 **The two vocabularies do different jobs, and the substitution changes what a reviewer is.**

```
CONFIRMED | WEAKENED | REFINED | REFUTED     an EPISTEMIC assessment of a claim's truth status.
                                             CONFIRMED = "no defect found given the evidence
                                             bundle", explicitly never "true".
ACCEPT | REQUEST CHANGES                     a GATE decision on whether an object may proceed.
                                             Binary, blocking, and about the artifact, not the claim.
```

A gatekeeper and an epistemic assessor need different independence guarantees: an assessor's
error is a wrong belief that a later reader can re-derive; a gatekeeper's error stops or releases
work, and nobody re-derives a release. **The single reviewer has been performing the gate
function under the name of the assessment function**, and C.2 supplies independence rules
calibrated for the second.

### 4 · The lifecycle, stage by stage — existing vs missing

```
AUTHOR ───────► REVIEWER ───────► RESPONSE ───────► ADJUDICATION
```

| Stage | Mechanism | Measured state |
|---|---|---|
| **AUTHOR** | `WORK_COMMIT` on the actor's own branch (H.1, D.1) | ✅ **EXISTS AND RUNS.** 25 of 30 authored by `plan` |
| **opening** | *"Apertura solo via Orchestrator"* (C.3) | 🔴 **MISSING IN PRACTICE.** 0 `ACTIVE` leases; there is no Orchestrator. Every review in this corpus was opened by an operator dispatch. `OPEN-`/`CLOSE-` artifacts exist for **1 cycle of 17** (`ORCHSURF-MIRROR-002`, 13 files) |
| **REVIEWER** | Annex C.2 single format | ⚠️ **EXISTS, PARTIALLY CONFORMANT.** All six C.2 header fields present in **21 of 73**; `STEELMAN` in 36; declared falsifier in 36 |
| **RESPONSE** | `AUTHOR_RESPONSE`, C.2 *"obbligatoria; il silenzio non è accettazione"* | 🔴 **MISSING FOR MOST.** 7 response artifacts, covering **6 of 17 review cycles**. Eleven cycles have no response |
| **ADJUDICATION** | C.3 `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`; H.1 challenge adjudication → Orchestrator | ⚠️ **PARTIAL.** Declared in 36 artifacts; the adjudicator is the operator in ~81%. **No adjudication artifact class exists** — the field is a frontmatter declaration, not a record |
| **dissent / challenge** | Annex F: `CHALLENGE_ID`, `ORCHESTRATOR_CHALLENGE`, F.3 lifecycle | 🔴 **ZERO INSTANCES.** See below |
| **max 2 rounds → adjudication** | C.3 | 🔴 **EXCEEDED, uncontested.** `SCIAB` ran **6 rounds** (`REV-SCIAB-MIRROR-001…006`); `P51C9` ran 3 plus 3 addenda; `GOV311`, `HASHDET`, `C9-STATE-MODEL` ran 3 each |
| **review yield** | G.3, one of Mirror's two exclusive metrics | 🔴 **NEVER COMPUTED.** `REVIEW_YIELD`: **0 files on 37 heads.** `AUTONOMY LEDGER`: 3 files, all definitions |

🔴 **The challenge apparatus has produced nothing, ever.** Measured across all 37 heads with a
positive control:

```
CHALLENGE_ID              1 distinct file   — governance/annex_f_challenge_dissent.md (the definition)
ORCHESTRATOR_CHALLENGE    3 distinct files  — GOVERNANCE body, annex B, annex F (all definitions)
DISSENT_ID                0 distinct files  — the identifier is not defined anywhere, including annex F
VALIDATED_LATER           4 distinct files  — body, annex F, roles/mirror.md, and this session's own review
POSITIVE CONTROL          STEELMAN → 43 distinct files. Instrument working.
```

**Not one challenge has been raised, adjudicated, overridden or later validated.** Annex F.3
assigns Mirror the question *"which classes of dissent does Orchestrator tend to `OVERRIDE` that
later prove `VALIDATED_LATER`?"* — that statistic has a population of zero, and would have one
even if the event ledger existed.

---

## INDEPENDENCE_ANALYSIS

### I-1 · The review graph is a single repeated edge

```
                    plan  ──authors──►  25 of 30 reviewed objects
                      │
                      ▼
                   mirror  ──reviews──►  39 of 39
                      │
                      ▼
                  operator ──adjudicates──►  ~29 of 36
```

Three nodes, two edges, no alternates. C.3's `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` is **satisfied
in every instance** — and satisfying it costs nothing when each role has exactly one candidate.
**The constraint is met and buys no independence**, because independence comes from the
possibility of a different reviewer, not from the reviewer differing from the author.

### I-2 · 🔴 A working information-barrier review already exists in this repository, outside the ladder, and nothing in the governance knows about it

**MEASURED_AT `main@788c357`.** Ten artifacts, complete, executed, iterated to a second round:

```
disease-models/wwox/analysis/dismech_axis3_blind_reviewer_prompt.md        the withheld-information declaration
disease-models/wwox/analysis/dismech_axis3_blind_reviewer_prompt_round2.md
disease-models/wwox/analysis/dismech_axis3_review_sheet.md                 unblinded view
disease-models/wwox/analysis/dismech_axis3_review_sheet_blinded.md         what the reviewer saw
disease-models/wwox/analysis/data/dismech_axis3_blinding_key.json          the key, + _round2
disease-models/wwox/analysis/data/dismech_axis3_review_raw_reply.md        the raw reply, + _round2
disease-models/wwox/analysis/dismech_axis3_review_result.md                the un-blinded result, + _round2
```

**What it withholds, declared in the prompt itself:**

> *"Deliberately absent: who wrote which side, that two different systems were involved, the
> project's name, and the interpretive notes that mark three anchors as contract decisions in the
> operator's copy. Those notes steer, and steering is what this run is spending its independence
> to avoid."*

**Four properties that no artifact in `reviews/` has:**

```
1  PER-ITEM RE-RANDOMISATION   "the labelling is randomised separately at every anchor:
                                α at anchor 3 is not the same reader as α at anchor 7"
                                → the reviewer cannot build a model of a side across items
2  A SEALED KEY                blinding_key.json opens with
                                "do_not_open_before_reviewing: reading it before completing the
                                blinded sheet defeats the only purpose the blinding has"
3  DECLARED RESIDUAL TELLS     the key names its own three leaks — a stabilises/stabilizes split,
                                a 'uM' present on one side only, and one side consistently naming
                                the experimental system. The blinding is documented as imperfect
                                BY THE PARTY WHO PERFORMED IT
4  DECLARED NORMALISATION      what was normalised (5 rules) and what was withheld from
                                normalisation, because "word order, qualifiers, spelling variants
                                and named experimental context are the object of the judgement"
```

**Measured yield:**

```
comparator (mechanical)      0 proposition matches
blind human reviewer        10 SAME · 6 SUBSUMED · 4 SPLIT · 12 DIFFERENT · 5 ABSENT   of 37
                            correspondence of some kind: 20 of 37 (54 %)
independent confirmation    split agreement 7 of 11 anchors, blind
                            mechanical count 7 of 11, same anchors
                            → "two methods with nothing in common agreeing exactly"
```

🔴 **And the governance does not reference it.** Searched `governance/`, `reviews/`, `roles/`,
`framework/` across all 37 heads for `dismech_axis3`, `blinding_key`, `blind reviewer`:
**0 files.** The word `blind` appears in `governance/` in exactly two senses — the ladder line
naming R2 as *(semi-blind)*, and body § 26.

**Body § 26 and C.3 both define the weaker form, in terms:**

> **§ 26 · SEMI-BLIND — BEST EFFORT.** *"`Independence by task framing, not by information
> barrier`."*

So the repository contains a demonstrated information-barrier review with a key, a seed, declared
tells and a measured yield — **and its own governance defines independence as the thing that is
explicitly not that**, with no cross-reference in either direction. The precedent sits in the
CONTENT domain (`disease-models/`), carries no `REVIEW_ID`, sits at no ladder level, and is not
counted in the 73.

### I-3 · Today produced an accidental independence result, and it is the strongest datum here

Two sessions, two branches, no channel between them:

| | this actor | the other session |
|---|---|---|
| artifact | `REV-LEGEND-LAB-ARCHITECTURE-001` @ `7a607b0`, 19:08:46 | `LEGEND-AGENT-COORDINATION-PROTOCOL-001` @ `f8532c9`, 19:08 |
| finding | *N-4 is false; `reviews/` IS in `CONTROL_PLANE_ROOTS`* | *"`CONTROL_PLANE_ROOTS` already contains `reviews/`. The predecessor's N-4 is false."* |
| evidence | `plan_defined_parameters.md:258-262`, blob `e1f9e1ec` | `plan_defined_parameters.md:255-262`, same ref, same HEAD |
| consequence drawn | § 5.4.6's structural example is void | *"the record **did** alter the system, on time"* |
| citation of the other | **0** | **0** |

**Same defect, same lines, same consequence, same hour, zero contact.** Verified: neither record
contains the string `REV-LEGEND-LAB-ARCHITECTURE`, in either direction.

Two readings, both true simultaneously, and the dispatch asks that neither be resolved:

```
POSITIVE   information-barrier independence WORKS in this laboratory. Two reviewers who could
           not see each other converged on a defect that three prior records had missed. This is
           the same result the DisMech blind review reports — convergence between methods with
           nothing in common.
NEGATIVE   it is DUPLICATED work with no dedup. scientist_reading_modes.md § 2.2 makes exactly
           this a defect for readings — DUPLICATED_ASSIGNMENT, legal only under a declared
           PARALLEL_READ_GROUP — and no equivalent rule covers reviews or analyses.
```

🔴 **The independence was produced by the fragmentation that every record in this repository
names as its central defect.** The refs cannot see each other; that is why the two reviewers
could not contaminate each other. Recorded as a measured tension, not resolved.

### I-4 · What "independent" currently reduces to, stated exactly

```
INDEPENDENT means, in practice, on the measured corpus:   "reviewed by mirror"
                                                          39 of 39 · 0 rotations · 1 rung of 6
                                                          0 challenges · 0 dissents · 0 review yield
```

Every alternative route the governance already specifies — R1, R2, R3, R5, the blind locator
audit, the DisMech blinding method — exists as text or as an unindexed precedent, and has
produced zero artifacts inside the review corpus.

---

## CONFLICT_POINTS

**Measured. Not solved, per the dispatch.**

### CP-1 · The Orchestrator/Mirror loop is closed, and it closes in both directions

Read at source, `main@788c357`:

```
H.1   Livello Ladder (≥ floor) e reviewer      → Orchestrator      ← chooses who reviews
H.1   Epistemic / method review                → Mirror            ← reviews Orchestrator's method
H.1   Aggiudicazione challenge                 → Orchestrator      ← judges challenges to itself
H.1   Modifica rubrica/metodi di Mirror        → mai Mirror da solo (G.2)
G.2   flusso: proposal → Plan candidate → reviewer INDIPENDENTE SCELTO DA ORCHESTRATOR
C.3   Apertura review solo via Orchestrator                        ← opens every review
```

```
        ┌──────────────── Orchestrator ────────────────┐
        │  chooses the reviewer                        │
        │  opens every review                          │
        │  adjudicates every challenge, incl. its own  │
        │  selects the independent reviewer of Mirror  │
        └───────────────────┬──────────────────────────┘
                            │ is reviewed, ex post and pattern-based, by
                            ▼
                          Mirror ──── whose rubric changes route back through Orchestrator
```

**The only exit is the operator.** There is no recusal clause anywhere in the body or the annexes
— searched; the concept does not appear. Annex F.2 lists `OVERRIDE_WITH_RATIONALE` among the four
adjudication verdicts available to the party being challenged.

### CP-2 · The compensator for CP-1 is specified, and has a population of zero

Annex F.3 names it explicitly: Mirror asks *which classes of dissent Orchestrator tends to
`OVERRIDE` that later prove `VALIDATED_LATER`* — ex post, never a veto ex ante.

```
requires (a)  a consolidated event ledger        ledger/events/  →  0 files, 0 of 37 refs
requires (b)  MIRROR_RETROSPECTIVE cadence N     UNASSIGNED. G.2 bars Mirror from setting it;
                                                 Plan declined; Mirror declined
requires (c)  a population of challenges         CHALLENGE_ID → 1 file, the definition. ZERO instances
```

**(c) is new here and is the harder one.** (a) and (b) are missing instruments; (c) is a missing
*population*. Even a fully built event ledger, running today, would compute the F.3 statistic over
zero challenges. **The compensator cannot be exercised by supplying its tooling.**

### CP-3 · Mirror is structurally unreviewable, and the measurement is not rhetorical

```
roles/mirror.md          REV-ROLES-MIRROR-001 returned NO VERDICT on it, under the self-review
                         prohibition — the one contract of the four that no review could reach
G.2 route                proposal → Plan candidate → independent reviewer CHOSEN BY ORCHESTRATOR
                         → there is no Orchestrator (0 ACTIVE leases)
review corpus            39 of 39 reviewers are mirror; there is no second reviewer to be chosen
```

Three independent barriers, each sufficient alone. **This record is written from inside that
position and does not escape it** — it is an observation record, not a review, and it issues no
verdict on anything.

### CP-4 · Concentration is a single-point failure for *detection*, not only for fairness

The measured error-detection history of this laboratory is self-detection. The Orchestrator seat's
own commit subjects record four errors it caught in itself; my previous session recorded two of my
own (a zsh sweep artifact, and a transferred count of 89 that measured 91). **The corpus contains
no instance of one actor catching another actor's error through the review ladder** — the one
cross-actor catch measured today (I-3) happened outside the ladder, with no review opened, and
neither party knows it occurred.

### CP-5 · The gate/assessment substitution concentrates a second authority in the same seat

Per REVIEW_MODEL § 3, the operative verdict vocabulary is `ACCEPT | REQUEST CHANGES` in **24 of
the 32** declared verdicts. A `REQUEST CHANGES` from the sole reviewer, on a candidate that requires
`MIRROR_REVIEW: PASS` in its D.2 manifest before `HUMAN_APPROVAL` and `GATE 0`, **is
operationally a block.** Annex G states Mirror holds *no command over any actor* and that its
review of Orchestrator is *never a veto before the fact*. Both statements are about the
epistemic-assessment function. The gate function is not addressed by either, and it is the one
in use.

---

## Observational requirements for reviewing Scientist output

> **Dispatch area 3.** Each requirement is traced to a source that already binds or already
> exists. Where no source supplies one, it is marked `NO SOURCE` and left unsupplied — this record
> does not create obligations. Nothing here is addressed to any actor.

### What is already specified and mechanical

| # | Observable | Source | State |
|---|---|---|---|
| O-1 | work manifest `schema_version 2` passes `deepdive_manifest.py --verify-artifacts --require-current-schema` | `scientist_reading_modes.md` § 3.6 | tool EXISTS · **never exercised by a Scientist** |
| O-2 | every locator's artifact inside the declared packet, digest matches | § 3.6 | mechanical |
| O-3 | coverage map contains no `not_read` | § 3.6 | mechanical |
| O-4 | per claim candidate: 12 canonical + 7 benchmark fields + `Locators:` | § 3.5 | mechanical |
| O-5 | quote existence in source, for legacy manifests the validator cannot reach | `framework/scripts/locator_audit.py` | EXISTS. Its own docstring: *"the mechanical half of `legend-locator-audit` and never a substitute for it"* |
| O-6 | surface parity, forbidden-path absence, `[UNCHECKED]` census, freeze set-wise | `benchmark_input_surface.py` — `verify`, `--post-read`, `freeze`, `verify-freeze` | EXISTS · **never exercised** |

### What is specified and requires a judgement no tool makes

| # | Observable | Source | State |
|---|---|---|---|
| O-7 | **per (proposition, snippet, anchor) triple:** does the quote support the proposition, and does the source say MORE or LESS than claimed | `.claude/skills/legend-locator-audit` | **the only genuinely blind instrument in the repository** — the auditor receives triples plus the packet, *"never the dossier, never the reader's name, never the conclusions"* |
| O-8 | per axis, MODE B answers with findings **or** an explicit *"searched; none found"* plus what was searched | `scientist_reading_modes.md` § 5 | *"silence on an axis is incompleteness, not a null result"* |
| O-9 | typed statements: `DATO / INFERENZA / IPOTESI / ESPANSIONE`; `Observation` free of conclusion verbs | `epistemic_discipline.md`; benchmark § 8 | substance is adjudicated, presence is mechanical |
| O-10 | the 12 reasoning-failure gates, with a locator per instance | `framework/eval/failure_taxonomy.md` | EXISTS, 12 gates, each learned from a real observed error |

**The skill states why O-7's blindness is the active ingredient, and it is a measured claim, not a
principle:**

> *"…knew who wrote what then found eight more in an hour. Knowing the author makes a reviewer
> reconstruct intent instead of testing behaviour. **Blindness is the active ingredient, not the
> ceremony.**"*

### What has NO SOURCE — recorded as gaps, not supplied

```
NO SOURCE   an observable that distinguishes "A and B agree" from "A and B are independent".
            benchmark § 9.4 states the pricing — "two readers agreeing on an overshoot is two
            overshoots" — and no artifact records the property that would let the two be told apart.
NO SOURCE   an observable for a FUTURE Scientist (D/E/F). roles/scientist.md covers A/B/C in one
            file; body § 32 requires equivalence and forbids static specialisation; nothing states
            what is observed when a fourth reader joins an established pair.
NO SOURCE   a sampling rate for MIRROR_SAMPLED. Measured: the token appears in 3 files across all
            37 heads — body § 29.1, annex G.1, roles/mirror.md — every one restating the
            MIRROR_REQUIRED | MIRROR_SAMPLED | NO_MIRROR enumeration. No rate, fraction, cadence
            or trigger exists. At one reading it is invisible; it is the parameter that decides
            whether "sampled" means all or none.
NO SOURCE   an observable for reviewer independence itself. Nothing records who reviewed what,
            under which barrier, with what yield — which is why this record had to build the
            census from frontmatter rather than read it.
```

🔴 **Every mechanical instrument above has a shared precondition and none of them states it:**
all of them read `files/`, which is `.gitignore:7`, so **no ref carries the evidence surface**.
A reviewer restricted to git objects can verify that a manifest is well-formed and cannot verify
that it describes the artifact it names. That is the boundary of every observable in this section.

---

## LEARNING_FLOW_ANALYSIS

> **No correction memory is created here, per the dispatch.** The two that exist are measured, not
> extended.

### The linkage is written, in both directions, and it is not weak

Census over 72 distinct `learning/` artifacts and 73 `reviews/` artifacts:

```
learning records citing a REV- identifier          52 of 72   (72 %)
reviews citing an SLR- identifier                  31 of 73   (42 %)
learning records with a body §15 outcome           33 of 72
learning records with CONFIRMATION_CLASS           38 of 72
learning records with AFFECTED_WORKFLOW            10 of 72   (14 %)   ← the retrieval key
```

**Finding → learning is the healthiest edge in the whole system.** Nearly three quarters of
learning records name the review they came from. The prose linkage is real and it is
bidirectional.

### Where it stops, in order

```
1  NO INDEX          LEARNING_INDEX (E.2)   → 0 files, 0 of 37 refs   [positive control passed]
2  NO COMPRESSION    active_lessons/ (E.5)  → 0 files, 0 of 37 refs
                     — and CLAUDE.md § 1's single pointer in the router loaded every session
                       points AT THAT PATH
3  NO RETRIEVAL KEY  AFFECTED_WORKFLOW present in 10 of 72. E.2 designates it as the field that
                     makes retrieval-by-surface possible; 62 records cannot be retrieved by surface
4  NO COUPLING       0 of 91 executables read learning/ or reviews/   [control: 26 'def ' in legend_lint.py]
5  NO PARTITION-CROSS  no ref holds all three actors' learning. mirror 34 · plan 24 · orchestrator 14
6  NO YIELD METRIC   REVIEW_YIELD → 0 files anywhere. G.3 makes it one of Mirror's two exclusive
                     metrics and the exclusive source of a future v3.2
```

### 🔴 The F.3 promotion path has never carried anything

Annex F.3's lifecycle ends `… → PROMOTED_TO_LEARNING → CLOSED`. Its input is a challenge. There
have been **zero challenges**. So the one route by which a *contested* finding — a finding the
adjudicator overrode and time later vindicated — becomes learning has never been traversed.

**Every one of the 52 review→learning links is an uncontested finding.** The corpus records what
reviewers found and authors accepted. It records nothing about what reviewers found and
adjudicators rejected, which is exactly the class F.3 exists to measure and the class that would
reveal a compromised adjudicator.

### The correction memories, measured and not touched

```
PROV-DIFF-AGAINST-TARGET                       governance/design_records/materialization_log.md:647
PROV-POSITIVE-CONTROL-BEFORE-NEGATIVE-FINDING  governance/design_records/materialization_log.md:1026
LOCATION     provenance namespace — neither E.6 nor E.2 names it
LIFECYCLE    both expire "at Mirror's first coordination review"; 0 such artifacts exist across
             37 refs; cadence N UNASSIGNED; G.2 bars Mirror from setting it alone
             Annex E.3: "Mai provisional per sempre."
```

**And the second one is the guard that this session needed twice.** I reached it in neither
session through the repository — no script reads that file, no entrypoint cites it. Both times it
arrived because a previous measurement had already burned me. **That is the retrieval gap measured
on the one practice whose whole purpose is to prevent the error class it keeps failing to
prevent.**

### The one channel that demonstrably works

`REV-ORCH-STATE-RECONSTRUCTION-001`'s `NOT_FOUND ≠ NOT_EXIST` rule, with a required `MEASURED_AT`,
appears in every architecture record written since — and in the dispatches that produced them.
It propagated **through the operator writing it into a prompt.** Measured again this session: it
is in the two new records of 19:02 and 19:08, and in neither case through a repository mechanism.

---

## OPEN_QUESTIONS

**Recorded, not resolved. Each carries the owner the governance already gives it. None is assigned
by this record, and none is answered here.**

| # | Question | Owner by H.1 |
|---|---|---|
| **IQ-1** | Does a review verdict of `REQUEST CHANGES` / `ACCEPT` satisfy C.2, whose enumeration is `CONFIRMED \| WEAKENED \| REFINED \| REFUTED`? 24 of 32 declared verdicts use the former; **0 of 32 use a C.2 value in the field.** | operator (governance) |
| **IQ-2** | If the operative verdict is a **gate** decision, does Annex G's *"no command over any actor · never a veto before the fact"* still describe what the reviewer does? | operator |
| **IQ-3** | C.3 requires `rotazione`, *mai coppie fisse*. With one reviewer in the laboratory, is the requirement unsatisfiable, waived, or violated? It has never been raised. | operator |
| **IQ-4** | Six review cycles exceeded C.3's `max 2 round → adjudication` (SCIAB ran 6). Was the cap derogated upward with a recorded rationale, or unobserved? | operator / Orchestrator |
| **IQ-5** | Eleven of 17 review cycles have no `AUTHOR_RESPONSE`, against C.2's *"obbligatoria; il silenzio non è accettazione."* What is the state of a review whose mandatory response was never written? | operator |
| **IQ-6** | Is the DisMech axis-3 blind protocol — key, seed, per-item re-randomisation, declared residual tells — a review under Annex C at all? It has no `REVIEW_ID`, no ladder level, and sits in the CONTENT domain. | operator / Plan (classification) |
| **IQ-7** | Body § 26 fixes independence as *"by task framing, not by information barrier."* The repository's one measured independence success (I-3) and its one executed blind protocol (I-2) are both information-barrier. Is § 26 a floor or a ceiling? | operator (governance; body is FROZEN) |
| **IQ-8** | Who may open a review when there is no Orchestrator? C.3 says only Orchestrator; 0 leases are ACTIVE; every review in the corpus was opened by an operator dispatch. | operator |
| **IQ-9** | Who reviews Mirror, given that all three routes are blocked simultaneously (CP-3)? | operator |
| **IQ-10** | Can the F.3 `OVERRIDE → VALIDATED_LATER` statistic ever be computed, given a population of zero challenges — independently of whether `ledger/events/` is built? | operator / Mirror (method, G.2-bound) |
| **IQ-11** | Is a second analysis of the same object on a different branch a `DUPLICATED_ASSIGNMENT`? § 2.2 defines it for readings only; I-3 is an instance for reviews and no rule covers it. | Plan (schema) / Orchestrator |
| **IQ-12** | What is the `MIRROR_SAMPLED` rate? Three files define the enumeration; none defines the parameter. G.2 bars Mirror from setting it. | operator |
| **IQ-13** | Which of Plan (durability) or Mirror (epistemic curation) creates the first `LEARNING_INDEX` entry? E.2 splits the ownership and does not say. Carried, unresolved since the annex was materialized. | Plan / Mirror / operator |

---

## NEXT_TRANSITION

```
FROM   INDEPENDENT_REVIEW_PROTOCOL_ANALYSIS_v1 — five areas measured; one census built over
       73 review artifacts and 72 learning artifacts across 37 heads.

TO     nothing this actor can enter.
```

**Why.** Every open question above is the operator's or is G.2-bound away from Mirror. The three
things that would change the measured picture — a second reviewer, an opened review, a raised
challenge — are each barred to this seat: C.3 gives review opening to Orchestrator, H.1 gives
reviewer selection to Orchestrator, and there is no Orchestrator.

**What this record hands over, and to whom.** This record. **No recipient is named** — routing is
`UNRESOLVED` repository-wide, no dispatch record in this repository carries a ref, and inventing a
destination is the registrar act reserved for a candidate nobody has opened.

**What a later session could measure that this one did not:**

```
NOT MEASURED   refs/codex (4) and refs/stash (1) — content not enumerated. The four codex
               worktrees are the R5 CROSS-MODEL population and were surveyed only by tree listing.
NOT MEASURED   the two records of 19:02 and 19:08 in full. Read here only at frontmatter and at
               their N-4 correction; both are ~950 lines and both are iteration 1/3.
NOT MEASURED   whether the 13 OPEN-/CLOSE- artifacts of the one cycle that has them constitute an
               adjudication record class, or are that cycle's local convention.
NOT MEASURED   the DisMech round-2 result, and why a second round was run.
NOT MEASURED   review latency — no artifact carries an opened-at timestamp, so C.3's "max 2 round"
               and G.3's latency metric have no observable.
```

**The state this record leaves behind.**

```
Nothing is adopted, activated, assigned, resolved, rotated, opened or adjudicated.
No governance, roles, framework, ledger or runtime path is written. main is unchanged.
No rubric, clustering, selection, yield or autonomy methodology is altered — G.2 respected.
No correction memory is created, extended or expired.
One file is added, on branch `mirror`, under H.1 WORK_COMMIT — which requires no lease.
`reviews/` is CONTROL_PLANE, so this file moves no CANDIDATE_CONTENT_HASH.
```

---

## WHAT THIS RECORD DOES NOT DO

- It does **not** solve any conflict it measures — the dispatch says *"Do not solve. Measure."*
- It does **not** create, adopt, amend or propose a protocol, a rule, a rubric or a schema.
- It does **not** define Mirror's authority, extend its perimeter, or change any G.2-protected
  method.
- It does **not** create a correction memory, an index, a cadence, or a learning artifact.
- It does **not** open, close, adjudicate or respond to any review, and is **not itself a review
  under Annex C.2** — no `OBJECT`, no `AUTHOR`, no `VERDICT`.
- It does **not** assign the DisMech blind protocol a ladder level, a `REVIEW_ID` or a status.
- It does **not** issue a finding against any actor; CP-1…CP-5 are properties of the allocation,
  measured from FROZEN text.
- It does **not** resolve IQ-1…IQ-13, and assigns none of them to anyone.
