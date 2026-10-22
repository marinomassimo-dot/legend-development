# Harness mandate — Drug Repurposing as a first-class LEGEND module

Audience: Harness Engineering, `ACTOR_ID plan`. Issued by the operator through the Orchestrator on
2026-10-22. Read this file whole before the first act. Where it names a design choice, the choice is
yours to confirm or overturn by measurement; record the decision in your task record.

Not medical advice. Nothing produced here is a dose, an administration or a suitability statement
for any person.

## 0 · Bootstrap, in this order

1. `framework/state/state_manifest_current.md`: confirm `current_state: READY`.
2. `CLAUDE.md`, then by name `LEGEND_CORE.md` §21c, §21d, §21e. They decide when you may not stop and
   what you decide alone. A question with a safe default is a stop that must not be taken.
3. `framework/master/harness_development_principles.md`: lean, no gates for harness work, remove or
   merge before adding, discovery before rigor.
4. Your role contract in `roles/`; `python3 framework/scripts/harness_session_start.py` as the
   session-start skill directs.
5. `framework/scripts/README.md`, the routing table. Never grep the two large registries; use
   `registry_records.py` and the routed tools.
6. `ARCHITECTURE.md`: generic engine in `framework/`, WWOX bindings in `disease-models/wwox/`, nothing
   under `.claude/`.

Task record: `ledger/tasks/plan/PLAN-DRUGREPURPOSING-MODULE-20261022.json` with an `AUTHORISED_QUEUE`
of the five deliverables below, so `python3 framework/scripts/mandate_continuity.py status --task
PLAN-DRUGREPURPOSING-MODULE-20261022` can answer whether a turn may end. Keep `DEFAULTS_TAKEN`,
`DECISIONS_TAKEN`, `STOP_LOG` current and run that status before ending any turn.

Working rules: task branch in your own worktree under `.claude/worktrees/`; never a branch in the
root checkout; land with `framework/scripts/task_close.py`; commit with
`scripts/legend_commit.sh "<message>" <file> [<file>...]` (files, not directories); push only with
`python3 framework/scripts/safe_push.py development main` on a gate PASS of the exact SHA, after every
landed stage, because GitHub is the operator's real backup. Use the commit trailer in force for the
session.

## 1 · Source documents and how to use them

All three are in `disease-models/wwox/research/drug_repurposing/`. Do not edit the first two: they are
the operator's deliverables, quoted verbatim under an English provenance header. Your notes go in new
files in the same folder.

| File | What it is | What it decides |
|---|---|---|
| `roadmap_v4_r14_20261020.md` | The operator's roadmap (uploaded as `LEGEND_Drug_Repurposing_Roadmap_v1.md`; content v4, revision 14): phases P0 to P8, priorities, proposed integrations, verifications to run | ORDER and PRIORITY. A plan, not a state: `ADOTTATO NEL_PIANO` is a planning decision, never an installation or a scientific claim; its SHAs and baselines are stale |
| `scout_log_r20_20261020.md` | The operator's scout register (uploaded as `LEGEND_Drug_Repurposing_Scout_Test_2026-10-08.md`; revision 20, checkpoints 2026-10-08 to 2026-10-20): evaluated tools, sources, limits, history of decisions | WHICH TOOL and WHY. Documentary scouting: READMEs, diffs, abstracts, editorial scores; nothing in it was installed or run here. Use it to choose and to avoid re-evaluating, never as proof that a tool works |
| `reconciliation_20261020.md` and `README.md` | The first reconciliation of the plan against code, installs and data, with commands and outputs; the stage table | The baseline for a DELTA. Stale in places (§ 3). Re-measure what changed since 2026-10-20; do not redo what still holds |

The operator's standing instruction for these documents, verbatim:

> Leggi entrambi i documenti e le istruzioni correnti di legend-development. Riconcilia il piano con
> codice, installazioni e dati realmente presenti, quindi implementa gli incrementi fattibili secondo
> le priorità della roadmap. Preserva limiti scientifici e provenienza; distingui adozione nel piano
> da implementazione verificata. Registra prove, risultati e blocchi e prosegui sui percorsi
> disponibili.

Rules of use:

- Roadmap and scout log disagree: say so, follow the roadmap's priority unless a measurement on this
  host contradicts it.
- Every statement carried from either document into a repository record keeps its status: PLAN (from
  the roadmap), SCOUTED (from the log, not run), MEASURED (by you, here, with command and output).
  Only MEASURED may be written as installed or working.
- The survey starts from the scout log's list and does not repeat its evaluations: add what changed,
  what the log did not cover, what a measurement here refutes.
- A blocked roadmap step is recorded with its evidence and left; continue on the open paths.

## 2 · Mandate

Make Drug Repurposing a strong, first-class module of LEGEND. LEGEND's research exists first to
produce inferences, hypotheses and experiments, and second to be leveraged by a repurposing module.
The module's value is that it runs inside LEGEND on the whole WWOX patrimony: receipted readings,
deepdive manifests with verbatim locators, the four scientific current files, the registries, the
research batches, the discovery ledger, the candidate cards. An external repository cannot have
this. Anything that would work as well outside LEGEND is the wrong thing to build.

Strong means coverage of the join between external evidence and LEGEND's own evidence, and the
ability to tell the research what to measure next. It does not mean many tools.

Principles, from the operator's documents:

1. Do not write from scratch what the field's best already does. Survey, adopt, install. Best of
   best changes, so the module is a thin layer of adapters around replaceable parts.
2. Lean, modular, flexible. Every external part sits behind one small adapter with a declared input
   and output contract, is added by one file and removed by deleting it, leaves nothing in the
   registries. Removal is a one-commit act with a regression proving nothing else broke. No new
   gate, no mandatory registry, no governance for its own sake.
3. The join is the differentiator. External evidence (targets, drugs, signatures, trials, safety) is
   bound to LEGEND's receipted WWOX evidence by locator, never substituted for it. A non-WWOX source
   stays labelled NOT WWOX EVIDENCE.
4. Adopted is not installed is not verified. Every tool gets a measured run on this host before it
   is called usable.

## 3 · Measured starting point (re-measure; trust nothing here without a command)

Present, tested, enrolled, routed: `framework/scripts/repurposing_bridge.py` (cards with states
MATCH_FOUND, NO_MATCH_FOUND, QUERY_ERROR, NOT_ATTEMPTED; translation block; no score, rank or
probability; design note `docs/repurposing_bridge_20261015.md`), `clinical_census.py` (ClinicalTrials
API v2, key-less; real run of 2026-10-20 in the folder), `kg_thin_slice.py` under the hypothesis-forge
skill (Monarch and DGIdb), `paper_packet.py rank`, `check_cards.py` (structure only, not truth),
`locator_audit.py --strength-scan` (advisory; recall 31%, false flags 4%), `record_staged_receipts.py`,
`manifest_receipt_repoint.py`, `docx_media_extract.py`, `discovery_lead.py`, `registry_records.py`,
`derived_inputs.py`, `candidate_tree_freshness.py --regenerate`.

Data and results in the folder: 21 blind-audited cards in `cards/` and `cards_early/`, written by
hand from the manifests and therefore prone to drift (one exposure sentence was superseded already);
P3 reconnaissance (24 known roads, every disease-modification cell empty); the rescue reference
scaffold (160 cells, 157 bound); the P5 two-path comparison in `p5/` (all candidates non-dominated,
seven of twelve deep rows resting on one measurement; a plain lookup misses every row carrying a
WWOX-system measurement; INCONCLUSIVE for choosing a candidate, KEEP for choosing what to measure,
which is the module's real use today); `gse156243/` qualified (digests match; 4 KO and 2 WT; the
universe unresolved; the reversal query INCONCLUSIVE; verbatim tool responses gitignored, committed
copies transformed by a manifest proven byte-reversible). A structured mechanism export exists at
`disease-models/wwox/analysis/data/pathograph_export.jsonl`: an input for the join, not to rebuild.

Not started: P1 installations (nothing installed; `_external_repos/` holds only its manifest; no R
interpreter on this host, which blocks drugfindR twice); P6 to P8 (the GSE156243 block is lifted, the
gold-set block stands until measured otherwise).

Stale surfaces: the `README.md` stage table (still says P4 and P5 not started) and the reconciliation
section on cards. Deliverable E updates them from measurement.

Records of the work that produced this, with the reasons for each decision:
`ledger/tasks/plan/PLAN-REPURPOSING-INTEGRATION-20261020.json`, `PLAN-STRENGTH-SCAN-20261022.json`,
`ledger/tasks/integrator/BATCH_20261019_012.json` to `_014.json`,
`ledger/tasks/orchestrator/ORCH-REPURPOSING-10H-20261021.json`, the Scientist records under
`ledger/tasks/scientist-a/` to `scientist-d/`.

Evidence quality to carry, never to hide: this week's blind audits found adverse rates between 3.8%
and 18.8% (`page_adjudications/locator_audit_*_20261022.md`). A repaired entry carries a
`contradicts_locator` declaration with a verdict and an auditor count; zero auditors means
unaudited. 28 figure attestations are still UNVERIFIABLE because the image reader failed, not the
reading. The module may consume a locator only with its audit status attached.

## 4 · Deliverables, in this order, each landed and pushed on its own

A. Survey, read-only, one note of at most two pages. From the scout log's list and a fresh search:
the 8 to 12 external tools, databases or plugins most worth adopting across target-disease evidence,
drug-target and pharmacology, expression-signature reversal, clinical-trial and regulatory census,
adverse-event and safety data, paediatric and rare-disease repurposing precedents, literature mining.
For each: what it gives that LEGEND lacks; licence and access (anything needing a key or payment is
flagged, never used); install route on this host; what replacing it would take; ADOPT NOW, TRY or
WATCH. Done when every row has all five fields, every ADOPT NOW has a measured dry call here or a
recorded block, and the note says what the scout log already covered.

B. The seam: one adapter contract (one page in `framework/protocols/`) and one adapter directory
under `framework/` (name the path and say why). An adapter declares name, inputs, outputs, network
use, licence, retrieval-date stamping and a self-test; the adapter registry is plain files. Re-use
the bridge's card format as the module output. One CLI: `adapter list | add | remove | selftest`.
Done when a regression removes every adapter in turn and the core still runs, each ADOPT NOW adapter
is MEASURED green or a recorded block, and `scripts/test_tool_routing.py` is green.

C. The leverage, the part nobody outside LEGEND can have. The join that turns the registries into
module inputs, deterministic, re-runnable, incremental (one command refreshes after a batch and prints
what changed): (1) queries derived from claims, hypotheses, discovery ledger, mechanism lines and the
pathograph export, each with the claim or locator it came from; (2) an evidence table per query from
receipts and manifests, carrying depth, audit status from the declarations and the adjudication
files, and the NOT WWOX EVIDENCE label; (3) cards composed from adapter hits plus that table, derived
rather than typed so they cannot drift; (4) a "what to measure next" list per candidate: the single
measurement that would split the dependence, an experiment sketch, the claim it would move. Done when
C runs end to end on the current corpus from one command, its regressions are enrolled, and its
output for a card that exists in `cards/` can be diffed against the hand-made one.

D. The feedback loop into research: a short, routed procedure by which a module result (new
candidate, abstention, gap, measure-next) becomes a Scientist assignment, a selection-file row or a
hypothesis, so batches are steered by the module and the module is fed by batches. Prefer a mode of
an existing tool over a new one. Done when one real result from C is turned into one real row for the
next batch.

E. Proof on the real corpus: run C on the three live axes (missense-class proteostasis, T-type
calcium axis, downstream Wnt/MYC/GSK3/mTOR) and report honestly what the module found that the
hand-made cards did not and what it missed that they had. Update the `README.md` stage table and the
reconciliation from measurement.

## 5 · Hard limits, binding every deliverable

- No dose, administration, paediatric suitability or individual recommendation. A drug named in a
  card is a hypothesis for discussion with a treating team and for laboratory design.
- No score, rank, probability or best-candidate output. Comparison only on the same target, endpoint
  and context; non-dominated sets are allowed, a scalar is not; abstention is a first-class state.
- Every non-WWOX source labelled NOT WWOX EVIDENCE; every external-database statement carries its
  retrieval date and query; NO_MATCH is never written as absence.
- The four scientific current files change only through BATCH_COMMIT. The module writes only
  non-canonical files under the folder, `framework/` and its adapter directory.
- No external spend, no keys, no private data, no individual-level record, nothing to the public
  release repository.
- Installations: `pip --user` and virtual environments are yours to take. Anything needing `sudo`, a
  system package or an R interpreter is a recorded block with its evidence; continue on open paths and
  list the blocks for the operator in each stage report.
- Readings: you do not read papers. A reading need becomes a line in your task record and a row
  proposed for the next Scientist batch.
- Never loosen a guard or a test to pass; repair the cause. New tests are executable, run with
  `verbosity=2`, enrolled in `scripts/run_release_regressions.py`; new tools routed in
  `framework/scripts/README.md`.
- The publication gate blocks truncated digests, e-mail-looking strings and parent-side terms paired
  with variants in records; write around them.

## 6 · Lessons that cost time this week

- A locator count is the length of `verbatim_locators['entries']`, never the length of the mapping.
- Exit status after a pipe is the pipe's; `2>&1 | tail` can reorder the two streams.
- Wait for a job by `process_wait.py --pid <PID:START>`; `--identity` only prints; `pgrep -f`
  matches the waiter itself.
- Release battery: fresh clone of the landed SHA, hard-link `files/`, launch detached with
  `setsid nohup`, output redirected; about thirty minutes.
- A session limit (HTTP 429) stops agents; resume from durable state (branch, task record, staged
  files), skipping what exists.
- The image reader is flaky; never write a figure value from a placeholder.
- Writes under `.claude/`, to another actor's ledger record, or loosening a scientific guard are
  refused by the permission classifier; do not route around, surface it.

## 7 · Reporting

After each stage, at most fifteen lines in the operator's language in chat and in English in the task
record: what landed (SHA), what was measured, what failed, what was removed or merged to stay lean,
blocks for the operator. The final report adds the self-evaluation per
`framework/protocols/session_self_evaluation.md`, a capability-scout entry and takeaways.
