---
artifact: MIRROR hostile review record (Annex C.2)
review_id: REV-GOV311-MIRROR-002
task_id: GOV311-MIRROR-REVIEW-002
directive_version: 1
generation: 2
reviewer: mirror
author: plan
adjudicator: operator
level: R4 — METHOD / MIRROR_REQUIRED (Annex G.1); MAJOR governance review
review_date: 2026-08-16
review_date_precision: date only — the runtime exposed no wall-clock time
disposition: REVISION_REQUESTED
supersedes_scope_of: REV-GOV311-MIRROR-001 (revision 4; no verdict transferred)
---

# MIRROR HOSTILE REVIEW — CAND-20260816-GOV311 revision 5

## 0 · Binding

```
CANDIDATE_ID:            CAND-20260816-GOV311 — revisione 5
CANDIDATE_CONTENT_HASH:  c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239   VERIFIED
BASE_HEAD:               749a9a9b8f29c855f803a43b979c591532557561                            VERIFIED
BRANCH_TIP:              9720a0cd1dddfe457f8e4eec1ebe47bd627512cc
BRANCH HEAD AT REVIEW:   evidence-index @ 6b3c038de49740894480297cd1ce5cd7b0ffc4ee
REVIEW_DATE:             2026-08-16
REVIEWER:                mirror
DISPOSITION:             REVISION_REQUESTED
```

This is a **new review from R-1**. Nothing from `REV-GOV311-MIRROR-001` was carried forward: the
prior review reached only R-1 and was bound to a superseded hash.

> **Scope note that changes the cost of the repair.** Every required change below lies in the
> **manifest**, which PID-19 places in the control plane, outside the content domain. I verified
> mechanically that manifest commits do not move the hash. Therefore: correcting them leaves
> `c39ecae8…` **unchanged**, this review's content verdicts stay bound to the same object, and a
> third full review is **not** required — only re-verification of the corrected fields.

---

## 1 · R-1 · CANDIDATE IDENTITY AND BINDING — Annex C.2

```
REVIEW_ID:   REV-GOV311-MIRROR-002 / R-1
OBJECT:      CANDIDATE_CONTENT_HASH c39ecae8…30c239 + BASE_HEAD 749a9a9b…557561
LEVEL:       R4 — MIRROR_REQUIRED, MAJOR      REVIEWER: mirror   AUTHOR: plan   ADJUDICATOR: operator
```

### The ten assigned checks

| # | Check | Result |
|---|---|---|
| 1 | The published command produces the declared hash | ✅ `c39ecae8…30c239`, exact |
| 2 | Two independent executions agree | ✅ three runs, identical |
| 3 | P5 and the script are semantically identical | ✅ the script *parses* P5 (`CANDIDATE_HASH_VERSION`, `CONTROL_PLANE_ROOTS`); serialization matches P5.2 line for line |
| 4 | No second competing recipe in the manifest | ✅ the manifest references P5 and states no formula; `legend-candidate-v3` is declared only in P5 |
| 5 | The domain includes/excludes exactly what is declared | ✅ 504 included, 8 excluded — all 8 under the two declared roots (1 manifest, 6 checkpoints, 1 task claim) |
| 6 | The excluded roots are genuinely control plane | ⚠️ true today; the prefix rule is unbounded — see NBN-3 |
| 7 | A change to an included file changes the hash | ✅ mutation test: one byte into the governance body → `d960c93f…`, different |
| 8 | A manifest/checkpoint change does not | ✅ mutation test on `CHK-plan-0006` → unchanged; and the hash is identical at `9720a0cd`, `fb67792` and `6b3c038` |
| 9 | The count is derived, not hand-maintained | ✅ `--show-domain` derives it in the same pass; no count in prose |
| 10 | `BRANCH_TIP` / `MANIFEST_COMMIT` / `SOURCE_COMMITS` no longer conflated | ⚠️ the three concepts are now cleanly distinct — but 3 of the 14 `SOURCE_COMMITS` oids do not resolve (RC-6) |

### The author's account of the revision-4 defect, independently tested

P5.2 states the cause: the recorded value was computed through `$(…)`, which strips the trailing
newline, while the published command used a pipe, which keeps it. **I tested the claim rather
than accepting it.** At `3c6c6e15`, with the revision-4 filter:

```
without trailing newline  →  2e7da13ff3bfff4554a28300d01b6e23b62ead3b787c3de78f92a2cd5b9256d7   ← the recorded rev-4 value
with trailing newline     →  e3ca1983f6f09bc613fa1b108efc805f28c0a43782978eba2586cc1e04e79e76   ← what I computed in review 001
printf '%s' "$LIST" | wc -l  →  507   ← exactly the count the rev-4 manifest recorded (true: 508)
```

Both symptoms — the hash and the off-by-one count — fall out of one missing byte. The account is
**verified, not merely plausible**, and my own review-001 `RESIDUAL_UNCERTAINTY` ("the mechanism
is UNKNOWN") is now closed. It also shows my 144-combination sweep was **not exhaustive**: it
never tried a listing without a terminating newline. Declaring the mechanism UNKNOWN rather than
inferring one was therefore the load-bearing decision, not the sweep.

### STEELMAN

The remediation is what a governed correction should look like. It did not patch a number: it
removed the *class* of defect. The definition now exists in exactly one place, is executed by
exactly one script that parses that place rather than copying it, and passes nothing through a
shell — the specific mechanism that caused the failure is structurally unavailable. The fix to
RC-5 is a **classification** (content vs control plane) rather than an exception for the one file
that bit, which means checkpoints, task claims and the future event ledger are all covered by a
rule instead of a patch. The cascade of RC-2 was declared before it was noticed, with the
invalidated checkpoints listed and generation 2 opened rather than the old ones quietly reused.
And Plan adopted the positive-control discipline from review 001 into its own verification record
before relying on a negative — an author absorbing a reviewer's method is the behaviour the
learning pipeline exists to produce.

### EVIDENCE_FOR

Every mechanical claim in the manifest's §6 that I re-ran reproduced: the hash (3×), the four
fingerprints, `LINT PASS` with exactly one INFO, `publication gate PASS / BLOCKS: 0` with exactly
four `[REVIEW]` items, `BYTE_IDENTITY` of the design record, base condition `0 behind`.

### EVIDENCE_AGAINST

1. Three of fourteen `SOURCE_COMMITS` oids are unresolvable — `891fba91`, `7f7c0cb0`, `d371eed4`
   against the real `891fba92`, `7f7c0cb7`, `d371eed7` (RC-6).
2. Two artifacts the frozen text requires are neither built, nor in `PENDING_IMPLEMENTATION`, nor
   handled by `BOOTSTRAP.md`: `HUMAN_APPROVAL_QUEUE` and `OPERATOR_DAILY_BRIEF` (RC-7).
3. Manifest structure is malformed: `## 6` appears twice (L228, L265) with `## 5b` between them,
   and the first `## 6` contains an orphan empty table header (RC-8).
4. §3's migration-map counts do not reconcile with the map (RC-9); §1's "0 behind, 12 ahead" is
   stale (RC-10).

### ALTERNATIVES_CONSIDERED

*Treat every finding as non-blocking and pass with notes.* Rejected: the instruction forbids using
`PASS_WITH_NOTES` to carry a required change, and an approver is entitled to a provenance table
that resolves. *Fail.* Rejected as disproportionate — no finding touches the content, and the
content-hash machinery is now demonstrably sound.

### VERDICT: **REFINED**

The binding itself is **CONFIRMED** — reproducible, deterministic, correctly sensitive and
correctly insensitive. The manifest *around* it carries four defects, none of which touches the
hashed content.

```
REFINED_FORMULATION: The candidate's identity is established and verifiable. Its manifest is not
                     yet a correct description of it.
REVIEWER_CONFIDENCE: HIGH on the binding (mutation-tested in both directions, three tips, three runs).
                     HIGH on RC-6/RC-7 (mechanical). MEDIUM on RC-9 (a counting convention is
                     plausible for group D; group E reconciles under none I could find).
RESIDUAL_UNCERTAINTY: Whether "verbatim materialization" of the frozen text is faithful cannot be
                     verified by me at all — I have no copy of the operator's transmission. See R-2.
EVIDENCE_NEEDED:     The operator's original v3.1.1 transmission, to close R-2 by comparison.
WHAT_WOULD_CHANGE_MY_MIND:
                     For RC-6: the three oids resolving in any clone of this repository.
                     For RC-7: a clause showing the queue and brief are covered somewhere I did not look.
AUTHOR_RESPONSE:     PENDING_OPERATOR_ROUTING
```

---

## 2 · R-2 · FIDELITY OF THE FROZEN MATERIALIZATION

**STEELMAN.** The separation is disciplined: every frozen artifact declares `status: FROZEN /
normative: yes`, every Plan artifact declares `PROPOSED — binding once Mirror hostile review
passes and the operator approves`, and the register declares itself non-normative. Plan's
commentary is kept *outside* the hashed frozen files precisely so they remain faithful carriers.

**Audited mechanically — no contamination found:**

| Class | Artifacts | Declared status |
|---|---|---|
| FROZEN, normative | body + annexes A–J (11 files) | `FROZEN` / `normative: yes` — uniform |
| PROPOSED | `plan_defined_parameters.md`, 4 role contracts, `BOOTSTRAP.md`, `deployment_profile.md` | `PROPOSED`, normative *on approval* |
| Non-normative | `ANNEX_INDEX.md`, `design_records/` | declared `normative: no` / provenance |

No element that is PROPOSED is presented as FROZEN; no authority is relocated; the annex hash
table declares itself a MAT-002 snapshot and defers to computation at use time.

🔴 **Declared limit.** *Verbatim* fidelity to the operator's transmitted text is **NOT VERIFIABLE
BY MIRROR**: the source of truth for the comparison is the operator's own transmission, which is
not in the repository. I can verify internal consistency, status hygiene and structure — not that
nothing was silently reworded. Stated as `UNRESOLVED`, not silently passed.

```
VERDICT: CONFIRMED, bounded — no defect found within what is verifiable from the durable state.
         Fidelity to the transmitted source is UNRESOLVED and only the operator can close it.
REVIEWER_CONFIDENCE: HIGH on status hygiene; NONE on verbatim fidelity (no access to the source).
WHAT_WOULD_CHANGE_MY_MIND: a diff between the transmitted text and the materialized files.
AUTHOR_RESPONSE: PENDING_OPERATOR_ROUTING
```

---

## 3 · R-3 · PLAN IMPLEMENTATION DECISIONS

**Census, not assumption:** the manifest carries **19** PIDs. Numbering `01–19` is complete with
**no gaps**, and no implementation decision was found outside the section.

Specific verifications the assignment named:

- **Fingerprint (PID-02).** Per-role Annex J granularity is exactly as declared:
  `scientist → J.0 J.2 J.3` · `plan → J.0 J.1 J.2 J.3` · `mirror → J.0 J.1 J.2 J.3` ·
  `orchestrator → J.0 J.1 J.2 J.3 J.4`. A COST_POLICY (J.4) change therefore cannot invalidate a
  scientist mid-reading — A.6's own worked example, satisfied. Too-broad / too-narrow: the body
  sits whole in CORE, which is broad by choice and correct while the body is frozen; P2.3 names
  the signal to watch and assigns it to me.
- **Fail-loud (PID-03, PID-06).** Tested by breaking the parsed prose four ways: heading renamed →
  `COMPOSITION FAILED: § P2.2 not found`, exit 2. Role-contract placeholder removed → `CORE must
  include the actor's own role contract`, exit 2. Role rows destroyed → `no per-role rows parsed`,
  exit 2. `CONTROL_PLANE_ROOTS` renamed → `DOMAIN FAILED`, exit 2; emptied → `an empty exclusion
  must be explicit`, exit 2. **No silent fallback in any case.**
- **Scientist contract (PID-09).** Parity holds: ACTOR_IDs distinct in frontmatter
  (`scientist-a/b/c`), worktrees distinct (`lettore`, `lettore-b`, `lettore-c`), SESSION_REF is
  per-actor by construction, capabilities are verified per actor at L2 in the Agent Card, and
  WORK_COMMITs are per-branch — no provenance fusion. One `ROLE_CONTRACT_HASH` for three
  equivalent actors is *correct*, not a compromise: §32 forbids static specialization, so
  divergent contracts would themselves be the defect.
- **Event ledger (PID-08/PID-19).** Design (a) satisfies one-writer by construction; source events
  immutable; `CLOSES_EVENT_ID` on closure only; `closed_by` confined to the derived view; repo
  sovereign; `RECONSTRUCTED` marking preserved. Design only — no writer exists.

| PID | Decision | Verdict | Rationale / risk | Falsifier / expiry | Required change |
|---|---|---|---|---|---|
| 01 | `on_exhaust = PARK` | CONFIRMED | A.1 delegates it; PARK is the only option that spends nothing and loses nothing. Risk: parked tasks accumulate unseen — detectable in the autonomy ledger | — | — |
| 02 | Fingerprint composition v1 | CONFIRMED | Verified per role incl. J-splitting; authority A.6/H.1 is Plan's | invalidation-rate monitoring (mine, P2.3) | — |
| 03 | Script parses P2.2 | CONFIRMED | Anti-drift; fail-loud verified 3 ways | — | — |
| 04 | ACK timeout 30 min | CONFIRMED | PROVISIONAL with all six E.3 fields | expiry: 3rd scientific batch | — |
| 05 | Heartbeat 30/90 min | CONFIRMED | idem; DOWN is recoverable | expiry: 3rd scientific batch | — |
| 06 | Hash defined once in P5, one script | CONFIRMED | Reproduced, deterministic, mutation-tested both directions | — | — |
| 07 | Lessons budget 25 / 4 000 words | CONFIRMED | Fixed cap correct *because* E.5 defines overflow | expiry: 2nd MIRROR_RETROSPECTIVE | — |
| 08 | Event ledger design (a) | CONFIRMED | (b) structurally cannot record recovery events | — | writer still PENDING |
| 09 | One `roles/scientist.md` | CONFIRMED (declared deviation) | Preserves §32 parity; identity stays distinct | — | operator ratification — ESC-2 |
| 10 | §35.2 as pointer table | REFINED (declared deviation) | Purpose met, drift avoided; but §7/Annex H say *replicata nei CLAUDE.md*, and a pointer is not a replica | — | operator ratification — ESC-2 |
| 11 | `local_instance.md` untracked | CONFIRMED | Verified: gitignored, 0 tracked; protects I.5 clone-and-run | — | — |
| 12 | ACTOR_IDs `scientist-a/b/c` | UNRESOLVED (correctly) | Permanent once set; confirmed at registration, not by materialization | — | — |
| 13 | `ledger/` paths | CONFIRMED | Coherent with PID-08; interacts with PID-19 — see NBN-3 | — | — |
| 14 | Growth principle → new master file | CONFIRMED | Existing layer, new file; three inventories found no prior home | — | — |
| 15 | Steps 2 and 4 reversed | CONFIRMED | Non-loss outranks instruction ordering; declared in MAT-006 | — | — |
| 16 | `MIRROR_RETROSPECTIVE` N | UNRESOLVED (correctly) | Plan rightly refused: G.2 places it inside Mirror's method | — | route via ESC-3 |
| 17 | Withdrawal of the smuggled rule | CONFIRMED | Verified: rule 4 restored, and the added sentences appear nowhere in `framework/protocols/` | expiry: my first coordination review | — |
| 18 | Design-record path, no inner header | CONFIRMED | Byte identity PASS; first line is the document's own title | — | — |
| 19 | Content vs control plane | REFINED | Resolves RC-5 by rule rather than exception — the right shape. But the prefix is unbounded: anything later placed under `ledger/` leaves the binding silently | — | none here — see NBN-3 |

---

## 4 · R-4 · CLAUDE.md MIGRATION AND ROUTER

**The frozen requirement, cited rather than assumed:** body **§0.3** — *"Il CLAUDE.md di root è un
router MINIMO"* — with the literal `IF no valid runtime inventory / no ACTIVE ORCHESTRATOR_LEASE`
block, reinforced by §35 (`CLAUDE.md = router MINIMO`).

**Verified:**

- The router is **107 lines**, opens with the §0.3 block **verbatim**, and states its own
  precedence rule: *"if this file and a normative file ever disagree, the normative file wins."*
- **All 27 artifacts referenced by the migration map resolve** in the tree — zero dangling
  destinations.
- **Literal preservation, tested against the source at `749a9a9b`:** 19 load-bearing literals
  (`FULL STATE NOT AVAILABLE — COMMIT BLOCKED`, `PARTIAL FILE — NOT SAFE FOR REPLACEMENT`,
  `PREMISE: DEFAULT_FROM_TEXTBOOK`, `REVIVAL_TRIGGER`, `Un abstract non è una lettura`,
  `crop_contains_span`, `PATTERN_ALREADY_SOLVED_GATE`, `FREEZE_SCOPE_GATE`, `MODE: Q&A`,
  `publish the derivation, not the derived`, the thousandth-batch question …) — **all survive
  outside the router**.
- The single literal that does not survive verbatim — *"Loss aversion overrides elegance"* — is
  classified `REPLACED_BY_EQUIVALENT`, and I checked the destination rather than the label: it is
  `R8 LOSS > ELEGANCE — completeness before synthesis` in `LEGEND_CORE.md` §14, beside R0–R7,
  plus `Lossless` in `ARCHITECTURE.md` §Core invariants. **The classification is honest.**
- **The `parallel_legend_protocol.md` incident.** Rule 4 now ends at *"in full, or not at all"*,
  byte-identical to the source; the two added sentences appear in **no** file under
  `framework/protocols/`; the withdrawal is recorded as `PROV-DIFF-AGAINST-TARGET` under an E.3
  lifecycle with an expiry, and the provenance survives in MAT-008 rather than being erased. The
  learning is in the correct class: one `ORIGINAL_OBSERVATION`, below E.2's threshold, not law.

**Objection.** The manifest's claim *"the router … legislates nothing"* is a mild overstatement:
§0 states three binding facts (medical-advice disclaimer, the `BATCH_COMMIT`-only rule for the
four current files, the public-edition rule). They are safety-critical, justified inline, and
neutralised by the router's own precedence clause — but they are normative sentences. NBN-4.

```
ROUTER ADJUDICATION: ACCEPT — conformant to §0.3, no loss demonstrated, duplication controlled by
                     an explicit precedence rule.
VERDICT: CONFIRMED (with NBN-4 and RC-9 on the summary counts).
REVIEWER_CONFIDENCE: HIGH — destinations and literals were checked mechanically, not read for tone.
RESIDUAL_UNCERTAINTY: I sampled 19 literals, not every sentence of a 600-line source.
WHAT_WOULD_CHANGE_MY_MIND: a rule from the old file that resolves to no destination.
AUTHOR_RESPONSE: PENDING_OPERATOR_ROUTING
```

---

## 5 · R-5 · PRIOR-ART DESIGN RECORD

```
PRIOR_ART_SOURCE_SHA256   = PRIOR_ART_ARCHIVED_SHA256 = 2563f82e82d661f98ff5eb2b029a8568b519d0ac3ae91e4fd76ba21704d6988e
```

Recomputed on the archived file: **identical**. Verified further: the first line is the document's
own title (`# LEGEND GOVERNANCE v3.1 — TARGETED HOSTILE PRIOR-ART REVIEW`) — **no header was
inserted into the historical bytes**; all ten `E1`–`E10` headings present; `DEFER` register
present; `Agno` preserved in its historical unverified state; the `PARTE 5` verdict preserved.

The proposed-vs-ratified divergences are represented as **provenance, not runtime law**, and the
ratified form governs in each case: E1 historical (binding to `GOVERNANCE_VERSION`) → ratified as
`APPLICABLE_GOVERNANCE_FINGERPRINT`; E2 (every mutation a transaction boundary) → ratified as the
durable milestone; E8 (`closed_by` on the opening event) → ratified as `CLOSES_EVENT_ID` on the
closing event with the source immutable. The candidate's implementations follow the **ratified**
forms, not the historical ones — checked against P7 and J.1.

```
VERDICT: CONFIRMED.   REVIEWER_CONFIDENCE: HIGH (hash identity is the primary proof).
RESIDUAL_UNCERTAINTY: none material.
WHAT_WOULD_CHANGE_MY_MIND: a mismatch between the two SHA-256 values, or a runtime artifact
                           implementing a historical form in preference to its ratification.
AUTHOR_RESPONSE: PENDING_OPERATOR_ROUTING
```

---

## 6 · R-6 · PENDING_IMPLEMENTATION AND UNRESOLVED

### 6.1 · The two thresholds, kept apart

| # | Component | Blocks CANONICAL COMMIT? | Blocks BOOTSTRAP / OPERATIONAL? | Adjudication |
|---|---|---|---|---|
| 1 | EVENT LEDGER writer + validator | **No** | **Yes** — §49.P requires it operational in the final report; G.3 makes it my analysis surface | Correctly pending. Must exist **before the lab is declared OPERATIONAL**, not merely "before the first batch" |
| 2 | Consolidated event view | No | Yes, with the writer | Correct |
| 3 | `LEARNING_INDEX` | No | **Yes** — §15 forbids filing a learning without consulting it; six records already wait | Correct; first act after commit |
| 4 | `ACTIVE_LESSONS` subsets | No | No (rehydration degrades gracefully) | Correct — and it is **my** authority, not Plan's |
| 5 | Runtime inventory / Agent Card | No | **Yes** — §8 requires assignment on *verified* capabilities; §47 step 15 | Correct: rows would be fabricated today |
| 6 | `deployment/local_instance.md` | No | Yes, at bootstrap step 2 | Correct; untracked by design, verified |
| 7 | Scientist C worktree `lettore-c` | No | **Yes** — §32 "da creare subito", §47 step 6 | Correct: creating a worktree is a bootstrap act |
| 8 | Skills/README pointer repair | No | No | Correct; mechanical, outside the frozen perimeter |

**No pending item blocks the canonical governance commit.** Five block the declaration of an
OPERATIONAL laboratory. That distinction is real and the candidate keeps it.

### 6.2 · 🔴 Omissions from the census — RC-7

Two artifacts the frozen text requires are **neither built, nor listed in
`PENDING_IMPLEMENTATION`, nor in `UNRESOLVED`, nor handled by `BOOTSTRAP.md`**:

| Artifact | Required by | Status |
|---|---|---|
| `HUMAN_APPROVAL_QUEUE` | Annex J.3; body §4 (*"Ogni HUMAN_REQUIRED genera un oggetto durevole … mai solo un messaggio"*); §49.P | absent and undeclared |
| `OPERATOR_DAILY_BRIEF` | body §10.4 (durable, at least once per working day); §49.L | absent and undeclared |

The queue is **load-bearing at the very next step of this sequence**: the `HUMAN_APPROVAL` that
follows this review is itself a `HUMAN_REQUIRED` of type MAJOR, which §4 says must produce a
durable queue object and never only a message. R-6's rule is explicit — *nothing may disappear by
omission* — so this must be declared even if building it stays pending.

### 6.3 · UNRESOLVED — census and adjudication

| # | Item | Authority (H.1) | Blocks approval? | Adjudication |
|---|---|---|---|---|
| 1 | PID-12 scientist ACTOR_IDs | Orchestrator at registration | No | Correctly deferred; permanent once set |
| 2 | PID-16 `MIRROR_RETROSPECTIVE` N | **not Mirror alone** (G.2) | No | **ESC-3** — I may not set it; route stated below |
| 3 | Design record | — | No | **Closed** — verified at R-5 |
| 4 | Two skill anchors + two descriptive lines | Plan (mechanical) | No | **Verified accurate**: `legend-start` cites `CLAUDE.md §LINT Severity`; `ARCHITECTURE.md:48` and `README.md:319` still call it the normative bootstrap. Honest declaration |
| 5 | Rule 5c `extraction_method` unenforced | Plan + Mirror | No | Correct: stated canonically, enforced by nothing. A `designed_for_growth` consequence-1 case; fix belongs to a schema change, not this candidate |
| 6 | `framework/master/` holds two peers | **Mirror** — referred to me explicitly | No | **ADJUDICATED: two peer files are the right shape.** Parity-of-sources and design-for-growth are independently cited superordinate principles; merging them would produce one file with two unrelated halves and weaken both citations |
| 7 | Home path in 11 tracked files | Operator | No | **Verified: exactly 11.** Pre-existing, gate passes. Flagged, not introduced here |
| 8 | Fingerprint never run by a second actor | — | No | **Closed at revision 5** — I reproduced it in review 001 |
| 9 | Post-RC-2 fingerprints not independently reproduced | — | No | **CLOSED BY THIS REVIEW** — I recomputed all four independently: plan `37c3b863…`, mirror `84d2b841…`, orchestrator `6b55605d…`, scientist `ce3c0d94…`, each exactly as claimed |
| 10 | All checkpoints unusable for resume | Plan | No | **Verified**: `CHK-plan-0006` opens generation 2 with the new fingerprint; 0001–0005 neither reused nor rewritten. P2.3's intended behaviour, correctly recorded |

```
VERDICT (R-6): REFINED — the census is accurate and well-reasoned for everything it contains, and
               incomplete by two required artifacts.
REFINED_FORMULATION: PENDING and UNRESOLVED are correctly adjudicated; the list is missing
                     HUMAN_APPROVAL_QUEUE and OPERATOR_DAILY_BRIEF.
REVIEWER_CONFIDENCE: HIGH — the census was run mechanically against the frozen text's requirements.
WHAT_WOULD_CHANGE_MY_MIND: a clause covering the queue or the brief that I did not find.
AUTHOR_RESPONSE: PENDING_OPERATOR_ROUTING
```

---

## 7 · R-7 · GATE-3 READINESS

| Annex D.2 field | State |
|---|---|
| `CANDIDATE_ID` / `REVISION` | present, consistent |
| `BASE_HEAD` | present; equals `main`; **0 behind** — GATE 0 base condition holds |
| `SOURCE_COMMITS` | present; **3 of 14 unresolvable** ❌ RC-6 |
| `CANDIDATE_CONTENT_HASH` | present and **verified** ✅ |
| `CHANGE_CLASS` | `MAJOR`, correct by definition (governance + authority + gate) |
| `LINT_RESULT` + pointer | re-run: `VERDICT: PASS`, 1 INFO ✅ |
| `PUBLICATION_GATE` + pointer | re-run: `PASS`, `BLOCKS: 0`, 4 non-blocking `[REVIEW]` ✅ |
| `MIRROR_REVIEW` | `PENDING`, correctly citing review 001 |
| `HUMAN_APPROVAL` | `PENDING` |
| `SNAPSHOT_ID` | `n/a until canonical execution — GATE 4 belongs to Orchestrator` ✅ correct restraint |

Further: **no later candidate exists** (one file in `governance/candidates/`); the tree is
reconstructible and was rebuilt independently in an isolated clone; no foreign dirty work is
present; the unit is coherent — one governance migration, not a bundle.

**Structural defect:** `## 6 · Verification record` appears **twice** (lines 228 and 265) with
`## 5b` between them, the first containing an orphan empty table header. RC-8.

```
CONCLUDING QUESTION — "Is there a verified defect that makes it imprudent to proceed to
HUMAN_APPROVAL?"

ANSWER: Yes, but none of them touch the content. Two are blocking (RC-6, RC-7), all five are
        repairable inside the manifest, and none changes CANDIDATE_CONTENT_HASH.

VERDICT: REFINED.   REVIEWER_CONFIDENCE: HIGH.
WHAT_WOULD_CHANGE_MY_MIND: RC-6 and RC-7 shown to be already satisfied elsewhere.
AUTHOR_RESPONSE: PENDING_OPERATOR_ROUTING
```

---

## 8 · REQUIRED_CHANGES

**All five are manifest-local. None changes `c39ecae8…`. None requires a third full review.**

| # | Change | Severity |
|---|---|---|
| **RC-6** | Correct the three `SOURCE_COMMITS` oids: `891fba91`→`891fba92`, `7f7c0cb0`→`7f7c0cb7`, `d371eed4`→`d371eed7`. Better: record full 40-char oids, which cannot be mistyped into a valid-looking prefix | **BLOCKING** |
| **RC-7** | Declare `HUMAN_APPROVAL_QUEUE` (J.3, §4, §49.P) and `OPERATOR_DAILY_BRIEF` (§10.4, §49.L) in `PENDING_IMPLEMENTATION`, with their eligibility threshold. The queue is required by the approval that immediately follows this review | **BLOCKING** |
| **RC-8** | Repair the section structure: one `## 6`, `## 5b` in order, no orphan table header | material |
| **RC-9** | Derive the §3 migration-map counts or drop them. Group D reconciles only if the two `PRESERVED (in router)` rows are excluded by an unstated convention; group E (claimed 4, actual 5) reconciles under none. RC-3's fix — *derive, never hand-maintain* — was applied to the domain count and not carried to these | material |
| **RC-10** | `0 behind, 12 ahead` is stale: actual is 0/14 at `BRANCH_TIP`, 0/16 at branch head. The load-bearing half (`0 behind`) is correct | minor |

---

## 9 · ESCALATE_TO_OPERATOR

**ESC-2 — two declared deviations from the frozen text need ratification, not reviewer acceptance.**
PID-09 departs from I.2 step 7's literal `/roles/<suo>.md`; PID-10 replaces §7/Annex H's
*"replicata nei CLAUDE.md"* with a pointer table. Both are **declared, reasoned, and preserve the
purpose** of the clause they depart from, and I recommend **ACCEPT** for both. But a deviation
from frozen text is a governance matter, and H.1 assigns governance to the operator. Ratifying
them silently through a Mirror PASS would be the reviewer taking an authority he does not hold.

**ESC-3 — `MIRROR_RETROSPECTIVE` N remains unassigned, and I may not assign it.** G.2 places
retrospective methodology inside Mirror's own method, which Mirror may not change alone. The
route is `MIRROR_UPGRADE_PROPOSAL → Plan candidate → independent reviewer chosen by Orchestrator →
operator`. I can open that proposal on instruction; I cannot short-circuit it by writing a number
into this review.

---

## 10 · NON_BLOCKING_NOTES

**NBN-3 — the control-plane exclusion is unbounded, and this is the residual risk of PID-19.**
Mutation-tested: a file created at `ledger/smuggled_rule.md` containing normative text left the
hash **unchanged** and was silently classified as excluded. Today the eight excluded paths are
genuinely control plane and `--show-domain` makes them visible, which is a real compensating
control. But nothing constrains *what* may be placed under `ledger/`, and the region will grow as
six actors write checkpoints, tasks and events. **Do not repair this in the current candidate:**
P5 is content, so amending it changes the hash and forces a new review, for a risk that is today
theoretical. Recommended for the evidence-driven cycle: have the script assert that excluded paths
match the declared shapes (`ledger/checkpoints/<actor>/`, `ledger/events/<actor>.jsonl`,
`ledger/tasks/<actor>/`) and fail loudly on anything else — the same fail-loud discipline PID-03
already applies to the prose it parses.

**NBN-4 — "the router legislates nothing"** is a mild overstatement; §0 carries three binding
facts. Justified inline, safety-critical, and neutralised by the router's own precedence clause.
No action.

**NBN-5 — UNRESOLVED #6 adjudicated in the candidate's favour:** two peer files in
`framework/master/` is the right shape.

**NBN-6 — my own review 001 sweep was not exhaustive.** 144 combinations, and the variant that
mattered (a listing without its terminating newline) was not among them. The finding held only
because I declared the mechanism `UNKNOWN` instead of inferring one. Recorded against my method,
not the candidate's.

---

## 11 · GOVERNANCE_DEFECT_CANDIDATES (against the FROZEN text — recorded, not acted on)

**GDC-1 — the bootstrap sequence requires an approval before it builds the approval queue.**
Body §4 and Annex J.3 require every `HUMAN_REQUIRED` to create a durable object in the
`HUMAN_APPROVAL_QUEUE`, *"mai solo un messaggio"*. But §47's sequence puts `Mirror hostile review
→ HUMAN_APPROVAL → CANONICAL_BATCH_COMMIT → bootstrap` **before** any step that creates the queue,
and §49.P requires it operational only in the closing report. The first approval the system ever
performs is therefore one the frozen text cannot record in the form it mandates. RC-7 is the local
consequence; the ordering gap is in the frozen text and belongs to the evidence-driven v3.2 cycle.

**GDC-2 — G.3 delegates `N` to nobody.** *"MIRROR_RETROSPECTIVE ogni N batch"* names no delegate,
and G.2 forbids Mirror from setting it alone. A parameter that no authority may set is a defect in
the delegation, not in Plan's refusal to take it. Plan handled it correctly by leaving it
`UNRESOLVED`.

**Neither makes immediate execution of v3.1.1 unsafe**, so neither is escalated as a BLOCKER.

---

## 12 · DISPOSITION

```
MIRROR_REVIEW: REVISION_REQUESTED

CANDIDATE_ID:           CAND-20260816-GOV311 — revisione 5
CANDIDATE_CONTENT_HASH: c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239
BASE_HEAD:              749a9a9b8f29c855f803a43b979c591532557561
REVIEW_DATE:            2026-08-16
REVIEWER:               mirror

REQUIRED_CHANGES:             RC-6, RC-7 (blocking); RC-8, RC-9 (material); RC-10 (minor)
ESCALATE_TO_OPERATOR:         ESC-2 (ratify two declared deviations), ESC-3 (route N)
NON_BLOCKING_NOTES:           NBN-3, NBN-4, NBN-5, NBN-6
GOVERNANCE_DEFECT_CANDIDATES: GDC-1, GDC-2
```

**What this disposition does and does not say.** The content at `c39ecae8…` was reviewed in full
across R-1…R-7 and **no defect was found in it**. Every blocking defect of revision 4 is genuinely
repaired, and repaired structurally rather than patched. The five required changes all lie in the
manifest — the control plane — so the corrected manifest will describe the **same** content under
the **same** hash.

Consequently the re-review is narrow: verify the three oids resolve, the two artifacts are
declared, the sections are ordered, the counts are derived or dropped. This review's R-1…R-7
verdicts remain bound to `c39ecae8…` and do not need to be redone — no verdict is transferred
across hashes, because the hash does not change.

**No file of the candidate was modified. No canonical commit was executed. Plan was not contacted.
No approval was granted. No lease was acquired.**
