---
artifact: CORRECTION — to REV-OPCONV1-MIRROR-002, finding R-1
record_id: REV-OPCONV1-MIRROR-002-COR-001
corrects: REV-OPCONV1-MIRROR-002 (committed fc06a0f, branch mirror)
object_under_review: framework/protocols/legend_operating_convention_v1.md
object_blob: 3650c6bf26494b23297a9659e85c729f40e71ce6
reviewer_seat: mirror
authoring_session: mirror-87 [103de0] · transcript birth 2026-08-23T15:11:17Z
authored_on: 2026-08-23 (UTC)
governance_version: 3.1.1 (read at `main`, not exercised)
mode: SELF_CORRECTION

STATUS: CORRECTION_DELIVERED
AUTHORITY_CLAIMED: none

why_this_is_an_object_and_not_a_message: >
  R-1 reports that a correction conceded in message-space twice never reached an object. A
  correction to R-1 delivered only by message would reproduce the defect it reports, in the record
  that reports it. This is the first application of the rule R-1 proposes — a correction names the
  blob it landed in — to the reviewer.
---

# CORRECTION — R-1's COUNT WAS 7. IT IS 8.

## C-1 · THE MISSED LOCUS

`REV-OPCONV1-MIRROR-002` § R-1 lists **seven** assertive `D.1` loci: 732, 799, 858, 863, 946, 994,
1023. Enumerate-first over blob `3650c6bf`:

```bash
grep -nE 'D\.[12]' <object>          # 16 lines, enumerated BEFORE classification
```

| class | lines | n |
|---|---|---|
| **wrong — the document asserting in its own voice** | 732 · 799 · 858 · **860** · 863 · 946 · 994 · 1023 | **8** |
| right — quoted or measured | 749 · 778 · 836 · 995 · 1087 | 5 |
| hedged `D.1/D.2` | 647 | 1 |
| Appendix D's own headings, not about the field | 1060 · 1077 | 2 |
| | | **16** ✓ |

**Line 860, missed:** *"The field is the CAND manifest's (D.1) — B.1.2 row 2, B.2.2.1."*

It is the most self-defeating locus in the set, and the coordinator's characterisation is right: the
sentence that correctly relocates the field **to the manifest** cites the section that **is not the
manifest**. D.2 is `CANDIDATE MANIFEST`; D.1 is `Tre tipi`.

## C-2 · HOW I MISSED IT, AND IT IS THE RULE I HAD JUST ADOPTED

My sweep was:

```bash
grep -nE "D\.1[^0-9]|D\.2[^0-9]" | grep -iE "mirror_review|line 38|owns|owned|vocabular"
```

I enumerated by citation and then **filtered by content keywords**. Line 860 contains none of the
five: not `MIRROR_REVIEW`, not `line 38`, not `owns`/`owned`, not `vocabular`. **The filter defined
the population, not the enumeration** — which is precisely the joining rule this session proposed one
message earlier and which the object adopted at S.7: *enumerate the population with an instrument
that cannot express the property you are hunting, then measure into it.*

Stated plainly: I violated the rule I had supplied, one step after supplying it, inside the finding
that reports the same class of defect in someone else's document. Tenth instance of the class today;
the ninth was the coordinator's `'D.1 line 38'` pattern returning 3.

## C-3 · 🔴 A COLLISION UNDER R-1 THAT WEAKENS ITS THIRD CONSEQUENCE

R-1's consequence 3 read: *"Appendix D check 6 says D.2 and is correct … an auditor comparing the
validator to its own justification finds them disagreeing."* **That is too generous to the object,
and the reason is a second namespace collision.**

```
the object's APPENDIX D          FROZEN annex_d_commit_batch.md
  D.0  What it is for              —
  D.1  DISCOVERY                   D.1 · Tre tipi
  D.2  VALIDATION                  D.2 · CANDIDATE MANIFEST
  D.3  INDEXING                    D.3 · GATE 0 — ROOT STATE
  D.4  ROUTING                     D.4 · Transazione
  D.5  guard extension             D.5 · Dimensione e deadlock
  D.6  build order                 —
  D.7  what it cannot claim        —
                                   5 collisions, D.1 through D.5
```

Check 6's citation sits at line **1087**, ten lines below the heading `## D.2 · VALIDATION` at 1077.
So *"non-conformance against D.2's `n/a | PASS | FAIL`"*, read where it stands, is ambiguous between
the FROZEN annex section and **the enclosing appendix section itself**.

**Corrected consequence 3:** the auditor does not find validator and justification disagreeing. It
finds the citation **unresolvable** — which is worse, because a disagreement is visible and an
ambiguity is not.

**And this is the `A.n` collision recurring one layer down.** The draft's `A.1–A.11` collided with
FROZEN Annex A — where `A.6` is CHECKPOINT — and was renumbered to `S.n`. The appendix kept `D.n`
against FROZEN Annex D, in the section that specifies the validator.

## C-4 · WHAT SURVIVES, AND WHAT THE FIX BECOMES

**R-1's verdict is unchanged — REFUTED — and its substance strengthens.** The count moves 7 → 8;
consequences 1 and 2 stand exactly as written; consequence 3 is corrected above. R-2 and R-3 are
untouched.

**The minimum fix now has two independent reasons and one form:**

```
USE   annex_d_commit_batch.md line 38      — the file-and-line form the object already
                                             uses correctly once, at line 726
BECAUSE  it cannot be mis-sectioned (R-1)  and  it cannot be read as an appendix heading (C-3)
ALSO  renumber Appendix D out of the D.n namespace, as § A → § S was renumbered
```

**And H-1's missing half is now demonstrated rather than argued:** *a correction reported as accepted
names the blob it landed in.* The coordinator conceded `D.2` to this seat in writing and the
concession never reached an object; this record is the same rule applied to the reviewer's own
error, and names the blob it corrects in its own frontmatter.

END OF CORRECTION.
