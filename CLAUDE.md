# CLAUDE.md — LEGEND (public edition)

Guidance for Claude Code — and for any agent or reader — working in this repository. This file is the **operating bootstrap**: read it before doing anything, and read [`framework/state/state_manifest_current.md`](framework/state/state_manifest_current.md) first, every session.

> ## 📌 Public Edition note — read this first
> This is the **public, de-identified edition** of LEGEND. It ships the **full framework** (instruction core, 21 skills, 5 reusable agents, protocols, evaluation, manuals, runnable scripts) plus **disease-level WWOX science from public literature**.
>
> The repository is organized into **three layers**, and that layering *is* the privacy design:
> - **`framework/`** — the generic, patient-free engine;
> - **`disease-models/wwox/`** — the de-identified, disease-level WWOX model, from public literature only;
> - **a private, non-public N-of-1 overlay** — excluded by design and **not part of this repository.**
>
> **What is intentionally omitted**, and what replaces it:
> - **individual-level material** → replaced by a disease-level model ([`disease-models/wwox/disease_model.md`](disease-models/wwox/disease_model.md)) and by the canonical [`working_model_current.md`](disease-models/wwox/registries/working_model_current.md). Where the private edition reasons about one person, the public edition reasons about **the reference genotype** — a WWOX-DEE genotype class;
> - **live operational logs** (`inbox_current`, `session_commit_log`, `legend_activity_log`, `capability_scout_log`) → process records. The reusable capabilities they produced are abstracted into [`framework/eval/learned_gates_registry.md`](framework/eval/learned_gates_registry.md);
> - the **external computational workshop** (`_external_repos` / "officina") → third-party code is not redistributed; see its [manifest](_external_repos/MANIFEST.md);
> - the **research-group knowledge base** → excluded (subjective third-party assessments).
>
> **Privacy:** the public layers operate on public evidence only and contain no individual-level record. **Nothing here is medical advice.**

---

## What this is

LEGEND is **not a bibliography.** It is a cumulative, lossless knowledge system that turns fragmented cross-disciplinary literature into a structured, provenance-tracked model of a rare disease — **while developing evolutionary, self-improving patterns with an automatic compounding effect.** Knowledge and capability grow together, in lockstep.

First disease model: **WWOX-related disorders** (WOREE / WWOX-DEE, SCAR12). Developed in partnership with, and sponsored by, the WWOX Foundation.

**Declared objectives** — mechanism, biomarkers, therapeutic hypotheses, the discriminating experiments that separate them, and **drug repurposing** as a staged track (Track C in [`mission.md`](disease-models/wwox/mission.md)). Repurposing is an objective, not a by-product: it opens as WWOX function, *signed* pathway direction, a proximal Tier 1/2 readout and CNS/paediatric safety become clearer. Until all four hold for a node, repurposing entries stay hypotheses in the discovery and hypothesis ledgers and are never described as candidate treatments.

It is not a software product: there is no build system. The "LINT" is an internal consistency/integrity protocol over the Markdown state ([`framework/scripts/legend_lint.py`](framework/scripts/legend_lint.py)), not a code linter.

## Read order

1. [`README.md`](README.md) — overview + the thesis.
2. [`FAQ.md`](FAQ.md) — the onboarding answers for a first-time reader: capabilities, what distinguishes the method, how a session is triggered, where the studies come from, mission and development rails, and the investment case.
3. [`CAPABILITIES.md`](CAPABILITIES.md) — the census of distinctive patterns.
4. [`ARCHITECTURE.md`](ARCHITECTURE.md) — the three layers, modes, skills.
5. [`framework/instruction/LEGEND_CORE.md`](framework/instruction/LEGEND_CORE.md) — how LEGEND thinks (the operating core).
6. [`framework/instruction/epistemic_discipline.md`](framework/instruction/epistemic_discipline.md) — the honesty machine.
7. [`framework/master/gold_is_in_the_details.md`](framework/master/gold_is_in_the_details.md) — parity of sources.
8. [`framework/manuals/operator_manual.md`](framework/manuals/operator_manual.md) — how to actually run a session.
9. [`disease-models/wwox/registries/working_model_current.md`](disease-models/wwox/registries/working_model_current.md) — the canonical disease-level model.

---

## 🚀 Bootstraps — apply these without being asked

| Trigger | Bootstrap |
|---|---|
| **A new reader asks what you can do, what makes you different, how to start, whether they must paste the studies, what the mission is, or why this deserves investment** | Answer from [`FAQ.md`](FAQ.md) — the seven onboarding answers, with maturity status attached to every capability claim (`BUNDLED` / `IMPLEMENTED` / `SPECIFIED` / `EXTERNAL`). Do not improvise capabilities: if the FAQ and [`SKILLS.md`](SKILLS.md) do not claim it, it is not shipped. |
| **Every session** | Read [`framework/state/state_manifest_current.md`](framework/state/state_manifest_current.md) first and confirm `current_state: READY`. |
| **Every analytical batch or completed full-text read, before growth/takeaways** | [`legend-session-self-eval`](.claude/skills/legend-session-self-eval/SKILL.md) → runs [`session_self_evaluation.md`](framework/protocols/session_self_evaluation.md): execute Part 1 and write the Part 2 diagnosis. A failing executable check blocks closure/`BATCH_COMMIT`; a weak judgement answer owes a proportional micro-upgrade before the session is described as complete. **The upgrade is the answer, not the promise of one.** Run it *before* takeaways: takeaways written first will describe a session that went well. |
| **Every session, before closing** | [`legend-capability-scout`](.claude/skills/legend-capability-scout/SKILL.md) — each session must leave at least one proportional micro-upgrade of *capability*, not only of knowledge. |
| **Every session, final response** | [`legend-session-takeaways`](.claude/skills/legend-session-takeaways/SKILL.md) — a compact, tabular, high-signal summary of what was *learned* and why it matters. Never skip it because details were logged elsewhere. |
| **A list of studies / PMIDs / DOIs / titles arrives, with "start / process / analyze / ingest / continue"** | [`legend`](.claude/skills/legend/SKILL.md) is the default orchestrator (autopilot). Study-intake triage is Phase 1 *inside* it, not the whole process. |
| **Any study list, before INGEST / full-text / DEEP_DIVE** | [`legend-study-intake-triage`](.claude/skills/legend-study-intake-triage/SKILL.md). Never spend deep-dive tokens before the list is classified known / in-pipeline / new / ambiguous. |
| **After intake, on the whole batch** | [`legend-batch-inferential-sweep`](.claude/skills/legend-batch-inferential-sweep/SKILL.md). `OUT_OF_SCOPE_LIKELY` can still be `DISCOVERY_ONLY`, `REPURPOSING_SEED`, `SAFETY_SIGNAL` or `ENDPOINT_SEED` — do not lose oncology / adult-neurology / immunology signals. |
| **Whenever the sweep runs** | [`legend-proband-priority-matrix`](.claude/skills/legend-proband-priority-matrix/SKILL.md) — rank by disease-specific axes (proteostasis, splice/ASO, gene therapy, network/seizure/sleep, myelin/glia, neuroinflammation, metabolism, repurposing, BLOCK-1 safety). Ranking aid only, never canonical evidence. |

---

## 🔴 Parity of sources — the superordinate principle

> **It overrides every gate, score, tier and matrix.** There is no hierarchy of importance among studies, and there is no study that "does not deserve" to be read. **The gold is in the details**, and the decisive detail can live anywhere — above all where the title promises nothing.

This is not an aspiration. On **2026-07-12** a paper on **thyroid cancer**, filed `Tier C`, showed that **P252A — not Q230P —** undergoes HSC70-associated lysosomal turnover and does not respond to MG-132. It demonstrated that a proteasome-only test could not exclude other turnover routes, risking a non-informative result being read as a **false negative**, and forced the separation of *synthesis · solubility · turnover · route · function*. The subsequent undue transfer to `Q230P → CMA` was itself corrected. The case proves both the value of cross-context reading and the risk of mechanistic over-transfer.

**Why the intuitive hierarchy is exactly inverted:**
- 🧬 **Oncology papers are twenty years ahead.** WWOX began as a tumour suppressor: the labs doing its real molecular biology (folding, stability, degradation routes, partners, localization, rescue) are cancer labs. *The biology needed to interrogate an allele often emerges there*, not in case reports.
- 🧠 **Adult neurology** (Alzheimer, Parkinson, ALS, tau) — fully relevant: shared pathways, proteostasis, biomarkers, endpoints, drugs already tested in humans.
- 📋 **WOREE papers** are the most *phenotype-coherent* but largely **descriptive**: they photograph the disease, they rarely give a lever. Coherence ≠ usefulness.
- 🐄 **The "noise"** (bovine, coronavirus, plants, basic biology) still yields a method, an assay, a partner, a heuristic.

**Binding operating rules:**
1. **No tier, score or category authorizes NOT reading.** `P4_BACKGROUND`, `DISCARD_LOW_SIGNAL`, `OUT_OF_SCOPE_LIKELY`, `Tier C` mean **only "later in the queue"** — never "never". They are *transient states*, not destinations.
2. **Ranking orders reading. It does not replace or negate it.** If a ranking ends up discarding a study, **the ranking is broken** — fix the ranking, do not lose the study.
3. **Disease context is never a reason to downgrade.** A thyroid, breast or lymphoma paper touching WWOX is worth as much as — often more than — a WOREE case report.
4. **`grep`/keyword is forbidden as a method of analysis** — only for technical file search, dedup, or post-reading audit. Never to decide what a paper says.
5. **For every available full text:** inspect beyond abstract and conclusions (Methods, Results, figures/tables, limits, supplementary) and produce a **coverage map**. `Evidence depth: full text reviewed` requires `coverage_status: complete_fulltext_read`; otherwise declare `partial full text` or `FULL TEXT LARGE — COMPLETE READING IN PROGRESS`.
5b. **Capture the verbatim locator while the document is open.** For every statement the reading will carry out, record what it is evidence *for*, the sentence quoted **verbatim**, and where it sits — section, figure or table. They go in the work manifest under `verbatim_locators`, and a `complete_fulltext_read` is refused without them. 🔴 **A receipt attests that a document was read; it does not attest which sentence supports which statement.** On 2026-08-04 an export found that *no verbatim locator existed anywhere in the canonical state*, across every complete read in the ledger — fourteen had to be recovered by reopening papers already read. Capturing costs seconds; recovering costs the reading twice. If a reading supports no statement, waive with an argument: waiving is legitimate, silence is not.

5c. 🔴 **A verbatim locator may only be verified against text extracted deterministically.** The
question is not which tool is best — tools age, and naming one here would be a hand-pinned
constant in prose. The question is whether the character sequence you match against is *the
author's*. A model that converts a PDF to Markdown reconstructs: it normalises, re-flows,
occasionally paraphrases. A quote checked against that output can pass while matching **the
reconstruction and not the paper** — the gate would report `verified` on a sentence nobody
wrote. That is the worst class of false positive this system can produce, because it is silent
and it wears the badge of having been checked. ML converters are legitimate *reading aids* and
must never be declared as the artifact behind a locator. `deepdive_manifest._artifact_text`
already enforces half of this: it verifies text only for `.xml`, `.html`, `.txt`, `.docx` and
refuses every other suffix for a text `kind`, so a PDF cannot itself be a text surface. The
half it cannot see is *how a `.txt` was produced* — so a derived text artifact declares its
extraction method, and the reading declares both artifacts fingerprinted: the original as
`article_binary`, the extracted text as `article_text`. Figures are a separate surface and are
inspected at original resolution, never read through a text conversion — on 2026-08-04 a figure
panel reversed a conclusion the running text did not contain, and on 2026-08-06 an unmarked
asterisk was the difference between "not significant" and "not tested".
6. **Reading debt is explicit and must be honoured:** what was not read today enters the queue with a tracked debt; it does not disappear.
7. **Universal full-text trace:** every route that actually analyses a full text must emit a `FULLTEXT_READ_RECEIPT` and the main session must persist it before reporting the paper as read. Check prior receipts first; a repeated complete read requires an explicit `reread_reason`. Retrieval, indexing, PaperQA/RAG queries and selected passages are not a complete read. Protocol and schema: [`fulltext_read_receipt.md`](framework/protocols/fulltext_read_receipt.md).

8. **A local abstract corpus is a map, never the territory.** [`pubmed_corpus_harvest.py`](framework/scripts/pubmed_corpus_harvest.py) harvests every record a documented PubMed query returns — for WWOX, 706 with 693 abstracts — into a gitignored `files/corpus/` artefact that carries its own `evidential_status: NOT_EVIDENCE`. **Permitted:** triage and ranking, census (what exists against what has been read), export pre-flight, and an honest `abstract_only` receipt that never clears reading debt. **Forbidden:** treating it as a full-text reading. **Un abstract non è una lettura.** New complete reads are fail-closed at the authoritative append primitive: they require a local full-text artifact with matching SHA-256 and a schema-v2 work manifest in which every evidentiary locator names a non-abstract `surface` and fingerprinted `artifact`; text locators are matched against the declared artifact with the XML abstract separated from its body. Missing validators, artifacts, surfaces, exact quotes or declared gaps block persistence. This is enforced in the writers and mutation-tested, not merely stated in [`test_abstract_corpus_is_not_evidence.py`](scripts/test_abstract_corpus_is_not_evidence.py). The hazard is not that anyone decides to cut corners — it is that hundreds of abstracts sitting locally and greppable make answering from them *feel* like working. Rule 4 already forbids grep as a method of analysis; this is the same rule pointed at the corpus. The harvest is also not "every paper on the gene": PubMed expands a free-text query by Automatic Term Mapping, and the manifest records what it actually ran. The seed preserves PubMed correction links: a retraction or expression of concern creates `PUBLICATION_INTEGRITY_HOLD`, and LINT blocks `BATCH_COMMIT` if a canonical claim links the held PAPER; ordinary errata remain annotated but do not trigger the hold.

Full statement: [`framework/master/gold_is_in_the_details.md`](framework/master/gold_is_in_the_details.md).

---

## 🌱 The system is alive and always growing — design for that, never for today

> **LEGEND is never finished, and no artefact in it may assume it is.** The corpus grows every
> day. Batches follow batches, exports are periodic and in principle endless, and the model is
> corrected as it grows — correction is not an exception, it is the product.

**Calibrate before designing.** Today: ~15 complete reads, 39 canonical claims, 49 integrated
papers, 358 corpus placeholders. One PubMed query on one gene returns 706 records. The
intended trajectory is **hundreds of thousands of full texts and beyond** — the WOREE field
leaders first, then all of WWOX, then everything that cascades: MYC, WNT, genotypes,
phenotypes, symptom-specific therapies, and whatever is needed for the inferences and the
inferences upon inferences. Growth is slow *now* because the infrastructure of tomorrow is
being built so nobody has to reopen it later. **Today's numbers are a starting point, never a
design target.**

🔴 **The question every check, constant, seal, baseline and ratchet must answer before it
ships: _will this still be informative at the thousandth batch?_** A control that is correct
today and noise at scale is not a control — it is a future alarm nobody hears, and the day it
means something no one will look.

**Four binding consequences, each learned by paying for it:**

1. **Never pin a number a human must remember to update.** The change must be re-anchored by
   the tool that causes it, as `fulltext_receipts.py record` re-anchors the ledger. The real
   criterion is sharper than "automate it": **updating a constraint must cost at least as much
   as complying with it.** When updating is cheaper than conforming, the guard is already
   lost — someone will bump the number to make the suite green, which is precisely the gesture
   the check existed to prevent. That has already happened here, diligent comment and all.
2. **A freeze over living state reports drift; it does not assert violation.** Immutable
   inputs are sealed whole. Living state — canonical registries, append-only ledgers — is
   verified by *what was consumed*: prefix digests, extracted scope. And because exports are
   periodic and the model keeps being corrected, each past seal would otherwise go red at its
   own moment, correctly and uselessly. History informs; the gate bites at export time, where
   shipping a contribution derived from superseded claims is the real risk. See
   `FREEZE_SCOPE_GATE` and [`scripts/test_freeze_scope.py`](scripts/test_freeze_scope.py).
3. **A fact about an external database is derived and cached, never hand-declared.** At five
   hundred manifests "visible in review" means invisible: it presumes a reviewer who, at
   scale, does not exist.
4. **State scale assumptions out loud.** An artefact that silently assumes the current volume
   is a defect waiting for a quiet birthday. If a design only works below some size, write the
   size down.
5. **Before building a guard, look for it — it is probably already here.** Three times in one
   day the correct pattern existed in this repository, applied at one site and not carried to
   the second: `append_only_prefix` in the ledger but not the registries; the corpus marker
   copied into four guards; `tracked_paths()` unused by two checks in its own file. The
   failure mode of a system that grows by accretion is not ignorance, it is **uneven
   application**. Grep the vocabulary — `prefix`, `anchor`, `tracked`, `scope`, `ratchet` —
   before inventing a mechanism, and if you diverge from what you find, say why.
   `PATTERN_ALREADY_SOLVED_GATE`.

**Why this section exists.** The receipt ledger was given `append_only_prefix` because someone
thought about growth — for the file that grows. The registries never got the equivalent, and a
2026-08-06 re-seal fixed *which bytes* were pinned without fixing *what happens over time*.
The principle was understood and applied unevenly, twice. It is written here so the next design
inherits it instead of rediscovering it.

## System architecture — layers

| Layer | Folder | Purpose |
|---|---|---|
| **0 — State** | [`framework/state/`](framework/state/) | `state_manifest_current.md` — single source of truth: framework version, WM version, file status, last batch/lint, gates. It is the only **state-control** file writable outside a `BATCH_COMMIT`; designated non-canonical append-only ledgers (including the full-text receipt ledger) are explicit, validated carve-outs. |
| **1 — Instruction** | [`framework/instruction/`](framework/instruction/) | `LEGEND_CORE.md` + `epistemic_discipline.md` — how LEGEND thinks. |
| **2 — Current (scientific)** | [`disease-models/wwox/registries/`](disease-models/wwox/registries/) | `working_model_current.md`, `claim_registry_current.md`, `paper_registry_current.md`, `literature_tracking_log_current.md`. **All 4 must exist before any commit.** |
| **3 — Meta** | [`disease-models/wwox/meta/`](disease-models/wwox/meta/) | `meta_index_current.md` + structured syntheses per biological axis. |
| **4 — Research** | [`disease-models/wwox/research/`](disease-models/wwox/research/) | research lines, candidates, full-text queue, **dismissal ledger**, **discovery ledger**, **therapeutic-hypotheses ledger**. |
| **5 — Biomarker / Endpoint** | [`disease-models/wwox/biomarker_endpoint/`](disease-models/wwox/biomarker_endpoint/) | Tier 1/2 gene-linked biomarkers vs Tier 3 distal clinical endpoints — kept strictly separate. |
| **6 — Operational** | *(private overlay)* | inbox quarantine, commit-candidate queue, activity log, merge-conflict report. |
| **7 — Protocols** | [`framework/protocols/`](framework/protocols/) | batch commit, LINT integrity, ingest, parallel protocol, wikilink schema, file-generation rule, navigation index. |
| **8 — Master** | [`framework/master/`](framework/master/) | the parity-of-sources principle. |
| **9 — Therapeutics** | [`disease-models/wwox/therapeutics/`](disease-models/wwox/therapeutics/) | scored portfolio of candidate strategies. Read-only toward the 4 currents; promotion via pipeline. |
| *— Manuals* | [`framework/manuals/`](framework/manuals/) | operator manual, deep-dive manual. |
| *— Skills / Agents* | [`.claude/skills/`](.claude/skills/), [`.claude/agents/`](.claude/agents/) | 21 skills + 5 reusable agent prompts. |

**Cross-references are basename wikilinks** (`[[claim_registry_current#CLAIM 019]]`) and are path-independent — they keep working regardless of folder. When locating a file, search by name; the folder only tells you its layer.

---

## Workflow & modes

LEGEND runs in a single session with explicitly declared modes:

- `MODE: LEGEND_AUTOPILOT` — default when a study list arrives. Orchestrates `start → intake-triage → batch sweep + priority matrix → ingest → full-text → deep-dive/discovery → therapeutic fan-out → safety/officina → commit gate → self-diagnosis → capability growth → takeaways`.
- `MODE: DEEP_DIVE` — analyse a paper; output is a **COMMIT CANDIDATE** appended to the commit queue. **Never modifies current files.**
- `MODE: INGEST` — bring a new source through the inbox quarantine (classify → deep dive / queue / filter). Nothing skips quarantine.
- `MODE: STUDY_INTAKE_TRIAGE` — mandatory pre-ingest gate for study lists.
- `MODE: BATCH_INFERENTIAL_SWEEP` — mandatory second pass over the whole batch.
- `MODE: DISEASE_PRIORITY_MATRIX` — disease-specific scoring layer over the sweep output.
- `MODE: LINT` — `LINT_AUTOMATIC` (fast, every session start + pre-batch) or `LINT_DEEP` (weekly/on demand).
- `MODE: BATCH_COMMIT` — propagate queued candidates into the current files. **The only moment current files change.**
- `MODE: PARALLEL_BRANCH` / `PARALLEL_MERGE` — parallel deep dives on disjoint scopes; merge before commit. *Parallel deep dive yes, parallel commit no.*
- `MODE: Q&A` — consultation layer, **non-canonical and READ-ONLY** toward the 4 currents. A Q&A answer is not a claim. Always carries the "not medical advice / discuss with the treating clinical team" disclaimer.

### Operational gates
`current_state: READY` means analytical work can proceed. Commit permission is gated separately in the state manifest:
- `deep_dive_gate` / `ingest_gate` control read-only and new-source work;
- `batch_commit_gate` controls canonical writes;
- `BLOCK_BATCH_COMMIT` blocks BATCH_COMMIT only; `BLOCK_SYSTEM` blocks everything.

### BATCH_COMMIT triggers
Triple trigger — first to fire wins: **weekly** (fixed day) · **threshold** (≥ 5 commit candidates) · **manual**. Execution is gated: trigger → `LINT_AUTOMATIC` → if PASS/WARN proceed, if BLOCK resolve first.

### URGENT_COMMIT_REQUEST (the exception to batching)
Admissible in 5 categories only: (1) a direct safety signal, (2) a grave working-model error, (3) a paper decisive for BLOCK 1, (4) an explicit operator request, (5) retraction/invalidation. **LEGEND proposes; only the operator authorizes. Never self-authorized.** Triggers a MAJOR working-model bump.

### Working-model versioning
Format `WM_vMAJOR.MINOR_YYYY-MM-DD`. MINOR = normal additions/claim updates. MAJOR = baseline-claim reversal, BLOCK-1 policy change, authorized URGENT, retraction of a baseline paper. Every commit candidate declares its `target_wm_version`.

---

## Session types

**Minimal** — load the state manifest + capability-scout + session-takeaways + the 4 currents. If studies are supplied, apply intake, sweep and priority matrix. No commit required.

**Standard** — the above + `meta_index_current.md` + the relevant metas. With a study list, use the autopilot by default and continue autonomously through ingest / full-text / deep-dive / discovery / fan-out where gates allow. Produces commit candidates; propagation via `BATCH_COMMIT`.

**Full** — load all layers. For bootstrap, recovery, batch consolidation, meta propagation, framework changes. Rigorous commit mandatory.

> Prefer a clean Standard session over a Full session on uncertain state. Always read the state manifest first.

---

## Epistemic discipline

Every claim must be explicitly classified (four levels):

- **DATO** — directly supported by a primary/secondary peer-reviewed source. Traceable, citable, not extrapolated.
- **INFERENZA** — plausible, derived from convergence of multiple data points, not demonstrated in the target context. Must be declared as inference.
- **IPOTESI** — reasonable but not directly supported; must be marked as hypothesis.
- **ESPANSIONE** — extension outside the direct domain. Useful for strategy space only; cannot enter the current files as consolidated fact without explicit promotion.

Never present inferences as data, never present expansions or hypotheses as robust inferences.

### 🔴 The discipline applies to PREMISES and NEGATIVES too

The classification above covers **only positive assertions**. Until 2026-07-12 LEGEND had **no discipline** for **premises** (what a claim rests on) or **rejections** (conclusions that close a door). Every error of that day came from that missing side.

**The asymmetry that makes negatives the real danger:** a **false positive** gets tested and dies. A **false negative** is **silent, permanent and self-reinforcing** — once discarded, nobody looks again. In a system that accumulates for months, a false positive is a cost; **a false negative is a compounding loss.** And tiers, gates, filters, `refuted` and *"do not assume…"* are all machinery that **produces negatives**.

**The shape of every error of 2026-07-12: `P → C`, where C is a rejection and P was never checked — because P was the "obvious" part.**

> **The most dangerous premises are the ones too obvious to write down.** Nobody records *"polyubiquitination leads to the proteasome"* as a claim needing a citation: it is background knowledge. Which is exactly why it is never tagged, and therefore never verified. (It was false as a universal rule: **K48 chains commonly support proteasomal turnover; K63 chains have context-dependent roles that include trafficking and selective-autophagy pathways, with CMA demonstrated for particular substrates. The route must be measured.**)

**Three binding obligations:**

1. **`PREMISE_TAG`** — every rejection, and every non-trivial conclusion, must **name** its load-bearing premise and tag it: `PREMISE: DATO` · `PREMISE: INFERENZA` · 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK`.
   > 🔴 **A textbook default is not a foundation: it is a RESEARCH TARGET.** A conclusion resting on one is **provisional by construction**.
2. **`REVIVAL_TRIGGER`** — nothing dies in silence. Every rejection goes into [`dismissal_ledger_current.md`](disease-models/wwox/research/dismissal_ledger_current.md) and declares **what would resurrect it**.
3. **Re-audit rule** — this is the loop that makes it compound. **Every time a new mechanistic `DATO` arrives, re-scan the dismissal ledger** for rejections whose premise that datum touches. Without this step you get self-correction, not self-improvement.

**Before discarding anything, consult the `DEFAULTS THAT BIT US` table** in the dismissal ledger: textbook defaults that in *this* domain already proved false (polyUb→proteasome; misfolded→ERAD/4-PBA; "it's a chaperone"→it helps; stabilize→function restored; the code does what the docs say; the anti-bug tool is immune to the bug).

---

## Claim states

The only valid claim states (exact strings): `consolidated baseline` · `in observation` · `conflicting evidence` · `flagged for review` · `background only` · `archived`.

Do not invent new states or use synonyms. If a non-standard state is found, flag it in the change log and propose the correct state — do not modify it autonomously.

## LINT severity scale

- `INFO` — report only.
- `WARN_BUT_PROCEED` — batch commit possible, warning stays in the queue.
- `BLOCK_BATCH_COMMIT` — commit blocked until resolved (dangling wikilink, claim without supporting paper, non-standard claim status, duplicate IDs).
- `BLOCK_SYSTEM` — everything blocked, recovery first (a missing current file, or a corrupt state manifest).

Biomarker discipline is LINT-enforced: Tier 3 endpoints in the biomarker file, biochemical markers in the endpoint file, or a candidate described as "gene-validated" without a validation paper → `BLOCK_BATCH_COMMIT`.

## Commit rules (hardened safety layer)

A commit is **blocked** if: one of the 4 currents is missing (`BLOCK_SYSTEM`); the commit would rest on state reconstructed from chat memory; there are unresolved mismatches (a claim in the working model absent from the claim registry, a paper in a claim absent from the paper registry); the output is a partial stub; `LINT_AUTOMATIC` returns `BLOCK_BATCH_COMMIT`/`BLOCK_SYSTEM`; or a parallel branch is active and unmerged.

Mandatory blocking message: `FULL STATE NOT AVAILABLE — COMMIT BLOCKED`

**Every valid BATCH_COMMIT must produce:** (1) `FILES TO CREATE`, (2) `FILES TO UPDATE` — rewritten in full, (3) `FILES UNCHANGED` — explicitly listed, (4) a `CHANGE LOG` per modified file with Added / Modified / Unchanged / Removed. "Removed" must be empty except in explicitly justified cases. The 8-phase procedure (inventory → conflict detection → backup → propagation → post-lint → manifest update → cleanup → activity log) is mandatory; abort restores from snapshot. **No partial commits — all or nothing.**

---

## Core operating rules

**Minimal change and verification contract.** Before every non-trivial operational change, state the assumptions, the smallest sufficient change, an observable success criterion, and the final verification. When testing scripts, lint rules, rankings, heuristics or reusable procedures, use [`legend-research-loop`](.claude/skills/legend-research-loop/SKILL.md): establish a baseline, change one conceptual variable, record `KEEP` / `DISCARD` / `INCONCLUSIVE` / `CRASH`. This loop validates only the tested procedure; it never replaces full-text reading, scientific judgement, safety review or the canonical promotion pipeline.

**No rebuild.** LEGEND cannot regenerate current, meta or structural files from chat memory, partial state or inferential reconstruction. Work only from files explicitly provided.

**Lossless.** Every output file must contain all previously valid information. Do not abbreviate, compress or omit sections that are not being changed. Copy unchanged sections verbatim.

**Loss aversion overrides elegance.** In a conflict between a more concise file and a more faithful one, always choose the faithful one.

**Supplementary commit rule.** If an omission is noticed within the same session, emit a supplementary commit immediately — do not defer it.

**Wikilink discipline.** Files cross-reference via `[[file_current#heading]]` per [`wikilink_schema.md`](framework/protocols/wikilink_schema.md). Broken links to entities that should exist are blocking; the LINT validates link integrity.

**File protocol.** All state files are `.md` with the `_current` suffix. Files must be complete, definitive, self-consistent and immediately usable. Partial files, stubs or placeholders are invalid output (`PARTIAL FILE — NOT SAFE FOR REPLACEMENT`). If a file is too long to generate completely and correctly, do not generate it — output the content in chat or give manual creation instructions. Append-only files (commit log, activity log, inbox) never lose entries; only status changes.

---

## Runnable checks

```bash
python3 framework/scripts/legend_lint.py .          # structural LINT over the canonical state
python3 framework/scripts/test_legend_lint.py       # its regression suite
python3 framework/scripts/unread_gold.py --help     # the unread-gold sweep
python3 framework/scripts/fulltext_receipts.py verify  # ledger chain + state-manifest tail anchor
python3 framework/scripts/growth_anchors.py check      # registry cardinality + both debt ratchets
python3 scripts/public_release_gate.py              # the publication gate (privacy, links, provenance)
python3 scripts/run_release_regressions.py          # every release suite at once
```

The `LINT` now reads the full-text receipt ledger as part of the state it validates: a
rewritten, truncated, absent or unparseable reading history blocks the system rather than
passing quietly. Persist receipts with `fulltext_receipts.py record` — hand-editing the
ledger breaks its hash chain and halts LEGEND until the edit is undone or authorized and
re-anchored.

## Recovery

If system state is uncertain or desynchronized, prioritize recovery over progress. Load at minimum the state manifest + the 4 currents + `meta_index_current.md`, run `LINT_AUTOMATIC`, then ask for a coherence verdict before any commit.

Recovery priority order: state manifest → current files → meta index → active metas → research/biomarker layer → protocols → master.

---

Nothing here is medical advice. Therapeutic outputs are material for discussion with a treating clinical team, never a substitute for it.
