---
record_type: WORK_ANALYSIS
id: PLAN-ADJUDICATION-STATE-MATRIX-001
title: Every degraded state of the adjudication gate, reproduced — and why 4 and 9 were never in conflict
date: 2026-08-26
role: PRODUCER
mode: ANALYSIS_FIRST / MINIMAL_DELTA
authority: Plan role contract — candidate preparation on own branch. No canonical file modified.
  `framework/scripts/` is not Plan's to author; the repair is deposited as a candidate and is
  adopted by its owner or not at all.
status: ANALYSIS_COMPLETE — repair candidate CAND-20260826-ADJFAILCLOSED prepared and hashed
---

# THE ADJUDICATION GATE — FULL DEGRADED-STATE MATRIX AND REPAIR

> **Nothing here is medical advice.** Tooling and gate semantics only.

**No count was inherited.** Two figures were in circulation — four fail-open states, and nine
degraded states with exit 0. Neither was carried into this analysis, and neither turns out to be
wrong. **They answer different questions**, which is why they disagreed, and § 2 states both
questions so that a future reader is never again asked to choose between the numbers.

---

## 0 · Method

A sandbox that mimics the repository layout, so the script's
`ROOT = Path(__file__).resolve().parents[2]` resolves inside it; a synthetic two-page PDF whose
text is known; a recipe whose digests are produced by the script's own render path, so the clean
case is genuinely clean. **One mutation per case, restored from a pristine copy each time.**

🔴 **The harness lied to me twice, both times by substituting a control for its subject, and both
are recorded because the failure mode is the point.**

1. `restore()` derived the pristine directory from the sandbox's own name. Pointed at the patched
   sandbox, it copied the **original** script over it on every case — and the battery returned a
   perfect row-for-row match with the pre-repair run. A comparison whose two arms are the same
   object agrees completely.
2. The new test file globbed the subject's own directory for dependencies. The subject was a
   candidate copy sitting alone in a scratch directory, so **both arms died at import** and failed
   identically, 11 and 11.

Both now name what they load instead of deriving it, and the test file refuses to run at all if
the sandbox cannot execute the subject. **Two agreeing arms are not a result; they are a
hypothesis about the harness.**

---

## 1 · The matrix — 24 states, each independently reproduced

`EXIT` is the code a gate would read. `MISTAKEN FOR PASS` asks only whether an automated consumer
reading the exit code would record success.

| # | Precondition | EXIT | Current message | What was actually verified | Mistaken for PASS? |
|---|---|:--:|---|---|:--:|
| S00 | clean — control | 0 | `OK: 2 artifact(s)… 2 locator(s)…` | everything it claims | — |
| S01 | adjudications directory empty | **0** | `OK: 0 artifact(s)…` | **nothing** | 🔴 yes |
| S02 | `page_adjudications` root absent | **0** | `OK: 0 artifact(s)…` | **nothing** | 🔴 yes |
| S03 | `--pmid` names no existing study | **0** | `OK: 0 artifact(s)…` | **nothing** | 🔴 yes |
| S04 | `--pmid` misspelled by one digit | **0** | `OK: 0 artifact(s)…` | **nothing** | 🔴 yes |
| S05 | all recipe digests absent | **0** | `OK: 2 artifact(s) regenerate to their declared digest` | 2 rendered, **0 compared** | 🔴 yes — and the message is **false** |
| S06 | one digest absent of two | **0** | `OK: 2 artifact(s) regenerate to their declared digest` | 2 rendered, **1 compared** | 🔴 yes — **false** |
| S07 | one declared digest wrong | 1 | `FAILED — 1 problem(s)` | correct | no |
| S08 | recipe declares no manifest | 0 | prints the degradation, then `OK` | uniqueness + containment; **not** the snippet check | partly — the warning is on stdout |
| S09 | manifest declared, file missing | **0** | `no manifest declared` | as S08 | 🔴 yes — and *"no manifest declared"* is **false** |
| S10 | manifest path misspelled | **0** | `no manifest declared` | as S08 | 🔴 yes — **false**, and this is the one a typo produces |
| S11 | `artifacts` list empty | **0** | `OK: 0 artifact(s)…` | **nothing** | 🔴 yes |
| S12 | `adjudicates` empty everywhere | 0 | `OK: 2 artifact(s)… and 0 locator(s)…` | digests only — **and it says so** | no |
| S13 | needle matches twice | 1 | `FAILED` | correct | no |
| S14 | needle resolves outside the crop | 1 | `FAILED` | correct | no |
| S15 | bare locator, no needle | 1 | `FAILED` | correct | no |
| S16 | needle not a fragment of its snippet | 1 | `FAILED` | correct | no |
| S17 | source PDF absent | 1 | `FAILED — … across 0 artifact(s)` | correct | no |
| S18 | source PDF digest mismatch | 1 | `FAILED — … across 0 artifact(s)` | correct | no |
| S19 | PyMuPDF unavailable | **2** | `PyMuPDF is required…` | nothing, and says so | no |
| S20 | on-disk image stale after `write` | 0 | `OK: …` | the **recipe**, never the file on disk | see § 4 |
| S21 | recipe missing `artifacts` key | 1 | `KeyError: 'artifacts'` traceback | nothing | no — but not a verdict |
| S22 | recipe is not valid JSON | 1 | `JSONDecodeError` traceback | nothing | no — but not a verdict |
| S23 | two studies, one broken | 1 | `FAILED — 1 problem(s)` | the good one does **not** mask the bad | no |

### 1.1 · S05 in full, because it contradicts itself inside one output

```
99999999 a.png: no digest declared, produced f495b656…
99999999 b.png: no digest declared, produced 6abfb6f0…

OK: 2 adjudication artifact(s) regenerate to their declared digest, and 2 locator(s) resolve…
```

**Two lines above the summary the script says no digest was declared; the summary says two
artifacts regenerate to their declared digest.** No inference is needed to see this and no
reviewer had.

---

## 2 · The two counts, and the definitions that separate them

**Neither figure is wrong; they are answers to two questions nobody had written down.**

| Question | States | Count |
|---|---|:--:|
| **Q1** — in how many states does `verify` return **0** while having verified **strictly less than the summary sentence asserts**? | S05, S06, S09, S10 | **4** |
| **Q2** — in how many states does `verify` return **0** while some declared check was **skipped**, whether or not the summary lies about it? | S01, S02, S03, S04, S05, S06, S08, S09, S10, S11, S12, S20 | **12** |
| **Q3** — how many states did the repair **flip from 0 to 1**? | S01, S02, S03, S04, S05, S06, S09, S10, S11 | **9** |

**The unified taxonomy is Q2 minus the states that are honest about degrading.** S08 and S12 print
what they skipped and are left alone. S20 is a different defect (§ 4). That leaves the **9** of Q3
— and 9 is derived here from the repair, not adopted from a peer.

🔴 **The number matching an earlier figure of 9 is not corroboration.** Two counts agreeing prove
nothing unless the underlying sets were compared, and the earlier enumeration is not in a durable
artifact I can open. **What agrees is a scalar; the sets are unverified.** Recorded as an
unresolved comparison rather than as a confirmation.

---

## 3 · `checked += 1` — the semantic defect named exactly

```python
checked += 1                       # line 227 — the image was RENDERED
...
if declared is None:               # line 236
    print("no digest declared")    # nothing is compared
elif produced != declared: ...
else: ...                          # here, and only here, it MATCHED
...
print(f"OK: {checked} artifact(s) regenerate to their declared digest")   # line 252
```

**The counter is incremented at the moment the work begins and reported at the moment the claim
would be true.** Between those two points sit three outcomes — absent, mismatched, matched — and
`checked` cannot tell them apart because it was already incremented before any of them happened.

**A count is a claim. It must be incremented where the claim becomes true.**

The same shape, one line lower: `adjudicated += len(artifact["adjudicates"])` counts what the
recipe *declares*, while `check_needles` can `continue` past an adjudication without verifying it.

### 3.1 · The variables the repair introduces

The existing structure is kept — no framework, no new abstraction, one integer per question:

| Variable | Incremented when |
|---|---|
| `rendered` | an image was produced from the PDF |
| `digest_declared` | the recipe states what that image must hash to |
| `digest_matched` | it does |
| `digest_absent` | it does not state it — **nothing was compared** |
| `locators_declared` | adjudications the recipe lists |
| `locators_resolved` | …that resolved uniquely to a span the crop shows |
| `locators_vs_manifest` | …that were **also** checked against the snippet they name |
| `studies_seen` / `studies_skipped` | a study entered the loop / was abandoned before rendering |

`locators_resolved` and `locators_vs_manifest` are **returned by `check_needles`**, not inferred by
the caller from `len(adjudicates)`: the caller cannot see which adjudications took an early
`continue`, and inferring a count from a declaration is how the summary came to report work that
never happened.

### 3.2 · The manifest has three states, and had two

`snippets()` returned `None` both for *the recipe names no manifest* and for *the recipe names one
that is not there*. The caller printed **"no manifest declared"** for both.

⇒ **A one-character typo in a path retired the locator-to-snippet check and reported the
retirement as the author's intention.** `manifest_state()` now returns `NONE` (allowed),
`UNREADABLE` (always a defect, fails closed) or `OK`.

---

## 4 · What the repair deliberately does NOT fix

**Stated so that nobody records this as a closed class.**

| State | Why it is left | Class |
|---|---|---|
| **S20** stale on-disk image | `verify` re-renders from the PDF and compares to the recipe; it never reads the PNG on disk. That is arguably correct — the recipe is the evidence, the image is a local artifact — but `write` creates files that no check ever validates again. **Changing this changes what the tool is for**, and is not a counting defect | design question, routed |
| **S21 / S22** malformed recipe | exits 1 via an uncaught traceback. Fails closed, so it is not dangerous, but a traceback is not a verdict and a gate consumer cannot distinguish it from a crash | cosmetic, deferred |
| **S19** missing PyMuPDF | exit **2**, correctly distinct from exit 1. Left exactly as it is — see § 6 | correct already |

---

## 5 · The repair, and both mutation arms

Candidate branch `plan-adjudication-failclosed-repair`, `BASE_HEAD 788c357d`, tip `9cb09c08`,
`CANDIDATE_CONTENT_HASH 1e37c8ea26eedb1521f11f3febbdcbaed2a1ad780944c6822d9eb12c13aad2b1`
(reproduced twice).

| Arm | Subject | Result |
|---|---|---|
| **1** | 14 new subprocess tests against the **repaired** script | **14/14 pass** |
| **2** | the same 14 against the **original** script | **11 fail.** The 3 that pass are the regression guards asserting behaviour that was already correct — wrong digest, absent PDF, tampered PDF |
| **3** | the 12 **existing** tests against the repaired script | **12/12 pass**, after a 4-line change at the call sites (`check_needles` now returns a triple) |
| **4** | the 12 existing tests against the repaired script **before** those 4 lines | 9 failed — recorded because it is the integration cost, and hiding it would misstate the size of the change |

**S02 has no dedicated test.** It is repaired and exercised only by equivalence with S01, which
takes the same branch. Declared rather than counted as covered.

---

## 6 · Phase 3 — the gate wiring, and the wall it hits

### 6.1 · Is the property normatively required? **Yes. Is the wiring? No.**

`framework/master/gold_is_in_the_details.md` rule 5e — in the mandatory reading path — states:
*"Two conditions are machine-checked rather than argued: `crop_contains_span` for every locator
adjudicated, re-checked after any rounding, and a digest that regenerates."*

**That is a norm about the property, not about which gate hosts it.** The property is required;
the placement is a normative decision boundary and Plan does not close it.

### 6.2 · Today nothing invokes it

`scripts/run_release_regressions.py` lists `framework/scripts/test_regenerate_adjudications.py`
and **not** `regenerate_adjudications.py verify`. Confirmed independently: the string `verify`
appears in the module docstring and in **zero** executable gates.

**And the suite that *is* run imports exactly one name — `check_needles` — and never calls
`run()`.** Every state in § 1 lives in `run()`.

⇒ 🔴 **The tested surface and the degraded surface were disjoint.** Not under-tested: untested,
with a green suite beside it.

### 6.3 · Where the result is transcribed by hand

`disease-models/wwox/registries/fulltext_read_receipts.jsonl`, receipt
`FTR-20260811-16061658-02`:

> *"`regenerate_adjudications.py verify --pmid 16061658` returns PASS: 9 artifacts regenerate to
> their declared digest and 10 locators resolve to a span inside the crop that shows them."*

**That is the tool's verdict copied by a human into a hash-chained ledger.** Two observations, both
mechanical:

- the script **never prints the string `PASS`** — 0 occurrences. `returns PASS` is a paraphrase of
  `OK:`;
- `--pmid 16061658` is the flag form of **S03/S04**. In this worktree that study's PDF is absent
  and the command returns 1. The receipt is not thereby wrong — it records a run on a machine that
  held the file — but **nothing re-runs it, and nothing can.**

### 6.4 · 🔴 Why `verify` cannot be wired into the release runner as a hard gate

**Its inputs are unshippable by the same rule that created it.**

| Measured | Value |
|---|---|
| files tracked under `files/` on `main` | **0** |
| `.gitignore` line 7 | `files/` |
| `verify` in a fresh worktree of `main`, original script | **exit 1** — source PDF absent, all 3 studies |
| `verify` in that worktree, repaired script | **exit 1**, same three |

Rule 5e publishes the recipe *because* the reproduction may not be redistributed. **So the gate
that checks the recipe can only run where the private corpus already is** — the operator's
machine, and nowhere else. Adding `verify` to `TESTS` would make the release battery permanently
red for every clone.

### 6.5 · The minimum wiring, and its honest limit

| Step | Status |
|---|---|
| Register a suite that drives `run()` and needs **no corpus** — it builds a one-page PDF | ✅ **done in the candidate.** `test_regenerate_adjudications_fails_closed.py`, added to `TESTS` |
| Make `verify` itself a runner target | ❌ **not proposed.** § 6.4 |
| A corpus-conditional target that runs `verify` when `files/` is populated and **skips with a declared reason** otherwise | ⚠️ **available and not built here.** The runner already emits `PASS WITH SKIPS` with one reason per skip, so the mechanism exists |

🔴 **The limit is not a tooling gap and must not be recorded as one.** A skip is not enforcement.
Under rule 5e the repository **cannot** enforce, in CI, a check whose inputs it is forbidden to
ship. What CI can enforce is that the *checker* fails closed — which is what the candidate does.
**The property is enforced where the evidence is; the gate's correctness is enforced everywhere.**
Classifying that as `MANUAL_TOOL → ENFORCED_CHECK` would overstate it; the accurate transition is
`UNTESTED_MANUAL_TOOL → TESTED_MANUAL_TOOL + CORPUS_CONDITIONAL_GATE`, and the second half is a
normative decision boundary.

### 6.6 · Environment dependencies

`PyMuPDF` is imported by `regenerate_adjudications.py`, `deepdive_manifest.py` and several analysis
scripts. **It is declared in no dependency file.** `requirements-analysis.txt` exists and contains
one line, `numpy==2.0.2`. There is no `requirements.txt`, `pyproject.toml`, `setup.py` or
`setup.cfg`.

Consequence for wiring: `run()` returns **2** when the import fails, distinct from 1, so a runner
*could* tell "not installed" from "check failed" — but nothing declares the dependency, so the
distinction is currently reachable only by accident. The new suite handles this with
`@unittest.skipIf`, producing a declared skip rather than a failure.

---

## 7 · Reproduction

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5 --tip 9cb09c0863d52829b7abd6d094a688b1cf106b11
git diff --stat main plan-adjudication-failclosed-repair
```

The state matrix, both mutation arms and the sandbox builder are in this session's scratchpad and
are **not** durable. **They should be committed with the candidate if it is adopted** — a battery
that exists only in a transcript is the same defect this record is about.
