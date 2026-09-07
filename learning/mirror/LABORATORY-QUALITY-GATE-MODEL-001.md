---
artifact: MIRROR analysis record — how Mirror evaluates the quality of the LEGEND laboratory
  process, across three layers, using only quality-control functions the governance already
  assigns. Learning artefact only
record_id: LABORATORY-QUALITY-GATE-MODEL-001
actor_id: mirror
date: 2026-08-22
task_id: LABORATORY_QUALITY_GATE_MODEL_v1
dispatcher: operator
role: >
  mirror — metacognitive layer. This record reviews no object, names no author, issues no verdict,
  and evaluates no scientific claim. It maps functions that already exist; it exercises none of them
authority: >
  The full normative surface: `governance/GOVERNANCE_v3.1.1.md` annexes A, B, C, E, F, G, H, I, J
  and `roles/mirror.md`. 🔴 THIS DIFFERS FROM THE PRIOR RECORD ON ADJACENT GROUND.
  `MIRROR-PROCESS-AUDIT-MODEL-001` was dispatched under an authority restricted to G and C and
  excluded Annex H by instruction. This dispatch carries no such restriction, so H.1's rows are
  used here — and where a conclusion depends on H.1, it is marked, so the two records stay
  comparable rather than merely consistent.
  Nothing here is adopted or in force. G.2 bars Mirror from self-approving material changes to its
  own review rubric or its own methods, and an evaluation model IS such an object. Every element is
  either (a) quoted from a normative file, (b) a measurement run this session, or (c) inherited and
  attributed. NO ELEMENT IS MARKED PROPOSED, because this record proposes nothing
classification: OBSERVATION AND ANALYSIS — not governance, not a protocol, not a validator,
  not a gate, not a rubric, not a score, not an amendment, not a decision
scope: >
  learning/mirror/ on branch `mirror` only. One new file. No governance/, roles/, framework/,
  ledger/, runtime/, reviews/ or disease-models/ path is written. No existing record is edited,
  superseded or corrected
prior_artefact_disclosure: >
  🔴 MATERIAL, EXTENSIVE, AND SPREAD ACROSS REFS THIS SEAT CANNOT READ WITHOUT ASKING FOR THEM.
  Five records on `mirror` overlap substantially: `MIRROR-PROCESS-AUDIT-MODEL-001` (719 lines,
  committed at da52ee5, this same date), `EPISTEMIC_REVIEW_MODEL-001`,
  `reviews/mirror/ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001`,
  `reviews/mirror/REV-LEGEND-LAB-ARCHITECTURE-001` and
  `SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001`. Two further records on OTHER refs cover LAYER 2
  more directly than anything on this one: `learning/orchestrator/SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001`
  (ref `orch-scientific-pipeline-lifecycle-model`) and
  `learning/orchestrator/ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001`
  (ref `orch-pipeline-loop-architecture`). This record SUPERSEDES NONE of them and CORRECTS none
  of them. Overlap is mapped at § OVERLAP_MAP; inherited findings are attributed inline and marked
  INHERITED; only items marked 🆕 are new. Roughly half of what follows would have read as
  original had the overlap not been declared — and the cross-ref half of it is § LAYER_3's subject
naming_deviation: >
  DECLARED. 29 of the now-37 records under learning/mirror/ match `SLR-mirror-NNNN[-ADD|-COR-NNN]`.
  This filename was specified by the dispatch and departs from that pattern, as seven others already
  do, each having declared its own departure. NO NAMING RULE IS ADOPTED AND NO PRECEDENT IS SET
measured_at: >
  mirror@da52ee5e9d3e6eb66455c61d422c4fb1d0e21391 · main@788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
  · 54 refs · 759 distinct paths in the ref-tip union · 2026-08-22T18:20Z–18:45Z.
  Every count below was run in this session against these refs. Numbers taken from another record
  are marked INHERITED and attributed. 🔴 The population moved between the prior record and this
  one: 53 refs / 758 paths at 2026-08-22T18:04Z, 54 / 759 now, with three ref tips later than that
  instant. Recorded because § LAYER_3 is partly about measurements taken over a moving population
---

# LABORATORY QUALITY GATE MODEL — three layers, the evidence each one needs, and the attribution the durable record cannot currently make

> **Mirror does not decide scientific truth. Mirror evaluates whether the process that produced a
> scientific conclusion was reliable.** The dispatch states this as a premise. Annex C states it as
> a definition of the strongest verdict any reviewer may reach — `CONFIRMED` = *"nessun difetto
> rilevato dato l'evidence bundle disponibile", **non "vero"***. The premise is therefore not a
> privilege granted to Mirror; it binds every reviewer, and what distinguishes Mirror is the
> object, not the epistemics.
>
> **And the model this dispatch asks for is already written.** It is distributed across five
> `DETECTION:` lines in the normative annexes, and every one of them names Mirror. This record
> collects them, measures whether each can currently run, and answers the attribution question
> at the end. It invents nothing.

---

## TASK_STATUS

```
TASK          LABORATORY_QUALITY_GATE_MODEL_v1
DISPATCHER    operator (no ACTIVE lease exists — derived this session, § PRECONDITIONS)
STATE         COMPLETE for the analysis; NOTHING ADOPTED; NOTHING DECIDED; NOTHING PROPOSED
DELIVERABLE   learning/mirror/LABORATORY-QUALITY-GATE-MODEL-001.md — this file, branch `mirror`

THE DISPATCH'S FIVE PROHIBITIONS, EACH CHECKABLE
  no new authority     0 authority statements. § ESCALATION routes exclusively through H.1 rows,
                       F.1–F.2, G.2 and J.3, quoted. No route is created, widened or reassigned
  no new validator     0 paths written under framework/, scripts/ or .claude/. No check, schema,
                       field or script is created. § LAYER_2 measures instruments; it adds none
  no new governance    0 annexes amended, interpreted, reconciled or extended. Quotations are
                       quotations. Where two readings of a clause exist, both are recorded and
                       neither is chosen (§ AUTONOMY_BOUNDARY AB-4)
  no new scoring       0 scores, 0 rankings, 0 weights, 0 thresholds, 0 severity orderings.
                       The dimension tables are unordered and their rows are not comparable
  not a new protocol   nothing here is executable, triggerable or owed by anyone. § WHAT THIS
                       RECORD DOES NOT DO states it again against each candidate misreading

AND THE ONE THE DISPATCH IMPLIES
  no truth judged      0 scientific claims assessed. The test applied to every finding below is
                       the retraction test, § D-4 — INHERITED, and applied, not merely cited
```

---

## PRECONDITIONS — run, not assumed

```
framework/state/state_manifest_current.md:141   current_state: READY
python3 framework/scripts/legend_lint.py .      VERDICT: PASS
                                                1 [INFO] MISSING_WIKILINK, CLAIM 010, non-blocking
python3 framework/scripts/fulltext_receipts.py verify
                                                OK: 128 chained receipt(s), tail anchored in
                                                framework/state/state_manifest_current.md
lease (main@788c357's lease_state.py, run       ACTIVE by derivation: 0
  against main:runtime/orchestrator_lease.md;     #1 STALE · #2 RELEASED · #3 derived STALE while
  the script is ABSENT on `mirror`)               stored EXPIRED — the tool reports the disagreement
                                                  #4 RELEASED · #5 RELEASED
                                                derivation instant 2026-08-22T18:39:22Z
```

**There is no Orchestrator.** C.3 — *"Apertura solo via Orchestrator"* — is unsatisfiable by anyone
at this instant. This record therefore opens no review; it describes how one would be evaluated.
INHERITED from `EPISTEMIC_REVIEW_MODEL-001` § IDENTITY, re-derived here rather than copied.

**The receipt chain verifies.** Recorded because it is the one Layer-1 instrument that runs, from
this seat, over a real scientific population, and returns a positive result. Every other executable
in this record returns an absence, and an absence-only report is the shape of a broken instrument
as much as of a broken system. The instrument was working.

---

## TERMINOLOGY — the title's term names nothing new, and that was checked

Measured across all 54 refs, over the full path union:

```
QUALITY_GATE              0 paths
"quality gate"            0 paths
"quality of the process"  0 paths
POSITIVE CONTROL          the same per-ref sweep resolves MIRROR_UPGRADE_PROPOSAL (26),
                          MIRROR_RETROSPECTIVE (42), LEARNING_INDEX (63). It was working
```

🔴 **The dispatch's title term has no precedent in this repository.** A new term in a record of
this kind is a hazard: repeated three times it becomes an object, and an object with no annex is
governance written sideways. So the term is used **once, in the filename the dispatch specified,
and nowhere below as the name of a thing.** What follows is a map of existing functions —
`DETECTION:` lines, C.2 fields, G.3 metrics, F.4's diagnosis, the executable checks — and each is
called by the name it already has.

INHERITED as a class: `SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001` § 4.5 names this failure
`FC-5 · Vocabulary contamination — dispatch terms entering durable records`. This paragraph is that
lesson applied, which is the only form of application available to a lesson with no index (§ 3.1).

---

## OVERLAP_MAP — what is new, and what is not

| § here | Prior coverage | Relation |
|---|---|---|
| D-1…D-2 (the five DETECTION lines) | — | 🆕 **NEW, AND THE RECORD'S ORGANISING FINDING.** No prior record reads the annexes' `GUARANTEE/FAILURE/DETECTION/RECOVERY` blocks as an existing quality model |
| D-3 (what that makes this record) | — | 🆕 NEW |
| D-4 (retraction test) | `MIRROR-PROCESS-AUDIT-MODEL-001` § Q-4 | **INHERITED**, restated and applied per-layer |
| LAYER 1 · dimensions | `MIRROR-PROCESS-AUDIT-MODEL-001` § TAXONOMY (7 classes, two forms each) | **INHERITED.** The two-form split is that record's; the layer assignment is new |
| LAYER 1 · evidence (O-1…O-10) | `ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001` § *Observational requirements* | **INHERITED IN FULL — attributed, not restated in detail.** 🆕 what is added is the reachability column, measured from this seat this session |
| LAYER 1 · no calibration surface | `EPISTEMIC_REVIEW_MODEL-001` § B-1 | **INHERITED**, re-measured (namespace census) |
| LAYER 2 · assignment contamination | `REV-LEGEND-LAB-ARCHITECTURE-001` F-5, F-6 | **INHERITED.** Two Scientist checkouts holding byte-identical uncommitted edits is that review's measurement |
| LAYER 2 · blind reading integrity | `ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001` I-2; the `legend-locator-audit` skill | **INHERITED.** The blind instrument outside the ladder is that record's finding |
| LAYER 2 · handoff integrity | `SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001` F-3 (**other ref**) | **INHERITED, cross-ref.** *"The sender's artifact is durable. The receiver's acceptance leaves no trace anywhere."* |
| LAYER 2 · events never emitted | same record, F-2 (**other ref**) | **INHERITED, cross-ref**, re-measured here (23 types · 0 emitted) |
| LAYER 2 · durable-state visibility per seat | `REV-LEGEND-LAB-ARCHITECTURE-001` F-7 covered `reviews/` and `learning/` | 🆕 **BUILDS ON.** F-7 measured the *narrative* namespaces; the control-plane namespaces (`ledger/tasks`, `ledger/checkpoints`) are measured here for the first time |
| LAYER 2 · the invalidation-rate proxy computed from three seats | — | 🆕 **NEW.** The one metric `roles/mirror.md` calls Mirror's own, computed three times, yielding three values |
| LAYER 2 · freeze inventory | scattered; no prior record enumerates them together | 🆕 **NEW as an enumeration**; every row is a prior object |
| LAYER 3 · memory / learning / loops | `EPISTEMIC_REVIEW_MODEL-001` § LEARNING_LOOP; `MIRROR-PROCESS-AUDIT-MODEL-001` LL-1…LL-4; `SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001` §§ 3.5, 4 | **INHERITED**, re-measured |
| LAYER 3 · duplicated work, measured | `SLR-…-CORRECTION-MEMORY-ANALYSIS-001` § 6.4 answered it "only where measurement reaches" | 🆕 **BUILDS ON.** 152 artefacts · 126 on exactly one ref · 14 on `main` is measured here |
| LAYER 3 · human bottleneck | `REV-LEGEND-LAB-ARCHITECTURE-001` F-3, F-8 | **INHERITED** |
| ESCALATION | H.1, F.1–F.2, G.2, J.3 | **QUOTATION.** Nothing new; occupancy measured |
| AUTONOMY_BOUNDARY AB-1…AB-3 | H.1 rows; G.2; C.3 | **BUILDS ON** |
| AUTONOMY_BOUNDARY AB-4 (two different reasons) | — | 🆕 **NEW.** Lack of authority and lack of evidence are different bars and have different remedies |
| ATTRIBUTION AQ-1 (F.4 as the existing shape) | `REV-ROLES-MIRROR-001` cites F.4 in another context | 🆕 **NEW here.** F.4 is the repository's existing ordered attribution procedure |
| ATTRIBUTION AQ-2 (the join key) | — | 🆕 **NEW, AND THE ANSWER TO THE DISPATCH'S FINAL QUESTION** |
| ATTRIBUTION AQ-3…AQ-5 | — | 🆕 NEW |

---

## D · DERIVATION — the model this dispatch asks for is already written, in a place nobody reads as a model

### D-1 · The repository already has a quality-control schema, and it is four lines long

Eight blocks in the normative annexes carry the same four-field shape, verbatim:

```
GUARANTEE:  what the mechanism actually promises
FAILURE:    the named way it breaks
DETECTION:  who or what notices, and how
RECOVERY:   what happens next, and who does it
```

| Block | Mechanism | Where |
|---|---|---|
| A.3 | task claim uniqueness without a lock | `annex_a_task_contract.md:47` |
| A.6 | checkpoint compatibility and the refusal rule | `:83` |
| A.7 | idempotent resume | `:101` |
| B.3 | message delivery under ACK | `annex_b_message_protocol.md:39` |
| E.5 | active-learning compression and budget | `annex_e_learning_lifecycle.md:50` |
| I.3 | the orchestrator lease singleton | `annex_i_bootstrap_deployment.md:54` |
| I.4 | declared vs verified capability | `:71` |
| J.1 | the event ledger | `annex_j_runtime_control_plane.md:56` |

Four further blocks exist in `governance/design_records/prior_art_review_v3.1.md`, which is
non-normative and duplicates I.4's and A.6/A.7's; they are excluded from every count below.

**J.0 is the same schema, tabulated.** Its left column is the guarantee LEGEND does *not* possess;
its right column is the compensating protocol. And it closes with a rule that binds this record
directly: *"Vietato a qualsiasi documento o attore descrivere questi meccanismi con vocabolario più
forte del protocollo compensativo."* A record that called any of the functions below a *gate* would
be violating exactly that clause. They are detections, and they are called detections.

### D-2 · 🆕 Five DETECTION lines name Mirror, and between them they are the three layers

| Line | Verbatim | Dispatch layer |
|---|---|---|
| **A.6** `:88` | *"(b) **Mirror** monitora il tasso di invalidazione e i casi di ripresa poi contestati"* | **LAYER 2** — freeze conditions, dependency failures |
| **A.7** `:104` | *"esistenza dell'evidenza nello stato durevole; **Mirror** osserva il rapporto rifatto/totale"* | **LAYER 3** — duplicated work |
| **E.5** `:52` | *"errori ripetuti su pattern già appresi (**Mirror** retrospettive); richieste degli attori"* | **LAYER 3** — learning, repeated failures |
| **I.4** `:73` | *"fallimenti ripetuti sullo stesso tipo di task → **Mirror** coordination review"* | **LAYER 3** — repeated failures, capability drift |
| **J.1** `:58–59` | *"incrocio ledger ↔ stato durevole (gap = evento mancante); aperture senza chiusura oltre soglia → **Mirror** retrospettive"* | **LAYER 2** — handoff integrity, unresolved loops |

Two more assignments of the same shape sit outside the G/F/D/R blocks:

```
F.3   "Mirror: quali classi di dissent Orchestrator tende a OVERRIDE che poi risultano
       VALIDATED_LATER?"  — ex post, mai veto ex ante          → LAYER 2, escalation quality
G.3   REVIEW YIELD per Ladder level; "yield nullo persistente → rituale → declassare"
      AUTONOMY LEDGER; AUTO-METRICHE; MIRROR_RETROSPECTIVE      → LAYER 3, and the loop's own measure
roles/mirror.md, verbatim: the A.6 invalidation rate and the A.7 redone-work ratio are
      "Mirror's specific responsibility for calibrating what Plan defined"
```

🔴 **Nothing in the dispatch's three layers is new to this repository.** LAYER 2 and LAYER 3 are
already assigned to Mirror by name, inside the compensating protocols for the six guarantees J.0
says the system does not possess. What is missing is not the assignment. It is, in every case
measured below, the evidence the detection would run on.

### D-3 · What that makes this record — and what it may not become

If the model already exists as five lines, then this record is a **reading**, not a design. That
distinction is load-bearing for G.2: a reading of existing normative text is an analysis Mirror may
write; a rubric assembled from that text is a material change to Mirror's own methods, which
`roles/mirror.md` and G.2 bar Mirror from adopting alone. The dividing line is operational, and
this record stays on the analysis side of it by refusing three specific moves — no threshold, no
ordering, no aggregation. **Any two of those three would turn the tables below into an instrument.**

### D-4 · The boundary that keeps every finding on the process side

INHERITED from `MIRROR-PROCESS-AUDIT-MODEL-001` § Q-4, and applied here rather than cited:

> **A Mirror finding must hold its truth value under both outcomes of the science.** Suppose the
> conclusion under examination were later confirmed; suppose instead it were retracted. A finding
> that survives both suppositions unchanged is a process finding. A finding that becomes false, or
> becomes uninteresting, under either supposition is a truth finding wearing a process badge, and
> C.4 routes it to a Scientist.

Applied per layer:

```
LAYER 1  "the record declares no alternative and no search for one"   survives both  → process
         "the alternative is the better explanation"                  fails both     → peer Scientist (C.4)
LAYER 2  "no artefact records that A's output was frozen before B read it"  survives both → process
         "B copied A"                                                  is an accusation, not a
                                                                       finding; the observable is
                                                                       the absence of the record
LAYER 3  "no MIRROR_UPGRADE_PROPOSAL has ever been instantiated"       survives both  → process
```

Every finding below was tested against this before being written. Where a candidate finding failed
the test, it was routed away by C.4 and does not appear.

---

## LAYER 1 — SCIENTIST PROCESS

> **Question, as dispatched:** *"Did the Scientist reason correctly from the available evidence?"*
> **Read against C.2 and C.4**, `correctly` cannot mean *arrived at the truth* — that is the
> INFERENCE object and C.4 assigns it to a peer Scientist. It means: **did the reasoning have a
> declared way of being wrong, and did it use it?**

### 1.1 · The six dispatched dimensions, each against the name it already carries

Unordered. No dimension is weighted, scored or ranked against another.

| Dimension | The process question — Mirror's | Existing name(s) | The truth question — NOT Mirror's (C.4) |
|---|---|---|---|
| **evidence handling** | do the locators resolve, is each quote inside the declared packet, is the coverage map free of `not_read`? | `fulltext_read_receipt` chain · `deepdive_manifest.py --verify-artifacts` · `locator_audit.py` | is the evidence strong enough? → peer Scientist |
| **hypothesis separation** | are statements typed `DATO / INFERENZA / IPOTESI / ESPANSIONE`, and is `Observation` free of conclusion verbs? | `epistemic_discipline.md` | is the hypothesis right? → peer Scientist |
| **uncertainty management** | are `RESIDUAL_UNCERTAINTY` and `EVIDENCE_NEEDED` present and non-empty? | **C.2 mandatory fields** | is the residual acceptable? → peer Scientist |
| **alternative explanations** | are alternatives carried, **or** an explicit *"searched; none found"* plus what was searched? | **C.2 `ALTERNATIVES_CONSIDERED`** · `scientist_reading_modes.md` § 5: *"silence on an axis is incompleteness, not a null result"* | is the alternative better? → peer Scientist |
| **overclaim risk** | was the claim's strength compared with the source's, by someone, and is that comparison an artefact? | `LOCATOR_OVERSHOOT_GATE` · `legend-locator-audit` verdicts `OVERSHOOT`/`UNDERSHOOT` | is the claim in fact too strong? → peer Scientist |
| **missing evidence** | is the gap **declared** or **silent**? A declared gap is work in progress; silence is the defect | **C.2 `EVIDENCE_AGAINST`** · `UNREAD_PREMISE` ratchet · `unread_gold.py` | is the missing evidence decisive? → peer Scientist |

🔴 **Four of the six have their antidote as a mandatory field inside Annex C.2.** A review written
to the single format cannot omit them *silently*; it can only leave them empty, and an empty
mandatory field is visible. That is a property of the format, not something this record adds.

INHERITED: the two-form split (process form / truth form) is `MIRROR-PROCESS-AUDIT-MODEL-001`
§ TAXONOMY's, where it is developed over seven classes. It is not re-derived here.

### 1.2 · Evidence required — inherited in full, with one column added

`ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001` § *Observational requirements for reviewing Scientist
output* enumerates ten observables (O-1…O-10) and four `NO SOURCE` gaps, each traced to a binding
source. **That enumeration is the answer to this dispatch's "evidence required" for LAYER 1, and it
is not restated here.** What is added is one column, measured from this seat this session:

| Observable class | Source | 🆕 Reachable from `mirror@da52ee5` today? |
|---|---|---|
| O-1…O-4 manifest, packet digests, coverage map, claim fields | `scientist_reading_modes.md` § 3.5–3.6 | 🔴 **NO.** The protocol is ABSENT on this ref (present on `main`); `deepdive_manifest.py` is present |
| O-5 quote existence | `locator_audit.py` | ⚠️ script present; **the packet it reads is not** — see below |
| O-6 surface parity, freeze verification | `benchmark_input_surface.py` | 🔴 **NO.** Script ABSENT on this ref, present on `main` |
| O-7 blind (proposition, quote, anchor) triples | `.claude/skills/legend-locator-audit` | ✅ skill present on this ref |
| O-8 per-axis MODE B answers | `scientist_reading_modes.md` § 5 | 🔴 **NO** — same absent file |
| O-9 typed statements | `epistemic_discipline.md` | ✅ present |
| O-10 the 12 reasoning-failure gates | `framework/eval/failure_taxonomy.md` — 12 rows, re-counted | ✅ present; `learned_gates_registry.md` present |

🔴 **And the precondition every mechanical observable shares is unsatisfied from here.** All of
them read `files/`, which is `.gitignore:7` — **and this worktree has no `files/` directory at
all.** The evidence surface is carried by no ref and is not present locally. INHERITED as a
statement (`ANALYSIS-…-001`, closing paragraph of that section); 🆕 as a measurement of *this*
checkout: a reviewer standing here can verify that a manifest is well-formed and cannot verify
that it describes the artefact it names.

**No calibration surface exists.** Re-measured: the `learning/` and `reviews/` namespaces across
all 54 refs are exactly `{mirror, orchestrator, plan}` — **there is no Scientist namespace, and no
Scientist artefact, anywhere in the union.** Every dimension in § 1.1 is therefore mapped against
protocol text and against zero real Scientist products. INHERITED from `EPISTEMIC_REVIEW_MODEL-001`
§ B-1; re-measured here by namespace census rather than by re-reading that record.

### 1.3 · Failure classes at this layer — existing names only

The seven classes of `MIRROR-PROCESS-AUDIT-MODEL-001` § TAXONOMY (overclaim · evidence gap · causal
leap · alternative missing · cherry picking · false negative · premature closure) are this layer's
failure classes. **They are not restated, renamed, extended or reordered here.** Two facts from
that record bear directly on the reachability column above and are re-verified:

```
five of the seven have their canonical name in scientist_reading_modes.md — ABSENT on this ref
premature closure has no name on any ref; C.2's WHAT_WOULD_CHANGE_MY_MIND is its only antidote
```

### 1.4 · What Mirror can and cannot conclude at LAYER 1

```
CAN, alone     that a mandatory C.2 field is empty; that a locator does not resolve within the
               declared packet; that a coverage map contains not_read; that an axis is silent
               where the protocol requires "searched; none found"; that a receipt chain verifies
CANNOT, alone  anything requiring the packet under files/ — not for want of authority but for
               want of evidence at this seat (§ AB-4)
MUST NOT       decide whether the reasoning reached the right answer. C.4: INFERENCE → peer
               Scientist. Every such question in § 1.1's right column is routed there and left
```

---

## LAYER 2 — PIPELINE PROCESS

> **Question, as dispatched:** *"Did the system preserve scientific independence?"*
> C.3 already fixes what independence is available: *"semi-blind = **independence by task framing,
> not by information barrier**"*. The pipeline question is therefore not *were the readers
> independent* — it is **does the durable record establish which framing each actor worked under.**

### 2.1 · The five dispatched dimensions, against existing objects

| Dimension | Existing object(s) that define it | Existing detection | State, measured this session |
|---|---|---|---|
| **assignment contamination** | A.1 `TASK_ASSIGNMENT` (`SCOPE`, `DEPENDENCIES`, `REVIEW_REQUIREMENT`) · A.3 claim uniqueness · C.3 rotation and `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` | A.3 `CLAIM_CONFLICT` at write or at Plan's reconciliation | 5 task records in the union, **all `plan`**; 0 for any other actor |
| **blind reading integrity** | `legend-locator-audit` (blind by construction) · `controlled_benchmark_ab.md` · `scientist_reading_modes.md` | the audit's own verdicts | skill present here; **the two protocol files are not on this ref** |
| **handoff integrity** | B.2 message type `HANDOFF` · B.3 ACK discipline | B.3: HEARTBEAT + absence of `TASK_CLAIM`/`STATUS` in window | 🔴 `HANDOFF` has **no closure object** — INHERITED, cross-ref |
| **freeze conditions** | § 2.5 below — eight distinct mechanisms | mixed: four executable, four textual | see § 2.5 |
| **dependency failures** | A.1 `DEPENDENCIES` · A.6 refusal rule · J.0's six missing guarantees | A.6 at rehydration; I.3 GATE 0 for the lease | A.6's refusal rule **has been exercised once**, by `plan` |

### 2.2 · Evidence required at this layer, and how much of it exists

Each row is an object the annexes already specify. The count is of **instances**, not of mentions —
the distinction that `MIRROR-PROCESS-AUDIT-MODEL-001` LL-1 established for G.2 and that is applied
here to the whole control plane.

| Evidence the annexes specify | Where specified | Instances in the ref union |
|---|---|---|
| `TASK_ASSIGNMENT` / `TASK_ACK` / `TASK_CLAIM` | A.1–A.3 | **5**, all under `ledger/tasks/plan/`; 13 refs carry all 5, 15 more carry 1–4, `mirror` carries 1 |
| `CHECKPOINT` with `APPLICABLE_GOVERNANCE_FINGERPRINT` | A.6 | **27** — 19 `plan` + 8 `mirror`; **27 of 27 carry the fingerprint** |
| `RESUMED_FROM_MILESTONE` | A.7 | 🔴 **0 in `ledger/`.** The token resolves to 10 paths, every one definitional or analytical |
| event, any of the 23 minimum types | J.1 | 🔴 **0 emitted.** `EVENT_ID` resolves to 13 paths, all definitional or analytical; no events file exists among the union's 10 `.jsonl` |
| `HUMAN_APPROVAL_QUEUE` entries | J.3 | **2 requests + 1 appended correction**, both `APPROVED`, `RESOLVED_BY: operator`, all 2026-08-16 |
| a closure for a `HANDOFF` | — | 🔴 **specified nowhere.** INHERITED: `SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001` F-3 |

🔴 **The one thing a pipeline audit most needs is the one thing that has never been written.**
J.1's ledger is the surface `roles/mirror.md` names as Mirror's primary analysis surface —
*"not by reading fifty chats"* — and it has 23 specified event types and zero events. The role
contract already says so in its own capability table: *"Event ledger analysis — **blocked: the
ledger has no writer yet**"*. Re-measured, unchanged.

**And the freeze that matters most is a promise.** Quoted from the cross-ref record, because the
sentence is exact and re-deriving it would be re-derivation for its own sake:

> *"Freezing is a handoff. With no closing event, the statement 'A's output was frozen before B's
> was read' is not a fact any instrument can establish after the fact — it is a promise."*
> — `SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001` F-3 (ref `orch-scientific-pipeline-lifecycle-model`)

### 2.3 · 🆕 No seat sees the whole durable state — measured on the control plane, not on the narrative

`REV-LEGEND-LAB-ARCHITECTURE-001` F-7 measured this for `reviews/` and `learning/`. The
control-plane namespaces had not been measured. They are now:

| Object | on `mirror@da52ee5` | on `main@788c357` | union |
|---|---|---|---|
| `ledger/tasks/**` | **1** | 5 | 5 |
| `ledger/checkpoints/plan/**` | **6** | 19 | 19 |
| `ledger/checkpoints/mirror/**` | 8 | **0** | 8 |
| `runtime/**` | **0** | 1 | 1 |
| `learning/` + `reviews/` of **other** actors | **0** | 14 | 65 |

```
🔴 From Mirror's own ref:  1 of 5 task records · 6 of 19 of the other actor's checkpoints ·
                           0 of 65 artefacts written by Orchestrator or Plan · no runtime/
🔴 From main:              0 of 8 Mirror checkpoints · 0 of 87 Mirror artefacts
🔴 Consequently:           NO REF CARRIES THE POPULATION ANY LAYER-2 OR LAYER-3 QUESTION IS ABOUT
```

The seat charged with lab-level analysis is the seat with the least of the lab on it. Stated
without inference about anyone's intent: this is a property of a worktree-per-actor design in which
nothing merges, and F-7 already established that nothing merges.

### 2.4 · 🆕 The metric Mirror is named to compute, computed three times, from three seats

`roles/mirror.md` names the A.6 **checkpoint invalidation rate** as one of two metrics that are
*"Mirror's specific responsibility"*. It is the only one whose numerator exists today: the 27
checkpoints, and a task record whose `ANTI_RESUME_DECLARATION` invalidates five of them at once by
the A.6 refusal rule.

**First, the honest caveat, before the numbers.** A.6's rate has **no operational definition**:
`"tasso di invalidazione"` resolves to exactly **1 path across 54 refs — Annex G itself** — and
`plan_defined_parameters.md` § P2.3 names Mirror as its monitor while defining no numerator and no
denominator. What follows is therefore **a text-pattern proxy over the checkpoint bodies, not the
metric**, and the value is not the point.

```
PROXY   checkpoints whose body states an incompatibility or an invalidation
        ("INCOMPATIBLE" | "NOT a compatible" | "invalidat*")

from mirror@da52ee5     5 of 14      from main@788c357     8 of 19      over the union   10 of 27
```

🔴 **Three seats, three values, one lab.** The divergence is not measurement error and not
disagreement — each count is correct over the population its ref carries. It is the § 2.3 finding
expressed as a number: **a metric assigned to a seat is a metric over that seat's ref.** Any
retrospective computing it without declaring the ref will report a lab-level quantity that is a
ref-local one, and no reader could tell.

*(The A.7 redone-work ratio, Mirror's other named metric, has the same missing definition — `"rapporto
lavoro-rifatto"` also resolves to 1 path — and additionally a numerator of zero: no
`RESUMED_FROM_MILESTONE` has ever been recorded. Whether that means no work was redone or that
redone work leaves no trace is not decidable from the durable state, and the second reading is the
one A.7's own DETECTION line presumes.)*

### 2.5 · 🆕 Freeze conditions — the enumeration, and which ones can act

The dispatch lists *freeze conditions* as a pipeline dimension. Eight distinct mechanisms in this
repository stop work. They are collected here for the first time; every row is a pre-existing
object and none is created, modified or ranked.

| Mechanism | Where | Executable? |
|---|---|---|
| `BLOCK_BATCH_COMMIT` / `BLOCK_SYSTEM` | structural LINT | ✅ yes — `legend_lint.py`, run this session |
| receipt-chain break halts LEGEND | `fulltext_receipts.py verify` | ✅ yes — run this session, `OK: 128 chained` |
| growth ratchets | `growth_anchors.py check` | ✅ present on this ref |
| publication gate | `scripts/public_release_gate.py` | ✅ present |
| A.6 refusal rule — incompatible fingerprint ⇒ do not resume | A.6 | ⚠️ **textual**; exercised once, by `plan`, declared in a task record |
| I.3 lease stop condition — double reacquisition ⇒ both stop | I.3 | ⚠️ textual; `lease_state.py` **absent on this ref** |
| F.1 `GOVERNANCE_BLOCK` — stop + escalation | F.1 | ⚠️ textual |
| J.4 spend stop condition — `DEFAULT_EXTERNAL_SPEND = 0` | J.4 | ⚠️ textual, fail-closed by policy |

🔴 **Every freeze that protects the *scientific record* is executable; every freeze that protects
the *process* is prose.** That asymmetry is not a defect anyone introduced — the executable four
run over files in the repository, and the textual four run over acts. But it fixes what a LAYER 2
audit can be: for four of these, the only observable that a freeze held is that someone wrote that
it did. The A.6 row is the sole instance in the repository where that writing exists.

### 2.6 · Failure classes at this layer — existing names only

```
CLAIM_CONFLICT             A.3     double claim on one TASK_ID + GENERATION
stale generation           A.4     resumption under a superseded contract — "anti-zombie"
incompatible fingerprint   A.6     resumption under changed pertinent rules
ACKed-but-not-started      B.3     a measured class: "turno troncato, permission prompt"
unclosed opening           J.1     an opening event with no CLOSES_EVENT_ID beyond threshold
premature consensus        REV-LEGEND-LAB-ARCHITECTURE-001 F-5/F-6 — INHERITED, not renamed here
```

**No class is coined.** Where the dispatch's vocabulary has no repository name —
*assignment contamination* is the clearest case, resolving to 46 paths none of which is a
definition — that is recorded as an absence and left. Naming it would be a taxonomy change, and a
taxonomy change is not Mirror's to make alone (G.2).

---

## LAYER 3 — LAB SYSTEM

> **Question, as dispatched:** *"Does LEGEND improve after experience?"*
> Improvement is not a mood; E.1's state machine says exactly what it consists of —
> `OBSERVED → LOCAL → PROVISIONAL → VALIDATING → PROMOTED | REJECTED | SUPERSEDED | EXPIRED` —
> and G.2 gives the one route by which a Mirror observation becomes a changed rule. Both are
> measurable, and both were measured.

### 3.1 · The six dispatched dimensions, measured

| Dimension | Existing object | State, measured this session |
|---|---|---|
| **memory** | E.2 `LEARNING_INDEX` (durability: Plan; epistemic care: Mirror) · E.5 `ACTIVE_LESSONS` | 🔴 `active_lessons/` → **0 paths across 54 refs**, and `CLAUDE.md` § 1's single learning pointer points at it. The E.2 field set resolves to the annex plus five Mirror records that *analyse* it |
| **learning** | G.2 `MIRROR_UPGRADE_PROPOSAL`, ten fields, four-step route | 🔴 **0 instantiations.** Re-run this session: of every path carrying `OBSERVED_FAILURE`, exactly one also carries `FALSIFIER` ∧ `VALIDATION_SAMPLE` ∧ `ROLLBACK` — `annex_g_mirror.md`, the definition. 26 paths name the route; none has travelled it |
| **repeated failures** | I.4 and E.5 DETECTION lines; G.1's `failure ricorrenti` | 🔴 unevaluable by mechanism: recurrence is a predicate over history and all three candidate retrieval surfaces (index, active lessons, event ledger) are empty. INHERITED · `MIRROR-PROCESS-AUDIT-MODEL-001` E-4 |
| **unresolved loops** | J.1 openings without closure; F.3 `OPEN → … → CLOSED` | 🔴 undetectable: 0 events means no opening and no closure is recorded at all. The `HANDOFF` class has no closure object even in specification (§ 2.2) |
| **duplicated work** | A.7 redone-work ratio (Mirror's, by name) | 🔴 no `RESUMED_FROM_MILESTONE` instance; the ratio has neither a definition nor a numerator. **§ 3.2 measures the phenomenon by another route** |
| **human bottlenecks** | G.3 `AUTONOMY LEDGER` — preventable vs unavoidable, hours blocked, false escalation | 🔴 `AUTONOMY_LEDGER` → 2 paths, never computed. `REVIEW_YIELD` → 2 paths, never computed. § 3.3 |

**The loop's shape** — recording works, retrieval does not, conversion has never run, yield has
never been measured — is `MIRROR-PROCESS-AUDIT-MODEL-001` LL-4 and is INHERITED whole. It is not
re-drawn here.

### 3.2 · 🆕 Duplicated work, measured — and this record is inside the measurement

The dispatch names *duplicated work* as a lab-system dimension. It is measurable without the
missing instruments, because duplication leaves artefacts:

```
learning/ + reviews/ artefacts across the ref union         152
  of which on exactly one ref                               126   (83%)
  of which on main                                          14    (9%)
  Mirror's own                                              87 — every one on exactly one ref
adjacent analyses of the pipeline / control plane / loop     ≥6, each on a different ref, none on main
  (SCIENTIFIC_PIPELINE_LIFECYCLE-MODEL-001 § S-4 records four of them, from its own seat, on a
   ref this seat does not carry — so that record and this one are themselves the pattern)
```

🔴 **A system that records well, retrieves not at all, and never converts, will re-derive its
findings indefinitely — each time correctly, each time newly.** That is
`MIRROR-PROCESS-AUDIT-MODEL-001` S-4's finding about one parameter recorded four times in one day.
Here it is the same shape at corpus scale, and the honest statement of this record's own position
is: **LAYER 2 of this dispatch is covered, in more depth, by two Orchestrator records on refs this
seat cannot see without being told they exist.** I found them by enumerating the union, not by any
mechanism. Had I not enumerated, this record would have re-derived them and reported the result as
new. **That near-miss is the dimension, demonstrated rather than asserted** — and the countermeasure
that caught it (enumerate the union before claiming novelty) is a discipline, not an instrument, and
therefore not transmissible by anything this system currently has.

### 3.3 · Human bottlenecks — what the record actually shows

```
HUMAN_APPROVAL_QUEUE           2 requests + 1 correction, both by `plan`, both APPROVED,
                               both RESOLVED_BY: operator, all 2026-08-16
Mirror artefacts declaring a
  dispatcher                   9 of 9 → `dispatcher: operator`
Mirror task_ids declared       14 distinct declarations across reviews/ + learning/
  with a durable task record   🔴 0 — the only task records in the repository belong to `plan`
the one propagation channel
  demonstrably working         the operator writing a lesson into the next prompt
                               (INHERITED · REV-LEGEND-LAB-ARCHITECTURE-001 F-7)
```

🔴 **The operator is the assigner, the approver, and the only working memory channel.** Recorded as
three measured facts, not as a criticism: with no ACTIVE lease there is no Orchestrator to hold the
first role, and G.2's own tail — *"se governance → operatore"* — assigns the second. The third is
the one that matters for this layer, because it is the only mechanism that has ever moved a lesson,
and it is not a mechanism.

### 3.4 · Failure classes at this layer — existing names only

`SLR-mirror-CORRECTION-MEMORY-ANALYSIS-001` § 4 already names six, each anchored to a repository
object, each with `PERSISTENCE` and `REUSE` measured: **FC-1** false-negative measurement · **FC-2**
ancestor-relative diff hiding loss · **FC-3** stale register · **FC-4** surface ambiguity (a claim
true on one ref, false on another) · **FC-5** vocabulary contamination · **FC-6** mutually-blocking
infrastructure absence. **They are this layer's failure classes and are not restated, renamed or
extended here.** Two of them were exercised in the writing of this record: FC-5 by § TERMINOLOGY,
FC-4 by § 2.4.

---

## FAILURE_CLASSES — the consolidated view, with nothing added

Every class below already exists under the name given. **This table coins nothing, orders nothing,
and scores nothing.** Its only content is the layer column and the detector column.

| Class | Layer | Named in | Detector the governance names | Detector state |
|---|---|---|---|---|
| overclaim · evidence gap · causal leap · alternative missing · cherry picking · false negative | 1 | `MIRROR-PROCESS-AUDIT-MODEL-001` § TAXONOMY; 12 gates in `failure_taxonomy.md` | reading protocols + `legend-locator-audit` | ⚠️ protocol absent on this ref; skill present |
| premature closure | 1 | 🔴 unnamed on any ref; antidote is C.2 `WHAT_WOULD_CHANGE_MY_MIND` | — | 🔴 none |
| `CLAIM_CONFLICT` | 2 | A.3 | write-time or Plan reconciliation | ⚠️ textual; 5 task records exist |
| stale generation | 2 | A.4 | rehydration check | ⚠️ textual |
| incompatible fingerprint | 2 | A.6 | rehydration refusal; **Mirror** monitors the rate | ⚠️ exercised once; rate undefined, ref-local (§ 2.4) |
| ACKed-but-not-started | 2 | B.3 | HEARTBEAT + missing claim in window | 🔴 no heartbeat, no events |
| unclosed opening | 2 | J.1 | ledger ↔ state cross-check → **Mirror** retrospectives | 🔴 0 events |
| handoff without acceptance | 2 | INHERITED (cross-ref F-3) | 🔴 no closure object is specified | 🔴 none |
| premature consensus | 2 | INHERITED (F-5, F-6) | — | 🔴 none |
| lesson not retrieved | 3 | E.2 / E.5 | **Mirror** retrospectives (E.5) | 🔴 index and active lessons absent |
| repeated failure on a task type | 3 | I.4 | **Mirror** coordination review | 🔴 never held; no retrieval surface |
| ritual review (persistent null yield) | 3 | G.3 | `REVIEW YIELD` per Ladder level | 🔴 never computed (2 paths, both Mirror noting its absence) |
| redone work | 3 | A.7 | **Mirror** observes redone/total | 🔴 undefined; numerator 0 |
| FC-1…FC-6 | 3 | `SLR-…-CORRECTION-MEMORY-ANALYSIS-001` § 4 | per-class, measured there | 🔴 `REUSE: NO by mechanism` for each |

🔴 **Eleven of the fifteen rows have a detector that cannot currently run, and in every one of those
cases the reason is missing evidence rather than missing authority.** That distinction is § AB-4's,
and it is what makes this table an observation rather than a work plan.

---

## ESCALATION — existing routes only, with their occupancy measured

Nothing here is created. Each row quotes a route that already binds, and adds only whether it has
ever carried anything.

| Observation | Route the governance already gives | Exercised? |
|---|---|---|
| doubtful MAJOR classification | **H.1**: *"Classificazione MAJOR dubbia → Mirror (fail-closed)"*; body §12: persistent doubt resolves to MAJOR | ✅ the Mirror review corpus records MAJOR findings |
| a defect in an object under review | C.2 verdict + `AUTHOR_RESPONSE` (*"il silenzio non è accettazione"*) | ✅ 52 reviews |
| disagreement with a directive | **F.1** `ADVISORY | MATERIAL | GOVERNANCE_BLOCK`; **F.2** `ORCHESTRATOR_CHALLENGE`, adjudication mandatory with rationale | ⚠️ requires an Orchestrator; none is ACTIVE |
| a rule that should change | **G.2**: proposal → Plan candidate → independent reviewer chosen by Orchestrator → validation; *"se governance → operatore"* | 🔴 step 1 never instantiated; **step 3 has no occupant**; steps 2 and 4 have working precedents |
| a MAJOR / spend / governance decision | **J.3** `HUMAN_APPROVAL_QUEUE`; *"APPROVAL ≠ AUTHORIZATION"* | ✅ 2 requests, both resolved by the operator |
| an instruction ACKed and not executed | **F.4 DIAGNOSE**, four ordered causes | ⚠️ no measured instance in the durable record |
| an unresolvable review | C.3: *"`DISAGREEMENT_UNRESOLVED` con spiegazione è esito legittimo"* | — |

🔴 **The G.2 route is blocked in the middle, not at the end.** INHERITED and re-verified: the
operator step has the demonstrated precedent; the step with no occupant is the *independent reviewer
chosen by an Orchestrator*, and there is no Orchestrator. **Every finding in this record that would
want to become a rule stops there** — which is why none of them is written as a proposal.

---

## AUTONOMY_BOUNDARY — what Mirror may conclude alone, and what it may not

### AB-1 · Alone, by H.1 and by evidence that exists

```
H.1 row  "Epistemic / method review → Mirror"          the object is Mirror's
H.1 row  "Classificazione MAJOR dubbia → Mirror"       fail-closed, body §12
G.1      MIRROR_REQUIRED | MIRROR_SAMPLED | NO_MIRROR  the perimeter Mirror enters on
```

Concretely, from this seat, today: that a mandatory C.2 field is empty · that a declared level or
reviewer is absent from a review's frontmatter · that a route named in 26 artefacts has zero
instances · that a metric assigned to Mirror has no operational definition · that a checkpoint
population differs by ref · that a receipt chain verifies · that an instrument is absent from a
ref. **All of these are properties of artefacts in git, and all of them survive the retraction
test.**

### AB-2 · Requires the Orchestrator — by authority, not by evidence

```
H.1  "Task / priorità / riassegnazione / generation"          → Orchestrator
H.1  "Livello Ladder (≥ floor) e reviewer"                    → Orchestrator
H.1  "Aggiudicazione challenge (con rationale)"               → Orchestrator
C.3  "Apertura solo via Orchestrator"                         → no review opens without one
G.2  step 3, the independent reviewer                          → chosen by Orchestrator
```

Mirror holds **no command** over any actor (`roles/mirror.md`) and produces **no primary evidence**.
Its review of Orchestrator is *ex post* and pattern-based, never a veto before the fact (F.3).

### AB-3 · Requires the operator

```
H.1  "Spese / MAJOR approval / governance"    and    "Strategia complessiva"     → Operatore
G.2  tail: "se governance → operatore"
G.2  Mirror NON auto-approva: rubrica di review; learning clustering;
     active-learning selection (incl. budget E.5); review-yield methodology;
     autonomy-classification methodology
```

🔴 **Including this record's own subject.** An evaluation model for Mirror's own reviewing is a
review-rubric object. Mirror may write the analysis; Mirror may not adopt it, and the route by
which anyone else could is § ESCALATION's blocked row.

### AB-4 · 🆕 Two different bars, with two different remedies — and conflating them is the error

The dispatch asks what Mirror can evaluate autonomously. The answer has two shapes, and they are
not interchangeable:

```
BARRED BY AUTHORITY   Mirror could reach the conclusion from evidence it has, and may not act on
                      it. Remedy: a route (§ ESCALATION). Example: the MIRROR_SAMPLED rate — both
                      readings of what kind of parameter it is exclude Mirror, and both terminate
                      at the operator (INHERITED · MIRROR-PROCESS-AUDIT-MODEL-001 S-3)

BARRED BY EVIDENCE    Mirror holds the authority and cannot reach the conclusion at all, because
                      the observable does not exist or is not on this ref. Remedy: an instantiation
                      of an object the annexes ALREADY specify. Examples: every 🔴 in
                      § FAILURE_CLASSES; A.6's rate; A.7's ratio; every LAYER 3 dimension
```

**Eleven of the fifteen failure classes are barred by evidence, not by authority.** A reading that
treats them as authority problems would route them to an Orchestrator who cannot supply them, and a
reading that treats authority problems as evidence problems would have Mirror build instruments it
is barred from adopting. The two lists are disjoint, and this record keeps them apart.

---

## ATTRIBUTION — the dispatch's final question

> *"If LEGEND produces a scientifically wrong conclusion, how can Mirror determine whether the
> failure came from the Scientist, the pipeline, or the laboratory itself?"*

### AQ-1 · The shape of the answer already exists, one level down, in F.4

Annex F.4 is an **ordered elimination** for a different object — an instruction ACKed and not
executed — and its ordering is its content:

```
1. delivery / runtime failure?     (turno troncato, permission prompt, crash, sessione degradata)
2. context failure?                (rehydration incompleta, generation stale, checkpoint incompatibile)
3. task contract ambiguity?        (acceptance criteria non verificabili; INTERACTION_MODE incoerente)
4. actual refusal?
        ↓
solo (4), ripetuto dopo chiarimento → NON_COMPLIANT → HUMAN_REQUIRED
(1)-(3) → recovery tecnico / chiarimento contratto, MAI insubordinazione
```

🔴 **The actor is the LAST hypothesis, and the annex says so in capitals of its own: `MAI`.** The
attribution question this dispatch asks is F.4's question with a different object — a wrong
conclusion instead of an unexecuted instruction — and the same ordering applies for the same
reason: *the layers below the actor produce failures that look exactly like the actor's.*

**This is an observation about an existing clause, not an extension of it.** F.4 binds instruction
execution and nothing else. What is claimed here is only that the repository already contains the
discipline the final question needs, and contains it in exactly one place, scoped to exactly one
object.

### AQ-2 · 🆕 The measurement that decides the answer: there is no join key

An attribution from a conclusion to the process that produced it needs a shared identifier. Tested
directly, this session:

```
PIPELINE IDENTIFIERS INSIDE THE SCIENTIFIC RECORD
  TASK_ID · CHECKPOINT_ID · GENERATION · ACTOR_ID · REVIEW_ID · MESSAGE_ID
    files under disease-models/    0    0    0    0    0    0
    files under framework/state/   0    0    0    0    0    0

CLAIM IDENTIFIERS INSIDE THE CONTROL PLANE
    "CLAIM-" under ledger/         0            "CLAIM-" under governance/      0

THE ONE SHARED IDENTIFIER
    PMID    appears in ledger/ (4 files, all plan checkpoints) and throughout disease-models/

POSITIVE CONTROL
    the same greps resolve 39 `## CLAIM ` headings in the claim registry and 27 checkpoints
    carrying CHECKPOINT_ID. The instrument was working
```

🔴 **The scientific record and the process record share no identifier except the paper.** A wrong
conclusion can therefore be traced to *which paper was read* and to nothing else — not to which
task, which actor, which generation, which contract, which checkpoint, or which review. **The join
that attribution requires does not exist in the durable state**, and no instrument can supply what
the schema does not carry.

### AQ-3 · What each attribution would require, and whether it exists

| Attribution | Evidence it needs | Exists? |
|---|---|---|
| **→ the Scientist** | the manifest, the packet, the locators, the typed statements, the coverage map | ⚠️ **partly.** The receipt chain verifies (128, this session); the packet under `files/` is on no ref and not in this checkout; the reading protocol is not on this ref |
| **→ the pipeline** | which task, generation and contract produced the reading; whether the freeze preceded the second read; whether a handoff was accepted; whether a resume was idempotent | 🔴 **no.** 0 events of 23 types · 0 `RESUMED_FROM_MILESTONE` · no handoff closure exists even in specification · 0 task records for any actor but `plan` |
| **→ the laboratory** | whether this failure class had occurred before and what was learned | 🔴 **no.** No learning index · `active_lessons/` 0 paths on 54 refs · 0 G.2 proposals · `REVIEW_YIELD` never computed |

### AQ-4 · 🆕 The consequence: elimination lands on the Scientist by default, and that is an artefact of the record

Run the F.4 ordering against AQ-3 with the evidence that actually exists:

```
step 1  did the pipeline fail?     UNANSWERABLE — no events, no handoff closure, no task record
step 2  did the lab fail to learn? UNANSWERABLE — no index, no active lessons, no yield
step 3  did the Scientist reason
        badly?                     PARTIALLY ANSWERABLE — manifest, locators, receipts, C.2 fields
        ↓
🔴 the only layer that can be examined is the only layer that gets blamed
```

**This is the finding.** Not that anyone would blame a Scientist unfairly — no actor has done so,
and no instance of it exists in the record — but that **the durable state supports exactly one of
the three attributions, so an honest investigator with only that state must either name the
Scientist or name nothing.** F.4 already forbids that inference for instruction execution and calls
it by name: *MAI insubordinazione*. The equivalent protection for conclusion production is not
absent by decision; it is absent because the evidence the other two layers would be judged on has
never been written.

By the retraction test (§ D-4), this holds whether the conclusion in question turns out true or
false: it is a statement about what the record can distinguish, not about any conclusion.

### AQ-5 · What would close it — and it is nothing new

Every object AQ-3's second and third rows require is **already specified**, by name, in annexes
this record only quotes:

```
A.1 / A.2 / A.3   the task contract, its ACK, and its claim, per actor        (5 exist, all `plan`)
A.6               the checkpoint, with fingerprint                            (27 exist, 27 carry it)
A.7               RESUMED_FROM_MILESTONE                                      (0 exist)
J.1               the event ledger, 23 minimum types, one writer              (0 exist)
E.2               the LEARNING_INDEX                                          (0 exist as an object)
G.3               REVIEW YIELD, AUTONOMY LEDGER                               (0 computed)
```

🔴 **The gap between LEGEND and an attributable laboratory is instantiation, not design.** Stated
as an observation and nothing else: naming which of these should exist first, or who should write
them, would be a proposal, and a proposal is a G.2 object that Mirror may not adopt and that the
route cannot currently carry (§ ESCALATION). This record therefore stops at the measurement.

---

## BLOCKERS

> Blockers to the model's **use**. Nothing below is assigned; Mirror holds no command.

```
B-1  🔴 NO JOIN KEY BETWEEN THE CONCLUSION AND THE PROCESS. 0 of 6 pipeline identifiers appear in
     disease-models/ or framework/state/; 0 claim identifiers appear in ledger/ or governance/.
     Attribution beyond "which paper" is not derivable from durable state. § AQ-2

B-2  🔴 THE ANALYSIS SURFACE roles/mirror.md NAMES DOES NOT EXIST. J.1's ledger: 23 specified event
     types, 0 events. The role contract already declares the capability blocked. § 2.2

B-3  🔴 NO SEAT HOLDS THE POPULATION. From `mirror`: 1 of 5 task records, 6 of 19 of the other
     actor's checkpoints, 0 of 65 artefacts by other actors. From `main`: 0 of 87 Mirror artefacts.
     Every lab-level number is ref-local unless the union is enumerated by hand. § 2.3

B-4  🔴 THE EVIDENCE SURFACE IS ON NO REF AND NOT IN THIS CHECKOUT. `files/` is `.gitignore:7` and
     absent here; every mechanical LAYER 1 observable reads it. § 1.2

B-5  🔴 THREE INSTRUMENTS ARE ABSENT FROM MIRROR'S OWN REF — `scientist_reading_modes.md`,
     `benchmark_input_surface.py`, `lease_state.py` — all present on `main`. The lease had to be
     derived by running another ref's script against another ref's record. § PRECONDITIONS, § 1.2

B-6  🔴 BOTH METRICS roles/mirror.md CALLS MIRROR'S OWN ARE UNDEFINED. "tasso di invalidazione" and
     "rapporto lavoro-rifatto" each resolve to 1 path across 54 refs — Annex G, which names them
     and does not define them. § 2.4

B-7  🔴 THE G.2 ROUTE IS BLOCKED AT STEP 3. INHERITED. No ACTIVE lease → no Orchestrator to choose
     the independent reviewer. Every finding here that would want to become a rule stops there

B-8  🔴 NO CALIBRATION SURFACE. Re-measured: the union's learning/ and reviews/ namespaces are
     exactly {mirror, orchestrator, plan}. LAYER 1 is mapped against protocol text and zero real
     Scientist artefacts. INHERITED · EPISTEMIC_REVIEW_MODEL-001 § B-1

B-9  🔴 THIS RECORD MAY NOT BE ADOPTED BY ITS AUTHOR. G.2 bars Mirror from self-approving material
     changes to its own review rubric and methods. The route out is B-7
```

---

## OPEN_QUESTIONS

> **Recorded, not resolved.** Questions already open in `EPISTEMIC_REVIEW_MODEL-001` (EQ-1…EQ-10),
> `ANALYSIS-INDEPENDENT-REVIEW-PROTOCOL-001` (IQ-1…IQ-13) and `MIRROR-PROCESS-AUDIT-MODEL-001`
> (OQ-1…OQ-8) are carried forward unchanged and **not restated**. No owner is assigned to any row
> below; assigning one would be a task decision, and H.1 puts task decisions with Orchestrator.

| # | Question |
|---|---|
| **LQ-1** | Should a claim or a commit candidate carry the `TASK_ID` + `GENERATION` that produced it? A.1 already defines both; nothing forbids the reference; nothing requires it. This is the whole of § AQ-2 |
| **LQ-2** | What closes a `HANDOFF`? B.2 lists the message type and no annex gives it a receipt, a state effect or a closing event — so *"frozen before read"* is unverifiable after the fact |
| **LQ-3** | A.6's invalidation rate and A.7's redone ratio are assigned to Mirror and defined nowhere. Who defines them — and is defining them an active-learning-selection change (G.2, barred to Mirror) or a Plan parameter (P2)? Both readings exclude Mirror acting alone |
| **LQ-4** | When a metric is computed, must the computing seat's ref be declared with the value? § 2.4 produced three correct values for one lab, and nothing in C.2's format has a field for the measurement base |
| **LQ-5** | Does F.4's *"MAI insubordinazione"* ordering extend, as a discipline, to attributing a wrong conclusion — or is its scope deliberately limited to instruction execution? |
| **LQ-6** | Does `NO_MIRROR` require a positive declaration that a class was assessed and excluded? Carried from OQ-1 because § 2.5's textual freezes have the same shape: a freeze that held and a freeze never considered leave identical evidence |
| **LQ-7** | With 126 of 152 artefacts on exactly one ref, is an analysis that does not enumerate the ref union *incomplete*, or merely *ref-scoped*? The two readings price § 3.2's near-miss very differently |

---

## WHAT THIS RECORD DOES NOT DO

```
NO ADOPTION        nothing is in force. G.2 bars Mirror from adopting it; B-7 blocks the route anyway
NO PROPOSAL        0 elements marked PROPOSED. § AQ-5 names existing specifications and stops
NO GOVERNANCE      no annex amended, interpreted, reconciled or extended. Quotations are quotations
NO NEW AUTHORITY   every route in § ESCALATION is quoted from H.1, F.1–F.2, G.2 or J.3
NO VALIDATOR       no check, script, schema or field created; 0 paths written under framework/,
                   scripts/ or .claude/
NO SCORING         no score, rank, weight, threshold or severity ordering. The dimension tables are
                   unordered and their rows are not comparable
NO NEW CLASS       every failure class carries the name it already had; where the dispatch's
                   vocabulary has no repository name, that is recorded as an absence and left
NO NEW TERM        "quality gate" appears in the filename the dispatch specified and is used
                   nowhere below as the name of an object. § TERMINOLOGY
NO TRUTH JUDGED    0 scientific claims assessed. § D-4 states the test each finding was put through
NO PEER SUBSTITUTE every truth-form question in § 1.1 is routed to a peer Scientist by C.4 and left
NO ASSIGNMENT      no actor is named as owner of any action; § OPEN_QUESTIONS carries no owners
NO BLAME           § AQ-4 is a statement about what the record can distinguish. No actor is named
                   as having misattributed anything, and no instance of misattribution was found
NO VERDICT         no object reviewed, no author named, no C.2 verdict issued, no review opened
NO SUPERSESSION    all five overlapping records on this ref, and the two on other refs, stand
                   unchanged; overlap is mapped at § OVERLAP_MAP
NO CLOCK STARTED   this is not a MIRROR_RETROSPECTIVE and starts no cadence. G.3's N is unassigned
```

---

## EVIDENCE

Every load-bearing number, with how to reproduce it. Refs as in `measured_at`. Per-ref sweeps use
`git for-each-ref` + `git grep -lI -- <term> <ref>` with `${r}` braced — the unbraced form applies
zsh's `:r` modifier and returns a silent false negative on every ref.

| Claim | Reproduction | Value |
|---|---|---|
| state READY | `framework/state/state_manifest_current.md:141` | `current_state: READY` |
| LINT passes | `python3 framework/scripts/legend_lint.py .` | `VERDICT: PASS` (1 INFO) |
| receipt chain verifies | `python3 framework/scripts/fulltext_receipts.py verify` | `OK: 128 chained receipt(s)`, tail anchored |
| no ACTIVE lease | `main@788c357`'s `lease_state.py --home <main:runtime/orchestrator_lease.md>` | `ACTIVE by derivation: 0`; #3 stored/derived disagreement reported |
| 54 refs · 759 paths | `git for-each-ref` + per-ref `git ls-tree -r --name-only`, union | 54 · 759 (prior record: 53 · 758 at 18:04Z) |
| "quality gate" has no precedent | per-ref `git grep -lI` for `QUALITY_GATE`, `quality gate`, `quality of the process` | **0 · 0 · 0**; controls resolved 26 / 42 / 63 |
| 8 normative G/F/D/R blocks | `grep -rn "^GUARANTEE:" governance/` | 12 total; 8 in normative annexes, 4 in a design record |
| 5 DETECTION lines name Mirror | `grep -rn "^DETECTION:.*[Mm]irror" governance/` + J.1's continuation at `:59` | A.6:88 · A.7:104 · E.5:52 · I.4:73 · J.1:58–59 |
| **0 pipeline identifiers in the scientific record** | `grep -rl <TASK_ID\|CHECKPOINT_ID\|GENERATION\|ACTOR_ID\|REVIEW_ID\|MESSAGE_ID> disease-models/ framework/state/` | **0 for all six, in both trees** |
| 0 claim identifiers in the control plane | `grep -rl "CLAIM-" ledger/ governance/` | 0 · 0 |
| positive control for both | `grep -c '^## CLAIM ' claim_registry_current.md`; checkpoint key dump | 39 claims · 27 checkpoints carrying `CHECKPOINT_ID` |
| PMID is the only shared identifier | `grep -rl PMID ledger/` | 4 files, all `plan` checkpoints 0002–0005 |
| task records: 5, all `plan` | `git ls-tree -r --name-only <ref> -- ledger/tasks` per ref | 13 refs carry all 5 · 15 refs carry 1–4 · **`mirror` carries 1** |
| checkpoints: 27 · fingerprint 27/27 | per-file body test over every `ledger/checkpoints/` path in the union | 19 `plan` + 8 `mirror`; **27 of 27** carry `APPLICABLE_GOVERNANCE_FINGERPRINT` |
| invalidation proxy, three seats | pattern `INCOMPATIBLE\|NOT a compatible\|invalidat` over checkpoint bodies per ref | `mirror` 5/14 · `main` 8/19 · union 10/27 |
| both Mirror metrics undefined | per-ref sweep for `tasso di invalidazione`, `rapporto lavoro-rifatto` | **1 path each — `annex_g_mirror.md`** |
| 0 events emitted | per-ref `git grep -lI EVENT_ID`, then `.jsonl` census of the union | 13 paths, all definitional/analytical; 10 `.jsonl`, none an event ledger |
| 23 minimum event types | `sed -n '/Tipi minimi/,/^$/p' annex_j…` tokenised | 23 |
| 0 `RESUMED_FROM_MILESTONE` instances | `grep -rl` in `ledger/`; per-ref path union | 0 in `ledger/`; 10 paths, all definitional/analytical |
| **0 G.2 proposals instantiated** | per ref: paths with `OBSERVED_FAILURE`, body tested for `FALSIFIER` ∧ `VALIDATION_SAMPLE` ∧ `ROLLBACK` | **1 path — `annex_g_mirror.md`, the definition** (re-run; matches prior record) |
| `REVIEW_YIELD` · `AUTONOMY_LEDGER` | per-ref sweep | 2 paths each, never computed |
| `active_lessons/` absent | path-union prefix count | **0 of 759** |
| artefact consolidation | per-artefact ref count over the 152 `learning/`+`reviews/` paths | 126 on exactly 1 ref · 14 on `main` · all 87 Mirror artefacts on 1 ref |
| no Scientist namespace | `awk -F/` namespace census of the union | `{mirror, orchestrator, plan}` only |
| other actors invisible from `mirror` | `git ls-tree -r --name-only HEAD -- learning/orchestrator learning/plan reviews/orchestrator runtime` | 0 · 0 · 0 · 0 |
| 3 instruments absent on `mirror` | `git cat-file -e HEAD:<path>` vs `main:<path>` | `scientist_reading_modes.md`, `benchmark_input_surface.py`, `lease_state.py` — absent here, present on `main` |
| `files/` unreachable | `.gitignore:7`; `ls -d files` in this worktree | gitignored; **no such directory** |
| 12 reasoning gates | `grep -c '^| \*\*' framework/eval/failure_taxonomy.md` | 12 |
| approval queue exercised | read `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | 2 requests by `plan`, both `APPROVED` / `RESOLVED_BY: operator`, 1 correction, all 2026-08-16 |
| 14 Mirror task_ids, 0 durable records | `grep -h '^task_id:' reviews/mirror/*.md learning/mirror/*.md \| sort -u` vs `ledger/tasks/` | 14 declarations · **0 records** — measured before this file, which is the 15th |
| dispatcher: operator | `grep -h '^dispatcher:'` over both namespaces | 9 of 9 — measured before this file, which is the 10th |
| corpus size | `ls reviews/mirror/*.md`, `ls learning/mirror/*.md` | 52 · 37 (this file included) |
