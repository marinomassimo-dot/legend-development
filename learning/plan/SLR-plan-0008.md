---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0008
actor_id: plan
role: Plan
date: 2026-08-19
task: XPORT-ROUTING-001 · directive v1 · generation 1 — targeted remediation of the single
  blocking finding M-1 of REV-XPORT-MIRROR-001, producing CAND-20260819-XPORT revision 2
scope: one blocking finding, two false sentences, one new normative subsection, one executed
  falsifier. No transport rule changed. Routing not reopened.
curation: PENDING — E.2 gives epistemic curation to Mirror. Every CONFIRMATION_CLASS below is
  **proposed**, never self-certified. L-1 in particular is adjacent to SLR-mirror-0015 L-2 and
  is offered as a distinct observation, not as a re-claim of it — Mirror decides which it is.
derived_from: [SLR-plan-0007, SLR-plan-0006, SLR-plan-0004, SLR-mirror-0014, SLR-mirror-0015]
---

# SLR-plan-0008 — the reviewer's suggested sentence was also false, and adopting it would have been the same defect one size smaller

## Context

`REV-XPORT-MIRROR-001` returned `REQUEST CHANGES` on one blocking finding. `M-1`: the transport
protocol's frontmatter and its §11 both assert that the protocol *names* no actor, role, worktree
or benchmark, and the same file names three actors and four roles across eight lines. Everything
else in the candidate — binding, partition, routing deferral, regression accounting, the size
model, the version model — was confirmed.

The correction had already been written, in revision 1's manifest §9.1b, where it moves no hash
and does not travel with the protocol. That is the whole of the defect: the truth existed and was
on the wrong side of the content / control-plane seam.

---

## WORK COMPLETED

```
IDENTITY            rehydrated fail-closed from durable state · roles/plan.md read in full ·
                    worktree evidence-index · governance 3.1.1
REVISION 1          verified from git, not from report — BASE_HEAD 4454feab unchanged, content
                    tip f48a807, hash 68173f01…c96a reproduced (positive control)
MIRROR REVIEW       REV-XPORT-MIRROR-001 + SLR-mirror-0015 read in full from durable state
M-1                 reproduced independently before editing — the two assertions located at
                    lines 16 and 424, the eight occurrences enumerated and classified
REMEDIATION         frontmatter actor_scope rewritten · §11 bullet rewritten · §11.1 added,
                    carrying the property, the three classes and the semantic falsifier ·
                    T-GENERIC-1 added to §10 and executed
FALSIFIER           executed, not asserted — 9 changed lines, none normative
GATES               LINT PASS (1 pre-existing INFO) · PUBLICATION GATE PASS / BLOCKS 0
M-2                 verified independently, classified, NOT repaired
NOT DONE            routing · P5 · orchestrator worktree · snapshot tags · T-TRANSPORT-1
```

---

## PROBLEMS

### 1 · The reviewer's suggested remedy was itself false of the file

`M-1` closes with a suggested replacement, offered as *"the author's own wording"*:

> *"No rule, no branch and no obligation in this protocol is conditioned on any actor, role,
> worktree or benchmark. **Actor names appear only in citations and measurements.**"*

The second sentence is false of the same file, and Mirror's own review contains the disproof.
Its §10 classification table sorts the eight occurrences into **three** classes, not two — line 5,
the `status:` line, is typed `FRAMEWORK RULE`, and a governance status line is neither a citation
nor a measurement. Revision 1's manifest §9.1b agrees, calling it *"front-matter status, the
standard formula on every PROPOSED artifact in this repository."*

So the sentence offered to repair a false absolute was a narrower false absolute, falsified by the
same enumeration in the same review that proposed it. Adopting it verbatim — which is the path of
least resistance, and which reads as deference to the reviewer — would have planted a third false
self-description in the file, in the revision whose entire purpose was to remove the first two.

### 2 · My first run of the falsifier measured a third of what it reported

`T-GENERIC-1` is a deletion test: strip every actor, role, worktree and benchmark name and ask
whether a normative sentence changes meaning. I ran it first through `sed -E` with `\b` word
boundaries for the role names. **BSD `sed` does not support `\b`.** The name pattern fired, the
role pattern silently matched nothing, and the run printed a tidy two-line diff that would have
supported exactly the conclusion I was hoping for.

Nine occurrences existed. Two lines changed. The result was clean, plausible, and void.

---

## SOLUTION

The property was derived from the protocol rather than from the review, and stated over all three
classes the file actually contains — MEASUREMENT, CITATION, GOVERNANCE STATUS — with the load
bearing on the semantic clause: *no rule, no branch and no obligation is conditioned on which
actor is acting.* Where a role does appear in a normative-looking position — §8's `DETECTION` row
naming who notices a missing artifact — the duty cited is one governance allocated already, in
body §43 and Annex G.3, and would bind identically if this protocol did not exist. That is the
carve-out, and it is written down rather than left as an unstated exception.

The falsifier travels **in the protocol**, not in the manifest, because the manifest is where the
first correction went to die. §11.1 states the deletion test, states that a grep is not it, and
states why: a grep returns non-zero on this compliant file and would return **zero** on a protocol
that branched on `ACTOR_ID` through a variable.

The void run was caught because the inventory grep had been run first, for a different purpose,
and it said nine. Re-run in Python, the test changed nine lines. The rewritten instrument now
refuses to report at all if either pattern matches zero occurrences.

---

## LEARNING

### L-1 — *A property expressed as the absence of a string is refuted by the cheapest check it invites, and passed by the failure it exists to exclude.*

`proposed: ORIGINAL_OBSERVATION (plan, this session) · offered for wider scope · adjacent to
SLR-mirror-0015 L-2, which is about where a correction sits; this is about how the property is
encoded`

Revision 1 meant *no transport rule is conditioned on actor identity* and shipped *no actor is
named*. The second is not a weaker version of the first. It is a **different predicate**, and it
fails in both directions:

```
LEXICAL CHECK (grep for names)      →  non-zero on this file, which is fully generic
                                    →  ZERO on a protocol reading `ACTOR_ID` into a variable
                                       and branching on it — the exact failure at stake
SEMANTIC CHECK (deletion test)      →  answers the question that was meant
```

> **When a property is semantic, encoding it as a string absence produces a claim that is easier
> to check, easier to falsify, and about something else. Inventory the names with a grep; decide
> with a test that deletes them and asks whether a rule changed.**

The reusable half is the diagnostic: if the check that would refute your claim is *cheaper* than
the claim is deep, the claim has probably been restated into the checker's vocabulary.

### L-2 — *A reviewer's suggested remedy is evidence, not a patch, and it inherits the defect class it was written against.*

`proposed: ORIGINAL_OBSERVATION (plan, this session) · offered for wider scope`

Annex C.2 makes `AUTHOR_RESPONSE` mandatory and says silence is not acceptance. It does not say
that a suggested formulation carries the reviewer's authority into the content — and here it could
not have, because the suggestion was falsified by the reviewer's own table two sections earlier.

The pull toward adopting it was real and worth naming: the reviewer had just been right about
everything, the wording was short, and it was explicitly framed as my own. All three are reasons to
read it *more* carefully, not less.

> **Apply a suggested remedy against the artifact, never against the reviewer's authority. A
> reviewer who correctly finds an over-strong claim is not thereby immune to writing one, and the
> author is the last party positioned to catch it.**

I record this without any implication that the review was weak. It found the defect, verified the
substantive property independently, and its declared falsifier is what made the remedy cheap. The
suggestion was one sentence inside a 953-line review that was right about the finding.

### L-3 — *An inventory built for one purpose is the cheapest available control for the instrument that later consumes it.*

`proposed: REPLICATION of SLR-mirror-0014's "shell as instrument", fourth recorded instance —
new mechanism (`\b` unsupported by BSD sed), same shape`

The class is not mine and I am not re-claiming it: an instrument returns a clean, agreeing,
plausible result while measuring nothing. Mirror has now recorded it three times; this is the
fourth, and the second in two sessions on this candidate.

What is worth adding is **why it was caught**, because it was not insight. I had run an inventory
grep minutes earlier, for the unrelated purpose of reproducing `M-1` before editing. It said nine.
The test said two. The disagreement was the detector.

> **Before believing a transform, compare its yield against a count you obtained by another route.
> Where no such count exists, make the instrument self-check — a pattern that matches zero
> occurrences must abort, not report a clean pass.**

The narrow, honest scope: this is one mechanism of a class already recorded, plus one cheap habit.
It is not a new class and I am not proposing it as one.

---

## MICRO-UPGRADE

1. **The falsifier now lives in the normative artifact** (§11.1), with the reason a grep is not it
   stated in the same block. The check and the claim are on the same side of the seam, which is
   `SLR-mirror-0015` L-2 applied rather than merely acknowledged.
2. **`T-GENERIC-1` added to §10 and actually executed** — nine changed lines, each classified. It
   can fail, which distinguishes it from the four tests Mirror correctly flagged as passing by
   construction (`O-1`).
3. **The session's deletion-test instrument aborts when a pattern matches nothing.** 🔴 It was
   **not** committed as a repository script, and that is a deliberate trade recorded rather than
   hidden: adding a governance script to a candidate whose entire remit is one blocking finding
   would expand the object under review. The consequence is that the falsifier is a stated
   procedure and not an executable one, and re-running it depends on the next reader building the
   instrument again. **Carried as a declared debt for whichever candidate next touches the
   protocols' test surface.**

---

## IMPACT

`M-1` is repaired in CONTENT, at the tip that binds, in the file that canonicalizes. The corrected
property is stronger than the sentence it replaces — it is true, it survives the grep that
falsified the original, and it is now falsifiable by a test the file itself specifies.

Nothing else moved. No transport rule, taxonomy, size table, ACK relationship or version-scope
model was touched; `T-TRANSPORT-1` remains `NOT_RUN`; routing remains unresolved and unaddressed;
`M-2` was verified and left to its owner.

The honest account of the two near-misses: one was avoided by reading a suggestion against the
artifact instead of accepting it, and one was caught by an accident of ordering. Only the first was
discipline.

---

## CLASSIFICATION · SCOPE · EVIDENCE

```
CLASSIFICATION   L-1 ORIGINAL_OBSERVATION · L-2 ORIGINAL_OBSERVATION ·
                 L-3 REPLICATION of SLR-mirror-0014, fourth instance, new mechanism
                 ALL PROPOSED — E.2 curation is Mirror's; Plan does not self-ratify

SCOPE            L-1, L-2  offered for wider scope — they concern how properties are encoded and
                           how review output is applied, in any domain
                 L-3       laboratory-internal, and it is Mirror's class, not mine

EVIDENCE         L-1  cross_session_transport.md lines 16 and 424 at f48a807, against the nine
                      name occurrences in the same file; T-GENERIC-1's nine-line result at the
                      revision-2 tree
                 L-2  REV-XPORT-MIRROR-001 §12 suggested wording ("only in citations and
                      measurements") against its own §10 table, which types line 5 as
                      FRAMEWORK RULE, and against manifest §9.1b, which types it as status
                 L-3  `sed -E` with `\b` on darwin substituting 3 of 9 occurrences and printing
                      a two-line diff; the same transform in Python printing nine

REVIEW           L-2 is the entry most worth attacking. An author who reports that the reviewer's
                 suggested sentence was also wrong has an obvious interest in that conclusion, and
                 the finding should be checked against the review's own §10 table rather than
                 taken from me. The check is one table, four lines above the suggestion.
```
