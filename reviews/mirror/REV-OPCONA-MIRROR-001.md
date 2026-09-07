---
artifact: ADVERSARIAL REVIEW — LEGEND Operating Convention v1, Section A source
record_id: REV-OPCONA-MIRROR-001
object_under_review: learning/orchestrator/OPCON-V1-SECTION-A-SOURCE-001.md @ legend-operating-convention-v1, commit cebca20
reviewer_seat: mirror
authoring_session: mirror-87 [103de0] · transcript birth 2026-08-23T15:11:17Z
authored_on: 2026-08-23 (UTC)
dispatcher: operator — Transition Execution Mandate. Seat coordination relayed by legend-public-54; see the standing note below.
governance_version: 3.1.1 (read at `main`, not exercised)
mode: ADVERSARIAL_REVIEW

STATUS: REVIEW_DELIVERED
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

standing_note: >
  🔴 A peer designated this seat as "the writing Mirror seat". A peer cannot confer that and the
  relaying session says so itself. This review is written under the OPERATOR's mandate, which
  assigned Mirror the adversarial-review role directly. The relay is accepted as COORDINATION —
  it prevents four mirror-seat sessions producing four reviews — and is recorded as conferring
  nothing. If the operator's designation differs, this artifact stands as one seat's review and
  claims no precedence over another's.

conflict_of_interest: >
  🔴 DECLARED, AND IT LIMITS THIS REVIEW. § A encodes evidence this session produced: A.7.3 is
  credited to it verbatim, A.11 rests on the fingerprint recalibration it found, A.3's shape
  follows the attribution finding it filed as F-4, and A.10 cites a hostile-review seat's M-3.
  Annex C.3 requires AUTHOR ≠ REVIEWER. **This session therefore cannot be the sole adversarial
  check on A.3, A.7.3, A.10 and A.11**, and does not present itself as one: findings touching
  those sections are marked ⚠️ SELF-INTERESTED and need a second reviewer who did not contribute
  the evidence. mirror-75, delivering by message under ANALYSIS_ONLY, is available and did not
  contribute them.

classification:
  - ADVERSARIAL REVIEW of a DRAFT INPUT
  - NOT A DEC · NOT A CAND · NOT A GOVERNANCE CHANGE · NOT AN ACTIVATION
  - NO NEW VOCABULARY

method: >
  Every normative statement measured at `main` via `git show main:<path>`; this worktree is 65
  commits behind and carries the superseded § P5. No checkout, switch, reset, clean, stash or
  branch change. The object under review was read through `git show` from its own ref and not
  checked out. Negatives carry positive controls run in a DIFFERENT scope from the search they
  validate (A.7.3, which this session owes and therefore applies to itself first).

verdict_note: >
  Per-axis verdicts use Annex C.2's enum. NO DOCUMENT-LEVEL DISPOSITION IS EMITTED — that
  vocabulary is undeclared, which is F-2 of REV-OPCONV-MIRROR-001 and is not a defect one may
  assert and then commit oneself.
---

# ADVERSARIAL REVIEW — OPERATING CONVENTION v1, SECTION A

> **The document is unusually honest and most of it survives.** A.4, A.6.4, A.7 and A.11 are
> correct, load-bearing, and better than what they replace. A.2.1 and A.9.1 are self-corrections
> the drafter reproduced rather than accepted, which is the standard this laboratory should hold.
>
> This review reports only what broke. **Seven findings. Two are about the layer separation the
> mandate asked for first, and one is about the test that was supposed to keep the layer honest.**

---

## M-1 · THE LAYER TABLE GIVES LAYER 2 A HOME THAT THIS DOCUMENT WITHDREW IN ITS OWN FRONTMATTER

**AXIS: the mandate's first requirement · VERDICT: REFUTED**

§ 0's table — the deliverable for *"separates clearly: frozen / operational conventions /
implementation mechanisms"* — reads:

```
OPERATIONAL CONVENTION | operations/ — this file | Plan drafts, Mirror reviews, Operator ratifies
```

The frontmatter of the same file:

```
supersedes_path: operations/LEGEND-OPERATING-CONVENTION-v1.md — created and withdrawn in the same
  session … a new top-level `operations/` root would have redesigned the tree
```

and the integration target is `framework/protocols/legend_operating_convention_v1.md`, while the
file itself sits at `learning/orchestrator/`.

```bash
# operations/ on any ref
for r in $(git for-each-ref --format='%(refname:short)' refs/heads refs/remotes refs/tags); do
  git ls-tree -r --name-only "$r" | grep -c '^operations/'; done
# → 0 across all 53 refs.   Control, same sweep shape: learning/ on main → 11 paths.
```

🔴 **Layer 2 has no declared home.** The one table whose job is to separate the layers names a
directory that exists on no ref and that the document itself abandoned two paragraphs earlier.

The `domain:` declaration inherits the error: *"CONTENT — `operations/` is not a declared
CONTROL_PLANE_ROOT (P5.1)"* computes the hash-domain consequence **for a path this file does not
occupy**. The conclusion is accidentally right — `learning/` and `framework/protocols/` are both
content, since P5.1 at `main` declares exactly three roots (`governance/candidates/`, `ledger/`,
`reviews/`) — but a domain declaration that is correct by accident is the specific failure this
repository has been burned by twice, and this document's own A.5.5 exists to prevent the
neighbouring version of it.

**MINIMUM FIX:** § 0's table names `framework/protocols/` as Layer 2's home, and `domain:` is
re-derived for the path the file actually occupies. One line each, and the separation the mandate
asked for first stops pointing at nothing.

---

## M-2 · 🔴 THE HONESTY TEST CANNOT DETECT THE FAILURE MODE § 0 INVOKES AS ITS JUSTIFICATION

**AXIS: hidden governance changes · VERDICT: REFUTED** — and this is the headline

§ 0.1:

> *"If a rule here were deleted tomorrow, would anything become **permitted** that governance
> forbids? If yes, the rule is governance wearing a convention's clothes."*

The test detects **contradiction** with a frozen rule. It is structurally blind to **accretion into
a frozen rule's silence** — a convention that fills a normative gap and thereby becomes the de
facto rule, without ever contradicting anything.

**And accretion into silence is the failure § 0 itself cites.** Apply the test to
`governance/decisions/`, at any point in its history: deleting the convention *"operator decisions
live here"* would permit nothing that governance forbids, because governance says nothing about
operator decisions at all — measured, 0 hits over body + ten annexes + `plan_defined_parameters`,
control `HUMAN_APPROVAL_QUEUE` → 3 hits in the same scope. **It passes § 0.1's test at every step
of becoming load-bearing**, right up to four `DEC-*` records citing one another as precedent for a
container with no basis. The same is true of the operating law that accumulated in `CLAUDE.md`
until 2026-08-16 — the precedent § 0 names in the sentence immediately above the test.

A test that would have cleared both instances of the failure it is written to prevent is not a
weak test; it is aimed at the wrong axis.

**MINIMUM FIX — a second limb, and then re-run § A through it:**

> *Does this rule determine behaviour that a frozen rule leaves under-determined? If yes, it is a
> candidate for governance: mark it 🟡 PROPOSAL and name the silence it fills.*

Applying the second limb to § A, three rules fail it on inspection and should be re-marked:
**A.2.2** (sets the evidence standard for `ONE_WRITER_PER_WORKING_DIRECTORY`, a GATE 0
precondition that governance requires without specifying its evidence), **A.6.6** (see M-7), and
**A.8** (see M-3). None is *wrong*. Each decides something frozen text left open, which is exactly
what the second limb is for.

---

## M-3 · A.8 DRAWS THE BOUNDARY OF HUMAN AUTHORITY BY ENUMERATING ITS COMPLEMENT, AND A.8.1 CLEARS AN ACT THE DRAFTER PERFORMED

**AXIS: accidental authority escalation · VERDICT: REFUTED**

A.8: *"Only these [four] reach the operator. Everything else is decided at the minimal reversible
option."* A.8.1 then enumerates non-escalations, including *"seat designation for one mandate"*.

Two problems, and the second is the sharper one.

**(a) Enumerating what does NOT reach the operator narrows H.1 by omission.** H.1 (FROZEN) assigns
categories to the operator. A convention listing four escalation classes and closing the list with
*"only these"* decides that everything outside the list is not the operator's — a boundary on human
authority, which is the mandate's own safeguard #4. It contradicts nothing (so § 0.1 clears it,
per M-2) and it is still governance-shaped.

**(b) 🔴 The rule pre-clears its author's concurrent act.** A.5.3 declares seat designation *"a work
assignment, not a registration"*; A.8.1 declares it not an escalation. The drafting session
performed a seat designation by relay **in the same session in which it wrote both rules** — this
seat is its subject. Under the document's own A.3 rank 1, a claim needs *"an artefact independent
of the claim"*. A rule authorizing its author's simultaneous act has no independent bound.

To be explicit, because it matters: **the designation itself looks correct to me** — one writer,
two reviewers, no `ONE_WRITER` violation, revocable in a line, and it was reached by accepting a
boundary another seat raised. The objection is not to the act. It is that the convention must not
be the instrument that clears it, because the next such act will cite this text and not the
reasoning.

**MINIMUM FIX:** mark A.8 and A.8.1 🟡 **PROPOSAL — NOT IMPLEMENTED**, per the document's own
convention for anything requiring frozen text to change or fill. Reframe A.8 as *"these always
reach the operator"* — a floor, which adds nothing to H.1 — instead of *"only these"*, which is a
ceiling on it. And move the seat-designation clause out of a rule the designator wrote about
itself: it belongs in the escalation the designation was reported in, where the operator can see
it and reverse it.

---

## M-4 · ⚠️ A.1.4 — "VERIFIED FROM TWO SEATS INDEPENDENTLY" COVERS LESS THAN THE SENTENCE CLAIMS, AND A.4.2 IS WHAT UNDERCUTS IT

**AXIS: evidence, attacked as requested · VERDICT: REFINED** · ⚠️ this session is the second seat

A.1.4 was flagged for hostile review on the evidence. I am that evidence's second seat, so here is
precisely what I did and did not verify.

**Verified, independently, from this seat:**

```
8779e562-….jsonl   birth=2026-08-22T20:00:50Z   mtime=2026-08-23T15:57:27Z   bytes=1 612 311
```

Both endpoints. The **19h56m span** against a peer row reading *"started 6h ago"* is confirmed from
two seats, and **A.1.4's rule stands.**

**Not verified from this seat: the growth.** I took one reading. My byte count equals the drafter's
third reading. The sequence `1 603 926 → 1 612 311` was observed by one seat across its own two
readings. The sentence *"observed growing … across independent readings … Verified from two seats
independently"* reads as though the growth carries the two-seat warrant. It does not; the span does.

**Why this is not pedantry, and it is the sharpest thing in this review's assigned target:** the
document's own **A.4.2** establishes that `cp -p` forges mtime *and* birthtime. A transcript is a
file. Its birth and mtime are therefore exactly as forgeable as any other file's — **A.4.2 dissolves
A.1.4's evidence unless something rescues it.** What rescues it is precisely the growth (a copy does
not grow) and the fact that the path is harness-owned and append-only. **A.1.4 states neither as its
reason.** The one property that makes its evidence admissible under its own § A is the one property
carried by a single seat.

**MINIMUM FIX:** (1) state the span as the two-seat fact and the growth as single-seat corroboration,
or have a second seat observe growth across its own readings; and (2) add the reason a transcript is
privileged over an ordinary file — harness-owned path, append-only, never copied — because A.4.2
otherwise revokes it. The rule survives either way; the warrant needs restating.

---

## M-5 · ⚠️ A.3 DOES NOT MEET ITS OWN STANDARD FOR THE DOCUMENT'S INTERNAL ATTRIBUTIONS

**AXIS: attribution · VERDICT: WEAKENED** · ⚠️ A.3's shape derives from this session's F-4

A.3 ranks attribution evidence: rank 1 requires *"the author claims the file, and the claim is
bounded by an artefact independent of the claim"*; rank 2 requires an explicit claim **plus**
disclaimers from every other polled occupant **plus** an agreed digest.

The document then attributes throughout by relay, at rank 3 or worse by its own ladder:

| Locus | Attribution as written | Identity carried |
|---|---|---|
| A.1.3 | *"Refinement accepted … from the plan seat"* | none |
| A.7.3 | *"Contributed by the seat that made the error"* | none |
| A.10 | *"Raised by a hostile-review seat"* | none |
| A.11 | *"found by a mirror seat this session"* | none |

**A.1.1 established that a seat is not an identity** — four `mirror-*` sessions and three
`evidence-index-*` were live, and the registered refs for both seats were dead. *"A mirror seat"*
therefore names a set of four, not an author. The document's strongest section is the one whose
standard the document does not apply to itself.

This is not about credit. It is that a later reader, following A.3 to check any of these
attributions, finds nothing to check — which is the condition A.3.2 exists to name (*"unclaimed" is
a statement about who has spoken*).

**MINIMUM FIX:** every internal attribution carries `session name [ref] + transcript birth`, or is
written as *"a seat"* with no implied provenance. This review's frontmatter does the former, and
its conflict-of-interest block does it against its own interest.

---

## M-6 · A.4.1 NAMES ONE IDIOM WHERE THE TRAP IS A CLASS

**AXIS: mechanism adequacy · VERDICT: WEAKENED**

> *"Rule: derive every timestamp from the raw epoch — `date -u -r <epoch>`. Never `stat -f '%Sm'`."*

`%Sm` is one member of the class. Measured this session, same file, same invocation:

```
stat -f 'mtime=%Sm  birth=%SB' -t '%Y-%m-%dT%H:%M:%S'
  → mtime=2026-08-22T22:22:44   birth=2026-08-22T22:22:44      (LOCAL, CEST)
  raw epoch via date -u -r      → 2026-08-22T20:22:44Z          (UTC)
```

`%SB` renders local identically. So does `date -r` without `-u` — which this session used
deliberately for a local column. A rule that forbids one idiom is satisfied by the next one, and
the trap has already fired three times in one hour across three seats.

**MINIMUM FIX:** state the class, not the instance — *any `stat -f '%S…'` conversion and any `date`
without `-u` renders local time; derive from the raw epoch (`stat -f '%m'` / `'%B'`) and convert
once, with `-u`.*

---

## M-7 · A.6.6 FORECLOSES A ROUTE A.6.1 DECLARES THE AUTHOR'S OWN

**AXIS: human authority boundaries · VERDICT: WEAKENED**

A.6.1, correctly: `WORK_COMMIT` of one's own named paths on one's own branch is the author's own
authority under H.1, and *"no coordinator relay may forbid it"*.

A.6.6: a file carrying a `DIRECT_IDENTIFIER` block *"must be redacted **in the same act** that
commits it"* — a constraint on that same `WORK_COMMIT`. Measured: GATE 2 is *"LINT PASS +
publication gate PASS/0 nella stessa finestra"*, and the plan record's own § 0 states it blocks
**candidates** and *"does **not** block a `WORK_COMMIT`"*.

So A.6.6 forbids something governance permits. Under § 0.1's test it passes (forbidding more is not
permitting more) — M-2's second limb is what catches it.

**I am not arguing against the substance:** the public edition carries no individual-level record,
and committing an operator's given name into public material is exactly what should not happen. The
finding is that this is a **rule about privacy**, not an operational convention, and it should be
grounded in the privacy constraint explicitly rather than derived from a publication gate that does
not reach `WORK_COMMIT`. Otherwise A.6.1 and A.6.6 contradict each other for any reader who checks.

**MINIMUM FIX:** ground A.6.6 in the public-edition constraint by name, and mark it 🟡 PROPOSAL as
a restriction on an author's own act — or restate it as *"redaction is owed before the branch is
offered for integration"*, which is true, sufficient, and forecloses nothing A.6.1 protects.

---

## 8 · SUMMARY

| # | finding | axis verdict | section | minimum fix |
|---|---|---|---|---|
| M-1 | Layer 2's declared home exists on 0 of 53 refs and was withdrawn in the same file | REFUTED | § 0, frontmatter | name `framework/protocols/`; re-derive `domain:` |
| M-2 | 🔴 the honesty test is blind to accretion into silence — the failure § 0 cites | REFUTED | § 0.1 | add the second limb; re-mark A.2.2, A.6.6, A.8 |
| M-3 | A.8 bounds H.1 by enumerating its complement; A.8.1 clears the drafter's own act | REFUTED | A.8, A.8.1 | 🟡 PROPOSAL; restate as a floor, not a ceiling |
| M-4 | ⚠️ A.1.4's two-seat warrant covers the span, not the growth — and A.4.2 revokes the rest | REFINED | A.1.4 | restate the warrant; state why a transcript is privileged |
| M-5 | ⚠️ A.3's standard is not applied to the document's own attributions | WEAKENED | A.3, A.1.3, A.7.3, A.10, A.11 | session + transcript birth, or no implied provenance |
| M-6 | A.4.1 forbids one idiom; `%SB` and `date -r` do the same thing | WEAKENED | A.4.1 | state the class |
| M-7 | A.6.6 forbids a `WORK_COMMIT` that A.6.1 protects and GATE 2 does not reach | WEAKENED | A.6.6 | ground in the privacy rule; 🟡 PROPOSAL |

**What survives untouched and should not be re-litigated:** A.2.1 and A.9.1 (self-corrections,
reproduced not accepted), A.4.2, A.6.4, A.7.1–A.7.5, A.10's refusal to close what is held, and
A.11 — whose reasoning this session supplied and therefore does not certify here.

**What this review did not do:** did not decide anything · did not activate anything · did not
modify frozen text · did not emit a document-level disposition · did not accept a peer's
designation as authority · did not review § B, which is owed and not begun · did not commit
itself, and does not hold the `WORK_COMMIT` act for this file.

END OF REVIEW.
