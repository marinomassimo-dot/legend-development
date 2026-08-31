---
record_type: WORK_ANALYSIS
id: PLAN-MIRROR-V3-MINIMUM-REPAIR-CONSOLIDATION-001
title: Consolidation of MIRROR v3 into a minimum repair set — re-measured, owned, ordered
date: 2026-08-25
role: PLAN
mode: CONSOLIDATION / MINIMUM-DELTA REPAIR PREPARATION
authority: none claimed — no lease acquired, no role contract relied upon
status: ANALYSIS_COMPLETE — repair set specified, nothing implemented, two Human Gates prepared
object: SCIENTIST_PILOT_PROCESS_HOSTILE_REVIEW_MIRROR_v3 @ mirror 77be2f4
relation_to_prior: COMPLEMENTS PATHOGRAPH_PIPELINE_HOSTILE_REVIEW_MIRROR_v2 and
  PATHOGRAPH-TRANSPORT-CONSOLIDATION-001. Supersedes neither.
personal_data: none introduced. The human role is `Operator` throughout. § 5 and § 11.1 report a
  pre-existing exposure; they name no person and quote no identifier.
---

# The three repairs Mirror sized are the right three, and two of them are aimed one step off

> **Nothing here is medical advice.** Disease-level only; no individual-level record.
> **Nothing here is canonical.** This is Plan work-analysis. It originates no actor, no control
> plane, no graph schema, no governance annex, and no stopping threshold.

---

## 0 · OBSERVATION_SCOPE

Every negative below is scoped to this table. **Local NOT_FOUND is not repo-wide NOT_EXIST**, and
**a worktree negative is not a repository negative.** Each row was re-measured in this session by
executing a command; nothing is carried from Mirror's report except where the row says so.

### 0.1 Derivation surface

| Fact | Value | How established |
|---|---|---|
| Derivation instant | `2026-08-25T20:12:08Z` | `lease_state.py` derivation clock |
| Worktree | `.claude/worktrees/evidence-index` | `pwd` |
| Branch / HEAD | `plan-orchsurf-r4-transcription` @ `e4aa80c` | `git rev-parse` |
| Divergence vs `main` | **2 behind, 56 ahead** | `git rev-list --left-right --count` |
| The 2 commits I lack | `788c357`, `2bb2700` — two files, both non-scientific | `git diff --name-only` |
| Ref population swept | **44 `refs/heads` + 6 `refs/remotes`** | `git for-each-ref` |
| Worktree population | **27** entries | `git worktree list` |
| Sweep positive control | `CLAUDE.md` present on **44 of 44** heads | required before any ref-level negative |
| `legend_lint.py .` | **PASS** (1 `[INFO]`, CLAIM 010 background-only) | run on this tree |
| `fulltext_receipts.py verify` | **OK — 128 chained, tail anchored** | run on this tree |
| `growth_anchors.py check` | **PASS** — claims 39 · papers 70 · corpus 356 · literature 390 | run on this tree |

**Scope difference from Mirror, recorded rather than reconciled.** Mirror swept `44 refs/heads + 5
refs/remotes`; I measure `44 + 6`. One remote ref has appeared since. No finding below depends on
`refs/remotes`.

### 0.2 What I could NOT reach — declared, not inferred

- **The 55-PDF corpus.** `files/` is `.gitignore` line 7 and per-worktree. Mirror's figure/no-text
  gradient, the 55/55/0 population and the `regenerate_adjudications.py verify` runtime verdict
  are **inherited, not re-derived**. This is M3-4 acting on me exactly as it acted on the four
  producer seats, and it is why § 2 marks those rows `INHERITED`.
- **The dispatch texts.** Still not durable artifacts. Unchanged from Mirror § 0.3.
- **Any biological proposition.** Plan adjudicated none, typed no edge, opened no current file for
  writing.

### 0.3 What this pass mutated

Two acts, both inside Plan's own perimeter, both reported in full at § 6.7:

1. **11 identifier occurrences removed** from 5 previously-untracked Plan records (Action 7a).
2. **This file created.** No canonical current file was opened for writing. No tracked file on any
   other actor's branch was touched.

---

## 1 · REF MAP — supplied historical ref vs current measured ref

The dispatch supplies Mirror's observation points as history. Measured now, **every one is
unchanged**: no surface moved between Mirror's review instant and this consolidation.

| Surface | Supplied by dispatch | Measured now | Δ | vs `main` |
|---|---|---|:--:|---|
| `mirror` (review artifact) | `77be2f4` | `77be2f4` | — | 0 behind, 85 ahead |
| `mirror` (derivation base) | `c7e8d6e` | `c7e8d6e` | — | 0 behind, 84 ahead |
| `main` | `788c357` | `788c357` | — | — |
| Scientist A · `lettore` | `605fc5d` | `605fc5d` | — | **201 behind**, 16 ahead |
| Scientist B · `lettore-b` | `9a09590` | `9a09590` | — | 0 behind, 16 ahead |
| Scientist C · `lettore-c` | `5b1d6c2` | `5b1d6c2` | — | 0 behind, 14 ahead |
| Orchestrator packet · `legend-operating-convention-v1` | `a58af46` | `a58af46` | — | 0 behind, 26 ahead |
| Plan · `plan-orchsurf-r4-transcription` | `e4aa80c` ("2 behind") | `e4aa80c` | — | **2 behind**, 56 ahead |

**Surfaces the dispatch names but does not stamp — measured here for the first time:**

| Surface | Measured | Consequence |
|---|---|---|
| `harden-release-scan-scoping` | `86c349a` (2026-07-31) — **456 behind `main`, 0 ahead** | The branch **exists** and is **fully merged**. It carries no unlanded work. It is a *name*, not a live workspace. See § 6.1. |
| `orchestrator` | `1e2fabd` — 37 behind, 42 ahead | Not a pilot surface; carries 13 files with the identifier form. |
| `scientist_evidence_standard.md` | present on **`lettore` only**; ABSENT on `main`, `mirror`, `lettore-b`, `lettore-c`, `legend-operating-convention-v1`, Plan | Action 4's owning object lives on **one branch, 201 commits behind `main`**. See § 4. |
| `PATHOGRAPH-TRANSPORT-CONSOLIDATION-001` | **untracked**, on disk in this worktree only; tracked on **0 of 44 heads** | Action 5's owning object is invisible to every other actor. See § 4 and § 7. |

---

## 2 · M3-1 … M3-15 — status re-measured

`CONFIRMED` = I re-derived it here. `INHERITED` = I could not reach the surface and say so.
`REFINED` = the finding stands and one of its terms moves. `PARTLY FALSIFIED` = a load-bearing
premise does not survive measurement.

| ID | Mirror's status | My status | What I ran |
|---|---|---|---|
| **M3-1** trees diverge | CONFIRMED | **CONFIRMED** | `lettore` 201 behind `main`; B and C 0 behind |
| **M3-2** contract publishes stale populations, names no ref | CONFIRMED | **CONFIRMED, sharpened** | § 0 of the standard says figures are *"true of the tree at the stated commit"* — and **states no commit anywhere in the document**. It promises the field it omits. |
| **M3-3** 448 is one of several defensible populations | CONFIRMED | **CONFIRMED, re-derived independently** | The gate's own population re-derived **statically from tracked JSON**, no PDFs needed: **3 recipes · 27 crop artifacts · 47 adjudicated locators (10 + 29 + 8)** — identical to Mirror, in a hand that did not read its code |
| **M3-4** agreement over one gitignored directory | CONFIRMED | **INHERITED — and it bound me too** | `files/` is not reachable from this worktree; § 0.2 |
| **M3-5** convergence map still reports an abandoned outcome | CONFIRMED | **CONFIRMED** | Row at `PHASE2_CROSS_REVIEW_SCIB_v1.md` still reads `ASSOCIATED` / *"resolved in A's favour"*; **1 of 16** files in B's run-diff mentions `convergence map` — the file itself. 0 amendments. |
| **M3-6** refuted falsifier in the closing artifact | CONFIRMED | **INHERITED** | Blob property established by Mirror; not re-derived, no surface added |
| **M3-7** summary under-counts its own table | CONFIRMED | **INHERITED** | Record-only; no repair depends on it |
| **M3-7a** "seven additive rounds" refuted | CONFIRMED | **INHERITED** | Record-only; § 8 keeps Mirror's instruction that it must not enter a design argument |
| **M3-8** no gate invokes `verify` | CONFIRMED | **CONFIRMED** | At `main`, `run_release_regressions.py:56` carries **only** `test_regenerate_adjudications.py`. `git grep regenerate_adjudications main -- '*.py'` → the string `verify` appears in a docstring at `regenerate_adjudications.py:38` and in **zero** executable gates. |
| **M3-9** 33.7 % of locators outside every text check | CONFIRMED | **CONFIRMED at the mechanism** | `deepdive_manifest.py`: `LOCATOR_SURFACES = {body, figure, table, supplement, abstract}` vs `TEXT_SURFACES = {body, table, supplement}`. `figure` and `abstract` are excluded **by construction**. The 338/1002 partition is INHERITED. |
| **M3-10** privacy gate blind spot | CONFIRMED | **CONFIRMED — and the discriminant is not the one named.** See § 3.1 | 5-fixture mutation battery + digest-set inspection + clean-`main` gate run |
| **M3-11** undeclared join gap = 5 pt | CONFIRMED | **INHERITED** | Needs the gitignored PDFs |
| **M3-12** Mirror handoff stale against its run | CONFIRMED | **CONFIRMED, exactly** | `PILOT_PMID32000863_MIRROR_HANDOFF_v1.md` declares `c44eb45` / `cf77cef` / `3c9969a`; actual tips are **8 · 7 · 9** commits further. `lettore-b`'s `9a09590` is current (0). |
| **M3-13** "every decisive locator came off a PNG" over-generalises | CONFIRMED | **INHERITED** | Record-only; narrows a producer claim, makes the repair cheaper |
| **M3-14** eight rounds against a frozen 2-round cap, cited nowhere | CONFIRMED | 🔴 **PARTLY FALSIFIED.** See § 3.2 | P2.2 pertinence sets · `roles/scientist.md` · run-diff citation sweep · `lease_state.py` · `REV-EVIDENCE-SCIB-001` |
| **M3-15** Plan's untracked records | CONFIRMED | **CONFIRMED, arithmetic corrected.** See § 3.3 | `git status --porcelain=v1` |

---

## 3 · THE THREE FINDINGS THAT MOVED

These are the reason this pass was worth running. In each case Mirror's finding **stands** and one
term of it does not, and in two of the three the term that moves **changes the patch**.

### 3.1 M3-10 · The blind spot is CASE, not PATH — and that changes the fix

Mirror names the defect *"blind to the lowercase **path form**"* and sizes the repair as
*"1 pattern + 2 fixtures"*, i.e. a rule that fires on the path shape.

**Five-fixture mutation battery, scanner taken from `main`, root = 5 `.md` files and nothing else:**

| # | Fixture | Verdict |
|---|---|---|
| 1 | Capitalised form, standalone prose | **BLOCK · PRIVATE_NAME** ✅ |
| 2 | Lowercase form, inside an absolute path | no finding ❌ |
| 3 | **Lowercase form, standalone prose** | **no finding** ❌ |
| 4 | **Capitalised form, inside an absolute path** | **BLOCK · PRIVATE_NAME** ✅ |
| 5 | Negative control — `Operator`, no identifier | no finding ✅ |

**Fixture 4 refutes the path hypothesis and fixture 3 refutes it again from the other side.** The
path is not the discriminant. The rule sees the capitalised form *anywhere*, including inside a
path, and is blind to the lowercase form *anywhere*, including in running prose.

**Mechanism, confirmed by inspecting the sets rather than inferring:**

```
PRIVATE_IDENTIFIER_DIGESTS   size 5   sha256(Capitalised) ∈ set  →  True
CASEFOLD_IDENTIFIER_DIGESTS  size 3   sha256(lowercase)   ∈ set  →  False
                                      sha256(lowercase) ∈ PRIVATE_IDENTIFIER_DIGESTS → False
```

`independent_privacy_scan.py:239` **already computes the casefolded digest and already checks it**
against `CASEFOLD_IDENTIFIER_DIGESTS`. The folded pathway is built, correct, and live. The given
name's folded digest is simply **not enrolled in it**.

⇒ **The minimum patch is one digest, not one pattern.** A path-form pattern would land, would pass
its own fixture pair, and would still return no finding on fixture 3 — a repair that closes the
instance and leaves the class open, which is the pilot's own failure class B arriving inside the
repair for M3-10. **Plan recommends enrolling the folded digest and keeping Mirror's fixture pair,
extended to the five above.**

### 3.2 M3-14 · The rule was visible, in hand, and cited mid-run — the cap's *exit* was closed

Mirror's diagnosis: *"the gap is not a missing rule, it is that no actor's fingerprint set surfaced
the rule they were bound by,"* routed to `plan_defined_parameters.md` § P2.2 fingerprint
composition.

**Four measurements, and the diagnosis does not survive any of them:**

| # | Measured | Result |
|---|---|---|
| 1 | Is Annex C in the Scientist and Orchestrator pertinence sets? | **Already, both.** § P2.2: `scientist` → CORE + Annex C, E, F. `orchestrator` → CORE + Annex C, D, F, G, I, J. `governance_fingerprint.py inputs --role scientist` lists `annex_c_review_protocol.md` as input #4. |
| 2 | Does the Scientist's *own role contract* state the cap? | **Yes, in prose.** `roles/scientist.md`: *"at most one active review per scientist, at most two rounds before adjudication, and `AUTHOR_RESPONSE` is mandatory — silence is not acceptance."* |
| 3 | Did any artifact **in the run's own diff** cite the cap? | **Yes — three, in the Orchestrator packet**, introduced by `5debf86` at **08-25 17:03**, inside the pilot window. Two state *"max 2 rounds → adjudication"* verbatim; `TRIAL-001-REVIEW-FINDINGS-REGISTER.md` names **`Annex C.3`** explicitly. My sweep pattern: `max 2 round\|annex c\.3\|two rounds before adjudication\|round cap`, over `git diff --name-only <merge-base> <ref>` for each of the four pilot refs. Scientist refs: **0**. |
| 4 | Was adjudication reachable at all? | **No.** `lease_state.py` → five leases, all `STALE` or `RELEASED`, **`ACTIVE by derivation: 0`** — reproduced by me at the derivation instant. |

**And one seat declared the deviation, in a durable committed artifact.**
`REV-EVIDENCE-SCIB-001.md` frontmatter: `LEVEL: declared outside the Annex C.1 ladder`,
`ADJUDICATOR: unassigned — no ACTIVE ORCHESTRATOR_LEASE (lease_state.py → ACTIVE by derivation: 0)`,
with § 0 stating *"This review … claims no rung of the C.1 ladder."* It further cites
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`, which determines that all four role contracts remain
`status: PROPOSED` and are **not binding**.

⇒ **Mirror's proposed Action 6 is a no-op.** Adding Annex C to pertinence sets that already contain
it would land, would look like a repair, and would change no behaviour. It is the fifth member of
class B in this package.

⇒ **The finding that survives is narrower, and better:** Annex C.3's cap terminates in
`→ adjudication`, and adjudication requires an ACTIVE `ORCHESTRATOR_LEASE`, of which there are
**zero**. **A cap whose only exit is unreachable cannot bind.** The pilot did not overrun a visible
rule; it ran a rule with a closed exit, and exactly one of four seats wrote that down.

**Residual genuine defect, and it is the only one:** the deviation was declared **by one seat, in
one artifact**, and was never aggregated to the run. Nothing collects per-seat authority
declarations into a run-level statement. That is a plumbing repair, not a fingerprint repair.

### 3.3 M3-15 · The inventory arithmetic, corrected

Mirror's prose reads *"Plan has 12 records + 3 commit candidates still untracked"* (= 15); Mirror's
own failure-map row for M3-15 reads *"14 dirty entries."* Both cannot be right.

Measured, `git status --porcelain=v1` in this worktree at `e4aa80c`:

| Class | Count |
|---|---:|
| Untracked — `learning/plan/` records | 8 |
| Untracked — commit candidates | 3 |
| Untracked — `disease-models/wwox/analysis/` | 1 |
| **Untracked, total** | **12** |
| Tracked-modified | 2 |
| **Total dirty entries** | **14** |

The 3 commit candidates are **inside** the 12, not additional to them. Mirror's table row (14) is
correct; its prose (15) double-counts. No conclusion moves; the repair is unchanged in kind.

---

## 3.4 · ADDENDUM — a guard that scans raw bytes fires on the document that reports its findings

Measured after this record was first committed, and it belongs with M3-8/M3-9/M3-10 because it is
the same family: **a gate whose population includes the reports written about it.**

**Tracking a document is a change to the release surface.** Action 7 committed twelve records; its
acceptance criteria named a privacy scrub and said nothing about the release suites. Two went from
green to red on that commit, and a third on a later one — measured with a before/after control on
clean extractions of `43cf690~2` and `HEAD`:

| Guard | What it matched | Why the document said it |
|---|---|---|
| `public_release_gate.py` → `BROKEN_WIKILINK` | a wikilink token shown inside backticks **as an illustration** | the paragraph was explaining that a registry mention *carries no wikilink* |
| `test_documented_commands.py` | two `pathograph` script paths under `framework/scripts/` | the document's finding is that those scripts **do not exist on any ref** |
| `test_fresh_clone_reader_journey.py` | two `.md` paths | same shape — one names an untracked file, one is **this record** reporting that `scientist_evidence_standard.md` is absent from `main` |

⇒ **Three independent guards, one evening, all firing on a true report of an absence.** The guards
read raw bytes, so they cannot distinguish *documenting a path* from *reporting that a path is
missing*, and the act of recording a negative is what falsifies it.

**Repaired here at the text layer only, meaning preserved:** paths written as filename plus
directory rather than one slash-joined string, and the wikilink token described rather than shown.
**Verified with a positive control** — planting a fresh bad path and a fresh bad wikilink makes both
guards fire again, so the green is informative and nothing was disabled. The full runner now shows
**the same six failures as the pre-commit baseline, and no seventh**: the regression is closed and
those six are pre-existing and outside this work.

🔴 **The text repair is not a fix for the class, and must not be recorded as one.** As
`legend-public-cb` established by trying it: there is **no construction that displays the wikilink
syntax inside the scanned surface** — backticks, fences, line splits all match, because the
extractor sees bytes. So the repository currently **cannot document its own wikilink convention**.
The real repair is code-span stripping in the extractor, which changes what a `BLOCK`-severity gate
blocks on and therefore routes through **GATE 3** — Plan does not self-adjudicate that.

**Consequence for Action 3, and it is a genuine addition to the repair set.** Action 3 asks gates to
*print* their population. This asks something adjacent and cheaper to state: **a guard must not
count, as a violation, a document that is reporting the violation.** Both are the same defect seen
from two sides — a gate that does not know what its population is.

**Consequence for Action 7, stated as an acceptance criterion nobody had written down:** *tracking a
document changes the release surface, so the release suites belong in the acceptance criteria of any
commit that tracks one.* Raised by `evidence-index-cb`, which found the two red suites and declined
to repair another author's file unilaterally — correctly.

---

## 4 · OWNING-OBJECT MAP — every finding to an existing object

**No object is originated below.** Two of the objects Mirror names are not where its handoff
assumes they are, and § 7 re-orders the work accordingly.

| Finding | Existing owning object | Object's measured state | Originates anything? |
|---|---|---|:--:|
| M3-1, M3-2, M3-3, M3-11 | `scientist_evidence_standard.md`, in `framework/protocols/` | **Exists on `lettore` only** — absent from `main` and all other heads. `lettore` is 201 behind `main`. Self-declared *"Non-canonical, PROPOSED."* | no |
| M3-4 | Same standard, § 0 denominator discipline | as above | no |
| M3-5, M3-6, M3-12 | `learning/plan/PATHOGRAPH-TRANSPORT-CONSOLIDATION-001` | **Untracked** — on disk here, tracked on **0 of 44 heads**. `record_type: WORK_ANALYSIS`, already carries an `OBSERVATION_SCOPE` § 0. | no |
| M3-8 | `scripts/run_release_regressions.py` + the v2 tool-repair commit | Both on `main`, live | no |
| M3-9, part of M3-3 | `framework/scripts/deepdive_manifest.py` verdict strings (`:1466`, `:1470`, `:1479`) · `regenerate_adjudications.py:246,252` · `independent_privacy_scan.py` report block | All on `main`, live | no |
| M3-10 | `scripts/independent_privacy_scan.py`, rule `PRIVATE_NAME` (`:239`, `:247`) | On `main`, live. Branch `harden-release-scan-scoping` is **fully merged and 0 ahead** — a historical name, not a live workspace. | no |
| M3-14 | Annex C.3 (FROZEN) · `lease_state.py` · run-level authority aggregation | C.3 frozen and normative; `lease_state.py` is **untracked on every head I checked** — it runs from disk only | no |
| M3-15 | Plan branch `plan-orchsurf-r4-transcription` | This worktree | no |
| M3-7, M3-7a, M3-13 | none required — record only | — | no |

🔴 **Two consequences the dispatch's § 16 does not carry:**

1. **Action 5's owning object is untracked.** Routing M3-5/M3-6/M3-12 into
   `PATHOGRAPH-TRANSPORT-CONSOLIDATION-001` routes them into a file no other actor can open.
   **Action 7 therefore gates Action 5's routability**, not merely its tidiness.
2. **Action 1's named home carries no work.** `harden-release-scan-scoping` is 0 ahead of `main`.
   Landing the patch "on the existing branch" means opening a fresh commit on a merged branch —
   which is fine, but it is not the "already exists and is the natural home" that Mirror's sizing
   implies. The *rule* is the home; the branch is a label.

---

## 5 · CLASSIFICATION — local repair layer × governed change class

The dispatch asks for canonical governed vocabulary "where one exists". **It exists for the
change class and not for the repair layer**, and this table says which is which rather than
blurring them.

- **Repair layer** — Mirror's `KEEP / TEST / TOOL PATCH / CONTRACT PATCH / HUMAN GATE`. Mirror
  states these are *"the dispatch's local analytical categories."* They are **not governed
  vocabulary** and are used here for analysis only.
- **Change class** — governed. `GOVERNANCE_v3.1.1.md` § 250 defines `MAJOR` strictly: *"SOLO
  governance/authority/gate/epistemic policy; breaking a schema/registry canonici;
  distruttivo/irreversibile; qualsiasi spesa."* § 244 gives the MAJOR route (**GATE 3**):
  `Plan candidate → Mirror hostile review → MIRROR PASS → HUMAN_APPROVAL → commit`.
  § 250 also fixes the doubt rule: *"dubbio persistente → MAJOR (fail-closed)."*

| Action | Findings | Repair layer (local) | Governed change class | Route |
|---|---|---|---|---|
| **1** privacy rule | M3-10 | TOOL PATCH + **HUMAN GATE** | **MAJOR** — it is a gate and a privacy policy, § 250 first clause | GATE 3 |
| **2** wire `verify` into the release battery | M3-8 | TOOL PATCH | **MAJOR (fail-closed)** — it changes what the release gate blocks on. Plan does not self-adjudicate this; § 250 doubt rule sends it to Mirror. | GATE 3, unless Mirror classes it non-MAJOR |
| **3** gates print their population | M3-9, M3-8, M3-3 | TOOL PATCH | **not MAJOR** — output-only. It changes what a verdict *says*, never what it *blocks on*. This is the distinction that keeps Action 3 cheap. | ordinary |
| **4** measured ref in Scientist output | M3-1, M3-2, M3-3, M3-11 | CONTRACT PATCH | **not MAJOR** — the target is self-declared non-canonical and PROPOSED | ordinary |
| **5** supersession / closing-artifact check | M3-5, M3-6, M3-12 | TEST + plumbing | **not MAJOR** — Plan-owned work analysis | ordinary |
| **6** Annex C.3 | M3-14 | **HUMAN GATE** | **MAJOR** — amending a FROZEN annex is governance | GATE 3 + Operator |
| **7** Plan untracked state | M3-15 | plumbing | **not MAJOR** — Plan-owned work artifacts on Plan's own branch | ordinary |
| **KEEP** | 12 items | KEEP | no change | — |
| **RECORD ONLY** | M3-7, M3-7a, M3-13 | none | no change | — |

---

## 6 · MINIMUM PATCH SET

Seven actions. **None is implemented here except 7**, which the dispatch assigns to Plan and which
§ 4 shows is a precondition for Action 5.

### 6.1 · Action 1 — enrol the folded digest (M3-10) · **HUMAN GATE**

**Not** a path-form pattern. Per § 3.1: `independent_privacy_scan.py:239` already checks
`CASEFOLD_IDENTIFIER_DIGESTS`; the given name's folded digest is not in it.

- **Change:** one entry added to `CASEFOLD_IDENTIFIER_DIGESTS`.
- **Test:** the five fixtures of § 3.1 — capitalised standalone, lowercase standalone, capitalised
  in path, lowercase in path, and the `Operator` negative control. Mirror's pair is a subset;
  fixture 3 is the one that discriminates the two candidate repairs.
- **Do not** create a parallel privacy mechanism. Do not touch `public_release_gate.py`.
- **Affected tracked surfaces, enumerated without printing identifiers** — see § 11.1.
- **Blocked on the Operator.** Plan prepares; Plan does not land it.

### 6.2 · Action 2 — one line and one real recipe (M3-8)

- Add `framework/scripts/regenerate_adjudications.py verify` to the release regression path.
- Add **one** test that opens a real recipe, sufficient to make deletion, digest drift and source
  absence observable. The gate population is not hypothetical: **3 recipes · 27 crop artifacts ·
  47 adjudicated locators**, all tracked, all re-derivable statically (§ 2, M3-3).
- **Preserve** the 12 `FakePage` predicate tests. **Do not** rewrite `regenerate_adjudications.py`.
  **Do not** add a skip-if-missing path — `verify` failing when the PDF is absent is correct.
- **Known interaction with fail-closed behaviour, and it must be designed for, not discovered:**
  `verify` is a property of *which directory you stand in*. It exits 0 in the shared checkout and
  fails with *"source PDF absent"* in a worktree without `files/`. Wiring it naively into a suite
  that runs in every worktree converts a correct fail-closed into a permanent red. The wiring must
  declare the artifact workspace, exactly as `deepdive_manifest.py --artifact-workspace` already
  does. **This is the reason Action 2 is sized at one line and is not one line.**

### 6.3 · Action 3 — a green verdict exposes its population (M3-9, M3-8, M3-3)

The invariant is **semantic, not lexical**: *a green verdict must expose the population over which
it is green.* Wording need not match across tools.

| Gate | Add to the verdict | Preserve exactly |
|---|---|---|
| `deepdive_manifest.py` | `n` text locators verified · `n` skipped as outside `TEXT_SURFACES` | *"exact **text** locators verified where declared"* — accurate today; **do not widen it** |
| `regenerate_adjudications.py` | `n` recipes opened · `n` locator spans resolved | the rule-5e delegation clause, which caught a would-be Mirror false finding |
| `independent_privacy_scan.py` | `n` files scanned under the rule, out of `n` in the population | the fail-closed BLOCK severity |

**Action 3 is the cheapest item here and the one with the highest leverage**, because it is the
only repair that would have made M3-9, M3-8 and M3-3 visible on day one without a reviewer.

### 6.4 · Action 4 — bind a population to the snapshot it was measured at

**Strictly after Action 3.** Mirror's sequencing note is load-bearing and Plan endorses it
unchanged: a contract that demands a ref while gates still print unqualified `PASS` produces the
next wrong denominator *wearing a ref stamp*.

**Do not hardcode a field name before checking existing vocabulary — and it exists.**
`scientist_evidence_standard.md` § 0 already writes *"true of the tree at the stated commit"*. The
document reaches for the field and never delivers it. `measured_at_ref` is Mirror's conceptual
name; **`stated commit` is the document's own**. Plan proposes adopting the document's existing
phrase rather than importing a new token, and defers the final spelling to the object's owner.

The representation must distinguish four things:

1. **WHAT** population was measured;
2. **AT WHICH** ref/snapshot;
3. **WHERE** — which tree/worktree, since `files/` proves the same ref yields different surfaces;
4. **WHICH** tool or derivation produced the number, when load-bearing.

**And it must preserve the distinction § 0 of that document already draws** between figures that
decay on their own (claim and paper counts) and figures that are object-derived. The pilot shows
the second kind decays too — silently — the moment the tree is not named. `49 → 64` manifests and
`813 → 1,002` locators moved without any population changing.

**Do not** originate a parallel object. Fold into the existing standard. Note § 4: that standard is
on `lettore` only, which is itself an input to the routing at § 12.

### 6.5 · Action 5 — supersession before a closing artifact lands (M3-5, M3-6, M3-12)

Owner: `PATHOGRAPH-TRANSPORT-CONSOLIDATION-001`. **Do not originate a parallel transport spec.**

Minimum behaviour, deterministic wherever possible:

1. establish when the closing artifact's working base was opened, where representable;
2. enumerate peer artifacts and position revisions committed since that base;
3. record, per item, whether the closing artifact **incorporated · superseded · rejected · missed** it;
4. stamp a superseded summary rather than silently rewriting the historical statement;
5. bind the final handoff to **actual current tips**, not a mid-run snapshot.

The three findings give the measured target: **8 · 7 · 9** commits of drift in one handoff (M3-12),
one convergence row still carrying an outcome all three actors abandoned with **0 amendments in 16
files** (M3-5), and a falsifier refuted 16 minutes before the closing artifact landed (M3-6).

**Do not solve this by asking another reviewer to read everything again.** Eight of Mirror's
fourteen findings were invisible to any prose reader; this class is a merge-base check.

### 6.6 · Action 6 — separate the two questions (M3-14) · **HUMAN GATE**

Per § 3.2, **Question A as Mirror framed it is already satisfied** and its patch would be a no-op.
The Plan-side residue is small and real:

- **A′ (Plan work, not a fingerprint change):** nothing aggregates per-seat authority declarations
  into a run-level statement. One seat declared itself outside the C.1 ladder; three did not; no
  artifact collects the four. Fold this into Action 5's plumbing — it is the same act (bind the
  closing artifact to what the seats actually declared).
- **B (Human Gate):** § 11.2. Reframed, because the measurement reframes it.

### 6.7 · Action 7 — Plan's untracked state · **EXECUTED IN THIS PASS**

The dispatch assigns this to Plan and § 4 shows Action 5 depends on it. Performed:

| Step | Result |
|---|---|
| Inventory | 12 untracked (8 `learning/plan/` · 3 commit candidates · 1 `analysis/`) + 2 tracked-modified = **14 dirty**. § 3.3 |
| Validity at current refs | All 12 are Plan-owned work artifacts; the 3 commit candidates are the ones Mirror § 11.10 says **not** to re-review |
| **Identifier removal** | **11 occurrences across 5 files**, removed. 8 in absolute-path form (gate-blind, per § 3.1); 3 in prose, capitalised (gate-visible today). Paths → `<repo-root>`, one → `~/.config/git/ignore`; prose → **`the Operator`**, per standing policy that the human role is always `Operator` |
| Anchor safety | Checked before rewriting one heading: `git grep` across all 44 heads found only prose mentions in `CHK-plan-0016.json`, **no markdown anchor link**. Heading rewritten safely |
| **Verification** | Two independent checks. (i) `independent_privacy_scan.py` from `main` over the 12-file population → **0 findings, 0 blocking**. (ii) External case-insensitive sweep → **0 occurrences**, with a **positive control**: planting one occurrence returned 1, proving the sweep capable of non-zero |
| **Honest weight of (i)** | The scanner's clean verdict **does not corroborate**. It is blind to the exact form removed (§ 3.1), so it would have returned 0 either way. **Check (ii) with its positive control is the load-bearing measurement.** |
| Canonical state | **Untouched.** Committing a Plan work artifact does not make it canonical; none of the 12 enters a current file |

---

## 7 · DEPENDENCY ORDER — Mirror's, plus two edges measurement adds

**Preserved from Mirror, unchanged and load-bearing:** `Action 3 → Action 4`.

**Added by § 4, and absent from the dispatch's § 16:**

- `Action 7 → Action 5` — Action 5's owning object is untracked; routing into it is routing into
  nothing until it is committed.
- `Action 1 ⇢ Action 7` — 5 of the 12 files carried 11 identifier occurrences. Committing before
  the rule can see the form would have added them to a tracked surface the gate returns `PASS` on.
  **Discharged in this pass by scrubbing first (§ 6.7), so Action 7 no longer waits on Action 1.**
  The edge is recorded because it will recur on the next Plan commit if Action 1 has not landed.

```
Action 1 · privacy rule ──────────────► HUMAN GATE (§ 11.1) ──► GATE 3
   ⇣ (discharged by scrubbing)
Action 7 · Plan state ✔ DONE ─────────► Action 5 · supersession ──► closing-artifact tests

Action 2 · real-recipe wiring
        ↓
Action 3 · gates print their population        ← cheapest, highest leverage
        ↓
Action 4 · measured ref in Scientist output

Action 6 · A′ aggregation ──► folds into Action 5
Action 6 · B  cap fitness  ──► HUMAN GATE (§ 11.2)
```

**No later step implies authority for an earlier unresolved Human Gate.** Actions 2–5 and 7 do not
depend on either gate, and neither gate is discharged by any of them landing.

---

## 8 · NO-CHANGE LIST — binding for this task

Measurement falsified none of these. Changing any is architecture tourism.

1. No new actor. No new reviewing actor. **Eight of fourteen findings were invisible to any prose
   reader and closed by a command**; zero required a seat that does not exist.
2. No new control plane. No new graph schema. No new governance annex.
3. **No numerical stopping threshold.** Mirror found no evidence for one; § 3.2 shows the system's
   problem is a cap with a closed exit, which a second number makes worse.
4. No rewrite of `regenerate_adjudications.py`. The needle discipline is correct and well tested at
   the predicate level. The defect is that nothing points it at real recipes.
5. Rule 5e and recipe-not-image delegation stand.
6. The manifest exact-text gate stands — **changed only to expose its denominator** (Action 3). Its
   scope string *"exact **text** locators verified where declared"* is accurate and must not widen.
7. Fail-closed behaviour on absent evidence stands. No skip-if-missing path (see § 6.2).
8. `UN-ATTACKED` on R-3 and R-4 stands. Do not route them to a synthesiser for closure.
9. Actor boundaries stand. No expansion of Mirror's perimeter.
10. **No mandated self-confession section.** A mandated confession becomes a form to fill in. Record
    the practice as an `ACTIVE_LESSON` candidate; leave the incentive alone.
11. The Pathograph `UNTYPED` edge stays `UNTYPED`. M3-5 did not reach it.
12. PMID 32000863 exploratory science stays closed. No biological proposition reopened.
13. `POINTER-01`, `DRIFT-01`, `GRAPH-MATERIALIZATION-01` are **not** re-reviewed because v3 exists.
14. The stopping *formulation* is kept verbatim: *"I have run out of surfaces I currently believe
    are unexamined"* and *"joint settlement is where the next thing lives."* Descriptive practice,
    not a competing normative threshold. Add no number.
15. **E is not a fifth failure class.** Merged into B, per Mirror § 2.1 and its repair test.
16. **M3-7a must not enter a design argument.** "Seven additive rounds before the first collision"
    is refuted by the Phase II documents; it would support "the protocol suppresses contradiction"
    when the record shows the opposite.

---

## 9 · ARCHAEOLOGY → SCIENTIST CONTRACT

**This is a frequency map of observed practice, not a schema.** The dispatch asks that the contract
be *extracted from* Scientist practice rather than imposed. Plan proposes no schema and designs no
graph.

### 9.1 The three under-represented objects, mapped

Mapping is against `roles/scientist.md`, `scientist_evidence_standard.md`, Annexes A/B/C/E,
`epistemic_discipline.md` and the current graph representation. **Labels are local analytical
vocabulary for this document only.**

| Object | Practice frequency (Mirror § 9) | Existing hook | **Label** |
|---|---|---|---|
| **A · Position revision with attribution** | 15/29 docs · 81 occurrences | `AUTHOR_RESPONSE` in `roles/scientist.md` and Annex C.3 — *"mandatory; silence is not acceptance"*; `SUPERSEDED` in Annex E's lifecycle | **PARTIALLY REPRESENTED** — a *response* obligation and a *lifecycle state* exist; an attributed revision record (what changed · who caused it · which evidence) does not |
| **B · Observation scope / denominator** | 16/29 docs · 45 occurrences | 1 hit in `annex_a_task_contract.md`; 1 in `gold_is_in_the_details.md`; **0 in `roles/scientist.md`** | **PARTIALLY REPRESENTED** — the idea is present at the edges of the normative surface and absent from the Scientist's own contract. Direct cause of M3-1, M3-2, M3-3, M3-11 |
| **C · Epistemic tier on the *relation*** | 16/29 docs · 66 occurrences | Vocabulary **exists** — `DATO` · `INFERENZA` · `IPOTESI` · `PREMISE_TAG` in `epistemic_discipline.md` — and attaches to propositions/nodes. `claim_edge` carries no tier (measured by Scientist A, confirmed in Mirror v2 § E) | **MISSING BUT PATCHABLE** — the vocabulary is governed and the *carrier* is absent. No new vocabulary needed |

**None is `INCOMPATIBLE`.** Every one has an existing hook. That is the finding: practice has
out-run the contract, and the contract can absorb it without new machinery.

**Resolution caveat, stated rather than hidden.** These are keyword sweeps over short pointer files
(`roles/scientist.md` 122 lines; the annexes 54–106; `epistemic_discipline.md` 56). The normative
surface is thin **by design** — it routes rather than legislates. A keyword absence there is weak
evidence of a conceptual absence. **Labels are PROVISIONAL**; the commands are named so the next
reader can widen the pattern rather than inherit my number.

### 9.2 Behaviour to preserve, formalize, and not legislate

| **PRESERVE** (unlegislated, high-value) | **FORMALIZE** (where a gap is measured) | **DO NOT LEGISLATE** |
|---|---|---|
| explicit disagreement — present from Phase II, structurally required by the form | snapshot/ref of load-bearing measurements (Action 4) | volume of review |
| independent primary-evidence derivation | observation scope / denominator (Actions 3 + 4) | number of findings |
| self-revision when counter-evidence wins | transport of peer position revisions into final synthesis (Action 5) | mandatory confession / self-criticism |
| **attribution of position changes** — the pilot's most characteristic act | run-level aggregation of declared authority (§ 6.6 A′) | actor personality |
| refusal to force consensus; `DISAGREEMENT_UNRESOLVED` is a legitimate close (Annex C.3) | | permanent static Scientist specialization |
| `UN-ATTACKED` marking | | |
| deterministic measurement where argument cannot settle a question | | |

**Scientist A/B/C remain one Scientist profile with task modes.** This pilot demonstrates no
function requiring a separate actor. The two strongest explanations of the epistemic gain were
*seats standing on different surfaces* — an accident that should become a **declaration** — and *a
third deterministic instrument settling what argument could not*. Neither is "more reviewers."

### 9.3 What the graph program may take from this — and no more

Recorded as **empirical evidence for later scientific-object-model work**, not as a design:

real Scientist work already emits **claims · hypotheses · relations · evidence locators · causal
limits · disagreements · graph contributions · epistemic tiers · position revisions.**

The Pathograph finding stands and is important: *a relation may already be scientifically present in
prose, title or material while its graph edge is untyped or structurally absent.* **This task does
not authorize blind decomposition or graph typing.** Graph relations requiring primary-evidence
interpretation remain Scientist origination. Orchestrator integrates and routes; Mirror holds
epistemic and process integrity; neither replaces the other.

---

## 10 · PLUMBING → ORCHESTRATOR

Four items, all transport, none requiring a reading actor.

| # | Item | Evidence |
|---|---|---|
| P-1 | **A handoff must bind to actual current tips.** The Mirror handoff declared three tips that were **8 · 7 · 9** commits stale; a consumer resolving its blob digests gets a mid-run snapshot | M3-12, re-measured § 2 |
| P-2 | **A superseded summary needs a supersession stamp, not a silent rewrite.** One convergence row still reports an outcome all three actors abandoned; `convergence map` appears in **1 of 16** files in the run-diff — the file itself | M3-5, re-measured § 2 |
| P-3 | **A closing artifact needs a merge-base check against peer artifacts committed since its draft opened.** 16 minutes separated the refutation from the closing document | M3-6, inherited |
| P-4 | **Per-seat authority declarations need run-level aggregation.** One of four seats declared itself outside the C.1 ladder and named the absent adjudicator; nothing collects the four into a run-level statement | § 3.2, measured here |

All four fold into Action 5. **P-4 is the part of M3-14 that is Plan/Orchestrator work rather than
Human Gate**, and it replaces the fingerprint change that § 3.2 shows would be a no-op.

---

## 11 · HUMAN GATE PACKETS

### 11.1 · M3-10 — the release gate returns PASS on a tree carrying the Operator's given name

**No identifier is reproduced in this packet.**

**MEASURED, by me, at clean `main` (`788c357`), extracted to a scratch tree of 580 files with zero
untracked entries:**

```
python3 scripts/public_release_gate.py --root . --mode release --skip-clean-clone
VERDICT: PASS
BLOCKS: 0
```

**On a tree carrying the identifier in absolute-path form:**

| Ref | Tracked files | Matching lines | **Occurrences** |
|---|---:|---:|---:|
| **`main`** | **16** | **26** | **31** |
| `legend-operating-convention-v1` | 16 | 26 | 31 |
| `lettore-b` | 19 | 31 | 36 |
| `plan-orchsurf-r4-transcription` | 19 | 30 | 35 |
| `lettore-c` | 17 | 27 | 32 |
| `orchestrator` | 13 | 24 | 29 |
| `lettore` | 4 | 9 | 9 |

**Denominator correction, and it is the class recurring inside its own report.** Mirror's
"occurrences" column is a **line** count. My file counts reproduce Mirror's **exactly** on all seven
refs. The occurrence counts run **+5** on every ref except `lettore`, where lines and occurrences
coincide at 9 — which is why the discrepancy was invisible. Exact measurement transformation, so the
next reader can reproduce or widen it: `git grep -l / -c / -o -F -- "/Users/<given-name>/" <ref>`.

**Five of `main`'s 16 files are shipped public-edition surfaces** — the discovery ledger, the
full-text queue, the read-receipts ledger, the sync-epochs ledger, and the kernel spec (which alone
carries 4 occurrences on one line-set).

**Standing policy already fixes the direction.** LEGEND must be scalable and reusable and must not
propagate personal identifying information into public/governance/runtime artifacts absent separate
authorization. The human role is always **`Operator`**, never a personal name. **The Operator is not
being asked whether the direction is right.**

**What the Operator is being asked, and it is bounded:**

| # | Decision |
|---|---|
| **D-1** | Authorize the rule change: enrol the folded digest so the lowercase form is detected **wherever it occurs** (§ 3.1 — not merely in paths). Route: **MAJOR → GATE 3** (`Plan candidate → Mirror hostile review → MIRROR PASS → HUMAN_APPROVAL → commit`). |
| **D-2** | Decide the disposition of the **16 existing tracked files on `main`**: remediate before the rule lands, remediate after and accept a red gate in between, or allow-list any occurrence found to be intended. Mirror recorded *"whether any occurrence is intended"* as its residual uncertainty on M3-10, and Plan did not resolve it — resolving it requires reading each site, which is the Operator's call, not a measurement. |
| **D-3** | Confirm the replacement convention. `main` already uses **`repository root`** (21 occurrences) as the neutral form; Plan used `<repo-root>` and `the Operator` in Action 7 (§ 6.7). One convention, or two, is the Operator's to fix. |

**Context that argues the repair belongs in the rule, not in a reviewer:** the Orchestrator's own
commit `5debf86` (*"seven identifiers leave with them"*) shows the seat already handles this class
**when it can see it**. The pilot neither introduced the class nor detected it.

**Plan asserts no authority here and lands nothing.**

### 11.2 · M3-14 — the round cap, reframed by measurement

**Do not answer this by building another stopping rule.**

**The premise has changed since Mirror wrote it — see § 3.2.** The cap was **not** invisible:

- Annex C is **already** in the Scientist *and* Orchestrator fingerprint pertinence sets (§ P2.2);
- `roles/scientist.md` **already** states *"at most two rounds before adjudication"*;
- **three artifacts in the run's own diff cite it**, introduced at 08-25 **17:03**, mid-pilot;
- `lease_state.py` → **`ACTIVE by derivation: 0`** — no ACTIVE `ORCHESTRATOR_LEASE` exists;
- `REV-EVIDENCE-SCIB-001` **declared itself outside the C.1 ladder** and named the absent
  adjudicator, citing `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (all four role contracts remain
  `PROPOSED` and not binding).

**So the question is not "did the actors miss a rule."** It is: **Annex C.3's cap terminates in
`→ adjudication`, and adjudication is unreachable with zero ACTIVE leases.** A cap whose only exit
is closed cannot bind, and one seat of four wrote that down.

**Bounded options, as the dispatch requires — and the recommendation is deliberately not a number:**

| Option | What it means | Plan's note |
|---|---|---|
| **1 · Retain the cap and require adjudication after two rounds** | The frozen text stands unchanged | **Incomplete on its own.** With `ACTIVE by derivation: 0` this makes every review terminate in an unreachable state. It needs to be paired with an adjudication route that exists |
| **2 · Permit a formally recorded deviation for this class of pilot/review** | The cap stands; a declared, durable deviation rationale is a lawful close | **Closest to what already happened.** One seat produced exactly this artifact unprompted. The gap is aggregation (§ 10, P-4), which is Plan work and needs no governance change |
| **3 · Amend the frozen rule** | Change C.3 through the existing governance mechanism | **MAJOR → GATE 3 + Operator.** Plan records **no evidence supporting any specific replacement number**, consistent with Mirror's refusal to propose one |

**A prior question the Operator may wish to settle first**, because all three options inherit it:
**was the PMID 32000863 pilot an Annex C review at all?** C.3 governs review *"opened only through
Orchestrator"* with `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`. There was no Orchestrator lease, and the
Orchestrator's own mid-run register recorded that C.3's required actor set is *"currently empty."*
If the pilot was never a C.3 review, the cap never bound it and the finding is about the **absence
of an applicable protocol** for operator-directed multi-seat work — a different and larger question
than the cap. **Plan does not decide this and flags it as the hinge.**

**Preserved regardless of the option chosen, as descriptive practice and not a competing threshold:**
*"I have run out of surfaces I currently believe are unexamined"* and *"joint settlement is where the
next thing lives."*

---

## 12 · DOWNSTREAM ROUTING

**The package does not go back to Scientist A/B/C.** Mirror concluded, and Plan confirms
independently, that no repair here requires primary scientific interpretation. Exploratory science
on this object stays closed.

| # | Object | Owner | Depends on | Authority | Exact reason this actor |
|---|---|---|---|---|---|
| R-1 | Privacy rule digest + 5 fixtures | **Operator**, then implementer | — | **HUMAN GATE → GATE 3** | Privacy property of a public repository. No producer seat is authorised; Mirror declined; Plan declines |
| R-2 | Wire `verify` + one real-recipe test, with a declared artifact workspace | tool implementer | — | GATE 3 unless Mirror classes non-MAJOR (§ 5) | Mechanical; § 6.2's workspace interaction is a design decision the implementer must make, not discover |
| R-3 | Three gate verdicts print their population | tool implementer | — | ordinary | Output-only; blocks on nothing new |
| R-4 | `stated commit` field in the evidence standard | owner of `scientist_evidence_standard.md` | **R-3** | ordinary | The object is on `lettore` only and self-declared PROPOSED. **Its owner is the Scientist seat that authored it** — this is the one place a Scientist is required, and it is contract work on its own document, **not** new primary-evidence work |
| R-5 | Supersession / closing-artifact check + run-level authority aggregation (§ 10 P-1…P-4) | **Plan**, into `PATHOGRAPH-TRANSPORT-CONSOLIDATION-001` | **Action 7 ✔ discharged** | ordinary | Transport class already owned by an existing open Plan object |
| R-6 | Annex C.3 fitness, and the prior question at § 11.2 | **Operator** | — | **HUMAN GATE → GATE 3 + Operator** | Amending a FROZEN annex is governance |
| R-7 | This consolidation, and the patches once landed | **Mirror** | R-1…R-5 | Annex C.2 / Annex G | **Mirror tests the patches; it does not re-debate the design.** § 3.1, § 3.2 and § 3.3 refine three of Mirror's own findings and must be attacked, not accepted |

**R-4 is the only Scientist dispatch, and it is deliberately narrow.** It is not another opinion on
the pilot; it is the author of a PROPOSED contract adding a field its own § 0 already promises.

---

## 13 · HANDOFF v2.1

```
HANDOFF · PLAN → OPERATOR (R-1, R-6) · → IMPLEMENTERS (R-2, R-3) · → SCIENTIST-A (R-4)
          · → PLAN (R-5) · cc ORCHESTRATOR · then → MIRROR (R-7)

RECORD_ID          PLAN-MIRROR-V3-MINIMUM-REPAIR-CONSOLIDATION-001
OBJECT             SCIENTIST_PILOT_PROCESS_HOSTILE_REVIEW_MIRROR_v3 @ mirror 77be2f4,
                   consolidated into a minimum repair set
MODE               CONSOLIDATION / MINIMUM-DELTA REPAIR PREPARATION
RELATION           COMPLEMENTS MIRROR v3 and PATHOGRAPH-TRANSPORT-CONSOLIDATION-001;
                   supersedes neither
OBSERVATION_SCOPE  2026-08-25T20:12:08Z · plan e4aa80c (2 behind main) · main 788c357 ·
                   mirror 77be2f4 · lettore 605fc5d (201 behind) · lettore-b 9a09590 ·
                   lettore-c 5b1d6c2 · orchestrator-packet a58af46 ·
                   44 heads + 6 remotes swept, positive control 44/44 ·
                   LINT PASS · receipts OK 128 chained · growth anchors PASS

1 · WHAT PLAN RE-MEASURED AND CONFIRMED
  M3-3 gate population re-derived independently and statically: 3 recipes · 27 crop artifacts ·
  47 adjudicated locators (10+29+8) — exact to Mirror, without the gitignored corpus.
  M3-8 confirmed: only the TEST is in the release suite; zero executable gates invoke verify.
  M3-9 mechanism confirmed: figure and abstract excluded from text verification by construction.
  M3-10 confirmed: public_release_gate.py → PASS, BLOCKS 0 at clean main.
  M3-12 confirmed exactly: 8 · 7 · 9 commits of tip drift; lettore-b current.
  M3-5 confirmed: the row still reads ASSOCIATED; 1 of 16 files mentions it; 0 amendments.
  M3-2 confirmed and sharpened: § 0 promises "the stated commit" and states none.
  Every supplied historical ref is unchanged at the current measured ref.

2 · WHAT PLAN REFINED OR PARTLY FALSIFIED
  M3-10  The discriminant is CASE, not PATH. Capitalised-inside-a-path BLOCKS; lowercase-standalone
         does not. The folded-digest pathway already exists at :239 and the name is not enrolled.
         Minimum patch = one digest, not one pattern. Mirror's proposed pattern would leave the
         standalone lowercase form uncaught.
  M3-10  Mirror's "26 occurrences" at main is a LINE count. Files reproduce exactly (16); true
         occurrences are 31. +5 on every ref except lettore, where lines == occurrences == 9.
  M3-14  PARTLY FALSIFIED. Annex C is already in both pertinence sets; roles/scientist.md already
         states the cap; three Orchestrator artifacts cite it mid-run at 17:03; and
         REV-EVIDENCE-SCIB-001 declared itself outside the C.1 ladder. lease_state.py →
         ACTIVE by derivation: 0. Mirror's Action 6 would be a NO-OP. The surviving finding:
         a cap terminating in "→ adjudication" cannot bind when adjudication is unreachable.
  M3-15  12 untracked (3 CCs INSIDE the 12) + 2 modified = 14 dirty. Mirror's prose said 15;
         Mirror's own table said 14. The table is right.

3 · WHAT PLAN ADDS TO THE DEPENDENCY GRAPH
  Action 7 → Action 5.  Action 5's owning object, PATHOGRAPH-TRANSPORT-CONSOLIDATION-001, is
  untracked on all 44 heads. Routing findings into it routed them into nothing.
  Action 1 ⇢ Action 7.  5 of 12 untracked Plan files carried 11 identifier occurrences.
  DISCHARGED in this pass by scrubbing first; recorded because it recurs on the next Plan commit.
  Mirror's Action 3 → Action 4 preserved unchanged and endorsed.

4 · WHAT PLAN EXECUTED
  Action 7 only. 11 identifier occurrences removed from 5 Plan-owned untracked records
  (8 path-form, gate-blind; 3 prose, capitalised and gate-visible). Verified twice, the
  load-bearing check being an external sweep with a positive control — because the scanner's
  own clean verdict is blind to the form removed and does not corroborate.
  No canonical file opened for writing. No other actor's branch touched. Nothing made canonical.

5 · REQUIRES HUMAN GATE
  M3-10  D-1 authorize the rule change · D-2 disposition of 16 existing tracked files on main ·
         D-3 confirm the replacement convention.
  M3-14  Options 1/2/3 on cap fitness, plus the prior question Plan flags as the hinge:
         was this pilot an Annex C review at all? No numerical threshold recommended;
         no evidence supports one.

6 · WHAT MUST NOT CHANGE
  Sixteen items at § 8. No new actor, control plane, graph schema, annex or threshold. No rewrite
  of regenerate_adjudications.py. Rule 5e, the manifest text gate, fail-closed behaviour, the
  UN-ATTACKED marking, actor boundaries, the UNTYPED edge, and the unlegislated self-defect-filing
  practice all stand. E stays merged into B. M3-7a must not enter a design argument.

7 · SCIENTIFIC vs OPERATIONAL
  SCIENTIFIC: none. No biological proposition adjudicated, no edge typed, no current file opened
  for writing, no commit candidate re-reviewed. PMID 32000863 stays closed.
  OPERATIONAL: all 15 findings owned; 0 new objects originated.

PLAN ASSERTS NO SCIENTIFIC VERDICT AND CLAIMS NO AUTHORITY. No lease acquired. No role contract
relied upon — all four remain PROPOSED per DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE. Two Human
Gates prepared and neither pre-empted. The system is ready for Mirror to test the patches rather
than debate the design — and § 2 of this handoff is what Mirror should attack first.
```
