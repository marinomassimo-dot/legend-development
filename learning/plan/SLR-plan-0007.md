---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0007
actor_id: plan
role: Plan
date: 2026-08-19
task: XPORT-ROUTING-001 · directive v1 · generation 1 — cross-session transport discipline and
  actor session lifecycle / routing, following canonical execution of CAND-20260818-SCIENTIST-AB-SPEC
scope: one harness probe, one author response, one transport protocol, one partition decision,
  and a routing candidate deliberately not opened
curation: PENDING — E.2 gives epistemic curation to Mirror. Every CONFIRMATION_CLASS below is
  **proposed**, never self-certified. SLR-plan-0006-COR-001, written this session, is offered as
  a further instance of SLR-plan-0004 L-2 and is likewise proposed, not ratified.
derived_from: [SLR-plan-0004, SLR-plan-0005, SLR-plan-0006, SLR-mirror-0013, SLR-mirror-0014]
---

# SLR-plan-0007 — two documents said a thing was impossible, and the second instrument had been there all along

## Context

The Scientist A/B specification became canonical at `4454feab`. This session was asked to close
the owed author response, classify three carried observations, probe the harness **once**, and
decide whether cross-session transport and actor routing are one candidate or two.

The probe was supposed to be preparatory. It turned out to be the finding.

---

## WORK COMPLETED

```
IDENTITY          rehydrated from durable state alone; worktree == git top-level == evidence-index;
                  roles/plan.md read in full; canonical main verified 4454feab; Scientist
                  fingerprint recomputed at source 82423a48b700bc…; lease #7 derived RELEASED,
                  ACTIVE by derivation 0; Mirror ACCEPT and HUMAN_APPROVAL both traced to their
                  commits and read
AUTHOR RESPONSE   reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md — P-12, P-13 and the three
                  Annex E.2 re-classifications of §10.2, all accepted, each reproduced first
CORRECTION        learning/plan/SLR-plan-0006-COR-001.md — P-13's half that lives in Plan's own
                  learning record, appended never edited
OBSERVATIONS      A ROUTING_RELEVANT · B ENVIRONMENTAL, instance not currently reproducible ·
                  C HISTORICAL_CONTROL_PLANE_DEBT, four instances not one, not load-bearing
PROBE             governance/design_records/runtime_harness_probe_20260819.md — one probe,
                  twelve findings, four epistemic classes kept apart
PROTOCOL          framework/protocols/cross_session_transport.md — PROPOSED
PARTITION         SPLIT · Transport first · Routing blocked on three preconditions, not merely next
```

---

## PROBLEMS

### 1 · The premise three canonical-or-durable artifacts rest on is false at this runtime version

`framework/protocols/scientist_reading_modes.md` §1.2 — canonical since this morning — states
*"No actor observes its own SESSION_REF."* `runtime/agent_card_registry.md` derives four session
references by set complement across peer listings precisely because of it. Lease record #7
declares `SESSION_REF: NOT DECLARED` and gives that as the reason. Phase −1's experiment `E5`
concluded *"Not obtainable: `session_ref` … The field is dropped from the schema"*, and
`actor_identity_proposal.md` §6 excludes a `session_ref` field from the proposed registry on that
authority: *"A session cannot learn its own name; a schema field an actor cannot fill about
itself will be filled by guesswork."*

`claude agents --json` returns this session's own row. Name, `sessionId`, `cwd`, `pid`.

### 2 · The number of live sessions per actor is not one, and has not been for days

`plan`: eight. `mirror`: seven. `scientist-a` and `scientist-b`: zero. And the session the Agent
Card registry records as `plan`'s current one — `evidence-index-59`, verified at L1 on
2026-08-17 — is **alive**, three days later, and is not this session.

### 3 · "The installed runtime version" is not a thing this machine has

Four extension versions installed, at least two hosting live sessions concurrently, and
`claude --version` on `PATH` reporting a third binary that hosts nothing.

### 4 · Two bounds in one schema, one enforced and one not

`SendMessage.to` declares `pattern` and the runtime rejects 213 characters with a structured
error. `SendMessage.summary` declares `maxLength: 200` and the runtime accepted 264 without a
word. Nothing in the schema distinguishes them.

---

## SOLUTION

The probe was performed **once** and persisted as a design record both candidates cite, rather
than twice by two candidates that would then disagree. Every claim carries one of four classes —
`DOCUMENTED`, `OBSERVED`, `REPORTED_UPSTREAM`, `PROPOSED` — plus `MEASURED_EARLIER` for facts in
`launch/KERNEL_SPEC.md` taken against a runtime no longer installed.

Transport was written as a **minimal extension**: it adds no message type, no envelope field, no
ACK and no escalation path. It fills the `DURABLE_POINTER` that Annex B.1 has always carried, and
cites `KERNEL_SPEC`'s measured failure classes instead of renaming them.

Routing was **not opened**, and §"IMPACT" says why that is the finding rather than the shortfall.

---

## LEARNING

### L-1 — *An impossibility measured through one instrument is a fact about the instrument.*

`proposed: ORIGINAL_OBSERVATION (plan, this session) · offered for wider scope`

`E5` concluded `session_ref` was **not obtainable**. Its evidence, in full: *"`ListAgents` lists
peers; a session does not appear in its own listing."* That is a true sentence about `ListAgents`.
The conclusion drawn from it was about the runtime.

The second instrument was not new, not hidden, and not a later release. `claude agents --json` is
documented in `claude agents --help`, and **`launch/legend_launch.sh` — tracked in `main`, written
two days after `E5` — already calls it**, for a different purpose, four lines from a comment
explaining why it refuses to parse the supervisor's roster instead. The laboratory had the
instrument, used it, and did not re-ask the question the other instrument had closed.

The detector, which is the reusable half:

> **When a report concludes `NOT OBTAINABLE`, the finding is only as wide as the widest
> instrument tried.** A negative result must name its instrument in the conclusion, not only in
> the method — because the conclusion is what gets quoted into the next document, and by the
> third quotation the instrument is gone.

Three quotations is exactly what happened: `E5` → `actor_identity_proposal.md` §6 → the canonical
protocol §1.2, which states it with no instrument at all.

🔴 **What this does NOT license.** It does not flip any of the conclusions those documents drew.
`ACTOR_ID` is still not `SESSION_REF`; a session reference is still ephemeral; no actor may invent
one. Those hold for reasons the probe *strengthened*. One stated ground was wrong; the position
was right.

### L-2 — *A version change can enable a capability, and nothing was watching for that direction.*

`proposed: ORIGINAL_OBSERVATION (plan, this session)`

Every version-bound rule this session wrote, and every one it read, points the same way: a runtime
upgrade may **invalidate** a guarantee, so revalidate. `A.6`'s refusal rule has the same shape,
and so does the fingerprint.

Nothing anywhere says: a runtime change may **lift a measured blocker**, and a design that was
correctly refused on the old measurement may become buildable without anyone noticing, because
nobody re-runs a feasibility study that concluded *no*.

The asymmetry is structural, not accidental. A `PASS` that decays into a `FAIL` hurts somebody, so
it gets a trigger. A `FAIL` that decays into a `PASS` hurts nobody, so it gets none — it just
quietly stops being true, and the document that recorded it goes on being cited.

```
REVALIDATION_TRIGGER, as everyone writes it   OBSERVED  → VERSION_CHANGED → REVALIDATION_REQUIRED
the direction nobody writes                   REFUTED   → VERSION_CHANGED → RE-TEST BEFORE CITING
```

Proposed consequence, and it is cheap: **a `DEFERRED` or `NOT_FEASIBLE` verdict that rests on a
runtime measurement carries the same `VERSION_OBSERVED` and `REVALIDATION_TRIGGER` fields as a
guarantee does.** `actor_identity_feasibility.md` has neither, and it is two months from being
quoted as settled law by someone who was not there.

### L-3 — *The condition a routing design must handle was the live state of the machine, and no experiment was needed to find it.*

`proposed: REPLICATION of SLR-plan-0004 L-1 (plan, this session), SCOPE widened`

`SLR-plan-0004` L-1 is *the finding was a lower bound, and the code was the denominator*: a defect
counted over the population the finder happened to look at, rather than over the population that
exists. Mirror widened it at `REV-SCIAB-MIRROR-006` §10.2 from findings-in-code to
normative-claims-in-prose.

This session widens it once more, to **hypothetical failure conditions**. `T-ROUTE-1` (zero
current) and `T-ROUTE-3` (multiple current) were handed to me as tests to design against. They
are not hypotheses. `scientist-a` and `scientist-b` have zero live sessions and `plan` has eight,
right now, and one `claude agents --json` shows it.

> **Before designing against a failure condition, measure whether it is already the state of the
> system.** A condition being enumerated in a test matrix is weak evidence that it is rare; the
> matrix records what the author imagined, and the machine records what is.

The cost of not asking is specific: a routing design specified against *zero or multiple as edge
cases* would have put its effort in the wrong place. **Multiple is the steady state here**, and
the honest cardinality target is not *keep it at one* but *elect one out of eight without ever
electing by recency*.

### L-4 — *An anti-ontology check found four existing surfaces, and three of them are on hold.*

`proposed: REPLICATION of SLR-plan-0005 L-3 on a new form — a design space rather than a harness`

Before proposing where routing state should live, I looked for what already exists. Four surfaces,
all tracked in `main` or on an actor branch, none of which I would have found by reasoning:

```
launch/legend_launch.sh + KERNEL_SPEC.md   an actor-generic, fail-closed birth/resume kernel with
                                           a per-(actor, cell) O_EXCL lineage reservation
framework/protocols/actor_identity_*.md    a Phase −1 feasibility report and a registry proposal,
                                           BUILD_MINIMAL_DIRECTORY, provisional
runtime/agent_card_registry.md             Annex I.4's card, with CURRENT_SESSION_REF already in it
PROPOSAL-C9-STATE-MODEL §7.2               where CURRENT_SESSION_REF should live, ACCEPTED
```

**Three of the four are on an explicit hold**, and none of the holds is mine to lift: C-9 carries
`acceptance_is_not_adoption: true` and *"no implementation and no governance modification until
that review completes"*; `BUILD_MINIMAL_DIRECTORY` is provisional *pending operator acceptance*;
and `MULTI_AGENT_ARCHITECTURE_FEASIBILITY` is `PRESERVED, NOT AUTHORIZED, NOT STARTED` with an
entry condition that is not satisfied.

The learning is not *look before you build* — that is `SLR-plan-0005` L-3 and it is already
recorded. It is the narrower thing that surprised me:

> **The anti-ontology check has a second output, and it is the more useful one.** Its first output
> is *which surface to extend*. Its second is *which surfaces are frozen, by whom, and what would
> unfreeze them* — and that output can convert a design task into an escalation. Here it did:
> Routing is not blocked on design effort, it is blocked on three decisions nobody has asked the
> operator to make.

Had I not looked, I would have produced a routing candidate that was, in substance, C-9 §7.2 plus
`BUILD_MINIMAL_DIRECTORY` re-derived under new names — self-authorizing two held decisions by
re-deriving them, which is the failure mode a hold exists to prevent.

---

## MICRO-UPGRADE

**Applied this session, small, and each closes something that was open:**

1. `governance/design_records/runtime_harness_probe_20260819.md` — the harness measured once,
   with a per-session `VERSION_OBSERVED` discipline, so a Transport candidate and a Routing
   candidate cannot drift apart by measuring it twice.
2. **One `KERNEL_SPEC` open measurement closed, in the negative, at zero cost.** *"Is `SendMessage`
   immediately available in an interactive session while requiring a `ToolSearch` in a background
   one?"* — no: it is deferred in this interactive session too, so `TOOL_DEFERRED` is not a
   property of the background actor class. Observed, not argued.
3. `learning/plan/SLR-plan-0006-COR-001.md` — the false noun in Plan's own canonical learning
   record, corrected by appending rather than by editing testimony.
4. Two findings handed to `launch/` and not acted on: the version gate reads the wrong binary, and
   the kernel births only `background` while every LEGEND actor is `interactive`. Recorded as
   H-2 and H-3 rather than repaired outside scope.

---

## IMPACT

**The deliverable this session was expected to produce is a routing candidate, and it produced a
reasoned refusal to produce one.** That is the impact, and it should be judged as such.

What is delivered: Transport, which stands alone, is a minimal extension of Annex B, and has eight
acceptance tests of which three are `PASS` on observation, four `PASS` by construction, and one is
recorded `NOT RUN` because running it requires exactly the thing Routing does not yet provide.

What is not delivered, and why it would have been worse to deliver it: a Routing candidate
depends on three held decisions and on a Phase −1 result whose central negative this session
falsified. Writing it now would have meant re-deriving two held proposals under new names and
binding a candidate to a feasibility study that needs re-running.

**The residual risk is that the refusal is wrong** — that Routing could be scoped narrowly enough
to sit inside Plan's authority without touching C-9 §7.2 or `BUILD_MINIMAL_DIRECTORY`. Mirror
should attack the partition decision itself, not only its content; the manifest §10 states the
three preconditions so that each can be contested separately.

---

## CLASSIFICATION · SCOPE · EVIDENCE

```
CLASSIFICATION   L-1 ORIGINAL_OBSERVATION · L-2 ORIGINAL_OBSERVATION ·
                 L-3 REPLICATION of SLR-plan-0004 L-1, scope widened ·
                 L-4 REPLICATION of SLR-plan-0005 L-3, new form
                 ALL PROPOSED — Mirror curates (E.2, H.1)

SCOPE            L-1, L-2  offered for wider scope: they are about how negative results and
                           feasibility verdicts are recorded, in any domain
                 L-3, L-4  laboratory-internal

EVIDENCE         L-1  claude agents --json returning this session's own row, against E5's
                      "not obtainable"; the same command already present in legend_launch.sh
                 L-2  actor_identity_feasibility.md carries no VERSION_OBSERVED on any verdict
                 L-3  8 / 7 / 1 / 0 / 0 live sessions per actor worktree, one command
                 L-4  four surfaces enumerated, three holds quoted at source

REVIEW           the partition decision and L-1's scope are the two things most worth attacking.
                 L-1 in particular is a learning about a mistake three artifacts share, and an
                 author who has just found such a thing is the reader least able to judge how
                 general it is.
```
