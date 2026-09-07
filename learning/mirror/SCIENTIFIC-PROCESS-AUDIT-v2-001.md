---
artifact: MIRROR analysis record — how Mirror would audit the process quality of the first real
  Scientist experiment, measured against the protocol that already specifies that experiment.
  Learning artefact only
record_id: SCIENTIFIC-PROCESS-AUDIT-v2-001
actor_id: mirror
date: 2026-08-22
task_id: SCIENTIFIC_PROCESS_AUDIT_v2
dispatcher: operator
role: >
  mirror — metacognitive layer. This record reviews no object, names no author, issues no verdict,
  and evaluates no scientific claim. It describes an audit; it does not conduct one. No reading
  exists to audit (§ PRECONDITIONS)
authority: >
  `governance/GOVERNANCE_v3.1.1.md` body §§2, 23–29, 32, 38, 41, 46, 48; annexes A, C, F, G, J;
  `roles/scientist.md`; `roles/mirror.md`; `framework/instruction/epistemic_discipline.md`;
  `framework/eval/failure_taxonomy.md`.
  🔴 AND THREE FILES THAT ARE NOT ON THIS REF. `framework/protocols/controlled_benchmark_ab.md`,
  `framework/protocols/scientist_reading_modes.md` and the whole of
  `framework/eval/benchmarks/BENCH-AB-001/` are ABSENT on `mirror` and were read from `main`.
  Every quotation from them is marked with the ref it came from. That absence is not a caveat
  about sourcing; it is § F-0, the record's first finding.
  Nothing here is adopted or in force. G.2 bars Mirror from self-approving material changes to its
  own review rubric, and an audit model IS a rubric object. Every element is either (a) quoted
  from a named file at a named ref, (b) a measurement run this session, or (c) INHERITED and
  attributed
classification: OBSERVATION AND ANALYSIS — not governance, not a protocol, not a validator,
  not a gate, not a rubric, not a score, not an amendment, not a decision, not an authorization
  to run anything
scope: >
  learning/mirror/ on branch `mirror` only. One new file. No governance/, roles/, framework/,
  ledger/, runtime/, reviews/ or disease-models/ path is written. No existing record is edited,
  superseded or corrected
prior_artefact_disclosure: >
  🔴 MATERIAL AND EXTENSIVE. Two records written earlier TODAY, on this ref, cover adjacent
  ground: `learning/mirror/MIRROR-PROCESS-AUDIT-MODEL-001.md` (the process-audit model, derived
  under an authority restricted to G and C) and `learning/mirror/LABORATORY-QUALITY-GATE-MODEL-001.md`
  (three-layer quality model, whose § ATTRIBUTION answers a THREE-way version of this dispatch's
  final question). `learning/mirror/EPISTEMIC_REVIEW_MODEL-001.md` overlaps in part.
  🔴 AND SIX REVIEWS OF THE EXPERIMENT ITSELF: `reviews/mirror/REV-SCIAB-MIRROR-001…006.md`, this
  seat's own hostile reviews of the candidate that specifies BENCH-AB-001, the last verdict
  ACCEPT / CONFIRMED at revision 6. Several contaminations and defects this dispatch asks me to
  look for were found THERE, are quoted in the protocol by their Mirror finding ids, and are
  marked INHERITED here rather than re-presented as discoveries.
  This record SUPERSEDES NONE of them and CORRECTS none of them. Only items marked 🆕 are new
naming_deviation: >
  DECLARED, TWICE OVER. (1) 29 of the now-38 records under learning/mirror/ match
  `SLR-mirror-NNNN[-ADD|-COR-NNN]`; this filename was specified by the dispatch and departs from
  that pattern, as eight others already do. (2) 🔴 The `v2` in the name succeeds NO v1: no
  `SCIENTIFIC-PROCESS-AUDIT-v1` exists on any of the 55 refs. The nearest prior object is
  `MIRROR-PROCESS-AUDIT-MODEL-001`, whose task_id is `MIRROR_PROCESS_AUDIT_MODEL_v1`. Recorded
  because a version number that indexes nothing is a claim of lineage, and this one is unfilled.
  NO NAMING RULE IS ADOPTED AND NO PRECEDENT IS SET
measured_at: >
  mirror@da52ee5e9d3e6eb66455c61d422c4fb1d0e21391 · main@788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
  · 55 refs · 2026-08-22T19:06Z–19:09Z. Every count below was run in this session against these
  refs. 🔴 The ref population is moving: 53 at 18:04Z, 54 at 18:20Z, 55 now — three counts, three
  records, one day. Numbers taken from another record are marked INHERITED and attributed
---

# SCIENTIFIC PROCESS AUDIT v2 — the experiment is already specified, Mirror's seat in it is already assigned, and the protocol that assigns it is not on Mirror's ref

> **Mirror asks whether the process that produced a result was reliable. It does not ask whether
> the result is true.** The dispatch states this as a premise. Annex C.2 states it as a
> definition — `CONFIRMED` is *"nessun difetto rilevato dato l'evidence bundle disponibile",
> **non "vero"***. The premise is not an exemption Mirror is granted; it is the review protocol
> read literally, and it binds every reviewer.

---

## TASK_STATUS

```
TASK          SCIENTIFIC_PROCESS_AUDIT_v2
DISPATCHER    operator (no ACTIVE lease exists — derived, § PRECONDITIONS)
STATE         COMPLETE for the analysis; NOTHING ADOPTED; NOTHING DECIDED; NOTHING AUTHORIZED
DELIVERABLE   learning/mirror/SCIENTIFIC-PROCESS-AUDIT-v2-001.md — this file, branch `mirror`

THE DISPATCH'S CONSTRAINTS, EACH CHECKABLE
  not scientific truth      0 scientific claims assessed. The test that enforces it is the
                            retraction test, INHERITED from MIRROR-PROCESS-AUDIT-MODEL-001 § Q-4
                            and applied to every finding below at § FQ-5
  not paper conclusions     0 conclusions of PMID 42397075 are read, cited or evaluated. The
                            paper's own text was never opened in this session; only the
                            protocol and manifest that describe the packet
  only process quality      every finding names the artifact, command or clause that would
                            carry it, and none depends on what the paper says
```

---

## PRECONDITIONS — run, not assumed

```
framework/state/state_manifest_current.md:141       current_state: READY
python3 framework/scripts/legend_lint.py .          VERDICT: PASS
                                                    1 [INFO] MISSING_WIKILINK, CLAIM 010, non-blocking
lease (lease_state.py + orchestrator_lease.md,      ACTIVE by derivation: 0
  both from main@788c357; the script is ABSENT        #1 STALE · #2 RELEASED · #3 STALE (stored
  on `mirror`, so both were extracted to a            EXPIRED — the tool reports the disagreement)
  scratch tree and run there)                         #4 RELEASED · #5 RELEASED
                                                    FINDING: #3 EXPIRED_WITHOUT_RENEWAL
```

**There is no Orchestrator.** C.3 — *"Apertura solo via Orchestrator"* — is unsatisfiable by
anyone at this instant, and so is step 2 of the benchmark sequence, which requires
*"Orchestrator (lease ACTIVE)"* to issue the two Task Contracts. This record therefore opens no
review; it describes one that cannot currently be opened. INHERITED from
`EPISTEMIC_REVIEW_MODEL-001` § IDENTITY, re-derived here rather than copied.

**And there is nothing to audit.** Measured this session, across all 55 refs:

```
BENCH-AB-001 output tree (first_pass/, frozen/, comparison/, audit/, outcome/)   0 paths
task contracts for scientist-a / scientist-b under ledger/tasks/                 0 (only `plan` has one)
any review in which a scientist holds AUTHOR or REVIEWER                         0 occurrences
event ledger of any name, on any ref                                             0 paths
```

The experiment has not run. This record is therefore **ex ante** — the audit design, not the
audit — and every statement about what an audit *would find* is marked as conditional.

---

## OVERLAP_MAP — what is new, and what is not

| § here | Prior coverage | Relation |
|---|---|---|
| F-0 (the protocol is not on Mirror's ref) | — | 🆕 **NEW, and the record's structural finding** |
| F-1 (Mirror's seat already assigned at §5 step 8) | — | 🆕 **NEW.** No prior record reads the benchmark sequence |
| F-2 (§8.2 already assigns Mirror 6 of 10 dimensions) | — | 🆕 **NEW** |
| § 1 CONTAMINATION — the two declared contaminations | `REV-SCIAB-MIRROR-002`, quoted in the protocol as *Mirror R-2* | **INHERITED.** Found by this seat in a prior review; re-presenting it as a discovery would be the second time |
| § 1 C-4 (the one unmechanised rule) | protocol §7, verbatim | **QUOTED**, not found |
| § 1 C-5 (corpus contamination, 21 → 32 paths) | protocol §2.1 states 21 at BASE_HEAD | 🆕 **NEW measurement** at `main`; the delta is reported, not treated as a contradiction |
| § 2 EVIDENCE DISCIPLINE — the triad is a subset of four | — | 🆕 **NEW.** The dispatch names 3 levels; the discipline has 4 |
| § 2 E-3 (the dispatch omits the negative side entirely) | `epistemic_discipline.md` §2, verbatim | 🆕 **NEW as a finding about the dispatch**; the clause it rests on is quoted |
| § 3 UNCERTAINTY | protocol §5.1, MODE_B "searched; none found" | **QUOTED.** The operative test already exists |
| § 4 REASONING QUALITY — all four bullets are overshoot | — | 🆕 **NEW, and the sharpest finding in the middle of the record** |
| § 5 PIPELINE — the join key exists *inside* the benchmark | `LABORATORY-QUALITY-GATE-MODEL-001` § AQ-2 measured its **absence** repo-wide | 🆕 **NEW, and it reverses the prior finding's sign** for this one object |
| § 5 P-5 (incomplete freeze is a typed state, not an error) | protocol §7 | **QUOTED** |
| § 6 LEARNING — 0 instantiated G.2 proposals | `MIRROR-PROCESS-AUDIT-MODEL-001` § LL-1 | **INHERITED**, re-measured |
| § 6 L-4 (ESC-3's stated harmlessness expires with this pilot) | — | 🆕 **NEW** |
| § FQ (final question) — two-way, with a "nothing failed" branch | `LABORATORY-QUALITY-GATE-MODEL-001` § ATTRIBUTION answers a **three-way** version | **DIFFERENT QUESTION.** § FQ-1 states the distinction before using anything |
| § FQ-3 (the benchmark emits no failure verdict) | — | 🆕 **NEW, and it dissolves the question's presupposition** |
| § FQ-4 (separation is a routing rule, not a judgement) | — | 🆕 **NEW** |
| § FQ-6 (the pilot is confounded by design, per §41) | — | 🆕 **NEW** |

---

## F-0 · The first finding is about this record's own sourcing

The dispatch asks me to define how Mirror will audit *the first real Scientist experiment*. That
experiment exists, is named, and is specified in detail:

```
BENCH-AB-001 · PMID 42397075 · doi 10.1093/brain/awag239 · Brain 2026
  framework/protocols/controlled_benchmark_ab.md          the protocol      745 lines
  framework/protocols/scientist_reading_modes.md          the reading modes
  framework/eval/benchmarks/BENCH-AB-001/                 10 tracked files
```

Measured across all 55 refs this session:

```
refs carrying controlled_benchmark_ab.md + scientist_reading_modes.md     18
refs carrying framework/eval/benchmarks/BENCH-AB-001/                     17
                                                          on `mirror`      0 · 0 · 0
                                                          on `main`        1 · 1 · 10
positive control: framework/eval/failure_taxonomy.md IS on `mirror`, and was read there
```

🔴 **Mirror is the assigned adjudicator of a protocol its own worktree does not carry.** Every
quotation in this record from those three sources came from `main`, by `git show`. That is a
legitimate read — the object store is shared and the ref is named at every use — but it is not
the same as the file being in the working tree of the actor who must execute against it. The
positive control matters: the taxonomy Mirror must score `FAILURE MODES` against *is* present,
so this is a specific gap and not a generally thin ref.

**Stated as an observation and nothing more.** Naming what should be done about it — a
cherry-pick, a rebase, a sparse checkout, a change to what `mirror` tracks — would be a proposal,
and § 6 explains why Mirror cannot currently route one.

---

## F-1 · The model this dispatch asks for is largely already written, and it assigns Mirror by name

`controlled_benchmark_ab.md` §5 (`main`) is a ten-step sequence. Step 8, verbatim:

> | 8 | Mirror | **adjudication of the process** (R4): failure modes per reading, epistemic
> discipline, whether the protocol was followed, whether the design held |
> `reviews/mirror/BENCH-AB-001-ADJUDICATION.md` on branch `mirror`; pointer + digest under
> `adjudication/` |

Four objects, one deliverable path, one review level. Set beside the dispatch's six audit
headings:

| Dispatch heading | Step 8's four objects | Match |
|---|---|---|
| 1 CONTAMINATION | *whether the design held* | direct |
| 2 EVIDENCE DISCIPLINE | *epistemic discipline* | direct |
| 3 UNCERTAINTY | *epistemic discipline* (partly) | partial — § 3 |
| 4 REASONING QUALITY | *failure modes per reading* | direct |
| 5 PIPELINE FAILURE | *whether the protocol was followed* | direct |
| 6 LEARNING | — | 🔴 **not in step 8.** Learning is G.2/G.3, outside the benchmark record |

🆕 **Five of the dispatch's six headings are step 8 restated.** The sixth is real and is
elsewhere. A Mirror audit model written without step 8 in view would not be a new model; it
would be a second, unreconciled copy of an existing one — and the two would diverge the first
time either was edited, invisibly, because they live on refs that do not see each other (F-0).

---

## F-2 · The dimension table already names the evaluator, row by row

`controlled_benchmark_ab.md` §8.2 (`main`) is a ten-row table whose last column is **Evaluator**.
Counted this session:

```
rows where Mirror is an evaluator                     6   CLAIM PRECISION (the Type question) ·
                                                          EPISTEMIC DISCIPLINE (substance) ·
                                                          CONTEXT PRESERVATION (instances) ·
                                                          METHODS / LIMITATIONS (substance) ·
                                                          CONTRADICTION / NEGATIVE EVIDENCE (substance) ·
                                                          FAILURE MODES (all of it)
rows with NO Mirror seat                              3   EVIDENCE COVERAGE (Plan) · PROVENANCE (Plan) ·
                                                          LOCATOR FIDELITY (Plan; blind agents)
rows routed OUT of the benchmark entirely             1   MECHANISTIC VALUE → Annex C review, opened by
                                                          Orchestrator, outside the record
```

The table's own summary sentence, verbatim: *"Mechanical rows are commands; adjudicated rows are
Mirror's, on the process; the one row that is scientific judgment (mechanistic value) is deferred
to the review ladder."*

🆕 **The process/science boundary the dispatch asks Mirror to hold is already drawn as a column in
a table.** § FQ-4 is about what follows from that.

---

## 1 · CONTAMINATION — did A and B remain independent?

### C-1 · The standard the question implies is not the standard the system claims

Body §26, verbatim, and it is the section's whole content:

> **SEMI-BLIND — BEST EFFORT.** Convergenza indipendente = segnale forte; divergenza →
> discussione → R3 → Mirror analizza il PERCHÉ. `Independence by task framing, not by
> information barrier`.

Annex C.3 repeats the same clause verbatim. 🔴 **An audit that scores BENCH-AB-001 against
information-barrier independence would be scoring it against a guarantee the governance
explicitly disclaims, twice.** The finding would be true of the world and false of the contract,
which is the shape of a false positive that costs a rebuild and buys nothing.

What the benchmark adds *above* the governance floor is a real strengthening, and it is
structural rather than promissory (§2.1, `main`): the surfaces are built **by allowlist, from
nothing**, into directories that are not checkouts of the LEGEND repository and share no object
store with it. *"What is not copied in is not there."*

### C-2 · Three checks exist, and they are commands, not judgements

`controlled_benchmark_ab.md` §4 (`main`) — blinding as a property, with §3's command list:

```
same bytes           SOURCE_FILES digests + PARITY, recomputed by `verify`
same instructions    COMMON_FILES byte-identical; PER_ACTOR_FILES exactly two paths
                     🔴 "A third differing file is a broken benchmark, and `verify` reports it"
no prior output      FORBIDDEN_PRIOR_OUTPUT_PATHS absent from both surfaces, no exemption
                     pre-handover; CONTENT_SCAN hits == 0
after the fact       every locator's artifact ∈ ALLOWED_PATHS, per entry;
                     a citation outside the surface is BENCH_INVALID for that entry —
                     "recorded, never silently dropped, because a dropped entry is a
                     reading that looks clean and is not"
```

**None of these is Mirror's.** They are `benchmark_input_surface.py` subcommands run by Plan, and
`verify` exits non-zero on any finding. Mirror auditing contamination by re-running them would be
duplicating a mechanical check; Mirror's object is whether they were run, when, in which mode,
and what their census said.

### C-3 · Two contaminations of the variable are already declared — INHERITED, and one is this seat's own

Protocol §0 (`main`), both stated by the protocol itself, unprompted:

1. **Session variance is not separable from mode.** *"With one paper and one session per actor,
   the benchmark cannot separate the effect of the mode from the variance between two sessions.
   It is a first controlled benchmark — one variable, everything else held — not a statistical
   study."*
2. 🔴 *"Each reader can read the other's mode directive, and the variable is narrower than it
   looks."* `scientist_reading_modes.md` §4–§5 is a **common** file, normative for both readers,
   and it describes both modes in full. So the manipulated variable is not knowledge of the two
   modes; it is **which directive is addressed to you**. The protocol records this as *"a known
   contamination of the variable … and not softened"*, and attributes it inline: **(Mirror R-2)**.

**INHERITED — and the attribution is the point.** Finding (2) came from
`reviews/mirror/REV-SCIAB-MIRROR-002.md`, this seat, in a prior review. A Mirror audit that
"discovers" it at step 8 would be recording the same finding a second time against a protocol
that already carries it with Mirror's own finding id attached. § 6 L-3 is about why that pattern
recurs here.

### C-4 · The one rule with no mechanism, and the protocol says so in its own words

Protocol §7 (`main`) — neither actor sees the other's first pass until **both** are frozen:

> 🔴 **This rule is `PROCEDURAL`** … Nothing mechanises it. No process stands between the two
> surfaces, and Plan showing B the contents of A's tree before B's freeze would leave no trace in
> any artifact this protocol produces.
>
> ```
> GUARANTEE_PROVIDED:            none by mechanism — discipline only
> FAILURE_MODE_STILL_POSSIBLE:   Plan reads or relays A's first pass to B before B freezes
> DETECTION:                     the two receipts carry FREEZE_TIMESTAMP_UTC and SURFACE_COMMIT;
>                                an inspection of B's commit history against A's freeze time
>                                makes a violation VISIBLE AFTER THE FACT, never prevented
> RECOVERY:                      the benchmark is void for the second reader; the outcome says so
> ```

🆕 **This is the only contamination question a process auditor can actually add value on, and its
detection route is an inspection nobody is assigned.** DETECTION names an act — *an inspection of
B's commit history against A's freeze time* — and §5's ten steps assign it to no one. It is not
in Plan's step 6 (mechanical checks, comparison matrix, disagreement list), and step 8 names
Mirror's four objects without naming it. Recorded as an observation about an unassigned act;
assigning it would be a proposal, which § 6 explains Mirror cannot route.

The two residuals the protocol carries beside it, and which no audit closes (§2.1, `main`): an
actor can read outside its surface by absolute path — *"Nothing prevents it"* — and the model may
carry the paper from training, *"Uncontrollable"*.

### C-5 · 🆕 The corpus is contaminated, was before the benchmark existed, and the number has grown

Protocol §2.1 (`main`) states that at `BASE_HEAD cbce3016`, **twenty-one** tracked files name the
paper — *"A first pass run in such a checkout is blind only by promise"* — and concludes: *"the
blinding problem is a property of the corpus, not of this paper"*.

Measured this session at `main@788c357`, by reading every tracked file's content for the
identifiers:

```
tracked paths naming the paper at main       32     (protocol records 21 at BASE_HEAD cbce3016)
```

🔴 **Reported as a delta, not a contradiction.** `main` has moved past `BASE_HEAD`; the two
numbers are measurements of different trees and both can be right. What the delta shows is
directional and is the auditable fact: **the corpus contamination the surface exists to escape
grew by roughly half while the benchmark waited to run.** The surface design is unaffected — it
copies from an allowlist, so a larger corpus does not enlarge the surface — but
`FORBIDDEN_PRIOR_OUTPUT_PATHS` is enumerated *from the tree at build time*, so the list is a
function of when `build` runs, and a benchmark built today excludes a different set than one
built on 2026-08-18.

---

## 2 · EVIDENCE DISCIPLINE — Observation / Inference / Hypothesis

### E-1 · The dispatch names three levels; the repository has four

`framework/instruction/epistemic_discipline.md` §1 (on `mirror`, read there):

```
DATO       (≈ L1)  directly supported by a primary/secondary peer-reviewed source
INFERENZA  (≈ L2)  plausible, from convergence of multiple data points; declared as an inference
IPOTESI            reasonable but not directly supported; marked as hypothesis
ESPANSIONE (≈ L3)  outside the direct gene/disease domain; strategy space only
```

The dispatch's triad maps onto the first three. **`ESPANSIONE` is absent from it**, and it is the
level with the sharpest gate: *"cannot enter the current files as consolidated fact without
explicit promotion."* Both mode directives (`main`) require all four by name — *"epistemic typing
on every statement you carry out: `DATO · INFERENZA · IPOTESI · ESPANSIONE`"* — so an audit built
on the dispatch's three would under-cover the instruction the readers actually received.

### E-2 · The split between mechanical and adjudicated is already drawn

§8.2's `EPISTEMIC DISCIPLINE` row (`main`), verbatim in its parts:

```
measure    every carried statement typed; negatives with PREMISE tag and REVIVAL_TRIGGER;
           DEFAULT_FROM_TEXTBOOK declared where used; the seven benchmark fields present and
           separable — Observation free of conclusion verbs, Author interpretation marked as
           theirs; hypothesis→observation promotions found by audit
route      mechanical for presence; adjudication for substance
evaluator  Plan; Mirror
```

🆕 **The dispatch's question — "did every claim maintain Observation / Inference / Hypothesis" —
is the *presence* half, and presence is Plan's, not Mirror's.** Mirror's half is *substance*: not
whether a `Type` field is filled, but whether the statement in it bears the type it claims. §8.2's
`CLAIM PRECISION` row makes that operational — *"per claim candidate: `Type` claimed vs `Type` the
audited evidence bears"*, with the blind locator audit supplying the evidence and Mirror answering
the `Type` question.

MODE_A (`main`) names the seam that makes this checkable, and calls it the most consequential
thing that mode does:

> **Report at the level at which the paper states it.** When the authors conclude something from
> their data, that is an *author interpretation* and goes in the `Author interpretation` field —
> not in `Observation`, and not silently into your own `Summary`. Keeping that seam clean is the
> single most consequential thing MODE A does, because it is what makes the reading attackable.

### E-3 · 🆕 The dispatch's triad omits the half the repository calls the real danger

`epistemic_discipline.md` §2 (on `mirror`), verbatim heading: *"The discipline also applies to
PREMISES and NEGATIVES"* — and the reason:

> The four levels above cover only **positive assertions**. A knowledge system that accumulates
> for months is far more endangered by what it **discards** than by what it asserts. … a **false
> positive** gets tested and dies. A **false negative** is **silent, permanent, and
> self-reinforcing** … a false positive is a cost; **a false negative is a compounding loss.**

Three binding obligations follow: `PREMISE_TAG` on every rejection and non-trivial conclusion;
`REVIVAL_TRIGGER` — *"nothing dies in silence"* — with one named destination, the dismissal
ledger; and the re-audit rule, *"the loop that makes this compound"*.

🔴 **`Observation / Inference / Hypothesis` is the positive side only.** An evidence-discipline
audit scoped to the dispatch's three words would audit the half this repository considers the
cheaper half to get wrong, and would pass a reading that discarded something silently. The
benchmark's own measure already includes the omitted half — *"negatives with `PREMISE` tag and
`REVIVAL_TRIGGER`"* is in the §8.2 row quoted at E-2 — so the gap is in the dispatch's framing,
not in the protocol.

**Stated as a defect in the task as specified, and the work is done under the wider reading**:
every section below treats the negative side as in scope, because the protocol Mirror would
actually execute against does.

---

## 3 · UNCERTAINTY — were missing evidence and limits preserved?

### U-1 · Three instruments already carry it, at three different layers

```
C.2 (governance)   RESIDUAL_UNCERTAINTY · EVIDENCE_NEEDED · WHAT_WOULD_CHANGE_MY_MIND
                   — mandatory fields of every review, Mirror's included
MODE_A (main)      uncertainty · limitations, "the authors', and yours, distinguished" ·
                   "unresolved ambiguity listed as unresolved, not resolved by choosing"
MODE_B (main)      the eleven axes, each answered
```

### U-2 · The operative test is already falsifiable, and it is MODE_B's

MODE_B (`main`), verbatim:

> An axis with findings carries them, anchored. An axis with none carries **"searched; none
> found"** and says *what was searched* — concretely, not "the paper". **Silence on an axis is an
> incomplete reading, not a clean paper.**

🆕 **This is the sharpest uncertainty-preservation rule in the repository, because it inverts the
default.** An empty field normally reads as "nothing there"; this rule makes an empty field read
as "not looked", unless the looking is described. It is checkable mechanically for presence
(eleven axes, each non-empty) and adjudicated by Mirror for substance (whether *what was searched*
names anything concrete).

Its counterweight, same file, and it constrains the auditor as much as the reader: *"**Do not
manufacture criticism.** … Findings invented to fill a table are worse than an empty axis, because
they are indistinguishable from real ones until someone checks."*

### U-3 · The budget rule is where uncertainty most plausibly gets destroyed

`BENCHMARK_INSTRUCTIONS.md` §3 (`main`), the whole rule:

> **Do not compress depth or coverage for token, time or cost.** A reading shortened for budget
> produces a receipt that overstates itself, and the receipt is what the rest of the system
> trusts.
>
> If you genuinely cannot complete at full depth, **stop and report the partial state with its
> coverage map naming exactly what is unread**. A declared partial reading is a legitimate,
> useful result. A silently thinned complete reading is a false record, and it is the more
> expensive of the two by a wide margin.

### U-4 · And it has a measurable form the freeze cannot repair

Protocol §5.1 (`main`):

> A reading declared complete without `verbatim_locators.entries[]` **is not complete**, and step
> 5 does not repair it: the freeze records what was in the tree, it does not confer the depth that
> was not. Under §8.2 such a reading scores `EVIDENCE COVERAGE` and `PROVENANCE` on an empty
> locator set, and the blind audit of step 7 has no triple to audit.

🆕 **The three failure signatures of destroyed uncertainty are therefore mechanically distinct,
before Mirror judges anything**: a coverage map carrying `not_read` (declared partial — legitimate);
a coverage map carrying no `not_read` over a thin locator set (silent thinning — a false record);
and an axis answered with silence rather than *"searched; none found"* (an incomplete reading
presented as a clean paper).

---

## 4 · REASONING QUALITY

### R-1 · All four of the dispatch's bullets already have named gates

| Dispatch bullet | Where it is already named | Ref |
|---|---|---|
| alternative explanations | MODE_B axis `ALTERNATIVE_EXPLANATION`; `TARGET_ATTRIBUTION_GATE` — *"a pharmacological rescue does not identify the target automatically"* | `main` · `mirror` |
| causal claims | `MECHANISM_DIRECTNESS_GATE` — *"A surrogate is not the mechanism; the intermediate must be measured"*; `DEGRADATION_DIRECTION_GATE`; `KG_EDGE_HAS_NO_SIGN` | `mirror` (taxonomy IS on this ref) |
| overconfidence | MODE_B axis `OVERCLAIM`; §8.2 audit verdict `OVERSHOOT` | `main` |
| unsupported assumptions | MODE_B axis `UNSUPPORTED_INFERENCE`; `PREMISE: DEFAULT_FROM_TEXTBOOK` — *"not a foundation: it is a research target"* | `main` · `mirror` |

Eleven MODE_B axes exist; the dispatch's four bullets reach seven of them. The four unreached:
`NEGATIVE_EVIDENCE`, `MODEL_DEPENDENCE`, `CONTEXT_COLLAPSE`, `OMISSION`.

### R-2 · 🆕 Every one of the dispatch's four bullets is an OVERSHOOT defect

Alternative explanations not excluded, causal claims beyond the data, overconfidence, unsupported
assumptions — all four are the same direction of error: **claiming more than the evidence bears.**
The audit vocabulary in §8.2 has five values, and one of them exists for the opposite direction:

```
SUPPORTED · OVERSHOOT · UNDERSHOOT · NOT_IN_SOURCE · UNVERIFIABLE_SURFACE
```

MODE_B (`main`) says why `UNDERSHOOT` is there, and it is the reverse of the dispatch's emphasis:

> **Under-reading is a finding too.** Overshoot is the common failure; **undershoot is the rarer
> and more dangerous one**, because a narrowing nobody challenges becomes a permanent false
> negative — and this repository treats false negatives as the compounding loss. If the paper
> supports **more** than it claims, say that.

🔴 **A reasoning-quality audit assembled from the dispatch's four bullets alone would be
systematically blind in the direction the repository considers most expensive** — and it would be
blind in exactly the way `epistemic_discipline.md` §2 predicts (E-3), which is the same defect
appearing at a second layer of the same task. The two are one finding seen twice: the dispatch
consistently frames error as over-assertion.

**The work below is done under the two-directional reading**, because the protocol's own verdict
vocabulary is two-directional.

### R-3 · 🆕 Reasoning quality is audited twice, at two different objects, and Mirror must not collapse them

MODE_B (`main`), verbatim and marked 🔴 in the source:

> 🔴 **You are not Mirror.** Mirror reviews the *process* — how the laboratory reasoned, reviewed
> and recorded — and remains the adjudicator of this benchmark's method. You review *the paper's
> evidence and inferences*, with a Scientist's authority.

```
scientist-b's object     the paper's reasoning        — is the paper's inference supported?
mirror's object          the reading's reasoning      — was the reasoning discipline followed?
```

Annex C.4 is the same partition one level up: `EVIDENCE → Scientist + Plan/provenance ·
INFERENCE → peer Scientist · SYSTEM → Mirror`. 🆕 **So a Mirror finding of the form "the paper
overclaims here" is a category error — that is MODE_B's finding to make, and Mirror duplicating it
takes a Scientist's seat.** Mirror's corresponding finding is *"MODE_B did not run the `OVERCLAIM`
axis, or ran it without saying what was searched."* § FQ-5's retraction test is the mechanical way
to tell the two apart.

---

## 5 · PIPELINE FAILURE

### P-1 · Wrong assignment — the detector exists because it already failed once

Annex A.3: *"Al più UN claim valido per TASK_ID + GENERATION"*, with its guarantee block stating
the compensating protocol rather than a lock — `GUARANTEE: unicità per costruzione organizzativa`,
`FAILURE: doppio claim … nessun lock di filesystem`, `DETECTION: CLAIM_CONFLICT`.

Inside the benchmark the check is tighter, and protocol §7 (`main`) records why:

> | `BENCHMARK_ID` · `ACTOR_ID` · `TASK_ID` · `MODE` · `PARALLEL_READ_GROUP` | **read from
> `ASSIGNMENT.md` inside the frozen tree**; the command line is checked against it and a
> disagreement is a refusal, exit 2 |

and, immediately before it: *"Revision 1 of this command recorded an absolute local path, took the
actor and benchmark ids as unchecked free text (**A's tree froze happily as `scientist-b`**)."*

🆕 **Wrong assignment is not hypothetical here: it occurred, in the tooling, and was caught by
Mirror review before any reader existed.** The identity is now read from inside the tree rather
than taken from the invoker, which is the structural form of the fix.

Measured this session: `ledger/tasks/` holds **one** contract, owner `plan`. **Zero** task
contracts exist for `scientist-a` or `scientist-b`, so the A.3 machinery has never run for a
Scientist.

### P-2 · Broken handoff — one transfer, recorded; and one layer that records nothing

The handoff is a single writer transfer (§2.2, `main`): *"Plan builds each surface and is its only
writer until HANDOVER; at handover the writer becomes the named actor and Plan does not write into
it again — Plan reads it once more, at FREEZE."* Its evidence is the manifest's `HANDOVER` block:
`{at, by, to, surface_tree_sha256, memory_scope_absent}`.

🆕 **`memory_scope_absent` is a handoff check for a failure mode the governance never names.**
§2.2 records it as *"a favourable accident of the deployment, not a guarantee"*: the interactive
runtime keeps auto-memory per working directory, so a session opened in a fresh surface starts
with an empty memory scope, whereas one opened in `lettore` would inherit what the `lettore`
sessions accumulated. Plan checks and records it. The protocol declines to rely on it, and the
audit should not either.

Against that, the layer with no record at all — measured across 55 refs this session, and
**INHERITED** from `LABORATORY-QUALITY-GATE-MODEL-001` § AQ-3, which measured the same absence:

```
event ledger, any name, any ref          0 paths
J.1's 23 minimum EVENT_TYPEs             0 events — TASK_ASSIGNED, TASK_ACKED, REVIEW_OPENED,
                                         REVIEW_CLOSED, CHECKPOINT_WRITTEN … none of them
```

`roles/mirror.md`: *"Mirror's primary analysis runs on the **consolidated event ledger** (Annex
J.1), not by reading fifty chats"*, and the same file lists `Event ledger analysis` among Mirror's
declared capabilities with the status **"blocked: the ledger has no writer yet"**. The handoff's
*within-benchmark* evidence exists; its *control-plane* evidence does not.

### P-3 · 🆕 Inside the benchmark, the join key exists — and this reverses the prior record's finding for this one object

`LABORATORY-QUALITY-GATE-MODEL-001` § AQ-2 measured, repo-wide, that the scientific record and the
process record share no identifier except the paper, and concluded: *"The join that attribution
requires does not exist in the durable state."* That finding is not disturbed; it was measured over
`disease-models/` and `ledger/`, and it holds there.

**BENCH-AB-001 is the exception, and it is the first one.** The freeze receipt
(`RECEIPT_SCHEMA_VERSION 2`, §7, `main`) carries, in one object:

```
BENCHMARK_ID · ACTOR_ID · TASK_ID · MODE · PARALLEL_READ_GROUP     read from inside the tree
INPUT_MANIFEST_SHA256 · INSTRUCTIONS_VERSION · OUTPUT_SCHEMA_VERSION
SURFACE_COMMIT · SURFACE_BRANCH · SURFACE_DIRTY
FREEZE_TIMESTAMP_UTC · FIRST_PASS_STATE
TREE_SHA256 · FILE_COUNT · FILES[] with role ∈ input · output · unexpected
GUARANTEE_PROVIDED · FAILURE_MODE_STILL_POSSIBLE · DETECTION
```

🆕 **A defect found in a BENCH-AB-001 reading is attributable to a task, an actor, a mode, an
instruction version and a commit — which is precisely what AQ-4 found impossible everywhere else.**
The benchmark is not merely the first scientific experiment; it is the first object in this
repository whose product and process share identifiers. That is a property worth naming *before*
the experiment runs, because it is the property that makes the audit possible at all.

### P-4 · Incomplete freeze — already a typed state, not an error

Protocol §7 (`main`): `FIRST_PASS_STATE` is one of

```
COMPLETE_DECLARED_BY_ACTOR · ABANDONED · TIMED_OUT
```

🆕 **Two of the three are incomplete freezes, and both are legitimate recorded outcomes rather
than failures.** The dispatch lists "incomplete freeze" as a pipeline failure to detect; the
protocol has already demoted it to a state to record. What remains a genuine failure is a freeze
that is *incomplete and says otherwise* — which is U-4's signature, not a freeze-mechanism defect.

The freeze's own integrity properties, verbatim: freeze happens *"on the completion declaration
and before reading the content"* — *"a freeze taken after Plan has read the content is a freeze
whose timing cannot be shown"*; `verify-freeze` recomputes **"set-wise, never by count"**
(`ADDED`/`REMOVED`/`MODIFIED`, each enumerated) because *"Two trees of equal file count holding
different files is exactly the substitution this exists to catch, and a count says they agree"*;
and `freeze` **refuses** a tree containing a symlink, *"since a link's bytes are not here"*.

Post-freeze corrections are not edits: *"A correction an actor wants to make after freeze is a
**new dated file** under `first_pass/<ACTOR_ID>/post_freeze/` … with the original left as frozen.
Retroactive edits are the one thing this section exists to make impossible to do quietly."*

### P-5 · What the three instruments do not establish, in the protocol's own words

Protocol §4.4 (`main`), closing the guarantee table:

> **Read together, the three bound the window and do not close it.** Before handover the tree
> provably held no prior output; at freeze the tree is pinned; after freeze any change to it is
> detectable. What no combination of them establishes is **authorship of bytes at the one
> colliding path**, and none of the three is to be described as if it did.

The colliding path is `disease-models/wwox/research/deepdive_manifests/PMID42397075.json` — the
reader's own manifest lands exactly where LEGEND's prior manifest sits, because
`deepdive_manifest.py` derives the path from disease and PMID. Measured this session: that path
**exists on `mirror`**, which is the concrete form of the collision.

Also unclosed, and stated where the claim is: *"a change to an allowlisted input applied
**identically to both surfaces**, which parity cannot see"* — with the repair named and
deliberately not made: *"`build --emit-digests` already records per-file input digests and
`verify` does not consume them."*

---

## 6 · LEARNING — what should change, what should remain fixed

### L-1 · The route is fixed, and it currently dead-ends

Annex G.2, the field set and the route, verbatim:

```
OBSERVED_FAILURE / CURRENT_RULE / PROPOSED_RULE / EXPECTED_BENEFIT / POTENTIAL_HARM /
PREDICTION / FALSIFIER / VALIDATION_SAMPLE / ROLLBACK / SCOPE

Flusso: proposal → Plan candidate → reviewer indipendente scelto da Orchestrator →
        validazione; se governance → operatore.
```

```
MIRROR_UPGRADE_PROPOSAL objects ever instantiated   0   INHERITED — MIRROR-PROCESS-AUDIT-MODEL-001 § LL-1
ACTIVE orchestrator leases, derived this session    0   § PRECONDITIONS
```

🔴 **Step 3 of the route requires an Orchestrator to choose the independent reviewer, and there is
none.** The learning loop this section is asked to design cannot presently be walked to
completion, which is why every candidate change below is written as an observation with its
route named, and none as a proposal.

### L-2 · What the pilot may license, and what it may not — the n=1 boundary

Protocol §0 (`main`) fixes this before any result exists: one paper, one session per actor,
*"cannot separate the effect of the mode from the variance between two sessions … Its value is the
**material** it produces … and the failure modes it surfaces, not a number."*

🆕 **The learning discipline that follows is a boundary, not a checklist:**

```
LICENSED by n=1     an existence claim — "this gate can be violated and pass", "this field was
                    ambiguous to a reader", "this command's census missed a class". One instance
                    is sufficient to establish that a failure mode is reachable
NOT LICENSED        any comparative or frequency claim — "MODE A is thinner than MODE B",
                    "readers usually miss supplements", "this check has a low yield".
                    Two sessions cannot support a rate, and §8.5 already forbids the composite
                    that would hide one
```

§8.5 backs the second row mechanically: *"No overall score. No weighting."* And §8.4 quarantines
the metrics most likely to be misread as quality: time, tokens, output volume — *"They are not
combined with anything, they do not break ties, and a reading is not 'better' for being faster,
shorter or cheaper."*

### L-3 · What should remain fixed — and the strongest candidate is the thing that keeps recurring

Fixed by explicit design, and none of it is the pilot's to revise:

```
body §50             "Design FROZEN: la v3.2 nascerà dai dati del laboratorio, o non nascerà"
Annex G.3            "Queste metriche sono la fonte esclusiva della futura v3.2 (freeze)"
Annex C.2            CONFIRMED = "nessun difetto rilevato dato l'evidence bundle disponibile", non "vero"
body §27 / §8.3      INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED is a legitimate outcome
protocol §8.5        no overall score, no weighting, every count an enumerated set
```

🆕 **And one fixed point this record can attest to from its own construction.** The protocol quotes
Mirror finding ids inline — `R-1`, `R-2`, `R-8`, `B-1`, `B-4`, `M-2`, `M-3`, `M-4` — each marking a
defect this seat found and the author repaired. Two of them, `M-2` → `M-3` → `M-4`, are the *same
pattern* found three times: *"`M-2` was scoped to one spec key, `M-3` to one skip condition, `M-4`
to one CLI flag. **A finding is measured under one invocation; the claim it repairs is printed
under all of them.**"* That sentence is a general rule about verification, it was learned inside
this protocol's review cycle, and it lives in a protocol file rather than in any learning index —
which is L-4's subject.

### L-4 · 🆕 ESC-3's stated reason for being harmless expires with this pilot

`governance/ANNEX_INDEX.md` records `G.3 — MIRROR_RETROSPECTIVE ogni N batch` as **UNASSIGNED** by
the annexes and *"left UNRESOLVED, not filled in by Plan"*. The approval queue records the operator
carrying it forward, verbatim from `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` (read this
session):

> `{"id":"ESC-3","item":"MIRROR_RETROSPECTIVE cadence parameter N","state":"UNRESOLVED","note":"Carried forward by explicit operator decision. No numeric value introduced. **Blocks nothing: retrospectives cannot run before there are batches to retrospect.**"}`

🔴 **The pilot produces the first batch to retrospect.** ESC-3 was carried unresolved on a reason
that is true today and false the moment BENCH-AB-001 completes. This is not a proposal to set `N`
— setting it is a G.2 parameter decision Mirror may not make, and the operator explicitly reserved
it — but the *condition attached to the deferral* is measurable and is about to be met, and a
deferral whose stated basis has lapsed should lapse visibly rather than quietly.

Alongside it, measured this session and **INHERITED** from the two prior records: `active_lessons/`
is absent on this ref; no `LEARNING_INDEX` exists as an object; `REVIEW_YIELD` has never been
computed. G.3's *"yield nullo persistente → rituale → declassare"* has no denominator to compute
over, and § F-2's six Mirror rows would be its first entries.

---

## FQ · THE FINAL QUESTION

> *"If the first LEGEND paper analysis fails, how do we know whether science failed or the system
> failed?"*

### FQ-1 · This is not the question the prior record answered, and the difference is a whole branch

`LABORATORY-QUALITY-GATE-MODEL-001` § ATTRIBUTION answers: *"how can Mirror determine whether the
failure came from the Scientist, the pipeline, or the laboratory itself?"* — a **three-way
partition inside the system**. Its findings stand and are used below.

This dispatch's cut is different and orthogonal:

```
prior record   system ── Scientist | pipeline | laboratory        (three ways to fail)
this dispatch  science  vs  system                                (two, and one of them is "nothing failed")
```

🆕 **The new branch is the null one.** "Science failed" includes the case where the process ran
correctly and the world did not cooperate — an ambiguous paper, an unmeasured intermediate, an
honest `DISAGREEMENT_UNRESOLVED`. The three-way partition has no room for it, because all three of
its branches are defects.

### FQ-2 · F.4 supplies the ordering, and the actor is last — INHERITED

Annex F.4's ordered elimination (delivery/runtime → context → contract ambiguity → actual refusal)
concludes *"(1)-(3) → recovery tecnico / chiarimento contratto, **MAI insubordinazione**"*.
INHERITED from `LABORATORY-QUALITY-GATE-MODEL-001` § AQ-1: the actor is the last hypothesis, and
the annex says so in capitals of its own.

### FQ-3 · 🆕 The question presupposes a verdict the benchmark does not emit

"If the first analysis **fails**" — measured against the protocol, *fails* has no referent. Every
outcome a reader can produce is either a recorded state or an explicitly legitimate result:

```
no overall score, no weighting                       §8.5 — there is no composite to fail
DISAGREEMENT_UNRESOLVED, explained                   body §27, §8.3 — "a legitimate outcome"
"searched; none found — searched: …"                 MODE_B — a complete axis, not an empty one
a declared partial reading                           §3 of the instructions — "a legitimate,
                                                     useful result"
ABANDONED · TIMED_OUT                                §7 — recorded FIRST_PASS_STATEs
CONFIRMED                                            C.2 — "non 'vero'"
the scientific-value judgment                        §8.2 — deferred OUT, to Annex C, by design
```

🔴 **BENCH-AB-001 has no failure verdict.** It produces material and enumerated findings, not a
pass/fail. So the honest first move on the final question is not to answer it but to observe that
it imports a binary the protocol deliberately refuses — the same refusal §8.5 makes explicit, and
the same one C.2 makes about `CONFIRMED`.

### FQ-4 · 🆕 The separation is already built as a routing rule, not as a judgement

What *can* go wrong is four things, each with an owner, an instrument, and a destination:

| What failed | Instrument | Who | Where it lands |
|---|---|---|---|
| **the apparatus** — surface not blind, third differing file, non-empty slot | `verify`, `rc=1`, pre-handover | Plan | never reaches a reader; surface rebuilt from spec |
| **the reading, as a reading** — no locators, coverage map inconsistent, artifact outside allowlist | §5.1; `deepdive_manifest.py --verify-artifacts`; `locators`; blind audit | Plan + blind agents | §8.2 mechanical rows |
| **the process** — discipline not followed, types not borne, axes silent | adjudication, R4 | **Mirror** | `reviews/mirror/BENCH-AB-001-ADJUDICATION.md` |
| **the science** — is the inference right? | ❌ **not decidable inside the benchmark** | Orchestrator opens an Annex C review | §5 step 10, *"**outside** the benchmark record"* |

🆕 **So "science failed or system failed" is answered by which artifact a finding lands in, and
that is fixed before the experiment starts.** The benchmark is constructed so that everything it
can decide is a system question by construction, and the one row that is scientific judgment
(`MECHANISTIC VALUE`) is routed out of the record to the review ladder. The boundary is not a call
someone makes after a bad result; it is the shape of the deliverable set.

### FQ-5 · The mechanical test for a finding that crossed the line — INHERITED

`MIRROR-PROCESS-AUDIT-MODEL-001` § Q-4's retraction test, applied here:

> **If PMID 42397075 were retracted tomorrow, would this finding survive?**
>
> A process finding survives — *"the coverage map declared complete over an empty locator set"* is
> true whatever happens to the paper. A science finding evaporates — *"the organoid result does
> not support the conclusion"* has nothing left to be about.

Every finding in this record was written to pass it, and § R-3 is the case where it does real work:
*"the paper overclaims"* dies on retraction and belongs to MODE_B; *"the `OVERCLAIM` axis was
answered with silence"* survives and belongs to Mirror.

### FQ-6 · 🆕 The pilot is a confounded experiment by design, and body §41 says so

Body §41, verbatim, on the first scientific batch:

> **PICCOLO (1–2 PMID a testa)** … Scopo del primo ciclo: **scienza vera + qualificazione
> simultanea** di claim, messaging, challenge, peer review, work commit, learning, integrazione,
> sampling Mirror, canonical batch, recovery.

🔴 **The first analysis is simultaneously the science and the system's own qualification test —
ten mechanisms qualified in the same run that is supposed to produce a scientific result.** Body
§38 names the state that makes this acute: `BOOTSTRAP QUALIFICATION — CONFIGURED != PROVEN`. And
the state is not hypothetical; measured this session against `roles/scientist.md` and
`roles/mirror.md`, **every declared capability of both roles reads `UNVERIFIED`**, and protocol §1
records L2 itself as *"SUSPENDED by the C-9 hold (operator, 2026-08-17)"*.

The consequence for attribution is directional and it is the record's closing finding: **at the
pilot, the prior probability of system failure is high and has never been measured, while the
science is being attempted for the first time under instruments none of which has been proven.**
Concluding "the science failed" from a bad first result would invert F.4's ordering at exactly the
moment the ordering matters most — and F.4 already names that inversion, for its own object, in
one word: `MAI`.

### FQ-7 · What remains genuinely inseparable, stated as the protocol states it

Not everything separates, and the protocol says which part does not before anyone has a motive to
wish otherwise (§0, caveat 1): with one paper and one session per actor, **mode, session variance
and paper region cannot be told apart.** If A's reading is thin in the supplement, the record
cannot distinguish *MODE A under-covers supplements* from *that session was worse* from *the
supplement is thin*.

🔴 **Mirror must not close that gap by judgement.** The protocol declares it first; an adjudication
that resolved it would be supplying a distinction the design cannot support, and § L-2 already
names it as the boundary of what the pilot licenses.

---

## BLOCKERS

> Blockers to the audit's **execution**. Nothing below is assigned; Mirror holds no command.

```
B-1  THE EXPERIMENT HAS NOT RUN. 0 output paths, 0 task contracts for either scientist, 0 freeze
     receipts. Everything above is ex ante and none of it has been exercised

B-2  THE PROTOCOL IS NOT ON THIS REF (§ F-0). controlled_benchmark_ab.md, scientist_reading_modes.md
     and BENCH-AB-001/ are on 17–18 refs, none of them `mirror`. Read from `main` throughout

B-3  THE BENCHMARK IS BLOCKED. Protocol §9: "BLIND FIRST PASS — BLOCKED BY CANONICALIZATION",
     and independently by P-2…P-4. Measured this session: no approval object for
     CAND-20260818-SCIENTIST-AB-SPEC exists in the queue on `mirror` or on `main` — the only two
     approval ids ever recorded are APR-20260816-GOV311-001 and -002. The protocol's own front
     matter still reads `status: PROPOSED`

B-4  NO ORCHESTRATOR. 0 ACTIVE leases derived. C.3 bars opening a review; §5 step 2 bars issuing
     the two Task Contracts; G.2 step 3 bars routing any proposal this record might have made

B-5  NO EVENT LEDGER, ON ANY REF. roles/mirror.md names it Mirror's primary analysis surface and
     marks that capability "blocked: the ledger has no writer yet". The within-benchmark receipts
     (§ P-3) are the only process evidence that would exist

B-6  THE C-4 INSPECTION IS ASSIGNED TO NOBODY. §7's only detection route for the one unmechanised
     rule — B's commit history against A's freeze timestamp — appears in no step of §5
```

---

## OPEN_QUESTIONS

```
Q-1  Does `verify --post-read` run against BOTH surfaces before the comparison, or once per
     surface at each freeze? §4.4 gives the contract; §5 step 5 gives the timing; the two do not
     obviously fix the number of invocations, and M-4 was precisely a defect of "which invocation"

Q-2  If the two freezes are far apart in time, does anything constrain how long A's frozen tree
     waits while B reads? §7 fixes the ORDER of disclosure, not the interval, and the interval is
     when the C-4 residual is live

Q-3  Who runs the C-4 inspection (B-6), and does its absence from §5 mean it is Plan's under step
     6 "mechanical checks" or Mirror's under step 8 "whether the design held"? Both readings are
     available and the text selects neither

Q-4  Does a `BENCH_INVALID` locator entry (§4.3) make the reading partial for §8.2's coverage
     denominator, or is it excluded from the numerator only? The two give different coverage
     numbers over the same 65-unit population
```

---

## WHAT THIS RECORD DOES NOT DO

It does not conduct an audit, adopt a rubric, propose a rule, or create a validator. It does not
start, authorize, unblock or schedule BENCH-AB-001; it does not lift the C-9 hold, verify a
capability, register an actor, take a lease, or issue a task. It does not evaluate PMID 42397075
— the paper was never opened in this session — and it reaches no conclusion about WWOX biology. It
does not set `N` for `MIRROR_RETROSPECTIVE`, resolve ESC-3, or decide anything G.2 reserves. It
does not amend, supersede or correct `MIRROR-PROCESS-AUDIT-MODEL-001`,
`LABORATORY-QUALITY-GATE-MODEL-001`, `EPISTEMIC_REVIEW_MODEL-001` or any of
`REV-SCIAB-MIRROR-001…006`. It writes one file, under `learning/mirror/`, on branch `mirror`.

---

## EVIDENCE

```
RUN THIS SESSION, 2026-08-22T19:06Z–19:09Z, mirror@da52ee5 · main@788c357 · 55 refs

  framework/scripts/legend_lint.py .                  VERDICT: PASS (1 INFO)
  framework/state/state_manifest_current.md:141       current_state: READY
  lease_state.py --check (script+record from main,    ACTIVE by derivation: 0; #3 EXPIRED_WITHOUT_RENEWAL
    extracted to a scratch tree — absent on `mirror`)
  ref sweep, controlled_benchmark_ab.md               18 refs · NOT on `mirror`
  ref sweep, scientist_reading_modes.md               18 refs · NOT on `mirror`
  ref sweep, framework/eval/benchmarks/BENCH-AB-001/  17 refs · NOT on `mirror`
  positive control: framework/eval/failure_taxonomy.md   PRESENT on `mirror`, read there
  ref sweep, event ledger (any name)                  0 refs
  ref sweep, BENCH-AB-001 outputs                     0 refs
  content sweep, tracked files naming the paper       32 at main (protocol records 21 at cbce3016)
  reviews/ sweep, AUTHOR|REVIEWER == scientist        0 occurrences, all refs
  ledger/tasks/                                       1 contract, owner `plan`
  ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl         2 approval ids, both GOV311; 0 for SCIAB
  learning/mirror/                                    38 records; 29 match SLR-mirror-NNNN
  git worktree list                                   lettore · lettore-b · lettore-c all exist

  ⚠️  A ref sweep in zsh must brace the variable: `"${r}:${f}"`, never `"$r:$f"` — the bare form
      applies the `:r` history modifier and returns a false ABSENT on every ref. Every sweep above
      used the braced form and each was run with a positive control.

READ AT `mirror`     GOVERNANCE_v3.1.1.md · annexes A, C, F, G, J · roles/scientist.md ·
                     roles/mirror.md · epistemic_discipline.md · failure_taxonomy.md ·
                     ANNEX_INDEX.md · reviews/mirror/REV-SCIAB-MIRROR-001, -006
READ AT `main`       controlled_benchmark_ab.md (all 10 sections) · BENCHMARK_INSTRUCTIONS.md ·
                     MODE_A.md · MODE_B.md · benchmark_manifest.json · surface_spec.json
NOT READ             PMID 42397075, in any surface. The packet is git-ignored and was never opened
```
