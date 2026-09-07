---
record_type: OPERATIONAL_READINESS_PLAN
record_id: LEGEND-OPERATIONAL-READINESS-PLAN-V1
task_id: LEGEND_OPERATIONAL_READINESS_PLAN_v1
title: Operational readiness plan for the first LEGEND scientific experiment — phase 1 of the readiness review cycle
revision: 1
author: unregistered session — no role contract, no ACTOR_ID
actor_id: NOT ESTABLISHED — a session cannot resolve its own actorhood
dispatcher: operator
date: 2026-08-24
status: PROPOSED — AWAITING HOSTILE REVIEW AND FEASIBILITY REVIEW
binding: NO
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none
governance_version: 3.1.1 — read, cited, neither exercised nor modified
activation_state_governing_this_record: >
  DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE, status BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE,
  returns OPTION B `ACTIVATION_NOT_CONFIRMED`: "No actor authority may be assumed from these
  contracts." Every seat named in this plan is named as a function, never as an authority.
mandate: >
  Team mandate — LEGEND Operational Readiness Plan + Review Cycle v1, phase 1 of 4.
  Phase 2 is a hostile review, phase 3 a feasibility review, phase 4 the integrated final plan.
  This record is the object those reviews are to be run against.
measured_at: >
  branch `legend-operating-convention-v1` @ 30cb4f3fd700e2aaf6b608e363438f883ddc3760,
  working tree as found, 2026-08-24T08:11Z–08:18Z. Every figure below carries its command
  in § 12 and its class. Population figures decay; object figures do not.
consumes:
  - LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v2.md, revision 2 — blob 6bd903cb08b29da6db86467a70db127502585974
  - LEGEND_DEVELOPMENT_BOOTSTRAP_AUDIT_v1.md — blob 598afd355bd4de2a94d67c7620f10c87b4e1e59d
  - TRIAL-001-REVIEW-FINDINGS-REGISTER.md — blob ee00195fac0f7c317803120d2a5d335098c33778
  - TRIAL-002-DESIGN-V2-FINDINGS-REGISTER.md — blob 635f1b21bf61b419f673e6b2773e27514007d99b
  - LEGEND_FIRST_OPERATIONAL_TRIAL_EXECUTION_PROTOCOL_v1.md — blob d5c0d296df69ea5a14426e2da351869959983c7b
  - the state of `legend-development` — remote `development`, main @ 788c357, an ancestor of HEAD
hazard: >
  🔴 All five consumed records are UNTRACKED files. Four survive additionally as loose objects
  reachable from 0 refs. The fifth — design v1, blob 9d744eb7… — does NOT exist in the object
  database at all: `git cat-file -e` returns absent while `git hash-object` of the working file
  returns exactly that hash. Its bytes exist in one place on one disk. See N-3.
domain: CONTENT. `learning/` is not among the CONTROL_PLANE_ROOTS of P5.1.
class: WORKING RECORD
---

# LEGEND — OPERATIONAL READINESS PLAN v1

> **PROPOSAL ONLY · NOT AN AUTHORIZATION · ACTIVATES NOTHING · ACQUIRES NOTHING · STARTS NOTHING**
>
> The mandate forbids: reading new papers · starting Scientist A/B · executing the trial ·
> building agents · modifying `framework/` · modifying `wwox-rare-disease-legend` · merging or
> releasing to stable · any automatic modification without approval. **This record performs none
> of them.** It measured, and it proposes. § 11 enumerates what it did not do.

---

## 0 · Four facts measured today that the three input records did not have

Design v2 and the bootstrap audit are both careful documents. Neither ran the two checks below
against the tree the laboratory actually works in. **The results change the plan's first move.**

### N-1 🔴 · The publication gate BLOCKS on this working tree, and two of the trial's own planning records are why

The bootstrap audit reports, correctly, that in CI *"lo step **`Public release gate`** — il gate di
pubblicazione vero e proprio — **è passato**"*. Run against the working tree at HEAD, today:

```
VERDICT: BLOCK_PUBLICATION          BLOCKS: 6
  5 × DIRECT_IDENTIFIER   "Legacy personal identifier remains in public material."
      learning/orchestrator/FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001.md   lines 359 · 386 · 484
      learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md     lines 298 · 546
  1 × DIRTY_RELEASE_TREE  (expected: untracked files present)
```

**These are not heuristic matches.** `public_release_gate.py:388` hashes each candidate token with
SHA-256 and fires only when the digest is in the registered private-identifier allowlist. A
regex-shaped false positive is not reachable by that rule. **They are true positives by
construction.**

> **The consequence, stated plainly.** Design v2's decision **D-13 recommends option (a): "commit
> these records on this branch."** Executed literally today, that act writes five registered legacy
> personal identifiers into the git history of the **public edition** — the repository whose
> `CLAUDE.md` opens by binding *"This is the public edition and contains no individual-level
> record."* **D-13(a) is not safe as written, and nothing in design v2, in either findings register,
> or in the bootstrap audit says so**, because none of them ran this gate against these files.

**The negative that matters, with its denominator and scope.** Over the **581** tracked files at
HEAD, `DIRECT_IDENTIFIER` blocks = **0**. All five hits are in **untracked** records. *The tracked
repository is clean; the planning corpus is not.* The gate is right, and the tree CI ran it on was
not the tree the laboratory works in.

**Scoped, so the fix is surgical, not a retreat.** Of the seven untracked planning artifacts:

| Record | `DIRECT_IDENTIFIER` blocks |
|---|---|
| `LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v2.md` (the record the trial would run from) | **0** |
| `LEGEND_FIRST_OPERATIONAL_TRIAL_EXECUTION_PROTOCOL_v1.md` | **0** |
| `TRIAL-001-REVIEW-FINDINGS-REGISTER.md` | **0** |
| `TRIAL-002-DESIGN-V2-FINDINGS-REGISTER.md` | **0** |
| `LEGEND_DEVELOPMENT_BOOTSTRAP_AUDIT_v1.md` | **0** |
| 🔴 `FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001.md` | **3** |
| 🔴 `LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md` | **2** |

Five of seven can be preserved today. Two require redaction first. **This is decision B-1.**

### N-2 🔴 · The local battery fails a *different* eight than CI, and the difference decomposes cleanly

The bootstrap audit declares as an explicit limit: *"Le suite fallite non sono state rieseguite in
locale."* Re-run today, full clone, PyMuPDF present, working tree as found:

```
REGRESSION VERDICT: FAIL        8 suites, exit 1
```

Eight again — but **not the same eight**. The decomposition, and it is exact:

| Class | Count | Suites | What it means |
|---|---|---|---|
| **Content defects — fail in BOTH** | **6** | `test_release_runner_verdict` · `test_release_surface` · `test_locator_obligation_reaches_every_route` · `test_abstract_corpus_is_not_evidence` · `test_fulltext_trace_contract` · `test_session_self_eval` | audit causes **A** (5 tokens) + **B** (unregistered suite) + **C** (exec bits). 🔴 **Real, reproducible without CI, and still present 3 commits past the audited tip** |
| **CI-only — environment** | **2** | `test_figure_ppi_preflight` · `test_dismech_independent_protocol` | audit cause **D**. Both **PASS locally**. Confirms D is environment, not content |
| 🆕 **Local-only — working-tree contamination** | **2** | `test_documented_commands` · `test_fresh_clone_reader_journey` | 🔴 **invisible to CI, and nobody has reported it** |

**The local-only pair is a finding about the laboratory itself.** `test_documented_commands.py:36`
walks `ROOT.rglob("*.md")` with `IGNORED_PARTS = {".git", ".venv", "node_modules", "__pycache__"}`.
It therefore scans **gitignored directories and untracked files**. Its 11 offending hits at HEAD:

- **6** inside `.claude/worktrees/{mirror,evidence-index}/` — *the sibling worktrees of the
  multi-agent laboratory,* gitignored, belonging to other sessions
- **3** inside `LEGEND_DEVELOPMENT_BOOTSTRAP_AUDIT_v1.md` — **the audit document itself**, because
  it quotes a bare `./<script>.py` launch form and a non-existent record-conventions module as examples of the defect it reports
- **2** inside `backup/` snapshots, gitignored

> **The suite's population is the disk, not the repository.** In the laboratory's own operating
> configuration — one worktree per session, per the operating convention — **this suite can never
> be green locally, and its redness says nothing about the repository.** In CI it is green because
> CI's disk carries neither worktrees nor untracked records. **An audit document cannot be written
> in this repository without turning the battery red**, which is a self-reference worth naming
> before anyone treats a green battery as a pre-Trial condition.

### N-3 🔴 · One reviewed blob does not exist as an object at all

Design v2's frontmatter names five consumed blobs and flags them as gc-prunable. Measured today,
with a positive control that fires:

```
positive control  HEAD:CLAUDE.md → bf807fec…        PRESENT, reachable_refs = 1
e88dc043…  design v2 revision 1     PRESENT, reachable_refs = 0    (gc-prunable)
d5c0d296…  execution protocol v1    PRESENT, reachable_refs = 0    (gc-prunable)
ee00195f…  TRIAL-001 register       PRESENT, reachable_refs = 0    (gc-prunable)
959b57f4…  coordination plan        PRESENT, reachable_refs = 1
🔴 9d744eb7…  design v1              ABSENT from the object database entirely
```

`git hash-object learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md` returns exactly
`9d744eb7…`. **The hash was computed and cited; the object was never written.** Design v1's bytes
exist in exactly one place: an untracked file on one disk. **Design v2's `consumes_by_blob` block
already contains one unresolvable reference**, and the register that cites it does not know.

**Total corpus at risk from one `git clean -fdx`: 7 files, 4 301 lines**, of which the two carrying
identifiers are also the two that must not be committed as they stand.

### N-4 ✅ · The DisMech freeze holds — the audit's one open risk is closed

The audit rates intervention 1.3 **medium risk** on exactly this unknown: *"Nessun ambiente con
`fetch-depth: 0` è stato costruito per verificare se il freeze DisMech, una volta reso
verificabile, regga davvero."* Run today on a full local clone:

```
disease-models/wwox/analysis/scripts/test_dismech_independent_protocol.py
Ran 44 tests in 0.758s        OK
```

**The seal holds. The CI failure was `fetch-depth: 1` and nothing else.** F-08's fix carries no
hidden second defect, and its risk drops from medium to low. This is the plan's one unambiguously
good news, and it is recorded with the same weight as the bad.

---

## 1 · Executive summary

### 1.1 · The readiness verdict

> **LEGEND is closer to a credible first experiment than the input records suggest, and further
> from a safe first commit than any of them says.**

The method is designed to a standard most laboratories never reach: a 2×2 crossover audit whose
primary is *anchor–grounding concordance* with all four cells reachable, a declared degradation
ladder, pre-registered falsifiers, and 44 review findings dispositioned in a register that lives
outside the object it reviews. **The science is ready to be argued about. The container is not
ready to hold it.**

Three things stand between today and a defensible `TRIAL-001`, in this order:

1. **Preservation is unsafe and urgent.** The entire design corpus is untracked (N-3), and the one
   act recommended to fix that would publish personal identifiers (N-1). **This is the first move
   and it is not the one design v2 proposed.**
2. **"The repository is ready" is not a single predicate** (N-2). A green battery means three
   different things in CI, on a clean clone, and in a laboratory worktree. Until that is decided,
   *"repository pronta"* cannot be a checklist item because nobody can evaluate it.
3. **The trial's own auditing instrument does not exist** (design v2 § 9.7, feasibility P-3). It is
   a written schema, priced, and unexercised — and it carries the primary metric.

### 1.2 · The recommendation, in one line

> **Path C, gated — unchanged from design v2 — but preceded by a preservation-and-scope phase
> (Φ−1) that design v2 does not have, and blocked from starting until B-1…B-4 of § 4 are decided.**

Design v2 reached C on measured premises and the re-derivations in § 12 do not disturb them:
`DEC-20260822` returns `ACTIVATION_NOT_CONFIRMED`; `roles/*.md` are **4 of 4 `PROPOSED`**;
`ACTIVE by derivation: 0` leases; `roles/scientist.md` carries **6** `UNVERIFIED` capabilities.
**Nothing measured today makes B reachable and nothing makes A sufficient.**

### 1.3 · What changed relative to design v2

| # | Design v2 says | This plan says | Why |
|---|---|---|---|
| **C-1** 🔴 | **D-13(a)**: commit these records on this branch | 🔴 **Not as written.** Commit the five clean records; redact the two identifier-carrying ones first, under a named redaction record | N-1 |
| **C-2** 🔴 | design v1 survives as blob `9d744eb7…`, gc-prunable | 🔴 **It is already gone as an object.** Only the untracked file remains | N-3 |
| **C-3** | Φ0 pre-flight re-derives seat tips | **Φ0 must additionally re-run the publication gate against the working tree**, and that check does not exist in any phase of design v2 | N-1 |
| **C-4** | *(silent)* | 🆕 **"Repository ready" is split into three predicates** with different truth values | N-2 |
| **C-5** | the audit's F-08 fix carries medium risk | **low** — the seal verifies | N-4 |
| **C-6** | 17 phases, Φ0…Φ11 | **a Φ−1 precedes Φ0** and is the only phase authorized to run before the operator's next mandate | N-1 + N-3 |

### 1.4 · What this plan refuses to do

It does not build a script, add a schema field, define a new gate, or propose a new agent. The
input records converge on one lesson — **F-1/F-8's shape: the trial must not become the
construction of the instrument it reports on** — and this plan is bound by it. Every proposal below
is either a decision for the operator, a use of an instrument that already exists, or a written
record. **Where something must be built, it is named as construction and priced, never smuggled in
as preparation.**

---

## 2 · Current state

### 2.1 · Scientific method

| Element | State | Evidence | Class |
|---|---|---|---|
| **Trial Design v2, revision 2** | `PROPOSED — REVIEWED, INTEGRATED, NOT APPROVED`. 988 lines. 44 findings dispositioned | frontmatter; register `635f1b21…` | object |
| **Reviews received** | 2 rounds, 4 reviews, **67 findings** total (33 on the protocol, 44 on design v2 rev 1, minus overlap). **0 auto-corrected.** Both verdicts bound to blobs | both registers | object |
| **Reviewer standing** | 🔴 **No review was performed by a registered seat.** Registry binds `mirror` → `mirror-9c [3940a9]` and `plan` → `evidence-index-59 [de42c4]`; neither was live at any dispatch. Three consecutive days | registers § 0 | object |
| **Primary metric** | **anchor–grounding concordance**, four cells, all reachable, neither direction structurally favoured | design v2 § 6.2 | object |
| **Primary's instrument** | 🔴 **Does not exist.** `legend-locator-audit` is 102 prose lines over `(proposition, quote, anchor)` triples; the bare condition is a re-read, the opposite cost profile. No act column, no `UNGROUNDED` | design v2 § 9.7; P-3 | object |
| **Definition of full text** | Four layers, ordered decision procedure, first match wins, total and single-valued over all 64 subsets, `NOT_PRESENT_IN_PAPER` for the empty layer | design v2 § 4.2 | object |
| **`FULL_TEXT_READ_COMPLETE`** | `G-3` removed from the predicate; `CRITICAL_ASSET_GAP` reported beside it | design v2 § 4.3 | object |
| **Layer enumeration** | 🔴 **No instrument enumerates layers.** Over **51** scripts in `framework/scripts/`, `TEXT_LAYER\|FIGURE_LAYER\|SUPPLEMENTARY_LAYER` → 0 tracked; control `COVERAGE_KEYS` → 5. Φ1d is hand labour over ≥21 unit types, a strict superset of the 65-unit/109-panel precedent | M-5, P-10 | object |
| **Baselines** | **One** under the recommended configuration (BL-1, the crossover). BL-2 optional and recommended against; BL-4 forbidden and measured as unavailable | design v2 § 7 | object |
| **Statistics** | **None.** n = 1 paper. Raw distributions only; *"arm L is X % better"* is out of bounds | design v2 § 7 | — |
| **The input paper** | PMID 28123895 · Bandini 2016 · `FT-018` HIGH · PMCID PMC5214935 open. **0 of 174** files in `files/fulltext/`; **72** `^## FT-` in the queue; **10 of 581** tracked files carry the identifier | re-derived § 12 | population |
| **Prior-output contamination** | 🔴 **Real and located.** `literature_tracking_log_current.md` carries the pre-reading inference verbatim; `full_text_queue_current.md:242` carries it in the `**Why:**` of FT-018 itself | re-read today | object |
| **Scientific state** | `current_state: READY` · LINT **PASS** · receipts **OK, 128 chained, tail anchored** · growth anchors **PASS** (claims 39 · papers 70 · corpus 356 · literature 390) | re-run § 12 | population |

### 2.2 · Infrastructure

| Element | State | Evidence |
|---|---|---|
| **`legend-development`** | remote `development` → `<operator-account>/legend-development`, `main` @ **788c357**, **an ancestor of local HEAD by 3 commits**. Local branch `main` is at exactly 788c357 | `git ls-remote`, `merge-base` |
| **`wwox-rare-disease-legend`** | remote `origin`, `main` @ **8ab8e4b**, **458 commits behind HEAD**, **455 behind development** | `rev-list --count` |
| **Ancestry** | `origin/main` ⊂ `development/main` ⊂ `HEAD`. 🔴 **Strictly linear — there is no divergence to reconcile, and therefore no merge problem to solve.** The mandate's question about "merge manuali continui" has, today, an empty referent | `merge-base --is-ancestor`, both true |
| **CI** | **one** workflow, `public-release-gate.yml`, 43 lines, `on: push` unfiltered, `fetch-depth: 1`, `--mode release`. 4/4 green on stable through 2026-08-01; **1 run ever** on development, red | file read; audit F-10/F-12 |
| **Regression battery** | **65** suites registered, **66** tracked test files, **exactly 1 never executed** (`governance/scripts/test_candidate_content_hash.py`) | runner module imported, not regex |
| **Battery verdict** | 🔴 **FAIL in CI (8) and FAIL locally (8), and the two sets differ by 4** — see N-2 | both runs |
| **Publication gate** | 🔴 **BLOCK_PUBLICATION on the working tree** (6 blocks); PASS in CI on a clean checkout | N-1 |
| **Exec bits** | **4 of 4** shebang entrypoints still mode `100644` at HEAD, 3 commits past the audited tip | `git ls-tree` |
| **Bootstrap surface** | **5 of 5** tokens absent from `CLAUDE.md`. **3 of 5** present in `AGENTS.md`; `state-control` and `session_self_evaluation.md` in **neither** | `grep -cF`, both files |
| **Dependencies** | `requirements-analysis.txt` = **1** package (`numpy==2.0.2`). PyMuPDF undeclared, present locally at 1.26.5 | file read; import |
| **Worktrees** | **25** in `git worktree list` — 6 named laboratory seats under `.claude/worktrees/`, 4 Codex reading trees, **14 marked `prunable`** under session scratchpads | `git worktree list` |
| **Refs** | **57** | `for-each-ref` |
| **DisMech freeze** | ✅ **verifies, 44/44** on a full clone | N-4 |

#### 2.2.1 🔴 · No single ref carries the control plane

Measured with a control row that fires on every ref:

| Object | opcon-v1 | main | mirror | orchestrator | lettore | evidence-index | scientist-ab-spec |
|---|---|---|---|---|---|---|---|
| `CLAUDE.md` *(control)* | Y | Y | Y | Y | Y | Y | Y |
| `runtime/agent_card_registry.md` | · | · | · | **Y** | · | · | · |
| `runtime/orchestrator_lease.md` | Y | Y | · | Y | · | · | Y |
| `roles/scientist.md` | Y | Y | Y | Y | · | Y | Y |
| `framework/protocols/scientist_reading_modes.md` | Y | Y | · | **·** | · | · | Y |
| `governance/decisions/DEC-20260822-…` | Y | Y | · | · | · | · | · |
| `governance/GOVERNANCE_v3.1.1.md` | Y | Y | Y | Y | · | Y | Y |

> 🔴 **The registry that says `scientist-a`/`-b` are `NOT_REGISTERED` lives only on `orchestrator`.
> The protocol that fixes their identities does not exist on `orchestrator`.** The two objects whose
> disagreement W-1/P-5 identified as the central staleness **have never been on the same tree.**
> The reconciliation design v2 asks for cannot be performed as a comparison today — it is a merge,
> and a merge is an act nobody has been authorized to perform. Likewise `DEC-20260822`, the
> determination that governs every role question, reaches **2 of 7** sampled refs.

### 2.3 · Governance

| Element | State | Evidence |
|---|---|---|
| **`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`** | `BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE`, returns `ACTIVATION_NOT_CONFIRMED`. **The only record in `governance/decisions/`** | file read; `ls` → 1 file |
| **Role contracts** | **4 of 4 `PROPOSED`** — *"binding once Mirror hostile review passes and the operator approves"*. Neither has happened for any of the four | `grep ^status roles/*.md` |
| **Capabilities** | `roles/scientist.md` carries **6** `UNVERIFIED`; L2 verification suspended under the C-9 hold | `grep -c` |
| **Leases** | **0 ACTIVE by derivation** (5 recorded; #3 `derived=STALE` vs `stored=EXPIRED`, unreconciled) | `lease_state.py`, 2026-08-24T08:11Z |
| **Annex D.3 GATE 0** | requires `lease ACTIVE singleton` → **the real blocker on any `BATCH_COMMIT`**, not `MIRROR_REVIEW` (0 of 16 `CC-*`) | design v2 B-10, re-derived |
| **OPCON-v1** | `DRAFTED`. Reaches **1** file at HEAD (`learning/orchestrator/OPCON-V1-SECTION-A-SOURCE-001.md`); the convention proper lives on `mirror` (8 files) and `plan-orchsurf-r4-transcription` | per-ref sweep |
| **`claude_md_migration_map.md`** | still `PROPOSED`, subject to a Mirror hostile review nobody has closed — while the migration it documents has been on `main` since 2026-08-16 | audit F-13 |
| **Authority limit of this session** | 🔴 **none.** No `ACTOR_ID`, no contract, no lease. This record produces findings and proposals, which need no authority, and grants nothing, which would | this frontmatter |

---

## 3 · Blocks

A block is a condition that makes the trial's result uninterpretable or the act unsafe — not merely
a thing that is missing. Each is stated with what it halts.

| # | Block | Halts | Status | Route out |
|---|---|---|---|---|
| **K-1** 🔴 | **Preserving the design corpus as it stands would publish 5 registered personal identifiers** (N-1) | *any* commit of the planning records — the act D-13(a) recommends | 🔴 **OPEN, and it is the only block that gets worse with time**: the corpus is untracked, one `git clean` from gone, and the obvious remedy is the unsafe one | decision **B-1** |
| **K-2** 🔴 | **The bare-condition audit instrument does not exist in any form** | the PRIMARY. Without it the trial measures cost, which design v2 demoted for being near-tautological | 🔴 **OPEN by design** — v2 declares it, prices it, and refuses to build a script | decision **B-2** (D-14) |
| **K-3** 🔴 | **"Repository ready" has three different truth values** (N-2) | the pre-Trial checklist itself — the item cannot be evaluated | 🔴 **OPEN, newly measured** | decision **B-3** |
| **K-4** 🔴 | **No lease is ACTIVE and no role contract is activated** | Φ2's Orchestrator branch; any `BATCH_COMMIT` (Annex D.3 GATE 0); every Scientist artifact | **OPEN — and correctly so.** Design v2's step 1 is built to run underneath it | decision **B-4** |
| **K-5** | **The control plane is not on one ref** (§ 2.2.1) | the registry/protocol reconciliation; any statement of the form *"the laboratory's state is X"* | OPEN | decision **I-1** |
| **K-6** | **The regression battery is red on 6 content defects** at HEAD | nothing about the trial *directly* — but it is the instrument that would tell us if the trial broke something | OPEN | decisions **I-2 · I-3** |
| **K-7** | **Acquisition of the paper is authorization- and network-blocked** from an isolated session | Φ1. Not instrument-blocked: routes exist | OPEN | decision **B-5** (D-3) |
| **K-8** | **No Φ7 artifact path exists** — `reviews/` holds `plan/` and 3 files | Φ7 | OPEN, trivial | decision **I-4** (D-8) |

> **Not blocks, and named so they are not mistaken for blocks:** the 4 exec bits · the Node 20 pins ·
> the unregistered suite · PyMuPDF's absence in CI · `fetch-depth: 1`. Each is real, each is cheap,
> **none of them prevents a scientific trial from being credible.** They belong to § 4's *important*
> tier, and putting them in the blocking tier is how a readiness plan becomes an infrastructure
> backlog wearing a lab coat.

---

## 4 · Human decisions

Three tiers, as the mandate requires. **Every one of them is the operator's; none is assumed here.**
A recommendation is given for each, because a decision list with no recommendation transfers the
work rather than the choice.

### 4.1 · BLOCKING — the trial cannot start until these are answered

| # | Decision | Options | Recommendation | If unanswered |
|---|---|---|---|---|
| **B-1** 🔴 | **How is the design corpus preserved, given that 2 of 7 records carry registered personal identifiers?** (N-1, N-3) | (a) commit all 7 as they stand · (b) **commit the 5 clean records now; redact the 2 and commit them after a named redaction record** · (c) commit the 5, leave the 2 untracked · (d) commit nothing | **(b).** (a) publishes identifiers into the public edition and is the option design v2's D-13 recommends without knowing. (c) leaves design v1 — already objectless (N-3) — one `git clean` from permanent loss, and both reviews of the protocol are bound to it. (d) is (c) for everything | **the corpus stays destructible, and the reviews stay bound to bytes one of which has no object** |
| **B-2** 🔴 | **Is `TRIAL-001-AUDIT-SCHEMA.md` authored before Φ0?** (design v2 D-14) | (a) **yes, schema first** · (b) improvise at Φ7 · (c) anchored condition only | **(a).** (c) deletes the primary and is the cut § 8.3 says never to make. (b) makes Φ7 unreplayable, which fails step 2's exit criterion by construction | **Φ7 cannot be replayed, so step 2 cannot authorize step 3** |
| **B-3** 🔴 | **What does "repository pronta" mean?** (N-2) | (a) CI green on a clean checkout · (b) **battery green on a full clone, evaluated over `git ls-files` rather than the disk** · (c) green in a laboratory worktree · (d) not a pre-Trial condition at all | **(b), with the scope stated in the checklist.** (c) is unreachable while the laboratory uses worktrees — the suites scan the disk. (a) is achievable but certifies a tree nobody works in. **(d) is defensible and should be argued against explicitly, not skipped** | **the pre-Trial checklist contains an item nobody can evaluate, and it will be marked green by whoever is least strict** |
| **B-4** 🔴 | **Path A, B, or C?** (design v2 D-1) | (a) **C, gated** · (b) A · (c) B | **(a).** Re-derived today: `ACTIVATION_NOT_CONFIRMED` · 4/4 `PROPOSED` · 0 ACTIVE leases · 6 `UNVERIFIED`. B is not reachable; A produces no evidence about verifiability, the one property the mandate names | **nothing else can be sequenced** |
| **B-5** 🔴 | **How is the full text acquired?** (design v2 D-3) | (a) authorize a connector · (b) **operator supplies the PDF** · (c) `find-fulltext` in a web-enabled session · (d) `pmc_pow_fetch.py` | **(b) or (c).** (d) is the last-resort tier and takes `url output`, not a PMCID | **Φ1 cannot start** |

### 4.2 · IMPORTANT — they improve the system; they do not block the trial

| # | Decision | Recommendation |
|---|---|---|
| **I-1** | **Reconcile the control plane onto one ref** (§ 2.2.1) — specifically, bring `runtime/agent_card_registry.md` and `framework/protocols/scientist_reading_modes.md` onto a common tree so the `NOT_REGISTERED` staleness becomes a comparison rather than a merge | Do it **before step 3**, not before step 1. Step 1 needs no actorhood, so the staleness costs nothing until it does |
| **I-2** | **Development gate vs release gate** (audit D-2, F-10) | Audit's **option 3** — two workflows, one body of tests. 🔴 **And one thing the audit could not know: the development gate must be scoped to `git ls-files`, or the laboratory's own worktrees will keep it red forever** (N-2) |
| **I-3** | **PyMuPDF: optional or mandatory?** (audit D-3, F-07) | **Mandatory for the development gate.** It gates 13 checks on the PDF surface — the surface that decides whether a citation is verifiable, which is the trial's subject matter |
| **I-4** | **Where do audit artifacts live?** (design v2 D-8) | `reviews/trial-001/`. The reviewers are ephemeral; a per-reviewer directory names a seat that does not exist |
| **I-5** | **Where do the inviolable facts live?** (audit D-1, F-01/F-02) | Audit's **option 3** — a declared bootstrap-surface registry, tests parameterized on it. 🔴 **With one correction the audit did not make: `state-control` and `session_self_evaluation.md` are in NEITHER `CLAUDE.md` nor `AGENTS.md`.** Two of the five tokens have no bootstrap home at all, so *"pointing the tests at `AGENTS.md`"* would still leave two red |
| **I-6** | **Where does the skip boundary run?** (audit D-4, F-11) | Declared categories per reason, **decided before the first green run, not after** |
| **I-7** | **Shallow-clone degradation contract** (audit D-5, F-08/F-09) | Both: `--is-shallow-repository` to degrade outside CI, `fetch-depth: 0` so the verifier runs. 🔴 **Risk now measured LOW, not medium** (N-4) |
| **I-8** | Register the 1 unexecuted suite; set 4 exec bits; update 3 action pins | Mechanical, unambiguous, **each in an isolated change** |

### 4.3 · FUTURE — after the first experiment, and deliberately not before

| # | Question | Why it waits |
|---|---|---|
| **F-1** | Activation act discharging `DEC-20260822`; lifting or scoping the C-9 L2 hold | Step 3's precondition. Doing it earlier grants authority nothing yet needs, which is how authority stops being traceable |
| **F-2** | `legend-development` visibility, `main` protection, `sha_pinning_required` (audit G-3) | Real, and orthogonal to whether the science is credible. **It becomes blocking the moment step 3 puts more than one writer on a branch** |
| **F-3** | What constitutes a "release point" (audit G-4) | 🔴 **Today it has an empty referent**: the three repositories are strictly linear (§ 2.2). Define it when there is something to promote |
| **F-4** | Derive `TESTS` from `git ls-files`; exec-bit hook upstream; extend migration inventory to tests | Class fixes. They are written after the cases are seen, never before |
| **F-5** | The A/B mode benchmark; a second reader; Scientist C and the § 32 synthesis conflict | Step 3 |
| **F-6** | T-8 — the 9 papers whose receipts yield undefined layers | Design v2 declares it open and unrepaired, correctly. Repairing it inside the trial would make the trial the repair |
| **F-7** | Who closes the Mirror review of `claude_md_migration_map.md` (audit G-2) | Governance hygiene. It has been `PROPOSED` on `main` for 8 days and the sky has not fallen |

---

## 5 · The first LEGEND execution — A, B, or C

Assessed on the mandate's four axes. **The fourth axis is the one that decides**, because the
mandate's guiding question is not *"did LEGEND produce a good reading?"* but *"does LEGEND improve
traceability, verifiability and correctability?"*

### Option A — a single LEGEND reader

| Axis | Assessment |
|---|---|
| **Scientific value** | Real and immediate: one paper read to LEGEND's discipline, typed claims, anchored locators, a commit candidate or a documented dismissal. `FT-018` is discharged either way |
| **Cost** | Lowest. Acquisition + Φ4 + Φ6's five existing mechanical checks. **No new instrument** |
| **Risk** | Low, and one specific danger: it produces an artifact that *looks* like evidence about the method and is not |
| 🔴 **Can it measure LEGEND's contribution?** | **No.** With no independent check, the only witness to the anchors' quality is the party that authored them. It measures the reader, and reports it as the method |

### Option B — Scientist A/B

| Axis | Assessment |
|---|---|
| **Scientific value** | Two readings of one paper under two declared modes; a genuine mode comparison |
| **Cost** | High **and largely unpriceable today**: `SURFACE-FULL` (a 421-line spec, ~42 % population block, a 678-line `evidence_units.json`, build/verify/population×2/freeze), plus a `freeze` that refuses unless the surface carries three identity files and an `--actor-id` no registry resolves |
| **Risk** | 🔴 **Not available, and the reason is governance rather than absence.** `ACTIVATION_NOT_CONFIRMED` · C-9 suspends L2 so no capability reaches `VERIFIED` (6 `UNVERIFIED`) · 0 ACTIVE leases against Annex D.3 GATE 0 · the registry says `NOT_REGISTERED` and lives on a ref that does not carry the protocol resolving it (§ 2.2.1) |
| 🔴 **Can it measure LEGEND's contribution?** | **It measures the wrong thing first.** A/B compares two LEGEND modes to each other. It answers *"which LEGEND mode reads better"*, not *"does LEGEND help"*. **Both arms are inside the system under test** |

### Option C — progressive, gated

| Axis | Assessment |
|---|---|
| **Scientific value** | Same reading as A, plus a crossover audit that produces the one thing A cannot: an independent party's verdict on whether the anchors land where the evidence is |
| **Cost** | A's cost **plus two named line items**: the Φ1d hand enumeration (≥21 unit types, a strict superset of a 65-unit/109-panel precedent) and `TRIAL-001-AUDIT-SCHEMA.md` (new, unexercised, no precedent on any ref). **Both are declared, not discovered** |
| **Risk** | The audit instrument is new construction and could stall — the feasibility review names Φ7 as the most likely stall. Mitigated by the schema-first requirement (B-2) and by § 2.3's degradation ladder, whose floor is a `READING RECORD` rather than nothing |
| ✅ **Can it measure LEGEND's contribution?** | **Yes, and it is the only one of the three that can.** `ANCHOR-ADDS` is evidence *for*; `ANCHOR-MISLEADS` is evidence *against*; both are reachable, neither is favoured. **A design in which the unfavourable cell cannot be populated is not a measurement**, and that is precisely why revision 1's cost primary was demoted |

### Recommendation

> ✅ **C, gated as three steps — and the recommendation carries two conditions design v2 does not
> impose.**
>
> ```
> Φ−1  PRESERVATION AND SCOPE          ← 🆕 new, and the only phase runnable before the next mandate
>      redact 2 records · commit 5 clean + 2 redacted · re-run the publication gate on the tree
>      needs: decision B-1 only
>
> STEP 1   single LEGEND reader + 2×2 crossover audit + operator gate
>          needs: B-2 (schema first) · B-3 (what "ready" means) · B-5 (acquisition route)
>          does NOT need: actorhood · a lease · the L2 lift · any new script
>
> STEP 2   method validation — a replay session reproduces every figure AND every audit verdict
>          from the record alone, asking nobody anything.  ← the exit criterion, and it gates step 3
>
> STEP 3   multi-agent extension — second reader, A/B benchmark, Scientist actorhood
>          needs, and only then: the activation act · the C-9 hold lifted or scoped ·
>          the registry reconciled onto one ref with the protocol (I-1) · one ACTIVE lease
> ```
>
> **Condition 1 — Φ−1 precedes everything.** Today the trial's design corpus is destructible and
> the act that would save it is unsafe. Starting a trial whose own design cannot survive a `git
> clean` fails *preservabile* before it has tested anything.
>
> **Condition 2 — if B-2 is answered (b) or (c), the recommendation degrades to A and must say so
> in the outcome.** An option C without its audit instrument is option A with a longer phase table,
> and the record must not let that substitution happen silently.

---

## 6 · Scientist A/B — what exists, what is specification, what must be built

The mandate is right to refuse the assumption. Measured at HEAD:

| Object | Path | State | Class |
|---|---|---|---|
| **Reading-modes protocol** | `framework/protocols/scientist_reading_modes.md` | ✅ **EXISTS — 526 lines, canonical**, landed by `4454feab` *"The Scientist A/B specification becomes canonical"* (2026-08-19), an ancestor of HEAD | built |
| **Role contract** | `roles/scientist.md` | ⚠️ **EXISTS — 122 lines, `PROPOSED`**, carries **6** `UNVERIFIED` capabilities | specification |
| **Benchmark packet** | `framework/eval/benchmarks/BENCH-AB-001/` | ✅ **EXISTS — 13 files**: `benchmark_manifest.json`, `surface_spec.json`, `population/evidence_units.json`, and 6 instruction files including `ASSIGNMENT.scientist-a.md`, `ASSIGNMENT.scientist-b.md`, `MODE_A.md`, `MODE_B.md`, `OUTPUT_SCHEMA.md` | built |
| **Mirror acceptance** | `mirror:reviews/mirror/REV-SCIAB-MIRROR-006.md` | ✅ `verdict: ACCEPT — M-5 is closed`, 2026-08-19 | built |
| **Physical seats** | `.claude/worktrees/{lettore,lettore-b,lettore-c,mirror,orchestrator,evidence-index}` | ✅ **all six exist on disk**, on their named branches | built |
| **Agent card registry** | `runtime/agent_card_registry.md` | 🔴 **EXISTS ON `orchestrator` ONLY**, and says `scientist-a`/`-b` `NOT_REGISTERED`. Written 2026-08-18 16:05 — **one day before** the execution that would resolve them | stale, and unreachable from the tree that could refute it |
| **Actorhood** | — | 🔴 **DOES NOT EXIST.** `DEC-20260822` → `ACTIVATION_NOT_CONFIRMED`; 4/4 contracts `PROPOSED`; 0 ACTIVE leases | must be granted, not built |
| **L2 capability verification** | — | 🔴 **SUSPENDED** under the C-9 hold | must be lifted or scoped |
| **A surface `freeze` can accept** | — | 🔴 **MUST BE BUILT per run.** `freeze` refuses without `ASSIGNMENT.md` + `BENCHMARK_INSTRUCTIONS.md` + `OUTPUT_SCHEMA.md`, then refuses again if `--actor-id` disagrees with `ASSIGNMENT.md` — forcing the surface to declare an actor id no registry resolves | blocked upstream of construction |

> **The honest summary, and it corrects the impression both design revisions leave.** Scientist A/B
> is **not mostly unbuilt — it is mostly built and entirely unauthorized.** The protocol is
> canonical, the packet exists, the worktrees exist, Mirror accepted it. What is missing is an
> activation act, an L2 lift, a lease, and one ref where the registry and the protocol can see each
> other. **Nothing on that list is a construction task.** Design v2's `U-1`/`U-2` said this and it
> deserves restating: *the laboratory is further along than its own records read.*
>
> **And therefore: A/B is not needed for step 1, and is not what step 1 is waiting for.** The
> crossover auditors need no actorhood; that half of design v2's load-bearing claim survived both
> reviews intact.

---

## 7 · GitHub architecture

### 7.1 · The mandate's diagram, and what is actually there

The mandate draws:

```
wwox-rare-disease-legend  ──release periodiche──▶  legend-development
```

Measured, the arrow runs the other way and nothing has ever traversed it:

```
HEAD (legend-operating-convention-v1) @ 30cb4f3
   │  3 commits
   ▼
legend-development/main @ 788c357          ← created 2026-08-23T20:47Z · 1 run ever · red
   │  455 commits
   ▼
wwox-rare-disease-legend/main @ 8ab8e4b    ← last green gate 2026-08-01 · the publication target
```

**All three are on one strictly linear history** (`origin/main` ⊂ `development/main` ⊂ `HEAD`, both
`merge-base --is-ancestor` checks return true). Consequences, and they are not small:

1. 🔴 **"Evitare merge manuali continui" has no referent today.** There is nothing to merge. Both
   remotes are ancestors; a promotion is a fast-forward push. The problem the mandate anticipates
   is a *future* problem, and designing for it now is designing against a shape nobody has seen.
2. 🔴 **The direction of flow is development → stable**, not the reverse. `wwox-rare-disease-legend`
   is not upstream; it is **the publication target**. The audit's reading is the correct one.
3. **The separation has already done work.** 455 unverified commits have been held out of the
   publication point. That is the separation succeeding, not failing.

### 7.2 · Are separate repositories the right model?

**Yes — and the evidence is stronger than the argument.** 4 real content defects arose in the 22
days and 455 commits during which no gate ran (audit F-12), and every one of them stopped at the
boundary. Merging the two would put them on the publication surface.

**What is missing is not the separation. It is the ratchet in the middle** — and § 7.3 shows the
ratchet cannot be built from the gate alone.

### 7.3 🔴 · The finding that changes the architecture question

A development gate is normally the answer. **Measured today, the obvious form of it does not work
in this laboratory**, and the reason is structural rather than incidental (N-2):

- `test_documented_commands.py` and `test_fresh_clone_reader_journey.py` scan
  `ROOT.rglob("*.md")` minus `{.git, .venv, node_modules, __pycache__}` — **the disk, not the
  repository**.
- The laboratory's operating method is **one gitignored worktree per session** under
  `.claude/worktrees/`. Those worktrees contain markdown by design.
- Therefore **a gate that runs on a developer's machine fails on other agents' files**, and a gate
  that runs only in CI is blind to exactly the class N-1 found: untracked records carrying personal
  identifiers, which CI never sees because CI never checks them out.

> **Neither gate sees what the other sees, and the union is not covered by running both.**
> CI sees the committed tree. A local run sees the disk. **The object nobody gates is the one that
> matters most here: files that exist, carry identifiers, and are not yet committed.**

### 7.4 · The proposal

Three changes, ordered by what makes the next one readable — the audit's own ordering criterion:

| # | Change | Rationale | Decision |
|---|---|---|---|
| **A-1** 🔴 | **A pre-commit privacy check on the staged set**, using `public_release_gate.py`'s existing identifier rule against **what is about to be committed**, not against the tree | This is the only gate position that would have caught N-1. It needs no new rule — the rule exists and fires correctly; it needs a **moment** | new — not in the audit |
| **A-2** | **Two workflows, one body of tests** (audit option 3): `development-gate.yml` on push, `fetch-depth: 0`, full dependencies, no `--mode release`; `release-gate.yml` on dispatch/tag, everything plus the publication gate | Separates *"is this commit sound?"* from *"is this state publishable?"* without letting the batteries diverge | audit **D-2** |
| **A-3** 🔴 | **Scope the disk-walking suites to `git ls-files`** | Without it, A-2's development gate is red forever in every laboratory worktree, and a permanently red gate is a gate nobody reads. **This is a prerequisite of A-2, not a follow-up** | new — a corollary of N-2 |

**A "release point"** — the audit's G-4 — is then definable and not before: *a commit on
`development/main` on which `release-gate.yml` has run green with the publication gate in
`--mode release` from a clean tree*. Today no such commit exists, in either repository.

---

## 8 · Pre-Trial checklist

Each condition is stated so that **it can be evaluated by someone who was not here**, with the
instrument that evaluates it. A condition whose evaluation is a judgement says so.

| # | Condition | Verified by | Today |
|---|---|---|---|
| **1 · Protocol approved** | The operator has answered **B-1…B-5**, and design v2 revision 2 carries a status other than `PROPOSED` | reading the frontmatter | 🔴 **NO** — 5 blocking decisions open, status `PROPOSED` |
| **2 · Corpus preserved** | The 7 planning records are reachable from a ref; `git cat-file -e` fires on each committed blob; **`public_release_gate.py` reports 0 `DIRECT_IDENTIFIER`** over the committed set | commands in § 12 | 🔴 **NO** — 0 of 7 committed; 5 identifier blocks; 1 blob objectless |
| **3 · Repository ready** | *Per decision **B-3***. Under the recommended (b): `run_release_regressions.py` green on a full clone with the disk-walking suites scoped to `git ls-files` | the runner | 🔴 **NO** — FAIL, and the predicate itself is undecided |
| **4 · Metrics frozen** | `TRIAL-001-AUDIT-SCHEMA.md` exists and carries: the column set, the verdict set **per condition**, the act-list format, the *"one act"* definition **with a worked example**, and the shuffle-recording format | file existence + field presence | 🔴 **NO** — the file does not exist on any ref |
| **5 · Input available** | The artifact is in `files/fulltext/`, its sha256 is recorded in the acquisition declaration **authored before acquisition**, and `fulltext_receipts.py verify` passes | the two commands | 🔴 **NO** — 0 of 174 |
| **6 · Audit defined** | `reviews/trial-001/` exists; two fresh sessions are reachable; the shuffle and the X/Y split are **recorded before** the audit begins | directory + the recorded shuffle | 🔴 **NO** — `reviews/` holds `plan/` and 3 files |
| **7 · Artifacts preservable** | Every phase's artifact has a declared path **inside the § 3.5 write allowlist**, and the allowlist has been re-derived against what the instruments write | reading `fulltext_receipts.py` | ⚠️ **PARTLY** — repaired in v2 after two BLOCKERs; **not re-verified since** |
| **8 · Roles defined** | Every phase has a named owner, and for each owner the record states whether its authority traces to **an instrument** (permitted) or **to a contract clause standing alone** (not, under `DEC-20260822`) | design v2 § 8.1 | ✅ **YES** — this one is done, and done well |
| **9 · Falsifiers satisfiable** | Every dimension in § 10.3 has a falsifier some observation could satisfy; `ANCHOR-MISLEADS` and `ANCHOR-ADDS` are both reachable | reading § 10.3 | ✅ **YES** |
| **10 · Friction log open** | `TRIAL-001-FRICTION-LOG.md` exists and is append-only **before Φ0**, since it is the only artifact that cannot be reconstructed afterwards | file existence | 🔴 **NO** |

**Score: 2 of 10 satisfied · 1 partial · 7 not.** Stated as a count because it is an enumerated set,
not because it is a grade.

---

## 9 · Roadmap

Four phases. **Only Φ−1 is proposed for the operator's next mandate**; the rest are sequenced, not
scheduled, and each opens only if the previous closes.

```
Φ−1  PRESERVATION AND SCOPE                                    ← needs decision B-1 only
     ├─ redact the 5 identifier hits in 2 records, into a named REDACTION RECORD that states
     │  what class was removed and from which lines — never what was removed
     ├─ re-run public_release_gate.py against the tree: expect 0 DIRECT_IDENTIFIER
     ├─ WORK_COMMIT the 7 records on this branch (a session's own named paths, its own branch)
     └─ EXIT: git cat-file -e fires on all 7 blobs · gate reports 0 identifier blocks
        FALSIFIER: any DIRECT_IDENTIFIER survives → Φ−1 did not close, and nothing proceeds

Φ0   DECISION AND SCHEMA                                        ← needs B-2, B-3, B-4, B-5
     ├─ the operator answers the five blocking decisions
     ├─ TRIAL-001-AUDIT-SCHEMA.md is authored (B-2 = a)
     ├─ the forbidden-path list is RE-ENUMERATED at this instant, because the set grows
     └─ EXIT: every § 8 checklist row is YES or carries an operator-signed waiver naming its cost

Φ1   TRIAL-001 STEP 1                                           ← design v2 § 9.1, Φ0…Φ11 unchanged
     └─ EXIT: two outcome records, one per track · the friction log closed · one SLR

Φ2   METHOD VALIDATION                                          ← design v2 step 2
     └─ EXIT CRITERION, and it is what authorizes step 3:
        a replay session reproduces every reported figure AND every audit verdict from the
        record alone, without asking the reader or the auditors anything
```

**Infrastructure runs beside this, never inside it.** The audit's P1/P2/P3 ordering is sound and is
adopted with two amendments: **A-3 (scope the suites to `git ls-files`) precedes A-2**, and F-08's
risk is **low**, not medium (N-4). No infrastructure item is a precondition of Φ−1 — *which is why
Φ−1 is the only phase runnable now.*

---

## 10 · Trial start criteria

The trial may begin when, and only when:

1. **§ 8's ten conditions** are each YES, or carry an operator waiver that names what the waiver
   costs the result. *A waiver with no stated cost is not a waiver; it is a deletion.*
2. **B-1…B-5** are answered, and the answers are in a record, not in a chat.
3. **Φ−1 has closed on its falsifier**, not on its author's judgement.
4. **The degradation rung is chosen before the run**, and § 10.1's success criteria are scoped to
   that rung. *(Design v2's P-15: a success criterion demanding every phase, offered beside rungs
   that remove phases, cannot be satisfied under cuts the design itself recommends.)*
5. **Someone who is not the reader** has checked the assignment for prior-conclusion leakage against
   the abstract retained at Φ1b — the contaminating line is in the queue entry the reader must
   never see (`full_text_queue_current.md:242`).

> **And one criterion that is not on the list, deliberately.** *"The regression battery is green."*
> Under B-3 it may become condition 3; until B-3 is answered it is unevaluable (N-2), and a
> checklist item nobody can evaluate is worse than an absent one — it will be marked green by
> whoever is least strict, and the record will carry a passing row that means nothing.

---

## 11 · What this record does not do

It does not start the trial, acquire a paper, read a paper, build a surface, author a spec, or run
a benchmark · does not start Scientist A/B or any agent · does not dispatch, register, activate,
assign, or grant authority · creates no Task Contract, candidate, `DEC`, approval, or ledger event ·
does not lift the C-9 hold, verify a capability, acquire a lease, or resolve an `ACTOR_ID` · does
not adopt or amend OPCON-v1 · adds no field to any schema and builds no script · **does not modify
`governance/`, `roles/`, `framework/`, `ledger/`, `runtime/`, the four scientific current files, or
`wwox-rare-disease-legend`** · advances no branch, stages nothing, commits nothing, pushes nothing ·
performs no redaction — **Φ−1 is proposed, not executed** · resolves no finding on anyone's behalf ·
claims no actorhood.

**What it did do, disclosed:** it ran read-only instruments — `lease_state.py`, `legend_lint.py`,
`fulltext_receipts.py verify`, `growth_anchors.py check`, `run_release_regressions.py`,
`public_release_gate.py --mode release`, and two suites individually. `git status --porcelain` was
captured before and after the battery and is **identical**; the battery wrote nothing visible to it.
🔴 **It wrote no loose git objects** — the write class `B-8` cannot see. This one file is its only
output.

---

## 12 · Verification trail

All at `legend-operating-convention-v1` @ `30cb4f3fd700e2aaf6b608e363438f883ddc3760`,
**2026-08-24T08:11Z–08:18Z**. Every figure in this record is below.

```bash
# ── N-1 · the publication gate, against the WORKING TREE
python3 scripts/public_release_gate.py --root . --mode release
#   VERDICT: BLOCK_PUBLICATION   BLOCKS: 6
#   5 × DIRECT_IDENTIFIER + 1 × DIRTY_RELEASE_TREE
python3 scripts/public_release_gate.py --root . --mode release 2>&1 \
  | grep '^\[BLOCK\]' | awk '{print $2, $3}' | sed 's/:[0-9]*$//' | sort | uniq -c
#   3 DIRECT_IDENTIFIER learning/orchestrator/FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001.md
#   2 DIRECT_IDENTIFIER learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md
#   1 DIRTY_RELEASE_TREE .
sed -n '386,402p' scripts/public_release_gate.py    # SHA-256 against a registered digest allowlist
#   → not a regex heuristic; a false positive of this shape is not reachable
#   NEGATIVE, WITH ITS DENOMINATOR AND SCOPE: over the 581 TRACKED files, DIRECT_IDENTIFIER = 0.
#   All five hits are in UNTRACKED records. The tracked repository is clean.

# ── N-2 · the local battery, and the 6/2/2 decomposition
python3 scripts/run_release_regressions.py            # REGRESSION VERDICT: FAIL, exit 1
#   local 8:  documented_commands · fresh_clone_reader_journey · release_runner_verdict ·
#             locator_obligation · abstract_corpus · release_surface · fulltext_trace_contract ·
#             session_self_eval
#   CI 8 (audit, @788c357): the six in common, plus figure_ppi_preflight + dismech_independent
python3 framework/scripts/test_figure_ppi_preflight.py                       # OK  (PyMuPDF 1.26.5)
python3 disease-models/wwox/analysis/scripts/test_dismech_independent_protocol.py  # OK, 44 tests
git rev-parse --is-shallow-repository                                        # false
sed -n '30,36p' scripts/test_documented_commands.py
#   IGNORED_PARTS = {".git",".venv","node_modules","__pycache__"} ; ROOT.rglob("*.md")
git check-ignore -q .claude/worktrees/mirror/reviews/mirror/REV-SCIAB-MIRROR-001.md && echo IGNORED
#   IGNORED  ← and the suite scans it anyway. 6 of 11 hits are sibling worktrees.
git status --porcelain > pre
python3 scripts/run_release_regressions.py
git status --porcelain > post
diff pre post          # identical — the battery wrote nothing

# ── N-3 · blob survival, with a positive control that fires
git rev-parse HEAD:CLAUDE.md                                     # bf807fec…
git cat-file -e bf807fec… && echo "control PRESENT"              # the tool works
git cat-file -e 9d744eb7a284c80b7a6a2e1258fd04f1c9d44036 || echo ABSENT     # ABSENT
git hash-object learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md
#   9d744eb7…   ← the hash was computed and cited; the object was never written
for b in e88dc043… d5c0d296… ee00195f…; do git rev-list --objects --all | grep -c "^$b"; done
#   0 0 0   ← present, reachable from no ref, gc-prunable
git status --porcelain | grep '^??' | wc -l                      # 7 untracked records
git status --porcelain | grep '^??' | sed 's/^?? //' | xargs wc -l | tail -1   # 4301 lines

# ── § 2.2.1 · the per-ref control-plane sweep
#   ⚠️ zsh does NOT word-split unquoted variables: a `for r in $REFS` loop silently iterates ONCE
#   over the whole string. Written with literal lists, and with ${r}:${p} braces so that `:p`
#   is not read as a history modifier. Control row = CLAUDE.md, which must be Y on every ref.
for p in CLAUDE.md runtime/agent_card_registry.md framework/protocols/scientist_reading_modes.md; do
  for r in legend-operating-convention-v1 main mirror orchestrator lettore evidence-index scientist-ab-spec; do
    git cat-file -e "${r}:${p}" 2>/dev/null && printf Y || printf .
  done; echo "  $p"
done
#   YYYYYYY  CLAUDE.md                                        ← control fires on all 7
#   ...Y...  runtime/agent_card_registry.md                   ← orchestrator ONLY
#   YY.....  framework/protocols/scientist_reading_modes.md   ← NOT on orchestrator
#   → the registry and the protocol that would resolve it have never been on the same tree

# ── § 2.2 / § 7.1 · the three repositories
git ls-remote development | head -2         # main 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
git ls-remote origin      | head -3         # main 8ab8e4b86393f536cba7f96146c7ae34f1877992
git merge-base --is-ancestor 8ab8e4b 788c357 && echo "origin ⊂ development"      # true
git merge-base --is-ancestor 788c357 HEAD  && echo "development ⊂ HEAD"          # true
git rev-list --count 8ab8e4b..788c357   # 455      git rev-list --count 788c357..HEAD   # 3
git rev-parse main                      # 788c357…  ← local main IS development/main

# ── § 2.3 · governance, re-derived
python3 framework/scripts/lease_state.py | tail -1                # ACTIVE by derivation: 0
grep -h '^status' roles/*.md | sort | uniq -c                     # 4 × PROPOSED
grep -c UNVERIFIED roles/scientist.md                             # 6
ls governance/decisions/ | wc -l                                  # 1
grep -n "No actor authority may be assumed" governance/decisions/DEC-20260822-*.md

# ── § 2.1 · scientific state, re-derived
python3 framework/scripts/legend_lint.py .            | tail -2   # VERDICT: PASS
python3 framework/scripts/fulltext_receipts.py verify | tail -1   # OK: 128 chained, tail anchored
python3 framework/scripts/growth_anchors.py check     | tail -1   # VERDICT: PASS
#   claims=39 · papers=70 · corpus=356 · literature=390 | registry_only=15 | unread_premises=4
git grep -lE "28123895|PMC5214935" HEAD | wc -l                   # 10  of 581 tracked
ls files/fulltext | wc -l                                         # 174
ls files/fulltext | grep -icE "28123895|PMC5214935|bandini"       # 0   of 174
grep -c '^## FT-' disease-models/wwox/research/full_text_queue_current.md   # 72
sed -n '242p'    disease-models/wwox/research/full_text_queue_current.md
#   the FT-018 `Why:` — the prior LEGEND inference the reader must never be shown
ls disease-models/wwox/research/commit_candidates | grep -c '^CC-'          # 16

# ── § 2.2 · infrastructure, re-derived at HEAD (3 commits past the audited tip)
git ls-tree -r HEAD framework/scripts/lease_state.py governance/scripts/candidate_content_hash.py \
  governance/scripts/governance_fingerprint.py governance/scripts/test_candidate_content_hash.py
#   4 of 4 still mode 100644 with a shebang
grep -c test_candidate_content_hash scripts/run_release_regressions.py      # 0  (still unregistered)
python3 -c "import sys;sys.path.insert(0,'scripts');import run_release_regressions as r;print(len(r.TESTS))"
#   65 registered ·  git ls-files | grep -cE '(^|/)test_[^/]*\.py$'  → 66 tracked  → 1 never run
for t in verbatim_locators pubmed_corpus_harvest FULLTEXT_READ_RECEIPT state-control \
         session_self_evaluation.md; do
  printf "%-26s CLAUDE=%s AGENTS=%s\n" "$t" "$(grep -cF "$t" CLAUDE.md)" "$(grep -cF "$t" AGENTS.md)"
done
#   3 of 5 survive in AGENTS.md · state-control and session_self_evaluation.md in NEITHER  ← I-5
ls framework/scripts/*.py | wc -l   # 51      git ls-tree -r --name-only HEAD | wc -l   # 581
git for-each-ref | wc -l            # 57      git worktree list | wc -l                 # 25

# ── § 6 · Scientist A/B, what exists on disk
wc -l framework/protocols/scientist_reading_modes.md roles/scientist.md   # 526 · 122
find framework/eval/benchmarks/BENCH-AB-001 -type f | wc -l               # 13
git merge-base --is-ancestor 4454feab HEAD && echo "A/B spec IS canonical"
git log -1 --format='%ad' --date=iso orchestrator -- runtime/agent_card_registry.md
#   2026-08-18 16:05:46   ← one day BEFORE the execution commit of 2026-08-19 15:08:55
```

> **Every population figure above is a photograph and decays; every object figure does not.**
> `581`, `10 of 581`, `0 ACTIVE`, `72`, `174`, `16`, `25`, `57` are population. `9d744eb7… ABSENT`,
> `4 of 4 mode 100644`, `65 vs 66`, the per-ref matrix, and *"the gate blocks on 5 identifiers"* are
> object facts about named objects, and they change only when someone changes those objects.
> **Check the class before concluding that anything moved.**

---

## 13 · How this record's reviews are to be handled

1. This record is **frozen by commit, not by `git hash-object -w`** — the loose-object route is what
   left design v1 with a cited hash and no object (N-3), and what left both protocol reviews bound
   to unreferenced bytes. Reviewers are to be given a **ref-reachable** object or a path plus a
   commit id. 🔴 **Until B-1 is answered this record is untracked like the other seven, and this
   clause describes what should happen, not what has.**
2. Findings live in a **separate register**, named before dispatch:
   `learning/orchestrator/READINESS-001-REVIEW-FINDINGS-REGISTER.md`. Nothing is written into a
   reviewed object — the rule X-1 discovered by violating it.
3. Integration produces a **successor**, `LEGEND_OPERATIONAL_READINESS_PLAN_FINAL_v1.md`. This
   revision is not edited.
4. A finding not acted on **says why**. Silence is not a disposition.
5. **A finding is not a blocker unless the operator makes it one.** No reviewer of this record holds
   authority over it, and neither does its author.
6. 🔴 **The reviewers of phases 2 and 3 will almost certainly not be the registered `mirror` and
   `plan` seats** — that has now been the case on three consecutive days of review. Each review is
   to record its own standing, unprompted, as the previous four did. **Findings need no actorhood;
   authority does.**
