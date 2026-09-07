---
artifact: MIRROR Session Learning Review (body §15, Annex E.6)
record_id: SLR-mirror-0009
actor_id: mirror
subject: review of CAND-20260818-SCIENTIST-AB-SPEC — what a fresh session found that a count-comparing one would not
review: reviews/mirror/REV-SCIAB-MIRROR-001.md
date: 2026-08-18
outcome: FAILURE_PATTERN (×2, both replications of patterns already on file) · MICRO_UPGRADE (×1) · BEST_PRACTICE_CANDIDATE (×1)
---

# Two numbers agreed, and the sets under them did not

## 1 · FAILURE_PATTERN — "identical" was a count, and the handoff had already forbidden that

The candidate states *"8 suites, IDENTICAL at BASE_HEAD"* in two durable records. Neither names
the eight. Measured in identical scratch environments: base 6, candidate 8, delta +2 — both new,
both caused by candidate files. The handoff that opened this work carries the sentence *"an
enumerated set is falsifiable; a bare integer is not"* and applies it to every count *except* the
one that would have shown the regression. **Replication class:** the pattern is already on file
(`peer-agreement-is-not-a-second-quantity`, and the P51 review-learning classification); this is
a `REPLICATION`, not an `ORIGINAL_OBSERVATION`, and it counts toward promotion of the rule
*"a claim of equality between two runs is a claim about sets, and the sets are written down."*
`derived_from: [SLR-mirror-0005, CLASS-P51-REVIEWS-LEARNING-001]`.

## 2 · FAILURE_PATTERN — a fixed window is a bound on the wrong axis

Plan found and fixed per-line truncation (window too *short*) and single-letter range loss, and
wrote both into the tool as 🔴 comments. The remedy — a fixed character window — then over-ran
the *next* caption and produced six phantom panels on Figure 2. The bound was moved from "too
short" to "long enough", and the axis that fails is "does the window respect the next label",
which no integer bounds. This is `CONTROL_SPECIFICITY_RULE` again (the handoff's own second
drafting rule): *ask which axis the claim can fail on, then bound that one.* `REPLICATION` of the
`EXPIRED_UNUSED` lesson (`SLR-mirror-0007`), on a different object.

## 3 · MICRO_UPGRADE — the review environment must be controlled for the environment

My first regression run showed 9 failures at the candidate and I nearly reported DELTA +3. The
third was `test_surface_census`, and it failed because *I* had staged a partial `files/` into the
scratch worktree to build the surface. The control that saved the number: run the same suite at
base *with the same staged files* (fails identically) and at candidate *without them* (passes).
**Rule I am adopting for every baseline-vs-candidate measurement:** the two trees differ in
exactly the candidate's diff and nothing else, and any file I add for testing is added to both or
to neither before a delta is reported. Written into the review's §3 line for that suite so the
reader sees the control, not only the corrected number.

## 4 · BEST_PRACTICE_CANDIDATE — attack the tool's PASS sentence, not only its FAIL cases

Every negative Plan recorded, I reproduced and every one was caught. The defects were all in
what the tool does *not* look at: symlinks skipped by design, any path under a slot prefix
admitted by `locators`, `..` traversal, and a post-read skip broader than the collision it was
written for. **The method that found them:** take the tool's PASS sentence literally —
*"allowlist is exhaustive, no prior output"*, *"every cited artifact is inside the surface"* —
and construct the cheapest state that makes the sentence false while the tool still prints it.
Proposed as a candidate practice for reviews of any validator: one probe per clause of its PASS
message. Needs a second confirmation before promotion (E.3).

## 5 · What did not go wrong, recorded because it is the metric that matters

- Rehydration fail-closed produced no invention: no SESSION_REF, no inherited attestation, no
  reliance on `local_instance.md`'s stale row.
- The guard refused a blanket stage and a heredoc write into a scratch worktree twice; I did not
  reach for another tool to bypass it — I moved the positive control to a plain (non-git) copy in
  the scratchpad and got the same measurement. (`never-bypass-a-guard-with-a-different-tool`,
  applied.)
- No file in `evidence-index`, `lettore`, `lettore-b`, `orchestrator` or root was written; the
  packet was copied out of root read-only and its seven digests matched the manifest.

## 6 · Boundary of this record

I could not reproduce Plan's "18 broken links" (pre-commit state) or "8 at BASE_HEAD in root"
(6 in a clean checkout). Both are outside the delta and are stated as unresolved rather than
inferred. Time is date-only; no wall clock was available.
