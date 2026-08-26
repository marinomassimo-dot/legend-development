---
record_type: WORK_ANALYSIS
id: PLAN-QUEUE-AND-CANDIDATE-CENSUS-001
title: Four approvals invisible on main, and a candidate census whose first two measurements were wrong
date: 2026-08-26
role: PRODUCER
mode: ANALYSIS_FIRST / MINIMAL_DELTA
authority: Plan role contract — Annex J.1 derived-view mandate; candidate preparation on own
  branch. No canonical merge performed. No scientific content read for judgement.
status: ANALYSIS_COMPLETE — CAND-20260826-APQCONS prepared; canonical merge NOT executed
---

# APPROVAL QUEUE RECONCILIATION, AND THE SCIENTIFIC CANDIDATE CENSUS

> **Nothing here is medical advice.** § 5 measures scientific candidates as objects and forms no
> view on any biological claim in them.

---

## 1 · The three lineages, enumerated before being measured

`ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl`, over all 47 local heads and 4 remote-tracking refs:

| Lineage | Blob | Records | Bytes | Refs carrying it |
|---|---|:--:|:--:|---|
| **L1** | `20c24a2b` | 6 | 9 379 | **`main`** + 30 others |
| **L2** | `95fc8163` | 14 | 14 088 | `evidence-index`, `p51c9-rebased-onto-c89c2217` |
| **L3** | `bb603d9a` | 10 | 43 357 | **`orchestrator` alone** |

🔴 **`main` carries the shortest.** A reader of the canonical branch sees **6 records of 18** and
has no way to discover that the other twelve exist.

**What is invisible on `main`, by identity:**

| Identity | State | Only on |
|---|---|---|
| `APR-20260818-SUNSET-DEC3-001` | **APPROVED** | `orchestrator` |
| `APR-20260819-SCIAB-001` | **APPROVED** | `orchestrator` |
| `APR-20260819-XPORT-001` | **APPROVED** | `orchestrator` |
| `APR-20260819-P5DOMAIN-001` | **APPROVED** | `orchestrator` |
| `APR-20260817-HA-1…4` + `RES-20260817-HA-1…4` | PENDING / APPROVED · DEFERRED · RESOLVED · DEFERRED | `evidence-index` |

**Four operator approvals, all in state `APPROVED`, exist on one ref of fifty-one.** That is the
objective stated plainly: *no valid approval should be invisible merely for living on a side ref.*

⚠️ **The first sweep for this file returned nothing at all.** It looked under `ledger/` and the
file is under `ledger/approvals/` — a wrong path produces an empty result and no error, and an
empty result reads exactly like *"this file exists nowhere"*. It was caught only because a
positive control was run beside it. **A per-ref sweep without a control is not a measurement.**

---

## 2 · Every reconciliation property, measured

| Property | Measured value | How |
|---|---|---|
| **Common prefix** | **6 records, byte-exact** | `head -6 L2 \| cmp - L1` and the same for L3 — a byte comparison of raw lines, not a field-by-field one |
| **Unique suffixes** | L2 **+8** (all `2026-08-17`) · L3 **+4** (`2026-08-18`, `2026-08-19`) | set difference on declared identity |
| **Stable IDs** | `APPROVAL_ID` · `RESOLUTION_ID` · `CORRECTION_ID` — **18 distinct across the union, 0 collisions** | every record but the schema header declares one |
| **Duplicates** | **12** — the 6-record prefix, counted three times. Zero *within* any lineage | identity census |
| **Conflicts** | 🔴 **zero.** The 6 shared identities are **byte-identical** in all three | sha256 per record, compared across lineages |
| **Ordering** | see § 2.1 — **the timestamps cannot totally order the queue** | granularity census |
| **Simple union deterministic?** | **yes, conditionally** — see § 2.2 | six-permutation test |
| **Rechain required?** | 🔴 **no.** **0 of 30** records carry a prev-hash — the queue is append-only but is **not** a hash chain | field census |
| **Provenance** | not carried by any record; must be **added**, and therefore must not go into the records | § 2.3 |

### 2.1 · The ordering signal is too coarse, and the records say so themselves

| Granularity | Count |
|---|:--:|
| date only, e.g. `2026-08-16` | **24 of 27** timestamped input records |
| full ISO with time, e.g. `2026-08-19T13:02:58Z` | 3 |
| no timestamp at all | 1 — the schema header |

And the schema already documents the cause: **`TIMESTAMP_PRECISION: "date only — the runtime
exposed no wall-clock time"`**, present on 9 records.

⇒ **A sort by timestamp alone cannot order this queue.** Eight records share `2026-08-17`; five
share `2026-08-16`. Any tie-break that is not already in the data would be an order this
consolidator *invented*.

### 2.2 · So: is a simple union deterministic? **Yes, and the condition is not cosmetic**

| Test | Result |
|---|---|
| all **6 permutations** of the order the lineages are supplied in | **byte-identical output**, fingerprint `a249f4e1…` |
| **reversing record order inside each lineage** | 🔴 **different output**, `536f75d7…` |

**The second row is not a defect and is not being reported as one.** Because most records share a
day, a record's **position in its own append-only file is the only surviving evidence of what
followed what.** Preserving it is right precisely because the sources are append-only — there,
position *is* chronology.

⇒ **The union is a function of the sources' content and of each source's internal order — not of
content alone.** That is a declared limitation with a test asserting it stays true, rather than a
tie-break that quietly manufactures an order. The alternative — dropping to identity-sort — would
be deterministic and would reorder eight same-day records against the sequence in which the
operator actually resolved them.

### 2.3 · Provenance goes beside the records, never inside them

Which lineage a record came from is **information the sources do not carry**. Writing it into a
record changes that record's bytes — and byte-identity of the shared prefix is exactly what makes
the dedup lossless. **Injecting provenance would destroy the property that licenses the merge.**

⇒ A sidecar keyed by identity: `{identity, lineages[], sha256, timestamp, state}`. Two tests assert
that no returned record is mutated and that no provenance key appears inside one.

---

## 3 · The consolidator

`CAND-20260826-APQCONS` — branch `plan-approval-queue-consolidator`, `BASE_HEAD 788c357d`, tip
`49303afd`, `CANDIDATE_CONTENT_HASH b9ee0ae7036e65b22e721226bfe5fb69ed8902725daf59293ce6c45c91123ad8`.

`consolidate_approval_queue.py` and its 16-test suite, both under `governance/scripts/`, plus the
one inventory line its own runner guard demands.

**It produces a view and a provenance sidecar. It does not write the canonical file.** The
canonical merge was **not** executed and is not requested by this record.

| Test class | What it holds |
|---|---|
| `TheFixtureMatchesTheRealShape` | 3 tests asserting the fixture still has the prefix, the date-disjoint suffixes and the coarse timestamps. **If these drift, every other test is measuring something else.** |
| `TheViewIsDeterministic` | 6-permutation agreement **and** the paired arm requiring internal-order reversal to change the output |
| `TheViewIsLossless` | every input record reaches the view; the prefix dedupes exactly once; **the four side-ref approvals survive** |
| `ProvenanceIsPreservedWithoutTouchingTheRecords` | inputs unmodified, no injected key, sidecar names every lineage |
| `AConflictIsRefused` | a mutated rationale raises · a mutated `STATE` alone raises · **and the control: the unmutated call succeeds** |
| `RecordsWithoutADeclaredIdentity` | kept and content-addressed, and two identical ones collapse |

**16 of 16 pass**, and the tool was then run against the three **real** blobs: 30 input lines →
**18 records, 12 deduped, 0 conflicts**, ordered `2026-08-16` → `2026-08-19T20:06:42Z`.

### 3.1 · Fixture — published as a recipe, not as a copy

The three lineages are already in the repository, on three refs. Copying 30 records into a fourth
file would create a fourth lineage of the object whose multiplication is the problem.

```bash
git cat-file -p 20c24a2ba478 > L1.jsonl    # main + 30 refs
git cat-file -p 95fc81639014 > L2.jsonl    # evidence-index
git cat-file -p bb603d9a270b > L3.jsonl    # orchestrator
```

The committed test fixture is a **structural skeleton** — the same identities, states, timestamps
and lineage membership, with the long rationale prose replaced — so the suite keeps every property
the consolidator reasons about without pinning itself to prose that is free to be reworded.

### 3.2 · Ordering dependency between two candidates, stated so it is not discovered at merge

`CAND-20260826-APQCONS` and `CAND-20260826-RELSURF` **both add a line to
`scripts/run_release_regressions.py`**. Whichever executes first moves the other's `BASE_HEAD`, and
the second must be rebased and re-hashed before its approval can bind under GATE 5. Same structure
as the `ORCHWT` / `P51C9` split already recorded on `main`, and stated here for the same reason.

---

## 4 · What this does not decide

- **which lineage is canonical.** The consolidator takes all three and prefers none;
- **whether the consolidated view replaces the canonical file, or sits beside it as a derived
  view.** Annex J.1 gives Plan the derived view; replacing a control-plane file under `ledger/` is
  a different act and is not performed;
- **what any `PENDING` or `DEFERRED` record means now.** Four records on L2 are unresolved and two
  are `DEFERRED`; their current standing is the Operator's, not this tool's.

---

## 5 · Scientific candidate census — objects only

**No scientific content was read for judgement.** Existence, tracking, distance, class, referenced
claims, reviewer floor.

### 5.1 · The census

**13 candidates** on `refs/heads/lettore` — twelve `CC-20260826-*` plus one `CC-20260825-*` in the
same directory. All **tracked**. `lettore` is **0 behind `main`, 21 ahead**.

| Change class | Count | Reviewer floor implied |
|---|:--:|---|
| **MINOR** | 7 | standard ladder |
| 🔴 **MAJOR** | 2 — `CLAIM037-01`, `SEIZURE-RECONCILIATION-01` | Mirror PASS **+** `HUMAN_APPROVAL` each |
| 🔴 **MAJOR + MIXED** | 1 — `CROSS-CLAIM-CENSUS-01` | as above |
| declared "none — modifies nothing" | 1 — `BLIND-REPLICATION-NOTRUN-01` | — |
| **no change class declared** | 2 — `ADVERSARIAL-FALSIFICATION-01`, `INDEX-PRIORITY` | undeterminable |

**28 distinct canonical claims** are referenced across the set, `CLAIM 001` through `CLAIM 040`.

### 5.2 · 🔴 Two measurements were wrong before they were right, and both failed toward under-reporting

**First pass — change class.** The pattern required `change_class:` at a line start. The candidates
declare `**Change class:** MINOR — …` in bold prose. It returned **"NOT DECLARED" for all 13**, and
that reads as a clean finding about the corpus rather than a broken instrument.

**Second pass** matched the label but stopped at the emoji in `**Change class:** 🔴 **MAJOR**`,
capturing a fragment of the following word. It reported **zero MAJOR**.

**Third pass** takes the whole line after the label and searches it for a class token, with a
positive control on the emoji-and-bold form. **Three candidates carry a MAJOR.**

⇒ **The wrong answer was "there are no MAJOR candidates here."** Both failures pointed the same
way — toward a lighter reviewer floor than the corpus actually demands — and neither produced any
error. A pattern that returns a confident zero is the failure mode that looks most like a result.

### 5.3 · The finding under the finding

**Change class is declared in prose, not in a machine-readable field.** There is no frontmatter, no
`change_class:` key, nothing a gate could read.

⇒ **No gate can derive the reviewer floor for a scientific commit candidate**, because the floor
depends on a value that exists only as bolded English inside a heading. That is why a mechanical
census needed three passes, and it is not a property of my regex.

### 5.4 · Durability risks

| Risk | Measured | Severity |
|---|---|---|
| **The whole set is on `lettore` and on no other ref** | 13 of 13 tracked there, `main` carries none | **not a defect** — a candidate belongs on its author's branch until it is committed |
| 🔴 **An untracked evidence object in the `lettore` worktree** | `PMID36828035.json`, in `disease-models/wwox/research/deepdive_manifests/` — the *only* untracked file there, and `CC-20260826-PMID36828035-01` is tracked | **real.** The candidate is durable; the manifest it is about is not |
| **Every candidate resting on a gitignored PDF** | 3 candidates cite `PMID33914858_Aqeilan2021.pdf`, under `files/fulltext/` — **not tracked on `lettore`, and not on this disk** | **inherent** — rule 5e, same as § 6.4 of the adjudication record |

🔴 **The untracked manifest is the reportable one.** By that candidate's own § 199–201 the manifest
*"is not emitted by this candidate"* and is to be produced by `deepdive_manifest.py` against the
shared checkout. **So the file sitting untracked in the lettore worktree is either that manifest
arriving early, or a different object with the same name** — and nothing in the repository can tell
which. Either way it is one `git clean` from gone, and a candidate whose evidence object is
untracked is a candidate whose evidence nobody else can open.

**Raised, not repaired.** It is another actor's worktree and another actor's file.

---

## 6 · Reproduction

```bash
for r in $(git for-each-ref --format='%(refname:short)' refs/heads refs/remotes); do
  git rev-parse -q --verify "${r}:ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl"; done | sort -u
git cat-file -p 20c24a2ba478 | head -6 | cmp - <(git cat-file -p 95fc81639014 | head -6)
python3 governance/scripts/candidate_content_hash.py \
  --base 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5 --tip 49303afd35b6ce6f7722d26d90874a8cb8524aac
git -C <lettore worktree> status --porcelain     # one untracked manifest
```

Note the braces in `${r}:path`. Without them zsh applies the `:r` history modifier to `$r` and the
sweep returns a silent negative on every ref.
