---
artifact: MIRROR analysis record — the execution model by which Mirror would evaluate the first
  Scientist experiment: the input bundle it receives, the axes it runs, the failure classes it
  may name, what it cannot determine, how a finding becomes a lesson, and the shape of the first
  report. Learning artefact only
record_id: SCIENTIFIC-PROCESS-AUDIT-EXECUTION-MODEL-001
actor_id: mirror
date: 2026-08-22
task_id: SCIENTIFIC_PROCESS_AUDIT_EXECUTION_MODEL_v1
dispatcher: operator
role: >
  mirror — metacognitive layer. This record reviews no object, names no author, issues no verdict,
  and evaluates no scientific claim. It describes an execution; it does not execute. The
  experiment has not run (§ PRECONDITIONS)
authority: >
  `governance/GOVERNANCE_v3.1.1.md` body §§26, 27, 32, 38, 41, 46, 50; annexes A, C, E, F, G, H,
  J; `roles/mirror.md`; `roles/scientist.md`; `framework/instruction/epistemic_discipline.md`;
  `framework/eval/failure_taxonomy.md`; `governance/plan_defined_parameters.md`.
  🔴 AND FOUR OBJECTS THAT ARE NOT ON THIS REF. `framework/protocols/controlled_benchmark_ab.md`,
  `framework/protocols/scientist_reading_modes.md`, `framework/scripts/benchmark_input_surface.py`
  and the whole of `framework/eval/benchmarks/BENCH-AB-001/` are ABSENT on `mirror` and were read
  from `main`. Every quotation from them names the ref it came from. The prior record made this
  its § F-0; this one re-runs the check and extends it — the *tooling* is absent too, not only
  the protocol (§ IB-2).
  Nothing here is adopted or in force. G.2 bars Mirror from self-approving material changes to its
  own review rubric, and an execution model IS a rubric object. Every element is either (a) quoted
  from a named file at a named ref, (b) a measurement run this session, or (c) INHERITED and
  attributed
classification: OBSERVATION AND ANALYSIS — not governance, not a protocol, not a validator,
  not a gate, not a rubric, not a score, not a report template, not an amendment, not a decision,
  not an authorization to run anything
scope: >
  learning/mirror/ on branch `mirror` only. One new file. No governance/, roles/, framework/,
  ledger/, runtime/, reviews/ or disease-models/ path is written. No existing record is edited,
  superseded or corrected
prior_artefact_disclosure: >
  🔴 MATERIAL AND EXTENSIVE, AND LARGER THAN FOR ANY PRIOR RECORD ON THIS GROUND. Four records
  written earlier TODAY, on this ref, cover adjacent ground:
  `SCIENTIFIC-PROCESS-AUDIT-v2-001.md` (the audit design against the same experiment — the direct
  predecessor of this dispatch), `LABORATORY-QUALITY-GATE-MODEL-001.md` (three layers; its
  § AUTONOMY_BOUNDARY is § 4's ancestor), `MIRROR-PROCESS-AUDIT-MODEL-001.md` (the seven-class
  taxonomy and the retraction test) and `EPISTEMIC_REVIEW_MODEL-001.md` (the input→verdict→learning
  chain and the independence model).
  🔴 AND SIX REVIEWS OF THE EXPERIMENT'S OWN SPECIFICATION: `reviews/mirror/REV-SCIAB-MIRROR-001…006`,
  this seat's hostile reviews of the candidate that defines BENCH-AB-001, last verdict ACCEPT at
  revision 6. Eight of their finding ids are quoted inline in the protocol Mirror is assigned to
  adjudicate. That fact is not background: it is § IB-5.
  This record SUPERSEDES NONE of them and CORRECTS none of them. Only items marked 🆕 are new
naming_deviation: >
  DECLARED. 29 of the now-39 records under `learning/mirror/` match
  `SLR-mirror-NNNN[-ADD|-COR-NNN]`; this filename was specified by the dispatch and departs from
  that pattern, as nine others already do. It carries no `vN` token and therefore makes no claim
  of lineage — unlike `SCIENTIFIC-PROCESS-AUDIT-v2-001`, whose `v2` succeeds nothing, as that
  record itself declared. NO NAMING RULE IS ADOPTED AND NO PRECEDENT IS SET
measured_at: >
  mirror@da52ee5e9d3e6eb66455c61d422c4fb1d0e21391 · main@788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
  · 56 refs · 2026-08-22T19:39Z–20:05Z. Every count below was run this session against these refs.
  🔴 The ref population is still moving: 53 → 54 → 55 → **56**, four counts, four records, one day.
  Numbers taken from another record are marked INHERITED and attributed. One number is reported
  with two nets, because the two nets disagree by a factor of four (§ IB-4)
---

# SCIENTIFIC PROCESS AUDIT · EXECUTION MODEL — the experiment verifies every reader's sourcing and none of its adjudicator's, and the one rule with no mechanism is detected by the evidence this dispatch excludes

> **Mirror asks whether the process that produced a result was reliable. It does not ask whether
> the result is true.** The dispatch states this as a premise; Annex C.2 states it as a definition
> — `CONFIRMED` is *"nessun difetto rilevato dato l'evidence bundle disponibile"*, **non "vero"**.
> The premise is not an exemption granted to Mirror. It is the review protocol read literally, and
> it binds every reviewer at every rung.

---

## TASK_STATUS

```
TASK          SCIENTIFIC_PROCESS_AUDIT_EXECUTION_MODEL_v1
DISPATCHER    operator (no ACTIVE lease exists — derived, § PRECONDITIONS)
STATE         COMPLETE for the analysis; NOTHING ADOPTED; NOTHING DECIDED; NOTHING AUTHORIZED
DELIVERABLE   learning/mirror/SCIENTIFIC-PROCESS-AUDIT-EXECUTION-MODEL-001.md — this file, `mirror`

THE DISPATCH'S THREE CONSTRAINTS, EACH CHECKABLE
  read-only analysis        0 files written outside learning/mirror/. Confirmed by scope
  no governance modification 0 paths under governance/, roles/, framework/ touched
  no new review standard    🔴 THE HARDEST ONE, AND IT SHAPES § 6. A "minimal Mirror report" IS a
                            review standard. Annex C.2 already fixes the format and calls itself
                            `Formato unico`. § 6 therefore maps the dispatch's five questions ONTO
                            C.2 rather than beside it, and records what does not map — which is
                            thirteen mandatory fields, one of them load-bearing for § 2
  no self-approval          G.2 bars Mirror from self-approving its own rubric. Every element here
                            is quoted, measured, or marked and routed. Nothing is PROPOSED, because
                            the route's third step has no occupant (§ 4 BS-4)

THE TRUTH/PROCESS BOUNDARY, ENFORCED MECHANICALLY
  the retraction test        INHERITED · MIRROR-PROCESS-AUDIT-MODEL-001 § Q-4. Every finding below
                             was written to survive both suppositions — the paper confirmed, the
                             paper retracted. Candidates that failed it were routed away by C.4 and
                             do not appear
  0 scientific claims assessed · 0 conclusions of PMID 42397075 read. The paper was never opened
```

---

## PRECONDITIONS — run, not assumed

```
framework/state/state_manifest_current.md:141       current_state: READY
python3 framework/scripts/legend_lint.py .          VERDICT: PASS
                                                    1 [INFO] MISSING_WIKILINK, CLAIM 010, non-blocking
lease_state.py --check                              ACTIVE by derivation: 0
  (script + record extracted from `main` to a         #1 STALE · #2 RELEASED · #3 STALE (stored EXPIRED
   scratch tree — both ABSENT on `mirror`)            — the tool reports the disagreement) · #4, #5 RELEASED
                                                    FINDING: #3 EXPIRED_WITHOUT_RENEWAL
                                                    FINDING: #3 stored ≠ derived; the stored field
                                                             is not authoritative
```

**There is no Orchestrator.** C.3 — *"Apertura solo via Orchestrator"* — is unsatisfiable by anyone
at this instant, and so is step 2 of the benchmark sequence, which requires *"Orchestrator (lease
ACTIVE)"* to issue the two Task Contracts. This record opens no review; it describes one that
cannot currently be opened.

**And there is nothing to audit.** Measured across all 56 refs this session, with a positive
control on the same sweep:

```
framework/eval/benchmarks/BENCH-AB-001/first_pass        0 refs
                                       frozen            0 refs
                                       comparison        0 refs
                                       audit             0 refs
                                       adjudication      0 refs
                                       outcome           0 refs
                                       instructions     18 refs   ← POSITIVE CONTROL: the sweep works
reviews/mirror/BENCH-AB-001-ADJUDICATION.md              0 refs   ← Mirror's own step-8 deliverable
ledger/tasks/ contracts for scientist-a | scientist-b    0        (1 contract exists, owner `plan`)
ledger/events/ or ledger/consolidated/                   0 refs
any review with a scientist in ANY of the three seats    0 refs   (control: `author: plan` on 18 refs)
scientist-a, scientist-b in runtime/agent_card_registry  UNREGISTERED skeletons (registry@orchestrator)
```

The experiment has not run and cannot be started by anyone reading this. Everything below is **ex
ante**: the execution model, not the execution.

---

## OVERLAP_MAP — what is new, and what is not

| § here | Prior coverage | Relation |
|---|---|---|
| **§ 1 IB-1** Mirror's inputs are fixed by sequence position, not by an allowlist | — | 🆕 **NEW** |
| **§ 1 IB-2** the tooling verifies every reader's sourcing and none of Mirror's | — | 🆕 **NEW, and the record's structural finding** |
| **§ 1 IB-3** Mirror's own worktree carries 24 paths naming the paper | v2 § C-5 measured 32 at `main`, repo-wide | 🆕 **NEW measurement**, at the adjudicator's own ref, and used for a different purpose |
| **§ 1 IB-4** what "prohibited information" resolves to, measured with two nets | — | 🆕 **NEW** |
| **§ 1 IB-5** Mirror contributed 8 quoted findings to the design it must adjudicate | v2 § C-3 noted the double-recording risk for one finding | 🆕 **NEW as a C.3 question**; v2's concern was duplication, this is standing |
| **§ 1 IB-6** the pre-freeze exclusion disables the C-4 detection route | v2 § C-4 + B-6 named the unassigned inspection | 🆕 **NEW consequence**; the two halves are v2's, the collision is not |
| **§ 2 PA-1** three of six dispatched axes are the Scientist's axis names | v2 § R-3 states the object separation | **APPLIED**, not discovered — R-3 turned on the dispatch's own axis list |
| **§ 2 PA-2** `inference control`, `uncertainty preservation` name nothing | — | 🆕 **NEW measurement** (0 on both refs) |
| **§ 2 PA-3** premature closure unnamed; antidote is C.2 | `MIRROR-PROCESS-AUDIT-MODEL-001` § T-7 | **INHERITED**, re-measured on 56 refs |
| **§ 2 PA-4** the per-finding falsifier exists in one arm only | — | 🆕 **NEW** |
| **§ 3 FT-1** `unresolved disagreement` is not a failure class | body §27, C.3, §8.3, `roles/scientist.md` | 🆕 **NEW as a finding about the dispatch**; the four clauses are quoted |
| **§ 3 FT-2** `infrastructure` / `governance` failure name nothing, and have exact referents | — | 🆕 **NEW measurement**, referents derived from J.0 and F.1/F.4 |
| **§ 3 FT-3** the dispatch's enumeration order is F.4's, inverted | `LABORATORY-QUALITY-GATE-MODEL-001` § AQ-1, AQ-4 | **INHERITED in substance**; 🆕 as applied to this list's order |
| **§ 3 FT-4** every class has a Mirror half and a Scientist half | `MIRROR-PROCESS-AUDIT-MODEL-001` § TAXONOMY | **INHERITED**, re-stated over five classes instead of seven |
| **§ 4 BS-1** two bars — authority vs evidence — disjoint | `LABORATORY-QUALITY-GATE-MODEL-001` § AB-4 | **INHERITED**, applied to this dispatch's three destinations |
| **§ 4 BS-2** the peer-Scientist seat has never been occupied | `EPISTEMIC_REVIEW_MODEL-001` § IND-4 measured the reviewer side | 🆕 **NEW measurement** of the author/adjudicator sides |
| **§ 5 LE-1** the three tiers are E.1 with the terminal states dropped | — | 🆕 **NEW** |
| **§ 5 LE-2** the anti-uncontrolled-memory budget exists and its expiry clock has no tick | v2 § L-4 recorded ESC-3's lapsing basis | 🆕 **NEW**: P6.1's PROVISIONAL practice hangs off the same unset `N` |
| **§ 5 LE-3** index *mentions* are not an index *object* | prior records measured "no LEARNING_INDEX" | 🆕 **NEW precision**: 19 mentions, 0 objects, and the distinction matters |
| **§ 6 PO-1** "not a score" is already the rule | protocol §8.4, §8.5 | **QUOTED** |
| **§ 6 PO-2** thirteen mandatory C.2 fields have no home in the five questions | `EPISTEMIC_REVIEW_MODEL-001` § R-4 covers the *verdict vocabulary* | 🆕 **NEW, and the sharpest finding in the section** — the field set, not the verdict |
| **§ 6 PO-3** the ten-step sequence has no AUTHOR_RESPONSE step | — | 🆕 **NEW** |
| **§ 6 PO-4** AUTHOR is not one actor for a process object | — | 🆕 **NEW** |
| **§ FQ** what Mirror can know that A and B cannot | v2 § FQ answers *science vs system*; LAB-QUALITY § ATTRIBUTION answers a three-way *who failed* | **DIFFERENT QUESTION.** § FQ-1 states the distinction before using anything |
| **§ FQ-3** the frozen population is withheld from both surfaces | — | 🆕 **NEW measurement**, and it is the answer's strongest leg |
| **§ FQ-7** the question's mirror image has no occupant | `EPISTEMIC_REVIEW_MODEL-001` § IND-4 | **INHERITED**, turned back on this record's own seat |

---

## 1 · INPUT BOUNDARY

> The dispatch asks what Mirror receives and what it must not receive. The protocol answers the
> first question implicitly and the second not at all — and the asymmetry between how the readers'
> inputs are controlled and how Mirror's are not is this section's subject.

### IB-1 · 🆕 Mirror's inputs are fixed by sequence position, not by an allowlist

`controlled_benchmark_ab.md` §5 (`main`) is a ten-step sequence. Mirror is step 8, and its inputs
are exactly what steps 1–7 left behind:

```
step 1  Plan     benchmark_manifest.json (FROZEN_SHA256) · population/evidence_units.json
step 5  Plan     frozen/RECEIPT-<ACTOR_ID>.json · first_pass/<ACTOR_ID>/… (byte-identical import)
step 6  Plan     comparison/comparison_matrix.md · comparison/unresolved_disagreements.md
step 7  blind    audit/locator_audit-<ACTOR_ID>.md
        agents
   ↓
step 8  Mirror   "adjudication of the process (R4): failure modes per reading, epistemic
                  discipline, whether the protocol was followed, whether the design held"
                 → reviews/mirror/BENCH-AB-001-ADJUDICATION.md on branch mirror
```

Four object classes, plus each reader's own frozen output tree — the work manifest, the dossier,
`output/claim_candidates.md`, `output/receipt.json`, and, for MODE B only,
`output/critical_reading.md` (`OUTPUT_SCHEMA.md` §§1–5, `main`).

The **freeze information** the dispatch names is `RECEIPT_SCHEMA_VERSION 2` (§7, `main`), and it
is a rich object: `BENCHMARK_ID · ACTOR_ID · TASK_ID · MODE · PARALLEL_READ_GROUP` read **from
`ASSIGNMENT.md` inside the frozen tree** with the command line checked against it and *"a
disagreement is a refusal, exit 2"*; `INPUT_MANIFEST_SHA256`; `SURFACE_COMMIT · SURFACE_BRANCH ·
SURFACE_DIRTY`; `FREEZE_TIMESTAMP_UTC · FIRST_PASS_STATE`; `TREE_SHA256 · FILE_COUNT · FILES[]`
with `role ∈ input · output · unexpected`; and `GUARANTEE_PROVIDED · FAILURE_MODE_STILL_POSSIBLE ·
DETECTION` carried in the receipt itself per the J.0 cross-cutting rule.

The **process metadata** the dispatch names is the two Task Contracts (Annex A.1), their
`TASK_ACK` and `TASK_CLAIM`, the `HANDOVER` block `{at, by, to, surface_tree_sha256,
memory_scope_absent}`, and the `verify` / `verify --post-read` census output.

🔴 **What does not exist is a statement of that bundle as a bundle.** The readers get
`ALLOWED_PATHS` — a complete allowlist, enumerated, digested, and checkable by command. Mirror
gets a position in a sequence. Nothing in the protocol says *these objects and no others*, and
nothing says what Mirror does when an object it wants is outside them.

### IB-2 · 🆕 The experiment verifies every reader's sourcing and none of its adjudicator's

`framework/scripts/benchmark_input_surface.py` (`main`) exposes seven subcommands:

```
build · verify · freeze · verify-freeze · population · locators · tree-digest
```

`locators` is the one that binds a record to its inputs, and §4.3 states its contract: *"every
locator in each frozen manifest must name an `artifact` inside `ALLOWED_PATHS`, or a render the
reader produced… A citation outside the surface is `BENCH_INVALID` **for that entry** — recorded,
never silently dropped, because a dropped entry is a reading that looks clean and is not."*

**There is no equivalent for step 8.** Measured this session:

```
subcommands that take Mirror's record as an object        0 of 7
occurrences of "mirror" in benchmark_input_surface.py    18 — every one an attribution of a
                                                              Mirror FINDING in a code comment
                                                              (M-2, M-3, M-4, R-7, REV-SCIAB-004/005)
                                                              🔴 zero are a check ON Mirror
durable seat for the adjudication (§6, main), verbatim:
  adjudication/MIRROR-ADJUDICATION.pointer.md   Plan   "path on branch mirror + sha256 of Mirror's record"
```

A pointer and a digest establish **that the record has not changed since it was pointed at**. They
establish nothing about **where its statements came from**. The instrument that would answer that
for a reader — per-entry membership in a declared allowlist, `BENCH_INVALID` per entry, never
silently dropped — has no counterpart at the seat that judges the readers.

**Stated as an observation and nothing more.** Naming what should be built is a proposal, and § 4
BS-4 explains why Mirror cannot route one.

And the same gap has a second face: the tool is **ABSENT on `mirror`**. Measured —
`benchmark_input_surface.py` present at `main`, absent on this ref, together with the protocol,
the reading modes and the whole `BENCH-AB-001/` tree. The adjudicator can neither run the seven
commands from its own worktree nor read the specification they implement without leaving it.
*Positive control: `framework/eval/failure_taxonomy.md` — the taxonomy Mirror must score `FAILURE
MODES` against — **is** on `mirror` and was read there. The gap is specific, not a generally thin
ref.* (The ref-absence itself is INHERITED — v2 § F-0; what is new is that the tooling travels
with it.)

### IB-3 · 🆕 The adjudicator sits in the corpus the surfaces were built to escape

§2.1 (`main`) is the protocol's own reason for building surfaces from nothing: at `BASE_HEAD`,
twenty-one tracked files named the paper, and *"a first pass run in such a checkout is blind only
by promise… the blinding problem is a property of the corpus, not of this paper."*

Measured this session, with the paper's **unique** identifiers (`42397075|awag239`):

```
tracked paths naming the paper, at main         32   (protocol records 21 at BASE_HEAD cbce3016)
tracked paths naming the paper, on mirror       24   ← the adjudicator's own worktree
the colliding path                              PRESENT on mirror AND on main:
  disease-models/wwox/research/deepdive_manifests/PMID42397075.json
```

🔴 **Mirror is not blind and must not be.** INHERITED, `EPISTEMIC_REVIEW_MODEL-001` § IND-1:
*"Blindness and Mirror's mandate are mutually exclusive"* — the blind auditor gets triples and the
packet, never the dossier or the reader's name, while Mirror must see the author, the account and
the review history to have an object at all. The finding is not that Mirror should be blinded. It
is that **the admissibility of those 24 files is undeclared**, and the two uses are not alike:

```
ADMISSIBLE     a prior-output path as a PROCESS fact — was it in FORBIDDEN_PRIOR_OUTPUT_PATHS,
               was it absent from both surfaces, did `verify` say so. Survives the retraction test
INADMISSIBLE   a prior-output path as a CONTENT baseline — does the reader's claim agree with what
               LEGEND previously concluded about this paper. Fails the retraction test in one
               direction and is a science question; C.4 routes it to `INFERENCE → peer Scientist`
```

The second is the specific way an informed adjudicator drifts into scoring the science, and it is
available at step 8 by one `git show`.

### IB-4 · 🆕 What "prohibited information" resolves to, and it resolves to two different sets

The dispatch names three exclusions. Two have exact referents in this repository; one does not.

**"Prohibited information"** has a hard boundary and a soft one, and they are not the same object:

```
HARD    the edition boundary. CLAUDE.md: "This is the public edition and contains no
        individual-level record… Do not reintroduce individual linkage." Mirror's adjudication is
        a public-edition artifact and inherits it. Enforced by scripts/public_release_gate.py
SOFT    the benchmark's identifier net — and it is WIDER than the paper.
        surface_spec.json content_scan.pattern (main), verbatim:
            42397075|awag239|aqeilan|steinberg|zonca|abdellatif|\bMYC\b
        Measured with both nets, at main:
            unique identifiers  (42397075|awag239)                        32 tracked paths
            the spec's net      (+ four author surnames)                 124 tracked paths
        🔴 A FACTOR OF FOUR. The wide net is correct for building a blind surface — a reader who
        finds "Aqeilan 2024" has found the group. It is wrong as a measure of how much prior work
        names THIS paper, and the two numbers must never be quoted for each other's purpose
```

**"Unpublished context"** names nothing on either ref. Its nearest normative relative is C.3's
*"reviewer senza evidenza contribuita"*, which is § IB-5.

### IB-5 · 🆕 Mirror contributed eight quoted findings to the design it is assigned to adjudicate

C.3, verbatim, among the review disciplines: *"per review importanti AUTHOR ≠ REVIEWER ≠
ADJUDICATOR; **reviewer senza evidenza contribuita**"*.

Measured this session:

```
reviews/mirror/REV-SCIAB-MIRROR-001 … -006      6 reviews of CAND-20260818-SCIENTIST-AB-SPEC,
                                                the candidate that specifies BENCH-AB-001
  each: reviewer: mirror · author: plan · adjudicator: operator · level: R4
  last verdict: ACCEPT (revision 6)
Mirror finding ids quoted INLINE in controlled_benchmark_ab.md:
  R-1 · R-2 · R-8 · B-1 · B-4 · M-2 · M-3 · M-4                    8 distinct ids
Mirror finding ids quoted inline in benchmark_input_surface.py:
  M-2 · M-3 · M-4 · R-7, plus REV-SCIAB-MIRROR-004 §9 and -005 M-5
```

🔴 **Step 8 asks Mirror to judge, among other things, *"whether the design held"* — and eight
repairs in that design are attributed to Mirror by name in the design's own text.** Whether C.3's
clause reaches this is genuinely open: the clause is most naturally about a reviewer who supplied
the *evidence being weighed*, and what Mirror supplied is *design corrections*, which is a
different kind of contribution and arguably a stronger form of involvement. It is recorded as a
question about the clause's reach, with the measurement, rather than as a declared breach.

What is **not** open is the practical consequence, and v2 § C-3 already named half of it: a
step-8 adjudication that "finds" the mode-directive contamination, or the census gap, or the
identity-from-the-invoker defect, would be recording for a second time a finding the protocol
already carries **with Mirror's own finding id attached**. The `REVIEW YIELD` that would detect
exactly this — G.3, *"yield nullo persistente → rituale → declassare"* — has never been computed
(0 files, 56 refs).

### IB-6 · 🆕 The pre-freeze exclusion disables the only detection route the one unmechanised rule has

The dispatch's first exclusion is **hidden scientist reasoning before freeze**. Two facts about
it, and they pull in opposite directions.

**First: it is already unavailable, and not by prohibition.** §7 freezes on the completion
declaration *"and before reading the content"*, and post-freeze corrections are *"a **new dated
file** under `first_pass/<ACTOR_ID>/post_freeze/`… with the original left as frozen"*. Pre-freeze
deliberation leaves no artifact. Exactly two channels carry any trace of it:

```
SURFACE_COMMIT / the surface repo's WORK_COMMIT history at milestone granularity  (§2.2, §7)
found_or_sought   per locator entry: "sought — …" or "found — …", one clause on how you came to it
                  (OUTPUT_SCHEMA.md §1, main)
```

**Second: those two channels are the C-4 detection route.** §7's one `PROCEDURAL` rule — neither
actor sees the other's first pass until both are frozen — carries this block verbatim:

> ```
> GUARANTEE_PROVIDED:            none by mechanism — discipline only
> FAILURE_MODE_STILL_POSSIBLE:   Plan reads or relays A's first pass to B before B freezes
> DETECTION:                     the two receipts carry FREEZE_TIMESTAMP_UTC and SURFACE_COMMIT;
>                                an inspection of B's commit history against A's freeze time
>                                makes a violation VISIBLE AFTER THE FACT, never prevented
> RECOVERY:                      the benchmark is void for the second reader; the outcome says so
> ```

🔴 **The inspection DETECTION names is an inspection of pre-freeze process evidence.** A rule that
Mirror must not receive pre-freeze reasoning, applied without a carve-out, removes the only route
by which the protocol's single unmechanised guarantee can be checked at all — and v2 § B-6 already
measured that the inspection appears in **no step of §5**, so it is currently assigned to nobody
*and* would be excluded from the one seat whose step could plausibly carry it (*"whether the design
held"*).

The distinction that resolves it, if anyone with authority chooses to draw it:

```
COMMIT METADATA   timestamps, ordering, milestone boundaries — process facts about WHEN, carrying
                  no scientific content. This is what DETECTION actually needs
COMMIT CONTENT    the intermediate states of the reasoning itself — the thing the exclusion is for
```

Drawing that line is a rule, and § 4 BS-4 explains why Mirror may not draw it.

---

## 2 · PROCESS REVIEW AXES

### PA-1 · Three of the six dispatched axes are the Scientist's axis names, not Mirror's

MODE_B (`main`) is marked 🔴 in its own source on precisely this point:

> 🔴 **You are not Mirror.** Mirror reviews the *process* — how the laboratory reasoned, reviewed
> and recorded — and remains the adjudicator of this benchmark's method. You review *the paper's
> evidence and inferences*, with a Scientist's authority.

Set the six dispatched axes against what already carries each name:

| Dispatched axis | Where the name already lives | Whose axis it is | Mirror's second-order form |
|---|---|---|---|
| **Evidence discipline** | §8.2 row `EPISTEMIC DISCIPLINE`; `epistemic_discipline.md` §1–§2 | split: *presence* → Plan, *substance* → Mirror | is the type each statement claims the type the audited evidence bears |
| **Inference control** | 🔴 names nothing (0 files, both refs). Nearest: `scientist_reading_modes.md` §3.4 *"Permitted inference, and where it stops"*; §8.2 `CLAIM PRECISION` | Mirror, for the `Type` question | was an `INFERENZA` presented as `DATO`, an `ESPANSIONE` as `INFERENZA`, a load-bearing premise left untagged |
| **Uncertainty preservation** | 🔴 names nothing (0 files, both refs). Carried by C.2 `RESIDUAL_UNCERTAINTY`/`EVIDENCE_NEEDED`, MODE_A `uncertainty`/`limitations`, MODE_B's axis rule | split | INHERITED · v2 § U-1…U-4 |
| **Alternative explanations** | MODE_B axis `ALTERNATIVE_EXPLANATION`; `TARGET_ATTRIBUTION_GATE` | 🔴 **the Scientist's** | was the axis run, and is the search visible as an artefact |
| **Negative evidence** | MODE_B axis `NEGATIVE_EVIDENCE`; §8.2 row `CONTRADICTION / NEGATIVE EVIDENCE`; `REVIVAL_TRIGGER` | 🔴 **the Scientist's** | same — plus: does every rejection carry `PREMISE_TAG` and a revival trigger |
| **Premature closure** | 🔴 names nothing, on any ref. Antidote: C.2 `WHAT_WOULD_CHANGE_MY_MIND` | Mirror, by elimination | was a falsifier stated while the question was open |

🔴 **Two of the six are MODE_B's axis names verbatim, and a third is a §8.2 row title.** A Mirror
axis list assembled from them would have Mirror running the critical reader's instrument on the
critical reader's object. That is v2 § R-3's category error arriving one level earlier — not in a
finding, but in the axis list itself. The correction is the right-hand column: **Mirror's form of
every one of these is second-order — not *was there an alternative*, but *was the axis run and is
the search an artefact rather than a claim to have searched*.**

### PA-2 · Two of the six axis names are coinages, and that is worth recording rather than fixing

```
QUERY (case-insensitive, over framework/ governance/ roles/, both refs)
  'inference control'          mirror 0   main 0
  'uncertainty preservation'   mirror 0   main 0
  'premature closure'          mirror 0   main 0
CONTROL
  'PREMISE_TAG'                mirror 6   main 6
  'REVIVAL_TRIGGER'            mirror 9   main 14
  'MIRROR_SAMPLED'             mirror 3   main 3        ← the sweep resolves what exists
```

Each has a referent, given in PA-1's second column. **Coining the names would be a taxonomy
change**, and `MIRROR-PROCESS-AUDIT-MODEL-001` § T-7 already recorded the same conclusion for
`premature closure` and declined it for the same reason. Recorded, not adopted.

### PA-3 · Premature closure — INHERITED, re-measured on 56 refs

INHERITED from `MIRROR-PROCESS-AUDIT-MODEL-001` § T-7 and re-run this session at a larger ref
population: **no repository name for the concept, on any ref**, while C.2 already makes its
antidote mandatory — `WHAT_WOULD_CHANGE_MY_MIND (falsificatore dichiarato, obbligatorio)`.
Premature closure is precisely the state of having no answer to that field while the question is
still open. **Annex C is ahead of the framework on this class.**

### PA-4 · 🆕 The per-finding falsifier exists in one arm and not the other, and that is not the declared variable

Measured against `OUTPUT_SCHEMA.md` (`main`), which is **byte-identical in both surfaces**:

```
BOTH ARMS, per claim candidate (§3)
  **Uncertainty:**            "what is not settled, and by what"     ← the second clause is the
                                                                       nearest MODE A falsifier
  **Limitations:** · **Contradictory evidence:** ("none found — searched: <what>")

MODE B ONLY, per critical finding (§5 — output/critical_reading.md)
  **What would resolve it:**  "the experiment, the statistic, the panel, or the datum"
```

🔴 **The explicit per-finding falsifier is a MODE B artifact.** MODE A carries `Uncertainty`'s
*"and by what"*, which is falsifier-shaped and is per *claim*, not per *finding*, and is one
clause rather than a named field. So the class § 2 asks Mirror to audit — premature closure — is
instrumented at different granularity in the two arms, and §0's *single declared variable* is the
mode directive, not the falsifier granularity.

**This is not a defect claim.** MODE B has a second half and MODE A does not, so the asymmetry
follows from the design. What it means for the audit is narrow and exact: **a premature-closure
finding is not comparable across arms**, and reporting it as though it were would read a property
of the output schema as a property of the reader. §8.5 already forbids the composite that would
hide it — *"No overall score. No weighting."*

---

## 3 · FAILURE TAXONOMY

### FT-1 · 🔴 "Unresolved disagreement" is not a failure class, and four normative clauses say so

The dispatch lists it fifth among failures to classify. Measured — every occurrence of
`DISAGREEMENT_UNRESOLVED` under `framework/ governance/ roles/`, on both refs, quoted in full:

```
GOVERNANCE_v3.1.1.md:333      "INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED con spiegazione
                               è esito legittimo; la sintesi forzata è un errore."
annex_c_review_protocol.md:50 "DISAGREEMENT_UNRESOLVED con spiegazione è esito legittimo."
roles/scientist.md:55         "Forced consensus is an error. INFERENCE_A + INFERENCE_B +
                               DISAGREEMENT_UNRESOLVED, explained, is a legitimate outcome."
controlled_benchmark_ab.md:675 (main, §8.3)  "…is a legitimate outcome (body §27)."

files classifying it as a failure, anywhere, on any ref:   0
```

🔴 **The governance names the opposite thing as the error, and names it in the same sentence:
*la sintesi forzata è un errore*.** An audit that scores unresolved disagreement as a failure
creates pressure toward the one outcome three of these four clauses prohibit. And §8.3 makes the
disagreement a *deliverable* — `comparison/unresolved_disagreements.md`, *"listed, typed,
unresolved"* — so at BENCH-AB-001 the class the dispatch would flag is a file the protocol
requires someone to produce.

**Where a real failure hides nearby, and it is a different object:** an unresolved disagreement
**without** the explanation, or one that never reaches `unresolved_disagreements.md`. The clause
is *con spiegazione*, and the qualifier is the whole content. That is a process finding, it
survives the retraction test, and it is Mirror's.

### FT-2 · 🆕 Two of the five classes name nothing, and both have exact referents

```
'infrastructure failure'   mirror 0   main 0
'governance failure'       mirror 0   main 0
```

Neither is a gap in the governance; both are gaps in the vocabulary. The referents:

| Dispatched class | What it already is | Where |
|---|---|---|
| **Infrastructure failure** | the six guarantees LEGEND does **not** possess, each with its compensating protocol — atomic task checkout · exactly-once delivery · transactional state with replay · automatic failure detection and restart · runtime-enforced RBAC · guaranteed singleton | **J.0**, a normative table, with the standing rule: *"Vietato a qualsiasi documento o attore descrivere questi meccanismi con vocabolario più forte del protocollo compensativo"* |
| | plus, at the instruction level: *"delivery/runtime failure? (turno troncato, permission prompt, crash, sessione degradata)"* | **F.4 step 1** |
| **Governance failure** | `GOVERNANCE_BLOCK` — *stop + escalation* — the third severity of F.1; and *"task contract ambiguity? (acceptance criteria non verificabili; INTERACTION_MODE incoerente)"* | **F.1**, **F.4 step 3** |

🔴 **J.0's closing rule binds this record and any audit built from it.** Calling any of those
compensating mechanisms a *gate* would describe it in stronger vocabulary than the protocol
supports. They are detections, and this record calls them detections.

### FT-3 · The dispatch's enumeration order is F.4's, inverted — INHERITED, and the inversion is consequential

Annex F.4's ordered elimination, verbatim, with its own closing capitals:

```
1. delivery / runtime failure?     (turno troncato, permission prompt, crash, sessione degradata)
2. context failure?                (rehydration incompleta, generation stale, checkpoint incompatibile)
3. task contract ambiguity?        (acceptance criteria non verificabili; INTERACTION_MODE incoerente)
4. actual refusal?
        ↓
solo (4), ripetuto dopo chiarimento → NON_COMPLIANT → HUMAN_REQUIRED
(1)-(3) → recovery tecnico / chiarimento contratto, MAI insubordinazione
```

```
F.4's order        infrastructure → context → contract → THE ACTOR, last
dispatch's order   THE ACTOR (scientist reasoning), first → pipeline → infrastructure → governance
```

INHERITED, `LABORATORY-QUALITY-GATE-MODEL-001` § AQ-1: *"the actor is the LAST hypothesis, and the
annex says so in capitals of its own."* 🆕 as applied here: **the dispatch's list is that ordering
reversed**, and AQ-4 measured why it matters — the durable state supports exactly one of the three
attributions, so *"the only layer that can be examined is the only layer that gets blamed."*
Re-verified this session at the larger ref population: 0 event ledgers, 0 task contracts for either
scientist, 0 `active_lessons/`, `REVIEW_YIELD` never computed.

**Enumeration order is not a rubric**, and this record adopts none. What is recorded is that an
audit that walks the dispatch's list in the order given reaches the actor before it has asked
whether the two layers beneath it failed — at a pilot where, per body §38, `CONFIGURED != PROVEN`
and every declared capability of both roles reads `UNVERIFIED`.

### FT-4 · Every class has a Mirror half and a Scientist half — INHERITED, restated over five

INHERITED from `MIRROR-PROCESS-AUDIT-MODEL-001` § TAXONOMY, whose seven-class table established
the shape: *"The seven classes do not divide into 'Mirror's' and 'not Mirror's' — **each one has a
Mirror half and a Scientist half**, and the halves are asked about different objects."*

| Dispatched class | Process form — Mirror's | Truth / ownership form — routed away by C.4 or H.1 |
|---|---|---|
| Scientist reasoning failure | was the discipline followed; is the claimed `Type` the one the audited evidence bears; is each axis's search visible | is the inference correct → `INFERENCE → peer Scientist` |
| Pipeline failure | did the transfer leave its record; was the freeze taken before the content was read; is the handoff block complete | — (mechanical; Plan's rows in §8.2) |
| Infrastructure failure | did a J.0 compensating protocol run, and did it leave the evidence it promises | did the runtime in fact drop the turn → not decidable from the record |
| Governance failure | was the floor met, the reviewer declared, the challenge adjudicated with rationale | should the rule be different → G.2, and not Mirror's alone |
| Unresolved disagreement | 🔴 **not a failure** — see FT-1. The process form is: *was it explained, typed and carried to `unresolved_disagreements.md`* | which reading is right → R2/R3, opened by Orchestrator, **outside** the benchmark record (§5 step 10) |

`NOT ADOPTED. NOT A RUBRIC. NOT SCORED. NOT ORDERED BY SEVERITY.`

---

## 4 · BLIND SPOTS

### BS-1 · Two bars, disjoint, with different remedies — INHERITED

INHERITED, `LABORATORY-QUALITY-GATE-MODEL-001` § AB-4, and applied to this dispatch's three
destinations rather than re-derived:

```
BARRED BY AUTHORITY   Mirror could reach the conclusion from evidence it has, and may not act on
                      it. Remedy: a route
BARRED BY EVIDENCE    Mirror holds the authority and cannot reach the conclusion at all, because
                      the observable does not exist or is not on this ref. Remedy: an
                      instantiation of an object the annexes ALREADY specify
```

Conflating them is the error: authority problems routed to an Orchestrator who cannot supply
evidence, or evidence problems answered by Mirror building an instrument G.2 bars it from adopting.

### BS-2 · 🆕 Requires a peer Scientist — and the seat has never been occupied

C.4 assigns it: `EVIDENCE → Scientist + Plan/provenance · INFERENCE → peer Scientist · SYSTEM →
Mirror`. Measured across the review corpus this session (52 files, all under `reviews/mirror/`):

```
reviewer:      mirror        36 of 36 declared          0 rotations, ever
author:        plan          20 · orchestrator 2 · 🔴 scientist 0
adjudicator:   operator      28 · orchestrator 4
level:         R4            31 of 31 declared          one rung of six
verdict first token:         REQUEST(CHANGES) 17 · ACCEPT 7 · other 9
refs with a scientist in ANY review seat:   0     (control: `author: plan` on 18 refs)
```

C.3 requires *"rotazione; mai coppie fisse"* and, for important reviews, `AUTHOR ≠ REVIEWER ≠
ADJUDICATOR`. With one reviewer the rotation constraint is satisfied and buys nothing — INHERITED,
`EPISTEMIC_REVIEW_MODEL-001` § IND-4. 🆕 what this session adds is the **author** and
**adjudicator** sides: the seat C.4 routes every inference question to has never held anyone, and
the two actors who would hold it — `scientist-a`, `scientist-b` — are unregistered skeletons in
`runtime/agent_card_registry.md` (`orchestrator`), which records *"Two Scientists remain
unregistered and their cards remain skeletons"* and, above it, `CONFIGURED != PROVEN`.

**So "this requires a peer Scientist" is, today, a route to an empty chair** — which is a
different statement from "this is outside Mirror's authority", and BS-1 is why the two must not be
merged.

### BS-3 · Requires the Orchestrator — by authority, and one act by assignment

```
H.1   Task / priorità / riassegnazione / generation          → Orchestrator
H.1   Livello Ladder (≥ floor) e reviewer                    → Orchestrator
H.1   Aggiudicazione challenge (con rationale)               → Orchestrator
C.3   "Apertura solo via Orchestrator"                       → no review opens without one
G.2   step 3, the independent reviewer                       → chosen by Orchestrator
§5 step 2 (main)  the two Task Contracts                     → Orchestrator, lease ACTIVE
§5 step 10        scientific disagreement → R2/R3            → Orchestrator, outside the record
```

Plus the one act that is assigned to no step at all — the C-4 inspection (§ IB-6, and v2 § B-6).
Whether it belongs to Plan's step 6 (*mechanical checks*) or Mirror's step 8 (*whether the design
held*) is not settled by the text; both readings are available and it selects neither.

Mirror holds **no command** over any actor and produces **no primary evidence** (`roles/mirror.md`);
its review of Orchestrator is *ex post* and pattern-based, never a veto before the fact (F.3).
Derived this session: `ACTIVE by derivation: 0`.

### BS-4 · Requires the human operator — including this record's own subject

```
H.1   Spese / MAJOR approval / governance   ·   Strategia complessiva      → Operatore
G.2   "se governance → operatore"
G.2   Mirror NON auto-approva: rubrica di review; learning clustering; active-learning selection
      (incl. budget E.5); review-yield methodology; autonomy-classification methodology
```

🔴 **An execution model for Mirror's own auditing is a review-rubric object.** Mirror may write
the analysis; Mirror may not adopt it. And the route by which anyone else could is blocked in the
middle: G.2's step 3 — *an independent reviewer chosen by an Orchestrator* — has no occupant, and
steps 2 and 4 have working precedents. Measured: `MIRROR_UPGRADE_PROPOSAL` appears as a token in
25 files and has been **instantiated as an object 0 times** (INHERITED · `MIRROR-PROCESS-AUDIT-MODEL-001`
§ LL-1, re-verified).

### BS-5 · What no seat can determine, stated as the protocol states it

The residuals the protocol declares about itself, and which no audit closes:

```
§2.1 (main)   an actor can read outside its surface by absolute path — "Nothing prevents it"
§2.1 (main)   the model may carry the paper from training — "Uncontrollable"
§4.4 (main)   "What no combination of them establishes is authorship of bytes at the one colliding
              path, and none of the three is to be described as if it did"
§4.3 (main)   "a change to an allowlisted input applied identically to both surfaces, which parity
              cannot see" — with the repair named and deliberately not made: "build --emit-digests
              already records per-file input digests and verify does not consume them"
§0 (main)     mode, session variance and paper region are not separable at n=1
```

🔴 **Mirror must not close any of these by judgement.** v2 § FQ-7 states the reason and it is not
improved by restating: the protocol declares them before anyone has a motive to wish otherwise,
and an adjudication that resolved one would supply a distinction the design cannot support.

---

## 5 · LEARNING EXTRACTION

### LE-1 · 🆕 The dispatch's three tiers are E.1 with the terminal states dropped

Annex E.1, verbatim:

```
OBSERVED → LOCAL → PROVISIONAL → VALIDATING → PROMOTED | REJECTED | SUPERSEDED | EXPIRED
```

| Dispatch tier | E.1 state(s) | What the mapping costs |
|---|---|---|
| **observation** | `OBSERVED` | — |
| **lesson** | `LOCAL` → `PROVISIONAL` | E.3's field set is lost: `SUCCESS_CRITERION`, `FAILURE_CRITERION`, `EXPIRY`, `ROLLBACK`, and *"Mai provisional per sempre"* |
| **reusable improvement** | `VALIDATING` → `PROMOTED` | E.4's preregistration is lost: *"Preregistrare `prediction / metric / falsifier / rollback`"* |
| — | 🔴 `REJECTED` · `SUPERSEDED` · `EXPIRED` | **no tier corresponds to any of them** |

🔴 **The dispatch asks for a learning route that does not create an uncontrolled memory layer, and
the three states it omits are exactly the ones that prevent one.** A ladder whose top rung is
`PROMOTED` and which has no rung for `EXPIRED` is a store that only grows. E.1's terminal branch is
not decoration; it is the mechanism.

### LE-2 · 🆕 The anti-uncontrolled-memory mechanism is fully specified, provisional, and its expiry clock has no tick

E.5 is the clause the dispatch's condition names, and it is already written:

```
RAW ARCHIVE → Mirror clustering → ACTIVE LESSONS → role-specific subset → rehydration

GUARANTEE (1)  RAW archive lossless — "il clustering non cancella mai i record originali"
GUARANTEE (2)  every ACTIVE_LESSON carries derived_from: [LEARN-###, …] — "Mirror non riscrive la storia"
BUDGET         "ogni subset role-specific ha un budget dimensionale definito da Plan"; overflow →
               Mirror compresses or demotes, never touching the RAW
```

The budget exists. `governance/plan_defined_parameters.md` § P6, read this session:

```
PER_ROLE_SUBSET_BUDGET: 25 lessons OR 4 000 words, whichever binds first   [PROVISIONAL]

§ P6.1 · Registered as PROVISIONAL (Annex E.3)
  PRACTICE_ID:        PROV-LESSON-BUDGET-25
  SUCCESS_CRITERION:  no recurrence of a pattern whose lesson was demoted for budget
  FAILURE_CRITERION:  a demoted lesson is followed by the failure it described
  EXPIRY:             at the second MIRROR_RETROSPECTIVE — PROMOTE | REJECT | EXTEND_WITH_REASON
  ROLLBACK:           budget suspended; full ACTIVE_LESSONS set loaded until recalibrated
```

🔴 **`EXPIRY` is pinned to the second `MIRROR_RETROSPECTIVE`, and the retrospective cadence `N`
does not exist.** `governance/ANNEX_INDEX.md` records G.3's `MIRROR_RETROSPECTIVE ogni N batch` as
**UNASSIGNED** by the annexes; `APPROVAL-GOV311-DEVIATIONS.md` § ESC-3 records why, verbatim:

> `MISSING AUTHORITY: The annexes assign N to nobody. Plan declined it because G.2 places
> retrospective methodology inside Mirror's own method. Mirror declined it for the same reason:
> G.2 forbids Mirror from self-approving changes to its own retrospective methodology.`
> `BLOCKS: nothing. Retrospectives cannot run before there are batches to retrospect.`

and the operator carried it forward in the approval ledger, appended as a new line rather than by
editing the pending one:

> `"CARRIED_UNRESOLVED":[{"id":"ESC-3","item":"MIRROR_RETROSPECTIVE cadence parameter N",`
> `"state":"UNRESOLVED","note":"Carried forward by explicit operator decision. No numeric value`
> `introduced. Blocks nothing: retrospectives cannot run before there are batches to retrospect."}]`

So: **the mechanism that prevents an uncontrolled memory layer is a PROVISIONAL practice whose
scheduled review is bound to an event whose cadence two actors have each declined to set, each
citing the same clause.** v2 § L-4 recorded that ESC-3's stated basis lapses when the pilot
produces the first batch to retrospect. 🆕 what this adds is the second thing that lapses with it:
`PROV-LESSON-BUDGET-25`'s expiry, and with it E.5's overflow behaviour, has been waiting on the
same unset number.

**No value is proposed here.** Setting `N` is reserved, twice over — by G.2 and by an explicit
operator decision.

### LE-3 · 🆕 Where a pilot finding would actually land today — mentions are not objects

Measured this session on `mirror`, and across all 56 refs where marked:

```
learning/mirror/ records                                       39      ← the RAW archive, de facto
files mentioning LEARNING_INDEX (learning/, ledger/)           19      ← ALL of them Mirror's own records
refs carrying a file whose NAME is a learning index             0      🔴 mentions ≠ object
refs carrying active_lessons/                                   0      of 56
MIRROR_UPGRADE_PROPOSAL — token in N files                     25
                        — instantiated as an object             0      INHERITED, re-verified
ledger/ total files                                            16      1 approval queue · 1 task (plan) ·
                                                                       6 plan checkpoints · 8 mirror checkpoints
refs carrying ledger/events/ or ledger/consolidated/            0      of 56
```

The event ledger is not merely unbuilt — it is **designed and unbuilt**. `plan_defined_parameters.md`
§ P7 decides it: option (a), `ledger/events/<ACTOR_ID>.jsonl` per actor, JSON Lines, append-only,
consolidated by Plan into `ledger/consolidated/`, reusing the existing hash-chained append-only
machinery — and closes *"Tracked as a debt; not yet built."* `roles/mirror.md` names that ledger
Mirror's **primary analysis surface** and lists `Event ledger analysis` among Mirror's declared
capabilities with status *"blocked: the ledger has no writer yet"*.

🔴 **The current state is RAW-only.** E.5's chain is `RAW ARCHIVE → clustering → ACTIVE LESSONS →
role-specific subset → rehydration`, and only the first link exists. That configuration is
lossless by construction and unretrievable by design: nothing selects from the 39 records at
rehydration, so a lesson recorded in one is available to a future session only if that session
happens to read the file. **An uncontrolled memory layer is one failure mode of a learning store;
an unread one is the other, and it is the one currently instantiated.**

### LE-4 · The three thresholds already exist, and none of them is Mirror's alone to apply

```
E.2   BEST_PRACTICE_CANDIDATE threshold: "≥2 conferme delle prime due classi, o 1 + validazione
      Mirror". Only ORIGINAL_OBSERVATION and REPLICATION count fully; EXPOSURE_AFTER_BROADCAST
      does not
E.2   Dedup: "simile esistente → conferma con classe". Conflicts → Mirror adjudicates →
      SUPERSEDED motivato
E.5   Material changes to clustering or selection = MIRROR_METHOD_CHANGE (G.2)
```

Applied to the pilot, the n=1 boundary INHERITED from v2 § L-2 governs what any of them may carry:
one instance licenses an **existence** claim (*this gate can be violated and pass*; *this field was
ambiguous to a reader*) and licenses **no** comparative or frequency claim. E.2's own arithmetic
agrees: a single session yields **one** `ORIGINAL_OBSERVATION`, which is below the two-confirmation
threshold unless Mirror validates it — and *"1 + validazione Mirror"* is the branch that turns the
pilot's findings into practice, which is precisely the branch G.2 bars Mirror from designing for
itself.

---

## 6 · FIRST PILOT OUTPUT

### PO-1 · "Not a score" is already the rule, in two places — QUOTED

```
§8.5 (main)   "No overall score. No weighting. Each dimension its own table, A and B side by side,
               with the route that produced each number… Every count is an enumerated set or
               carries the command that produced it."
§8.5 (main)   agreement between A and B is descriptive and "is not a quality measure — two readers
               agreeing on an overshoot is two overshoots"
§8.4 (main)   TIME · TOKEN/CONTEXT · OUTPUT VOLUME: "They are not combined with anything, they do
               not break ties, and a reading is not 'better' for being faster, shorter or cheaper"
```

The dispatch's constraint is the protocol's constraint. Nothing needs to be added to honour it.

### PO-2 · 🔴 The five questions are not the C.2 format, and C.2 calls itself the only one

Annex C.2's heading is `Formato unico`. Mapping the dispatch's five questions onto it:

| Dispatch question | C.2 field it is | Note |
|---|---|---|
| **What worked?** | `STEELMAN` | 🆕 and the dispatch independently recovers C.2's ordering rule: *"STEELMAN (obbligatorio, **prima delle obiezioni**)"*. Putting it first is not a stylistic choice in this repository |
| **What failed?** | `KEY_OBJECTIONS` + `EVIDENCE_AGAINST` | two fields, not one |
| **Why?** | — | 🔴 **no C.2 field.** The nearest normative instrument is **F.4's ordered DIAGNOSE**, which belongs to non-compliance, not to review |
| **Would this failure repeat?** | — | 🔴 **no C.2 field.** Nearest: E.2's `CONFIRMATION_CLASSES` (a second instance is a `REPLICATION`) and G.2's `PREDICTION` |
| **What should change before scaling?** | — | 🔴 **not a review field at all.** It is `MIRROR_UPGRADE_PROPOSAL` — a separate object, on a separate route, that Mirror may not self-approve (G.2) |

**And the fields with no question — thirteen of them:**

```
REVIEW_ID · OBJECT · LEVEL · REVIEWER · AUTHOR · ADJUDICATOR
ALTERNATIVES_CONSIDERED · VERDICT · REVIEWER_CONFIDENCE
RESIDUAL_UNCERTAINTY · EVIDENCE_NEEDED · WHAT_WOULD_CHANGE_MY_MIND · AUTHOR_RESPONSE
```

🔴 **`WHAT_WOULD_CHANGE_MY_MIND` is among them, and it is the antidote to the very class § 2 asks
Mirror to audit.** § PA-3 measured that premature closure has no name anywhere in this repository
and that C.2's mandatory falsifier is its only instrument. A first report that audits premature
closure while carrying no falsifier of its own commits, at the meta level, the defect it was sent
to look for. `ALTERNATIVES_CONSIDERED` and `RESIDUAL_UNCERTAINTY` are in the same list, and
`MIRROR-PROCESS-AUDIT-MODEL-001` § F-2 already recorded why that matters: four of its seven failure
classes have a mandatory C.2 field, so a review written to the format *cannot omit them silently* —
it can only leave them empty, which is visible. **A report written to the five questions can omit
them invisibly.**

Measured, so the claim is about practice and not only about text — C.2 field occupancy across the
52 reviews in `reviews/mirror/`:

```
STEELMAN 31 · WHAT_WOULD_CHANGE_MY_MIND 31 · AUTHOR_RESPONSE 30 · REVIEWER_CONFIDENCE 22 ·
RESIDUAL_UNCERTAINTY 22 · EVIDENCE_NEEDED 21 · EVIDENCE_AGAINST 15 · KEY_OBJECTIONS 14 ·
EVIDENCE_FOR 14 · ALTERNATIVES_CONSIDERED 13         (frontmatter seats measured separately, BS-2)
```

The format is in use. It is not a form nobody fills in.

**The reading this record works under**, and it is subtractive rather than additive: the dispatch's
five questions are a **legible ordering of C.2's existing fields**, not a replacement for them —
`What worked` before `What failed` *is* C.2's steelman-first rule — and the two questions with no
C.2 home are two different objects (`Why` → F.4's diagnostic ordering; `What should change` → a
G.2 proposal that leaves the review entirely). Adopting anything narrower would be a new review
standard, which the dispatch forbids and G.2 bars.

### PO-3 · 🆕 The ten-step sequence has no AUTHOR_RESPONSE step

C.2 makes it mandatory and states the reason in four words: `AUTHOR_RESPONSE (obbligatoria; il
silenzio non è accettazione)`. `roles/scientist.md` repeats it for peer review: *"`AUTHOR_RESPONSE`
is mandatory — silence is not acceptance."*

Read against §5 (`main`):

```
step 8   Mirror        adjudication → reviews/mirror/BENCH-AB-001-ADJUDICATION.md
step 9   Plan          outcome summary — every dimension separately, no composite
step 10  Orchestrator  scientific disagreements → Annex C review, OUTSIDE the benchmark record
```

🔴 **No step returns the adjudication to any author, and the sequence ends.** The field exists in
30 of 52 existing reviews, so the practice is established; what has no step here is the act. Under
C.2 read literally, a step-8 adjudication with no author response is an incomplete review — and
the incompleteness would be structural rather than anyone's omission.

### PO-4 · 🆕 For a process object, `AUTHOR` is not one actor

C.2's header line names one `AUTHOR`. The object at step 8 is *the process*, which spans steps 1–7
and three actor classes: Plan built the surfaces, froze both trees, ran the mechanical checks and
built the comparison; two Scientists produced the readings; fresh blind agents produced the audits.

Measured: no review in the corpus has ever had a Scientist in any seat (0 refs), and the
single-author assumption has already been strained once —
`reviews/mirror/REV-LEGEND-LAB-ARCHITECTURE-001.md` carries `author: two records by two distinct
sessions — see OBJECT`.

And the third seat: C.3 requires `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` for important reviews, and R4 is
important by construction. The six REV-SCIAB reviews resolve it by escalation — every one reads
`adjudicator: operator (MAJOR → HUMAN_APPROVAL, Annex J.3) — none granted or implied here`. For
step 8, H.1 would put adjudication with Orchestrator, and `ACTIVE by derivation: 0`.

**Recorded as an observation about a format applied to a new kind of object.** Which actor answers
for the process, or whether several do, is an assignment; assignments are Orchestrator's under H.1
and are not made here.

---

## FQ · THE FINAL QUESTION

> *"After the first pilot, what can Mirror know that Scientist A and B cannot know about
> themselves?"*

### FQ-1 · This is a third question, and the difference from the other two is the direction

```
LABORATORY-QUALITY-GATE-MODEL-001   "Scientist | pipeline | laboratory?"    — three ways to fail
SCIENTIFIC-PROCESS-AUDIT-v2-001     "science or system?"                    — two, one of them null
this dispatch                       "what does the audit's seat see that the audited seat cannot?"
```

The first two ask **what failed**. This one asks **what is knowable from where**, and it has an
answer even when nothing failed. Their findings are used below and attributed; neither answers it.

### FQ-2 · The honest first move is to bound the question with the dispatch's own § 1

§ 1 of this dispatch excludes **hidden scientist reasoning before freeze** from Mirror's bundle. So
whatever Mirror can know, it is not what happened inside a reading while it was happening. **The
answer is therefore not "more" — it is "elsewhere".** Every item below is a fact located in another
arm, in an object outside the surface, or after the reader's own stopping point.

### FQ-3 · 🆕 The denominator was frozen before either read, and it is in neither surface

`population/evidence_units.json`, read this session at `main`:

```
65 evidence units · 109 sub-units (panels)
  main_figure 6 · main_results_section 7 · main_methods_section 2 · main_table 0 (measured — the
  paper prints none) · supplementary_figure 10 · supplement_methods_section 24 ·
  supplement_table_section 7 · source_data_blot 9
digest recorded in the frozen manifest, so it "cannot be redefined after the readings exist" (§8.1)
```

And the surface allowlist, enumerated from `surface_spec.json` this session:

```
11 common_files · 7 source_files · 2 per_actor_files · 4 empty output dirs
🔴 population/evidence_units.json is in NONE of them — 0 occurrences of "evidence_units" anywhere
   in the spec's allowlist
```

**Neither reader knows the denominator.** Coverage — *"units of the population with ≥1 locator
anchored in them, per reader; units touched by one reader only"* (§8.2) — is computable only from
outside the reading, and it is computed there: the row's evaluator is Plan, with Mirror adjudicating
substance. A reader can know what it covered. **It cannot know what it missed**, because the list
of what there was to miss was deliberately withheld — and §8.1 says why in one clause: the
population *"does not say which units matter — that is exactly what the two readings and the
adjudication will disagree about, and it must not be pre-empted."*

### FQ-4 · 🆕 Two receipts exist per reader — one attested, one measured — and they are different objects

```
output/receipt.json                    written by THE READER, before freeze
  coverage map · supplements_covered · renders · validator{command, verdict_line, exit_code}
  self_check{locators_inside_surface, no_not_read_in_coverage, all_claims_typed,
             negatives_carry_premise_and_revival_trigger, mode_b_axes_all_answered}
  blockers[] · contamination_declared[]
  — "Every value is a fact you checked, not an intention" (OUTPUT_SCHEMA §4)

frozen/RECEIPT-<ACTOR_ID>.json         computed by PLAN, at freeze, before reading the content
  TREE_SHA256 · FILE_COUNT · FILES[] with role ∈ input · output · unexpected
  OUTPUT_FILE_SET and UNEXPECTED_FILE_SET enumerated separately
  SURFACE_COMMIT · SURFACE_BRANCH · SURFACE_DIRTY · FREEZE_TIMESTAMP_UTC · FIRST_PASS_STATE
  identity read FROM INSIDE the tree; "a disagreement is a refusal, exit 2"
```

The first is an **attestation**; the second is a **measurement of the same tree**, taken after the
reader stopped. Only a seat downstream of the freeze holds both, and the comparison between them —
*does the self-check survive the census* — is unavailable to the actor who wrote the self-check,
not because it was hidden but because the second object did not exist yet.

The same shape governs the census: `verify --post-read` prints `[UNCHECKED]` per actor with six
classes (`blind_spot`, `scan_exempt_present`, `undecodable_prefix`, `scan_exempt_input`,
`suffix_not_scanned`, `undecodable_text`), each line carrying the path, the class, the reason,
whether the skip is *a consequence this protocol declares*, and which checks did still run. **No
reader has a census of its own surface.**

### FQ-5 · 🆕 Blindness is not something a reader can do to itself

Step 7 spawns fresh blind agents over *"every (proposition, snippet, anchor) triple of both
readings, reader identity withheld"*, and it runs **after** step 5's freeze. The verdict vocabulary
is `SUPPORTED · OVERSHOOT · UNDERSHOOT · NOT_IN_SOURCE · UNVERIFIABLE_SURFACE`.

The skill that supplies those agents states its own active ingredient, and it is quoted in
`EPISTEMIC_REVIEW_MODEL-001` § IND-1: *"Knowing the author makes a reviewer reconstruct intent
instead of testing behaviour. **Blindness is the active ingredient, not the ceremony.**"*

🔴 **A reader auditing its own locators is, necessarily, not blind.** The audit's verdicts on a
reading's own triples are structurally unavailable to that reading *before it freezes*, and the
protocol makes that ordering explicit rather than incidental: §5's steps run 5 → 6 → 7, and §7
forbids the frozen record from absorbing anything that follows — *"corrections after freeze go in
a separate dated file and are reported as corrections."*

### FQ-6 · The other arm — and the limit of what the pair licenses

Neither reader sees the other's first pass until both are frozen (§7); MODE B is instructed not to
*"attempt to reconstruct what the other reader concluded"*; each ran exactly one arm. Mirror is
downstream of both frozen trees and of `comparison/comparison_matrix.md`, whose rows align claim
candidates *"by shared locator anchors… structural, by unit, not by Plan's reading of whether two
claims 'mean the same'"*.

⚠️ **And here the answer must stop short of where it wants to go.** §0's first caveat is exact:
*"With one paper and one session per actor, the benchmark cannot separate the effect of the mode
from the variance between two sessions."* So what Mirror can know is that **a difference exists,
and where** — which units one reader anchored and the other did not, which claims one carried and
the other did not, which axis one answered and the other left silent. What Mirror cannot know is
**why**, and §0's second caveat narrows it further: each reader can read the other's mode directive
in a common file, so the manipulated variable is only *which directive is addressed to you* — a
contamination the protocol records against Mirror's own finding id, `R-2`.

Nor is Mirror alone in this seat: step 6 gives Plan the comparison matrix and the unresolved-
disagreement list. The seat that is uniquely Mirror's is not *seeing both* — it is the substance
adjudication on six of §8.2's ten rows. **The readers are the only actors excluded, and that is
the question's actual subject.**

### FQ-7 · The answer, and its exact converse

**What Mirror can know that A and B cannot know about themselves — five things, and they share
one shape:**

```
1  what it missed          the 65-unit population was frozen before it read and withheld from its
                           surface. A reading knows its numerator, never its denominator
2  whether its locators    the blind audit runs after the freeze, and blindness is not
   bear their propositions  self-administrable
3  whether its attestation the self-check is written by the reader; the tree census is computed by
   survived measurement    Plan afterwards. Two objects, one of them later
4  which of its own files  the [UNCHECKED] census, six classes, per actor, on a surface the reader
   were never scanned      never enumerated
5  that a difference from  visible only where both frozen trees coexist — and, per §0, attributable
   the other arm exists    to a difference, never to a cause
```

🔴 **Every one is a fact about a reader that the reader is structurally barred from holding.** Not
withheld out of caution, and not a failure of the reader's diligence: each is located in another
arm, in an object outside the surface, or after the reader's own stopping point. **A blind spot is
by definition not visible from the seat that has it, and this benchmark manufactures five seats
from which each reader's blind spots are visible.** That, and not adjudication authority, is what
step 8 is for.

**And the exact converse, which the dispatch's own § 1 makes permanent.** What A and B know that
Mirror cannot: what they read and did not cite; what they considered and rejected without recording
it; whether an absent locator means *not read* or *read and judged irrelevant*. The protocol has
exactly one partial instrument for it — `found_or_sought`, *"'sought — …' or 'found — …', one
clause on how you came to it"* — and it fires only for the quotes that made it in. **The reading's
negative space is the readers' private knowledge**, and § 1's exclusion of pre-freeze reasoning
makes it permanently so. That is a design choice with a cost, and the cost is § IB-6.

**And the same question, turned on this seat.** *What can A and B know about Mirror that Mirror
cannot know about itself?* Measured, the answer is: nothing, because no one is looking.

```
reviewer: mirror                36 of 36 declared          0 rotations, ever
level: R4                       31 of 31                   one rung of six
REVIEW_YIELD computed           0 times, 56 refs           G.3's own ritual detector
G.2 step 3 (independent reviewer chosen by Orchestrator)   no occupant
```

The five asymmetries above exist because the design put a second seat downstream of the first.
**There is no second seat downstream of Mirror.** INHERITED in its parts from
`EPISTEMIC_REVIEW_MODEL-001` § IND-2 and § IND-4; stated here because a record that answers *what
can the auditor see that the audited cannot* and does not ask it of the auditor has answered half a
question.

---

## BLOCKERS

> Blockers to the model's **execution**. Nothing below is assigned; Mirror holds no command.

```
B-1  THE EXPERIMENT HAS NOT RUN. 0 output paths across 6 output directories, 56 refs; 0 task
     contracts for either scientist; 0 freeze receipts; 0 audits. Everything above is ex ante

B-2  THE PROTOCOL AND ITS TOOLING ARE NOT ON THIS REF. controlled_benchmark_ab.md,
     scientist_reading_modes.md, benchmark_input_surface.py and BENCH-AB-001/ read from `main`.
     Positive control: failure_taxonomy.md IS on `mirror`. (Protocol absence INHERITED · v2 F-0;
     the tooling is 🆕)

B-3  MIRROR'S INPUT BUNDLE IS UNDECLARED AND UNVERIFIED (§ IB-1, IB-2). 0 of 7 subcommands take
     Mirror's record as an object; the durable seat holds a pointer and a digest

B-4  THE BENCHMARK IS BLOCKED. Protocol §9: "BLIND FIRST PASS — BLOCKED BY CANONICALIZATION", and
     independently by P-2…P-4. scientist-a and scientist-b unregistered; L2 SUSPENDED by the C-9
     hold; every declared capability of both roles UNVERIFIED

B-5  NO ORCHESTRATOR. 0 ACTIVE leases derived; lease #3 EXPIRED_WITHOUT_RENEWAL and its stored
     status disagrees with the derived one. C.3 bars opening a review; §5 step 2 bars issuing the
     contracts; G.2 step 3 bars routing any proposal

B-6  NO EVENT LEDGER, ON ANY REF — and it is DESIGNED (P7) rather than merely absent.
     roles/mirror.md names it Mirror's primary analysis surface, capability status "blocked: the
     ledger has no writer yet"

B-7  THE C-4 INSPECTION IS ASSIGNED TO NOBODY, AND § 1 WOULD EXCLUDE ITS EVIDENCE (§ IB-6).
     INHERITED · v2 B-6 for the first half

B-8  THE PILOT'S OWN LEARNING ROUTE TERMINATES. E.5's chain has one link built; PROV-LESSON-BUDGET-25
     expires at an event whose cadence N is UNRESOLVED by explicit operator decision; 0
     MIRROR_UPGRADE_PROPOSAL objects; REVIEW_YIELD never computed
```

---

## OPEN_QUESTIONS

```
Q-1  Does C.3's "reviewer senza evidenza contribuita" reach a reviewer who contributed eight
     repairs to the design under review (§ IB-5)? The clause reads most naturally as being about
     contributed EVIDENCE; design corrections are a different kind of contribution and arguably a
     heavier one. Not answerable by Mirror about Mirror

Q-2  Which of the 24 paths on `mirror` that name the paper may the adjudication consult, for which
     purpose (§ IB-3)? The process/content distinction is stated there; nothing declares it binding

Q-3  Who is the AUTHOR of a process object spanning three actor classes, and who adjudicates a
     review whose reviewer is the only declared reviewer in the corpus (§ PO-4)?

Q-4  Does the pre-freeze exclusion admit commit METADATA while excluding commit CONTENT (§ IB-6)?
     Without that distinction the C-4 detection route is closed; with it, the exclusion needs a
     stated boundary that currently exists nowhere

Q-5  Is a premature-closure finding comparable across arms when the per-finding falsifier is a
     MODE B artifact (§ PA-4)? §8.5 forbids the composite; it does not say how to report an
     instrument that exists in one arm only

Q-6  Does the pilot's single session yield an ORIGINAL_OBSERVATION that reaches E.2's threshold
     only via "1 + validazione Mirror" — the branch G.2 bars Mirror from designing for itself
     (§ LE-4)?
```

---

## WHAT THIS RECORD DOES NOT DO

It does not conduct an audit, adopt a rubric, propose a rule, define a report template, or create a
validator. It does not start, authorize, unblock or schedule BENCH-AB-001; it does not lift the C-9
hold, verify a capability, register an actor, take a lease, or issue a task. It does not evaluate
PMID 42397075 — the paper was never opened in this session — and it reaches no conclusion about
WWOX biology. It does not set `N` for `MIRROR_RETROSPECTIVE`, resolve ESC-3, promote or extend
`PROV-LESSON-BUDGET-25`, name the C-4 inspection's owner, declare an admissibility rule for
Mirror's inputs, or decide anything G.2 reserves. It does not amend, supersede or correct
`SCIENTIFIC-PROCESS-AUDIT-v2-001`, `LABORATORY-QUALITY-GATE-MODEL-001`,
`MIRROR-PROCESS-AUDIT-MODEL-001`, `EPISTEMIC_REVIEW_MODEL-001` or any of `REV-SCIAB-MIRROR-001…006`.
It writes one file, under `learning/mirror/`, on branch `mirror`.

---

## EVIDENCE

```
RUN THIS SESSION, 2026-08-22T19:39Z–20:05Z · mirror@da52ee5 · main@788c357 · 56 refs

  framework/scripts/legend_lint.py .                   VERDICT: PASS (1 INFO)
  framework/state/state_manifest_current.md:141        current_state: READY
  lease_state.py --check (script + record from main,   ACTIVE by derivation: 0
    extracted to a scratch tree — both absent here)     #3 EXPIRED_WITHOUT_RENEWAL; stored ≠ derived

  ref sweep, BENCH-AB-001/{first_pass,frozen,          0 · 0 · 0 · 0 · 0 · 0 refs
    comparison,audit,adjudication,outcome}
  ref sweep, BENCH-AB-001/instructions                 18 refs   ← POSITIVE CONTROL
  ref sweep, reviews/mirror/BENCH-AB-001-ADJUDICATION  0 refs
  ref sweep, ledger/events + ledger/consolidated       0 refs
  ref sweep, active_lessons/                           0 refs
  ref sweep, a file NAMED as a learning index          0 refs (19 files MENTION LEARNING_INDEX)
  ref sweep, scientist in any review seat              0 refs (control: author: plan → 18 refs)

  presence, this ref   controlled_benchmark_ab.md · scientist_reading_modes.md ·
                       benchmark_input_surface.py · BENCH-AB-001/       ALL ABSENT on `mirror`
                       framework/eval/failure_taxonomy.md               PRESENT — read here
  presence, collision  deepdive_manifests/PMID42397075.json    PRESENT on mirror AND main

  content sweep, unique ids (42397075|awag239)         main 32 · mirror 24 tracked paths
  content sweep, spec net (+ 4 author surnames)        main 124            ← the two differ ×4
  surface allowlist, enumerated from surface_spec.json 11 common · 7 source · 2 per-actor · 4 dirs
                     population/evidence_units.json    NOT in the allowlist — 0 occurrences
  population/evidence_units.json (read at main)        65 units · 109 sub-units · main_table 0
  forbidden_prior_output_paths                         23, derivation recorded in the spec

  term sweep (framework/ governance/ roles/, both refs)
    'infrastructure failure' 0/0 · 'governance failure' 0/0 · 'inference control' 0/0 ·
    'uncertainty preservation' 0/0 · 'premature closure' 0/0
    DISAGREEMENT_UNRESOLVED  3/5 — every occurrence declaring it LEGITIMATE; 0 as a failure
    controls: PREMISE_TAG 6/6 · REVIVAL_TRIGGER 9/14 · MIRROR_SAMPLED 3/3

  reviews/ corpus (52 files, all under reviews/mirror/)
    frontmatter seats  reviewer: mirror 36/36 · author: plan 20, orchestrator 2, scientist 0 ·
                       adjudicator: operator 28, orchestrator 4 · level: R4 31/31
    verdict tokens     REQUEST 17 · ACCEPT 7 · other 9      (0 C.2 values — INHERITED, re-verified)
    C.2 body fields    STEELMAN 31 · WWCMM 31 · AUTHOR_RESPONSE 30 · REVIEWER_CONFIDENCE 22 ·
                       RESIDUAL_UNCERTAINTY 22 · EVIDENCE_NEEDED 21 · EVIDENCE_AGAINST 15 ·
                       KEY_OBJECTIONS 14 · EVIDENCE_FOR 14 · ALTERNATIVES_CONSIDERED 13
    REV-SCIAB-MIRROR-001…006   reviewer: mirror · author: plan · adjudicator: operator · R4
    Mirror finding ids quoted in the protocol   8 distinct: R-1 R-2 R-8 B-1 B-4 M-2 M-3 M-4
    "mirror" in benchmark_input_surface.py      18 — all finding attributions in comments

  ledger/                       16 files: 1 approval queue · 1 task (plan) · 6 plan + 8 mirror
                                checkpoints. 0 contracts for either scientist
  HUMAN_APPROVAL_QUEUE.jsonl    2 approval ids, both GOV311; ESC-3 CARRIED_UNRESOLVED, verbatim
  plan_defined_parameters.md    P6 budget 25 lessons / 4 000 words [PROVISIONAL];
                                P6.1 PROV-LESSON-BUDGET-25, EXPIRY "at the second MIRROR_RETROSPECTIVE";
                                P7 event ledger design decided — "Tracked as a debt; not yet built"
  runtime/agent_card_registry.md (@orchestrator)   scientist-a, scientist-b UNREGISTERED skeletons
  learning/mirror/              39 records (this file is the 39th); 29 match SLR-mirror-NNNN

  ⚠️  Two instrument notes, both of which changed a number this session:
      (1) A ref sweep in zsh must brace the variable: "${r}:${f}", never "$r:$f" — the bare form
          applies the `:r` history modifier and returns a false ABSENT on every ref. Every sweep
          above used the braced form, each with a positive control.
      (2) Frontmatter keys are LOWERCASE. An uppercase grep for ADJUDICATOR reported 0 in the six
          REV-SCIAB reviews; `^adjudicator:` reports 6 of 6, all `operator`. The first reading was
          a false negative of the instrument, corrected before use.

READ AT `mirror`   GOVERNANCE_v3.1.1.md · annexes C, E, F, G, H, J · plan_defined_parameters.md ·
                   ANNEX_INDEX.md · roles/mirror.md · roles/scientist.md · epistemic_discipline.md ·
                   failure_taxonomy.md · APPROVAL-GOV311-DEVIATIONS.md · the four prior
                   learning/mirror records · REV-SCIAB-MIRROR-001…006 (frontmatter + tails)
READ AT `main`     controlled_benchmark_ab.md (§§0–10) · scientist_reading_modes.md (§§2–3, 5) ·
                   BENCHMARK_INSTRUCTIONS.md · OUTPUT_SCHEMA.md · MODE_A.md · MODE_B.md ·
                   surface_spec.json · population/evidence_units.json ·
                   benchmark_input_surface.py (CLI surface + Mirror attributions)
NOT READ           PMID 42397075, in any surface, in any form. The packet is git-ignored and was
                   never opened. 0 scientific claims assessed
```
