---
artifact: ADVERSARIAL REVIEW — LEGEND Operating Convention v1, integrated object (§ A + § B + Appendix D)
record_id: REV-OPCONV1-MIRROR-001
object_under_review: framework/protocols/legend_operating_convention_v1.md
object_blob: 27587908dde910f8cc2428fcf78bec26457e2178
object_commit: 1562ed6 @ plan-orchsurf-r4-transcription, committed 2026-08-23T16:25:07Z
reviewer_seat: mirror
authoring_session: mirror-87 [103de0] · transcript birth 2026-08-23T15:11:17Z
authored_on: 2026-08-23 (UTC)
governance_version: 3.1.1 (read at `main`, not exercised)
mode: ADVERSARIAL_REVIEW

STATUS: REVIEW_DELIVERED
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

binding_note: >
  This review binds the BLOB, per the object's own B.4 H-1. It reviews 27587908…, not the branch
  tip, and N-4 is about exactly why that distinction earns its place.

conflict_of_interest: >
  🔴 DECLARED. § A.9, B.2.2 and parts of B.9 rest on evidence this session produced; B.2.2 names
  the finding explicitly. Under C.3 this session is not the sole adversarial check on those, and
  N-3 below CORRECTS this session's own prior sequencing claim rather than defending it.
  mirror-75 remains the independent second check on § A.3 / § A.7 / § A.8 / § A.9.

verdict_note: >
  Per-axis verdicts use Annex C.2's enum. NO DOCUMENT-LEVEL DISPOSITION IS EMITTED, for the reason
  N-2 gives: the governed gate-bearing token is D.2's `MIRROR_REVIEW: n/a | PASS | FAIL`, and this
  convention does not yet provide a field to carry it.
---

# ADVERSARIAL REVIEW — OPERATING CONVENTION v1, INTEGRATED OBJECT

> **This is a good document and most of it holds.** B.8.2 (the compatibility claim that cannot be
> made), B.9's load-bearing-fact table, B.10's proposal register, and B.4 H-1 are better than what
> they replace. **The A.9.1 correction is complete, not cosmetic** — verified below.
>
> **Four findings. One is the answer to "can an author change what is hashed by choosing a class",
> and the answer is yes. One corrects this reviewer's own earlier work.**

---

## 0 · THE COORDINATOR'S CORRECTION — VERIFIED COMPLETE

Asked to check whether the S.11/A.9.1 fix is complete rather than cosmetic. It is complete.

```bash
git show main:governance/plan_defined_parameters.md | sed -n '11p'
# change_class: MAJOR — these values are governance; changing them follows gate 3
git show main:governance/GOVERNANCE_v3.1.1.md | grep -n "GATE 3"
# 244: GATE 3 — MAJOR. Plan candidate → Mirror hostile review → MIRROR PASS →
#      HUMAN_APPROVAL (oggetto in coda, J.3) → commit … APPROVAL ≠ AUTHORIZATION (E4)
```

A.9.1 states the gate, states that A.6's `modifica governata` **is** that path rather than an
exemption from it, splits `Plan MAY prepare` from `Plan MAY NOT perform`, and P-6 in B.10 carries
the same split into the proposal register. The correction propagated to both places it had to.

**This reviewer's share of the error is recorded here.** The original finding was mine, and I wrote
that the recalibration *"needs no new governance"*. That sentence is true and it stops one clause
early: I read A.6's `RECOVERY: Plan ricalibra … (modifica governata)` and never pursued *modifica
governata* to the gate it names. The coordinator escalated my phrasing to *"consumes no operator
decision"*, which is false — but the clause I left unopened is what made the escalation available.

---

## N-1 · 🔴 ONE CLASS, BOTH HASH DOMAINS — AND THE AUTHOR CHOOSES WHICH

**AXIS: hidden governance change · VERDICT: REFUTED** — this is the headline

B.1.1 clause 2: *"CLASS declares DOMAIN — CONTENT or CONTROL_PLANE — explicitly, in the artifact."*

B.1.2 rows 6 and 7, DOMAIN column: **"follows its root."**

Those are not the same rule, and the second is the true one. Domain is a property of the **path**
(P5.1: three roots; everything else is content), computed by `candidate_content_hash.py` from the
prefix. An artifact's declaration transcribes it and cannot change it. So for two of seven classes,
the table concedes that the class does **not** declare the domain — its container does.

**Measured, across 43 heads, class by class:**

```
HANDOFF          (class 6)   7 CONTROL_PLANE   ·   5 CONTENT
  control plane:  governance/candidates/HANDOFF-{GOV311-ORCHESTRATOR, ORCHSURF-MIRROR,
                  P5DOMAIN-MIRROR, SCIENTIST-AB-SPEC, SUNSET-DECISION3, XPORT-MIRROR}.md
                  reviews/mirror/HANDOFF-CANDIDATE-READINESS-001.md
  content:        learning/mirror/HANDOFF-{MIRROR-PERSISTENCE…, ROLE-CONTRACTS-001}.md
                  learning/plan/HANDOFF-{20260822-ROLE-CONTRACT-REPAIR, 20260823-SURFACE-MAP…}.md
                  runtime/handoff/C-2/HANDOFF-C-2-PMID42422765.md

WORKING RECORD   (class 7)  15 CONTROL_PLANE   ·  64 CONTENT
                  (AUTHOR-RESPONSE · SLR- · PROPOSAL- · PREP- · ADVISORY- · DELTA-)
```

🔴 **Class 7's own row names two roots that sit in opposite domains** — `learning/<actor>/`
(content) and `reviews/<actor>/` (control plane). An author writing a working record therefore
decides whether it enters `CANDIDATE_CONTENT_HASH` **by choosing between two paths the same row
permits, without changing class.** Fifteen artifacts are already on the excluded side, all six
`AUTHOR-RESPONSE-*` among them.

That is the question this review was pointed at, and the answer is yes. It is also the exact defect
the surface analysis recorded as *"same self-declared kind, opposite hash-domain behaviour, decided
by directory alone"* — and B.1.3 now declares HANDOFF's five roots **conformant** under B.1.2's
author-root rule. **The taxonomy written to end the container-vs-class conflation ratifies it for
two of its seven classes**, and B.1.3's own headline says the defect *"is one directory"* when it is
measurably three.

**MINIMUM FIX — the reversible half, not the migration:**
1. restate clause 2 truthfully — *"PATH declares DOMAIN; the artifact transcribes it, and a
   transcription that disagrees with the path is a finding"* — which is what the § A source's own
   `domain:` error demonstrated at n=1;
2. add one validator rule to Appendix D.2: **a class whose instances span both domains is reported**.
   That does not move a file, does not amend P5.1, and turns an invisible author-controlled lever
   into a printed line.

Relocation stays where B.1.4 correctly put it — migration, not convention.

---

## N-2 · THERE ARE THREE VERDICT AXES, AND THE ONE THAT GATES MAJOR WORK IS THE ONE NOT PROVIDED

**AXIS: internal consistency · VERDICT: REFINED**

B.2.2 names two axes — DISPOSITION (`ACCEPT | REQUEST CHANGES | BINDING VERIFIED`) and C.2 VERDICT —
and B.2.3 mandates the two fields `verdict:` and `c2_verdict:`. Both are real. **A third exists, is
governed, and is the only one a FROZEN gate consumes:**

```bash
git show main:governance/annex_d_commit_batch.md | grep -n MIRROR_REVIEW
# 38: MIRROR_REVIEW: n/a | PASS | FAIL + REVIEW_ID
```

GATE 3 (body § 244) requires **MIRROR PASS**. D.2's manifest field carries `PASS | FAIL`. Neither
token appears in B.2.3's disposition set. **A review written exactly to this convention cannot fill
`MIRROR_REVIEW` and cannot satisfy GATE 3**, unless an `ACCEPT → PASS` mapping exists — and no such
mapping is declared anywhere, here or in the annexes.

This refines rather than repeats the earlier finding: the earlier one said *two axes, one declared*.
Measured, it is **three axes, and the convention transcribed the two that gate nothing.**

**MINIMUM FIX:** a third field, `mirror_review: PASS | FAIL | n/a`, populated for reviews of objects
that will pass a gate — or a declared mapping, recorded where a validator can read it. Without one,
N-3 has no exit.

---

## N-3 · P-6 IS DOWNSTREAM OF P-2, AND THIS CORRECTS MY OWN SEQUENCING

**AXIS: ordering · VERDICT: REFINED** · ⚠️ corrects this reviewer's prior finding

A.9's sequencing conclusion — recalibrate **before** correcting `plan_defined_parameters.md` — is
right and I stand behind it. **It is not the whole order, and the missing half is mine.**

Trace P-6 through the gate A.9.1 correctly identifies:

```
P-6  →  Plan CAND
     →  Mirror hostile review
     →  MIRROR PASS            ← D.2 vocabulary. No review in the repository emits it (N-2).
     →  HUMAN_APPROVAL, "oggetto in coda, J.3"
                               ← the queue with NO DECLARED WRITER, forked into 3 lineages,
                                 which is B.3.2 and P-2 of this same document.
     →  commit
```

**P-6 terminates in the surface P-2 exists to repair.** The recalibration cannot complete until the
approval queue has a declared writer. So the true order is:

```
P-2 (queue writer)  →  N-2 (a token that can carry MIRROR PASS)  →  P-6 (recalibrate)
                    →  only then, any correction to plan_defined_parameters.md
```

I originated *"recalibrate first"* and presented it as unblocked. It is not first; it is fourth.
B.8.3's *"Recalibrate first (P-6), then correct"* inherits the same incompleteness and should carry
the dependency explicitly, since a reader of B.8.3 alone would schedule P-6 as available work.

**MINIMUM FIX:** B.10 gains a dependency column, and P-6's row reads `depends on P-2, N-2`.

---

## N-4 · THE OBJECT PREDATES THE CORRECTIONS ITS CHANGELOG ANNOUNCES — BY TWO MINUTES

**AXIS: process integrity · VERDICT: CONFIRMED** (a race, not a regression — and the distinction was measured, not assumed)

The integrated object does **not** contain the second limb of § 0.1, the escalation floor, S.8.2, or
the three 🟡 limb-2 markings, all of which were reported to this seat as accepted.

```
integrated § 0.1 (line 64–68)   the single limb only — "would anything become PERMITTED…"
integrated B.6.1 (line 597)     "Escalate if and only if"        ← a biconditional, i.e. a ceiling
integrated B.6.2 (line 623)     "seat designation for one mandate"  ← the pre-clearing clause
integrated 🟡 markings           1 occurrence, the generic preamble at line 48. Zero limb-2 marks.
```

**My first reading of this was that the integration dropped a reviewed correction. That reading is
wrong, and the timestamps are what refuted it:**

```
cebca20  2026-08-23T16:14:59Z   § A source r1     ← what Plan integrated
1562ed6  2026-08-23T16:25:07Z   the integration
ce2dc6e  2026-08-23T16:27:14Z   § A source r2     ← carries S.8 as a floor, S.8.2, the limb-2 marks
git merge-base --is-ancestor ce2dc6e 1562ed6  →  NO
```

r2 landed **2m07s after** the integration and is not in its history. **Nobody dropped anything.**
Plan integrated the only revision that existed. Had I reported this on the natural reading, I would
have accused an integrator of losing a fix that had not yet been written, on a two-minute margin.

What survives is not an accusation and still matters: **the changelog describes a document that does
not exist.** The object is LINT-green, link-tested, and offered as reviewable, and at this blob § 0.1
still carries the single blind limb. Adopted at `27587908…`, M-2 is unfixed in the adopted text.

🔴 **And the convention already contains the rule that prevents this, applied to the wrong
direction.** B.4 H-1: *"A HANDOFF BINDS BY BLOB, NOT BY BRANCH TIP … a branch tip may sit ahead of
the content that was reviewed. Earned: a handoff bound a revision its own addendum had superseded."*
The same hazard just recurred source→integration, where H-1 does not reach.

**MINIMUM FIX:** extend H-1 to every integration and every review — *an integration declares the
blob of each source it consumed; a review declares the blob it reviewed; a correction reported as
accepted names the blob it landed in.* One line, and the two-minute race becomes visible instead of
requiring a timestamp forensics pass to detect.

---

## 5 · SUMMARY

| # | finding | axis verdict | locus | minimum fix |
|---|---|---|---|---|
| N-1 | 🔴 one class spans both hash domains; class 7's row lets the author pick — HANDOFF 7/5, WORKING RECORD 15/64 | REFUTED | B.1.1 cl.2, B.1.2 rows 6–7, B.1.3 | restate clause 2; validator reports a class spanning domains |
| N-2 | three verdict axes; D.2's gate-bearing `PASS\|FAIL` is the one omitted | REFINED | B.2.2, B.2.3 | `mirror_review:` field, or a declared mapping |
| N-3 | ⚠️ P-6 terminates in the queue P-2 repairs; my "recalibrate first" was incomplete | REFINED | A.9, B.8.3, B.10 | dependency column; P-6 depends on P-2, N-2 |
| N-4 | the object predates r2 by 2m07s; § 0.1's second limb is absent from the reviewed blob | CONFIRMED | § 0.1, B.6.1, B.6.2 | extend B.4 H-1 to integrations and reviews |

**Holds, and I would not re-litigate:** B.1.4's refusal to relocate · B.2.3's non-retroactivity ·
B.3.2 declaring the writer gap and stopping · B.4 H-1 · B.5 R-2/R-5 · B.8.2 · B.9's load-bearing
table · B.10 as a register · B.11.

**What this review did not do:** did not decide anything · did not activate anything · did not
modify frozen text · did not emit a document-level disposition (N-2) · did not review Appendix D
beyond D.2's validator surface, which N-1 touches · did not commit itself · did not touch the
object, which lives on another seat's branch and was read through `git show`.

END OF REVIEW.
