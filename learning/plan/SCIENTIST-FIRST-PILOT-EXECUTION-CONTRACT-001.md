---
artifact: FIRST PILOT EXECUTION CONTRACT — the benchmark made dispatchable, and the two acts no instrument performs
record_id: SCIENTIST-FIRST-PILOT-EXECUTION-CONTRACT-001
task_id: SCIENTIST_FIRST_PILOT_EXECUTION_CONTRACT_v1
author: plan
authored_on: 2026-08-22
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)

STATUS: READ_ONLY_ANALYSIS · EXECUTION CONTRACT PROPOSAL
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - EXECUTION CONTRACT PROPOSAL
  - NOT GOVERNANCE
  - NOT A PROTOCOL
  - NOT A DECISION
  - NOT EXECUTION AUTHORIZATION
  - NOT A TASK CONTRACT — §9 proposes the shape of two; it issues neither
  - NOT A PAPER SELECTION — §1.6 analyses a selection the benchmark already made and does not ratify it
  - NOT A SCIENTIST ACTIVATION
  - NOT AN AGENT DEFINITION

naming_note: >
  Named as the dispatch named it. Not a Session Learning Record (Annex E.6), not a handoff, and
  it takes no `SLR` number it has not earned — the precedent of the seven non-SLR records already
  in this seat.

domain: >
  CONTENT — verified this session. `governance/plan_defined_parameters.md` § P5.1 declares
  `CONTROL_PLANE_ROOTS` exhaustively as `governance/candidates/`, `ledger/`, `reviews/`, and
  *"everything not under a declared root is content"*. `learning/` is under none of them, so this
  file sits inside the `CANDIDATE_CONTENT_HASH` of any future candidate spanning this branch and
  moves it. Disclosed.

relation_to_prior_work: >
  Seven Scientist records precede this one. This record does not restate their designs. It does
  one thing none of them does: it converts `BENCH-AB-001` into a form an Orchestrator could
  dispatch — concrete fields, concrete commands, concrete exit conditions — and then measures
  what stops the dispatch. Three of its findings contradict or narrow a prior record, and each is
  measured here rather than transferred (§ 11.3).

verdict_transfer: >
  NONE. Every number below was produced by a command run in this session at the HEAD named in
  § 0.2, and the command is shown beside it. Where a prior record reached the same number I say
  so; where my measurement contradicts one I give both numbers.
---

# FIRST PILOT EXECUTION CONTRACT — 001

> **The five findings that shape this record.**
>
> **1 · The dispatch's freeze model is the benchmark's own, and it is the first one the tool can
> already express.** `FIRST-WWOX-PAPER-PILOT-DESIGN-001` § 4.4 named two unbuilt pieces —
> `FIRST_PASS_STATES` has no *stage 1 done, stage 2 pending* value, and § 6 prescribes one receipt
> path per actor where a staged read needs two. **Both defects are properties of the staged read,
> and this dispatch drops it.** F0 · F1 · F2 · F3 as dispatched are a single-stage model;
> `BENCH-AB-001` is single-stage by construction — its surface contains no corpus, so there is no
> cross-query to stage. `Q-16` and `Q-17` do not arise under this contract. They are not solved;
> they are **out of scope**, and that is worth more than a solution.
>
> **2 · 🔴 Naming F1 "after Scientist A" fixes an ordering the protocol refuses to fix.**
> Protocol § 7: *"whichever finishes first is frozen first; the second is not shown the first
> until its own freeze is recorded."* A contract that indexes freezes by actor either idles B
> until A declares, or makes B's completion timing a function of A's — **and a schedule
> conditioned on the other reader is a channel, thin but real.** § 5 indexes the two freezes by
> **declaration order** and records the actor as a field.
>
> **3 · 🔴 The `verify` prior-output check is a function of a stale `BASE_HEAD`, and its coverage
> has narrowed without anything detecting it.** The spec's 23 forbidden paths derive from
> `cbce3016`, where the recorded command yields **20** today (the note beside it says 21). At this
> HEAD the same command yields **38**, of which **10 outside the seat are not on the list** and at
> least five are prior LEGEND output about the paper. The check still passes; it passes over less.
>
> **4 · 🔴 The paper the whole programme says it lacks has been selected, acquired and specified
> since 2026-08-18 — and it fails the gate a later record invented.** `BENCH-AB-001` names
> `PMID 42397075`; its packet is in the shared corpus today; its population is enumerated at
> **65 units / 109 panels**. It fails `C-1 NULL PRIOR` by **29** tracked paths. **That is not a
> disqualification, because null prior and surface allowlisting are two independent routes to the
> same guarantee and the benchmark implements the second** — § 2.1 of the protocol argues exactly
> this and argues it first. The two routes are not equally strong (§ 4.4), and the choice is the
> operator's. **But "there is no paper" is not true of this experiment, and seven records have
> carried it.**
>
> **5 · 🔴 The answer to the final question is yes for prompts and no for the pilot, and prompts
> were never the constraint.** Three of the seven instruction files carry **zero** paper
> identifiers and transfer to any paper unchanged; the other four are already written for this
> paper. Nothing needs authoring to run *this* pilot. What blocks it is that **the repository
> contains no instrument that delivers anything to an actor** — measured: zero across
> `framework/scripts/`, `governance/scripts/`, `scripts/` — that **0 leases are ACTIVE**, and
> that five of the nine sequence steps belong to Plan, not Orchestrator (§ 8).

---

## TASK_STATUS

```
TASK_ID          SCIENTIST_FIRST_PILOT_EXECUTION_CONTRACT_v1
MODE             READ_ONLY ANALYSIS + EXECUTION CONTRACT PROPOSAL · no Scientist activation ·
                 no paper read · no execution · no actor created · no contract issued ·
                 no lease taken · no surface built · no freeze run
STATE            COMPLETE — the seven requested sections are defined and the final question is
                 answered in § 8. Every answer that could be measured was measured; every answer
                 that is a design choice is marked as a proposal with the party who owns it.

EXECUTED         controlled_benchmark_ab.md §0–§10 read in full · MODE_A.md and MODE_B.md read in
                 full · OUTPUT_SCHEMA.md · ASSIGNMENT.scientist-a.md · BENCHMARK_INSTRUCTIONS.md ·
                 Annex A.1–A.7 · Annex C.1–C.4 · Annex J.0–J.3 · roles/orchestrator.md ·
                 roles/scientist.md frontmatter · DEC-20260822 (via `git show main:`) ·
                 24 executable measurements (git identity · lease derivation · scientist
                 fingerprint · corpus pin by tree-digest · population and manifest and spec
                 digests · manifest `_state` and null-field parse · per-file identifier counts
                 over all 7 instruction files · forbidden-path derivation recomputed at three
                 refs and set-differenced against the spec · all-refs sweep with positive control ·
                 seat directory enumeration · ledger/tasks enumeration · 5-worktree survey ·
                 delivery-instrument sweep over three script roots · CLI arity of all 7
                 subcommands · cmd_build source read)
NOT EXECUTED     no Scientist created, spawned, contacted, assigned or activated · no paper
                 opened or read · no surface built, verified or frozen · no candidate opened ·
                 no Task Contract written · no lease taken · no path under governance/ roles/
                 framework/ ledger/ runtime/ disease-models/ modified · no schema, field or
                 vocabulary created in any normative file
FILES ADDED      exactly one — this file
```

---

## 0 · IDENTITY AND PIN

### 0.1 · Why a contract needs a pin before it needs clauses

Every clause below is a claim about a state. `files/fulltext/` is gitignored, so the commit SHA
does not cover the evidence bytes, and two checkouts at the same SHA can hold different papers.
Both halves are recorded so that any clause can be re-derived or falsified.

### 0.2 · Measured, not inherited

| Field | Measured value | Command |
|---|---|---|
| branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `b72af2f25d42c3cafb781d42b66ef3a1761cdb66` | `git rev-parse HEAD` |
| worktree | `.claude/worktrees/evidence-index` | `git rev-parse --show-toplevel` |
| vs `main` (`788c357d…`) | 2 behind · 41 ahead | `git rev-list --left-right --count main...HEAD` |
| working tree | 3 untracked files, all prior records of this seat | `git status --porcelain` |
| lease | **`ACTIVE by derivation: 0`** — 5 leases, 2 STALE, 3 RELEASED | `framework/scripts/lease_state.py` |
| scientist fingerprint | `b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a` | `governance_fingerprint.py compose --role scientist` |

`CLAUDE.md` § 0: no ACTIVE lease and no runtime inventory ⇒ `BOOTSTRAP_MODE`. This session is not
Orchestrator, issues nothing, creates no actor and activates no Scientist. The single act it
performs — writing one file under `learning/plan/` on its own branch — traces to **H.1
`WORK_COMMIT`**, an annex, not a role contract. That distinction is load-bearing:
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (`main` `2bb2700`, read here via `git show main:`)
determines `roles/scientist.md`, `roles/plan.md`, `roles/orchestrator.md` and `roles/mirror.md`
to be **non-binding documents** requiring *"a new, explicit activation act"*.

### 0.3 · The pin the contract would freeze at F0

```
PIN  (candidate, this instant — NOT a selection and NOT a freeze)
  repository        main  788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
  corpus            <repo-root>/files/fulltext
                    b48694a13d07c691242d1dcbfcd592a77002ba1450ae2e97eee3cb69e27318da
                    654 file(s) recursive · 174 top-level entries
  spec              surface_spec.json          e7c2715b44a823ef19af3f7e803e622c81179c3c14944f059bc256f29df76c5b   spec_version 2
  manifest          benchmark_manifest.json    9f38991dc73cc118105849b446168a531c66828eb85825345a5b2867576caeda
  population        population/evidence_units.json
                    b41c7b9f432e48c74eb79be08b6d544f534aba9d0560063b1ee48f851e0b403a   65 units · 109 panels
```

🔴 **Two numbers routinely confused, and one of them cannot detect the failure it is used for.**
`surface_census.md` reports 174 entries — a top-level `ls`. The recursive file count is **654**,
because supplementary asset directories hang under paper entries. A pin taken as "174 files"
would not detect a supplement being added or swapped, and supplements are exactly where the
reading debt of this corpus has landed before. **The pin is the recursive digest.**

🔴 **The manifest is a template, and says so.** Its `_state` field reads *"PREPARED — NOT
FROZEN"*, `FROZEN_SHA256` is `null`, both `HANDOVER` blocks are `null`, and
`EVALUATION_POPULATION.sha256` holds the literal string `DERIVED_AT_BUILD` rather than the digest
`b41c7b9f…` I computed above. **That is not a defect — it is the honest state of an object whose
freeze is a build-time act nobody has performed.** It is also the precise reason F0 cannot be
described as *done*: the instrument is built, the artifact is not written.

---

## 1 · EXPERIMENT INPUT

### 1.1 · What the input is, as a set of objects rather than a description

The pilot's input is not "a paper". It is **five objects, each with a digest, each derivable by a
command**, and the contract is executable exactly to the degree that all five exist before
anyone reads.

| # | Object | Carrier | State today |
|---|---|---|---|
| I-1 | **the packet** — the article, its text surface, its supplements | `SOURCE_FILES[]` in the spec, 7 entries with per-file `sha256` and `bytes` | ✅ present in the shared corpus |
| I-2 | **the discipline set** | `COMMON_FILES[]`, 11 entries | ✅ present |
| I-3 | **the two per-actor files** | `PER_ACTOR_FILES`, exactly `ASSIGNMENT.md` and `benchmark/MODE_DIRECTIVE.md` | ✅ present |
| I-4 | **the evidence population** | `population/evidence_units.json`, 65 units / 109 panels | ✅ enumerated, digested |
| I-5 | **the pin** | § 0.3 — repository SHA + recursive corpus digest | 🔴 computable today; **no manifest field holds it** |

I-5 is the only gap in the input half, and it is a field in a manifest, not a tool. The command
that produces it (`tree-digest --path`) was verified against a known directory in a prior session
and re-run here.

### 1.2 · Paper requirements — mechanical, and each one disqualifying

Stated as predicates over metadata and bytes, never over meaning. **The screener is disqualified
from reading**: anyone who reads the paper to judge whether it qualifies has already spent the
blindness they were checking for. Plan may run this screen and only this screen — it is
structural, decides nothing about meaning, and is therefore inside body § 28.

| # | Requirement | Predicate | Instrument |
|---|---|---|---|
| **P-1** | **readable body** | the body is *substantially larger than its own abstract*. A relational test, not an existence test | direct measurement over the surface; `caption_census.py` for figures outside `<body>` |
| **P-2** | **countable primary population** | ≥1 enumerable evidence unit under a written spec. A review, editorial, correction or commentary carries none, cannot support a `DATO`, and cannot exercise the pipeline | `benchmark_input_surface.py population --spec … --source-root …` |
| **P-3** | **relevance** | title/abstract/MeSH from metadata only. Bridge and oncology literature yields `ESPANSIONE`, which cannot enter the current files as consolidated fact — the pilot would end with nothing to land | metadata |
| **P-4** | **no adjudication debt** | not retracted, not retraction-forward, no erratum entangled with an already-read paper, no unresolved preprint-vs-published ambiguity | metadata + ledger |
| **P-5** | **single ownership** | not being read right now in another checkout. `reading_state.md` says of itself *"This page is true of ONE checkout"* — a local check proves nothing about a reading in flight elsewhere | **all-refs** sweep, positive-controlled |
| **P-6** | **blindness route declared** | either `C-1 NULL PRIOR` (zero prior LEGEND output) **or** `SURFACE_ALLOWLIST` (§ 1.4). One of the two, named in the manifest, never neither and never silently | § 1.4 |

**P-1 is not a formality.** Of the twelve unread `structured` + `clean` papers in this corpus,
**three carry no readable body** — one has no `<body>` element at all, two have bodies of 258 and
308 characters. All three pass every existence check the census makes.

### 1.3 · Selection criteria — what the contract does and does not decide

`BENCH-AB-001` has already selected `PMID 42397075 · doi 10.1093/brain/awag239 · Brain 2026`, and
its packet is present:

```
files/fulltext/PMID42397075_Aqeilan2026.pdf                 3 341 414 bytes  b6b44816…
files/fulltext/PMID42397075_Aqeilan2026_fitz.txt            article_text
files/fulltext/PMID42397075_Aqeilan2026_assets/             5 supplements
```

**This record does not ratify that selection.** It measures it against the six requirements and
reports the one it fails, in § 1.6.

### 1.4 · Allowed sources — and the two routes to blindness, which are not equivalent

The reader's allowed source set is **the surface, and nothing else**. `ALLOWED_PATHS` is the
union of `COMMON_FILES`, `SOURCE_FILES`, `PER_ACTOR_FILES` and the empty output slots; `verify`
asserts `present ⊆ ALLOWED_PATHS` exhaustively.

Blindness — *the reader cannot reach LEGEND's prior conclusions about this paper* — has two
independent implementations, and the programme has been assuming only one of them exists.

| Route | Mechanism | Strength | Cost |
|---|---|---|---|
| **C-1 NULL PRIOR** | select a paper about which LEGEND has written nothing; prove it by an enumerated sweep at the pin | **absolute against every channel** — the prior output does not exist to be read, in the surface or out of it | requires acquisition; the corpus has produced no qualifier, and its unread residue is predominantly oncology and review |
| **SURFACE_ALLOWLIST** | build the surface from an allowlist into a **standalone repository** sharing no object store with LEGEND; nothing not listed is present | **absolute inside the surface; procedural outside it** — an absolute path still reaches the repository, and Annex J.0 grants no runtime permissions | available today; the repository holds **29** paths naming this paper |

🔴 **The protocol argues the second route first, and argues it against the first.** § 2.1:
*"the blinding problem is a property of the corpus, not of this paper, and choosing another WWOX
paper does not solve it, because every paper with verifiable provenance here is one this
repository has already worked."* That sentence is the whole argument for the allowlist, and it is
correct — but it establishes that the allowlist is **sufficient**, not that null prior is
**unnecessary**. The two claims differ, and the difference is the row above: under null prior,
leaving the surface finds nothing; under the allowlist, leaving the surface finds 29 files.

**The contract's requirement is therefore P-6: name the route in the manifest.** A run that names
neither is a run whose blindness claim has no referent.

### 1.5 · Forbidden previous context — enumerated, and the enumeration has decayed

`FORBIDDEN_PRIOR_OUTPUT_PATHS` is checked by `verify` **pre-handover with no exemption**, and
post-read with exactly one printed exemption (the blind spot, the path where the reader's own
manifest must land). Re-derived here at three refs with the spec's own recorded command:

| Ref | Paths naming the paper | Note |
|---|---:|---|
| `cbce3016` (the spec's `BASE_HEAD`) | **20** | the spec's derivation note says *"21 tracked paths"* |
| `main` `788c357` | **32** | |
| `HEAD` `b72af2f` | **38** | 29 outside the benchmark seat and the candidate directory |

Set-differenced against the spec's 23 listed entries:

```
listed but absent at BASE_HEAD    3 — claim_registry_current.md, working_model_current.md,
                                      controlled_benchmark_ab.md.  All three are DECLARED
                                      additions in the note; the list is 20 + 3 and is correct
present at BASE_HEAD, unlisted    0 — the derivation reproduces its own set exactly
at HEAD, outside the seat, unlisted  10
     governance/candidates/CAND-20260818-SCIENTIST-AB-SPEC.md    ← excluded by policy (wholesale)
     governance/candidates/HANDOFF-SCIENTIST-AB-SPEC.md          ← excluded by policy (wholesale)
     framework/scripts/benchmark_input_surface.py                ← names the paper as a fixture
     framework/scripts/test_benchmark_input_surface.py           ← same
     learning/plan/SCIENTIST-PIPELINE-READINESS-001.md
     learning/plan/SCIENTIST-PIPELINE-EXECUTION-MODEL-001.md
     learning/plan/SCIENTIST-BOOTSTRAP-CONTRACT-ANALYSIS-001.md
     learning/plan/SCIENTIST_RUNTIME_PROFILE-001.md
     learning/plan/SLR-plan-0003.md
     ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json
```

🔴 **Two findings, and the second is the one that matters.**

**One — an arithmetic slip in the derivation note.** The command yields 20 at the ref it names;
the note says 21; the list is 23 and decomposes as 20 + 3 declared additions. A ref's tree is
immutable, so the command is deterministic and the discrepancy is in the prose. Small, and owed.

**Two — the check's coverage is a function of `BASE_HEAD`, and `BASE_HEAD` is 41+ commits
stale.** Five to eight further paths carrying LEGEND's reasoning about this paper now exist and
are named by nothing. **The practical exposure is narrow** — `build` copies only the allowlist, so
an unlisted file cannot arrive in the surface by accident — **but that is precisely what the
forbidden check is for: catching a surface that was patched, or built from the wrong root.** Its
catch is now eight paths narrower and the `VERDICT: PASS` reads identically. **The repair is to
re-derive at the pin, at build time, and to record the command's output rather than a list
transcribed from an earlier run.**

### 1.6 · 🔴 The selected paper, measured against the six requirements

| # | Requirement | Verdict for `PMID 42397075` |
|---|---|---|
| P-1 | readable body | ✅ — 6 main figures, 7 results sections, 2 methods sections enumerated from the text and PDF |
| P-2 | countable primary population | ✅ — **65 units · 109 panels**, enumerated by command, digest `b41c7b9f…` |
| P-3 | relevance | ✅ — `Brain` 2026, primary, the group's own WWOX line |
| P-4 | no adjudication debt | ⚠️ accepted manuscript; a version-of-record check is owed at the pin |
| P-5 | single ownership | ⚠️ **not run here** — requires an all-refs + all-worktree sweep at selection time |
| P-6 | blindness route declared | 🔴 fails `C-1` by **29** paths; **satisfiable today by declaring `SURFACE_ALLOWLIST`** |

**The consequence, stated plainly and against seven records.** The programme's standing verdict —
*"the eighth should be a paper"* — was reached under a gate (`C-1 NULL PRIOR`) that
`FIRST-WWOX-PAPER-PILOT-DESIGN-001` introduced and that `BENCH-AB-001` never adopted. Under the
benchmark's own route the paper exists, is acquired, is specified, and its denominator is fixed.
**Acquisition is a precondition of the stronger blindness route, not of the experiment.** Which
route to run is the operator's call, and § 4.4 states what the weaker one costs.

### 1.7 · Population freeze — the one thing that must precede everything

`population/evidence_units.json` enumerates the paper's **structural** evidence units by declared
pattern. Structural enumeration is not a reading: it lists what the paper *contains*, not what it
*shows*, so Plan may do it under § 28.

```
FROZEN OBJECT   population/evidence_units.json
DIGEST          b41c7b9f432e48c74eb79be08b6d544f534aba9d0560063b1ee48f851e0b403a
CONTENT         65 units · 109 panels
                main_figure 6 · main_table 0 · main_results_section 7 · main_methods_section 2
                supplementary_figure 10 · supplement_methods_section 24
                supplement_table_section 7 · source_data_blot 9
DECLARED EMPTY  File008 (author contributions) — no figure, table, method or datum; outside the
                denominator because there is nothing in it to cover
```

**What the freeze buys:** every coverage number is computed over this set and nothing else, so a
reader who covered less cannot redefine the population afterwards. **`main_table: 0` is a
measured zero, not an omission** — the command refuses a spec in which a packet source is neither
enumerated nor declared empty.

**What it deliberately does not do:** it does not say which units *matter*. That is what the two
readings and the adjudication will disagree about, and pre-empting it would decide the experiment
before it runs.

---

## 2 · SCIENTIST A — `MODE A · PRIMARY_EVIDENCE_READ`

### 2.1 · Objective

> **Reconstruct what the paper establishes, from the paper — complete enough that a claim can be
> built on it and a second reader can attack it.**

The reading is not a summary and not a defence. `MODE_A.md`: *"'Read completely' is not 'read
charitably.' You are not defending the paper and you are not prosecuting it."*

### 2.2 · Allowed information — exhaustive

```
the packet                7 files, digested, byte-identical to B's
the discipline set        epistemic_discipline · gold_is_in_the_details · fulltext_read_receipt
                          scientist_reading_modes · failure_taxonomy — byte-identical to B's
roles/scientist.md        the actor's contract; its digest IS ROLE_CONTRACT_HASH
the validators            deepdive_manifest.py · corpus_firewall.py — unmodified
the output schema         OUTPUT_SCHEMA.md, one shape for both readers
ASSIGNMENT.md             identity, TASK_ID, MODE, PARALLEL_READ_GROUP        ← per-actor
MODE_DIRECTIVE.md         MODE_A.md content                                    ← per-actor, THE VARIABLE
renders it produces       page renders and figure crops it makes itself, in its own output slot
```

Renders are deliberately **not** supplied. A prior reader's crops encode which pages and which
panels that reader thought mattered; supplying them imposes parity of *attention* on top of
parity of *source*. Each reader renders what it needs, from the recipe in the instructions, and
lists its renders with digests as `source_artifacts`.

### 2.3 · Forbidden information — with the mechanism and its honest reach

| Forbidden | Mechanism | Reach |
|---|---|---|
| the other reader's output, identity, progress or existence beyond the group name | separate standalone repositories, no channel; Orchestrator relays no content — a `BLOCKER` is answered on the protocol, never on the paper | **structural** |
| LEGEND's prior output on this paper | `FORBIDDEN_PRIOR_OUTPUT_PATHS` absent from the surface; `CONTENT_SCAN` hits `== 0` over every non-exempt file | **mechanical inside the surface** — § 1.5 on its decay |
| any file outside the surface | `verify`: `present ⊆ ALLOWED_PATHS`; `locators`: every cited artifact ∈ `ALLOWED_PATHS` | 🔴 **the default path is blind; the departure is an act, not a wall** (J.0) |
| network retrieval | Plan performs the retraction/version check before handover, so no mandated step needs it | structural, at the cost of one pre-step |
| a research question, an evidence target, a hypothesis to test, an anticipated conclusion | absent from every input file **by design**, not by omission. H.1: *"Conclusione scientifica — Scientist responsabile … mai a ordine"* — which binds the dispatcher | governance |
| the evaluation population | Plan holds the denominator; it is not in the surface | a reader who knew it could optimize coverage against it |
| the pilot's own scoring design | § 7 is not in the surface | same reason |

🔴 **One exclusion the design cannot make, stated before it is discovered.** Both mode directives
are described in full inside `scientist_reading_modes.md`, which is a **common** file and could
not honestly be withheld from either reader. The manipulated variable is therefore not *knowledge
of the two modes*; it is **which directive is addressed to you**. The instruction *"do not
speculate about what the other directive says"* is about attention, not information.

### 2.4 · Expected artifact — four objects, no new data model

```
<SURFACE>/disease-models/wwox/research/deepdive_manifests/PMID42397075.json
      schema_version 2 · validated by deepdive_manifest.py in the surface
      verbatim_locators.entries[] — proposition · snippet · surface · artifact · anchor ·
      panel_text_relation · found_or_sought
<SURFACE>/disease-models/wwox/research/fulltext_dossiers/PMID42397075.md
      the human-readable twin; the two must not disagree
<SURFACE>/output/claim_candidates.md
      the canonical claim form + the seven benchmark fields + the Locators: cross-reference
<SURFACE>/output/receipt.json
      the reading's own receipt — receipt id BENCH-AB-001-<ACTOR_ID>-01, NOT a ledger id:
      this reading does not touch the receipt ledger
```

**Every field the dispatch asks MODE A to produce already has a carrier.** `Observation` free of
conclusion verbs and `Author interpretation` marked as the authors' are both existing fields.
**The pilot creates no schema, no field and no vocabulary.**

Several manifest sections — `multihop`, `corpus_crossquery`, `group_assessment` — ask about a
corpus this surface does not contain. **They are waived, and the waiver names the surface
boundary as the reason.** A waiver that says why is honest; a fabricated corpus query is not.

### 2.5 · Completion criteria — commands, not self-report

| # | Criterion | Decided by |
|---|---|---|
| A-1 | manifest validates | `deepdive_manifest.py --workspace . --pmid 42397075 --verify-artifacts --require-current-schema` → `VERDICT: PASS` |
| A-2 | every locator resolves inside the surface | `benchmark_input_surface.py locators --spec … --surface … --actor-id … --pmid …` — an outside citation is `BENCH_INVALID` **for that entry, recorded, never silently dropped** |
| A-3 | every claim candidate anchors to ≥1 locator entry | manifest inspection |
| A-4 | the coverage map carries **no `not_read`** over all nine sections — **or** a declared partial with an honest map | manifest inspection |
| A-5 | `verify --post-read` clean | parity, allowlist, forbidden paths, census |
| A-6 | the actor declares `TASK_COMPLETE` | Annex A.5 |

🔴 **A-4 carries an open question this contract cannot close.** Whether a **declared partial**
reading may produce a commit candidate is answered on no ref (`Q-10`). `BENCH-AB-001` permits it,
but its output was quarantined; with a real destination, *legitimate result* and *sufficient to
move the model* are different questions. **The contract's position: a declared partial completes
the reading and does not by itself authorize a candidate.** That is a proposal, and the operator
owns it.

🔴 **A reading declared complete without `verbatim_locators.entries[]` is not complete, and the
freeze does not repair it.** The freeze records what was in the tree; it does not confer the
depth that was not. Such a reading scores coverage and provenance on an empty locator set, and
the blind audit has no triple to audit — which is the measurable form of the same statement.

---

## 3 · SCIENTIST B — `MODE B · INDEPENDENT_CRITICAL_READ`

### 3.1 · Objective

> **Do the whole primary reading — the same completeness, the same outputs, the same discipline,
> nothing reduced — and in addition search explicitly for what the paper does not establish.**

🔴 **B is A plus a second full deliverable, and any plan that treats B as the cheaper seat has
mis-scoped the run.** `MODE_B.md`: *"This half is not abbreviated because you also have a second
half. A critical record over a thin reading is criticism without evidence."*

Two boundaries the directive draws itself, both worth restating in a dispatch:

- **B is a reader, not a reviewer of anyone.** It has not seen the other reading and will not
  during this pass. It is not adjudicating it, correcting it, or predicting it.
- **B is not Mirror.** Mirror reviews the *process*. B reviews *the paper's evidence and
  inferences*, with a Scientist's authority — subject to review, never to order.

### 3.2 · Allowed information

**Byte-identical to § 2.2, with one file different.** `MODE_DIRECTIVE.md` carries `MODE_B.md`
content. That is the entire declared variable, and `verify` reports a third differing file as a
finding.

### 3.3 · Forbidden information

**Identical to § 2.3, plus one clause specific to the mode**: *"attempt to reconstruct what the
other reader concluded"* is named as forbidden in `MODE_B.md` and not in `MODE_A.md` — because B
is the mode whose framing invites it.

### 3.4 · Expected artifact — the four of § 2.4, plus one

```
<SURFACE>/output/critical_reading.md      — eleven mandatory axes, each answered
```

```
CONTRADICTORY_EVIDENCE   NEGATIVE_EVIDENCE   OVERCLAIM   UNSUPPORTED_INFERENCE
MODEL_DEPENDENCE   RESULT_VS_INTERPRETATION   METHODS_STATISTICS
ALTERNATIVE_EXPLANATION   CONTEXT_COLLAPSE   OMISSION   UNSUPPORTED_MECHANISTIC_LEAP
```

**An axis with no finding carries `"searched; none found"` and says *what was searched*,
concretely.** Silence on an axis is an incomplete reading, not a clean paper.

### 3.5 · Completion criteria

**A-1 through A-6 of § 2.5, unchanged, plus:**

| # | Criterion | Decided by |
|---|---|---|
| B-7 | all eleven axes present and answered — findings anchored, or `searched; none found` **with what was searched** | inspection of `critical_reading.md` |
| B-8 | every critical entry anchored to a locator and typed | *"A criticism is a claim and carries the same burden."* `"The n is too small"` without the n, the test and the sentence is not a finding |
| B-9 | undershoot reported where found | *"If the paper supports more than it claims, say that."* A narrowing nobody challenges becomes a permanent false negative |

🔴 **The asymmetry that must be declared before the run, not discovered after it.** MODE B
produces an `OMISSION` class that MODE A structurally cannot, because MODE A is never asked what
is absent. **A comparison table counting `OMISSION` entries per reader will show B "finding more"
for a reason that has nothing to do with either reader.** Until `Q-5` is answered, `OMISSION` is
reported **outside** any A-vs-B column.

---

## 4 · CONTAMINATION CONTROL

> The question the dispatch asks — *how do we prove Scientist B was not influenced by Scientist
> A?* — has an answer, and the answer is that **we cannot prove it.** What follows is what can be
> proved, what can only be detected, and what rests on discipline alone. The three are kept
> apart because merging them is how a procedural rule acquires mechanical vocabulary.

### 4.1 · Mechanical guarantees — each a command, each falsifiable by anyone

| # | Guarantee | Command | What it actually proves |
|---|---|---|---|
| M-1 | both read the same bytes | `verify` — `sha256_A == sha256_B` per path, recomputed from disk | parity **at verification time**, not a claim about how files were copied |
| M-2 | exactly two files differ | `verify` — `PER_ACTOR_FILES` present and asserted **different**; a third differing file is a finding | the variable is one, and a broken benchmark is reported rather than assumed away |
| M-3 | no prior LEGEND output in either surface | `verify` — every `FORBIDDEN_PRIOR_OUTPUT_PATHS` entry absent, **no exemption pre-handover** | absence of the listed paths. § 1.5: the list has decayed |
| M-4 | no paper identifier outside the packet | `verify` — `CONTENT_SCAN` hits `== 0`, with `SCANNED` and `[UNCHECKED]` **partitioning** the present files | no file is skipped without being printed by name, in **either** verify mode |
| M-5 | nothing present outside the allowlist | `verify` — `present ⊆ ALLOWED_PATHS`, exhaustive | the surface content is a function of the spec |
| M-6 | no object-store path back to LEGEND | each surface is a **standalone `git init`**, sharing no object store | `git show main:<prior output>` **fails**; in a worktree it is one command |
| M-7 | output slots empty at handover | `verify` — a file in a slot is `NOT EMPTY` | the reader started from nothing |
| M-8 | the frozen tree is what was frozen | `freeze` → `TREE_SHA256`, `FILE_COUNT`, `FILES[]`; `verify-freeze` recomputes **set-wise** — `ADDED`/`REMOVED`/`MODIFIED` enumerated | 🔴 set-wise, **never by count**: two trees of equal file count holding different files is exactly the substitution this exists to catch |
| M-9 | the receipt belongs to this tree | `freeze` reads `ACTOR_ID`/`BENCHMARK_ID` from `ASSIGNMENT.md` **inside the tree**; a command-line disagreement **refuses, exit 2** | A's tree cannot be frozen as `scientist-b` |
| M-10 | no frozen byte lives outside the tree | `freeze` **refuses** a tree containing a symlink | a link's bytes are not in the receipt |
| M-11 | an out-of-surface source that was **used and cited** is visible | `locators` — artifact ∉ `ALLOWED_PATHS` → `BENCH_INVALID` for that entry | 🔴 blind to an out-of-surface source used and **not** cited |

**What M-1…M-11 jointly prove: B's surface never contained A's output, and B's tree at freeze is
exactly what the receipt says.** They do not prove B was never *told*.

### 4.2 · 🔴 Detection-only signals — the class the dispatch's binary split omits

These are neither guarantees nor discipline. They make a violation **visible after the fact** and
prevent nothing. Reporting them as guarantees is the specific error Annex J.0 forbids.

| # | Signal | Instrument | What a clean result means |
|---|---|---|---|
| D-1 | freeze ordering | both receipts carry `FREEZE_TIMESTAMP_UTC` | if the second freeze precedes the first, the ordering rule was not followed |
| D-2 | surface commit history | each receipt carries `SURFACE_COMMIT`, `SURFACE_BRANCH`, `SURFACE_DIRTY`; each surface is its own repo with authored commits | 🔴 **a real but narrow bound**: if the later reader's last commit precedes the earlier reader's freeze, the later *tree* cannot contain post-freeze content. It bounds the artifact, never the reader's knowledge |
| D-3 | session memory scope | Plan checks the surface path carries no accumulated auto-memory **before** handover, and records the check | *"a favourable accident of the deployment, not a guarantee"* |
| D-4 | locator containment | § 4.1 M-11 | a clean result is consistent with an uncited out-of-surface read |

**Every D-row's clean result is an absence of evidence and must be reported in those words.**

### 4.3 · Discipline-based guarantees — named, with the failure each leaves open

| # | Rests on | Failure still possible | Trace it would leave |
|---|---|---|---|
| G-1 | 🔴 **Plan not relaying A's content to B before B freezes** | Plan reads or relays A's first pass to B | **none in any artifact this protocol produces** |
| G-2 | neither reader reading outside its surface by absolute path | a reader reads the repository and does not cite it | none, unless cited (M-11) |
| G-3 | Orchestrator answering a `BLOCKER` on the protocol, never on the paper | a substantive answer about the paper | the message, if messages are durable |
| G-4 | neither reader speculating about the other's directive | both directives are in a common file | none |
| G-5 | model training knowledge of the paper | uncontrollable by any route | covered by `DEFAULT_FROM_TEXTBOOK` and by MODE B's `OMISSION` axis run on both |

### 4.4 · 🔴 The conflict of interest, and the three mitigations ordered by cost

**Plan freezes both trees, holds both, and performs the comparison. The party the barrier
constrains is the party that operates it, and the barrier it is trusted to keep is the only one
with no mechanism.** The protocol labels its own guarantee and this contract reproduces the label
rather than paraphrasing it:

```
GUARANTEE_PROVIDED:            none by mechanism — discipline only
FAILURE_MODE_STILL_POSSIBLE:   Plan reads or relays A's first pass to B before B freezes
DETECTION:                     FREEZE_TIMESTAMP_UTC + SURFACE_COMMIT, inspected against each
                               other — VISIBLE AFTER THE FACT, never prevented
RECOVERY:                      the run is void for the second reader; the outcome says so
```

And the tool confirms the gap is structural rather than an omission of prose: `verify-freeze` is
**strictly unary** — `--receipt` ×1, `--surface` ×1. **There is no arity in which the pair is the
object.** Nothing in this repository can be asked *"are both frozen?"* and answer it.

| # | Mitigation | Cost | Effect |
|---|---|---|---|
| **1** | **Declare it.** The outcome carries the block above, unedited | zero | converts an invisible risk into a stated one. **Do this regardless of the other two** |
| **2** | **Write the join as an artifact** — `frozen/JOIN-BARRIER.md`, carrying both `TREE_SHA256`, both `FREEZE_TIMESTAMP_UTC`, and Plan's dated declaration that no content of either tree was read before the later timestamp. Order the imports so neither `first_pass/` import happens until both receipts exist | one file, no tool change | makes the violation require **a false statement in a durable artifact** rather than a silence. Still not a proof |
| **3** | **Split the party** — the freeze operator is not the comparison author | an actor the pilot does not have | **actually removes the conflict** |

**Mitigation 2 is the contract's proposal and is the largest available improvement that costs
nothing.** It is a Plan work artifact, not a schema and not a tool change.

### 4.5 · The answer to the dispatch's question, stated without softening

> **We can prove that B's surface never contained A's output, that B read the same bytes as A,
> and that B's frozen tree is exactly what was frozen. We cannot prove B was not influenced by
> A. What the design achieves is that any influence requires a deliberate act by a named party,
> and that three of the four channels leave a trace. The fourth — Plan relaying — leaves none,
> and the party it constrains is the party that operates it.**

---

## 5 · FREEZE MODEL

### 5.1 · Four moments, and why this is the model the tool can express

The dispatch names four. Under the **single-stage** read they map one-to-one onto acts the
existing commands perform.

```
F0  INPUT FREEZE      before either reader opens anything
                      object: the surface bytes · the evidence population · the pin
F1  FIRST FREEZE      on the FIRST completion declaration, before its content is read
                      object: that reader's whole tree
F2  SECOND FREEZE     on the SECOND completion declaration, before its content is read
                      object: that reader's whole tree
F3  JOIN BARRIER      before comparison begins
                      object: NOT bytes — the PAIR
```

🔴 **F1 and F2 are indexed by declaration order, not by actor.** The dispatch names them "after
Scientist A" and "after Scientist B"; the protocol says *"whichever finishes first is frozen
first."* Indexing by actor would either idle B until A declares, or make B's completion timing a
function of A's — **and a schedule conditioned on the other reader is a channel, thin but real.**
The actor is recorded as a field of each freeze, never as its name.

🔴 **And the two defects the prior record named do not arise here.**
`FIRST_PASS_STATES` (line 739: `COMPLETE_DECLARED_BY_ACTOR · ABANDONED · TIMED_OUT`) has no value
meaning *stage 1 done, stage 2 pending* — but under a single-stage read no such state exists.
Protocol § 6 prescribes one receipt path per actor — which is exactly one per actor here.
**`Q-16` and `Q-17` are properties of the staged read, and this contract does not stage.**

### 5.2 · What each freeze holds, who performs it, how it is verified

| | **F0 · INPUT** | **F1 · FIRST** | **F2 · SECOND** | **F3 · JOIN** |
|---|---|---|---|---|
| **what is frozen** | both surface trees · `population/evidence_units.json` · the manifest (`FROZEN_SHA256` over every field but `HANDOVER`) · the pin | the first declaring reader's entire tree | the second declaring reader's entire tree | **nothing — it is a barrier, not bytes**: the assertion that both F-receipts exist and that neither tree was read before the later of them |
| **who freezes** | **Plan** | **Plan**, on the declaration, **before reading the content** | **Plan**, same rule | **Plan** — 🔴 § 4.4 |
| **command** | `build` → `verify` → `population` → `freeze` (manifest) → `tree-digest --path files/fulltext` | `freeze --surface … --actor-id … --benchmark-id … --spec … --input-manifest … --out frozen/RECEIPT-<ACTOR_ID>.json` | same | 🔴 **none exists** |
| **verified by** | `verify` exits 0 · manifest digest recorded in **each** receipt as `INPUT_MANIFEST_SHA256` · population digest in the manifest | `verify-freeze --receipt … --surface …` — set-wise, `ADDED`/`REMOVED`/`MODIFIED` **enumerated** · identity checked against the tree's own `ASSIGNMENT.md` | same | 🔴 mitigation 2 of § 4.4 — a declaration in a durable artifact |
| **what its absence costs** | every coverage number becomes unfalsifiable: a reader who covered less redefines the denominator | the first reading becomes editable after the fact and leaves no trace | the second reading becomes editable after the fact | the second reading is contaminated and the run measures one reading twice |
| **state today** | ✅ instrument built; 🔴 **artifact not written** — manifest `_state: PREPARED — NOT FROZEN`, `FROZEN_SHA256: null` | ✅ mechanised | ✅ mechanised | 🔴 **no instrument** |

### 5.3 · Immutability after freeze — the one rule that must not be quiet

A correction a reader wants to make after its freeze is a **new dated file** under
`first_pass/<ACTOR_ID>/post_freeze/`, referenced from the outcome, with the original left frozen.
**The comparison, the audit, the adjudication and the outcome never modify a first pass.**
Retroactive edits are the one thing this section exists to make impossible to do quietly.

### 5.4 · Sequence, with the owner of each step

```
STEP  MOMENT                OWNER          ACT                                        ARTIFACT
 0    preconditions         operator/Orch  P-1…P-7 of protocol §1, each by its route  lease · registry · L2
 1    F0                    Plan           build · verify · population · freeze       manifest + population
      F0 pin                Plan           tree-digest files/fulltext                 PIN in the manifest
 2    contracts             Orchestrator   two Task Contracts, one group              ledger/tasks/<ACTOR_ID>/
 3    handover              Plan           writer transfer; memory-scope check        HANDOVER block
 4    reading               A, B           blind, autonomous, in the surface          output tree + commits
 5    F1                    Plan           freeze on 1st declaration, before reading  receipt #1
 6    F2                    Plan           freeze on 2nd declaration, before reading  receipt #2
 7    F3 · join             Plan           both receipts exist; imports ordered       🔴 no instrument
 8    comparison            Plan           structural alignment only (§28)            matrix + disagreements
 9    audit                 blind agents   100% of triples, identity withheld         audit/
10    adjudication          Mirror         R4 · the process                           pointer + digest
11    outcome               Plan           every dimension separately, no composite   outcome/
12    re-pin                Plan           tree-digest again; any delta declared      contamination note
```

**Steps 1, 3, 5, 6, 7, 8, 11 and 12 are Plan's.** That concentration is § 4.4 restated as a
staffing fact, and it is the argument for mitigation 3 the moment a third party exists.

---

## 6 · OUTPUT ROUTING

### 6.1 · The destinations, separated by trigger and by timing

They are not alternatives. They fire at different moments, and two of them are unconditional.

| Path | Trigger | Receives | Authority | Timing |
|---|---|---|---|---|
| **Orchestrator** | **always** — every completion | the completion payload; assigns the Ladder level and opens every review | C.3 *"Apertura solo via Orchestrator"*; H.1 | **first, and not optional** |
| **Plan** | always | structural / provenance / schema integration; the comparison matrix aligned **by shared locator anchor** | H.1 structural integration; 🔴 **§ 28 — Plan `NON risolve significato scientifico conteso`** → `INTEGRATION_BLOCK → Orchestrator → Scientist` | after Orchestrator |
| **blind locator audit** | 🔴 **always, and it is not a Scientist** | only `(proposition, quote, anchor)` triples + the source artifact. No dossier, no conclusions, no reader identity | none — forms no scientific conclusion | per triple, **100 %**, never sampled |
| **peer Scientist review** | **conditional**, by C.1 floors: `inferenza L2 importante → R1`; `therapeutic-actionable → R2` | the claim + its locators + the packet — **not the other reading** | C.4 `INFERENCE → peer Scientist`; *"reviewer senza evidenza contribuita"* | routed by content, unknowable at design time |
| **R3 TRIADIC adjudication** | `disaccordo scientifico persistente`, after max 2 rounds | both statements, quoted and typed, plus both locator sets | a **turn**, never a post: `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`, rotation, *"mai coppie fisse"* | 🔴 **outside this pilot** — § 6.3 |
| **Mirror · R4 METHOD** | **floor** — a first end-to-end run is `processo inferenziale methodology-changing` on its face | both frozen readings, both receipts, timelines, surface verifications, the blindness-route proof, the pin and its re-digest, audit verdicts, every disagreement quoted and typed, contamination declarations | `SYSTEM → Mirror`; **not** the power to decide whether anything commits | **after both freezes**, never streaming |

### 6.2 · 🔴 "Scientific synthesis" is not a free-standing output

Body § 27, verbatim: `INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED` *con spiegazione è
esito legittimo;* **la sintesi forzata è un errore.**

What synthesis legitimately means here is narrow and mechanical:

- matrix rows are aligned **by shared locator anchor** — same figure, table or section unit — and
  **not** by Plan judging that two differently-worded claims mean the same thing;
- where both readings anchor the same unit and their typed claims agree, the row is **convergent**,
  and § 26 calls independent convergence *"segnale forte"*;
- where they do not, the row carries a **disagreement flag**, goes to
  `comparison/unresolved_disagreements.md` with both statements quoted and typed, and **stays
  unresolved there**.

**Synthesis is the residue of structural alignment, not a product Plan authors.** Anything richer
is a scientific judgement and § 28 routes it out of Plan entirely.

🔴 **Agreement is reported descriptively and is never a quality measure.** Two readers agreeing
on an overshoot is two overshoots.

### 6.3 · 🔴 The pilot terminates at unresolved disagreement, and escalates nothing

Governance splits what the dispatch treats as one destination:

```
the disagreement itself   → R3 TRIADIC   → needs a THIRD Scientist
why the two diverged      → R4 METHOD    → Mirror
```

`scientist-c` exists, is `REGISTERED_PENDING_L1_L2`, and holds the only two verified Scientist
capabilities in the repository — and no design gives it a function. Body § 32 says the three were
to be *"qualificato insieme"*. **A pilot run with exactly two Scientists can produce the one
outcome § 27 explicitly protects and be unable to route it.**

**The resolution is available today and costs nothing:** § 27 makes `DISAGREEMENT_UNRESOLVED` *an
outcome*, not a step. **The pilot ends there.** Annex C is unambiguous that a review opens only
via Orchestrator, so the pilot could not open R3 in any case. **What the contract owes is the
declaration** — so that a reader of the outcome does not infer an escalation that was never
authorized, never staffed and never opened.

### 6.4 · 🔴 Two carriers the routing needs, measured

| Object | Refs carrying it | Verdict |
|---|---:|---|
| `comparison/unresolved_disagreements.md` | **0 of 46** | it is a **run artifact of step 8**, written by Plan. Its absence is the expected state of a benchmark that has never been handed over — **not** a missing destination |
| `ledger/events/` (Mirror's primary R4 surface, § 29.3 / J.1) | **absent** | `ledger/` holds `approvals/`, `checkpoints/`, `retirements/`, `tasks/`. J.1 specifies 23 minimum event types; none is being written |

*(All-refs sweep over 46 `refs/heads` + `refs/remotes`, each with `git ls-tree -r --name-only
"${r}"` and a positive control: `CLAUDE.md` returns **46 of 46**. The braces are deliberate —
`"$r:path"` in zsh applies the `:r` history modifier and returns ABSENT on every ref.)*

**Consequence for Mirror, stated as a choice the operator owns:** Mirror can be handed the frozen
artifacts and the comparison matrix instead, and that is a usable R4 input — **but it is a
declared deviation from § 29.3, not the normal route, and it belongs in the outcome as one rather
than passed off as compliance.**

### 6.5 · The seat, measured

```
PRESENT   instructions/ (7 files) · population/ (1 file) · benchmark_manifest.json · surface_spec.json
ABSENT    first_pass/ · frozen/ · comparison/ · audit/ · adjudication/ · outcome/
```

**The seat holds its entire input half and none of its output half — exactly the shape of a
benchmark that was fully prepared and never handed over.**

---

## 7 · SUCCESS / FAILURE

**No score, no weighting, no threshold.** § 8.5 refuses a composite verdict. What follows is an
enumeration of four mutually exclusive outcome classes with a **precedence order**, because a
run can satisfy the predicates of more than one and the class it is reported as must not depend
on who reads the list first.

### 7.1 · 🔴 A name collision that must be disambiguated before anything else

`DISAGREEMENT_UNRESOLVED` (body § 27) is a **scientific** outcome and lives **inside**
`EXPERIMENT_VALID`. The outcome class `UNRESOLVED` below is a statement about **the experiment**.
A run in which A and B disagree about everything, preserved and quoted, is `EXPERIMENT_VALID`.
Conflating the two would report the pipeline's best-protected success as its failure.

### 7.2 · Precedence — evaluated top to bottom, first match wins

```
1  INFRASTRUCTURE_FAILURE     the run never reached the state it was designed to test
2  EXPERIMENT_INVALID         the run happened and a guarantee broke
3  UNRESOLVED                 the run held every guarantee and answers nothing
4  EXPERIMENT_VALID           everything else
```

**Infrastructure is checked first** because a run that never started says nothing about the
method, and reporting it as an invalidation would blame the design for a tool.

### 7.3 · `INFRASTRUCTURE_FAILURE` — the run did not reach the test

Any one of these, all upstream of any reading:

- `verify` exits non-zero pre-handover and the surface cannot be rebuilt clean from the spec;
- `freeze` refuses — symlink present, or `ASSIGNMENT.md` identity disagreement (exit 2);
- an actor cannot compose its own fingerprint in situ, or has no contract to read at registration;
- the lease lapses mid-run and no Task Contract governs the work;
- a reader dies or is rotated with no checkpoint, and `A.7` resume is impossible;
- the packet cannot be assembled — a source file missing at build (`MISSING SOURCE`).

**Diagnostic value:** high, and it is about the laboratory, not the method. Under Annex F.4 this
class goes through `DIAGNOSE` before any accusation: delivery failure, runtime failure,
task-contract ambiguity, or actual refusal — and only the fourth, repeated after clarification,
is non-compliance.

### 7.4 · `EXPERIMENT_INVALID` — the run happened and a guarantee broke

| Condition | Decided by |
|---|---|
| a receipt does not re-verify — `ADDED`/`REMOVED`/`MODIFIED` non-empty | `verify-freeze`, enumerated, never counted |
| the pin moved and the delta was **not declared** | `tree-digest` re-run at step 12 |
| a first pass was edited after its freeze rather than appended to `post_freeze/` | receipt vs import |
| a locator cannot be resolved against the frozen surface | `locators` + `deepdive_manifest --verify-artifacts` |
| a disagreement was **resolved by Plan** rather than recorded | inspection of `unresolved_disagreements.md` against the matrix — § 28 |
| an independence violation is discovered | § 4.2 D-1/D-2 — **recovery: the run is void for the second reader, and the outcome says so** |
| a third file differed between the surfaces | `verify` |

🔴 **An invalidation is a result and is reported as one.** *"A declared contamination is a usable
result, and an undeclared one silently invalidates the experiment for everyone."*

### 7.5 · `UNRESOLVED` — every guarantee held and the experiment answers nothing

This is the class the pilot's own falsifier lands in:

> **If both readings, independently produced, prove individually traceable and mutually
> incomparable — because they anchored disjoint units of the population and no matrix row has
> entries in both columns — then the pipeline produced two artifacts and no experiment.**

Instrument: the F0 population. Coverage per reader, and **the size of the intersection**.
**A zero intersection is `UNRESOLVED` even though every reproducibility and traceability check
passes**, and no other criterion here would catch it.

Also `UNRESOLVED`:

- both readings declared partial, so what was compared is not what was designed;
- the join barrier's status cannot be established at all — no `JOIN-BARRIER` artifact and no
  usable receipt timestamps (§ 4.4 mitigation 2 exists precisely to make this rare);
- neither reading produced a claim candidate, so the matrix has no rows to align.

🔴 **`UNRESOLVED` is not a soft pass.** It says the *design* did not produce an experiment, and
the correct response is to change the design — not to re-run the same design with different
readers.

### 7.6 · `EXPERIMENT_VALID` — what it asserts and what it does not

| # | Condition | Decided by |
|---|---|---|
| V-1 | **reproducibility** | both receipts re-verify set-wise; the pin is unchanged, or its delta is declared |
| V-2 | **evidence traceability** | manifest `PASS` under `--verify-artifacts --require-current-schema`; every locator's artifact ∈ `ALLOWED_PATHS` with matching digest; every text snippet matches the surface exactly; figure attestations declared as such; every claim candidate anchors to ≥1 unit of the F0 population |
| V-3 | **disagreement preservation** | every flagged row appears in `unresolved_disagreements.md` with **both** statements quoted and typed; **zero rows resolved by Plan** |
| V-4 | **independence held** | 🔴 **detection only** — a pass is an absence of evidence, not evidence of absence, and is reported in those words |
| V-5 | **comparability** | the intersection of anchored population units is non-empty |

**What `EXPERIMENT_VALID` asserts:** *two independent readings of the same frozen evidence, under
this discipline, produced artifacts that a third party can re-derive, align, and disagree with.*

**What it does not assert, written down so it cannot be smuggled back in:**

```
NOT  that the reading reached the correct answer   — the pilot has no oracle, and inventing one
                                                     would make the pipeline's output its own judge
NOT  that anything committed                       — BATCH_COMMIT is Orchestrator's under an ACTIVE
                                                     lease; a pilot that must commit creates
                                                     pressure to commit
NOT  that A beat B, or B beat A                    — §32 and §8.5 both refuse it, and the two modes
                                                     have different landing places
NOT  that A and B agreed                           — two readers agreeing on an overshoot is
                                                     two overshoots
NOT  anything about speed, tokens or output volume — recorded apart (§8.4), never a quality proxy
NOT  that more claims is better                    — three well-anchored claims beat twelve unanchored
```

---

## 8 · THE FINAL QUESTION

> *"Could Orchestrator execute this pilot without asking a human to manually prepare prompts?"*

### 8.1 · The prompt half: yes — and for this paper, nothing needs writing at all

Measured per file, `grep -c -i -E '42397075|awag239|aqeilan|10\.1093/brain'`:

| Instruction file | Paper-identifier hits | Transfers to another paper? |
|---|---:|---|
| `MODE_A.md` | **0** | ✅ unchanged |
| `MODE_B.md` | **0** | ✅ unchanged |
| `SURFACE_CLAUDE.md` | **0** | ✅ unchanged |
| `ASSIGNMENT.scientist-a.md` | 1 | ✏️ one `SOURCE` line |
| `ASSIGNMENT.scientist-b.md` | 1 | ✏️ one `SOURCE` line |
| `BENCHMARK_INSTRUCTIONS.md` | 7 | ✏️ packet paths, output paths, the validator command |
| `OUTPUT_SCHEMA.md` | 6 | ✏️ manifest path, `pmid`, `doi`, landing, dossier path, command |

**The three that carry the reasoning carry no paper.** The four that are paper-bound are
already written for `PMID 42397075`. **For this pilot the prompt-authoring cost is zero.**

🔴 **And `build` will not template them.** `cmd_build` calls `shutil.copyfile` and nothing else —
a digest promised inside a copied file would be a digest nobody wrote. So for **any other** paper
those four files must exist as concrete bytes before `build` runs, and nothing in the repository
generates them.

### 8.2 · 🔴 But the automation ceiling is the spec, not the prompts

For a different paper the harder object is `surface_spec.json`, and one of its blocks cannot be
derived at all:

| Spec block | Automatable? |
|---|---|
| `content_scan.pattern` | ✅ from PMID / DOI / first author |
| `forbidden_prior_output_paths` | ✅ **by a recorded command at the pin** — and § 1.5 shows exactly what happens when it is transcribed instead |
| `source_files[]` with digests | ✅ from the corpus |
| `common_files[]`, `per_actor_files`, `empty_dirs`, `expected_output_*` | ✅ paper-independent |
| `population.sources[].rules` | 🔴 **no** — see below |

The population rules encode **the typography of the specific PDF**:

```
"heading": {"font_contains": "Aptos Display", "size": 15.77, "size_tolerance": 0.05}
"scope":   {"start_after": {... "size": 20.27, "text": "Materials and methods"},
            "stop_before": {... "size": 20.27, "text": "Results"}}
```

Those point sizes were measured off this publisher's typesetting. **Nothing in the repository
derives them, and a wrong value does not fail loudly — it produces a population that is short by
sections**, which is the failure a prior revision of this very spec made (four sections missing,
and a caption rule that ran 925 characters into the next figure). **The per-paper spec is a
measured, reviewed artifact. That is the automation ceiling, and it is upstream of every prompt.**

### 8.3 · The execution half: no — for three reasons, none of which is a prompt

**Reason 1 — 🔴 the repository contains no instrument that delivers anything to an actor.**
Swept `framework/scripts/`, `governance/scripts/`, `scripts/` for
`sendmessage|notify_actor|deliver_message|spawn_agent|open_session`: **0 files**. The broader
sweep for `dispatch|spawn` returns exactly one hit — `multiprocessing.get_context("spawn")`
inside a receipts test. Orchestrator *"assigns exclusively through Task Contracts"*, which are
**files**; a file that nobody opens has assigned nothing. Annex J.0 states the position the
repository is in: no exactly-once delivery, compensated by `ACK + dedup MESSAGE_ID + reinvio +
DIAGNOSE`. **A compensating protocol presumes a delivery channel. Opening a session in a surface
directory is a human act, and no artifact here performs it.**

**Reason 2 — nothing may be assigned.** `ACTIVE by derivation: 0`. Without an ACTIVE lease no
Task Contract may issue, no review level may be assigned, and no review may open. And
`ledger/tasks/` holds `plan/` only: **zero Scientist Task Contracts have ever existed.**

**Reason 3 — 🔴 "Orchestrator executes this pilot" is a category error.** Eight of the thirteen
steps in § 5.4 are **Plan's**, including both freezes, the join, the comparison and the outcome.
Orchestrator *"controls what work is done, by whom and in which order"* and must not *"bypass
Plan"*. An Orchestrator that performed steps 1, 3, 5, 6, 7, 8, 11 and 12 would not be executing
the pilot; it would be operating without the separation the pilot exists to test.

### 8.4 · The answer

> **Yes to the prompts, no to the pilot — and prompts were never the constraint.**
>
> For `PMID 42397075` every instruction file already exists, three of them are paper-independent,
> and `build` copies them verbatim. Nothing needs writing. **What a human still performs is not
> authorship — it is delivery and authorization**: opening two sessions in two surface
> directories, which no script in this repository does; taking a lease, which nothing derives on
> its own; and the explicit activation act `DEC-20260822` requires and whose form nobody has
> described.
>
> **For any other paper a human also performs a measurement** — the typographic rules of the
> population spec — and that is upstream of everything, including the prompts.

**The narrowest true statement of what is missing:** two acts and one determination.
`(i)` a delivery instrument, `(ii)` an ACTIVE lease, `(iii)` the activation act. **Not a prompt,
not a paper, and not a tool for the reading itself.**

---

## 9 · THE DISPATCH BLOCK

**This is a proposal, not an issued contract.** It is written in the form
`ledger/tasks/<ACTOR_ID>/<TASK_ID>.json` already takes in this repository, so that the object
Orchestrator would have to produce is described rather than invented at the moment it is needed.

```
SHARED
  BENCHMARK_ID          BENCH-AB-001
  PARALLEL_READ_GROUP   BENCH-AB-001         ← without it, two contracts on one source classify
                                                as DUPLICATED_ASSIGNMENT: a defect, not a design
  BLINDNESS_ROUTE       SURFACE_ALLOWLIST | C-1_NULL_PRIOR   ← §1.4, declared, never omitted
  PIN                   repository SHA + recursive files/fulltext digest   ← §0.3
  INPUT_MANIFEST_SHA256 recorded in BOTH receipts, binding the manifest to the pass that ran under it
  INTERACTION_MODE      AUTONOMOUS_COMPLETE   ← a reader that must ask cannot be blind
  REVIEW_REQUIREMENT    R4 · Mirror · the PROCESS  (C.1 floor; derogable only upward)
  RETRY_POLICY          max_attempts 1 · on_exhaust PARK   ← a retried blind read is not blind
  NETWORK               none, either reader, whole run. Plan runs the retraction/version check
                        before handover, so no mandated step needs it
  MILESTONE_PLAN        M1 packet opened and source_artifacts digested
                        M2 locators captured while the document is open
                        M3 coverage map complete over nine sections
                        M4 claim candidates written and anchored
                        M5 (B only) eleven critical axes answered
                        M6 validator PASS, TASK_COMPLETE declared
  DELIVERABLE           the surface output tree; WORK_COMMITs in the surface repo at M1…M6

PER ACTOR
  TASK_ID  BENCH-AB-001-A   OWNER scientist-a   MODE PRIMARY_EVIDENCE_READ      surface: <BENCH_ROOT>/BENCH-AB-001/scientist-a
  TASK_ID  BENCH-AB-001-B   OWNER scientist-b   MODE INDEPENDENT_CRITICAL_READ  surface: <BENCH_ROOT>/BENCH-AB-001/scientist-b
  ACCEPTANCE_CRITERIA      A-1…A-6 (§2.5); B additionally B-7…B-9 (§3.5)
  CURRENT_STATE            the surface repo HEAD; checkpoint at each milestone with
                           APPLICABLE_GOVERNANCE_FINGERPRINT composed IN SITU
```

### 9.1 · The command sequence, in order, with what each proves

```
1  population  --spec surface_spec.json --source-root <root> --out population/evidence_units.json
                                                     the denominator, before anyone reads
2  build       --spec surface_spec.json --source-root <root> --out <BENCH_ROOT> --emit-digests <map>
                                                     copies the allowlist; proves nothing
3  verify      --spec surface_spec.json --surfaces <BENCH_ROOT>
                                                     🔴 THE HANDOVER GATE. Exit 0 is precondition P-7
4  tree-digest --path <root>/files/fulltext          the pin's second half
5  freeze      (manifest)                            FROZEN_SHA256 over every field but HANDOVER
   ── HANDOVER ── writer transfer recorded; memory-scope check recorded ──
   ── the two readings ──
6  freeze      --surface <first declarer> --actor-id … --benchmark-id … --spec … --input-manifest …
                                                     F1 — before the content is read
7  freeze      --surface <second declarer> …         F2 — same rule
   ── F3 · JOIN: both receipts exist; imports ordered; JOIN-BARRIER written (§4.4 mitigation 2) ──
8  verify-freeze --receipt … --surface …   ×2        set-wise: ADDED/REMOVED/MODIFIED enumerated
9  verify      --spec … --surfaces … --post-read     parity, allowlist, forbidden paths, census
10 locators    --spec … --surface … --actor-id … --pmid …   ×2   containment, per entry
11 deepdive_manifest.py --workspace <surface> --pmid … --verify-artifacts --require-current-schema  ×2
12 tree-digest --path <root>/files/fulltext          re-pin; any delta declared as contamination
```

🔴 **Step 3 is a gate and step 2 is not.** *"Building is not proving"* is the tool's own verdict
line, and a surface that fails is **rebuilt from the spec, never patched** — a patched surface is
one whose content is no longer a function of the allowlist.

### 9.2 · Preconditions this contract cannot satisfy, measured today

| # | Precondition | State | Owner |
|---|---|---|---|
| C-1 | an **explicit activation act** making `roles/scientist.md` binding | 🔴 `ACTIVATION_NOT_CONFIRMED`; form unspecified | **operator** |
| C-2 | `scientist_reading_modes.md` + `controlled_benchmark_ab.md` canonical | 🔴 `PROPOSED` — *"Until then it binds nobody"* | operator, on the candidate |
| C-3 | an **ACTIVE** `ORCHESTRATOR_LEASE` | 🔴 `ACTIVE by derivation: 0` | Orchestrator |
| C-4 | `scientist-a` / `scientist-b` registered, `ACTOR_ID` fixed | 🔴 `NOT_REGISTERED` | Orchestrator, under lease |
| C-5 | Scientist capabilities `VERIFIED` **per actor** | 🔴 0 of 6 each; the two verified Scientist rows belong to `scientist-c` | L2 |
| C-6 | both reader worktrees clean and carrying their own governance | 🔴 `lettore` **201·0**, `lettore-b` **203·0**, both dirty, neither holds `governance/` or `roles/scientist.md` | Orchestrator + the actors |
| C-7 | a delivery channel | 🔴 **no instrument in the repository** (§ 8.3) | operator |

🔴 **C-6 carries a finding underneath the housekeeping, and it is the one that touches this
contract directly.** Both reader worktrees hold the **same uncommitted blob**, byte-identical, a
two-line receipt-id bump — written by something that reached both. **Two directories whose entire
purpose is independent parallel reading contain identical bytes from a common writer.** Whatever
wrote them crossed the isolation boundary this contract's § 4 treats as structural. The hypothesis
is testable and untested, and **it should be tested before independence is claimed of these two
directories** — which, note, the surface design sidesteps entirely by reading in standalone
repositories elsewhere.

---

## 10 · OPEN QUESTIONS

Recorded, not resolved. Numbering continues the prior records where the question is the same.

| # | Question | Owner |
|---|---|---|
| **Q-4** | what is `scientist-c`'s function, and when is its `ACTOR_ID` fixed? § 6.3 gives it a concrete one — R3 staffing | operator + Orchestrator |
| **Q-5** | the `OMISSION` asymmetry — MODE B only (§ 3.5) | Mirror (method) |
| **Q-10** | may a **declared partial** reading produce a commit candidate? § 2.5 proposes *no*; nothing on any ref decides it | operator |
| **Q-11** | what **form** does the activation act of `DEC-20260822` take? Everything downstream waits on an object nobody has described | **operator** |
| **Q-18** | who operates F3, given that the party the barrier constrains is the party that operates it? | operator + Orchestrator |
| **Q-19** | is Mirror handed the event ledger J.1 (absent) or the frozen artifacts (a declared deviation from § 29.3)? | **operator** |
| **Q-20** | 🔴 **which blindness route does the pilot run — `C-1 NULL PRIOR` or `SURFACE_ALLOWLIST`?** § 1.4 states what each costs. The first requires an acquisition that has not started; the second is available today and leaves 29 paths reachable by absolute path | **operator** |
| **Q-21** | 🔴 is `forbidden_prior_output_paths` **re-derived at the pin at build time**, or transcribed from `BASE_HEAD`? § 1.5 measures what transcription has already cost | **Plan candidate → operator** |
| **Q-22** | 🔴 is `JOIN-BARRIER` adopted (§ 4.4 mitigation 2)? It is one Plan artifact, no tool change, and it is the largest free improvement available to the only guarantee with no mechanism | **Plan candidate → operator** |
| **Q-23** | what wrote the identical uncommitted blob into both reader worktrees? Untested since 2026-08-17, in the two trees whose isolation the design depends on | Orchestrator, at registration |

---

## 11 · VALIDATION

### 11.1 · Constraint compliance — checked, not asserted

| Dispatch constraint | Status | Evidence |
|---|---|---|
| **read-only analysis** | ✅ | one file added under `learning/plan/`; no path under `governance/`, `roles/`, `framework/`, `ledger/`, `runtime/`, `disease-models/` touched |
| **no Scientist activation** | ✅ | no actor created, spawned, contacted, registered or assigned; no contract issued; no lease taken; `ACTIVE by derivation: 0` unchanged |
| **no paper reading** | ✅ | no paper opened; the only paper bytes touched were digested and counted, never read for content |
| **no execution** | ✅ | no surface built, verified or frozen; no benchmark command run against any actor tree |
| 1 · experiment input, all five sub-items | ✅ | § 1.1–1.7 |
| 2 · Scientist A, all five sub-items | ✅ | § 2.1–2.5 |
| 3 · Scientist B, all five sub-items | ✅ | § 3.1–3.5 |
| 4 · contamination control, mechanical vs discipline separated | ✅ | § 4.1 / § 4.3, with the third class § 4.2 named rather than folded into either |
| 5 · freeze model F0–F3, each with what/who/how-verified | ✅ | § 5.2, one table |
| 6 · output routing with the three named destinations | ✅ | § 6.1–6.5 |
| 7 · success/failure **without scores** | ✅ | § 7 — four classes, a precedence order, no composite, no threshold |
| final question | ✅ | § 8.4 |
| **a contract Orchestrator could dispatch** | ✅ | § 9, in the JSON form this repository already uses, with the command sequence and the preconditions it cannot satisfy |

### 11.2 · What this record does NOT do

It does **not** select or ratify a paper · create, activate, qualify, register or contact any
Scientist · issue a Task Contract · take a lease · build, verify or freeze any surface · open a
candidate or a review · write `unresolved_disagreements.md`, `JOIN-BARRIER.md` or any run
artifact · modify `surface_spec.json`, `benchmark_manifest.json` or the population · re-derive the
forbidden list into the spec (it measures the decay and names it `Q-21`) · create any schema,
field or vocabulary in a normative file · authorize `FIRST_PASS_STATES` to change · perform or
specify the activation act of `DEC-20260822` · commit anything to the disease model.

Every requirement, criterion and field below `§ 1` is an assessment of what the existing design
implies or a proposal marked as one. **None of it binds anyone**, and § 9.2 names who would act.

### 11.3 · Prior claims this record narrows or contradicts

| Prior claim | Where | Measured here |
|---|---|---|
| *"`FIRST_PASS_STATES` gains a staged value or the staged read is abandoned"* — carried as a blocking defect (`Q-16`) | `FIRST-WWOX-PAPER-PILOT-DESIGN-001` § 4.4 | **Correct about the staged read and out of scope here.** The dispatched freeze model is single-stage, which is `BENCH-AB-001`'s native shape; `Q-16` and `Q-17` do not arise (§ 5.1) |
| *"the pilot's paper most likely has to be acquired"* / *"the eighth should be a paper"* | ibid. § 2.2, § 7.4; `SCIENTIST-ACTIVATION-READINESS-001` § 8 | **True under `C-1 NULL PRIOR`, and that gate is not the benchmark's.** Under `SURFACE_ALLOWLIST` the paper exists, is acquired and is specified (§ 1.6). The two routes are not equally strong and the choice is `Q-20` |
| *"F0 surface + population: ✅ mechanised"* | ibid. § 4.3 | **True of the instrument, not of the artifact.** The manifest declares `_state: PREPARED — NOT FROZEN`, `FROZEN_SHA256: null`, `EVALUATION_POPULATION.sha256: "DERIVED_AT_BUILD"` (§ 0.3) |
| the forbidden-prior-output list as a settled input | spec `_forbidden_derivation` | its command yields **20** at the ref it names, the note says **21**, and **10** further paths name the paper at HEAD (§ 1.5) |

### 11.4 · Negative claims — each with its instrument and how long it holds

| Claim | Instrument | Holds until |
|---|---|---|
| no delivery/dispatch instrument exists in the repository | `grep -rl -i -E 'sendmessage\|notify_actor\|deliver_message\|spawn_agent\|open_session'` over `framework/scripts/`, `governance/scripts/`, `scripts/` → **0 files**; the broader `dispatch\|spawn` sweep returns one hit, `multiprocessing.get_context("spawn")` in a test | any such script is added |
| `unresolved_disagreements.md` on 0 refs | all-refs `git ls-tree -r --name-only "${r}"` over 46 refs, positive control `CLAUDE.md` → **46 of 46** | any ref adds it |
| no event ledger under `ledger/` | directory enumeration — 4 subdirectories, all inspected | J.1 is materialized |
| no Scientist Task Contract has ever existed | `ledger/tasks/` holds `plan/` only, 5 contracts | one is written |
| `verify-freeze` cannot express a pair | `--help` arity: `--receipt` ×1, `--surface` ×1 | the CLI changes |
| `build` does no templating | `cmd_build` source: `shutil.copyfile`, no substitution | the function changes |
| `MODE_A.md`, `MODE_B.md`, `SURFACE_CLAUDE.md` carry no paper identifier | `grep -c -i -E '42397075\|awag239\|aqeilan\|10\.1093/brain'` → 0, 0, 0 | those files change |
| the corpus is unchanged since the census date | 174 top-level / 654 recursive; digest `b48694a1…` identical to yesterday's computation | the next acquisition |

---

## 12 · NEXT_TRANSITION

Nothing in this record authorizes a next step. Three are unblocked today, ordered by what their
duration argues for:

1. **Decide `Q-20` — the blindness route.** It is the only decision that changes whether this
   pilot needs an acquisition at all, and it is upstream of everything in § 9. If the answer is
   `SURFACE_ALLOWLIST`, the experiment's input half is complete today and the remaining blockers
   are the three in § 8.4 — none of which is a paper, a prompt or a tool for the reading.
2. **Adopt `Q-22` — `JOIN-BARRIER`.** One Plan artifact, no tool change, no approval dependency,
   and it is the largest available improvement to the only guarantee in the design with no
   mechanism at all.
3. **Re-derive the forbidden list at the pin (`Q-21`).** A transcribed enumeration has already
   narrowed by eight paths without the verdict line changing, and the repair is to run the command
   at build time instead of quoting an earlier run of it.

`Q-11` — the form of the activation act — remains the operator's and has no date. All three above
proceed while it waits.

🔴 **The finding I would put above the contract.** Seven records have carried *"the pilot has no
paper."* Measured at this HEAD, `PMID 42397075` is acquired, specified, and its denominator is
fixed at 65 units and 109 panels; four of the seven instruction files are already written for it
and the other three never needed to be. **What is missing is not the paper and not the prompt. It
is that nothing in this repository can hand a directory to a reader, and nobody holds the lease
that would let them.**
