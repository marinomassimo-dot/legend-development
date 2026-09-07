---
artifact: MIRROR hostile review (Annex C.2)
review_id: REV-P51C9-MIRROR-002
candidate: CAND-20260817-P51C9 revision 2
content_hash: f325bd9d1667638eeda718b73bc106263fea3a509f832bcc62e082cdba0651da
base_head: 908197ba62a064546f17c9c277ff497ffc753656
branch_tip: b5eaf81ed50b3c994c6ee7cede47a2114cdcaa6c
remediates: REV-P51C9-MIRROR-001 (fe08e685, REQUEST CHANGES, F-1 · F-2 · F-3)
reviewer: mirror
adjudicator: operator
level: R4 / MIRROR_REQUIRED
review_date: 2026-08-17
verdict: ACCEPT
scope: candidate review only — no content modified, no execution authorised, GATE 0 / approval / batch / merge not evaluated
---

# MIRROR HOSTILE REVIEW — CAND-20260817-P51C9 r2

```
candidate  CAND-20260817-P51C9 revision 2
reviewer   mirror
level      R4 / MIRROR_REQUIRED
verdict    ACCEPT
```

All six mandated checks pass on independent verification. Every value below was recomputed or
re-derived here; none is taken from the candidate's own declaration.

---

## 1 · Scope integrity — **CONFIRMED**

`deployment/deployment_profile.md` is **absent** from the change set `908197b → b5eaf81e`. No
ORCHWT file, commit or hash participates: `git diff -- deployment/` returns **0 files**, and the
worktree wording of the split-out change appears **0 times** in the candidate tree.

**Content radius: two files.** `governance/plan_defined_parameters.md` (the P5.1 amendment) and
`learning/plan/SLR-plan-0001.md`. Everything else in the change set is control plane
(`governance/candidates/`, `ledger/`) and does not enter the domain.

**F-1 is closed, and closed forward.** The commit that does it — *"Split F-1: the deployment change
leaves this candidate, forward and not by rewrite"* — is itself the declared tip. The split was
performed by moving the change out on a new commit rather than by rewriting history, which is the
only method that does not orphan what the previous revision already cited.

## 2 · Provenance — **CONFIRMED, and repaired beyond what F-3 required**

All six `SOURCE_COMMITS` verified individually: each exists, each passes
`git merge-base --is-ancestor <oid> b5eaf81e`, and each carries its full 40-character oid.

```
0d9519bf70…  63e34c7b03…  59fd5f55e1…  488d459951…  629bc89ac6…  b5eaf81ed5…
```

These are exactly the in-history oids I identified in F-3 as the correct replacements for the four
orphaned ones. **No orphan lineage is presented as active provenance**, and §2 states plainly what
F-3 was: the four cited at revision 1 *"resolve as objects and none is an ancestor of the branch
tip — the pre-rebase forms of rows 1–4, orphaned when the branch was realigned."* The defect is
recorded rather than quietly corrected.

**The repair exceeds the finding.** §2 adds blob identity for the three referenced artifacts,
because *"a commit oid is reachability-dependent; a blob hash is not."* All three verified against
the declared tip:

```
governance/plan_defined_parameters.md              09bd9e03170d50d66b8750f37fd5b534f37f1fa2  MATCH
governance/candidates/PROPOSAL-C9-STATE-MODEL.md   d2ada5bc13152d8552048f6cdac9b3ef5c66e4fb  MATCH
learning/plan/SLR-plan-0001.md                     c8fa683379d7822620cd6f7643568d37e60a9e72  MATCH
```

That closes the *mechanism* of F-3, not only its instance: a future rewrite cannot orphan a blob.

## 3 · Manifest consistency — **CONFIRMED**

Full sweep of every hash, tip, base, count and commit token:

| Token | Role | Occurrences | State |
|---|---|---|---|
| `f325bd9d…0651da` | candidate hash | 6 | current at every site |
| `b5eaf81e…` | declared tip | 8 | current |
| `908197ba…` | BASE_HEAD | 2 | current, = `main` |
| `b1f3729b…` | revision 1 hash | 2 | `SUPERSEDED_HASH`, explicitly marked ✅ |
| `629bc89a…` | revision 1 tip | 2 | **not** stale — it is source-commit row 5 and a verified ancestor |

**Domain counts are derived and correct.** The manifest states *"505 included · 19 excluded, as
produced by the command at this tip"*; the command at `b5eaf81e` returns **505 / 19**. Exact. §1
also records that my revision-1 figures (504 / 17) *"are exactly right at the tip it reviewed"* —
which is the honest way to supersede a number rather than to contradict it. N-1 of my prior review
is addressed by deriving instead of copying.

## 4 · P5.1 classification — **CONFIRMED**

At the declared tip:

```
CONTROL_PLANE_ROOTS:
- governance/candidates/
- ledger/
- reviews/
```

`reviews/` added ✅ · `learning/` **not** a root, therefore content ✅ · `runtime/` **not** a root,
remaining an open question ✅ · exactly three roots, **no additional root introduced** ✅.

## 5 · HASHDET replay — **CONFIRMED**

Recomputed in a disposable clone checked out at `hash-determinism` (`6422e22`), so the tooling is
HASHDET r3 **only** and no part of the candidate's own branch supplied the script:

```
run 1   f325bd9d1667638eeda718b73bc106263fea3a509f832bcc62e082cdba0651da
run 2   f325bd9d1667638eeda718b73bc106263fea3a509f832bcc62e082cdba0651da
manifest f325bd9d1667638eeda718b73bc106263fea3a509f832bcc62e082cdba0651da
```

**Tip invariance verified.** The branch head is four commits beyond the declared tip. I checked all
four: every one touches only `governance/candidates/` or `ledger/`, and the hash at each is
**identical** to the hash at `b5eaf81e`. The declared tip therefore still describes the branch's
content.

## 6 · Regression — **NONE**

Recomputed with the same r3 tooling:

```
HASHDET r3  tip b9af54eb → c85acdb2d3e55f71bed9aa985ff996fdcfdd5b43c4b1e097c3b6063b80ad05d8  unchanged
ORCHWT      tip ab4856b1 → 280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d  unchanged
GOV311      tip 9720a0cd → c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239  unchanged
main                      → 908197ba62a064546f17c9c277ff497ffc753656                          unchanged
```

---

## 7 · The two points the candidate flagged rather than decided

Plan declined to resolve two readings and asked the reviewer to confirm them. Declining was
correct; here are my readings.

**7.1 · `SLR-plan-0001.md` inside the candidate — the inclusion is sound.** Body §18 prescribes
that a learning record reaches durable state *"via WORK_COMMIT … o inclusione nel prossimo
candidate."* Inclusion in a candidate is the frozen text's own route, not an exception to it.
Operator decision 4 excluded *the Orchestrator's two SLRs* pending curation; this record is Plan's
own and postdates that decision, so Plan's reading is textually supported. And the record does not
pre-empt my authority: it carries `curation: PENDING — the confirmation classes are proposed by the
author and are not self-certified`. It is also the first artifact placed under the `learning/` =
content declaration and moves the hash exactly as that declaration requires — the classification
demonstrating itself. **Not a blocker.** Decision 4 was the operator's, so its scope remains the
operator's to state; my finding is only that the candidate does not contradict it.

**7.2 · The ORCHWT references in §3 — not inclusion.** The mandate asks that no ORCHWT *content,
commits, hashes or runtime authority changes* be included, and none is: 0 files, 0 commits, 0
hashes, verified. §3's references are narrative, recording where the split content went. Removing
them would leave the manifest showing content absent with no account of why — which is worse. **I
confirm Plan's reading.**

## 8 · Non-blocking observations

**N-1 · two false positives of my own, reported.** My token sweep flagged `629bc89a` as an unmarked
stale value: it is source-commit row 5, a verified ancestor, and legitimately current. It also
flagged three 40-hex tokens as unresolvable commits; they are **blobs**, correctly labelled as such
in the blob-identity table. Both were my regexes assuming every 40-hex string is a commit oid.
Caught before either became a finding.

**N-2 · the declared tip trails the branch head by four commits.** All four are control plane and
the hash is invariant across them — verified, not assumed. A reader comparing `BRANCH_TIP` to the
branch will see a divergence and should know it is by construction.

**N-3 · items carried from my revision-1 review remain open**, correctly outside this revision's
scope: `reviews/` is a third unbounded prefix root; `runtime/`'s interim safety is conditional on
staying untracked and nothing enforces it; `legend_lint.py` still has zero coverage of
`governance/`, so none of this class of defect is machine-detectable.

**N-4 · F-2 travelled with the change it concerned.** My revision-1 F-2 — that the Orchestrator
worktree change cites §8's obligation and omits §8's location — belongs to `CAND-20260817-ORCHWT`,
whose manifest addresses it. It was not silently dropped, and it is out of scope here.

---

## 9 · FINAL DISPOSITION

```
MIRROR_REVIEW: ACCEPT

CANDIDATE  CAND-20260817-P51C9 revision 2
HASH       f325bd9d1667638eeda718b73bc106263fea3a509f832bcc62e082cdba0651da
BASE       908197ba62a064546f17c9c277ff497ffc753656
TIP        b5eaf81ed50b3c994c6ee7cede47a2114cdcaa6c
DATE       2026-08-17     REVIEWER  mirror

F-1 scope contamination      CLOSED — deployment change split out, forward, not by rewrite
F-2 §8 reconciliation        DEPARTED with ORCHWT; out of scope here
F-3 orphaned provenance      CLOSED — six ancestors verified, plus blob identity
Scope integrity              CONFIRMED — two content files, one coherent radius
Manifest consistency         CONFIRMED — no unmarked historical value; counts derived
P5.1 classification          CONFIRMED — three roots, runtime/ still open
HASHDET replay               CONFIRMED — twice, r3 tooling, independent checkout
Regression                   NONE — HASHDET r3, ORCHWT, GOV311, main all unchanged
```

**No blockers remain.**

🔴 **`ACCEPT` is a review outcome only and does not authorise execution.** It states that I found no
defect requiring change before the candidate is put to the operator. It is not an approval, not a
`GATE 0` assessment, not a batch authorisation and not a merge. Those were excluded from this
mandate and I did not evaluate them; `HUMAN_APPROVAL` and every gate remain untouched and pending,
and the decision is the operator's alone.

No file of the candidate was modified, no governance changed, no gate executed. All recomputation
ran in a disposable clone outside the repository; this worktree is clean.

---

## Appended 2026-08-18 — where this record's C.2 elements live

All three obligatory elements were missing and are supplied in `OWED-C2-FORMAT-001-REPAIR` **§ B.5**, written on 2026-08-18 and marked there as after-the-fact.

Appended, not edited. The original text above is unchanged.
