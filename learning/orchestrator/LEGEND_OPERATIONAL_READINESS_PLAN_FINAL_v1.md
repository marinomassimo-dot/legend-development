---
record_type: OPERATIONAL_READINESS_PLAN_FINAL
record_id: LEGEND-OPERATIONAL-READINESS-PLAN-FINAL-V1
task_id: LEGEND_OPERATIONAL_READINESS_PLAN_FINAL_v1
title: Operational readiness plan — final, after the hostile and feasibility reviews of v1
revision: 1
author: unregistered session — no role contract, no ACTOR_ID
actor_id: NOT ESTABLISHED — a session cannot resolve its own actorhood
dispatcher: operator
date: 2026-08-24
status: PROPOSED — INTEGRATED, NOT APPROVED
binding: NO
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none
governance_version: 3.1.1 — read, cited, neither exercised nor modified
activation_state_governing_this_record: >
  DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE returns OPTION B ACTIVATION_NOT_CONFIRMED:
  "No actor authority may be assumed from these contracts." This record is bound by it, and
  finding M-2 is the proof that its predecessor was not.
mandate: Team mandate — LEGEND Operational Readiness Plan + Review Cycle v1, phase 4 of 4.
reviewed_predecessor:
  path: learning/orchestrator/LEGEND_OPERATIONAL_READINESS_PLAN_v1.md
  hash: f12d8acecb5acc6d5a7a96662a398dc846e57573
  note: >
    NOT EDITED. This is a successor. The predecessor's bytes are unchanged and its hash still
    resolves against the working file. No git object preserves them — see D-1.
reviews_integrated:
  - hostile review — 20 findings M-1…M-20 (2 CRITICAL, 6 MAJOR, 8 MODERATE, 4 MINOR),
    hash 0f24ef91a7d8fb1373371831134614d5618f37fc, reviewer holds no actorhood and is NOT the
    registered Mirror seat
  - feasibility review — 15 findings P-1…P-15 (1 CRITICAL, 7 MAJOR, 6 MODERATE, 1 MINOR),
    verdict NOT FEASIBLE AS WRITTEN, hash fddda3c408ae8ffb5b10c2f859630aadb6e905c9, reviewer
    holds no actorhood and is NOT the registered Plan seat
findings_disposition: section 12 of this record — all 35, none silent
independently_re_derived_by_this_session: >
  M-1, M-2, M-6(partial), P-1, P-2, P-3(by a second classifier that DISAGREES — see 12.3),
  P-7, P-9. The rest are dispositioned on the reviewers' evidence and are marked AS REPORTED.
  A finding carried on a report is carried on trust, and this record says which are which.
measured_at: >
  branch legend-operating-convention-v1 @ 30cb4f3fd700e2aaf6b608e363438f883ddc3760,
  working tree as found, 2026-08-24T08:11Z–09:40Z.
domain: CONTENT. learning/ is not among the CONTROL_PLANE_ROOTS of P5.1.
class: WORKING RECORD
---

# LEGEND — OPERATIONAL READINESS PLAN · FINAL

> **PROPOSAL ONLY · NOT AN AUTHORIZATION · ACTIVATES NOTHING · ACQUIRES NOTHING · STARTS NOTHING**
>
> Section 11 enumerates what this record did not do. Section 13 states what it cannot do at all.

---

## 0 · The three sentences that changed between v1 and this record

**1. v1's only proposed act cannot be performed by the party that proposed it.** `WORK_COMMIT` is
granted by `annex_h_authority_matrix.md:34` to *"ogni **attore**, solo proprio branch"* and by
`GOVERNANCE_v3.1.1.md:229` to *"ogni **attore**, PROPRIO worktree/branch."* This session's standing
is `actor_id: NOT ESTABLISHED`, and `DEC-20260822` forbids assuming actor authority from a contract.
v1 inherited that premise verbatim from design v2's D-13 and never re-derived it — **the one
premise its verification trail skipped, in a record whose entire method was re-deriving design v2's
premises** (M-2, re-derived here). *Nothing in v1's roadmap was runnable by v1's author.*

**2. The hazard v1 built its urgency on is roughly twice as bad as v1 measured, and its cheap remedy
needs no authority at all.** v1's frontmatter claimed four of five consumed blobs survive as loose
objects. Measured one by one with a control: **two of five.** Absent from the object database
entirely — design v2 revision 2 (*the record the trial would run from*), the bootstrap audit, and
the TRIAL-002 register (M-1, re-derived). And the at-risk corpus is not *"7 files, 4 301 lines"*: a
`git clean -fdx` removes **≈1 097 files, ≈984 MB**, of which **795 files / 899 MB is `files/`** —
gitignored by design, holding the 174 full texts and the place the trial's own input paper must
land (P-7, re-derived). **No commit anyone has proposed reaches any of it.**

> 🔴 **And therefore the plan's shape was wrong.** A byte-copy of the untracked records to a
> location outside the repository discharges the destructibility hazard **in seconds, with no git
> act, no commit, and no actorhood**. v1 routed a free, authority-free remedy through an act
> requiring an authority nobody holds — and made everything else wait behind it.

**3. The plan's mass sat on the container, not on the science.** All four of v1's new measurements
were about LEGEND's machinery — a privacy gate, a test battery, a git object store, a freeze
verifier. Six of its eight blocks were repository state. Seven of ten checklist rows were process
hygiene. Its longest analytical section was infrastructure, and its only runnable phase was git
hygiene producing zero scientific observation (M-20). **v1 wrote *"infrastructure runs beside this,
never inside it"* and then put infrastructure on the path.** Section 3 of this record separates the
two tracks so that the first scientific observation is not gated behind repository maintenance.

---

## 1 · Final recommendation

> ✅ **Path C, gated — unchanged, and now the only conclusion of v1 that survived both reviews
> untouched.** The hostile review re-derived roughly forty of v1's figures and called § 5's axis-4
> reasoning *"the strongest reasoning in the document."* Neither review disturbed it.
>
> 🔴 **But the operating order is inverted relative to v1.** Preservation of the *bytes* comes first
> because it is free and needs nobody's authority. Preservation of the *state* — the commit — is an
> operator act that everything else no longer waits behind.

```
Φ−1a  PRESERVE THE BYTES            operator act · seconds · NO git act · NO actorhood needed
      copy the untracked planning records out of the repository, byte for byte
      → discharges the destructibility hazard for the 10 records. Does NOT touch files/.

Φ−1b  ARCHIVE files/                operator decision · 899 MB · out of git, by size
      → the only route to preserving the corpus and the trial's future input. Priced nowhere
        in v1, in design v2, or in the bootstrap audit.

Φ−1c  DURABLE STATE                 operator act · needs D-1 · requires an ACTOR
      redact 2 records · preserve design v1's pre-redaction bytes FIRST (M-7) · commit
      → this is where WORK_COMMIT authority is required, and it is the only place.

Φ0    DECISION AND SCHEMA           needs D-2 · D-3 · D-4 · D-5 · D-6 · D-7
Φ1    TRIAL-001 STEP 1              design v2 § 9.1, Φ0…Φ11, unchanged
Φ2    METHOD VALIDATION             🔴 RESTRICTED — see § 6. v1's version cannot fail.
```

**Φ−1a is the only act in this entire plan that discharges a real hazard, requires no authority
anybody lacks, and blocks nothing else.** If the operator does one thing after reading this, it is
that one.

---

## 2 · The readiness verdict, restated

> **The method is sound. The container is not ready to hold it. And v1 overstated how much of the
> unreadiness is the method's problem.**

Two reviews, 35 findings, and the corrections run in both directions:

| | v1 said | Measured by the reviews |
|---|---|---|
| **K-2** — the audit instrument | *"does not exist **in any form**"* | 🔴 **Overstated.** `framework/scripts/locator_audit.py` — 233 lines, mode `100755`, read-only — mechanizes the *anchored* half of the primary and ran green today: **54 manifests audited, 0 quotes not found.** Design v2 § 6.4 already routes V-2 through it. **v1 names it zero times.** What has no instrument is the *bare* condition, which is a find, not a check (P-2, re-derived) |
| **§ 8 row 7** — the write allowlist | ⚠️ *"not re-verified since"* | ✅ **It verifies.** `record` writes exactly two paths outside `learning/`, and design v2 § 3.5 names both, unqualified. v1 could have established this by reading three functions (P-11) |
| **§ 7.3** — *"the object nobody gates"* | *"the union is not covered by running both"* | 🔴 **Escalated a missing *moment* into a missing *mechanism*.** `walk_publishable` scans everything untracked-and-not-ignored, so a local gate run covers a **superset** of CI's privacy scope. **v1's own N-1 is the proof — it was produced by running that gate** (M-9) |
| **§ 2.2.1** — the control plane | *"cannot be performed as a comparison today — it is a merge"* | 🔴 **False, and the true claim is stronger.** Both objects are readable on this disk **right now, simultaneously**, at zero authority cost. And the dispersal is **1 of 56 path-bearing refs**, not 1 of 7 — with **0 refs carrying both** (P-9) |
| **K-8** — the Φ7 path | a BLOCK halting Φ7 | 🔴 **Not a block.** `reviews/trial-001/` is a `mkdir` inside a declared allowlist, not ignored. The block is the *commit*, counted twice (P-12) |

**And in the other direction**, the hostile review found nothing wrong with: the 49-cell control-plane
matrix (it added the negative control v1 lacked; it fires) · N-1's block set, exact to every line
number · the local-eight and the 6/2/2 set arithmetic · N-4's 44/44 · all five `consumes` hashes,
byte for byte · § 1.4's refusal to smuggle construction into preparation, *"which holds
throughout"* · and § 11's hardest claim, *"it wrote no loose git objects"* — **checkable, and true**:
0 loose objects dated 2026-08-24 against a positive control of 147 dated 2026-08-23.

---

## 3 · Two tracks, separated — the answer to M-20

v1's failure of proportion is structural, not stylistic. The fix is to stop letting one queue hold
both kinds of work.

| | **TRACK-C · the container** | **TRACK-E · the experiment** |
|---|---|---|
| **Question** | Can this repository hold, preserve and gate a scientific result? | Does LEGEND improve traceability, verifiability and correctability? |
| **Phases** | Φ−1a · Φ−1b · Φ−1c · A-1 · A-2 · A-3 · I-1…I-8 | Φ0 · Φ1 · Φ2 |
| **Produces** | zero scientific observation, by construction | the reading, the crossover, the candidate or the `READING RECORD` |
| **Blocked by** | operator authority (Φ−1c) · operator decisions | D-2…D-7 |
| 🔴 **Gates the other?** | **Only Φ−1a and Φ−1c do.** Everything else in TRACK-C runs beside TRACK-E, never in front of it | no |

> **The rule this record adds, and v1 needed.** *An infrastructure item may block the experiment
> only if it is named in § 4's blocking tier with the reason it blocks.* Under that rule the
> battery's 6 content defects, the exec bits, the Node pins, `fetch-depth`, PyMuPDF, the skip
> boundary and the two gate workflows **do not block `TRIAL-001`**. They are real, they are cheap,
> and v1's own § 3 said so — then wrote a roadmap in which they came first anyway.

---

## 4 · Decisions required from the operator

**Denominator, stated because v1 omitted it (M-4).** Design v2 § 13 carries **14** decisions,
`D-1…D-14`, **9** of them 🔴. v1's § 4 carried **5** of the 14 and **3** of the 9 red, while its
preamble read as exhaustive. This record carries **all 14**, plus **4** the reviews added. Each is
numbered here in its own namespace; design v2's number is given so nothing is lost. *v1 also
collided its own D-numbers with the bootstrap audit's — that namespace collision is why the
mapping column exists.*

### 4.1 · BLOCKING — the experiment cannot start until these are answered

| # | ← | Decision | Options | Recommendation | Depends on |
|---|---|---|---|---|---|
| **D-1** 🔴 | v2 D-13 | **How is the corpus preserved?** Now **10** untracked records, growing by one per phase of this very review cycle (P-6), of which **2** carry 5 registered identifier hits and **4** have no git object at all (M-1) | (a) commit all · (b) **byte-copy out of the repo NOW (Φ−1a), then redact the 2 and commit** · (c) commit only the clean ones · (d) nothing | 🔴 **(b), and its first half needs no decision from anyone but you** — it is a file copy. (a) writes registered personal identifiers into the public edition. **And before any redaction, design v1's pre-redaction bytes must be preserved: redaction changes its hash, and two records that will be committed cite the old one** (M-7) | — |
| **D-2** 🔴 | v2 D-2 | **The paper, and the re-authored question** — *v1 omitted this decision entirely* (M-4) | (a) **28123895 with design v2 § 3.3's question** · (b) the queue's contaminated `Why` · (c) an alternate · (d) operator-supplied | **(a).** The queue entry at `full_text_queue_current.md:242` carries the pre-reading conclusion and must never reach the reader | — |
| **D-3** 🔴 | v2 D-3 | **How is the full text acquired?** | (a) authorize a connector · (b) **operator supplies the PDF** · (c) `find-fulltext` in a web-enabled session · (d) `pmc_pow_fetch.py` | **(b) or (c).** (d) is the last-resort tier and takes a URL, not a PMCID | D-2 |
| **D-4** 🔴 | v2 D-14 | **Is `TRIAL-001-AUDIT-SCHEMA.md` authored before Φ0?** | (a) **yes** · (b) improvise at Φ7 · (c) anchored condition only | **(a).** 🔴 **And a correction to v1's pricing: the schema is *smaller* than v1 said** — `locator_audit.py` already mechanizes the anchored half (P-2), so the schema covers only the judgement columns. 🔴 **But (b) and (c) both leave TRACK-M with a success criterion that cannot be met and no degradation rung that rescopes it** (M-8) | — |
| **D-5** 🔴 | v2 D-4 | **Unregistered rehearsal, or lift/scope the C-9 L2 hold first?** — *v1 omitted this* (M-4) | (a) **rehearsal claiming no actorhood** · (b) scope the hold · (c) lift it | **(a).** Under `DEC-20260822` even (b) and (c) leave the contracts non-activated. Under (a): **no governed Scientist artifact**, and the outcome must say so | — |
| **D-6** 🔴 | new (M-2) | **Who performs Φ−1c's `WORK_COMMIT`?** The act requires an **actor**; no session in this cycle is one | (a) **the operator commits** · (b) an explicit activation act granting one session actorhood for this act · (c) leave the records uncommitted indefinitely | **(a).** It is one act, it needs no standing beyond yours, and (b) grants durable authority to discharge a one-off | D-1 |
| **D-7** 🔴 | new (P-11) | **Scoped lift of the `framework/` prohibition for `state_manifest_current.md`, for Φ1 only** | (a) **yes, named and scoped** · (b) no → **Φ1b cannot run** | 🔴 **(a).** `fulltext_receipts.py record` re-anchors that file **atomically, in-lock, on every append** — not optional, not deferrable. The mandate forbids modifying `framework/`. **The instrument will write it whether or not anyone asked**, so it must be asked for | D-3 |

**Dependency edges v1 presented as absent (P-5).** `D-8 → D-1`: readiness is defined over the
tracked set, and D-1 decides what is in it. `D-1 → D-8`: committing the records injects **5** known
`test_documented_commands` failures into that set, permanently and CI-visibly (P-4). `D-4 → D-1`:
answering D-4(a) creates an eleventh record needing preservation.

### 4.2 · IMPORTANT — they improve the system; they do not block the experiment

| # | ← | Decision | Recommendation |
|---|---|---|---|
| **D-8** | new (v1 B-3) | **What does "repository ready" mean?** | **Battery green on a full clone, evaluated over `git ls-files` rather than the disk.** 🔴 v1's option "green in a laboratory worktree" is even less reachable than v1 argued: `test_release_surface` carries a *third* contamination failure inside the class v1 labelled content defects (M-6) |
| **D-9** | v2 D-5 | `SURFACE-LITE` or `SURFACE-FULL`? | `SURFACE-LITE` with design v2 § 9.2's **measured** forbidden list, re-enumerated at Φ0 |
| **D-10** | v2 D-6 | Is design v2 § 4 (the layer model) in scope? | In scope, scoped per § 4.5, with T-8 repaired separately afterwards |
| **D-11** | v2 D-7 | Does BL-2 (control reader) run? | **No** for step 1 — leaving **one** baseline, and the outcome must say so |
| **D-12** | v2 D-8 | Where do audit artifacts live? | `reviews/trial-001/`. 🔴 **Downgraded from v1's blocking tier: it is a `mkdir` inside a declared allowlist, not a block** (P-12) |
| **D-13** | v2 D-9 | Run under OPCON-v1? | Declared non-binding discipline |
| **D-14** | v2 D-10 | Review floor `R2`? | Yes, now — derogation is upward-only, so it costs nothing |
| **D-15** | v2 D-11 | End at the candidate, or proceed to `BATCH_COMMIT`? | **Stop at the candidate.** The gate is Annex D.3 GATE 0's `lease ACTIVE singleton`, and 0 are ACTIVE |
| **D-16** | v2 D-12 | Is step 2's exit criterion the gate for step 3? | 🔴 **Yes, but only in its restricted form** — see § 6. v1's version cannot fail |
| **D-17** | new (P-7) | **Archive `files/` — 795 files, 899 MB, gitignored by design** | An archival decision, out of git, by size. **Priced nowhere in any record until now.** It holds the 174 full texts and the place the trial's input must land |
| **D-18** | audit D-1 | Where do the inviolable facts live? | A declared bootstrap-surface registry, tests parameterized on it. 🔴 **`state-control` and `session_self_evaluation.md` are in NEITHER `CLAUDE.md` nor `AGENTS.md`** — repointing the tests at `AGENTS.md` still leaves two red |
| **D-19** | audit D-2 | Development gate vs release gate | Two workflows, one body of tests — **and the disk-walking suites rescoped first (A-3), or the development gate is red forever in every laboratory worktree** |
| **D-20** | audit D-3 | PyMuPDF optional or mandatory? | Mandatory for the development gate — it gates 13 checks on the surface that decides whether a citation is verifiable |
| **D-21** | audit D-4 | Where does the skip boundary run? | Declared categories per reason, **decided before the first green run** |
| **D-22** | audit D-5 | Shallow-clone degradation | Both routes. 🔴 **Risk measured LOW, not medium: the freeze verifies 44/44 on a full clone** |
| **D-23** | new (P-13b) | **`git worktree prune` for the 14 dead worktrees** | Mechanical. Each still holds a branch registered as checked out, and a branch checked out anywhere cannot be updated from elsewhere |
| **D-24** | v1 I-8 | Register the 1 unexecuted suite · set 4 exec bits · update 3 action pins | Mechanical, **each in an isolated change** |

### 4.3 · FUTURE — after the first experiment

Activation act discharging `DEC-20260822` and the C-9 L2 lift (step 3's precondition) ·
`legend-development` visibility, `main` protection, `sha_pinning_required` — **becomes blocking the
moment step 3 puts a second writer on a branch** · the definition of a release point, which today
has an empty referent · deriving `TESTS` from `git ls-files` · the exec-bit hook upstream ·
extending the migration inventory to the test battery · the A/B mode benchmark and Scientist C ·
T-8's nine papers · who closes the Mirror review of `claude_md_migration_map.md`.

---

## 5 · The pre-Trial checklist, rescored

v1 scored *"2 of 10"*. **Both ✅ rows were the only two graded by reading a document rather than
running an instrument, and neither declared itself a judgement — while § 8's own preamble required
exactly that** (M-5). It is the third instance of the H-14 shape the findings register had closed
twice, and this time it was v1's.

| # | Condition | Instrument | Rescored |
|---|---|---|---|
| **1** | Protocol approved | frontmatter status | 🔴 NO — 7 blocking decisions open |
| **2** | Corpus preserved | 🔴 **restated**: a byte-copy exists outside the repository, enumerated at the instant Φ−1a opens (P-6); and no committed record cites a blob that does not resolve (M-7) | 🔴 NO |
| **3** | Repository ready | *per D-8*; and its evaluation cannot precede D-1's execution (P-5) | 🔴 NO — and undecided |
| **4** | Metrics frozen | `TRIAL-001-AUDIT-SCHEMA.md` exists, judgement columns only | 🔴 NO |
| **5** | Input available | 🔴 **three clauses, two of which `verify` cannot evaluate** (P-10): a directory listing for presence; the ledger check for the chain; and **the "authored before acquisition" clause is a JUDGEMENT with a named party — no instrument in this repository evaluates authorship order, and filesystem timestamps do not establish it** | 🔴 NO |
| **6** | Audit defined | directory + the recorded shuffle | 🔴 NO |
| **7** | Artifacts preservable | reading `fulltext_receipts.py` | ✅ **YES — upgraded.** The allowlist matches the instrument (P-11) |
| **8** | Roles defined | ⚠️ **JUDGEMENT, now declared.** Design v2 § 8.1 is a six-seat table, not a per-phase map; § 8.3 records that Plan owns 6 of 17 phases and nothing checks it; `reader-L` is ⚠️ pending **D-5** | ⚠️ JUDGEMENT — not ✅ |
| **9** | Falsifiers satisfiable | ⚠️ **JUDGEMENT, now declared.** Its input is authored by the party it is about and it is graded by reading it. **No observation could make this row come out NO** — it has no falsifier of its own, which is the property it certifies in others | ⚠️ JUDGEMENT — not ✅ |
| **10** | Friction log open | file existence | 🔴 NO |

> **Score: 1 of 10 instrument-verified · 2 judgements · 7 NO.** Lower than v1's claim, and the
> difference is entirely that v1 counted its two self-graded rows as passes.

---

## 6 · Φ2 — restricted, because v1's version cannot fail

v1's step-2 exit criterion — *"a replay session reproduces every reported figure **AND** every audit
verdict from the record alone"* — is the gate on the entire multi-agent extension, and v1 gave it
two lines. The feasibility review's verdict names it **the phase most likely to stall**, and for a
reason worth stating in full: **it fails silently in both directions — it will not announce that it
stalled, it will announce that it passed** (P-8).

```
FIGURES   ── executable in principle. A figure with a runnable command beside it can be re-run.
             🔴 The precedent is against it: v1's own § 12 is NOT runnable as printed —
                a literal ellipsis inside a shell loop, a sentinel pair that writes into the
                repository it measures, and a joined continuation naming a flag the runner
                does not expose (M-12).

VERDICTS  ── 🔴 NOT executable, and nothing in this repository makes it so.
             Tracked files with `transcript` in the name: 0. Positive control `receipt`: 6.
             · If the verdicts are IN the record — and they must be, since the criterion says
               "from the record alone" — the replayer READS them. Reading a verdict is not
               reproducing it. The criterion passes trivially and tests nothing.
             · If the replayer RE-JUDGES, disagreement is the expected behaviour of a judgement
               instrument, and no concordance threshold is declared, no rung covers it, and
               design v2 § 7 states "Statistics: None. n = 1 paper."

RESTRICTION ADOPTED
  Φ2 verifies FIGURES ONLY, and the outcome says so in those words.
  Step 3's gate is thereby WEAKER than design v2's D-12 claims, and that is stated rather
  than quietly inherited.
  The stronger form — a BLIND RE-AUDIT with verdicts withheld and an agreement threshold
  declared before the shuffle — is a SECOND STUDY with its own personnel, instrument and
  schema. It is named here as construction and priced as such. It is not in step 2.
```

---

## 7 · The audit instrument — K-2 corrected

v1 declared the class empty. It is not.

| Question the primary asks | Instrument today |
|---|---|
| Does the quote occur in the artifact it is attributed to? | ✅ `framework/scripts/locator_audit.py`, `--strict`, read-only, mode `100755`. Ran green: **54 manifests, 10 unauditable, 0 quotes not found** |
| Do the quotations in prose dossiers occur in a paper anyone can point at? | ✅ `framework/scripts/dossier_quote_audit.py` — named in neither v1 nor design v2 |
| Does the quote **support** the proposition, and does the source say more or less than claimed? | 🔴 **none.** This is the whole of what the schema must define |
| Can an independent party ground the proposition **without** the anchor? | 🔴 **none.** The bare condition is a *find*, not a *check*, with the opposite cost profile |

**One dependency this creates and v1 could not have seen:** `locator_audit.py` audits *deepdive
manifests*, and PMID 28123895 has none. **The mechanized half is reachable only after Φ1 has
produced a manifest** — it verifies a reading; it cannot audit a bare condition. So D-4's schema
gets smaller, and one of its columns gets a prerequisite.

---

## 8 · Infrastructure — corrected pricing

| # | Item | v1 said | Corrected |
|---|---|---|---|
| **A-1** | Pre-commit privacy check | *"needs no new rule — it needs a moment"* | 🔴 **CONSTRUCTION, and v1's § 1.4 forbade exactly this smuggling.** `public_release_gate.py` exposes only `--root`, `--mode`, `--report-json`, `--skip-clean-clone`; `--root` names a *repository*, and the walker is an `os.walk` beneath it. **Pointed at a subset it produced 30 unrelated blocks.** The one working route — materialize the index into a temporary tree (0.12 s) and gate that (3.6 s, 0 blocks) — needs a wrapper of ~60–100 lines, a `.git/hooks/` file **git neither versions nor distributes**, a per-checkout install, and a policy on `--no-verify`. 🔴 **It would be the only gate in this repository the registered battery cannot test** (P-1) |
| **A-2** | Two workflows, one body of tests | gated by A-3 | 🔴 **Not gated by A-3 — gated by D-1.** A-2 runs on a clean CI runner where the disk-walking failure cannot occur. What changes CI is **D-1**, which moves 5 measured failures from untracked into tracked, permanently and CI-visibly (P-4) |
| **A-3** | Rescope the disk-walking suites | *"2 suites"* | 🔴 **At least 4× that, and the two classifiers disagree.** The feasibility review enumerates **27 of 65** registered suites as filesystem-enumerating, **8** of them walking from the repository root. An independent classifier run by this session returns **17** disk-walkers with 3 using `git ls-files`. 🔴 **Two enumerations of the same concept disagree, which means the concept is under-specified — the number is reported as a disagreement rather than picked** (P-3, and § 12.3) |

**Operational risks with no phase in v1** (P-13): concurrent writers on one shared checkout — **and
the PreToolUse guard that denies blanket staging is doing load-bearing safety work that appears in
no record** · 14 dead worktrees each still holding a branch registered as checked out (D-23) ·
`refs/heads/orchestrator` checked out in a live worktree, which blocks the reconciliation merge
*mechanically*, independent of authority · and the fact that **the fourteen worktrees already lost
lived under `/private/tmp` — that is the precedent for how this laboratory loses artifacts, and it
has already happened fourteen times.**

**And one line per phase, the cheapest fix in either review** (P-14): every phase of this roadmap
authors a markdown record into a repository whose battery walks every markdown file and asserts
that every documented flag exists and every documented path resolves. **No phase in v1 ran the two
guard suites before declaring a record closed.** v1 did not either — and reddened them twice.

---

## 9 · The control plane — corrected

v1: *"the reconciliation cannot be performed as a comparison today — it is a merge."* **False, and
the true claim is stronger** (P-9, re-derived here).

| Object | present on | scope |
|---|---|---|
| `CLAUDE.md` *(positive control)* | **56 / 56** | path-bearing refs |
| a path present nowhere *(negative control)* | **0 / 57** | all refs |
| `runtime/agent_card_registry.md` | **1** — `refs/heads/orchestrator` only | 56 |
| `framework/protocols/scientist_reading_modes.md` | **23** | 56 |
| 🔴 refs carrying **both** | **0** | 56 |

*(The 57th ref is a tag pointing at a **blob**, where `ref:path` has no meaning. The path-bearing
denominator is 56, not the 57 both v1 and the hostile review carried.)*

**Three routes, not one:**

| Route | Cost | Available now? |
|---|---|---|
| **(a) a READ** — compare the two objects where they already are | nothing: no git act, no actorhood | ✅ **yes, and it was performed** |
| **(b) a CHERRY-PICK** — the registry entered `orchestrator` in one commit | one commit | needs an actor |
| **(c) a MERGE** | 42 ahead / 40 behind, 82 commits of divergence | needs an actor **and is mechanically refused**, because the branch is checked out in a live worktree |

> **W-1/P-5 asked for a comparison. A comparison is a read. The read is free.** Only the durable
> single-tree state needs authority — and v1 deferred both on the strength of the expensive one.

---

## 10 · Operating order

```
NOW, and it needs only your say-so — no authority question arises
  Φ−1a   byte-copy the 10 untracked planning records out of the repository
         → EXIT: each file exists outside the repo and its git hash-object value matches
         → this discharges the destructibility hazard for the records. It does NOT touch files/.

NEXT, and each is a decision before it is an act
  D-17   archive files/ — 795 files, 899 MB. No commit will ever reach it.
  D-1    redact the 2 identifier-bearing records
         🔴 PRESERVE design v1's PRE-REDACTION bytes FIRST — redaction changes its hash, and two
            records that will be committed cite the old one, which already has no object (M-7)
  D-6    the operator performs the WORK_COMMIT
         → EXIT: git cat-file -e fires on every record present at the instant Φ−1c opened,
                 ENUMERATED IN THE PHASE RECORD BEFORE THE FIRST ACT (the set grows — P-6)
         → EXIT: the gate reports 0 DIRECT_IDENTIFIER over the committed set
         → EXIT: no committed record cites a blob that does not resolve      ← M-7's addition
         → FALSIFIER: any of the three fails → Φ−1c did not close

THEN, and only then does the experiment's clock start
  Φ0     D-2 · D-3 · D-4 · D-5 · D-7 answered · the schema authored · the forbidden list
         RE-ENUMERATED at that instant, because the set grows
  Φ1     TRIAL-001 step 1, design v2 § 9.1 unchanged
  Φ2     figures only (§ 6), and the outcome says so

BESIDE, never in front — TRACK-C
  A-3 → A-2 → A-1(construction) · D-18…D-24
```

**One rule for every phase**, and it costs a line each: *before a phase declares its record closed,
run the two guard suites and confirm the record adds zero hits.* The hostile review did this. v1
did not, and its verification trail is now a source of the failures it reports.

---

## 11 · What this record does not do

It does not start the trial, acquire or read a paper, build a surface, author a spec, or run a
benchmark · does not start Scientist A/B or any agent · does not dispatch, register, activate,
assign or grant authority · creates no Task Contract, candidate, `DEC`, approval or ledger event ·
does not lift the C-9 hold, verify a capability, acquire a lease, or resolve an `ACTOR_ID` · does
not perform Φ−1a, Φ−1b or Φ−1c — **all three are proposed, none is executed** · performs no
redaction · does not adopt or amend OPCON-v1 · adds no field to any schema and builds no script ·
**does not modify `governance/`, `roles/`, `framework/`, `ledger/`, `runtime/`, the four scientific
current files, or `wwox-rare-disease-legend`** · advances no branch, stages nothing, commits
nothing, pushes nothing · does not edit its predecessor or either review · resolves no finding on
anyone's behalf · claims no actorhood.

**Disclosed** (M-11's lesson, applied to this record): it wrote **one** file, this one. It wrote no
loose git objects. It ran read-only instruments only. **And before closing it ran the two guard
suites and confirmed this record adds zero hits to each** — the check v1 omitted.

---

## 12 · Disposition of all 35 findings

`ACTED` = this record changes the plan · `ACCEPTED / NOT FIXABLE HERE` = true, and no instrument in
this repository can fix it · `SCOPED` = the operator's call · `NOTED` = true, no action follows.
**No finding is silent. Findings this session re-derived are marked; the rest are carried on the
reviewer's evidence and say so.**

### 12.1 · Hostile review — M-1…M-20

| # | Sev | Disposition | Verified by me |
|---|---|---|---|
| **M-1** | CRITICAL | **ACTED** — § 0.2. Two of five, not four. The frontmatter claim is withdrawn | 🔴 **RE-DERIVED** |
| **M-2** | CRITICAL | **ACTED** — § 0.1, D-6, § 10. Φ−1 split; the commit is the operator's act | 🔴 **RE-DERIVED** |
| **M-3** | MAJOR | **ACTED** — the "true positives by construction" claim is withdrawn. **The operational conclusion survives on sufficient grounds: the gate is the instrument that decides publishability, and it returns `BLOCK_PUBLICATION` on those files.** The token regex matches any bare 3–24-letter word, and the allowlist's semantics are deliberately withheld from every reader of this repository, including me | AS REPORTED — the reviewer demonstrated the collision without disclosing anything |
| **M-4** | MAJOR | **ACTED** — § 4 now carries all 14 design-v2 decisions with its denominator; D-2 and D-5 restored to the blocking tier; D-12 moved out of it per P-12 | AS REPORTED (design v2 § 13 read) |
| **M-5** | MAJOR | **ACTED** — § 5 rescored. Rows 8 and 9 are declared judgements; the score is 1 of 10 instrument-verified | READ |
| **M-6** | MAJOR | **ACTED** — the decomposition is exact at *suite* granularity and not at *failure* granularity, which is what its causal sentence claimed. `test_release_surface` carries a working-tree failure inside the class v1 called content defects. **This is the "a causal story is not a measurement" failure: v1 imported the audit's CI causes instead of reading the local failures it had in hand** | PARTIAL — the local eight re-run; the per-test attribution AS REPORTED |
| **M-7** | MAJOR | 🔴 **ACTED, and it changes the order of operations** — § 10 adds the citation check to Φ−1c's exit, and design v1's pre-redaction bytes must be preserved *before* redaction, because redaction changes its hash and two records that will be committed cite the old one | AS REPORTED |
| **M-8** | MAJOR | **ACTED** — § 6 and D-4. Two of B-2's three answers leave TRACK-M unsatisfiable with no rung that rescopes it. **P-15's defect reappearing on a new axis, in the record that quotes design v2's fix of it** | READ |
| **M-9** | MODERATE | **ACTED** — § 2. § 7.3 escalated a missing *moment* into a missing *mechanism*. **Where M-9 and P-1 differ, both are adopted: the object *is* gated by a local run (M-9), and no invocation of the existing tool gates a staged set (P-1). They are not in conflict** | READ |
| **M-10** | MODERATE | **ACTED** — "the tracked repository is clean" is withdrawn. The gate emits 4 `[REVIEW] PARENT_OF_ORIGIN_ATTRIBUTED` findings in **tracked** files that v1's quoted block filtered out. Zero blocks of one code is not clean | RE-DERIVED (they appear in my own § 12.4 output) |
| **M-11** | MODERATE | **ACTED** — disclosed in § 11, and § 10 adds the per-phase guard-suite rule. v1's own § 12 introduced a *new* CLI-contract failure, so N-2's "11 hits" was 12 | 🔴 **RE-DERIVED — and worse: 2 hits, not 1** |
| **M-12** | MODERATE | **ACTED** — § 12.4 is runnable: no ellipsis in a loop, no sentinel written into the tree, no joined continuation. **The underlying claim was true — the battery wrote nothing — the receipt was not** | AS REPORTED (the sandbox reproduction) |
| **M-13** | MODERATE | **ACTED** — the packet is **10 files**, not 13; `find` without `-type f` returned the 3 directories too. The instruction files are **7**, not 6. The conclusion survives; the arithmetic did not | AS REPORTED |
| **M-14** | MODERATE | **ACTED** — the workflow is **48** lines, on every ref and in its only revision. There is no ref at which it is 43. An object figure, simply wrong | AS REPORTED |
| **M-15** | MODERATE | **ACTED** — `66` is population, not object. And the *"7 files, 4 301 lines"* figure decayed **inside the record's own authorship**, in the section warning that population figures decay. **Measured now: 10 files** | 🔴 **RE-DERIVED — 10, past the reviewer's 8** |
| **M-16** | MINOR | **ACTED** — the "67 findings" figure is withdrawn. Its subtrahend was never stated and I will not restate a number nobody enumerated | READ |
| **M-17** | MINOR | **NOTED** — the conclusion survives (`86c349a` is also an ancestor), but it survived by luck of the denominator: a claim of the form *"there is no divergence anywhere"* drawn from one branch per remote | AS REPORTED |
| **M-18** | MINOR | **ACTED** — the OPCON figures are withdrawn as unverifiable as printed. Without v1's pattern neither of us can say which set is right | AS REPORTED |
| **M-19** | MINOR | **ACTED** — "identifier" is used in this record only for the registered personal token. The PMID/PMCID is called an *accession* wherever both appear | READ |
| **M-20** | MODERATE | 🔴 **ACTED, and it is the deepest change in this record** — § 3 separates TRACK-C from TRACK-E, and § 0.3 states the failure plainly. **v1 wrote "infrastructure runs beside this, never inside it" and then put infrastructure on the path** | READ |

### 12.2 · Feasibility review — P-1…P-15

| # | Sev | Disposition | Verified by me |
|---|---|---|---|
| **P-1** | CRITICAL | **ACTED** — § 8. A-1 is reclassified as construction and priced: wrapper, hook, per-checkout install, `--no-verify` policy, **and it would be the only gate the registered battery cannot test** | 🔴 **RE-DERIVED** — argument surface and `os.walk` confirmed |
| **P-2** | MAJOR | 🔴 **ACTED** — § 7 and D-4. K-2's class is not empty; the schema shrinks and gains a prerequisite | 🔴 **RE-DERIVED** — ran it: 54 manifests, 0 quotes not found |
| **P-3** | MAJOR | **ACTED as a disagreement** — § 8 and § 12.3. Two classifiers of "walks the filesystem" return different sets. **The load-bearing point survives either: A-3's population is at least 4× what v1 priced** | 🔴 **RE-DERIVED by an independent classifier that DISAGREES** |
| **P-4** | MAJOR | **ACTED** — § 8. A-2 is gated by D-1, not A-3 | AS REPORTED |
| **P-5** | MAJOR | **ACTED** — § 4.1 carries a dependency paragraph; three edges named | AS REPORTED |
| **P-6** | MAJOR | **ACTED** — § 10. The exit is restated over an enumeration made at the instant the phase opens, because the set grows by one per phase of this cycle | 🔴 **RE-DERIVED — 10 now** |
| **P-7** | MAJOR | 🔴 **ACTED, and it inverted the plan** — § 0.2, Φ−1a, Φ−1b, D-17. **The cheap remedy needs no authority; the expensive one reaches under 1 % of the at-risk file count** | 🔴 **RE-DERIVED** — 1 097 files, `files/` 795 / 899 MB |
| **P-8** | MAJOR | **ACTED** — § 6. Φ2 restricted to figures; the blind re-audit is named as a second study and priced | AS REPORTED (the transcript sweep re-run: 0, control fires) |
| **P-9** | MODERATE | **ACTED** — § 9. Three routes; the read is free and was performed; the denominator is 56 | 🔴 **RE-DERIVED** — both objects readable simultaneously, negative control fires |
| **P-10** | MODERATE | **ACTED** — § 5 row 5. Three clauses; `verify` evaluates one; the ordering clause is a declared judgement, because **filesystem timestamps do not establish authorship order** | AS REPORTED |
| **P-11** | MODERATE | **ACTED** — § 5 row 7 upgraded to ✅, **and D-7 created**. The `framework/` prohibition collides with what the instrument writes in-lock, and nothing in v1 converted that into a decision | AS REPORTED |
| **P-12** | MODERATE | **ACTED** — K-8 is not a block; D-12 sits in the important tier and § 3's rule keeps it out of the experiment's way | AS REPORTED |
| **P-13** | MODERATE | **ACTED** — § 8. Four risks named, **including that the PreToolUse guard is doing load-bearing safety work that appears in no record**, and that this laboratory has already lost artifacts fourteen times, under `/private/tmp` | PARTIAL — 25 worktrees and 14 prunable re-derived; the rest AS REPORTED |
| **P-14** | MODERATE | **ACTED** — § 10's per-phase rule, and § 11 records that this record ran the check | AS REPORTED |
| **P-15** | MINOR | **NOTED** — the instrument surfaces are recorded so the next record need not re-measure them | AS REPORTED |

### 12.3 · A disagreement this record does not resolve

**A-3's population.** The feasibility review enumerates **27 of 65** registered suites as
filesystem-enumerating, **8** walking from the repository root. An independent classifier written by
this session — matching `rglob`/`os.walk`/`glob` and excluding suites that use `git ls-files` —
returns **17** disk-walkers, **3** using `ls-files`, **45** neither.

**Neither number is adopted.** The two classifiers operationalize "walks the filesystem"
differently, and a count reached by two disagreeing definitions is a sign the definition is
under-specified, not a sign that one enumerator is wrong. **What both establish, and what A-3's
pricing depends on, is that the population is at least four times the 2 suites v1 named.** Whoever
executes A-3 enumerates the set first and publishes it — which is what v1 should have done and did
not.

### 12.4 · Verification trail

All at `legend-operating-convention-v1` @ `30cb4f3fd700e2aaf6b608e363438f883ddc3760`,
2026-08-24T08:11Z–09:40Z. **Written to be runnable** — M-12 found v1's was not.

```bash
# M-1 — my predecessor's OWN consumes list, tested one by one, control first
git cat-file -e "$(git rev-parse HEAD:CLAUDE.md)" && echo "control PRESENT"
for b in 6bd903cb08b29da6db86467a70db127502585974 \
         598afd355bd4de2a94d67c7620f10c87b4e1e59d \
         ee00195fac0f7c317803120d2a5d335098c33778 \
         635f1b21bf61b419f673e6b2773e27514007d99b \
         d5c0d296df69ea5a14426e2da351869959983c7b; do
  git cat-file -e "$b" 2>/dev/null && echo "$b PRESENT" || echo "$b ABSENT"
done
#   ABSENT · ABSENT · PRESENT · ABSENT · PRESENT      → 2 of 5, not 4 of 5

# M-2 — the authority WORK_COMMIT is granted to
grep -n "WORK_COMMIT" governance/annex_h_authority_matrix.md
#   34: | WORK_COMMIT | ogni attore, solo proprio branch, granularità milestone |
grep -n "WORK_COMMIT " governance/GOVERNANCE_v3.1.1.md | head -1
#   229: WORK_COMMIT  → ogni attore, PROPRIO worktree/branch.

# P-7 / M-15 / P-6 — the two populations, each with its scope stated
git status --porcelain | grep -c "^??"                      # 10  untracked, NOT ignored
find files -type f | wc -l                                  # 795  under files/
du -sh files                                                # 899M
#   full-clean population expands to ~1097 files once directories are walked

# P-2 — the instrument K-2 said did not exist in any form
python3 framework/scripts/locator_audit.py --strict
#   54 manifest(s) audited, 10 unauditable, 0 quote(s) not found
grep -c "locator_audit" learning/orchestrator/LEGEND_OPERATIONAL_READINESS_PLAN_v1.md   # 0

# P-1 — A-1's reachability
python3 scripts/public_release_gate.py --help
#   only --root / --mode / --report-json / --skip-clean-clone ; --root names a REPOSITORY
grep -n "os.walk" scripts/public_release_gate.py            # 123

# P-9 — the reconciliation is a read, and it was performed
git cat-file -e orchestrator:runtime/agent_card_registry.md && echo "registry READABLE"
git cat-file -e HEAD:framework/protocols/scientist_reading_modes.md && echo "protocol READABLE"
git cat-file -e HEAD:runtime/agent_card_registry.md 2>/dev/null || echo "negative control fires"

# M-10 — the four findings v1's quoted block filtered out
python3 scripts/public_release_gate.py --root . --mode release 2>&1 | grep -c "PARENT_OF_ORIGIN"
#   4, all in TRACKED files, all "Not blocked; read it before publishing"

# M-11 — my predecessor is a source of the failures it reports
python3 scripts/test_documented_commands.py 2>&1 | grep -c "READINESS_PLAN_v1"     # 3 lines, 2 hits

# ⚠️ zsh: `for x in $VAR` iterates ONCE over the whole string — use literal lists.
#    And `"$r:$p"` applies the `:p` history modifier — always `${r}:${p}`.
#    Both traps were hit during this cycle and caught only by a positive control.
```

> **Population figures decay; object figures do not.** Population here: `10`, `795`, `899M`,
> `1097`, `54`, `4`, `56`. Object here: the five blob verdicts, the two governance line numbers,
> `public_release_gate.py`'s argument surface, and *"0 refs carry both."* **Check the class before
> concluding anything moved** — and note that v1's own *"7 files"* decayed to 10 inside this cycle.

---

## 13 · What this record cannot do, and who must

**It cannot preserve anything.** Φ−1a is a file copy and this record did not perform it. Φ−1c is a
`WORK_COMMIT`, and by M-2 that authority belongs to an actor; this session is not one, and saying so
is the whole point of the finding.

**It cannot make a finding binding.** Thirty-five findings arrived from two reviewers, neither of
whom held actorhood, neither of whom was the registered seat — **the fifth consecutive review in
this laboratory performed by a session the registry does not name.** Findings need no actorhood.
Authority does.

**And it cannot answer the mandate's question.** *"Does LEGEND improve traceability, verifiability
and correctability?"* is answered by running `TRIAL-001`, not by planning it. This record, its
predecessor, both reviews, both trial designs, the execution protocol and the two findings registers
amount to **≈6 000 lines about an experiment that has not been performed on a paper nobody has yet
acquired.** That is not a criticism of the care taken — the crossover design is better for it, and
the reviews caught defects that would have voided the result. **But the next act that produces
scientific evidence is Φ1, and everything between here and there is the container.**
