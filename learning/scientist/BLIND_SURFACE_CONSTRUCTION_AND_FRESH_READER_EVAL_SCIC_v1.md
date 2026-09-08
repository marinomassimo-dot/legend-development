---
artifact: LEGEND scientific evaluation — BLIND SURFACE CONSTRUCTION, FRESH-READER EVALUATION
id: BLIND_SURFACE_CONSTRUCTION_AND_FRESH_READER_EVAL_SCIC_v1
class: evaluator-side record for a controlled benchmark in the vocabulary of
  `framework/protocols/controlled_benchmark_ab.md` §2.1–§2.3. It specifies and builds an input
  surface. It is NOT a benchmark manifest and authorizes no run.
continues: BENCHMARK_DECONTAMINATION_AND_DISPATCHABILITY_SCIC_v1
actor: scientist-c (NOT ACTIVATED — operator-directed analytical pilot)
worktree: lettore-c · branch lettore-c
date: 2026-08-26
audience: EVALUATOR ONLY
scope: EVALUATION INFRASTRUCTURE. No governance, role-contract, schema or architecture change.
status: NON-CANONICAL. Mutates no canonical file, manifest, receipt or ledger.
canonical_mutation: NONE
---

# The surface exists

> 🔴 **Evaluator material.** The participant surfaces are the built directories and the orphan
> delivery ref; both are gated by commands, not by promises.

> **Nothing here is medical advice.** · **A/B were not contacted. No blind replication was run.**

---

## 0 · The one line

Three sessions established that a checkout of this repository cannot host a blind reading: `main`
carries an adjudicating artifact for 24 of 27 case papers, spending 43 of 48 cases in every
worktree. The conclusion each time was *build the surface*. **This session built it.**

```
BLIND-FR-001   17 files   d0adbd8a601fb68e2e027d489aa7db4f5500573c5c4fd30ca7d9bc0d05be12af
BLIND-FR-003   15 files   0a8c8c5709c7f23dc983a649044417d8cb21cfdb4782ce5a7bff2d497ee47aff

in a checkout            0 dispatchable
on a built surface      15 fresh-reader eligible
```

And it cost two defects in my own tools to get there, both found by running them rather than
reading them.

---

## 1 · Phase 1 — the blind surface contract

### 1.1 · The mechanism, decided by measurement

| Mechanism | history leakage | tool compat. | reproducible | auditable | cleanup | hashable |
|---|---|---|---|---|---|---|
| **orphan git branch** | 🔴 **FAILS** | ✅ | ✅ | ✅ | ✅ | ✅ |
| plain temp directory | ✅ | 🔴 no repo → the reader cannot meet its `WORK_COMMIT` obligation (D.1) | ✅ | partial — no commit trail | ✅ | ✅ |
| **isolated `git init` repository** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

🔴 **The orphan branch fails, and I shipped one last session.** Measured, not argued — a worktree
of `bench-blind-participant`, the orphan I built:

```
git show main:…/fulltext_read_receipts.jsonl | grep -c "ATR IS NEVER MEASURED"   ->  1
git log --all --oneline | wc -l                                                  ->  915
git branch -a | wc -l                                                            ->   65
```

A branch of any shape shares an object store. `NO_MAIN_ANCESTRY` and `NO_REPOSITORY_HISTORY` are
properties of the **object store**, not of the commit graph, and no branch can have them.

**Decision: an isolated repository — `git init` in a directory outside every checkout.** Which is
what `controlled_benchmark_ab.md` §2.2 already prescribed and nobody had executed.

### 1.2 · The nine properties, and how each is enforced

| Property | Enforcement |
|---|---|
| `NO_MAIN_ANCESTRY` | fresh `git init`; verified `git show main:` → *fatal: invalid object name* |
| `NO_REPOSITORY_HISTORY` | 1 commit · 1 branch · no remotes · **no `objects/info/alternates`** |
| `ALLOWLIST_ONLY` | every file present ⇔ an entry in the build manifest; either direction is a finding |
| `PINNED_SOURCE_BYTES` | SHA-256 per file, source and destination, in the manifest |
| `NO_EVALUATOR_ARTIFACTS` | `LANGUAGE` scan over authored/derived files; the build manifest is written **outside** the surface, because a repository path is history |
| `NO_PRIOR_ADJUDICATION` | `ADJ_FIELD` scan for this repository's record shapes (`verbatim_locators`, `evidence_basis`, `adjudicates`, `FTR-…`) |
| `NO_ANSWER_BEARING_FILENAMES` | neutral destination names by construction + a `FILENAME` screen |
| `PROVENANCE_WITHOUT_INTERPRETATION` | §4 |
| `REPRODUCIBLE_BUILD` | two builds into different roots → **identical tree hash** |

🔴 **Two channels the contract has that no prior spec named**, both found by probing rather than
by thinking:

1. **`CLAUDE.md` discovery walks upward.** A surface placed under a directory that carries a
   `CLAUDE.md` or a `.claude/` inherits it. The builder **refuses** such a destination, and
   refuses any destination with a git working tree above it.
2. **`git init` inherits the global identity.** A fresh repository picks up `user.name` /
   `user.email` from `~/.gitconfig` — here a personal address, differing from the repository's
   shared project identity. The builder sets both explicitly to `benchmark participant`.

**One declared residual.** The prototype root is inside a scratchpad whose *path name* encodes the
repository (`…-Users-⟨op⟩-Desktop-legend-public--claude-worktrees-lettore-c…`). A reader in it
sees the provenance in `pwd`. It leaks no answer, and a real build must use a neutral
`BENCH_ROOT` — which the protocol already declares a local-instance value. Recorded, not hidden.

---

## 2 · Phase 2 — the prototype, built

`framework/eval/benchmarks/blind_rounds/build_blind_surface.py`, case spec in `cases/`.

```
SURFACE      <BENCH_ROOT>/BLIND-FR-001
files        17
tree sha256  d0adbd8a601fb68e2e027d489aa7db4f5500573c5c4fd30ca7d9bc0d05be12af
source-paper rescan hits: 0 OK
```

Every entry carries `SOURCE_OBJECT · SOURCE_HASH · DESTINATION_NEUTRAL_NAME · WHY_REQUIRED ·
NO_ADJUDICATION_ASSERTION`. The packet:

| source | destination | why |
|---|---|---|
| `PMID26675548_AbuOdeh2016.pdf` | `sources/article.pdf` | the only surface panels can be rendered from |
| `PMID26675548_AbuOdeh2016_PMC.xml` | `sources/article.xml` | what verbatim locators quote against |
| `oncotarget-07-4344-s001.pdf` | `sources/supplement_01.pdf` | the published deposit; excluding it would withhold evidence the question needs |
| `oncotarget-07-4344-s002.pptx` | `sources/supplement_02.pptx` | the whole published record, not the part a prior reader found useful |

**Excluded and recorded:** eight prior-reader renders (`supp_page01…07_144dpi.png`,
`table_s1_render.png`) — §2.3, *their selection encodes a prior reader's attention*.

**Eleven of thirteen inherited files copy verbatim. Two are paper-specific** to BENCH-AB-001's own
paper (`BENCHMARK_INSTRUCTIONS.md` ×12, `OUTPUT_SCHEMA.md` ×6) and are **derived by a declared
substitution table**, not re-authored: both digests and every substitution rule go in the manifest,
and the result is re-scanned. Re-authoring would have been faster and would have let the canonical
text drift silently.

**A second surface was built to test that the builder generalises**: `BLIND-FR-003` (PMID 42128308),
15 files, `0a8c8c57…`, PASS, 7/7 mutations blocked.

---

## 3 · Phase 3 — the leakage checker

`check_blind_surface.py`. It is **scoped by how each file got there**, because a blanket scan is
incoherent on a surface:

| Origin | Check | Why not the others |
|---|---|---|
| inherited discipline · mode directive | **IDENTITY** against the manifest | `failure_taxonomy.md` is a taxonomy of overclaims; a language scan fires on the rulebook |
| derived instructions · output schema | IDENTITY + scan for the source paper's identifiers | they were templated, so they can fail by templating |
| **authored** (`ASSIGNMENT.md`) | **DERIVATION** — re-rendered from (template + case spec) and compared | see §3.2 |
| packet | IDENTITY only | it is the source; scanning it for the case's answer is incoherent |
| anything else | `UNALLOWLISTED` — always a finding | |

Plus, surface-wide: `HISTORY` · `FILENAME` · `ANSWER` (everywhere except the packet).

### 3.1 · Seven mutations, seven blocks

```
S1  inject answer text                   BLOCKED   DERIVATION,DIGEST
S2  inject evaluator artifact            BLOCKED   LANGUAGE,UNALLOWLISTED
S3  inject contaminated filename         BLOCKED   FILENAME,UNALLOWLISTED
S4  inject .git history                  BLOCKED   HISTORY
S5  inject one unallowlisted file        BLOCKED   UNALLOWLISTED
S6  inject prior receipt with answer     BLOCKED   ADJ_FIELD,ANSWER,UNALLOWLISTED
S7  build-time leak, manifest regenerated BLOCKED  DERIVATION
```

### 3.2 · 🔴 The hole S7 exists because of

On the first run, six mutations blocked — but **S1 was caught by `DIGEST` alone.** A digest proves
a file has not changed *since* the build. It proves nothing *about* the build.

So I replayed it as a build-time leak: the same sentence, paraphrased, written into `ASSIGNMENT.md`
as if by a careless builder, with the manifest regenerated to match.

> *"Context for the reader: prior work found the kinase named in the title was never measured here."*

No case identifier. No expectation-bearing token. No `ATR`. **It passed every check in the file.**

**The repair is not a wider word list** — that is the blacklist trap, and I have now walked into it
three times in three sessions. `ASSIGNMENT.md` is the only file authored at build time, so it is now
**rendered** from a template plus three fields of the case spec, and the checker **re-renders and
compares byte-for-byte**. Any extra sentence fails whatever its wording, because it is not in the
template. *Identity catches what pattern cannot.* The refactor is behaviour-preserving — the rebuilt
surface has the identical tree hash — and the replay is now S7.

🔴 **Without `--case` the derivation check cannot run, so the checker says so as a finding** rather
than passing quietly.

### 3.3 · A second defect, in the builder

The `BLIND-FR-003` build **refused**: its rescan found `Steinberg` in `sources/article_text.txt`.
The review cites Steinberg in its bibliography, and Steinberg is an author of the paper the
templates were derived from. Aqeilan is senior author of half this corpus — **a whole-surface scan
would have blocked most builds it was written to protect.** The rescan exists to catch a
*templating failure*, and a packet cannot fail that way because nobody templated it. Now scoped to
derived and authored files. Same incoherence as scanning the source for the answer, one file over.

---

## 4 · Phase 4 — provenance without adjudication

`participant_provenance_view.py`, emitting by **whitelist**:
`SOURCE_ID · FILE_HASH · PAGE · FIGURE · CROP · DPI/RECIPE · NEUTRAL_NAME`.

```
papers with >=1 figure artifact       58
ALL fields derivable                   5   15070730  16061658  17803050  21212533  22634283
NO regeneration recipe derivable      53   -> MISSING_PROVENANCE_STRUCTURE
```

**3 → 5 this session**, honestly: two papers carry a publisher URL inside the free-text `route`
field. **A URL is a location; the prose around it is a prior reader's account of retrieval.** Only
the URL crosses, extracted by pattern, emitted as `{kind: fetch, url, expected_sha256}`.

For the other 53, `MISSING_PROVENANCE_STRUCTURE` is exact: `source_artifacts` carries `path`,
`sha256`, `kind` and nothing else for 320 of 333 figure rows. **The blocker is not co-location and
never was** — page, crop and dpi do not exist anywhere outside `page_adjudications`.

🔴 **Not silently derived from adjudication fields.** `adjudications.json` holds
`{file, page, crop, dpi, sha256}` beside `adjudicates`, `needles`,
`why_this_article_is_adjudicated`. The projection reads the first set and never the second — and it
does **not** emit the stored filename, because 7 of 27 of them state conclusions
(`p03_CT_indispensable_no_structure`, `p03_ww1_primarily_responsible`, …). The handle is derived
from the digest instead.

---

## 5 · Phase 5 — fresh-reader eligibility

Not A/B eligibility discounted. A fresh reader on a built surface holds **two things**: the
thirteen inherited files and the packet. `main` is not there.

```
FRESH_READER_ELIGIBLE  15   A4 B5 B6 C1 C2 C3 D1 D2 D4 E2 G1 G3 G4 I3 J2
NOT_ELIGIBLE           33
   source not held                            10   A3 B3 B4 C4 F4 I6 I9 J1 X1 X4
   answer/premise in the inherited files      13   A1 B1 I1 I2 (L3) · A2 E1 E3 F1 F2 H1 I4 I8 J3 (L2)
   no bounded packet                           3   F3 I7 X3
   question is about repository state           2   I10 X2
   rubric (STRESS_ONLY / EXCLUDE / falsified)   5   D3 G2 B2 I5 X5
```

🔴 **The thirteen are the only irremediable class.** Their leak is in a file the reader must hold
to be graded at all: removing it removes the rule the reading is graded against, or changes bytes
the validator must run identically. No build fixes those. Everything else is a *debt* — acquire a
figure raster, name a boundary — and debts close.

---

## 6 · Phase 6 — the pilot

**`ROUND1_CASE_ID: BLIND-FR-001`** (internal `HC-E2`, PMID 26675548), selected **after** the
surface existed and passed.

| Criterion | |
|---|---|
| high value | title asserts a kinase; `ATR` ×30 and `CHK1` ×22 in the body. `CAUSALITY` · `ABSTRACT_VS_FULLTEXT` · `NEGATIVE_EVIDENCE` |
| bounded corpus | one paper, whole published record, four files |
| surface buildable | ✅ built, 17 files, checker PASS, 7/7 mutations |
| answer not leaked | ✅ 0 `L2`/`L3` in the thirteen inherited files; one `L0` |
| evaluator can adjudicate independently | 🔴 **NO — and this is universal, not case-specific** |

🔴 **I have read this case's answer.** It is in `main`, I quoted it last session, and I quoted it
again this one. So I am disqualified as its independent adjudicator — and since 43 of 48 papers are
adjudicated on `main`, **any evaluator who has worked in this repository is disqualified for
almost every case.** That is not a reason to delay the reading: the participant's output is frozen
before anything is compared, and the gold adjudication is a separate act by a separate actor. It is
`NEEDS_SECOND_ADJUDICATOR`, which every case has carried since the first session, now with its
real reason.

`ROUND1_FRESH_READER_PACKET.md` is on the orphan delivery ref: five fields, checker PASS.

---

## 7 · Phase 7 — gold readiness

| # | Case | `MISSING_ACT` | `FIRST_ADJ` | `SECOND_ADJ` | `VISUAL` | `PRIMARY` | `CONTAM_REPAIR` |
|---|---|---|---|---|---|---|---|
| 1 | `HC-A4` | ✅ **done, prior session** | ✅ me | **owed** | no | ✅ XML | none |
| 2 | `HC-C2` | ✅ **done, prior session** | ✅ me | **owed** | no | ✅ XML | none |
| 3 | **`HC-A2`** | ✅ **done, this session — §8** | ✅ me | **owed** | ✅ done | ✅ XML + raster | surface build |
| 4 | `HC-D2` | enumerate the assay inventory of PMID 18487609 | open | owed | no | ✅ PDF + HTML | surface build |
| 5 | `HC-G3` | re-derive the stage confound from PMID 34268881 | open | owed | maybe | ✅ PDF + XML + assets | surface build |

**`GOLD_READY_COUNT: 0`.** Three first adjudications exist; **not one has an independent second**,
and §6 explains why I cannot supply it. I did not self-supply.

---

## 8 · Phase 8 — `HC-A2` stressed

The category must mean *the evidence cannot decide*, not *we did not find it*. Every surface was
opened.

| Test | Measured this session | Result |
|---|---|---|
| all relevant surfaces available | XML 155 476 chars + **7 figure rasters** incl. `Fig7_HTML.png` (`ced68a66…`, 1946×1627) | ✅ complete |
| the panel prints `****` | 🔴 **read off the raster at 2×, not inherited**: the LiCl panel carries `****` on the `+/−` row *and* on the `−/−` row | ✅ confirmed |
| `****` defined in prose | `****` occurs **0 times** in 155 476 chars | ✅ absent |
| any threshold below 0.001 defined | the string `0.0001` occurs **0 times** anywhere | ✅ absent |
| the legend's own definitions | Figure 7 caption defines exactly `n.s., non-significant` and `*** P < 0.001` — two tokens, and the panel prints a third | ✅ |
| Methods | *"statistical tests with one-way analysis of variance (ANOVA)"* — no α below 0.05 declared | ✅ |
| negative control | the ETS panel (7b) uses `***` and `n.s.`, **both defined** — the paper *can* label correctly and does, elsewhere in the same figure | ✅ |

**`HC_A2_UNRESOLVABLE_STATUS: PROVEN — RECORD_DOES_NOT_DECIDE.`** The record is complete; the
token is defined on no surface. Importing `P < 0.0001` from plotting-software convention would be a
fabricated datum with real-looking provenance.

🔴 **Not dispatched**, and the reason is the one the phase warns about: telling a participant a case
is *unresolvable* tells them not to resolve it, which is the answer. `HC-A2` is also
`FULLY_CONTAMINATED` — both readers worked PMID 32000863 heavily and `main` adjudicates it. It
stands as **evaluator evidence that the category is non-empty**, not as a dispatchable item.

---

## 9 · Phase 9 — two layers, never collapsed

```
PAIRWISE_REPRODUCIBILITY        two readings, no gold. Available now.
  observation overlap · locator overlap · epistemic-label overlap
  negative evidence (carried-by-both / by-one / by-neither)
  corpus discipline · contradiction detection (pointer completeness only)
  MEANS reproducibility.    MEANS NOT correctness.

GOLD_ACCURACY                   a reading against the source. Needs an adjudicated gold.
  correctness · overclaim · underclaim · unresolvability recognition
  MEANS correctness.        MEANS NOT reproducibility.
```

🔴 **The dangerous cell is high pairwise + low gold**, and this laboratory will hit it: A and B
share a discipline file, a mode vocabulary and a model. Reporting only the first reads as success.

**Where the two layers see the same dimension differently:** *contradiction detection* is pairwise
for **pointer completeness** (did both name two sides and a governing surface?) and gold for
**whether the contradiction is real** — a fabricated one scores as agreement in the first layer and
as an error in the second. It is listed in both, computed differently, and never summed.

`PAIRWISE_SCORING_READY: YES` · `GOLD_SCORING_READY: NO — 0 adjudicated golds.`

---

## 10 · Phase 10 — the estimand

**Primary `ERROR_PER_CLAIM`; secondary `ERROR_PER_PAPER`.** No single unit covers all questions,
so both are reported and never combined.

| | primary `ERROR_PER_CLAIM` | secondary `ERROR_PER_PAPER` |
|---|---|---|
| `DENOMINATOR` | claims the reading produced — 🔴 **chosen by the reader** | papers drawn from the frame — fixed before the reading |
| `DEPENDENCE` | clusters within paper. **m = 15.7 measured** (1 002 locators / 64 manifests). Independence false; `DEFF = 1+(m−1)ρ`, **ρ not measured** | independent across papers if the draw is |
| `WHAT_FAILURE_MEANS` | one carried claim misstates what its cited evidence bears — the unit the model consumes and a defect propagates through | ≥1 defect of a named class anywhere in the reading — saturating, and **monotone in depth, so it rewards shallow reading** |
| `WHAT_REPEAT_RUNS_MEAN` | 🔴 a **third level**, not more claims: `run ⊃ paper ⊃ claim`. Two runs of one paper are one paper measured twice; their agreement **estimates ρ**, it does not add precision | repeat runs estimate run-to-run variance of the per-paper rate — the only route to the *undetected*-defect rate, at double cost |

The pair is chosen precisely because the first is actionable and gameable and the second is neither.
🔴 **The choice is normative, not empirical**, and the units are not convertible.

🔴 **Still blocked upstream:** the frame is three entry classes — 70 `PAPER`, 188 `CORPUS`, 168
`STUB` = 426 — with no published rule for which is drawn. Every *n* is downstream of that rule.

---

## 11 · Phase 11 — could A or B ever participate?

Four contaminations. **A clean external surface removes two.**

| | What it is | Removed by a built surface? |
|---|---|---|
| `SURFACE` | the files in front of the reader | ✅ **yes** — allowlist + checker |
| `CHECKOUT` | `main` and the reader's branch on disk | ✅ **yes** — the surface is outside every checkout |
| `REPOSITORY` | the object store: `git show main:…`, `git log --all` | ✅ **yes** — fresh `git init`, no alternates, verified |
| `MEMORY/SESSION` | what the actor has already read, in this or an earlier session | 🔴 **NO. Nothing removes it and no command inspects it.** |

**`A_B_FUTURE_ELIGIBILITY`: per case, and only where prior exposure can be EXCLUDED — not merely
not-demonstrated.**

Exclusion is possible in exactly one shape: the case's paper carries **no adjudicating artifact on
`main`** and **no mention on that reader's branch**. Measured, that is three papers — 12065620,
25703206, 32185845 — and the cases on them (`HC-F4`, `HC-J1`, `HC-I6`) are all `source not held`.

```
A_B_FUTURE_ELIGIBILITY   presently 0 cases for A · 0 for B.
                         Not "they are contaminated actors" — they are contaminated PER CASE,
                         and the eligible set is empty because every case they could read is
                         adjudicated in the history they descend from.
                         It becomes non-empty for any case built on a paper acquired AFTER
                         their branches, never read into this repository, and never adjudicated
                         on main. That is a route, and acquiring PMID 12065620 and PMC3139124
                         is the first step on it.
```

🔴 **The honest asymmetry.** A *fresh* reader needs the surface to be clean. A or B additionally
need the *case* to be new to them, and "I have no evidence they read it" is not exclusion. I am not
declaring them eligible for anything.

---

## 12 · What this does not claim

- **It authorizes no run.** `controlled_benchmark_ab.md` §9 still determines
  `BLIND FIRST PASS — BLOCKED BY CANONICALIZATION`; P-2…P-4 remain unmet. A prototype surface is
  not a handover: nothing was transferred to anyone, and §2.2's one-writer rule is untouched.
- **The prototype is a prototype.** Its root is a scratchpad path that names this repository.
- **`GOLD_SCORING_READY: NO`.** Three first adjudications, zero seconds, and I am disqualified.
- **The checker is not complete.** Seven mutations block; a leak phrased outside the `LANGUAGE`
  list still passes any file the `DERIVATION` check does not cover.
- **Nothing here is medical advice.**

---

## 13 · Summary

```
BLIND_SURFACE_ARCHITECTURE      isolated `git init` outside every checkout.
                                Orphan branch REJECTED by measurement: 915 commits, 65 branches
                                and the answer reachable via `git show main:`.
                                Builder refuses a dest inside a working tree, or under a
                                CLAUDE.md/.claude ancestor, and sets git identity explicitly.

PROTOTYPE_SURFACE_BUILT         YES x2
PROTOTYPE_SURFACE_HASH          BLIND-FR-001  d0adbd8a601fb68e2e027d489aa7db4f5500573c5c4fd30ca7d9bc0d05be12af
                                BLIND-FR-003  0a8c8c5709c7f23dc983a649044417d8cb21cfdb4782ce5a7bff2d497ee47aff
                                reproducible: two builds, different roots, identical hash

LEAKAGE_CHECKER_STATUS          PASS. 7/7 surface mutations blocked; 5/5 document mutations.
                                Two defects found in my own tools by running them:
                                  - a build-time leak passed everything (fixed: ASSIGNMENT.md
                                    is now re-derived, not digest-checked) -> now S7
                                  - the builder refused a legitimate build because the review
                                    cites Steinberg (fixed: rescan scoped to derived files)

PROVENANCE_SEPARATION_COUNT     5 of 58   (was 3). 53 = MISSING_PROVENANCE_STRUCTURE.
                                Adjudication fields never read; stored filenames never emitted.

FRESH_READER_ELIGIBLE_COUNT     15   A4 B5 B6 C1 C2 C3 D1 D2 D4 E2 G1 G3 G4 I3 J2
ROUND1_FRESH_READER_READY       YES — surface built, checker PASS, packet on the orphan ref
ROUND1_CASE_ID                  BLIND-FR-001   (internal HC-E2, PMID 26675548)

GOLD_READY_COUNT                0.  Three FIRST adjudications done (HC-A4, HC-C2, HC-A2).
                                Zero seconds. I am disqualified for ~43 of 48 cases because
                                main adjudicates them and I have read it.

HC_A2_UNRESOLVABLE_STATUS       PROVEN. Panel prints **** on both rows (read off the raster);
                                **** occurs 0 times in 155,476 chars; `0.0001` occurs 0 times;
                                the legend defines exactly n.s. and *** P<0.001; Methods declare
                                one-way ANOVA. Negative control: the ETS panel labels correctly.
                                NOT dispatched — the category label is itself the answer.

PAIRWISE_SCORING_READY          YES
GOLD_SCORING_READY              NO — 0 adjudicated golds
PRIMARY_ESTIMAND                ERROR_PER_CLAIM primary + ERROR_PER_PAPER secondary.
                                Normative, non-convertible, m=15.7 measured, rho unmeasured,
                                frame rule still unpublished.

A_B_FUTURE_ELIGIBILITY          0 cases now, for either. A built surface removes SURFACE,
                                CHECKOUT and REPOSITORY contamination — all three verified —
                                and removes nothing of MEMORY/SESSION. Eligibility requires
                                prior exposure to be EXCLUDED per case, which today is possible
                                only for papers not on main and not on their branch: three,
                                all unheld.

NEXT_EVALUATION_ACTIONS         1  Designate a reader with no history here. The surface is built;
                                   the actor is now the binding constraint.
                                2  Move BENCH_ROOT to a neutral path — the prototype root names
                                   this repository in its own directory name.
                                3  Obtain an independent second adjudicator for HC-A4, HC-C2,
                                   HC-A2. Three golds are one act each from existing.
                                4  Acquire PMID 12065620 and PMC3139124: unblocks Round 2, gives
                                   a second UNRESOLVABLE candidate, and is the only known route
                                   to A/B ever being eligible for anything.
                                5  Publish the frame rule (PAPER / CORPUS / STUB).
```

🔴 **The line to carry.** Every session so far found the leak one level further out and concluded
*build the surface*. Building it took one afternoon, and the two things that nearly defeated it were
not in the repository at all — they were in my own instruments: a checker that certified a build it
had not inspected, and a builder that refused a clean paper for citing the wrong author. **The
contamination work is done; what remains is an actor.** The surface can be built. A reader who has
never opened this repository cannot.
