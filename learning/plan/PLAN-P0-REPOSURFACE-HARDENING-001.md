---
record_type: WORK_ANALYSIS
id: PLAN-P0-REPOSURFACE-HARDENING-001
title: One repair of three call sites left the bypass live, and one population was answering two questions
date: 2026-08-26
role: PRODUCER
mode: EXECUTABLE HARDENING / INTEGRATION ENGINEERING
authority: Plan role contract — candidate preparation on own branches. No CANONICAL_BATCH_COMMIT.
  No H.1 decision selected. No governance text amended. No event emitted. The control-plane
  relevance set is REDUCED here and NOT chosen.
status: REPOSURFACE hardened · one new candidate · relevance fork reduced to a single question
---

# P0 REPOSURFACE HARDENING

> **Nothing here is medical advice.** Tooling, control plane and integration shape only.

---

## 1 · 🔴 REPOSURFACE was one repair of three call sites

The candidate as reviewed repaired `walk_publishable`. `is_nested_checkout` gained optional
`root`/`tracked` parameters, and its own docstring said why: *"so existing callers keep working"*.

**There are two other callers, and both call the one-argument form.**

| Caller | What it walks |
|---|---|
| `test_link_targets.markdown_files` | markdown of this checkout, gitignored files included on purpose |
| `test_release_surface.walk_this_checkout` | every file of this checkout, for the ignore audit |

Measured on the candidate branch `d3c4b2a`, with **one untracked line** written to
`governance/.git`, at the level of the test that owns each guard:

```
test_release_surface  ReleaseSurfaceTests.test_no_public_file_is_silently_gitignored
    without the marker   FAILED (failures=1)        with the marker   OK
test_link_targets     LinkTargetTests.test_markdown_fragments_resolve_to_headings
    without the marker   FAILED (failures=1)        with the marker   OK
```

and at the level of the population underneath:

```
unexpectedly_ignored_files()   ['governance/notes_private_draft.md']  ->  []
markdown collected                                  282  ->  246
governance markdown                                  36  ->    0
walk_this_checkout                                 3601  -> 3562
```

**Identical on `main` and on the candidate.** "Existing callers keep working" meant "existing
callers keep the bypass".

⚠️ **My first attempt to demonstrate this was wrong and I nearly reported it as a null result.**
I ran the whole suites, saw `test_release_surface` red on both arms, and would have concluded
there was no bypass. It was red for an unrelated inherited reason — the four `100644` shebang
files RELSURF owns. **A suite verdict is the wrong instrument for a per-check bypass.** Only
isolating the owning test method, and the function under it, produced the measurement above.

**Repair.** `root` and `tracked` are now **required**. A caller that cannot name the repository
it is pruning for has not decided what it is asking, and a `TypeError` says so where a wrong
boolean would not. All three call sites pay one `git ls-files` for the whole walk.

---

## 2 · The hostile matrix — MAIN against the candidate

Nineteen fixtures, each built on a pristine clone of `788c357d`. Population is publishable
markdown; `planted_detected` is whether the specific planted violation was reported, which is
not the same question as the verdict.

| Fixture | MAIN | CANDIDATE |
|---|---|---|
| untracked `.git` **file** in a tracked directory | 246 md · **PASS** | 281 md · BLOCK |
| `.git` **directory** | 246 md · **PASS** | 281 md · BLOCK |
| **empty** `.git` file | 246 md · **PASS** | 281 md · BLOCK |
| `.git` **symlink that resolves** | 246 md · **PASS** | 281 md · BLOCK |
| `.GIT` **case variant** (case-insensitive fs) | 246 md · **PASS** | 281 md · BLOCK |
| marker on a **second** tracked directory (`roles/`) | 277 md · **PASS** | 281 md · BLOCK |
| real `git init` **on top of tracked content** | 246 md · **PASS** | 282 md · BLOCK |
| marker one level deeper (`framework/protocols/`) | 265 md · BLOCK, **planted violation NOT detected** | 281 md · BLOCK, detected |
| `.git` **dangling** symlink | 281 md · BLOCK | 281 md · BLOCK |
| tracked file committed then **deleted from disk** | 280 md · BLOCK, **planted NOT detected** | 280 md · BLOCK, **planted NOT detected** |
| tracked directory **renamed aside** | 281 md · BLOCK, detected | 281 md · BLOCK, detected |

**`PUBLICATION_BYPASS_FALSE_PASS_COUNT` on `main`: 7.** Seven distinct filesystem objects, one
name, and each of them turned `BLOCK_PUBLICATION` into `PASS`.

🔴 **The deeper marker is worse than a PASS, not better.** Pruning `framework/protocols/` removed
the document holding the planted violation *and* removed the targets of wikilinks pointing into
it, so `main` reported **four BROKEN_WIKILINKs that do not exist** while missing the one that
does. A gate that fabricates findings while suppressing the real one is harder to distrust than
one that says PASS.

### Negative controls — the repair must not stop pruning

| Control | MAIN | CANDIDATE |
|---|---|---|
| real nested **repository** under `vendor/` | 281 md, pruned | 281 md, pruned |
| real nested **worktree**, gitignored path | 281 md, pruned | 281 md, pruned |
| real nested worktree, **un-ignored** path | 281 md, pruned | 281 md, pruned |
| vendored untracked tree, **no** `.git` | 282 md, scanned | 282 md, scanned |
| local ignored material (`tmp/`) | 281 md, excluded | 281 md, excluded |
| **force-added** gitignored file | 282 md, scanned | 282 md, scanned |
| clean tree | 281 md, PASS | 281 md, PASS |

Every control holds. The predicate did not become "never prune".

### The one behaviour that deliberately changed

`git init` inside `governance/` makes it a genuine checkout **and** leaves 35 tracked documents
underneath. The predicate resolves that in favour of the tracked content: the 35 stay, and the
intruder's own untracked file is scanned too (`EMAIL_ADDRESS`, correctly). **Over-scanning is
noisy and visible; the alternative loses 35 governance documents silently**, which is where this
whole thread started. Stated as a decision, and asserted by a test, so it is not an accident.

---

## 3 · PUBLISHABLE and DOCUMENTATION are not one question

The queue asked whether the two populations have identical semantics. **They do not, and the
first repair forced one helper to serve both.**

```
clean checkout of 788c357d   publishable 281  ·  tracked 281  ·  SET-EQUAL, not merely equal counts
untracked, not ignored .md   publishable 282  ·  tracked 281
tracked document deleted     publishable 280  ·  tracked 281
```

| | PUBLISHABLE | DOCUMENTATION |
|---|---|---|
| question | what could leak from here | what a reader of a clone holds |
| asked of | the **disk** | the **index** |
| bias | over-inclusive on purpose — a missed finding is a published breach | exact — a promise is carried by what ships |
| untracked scratch file | scanned (one commit from shipping) | **must not** turn the guard red |
| tracked file deleted locally | nothing on disk to leak | **must not** leave the population |

They coincide on a clean tree, which is exactly why reuse looked adequate. They separate under
precisely the local filesystem state a guard has to be immune to. `test_documented_commands` now
takes `tracked_documents(ROOT)` — `git ls-files` — and **no working-tree action can move that
population**: not a stray marker, not a deletion, not a scratch file, not a rename.

🔴 **`tracked_documents` refuses an empty answer rather than returning one.** My own test caught
this: outside a repository the index is empty, and a documentation guard handed an empty
population checks nothing and exits 0. That is the vacuous pass `test_release_surface` already
names in `test_an_empty_index_is_a_refusal_not_a_pass`, arriving through a second door.

### A residual, stated rather than engineered away

The **F07** row above: a violation committed to `HEAD` and then deleted from the working tree is
missed by both arms of the publishable gate. It is not unbounded — `git status --porcelain`
reports a deletion, so `--mode release` blocks on `DIRTY_RELEASE_TREE`, and the `git archive`
arm scans `HEAD` regardless. **The default documented invocation is `--mode staging`, which runs
neither.** Recorded as a bounded gap in the working-tree arm, not repaired here.

By contrast a stray `.git` file is **not** reported by `git status` at all — measured — so it
never made the tree dirty and never reached either compensating arm.

---

## 4 · `tracked_paths` — two failure modes on one sentinel, twice

| Draft | Failure answer | What broke |
|---|---|---|
| first | `frozenset()` always | "tracks nothing" is the *pruning* answer: a tool that could not run git pruned more, silently |
| second | `None` always | broke two green controls whose fixtures mount a real nested checkout inside a temp directory that is **not** a repository |
| now | `frozenset()` when not inside a work tree · `None` when inside one and the index is unreadable | — |

Outside a repository there is no outer index, so "the outer index claims nothing inside this
subdirectory" is simply **true**, and pruning is right. Inside one with an unreadable index the
question was **asked and not answered**, and pruning on that is the original defect. **Absence of
an index is not absence of an answer**, and I compressed them onto one sentinel twice — once in
each direction — before separating them.

---

## 5 · My own errors this session

| Error | How it surfaced | Correction |
|---|---|---|
| Ran whole suites to detect a per-check bypass; both arms red for an unrelated reason | would have reported "no bypass found" | isolate the owning test method and the function under it |
| `tracked_paths` returning `None` on every failure | two previously-green controls turned red | separate not-a-repository from index-unreadable |
| `test_an_unreadable_index_never_prunes` **passed against the code it was written to refute** | the negative arm against `d3c4b2a` said `OK` | the fixture asked about a path with no `.git`, so the predicate returned on its first line — a vacuous pass inside the file whose subject is vacuous passes. It now asserts the fixture is capable of failing first |
| `mode_bit_offenders` read every blob as text | `UnicodeDecodeError: byte 0x89` nine minutes into a ten-step run, on the first PNG | read bytes through one `cat-file --batch`; committed as a fixture |
| `EveryShapeOfTheSameMarker` claimed as evidence for the **hardening** | all five pass against `d3c4b2a` | their negative arm is `main` (5 failures), not the pre-hardening candidate. Recorded so the two arms are not conflated |

---

## 6 · Both arms, per test class

| Class | vs `main` | vs `d3c4b2a` (pre-hardening) | on `299492b` |
|---|---|---|---|
| `EveryShapeOfTheSameMarker` | **5 failures** | OK — already repaired there | OK |
| `TheMarkerCannotEmptyTheGuardsThatMerelyImportThePredicate` | 2 failures | **2 failures** | OK |
| `ThePredicateRequiresTheRepositoryItIsPruningFor` | 1 failure, 4 errors | **2 failures, 1 error** | OK |
| `TheTwoPopulationsAreNotOneQuestion` | import error (`tracked_documents` absent) | import error | OK |

**25 tests in the file, all green on the hardened tip.** The fixture checks out `HEAD`, not the
working copy — deliberately, so every assertion is about a reviewable object — which cost one
diagnosis when three tests read as failing against a working tree that already held the fix.

---

## 7 · Candidate state

`plan-repo-surface-determinism` — `d3c4b2a` → **`299492b`**, six files.

| | before | after |
|---|---|---|
| `CANDIDATE_CONTENT_HASH` | `16241562…9eaddb968` | **`e5ac47e2…292b73ec`** |
| files touched | 4 | 6 (`test_link_targets.py`, `test_release_surface.py` added) |
| new conflicts with other candidates | — | **none**: no other candidate touches either file |

Any review of `d3c4b2a` is invalidated. The eight other candidate hashes are unchanged.
