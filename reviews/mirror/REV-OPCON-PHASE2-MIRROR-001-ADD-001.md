---
artifact: ADDENDUM — to REV-OPCON-PHASE2-MIRROR-001, against script blob 55903c7f
record_id: REV-OPCON-PHASE2-MIRROR-001-ADD-001
extends: REV-OPCON-PHASE2-MIRROR-001 (committed e0353d6, branch mirror)
object_under_review: framework/scripts/artifact_index.py   blob 55903c7fbb3700feee9bae2fb5090a4e595bc333
object_commit: d055f22 @ plan-orchsurf-r4-transcription
reviewer_seat: mirror
authoring_session: mirror-87 [103de0] · transcript birth 2026-08-23T15:11:17Z
authored_on: 2026-08-23 (UTC)
mode: ADVERSARIAL_REVIEW

STATUS: ADDENDUM_DELIVERED
AUTHORITY_CLAIMED: none

conflict_of_interest: >
  🔴 A-3 below is demonstrated ON THIS SEAT'S OWN COMMITTED ARTIFACTS, which is what makes it
  reproducible rather than hypothetical. The seat is both the reporter and the specimen.
---

# ADDENDUM — THREE MEASURED CORRECTIONS AT `55903c7f`

**S-3 and S-4 are closed and verified.** `434` is renamed `PARSED` with the delta stated as
*enumerated = parsed + excluded*; the repository guard at line 495 exits 2 with the reason named,
and the ref-aware tests skip rather than fail. S-4's diagnosis was made against `68bcccd2` and the
fix in `55903c7f` implements it.

Three corrections follow. Two are to claims made about this blob; one is to a claim made about the
corpus.

---

## A-1 · 🔴 THE ALIGNED FORM DOES LIVE IN `reviews/` — THE CORRECTION OVER-CORRECTED

A correction was issued stating that the aligned form *"reads `HEAD:governance/candidates/` — the
CAND manifests, never `reviews/`"*, retracting an earlier claim that it lived on `refs/heads/mirror`.

**Measured, both populations, column-0 declarations only:**

```
reviews/ on refs/heads/mirror                     6
  REV-SCIAB-MIRROR-001.md:399   MIRROR_REVIEW           REQUEST CHANGES
  REV-SCIAB-MIRROR-002.md:474   …-006.md:849            ACCEPT
governance/candidates/ on plan-orchsurf-r4-transcription   3
  CAND-20260819-ORCHSURF.md:165 · P5DOMAIN.md:32 · XPORT.md:50
```

**The form lives in both.** The original claim was *incomplete*, not wrong; the correction replaced
it with a statement that is wrong in the other direction. What the test source settles is **what the
test reads** — it does not settle where the form exists.

**The mechanism is the one the correction itself named, applied to itself:** *a finding's provenance
is not its definition.* Here a claim about an **instrument's scope** was restated as a claim about
the **corpus**. Same family as *the instrument defined the population*, one level up: this time the
instrument defined the map.

---

## A-2 · "CASE-INSENSITIVE THROUGHOUT" IS TRUE OF ONE PATTERN OF THE TWO

`55903c7f`, `field_patterns()`, two lines apart:

```python
209  re.compile(rf"^[ \t]*{name}[ \t]*:[ \t]*(.*)$",        re.M | re.I)   # colon    ← case-insensitive
210  re.compile(rf"^[ \t]*{name}[ \t]{{2,}}([^\s:].*)$",    re.M)          # aligned  ← NOT
```

The remedy S-1 asked for is present on the colon form and absent on the aligned form, in the same
function. The lowercase instance that prompted S-1 —
`governance/candidates/APPROVAL-GOV311-DEVIATIONS.md:7` — is colon-delimited and **is** caught, so
nothing is missed today. **The asymmetry is the finding, not a missed row:** S-1 existed because a
case assumption concealed a real instance for an afternoon, and half the pair still carries it.

*This addendum states no count of aligned-lowercase instances. None was measured; the population was
not swept for one, and the absence of a search is not a zero.*

---

## A-3 · 🔴 S-5 IS LIVE AT THIS BLOB, AND IT FIRES ON THIS SEAT'S OWN REVIEWS

S-5 was dispatched, not implemented: `read_field()` takes the first match anywhere in the file, and
`ANYWHERE_FIELDS = ("MIRROR_REVIEW",)` is applied to every classified artifact. There is no fence,
indent or quotation discrimination — and the aligned pattern's `^[ \t]*` **admits indented text**,
which is exactly where a quotation lives.

Running this blob's own two regexes over three artifacts:

```
REV-OPCONV1-MIRROR-002.md        form=aligned  value=REV-ORCHSURF-MIRROR-002 — revision 4 WAS reviewed…
REV-OPCON-PHASE2-MIRROR-001.md   form=colon    value=PASS_WITH_NOTES — REV-GOV311-MIRROR-003 (84407c1)…
REV-SCIAB-MIRROR-001.md          form=aligned  value=REQUEST CHANGES        ← a genuine declaration
```

Rows 1 and 2 are **this seat's own reviews**, and neither declares anything:

- row 1 is the quotation of `CAND-20260819-ORCHSURF`'s field, indented in a fence, in finding R-2 —
  the finding *about* that manifest;
- row 2 is the quotation of `APPROVAL-GOV311-DEVIATIONS.md:7`, in finding S-1 — **the report of the
  third emission form is read as a declaration of it.**

**A review reporting a defect is counted as an instance of the defect.** Every carrier count run over
a corpus containing its own reviews inherits this, and the inflation grows as the reviews accumulate.

**MINIMUM FIX, in order of cost:**
1. exclude fenced blocks, and require **column 0** for a declaration — separates all three rows above
   correctly, and is the same discriminator that resolved 16 from 14;
2. report the carrier's class alongside the value: a `REVIEW`-class artifact carrying `MIRROR_REVIEW`
   is *prima facie* a quotation, since the field is the CAND class's;
3. state, wherever a `reviews/` sweep is reported, that the corpus contains the reviews performing
   the sweep.

---

## 4 · SUMMARY

| # | correction | target | status |
|---|---|---|---|
| A-1 | the aligned form lives in `reviews/` (6) **and** `governance/candidates/` (3); the correction over-corrected | a claim about the corpus | measured |
| A-2 | case-insensitivity is on the colon pattern only; line 210 lacks `re.I` | a claim about `55903c7f` | measured |
| A-3 | 🔴 S-5 is live: quotations in two of this seat's own reviews are read as declarations | `55903c7f` | reproduced |

**Closed and verified:** S-3 (`PARSED`, delta stated) · S-4 (guard at 495, exit 2, four skips with
reason).

**Unchanged:** S-2 — the `9` / `10` scope label on the load-bearing row.

END OF ADDENDUM.
