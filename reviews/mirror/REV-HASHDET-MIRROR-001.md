---
artifact: MIRROR R4 verification report (Annex C.2)
review_id: REV-HASHDET-MIRROR-001
object: governance/scripts/candidate_content_hash.py — determinism, fallback, failure behaviour
reviewer: mirror
adjudicator: operator
level: R4 / MIRROR_REQUIRED
review_date: 2026-08-17
verdict: REQUEST CHANGES — three blocking defects, all reproduced
scope: verification only — no implementation, no modification
---

# HASHDET R4 — the candidate content hash is not a function of (base, tip)

## Method

Two clones of the same repository, sharing one object store, checked out at two commits that carry
**different versions of the rule**:

```
hd_main   @ 908197b (canonical main)   CANDIDATE_HASH_VERSION: v3   roots: candidates/, ledger/
hd_ei     @ evidence-index             CANDIDATE_HASH_VERSION: v4   roots: candidates/, ledger/, reviews/
```

Every result below is a command output, run in both, with a positive control (test 4b) confirming
the comparison discriminates before any negative result was relied on.

---

## 1 · Determinism across checkouts — **FAIL**

Same `--base`, same `--tip`, two checkouts:

```
base 908197ba…  tip 629bc89a…
  from hd_main :  573867891ae2550385988cba13533074372baf3f3aba1e01667048ae4f171992
  from hd_ei   :  b1f3729ba493c414cba5eb1cdccc8b739f9631a3cecf87cbf070714bad32f956
```

**The hash is not a function of (base, tip). It is a function of (base, tip, the working tree of
the checkout it is run from.)** The manifest's published value is the one obtainable from a
checkout that already carries the amended rule; from canonical `main` the same command returns a
different 64 hex characters with no warning and exit 0.

This is the property the whole binding rests on. Gate 5 binds an approval to a value; a value that
depends on where the verifier stands cannot discharge that binding.

## 2 · No fallback / no working-tree read — **FAIL**

The content comes from the committed tree (`git ls-tree -r --full-tree <tip>`). **The rule does
not.** `parse_p5()` reads `plan_defined_parameters.md` from the filesystem path of the checkout, so
the domain definition is taken from the working tree while the domain contents are taken from the
commit.

Demonstrated with an **uncommitted** edit:

```
before edit            b1f3729ba493c414cba5eb1cdccc8b739f9631a3cecf87cbf070714bad32f956
after uncommitted edit 4fec4ccaf70c81c6eda3c34c99c8ab738e9c0d7c31cbfbf8ba94100c363f1462
git status             " M governance/plan_defined_parameters.md"
```

A dirty checkout produces a valid-looking hash. GATE 0's root-clean requirement mitigates this at
*execution* time and not at *preparation or verification* time — and candidates are prepared on
`evidence-index`, where no clean requirement applies at all.

## 3 · A tip without the rule must fail — **FAIL**

```
tip 749a9a9b — governance/ files in that tree: 0
result        e0c846951ac8ba1236205b2f39f439ea1d21660f35b3a139b6673de34f149461
exit          0
```

The tip predates the existence of `plan_defined_parameters.md` entirely. The script returns a hash
anyway, having silently borrowed the rule from the checkout. **A domain rule was applied to a tree
that never contained one, and nothing said so.**

This is `PATTERN_ALREADY_SOLVED_GATE` variant 3 in its exact shape: *a green result from an
environment incapable of exhibiting the defect.* The tip cannot disagree with the rule, because the
tip is never asked.

## 4 · Negative controls — **PASS, and they matter**

The fail-closed behaviours that exist are correct. Reported because a report of three failures is
worth less without them:

```
4a  bad tip (deadbeef…)          exit 2   ✅ refuses
4c  rule file absent entirely    exit 2   "DOMAIN FAILED: cannot read …"   ✅ refuses
4b  positive control             two genuinely different tips → two different hashes ✅
```

*(4a's exit code needed a second measurement: my first read `$?` after a pipeline, which reports
`tail`, not the script. The corrected reading is 2.)*

So the script refuses a missing rule and a missing commit. **It does not refuse the case where a
rule exists but is the wrong one for the tree being hashed** — which is the only one of the three
that can occur silently.

## 5 · Backward impact — recorded hashes stop reproducing

`CAND-20260816-GOV311`, approved under `APR-20260816-GOV311-001` and committed at `908197b`:

```
RECORDED / APPROVED       c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239
recomputed from hd_main   c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239   ✅
recomputed from hd_ei     db5ede52aeabac28af266e879d2a6040cd5d7e8beb8db40d711a7e44af314afb   ❌
```

**Existing candidates do not become invalid.** The approval and the commit are historical records —
STATIC, in C-9's terms — and nothing about them changes. What breaks is the **re-verification
path**: once the amendment is on `main`, the command the manifest publishes no longer returns the
value the manifest records, from the checkout a reader will actually have.

The value is still recoverable — by first checking out the rule in force when it was computed — but
that procedure is written nowhere, and a reader who runs the published command and gets a different
answer has every reason to conclude the binding was falsified.

**The version prefix does not cover this.** P5 introduces it *"so that a future change to this
definition cannot silently produce colliding values with the old one"* — it guarantees v3 and v4
values can never be **equal**. It says nothing about a v3 value remaining **reproducible**, and the
candidate's reasoning treats anti-collision as if it were backward compatibility. They are
different properties and only the first is delivered.

## 6 · CHANGE_CLASS — **MAJOR confirmed, and these results strengthen it**

Already confirmed in `REV-P51C9-MIRROR-001` on two independent routes. This verification adds a
third and larger one: the amendment does not merely change one candidate's value, it changes **what
the command means in every checkout, for every past and future invocation**. A change that alters
the semantics of the instrument by which gate 5 is discharged is gate policy under §12 by the
shortest possible argument.

---

## BLOCKING FINDINGS

```
F-1  The hash is a function of the checkout, not of (base, tip).  §1
F-2  The domain rule is read from the working tree; an uncommitted edit changes the value.  §2
F-3  A tip that does not contain the rule is hashed anyway, exit 0.  §3
```

**What must be true.** The rule must be read from the same place the content is: the tip's own tree.
That single property closes all three — the hash becomes a pure function of (base, tip); the
working tree stops participating; and a tip with no rule has nothing to read and must refuse, which
is the failure §3 asks for. It also restores §5, because a historical hash then recomputes from any
checkout.

I state the property, not the patch. Whether the rule is read from the tip, or pinned by digest
into the manifest, or something else, is Plan's to propose.

**One consequence to weigh, not to hide:** reading the rule from the tip means a candidate is
hashed under the rule *it* carries. That is correct for verification and it makes preparing a
candidate under a newer rule an explicit act rather than an ambient one.

---

## DISPOSITION

```
1 determinism        FAIL      2 no fallback      FAIL      3 failure behaviour   FAIL
4 negative controls  PASS      5 backward impact  recorded hashes stop reproducing
6 change class       MAJOR — confirmed
```

The three failures are one defect seen from three sides: **the rule and the content come from
different places.** Nothing here impugns the byte layout, the entry ordering, the newline
discipline or the exclusion logic — I re-verified that the script refuses a missing rule and a
missing commit, and that its included-set construction is sound. The defect is the provenance of
the rule, and it is upstream of every property the hash is asked to have.

**This report does not authorise execution and takes no decision.** No file modified, no candidate
touched, no governance changed. All tests ran in disposable clones outside the repository.

---

## Appended 2026-08-18 — where this record's C.2 elements live

🔴 **The `(Annex C.2)` label in the text above is wrong.** `OWED-C2-FORMAT-001-REPAIR` **§ A** reclassifies this record as a **MIRROR R4 verification report**, for which **C.2 is NOT APPLICABLE** — a verification report has no author to steelman and no thesis to falsify. Findings unaffected.

Appended, not edited. The original text above is unchanged.
