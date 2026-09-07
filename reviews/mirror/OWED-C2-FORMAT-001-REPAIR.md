---
artifact: MIRROR format repair — appended, never an edit
record_id: OWED-C2-FORMAT-001-REPAIR
repairs: OWED-C2-FORMAT-001 (e528712b) — the seven records asserting (Annex C.2) without carrying it
actor_id: mirror
date: 2026-08-18
discipline: append-only. No original record is edited. Elements supplied here are supplied TODAY and
  say so; a contemporaneous element cannot be manufactured after the fact, and pretending otherwise
  would be the defect this repairs.
status: CLOSED — scope discharged
---

# Repair of the seven

Two kinds of defect were collapsed under one number. They need different repairs, and separating
them is most of the work.

## A · Two records are not reviews, and their own front matter said so

`REV-HASHDET-MIRROR-001` declares *"MIRROR **R4 verification report**"*.
`REV-HASHDET-MIRROR-003` declares *"MIRROR **final delta review**"* — a delta verification.

Both then appended `(Annex C.2)` to a class that is not a C.2 review. **The label was wrong, not the
artifact.** A verification report establishes whether stated properties hold; it has no author to
steelman and no thesis to falsify, and C.2's format does not fit it.

```
CORRECTED CLASS   MIRROR R4 verification report  — Annex C.2 NOT APPLICABLE
                  MIRROR delta verification      — Annex C.2 NOT APPLICABLE
```

Their content stands unchanged and their findings are unaffected.

## B · Five are reviews and owe elements

| Record | Missing | Supplied below |
|---|---|---|
| `REV-C9-STATE-MODEL-003` | STEELMAN | § B.1 |
| `REV-HASHDET-MIRROR-002` | falsifier · author response | § B.2 |
| `REV-ORCHWT-MIRROR-001` | all three | § B.3 |
| `REV-P51C9-MIRROR-001` | falsifier · author response | § B.4 |
| `REV-P51C9-MIRROR-002` | all three | § B.5 |

**Supplied on 2026-08-18, after the fact, and marked as such.** A steelman written today for a
review completed days ago is a real steelman and is not a contemporaneous one. Recording which it is
costs a sentence; concealing it would reproduce the defect being repaired.

### B.1 · `REV-C9-STATE-MODEL-003` — STEELMAN

Revision 3 answered both blocking findings at the level of the model rather than the wording, and
two of its answers were better than what the review had asked for: `field scoped by record` is a
cleaner unit than the granularity rule I proposed, and §6.1's resolver contract added a
no-self-reference clause I had not thought to require. It also entered its own prior defect into its
evidence table as instance 10 rather than quietly correcting it.

`AUTHOR_RESPONSE: PENDING_OPERATOR_ROUTING` · `WHAT_WOULD_CHANGE_MY_MIND` already present.

### B.2 · `REV-HASHDET-MIRROR-002` — falsifier and author response

`WHAT_WOULD_CHANGE_MY_MIND` — a derivation of `1ef68cc0…` from a committed object in this repository
would have made §8's `12d8f4b1…` a live value rather than revision 1's; and a suite defining five
tests rather than seven would have made the `5/5` figure current rather than stale.

`AUTHOR_RESPONSE: PENDING_OPERATOR_ROUTING`.

### B.3 · `REV-ORCHWT-MIRROR-001` — all three

**STEELMAN.** The candidate quotes the text that resists it before the text that supports it —
§8, §0.2, §47 before D.1 and §14 — which is the inversion the earlier finding asked for. It abandons
Option A honestly rather than reinterpreting §8 to reach it, conceding that a chat's session
location and its filesystem boundary are the same concept in this deployment. It is also the
tightest candidate of the three: one content file, zero fingerprint movement.

**WHAT_WOULD_CHANGE_MY_MIND.** A reading under which §8's residence clause and the deployment
profile's `Worktree` column name different concepts, making Option A available and the divergence
unnecessary; or evidence that the Orchestrator did have a branch on which a `WORK_COMMIT` was
possible, which would remove the defect the candidate exists to correct.

`AUTHOR_RESPONSE: PENDING_OPERATOR_ROUTING`.

### B.4 · `REV-P51C9-MIRROR-001` — falsifier and author response

`WHAT_WOULD_CHANGE_MY_MIND` — for F-1, a demonstration that the two content changes share a blast
radius, which would make the single candidate correct; for F-2, a clause reconciling the worktree
change with §8 that I read past; for F-3, the three cited oids resolving in a fresh clone.

`AUTHOR_RESPONSE: PENDING_OPERATOR_ROUTING`.

### B.5 · `REV-P51C9-MIRROR-002` — all three

**STEELMAN.** Revision 2 closed F-1 by moving the change out on a **new commit** rather than by
rewriting history — the only method that does not orphan what the previous revision already cited —
and closed F-3 beyond the finding, adding blob identity on the reasoning that a commit oid is
reachability-dependent and a blob is not. That repairs the mechanism, not the instance.

**WHAT_WOULD_CHANGE_MY_MIND.** Any content path in `git diff 908197b b5eaf81e` beyond the two named;
a source commit failing `merge-base --is-ancestor`; or the hash failing to reproduce under HASHDET
r3 tooling from a third checkout.

`AUTHOR_RESPONSE: PENDING_OPERATOR_ROUTING`.

---

## What this repair does not claim

The five reviews' **verdicts are unchanged** — no finding, disposition or binding is revisited, and
supplying a steelman after the fact does not re-open a review that was decided without one written
down. What changes is that the records now carry the format they asserted, with the date of supply
visible.

The two reclassified records lose a label they should not have carried and keep everything else.

**Scope discharged: 7 of 7.** The register `OWED-C2-FORMAT-001` closes with this record, and the
count that was derived twice from two definitions is now the count repaired.
