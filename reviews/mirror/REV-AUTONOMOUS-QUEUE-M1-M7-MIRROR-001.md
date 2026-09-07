---
artifact: MIRROR hostile review (Annex C.2) — autonomous queue M1–M7
review_id: REV-AUTONOMOUS-QUEUE-M1-M7-MIRROR-001
object: ORCHMAJOR2-A `abdcc7f` · REPOSURFACE `299492b` (moved twice mid-review) · CPROOT `5e8d66f` · APQCONS `897bef7` ·
  ADJFAILCLOSED `edb8172` · Scientist A's FIVECLAIM/CLAIM006/DOSE packet on `lettore` `ccddc28` ·
  Scientist B's therapeutic candidates — blob `fc40eb42`, reached at `lettore-b` `29408ca`
base_head_at_measurement: `main` `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5`
tips_at_publication: `lettore-b` `0b67a9d` (moved three times during this review; the reviewed
  blob `fc40eb42` is unchanged at that tip and § 10 stands against it) · REPOSURFACE `299492b` ·
  `lettore` `ccddc28` · every other ref as measured in § 1. **Findings are bound to blobs, not to
  branch names.**
supersedes_verdicts_on: CPROOT, REPOSURFACE, ADJFAILCLOSED — reviewed against hashes that have
  since moved; re-derived here. APQCONS is the same object and its verdict is re-verified, not
  re-asserted.
level: R4 (METHOD — Mirror)
reviewer: mirror
date: 2026-08-26
verdict: ONE BLOCKING FINDING ON REPOSURFACE · one routing discrepancy on MAJOR-2 that no
  technical review can settle · one false universal negative proposed into a consolidated
  baseline · FIVE of my own findings or fixtures corrected, downgraded or withdrawn, two of them
  because the object answered me between measurement and writing
mode: OPERATOR ABSENT — nothing here is adopted, routed or committed beyond this branch
---

# The gate that was repaired restores its own defect wherever git is not on the PATH, and the clause the operator chose is not the clause that is deposited

---

## 1 · `CURRENT_HASH_REVIEW_MAP`

`CANDIDATE_CONTENT_HASH` via `governance/scripts/candidate_content_hash.py --base 788c357 --tip <ref>`.
Recorded because three of these moved between my 17:00 review and this one, and two moved again
while the queue was being worked.

| candidate | reviewed tip | current tip | `REVIEWED_HASH` | `CURRENT_HASH` | `SAME_OBJECT` |
|---|---|---|---|---|---|
| **CPROOT** | `a3efcb0` | `5e8d66f` | `1cac95c55c1148e5` | `147cdba2dc960a8b` | **NO — re-derived** |
| **REPOSURFACE** | `47c6e2c` → `d3c4b2a` | **`299492b`** | `1624156275beed9d` | `e5ac47e20891c868` | **NO — moved twice mid-review; § 3 is against `299492b`** |
| **ADJFAILCLOSED** | `775e44e` | `edb8172` | `ff99959cbd49305a` | `8a082f93cb777142` | **NO — re-derived** |
| **APQCONS** | `897bef7` | `897bef7` | `601963b4e59082f6` | `601963b4e59082f6` | **YES** |
| **ORCHMAJOR2-A** | `abdcc7f` | `abdcc7f` | `756b9320a1853468` | `756b9320a1853468` | **YES** |
| RELSURF | `bf9c807` | `bf9c807` | `541a2631b67e9500` | unchanged | YES |
| GOVTESTS | `c1294fd` | `c1294fd` | `16a20ba43ca9e6cb` | unchanged | YES |

Scientific surfaces, by blob:

| artifact | reviewed blob | current blob | |
|---|---|---|---|
| `CC-…-LOCATOR-PACKET-01` | `dccf8039` | `6871a275` | **MOVED** |
| `CC-…-FIVECLAIM-PACKAGE-01` | `7cf328f3` | `ae472b29` | **MOVED** |
| `CC-…-CLAIM006-01` | absent | `e6b35edb` | **NEW** |

---

## 2 · `MAJOR2_A_FINAL_REVIEW`

Operator decision: **Variant A — *"through `CANONICAL_BATCH_COMMIT`"***.

### 2.1 · The object, exactly

`plan-major2-f8-option-A` `abdcc7f` is **1 ahead of `main`, 0 behind**, touching
`roles/orchestrator.md` and nothing else: `+6/−5`. Two spans — frontmatter
`worktree: the repository root checkout` → `worktree: orchestrator` (**identical in A, B, C and D**),
and the must-not clause.

### 2.2 · 🔴 FINDING M1-1 — the deposited state is not variant A

| ref | must-not clause | is this A? |
|---|---|---|
| `plan-major2-f8-option-A` `abdcc7f` | *"commit its own work **through `CANONICAL_BATCH_COMMIT`**"* | ✅ the decided text |
| `plan-major2-restricted-repair` `5e3a757` | *"commit its own work **to the canonical surface**"* | ❌ |
| `plan-integration-preview` `6add618` | *"commit its own work **to the canonical surface**"* | ❌ |

The deposited and integration-merged state carries **variant C's wording without variant C's
frontmatter definition** — the candidate record's own label for it is **`C0`**, *"phrase kept,
undefined"*, `CANDIDATE_CONTENT_HASH 9f852385…`. Verified by diff: `option-C` → `restricted-repair`
differs only by the deletion of the three-line `canonical surface:` definition.

This is not a defect in A. It is a **routing discrepancy**: the decision names an object that is
not the one staged. Executing `plan-integration-preview` as it stands would land a clause the
operator did not choose, and the difference is not cosmetic — my own earlier F8 review measured it
as *act-scope versus place-scope*, which disagree precisely about a hand commit to `main`.

**Credit where it is due.** Plan found this independently and recorded it against itself: commit
`5e3a757` — *"The term is not undefined, it is already used on main to mean something else"* —
measures **4 occurrences of "canonical surface" on `main`, all plural, all non-normative, all in
the scientific layer**, meaning *a canonical file that carries a claim*. Its § 6bis.2 further
concedes that the four words were **imported from ORCHSURF revision 4**, which its own § 5 says the
candidate does not do, and § 6bis.4 concludes that *"A and B implement the scope; C0 transcribes
the description."* **The candidate record already recommends against what the candidate deposits.**

### 2.3 · The eight checks

| # | check | result |
|---|---|---|
| 1 | `WORK_COMMIT` remains possible | ✅ in the role contract — ⚠️ see M1-2 |
| 2 | self-canonicalisation blocked | ✅ **GATE 1** (`body §12`) — *"Solo candidate preparati da Plan; mai lavoro proprio"* — is untouched and blocks it independently of A |
| 3 | direct-`main` governed elsewhere | ⚠️ see M1-4 |
| 4 | **no ORCHSURF rev-4 import** | ✅ `session_home` **0**, `canonical_batch_surface` **0**, in A and on `main` alike |
| 5 | root/worktree coherent | 🔴 see M1-3 |
| 6 | **no new authority term** | ✅ `CANONICAL_BATCH_COMMIT` pre-exists on `main` in **23 files**, defined at body § 11 and gated at § 12 |
| 7 | body alignment | 🔴 see M1-2 |
| 8 | **fingerprint containment** | ✅ **exact** — measured at both refs |

Check 8, measured rather than predicted:

```
                main 788c357          option-A abdcc7f
orchestrator    88dea7a635919c9f…  →  1f8b55ecb9168f20…    MOVES
plan            0d6987bd79e54839…  →  0d6987bd79e54839…    identical
mirror          e01b410891c4f300…  →  e01b410891c4f300…    identical
scientist       b66959cd0bb7ccd5…  →  b66959cd0bb7ccd5…    identical
```

### 2.4 · FINDING M1-2 — A edits the transcription, not the norm

The role contract's must-not list is a **1:1 English transcription of body § 35.1**: eight items,
same order.

| source | text | rank (body § 5) |
|---|---|---|
| Body § 35.1 | *"NON DEVE: **committare lavoro proprio**; …"* — unqualified | **1** |
| `roles/orchestrator.md` at A | *"must not: commit its own work **through `CANONICAL_BATCH_COMMIT`**"* | **4** |

A does not touch § 35.1. **On `main` the two agree; after A they disagree, and the body outranks
the contract.** So either the narrowing is inoperative, or a reader who consults the contract —
which body § 35.2 requires to be materialised in every worktree — gets the permissive reading while
the binding text stays absolute.

Plan's defence is that GATE 1 *scopes* § 35.1: *"§ 35.1 states the prohibition and GATE 1 states
what it ranges over."* **That reading is plausible and is not compelled by the text.** § 35.1's own
list separately names *"batch senza gate (incluso GATE 0)"* — it already incorporates the gates by
reference. A list that names batch-gate violations **and** "committare lavoro proprio" as distinct
items reads more naturally as two rules than as one stated twice. Plan says so itself: *"a reviewer
must be free to reject the reading above."* I record the reading as **contested, not refuted**, and
the companion edit to § 35.1 as rank-1 governance that A does not perform.

### 2.5 · FINDING M1-3 — root/worktree consistency fails on two further surfaces

A moves the frontmatter to `worktree: orchestrator`. Still saying otherwise at A:

| surface | text | rank |
|---|---|---|
| **`BOOTSTRAP.md`:86** | `| orchestrator | the repository root checkout | roles/orchestrator.md |` | mandatory reading path (CLAUDE.md § 0) |
| **body § 11** | `CANONICAL_BATCH_COMMIT → SOLO Orchestrator, **root**, sotto gate 0–5` | 1 |

`git diff main plan-major2-f8-option-A -- BOOTSTRAP.md` is **empty**. Three surfaces, two answers,
and A leaves undefined whether the root remains inside the *"perimetro"* § 35.1 permits git in once
the work surface moves off it. **Variant C's deleted frontmatter line is exactly the text that
closed this**; A is the variant that leaves it open, and that is a cost of the decision, not an
error in it.

### 2.6 · FINDING M1-4 — A's clause is honest; A's justification is not

The brief asks that A not *claim* to solve the direct-`main` problem. **Its normative text does
not** — it says nothing about `main`, and that is correct and honest.

Its **justification** does. Candidate record § 6bis.4: *"Since the batch is the only sanctioned
route, they coincide in practice, and a strictness that closes an unsanctioned route is not a
capability change."* The question at issue is whether the unsanctioned route is *prohibited*;
answering "it is unsanctioned" assumes it. **The clause under-claims correctly and the sentence
defending it over-claims.**

`MAJOR2_A_FINAL_REVIEW = A IS SOUND AS AN OBJECT — no new term, no rev-4 import, GATE 1 intact,
fingerprint contained. It is not the object deposited, it leaves two surfaces contradicting its own
frontmatter, and it creates a precedence divergence its scope cannot close.`

---

## 3 · `REPOSURFACE_HOSTILE_VERDICT` — **BLOCKING**

Baseline at `d3c4b2a`: **581 publishable, 551 text files, `VERDICT: PASS`, `BLOCKS: 0`.**

### 3.1 · What the repair closes — it does

| # | case | governance files | verdict |
|---|---|---:|---|
| C1 | untracked one-line `.git` **file** in tracked `governance/` | 38 = baseline | **FIXED** |
| C2 | untracked `.git` **directory** in tracked `governance/` | 38 | **FIXED** |
| C3 | worktree **gitfile syntax** in tracked `framework/` | 38 | **FIXED** |
| C4 | **real nested clone** (negative control) | 38, `551` unchanged | correctly pruned |
| C11 | symlinked directory alias | scanned once, alias not followed | correct |

### 3.2 · 🔴 FINDING S-2 — the repair is scoped to "inside a work tree", and the publication surface is outside it

**The object moved twice while I was measuring it** (`d3c4b2a` → `da63222` → `299492b`, +133 lines
to the gate), and the new revision addresses this finding directly. It is re-derived against
`299492b` / `e5ac47e20891c868`. The candidate now separates two failures that its first draft
merged:

```
not inside a work tree      frozenset()   "nothing outer is claimed, so nested checkouts prune
                                           — an archive extraction, a plain directory"
inside one, index unread    None          "the question was asked and not answered"
```

That separation is correct reasoning about a **real** nested checkout. It is false about a **stray
marker**, and a stray marker is the candidate's entire premise. Measured at `299492b`, paired
controls throughout:

| # | environment | marker | text files | `governance/` |
|---|---|---|---:|---:|
| C1 | inside the work tree | untracked `.git` in `governance/` | 551 | 38 | ✅ fixed |
| C6b | **exported release copy** (`git archive`, no `.git`) | none | 551 | 38 |
| **C6** | **exported release copy** | untracked `.git` in `governance/` | **513** | **0** |

```
C7a  exported copy, violation in a TRACKED document, no marker   VERDICT: BLOCK_PUBLICATION   BLOCKS: 1
C7b  exported copy, violation in a TRACKED document, + .git       VERDICT: PASS                BLOCKS: 0
```

The control returning exactly the in-repo baseline (551) rules out an extraction artefact.
**`BLOCK_PUBLICATION → PASS`, from a one-line untracked file, against the current candidate.**

What changed is not the outcome but its status: at `d3c4b2a` this was an oversight in an
`except` clause; at `299492b` it is a **deliberate design decision**, justified on the ground that
*"a subtree with its own `.git` is unambiguously a different repository's disk."* **That premise is
exactly what the candidate's headline defect refutes** — a one-line untracked file named `.git` is
not a repository, which is the sentence the whole repair exists to make true. The repair makes it
true inside a work tree and leaves it false outside one, and outside one is
`unpublishable_paths()`'s own named case: *"Outside a git checkout (an exported release copy)
nothing is exempt."* An exported copy is where a publication gate runs.

### 3.2b · FINDING S-4 — `git` absent is now a traceback

`tracked_paths()` at `299492b` opens with `subprocess.run(["git", …, "--is-inside-work-tree"])`
carrying `check=False` and **no `OSError` guard**. With `git` off the `PATH`:

```
File "scripts/public_release_gate.py", line 141, in tracked_paths
FileNotFoundError: [Errno 2] No such file or directory: 'git'
```

This **replaces** the silent false PASS that the same environment produced at `d3c4b2a`, and
failing loudly is strictly better than passing quietly. It is nonetheless an unhandled error path
in a gate, and it is the same class as CPROOT's R-3 — one `OSError` catch away, in a second module,
on the same day. **`MAJOR_FINDING`, and an improvement on what it replaced.**

### 3.3 · FINDING S-3 — `FALSE_INCLUDE`, `PASS → BLOCK`

Once the outer repository tracks **any** path under a directory, a real nested checkout there is no
longer pruned, and its non-ignored files enter this gate's population.

```
C9   outer tracks vendored/outer_tracked.md, then `git init` inside vendored/
     population: ['vendored/neutral_doc.md', 'vendored/outer_tracked.md']
     VERDICT: BLOCK_PUBLICATION   BLOCKS: 2   ← both from another repository's working tree
```

Direction is fail-closed for publication, so it leaks nothing; it re-opens the 37-false-BLOCK
regime `is_exempt()`'s docstring documents historically, and it pulls a second repository's files
into this gate's scan.

**Method note against myself:** my first run of this case showed no `FALSE_INCLUDE`, and I almost
recorded that. The nested file was excluded by `.gitignore:26 *private*`, not by the candidate's
logic — I had named the fixture `private_notes.md`. With a non-ignored name the defect appears.

### 3.4 · FINDING S-1 — re-confirmed against the new hash, not carried forward

```
C10  git add -f backup/forced.md   (tracked, privacy-violating)
     in population: []             VERDICT: PASS   BLOCKS: 0
```

`SKIP_DIRS` is evaluated **before any tracked check**, at both the directory filter and the file
filter. The gate's own `unpublishable_paths()` docstring: *"an allowlist keyed on directory names
would silently exempt exactly the case that matters."* `SKIP_DIRS` is that allowlist. Live blast
radius remains **0** tracked paths under any `SKIP_DIRS` name.

### 3.5 · Suite coverage, and what re-testing changed

At `d3c4b2a` the suite carried 9 tests and the keyword probe returned zero for every route into the
failure path (`PATH`, `FileNotFoundError`, `OSError`, `CalledProcessError`, `archive`, `export`,
`outside`). `299492b` adds 251 lines to that file — its own commit message is *"A test of vacuous
passes that passed vacuously"* — and separates the two sentinels. **S-1, S-2 and S-3 were all
re-run against `299492b` and all three reproduce.**

`REPOSURFACE_HOSTILE_VERDICT = BLOCKING at content hash e5ac47e20891c868. The primary invariant —
a local, untracked filesystem marker must not remove tracked publishable material — holds inside a
work tree and fails in an exported release copy, which is the surface a publication gate is run
against.`

---

## 4 · `CPROOT_HOSTILE_VERDICT` — **MAJOR_FINDING** (materially improved)

`repo_root.py` is **byte-identical** to the version I reviewed; `5e8d66f` adds
`control_plane_probe.py`, ten lines to `lease_state.py` and 7 tests.

### 4.1 · My § 2.4 finding is closed

```
CONTROL_PLANE_SOURCE_PATH    <absolute path actually read>
CONTROL_PLANE_SOURCE_SHA256  <digest>
CONTROL_PLANE_RECORD_COUNT   <n>
```

Run from this worktree the tool now says it read
`…/worktrees/mirror/runtime/orchestrator_lease.md`; run from the candidate root it names that root.
**The two answers that were previously indistinguishable now name their objects.** That is exactly
the repair I asked for, and `control_plane_probe.py` makes the comparison a command rather than a
habit.

### 4.2 · The battery, re-run

| case | exit | answer | verdict |
|---|---:|---|---|
| candidate root | 0 | `ACTIVE: 0`, source named | ✅ |
| nested subdir `framework/scripts` | 0 | same root, source named | ✅ |
| outside any repository (`/tmp`) | 2 | `LEASE STATE UNDERIVABLE` | ✅ fails closed |
| **bare repository** | 2 | `LEASE STATE UNDERIVABLE` | ✅ fails closed |
| decoy `runtime/` in a plain subdir | 0 | true root's lease | ✅ |
| **R-1b** nested repo present, caller at root | 0 | true root's lease, `ACTIVE: 0` | ✅ |
| **R-2** `GIT_DIR`+`GIT_WORK_TREE`, caller at root | **0** | **decoy lease, `ACTIVE: 1`** | 🔴 **survives** |
| **R-3** `git` absent from `PATH` | **1** | **uncaught `FileNotFoundError`** | 🔴 **survives** |

`GIT_DIR` **alone** does not do it — both variables are required.

### 4.3 · 🔴 I withdraw R-1 as I stated it

> **R-1** *(REV-CURRENT-HASH-CLOSURE-MIRROR-001 § 2.1)* — *"a decoy `runtime/orchestrator_lease.md`
> inside any nested checkout is read as the laboratory's lease record."*
>
> **WITHDRAWN.** The sentence omits its precondition. The nested lease is read **only when the
> caller stands inside the nested checkout**, which is `repo_root.py`'s explicitly declared
> contract — *"It binds to the worktree the caller is in"* — and is now observable in the output.
> From the candidate root with a nested repository present, the answer is correct (`R-1b`).
> Reclassified **`ACCEPTABLE_BY_CONTRACT`**.

**And the way I nearly got this wrong is the finding worth keeping.** My first re-test of R-1 and
R-2 returned **exit 2** for both, which reads as a refusal, and I was one step from recording both
as FIXED. The exit was `no LEASE block found` — **my decoy fixture was malformed**, not the tool
refusing. Calling `repo_root()` directly showed it returning the decoy root in both cases. A
fixture that fails for its own reasons produces the exact output shape a successful repair produces.

R-2 and R-3 remain **`MAJOR_FINDING`** — downgraded from blocking only because the source path is
now printed, so R-2 is at least visible to a reader.

`test_repo_root.py` now carries **19** tests. `GIT_DIR` 0 · `GIT_WORK_TREE` 0 · `FileNotFoundError`
0 · `nested` 0. Neither surviving finding is reachable by the suite.

---

## 5 · `APQCONS_CURRENT_VERDICT` — same object, re-verified

`897bef7` / `601963b4e59082f6`, unchanged. Re-run at CLI level, not read off my prior report.

| residual | observed | class |
|---|---|---|
| basename collision, 3× `queue.jsonl` | `dirA=4, dirB=5, dirC=6` → **13 records from 15 input line(s); 2 deduped** — all **12** approvals survive, headers deduped | **ACCEPTABLE_BY_CONTRACT** |
| count accuracy before/after dedup | exact and honest | **ACCEPTABLE_BY_CONTRACT** |
| malformed JSONL | `SOURCE ERROR … not valid JSON`, line-numbered, **exit 2** | **ACCEPTABLE_BY_CONTRACT** |
| symlink / alias identity | `SOURCE ERROR — the same file was supplied more than once`, **exit 2** | **ACCEPTABLE_BY_CONTRACT** |
| **malformed** timestamp | `not-a-date` sorts **after** `2026-08-17` | **ACCEPTABLE_BY_CONTRACT** — repaired |
| same identity, conflicting payload (**string** id) | `SOURCE ERROR … AP-1 appears twice … with different bodies`, **exit 2** | **ACCEPTABLE_BY_CONTRACT** |
| **non-string id**, conflicting payload | `{"APPROVAL_ID": 7, "STATE": "APPROVED"}` and `…"REJECTED"` **both kept, exit 0**, content-addressed to two `sha256:` identities | 🔴 **MAJOR_FINDING** |
| **missing** timestamp | `AP-NO-TS` sorts to **position 1**, ahead of a legible `2026-08-17` | 🔴 **MAJOR_FINDING** |
| **directory / missing file** as source | uncaught `IsADirectoryError` / `FileNotFoundError`, **exit 1** | 🔴 **MAJOR_FINDING** |

The last one is sharper than I recorded it: **exit 1 is this tool's `CONFLICT` code** (`return 1`
on `ConflictError`; `return 2` on `SourceError`). An unreadable source therefore reports as a
conflict for an Operator to adjudicate.

The missing-timestamp defect is the one the tool's own docstring describes — *"a record whose date
could not be read was presented first, at position 1"* — repaired for the **non-string** case
(raises) and the **unreadable-string** case (sorts last), and still open for the **absent** case,
which returns `""`. Two failure modes that look alike to a reader are handled oppositely.

**Method note against myself:** my first battery set `TIMESTAMP` on the fixtures. The tool reads
`REQUESTED_AT` / `RESOLVED_AT` / `RECORDED_AT`. Both ordering results from that run were void and
were re-run; the timestamp column reading `—` for records I had just dated is what exposed it.

`APQCONS_CURRENT_VERDICT = NO LONGER BLOCKING. Three residuals, one of which loses the distinction
between two contradictory decisions.`

---

## 6 · `ADJFAILCLOSED_CURRENT_VERDICT` — scoped to `RECIPE_REGENERATION`

`edb8172` adds `check_output_names()`, called once at line 226; `write` is unconditional at line
429 (`(directory / name).write_bytes(image)`). It is the **only** name gate.

| state | guard | class |
|---|---|---|
| exact duplicate `file` | **REJECTED** | repaired |
| traversal `../x.png` | **REJECTED** | repaired |
| absolute `/tmp/x.png` | **REJECTED** | repaired |
| trailing slash `b.png/` | **REJECTED** | repaired |
| `./a.png` | **REJECTED** | repaired |
| non-dict artifact / absent `file` | **REJECTED** | repaired |
| **case alias** `A.png` + `a.png` | 🔴 **ACCEPTED** | **MAJOR_FINDING** |
| **NFC/NFD alias** `café.png` ×2 | 🔴 **ACCEPTED** | **MAJOR_FINDING** |

Both reach `write`. On this filesystem, measured directly:

```
A.png then a.png       -> files on disk: ['A.png']       A.png holds: TWO
café.png NFC then NFD  -> files on disk: ['café.png']    read back via NFC: TWO
```

**One declared regeneration destroys the other** — the guard's own stated failure mode, arriving
through path aliasing instead of string identity. `seen` is keyed on the raw string; the filesystem
keys on a case-folded, normalised form. And because `verify` re-renders from the PDF and never
reads the disk, both artifacts still report their digests matching.

**On the directory claim, per the brief:** I do not classify stale PNGs as false passes. The
narrower point is that in exactly this state the `OBSERVED, NOT VERIFIED` line — *"every declared
artifact is present"* — remains unfalsifiable, because on a case-insensitive filesystem a presence
check on `a.png` succeeds against the `A.png` that overwrote it. The claim is not wrong here; it is
**unable to be wrong here**, which is a weaker property than it reads as.

### 6.1 · 🔴 I correct the input class of my own N5 finding

> **N5** *(REV-CURRENT-HASH-CLOSURE-MIRROR-001 § 5.3)* — *"zero-area crop → uncaught
> `FzErrorArgument` traceback."*
>
> **CORRECTED.** Against `8a082f93cb777142` a zero-area crop `(100,100,100,100)` **renders
> normally** (90 bytes); the candidate's claim that geometry refuses it is not needed and my stated
> input does not reproduce. An **inverted** crop `(200,200,100,100)` raises the uncaught
> `FzErrorArgument`, at `render()`, which runs **before** the containment check the candidate cites
> as the refusal. The finding survives; the input class was wrong. **`MINOR_FINDING`.**

`ADJFAILCLOSED_CURRENT_VERDICT = CONDITIONAL_PASS ON THE STATED CONTRACT, with one in-contract
MAJOR: the output-name guard is string-exact and the filesystem is not.`

---

## 7 · `FIVECLAIM_LOCATOR_REVIEW_STATUS`

The package is careful work: nine axes held apart rather than merged, per-claim
`WHAT_IS_FALSE` / `TOO_BROAD` / `NOMENCLATURE` / `MEASURED` separation, and repairs proposed as
narrowings rather than deletions. Two catches are excellent — `CLAIM 004`'s *"recupera letalità"*
corrected to **survival extension** against a curve that reaches 0 % by ~330 d, and
`MEASURED_SPIKE_RATE` held at `UNRESOLVED` because `p = 0.2000` is the **rank-test floor** under
complete separation.

### 7.1 · 🔴 FINDING SCI-1 — the axis that carries the whole package is a universal negative built from a term census

`EPILEPTOGENESIS` is declared **`UNRESOLVED` — never measured in any WWOX model**, and the proposed
canonical replacement for `CLAIM 005` — a **`consolidated baseline`** — reads:

> *"No canonical statement may assert `EPILEPTOGENESIS` … **in any WWOX model, because no study has
> measured that process**."*

The evidence offered for that universal is:

> *"Cheng 2020 uses the word twice, both times for provoked seizure susceptibility at a time point;
> Obeid 2026 does not use it at all (**zero occurrences**)."*

**Two papers, by word occurrence.** A term census cannot detect a study that measured the process
without using the term, and that is exactly the case that exists.

**The counterexample is in this repository's own registry.** `PMID19500159.json`, locator
proposition, verbatim:

> *"Latency to seizure shortens across repeated daily stimulations, a **kindling-like progression
> rather than a fixed trait threshold**."*

`claim_registry_current.md:670`: **56±24 → 36±4 → 25±3 s over three days.** A's own stated
criterion for measuring the process is *"a latent period, a documented conversion, or **a
manipulation that shifts it**"* — repeated stimulation shifting latency by more than half is that
manipulation. **A's own package names the same phenotype "audiogenic/kindling" three times** while
its axis table records the axis as never measured in any model.

This does not touch the mouse conclusion, which is sound. It falsifies the **quantifier**. As
drafted, the repair would install a false universal negative into a consolidated baseline — the
precise failure class the repair exists to remove, with the sign reversed. The denominator is not
stated and the corpus was never enumerated.

### 7.2 · Method note — `statistical null ≠ biological equivalence`

`GENE_THERAPY_RESCUE` and `MEASURED_SWD` carry **`✅ DATO`** on *"rescued to `ns`"* at **n = 5/group**.
A failure to reject is not equivalence. A applies this discipline correctly one row above, so the
instrument is present and is not applied to the rescue axes.

`FIVECLAIM_LOCATOR_REVIEW_STATUS = ONE BLOCKING FINDING ON THE MAJOR. The per-claim repairs are
sound; the universal quantifier that licenses them is falsified by a paper already in the canon.`

---

## 8 · `CLAIM006_REVIEW_STATUS` — **SUPPORTED, with a method caveat**

A's disaggregation of *"progressive"* into six axes read at panel level is exactly
**headline/abstract ≠ figure-level support**, and it is done fairly: § 0 records that `CLAIM 006` is
a **faithful transcription of the paper's own title and abstract**, so the failure is named as
*never checking the headline against the figures* rather than as fabrication. The `IBA1_AREA` catch
— *"the gap widens because the **WILD TYPE** declines"* (WT ≈14.5 → ≈11, mutant ≈21 → ≈20.5) — is
the kind of thing a headline can never show.

**Caveat, `MINOR_FINDING`.** The `NOT PROGRESSIVE` verdicts are *stated* as resting on the **absence
of a within-genotype significance bracket**, on the premise that the paper drew brackets wherever it
tested an age effect. That premise is an inference about a figure convention, and absence of a
bracket is compatible with *tested and null* **and** with *not tested* — `NOT_REPORTED ≠ ABSENT`.
What actually carries both verdicts is **value identity** (≈34 → ≈34; ≈21 → ≈20.5), which is
independent and sufficient. The conclusion survives; the stated warrant is the weaker of its two
legs and should not be generalised to an axis where the values do not independently settle it.
Panel values are read `≈` from pixels — the normalisation and read method should be declared per
axis, as the dose candidate does.

---

## 9 · `DOSE_REVIEW_STATUS` — **`PIXEL_MATCH`, exact, independently reproduced**

Recipe applied verbatim from `CC-20260826-DOSE-ADJUDICATION-01` § 1, sources read from the **root
checkout** so that nothing of Scientist A's was touched:

| dimension | declared | measured | |
|---|---|---|---|
| `source_pdf_sha256` (Appendix) | `1e5c30a903d96726…` | `1e5c30a903d96726…` | **MATCH** |
| page / crop / dpi | 2 · `(0,0,510,567)` · 300 | applied as declared | — |
| pixels | `2125 × 2363` | `2125 × 2363` | **MATCH** |
| `image_sha256` | `e362bdf80c8d850b…` | `e362bdf80c8d850b…` | 🟢 **PIXEL_MATCH** |
| `source_pdf_sha256` (article) | `32ee98733a6f4555…` | `32ee98733a6f4555…` | **MATCH** |

**`DO_NOT_INFER`.** `PIXEL_MATCH` verifies the **instrument** — the recipe names a stable, correctly
identified surface and reproduces byte-for-byte from a second checkout. It does **not** verify the
proposition that *all three Repudi vectors are WPRE-free*; that requires reading the rendered panel,
which this pass did not do. `CLAIMED_FACT_SUPPORTED: NOT ASSESSED — surface verified, content not
read.`

**Credit.** The candidate reports a **falsified prediction as falsified** — the WPRE discriminant
was expected to reconcile `CLAIM 004` and `CLAIM 011` and instead excludes the reconciliation — and
states that the contradiction is *sharpened, not softened*. That is the harder direction to report.

---

## 10 · `THERAPEUTIC_REVIEW_STATUS`

**Transfer boundary — no finding.** `NMDAR-CONJUNCTION-01` and `GAPJUNCTION-ATTRIBUTION-01` edit the
same sentence of `CLAIM 021` and are deliberately split, with the independence stated in both
files: an **upgrade on a positive pharmacological result** versus a **withdrawal of attribution on a
washout failure**. *"Neither presupposes the other."* That is the boundary drawn correctly, and it
is what lets a reviewer accept one and refuse the other.

**Surface identity verified.** `gr4.jpg` →
`4bfa9eefa0e9eae4ccc12c97894c7044419785e63b8128952377a97d4d566d6d`, matching B's declared
`4bfa9eef…d566d6d`. Base head `b80ae8b` is the parent of the authoring commit `bf88c1a` — checked,
correct convention, not a finding.

**B's self-correction is the right one.** MOTOR was recorded as `RESCUE` in two of B's own files on
the strength of S4A's `ns`; B re-read Figure 4, found the WT-versus-treated bracket drawn in **all
eight panels**, and withdrew its own verdict in the direction unfavourable to the therapy.

### 10.0 · 🔴 Both findings below were raised against `bf88c1a` and the branch moved to `29408ca` while I wrote them

The candidate blob went `1f772b48` → **`fc40eb42`**. I re-derived both findings against the current
blob before publishing. **One is withdrawn and one is downgraded**, and the reason is that Scientist
B answered them in the interval. This is the same failure as § 12 item 7, on a second branch, in the
same sitting.

### 10.1 · FINDING TX-1 — **DOWNGRADED to `MINOR_FINDING`** — the label, not the text

B's measurement: three of eight panels significant, and **in all three the treated animals exceed
wild type** — velocity ≈9.5 → ≈11.5, distance ≈3 400 → ≈4 300, rotarod latency ≈85 s → ≈145 s.

`PARTIAL` denotes **incomplete movement toward** the reference; these animals are on the **far side
of it**. I raised this as MAJOR against `1f772b48`.

**Against `fc40eb42` it survives only as a label.** The canonical text B now proposes carries the
direction explicitly:

> *"**Motor and locomotor behaviour** is not impaired and not normalised: three of eight panels
> differ significantly from wild type, **in the exceed direction**, unadjusted for multiplicity."*

That sentence is precise and does not imply partway-toward-wild-type. What remains is that the
internal matrix still files it under the header word `PARTIAL`, whose contents B defines by
enumeration and enumerates correctly. **`MINOR_FINDING` — a header word, not a claim.**

### 10.2 · FINDING TX-2 — **WITHDRAWN**

> I was going to write: *B discounts the three asterisks as marginal and unadjusted across eight
> comparisons, and simultaneously rests `NOT_NORMALISED` on those same three asterisks; applied
> consistently the caveat nulls all eight comparisons.*
>
> **WITHDRAWN against `fc40eb42`, where B has already made the discrimination I was about to ask
> for**, and made it in the harder direction — against the reading most favourable to the tidy
> conclusion:
>
> - *noise / marginal statistics* — **partially disfavoured for M3 only** (rotarod ≈1.71× is a poor
>   fit for a threshold artefact); **not disfavoured for M1 and M2**, which *"sit exactly where a
>   `*` at n ≈ 10 in an uncorrected family of eight would fall"*; ⇒ **"the three positives do not
>   stand or fall together"**;
> - *hyperactivity* — explains M1 and M2, **fails to explain M3**;
> - *overexpression overshoot* — **"consistency is not discrimination"**, and the discriminating
>   test *"cannot be run in this dataset"* because the low dose does not reach P90.
>
> B also names the structural consequence — *"the failure to discriminate is structural, not
> incidental"* — and converts it into one experimental arm discharging two revival triggers. My
> objection assumed the three asterisks were being treated as one block. They are not.

B further separates three status words this review would otherwise have had to ask for —
`NOT_TESTED` (comparison never drawn) · `NOT_REPORTED` (drawn, no result printed) · `NOT_RECORDED`
(drawn and printed, **our locator missed it**) — the third of which is a category for the reader's
own failure, and I have not seen another actor in this repository volunteer one.

`THERAPEUTIC_REVIEW_STATUS = TRANSFER BOUNDARY SOUND. One finding withdrawn, one downgraded to a
header word, both because the object answered them between my measurement and my writing.`

---

## 11 · `NEW_FALSE_PASS_FINDINGS`

| # | surface | direction |
|---|---|---|
| **S-2** | `public_release_gate.py` `299492b` — `BLOCK_PUBLICATION → PASS` in an **exported release copy** | 🔴 **false PASS** |
| **S-4** | `public_release_gate.py` `299492b` — `git` absent raises an uncaught `FileNotFoundError` | fail-loud; **replaces** a false PASS |
| **A-2** | `regenerate_adjudications.py` — an alias pair destroys one regeneration while both artifacts verify green | 🔴 **false PASS** |
| **APQ** | `consolidate_approval_queue.py` — two contradictory decisions on one non-string id survive at exit 0 | 🔴 **false PASS** |
| **SCI-1** | `CC-…-FIVECLAIM-PACKAGE-01` — a false universal negative proposed into a `consolidated baseline` | 🔴 **false negative, canonical** |
| **S-3** | `public_release_gate.py` — another repository's working tree enters the population | `PASS → BLOCK` |

---

## 12 · `STALE_REVIEWS_WITHDRAWN` — and my own errors, at the same visibility

| # | mine | disposition |
|---|---|---|
| 1 | **CPROOT R-1** as stated — *"a decoy inside **any** nested checkout is read as the laboratory's lease"* | **WITHDRAWN** — the precondition (caller stands inside it) was omitted, and with it the sentence describes a defect reachable from a legitimate position. It is not. Reclassified `ACCEPTABLE_BY_CONTRACT` |
| 2 | **ADJFAILCLOSED N5** — *"zero-area crop → traceback"* | **CORRECTED** — zero-area renders; **inverted** crop raises. Finding survives, input class was wrong |
| 3 | **REV-CURRENT-HASH-CLOSURE-MIRROR-001 § 7, check 8** — predicted the orchestrator fingerprint moving `88dea7a6… → 756b9320…` | **CORRECTED** — `756b9320…` is A's `CANDIDATE_CONTENT_HASH`, not a fingerprint. I wrote a transition between two different quantities. Measured: `88dea7a6… → 1f8b55ec…` |
| 4 | this session, CPROOT | R-1 and R-2 first re-tested as **exit 2**, one step from being recorded FIXED. The exit was my **malformed decoy fixture**; `repo_root()` returned the decoy root in both cases |
| 5 | this session, APQCONS | ordering battery run with field `TIMESTAMP`; the tool reads `REQUESTED_AT`/`RESOLVED_AT`/`RECORDED_AT`. Both results void, re-run |
| 6 | this session, REPOSURFACE | recorded *no `FALSE_INCLUDE`* before establishing the mechanism. The exclusion was `.gitignore:26 *private*` matching my fixture's **name**. With a neutral name the defect appears |
| 7 | this session, REPOSURFACE | I wrote § 3 against `d3c4b2a` and the branch was already at **`299492b`**, two commits further on, one of which was a direct answer to the finding I was writing. Caught only by re-reading the tips at close, after the report existed. **The re-derivation changed one finding's class** (S-4) and changed *why* another one stands (S-2) — the outcome survived, the explanation in the draft did not |

| 8 | this session, THERAPEUTIC | **TX-1 and TX-2** were raised against `lettore-b` `bf88c1a` / blob `1f772b48`; the branch was at `29408ca` and the blob at `fc40eb42` before I published. **TX-2 withdrawn, TX-1 downgraded to a header word** — B had already answered both, and in the harder direction |

Items 4–8 are one class: **a fixture, or a ref, that has moved for its own reasons produces the
output shape a correct answer produces.** Five times in one session. The only thing that caught each
was checking the mechanism instead of the verdict, and items 7–8 say the frozen set thaws inside a
single sitting: the tips in § 1 were measured at the start, and **three of them** — REPOSURFACE,
`lettore-b`, `lettore-c` — were already wrong by the end. Two of the verdicts I was about to publish
changed on re-derivation, **both in the candidate's favour**.

**A hostile review that measures once is reviewing a past.** The operational consequence is in § 14
item 1, and it is not a preference: re-deriving the tips took under a minute and changed what this
document says.

---

## 13 · `TRUE_HUMAN_REQUIRED`

1. **`CONTROL_PLANE_RELEVANCE_SET`** — unchanged, and the operator has already ruled it
   `HUMAN_REQUIRED`. The Annex I.3 singleton stays unverifiable under per-worktree lease records,
   and `test_repo_root.py:127` still pins that as a defect so it cannot be closed silently.
2. **MAJOR-2 routing** — the decision names variant **A**; the deposited and integration-merged
   state is **C0**. Which object executes is not a reviewer's call.
3. **Body § 35.1 companion edit** — whether the rank-1 clause is narrowed alongside the rank-4
   transcription. Rank-1 governance; A cannot reach it and does not claim to.
4. **`BOOTSTRAP.md`:86 and body § 11** — both still place Orchestrator and the canonical commit at
   the root while A's frontmatter moves the work surface off it.

---

## 14 · `NEXT_5_MIRROR_ACTIONS`

1. **Re-derive every candidate hash before any hand-off.** Three moved between my last review and
   this one; the map in § 1 is already perishable.
2. **Re-attack REPOSURFACE** once `tracked_paths()` distinguishes *"this repository tracks nothing
   here"* from *"I could not ask"* — the fix is a sentinel, and the regression test is the exported
   copy, which the suite has never run.
3. **Convert SCI-1 from a term census to a method census** — enumerate the WWOX corpus and ask of
   each study whether it observed a transition, rather than whether it used the word.
4. **Read the rendered Appendix Fig S1 panel** to move the dose locator from instrument-verified to
   proposition-verified. The recipe is sound; the fact is not yet checked.
5. **Re-review ADJFAILCLOSED** against a normalisation-aware output-name guard, and re-run the
   inverted-crop path.

---

**Nothing in this review was adopted, routed or committed beyond this branch. No canonical file was
modified. Every figure above was measured in this session against the hashes named in § 1, and the
three fixtures that misled me are recorded in § 12 beside the findings they nearly became.**
