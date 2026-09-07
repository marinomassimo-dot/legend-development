---
artifact: DURABLE HANDOFF — sunset of DECISION 3 (interim lease home)
id: HANDOFF-20260818-SUNSET-DEC3
status: NOT STARTED — awaiting a Plan session with capacity
prepared_by: plan (evidence-index) — handing off, not authoring
authorized_by: operator, 2026-08-18
domain: CONTROL PLANE — governance/candidates/, so writing this moves no candidate hash
scope_rule: THE SCOPE MUST NOT BE REDUCED. The operator authorized a handoff instead of
  completion, explicitly on condition that scope is preserved. A smaller candidate is not
  available.
---

# Handoff — the `DECISION 3` sunset candidate

**Plan is handing this off, not authoring it.** The operator's instruction was *complete it, or
make a durable handoff and resume in a new Plan session **without reducing the scope***. This is
that handoff. **It is durable because a specification held only in a peer exchange dies with the
session holding it** — the operative clause registered in `DEC-20260818-007`.

**Nothing here is started. No file has been drafted. `main` is untouched at `f5b32155`.**

---

## Binding scope — A through G

### A · TRACKED LEASE HOME

Retire `deployment/local_instance.md` as the operative interim seat. Create a tracked lease home
in the Orchestrator worktree: **versioned · readable via git from every checkout · observable by
Mirror · compatible with `ONE_WRITER_PER_WORKING_DIRECTORY`**.

🔴 **The existing interim history must NOT be deleted or silently rewritten.** Five lease records
stand in it.

### B · I.3 OBSERVABILITY

Restore the cross-actor detector. Make **`VISIBILITY ≠ LIFECYCLE ENFORCEMENT`** explicit **and
operative** — *readability of the record does not demonstrate the lifecycle is correct.*

### C · LEASE LIFECYCLE

A durable, verifiable derivation using at least **`EXPIRES_AT` · `RELEASED_AT` · a terminal
state**. It must not depend on the stored `STATUS` alone, on time alone, or on an ephemeral
session script.

**Declare three things separately:**

| | |
|---|---|
| `MECHANIZED` | what is actually computed or checked |
| `OBSERVABLE` | what another actor can verify |
| `PROCEDURAL` | what still depends on discipline or human intervention |

**Treat the observed case explicitly: `LEASE EXPIRED UNUSED BETWEEN TURNS`.** A tracked home alone
does not solve it — nothing was watching.

### D · `Current instance — status` — FULL REWRITE

**No line-level corrections.** Describe the post-`ORCHWT` state a repository reader can verify:
bootstrap happened · the Orchestrator has its own worktree · the root is reserved to
`CANONICAL_BATCH_COMMIT` · scientist worktrees per verifiable state · the lease lifecycle really
exists. **Distinguish canonical state from runtime state from local surfaces.**

Avoid unnecessary counts, unverifiable facts, and future-tense phrasing for things that have
already happened.

> **Do not carry a count of how many claims in the old paragraph were false.** The number was
> offered in discussion and is not load-bearing; **the paragraph is wrong as a paragraph.**
> Reproducing the count would repeat the defect the rewrite exists to remove.

### E · P1 — RECORD THE ACTUAL RESULT

```
P1   CRITERION_MET / NAME_NOT_DELIVERED
```

**Not `VERIFIED`. Not `FAILED`. Not `SUBORDINATE`-for-missing-registry — that precondition is
resolved.** The registry instance exists, the existing criterion is met, and **the capability's
NAME promises a registry validation no instrument performs.**

Evidence, executed by Plan on 2026-08-18 in its own worktree: five validators `rc=0` —
`legend_lint` PASS (1 INFO) · `fulltext_receipts verify` 128 chained, tail anchored ·
`growth_anchors check` PASS · `public_release_gate` PASS (1 REVIEW) · `governance_fingerprint
compose --all` PASS. Registry read from `orchestrator@632ad22`: 314 lines / 30 rows;
`runtime_inventory.md` 551 lines.

### F · NEW OPEN DEBT — `REGISTRY VALIDATOR: MISSING INSTRUMENT`

The absence of a tool that actually validates the Agent Card registry, the runtime inventory, the
relevant structure/schema, and any cross-file invariants the contract declares.

🔴 **DO NOT implement it in the sunset candidate** unless strictly necessary to the sunset. **Do
not widen scope silently.** Its development needs a separate authorization.

### G · OPEN DEBTS CARRIED FORWARD

```
approval queue non-canonical · ACK criteria · Plan→Mirror routing
P7 event ledger — OWED NOT BARRED
Mirror's methodology observation — UNRATIFIED under G.2
registry validator — MISSING INSTRUMENT
```

**DO NOT carry:** `C.2` (**CLOSED** by operator determination, 7/7 both directions) · P1's
missing-registry precondition (**resolved**).

---

## Candidate discipline

Manifest · `BASE_HEAD` · candidate tip · `CANDIDATE_CONTENT_HASH` **under the canonical rule now
in force** (`legend-candidate-v4`; `reviews/` is a declared root) · complete classified diff ·
file list · **normative vs runtime vs documentation changes distinguished** · applicable
test/validator evidence · unresolved open debts.

**No `HUMAN_APPROVAL` pre-filled. None exists and none is implied.**

## Then Mirror — and the operator names what to ask

Independent review of **both the new binding and the content**, verifying specifically:

```
VISIBILITY vs LIFECYCLE ENFORCEMENT · lease-state derivation · the Current-instance rewrite
P1's classification · the registry-validator debt · absence of scope creep
```

**No prior attestation transfers.** Mirror's `ORCHWT` verification says nothing about this
candidate.

## Not authorized — for Plan or Orchestrator

Executing the sunset · any `CANONICAL_BATCH_COMMIT` · new `HUMAN_APPROVAL` · implementing the
registry validator · P7 · the approval queue · ACK criteria · ratifying Mirror's observation ·
further L2 smoke tests · scientific content · **any change to `main`**.

---

## Context the next Plan session needs, and would otherwise re-derive

**The finding that decides C's shape.** Today's three lease failures separate on one axis, and a
tracked home answers only two:

| Failure | Fixed by a tracked home? |
|---|---|
| stored `ACTIVE` past expiry | **no** — makes it visible, not correct |
| derivation read `ACTIVE` on a released lease | already fixed, by a two-input rule |
| **expired unused between turns, before `GATE 0` could be asserted** | **no — nothing was watching** |

**The lifecycle is currently an instruction, not a mechanism.** The derivation tool is ephemeral
and dies with its session; the obligation to write the terminal row is prose. Five lease records
stand, **every terminal state written by hand, and not one of those hands is a mechanism.**

**Why `deployment/local_instance.md` was chosen and why it must go.** It satisfied three
constraints — no root dirt, no `main` movement, durable across sessions — and it was ratified as
**interim** with `ORCHWT` execution as its stated sunset. `ORCHWT` has executed. The cost accepted
at ratification was that **I.3's specified `DETECTION` — *"doppio record sulla stessa
successione"* — is removed, not weakened**, since a gitignored file no other checkout can read
cannot produce a double record observable by anyone.

**Where the state stands.** `main f5b32155` · orchestrator worktree at `632ad22` ·
`EVAC-20260817-001` returned 9/9, 0 digest mismatches · the registry instance is back **and now
tracked**, which is a better state than it held before the evacuation.

**A drafting warning earned this week.** **Record every number with its bound.** The recurring
defect across this entire effort was a measurement that was **correct** and a noun that was
**wrong**. **A bare number is the form in which that defect is undetectable** — and *produce a
second quantity* and *define the population* are both special cases of it.

**Instances, with their provenance marked** — because a list carried without its bound is the
defect arriving inside the warning against it:

| Instance | Provenance |
|---|---|
| pipe lines vs body rows, 13/12 in §4 | `PRIMARY` — measured in this repository |
| a branch tip vs an approved commit (`hash-determinism` vs `b9af54eb`) | `PRIMARY` |
| a tool's scope vs a protocol's (`snapshot()` vs Phase 3) | `PRIMARY` |
| a criterion vs a capability's name (`M2`/`S6`/`P1`) | `PRIMARY` |
| the reviewed *range* vs the reviewed *scope* (`05cdedae` vs `5cd7f85`) | `PRIMARY` |
| a grep population vs the population intended (`--grep=BATCH_COMMIT`) | `PRIMARY` |
| bytes vs characters, 834/829 | `BY-REPORT (ORCH)` — the Orchestrator measured it and places it in its own record: `awk` counted **bytes**, Python counted **characters**, and the byte count was published as a character count. **Checkable, by asking its author.** Plan did not measure it |
| zero- vs one-based, 469/470 | 🔴 `UNPLACEABLE` — **neither actor measured it and neither can locate it.** Retained as illustration only, and explicitly **not** reconstructed from plausibility |

**The last two rows were one row until the Orchestrator split them**, and the correction is worth
more than the content: `BY-REPORT` names *who did not measure something*, **not whether anyone
did**. Grouping a checkable relayed measurement with an unplaceable one under a single label was
the defect appearing **inside the row created to record evidential status** — the warning applied
to itself, and then applied to its own fix.

**The principle stands on the six marked `PRIMARY`**, all of which a next session can verify in
this repository without asking anyone.
