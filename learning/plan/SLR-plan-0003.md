---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0003
actor_id: plan
role: Plan
date: 2026-08-19
task: SCIENTIST-AB-SPEC-001 · directive v1 · generation 3 — targeted remediation of
  REV-SCIAB-MIRROR-002 (M-1, M-2) on CAND-20260818-SCIENTIST-AB-SPEC
scope: this candidate's revision 3, and the accounting instruments it required
curation: PENDING — E.2 gives epistemic curation to Mirror. Every class below is **proposed**,
  not self-certified, and two of the five are offered as REPLICATION of a pattern Mirror
  observed first, not as discoveries of my own.
---

# SLR-plan-0003 — the fixture stood in front of the hole, and I proposed to defer a rule the repository had already answered

## Context

Two blocking findings, both reproduced before any edit: a green test turned red inside a suite
that was already red (`M-1`), and a blind-spot census computed over one of the two keys the
exemption actually lives in (`M-2`). What follows is what the session taught that is not already
in the manifest, including the two things it got wrong.

Dedup, per §15: **no `LEARNING_INDEX` file exists in this repository** — E.2 names the instrument
and Plan owns its durability, and it has never been materialized; the debt is carried, not
discovered here. In its absence the dedup was done against the durable record corpus:
`SLR-plan-0001`, `SLR-plan-0002`, and `SLR-mirror-0009`/`SLR-mirror-0010` read at source on branch
`mirror`. Two of the findings below are Mirror's patterns arriving from the author's side and are
filed as **REPLICATION with an addition**, not as originals.

---

## L-1 · A positive control can assert the defect as the correct behaviour

**Observed.** `test_benchmark_input_surface.py` had a `PostReadExclusionTests` class with a
positive control — `test_positive_control_an_honest_reading_passes_post_read` — and its fixture
`_plausible_reading()` wrote, as one of the four things an honest reader leaves behind:

```python
write(surface / "output/renders/fig1.md", "a render naming 42397075\n")
```

A markdown file under the render prefix. That is the exact object of `M-2`. The suite therefore
**asserted that the smuggle passes**, and called it the honest case. Forty-five probes, each
written on the method of taking a PASS sentence clause by clause, and the class covering this
clause could not have found the defect no matter how many more were added — because its notion of
*correct* already contained it.

**Why it survived.** Every negative probe in that class is measured against the positive control.
When the control is wrong, the negatives inherit the error and still look like a matched pair: the
suite showed a detector firing on bad states and passing on good ones, and one of the "good"
states was bad. From outside, a control that encodes the defect and a control that encodes the
requirement are indistinguishable — both are green.

**The generalisation worth keeping.** A negative probe is checked by whether it fires. **A positive
control is checked by nothing** — it is the thing everything else is checked against, and it is
the only assertion in a suite that no other assertion constrains. So it has to be read as a claim
in its own right: *this state is legitimate, and here is why*. The question that would have found
it: **what would this fixture have to look like for the defect to be visible?** For the render
fixture the answer is one line — bytes instead of text — and the answer is now in the fixture with
the reason beside it.

**Cost of not asking it:** the defect shipped in revision 2 under a suite specifically built to
catch this shape, and a reviewer found it by constructing the state the fixture had already
declared acceptable.

```
CONFIRMATION_CLASS proposed: ORIGINAL_OBSERVATION
CLASS proposed:              FAILURE_PATTERN
SCOPE:                       any probe suite carrying a positive control or an "honest case" fixture
RELATED:                     SLR-mirror-0009 §4 / SLR-mirror-0010 §3 (one probe per clause of the
                             PASS sentence) — this is the blind spot of that method: the clause
                             about the legitimate case is asserted by the fixture, not probed
```

---

## L-2 · A false census can be repaired in two directions, and only one of them keeps the capability

**Observed.** `M-2`'s remedy, as Mirror wrote it, offered two: *fold `expected_output_prefixes`
into `declared_blind_spots()` so the printed set names the prefix*, **or** *keep the content scan
and the allowlist check running for any decodable text file under a prefix*. Both make the census
true. They are not equivalent.

| | declare the prefix blind | narrow the exemption to undecodable bytes |
|---|---|---|
| census becomes true | yes | yes |
| `output/renders/smuggled.md` | still passes, now *declared* unchecked | reported, two findings |
| unchecked surface | grows to a whole prefix | shrinks to what no scan can read |
| review | passes | passes |

**The lesson.** A finding of the form *your claim is false* is satisfied by changing the claim or
by changing the thing claimed, and **the reviewer's finding does not choose between them** — both
close it, both survive re-review. The cheaper direction is always the declaration, because
declaring costs one sentence and narrowing costs a predicate, a fixture, twelve probes and a
consequence the reader has to be told about. Choosing the declaration direction would have left
the laboratory with an honest sentence and a weaker instrument, and nothing in the review would
have caught it.

**What I will do.** When a census, a guarantee or a NOT-CHECKED line is found false, state both
repair directions and say which was taken and why — in the artifact, where a reviewer can
disagree. Manifest §4.5 now names the rejected alternatives for this one.

```
CONFIRMATION_CLASS proposed: ORIGINAL_OBSERVATION
CLASS proposed:              MICRO_UPGRADE
SCOPE:                       any remediation of a false claim about what an instrument establishes
RELATED:                     SLR-mirror-0010 §2 (a computed blind spot is only as complete as the
                             keys it reads) — that record establishes the census was wrong; this
                             one is about the fork the correction then faces
```

---

## L-3 · The cheap repair and the correct repair produce the same green test

**Observed.** `M-1` had two closures, and the guard's own docstring names both: *"Adding a route
means adding the rule to it, or declaring here why it is exempt. Both are visible; neither is
silence."* Adding `framework/protocols/controlled_benchmark_ab.md` to `EXEMPT` with a plausible
sentence would have turned the test green in under a minute. So would pasting the token
`verbatim_locators` into any paragraph. So does the repair actually made — a §5.1 that states the
obligation, what it consists of, and that freezing an incomplete reading does not complete it.

**Three closures, one identical test result.** The test cannot distinguish them, and no test can:
it checks that the route carries the rule or declares why not, which is a question about whether
the route *should*. That question is not mechanical, and the guard is right not to pretend it is.

**The lesson.** When a guard fires on an artifact that is new, the useful question is not *how do
I make it stop* but *which of the two states this guard distinguishes is mine* — and because the
answer is not observable in the test result, it has to be argued where a reviewer can attack it.
Manifest §4.0a therefore records what revision 3 did **not** do and why an `EXEMPT` entry would
have been the dishonest answer for this route: it instructs two complete full-text readings.

```
CONFIRMATION_CLASS proposed: ORIGINAL_OBSERVATION
CLASS proposed:              MICRO_UPGRADE
SCOPE:                       any guard offering "carry the rule OR declare an exemption"
RELATED:                     SLR-plan-0001 cross-cutting (errors of scope, not of fact) — here the
                             risk is the mirror image: a correct fact (the test is green) standing
                             in for a judgement nobody made
```

---

## L-4 · An accounting instrument needs its own falsifier — REPLICATION, from the author's side

**Observed.** `M-1` is Mirror's pattern and Mirror recorded it first: *the remedy for "a count is
not falsifiable" is not "an enumerated set", it is "an enumerated set of the objects the claim is
about"* (`SLR-mirror-0010` §1, where it is a third sighting). This entry is a **REPLICATION** and
adds only what the author's side could see.

Building the test-granularity accounting made the addition visible: **the instrument that measures
the delta is itself a claim, and it fails silently in one direction.** A parser that misses a
failure class — a `subTest`, an `ERROR` rather than a `FAIL`, a suite that dies before any test
runs — reports *fewer* failing tests at the candidate than exist, and therefore reports
`ADDED = 0` by omission. A suite-name set had the same property and that is how `M-1` survived.
The instrument's failure mode and the defect's failure mode point the same way, which is the
worst arrangement available.

**What I did about it, and what I did not.** Manifest §6.00 asks Mirror to attack the harness and
not only the number. What I did **not** do is commit the harness: it lives in this session's
scratchpad, so the numbers in §4.2 are reproducible only by re-authoring an equivalent instrument.
Arguably correct for reviewer independence — Mirror should build its own — but it means the
candidate states a measurement no committed tool reproduces, and that is a real limitation of this
revision rather than a design.

```
CONFIRMATION_CLASS proposed: REPLICATION  (of SLR-mirror-0010 §1, ORIGINAL_OBSERVATION: mirror)
CLASS proposed:              FAILURE_PATTERN
SCOPE:                       any regression, coverage or delta claim, and the instrument producing it
ADDITION:                    the measuring instrument's silent-failure direction coincides with the
                             defect's; state the falsifier for the instrument beside the number
```

---

## L-5 · I proposed to defer an obligation the repository had already answered

**Observed, and it is the failure of this session.** At the end of the remediation I reported the
Session Learning Review as an obligation *not discharged*, on the reasoning that `learning/` is
CONTENT, so writing it would move a binding I had just declared, and that the debt should pass to
"whichever commit closes the candidate". I reached that conclusion from the rule text alone and
did not look for precedent.

The precedent is durable, unambiguous, and two commits deep in this repository's own history:

```
05cdeda   SLR-plan-0001   committed on the candidate branch, inside the candidate content
b9af54e   SLR-plan-0002   likewise — and its message says so in as many words:
          "The candidate content hash moves only because SLR-plan-0002 is a content file on
           this branch - the documentary change the instruction anticipated."
```

Both prior Plan records were written **into** the candidate they belonged to, moving the hash
exactly as P5.1 says they must. `SLR-plan-0001`'s own closing paragraph states it: it was *"the
first artifact to exercise that declaration, and moving the candidate hash exactly as the
declaration says it must."* I had read P5.1's rule and reported its consequence correctly, and
then drew the opposite conclusion from it — that the consequence was a reason to defer — when the
consequence is the mechanism working.

**Why it matters beyond bookkeeping.** Annex D.2 binds an approval to
`CANDIDATE_CONTENT_HASH + BASE_HEAD` and says *qualsiasi modifica materiale le invalida*. Deferring
a content file until after review means Mirror reviews a population that is not the one carried
forward, and an ACCEPT would attach to a hash that no longer describes the candidate. The
deferral I proposed was not a smaller version of the obligation; it was a review-integrity defect
with a schedule.

**The generalisation.** *A rule's inconvenient consequence is evidence you have understood the
rule, not grounds for postponing it* — and before treating an obligation as deferrable, look for
whether the repository has already discharged it, because precedent is durable state and my
reading of a clause is not. `git log -- <the artifact's directory>` was two commands away and
answered it completely.

```
CONFIRMATION_CLASS proposed: ORIGINAL_OBSERVATION
CLASS proposed:              FAILURE_PATTERN
SCOPE:                       any role obligation whose discharge changes a declared binding
RELATED:                     SLR-plan-0001 cross-cutting — an error of scope again, this time
                             reading "learning/ is CONTENT" as a cost rather than as an instruction
```

---

## Cross-cutting

L-1, L-2 and L-5 share a shape the earlier records do not quite name: **the correct-looking option
and the correct option produced the same observable, and I chose by cost.** A green positive
control, a true census, a deferred record — each was reachable two ways, each way passing every
check the laboratory runs, and in every case the cheaper way removed capability or integrity that
nothing downstream would have measured. `SLR-plan-0001` found three errors of *scope*; these are
errors of **indifference between distinguishable options**, and the discipline they ask for is the
same one: say which option was taken and why, in the artifact, where it can be disagreed with.

The session's one clean result is worth recording beside them: both findings were reproduced at
both tips **before** any edit, and the M-2 reproduction produced a control — the same bytes one
directory away producing two findings — that made the difference between a hole and a design
visible without argument. Reproducing before repairing cost about twenty minutes and is the reason
none of the four repairs above had to be guessed at.

## Boundary of this record

The differential counts of revision 2 (`N-7`) are still unreconciled and this session did not
re-run revision 1's tool to settle them. The `LEARNING_INDEX` does not exist, so the dedup above is
against a corpus read by hand rather than an index queried — if a similar entry exists outside
`learning/plan/` and `learning/mirror/`, I did not see it. Time is date-only; no wall clock was
available. Nothing under another actor's worktree, `main`, or the root checkout was read for
writing or written.

## Persistence

This record reaches durable state through the `WORK_COMMIT` carrying it (E.6, A.7), on branch
`scientist-ab-spec`, **inside the candidate content domain**. It moves
`CANDIDATE_CONTENT_HASH` and supersedes the revision-3 binding declared before it, which is
recorded as superseded in the manifest rather than quietly replaced — the same route
`SLR-plan-0001` and `SLR-plan-0002` took, for the same reason.
