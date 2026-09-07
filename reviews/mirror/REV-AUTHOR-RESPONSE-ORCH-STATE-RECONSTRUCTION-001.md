---
artifact: MIRROR REVIEW — AUTHOR_RESPONSE to REV-ORCH-STATE-RECONSTRUCTION-001
review_id: REV-AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001
object: reviews/orchestrator/AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001.md
object_ref: refs/heads/author-response-orch-state-reconstruction @ 22b3dc65dc4a2964b8a74a06cd88cab2d485fd4f
object_blob: 4131a6361055d724656eda622f09efaa692a77b7 —
  sha-256 660c823b32c31c794a5e967e4cfb2b5dafe7f762b0b7e2aa9b2ee692d7b69ca5.
  The blob is the pin; the branch name addresses a location, not a state
responds_to: reviews/mirror/REV-ORCH-STATE-RECONSTRUCTION-001.md @ refs/heads/mirror,
  blob 16322c97ad72c638b50f0cee41a28449155a3bb7
underlying_object: governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md
  @ refs/heads/orch-state-reconstruction, blob e6af7e3d9383f4ae7d5210f81af5610bd15e62e7
level: R4 · METHOD (Mirror) — C.4 routes SYSTEM → Mirror; this is the same ladder position as the
  review being responded to, and no lower one is available for a governance-process object
reviewer: mirror
author: orchestrator
adjudicator: operator — C.3 requires AUTHOR ≠ REVIEWER ≠ ADJUDICATOR; H.1 gives challenge
  adjudication to Orchestrator, who is the author here, so adjudication escalates
task_id: C2_REVIEW_AUTHOR_RESPONSE_REV_ORCH_STATE_RECONSTRUCTION_001
iteration: 1/3
dispatcher: operator
date: 2026-08-22
governance_version: 3.1.1
mode: VERIFICATION_ONLY — no ratification, no adoption, no modification of the candidate, no
  resolution of any operator decision, no dispatch of any actor
domain: CONTROL PLANE — `reviews/` is a declared CONTROL_PLANE_ROOT
  (`governance/plan_defined_parameters.md`, CONTROL_PLANE_ROOTS), so this file changes no candidate
  content hash and no role fingerprint
authority: none. This file assigns nothing, adopts nothing, activates nothing, closes no finding,
  amends no document and opens no round. A verdict is a reviewer's judgement, not a governed change
---

# REV-AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001

> **What this is.** A C.2 verification of one `AUTHOR_RESPONSE`. Every factual claim the response
> makes was **re-executed** in this session rather than read. Where my measurement diverges from the
> response's, both are shown. Nothing here ratifies the response, the review it answers, or the
> object either concerns.

---

## A · IDENTITY — established from repository evidence, not from this dispatch

| Field | Value | How established |
|---|---|---|
| `ACTOR_ID` | `mirror` | worktree path `.claude/worktrees/mirror`; branch `mirror` |
| role contract | `roles/mirror.md` — `status: PROPOSED — binding once Mirror hostile review passes and the operator approves` | `grep -m1 '^status:' roles/mirror.md` |
| branch | `mirror` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `78dccaf838cedb82db1337320ae5d41f125ee139` | `git rev-parse HEAD` |
| working tree | clean before this file | `git status --porcelain` → empty |

🔴 **Authority is not read from the role contract.** `roles/mirror.md` is `PROPOSED`, and
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` consequence 2 forbids reading actor authority from a
`PROPOSED` contract. The warrant is traced instead to:

- **H.1 row `Epistemic / method review` → Mirror** — re-counted this session at `main @ 788c357`:
  the H.1 table is 19 pipe-leading lines, i.e. **1 header + 1 separator + 17 rows**, and
  `Epistemic / method review | Mirror` is row 6 of the 17;
- **Annex G.1** (`governance/annex_g_mirror.md:21`) —
  `MIRROR_REQUIRED (MAJOR; protocolli/governance; R4; …)`. The object of the chain is a
  governance-process candidate, so it sits inside the required perimeter;
- **H.1 `WORK_COMMIT` — *"ogni attore, solo proprio branch"*** — for committing this file.

**I hold no Orchestrator authority and take none.** No lease was taken and none is needed.

🔴 **One identity limit, stated rather than smoothed.** Being dispatched as Mirror is not evidence
of being Mirror. The repository evidence above establishes what the `mirror` branch and worktree
are; it does not prove that this session is the actor entitled to them. That gap is the same one
`HANDOFF-ORCHSURF-MIRROR` and `HANDOFF-P5DOMAIN-MIRROR` both record as `delivery: MANUAL — routing
is unresolved`, and it is not closed here.

---

## B · DISPATCH VALIDATION — every named term tested before being reasoned from

| Dispatch term | Verdict | Repository evidence |
|---|---|---|
| `AUTHOR_RESPONSE` | **defined** | `governance/annex_c_review_protocol.md:43` — *"AUTHOR_RESPONSE (obbligatoria; il silenzio non è accettazione)"*. Restated at `GOVERNANCE_v3.1.1.md` § 25, line 325 |
| `Annex C.2` | **defined** | `governance/annex_c_review_protocol.md:34` `### C.2 · Formato unico`. Verified byte-identical between this HEAD and `main @ 788c357` — sha-256 `a3fd5587…4a5b` on both. Its four verdict values are `CONFIRMED \| WEAKENED \| REFINED (+REFINED_FORMULATION) \| REFUTED`; `CONFIRMED = "nessun difetto rilevato dato l'evidence bundle disponibile", non "vero"` |
| `REV-ORCH-STATE-RECONSTRUCTION-001` | **exists, located, pinned** | `reviews/mirror/REV-ORCH-STATE-RECONSTRUCTION-001.md`, present on **1 of 44 refs** (`refs/heads/mirror`), blob `16322c97`, sha-256 `d7a53501…8574` |
| `F-7` | **exists in the review** | § F `EVIDENCE_AGAINST`, line 351, graded `WEAKENED`. Named in § K as owed by the author |
| `F-8` | **exists in the review** | § F `EVIDENCE_AGAINST`, line 381, graded `REFINED`. Named in § K as owed by the author |

**Terms named by the dispatch with no repository source: none.** All five resolve.

**Terms I use only as labels**, because the repository does not define them: `TRANSITION_CHECK`,
`ARTIFACT_STATE`, `ACTOR_STATE`, `AUTHORITY_STATE`, `DEPENDENCY_STATE`, and the bare English noun
`transition`. This was established in the review's § B-1 and re-affirmed in the response's § 0.2.
**This review may not be cited as evidence that any of them is governed.**

### B-1 · One dispatch instruction is in tension with C.2, and C.2 wins

The dispatch orders `STEELMAN` first in its required-output list and again in `FINAL`. **C.2 requires
`STEELMAN (obbligatorio, prima delle obiezioni)`.** Both agree that the steelman precedes the
objections; the artifact follows C.2 (§ D precedes § E and § F). No conflict arises.

### B-2 · The dispatch's opening is irregular in the same way the prior one was

**C.3: `Apertura solo via Orchestrator`.** This review was opened by the **operator**. Recorded, not
treated as disqualifying, for the same measured reasons as in the prior review — and one more that
is now sharper: **the Orchestrator is the author of the artifact under review here.** Had the
Orchestrator opened this review, C.3's `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR` would have been breached at
the opening. **The correct resolution is the operator's, and it is not taken here.**

---

## C · SURFACE MAP — the measurement every negative claim below is scoped by

```
ACTOR                mirror
BRANCH               mirror
HEAD                 78dccaf838cedb82db1337320ae5d41f125ee139
WORKING TREE         clean — git status --porcelain empty before this file

REVIEWED RESPONSE    reviews/orchestrator/AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001.md
                       @ refs/heads/author-response-orch-state-reconstruction = 22b3dc65
                       blob  4131a6361055d724656eda622f09efaa692a77b7
                       sha256 660c823b32c31c794a5e967e4cfb2b5dafe7f762b0b7e2aa9b2ee692d7b69ca5
                       🔴 ABSENT at my HEAD — read via `git show`, never checked out
                       present on 1 of 44 refs

ORIGINAL REVIEW      reviews/mirror/REV-ORCH-STATE-RECONSTRUCTION-001.md @ refs/heads/mirror
                       blob  16322c97ad72c638b50f0cee41a28449155a3bb7
                       sha256 d7a535012a353878fc1f8ab238dff7c7a9c2bcbf63c49f35de0d90d293718574
                       present on 1 of 44 refs — UNCHANGED since the response pinned it

UNDERLYING OBJECT    governance/candidates/PROPOSAL-ORCH-STATE-RECONSTRUCTION.md
                       @ refs/heads/orch-state-reconstruction = f1074aab
                       blob  e6af7e3d9383f4ae7d5210f81af5610bd15e62e7
                       sha256 f491d5247dc1cfffbee3aae66eb646e3114d764e9f18930f9082c34a3ea072ba
                       🔴 ABSENT at my HEAD — read via `git show`, never modified
                       present on 1 of 44 refs — UNCHANGED

main                 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5 — does NOT contain 22b3dc65
                       (`git merge-base --is-ancestor 22b3dc6 788c357` → false)

REFS SURVEYED        49 total — 35 refs/heads · 5 refs/tags · 4 refs/remotes · 1 refs/stash ·
                       4 refs/codex/turn-diffs/*
                       Repository-wide sweeps below iterate heads + tags + remotes = 44 refs.
WORKTREES            17
MEASURED_AT          2026-08-22, this session

VALIDITY             Every absence claim holds for the 44 refs enumerated above and for no wider
                       surface. NOT_FOUND on 44 refs is not NOT_EXIST.
```

**Denominator reconciliation.** My sweep is **44**, identical to the response's. The prior review
swept 42 and declared 47; two branches have been created since (`operator-decision-…` and the
author's own), and the response's § 0.3 reconciliation of 33+5+4+1 = 43 against 47, with the
remaining 4 being `refs/codex/turn-diffs/*`, **is arithmetically correct and reproduces**.

### C-1 · 🔴 My own checkout is not `main`, and one file I measure differs

`git rev-list --left-right --count main...mirror` → **65 behind, 73 ahead**. Diffing the normative
files this review quotes:

```
git diff --stat 788c357..HEAD -- GOVERNANCE_v3.1.1.md annex_c_review_protocol.md
                                 annex_h_authority_matrix.md plan_defined_parameters.md roles/mirror.md
  → governance/plan_defined_parameters.md | 4 insertions(+), 82 deletions(-)   [ONLY THIS FILE]
```

**Annex C, Annex H, the governance body and `roles/mirror.md` are byte-identical** between my
checkout and `main`. **`plan_defined_parameters.md` is not**: my branch carries a 367-line version,
`main` carries 445. Where the response cites that file, **I measured `main`'s copy**, which is the
surface the response was written against. This is declared because a reviewer who quietly measured
the shorter copy would have contradicted the response on an artefact of its own checkout.

---

## D · STEELMAN — the strongest form of the response, before any objection

**C.2 requires the steelman before the objections. This is it, and it is not a courtesy.**

**1 · It accepts both findings and contests nothing, then goes past the grade it was given.** On
F-7 the reviewer graded two table rows together as `WEAKENED`. The author separates them and states
that **row 4 is not weakened but false as written** — *"A claim that something does not exist, made
about four artifacts that exist, is not weakened. It is wrong, and I state it as wrong."* An author
declining the softer grading of its own row is the opposite of the failure mode `AUTHOR_RESPONSE`
exists to catch.

**2 · It tests the finding against the reviewer's own falsifier, trying to make the finding harder.**
Falsifier 3 of the review would have hardened F-7 from `WEAKENED` to `REFUTED` had any normative
file required a ref field of a handoff. The author ran it — `0 hits` across the governance body and
all annexes — and **confirms the reviewer's softer grade after trying to break it**. That is an
author arguing against its own interest and reporting the result either way.

**3 · It measured the population where the reviewer sampled.** The review named one artifact and
listed five key sets. The author read the frontmatter of **all fifteen handoff paths across 44
refs**, and reports the result at population scale: eleven carry frontmatter, four carry ref or
immutable-identifier information as structured keys, and — extending the reviewer's own point —
across eleven **not even `artifact` is common to all**, because
`HANDOFF-MIRROR-PERSISTENCE-AND-HANDOFF-v2` opens with `record_id`. **I reproduced every one of
those figures exactly.**

**4 · It corrects the reviewer without using the correction as a defence.** The review asserted
*"the 11 / 3 split is exact under either rule."* It is not: 11/3 by filename, 12/3 by path. The
author states the correction and then immediately disarms it — *"This changes nothing about F-8, and
it is not offered to soften it… I record it because F-8 is right, not because it is not"* — and
explicitly declines to raise it as a disagreement that would trigger D-3 adjudication. **A correct
correction, offered with its own weight removed.**

**5 · It records its own measurement error before that error could enter a finding.** § 0.4 reports
that a first count of H.1 returned 18 because it included the table header, and that the correct
figure is 17. **I re-counted at `main`: 19 pipe-leading lines = header + separator + 17 rows.** Both
the error and its correction are exactly as described. The author then names the class — *"the
fourth instance of one failure class in this chain"* — rather than filing a silent fix.

**6 · It discharges a conditional the reviewer left open, and refuses to draw the reviewer's
conclusion from it.** `main` moved from `2bb2700` to `788c357` between the review and the response.
The author re-derives it: one commit, one file, 585 insertions; the governance surface
**byte-identical**; falsifier 4's seven objects **7 of 7 still absent from `main`**. **I re-executed
all three: all three reproduce.** And having measured that the falsifier did not fire, the author
declines to re-confirm the verdict — *"the conditional is the reviewer's to close, not mine."*

**7 · It preserves every unresolved item as unresolved, including one against itself.** § 4.3
records that the false row **is still false in the object**, that the concession sits in a
`CONTROL_PLANE_ROOT` where *"it moves no hash and is not read beside the protocol"*, and that this is
the same defect shape as the blocking finding in `REV-XPORT-MIRROR-001`. **An author noting that its
own concession is structurally unable to reach the document it concerns, rather than letting a later
reader discover the false row unaided.**

**8 · Its authority derivation is disciplined throughout.** No authority is read from
`roles/orchestrator.md` (`PROPOSED`); authorship is established from four artifacts on four refs; the
starting-location discrepancy against `deployment_profile.md` is recorded and explicitly **not**
resolved; and the response declines to open a round 2 because C.3 gives opening to the Orchestrator,
who is the author.

---

## E · THE FIVE C.2 CHECKS

### E-1 · Did the author answer the finding? — **YES, for both.**

| Finding | Answered | Where | Disposition stated |
|---|---|---|---|
| F-7 | yes | § 2.1 | `ACCEPTED — WEAKENED accepted as graded for row 3. Row 4 conceded FALSE AS WRITTEN` |
| F-8 | yes | § 2.2 | `ACCEPTED as REFINED… Reproduced independently: 15 by path, 14 by filename` |

**These are exactly the two the review's § K assigns**: *"Owed by the author (`orchestrator`) on
**F-7** … and **F-8**."* Verified at line 654 of the review blob.

**F-13 is correctly identified as not the author's.** The response's § 0.2 records that F-13 exists
in the review (line 484) but that § K does not name it, and carries it to § 3 unanswered rather than
answering it. **Answering an unassigned finding would have been the more impressive-looking error.**

### E-2 · Did the author distinguish observation, interpretation and design decision? — **YES, with one lapse.**

**Where it is done well:**

| Kind | Instance | How it is marked |
|---|---|---|
| observation | § 2.2's reproduction — 15 by path, 14 by filename, the fifteenth named | presented as a swept measurement with the rule stated *for this count* |
| interpretation | § 2.1's B.1-envelope block | 🔴-marked as *"an interpretive question about a **FROZEN** annex"*, with **both branches stated in advance**: *"If B.1 does govern these artifacts, row 3's 'not by any schema' is too strong… If it does not, row 3 stands"* — and then **refused**: *"I do not resolve it."* |
| design decision | a handoff schema, a corrected § 2.1 row, a counting convention | § 2.1 and § 2.2 *"What I did not do"* — *"No fix is invented and none is proposed here"*, routed to Plan under H.1 `Integrazione strutturale` |

**The lapse — AR-1 below.** § 2.1's four-artifact classification is presented as observation
(*"I swept all 15 handoff paths across 44 refs and read the frontmatter of every one"*) but the
boundary of *"carries ref and/or immutable-identifier information as structured frontmatter keys"* is
an **interpretive** classification with an undeclared rule. It is the one place in the response where
an interpretation is presented in the register of a measurement.

### E-3 · Did the author avoid unauthorized changes? — **YES. Verified, not accepted.**

```
git diff --stat main...author-response-orch-state-reconstruction
  → reviews/orchestrator/AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001.md | 551 +++++
    1 file changed, 551 insertions(+), 0 deletions(-)
```

| Claim | Measured |
|---|---|
| the object is unmodified | blob `e6af7e3d` at `orch-state-reconstruction`, **unchanged** — identical to the value the review pinned |
| the review is unmodified | blob `16322c97` at `mirror`, **unchanged** — identical to the value the response pinned, sha-256 `d7a53501…8574` |
| no governance / roles / framework / ledger path touched | the branch's only delta vs `main` is the one file above |
| `main` is unmoved by the author | `main` = `788c357`; `git merge-base --is-ancestor 22b3dc6 788c357` → **false**. Not merged |
| written in its own namespace | `reviews/orchestrator/`, not `reviews/mirror/`, not `governance/candidates/` |
| no merge, no `CANONICAL_BATCH_COMMIT` | one `WORK_COMMIT` on the author's own branch — H.1 |

**The dispatch's `CREATE_AUTHOR_RESPONSE_ONLY` bound is respected in full.**

### E-4 · Did the response provide evidence? — **YES. I re-executed fourteen measurements; all fourteen reproduce.**

| # | Response's claim | My independent measurement | Result |
|---|---|---|---|
| 1 | review blob `16322c97`, sha-256 `d7a53501…8574` | `git rev-parse` + `shasum -a 256` | ✅ exact |
| 2 | object blob `e6af7e3d`, sha-256 `f491d524…72ba` | same | ✅ exact |
| 3 | review present on 1 of 44 refs | swept 44 refs | ✅ `refs/heads/mirror` only |
| 4 | `main` moved `2bb2700` → `788c357`, one commit, one file, 585 insertions | `git show --stat 788c357` | ✅ exact |
| 5 | governance surface byte-identical across that move | `git diff --stat 2bb2700..788c357 -- GOVERNANCE_v3.1.1.md annex_*.md roles/` | ✅ empty |
| 6 | falsifier 4: 7 of 7 objects still absent from `main` | `git cat-file -e 788c357:<path>` × 7 | ✅ 7/7 ABSENT |
| 7 | 15 handoff paths, 14 by filename, difference is the `lettore`/`lettore-b` JSON | sweep over 44 refs | ✅ exact |
| 8 | eleven carry frontmatter; 3 release docs + 1 JSON carry none | frontmatter extraction on all 15 | ✅ exact |
| 9 | 11/3 by filename, 12/3 by path — the review's *"exact under either rule"* is wrong | recount | ✅ the correction holds |
| 10 | `artifact` absent from `HANDOFF-MIRROR-PERSISTENCE-AND-HANDOFF-v2`, which opens with `record_id` | frontmatter read | ✅ exact |
| 11 | zero of 15 handoff artifacts carry a B.1 envelope key | grep `message_id\|durable_pointer\|state_change` on all 15 | ✅ 0/15 |
| 12 | 0 normative hits for `source_branch\|candidate_content_hash\|base_head`; 3 hits in `plan_defined_parameters.md` at 222 / 360 / 371 | grep at `main @ 788c357` | ✅ exact — see § C-1 |
| 13 | H.1 is 17 rows; a header-inclusive count returns 18 | recount at `main` | ✅ 19 pipe lines = header + separator + 17 |
| 14 | *"All four were prepared by `plan`"* (§ 4.2) | `prepared_by` / `from` on all four | ✅ all four are `plan`'s |

**The four-artifact table's contents were also verified individually**, and each key carries what the
response says it carries: `HANDOFF-GOV311-ORCHESTRATOR` (`source_branch: evidence-index`,
`base_head: 749a9a9b…`, `candidate_content_hash: c39ecae8…`); `HANDOFF-SCIENTIST-AB-SPEC`
(`carried_from:` with branch, two commits, blob `8e59df08` and sha-256 `f3f883c1…`; `base: main
cbce3016…`); `HANDOFF-ORCHSURF-MIRROR` (`supersedes:` with three `CONTENT_TIP` oids and three
`CONTENT_HASH` values); `HANDOFF-XPORT-MIRROR` (`revision_2:` with content tip `e839db38`, hash
`81f241f2…6e1f`).

**No claim in the response failed reproduction.**

### E-5 · Did the response leave unresolved items unresolved? — **YES, conspicuously.**

| Left open | Where | Held by |
|---|---|---|
| F-9 — encroachment on Mirror's H.1 row | § 3.1 — *"The author is the last actor who may size an encroachment by the author's own document"* | independent reviewer, via G.2 |
| Q-1, Q-3, Q-6, Q-7, Q-8; F-10's drift path | § 3.2 | operator |
| Q-2, Q-4, F-13 / Q-10 | § 3.3 | Plan |
| F-11, F-12 | § 3.4 | any future adopter — *"this response adopts nothing"* |
| whether B.1's envelope governs handoff artifacts | § 4.2 — *"The answer changes F-7's grade"* | operator, as Q-6 |
| the false row still standing in the object | § 4.3 — *"it is still false… I do not repair it here"* | not this response's |
| the verdict | § 1.2 — *"It does not re-open the verdict"* | reviewer |
| round 2 | § 5 — *"I do not open anything"* | Orchestrator / opener |
| the location discrepancy vs `deployment_profile.md` | § 0.1 — *"recorded, and it is not this file's to fix"* | not this response's |

**Nothing was closed by being written down.** The response states this of itself and it holds under
inspection: no item in §§ 3–4 is answered, sized, assigned or scheduled anywhere in the document.

---

## F · FINDING_ASSESSMENT — C.2 vocabulary only

### F-7 — **REFINED**

```
F-7  ·  REFINED
```

**The finding stands. Its formulation under-graded one of the two rows it covered, and the author
corrected that upward.**

- **Row 3 remains `WEAKENED`, and I re-ran the falsifier that would have hardened it.**
  `grep -E 'source_branch|candidate_content_hash|base_head'` over `GOVERNANCE_v3.1.1.md` and every
  annex returns **0**; the three hits in `plan_defined_parameters.md` are inside the
  candidate-content-hash procedure and require no field of any handoff. **No normative file imposes
  a schema on a handoff**, so row 3's literal *"as a required element… not by any schema"* survives.
  `REFUTED` does not fire.
- **Row 4 is false, and it is false against more artifacts than the response counts.** Under the
  rule *"a frontmatter key whose value carries a blob oid, commit oid or content hash"*, my
  measurement returns **five**, not four: the four the response names, plus
  `HANDOFF-MIRROR-PERSISTENCE-AND-HANDOFF-v2`, whose `provenance_boundary:` key carries branch
  `mirror` and the full 40-hex HEAD `7547724392509c0433b3c633c16570d766442699`.
- **Direction of both corrections is the same: against the object.** Nothing in F-7 is weakened or
  refuted. Its diagnosis — *"the object argues from the weakest example"* — is confirmed, and the
  response is right that the review understated it.

**Why `REFINED` and not `CONFIRMED`.** The finding as issued applied one grade to two rows that do
not deserve the same grade. That is a defect in the finding's formulation, corrected by the author
and independently reproduced here. C.2's `REFINED (+REFINED_FORMULATION)` is the value for a finding
that survives with its statement corrected.

### F-8 — **REFINED**

```
F-8  ·  REFINED
```

**The finding's core is confirmed and reproduced without qualification. One sub-clause of the
finding is refuted, and the refutation is of my sentence, not of the finding.**

- **Core, reproduced independently:** 15 paths matching `/handoff/i` across 44 refs; 14 by basename;
  the difference is exactly
  `runtime/handoff/C-2/PMID42422765.working.lettore-and-lettore-b.json`. **The object stated `14`
  without declaring which rule produced it.** Confirmed.
- **Sub-clause refuted:** the review wrote *"The 11 / 3 split is **exact** under either rule."*
  Measured: release-process is 3 under both rules; actor-to-actor is **11 by filename and 12 by
  path**. The split is not exact under either rule. **The author's arithmetic is correct and I
  reproduce it.**
- **The stronger point the review added is confirmed at population scale**: across eleven
  frontmatter-bearing handoffs, not even `artifact` is common to all.

**Why `REFINED` and not `CONFIRMED`.** A finding one of whose sub-clauses is false is not a finding
delivered intact. The substance is untouched; the statement needed correcting; the author corrected
it and refused to bank the correction as a defence.

---

## G · OBSERVATIONS ON THE RESPONSE — no verdict attaches to these

**These are not findings against F-7 or F-8, and none of them reduces either. They are recorded
because a later reader inheriting this chain should not have to re-derive them.**

### AR-1 · 🔴 The response states two different counts of the same population, and declares the rule for neither

| Where | Sentence | Count |
|---|---|---|
| § 2.1 | *"four carry ref and/or immutable-identifier information as structured frontmatter keys"* | **4** |
| § 2.2 | *"across all eleven frontmatter-bearing handoffs… ref-bearing keys appear in two"* | **2** |

Measured myself, over the same eleven, under four rules stated explicitly:

| Declared rule | Count | Artifacts |
|---|---|---|
| key **named** for a ref or base | **2** | GOV311 (`source_branch`, `base_head`); SCIENTIST-AB-SPEC (`carried_from`, `base`) |
| the response's § 2.1 set | **4** | + ORCHSURF-MIRROR (`supersedes`); XPORT-MIRROR (`revision_2`) |
| key **value** contains a blob/commit oid or content hash | **5** | + MIRROR-PERSISTENCE-v2 (`provenance_boundary`: branch `mirror`, HEAD `75477243…2699`) |
| key **value** contains a git ref name **or** an oid | **6** | + P5DOMAIN-MIRROR (`delivery`: *"durable git state on branch `p5-domain-truth`"*) |

**Both of the response's figures are defensible; neither rule is declared; and the two sentences are
about the same eleven artifacts.** The author demonstrably read
`HANDOFF-MIRROR-PERSISTENCE-AND-HANDOFF-v2` — § 2.2 cites it by name for the absence of `artifact` —
so this is a classification boundary, not an unread file.

🔴 **The class matters more than the count.** § 0.4 of the response names three prior instances of
one failure class in this chain and calls itself *"the fourth"*. This is the **fifth**, and it occurs
in the two sections that accept F-8 — a count stated without its rule, inside the document conceding
that a count stated without its rule travels wrongly. **The direction is against the author**: under
the oid rule, row 4 of the object is false by five rather than four. **Nothing here softens F-7 or
F-8.**

### AR-2 · AR-1 changes the answer to a question the response itself leaves open

§ 4.2 asks whether the ref-carrying practice is *"a convention or a lineage"*, observing *"All four
were prepared by `plan`"* — **which I verified: all four are `plan`'s.** But the all-`plan` property
belongs to the undeclared rule, not to the practice: under the oid rule the population also contains
`HANDOFF-MIRROR-PERSISTENCE-AND-HANDOFF-v2`, whose `actor_id:` is **`mirror`**. The response states
that this question *"bears on how much weight Q-2 may place on the precedent."* **It does — and the
two rules answer it differently. Recorded, not resolved: Q-2 is Plan's.**

### AR-3 · 🔴 An error in my own review, surfaced by verifying the response

The review's § F-8 five-artifact key listing reads:

```
HANDOFF-XPORT-MIRROR   artifact handoff_id candidate from to opened_by date domain consequence
```

**Measured at blob `aa286f30`:** the ninth frontmatter key is **`revision_2`**, not `consequence`;
`consequence:` occurs at **body line 102**, outside the frontmatter. And `revision_2` carries
*"content tip `e839db38`, hash `81f241f2…6e1f`"*.

**Consequence for my own sentence.** The review wrote *"the ref-bearing keys in **one**"* of its
sample of five. It is **two of five** — GOV311 and XPORT. **The review understated F-7 inside its own
displayed evidence, in the same direction the author later corrected.** The response's § 2.1 table
names `revision_2` correctly and does not flag that the review's key list was wrong; not flagging
someone else's transcription error is not a defect in a response.

**This is my error, it is recorded here, and it is not charged to the author.**

### AR-4 · The object's single example is also mis-described, and neither document says so

Object row 3 offers `HANDOFF-P5DOMAIN-MIRROR` as the weak case — *"carries `BRANCH` in a prose code
block by the author's own care"*. Measured at blob `5a0c305d`:

- **body line 18** — `BRANCH            p5-domain-truth` in a prose code block ✅ as described;
- **frontmatter line 8**, key `delivery:` — *"Read this from durable git state on branch
  `p5-domain-truth`."* **The same ref, in a structured frontmatter key.**

**This does not change row 3's grade** — a frontmatter key by authorial care is still not a schema,
and the falsifier does not fire. But the object's *evidence* for row 3 mis-describes the one artifact
it cites, and the response, having re-read all fifteen frontmatters, did not catch it. **Recorded as
an observation on the object, carried by neither the review nor the response.**

### AR-5 · One citation imprecision

§ 0.2 cites C.2 as *"Restated in `GOVERNANCE_v3.1.1.md` § 325"*. The restatement is at **§ 25 ·
DISCIPLINA PEER REVIEW**, which begins at **line 325**. A line number in section position. **The
content cited is accurate and complete**, including the four verdict values, `max 2 round →
adjudication` and the `CONFIRMED` gloss.

---

## H · C.2 VERDICT ON THE RESPONSE

```
C2_VERDICT: RESPONSE CONFORMS TO ANNEX C.2 — the obligation is discharged as to F-7 and F-8.
            All five C.2 checks pass. One method observation (AR-1) is recorded; it runs against
            the author's own document and alters the standing of neither finding.

F-7:  REFINED
F-8:  REFINED
```

🔴 **What this verdict is not.** Per C.2, `CONFIRMED` on a review means *"nessun difetto rilevato
dato l'evidence bundle disponibile", non "vero"*, and the same discipline binds this one. **This
verdict ratifies nothing.** It does not approve adoption, does not advance
`PROPOSAL-ORCH-STATE-RECONSTRUCTION` beyond `status: PROPOSED / normative: no / authority: none`,
does not close F-9 … F-13 or any of Q-1 … Q-10, does not resolve the operator's Q-1 fork, does not
repair the false row that still stands in the object at blob `e6af7e3d`, and does not open a second
round. **The candidate remains where
`DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE` put it: `OPTION B — HELD_AS_CANDIDATE`,
`NEXT_ALLOWED_ACTION: none`.**

**Nothing is contested by the response, so no adjudication is triggered.** Had anything been
contested, D-3 sends it to the operator, because H.1's adjudicator is the author here.

---

## I · WHAT_WOULD_CHANGE_MY_MIND — declared falsifiers, C.2 mandatory

1. **A governed determination that Annex B.1's envelope governs handoff *artifacts*, not only
   messages.** Row 3's *"not by any schema"* would fail, F-7 would harden past `WEAKENED`, and the
   author's acceptance would prove **under-graded a second time**. The response identifies this
   falsifier against itself and refuses to resolve it; Annex B is FROZEN and this is Q-6's territory.

2. **A declared counting rule, from an authority entitled to declare one, fixing the boundary of
   *"carries ref / immutable-identifier information as a structured key."*** If it yields 4, AR-1
   dissolves entirely. If it yields 2, 5 or 6, then § 2.1 or § 2.2 of the response is wrong on its
   own terms — and my own four-rule table would need reissuing against it.

3. **The author declaring the intended rule as *"the address of the referent, not of the authoring
   session."*** `provenance_boundary` and `delivery` would fall outside it, `four` would stand, and
   **AR-1 reduces to an undeclared-rule observation with no arithmetic consequence.**

4. **Any normative file, on any ref, requiring a ref field of a handoff.** F-7 → `REFUTED`, and the
   response's careful confirmation of `WEAKENED` would be wrong in the author's favour.

5. **A sixteenth handoff path on a ref outside the 44 swept.** Every count in § E-4 rows 7–8 and in
   AR-1 is scoped to that surface and to no wider one. A clone I cannot see falsifies them.

6. **`main` moving so that the seven objects of the object's § 1.1 become a subset of it.**
   Falsifier 4 of the original review fires, § 2.3's re-derivation is stale, and the original
   verdict's `CONFIRMED` on architectural necessity should be withdrawn by its reviewer.

7. **A governed determination that `PROPOSAL-C9-STATE-MODEL` and this object are one object.**
   Reviewing them separately becomes a methodological error, and both the review and this
   verification would need reissuing against the merged object.

8. **Evidence that this session is not the actor entitled to `mirror`.** § A records that the
   dispatch is not proof of identity. If the addressing is wrong, this artifact is a stranger's
   verdict in Mirror's namespace, and **it should be voided rather than corrected.**

---

## J · RESIDUAL UNCERTAINTY

1. **AR-1's four rules are mine, declared here for the first time.** No repository authority defines
   any of them. They are stated so the count can be checked, not because any of them governs.
2. **44 refs is not the universe**, and every absence above inherits that bound.
3. **F-9 is unsized, by design and by two documents.** The author may not size an encroachment by
   the author's own document; I may not adjudicate the scope of my own function. **It is still
   unsized, and this artifact does not change that.**
4. **The false row still travels.** § 4.3 of the response is correct that the concession sits in a
   `CONTROL_PLANE_ROOT` and does not reach the object. **This review adds a second artifact in the
   same root, with the same limitation.**

---

*Prepared by Mirror under Annex C.2 at R4, as verification only. It creates one file under
`reviews/mirror/` — a declared `CONTROL_PLANE_ROOT` — and touches nothing else: no governance file,
no annex, no role contract, no ledger, no decision, no candidate, no other actor's branch. It is a
`WORK_COMMIT` on branch `mirror` under H.1, not a merge and not a `CANONICAL_BATCH_COMMIT`.*
