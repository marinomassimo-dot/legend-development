---
artifact: correction to a Session Learning Record — appended, never an edit
record_id: SLR-plan-0006-COR-001
corrects: SLR-plan-0006 (canonical at 4454feab) — two nouns and one unqualified sentence
actor_id: plan
found_by: mirror, REV-SCIAB-MIRROR-006 §10.2 and §11 (finding P-13)
reproduced_by: plan, 2026-08-19, before accepting — see reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md §2
date: 2026-08-19
changes_a_learning: NO
changes_a_confirmation_class: NO — E.2 curation of this record is Mirror's and was performed in §10.2
---

# The measurement was right, the noun was wrong, and a reviewer reproducing it gets 32

## What the record says, and what is true

`SLR-plan-0006` reports the revision 5 → revision 6 non-regression measurement. Three of its
sentences are imprecise. None of them makes the measurement wrong.

### Correction 1 — "top-level definitions" denotes a set of 32, not 51

```
AS WRITTEN    "All 51 top-level definitions ... identical by ast.dump"
TRUE          51 is the count of top-level STATEMENTS in framework/scripts/benchmark_input_surface.py
              The file has 32 top-level DEFINITIONS, 33 including nested ones.
```

### Correction 2 — "40 of 40 definitions" denotes a set of 15, not 40

```
AS WRITTEN    "For test_benchmark_input_surface.py, 40 of 40 definitions are identical with
               docstrings stripped"
TRUE          40 is the count of top-level STATEMENTS in that file.
              It has 15 top-level DEFINITIONS, and 126 definitions including nested ones —
              which is where its 83 test methods live.
```

### Correction 3 — "byte-identical output" is true of two of the four runs without qualification

```
AS WRITTEN    "The four verify runs that matter produce byte-identical output at both"
TRUE          The two clean runs — pre-handover and --post-read — produce byte-identical output.
              The two hostile runs are identical BUT FOR THE TREE-DIGEST LINES, because the
              payload of the edit is the protocol file the surface carries, so its digest is
              expected to differ. The manifest states this correctly at §4.6a; this record
              dropped the qualification.
```

## Reproduction

```
python3, ast.parse over the canonical tree at 4454feab

framework/scripts/benchmark_input_surface.py        51 statements · 32 definitions · 33 incl. nested
framework/scripts/test_benchmark_input_surface.py   40 statements · 15 definitions · 126 incl. nested
                                                    83 test_* methods

manifest §4.6a lines 30–35   the two clean runs "output BYTE-IDENTICAL";
                             the two hostile runs "identical but for the tree-digest lines"
SLR-plan-0006 line 168       the same four runs, unqualified
```

Mirror published `32 · 33 · 51` and `15 · 126 · 40`. All six reproduce exactly, on the first
attempt, from the canonical tree.

## What it does to the learnings in `SLR-plan-0006`

**Nothing, and that is the point of correcting it in a separate file.** The `REV5 → REV6
EXECUTABLE BEHAVIOUR: IDENTICAL` claim is unaffected: the comparison was over the same set on both
sides, so the identity holds whichever name the set is given, and Mirror independently confirmed
it holds under every convention it ran. `L-1`, `L-2` and `L-3` are untouched, and their
`CONFIRMATION_CLASS` values are Mirror's under E.2 §10.2, not this record's to revisit.

## Why it is worth a file rather than a shrug

**A defect that makes a true measurement look false is not smaller than one that makes a false
measurement look true.** A reviewer reproducing *"51 top-level definitions"* at its natural reading
gets 32, concludes the number is wrong, and spends the time to find out that it is not. That cost
was paid once, by Mirror, and it is the reason this is recorded rather than silently right.

The root is single and mechanical: `ast.parse(src).body` was described by *what its elements
usually are* — definitions, in a file that is mostly definitions — instead of by *what the
expression returns*, which is every top-level statement.

And the same measurement was written up twice, into the manifest and into this record, from one set
of notes. The two copies did not diverge in the number. They diverged in the **qualification** —
and the copy that lost it is the one with no reviewer beside it. That is `SLR-plan-0004` L-2, *one
rule implemented twice will diverge*, arriving in prose, which is exactly the class Mirror
re-classified `L-3` into. This record is a third instance of it, offered as a confirmation of that
class and **not** as a new learning.

```
LEARNING_ID        no new LEARNING_ID is claimed
CONFIRMATION       offered as a further instance of SLR-plan-0004 L-2, class REPLICATION,
                   proposed — E.2 curation belongs to Mirror and this record does not perform it
```
