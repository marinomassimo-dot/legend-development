---
record_type: WORK_ANALYSIS
id: PLAN-INTEGRATION-TOOLING-DURABILITY-001
title: A tool about nine candidates cannot live inside one of them, and a shorter failure list is not better news
date: 2026-08-26
role: PRODUCER
mode: EXECUTABLE HARDENING / INTEGRATION ENGINEERING
authority: Plan role contract — candidate preparation on own branches. The tool deposited here
  holds NO governance authority: it selects nothing, orders nothing, ratifies nothing and emits
  no event. No CANONICAL_BATCH_COMMIT.
status: tenth candidate · 17 tests · composed matrix over ten candidates at current hashes
---

# INTEGRATION TOOLING — DURABILITY AND PLACEMENT

> **Nothing here is medical advice.**

---

## 1 · The problem the scratchpad was hiding

The composition matrix and the union resolver had been rebuilt from scratch in three separate
sessions and thrown away three times. Each rebuild re-derived the same properties and re-made
some of the same mistakes. **They were the one piece of critical evidence that was never
durable**, and the stated reason was correct: they operate *across* candidate branches, so
committing them into one candidate would make that candidate's acceptance carry a tool about the
other nine.

That is an argument against a **home**, not against **durability**. The answer is a candidate of
its own.

## 2 · Placement, and why the alternatives are worse

`integration_matrix.py` under `framework/scripts/` on `plan-integration-matrix`, based on
`788c357d`. That branch is unmerged, so the file is reachable there and in no other tree.

| Candidate home | Why not |
|---|---|
| inside one repair's branch | the ownership fiction the queue forbids — nine candidates measured by a tool one of them ships |
| `governance/scripts/` | that directory is where governance tooling lives, and its neighbours (`governance_fingerprint.py`, `candidate_content_hash.py`) are consulted *by* governance. A composition simulator placed there reads as authority it does not have |
| `scripts/` | the public-release battery. This is not a release gate: it never runs on a published clone and answers nothing about publishability |
| **`framework/scripts/`** | ✅ CLAUDE.md calls `framework/` "the generic engine". It already holds every multi-agent runtime primitive — `lease_state.py`, `lease_singleton.py`, `control_plane_probe.py`, `event_ledger.py`, `repo_root.py` — all of them role-neutral, none of them normative. The tool is one more of those |

**`plan-integration-matrix` is a candidate like the other nine**: one base head, one content hash,
independently reviewable, and it repairs nothing anybody else is repairing.

## 3 · The contract, and what is deliberately absent

| Requirement | How |
|---|---|
| no governance authority | selects no candidates, chooses no order, ratifies no merge, emits no event |
| no candidate-specific ownership | its own branch; measures properties of the **composition**, which belong to no repair |
| deterministic order simulation | base and ordered candidate list are **required arguments**. Two orders of one set are two reports, and it produces both |
| runner-entry loss | `--list` count per prefix step |
| duplicate enrolment | the same suite twice — the signature of a union resolution that ran twice |
| mode-bit loss | tracked `100644` files whose blob starts `#!`, read from the **index** |
| unexpected failure disappearance | see § 4 |
| new failures | failing here, not at the previous step |
| candidate identity | tip SHA read before and after; supplied `CANDIDATE_CONTENT_HASH` carried verbatim; the simulation runs on a throwaway branch in a throwaway worktree |

🔴 **Every input that could constitute a decision is required on the command line.** The same
discipline `lease_singleton.py` holds: a tool that discovered its own inputs would be answering
the question it exists to inform.

## 4 · 🔴 `unexplained_vanishings` — the finding the tool exists for

**A failure that disappears is not good news by default.** A suite dropped from the runner by a
bad merge disappears from the failure list in exactly the same way as a suite that was repaired:
the list gets shorter, and nothing distinguishes the two.

The tool cannot infer what a candidate *meant* to fix, and inferring it would be the ownership
fiction again. So the declaration is an **input**: `--declares REF=SUITE[,SUITE]`. With none
supplied, **every** vanishing is reported unexplained — noisy on purpose, and fail-closed.

Both arms are fixtures:

```
a branch that DROPS suite_b from the inventory   -> VANISHED-UNEXPLAINED, exit 1
a branch that REPAIRS suite_b, declared          -> vanished, no finding,  exit 0
the same repair, UNDECLARED                      -> VANISHED-UNEXPLAINED, exit 1
```

The third exists so the second is answered by the declaration and not by the branch.

## 5 · Union is refused where it would destroy

The only automated resolution is a conflict in which **both sides only added lines**. Safety is
read from git's stages 1/2/3, not from the marked-up file — the working copy no longer contains
the merge base, and a union that cannot see the base cannot know what it is resurrecting.

```
two pure additions to the runner       -> union, 4 entries, 0 duplicates
one side deletes a line                -> SIMULATION_REFUSED, exit 3, no branch left behind
```

## 6 · My own errors building it

| Error | How it surfaced | Correction |
|---|---|---|
| every 100644 blob read as **text** | `UnicodeDecodeError: byte 0x89 in position 0` — a PNG — **nine minutes into a ten-step run** | one `cat-file --batch` in bytes; committed as a fixture. It failed closed, which is right, and still cost a whole measurement. A repository check that assumes its own repository is all text has not met one |
| the stub runner carried a shebang at `100644` | every fixture inherited a mode-bit finding it never caused | `chmod 0o755` in the fixture; a defect of the fixture reading as a defect of the tool |
| `drops_a_suite` branched from the base | it conflicted on the runner, the union guard refused it, and the test measured the **refusal** instead of the loss | branch it from its predecessor so the loss arrives through a clean merge |
| **I nearly filed a defect against `candidate_content_hash.py`** | the hash looked unchanged across two tips that differ by two files | 🔴 **The tool was right and I had mis-sequenced my own commands.** Re-derived: the domain listing is not byte-identical between the tips (`integration_matrix.py` `6805764c` → `5155e5e1`), and the domain hashes to `e7c4dec4…` at `66f0546` and `2df0ce95…` at `4149901`. The value I had recorded was always the second one. **The positive control is that the hash moved with the content**, and I checked that before saying anything |

---

## 7 · 🔴 The tool committed its own headline finding, and a real run exposed it

The first ten-candidate run over the real repository produced this:

```
PREFIX STEP                          RUNNER  DUP  MODE  FAILS  CONFLICT  NEW / VANISHED
plan-repo-surface-determinism            66    0     4      0  clean     (baseline)
plan-release-surface-repair              67    0     0      0  clean     none
...
plan-major2-restricted-repair            76    0     0      0  clean     none
```

**`FAILS 0` at all ten steps** — and the isolated battery on the very first of those candidates
reports **six**. The runner writes 1925 lines of test output to **stdout** and its verdict —
`REGRESSION VERDICT: FAIL` and one `- suite: exit N` line per failure — to **stderr**. The first
version read stdout only.

That is § 4's finding, inside the function that reports § 4's finding: **an empty failure list
because the check stopped being read, indistinguishable from an empty failure list because
everything passed.** The runner-entry and mode-bit columns were correct throughout — 66 → 76, and
4 offenders cleared by RELSURF — which is what made the table look healthy.

**Seventeen passing tests said nothing about it**, because every fixture's stub runner printed to
stdout. *The tested surface and the defective surface were disjoint* — the same shape as the
approval-queue CLI whose 27 tests never called `main()`, and as the adjudication script whose
every fail-open state lived in the one function its suite never ran. **Third occurrence, same
mechanism, this time in a tool written to catch it.**

Two repairs, and the second is the one that outlives this particular mistake:

1. both streams are read;
2. **the exit code and the parsed list must agree.** A non-zero exit naming no suite, or a zero
   exit naming one, is `SIMULATION_REFUSED` rather than a number.

Three fixtures, all arms:

```
a runner that reports on stderr                    -> failures = ['suite_b.py']
a runner that fails and says nothing               -> exit 3, "named no failing suite"
a runner that genuinely passes                     -> failures = [], exit 0
```

The third exists because the first two are satisfied by a tool that refuses everything.

**20 tests.** Reading both streams fixes today's runner; refusing a verdict that disagrees with
its own list is what catches the next one.

---

## 8 · The composed P0 matrix, at current hashes

`BASE 788c357d`, ten candidates, order chosen for **earliest trustworthy detection** and not for
fewest conflicts. Composed tip `630731cc`. **Candidate identity preserved: every tip identical
before and after.**

| Prefix step | runner | dup | mode-bit | fails | conflict | movement |
|---|:--:|:--:|:--:|:--:|---|---|
| `REPOSURFACE` | 66 | 0 | **4** | **6** | clean | *(baseline)* |
| + `RELSURF` | 67 | 0 | **0** | **4** | clean | VANISHED ×2, **both declared** |
| + `CPROOT` | 68 | 0 | 0 | 4 | union | none |
| + `LEASESINGLETON` | 69 | 0 | 0 | 4 | union | none |
| + `GOVTESTS` | 71 | 0 | 0 | 4 | union | none |
| + `ADJFAILCLOSED` | 72 | 0 | 0 | 4 | union | none |
| + `P7LEDGER` | 73 | 0 | 0 | 4 | union | none |
| + `APQCONS` | 75 | 0 | 0 | 4 | union | none |
| + `INTMATRIX` | 76 | 0 | 0 | 4 | clean | none |
| + `ORCHMAJOR2` | 76 | 0 | 0 | 4 | clean | none |

**Zero duplicate enrolments and zero new failures at every step.** Runner entries 65 → **76**.
The only conflicts are on `scripts/run_release_regressions.py`, six of them, every one a
pure-addition union that passed the base-stage safety check.

### Why REPOSURFACE first, and what it bought

Not fewer conflicts — it is clean either way. **Every later measurement is taken through a walker
that cannot lose files.** The baseline step immediately surfaces the four `100644` shebang files
inherited from `main`, and the next step clears them:

```
step 1  framework/scripts/lease_state.py · governance/scripts/candidate_content_hash.py
        governance/scripts/governance_fingerprint.py · governance/scripts/test_candidate_content_hash.py
step 2  none
```

### The two vanishings, and why they are not findings

```
scripts/test_release_runner_verdict.py    declared by RELSURF
scripts/test_release_surface.py           declared by RELSURF
```

Both were supplied as `--declares`. **Undeclared, the same two would have been reported
`VANISHED-UNEXPLAINED` and the run would have exited 1** — which is the point: the tool does not
decide that a shorter list is good news, it asks who claimed it.

### The four that never move

```
scripts/test_locator_obligation_reaches_every_route.py   'verbatim_locators'        not in CLAUDE.md
scripts/test_abstract_corpus_is_not_evidence.py          'pubmed_corpus_harvest'    not in CLAUDE.md
scripts/test_fulltext_trace_contract.py                  'FULLTEXT_READ_RECEIPT'    not in CLAUDE.md
framework/scripts/test_session_self_eval.py              'session_self_evaluation.md' not in CLAUDE.md
```

All four assert a literal string is present in `CLAUDE.md`, which became a router on 2026-08-16
and deliberately stopped reproducing operating law. **They are red on `main` and on every prefix,
and no candidate here introduced or could remove them.** Not counted as candidate regressions.

🔴 **The migration map answers only one of the four.** `claude_md_migration_map.md` names
`session_self_evaluation.md` and does not name the other three; the three strings are present in
27, 5 and 21 tracked files respectively. **Repointing the guards is therefore not mechanically
derivable** — choosing which surface must carry an obligation is a routing decision, not an
engineering one, so it is stated and not made.

### A residual of the tool, stated

**The baseline step inherits the base's defects and the tool cannot tell them apart from the
candidate's.** `INTEGRATION FINDINGS: plan-repo-surface-determinism` names the step that carried
the 4 mode-bit offenders, and those offenders are `main`'s. A step zero measuring the base alone
would separate them; it is not built here, and until it is, the first row of any matrix must be
read as *base + candidate*.
