---
artifact: LEGEND governance — Plan-defined parameters
governance_version: 3.1.1
status: PROPOSED — normative once Mirror hostile review passes and the operator approves
normative: yes (on approval)
authored_by: plan
authored_on: 2026-08-16
authority: Annex H.1 — "Composizione APPLICABLE_GOVERNANCE_FINGERPRINT | Plan (modifica governata)";
  A.1 RETRY_POLICY default; B.3 ACK timeout and HEARTBEAT cadence; D.2 content-hash definition;
  E.5 role budgets; J.1 ledger design
change_class: MAJOR — these values are governance; changing them follows gate 3
---

# Plan-defined parameters

The annexes delegate seven values and definitions to Plan by name. They are collected here, in
one place, so that a reader can see every knob at once and so that the fingerprint has a single
artifact to hash rather than seven scattered footnotes.

**Nothing here overrides an annex.** Where an annex states a rule, this file supplies only the
value the annex left open. Each entry names the delegating clause.

Two disciplines from the repository's own operating rules shape the choices below, and are worth
stating because they rule out the obvious answers:

- *Will this still be informative at the thousandth batch?* A control that is correct today and
  noise at scale is a future alarm nobody hears. Timeouts short enough to be tidy today would
  fire constantly against actors that legitimately spend an hour inside one turn.
- *Never pin a number a human must remember to update.* Where a number could not be avoided, it
  is not left as a bare constant: it is registered as a `PROVISIONAL_OPERATIONAL_PRACTICE`
  (Annex E.3), which forces an explicit `PROMOTE | REJECT | EXTEND_WITH_REASON` at expiry. The
  governance already owns the machinery that makes someone decide; using it beats a comment
  asking a future reader to remember.

---

## P1 · RETRY_POLICY — default `on_exhaust`

**Delegated by:** A.1 — *"on_exhaust: REASSIGN | PARK | ESCALATE (default definito da Plan)"*.

```
DEFAULT_ON_EXHAUST: PARK
```

A task contract may name a different value; this is the default when it does not.

**Why PARK and not the other two.** `REASSIGN` spends a second actor on a task that has already
exhausted its retries without anyone having diagnosed why — it converts one failure into two.
`ESCALATE` spends a HUMAN_REQUIRED, and §3 measures exactly that: an escalation that Orchestrator
could have resolved counts as `PREVENTABLE` in the autonomy ledger. `PARK` keeps the checkpoint
(A.6), keeps the rest of the laboratory running, and leaves the decision to Orchestrator with
the retry history already in the durable state. It is the only one of the three that spends
nothing while losing nothing.

---

## P2 · APPLICABLE_GOVERNANCE_FINGERPRINT — composition

**Delegated by:** A.6 and H.1 — composition per role / task class is Plan's, under governed change.

```
FINGERPRINT_COMPOSITION_VERSION: 1
```

The composition is itself versioned: changing it changes every fingerprint in the system, so the
change must be visible rather than inferred from a wave of invalidations.

### P2.1 · Composition function

```
inputs      = the ordered set of governance artifacts pertinent to the role (P2.2),
              each identified by repo-relative path, plus the actor's own role contract
per input   = SHA-256 over the exact bytes of the named artifact
              (whole file, or the extracted section range where P2.2 names a section)
serialize   = for each input, sorted lexicographically by identifier:
                  "<identifier>:<sha256-hex>\n"
fingerprint = SHA-256 over that serialization, full hex
```

Section extraction, where used, is mechanical: from the line of the named heading up to (not
including) the next heading of equal or higher level, bytes taken verbatim.

### P2.2 · Pertinence sets

`CORE` binds every actor. A change inside CORE invalidates all in-flight checkpoints, which is
the intended behaviour: CORE is the part of the constitution under which any actor's work is
being done.

```
CORE = GOVERNANCE_v3.1.1.md
     + annex_a_task_contract.md
     + annex_b_message_protocol.md
     + annex_h_authority_matrix.md
     + annex_j_runtime_control_plane.md § J.0
     + annex_j_runtime_control_plane.md § J.2
     + annex_j_runtime_control_plane.md § J.3
     + plan_defined_parameters.md
     + <the actor's own role contract>
```

| Role | CORE plus |
|---|---|
| `scientist` (A/B/C) | Annex C, Annex E, Annex F |
| `plan` | Annex D, Annex E, Annex I, Annex J § J.1 |
| `mirror` | Annex C, Annex E, Annex F, Annex G, Annex J § J.1 |
| `orchestrator` | Annex C, Annex D, Annex F, Annex G, Annex I, Annex J § J.1, Annex J § J.4 |

**Annex J is deliberately split rather than hashed whole.** A.6's own worked example of a
change that must *not* invalidate anything is *"un cambio alla COST_POLICY mentre uno Scientist
legge un paper"* — and COST_POLICY is J.4. Hashing Annex J as one file would invalidate every
scientist checkpoint on exactly the change the annex uses to illustrate the opposite. J.4
therefore sits only in Orchestrator's set, because Orchestrator is the actor whose behaviour it
governs (it classifies HUMAN_REQUIRED of type SPEND).

This is a statement about *resume compatibility*, not about what binds. The cost stop condition
(§48) binds every actor at all times whether or not J.4 is in its fingerprint. Compatibility
asks "were the rules I was working under still the rules?"; it does not ask "which rules apply
to me?".

### P2.3 · Known calibration risk, per A.6

The whole body sits in CORE, so any body change invalidates everything. The body is frozen and
changes only by MAJOR governance upgrade, where broad invalidation is the correct outcome. If
that stops being true — if the body starts absorbing minor edits — the composition is too broad
and must be narrowed to sections. A.6 assigns Mirror the monitoring of the invalidation rate;
this is the specific signal to watch.

### P2.4 · Executable, and the prose above is its input

A composition recorded only in prose decays silently, and the repository has already paid for
that lesson in its adjudication recipes: *"A recipe recorded only in prose decays silently; one
a command runs cannot."* So no actor hand-assembles a fingerprint:

```
governance/scripts/governance_fingerprint.py compose --role <role>
governance/scripts/governance_fingerprint.py inputs  --role <role>
```

The script does **not** carry its own copy of the pertinence sets. It parses § P2.2 above — the
CORE block and the per-role table — so this document remains the single source of truth and the
two cannot disagree. Editing the table changes the computed fingerprint; if the table stops
parsing, the script fails loudly rather than falling back to a stale default.

One consequence is worth stating because it looks like a bug the first time it is seen: this file
is itself in `CORE`, so **editing this file changes every role's fingerprint**, including through
edits to this very paragraph. That is correct. A change to the parameters is a change to the
rules an actor is working under, and A.6 says resume compatibility is exactly the question of
whether those rules still hold.

---

## P3 · ACK timeout

**Delegated by:** B.3 — *"ACK obbligatorio su STATE_CHANGE: yes entro timeout (Plan)"*.

```
ACK_TIMEOUT: 30 minutes          [PROVISIONAL — see P3.1]
on timeout   → resend (dedup via MESSAGE_ID)
on 2nd miss  → BLOCKER
```

The constraint that sets the floor is a property of this runtime, not of the protocol: an actor
occupied inside a single long turn — a full-text read, a validator run — cannot see a message
until that turn ends. A timeout shorter than a legitimate working turn does not detect failure;
it manufactures BLOCKERs, and a BLOCKER that usually means nothing is a control that will be
ignored on the day it means something.

### P3.1 · Registered as PROVISIONAL (Annex E.3)

```
PRACTICE_ID: PROV-ACK-TIMEOUT-30M
HYPOTHESIS: 30 minutes exceeds the longest legitimate silent turn often enough that a missed ACK
            signals a real delivery or runtime failure rather than a busy actor
APPLIES_TO: all STATE_CHANGE: yes messages
EVIDENCE_EXPECTED: ACK latency distribution from the event ledger (J.1) over the first batches
SUCCESS_CRITERION: false-BLOCKER rate below one per batch, with no missed real failure
FAILURE_CRITERION: BLOCKERs raised on actors that were merely working
EXPIRY: after the third scientific batch — PROMOTE | REJECT | EXTEND_WITH_REASON
ROLLBACK: value returns to UNRESOLVED; Orchestrator falls back to explicit status requests
```

---

## P4 · HEARTBEAT cadence

**Delegated by:** B.3 — *"HEARTBEAT attore→Orchestrator a cadenza fissa (Plan)"*.

```
HEARTBEAT_CADENCE: 30 minutes    [PROVISIONAL — see P4.1]
DOWN after 3 consecutive missed heartbeats (≈ 90 minutes)
```

A heartbeat here costs an actor turn, so cadence trades against the work it interrupts. Three
missed beats before DOWN is what keeps a single long turn from being read as a crash, and DOWN
is not a destructive verdict: it parks or reassigns with generation+1 (§36.6), all of which is
recoverable.

### P4.1 · Registered as PROVISIONAL (Annex E.3)

```
PRACTICE_ID: PROV-HEARTBEAT-30M-3X
HYPOTHESIS: 30/90 distinguishes a crashed or closed session from a working one without
            interrupting long reads
APPLIES_TO: all persistent actors
EVIDENCE_EXPECTED: DOWN declarations vs actual session deaths, from the event ledger
SUCCESS_CRITERION: every DOWN corresponds to a session that genuinely needed reopening
FAILURE_CRITERION: an actor declared DOWN while mid-task, or a dead session unnoticed for hours
EXPIRY: after the third scientific batch — PROMOTE | REJECT | EXTEND_WITH_REASON
ROLLBACK: cadence returns to UNRESOLVED; DOWN determined by operator observation
```

This resolves the `HEARTBEAT_CADENCE = UNRESOLVED` that Plan declared at rehydration.

---

## P5 · CANDIDATE_CONTENT_HASH — the candidate content domain and its hash

**Delegated by:** D.2 — *"hash del CONTENUTO (tree/patch deterministico definito da Plan) — NON
l'hash git del commit futuro"*.

**This section is the single authoritative definition.** A candidate manifest **references** it;
it never restates it. `governance/scripts/candidate_content_hash.py` parses the two declarations
below rather than carrying its own copy, so the executable form and the governed form cannot
disagree.

```
CANDIDATE_HASH_VERSION: legend-candidate-v3
```

### P5.1 · The candidate content domain

Two kinds of artifact live on a candidate branch, and conflating them creates a fixed point:

- **CONTENT** — what is proposed for canonical integration: the governance body and annexes, role
  contracts, framework instruction, protocols, scripts, the disease model, documentation, the
  bootstrap and deployment files. **Content determines the candidate's identity.**
- **CONTROL PLANE** — artifacts whose function is to *describe or manage* a candidate, a review,
  or an actor's runtime state: candidate manifests, checkpoints, task claims, the event ledger.
  They exist because of the candidate; they are not the candidate.

The rule follows from the difference: **an artifact that describes the candidate must not be able
to change the identity of what it describes, and an artifact that constitutes the candidate must
always change it.** A manifest recording a hash of a tree containing that manifest is a fixed
point; so is a checkpoint recording the candidate's state inside the hashed tree. Revision 4
excluded the first and left the second standing, which is what Mirror found.

Control-plane roots are declared here, exhaustively, as directory prefixes:

```
CONTROL_PLANE_ROOTS:
- governance/candidates/
- ledger/
```

Everything not under a declared root is content. Adding a root is a **governed change to this
file**, reviewable as such — never an ad-hoc exclusion made while preparing a candidate. The
script prints every excluded path under `--show-domain`, so a reviewer sees exactly what was
dropped rather than trusting that the filter did what it says.

Nothing scientific or normative can be excluded by accident: `disease-models/`, `framework/`,
`roles/`, `scripts/`, `deployment/`, the top-level documents and all of `governance/` except
`candidates/` are outside both roots and always in the domain.

### P5.2 · The hash

```
serialized = CANDIDATE_HASH_VERSION + "\n"
           + BASE_HEAD + "\n"
           + for each included entry, path-sorted:  <git ls-tree -r --full-tree line> + "\n"

CANDIDATE_CONTENT_HASH = SHA-256(serialized), full hex
```

Each `ls-tree` line carries mode, type, object id and path, so a permission change or a blob
change moves the hash exactly as a content change should. `BASE_HEAD` is inside the hash as well
as beside it, so an approval cannot be transplanted onto a different base while still matching.

**Every entry is newline-terminated, including the last.** This is stated because its absence
caused a real defect: at revision 4 the recorded value was computed through a shell variable,
where `$(...)` strips the trailing newline, while the published command used a pipe, which keeps
it. One byte, two different hashes, on the same tree — and the count reported alongside it was
short by one for the same reason. Byte layout is therefore pinned in the definition, and computed
by a script that never passes the listing through a shell.

### P5.3 · Reproduction

```bash
python3 governance/scripts/candidate_content_hash.py --base <BASE_HEAD> --tip <BRANCH_TIP>
```

Add `--show-domain` to print the version, the base, the tip, the included entry count and every
excluded path. The count is **derived by the command**, never maintained by hand in a manifest.

The version prefix moves to `v3` because both the byte layout and the excluded roots changed;
`v1` and `v2` values can therefore never collide with these.

---

## P6 · ACTIVE_LESSONS — role subset budgets

**Delegated by:** E.5 — *"ogni subset role-specific ha un budget dimensionale definito da Plan"*.

```
PER_ROLE_SUBSET_BUDGET: 25 lessons OR 4 000 words, whichever binds first   [PROVISIONAL]
overflow → Mirror compresses or demotes (E.5); the RAW archive is never touched
```

A fixed cap is the right shape here — not despite the growth discipline but because of it. E.5
already defines what happens when the cap is reached, so the number does not silently degrade at
scale: it triggers the compression the annex designed. A budget expressed as a fraction of
something growing would instead let the subset grow forever while appearing bounded.

### P6.1 · Registered as PROVISIONAL (Annex E.3)

```
PRACTICE_ID: PROV-LESSON-BUDGET-25
HYPOTHESIS: 25 lessons is enough to carry a role's learned behaviour and small enough to be
            re-read at every rehydration without displacing task context
EVIDENCE_EXPECTED: repeated errors on already-learned patterns (E.5 DETECTION); actor requests
SUCCESS_CRITERION: no recurrence of a pattern whose lesson was demoted for budget
FAILURE_CRITERION: a demoted lesson is followed by the failure it described
EXPIRY: at the second MIRROR_RETROSPECTIVE — PROMOTE | REJECT | EXTEND_WITH_REASON
ROLLBACK: budget suspended; full ACTIVE_LESSONS set loaded until recalibrated
```

---

## P7 · EVENT LEDGER — one-writer design

**Delegated by:** J.1 — *"Design one-writer (decisione di Plan): (a) … oppure (b) …"*.

```
DECISION: (a) — per-actor append-only event file inside each actor's own worktree,
                consolidated by Plan into a derived canonical view
FORMAT:   JSON Lines, one event per line, append-only
PATH:     ledger/events/<ACTOR_ID>.jsonl   (in the actor's own worktree)
VIEW:     ledger/consolidated/  — derived, rebuilt by replay, never hand-edited
```

**Why (a) and not (b).** Option (b) derives events from commits plus ACKed messages, and several
event types in J.1's own minimum list leave neither: `CHECKPOINT_WRITTEN`, `ACTOR_DOWN`,
`LEASE_STALE`, `HUMAN_REQUIRED_OPENED`, `RESUMED_FROM_MILESTONE`. A ledger that structurally
cannot record its own recovery events is exactly the wrong instrument for Mirror, whose primary
analysis surface it is meant to be (G.3). Option (a) satisfies one-writer by construction —
each file has exactly one writer, its own actor — with no shared multi-writer file anywhere.

**`closed_by` appears only in the consolidated view.** The source line is never rewritten; the
closing event carries `CLOSES_EVENT_ID` pointing back. This is J.1's strict rule and it is the
reason the consolidated view must be rebuildable rather than maintained.

**This should reuse the existing append-only machinery, not invent a second one.** The
repository already runs an append-only ledger with a hash chain and a tail anchor
(`framework/scripts/fulltext_receipts.py`, whose `verify` the LINT already consumes), and its
own operating rules name uneven application as the characteristic failure of a system that grows
by accretion: *"Before building a guard, look for it — it is probably already here."* The event
ledger's writer and validator are to be built on that pattern, and any divergence from it stated
with a reason. Tracked as a debt; not yet built.

---

## Not delegated to anyone — recorded so it is not lost

`MIRROR_RETROSPECTIVE ogni N batch` (G.3) leaves `N` unassigned: the annexes give it to neither
Plan, nor Mirror, nor Orchestrator. Plan does not take it — G.2 places retrospective methodology
inside Mirror's own method, which Mirror may not change alone. It is flagged as
`UNASSIGNED_PARAMETER` for adjudication at bootstrap, and left `UNRESOLVED` here rather than
quietly filled in.
