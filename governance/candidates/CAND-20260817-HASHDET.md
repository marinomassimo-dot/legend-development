---
artifact: INTEGRATION_CANDIDATE manifest (Annex D.2)
candidate_id: CAND-20260817-HASHDET
governance_version: 3.1.1
change_class: MAJOR
prepared_by: plan
prepared_on: 2026-08-17
state: READY FOR MIRROR HOSTILE REVIEW
scope: governance/scripts/candidate_content_hash.py + its determinism tests. Nothing else.
origin: defect found by Plan during the final verification of the P51C9 remediation, classified
  by the operator as a new change rather than a fix inside either pending candidate
---

# INTEGRATION_CANDIDATE — hash determinism

## 1 · Manifest (Annex D.2)

```yaml
CANDIDATE_ID:               CAND-20260817-HASHDET
BASE_HEAD:                  908197ba62a064546f17c9c277ff497ffc753656
BRANCH:                     hash-determinism
REVISION:                   3 — verification-record repair per REV-MIRROR-HASHDET-R2 (7cd8b397)
BRANCH_TIP:                 b9af54ebe2fd24d94ec0eee71fcb064797922082
CANDIDATE_CONTENT_HASH:     c85acdb2d3e55f71bed9aa985ff996fdcfdd5b43c4b1e097c3b6063b80ad05d8
SUPERSEDED_HASHES:          12d8f4b1…695c61 (r1) · 1ef68cc0…c650be (r2) — DO NOT REVIEW
CANDIDATE_HASH_VERSION:     legend-candidate-v3   (this branch is cut from main; see P51C9 §1.2)
CHANGE_CLASS:               MAJOR
LINT_RESULT:                PASS
PUBLICATION_GATE:           PASS / BLOCKS: 0
MIRROR_REVIEW:              PENDING
HUMAN_APPROVAL:             PENDING
SNAPSHOT_ID:                n/a until canonical execution — GATE 4 belongs to Orchestrator
```

### Reproduction — one command, run twice

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 908197ba62a064546f17c9c277ff497ffc753656 \
  --tip  b9af54ebe2fd24d94ec0eee71fcb064797922082 --show-domain
```

```
EXPECTED          c85acdb2d3e55f71bed9aa985ff996fdcfdd5b43c4b1e097c3b6063b80ad05d8
OBTAINED (run 1)  c85acdb2d3e55f71bed9aa985ff996fdcfdd5b43c4b1e097c3b6063b80ad05d8
OBTAINED (run 2)  c85acdb2d3e55f71bed9aa985ff996fdcfdd5b43c4b1e097c3b6063b80ad05d8
DOMAIN            506 included · 12 excluded, as produced at this tip
```

### SOURCE_COMMITS

| # | Commit oid | Ancestry | Subject |
|---|---|---|---|
| 1 | `b2c326b56fe5367c5ff75c04a39f29d3cd35ccda` | **PASS** | The hash was a function of the checkout, and now it is not |
| 2 | `153b35da216ef33cdf4a990bfa6fccf41adce966` | **PASS** | The hashed object becomes publishable, and the approved candidate replays |
| 3 | `b9af54ebe2fd24d94ec0eee71fcb064797922082` | **PASS** | The verification record catches up with the object it verifies |

Cut directly from `BASE_HEAD`, no rebase in either commit's history. Row 2 was missing at the
reviewed revision — the same stale-representation defect as F-1, in the row directly above the
verification record, and found while repairing it.

---

## 1b · Revision 2 — response to REV-HASHDET-MIRROR-001

**Mirror's three findings were made against the pre-fix script**, the version on `main` and on the
two pending branches — not against this candidate, which did not exist when the review ran. Its
prescription is the property this candidate already implements: *"the rule must be read from the
same place the content is: the tip's own tree."* Evidence, from a branch carrying neither pending
candidate:

| Finding | Closed by | Demonstrated |
|---|---|---|
| F-1 identity depends on the checkout | rule read at `--tip` | historical replay of an approved candidate from a third branch (§4, test D) |
| F-2 working-tree rule leakage | the working-tree path constant no longer exists | `test_dirty_working_tree_does_not_move_the_hash`; fails on the pre-fix script |
| F-3 missing rule hashed anyway, exit 0 | explicit refusal, no fallback | `test_missing_rule_at_tip_fails_explicitly`; pre-fix returns a value |

**What revision 2 adds** is the half of the operator's principle that revision 1 did not carry: an
*explicit, versioned representation of the domain derived from the tip*.

### The single canonical source, made checkable rather than asserted

```
CANDIDATE_HASH_VERSION   § P5 at the tip
CONTROL_PLANE_ROOTS      § P5 at the tip
included / excluded      derived from the tip's tree under those roots
the hashed object        emitted verbatim by  --emit-domain
```

`--emit-domain` prints the exact bytes that are hashed. Their digest is the candidate hash:

```bash
candidate_content_hash.py --base <b> --tip <t> --emit-domain | shasum -a 256   # → the same value
```

That is what makes the source canonical instead of merely declared: **the recipe is defined over a
published representation, not over what this script does.** Any implementation that rebuilds those
bytes from `(base, tip)` reproduces the digest, and this script becomes one implementation of a
published recipe rather than the recipe itself. Mirror's own framing — *"whether the rule is read
from the tip, or pinned by digest into the manifest, is Plan's to propose"* — is answered by doing
both: the rule travels in the tip, and the domain it yields is emittable and digestible.

### Test D — the property that matters most, and it holds

The approved candidate `CAND-20260816-GOV311` **replays exactly**:

```
base 749a9a9b · tip 9720a0cd · rule at that tip: legend-candidate-v3
replayed → c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239
approved   c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239
```

Run from `hash-determinism`, which carries neither that candidate's rule nor its content. **The
rule travelling with the tip is what lets an already-approved hash survive every later change to
the recipe** — including the v3→v4 amendment pending in P51C9. Under the pre-fix script this was
impossible: the value depended on the checkout, so an approved hash decayed the moment governance
moved.

Suite: **7/7** against the fixed script, **2/7** against the pre-fix one.

---

## 2 · The defect

`candidate_content_hash.py` read the **tree** from the commit given as `--tip`, and the **rule** —
the version prefix and the control-plane roots — from `governance/plan_defined_parameters.md` **in
the working tree**. The contract in `§ P5` says the hash is a function of `(base, tip)`. The
implementation made it a function of `(base, tip, whichever branch happened to be checked out)`.

Measured, on the two pending candidates:

| Tip | Hashed from `orchestrator-worktree` (rule v3) | Hashed from `evidence-index` (rule v4) |
|---|---|---|
| `ab4856b1` | `280dc497…65763d` | `b4e7c493…cea3be0` |

Same commit, same base, two values. Under `gate 5` an approval binds to a content hash; a hash a
third party cannot reproduce makes that binding unenforceable at the exact moment it matters — the
same class as RC-1, from a different door.

**Why it stayed invisible.** For as long as every candidate was hashed from its own branch, the
working tree and the tip carried the same rule and the two definitions coincided. The defect
required two branches with *different governance* to become observable, and the candidate split of
this same day is what first created that configuration. It was introduced when the script was
written and was latent for its whole life.

---

## 3 · The fix

`parse_p5()` takes the tip and reads the rule with `git show <tip>:governance/plan_defined_parameters.md`.
The working-tree path constant is gone; there is no code path left that reads the rule from disk.

A tip that carries no rule now **fails explicitly**:

```
DOMAIN FAILED: the domain rule is absent at <tip>: governance/plan_defined_parameters.md could
not be read there. A tip that does not carry § P5 cannot be hashed under it, and this command
will not substitute the working tree's copy.
```

The refusal matters as much as the read. A silent fallback is precisely what let the defect live:
the old code, given a tip without the rule, quietly used the checkout's copy and returned a
plausible number.

### 3.1 · The fix validates the two pending candidates rather than disturbing them

Both published hashes now reproduce **from any checkout**, each under the rule its own tip carries:

| Candidate | Tip | Rule at that tip | Hash |
|---|---|---|---|
| `CAND-20260817-ORCHWT` | `ab4856b1` | v3 | `280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d` |
| `CAND-20260817-P51C9` | `b5eaf81e` | v4 | `f325bd9d1667638eeda718b73bc106263fea3a509f832bcc62e082cdba0651da` |

Verified from `hash-determinism`, a third branch carrying neither candidate. **Neither pending
manifest requires amendment**, which is why this is a separate candidate and not an edit to
either.

---

## 4 · Tests — and the demonstration that they can fail

`governance/scripts/test_candidate_content_hash.py`, five tests. Each builds a **throw-away git
repository** with two commits whose *rules* differ, so nothing depends on this repository's
history and the suite passes in a clean clone.

```
PASS  test_rule_comes_from_the_tip_not_the_working_tree — rule read from the tip, not the checkout
PASS  test_hash_is_branch_independent — branch-independent
PASS  test_dirty_working_tree_does_not_move_the_hash — immune to a dirty working tree
PASS  test_missing_rule_at_tip_fails_explicitly — absent rule fails explicitly, no fallback
PASS  test_determinism_across_runs — stable across runs
PASS  test_emitted_domain_is_the_hashed_object — emitted representation digests to the reported hash
PASS  test_historical_replay — approved candidate replays: c39ecae896773638…
7/7 passed
```

**The companion demonstration**, required by `PATTERN_ALREADY_SOLVED_GATE` variant 3 — *a green
suite is evidence only if the environment it ran in is capable of exhibiting the defect*. The same
suite, run unchanged against the **pre-fix** script:

```
2/7 passed
  FAIL  test_rule_comes_from_the_tip_not_the_working_tree
  FAIL  test_hash_is_branch_independent — 'a6ca8ee7…' vs '5081c7cf…'
  FAIL  test_dirty_working_tree_does_not_move_the_hash
  FAIL  test_missing_rule_at_tip_fails_explicitly — fell back instead of refusing
  PASS  test_determinism_across_runs
```

The one that passes on both is the one that could never have caught this: running twice from the
same checkout was always stable. That row is worth keeping precisely because it shows what a
determinism test looks like when it is measuring the wrong invariant.

---

## 5 · CHANGE_CLASS: MAJOR

The script implements the definition `Annex D.2` delegates to `§ P5`, and `gate 5` binds every
approval to its output. A change to how a candidate's identity is computed is a gate-model change,
and body §12 resolves a doubtful classification to MAJOR fail-closed. The small diff is not
evidence of a small blast radius.

---

## 6 · Scope — what is deliberately absent

| Excluded | Why |
|---|---|
| `CAND-20260817-P51C9` | held PENDING, unmodified, per operator instruction |
| `CAND-20260817-ORCHWT` | same |
| `runtime/` classification | open against C-9 §7.2; not this candidate's question |
| SLR integration | awaits Mirror's E.2 curation |
| `legend_lint.py` | Mirror classified lint expansion as a future candidate (N-5) |
| `plan_defined_parameters.md` | **the rule itself is untouched.** This candidate changes only how the rule is *read* |

That last row is the load-bearing one: fixing a reader by editing what it reads would have put the
change inside P51C9's content and rehashed a candidate under review.

---

## 7 · Execution ordering

`HASHDET` should execute **first** among the three. It changes how every subsequent candidate's
identity is computed, and executing it after the others would mean their approvals were bound by a
recipe that is being replaced. Executing it first costs nothing: it validates the other two
without altering them (§3.1), so neither needs re-hashing on its account — only the ordinary
re-base that any candidate needs once another has moved `main`.

Recommended: `HASHDET` → `ORCHWT` → `P51C9`. Plan recommends; the operator and Orchestrator decide.

---

## 8 · Verification record

| Check | Command | Result |
|---|---|---|
| Candidate hash | published command, twice | identical `c85acdb2…ad05d8` |
| Record consistency | grep every hash and count in this document | one current value per site; superseded values labelled as such |
| Determinism suite | `test_candidate_content_hash.py` | **7/7 PASS** |
| Suite can fail | same suite vs the pre-fix script | **2/7** — 5 failures, the defect exhibited |
| Emitted domain | `--emit-domain \| shasum -a 256` | equals the candidate hash |
| Historical replay | approved `GOV311`, base `749a9a9b`, tip `9720a0cd` | `c39ecae8…30c239`, matches the approved value |
| Both pending hashes reproduce | from `hash-determinism`, a third branch | `280dc497…` and `f325bd9d…`, matching their manifests |
| No residual working-tree read | `grep PARAMETERS` | only the tip-scoped `git show` |
| Structural LINT | `legend_lint.py .` | `PASS` |
| Publication gate | `public_release_gate.py` | `PASS`, `BLOCKS: 0` |
| No history rewritten | branch from `main`, single commit | no rebase, amend or force push |

**NO CANONICAL_BATCH_COMMIT EXECUTED.** Preparation only. `GATE 0` still cannot pass: root not
clean, no lease, L2 suspended.
