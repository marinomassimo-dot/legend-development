---
artifact: PATCH SPECIFICATION (draft) — the replacement text ADD-002 authorized as a class, written
  down so that it becomes a durable object that can be read, challenged and falsified
record_id: REV-ORCHSURF-ADD-002-PATCH-SPECIFICATION
authorizes_nothing: this is a DRAFT SPECIFICATION. It is not a patch, not an application of one,
  not a review, not a reopening, not a canonicalization, not an approval and not a governance change
derives_from: CLOSE-REV-ORCHSURF-MIRROR-002-ADD-002 @ aa0e8769b7fdfa9172a4d6e19916cc7f75f422f8
  — which authorizes a CLASS of correction and explicitly requires a separate act (§ 6)
object_described: CAND-20260819-ORCHSURF revision 4 · CANDIDATE_CONTENT_HASH 844de909…acb6dc
  @ BASE_HEAD 04693e68 · CONTENT_TIP 9a70e94d. NOT MODIFIED by this record
written_by: orchestrator
written_at: 2026-08-21T08:53Z
purpose: "Durable specification for later transcription and validation. Not an applied patch."
validation_status: AWAITING MIRROR COMPLIANCE REVIEW
approval: NONE. `HUMAN_APPROVAL` unchanged. `MIRROR_REVIEW` not-PASS. No readiness is implied
scope_negative: no candidate file is edited; no hashed content file is touched; no review closure is
  amended; the `mirror` branch is not written to; canonical `main` is not written to; no
  `ORCHESTRATOR_LEASE` is acquired or claimed; no review round is opened
discipline: append-only
---

# Patch specification — the text ADD-002 authorized as a class, written out as a class instance

## 0 · Rehydration — every value below measured from the repository this session, none from the prompt

```
ACTOR_ID          orchestrator — roles/orchestrator.md frontmatter `actor_id: orchestrator`, and
                  the one-writer clause of runtime/orchestrator_lease.md ("orchestrator ONLY, from
                  the orchestrator worktree"). NOT inferred from cwd, session name or prior chat
AUTHORITY         none is exercised. This record decides nothing. It writes down a text so that a
                  reviewer has an object to read. C.3 rounds are spent and none is opened here
LEASE             ACTIVE by derivation: 0 — python3 framework/scripts/lease_state.py --check, run
                  by me. Two standing findings on historical row #3, both pre-existing, neither
                  touched. No lease is required: this is not a CANONICAL_BATCH_COMMIT
canonical main    04693e683a254ff0a6d0619fba47103a0fb7d122 — from git refs. Root clean, 0 entries
BASE_HEAD         04693e68 — identical to canonical main, verified by ref, not asserted
CONTENT_TIP       9a70e94d6d9863622c22159d0d7f2117b77b793d
BINDING           hash(04693e68, 9a70e94d) = 844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
                  RECOMPUTED by me from this worktree with governance/scripts/candidate_content_hash.py.
                  MATCHES the value ADD-002 carries. 539 included entries, reproduced in § 10
ADDENDUM          CLOSE-REV-ORCHSURF-MIRROR-002-ADD-002 @ aa0e8769, blob e54fe24b — read in full at
                  source, from the repository, this session
CLOSURE           CLOSE-REV-ORCHSURF-MIRROR-002 @ 0a1929e — read at source
ROUNDS            REV-ORCHSURF-MIRROR-002 @ 36e1381 and REV-ORCHSURF-MIRROR-002-R2 @ 95f64f9 —
                  both read at source, both frontmatter verdicts read verbatim
WORKTREES         root · orchestrator · mirror · evidence-index — all 0 dirty entries at the instant
                  this record was written. Neither `mirror` nor `evidence-index` was written to
```

**One thing did not come from the repository and is named as such: nothing.** Plan's transmitted
patch is not in evidence — ADD-002 § 6 established that with its search population, and this record
does not reconstruct it, does not reuse it, and did not consult it. Every sentence in § 3, § 4 and
§ 5 is derived from ADD-002's constraints, from the review records named above, and from the current
candidate text quoted at its measured surface.

---

## 1 · What this object is, and the five things it is not

**It is a durable specification.** ADD-002 § 6 says, plainly, that it *authorizes a CLASS, not a
TEXT*, and that verifying a patch against § 4's six conditions *"is a separate act, it is owed, and
it did not happen here."* The class has no instance in this repository. This record creates one, so
that the instance can be read and attacked rather than described.

```
NOT a patch                  nothing is applied to any candidate file
NOT a review                 no round is opened; REV-ORCHSURF-MIRROR-002 stays closed
NOT a canonicalization       main is untouched; no lease; no GATE asserted
NOT an approval              HUMAN_APPROVAL unchanged; no APPROVAL_ID exists anywhere
NOT a governance change      D.2, C.3, H.1 and P5 are quoted, never amended
```

🔴 **Writing the text down does not make it correct.** This record is the thing to be checked, not
the check. Its own § 8 lists what it decided without a source that settles it, and marks four items
`UNRESOLVED` rather than resolving them by preference.

---

## 2 · The three loci at their surfaces — anchors re-derived, and one anchor corrected

> 🔴 **REVISED at `REV-ORCHSURF-ADD-002-PATCH-SPECIFICATION` revision 2, 2026-08-21.** Two
> measurement defects in this section are corrected below, both found by an independent verifier
> and both reproduced by me before being accepted. **The superseded numbers are kept visible, not
> erased** — the same rule this record applies to the candidate applies to this record. Nothing in
> § 3, § 4, § 5 or § 8 changes: neither defect touched a proposed replacement text, and the
> conclusion each defect was offered in support of survives its own correction. The revision is
> confined to this section and to the methodological statements it caused.

ADD-002 `D-1` holds that a line anchor is valid only at the surface it was taken over. Every number
below is re-derived at each blob **by locating the locus by its content at that blob**, never by
carrying a line number across.

```
                                     @ 9a70e94d        @ 6110421        @ 5a69a05 · 5fa1cf2
                                     blob 2dbe570c     blob 7469f4e1    blob 92c1b7d8
                                     (CONTENT_TIP)     (round-2 obj)    (closing tip · branch tip)
                                     993 lines         1077 lines       1114 lines
L-1  frontmatter `supersedes:`         lines 53–54       lines 53–54       lines 53–54
L-2  § 1 manifest `MIRROR_REVIEW`      lines 135–138     lines 158–161     lines 158–161
L-3  § 17.3 first bullet               lines 978–979     lines 1055–1056   lines 1086–1087
```

🔴 **`OBS-3` — as first written, this table's middle column was carried across from the first, and
the sentence above it denied doing exactly that.** The record claimed `L-2 135–138` and
`L-3 978–979` at `7469f4e1`. Both are wrong, and wrong in the way that matters: they are the
first column's numbers, transcribed. Measured at `7469f4e1`, `L-2` opens at **158** and `L-3` at
**1055**. The three blobs are 993, 1077 and 1114 lines long; only `L-1`, which sits in frontmatter
above every insertion, is genuinely stable across all three.

**The failure was silent, and would not have been caught downstream.** At `7469f4e1`, lines
`135–138` are the `LINT_RESULT` and `PUBLICATION_GATE` manifest rows and lines `978–979` are a
table row about the T10 enumeration method. A transcriber patching that surface by this table would
have destroyed four unrelated manifest lines and a findings-table row, and the result would still
have looked like a manifest. **This is `OBS-1`'s hazard realised inside the record that raised it.**

**ADD-002 names four surfaces; they are three distinct objects.** `5a69a05` and `5fa1cf2` carry the
same blob `92c1b7d8`, verified by `rev-parse` at both commits.

**Byte-identity of the three loci reproduces — and the method is now stated, because it was not.**
As first written this section reported three digests *"by hashing the extracted regions"* and named
neither the extraction nor the hash, so no reader could reproduce them; that is a violation of
`D-1`'s own requirement that a reader be told, committed by the step whose purpose was verification.
The method, stated:

```
EXTRACTION   git cat-file -p <blob> | sed -n '<first>,<last>p'   — the per-blob range in the
             table above, trailing newline included
DIGEST       shasum -a 1 | cut -c1-12                            — SHA-1, truncated to 12 hex

             L-1  3d44eb0b221d      identical at 2dbe570c, 7469f4e1, 92c1b7d8
             L-2  176bae1745ae      identical at all three
             L-3  c0a63e189914      identical at all three

NEGATIVE     the same bytes under SHA-256 give 0b160e9d5646 / 35c56f1caf0e / 50211e63fe2f.
CONTROL      Recorded so the algorithm cannot be mistaken for the default a reader would try
```

**ADD-002's byte-identity claim reproduces**, and it reproduces *at the corrected ranges* — which
is itself the evidence that the hashing was done at the right regions and only the table was
mis-transcribed. Had the middle column been used to extract, the digests would not have matched,
and they do.

🔴 **`OBS-1` — ADD-002's `L-2` anchor is one line below the field it names, and a transcriber
following it literally would corrupt the field.** ADD-002 § 1 gives `L-2` at line `136` / `159`.
Line `136` / `159` is the *second physical line* of the `MIRROR_REVIEW` entry — the line carrying
the false sentence it quotes. The entry itself opens at line **135** / **158**. This is not an error
in the ruling: ADD-002 anchored the false sentence, and the false sentence does begin there. It is a
hazard for transcription, because the replacement must consume the whole field, lines `135–138` /
`158–161`. The same shape applies to `L-1`: ADD-002 gives line `54`, and the clause to be replaced
begins mid-line `53`, after `"…because the bound content moved."`

**The population of false statements was measured, not assumed.** ADD-002 § 4 condition 1 forbids a
fourth locus. I checked whether one exists rather than trusting the count: a case-tolerant search of
the whole candidate at both `2dbe570c` and `92c1b7d8` for every assertion that a review did not
happen —

```
grep -nE "NEVER been reviewed|never been reviewed|No review exists|no review has|NO REVIEW|
          not been reviewed|unreviewed|has reviewed"
  @ 2dbe570c → 3 hits: 54, 136, 978        and they are exactly L-1, L-2, L-3
  @ 92c1b7d8 → 3 hits: 54, 159, 1086       and they are exactly L-1, L-2, L-3
```

The `L-2` hit lands at `136` / `159`, the field's *second* physical line, not at its opening `135` /
`158` — which is `OBS-1` above, arriving from the other direction. **No fourth locus exists.**

**And the document already contradicts itself — but not at the count first recorded here.**

🔴 **`OBS-4` — the count of seven was wrong under every reading, and one of the seven was a
different candidate's review.** As first written this section stated that `REV-ORCHSURF-MIRROR-002`
*"is named by the candidate at seven places (`92c1b7d8` lines 480, 980, 981, 985, 1002, 1092,
1105)"*. Re-measured at `92c1b7d8`:

```
LINE 480 IS NOT A HIT       it reads REV-ORCH*WT*-MIRROR-002 — the round-2 review of
                            CAND-20260817-ORCHWT, a different candidate. The id differs by two
                            characters and was matched on its resemblance
SUBSTRING HITS              6 lines — 980, 981, 985, 1002, 1092, 1105. Not seven
EXACT-TOKEN BREAKDOWN of those six, because the id is a prefix of two other identifiers:
  REV-ORCHSURF-MIRROR-002        3 — lines 980 (§ 17.1), 1002 (§ 17.1a), 1105 (§ 17.3)
  REV-ORCHSURF-MIRROR-002-R2     2 — lines 985 (§ 17.1), 1092 (§ 17.3). Round 2 is a distinct
                                     record and naming it is not naming round 1
  OPEN-REV-ORCHSURF-MIRROR-002   1 — line 981 (§ 17.1). An orchestrator open-record, not a review
```

So the honest number is **3** under exact matching, **6** by substring, and **never 7**. Section
attribution was checked rather than assumed: *"including § 17.1"* is correct — 980, 981 and 985 all
fall under `### 17.1`. The `M-4` remedy bullet below `L-3` is line 1092, and it names `-R2`, not the
bare id.

**The conclusion the miscount was offered in support of stands, and does not depend on the number.**
`§ 17.3`'s first bullet at `1086–1087` denies that any review exists, while the same document names
that review, its second round and its open-record across six lines — one of them at `1105`, inside
`§ 17.3` itself. **The correction removes an internal contradiction between § 17.3's first bullet
and § 17.3's second**, exactly as stated. Only the measurement behind it was wrong.

**The D.2 surface was checked too, and it is not ambiguous.** `governance/annex_d_commit_batch.md`
is blob `23895689` at `main`, at `orchestrator`, at `orchestrator-surface` and at `CONTENT_TIP`
`9a70e94d` — one object, four surfaces. Line 38 reads `MIRROR_REVIEW: n/a | PASS | FAIL + REVIEW_ID`
and is the **only** occurrence of `MIRROR_REVIEW` in the entire annex; nothing there declares the
enumeration exhaustive, and nothing there declares it open. 🔴 **That is a measurement, not a
reading.** Which of the two it is remains `UNRESOLVED-A` in § 8, unchanged, undecided, and routed
rather than settled — D.2 is not amended here and no reading of it is adopted.

---

## 3 · `L-1` — proposed replacement · frontmatter `supersedes:`

**Current text, verbatim at `92c1b7d8` lines 53–54** (identical at the other two blobs):

```
  Annex D.2 invalidates them because the bound content moved. REV-ORCHSURF-MIRROR-001 reviewed
  revision 1; NO REVIEW has ever been performed on revision 2, 3 or 4
```

**Proposed replacement for lines 53–54.** The first sentence of line 53 is re-emitted unchanged; only
the clause after it is corrected.

```
  Annex D.2 invalidates them because the bound content moved. REV-ORCHSURF-MIRROR-001 reviewed
  revision 1; revisions 2 and 3 have NEVER been reviewed; revision 4 WAS reviewed —
  REV-ORCHSURF-MIRROR-002, rounds 1 and 2, REQUEST CHANGES at both, closed at
  CLOSE-REV-ORCHSURF-MIRROR-002 with every finding disposed and no DISAGREEMENT_UNRESOLVED.
  Examined is not approved: no reviewer issued PASS on revision 4 and HUMAN_APPROVAL is
  unchanged. Until CLOSE-REV-ORCHSURF-MIRROR-002-ADD-002 this clause read "NO REVIEW has ever
  been performed on revision 2, 3 or 4" — true when written, false from the moment
  REV-ORCHSURF-MIRROR-002 reviewed revision 4, and kept rather than erased because a record
  edited to agree with its own present is no longer evidence of what it said
```

---

## 4 · `L-2` — proposed replacement · § 1 manifest, `MIRROR_REVIEW` field

**Current text, verbatim at `92c1b7d8` lines 158–161** (`2dbe570c` lines 135–138, byte-identical):

```
MIRROR_REVIEW             REV-ORCHSURF-MIRROR-001 returned REQUEST CHANGES on revision 1.
                          Revisions 2, 3 and 4 have NEVER been reviewed. None performed, none
                          assumed, and revision 4 inverts the direction revision 1 was reviewed
                          under — so the earlier review does not transfer
```

**Proposed replacement for the whole field.** The label column is 26 characters wide, matching the
surrounding manifest rows; continuation lines are indented 26 spaces.

```
MIRROR_REVIEW             REV-ORCHSURF-MIRROR-002 — revision 4 WAS reviewed, over two rounds.
                          Round 1, REV-ORCHSURF-MIRROR-002: REQUEST CHANGES. Round 2,
                          REV-ORCHSURF-MIRROR-002-R2: REQUEST CHANGES. Closed at
                          CLOSE-REV-ORCHSURF-MIRROR-002 — findings M-1, M-2, M-3, M-4 and the
                          adjudicator residual R-1 all disposed, no DISAGREEMENT_UNRESOLVED
                          NOT `PASS`, and not any other value D.2 declares. D.2 gives
                          `n/a | PASS | FAIL + REVIEW_ID`, and the true state is none of the
                          three: `n/a` would deny a review that happened, `FAIL` would assert a
                          verdict no round returned, and `PASS` was issued by no reviewer on
                          revision 4. The state is named here rather than forced into a legal
                          value, and the vocabulary mismatch is disclosed rather than resolved
                          silently. CHANGE_CLASS is MAJOR: a `PASS` written into this field
                          would manufacture a GATE input out of a review that produced none
                          Examination is not approval, and this field is not one. HUMAN_APPROVAL
                          is unchanged and no APPROVAL_ID exists
                          REV-ORCHSURF-MIRROR-001 returned REQUEST CHANGES on revision 1 and does
                          NOT transfer — revision 4 inverts the direction revision 1 was reviewed
                          under. Revisions 2 and 3 have NEVER been reviewed
                          Until CLOSE-REV-ORCHSURF-MIRROR-002-ADD-002 this field read "Revisions
                          2, 3 and 4 have NEVER been reviewed. None performed, none assumed" —
                          true when written, false from the moment REV-ORCHSURF-MIRROR-002
                          reviewed revision 4
```

---

## 5 · `L-3` — proposed replacement · § 17.3, first bullet

**Current text, verbatim at `92c1b7d8` lines 1086–1087** (`2dbe570c` lines 978–979, byte-identical):

```
- **It does not claim Mirror has reviewed this.** No review exists for revisions 2, 3 or 4, and
  revision 1's review was conducted under the opposite direction, so it does not transfer.
```

**Proposed replacement.** The bold lead is re-headed, because the section heading above it is
*"What revision 4 does NOT claim"* and the existing lead is now false as a lead. The form follows the
bullet immediately below it — the `M-4` remedy — which ADD-002 § 4 names as the model: state what is
true now, state what was true before, say why the old clause was false.

```
- **It does not claim Mirror's review approved it.** Mirror DID review revision 4 —
  `REV-ORCHSURF-MIRROR-002`, rounds 1 and 2, `REQUEST CHANGES` at both, closed at
  `CLOSE-REV-ORCHSURF-MIRROR-002` with every finding disposed. What that establishes is that the
  package was examined, which is not that it may be canonicalized: no reviewer issued `PASS` on
  revision 4 and `HUMAN_APPROVAL` is unchanged. Revisions 2 and 3 have NEVER been reviewed, and
  revision 1's review was conducted under the opposite direction, so it does not transfer.
  *Until `CLOSE-REV-ORCHSURF-MIRROR-002-ADD-002` this bullet read "It does not claim Mirror has
  reviewed this. No review exists for revisions 2, 3 or 4" — true when written, and false from the
  moment `REV-ORCHSURF-MIRROR-002` reviewed revision 4. The bullet is re-headed rather than deleted,
  because a list of what revision 4 does not claim still owes a true entry on the review, and the
  old sentence is kept visible because a record edited to agree with its own present is no longer
  evidence of what it said.*
```

---

## 6 · Explicit constraints the replacement text must carry, and where each is discharged

Every constraint is stated as a falsifiable predicate over the three texts above, so a reviewer can
fail one without arguing about intent.

| # | Constraint | Source | Discharged at |
|---|---|---|---|
| 1 | **revision 4 WAS reviewed** | ADD-002 § 1; `REV-ORCHSURF-MIRROR-002` frontmatter `object: … revision 4` | L-1, L-2, L-3 |
| 2 | **review means examination, not approval** | `CLOSE-REV-ORCHSURF-MIRROR-002` § 1 — *"It means the package was examined … It is not an approval and not a readiness certificate"* | L-1 "Examined is not approved"; L-2 "Examination is not approval"; L-3 "examined, which is not that it may be canonicalized" |
| 3 | **`HUMAN_APPROVAL` remains NONE** | ADD-002 frontmatter `approval:`; ADD-002 § 4 condition 3 | all three loci: "`HUMAN_APPROVAL` is unchanged", "no `APPROVAL_ID` exists". See `D-5` in § 8 for why the words are these |
| 4 | **revisions 2 and 3 were never reviewed** | measured: no review record in the repository names ORCHSURF revision 2 or 3 — `REV-ORCHSURF-MIRROR-001` names revision 1, `-002` and `-002-R2` name revision 4 | L-1, L-2, L-3 |
| 5 | **revision 1's review does not transfer** | `REV-ORCHSURF-MIRROR-002` frontmatter — *"supersedes_scope_of: nothing. REV-ORCHSURF-MIRROR-001 reviewed revision 1 under the opposite remedy direction and transfers NOTHING as a verdict"* | L-2, L-3. **Deliberately NOT added to L-1**, which never carried it — adding it would be adjacent tidying, forbidden by ADD-002 § 4 condition 1 |
| 6 | **`REV-ORCHSURF-MIRROR-002` is closed** | `CLOSE-REV-ORCHSURF-MIRROR-002` frontmatter `closes: … rounds 1 and 2`, `outcome: FINDINGS RAISED AND DISPOSED` | L-1, L-2, L-3 |
| 7 | **C.3 rounds are spent** | ADD-002 § 3 — *"the rounds are spent, and opening a third is a thing only I may do. I decline to do it"* | **not written into the candidate.** It is a fact about the review process, not about the candidate; writing it into a locus would exceed the three. Recorded here instead |
| 8 | **no readiness implication** | ADD-002 § 6 — *"No readiness. Canonicalization … would still require `HUMAN_APPROVAL`, an `ACTIVE` `ORCHESTRATOR_LEASE` and `GATE 0–5`"* | L-3 "which is not that it may be canonicalized"; L-2's `PASS`/GATE clause; and negatively, by condition 5 in § 7 below |

### 6.1 · ADD-002 § 4's six conditions, checked against the proposed text

```
1  LOCI              three loci only. No fourth locus proposed. The population of false
                     statements was measured (§ 2) and is exactly three. PASS
2  REVIEW ≠ APPROVAL  present at all three loci, explicitly. PASS
3  HUMAN_APPROVAL     not set, not prefilled, not described as pending or in progress. PASS
4  CLOSURE LANGUAGE   "examined", "findings disposed", "not approved", "not that it may be
                     canonicalized" — the closure's own register. PASS
5  VOCABULARY         no word implying approval, pass, clearance or readiness is ASSERTED.
                     `PASS` appears only under negation. See D-3 in § 8 — this is a reading of
                     condition 5, and the reading is declared rather than assumed
6  MIRROR_REVIEW      not `PASS`. The field names the review, its rounds, its verdict and its
                     closure, and asserts no verdict the record does not contain. PASS on the
                     letter of condition 6 — and see UNRESOLVED-A, which is about D.2, not
                     about condition 6
```

---

## 7 · Derivation ledger — no clause without a source

Every non-trivial clause in § 3–§ 5 traces to one of the three permitted sources. Nothing traces to
chat, to memory, or to Plan's transmitted patch.

| Clause | Source, read at |
|---|---|
| "rounds 1 and 2" | `CLOSE-REV-ORCHSURF-MIRROR-002` frontmatter `closes: REV-ORCHSURF-MIRROR-002, rounds 1 and 2` |
| "REQUEST CHANGES at both" | `REV-ORCHSURF-MIRROR-002` frontmatter `verdict: REQUEST CHANGES`; `REV-ORCHSURF-MIRROR-002-R2` frontmatter `verdict: REQUEST CHANGES` |
| "M-1, M-2, M-3, M-4 and the adjudicator residual R-1" | `CLOSE-REV-ORCHSURF-MIRROR-002` § 3 disposition table, verbatim row labels |
| "no DISAGREEMENT_UNRESOLVED" | `CLOSE-REV-ORCHSURF-MIRROR-002` frontmatter `outcome:` |
| "every finding disposed" | same, `outcome: FINDINGS RAISED AND DISPOSED` |
| "`n/a \| PASS \| FAIL + REVIEW_ID`" | `governance/annex_d_commit_batch.md:38`, quoted, not paraphrased |
| "CHANGE_CLASS is MAJOR" | candidate § 1, line 128 @ `92c1b7d8` / line 108 @ `2dbe570c` — *"CHANGE_CLASS  MAJOR — unchanged from revision 3"* |
| "would manufacture a GATE input" | ADD-002 § 4 — *"it would manufacture a GATE input for a MAJOR out of a correction whose entire warrant is that it adds no judgement"* |
| "no PASS was issued by any reviewer on revision 4" | ADD-002 § 4, verbatim sense; corroborated by both round frontmatters, neither of which contains `PASS` as a verdict |
| "examined … not that it may be canonicalized" | `CLOSE-REV-ORCHSURF-MIRROR-002` § 1 and the commit subject of `0a1929e` |
| "a record edited to agree with its own present is no longer evidence of what it said" | ADD-002 § 4, verbatim |
| "revision 4 inverts the direction revision 1 was reviewed under" | the current candidate text at `L-2`, preserved verbatim; independently corroborated by `REV-ORCHSURF-MIRROR-002` `supersedes_scope_of:` |
| "true when written … false now" | ADD-002 § 1 — *"All three were true when written and are false now"* |

---

## 8 · Declared wording decisions, and four items marked `UNRESOLVED`

The instruction under which this record was written requires that a wording choice needing
interpretation beyond the three permitted sources be stopped on and marked, not resolved by
preference. Five decisions are declared with their grounds; four items are marked `UNRESOLVED`.

### Declared decisions — grounded, but a reviewer may reject the ground

```
D-1  VOICE — documentary third person, not first person.
     The model ADD-002 names (§ 17.3's M-4 bullet) is written in Plan's first person: "I
     corrected §1 …". This specification is written by orchestrator, and ADD-002 § 6 records that
     the transcription is a separate act by someone else. Writing "I" would attribute an act to
     whoever transcribes it. The departure is in PERSON, not in FUNCTION: the model's three parts
     — true now, true before, why it was false — are all preserved.

D-2  L-3's BOLD LEAD IS RE-HEADED, not preserved.
     § 17.3 is headed "What revision 4 does NOT claim"; the existing lead "It does not claim
     Mirror has reviewed this" is false as a lead once the review exists. Deleting the bullet was
     considered and REJECTED: ADD-002 § 4 requires the correction stay auditable, and a deleted
     bullet destroys the evidence that it was needed. The lead is inside the locus — ADD-002 § 1
     quotes L-3 including its lead.

D-3  `PASS` APPEARS, ONLY UNDER NEGATION.
     Condition 5 forbids "no word implying approval, pass, clearance or readiness anywhere in the
     three loci". The proposed texts use `PASS` exclusively to DENY it. Ground: ADD-002 § 4
     reasons in exactly that register and its own prose says "no `PASS` was ever issued by any
     reviewer on revision 4". 🔴 If Mirror reads condition 5 as a literal token ban rather than an
     assertion ban, ALL THREE replacements fail it and must be re-worded. This is stated rather
     than assumed, because the reading is mine.

D-4  L-1's AUDIT TRAIL SITS INSIDE YAML FRONTMATTER.
     ADD-002's model is prose in the document body. Frontmatter is a different medium and ADD-002
     does not address it. Ground for proceeding: the `supersedes:` key already carries several
     sentences of prose, so the form is not new to this file. A reviewer may hold that an audit
     trail belongs in § 1 and that frontmatter should carry the corrected fact alone.

D-5  "HUMAN_APPROVAL is unchanged" / "no APPROVAL_ID exists" — NOT "NONE", NOT "n/a".
     ADD-002 says HUMAN_APPROVAL "remains NONE". The candidate's own field literally reads
     `n/a — not requested, not prefilled, and no APPROVAL_ID exists`. Writing "NONE" into a
     corrected locus would describe the field with a value it does not carry; writing "n/a" would
     restate a different field's value inside these three. Both readings are true of the wording
     chosen, so the disagreement is avoided rather than adjudicated.
```

### `UNRESOLVED` — no permitted source settles these, and none is settled here

```
🔴 UNRESOLVED-A   MAY THE CORRECTED `MIRROR_REVIEW` CARRY A VALUE OUTSIDE D.2's VOCABULARY?
                  ADD-002 § 4 condition 6 forbids `PASS` and directs that the value "names the
                  review, its rounds, its verdict and its closure". D.2 declares the field as
                  `n/a | PASS | FAIL + REVIEW_ID`, and reads as an exhaustive enumeration.
                  ADD-002 does not amend D.2 and could not: it is an adjudication, not a
                  governed change. So the value in § 4 is directed by the addendum and is
                  outside the annex's enumeration, and NOTHING in ADD-002, in the closure, or in
                  either round resolves whether that is permitted or requires a governed
                  amendment to D.2. The text is written as ADD-002 directs; the conflict is
                  routed, not decided.

🔴 UNRESOLVED-B   WHO TRANSCRIBES.
                  ADD-002 § 4 is headed "Conditions on Plan's patch", and § 6 records that Plan's
                  patch has no durable trace. This specification is not Plan's patch. Whether a
                  text authored by the adjudicator may be transcribed by the adjudicator, or must
                  be routed to Plan as the candidate's author, is settled by no source I may use.

🔴 UNRESOLVED-C   AT WHICH SURFACE THE TRANSCRIPTION LANDS.
                  The candidate exists at `5fa1cf2` (blob 92c1b7d8) on `orchestrator-surface`;
                  the binding names CONTENT_TIP `9a70e94d` (blob 2dbe570c). Patching at the
                  branch tip leaves the corrected bytes absent from CONTENT_TIP; patching at
                  CONTENT_TIP would be a re-bind, which ADD-002 § 2 says it does not authorize.
                  MEASURED, so the choice is not blind: either way the binding is unmoved, because
                  governance/candidates/ is excluded from the hashed domain (§ 10). What is NOT
                  settled is which surface a reviewer should read the patch at, and D-1 of this
                  review says a reader must be told.

🔴 UNRESOLVED-D   WHETHER § 6 CONSTRAINT 7 ("C.3 rounds are spent") BELONGS IN THE CANDIDATE.
                  It is required by the task instruction to be carried by this specification, and
                  it IS carried here. It is a fact about the review, not about the candidate, and
                  writing it into a locus would exceed the three ADD-002 permits. Recorded in § 6
                  rather than in § 3–§ 5. A reviewer may hold that L-2 should carry it.
```

---

## 9 · Validation status

```
VALIDATION STATUS     AWAITING MIRROR COMPLIANCE REVIEW
WHAT IS ASKED         does the text in § 3, § 4 and § 5 faithfully transcribe the closed record,
                      and does it satisfy ADD-002 § 4's six conditions?
FALSIFIER             the closure and the two rounds, read against these three texts. This is a
                      real falsifier — ADD-002 § 3(c) says so explicitly, and § 5 routes exactly
                      this question to Mirror as a CHALLENGE under Annex F, not as a review round
NOT ASKED             whether REV-ORCHSURF-MIRROR-002 occurred (ADD-002 § 3(c): Mirror is the
                      evidence and cannot be independent of its own occurrence)
NOT ASKED             approval, readiness, canonicalization, or any GATE verdict
ON REJECTION          the text is rewritten here. Nothing downstream has happened that would need
                      undoing, which is the reason this exists as a specification and not a patch
```

---

## 10 · Separate observation — `OBS-2`, the hash divergence between worktrees

**Recorded as a finding. NOT a blocker for this record, NOT fixed, NOT within its scope.** No file
under `governance/scripts/` is modified by this record and no hashing behaviour is changed.

**Reported by Mirror:** `candidate_content_hash.py` reads `plan_defined_parameters.md` from the
invoking worktree; orchestrator worktree yields `844de909…`, mirror worktree yields `2081220b…`;
cause, different P5 `CONTROL_PLANE_ROOTS`.

🔴 **I did not file this as testimony, because it was measurable and this laboratory's own closure
lists "testimony where measurement was available" among its seven structural instances.** Measured
from the shared object store, without running anything inside the `mirror` worktree and without
writing to it:

```
candidate_content_hash.py blob      orchestrator          cd5776d3
                                    orchestrator-surface  cd5776d3
                                    main                  cd5776d3
                                    @ CONTENT_TIP         cd5776d3
                                    mirror                be20e303   ← different object

plan_defined_parameters.md blob     main / surface / @tip e1f9e1ec   v4 · 3 roots
                                    orchestrator          09bd9e03   v4 · 3 roots
                                    mirror                a139b283   v3 · 2 roots
```

**The two versions of the script differ in the one place that matters.** At `cd5776d3`,
`parse_p5(tip)` calls `git show {tip}:governance/plan_defined_parameters.md` and its own docstring
states the rule: *"The rule is read from the tip being hashed, never from the working tree … Reading
the rule from the checkout made it a function of `(base, tip, whichever branch happened to be
checked out)`."* At `be20e303`, `parse_p5()` takes no tip and calls `PARAMETERS.read_text()` — the
checked-out file.

**So the divergence reproduces exactly, and the cause is narrower than "the script reads from the
worktree".** With a positive control first, so the reproduction is not just a matching number:

```
POSITIVE CONTROL   v4 + {governance/candidates/, ledger/, reviews/}
                   → 844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc · 539 entries
                   MATCHES the tool's output and ADD-002's DOMAIN line. The reproduction is faithful

SIMULATED MIRROR   v3 + {governance/candidates/, ledger/}
                   → 2081220b7529d5abbe481d3600eb2d5ddcf0138b62e1c2a89da90b4186ad8cdf · 543 entries
                   MATCHES the value Mirror reported
```

**Three corrections to the framing, all measured:**

1. **It is worktree STALENESS, not a live defect in the current tool.** The behaviour Mirror
   describes is a property of the copy checked out in the `mirror` worktree. The version at
   `main`, at `orchestrator-surface`, at `orchestrator` and at the tip being hashed does not have
   it, and documents it as a defect it fixed.
2. **`CONTROL_PLANE_ROOTS` is one of two differences, and not sufficient on its own.**
   `CANDIDATE_HASH_VERSION` also differs — `v3` against `v4` — and the prefix is inside the hashed
   serialization, so it alone moves the value even where the root sets agree. The `reviews/` root
   accounts for the entry-count delta, 543 → 539.
3. **The stale P5 is stale for a stated reason.** `e1f9e1ec` § P5 records why `v4` exists: the
   amendment added `reviews/` and *"the prefix must move whenever the rule does rather than
   whenever the output does"*. The mirror checkout predates that amendment.

```
IMPACT ON THIS RECORD    none. The binding was recomputed from THIS worktree with the current
                         script and matches at 844de909…acb6dc
IMPACT ON ADD-002        none measured. Its DOMAIN line — 539 included, 49 excluded — reproduces
OWNER                    UNASSIGNED. Not routed, not opened, not fixed here
NOT ESTABLISHED          whether any recorded value anywhere in this repository was computed from a
                         stale checkout. I did not survey for that, and do not claim I did
```

---

## 11 · Standing at the instant this record was written

```
main                  04693e68 — UNCHANGED. Root checkout clean, 0 entries, all session
candidate blob        92c1b7d8 @ 5fa1cf2 · 2dbe570c @ 9a70e94d — both UNCHANGED, not opened
BASE_HEAD             04693e68 — UNCHANGED
CONTENT_TIP           9a70e94d — UNCHANGED, not re-bound
binding               844de909…acb6dc — recomputed by me this session, UNCHANGED
review                REV-ORCHSURF-MIRROR-002 CLOSED. Not reopened. No round opened. C.3 spent
lease                 ACTIVE by derivation: 0. None acquired, none claimed
approval              NONE — not sought, not granted, not inferred, none exists to be found
mirror worktree       not written to. evidence-index worktree not written to. Both 0 dirty
this record           reviews/orchestrator/ — a declared CONTROL_PLANE_ROOT under P5 at every
                      surface that carries v4, and outside every candidate domain. It describes a
                      proposed correction; it constitutes no candidate and applies nothing
```
