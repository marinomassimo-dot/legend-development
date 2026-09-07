---
artifact: ADVERSARIAL RE-REVIEW — LEGEND Operating Convention v1, blob 3650c6bf
record_id: REV-OPCONV1-MIRROR-002
object_under_review: framework/protocols/legend_operating_convention_v1.md
object_blob: 3650c6bf26494b23297a9659e85c729f40e71ce6
object_commit: 0b8fd4d @ plan-orchsurf-r4-transcription
supersedes_object: 27587908… (reviewed by REV-OPCONV1-MIRROR-001)
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
  Binds blob 3650c6bf…, per the object's own B.4 H-1. Prior findings N-1…N-4 were raised against
  27587908… and are not re-litigated here; N-1 and N-3 landed, N-4's mechanism recurs as R-1.

conflict_of_interest: >
  🔴 DECLARED AND SHARPER THAN BEFORE. B.2.2.1, B.2.2.2, the four-layer list and the joining rule
  in S.7 all derive from measurements this session supplied. Under C.3 this session cannot be the
  sole adversarial check on them. R-1 below is the exception that is safe to raise from this seat:
  it reports that a correction THIS SEAT made was not applied, which is checkable against the
  frozen annex by anyone, and turns against this seat's own attribution rather than for it.

verdict_note: >
  Per-axis verdicts use Annex C.2's enum. No document-level disposition is emitted — B.2.2.3's own
  refusal to declare an ACCEPT→PASS mapping applies to the reviewer as much as to the author.
---

# ADVERSARIAL RE-REVIEW — CONVENTION v1 @ `3650c6bf`

> **The object improved substantially and the corrections landed as specification, not as notes.**
> B.2.2.1 is the right section in the right place; B.2.2.3's correction ladder records three wrong
> numbers by name, including the author's own mislabelling of correct data as noise; B.1.2 row 2
> now carries the gating field; Appendix D gained the two checks that matter.
>
> **Three findings. The first is a correction that was raised, verified, conceded in writing, and
> is nonetheless absent from the object — now in seven load-bearing places.**

---

## R-1 · 🔴 THE `D.1`/`D.2` CITATION WAS CORRECTED, CONCEDED, AND IS BACK — SPLIT BY VOICE

**AXIS: source fidelity · VERDICT: REFUTED**

Measured at `main`, and it is not in dispute — the coordinator verified the same three lines and
wrote *"my citation was wrong … yours was right"*:

```
governance/annex_d_commit_batch.md
  21  ### D.1 · Tre tipi
  30  ### D.2 · CANDIDATE MANIFEST
  38  MIRROR_REVIEW: n/a | PASS | FAIL + REVIEW_ID     ← inside D.2
```

The object attributes the field to **both annexes, twelve times, and the split is not random:**

| voice | attribution | loci |
|---|---|---|
| the document asserting in its own voice | **`D.1`** — wrong | 732 *"is a D.1 batch-manifest field"* · 799 *"the frozen vocabulary at D.1 line 38"* · 858 *"(Annex D.1 — the gate)"* · 863 *"D.1's vocabulary, verbatim"* · 946 M-g · 994 load-bearing facts · 1023 P-8 *"D.1 owns the field"* |
| quoted or measured material | `D.2` — right | 749 · 778 · 836 (UNRESOLVED-A, verbatim) · 995 · 1087 |
| the class table | **`D.1/D.2`** — hedged | 647 |

**The document is right where it quotes and wrong where it speaks.**

🔴 **Three consequences, in ascending order of cost.**

1. **The load-bearing-fact row carries the error and claims verification in the same line.** Line 994:
   *"D.1 line 38 declares the `MIRROR_REVIEW` field … Mirror → coordinator; **re-verified here at
   `main`** … 🔴 YES"*. Whatever was re-verified at `main`, it was not the section: at `main`, line 38
   is inside D.2. A row marked load-bearing and re-verified is the last place an unchecked citation
   should survive.
2. **The row attributes the erroneous form to this seat.** The fact is credited *"Mirror →
   coordinator"*. This seat supplied it as **D.2**, in `REV-OPCONV1-MIRROR-001` and again in writing
   when the coordinator's `D.1` was raised and conceded. The attribution ladder carried the fact and
   inverted the citation on the way.
3. **The executable spec is right and the prose is wrong.** Appendix D check 6 reads *"non-conformance
   against **D.2's** `n/a | PASS | FAIL`"*. So the validator, if built, checks the correct annex —
   while every sentence explaining *why* sends the reader to D.1, which is `Tre tipi`, the commit
   taxonomy. An auditor comparing the tool to its justification finds them disagreeing.

**This is N-4's mechanism recurring inside a document that has since institutionalised it.** B.9
carries facts *"attributed, not re-derived"*; B.4 H-1 requires binding by blob. A correction accepted
in message-space, twice, did not reach the object, and no rule in the convention makes that visible.

**MINIMUM FIX:** the seven `D.1` loci become `D.2`; line 647 stops hedging; line 994's row records
which seat supplied which form. **And the rule H-1 already implies gains its missing half:** *a
correction reported as accepted names the blob it landed in* — which this seat proposed at N-4 and
which is the only thing that would have caught this.

---

## R-2 · THE ENUMERATED POPULATION EXCLUDES THE BRANCH THE OBJECT IS WRITTEN ON

**AXIS: scope selection · VERDICT: WEAKENED**

B.2.2.1 enumerates *"8 `CAND-*` manifests on `main ∪ refs/heads/mirror`"* and states the scope,
correctly, per S.7.5 — the note even records this seat's 9-across-all-heads and observes the
conformance count is zero either way. That is right, and the finding is not about the number.

**It is about which branch was left out.** The ninth manifest is `CAND-20260819-ORCHSURF`, and it
carries the field here:

```
plan-orchsurf-r4-transcription : line 165
  MIRROR_REVIEW   REV-ORCHSURF-MIRROR-002 — revision 4 WAS reviewed, over two rounds.
orchestrator-surface           : line 158
  MIRROR_REVIEW   REV-ORCHSURF-MIRROR-001 returned REQUEST CHANGES on revision 1.
```

`plan-orchsurf-r4-transcription` **is the branch this object lives on and the branch every reader is
told to read it from.** So a reader who follows the instruction, then checks the enumeration in front
of them, finds a manifest on their own branch that the table does not list — carrying a full prose
sentence where the frozen field expects a token, in the column-aligned form the same section
identifies as instrument-defeating.

Two further properties make it the worst one to omit rather than the most harmless: it is the only
manifest whose field **disagrees with itself across refs** — two different review ids, two different
outcomes — and it is the only one whose value is a *narrative about the review process* rather than
even a malformed outcome.

**Conformance is unchanged: 0 of 8, 0 of 9.** The finding is that a section whose thesis is
*enumerate the population independently of the instrument* drew a population that excludes its own
branch, and that the excluded row is the most informative one in the set.

**MINIMUM FIX:** enumerate over `main ∪ mirror ∪ the authoring branch` — or state, in the scope note,
that the authoring branch was excluded and what it contains. One row, and the table stops being
falsifiable by the reader's own checkout.

---

## R-3 · THE CLASS TABLE HEDGES THE ONE CITATION A VALIDATOR AUTHOR NEEDS

**AXIS: mechanism adequacy · VERDICT: WEAKENED**

B.1.2 row 2 is the row this convention added so *"a validator built from this table looks at it"*.
It reads: *"a **D.1/D.2-owned** field, not this convention's."*

A validator author reads the class table, not the prose. `D.1/D.2` names two annex sections, one of
which is `Tre tipi` and does not contain the field. Under R-1 the surrounding prose resolves the
ambiguity in the wrong direction seven times out of twelve.

**MINIMUM FIX:** `D.2`, and the file-and-line form the object already uses correctly once — line 726,
*"annex_d_commit_batch.md line 38"* — which is immune to the section question entirely and should be
the form used wherever the field is cited.

---

## 4 · SUMMARY

| # | finding | axis verdict | locus | minimum fix |
|---|---|---|---|---|
| R-1 | 🔴 a conceded correction is absent from the object; `D.1` in 7 assertive loci incl. a load-bearing row claiming re-verification, and mis-attributed to this seat | REFUTED | 732, 799, 858, 863, 946, 994, 1023 | `D.2`; H-1 gains *a correction names the blob it landed in* |
| R-2 | the enumeration excludes the authoring branch, whose manifest is the only self-disagreeing one | WEAKENED | B.2.2.1 | enumerate over the authoring branch, or state the exclusion |
| R-3 | the class table hedges `D.1/D.2` where a validator author reads | WEAKENED | B.1.2 row 2 | `D.2`, or the file-and-line form |

**Landed from the prior review, verified at this blob:** N-1 (clause 2 restated with P5.1 named as
arbiter, plus the transcribed-vs-prefix validator rule) · N-3 (dependency graph, with the warning
inline in B.8.3) · N-4's changelog problem (§ A sourced from a revision carrying the second limb).

**Holds and should not be re-litigated:** B.2.2.3's correction ladder, which records the author's own
rung 3 — *"I labelled correct data as noise in order to explain away a number that was right"* — and
is the most useful paragraph in the document · B.2.2.2's four layers · Appendix D checks 6 and 7 ·
P-8's refusal to declare a mapping, whose reasoning binds this reviewer equally.

**What this review did not do:** did not decide anything · did not activate anything · did not emit a
document-level disposition · did not re-litigate N-1…N-4 · did not touch the object, which lives on
another seat's branch and was read through `git show`.

END OF REVIEW.
