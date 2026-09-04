# CHK-orchestrator-0002 — a mode-only commit moves `CANDIDATE_CONTENT_HASH`

Recorded 2026-09-04 at HEAD `66b1526`, during TASK-0B-ENTRY. Found by measuring something
that was supposed to be a no-op check, and it contradicted the inference that preceded it.

## The measurement

`66b1526` changes three file modes and nothing else:

```
$ git diff --stat 6459bf8 66b1526
 governance/scripts/candidate_content_hash.py      | 0
 governance/scripts/governance_fingerprint.py      | 0
 governance/scripts/test_candidate_content_hash.py | 0
 3 files changed, 0 insertions(+), 0 deletions(-)

$ git diff 6459bf8 66b1526
 old mode 100644
 new mode 100755      (×3)
```

The candidate content hash over the same base moves:

```
57c0f25..6459bf8  f9951607d032448d824d2376d24112cb09423be82c73e38604c8adbeb9bf8e21
57c0f25..66b1526  a32edb7d80baa48a4fc5955ee66ce354934bdb9c2ca3c33be76acd6902be6644
```

Zero insertions, zero deletions, and the only delta between the two tips is three mode
bits. So **the hash is mode-sensitive**, and that is measured rather than argued.

## The inference it corrected

Before making the change I grepped `candidate_content_hash.py` for `mode`, `st_mode`,
`100644`, `ls-files` and `hash_object`, got nothing, and concluded modes were not part of
the hashed domain. That conclusion was wrong. The grep was over the vocabulary I expected
the mechanism to use, and the mechanism uses a different one.

`domain()` at `:101` keeps the WHOLE `git ls-tree -r --full-tree` line:

```
<mode> SP <type> SP <sha> TAB <path>
```

and `serialize_domain` concatenates those lines verbatim. The mode is the first field of
every entry, so it is inside the hashed bytes by construction — without the word "mode"
appearing anywhere in the file.

There is a second, softer error worth naming: the first "after" measurement I took was
against `--tip HEAD` while the change was still only STAGED, so it hashed the same tree as
the "before" and agreed with it perfectly. An unchanged hash there was evidence of nothing.
The comparison only became a measurement once the change was committed and the two tips
genuinely differed.

## What follows, and what does not

The behaviour is defensible: a tree identity that ignored modes would call two trees
identical when one ships an executable and the other does not. The name is what misleads —
it is a TREE hash, and "content hash" reads as content-only.

The consequence is real for this laboratory. `test_release_surface.py` requires every
tracked `#!` file to be executable, so satisfying it is necessarily a mode change, and
every such repair rotates the governance candidate fixed point even though no reviewable
content moved. That is the shape `PLAN-MODULAR-EVOLUTION-001` §M6 already lists as a
DE-PIN candidate — a mutable property defining candidate identity — reached here from a
different direction.

**Not repaired, deliberately.** Changing what the domain hashes would move every candidate
hash ever recorded, and the definition is published as a recipe any implementation can
rebuild. That is a change to a fundamental guarantee under §21d's RESERVED list. This
checkpoint records it; it does not act on it.

## The task's own result

`test_release_surface.py` was one of the eight suites red at the 57c0f25 baseline. In a
fresh clone at `66b1526` it is green:

```
$ git clone --local . fresh2 && cd fresh2 && python3 scripts/test_release_surface.py
Ran 10 tests in 0.157s
OK
```

Measured in a clone, not in this working tree — the local tree still shows the mode residue
of 4ec79ce, which `chmod` cannot repair at this authority and which no clone inherits.
