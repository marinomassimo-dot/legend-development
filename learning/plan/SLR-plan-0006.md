---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0006
actor_id: plan
role: Plan
date: 2026-08-19
task: SCIENTIST-AB-SPEC-001 · directive v1 · generation 6 — targeted remediation of
  REV-SCIAB-MIRROR-005 (M-5) on CAND-20260818-SCIENTIST-AB-SPEC
scope: this candidate's revision 6, and one sentence in §4.4 about where a rule came from
curation: PENDING — E.2 gives epistemic curation to Mirror. Every class below is **proposed**,
  not self-certified. L-1 is offered as a REPLICATION of `REV-SCIAB-MIRROR-005` §4C and of the
  REFINED_FORMULATION Mirror attached to `SLR-plan-0005` L-2, both read at source before this
  remediation began.
derived_from: [SLR-plan-0004, SLR-plan-0005, SLR-mirror-0012, SLR-mirror-0013]
---

# SLR-plan-0006 — the rule was right, and I wrote down the wrong reason for having authority over it

## Context

One blocking finding, and it moves no byte of behaviour. `REV-SCIAB-MIRROR-005` confirmed `M-4`
closed in both modes, measured against an independent `os.walk` universe with a passing instrument
check, and confirmed `M-1`, `M-2` and `M-3` closed from `R-1`. Then it went at the section
revision 5 **added** to justify the one new rule inside that remedy, and found the heading false:

> **Why the one asymmetry, derived and not chosen.**

I reproduced the finding before editing anything, from the sources rather than from the review.
§2.2 makes Plan the surface's only writer until handover; §3 forbids patching a failed surface;
§1's `P-7` authorizes the blind first pass only when `verify` is satisfied; §2.3 records the
ex-ante blinding greps. Written out as a derivation, those premises reach exactly this far: **a
`PASS` over an `undecodable_text` file pre-handover would assert a guarantee the run cannot
support.** They do not reach the next step. Two contracts discharge that conclusion —

```
(a) BLOCK      rc=1, the surface is rebuilt from the spec          — what this protocol does
(b) ENUMERATE  PASS, named under [UNCHECKED] as EXPECTED_BY_PROTOCOL NO, counted apart,
               and the pre-handover GUARANTEE_PROVIDED row narrowed to say so
```

— and **(b) is what the same tool already does post-read with the same class.** Nothing in §1,
§2.2, §2.3, §3 or §4.3 selects between them. I checked the one branch that could have made it an
entailment, Mirror's own `WHAT_WOULD_CHANGE_MY_MIND`: a clause under which an
unanticipated-but-allowlisted artifact must make the command exit non-zero rather than be
enumerated. There is none, at `BASE_HEAD` or at revisions 1–4. `M-5` is confirmed on my own
reading, not adopted on the reviewer's.

---

## L-1 · FAILURE_PATTERN — I argued for the authority I had by claiming I had not used it

`CONFIRMATION_CLASS: REPLICATION` of `REV-SCIAB-MIRROR-005` §4C and of Mirror's
REFINED_FORMULATION on `SLR-plan-0005` L-2 (mirror, this review; read at source on branch
`mirror` before this remediation began) · `CLASS: FAILURE_PATTERN` ·
`SCOPE: LOCAL → offered for wider scope` · `STATUS: proposed`

I had the authority to make this rule. H.1 gives *integrazione strutturale / candidate* to Plan,
the protocol is not canonical at `BASE_HEAD`, no prior durable rule was being overridden, the rule
was declared ex ante in three places, and the implementation matches all three. Mirror checked
every one of those and passed them: **PLAN AUTHORITY FOR CHANGE: PASS.**

And having that authority, I wrote a heading that said the decision had not been made.

The mechanism is worth naming precisely, because it is not dishonesty and it is not carelessness.
I had just refused the cheap remedy — scoping the printed sentence — on the grounds that it would
**weaken a guarantee the code could already meet**, and I was right to. But refusing a weakening
felt like *declining to choose* rather than *choosing the stricter of two contracts*. A
fail-closed option presents itself as the absence of a decision: it looks like what you get when
you simply do not weaken anything. So the strictness got written up as an inheritance from §2.2
instead of as the selection it was, and the sentence that would have exposed it — *the alternative
was (b), and I refused it* — was written twice, in §4.0aaa of the manifest and in `SLR-plan-0005`
L-2, in **both** places about the remedy rather than about the blocking level, and in neither
place inside the protocol.

That last part is the part that made it blocking rather than untidy. §4.4 is content and
canonicalizes; the manifest is control plane and does not. A reader of the canonical protocol has
§4.4 alone, and §4.4 alone told them there was nothing here to decide — at the one point in the
document where the decision is the operator's under H.1.

**The generalisation:** *a fail-closed choice is still a choice, and it is the kind most likely to
be written up as an entailment, because refusing to weaken something feels like not having
decided. When a normative text argues that a rule is right, check separately whether it also
claims the rule was unavoidable — those are two claims, and the second is the one that quietly
removes an approver from the loop.*

---

## L-2 · MICRO_UPGRADE — a derivation that ends in a disjunction has not ended

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (plan, this session) · `CLASS: MICRO_UPGRADE` ·
`SCOPE: LOCAL` · `STATUS: proposed`

`SLR-plan-0005` L-2 proposed: *when one mechanism runs at two points of a transfer of authorship,
write its contract once per point before deciding anything about either.* I did that, and §4.4 is
the artifact. Writing the two contracts out **did** answer the question I had been about to answer
by analogy — whether the class blocks. What it did not do, and what I assumed it did, is tell me
**how hard**.

The check that would have caught it is mechanical and costs nothing. Write the derivation out with
its premises numbered, as I did in §4A of the reproduction, and then read only the **last** line:

```
I4   a PASS in that state asserts a guarantee the run cannot support
C    therefore rc=1
```

`I4` is a statement about what cannot be *said*. `C` is a statement about what the process must
*do*. Nothing carries one to the other, and the shape that hides it is that `I4` genuinely
eliminates the *permissive* reading — so the argument feels finished at exactly the point where
two options remain. **A derivation whose last inference eliminates one option out of three has not
selected among the remaining two**, and the give-away is that the conclusion introduces a
vocabulary the premises never used: the premises are about assertability, the conclusion is about
an exit code.

**The rule I am proposing:** *when a normative text concludes in a mechanism — an exit code, a
refusal, a gate — check that the premises above it are in the same vocabulary. If the derivation
speaks of what can be claimed and the conclusion speaks of what the machine does, there is an
unstated step, and it is a policy choice. Name it, state the alternative, and say who approves
it.*

---

## L-3 · MICRO_UPGRADE — the same sentence was in four artifacts, and the review named one

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (plan, this session) · `CLASS: MICRO_UPGRADE` ·
`SCOPE: LOCAL` · `STATUS: proposed`

`M-5` is written against `§4.4`. I searched the revision-5 content population for the claim rather
than for the string, and it was in **four** operative places:

```
controlled_benchmark_ab.md §4.4      "Why the one asymmetry, derived and not chosen"
benchmark_input_surface.py  ~L596    "the asymmetry is derived rather than chosen", in the
                                     comment directly above the branch that implements it
test_benchmark_input_surface.py      the hostile-case docstring: "...so a text-suffixed file
                                     that is not text is a state build cannot produce ...
                                     It is a FINDING, and rc=1" — the same jump, no keyword
surface_spec.json content_scan/_note "See controlled_benchmark_ab.md 4.4 for the derivation,
                                     which is 2.2's single-writer rule" — and it drops the
                                     source-root branch entirely, so it is false twice
```

Three of the four would have survived a grep for *"derived and not chosen"*. The spec note is
worse than §4.4, not milder: §4.4 at least names both disjuncts of `I1` before refuting one, while
the note asserts flatly that `build` cannot produce the state — which is false if the source root
carries such a file, since `build` would copy it faithfully. **The most degraded copy of a claim
is the one furthest from the review that found it**, because it is the one nobody re-derived when
they wrote it down.

This is `SLR-plan-0004` L-2 arriving at the level of prose: that record's lesson was that one rule
implemented twice will diverge, and the repair was a shared predicate. There is no shared
predicate for a justification. The only instrument is to treat *the population of a normative
claim* the way `SLR-plan-0004` L-1 taught me to treat the population of a finding — **the finding
names one site and is a lower bound on the sites**, and the search has to be for the claim's
meaning, in the artifacts a reader would reach for, not for its wording.

---

## What this session did not do

**No executable byte moved, and it is measured rather than asserted.** All **51** top-level
definitions of `benchmark_input_surface.py` are identical by `ast.dump` at revision 5 and
revision 6 — comments are not in the parse tree — and identical again with docstrings stripped.
For `test_benchmark_input_surface.py`, **40 of 40** definitions are identical with docstrings
stripped; the single class that differs by `ast.dump` is `HandoverGateCensusTests`, which is
exactly where the docstring was edited, and a docstring is not an assertion. `surface_spec.json`
differs at **one** key by structural comparison — `content_scan/_note` — which no code reads and
no test asserts. The four `verify` runs that matter produce **byte-identical output** at both
revisions: pre-handover clean `rc=0`, post-read clean `rc=0`, the UTF-16 hostile case `rc=1` with
`UNANTICIPATED` in both surfaces, and the same case post-read `rc=0`. The suite is **83/83** at
both. `freeze` and `verify-freeze` pass at both tips and the mutation control refuses.

I did **not** fix `P-4`, `P-6` or `N-7`, and this remediation closes none of them. `N-7` is
unreconciled for the fifth review running; I did not re-run revision 1's tool and I make no claim
about it. I did not touch `SLR-plan-0005`: its L-2 carries the formulation Mirror superseded and
refined, and it is the durable record of what I reasoned at revision 5 — curating it is E.2 work
and Mirror's, and rewriting it would be erasing the evidence for `M-5` from the branch that
carries `M-5`'s repair. I corrected `P-9`'s stale manifest cells and `P-10`'s tests-executed row
because both are currently-false statements in the artifact the operator reads to approve; those
are control plane and move no hash. I did not implement the session-routing debt, register any
actor, execute the benchmark, or touch `main`.

## Boundary of this record

The delta harness is **still not committed** — declared at `SLR-plan-0003` L-4 and unrepaired for
the fourth consecutive revision; the numbers here are reproducible only by re-authoring an
equivalent instrument, which is what I did and what Mirror did. My instrument's first target list
was built by regex over `run_release_regressions.py` and returned **63/62** targets against the
true **65/64**: two entries are split across lines as implicit string concatenation and the regex
saw neither. Reading the `TESTS` tuple by AST returns the right list, and the error was caught
only because Mirror had published 65/64 — the fourth session running in which one of my
instruments was wrong in a way that looked clean, and the second in which another actor's
published number is what caught it. That family is `SLR-plan-0005` L-3, `CONFIRMATION_CLASS:
REPLICATION` added here on a new form: **the target list, not the result**. Three regression
targets remain custom harnesses with no test-id granularity and are recorded apart, `rc=0` at both
tips, never counted as passes. No `LEARNING_INDEX` exists to dedup against; that debt is Plan's,
it is five reviews old, and dedup was again done by reading records at source. No `SESSION_REF`
was declared or inferred. Nothing under `main`, the root checkout or another actor's worktree was
written; `REV-SCIAB-MIRROR-005` and `SLR-mirror-0013` were read from git objects on branch
`mirror` without merging it. The session guard refused one inline heredoc that would have run a
write while the shell was inside a repository worktree; I did not reach for an unchecked tool —
the probe was authored with `Write` into the scratchpad and invoked by name, and the measurement
is the same one.

## Persistence

`WORK_COMMIT` on branch `scientist-ab-spec`, under `learning/plan/` (E.6, A.7). `learning/` is
CONTENT by intent (P5.1), so this record is inside the population Mirror reviews and moves the
candidate hash. It is committed **before** any revision-6 binding is declared, so nothing is
superseded within the revision — held for a third consecutive revision.
