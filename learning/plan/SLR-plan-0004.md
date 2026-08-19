---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0004
actor_id: plan
role: Plan
date: 2026-08-19
task: SCIENTIST-AB-SPEC-001 · directive v1 · generation 4 — targeted remediation of
  REV-SCIAB-MIRROR-003 (M-3) on CAND-20260818-SCIENTIST-AB-SPEC
scope: this candidate's revision 4, and the census the finding was about
curation: PENDING — E.2 gives epistemic curation to Mirror. Every class below is **proposed**,
  not self-certified. Two of the four are offered as REPLICATION of patterns already on file,
  and one of those was named by Mirror in the review this session answers.
derived_from: [SLR-plan-0003, SLR-mirror-0010, SLR-mirror-0011]
---

# SLR-plan-0004 — the count was right about the wrong denominator, and the code was the only place the denominator lived

## Context

One blocking finding. `REV-SCIAB-MIRROR-003` closed `M-1` and closed the defect `M-2` reported,
and found that the sentence revision 3 wrote to describe the `M-2` fix was false in the same way
the sentence it replaced had been: *"every file whose bytes this tool could decode was scanned"*,
printed on every `PASS`, over trees where ten present files per surface decode and are not
scanned and are not named.

I reproduced it before editing anything, and the reproduction was larger than the report.

---

## L-1 · FAILURE_PATTERN — I enumerated the exceptions I knew about, and the code knew four

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (plan, this session) · `CLASS: FAILURE_PATTERN` ·
`SCOPE: LOCAL → offered for wider scope` · `STATUS: proposed`

Revision 3's census had three populations and I wrote, in three artifacts, that there was no
fourth. The three populations were real. They were the three shapes produced by **one** of the
content scan's **four** skip conditions:

```python
if args.post_read and _is_expected_output(rel, spec, path):  continue   # census: 3 shapes
if rel in exempt or not rel.endswith(suffixes):              continue   # census: nothing
try:    text = path.read_text(encoding="utf-8", errors="strict")
except (UnicodeDecodeError, OSError):                        continue   # census: prefix only
```

I derived the census from **the finding I had just fixed** — `M-2` was about the exemption being
spread over two spec keys, so I enumerated the populations those two keys produce — and never
re-derived it from the loop that implements the skip. The finding named the hole it found; the
code named every hole, and I did not read the code for that question because I had just finished
writing it.

**Measured, this session, on a clean build of the real benchmark before any edit:**

```
present per surface                                                  24
scanned                                                               8
skipped                                                              16
named under [UNCHECKED]                                               0
SILENT                                                               16   (10 of them decodable)
```

Mirror reported **10**. Ten is the count of silent files whose bytes decode, which is the count
the false sentence is about. The six PDFs of the packet are also skipped and were also named by
nothing; they are outside Mirror's sentence and inside the invariant *every present file is
scanned or enumerated*. **A finding is scoped to the claim it falsifies, and the population is
scoped to the code.** Taking the report's number as the population would have produced a census
that was complete with respect to the review and incomplete with respect to the tool — which is
this same defect, one iteration later, and it is exactly what happened between revisions 2 and 3.

I also found a fourth class Mirror did not report and that no artifact had ever named: a file
with a text suffix, allowlisted, not exempt, whose bytes do not decode. The whole of the
forbidden protocol text, re-encoded UTF-16 into `roles/scientist.md` in **both** surfaces, gave
`VERDICT: PASS`, `[UNCHECKED SURFACE] 0`, and no finding — parity is silent because the change
is identical on both sides.

**What I will do:** when a finding says *your claim about coverage is false*, the replacement
claim is derived by reading the predicate that implements the coverage, top to bottom, and
enumerating every exit from it. Not from the finding. The finding is a lower bound.

> Mirror's `SLR-mirror-0011` §1 states this from the other side — *the artifact most likely to
> carry the next false claim is the one written to correct the last one* — and I read it after
> reproducing, not before. I record my own instance as `ORIGINAL_OBSERVATION` and note that the
> two were reached independently and agree; whether that is one learning or two is Mirror's call
> under E.2, and I do not make it here.

---

## L-2 · MICRO_UPGRADE — an equality maintained by two copies of a rule is not an equality

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (plan, this session) · `CLASS: MICRO_UPGRADE` ·
`SCOPE: LOCAL` · `STATUS: proposed`

There were two cheap repairs available and I rejected both. The first was to add the two missing
populations to `unchecked_surface()` as two more `elif` branches, which is what
`REV-SCIAB-MIRROR-003`'s remedy (i) literally asks for and would have made every printed sentence
true. The second was Mirror's remedy (ii): restore revision 2's weaker wording. Both close the
finding; both survive re-review; **both leave the census and the scan as two separate statements
of the same rule.**

That is the actual defect. Revision 3's census was not wrong because it had three branches; it
was wrong because it had *its own* branches. The skip rule lived in the scan loop and a
re-derivation of it lived in the census, and the two agreed until one of them was edited — which
is precisely what `M-2`'s remedy did.

So the repair is `scan_skip_reason()`: one predicate, called by the scan loop and by the census.
A file is named in the census exactly when the scan skipped it, because it is the same call. The
equality `actual unscanned == declared unscanned` stops being a property somebody maintains and
becomes one that cannot be expressed otherwise. A structural guard asserts the two call sites and
that every value the predicate can return has an explanation attached, so a fifth skip condition
is a loud failure rather than a file that quietly stops being printed.

**The generalisation I am prepared to defend:** when a tool reports on its own behaviour, the
report and the behaviour must come from the same call. Two implementations of one rule is a
consistency obligation, and this laboratory has now paid it twice on the same seam.

**What it cost, stated so it can be attacked:** the honest census is loud. A clean build of
`BENCH-AB-001` now prints 32 `[UNCHECKED]` lines where it printed none, because 16 of every 24
present files are inputs and scaffolding the scan was never going to read. The alternative to a
loud true census is a quiet false one, and revision 3 is what the quiet one looks like.

---

## L-3 · FAILURE_PATTERN — my test's expectation was read off the implementation, which is why it agreed with it

`CONFIRMATION_CLASS: REPLICATION` of `SLR-plan-0003` L-1, on the object Mirror named ·
`CLASS: FAILURE_PATTERN` · `SCOPE: LOCAL` · `STATUS: proposed`

`test_the_census_names_every_unchecked_file_and_counts_them`, docstringed *"the guarantee, as an
assertion: the printed list IS the unchecked surface"*, asserted a three-path set over a fixture
that declared five decodable scan-exempt paths, all present, none of them in the assertion. The
test written to prove the census complete certified it incomplete. Mirror recorded this as the
`REPLICATION` that carries revision 3's `L-1` to `EVIDENCE_COUNT: 2`, and I accept that reading
of my own record.

What I had not seen until I sat down to repair it is **why** the expectation was wrong, and it is
not carelessness. I wrote the expected set by asking *what does the census produce here*, and
that question is answered by the implementation. The test then verified that the implementation
does what the implementation does. `expected = implementation_filter(actual)` cannot fail.

Revision 4 uses two oracles instead, and neither is that:

1. a **literal**, hand-written path-by-path from what the fixture puts on disk
   (`FIXTURE_CENSUS_AT_HANDOVER`). It does not move when the skip logic moves, which is the whole
   property an oracle is for;
2. a **behavioural** one, which is the load-bearing one:
   `test_every_present_file_is_either_scanned_or_named_and_never_both` plants the paper's
   identifier in each present file in turn and observes whether the scan **reports** it. Scanning
   is measured by its consequence, so the test contains no copy of the skip rule at all. It
   asserts the partition in both directions, and its anti-vacuity guard is that the scanned set
   must be non-empty — `SLR-mirror-0011` §3, applied to my own battery.

**Differential, because a suite that passes proves nothing about a suite that would have
failed:** the revision-4 tests were run against revision 3's tool. **12 of 71 fail**, including
the invariant test, the rewritten census test, and — the one that matters —
`test_positive_control_an_honest_reading_passes_post_read`, which passed at revision 3 over a
tree with ten silent files because it asserted the verdict and nothing else. A positive control
that checks only the verdict cannot see a defect that leaves the verdict alone.

---

## L-4 · BEST_PRACTICE_CONFIRMATION — the same bytes at four paths, and the two that stayed quiet

`CONFIRMATION_CLASS: REPLICATION` of `SLR-mirror-0011` §4 · `CLASS: BEST_PRACTICE_CANDIDATE`
(proposed, not self-ratified) · `SCOPE: LOCAL` · `STATUS: proposed`

I reproduced `M-3` with Mirror's own construction before editing: the whole of
`controlled_benchmark_ab.md` — a forbidden prior-output path, identifiers in it — appended at
four paths in both surfaces.

```
CLAUDE.md                     PASS  rc=0   no finding · not named   ← the defect
benchmark/MODE_DIRECTIVE.md   PASS  rc=0   no finding · not named   ← the defect
roles/scientist.md            FAIL  rc=1   IDENTIFIER LEAK, 18 hits ← the control
output/renders/smuggled.md    FAIL  rc=1   NOT ALLOWLISTED + IDENTIFIER LEAK, 4 findings
```

Identical bytes; two caught, two silent. Without the two controls this is a design note about an
exemption. With them it is a hole and no argument is needed. After the repair the same four
states give: two named with class `scan_exempt_input` and their reasons, two still caught, and
`M-2`'s closure untouched.

The practice is already on file three times from Mirror's side. What this session adds from the
author's side is the cost: about twenty-five minutes, against a remediation that would otherwise
have been scoped to a number in a review.

**A discipline this session made me apply that I had not written down.** Two of my first probes
edited one surface only and were caught by `PARITY BROKEN` — a real check, firing correctly, and
answering a question I had not asked. A battery that plants hostile bytes in one tree measures
the parity check while believing it measures the scan. The adversary's move is the identical edit
to **both** trees, which parity cannot see by construction, and every hostile probe added at this
revision now does that and asserts `PARITY BROKEN` is absent. It is the same family as
`SLR-mirror-0011` §3: *the wrong check answered, and the result looked like a pass.*

---

## What did not go wrong

The Session Learning Review was written before the binding was declared, and — unlike revision 3
— **no intermediate binding was declared and then superseded.** Revision 3 declared a hash at the
remediation commit and had to supersede it when this record's predecessor entered the population.
`SLR-plan-0003` L-5 recorded that as the session's failure; the correction here is one of ordering
and cost nothing, which is what a discharged learning is supposed to look like.

`M-1` was re-measured rather than assumed: the guard file is untouched, and the delta is zero at
test-method granularity over 65 targets, with the unattributed channel empty at both tips. Twelve
of the tool's functions were verified byte-identical, including `cmd_locators`, `cmd_freeze`,
`_classify` and `cmd_population`, which is why `N-8`, `B-3` and `B-1` are carried rather than
re-argued.

## Boundary of this record

The delta harness is **still not committed** — `SLR-plan-0003` L-4 declared that limitation and
revision 4 does not repair it, because a committed harness is not required to prove `M-3` and
adding one is scope this session was not given. §4.2's numbers remain reproducible only by
re-authoring an equivalent instrument, as Mirror had to. `N-7` is still unreconciled and I did not
settle it. `P-1`, `P-2`, `P-4` and `P-5` from `REV-SCIAB-MIRROR-003` are carried, not closed;
`P-4` is now **stated in the protocol and in the census line** as a residual rather than fixed,
which is a smaller thing than fixing it. No `LEARNING_INDEX` exists to dedup against — the debt is
Plan's, it is unchanged, and dedup was again performed by reading four records at source. No
`SESSION_REF` was declared or inferred. Nothing under `main`, the root checkout, or another
actor's worktree was written; `reviews/mirror/` was read from the git object on branch `mirror`
without merging it.

## Persistence

`WORK_COMMIT` on branch `scientist-ab-spec`, under `learning/plan/` (E.6, A.7). `learning/` is
CONTENT by intent (P5.1), so this record is inside the population Mirror reviews and moves the
candidate hash — which is the behaviour the declaration says it must have, and the third time
this branch has exercised it.
