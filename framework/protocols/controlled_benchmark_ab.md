---
artifact: LEGEND protocol — CONTROLLED BENCHMARK · Scientist A vs Scientist B · first instance
protocol_id: CONTROLLED_BENCHMARK_AB
version: 1
benchmark_id: BENCH-AB-001
governance_version: 3.1.1
normative: yes — for the benchmark it defines; it changes no rule outside it
status: PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC. The
  benchmark it defines is NOT authorized to start by this file (see §9).
materialized_by: plan
materialized_on: 2026-08-18
authority: HANDOFF-SCIENTIST-AB-SPEC (operator scope); framework/protocols/scientist_reading_modes.md;
  Annex A, C, D, J.0; body §2, §14, §27, §37
paper: PMID 42397075 · doi 10.1093/brain/awag239 · Steinberg/Zonca/Abdellatif … Aqeilan, Brain 2026
---

# CONTROLLED BENCHMARK — Scientist A vs Scientist B, one paper, blind first pass

## 0 · What is being measured, and what is not

One paper. Two persistent actors — `scientist-a` in `MODE A · PRIMARY_EVIDENCE_READ`,
`scientist-b` in `MODE B · INDEPENDENT_CRITICAL_READ` (`scientist_reading_modes.md` §4–§5). Each
reads **the same bytes**, under **the same instructions and the same output schema**, in a
surface that **contains no prior LEGEND output on the paper and no view of the other reader**.
Both first passes are **frozen** before either is compared with anything. Then a structural
comparison, a blind locator audit, Mirror's adjudication of the process, and an outcome that
reports every dimension separately.

**The single declared variable is the mode directive.** Everything else the two readers receive
is byte-identical and the manifest proves it (§3–§4). One caveat is stated here so it cannot be
lost later: with one paper and one session per actor, **the benchmark cannot separate the effect
of the mode from the variance between two sessions**. It is a first controlled benchmark — one
variable, everything else held — not a statistical study. Its value is the *material* it produces
(two frozen readings, an audit, an adjudication) and the failure modes it surfaces, not a
number.

**Explicitly not measured as quality:** speed, token use, cost, output length, or how often A and
B agree. They are recorded (§8.4) because they are cheap to record and someone will ask; they are
reported in a separate table and never enter a quality judgment.

---

## 1 · Preconditions — none of them is satisfied by this file

| # | Precondition | Source | State at materialization (2026-08-18) |
|---|---|---|---|
| P-1 | `scientist_reading_modes.md` and this protocol canonical | §9 | **not canonical** — this candidate |
| P-2 | `scientist-a`, `scientist-b` registered (I.2 step 7) | Agent Card registry, branch `orchestrator` | **NOT_REGISTERED**, `ACTOR_ID UNRESOLVED` |
| P-3 | Scientist capabilities `VERIFIED` at L2 — at minimum *Full-text read producing a receipt*, *Work manifest with verbatim locators*, *Worktree confinement*, *Auto Mode actually active* | body §8, I.4: assignment on VERIFIED capabilities | **all UNVERIFIED**; L2 **SUSPENDED** by the C-9 hold (operator, 2026-08-17) — this protocol does not lift it |
| P-4 | `ORCHESTRATOR_LEASE` ACTIVE for the assignment and for any canonical step | H.1, I.3 | derive with `framework/scripts/lease_state.py --check` at the moment; never assume |
| P-5 | C-2 preconditions declared by both actors at registration | `scientist_reading_modes.md` §1.4 | pending registration |
| P-6 | Two Task Contracts issued (§5 step 3) | Annex A.1 | none exists |
| P-7 | Input surfaces built, verified, manifest frozen (§2–§4) | this protocol | not built |

`BLIND FIRST PASS` is authorized only when every row reads satisfied **at the moment of
handover**, by the route each row names.

---

## 2 · The benchmark input surface — allowlisted, per actor, outside every LEGEND checkout

### 2.1 · Why a separate surface and not the actor's worktree

`lettore` and `lettore-b` are checkouts of a repository that has **already worked this paper**:
at `BASE_HEAD cbce3016`, twenty-one tracked files name it — the canonical deep-dive manifest,
the partial-locators dossier, the receipt ledger, the paper registry, the tracking log, the
discovery ledger, the surface census, an orchestration review, an eval finding, three other
manifests that cross-reference it. A first pass run *in* such a checkout is blind only by
promise. The handoff said it precisely: *the blinding problem is a property of the corpus, not
of this paper*, and choosing another WWOX paper does not solve it, because every paper with
verifiable provenance here is one this repository has already worked.

So the surface is **built by allowlist, from nothing**, into a directory that is **not a checkout
of the LEGEND repository** and shares no object store with it. What is not copied in is not
there. Blindness becomes a property of a directory whose full content is enumerated, digested,
and re-verifiable by anyone with the manifest.

**Two residuals, stated where the claim is** (J.0 — no runtime-enforced permissions):

- an actor can read *outside* its surface by absolute path. Nothing prevents it. The surface
  makes the blind path the **default** path and the only one that leaves the required evidence
  — every locator must resolve inside the surface (§4.3) — and it makes the leaving of the
  surface an *act*, not an accident;
- the model may carry knowledge of the paper from training. Uncontrollable; covered by the
  standing rule that undeclared general knowledge is `DEFAULT_FROM_TEXTBOOK` and by MODE B's
  `OMISSION` axis being run on both.

Neither residual is a reason to weaken the surface. Both are reasons not to describe it in
stronger words than "the default path is blind and the evidence path is inside".

### 2.2 · One writer per surface, transferred once

Plan builds each surface and is its only writer until **HANDOVER**; at handover the writer
becomes the named actor and Plan does not write into it again — Plan reads it once more, at
**FREEZE** (§7). Body §14 holds by construction: two directories, two writers, one transfer,
recorded in the manifest's `HANDOVER` block.

Each surface is a fresh, standalone `git init` repository so the actor's `WORK_COMMIT` obligation
(D.1) is met inside the surface, at milestone granularity, on a branch nobody else writes.
🔴 **Declared deviation, scoped to the benchmark:** the actor's `WORK_COMMIT`s for the first
pass land in the surface repository, **not** on `lettore` / `lettore-b`. Reason: a worktree of
the LEGEND repository — sparse, orphan or otherwise — still shares its object store, so
`git show main:<prior output>` is one command away; a standalone repository is not. The
reconciliation is FREEZE + IMPORT (§7): the frozen tree is imported byte-identically into the
LEGEND repository by Plan, digests recorded, and the surface repository is retained as evidence
until the outcome is canonical.

*Observed property of this runtime, recorded and not relied on:* the interactive Claude Code
profile keeps auto-memory **per working directory**. A session opened in a fresh surface path
starts with an empty memory scope, whereas one opened in `lettore` would open the memory the
`lettore` sessions accumulated. Plan checks the surface's memory scope is absent before
handover and records the check; it is a favourable accident of the deployment, not a
guarantee.

### 2.3 · Layout — repository paths kept, so the validators run unmodified

```
<BENCH_ROOT>/BENCH-AB-001/<ACTOR_ID>/            ← standalone git repo; BENCH_ROOT is a local-instance
│                                                   value (deployment/local_instance.md), never written here
├── ASSIGNMENT.md                                 🔴 the ONE per-actor file: ACTOR_ID · TASK_ID · MODE · BENCHMARK_ID
├── CLAUDE.md                                     identical: minimal router → benchmark/BENCHMARK_INSTRUCTIONS.md
├── benchmark/
│   ├── BENCHMARK_INSTRUCTIONS.md                 identical
│   ├── OUTPUT_SCHEMA.md                          identical
│   └── MODE_DIRECTIVE.md                         🔴 same path, different bytes: MODE_A.md content for A, MODE_B.md for B
├── roles/scientist.md                            identical — the actor's contract; its digest IS ROLE_CONTRACT_HASH
├── framework/
│   ├── instruction/epistemic_discipline.md       identical
│   ├── master/gold_is_in_the_details.md          identical
│   ├── protocols/fulltext_read_receipt.md        identical
│   ├── protocols/scientist_reading_modes.md      identical
│   ├── eval/failure_taxonomy.md                  identical
│   └── scripts/deepdive_manifest.py, corpus_firewall.py   identical — the validator, unmodified
├── files/fulltext/
│   ├── PMID42397075_Aqeilan2026.pdf              article_binary   b6b44816…
│   ├── PMID42397075_Aqeilan2026_fitz.txt         article_text     9c48aa09…
│   └── PMID42397075_Aqeilan2026_assets/
│       └── brain-2025-03809-File008…012.pdf      supplements ×5   (author contributions · detailed
│                                                  methods · supplementary figures · resource table ·
│                                                  uncropped blots)
├── disease-models/wwox/research/deepdive_manifests/    EMPTY at handover — the actor's manifest goes here
├── disease-models/wwox/research/fulltext_dossiers/     EMPTY at handover — the actor's dossier goes here
└── output/                                        EMPTY at handover — receipt.json · claim_candidates.md ·
                                                   critical_reading.md · renders/
```

**What is deliberately not in the surface, and why:**

- the page renders and figure crops under `_assets/` (`S_fig_*`, `S_page_*`, `S_native_*`,
  `figs/*`, `S10_caption_*`) — they are renders of the source, but **their selection encodes a
  prior reader's attention** (which pages, which panels, which dpi). Each actor renders what it
  needs, with the recipe in the instructions, and lists its renders with digests as
  `source_artifacts` of kind `figure`. Parity of *source* is preserved; parity of *attention* is
  not imposed;
- every other repository file. The discipline documents included were checked for the paper's
  identifiers: `0` occurrences in each (`grep -c -i -E '42397075|aqeilan|steinberg|awag239|MYC'`).
  `framework/eval/finding_20260809_text_surface_fidelity.md` names the paper and is **excluded**.

**A caveat carried, not hidden.** The text surface `…_fitz.txt` (`9c48aa09…`) is the one the
prior reading used, and its dossier records that the declared extraction recipe does not
regenerate it byte-for-byte. For the benchmark that is irrelevant in one direction and relevant
in another: both actors get the identical bytes, so parity holds; but the surface is not
reproducible from the PDF by a stated command, so **the digest, not the recipe, is the
identity of the text surface**. Recorded in the manifest as `text_surface_recipe: NOT_REPRODUCIBLE
— identity by digest`.

---

## 3 · The input manifest — an experiment record, not a data model

`framework/eval/benchmarks/BENCH-AB-001/benchmark_manifest.json`, **frozen before HANDOVER**,
tracked, its own digest recorded in each actor's `ASSIGNMENT.md`. Fields:

```
BENCHMARK_ID · PMID · DOI · PAPER_TITLE_SHORT · BASE_HEAD
PROTOCOL: {reading_modes: {path, version, sha256}, benchmark: {path, version, sha256}}
SCHEMA_VERSION            manifest schema of the outputs (deepdive_manifest CURRENT_SCHEMA_VERSION = 2)
                          + OUTPUT_SCHEMA.md version + sha256
INSTRUCTIONS_VERSION      BENCHMARK_INSTRUCTIONS.md version + sha256; MODE_A.md, MODE_B.md version + sha256
SOURCE_FILES[]            {surface_path, kind, sha256, bytes, origin} — the packet
COMMON_FILES[]            {surface_path, sha256} — every identical non-packet file
PER_ACTOR_FILES           {scientist-a: [{surface_path, sha256}], scientist-b: [...]} — exactly
                          ASSIGNMENT.md and benchmark/MODE_DIRECTIVE.md, nothing else
ALLOWED_PATHS[]           the complete allowlist — the union of the three above plus the empty output slots
FORBIDDEN_PRIOR_OUTPUT_PATHS[]  every tracked path at BASE_HEAD naming the paper, enumerated by the
                          command recorded beside the list; must be ABSENT from every surface
CONTENT_SCAN              the identifier regex run over each surface excluding the packet and the
                          instruction files; expected hits: 0
EVALUATION_POPULATION     {path, sha256} — population/evidence_units.json, fixed here (§8.1)
PARITY                    per surface path: sha256_A == sha256_B for all COMMON and SOURCE files;
                          the two PER_ACTOR paths listed with both digests
HANDOVER                  {scientist-a: {at, by, to, surface_tree_sha256, memory_scope_absent},
                           scientist-b: {…}} — filled at handover, and the manifest is otherwise
                          frozen: FROZEN_SHA256 covers every field except this block
```

`SHA256` throughout is the SHA-256 of file bytes; `surface_tree_sha256` is the SHA-256 over
the sorted `path\0sha256\n` lines of every regular file in the surface — computed by the same
command for build, verify and freeze (`framework/scripts/benchmark_input_surface.py`).

**Ex ante checks the manifest makes possible, each a command:**

```
build       plan builds both surfaces from the source root and the allowlist, digests every file
verify      for every path in ALLOWED_PATHS: exists in A, exists in B, sha256_A == sha256_B
            (PER_ACTOR paths: present, and NOT identical across actors)
            for every path in FORBIDDEN_PRIOR_OUTPUT_PATHS: absent from A, absent from B
            no file present in either surface outside ALLOWED_PATHS
            output slots empty
            CONTENT_SCAN hits == 0
freeze      surface_tree_sha256 per actor; recorded in HANDOVER, then in the frozen receipt
locators    after a reading: every cited artifact ∈ ALLOWED_PATHS or produced in an output slot
verify --post-read   the same parity, allowlist and prior-output checks, with the output slots
            excluded — see §4.3 for why authorship inside a slot is not decidable there
```

Every one of these is a subcommand of `framework/scripts/benchmark_input_surface.py`, and
`verify` exits non-zero on any finding. **A surface that fails is rebuilt from the spec, never
patched**: a patched surface is one whose content is no longer a function of the allowlist.

---

## 4 · Blinding as a property, and its three checks

### 4.1 · Same paper, same version, same bytes, same digests

`SOURCE_FILES` carries one digest per file; `PARITY` asserts equality per path across the two
surfaces; `verify` recomputes both. `A_PACKET_SHA256 == B_PACKET_SHA256` is therefore a fact
about bytes on disk at verification time, not a statement about how the files were copied.
(The root and `lettore` copies of the PDF are hard-linked — same inode. The surfaces are
**copies**, so a write in one cannot appear in the other.)

### 4.2 · Same instructions, same output schema, one declared difference

`COMMON_FILES` are byte-identical. `PER_ACTOR_FILES` are exactly two paths, both fully specified
in the manifest with per-actor digests: `ASSIGNMENT.md` (identity and task — differs by
necessity) and `benchmark/MODE_DIRECTIVE.md` (the experimental variable). **A third differing
file is a broken benchmark, and `verify` reports it.**

### 4.3 · No visibility A↔B, no prior output — and how it is checked after the fact

- **Before:** the surfaces are separate directories with separate repositories; neither is
  addressed to the other; `FORBIDDEN_PRIOR_OUTPUT_PATHS` absent; `CONTENT_SCAN` clean.
- **During:** no channel between the actors, and Orchestrator relays no content. A `BLOCKER`
  from a reader is answered on the protocol, never on the paper.
- **After:** every locator in each frozen manifest must name an `artifact` inside
  `ALLOWED_PATHS`, or a render the reader produced in its own output slots.
  `deepdive_manifest.py --verify-artifacts` enforces existence and digest;
  `benchmark_input_surface.py locators` enforces *membership in the allowlist*, per entry. A
  citation outside the surface is `BENCH_INVALID` **for that entry** — recorded, never
  silently dropped, because a dropped entry is a reading that looks clean and is not.

  🔴 **One collision, and it is the sharpest argument for §2.1.** The reader's own manifest
  lands at `disease-models/wwox/research/deepdive_manifests/PMID42397075.json` — the exact
  path LEGEND's prior manifest occupies, because `deepdive_manifest.py` derives that path from
  disease and PMID and it cannot be elsewhere without breaking the validator. **In a checkout
  of the repository the reader would be writing its manifest on top of the prior one.** In the
  surface the slot is proven empty at handover and the freeze receipt pins what it held at
  completion; the post-read run therefore skips the output slots rather than reporting on
  authorship it cannot determine. *Both this and the mirror-image case — the content scan
  firing on the reader's own PMID — were found by running the tool against a synthetic output
  tree before any reader existed, and are recorded in the candidate's test evidence.*

What "after" cannot do: prove that a reader did not open a file by absolute path and quote
nothing from it. That is the J.0 residual of §2.1, and this section does not claim otherwise.

---

## 5 · Sequence — who does what, in what order, leaving what

| Step | Actor | Act | Durable evidence |
|---|---|---|---|
| 0 | operator / Orchestrator | preconditions P-1…P-5 satisfied by their own routes | canonical tip; registry rows; L2 record; lease derivation |
| 1 | Plan | build both surfaces from the source root; `verify`; enumerate the evaluation population (§8.1); write and **freeze** the manifest | `benchmark_manifest.json` (FROZEN_SHA256), `population/evidence_units.json` — WORK_COMMIT on Plan's branch |
| 2 | Orchestrator (lease ACTIVE) | issue **two** Task Contracts: `BENCH-AB-001-A` OWNER `scientist-a` MODE A; `BENCH-AB-001-B` OWNER `scientist-b` MODE B; both `PARALLEL_READ_GROUP: BENCH-AB-001`; INTERACTION_MODE `AUTONOMOUS_COMPLETE`; REVIEW_REQUIREMENT R4 (Mirror, process); MILESTONE_PLAN = §6 milestones; DELIVERABLE = the surface's output tree | the two contracts under `ledger/tasks/<ACTOR_ID>/`; TASK_ACK; TASK_CLAIM (each actor checks §2.2 rule 3 of the reading-modes protocol first) |
| 3 | Plan → each actor | **HANDOVER**: writer transfer recorded; memory-scope check recorded | manifest `HANDOVER` block |
| 4 | `scientist-a`, `scientist-b` | **blind first pass**, autonomous, in the surface, at full depth; WORK_COMMITs in the surface repo at milestones; `TASK_COMPLETE` to Plan | output tree in the surface; commits |
| 5 | Plan | **FREEZE** each reading the moment its completion is declared — before reading its content: tree digest, per-file digests, commit sha, timestamps → receipt; then **IMPORT** byte-identical into the LEGEND repository | `frozen/RECEIPT-<ACTOR_ID>.json`; `first_pass/<ACTOR_ID>/…` |
| 6 | Plan | mechanical checks (§8.2 rows marked *mechanical*); structural **comparison matrix**; **unresolved disagreement list** — listed, never resolved by Plan (§28) | `comparison/comparison_matrix.md`; `comparison/unresolved_disagreements.md` |
| 7 | fresh blind agents, spawned by Plan per `legend-locator-audit` | blind audit of every (proposition, snippet, anchor) triple of both readings, reader identity withheld | `audit/locator_audit-<ACTOR_ID>.md` |
| 8 | Mirror | **adjudication of the process** (R4): failure modes per reading, epistemic discipline, whether the protocol was followed, whether the design held | `reviews/mirror/BENCH-AB-001-ADJUDICATION.md` on branch `mirror`; pointer + digest under `adjudication/` |
| 9 | Plan | **outcome summary** — every dimension separately, secondary metrics apart, disagreements carried, no composite | `outcome/BENCH-AB-001-OUTCOME.md` |
| 10 | Orchestrator | scientific disagreements → Annex C review (R2/R3) if warranted — **outside** the benchmark record; any promotion of a claim → ordinary pipeline; any promotion of the intermediate fields → a governed change | not part of `BENCH-AB-001` |

Steps 5–9 each reach `main` only through an integration candidate. Nothing in the benchmark
writes a `*_current.md`, the receipt ledger, or any registry.

---

## 6 · Durable seats — one directory, one writer per file, imports by digest

`framework/eval/benchmarks/BENCH-AB-001/` (content domain — hashed in every candidate):

```
benchmark_manifest.json                     Plan     frozen before handover (§3)
population/evidence_units.json              Plan     ex ante population (§8.1); digest in the manifest
instructions/BENCHMARK_INSTRUCTIONS.md      Plan     versioned; digest in the manifest
instructions/OUTPUT_SCHEMA.md               Plan     versioned; digest in the manifest
instructions/MODE_A.md · MODE_B.md          Plan     versioned; digests in the manifest
instructions/ASSIGNMENT.template.md         Plan     the per-actor file, with the two values that vary
first_pass/scientist-a/…                    Plan (import, byte-identical from A's frozen tree)
first_pass/scientist-b/…                    Plan (import, byte-identical from B's frozen tree)
frozen/RECEIPT-scientist-a.json             Plan     the freeze record — commit sha, tree digest, file digests, timestamps
frozen/RECEIPT-scientist-b.json             Plan
comparison/comparison_matrix.md             Plan     structural alignment (§8.3)
comparison/unresolved_disagreements.md      Plan     listed, typed, unresolved
audit/locator_audit-<ACTOR_ID>.md           blind auditor output, imported by Plan
adjudication/MIRROR-ADJUDICATION.pointer.md Plan     path on branch mirror + sha256 of Mirror's record
outcome/BENCH-AB-001-OUTCOME.md             Plan
```

Mirror writes on its own branch (`reviews/mirror/`), a declared control-plane root; the
benchmark directory carries a pointer and a digest, never a copy that could drift.

---

## 7 · Freezing — first passes are immutable from the moment they are declared complete

- Plan freezes **on the completion declaration and before reading the content**: the receipt is
  written from `git rev-parse HEAD`, the tree digest, and per-file digests of the surface's
  output tree. The order matters: a freeze taken after Plan has read the content is a freeze
  whose timing cannot be shown.
- The import into `first_pass/<ACTOR_ID>/` is byte-identical and the receipt's digests are the
  check. Anyone can re-derive them from the import.
- **The comparison, the audit, the adjudication and the outcome never modify a first pass.** A
  correction an actor wants to make after freeze is a **new dated file** under
  `first_pass/<ACTOR_ID>/post_freeze/`, referenced from the outcome, with the original left as
  frozen. Retroactive edits are the one thing this section exists to make impossible to do
  quietly.
- Neither actor sees the other's first pass until **both** are frozen. Ordering: whichever
  finishes first is frozen first; the second is not shown the first until its own freeze is
  recorded.

---

## 8 · Evaluation design — population first, dimensions separately, no composite

### 8.1 · The evaluation population is fixed before anyone reads

`population/evidence_units.json` enumerates the paper's **structural evidence units** from the
text surfaces alone, by command, before either first pass — main figures and their lettered
panels as named in captions, tables, Results subsection headings, supplementary figures and
tables, supplement sections. Structural enumeration is not a reading: it lists what the paper
*contains*, not what it *shows*, and Plan may do it (§28) because it decides nothing about
meaning. Its digest is in the manifest, so it cannot be redefined after the readings exist. Every
coverage measure below is computed over this population and nothing else. What the population
does **not** do: it does not say which units matter — that is exactly what the two readings and
the adjudication will disagree about, and it must not be pre-empted.

### 8.2 · Dimensions — each with unit, measure, route, evaluator, blindness

| Dimension | Unit / measure | Route | Evaluator |
|---|---|---|---|
| **EVIDENCE COVERAGE** | units of the population with ≥1 locator anchored in them, per reader; units touched by one reader only; coverage map states per section; supplementary units covered | mechanical over locators + population | Plan |
| **CLAIM PRECISION** | per (proposition, snippet, anchor): `SUPPORTED · OVERSHOOT · UNDERSHOOT · NOT_IN_SOURCE · UNVERIFIABLE_SURFACE`; per claim candidate: `Type` claimed vs `Type` the audited evidence bears | blind locator audit; then adjudication for the `Type` question | fresh blind agents; Mirror |
| **PROVENANCE** | every locator's artifact ∈ ALLOWED_PATHS with matching digest; manifest `PASS` under `--verify-artifacts --require-current-schema`; `source_artifacts` complete; coverage map consistent with where locators come from (a supplement locator against `Supplementary: not_read` is an inconsistency) | mechanical | Plan |
| **LOCATOR FIDELITY** | text-surface snippets match exactly (validator); figure attestations declared as such; elisions marked; anchors resolvable | mechanical + audit | Plan; blind agents |
| **EPISTEMIC DISCIPLINE** | every carried statement typed; negatives with `PREMISE` tag and `REVIVAL_TRIGGER`; `DEFAULT_FROM_TEXTBOOK` declared where used; the four intermediate fields present and separable — `Observation` free of conclusion verbs, `Author interpretation` marked as theirs; hypothesis→observation promotions found by audit | mechanical for presence; adjudication for substance | Plan; Mirror |
| **CONTEXT PRESERVATION** | per claim candidate: genotype · cell type · developmental stage · intervention · endpoint present; instances of context collapse (`CONTEXT_COLLAPSE` axis; `MECHANISTIC_OVERTRANSFER` gate) | presence mechanical; instances adjudicated | Plan; Mirror |
| **METHODS / LIMITATIONS** | findings with methods captured; limitations recorded (authors' and reader's, distinguished); statistics caveats named; detailed-methods supplement (File009) covered | presence mechanical; substance adjudicated | Plan; Mirror |
| **CONTRADICTION / NEGATIVE EVIDENCE** | null/negative findings carried; internal contradictions found; `panel_qualifies_text` / `text_contradicted_by_panel` used with valid pointers; MODE B axes each answered | mechanical for pointers and axis completeness; substance adjudicated | Plan; Mirror |
| **MECHANISTIC VALUE** | mechanistic implications carried, each typed and each stating whether the intermediate is measured or hypothesized; **recorded descriptively — the judgment of value is not made inside the benchmark** | listing | Plan lists; judgment → Annex C review opened by Orchestrator, outside the record |
| **FAILURE MODES** | instances per `framework/eval/failure_taxonomy.md` gate, per reading, with locator | adjudication | Mirror |

**Mechanical rows are commands; adjudicated rows are Mirror's, on the process; the one row that
is scientific judgment (mechanistic value) is deferred to the review ladder.** Plan never
decides what a claim means (§28) — it aligns, counts, and lists.

### 8.3 · The comparison matrix

Rows: claim candidates of both readings, aligned by shared locator anchors (same figure/table/
section unit) — alignment is structural, by unit, not by Plan's reading of whether two claims
"mean the same". Columns: present in A · present in B · units cited · `Type` A · `Type` B ·
`Direction` A · `Direction` B · audit verdicts · intermediate-field agreement · disagreement
flag. A row with a disagreement flag goes to `unresolved_disagreements.md` with both readings'
statements quoted and typed, and stays unresolved there. `INFERENCE_A + INFERENCE_B +
DISAGREEMENT_UNRESOLVED`, explained, is a legitimate outcome (body §27).

### 8.4 · Secondary — operational, recorded apart, never a quality proxy

```
TIME              handover → completion declaration, per actor (wall clock from the receipts)
TOKEN / CONTEXT   only if the runtime exposes it; otherwise "NOT OBSERVABLE" — never estimated
OUTPUT VOLUME     bytes; locator count; claim-candidate count; critical-record entries
```

Reported in their own table in the outcome. **They are not combined with anything, they do not
break ties, and a reading is not "better" for being faster, shorter or cheaper.**

### 8.5 · Reporting rules

No overall score. No weighting. Each dimension its own table, A and B side by side, with the
route that produced each number. Agreement between A and B is reported descriptively (units both
covered; claims both carried) with the caveat in §0 beside it, and is not a quality measure —
two readers agreeing on an overshoot is two overshoots. Every count is an enumerated set or
carries the command that produced it.

---

## 9 · Canonicalization dependency — determined at source

The question was whether the blind first pass may run before `scientist_reading_modes.md` and
this protocol are canonical. Read, not inferred:

1. `roles/scientist.md` front matter: *`status: PROPOSED — binding once Mirror hostile review
   passes and the operator approves`*. The reading modes are a directive on how a Scientist
   reads under a task; the candidate amends the role contract to reference them. A role
   contract binds when canonical, not before.
2. **The fingerprint — measured, not predicted.** `governance/plan_defined_parameters.md` § P2.2:
   the scientist set is `CORE` + Annex C, E, F, and `CORE` includes `roles/scientist.md`. The
   candidate edits that file, so the scientist fingerprint rotates on canonical execution. Both
   values were composed, at `BASE_HEAD`'s contract and at the candidate's:

   ```
   scientist      355e3529431f89f3e7adf764548f4117374fa92118f8f794bd0ba579b7ff97ab   at cbce3016
   scientist      82423a48b700bc2b392b4c8e944eb6a0b07cefebddf63db00e96716cbed43e79   with this candidate
   plan · mirror · orchestrator                                          UNCHANGED — all three
   ```

   A checkpoint written under `355e3529…` is `INCOMPATIBLE` (Annex A.6 refusal rule) the moment
   the spec becomes canonical: a benchmark started before would have to be abandoned or resumed
   under a fingerprint it was not written under. **The rotation is confined to the scientist
   set** — the other three are byte-identical across the change, so nothing outside the reading
   role is invalidated.
3. Annex A.1: a Task Contract names an `OWNER (ACTOR_ID)`. Both ACTOR_IDs are `UNRESOLVED`
   until the candidate executes (`scientist_reading_modes.md` §1.1). No contract can be issued
   to an unresolved owner.
4. Body §8 / I.4: assignment on `VERIFIED` capabilities. None is verified; L2 is suspended by
   operator decision. Independent of canonicalization, and also unmet.

**Determination: `BLIND FIRST PASS — BLOCKED BY CANONICALIZATION`** (and, independently, by
P-2…P-4). The work under `HANDOFF-SCIENTIST-AB-SPEC` therefore ends at *candidate complete +
Mirror review*; nothing in this protocol is executed by materializing it.

---

## 10 · What this protocol does not do

It does not start the benchmark, register anyone, verify a capability, lift the L2 hold, take a
lease, or issue a task. It does not integrate a benchmark claim into the disease model, write to
any `*_current.md` or to the receipt ledger, promote the intermediate fields into the claim
registry, add a Metacognition Agent, run a Scientist C arm, or name a second paper. It does not
resolve the registry validator, P7, the approval queue, the ACK criteria, the Plan→Mirror routing,
or Mirror's unratified methodology observation — each is carried forward exactly as owed.
