---
artifact: MIRROR analysis record — how Mirror may evaluate the scientific reasoning of a Scientist,
  derived from authority that already exists. Learning artefact only
record_id: EPISTEMIC_REVIEW_MODEL-001
actor_id: mirror
date: 2026-08-22
task_id: MIRROR_EPISTEMIC_REVIEW_MODEL_v1
dispatcher: operator
role: >
  mirror — metacognitive layer (roles/mirror.md, "Mandate — three layers"). The hostile review
  layer is described here and is NOT exercised: this record reviews no object, names no author,
  and issues no verdict on anything any actor has produced
authority: >
  🔴 NONE, AND THE DECLARATION IS LOAD-BEARING. Annex G.2 bars Mirror from self-approving material
  changes to its own review rubric. A review model IS a rubric object. Nothing below is adopted,
  binding, or in force. Every element is either (a) traced to a normative source that already
  binds, or (b) marked PROPOSED and routed — MIRROR_UPGRADE_PROPOSAL → Plan candidate →
  independent reviewer chosen by Orchestrator → validation; operator if it touches governance
classification: OBSERVATION AND ANALYSIS — not governance, not a protocol, not a validator,
  not an amendment, not a decision
scope: >
  learning/mirror/ on branch `mirror` only. One new file. No governance/, roles/, framework/,
  ledger/ or reviews/ path is written. No existing record is edited, superseded or deprecated
confirmation_class: >
  UNASSIGNABLE BY THE PRESCRIBED PROCEDURE. Annex E.2 requires the LEARNING_INDEX be consulted
  before a class is assigned; it does not exist (0 objects, 52 refs, MEASURED_AT mirror@f8db068).
  Dedup was performed instead by enumerating the ref-tip path union — see § SURFACE_MAP. The
  finding at REVIEW_MODEL § R-1 would read ORIGINAL_OBSERVATION on that substitute basis;
  LEARNING_LOOP § L-4 would read REPLICATION of [[SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001]]
  § 3.5. Recorded as a description of what was done, not as a class assigned by the procedure
prior_artefact_disclosure: >
  🔴 MATERIAL, DECLARED FIRST. Two Mirror records written on this same date already cover part of
  this ground, both found by listing a directory rather than reported to me:
  reviews/mirror/ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001.md (667 lines — its "Observational
  requirements for reviewing Scientist output" § and its INDEPENDENCE_ANALYSIS §), and
  learning/mirror/SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001.md (748 lines — its § 3.5, § 5).
  This record does NOT supersede, amend or replace either. Overlap is mapped at § SURFACE_MAP.
  What is materially NEW is: REVIEW_MODEL § R-1 (the object boundary, resolved against C.4 and
  scientist_reading_modes § 5.4), EPISTEMIC_CRITERIA (the six dispatch checks mapped to existing
  owners, plus CRIT-7), and LEARNING_LOOP § L-4 (the science-side retrieval channel, measured —
  a surface none of the four in the prior census covered)
naming_deviation: >
  DECLARED. 29 of the 34 records under learning/mirror/ match `SLR-mirror-NNNN[-ADD|-COR-NNN]`;
  5 do not, each having declared its own departure. This filename was specified by the dispatch
  and departs likewise. NO NAMING RULE IS ADOPTED AND NO PRECEDENT IS ESTABLISHED
measured_at: >
  mirror@f8db0688ad00758ab77c9d9ad43656fd932e2456 · main@788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
  · 52 refs · 755 distinct paths in the ref-tip union · 2026-08-22T17:36Z–17:39Z.
  Every count below was re-run in this session. Where a number is inherited from another record
  it is attributed and marked INHERITED
---

# EPISTEMIC REVIEW MODEL — what Mirror may ask of a Scientist's reasoning, and what it may not

> **Mirror does not decide the truth. Mirror evaluates the quality of the reasoning process.**
> The dispatch closes with that sentence. This record takes it literally, and the literal reading
> turns out to be a *constraint* rather than a slogan: the governance already assigns the truth
> question to someone else, by name, in two places. § REVIEW_MODEL is mostly the consequence.

---

## TASK_STATUS

```
TASK          MIRROR_EPISTEMIC_REVIEW_MODEL_v1
DISPATCHER    operator (no ACTIVE lease exists — see IDENTITY)
STATE         COMPLETE for the analysis; NOTHING ADOPTED
DELIVERABLE   learning/mirror/EPISTEMIC_REVIEW_MODEL-001.md — this file, on branch `mirror`
PERSISTENCE   WORK_COMMIT on `mirror` (body §11, §18). Not a candidate. Not for canonical history

CONSTRAINTS HONOURED, EACH CHECKABLE
  no governance created      0 paths written under governance/
  no validator created       0 paths written under framework/ or scripts/
  no framework modified      0 paths written under framework/
  own branch only            1 path written, under learning/mirror/
  authority derived only     from H.1 (row "Epistemic / method review → Mirror") and Annex G.
                             roles/mirror.md is status: PROPOSED and is CITED FOR ITS CONTENT,
                             never invoked as a source of authority — see IDENTITY
```

---

## IDENTITY

### What I am, derived rather than assumed

```
ACTOR_ID              mirror
BRANCH / WORKTREE     mirror  (f8db068) — one writer, body §14
GOVERNANCE_VERSION    3.1.1
AUTHORITY SOURCE      Annex H.1 · Annex G (G.1 perimeter, G.2 self-upgrade bar, G.3 metrics)
                      Annex C (review protocol) · Annex E (learning lifecycle) · Annex F · J.1
ROLE CONTRACT         roles/mirror.md — `status: PROPOSED — binding once Mirror hostile review
                      passes and the operator approves`.
                      🔴 NOT USED AS AUTHORITY. Where this record cites it, it cites descriptive
                      content whose normative twin is in the body or an annex, and the twin is
                      named beside it
```

### The lease, derived and not read

The bootstrap rule in `CLAUDE.md` § 0 turns on whether an `ACTIVE` `ORCHESTRATOR_LEASE` exists.
`runtime/orchestrator_lease.md` is **absent on this ref** and present on 14 others. Its own
frontmatter says the stored `STATUS` field is never authoritative. So the state was **derived**,
this session, by running `framework/scripts/lease_state.py` from `main` against `main`'s record:

```
now (derivation instant)  2026-08-22T17:39:01Z
  lease #1  derived=STALE     stored=STALE
  lease #2  derived=RELEASED  stored=RELEASED
  lease #3  derived=STALE     stored=EXPIRED     ← DISAGREEMENT, reported by the tool
  lease #4  derived=RELEASED  stored=RELEASED
  lease #5  derived=RELEASED  stored=RELEASED
ACTIVE by derivation: 0
```

**There is no Orchestrator.** Three consequences bind this record and are not rhetorical:

1. Annex C.3 — *"apertura solo via Orchestrator"* — cannot be satisfied by anyone right now.
   This record therefore opens no review and describes what a review would be.
2. H.1 gives *"Livello Ladder (≥ floor) e reviewer"* to Orchestrator. I cannot set a level for
   any future review of a Scientist, and do not.
3. H.1 gives challenge adjudication to Orchestrator. A Mirror verdict that behaved like an
   adjudication would be filling a **vacancy**, not a seat. § INDEPENDENCE_MODEL § IND-3.

### Session preconditions, run not assumed

```
framework/state/state_manifest_current.md   current_state: READY      (line 141)
python3 framework/scripts/legend_lint.py .  VERDICT: PASS
                                            1 [INFO] MISSING_WIKILINK, CLAIM 010, non-blocking
```

---

## SURFACE_MAP

### What was read, and at which ref

| Surface | Path | Ref | Role in this record |
|---|---|---|---|
| Authority matrix | `governance/annex_h_authority_matrix.md` § H.1 | mirror | the only authority claimed |
| Mirror annex | `governance/annex_g_mirror.md` § G.1–G.3 | mirror | perimeter, self-upgrade bar, metrics |
| Review protocol | `governance/annex_c_review_protocol.md` § C.1–C.4 | mirror | ladder, format, **§ C.4 the object boundary** |
| Learning lifecycle | `governance/annex_e_learning_lifecycle.md` § E.1–E.6 | mirror | the loop's declared stages |
| Challenge / dissent | `governance/annex_f_challenge_dissent.md` § F.1–F.4 | mirror | the contested-finding route |
| Body | `governance/GOVERNANCE_v3.1.1.md` §§ 11, 12, 14–19, 23–29, 32, 40, 46 | mirror | §23 duplicates C.4; §16 the two pipelines |
| Runtime control plane | `governance/annex_j_runtime_control_plane.md` § J.0–J.1 | mirror | guarantees NOT possessed; the ledger |
| Epistemic discipline | `framework/instruction/epistemic_discipline.md` | mirror | the four levels; premises and negatives |
| Parity of sources | `framework/master/gold_is_in_the_details.md` rules 1–8, 5b–5e | mirror | what counts as having read |
| Failure taxonomy | `framework/eval/failure_taxonomy.md` | mirror | **12** reasoning-failure gates |
| Learned gates | `framework/eval/learned_gates_registry.md` | mirror | **79** rows · 21 ACTIVE_EXECUTABLE |
| Failure-aware eval | `framework/eval/README.md` | mirror | the 10 metrics; the T0→T1 temporal test |
| Self-evaluation | `framework/protocols/session_self_evaluation.md` | mirror | Part 1 executable / **Part 2 judgement** |
| Reading modes | `framework/protocols/scientist_reading_modes.md` | 🔴 **main** | **§ 3.8 acceptance test · § 5.2 axes · § 5.4** |
| Scientist contract | `roles/scientist.md` (`status: PROPOSED`) | mirror | content only, never authority |

🔴 **`scientist_reading_modes.md` is not on this ref.** Present on 14 refs including `main`;
absent on `mirror`. It is the protocol that defines what a Scientist *produces* — the object this
whole record is about — and Mirror's own working ref does not carry it. Recorded at
§ BLOCKERS B-2, not repaired here.

### The population Mirror would be reviewing, measured

```
DEEP-DIVE MANIFESTS      64 files at disease-models/wwox/research/deepdive_manifests/
                         schema_version 2 in 60 · 🔴 ABSENT in 4 (PMID22193544, 34214506,
                         35716775, 40875931) — the legacy class locator_audit.py exists for
                         63 carry locator entries · 1 declares waived: true
VERBATIM LOCATORS        1002 (proposition · snippet · surface · artifact · anchor) triples
                         by surface: body 617 · figure 338 · undeclared 33 · table 13 · supplement 1
                         🔴 the 33 undeclared-surface locators are EXACTLY the 33 held by the 4
                         legacy manifests — 0 in any schema-v2 manifest. None of the 33 declares
                         an artifact, so no per-locator artifact check has ever reached them
REVIEWS                  52 files at reviews/mirror/ on this ref
                         reviewer: declared in 36 → mirror 36 / 36 = 100%
                         level:    declared in 31 → R4 in 31 / 31 = 100%
                         verdict:  declared in 33 → 17 REQUEST CHANGES · 7 ACCEPT · 9 prose
                                   🔴 0 use a C.2 value (CONFIRMED | WEAKENED | REFINED | REFUTED)
                                   POSITIVE CONTROL: the four words appear in the BODY of 29 of
                                   the 52 files. The instrument was working — they are discussed
                                   and never declared
LEARNING RECORDS         learning/mirror 34 · learning/plan 25 · learning/orchestrator 15
                         (union over 52 refs)
🔴 SCIENTIST OUTPUT      0 records authored by any scientist, in learning/ or reviews/, on any
                         of the 52 refs. Positive control: the string `scientist` resolves to 11
                         paths — contracts, specs, benchmark assignments, one working handoff —
                         and to no authored learning or review record. The instrument was working
```

The reviewer/level/verdict figures reproduce, on this branch and by my own run,
what `reviews/mirror/ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001.md` § 1–3 measured across 73
artifacts on a wider surface. Re-measured rather than cited, per that record's own method.

### Overlap with the two prior records, mapped rather than hidden

| This record | Prior coverage | Relation |
|---|---|---|
| SURFACE_MAP census | ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001 § 1–3 | **RE-MEASURED**, narrower surface (this branch), same result |
| REVIEW_MODEL § R-2/R-3 owners | same record, "Observational requirements" O-1…O-10 | **BUILDS ON.** That record listed observables; this one assigns them to review *types* and to owners |
| REVIEW_MODEL § R-1 object boundary | — | **NEW.** Neither prior record resolves C.4 against `scientist_reading_modes.md` § 5.4 |
| EPISTEMIC_CRITERIA | — | **NEW.** The dispatch's six checks had not been mapped to existing owners |
| INDEPENDENCE_MODEL | ANALYSIS… § INDEPENDENCE_ANALYSIS I-1…I-4, CP-1…CP-5 | **BUILDS ON**, restated against the three failure modes the dispatch names |
| LEARNING_LOOP § L-1…L-3 | SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001 § 3, § 5 | **INHERITED**, attributed inline, not re-derived |
| LEARNING_LOOP § L-4 | — | **NEW.** The science-side channel is outside all four surfaces that record measured |

---

## REVIEW_MODEL

### R-1 · Which of the three review types belongs to Mirror — and the answer is *none of them, at first order*

The dispatch separates three review types and asks which is Mirror's. The governance answers in
one line, stated twice, identically:

> **Annex C.4 · Tre oggetti** — `EVIDENCE → Scientist + Plan/provenance · INFERENCE → peer
> Scientist · SYSTEM → Mirror`. (Body § 23 repeats it verbatim.)

And the reading protocol draws the same boundary from the other side, in a section written to
prevent exactly this confusion:

> **`scientist_reading_modes.md` § 5.4 · 🔴 MODE B is not Mirror.**
> Object — MODE B: *"the **paper** — its evidence and its inferences"*. Mirror: *"the **process**
> — how the laboratory reasoned, reviewed and recorded"*.

Mapped onto the dispatch's three types:

| Dispatch type | Object | Owner by C.4 / § 5.4 | Instrument that exists | Mirror's relation |
|---|---|---|---|---|
| **A · Artifact review** — format, completeness, compliance | the artefact | validators; `NO_MIRROR` is defined by G.1 as *"routine coperta da validator"* | `deepdive_manifest.py --verify-artifacts --require-current-schema` · `session_self_eval.py` · `legend_lint.py` · `fulltext_receipts.py verify` · `locator_audit.py` | 🔴 **NOT MIRROR'S.** G.1 names this class as the one Mirror stays out of |
| **B · Scientific reasoning review** — inference quality, observation-vs-hypothesis, evidence strength | the **paper** and the reading of it | `INFERENCE → peer Scientist` (C.4). MODE B searches 11 mandatory critical axes on the paper itself | `scientist_reading_modes.md` § 5.2; peer review at C.1 floors R1/R2 | ⚠️ **NOT MIRROR'S AT FIRST ORDER.** Mirror reaches it only at the R4 floor — *"processo inferenziale methodology-changing"* — or under `MIRROR_SAMPLED` |
| **C · Claim review** — single claims, locators, support | the (proposition, snippet, anchor) triple | mechanical: `locator_audit.py`. Judgement: the **blind** auditor of `.claude/skills/legend-locator-audit` | both exist | 🔴 **NOT MIRROR'S, AND STRUCTURALLY CANNOT BE.** The skill's active ingredient is blindness; Mirror sees author, dossier and conclusions by construction. § IND-1 |

🔴 **So the model's first result is subtractive, and it is the finding of this record.** A review
in which Mirror answers *"is this claim well supported?"* would place Mirror in a seat the
annexes give to a Scientist — on a branch where **one actor already holds 36 of 36 declared
reviewer positions across every review ever written**. The dispatch's own closing sentence is the
correct constraint, and it is narrower than it sounds.

### R-2 · What Mirror's object actually is — the fourth thing

`SYSTEM` in C.4 is not a residue. It is the review apparatus itself. Mirror's question is
second-order and can be stated in one line:

> **Not** *"is this conclusion right?"*
> **but** *"did the process that produced this conclusion have a way of being wrong, and did it
> use it?"*

That distinction is not invented here. It is the design principle of
`framework/protocols/session_self_evaluation.md`, which exists because of a session that passed
every check and was wrong in four ways, and which states the reason:

> *"**self-assessment written by the same agent that did the work is not evidence.** The session
> graded itself green while all four held."*

The self-evaluation's Part 2 is 27 judgement questions the Scientist answers **about itself**.
That is precisely the artefact whose author cannot certify it. **Mirror's object is the answer,
not the paper** — and reviewing an answer is a review of process, which is C.4's `SYSTEM`.

### R-3 · The input → verdict → learning chain, with each stage's existing owner

```
INPUT      the frozen output tree of a completed reading:
             · work manifest (schema_version 2)          — provenance
             · dossier with verbatim locators            — locator fidelity
             · claim candidates, NOT written to registry — claim assertion
             · MODE B critical-reading record            — one entry per axis finding
             · the Part 2 self-evaluation answers        — the reasoning account
             · the validator verdict lines from § 3.8 steps 1–4
             · the blind locator audit output, if one was run
   ↓
ANALYSIS   Mirror compares the ACCOUNT against the ARTEFACTS, at three seams:
             S-1  did every instrument that should have run, run — and at which floor
             S-2  where an axis, a gate or a premise was declared searched, is the search
                  visible as an artefact, or only as a claim to have searched
             S-3  where the account and the artefacts disagree, which is load-bearing
   ↓
FINDING    one per seam, anchored to a repository object, typed like everything else
   ↓
VERDICT    Annex C.2, four values, over a PROPOSITION ABOUT THE PROCESS — see R-4
   ↓
LEARNING   Annex E.6 record; body §15 outcome; E.2 confirmation class → § LEARNING_LOOP
```

Every stage above already has a named home. **Nothing in this chain is a new component.**

### R-4 · The C.2 verdict vocabulary, applied to a process object

C.2 fixes four values and defines the first one narrowly:

```
CONFIRMED   "nessun difetto rilevato dato l'evidence bundle disponibile", esplicitamente NON "vero"
WEAKENED    the object survives, with less support than claimed
REFINED     the object survives, reformulated (+ REFINED_FORMULATION, mandatory)
REFUTED     the object does not survive
```

Two observations, one inherited and one new.

**INHERITED** (ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001 § 3, re-measured by me on this branch):
of **33** reviews declaring a `verdict:` field, **0 declare a C.2 value** — 17 read
`REQUEST CHANGES`, 7 read `ACCEPT`, 9 are prose. Those first two are a **gate** vocabulary —
binary, blocking, about the artefact — and C.2's four are an **epistemic** vocabulary about a
claim's support. The substitution has already run for 33 reviews on control-plane objects, and
the four C.2 words appear in the bodies of 29 files, so this is not a vocabulary anyone forgot.

**NEW, and the reason this matters more for scientific objects than it did for governance ones:**
when the reviewed object is a governance candidate, a gate verdict is at least *about* the right
thing — the candidate either proceeds or does not. When the reviewed object is a **reading**, a
gate verdict answers *"may this reading proceed?"*, which is a question C.4 does not give Mirror,
and it answers it in language that reads like an epistemic assessment of the science. The
substitution would convert Mirror from an assessor of process into a **gatekeeper of scientific
output**, silently, in a laboratory where no second reviewer exists to notice.

`PROPOSED — NOT ADOPTED, routes through G.2:` a Mirror review of a Scientist's reasoning declares
its `OBJECT` as a proposition **about the process** (e.g. *"the ALTERNATIVE_EXPLANATION axis was
searched and the search is visible in the critical-reading record"*), never as the scientific
claim; and where a gate decision is also owed, it is carried in a **separate field with a
separate name**, so that a reader can tell an assessment from a release. Mirror may not adopt
this. It is a rubric change under G.2.

### R-5 · When Mirror looks at a reading at all — and the parameter that decides it does not exist

```
MIRROR_REQUIRED   MAJOR · protocols/governance · R4 · repeated dissent · recurring failures
MIRROR_SAMPLED    ordinary batches, audit a campione
NO_MIRROR         routine already covered by a validator
```

An ordinary reading is not MAJOR, is not governance, and is not a recurring failure. It falls
under `MIRROR_SAMPLED`. Re-measured this session: the token `MIRROR_SAMPLED` occurs in **3
normative files** on this ref — `annex_g_mirror.md:21`, `GOVERNANCE_v3.1.1.md:341`,
`roles/mirror.md:43` — each restating the same three-value enumeration. **No rate, fraction,
cadence or trigger exists anywhere.** At one reading the parameter is invisible; it is the one
that decides whether *sampled* means **all** or **none**. G.2 bars Mirror from setting it.
§ BLOCKERS B-4; carried as an open question by IQ-12 of the prior record and not answered here.

---

## EPISTEMIC_CRITERIA

> **How to tell a good scientific answer from a plausible but epistemically weak one.**
> The dispatch lists six checks. Every one of them already has a name in this repository, an
> owner, and an instrument — and in five of six cases the owner is not Mirror. What follows maps
> each to what exists, then states the **second-order** question that is Mirror's and no one
> else's. Nothing here is a new criterion.

### The mapping

| # | Dispatch check | Existing name(s) in this repository | First-order owner | Instrument state | **Mirror's second-order question** |
|---|---|---|---|---|---|
| **CRIT-1** | hallucination | no repository term. Nearest: quote existence; `SOURCE_INTEGRITY` (failure_taxonomy); rule **5c** — a quote checked against an ML reconstruction *"can pass while matching the reconstruction and not the paper"* | `locator_audit.py`; the blind auditor | EXISTS. `locator_audit.py` docstring: *"the mechanical half of `legend-locator-audit` and never a substitute for it"* | Was the surface the quote was matched against **deterministically extracted, and is the method declared**? 5c names this the worst false positive the system can produce, *"because it is silent and wears the badge of having been checked"* |
| **CRIT-2** | overclaim | `OVERCLAIM` axis (reading modes § 5.2); the blind audit's second question — *does the source say MORE or LESS than the proposition claims*; `LOCATOR_OVERSHOOT_GATE` | MODE B reader; then the **blind** auditor | Both exist. 🔴 **0 blind locator-audit verdict artefacts in the 52-ref union.** The `*_locators.md` dossiers are captures, and `locator_contract_live_test.md` tests the capture contract — neither is an audit. The one blind protocol that did execute is DisMech axis-3 (8 paths), a different protocol, outside the ladder — § IND-1 | Did the blind audit **run**, over which triples, and who chose the subset? Mirror verifies the instrument ran; it does not become the instrument |
| **CRIT-3** | evidence gap | `NEGATIVE_EVIDENCE` and `OMISSION` axes; `UNREAD_PREMISE` ratchet; reading debt (rule 6); `[DECLARED GAP]` lines | MODE B reader; `session_self_eval.py` | EXISTS and executable. `UNREAD_PREMISE` is a **ratchet** against a baseline — *"the count may fall, never rise"* | Is the gap **declared or silent**, and is the ratchet moving? A declared debt is *"legitimate work in progress; silence is not"* |
| **CRIT-4** | causality / correlation confusion | `DEGRADATION_DIRECTION_GATE` · `MECHANISM_DIRECTNESS_GATE` · `KG_EDGE_HAS_NO_SIGN` · `TARGET_ATTRIBUTION_GATE`; axis `UNSUPPORTED_MECHANISTIC_LEAP` | MODE B reader, against `failure_taxonomy.md` | EXISTS — 12 gates, each *"learned from a real, observed error"* | Was the applicable gate **named in the manifest**, or applied silently? Measured: **5 gate citations across 64 manifests; 4 manifests of 64 cite any; 5 distinct gates of 79** |
| **CRIT-5** | missing alternative explanation | `ALTERNATIVE_EXPLANATION` axis; C.2's own `ALTERNATIVES_CONSIDERED` field | MODE B reader | EXISTS, with an explicit anti-silence rule | § 5.2: *"silence on an axis is incompleteness, not a null result."* Did the axis carry findings **or** an explicit *"searched; none found"* **plus what was searched**? A bare absence is the failure, not the finding |
| **CRIT-6** | cherry picking | `gold_is_in_the_details` rules 1–3 — *"no tier, score, or category authorizes NOT reading"*; `READING_DEBT_FALSE_NEGATIVE` gate; coverage map with no `not_read`; `unread_gold.py` | Scientist; `fulltext_receipts.py`; `session_self_eval.py` | EXISTS and executable | Self-eval Q19: *"Where the ranking and my judgement diverged, did I record the divergence? **A ranking that is never contradicted is not being used.**"* Mirror's question is about the divergence record, not about the ranking |

### A measured instance of CRIT-1, found while checking my own clause

I asserted, and then re-measured, that all 64 manifests carry `schema_version 2`. Four do not.
The consequence is not bookkeeping:

```
LEGACY MANIFESTS   4 of 64 declare no schema_version
LOCATORS IN THEM   33 — and 0 of the 33 declares an `artifact`
CROSS-CHECK        the 33 locators lacking a declared `surface` are EXACTLY these 33;
                   schema-v2 manifests contribute 0
CONSEQUENCE        deepdive_manifest.py --verify-artifacts can only match a locator against
                   its declared artifact, so these 33 quotes have never been matched against
                   anything by that route. locator_audit.py exists precisely for them, and its
                   own docstring records what such an audit found the last time it ran:
                   "PMID 32000863 had five locators out of twenty-two that did not occur in its
                   own XML […] transcribed as the page reads rather than extracted as the
                   artifact contains"
```

This is what a second-order question looks like when it lands. Mirror did not adjudicate a single
quote. It asked which population an instrument's `PASS` actually covers, and the answer named 33
triples that sit outside it. The finding is about coverage, not about truth — which is the whole
distinction § R-1 draws.

### CRIT-7 · The class the dispatch does not list, and the repository calls the most dangerous

All six checks above concern what a reading **asserted**. `epistemic_discipline.md` § 2 states
that the greater danger runs the other way, and states why the asymmetry is not intuitive:

> *"a **false positive** gets tested and dies. A **false negative** is **silent, permanent, and
> self-reinforcing** — once discarded, nobody looks at it again. […] a false positive is a cost;
> **a false negative is a compounding loss.** And tiers, gates, filters, `refuted`, "do not assume
> that…" are *all machinery that produces negatives*."*

`failure_taxonomy.md` calls it *"the keystone: the permanent false negative."* Its three binding
obligations — `PREMISE_TAG`, `REVIVAL_TRIGGER`, the re-audit rule — are the only part of the
epistemic discipline with executable coverage, and the coverage is thin and non-blocking.
Measured this session in `framework/scripts/legend_lint.py`:

```
DISMISSAL_WITHOUT_PREMISE     WARN_BUT_PROCEED   fires on a DIS-### block with no tagged PREMISE
DEFAULT_PREMISE_NO_TRIGGER    WARN_BUT_PROCEED   fires on PREMISE: DEFAULT_FROM_TEXTBOOK with
                                                 no REVIVAL_TRIGGER
SCOPE                         only DIS-### blocks in the dismissal ledger
NOT CHECKED BY ANY TOOL       whether the premise is CORRECT · whether the revival trigger is
                              ADEQUATE · whether the re-audit rule ran when a new mechanistic
                              DATO arrived
```

**Mirror's second-order question, and the one place where the process question and the truth
question genuinely coincide:** the re-audit rule — *"every time a new mechanistic `DATO` arrives,
re-scan the dismissal ledger for rejections whose premise that datum touches"* — is a **process
obligation with no instrument**. `framework/eval/README.md` designs the T0→T1 temporal test to
measure exactly it. Whether a reading triggered a re-audit is answerable from artefacts alone,
without adjudicating any science. It is recorded here as the criterion Mirror is best placed to
carry and least equipped to run.

### What this list is not

`PROPOSED — NOT ADOPTED.` These seven are **not a rubric**. They are a map of criteria that
already bind, showing where each is owned. Turning them into a scored rubric would be a material
change to Mirror's review rubric and is barred to Mirror by G.2 and by H.1's row *"Modifica
rubrica/metodi di Mirror → mai Mirror da solo"*.

---

## INDEPENDENCE_MODEL

> The dispatch names three ways Mirror could fail. Each is answered from measurement, and each
> already has a compensator somewhere in the governance — in two of three cases a compensator
> that has never run.

### IND-1 · Mirror being influenced by the Scientists

**The measured claim, not the principle.** `.claude/skills/legend-locator-audit` states its own
active ingredient:

> *"…knew who wrote what then found eight more in an hour. Knowing the author makes a reviewer
> reconstruct intent instead of testing behaviour. **Blindness is the active ingredient, not the
> ceremony.**"*

🔴 **Mirror cannot be that instrument, structurally.** The blind auditor receives triples plus the
source packet — *"never the dossier, never the reader's name, never the conclusions"*. Mirror's
object is the process: it must see the author, the account, the conclusions and the review
history to have an object at all. **Blindness and Mirror's mandate are mutually exclusive.**

What follows is not that Mirror is compromised, but that Mirror's independence has to come from
somewhere else, and the repository shows exactly where — and that it is not where the governance
looks:

```
BODY § 26     "SEMI-BLIND — BEST EFFORT.  Independence by task framing, not by information barrier"
              → the governance defines independence as explicitly NOT an information barrier

MEASURED      the one blind protocol this repository has EXECUTED — per-item re-randomisation,
              a sealed key, declared residual tells, a measured yield — sits at
              disease-models/wwox/analysis/dismech_axis3_* and carries NO REVIEW_ID and NO ladder
              level. governance/, reviews/, roles/ and framework/ reference it 0 times
              (INHERITED: ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001 § I-2)

MEASURED      reviewer: mirror in 36 of 36 · level: R4 in 30 of 30 · 0 rotations, ever.
              C.3 requires "rotazione; mai coppie fisse". With one reviewer the constraint is
              satisfied and buys nothing
```

**The model that follows:** Mirror's independence from a Scientist is *positional*, not
informational — it comes from reviewing a **different object** (the process) than the one the
Scientist argued about (the paper). The moment Mirror starts assessing whether a claim is true,
it loses the only independence it actually has, because it is then arguing about the same object
with more context than any blind reviewer and less evidence than the reader.

### IND-2 · Mirror degenerating into an automatic validator

The guard exists, is named, and has never been computed.

```
G.1   NO_MIRROR = "routine coperta da validator".  A Mirror review that re-runs what
      deepdive_manifest.py or legend_lint.py already checks is, by definition, outside the perimeter

G.3   REVIEW YIELD: per Ladder level; "yield nullo persistente → rituale → declassare"
      🔴 MEASURED: REVIEW_YIELD — 0 files, 52 refs. The metric that detects ritual review has
         never been computed, and G.3 makes it one of Mirror's two exclusive metrics AND
         "la fonte esclusiva della futura v3.2"
```

**The operative rule is already written and needs no addition:** if Mirror's finding on a class
of readings would have been produced by a validator that already runs, the correct outcome is
`NO_MIRROR` for that class — not a review that agrees with the tool. The measurement that would
show this is happening is review yield, and it is unbuilt. § BLOCKERS B-7.

### IND-3 · Mirror substituting for human adjudication

Three separate bars, all textual, none enforced at runtime (J.0: *"RBAC enforced a runtime
(attori interattivi)"* is a guarantee this system does **not** possess; the compensator is
*"authority matrix testuale + audit + event ledger"*, and the event ledger has 0 objects):

```
H.1   Aggiudicazione challenge            → Orchestrator (con rationale)
H.1   Spese / MAJOR approval / governance → Operatore
G / roles  Mirror holds no command over any actor, produces no primary evidence,
           and its review of Orchestrator is "ex post and pattern-based — never a veto before the fact"
```

🔴 **And the vacancy makes the risk concrete rather than theoretical.** Derived this session:
`ACTIVE by derivation: 0`. There is no Orchestrator to adjudicate. Every review in the corpus was
opened by an operator dispatch. In that configuration a Mirror verdict that carries a gate
decision does not *substitute* for an adjudicator — it **occupies an empty chair**, which is
harder to see and harder to undo. This is the same seam R-4 reaches from the vocabulary side, and
it is why the two-field separation there is the specific compensator for this failure mode.

### IND-4 · What independence currently reduces to, stated exactly

```
INDEPENDENT means, on the measured corpus:   "reviewed by mirror"
                                             36 of 36 declared reviewers · 0 rotations
                                             1 ladder rung of 6 · 0 challenges · 0 dissents
                                             0 review-yield computations
```

R1 peer review, R2 semi-blind, R3 triadic and R5 cross-model exist as text and have produced
nothing. **A model for reviewing Scientist reasoning that routes everything to Mirror would
therefore not be a design choice — it would be the continuation of a measured single point of
failure.** The subtractive result at R-1 is the mitigation, and it is the only one available
without creating something, which this record may not do.

---

## LEARNING_LOOP

> **How a negative review becomes a future improvement.** Body § 16 makes this one of two
> pipelines and calls the second *"prodotto fondamentale"*:
> `experience → review → learning con lifecycle → cross-agent evaluation → validated practice →
> protocol/skill/guardrail update → better behavior`.
> Every component below already exists or is already measured absent. **Nothing is invented.**

### L-1 · The five components the dispatch names, against what exists

| Component | Existing primitive | State (MEASURED_AT mirror@f8db068, 52 refs) |
|---|---|---|
| **learning record** | Annex E.6 field set; body § 15 outcome enum | ✅ EXISTS. 34 records at `learning/mirror/`, 74 across three actors |
| **failure mode** | `framework/eval/failure_taxonomy.md`; body § 40's mandatory `FAILURE / DETECTION / RECOVERY` block | ✅ EXISTS. 12 gates; § 40 blocks throughout the annexes |
| **correction memory** | `framework/eval/learned_gates_registry.md`; Annex E.3 `PROVISIONAL_OPERATIONAL_PRACTICE` | ✅ EXISTS. **79** rows, by status column: 54 ACTIVE_METHOD · 19 ACTIVE_EXECUTABLE · 2 PENDING_EXECUTABLE · 1 SUPERSEDED · 1 PROPOSED · 2 compound cells. Plus 2 fully-fielded E.3 instances (INHERITED: SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001 § 5.3) |
| **index** | Annex E.2 `LEARNING_INDEX` | 🔴 **ABSENT.** 0 objects, 52 refs. `ANNEX_INDEX.md` → pending |
| **retrieval** | Annex E.5 `ACTIVE_LESSONS` → role subset → rehydration | 🔴 **ABSENT.** 0 objects. `CLAUDE.md` § 1's single pointer names `active_lessons/` — *"not yet materialized"* |

### L-2 · Where the governance-side loop stops — INHERITED, attributed, not re-derived

From `SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001` § 3.5 and § 5.5, which tested this with a
positive control rather than assuming it:

```
SCHEMA        present three times over (E.2 index entry · E.3 practice · G.2 proposal)
CONTENT       present at scale — FAILURE_PATTERN in 13 of 33 learning records
🔴 KEY        AFFECTED_WORKFLOW — the field that makes a lesson retrievable by the surface it
              applies to — present in 3 of 33
🔴 COUPLING   0 of 85 executables read learning/ or reviews/  [control: 26 'def ' in legend_lint.py]
🔴 LIFECYCLE  both fully-fielded correction memories expire "at Mirror's first coordination
              review"; 0 such artefacts exist; cadence N is unassigned; G.2 bars Mirror from
              setting it. Annex E.3: "Mai provisional per sempre"
```

I re-ran the coupling test on this ref with the same shape: **0 of 87** Python files under
`framework/scripts`, `scripts` and `governance/scripts` reference `learning/`.

### L-3 · The F.3 promotion path, and why it matters specifically for scientific review

Annex F.3's lifecycle ends `… → PROMOTED_TO_LEARNING → CLOSED`, and its input is a **challenge**.
INHERITED and re-checked: `CHALLENGE_ID` resolves to 1 file (the definition), `DISSENT_ID` to 0.
**Zero challenges have ever been raised.**

The consequence is precise and bears directly on this model: every review→learning link in the
corpus is an **uncontested** finding. The corpus records what a reviewer found and an author
accepted. It records nothing about what a reviewer found and an adjudicator **rejected** — which
is the class F.3 exists to measure, the class that would reveal a compromised adjudicator, and
the class that a Scientist exercising the epistemic independence `roles/scientist.md` grants
would generate first. *"What the evidence supports is the responsible Scientist's call. It is
subject to review and never to an order."* A model for reviewing Scientists that never produces
a contested finding is not measuring what it thinks it is measuring.

### L-4 · 🔴 NEW — the science-side channel exists, is coupled, and is 6% occupied

The prior census measured four memory surfaces — `learning/`, `reviews/`, `governance/`, and the
85 executables — and found zero coupling. It did not measure a fifth, which is the one a
*scientific* correction memory would actually use. Measured this session, with the same
instrument shape:

```
CHANNEL       a deep-dive manifest declares, in landing[], the gates the reading applied:
              "learned_gates_registry#CUTPOINT_ENDPOINT_DRIFT_GATE"

OCCUPANCY     manifests: 64 · citing ≥1 gate: 4 · total citations: 5 · distinct gates cited: 5
              registry population: 79 gates
              → 6% of readings name a gate; 6% of gates have ever been named by a reading

EXECUTABLE    2 of 87 .py files reference learned_gates_registry:
COUPLING        scripts/test_freeze_scope.py                          (pins FREEZE_SCOPE_GATE)
                scripts/test_locator_obligation_reaches_every_route.py
              0 of 87 reference failure_taxonomy
              3 of 87 reference dismissal_ledger — session_self_eval.py, legend_lint.py,
                test_link_targets.py — the negative-memory side, and the only epistemic
                obligation with any executable presence at all
```

**The two loops fail differently, and the distinction is the useful part.** The governance-side
loop has **no channel**: nothing routes a later agent to `learning/`. The science-side loop
**has a channel and barely uses it**: a manifest field, a registry with 79 rows, 21 of them
enforced by regression tests, and 5 citations in 64 readings. One needs a mechanism built; the
other needs the mechanism used. Recorded as a measurement. **No component is proposed here, and
raising the occupancy is not a Mirror act** — the manifest schema is `framework/`, and a
requirement that readings cite gates would be a protocol change.

### L-5 · The route a negative Mirror review would travel, using only existing objects

```
1  FINDING       in a REV- record under Annex C.2, anchored to a repository object
                 → EXISTS (52 such records)
2  RECORD        Annex E.6 Session Learning Record; body §15 outcome
                 → EXISTS (34 records)
3  CLASS         Annex E.2 CONFIRMATION_CLASS; only ORIGINAL_OBSERVATION and REPLICATION count
                 → 🔴 the annex requires consulting the LEARNING_INDEX first. It does not exist,
                    so the class cannot be assigned by the prescribed procedure — this record's
                    own frontmatter is an instance of the defect
4  THRESHOLD     ≥2 confirmations of the first two classes, OR 1 + Mirror validation (E.2)
                 → available; the second branch is why a self-authored class is not self-certified
5  PRACTICE      Annex E.3 PROVISIONAL_OPERATIONAL_PRACTICE, with SUCCESS_CRITERION,
                 FAILURE_CRITERION, EXPIRY, ROLLBACK
                 → EXISTS, instantiated twice
6  DISPOSITION   at expiry: PROMOTE | REJECT | EXTEND_WITH_REASON
                 → 🔴 BLOCKED. Both existing instances expire at an event that has never occurred
                    and that no single actor may schedule
7  LANDING       scientific-reasoning failure → a row in learned_gates_registry (the surface with
                 21 executable enforcements)
                 method failure → MIRROR_UPGRADE_PROPOSAL → Plan candidate → independent
                 reviewer → operator (G.2)
                 → both routes EXIST; neither has carried a finding about a Scientist's reasoning,
                   because no Scientist output exists
```

Stages 1, 2, 4, 5 and 7 run. Stage 3 cannot be performed as specified. Stage 6 terminates on an
event no actor may schedule alone. **That is the loop's actual shape, and it is not a loop yet.**

---

## BLOCKERS

> Stated as blockers to the model's *use*, not as requests. Nothing below is assigned to any
> actor. Mirror holds no command.

```
B-1  🔴 NO CALIBRATION SURFACE EXISTS.
     0 learning records and 0 review records authored by any scientist, across 52 refs. Neither
     MODE A nor MODE B has ever been exercised. The 64 manifests in the corpus were produced by
     main-session readings, not by a registered Scientist actor under a task contract.
     CONSEQUENCE: every criterion in § EPISTEMIC_CRITERIA is untested against a real Scientist
     artefact, and this record cannot claim otherwise. It is a model derived from normative
     sources, not one validated on instances

B-2  🔴 THE PROTOCOL DEFINING THE REVIEWED OBJECT IS NOT ON THE REVIEWER'S REF.
     framework/protocols/scientist_reading_modes.md — absent on `mirror`, present on 14 refs
     including main. Mirror's branch is 65 commits behind main and 76 ahead. Every citation of
     § 3.8, § 5.2 and § 5.4 in this record reads from main@788c357

B-3  🔴 THE EVIDENCE SURFACE IS NOT IN GIT.
     `files/` is .gitignore:7 → 0 paths under files/ in the 755-path ref union. Every mechanical
     instrument in § R-3 resolves locators against artifacts under files/. A reviewer restricted
     to git objects can verify that a manifest is WELL-FORMED and cannot verify that it describes
     the artifact it names. This is the outer boundary of every observable in this record

B-4  🔴 MIRROR_SAMPLED HAS NO RATE.
     3 normative occurrences, all restating the enumeration; no rate, fraction, cadence or
     trigger. The parameter that decides whether an ordinary reading is ever reviewed by Mirror
     is undefined, and G.2 bars Mirror from setting it

B-5  🔴 NO ORCHESTRATOR.
     0 ACTIVE leases by derivation. C.3's "apertura solo via Orchestrator" is unsatisfiable;
     H.1's "Livello Ladder (≥ floor) e reviewer → Orchestrator" has no holder; challenge
     adjudication has no holder

B-6  🔴 THIS MODEL MAY NOT BE ADOPTED BY ITS AUTHOR.
     G.2 and H.1 both bar Mirror from self-approving a change to its own review rubric. Every
     element marked PROPOSED requires: MIRROR_UPGRADE_PROPOSAL → Plan candidate → independent
     reviewer chosen by Orchestrator → validation; operator if governance. Two of those four
     steps have no current holder (B-5)

B-7  🔴 THE METRIC THAT WOULD FALSIFY THIS MODEL HAS NEVER BEEN COMPUTED.
     REVIEW_YIELD: 0 files, 52 refs. G.3 makes it one of Mirror's two exclusive metrics and
     the exclusive source of a future v3.2. Without it, "Mirror's reviews of readings are
     ritual" is unfalsifiable — which is the precise condition § IND-2 exists to prevent

B-8  🔴 NO EVENT LEDGER.
     0 objects; 0 of 755 paths contain "event". roles/mirror.md states Mirror's primary analysis
     runs on the consolidated ledger (J.1). 5 of the 8 DETECTION routes the frozen specification
     declares are routed to Mirror instruments that are unmaterialized, including both routes
     that fire on RECURRENCE — the condition G.1 names as MIRROR_REQUIRED
     (INHERITED: SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001 § 5.4)
```

---

## OPEN_QUESTIONS

> **Recorded, not resolved.** Each carries the owner H.1 already gives it. None is assigned by
> this record; none is answered here; none is ranked. Questions already open in
> `ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001` (IQ-1…IQ-13) are **not** restated — they are carried
> forward unchanged, and EQ-2 and EQ-6 below are the two that intersect them.

| # | Question | Owner by H.1 |
|---|---|---|
| **EQ-1** | C.4 routes `INFERENCE → peer Scientist`. With one Scientist active on a reading and no second one registered, who performs the inference review — or is the reading held until a peer exists? | Orchestrator / operator |
| **EQ-2** | If a Mirror review of a reading must also carry a gate decision (may this reading proceed), is that gate decision within Annex G's *"no command over any actor · never a veto before the fact"*? Intersects IQ-2. | operator |
| **EQ-3** | Is a reading's **Part 2 self-evaluation answer** a reviewable object under C.2 — with an `OBJECT`, an `AUTHOR` and an `AUTHOR_RESPONSE` — or is it an input to a review of something else? | operator / Plan (classification) |
| **EQ-4** | What is the floor for a review of an ordinary reading? C.1 gives R0 for `osservazione L1 ordinaria` and R2 for `inferenza therapeutic-actionable`. A complete full-text read produces both in one artefact. Does the floor follow the highest claim in the reading? | Orchestrator (H.1: Ladder level) |
| **EQ-5** | Must the blind locator audit run before a reading is reviewable, or is it optional? `scientist_reading_modes.md` § 3.8 lists it as step 5 of the acceptance test; `locator_audit.py` calls itself *"the mechanical half"* of it; **0 blind-audit outputs exist**. | operator / Plan (protocol) |
| **EQ-6** | Who chooses **which** triples a blind audit covers, given that the chooser sees what the auditor may not? Intersects IQ-12 (the `MIRROR_SAMPLED` rate) and is the same question one level down. | operator |
| **EQ-7** | Does a `MIRROR_SAMPLED` audit of a reading require the operator's dispatch, given that C.3 gives review opening to an Orchestrator that does not exist? | operator |
| **EQ-8** | Is a manifest's `landing[]` citation of a `learned_gates_registry#GATE` an assertion that the gate was **applied**, or that the reading **landed** in the registry? The field name says the second; 4 of 64 manifests use it as the first. | Plan (schema) |
| **EQ-9** | The re-audit rule (`epistemic_discipline.md` § 2, obligation 3) has no instrument and no owner. Is a reading's failure to re-scan the dismissal ledger on a new mechanistic `DATO` a defect of the reading, of the protocol, or of neither until an instrument exists? | operator / Scientist |
| **EQ-10** | Does reviewing a Scientist's **reasoning account** rather than its **conclusions** satisfy the dispatch's stated goal, or does the operator intend Mirror to reach the conclusions — which C.4 and `scientist_reading_modes.md` § 5.4 both route elsewhere? **This is the question on which the whole record turns, and it is the operator's.** | operator |

---

## WHAT THIS RECORD DOES NOT DO

```
NO ADOPTION        nothing here is in force. Every PROPOSED element routes through G.2
NO GOVERNANCE      no annex is amended, interpreted, reconciled or extended. Quotations are quotations
NO VALIDATOR       no check, script, schema or field is created
NO FRAMEWORK EDIT  framework/ is read at two refs and written at none
NO RUBRIC          § EPISTEMIC_CRITERIA maps existing criteria to existing owners; it scores nothing
NO ASSIGNMENT      no actor is named as owner of any action. Mirror holds no command
NO VERDICT         no object is reviewed, no author named, no C.2 verdict issued
NO SUPERSESSION    ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001 and
                   SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001 stand unchanged; overlap is mapped
NO ANSWER          all ten EQ questions and all thirteen inherited IQ questions stay open
NO CLOCK STARTED   this task produced no MIRROR_RETROSPECTIVE and no coordination review, and
                   makes no claim about the expiry anchor of any provisional practice
```

---

## EVIDENCE

Every load-bearing number in this record, with how to reproduce it.

| Claim | Reproduction | Value |
|---|---|---|
| no ACTIVE lease | `lease_state.py --check` on `main:runtime/orchestrator_lease.md` | `ACTIVE by derivation: 0` |
| state READY | `framework/state/state_manifest_current.md:141` | `current_state: READY` |
| LINT | `python3 framework/scripts/legend_lint.py .` | `VERDICT: PASS` |
| 52 refs / 755 paths | `git for-each-ref` + `git ls-tree -r --name-only` union | 52 · 755 |
| 0 scientist-authored records | grep `scientist|lettore` over the path union | 11 paths, 0 authored records |
| reviewer 36/36, level R4 31/31 | `grep -l '^reviewer:\|^level:' reviews/mirror/*.md` | 36 · 31 |
| 0 C.2 verdicts declared | classify `^verdict:` by leading token; control = the four words in any body | 0 of 33 · control 29 of 52 |
| gate status distribution | last table column of each `^| \`` row | 54 / 19 / 2 / 1 / 1 / 2 compound |
| 64 manifests / 1002 locators | JSON walk over `deepdive_manifests/*.json` | 64 · 1002 |
| 4 legacy manifests, 33 unreachable locators | JSON walk: `schema_version != 2`; then `surface` / `artifact` absence | 60 v2 · 4 absent · 33 locators · 0 with an artifact |
| 12 failure-taxonomy gates | `grep -c '^| \*\*' framework/eval/failure_taxonomy.md` | 12 |
| 79 learned gates | `grep -c '^| \`' framework/eval/learned_gates_registry.md` | 79 |
| 11 MODE B axes | `sed -n '/### 5.2/,/### 5.3/p'` on `main:scientist_reading_modes.md` | 11 |
| gate citations in manifests | JSON walk over `landing[]` for `learned_gates_registry#` | 4 of 64 · 5 citations · 5 distinct |
| 2 of 87 executables cite the registry | `grep -rl learned_gates_registry --include='*.py'` | `test_freeze_scope.py`, `test_locator_obligation_reaches_every_route.py` |
| 0 of 87 read `learning/` | `grep -rl 'learning/' --include='*.py'` · control: 3 hits for `dismissal_ledger` | 0 · control passed |
| `files/` absent from git | `.gitignore:7`; `grep -c '^files/'` over the path union | 0 |
| `scientist_reading_modes.md` off-ref | per-ref `git cat-file -e` sweep, braced expansion | absent on `mirror`, present on 14 |
| MIRROR_SAMPLED unparameterised | `grep -rn MIRROR_SAMPLED` over normative files | 3 files, enumeration only |
| premise/revival checks are non-blocking | `framework/scripts/legend_lint.py:215,224` | `WARN_BUT_PROCEED` ×2 |
