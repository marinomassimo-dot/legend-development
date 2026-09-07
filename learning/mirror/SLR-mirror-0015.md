---
artifact: MIRROR Session Learning Review (body §15, Annex E.6)
record_id: SLR-mirror-0015
actor_id: mirror
subject: review of CAND-20260819-XPORT — the protocol's revalidation rule fired on me before I
  had read it, and the governance I was about to judge it by was stale in my own checkout
review: reviews/mirror/REV-XPORT-MIRROR-001.md
date: 2026-08-19
outcome: FAILURE_PATTERN (×2, both in my own harness — one of them the third form of a class I
  recorded at -0014) · ORIGINAL_OBSERVATION (×2, proposed) · CURATION (Annex E.2, over
  SLR-plan-0007) · MICRO_UPGRADE (×2)
derived_from: [SLR-mirror-0011, SLR-mirror-0012, SLR-mirror-0013, SLR-mirror-0014,
  SLR-plan-0005, SLR-plan-0006, SLR-plan-0007]
curation: my classifications below are **proposed**. Mirror does not self-ratify methodology
  (Annex G.2); the entries offered for wider scope need an independent curator.
---

# I was the endpoint the protocol was written about, and I nearly reviewed it against the wrong constitution

## Context

Manual operator selection opened this session to review `CAND-20260819-XPORT` — a transport
protocol built on a harness probe that had just discovered the machine hosts multiple runtimes and
that `plan` and `mirror` each have many live sessions. The review was scoped to transport, with
routing explicitly out of bounds.

Two things happened before I had finished reading the object, and both changed how the review ran.

---

## PROBLEMS

### 1 · The candidate's version-bound guarantees did not apply to me, and I found out by looking

Every runtime guarantee in the candidate is bound to `VERSION_OBSERVED: 2.1.232`. My own session
runs **2.1.233** — read from my parent process image, not from `claude --version`, which reports
2.1.232 and resolves to a third binary hosting no session at all.

So the protocol's `OBSERVED → VERSION_CHANGED → REVALIDATION_REQUIRED` fired on its first reader.
Had I inherited the candidate's measurements instead of observing my own runtime, I would have
written a review asserting version-bound facts that were, for my endpoint, **unmeasured**.

### 2 · The governance in my own worktree was not the governance the candidate binds to

My branch has diverged from canonical `main`. My checkout carried
`CANDIDATE_HASH_VERSION: legend-candidate-v3` with `CONTROL_PLANE_ROOTS` lacking `reviews/`;
canonical `main` carries **v4**, with `reviews/` declared.

Read from my checkout, `reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md` is **content** — and the
candidate's binding invariance across its control-plane commits is **false**. I was one command
away from publishing that as a blocking finding. It would have been wrong, and it would have been
wrong in the most expensive direction: a reviewer's false positive against a correct binding costs
the author a revision cycle and teaches the laboratory to distrust the check.

### 3 · Two wrong-reason events, both mine, both in the instrument rather than the object

```
(a) NEGATIVE CONTROL THAT WAS NOT ONE
    I ran two "independent" wrong-base controls: base cbce3016, then base main^.
    main^ IS cbce3016. One input, run twice, agreeing with itself.
    Caught only because two supposedly independent controls returned the identical digest —
    the agreement was the symptom, and I had been about to read it as corroboration.

(b) A GREEN RUN THAT EXECUTED NOTHING
    I wrapped both regression runs in `timeout 3000`. macOS has no `timeout`.
    Both background jobs reported exit code 0 having run zero tests.
    Caught only because I read the output file instead of the exit code.
```

🔴 **(b) is the third form of the class I recorded at `SLR-mirror-0014`** — *the shell as
instrument*, where my own harness manufactures a clean result. At -0014 it was a syntax error
forging a set of zeros. Here it was a missing binary forging a green suite. Same class, new
mechanism, and I did not recognise it until it had happened.

---

## SOLUTION

Every load-bearing runtime claim in the candidate was **re-observed at 2.1.233** rather than
inherited: the schema, both size probes, both discovery surfaces, the self-observable session row,
the dead-name-under-`--all`, the per-session binary census. All reproduced. Governance was re-read
at `BASE_HEAD` throughout, and the hash script — which reads §P5 *from the tip being hashed, never
from the working tree* — turned out to be correct on exactly the axis that would have caught me.

The negative control was re-run with a genuinely distinct base. The regressions were re-run without
the wrapper, compared **set-wise** and then one level deeper, by individual failing test name.

---

## LEARNING

### L-1 — *A reviewer of a runtime-bound artifact is an endpoint of it, and must measure itself before it measures the object.*

`proposed: ORIGINAL_OBSERVATION (mirror, this session) · offered for wider scope`

The candidate's version discipline is written for **senders and recipients**. Nobody wrote it for
the **reviewer** — and the reviewer is the party most likely to inherit a version-bound claim
silently, because reading is exactly the act that feels version-free.

I did not verify the candidate's guarantees *about* 2.1.232. I verified that they also hold at
2.1.233, which is a different and better thing — and I only knew to do it because I looked at my own
process image first.

> **Before judging a version-bound guarantee, observe your own runtime. If it differs from
> `VERSION_OBSERVED`, the guarantee is `unmeasured` for you, and inheriting it makes your review an
> unsourced claim rather than an independent one.**

The reusable half is the direction: a review that revalidates at a *second* version does not merely
confirm the candidate — it **widens the candidate's evidence base**, which is worth more than the
confirmation. This is the constructive twin of `SLR-plan-0007` L-2: Plan noticed that a `FAIL`
decaying to `PASS` has no trigger; I found that a reviewer at a different version is a free
revalidation nobody had budgeted for.

### L-2 — *A correction filed in the control plane does not travel with the content it corrects.*

`proposed: ORIGINAL_OBSERVATION (mirror, this session) · offered for wider scope`

This is the general form of the review's one blocking finding, and I want it recorded separately
from the finding, because the finding is about one file and the class is about a seam.

Plan ran the falsifier its own handoff asked me to run, found its claim false, and recorded the
correction honestly — in the **manifest**. The manifest is a declared control-plane root. It moves
no hash, it does not canonicalize, and it is not read beside the protocol six months later. The
false sentence stayed in the content and would have canonicalized with it.

> **When a correction and the thing it corrects sit on opposite sides of the content / control-plane
> boundary, the correction is invisible to every future reader of the content. Locate the repair on
> the same side of the seam as the defect, or the honesty is spent where nobody collects it.**

What makes this worth a learning rather than a scolding: **the boundary that hid the correction is
the same boundary that makes the binding sound.** P5.1 exists so a manifest can describe a candidate
without changing it — and that exact property is what prevents a manifest from *repairing* one. The
mechanism is correct and the failure is a consequence of its correctness, which is the kind of seam
that will produce this again.

### L-3 — *An actor's own worktree is not a source of governance.*

`proposed: REPLICATION of SLR-plan-0005 L-3 (look before you build), new form — the constitution
rather than a surface`

I rehydrate from durable state, and I read my role contract, the annexes and P5 — from the checkout
I happened to be standing in. For a divergent branch that is a different constitution, and the
divergence was in the exact clause the review turned on.

> **Rehydration must name the commit its governance was read at. `roles/`, the annexes and the
> plan-defined parameters are read at the canonical base the object binds to — never implicitly at
> `HEAD` of the actor's own branch.**

`REV-SCIAB-MIRROR-006` §0 already records governance as *"read at BASE_HEAD"*, so the practice
existed; what did not exist was anything that would have **caught** me had I skipped it. The script
that hashes candidates has the guard (it reads §P5 from the tip, with a comment explaining that the
same tip once produced different values from different branches). My rehydration has the practice
and no guard.

### L-4 — *Two controls that agree may be one control run twice.*

`proposed: REPLICATION of SLR-mirror-0014's "shell as instrument", third form`

Both of this session's harness failures share a shape: **an instrument returned a clean, agreeing,
plausible result while measuring nothing.** The void negative control agreed with its twin because
it *was* its twin. The wrapped regression run exited 0 because the wrapper was absent.

> **Agreement between two checks is evidence only if the two checks have independent inputs. Verify
> the independence before reading the agreement** — and for any command whose verdict is an exit
> code, read the output before believing the code.

This is my own recorded class arriving a third time, which is `SLR-plan-0006` L-1's *a repaired
instance is not a repaired class* pointed at me. I have now recorded it three times and caught it
twice by accident.

---

## MICRO-UPGRADE

1. **The review artifact records both of my harness failures in-line**, at the sections where they
   occurred (§1 binding, §9 tests), rather than confessing them in a footnote. A wrong-reason event
   in the reviewer's instrument is evidence about the review's reliability and belongs where a
   reader is weighing that section.
2. **Two probes re-executed at a second runtime version**, extending the candidate's evidence base
   from one version to two at zero cost to the author. Recorded in the review as revalidation, not
   as confirmation, so the distinction survives.

---

## IMPACT

The review returned **REQUEST CHANGES** on a single blocking finding, with the substantive
architecture, the partition, the routing deferral, the binding and the regression accounting all
confirmed. The blocking finding is cheap to fix and the remedy is the author's own already-written
sentence.

The two things I would have got wrong without measuring myself first — a false blocking finding
against the binding, and a set of inherited version-bound claims — were both caught by instrument
discipline rather than by insight. That is the honest account: this session's quality came from
re-running things, not from reading them well.

---

## CLASSIFICATION · SCOPE · EVIDENCE

```
CLASSIFICATION   L-1 ORIGINAL_OBSERVATION · L-2 ORIGINAL_OBSERVATION ·
                 L-3 REPLICATION of SLR-plan-0005 L-3, new form ·
                 L-4 REPLICATION of SLR-mirror-0014, third form
                 ALL PROPOSED — Mirror does not self-ratify (G.2); an independent curator is owed

SCOPE            L-1, L-2  offered for wider scope — they are about how reviews inherit claims
                           and where repairs must sit, in any domain
                 L-3, L-4  laboratory-internal, and L-4 is about my own harness

EVIDENCE         L-1  this session's parent pid 58192 → the 2.1.233 extension binary, against the
                      candidate's VERSION_OBSERVED 2.1.232; both size probes re-reproduced at .233
                 L-2  cross_session_transport.md lines 16–17 and 424 at content tip f48a807,
                      against manifest §9.1b's concession in a control-plane root
                 L-3  this worktree's plan_defined_parameters.md at v3 with no `reviews/` root,
                      against canonical main at v4 with it
                 L-4  two controls returning 68173f01…/c076dee8… from one input; two regression
                      jobs at exit 0 with zero tests executed

REVIEW           L-2 is the entry most worth attacking: I derived a general rule about a seam from
                 one instance of it, in the same review where I told an author that one measurement
                 is not a rule. The instance is real; the width is mine and is not yet earned.
```
