---
artifact: PLAN-RETRIEVAL-ARCHITECTURE-EVALUATION-001 — evaluation of the proposed four-phase
  retrieval architecture (canonical CLI · derived SQLite index · derived knowledge graph ·
  non-canonical vector RAG) against the measured state of this repository
record_id: PLAN-RETRIEVAL-ARCHITECTURE-EVALUATION-001
task_id: PLAN_RETRIEVAL_ARCHITECTURE_EVALUATION_v1
author: plan
authored_on: 2026-09-18
dispatcher: operator
mode: ANALYSIS_ONLY
STATUS: READ_ONLY_EVALUATION · ACTIVATION: NOT_REQUESTED · APPROVAL: NOT_GRANTED · AUTHORITY_CLAIMED: none
canonical_effect: NONE
measured_at_commit: 83ec6be
classification:
  - EVALUATION REPORT · NOT AN IMPLEMENTATION · NOT A GOVERNANCE DECISION · NO NEW VOCABULARY
  - Every figure below was re-measured on this checkout at 83ec6be, not quoted from an earlier record
---

# Retrieval architecture — what is already built, what the roadmap would add, and the one thing worth doing now

> **Reading note.** Three registers are kept separate throughout and never merged:
> **OSSERVATO** (re-measured on this checkout), **INFERENZA ARCHITETTURALE** (a reading of
> what those measurements imply), **PROPOSTA** (what this record recommends). Where a section
> mixes them the label is inline.

---

## 1 · Verdict

| Phase | Verdict | Why (≤5 lines) |
|---|---|---|
| **1 — canonical read-only CLI** | **ADOPT WITH CHANGES** | The *contract* already exists and is already prescribed: `registry_records.py` delivers whole records, identity≠mention, digests, `--hops`, named residue, fail-closed empties; `paper_packet.py` delivers the per-PMID technical packet. What is missing is not a CLI — it is **git provenance in the envelope**, **smoke-test enrolment**, and **discoverability across 70 non-test scripts**. Building a new `legend` entry point would re-wrap a solved problem and create the repository's first packaging surface. Adopt the gaps, reject the wrapper for now. |
| **2 — derived SQLite index** | **DEFER** | The token problem the index is meant to solve is **already measured as solved** (1,066,618 → 193,093 chars, −82 %, re-confirmed today) and the residual 163 KB is the working model + claim registry, which were **deliberately** left whole because selective retrieval cannot promise to find a claim a paper contradicts. An index would not reduce that residue; it would add the repository's first on-disk retrieval state and its first stale-index failure mode. Current cost: **0.242 s** per cross-registry query at 449+418 records. Defer behind a measured trigger, not a date. |
| **3 — derived knowledge graph** | **ADOPT WITH CHANGES — and the change is that the graph is not the work** | `pathograph.py` (71 KB) + `pathograph_export.jsonl` (842 KB, tracked) already assemble the object: claim nodes, declared wikilink edges, candidate edges from a closed connective lexicon, absence classified into three kinds. It emits **every edge `UNTYPED`**, on purpose, because no claim record annotates a relation type. The roadmap's §3 constraint (*"le relazioni devono avere tipo e provenienza espliciti"*) is therefore **already the measurement pathograph reports**. The missing piece is a `Relation` annotation in the claim-record convention — registry work under `BATCH_COMMIT`, not harness work. No new graph engine, no Neo4j, no CX2 export until edges are typed. |
| **4 — vector RAG** | **DEFER** (near-REJECT for the current horizon) | The capability exists as `legend-paperqa`, already fenced correctly (`queried_not_full_read`, discharges no reading debt, emits no receipt, human gate, external-spend authorization). Standing it up costs external spend — **RESERVED to the operator, §21d** — or a local model stack this repository does not carry. And its retrieval unit is a chunk, which is precisely the defect mode this repository has named twice in writing (*"a fragment is how a caveat dies"*). Discovery is currently served by `--theme`, `unread_gold.py` and `pubmed_corpus_harvest.py`. |
| **DisMech as a pattern source** | **ADOPT 2 of 5 patterns** | Evidence-snippet exactness: already stronger here (hash-chained receipts + fingerprinted artefacts) — **keep, do not import**. Ontology binding: the MAXO crosswalk and HPO neighbour ranking already exist — **extend**. YAML-as-source-of-truth: **REJECT**, it is a second source of truth by construction. Schema/reference validation: **partially present** (`legend_lint.py`, `deepdive_manifest.py`) — no import needed. CX2/NDEx export: **DEFER** until edges carry types; exporting UNTYPED edges to a public graph is exactly the "connection reads as causation" failure the roadmap forbids. |

---

## 2 · State measured on this checkout

All figures re-derived at `83ec6be` on 2026-09-18. Commands are given so each is re-runnable.

### 2.1 OSSERVATO — the canonical surfaces and their size

`python3 framework/scripts/registry_records.py index`

| Surface | Records | Bytes |
|---|---:|---:|
| `paper_registry_current.md` | 449 | 411,766 |
| `literature_tracking_log_current.md` | 418 | 491,623 |
| `claim_registry_current.md` | 43 | 115,589 |
| `working_model_current.md` | 13 | 47,640 |
| `full_text_queue_current.md` | 113 | — |
| `discovery_ledger_current.md` | 30 | 564,775 |
| `dismissal_ledger_current.md` | 4 | — |
| **four current files, total** | **923** | **1,066,618** |

Largest tracked objects overall: `corpus_seed_pubmed_20260806.jsonl` (3.92 MB, a census and
explicitly **not evidence**), `pathograph_export.jsonl` (842 KB, derived and tracked),
`fulltext_read_receipts.jsonl` (773 KB, append-only hash-chained ledger).

### 2.2 OSSERVATO — `registry_records.py`, against the roadmap's own Phase-1 checklist

23,470 bytes, two subcommands (`get`, `index`), standard library only, no state written.

| Roadmap requirement for the CLI | Status at 83ec6be |
|---|---|
| use `registry_records.py` as base, do not reimplement | — (it *is* the base) |
| whole records, never fragments or substitute summaries | ✅ exact byte slice, heading→next heading |
| distinguish `identity` from `mention` | ✅ `IDENTITY_FIELDS`; `Source:` deliberately excluded (incident A13) |
| surface ambiguity, records not returned, unresolved links, residue | ✅ all four, each in its own named block |
| report path, record id, line, record digest, source digests | ✅ |
| **report git commit / repository state** | ❌ **absent — the one contract gap** |
| human output and `--json` | ✅ same bytes both ways |
| read-only toward canonical registries | ✅ |
| fail explicitly on no data / unverifiable provenance | ✅ exit 1 + *"this is not evidence that the laboratory does not know this paper"* |
| usable by Claude Code, Codex, scripts, CI, future MCP | ✅ plain argv + JSON on stdout |
| reduce systematic full-registry loading in MINIMAL/STANDARD/FULL | ✅ **already prescribed**: `operator_manual.md` §1.1 (l.68), §1.2 (l.92), §1.3 (l.133–134), §7 (l.261); `scientist_standing_brief.md` l.207 (M4b); `legend-start` step 5; agents `legend-deepdive`, `study-intake-triage` |

Measured today: `get --pmid 33914858 --hops 1 --json` → **0.242 s**, **59,535 chars**.

### 2.3 OSSERVATO — everything else the roadmap proposes to build, that already exists

| Roadmap element | Existing implementation | Notes |
|---|---|---|
| `legend paper <pmid>` | `paper_packet.py packet --pmid` (+ `check`) | Carries identity, bytes, coverage state, acquisition history, applicable checks. **Deliberately carries no prior claim, dossier, locator or conclusion** — `scientist_reading_modes.md` §3.1/§3.3; `test_paper_packet.py` asserts the absence. |
| `legend claim` / `legend provenance` | `registry_records.py get --id "CLAIM 030"`, `trace_claim_foundation.py` | The latter traces a claim to the **species and reading depth** of what it rests on — the 2026-08-06 rat/mouse inversion is its origin. |
| `legend queue` | `batch_queue.py` (42 KB, `--json`, `--check`) | Already a generated surface with an inputs-dirty guard. |
| `legend status` | `reading_state.py`, `coverage_report.py`, `session_self_eval.py`, `legend_lint.py` | `reading_state.py` **sums** receipts rather than choosing the last one — a merge-safety property a naive status view would lose. |
| `legend find --has-fulltext --not-deep-dived` | `unread_gold.py` | Born from FM-011: high-relevance corpus placeholders never read. |
| structured cross-cutting index | `build_evidence_index.py` | **A derived queryable index that is deliberately never written to disk**, with tier breakdown and an honest denominator (15 of 49 papers have a manifest). This is the working precedent for Phase 2 without SQLite. |
| knowledge graph | `pathograph.py` + `pathograph_export.jsonl`; `generate_semantic_graph.py` | See §1 and §4.3. |
| RAG | `.claude/skills/legend-paperqa/` | Skill + setup reference; no index, no dependency, no spend authorized. |
| **stale-derived-artifact guard** | `derived_inputs.py` | `input_state()` / `refuse_if_dirty()`: a generator about to write a derived surface refuses when its inputs are modified or untracked, unless the caller states why (`--inputs-dirty-because`). Names `UNBOUND` outside git. **This is the Phase-2 stale-index gate, already written, already reused.** |
| committed-derived lifecycle | `test_generated_surfaces_are_regenerated.py` | Discovers self-declared generated Markdown and requires `prompt_batch_commit.md` phase 4.7 to name it. Found its own first case (`batch_queue.md`). |
| anti-drift constant policy | `growth_anchors.py` | *"Updating a constraint must cost at least as much as complying with it."* |

### 2.4 OSSERVATO — maintenance surface, packaging, name collisions

- **164** Python files under `framework/scripts/`, `scripts/`, `governance/scripts/`; **94** of them are test files. Net **70 executable tools**.
- **No `pyproject.toml`, no `setup.py`, no `setup.cfg`.** `requirements-analysis.txt` pins exactly two optional packages (`numpy`, `PyMuPDF`). An installable `legend` entry point would be **the first packaging surface this repository has ever had**.
- `which legend` → **not found** on this host. But `.claude/skills/legend/` is the autopilot skill invoked as `/legend`; a shell `legend` and a `/legend` skill would be two different things wearing one name.
- `scripts/test_cli_smoke.py` declares **24** `PUBLIC_CLIS`. **`registry_records.py` and `paper_packet.py` are not among them** — the two commands the operator manual now routes every scientific session through have no `--help` smoke coverage.
- `scripts/test_repository_surface_determinism.py` fixes the test population to the **git index**, not the disk: a gitignored file can no longer turn the release battery red. An ignored `.db` artifact is therefore already safe by construction — **if** it is gitignored.

### 2.5 INFERENZA ARCHITETTURALE

1. **Phase 1 is not a greenfield; it is a 90 %-complete contract with one hole.** The hole is git
   provenance. Every other guarantee the roadmap lists for the CLI is implemented and tested.
2. **The repository has already paid for Phase 1 twice — once in code and once in an adversarial
   verification that refuted four of five guarantees on first pass** (`2026-09-11_registry_context_reduction.md`
   §5: em-dash headings, `Source` mistaken for identity, order-sensitive ambiguity keys,
   `CORPUS P###`/`LIT-EX-###` withheld as prose). A new wrapper over this surface inherits none of
   that scrutiny automatically and would need its own.
3. **The problem is no longer size; it is routing.** 70 tools, one router (`CLAUDE.md`) that
   explicitly "does not legislate", and a skill layer that names some tools and not others. An
   agent that does not know `unread_gold.py` exists will grep. That is a **documentation and
   discovery** problem, and an index or a graph does not fix it.
4. **This repository's characteristic failure is the fragment, not the byte count.** Both
   `registry_records.py`'s docstring and the 2026-09-11 record state it in the same words. Every
   layer the roadmap proposes below Phase 1 (SQLite rows, graph edges, vector chunks) is a
   fragment-producing layer. Each therefore needs a return path to the whole record, and the
   return path is `registry_records.py` — which is an argument for hardening it first and an
   argument against building consumers before it carries a commit SHA.
5. **The graph's missing element is scientific, not technical.** `pathograph.py` refuses to derive
   `DIRECT` from "both endpoints are `DATO`" because two demonstrated facts are not a demonstrated
   relation. No amount of graph tooling changes that. Typing edges is Scientist work against
   evidence, gated by `BATCH_COMMIT`.

---

## 3 · Against the two stated objectives

### A · Scientific flexibility

| Property | Phase 1 | Phase 2 (SQLite) | Phase 3 (graph) | Phase 4 (RAG) |
|---|---|---|---|---|
| Claims stay strengthenable / weakenable / reopenable | **Neutral–positive.** Parses at call time; nothing cached, so a registry edit is visible on the next call. | **Risk.** An index built at T is a snapshot; a query at T+1 answers about T unless the staleness gate is perfect. | **Risk if typed edges are stored outside the registry.** Neutral if the type lives in the claim record and the graph only reads it. | **Risk.** An embedding built from a pre-revision record survives the revision. |
| No fossilisation of the model | Positive — the selection is per-query and its limits are printed. | Neutral, if regenerable and gitignored. | **Negative if the graph acquires hand-maintained edges.** The roadmap already forbids this; the forbidding must be executable. | Negative at the margin: similarity rankings bias what gets re-read. |
| Git history and reasons for change preserved | **Currently incomplete** — the envelope has record and file digests but no commit SHA. | Adds a second artifact whose history is not the registries' history. | `pathograph_export.jsonl` is already tracked, so its history *is* in git. | Index history is not preserved by anything. |

The sharpest flexibility risk in the whole roadmap is **Phase 2's staleness**, and the roadmap
already names the right answer (fail closed or regenerate explicitly). `derived_inputs.py`
implements that answer today, for writes. Extending it to *reads* is the non-trivial part.

### B · Operational lightness

**OSSERVATO — what is already banked** (`2026-09-11_registry_context_reduction.md` §4, spot-checked
today at 1,066,618 total and 0.242 s/query):

| | Characters |
|---|---:|
| OLD — four current files, every MINIMAL session | 1,066,618 |
| NEW — per paper, one hop, records whole (7 papers, median 33,471) | 29,864 |
| still loaded whole (working model + claim registry, deliberately) | 163,229 |
| **MINIMAL session carries** | **1,066,618 → 193,093 (−82 %)** |

**What is NOT established, in that record's own words**: token consumption (only characters were
measured); and whether a real scientific reading through the selective path loses coverage,
caveats or contradictions — *"only the transport is verified"*.

#### PROPOSTA — the measurement plan, and what it must NOT re-measure

Do **not** re-run the character measurement. It is done, it was independently verified, and
repeating it produces a number that already exists. The four numbers this system actually owes are
already specified in `2026-09-11_control_efficacy_baseline.md` §2 and are unpaid because no
Scientist wave has yet used the controls.

| Metric | Baseline (today) | Instrument | Post-intervention criterion |
|---|---|---|---|
| Characters carried per task | 193,093 (MINIMAL) | already measured; do not repeat | unchanged or lower — **a regression here fails the intervention** |
| Tool calls per single-paper task | **unmeasured** — transcripts show 16 Bash calls naming the paper registry and 8 naming the literature log across 4 sessions, pre-intervention | count `Bash`/`Read` calls naming a registry path in the next wave's transcript | ad-hoc `grep` calls on the two large registries → **0** |
| Retrieval latency | 0.242 s (`get --pmid … --hops 1 --json`) | `time` over the same 7 PMIDs | < 0.5 s; any added guard costing > 50 ms is reported |
| Records returned | 7-PMID set, median 33,471 chars | `--json` `records[]` length | **byte-identical** to the pre-change output — a provenance change must not change a record |
| Provenance present | record digest ✅, source digests ✅, **commit SHA ❌** | inspect `--json` | 100 % of outputs carry commit SHA + working-tree state |
| Caveats lost / not lost | **unmeasured on a real reading** | the four numbers of `control_efficacy_baseline.md` §2, reported by the next wave | errors intercepted / false alarms / added time / coverage, each with its denominator |

🔴 Characters are not provider-billed tokens. The telemetry separating input, output and cached
tokens is not exposed on this host, and no figure here should be read as a bill.

---

## 4 · Minimum target architecture

### 4.1 PROPOSTA — the boundary, in one picture, with today's occupants

```
CANONICAL (BATCH_COMMIT, LINT, receipts)
  disease-models/<disease>/registries/*.md      ← the four current files
  disease-models/<disease>/research/*.md
  disease-models/<disease>/registries/fulltext_read_receipts.jsonl   (append-only, hash-chained)

ACCESS CONTRACT (read-only, no state, stdlib)
  framework/scripts/registry_records.py   ← whole records, identity≠mention, digests, hops
  framework/scripts/paper_packet.py       ← per-PMID technical packet, conclusion-firewalled

DERIVED, COMPUTED ON DEMAND, NEVER WRITTEN   ← the existing pattern, and the preferred one
  framework/scripts/build_evidence_index.py
  framework/scripts/coverage_report.py · reading_state.py · unread_gold.py · trace_claim_foundation.py

DERIVED, WRITTEN, TRACKED, REGENERATED IN BATCH_COMMIT PHASE 4.7
  batch_queue.md · coverage_report.md · pathograph inventory + export
  guarded by derived_inputs.py; enumerated by test_generated_surfaces_are_regenerated.py

DERIVED, WRITTEN, GITIGNORED, REBUILDABLE   ← where SQLite/embeddings WOULD live, if ever
  files/ · _qa/ · tmp/                       (already ignored; no new policy needed)
```

**PROPOSTA — the rule that keeps this simple.** A derived artifact is written to disk only when it
cannot be recomputed inside a session's latency budget. At 923 records and 0.242 s, nothing in the
roadmap meets that bar. `build_evidence_index.py` states the principle already: *"a derived file
committed beside its sources becomes a second truth the moment the sources move."*

### 4.2 PROPOSTA — the minimal JSON envelope addition (Phase 1's only real gap)

Additive, top-level, alongside the existing keys. No key is removed, no record byte changes:

```json
{
  "query": "...",
  "records": [ { "source": "...", "path": "...", "record_id": "...", "kind": "record",
                 "line": 1234, "match": "identity",
                 "record_digest": "sha256:...", "text": "<the whole record>" } ],
  "source_digests": { "paper_registry_current": "..." },
  "repository": {
    "verdict": "BOUND",
    "commit": "83ec6be…",
    "inputs": ["disease-models/wwox/registries/paper_registry_current.md"],
    "dirty_inputs": [{"status": "M", "path": "…"}]
  },
  "ambiguous": [], "unresolved_links": [], "matched_but_not_returned": [],
  "residue_not_returned": 0,
  "empty_result_is_not_a_scientific_statement": false
}
```

`repository` is computed by calling `derived_inputs.input_state()` on the source paths already
opened — **no new logic, no new concept, no new dependency**.

> **Amended on implementation (2026-09-18).** The block carries `derived_inputs`' own
> three-state `verdict` — `BOUND` / `DIRTY` / `UNBOUND` — rather than the `bound` and
> `inputs_clean` booleans this section first proposed. The booleans were two derivable
> restatements of one state, which is the shape `test_record_conventions.py` exists to prevent
> (*five modules, five private copies of one definition, and the shortest was wrong*). `UNBOUND`
> is the named non-git state that keeps the temp-directory test fixtures working; it is a state,
> never a pass. `refuse_if_dirty` is deliberately **not** called: this is a read-only command, so
> a dirty tree is reported and the answer is still given — refusing would make the selective path
> fail during a `BATCH_COMMIT`, which is when a reader most needs to look at the registries.

### 4.3 PROPOSTA — Phase 3, restated as what it actually is

The graph does not need building. It needs its edges to acquire types, and that is registry work:

1. **Scientific proposal (not harness, not this session):** a `Relation:` annotation on the
   claim-record convention, from a closed vocabulary — `SUPPORTS`, `CONTRADICTS`, `INFERRED_FROM`,
   `HYPOTHESIZES`, `RELATED_TO`, `MENTIONS` — each instance carrying its epistemic level
   (`DATO` / `INFERENZA` / `IPOTESI` / `ESPANSIONE`) and its source. Goes through `BATCH_COMMIT`.
2. **LINT rule** rejecting a relation type outside the vocabulary or without a declared source.
3. **`pathograph.py` reads the annotation** — its step 5 is already written to do exactly this and
   is waiting for input. Zero new tooling.
4. **CX2/NDEx export only after (1)–(3)**, and only for typed edges. `DISMECH_INTEGRATION.md`
   already states the eligibility rule: only `consolidated baseline` and `in observation` claims
   propagate; `background only` and `archived` never do; the dismissal ledger has **no target, on
   purpose**.

### 4.4 PROPOSTA — the `legend` name

**Do not take it yet.** Three reasons, in order of weight: (a) `/legend` is already the autopilot
skill, and one word naming two dispatchers is a support cost paid forever; (b) an installable entry
point would be this repository's first packaging surface, and packaging is a distribution decision
adjacent to publication — RESERVED, §21d; (c) nothing today is blocked by the absence of a short
name. If a dispatcher is ever wanted, `python3 framework/scripts/legend_cli.py <subcommand>` reuses
the repository's existing invocation shape, needs no install, and cannot collide.

### 4.5 PROPOSTA — not duplicating `registry_records.py`

Any future consumer (a filter, an index builder, a graph loader) **imports** `parse_records`,
`select`, `is_record`, `identity_key` and `file_digest` rather than re-parsing Markdown.
`build_evidence_index.py` already establishes the `sys.path.insert` + import idiom used across
`framework/scripts/`. `test_record_conventions.py` exists precisely because five modules once held
five private copies of one definition **and the shortest was wrong** — 168 records went uncounted.
That test is the guardrail for this rule and it already runs.

---

## 5 · Risks and guardrails

| # | Risk | Guardrail (technical) | Test | Explicit failure mode |
|---|---|---|---|---|
| R1 | **Second source of truth** — a derived store answers a question the registries should answer | Derived artifacts are gitignored or regenerated in phase 4.7; no derived artifact is ever an input to a claim | `test_generated_surfaces_are_regenerated.py` (extend to any new written surface) | A commit candidate cites an index row instead of a record → LINT must not be the thing that catches it; review does |
| R2 | **Stale index** presented as current | `derived_inputs.input_state()` on every read, not only every write; fail closed | new: a query against an index whose recorded commit ≠ `HEAD` must exit non-zero | Silent stale answer. **This is the single highest-severity risk in the roadmap** — it is the only one that produces a *confidently wrong* scientific input |
| R3 | **Caveat lost to chunking** | Record is the minimum retrieval unit; a chunk may be a locator, never a payload | assert `records[i].text` is byte-identical to the file slice | A caveat alive in prose and dead in a row — named twice already in this repository (sweep S3; `gold_is_in_the_details.md`) |
| R4 | **Graph edge or vector score read as causation** | `pathograph.py` emits `UNTYPED` with the reason attached and refuses to infer; no export of untyped edges | `test_pathograph.py` | A public knowledge graph inherits an assertion LEGEND never made |
| R5 | **Regression of the complete-read protocol** — retrieval starts substituting for reading | `queried_not_full_read` is already a named, weaker state; receipts unaffected; RAG discharges no reading debt | `test_fulltext_trace_contract.py`, `test_abstract_corpus_is_not_evidence.py`, `test_locator_obligation_reaches_every_route.py` | A paper counted as read because it was retrieved |
| R6 | **Maintenance debt** — 70 tools become 74 | Reuse before addition; every new tool enrolled in `test_cli_smoke.py` at birth | `test_cli_smoke.py`, `test_documented_commands.py` | A tool documented in prose whose executable has moved — the exact failure `test_documented_commands.py` exists for |
| R7 | **Agent misuse** — an agent queries the index and skips the record | The return path is mandatory and printed in every answer's *limits of this selection* line | `test_agent_pipeline_contract.py`, agent contracts in `.claude/agents/` | An inference built on a row |
| R8 | **Privacy / release-gate conflict** | New artifacts land under already-ignored roots (`files/`, `_qa/`, `tmp/`); the release battery's population is the git index, not the disk | `scripts/public_release_gate.py`, `test_repository_surface_determinism.py`, `independent_privacy_scan.py` | A derived artifact carrying corpus text into a published tree |
| R9 | **External spend** (Phase 4 embeddings/LLM) | RESERVED to the operator, §21d | — | An agent authorizing spend. Not a technical failure — a governance one |
| R10 | **A provenance change silently changes a record** | The intervention in §7 must be byte-neutral on `records[]` | new: byte-equality over the 7-PMID measurement set, before vs after | A "harmless" envelope change that re-normalises text |

---

## 6 · Incremental, reversible plan

Each milestone is isolated, testable, measurable, reversible by a single `git revert`, and touches
no canonical file.

| M | Scope | Test | Measure | Reversal |
|---|---|---|---|---|
| **M1** | **Git provenance in the envelope** — `repository{commit, inputs_clean, dirty_inputs, bound}` on `registry_records.py --json` and `paper_packet.py --json`, via `derived_inputs.input_state()` | `test_registry_records.py` +2, `test_paper_packet.py` +1, byte-equality of `records[]` | 100 % of outputs carry a commit; latency delta < 50 ms | revert one commit |
| **M2** | **Smoke-test enrolment** — `registry_records.py`, `paper_packet.py` into `PUBLIC_CLIS` | `test_cli_smoke.py` | 26 of 26 CLIs expose `--help` at exit 0 | revert |
| **M3** | **Routing table** — one section in `framework/protocols/index.md` (or a `framework/scripts/README.md`) mapping *question → tool*, covering the 70 executables | `test_documented_commands.py` | ad-hoc `grep` calls on the two large registries → 0 in the next wave's transcript | revert |
| **M4** | **Filters computed on demand** in `registry_records.py` (`--status`, `--has-fulltext`, `--not-deep-dived`), **no file on disk** — the `build_evidence_index.py` pattern | new cases + existing suite | answers the roadmap's §2 example queries at < 1 s with zero persisted state | revert |
| **M5** | *Only if M4 exceeds a latency budget measured in a real session* — SQLite under `files/`, gitignored, with a read-side staleness gate that fails closed | new suite; must include a deliberately-stale-index case | the trigger itself is the measure | delete the file |
| **M6** | **Claim-relation annotation** — scientific proposal to Orchestrator/Scientist, `BATCH_COMMIT` + LINT rule; `pathograph.py` unchanged | `legend_lint.py`, `test_pathograph.py` | typed edges > 0, each with a declared source | a `BATCH_COMMIT` reversal, under the ordinary scientific discipline |
| **M7** | CX2/NDEx export — **after M6 only** | — | — | derived output, delete it |
| **M8** | RAG — operator spend authorization first; or a local stack | — | — | delete the index |
| **M9** | MCP wrapper over the CLI — **after M1**, so every MCP answer carries a commit | — | — | revert |

M1–M3 are hours of work in total and are **T0 changes under §21e** (harness: `framework/`,
`scripts/`, no active gate, Mirror reviews ex post). M6 is not — it is scientific, and it is gated.

---

## 7 · The first intervention

> **Add git provenance to the two commands the operator manual already routes every scientific
> session through, and enrol them in the smoke test.** (M1 + M2.)

**Why this one and not a bigger one.** The roadmap's own inviolable rule is that every result used
for scientific reasoning *"deve tornare al record canonico completo, con provenance verificabile"*.
That is the one Phase-1 guarantee currently **not** met: the envelope carries a record digest and
source-file digests, but a reader who holds a quoted record cannot tell **which commit** it came
from, or whether the working tree was dirty when it was read. Every later layer in the roadmap —
index, graph, RAG, MCP — depends on that return path being verifiable. Hardening it costs about
fifteen lines and reuses a module (`derived_inputs.py`) that is already written, already imported
by other generators, and already defines the `UNBOUND` non-git state the test fixtures need.

**Exact scope**

- `framework/scripts/registry_records.py` — import `derived_inputs`; add a `repository` block to
  the `--json` output and one line to `render()`. No change to selection, parsing or record bytes.
- `framework/scripts/paper_packet.py` — the same block in its `--json` output.
- `framework/scripts/test_registry_records.py` — a case asserting the block is present and
  populated; a case asserting `bound: false` outside a git repository; a case asserting
  `records[]` is byte-identical to the pre-change output.
- `framework/scripts/test_paper_packet.py` — one equivalent case.
- `scripts/test_cli_smoke.py` — two entries added to `PUBLIC_CLIS`.
- `framework/manuals/operator_manual.md` — **only** if the rendered (non-JSON) line changes what
  §7 tells a reader to paste. Prefer a change that does not.

**Files that must NOT change**

- The four scientific current files, and every file under `disease-models/*/registries/` and
  `disease-models/*/research/`.
- `fulltext_read_receipts.jsonl` and any hash-chained ledger.
- `framework/instruction/LEGEND_CORE.md`, `epistemic_discipline.md`, any protocol under
  `framework/protocols/`, any file under `governance/`.
- `.gitignore`, `CLAUDE.md`, `ARCHITECTURE.md`.
- `registry_records.py`'s parsing constants — `RECORD_HEAD`, `RECORD_ID`, `IDENTITY_FIELDS`,
  `identity_key`. Each encodes a refuted-then-repaired guarantee from the 2026-09-11 independent
  verification; none is in scope here.

**Tests required**

```
python3 framework/scripts/test_registry_records.py
python3 framework/scripts/test_paper_packet.py
python3 scripts/test_cli_smoke.py
python3 scripts/test_documented_commands.py
python3 framework/scripts/legend_lint.py .                 # must show zero delta
python3 framework/scripts/fulltext_receipts.py verify       # must show zero delta
python3 scripts/run_release_regressions.py                  # nothing green-before may be red-after
```

**Quantitative success criterion**

1. **100 %** of `--json` invocations of both commands carry `repository.commit` and
   `repository.inputs_clean`.
2. **Byte-identical `records[]`** against the pre-change output over the 7-PMID measurement set of
   `2026-09-11_registry_context_reduction.md` §4 (33914858, 29724996, 18460020, 20146584, 25411445,
   21115974, 15070730). A single differing byte fails the intervention.
3. Added latency **< 50 ms** against the measured 0.242 s baseline.
4. `test_cli_smoke.py` reports **26 of 26** CLIs at exit 0.
5. No release regression green before the change is red after it.

**Stop / rollback criterion**

Any of: a record byte differs; latency exceeds 0.3 s; `derived_inputs` raises on a non-git fixture
directory; any release-suite regression. Rollback is `git revert <sha>` — one commit, no canonical
file touched, nothing scientific to restore. The precedent is already recorded: *"it is four
documentation edits and one new script. Revert the commit; the registries were never modified."*

---

## 8 · What this evaluation does not establish

- **It measured transport, not reading.** Whether selective retrieval costs coverage, caveats or
  contradictions in a real scientific reading is still unmeasured; the four numbers owed are in
  `2026-09-11_control_efficacy_baseline.md` §2 and are unpaid because no Scientist wave has used
  the controls yet.
- **No token figure appears here.** Characters were measured; provider-billed tokens were not, and
  the telemetry that would separate them is not exposed on this host.
- **DisMech's side is taken on the collaboration's authority.** `/curate`, the YAML schema and the
  PR flow have not been exercised from this repository — `DISMECH_INTEGRATION.md` states this
  itself, and nothing in this record changes it.
- **The staleness gate for a hypothetical read-side index was designed, not prototyped.**
  `derived_inputs.py` implements refusal on **write**; extending it to reads is the non-trivial
  part of M5 and no estimate is offered for it.
- **No judgement is offered on whether the residual 163 KB (working model + claim registry) should
  become selective.** It was evaluated and deliberately left alone on 2026-09-11, for a stated
  reason — a claim a paper contradicts may not be linked to that paper — and re-opening it needs a
  measurement this record did not make.

---

## 9 · What was implemented, and what it measured

**Implemented on 2026-09-18, same session, under §21e (harness, T0, no gate).** M1 and M2 of §6
only. Nothing from Phases 2–4 was built, and no canonical file was touched.

### 9.1 The change

| File | Change |
|---|---|
| `framework/scripts/registry_records.py` | `repository_state()` — a thin call to `derived_inputs.input_state()` over **the files the call actually opened** (which `--hops` may widen past `--source`); a `repository` block in `--json`; `repository_line()` rendered on every exit including the empty-result refusal; the derived `index` carries it too |
| `framework/scripts/paper_packet.py` | the same block over the packet's own inputs — manifest, receipt ledger, retrieval manifest, corpus seed |
| `framework/scripts/test_registry_records.py` | +9 cases (`TheAnswerNamesTheTreeItWasReadFrom`) |
| `framework/scripts/test_paper_packet.py` | +4 cases (`ThePacketNamesTheTreeItDescribes`) |
| `scripts/test_cli_smoke.py` | both commands enrolled; 24 → **26** declared public CLIs |

Two design points decided at implementation, both recorded in the code:

- **`refuse_if_dirty` is deliberately not called.** These commands are read-only, so a dirty tree
  is reported and the answer is still given. Refusing would make the selective path fail during a
  `BATCH_COMMIT` — precisely when a reader most needs to look at the registries.
- **The block carries `derived_inputs`' own three-state `verdict`**, not booleans derived from it.
  See the amendment in §4.2.

### 9.2 Measured against §7's criteria

| Criterion | Result |
|---|---|
| `repository.commit` + `verdict` on 100 % of `--json` outputs | ✅ both commands, plus the rendered form, the `index` action and the empty-result refusal |
| **`records[]` byte-identical** over the 7-PMID set | ✅ **7 of 7 IDENTICAL** (sha256 over the serialised array, before vs after) |
| added latency < 50 ms | ✅ **+14 ms/call** (241.4 → 255 ms median over 3 runs of 7 calls); `input_state` itself costs 7.2 ms |
| `test_cli_smoke.py` 26 of 26 at exit 0 | ⚠️ **24 of 26** — the two enrolled commands pass; 3 entries fail on `ModuleNotFoundError: numpy`, **identically at clean HEAD** (failure lists diffed, byte-equal) |
| no regression green-before, red-after | ✅ **verified against a detached worktree at clean HEAD**: the same 7 suites fail there and here, an identical set. All 7 are environmental — `numpy` absent, and `files/` gitignored so its artefacts are absent in this container |

Also green with the change in the tree: `legend_lint.py` **PASS**; `fulltext_receipts.py verify`
**OK, 156 chained receipts, tail anchored**; `test_documented_commands.py`, `test_link_targets.py`;
`public_release_gate.py` **PASS, 0 blocks**.

**Mutation-checked, not merely asserted.** Forcing `repository_state` to report `BOUND` with an
empty dirty list turned **2 of the 9 new cases red**. A provenance field that always says "clean"
is the one failure mode that would make this change worse than not making it.

### 9.3 What this did not do

- It did not reduce context further. The −82 % was already banked; M1 buys **verifiability**, not
  size, and the latency it costs is a real if small price paid for it.
- It did not measure tokens, and it did not run a scientific reading through the path. The four
  numbers of `2026-09-11_control_efficacy_baseline.md` §2 remain unpaid.
- **M3 (the routing table over the 70 executables) was not implemented.** It is the next step in
  §6 and the one that addresses the *routing* problem §2.5 names as the real residual defect.
- One pre-existing failure in `test_paper_packet.py` (`test_artefact_digests_are_verified_not_quoted`)
  is left as found: it fails at clean HEAD for the same reason, and repairing an environmental
  fixture gap was not in this intervention's scope.
