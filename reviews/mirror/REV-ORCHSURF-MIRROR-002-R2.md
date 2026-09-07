---
artifact: MIRROR R4 hostile review — ROUND 2, remediation verification (Annex C.2)
review_id: REV-ORCHSURF-MIRROR-002-R2
addends: REV-ORCHSURF-MIRROR-002 (branch `mirror` @ 36e1381). Round 1 is NOT edited — it is the
  evidence of what was claimed before the remediation, and a review rewritten to match its own
  outcome has stopped being evidence
object: CAND-20260819-ORCHSURF revision 4, remediated, @ **6110421** on branch
  `orchestrator-surface` — the object was re-bound from e1dac06 mid-review (ADD-005) and every
  anchor below is recomputed at 6110421, not carried across
  CANDIDATE_CONTENT_HASH 844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
  UNCHANGED · BASE_HEAD 04693e68 · CONTENT_TIP 9a70e94d
opened_by: OPEN-REV-ORCHSURF-MIRROR-002-ADD-004 @ dd434d5, re-bound by ADD-005 @ a22fd28
task_id: TASK-20260820-MIRROR-ORCHSURF-REV4 · DIRECTIVE_VERSION 2 · round 2 of 2 (C.3)
level: R4 — METHOD / MIRROR_REQUIRED
reviewer: mirror
author: plan
adjudicator: orchestrator (C.3) · HUMAN_APPROVAL operator (H.1) — none granted, none implied
review_date: 2026-08-20
verdict: REQUEST CHANGES
scope: M-1/M-2/M-3 remediation ONLY, plus the volunteered §8 correction. M-1/M-2/M-3 are NOT
  re-opened (accepted in full, uncontested). T7 NOT re-opened — adjudicated WITHDRAWN in ADD-004
  §4. ROOTGUARD not entered. The owed items — now FIVE, `SLR-plan-0014` added at ADD-006 — remain
  owed and none is discharged by this verdict
---

# R4 ROUND 2 — does the remediation dispose of M-1, M-2 and M-3?

```
OBJECT    CAND-20260819-ORCHSURF r4 @ 6110421 · hash 844de909…acb6dc UNCHANGED
VERDICT   REQUEST CHANGES — one blocking finding, single-clause, NEW and not a re-opening
          M-1  DISPOSED — my falsifier 1 fires
          M-2  DISPOSED — my falsifier 2(b) fires
          M-3  DISPOSED — my falsifier 3 fires
          M-4  NEW · BLOCKING — §17.3 states, in the governing layer, that the publication
               gate does NOT pass, and cites §1, which says it does. One of the two is
               false and they are in the same layer. SURVIVES the re-bind to 6110421
          §8 correction volunteered by Plan: VALUE VERIFIED · CHARACTERISATION NOT ESTABLISHED
          T7 ruling, as RECORDED in §17.1: ACCURATE — verified against ADD-004 §4 at the
               exact commit the row cites. The ruling itself is closed and not re-opened
```

> **On the re-binding, because it is the reason this section exists in this form.** The object
> moved `e1dac06 → 6110421` while this review was being written. The adjudicator flagged it rather
> than letting me discover it, and the reason it had to be flagged is the important part: the
> `CANDIDATE_CONTENT_HASH` is **invariant by construction** across these commits, because
> `governance/candidates/` and `reviews/` are excluded from the hashed domain. **A matching digest
> here certifies nothing about which text a reviewer is reading.** Content identity unmoved and
> review object unmoved are two claims, and a green hash establishes only the first. Every anchor,
> count and boundary below was recomputed at `6110421`; none was carried from the `e1dac06` draft.

## 0 · Preflight and re-derivation

**Instrument preflight run first** (`SLR-mirror-0018`), because my own branch is the hazard it
records:

```
                                    mirror     04693e68   9a70e94d   e1dac06    6110421
candidate_content_hash.py           be20e303   cd5776d3   cd5776d3   cd5776d3   cd5776d3
plan_defined_parameters.md (§P5)    a139b283   e1f9e1ec   e1f9e1ec   e1f9e1ec   e1f9e1ec
governance_fingerprint.py           c6e05e10   c6e05e10   c6e05e10   c6e05e10   c6e05e10
```

Reviewer branch differs from base on two of three → executed from a throwaway detached checkout at
`6110421`, never from my worktree. Base equals tip on all three → the remediation does not modify
its own verifier. Both branches of the preflight fired, as at round 1, and again after the re-bind.

**Integrity, re-derived at the current object rather than accepted from ADD-004 or ADD-005:**

| Claim | Re-derived | Result |
|---|---|---|
| only control plane moved `da47440 → e1dac06` | `M …/CAND-20260819-ORCHSURF.md` · `A reviews/plan/AUTHOR-RESPONSE-ORCHSURF-MIRROR-002.md` — **two paths, both under declared CONTROL_PLANE_ROOTS** | **reproduces** |
| only control plane moved `e1dac06 → 6110421` | `M …/CAND-20260819-ORCHSURF.md` · `M reviews/plan/AUTHOR-RESPONSE-ORCHSURF-MIRROR-002.md` — **two paths, same two roots** | **reproduces** |
| Plan *"RAN NOTHING"* at the re-bind | `git diff --stat e1dac06 6110421` = **2 files, +15 −2**, and the candidate's share is **+3 −2**. No test output, no capture file, no measurement artefact entered the tree | **consistent — confirmed, not taken on report** |
| CONTENT_HASH unchanged | recomputed at `6110421`: `844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc` | **reproduces exactly** |
| the SET, not the digest | `--emit-domain` at `6110421` vs at `9a70e94d`: **byte-identical**. Included **539** unchanged; excluded **49 → 50** across the round, the new entry being the author response under `reviews/` | **set-verified** |
| FROZEN across `04693e68..6110421` | diff over body, `annex_a…annex_j`, `ANNEX_INDEX.md`, `plan_defined_parameters.md`: **EMPTY** | **reproduces** |

**One observation worth recording rather than leaving implicit.** The author response could be
added to the branch without moving the candidate's identity *only because* `reviews/` is a
control-plane root — the `legend-candidate-v4` amendment whose own §P5 text says it *"happens to
change nothing in the tree that carries it."* It changes something here: it is what lets a review
cycle run on a live candidate without re-binding it. The rule earned its keep between round 1 and
round 2.

**Section boundaries recomputed per tip, never carried across** — the discipline round 1 taught:

```
@ 6110421   §1 = 65–250   §16 = 931   §17 = 956–1077   (1077 lines)
            prior tips: 1076 @ e1dac06 · 1032 @ da47440 · 993 @ 9a70e94d — four texts, one hash
```

---

## STEELMAN

**Plan accepted all three findings, contested none, and then went past them.** The remediation is
not the minimum that would clear a reviewer. §17.1 does not merely withdraw T7's and T8's results
— it **splits the row that caused the defect**, keeping the inherited-universe METHOD lesson
`PRESERVED` and adding two separate `RESULT` rows, with the diagnosis stated in the row itself:
*"This row disposes of the LESSON only. The RESULTS are disposed of in the two rows below — a
distinction revision 4 originally failed to draw."* That is the finding's mechanism written into
the structure, not just its conclusion.

**It also added a row I did not ask for and could not have compelled.** `T1–T6, T9, T10 results —
NOT RE-RUN at revision 4`, with T10 separated into a preserved *method* and a revision-3 *result*.
M-2 named T7 and T8; Plan generalised the defect to the whole battery and disclosed the larger
gap. A package under review normally concedes the narrowest thing that closes the finding.

**§17.1a answers the question I actually asked, not the question that would have been easier.** I
found that Layer 1 was *silent* on the candidate's own subject. The cheap fix is a hedge —
"status unchanged pending review". Instead it states a position that can be wrong: `ORCHESTRATOR
SURFACE RESOLVED`, `BLOCKED_BY_FROZEN NO. WITHDRAWN`, `A FRESH BOOTSTRAP COMPLETES`, and — the
part that costs something — **§16's *"It does not claim a fresh bootstrap can complete"* explicitly
WITHDRAWN**, naming the retracted sentence rather than leaving precedence to do the work silently.
It also separates `WHAT STILL BLOCKS` (*"nothing in governance"*) from `WHAT IS STILL OWED`
(*"the review ladder itself … MAJOR requires both"*), which keeps a resolved *governance* question
from being read as a resolved *candidate*.

**And it repairs the mechanism, not only the instance.** My L-4 was that a blanket precedence
clause resolves conflicts and cannot reach a silence. §17.1a converts the silence into a stated
conflict — Layer 1 now says `RESOLVED` where Layer 2 says `PARTIALLY_RESOLVED` — so the clause in
§17's header becomes load-bearing where before it was inert. `PARTIALLY_RESOLVED` still occurs
4 times in Layer 2 and **0** times in Layer 1, which is now correct rather than defective.

**Plan filed a divergence against the adjudicator's transport, and it was right.** ADD-004 §2
records that the routing message's line anchors were CONTENT_TIP-relative and resolved to the
wrong text at the branch tip its own handoff tells a reviewer to fetch. My round-1 review survived
the same shift because it anchored by section and quoted string. The author caught a defect in the
adjudicator's artefact while under review by both — that is the laboratory working.

---

## EVIDENCE_FOR — the three dispositions, tested against my own declared falsifiers

Round 1 published six falsifiers so that someone who does not trust me could retire the findings.
Three of them now fire. I record that as they were written, not as I would write them today.

**M-1 — DISPOSED.** Falsifier 1 was: *"M-1 falls if a sentence in §1 or §17 states the operative
status of the Orchestrator surface at revision 4 — resolved, partially resolved, or blocked by
something named."* §17.1a does exactly this.

```
Layer 1 (§1+§17) @ 6110421   "ORCHESTRATOR SURFACE"  1   (round 1: 0)
                             "RESOLVED"              3   (round 1: 0)
                             "PARTIALLY_RESOLVED"    0   — correct: it is Layer 2's word
Layer 2 still asserts it     "PARTIALLY_RESOLVED"  §§2–15: 3 · §16: 1 — retained verbatim
```

The asymmetry is the disposition working. Layer 1 now carries the status and Layer 2 keeps the
superseded one, so §17's precedence clause has a genuine conflict to resolve — which is the repair
M-1 asked for, not merely the sentence it asked for.

**M-2 — DISPOSED.** Falsifier 2(b) was: *"§17 anywhere discloses that T1–T10 were not re-run at
revision 4."* It now does, in two places: a §17.1 row and a §17.3 bullet naming the omission and
attributing it. `re-run` occurs 4× and `T1–T10` 1× in Layer 1; both were 0 at round 1. The §17.3
bullet also states *"their stated reasons do not describe this one"* — which is the finding, not a
paraphrase of it.

**T7's ruling, as RECORDED — ACCURATE.** In scope this round, per ADD-005: the ruling is closed,
but whether §17.1 records it faithfully is part of the disposition layer. Checked against
`git show dd434d5:reviews/orchestrator/OPEN-REV-ORCHSURF-MIRROR-002-ADD-004.md` §4 — the exact
commit the row cites, read from durable state and not from any message:

| §17.1 row says | ADD-004 §4 says | |
|---|---|---|
| *"ADJUDICATED, not decided by Plan"* · *"Plan routed the re-framing for adjudication"* | *"Plan asked rather than re-framed quietly"*; conduct *"affirmed on the record"* | ✅ |
| *"Grounds, the first decisive"* | *"Three grounds, and the first is the one that decides it"* | ✅ |
| (a) *"entailed by the design under test … credit this candidate with evidence it did not earn"* | *"entailed by the design under test … credit the candidate with evidence it did not earn"* | ✅ |
| (b) *"a second wrong-reason pass … §9's own `WRONG-REASON LOAD-BEARING PASSES 0` forbids"* | *"manufacture a second wrong-reason pass … which §9's own … forbids"* | ✅ |
| (c) *"the enforcement question … ratified record §1 item 5 defers to ROOTGUARD"* | *"the **enforcement** question … § 1 item 5 defers it to `CAND-20260820-ROOTGUARD-001`"* | ✅ |
| T8 *"WITHDRAWN, on the same ruling"* | *"T8 falls the same way and for the same reason"* | ✅ |
| re-framed T7 *"OWED TO `CAND-20260820-ROOTGUARD-001`, and NOT to this candidate"* | *"owed to `CAND-20260820-ROOTGUARD-001` … not owed to this candidate"* | ✅ |

No paraphrase drifts from the ruling and no ground is dropped, softened or added. The citation
resolves at the commit named. **And the row that registers the re-framed question does not import
ROOTGUARD**: it records the question as owed elsewhere and answers nothing, which is the
distinction ADD-004 §4(c) drew. I did not re-open the ruling and no finding here depends on it.

**M-3 — DISPOSED.** Falsifier 3 was: *"M-3 falls if `SELECTED REMEDIATION CLASS`, `WHAT REMAINS
UNSOLVED` or `PROBLEM DECLARED, NOT SOLVED` is disposed of anywhere in Layer 1."* All four §8 keys,
including `BLAST RADIUS`, are now named and withdrawn in a §17.1 row. Each was 0 in Layer 1 at
round 1 and is 1 now.

**T7 — not examined.** Adjudicated `WITHDRAWN` in ADD-004 §4 and out of scope. I record only that
I did not re-open it and that no finding here depends on it.

---

## EVIDENCE_AGAINST

Held against the dispositions above, so the section is not a formality:

- **§17.3 is internally stale while being the section that repaired a §17.3 omission.** The M-2
  remedy was added to a list that already contained a false bullet, and the audit that added it did
  not sweep the list it was editing. That is evidence that the remediation was targeted at the
  findings rather than at the section, and it is the whole of M-4.
- **`ORCHESTRATOR SURFACE` occurs once in Layer 1 and twice in Layer 2.** One sentence now carries
  the operative status of the package's subject. It is sufficient — a status stated once in the
  governing layer *is* stated — but it is thin, and a future revision that touches §17.1a without
  noticing what it carries will reproduce M-1 exactly.
- **`RESOLVED` at 3 occurrences in Layer 1 is doing more work than `ORCHESTRATOR SURFACE` at 1.**
  The status is expressed largely through qualifiers — *"RESOLVED at the level this candidate
  operates on"* — and "the level this candidate operates on" is not defined anywhere in Layer 1.
  I did not raise it as a finding because §17.1a's `WHAT STILL BLOCKS` and `WHAT IS STILL OWED`
  rows bound it in practice; a stricter reviewer could.
- **Four texts of this file now share one `CANDIDATE_CONTENT_HASH`.** Nothing is wrong with that —
  it is the domain rule working — but it means every claim in this review is anchored to a blob,
  and blob anchoring is a discipline this exchange had to learn twice mid-round.

## KEY_OBJECTIONS

### 🔴 M-4 · Layer 1 contradicts itself about the publication gate, and sends the reader to the refutation — BLOCKING, NEW

§17.3 at `6110421`, **line 1057**, verbatim — and unchanged at `5ea744c`, where the candidate blob
is byte-identical (`7469f4e1`):

> - **It does not claim the publication gate passes.** It does not — see §1. The block is the
>   operator's signature in a public-edition repository, it is disclosed rather than absorbed, and
>   Plan does not resolve it.

§1 at `6110421`, **line 138**, same layer, verbatim:

```
PUBLICATION_GATE          PASS · BLOCKS: 0 …
                            at BASE_HEAD, matched checkout        PASS · 0
                            at 1a650d85, first revision-4 binding BLOCK · 1
                            at 9a70e94d, CONTENT_TIP              PASS · 0
                          CLEARED BY     9a70e94d, operator-approved redaction to `Operatore`
```

Measured independently at round 1, in matched checkouts: **PASS · 0 BLOCKS at BASE_HEAD and at
CONTENT_TIP, DELTA 0**, with the same four pre-existing `REVIEW` items either side. §1 is right.
**§17.3's bullet is false at this tip**, and it is false in the present tense — *"It does not"*,
*"The block **is**"*, *"Plan does not resolve it"*. It survived the re-bind that cleared the block
at `9a70e94`, where §1 and the frontmatter were both updated and this bullet was not.

Why blocking rather than cosmetic:

1. **Both statements are Layer 1.** The precedence clause in §17's header governs Layer 1 over
   Layer 2. It says nothing about §1 versus §17, so the contradiction has no resolution rule —
   this is not a conflict the package's own machinery can settle.
2. **It points at its own refutation.** *"see §1"* directs the reader to the section that
   disproves the sentence making the reference.
3. **It misstates readiness to the party who decides.** This is a MAJOR governance candidate whose
   approval is the operator's. A reader of §17.3 — the section written to be the honest inventory
   of non-claims — is told the candidate carries an unresolved publication block. It does not.
4. **It is the same defect class as M-2, in the same list.** M-2 was a §17.3 omission about
   evidence the inversion had invalidated. M-4 is a §17.3 assertion the re-bind invalidated. The
   list was audited for what was missing from it and not for what had gone stale inside it.

**Disclosure against myself: this was reachable at round 1 and I missed it.** I read §17.3 in full,
quoted it approvingly in my STEELMAN as disclosing against interest, and separately measured the
gate as PASS — I held both halves and did not put them together. My round-1 mandate was Layer-3
completeness (Layer 2 versus Layer 1), and a Layer-1-internal contradiction sits outside that
frame; that explains the miss and does not excuse it. I raise it now because §17.3 is one of the
three sites this round put in scope, not to widen the scope by the back door. **If the adjudicator
rules M-4 out of scope as something that passed at round 1, I will not contest the ruling — but
the sentence is still false, and it should not reach the operator in this state.**

**Remedy:** delete the bullet, or restate it in the past tense as §1 already does. One clause.

### 🟡 The volunteered §8 correction — VALUE VERIFIED, CHARACTERISATION NOT ESTABLISHED

Plan went past M-3 and asserts `BLAST RADIUS 5` is not merely stale but *arithmetically wrong* —
*"the blast radius is **three** content files at revision 4 … not five."* I was directed to verify
it and not adopt it. Measured, per revision, content plane only:

```
tip 7b6a9d9  (rev 2)   3 modified content files + 3 added (SLR-plan-0010, -0010-COR-001, -0011)
tip 25fa61a  (rev 3)   3 modified + 4 added
tip 1a650d8  (rev 4)   3 modified + 6 added
tip 6110421  (rev 4)   3 modified + 6 added   <- the review object
                       modified = BOOTSTRAP.md · deployment/deployment_profile.md · roles/orchestrator.md
```

**The value 3 is correct and reproduces**, and Plan's three named files are exactly the modified
set. It is also the count the rest of the package already used consistently — §5.3 *"Three content
files, not a control-plane note"*, §16 *"three content files"*, and §1's own *"this candidate's
three edited files"*.

**The characterisation does not.** §8 is headed *"Remediation classes considered, **at revision
2**"*, and at revision 2 the figure **5 is reproducible** under at least one defensible population:
three edited content files plus two learning *records*, `SLR-plan-0010` (with its `COR-001`
correction folded into its parent) and `SLR-plan-0011`. So 5 was not an arithmetic error; it was a
revision-2 figure over an unstated population, retained into a revision-4 disposition. Calling it
*"wrong"* rather than *"stale, and over a population never declared"* misdiagnoses it — and the
corrected row **inherits the same defect it fixes the value of**: it states `three content files`
without saying whether that counts files edited (3), content-domain paths added or modified (9),
or domain entries the pre-image grew by (2). Under the second reading, `three` is itself an
undercount.

This is not a request to change the number. It is a request not to record a population failure as
an arithmetic one, because the laboratory keeps finding the former and will not learn it from a
record that names the latter. A correction offered **in the reviewer's favour is still a claim**,
and this one is right about the value and wrong about the diagnosis.

## ALTERNATIVES_CONSIDERED

1. **Return CONFIRMED and note M-4 as an observation.** Rejected: C.2 defines `CONFIRMED` as *"no
   defect found given the available evidence bundle"*. A false sentence in the governing layer of
   a MAJOR candidate bound for operator approval is a defect, and grading it down to an
   observation because the remediation was otherwise excellent is the inheritance trap wearing a
   compliment.
2. **Treat M-4 as out of scope and stay silent.** Rejected. §17.3 is one of three sites explicitly
   in scope this round; I found it there. Silence would also mean withholding, from the party who
   approves, a sentence I have measured to be false.
3. **Fold the §8 characterisation into M-4 as a second blocking finding.** Rejected as
   disproportionate: the delivered *value* is correct and no reader is misled about the candidate's
   scope. It is recorded as non-blocking.
4. **Re-open M-1's `A FRESH BOOTSTRAP COMPLETES` as unverified.** Rejected. Read precisely, the row
   grounds itself on the removal of the governance stop — *"Revision 3 could not say this: its step
   9 halted"* — which I measured (`UNTIL RESOLVED`: 1 hit at `25fa61a`, 0 at `9a70e94d` and
   `6110421`). It claims no successful end-to-end execution, and §17.3 already discloses that the
   test battery was not re-run. Pressing further would be re-opening M-1, which is out of scope.

---

## VERDICT

```
REQUEST CHANGES — one blocking finding (M-4), single-clause, newly found in a section this
round placed in scope. M-1, M-2 and M-3 are DISPOSED, each against a falsifier I published
before the remediation existed.
```

Stated plainly so it cannot be mistaken: **the remediation of my three findings is complete and
better than what I asked for.** Were M-4 not present I would return `CONFIRMED` — meaning no defect
found given this bundle, never "true". M-4 is one stale sentence that outlived the re-bind which
falsified it, in the one list whose whole function is to be accurate about what is not claimed.

**REVIEWER_CONFIDENCE** — HIGH on all three dispositions: each was tested against a falsifier
written before the remedy, and each is a mechanical count over a bounded text with boundaries
recomputed per tip. HIGH on M-4's factual half — I measured the gate PASS at both ends in matched
checkouts at round 1 and §1 states the same. MEDIUM on M-4's scope: whether it is admissible this
round is the adjudicator's call, not mine.

**RESIDUAL_UNCERTAINTY** — (a) I verified the three dispositions by occurrence counting plus
reading the rows; I did not re-audit §§2–15 for assertions outside the three findings, which round
2's scope excludes. (b) The regression suite is still not re-measured and I did not measure it.
(c) The `BLAST RADIUS` population reading is mine; Plan may hold a different definition, and if it
states one my objection narrows to "state it in the row".

**AN ABSENCE THAT IS NOT A GAP, checked rather than assumed.** `SLR-plan-0014` does not exist and
I confirm it is **not** a finding. Plan declared it owed under body §15 and deliberately withheld
it while this review is open, on the ground that `learning/` is inside the hashed pre-image so
writing it would move `CANDIDATE_CONTENT_HASH` and invalidate the binding under review mid-round.
I measured the ground rather than accepting it: **15 `learning/` entries included in the domain at
`6110421`, 0 excluded**, and `SLR-plan-0014` is absent from the tree at `5ea744c`. The reasoning
holds and the restraint is correct — an author who improved its own learning record mid-round
would have invalidated the object I am reviewing in order to look better while I reviewed it.

**EVIDENCE_NEEDED** — none for M-1/M-2/M-3. For M-4, none: the two sentences are both in the file
and one of them is measurably false.

---

## WHAT_WOULD_CHANGE_MY_MIND

1. **M-4 falls** if the publication gate does **not** pass at `6110421` — i.e. if
   `python3 scripts/public_release_gate.py`, run in a checkout at that tip, reports `BLOCKS: 1`
   with a `DIRECT_IDENTIFIER` at the DEC. **I measured `VERDICT: PASS · BLOCKS: 0` at BASE_HEAD and
   at CONTENT_TIP with DELTA 0.** If the gate blocks, §17.3 is right and §1 is the defective half —
   and my finding then stands against §1 instead, unchanged in substance.
2. **M-4 falls as a contradiction** if §17.3's bullet is read as historical rather than present
   tense. Test: it says *"The block **is** the operator's signature"* and *"Plan does **not**
   resolve it"*, beside §1's `CLEARED BY 9a70e94d`. I hold that no reader reconciles those; if the
   adjudicator does, the finding reduces to a request for tense.
3. **The §8 objection falls** if `5` is unreproducible at revision 2 under **every** population,
   not merely under the one Plan used. **I reproduced it under one** — three edited files plus two
   learning records. Show that population is indefensible and "arithmetically wrong" becomes the
   right description.
4. **A disposition reverses** if any count is wrong at boundaries computed for `6110421`
   specifically: `ORCHESTRATOR SURFACE` 1, `RESOLVED` 3, `PARTIALLY_RESOLVED` 0, `re-run` 4,
   `T1–T10` 1, the four §8 keys 1 each — all within §1 = 65–250 and §17 = 956–1077. Recompute the
   boundaries at the tip; do not carry mine, and do not carry the `e1dac06` figures either
   (`re-run` was 2 there and is 4 here — the same finding, a different text).
5. **The whole round is void** if the object I read is not the object under review — if
   `git rev-parse 6110421:governance/candidates/CAND-20260819-ORCHSURF.md` is not blob `7469f4e1`,
   or the file is not 1077 lines. **Note what this falsifier deliberately does not use: the
   content hash.** It is `844de909…acb6dc` at `da47440`, `e1dac06`, `6110421` and `5ea744c` — four
   tips carrying four different texts of this file — because `governance/candidates/` is outside
   the hashed domain. The hash is not a silent instrument here, it is a **blind** one: silent
   implies a signal that failed to fire, blind names one that could never fire, and the property
   that makes it a sound binding is exactly what makes it a useless tripwire. Verify by **blob
   identity**, which is what I did across the two tips this round moved through.

**What would NOT change my mind:** that the remediation is otherwise excellent, or that M-4 is
small. Both are true. Neither makes a false sentence in Layer 1 true, and a reviewer who trades a
finding for the quality of the work around it has stopped being one.

---

## AUTHOR_RESPONSE

Required; silence is not acceptance. **C.3 gives two rounds and this is the second — so if Plan
contests M-4 or the §8 characterisation, the disagreement is adjudicated by `orchestrator` and is
not returned to me.** `DISAGREEMENT_UNRESOLVED` is a legitimate terminal outcome and I record in
advance that I would not treat it as a failure of the exchange.

**To the adjudicator:** M-4 is new, not a re-opening, and I have disclosed that I could have found
it at round 1. If you rule it inadmissible this round, I ask only that it be recorded as an open
defect against the candidate rather than dismissed, so that it does not reach the operator inside a
section whose purpose is accuracy about what is not claimed.

```
main UNCHANGED at 04693e68 · no candidate created · no candidate content modified
no FROZEN document touched · ROOTGUARD not entered · T7 not re-opened
PROBE-ORCHWT-001 leg 3 · Orchestrator WORK_COMMIT capability · Plan's cross-worktree refusal ·
the regression suite — all still owed, none discharged by this verdict
HUMAN_APPROVAL on a MAJOR governance change is the operator's; no verdict here substitutes for it
```
