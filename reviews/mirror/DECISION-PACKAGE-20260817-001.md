---
artifact: MIRROR decision package for HUMAN_APPROVAL
package_id: DECISION-PACKAGE-20260817-001
reviewer: mirror
adjudicator: operator
date: 2026-08-17
supersedes_fact_in: HANDOFF-CANDIDATE-READINESS-001 § 3.3 — see § 0
scope: decisions requiring operator intent only — no execution authorised, GATE 0 not evaluated, no batch, no merge
---

# HUMAN_APPROVAL — DECISION PACKAGE

## 0 · A correction to my own previous handoff, first

`HANDOFF-CANDIDATE-READINESS-001` §3.3 listed `APR-20260816-GOV311-001` and `-002` as *"both read
`PENDING`"* and carried them as open governance decisions. **That is wrong, and the error is mine.**

Both are **resolved and APPROVED**:

```
L2  APR-20260816-GOV311-001  MAJOR       PENDING     ← the original request, never edited
L3  RES-20260816-GOV311-001              APPROVED    ← the resolution, appended
L4  APR-20260816-GOV311-002  GOVERNANCE  PENDING
L5  RES-20260816-GOV311-002              APPROVED
```

The queue is append-only: a resolution is a **new line** and the `PENDING` line is never mutated,
exactly as J.1 requires. My query selected lines carrying `APPROVAL_ID`; the resolutions carry
`RESOLUTION_ID`, so my filter dropped precisely the lines that answered the question, and the
subset read as the whole.

That is the sixth instance of the family this sequence has been tracking, and the third of them is
mine. It changes §4 materially: two items I listed as open are closed, and one of them closed
things I also listed as open.

---

## 1 · HASHDET r3 — decision summary

```
CAND-20260817-HASHDET   tip b9af54eb…   hash c85acdb2…ad05d8   v3   MAJOR
Mirror review: ACCEPTED (REV-HASHDET-MIRROR-003, e0da42b0) — no blockers
```

**Why it is prerequisite.** Before this candidate, `CANDIDATE_CONTENT_HASH` was a function of
`(base, tip, the verifier's checkout)`. Measured, with the pre-fix tool:

| Candidate | from a **v3** checkout | from a **v4** checkout | its manifest declares |
|---|---|---|---|
| P51C9 rev 2 | `db6cffac…` | **`f325bd9d…`** | `f325bd9d…` |
| ORCHWT | **`280dc497…`** | `b4e7c493…` | `280dc497…` |

**The two other candidates require opposite checkouts to reproduce their own declared hashes.**
There is no single vantage point from which you could verify both bindings: confirming one
falsifies the other. HASHDET restores `HASH = f(BASE, TIP)`, after which both reproduce from
anywhere — which is what I verified in each acceptance review.

That is the whole of the prerequisite, and it is narrow: it concerns **who can check a binding**,
not what the binding is. The hash values never change.

🔴 **What acceptance means.** `MIRROR_ACCEPTED` states that identity is reproducible and that I
found no defect requiring change. It is **not** execution authorization, not a gate assessment, and
not a statement that the change should be made. Annex C.2: `CONFIRMED` means *"no defect found given
the available evidence bundle"* — never *"true"*, and never *"proceed"*.

**Four non-blocking items remain open and were not waived**: the duplicated serialization
expression; `$(…)` stripping the last byte of the emitted representation; `test_historical_replay`
not discriminating in a v3 checkout; encoding implicit in P5.2.

---

## 2 · P51C9 rev 2 — decision summary

```
CAND-20260817-P51C9   tip b5eaf81e…   hash f325bd9d…0651da   v4   MAJOR
Mirror review: ACCEPTED (REV-P51C9-MIRROR-002, 64177c08) — no blockers
```

### Technically closed

| Item | State |
|---|---|
| F-1 scope contamination | **closed** — the deployment change left on a new commit, forward, not by rewrite; 0 `deployment/` files remain |
| F-3 orphaned provenance | **closed** — six source commits verified as ancestors, plus blob identity so a future rewrite cannot orphan the content |
| Manifest consistency | **closed** — no unmarked historical value; counts derived (505 / 19, matching the command) |
| P5.1 classification | **closed** — three roots; `learning/` content; `runtime/` still an open question, unchanged |
| Hash replay | **closed** — reproduced twice under HASHDET r3 tooling from an independent checkout |
| Regression | **none** — HASHDET r3, ORCHWT, GOV311 and `main` all unchanged |

### The one point requiring your interpretation

**`learning/plan/SLR-plan-0001.md` is inside the candidate. Decision 4 excluded SLRs from it.**

The recorded wording of Decision 4: *"SLRs — **excluded from this candidate** — both go to Mirror
for E.2 curation first."*

Two readings, both genuine. I present both and choose neither.

**Reading 1 — the decision named the two records then in existence.**
"Both" identifies the Orchestrator's two SLRs, which were what existed when you decided.
`SLR-plan-0001` is Plan's own and was produced afterwards, as a deliverable of the F-1/F-3
remediation. Body §18 names *"inclusione nel prossimo candidate"* as a route to durability for a
learning record, so inclusion is the frozen text's own mechanism rather than an exception to it.
The record carries `curation: PENDING — the confirmation classes are proposed by the author and are
not self-certified`, so it does not pre-empt E.2.
*Consequence if this is your reading:* nothing changes. The candidate stands as reviewed.

**Reading 2 — the decision stated a principle, and "both" merely counted the instances.**
The purpose was that **no uncurated learning record enters a MAJOR candidate before Mirror's E.2
curation**. On that reading the count is incidental and the rule is forward-looking, so a record
created *after* the decision is more squarely covered by it, not less. What sits in the candidate
today is exactly the described condition: a learning record inside a MAJOR whose confirmation
classes are proposed by its own author and curated by nobody.
*Consequence if this is your reading:* the SLR must be removed. That changes the content domain and
therefore the hash, producing a new candidate identity and requiring a fresh Mirror review.

**Why I do not choose.** Reading 1 is textually supported — I verified that §18 permits the route
and that the record does not self-certify. But textual support for one reading is not a
determination of what you meant, and Decision 4 is yours. The asymmetry worth knowing: **Reading 1
is reversible later at the cost of a re-hash; Reading 2 applied later is the same cost.** Neither
choice forecloses the other, so this is not urgent — it is only unavoidable.

---

## 3 · ORCHWT — the STOP CONDITION ambiguity

```
CAND-20260817-ORCHWT   tip ab4856b1…   hash 280dc497…65763d   v3   MAJOR
Mirror review: NOT PERFORMED
Content radius: deployment/deployment_profile.md — one file
```

Your instruction offered **Option B, formal divergence**, for the case where a compatibility
argument fails — and also instructed a **STOP** on conflict. The candidate reports both clauses and
declines to resolve them, stating that under one reading *"this candidate should be withdrawn
rather than reviewed."*

**The choice you must make is a question about your own instruction, not about the candidate.**
No review resolves it, which is why I have not performed one: reviewing first risks issuing a
verdict on an object that should not exist.

| | **Option A — withdraw** | **Option B — retain, with declared divergence** |
|---|---|---|
| Reading | STOP meant: stop the candidate | STOP meant: stop the compatibility route, then declare the divergence |
| Immediate consequence | the candidate leaves the queue unreviewed | the candidate enters Mirror review |
| What happens to the defect it addresses | it persists: body §8 places the Orchestrator in the root, the root's branch is `main`, and Annex D.1 obliges every actor to `WORK_COMMIT` on its own branch — so one actor cannot meet an obligation the frozen text imposes on all six. Addressing it would then need a different route, plausibly a body amendment rather than a profile change | the divergence from §8's residence clause becomes an explicit, reviewable object |
| What it then costs | a route not yet designed | if review passes, the divergence itself needs your ratification — the same shape as PID-09/PID-10, which you settled in `RES-001` |
| Reversibility | the branch and its single commit remain; withdrawal is not deletion | a declared divergence can be withdrawn later; an undeclared one cannot be found |

**I take no position on which reading was meant.** I record only that the two are genuinely
available in the text of the instruction, and that the candidate flagged the ambiguity instead of
resolving it silently — which was the correct behaviour.

---

## 4 · Remaining governance decisions — corrected

| Item | Actual state |
|---|---|
| **PID-09 / PID-10** | 🟢 **SETTLED.** `RES-20260816-GOV311-001` records both as `ACCEPTED`, with rationales, by the operator on 2026-08-16. My earlier listing of these as open was part of the §0 error. *(Note: `APPROVAL-GOV311-DEVIATIONS.md` still reads `state: AWAITING_HUMAN_APPROVAL` — a document describing a wait that ended, which is the same stale-state pattern, in a file whose correction is Plan's.)* |
| **`MIRROR_RETROSPECTIVE` cadence `N`** | 🟡 **DELIBERATELY CARRIED.** `RES-001` records it as `CARRIED_UNRESOLVED` *"by explicit operator decision. No numeric value introduced. Blocks nothing."* It is not an open decision awaiting attention; it is a decision already taken to defer. Ownership is unchanged: G.2 forbids me setting it alone |
| **Capability rollback authority** | 🔴 **OPEN.** C-9 §10 derives *Mirror writes the evidence event · Orchestrator writes the `VERIFIED → UNVERIFIED` transition* from Annex C.4 and promotion symmetry. Derived is not ratified, and the frozen text names neither writer. Requires you under H.1 |
| **C-9 adoption** | 🔴 **OPEN, and distinct from acceptance.** The document is `status: ACCEPTED` and carries `acceptance_is_not_adoption: true`. None of its clauses binds until adopted through a governed change. Accepting the document was a review outcome; adopting it is yours |
| **`APR-20260816-GOV311-001`** | 🟢 **APPROVED** (`RES-001`). Carries the E4 clause explicitly: the approval authorises the intent and does not authorise execution outside GATE 0–5, the stop conditions and the authority matrix |
| **`APR-20260816-GOV311-002`** | 🟢 **APPROVED** (`RES-002`), `ACCEPT INTERPRETATION 1`. Ruling: the lease requirement applies to canonical batches **after** the governance installation commit. **Scope is explicit and narrow** — *"for `CAND-20260816-GOV311` only … it does not generalise: every canonical batch after this one requires an ACTIVE singleton lease, unchanged."* |

🔴 **One consequence of `RES-002` bears directly on all three candidates in this package.** They are
all *after* the governance installation commit, so the lease exemption does not reach them: by your
own ruling, an ACTIVE singleton `ORCHESTRATOR_LEASE` is required for any canonical batch carrying
them. I state this as a scope fact from your resolution, not as a gate evaluation — GATE 0 is
outside this package by instruction.

---

## 5 · Final decision matrix

| Candidate | Technical state | Human decision required | Execution allowed? |
|---|---|---|---|
| **HASHDET r3** | `MIRROR_ACCEPTED`, no blockers, 4 non-blocking open | **Approve the intent, or not.** No interpretive question outstanding | **NO** — no authorization given; not evaluated here |
| **P51C9 rev 2** | `MIRROR_ACCEPTED`, no blockers, 3 non-blocking open | **Approve the intent, or not** — *and* settle §2: is `SLR-plan-0001` covered by Decision 4? Reading 2 requires its removal, a new hash and a new review | **NO** — no authorization given; not evaluated here |
| **ORCHWT** | **not reviewed** | **Settle §3 first**: Option A withdraw, or Option B retain and send to review. This precedes any approval question | **NO** — not reviewed, not approved |
| **GOV311** | approved, in canonical history | none — reference only | n/a — already committed |

| Cross-cutting | Requires you |
|---|---|
| Capability rollback authority | ratify or redirect C-9 §10's derivation |
| C-9 adoption | acceptance ≠ adoption; adoption is a governed change |

---

🔴 **This package recommends no execution and authorises no batch.** It contains no gate
assessment, no merge, and no canonical commit. `HUMAN_APPROVAL` is ungranted for all three
candidates. Every "Execution allowed?" cell reads **NO**, and none of them will change by anything
written here — only by your decision, followed by the gates that decision explicitly does not
bypass.

No file of any candidate was modified. All verification ran in disposable clones outside the
repository.
