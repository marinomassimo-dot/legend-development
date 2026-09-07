# TEAM PILOT — PHASE I · authority state and measured workset

**Actor:** worktree `lettore`, branch `lettore`.
**Status:** NON-CANONICAL work artifact. No canonical file was written, no governance modified,
no actor activated, no `BATCH_COMMIT` performed.
**Public, disease-level, de-identified. Nothing here is medical advice.**

---

## 1 · Authority — determined before execution, not assumed

The dispatch requires that the actual activation state be established first and that a
`PROPOSED` role contract not be self-activated. It was established from the record, and the
record is unambiguous.

| Fact | Where measured | Value |
|---|---|---|
| `roles/scientist.md` status | `git show main:roles/scientist.md`, line 12 | `PROPOSED — binding once Mirror hostile review passes and the operator approves` |
| Operator determination on activation | `main:governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` | 🔴 **OPTION B — `ACTIVATION_NOT_CONFIRMED`** |
| Consequence 2 of that decision, verbatim | same file | *"No actor authority may be assumed from these contracts."* |
| Consequence 3 | same file | *"A new, explicit activation act is required before any actor relies on these contracts as binding."* |
| Companion gloss on the same status grammar | `main:framework/protocols/scientist_reading_modes.md` frontmatter | *"Until then it binds nobody."* |
| Hostile review of the four contracts | `REV-ROLES-MIRROR-001` as cited in the decision, §E-6 | `CHANGES_REQUIRED` on three of four; no verdict on `roles/mirror.md` |

### 1.1 What I therefore operated under

**`OPERATING_AUTHORITY: OPERATOR_DIRECTED_ANALYTICAL_PILOT`.**

The canonical Scientist contract is **not binding**. This session is an Operator-directed
analytical pilot and nothing more. Concretely, the authority actually exercised was:

- read canonical state read-only;
- read primary evidence artifacts from the shared checkout;
- write non-canonical work artifacts under `learning/scientist/` on branch `lettore`;
- commit those artifacts to my own branch.

Authority **not** exercised, and not available to be exercised: canonical mutation, governance
edit, relation-vocabulary creation, actor activation, `BATCH_COMMIT`, merge to `main`.

🔴 **The scientific discipline is unaffected by this.** Parity of sources, the ban on grep as a
method of analysis, verbatim locators captured while the document is open, structured surfaces
preferred over PDFs, figures inspected at original resolution, negatives scoped to their
denominator — those bind through `CLAUDE.md` and the framework protocols, which were installed
and bind on their own terms. The contract being `PROPOSED` removes *role authority*, not
*method*.

### 1.2 Identity — established, not accepted from the dispatch

The dispatch states that *"Scientist-B has already produced a NON-CANONICAL pilot on PMID
32000863"*, and directs Scientist A and Scientist C to adjudicate independently. A dispatch does
not establish who its reader is, so the addressee was verified rather than assumed.

| Evidence | Result |
|---|---|
| `main:roles/scientist.md` frontmatter | `worktrees: {scientist-a: lettore, scientist-b: lettore-b, scientist-c: lettore-c}` |
| My worktree | `<REPO_ROOT>/.claude/worktrees/lettore`, branch `lettore` |
| Prior artifacts held in my worktree | `framework/protocols/scientist_evidence_standard.md` and `scientist_operating_practice_v1.md`, both self-declaring *"Scientist A, branch `lettore`"* |
| Peer branch `lettore-b`, path names only | carries `reviews/scientist-b/PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_SCIB_v1.md`, committed |

⇒ **I am Scientist A.** Two independent lines agree, and the dispatch's statement about B is
confirmed rather than merely believed: B's pilot exists, is a different file from mine, and is
durable on B's branch. The prior pilot held in *my* worktree is mine, not B's — the two were
produced independently and both exist.

The mapping is recorded in a document that binds nobody (§1). It is used here as the best
available *addressing* fact, not as a grant of authority.

---

## 2 · Source-tree state, measured

| Fact | Value |
|---|---|
| Branch `lettore` vs local `main` (`788c357`) | **201 behind, 0 ahead** — HEAD `9b0cf47` is a strict ancestor of `main` |
| Refs enumerated when making absence claims | **57** |
| Dirty in my worktree, not authored by me this session | `M disease-models/wwox/research/deepdive_manifests/PMID42422765.json` |

**I did not fast-forward, and the reason is specific.** Normally a branch with zero commits of
its own should be fast-forwarded before anything is measured — measuring a tree nobody has is
the failure this repository has already paid for. It is *not* safe here: `main` modifies the one
file my worktree holds dirty (`PMID42422765.json`), and I did not author that edit. Clearing the
way would be a destructive write over another actor's uncommitted work, which is the exact
failure the one-actor-one-worktree rule exists to prevent.

🔴 **So every canonical quotation in these artifacts was read non-destructively from `main` via
`git show main:<path>`, never from my own checked-out tree**, and each says so at the point of
use. Evidence artifacts were read from the shared checkout's `files/` — `.gitignore` excludes
`files/`, so a branch carries the manifest and never the evidence, and the shared checkout is
the only tree that will still hold them tomorrow.

---

## 3 · The workset — re-measured, not inherited

The dispatch supplies expected counts and instructs that they be re-measured. They were, from
the generated inventory rather than from the dispatch.

**Canonical task surface:** `legend-operating-convention-v1:disease-models/wwox/analysis/pathograph_inventory.md`,
regenerated from `pathograph.py` under `framework/scripts/` on that same branch.

> 🔴 **Paths qualified by ref, 2026-08-26.** Both objects live on
> `legend-operating-convention-v1` and on no other head. This note said the surface was untracked
> in the very next line, and still wrote the paths as if a reader could open them — the location
> claim and the existence claim were separated by one sentence and disagreed.

🔴 **The surface is untracked.** `pathograph` appears on **0 of 57 refs**. The inventory, its
export (`data/pathograph_export.jsonl`), the assembler and its test exist **only as untracked
files on the shared checkout's disk**. There is no canonical task packet: `ledger/tasks/` holds
`plan/` and nothing else on every one of the 57 refs. This is reported as a finding, not worked
around — see §6.

### 3.1 Counts

| Measure | Dispatch expected | **Measured** | Agreement |
|---|---|---|---|
| Current edges | ~20 | **20** | ✅ |
| …with a shared evidential paper | ~17 | **17** | ✅ |
| …without one | ~3 | **3** | ✅ |
| Edges carrying a declared relation type | — | **0** | all 20 are `UNTYPED` |
| Claim nodes | — | 39 | |
| Nodes carrying a biological scale | — | 0 | |

The three edges with **no** shared evidential paper: `CLAIM 001<->CLAIM 002`,
`CLAIM 003<->CLAIM 004`, `CLAIM 030<->CLAIM 033`.

**Governed relation vocabulary**, from the inventory's own statement of what the assembler
accepts — and the only vocabulary used anywhere in these artifacts:

```
DIRECT · INDIRECT_UNKNOWN_INTERMEDIATES · ASSOCIATED · CONTROVERSIAL_OPEN
```

No token outside that set was used, proposed or implied.

### 3.2 🔴 Adjudicability triage — which edges can actually be adjudicated *today*

The dispatch orders the work as (B) edges with a shared evidential paper first, (C) edges
without one separately. **That ordering is not sufficient**, and the reason is a measurement the
dispatch could not have known: *having* a shared evidential paper does not mean the paper's
primary evidence is reachable. Four of the seventeen name a paper the registry records as read
whose artifact is not on this disk and which has no deep-dive manifest.

Derived mechanically (edge table × paper registry identifiers × `files/fulltext/` ×
`deepdive_manifests/`), not by hand:

| Class | Edges | Meaning |
|---|---|---|
| `PRIMARY_AVAILABLE` | **12** | ≥1 shared paper with a local artifact **and** a deep-dive manifest — adjudicable now |
| `ARTIFACT_ONLY_NO_MANIFEST` | **1** | artifact on disk, no manifest; PDF-only surface, so `CLAUDE.md` §5d applies before any locator |
| `SHARED_PAPER_NO_LOCAL_ARTIFACT` | **4** | the shared paper exists in the registry; its evidence does not exist on this disk |
| `NO_SHARED_PAPER` | **3** | no shared evidential paper at all |
| | **20** | |

Per edge:

| Edge | Class | Shared evidence, resolved |
|---|---|---|
| CLAIM 005 <-> CLAIM 036 | `PRIMARY_AVAILABLE` | PAPER 057 = PMID 19936220 (3 artifacts, manifest) |
| CLAIM 005 <-> CLAIM 037 | `PRIMARY_AVAILABLE` | PAPER 058 = PMID 19500159 (3, manifest) |
| CLAIM 009 <-> CLAIM 028 | `PRIMARY_AVAILABLE` | PAPER 054 = PMID 34214506 (1, manifest) |
| CLAIM 009 <-> CLAIM 034 | `PRIMARY_AVAILABLE` | PAPER 054; PAPER 071 = PMID 21075834 (1, manifest) |
| **CLAIM 016 <-> CLAIM 035** | `PRIMARY_AVAILABLE` | PAPER 056 = PMID 22193544 (3, manifest) — **adjudicated, artifact 02** |
| CLAIM 028 <-> CLAIM 034 | `PRIMARY_AVAILABLE` | PAPER 054 |
| CLAIM 028 <-> CLAIM 035 | `PRIMARY_AVAILABLE` | PAPER 056 |
| CLAIM 030 <-> CLAIM 032 | `PRIMARY_AVAILABLE` | PAPER 039 = PMID 34268881 (3, manifest, **partial** read); PAPER 041, 043 unreachable |
| CLAIM 030 <-> CLAIM 035 | `PRIMARY_AVAILABLE` | PAPER 056 |
| CLAIM 036 <-> CLAIM 038 | `PRIMARY_AVAILABLE` | PAPER 057 |
| CLAIM 037 <-> CLAIM 038 | `PRIMARY_AVAILABLE` | PAPER 058; PAPER 059 = PMID 17803050 (3, manifest) |
| CLAIM 037 <-> CLAIM 039 | `PRIMARY_AVAILABLE` | PAPER 059 |
| CLAIM 019 <-> CLAIM 033 | `ARTIFACT_ONLY_NO_MANIFEST` | PAPER 040 = PMID 33916893 — PDF only, no manifest |
| CLAIM 001 <-> CLAIM 031 | `SHARED_PAPER_NO_LOCAL_ARTIFACT` | PAPER 045 = PMID 30361190 — 0 artifacts |
| CLAIM 019 <-> CLAIM 030 | `SHARED_PAPER_NO_LOCAL_ARTIFACT` | PAPER 041 = PMID 29808465; PAPER 042 = PMID 24369382 — 0 artifacts each |
| CLAIM 019 <-> CLAIM 032 | `SHARED_PAPER_NO_LOCAL_ARTIFACT` | PAPER 041 — 0 artifacts |
| CLAIM 031 <-> CLAIM 032 | `SHARED_PAPER_NO_LOCAL_ARTIFACT` | PAPER 049 = PMID 27495153 — 0 artifacts |
| CLAIM 001 <-> CLAIM 002 | `NO_SHARED_PAPER` | — |
| CLAIM 003 <-> CLAIM 004 | `NO_SHARED_PAPER` | — |
| CLAIM 030 <-> CLAIM 033 | `NO_SHARED_PAPER` | — |

### 3.3 🔴 Two findings that fall out of the triage and matter beyond it

**(a) The Q230P edge cluster rests on a paper LEGEND has never read in full.**
`PAPER 041` = PMID 29808465 (Johannsen 2018) is the shared evidence for **three** edges —
`019<->030`, `019<->032`, `030<->032` — and the paper registry records its evidence depth as
*"abstract only — full text paywalled"*. `CLAIM 019` is `consolidated baseline`. Under
`CLAUDE.md` §8 an abstract is not a reading and cannot clear reading debt; it follows that three
edges of the Q230P cluster **cannot be typed from primary evidence at all** until that full text
is acquired. This is not a defect in the claims — it is a bounded, nameable acquisition task.

**(b) Four papers the registry records as fully read have no artifact and no manifest.**
PMIDs 24369382, 24456803, 30361190, 27495153 are each recorded as `full text reviewed` /
`coverage_status: complete_fulltext_read`, and each has **0 files in `files/fulltext/`** and no
deep-dive manifest. The readings may well have happened; what is measurable today is that
**their inputs are gone**, and a verdict whose inputs are gone is a memory of a verification
rather than a verification. Any edge typed from them today would be typed from prose about a
paper, not from the paper.

Both findings are reported to the Operator and to whoever routes the next phase. **Neither is
mine to repair**, and neither was worked around.

---

## 4 · What Phase I of this actor produced

| # | Artifact | Content |
|---|---|---|
| 00 | this file | authority, identity, tree state, workset, adjudicability triage |
| — | `PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_LETTORE_v1.md` | **pre-existing first pass, preserved byte-unchanged** and made durable by commit |
| 01 | `TEAM_PHASE1_LETTORE_01_PMID32000863_ADDENDUM.md` | closes dispatch questions 4, 7 and extends 8 with new primary work |
| 02 | `TEAM_PHASE1_LETTORE_02_EDGE_CLAIM016_CLAIM035.md` | full per-edge adjudication in the dispatch's §5 schema |
| 03 | `TEAM_PHASE1_LETTORE_03_OPERATING_PRACTICE.md` | §13 process observations |
| — | `HANDOFF_LETTORE_TEAM_PHASE1.md` | §17 closure |

**`RESUMED_FROM_MILESTONE`.** The first pass on PMID 32000863 already existed in durable-on-disk
form when this session began. It was **not rewritten** — the dispatch forbids rewriting a
preserved first pass, and the idempotent-resume discipline says a milestone whose evidence
already exists is skipped rather than redone. It was verified for coverage against the eight
dispatch questions instead, and the two it did not fully answer were answered in a **separate
addendum** that leaves the original intact.

---

## 5 · 🔴 Phase II gate — measured, and it is CLOSED

> ### 🔴 CORRECTION — 2026-08-25, Phase II
>
> **The verdict recorded below is FALSE. The text is left standing so the error stays readable.**
> Scientist C committed `PHASE1_PMID32000863_SCIC_FIRSTPASS_v1.md` at **15:37:28** (`lettore-c`
> `c55c25c`, blob `4be1f97`, 41 547 B). My handoff declaring the gate closed is timestamped
> **15:43:51** — six minutes and twenty-three seconds later. **The gate was open and I reported it
> shut**, then repeated the claim in a cross-session reply after all four of my commits, without
> re-measuring.
>
> The commit count below (*"0 commits ahead of `main`"*) came from a path-blind
> `git log main..lettore-c` and was correct at the instant it ran; the fault is the republication
> of a decayed figure. The *untracked* check beside it was directory-scoped to
> `learning/scientist/` and would have missed C had C written elsewhere — the mirror image of the
> sweep by which C missed Scientist B in `reviews/scientist-b/`. **Two distinct faults, two
> distinct repairs:** re-measure at publication, and enumerate the population rather than let a
> directory convention define it.
>
> Full account: [`PHASE2_CROSS_REVIEW_LETTORE_v1.md`](PHASE2_CROSS_REVIEW_LETTORE_v1.md) § 0.3.

§3 of the dispatch: *"Only after all three first-pass artifacts exist may Phase II begin."*
§12: *"Only after A and C have durably recorded independent outputs may they read Scientist-B's
pilot."*

Measured by **path names only** — no peer artifact content was opened, and none of the file
contents below was read:

| Actor | First pass on PMID 32000863 | Durable? |
|---|---|---|
| **A** (`lettore`, me) | `learning/scientist/PILOT_PMID32000863_…_LETTORE_v1.md` | untracked at session start → **committed by this session** |
| **B** (`lettore-b`) | `reviews/scientist-b/PILOT_PMID32000863_…_SCIB_v1.md` | ✅ committed, 4 commits ahead of `main` |
| **C** (`lettore-c`) | ❌ **none** — its only pilot is `PILOT_PMID33914858_FULLTEXT_DEEPDIVE_SCIC_v1.md`, a **different paper** | 0 commits ahead of `main`; everything it holds is untracked |

⇒ **Phase II cannot legitimately begin, and I did not read Scientist B's pilot.**

The gate fails on C, not on B: C has recorded no first pass on this paper, durably or otherwise.
Reading B's artifact now would consume the one property the whole exercise is built to
produce — three independent readings of one paper — to buy a few hours. That trade is not mine
to make, and the cost is asymmetric: independence, once spent, cannot be restored by noticing
later that it was spent.

**This is the correct blocking condition to escalate.** It is a routing fact, not a scientific
one, and §15 puts routing with Orchestrator.

---

## 6 · Findings about the exercise's own surfaces

1. 🔴 **No canonical Scientist task packet exists.** `ledger/tasks/` contains only `plan/` on all
   57 refs. The workset was recovered from a generated inventory that is itself untracked. The
   dispatch says *"Do NOT infer the workset from this prompt if a canonical packet exists"* — no
   packet exists, so the measured inventory was used and the divergence is reported here.
2. 🔴 **Two of three scientists' work lives only on the untracked surface.** Mine did at session
   start; C's still does. Scientist B's own commit message names the same problem — *"The
   first-pass artifacts existed only on the surface nobody gates."* Three actors independently
   hitting one failure mode is a property of the working method, not three coincidences. The
   fix is one line of discipline — a first pass is not recorded until it is committed — and it
   belongs in whatever contract eventually binds.
3. **Framework-surface placement, flagged rather than repaired.** My worktree holds two
   untracked files under `framework/protocols/` authored by Scientist A in prior sessions. Both
   declare themselves `PROPOSED` / non-canonical in their own headers. A Scientist writing into
   `framework/protocols/` puts a proposed artifact on a canonical-looking path, where a future
   reader finds it by location and not by frontmatter. **I did not move, edit or rename them** —
   placement of a framework artifact is not a Scientist call. Committed unchanged so they stop
   being invisible; adjudication belongs to Plan or Mirror.
4. **`PMID42422765.json` is dirty in my worktree and was not authored by me.** Not committed,
   not reverted, not staged.

---

*Non-canonical. Nothing here is medical advice. No canonical file was modified in producing it.*
