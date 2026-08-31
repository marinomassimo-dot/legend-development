---
artifact: HANDOFF — CAND-20260819-ORCHSURF revision 4 → Mirror hostile review
from: plan
to: mirror
revision: 4
supersedes: the revision-3 handoff (CONTENT_TIP 25fa61ab, CONTENT_HASH ed020f37…c1f8), never
  reviewed; the revision-2 handoff (CONTENT_TIP 7b6a9d9a, hash b0a0c9ed…65d1), never reviewed;
  and the revision-1 handoff (CONTENT_TIP b3afdde4, hash 3af61c6d…4c7), reviewed as
  REV-ORCHSURF-MIRROR-001 (REQUEST CHANGES). Under Annex D.2 all three bindings are superseded
  because the content moved. **Nothing from that one review transfers as a verdict — and less
  than ever, because revision 4 inverts the direction revision 1 was reviewed under**
delivery: MANUAL. Routing is unresolved, so this file IS the transport. No SendMessage was sent,
  and no session was addressed, elected or verified as a recipient
authored_on: 2026-08-20
review_floor: Annex C.1 · MIRROR_REQUIRED (Annex G.1 — governance artifacts, MAJOR)
opens_by: Orchestrator (Annex C.3). Plan does not open its own review
---

# HANDOFF — `CAND-20260819-ORCHSURF` revision 4

## What to fetch

```
branch          orchestrator-surface
BASE_HEAD       04693e683a254ff0a6d0619fba47103a0fb7d122
CONTENT_TIP     9a70e94d6d9863622c22159d0d7f2117b77b793d
CONTENT_HASH    844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
                legend-candidate-v4 · 539 included · pre-image 541 lines / 58 040 bytes
MANIFEST_TIP    the branch tip — fetch `orchestrator-surface`, not a recorded SHA. A manifest
                cannot name the commit containing it, so any MANIFEST_TIP value is one commit
                behind the package. governance/candidates/ is excluded from the hashed domain,
                so control-plane commits cannot move CONTENT_HASH
manifest        governance/candidates/CAND-20260819-ORCHSURF.md
operator record governance/decisions/DEC-20260820-ORCH-SESSION-HOME.md  — RATIFIED
preparation     governance/candidates/PREP-20260820-ORCHSURF-REV4.md  — eight findings, the
                measurements, and the reasoning §17 compresses
SLR             learning/plan/SLR-plan-0013.md · SLR-plan-0012 · SLR-plan-0011
author response reviews/plan/AUTHOR-RESPONSE-ORCHSURF-MIRROR-001.md
```

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 04693e683a254ff0a6d0619fba47103a0fb7d122 \
  --tip  9a70e94d6d9863622c22159d0d7f2117b77b793d
# 844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
```

## Manifest lineage — two bindings inside revision 4, and why

Revision 4 was bound twice. **Both bindings are recorded, and the seam is not hidden.**

```
1a650d85e7686654e37329576c034b899d43bb40   first revision-4 content tip
    hash 79af3e52302aa4ca9fc99e53979904aff2535f28949f2af2a573eee222d82ea0
    publication gate at this tip: BLOCK · 1

9a70e94d6d9863622c22159d0d7f2117b77b793d   CONTENT_TIP as delivered
    hash 844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
    publication gate at this tip: PASS · 0
```

**What moved between them: one field, in one file.** `DEC-20260820-ORCH-SESSION-HOME.md` is an
**included** entry of the candidate content domain, so redacting a field inside it moved the
binding. Annex D.2 invalidates the first hash for that reason. The domain delta between the two
pre-images is **exactly one line** — the DEC's digest — and both pre-images are 541 lines /
58 040 bytes, identical in shape.

**Plan's judgement, offered for you to overturn: this is a re-binding, not a revision 5.** No
argument, finding, remedy or disposition changed. If you hold that any content change demands a
revision bump regardless of substance, say so — the judgement is recorded here precisely so it
can be contested rather than discovered.

## The DEC redaction event, and the three hashes of the operator record

The operator record was ratified, then redacted. Each step changed exactly one line, verified by
diff both times, and **all three hashes are meaningful and none is interchangeable**:

```
9861fb05c66d4e763f6f1e36e012f6f019a5447356fa35ec87f0153b29c0bee7
    the content AS RATIFIED, before any signature existed.
    THE RATIFICATION ATTACHES TO THIS VALUE

6e89ba5f23f6a5fd1ae70e7bc339d1cb452b38fb1a5f0c9ffaa22e705fc4e1e1
    after signature, carrying a direct identifier.
    This is the value that tripped the publication gate

6b5d9c3fd625aed3c72811d8bfff458f38b92f2973aa9b99aa90063df762f83c
    after identifier redaction — THE RECORD AS IT NOW STANDS in the tree
```

```
ec4bf60   ratification — ratified_by filled
9a70e94   redaction    — ratified_by: <operator name>  →  ratified_by: Operatore
```

The redaction was an operator decision of 2026-08-20, on the ground that the record's own
`authority:` field already read `Operatore`, that ratification is an operator **action** rather
than a public identity assertion, and that this is the public edition, where a registered private
identifier in canonical content is a publication block. **The ratification act is unchanged; only
its rendering is.** Verify that claim rather than take it: `git show 9a70e94` is one line.

**Why you are being told this at all.** The block was real, it was measured, and it was caused by
the ratification rather than by any content this candidate edits — established by stashing the
three edited files and re-measuring, which reproduced the same single block. A handoff that
reported only the final green gate would have concealed a genuine event in the package's history.

## Read the candidate in three layers — they are not the same kind of text

This is the most important instruction in this handoff, and it is deliberate rather than
accidental. **The operator directed that §§2–15 remain unrewritten**, so the package contains
reasoning that its own §17 supersedes.

```
LAYER 1 — OPERATIVE            §1 (manifest) and §17 (revision-4 disposition)
                               These govern. Where §§2–15 conflict with them, they win

LAYER 2 — HISTORICAL EVIDENCE  §§2–15, retained VERBATIM and NOT rewritten
                               These argue revisions 1–3's direction, which is withdrawn. They
                               are preserved as the observed record of how the reasoning went
                               wrong, not as claims the package still makes

LAYER 3 — RESOLVED FINDINGS    §17.1, a row per revision-3 finding, each disposed by ONE test:
                               did it depend on the remediation direction?
                               PRESERVED — direction-independent, carried unchanged
                               WITHDRAWN — direction-dependent, and the direction inverted
```

**Do not review §§2–15 as current assertions, and do not let them pass as harmless either.** They
are in scope as evidence: if §17 fails to withdraw something §§2–15 assert, that gap is a finding
and it is exactly the kind this layering could hide.

The rationale for keeping them is the operator's: rewriting would replace an observed evolution
with a cleaned narrative and reduce auditability. `SLR-plan-0012` L-1 records the same principle
from the other direction — a claim removed from a derived document is not thereby removed.

## What changed at revision 4, in one paragraph

**The remedy direction is inverted, and not one measurement is withdrawn to do it.**
`DEC-20260820-ORCH-SESSION-HOME`, ratified, states that the Orchestrator's **session home** is the
repository root by architectural intent and that the `orchestrator` worktree is that actor's
**WORK_COMMIT surface** — both at once, because they answer different questions. Revisions 1–3
read them as rival topologies and proposed to extinguish root-promotion; that direction is gone,
and with it the `HUMAN_REQUIRED` FROZEN transition, the four-role fingerprint rotation and the
`BLOCKED_BY_GOVERNANCE` stop. Three findings are new and none was reachable from the old
direction: **body §8 states the architecture at rank 1 and the whole package quoted one clause of
it against the rest (F-1)**; the WORK_COMMIT-impossibility premise that grounded the stop is
**false and was canonical in `main` (F-2)**; and **Annex I.2 step 4 and the deployment profile
were never one list (F-7)**. No FROZEN document is amended — `git diff` over the body and annexes
A–J across the whole range returns empty.

## Where to attack — ranked

**1 · Does body §8 mean session home, or association?** The costliest attack. *"Orchestrator vive
nella chat grafica associata a `<REPO_ROOT>`"* — a reader could hold that *associata* denotes the
actor's association with the root as its canonical batch surface, not the chat's filesystem
location. My answer: the subject of *vive* is *la chat grafica*, a chat's location is where it is
opened, §8's own title is **"ORCHESTRATOR — ROOT, AUTORITÀ, IDENTITÀ"**, and the very next
sentence denies that the location confers authority — a denial only necessary if the location is
real. **It is a reading, and F-1 and the whole revision depend on it.**

**2 · Does F-7's separation hold, or is it a distinction without a difference?** I claim Annex I.2
step 4's five worktrees are *derived from* step 6's five chats, so `orchestrator`'s absence is the
architecture rather than a gap. A reviewer could hold step 4 is an independent enumeration that
merely shares a cardinality — in which case its silence is silence, and revision 3's permission
argument (*"I.2 does not prohibit others"*), which revision 4 **withdraws**, would come back.

**3 · Is `BOOTSTRAP.md` step 11 lawful, and is it in the right place?** It is the one instruction
in this package with **no antecedent in any governed document**, and it is declared as new rather
than presented as a restoration. Two surfaces: does body §0.4's *"crea/verifica i worktree"* make
worktree creation an exclusively Controller act (if so, step 11 has no owner); and does the
pre-promotion perimeter *"SOLO artefatti di bootstrap"* reach post-promotion acts (I answer on
**temporal** scope and deliberately never define "artefatto" — attack that evasion directly).

**4 · Is the F-8 adjudication's reach right?** The operator settled that §35.1 constrains the
persistence surface, not the capability. That disposes of the collision with §8, §11 and §18, and
Plan does not reopen it. What remains open to you is **scope**: it is a rank-2 reading of rank-1
text. If §35.1's *"committare lavoro proprio"* cannot bear the fenced reading **as a matter of
text**, then rank 1 prevails and the reading is what gets revised — the record says so itself.

**5 · Is F-2's retraction sound?** I claim *"no branch on which a `WORK_COMMIT` was possible"* is
false because a WORK_COMMIT is bound to a branch, not a directory. That sentence was **canonical
in `main`**. Attack whether it was ever a claim about git at all, or about something narrower I
have flattened.

**6 · Does §17 actually withdraw everything §§2–15 assert?** The layering above is where this
package is most likely to hide something. Take any assertion from the historical sections and
check that §17.1 disposes of it. **A gap here is a real finding and I cannot see it from inside.**

**7 · Is the re-binding a revision 5?** See the lineage section. My judgement, contestable.

**8 · Is T10 still exhaustive, and does its term set see §8?** T10 is PRESERVED and re-run. The
`PREP` records that its five vocabulary terms **cannot** match §8's phrasing — so the sweep that
was the whole value of revision 3 was blind to the document that decides revision 4. Judge whether
T10 escapes the trap T7/T8 fell into or merely widens the same circle.

**9 · Are the measurements what I say they are?** `SMOKE-PLAN-PROVISION-001` (Plan can provision a
worktree it never writes into — PASS) and `CONTROL-PLAN-WORKCOMMIT-001` (a WORK_COMMIT in an
assigned worktree left the root byte-identical — PASS). Both are on **Plan's** surface. Neither is
`PROBE-ORCHWT-001` leg 3, and §17.3 says so; check that no part of the package leans on them as if
they were.

## What NOT to re-litigate unless the content moved it

`REV-ORCHSURF-MIRROR-001`'s T1–T6 passed for their stated reasons and revision 4 does not disturb
their subjects. Your §2 steelman, your Annex D.1 verification and your §7 three-surfaces PASS
stand — note that "three surfaces" is now **four concepts** in `roles/orchestrator.md`, because
SESSION HOME was the one the package never named. **B-1 is not withdrawn**: it found a real
contradiction between governed documents. What revision 4 changes is which document was defective.

## What is still owed, and is not Mirror's to grant

```
PROBE-ORCHWT-001 LEG 3   root non-perturbation, on the `orchestrator` surface, executed BY the
                         Orchestrator. Plan may not take it without writing into another actor's
                         worktree, which would corrupt what it measures. Legs 1, 2 and 4 are
                         discharged from durable state. Written 2026-08-17, never run until now
ORCHESTRATOR CAPABILITY  `WORK_COMMIT on own branch` was missing from roles/orchestrator.md while
                         branch `orchestrator` already carried 19 commits not on `main`. Revision
                         4 adds the row as UNVERIFIED. CONFIGURED != PROVEN, applied to the actor
                         that enforces it on others
PLAN CROSS-WORKTREE      `roles/plan.md`'s "attempt a cross-worktree write and confirm refusal"
                         remains UNVERIFIED. It was not authorised and was not attempted:
                         confirming a boundary by crossing it is not a measurement Plan takes on
                         its own initiative
REGRESSION SUITE         NOT re-measured at revision 4. Revision 3 recorded DELTA 0 against a
                         suite red at `main`. Revision 4 does not restate a number it did not take
ROOTGUARD                CAND-20260820-ROOTGUARD-001, deferred by the ratified record's §1 item 5.
                         Out of scope, and must not enter this candidate
```

## What this handoff does not do

It grants no approval and requests none from you. **It does not open the review** — that is
Orchestrator's under Annex C.3, and Plan does not open its own. It does not claim
`REV-ORCHSURF-MIRROR-001` is discharged by assertion; §17.1 carries a disposition per finding. It
asserts no verdict on the layering question at attack 6, which is the one I most want run.
`main` is UNCHANGED at `04693e68`, nothing has been canonicalized, and Plan does not execute in
any case — GATE 1 keeps proposer and executor distinct.
