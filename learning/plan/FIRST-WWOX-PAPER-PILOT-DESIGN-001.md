---
artifact: FIRST WWOX PAPER PILOT — the design, and the three freezes the repository can only half hold
record_id: FIRST-WWOX-PAPER-PILOT-DESIGN-001
task_id: FIRST_WWOX_PAPER_PILOT_DESIGN_v1
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
  - NOT A SCIENTIST ACTIVATION

naming_note: >
  Named as the dispatch named it. Not a Session Learning Record (Annex E.6), not a handoff, and
  it takes no `SLR` number it has not earned — the precedent of the six non-SLR records already
  in this seat.

domain: >
  CONTENT — verified this session. `governance/plan_defined_parameters.md` § P5.1 declares
  `CONTROL_PLANE_ROOTS` exhaustively as `governance/candidates/`, `ledger/`, `reviews/`.
  `learning/` is under none of them, so this file sits inside the `CANDIDATE_CONTENT_HASH` of any
  future candidate spanning this branch and moves it. Disclosed.

relation_to_prior_work: >
  Six Scientist records precede this one. Two of them — `SCIENTIST-FIRST-REAL-PAPER-PILOT-001`
  and `SCIENTIST-ACTIVATION-READINESS-001` — already hold the ground this dispatch's sections 1,
  2, 3 and 6 cover. This record does not restate them. It re-measures their load-bearing numbers
  at this HEAD (§ 2), maps the dispatch's four selection criteria onto the eight that exist and
  names the two the dispatch drops (§ 2.3), and then spends its length on the one section no
  prior record holds: **FREEZE POINTS** (§ 4), and the merge that depends on them (§ 5).

verdict_transfer: >
  NONE. Every number below was produced by a command run in this session at the HEAD named in
  § 0.2, and the command is shown beside it. Where a prior record reached the same number I say
  so; where my measurement contradicts a prior record's framing I say that too (§ 5.4).
---

# FIRST WWOX PAPER PILOT — DESIGN — 001

> **The four findings that shape this record.**
>
> **1 · The dispatch names three freeze points. The pipeline it describes has four moments, and
> the repository mechanises one of them.** `before reading` is real and commanded. `after reading`
> is two distinct moments once the read is staged — closed read, then corpus cross-query — and
> `benchmark_input_surface.py` cannot tell them apart: `FIRST_PASS_STATES` has exactly three
> values (`COMPLETE_DECLARED_BY_ACTOR · ABANDONED · TIMED_OUT`), none of which means *stage 1
> done, stage 2 pending*. `before comparison` is **not a freeze at all** — it is a join over a
> pair, and `verify-freeze` takes one receipt and one surface. It has no instrument.
>
> **2 · 🔴 The merge cannot produce all three outputs the dispatch asks for, because governance
> forbids one of them as stated.** Body § 27: *"la sintesi forzata è un errore."* "Scientific
> synthesis" is therefore not a third product sitting beside disagreement — it is only what is
> left where the two readings align **structurally, by shared locator anchor**, and Plan is
> barred by § 28 from deciding that two differently-worded claims mean the same thing.
>
> **3 · 🔴 "Mirror input" splits into two destinations, and one of them needs an actor the pilot
> does not have.** Body § 26 routes divergence to **R3 TRIADIC**; Annex C confirms *"disaccordo
> scientifico persistente → R3"*. R3 needs a third Scientist. Mirror's own object is the R4
> question — *perché* the two diverged — and § 29.3 [v3.1.1] makes Mirror's **primary** analysis
> surface the consolidated EVENT LEDGER (J.1). `ledger/` holds four subdirectories at this HEAD;
> none of them is an event ledger.
>
> **4 · 🔴 This is the seventh Scientist record, and the sixth ended by saying it should not
> exist.** `SCIENTIST-ACTIVATION-READINESS-001` § 8 closed: *"The sixth should not be a seventh;
> it should be a paper."* I have written the seventh because it was dispatched, and because § 4
> is genuinely new. **It does not change that verdict, and I restate it in § 7.3 rather than
> bury it.** The corpus has not moved: 174 entries on the census date of 2026-08-15, 174 today.

---

## TASK_STATUS

```
TASK_ID          FIRST_WWOX_PAPER_PILOT_DESIGN_v1
MODE             ANALYSIS + DESIGN PROPOSAL · no paper execution · no Scientist activation ·
                 no actor created · no contract issued · no lease taken · no surface built ·
                 no freeze run · no paper selected
STATE            COMPLETE — the six requested sections are answered and the final question is
                 answered in § 7. Every answer that could be measured was measured; every answer
                 that is a design choice is marked as a proposal with the party who owns it.

EXECUTED         controlled_benchmark_ab.md §6, §7, §8.2, §8.3, §8.5 read in full · GOVERNANCE
                 §26, §27, §28, §29, §32 · annex_c_review_protocol ladder + routing table ·
                 annex_g_mirror G.1–G.3 · annex_j_runtime_control_plane J.1 ·
                 file_generation_rule §0–§0.1 · benchmark_input_surface.py CLI surface + source
                 line 739 · 17 executable measurements (git identity, lease derivation, scientist
                 fingerprint, all-refs ls-tree sweep with positive control, census screen
                 recomputed from raw rows, XML body/abstract measurement over all 12 pool
                 surfaces in the shared checkout, population JSON parse, seat directory
                 enumeration, ledger enumeration, tree-digest positive control, corpus pin
                 computation, erratum entanglement trace)
NOT EXECUTED     no Scientist created, spawned, contacted, assigned or activated · no paper
                 opened, read or selected · no pilot protocol written to framework/ · no
                 candidate opened · no surface built · no freeze or verify-freeze run against any
                 actor tree · no path under governance/ roles/ framework/ ledger/ runtime/
                 disease-models/ modified · no schema, field or vocabulary created in any
                 normative file
FILES ADDED      exactly one — this file
```

---

## 0 · IDENTITY AND PIN

### 0.1 · Why this section exists before the design

A design that names a corpus must name *which* corpus. `files/fulltext/` is gitignored, so the
commit SHA does not cover the evidence bytes, and two checkouts at the same SHA can hold
different papers. Both halves are recorded here so that every number below can be re-derived.

### 0.2 · Measured, not inherited

| Field | Measured value | Command |
|---|---|---|
| branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `b72af2f25d42c3cafb781d42b66ef3a1761cdb66` | `git rev-parse HEAD` |
| worktree | `.claude/worktrees/evidence-index` | `git rev-parse --show-toplevel` |
| working tree | 2 untracked files, both prior records of this seat | `git status --porcelain` |
| lease | **`ACTIVE by derivation: 0`** — 5 leases, 2 stale, 3 released | `lease_state.py` |
| scientist fingerprint | `b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a` | `governance_fingerprint.py compose --role scientist` |

`CLAUDE.md` § 0: no ACTIVE lease and no runtime inventory ⇒ `BOOTSTRAP_MODE`. This session is not
Orchestrator, issues nothing, creates no actor, and activates no Scientist. The single act it
performs — writing one file under `learning/plan/` on its own branch — traces to **H.1
`WORK_COMMIT`**, an annex, not a role contract.

The fingerprint is byte-identical to the value composed in both prior records. That is the
expected result and not a copy: the two commits since then touched only `learning/`, and no input
of the scientist set is under `learning/`. **`B-8` — the stale `ce3c0d94…` recorded in the runtime
inventory and the Agent Card registry — is still owed and still uncleared.**

### 0.3 · 🔴 A concrete `CORPUS_PIN`, computed rather than described

Prior records specified the *shape* of `CORPUS_PIN` — commit SHA plus `files/` tree digest — and
left it unvalued because no command had been shown to produce the second half. It exists:
`benchmark_input_surface.py tree-digest --path <any path>` accepts an arbitrary path, and I
verified it against a known directory before pointing it at the corpus.

```
CORPUS_PIN  (candidate, this instant, shared checkout — NOT a selection and NOT a freeze)
  checkout        <repo-root>   branch main
  commit          788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
  files/fulltext  b48694a13d07c691242d1dcbfcd592a77002ba1450ae2e97eee3cb69e27318da
                  654 file(s) recursive · 174 top-level entries
  positive ctrl   tree-digest on BENCH-AB-001/population → 97953f55…  1 file(s)   ✓ exits 0
```

🔴 **Two numbers that are both true and are routinely confused.** `surface_census.md` reports
*"174 entries"* — that is a top-level `ls`. The recursive file count is **654**, because
supplementary asset directories hang under paper entries. **A pin taken as "174 files" would not
detect a supplement being added or swapped**, and supplements are exactly where `FT-050` recorded
the reading debt that held `PMID 38182577` at `partial`. The pin must be the recursive digest.

**Consequence for the design: the corpus-pin half of the input freeze needs no new tool.** It
needs a field in a manifest and the discipline to re-run it at the end of the run. That is the
cheapest of every gap this record names.

---

## 1 · WHAT THE PILOT IS FOR

Stated once, because §§ 2–6 are only coherent against it.

The pilot's object is **the pipeline**, not the reader. It asks whether an independent double
reading of a paper the model has never seen can produce a **traceable, reviewable, resumable
increment** — and it ends at *candidate proposed*, never at *committed*. `BATCH_COMMIT` is
Orchestrator's under an ACTIVE lease (H.1) and is a separate authorized act.

Three inheritances it must refuse, each for a reason that survives without the others:

| Refused | Why | Authority |
|---|---|---|
| **scoring A against B** | the two modes have different landing places; ranking them makes the destination a confound, and reports as a finding precisely the static specialization § 32 forbids | body § 32; benchmark § 8.5 |
| **a produced claim as the success condition** | a pilot that succeeds only if something commits creates pressure to commit | H.1; § 7.2 below |
| **agreement as a quality measure** | two readers agreeing on an overshoot is two overshoots | benchmark § 8.5, verbatim |

---

## 2 · PAPER SELECTION

### 2.1 · The dispatch's four criteria, made mechanical

The dispatch names four. Each maps onto a gate that already has a decision procedure. **The screen
is metadata-only and the screener is disqualified from reading**: anyone who reads the paper to
judge whether it qualifies has already spent the blindness they were checking for. Plan may run
this screen and only this screen — it is structural, decides nothing about meaning, and is
therefore inside § 28.

| Dispatch criterion | Gate | Decided by |
|---|---|---|
| **no previous LEGEND contamination** | **C-1 NULL PRIOR** | enumerated sweep at the pin over: receipt ledger · `reading_state.md` · `deepdive_manifests/` · `fulltext_dossiers/` · `commit_candidates/` · `paper_registry_current` · `literature_tracking_log_current` · `claim_registry_current` · `full_text_queue_current` · **`discovery_ledger_current`** · `dismissal_ledger_current`. Zero hits, or bibliographic-mention-only with every mention enumerated and shown to state no finding |
| **readable full text** | **C-2 SURFACE SUBSTANCE** | 🔴 *not* the census verdict — see § 2.2. The predicate is relational: **a body not substantially larger than its own abstract is not a body**. Plus `caption_census.py` for figures outside `<body>` |
| **sufficient evidence** | **C-3 COUNTABLE PRIMARY POPULATION** | `benchmark_input_surface.py population` against a spec written for the paper. A review, editorial, correction or commentary carries no primary evidence unit, cannot support a `DATO`, and cannot exercise the pipeline. Article type from metadata, never from reading |
| **biological relevance** | **C-4 WWOX-DEE RELEVANCE** | title/abstract/MeSH from metadata. Bridge and oncology literature yields `ESPANSIONE`, which per `epistemic_discipline` § 1 *"cannot enter the current files as consolidated fact"* — the pilot would end with nothing to land |

### 2.2 · The screen re-run at this HEAD — and the three papers the census verdict passes and the body fails

I recomputed the census screen from the raw table rows rather than reusing a prior count.

| Measurement | Value | Command |
|---|---|---|
| papers in the surface census | **116** | `grep -oE 'PMID [0-9]+' surface_census.md \| sort -u \| wc -l` |
| papers with ≥1 receipt | **82** | same over `reading_state.md` |
| papers with no receipt | **48** | `comm -23` of the two sets |
| of those, `structured` **and** sentinel `clean` | **12** | join of the set difference against census columns 3–4 |

The twelve are the entire pool that could satisfy C-1 and C-2 without an acquisition. I measured
their surfaces directly in the shared checkout — these are my numbers, not the census's:

| PMID | surface | body chars | abstract chars | figs in body | verdict against C-2 |
|---|---|---:|---:|---:|---|
| 42395553 | `_PMC.xml` | **0** | 2 066 | 0 | 🔴 **FAIL** — no `<body>` content at all; the abstract is the whole surface |
| 38355659 | `_PMC.xml` | **258** | 0 | 0 | 🔴 **FAIL** — and it fails C-1 and C-5 independently (§ 2.4) |
| 30470736 | `_PMC.xml` | **308** | 0 | 0 | 🔴 **FAIL** — body element present, body empty |
| 27551470 | `_PMC.xml` | 9 489 | 0 | **0** | thin for a primary report, and no figure reaches `<body>` |
| 31428585 | `_PMC.xml` | 10 645 | 0 | **0** | `Front Oncol` — no figure in body; review-shaped |
| 25238781 | `_PMC.html` | 30 743 | — | — | short for a primary report — `Aqeilan 2014` |
| 16223882 · 18460020 · 21115974 · 21731849 · 25245215 · 26499798 | `_PMC.html` | 58 k – 85 k | — | — | substantive; C-3/C-4 unresolved from metadata alone |

**A measurement caveat I will not launder.** The HTML figures are tag-stripped whole-document
character counts and therefore include navigation, reference lists and publisher boilerplate.
They are an **upper bound**, not a body measurement, and are not comparable to the XML `<body>`
numbers beside them. Only the XML rows above support a C-2 verdict as written.

🔴 **Three of twelve fail C-2 on a measurement the census cannot make.** The queue's own
Appendix 3 predicted this exact form: *"la forma 2 è la più pericolosa delle tre, ed è quella che
nessuna guardia attuale vede"* — a body that exists, is 258 characters, passes every existence
check, and would validate as `article_text` in a manifest until a locator tried to quote a
sentence that is not there.

🔴 **And the residue is the wrong literature.** Fabbri 2005 `PNAS`, Nakayama 2008, Del Mare 2011,
Fu 2011 `Blood`, Aqeilan 2014 ×2, Abu-Remaileh 2015, Chang 2019 `Front Oncol` — the unread
structured residue is predominantly **oncology and review**. Against C-3 and C-4 that is close to
a clean sweep of disqualifications, and I cannot tighten the judgement further without reading,
which the screen forbids.

**The operational consequence, stated plainly: the pilot's paper most likely has to be acquired.**
That makes acquisition a precondition rather than a convenience, and points the selection at
fresh WWOX-DEE primary literature — which is also where C-4 is strongest. `find-fulltext` is the
existing route. **Nothing in this section selects a paper, and it is not a shortlist.**

### 2.3 · 🔴 The two gates the dispatch's four do not cover

The dispatch's four criteria are **necessary and not sufficient**. Two further gates exist in the
prior design, and dropping them is not a simplification — each one disqualifies a paper that
passes all four.

| Gate | What it catches that the four do not | Why it cannot be folded into another gate |
|---|---|---|
| **C-5 NO ADJUDICATION DEBT** | retraction; retraction-forward; an erratum entangled with an already-read paper; an unresolved preprint-vs-published ambiguity | a retracted paper can have a perfect body, primary data, WWOX relevance and zero prior LEGEND output. C-1 through C-4 all pass. The pilot would then produce a traceable, reproducible reading of a withdrawn result |
| **C-6 SINGLE OWNERSHIP** | the paper being read right now in another checkout | 🔴 `reading_state.md` says of itself *"This page is true of ONE checkout."* C-1 run locally proves nothing about a reading in flight elsewhere. This requires an **all-refs** sweep |

Two further criteria are **scores, not gates**, and the distinction matters: **C-7 DISSENT
SURFACE** (does an existing claim exist that this reading could corroborate, narrow or reverse)
and **C-8 COMPLEXITY BAND**. A paper with zero overlap against the 39 claims of the registry
still measures independence, traceability and reviewability — three of the four success criteria
in § 6. Making C-7 a gate would let a scarce corpus veto the pilot entirely.

### 2.4 · The worked example, traced this session

`PMID 38355659` is the correction *"Correction: WWOX promotes osteosarcoma development via
upregulation of Myc"* to `PMID 38182577`, which `reading_state.md` records as
`complete_fulltext_read` with 2 receipts. It is therefore disqualified **three times over, by
three independent gates**:

```
C-2  body = 258 characters
C-5  erratum entangled with a completely-read paper
C-1  discovery_ledger_current.md already carries a LEGEND statement ABOUT the erratum —
     "L'errata PMID 38355659 corregge un nome d'autore e non tocca il titolo"
```

**That over-determination is the argument for keeping all the gates.** Each caught it alone. A
screen reduced to the dispatch's four would have caught it on C-2 only — by 258 characters — and
a paper whose body happened to be 4 000 characters would have passed a screen that three
independent gates were built to stop. **And the C-1 hit is the instructive one: it is in the
discovery ledger, which is the register a null-prior sweep is most likely to omit.**

### 2.5 · Validity window

Every number in § 2.2 expires. `surface_census.md` is dated **2026-08-15** and says of itself
*"A photograph, not an invariant"*; `files/fulltext/` is gitignored, so the corpus differs per
checkout — **this worktree holds 13 top-level entries, the shared checkout 174**; and
`reading_state.md` is true of one checkout only. **The screen must be re-run at the pin, in the
shared checkout, at selection time.**

> **A sweep note that will otherwise cost a false negative.** An all-refs check written in zsh as
> `git show "$r:path"` applies the `:r` history modifier, strips the extension, and returns ABSENT
> on every ref. Always `${r}:path`, and always run a positive control against a ref where the file
> is known to exist. Every all-refs result in this record was produced with
> `git ls-tree -r --name-only "$r"` and a positive control (§ 5.4).

---

## 3 · SCIENTIST A AND SCIENTIST B

### 3.1 · Identical inputs, and how identity is *proved* rather than asserted

| Input | Carrier | Proof |
|---|---|---|
| the paper packet | `source_files` | SHA-256 per file, equal across both surfaces; `verify` enforces parity |
| the pinned corpus | `CORPUS_PIN` | commit SHA **plus** recursive `files/fulltext` tree digest (§ 0.3); both re-derived at completion |
| the discipline set | `common_files` | `epistemic_discipline` · `gold_is_in_the_details` · `fulltext_read_receipt` · `scientist_reading_modes` · `failure_taxonomy` — byte-identical, unaltered by this being a pilot |
| the output schema | `common_files` | one shape, or there is no comparison |

Exactly **two** files differ between the surfaces: `ASSIGNMENT.md` and the mode directive. That
is the benchmark's own configuration and the pilot does not widen it.

### 3.2 · Scientist A — independent evidence reconstruction

```
ROLE     reconstruct what the paper establishes, from the paper
INPUT    the frozen packet, the discipline set, MODE A directive. Nothing else in stage 1.
OUTPUT   observations (free of conclusion verbs) · methods · results · limitations
         (authors' and reader's, distinguished) · claim candidates, each typed
         · locators, each anchored to a unit of the fixed population
```

**Every output field the dispatch names already has a carrier in `OUTPUT_SCHEMA.md`.** The pilot
creates no field. `Observation` free of conclusion verbs and `Author interpretation` marked as
theirs are both already dimensions in benchmark § 8.2 under EPISTEMIC DISCIPLINE.

### 3.3 · Scientist B — independent critical analysis

```
ROLE     interrogate what the paper assumes, omits, and could otherwise explain
INPUT    the same frozen packet, the same discipline set, MODE B directive.
         Same bytes. Different reasoning path. Not a different paper and not a later paper.
OUTPUT   assumptions (stated and unstated) · missing evidence · alternative explanations
         · negative and null findings carried · internal contradictions
         · panel-vs-text relations, with valid pointers
```

🔴 **The asymmetry that must be declared before the run, not discovered after it.** MODE B
produces an `OMISSION` class that MODE A structurally cannot, because MODE A is not asked what is
absent. **A comparison table that counts `OMISSION` entries per reader will therefore show B
"finding more" for a reason that has nothing to do with either reader.** This is `Q-5` in the
open-question set, owned by Mirror as a method question. Until it is answered, the pilot must
report `OMISSION` **outside** any A-vs-B column.

### 3.4 · Forbidden, each with its mechanism — and the honest limit

| Forbidden | Mechanism | Strength |
|---|---|---|
| A sees B's tree, or B sees A's, before both freeze | none — see § 4.5 | 🔴 `PROCEDURAL` only |
| either sees LEGEND's prior output about this paper | C-1 null-prior proof at the pin | **mechanical**, enumerable, re-provable |
| either opens the corpus during stage 1 | surface allowlist + `verify` content scan | mechanical for path access |
| either edits a frozen first pass | `post_freeze/` new dated file; original left frozen | mechanical after the fact |

**The limit `BENCH-AB-001` states about itself applies here unchanged and is not repaired by
anything in this design:** each reader can read the other's directive inside the common
`scientist_reading_modes.md`, and with one paper and one session per actor, session variance is
not separable from mode. **The pilot inherits both. Neither is a reason not to run it; both are
reasons not to report a mode difference as a finding.**

---

## 4 · FREEZE POINTS

> This is the section no prior record holds, and the reason this record exists.

### 4.1 · The dispatch's three, against the moments the pipeline actually has

The dispatch names `before reading`, `after reading`, `before comparison`. Once the read is staged
— and it must be staged, because a corpus that is present must be opened *after* the closed read
or anchoring is undetectable — `after reading` is **two** moments. The pipeline has four.

```
F0  INPUT FREEZE        before either reader opens anything
       object: the surface bytes + the evidence population + the corpus pin
F1  STAGE-1 FREEZE      on the closed read being declared complete, BEFORE the corpus opens
       object: the pre-corpus reading — the record that makes anchoring detectable
F2  STAGE-2 FREEZE      on the cross-query addendum being declared complete
       object: the addendum. It may not edit stage 1.
F3  JOIN BARRIER        before comparison begins
       object: NOT bytes — the PAIR. Neither reader's output may be visible to the other,
               and comparison may not start, until BOTH F2 receipts exist.
```

### 4.2 · What each freeze protects, and what its absence costs

| | Protects | If it is missing |
|---|---|---|
| **F0** | the **denominator** — units and panels fixed before anyone reads, so coverage cannot be redefined once the readings exist | every coverage number becomes unfalsifiable: a reader who covered less redefines the population |
| **F1** | the **detectability of anchoring** — a pre-corpus record exists, is digested, and cannot be revised | a reader who reads the model first and the paper second produces an indistinguishable artifact |
| **F2** | the **immutability of a first pass** — corrections are new dated files, never edits | retroactive editing becomes possible and leaves no trace |
| **F3** | the **independence of the second reader** | the second reading is contaminated, and the run measures one reading twice |

### 4.3 · 🔴 What the repository can actually hold — measured against the tool, not the prose

| Freeze | Instrument | Status |
|---|---|---|
| **F0** surface + population | `build` → `verify` → `population` → `freeze` (manifest) | ✅ **mechanised** |
| **F0** corpus pin | `tree-digest --path files/fulltext` | ✅ **available** — verified this session with a positive control (§ 0.3); needs a manifest field, not a tool |
| **F1** stage-1 | `freeze` | 🔴 **schema cannot express it** — § 4.4 |
| **F2** stage-2 | `freeze` | 🟡 **command works; the seat layout has no slot** — § 4.4 |
| **F3** join | — | 🔴 **no instrument exists** — § 4.5 |

### 4.4 · 🔴 The staged read has no state to freeze into, and no second slot to freeze to

Two distinct defects, both verified in source rather than inferred from the protocol text.

**One — the vocabulary.** `benchmark_input_surface.py` line 739:

```python
FIRST_PASS_STATES = ("COMPLETE_DECLARED_BY_ACTOR", "ABANDONED", "TIMED_OUT")
```

and `freeze --first-pass-state` is `choices=list(FIRST_PASS_STATES)`, defaulting to
`COMPLETE_DECLARED_BY_ACTOR`. **There is no value meaning *stage 1 complete, stage 2 pending*.**
A stage-1 freeze must therefore either declare `COMPLETE_DECLARED_BY_ACTOR` — which is false, and
false in the receipt that exists to be trusted — or not use the command, which forfeits the
identity check, the set-wise recomputation and the timestamp. **Neither is acceptable, and the
repair is one tuple entry plus one schema note, which is the smallest repair this record names.**

**Two — the layout.** Protocol § 6 prescribes exactly one receipt path per actor:

```
frozen/RECEIPT-scientist-a.json
frozen/RECEIPT-scientist-b.json
```

A staged read produces **two** receipts per actor. `freeze --out` takes an explicit path, so the
tool does not collide — **the seat layout does.** Writing both to the prescribed path silently
overwrites the stage-1 receipt with the stage-2 receipt, and the overwritten one is precisely the
record that made anchoring detectable. A layout decision is owed before any pilot runs.

### 4.5 · 🔴 The third freeze point is not a freeze, and it is the one with nothing behind it

The dispatch's `before comparison` names the rule the protocol states in § 7:

> *"Neither actor sees the other's first pass until **both** are frozen. Ordering: whichever
> finishes first is frozen first; the second is not shown the first until its own freeze is
> recorded."*

The protocol labels its own guarantee, and I reproduce the label rather than paraphrasing it:

```
GUARANTEE_PROVIDED:            none by mechanism — discipline only
FAILURE_MODE_STILL_POSSIBLE:   Plan reads or relays A's first pass to B before B freezes
DETECTION:                     the two receipts carry FREEZE_TIMESTAMP_UTC and SURFACE_COMMIT;
                               an inspection of B's commit history against A's freeze time
                               makes a violation VISIBLE AFTER THE FACT, never prevented
RECOVERY:                      the benchmark is void for the second reader; the outcome says so
```

**And the tool confirms the gap is structural, not an omission of prose.** `verify-freeze` is
strictly unary:

```
verify-freeze [-h] --receipt RECEIPT --surface SURFACE
```

One receipt, one surface. **There is no arity in which the pair is the object.** Nothing in the
repository can be asked the question *"are both frozen?"* and answer it.

🔴 **The conflict of interest this exposes is the sharpest structural finding of the section.**
Plan freezes both trees, holds both, and performs the comparison. **The party the barrier
constrains is the party that operates it, and the barrier it is trusted to keep is the only one
with no mechanism.** Three mitigations exist and none is a fix — they are ordered by cost:

1. **Declare it.** The outcome carries the `GUARANTEE_PROVIDED` block above, unedited. Zero cost;
   converts an invisible risk into a stated one. **Do this regardless of the other two.**
2. **Order the imports** so neither `first_pass/` import happens until both F2 receipts exist.
   Cheap; makes the violation require an extra deliberate act rather than a slip.
3. **Split the party** — the freeze operator is not the comparison author. This actually removes
   the conflict, and it costs an actor the pilot does not have (§ 5.3).

### 4.6 · The sequence, with the owner of each step

```
STEP  MOMENT                      OWNER    ACT                                    ARTIFACT
 1    F0                          Plan     build · verify · population · freeze   manifest + population
      F0 corpus                   Plan     tree-digest files/fulltext             CORPUS_PIN in manifest
 2    handover                    Plan     two surfaces, two assignments          —
 3    stage 1 · closed read       A, B     independent, corpus unreadable         first pass
 4    F1                          Plan     freeze on declaration, BEFORE reading  stage-1 receipt ×2
 5    stage 2 · cross-query       A, B     corpus opens at the pin                addendum
 6    F2                          Plan     freeze on declaration, BEFORE reading  stage-2 receipt ×2
 7    F3 · join                   Plan     both F2 receipts exist                 🔴 no instrument
 8    comparison                  Plan     structural alignment only (§28)        matrix + disagreements
 9    corpus re-pin               Plan     tree-digest again; any delta declared  contamination note
```

**Steps 1, 4, 6, 7, 8 and 9 are all Plan.** That concentration is the § 4.5 finding restated as a
staffing fact, and it is the argument for mitigation 3 whenever a third party is available.

---

## 5 · MERGE

### 5.1 · 🔴 "Scientific synthesis" is not a free-standing output

Body § 27, verbatim:

> `INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED` con spiegazione è esito legittimo;
> **la sintesi forzata è un errore.**

The dispatch asks how the two outputs become a scientific synthesis. **Governance answers that
they mostly do not, and that making them is an error.** What synthesis legitimately means here is
narrow and mechanical:

- rows of the comparison matrix are aligned **by shared locator anchor** — same figure, table or
  section unit — **not** by Plan judging that two differently-worded claims mean the same thing.
  § 28: Plan *"NON risolve significato scientifico conteso."*
- where both readings anchor the same unit and their typed claims agree, the row is **convergent**
  and § 26 calls independent convergence *"segnale forte"*.
- where they do not, the row carries a **disagreement flag** and goes to
  `comparison/unresolved_disagreements.md` with both statements quoted and typed, and **stays
  unresolved there**.

**Synthesis is the residue of structural alignment, not a product Plan authors.** Any richer
synthesis is a scientific judgement, and § 28 routes it out of Plan entirely:
`INTEGRATION_BLOCK → Orchestrator → Scientist`.

### 5.2 · The three destinations, and what each is allowed to contain

| Output | Carrier | Author | Constraint |
|---|---|---|---|
| **convergent findings** | `comparison/comparison_matrix.md` | Plan | structural alignment only; agreement reported **descriptively**, never as a quality measure (§ 8.5) |
| **unresolved disagreement** | `comparison/unresolved_disagreements.md` | Plan | listed, typed, **not resolved**; both statements quoted verbatim |
| **the process question** | Mirror, at R4 | Mirror | *why* the two diverged — a method object, not the disagreement itself |

### 5.3 · 🔴 The third leg splits, and one half needs an actor the pilot does not have

The dispatch treats "Mirror input" as one destination. Governance splits it.

**§ 26** — *"Convergenza indipendente = segnale forte; divergenza → discussione → **R3** → Mirror
analizza il PERCHÉ."* **Annex C** confirms the routing table: *"disaccordo scientifico persistente
→ R3"*, and *"processo inferenziale methodology-changing → R4"*.

```
the disagreement itself   → R3 TRIADIC   → needs a THIRD Scientist
why they diverged         → R4 METHOD    → Mirror
```

**R3 is triadic.** Body § 32 makes A/B/C equivalent and says *"Scientist C da creare subito
(`lettore-c`), qualificato insieme ad A/B"* — and prior measurement records that C has no fixed
`ACTOR_ID` and no assigned function (`Q-4`, open). **A pilot run with exactly two Scientists can
therefore produce the one outcome § 27 explicitly protects and be unable to route it.**

**The resolution, and it is available today.** § 27 makes `DISAGREEMENT_UNRESOLVED` *an outcome*,
not a step. **The pilot terminates there.** R3 is a separate review, and Annex C is unambiguous
that *"Apertura solo via Orchestrator"* — the pilot could not open it in any case. **What the
design owes is the declaration**: the pilot ends at the unresolved disagreement and escalates
nothing, so that a reader of the outcome does not infer an escalation that was never authorized,
never staffed, and never opened.

### 5.4 · 🔴 Two carrier findings, one of which corrects a prior record

**`unresolved_disagreements.md` — the prior framing is wrong, and the true finding is different.**
`SCIENTIST-FIRST-REAL-PAPER-PILOT-001` reported the file as absent on every ref and read that as
*"the destination the design has been assuming does not exist."* The absence reproduces — I re-ran
the all-refs sweep with a positive control and the file is on **zero** refs — but the inference
does not. Protocol § 6 places it at `framework/eval/benchmarks/BENCH-AB-001/comparison/
unresolved_disagreements.md`: **it is a run artifact, written by Plan at step 8.** Its absence is
not a missing destination; it is the expected state of a directory no run has ever reached.

The sharper measurement is the seat itself. Of the eight directories § 6 prescribes, the seat
holds **two**:

```
PRESENT   benchmark_manifest.json · surface_spec.json · instructions/ (7 files) · population/ (1)
ABSENT    first_pass/ · frozen/ · comparison/ · audit/ · adjudication/ · outcome/
```

**The seat has its entire input half and none of its output half, which is exactly the shape of a
benchmark that was fully prepared and never handed over.** And because
`framework/eval/benchmarks/` is content domain, the pilot writing its comparison output there
moves the `CANDIDATE_CONTENT_HASH` of any candidate spanning the branch — the same disclosure
this record makes about itself in its front matter.

**Mirror's primary analysis surface does not exist.** § 29.3 [v3.1.1]: *"L'analisi primaria di
Mirror avviene sull'EVENT LEDGER consolidato (J.1), non leggendo le chat."* At this HEAD `ledger/`
holds `approvals/` (1 file), `checkpoints/` (1 dir), `retirements/` (1 file), `tasks/` (1 dir) —
**and no event ledger.** J.1 specifies the event shape and 23 minimum event types; none is being
written.

**Consequence for the merge, stated as a choice the operator owns.** Mirror can be handed the
frozen artifacts and the comparison matrix instead, and that is a usable R4 input — **but it is a
declared deviation from § 29.3, not the normal route**, and it should be recorded as one in the
outcome rather than passed off as compliance.

---

## 6 · SUCCESS CRITERIA

### 6.1 · Four conditions, each decided by a command and none of them "was the answer right"

| # | Criterion | Decided by | Pass condition |
|---|---|---|---|
| **S-1** | **REPRODUCIBILITY** | `verify-freeze` per receipt per surface; `tree-digest` re-run on the corpus | every receipt re-verifies set-wise (`ADDED`/`REMOVED`/`MODIFIED` all empty, **enumerated, never counted**); the corpus pin is unchanged, or the delta is declared as contamination |
| **S-2** | **EVIDENCE TRACEABILITY** | manifest `PASS` under `--verify-artifacts --require-current-schema`; locator validator; blind locator audit | every locator's artifact ∈ `ALLOWED_PATHS` with matching digest; every text snippet matches the surface exactly; figure attestations declared as such; every claim candidate anchors to ≥1 unit of the F0 population |
| **S-3** | **DISAGREEMENT PRESERVATION** | inspection of the comparison outputs | every disagreement-flagged row appears in `unresolved_disagreements.md` with **both** statements quoted and typed; **zero rows resolved by Plan**; `INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED` is recorded as an outcome, not as a failure |
| **S-4** | **INDEPENDENCE HELD** | the two F2 receipts' `FREEZE_TIMESTAMP_UTC` and `SURFACE_COMMIT`, inspected against each other | no commit in the later reader's surface history falls after the earlier reader's freeze in a way that indicates exposure. 🔴 **Detection only** (§ 4.5) — a pass here is an absence of evidence, not evidence of absence, and must be reported in those words |

### 6.2 · Explicit non-criteria — written down so they cannot be smuggled back in

```
NOT  "the reading reached the correct answer"     — the pilot has no oracle, and inventing one
                                                     would make the pipeline's output its own judge
NOT  a commit                                     — BATCH_COMMIT is Orchestrator's under an ACTIVE
                                                     lease; a pilot that must commit creates
                                                     pressure to commit
NOT  A scored against B                           — §32, and §8.5 already refuses it
NOT  agreement between A and B                    — two readers agreeing on an overshoot is
                                                     two overshoots
NOT  speed, tokens, output volume                 — recorded apart (§8.4), never a quality proxy
NOT  the number of claims produced                — a reading that carries three well-anchored
                                                     claims beats one that carries twelve unanchored
```

### 6.3 · What makes the pilot a failure

Failure is not "no claim was produced". Failure is any state in which **the output cannot be
attributed, resumed, reviewed or landed**:

- a receipt that does not re-verify, or a corpus pin that moved undeclared and unnoticed;
- a locator that cannot be resolved against the frozen surface;
- a disagreement that was resolved by Plan rather than recorded;
- a stage-1 record that was overwritten by stage 2 (§ 4.4);
- an independence violation discovered after the fact — for which the recorded recovery is that
  **the run is void for the second reader**, and the outcome must say so.

### 6.4 · 🔴 The pilot's own falsifier

Stated so the pilot can fail honestly rather than be declared a success by its own author:

> **If both readings, independently produced, prove to be individually traceable and mutually
> incomparable — because they anchored disjoint units of the population and no matrix row has
> entries in both columns — then the pipeline produced two artifacts and no experiment.**

The instrument is the F0 population: coverage per reader, and the size of the intersection. **A
zero intersection is a pipeline failure even though every S-1 and S-2 check passes**, and no
success criterion above would otherwise catch it.

---

## 7 · THE FINAL QUESTION

> *"What is the smallest real scientific experiment that can prove LEGEND works?"*

### 7.1 · The question needs one correction before it can be answered

**No experiment can prove that LEGEND works, and an experiment designed to do so is not an
experiment.** "Works" is not falsifiable; it names an aspiration, and an aspiration is confirmed
by any evidence the aspirant is willing to accept. The smallest *real* experiment is the one that
states a proposition that could come back false, and then runs the procedure that could return
it. So, restated with the smallest change that makes it answerable:

> **What is the smallest experiment whose failure LEGEND could not explain away?**

### 7.2 · The answer

> **One paper with a proved null prior, read independently by two actors from byte-identical
> frozen surfaces, each declaring completion into its own freeze, compared only where their
> locators anchor the same unit of a population fixed before either read — and ending at a
> commit candidate that is not committed.**
>
> **The falsifiable proposition it tests is not about the paper. It is: *two independent readings
> of the same frozen evidence, under this discipline, produce artifacts that a third party can
> re-derive, align, and disagree with.*** Failure looks like: receipts that do not re-verify,
> locators that do not resolve, or two readings with nothing in common to compare (§ 6.4).

### 7.3 · What is smaller than the current design — and what is not

**Three things the design carries can be dropped without making the experiment unreal:**

| Droppable | Why it is not load-bearing |
|---|---|
| **stage 2 / cross-query** | it exercises the corpus-contradiction half. Dropping it costs a *kind of output*, not the experiment's validity — and it removes the F1/F2 problem entirely (§ 4.4), which is the largest unbuilt piece in this record |
| **a third Scientist** | R3 is out of scope by § 5.3; the pilot terminates at `DISAGREEMENT_UNRESOLVED` |
| **the commit candidate** | the pipeline is proved by *candidate proposed*; proposing is the last act inside the pilot's authority anyway |

**Four things cannot be dropped, and each has a named reason:**

```
F0 with a fixed population   without it, coverage is unfalsifiable and every number is
                             renegotiable after the fact
two independent readers      one reader is not an experiment about independence
per-reader freezes           without them nothing is re-derivable and S-1 is unanswerable
the null-prior proof         without it the readers may be reading LEGEND's own prior output
                             back to itself, which is the one failure that would look
                             exactly like success
```

**The minimum is therefore: one paper · two readers · one closed stage · two freezes · one
comparison · no commit.** That is strictly smaller than the pilot in §§ 2–6, and it is real.

### 7.4 · 🔴 The finding I would put above the design

**The smallest real experiment is not blocked by the tooling.** F0 is mechanised, the corpus pin
is computable today (§ 0.3), the freeze command works, and dropping stage 2 removes the two
freeze defects in § 4.4. **What the smallest experiment lacks is a paper.**

The corpus was **174 top-level entries on the census date of 2026-08-15**. It is **174 today**,
2026-08-22. The unread structured pool is **12 papers**, of which **three have no readable body**
and the residue is predominantly oncology and review.

**Seven design records now exist about a first experiment that has no subject.** The sixth closed
with *"The sixth should not be a seventh; it should be a paper."* I have written the seventh
because it was dispatched and because § 4 was genuinely unheld — the three freeze points had never
been checked against the tool, and two of them do not survive the check. **That does not move the
verdict. The eighth should be a paper.**

---

## 8 · OPEN QUESTIONS

Recorded, not resolved. Numbering continues the prior records where the question is the same one;
`Q-16` through `Q-19` are new and arise from § 4 and § 5.

| # | Question | Owner |
|---|---|---|
| **Q-4** | what is `scientist-c`'s function, and when is its `ACTOR_ID` fixed? § 5.3 gives it a concrete one — R3 staffing — for the first time | operator + Orchestrator |
| **Q-5** | the `OMISSION` asymmetry — MODE B only (§ 3.3) | Mirror (method) |
| **Q-7** | which paper? The pool is empty of qualifiers; acquisition is required | operator/Orchestrator, on a metadata-only screen |
| **Q-10** | may a **declared partial** reading produce a commit candidate? | operator |
| **Q-16** | 🔴 **does `FIRST_PASS_STATES` gain a staged value, or is the staged read abandoned?** One tuple entry decides which. Until then a stage-1 freeze must record something false | **operator, on a Plan candidate** |
| **Q-17** | 🔴 what is the seat layout for **two** receipts per actor? § 6 prescribes one path and the second overwrites the first (§ 4.4) | **Plan candidate → operator** |
| **Q-18** | 🔴 who operates F3, given that the party the barrier constrains is the party that operates it (§ 4.5)? | **operator + Orchestrator** |
| **Q-19** | 🔴 is Mirror handed the event ledger J.1 (which does not exist) or the frozen artifacts (a declared deviation from § 29.3)? | **operator** |

---

## 9 · VALIDATION

### 9.1 · Constraint compliance — checked, not asserted

| Dispatch constraint | Status | Evidence |
|---|---|---|
| **no paper execution** | ✅ | no paper opened or read; the only file bytes touched were measured (`len()` of body/abstract), never read for content |
| **no Scientist activation** | ✅ | no actor created, spawned, contacted, assigned or qualified; no contract issued; no lease taken; `ACTIVE by derivation: 0` unchanged |
| **no paper selected** | ✅ | § 2.2 is a disqualification screen and states it is not a shortlist |
| all six requested sections defined | ✅ | §§ 2, 3.2, 3.3, 4, 5, 6 |
| the final question answered | ✅ | § 7, with the restatement it required in § 7.1 |
| one real saveable `.md` file | ✅ | `file_generation_rule` § 0.1 |

### 9.2 · What this record does NOT do

It does **not** select a paper · create, activate, qualify or contact any Scientist · write to
`framework/`, `governance/`, `roles/`, `ledger/`, `runtime/` or `disease-models/` · build, verify
or freeze any surface · open a candidate or a review · take a lease · create any schema, field or
vocabulary in a normative file · authorize `FIRST_PASS_STATES` to change (it names the change as
`Q-16` and leaves it to a candidate) · commit anything to the disease model.

### 9.3 · The prior claim this record contradicts

`SCIENTIST-FIRST-REAL-PAPER-PILOT-001` header finding 3 — *"the destination the design has been
assuming does not exist"* — is **misframed**. The absence reproduces exactly; the inference does
not. `unresolved_disagreements.md` is a run artifact of protocol step 8, and its absence is the
expected state of a benchmark that has never been handed over. The correct finding is the one in
§ 5.4: **the seat holds its whole input half and none of its output half.**

### 9.4 · Negative claims — each with the instrument and how long it holds

| Claim | Instrument | Holds until |
|---|---|---|
| no `unresolved_disagreements` on any ref | `git ls-tree -r --name-only` over all `refs/heads` + `refs/remotes`, with a positive control on `CLAUDE.md` | any ref adds it |
| no event ledger under `ledger/` | directory enumeration, 4 subdirectories, all inspected | J.1 is materialized |
| no staged value in `FIRST_PASS_STATES` | source read at line 739 + `--help` `choices` | the tuple changes |
| `verify-freeze` cannot express a pair | `--help` arity: `--receipt` ×1, `--surface` ×1 | the CLI changes |
| corpus unchanged since the census date | 174 top-level entries then and now; digest `825fc4a9d8415b0e` recorded in the census, recursive pin `b48694a1…` computed today | the next acquisition |

---

## 10 · NEXT_TRANSITION

Nothing in this record authorizes a next step. The three that are unblocked today, in the order
their duration argues for:

1. **Acquire a candidate paper.** Longest lead, blocked by no approval, and the one precondition
   seven records have not advanced (`Q-7`). `find-fulltext` is the existing route.
2. **Decide `Q-16` and `Q-17`** — one tuple entry and one layout line. Together they are the whole
   difference between a staged read that can be frozen and one that cannot. **Or drop stage 2
   (§ 7.3) and both questions disappear.**
3. **Decide `Q-19`** — what Mirror is handed, and whether the deviation from § 29.3 is declared.

`Q-18` is not on that list because it is a staffing question, and staffing is blocked upstream.
