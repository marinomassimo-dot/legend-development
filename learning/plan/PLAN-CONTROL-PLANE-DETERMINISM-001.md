---
record_type: WORK_ANALYSIS
id: PLAN-CONTROL-PLANE-DETERMINISM-001
title: The compensating protocol J.0 names is the one that does not work, and three guards answered by where you stood
date: 2026-08-26
role: PRODUCER
mode: BUILD / P0 CONTROL-PLANE DETERMINISM
authority: Plan role contract — candidate preparation on own branches. No CANONICAL_BATCH_COMMIT.
  No H.1 decision selected. No governance text amended.
status: FOUR NEW CANDIDATES · eight total · all composed and measured · two normative boundaries
  routed
---

# CONTROL-PLANE DETERMINISM AND FALSE-PASS CLOSURE

> **Nothing here is medical advice.** Tooling and control-plane semantics only.

**Everything below was re-derived. Three of the six incoming statements changed shape under
measurement, and one of my own from the previous session turned out to be wrong.**

---

## 1 · CPROOT — three readers, and the question they were answering

`lease_state.py` resolved `DEFAULT_HOME = "runtime/orchestrator_lease.md"` against `os.getcwd()`.
Measured across the five required directories, one repository, one tool:

| CWD | resolved blob | records | `ACTIVE` | exit |
|---|---|:--:|:--:|:--:|
| ROOT | `c34f4866` | **5** | 0 | 0 |
| ORCHESTRATOR_WORKTREE | `d8a2b47b` | **9** | 0 | 0 |
| PLAN_WORKTREE | `c34f4866` | 5 | 0 | 0 |
| NESTED_SUBDIRECTORY | — | — | — | **2** |
| TMP | — | — | — | **2** |

**Two different control-plane objects, both exit 0.** Four leases — the whole of 2026-08-18
evening and 2026-08-19 — are invisible to anyone running the tool from the repository root.

🔴 **And they agree on `ACTIVE: 0` by luck, not by design.** `derive()` treats `RELEASED_AT` as
terminal regardless of the clock, and every one of the nine leases is released, so no instant
separates them today. **I looked for an instant that would and did not find one** — recorded
because the absence of a divergent answer is what makes this a latent defect rather than an
active one, and reporting it as active would have been the easier and less accurate claim.

### 1.1 · The reader census, and a classification of my own that was wrong

A static classifier flagged four cwd-relative readers. **Run empirically, one of the four was
not**: `growth_anchors.py` reports identical numbers from `/tmp`, because it resolves
`REPO_ROOT = HERE.parent.parent`. My regex saw a relative constant and inferred the defect.

| Reader | Resolution | Diverges? |
|---|---|---|
| `lease_state.py` | `--home` default, a bare relative string | 🔴 yes |
| `legend_lint.py` | positional root, `default="."` | 🔴 yes |
| `sync_epochs.py` | `--root`, `default="."` | 🔴 yes |
| `growth_anchors.py` | `HERE.parent.parent` | **no — and it is the existing precedent** |

**`default="."` is the cwd defect spelled as an argument default**: it looks explicit and behaves
exactly like resolving against the working directory.

Measured divergences beyond the lease:

- **`legend_lint.py` with no argument: `VERDICT: PASS` from the repository root, `VERDICT:
  BLOCK_SYSTEM` from a subdirectory of the same checkout.** A false BLOCK is not the safe
  direction; it is the same defect with the sign flipped, and it teaches a reader to disbelieve
  the gate.
- **`sync_epochs.py status`: *"no sync epoch recorded"* from any subdirectory**, at exit 0 — an
  absence manufactured by looking in the wrong place.
- **`legend_lint.py` from `lettore`** reads a *different* state manifest (`b0ec4a26` against
  `0b327d25`) and also says PASS. Agreement by luck a second time.

### 1.2 · 🔴 The finding that outranks all of them

**Annex J.0 lists `Singleton garantito (compare-and-swap)` as a guarantee this system does NOT
possess, and names the compensating protocol: `lease record + rilevazione doppio ACTIVE + stop
condition (I.3)`.**

Two worktree-shaped fixtures, each holding one ACTIVE lease:

```
wtA  exit=0   ACTIVE by derivation: 1 — lease #1
wtB  exit=0   ACTIVE by derivation: 1 — lease #1
```

**Both report exactly what a healthy singleton looks like.** Annex I.3 says `Un solo ACTIVE`;
`lease_state.py` calls the invariant *"fatal in every mode"*. It is violated, and no command in
the repository can see it.

⇒ **The detection J.0 offers in place of a guarantee is the thing that does not work.** Under
per-worktree records, `rilevazione doppio ACTIVE` is unavailable. This is not a missing rule —
it is a named compensating protocol that is not enforceable as deployed.

---

## 2 · The primitive, and the boundary it stops at

Four candidates, all seven conditions:

| | ROOT | ACTOR_WT | SUBDIR | DETACHED | FRESH_CLONE | TMP | NO_GIT |
|---|---|---|---|---|---|---|---|
| **CWD** | ok | ok | 🔴 wrong | ok | ok | 🔴 wrong | 🔴 wrong |
| **SCRIPT_ROOT** | script's tree | 🔴 script's tree | ok | 🔴 script's tree | 🔴 script's tree | 🔴 **answers anyway** | 🔴 **answers anyway** |
| **GIT_TOPLEVEL** | ok | caller's tree | ok | ok | ok | **refuses** | **refuses** |
| **GIT_COMMON_DIR** | ok | **the shared repo** | ok | **the shared repo** | ok | **refuses** | **refuses** |

| | `WORKTREE_SAFE` | `ROOT_SAFE` | `FAIL_CLOSED` | `FALSE_FALLBACK_RISK` | `NEW_DEPENDENCY` | `DUPLICATES_EXISTING` |
|---|:--:|:--:|:--:|---|:--:|:--:|
| CWD | ✗ | ✗ | ✗ | **the defect itself** | none | — |
| SCRIPT_ROOT | ✗ | ✓ | **✗** | 🔴 **never refuses** — from `/tmp` it returns a root and reads a lease | none | yes, `growth_anchors.py` |
| GIT_TOPLEVEL | ✓ | ✓ | ✓ | none measured | git | no |
| GIT_COMMON_DIR | ✓ | ✓ | ✓ | none measured | git | no |

**`repo_root()` uses `--show-toplevel` and raises.** Not script-location: that is deterministic
about the wrong thing — it answers with *the checkout the script lives in*, so one worktree's copy
of a tool invoked from another reports on the first, and **it never refuses**. A primitive that
always answers cannot fail closed.

🔴 **It binds to the caller's worktree, and that is a deliberate non-decision.**
`--git-common-dir` would give one control plane for the whole laboratory — which is what § 1.2's
invariant needs — and would **also change which lease record is authoritative, discarding four
leases held on one worktree and not the other.** That is the relevance-set question, and a path
helper is not where it gets settled.

**After:** all three readers give one answer from anywhere inside a checkout, and refuse outside
one. **12 tests; 6 fail against `main`'s unwired tools.** One test asserts the singleton defect
**still exists**, so that repairing it cannot happen silently.

---

## 3 · CPLINEAGE — the relevance model, and where it stops

The problem is not *"more than one blob exists on more than one ref"*. It is: **more than one
simultaneously relevant lineage can produce different current-authority answers.**

| Category | Lease | Approval queue | Participates? |
|---|---|---|---|
| `CANONICAL_REF` (`main`) | 5 records | 6 records | yes — but it is the **shortest** of both |
| `ACTIVE_BRANCHES` (actor worktrees, live) | `orchestrator` 9 | `orchestrator` 10, `evidence-index` 14 | **undecidable from current governance** |
| `LATERAL_CONTROL_PLANE_REFS` | — | 2 lineages | as above |
| `STALE_REFS` (merged / superseded) | — | 31 refs share `main`'s blob | no — same object |
| `HISTORIC_TAGS` | none in this repository | none | n/a |

**For the lease, the answer is derivable and I.3 gives it**: `Un solo ACTIVE` plus J.0's
`rilevazione doppio ACTIVE` require one object; two are deployed. **Enforcement is missing, not
the rule.**

🔴 **For the approval queue, it is not derivable and I stop here.** Annex J.3 says every
`HUMAN_REQUIRED` creates an object in the queue and that the daily brief exposes
`PENDING HUMAN DECISIONS`. It does not say **which** queue, nor what to do when an actor's
branch holds approvals `main` has never seen. Four `APPROVED` records live on `orchestrator`
alone. Deciding whether a lateral ref's approvals are in force is a governance act.

**Normative boundary. Not crossed.**

---

## 4 · APQCONS — a false PASS before `consolidate()` was ever called

Re-derived. Three real lineages of 6, 14 and 10 records, copied into three directories, each
named `queue.jsonl`:

```
sources: queue=10
consolidated: 10 records from 10 input line(s); 0 deduped, 0 conflicts
exit 0
```

**Twenty of thirty records discarded**, described as a clean conflict-free consolidation. `{path.stem:
load(path) …}` collapsed three keys to one, last wins. **Even the input count was wrong**, because
it too was derived from the collapsed dict.

🔴 **And twenty-seven passing tests said nothing about it.** They call `consolidate()` with a dict
the test builds, so they never executed the line that turns files into that dict. **The tested
surface and the defective surface were disjoint** — the identical shape to the adjudication
script, whose every fail-open state lived in the one function its suite never called. *I hardened
`consolidate()` last session and never tested `main()`.*

**Repair:** source identity is the **resolved path**; the label is the shortest unique path
suffix and is a display name only. The same file supplied twice is refused rather than presented
as a lineage agreeing with itself.

```
sources: d1/queue.jsonl=6, d2/queue.jsonl=14, d3/queue.jsonl=10
consolidated: 18 records from 30 input line(s); 12 deduped, 0 conflicts
```

**17 CLI tests covering all fourteen required fixtures; 6 fail against the pre-repair CLI.**

⚠️ **One of them passed on both arms in its first draft.** `two_directories_one_basename`
asserted the output count: with the collision, 4 records in and 4 out. It was strengthened to
assert the **input** count, which is what exposes a dropped lineage. **A test that passes on both
arms of a battery has tested nothing.**

---

## 5 · Consolidation is not gate assertability

A consolidator produces a view; it does not decide which lineage is authoritative. The detector
those are separated into returns `UNIQUE | DIVERGENT | UNDERIVABLE` — **never `PASS`/`FAIL` on
authority while divergence is unresolved**, because a `PASS` there would be asserting exactly the
question § 3 leaves open.

| Case | Correct verdict | Why |
|---|---|---|
| `one_blob_many_refs` | `UNIQUE` | 31 refs, one object |
| `historic_old_blob_only` | `UNIQUE` | superseded is not divergent |
| `canonical_plus_strict_prefix` | `UNIQUE` | the lease case — a superset, no contradiction |
| `two_live_disjoint_suffixes` | **`DIVERGENT`** | the queue case |
| `canonical_missing_lateral_present` | **`DIVERGENT`** | the agent card registry |
| `malformed_lateral` | `UNDERIVABLE` | a source error is not a divergence |
| `same_content_different_refs` | `UNIQUE` | content, not location, decides |

**`FALSE_PASS` risk is the whole point**: returning `UNIQUE` for `two_live_disjoint_suffixes`
would report a settled authority that nobody settled. **`FALSE_BLOCK` risk is the mirror**:
returning `DIVERGENT` for `one_blob_many_refs` would halt the laboratory over 31 copies of one
file. **Built as a classification, deposited as none** — a detector whose verdict feeds a gate is
a gate, and § 3's boundary is not crossed by naming the states.

---

## 6 · ADJFAILCLOSED — the residuals, and the question that decides it

Re-derived without reading an interpretation. **Can summary bytes remain indistinguishable from a
fully verified run?**

| State | Before | After |
|---|---|---|
| `DECLARED_PNG_CORRUPTED` | exit 0, **sha `df5b3ad14e`** | exit 0, `9a03cfc6f9` |
| `UNDECLARED_PNG_PRESENT` | exit 0, **sha `df5b3ad14e`** | exit 0, `81fc78e797` |
| `DIRECTORY_WITHOUT_ADJUDICATIONS_JSON` | exit 0, **sha `df5b3ad14e`** | exit 0, `1b5bd124a5` |
| `MALFORMED_RECIPE` | exit 1, **`KeyError: 'artifacts'`** | exit 1, a named verdict |
| CLEAN reference | `df5b3ad14e` | `2ec2c1f5ef` |

**Three states produced byte-identical output to a clean run.** The answer was **yes**, so the
candidate was not fail-closed for its declared scope. It is now: **0 indistinguishable
false-greens**, asserted by a test that requires the four to be pairwise distinct — the property,
rather than any one of them.

### 6.1 · Directory semantics — which of the two paths, and why

The tool's docstring promises *"fails closed when a digest disagrees, when the PDF is absent, or
when the PDF itself is not the one the recipe was taken from"*. Rule 5e promises *"A page
adjudication is published as a recipe, never as the image"* — and it governs what is **published**,
while these images are gitignored.

⇒ **Recipe verification, not directory adjudication integrity. Nothing was made to fail.**

| Set | Treatment |
|---|---|
| `DECLARED` · `REGENERATED` · `COMPARED` · `MATCHED` | verified, counted, reported — unchanged |
| `UNDECLARED` (image present, no recipe names it) | **observed, reported, not a failure** |
| directory with images and no `adjudications.json` | **observed, reported, not a failure** |
| `CORRUPT` (declared, on disk, bytes ≠ recipe) | **observed, reported, not a failure** |
| `MISSING` (declared, absent from disk) | 🔴 **deliberately NOT reported** — 5e ships the recipe and not the image, so absence is the designed state of a fresh checkout. Reporting it every run would fill the block with expected noise and teach a reader to skip the lines that are *not* expected |

**The `SCOPE:` line is printed unconditionally, including on a clean run**, so the boundary of the
claim is learned from the tool rather than from its source. **A gate need not check everything; it
must not be quiet about what it did not check.**

**The alternative path is named and not taken**: if rule 5e were read as requiring directory
integrity, the three observations become failures — one changed line each. That reading is a
governance question about what 5e requires, not a defect in the tool.

---

## 7 · Repository surface determinism

Same tracked tree, three verdicts from `test_documented_commands.py`:

| Condition | markdown scanned | verdict |
|---|:--:|:--:|
| `CLEAN_CLONE` | 281 | 0 |
| `WITH_GITIGNORED_MD` (one file, bad path) | 282 | 🔴 **1** |
| `WITH_NESTED_CHECKOUT` | **562** | 0 |
| `WITH_BACKUP` | 285 | 0 |
| `WITH_PRIVATE_CORPUS` | 281 | 0 |

**A file in no commit, in no clone and explicitly gitignored could turn the release battery red.**
A nested checkout **doubled** the population and the verdict survived only because the copy
happened to be self-consistent.

| Primitive | On a clean checkout | Under incidental state |
|---|:--:|---|
| `RAW_RGLOB` | 281 | 🔴 moves with anything on disk |
| `GIT_TRACKED` | 281 | misses force-added files, which do ship |
| **`walk_publishable`** | 281 | **holds at 281** |

🔴 **`walk_publishable` already exists**, in `public_release_gate.py`, and its docstring records
the measurement that produced it — *37 BLOCKs from a nested checkout, every one false*. The repair
is reuse.

**Reuse is argued, not assumed.** The prompt's warning is right that publication surface need not
equal documentation surface. They coincide here for a stated reason: **this guard exists to stop a
document promising an executable that is not there, and a document that reaches no clone promises
nothing to anybody.** Two controls hold that argument to account — a **tracked** document with a
bad path still fails, and so does a **force-added gitignored** one, which is the case a directory
allowlist would silently exempt.

**`test_fresh_clone_reader_journey` also rglobs and did NOT diverge** under any of the five
conditions. It is left alone rather than rewired on the strength of a resemblance.

---

## 8 · MAJOR-2 A and B are not equivalent

**A** — `commit its own work through \`CANONICAL_BATCH_COMMIT\`` · **B** — `commit its own work to
\`main\``

| | A | B |
|---|---|---|
| forbids | the governed **act** | the **outcome**, by any route |
| a direct non-batch commit to `main` | **not forbidden by this clause** | forbidden |
| mirrors an existing rank-1 clause | **yes — GATE 1 verbatim in structure**: *"Proponente ≠ esecutore. Solo candidate preparati da Plan; mai lavoro proprio"* | **no rank-1 clause states this in this form** |
| self-contained | no — relies on line 49 and Annex D.1 | yes |

**What rank-1 governance already settles**, and it settles less than it appears to:
`GOVERNANCE_v3.1.1.md:231` reads `CANONICAL_BATCH_COMMIT → SOLO Orchestrator, root, sotto gate
0–5. Storia canonica.` That **defines** what produces canonical history; it does not, in that
sentence, **prohibit** a direct write. A's residual route is closed instead by two other clauses,
both preserved in every variant: line 49's *"or treat the root as free working space"*, and
Annex D.1's three-type taxonomy.

⇒ **A is a materialization of GATE 1. B is a small new rule** — stricter, self-contained, and not
a restatement of anything. **They converge in effect and differ in what the clause itself asserts,
and calling them equivalent would hide exactly that.** Not chosen; no Operator decision exists.

---

## 9 · Composed integration

Every candidate passed **isolated** validation before entering, and each ordered prefix was
measured. The only conflicts are on `run_release_regressions.py`, resolved by union — correct
because `test_release_runner_verdict` reads `set(runner.TESTS)`, so position is not asserted.

| Prefix step | runner entries | mode-bit offenders | duplicate tests | fails | conflict | new failures |
|---|:--:|:--:|:--:|:--:|---|---|
| `RELSURF` | 66 | 0 | 0 | 4 | clean | *(baseline)* |
| + `CPROOT` | 67 | 0 | 0 | 4 | union | none |
| + `REPOSURFACE` | 68 | 0 | 0 | 4 | clean | none |
| + `GOVTESTS` | 70 | 0 | 0 | 4 | union | none |
| + `ADJFAILCLOSED` | 71 | 0 | 0 | 4 | union | none |
| + `P7LEDGER` | 72 | 0 | 0 | 4 | union | none |
| + `APQCONS` | 74 | 0 | 0 | 4 | union | none |
| + `ORCHMAJOR2` | 74 | 0 | 0 | 4 | clean | none |

`main` fails **6**. The composed branch fails **4**, and the four are one class.

**Zero mode-bit offenders and zero duplicate test entries at every prefix**, and no prefix
introduced a failure. The four residual failures are the CLAUDE.md router class throughout.

⚠️ **Composition is not a formality here.** The previous session's preview found a `100644`
shebang file that was invisible on its own branch, because that guard was already red there for
four other files. **A candidate can only be checked against a clean guard once an earlier
candidate has cleaned it** — which is the argument for the order, not merely for the testing.

**Candidates were not merged to avoid rehash.** Eight units, eight hashes; each of the four
runner-touching ones remains independently reviewable.

---

## 10 · Formalization minimum

| Principle | Classification | The minimum |
|---|---|---|
| **A** · control-plane path independent of cwd | **CODE_ONLY_REPAIR** | No normative text says *resolve from the working directory*, so removing it implements no new rule and breaks none. Done. |
| **B** · current authority cannot be asserted from divergent live lineages | 🔴 **ALREADY_NORMATIVE_NEEDS_ENFORCEMENT** | Annex I.3 `Un solo ACTIVE`, and **J.0 names the compensating protocol by name: `rilevazione doppio ACTIVE`.** The detection is unavailable under per-worktree records. **Nothing needs writing; something needs enforcing** — and the enforcement requires the § 3 relevance decision, which is the Operator's. |
| **C** · repository validation independent of incidental local state | **CODE_ONLY_REPAIR** | `walk_publishable` already encodes it. Reused, with controls. Done. |

**No governance text is proposed.** For B, the single proposition that would need to exist if I.3
and J.0 were judged insufficient is: *a control-plane record is one object for the laboratory, and
a reader resolves it from the repository authority root.* **It is not proposed here**, because
J.0 already promises the detection that sentence would enable.

---

## 11 · Reproduction

```bash
for d in <root> <orchestrator worktree> <a subdirectory> /tmp; do (cd $d && python3 <lease_state>); done
python3 governance/scripts/candidate_content_hash.py --base 788c357d… --tip <branch>
```

The CPROOT probe, the primitive comparison, the residual prober and the composition matrix are in
this session's scratchpad and are **not durable**. The state matrices, mutation batteries and CLI
suites **are**, inside their candidates.
