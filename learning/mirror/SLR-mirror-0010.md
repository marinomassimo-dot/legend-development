---
artifact: MIRROR Session Learning Review (body §15, Annex E.6)
record_id: SLR-mirror-0010
actor_id: mirror
subject: review of CAND-20260818-SCIENTIST-AB-SPEC revision 2 — a remedy that moves the comparison one level up, and the level below it
review: reviews/mirror/REV-SCIAB-MIRROR-002.md
date: 2026-08-19
outcome: FAILURE_PATTERN (×2, both replications) · BEST_PRACTICE_CONFIRMATION (×1, second sighting) · MICRO_UPGRADE (×1)
derived_from: [SLR-mirror-0009, CLASS-P51-REVIEWS-LEARNING-001]
---

# The unit of comparison moved, and the defect moved with it

## 1 · FAILURE_PATTERN — a set of the wrong objects is still a set

Revision 1's `B-2` was *"the claim of equality was a count; a count is not falsifiable"*. Revision 2
answered it exactly: it enumerated both failure **sets** and wrote them into the manifest. The sets
are identical, and the delta is still not zero — because the set is of **suite names**, and one of
those suites is already red and absorbed a new failing test without changing its name.

The generalisation, and it is not the one I would have written yesterday: **the remedy for "a count
is not falsifiable" is not "an enumerated set". It is "an enumerated set of the objects the claim
is about."** A claim about regressions is about tests. A claim about coverage is about units. A set
of containers is a count wearing a list.

`REPLICATION` of the pattern already on file (`peer-agreement-is-not-a-second-quantity`,
`SLR-mirror-0009` §1), on a new object and one level up. It now has three sightings and I think the
rule is ready for promotion (E.3): *state the granularity of a comparison beside its result, and
make it the granularity the claim is about.*

## 2 · FAILURE_PATTERN — a computed blind spot is only as complete as the keys it reads

The candidate did the right thing structurally: it stopped *asserting* the blind spot and started
*computing* it, as the intersection of two spec keys, printed on every run. That is strictly better
than a comment. And it is still incomplete, because the exemption it models lives in **two** keys —
`expected_output_paths` and `expected_output_prefixes` — and the computation reads one.

This is `CONTROL_SPECIFICITY_RULE` again, arriving from a third direction. Revision 1: a fixed
window bounded the wrong axis. Revision 2's population fixed that. Revision 2's blind spot then
bounded the right axis over the wrong domain. **Ask not only "is this computed rather than
asserted" but "over what domain is it computed, and is that the domain of the thing it claims to
bound".** A derived number inherits the incompleteness of its inputs and looks authoritative while
doing it.

## 3 · BEST_PRACTICE_CONFIRMATION — one probe per clause of the PASS sentence, second sighting

`SLR-mirror-0009` §4 proposed this as a candidate practice needing a second confirmation before
promotion. This session is that confirmation, and it is a strong one: the candidate **adopted the
method** — its own 45-test suite is built on it and its docstrings say so — and the method still
found the two things the suite does not test, by the same route. I took the guarantee table of
`controlled_benchmark_ab.md` §4.3 clause by clause and built the cheapest state that falsifies each.
Twelve clauses held. The clause *"nothing outside the allowlist and the declared output set is
present"* did not, and the falsifying state was a file copy.

**Promotable (E.3):** *for any validator, take its PASS sentence and its guarantee table clause by
clause and construct the cheapest state that makes each clause false while the instrument still
prints it. A clause with no probe behind it is a clause nobody has tested.*

## 4 · MICRO_UPGRADE — assert the reason, or the harness lies to you first

My own B-4 battery reported **13 of 13 caught** on its first run. Every one was `rc=2`, and `rc=2`
is this tool's *refusal* code: I had passed `--out` where the command takes `--surfaces`, and
argparse rejected the unknown flag before any check ran. Had I asserted only `returncode != 0` — the
obvious way to write it — I would have reported that every hostile case was detected, in a review
whose §12 mandate was specifically to hunt for tests that pass for the wrong reason. The harness
committed the exact defect it was built to find, in its first execution.

It did not survive one turn, and only because every case carried an expected **reason string**
beside its expected exit code, so all thirteen reported `reason ABSENT` instead of `PASS`.

**Rule I am adopting for every hostile battery I write from now on:** an expected exit code is never
sufficient; every case declares the reason token it must see, and a case that exits non-zero without
its token is a FAIL of the harness, not a PASS of the target. And the first thing a battery prints is
its positive control — if the honest case does not come back clean, nothing below it means anything.

This also sharpens what I can say about Plan's two declared-spurious tests. They assert
`assertEqual(2, returncode)` and `assertNotEqual(0, returncode)` with no reason, which is exactly the
shape my harness had. Plan found and declared them without being asked. I verified independently that
both fire for the right reason against the fixed tool, so neither is load-bearing — but the honest
reading is that the author caught in its own suite the mistake I then made in my instrument.

## 5 · What did not go wrong, recorded because it is the metric that matters

- Rehydration fail-closed invented nothing: no SESSION_REF, no inherited attestation, and no PASS
  carried across from `REV-SCIAB-MIRROR-001` — including the ten rows that review found acceptable,
  every one of which was re-tested here.
- The stale-worktree trap was caught before it became a finding. Run in `mirror`'s own worktree the
  candidate hash comes out `02231e82…`, because this branch carries P5 v3 and the pre-fix hash
  script. Reporting that as a binding divergence would have been a false BLOCKING finding against
  the candidate for a defect that is mine. The control: compute in a clean detached worktree of
  `BASE_HEAD`, and check the script and the rule are the ones the tip carries. `R-10` is now two
  reviews old and has cost measurement time twice.
- The regression environment was controlled before the numbers were read: the two regression
  worktrees hold no `files/` at either tip, so the `test_surface_census` confound of `SLR-mirror-0009`
  §3 could not recur. It did not.
- The session guard refused two heredoc writes while the shell was inside a repository worktree. I
  did not reach for the unchecked tool: the probe scripts were authored with `Write` into the
  scratchpad and invoked by name, and the measurements are identical.
  (`never-bypass-a-guard-with-a-different-tool`, applied — third time on file.)
- Nothing under `lettore`, `lettore-b`, `lettore-c`, `evidence-index`, `orchestrator` or root was
  written; the packet was copied out of root read-only and its seven digests matched the manifest.

## 6 · Boundary of this record

I could not reproduce Plan's differential counts (41 ran / 9 pass / 7 genuine against my 45 / 14 /
12). I infer a `setUpClass` abort collapsing a five-test class — the arithmetic fits exactly — but I
did not observe it, and it is recorded as inferred. Time is date-only; no wall clock was available.
The exposure behind M-2 is bounded by a residual the candidate itself declares under J.0, and I have
said so in the finding rather than letting the blocking classification imply more than it should.
