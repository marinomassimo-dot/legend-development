---
artifact: MIRROR analysis record — the framework by which Mirror would audit the first real
  Scientist experiment: what it receives, the five process questions it may run, the boundary it
  may not cross, the shape of the minimal report, how a finding becomes reusable, and what
  evidence would attribute a failure to LEGEND rather than to the reader. Learning artefact only
record_id: FIRST-PILOT-MIRROR-AUDIT-FRAMEWORK-001
actor_id: mirror
date: 2026-08-22
task_id: FIRST_PILOT_MIRROR_AUDIT_FRAMEWORK_v1
dispatcher: operator
role: >
  mirror — metacognitive layer. This record reviews no object, names no author, issues no verdict,
  and evaluates no scientific claim. It describes a framework; it does not apply one. The
  experiment has not run (§ PRECONDITIONS)
authority: >
  `governance/GOVERNANCE_v3.1.1.md` body §§26, 27, 28, 38, 41, 46; annexes A, C, E, F, G, H, J;
  `roles/mirror.md`; `roles/scientist.md`; `framework/instruction/epistemic_discipline.md`;
  `framework/eval/failure_taxonomy.md`; `framework/eval/learned_gates_registry.md`;
  `governance/plan_defined_parameters.md`.
  🔴 AND FOUR OBJECTS THAT ARE NOT ON THIS REF, re-checked this session and still absent:
  `framework/protocols/controlled_benchmark_ab.md`, `framework/protocols/scientist_reading_modes.md`,
  `framework/scripts/benchmark_input_surface.py` and the whole of
  `framework/eval/benchmarks/BENCH-AB-001/` are ABSENT on `mirror` and were read from `main`.
  Every quotation from them names the ref it came from. The absence is INHERITED — v2 § F-0,
  extended to the tooling by EXECUTION-MODEL § IB-2 — and is re-measured here, not re-discovered.
  Nothing below is adopted or in force. G.2 bars Mirror from self-approving material changes to
  its own review rubric, and an audit framework IS a rubric object. Every element is either
  (a) quoted from a named file at a named ref, (b) a measurement run this session, or
  (c) INHERITED and attributed
classification: OBSERVATION AND ANALYSIS — not governance, not a protocol, not a validator,
  not a gate, not a rubric, not a score, not a report template, not an amendment, not a decision,
  not an authorization to run anything
scope: >
  learning/mirror/ on branch `mirror` only. One new file. No governance/, roles/, framework/,
  ledger/, runtime/, reviews/ or disease-models/ path is written. MODE: READ-ONLY, as dispatched,
  and the constraint is checkable — see § TASK_STATUS
corrects: >
  🔴 YES — ONE SENTENCE OF ONE PRIOR RECORD, AND THIS IS THE FIRST OF THESE RECORDS TO CORRECT
  ANOTHER. `SCIENTIFIC-PROCESS-AUDIT-v2-001` § C-5 states that `FORBIDDEN_PRIOR_OUTPUT_PATHS` is
  *"enumerated from the tree at build time, so the list is a function of when `build` runs"*. It
  is not: the list is a static 23-entry array in `surface_spec.json`, pinned at `BASE_HEAD`, and
  the tool reads it from the spec at three call sites. The measurement, the code lines and the
  consequence are at § C-3. The rest of § C-5 stands
prior_artefact_disclosure: >
  🔴 MATERIAL AND EXTENSIVE. Five records written earlier TODAY, on this ref, cover adjacent
  ground: `SCIENTIFIC-PROCESS-AUDIT-EXECUTION-MODEL-001.md` (the input bundle, the axes, the
  failure classes, the blind spots, the learning tiers, the first report — the direct predecessor
  of this dispatch and its closest overlap), `SCIENTIFIC-PROCESS-AUDIT-v2-001.md` (contamination,
  evidence discipline, uncertainty, pipeline failure), `LABORATORY-QUALITY-GATE-MODEL-001.md`
  (three layers; the attribution question), `MIRROR-PROCESS-AUDIT-MODEL-001.md` (the seven-class
  taxonomy and the retraction test), `EPISTEMIC_REVIEW_MODEL-001.md` (the independence model).
  🔴 AND SIX REVIEWS OF THE EXPERIMENT'S OWN SPECIFICATION: `reviews/mirror/REV-SCIAB-MIRROR-001…006`,
  this seat's hostile reviews of the candidate that defines BENCH-AB-001, last verdict ACCEPT at
  revision 6, with eight of their finding ids quoted inline in the protocol Mirror is assigned to
  adjudicate (EXECUTION-MODEL § IB-5).
  This record SUPERSEDES none of them and CORRECTS exactly one sentence of one, declared above.
  Only items marked 🆕 are new
naming_deviation: >
  DECLARED. 29 of the 39 records under `learning/mirror/` match `SLR-mirror-NNNN[-ADD|-COR-NNN]`;
  this filename was specified by the dispatch and departs from that pattern, as ten others now do.
  🔴 AND IT CARRIES A CORRECTION WHILE NOT CARRYING THE `-COR-` TOKEN THE CONVENTION USES FOR ONE
  — because the dispatch fixed the name and a record does not rename itself to fit a convention no
  rule has adopted. The correction is declared in the front matter and sectioned in the body
  instead. NO NAMING RULE IS ADOPTED AND NO PRECEDENT IS SET
measured_at: >
  mirror@da52ee5e9d3e6eb66455c61d422c4fb1d0e21391 · main@788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
  · 2026-08-22T20:08Z–20:41Z. Every count below was run this session against these refs.
  🔴 THE REF NET CHANGED, AND THE PRIOR NUMBER WAS NOT WRONG. This session counts **57 refs in
  total** — 43 under `refs/heads`, 4 snapshot tags, 1 handoff tag, 4 remotes, 5 codex checkpoint
  refs. The prior record's population of 56 was the same net one ref earlier. Where a sweep needs
  the branch population rather than the whole net, the number used is **43**, and it is named as
  such. Numbers taken from another record are marked INHERITED and attributed
---

# FIRST PILOT MIRROR AUDIT FRAMEWORK — the byte-identical import the freeze depends on is refused by the repository's own ignore rule, and the four fields the report is asked to carry are four names the audited objects already own

> **Mirror asks whether the process that produced a result was reliable. It does not ask whether
> the result is true.** The dispatch states it as a separation to enforce; Annex C.2 states it as a
> definition — `CONFIRMED` is *"nessun difetto rilevato dato l'evidence bundle disponibile"*, **non
> "vero"**. The boundary is not an exemption granted to Mirror. It is the review protocol read
> literally, and it binds every reviewer at every rung.

---

## TASK_STATUS

```
TASK          FIRST_PILOT_MIRROR_AUDIT_FRAMEWORK_v1
DISPATCHER    operator (no ACTIVE lease exists — derived, § PRECONDITIONS)
MODE          READ-ONLY, as dispatched
STATE         COMPLETE for the analysis; NOTHING ADOPTED; NOTHING DECIDED; NOTHING AUTHORIZED
DELIVERABLE   learning/mirror/FIRST-PILOT-MIRROR-AUDIT-FRAMEWORK-001.md — this file, `mirror`

THE DISPATCH'S CONSTRAINT, CHECKABLE
  READ-ONLY                  0 files written outside learning/mirror/; 0 paths under governance/,
                             roles/, framework/, ledger/, runtime/, reviews/, disease-models/.
                             Every command run this session was a read, a digest or a validator
                             invoked in report mode. The two validators that ran —
                             legend_lint.py and public_release_gate.py — write nothing

  🔴 AND ONE CONSTRAINT THE DISPATCH DID NOT STATE, WHICH BINDS ANYWAY. § 4 asks for a "minimal
     report". A report format IS a review-rubric object, and G.2 bars Mirror from self-approving
     one. § 4 therefore maps the four requested fields ONTO the formats that already exist —
     C.2 and the J.0 quadruple — and records what does not map. Nothing in § 4 is PROPOSED,
     because the route's third step has no occupant (§ N-4, § BLOCKERS B-5)

THE TRUTH/PROCESS BOUNDARY, ENFORCED MECHANICALLY
  the retraction test        INHERITED · MIRROR-PROCESS-AUDIT-MODEL-001 § Q-4. Every finding below
                             was written to survive both suppositions — PMID 42397075 confirmed,
                             PMID 42397075 retracted. Candidates that failed it were routed away
                             by C.4 and do not appear
  0 scientific claims assessed · 0 conclusions of PMID 42397075 read. The paper was never opened;
  its packet is git-ignored in this repository (`.gitignore:7`, measured — § IR-4)

CORRECTION CARRIED BY THIS RECORD
  🔴 SCIENTIFIC-PROCESS-AUDIT-v2-001 § C-5, one sentence, on the mechanism by which
     FORBIDDEN_PRIOR_OUTPUT_PATHS is produced. Corrected at § C-3 with the code lines. The
     finding's direction changes; its subject does not
```

---

## PRECONDITIONS — run, not assumed

```
framework/state/state_manifest_current.md:141       current_state: READY
python3 framework/scripts/legend_lint.py .          VERDICT: PASS
                                                    1 [INFO] MISSING_WIKILINK, CLAIM 010, non-blocking
lease_state.py --check                              ACTIVE by derivation: 0
  (script + record extracted from `main` into a       #1 STALE · #2 RELEASED · #3 STALE (stored
   scratch tree — both ABSENT on `mirror`)            EXPIRED — the tool reports the disagreement) ·
                                                      #4, #5 RELEASED
                                                    FINDING: #3 EXPIRED_WITHOUT_RENEWAL
                                                    FINDING: #3 stored ≠ derived; the stored field
                                                             is not authoritative
python3 scripts/public_release_gate.py              1 [BLOCK] · 4 [REVIEW]
```

🔴 **The one BLOCK the publication gate reports today is in Mirror's own output directory, and it
is a true positive of the rule about a value the rule was not written for.**

```
[BLOCK] EMAIL_ADDRESS  reviews/mirror/REV-ORCHSURF-R4-POST-TRANSCRIPTION-FIDELITY.md:73
        "A non-placeholder email address remains in public material."
the value at that line, read this session:
        author/committer  The LEGEND project <legend-project@users.noreply.github.com>
```

It is the repository's **own committer identity**, a GitHub `users.noreply` address that is
undeliverable by construction, reproduced inside a verbatim transcription of a commit object. Two
readings are available and this record selects neither: the rule fired correctly on its literal
text, and the intent it protects — no personal address in public material — is not engaged. It is
recorded here because § IR-3 makes Mirror's adjudication a public-edition artifact subject to this
same gate, and because the seat that would write that adjudication is the seat currently holding
the gate's only BLOCK. **Not fixed here: this dispatch is READ-ONLY and the file is not its
object.**

**There is no Orchestrator.** C.3 — *"Apertura solo via Orchestrator"* — is unsatisfiable by anyone
at this instant, and so is step 2 of the benchmark sequence, which requires *"Orchestrator (lease
ACTIVE)"* to issue the two Task Contracts.

**And there is nothing to audit.** Re-measured across all 57 refs this session, with positive
controls on the same sweep:

```
framework/eval/benchmarks/BENCH-AB-001/first_pass       0 refs
                                       frozen           0 refs
                                       comparison       0 refs
                                       audit            0 refs
                                       adjudication     0 refs
                                       outcome          0 refs
                                       instructions    19 refs   ← POSITIVE CONTROL
                                       population      19 refs   ← POSITIVE CONTROL
reviews/mirror/BENCH-AB-001-ADJUDICATION.md             0 refs   ← Mirror's own step-8 deliverable
deployment/local_instance.md                            0 refs   ← § F-5
ledger/events · ledger/consolidated                     0 refs · 0 refs
active_lessons/                                         0 refs
```

Everything below is **ex ante**: the framework, not its application.

---

## OVERLAP_MAP — what is new, and what is not

> This dispatch is the sixth on adjacent ground in one day and the second to ask for an audit
> design against BENCH-AB-001. The honest first act is to say which parts are already written.

| § here | Prior coverage | Relation |
|---|---|---|
| **§ 1 IR-1** the bundle enumerated as eleven objects, with the producer and step of each | EXECUTION-MODEL § IB-1 (position, not allowlist) | **INHERITED** in its premise; 🆕 as an enumeration with per-object existence counts |
| **§ 1 IR-2** the bundle's root of trust declares itself NOT FROZEN today | — | 🆕 **NEW measurement** |
| **§ 1 IR-3** Mirror's deliverable ref holds none of its inputs, and the adjudication inherits the edition boundary | § IB-2 (tooling absent), § IB-4 (HARD boundary) | **INHERITED** in parts; 🆕 as a statement about the bundle, with the gate's live BLOCK |
| **§ 1 IR-4** 🔴 the frozen tree cannot be imported byte-identically — 7 of its files are refused by `.gitignore:7` | — | 🆕 **NEW, and the record's structural finding** |
| **§ 1 IR-5** `contamination_declared[]` and `blockers[]` have no positive form, while the axis fields next to them do | — | 🆕 **NEW** |
| **§ 2 F-1** "freeze" denotes five distinct objects here | v2 § P-4 named one of them | 🆕 **NEW as an enumeration** |
| **§ 2 F-2** the repository already holds an executable gate for this axis — `FREEZE_SCOPE_GATE` | — | 🆕 **NEW**, and it is on `mirror` |
| **§ 2 F-3** three of the four benchmark freezes pass that gate's tiering; the fourth is a tier-4 case | — | 🆕 **NEW** |
| **§ 2 F-4** the freeze is mechanised and the import is not — 7 subcommands, none of them `import` | § IB-2 measured the 7 subcommands for a different purpose | 🆕 **NEW consequence** |
| **§ 2 F-5** the detection route's object has no recorded address and a bounded retention | § IB-6 named the route and its exclusion | 🆕 **NEW**: the object is unreachable *and* expires at the moment the question can be asked |
| **§ 2 F-6** `FREEZE_TIMESTAMP_UTC` is uncorroborated by the protocol's own words, and the corroborating object is designed and unbuilt | § LE-3 (ledger designed, unbuilt) | **INHERITED** in its second half; 🆕 as applied to freeze ordering |
| **§ 2 C-1…C-2** the standard, the three commands, the two declared contaminations, the corpus | v2 § C-1…C-5 | **INHERITED**, re-measured, not re-derived |
| **§ 2 C-3** 🔴 the forbidden list is static, not build-time — **CORRECTION** to v2 § C-5 | v2 § C-5 states the opposite mechanism | 🆕 **CORRECTION**, with three code lines and the spec |
| **§ 2 C-4** the number stated twice in prose is one more than the command it cites produces | — | 🆕 **NEW measurement** |
| **§ 2 E-1…E-2** four levels not three; the omitted half is the premise tag | v2 § E-1, § E-3; EXECUTION-MODEL § PA-1 | **INHERITED** |
| **§ 2 U-1…U-2** the instruments, and the budget rule as the place uncertainty dies | v2 § U-1…U-4 | **INHERITED**; 🆕 only the receipt-field observation |
| **§ 2 D-1** 🆕 this dispatch REPAIRS the defect the prior one carried | EXECUTION-MODEL § FT-1 flagged the defect | 🆕 **NEW**: the repair, and what it costs to state |
| **§ 2 D-2** 🔴 the last stage of disagreement handling runs AFTER the adjudication that audits it | — | 🆕 **NEW** |
| **§ 3 N-1…N-2** the boundary, routed twice; the retraction test | v2 § FQ-4, § FQ-5; MIRROR-PROCESS-AUDIT § Q-4 | **INHERITED**, quoted |
| **§ 3 N-3** the one dimension row that sits on the boundary, and the rule that keeps it on the process side | v2 § R-3 (two objects); § PA-1 (second-order form) | 🆕 **NEW as applied to `CLAIM PRECISION`'s `Type` question** |
| **§ 3 N-4** no route exists for Mirror disagreeing with a blind audit verdict — the author is ephemeral by construction | § PO-3, § PO-4 (no AUTHOR_RESPONSE step; AUTHOR is not one actor) | 🆕 **NEW mechanism** for one object class |
| **§ 4 R-1** 🔴 all four requested field names are already occupied, three of them by the audited objects | — | 🆕 **NEW measurement**, and the section's sharpest finding |
| **§ 4 R-2** the format is the J.0 quadruple with `DETECTION` removed | — | 🆕 **NEW** |
| **§ 4 R-3** it is not C.2, and C.2 calls itself the only format | § PO-2, for the five-question form | **INHERITED**, re-derived for a four-field form |
| **§ 4 R-4** `RECOVERY` is an act by a named actor in all eight normative blocks, and Mirror appears in one, via G.2 | — | 🆕 **NEW measurement** |
| **§ 5 L-1** the tiers, the budget, where a finding lands | § LE-1…LE-4 | **INHERITED**, re-verified |
| **§ 5 L-2** 🔴 E.2's confirmation arithmetic assumes independent instances; 18 of 20 input paths are byte-identical | — | 🆕 **NEW**, with the manifest's own partition as the discriminator |
| **§ 5 L-3** body §46 already supplies the promotion filter, four-way | — | 🆕 **NEW** |
| **§ FQ** LEGEND or the Scientist? | LAB-QUALITY § ATTRIBUTION (three-way); v2 § FQ (science or system); EXECUTION-MODEL § FQ (knowable from where) | **DIFFERENT QUESTION** — § FQ-1 states the difference before using anything |
| **§ FQ-3** §46 partitions four ways; the dispatch's binary has no bin for `noise` | — | 🆕 **NEW, and the answer's structural leg** |
| **§ FQ-5** F.4's only actor-terminating branch is unreachable under `AUTONOMOUS_COMPLETE` | § FT-3 (the ordering) | 🆕 **NEW consequence** |

---

## 1 · INPUT RECEIVED

> The dispatch asks for *exactly* what Mirror receives. The protocol answers by sequence position;
> this section converts that into an enumeration, then measures what each object is today.

### IR-1 · The bundle, enumerated — and the enumeration is derived, not declared

INHERITED premise (EXECUTION-MODEL § IB-1): **Mirror's inputs are fixed by its position in
`controlled_benchmark_ab.md` §5 (`main`), not by an allowlist.** Mirror is step 8; its inputs are
what steps 1–7 left. 🆕 what this section adds is the enumeration, with the producer, the step and
the existence count of each object across the 57-ref net:

| # | Object | Producer · step | Exists |
|---|---|---|---|
| 1 | `benchmark_manifest.json` (`FROZEN_SHA256`) | Plan · 1 | spec only, **not frozen** — § IR-2 |
| 2 | `population/evidence_units.json` | Plan · 1 | 19 refs |
| 3 | `frozen/RECEIPT-scientist-a.json` | Plan · 5 | 0 refs |
| 4 | `frozen/RECEIPT-scientist-b.json` | Plan · 5 | 0 refs |
| 5 | `first_pass/scientist-a/…` (import) | Plan · 5 | 0 refs — and § IR-4 |
| 6 | `first_pass/scientist-b/…` (import) | Plan · 5 | 0 refs — and § IR-4 |
| 7 | `comparison/comparison_matrix.md` | Plan · 6 | 0 refs |
| 8 | `comparison/unresolved_disagreements.md` | Plan · 6 | 0 refs |
| 9 | `audit/locator_audit-scientist-a.md` | blind agents · 7 | 0 refs |
| 10 | `audit/locator_audit-scientist-b.md` | blind agents · 7 | 0 refs |
| 11 | the two Task Contracts + `TASK_ACK` + `TASK_CLAIM` | Orchestrator · 2 | 0 contracts for either scientist |

Inside 5 and 6, per `OUTPUT_SCHEMA.md` (`main`): the work manifest, the dossier,
`output/claim_candidates.md`, `output/receipt.json`, `output/renders/…`, and — MODE B only —
`output/critical_reading.md`.

🔴 **Nothing in the protocol says *these objects and no others*.** The readers receive
`ALLOWED_PATHS`: a complete allowlist, enumerated, digested, and checkable by command. Mirror
receives a position. That asymmetry is INHERITED (§ IB-1, § IB-2) and is not re-argued here.

### IR-2 · 🆕 The bundle's root of trust declares itself NOT FROZEN, today

Object 1 is the root: every other object's identity is bound to it —
`INPUT_MANIFEST_SHA256` is recorded in **each actor's freeze receipt**, so the receipts point at
the manifest and the manifest points at the surfaces. Read this session at `main`:

```
_state          "PREPARED — NOT FROZEN. Freezing happens at build time, immediately before
                 handover, and only after every precondition of controlled_benchmark_ab.md §1
                 is satisfied. The fields below marked DERIVED_AT_BUILD are computed by the
                 command named beside them and are deliberately absent here: a digest written
                 by hand today would be a value that ages without anything detecting it."
FROZEN_SHA256   null
HANDOVER        {scientist-a: {at: null, surface_tree_sha256: null, memory_scope_absent: null},
                 scientist-b: {…}}
EVALUATION_POPULATION.sha256   "DERIVED_AT_BUILD"
```

**This is not a defect and is stated as the opposite.** The file refuses to carry a digest it
cannot compute yet, and says why in a sentence that names the failure mode it is avoiding. What it
means for the audit is exact and narrow: **an audit that opens by asserting "the manifest was
frozen" is asserting the precondition that gates handover** (P-7 of §1: *"Input surfaces built,
verified, manifest frozen"*), and today that field is `null`. The process form of the question is
the checkable one — *was `FROZEN_SHA256` non-null before the `HANDOVER` block was written, and
does each receipt's `INPUT_MANIFEST_SHA256` equal it* — and both halves are facts in objects Mirror
receives.

### IR-3 · Mirror's deliverable ref holds none of its inputs, and the adjudication inherits the edition boundary

Measured this session:

```
on `mirror`   framework/eval/benchmarks/BENCH-AB-001/          ABSENT (whole tree)
              framework/protocols/controlled_benchmark_ab.md   ABSENT
              framework/protocols/scientist_reading_modes.md   ABSENT
              framework/scripts/benchmark_input_surface.py     ABSENT
              framework/eval/failure_taxonomy.md               PRESENT  ← POSITIVE CONTROL
              framework/eval/learned_gates_registry.md         PRESENT  ← and § F-2 needs it
durable seat for the adjudication (§6, main), verbatim:
              adjudication/MIRROR-ADJUDICATION.pointer.md   Plan   "path on branch mirror
                                                                   + sha256 of Mirror's record"
```

INHERITED (§ IB-2): the pointer establishes that the record has not changed since it was pointed
at, and establishes nothing about where its statements came from. 🆕 the input-side statement is
the mirror image: **the adjudication is written on a ref that carries none of the eleven objects it
adjudicates**, so every act of step 8 is a cross-ref read, and the protocol that says which reads
are legitimate is itself one of the absent files.

And one consequence that is not about sourcing. `reviews/mirror/` is public-edition material;
CLAUDE.md's edition boundary binds it (*"contains no individual-level record… Do not reintroduce
individual linkage"*), and `scripts/public_release_gate.py` enforces it. That gate reports one
BLOCK today, in this directory (§ PRECONDITIONS). **The adjudication is not merely a review; it is
a publishable artifact that passes or fails a gate**, and the gate's state is a precondition of the
deliverable in the same way `verify` is a precondition of handover.

### IR-4 · 🔴 🆕 The frozen tree cannot be imported byte-identically, and the rule that refuses it is the repository's own

§5 step 5 and §6 (`main`) both say the import is byte-identical:

> step 5 · Plan — *"**FREEZE** each reading the moment its completion is declared… then **IMPORT**
> byte-identical into the LEGEND repository"* → `first_pass/<ACTOR_ID>/…`
>
> §6 · `first_pass/scientist-a/…    Plan (import, byte-identical from A's frozen tree)`
>
> §7 · *"The import into `first_pass/<ACTOR_ID>/` is byte-identical and the receipt's digests are
> the check. **Anyone can re-derive them from the import.**"*

The frozen tree contains the packet. `surface_spec.json` `source_files` (`main`), enumerated this
session — **seven files, every one of them under `files/`**:

```
files/fulltext/PMID42397075_Aqeilan2026.pdf                              article_binary
files/fulltext/PMID42397075_Aqeilan2026_fitz.txt                         article_text
files/fulltext/PMID42397075_Aqeilan2026_assets/brain-2025-03809-File008.pdf … File012.pdf
                                                                         supplement_text ×5
```

And `files/` is ignored by this repository, at the import path, measured with the tool that
decides it:

```
$ git check-ignore -v framework/eval/benchmarks/BENCH-AB-001/first_pass/scientist-a/\
files/fulltext/PMID42397075_Aqeilan2026.pdf
  .gitignore:7:files/     …/first_pass/scientist-a/files/fulltext/PMID42397075_Aqeilan2026.pdf

$ git check-ignore -v …/first_pass/scientist-a/output/receipt.json      → NOT IGNORED
$ git check-ignore -v …/first_pass/scientist-a/roles/scientist.md       → NOT IGNORED
$ git ls-tree -r --name-only main -- files/fulltext | wc -l             → 0 tracked
```

🔴 **The ignore rule is not incidental: it is what keeps publisher full texts out of the public
edition.** So the import has two horns and the protocol selects neither:

```
HORN A — import faithfully      7 of the tree's files are refused by .gitignore:7. The committed
                                import is NOT byte-identical to the frozen tree. `verify-freeze`
                                run against it reports REMOVED ×7 plus a TREE_SHA256 mismatch —
                                i.e. the re-derivation §7 offers to "anyone" FAILS on a correct
                                import, and fails in the two shapes §7 built the command to detect
HORN B — force the import       seven copyrighted publisher PDFs enter a public repository. And
                                measured: public_release_gate.py carries NO rule about `files/`,
                                PDFs or binaries — the ignore rule is the only mechanism, and
                                `git add -f` defeats it leaving a green gate
```

**The resolving distinction already exists in an object Mirror receives**, and naming it is not a
proposal: the freeze receipt's `FILES[]` carries `role ∈ input · output · unexpected`, and
`OUTPUT_FILE_SET` / `UNEXPECTED_FILE_SET` are *"enumerated separately"* (§7). An import scoped to
one of those roles, with the re-derivation scoped to the same subset, is well-defined with nothing
new. What does not exist is a clause saying which scope the import has — and § F-4 measures that
the tool has no `import` subcommand to make the scope a fact rather than a practice.

**What this is for the audit, stated at the right strength.** It is not evidence that anyone will
import wrongly. It is that **the one link in the chain of custody that produces Mirror's largest
input is the one link with no command, no declared scope, and a repository rule that refuses its
literal reading.** Whichever horn is taken, the receipt-versus-import comparison Mirror would run
first has an outcome that is not `PASS` for reasons that are nobody's error.

### IR-5 · 🆕 Two receipt fields have no positive form, and the field beside them does

`OUTPUT_SCHEMA.md` §4 (`main`) — the reader's own receipt, written before freeze, imported into
Mirror's bundle:

```json
  "self_check": {
    "locators_inside_surface": true,
    "no_not_read_in_coverage": true,
    "all_claims_typed": true,
    "negatives_carry_premise_and_revival_trigger": true,
    "mode_b_axes_all_answered": "n/a | true"
  },
  "blockers": [],
  "contamination_declared": []
```

with the standing instruction *"Every value is a fact you checked, not an intention"*, and
`BENCHMARK_INSTRUCTIONS.md` §6 (`main`) making declaration rational:

> *"If you break one by accident, **say so in `output/receipt.json`**: a declared contamination is
> a usable result, and an undeclared one silently invalidates the experiment for everyone."*

🔴 **`self_check` has five booleans; `blockers` and `contamination_declared` have empty arrays
printed in the template.** A `true` is an assertion a reader had to write. An empty array copied
out of the schema is indistinguishable from a field nobody considered — and the by-hand checklist
of `BENCHMARK_INSTRUCTIONS.md` §5, five items long, does not include either field.

**The repository already owns the repair pattern and applies it one file away.** MODE B's axes may
not be silent: *"An axis with none carries **"searched; none found"** and says *what was searched*…
Silence on an axis is an incomplete reading, not a clean paper."* The same shape — a positive
declaration of a negative — is what would make an empty `contamination_declared` an assertion.

**Mirror's form of this is second-order and stays on the process side:** not *was there
contamination* (that is what `verify` measures), but *is the reader's declaration channel evidence
of anything, or is an empty array the schema's default surviving into the record*. Recorded, not
proposed: § R-1 explains why a field-shape change is a rubric object.

---

## 2 · PROCESS QUESTIONS

> Five axes, dispatched. Two of them — freeze integrity and disagreement handling — are new to this
> ground; three are re-measured from records written earlier today and are marked as such rather
> than rediscovered.

### 2.1 · FREEZE INTEGRITY

#### F-1 · 🆕 "Freeze" denotes five different objects here, and only one is this axis's

An audit finding lands on an object. Measured across the normative corpus on `mirror` and the
protocol at `main`:

| # | The freeze | What it pins | Where |
|---|---|---|---|
| 1 | **the governance design** | v3.1.1 itself: *"Design FROZEN: la v3.2 nascerà dai dati del laboratorio, o non nascerà"* | body §§1, 50; `annex_g_mirror.md` G.3 *"(freeze)"*; `roles/mirror.md` |
| 2 | **each annex's text** | `status: FROZEN` in the front matter of all 11 governance files (measured: 11) | `governance/*.md` |
| 3 | **the benchmark input manifest** | `FROZEN_SHA256` over every field except `HANDOVER` | protocol §3 |
| 4 | **the evaluation population** | 65 units, digest in the manifest, *"cannot be redefined after the readings exist"* | protocol §8.1 |
| 5 | **each first pass** | `TREE_SHA256` + `FILES[]` + `FREEZE_TIMESTAMP_UTC` + `FIRST_PASS_STATE` | protocol §7 |

Plus two pins that are freezes in effect and not in name: **`BASE_HEAD cbce3016`**, and the
**23-entry `forbidden_prior_output_paths`** derived from it (§ C-3).

🔴 **The dispatch's axis is #5, and #3 and #4 are its preconditions.** #1 and #2 are a different
subject and a finding written against them would be a governance finding wearing a benchmark
label. Naming the five costs one table and prevents the class of error where an audit reports a
true fact about the wrong object.

#### F-2 · 🆕 The repository already holds an executable gate for exactly this axis, and it is on this ref

`framework/eval/learned_gates_registry.md` — 79 rows, 21 `ACTIVE_EXECUTABLE`, 57 `ACTIVE_METHOD`
(measured; the second number is a coincidence with the ref net and is not it). Among the
executable ones, `FREEZE_SCOPE_GATE`, whose companion checker is present here
(`scripts/test_freeze_scope.py`). Quoted, because the audit axis is its subject:

> **Freeze what you consumed, not the container it arrived in.** Three tiers, chosen per input,
> never one rule for all: (1) *immutable artefacts* … whole-file SHA-256 …; (2) *append-only
> ledgers* — pin **prefix length + prefix digest** …; (3) *living canonical files* — pin the
> **extracted scope actually consumed** …
>
> Two corollaries. **A verifier must never be a sealed input of the seal it implements** … And **a
> freeze must declare its own lifecycle**: frozen-at revision plus whether the window is open or
> closed …
>
> [fourth tier] **A freeze over living state reports drift; it does not assert violation.**

**This is the axis's instrument and it is not Mirror's to invent.** It is an existing
`ACTIVE_EXECUTABLE` gate on Mirror's own ref, learned from a measured 2026-08-06 failure, and the
audit question it supplies is one sentence: *for each of the five freezes, is the tier the right
tier, and does the freeze declare its own lifecycle?*

#### F-3 · 🆕 Applied: three of the four benchmark freezes pass that tiering, and the fourth is a tier-4 case

| Freeze | Tier used | Correct? | Lifecycle declared? |
|---|---|---|---|
| input manifest (#3) | 1 — whole-object digest, `FROZEN_SHA256` | ✔ the object is immutable by construction; the one mutable block (`HANDOVER`) is **excluded by name** from the digest | ✔ `_state: PREPARED — NOT FROZEN`, and `FROZEN_SHA256: null` until it is |
| population (#4) | 1 — whole-file digest recorded in the manifest | ✔ derived once, deterministically (*"identical bytes across two consecutive runs"*), never re-derived after reading | ✔ `fixed_before_reading: true` |
| first pass (#5) | 1 — `TREE_SHA256` + per-file digests | ✔ §7 makes the object immutable: post-freeze corrections are *"a **new dated file**… with the original left as frozen"* | ✔ `FIRST_PASS_STATE ∈ COMPLETE_DECLARED_BY_ACTOR · ABANDONED · TIMED_OUT` — INHERITED, v2 § P-4 |
| forbidden list (pin) | 1 — a static array | 🔴 **the population it pins is living**: the same command yields 20 paths at `BASE_HEAD` and **32** at `main` (§ C-4) | ✖ no frozen-at field in the array itself; the derivation note carries the ref |

**And the first corollary holds, in the direction that matters.** `benchmark_input_surface.py` — the
tool that computes and checks every one of these digests — is **not** in the surface it seals: the
11 `common_files` are `CLAUDE.md`, the two instruction files, `roles/scientist.md`, four discipline
documents, `failure_taxonomy.md`, `deepdive_manifest.py` and `corpus_firewall.py`. The sealing tool
is absent from the sealed set. `deepdive_manifest.py` *is* sealed, and that is the correct
direction: it is a **verifier of the reading**, sealed as an *input* so the record pins which
validator version ran — not a verifier sealed by the seal it implements.

**The tier-4 reading of the forbidden list is the one that matters, and it is contained.** Under
the gate's fourth rule the pin *reports drift, it does not assert violation* — and here the drift
has no path into the surface, because a different mechanism is exhaustive: `verify` checks *"no file
present in either surface outside `ALLOWED_PATHS`"*, and the surfaces are built by copying an
allowlist into an empty directory. A prior-output path created after `BASE_HEAD` cannot be in a
surface, whether or not it is in the forbidden list. 🔴 **So the correct Mirror finding is not that
the list is stale. It is that the list is not the guarantee** — and J.0's closing rule bites on any
report that credits it as one: *"Vietato a qualsiasi documento o attore descrivere questi meccanismi
con vocabolario più forte del protocollo compensativo."*

#### F-4 · 🆕 The freeze is mechanised; the step that hands the frozen bytes to Mirror is not

`benchmark_input_surface.py` (`main`), the complete subcommand surface, re-measured:

```
build · verify · freeze · verify-freeze · population · locators · tree-digest        7
subcommands named `import`, or taking first_pass/ as an object                       0
```

`verify-freeze` recomputes *set-wise, never by count* — `ADDED` / `REMOVED` / `MODIFIED`, each
enumerated — plus an identity check that reads `ASSIGNMENT.md` **from inside the tree** so a receipt
pointed at the wrong actor's tree fails on identity rather than on digests. Read this session, the
implementation matches: `tree_digest(root)`, a set comparison against `receipt["FILES"]`, and a
final refusal even when every file matches but the digest does not (*"the digest function is not the
one that produced this receipt"*).

🔴 **It takes `--surface <tree>`, so it can be re-run by Mirror against the import — and § IR-4 is
why that run does not return `PASS` on a faithful one.** Two further conditions are unstated: the
import must preserve the surface's *relative* paths under its new root (the digest is a function of
paths), and no clause says it does. **A check that anyone can run, against a tree nobody's command
produced, under a path convention no clause fixes** is the exact state this axis exists to notice.

#### F-5 · 🆕 The one unmechanised freeze rule is detected by an object with no address and a bounded life

INHERITED (v2 § C-4, EXECUTION-MODEL § IB-6): §7's ordering rule — *neither actor sees the other's
first pass until both are frozen* — is labelled `PROCEDURAL`, *"Nothing mechanises it"*, and its
block reads:

```
GUARANTEE_PROVIDED:            none by mechanism — discipline only
FAILURE_MODE_STILL_POSSIBLE:   Plan reads or relays A's first pass to B before B freezes
DETECTION:                     the two receipts carry FREEZE_TIMESTAMP_UTC and SURFACE_COMMIT;
                               an inspection of B's commit history against A's freeze time
                               makes a violation VISIBLE AFTER THE FACT, never prevented
RECOVERY:                      the benchmark is void for the second reader; the outcome says so
```

🆕 **What is new is the state of the object `DETECTION` names.** *B's commit history* lives in the
surface repository, and:

```
the receipt records            SURFACE_COMMIT — one sha, the tip. Not the log
the receipt does NOT record    SURFACE_ABSOLUTE_PATH — "explicitly NOT RECORDED" (§7), because
                               BENCH_ROOT is a local-instance value
the file named as its home     deployment/local_instance.md   →   0 of 57 refs, measured
the import carries             the frozen tree, not the repository (§ IR-4) — no reflog, no history
retention                      "the surface repository is retained as evidence until the outcome
                               is canonical" (§2.2)
```

🔴 **The retention window closes at the moment the question becomes askable.** Step 8 is Mirror's
adjudication; step 9 is the outcome; *canonical* is downstream of both. So the artifact that would
settle the protocol's only unmechanised guarantee is unaddressed in the durable record, absent from
the import, and guaranteed to exist only until the outcome that Mirror's own step feeds.

**Not a proposal.** The two halves that would make it tractable — commit *metadata* admitted, commit
*content* excluded — were stated in EXECUTION-MODEL § IB-6 as a distinction *someone with authority
could draw*, and drawing it is a rule.

#### F-6 · The freeze's own timestamp is uncorroborated, and the corroborating object is designed and unbuilt

The protocol says it about itself (§4.4, `main`), in the `freeze` row of its guarantee table:

> `FAILURE_MODE_STILL_POSSIBLE` — *"a substitution made **before** the freeze; **the timestamp is
> this process's clock and nothing corroborates it**"*

🆕 the second half: the object that *would* corroborate an ordering claim is specified and does not
exist. J.1's event types include `WORK_COMMIT`, `CHECKPOINT_WRITTEN` and `TASK_COMPLETE`, each with
a timestamp and an `ACTOR_ID`; `plan_defined_parameters.md` § P7 decides its design — option (a),
`ledger/events/<ACTOR_ID>.jsonl`, append-only, consolidated by Plan — and closes *"Tracked as a
debt; not yet built."* Measured: `ledger/events` and `ledger/consolidated`, **0 of 57 refs**;
`roles/mirror.md` names that ledger Mirror's **primary analysis surface** and marks the capability
*"blocked: the ledger has no writer yet"*.

**So the axis's three claims have three different evidential states**, and an audit that reports
them at one strength is the J.0 violation:

```
"the tree holds what the receipt froze"      MECHANICAL — verify-freeze, set-wise, re-runnable
                                             (with § IR-4's caveat on what it is run against)
"the freeze was taken before the content     ATTESTED — one clock, declared uncorroborated by the
 was read"                                   protocol itself; no second source exists on any ref
"B did not see A before B froze"             PROCEDURAL — no mechanism; detection route § F-5
```

### 2.2 · CONTAMINATION RISK

#### C-1 · The standard, and the three commands — INHERITED

INHERITED in full from v2 § C-1 and § C-2, quoted rather than re-derived: body §26 and Annex C.3
both say `Independence by task framing, not by information barrier`, so **an audit scoring
BENCH-AB-001 against information-barrier independence scores it against a guarantee the governance
disclaims twice**; and the three blinding checks — parity, exactly-two-differing-files, forbidden
paths absent + content scan clean — *"are `benchmark_input_surface.py` subcommands run by Plan…
Mirror's object is whether they were run, when, in which mode, and what their census said."*

The two declared contaminations of the variable are also INHERITED (v2 § C-3): session variance is
not separable from mode at n=1, and each reader can read the other's mode directive because
`scientist_reading_modes.md` §4–§5 is a **common** file — recorded by the protocol as *"a known
contamination of the variable… and not softened"*, attributed inline to **(Mirror R-2)**.

#### C-2 · What the surface partition is, measured — because § L-2 and § FQ-4 both need it

`surface_spec.json` (`main`), enumerated this session:

```
common_files       11    byte-identical in both surfaces
source_files        7    byte-identical in both surfaces — the packet
per_actor_files     2    ASSIGNMENT.md · benchmark/MODE_DIRECTIVE.md, per reader
empty_dirs          4
                  ───
input paths        20    of which 18 are the SAME BYTES for both readers
```

**Eighteen to two.** That ratio is the experiment: *"A third differing file is a broken benchmark,
and `verify` reports it."* It is also, in § L-2 and § FQ-4, the discriminator that decides whether
two observations are two instances or one.

#### C-3 · 🔴 CORRECTION — the forbidden list is static, not enumerated at build time

`SCIENTIFIC-PROCESS-AUDIT-v2-001` § C-5 states:

> *"`FORBIDDEN_PRIOR_OUTPUT_PATHS` is enumerated **from the tree at build time**, so the list is a
> function of when `build` runs, and a benchmark built today excludes a different set than one
> built on 2026-08-18."*

**It is not.** Measured this session, three ways:

```
surface_spec.json `forbidden_prior_output_paths`      a static array — 23 entries, enumerated above
benchmark_input_surface.py, every use of it           spec["forbidden_prior_output_paths"]
                                                      at lines 230, 531 and 1379 — read from the spec
every git invocation in that tool                     _git(root, "rev-parse"…) · "status --porcelain",
                                                      inside `freeze` only. There is no `git grep`,
                                                      and no enumeration of any tree but the surface
```

and the design says so in its own words. The manifest's `_enumerated_in`: *"surface_spec.json
`forbidden_prior_output_paths` — the list a command checks, **kept in one place so it cannot drift
from the one a reviewer reads**"*. The protocol's §3 field description: *"every tracked path **at
BASE_HEAD** naming the paper"* — `BASE_HEAD`, not *at build*.

**What changes, and what does not.** The subject of v2 § C-5 stands: the corpus contamination the
surface exists to escape has grown, and that growth is real and measured (§ C-4). What was wrong is
the mechanism, and correcting it moves the finding from one class to another: it is not *"different
builds check different sets"* (they check the same 23), it is *"a tier-1 pin over a living
population"* — § F-3, whose consequence is contained by the closed allowlist rather than by the list
itself. The corrected finding is narrower in one direction and sharper in the other.

**Recorded as a correction, not as a supersession.** The prior record is not edited; nothing else in
it is disturbed; and this paragraph is the whole of the change.

#### C-4 · 🆕 The number stated twice in prose is one more than the command it cites produces

The derivation is recorded beside the list, which is the repository's own rule — *"Every count is an
enumerated set or carries the command that produced it"* (§8.5). Run verbatim this session:

```
$ git grep -l -i -E '42397075|awag239|Aqeilan 2026|Aqeilan2026' cbce3016 -- . \
    | grep -v '^governance/candidates'
  → 20 paths          (and 0 of the matches are under governance/candidates, so the filter is
                       a no-op twice over: the rev-prefixed output cannot match a `^governance/`
                       anchor either)
$ the same command at main                                              → 32 paths
$ len(surface_spec.json["forbidden_prior_output_paths"])                → 23
```

And the list reconciles at **20**, not 21: `20 + claim_registry_current.md + working_model_current.md
+ controlled_benchmark_ab.md = 23`, which is exactly the three additions the derivation note names.

🔴 **The artifact is right and the prose is not.** *"twenty-one tracked files name it"* appears in
protocol §2.1 and *"→ 21 tracked paths at BASE_HEAD"* in the manifest's `_derivation`; the built list
is consistent with 20. The likeliest cause is benign — a working-tree run, which sees untracked files
a rev-scoped `git grep` cannot — and it is exactly the class this axis is for: a number carried in
prose, cited to a command, one greater than the command returns, in a file whose own standard is that
counts carry their commands. **Recorded, with the command, for whoever holds the number.** It changes
nothing about the surface.

#### C-5 · The corpus is contaminated and Mirror sits in it — INHERITED, re-verified

INHERITED (v2 § C-5, EXECUTION-MODEL § IB-3), re-run today with the unique-identifier net
(`42397075|awag239`) and unchanged since this morning:

```
tracked paths naming the paper, main      32          mirror   24
the colliding path  disease-models/wwox/research/deepdive_manifests/PMID42397075.json
                                          PRESENT on both
```

with § IB-3's admissibility distinction carried forward unresolved: a prior-output path is
admissible to Mirror as a **process** fact (was it forbidden, was it absent, did `verify` say so)
and inadmissible as a **content** baseline (does the reader's claim agree with what LEGEND
previously concluded) — the second fails the retraction test and is a science question C.4 routes
to a peer Scientist.

### 2.3 · EVIDENCE DISCIPLINE — INHERITED, with the omitted half restated

INHERITED (v2 § E-1, § E-3; EXECUTION-MODEL § PA-1), because nothing this session changes it:

```
the repository types FOUR levels, not three     DATO · INFERENZA · IPOTESI · ESPANSIONE
                                                (epistemic_discipline.md §1, on `mirror`)
the split is already drawn                      §8.2 EPISTEMIC DISCIPLINE: "mechanical for
                                                presence; adjudication for substance" — Plan; Mirror
the half most audits omit                       the PREMISE tag. Every rejection or non-trivial
                                                conclusion names its premise and tags it
                                                DATO | INFERENZA | DEFAULT_FROM_TEXTBOOK; every
                                                negative carries a REVIVAL_TRIGGER
```

**Mirror's form is second-order** (§ PA-1's rule, applied): not *is this statement true*, but *is
the type it claims the type the audited evidence bears* — a question whose input is the blind
audit's per-triple verdict, and whose boundary is § N-3.

### 2.4 · UNCERTAINTY PRESERVATION — INHERITED, with one new observation

INHERITED (v2 § U-1…U-4): three instruments carry it at three layers — C.2's `RESIDUAL_UNCERTAINTY`
and `EVIDENCE_NEEDED` at the review layer, `Uncertainty` and `Limitations` as required claim fields
at the reading layer, MODE B's *"searched; none found — searched: <what>"* at the axis layer — and
the place uncertainty most plausibly dies is the budget rule, which both mode directives state
identically:

> *"**Do not compress depth or coverage for token, time or cost.** A reading shortened for budget
> produces a receipt that overstates itself… A declared partial reading is a legitimate, useful
> result. A silently thinned complete reading is a false record."*

🆕 the one addition, and it belongs beside § IR-5: the receipt has a field that makes thinning
*declarable* — `evidence_depth: complete_fulltext_read | partial_fulltext_read` — and the
coverage map that would show it (*no `not_read`*) is checked by a `self_check` boolean the reader
writes about its own work. **The measurement that would test that attestation is the tree census,
which is computed after the reader stops** (EXECUTION-MODEL § FQ-4). So uncertainty preservation is
auditable exactly to the extent that the two receipts disagree — and INHERITED § FQ-4 is the reason
only a seat downstream of the freeze holds both.

### 2.5 · DISAGREEMENT HANDLING

#### D-1 · 🆕 This dispatch repairs a defect the previous one carried, and the repair is worth naming

`SCIENTIFIC-PROCESS-AUDIT-EXECUTION-MODEL-001` § FT-1 recorded, with four normative clauses quoted
in full, that the prior dispatch listed **"unresolved disagreement"** among *failure classes to
name* — while body §27, Annex C.3, `roles/scientist.md` and protocol §8.3 all declare it a
**legitimate outcome**, and body §27 names the opposite as the error in the same sentence: *"la
sintesi forzata è un errore."*

🔴 **This dispatch asks about *disagreement handling*, not about disagreement**, and that is exactly
the object that can fail. The change is one word wide and it moves the axis from a class the
governance forbids scoring to a class the governance requires someone to produce. Recorded because a
process record that only notes what dispatches get wrong is not measuring the process.

#### D-2 · 🆕 The last stage of disagreement handling runs after the adjudication that would audit it

The three stages, from §5 (`main`), with their steps:

```
step 6   Plan          comparison/unresolved_disagreements.md — "listed, typed, unresolved";
                       Plan never decides what a claim means (§28)
step 8   MIRROR        adjudication of the PROCESS
step 9   Plan          outcome summary — disagreements carried, no composite
step 10  Orchestrator  "scientific disagreements → Annex C review (R2/R3) if warranted —
                       OUTSIDE the benchmark record"
```

🔴 **Two of the three stages Mirror is asked to audit are not Mirror's, and one of them has not
happened when Mirror writes.** Step 10 is after step 9, which is after step 8; and it is explicitly
*outside* the benchmark record, so it leaves no artifact in the directory Mirror's bundle is drawn
from. An audit of "disagreement handling" at step 8 can therefore reach step 6's act and not
step 10's, and a report that does not say so describes a three-stage handling on evidence of one.

**The operative test, in the clauses' own terms, and it is entirely a step-6 test:**

```
1  is every flagged row IN comparison/unresolved_disagreements.md   §8.3 makes the file the
                                                                    deliverable, not the exception
2  is each one EXPLAINED                                            "con spiegazione" is the whole
                                                                    qualifier — C.3, body §27
3  is each one TYPED, with both readings quoted                     §8.3: "both readings' statements
                                                                    quoted and typed"
4  was it resolved by anyone who may not resolve it                 §28: Plan "NON risolve significato
                                                                    scientifico conteso"; §5 step 6:
                                                                    "listed, never resolved by Plan"
```

All four survive the retraction test — they are true or false of the record whether or not the paper
stands — and all four are Mirror's under C.4's `SYSTEM → Mirror`. **Which reading is right is not on
the list**, and § N-1 is why.

#### D-3 · Where the real failure hides — INHERITED, restated at this axis

INHERITED (§ FT-1's closing paragraph): the failure adjacent to a legitimate disagreement is *an
unresolved disagreement **without** the explanation, or one that never reaches the file*. 🆕 the
alignment rule adds a second: §8.3 aligns rows *"by shared locator anchors… structural, by unit, not
by Plan's reading of whether two claims 'mean the same'"* — so **a disagreement between two claims
that cite no common unit cannot become a row at all**. It is not concealed; it is not
representable. Whether that class exists is measurable from objects Mirror receives (both claim
sets, both locator sets, the population), and it is a coverage question rather than a meaning
question, which is what keeps it on this side of § 3.

---

## 3 · WHAT MIRROR MUST NOT JUDGE

> The dispatch asks for the separation. The repository draws it in four places and routes across it
> in two. This section quotes the four, names the one row that sits on the line, and records the
> one object for which the route back has no addressee.

### N-1 · The boundary is already drawn, and already routed — INHERITED

```
C.4                 EVIDENCE → Scientist + Plan/provenance · INFERENCE → peer Scientist ·
                    SYSTEM → Mirror
H.1                 "Epistemic / method review | Mirror"
reading modes §5.4  MODE B's object is "the paper — its evidence and its inferences";
   (main)           Mirror's is "the process — how the laboratory reasoned, reviewed and recorded"
protocol §8.2       MECHANISTIC VALUE: "recorded descriptively — the judgment of value is not made
   (main)           inside the benchmark"; evaluator: "Plan lists; judgment → Annex C review opened
                    by Orchestrator, outside the record"
protocol §5 step 10 "scientific disagreements → Annex C review (R2/R3) if warranted — OUTSIDE the
   (main)           benchmark record"
```

INHERITED and quoted rather than re-derived. The separation the dispatch asks Mirror to enforce is
not a discipline Mirror imposes on itself; it is a **routing rule with two named destinations**, and
both destinations are seats other than Mirror's.

### N-2 · The mechanical test — INHERITED, and it is what makes the boundary checkable

INHERITED (`MIRROR-PROCESS-AUDIT-MODEL-001` § Q-4), the retraction test, restated because § 3 is
where it is applied:

> Write the finding twice — once supposing PMID 42397075 stands, once supposing it is retracted
> tomorrow. **A finding that survives both is a process finding. A finding that changes is a
> science finding**, and C.4 names the seat it belongs to.

Every finding in this record was written against that test. It is cheap, it is mechanical, and it
does not require Mirror to know any biology — which is the property that makes it usable by the seat
that must not know it.

### N-3 · 🆕 One dimension row sits on the line, and it is assigned to Mirror by name

§8.2 (`main`), the `CLAIM PRECISION` row, verbatim:

> per (proposition, snippet, anchor): `SUPPORTED · OVERSHOOT · UNDERSHOOT · NOT_IN_SOURCE ·
> UNVERIFIABLE_SURFACE`; per claim candidate: `Type` claimed vs `Type` the audited evidence bears
> — *route:* blind locator audit; **then adjudication for the `Type` question** — *evaluator:*
> fresh blind agents; **Mirror**

🔴 **Deciding what type a body of evidence bears is one step from deciding what the evidence
shows.** The rule that keeps it on the process side is available and is not a new standard — it is
the retraction test applied to the two available phrasings:

```
PROCESS   "this proposition is typed DATO, and the audited snippet supports at most INFERENZA"
          — survives both suppositions: it is a statement about the relation between a claim and
            its own cited quote, and a retraction changes neither
SCIENCE   "this proposition is false" · "the mechanism is not what the reader says it is"
          — changes under retraction. C.4: INFERENCE → peer Scientist
```

**And Mirror's input to that row is a verdict Mirror did not produce.** Step 7's blind agents emit
the five-value vocabulary; step 8 adjudicates the `Type` question on top of it. So the boundary
holds only while Mirror reasons *from* the audit verdicts rather than *behind* them — re-deriving a
verdict would mean reading the packet, and § N-1's routing plus `EPISTEMIC_REVIEW_MODEL-001` § IND-1
(*"Blindness is the active ingredient, not the ceremony"*) both say why an informed seat cannot
supply a blind one's output.

### N-4 · 🆕 There is no route for Mirror disagreeing with a blind audit verdict, and its author is ephemeral by construction

Suppose the boundary holds and Mirror still finds an audit verdict wrong. C.2's format makes the
next move mandatory: `AUTHOR_RESPONSE (obbligatoria; il silenzio non è accettazione)`.

```
the object      audit/locator_audit-<ACTOR_ID>.md
its author      "fresh blind agents, spawned by Plan per legend-locator-audit" (§5 step 7)
                — the skill's own contract: the auditor "receives only (proposition, quote, anchor)
                  triples plus the source artefact — never the dossier, never the reader's name,
                  never the conclusions"
its importer    Plan
```

🔴 **The author is fresh by design and gone by the time the object is read.** INHERITED
(§ PO-3): the ten-step sequence has no `AUTHOR_RESPONSE` step at all. 🆕 what this adds is that for
*this one object class* the omission is not an oversight that a step could repair — **a blind
ephemeral auditor cannot be given an author's response without ceasing to be either blind or
ephemeral**, and the seat that could answer for the object instead (Plan, who spawned and imported
it) did not write it and is barred by §28 from deciding what it means.

The two available moves both stay inside existing objects and neither is adopted here: record the
disagreement as `DISAGREEMENT_UNRESOLVED con spiegazione`, which C.3 makes a legitimate outcome; or
re-run the audit, which is Plan's step-7 act and Orchestrator's to order. **Naming which is a rule.**

---

## 4 · REQUIRED OUTPUT

> The dispatch asks for a minimal report: `Observation / Finding / Impact / Recovery`. A report
> format is a review-rubric object, so this section maps those four onto the formats that already
> bind and records what does not map. Nothing here is adopted; § BLOCKERS B-5 is why nothing is
> proposed either.

### R-1 · 🔴 🆕 All four names are already occupied, and three of them by the objects being audited

Measured this session, as **field labels**, across the tracked corpus:

| Requested field | Where the label already lives | Whose object | Count |
|---|---|---|---|
| **Observation** | `**Observation:**` — the first of the seven benchmark fields of every claim candidate: *"what was measured, in what system, with what result. **No verb of conclusion.**"* | 🔴 **the reader's** | 2 files at `main`, and both are the reader's specification (`OUTPUT_SCHEMA.md`, `scientist_reading_modes.md`) |
| **Finding** | `**Finding:**` — the first line of every MODE B critical-record entry: *"…(or: "searched; none found — searched: <what>")"* | 🔴 **the reader's** | 1 file at `main` (`OUTPUT_SCHEMA.md` §5) |
| **Impact** | `**Impact on Working Model:**` — a canonical claim field; and `IMPACT`, a field of the Session Learning Record | the claim registry; Annex E.6 | 8 files at `main`; E.6 |
| **Recovery** | `RECOVERY:` — the fourth line of the governance's guarantee block | the governance | 8 occurrences in the normative annexes on `mirror`; 1 more in the benchmark protocol at `main` |

🔴 **A Mirror report written under these four labels reuses the audited object's vocabulary at every
field.** The consequential one is the first: `Observation` is not a loose word in this repository, it
is a field with a **prohibition attached** — no conclusion verbs, because *"the one thing a second
reader must be able to attack is where measurement ends and conclusion begins"*. Two things follow,
and only one of them is a choice:

```
ENTAILED   if Mirror writes a field called `Observation`, the label imports its definition. A Mirror
           `Observation` containing "shows that", "demonstrates" or "suggests" commits, in the
           audit, the defect the audit exists to look for — one level up, exactly as § PO-2 found
           for premature closure
NOT SETTLED whether the collision should be resolved by renaming, by scoping, or by leaving the
           labels to be read in context. That is a rubric decision, and G.2 reserves it
```

### R-2 · 🆕 The four fields are the J.0 quadruple with `DETECTION` removed

The governance's own four-field block, and the dispatch's, side by side:

```
GOVERNANCE (8 instances, measured)      DISPATCH
  GUARANTEE  what the mechanism gives     Observation   what was seen
  FAILURE    what can still go wrong      Finding       what is defective
  DETECTION  by what route it is seen     —             🔴 no field
  RECOVERY   what restores a good state   Impact        what it costs
                                          Recovery      what restores a good state
```

🔴 **`DETECTION` is the field with no home, and it is the field the two axes with unmechanised rules
depend on.** § F-5's `PROCEDURAL` block, § F-6's uncorroborated timestamp, § C-1's *"best effort"*
independence: for every one of them, the only thing that can be written down is *by what route a
violation becomes visible*. A four-field report cannot carry it, and its absence is invisible — a
report simply has no empty box where the route would go.

**Two further absences, INHERITED from § PO-2 and re-derived for a four-field form rather than a
five-question one:** `STEELMAN` — mandatory, *"prima delle obiezioni"* — and
`WHAT_WOULD_CHANGE_MY_MIND` — the declared falsifier, mandatory, and the only instrument this
repository has against premature closure (§ PA-3). Neither maps onto Observation, Finding, Impact or
Recovery. The full mapping, for the record:

| C.2 field | Home in the four | |
|---|---|---|
| `STEELMAN` | — | 🔴 mandatory, and first by rule |
| `EVIDENCE_FOR` / `EVIDENCE_AGAINST` | inside `Observation` | two fields into one |
| `KEY_OBJECTIONS` | `Finding` | |
| `ALTERNATIVES_CONSIDERED` | — | |
| `VERDICT` (`CONFIRMED · WEAKENED · REFINED · REFUTED`) | — | the vocabulary has no field |
| `REVIEWER_CONFIDENCE` · `RESIDUAL_UNCERTAINTY` · `EVIDENCE_NEEDED` | — | and § 2.4 audits exactly this |
| `WHAT_WOULD_CHANGE_MY_MIND` | — | 🔴 mandatory falsifier |
| `AUTHOR_RESPONSE` | — | 🔴 mandatory; § N-4 and § PO-3 |
| `REVIEW_ID · OBJECT · LEVEL · REVIEWER · AUTHOR · ADJUDICATOR` | — | the header, six fields |
| — | `Impact` | 🆕 no C.2 field; nearest is G.2's `EXPECTED_BENEFIT` / `POTENTIAL_HARM` |
| — | `Recovery` | 🆕 no C.2 field; it is the J.0 block's, and § R-4 |

INHERITED measurement (§ PO-2), unchanged: across the 52 files in `reviews/mirror/`, `STEELMAN`
appears 31 times, `WHAT_WOULD_CHANGE_MY_MIND` 31, `AUTHOR_RESPONSE` 30. **The format is in use. It is
not a form nobody fills in.**

### R-3 · The reading this record works under — subtractive, as § PO-2 was

Annex C.2's heading is `Formato unico`, and a fifth format would be a new review standard Mirror may
not adopt. So the four fields are read as **a legible ordering of fields that already exist**, not as
a replacement for them:

```
Observation   the facts, before any claim about them            ← C.2's steelman-first discipline,
                                                                  and the reader's own prohibition
                                                                  on conclusion verbs (§ R-1)
Finding       the defect, stated once                           ← KEY_OBJECTIONS + EVIDENCE_AGAINST
Impact        what it costs, and to which object                ← nearest: G.2's EXPECTED_BENEFIT /
                                                                  POTENTIAL_HARM, which live on a
                                                                  different route
Recovery      what restores a correct state, and WHO acts       ← the J.0 block's fourth line, § R-4
```

with `DETECTION` carried inside `Finding` **explicitly, or not at all** — and § R-2 is why saying so
matters more than where it goes.

### R-4 · 🆕 `RECOVERY` is an act by a named actor in all eight normative instances, and Mirror appears in exactly one — via G.2

Every `RECOVERY:` line in the governance annexes on `mirror`, read this session:

```
A.3   "Orchestrator aggiudica; l'altro attore riceve TASK_CANCEL o nuova generation…"
A.6   "(a) richiesta stato a Orchestrator → conferma o nuovo contratto; (b) Plan ricalibra…"
A.7   "skip + RESUMED_FROM_MILESTONE; Plan/Orchestrator ricalibrano il MILESTONE_PLAN…"
B     "DIAGNOSE (Annex F.4) — mai classificare come rifiuto un guasto di runtime"
E.5   "ricalibrazione budget (Plan) o ricomposizione subset (Mirror, VIA G.2 SE MATERIALE)"
I     "entrambe si fermano (stop condition); l'operatore designa; successione registrata"
I     "retrocessione a UNVERIFIED → nuovo smoke → riabilitazione"
J.1   "Plan ricostruisce dallo stato durevole marcando RECONSTRUCTED…"
and at main, protocol §7:
      "the benchmark is void for the second reader; the outcome says so"
```

🔴 **Six name an actor; two name a procedure; the single one that names Mirror qualifies it with
`via G.2 se materiale`.** And `roles/mirror.md` is categorical: Mirror *"holds **no command** over
any actor"*.

**The operative consequence is exact.** A `Recovery` field written by Mirror is one of two things:

```
LEGITIMATE   a CITATION of a recovery the governance already declares, with its actor named —
             e.g. for a § F-5 violation, protocol §7's own line, verbatim, unaltered
LEGITIMATE   a ROUTING statement: "this is H.1's row X" / "this is a G.2 proposal, which Mirror may
             not route because step 3 has no occupant"
BARRED       an INSTRUCTION to an actor. Mirror holds no command, and inventing a recovery where the
             governance declares none is a rule, which G.2 reserves
```

For the pilot this is not hypothetical: the recovery for the one contamination rule that can be
violated is already written by the protocol, and Mirror writing anything else in that box would be
legislating in a report field.

### R-5 · "Not a score" is already the rule — INHERITED, quoted

```
§8.5 (main)   "No overall score. No weighting. Each dimension its own table, A and B side by side,
               with the route that produced each number… Every count is an enumerated set or
               carries the command that produced it."
§8.5 (main)   agreement is descriptive and "is not a quality measure — two readers agreeing on an
               overshoot is two overshoots"
§8.4 (main)   TIME · TOKEN/CONTEXT · OUTPUT VOLUME: "They are not combined with anything, they do
               not break ties, and a reading is not 'better' for being faster, shorter or cheaper"
```

Nothing needs adding to honour it; the constraint is the protocol's own.

---

## 5 · LEARNING EXTRACTION

### L-1 · The route, the budget and the landing site — INHERITED, re-verified today

INHERITED (EXECUTION-MODEL § LE-1…LE-4), re-measured this session; every number unchanged except one,
and the exception is explained:

```
E.1 states eight learning states           OBSERVED → LOCAL → PROVISIONAL → VALIDATING →
                                           PROMOTED | REJECTED | SUPERSEDED | EXPIRED
                                           🔴 the three terminal branches are what prevent a store
                                              that only grows — § LE-1
P6 budget                                  25 lessons OR 4 000 words [PROVISIONAL]
P6.1 PROV-LESSON-BUDGET-25 expiry           "at the second MIRROR_RETROSPECTIVE"
G.3's cadence N                            UNRESOLVED by explicit operator decision (ESC-3)
E.5's chain, links built                   1 of 5 — RAW archive only
learning/mirror records                    39 (this file is the 40th)
files NAMED as a learning index            0        (mentions ≠ object — § LE-3)
active_lessons/                            0 of 57 refs
MIRROR_UPGRADE_PROPOSAL — token in files   26   ← was 25; the 26th is the record that measured 25
                        — as an object      0
REVIEW_YIELD — files mentioning it          6
             — times computed               0    ← G.3's own ritual detector, never run
ledger/ total files                        16   (1 approval queue · 1 task, owner plan ·
                                                 6 plan + 8 mirror checkpoints)
```

🔴 **The one number that moved, moved because a record was written about it.** That is not a defect;
it is the shape of a RAW-only store, and § LE-3's conclusion stands verbatim: *"An uncontrolled
memory layer is one failure mode of a learning store; an unread one is the other, and it is the one
currently instantiated."*

### L-2 · 🔴 🆕 E.2's confirmation arithmetic assumes independent instances; 18 of the pilot's 20 input paths are the same bytes

Annex E.2, the threshold, verbatim:

> `CONFIRMATION_CLASSES: {actor, session, class}` with class ∈ `ORIGINAL_OBSERVATION | REPLICATION |
> EXPOSURE_AFTER_BROADCAST`. *"Contano pienamente solo ORIGINAL_OBSERVATION e REPLICATION. Soglia
> BEST_PRACTICE_CANDIDATE: **≥2 conferme delle prime due classi**, o 1 + validazione Mirror."*

The class key is `{actor, session, class}`. **The pilot produces two actors and two sessions.** So a
process defect visible in both readings counts, by the key, as two confirmations and crosses the
threshold without Mirror validating anything.

🔴 **But the two arms are not independent for anything rooted in what they share.** § C-2's
measurement is the whole argument:

```
18 of 20 input paths are BYTE-IDENTICAL between the surfaces  (11 common + 7 source)
 2 differ, by design                                          (ASSIGNMENT.md · MODE_DIRECTIVE.md)
```

A defect caused by an ambiguous field in `OUTPUT_SCHEMA.md`, an unanswerable manifest field, a
prohibition with no positive form (§ IR-5) or a validator's behaviour **must** appear in both arms —
not because two readers independently erred, but because one cause was delivered twice. Counting
that as two `ORIGINAL_OBSERVATION`s promotes a single observation to `BEST_PRACTICE_CANDIDATE` on
arithmetic alone.

**The discriminator exists and is mechanical, and it is the manifest's own partition:**

```
the defect's locus ∈ COMMON_FILES ∪ SOURCE_FILES     ONE cause, reported twice
                                                     → one confirmation, whatever the actor count
the defect's locus ∈ PER_ACTOR_FILES,
  or in behaviour under differing directives         two arms are two instances — subject to §0's
                                                     caveat that mode and session variance are not
                                                     separable at n=1
neither, and single-arm                              § FQ-4 — and it is where the answer stops
```

**Recorded, not adopted.** E.2's dedup and conflict rules are Mirror's to apply (*"Conflitti → Mirror
aggiudica"*), but the *methodology* of learning clustering and selection is explicitly among the
things G.2 bars Mirror from changing for itself.

### L-3 · 🆕 The promotion filter already exists, and it is four-way

Body §46, the whole section:

> **Mirror chiede WHY?, non WHO WON?.** `noise vs individual strength vs reusable strategy vs
> systemic weakness` — si distingue, poi si promuove.

🔴 **Four classes, and the ordering is the instruction: distinguish first, promote second.** Applied
to a pilot finding, with the n=1 boundary INHERITED from v2 § L-2 (*one instance licenses an
existence claim and no comparative or frequency claim*):

| §46 class | What it licenses after n=1 | Where it goes |
|---|---|---|
| `noise` | nothing | recorded, not promoted — and § FQ-3 is why this bin is the largest |
| `individual strength` | an existence claim about one reader in one session | recorded; it is not a system property |
| `reusable strategy` | a `LOCAL` at best; `PROVISIONAL` needs E.3's field set — `SUCCESS_CRITERION`, `FAILURE_CRITERION`, `EXPIRY`, `ROLLBACK` | E.1's ladder — and *"Mai provisional per sempre"* |
| `systemic weakness` | the only class that can become a rule change | G.2's `MIRROR_UPGRADE_PROPOSAL` → Plan candidate → independent reviewer → validation; operator if governance |

**And the route's third step has no occupant** (0 ACTIVE leases, derived). So the honest statement of
how a pilot finding becomes a reusable improvement is: *it is classified under §46, it reaches
`OBSERVED` or `LOCAL` in the E.1 ladder by being written down, and everything above that waits on a
seat that is empty.* INHERITED in its parts (§ LE-4, § L-1), stated here because § 5 asked for the
mechanism and this is the mechanism's current state.

---

## FQ · THE FINAL QUESTION

> *"What evidence would convince Mirror that the experiment failed because of LEGEND and not because
> of the Scientist?"*

### FQ-1 · This is a fourth question, and the difference is that it is binary

```
LABORATORY-QUALITY-GATE-MODEL-001   "Scientist | pipeline | laboratory?"      three-way attribution
SCIENTIFIC-PROCESS-AUDIT-v2-001     "science or system?"                      two-way, one bin null
SCIENTIFIC-PROCESS-AUDIT-EXECUTION  "what is knowable from where?"            not an attribution
this dispatch                       "LEGEND, or the Scientist?"               two-way, both bins live
```

Their findings are used below and attributed; none of them answers this. **And the question is a
legitimate one to ask in this laboratory**: F.4 makes DIAGNOSE *mandatory* before any non-compliance
is named, and DIAGNOSE is precisely an attribution. What body §46 constrains is not the asking but
the use — *WHY, not WHO WON* — which is why § L-3's four classes, not this section's two, are what a
finding is promoted under.

### FQ-2 · The first bound: there is no verdict to attribute — INHERITED

INHERITED (v2 § FQ-3): **the benchmark emits no pass/fail.** §8.5: *"No overall score. No weighting."*
§0: *"Its value is the **material** it produces… and the failure modes it surfaces, **not a
number**."* Two of the three `FIRST_PASS_STATE` values — `ABANDONED`, `TIMED_OUT` — are recorded
states, not failures (v2 § P-4).

**So the question is answerable only per finding, never per experiment**, and every clause below is
scoped to one finding at a time.

### FQ-3 · 🔴 🆕 The governance partitions this space four ways, and the binary has no bin for the one that is largest at n=1

Body §46's four classes, set against the dispatch's two:

```
noise                  →  neither LEGEND nor the Scientist
individual strength    →  the Scientist (and the positive form, which a failure question hides)
reusable strategy      →  the Scientist's method, promotable to LEGEND
systemic weakness      →  LEGEND
```

🔴 **`noise` has no bin in a binary, and `noise` is exactly what protocol §0 says cannot be separated
here:** *"With one paper and one session per actor, the benchmark **cannot separate the effect of the
mode from the variance between two sessions**."* A binary attribution forces every observation into
one of two boxes; the design declares that a third box is occupied and that its contents cannot be
told apart from one of the other two.

**That is the structural answer, and it precedes the evidence list:** the question can be answered
positively for LEGEND and can never be answered *by elimination*, because elimination requires the
`noise` bin to be empty and §0 says it is not.

### FQ-4 · The evidence that would land a finding on LEGEND — five classes, each with its state

Each class below is *sufficient on its own* for one finding. Where the evidence does not exist, that
is said rather than assumed.

```
1  THE LOCUS TEST — the strongest, and it exists
   The defect's locus is in COMMON_FILES ∪ SOURCE_FILES (18 of 20 input paths, § C-2), and both
   readings show it. One cause delivered twice. The manifest partitions the surface for other
   reasons and the partition answers this question for free.
   EVIDENCE: benchmark_manifest.json PARITY + COMMON_FILES + PER_ACTOR_FILES; both frozen trees
   STATE: available the moment the two receipts exist

2  THE PRECONDITION TEST — available, and currently failing on its own terms
   §1's P-1…P-7 gate the blind first pass, "satisfied AT THE MOMENT of handover, by the route each
   row names". If a row was unmet and the pass ran, the failure is the laboratory's before it is
   anyone's reading. Measured today: P-2 NOT_REGISTERED, P-3 all capabilities UNVERIFIED with L2
   SUSPENDED, P-4 zero ACTIVE leases, P-6 no Task Contracts, P-7 no surfaces built.
   EVIDENCE: the manifest's HANDOVER block; the `verify` run; the registry; the lease derivation
   STATE: available, and §9's own determination is "BLIND FIRST PASS — BLOCKED BY CANONICALIZATION"

3  THE UNSATISFIABLE-INSTRUCTION TEST — available, and the schema anticipates it
   A field the surface makes unanswerable, penalised as if it were answerable. OUTPUT_SCHEMA §1
   already names the case: several manifest fields "ask about the corpus, which this surface does
   not contain: waive them, and say THAT is why." A finding that scores such a waiver as a defect
   is a finding about LEGEND's instructions.
   EVIDENCE: the instruction's own text, byte-identical in both surfaces
   STATE: available

4  THE UNANSWERED-BLOCKER TEST — 🆕 available, and it is the cleanest of the five
   INTERACTION_MODE is AUTONOMOUS_COMPLETE: "do not ask questions to proceed… record it as a
   BLOCKER in output/receipt.json and continue with everything that is not blocked." A declared
   BLOCKER is therefore the reader's ONLY channel, it is addressed to a laboratory that must answer
   it, and the answering seat is Orchestrator — derived ACTIVE: 0.
   EVIDENCE: output/receipt.json blockers[]; the absence of any answering artifact
   STATE: available — and § IR-5's caveat applies to the empty case, not to a populated one

5  THE UNVERIFIED-CAPABILITY TEST — available, and it is the laboratory's own assignment rule
   Body §38: CONFIGURED != PROVEN, applied to capabilities; I.4 and body §8: "Orchestrator assegna
   sulle capabilities VERIFICATE, non sul ruolo presunto." Every declared Scientist capability
   reads UNVERIFIED. A failure of a capability that was assigned without verification is a failure
   of the assignment rule, which is LEGEND's.
   EVIDENCE: runtime/agent_card_registry.md; roles/scientist.md's capability table
   STATE: available today, and reads UNVERIFIED today
```

**And the class that would be decisive and does not exist**, INHERITED (§ FT-3, LAB-QUALITY § AQ-4):
F.4's ordered DIAGNOSE asks first about *delivery/runtime failure* and second about *context failure*
— truncated turns, permission prompts, crashes, stale generations, incompatible checkpoints — and the
observable for both is the event ledger. **0 of 57 refs.** *"The only layer that can be examined is
the only layer that gets blamed."*

### FQ-5 · 🆕 F.4's only actor-terminating branch is unreachable inside one generation of this task

F.4's elimination, verbatim, with its own closing capitals:

```
1. delivery/runtime failure?   2. context failure?   3. task contract ambiguity?   4. actual refusal?
        ↓
solo (4), RIPETUTO DOPO CHIARIMENTO → NON_COMPLIANT → HUMAN_REQUIRED
(1)-(3) → recovery tecnico / chiarimento contratto, MAI insubordinazione
```

🔴 **The terminal branch requires a clarification round, and the pilot's interaction mode removes
it.** `AUTONOMOUS_COMPLETE` is set by §5 step 2 for both contracts and restated in both mode
directives: *do not ask questions to proceed*. There is no channel during the pass on which a
clarification could be issued or answered; the substitute is a `BLOCKER` recorded and carried
forward, which is class 4 of § FQ-4 and points the other way.

**So within a single generation, F.4 cannot reach "the Scientist".** The earliest a reader-attributed
non-compliance could be established is a second generation issued after a clarification — an act
that requires an Orchestrator (`GENERATION` is H.1's row) and a lease that does not exist.

### FQ-6 · The answer, and its exact converse

**What would convince Mirror the failure was LEGEND's — one of five, each sufficient alone:**

```
1  the defect's locus is a byte both readers received, and both readings show it        § FQ-4·1
2  a §1 precondition was unmet at handover and the pass ran anyway                      § FQ-4·2
3  the instruction demanded what the surface made unanswerable                          § FQ-4·3
4  a declared BLOCKER had no addressee, under a mode that forbids asking                § FQ-4·4
5  the capability was assigned UNVERIFIED, against the laboratory's own assignment rule  § FQ-4·5
```

**What would convince Mirror the failure was the Scientist's — and this is where the answer stops.**
A finding must be single-arm *and* not rooted in either differing file, and then §0's first caveat
applies with full force: at one paper and one session per actor the residue is mode, session variance
and reader, unseparated. Add § FQ-5: the governance's own elimination cannot terminate at the actor
inside one generation. **At n = 1 this experiment can attribute a failure to LEGEND and cannot
attribute one to the Scientist.**

🔴 **And the record pushes the opposite way, which is the thing to guard against.** INHERITED,
`LABORATORY-QUALITY-GATE-MODEL-001` § AQ-4: with no event ledger and no join key, *"elimination lands
on the Scientist by default, and that is an artefact of the record."* Two forces, opposed: the
**evidence** structure can only prove LEGEND; the **record** structure silently blames the reader.
An audit that does not state which of the two it is standing on will produce the second while
believing it produced the first.

**The asymmetry is not a flaw in the design; it is the design.** F.4 orders the actor last, in
capitals of its own; body §41 puts ten laboratory mechanisms — *"claim, messaging, challenge, peer
review, work commit, learning, integrazione, sampling Mirror, canonical batch, recovery"* — under
test in the same first cycle as the science. **A failure in any of those ten is the pilot's product,
not its defect**, and none of the ten is a reader's reasoning.

### FQ-7 · What would change this answer — the declared falsifier

Because § R-2 measured that a four-field report has no box for one, this section carries its own:

```
a second arm-independent instance      two findings whose locus is in PER_ACTOR_FILES, or one
                                       replication in a later batch, moves E.2's arithmetic off
                                       the 18:2 objection (§ L-2) and makes "the Scientist" reachable
an event ledger with a writer          J.1 as designed in P7 would supply the observable F.4's
                                       first two questions require, and elimination would stop
                                       landing on the reader by default
a join key between product and process INHERITED · LAB-QUALITY § AQ-2. v2 § P-3 already found that
                                       INSIDE the benchmark the key exists — task, actor, mode,
                                       instruction version, commit — which is why this pilot can
                                       answer the question at all, and why the answer does not
                                       generalise past it
```

If none of the three arrives, this section's answer stays true and stays narrow, which is the correct
outcome for an n=1 design that says so about itself.

---

## BLOCKERS

> Blockers to the framework's **application**. Nothing below is assigned; Mirror holds no command.

```
B-1  THE EXPERIMENT HAS NOT RUN. 0 output paths across 6 output seats, 57 refs; 0 task contracts for
     either scientist; 0 freeze receipts; 0 audits. Positive controls: instructions 19, population
     19. Everything above is ex ante

B-2  THE PROTOCOL AND ITS TOOLING ARE NOT ON THIS REF — re-verified. Positive control:
     failure_taxonomy.md and learned_gates_registry.md ARE here, and § F-2 needed the second
     (INHERITED · v2 F-0, EXECUTION-MODEL B-2)

B-3  🔴 THE IMPORT HAS NO DEFINED SCOPE AND NO COMMAND (§ IR-4, § F-4). 7 of the frozen tree's files
     are refused by .gitignore:7 at the import path, measured with git check-ignore; 0 of the tool's
     7 subcommands take first_pass/ as an object; the release gate carries no rule that would catch
     a forced import. This blocks the first check Mirror would run on its largest input

B-4  THE DETECTION ROUTE FOR THE ONE PROCEDURAL FREEZE RULE HAS NO REACHABLE OBJECT (§ F-5).
     SURFACE_ABSOLUTE_PATH deliberately not recorded; deployment/local_instance.md 0 of 57 refs;
     retention bounded by "until the outcome is canonical", which is downstream of the step that
     would ask. INHERITED in its first half · v2 C-4, EXECUTION-MODEL IB-6

B-5  NO ORCHESTRATOR. ACTIVE by derivation: 0; lease #3 EXPIRED_WITHOUT_RENEWAL with stored ≠
     derived. C.3 bars opening a review; §5 step 2 bars issuing the contracts; G.2 step 3 bars
     routing any proposal — which is why § 4 proposes nothing

B-6  NO EVENT LEDGER, ON ANY REF — designed in P7, not built. It is the observable F.4's first two
     diagnostic questions need (§ FQ-4) and the only possible corroboration of a freeze timestamp
     (§ F-6). INHERITED · EXECUTION-MODEL B-6

B-7  THE BENCHMARK IS BLOCKED. Protocol §9: "BLIND FIRST PASS — BLOCKED BY CANONICALIZATION", and
     independently by P-2…P-4. Every declared capability of both roles UNVERIFIED; L2 SUSPENDED by
     the C-9 hold

B-8  THE PUBLICATION GATE BLOCKS IN MIRROR'S OWN OUTPUT DIRECTORY (§ PRECONDITIONS). One [BLOCK],
     EMAIL_ADDRESS, on the repository's own noreply committer identity inside a verbatim commit
     transcription. Not this dispatch's object and not fixed here; recorded because the adjudication
     of step 8 is a public-edition artifact subject to the same gate
```

---

## OPEN_QUESTIONS

```
Q-1  What is the import's scope — the whole frozen tree, or FILES[] filtered by role (§ IR-4)? The
     receipt already partitions input / output / unexpected, so the question is answerable with
     existing objects; nothing states which answer is the protocol's, and .gitignore:7 refuses the
     literal reading of the clause as written

Q-2  Does verify-freeze, run against an import, require the import to preserve the surface's
     relative paths (§ F-4)? The tree digest is a function of paths and no clause fixes the
     convention

Q-3  Is an empty `contamination_declared: []` an assertion or a default (§ IR-5)? The schema's own
     standard is "a fact you checked, not an intention", and the pattern that would make it one is
     applied to MODE B's axes one file away

Q-4  Does E.2's `{actor, session, class}` key count two arms of a byte-identical surface as two
     confirmations (§ L-2)? The manifest's 18:2 partition supplies a discriminator; adopting it is
     a clustering-methodology change, which G.2 reserves

Q-5  Which of the four §46 classes does a pilot finding enter, and who classifies it (§ L-3)? The
     ordering "si distingue, poi si promuove" makes classification prior to promotion, and the
     promotion route's third step has no occupant

Q-6  Should Mirror's report reuse the labels `Observation` and `Finding`, which the audited objects
     own (§ R-1)? If yes, the definitions travel with them — including the prohibition on conclusion
     verbs. That is a rubric decision and it is not Mirror's alone

Q-7  Where does DETECTION go in a four-field report (§ R-2)? Its absence is the one that cannot be
     seen, because the format has no empty box for it

Q-8  Who reconciles the 21-versus-20 count (§ C-4)? The list built from it is internally consistent
     at 20 + 3 = 23; two prose statements say 21
```

---

## WHAT THIS RECORD DOES NOT DO

It does not conduct an audit, adopt a framework, propose a rule, define a report template, or create
a validator. It does not start, authorize, unblock or schedule BENCH-AB-001; it does not lift the C-9
hold, verify a capability, register an actor, take a lease, or issue a task. It does not evaluate
PMID 42397075 — the paper was never opened in this session, and its packet is git-ignored in this
repository — and it reaches no conclusion about WWOX biology. It does not set `N` for
`MIRROR_RETROSPECTIVE`, resolve ESC-3, promote or extend `PROV-LESSON-BUDGET-25`, decide the import's
scope, name the C-4 inspection's owner, declare an admissibility rule for Mirror's inputs, rename any
report field, adopt the 18:2 independence discriminator, fix the publication gate's BLOCK, or decide
anything G.2 reserves. It **corrects one sentence** of `SCIENTIFIC-PROCESS-AUDIT-v2-001` § C-5,
declared in the front matter and sectioned at § C-3, and supersedes nothing. It writes one file, under
`learning/mirror/`, on branch `mirror`.

---

## EVIDENCE

```
RUN THIS SESSION, 2026-08-22T20:08Z–20:41Z · mirror@da52ee5 · main@788c357
REF NET: 57 total (43 refs/heads · 4 snapshot tags · 1 handoff tag · 4 remotes · 5 codex checkpoints)

  framework/scripts/legend_lint.py .                   VERDICT: PASS (1 INFO)
  framework/state/state_manifest_current.md:141        current_state: READY
  scripts/public_release_gate.py                       1 [BLOCK] · 4 [REVIEW]
                                                       BLOCK: EMAIL_ADDRESS
                                                       reviews/mirror/REV-ORCHSURF-R4-POST-
                                                       TRANSCRIPTION-FIDELITY.md:73 —
                                                       legend-project@users.noreply.github.com
  lease_state.py --check (script + record from main,   ACTIVE by derivation: 0
    extracted to a scratch tree — both absent here)     #3 EXPIRED_WITHOUT_RENEWAL; stored ≠ derived

  ref sweep, BENCH-AB-001/{first_pass,frozen,          0 · 0 · 0 · 0 · 0 · 0   of 57
    comparison,audit,adjudication,outcome}
  ref sweep, BENCH-AB-001/instructions                 19 of 57   ← POSITIVE CONTROL
  ref sweep, BENCH-AB-001/population                   19 of 57   ← POSITIVE CONTROL
  ref sweep, reviews/mirror/BENCH-AB-001-ADJUDICATION  0 of 57
  ref sweep, deployment/local_instance.md              0 of 57
  ref sweep, ledger/events · ledger/consolidated       0 · 0     of 57
  ref sweep, active_lessons/                           0 of 57

  presence, this ref   controlled_benchmark_ab.md · scientist_reading_modes.md ·
                       benchmark_input_surface.py · BENCH-AB-001/       ALL ABSENT on `mirror`
                       failure_taxonomy.md · learned_gates_registry.md  PRESENT — both read here

  IMPORT / IGNORE (§ IR-4)
    git check-ignore -v  …/first_pass/scientist-a/files/fulltext/PMID42397075_Aqeilan2026.pdf
                       → .gitignore:7:files/            IGNORED
    git check-ignore -v  …/first_pass/scientist-a/output/receipt.json      → NOT IGNORED
    git check-ignore -v  …/first_pass/scientist-a/roles/scientist.md       → NOT IGNORED
    git ls-tree -r --name-only main -- files/fulltext                      → 0 tracked
    surface_spec.json source_files                                         → 7, all under files/
    public_release_gate.py, rules naming files/ | pdf | binary | copyright → 0

  SURFACE PARTITION (§ C-2)
    common_files 11 · source_files 7 · per_actor_files 2 · empty_dirs 4
    expected_output_paths 5 · expected_output_prefixes 1 · forbidden_prior_output_paths 23
    common_files enumerated: CLAUDE.md · BENCHMARK_INSTRUCTIONS.md · OUTPUT_SCHEMA.md ·
      roles/scientist.md · epistemic_discipline.md · gold_is_in_the_details.md ·
      fulltext_read_receipt.md · scientist_reading_modes.md · failure_taxonomy.md ·
      deepdive_manifest.py · corpus_firewall.py

  FORBIDDEN LIST (§ C-3 CORRECTION, § C-4)
    spec key `forbidden_prior_output_paths`             a static array, 23 entries
    benchmark_input_surface.py uses of it               lines 230, 531, 1379 — all spec[...]
    git invocations in that tool                        rev-parse / status, inside `freeze` only;
                                                        no git grep, no tree enumeration
    the recorded derivation, run verbatim at cbce3016   20 paths (0 under governance/candidates)
    the same command at main                            32 paths
    reconciliation                                      20 + 3 named additions = 23 ✔
    the prose figure, in two places                     "twenty-one" (§2.1) · "21" (manifest)

  MANIFEST STATE (§ IR-2)
    _state "PREPARED — NOT FROZEN" · FROZEN_SHA256 null · HANDOVER all null ·
    EVALUATION_POPULATION.sha256 "DERIVED_AT_BUILD"

  TOOL SURFACE (§ F-4)
    subcommands   build · verify · freeze · verify-freeze · population · locators · tree-digest = 7
    subcommands taking first_pass/ or named import                                              = 0
    verify-freeze  set-wise ADDED/REMOVED/MODIFIED + identity read from the tree's ASSIGNMENT.md
                   + a refusal when files match and the tree digest does not

  FIELD-NAME OCCUPANCY (§ R-1, § R-4), tracked corpus
    '**Observation:**'            2 files at main — OUTPUT_SCHEMA.md · scientist_reading_modes.md
    '**Finding:**'                1 file  at main — OUTPUT_SCHEMA.md §5 (MODE B critical record)
    'Impact on Working Model'     8 files at main; plus IMPACT in Annex E.6
    quadruple census on `mirror`  GUARANTEE 8 · FAILURE 11 · DETECTION 8 · RECOVERY 8
    RECOVERY lines, verbatim      A.3 · A.6 · A.7 · B · E.5 · I ×2 · J.1 ; +1 at main (protocol §7)
                                  6 name an actor · 2 name a procedure · 1 names Mirror, "via G.2"

  LEARNED GATES (§ F-2)          learned_gates_registry.md — 79 rows, 21 ACTIVE_EXECUTABLE,
                                 57 ACTIVE_METHOD; FREEZE_SCOPE_GATE ACTIVE_EXECUTABLE;
                                 companion checker scripts/test_freeze_scope.py PRESENT here

  CORPUS COUNTS
    tracked paths naming the paper (42397075|awag239)   main 32 · mirror 24   (INHERITED, unchanged)
    learning/mirror records                             39 (this file is the 40th); 29 match
                                                        SLR-mirror-NNNN
    reviews/mirror files                                52; REV-SCIAB-MIRROR-001…006 = 6
    ledger/ files                                       16
    MIRROR_UPGRADE_PROPOSAL — token in files            26 (was 25; the 26th measured the 25)
                            — as an object               0
    REVIEW_YIELD — files mentioning                      6 ·  times computed  0
    files NAMED as a learning index                      0 · active_lessons/  absent

  ⚠️  Two instrument notes, both of which would have changed a number:
      (1) A per-ref sweep in zsh must brace the variable — "${r}" — and every sweep above carried a
          positive control that fired. INHERITED as a discipline · EXECUTION-MODEL EVIDENCE (1)
      (2) `grep --include=*.md` unquoted is glob-expanded by zsh and returns "no matches found"
          rather than an error a reader would notice. Two counts read 0 on the first pass and were
          re-run quoted; both are reported above from the quoted run

READ AT `mirror`   GOVERNANCE_v3.1.1.md (§§26, 27, 28, 38, 41, 46) · annexes A, C, E, F, G, H, J ·
                   plan_defined_parameters.md · roles/mirror.md · roles/scientist.md ·
                   epistemic_discipline.md · failure_taxonomy.md · learned_gates_registry.md ·
                   .claude/skills/legend-locator-audit/SKILL.md · the five prior learning/mirror
                   records on this ground
READ AT `main`     controlled_benchmark_ab.md (§§0–10) · scientist_reading_modes.md (§§3–5) ·
                   BENCHMARK_INSTRUCTIONS.md · OUTPUT_SCHEMA.md · MODE_A.md · MODE_B.md ·
                   ASSIGNMENT.scientist-a.md · benchmark_manifest.json · surface_spec.json ·
                   benchmark_input_surface.py (CLI surface + cmd_verify_freeze)
NOT READ           PMID 42397075, in any surface, in any form. The packet is git-ignored
                   (`.gitignore:7`) and was never opened. 0 scientific claims assessed
```
