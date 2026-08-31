---
artifact: FIRST SCIENTIST PILOT READINESS AUDIT — the input half is ready, the laboratory is not, and nothing is running
record_id: FIRST-SCIENTIST-PILOT-READINESS-AUDIT-001
task_id: FIRST_SCIENTIST_PILOT_READINESS_AUDIT_v1
author: plan
authored_on: 2026-08-22
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)

STATUS: READ_ONLY_AUDIT
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - READINESS AUDIT
  - NOT GOVERNANCE
  - NOT A PROTOCOL
  - NOT A DECISION
  - NOT EXECUTION AUTHORIZATION
  - NOT A TASK CONTRACT
  - NOT A PAPER SELECTION — § 1 measures a selection made elsewhere and ratifies nothing
  - NOT A SCIENTIST ACTIVATION
  - NOT AN AGENT DEFINITION

naming_note: >
  Named as the dispatch named it. Not a Session Learning Record (Annex E.6), not a handoff, and
  it takes no `SLR` number it has not earned — the precedent of the eight non-SLR records already
  in this seat.

domain: >
  CONTENT — verified this session. `governance/plan_defined_parameters.md` § P5.1 declares
  `CONTROL_PLANE_ROOTS` exhaustively as `governance/candidates/`, `ledger/`, `reviews/`, and
  everything not under a declared root is content. `learning/` is under none of them, so this
  file sits inside the `CANDIDATE_CONTENT_HASH` of any future candidate spanning this branch and
  moves it. Disclosed.

relation_to_prior_work: >
  Eight Scientist records precede this one, four of them uncommitted in this working tree. This
  record restates none of their designs. It does the one thing none of them does: it treats
  their claims as hypotheses and re-executes the measurements behind them, then answers a single
  binary — can the pilot start. Six prior numbers came back different and are given both ways in
  § 8; one prior claim is withdrawn outright.

verdict_transfer: >
  NONE. Every number below was produced by a command run in this session at the HEAD named in
  § 0.1, and the command is named beside it. Nothing is carried from a prior record, a manifest
  field, a registry row or a handoff. Where a prior record reached the same number I say so;
  where my measurement contradicts one I give both.

disclosure: >
  🔴 This file names `PMID 42397075`. It is therefore itself a path that a re-derivation of
  `forbidden_prior_output_paths` will return, and § 5.T-4 counts it. Naming the paper is
  necessary for the audit to be checkable; the alternative — an audit that cannot say what it
  audited — is worse. The decay this adds to is measured rather than avoided, and it is the
  reason the repair in § 5.T-4 is a build-time command and not a longer list.
---

# FIRST SCIENTIST PILOT READINESS AUDIT — 001

> **The five findings that decide this audit.**
>
> **1 · The input half is not merely designed — it is byte-verified today.** All seven packet
> files exist in the shared corpus and **all seven digests match** the values the manifest
> recorded on 2026-08-18, re-computed here four days later. All eleven common files are present.
> The population is fixed at **65 units / 109 panels**, digest reproduced. **Nothing in
> `1 · INPUT READY` is blocking, and no prior record had checked the packet digests against
> disk.**
>
> **2 · 🔴 The two Scientists do not exist, and the gap is not registration paperwork — it is
> identity.** `ACTOR_ID` for both reads the literal string `UNRESOLVED`, `STATUS`
> `NOT_REGISTERED`. Their `ACTOR_ID`s are declared *"FIXED on canonical execution of
> `CAND-20260818-SCIENTIST-AB-SPEC`"* — a candidate whose own state line reads **`READY FOR
> MIRROR REVIEW (revision 6) — no approval requested, granted or implied`**. The actors are not
> waiting to be registered. **The act that would give them names has not been reviewed.**
>
> **3 · 🔴 A blocker no prior Scientist record surfaced: L2 is SUSPENDED, and the suspension is
> upstream of everything.** `controlled_benchmark_ab.md` P-3 records it — *"L2 **SUSPENDED** by
> the C-9 hold (operator, 2026-08-17) — this protocol does not lift it"* — and
> `PROPOSAL-C9-STATE-MODEL` carries the hold in its own front matter. Measured: **0 of 21
> capability rows in the registry are `VERIFIED`.** Assignment runs on `VERIFIED` capabilities.
> **No decision on any file lifts this hold**, and the only operator decision on `main` is about
> something else.
>
> **4 · 🔴 The registry's Scientist binding is against a blob that no longer exists at the tip.**
> The card records `ROLE_CONTRACT_HASH 4d075b3f…` — which I matched to
> `refs/heads/orchestrator:roles/scientist.md` — while the contract at `main` **and** at this
> HEAD hashes to `dea0d816…`. The recorded `FINGERPRINT ce3c0d94…` likewise does not match what
> composes today, `b66959cd…`. **An actor registering this afternoon and composing its
> fingerprint in situ, exactly as the dispatch block requires, would produce two values that
> disagree with its own card.** This is new, technical, small, and sits directly on the
> registration path.
>
> **5 · The join barrier is definable to the instant and mechanised nowhere.** § 4 states it as
> six predicates over two receipts. Measured across **47 refs with a passing positive control**:
> `JOIN-BARRIER` **0/47**, `first_pass/` **0/47**, any freeze receipt **0/47**,
> `unresolved_disagreements.md` **0/47**, `ledger/events/` **0/47**. `verify-freeze` is strictly
> unary. **Nothing in this repository can be asked whether both are frozen.**

---

## TASK_STATUS

```
TASK_ID          FIRST_SCIENTIST_PILOT_READINESS_AUDIT_v1
MODE             READ_ONLY AUDIT · no Scientist activation · no paper read · no execution ·
                 no actor created · no contract issued · no lease taken · no surface built ·
                 no freeze run · no candidate opened
STATE            COMPLETE — the six requested sections are answered and the final question is
                 answered in § 7. Every answer that could be measured was measured; every
                 answer that is a judgement is marked as one, with the party who owns it.

EXECUTED         4 prior records read in full (FIRST-WWOX-PAPER-PILOT-DESIGN-001,
                 SCIENTIST-ACTIVATION-READINESS-001, SCIENTIST-FIRST-PILOT-EXECUTION-CONTRACT-001,
                 SCIENTIST-FIRST-REAL-PAPER-PILOT-001) · controlled_benchmark_ab.md §1 and §7 ·
                 scientist_reading_modes.md front matter · roles/scientist.md front matter ·
                 MODE_A.md / MODE_B.md / ASSIGNMENT.scientist-a.md constraint clauses ·
                 DEC-20260822 via `git show main:` · CAND-20260818 state line ·
                 PROPOSAL-C9-STATE-MODEL hold · runtime/orchestrator_lease.md ·
                 agent_card_registry via `git show refs/heads/orchestrator:`
                 — and 27 executable measurements:
                 git identity · lease derivation + --check + TTL extraction · scientist
                 fingerprint composition · role-contract hash at 3 refs · packet digest
                 re-verification 7/7 against disk · common-file presence 11/11 · population
                 parse and count by kind · spec/manifest/population digests · manifest _state
                 and null-field parse · seat file and directory enumeration · corpus count
                 top-level and recursive · forbidden-path derivation recomputed at 3 refs and
                 set-differenced both directions · paper-identifier counts over 7 instruction
                 files and 4 untracked records · all-refs sweep over 47 refs for 6 artifacts,
                 with positive control · delivery-instrument sweep over 3 script roots ·
                 verify-freeze arity · cmd_build templating check · ledger enumeration ·
                 capability-row status census · 3-worktree survey with per-path presence ·
                 dirty-blob digest comparison across the two reader worktrees · LINT ·
                 receipts verify · growth anchors
NOT EXECUTED     no Scientist created, spawned, contacted, assigned, registered or activated ·
                 no paper opened or read · no surface built, verified or frozen · no candidate
                 opened · no Task Contract written · no lease taken · no path under governance/
                 roles/ framework/ ledger/ runtime/ disease-models/ modified · no schema, field
                 or vocabulary created in any normative file
FILES ADDED      exactly one — this file
```

---

## 0 · PIN

### 0.1 · Measured, not inherited

| Field | Measured value | Command |
|---|---|---|
| branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `b72af2f25d42c3cafb781d42b66ef3a1761cdb66` | `git rev-parse HEAD` |
| vs `main` (`788c357d…`) | 2 behind · 41 ahead | `git rev-list --left-right --count main...HEAD` |
| working tree | 4 untracked files, all prior records of this seat | `git status --porcelain` |
| lease | **`ACTIVE by derivation: 0`** — 5 rows, 2 STALE, 3 RELEASED | `framework/scripts/lease_state.py` |
| scientist fingerprint | `b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a` | `governance_fingerprint.py compose --role scientist` |
| corpus | 174 top-level entries · **654 files recursive** | `ls` and `find -type f` |
| LINT · receipts · growth | `PASS` · `128 chained, tail anchored` · `PASS` | the three scripts in `CLAUDE.md` § 3 |

`CLAUDE.md` § 0: no ACTIVE lease and no runtime inventory ⇒ `BOOTSTRAP_MODE`. This session is not
Orchestrator, issues nothing, creates no actor and activates no Scientist. Its single act —
writing one file under `learning/plan/` — traces to **H.1 `WORK_COMMIT`**.

### 0.2 · The health layer is green and it is not what is being audited

`LINT PASS`, `128` chained receipts with the tail anchored, growth anchors `PASS` over
`claims=39 · papers=70 · corpus=356 · literature=390`. **Not one item on the blocker list in § 5
is a failure of the instrument layer.** Stating this first prevents the audit's `NOT READY` from
being read as a claim that something is broken. Nothing is broken. Things are unbuilt, unnamed
and undecided, which is a different condition with a different remedy.

---

## 1 · INPUT READY

**Verdict: ✅ READY — with one artifact unwritten, and the unwritten artifact is `F0` itself.**

### 1.1 · Paper

| Check | Measured |
|---|---|
| identity | `PMID 42397075 · doi 10.1093/brain/awag239 · Brain 2026` |
| packet present | ✅ **7 of 7** source files exist in `<repo-root>/files/fulltext` |
| packet **unaltered** | ✅ **7 of 7 sha256 MATCH** the manifest's `SOURCE_FILES[].sha256`, whose `verified_on` is `2026-08-18` — recomputed here at `2026-08-22` |
| bytes | `3 341 414` (PDF) · `91 848` (text surface) · `74 416 / 250 075 / 4 084 016 / 173 539 / 456 041` (five supplements) |
| corpus stable | 174 top-level / 654 recursive — unchanged from the census figure |

```
MATCH  files/fulltext/PMID42397075_Aqeilan2026.pdf                              b6b44816…
MATCH  files/fulltext/PMID42397075_Aqeilan2026_fitz.txt                         9c48aa09…
MATCH  files/fulltext/PMID42397075_Aqeilan2026_assets/brain-2025-03809-File008.pdf
MATCH  files/fulltext/PMID42397075_Aqeilan2026_assets/brain-2025-03809-File009.pdf
MATCH  files/fulltext/PMID42397075_Aqeilan2026_assets/brain-2025-03809-File010.pdf
MATCH  files/fulltext/PMID42397075_Aqeilan2026_assets/brain-2025-03809-File011.pdf
MATCH  files/fulltext/PMID42397075_Aqeilan2026_assets/brain-2025-03809-File012.pdf
                                                     → match 7 · mismatch 0 · missing 0
```

**This check had not been run before.** Prior records established that the packet was *listed*;
this one establishes that what is on disk today is what was digested four days ago. `files/`
is gitignored, so no commit covers these bytes and nothing but this comparison could have caught
a swap. **It is the single most decay-prone input object and it is clean.**

⚠️ Two requirements remain open and neither is a byte:

- **version of record** — the packet is an accepted manuscript (`brain-2025-03809-*`). A
  retraction / version check at the pin is owed, is metadata-only, and is Plan's to run under
  § 28 because it decides nothing about meaning.
- **single ownership** — no reading of this paper in flight in another checkout. Checkable only
  at the moment of selection, and stale the instant after.

### 1.2 · Population

**Verdict: ✅ READY — enumerated, digested, reproduced here.**

```
OBJECT    framework/eval/benchmarks/BENCH-AB-001/population/evidence_units.json
DIGEST    b41c7b9f432e48c74eb79be08b6d544f534aba9d0560063b1ee48f851e0b403a   ← reproduced
COUNTS    units 65 · sub_units 109 · panels 109
BY KIND   main_figure 6 · main_table 0 · main_results_section 7 · main_methods_section 2
          supplementary_figure 10 · supplement_methods_section 24
          supplement_table_section 7 · source_data_blot 9
EMPTY     File008 (author contributions) — declared, with a reason, outside the denominator
```

`main_table: 0` is a **measured zero under a declared rule**, not an omission. The rules are
typographic and revision 2 — rebuilt after a Mirror finding that a fixed 3600-character caption
window ran 925 characters into the next figure and reported twelve panels for a caption printing
six. The current rule runs a caption to the next match of its own rule.

🔴 **And that is the automation ceiling, restated as a measurement.** The population rules encode
this publisher's typesetting: `font_contains "Aptos Display"`, `size 15.77`, `size 20.27`,
`size 15.96`, `size 18.0`, `size 12.0`, `size 8.04`, `size_tolerance 0.05`, across 6 declared
sources. **Nothing in the repository derives those constants, and a wrong one does not fail
loudly — it produces a population short by sections.** For *this* paper they are measured and
reviewed. For any other paper, a human measures them before anything else can happen.

### 1.3 · Surface

**Verdict: ⚠️ SPECIFIED, NOT BUILT — and the F0 artifact does not exist.**

| Object | State |
|---|---|
| `surface_spec.json` | ✅ present · `spec_version 2` · digest `e7c2715b…` |
| allowlist complete | ✅ `source_files` 7 · `common_files` 11 · `per_actor_files` 2 per actor · `empty_dirs` 4 · `expected_output_paths` 5 · `expected_output_prefixes` 1 · `content_scan` declared |
| the surface itself | 🔴 **not built** — `build` has never run; no surface tree exists |
| `benchmark_manifest.json` | 🔴 **`_state: "PREPARED — NOT FROZEN"`**, `FROZEN_SHA256: null`, both `HANDOVER` blocks `null`, `EVALUATION_POPULATION.sha256: "DERIVED_AT_BUILD"` |
| the seat's output half | 🔴 **absent** — `first_pass/` · `frozen/` · `comparison/` · `audit/` · `adjudication/` · `outcome/` all missing |

The seat holds exactly **10 files in 3 directories**: 7 instructions, 1 population, the spec and
the manifest. **Its entire input half and none of its output half — the shape of a benchmark
fully prepared and never handed over.**

**This is not a defect.** F0 is a build-time act performed immediately before handover. The
instrument exists and the artifact does not, because handover has not happened. It is listed
here so that *"F0: mechanised"* is never read as *"F0: done."*

### 1.4 · Sources

**Verdict: ✅ READY — the allowlist resolves completely against disk.**

`common_files` **11 of 11 present, 0 missing**. Per-actor files defined for both actors and
mapping to the same two surface paths — `ASSIGNMENT.md` and `benchmark/MODE_DIRECTIVE.md` —
which is what makes *exactly two files differ* a checkable assertion rather than a hope.

Instruction files, paper-identifier hits, `grep -c -i -E '42397075|awag239|aqeilan|10\.1093/brain'`:

| File | Hits | Transfers to another paper |
|---|---:|---|
| `MODE_A.md` | **0** | ✅ unchanged |
| `MODE_B.md` | **0** | ✅ unchanged |
| `SURFACE_CLAUDE.md` | **0** | ✅ unchanged |
| `ASSIGNMENT.scientist-a.md` | 1 | ✏️ |
| `ASSIGNMENT.scientist-b.md` | 1 | ✏️ |
| `BENCHMARK_INSTRUCTIONS.md` | 7 | ✏️ |
| `OUTPUT_SCHEMA.md` | 6 | ✏️ |

**The three files carrying the reasoning carry no paper; the four that are paper-bound are
already written for this one.** Prompt-authoring cost for this pilot: **zero**. `cmd_build`
contains exactly one `shutil.copyfile` and no substitution of any kind, so for any *other* paper
those four must exist as concrete bytes before `build` runs, and nothing generates them.

---

## 2 · SCIENTIST A READY

**Verdict: 🔴 NOT READY — the work is fully specified and the worker does not exist.**

### 2.1 · Artifacts

**Verdict: ✅ DEFINED — four objects, every one on an existing carrier.**

```
<SURFACE>/disease-models/wwox/research/deepdive_manifests/PMID42397075.json   schema_version 2
<SURFACE>/disease-models/wwox/research/fulltext_dossiers/PMID42397075.md      the readable twin
<SURFACE>/output/claim_candidates.md                                         canonical claim form
<SURFACE>/output/receipt.json                                                the reading's receipt
```

All four appear in the spec's `expected_output_paths`, so `verify` can assert the slots empty at
handover and populated after. **The pilot creates no schema, no field and no vocabulary** — every
field MODE A must produce already has a carrier. Manifest sections asking about a corpus this
surface does not contain (`multihop`, `corpus_crossquery`, `group_assessment`) are waived with the
surface boundary named as the reason.

### 2.2 · Constraints

**Verdict: ✅ DEFINED · ⚠️ one is procedural and says so.**

Read from `MODE_A.md` directly: *"'Read completely' is not 'read charitably.' You are not
defending the paper and you are not prosecuting it"*, and the prohibition line — *"read anything
outside this surface · communicate with the other reader · write to any canonical file"*.

| Constraint | Mechanism | Reach |
|---|---|---|
| nothing outside the surface enters | `verify`: `present ⊆ ALLOWED_PATHS`, exhaustive | **mechanical inside the surface** |
| no prior LEGEND output present | forbidden paths absent + `CONTENT_SCAN == 0` | mechanical, **and decayed** — § 5.T-4 |
| no object-store route back to LEGEND | each surface a standalone `git init` | **structural** |
| output slots empty at handover | `verify` | mechanical |
| the reader does not leave the surface | — | 🔴 **nothing enforces it** (Annex J.0). The blind path is the *default* path; departure is an act, not a wall |
| no research question, no evidence target, no anticipated conclusion | absent from every input file by design | governance — H.1, *conclusion never to order* |

### 2.3 · Freeze

**Verdict: ✅ MECHANISED — and never exercised.**

`freeze` reads `ACTOR_ID` / `BENCHMARK_ID` from the `ASSIGNMENT.md` **inside the tree** and
refuses on a command-line disagreement (exit 2), so A's tree cannot be frozen as `scientist-b`.
It refuses a tree containing a symlink. `verify-freeze` recomputes **set-wise** —
`ADDED` / `REMOVED` / `MODIFIED` enumerated, never a count comparison.

🔴 **Zero freeze receipts exist on any of 47 refs** (`RECEIPT-scientist`: 0/47, positive control
`CLAUDE.md`: 47/47). The command has never been run against an actor tree. **A mechanism that has
never executed is a design, and its first execution is also its first test.**

### 2.4 · The actor

**Verdict: 🔴 NOT READY.** Read from `refs/heads/orchestrator:runtime/agent_card_registry.md`:

```yaml
ACTOR_ID:  UNRESOLVED   # proposed: scientist-a
WORKTREE:  lettore
STATUS:    NOT_REGISTERED
LAST_SEEN: UNKNOWN
DIRTY_WORK: yes — 1 modified file
```

And the worktree it names, measured today:

| | `lettore` (A) | `lettore-b` (B) | `lettore-c` (C, for contrast) |
|---|---|---|---|
| behind `main` / ahead | **201 / 0** | **203 / 0** | 65 / 0 |
| dirty | 1 file | 1 file | clean |
| `governance/` | ABSENT | ABSENT | **PRESENT** |
| `roles/scientist.md` | ABSENT | ABSENT | **PRESENT** |
| `governance_fingerprint.py` | ABSENT | ABSENT | **PRESENT** |
| `scientist_reading_modes.md` | ABSENT | ABSENT | ABSENT |
| `BENCH-AB-001` | ABSENT | ABSENT | ABSENT |

**A session opened in `lettore` today cannot compose its own governance fingerprint, cannot read
its own role contract, and cannot reach the protocol it would be asked to follow — because none
of those files is on the ref.** That is not a readiness gap in the pilot design; it is a
statement that the two directories named for A and B predate the laboratory that would use them.

🔴 **A finding that inverts the usual reading of `scientist-c`.** Of the three Scientist
worktrees, the only one that could host a session today is `lettore-c` — clean, and carrying
governance, the contract and the fingerprint script. The two the pilot needs are the two that
cannot. *(The registry records `scientist-c` as `0 behind, 0 ahead`; measured today it is **65
behind**. The registry is a 2026-08-17 snapshot and `main` has moved under it.)*

---

## 3 · SCIENTIST B READY

**Verdict: 🔴 NOT READY — for every reason in § 2, plus one measured contamination signal.**

B's artifacts are A's four plus `output/critical_reading.md`; its freeze mechanism is identical.
Neither is restated. What follows is only what differs.

### 3.1 · Independence

**Verdict: ⚠️ PROVABLE OF THE SURFACE · 🔴 A COUNTER-SIGNAL IN THE WORKTREE.**

What can be proved by command, once a run exists: both readers read the same bytes (`verify`,
`sha256_A == sha256_B` per path, recomputed from disk); **exactly two files differ**, and a third
differing file is a reported finding, not an assumption; nothing present outside the allowlist;
no object-store path back to LEGEND, each surface being a standalone repository.

What cannot: whether B was *told*. Three of the four channels leave a trace. The fourth — **Plan
relaying A's first pass to B before B freezes** — leaves none, and **the party the barrier
constrains is the party that operates it.** The protocol labels its own guarantee, and the label
is reproduced rather than paraphrased:

```
GUARANTEE_PROVIDED:            none by mechanism — discipline only
FAILURE_MODE_STILL_POSSIBLE:   Plan reads or relays A's first pass to B before B freezes
DETECTION:                     FREEZE_TIMESTAMP_UTC + SURFACE_COMMIT, inspected against each
                               other — VISIBLE AFTER THE FACT, never prevented
RECOVERY:                      the benchmark is void for the second reader; the outcome says so
```

🔴 **And the counter-signal, verified independently here.** The two worktrees whose entire purpose
is independent parallel reading hold the **same uncommitted file with the same digest**:

```
lettore   M disease-models/wwox/research/deepdive_manifests/PMID42422765.json
lettore-b M disease-models/wwox/research/deepdive_manifests/PMID42422765.json
both      sha256 6c3fe60fa09cdb8f4b957a20801751673e5bad66d84fb51b843ef60bcf888b83
```

Byte-identical, in both, uncommitted, since 2026-08-17. **Whatever wrote them reached both.**
The design sidesteps this entirely by reading in standalone repositories elsewhere — but the
hypothesis is testable, untested, and **should be tested before independence is claimed of these
two directories**, because a claim of isolation that is contradicted in the only place it has
ever been observable is not a claim worth carrying into an experiment about isolation.

### 3.2 · Blindness

**Verdict: ⚠️ AVAILABLE — under a route nobody has declared.**

Two independent implementations exist and the programme has been reasoning as if only one did.

| Route | Mechanism | Strength | Available today |
|---|---|---|---|
| **C-1 NULL PRIOR** | a paper LEGEND has written nothing about | **absolute against every channel** — the prior output does not exist to be read | 🔴 no — requires an acquisition not started |
| **SURFACE_ALLOWLIST** | build from an allowlist into a standalone repository sharing no object store | **absolute inside the surface, procedural outside it** | ✅ yes |

Measured: the repository holds **36 tracked paths naming this paper at HEAD** (excluding
`governance/candidates`, which the recorded command excludes wholesale). Under
`SURFACE_ALLOWLIST` those 36 remain reachable by absolute path — J.0 grants no runtime
enforcement. Under `C-1` they would not exist.

**Neither route is declared in the manifest.** The audit's requirement is that one be named — a
run that names neither is a run whose blindness claim has no referent. **This is `Q-20`, and it
is the operator's.**

B's mode-specific clause is present and reads, verbatim from `MODE_B.md` line 82: *"read anything
outside this surface · communicate with the other reader · attempt to reconstruct what the other
reader concluded"*. All **eleven** critical axes are present in the directive.

🔴 **One exclusion the design cannot make.** Both mode directives are described in full inside
`scientist_reading_modes.md`, a **common** file that could not honestly be withheld from either
reader. The manipulated variable is not *knowledge of the two modes*; it is **which directive is
addressed to you**.

### 3.3 · Freeze

Identical to § 2.3, with one asymmetry that must be declared **before** the run rather than
discovered after it: **MODE B produces an `OMISSION` class MODE A structurally cannot**, because
MODE A is never asked what is absent. A table counting `OMISSION` entries per reader will show B
"finding more" for a reason having nothing to do with either reader. Until that is answered,
`OMISSION` is reported **outside** any A-vs-B column.

---

## 4 · JOIN BARRIER

> **Defined exactly, as the dispatch requires. Then measured.**

### 4.1 · The definition

**A's and B's outputs may first become visible together at the instant `T_join`, where**

```
T_join = max( RECEIPT_1.FREEZE_TIMESTAMP_UTC , RECEIPT_2.FREEZE_TIMESTAMP_UTC )
```

**and only once all six predicates below hold. Not one instant earlier.**

| # | Predicate | Decided by |
|---|---|---|
| **J-1** | **both** receipt files exist on disk | file existence — the barrier is over the *pair*, and a pair is not a pair until its second element exists |
| **J-2** | each receipt re-verifies against its own tree, set-wise | `verify-freeze --receipt … --surface …` ×2 — `ADDED`/`REMOVED`/`MODIFIED` all empty, **enumerated, never counted** |
| **J-3** | each receipt's identity matches the `ASSIGNMENT.md` inside the tree it froze | `freeze`/`verify-freeze` identity check — a receipt pointed at the wrong actor's tree fails on identity, not merely on digests |
| **J-4** | no content of **either** tree was read by Plan before `T_join` | 🔴 **no mechanism** — a dated declaration, § 4.3 |
| **J-5** | neither import into `first_pass/<ACTOR_ID>/` occurred before J-1 held | ordering of the import acts; the import is byte-identical and the receipt digests are the check |
| **J-6** | the barrier itself is recorded in a durable artifact carrying both `TREE_SHA256`, both `FREEZE_TIMESTAMP_UTC` and the J-4 declaration | 🔴 **no such artifact exists on any ref** |

### 4.2 · Three things the barrier is not

- **It is not a freeze.** F0, F1 and F2 freeze bytes. F3 freezes nothing; it asserts a
  relation between two objects. `verify-freeze` takes `--receipt` ×1 and `--surface` ×1 —
  **there is no arity in which the pair is the object.**
- **It is not the moment the readers see each other.** They never do. Their passes are over and
  frozen. The barrier governs when a **third party** — Plan, then Orchestrator, the blind
  locator audit and Mirror — may hold both artifacts at once.
- **It is not indexed by actor.** The protocol: *"whichever finishes first is frozen first; the
  second is not shown the first until its own freeze is recorded."* 🔴 **Indexing F1/F2 by actor
  name would either idle B until A declares, or make B's completion timing a function of A's —
  and a schedule conditioned on the other reader is a channel, thin but real.** The actor is a
  **field** of each freeze, never its name.

### 4.3 · What is missing, measured

Across **47 refs**, positive control `CLAUDE.md` returning **47/47**:

```
JOIN-BARRIER                    0 / 47
first_pass/                     0 / 47
BENCH-AB-001/frozen             0 / 47
RECEIPT-scientist               0 / 47
comparison/unresolved_disagreements.md   0 / 47
ledger/events/                  0 / 47
```

*(The first run of this sweep returned **0/47 for the positive control** — the `for r in $refs`
loop does not word-split in zsh. The result is reported from the corrected run. A sweep whose
control fails is a false negative wearing a verdict, and it is the reason a control is run at
all.)*

🔴 **`ledger/events/` at 0/47 is a second-order finding.** § 29.3 makes the consolidated event
ledger Mirror's **primary** R4 analysis surface. It does not exist on any ref. Mirror can be
handed the frozen artifacts and the comparison matrix instead, and that is usable input — **but
it is a declared deviation, not the normal route, and it belongs in the outcome as one.**

### 4.4 · The one improvement that costs nothing

**J-6 is satisfiable today by one Plan-authored file** — `frozen/JOIN-BARRIER.md` carrying both
tree digests, both freeze timestamps and Plan's dated declaration for J-4, with imports ordered
so that neither `first_pass/` import happens until both receipts exist. **No tool change, no
schema, no approval dependency.**

It does not remove the conflict of interest. It converts a violation from *a silence* into *a
false statement in a durable artifact*. **That is the largest available improvement to the only
guarantee in the design with no mechanism at all.** The improvement that would actually remove
the conflict — the freeze operator is not the comparison author — requires an actor the pilot
does not have.

---

## 5 · BLOCKERS

**16 blockers. 4 technical, 6 governance, 6 human decision. Not one of them is the paper, the
prompts, or a tool for the reading itself.**

### 5.1 · TECHNICAL — something must be built or repaired

| # | Blocker | Measurement | Human-substitutable? |
|---|---|---|---|
| **T-1** | **No instrument delivers anything to an actor.** Orchestrator assigns through Task Contracts, which are *files*; a file nobody opens has assigned nothing | `grep -rl -i -E 'sendmessage\|notify_actor\|deliver_message\|spawn_agent\|open_session'` over `framework/scripts/`, `governance/scripts/`, `scripts/` → **0 files**. The broader `dispatch\|spawn` sweep returns exactly one hit: `multiprocessing.get_context("spawn")` in a receipts test | ✅ **yes** — a human opens two sessions in two directories |
| **T-2** | **No instrument expresses the join.** Nothing can be asked *"are both frozen?"* | `verify-freeze --help` arity: `--receipt` ×1, `--surface` ×1 | ✅ **yes** — § 4.4, one Plan artifact |
| **T-3** | 🔴 **The registry's Scientist binding points at a superseded blob.** An actor registering today and composing its fingerprint in situ produces values disagreeing with its own card | recorded `ROLE_CONTRACT_HASH 4d075b3f…` = `refs/heads/orchestrator:roles/scientist.md`; at `main` **and** HEAD the contract hashes `dea0d816…`. Recorded `FINGERPRINT ce3c0d94…` vs composed today `b66959cd…` | ⚠️ **repair, not substitution** — reconcile at registration |
| **T-4** | 🔴 **The forbidden-prior-output list is a transcription and it has decayed.** The check still passes; it passes over less | listed **23**. Derived at the spec's own `BASE_HEAD cbce3016`: **20** (the derivation note says 21). At `main`: **32**. At HEAD: **36** — of which **15 are unlisted, 8 of them outside the benchmark seat** | ⚠️ **repair** — re-derive at the pin at build time |

🔴 **T-4 is decaying while it is being audited.** Two of the four untracked records in this
working tree name the paper (`SCIENTIST-FIRST-PILOT-EXECUTION-CONTRACT-001`: 14 hits;
`SCIENTIST-FIRST-REAL-PAPER-PILOT-001`: 3 hits), and this file makes a third. Committing this
seat's own analysis pushes the derived set from 36 to 39 and the unlisted-outside-seat count from
8 to 11. **A list transcribed from a ref that is 41 commits stale cannot track a repository that
writes about the paper faster than the list is edited. The repair is a command run at build time
whose output is recorded — never an enumeration copied from an earlier run of it.**

### 5.2 · GOVERNANCE — a rule blocks, and no amount of work removes it

| # | Blocker | Measurement |
|---|---|---|
| **G-1** | **No binding Scientist role contract exists.** `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` selects **`OPTION B · ACTIVATION_NOT_CONFIRMED`**: the four role contracts *"remain `PROPOSED`"* and *"a new, explicit activation act is required before any actor relies on these contracts as binding"* | read via `git show main:`; `roles/scientist.md` front matter: `status: PROPOSED` |
| **G-2** | **The protocol governing the experiment is not canonical.** Both `controlled_benchmark_ab.md` and `scientist_reading_modes.md` declare `normative: yes` **and** `status: PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC` | front matter of both |
| **G-3** | 🔴 **The candidate that would fix G-2 has not been reviewed.** Its own state line: **`READY FOR MIRROR REVIEW (revision 6) — no approval requested, granted or implied`**; `HUMAN_APPROVAL: NONE — not requested, not granted, not implied` | `CAND-20260818-SCIENTIST-AB-SPEC.md` |
| **G-4** | 🔴 **The two actors have no names.** `actor_id_status` — `scientist-a: FIXED on canonical execution of CAND-20260818`; `scientist-b: FIXED on the same execution`. Registry: `ACTOR_ID: UNRESOLVED`, `STATUS: NOT_REGISTERED`, both | `roles/scientist.md` front matter + `refs/heads/orchestrator:runtime/agent_card_registry.md` |
| **G-5** | 🔴 **L2 is SUSPENDED by the C-9 hold (operator, 2026-08-17), and nothing lifts it.** Assignment runs on `VERIFIED` capabilities. Measured: **0 of 21 capability rows in the entire registry are `VERIFIED`** — 21 `UNVERIFIED`. The Scientist block is `# COMMON TO ALL THREE`, six rows, all `UNVERIFIED` | `PROPOSAL-C9-STATE-MODEL` front matter: *"hold: … L2 suspended; the status/C-8 batch frozen pending a later operator decision"*; `controlled_benchmark_ab.md` P-3; registry status census |
| **G-6** | **No lease, therefore no assignment.** `ACTIVE by derivation: 0` — 5 rows, 2 STALE, 3 RELEASED, last expiry `2026-08-18T15:03:41Z`. `ledger/tasks/` holds `plan/` only: **zero Scientist Task Contracts have ever existed** | `lease_state.py`; `find ledger/tasks -type f` → 5 files, all under `plan/` |

**The protocol's own precondition table, re-read at this HEAD — all seven unmet:**

```
P-1  protocol + reading modes canonical ............ not canonical
P-2  scientist-a / scientist-b registered .......... NOT_REGISTERED, ACTOR_ID UNRESOLVED
P-3  Scientist capabilities VERIFIED at L2 ......... all UNVERIFIED; L2 SUSPENDED (C-9 hold)
P-4  ORCHESTRATOR_LEASE ACTIVE .................... 0 by derivation
P-5  C-2 preconditions declared at registration .... pending registration
P-6  two Task Contracts issued ..................... none exists
P-7  surfaces built, verified, manifest frozen ..... not built
```

🔴 **G-5 is the blocker no prior Scientist record surfaced, and it sits above the others.** Prior
records reported the capabilities as `UNVERIFIED` — true, and incomplete. They are unverified
**because the process that verifies them is under an operator hold**, and the hold is not
mentioned in any of the four records this audit reviewed. Registration does not unblock it.
Building the surface does not unblock it. **Only the operator does.**

### 5.3 · HUMAN DECISION — nobody but the Operator can close these

| # | Decision | Why only the operator | Blocks |
|---|---|---|---|
| **H-1** | **What form does the activation act of `DEC-20260822` take?** Everything downstream waits on an object nobody has described | H.1 routes governance to the Operatore; the decision itself names it as required and does not specify it | G-1 → all |
| **H-2** | **Lift, or do not lift, the C-9 hold on L2** | The hold's `status_transition_owner` is the operator | G-5 → P-3 → assignment |
| **H-3** | **Send `CAND-20260818` to Mirror review; approve or refuse** | `CHANGE_CLASS: MAJOR`; H.1 — MAJOR approval → Operatore | G-2, G-3, G-4 |
| **H-4** | **Which blindness route: `SURFACE_ALLOWLIST` or `C-1 NULL PRIOR`?** | The only decision that determines whether this pilot needs an acquisition at all | § 3.2; upstream of F0 |
| **H-5** | **Who operates F3, given that the party the barrier constrains is the party that operates it?** | Staffing; a third party does not exist and creating one is not Plan's | J-4, J-6 |
| **H-6** | **Forward ownership of the identical uncommitted blob in `lettore` and `lettore-b`** | Open as `CONTENT RESOLVED · FORWARD OWNERSHIP UNRESOLVED` since 2026-08-17; `BOOTSTRAP.md` forbids proceeding past a point that could lose uncommitted work | any sync of A's and B's worktrees |

Four further questions are recorded and **do not block the start**: whether a declared partial
reading may produce a commit candidate; whether Mirror receives the absent event ledger or the
frozen artifacts as a declared deviation; what `scientist-c`'s function is; and how the `OMISSION`
asymmetry is handled in comparison. Each becomes blocking at a later step, none at F0.

### 5.4 · The dependency chain, which is the actual answer

The 16 blockers are not a list. They are a chain, and its ordering is why the verdict is what it
is:

```
H-1 activation act ─┐
H-3 Mirror + approval of CAND-20260818 ─┤
                    ├─→ G-2 protocol canonical ─→ G-4 ACTOR_IDs fixed ─→ P-2 registration
H-2 lift C-9 hold ──┴─→ G-5 L2 runs ─────────────→ P-3 capabilities VERIFIED
                                                          │
                              G-6 lease ACTIVE ───────────┼─→ P-6 two Task Contracts
                                                          │
H-4 blindness route ──→ F0 build · verify · population · freeze  (P-7)
                                                          │
                              T-1 delivery (human act) ───┴─→ the two readings
```

**Every technical blocker is downstream of a human decision, and three human decisions are
upstream of everything.** Nothing in the chain can be started in parallel with the top of it
except F0, and F0 requires H-4.

---

## 6 · FINAL STATUS

# 🔴 NOT READY

### 6.1 · Why not `READY WITH HUMAN GATE`

That status asserts a specific predicate: **everything is prepared, and the only missing thing is
a human saying yes.** It is false here, and the discriminating test is simple — *if the Operator
authorized everything in one sentence right now, could the pilot start?*

**No.** After every authorization there would still remain: a registration that has never
happened for either actor, an L2 verification pass that has never run for any capability, two
worktrees 201 and 203 commits behind that cannot read their own contract, a registry binding to
a superseded blob, a surface that has never been built, and a manifest that has never been
frozen. **Those are work, not consent.**

`READY WITH HUMAN GATE` is the status the pilot **reaches** once the chain in § 5.4 is executed —
at which point the remaining gate is genuinely a human one, because delivery is a human act. It
is the correct label for the state *after* the work and the wrong label for the state now.

### 6.2 · Why not simply "blocked everywhere"

Because the input half is genuinely ready and that is a real result, not a consolation. Seven
packet digests match after four days. The population is fixed at 65 units and 109 panels under a
reviewed rule. Eleven common files resolve. Three of the seven instruction files are
paper-independent and the other four are already written for this paper. LINT passes, 128
receipts chain to an anchored tail, growth anchors pass.

**Eight records have carried *"the pilot has no paper."* Measured at this HEAD, that is not
true.** The paper is acquired, specified, digest-verified and denominated. What is missing is
that **nothing in this repository can hand a directory to a reader, nobody holds the lease that
would let them, the two readers have no names, and the process that would verify they can read
is under an operator hold.**

### 6.3 · The status per section, so the verdict is decomposable

| Section | Status |
|---|---|
| 1 · INPUT READY — paper | ✅ **READY** — 7/7 digests match disk today |
| 1 · INPUT READY — population | ✅ **READY** — 65 / 109, digest reproduced |
| 1 · INPUT READY — surface | ⚠️ **SPECIFIED, NOT BUILT** — F0 artifact unwritten |
| 1 · INPUT READY — sources | ✅ **READY** — allowlist resolves 11/11 and 7/7 |
| 2 · SCIENTIST A | 🔴 **NOT READY** — actor `UNRESOLVED` / `NOT_REGISTERED`; worktree 201 behind |
| 3 · SCIENTIST B | 🔴 **NOT READY** — as A, plus an unexplained shared uncommitted blob |
| 4 · JOIN BARRIER | ⚠️ **DEFINABLE, UNMECHANISED** — 0/47 refs; free repair available |
| 5 · BLOCKERS | 🔴 **16** — 4 technical · 6 governance · 6 human decision |

---

## 7 · THE FINAL QUESTION

> *"If the Operator disappeared for 4 hours, what exactly would stop and why?"*

### 7.1 · The literal answer

> **Nothing would stop, because nothing is running.**

This is not a rhetorical answer; it is the measured one. There is no run in flight to interrupt:

```
ACTIVE leases ......................... 0
Scientist Task Contracts ever issued .. 0
surfaces built ........................ 0
freeze receipts on 47 refs ............ 0
first_pass/ on 47 refs ................ 0
ledger/events/ on 47 refs ............. 0
```

Four hours of absence changes no state in this repository. The pin does not drift: the corpus
digest is stable and seven packet files matched their 2026-08-18 digests after four days, not
four hours. **The decision queue is the only thing that would stall, and it is already stalled.**

### 7.2 · The useful answer — what would stop **if the pilot were running**

The question is worth answering counterfactually, because the answer names a real design
property. **Three things would stop, and they stop for three different reasons.**

**① The lease would lapse, and the run would become an `INFRASTRUCTURE_FAILURE`.**
Observed lease durations in the ledger: **4, 40, 40, 60 and 60 minutes** — maximum **one hour**.
Renewal is `PROCEDURAL`: *"Acquisition, renewal and the terminal row are still authored by hand.
Nothing compels the Orchestrator to record an acquisition, and **nothing runs between turns**."*
A four-hour absence spans at least four lease lifetimes. Without an ACTIVE lease no Task Contract
governs the work, which is enumerated by name as an infrastructure failure — *"the lease lapses
mid-run and no Task Contract governs the work."* **This is the sharpest answer: the pilot's
authorization has a one-hour half-life and its renewal is a human act.**

**② Delivery would stop, because delivery is a human act.** No script in this repository opens
a session in a surface directory — measured, 0 files across three script roots. Whatever has not
been handed over at hour zero is not handed over at hour four.

**③ Every operator decision would stop** — the six in § 5.3. None has a deadline, so a four-hour
absence costs nothing there that a four-day absence has not already cost.

**What would *not* stop, and this is the part worth noticing.** A reader already inside its
surface, with `INTERACTION_MODE: AUTONOMOUS_COMPLETE`, has everything it needs: the packet, the
discipline set, the validators, its directive. It is designed to need nobody. **The reading is
the one part of this pilot that survives the operator's absence.** What cannot survive it is the
scaffolding around the reading — the lease, the delivery, the freeze taken on a declaration, the
join.

### 7.3 · The finding underneath the question

> **Every part of this pilot that is autonomous is a part nobody has authorized, and every part
> that is authorized requires a human to be present for it.**
>
> The reading is autonomous and cannot start. The lease renews only when someone types. The
> freeze must be taken *on* the completion declaration and *before* the content is read — so a
> reader declaring complete at hour one of a four-hour absence leaves its tree editable for three
> hours with no freeze standing between the declaration and the content. The join barrier is a
> promise made by the party it constrains.
>
> **A four-hour absence does not break this laboratory. It reveals that the laboratory has never
> run long enough for four hours to matter — and that the first thing an operator should want
> from the first pilot is not the reading, but a measurement of how long the run survives
> without them.**

---

## 8 · PRIOR CLAIMS THIS AUDIT CORRECTS

Re-executed, not transferred. Where a prior number differs, both are given.

| Prior claim | Where | Measured here |
|---|---|---|
| *"the two verified Scientist capabilities in the repository belong to `scientist-c`"* | `SCIENTIST-FIRST-PILOT-EXECUTION-CONTRACT-001` § 6.3 / § 9.2 C-5 | 🔴 **Withdrawn. There are no verified capabilities anywhere.** `grep -c 'status: VERIFIED'` over the whole registry → **0**; 21 rows, all `UNVERIFIED`. The Scientist block is `# COMMON TO ALL THREE`, not per-actor — so `scientist-c` holds no capability the others lack |
| *"at this HEAD the same command yields **38**, of which **10** outside the seat are not on the list"* | ibid. § 1.5 | **36** and **8**. The prior count included the two `governance/candidates` paths that the spec's own recorded command excludes wholesale. The finding stands; the arithmetic was one filter short |
| *"`SOURCE_FILES[]` in the spec, 7 entries with per-file `sha256` and `bytes`" | ibid. § 1.1 (I-1) | The **spec's** `source_files[]` carry `source`/`surface`/`kind` and **no digest** — `any('sha256' in e)` → `False`. The digests live in the **manifest's** `SOURCE_FILES[]`, keyed `surface_path`. The objects exist; the carrier was misattributed |
| L2 / capability verification reported as *"UNVERIFIED, pending L2"* | all four records reviewed | **Incomplete.** L2 is not pending, it is **SUSPENDED by the C-9 hold (operator, 2026-08-17)**, recorded in `controlled_benchmark_ab.md` P-3 and in `PROPOSAL-C9-STATE-MODEL` front matter. None of the four records names the hold. It is the blocker with the fewest alternatives |
| the registry's `scientist-c` row as current state | registry, `WORKTREE_HEAD … 0 behind, 0 ahead` | **65 behind** today. The row was true on 2026-08-17; `main` has moved. The registry is a snapshot and is read here as one |
| the packet as *"present in the shared corpus"* | ibid. § 1.1, § 1.3 | **True and understated.** Presence had been checked; **byte-identity had not**. All 7 digests match their 2026-08-18 values — the strongest input result in this audit, and it was one command away in every prior record |

---

## 9 · NEGATIVE CLAIMS — each with its instrument and its expiry

| Claim | Instrument | Holds until |
|---|---|---|
| no delivery instrument exists in the repository | `grep -rl` over three script roots → **0 files**; broader `dispatch\|spawn` → 1 hit, `multiprocessing.get_context("spawn")` in a test | any such script is added |
| `JOIN-BARRIER`, `first_pass/`, any freeze receipt, `unresolved_disagreements.md`, `ledger/events/` exist on **no** ref | all-refs `git ls-tree -r --name-only "${r}"` over **47** refs, positive control `CLAUDE.md` → **47/47** | any ref adds one |
| no Scientist Task Contract has ever existed | `find ledger/tasks -type f` → 5 files, all under `plan/` | one is written |
| zero capabilities are `VERIFIED` for any actor | registry status census → 21 `UNVERIFIED`, 0 `VERIFIED` | L2 runs, which requires the C-9 hold lifted |
| `verify-freeze` cannot express a pair | `--help` arity: `--receipt` ×1, `--surface` ×1 | the CLI changes |
| `build` does no templating | `grep -c 'shutil.copyfile'` → 1, no substitution in `cmd_build` | the function changes |
| `MODE_A.md`, `MODE_B.md`, `SURFACE_CLAUDE.md` carry no paper identifier | `grep -c -i -E` → 0, 0, 0 | those files change |
| the packet is unaltered since 2026-08-18 | 7/7 sha256 recomputed against the manifest | the next write to `files/fulltext/` |
| the seat has no output half | `find` → 10 files, 3 directories | handover |
| 0 leases ACTIVE | `lease_state.py`, derived from `EXPIRES_AT`/`RELEASED_AT` against the clock, not from the stored field | a lease is acquired |

---

## 10 · VALIDATION

### 10.1 · Dispatch compliance

| Constraint | Status | Evidence |
|---|---|---|
| **READ-ONLY** | ✅ | one file added under `learning/plan/`; no path under `governance/`, `roles/`, `framework/`, `ledger/`, `runtime/`, `disease-models/` touched |
| **no execution** | ✅ | no surface built, verified or frozen; no benchmark command run against any actor tree; no lease taken; no contract issued |
| **no paper reading** | ✅ | no paper opened. The only paper bytes touched were **hashed and counted** — `sha256` over 7 files — never read for content |
| 1 · INPUT READY — paper · population · surface · sources | ✅ | § 1.1–1.4, each measured |
| 2 · SCIENTIST A — artifacts · constraints · freeze | ✅ | § 2.1–2.3, plus § 2.4 on the actor |
| 3 · SCIENTIST B — independence · blindness · freeze | ✅ | § 3.1–3.3 |
| 4 · JOIN BARRIER — *defined exactly* | ✅ | § 4.1, `T_join` plus six predicates J-1…J-6 |
| 5 · BLOCKERS — technical · governance · human decision | ✅ | § 5.1–5.3, 16 blockers, plus the chain in § 5.4 |
| 6 · FINAL STATUS — one of three | ✅ | § 6 — **NOT READY**, with the discriminating test against `READY WITH HUMAN GATE` stated in § 6.1 |
| final question | ✅ | § 7 |

### 10.2 · What this record does NOT do

It does **not** select, ratify or reject a paper · create, activate, qualify, register or contact
any Scientist · issue a Task Contract · take a lease · build, verify or freeze any surface · open
a candidate or a review · write `JOIN-BARRIER.md`, `unresolved_disagreements.md` or any run
artifact · modify `surface_spec.json`, `benchmark_manifest.json` or the population · re-derive the
forbidden list into the spec (it measures the decay and prices the repair) · reconcile the
registry's stale contract hash or fingerprint · lift or interpret the C-9 hold · perform or
specify the activation act · authorize anything.

**None of it binds anyone.** § 5.3 names who would act.

### 10.3 · NEXT_TRANSITION

Nothing here authorizes a next step. Three moves are unblocked today and none needs approval:

1. **Decide the blindness route (H-4).** It is the only decision determining whether this pilot
   needs an acquisition at all, and it is upstream of F0. If the answer is `SURFACE_ALLOWLIST`,
   the input half is complete today.
2. **Write `JOIN-BARRIER` (§ 4.4).** One Plan artifact, no tool change, no dependency — the
   largest free improvement to the only guarantee with no mechanism.
3. **Re-derive the forbidden list at the pin (T-4).** A transcribed enumeration has narrowed by
   eight paths without the verdict line changing, and this audit's own siblings widen the gap
   again the moment they are committed.

**And one that does need the operator, stated last because it is the one that governs the rest:
the C-9 hold suspends L2, L2 verifies the capabilities, and assignment runs on verified
capabilities. Until that hold moves, no Scientist can be assigned anything — no matter what else
is built.**
