---
artifact: MIRROR hostile review (Annex C.2)
review_id: REV-HASHDET-MIRROR-002
candidate: CAND-20260817-HASHDET (revision 2)
content_hash: 1ef68cc09b1607623971af6eb2c2f91fa952d85bcaa4f5599c7765fbd9c650be
base_head: 908197ba62a064546f17c9c277ff497ffc753656
branch_tip: 153b35da216ef33cdf4a990bfa6fccf41adce966
supersedes_scope_of: REV-HASHDET-MIRROR-001 (e66d4a98, REQUEST CHANGES, F-1/F-2/F-3)
reviewer: mirror
adjudicator: operator
level: R4 / MIRROR_REQUIRED
review_date: 2026-08-17
verdict: REQUEST CHANGES
scope: verification and governance only — no implementation, no modification, no authorisation
---

# MIRROR HOSTILE REVIEW — CAND-20260817-HASHDET r2

```
candidate  CAND-20260817-HASHDET revision 2
reviewer   mirror
level      R4 / MIRROR_REQUIRED
verdict    REQUEST CHANGES  — one blocking finding, manifest-local, hash unaffected
```

**All three blockers from `e66d4a98` are closed**, on tests I re-ran independently — including one
of my own that was invalid and had to be redone. The single blocking finding below is in the
manifest's verification record, not in the fix.

---

## 1 · STEELMAN

**The correction is the one I said had to be true, and it is implemented at the source rather than
patched at the edges.** `parse_p5()` now reads via `_git("show", f"{tip}:{PARAMETERS_PATH}")`; the
`read_text` call on the checkout is gone; the failure path is specific rather than generic —
*"the domain rule is absent at <tip> … this command will not substitute the working tree's copy."*
A refusal that names the thing it refuses to do is a better artifact than a refusal.

**The tests discriminate, and I proved it by mutation rather than by reading the claim.** Running
the same suite against the pre-fix script recovered from `908197b`:

```
against the fixed script    7/7 PASS
against the pre-fix script  2/7 — branch-independence, dirty-tree, missing-rule and
                            emitted-domain all FAIL, exhibiting the defect
```

That is the property `LEARN-MIRROR-002` asks for: a suite seen to pass **and** to fail. The
declared 7/7 and 2/7 are exact.

**`--emit-domain` does what it claims.** 54 553 bytes, `version \n base \n` then the newline-
terminated entries, and `shasum -a 256` over those bytes returns
`b1f3729b…` — **identical to the reported hash**. The hashed object is now inspectable rather than
asserted, which is the difference between a script that *is* the recipe and a script that
*implements* one.

**Historical replay is restored, which was the point.** The approved `CAND-20260816-GOV311`
recomputes to `c39ecae8…30c239` from all three checkouts — including one whose working tree carries
the v4 rule — because the rule now travels with tip `9720a0cd`, which carries v3. This is the
property whose failure I reported as the most consequential, and it is fixed.

**All four declared reproductions verify exactly**, recomputed independently:
`c39ecae8…`, `f325bd9d…0651da`, `280dc497…65763d`, `1ef68cc0…c650be`.

---

## 2 · BLOCKING FINDINGS

### F-1 — §8's verification record belongs to revision 1, and contradicts §1 on the candidate hash

```
claim      "Candidate hash | published command, twice | identical 12d8f4b1…695c61"
           "Determinism suite | 5/5 PASS"   ·   "Suite can fail | 1/5 — 4 failures"

evidence   §1 declares CANDIDATE_CONTENT_HASH: 1ef68cc09b16…c650be at BRANCH_TIP 153b35da,
           and the published command returns exactly that.
           12d8f4b1…695c61 is the hash at tips b2c326b and d368744 — revision 1.
           The suite defines 7 test functions (`grep -c '^def test_'` → 7) and reports 7/7
           against the fix and 2/7 against the pre-fix script, both re-run by me.

problem    The manifest states two different candidate hashes in one document, and the row that
           does it is the row attesting that the value reproduces. For a MAJOR whose entire
           subject is hash reproducibility, an internally contradictory hash record is the one
           defect that cannot be waved through: the operator would be approving a document that
           disagrees with itself about the value being approved. The stale test counts compound
           it by understating the evidence that actually exists.

required   Recompute §8 against revision 2: hash 1ef68cc0…c650be, suite 7/7, mutation 2/7.
correction
```

**This is manifest-local.** `governance/candidates/` is a declared control-plane root, so the
correction leaves `1ef68cc0…c650be` unchanged, and the verdicts in this review remain bound to the
same object. No new review is required — only re-verification of the corrected rows.

**Recorded because it is the fifth occurrence of one pattern in this series.** A verification
record carried forward from a prior revision while the header advanced: rev-4's 507-for-508, RC-3's
stale count, N-1's 16-for-17 in P51C9, and now a stale *hash* plus stale test counts. Each was
caught, each was fixed locally, and the shape returned. That is branch (B) of the candidate's own
sibling proposal — a value true when written, invalidated by the work moving on, with nothing that
re-anchors it — sitting in the verification section of the very candidate that fixes reproducibility.

---

## 3 · NON-BLOCKING OBSERVATIONS

**N-1 · the `--emit-domain` == hash invariant holds by duplication, not by construction.**
`serialize_domain()` (line 127) and `compute()` (line 135) each build the serialization with an
identical expression; `compute()` does not call `serialize_domain()`. Today the bytes and the hash
agree because two lines are the same. Edit one and the published representation stops describing
the hashed object, with a passing test suite unless the emitted-domain test happens to catch it —
it would, which is why this is non-blocking. Structurally, the property the section exists to
guarantee is asserted twice rather than derived once.

**N-2 · the published representation is vulnerable to the exact defect that started this.**
Measured: `--emit-domain | shasum -a 256` → `b1f3729b…` ✅; `printf '%s' "$(--emit-domain)"` →
`c0a53fd3…` ❌. `$(...)` strips the trailing newline, so the third party the representation was
published for can silently re-digest 54 552 of 54 553 bytes. The script is right and the hazard is
in the hands of whoever verifies. P5.2 already documents *"every entry is newline-terminated,
including the last"* and cites the revision-4 incident; the emitted output carries no such warning.

**N-3 · `test_historical_replay` does not discriminate in the environment it runs in.** It is one
of the two tests that **pass against the pre-fix script**, because the checkout used carries the v3
rule — the same rule tip `9720a0cd` carries — so the broken implementation gets the right answer
for the wrong reason. From a v4 checkout the same test would fail against pre-fix. The property is
covered by `test_hash_is_branch_independent`, which does discriminate, so nothing is unproven; but
the test named for the property the mandate calls *"il punto più importante"* is not the one that
proves it.

**N-4 · encoding is implicit.** P5.2 specifies the version line, the base line, `git ls-tree -r
--full-tree`, path-sorting and newline termination — enough for an independent implementation
except the encoding, which is UTF-8 in the script and unstated in the recipe. Moot while every path
is ASCII; load-bearing the first time one is not.

**N-5 · my own first determinism test was invalid and I report it.** I initially ran one copy of
the fixed script from three working directories, which varies nothing: `REPO_ROOT` derives from
`__file__`, so all three runs operated on the same repository. I noticed because a checkout whose
working tree said v3 returned the v4 value, and redid the test by placing the script in each clone
so `REPO_ROOT` genuinely differed. The results in §1 are from the corrected test.

---

## 4 · CHANGE_CLASS VALIDATION — **MAJOR CONFIRMED**

Confirmed, and this revision makes the case stronger rather than weaker. §12's strict test is met on
three independent routes: it changes the canonical identity function; it changes what GATE 5 binds
to; and it changes the replay semantics of every approval record ever issued. The fact that the
change *restores* a property rather than altering one does not lower the class — the instrument by
which candidate identity is established is being redefined, and every past and future invocation
changes meaning with it.

---

## 5 · GOVERNANCE RISKS

**Historical replay — resolved, and it is the risk that mattered.** Before this fix, approvals
bound to `c39ecae8` stopped reproducing the moment a newer rule reached a checkout. After it, they
reproduce from anywhere. The approval record and the recomputation now agree permanently, because
neither depends on where the verifier stands.

**Third-party verifiability — substantially improved, with one residual.** `(base, tip)` plus P5.2
is now sufficient for an independent implementation, and `--emit-domain` lets a third party check
the object rather than trust the tool. The residual is N-2: the commonest shell idiom silently
breaks the re-digest.

**Future compatibility — a property worth naming.** Reading the rule from the tip means a future
rule change cannot retroactively alter a past candidate's identity, because past tips carry past
rules. That is stronger than the version prefix, which only prevented collisions. The candidate
does not claim this and it is worth recording as a gain.

**Regression risk — low and localised.** The change is one function's source of input. The suite
covers all three former defects and is proven to fail without the fix. N-1 is the only structural
soft spot and it is one refactor from being closed.

---

## 6 · LOCATOR_OVERSHOOT REVIEW

| Claim | Verdict | Evidence |
|---|---|---|
| `HASH = f(BASE, TIP)`, checkout-independent | **SUPPORTED** | three clones, working-tree rules v3/v3/v4, each running its own copy: `b1f3729b…` from all three |
| the working-tree constant is removed | **SUPPORTED** | no `read_text`; rule via `git show {tip}:`; `REPO_ROOT` survives only as git's `-C` |
| a tip without the rule fails | **SUPPORTED** | tip `749a9a9`, 0 governance files → exit 2, `DOMAIN FAILED: the domain rule is absent at …` |
| suite 7/7 against fixed, 2/7 against pre-fix | **SUPPORTED** | re-run by mutation, both figures exact |
| `--emit-domain` prints the hashed bytes | **SUPPORTED** | 54 553 bytes; `shasum` → identical to the reported hash |
| representation sufficient for an independent implementation | **SUPPORTED**, with N-4 | P5.2 gives layout, flags, sort and newline rule; encoding unstated |
| the four reproductions | **SUPPORTED** | all four recomputed independently, exact |
| §8 "identical `12d8f4b1…695c61`" | **NOT_IN_SOURCE** | that is revision 1's hash (tips `b2c326b`, `d368744`); r2 is `1ef68cc0…` |
| §8 "5/5 PASS" / "1/5" | **UNDERSHOOT** | the suite defines 7 and yields 7/7 and 2/7 |
| "no history rewritten — single commit, no rebase" | **SUPPORTED** | `hash-determinism` branches from `908197b`; the C-9 lineage orphaning I reported earlier is absent here |

---

## 7 · FINAL DISPOSITION

```
MIRROR_REVIEW: REQUEST CHANGES

CANDIDATE  CAND-20260817-HASHDET revision 2
HASH       1ef68cc09b1607623971af6eb2c2f91fa952d85bcaa4f5599c7765fbd9c650be
BASE       908197ba62a064546f17c9c277ff497ffc753656
TIP        153b35da216ef33cdf4a990bfa6fccf41adce966

CLOSED     F-1 determinism · F-2 working-tree rule · F-3 fail-closed on a missing rule
           — all three verified by independent re-execution, and by mutation against the pre-fix script

BLOCKING   F-1 §8's verification record is revision 1's: a hash contradicting §1, and two
               understated test counts

NON-BLOCKING  N-1 duplicated serialization · N-2 $(...) strips the published bytes' last newline
              N-3 the replay test does not discriminate in a v3 checkout · N-4 encoding implicit
              N-5 my own first test was invalid, corrected and reported
```

**The engineering is done and I could find nothing wrong with it.** The blocking finding is three
table rows describing an earlier revision of the same work. Corrected, this is `ACCEPT` — and the
correction changes no byte inside the domain, so this review's verdicts stay bound to
`1ef68cc0…c650be` and the re-review is three rows, not a fourth pass.

**This review does not authorise execution.** The final decision is the operator's. No file of the
candidate was touched, no governance modified, no gate executed. All tests ran in disposable clones
outside the repository; the working tree here is clean.

---

## Appended 2026-08-18 — where this record's C.2 elements live

Its `WHAT_WOULD_CHANGE_MY_MIND` and `AUTHOR_RESPONSE` were missing and are supplied in `OWED-C2-FORMAT-001-REPAIR` **§ B.2**, written on 2026-08-18 and marked there as after-the-fact.

Appended, not edited. The original text above is unchanged.
