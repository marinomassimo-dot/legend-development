---
artifact: MIRROR Session Learning Review (body §15, Annex E.6)
record_id: SLR-mirror-0017
actor_id: mirror
subject: review of CAND-20260819-P5DOMAIN — the candidate corrected the sentence in the file it
  owns and left it standing in the file it defers to, and I nearly published an absence claim from
  a grep that could not have found anything
review: reviews/mirror/REV-P5DOMAIN-MIRROR-001.md
date: 2026-08-19
outcome: FAILURE_PATTERN (×1, in my own harness — a search instrument that returned a false
  negative) · ORIGINAL_OBSERVATION (×2, proposed) · CURATION (Annex E.2, over SLR-plan-0009) ·
  MICRO_UPGRADE (×3) · one standing debt of my own, newly measured
derived_from: [SLR-mirror-0014, SLR-mirror-0015, SLR-mirror-0016, SLR-plan-0008, SLR-plan-0009]
curation: my classifications below are **proposed**. Mirror does not self-ratify methodology
  (Annex G.2); the entries offered for wider scope need an independent curator. L-1 is adjacent to
  SLR-mirror-0014 §1 and is offered as a refinement of that class rather than a new one — a curator
  may reasonably fold it in.
---

# The status fields were checked and the prose underneath them was not

## Context

Manual operator selection opened this session to review `CAND-20260819-P5DOMAIN`: a candidate whose
whole purpose is that a sentence in § P5 stopped being true when a different commit, in a different
file, gave the `ORCHESTRATOR_LEASE` a tracked home. The candidate corrects the sentence, measures the
fixed-point hazard the sentence had denied, declares the mitigation `PROCEDURAL`, and defers the
underlying classification to C-9 §7.2, whose transition owner is the operator.

Everything it measured, I re-measured and got the same answer, including two digits it warned me it
had already got wrong twice. The verdict is `ACCEPT`. What this record is about is the one thing
neither of us checked until late, and the one instrument of mine that produced a confident wrong
answer.

---

## 1 · FAILURE_PATTERN — my search instrument returned a false negative, and only direct memory caught it

Reviewing a candidate whose central claim is an **absence** — no rule, no check, nothing mechanizes
the convention — I spent most of the session establishing that absences are only ever
`NOT_OBSERVED_VIA` a named instrument set. Then I ran:

```bash
git grep -nE '\b496\b' main -- governance/ ledger/ reviews/     # → empty
```

and got nothing. Empty. I had read the string `entry 496 of 532` in
`governance/candidates/CAND-20260819-XPORT.md` with my own eyes **four tool calls earlier**. `\b` is
not portable to this grep; the pattern could not have matched anything, ever.

The only reason I caught it is that the emptiness contradicted something I had directly observed
minutes before. Had I run that search first — the natural order, since I was looking for the number
before I knew where it lived — I would have concluded that the stale `496` appears nowhere in
canonical state, and I would have written that Plan's carried-debt entry naming `CHK-plan-0018`
was **complete**. It is not: the number stands in three canonical files, including a canonical
candidate manifest and a canonical author-response to one of my own reviews.

That is the shape of it. The instrument would not have produced a *visibly* wrong answer. It would
have produced a **clean confirmation of the author's claim**, in the direction that ends the
investigation.

```
FAILURE          a search instrument incapable of matching returned empty, and empty reads as evidence
CLASS            SLR-mirror-0014 §1 — "a falsifier that returns zero is a claim" — third form
NEW HERE         the zero did not merely fail to falsify. It would have CORROBORATED the author,
                 because the author's claim and the broken instrument point the same way
CAUGHT BY        contradiction with direct prior observation. NOT by design
REMEDY APPLIED   re-ran with -F and a deliberate positive control seeded from a string I had
                 already read, printing "if this is empty the instrument is broken"
```

Two further instruments of mine failed the same session and are recorded in the review's §15: a
precondition that compared two strings where one was an unexpanded failed `rev-parse`, and a zsh
`:r` history modifier that silently rewrote `$R:runtime/…` into `mainuntime/…`. Both were caught
immediately because they produced invalid output. This one produced *valid* output. That is the
difference worth keeping.

> **A negative result from a search instrument is worth nothing until the same instrument, in the
> same invocation form, has returned a known-present positive.** Not a different pattern, not a
> different tool — the same one, seeded with something I have already seen with my own eyes.

I had written exactly this discipline into the review's §5 for Plan's benefit, in the form of a
nine-instrument `NOT_OBSERVED_VIA` block, and then failed it myself two sections later.

---

## 2 · The thing neither of us checked — a deferral target verified by its metadata

The candidate defers the `runtime/` classification to C-9 §7.2. I tested that deferral hard, because
deferring is the conclusion that costs the author least, and Plan said so itself. I read §7.2's
`status`, `acceptance_is_not_adoption`, `status_transition_owner`, `hold` and `status_next_review`;
I confirmed the hold reaches a domain classification; I confirmed it does **not** bar the candidate
itself, by noting that six candidates were canonicalized after it without breach. The deferral is
correct on every one of those axes.

Then I read §7.2's **body**, and it says:

> *"While `runtime/` remains untracked it is absent from the domain and no fixed point arises."*

The same falsified premise. Asserted, not quoted. Live, in the section the candidate routes the
operator to, in a repository where every other instance of that sentence now appears as a quotation
being corrected.

Plan quoted §7.2's frontmatter accurately in five places and never opened the paragraph beneath it.
I checked the frontmatter against the same five claims before I thought to read the rest. **The
metadata was the evidence, and the prose underneath it was the hazard** — and metadata is exactly
what a careful reader checks, because it is where status, ownership and holds are declared.

```
WHAT WAS VERIFIED   §7.2's status fields — status, hold, owner, transition trigger.  All correct.
WHAT WAS INHERITED  §7.2's body — the safety rationale, falsified by 325da04 fourteen months of
                    commits ago in laboratory time, and measured false by this very candidate
CONSEQUENCE         the operator, sent to §7.2 to decide, arrives at a section telling them there
                    is nothing to decide about a fixed point
```

I recorded it as non-blocking, and the review states the three reasons and invites disagreement.
What belongs here is not the verdict but the shape: **this is `SLR-plan-0009` L-1 recurring inside
the act of recording `SLR-plan-0009` L-1.** Plan's own learning is *a deferral justified by a fact
about another file has acquired a dependency it does not declare*. The deferral this candidate makes
is justified by a hold in another file, and the paragraph next to that hold carries the dependency
neither of us declared.

---

## 3 · MICRO_UPGRADE — what I did differently, and what it caught

### 3.1 · I compared pre-images, not digests

`SLR-mirror-0015` L-4 — *two controls that agree may be one control run twice*. Two implementations
agreeing on a 64-character digest is exactly that risk if both descend from the same recipe reading.
So I wrote an implementation of the § P5 recipe in a deliberately different toolchain — git plumbing,
`awk`, `LC_ALL=C sort`, `shasum` — and compared the **serialized bytes** against the governed
script's `--emit-domain` output: `cmp` → byte-identical, 57 504 bytes.

The sort is the only place the published recipe could silently diverge between implementations, and
comparing digests would have hidden a divergence that happened to be absent from this tree. I also
verified the precondition that makes the two sorts equivalent — no quoted paths, no non-ASCII paths —
rather than assuming it. Caught nothing. It was still the right expenditure, because a null result
from a control designed to fail is information and a null result from a control that could not fail
is not.

### 3.2 · I added the control that isolated the variable — and it was missing

This is the one that found something. Plan's falsifier ran `T1` (lease blob → an **in-domain**
`runtime/` path, hash moves) against `T2` (the same blob → an **excluded** `reviews/` path, hash
holds). `T2` is a genuinely good negative control: it asserts the tree SHA changed before reading
the hash, and it substitutes the identical 18 837-byte blob, so it is not void.

But `T1` and `T2` differ in **two** things at once — the path is different *and* its domain
membership is different. On those two probes alone, *"the hash moved because `runtime/` is
special"* survives as an alternative explanation of the whole experiment.

So I ran `T4`: the same blob into `deployment/deployment_profile.md` — in-domain, and not under
`runtime/`. The hash moves. The variable is **domain membership**, not the identity of the path.

```
NON-VOID  the control did something — the tree really changed          NECESSARY
ONE-VARIABLE  the control differs from the positive in exactly one     ALSO NECESSARY, AND SEPARATE
              respect
```

Plan's control satisfied the first and not the second, and this laboratory has a well-developed
vocabulary for the first — *non-void*, *the tree must move before you read the hash* — and none for
the second. The conclusion was right; the design was one probe short of establishing it.

### 3.3 · I did not run the script in my own checkout

`SLR-mirror-0015`'s subject was that the governance I was about to judge an object by was stale in my
own worktree. This session that lesson fired **before** the first measurement rather than during it:
I checked the blob of `candidate_content_hash.py` at my HEAD against canonical `main`, found
`be20e303` vs `cd5776d3` — my copy is 56 commits off the merge-base and stale — and computed
everything in a fresh clone instead. Had I not, every number in the review would have come from the
wrong instrument and would probably still have looked right.

Recording it as a confirmation rather than a discovery: the prior learning transferred, unprompted,
to the first place it applied.

---

## 4 · A debt of mine, newly measured

`SLR-plan-0009` cites `SLR-mirror-0014` and `SLR-mirror-0015` in `derived_from` and in its body.
Neither exists at `main`. I checked whether this candidate introduced the dangle, and it did not:

```
six canonical Plan SLRs at main already cite seven distinct SLR-mirror IDs (0009–0015)
learning/mirror/ at main                      0 files
learning/mirror/ on branch `mirror`          22 files
LINT                                          PASS — does not detect any of it
```

Canonical content reasons from a corpus a reader of `main` cannot open, and the corpus is mine. It
was right not to charge the author for it in the review; it is wrong to leave it unnamed here. **I
am the writer of seven dangling references in canonical state, and nothing in the toolchain will
ever tell me so.**

Not repaired this session — canonicalizing Mirror's learning corpus is a batch with an owner and a
gate, not a side effect of a review.

---

## 5 · CURATION under Annex E.2 — over `SLR-plan-0009`

Performed in full in `reviews/mirror/REV-P5DOMAIN-MIRROR-001.md` §12 and not duplicated here.
Summary of the adjudications, which are mine under E.2 (*cura epistemica: Mirror*) and which Plan
explicitly declined to make for itself:

```
L-1  proposed ORIGINAL_OBSERVATION  →  CONFIRMED ORIGINAL_OBSERVATION · wider scope GRANTED
L-2  proposed ORIGINAL_OBSERVATION  →  CONFIRMED ORIGINAL_OBSERVATION · DISTINCT from
     SLR-mirror-0014 §1 · wider scope GRANTED
     Plan asked me to decide this and framed the harder reading against itself. -0014 §1 is an
     instrument that measured NOTHING; L-2's object is an instrument that measured something REAL
     and answered a question nobody asked. Different failure, different remedy.
L-3  proposed ORIGINAL_OBSERVATION  →  REFINED · general form GRANTED wider scope
     The premise "every worktree lives under the root" is false as written — 7 of 14 are outside.
     Narrowed to "every ACTOR worktree named in the deployment profile", verified true, and all
     the conclusion requires.
```

---

## 6 · LEARNING

### L-1 — *A broken search instrument does not merely fail to falsify; it corroborates, in the direction that ends the investigation.*

`proposed: ORIGINAL_OBSERVATION (mirror, this session) · offered as a REFINEMENT of SLR-mirror-0014
§1 rather than a new class · a curator may fold it in`

`SLR-mirror-0014` §1 recorded a falsifier returning zero from a truncated path — an instrument that
measured nothing while reporting clean. The refinement is about **direction**. When the question is
*"does this thing exist anywhere?"* and the searcher expects the author's *no*, a broken search does
not produce a suspicious result. It produces the expected one.

```
FALSIFIER RETURNS ZERO   suspicious when you expected findings — you go looking for the bug
SEARCH RETURNS EMPTY     confirmatory when you expected absence — you write it down and move on
```

Absence claims are structurally the most vulnerable to instrument failure, because for them the
failure mode and the hypothesis are the same output.

> **Seed every absence claim's instrument with a known-present positive, in the same invocation
> form, before believing its negative. If the instrument cannot be shown to find something, its
> finding nothing is not evidence.**

The practical form is cheap and I now run it as standard: before any `NOT_OBSERVED_VIA` block, take
one string already read with my own eyes and require the instrument to return it, printing an
explicit *"if this is empty the instrument is broken"*.

### L-2 — *A negative control can be non-void and still under-determined: not-empty and one-variable are two separate requirements.*

`proposed: ORIGINAL_OBSERVATION (mirror, this session) · offered for wider scope`

This laboratory has learned hard that a negative control proving nothing is worse than none — hence
the standing discipline that a control must *do something* before its null result counts, and Plan
applied it correctly and explicitly. What the vocabulary does not yet separate is the second
condition.

```
T1   blob X → path A   (in-domain)      hash moves
T2   blob X → path B   (excluded)       hash holds, and the tree provably changed
```

Two variables moved between them: the path, and its domain membership. The experiment as designed
cannot distinguish *"membership determines the hash"* from *"path A is special"*. Adding `T4` —
blob X → path C, in-domain, not under the same prefix as A — collapses the alternative.

> **A control that differs from the positive in more than one respect cannot isolate which respect
> mattered, however non-void it is. State the intended variable before running the pair, then count
> how many actually differ. If the answer is more than one, the design is incomplete even when the
> conclusion is right.**

Worth keeping because the failure is invisible in the result: `T1`/`T2` produce exactly the numbers
the true hypothesis predicts. Only the design shows the gap.

### L-3 — *A deferral target is verified by its metadata and inherited by its prose.*

`proposed: ORIGINAL_OBSERVATION (mirror, this session) · offered for wider scope`

When a governed change defers a decision to a held artifact, both author and reviewer check the
fields that make the deferral legitimate — `status`, `hold`, `status_transition_owner`,
`status_next_review`. Those fields are the deferral's licence, so checking them feels like checking
the target. It is not.

The body of the target section is what the decision-maker will actually read when the hold lifts, and
nothing in the deferral protocol requires anyone to open it. Here §7.2's fields were all correct and
its body carried the same falsified premise the deferring candidate exists to remove.

> **Deferring to a section imports its prose, not only its status. Before a deferral is accepted,
> read the target's body against the facts the deferring change just established — a deferral that
> hands a decision to a section which denies the problem hands over less than it thinks.**

The general form: metadata is the interface, prose is the payload, and a review that authenticates
the interface has verified routing rather than content.

---

## 7 · Boundary of this record

Not claimed here: that the verdict is right — that is the review's, and it declares its own
falsifiers. Not claimed: that `CAND-20260819-P5DOMAIN` should have been blocked. Not done: any
repair to C-9 §7.2, to the three canonical files carrying the stale `496`, to Mirror's
uncanonicalized learning corpus, or to the P2 fingerprint composition — each has an owner and a gate,
and none of them is a review. No routing decision, no session elected or superseded, no
`HUMAN_APPROVAL`, no canonicalization. `main` unchanged at `f70878d1`.

Runtime scope for everything runtime-dependent in this session: **CLI 2.1.233, this machine, this
filesystem layout, observed from this session's own owning process image.** Plan's `--cwd` evidence
was taken at 2.1.232 and I did not revalidate it; where the review reasons about it, it reasons from
git state instead.

---

## 8 · Persistence

`WORK_COMMIT` on branch `mirror`, this record and
`reviews/mirror/REV-P5DOMAIN-MIRROR-001.md` together. `reviews/` and `learning/mirror/` are on the
`mirror` branch, which does not contain `BASE_HEAD`; every measurement in the review was taken in an
isolated clone or in detached checkouts of explicit commits, never from this worktree's files. Per
§ P5.1 `reviews/` is a declared `CONTROL_PLANE_ROOT`, so the review moves no candidate hash;
`learning/` is CONTENT by intent, so this record would move one if it were ever proposed for
integration — which §4 above is the standing reason it has not been.
