---
artifact: REVIEW OPENING — Annex C.3 (`Apertura solo via Orchestrator`)
review_id: REV-ORCHSURF-MIRROR-002
opens: Mirror hostile review of CAND-20260819-ORCHSURF **revision 4**
object: CAND-20260819-ORCHSURF r4 · CANDIDATE_CONTENT_HASH
  844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
  @ BASE_HEAD 04693e68 · CONTENT_TIP 9a70e94d · branch `orchestrator-surface`
level: R4 — MIRROR_REQUIRED (Annex G.1: governance artifacts, MAJOR; Annex C.1 floor R4 METHOD)
reviewer: mirror
author: plan
adjudicator: orchestrator (Annex C.3) · HUMAN_APPROVAL operator (Annex H.1, MAJOR/governance) —
  none granted, none implied, none prefilled by this opening
opened_by: orchestrator
opened_at: 2026-08-20T16:52:47Z
supersedes: nothing. REV-ORCHSURF-MIRROR-001 reviewed revision 1 and is CLOSED at
  REQUEST CHANGES. Under Annex D.2 its binding is superseded because the content moved. **No
  verdict transfers.**
delivery: see § 7. Routing is UNRESOLVED. This file is the durable transport; any message is a
  pointer to it, never a substitute for it
---

# Opening — `REV-ORCHSURF-MIRROR-002`

Plan delivered revision 4 with an explicit statement that it does not open its own review
(Annex C.3). This file is that opening. It assigns the review, states the mandate, records what
the Orchestrator verified for **readiness only**, and names what is out of scope and what remains
owed.

**This opening grants no approval and predicts no verdict.** `REQUEST CHANGES`, `CONFIRMED`,
`WEAKENED`, `REFINED`, `REFUTED` and `DISAGREEMENT_UNRESOLVED` are all open outcomes.

---

## 1 · Task contract (Annex A.1)

```
TASK_ID              TASK-20260820-MIRROR-ORCHSURF-REV4
DIRECTIVE_VERSION    1
GENERATION           1
OWNER                mirror
PRIORITY             HIGH — the candidate is delivered and blocked on review; main is untouched
OBJECTIVE            Hostile review, Annex C.2 format, of CAND-20260819-ORCHSURF revision 4,
                     evaluated against the RATIFIED operator intent record
                     governance/decisions/DEC-20260820-ORCH-SESSION-HOME.md
SCOPE                The three-layer structure of § 3 below, the integrity items of § 4, and the
                     ranked attack surface Plan supplies in HANDOFF-ORCHSURF-MIRROR.md
DEPENDENCIES         none blocking. The package is self-contained on branch `orchestrator-surface`
REVIEW_REQUIREMENT   R4 (floor), Annex C.1 · MIRROR_REQUIRED, Annex G.1
INTERACTION_MODE     QUESTIONS_ALLOWED — an unresolved question routed to Orchestrator is inside
                     this contract, not a failure of it
RETRY_POLICY         max_attempts 1 · on_exhaust ESCALATE to Orchestrator. A review is not retried
                     on disagreement; disagreement is an outcome (C.3)
MILESTONE_PLAN       M1 rehydration + independent re-derivation of § 4 → the review's § 0
                     M2 layer-by-layer findings → the review body
                     M3 verdict + WHAT_WOULD_CHANGE_MY_MIND → durable file, WORK_COMMIT
DELIVERABLE          reviews/mirror/REV-ORCHSURF-MIRROR-002.md on branch `mirror`, worktree
                     `.claude/worktrees/mirror`, persisted by WORK_COMMIT
CURRENT_STATE        branch `orchestrator-surface` @ da47440 (manifest tip); CONTENT_TIP 9a70e94d
```

**ACCEPTANCE_CRITERIA** — each verifiable, none satisfied by assertion:

1. Every value in § 4 **re-derived independently**, not compared against this file (see § 5).
2. A disposition for each of the six mandate items in § 3.
3. Annex C.2 format complete, with `STEELMAN` **before** the objections and
   `WHAT_WOULD_CHANGE_MY_MIND` as a declared falsifier.
4. Layer-3 completeness executed as a **search**, not an inspection: § 17.1 either disposes of
   every assertion §§ 2–15 still make, or the gap is named as a finding.
5. Any contradiction that survives is reported as a finding rather than resolved by deference to
   Plan, to the operator record, or to this opening.

---

## 2 · Why this review exists and what changed under it

Revision 4 **inverts the remedy direction** of revisions 1–3. The ratified operator record states
that the Orchestrator's **session home is the repository root by architectural intent**, and that
the `orchestrator` worktree is that actor's **WORK_COMMIT surface** — both, because they answer
different questions. Revisions 1–3 read these as rival topologies and proposed to extinguish
root-promotion. That direction is withdrawn, and with it the `HUMAN_REQUIRED` FROZEN transition,
the four-role fingerprint rotation and the `BLOCKED_BY_GOVERNANCE` stop.

`REV-ORCHSURF-MIRROR-001` therefore transfers **nothing as a verdict** — and less than for an
ordinary re-binding, because the direction it reviewed no longer exists.

---

## 3 · The mandate — three layers, six items

The candidate must be read as three kinds of text. Reviewing them as one kind is the specific
failure this structure invites.

```
LAYER 1 — CURRENT OPERATIVE MODEL   § 1 (manifest) and § 17 (revision-4 disposition).
                                    These govern. Where §§ 2–15 conflict, these win.

LAYER 2 — HISTORICAL EVIDENCE       §§ 2–15, retained VERBATIM at operator direction.
                                    They argue the withdrawn direction. They are NOT current
                                    claims — and they are NOT out of scope either.

LAYER 3 — RESOLVED FINDINGS         § 17.1 must dispose of every relevant historical finding,
                                    each by one test: did it depend on the remediation
                                    direction? PRESERVED if direction-independent,
                                    WITHDRAWN if direction-dependent.
```

Mirror must independently verify, and report a finding wherever a contradiction survives:

1. **DEC lineage and hash history** — the three hashes of the operator record, and which one the
   ratification attaches to.
2. **The re-bind event `1a650d8 → 9a70e94`** — whether it is a re-binding or a revision 5. Plan
   offers its judgement explicitly so it can be overturned; overturning it is a legitimate
   outcome.
3. **CONTENT_HASH** `844de909…acb6dc` at CONTENT_TIP under BASE_HEAD.
4. **No FROZEN governance modification.**
5. **BASE_HEAD and candidate binding** — that the declared base is canonical `main` and the
   binding holds.
6. **Historical sections versus operative disposition** — Layer 3 completeness. Plan states this
   is where the package is most likely to hide something and that it cannot see it from inside.
   Treat item 6 as the primary object of this review, not the last box.

---

## 4 · Orchestrator readiness verification — NOT a review, NOT transferable

Run before opening, to establish that the package is coherent enough to review. Every value was
computed from explicit commit SHAs in the root checkout and a throwaway detached checkout, which
was removed; the root tree was byte-clean before and after.

```
pwd == git top-level      <REPO_ROOT>               PASS
canonical main            04693e683a254ff0a6d0619fba47103a0fb7d122
                          read from git refs, not from any prompt or document PASS
BASE_HEAD declared        04693e68…  == canonical main                       PASS
merge-base(main, branch)  04693e68…  == BASE_HEAD — branch descends from base PASS
CONTENT_TIP ancestry      9a70e94d is an ancestor of branch tip da47440       PASS
CONTENT_HASH recomputed   844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
                          == declared                                        PASS
pre-rebind hash           79af3e52…82ea0 at 1a650d8 — DIFFERENT, so the
                          re-bind moved a real value, not a label            PASS
manifest-tip invariance   hash at da47440 == hash at 9a70e94d, because
                          9a70e94..da47440 touches only governance/candidates/,
                          a declared CONTROL_PLANE_ROOT                      PASS
FROZEN untouched          git diff BASE..da47440 over the body and annexes
                          A–J is EMPTY                                       PASS
DEC three hashes          9861fb05…c0bee7 @ c4c0fa1  (as ratified, pre-signature)
                          6e89ba5f…4e1e1 @ ec4bf60 and 1a650d8 (signed)
                          6b5d9c3f…2f83c @ 9a70e94 and da47440 (redacted)
                          all three reproduce exactly as claimed             PASS
redaction magnitude       one line, frontmatter `ratified_by` only           PASS
DEC ratification          `ratified_by` is filled — the record is RATIFIED
                          and therefore binding under its own § 6            PASS
lease (derived)           9 records, ACTIVE by derivation = 0. Derived, never
                          read from the stored STATUS field                  PASS
```

**Fingerprint rotation — measured, and it is exactly one role:**

| role | @ BASE_HEAD | @ CONTENT_TIP | rotates |
|---|---|---|---|
| `mirror` | `e01b4108…0412` | `e01b4108…0412` | **no** |
| `orchestrator` | `88dea7a6…5ebb` | `f85d743c…fefe` | **YES** |
| `plan` | `0d6987bd…1429` | `0d6987bd…1429` | no |
| `scientist` | `b66959cd…9d1e` | `b66959cd…9d1e` | no |

Two consequences, offered as input and not as conclusions. **Mirror's own fingerprint does not
move**, so this candidate does not invalidate the reviewer's checkpoint — the same condition that
held at `REV-ORCHSURF-MIRROR-001`. **The Orchestrator's fingerprint does move**, because
`roles/orchestrator.md` is in that actor's `CORE` (P2.2: `CORE` includes *the actor's own role
contract*) and revision 4 adds 103 lines to it. Whether one rotation is the correct and
sufficient consequence of revision 4 — against revision 3's withdrawn four-role rotation — is a
question for the review, not a fact this opening settles.

---

## 5 · How this section must be used — the inheritance trap

🔴 **Do not approve by inheritance, and do not verify by agreement.**

§ 4 is disclosed so that a disagreement between Orchestrator and Mirror becomes visible instead of
silent. It is **not** an evidence bundle and it discharges nothing.

**Re-derive; do not compare.** Two counts that agree verify nothing if the numbers were compared
and the sets underneath them never were. The hash pre-image is 541 lines across 539 included
entries — a matching scalar is consistent with a different domain. Re-derive the *set*: run
`--show-domain`, and check what was excluded and why, not merely that the digest matches.

If a value in § 4 does not reproduce, that discrepancy outranks this file and is a finding
against it.

---

## 6 · Boundaries

**Out of scope — must not enter this review:**

- **ROOTGUARD** (`CAND-20260820-ROOTGUARD-001`). Deferred by the ratified record § 1 item 5,
  explicitly out of scope, and it must not be smuggled in.
- Routing, Candidate B, C-9 § 7.2, the `runtime/` classification, Scientist activation and
  BENCH-AB-001 — this candidate does not canonicalize them.

**Owed, and NOT discharged by this review or by any verdict it reaches:**

```
PROBE-ORCHWT-001 LEG 3   Historical Orchestrator root-contamination measurement: UNVERIFIED.
                         It is the Orchestrator's to take — Plan may not, without writing into
                         another actor's worktree and corrupting what it measures. It is NOT
                         taken by this opening and is not a precondition of the review. No part
                         of the package may lean on SMOKE-PLAN-PROVISION-001 or
                         CONTROL-PLAN-WORKCOMMIT-001 as if either were leg 3; both are on
                         Plan's surface. Check that § 17.3 holds that line.
ORCH WORK_COMMIT CAP     Distinguish measured fact from assumption. Branch `orchestrator` carries
                         19 commits not on `main`, which is an observation about the branch; the
                         capability row is added as UNVERIFIED. CONFIGURED != PROVEN applies to
                         the actor that enforces it on others.
PLAN CROSS-WORKTREE      Refusal NOT tested and NOT to be assumed. It was not authorised and not
                         attempted. Confirming a boundary by crossing it is not a measurement
                         taken on one's own initiative.
REGRESSION SUITE         NOT re-measured at revision 4. Revision 3's DELTA 0 was taken against a
                         suite red at `main`. Revision 4 does not restate a number it did not
                         take, and neither does this opening.
```

**One observation handed over, adjudicated by nobody yet.** The redaction removed the direct
identifier from the tree, and the publication gate reads the tree at a tip. The identifier remains
reachable in branch history at `ec4bf60` and `1a650d8`. This is not a defect in revision 4's
reasoning and it is not a FROZEN violation; it is a residual the redaction cannot reach by
construction. It falls inside mandate item 1 ("DEC lineage and hash history"), so it is recorded
here rather than left for someone to rediscover. Its disposition is the operator's, not Mirror's
and not mine.

---

## 7 · Delivery, stated honestly

Routing remains **UNRESOLVED**, exactly as Plan recorded when it delivered the handoff. This file
is the transport.

A peer session presenting as `mirror-99` is visible from this session. **A displayed name is not
an ACTOR_ID.** No session has been elected, addressed or verified as `mirror` by this opening, and
none is treated as having received it. If a message is sent, it carries a pointer to this file and
the recipient proves identity from durable state — ACTOR_ID, worktree and branch — before anything
is treated as delivered. Delivery is recorded when it is verified, and not before.

---

## 8 · Standing of `main`

`main` is UNCHANGED at `04693e68`. Nothing is canonicalized, no lease was acquired, and no batch
was opened — this opening is not a `CANONICAL_BATCH_COMMIT` and GATE 0 is not the gate it passes
through. GATE 1 keeps proposer and executor distinct: Plan authored, Mirror reviews, Orchestrator
adjudicates, and the operator approves a MAJOR. Those are four positions and this file occupies
exactly one of them.
