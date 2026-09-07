---
artifact: ADJUDICATION ADDENDUM (Annex C.3) — the reviewed object is unchanged and the reviewed
  manifest text is corrected, and those are two different sentences
record_id: CLOSE-REV-ORCHSURF-MIRROR-002-ADD-002
addends: CLOSE-REV-ORCHSURF-MIRROR-002 (0a1929e), following ADD-001 (9b86373). The closure is NOT
  edited and ADD-001 is NOT edited — both were correct at the instants they were taken
object: CAND-20260819-ORCHSURF revision 4 · CANDIDATE_CONTENT_HASH 844de909…acb6dc
  @ BASE_HEAD 04693e68 · CONTENT_TIP 9a70e94d — recomputed by me this session, not carried
raised_by: plan — the correction was TRANSMITTED. It is not durably recorded anywhere in this
  repository, and this record does not pretend otherwise: see § 6
adjudicated_by: orchestrator, as adjudicator. C.3 rounds are spent; no reviewer re-examined this
date: 2026-08-20T22:25Z
outcome: REVIEW REOPEN REQUIRED — NO. The correction is authorized as a CLASS, under conditions
approval: NONE. Not sought, not granted, not implied. `HUMAN_APPROVAL` remains NONE and
  `MIRROR_REVIEW` remains not-PASS. Nothing here is a readiness certificate
scope_negative: the candidate is NOT edited; no patch is applied; Mirror is NOT reopened; no new
  review round is opened; nothing is canonicalized; no `ORCHESTRATOR_LEASE` is acquired or claimed
discipline: append-only
---

# Addendum — a correction that transcribes a closed finding is not a new judgement

## 0 · Rehydration, fail-closed — every value below read from the repository, none from the prompt

```
ACTOR_ID          orchestrator — from roles/orchestrator.md, actor_id: orchestrator, and from the
                  one-writer clause of runtime/orchestrator_lease.md ("orchestrator ONLY, from the
                  orchestrator worktree"). NOT inferred from cwd, session name or prior chat
AUTHORITY         C.3 adjudication + H.1 "Aggiudicazione challenge — Orchestrator (con rationale)"
                  Position in the root confers nothing (roles/orchestrator.md; body §0.2, §8)
LEASE             ACTIVE by derivation: 0 — python3 framework/scripts/lease_state.py --check,
                  run by me. Two standing findings on historical row #3, both pre-existing.
                  No lease is required for this record: it is not a CANONICAL_BATCH_COMMIT
canonical main    04693e683a254ff0a6d0619fba47103a0fb7d122 — from git refs. Root clean, 0 entries
BINDING           hash(04693e68, 9a70e94d) = 844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
                  RECOMPUTED by me with governance/scripts/candidate_content_hash.py. MATCHES
DOMAIN            539 included · 49 excluded, printed by --show-domain
CLOSURE           CLOSE-REV-ORCHSURF-MIRROR-002 @ 0a1929e — read at source. Two rounds,
                  findings raised and disposed, no DISAGREEMENT_UNRESOLVED, approval NONE
CANDIDATE BLOB    92c1b7d8 at the `orchestrator-surface` tip 5fa1cf2 — the closing blob, unmoved
                  since 5a69a05. The branch moved past CONTENT_TIP in `learning/` only (ADD-001 §1)
```

One of the six rehydration items **did not reconstruct**, and it is recorded here rather than
assumed: **Plan's prepared correction has no durable trace.** § 6.

---

## 1 · The finding, transcribed at a stated surface — because an anchor without a surface is not an anchor

`D-1` of this review was that line anchors are valid only at the surface they were taken over. So
both surfaces are given, and neither is carried across.

```
                                        @ 9a70e94d          @ 5fa1cf2
                                        blob 2dbe570c       blob 92c1b7d8
                                        (CONTENT_TIP)       (closing blob, branch tip)
L-1  frontmatter, `supersedes:`             line 54            line 54
L-2  § 1 manifest, `MIRROR_REVIEW`          line 136           line 159
L-3  § 17.3, first bullet                   line 978           line 1086
```

**The three sentences are byte-identical across every surface this review touched** — CONTENT_TIP
`9a70e94d`, the round-2 object `6110421` (blob `7469f4e1`), the closing tip `5a69a05` and the
current branch tip `5fa1cf2`. So the surface decides *where to look*, not *what the correction must
say*. Verbatim, at `92c1b7d8`:

```
L-1   "REV-ORCHSURF-MIRROR-001 reviewed revision 1; NO REVIEW has ever been performed on
       revision 2, 3 or 4"
L-2   "MIRROR_REVIEW   REV-ORCHSURF-MIRROR-001 returned REQUEST CHANGES on revision 1.
       Revisions 2, 3 and 4 have NEVER been reviewed. None performed, none assumed …"
L-3   "It does not claim Mirror has reviewed this. No review exists for revisions 2, 3 or 4, and
       revision 1's review was conducted under the opposite direction, so it does not transfer."
```

**All three were true when written and are false now.** `REV-ORCHSURF-MIRROR-002` reviewed
revision 4 over two substantive rounds — round 1 at `REV-ORCHSURF-MIRROR-002`, round 2 at
`REV-ORCHSURF-MIRROR-002-R2`, verdict `REQUEST CHANGES`, four reviewer findings and one
adjudicator residual, all disposed at `CLOSE-REV-ORCHSURF-MIRROR-002`.

🔴 **They are not harmless.** `L-2` is a manifest field the governance defines (`D.2`
`MIRROR_REVIEW`), `L-3` sits inside the one list whose entire subject is accuracy about what is
*not* claimed, and `L-1` travels in frontmatter, which is what a reader loads first. This is the
same shape as `M-4`: a false sentence in the operative layer, which reaches the operator unless
someone corrects it. That is why this is adjudicated rather than waved through.

---

## 2 · RULING ONE — the reviewed OBJECT is unchanged; the reviewed TEXT is corrected

```
REVIEWED OBJECT IDENTITY      UNCHANGED
REVIEWED MANIFEST TEXT        CORRECTED
```

**These are two different sentences and the whole ruling is that they do not collapse into one.**
Confusing them in either direction is this session's own structural finding — an instrument
reporting faithfully about the wrong object.

**The object half is measured, not argued.** `P5.1` declares `governance/candidates/` a
`CONTROL_PLANE_ROOT`, exhaustively, as a directory prefix; the hash script parses that rule out of
`P5` at the tip being hashed rather than restating it, and prints what it dropped:

```
$ python3 governance/scripts/candidate_content_hash.py --base 04693e68… --tip 9a70e94d… --show-domain
included   539 entries
excluded   49 entries (control plane)
             …
             governance/candidates/CAND-20260819-ORCHSURF.md      ← the file being corrected
             …
```

The document that would be patched is **in the excluded set, by name, printed by the tool**. It
cannot move `CANDIDATE_CONTENT_HASH`, because it is not in the pre-image. `BASE_HEAD` is a git ref
and no edit to a candidate file reaches it. `CONTENT_TIP` is a commit id and naming a different one
would be a re-binding, which this record neither performs nor authorizes.

```
BASE_HEAD                   04693e68            NOT CHANGED — it is a ref, not a claim
CONTENT_TIP                 9a70e94d            NOT CHANGED — no re-bind here
CANDIDATE_CONTENT_HASH      844de909…acb6dc     CANNOT change — the file is outside the domain
HASHED DOMAIN CONTENT       539 entries         NOT TOUCHED
REVIEWED MANIFEST TEXT      3 loci              DOES change. Stated, not minimised
```

**The text half is conceded in full.** Two rounds of hostile review read this document, and Mirror
read `§ 17.3` in round 1 closely enough to quote it approvingly (`ADD-008 § 2`). The bytes a
reviewer read would change. **Nothing here calls that nothing.** The ruling is that a change to
those bytes does not change *what was reviewed* in the sense `D.2` binds — and `D.2` says what it
binds: *"ogni approvazione si lega a `CANDIDATE_CONTENT_HASH` + `BASE_HEAD`."* The pair is fixed.

🔴 **And the clause that follows it has nothing to bite on here, in either direction.** `D.2`
continues *"qualsiasi modifica materiale le invalida"* — it invalidates **approvals**. There are no
approvals bound to this candidate: `HUMAN_APPROVAL` is NONE and Mirror never issued a `PASS`. So
the argument above does **not** rest on that clause, and it must not be read as though the clause
had cleared the correction. It rests on `P5.1` for the domain and on `D.2`'s first sentence for
what the binding is.

---

## 3 · RULING TWO — `REVIEW REOPEN REQUIRED: NO`

**Authority basis, each read at source this session:**

| Basis | Text relied on |
|---|---|
| `C.3` | *"Apertura solo via Orchestrator … max 2 round → adjudication"* — the rounds are spent, and opening a third is a thing only I may do. I decline to do it |
| `H.1` | *"Aggiudicazione challenge — Orchestrator (con rationale)"* — hence this record, and hence its grounds are written out rather than asserted |
| `D.2` | the binding is `CANDIDATE_CONTENT_HASH + BASE_HEAD`; both are fixed and measured above |
| `P5.1` | `governance/candidates/` is a declared `CONTROL_PLANE_ROOT`; the manifest describes the candidate and does not constitute it |

**Classification: `CONTROL-PLANE HISTORICAL-METADATA CORRECTION`.**

**Rationale — three grounds, and the third is the one that decides it.**

**(a) The correction transcribes the reviewer's own closed findings.** The facts to be written —
that `REV-ORCHSURF-MIRROR-002` occurred, over two rounds, on revision 4 — were authored by Mirror
and recorded by me. Nothing new is being asserted about the world.

**(b) It introduces no new judgement, and it does not alter the reviewed technical object.** The
patch changes what the document *says about the review*, not what the document *proposes*. The 539
content entries are untouched; the argument, the findings and the remedies of revision 4 are
untouched.

**(c) A new review round would have no independent falsifier.** This is the decisive ground.
`C.3` asks for a *reviewer senza evidenza contribuita* — a reviewer that did not contribute the
evidence it now checks. **On the question "did `REV-ORCHSURF-MIRROR-002` happen", Mirror is the
evidence.** It cannot be independent of its own occurrence, and no round it ran could falsify it.
A round that cannot fail is not a check; it is a ceremony that would end in the same sentence this
record already contains, at the cost of pretending an independence that does not exist.

🔴 **What ground (c) does NOT license.** It is narrow, and it is narrow on purpose. It says a
review round cannot independently verify *that a review occurred*. It says nothing about whether
the patch *faithfully transcribes* what occurred — that question has a perfectly good independent
falsifier, namely reading the patch against the closure, and § 4 and § 5 route it accordingly.
Reading (c) any wider would convert an unfalsifiable question into a general exemption, which is
the exact move `ADD-008 (b)` refused when it declined to read *not looked at* as *cleared*.

---

## 4 · Conditions on Plan's patch — authorized as TRANSCRIPTION, and as nothing else

The patch is authorized **only** as transcription of the closed record. Six conditions, and the
last is not a restatement of the others.

```
1  LOCI          limited to L-1, L-2, L-3. No fourth locus, no adjacent tidying, no restructure
2  REVIEW ≠      the corrected text must preserve that a review having occurred is not an
   APPROVAL      approval, and must not let the first imply the second
3  HUMAN_        stays NONE. Not "pending", not "in progress", not prefilled with an APPROVAL_ID
   APPROVAL
4  CLOSURE       the closure's own language survives: examined, findings disposed, not approved
   LANGUAGE      and not certified ready
5  VOCABULARY    no word implying approval, pass, clearance or readiness anywhere in the three loci
6  MIRROR_       must NOT be set to `PASS` — see below
   REVIEW
```

🔴 **Condition 6 exists because the field's own vocabulary is a trap, and a naive transcription
falls straight into it.** `D.2` defines `MIRROR_REVIEW: n/a | PASS | FAIL + REVIEW_ID`. A writer
correcting `L-2` from *"never reviewed"* now has three legal values and **the true state is none of
them**: two rounds ran, round 2 returned `REQUEST CHANGES`, the remedies were verified by the
adjudicator with the rounds already spent, and no `PASS` was ever issued by any reviewer on
revision 4.

**The consequence is not cosmetic.** `CHANGE_CLASS` is `MAJOR` (candidate § 1, line 128 at blob
`92c1b7d8` — the surface, because an anchor without one is not an anchor), and the
Orchestrator role contract forbids running a MAJOR *"without Mirror PASS **and** `HUMAN_APPROVAL`"*.
Writing `PASS` into that field would not merely overstate the record — **it would manufacture a
GATE input for a MAJOR out of a correction whose entire warrant is that it adds no judgement.**
The correct value names the review, its rounds, its verdict and its closure, and asserts no verdict
the record does not contain.

**The model is already in the document.** `§ 17.3`'s second bullet — the `M-4` remedy — states what
is true now, states what was true before, and says why the old clause was false, keeping the
correction auditable instead of erasing the evidence that it was needed. `L-1`, `L-2` and `L-3`
should be corrected the same way. **A record edited to agree with its own present is no longer
evidence of what it said.**

---

## 5 · Mirror handling

```
MIRROR REOPENED      NO
MIRROR NOTIFIED      by this record, on branch `orchestrator`, readable by every actor via git
DISAGREEMENT ROUTE   open, and about transcription fidelity only
```

**What Mirror may raise, without any of this being reopened:** that the patch does not faithfully
transcribe the closed findings — wrong verdict named, a `PASS` implied, a locus exceeded, closure
language weakened. That is a disagreement about *fidelity*, it has a real falsifier (the closure
itself), and it travels under `Annex F` as a challenge rather than as a review round.

**What is not reopened:** `REV-ORCHSURF-MIRROR-002`, its two rounds, its four findings, the
residual `R-1`, and every disposition recorded at `CLOSE-REV-ORCHSURF-MIRROR-002`.

🔴 **On the notification, precisely.** No message was dispatched from this session, and there is no
event ledger to write one into — `P7` is `OWED NOT BARRED`, and `runtime/orchestrator_lease.md`
says plainly that nothing runs between turns. The notification is this commit, on the branch Mirror
can read. Per body § 18, *"il messaggio notifica, il commit fa fede"* — so what exists here is the
part that counts and not the part that alerts. **Whether Mirror has read it is not established by
this record and is not assumed by it.**

---

## 6 · What this adjudication does NOT establish

🔴 **Plan's patch is not in evidence, and this record authorizes a CLASS, not a TEXT.** I searched
for it before writing this, and the search is stated with its population rather than as "I looked":

```
git status over all 14 worktrees         clean, except 3 unrelated: two `lettore*` deepdive
                                         manifests and one codex reading branch. None is Plan's
git log --all --since 2026-08-20         51 commits, every one read by subject. The first pass
                                         read 40 and reported 40 — a truncated view read as a
                                         population, on the day whose whole finding that is
git stash list                           one entry, unrelated (a PMID manifest, pre-rebase)
git grep over ALL 696 reachable commits  for the three sentences
  → exactly one path, on every ref that carries them:
    governance/candidates/CAND-20260819-ORCHSURF.md
```

**No artefact anywhere in this repository carries the proposed replacement text.** Plan's latest
durable record is `SLR-plan-0014-COR-004` at `5fa1cf2`, and it is about something else.

**So the sixth rehydration item did not reconstruct.** Body § 18 makes the commit what counts; a
patch that exists only in a message has no durable trace, and I will not certify text I have not
read by treating a transmission as a record. **Verifying the patch against § 4's six conditions is
a separate act, it is owed, and it did not happen here.** Anyone reading this record as clearance
for a specific diff is reading it wrongly.

**Also not established:**

- **No approval of anything.** `HUMAN_APPROVAL` is the operator's alone under `H.1`. None exists,
  none is inferred, and a completed review is not one.
- **No readiness.** Canonicalization of ORCHSURF r4 would still require `HUMAN_APPROVAL`, an
  `ACTIVE` `ORCHESTRATOR_LEASE` and `GATE 0–5`. None of the three is present.
- **No re-binding.** `CONTENT_TIP` stays `9a70e94d`. ADD-001 § 1 already recorded that the branch
  tip carries `learning/` content past that binding which no review examined; **that hazard is
  untouched by this record and is not reduced by it.**
- **The owed list is not re-derived here.** The closure's items stand as ADD-001 left them. Items 1
  and 2 have activity after ADD-001 in `ledger/probe/` (`601787f`, `4e734b1`); this record neither
  adjudicates nor discharges them.
- **The regression suite** is still `NOT RE-MEASURED at revision 4`, by anyone, at any round.

---

## 7 · Standing at the instant this record was written

```
main                  04693e68 — UNCHANGED. Root checkout clean, 0 entries, all session
candidate             CAND-20260819-ORCHSURF r4 UNTOUCHED — blob 92c1b7d8, not opened for writing
binding               844de909…acb6dc @ (04693e68, 9a70e94d) — recomputed, unchanged
review                REV-ORCHSURF-MIRROR-002 CLOSED. Not reopened. No new round opened
lease                 ACTIVE by derivation: 0. None acquired, none claimed
approval              NONE — not sought, not granted, not inferred
this record           reviews/orchestrator/ — control plane under P5.1, outside every candidate
                      domain. It describes an adjudication; it constitutes no candidate
```
