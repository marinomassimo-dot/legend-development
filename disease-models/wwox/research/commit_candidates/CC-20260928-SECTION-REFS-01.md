# COMMIT CANDIDATE — CC-20260928-SECTION-REFS-01

**Candidate ID:** CC-20260928-SECTION-REFS-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Base head:** branch `task/section-refs` at land time. The five `old` strings were re-measured
unique after `main` @ `4632dbe` was merged in (`a794560`), so the ops apply to `main` as it stands.
**Author:** ACTOR_ID `scientist`, package `section-refs`, dispatched by the Orchestrator under the
operator's standing authorisation of 2026-09-28.
**Source of the task:** `scripts/test_section_references.py`, shipped by Harness Engineering on
2026-09-28 (`4249755`). It resolves every `` `<file>` §<label> `` citation against the sections the
cited file actually defines, **gates** the normative surface and **censuses** the rest. Its
repository-wide census reported **68 unresolvable of 1155 checked**. All 68 were classified before
any repair; **63 sit outside the four scientific current files and were repaired directly on this
branch** (commit `ba5cd32`). **This candidate carries the five that touch a canonical registry and
can therefore only change through `BATCH_COMMIT`.**

**Declared change class: `MINOR`, every op.** No claim, paper, corpus or working-model record is
added or removed; no `Status`, `Classification`, `Type`, `Transferability`, `clinical relevance`,
`Claim links`, `Evidence depth` or `BLOCCO 1` value moves; no score moves; no scientific assertion
is added, withdrawn, widened or narrowed. **Each op replaces a cross-reference address with the
address that resolves, and nothing else.** 🔵 **Checked explicitly, because the change class would
be wrong if it were not true:** for all five, the target section the citation *meant* says what the
citing sentence claims it says, so no claim's content changes with its pointer. The verification is
recorded per op in §1. One op sits in the `working_model_current.md` `## Changelog` — a historical
record of a completed act — and is exactly the *"identifier / wrong reference"* correction
[`prompt_batch_commit.md`](../../../../framework/protocols/prompt_batch_commit.md) §7.2 permits in
place, with all three of its conditions met (correcting candidate, date, and the replaced wording
verbatim inside the row). **No row's stated conclusion is touched.**

**`context_policy`: `QUESTION_DRIVEN`** — declared. Held before any registry was opened: the census
output, `CLAIM 030`, `CORPUS P385`, `PAPER 099`, `PAPER 101`, the `working_model_current.md`
`WM_v5.1` changelog row, and the five *cited* files
(`fulltext_dossiers/PMID20146584.md`, `fulltext_dossiers/PMID16941225.md`,
`commit_candidates/CC-20260921-CLAIM033-REPLICATION-01.md`,
`commit_candidates/CC-20260914-15266310-01.md`, `analysis/therapy_levers.md`). Questions fixed
**before** the files were opened: *(1) for each citation, what does the cited file actually define at
or around that label; (2) does the content the citing sentence attributes to it exist there under a
different address, or not at all; (3) if it exists, is the citing sentence still true of it — i.e. is
this a typo or a claim resting on nothing.* The two large registries were reached with
`registry_records.py` and by line address, **never read whole**.

**Target WM version:** `WM_v7.4` (MINOR). **Batch gate:** intentionally untouched.

---

## 1 · CURRENT_TARGET and the classification of each of the five

Each `old` string below was measured in its target file: **all five occur exactly once.**

| # | record | citation as it stands | class | what the cited file actually defines | does the citing sentence survive? |
|---|---|---|---|---|---|
| `C30-1` | `CLAIM 030` (`claim_registry_current.md:577`) | CC-20260921-CLAIM033-REPLICATION-01 §5c | **(d)** lettered list item cited as a subsection | that candidate defines §1–§9 and §12. Its `## 5 · What is proposed` is a lettered list `(a0) (a) (b) (c) (d) (e)`; **(c)** is *"`CLAIM 030` — record the both-tails finding"* | 🟢 **yes.** §5 (c) is the op that put the two-tails observation into `CLAIM 030`. The record's own `Corretto 2026-09-28` adjudication of that observation is untouched by this op |
| `P385-1` | `CORPUS P385` (`paper_registry_current.md:5848`) | fulltext_dossiers/PMID20146584.md § 3.2 | **(c)** a subsection that never existed | that dossier defines §0–§11 with no §3.x. **§3** is *"🔴 A directional conflict between the two documents read this wave"* — the two-row table *reduced* (2010) vs *increased* (2014) | 🟢 **yes.** §3 as a whole **is** the registered UV directional conflict the `Role` field points at; there was never a narrower sub-address to mean |
| `P099-1` | `PAPER 099` (`paper_registry_current.md:7336`) | CC-20260914-15266310-01 §3a | **(d)** lettered list item cited as a subsection | that candidate defines §1–§8. Its `## 3 · What the reading adds that canon does not carry at all` is a lettered list `(a) (b) (c)`; **(a)** is *"It resolves a unit ambiguity canon has recorded as unresolvable"*, tagged **INFERENZA** by the candidate itself | 🟢 **yes**, including the `INFERENZA, non DATO` qualifier the registry line carries — §3 (a) states exactly that tag |
| `P101-1` | `PAPER 101` (`paper_registry_current.md:7382`) | PMID16941225.md §4.1 | **(d)** numbered list item cited as a subsection | that dossier defines §1–§9 and `T2`, no §4.x. Its `## 4 · What the paper does NOT support` is a numbered list of 11 negatives, each with its premise and revival trigger; **negative 1** is *"Antibody specificity is not established here … `PREMISE: INFERENZA` — the delegated control is adequate"* | 🟢 **yes.** The *"premise completion"* this assessment note defers is precisely that premise tag. Ten further citations of the same address, in eight non-canonical files, were repaired the same way on this branch |
| `WM-1` | `## Changelog`, `WM_v5.1` row (`working_model_current.md:266`) | therapy_levers.md §B2 | **(d)** a file that defines **no sections at all** | `analysis/therapy_levers.md` has only prose headings (`## A —`, `## B —`, `## C —`); its levers are list items, so `B2` is the record `- **B2. Neuroinflammation control.**` under `## B` | 🟢 **yes.** `BATCH_20260926_ALDAZ` did align that lever; only its address was unwritable as a `§`. **The row's stated conclusion is not touched** |

🔴 **Nothing in this candidate is a class-(a) line-number citation.** All fourteen of those were
outside the registries and are repaired on this branch; they are listed in the branch's commit
message and each carries its replaced wording inline.

🔵 **One finding worth naming although it is not in this candidate.** The census's single
normative-file target was epistemic_discipline.md §2.2, cited from
`analysis/metabolic_differential_vulnerability_reposed_20260922.md:621` to license a
`REVIVAL_TRIGGER`. That file defines §1–§5 and no §2.2 — **but the rule is real**: it is obligation
**2** of the *"Three binding obligations"* under §2, *"`REVIVAL_TRIGGER` — nothing dies in silence.
Every rejection is recorded with what evidence would reopen it."* **The analysis record's argument
survives the correct reference unchanged** — the node's five revival triggers are licensed exactly
as written, and no claim rested on a rule that does not exist. The same §2-as-§2.x mis-numbering
appears independently in `learning/plan/SCIENTIST-FIRST-REAL-PAPER-PILOT-001.md:451` (§2.3 =
obligation 3, the re-audit rule), which is why the hand-off to Harness Engineering proposes that
`epistemic_discipline.md` label its three obligations.

---

## 2 · PROPOSED_DELTA — exact operation list

**Five `replace-within` ops over three files, all record-scoped.** Every `old` is verbatim from the
current text at `b24779b` and occurs **exactly once in its file** (measured, not assumed).

### 2.1 `disease-models/wwox/registries/claim_registry_current.md` — `batch_commit.py propagate` (record-scoped)

#### `C30-1` — `CLAIM 030` · `replace-within` · change class `MINOR`

**old (verbatim, 1 occurrence):**

```text
(wave-2 `provenance`, 2026-09-27; `CC-20260921-CLAIM033-REPLICATION-01` §5c)
```

**new:**

```text
(wave-2 `provenance`, 2026-09-27; `CC-20260921-CLAIM033-REPLICATION-01` §5 (c) [ref corrected 2026-09-28 from “§5c” · CC-20260928-SECTION-REFS-01])
```

### 2.2 `disease-models/wwox/registries/paper_registry_current.md` — `batch_commit.py propagate` (records `CORPUS P385`, `PAPER 099`, `PAPER 101` only)

#### `P385-1` — `CORPUS P385` · `replace-within` · change class `MINOR`

**old (verbatim, 1 occurrence):**

```text
conflitto direzionale UV registrato in `fulltext_dossiers/PMID20146584.md` § 3.2.**
```

**new:**

```text
conflitto direzionale UV registrato in `fulltext_dossiers/PMID20146584.md` § 3 [ref corrected 2026-09-28 from “§ 3.2” · CC-20260928-SECTION-REFS-01].**
```

#### `P099-1` — `PAPER 099` · `replace-within` · change class `MINOR`

**old (verbatim, 1 occurrence):**

```text
(`CC-20260914-15266310-01` §3a, INFERENZA, non DATO)
```

**new:**

```text
(`CC-20260914-15266310-01` §3 (a) [ref corrected 2026-09-28 from “§3a” · CC-20260928-SECTION-REFS-01], INFERENZA, non DATO)
```

#### `P101-1` — `PAPER 101` · `replace-within` · change class `MINOR`

**old (verbatim, 1 occurrence):**

```text
and the `PMID16941225.md` §4.1 premise completion
```

**new:**

```text
and the `PMID16941225.md` §4 item 1 [ref corrected 2026-09-28 from “§4.1” · CC-20260928-SECTION-REFS-01] premise completion
```

### 2.3 `disease-models/wwox/registries/working_model_current.md` — `batch_commit.py propagate` (record-scoped, `## Changelog`)

#### `WM-1` — `## Changelog`, the `WM_v5.1` / `BATCH_20260926_ALDAZ` row · `replace-within` · change class `MINOR`

Governed by `prompt_batch_commit.md` §7.2: a wrong reference inside the *description of a past act*
may be corrected in place, and the replaced wording travels in the row. The row's `frozen`/`released`
dates, its version label and its batch id do not move, and its stated conclusion is not touched.

**old (verbatim, 1 occurrence):**

```text
`RL-NEUROINF-001`, `therapy_levers.md` §B2 and the `meta_gaba_paradox_current.md` line
```

**new:**

```text
`RL-NEUROINF-001`, `therapy_levers.md` lever B2 [ref corrected 2026-09-28 from “§B2” · CC-20260928-SECTION-REFS-01] and the `meta_gaba_paradox_current.md` line
```

---

## 3 · Post-propagation expectation, stated so it can be checked

After these five ops land, the repository-wide census (`scripts/test_section_references.py`
with `--census`) should report
**12 unresolvable**, down from 68 at `4249755` and from 17 on this branch. The residue is, exhaustively:

| residue | n | why it stays |
|---|---:|---|
| another actor's record — `reviews/mirror` (4), `reviews/orchestrator` (1), `mirror_consultations` (2), the two persisted mirror reviews (2) | **9** | not the Scientist's to rewrite. Each carries an appended dated `SECTION-REFERENCE CORRECTION NOTE` naming the wrong reference and the right one. One of the nine (`REV-AUTHOR-RESPONSE-ORCH-STATE-RECONSTRUCTION-001.md:465`) is **not a defect at all**: it is Mirror's own `AR-5`, quoting the bad reference in order to correct it |
| the checker's label grammar truncating `4bis` / `10bis` / `4ter` | **3** | `learning/scientist/SCIENTIST_OPERATING_PRACTICE_v1.md:152, 198, 236` are **correct** citations. `scripts/` is Harness Engineering's surface; recorded in that file and handed off |

---

## 4 · What this candidate deliberately does NOT propose

- **No re-lettering, re-numbering or promotion-to-heading of any cited target.** Nine of the 68
  citations failed because the target's records are list items — which
  [`wikilink_schema.md`](../../../../framework/protocols/wikilink_schema.md) §1.2.1 rule 2 says is
  legitimate and must be addressed by a block ID, never by rewriting the record as a heading. The
  repair belongs on the citing side, and that is where it was made.
- **No edit to `scripts/test_section_references.py`** or to anything under `framework/`.
- **No widening of the gate.** The measurement that would justify one, and the recommendation it
  supports, are in this package's report as a hand-off to Harness Engineering, not here.
- **No claim, premise tag or revival trigger is changed anywhere**, including the two records whose
  argument was re-checked against the corrected reference (`epistemic_discipline.md` §2 obligation 2
  and obligation 3). Both survived; had either not, it would be a separate candidate with its own
  change class.

---

## 5 · Applied outside this candidate by the same package (non-canonical, 2026-09-28)

63 of the 68, on branch `task/section-refs`, commit `ba5cd32`: 13 in `disease-models/wwox/analysis/`,
17 in `research/commit_candidates/`, 12 elsewhere under `research/`, 8 in `learning/`, 1 in
`governance/candidates/`, 9 recorded as appended correction notes in other actors' records, and 3
left untouched because they are correct. Every in-place repair carries the wording it replaces,
verbatim, in its own line.

---

## 6 · Review required

- **Producer ≠ verifier.** The scientific content of the five records is unchanged, so no Mirror
  hostile review is *required* by a guarantee; the one judgement worth a second reader is §1's
  right-hand column — *does the citing sentence survive the corrected address* — which is the only
  place this candidate could hide a content change behind a pointer change.
- **The `WM-1` op is the one to read twice**: it is the only op inside a historical changelog row.

---

## 7 · One harness defect found by landing this candidate — handed off, not fixed here

🔴 **`scripts/test_section_references.py` does not expose `--census` in its `--help`.** It has no
`argparse`; `--census` is read straight off `sys.argv` (line 308) while `--help` falls through to
`unittest`'s own parser, which lists `-v`, `-q`, `--locals`, `--durations`, `-f`, `-c`, `-b`, `-k`
and nothing else. Consequence, measured here: `scripts/test_documented_commands.py`
(`test_documented_cli_flags_exist`) goes **red** on any markdown that documents the flag in the
guarded `python3 <path> --flag` form — which this candidate's §3 did on its first draft, and which
made four cases of `scripts/test_repository_surface_determinism.py` fail, since that suite runs the
documented-commands guard on a disposable worktree. The eleven documents already carrying
`scripts/test_section_references.py --census` escape only because they omit the `python3` prefix the
matcher keys on, so **the repository currently cannot document its newest tool's only flag in the
form its own convention prefers.** Repaired on this side by using the unprefixed form. The tool is
Harness Engineering's surface, so the fix — give the script an `argparse` front that declares
`--census`, or teach the guard the flag — is proposed, not applied.

---

## BATCH DISPOSITION — `BATCH_20260928_004` (2026-09-28, ACTOR_ID `scientist`), append-only

**Nothing above this line was rewritten.**

**Status: `PROPAGATED`**
**Verdict:** PROPAGATED

`BATCH_20260928_004`: MINOR, MANUAL, `WM_v7.3` → **`WM_v7.4`**, under the operator's standing authorisation of 2026-09-28, given in writing, verbatim:
***«procedi, ti autorizzo a migliorare tutto quello che trovi… l'autorizzazione supera anche cose
fatte da me in passato»***.
Base `main` `a923e10`, branch `task/batch-20260928-004`. **Four of five ops applied; the fifth is
DROPPED because it is NOT A DEFECT.**

🔴 **`WM-1` — the `therapy_levers.md` §B2 citation in the `WM_v5.1` changelog row — DROPPED, NOT
DEFERRED.** The batch actor re-ran `python3 scripts/test_section_references.py --census` first-hand
rather than propagating § 2's list. That citation **no longer appears in the census at all**: it
resolves, because `analysis/therapy_levers.md` defines its levers as list-item bold definitions and the
checker learned to see them. ⇒ **`registries/` was `4` red, not five**, and an op against a resolving
citation would have edited a historical changelog row for nothing. This also means § 3's post-landing
expectation of **12 unresolvable** was already satisfied *before* this batch: the census read **12**
at pre-flight, not 17.

**APPLIED, and the four are exactly the rows the census printed:**

| op | record | file | verdict |
|---|---|---|---|
| `C30-1` | `CLAIM 030` | claim registry | ✅ PROPAGATED |
| `P385-1` | `CORPUS P385` | paper registry | ✅ PROPAGATED |
| `P099-1` | `PAPER 099` | paper registry | ✅ PROPAGATED |
| `P101-1` | `PAPER 101` | paper registry | ✅ PROPAGATED |
| `WM-1` | `## Changelog`, `WM_v5.1` row | working model | ⚪ DROPPED — the citation resolves; not a defect |

All four `old` strings re-measured **unique in their file, hence in their record** (count 1 each).
Each `new` carries the address it replaces, verbatim, inside the record.

🟢 **§ 1's right-hand column — the one judgement § 6 asks a second reader for — was re-checked
independently for all four, and all four survive.** The pointer change carries no content change:
`CC-20260921-CLAIM033-REPLICATION-01` § 5 is a lettered list whose **(c)** is the `CLAIM 030` both-tails
op; `PMID20146584.md` § 3 **is** the registered UV directional conflict, with no narrower sub-address
ever available; `CC-20260914-15266310-01` § 3 **(a)** carries the `INFERENZA, non DATO` tag the registry
line declares; `PMID16941225.md` § 4 negative **1** is precisely the `PREMISE: INFERENZA` the deferred
premise completion names.

**MERGED COLLISIONS, declared because two of them are genuine.** `paper_registry_current.md` was
**full-rewritten once** with this candidate's three ops **plus** `CC-20260826-PMID36828035-01` `B1`, as
one op list. And `CLAIM 030` is touched by **two** candidates — this one's `C30-1` and
`CC-20260928-A1-RESIDUE-01`'s `C30-1` — **on the same line 577**, on **non-overlapping bytes**, so
**neither wording was overridden**: this candidate owns the section-reference bytes, the other owns the
stray-bracket byte. ⚠️ Checked deliberately, because the two interact through a bracket count: this
op's `new` adds one `(` and one `)` (`§5 (c)`), the other removes one unopened `)`, and the block
balances at **53 / 53** afterwards — verified, not assumed.

**RESIDUAL, measured after landing:** `disease-models/wwox/registries` = **0** unresolvable of 32
checked. Repository-wide **12 → 8**, all eight outside the registries — `reviews/mirror` 4,
`research/session_evaluations` 3, `reviews/orchestrator` 1 — and none of them the Scientist's to
rewrite. The gated normative surface stays at 0.

§ 7's harness defect (`--census` invisible to `--help`) is **not** fixed here; it remains Harness
Engineering's. **No claim, premise tag, revival trigger, score or datum changed anywhere.** No receipt
written or recorded (ledger 262 chained).

**Mirror ex-post review due** under §21e. **Not medical advice.**
