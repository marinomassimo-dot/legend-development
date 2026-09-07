---
artifact: ADDENDUM 2 — to REV-OPCON-PHASE2-MIRROR-001, against script blob a68a8091
record_id: REV-OPCON-PHASE2-MIRROR-001-ADD-002
extends: REV-OPCON-PHASE2-MIRROR-001 (e0353d6) · REV-OPCON-PHASE2-MIRROR-001-ADD-001 (00ccb12)
object_under_review: framework/scripts/artifact_index.py   blob a68a809137466244edb330593a5d33dfd5673fff
object_commit: e4aa80c @ plan-orchsurf-r4-transcription
reviewer_seat: mirror
authoring_session: mirror-87 [103de0] · transcript birth 2026-08-23T15:11:17Z
authored_on: 2026-08-23 (UTC)
mode: ADVERSARIAL_REVIEW

STATUS: ADDENDUM_DELIVERED
AUTHORITY_CLAIMED: none

conflict_of_interest: >
  🔴 As with ADD-001, the specimen is this seat's own committed artifact. That is what makes the
  finding reproducible by anyone holding the blob.
---

# ADDENDUM 2 — A-3 LANDED ON ONE PATTERN OF TWO

**A-2 is fully closed** — `re.I` is on both patterns, verified at the byte (lines 21 and 22 of
`field_patterns`).

**A-3 is closed for the aligned form and open for the colon form**, and the residue is reproducible
at this blob.

---

## B-1 · THE COLUMN-0 DISCRIMINATOR WENT ONTO ONE PATTERN, NOT THE PAIR

```python
colon    re.compile(rf"^[ \t]*{name}[ \t]*:[ \t]*(.*)$",   re.M | re.I)   ← still admits indentation
aligned  re.compile(rf"^{name}[ \t]{{2,}}([^\s:].*)$",     re.M | re.I)   ← column 0 required
```

Running this blob's own patterns over three artifacts:

```
REV-OPCONV1-MIRROR-002.md        form=None                                        ← FIXED
REV-OPCON-PHASE2-MIRROR-001.md   form=colon   PASS_WITH_NOTES — REV-GOV311-MIRROR-003 (84407c1)…
REV-SCIAB-MIRROR-001.md          form=aligned REQUEST CHANGES                     ← genuine, preserved
```

Row 1 is repaired and row 3 survives — the coordinator is right that excluding fences wholesale
would have destroyed a real declaration, and column-0-inside-a-fence was the correct discriminator.

🔴 **Row 2 is unchanged.** The matching line, `od -c` verified, is:

```
  mirror_review: PASS_WITH_NOTES — REV-GOV311-MIRROR-003 (84407c1). ESC-2 was raised in
^^  two spaces — REV-OPCON-PHASE2-MIRROR-001.md line 52
```

It is this seat's **quotation** of `APPROVAL-GOV311-DEVIATIONS.md:7` inside finding S-1 — the report
of the third emission form, still read as a declaration of it. **The illustration A-3 was built on
survives the fix for A-3.**

The shape is A-2's, one iteration later and inside A-3's own remedy: **a fix applied to one member
of a two-member pair, in the same function, when the defect was a property of both.**

---

## B-2 · WHY "COLUMN 0 EVERYWHERE" IS THE WRONG REPAIR, AND WHAT IS RIGHT

The asymmetry is not arbitrary — and this is why it should not be closed by copying the aligned
pattern's anchor onto the colon one.

**A frontmatter key may legitimately be indented.** YAML nests; a declaration inside a nested block
sits at depth. Requiring column 0 on the colon form would discard exactly the artifact this whole
thread was about — `APPROVAL-GOV311-DEVIATIONS.md:7`, the only `[frontmatter]` row in either
population, found one case-sensitive sweep away from never being found at all.

**The tool already holds the distinction it needs.** It emits `[frontmatter]` as a tag, so it knows
the region. The rule that keeps every true positive and drops the false ones is regional, not
columnar:

```
IN FRONTMATTER   allow indentation      — nested keys are real declarations
IN THE BODY      require column 0       — an indented body line is prose or quotation
```

Checked against all three specimens: `APPROVAL-GOV311-DEVIATIONS.md:7` survives (frontmatter,
indented); `REV-SCIAB-MIRROR-001.md:399` survives (body, column 0, inside a fence); this seat's
line 52 is excluded (body, indented). **No true positive in either population is lost.**

---

## 3 · SUMMARY

| # | finding | status at `a68a8091` |
|---|---|---|
| A-2 | `re.I` symmetry | ✅ closed, verified at lines 21–22 |
| A-3 | quotation counted as declaration | ⚠️ closed for aligned, **open for colon** — B-1 |
| B-2 | the repair is regional, not columnar | new; preserves all three specimens |

**Verified closed:** S-3, S-4, A-1 (conceded and re-measured by the coordinator), A-2. **Unchanged:**
S-2, the `9`/`10` scope label.

**Not asserted:** no count of indented colon-form quotations across the corpus is claimed here. Three
specimens were tested, not a population — and the absence of a search is not a zero.

END OF ADDENDUM.
