# COMMIT CANDIDATE — candidate metadata: Base head is derivable, Author is not, and the difference is measurable

**Candidate ID:** CC-20260826-CANDIDATE-METADATA-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** answers Plan's observation that Scientist B candidates carry `Author`, `Base head` and a
parseable change class. **Adds no schema.**
**Change class:** MINOR — header lines on this branch's own candidates only
**Canonical targets:** none
**Base head:** `ccddc28939234ad4fe29c417935a0dbe11de86d0` (branch `lettore`)
**Batch gate:** intentionally untouched

---

## 1. `Author` — 🔴 **UNDERIVABLE**, and here is the measurement that says so

```bash
git log --format='%an <%ae>' -- disease-models/wwox/research/commit_candidates/ | sort | uniq -c
git log --format='%an <%ae>' | sort | uniq -c
```

| Scope | Distinct identities | Value |
|---|---|---|
| Commits touching `commit_candidates/` | **1** | display name `The LEGEND project`, one `noreply` project address — **28 of 28** |
| Whole repository | **1**, in two spellings | 488 commits on the `noreply` project address + 5 on a placeholder-domain variant of the same project name |

> ⚠️ **The two addresses are deliberately not printed.** A first draft quoted them literally and
> `scripts/public_release_gate.py` returned `BLOCK_PUBLICATION · EMAIL_ADDRESS` on this file, at
> these two lines. The gate was right and the quotation was unnecessary: the finding is *"one
> identity, shared"*, and the counts carry it. **The block was repaired, not bypassed** — and it is
> recorded because a metadata candidate that trips the privacy gate while arguing about provenance
> is worth leaving legible.

⇒ **The git author field is a shared project identity, not an actor.** It cannot distinguish
Scientist A from Scientist B from Plan from the Orchestrator, because every commit in the
repository's history carries the same name.

🔴 **Writing `Author: Scientist A` into these candidates would be fabricated provenance.** It would
assert something no artefact in the repository records and no command can check. **Not done.**

### What *is* derivable, and is not authorship

```bash
git branch --contains <add-commit> --format='%(refname:short)'
```

Every candidate examined below returns exactly **one** branch: `lettore`. That is an objectively
derivable **workstream** attribution — it says which line of work the file was committed on. It is
strictly weaker than authorship: a branch can carry more than one actor's work, and a merge would
make it carry more. **Recorded as `Branch`, never as `Author`.**

⚠️ And it decays. `git branch --contains` returns *"every branch that now contains this commit"*.
The single-branch answer above is true at `ccddc28939234ad4fe29c417935a0dbe11de86d0`; it becomes
false the moment the branch merges. **The value must be read as dated, or re-derived.**

---

## 2. `Base head` — ✅ **derivable**, with one distinction that must travel with it

The parent of the commit that first added the file:

```bash
add=$(git log --diff-filter=A --format=%H -- <path> | tail -1); git rev-parse "${add}^"
```

🔴 **This is the base head of the *commit*, not of the *reading*.** Two measurements from this
branch make the gap concrete rather than theoretical:

| Observation | Evidence |
|---|---|
| **One commit added eight candidates.** `57bcbde2` added `CLAIM002`, `CLAIM003`, `CLAIM032`, `CLAIM037`, `INDEX-PRIORITY`, `PROVENANCE-01`, `ADVERSARIAL-FALSIFICATION-01` and more — all with base `605fc5de` | eight documents, one base head. The value describes the commit; it says nothing about which tree each document was written against |
| **A candidate's own ID date precedes its add date.** `CC-2026**0825**-ADVERSARIAL-FALSIFICATION-01.md` was added on **2026-08-26** in `57bcbde2` | the document existed before the commit that carries it. **Its base head is not the tree its author read** |

⇒ `Base head` is honest as *"the tree this file's first commit was made on top of"* and dishonest
as *"the state the analysis was performed against"*. **Only the first reading is recorded.**

⚠️ A second ambiguity: `Base head` of the **add** commit and of the **last** commit differ for every
file edited after creation — e.g. `FIVECLAIM-PACKAGE-01` (add `57d08811`, last `ccddc289`),
`LOCATOR-PACKET-01` (add `57d08811`, last `fe21ee82`). **A bare "Base head" with no commit named is
under-specified.** The field below always names which.

---

## 3. Derived values — this branch's 2026-08-25/26 candidates

Measured at `ccddc28939234ad4fe29c417935a0dbe11de86d0`. **Every cell is a command output.**

| Candidate | Add commit | **Base head (of add)** | Last commit | Branch | Author |
|---|---|---|---|---|---|
| `CC-20260825-ADVERSARIAL-FALSIFICATION-01` | `57bcbde2` | `605fc5de` | `57bcbde2` | `lettore` | 🔴 underivable |
| `CC-20260826-BLIND-REPLICATION-NOTRUN-01` | `bcd1cc5e` | `ba7da24f` | `bcd1cc5e` | `lettore` | 🔴 underivable |
| `CC-20260826-CLAIM002-01` | `57bcbde2` | `605fc5de` | `57bcbde2` | `lettore` | 🔴 underivable |
| `CC-20260826-CLAIM003-01` | `57bcbde2` | `605fc5de` | `57bcbde2` | `lettore` | 🔴 underivable |
| `CC-20260826-CLAIM006-01` | `23f4419c` | `fe21ee82` | `23f4419c` | `lettore` | 🔴 underivable |
| `CC-20260826-CLAIM032-01` | `57bcbde2` | `605fc5de` | `57bcbde2` | `lettore` | 🔴 underivable |
| `CC-20260826-CLAIM037-01` | `57bcbde2` | `605fc5de` | `57bcbde2` | `lettore` | 🔴 underivable |
| `CC-20260826-CROSS-CLAIM-CENSUS-01` | `ba7da24f` | `2d954fdc` | `ed4f1779` | `lettore` | 🔴 underivable |
| `CC-20260826-CROSS-CLAIM-CENSUS-02` | `6e4ae60b` | `57d08811` | `ccddc289` | `lettore` | 🔴 underivable |
| `CC-20260826-DOSE-ADJUDICATION-01` | `ed4f1779` | `4f8643c4` | `ed4f1779` | `lettore` | 🔴 underivable |
| `CC-20260826-DOSE-TRANSFERABLE-QUANTITY-01` | `23f4419c` | `fe21ee82` | `23f4419c` | `lettore` | 🔴 underivable |
| `CC-20260826-EGABA-ANALYSIS-PLAN-01` | `ccddc289` | `23f4419c` | `ccddc289` | `lettore` | 🔴 underivable |
| `CC-20260826-EGABA-EXPERIMENT-01` | `ba7da24f` | `2d954fdc` | `6e4ae60b` | `lettore` | 🔴 underivable |
| `CC-20260826-FIVECLAIM-PACKAGE-01` | `57d08811` | `ed4f1779` | `ccddc289` | `lettore` | 🔴 underivable |
| `CC-20260826-INDEX-PRIORITY` | `57bcbde2` | `605fc5de` | `57bcbde2` | `lettore` | 🔴 underivable |
| `CC-20260826-LOCATOR-PACKET-01` | `57d08811` | `ed4f1779` | `fe21ee82` | `lettore` | 🔴 underivable |
| `CC-20260826-PMID36828035-01` | `ba7da24f` | `2d954fdc` | `7ff7995f` | `lettore` | 🔴 underivable |
| `CC-20260826-PMID36828035-02` | `ed4f1779` | `4f8643c4` | `ccddc289` | `lettore` | 🔴 underivable |
| `CC-20260826-PROVENANCE-01` | `57bcbde2` | `605fc5de` | `6e4ae60b` | `lettore` | 🔴 underivable |
| `CC-20260826-PROVENANCE-PAPER007-01` | `57d08811` | `ed4f1779` | `57d08811` | `lettore` | 🔴 underivable |
| `CC-20260826-REVIEW-INDEX` | `6e4ae60b` | `57d08811` | `7ecbe437` | `lettore` | 🔴 underivable |
| `CC-20260826-SEIZURE-RECONCILIATION-01` | `ba7da24f` | `2d954fdc` | `ba7da24f` | `lettore` | 🔴 underivable |
| `CC-20260826-UPSTREAM-CITATION-FAILURE-01` | `bcd1cc5e` | `ba7da24f` | `bcd1cc5e` | `lettore` | 🔴 underivable |

**23 rows. `Base head` derived for 23 of 23. `Author` derivable for 0 of 23.**

The six candidates written in this run —
[`FIVECLAIM-HARDENING-01`](CC-20260826-FIVECLAIM-HARDENING-01.md),
[`CLAIM006-HARDENING-01`](CC-20260826-CLAIM006-HARDENING-01.md),
[`DOSE-DECISION-TABLE-01`](CC-20260826-DOSE-DECISION-TABLE-01.md),
[`PMID36828035-DURABILITY-01`](CC-20260826-PMID36828035-DURABILITY-01.md),
[`EGABA-CLOSURE-01`](CC-20260826-EGABA-CLOSURE-01.md) and
[`CROSS-CLAIM-CENSUS-03`](CC-20260826-CROSS-CLAIM-CENSUS-03.md) — each carry
`**Base head:** ccddc28939234ad4fe29c417935a0dbe11de86d0` in their headers. 🔴 **For those six that
value is not a post-hoc derivation: it is the head the work was performed against, recorded while
it was true.** That is the only circumstance in which `Base head` means what a reader assumes it
means, and it is recorded here as the reason to write the field **at authoring time** rather than
reconstruct it later.

---

## 4. Change class — already parseable, and the gap is elsewhere

```bash
python3 framework/scripts/candidate_durability_index.py
```

| Property | Count | Note |
|---|---|---|
| `TRACKED` | **41 / 41** | at run time |
| `COMMITTED` | **41 / 41** | |
| `BASE_DECLARED` | 34 / 41 | |
| `CHANGE_CLASS_DECLARED` | 20 / 41 | |
| `CANONICAL_TARGETS_DECLARED` | 27 / 41 | |
| `LOCATOR_AUDIT_TRIGGER_DECLARED` | 5 / 41 | |

⚠️ **Object-derived and dated.** The population was **38** when
[`CC-20260826-REVIEW-INDEX`](CC-20260826-REVIEW-INDEX.md) measured it earlier the same day and is
**41** now. **Re-run rather than cite.**

🔴 **Every gap is in the sixteen pre-2026-08-25 candidates**, which predate the fields.
**Not retrofitted** — the queue forbids fabricated provenance, and a change class inferred now for
a 17-line record written on 2026-08-10 would be exactly that. Their absence is the honest signal
that they are unrouted by the modern fields.

---

## 5. What is proposed, and what is not

**Proposed — for this branch's own candidates only, using fields that already exist in prose:**

| Field | Value | Basis |
|---|---|---|
| `**Base head:**` | full 40-char SHA **with the branch named inline**, e.g. `ccddc28939234ad4fe29c417935a0dbe11de86d0 (branch lettore)` | §1 + §2 |

⚠️ **One field, not two.** A first draft of this section proposed a separate `**Branch:**` line. The
six candidates written in this run already carry the branch **inside** `Base head`, so a second
field would have added a parse target and no information. **Dropped rather than shipped** — a
proposal that changes no behaviour still costs a governance cycle.

**Explicitly NOT proposed:**

- 🔴 **`Author`.** Underivable; §1 is the measurement. Where a reader expects it, the honest entry
  is *"underivable — the git author field is a shared project identity; see
  `CC-20260826-CANDIDATE-METADATA-01` §1"*.
- **No new schema, no machine-readable header block, no YAML front-matter.** All four fields are
  prose lines the existing candidates already use, and
  `candidate_durability_index.py` already parses them by regex.
- **No retrofit** of the sixteen legacy candidates.
- **No change** to `candidate_durability_index.py`. Adding `Author`/`Branch` columns would create a
  gap metric for a value that is underivable by construction, which is worse than not measuring it.

---

## 6. The general lesson, stated once

**`Base head` is provenance of the commit; `Author` is provenance of nothing.** Both look like
document metadata and only one is. The distinguishing test is whether a command can return the
value from the artefact — and for `Author`, in this repository, none can. A field that must be
typed in by the thing it describes is an **attestation**, not a measurement, and it should be
labelled as one or omitted.
