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

---

## 10 · M3 — the routing table, and why it is a test rather than a document

**Implemented on 2026-09-18, same session, under §21e.** §2.5 named routing, not size, as the
residual defect: the tools answer almost every question a session asks, they are spread across
three directories, and `CLAUDE.md` deliberately does not legislate a list of them. A session that
does not know a tool exists greps — and the fragment is the failure this repository has named
twice.

### 10.1 The change

| File | Change |
|---|---|
| `framework/scripts/README.md` | **new** — *question → tool*, in twelve sections, covering every shipped tool including the three importable-only modules, opening with the one rule it exists to carry: never grep the two large registries |
| `scripts/test_tool_routing.py` | **new** — 7 cases; the completeness guard |
| `CLAUDE.md` | §1 routes to the table; §3 says the handful listed there are what a session runs most and the table routes the rest |
| `framework/manuals/operator_manual.md` | §2 core scientifico points at the table beside the per-record rule |

### 10.2 Why a guard and not just a document

A hand-kept table over this many tools is wrong by the third tool added. So the table is **not
the constraint** — the suite is:

- The **population is enumerated from the git index** (`git ls-files`), never from the disk.
  Two paid-for reasons, both cited in the suite: `artifact_index.py` rule 3 (a count whose
  denominator is *"whatever my pattern matched"* is not a measurement) and
  `test_repository_surface_determinism.py` (one clean checkout, three verdicts from a
  disk-walking guard). An untracked scratch script does not turn it red; a committed tool does.
- **No tool count is written anywhere** — not in the table, not in `CLAUDE.md`, not in the suite.
  The first draft carried one and it is precisely the constant `growth_anchors.py` calls *a quiet
  birthday*. The registry record counts that remain are dated, with the command that reprints
  them.
- A library with no `__main__` must be listed **as a library**, derived from the files — so a
  module that grows a CLI, or a command that loses one, fails the suite rather than drifting.

**The rule is one section, not one row, and the suite found that itself on its first run.**
`paper_packet.py` legitimately earns two rows in §1 — `packet` and `check` are two questions —
while one tool offered from §1 *and* §7 would leave a reader unable to tell which is current.
The first cut asserted one row and went red on a correct table; the assertion was wrong, not the
table. A vacuity case now pins that the parser really attributes a tool to the section it sits
under.

### 10.3 Measured

| Criterion | Result |
|---|---|
| every shipped tool routed | ✅ set-equality against the git index |
| mutation: delete a routed row | ✅ **red**, naming the orphaned tool |
| mutation: commit a new unrouted tool | ✅ **red** |
| auto-enrolled in the release inventory | ✅ `run_release_regressions.py` discovers rather than lists: 107 → **108** suites |
| no regression green-before, red-after | ✅ **the same 7 suites** fail as at `be8239d`, an identical set, all environmental |
| gate, LINT, receipts | ✅ release gate **PASS 0 blocks**; LINT **PASS**; receipts **OK, 156 chained, tail anchored**; `test_documented_commands.py`, `test_link_targets.py` green |

### 10.4 What M3 did not do

- **It did not measure its own effect.** The success criterion in §6 is *ad-hoc `grep` calls on
  the two large registries → 0 in the next wave's transcript*, and no wave has run. The table is
  a prescription until then, exactly as `registry_records.py` was on 2026-09-11 — and the lesson
  of that record is that the prescription and the behaviour were two different things.
- It routes tools, not skills or agents. `.claude/skills/` and `.claude/agents/` have their own
  surfaces and are out of this table's population.
- The twelve section headings are a judgement about which questions a session asks. Nothing
  tests that judgement; only completeness is executable.

---

## 11 · M4 — filters computed on demand, and the corpus measurement that reshaped them

**Implemented on 2026-09-18, same session, under §21e.** M4 is the milestone that answers the
roadmap's §2 example queries **without an index on disk** — the `build_evidence_index.py` pattern.
Nothing is written; every answer is parsed from the current file at call time.

### 11.1 The roadmap's own example queries did not fit the corpus

`--status INFERENZA` was measured before it was implemented, and two things are wrong with it:

- **The epistemic level is declared in `Type`, not in `Status`.** `Status` is the claim's
  lifecycle — `consolidated baseline` (18), `in observation` (17), `flagged for review` (2),
  `conflicting evidence` (1), `background only` (1).
- **`Type` is compound free prose.** Of 39 claim records, 21 distinct `Type` values; only a
  handful are a bare level. The rest read `DATO + INFERENZA prudente`, `DATO (le misure) +
  IPOTESI (entrambe le spiegazioni)`, `DATO (serie allelica su cellule di paziente) + INFERENZA
  (la regola)`.

So exact matching returns **2** records and calls them *"the inferential claims"*; substring
matching returns **14** and would call the same thing by the same name. **Neither is the answer**,
and choosing silently would be the `identity` / `mention` confusion one field along — the error
the 2026-09-09 sweep produced (A13) and that `registry_records.py` exists to refuse.

`--has-fulltext --not-deep-dived` fits even less: the paper registry declares no full-text field
at all. `unread_gold.py` and `reading_state.py` already answer that question and M4 does not
reimplement them; the routing table says so in the same section.

### 11.2 What was built instead

| | |
|---|---|
| `get --field NAME=VALUE` | repeatable and AND-ed; matches a **declared** field (never the prose) as a case-insensitive substring; composes with `--pmid`, `--id`, `--theme`, `--source` |
| **the report that travels with it** | how many records **declare** the field (the denominator), how many matched, and **every distinct value behind that count** |
| unknown field | a **named refusal with `difflib` near-misses** (`Stato` → `Status`), never an empty result |
| `fields` action | the whole vocabulary, per surface, derived from the files — because none is declared anywhere |
| `--id` exemption | a record asked for by name is never withheld by a filter: `--id X --field Y=z` returning nothing would be indistinguishable from *"X does not exist"* |

### 11.3 Measured

| Criterion | Result |
|---|---|
| agreement with an independent scan | ✅ expected sets derived by line-scanning the raw file, never from the selector's own output |
| `records[]` byte-identical on the 7-PMID set | ✅ **7 of 7** |
| latency on the ordinary path | ✅ **no measurable change** — interleaved A/B against a detached worktree at `ec7caa1`: pre-M4 344 / 334 ms, post-M4 335 / 338 ms per call |
| the new path | cross-registry field filter over all seven surfaces: **≈310 ms**, no file written |
| suite | 49 → **61** cases; LINT **PASS**, receipts **OK**, gate **PASS 0 blocks** |

**Four mutations, and two of them survived the first draft of the tests.** Swapping the matcher to
`==` and moving the denominator over every reachable surface both left the class green, because
every case used `Status` (whose values happen to be exact) and the one compound case asserted on
the *report* rather than on the *hits*. The report and the selection are two code paths and are
now pinned separately; the denominator case was vacuous until it used a field **two** surfaces
declare. Both weaknesses are recorded in the tests that now cover them.

### 11.4 Two corrections to this record's own method

- **§9.2's "+14 ms/call" was measured without interleaving.** The A/B run above shows the host's
  absolute numbers drifting between 255 and 344 ms for *unchanged* code, so a before/after taken
  minutes apart cannot resolve a 14 ms effect. What §9.2 established is that M1 is not expensive;
  the specific figure should not be quoted. M4's figure is interleaved and can be.
- **A stale `__pycache__` briefly produced a false failure.** The mutation `in` → `==` is
  byte-identical in length, so after restoring the source Python reused the mutated bytecode.
  Any future mutation run in this repository should clear `__pycache__` between passes — a
  mutation that changes no byte count is invisible to the timestamp-and-size check.

### 11.5 What M4 did not do

- **No dashboard, no aggregate.** `dashboard coverage` in the roadmap's §2 is `coverage_report.py`,
  which already exists with an honest denominator. Nothing was duplicated.
- **No natural-language query.** `legend query "which claims link glia and myelin and have
  contradictory evidence?"` is not a filter; it is the RAG of Phase 4, whose verdict stays DEFER.
- **It did not lower the latency budget question for Phase 2.** The measured cross-registry filter
  is ≈310 ms with zero persisted state. That is the number an SQLite index would have to beat by
  enough to justify a stale-index failure mode, and it does not yet.

---

## 12 · A correction, and the seven red suites this record kept naming without looking

### 12.1 The correction

**§9.2, §10.3 and §11.3 each say the seven failing release suites are "all environmental". That
is wrong, and it was asserted three times without being checked.** The claim came from reading
two of the seven (`numpy`, a gitignored artefact) and generalising to the rest. Diagnosed
properly on 2026-09-18, they are **three different things**:

| Suite | Actually |
|---|---|
| `scripts/test_cli_smoke.py` | `numpy` absent — optional dependency |
| `disease-models/wwox/analysis/scripts/test_structural_analysis.py` | `numpy` absent |
| `framework/scripts/test_figure_ppi_preflight.py` | `PyMuPDF`/`fitz` absent |
| `framework/scripts/test_regenerate_adjudications_fails_closed.py` | `fitz` absent — the suite already had `skipIf(fitz is None)`, on **one** of its four classes |
| `framework/scripts/test_paper_packet.py` | artefacts under gitignored `files/` absent (15 declared, 0 present) |
| `disease-models/wwox/analysis/scripts/test_dismech_independent_protocol.py` | **a shallow clone** — 54 commits, `is-shallow-repository: true`; the seal's `git_head_at_freeze` (`8ca27121…`) is not an object here, so 14 sealed inputs report `git blob unavailable` |
| `framework/scripts/test_batch_queue.py` | **NOT environmental.** *"80 studies counted as read against 59 PAPER records claiming full text. Only a BATCH_COMMIT closes this."* |

No verification conclusion changes — the §21e criterion being checked was *no suite green before
a change is red after it*, and the same seven were red at clean HEAD each time. But the
characterisation was wrong, it is in three commit messages, and the correction belongs where the
claim was made.

### 12.2 Why the first six are a defect and not a fact of life

`test_repository_surface_determinism.py` exists to enforce one rule: **same tracked tree, same
verdict, whatever else is on the disk.** These six broke it from the other side — the verdict was
following the *machine* (which optional packages happen to be installed, how deep the clone is),
not the tree. And a missing optional dependency and a broken argparse were reported identically,
as `exit 1`, so the battery could not tell them apart.

The repository already had the right idiom in three places — `skipIf(fitz is None, …)`,
`skipUnless(LIVE_CORPUS.is_dir(), …)`, and the wording *"real artefact absent: `files/` is
gitignored, so this case does not run in a fresh clone. It is skipped, never passed."* It was
applied unevenly. Extending it was reuse, not invention.

| Suite | Change |
|---|---|
| `test_regenerate_adjudications_fails_closed.py` | the existing guard extended to the three classes that lacked it |
| `test_figure_ppi_preflight.py`, `test_structural_analysis.py` | the import guarded — **including the subject's own import**, since each subject imports the dependency at module level and would raise before any `skipIf` could fire |
| `test_paper_packet.py` | the artefact-digest case skips when no declared artefact is present, naming three of them |
| `test_dismech_independent_protocol.py` | a **third** state beside "git present" and "git absent": *git, but not this history*, which is what a container or CI checkout ordinarily is. The message says the baseline is **not thereby verified** and gives the remedy (`git fetch --unshallow`) |
| `scripts/test_cli_smoke.py` | a `--help` dying on `ModuleNotFoundError` for a module **this repository does not ship** is skipped with the module named; anything else still fails. The shipped set is derived from `git ls-files`, never listed |
| `scripts/run_release_regressions.py` | repeated skip reasons folded with their multiplicity — one suite produced **27 identical lines**, which buries the one distinct reason below them. The header's total is unchanged. And **skips are now printed on the FAIL path too**: until now they appeared only when the battery passed, so a run with one failure said nothing about the suites that skipped every case they own — and *"skipped, never passed"* is a promise that depends entirely on being said out loud |
| 18 inventory suites | `unittest.main()` → `unittest.main(verbosity=2)`: unittest emits the skip **reason** only at that verbosity, so a skip from any of them reached the verdict as `reason unavailable` — the guarantee reduced to a number |
| `scripts/test_release_runner_verdict.py` | a guard: no suite in the release inventory may hide its skip reasons. Discovered from the inventory, so the next suite added fails it until it can say why it skipped |

**Mutation-checked where it matters most**, because the hazard of this whole change is a skip
that hides a real breakage:

| Mutation | Result |
|---|---|
| break a CLI's module body outright | ✅ **FAILED** — not skipped |
| make a CLI fail on a module the repository **does** ship | ✅ **FAILED** — the shipped/not-shipped distinction is the load-bearing one |
| *(first attempt at the above used `registry_records`, which is importable from that directory, so it produced no error at all — the mutation was re-done with a module that is shipped but off that path)* | |

### 12.2b · The guard found two defects in itself, and one of them was mine twice

Writing the "no suite hides its skip reasons" check produced three corrections in a row, all of
the same shape — **an instrument that reads text where it should read structure**:

1. **A substring scan for `unittest.main()` flagged the guard's own file**, whose docstring and
   failure message both quote the pattern they are about. Rewritten with `ast`.
2. **The same substring scan had already damaged `test_self_test_coverage.py`** — it rewrote four
   *fixture strings*, synthetic suites embedded as constants for the coverage analyser to read,
   while that file's real entry point had been verbose all along. Reverted; the file never needed
   changing. This is `artifact_index.py` rule 3 restated: the population must be enumerated by an
   instrument that cannot express the property being hunted.
3. **The first `ast` version then over-matched**, flagging five suites that call their own local
   `main()` — one of which does not import `unittest` at all and prints its own PASS/FAIL lines.
   A suite that emits no unittest skips has nothing to disclose. Narrowed to `unittest.main`, plus
   `main` only where `from unittest import main` is present, with a fixture case pinning each of
   bare / verbose / prose / a suite's own `main()`.

The "13 bare suites" figure this section first carried was therefore wrong in **both** directions
— it counted fixtures and missed real forms. The AST count is the one to trust, and every edited
file was re-audited afterwards to hold exactly one real `unittest.main` call.

### 12.3 What was deliberately left red

**`test_batch_queue.py` stays red.** *"80 studies counted as read against 59 PAPER records
claiming full text"* is a finding about the scientific state, and the test's own message names
the remedy: **only a `BATCH_COMMIT` closes this.** That is Scientist/Orchestrator work under the
gate, not harness work, and this session is Harness Engineering. Skipping it, relaxing it, or
adjusting its threshold would be precisely *"skip a test to get green"* — the thing the operating
rules forbid and the thing this whole change could most easily have become.

It is reported here so it is not lost: **the queue counts 21 more studies as read than the paper
registry declares full text for.** Either the queue over-counts or the registry under-declares,
and a reading decides which.

### 12.3b · The number the change actually surfaced

With the skips now printed on the FAIL path, the full battery reports **82 skipped cases** where
it previously printed none. Only about a dozen of those are the six suites repaired above; **the
rest were already skipping silently**, on every recent run, for reasons no reader of the verdict
could see:

```
- test_deepdive_manifest.py: PyMuPDF unavailable  [x13]
- test_deepdive_manifest.py: PMID 38499540 supplement absent from this checkout
- test_deepdive_manifest.py: Retraction Watch snapshot unusable: … (run: dependency_integrity.py fetch)
- test_manifest_flag_drift.py: history absent in this checkout: a second revision of …PMID38499540.json
- test_self_test_coverage.py: history absent from this checkout: 0e33f0f
- test_repository_surface_determinism.py: case-sensitive filesystem: `.GIT` cannot impersonate `.git`
- test_cli_smoke.py: 23 of 26 declared commands verified; 3 not run because …
```

The battery has been red for some time, so `format_success_verdict` — the only place skips were
printed — never ran. **That is the finding**: the repository's most load-bearing verification
surface was reporting a one-line verdict over a battery in which eighty-two cases did not
execute, and nothing said so. The six repaired suites are the smaller half of this section's
value; making the other seventy visible is the larger half.

Three distinct causes stand out and none is addressed here: **PyMuPDF absent** (13 cases in the
manifest validator alone), **the shallow clone** (`0e33f0f`, `8ca27121`, prior manifest
revisions — history the seal and the drift detector both need), and **a Retraction Watch snapshot
that was never fetched**. Each is a deployment decision, not a code change, and each now names
itself in the verdict.

### 12.4 What this did not establish

- **Nothing was verified that was not verified before.** Six suites moved from *red for a reason
  nobody read* to *skipped for a reason printed in the verdict*. That is a gain in legibility and
  determinism, not in coverage — and the count of what is actually exercised on this host is
  unchanged. Eighty-two cases still do not run here; the change makes that sentence sayable, and
  it does not make it false.
- **The optional dependencies were not installed.** Whether these suites pass with `numpy` and
  `PyMuPDF` present is untested here, and a deployment that has them will be the first to find out.
- **The shallow clone was not deepened.** The dismech seal remains unverified on this host.
