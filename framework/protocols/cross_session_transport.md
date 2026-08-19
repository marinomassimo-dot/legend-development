---
artifact: LEGEND protocol — CROSS-SESSION TRANSPORT DISCIPLINE
protocol_id: XPORT
governance_version: 3.1.1
status: PROPOSED — binding once Mirror hostile review passes and the operator approves
normative: yes
extends: governance/annex_b_message_protocol.md — B.1 envelope, B.2 types, B.3 reliability.
  This protocol adds NO message type, NO envelope field of its own, and NO second ACK. It fills
  B.1's existing DURABLE_POINTER with a rule, and binds B.3's reliability clauses to what the
  installed runtime was measured to do.
rests_on: governance/design_records/runtime_harness_probe_20260819.md — every runtime fact
  cited here names a section of that record. Nothing here re-measures the harness.
also_references: launch/KERNEL_SPEC.md — REACHABLE/OPERATIONAL (MC-5), the five emission
  outcomes, MESSAGE_TURN_TRUNCATION, OB-3. Those classes are cited, never restated.
enforcement_mode: PROCEDURAL — see §8. No mechanism in this protocol runs between turns.
actor_scope: ACTOR-GENERIC in the semantic sense, which is the only sense in which it is true.
  No rule, no branch and no obligation in this protocol is conditioned on which actor is acting;
  every clause is stated over any actor, and it binds every actor that sends or receives a
  cross-session message. Actor, role and worktree names DO occur in this file — as measurements,
  as citations of prior art or of duties governance has already allocated, and in the status line
  above. §11.1 states the property, those three classes, and the falsifier that tests it. That
  falsifier is a deletion test, not a grep; a grep for names returns non-zero here by design.
---

# CROSS-SESSION TRANSPORT — the message notifies, the repository proves

## 0 · The one sentence, and the four it is not

```
CHAT / SendMessage           →  COORDINATION AND NOTIFICATION PLANE
DURABLE REPOSITORY ARTIFACT  →  AUTHORITATIVE PAYLOAD AND EVIDENCE PLANE
```

This is not new law. Body §21 already says *"messaggi = pointer, stato durevole decide"*, Annex
B.1 already carries a `DURABLE_POINTER` field in the envelope, and `roles/plan.md` already says
*"the message notifies, the commit is what happened."* **What has been missing is the
consequence**: nothing stated that authoritative content *must not depend for its integrity on
the body of a message*, and nothing said what happens when it does.

Four things this protocol deliberately is not:

- **not a second message protocol.** Annex B owns the envelope, the types and the ACK. This adds
  a rule about the *payload*, not a channel.
- **not a second escalation path.** A non-responsive actor is Annex B.3 → `BLOCKER` → Annex F.4
  `DIAGNOSE` → body §36.6. Unchanged, and not reproduced here.
- **not a routing protocol.** Who the current incarnation of an `ACTOR_ID` is, and how a sender
  resolves it, is **out of scope and unresolved** — §9 states the dependency explicitly rather
  than assuming it away.
- **not a claim to have measured the runtime.** Every runtime fact carries a pointer to the
  design record that measured it, and the four epistemic classes of that record travel with it.

---

## 1 · The rule

### 1.1 · What must live in a durable artifact

**AUTHORITATIVE CONTENT** is content whose integrity, completeness or exact wording is what
makes it usable. At minimum:

```
task contracts · handoffs · reviews · approvals · governance directives
benchmark specifications · scientific analysis · scientific results
substantial evidence packages · candidate manifests · learning records
```

> 🔴 **Authoritative content MUST live in a durable repository artifact, and MUST NOT depend for
> its integrity on the body of a `SendMessage`.**

The reason is measured and specific, not stylistic. Design record §8.1: on the installed runtime
one field of the message tool declares a bound the runtime enforces and another declares a bound
it does not, **with nothing in the declaration distinguishing them**. A payload whose completeness
cannot be established by its recipient is not evidence, whatever it says.

### 1.2 · The control envelope

A notification about authoritative content carries a **reference**, and the reference must be
sufficient for the recipient to find the object and prove it is the right one:

```
CONTROL ENVELOPE  (Annex B.1 fields, with DURABLE_POINTER filled per this protocol)

  MESSAGE_ID · TASK_ID · ACTOR_ID (sender identity) · FROM · TO · TYPE (Annex B.2)
  STATE_CHANGE: yes | no
  DURABLE_POINTER:
      object_id        the artifact's own identifier where it has one
      path             repository-relative, never absolute (Annex I.5)
      commit / tip     the commit or branch tip at which the object is to be read
      binding          the digest or hash the object is bound to, where one exists
                       (CANDIDATE_CONTENT_HASH, blob sha256, receipt digest, …)
      branch           where the commit lives, when it is not on `main`
  INSTRUCTION:  read the durable object in full at the named commit
```

**Naming the branch is part of the claim.** `deployment/deployment_profile.md` already states this
for status assertions — *"what actors have recorded on their own branches: `git show <branch>:<path>`
— naming the branch is part of the claim"* — and it applies identically to a pointer, because a
path without a branch is unresolvable from any other worktree.

### 1.3 · What the message body may contain

Anything that does not have to survive: a one-line statement of what happened, why the recipient
is being notified, and what it is being asked to do. If the body were lost entirely and only the
`DURABLE_POINTER` arrived, the recipient must still be able to do the right thing.

**Test for whether a body is too heavy:** delete it, leave the pointer, and ask whether the
handoff still works. If it does not, the content was authoritative and belongs in the artifact.

### 1.4 · 🔴 The depth rule — non-negotiable

> **Only the TRANSPORT REPRESENTATION may become shorter.**

Nothing in this protocol reduces, or may be cited to reduce:

```
scientific reading depth · evidence depth · evidence coverage · methods review
locator coverage · uncertainty analysis · the population any finding is measured over
```

A reading that would have been done at full depth and is done at less because a message would
have been long is a protocol violation, and the protocol it violates is this one. The artifact
absorbs the depth; the envelope carries the pointer.

---

## 2 · Message budget — structural, and no number is invented

```
LEGEND_MESSAGE_BUDGET:  NOT SET — deliberately, on measurement
```

Design record §8.1: `SendMessage.message` declares **no bound**, and none was probed, because
discovering one requires abusing the runtime and a number obtained that way would be a property
of one attempt rather than a contract. `SendMessage.summary` declares 200 and the runtime accepted
264 without complaint. So there is no honest numeric threshold to publish for the body, and the
only enforced bound in the tool — `to` at 200 characters — is one no LEGEND address approaches.

**The structural rule replaces the number:**

```
AUTHORITATIVE CONTENT  →  DURABLE ARTIFACT + CONCISE CONTROL ENVELOPE
```

The purpose is **not** token minimization. It is: avoid an avoidable runtime rejection; avoid
transporting the same content twice; keep the message control-plane sized; and put the substance
where its integrity can be verified.

**The one number this protocol carries, bound as §3 requires:**

```
VALUE                 200
UNIT                  characters, JSON string length
FIELD                 SendMessage.to
SOURCE                tool schema (DOCUMENTED) + 213-character probe rejected (OBSERVED)
VERSION_OBSERVED      2.1.232
RATIONALE             the only bound on this tool both declared AND enforced
SAFETY MARGIN         n/a — the longest ACTOR_ID in the laboratory is 11 characters
REVALIDATION TRIGGER  the sending session's runtime version differs from 2.1.232
```

If a numeric body budget is ever proposed, it binds all seven fields or it is not proposed.

---

## 3 · Version-bound runtime guarantees

> **Every guarantee in this protocol that depends on runtime behaviour is VERSION-BOUND.**

```
VERSION_OBSERVED       the runtime version of the SESSION that made the observation
SOURCE                 the official surface read, or the command run
OBSERVATION / TEST     what was seen
REVALIDATION_TRIGGER   default: the acting session's runtime version differs from VERSION_OBSERVED
```

🔴 **The version is a property of the session, never of the machine.** Design record §1 measured
four extension versions installed and at least two hosting live sessions concurrently, while
`claude --version` on `PATH` reported a third thing — the CLI, which hosts no session. An actor
establishes its own runtime version from its own process image or its own transcript's `version`
field. **A machine-level version string is not evidence about any session, including the one
reading it.**

At every bootstrap and at every `GATE 0` where a runtime guarantee is load-bearing, the acting
session observes its own version. On a difference:

```
OBSERVED  →  VERSION_CHANGED  →  REVALIDATION_REQUIRED
```

The guarantee does not become false. It becomes **unmeasured**, exactly as an Annex A.6 checkpoint
with a changed fingerprint is not wrong but is not resumable without asking. Nothing may be
assumed to survive an upgrade: not naming, not discovery scope, not size limits, not truncation,
not delivery, not resume or fork behaviour.

**A guarantee stated in this protocol without a `VERSION_OBSERVED` is a defect in this protocol.**

---

## 4 · Field-specific size and truncation

Design record §8.1 is the measurement; this is the rule that follows from it.

| field | bound | enforced? | oversize outcome | sender sees it? |
|---|---|---|---|---|
| `to` | 200 chars | **YES** — `pattern` | `REJECTED_TOO_LARGE` before the tool runs | **yes**, structured error naming the field |
| `summary` | 200 declared | **NO** — `maxLength` not applied at 264 | `TRUNCATED` (DOCUMENTED, not observed) | **no** — result identical to an in-bounds call |
| `message` | none declared | — | `UNKNOWN` | `UNKNOWN` |
| envelope / serialized request / tool result | not exposed | — | `UNKNOWN` | `UNKNOWN` |

> 🔴 **A declared schema bound may or may not be enforced, and the declaration does not say
> which.** Two constraints in the same schema, one enforced and one not. No LEGEND rule may
> assume enforcement from a declaration; enforcement is established by probe, per field, per
> version, or the field is treated as unbounded.

**Consequence for the summary field.** `summary` is a UI preview. Nothing authoritative goes in
it, because silent truncation of an unenforced bound is the worst available combination: the
sender believes it sent, the recipient sees something shorter, and no surface reports the
difference.

---

## 5 · Transport outcome taxonomy

Mapped to what the installed runtime actually returns. `OBSERVED` marks a class this session
produced; `DOCUMENTED` marks one the runtime describes; `UNOBSERVED` marks one the taxonomy needs
and this probe did not produce.

| LEGEND class | runtime evidence | status |
|---|---|---|
| `DELIVERY_ACCEPTED` | `success: true` from the message tool | DOCUMENTED |
| `REJECTED_TOO_LARGE` | `InputValidationError` naming the field and its pattern; the tool never ran | **OBSERVED** (`to`, 213 chars) |
| `TARGET_UNRESOLVED` | `{"success": false, "message": "No agent named '<x>' is reachable."}` | **OBSERVED** |
| `TARGET_STALE` | a reference read from an earlier listing no longer resolving | DOCUMENTED — *"a ref you did not just read from a listing or an error will not resolve"* |
| `DELIVERY_FAILED` | a send that neither succeeds nor resolves to one of the above | UNOBSERVED |
| `DISCOVERY_INCOMPLETE` | no completeness signal exists on either discovery surface | **structurally unavailable** — §6 |
| `DELIVERY_UNKNOWN` | any outcome the sender cannot classify into the above | the residual class, and it must stay non-empty |
| `TRUNCATED_OR_PARTIAL` | `summary` over its declared bound | DOCUMENTED, sender-invisible |
| `RECIPIENT_PROCESSING_FAILED` | see §7 — the classes exist and are KERNEL_SPEC's | MEASURED_EARLIER |
| `OTHER` | required. A taxonomy with no escape hatch gets its residue misfiled | — |

### The four boundaries, and none of them implies the next

```
SENDMESSAGE INVOKED   !=   DELIVERY ACCEPTED   !=   RECIPIENT PROCESSED   !=   HANDOFF ESTABLISHED
```

KERNEL_SPEC MC-5 already draws the second boundary and supplies its test receipt:
`REACHABLE` asserts existence, discoverability and addressability and asserts **nothing about
acceptance** — *"a refusal on arrival is silent to the sender"* — and promoting a `success: true`
into an `OPERATIONAL_PASS` is refused as `EVIDENCE_CLASS_MISMATCH: delivery is not acceptance`.
This protocol adopts that receipt verbatim and extends it one boundary further, to handoff (§8).

```
GUARANTEE_PROVIDED             a sender that classifies its outcome into the table above has a
                               name for what happened, and the two failure classes it can
                               actually observe — REJECTED_TOO_LARGE and TARGET_UNRESOLVED —
                               are structured, immediate and unambiguous
                               VERSION_OBSERVED 2.1.232
FAILURE_MODE_STILL_POSSIBLE    a send that returns success:true and is never processed; a
                               summary silently shortened; any outcome the runtime does not
                               distinguish, which lands in DELIVERY_UNKNOWN by construction
DETECTION                      the durable object and its ACK (§8). NOT the send's return value
RECOVERY                       Annex B.3 — resend with the same MESSAGE_ID (dedup), second miss
                               → BLOCKER → Annex F.4 DIAGNOSE. Unchanged, not duplicated here
```

---

## 6 · Discovery is not liveness, and neither is routability

Design record §3 and §9. Two discovery surfaces exist and they do not return the same set: the
tool excludes the caller's own session, the CLI includes it and adds `sessionId`, `cwd`, `pid`
and — under `--all` — dead rows and job ids.

```
DISCOVERED   a surface returned a row
LIVE         a process exists behind it
ROUTABLE     LEGEND has decided this incarnation is the actor's current one
```

> 🔴 **`NOT LISTED → UNKNOWN`. Never `NOT LISTED → DEAD`**, unless exhaustive discovery is an
> `OBSERVED`, version-bound guarantee for the scope in question. Neither surface signals
> completeness, truncation, or that more may exist.

And the converse, which is the one that bites: **a name that resolves is not a session that is
alive.** Design record §5 observed the name `scientist-a` still resolving under `--all` to a job
that died three days earlier, `pid: null`. Any resolution must additionally require a live pid.

**LEGEND today can measure the first two and has no mechanism for the third.** That is §9.

---

## 7 · Recipient-side processing failure

A delivery that is accepted can still fail on the far side, and the classes already exist. They
are `launch/KERNEL_SPEC.md`'s, measured, and are **cited rather than restated**:

```
PASS · TOOL_DEFERRED · TOOL_UNAVAILABLE · NOT_EMITTED · EMITTED_NOT_ARRIVED
MESSAGE_TURN_TRUNCATION   — defined by SYMPTOM: tool calls emitted → results returned, not
                            interrupted → no subsequent assistant continuation. Two observed
                            instances, different mechanisms, same shape.
```

They map into `RECIPIENT_PROCESSING_FAILED` (§5) and are not renamed. Annex F.4 already classes
truncated turns and permission prompts as **runtime failures and never insubordination**; this
protocol adds nothing to that and repeats none of it.

🔴 **Never merge `TOOL_DEFERRED` with `TOOL_UNAVAILABLE`.** The first is a latency to budget; the
second is an absent capability. Design record §3.1 observed `TOOL_DEFERRED` **in an interactive
session** — the message tool required a schema fetch before it could be called, while the
discovery tool did not. So the cost falls on the send leg, which is exactly where
`MESSAGE_TURN_TRUNCATION` was measured striking twice. A protocol that treats the send as free is
budgeting nothing at its most fragile point.

---

## 8 · Authoritative handoff — a conjunction, and enforcement is PROCEDURAL

> **`HANDOFF ESTABLISHED`** requires **all** of:

```
1  the DURABLE ARTIFACT exists at the named commit
2  its binding (hash / digest) is valid where one exists
3  exactly ONE current target was resolved for the ACTOR_ID          ← see §9, UNRESOLVED today
4  the notification returned DELIVERY_ACCEPTED
5  the recipient READ the durable object
6  the recipient produced a DURABLE ACK
```

**If any term is absent: `HANDOFF NOT ESTABLISHED`.** Sender-side success is term 4 of six.

**No durable recipient ACK → no handoff.** Annex B.3 already makes ACK mandatory on
`STATE_CHANGE: yes` and this protocol does not redefine it; what it adds is that for
authoritative content the ACK must be **durable** — a commit, a claim record, a receipt, a
checkpoint — and not only a message. Body §21's rule is the precedent: *the receipt ledger, not
the queue, decides what was read.*

```
ENFORCEMENT MODE:  PROCEDURAL

GUARANTEE_PROVIDED             a sender following this protocol cannot establish a handoff on a
                               message body alone, because terms 1, 2, 5 and 6 are all facts
                               about durable state that a message cannot manufacture. Where the
                               terms are met, the handoff is reconstructible by a third party
                               from the repository alone, with no chat
FAILURE_MODE_STILL_POSSIBLE    the sender skips the discipline entirely and puts the payload in
                               the body; the recipient ACKs without reading; term 3 cannot be
                               satisfied at all today
DETECTION                      terms 1, 2 and 6 leave durable artifacts, so their absence is
                               visible to Plan at reconciliation and to Mirror on the ledger.
                               Term 5 — "the recipient read it" — has NO detector:
                               🔴 DETECTION: NONE — ATTENTION_ONLY
RECOVERY                       Annex B.3 resend → BLOCKER → Annex F.4 DIAGNOSE; the task returns
                               to the assigner with the handoff recorded as not established
```

> 🔴 **This is procedural discipline and it is not an enforced invariant.** No validator runs at
> send time, no hook was demonstrated to fire (Phase −1, E2 `INCONCLUSIVE`, cause not
> established), and nothing runs between turns. Any document that describes this protocol in
> stronger vocabulary than the block above is violating the Annex J.0 cross-cutting rule.

---

## 9 · The dependency this protocol does not resolve, and says so

Term 3 of §8 — *exactly one current target resolved for the `ACTOR_ID`* — **cannot be satisfied
today**, and this protocol does not pretend otherwise.

Design record §6, measured on the machine as it stands: `plan` has 8 live sessions in its
worktree, `mirror` has 7, `scientist-a` and `scientist-b` have 0, and the Agent Card registry's
recorded current session for `plan` is alive, is three days old, and is not the current one.
Worktree is not a resolver: `--cwd` narrows 19 candidates to 8, not to 1.

```
ACTOR-ROUTED SEND        →  RESOLVE AT SEND TIME, against governed routing state
NEVER                    →  reuse a SESSION_REF remembered from conversation, an old handoff,
                            a prior message, memory, or stale runtime output
IF no unique target      →  ROUTING: BLOCKED. Fail closed. The handoff is not established.
NEVER elect CURRENT by   →  latest chat · last seen · most recently created · newest timestamp
                            · registration recency · last responder · last successful recipient
```

**Those five lines bind now**, because they are refusals and a refusal needs no mechanism. What
does not exist is the positive half: *governed routing state* against which to resolve. Until it
exists:

> **Actor-routed sends of authoritative content are operator-mediated.** The sender prepares the
> durable artifact and the control envelope, and the operator — who can see which chat is which —
> directs it. This is the laboratory's current practice; this protocol records it as the honest
> state rather than leaving it implicit.

`CANDIDATE B — ACTOR SESSION LIFECYCLE / ROUTING` is the successor work. §10 of the accompanying
manifest states why it is not merely *next* but **blocked on preconditions Plan may not satisfy
alone**.

---

## 10 · Acceptance tests

Every test is executable by a reviewer with the repository and the installed runtime. `T-TRANSPORT-2`
and `T-TRANSPORT-3` are run against a deliberately unresolvable target so that **no peer is
contacted**.

| # | test | expected | status at authoring |
|---|---|---|---|
| `T-TRANSPORT-1` | small control envelope, end to end | `DELIVERY_ACCEPTED`, recipient reads the object, durable ACK | **NOT RUN** — requires term 3 (§9). Cannot be run honestly today, and is recorded as unrun rather than passed |
| `T-TRANSPORT-2` | oversize `to` (213 chars) | `REJECTED_TOO_LARGE`, structured, pre-send | **PASS** — observed |
| `T-TRANSPORT-3` | oversize `summary` (264 chars) | **not** rejected; the declared bound is unenforced; the sender sees nothing | **PASS** — observed |
| `T-TRANSPORT-4` | large authoritative payload | artifact + concise reference; recipient identifies the exact object and verifies its binding | **PASS by construction** — the SCIAB canonicalization is the worked example: a 143 KB manifest handed off as `hash + base + two tips + branch`, and the binding reproduced independently three times |
| `T-TRANSPORT-5` | delivery failure | never recorded as handoff success | **PASS** — `TARGET_UNRESOLVED` observed as `success: false`; §8 makes term 4 one of six |
| `T-TRANSPORT-6` | truncation / partial delivery | cannot alter the authoritative instruction, because the artifact owns it | **PASS by construction** — §1.3's deletion test |
| `T-TRANSPORT-7` | recipient-processing failure after accepted delivery | no durable ACK → handoff not established | **PASS by construction** — §8 term 6; the failure classes are KERNEL_SPEC's, measured twice |
| `T-DEPTH-1` | the size discipline changes only the transport representation | reading depth, evidence coverage, locator coverage and uncertainty analysis are unchanged | **PASS by construction** — §1.4, and no clause of this protocol mentions any of them except to forbid their reduction |
| `T-GENERIC-1` | actor-generality — delete every actor, role, worktree and benchmark name from this file | no normative sentence changes meaning; no clause branches on `ACTOR_ID`; every remaining occurrence falls in one of §11.1's three classes | **PASS** — executed at this revision, §11.1. The inventory grep returns non-zero by design and is **not** this test |

🔴 **`T-TRANSPORT-1` is the one that matters and it is unrun.** It is recorded as `NOT RUN`
because running it requires choosing one of eight live sessions to address, and choosing one
without governed routing state is the exact defect Candidate B exists to fix. A `PASS` obtained
by picking a session would be a measurement of luck.

---

## 11 · What this protocol does not do

- does not resolve `ACTOR_ID → SESSION_REF`, and does not claim routing is operational;
- does not create a message type, an envelope field, an ACK, or an escalation path;
- does not modify Annex B, which is FROZEN;
- does not set a numeric body budget;
- does not condition any rule, branch or obligation on any actor, role, worktree or benchmark —
  §11.1 states that property, the three classes in which names do legitimately occur here, and
  the falsifier that tests it;
- does not measure the harness — it cites the design record that did;
- does not claim any enforcement the harness has not been shown to provide.

### 11.1 · The actor-generality property, and the falsifier that tests it

Revision 1 of this file asserted, in this section and in `actor_scope`, that the protocol *names*
no actor, role, worktree or benchmark. **That was false of this file at the moment it was
written**, and false in the direction that costs most: it put a checkable *absence of strings*
where the semantic property was meant, so the cheapest check available — a grep — falsifies it.
The property below is the one that was meant. It is stronger, and it survives the grep.

> **THE PROPERTY.** No rule, no branch and no obligation in this protocol is conditioned on which
> actor is acting. Every clause is stated over *any* actor, and a new actor needs no new
> transport clause.

Actor, role and worktree names occur in this file in three classes, and none of the three is a
transport rule:

| class | what the name is doing | where |
|---|---|---|
| MEASUREMENT | quoting what was observed — and an observation names its subjects | §6's dead-name example; §9's live-session counts |
| CITATION | pointing at prior art, or at a duty governance has already allocated elsewhere | §0's `roles/plan.md` quote; §8's `DETECTION` row; §9's note that the successor work exceeds one actor's authority |
| GOVERNANCE STATUS | this artifact's own standing under the framework rules that bind every artifact | the `status` line |

A role named in a CITATION carries no transport rule with it. The duty is the one governance
allocated already — body §43 and Annex G.3 for the `DETECTION` row — cited here rather than
restated, and it would bind identically if this protocol did not exist. A MEASUREMENT that names
its subjects is more checkable, not less general.

> **THE FALSIFIER — semantic, and a grep is not it.** Delete every actor, role, worktree and
> benchmark name from this file and ask whether any normative sentence changes meaning. If none
> does, the property holds. It is **falsified** by any clause of the form *if the actor is X,
> transport rule P applies, otherwise Q* — unless the difference is an authority class governance
> has already allocated, cited here and not created here.

**Why the lexical check is the wrong instrument, said here so it is not run as the right one.** A
grep for actor names returns non-zero on this file and is expected to. It would return **zero** on
a protocol that branched on `ACTOR_ID` through a variable, which is precisely the failure this
property exists to exclude. Use a grep to build the inventory; use the deletion test to decide.
