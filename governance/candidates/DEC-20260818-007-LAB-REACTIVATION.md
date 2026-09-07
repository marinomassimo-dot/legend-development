---
artifact: HUMAN_REQUIRED — lab reactivation
id: DEC-20260818-007-LAB-REACTIVATION
status: DECISION REQUIRED
decision_owner: operator
prepared_by: plan (materialized · §2.1 measured here) · orchestrator (composed from measurement) · operator (structure)
domain: CONTROL PLANE — governance/candidates/, so registering this moves no candidate hash
objective: reactivate the scientific laboratory after DEC-006 closure, keeping governance
  decision · durable registration · subsequent implementation separate
---

# Lab reactivation — L2 suspension + lease ratification

> 🔴 **This is a package that REQUIRES a decision, not a decision taken.** Every choice field
> below is deliberately unfilled. Registering it as an open governance object is the whole of
> what has been done.
>
> **PROVENANCE.** Structure composed by the operator; filled from measurement by the
> Orchestrator; materialized by Plan, who re-verified §2.1 at source. Relayed, not originated.
> **If the operator states this directly, theirs is authoritative over this file.**

## DECISION 1 — L2 suspension

```
OPTION A   FULL L2 RESUMPTION
           the perimeter previously defined; already-authorised activity resumes

OPTION B   SCOPED L2 RESUMPTION
           revoked only for a declared scope; every exclusion stays explicitly suspended;
           nothing outside the scope is implicitly reactivated
```

**The final decision must declare: authorised scope · excluded scope · decision owner.**

### 1.1 · Capability state, as it stands

| Capability | State |
|---|---|
| batch dry-run (GATE 0/2/4 + restore) | restore path still infeasible under root-clean |
| snapshot restore | tested in scratch — **FAILED set equality** |
| messaging + broadcast with receipts | L1 criterion met; **the broadcast half never exercised** |
| lease acquisition and renewal | gated on DECISION 2 |
| task assignment by contract | requires authority not held |

### 1.2 · 🔴 The fact that did not exist yesterday

`DEC-006` acceptance criterion 4, registered 2026-08-18, states that `restore()` **must remove
non-snapshot files** and that post-restore state **must equal pre-snapshot state exactly,
including the absence of files**. The shipped implementation does not — read at source by both
actors: `restore()` iterates a fixed list, copies, and removes nothing.

**Therefore promoting `snapshot restore` to `VERIFIED` under a full resumption would attest a
capability whose implementation is known — in a record registered hours earlier — to fail an
acceptance criterion.**

Stated as a fact, not an argument for either option. **It is what whichever option is chosen
has to survive.**

## DECISION 2 — Lease ratification

Three minimum clauses, each of which the final decision must declare:

```
1  RISK PERIMETER         area covered · actions permitted · actions out of scope
2  COMPENSATING DETECTOR  what compensates the residual risk · where recorded · who verifies
3  SUNSET / MIGRATION     duration or validity condition · migration criterion · closing event
```

### 2.1 · Clause 1 — the perimeter is genuinely open in the frozen text

Verified by Plan at source, not relayed:

```
annex_h_authority_matrix.md:33   | CANONICAL_BATCH_COMMIT | Orchestrator (unico, lease ACTIVE) |
                                 ← the ONLY occurrence of the lease in the entire annex
GOVERNANCE_v3.1.1.md:182         "L'autorità deriva dal ruolo esplicitamente assegnato e,
                                  per Orchestrator, dal LEASE ACTIVE."
```

- **Narrow reading** — the lease gates the canonical batch only. H.1 supports it **by
  enumeration**.
- **Broad reading** — the lease is the source of all Orchestrator authority: task assignment,
  Ladder level, `HUMAN_REQUIRED` classification, challenge adjudication. §8 supports it **by
  derivation**.

**Plan's measurement, offered as evidence bearing on the choice and NOT as a resolution.**
The lease appears in exactly two *operative* places in the frozen text, and both are
batch-scoped:

| Site | Scope |
|---|---|
| `annex_h:33` | `CANONICAL_BATCH_COMMIT` |
| `GOVERNANCE:238` | `GATE 0` — *"Root dirty → NO BATCH"* |

§8:182 is the only generalising sentence, and **its context is contrastive**: it sits in a
blockquote whose subject is that *position in the root confers no authority* (§0.2). It is
answering *"where does authority come from"* — refuting **root-presence** as a source — rather
than enumerating **what the lease unlocks**. Source versus extent are different questions, and
only the first is what that sentence is arguing about.

**This does not resolve the ambiguity and is not intended to.** It is recorded because
`DEC-006` has just demonstrated what an implicit clause-scope reading costs, and because the
same signature — a reading accurate about a claim the sentence does not make — has now
occurred at byte, index, row, object, tool and clause scale in this record.

### 2.2 · Clause 2 — the residual risk is precisely identifiable

`annex_i_bootstrap_deployment.md`, I.3, verbatim:

```
FAILURE:    due sessioni leggono STALE quasi simultaneamente e tentano entrambe la
            reacquisition (nessun CAS)
DETECTION:  doppio record sulla stessa successione → alla scrittura o alla riconciliazione;
            GATE 0 blocca i batch
```

A lease in `deployment/local_instance.md` is gitignored and does not propagate to worktrees,
so **no second actor can observe a double record.**

**The detector I.3 specifies is removed, not weakened.** That is what clause 2 must
compensate, stated at that width. A compensating detector that is merely *different* does not
discharge it; it has to be one another actor can actually read.

### 2.3 · Clause 3 — the closing event already exists

`ORCHWT` is the definitive solution: it gives the Orchestrator a worktree and removes the
reason the lease needs a gitignored home at all. **Its execution is the natural closing
event.** `ORCHWT` is currently `DEFERRED` behind `HASHDET` (`HA-4`).

Recorded consequence: a sunset written against `ORCHWT` inherits `HASHDET`'s execution as its
own precondition, and `HASHDET` cannot execute while `GATE 0` lacks a lease. **A sunset
condition that depends on the thing the lease exists to unblock needs that circularity stated
in the decision, not discovered after it.**

## NOT AUTHORIZED

No batch · no code change · no `main` movement · no implementation candidate opened · no
capability state change · no `VERIFIED`/`DEMONSTRATED` promotion.

**Sequence: decision → durable registration → implementation authorised separately afterwards.**

## Current state, unchanged by this registration

```
L2                   SUSPENDED — no scope declared
ORCHESTRATOR_LEASE   NOT RATIFIED — no perimeter declared
capabilities         21 of 21 UNVERIFIED — nothing promoted
main                 908197ba62a064546f17c9c277ff497ffc753656
HASHDET · P51C9 · ORCHWT    c85acdb2… · f325bd9d… · 280dc497… — unchanged
```

---

---

# RESOLVED — 2026-08-18 · `STATUS: DECISION RESOLVED`

## DECISION 1 — L2 SUSPENSION

```
CHOSEN:            RESUMED, PER-CAPABILITY, WITH DECLARED EXCLUSIONS

AUTHORISED_SCOPE:  messaging incl. the never-exercised broadcast branch · Plan registry
                   validation · Mirror micro-review · Scientist A/B/C validator run + Auto
                   Mode + worktree-confinement declaration · Orchestrator GATE 0/2 dry-run on
                   scratch, no commit

EXCLUDED_SCOPE:    snapshot restore → BLOCKED_BY_DEC006_CRITERION_4 — the current
                   implementation fails post-restore set equality because it does not remove
                   non-snapshot files. Not promotable · no exception · no provisional
                   promotion. The fix requires a governed candidate derived from DEC-006.
                   lease acquisition/renewal → SUBORDINATE to DECISION 2/3.
                   Still excluded: batch · canonical changes · main · current files · HASHDET
                   execution — GATE constraints, not L2 constraints.

PROMOTION:         UNVERIFIED → VERIFIED authorized under the DEC-4 interim ruling. Every
                   promotion backed by observed evidence. Orchestrator self-attested
                   capabilities must carry the mitigation: outcome observable by the Operator.

DECISION_OWNER:    Operator — 2026-08-18
```

## DECISION 2 — LEASE SCOPE

```
CHOSEN:            NARROW — the lease authorizes CANONICAL_BATCH_COMMIT and nothing else.
                   H.1's enumeration is the adopted reading.

DERIVATION:        every other Orchestrator authority derives from role contract + completed
                   Annex I registration + governance hierarchy. The lease is NOT an automatic
                   source of task assignment, HUMAN_REQUIRED classification, challenge
                   adjudication, Ladder levels, governance change or process override.
                   A broad reading requires a separate governance decision.

DECISION_OWNER:    Operator — 2026-08-18
```

## DECISION 3 — LEASE HOME

```
CHOSEN:                 deployment/local_instance.md — RATIFIED AS INTERIM

RISK_PERIMETER:         gitignored, so cross-worktree visibility is reduced and I.3's original
                        cross-checkout double-record DETECTION is removed. Residual risk
                        declared minimal, not nil — one machine, one root checkout,
                        VISIBLE_VSCODE.

COMPENSATING_DETECTOR:  MANDATORY. At every lease acquisition, renewal and GATE 0, Orchestrator
                        prints the full lease content in chat — holder, SESSION_REF,
                        timestamps, STATUS. The missing cross-actor observer is replaced by the
                        Operator, who remains the recovery arbiter under I.3.
                        Acquisition/renewal receipts to be durably recorded once a committable
                        home exists.

SUNSET_MIGRATION:       ORCHWT execution. The lease then migrates to a tracked file in the
                        Orchestrator worktree, becomes readable from every checkout via git,
                        and I.3's detector is restored. No implicit extension.

DECISION_OWNER:         Operator — 2026-08-18
```

**Note on §2.3's recorded circularity.** The sunset is `ORCHWT` execution; `ORCHWT` is
`DEFERRED` behind `HASHDET`; `HASHDET` needs `GATE 0`, which needs the lease. The decision
adopts that sunset with *"no implicit extension"*, which makes the circularity a live term of
the ratification rather than an oversight. Recorded, not reopened.

---

# L2 PLAN — registered before any smoke test runs

21 capabilities. Outcomes: `VERIFIED` · `FAILED` · `BLOCKED_BY_DEC006_CRITERION_4` ·
`SUBORDINATE`.

## Orchestrator (5) — all self-attested, all carrying the observability mitigation

| # | Capability | Expected | Basis |
|---|---|---|---|
| O1 | Batch dry-run: snapshot + LINT, no commit | **BLOCKED_BY_DEC006_C4** | its criterion is *"exercises GATE 0/2/4 **and the restore path**"*; the restore path is blocked, so the capability as declared cannot reach VERIFIED. GATE 0/2 exercised on scratch = partial evidence, not promotion |
| O2 | Snapshot restore | **BLOCKED_BY_DEC006_C4** | operator-declared |
| O3 | Messaging + broadcast with receipts | **VERIFIED** expected | L1 met the stated criterion 3/3 with observed `from`; the broadcast branch is the missing half and is now authorized |
| O4 | Lease acquisition and renewal | **SUBORDINATE** | see flag |
| O5 | Task assignment by contract | **SUBORDINATE** | needs an issued contract + ACK + CLAIM; under DECISION 2 this authority derives from completed Annex I registration, at step 8 of 10 |

> 🔴 **Flag on O4, raised by the Orchestrator and not resolved by inference.** DECISION 1 made
> it *"testable only after lease ratification"*, and DECISION 3 ratifies — **but the
> authorized-now list does not contain lease acquisition. A removed blocker is not an
> authorization.** Inferring one would be exactly the convenient reading that the sequence
> *decision → registration → execution* exists to prevent. `SUBORDINATE` pending explicit
> authorization.

## Plan (6)

| # | Capability | Expected | Basis |
|---|---|---|---|
| P1 | Registry / structural validation | 🔴 **SUBORDINATE — precondition unmet** | see correction below |
| P2 | Messaging with ACK discipline | **VERIFIED** expected | authorized |
| P3 | Write within own worktree only | SUBORDINATE | not in the authorized list. Observed evidence exists in production; that is material for a promoter, not a promotion |
| P4 | WORK_COMMIT at milestone granularity | SUBORDINATE | as P3 |
| P5 | Candidate manifest incl. `CANDIDATE_CONTENT_HASH` | SUBORDINATE | as P3 — heavily exercised across HASHDET/P51C9/ORCHWT |
| P6 | Fingerprint composition | SUBORDINATE | as P3. Its contract line remains stale (C-8), unfixable without a CORE change |

> 🔴 **Plan's correction to its own row — P1 cannot be `VERIFIED` expected.** The plan lists
> P1 as explicitly authorized and therefore expected to pass. **Its object does not exist.**
> Measured here: `runtime/` is absent, and no file carries the Agent Card row schema as data —
> the registry **instance** left with `EVAC-20260817-001`, and only the schema (Annex I.4)
> remains. This is the same finding recorded in `DEC-20260817-006-L2-SCOPE.md` §1 and it was
> not carried into this plan.
>
> **The correct expected outcome is `SUBORDINATE — precondition unmet (no registry
> instance)`, not `VERIFIED`, and not `FAILED`** — by the plan's own principle for Scientists
> A/B: *a capability that could not be attempted has not failed*. The principle was applied to
> two other actors and missed on mine.
>
> **Consequence for the aggregate: 8 expected VERIFIED becomes 7.**

## Mirror (4)

| # | Capability | Expected | Basis |
|---|---|---|---|
| M1 | Micro-review under Annex C.2 | **VERIFIED** expected | explicitly authorized |
| M2 | Messaging with ACK discipline | **VERIFIED** expected | authorized |
| M3 | Read-only access across durable state | SUBORDINATE | not listed; exercised throughout |
| M4 | Event ledger analysis | **BLOCKED — different cause** | `ledger/events/` does not exist. **Verified by Plan: absent.** P7 chose the design and recorded the writer as a debt. Blocked by a missing writer, not by criterion 4, and filed under its own label |

## Scientist A/B/C (6 each)

| # | Capability | Expected |
|---|---|---|
| S1 | Full-text read producing a receipt | SUBORDINATE — scientific work, not authorized |
| S2 | Work manifest with verbatim locators | **VERIFIED** expected — *"validator run"* |
| S3 | Worktree confinement | **VERIFIED** expected — authorized as a declaration |
| S4 | Auto Mode actually active | **VERIFIED** expected |
| S5 | WORK_COMMIT at milestone granularity | SUBORDINATE — not listed |
| S6 | Messaging with ACK discipline | **VERIFIED** expected |

> 🔴 **Precondition failure, measured — it changes the plan for two of three Scientists.**
> `BY-REPORT (ORCH)`:
> ```
> lettore     NOT REGISTERED · 136 behind main · roles/scientist.md ABSENT
> lettore-b   NOT REGISTERED · 138 behind main · roles/scientist.md ABSENT
> lettore-c   REGISTERED     · 0 behind        · roles/scientist.md present
> ```
> The decision authorizes *"Scientist A/B/C"*, but **A and B cannot run any smoke test**:
> unregistered, no governance in their worktrees, and unable to read the contract declaring the
> capabilities being tested. All six → **`SUBORDINATE` — precondition G1 unmet (sync +
> registration)**, not `FAILED`. Only **scientist-c** can execute S2/S3/S4/S6 today.
>
> `PRIMARY (PLAN)`: `roles/scientist.md` **is** present at this HEAD, consistent with A and B
> being 136–138 commits behind — `roles/` was materialized recently.

### 🔴 P1's cause — the fifth evacuation cost, and it is of a different kind

`BY-REPORT (ORCH)` — the registry instance is missing because it was evacuated:
`EVAC-20260817-001` files 1 and 2, now at
`~/Desktop/legend-evacuation-20260817/runtime/{agent_card_registry.md, runtime_inventory.md}`.
`PRIMARY (PLAN)`: no tracked registry instance exists on any branch; only the I.4 schema.

**The first four costs were things nobody listed. This one was listed — and accepted on a
condition that has since expired.** The manifest, verbatim:

> *"Moving 1 and 2 out of the repository is a real cost and is accepted only because the
> laboratory is stopped: lease ABSENT, L2 SUSPENDED, task contracts 0, no batches pending. No
> actor is working, none is rehydrating, and no assignment depends on a capability status."*

**L2 is no longer suspended.** The condition under which the cost was accepted no longer holds,
and the first thing the resumed L2 asks for is the artifact that left under it. The manifest
even names the mechanism — *"the condition is the laboratory is stopped, not evacuation is a
normal tool"* — **which is the sentence that should have fired when the lab restarted, and
fired for neither actor.**

**Plan's addition: this is the fourth instance today of one structural defect.** A condition
written in prose, with no mechanism to detect its own expiry:

| Requirement | Its detector |
|---|---|
| I.3 `DETECTION` — *"doppio record sulla stessa successione"* | **removed** by a gitignored home |
| Phase 3 — *"Without a complete snapshot: ABORT"* | **cannot fire** — `snapshot()` returns 0 |
| Transmission rule — *"any free reformulation is a clause-loss point with no diff"* | **none, until a digest was pinned today** |
| Evacuation manifest — *"accepted only because the laboratory is stopped"* | **none — nothing watches the condition** |

Three of the four were repaired or flagged only because someone read the text against reality
by hand. **This system repeatedly states conditions in prose and then relies on attention to
notice when they expire** — and today's record is largely a catalogue of attention at its best
missing things anyway.

**OPERATOR DECISION REQUIRED — recorded, not taken.** Three routes, and neither actor may
choose:

1. re-create the registry instance in-repo
2. return files 1 and 2 early, ahead of the manifest's `ORCHWT`-bound return plan
3. accept `P1 SUBORDINATE` until `ORCHWT` executes

**Note that route 3 joins the sunset circularity already recorded**: P1's precondition and the
lease's sunset now resolve at the same event, `ORCHWT` execution — which is `DEFERRED` behind
`HASHDET`, which needs the lease. Choosing 3 adds a second thing waiting on that knot.

## Aggregate expected outcome — corrected

```
VERIFIED expected      7    O3 · P2 · M1 · M2 · scientist-c S2/S3/S4/S6
                            (was 8; P1 removed — precondition unmet)
BLOCKED_BY_DEC006_C4   2    O1 · O2
BLOCKED, other cause   1    M4 — missing event-ledger writer
SUBORDINATE            remainder, incl. all 12 A/B capabilities and P1
```

**Of 21, at most 7 can move today, and none is a capability `GATE 4` depends on.**

---

# L2 PLAN ADDENDUM — 2026-08-18 · three operator resolutions

## 1 · P1 — `SUBORDINATE` confirmed, until `ORCHWT` execution

Files 1–2 return per the manifest with SHA-256 verification. **Neither registry recreation nor
early return: a second instance would be a double source of truth.** Routes 1 and 2 of the
three recorded above are declined; route 3 is chosen.

**Interim home for L2 outcomes.** Every outcome — `VERIFIED` / `FAILED` / `BLOCKED` /
`SUBORDINATE`, with evidence — is durably recorded in Plan's decision record / ledger and
transferred into the registry when it returns.

> 🔴 **No outcome lives only in chat.** Until an outcome is in this record, it has not
> happened.

**Plan's note on the dependency this creates.** This makes one actor the sole durable home for
every L2 outcome, and that actor is the one holding a worktree. It is the correct arrangement
today — the Orchestrator has no writable durable location, which is the fourth evacuation cost
— but it is a **single point of recording**, and it is worth naming rather than discovering.
It resolves at the same event as everything else: `ORCHWT`.

## 2 · O4 — **AUTHORIZED**

The lease acquisition/renewal smoke test is explicitly authorized, in the home ratified by
DECISION 3, with the compensating detector active **from the first act**: full lease content
printed in chat at acquisition.

**The operator states the flag was correct and this is the authorization that was missing.**
The flag read: *"a removed blocker is not an authorization."* It was raised by the Orchestrator
against its own capability, and it was right.

## 3 · Scientist A/B — 12 rows stay `SUBORDINATE`, precondition G1

*"Sync + rehydration + registration for A/B"* is scheduled as a named post-`ORCHWT` activity,
with an obligation to declare any residual C-2 state at rehydration. **It does not gate the
`HASHDET` → `P51C9` → `ORCHWT` chain.**

## Convergence, recorded by the operator as a live term

Lease sunset · P1's precondition · evacuated-file return — **all three land on `ORCHWT`
execution**, which reinforces the execution order already decided rather than competing with
it.

---

# Pre-execution statements — recorded BEFORE any test runs

## Who executes what

Of the eight rows, **only O3 and O4 are the Orchestrator's.** P2 is Plan's, M1/M2 are
Mirror's, S2/S3/S4/S6 are scientist-c's.

L2 is conducted under **`I.2 step 8`**, which assigns L1/L2 conduct to the bootstrap
controller — **not as task assignment**, since O5 is `SUBORDINATE` and DECISION 2 explicitly
denies the lease as a source of task-assignment authority. Same basis on which L1 was
conducted.

**Recorded so that no later reader construes those messages as contracts.**

## O4's end state — stated before acquisition, not after

The criterion is *"acquire, renew by heartbeat, observe expiry to STALE"*. **Executed
literally, the sequence ends with a `STALE` lease, not an `ACTIVE` one.**

Therefore the smoke test:

- **does not** leave an `ACTIVE` lease behind
- **does not** thereby complete bootstrap step 9

**If the operator intended otherwise, this is the moment to say so** — after acquisition it is
a state to unwind rather than a reading to correct.

**Plan concurs with the reading and records why it matters structurally:** a capability test
that silently left the tester as `ACTIVE_ORCHESTRATOR` would be a smoke test with a governance
side effect, and `GATE 0`'s lease condition would then have been satisfied by an act whose
stated purpose was to measure, not to acquire. Keeping the two apart is what makes the later
lease acquisition a decision rather than a residue.

## Execution precondition

**Execution waits on Plan's confirmation of registration.** That confirmation completes a
precondition the operator set; **it is not an authorization, which is the operator's and is
already given above.**

---

---

# L2 OUTCOMES — the interim home · opened 2026-08-18

Recorded one per row, with evidence. **No outcome lives only in chat.** `FAILED` and `BLOCKED`
rows are recorded at the same weight as `VERIFIED` ones.

Conduct basis: `I.2 step 8`, bootstrap-controller conduct. **Not task assignment.**

## P2 — messaging with ACK discipline · **NOT VERIFIED — criterion partially exercised**

`PRIMARY (PLAN)` — self-reported, and reported against the criterion as written rather than
against what was convenient.

Criterion, `roles/plan.md:72`: *"L1 ping, envelope fields, `from` copied verbatim"*.
Plus B.3: *"ACK obbligatorio su `STATE_CHANGE: yes` entro timeout; assente → reinvio (dedup via
MESSAGE_ID); secondo fallimento → BLOCKER."*

| Component | Outcome | Evidence |
|---|---|---|
| L1 ping | met | L1 ping received and answered with an observed `from` |
| envelope fields | met | `MESSAGE_ID` · `TYPE` · `STATE_CHANGE` · `IN_REPLY_TO` on every message, `PLAN-20260817-011` → `PLAN-20260818-026`, 16 consecutive |
| **`from` copied verbatim** | 🔴 **not exercised as stated** | every send addressed `legend-public-cf` — the **name**, not the `from` attribute `uds:/tmp/cc-socks/12279.sock`. Delivery succeeded, which is not the same as meeting the criterion |
| **B.3 ACK on `STATE_CHANGE: yes`** | 🔴 **never exercised** | messages carrying `STATE_CHANGE: yes` were sent (`-015`, `-024`, `-026`) and **no explicit ACK was ever sent or received** in either direction. Replies arrived, but a reply is not an ACK, and B.3 names ACK as its mechanism |

**Outcome: `NOT VERIFIED`.** Not `FAILED` — nothing was tried and found wanting. Not `BLOCKED`
— nothing prevents it; both components are exercisable today. **The criterion has three named
components plus B.3's mechanism, and two of the four were never performed as specified.**

**Recorded because the alternative was available and worse.** Sixteen messages with correct
envelopes and successful delivery would read as a passing row to anyone not checking the
criterion word by word. *Delivery succeeded* and *the criterion was met* are different claims —
which is the same distinction this record has been enforcing against other actors all week,
and the first time it lands on Plan's own capability.

## O4 — lease acquisition/renewal · **IN PROGRESS — no outcome reported**

`BY-REPORT (ORCH)`. ACQUIRE step complete. Home `deployment/local_instance.md`, gitignored at
`.gitignore:49`; root reported clean after the write, 0 entries. Compensating detector fired at
the first act as DECISION 3 requires, full content printed in chat:

```
LEASE:
  ACTOR_ID:            orchestrator
  SESSION_REF:         legend-public-cf
  GOVERNANCE_VERSION:  3.1.1
  ROOT_HEAD:           908197ba62a064546f17c9c277ff497ffc753656
  ACTIVATED_AT:        2026-08-18T09:36:22Z
  LAST_RENEWED:        2026-08-18T09:36:22Z
  EXPIRES_AT:          2026-08-18T09:40:22Z
  STATUS:              ACTIVE
```

Expiry deliberately short so the terminal `STALE` transition is observable inside the session.
**Renewal and expiry observation outstanding; the row is incomplete and no outcome is claimed.**

Consistent with the pre-execution statement: the sequence ends at `STALE`, so this leaves no
`ACTIVE` lease and does not complete bootstrap step 9.

## O3 — messaging + broadcast with receipts · **BLOCKED — no runtime broadcast primitive**

`BY-REPORT (ORCH)`. First half met at L1: three pings, three replies, three receipts, every
`from` observed rather than derived. Broadcast half **probed rather than inferred**:

```
to: "evidence-index-59, mirror-9c, lettore-c-b2"
→ {"success": false, "message": "No agent named '…' is reachable."}
```

The runtime resolves the list as a single agent name. **There is no broadcast primitive.**

`BLOCKED`, not `FAILED` — one of the capability's two named components has no primitive to
exercise. **Same category as M4's missing writer; a different cause from O1/O2, and it does not
carry the criterion-4 label.**

### 🔴 Finding beyond the row — a permanently unverifiable capability

`roles/orchestrator.md` declares *"Messaging + broadcast with receipts"*. **On this runtime that
capability can never reach `VERIFIED`** without either a broadcast primitive appearing or the
contract being amended. Amending it is a content-domain change and is nobody's to make here.

Recorded because **a capability that is unverifiable by construction should be visible as
such**, rather than sitting at `UNVERIFIED` looking like it is merely waiting its turn. The
roster cannot distinguish *not yet tested* from *cannot be tested*, and that is the same
flattening already recorded for the four distinct `UNVERIFIED` reasons.

## 🔴 One capability name, four criteria — and the weakest is the one two rows will pass on

`PRIMARY (PLAN)` — all four role contracts read at source. The Orchestrator raised the
asymmetry between its row and Plan's; measuring all four shows it is **systematic, not a
quirk of one table cell**.

| Role | Capability **name** | Criterion **as written** |
|---|---|---|
| Orchestrator `:69` | Messaging + **broadcast** with receipts | *"L1 ping to every registered actor"* |
| Plan `:72` | Messaging **with ACK discipline** | *"L1 ping, envelope fields, `from` copied verbatim"* |
| Mirror `:75` | Messaging **with ACK discipline** | *"L1 ping"* |
| Scientist `:84` | Messaging **with ACK discipline** | *"L1 ping"* |

**Three roles carry the identical capability name and three different criteria. Not one of the
four criteria mentions ACK** — including the three whose capability is *named* for it.

**Consequence for this L2 run, and it reaches the aggregate.** `M2` and scientist-c's `S6` are
both in the expected-`VERIFIED` set, and both would pass on *"L1 ping"* — a criterion that
omits the mechanism the capability is named after. **Promoting them would attest ACK discipline
on evidence that measured a ping.**

**And B.3 was never exercised by anyone.** Verified against this exchange: five Plan messages
carried `STATE_CHANGE: yes` (`-015`, `-022`, `-024`, `-026`, `-027`); none was ACKed until
`-027`/`ORCH-004`, the pair sent *after* the defect was found. B.3 is unconditional —
*"assente → reinvio; secondo fallimento → BLOCKER"* — so by the letter several messages were
owed a resend and a BLOCKER, and neither happened **because nothing was counting.**

**The structural defect, stated at the width the evidence supports.** The roster already cannot
distinguish four kinds of `UNVERIFIED`. It equally cannot distinguish **`criterion met`** from
**`criterion weak enough to be met`** — and here the weak criterion is not an accident of one
row: it is the version *three of four* contracts carry.

This is the record's recurring signature at criterion scale: **the name claims ACK discipline,
the criterion measures a ping.** Accurate measurement, wrong noun — after bytes, indices, rows,
objects, tools and clauses.

**Plan does not adjust `M2` or `S6`.** They are not Plan's rows, the criteria are content
domain, and rewriting a criterion to make a promotion harder is as much an unauthorized
amendment as rewriting one to make it easier. **Recorded for the promoter and for the
operator**, before the promotions rather than after — which is the only point at which it costs
nothing.

## O4 — RENEW step complete · row still open

`BY-REPORT (ORCH)`. Heartbeat at `2026-08-18T09:38:25Z`, inside the window; detector fired at
renewal as DECISION 3 requires.

```
LEASE:  ACTOR_ID orchestrator · SESSION_REF legend-public-cf · GOVERNANCE_VERSION 3.1.1
        ROOT_HEAD 908197ba62a064546f17c9c277ff497ffc753656
        ACTIVATED_AT 2026-08-18T09:36:22Z · LAST_RENEWED 2026-08-18T09:38:25Z
        EXPIRES_AT 2026-08-18T09:40:25Z · STATUS ACTIVE
```

Renewal performed **inside** the window deliberately: a renewal after expiry is a
**reacquisition**, which I.3 permits only on `STALE`/`RELEASED` with a recorded succession — a
different act from the one this row measures.

**EXPIRY in progress, real time, not simulated.** No `STALE` is being written into the record
and called observed: *"that would be declaring the transition rather than watching it, which is
the unperturbed-restore defect in another costume."* **No outcome claimed for O4 until the
clock passes it.**

## O4 — **VERIFIED**, and its own finding is larger than the row

`BY-REPORT (ORCH)`. ACQUIRE → RENEW → expiry observed in real time, detector fired at every
act as DECISION 3 requires. **The only `VERIFIED` in this run, and it is self-attested** — its
mitigation is real rather than formal, since the full lease was printed at each act and every
claim in it is operator-checkable.

> 🔴 **At 29 seconds past `EXPIRES_AT` the record still read `STATUS: ACTIVE`, and nothing
> moved it.** The transition was written by hand, and the Orchestrator said so — *"a `STALE`
> appearing with no author is the same defect one layer up."*

**`STATUS` is a transitional value with no transition owner and no detector, inside the
artifact `GATE 0` tests.** So `GATE 0` can read `ACTIVE` on a lease that expired hours earlier,
and pass.

**Plan's addition — this bears directly on DECISION 3's compensating detector.** The detector
prints the full lease content, which includes **both** `STATUS` and `EXPIRES_AT`. The
contradiction is therefore *visible* to a reader who compares the two fields — **but nothing
compares them.** The detector is a **display, not a check**. It supplies the raw material for
the observation and leaves the observation to attention.

That is the **fifth** instance of one structural defect in this record — a requirement or
condition with no mechanism to detect its own violation, after I.3's removed detection, Phase
3's unfireable `ABORT`, the transmission rule's missing diff, and the evacuation manifest's
unwatched condition. **This one is inside the lease that DECISION 3 ratified hours ago**, and
it is the artifact `GATE 0` consults.

## M2 · S6 — **`CRITERION_MET / NAME_NOT_DELIVERED`**, not promoted

`BY-REPORT (ORCH)`, and the decision is the Orchestrator's under DEC-4. Promoting them would
attest *ACK discipline* on evidence that measured *a ping*, against an operator constraint that
every promotion be supported by observed evidence.

**No criterion was touched.** Declining to transition is inside DEC-4; amending the cell is
not, and the cells are content domain.

**The same treatment applied three times, which is the only reason it is trustworthy:** `O3`
(criterion met, name says broadcast, no primitive → `BLOCKED`, narrow criterion refused as an
excuse) · `M1` (criterion met six times, name says Annex C.2, seven of thirteen records lack it
→ Mirror proposed `CRITERION_MET / FORMAT_NOT_UNIFORM` **against itself**) · now `M2`/`S6`.
Promoting these two after refusing its own would have made the inconsistency the finding.

## Aggregate — **collapsed from 7 expected to 1 actual**

```
O4   VERIFIED                              the only one · self-attested · mitigation real
O3   BLOCKED — no runtime broadcast primitive
P1   SUBORDINATE — no registry instance (EVAC-20260817-001)
P2   NOT VERIFIED — self-reported against its own stricter criterion
M1   CRITERION_MET / FORMAT_NOT_UNIFORM    Mirror, against itself
M2   CRITERION_MET / NAME_NOT_DELIVERED
M3   SUBORDINATE
M4   BLOCKED — no event-ledger writer
     scientist-c S2/S3/S4/S6 outstanding
```

**One of seven, and it is the row whose promoter is also its subject.**

**What that number means, stated so it is not misread.** It is not evidence that the actors are
incapable — every one of these rows was exercised, and most of the work they describe has been
performed repeatedly in production this week. It is evidence that **the contracts, the
criteria, the tooling and the roster do not yet measure what they claim to measure**. Four of
the eight rows fail for a reason discovered *during* this run rather than known before it, and
three of those four were raised by the actor against its own row.

---

# L2 RUN — FINAL OUTCOMES · closed 2026-08-18

```
O3  messaging + broadcast      BLOCKED — no runtime broadcast primitive
O4  lease acquire/renew/stale  VERIFIED — self-attested, operator-observable
P1  registry validation        SUBORDINATE — object evacuated under EVAC-20260817-001
P2  messaging ACK discipline   NOT VERIFIED — criterion partially exercised (Plan, self-reported)
M1  micro-review Annex C.2     CRITERION_MET / FORMAT_NOT_UNIFORM (Mirror, self-reported)
M2  messaging ACK discipline   CRITERION_MET / NAME_NOT_DELIVERED
M3  read-only durable state    SUBORDINATE
M4  event ledger analysis      BLOCKED — no writer
S2  work manifest validator    VERIFIED — 60/64 STRICT PASS, 4 legacy schema-1
S3  worktree confinement       UNEXERCISED, WITH CONTRARY EVIDENCE (scientist-c, self-reported)
S4  Auto Mode active           VERIFIED
S6  messaging ACK discipline   CRITERION_MET / NAME_NOT_DELIVERED

VERIFIED 3 of 12 attempted — O4 · S2 · S4.   Expected 7.
Self-reported against their own row: O3 · P2 · M1 · S3 — all four.
```

## 🔴 The unification — one absence, three symptoms

Mirror's finding, **verified by Plan at source.** `annex_j_runtime_control_plane.md:47`, J.1's
minimum event types, names verbatim among others:

```
TASK_ACKED … LEASE_ACQUIRED, LEASE_STALE
```

**The absent event ledger is the missing detector for three of this run's findings, not one:**

| Symptom | Event that would have caught it |
|---|---|
| P2 / M2 / S6 — B.3 ACK never exercised, no resend, no BLOCKER | `TASK_ACKED` |
| M4 — its own blocker | the ledger itself |
| O4 — lease sat `ACTIVE` 29s past expiry with nothing moving it | `LEASE_ACQUIRED` · `LEASE_STALE` |

**P7 recorded the writer as a debt.** *"Nobody was counting"* is therefore not inattention — it
is **the missing mechanism doing exactly what its absence predicts.**

Measured alongside: **zero durable hits** across all branches for every `STATE_CHANGE: yes`
message ID in this exchange and for the first ACK. **No message log exists anywhere**, so a
false claim and its true correction are unverifiable by the same reader for the same reason.

## The detector finding, completed — and it is worse than "a display"

Plan found the DECISION 3 detector prints both `STATUS` and `EXPIRES_AT` but nothing compares
them. **Measured, and confirmed by Plan independently:**

```
code referencing EXPIRES_AT anywhere in the repository:   0
```

**Nothing compares them because nothing reads `EXPIRES_AT` at all.**

Mirror's third point closes it: under C-9 §4.1 `STATUS` is **`DERIVED`** — a function of
`EXPIRES_AT` and the clock — and C-9's own table permits caching a derived value only *"with
its input digest — rare, and a smell"*, the normal case being computed on demand. **Nothing
moved the field because, by that classification, there was nothing to move it *by design*.**

That is a classification question and its correction is content domain. **Neither actor writes
it.**

## Closing statement on the number

**3 of 12, against 7 expected, and it will be misread.**

It is **not** evidence that the actors are incapable. Every row was exercised, and most of the
work these rows describe has been performed repeatedly in production this week — including by
the two actors whose rows did not pass.

It is evidence that **the contracts, the criteria, the tooling and the roster do not measure
what they claim to measure.** Four rows failed for reasons discovered *during* the run, and
**all four were raised by the actor against its own row**: O3 by the Orchestrator, P2 by Plan,
M1 by Mirror, S3 by scientist-c.

**A run returning seven clean promotions would have told the operator far less.**

---

# OPERATOR DIRECTIVE — 2026-08-18 · registered, transmitted by the Orchestrator

Authority is the operator's. Recorded because no decision lives only in chat.

**§1 · L2 TABLE RATIFIED.** 3 VERIFIED promoted — `O4` · `S2` · `S4`. The 9 non-promotions
ratified each with its own cause, **including the three CRITERION_MET-not-promoted**: promoting
`M2`/`S6` would have attested ACK discipline on evidence that measured a ping. The 3-of-7
collapse is registered as a finding **about the measuring apparatus, not about the actors**,
and does not block the chain.

**§2 · BOOTSTRAP STEP 9 AUTHORIZED.** Real lease acquisition, **explicitly distinct from smoke
`O4`** and to be declared as such. Interim seat per DECISION 3 unchanged; detector integral at
the first act; TTL sized to batch duration with heartbeat renewals inside the window. Sunset
remains `ORCHWT` execution.

**§3 · BINDING COMPENSATOR — the O4 finding converted into an operating rule the same day it
was measured.**

> **`STATUS` is not authoritative.** At every lease consultation — `GATE 0`, every subsequent
> gate, every renewal — the state is **derived**: print `EXPIRES_AT`, the current clock, and the
> computed verdict. Never the stored field alone. **Expiry mid-batch = immediate STOP, no
> implicit reacquisition.**

**§4 · DEGRADED FAILURE PATH.** `snapshot restore` remains `BLOCKED_BY_DEC006_CRITERION_4` →
**attended execution, operator present**. Snapshot manifest printed before execution. If the
failure path triggers: STOP after restore · set-equality against the printed manifest · manual
removal of strays **only on explicit operator confirmation in chat** · no autonomous repair.

**§5/§6 · SEQUENCE.** `GATE 0–5` with evidence → `CANONICAL_BATCH_COMMIT` of
`CAND-20260817-HASHDET` (`c85acdb2…`, BASE_HEAD `908197ba…`) → mechanical re-baseline of
`P51C9` → **STOP at delivery of the re-attestation package.** New `HUMAN_APPROVAL` lands on the
new binding.

**§7 · NOT AUTHORIZED.** `P51C9`/`ORCHWT` execution · any amendment to contracts, criteria or
rubric — **including the ACK criteria mismatch** · event-ledger creation · repair of Mirror's 7
C.2 records · governance registration of the Plan→Mirror routing constraint · any act on
scientific content. **All L2 findings remain material for post-`ORCHWT` candidates.**

## GATE 1 — proposer ≠ executor

**Plan prepared HASHDET; the Orchestrator executes it.** Plan takes no part in the execution and
does not touch `hash-determinism` while it runs.

### Plan's confirmation of the tip delta — measured read-only, no checkout

```
manifest binds BRANCH_TIP   b9af54eb   (r3 reviewed)
actual branch tip           6422e22    "HASHDET r3 manifest: record aligned, and it converges"
commits between             exactly 1
paths touched               governance/candidates/CAND-20260817-HASHDET.md  — only
classification              CONTROL_PLANE_ROOT declared at b9af54eb → identity does not move
```

**Confirmed, and not for the first time.** Already measured and recorded in
`DEC-20260817-006-L2-SCOPE.md` as `COR-20260817-GATE0-003`, where both standpoints returned
`c85acdb2…` identically and Plan's own contrary claim was withdrawn. **The executor is therefore
not relying on a single measurement of its own.**

**Plan did not recompute the hash now, deliberately.** From this worktree that requires either
checking out `hash-determinism` — which `GATE 1` forbids while execution runs — or computing
with *this* worktree's `P5`, which declares `reviews/` and would yield a **different and wrong**
value. **That is the HASHDET defect itself**, and reproducing it while verifying HASHDET would
have been the exact error the candidate exists to fix.

## Not attempted

**P1** — `SUBORDINATE` per the addendum, object left with `EVAC-20260817-001`, neither
recreation nor early return authorized. **Not attempted.**

## Not authorized

Batch · HASHDET · code · `main` · current files · existing candidates · capability state
outside the authorized smoke tests · promotion without evidence.

**Nothing has been executed.** The plan is registered; execution follows registration, per the
operator's stated sequence.
