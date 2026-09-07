---
artifact: MIRROR final delta review (Annex C.2)
review_id: REV-HASHDET-MIRROR-003
candidate: CAND-20260817-HASHDET revision 3
content_hash: c85acdb2d3e55f71bed9aa985ff996fdcfdd5b43c4b1e097c3b6063b80ad05d8
base_head: 908197ba62a064546f17c9c277ff497ffc753656
branch_tip: b9af54ebe2fd24d94ec0eee71fcb064797922082
remediates: REV-HASHDET-MIRROR-002 (7cd8b397, REQUEST CHANGES, F-1)
reviewer: mirror
adjudicator: operator
level: R4 / DELTA_REVIEW
review_date: 2026-08-17
verdict: ACCEPT
scope: delta review of the remediation only — no implementation, no modification, no authorisation
---

# MIRROR FINAL DELTA REVIEW — CAND-20260817-HASHDET r3

```
candidate  CAND-20260817-HASHDET
revision   r3
reviewer   mirror
level      R4 / DELTA_REVIEW
verdict    ACCEPT
```

---

## 1 · DELTA VERIFIED

**Scope of the revision is exactly what was declared.** Two files changed since the r2 tip:
`governance/candidates/CAND-20260817-HASHDET.md` and `learning/plan/SLR-plan-0002.md`. The script,
the test suite and `plan_defined_parameters.md` are **byte-untouched** — verified per file, not
inferred from a summary.

**F-1 is closed.** The §8 verification record now describes r3 throughout:

| Row | r2 (defective) | r3 (verified by me) |
|---|---|---|
| Candidate hash | `12d8f4b1…695c61` (r1's value) | `c85acdb2…ad05d8` ✅ |
| Determinism suite | `5/5 PASS` | `7/7 PASS` ✅ |
| Suite can fail | `1/5 — 4 failures` | `2/7 — 5 failures` ✅ |

**Hash consistency sweep — clean.** Every hash token in the document, classified:

```
c85acdb2  r3, current            ×5   consistent at every site
12d8f4b1  r1                     ×1   SUPERSEDED_HASHES … "— DO NOT REVIEW"
1ef68cc0  r2                     ×1   SUPERSEDED_HASHES … "— DO NOT REVIEW"
c39ecae8 / f325bd9d / 280dc497 / b4e7c493   other objects, each labelled with its object
```

No intermediate value survives unmarked. Both prior HASHDET hashes are collected in one
`SUPERSEDED_HASHES` field carrying an explicit `DO NOT REVIEW`, which is a better shape than
scattering annotations at each site.

**Domain counts are the derived ones.** The manifest states *"506 included · 12 excluded, as
produced at this tip"*; the command at tip `b9af54eb` returns **506 / 12**. Exact.

*(The `505 included` figure named in the mandate is the count at the r2 tip `153b35da` — I
confirmed it there. The SLR added one content entry, taking it to 506. The committed document
carries the value for the tip it declares, which is the correct one.)*

**Binding verified, and the invariance claim holds.** Hash at the declared tip `b9af54eb` =
`c85acdb2…ad05d8` = declared. Hash at the branch head `6422e22`, which adds only the manifest
commit, is **identical** — the manifest is control plane and does not perturb the object, exactly
as claimed.

**SOURCE_COMMITS coherent.** Three commits — `b2c326b5`, `153b35da`, `b9af54eb` — all resolve, all
are ancestors of the declared tip, and the r3 commit is present. No orphaned oid of the kind that
appeared in the C-9 lineage.

**Regression — none.** Recomputed independently from `hash-determinism`:

```
GOV311  tip 9720a0cd → c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239  unchanged
P51C9   tip b5eaf81e → f325bd9d1667638eeda718b73bc106263fea3a509f832bcc62e082cdba0651da  unchanged
ORCHWT  tip ab4856b1 → 280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d  unchanged
main    908197ba…, ancestor of the branch, 6 commits behind it                            unchanged
```

**SLR — correctly a learning, and it stops there.** `SLR-plan-0002` declares
`curation: PENDING — E.2 gives epistemic curation to Mirror. The class below is proposed, not
self-certified.` That is the right posture: Plan records the pattern and does not assign it a
class it lacks the authority to assign.

The pattern itself is well drawn and, notably, is **not** filed lazily under an existing branch —
it argues that it is neither (A) nor quite (B), and lands on *"the verification record is a claim
about the object, stored inside the object"*, which is C-9 §7's fixed point one level down. The
self-diagnosis is the part worth keeping: *"I re-ran the reproduction and got the r2 value. I
re-ran the suite and got 7/7. Both checks passed — and neither compared its result against what the
document said."*

**No implementation was shipped with it.** The proposed habit stayed a habit: no new script, no new
test, no gate. The only trace in the candidate is one verification row recording that the check was
performed. That is the correct boundary for a learning under a review hold.

---

## 2 · REMAINING BLOCKERS

**None.**

---

## 3 · NON-BLOCKING OBSERVATIONS

**N-1 · my sweep produced four false positives and I report them.** My classifier flagged
`c39ecae8`, `280dc497`, `f325bd9d` and `b4e7c493` as unmarked stale values. They are not HASHDET
values at all — they are the approved GOV311 hash and the two pending candidates', plus ORCHWT
computed under v4 as a deliberate contrast, each correctly labelled with its object. My heuristic
looked for supersession language on the same line and mistook "belongs to another object" for
"unmarked". Corrected before it reached a finding.

**N-2 · two live candidates now carry different hash versions, and that is the fix working.** This
manifest declares `legend-candidate-v3` because the branch is cut from `main`; P51C9's tip carries
`v4`. Before the repair this would have been a contradiction — one script, one ambient rule. Now
each candidate is hashed under the governance its own tip carries, so both are simultaneously
correct. Recorded as a property that has become observable, not as an issue.

**N-3 · first observable instance of `learning/` behaving as content.** Adding `SLR-plan-0002` moved
the included count 505 → 506 and therefore moved the candidate hash. That is exactly what
`CLASS-P51-REVIEWS-LEARNING-001` determined and what §18 requires — a learning record is proposed
for canonical integration and must move the hash when it changes. The determination now has a
worked case.

**N-4 · the four non-blocking items from R2 persist and were correctly out of scope.** The
duplicated serialization expression in `serialize_domain`/`compute`; `$(…)` stripping the last byte
of the emitted representation; `test_historical_replay` not discriminating in a v3 checkout; the
implicit encoding in P5.2. None was in this revision's mandate and none was touched. They remain
recorded against the candidate rather than closed.

---

## 4 · FINAL DISPOSITION

```
MIRROR_REVIEW: ACCEPT

CANDIDATE  CAND-20260817-HASHDET revision 3
HASH       c85acdb2d3e55f71bed9aa985ff996fdcfdd5b43c4b1e097c3b6063b80ad05d8
BASE       908197ba62a064546f17c9c277ff497ffc753656
TIP        b9af54ebe2fd24d94ec0eee71fcb064797922082
DATE       2026-08-17     REVIEWER  mirror

F-1 (verification record stale)   CLOSED — every row now describes r3
Hash consistency                  CLEAN — no unmarked intermediate value
Domain counts                     DERIVED — 506 / 12, matching the command
SOURCE_COMMITS                    COHERENT — three commits, all ancestors, r3 present
Regression                        NONE — GOV311, P51C9, ORCHWT and main all unchanged
SLR                               correctly a proposed learning; no implementation shipped
```

`ACCEPT` is on the remediation as measured against `REV-HASHDET-MIRROR-002`, and it inherits the
substantive verdict of that review: the three original blockers — determinism, working-tree rule
leakage, and silent hashing of a tip without the rule — were verified closed there by independent
re-execution and mutation testing, and nothing in r3 touches the code that closed them.

Four non-blocking observations stand open (N-4). They are recorded, not waived: `ACCEPT` means no
change is required before `HUMAN_APPROVAL`, not that nothing remains worth doing.

**This review does not authorise execution.** `GATE 0` still cannot pass — root unclean, no lease,
L2 suspended — and the candidate says so itself. The final decision is the operator's. No file of
the candidate was touched, no governance modified, no gate executed; all recomputation ran in a
disposable clone outside the repository.

---

## Appended 2026-08-18 — where this record's C.2 elements live

🔴 **The `(Annex C.2)` label in the text above is wrong.** `OWED-C2-FORMAT-001-REPAIR` **§ A** reclassifies this record as a **MIRROR delta verification**, for which **C.2 is NOT APPLICABLE**. Findings unaffected.

Appended, not edited. The original text above is unchanged.
