---
artifact: HUMAN_APPROVAL_QUEUE — keyed comparison and divergence report across three lineages
record_id: PLAN-J3-QUEUE-RECONCILIATION-001
task_id: PLAN_J3_QUEUE_RECONCILIATION_v1
scope_source: DEC-20260823-SURFACE-MAP-QUEUE-CLOSURE, Action 1 — HUMAN_APPROVAL_QUEUE reconciliation
author: plan
authored_on: 2026-08-23
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)
mode: ANALYSIS_ONLY

STATUS: READ_ONLY_COMPARISON
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - KEYED COMPARISON AND DIVERGENCE REPORT
  - NOT A MERGE
  - NOT A MERGE AUTHORIZATION
  - NOT A CAND — see § 6.3 for why, and what would have to be true for one
  - NOT A GOVERNANCE DECISION
  - NOT A SEMANTIC RESOLUTION — no record's status, validity or currency is decided here
  - NO NEW VOCABULARY

scope_note: >
  🔴 The governing decision `DEC-20260823-SURFACE-MAP-QUEUE-CLOSURE` is NOT a readable artifact.
  Measured over all 52 content refs and the working tree including untracked files: 0 paths under
  `governance/decisions/` matching `20260823`, 0 occurrences of the string `DEC-20260823`, with
  `DEC-20260822` at 47 as a working positive control. This record therefore works from the scope
  the operator transmitted in-session and says so, rather than citing an artifact it cannot read.
  If the DEC's Action 1 differs from the transmitted description, this scoping is wrong.

domain: >
  CONTENT. `learning/` is content by explicit intent (plan_defined_parameters.md § P5.1). The
  OBJECT of this analysis — `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` — is CONTROL PLANE and
  is NOT written by this record.
---

# `HUMAN_APPROVAL_QUEUE` — KEYED COMPARISON AND DIVERGENCE REPORT

> **Nothing is merged. Nothing is resolved. Nothing is authorized.**
> This record compares three lineages by approval ID, reports where they differ, and preserves
> every record. It decides the status of none of them.

---

## 1 · OBSERVATION_SCOPE

```
OBSERVATION_INSTANT   2026-08-23T10:30Z … 10:45Z (UTC, runtime clock)
ACTING_WORKTREE       .claude/worktrees/evidence-index
BRANCH                plan-orchsurf-r4-transcription     HEAD a277e82bb5a8f588
CANONICAL main        788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5     OBSERVED, NOT MOVED
CONTENT REFS          52   (43 refs/heads · 4 refs/remotes · 5 refs/tags)
OBJECT                ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl
                      present on 30 of 52 content refs
```

**Three lineages, and no fourth.** Every ref carrying the file resolves to one of three blobs; the
working-tree copy is the tracked one, not a fourth:

| blob | lines | refs | reachable from |
|---|---|---|---|
| `20c24a2ba478` | 6 | **27** | `main` and 26 others, including this HEAD |
| `bb603d9a270b` | 10 | **1** | `refs/heads/orchestrator` |
| `95fc81639014` | 14 | **2** | `refs/heads/evidence-index`, `refs/heads/p51c9-rebased-onto-c89c2217` |

---

## 2 · KEYED COMPARISON BY APPROVAL ID

Every line of every lineage, keyed. `REQU` = request, `RESO` = resolution, `CORR` = correction,
`HEAD` = the schema header. Line numbers are positions in that lineage's own file.

| APPROVAL KEY | `main` (6) | `orchestrator` (10) | `evidence-index` (14) |
|---|---|---|---|
| *(schema header)* | L1 HEAD | L1 HEAD | L1 HEAD |
| `APR-20260816-GOV311-001` | L2 REQU/PENDING · L3 RESO/APPROVED | L2 · L3 **identical** | L2 · L3 **identical** |
| `APR-20260816-GOV311-002` | L4 REQU/PENDING · L5 RESO/APPROVED | L4 · L5 **identical** | L4 · L5 **identical** |
| `COR-20260816-GOV311-001` | L6 CORR | L6 **identical** | L6 **identical** |
| `APR-20260817-HA-1` | — absent | — absent | L7 REQU/PENDING · L11 RESO/**APPROVED** |
| `APR-20260817-HA-2` | — absent | — absent | L8 REQU/PENDING · L12 RESO/**DEFERRED** |
| `APR-20260817-HA-3` | — absent | — absent | L9 REQU/PENDING · L13 RESO/**RESOLVED** |
| `APR-20260817-HA-4` | — absent | — absent | L10 REQU/PENDING · L14 RESO/**DEFERRED** |
| `APR-20260818-SUNSET-DEC3-001` | — absent | L7 REQU+RESO/**APPROVED** | — absent |
| `APR-20260819-SCIAB-001` | — absent | L8 REQU+RESO/**APPROVED** | — absent |
| `APR-20260819-XPORT-001` | — absent | L9 REQU+RESO/**APPROVED** | — absent |
| `APR-20260819-P5DOMAIN-001` | — absent | L10 REQU+RESO/**APPROVED** | — absent |

### 2.1 · The shared base is byte-identical, verified per line

Not asserted from the prefix test — each of the six lines was hashed independently on each
lineage and the three hashes compared:

```
L1 (header)                 235d5b5b98d4   IDENTICAL × 3
L2 APR-…-GOV311-001 REQU    f165c1504064   IDENTICAL × 3
L3 APR-…-GOV311-001 RESO    935ee0808d1a   IDENTICAL × 3
L4 APR-…-GOV311-002 REQU    0415b2f27d31   IDENTICAL × 3
L5 APR-…-GOV311-002 RESO    a92961fb2a1e   IDENTICAL × 3
L6 COR-…-GOV311-001         4748772d3ac3   IDENTICAL × 3
```

### 2.2 · 🔴 ZERO KEY COLLISIONS — the divergence is additive, not contradictory

**No approval ID appears on two lineages with different content.** The two divergent slices are
**disjoint sets** over a byte-identical common base. Nothing in either slice contradicts anything
in the other.

```
shared base        3 approval objects  (2 approvals + 1 correction), identical on all three
orchestrator only  4 approvals         SUNSET-DEC3 · SCIAB · XPORT · P5DOMAIN
evidence-index only 4 approvals        HA-1 · HA-2 · HA-3 · HA-4
collisions          0
byte conflicts      0
```

---

## 3 · DIVERGENCE REPORT

### 3.1 · 🔴 D-1 — LINE COUNT IS NOT CHRONOLOGY, and this is the trap

The 14-line lineage is **earlier** than the 10-line lineage. Dates read from the records
themselves:

```
evidence-index (14 lines)   HA-1 … HA-4            2026-08-17          ← EARLIER
orchestrator   (10 lines)   SUNSET-DEC3-001        2026-08-18
                            SCIAB-001              2026-08-19T13:02:58Z
                            XPORT-001              2026-08-19T17:05:17Z
                            P5DOMAIN-001           2026-08-19T20:06:42Z ← LATER
```

**The two slices are consecutive, not competing.** They are adjacent segments of one approval
history that was never written into one file. Anyone reconciling by "take the longest file" or
"take the most recent branch" would place the 2026-08-17 round *after* the 2026-08-19 round.

### 3.2 · D-2 — the two slices use different record shapes

| | `evidence-index` slice | `orchestrator` slice |
|---|---|---|
| shape | **two lines** per approval: REQUEST (`PENDING`) then RESOLUTION | **one line** per approval: `APPROVAL_ID` + `RESOLUTION_ID` together |
| fields | `APPROVAL_ID, STATE, REQUESTED_AT` → `RESOLUTION_ID, RESOLVES_APPROVAL_ID, STATE, RESOLVED_AT` | `APPROVAL_ID, RESOLUTION_ID, STATE, RESOLVED_AT, DECIDED_BY` |
| implication | matches the header's own rule: *"A resolution is a NEW line carrying `RESOLVES_APPROVAL_ID`; the PENDING line below is never edited"* | the approval **never existed as `PENDING`** in this file; it was recorded once, after the fact |

**Reported, not adjudicated.** Whether a single-line after-the-fact record satisfies J.3 is a
determination this record does not make.

### 3.3 · D-3 — two `STATE` values are outside J.3's vocabulary

J.3 declares `PENDING | APPROVED | APPROVED_WITH_MODIFICATION | DENIED | REVISION_REQUESTED`.

```
APR-20260817-HA-2   STATE: DEFERRED   ← not in J.3
APR-20260817-HA-3   STATE: RESOLVED   ← not in J.3
APR-20260817-HA-4   STATE: DEFERRED   ← not in J.3
```

🔴 **These are preserved exactly as written and are NOT normalised.** The rule is the lease
record's, and it applies unchanged here: *"Do not normalise a historical row to make the check
pass. A disagreement is a finding about the record, and a record edited to agree with its own
derivation has stopped being evidence."* Mapping `DEFERRED` onto a J.3 value would be a semantic
resolution, which this scope forbids.

### 3.4 · D-4 — `main` carries neither slice

The sovereign ref carries **6 lines**. Eight operator approvals — every approval of 2026-08-17,
-18 and -19 — are **invisible from `main`**, including the four that accompany candidates now
canonical. An actor reconstructing approval state from the sovereign ref alone sees none of them.

### 3.5 · 🔴 D-5 — one operator decision exists ONLY inside this file, on one ref

`APR-20260817-HA-3` is `TYPE: GOVERNANCE` and its object is a decision:

```
decision_id: DEC-20260817-001-B2
question:    "adoption of the declared §8 divergence"
options:     A adopt the declared divergence · B do not adopt now · C amend §8 in a future
             governance change
RESOLUTION:  STATE: RESOLVED   DECISION: "B — NOT NOW"
```

`governance/decisions/` contains **no `DEC-20260817` record** (§ 1 of the surface map measured the
directory's five files; its earliest is 2026-08-20). The decision string appears in 4 files across
52 refs. **An operator governance determination is recorded only as an approval-queue line, on
two of fifty-two refs.** Reported; not resolved, and not relocated.

---

## 4 · PRESERVATION — every unique record, subject verbatim

No record is summarised into a status. The `OBJECT` field is reproduced as written.

### 4.1 · `evidence-index` slice — 2026-08-17

| key | TYPE | REQUESTED_BY | OBJECT as written | resolution as written |
|---|---|---|---|---|
| `APR-20260817-HA-1` | MAJOR | plan | `CAND-20260817-HASHDET` r3, hash `c85acdb2…05d8`, base `908197ba…3656` | `APPROVED` |
| `APR-20260817-HA-2` | MAJOR | plan | `CAND-20260817-P51C9` r2, hash `f325bd9d…51da`, base `908197ba…3656` | `DEFERRED` |
| `APR-20260817-HA-3` | GOVERNANCE | plan | `DEC-20260817-001-B2` — adoption of the declared §8 divergence | `RESOLVED` · `B — NOT NOW` |
| `APR-20260817-HA-4` | MAJOR | plan | `CAND-20260817-ORCHWT`, hash `280dc497…5763`, base `908197ba…3656` | `DEFERRED` |

### 4.2 · `orchestrator` slice — 2026-08-18 / 19

| key | TYPE | DECIDED_BY | operator statement as written | resolution |
|---|---|---|---|---|
| `APR-20260818-SUNSET-DEC3-001` | MAJOR | operator | *(none recorded)* | `APPROVED` |
| `APR-20260819-SCIAB-001` | MAJOR | operator | *(none recorded)* | `APPROVED` |
| `APR-20260819-XPORT-001` | MAJOR | operator | *"Approvo XPORT Revision 2"* | `APPROVED` |
| `APR-20260819-P5DOMAIN-001` | MAJOR | operator | *"Approvo CAND-20260819-P5DOMAIN."* | `APPROVED` |

### 4.3 · Corroboration measured elsewhere — evidence, NOT a determination of status

Content-tip ancestry of `main`, read from each candidate's own manifest rather than from a branch
tip (a branch tip may sit ahead of the canonicalized content and is the wrong test):

| approval | candidate content tip | ancestor of `main`? |
|---|---|---|
| `HA-1` | `b9af54ebe2fd` (HASHDET) | **YES** |
| `HA-2` | 🔴 **NOT DECLARED** in `CAND-20260817-P51C9.md` | **NOT MEASURABLE at content-tip precision** |
| `HA-3` | — decision, no content tip | n/a |
| `HA-4` | `ab4856b1d90c` (ORCHWT) | **NO** |
| `SUNSET-DEC3-001` | `234c8bae2a33` | **YES** |
| `SCIAB-001` | `4454feab72b7` | **YES** |
| `XPORT-001` | `e839db383827` | **YES** |
| `P5DOMAIN-001` | `ceefaa286115` | **YES** |

> 🔴 **This table is corroboration, not adjudication.** That a candidate's content reached `main`
> is not a ruling that its approval record is current, valid or superseded; that it did not is not
> a ruling that the approval lapsed. `HA-2`'s row is `NOT MEASURABLE`, not `NO`.

---

## 5 · WHAT A ONE-OFF RECONCILIATION WOULD REQUIRE — proposed, not authorized

### 5.1 · The union is well-defined, and that is a measurement

Because § 2.2 found **zero key collisions and zero byte conflicts on the shared base**, a union
exists and is unambiguous at the key level. Its order is fixed by § 3.1's dates, not by line
count:

```
L1–L6      the shared base, byte-identical on all three lineages
then       APR-20260817-HA-1 … HA-4  with their four resolutions   (2026-08-17)
then       APR-20260818-SUNSET-DEC3-001                            (2026-08-18)
then       APR-20260819-SCIAB-001 · XPORT-001 · P5DOMAIN-001       (2026-08-19)
           = 6 + 8 + 4 = 18 lines, every existing line preserved, none rewritten
```

**No line needs editing, deleting or normalising for this union to be constructible.** That is
the whole content of the claim; it is not permission to build it.

### 5.2 · 🔴 The constraint that governs who may perform it

**A reconciliation performed from here would create a FOURTH lineage.** This worktree is on
`plan-orchsurf-r4-transcription`; writing an 18-line file here adds a fourth blob to a file whose
forking is the defect being reconciled. The same is true of any actor writing from any branch that
is not the one the result must live on.

```
REQUIRED   exactly ONE writer, writing ONCE, onto the ref the reconciled file is to live on
ABSENT     ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl has NO DECLARED WRITER — J.3 names
           REQUESTED_BY and a resolver, and allocates no file writer; P7's one-writer decision
           covers ledger/events/, not ledger/approvals/
ABSENT     0 ACTIVE leases by derivation, so there is no ACTIVE_ORCHESTRATOR to write onto main
           under GATE 0
```

**Both absences are outside this scope** (allocating a writer is a governance act; the lease is an
activation condition). They are stated because a reconciliation that ignores them repeats the
defect it repairs.

### 5.3 · Why this record is not a CAND

A `CAND` under Annex D.2 proposes content for canonical integration, carries a
`CANDIDATE_CONTENT_HASH`, and exists to be approved and executed. Three reasons it is the wrong
instrument here, and the first is decisive:

1. **The scope forbids merge authorization.** A candidate proposing the reconciled file *is* the
   merge authorization, in the only form the governance has.
2. **The object is outside the candidate content domain.** `ledger/` is a declared
   `CONTROL_PLANE_ROOT` (P5.1), so the queue file cannot move a `CANDIDATE_CONTENT_HASH`. A
   candidate whose entire payload is invisible to its own binding is not a candidate.
3. **GATE 2 currently fails in this working tree** — `BLOCK_PUBLICATION`, 3 `DIRECT_IDENTIFIER`
   findings in an untracked file authored by another session. A clean checkout of this HEAD passes
   with 0 blocks, so the block is working-tree-only and touches no committed state; but no
   candidate can be gate-evidenced from here while it stands.

**What would have to be true for a CAND to be the right instrument:** a declared writer for the
J.3 surface, an authorization to merge, and a decision on whether reconciliation is a canonical
act or a control-plane one. All three are governance determinations, and none is made here.

---

## 6 · WHAT THIS RECORD DOES NOT DO

Does not merge · does not authorize a merge · does not write to
`ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` on any ref · does not create a fourth lineage ·
does not normalise `DEFERRED` or `RESOLVED` onto J.3's vocabulary · does not decide whether the
single-line record shape is J.3-conformant · does not rule on the currency, validity or
supersession of any approval · does not decide whether `HA-2` and `HA-4` deferrals remain live ·
does not relocate `DEC-20260817-001-B2` · does not allocate a writer · does not open a `CAND` ·
does not write a `DEC` · does not introduce vocabulary · does not touch the five untracked
artifacts of another session · does not advance `main`.

---

## 7 · VERIFICATION TRAIL

| # | check | result |
|---|---|---|
| 1 | governing DEC readable? | 🔴 **NO** — `DEC-20260823` : 0 hits over 52 refs and the working tree · control `DEC-20260822` : 47 ✅ |
| 2 | queue lineages | **3** — blobs `20c24a2ba478` (6 L, 27 refs), `bb603d9a270b` (10 L, 1 ref), `95fc81639014` (14 L, 2 refs) |
| 3 | fourth copy? | **none** — the working-tree file is tracked; 30 of 52 refs carry the file |
| 4 | shared base | **6 lines, byte-identical on all three**, hashed per line |
| 5 | key collisions | **0** |
| 6 | byte conflicts on shared base | **0** |
| 7 | chronology vs line count | 🔴 **inverted** — the 14-line lineage is dated 2026-08-17, the 10-line one 2026-08-18/19 |
| 8 | out-of-vocabulary states | **3** (`DEFERRED` × 2, `RESOLVED` × 1) — preserved, not normalised |
| 9 | approvals invisible from `main` | **8** |
| 10 | union size if constructed | **18 lines**, 0 edited, 0 deleted |
| 11 | declared writer for the surface | 🔴 **none** |
| 12 | ACTIVE leases | **0 by derivation** |
| 13 | `main` | `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` — unchanged |

---

**Prepared by:** `plan`, worktree `evidence-index`, branch `plan-orchsurf-r4-transcription`,
2026-08-23 — under the operator's transmitted scope for Action 1, **not** under the authority of
`roles/plan.md`, and **not** under an artifact named `DEC-20260823-SURFACE-MAP-QUEUE-CLOSURE`,
which is not readable from any ref.
