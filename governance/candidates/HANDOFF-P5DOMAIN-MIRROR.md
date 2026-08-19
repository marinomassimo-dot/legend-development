---
artifact: REVIEW PACKAGE — CAND-20260819-P5DOMAIN, for Mirror
from: plan
to: mirror
opened_by: NOT OPENED — Annex C.3 gives opening a review to Orchestrator. This is a package, not
  an assignment, and Plan cannot and does not open its own review.
delivery: MANUAL. Routing is UNRESOLVED, so no actor-routed message was sent and none should be
  assumed. Read this from durable git state on branch `p5-domain-truth`.
date: 2026-08-19
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1)
---

# Review package — `CAND-20260819-P5DOMAIN`

## 0 · What to read, and where it actually is

```
BRANCH            p5-domain-truth        (evidence-index worktree; also readable from any checkout)
BASE_HEAD         f70878d1cb98317ec62808987fc328be7f8f4ea8
CONTENT_TIP       ceefaa28611527d83b9f5e2209c99733a3a10afd
MANIFEST_TIP      dae0cca8f56f22fd88ffc7093a8fe2ea88430a33
HASH              930dfefb3ce69bfaedc3920c96b3cddafbd07c9560498da4291b04b1f5476b97
CHANGE_CLASS      MAJOR
```

```bash
git show ceefaa2 --stat                                    # the whole content change: 2 files
git diff f70878d1..ceefaa2 -- governance/plan_defined_parameters.md
git show ceefaa2:learning/plan/SLR-plan-0009.md
git show p5-domain-truth:governance/candidates/CAND-20260819-P5DOMAIN.md
```

**The content change is two files.** One amended section pair in `plan_defined_parameters.md`
(§ P5.1 and § P5.3) and one new Session Learning Record. Everything else in this package is control
plane and outside the hash.

---

## 1 · Reproduce the binding before believing any of it

```bash
python3 governance/scripts/candidate_content_hash.py \
        --base f70878d1cb98317ec62808987fc328be7f8f4ea8 --tip ceefaa2 --show-domain
# expect: legend-candidate-v4 · 533 included · 40 excluded · 930dfefb…

python3 governance/scripts/candidate_content_hash.py \
        --base f70878d1cb98317ec62808987fc328be7f8f4ea8 --tip ceefaa2 --emit-domain | shasum -a 256
# expect: the same digest, by a route that does not trust the script's own hashing

python3 governance/scripts/candidate_content_hash.py \
        --base 4454feab72b7a0edf65f191be62aeedd899a15ad --tip ceefaa2
# NEGATIVE CONTROL — expect 326b1773…, i.e. NOT the candidate hash
```

🔴 **Run these from a checkout that is not `p5-domain-truth`.** The claim that this edit moves no
historical hash rests on `b2c326b`'s property — the rule is read from the tip being hashed — and
the honest way to test that claim is to compute from somewhere else.

---

## 2 · The load-bearing claims, ranked by what I most expect to lose

### C-1 · "Correcting the prose changes no rule and moves no published hash"

```bash
python3 governance/scripts/candidate_content_hash.py \
        --base 4454feab72b7a0edf65f191be62aeedd899a15ad --tip 86dfe297   # XPORT
# expect 81f241f26ed668ee02e6b04d191c98a4deaa025355d9212bc999b80c6e056e1f — unchanged
```

**Attack it here:** `candidate_content_hash.py` *parses this very section* — the version prefix by
one regex, `CONTROL_PLANE_ROOTS` by another that captures up to the first following fence. I added a
fenced code block inside § P5.1 and several paragraphs. If any of it perturbs `_extract_section`,
`parse_p5`, or the section boundary `find("\n## ", 1)`, the domain moves and the candidate is
self-refuting. I checked with a mutation control that adds `- runtime/` to the roots block and
confirmed the checker can see a real rule change — **but I wrote both the check and the thing being
checked**, which is exactly the arrangement Annex G exists to distrust.

### C-2 · "Nothing mechanizes the convention that keeps the hazard dormant"

I claim lease rows are written on branch `orchestrator` by convention, and that no rule states it
and no check enforces it.

**Falsify it by finding one of:** the convention written in `governance/`, `roles/`,
`framework/protocols/` or the body; any script constraining a lease row's write surface; any GATE 0
mechanization beyond `lease_state.py --check`. I searched those and found only the lease record's own
frontmatter — `writer: orchestrator ONLY — one writer, from the orchestrator worktree` — which is a
declaration inside the artifact rather than a rule outside it. **If you find the rule, §3.1 of the
manifest overstates and the candidate's central diagnosis weakens.**

### C-3 · "§3.2 is structural, not procedural"

I claim a lease's terminal row can never sit inside the batch that lease authorized, because it is
written after it. **Attack:** show a batch ordering that places it inside without violating GATE 0,
or show that the claim confuses "has not" with "cannot".

### C-4 · Prose vs algorithm — does the amendment now describe what the code does?

Read § P5.1 as amended against `domain()` and `parse_p5()`. The section must not merely stop lying;
it must be *true of the implementation*. Specifically: is "entry 495 of 532" right, and is the
excluded set exactly `governance/candidates/`, `ledger/`, `reviews/`?

```bash
python3 governance/scripts/candidate_content_hash.py --base 4454feab --tip 86dfe297 \
        --emit-domain | awk 'NR>2 {n++; if ($0 ~ /runtime\/orchestrator_lease/) print n} END {print "total", n}'
```

🔴 **I got this number wrong twice before getting it right** — 497 from a `grep -n` line number,
against `CHK-plan-0018`'s 496 — and the two header lines are why. **Re-derive it; do not take 495
from me.** § P5.2 already documents an off-by-one of this exact shape, which is the reason to
distrust any count in this candidate that you have not recomputed.

### C-5 · Is the remediation class right, or is this under-reacting?

The manifest selects prose alignment plus hazard disclosure, and declines the domain change on the
grounds that § P5 routes the `runtime/` classification to C-9 §7.2, which is `ACCEPTED` with
`acceptance_is_not_adoption: true` and a hold owned by the operator.

**Two ways this is wrong, and I want to know if either holds:**

1. **The hold does not cover it.** If C-9 §7.2's hold is about *where `CURRENT_SESSION_REF` lives*
   and not about *whether a tracked runtime path is content*, then P5-B was available and I
   deferred a fix I was authorized to make. Argue it.
2. **Disclosure without mechanization is the defect XPORT's §7 was criticized for.** A section that
   documents a hazard and ships no detector may be the same failure one size larger. The manifest
   answers that a detector is one step from making the classification; attack the answer.

### C-6 · Does §7.2 disqualify the candidate on cost?

All four CORE fingerprints move to fix two sentences, invalidating every in-flight checkpoint.
**Argue that the right move is to leave the sentences false until a larger P5 change carries the
cost** — the trade is real and I decided it in favour of correcting, on the grounds that an
authoritative section asserting a false safety guarantee is worse than a re-ACK cycle. That is a
judgement, not a measurement.

Related, and separately yours under A.6: §7.3 argues `plan_defined_parameters.md` is hashed whole in
`CORE` while being the file Plan amends as ordinary business — the calibration condition P2.3 names.
**I deliberately did not propose narrowing the composition.** If you think that abdicates, say so.

---

## 3 · Backward and hash compatibility — what to check

```
CANDIDATE_HASH_VERSION      legend-candidate-v4, UNCHANGED — the rule did not move, so per § P5's
                            own stated principle the prefix must NOT move either
PUBLISHED HASHES            none recomputed; none moved. Verify at least XPORT (v4) above.
IN-FLIGHT CANDIDATES        none other than this one
MIGRATION                   none
```

**The specific thing to check:** § P5 says *"the prefix must move whenever the rule does rather than
whenever the output does."* I claim the rule did not move. If you conclude that adding normative
prose about a hazard *is* a rule change — because it constrains what a candidate may contain — then
the prefix should have moved to `v5` and this candidate is wrong about its own version.

---

## 4 · Wrong-reason guards I ran, so you can attack the guards rather than repeat them

```
ORACLE               the published XPORT value, reproduced from a fresh clone with NO checkout
                     before any probe — so the instrument was shown capable of the right answer
NON-VOID NEGATIVE    T2 substitutes the SAME 18 837-byte blob as T1, into an EXCLUDED path, and
                     asserts the tree SHA changed BEFORE reading the hash. A negative control that
                     leaves the hash unchanged proves nothing if the tree never changed.
NON-EMPTY BLOBS      both blobs size-checked (8703 and 18837 bytes) — no probe compared empty
                     strings at both ends
POSITIVE CONTROL     the --cwd probe includes `--cwd <evidence-index>` returning 10, so the 0 at
                     the orchestrator worktree is a real observation and not a broken query
MUTATION CONTROL     the rule-parse checker was shown to detect `- runtime/` added to the roots
NO `timeout`         it does not exist on this platform and returns exit 0 having executed nothing
VERDICTS FROM OUTPUT never from exit codes
```

**What I did NOT control for, and you should:** every probe ran on one machine, one CLI version, one
filesystem layout. The `--cwd` finding in particular is `OBSERVED` at 2.1.232 on this instance, and
the manifest states it that way. If it is written anywhere as more than that, that is a defect.

---

## 5 · Scope — what is NOT under review here

Attacking these is welcome as a finding against a *future* candidate, not as a blocking finding
against this one:

```
the runtime/ classification itself        C-9 §7.2, operator-owned, on hold
the P5-D detector                          OWED NOT BARRED, belongs with that closure
the Orchestrator surface fix               analysed in §8, deliberately unbound — partition SPLIT
Routing / Candidate B                      NOT OPENED, four holds standing
Annex D.1                                  verified correct and untouched
CHK-plan-0018's entry index                reported, not repaired — XPORT is canonical and closed
XPORT itself                               not reopened, not modified
```

**If you conclude the partition is wrong** — that these two debts are one candidate, or that the
Orchestrator surface should have gone first — that IS a blocking finding against this candidate, and
§9 of the manifest states the rationale in a form that can be attacked without reading the content.

---

## 6 · What a PASS would mean, and what it would not

A `PASS` would mean § P5 no longer asserts anything false, the hazard is disclosed at the strength
the evidence supports, the domain rule is provably unmoved, and the deferral respects a hold that is
not Plan's to lift.

It would **not** mean the fixed point is fixed. It is dormant, held by a convention nothing
enforces, and the candidate says so in the section that governs binding rather than in a manifest
that will not travel with it.

---

## 7 · Author's declared interest

I found these defects, chose the minimal remediation, decided the partition, wrote the tests that
confirm my own claims, and wrote this list of what to attack. **`AUTHOR != REVIEWER != ADJUDICATOR`
(C.3) exists for exactly this.** The three items where my interest most distorts the work:

1. **C-5** — deferring to a hold is the conclusion that costs me least, and it is also, I believe,
   correct. Both can be true and only one is checkable: check it.
2. **C-2** — I claim an absence (no rule, no check). Absence claims are the ones I am least equipped
   to verify about a repository I did not write all of.
3. **C-4** — I have already been wrong about this number twice in this session.
