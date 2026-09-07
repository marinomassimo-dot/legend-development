---
artifact: ADVERSARIAL REVIEW — Operating Convention v1 Phase 2 (document + first tool)
record_id: REV-OPCON-PHASE2-MIRROR-001
objects_under_review:
  - framework/protocols/legend_operating_convention_v1.md   blob ed2126a3ac26538bb21eddca3d79cf882b076e58
  - framework/scripts/artifact_index.py                     blob 68bcccd2dcca4669600d1c5d26d7f286105d214d
object_commit: c964324 @ plan-orchsurf-r4-transcription
reviewer_seat: mirror
authoring_session: mirror-87 [103de0] · transcript birth 2026-08-23T15:11:17Z
authored_on: 2026-08-23 (UTC)
governance_version: 3.1.1 (read at `main`, not exercised)
mode: ADVERSARIAL_REVIEW

STATUS: REVIEW_DELIVERED
ACTIVATION: NOT_REQUESTED
AUTHORITY_CLAIMED: none

binding_note: >
  Binds both blobs, per H-1 and H-1b as the object now states them.

conflict_of_interest: >
  🔴 DECLARED, AND S-5 IS ABOUT IT. This seat's own committed reviews have entered the corpus this
  review measures. Sections deriving from this seat's prior findings — B.2.2.x, S.7, the four
  layers — remain mirror-75's to check independently.

verdict_note: >
  Per-axis verdicts use Annex C.2's enum. No document-level disposition is emitted.
---

# ADVERSARIAL REVIEW — PHASE 2

> **Everything raised against `3650c6bf` landed, verified line by line at this blob:** the eight
> own-voice `D.1` citations are `D.2`; the appendix is renumbered `APX-0`…`APX-7` out of the frozen
> `D.n` namespace; **H-1b** carries the missing half — *a correction reported as accepted names the
> blob it landed in*; the class-table row cites by file and line; the manifest population is now
> `9 of 9`, including the authoring branch. The tool exists, has 21 tests, and prints the N-1
> domain lever as `SPANS BOTH DOMAINS` rather than as prose.
>
> **Five findings. The first cost this reviewer a near-miss and is a third emission form.**

---

## S-1 · 🔴 A THIRD EMISSION FORM — LOWERCASE, IN FRONTMATTER, IN A CAND-CLASS ARTIFACT

**AXIS: completeness of a measured claim · VERDICT: REFINED**

B.2.2.3 concludes a three-rung correction ladder with *"two syntactic forms"* — `MIRROR_REVIEW:`
colon-delimited and `MIRROR_REVIEW␣␣␣` column-aligned. There is a third:

```
governance/candidates/APPROVAL-GOV311-DEVIATIONS.md : 7      (5 refs)
  mirror_review: PASS_WITH_NOTES — REV-GOV311-MIRROR-003 (84407c1). ESC-2 was raised in
```

**Lowercase, colon, and in FRONTMATTER** — the only frontmatter declaration this reviewer has found
anywhere, in either population. Every pattern published so far, mine and the coordinator's, has been
case-sensitive on `MIRROR_REVIEW`; all of them miss it.

🔴 **This nearly became a false refutation.** The coordinator reported a tenth carrier at this file.
My first sweep — `^ *MIRROR_REVIEW([[:space:]]{2,}|:)`, syntax-agnostic but **case-sensitive** —
returned nothing, and I was one message from replying *"your tenth does not reproduce."* The
unanchored re-check fired only because I had been burned twice already today. **Third over-anchoring
from this seat in one afternoon: colon, then keyword filter, now case.** The mechanism is identical
each time and it is the rule this seat supplied: *the instrument defined the population.*

**Consequence for `APX-2`.** The proposed validator parses `MIRROR_REVIEW`. Case-sensitively it
misses the one artifact that puts the field where a frontmatter parser would look. **Match the field
name case-insensitively, and record that a `.md` frontmatter key and a body declaration are the same
field in different clothes.**

---

## S-2 · THE DOCUMENT SAYS `9 OF 9`; THE TOOL DERIVES `10`. TWO POPULATIONS, ONE LABEL

**AXIS: S.7.5 applied to the load-bearing figure · VERDICT: WEAKENED**

```
document, line 1039   "9 of 9 CAND-* manifests carry MIRROR_REVIEW; 0 conform"   ← filename-scoped
tool, class-derived   10 carriers, 0 conforming                                   ← class-by-path
delta                 governance/candidates/APPROVAL-GOV311-DEVIATIONS.md
                      an APPROVAL-named file in the CAND directory, which derives to CAND
```

Both are correct under their own definition, and **the row does not say which it uses.** S.7.5 —
*state the scope with the number* — is the document's own rule, applied everywhere except the figure
the whole section turns on.

It is not a tidy-up. **The gap between the two counts is exactly the class-vs-container question the
taxonomy exists to answer**: is an artifact a CAND because its name says `CAND-`, or because it sits
in the CAND directory? B.1.3 measured that same file as an `APPROVAL-*` misplaced inside
`governance/candidates/`. So one artifact is simultaneously *evidence of the misplacement defect* and
*a member of the population by derivation*, and the two figures differ by precisely it.

**MINIMUM FIX:** the row reads `9 of 9 by filename, 10 of 10 by derived class — the difference is
APPROVAL-GOV311-DEVIATIONS.md, which B.1.3 also lists as misplaced`. Conformance is 0 either way; the
scope is what is missing.

---

## S-3 · THE TOOL'S HEADER BREAKS S.7.5, AND THE THIRD POPULATION HAS A NAME

**AXIS: mechanism · VERDICT: CONFIRMED** (raised by the coordinator; named here from source)

```
line 399   ENUMERATED   {len(population.paths)} paths, before any pattern ran        → 611
line 411   CLASSIFIED   {len(classified)} of {len(records)} enumerated paths         → 61 of 434
```

Two different collections, both labelled *enumerated*. The coordinator reported 434 as *"a third set
the output does not name."* It is nameable, at line 481:

```python
records = [ … for path in population.paths if path.endswith((".md", ".jsonl", ".json")) ]
```

**434 = paths with a structured-document extension.** Not the 611 enumerated, not the markdown
subset. **MINIMUM FIX, one clause:** `CLASSIFIED 61 of 434 .md/.jsonl/.json records, of 611 paths
enumerated`.

---

## S-4 · `git()` CONVERTS EVERY FAILURE INTO AN EMPTY MEASUREMENT — S.7.4'S MIRROR IMAGE

**AXIS: silent failure · VERDICT: REFINED**

```python
def git(*args, cwd=None) -> str:
    proc = subprocess.run(("git", *args), cwd=str(cwd or ROOT), check=False)
    if proc.returncode != 0:
        return ""
    return proc.stdout
```

**It satisfies S.7.4's letter** — the exit status *is* checked, unlike the `rev-parse` stdout trap
S.7.4 was written for — **and it reproduces the harm in the opposite direction.** The status is
checked and then discarded: a failed `git ls-tree` is indistinguishable from a tree with no files.
`enumerate_refs()` then yields an empty population and the report prints

```
ENUMERATED   0 paths, before any pattern ran
```

which reads as a measurement, not as an error. There is no guard: the three `raise` sites are
`ConventionParseError` on the class table, none on an empty population.

**This is the mechanism behind the coordinator's own 2-of-21 test failure on a `git archive`
extraction** — and it lives in the tool, not only in the tests. S.7.4 names the false positive;
**the false negative — a failed measurement printed as a zero — has no rule.**

**MINIMUM FIX:** `git()` raises, or returns a sentinel the caller must handle; and the report refuses
to print a population of zero without saying whether git answered. **And S.7.4 gains its mirror
clause**, the way H-1 gained H-1b.

---

## S-5 · THE REVIEWER'S ARTIFACTS HAVE ENTERED THE POPULATION UNDER MEASUREMENT

**AXIS: measurement integrity · VERDICT: CONFIRMED** · ⚠️ this finding is about this seat

Re-measuring the review corpus with a whitespace-tolerant pattern returns **16 in 15 files**, against
the published **14 in 14**. The delta is not a fourth form:

```
REV-OPCONV1-MIRROR-002.md:111    MIRROR_REVIEW   REV-ORCHSURF-MIRROR-002 — revision 4 WAS reviewed…
REV-OPCONV1-MIRROR-002.md:113    MIRROR_REVIEW   REV-ORCHSURF-MIRROR-001 returned REQUEST CHANGES…
```

Both are **this reviewer's own quotations** of the ORCHSURF manifest, indented inside a fenced block
in R-2. **The published 14 is right; my 16 counted quotation as declaration** — a pattern that cannot
tell a declaration from a citation of one, sweeping up my own citation of the defect.

Two rules follow, and neither exists yet:

1. **`APX-2` must exclude quotation contexts** — indented-inside-a-fence is the cheap discriminator,
   and it is exactly what separates 14 from 16.
2. **A corpus sweep over `reviews/` now includes the reviews performing the sweep.** This seat
   committed three artifacts into `reviews/mirror/` today; the population grew from 39 by exactly
   that. A measurement over a corpus the measurer writes into must say so, or the denominator drifts
   under the reviewer's own hand.

---

## 6 · SUMMARY

| # | finding | axis verdict | locus | minimum fix |
|---|---|---|---|---|
| S-1 | 🔴 third emission form: lowercase `mirror_review:`, in frontmatter, in a CAND-class artifact | REFINED | B.2.2.3, APX-2 | match case-insensitively; record frontmatter-key ≡ body declaration |
| S-2 | `9 of 9` by filename vs `10` by derived class, unlabelled — on the load-bearing row | WEAKENED | doc 1039 | state both scopes; the delta is B.1.3's own misplaced file |
| S-3 | `CLASSIFIED n of m enumerated` — m is the `.md/.jsonl/.json` subset, from line 481 | CONFIRMED | script 399/411 | one clause |
| S-4 | `git()` prints a failed measurement as zero — S.7.4's mirror image | REFINED | script `git()` | raise or sentinel; S.7.4 gains a mirror clause |
| S-5 | ⚠️ the reviewer's own quotations enter the corpus; 16 vs 14 | CONFIRMED | APX-2, method | exclude quotation contexts; declare the self-inclusion |

**Landed and verified at `ed2126a3`:** the eight `D.1` loci → `D.2` · `APX-n` renumbering, with the
collision recorded as *"the § A → § S collision recurring one layer down"* · H-1b · file-and-line
citation adopted document-wide · class-table row · `9 of 9` including the authoring branch.

**One inconsistency not worth a finding, recorded for the editor:** the document adopts *"cite a
frozen clause by FILE AND LINE, never by section number"* and then cites `D.2` by section at lines
761, 822, 843, 1038 and 1148. The rule is right; it is applied unevenly in the same blob that
declares it.

**What this review did not do:** did not decide anything · did not activate anything · did not run
the tool against the repository — `ROOT` is derived from `__file__` and the script must sit in
`framework/scripts/` to resolve, so the tool was read at source, not executed · did not re-litigate
N-1…N-4 or R-1…R-3 · did not emit a document-level disposition.

END OF REVIEW.
