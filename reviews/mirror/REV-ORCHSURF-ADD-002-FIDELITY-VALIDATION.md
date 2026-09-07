---
artifact: MIRROR FIDELITY VALIDATION — does the specified transcription say what the closed record
  says, and nothing else
record_id: REV-ORCHSURF-ADD-002-FIDELITY-VALIDATION
source: CLOSE-REV-ORCHSURF-MIRROR-002-ADD-002 @ aa0e8769b7fdfa9172a4d6e19916cc7f75f422f8,
  blob e54fe24b — the authorization source, read at source this session
target: REV-ORCHSURF-ADD-002-PATCH-SPECIFICATION @ 1e2fabd3c73a908bca2439cf080a7c83e8b17d30,
  blob ab3a946c — the proposed transcription specification
candidate_context: CAND-20260819-ORCHSURF revision 4, blob 92c1b7d8 @ orchestrator-surface
  aa49df9 — read ONLY to verify referenced loci and unchanged source context. Not edited
validated_by: mirror
validated_at: 2026-08-21
question_answered: does the patch specification faithfully transcribe the correction ADD-002
  authorized? That question ONLY
scope_negative: this is NOT a C.3 review round; no previous Mirror round is reopened; ORCHSURF is
  not approved; the candidate is not approved; this is not HUMAN_APPROVAL; nothing is canonicalized;
  the transcription is NOT executed; UNRESOLVED-A, -B, -C and -D are NOT resolved
discipline: append-only
---

# Fidelity validation — the text was checked against the record, not against the intent

## 0 · Identity and rehydration — read from the repository, none from the prompt

```
ACTOR_ID          mirror — roles/mirror.md frontmatter `actor_id: mirror`, `worktree: mirror`
ROLE SOURCE       roles/mirror.md · CLAUDE.md § 1 · governance/annex_c_review_protocol.md
AUTHORITY         inspect repository evidence, compare artefacts, produce this report. Mirror
                  "holds no command over any actor and produces no primary evidence"
                  (roles/mirror.md). Nothing below is a verdict on ORCHSURF
BOUNDARY          Mirror does NOT edit the candidate, the patch specification or ADD-002; does not
                  transcribe; does not create HUMAN_APPROVAL; does not resolve governance questions

branch            mirror
HEAD              dfdfee5732d777b663b6089200e374d9f4d4e823
worktree          <REPO_ROOT>/.claude/worktrees/mirror
git status        clean, 0 entries, at the instant this record was written
```

**The three source artefacts are not on this branch and were read as repository objects**, which is
what "repository objects only" permits. `git cat-file` and `git show` against the shared object
store; nothing checked out, nothing written outside `reviews/mirror/`.

---

## 1 · VALIDATION_RESULT

```
TASK_STATUS           COMPLETED
VALIDATION_RESULT     FAITHFUL — with three findings, none of which defeats fidelity
```

**What that means and does not mean.** It means: the three proposed replacement texts say what
`CLOSE-REV-ORCHSURF-MIRROR-002` and its two rounds say, at the three loci ADD-002 named, within the
six conditions ADD-002 set, adding no judgement the record does not contain and no approval of any
kind. It does **not** mean the specification is complete, that its supporting measurements are all
sound — two are not, see `F-1` and `F-2` — or that anything downstream is cleared.

Every measurement the specification makes about the candidate was **re-run by me** rather than read.
All of them reproduce. That is stated because the specification's own § 2 records two defects found
by a prior verifier, and a validator that accepted the corrected numbers on the strength of the
correction would be repeating the failure the correction cured.

---

## 2 · SOURCE_BINDING

```
ADD-002 commit        aa0e8769b7fdfa9172a4d6e19916cc7f75f422f8   blob e54fe24b
                      reviews/orchestrator/CLOSE-REV-ORCHSURF-MIRROR-002-ADD-002.md
                      branch `orchestrator`

PATCH_SPEC commit     1e2fabd3c73a908bca2439cf080a7c83e8b17d30   blob ab3a946c
                      reviews/orchestrator/REV-ORCHSURF-ADD-002-PATCH-SPECIFICATION.md
                      branch `orchestrator` (tip). Two commits in its history — d538263 then
                      1e2fabd — and BOTH touched that one file and nothing else, verified by
                      `git show --stat`

candidate commit      5a69a05da563576ab2754d9a1fcc9ead3a17989a — last commit to touch the file
                      blob 92c1b7d8be169232613ae8b219112a09d7b315dc, IDENTICAL at the
                      `orchestrator-surface` tip aa49df9. The candidate has NOT moved since closure
                      governance/candidates/CAND-20260819-ORCHSURF.md — absent from `main`

closure               CLOSE-REV-ORCHSURF-MIRROR-002 @ 0a1929e — read at source
rounds                REV-ORCHSURF-MIRROR-002 · REV-ORCHSURF-MIRROR-002-R2 — both read at source
```

---

## 3 · CHECKS

### 3.1 · AUTHORIZATION BOUNDARY

| Requirement | Evidence | Result |
|---|---|---|
| ADD-002 authorizes only transcription | ADD-002 § 4 heading — *"authorized as TRANSCRIPTION, and as nothing else"*; § 3 classification `CONTROL-PLANE HISTORICAL-METADATA CORRECTION`; § 6 — it *"authorizes a CLASS, not a TEXT"* | **PRESENT** |
| No new judgement introduced | every non-trivial clause in the specification's § 3–§ 5 re-traced by me to the closure, a round frontmatter, the annex or the candidate's own preserved text. All trace. Two elaborations are the exception — `F-3` | **PRESENT** |
| No approval language introduced | exhaustive token sweep of the three proposed texts for the approval family. Every occurrence is negated or is a quotation of D.2's enumeration. `PASS` never appears as an assertion | **PRESENT** |
| No canonicalization introduced | `main` @ 04693e68 does not carry the candidate at all; both specification commits touched one file in `reviews/orchestrator/`; candidate blob unmoved at 92c1b7d8; no lease claimed | **PRESENT** |

### 3.2 · THE THREE TRANSCRIPTION LOCI

**Anchors re-derived by content at each blob, never carried across.** ADD-002 `D-1`'s own rule,
applied to ADD-002.

```
                                  @ 2dbe570c        @ 7469f4e1        @ 92c1b7d8
                                  (CONTENT_TIP)     (round-2 obj)     (closing · branch tip)
                                  993 lines         1077 lines        1114 lines
L-1  frontmatter `supersedes:`      53–54             53–54             53–54
L-2  § 1 manifest MIRROR_REVIEW     135–138           158–161           158–161
L-3  § 17.3 first bullet            978–979           1055–1056         1086–1087

BYTE-IDENTITY REPRODUCED, method re-run by me exactly as the specification states it
  extraction  git cat-file -p <blob> | sed -n '<first>,<last>p'
  digest      shasum -a 1 | cut -c1-12
  L-1  3d44eb0b221d    L-2  176bae1745ae    L-3  c0a63e189914    identical at all three blobs
```

**All nine digests match the specification's § 2 table.** The corrected middle column is correct;
the superseded one was not, and the specification says so rather than erasing it.

---

**L-1 · frontmatter `supersedes:`**

```
ADD-002 WORDING       "REV-ORCHSURF-MIRROR-001 reviewed revision 1; NO REVIEW has ever been
                       performed on revision 2, 3 or 4"
SOURCE VERIFIED       verbatim at 92c1b7d8 lines 53–54. MATCHES byte for byte
PROPOSED              revision 1 reviewed by -001; revisions 2 and 3 never reviewed; revision 4
                      WAS reviewed — -002, rounds 1 and 2, REQUEST CHANGES at both, closed at
                      CLOSE-REV-ORCHSURF-MIRROR-002, every finding disposed, no
                      DISAGREEMENT_UNRESOLVED; "Examined is not approved"; audit trail retained
MEANING & SCOPE       PRESERVED. The scope claim that revisions 2 and 3 are unreviewed survives
                      intact; only the false conjunct about revision 4 is corrected. Line 53's
                      leading sentence is re-emitted unchanged, verified against the blob
ADDITIONAL INTERP.    the transfer clause is deliberately NOT added — L-1 never carried it, and
                      adding it would be the adjacent tidying condition 1 forbids. Correct
```

**L-2 · § 1 manifest, `MIRROR_REVIEW`**

```
ADD-002 WORDING       "REV-ORCHSURF-MIRROR-001 returned REQUEST CHANGES on revision 1.
                       Revisions 2, 3 and 4 have NEVER been reviewed. None performed, none
                       assumed …"
SOURCE VERIFIED       verbatim at 92c1b7d8 lines 158–161. MATCHES
PROPOSED              names the review, both rounds, both verdicts, the closure, the five disposed
                      findings, the absence of DISAGREEMENT_UNRESOLVED; states NOT `PASS` and
                      discloses the D.2 vocabulary mismatch; preserves the -001 non-transfer
                      clause verbatim in substance; carries the audit trail
MEANING & SCOPE       PRESERVED, and geometry preserved: label column 26 wide, continuations
                      indented 26 — re-measured against the surrounding manifest rows, which use
                      exactly 26. Max proposed line 99 chars against 106 already present in the
                      block. No LINT rule and no script anywhere parses MIRROR_REVIEW — verified
ADDITIONAL INTERP.    YES, two per-value grounds ADD-002 does not supply. See F-3
```

**L-3 · § 17.3 first bullet**

```
ADD-002 WORDING       "It does not claim Mirror has reviewed this. No review exists for revisions
                       2, 3 or 4, and revision 1's review was conducted under the opposite
                       direction, so it does not transfer."
SOURCE VERIFIED       verbatim at 92c1b7d8 lines 1086–1087. MATCHES. ADD-002 quotes the bold lead,
                      so the lead IS inside the locus and re-heading it does not exceed it
PROPOSED              re-headed to "It does not claim Mirror's review approved it"; states the
                      review occurred; "examined, which is not that it may be canonicalized";
                      preserves both surviving true clauses; audit trail in italics
MEANING & SCOPE       PRESERVED, and the section stays true to its heading "What revision 4 does
                      NOT claim". I read all nine bullets of § 17.3 at source: after the
                      correction no surviving bullet contradicts the new first bullet, and two of
                      them (1092, 1105) already name the review — which is the internal
                      contradiction the correction removes
ADDITIONAL INTERP.    the re-heading is a wording choice, declared as D-2 with its ground, and the
                      ground holds: deleting the bullet would destroy the evidence of the defect
```

### 3.3 · THE SIX CONDITIONS OF ADD-002 § 4

| # | Condition | Evidence | Result |
|---|---|---|---|
| 1 | **LOCI** — three only, no fourth, no adjacent tidying, no restructure | three replacements, at exactly L-1/L-2/L-3. I re-ran the specification's population grep (3 hits at each of 2dbe570c and 92c1b7d8, exactly the three loci) **and an independent second sweep with different vocabulary** — `awaiting review`, `pending review`, `not yet reviewed`, `no reviewer`, `review has not/never`, `un-reviewed`, `without a review` — which returns **zero** additional hits. The two anticipatory sentences at 944 and 966 are hortatory ("Mirror should …"), not assertions of non-occurrence, and are not falsified by the review having happened | **PRESENT** |
| 2 | **REVIEW ≠ APPROVAL** | explicit at all three: "Examined is not approved" (L-1) · "Examination is not approval, and this field is not one" (L-2) · "examined, which is not that it may be canonicalized" (L-3) | **PRESENT** |
| 3 | **HUMAN_APPROVAL stays NONE** — not pending, not in progress, not prefilled | the field at line 162 is outside all three loci and is untouched. No locus sets it, describes it as pending or in progress, or prefills an `APPROVAL_ID`; all three assert the negative. Discharged — but the *wording* chosen departs from ADD-002's own word on a falsified ground: `F-2` | **PRESENT** |
| 4 | **CLOSURE LANGUAGE survives** — examined, findings disposed, not approved, not certified ready | verified against the closure at source. Closure § 1: *"It means the package was examined"* · *"It is not an approval and not a readiness certificate"*. All four elements appear across the three loci; the readiness element appears only in L-3, the "not approved" element in all three | **PRESENT** |
| 5 | **VOCABULARY** — no word implying approval, pass, clearance or readiness | every approval-family token in the three texts is either negated or a verbatim quotation of D.2's enumeration. The specification declares (D-3) that under a *literal token ban* all three fail. **That reading is not available**: condition 6 requires the field to disclose that it is not `PASS`, which cannot be written without the token, so a literal ban would make ADD-002 § 4 self-defeating. Conditions in one list are not read to annihilate one another. This is a reading of the authorization source — fidelity work — and it amends nothing | **PRESENT** |
| 6 | **MIRROR_REVIEW must NOT become PASS by transcription alone** | the proposed value opens `REV-ORCHSURF-MIRROR-002 — revision 4 WAS reviewed, over two rounds`, states `NOT PASS` explicitly, and names REQUEST CHANGES at both rounds. Re-verified at source: **neither round frontmatter contains `PASS` as a verdict**. No GATE input is manufactured | **PRESENT** |

### 3.4 · THE FOUR UNRESOLVED ITEMS

| Item | Requirement | Evidence | Result |
|---|---|---|---|
| **UNRESOLVED-A** | not resolved — may `MIRROR_REVIEW` carry a value outside D.2's enumeration | the text is written as ADD-002 § 4 condition 6 directs and the conflict is routed, not decided. D.2 is quoted, never amended: `annex_d_commit_batch.md` line 38 is the only occurrence of `MIRROR_REVIEW` in the annex, and the annex blob is `23895689` identically at `main`, `orchestrator`, `orchestrator-surface` and CONTENT_TIP — one object, four surfaces, re-measured by me. **NOT RESOLVED** — but routed on an incomplete population: `F-1` | **NOT RESOLVED** ✓ |
| **UNRESOLVED-B** | not resolved — who transcribes | § 8 states the question and declines it: *"settled by no source I may use"*. No actor is named, assigned or empowered anywhere in the specification | **NOT RESOLVED** ✓ |
| **UNRESOLVED-C** | not resolved — at which surface the transcription lands | both surfaces are measured and neither is chosen; the consequence of each is stated. The binding is shown to be unmoved either way, which is a measurement, not a choice | **NOT RESOLVED** ✓ |
| **UNRESOLVED-D** | not resolved — whether "C.3 rounds are spent" belongs in the candidate | recorded in § 6 rather than written into a locus, and flagged as contestable. Writing it into a locus is the only alternative and condition 1 forbids it, so the narrower course is compliance with condition 1 rather than a resolution of D | **NOT RESOLVED** ✓ |

**No attempt to resolve any of the four was found.** That was checked positively, by reading § 8 in
full and by searching the three proposed texts for any clause that would settle one of them.

### 3.5 · VOCABULARY AND SCOPE

| Requirement | Evidence | Result |
|---|---|---|
| Does not change the meaning of existing governance terms | `D.2`, `C.3`, `H.1`, `P5` are quoted and never amended. The specification discloses a vocabulary mismatch rather than redefining a term | **PRESENT** |
| Introduces no new authority | no actor is empowered; no route is created; no gate is declared satisfied. Mirror's own perimeter is not enlarged by the text | **PRESENT** |
| Creates no implicit approval | verified by exhaustive sweep. The strongest candidate phrase — "findings … all disposed, no DISAGREEMENT_UNRESOLVED" — is the closure's own required language under condition 4 and travels alongside `REQUEST CHANGES` at both rounds and an explicit not-`PASS` | **PRESENT** |
| Does not change D.2's interpretation | D.2 is not amended and no reading of it is adopted; the question is routed as UNRESOLVED-A. **Measured, not assumed:** three sibling candidates already carry non-enumerated `MIRROR_REVIEW` values in canonical state, so the proposed value does not depart from the standing register — see `F-1` | **PRESENT** |

---

## 4 · FINDINGS

### F-1 · UNRESOLVED-A is routed over a population that excludes the answer's most direct evidence

```
LOCATION          REV-ORCHSURF-ADD-002-PATCH-SPECIFICATION § 2 ("The D.2 surface was checked too,
                  and it is not ambiguous") and § 8 UNRESOLVED-A
CLASSIFICATION    MECHANICAL_MISMATCH
```

The specification states that nothing in the annex declares the enumeration exhaustive or open, and
that *"NOTHING in ADD-002, in the closure, or in either round resolves whether that is permitted"*.
Both sentences are true **over the population searched** — and that population is the annex plus
three review records. It excludes `governance/candidates/` at canonical `main` @ `04693e68`, which
is ORCHSURF's own `BASE_HEAD`, where three sibling candidates already carry `MIRROR_REVIEW` values
outside `n/a | PASS | FAIL + REVIEW_ID`, in the same descriptive register the specification proposes:

```
CAND-20260819-XPORT.md:50            "REV-XPORT-MIRROR-001 — REQUEST CHANGES on M-1, CONFIRMED on
                                      every other axis … Revision 2 has NOT been reviewed"
CAND-20260818-SCIENTIST-AB-SPEC.md:91 "REV-SCIAB-MIRROR-005 → REQUEST CHANGES, on revision 5 …
                                      No PASS, no PRESERVED and no CONFIRMED … transfers"
CAND-20260818-SUNSET-DEC3.md:33      "REQUEST CHANGES on revision 1 (REV-SUNSET-DEC3-MIRROR-001)
                                      — re-review of revision 2 requested"
```

🔴 **This does NOT resolve UNRESOLVED-A and is not offered as resolving it.** Presence in a
`CONTROL_PLANE_ROOT` on `main` is not a governed permission, and none of the three establishes that
D.2's enumeration is open. What it changes is the standing of the routed question: the reviewer who
receives UNRESOLVED-A receives it framed as *no source addresses this*, when the accurate frame is
*no governance source addresses it, while the canonical control plane already contains three
instances of the practice*. A negative stated over an unnamed population is the defect this
laboratory's own records name most often, and this one is stated by the record that raised it.

### F-2 · D-5 departs from ADD-002's word on a ground the repository falsifies

```
LOCATION          § 8 declared decision D-5, and the consequent wording in § 3, § 4 and § 5
CLASSIFICATION    MECHANICAL_MISMATCH
```

`D-5` declines ADD-002's own word — `HUMAN_APPROVAL` *"remains NONE"* — on the stated ground that
*"Writing 'NONE' into a corrected locus would describe the field with a value it does not carry."*
Measured at blob `92c1b7d8`, the candidate carries `HUMAN_APPROVAL` in **four** registers:

```
line   18   frontmatter    human_approval: NOT REQUESTED — no APPROVAL_ID is prefilled here
line  162   manifest       HUMAN_APPROVAL   n/a — not requested, not prefilled, and no APPROVAL_ID
line  952   § 16 bullet    **It grants no approval and implies none.** `HUMAN_APPROVAL: NONE`
line 1113   § 17.3 bullet  **It grants no approval and implies none.** `HUMAN_APPROVAL: NONE`
```

Line 1113 sits **inside § 17.3, twenty-seven lines below L-3 itself**, and two of the sibling
candidates on canonical `main` write `HUMAN_APPROVAL: NONE — not requested, not granted, not
implied` as their field value. So "NONE" is not a value the document does not carry: it is the
document's own word in the very section being corrected, and the canonical register elsewhere.
The proposed wording adds a fifth register.

🔴 **Condition 3 is nonetheless discharged**, and this finding does not say otherwise. The field is
untouched, and *"HUMAN_APPROVAL is unchanged … no APPROVAL_ID exists"* asserts no approval and
prefills nothing. The defect is in the justification and in register consistency, not in compliance
— and it is worth recording because the correction's entire purpose is that a document should not
say two things about the same fact.

### F-3 · L-2 supplies two per-value grounds ADD-002 does not, and one rests on an undeclared mismatch

```
LOCATION          § 4, proposed L-2 — "`n/a` would deny a review that happened, `FAIL` would assert
                  a verdict no round returned"
CLASSIFICATION    INTERPRETATION_DEPENDENCY
```

ADD-002 § 4 states the conclusion — *"the true state is none of them"* — and supplies the ground
only for `PASS` (*"no `PASS` was ever issued by any reviewer on revision 4"*). The per-value grounds
for `n/a` and `FAIL` are the specification's own elaboration. The conclusion is transcribed
faithfully; the reasoning under it is added.

🔴 **The `FAIL` ground carries an undeclared vocabulary mismatch of exactly the shape of
UNRESOLVED-A.** It presupposes that `REQUEST CHANGES` is not `FAIL` — and `REQUEST CHANGES` appears
**nowhere** in Annex C's declared verdict enumeration. `annex_c_review_protocol.md` § C.2 line 40
reads `VERDICT: CONFIRMED | WEAKENED | REFINED (+REFINED_FORMULATION) | REFUTED`, and a search of
`governance/` at `main` returns `REQUEST CHANGES` only inside candidate files, never in the body or
an annex. The specification checked the D.2 surface, which governs the *field*, and never checked
the C.2 surface, which governs the *verdict* it writes into three loci.

**This does not make the transcription unfaithful** — both rounds did return `REQUEST CHANGES`, and
naming what the rounds returned is the faithful act; a transcription that substituted a
C.2-enumerated verdict would be inventing one. By the specification's own D-3 and UNRESOLVED-A
discipline the mismatch would be declared rather than left inside an asserted clause.

---

## 5 · What was checked and found sound, recorded so the negatives are not silent

Three things I expected to be defects and measured instead:

**The "Until ADD-002 this clause read …" construction is NOT a misdating.** It appears in all three
proposed texts and attributes the change point to the authorization rather than to the future
transcription commit. I checked the model ADD-002 § 4 names — § 17.3's `M-4` remedy bullet at lines
1088–1096 — and it uses the identical idiom: *"Until `REV-ORCHSURF-MIRROR-002-R2` M-4 this clause
read …"*, naming the record that raised the finding, not the commit that applied the fix. ADD-002
directs that the loci *"should be corrected the same way"*. The construction is the authorized
model's own, and following it is fidelity, not error.

**The expansion of L-2 from four lines to twenty-two is not a restructure.** Condition 1 forbids
adjacent tidying and restructure; the replacement consumes the field's own extent and no neighbour.
Condition 6 requires the field to name the review, its rounds, its verdict and its closure, and
condition 4's model requires the before/after/why triple — the length is what those conditions
compel. Geometry re-measured and preserved.

**The first-person departure from the model is grounded.** `D-1` writes documentary third person
where the model uses Plan's *"I corrected §1 …"*. Given that UNRESOLVED-B leaves the transcriber
unknown, a first-person sentence would attribute an act to an unnamed actor. The departure is in
person, not in function, and all three parts of the model survive.

---

## 6 · NOT_ESTABLISHED

```
ORCHSURF APPROVAL         NOT ESTABLISHED. This record is not a review round, not a verdict on the
                          candidate, and not a recommendation that it merge. REV-ORCHSURF-MIRROR-002
                          remains closed at REQUEST CHANGES and is not reopened by this record

TRANSCRIPTION EXECUTION   NOT ESTABLISHED. No candidate file is edited by this record and none is
                          authorized to be. The candidate blob is 92c1b7d8, unmoved. Whether the
                          transcription may be executed, by whom, and at which surface are
                          UNRESOLVED-B and UNRESOLVED-C, and both remain open

HUMAN_APPROVAL            NOT ESTABLISHED. NONE exists, none is sought, none is inferred, and it is
                          the operator's alone under H.1. A completed fidelity validation is not one

CANONICALIZATION          NOT ESTABLISHED. Canonicalization of ORCHSURF r4 would still require
                          HUMAN_APPROVAL, an ACTIVE ORCHESTRATOR_LEASE and GATE 0–5. None of the
                          three is present, and this record supplies none of them

UNRESOLVED-A/B/C/D        NOT RESOLVED by this record. F-1 adds evidence bearing on A and
                          explicitly declines to settle it

D.2 INTERPRETATION        NOT SETTLED. Whether MIRROR_REVIEW may carry a non-enumerated value is
                          routed, not decided, here as in the specification

C.2 VERDICT VOCABULARY    NOT SETTLED. Whether `REQUEST CHANGES` is a legal Annex C verdict is
                          raised at F-3 as an undeclared mismatch and is not adjudicated here.
                          It is a pre-existing condition of the two rounds, not of the patch

THE OWED ITEMS            untouched. The closure's owed list, the regression suite still
                          NOT RE-MEASURED at revision 4, and the ADD-001 CONTENT_TIP hazard are
                          neither discharged nor reduced by this record
```

---

## 7 · Standing at the instant this record was written

```
branch mirror         HEAD dfdfee5 → this commit. Working tree clean before and after
files changed         reviews/mirror/REV-ORCHSURF-ADD-002-FIDELITY-VALIDATION.md — this file only
candidate             CAND-20260819-ORCHSURF r4, blob 92c1b7d8 — NOT opened for writing
patch specification   blob ab3a946c — NOT edited
ADD-002               blob e54fe24b — NOT edited
closure and rounds    NOT edited, NOT reopened. No C.3 round opened by this record
main                  04693e68 — not written to, not read into any decision except as BASE_HEAD
lease                 none acquired, none claimed. This is not a CANONICAL_BATCH_COMMIT
this record           reviews/mirror/ — control plane. It describes a validation; it constitutes
                      no candidate, authorizes no act, and clears no gate
```
