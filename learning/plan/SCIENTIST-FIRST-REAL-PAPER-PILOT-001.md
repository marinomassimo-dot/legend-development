---
artifact: SCIENTIST — the first real scientific experiment, designed against the benchmark that is not one
record_id: SCIENTIST-FIRST-REAL-PAPER-PILOT-001
task_id: SCIENTIST_FIRST_REAL_PAPER_PILOT_v1
author: plan
authored_on: 2026-08-22
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)

STATUS: READ_ONLY_ANALYSIS · DESIGN PROPOSAL
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - ANALYSIS AND DESIGN PROPOSAL
  - NOT GOVERNANCE
  - NOT A PROTOCOL
  - NOT EXECUTION AUTHORIZATION
  - NOT A DECISION
  - NOT AN AGENT DEFINITION
  - NOT A ROLE
  - NOT A PAPER SELECTION

naming_note: >
  Not a Session Learning Record (Annex E.6) and not a handoff. Named as the dispatch named it,
  and takes no `SLR` number it has not earned — the precedent of the five non-SLR records
  already in this seat.

domain: >
  CONTENT — verified this session, not inherited. `governance/plan_defined_parameters.md` § P5.1
  (lines 255–267, read at this HEAD) declares `CONTROL_PLANE_ROOTS` exhaustively as
  `governance/candidates/`, `ledger/`, `reviews/`. `learning/` is under none of them, so this
  file sits inside the `CANDIDATE_CONTENT_HASH` of any future candidate spanning this branch and
  moves it. Disclosed.

relation_to_prior_work: >
  This record answers `Q-1` of `SCIENTIST_RUNTIME_PROFILE-001` — *"what is the configuration for
  a real reading?"* — which that record raised and explicitly refused to answer, assigning it to
  operator (strategy) → Plan (structure). The dispatch supplies the strategy half. Four adjacent
  records already hold ground this one does not restate: `SCIENTIST-PIPELINE-READINESS-001`,
  `SCIENTIST-PIPELINE-EXECUTION-MODEL-001`, `SCIENTIST-BOOTSTRAP-CONTRACT-ANALYSIS-001` and
  `SCIENTIST_RUNTIME_PROFILE-001`. Every mechanical fact reused from them was re-run at this
  HEAD before being written here.

verdict_transfer: >
  NONE. Every measurement below was executed in this session, at the HEAD named in § 1, by the
  command shown beside it.
---

# SCIENTIST — THE FIRST REAL SCIENTIFIC EXPERIMENT — 001

> **The three findings that shape this record.**
>
> **1 · Blindness and the corpus are not actually in conflict — `BENCH-AB-001` conflated two
> different exclusions.** It removes the whole corpus in order to guarantee that no reader sees
> LEGEND's prior output *on this paper*. The second is what matters; the first is only the
> cheapest proof of it. **If the paper has never been read, the prior output does not exist, and
> the corpus can be present without breaking anything.** The blindness moves out of the surface
> and into the *paper selection* — where it is proved by an enumerated command over the corpus
> rather than promised by a reader. This is the structural answer to `Q-1`, and it costs one new
> discipline: a **two-stage read**, closed then cross-queried, with a freeze between them.
>
> **2 · 🔴 The pool of papers that could carry this pilot is close to empty at this HEAD, and the
> shortfall is not a scheduling problem.** Measured: **116** papers in the surface census, **82**
> with a receipt, **48** without one, **12** of those with a `structured` + `clean` local surface.
> Of those 12 I re-measured the surfaces myself in the shared checkout: **three carry no readable
> body at all** (`42395553` body = 0 chars against a 2 066-char abstract; `38355659` body = 258;
> `30470736` body = 308), and by title, journal and article type the residue is predominantly
> **oncology and review**, not WWOX-DEE primary data. **The census verdict `structured` + `clean`
> is not sufficient to select a pilot paper**, and the paper this pilot needs will most likely
> have to be *acquired*, not found.
>
> **3 · 🔴 The destination the design has been assuming does not exist.** `unresolved_disagreements.md`
> is named as the landing place for every disagreement flag by `controlled_benchmark_ab.md` § 8.3
> and is referenced on **16 refs**. `git ls-tree` over **every branch in the repository** finds the
> file on **zero** of them. A disagreement produced by the first real experiment today has nowhere
> to be recorded, and §27 makes an unresolved disagreement a *legitimate outcome* — which means the
> outcome the governance most explicitly protects is the one the state cannot hold.

---

## TASK_STATUS

```
TASK_ID          SCIENTIST_FIRST_REAL_PAPER_PILOT_v1
MODE             ANALYSIS + DESIGN PROPOSAL · no actor creation · no role activation ·
                 no contract binding · no paper selected · no protocol materialized
STATE            COMPLETE — the seven study areas are answered. Every answer that could be
                 measured was measured; every answer that is a design choice is marked as a
                 proposal with the party who owns the decision.

EXECUTED         BENCH-AB-001's 7 instruction files read in full · protocol §0–§1, §8, §9, §10
                 read · scientist_reading_modes §0–§1 · roles/scientist.md and roles/mirror.md
                 in full · Annex C.1–C.4 · Annex H.1 · body §26–§33 · epistemic_discipline
                 §1–§2 · fulltext_read_receipt §1–§4 · ingest_protocol steps 2–4 · P5.1 ·
                 14 executable measurements (lease, fingerprint, approval-queue parse, surface
                 census vs reading-state set difference, XML body/abstract measurement over 12
                 candidate surfaces in the shared checkout, all-refs greps, all-refs ls-tree,
                 claim-registry label counts, builder CLI, surface-spec parse)
NOT EXECUTED     no Scientist created, spawned, contacted or assigned · no paper opened, read or
                 selected · no pilot protocol written to framework/ · no candidate opened · no
                 surface built · no lease taken · no contract issued · no path under governance/
                 roles/ framework/ ledger/ runtime/ disease-models/ modified · no schema, field
                 or vocabulary created in any normative file
FILES ADDED      exactly one — this file
```

---

## IDENTITY

### 1 · From repository evidence; not from `roles/scientist.md` or `roles/plan.md`, neither of which is binding

| Field | Measured value | Command |
|---|---|---|
| branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `b72af2f25d42c3cafb781d42b66ef3a1761cdb66` | `git rev-parse HEAD` |
| worktree | `.claude/worktrees/evidence-index` | `git rev-parse --show-toplevel` |
| working tree | **clean** at session start | `git status --porcelain` → empty |
| lease | **`ACTIVE by derivation: 0`** (5 leases: 2 stale, 3 released) | `python3 framework/scripts/lease_state.py` |
| scientist fingerprint | `b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a` | `governance_fingerprint.py compose --role scientist` |

`CLAUDE.md` § 0: no ACTIVE lease and no runtime inventory ⇒ `BOOTSTRAP_MODE`. This session is
not Orchestrator, issues nothing, and creates no actor. The single act it performs — writing one
file under `learning/plan/` on its own branch — traces to **H.1 `WORK_COMMIT`** (*"ogni attore,
solo proprio branch, granularità milestone"*), an annex, not a role contract.

**The fingerprint is unchanged from the value composed in the previous record** at `9e10190`,
which is expected: `b72af2f` added one file under `learning/`, and no input of the scientist set
is under `learning/`. `B-8` — the stale `ce3c0d94…` recorded in the runtime inventory and the
Agent Card registry — **is still owed and still uncleared**.

---

## 1 · BENCHMARK VERSUS SCIENCE

### 1.1 · What `BENCH-AB-001` measures

Read from `controlled_benchmark_ab.md` §0 and §8, not summarized from memory.

| | |
|---|---|
| **object under measurement** | **the instrument.** Two reading *modes* applied to one paper |
| **manipulated variable** | exactly one — which mode directive is addressed to you. 18 of 20 surface files byte-identical; `ASSIGNMENT.md` and `benchmark/MODE_DIRECTIVE.md` differ |
| **dependent variables** | ten process dimensions (§ 8.2): coverage · claim precision · provenance · locator fidelity · epistemic discipline · context preservation · methods/limitations · contradiction/negative evidence · mechanistic value (listed, not judged) · failure modes |
| **denominator** | fixed before anyone reads — **65 evidence units, 109 panels** |
| **what it refuses** | a composite score; a weighting; agreement as a quality measure; speed/tokens/cost as quality |
| **destination of its output** | **quarantine, by construction.** *"None of the seven is written to `claim_registry_current.md`"*; § 10 forbids integrating a claim into the disease model, writing any `*_current.md`, or touching the receipt ledger. The receipt id `BENCH-AB-001-<ACTOR>-01` is declared in the schema as *"benchmark id, NOT a receipt-ledger id"* |
| **corpus access** | **none.** `corpus_crossquery`, `multihop` and `group_assessment` are waived by instruction, and the schema tells the reader to *"waive them, and say THAT is why"* |
| **what it can conclude** | bounded by its own two declared caveats: session variance is not separable from mode with one paper and one session per actor; and each reader can read the other's directive inside the common `scientist_reading_modes.md` |

**It is a calibration of a reading instrument, and it is honest about being one.** Its value, in
its own § 0, is *"the material it produces… and the failure modes it surfaces, not a number."*

### 1.2 · What `SCIENCE-PILOT` must measure — and the two things it must not inherit

The pilot's object is **not** the reader. It is **the pipeline**: whether an independent double
reading of a paper the model has never seen can produce a **commitable increment to the disease
model** without either reader contaminating the other, and without the model contaminating either.

| | `BENCH-AB-001` | `SCIENCE-PILOT` |
|---|---|---|
| object under measurement | the two reading modes | the pipeline, `SOURCE → READ → CANDIDATE`, end to end |
| manipulated variable | the mode directive | **none.** This is not a comparative experiment |
| what varies by design | mode A vs mode B | nothing is varied to be compared; two modes are used because that is the pipeline's shape |
| corpus | absent | **present, pinned, and opened only in stage 2** |
| blindness carried by | the surface (23 forbidden paths + a content scan) | **the paper choice** (a null-prior proof over the pinned corpus) |
| receipt | a benchmark id, ledger untouched | a real `FULLTEXT_READ_RECEIPT` in the hash-chained ledger, one per reader |
| destination | quarantine | `disease-models/wwox/research/commit_candidates/` — **and stops there** |
| what success means | the material and the failure modes | independence held · reasoning traceable · review possible · failures identifiable (§ 7) |

🔴 **Two inheritances the pilot must refuse, both of which would look like continuity.**

**It must not score A against B.** The moment the pilot ranks the two readers, the destination
becomes a confound: a MODE A claim that reaches a commit candidate and a MODE B criticism that
does not are not two grades of the same thing, they are two different objects with different
landing places. Worse, `roles/scientist.md` and body § 32 make the three Scientists *equivalent*,
and a result reported as "A did better than B" is precisely the static specialization § 32
forbids, restated as a finding. `BENCH-AB-001` § 8.5 already refuses it; the pilot must refuse it
for a second, independent reason.

**It must not treat a produced claim as its success condition.** A pilot that succeeds only if
something commits creates pressure to commit. `BATCH_COMMIT` is Orchestrator's under an ACTIVE
lease (H.1) and is a separate authorized act. The pilot ends at *candidate proposed*.

### 1.3 · 🔴 The structural resolution of `Q-1` — blindness without removing the corpus

`SCIENTIST_RUNTIME_PROFILE-001` § 13 named the tension and did not resolve it: *"the mechanism
that makes the first experiment trustworthy is the mechanism a real experiment cannot keep."*

**The tension dissolves once two exclusions that `BENCH-AB-001` bundles are separated.**

```
E1  no LEGEND prior output ABOUT THIS PAPER     ← the exclusion that protects the reading
E2  no corpus at all                            ← the proof BENCH-AB-001 chose for E1
```

`E2 ⇒ E1`, and the benchmark needs `E2` because its paper — PMID 42397075 — **has been read**
(two partial receipts, `FTR-20260809-42397075-01` and `-02`, recorded in `FT-010`). With prior
output in the tree, removing the tree is the only mechanical guarantee.

**`E2` is sufficient and not necessary.** Select a paper with **zero** receipts, zero manifest,
zero dossier, zero commit candidate, zero claim citing it and zero queue prose stating its
findings, and `E1` holds *with the corpus present* — because there is nothing about the paper in
the corpus to be contaminated by. And unlike a prohibition, this is a **property of the corpus**,
enumerable by command, provable before the run and re-provable after it.

Two objects carry it:

**`CORPUS_PIN`** — one commit SHA of the shared checkout **plus** the `files/` tree digest, since
`files/` is gitignored and the SHA does not cover the evidence bytes (`fulltext_read_receipt.md`,
*"Evidence locality across branches"*). Both readers resolve the same pin, read-only. The pin is
re-digested at the end of the run; any change during the run is a declared contamination.

**`NULL_PRIOR_PROOF`** — an enumerated, command-produced proof, archived with the run, that the
corpus at the pin contains no LEGEND statement about the paper. Every hit is either zero or is a
*bibliographic mention* — identifier, title, journal, year and nothing else — listed individually
and shown to state no finding. One line of a queue entry that summarizes a result disqualifies
the paper; `FT-002` is the worked example of why, and it is seven paragraphs of findings.

**And the anchoring risk, which `E1` does not touch, is answered by staging rather than by
prohibition.** A reader who opens the working model before reading the paper will look for
confirmation, and no allowlist detects that.

```
STAGE 1 · CLOSED READ    the packet only. Corpus unreadable. Produces manifest, dossier,
                         claim candidates, receipt. → FROZEN, before anything else opens.
STAGE 2 · CROSS-QUERY    the pinned corpus opens. The reader records what the model already
                         says, and whether stage 1 corroborates / narrows / contradicts it.
                         → an ADDENDUM. It may not edit stage 1.
```

The freeze between the stages is the same instrument `BENCH-AB-001` already uses at the same
moment, for the same reason, and it is what makes anchoring **detectable**: the pre-corpus record
exists, is digested, and cannot be revised. Stage 2 is also where *"possibilità di dissentire"*
stops being an aspiration — disagreeing with the existing model is a first-class stage-2 output
with its own destination.

---

## 2 · PAPER SELECTION

### 2.1 · Eight criteria — five gates and three scores, each with the command that decides it

**The screen is metadata-only, and the screener is disqualified from reading.** Anyone who reads
the paper to judge whether it qualifies has spent the blindness they were checking for. Plan may
run this screen and only this screen: it is structural, decides nothing about meaning, and is
therefore inside § 28.

| # | Criterion | Gate/score | How it is decided, mechanically |
|---|---|---|---|
| **C-1** | **NULL PRIOR** — zero LEGEND statements about the paper at the pin | **GATE** | the `NULL_PRIOR_PROOF` sweep: receipt ledger · `reading_state.md` · `deepdive_manifests/` · `fulltext_dossiers/` · `commit_candidates/` · `paper_registry_current` · `literature_tracking_log_current` · `claim_registry_current` · `full_text_queue_current` · `discovery_ledger` · `dismissal_ledger`. Zero, or bibliographic-mention-only with each mention enumerated |
| **C-2** | **SURFACE SUBSTANCE** — a structured surface that is actually a body | **GATE** | 🔴 *not* the census verdict. `structured` + `clean` passes three files that have no readable body (§ 2.2). The predicate is the relational one the queue's Appendix 3 already argues for and `deepdive_manifest._xml_surfaces` already computes: **a body not substantially larger than its own abstract is not a body**. Plus `caption_census.py` for figures outside `<body>` |
| **C-3** | **VERIFIABLE PRIMARY DATA** — a countable evidence population, and it is the authors' own | **GATE** | `benchmark_input_surface.py population` against a spec written for the paper. A review, editorial, correction or commentary carries no primary evidence unit, cannot support a `DATO`, and cannot exercise the pipeline. Article type comes from metadata, never from reading |
| **C-4** | **WWOX-DEE RELEVANCE** — the paper measures WWOX or a WWOX genotype in a system the disease model can receive | **GATE** | title/abstract/MeSH from metadata. Bridge and oncology literature can only produce `ESPANSIONE`, which by `epistemic_discipline` § 1 *"cannot enter the current files as consolidated fact"* — so the pilot would end with nothing to land |
| **C-5** | **NO ADJUDICATION DEBT** | **GATE** | no retraction and no retraction-forward (`retraction_check`, run by Plan before handover); not an erratum entangled with a read paper — this is exactly what disqualifies `PMID 38355659`; no unresolved preprint/published ambiguity |
| **C-6** | **SINGLE OWNERSHIP** — no in-flight reading elsewhere | **GATE** | 🔴 `reading_state.md` says of itself: *"This page is true of ONE checkout."* An all-refs sweep is required, not a local check. See the `:r`-modifier trap in the sweep note below |
| **C-7** | **DISSENT SURFACE** — at least one existing claim the reading could corroborate, narrow or reverse | **SCORE** | structural overlap of pathway / endpoint / model / genotype against the 39 claims of `claim_registry_current.md`. Zero overlap is not disqualifying; it means stage 2 will be empty and the pilot will not exercise the half that only a real experiment has |
| **C-8** | **COMPLEXITY BAND** — differentiating, and completable at full depth in one session | **SCORE** | the evidence-unit count from C-3, read as a band. A two-page case report leaves the two readers nothing to diverge on; a 60-panel multi-omics paper makes both declare partial and the pilot measures budget instead of method. PMID 42397075's **65 units / 109 panels** is a defensible upper anchor: the benchmark's own designers treated it as one session's work |

**Why "possibilità di dissentire" is a score and not a gate.** A pilot on a paper with no bearing
on any existing claim still measures independence, traceability and reviewability — three of the
four success criteria in § 7. It only fails to exercise the fourth kind of output (paper-vs-corpus
contradiction). Making it a gate would let a scarce corpus veto the pilot entirely.

### 2.2 · The screen, applied at this HEAD — and what it returns

| Measurement | Value | Command |
|---|---|---|
| papers in the surface census | **116** | `grep -oE '^\| PMID [0-9]+' surface_census.md \| sort -u \| wc -l` |
| papers with ≥1 receipt | **82** (128 receipts) | same over `reading_state.md` |
| papers with no receipt | **48** | `comm -23` of the two sets |
| of those, `structured` + sentinel `clean` | **12** | census columns 3–4 |

Those 12 are the whole pool that could satisfy C-1 and C-2 without an acquisition. I measured
their surfaces directly in the shared checkout — the numbers below are mine, not the census's:

| PMID | surface | body chars | abstract chars | verdict |
|---|---|---:|---:|---|
| 42395553 | `_PMC.xml` | **0** | 2 066 | 🔴 **C-2 FAIL** — no `<body>` element at all |
| 38355659 | `_PMC.xml` | **258** | 0 | 🔴 **C-2 + C-5 FAIL** — and it is the *correction* to `38182577`, which is read |
| 30470736 | `_PMC.xml` | **308** | 0 | 🔴 **C-2 FAIL** — body present, empty |
| 27551470 | `_PMC.xml` | 9 489 | — | body thin for a full report; 1 `<fig>` |
| 31428585 | `_PMC.xml` | 10 645 | — | 0 `<fig>` in body — form 3 or a review; `Front Oncol` |
| 16223882 · 18460020 · 21731849 · 21115974 · 25245215 · 26499798 | `_PMC.html` | 39 k–66 k text | — | substantive; C-3/C-4 unresolved from metadata alone |
| 25238781 | `_PMC.html` | **12 894** | — | short for a primary report; `Aqeilan 2014` |

🔴 **Three of twelve fail C-2 on a measurement the census cannot make**, and the queue's own
Appendix 3 predicted exactly this: *"la forma 2 è la più pericolosa delle tre, ed è quella che
nessuna guardia attuale vede"* — a body that exists, is 258 characters, passes every existence
check, and would validate as `article_text` in a manifest until a locator tried to quote a
sentence that is not there.

🔴 **And the residue is the wrong literature.** By title, journal and author line — Fabbri 2005
`PNAS`, Nakayama 2008, Del Mare 2011, Fu 2011 `Blood`, Hazan 2015, Chang 2019 `Front Oncol`,
Aqeilan 2014 ×2, Abu-Remaileh 2015 `JBC R115` — the unread structured residue is predominantly
**oncology and review**. Against C-3 and C-4 that is close to a clean sweep of disqualifications,
and I cannot tighten the judgement without reading, which the screen forbids.

**The operational consequence, stated plainly: the pilot's paper probably has to be acquired.**
That makes acquisition a precondition rather than a convenience (`P-14`, § 8), and it points the
selection at fresh WWOX-DEE primary literature — which is also, not coincidentally, where C-4 and
C-7 are strongest. `find-fulltext` is the existing route.

**Three caveats on every number above, each of which shortens its validity.**
`surface_census.md` is dated **2026-08-15** and says of itself *"a photograph, not an invariant"*;
`files/fulltext/` is gitignored, so the corpus differs per checkout — **this worktree holds 13
entries, the shared checkout 174**; and `reading_state.md` is true of one checkout only. **The
screen must be re-run at the pin, in the shared checkout, at selection time.** Nothing here
selects a paper, and § 2 is not a shortlist.

> **A sweep note that will otherwise cost a false negative.** An all-refs check written in zsh as
> `git show "$r:path"` applies the `:r` history modifier and strips the extension, returning
> ABSENT on every ref. Always `${r}:path`, and always run a positive control against a ref where
> the file is known to exist. This is how the `unresolved_disagreements` negative in the header
> was checked — via `git ls-tree -r --name-only "$r"`, with the branch list expanded once.

---

## 3 · SCIENTIST A AND B — WHAT IS IDENTICAL, WHAT DIFFERS, WHAT IS FORBIDDEN

### 3.1 · Identical — and how each is *proved* identical, not asserted

| Input | Carrier | Proof of identity |
|---|---|---|
| the paper packet | `source_files` | SHA-256 per file, equal across both surfaces; `verify` enforces parity |
| **the pinned corpus** | `CORPUS_PIN` | one commit SHA **plus** the `files/` tree digest; both re-derived at completion |
| the discipline set | `common_files` | `epistemic_discipline` · `gold_is_in_the_details` · `fulltext_read_receipt` · `scientist_reading_modes` · `failure_taxonomy` — byte-identical, and unaltered by this being a pilot |
| the output schema | `common_files` | one shape, or there is no comparison |
| the two-stage protocol | `common_files` | both readers must know that stage 1 freezes before stage 2 opens |
| validator + completion gate | `common_files` | `deepdive_manifest.py --verify-artifacts --require-current-schema`, `VERDICT: PASS` as a precondition, not a self-report |
| `PARALLEL_READ_GROUP` | `ASSIGNMENT.md` | the declaration that makes two readings *intended* rather than a `DUPLICATED_ASSIGNMENT` (`scientist_reading_modes` § 2) |

### 3.2 · Differing — exactly two files, unchanged from the benchmark

```
ASSIGNMENT.scientist-a.md → ASSIGNMENT.md          ASSIGNMENT.scientist-b.md → ASSIGNMENT.md
MODE_A.md → benchmark/MODE_DIRECTIVE.md            MODE_B.md → benchmark/MODE_DIRECTIVE.md
```

With the § 0 caveat carried forward unsoftened: `scientist_reading_modes.md` is a **common** file
and describes both modes in full, so the variable is attention, not information. **In the pilot
this caveat costs nothing**, because the pilot does not compare the modes (§ 1.2) — the leak
degrades a comparison that is not being made.

### 3.3 · Forbidden — each with the mechanism, not the promise

| Excluded | Mechanism | Reaches |
|---|---|---|
| LEGEND's prior output on this paper | **C-1 + `NULL_PRIOR_PROOF`** | absolute — it does not exist to be read |
| the other reader's output, identity, progress or existence beyond the group declaration | separate worktrees, no channel, Orchestrator relays no content | structural; a `BLOCKER` is answered *on the protocol, never on the paper* |
| the corpus, **during stage 1** | staging + freeze | 🔴 a prohibition, not a wall — see § 3.4 |
| any external network retrieval, both stages | **the pilot is network-free for both readers** | Plan performs the retraction check before handover, so no reader needs the network for any mandated step. This removes a whole contamination class at the cost of one pre-step |
| a research question, evidence target, or hypothesis to test | not present in any input file | excluded **by design**, not omitted — `SCIENTIST-BOOTSTRAP-CONTRACT-ANALYSIS-001` § 3.2, re-affirmed |
| any anticipated conclusion, from operator, Orchestrator or Plan | H.1: *"Conclusione scientifica — Scientist responsabile (soggetta a review, mai a ordine)"* | governance, and it binds the dispatcher too |
| the evaluation population | Plan holds the denominator; it is not in the surface | a reader who knew it could optimize coverage against it |
| the pilot's own evaluation design | forbidden path | the reader is not shown how it is scored |

### 3.4 · 🔴 The honest limit, restated for the configuration that changes it

In `BENCH-AB-001` every *before* and *after* check is mechanical and only the *during* checks are
prohibitions. **The pilot moves one thing from the mechanical column into the prohibition column**:
the corpus is physically reachable during stage 1, and "do not open it yet" is an instruction.

Three things bound the damage, and none of them is a promise:

1. **the stage-1 freeze precedes stage 2** — the pre-corpus record is digested and immutable, so
   an anchored reading cannot be retro-fitted;
2. **`benchmark_input_surface.py locators` checks membership per entry** — a stage-1 locator
   pointing at a corpus path is `BENCH_INVALID` for that entry, *recorded, never silently dropped*;
3. **declaring is cheap** — *"a declared contamination is a usable result, and an undeclared one
   silently invalidates the experiment for everyone."*

This is a real weakening relative to the benchmark and it is the price of the corpus. It is stated
here, before the design's benefits, so it cannot be discovered later as a defect.

---

## 4 · OUTPUT CONTRACT

### 4.1 · The dispatch's seven concepts, against the carriers that exist

Re-measured at this HEAD. **Four map cleanly. Three do not, and the three are the work.**

| Dispatch concept | Carrier | Verdict |
|---|---|---|
| **observation** | `**Observation:**` — required, and free of conclusion verbs | ✅ exists |
| **interpretation** | 🔴 **two fields**: `**Author interpretation:**` and `**LEGEND interpretation:**` | ⚠️ **do not collapse.** *"The seam is the point… the one thing a second reader must be able to attack is where measurement ends and conclusion begins."* A single `Interpretation` field destroys exactly the seam the design exists to hold open |
| **hypothesis** | the epistemic `**Type:**` — `DATO · INFERENZA · IPOTESI · ESPANSIONE`, compound allowed | ⚠️ **a property, not a slot.** A hypothesis is a *typing of a claim*, not a container beside it. Adding a `Hypothesis:` field would create a second place where epistemic level lives, and the two would drift |
| **evidence** | `verbatim_locators` + `source_artifacts` in the manifest; `**Locators:**` on the claim | ✅ exists — with one pilot-specific addition, § 4.3 |
| **uncertainty** | `**Uncertainty:** what is not settled, and by what` | ✅ exists — and § 4.2 is about its second clause |
| **missing evidence** | 🔴 the `OMISSION` axis — **MODE B only** | 🔴 asymmetric. `grep -niE 'omission\|expected to see\|did not find\|missing'` over `MODE_A.md` returns **0 hits**. In a *benchmark* that asymmetry is the variable. In a *production* run it is a hole |
| **contradiction** | `**Contradictory evidence:**` (both) + `CONTRADICTORY_EVIDENCE` axis (B) | ✅ **intra-paper.** The *inter*-corpus one does not exist and cannot, in a design with no corpus — § 4.4 |

For the record, because it is the reason those three are *fields* and not conventions: measured
over the **39** claims of `claim_registry_current.md`, the labels `**Uncertainty:**`,
`**Limitations:**` and `**Contradictory evidence:**` appear **0, 0 and 0** times.

### 4.2 · 🔴 "Missing evidence" for MODE A — the container already exists, and it is a clause

The tempting fix is a new `Missing evidence:` field for MODE A. **It is the wrong fix**, and the
benchmark instructions say why in general terms: *"if you find yourself inventing a container, the
container already exists — the schema names where."*

It does. `**Uncertainty:** what is not settled, **and by what**`. The second clause *is* the
missing evidence, scoped to the claim. Annex C.2 carries the same object under review, as
`EVIDENCE_NEEDED`. The defect is not an absent field; it is that the second clause is written as
prose and nothing checks it.

**Proposal — one gate, no new field:**

> A claim candidate whose `Uncertainty` names what is unsettled but **not what would settle it**
> is incomplete, and the completion self-check fails it — the same way a coverage map containing
> `not_read` fails a `complete_fulltext_read`.

The two scopes then stay distinct and both are covered:

```
MODE A   claim-scoped     Uncertainty's second clause — "this claim needs X, the paper has no X"
MODE B   paper-scoped     the OMISSION axis — "I expected to see X in this paper and did not"
```

This resolves `Q-5` **inside the pilot's scope only**. It does not touch `BENCH-AB-001`, whose
schema is a frozen benchmark artifact, and it does not promote anything into
`claim_registry_current.md` — `Q-2` stays open and stays the operator's.

### 4.3 · 🔴 Stage 2 citations are not locators, and mixing them breaks the validator

A stage-2 addendum cites the corpus. A stage-1 locator cites the packet. They are different
objects with different guarantees, and the manifest has exactly one `verbatim_locators` array.

If a corpus citation is written as a locator, one of two things happens, and both are bad: the
allowlist check reports it as outside the surface and the entry is invalidated, or — worse, if the
corpus is inside the workspace — it validates, and the paper's evidence set silently acquires
sentences the paper does not contain.

**Proposal:** stage 2 writes `corpus_reference` entries in the addendum, never into
`verbatim_locators`. Each carries `{claim_or_locator_ref, corpus_path, corpus_pin, quote, relation}`
where `relation ∈ corroborates · narrows · contradicts · orthogonal · supersedes_premise`. The
stage-1 manifest is frozen and gains nothing.

### 4.4 · The addendum — the half only a real experiment has

Two of the pilot's seven output concepts acquire a second, inter-corpus scope that
`BENCH-AB-001` structurally cannot produce:

| Object | Where it goes | Why there |
|---|---|---|
| paper-vs-corpus **contradiction** | 🔴 `unresolved_disagreements.md` — **the file does not exist on any ref** (§ 8, `B-11`) | § 8.3 sends every disagreement flag there to *stay* unresolved; § 27 makes that a legitimate outcome |
| a corpus **negative** the paper reopens | `dismissal_ledger_current.md`, with its `REVIVAL_TRIGGER` | `epistemic_discipline` § 2.3: *"every time a new mechanistic `DATO` arrives, re-scan the dismissal ledger."* A rejection recorded anywhere else is a rejection nobody re-scans |
| a corpus **premise** the paper undercuts | the addendum, tagged `supersedes_premise`, plus the `PREMISE_TAG` it displaces | `PREMISE: DEFAULT_FROM_TEXTBOOK` is the class most likely to be hit |
| corroboration | the commit candidate's *Proposed canonical propagation* | the shape `CC-20260811-21075834-01` already uses |

### 4.5 · What each reader produces, and where it lands

```
disease-models/wwox/research/deepdive_manifests/PMID<X>.json       schema v2, stage 1, FROZEN
disease-models/wwox/research/fulltext_dossiers/PMID<X>.md          stage 1, FROZEN
<run>/output/claim_candidates.md                                   stage 1, FROZEN
<run>/output/receipt.json                                          coverage, blockers, self-check
<run>/output/critical_reading.md                                   MODE B only — every axis answered
<run>/output/renders/…                                             pixels only, digested
<run>/output/stage2_addendum.md                                    corpus_references + disagreements
ledger/…  FULLTEXT_READ_RECEIPT                                    🔴 REAL, hash-chained, one per reader
disease-models/wwox/research/commit_candidates/CC-<date>-<PMID>-NN.md   the terminus
```

🔴 **The receipt ledger already models the pilot's output shape, and `BENCH-AB-001` opted out of
it unnecessarily.** `reading_state.md` measured at this HEAD: **1 paper read in parallel by two
receipts sharing a parent** (`PMID 42422765`), and the protocol states the rule beside it —
*"Two actors can read one paper in parallel and both be right; the later receipt is not a
correction of the earlier one."* Two receipts on one paper is not an exception the pilot needs
built; it is the documented normal case.

**And the artifact-workspace split is not optional.** `files/` is gitignored, so a branch carries
the manifest and not the bytes. Both readers must run with `--artifact-workspace` pointing at the
shared checkout, and *"the strict manifest command that counts is launched with the shared
checkout as the current directory."* A PASS obtained inside an ephemeral worktree is
*"historically true but operationally unverifiable and does not close the read."*

---

## 5 · PEER SCIENTIST — WHEN A THIRD ACTOR IS NEEDED

### 5.1 · Four different functions get confused into one question

The dispatch is right not to assume C is synthesis, and the repository forbids it twice over:
§ 27 — *"la sintesi forzata è un errore"*; § 28 — Plan *"NON risolve significato scientifico
conteso."* But "do we need a third Scientist" collapses four things that have different triggers,
different inputs and different authority. **Only one of them is a third reader, and only one of
them is even a Scientist.**

| # | Function | Trigger | Receives | Authority |
|---|---|---|---|---|
| **F-1** | **third reading** of the same paper | both first passes declared **partial** with non-overlapping gaps such that the union still leaves the population uncovered | the packet + a mode scoped to the gap; **not** either reading | a reader. This is a coverage remedy, not an adjudication |
| **F-2** | **peer review of an inference** | C.1 floors: `inferenza L2 importante → R1 PEER`; `therapeutic-actionable → R2 INDEPENDENT` | the claim + its locators + the packet; **not** the other reading | C.4: `INFERENCE → peer Scientist`. Reviewer, not reader. *"reviewer senza evidenza contribuita"* |
| **F-3** | **adjudication** of persistent disagreement | `disaccordo scientifico persistente → R3 TRIADIC`, and only after **max 2 rounds** | both statements, quoted and typed, plus both locator sets | a **turn**, never a post. C.3: `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`, rotation, *"mai coppie fisse"* |
| **F-4** | **blind locator audit** | 🔴 **always** — it is not conditional | only `(proposition, quote, anchor)` triples + the source artifact. **No dossier, no conclusions, no reader identity** | **not a Scientist.** Forms no scientific conclusion and holds no authority. `legend-locator-audit` is the existing instrument |

🔴 **F-4 is the one most often mistaken for "a third Scientist" and it is the least like one.**
It answers two mechanical questions per triple — does the quote support the proposition, and does
the source say MORE or LESS than the proposition claims — and it must be blind, including to
authorship. The operator's own recorded experience is the argument: *a reviewer who did not know
the authorship found eight defects two informed reviewers had passed over twice.*

### 5.2 · What the pilot needs in its baseline, and what it only routes

**Baseline:** two readers and **F-4 over 100 % of triples** — not a sample, since a sampled audit
reports a rate and the pilot needs a per-triple verdict on the claims it may propose.

**Routed, not scheduled:** F-2 and F-3 are triggered by *what the readings turn out to contain*,
which is unknowable at design time. A pilot that pre-commits to "three Scientists" has decided in
advance that a disagreement will occur. **So the pilot declares the routing rule, not the actor
count** — and every opening runs through Orchestrator (C.3: *"apertura solo via Orchestrator"*),
never through Plan and never actor-to-actor.

**F-3's job is not to produce a verdict.** Under § 27 it is to determine which kind of
disagreement it is:

```
EVIDENTIAL     resolvable by a datum       → EVIDENCE_NEEDED → full_text_queue_current
INFERENTIAL    not resolvable today        → DISAGREEMENT_UNRESOLVED, recorded and left open
```

### 5.3 · `scientist-c` — and the inversion that is not a reason

Measured, and unchanged from the previous record: `scientist-c` is `REGISTERED_PENDING_L1_L2`
with a verified fingerprint, while `scientist-a` and `scientist-b` are `NOT_REGISTERED` with
`ACTOR_ID UNRESOLVED`. **The one Scientist that is registered is the one no design uses.**

That is an operational accident, and it is not an argument for giving C a function. C becomes the
static specialization § 32 forbids the moment it acquires a *fixed* one — and
`APPROVAL-GOV311-DEVIATIONS.md` line 265 sketches exactly the forbidden shape,
`A → B hostile review → C adjudication`, which makes adjudication a post rather than a turn.
**Nothing in this pilot requires C, and `Q-4` stays open and stays the operator's.**

---

## 6 · MIRROR HANDOFF

### 6.1 · The pilot's process review has floor R4, and that is measured, not chosen

C.1: `processo inferenziale methodology-changing → R4 METHOD (Mirror)`, *"derogabili solo verso
l'ALTO."* A first end-to-end run of a new pipeline configuration is methodology-changing on its
face. **R4 is therefore the floor, and going below it requires a registered rationale.**

### 6.2 · What Mirror receives

| Class | Contents |
|---|---|
| **process** | both stage-1 readings **as frozen, digested artifacts** · both stage-2 addenda · per-actor timeline, handover → freeze, from the receipts · the surface manifests with `verify`, `verify-freeze` and `verify --post-read` output · the `NULL_PRIOR_PROOF` · the `CORPUS_PIN` and its end-of-run re-digest · the F-4 per-triple verdicts · Plan's structural comparison matrix · every disagreement flag with both statements quoted and typed · contamination declarations · blockers |
| **metadata** | `ACTOR_ID`s · `TASK_ID`s · modes · `PARALLEL_READ_GROUP` · the governance fingerprint each checkpoint was written under · generation · the review levels Orchestrator assigned and why |
| **its own two metrics** | the checkpoint invalidation rate (A.6) and the redone-work ratio (A.7) — `roles/mirror.md` names both as Mirror's specific responsibility for calibrating what Plan defined |

Mirror's questions are § 29 and G.1 questions: was the process sound, did independence hold, where
did the method fail, what is the failure-mode inventory. *"The question is always why, never who
won"* (body § 46).

### 6.3 · What Mirror does **not** receive, and the mechanism for each

| Withheld | Mechanism | Why it would destroy independence |
|---|---|---|
| **either reading before both are frozen** | handoff is gated on the second freeze | Mirror reads through Orchestrator's channel; a Mirror observation on A, relayed while B is still reading, is a contamination path with a governance actor in the middle |
| **any streaming view during the run** | no incremental handoff | same path, slower |
| **Plan's or the operator's preference between the readings** | § 8.5 — no overall score, no weighting; the matrix is structural and unweighted | a ranking handed to the adjudicator of *method* invites the method verdict to follow the science verdict |
| **authorship, wherever the review can be blind** | 🔴 it cannot be, for Mirror | see § 6.4 |
| **the power to decide whether the claim commits** | H.1 — `CANONICAL_BATCH_COMMIT` is Orchestrator's alone, under an ACTIVE lease | Mirror *"holds no command over any actor and produces no primary evidence"* |
| **self-review of its own rubric** | § 29.2 / G.2 — `MIRROR_UPGRADE_PROPOSAL` → Plan candidate → an independent reviewer chosen by Orchestrator | if the pilot's method changes Mirror's rubric, Mirror may not ratify that itself |

### 6.4 · 🔴 The pilot needs two reviews, because one of them cannot be blind and the other must be

**Mirror's review cannot be blind and should not be.** Process review needs to know who did what:
the anti-fossilization guard of § 32 is a statement *about actors over time*, and it is
unanswerable without identities.

**The locator audit must be blind and Mirror is not its auditor.** F-4 receives triples and a
source artifact — no dossier, no conclusions, no names.

These are not two grades of the same review; they are two different objects from C.4 —
`SYSTEM → Mirror` and `EVIDENCE → Scientist + Plan/provenance` — and running only one leaves the
other's failure class undetected. The pilot needs both, in that separation.

---

## 7 · SUCCESS CRITERIA FOR THE FIRST PILOT

**The dispatch is right that the criterion is not scientific truth, and the repository already
refuses the alternative shape.** § 8.5: *"No overall score. No weighting."* So the pilot's criteria
are enumerable states with the command that decides each — never a number, never a threshold.

### 7.1 · Four conditions, each decided by a command

**`S-1 · INDEPENDENCE HELD` — proved, not promised**

| Check | Passes when |
|---|---|
| packet parity | per-file SHA-256 equal across both surfaces |
| corpus pin integrity | the commit SHA and the `files/` tree digest re-derive **unchanged** at completion |
| freeze ordering | both stage-1 freeze timestamps precede any stage-2 open and any cross-exposure, from the receipts |
| stage-1 locator containment | `benchmark_input_surface.py locators` — every stage-1 entry inside the packet allowlist; **zero corpus paths** |
| null prior | the `NULL_PRIOR_PROOF` re-runs at the pin with the same enumerated result |
| contamination | **zero undeclared.** A *declared* one does not fail S-1; it is a usable result and is reported |

**`S-2 · REASONING TRACEABLE`**

`deepdive_manifest.py --verify-artifacts --require-current-schema` → `VERDICT: PASS`, both readers ·
`fulltext_receipts.py verify` → chain intact **after** both receipts are appended · every carried
statement typed · every negative carrying `PREMISE_TAG` **and** `REVIVAL_TRIGGER` · every
`Uncertainty` carrying its "settled by" clause (§ 4.2) · coverage map with **no `not_read`**, or an
honestly declared partial · every `corpus_reference` resolving at the pin.

**`S-3 · REVIEW POSSIBLE` — and it is *tested*, not assumed**

A commit candidate exists per reader · F-4 ran on **100 %** of triples with a per-triple verdict ·
the comparison matrix aligns rows **structurally, by shared unit** — never by Plan's reading of
whether two claims "mean the same" · every disagreement flagged, quoted, typed and landed.

> **The operational test:** one reviewer who was not present reconstructs **one** claim from the
> record alone, without asking anyone, and reaches the same evidence. A record that requires its
> author to explain it has not passed.

**`S-4 · FAILURES IDENTIFIABLE` — the detection surface is published before the run**

A pilot that reports "no failures" without an enumerated detection surface has measured nothing.
So the pilot names in advance, from `framework/eval/failure_taxonomy.md` plus this design's own
classes, every failure state it is *capable* of detecting, and reports which occurred and which
were searched for and not found. **Silence on a class is an incomplete report, not a clean run** —
the same rule MODE B's axes already carry.

### 7.2 · Explicit non-criteria — written down so they cannot be smuggled back in

```
agreement between A and B      two readers agreeing on an overshoot is two overshoots (§ 8.5)
number of claims produced      a count without a population is not a number
speed · tokens · cost · length recorded apart, never a quality proxy (§ 8.4)
whether anything commits       BATCH_COMMIT is a separate authorized act — see § 1.2
whether the reading "found     the pilot measures the apparatus, not the paper's luck
  something important"
scientific truth               not available, and not the question
```

### 7.3 · The states that make the pilot a failure

Undeclared contamination · a silently thinned reading claimed as complete · a stage-2 addendum
that **edits** stage 1 · a stage-1 locator resolving outside the packet · a corpus mutation
mid-run · **any write to a `*_current.md` inside the pilot** · a handover made while any
precondition of § 8 is unsatisfied.

### 7.4 · 🔴 The pilot's own falsifier

`WHAT_WOULD_CHANGE_MY_MIND` is mandatory in this repository's review format, so this design owes
one:

> **If the run shows that independence cannot be preserved with the corpus reachable — a stage-1
> locator drawn from the corpus, a stage-2 addendum that contradicts a frozen stage-1 claim in a
> way only prior knowledge explains, or a declared anchoring contamination — then § 1.3's
> resolution of `Q-1` is wrong, and `E2` is necessary after all.**

That outcome is a **successful pilot with a negative result**, it must be reportable as such, and
the fallback it implies is a real one: corpus-blind stage 1 in a surface, corpus cross-query
performed by a **different** actor in a second task. Recorded as `Q-9`.

---

## 8 · PRECONDITIONS AND BLOCKERS

The pilot inherits every blocker of `BENCH-AB-001` — re-measured at this HEAD, none cleared — and
adds seven of its own.

| # | Blocker | Clearing act | Owner |
|---|---|---|---|
| **B-1** | `CAND-20260818-SCIENTIST-AB-SPEC` carries no approval line — the queue holds 6 lines, 2 approvals, both `CAND-20260816-GOV311` | operator resolution appended to `HUMAN_APPROVAL_QUEUE.jsonl` | **operator** |
| **B-2** | both protocols and `roles/scientist.md` remain `PROPOSED` | follows from B-1 via `CANONICAL_BATCH_COMMIT` | Orchestrator, lease ACTIVE |
| **B-3** | L2 suspended by the C-9 hold; 0 of 27 capabilities `VERIFIED` | lift the hold, then run L2 | **operator**, then Orchestrator |
| **B-4** | `scientist-a`/`-b` unregistered; worktrees 136/138 commits behind | sync, then I.2 step 7 registration | Orchestrator + the actors |
| **B-5** | no ACTIVE lease (`ACTIVE by derivation: 0`) | take a lease | Orchestrator |
| **B-6** | no Task Contract for either Scientist | issue two, naming resolved `ACTOR_ID`s | Orchestrator, under lease |
| **B-7** | no surface built; manifest `PREPARED — NOT FROZEN` | `build → verify → freeze` after B-1…B-6 | Plan, under a task |
| **B-8** | the recorded scientist fingerprint `ce3c0d94…` is stale against the composed `b66959cd…` | recompose and update the inventory row | **Plan** — owed, independent of B-1, **still uncleared** |
| **B-9** | 🔴 **no pilot protocol object exists.** `SCI-PILOT`, `SCIENCE-PILOT`, `CORPUS_PIN`, `NULL_PRIOR` → **0 refs each** | a Plan candidate materializing the two-stage protocol, the surface spec and the null-prior sweep | operator authorizes → Plan materializes under a task |
| **B-10** | 🔴 **no paper qualifies at this HEAD** without acquisition (§ 2.2) | run the screen at the pin in the shared checkout; acquire via `find-fulltext` if the pool is empty | Plan screens (metadata only); **operator/Orchestrator selects** |
| **B-11** | 🔴 **`unresolved_disagreements.md` exists on 0 of 40 refs** while being named on 16 | create it with its writer and its append discipline | Plan, under a task |
| **B-12** | the `Uncertainty` second-clause gate (§ 4.2) is a proposal with no implementation | decide, then implement in the completion self-check | operator (or Mirror, per `Q-5`) → Plan |
| **B-13** | the `corpus_reference` entry shape (§ 4.3) does not exist | define in the pilot's output schema; **not** in `deepdive_manifest` schema v2 | Plan, under a task |
| **B-14** | the paper packet must exist in the **shared checkout's** `files/` tree, not a worktree | acquire, verify, digest before handover | Plan, under a task |

**`B-1` is still the root**, exactly as it was. **`B-9`, `B-10`, `B-11` are new and none of them
depends on `B-1`** — they can be prepared while the approval is pending. `B-8` remains the only
one clearable today, by this actor, under a task it does not hold.

🔴 **The sequencing constraint that will cost a run if it is missed, carried forward unchanged.**
Canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC` **rotates the scientist fingerprint**, and
a checkpoint written under the old value is `INCOMPATIBLE` under A.6 the moment the spec becomes
canonical. A pilot started before `B-2` would have to be abandoned or resumed under a fingerprint
it was not written under. The rotation is confined to the scientist set.

### 8.1 · Order — and the honest case for each

`SCIENTIST_RUNTIME_PROFILE-001` § 13 argued that *"a method you have not calibrated should not be
pointed at a disease model."* That argument still holds and I am not quietly dropping it. But it
is not the only consideration, so here is the cost of each order rather than a flat verdict.

| Order | Cost |
|---|---|
| **`BENCH-AB-001` first** | the calibration is bought, and the pilot inherits a measured instrument. But BENCH is blocked on `B-1`, an operator act with no date, and the whole apparatus produces **no science** until it clears |
| **`SCIENCE-PILOT` first** | science is produced sooner, on an **uncalibrated instrument**. The mitigation is structural and already in the design: the pilot stops at a commit candidate and never auto-commits, so an uncalibrated reading cannot reach the model without the ladder and `BATCH_COMMIT` — two gates with named owners |

**Recommendation, since the dispatch asks for a real paper and not a benchmark: the pilot, with
the calibration deferred and its risk named.** The two runs do not subsume each other — BENCH's
extra control is the clean mode variable, the pilot's extra variables (corpus present, two stages,
a real destination) make that variable noisier — so deferring BENCH defers a real measurement and
does not delete it. **The order is the operator's decision, not mine**, and both are defensible.

---

## 9 · OPEN QUESTIONS

Recorded, not resolved. `Q-1` is answered structurally in § 1.3 and *implemented* nowhere.

| # | Question | Owner |
|---|---|---|
| **Q-1** | ✅ **answered structurally** (§ 1.3): blindness moves into paper selection; corpus present under a pin; two stages with a freeze between. **Unimplemented** — `B-9` | operator authorizes → Plan materializes |
| **Q-2** | do the seven benchmark fields become canonical claim-registry fields, or stay run-local? Unchanged and still deferred by `OUTPUT_SCHEMA.md` § 3 | operator, on a Plan candidate |
| **Q-4** | what is `scientist-c`'s function, and when is its `ACTOR_ID` fixed? § 5.3 gives it none | operator + Orchestrator at registration |
| **Q-5** | the `OMISSION` asymmetry — § 4.2 proposes a resolution scoped to the pilot only, as a gate on an existing clause rather than a new field | Mirror (method), on a Plan note |
| **Q-7** | 🔴 **which paper?** § 2 gives the criteria and the screen; the pool is near-empty and acquisition is likely required. **This record deliberately selects nothing** | operator/Orchestrator, on Plan's metadata-only screen |
| **Q-8** | may Plan run the selection screen at all, given the screener is thereby disqualified from reading? § 28 says yes — it is structural and decides nothing about meaning — but it should be stated in the pilot protocol rather than assumed | operator, on the pilot candidate |
| **Q-9** | if § 7.4's falsifier fires, is the fallback corpus-blind stage 1 with cross-query by a **different** actor in a second task? Designing it now would pre-commit to a failure | operator, only if it fires |
| **Q-10** | 🔴 does a **declared** partial reading still qualify to produce a commit candidate? BENCH says a declared partial is a legitimate result — but BENCH's output was quarantined. With a real destination, "legitimate result" and "sufficient to move the model" are not the same question, and nothing on any ref answers the second | operator, on the pilot candidate |

---

## 10 · VALIDATION

### 10.1 · Constraint compliance — checked, not asserted

| Constraint from the dispatch | Compliance |
|---|---|
| operate as Plan | ✅ identity from repository evidence (§ 1), not from a `PROPOSED` contract |
| no authority from role contracts | ✅ the one act performed traces to H.1 `WORK_COMMIT`; stated in § 1 |
| no Scientist activation | ✅ none created, spawned, contacted, assigned or registered |
| define BENCH vs SCIENCE | ✅ § 1, from the protocol's own § 0 / § 8 / § 10, re-read this session |
| define paper-selection criteria | ✅ § 2 — eight criteria, five gates, three scores, each with its deciding command, **and the screen applied at this HEAD** |
| define A/B inputs, identical and forbidden | ✅ § 3, including the one place the pilot is measurably weaker than the benchmark (§ 3.4) |
| define the output contract | ✅ § 4 — four concepts map, three do not, and the three are treated as the work |
| analyse when a third Scientist is needed | ✅ § 5 — four functions separated; C given no function; **no synthesis actor proposed** |
| define the Mirror handoff | ✅ § 6, including the two reviews that cannot both be blind |
| define pilot success criteria | ✅ § 7 — four conditions, six non-criteria, seven failure states, one falsifier |
| do not assume C is synthesis | ✅ § 5.3 — and § 27 forbids forced synthesis independently |
| output to the named path | ✅ `learning/plan/SCIENTIST-FIRST-REAL-PAPER-PILOT-001.md` |

### 10.2 · What this record does NOT do

It does not authorize, start, schedule or scope the pilot · select, acquire or open a paper ·
register or qualify any actor · verify a capability · lift the L2 hold · take a lease · issue a
Task Contract · build, verify or freeze a surface · create `unresolved_disagreements.md` ·
implement the `Uncertainty` gate or the `corpus_reference` shape · write any protocol into
`framework/` · open a governance candidate · update the runtime inventory or the Agent Card
(**`B-8` is reported, not performed** — for the second record running) · decide `scientist-c`'s
function · propose `scientist-d` or `-e` · read any paper · form any scientific conclusion.

Everything in §§ 1.3, 2.1, 4.2, 4.3, 5.2, 6.3 and 7 marked *proposal* is a proposal. None of it
binds anyone, and § 8 names who would have to act for any of it to become real.

---

## 11 · NEXT_TRANSITION

The dispatch asked for the first **real** scientific experiment, and the answer has a shape now
that it did not have four hours ago: **the paper carries the blindness, the corpus stays and is
pinned, the read happens in two stages with a freeze between them, the receipt is real, and the
run ends at a commit candidate.** That is `Q-1`, answered.

**It is also unbuilt, and the shortest path to it is not the approval queue.** `B-9`, `B-10` and
`B-11` are independent of `B-1` and can be prepared while the approval sits:

```
B-11   create unresolved_disagreements.md — named on 16 refs, existing on 0
B-10   run the selection screen at the pin, in the shared checkout, metadata only;
       expect to acquire rather than to find
B-9    materialize the two-stage protocol, the surface spec, the null-prior sweep
B-8    recompose the scientist fingerprint into the inventory — still owed, still uncleared
```

Each is Plan's, under a task Plan does not hold today. `B-1` remains the root of everything else,
and it remains the operator's.

🔴 **And the finding worth carrying out of this record above the design:** the pilot's hardest
constraint is not governance and not independence. It is that **the corpus's unread residue is
oncology and reviews**, and the first real scientific experiment will have to begin by acquiring
the paper it is about.
