---
name: legend
description: LEGEND orchestrator/autopilot — the operator gives a list of studies and the process starts and continues as autonomously as possible. It understands the phase, runs the whole chain (intake→acquire→analyze→therapeutic fan-out→commit→growth), does conditional fan-out to the skills (deepdive, discovery, hypothesis-forge, aso-designer, safety-triage, paperqa) and routes the computational workshop in _external_repos/medical_ai, closing with capability-scout to learn/evolve. Use it for "start LEGEND", "work these papers/studies", "start with this list", "commit". Autonomous by default; it stops only on URGENT cat-1, MAJOR baseline-reversal, or any paid service.
---

# legend — LEGEND autopilot

Paths are relative to root. One entry point: **the operator gives a list of studies → the process starts and continues on its own** through the phases, stopping only at the explicit gates. It dispatches to the atomic skills and routes the external workshop.

Guiding principle: every batch of studies does not merely add or sort knowledge. It must increase the system's power to discover: new connections, hypotheses, therapeutic axes, heuristics, tools and inferential capabilities that make LEGEND stronger on the next batch.

## When it activates

Activate this autopilot when the operator provides a study list, a PubMed/Scholar/Zotero export, PMIDs/DOIs/titles, or says in substance: "start", "work these studies", "analyze them", "proceed", "continue the process".

If the operator explicitly asks only for "dedup", "just triage", "tell me which are new", then use only `legend-study-intake-triage` and stop at the report.

Default: **a bounded autonomous full run**, not single manual skills.

## Autonomy contract (read first)
**Never ask permission** for operational work already pre-approved by the local policy: create a local virtual environment, write/open/read files, run the listed Bash commands, use already-installed **local and free** tools (including `legend-paperqa`), queue a COMMIT CANDIDATE, and write to the carve-out files (discovery ledger, hypothesis ledger, researchers KB, capability scout log). Dependency installation and other network-capable actions require separate approval. Once launched, the process **continues without interruption** across approved operations even if the operator is away. Permissions come from your own `.claude/settings.local.json`; a ready-to-adapt, allow-list-based template ships as [`.claude/settings.json.example`](../../settings.json.example). Copy it, adapt the paths and read its security note first. Do not use `bypassPermissions` on a host workspace; reserve it for an isolated container or VM.

**Only two cases where you STOP for a one-line "ok":**
1. **URGENT cat-1** — a direct safety signal for the case.
2. **MAJOR baseline-reversal** — overturning a baseline claim / a BLOCK-1 policy change.

**One case that is a HARD STOP, not a question:**
3. **Anything paid** (service, API, model, paid license) → **you are not authorized, period.** Do not ask for the ok (the operator will never give it): stop on that branch, use the local/free alternative if one exists, and flag the block while continuing the rest of the work.

**Never**: ask permission outside cases 1–2; write to the 4 canonical current files outside `legend-commit`; present IPOTESI/ESPANSIONE as DATO; false hope; medical advice; self-authorize an URGENT.

---

## The phases (auto-sequenced)

### Phase 0 — BOOTSTRAP & GATE
- `legend-start` → selects the scientific session profile and loads its context + structural LINT.
  - `BLOCK_SYSTEM` → recovery, **STOP**.
  - `BLOCK_BATCH_COMMIT` → read-only analysis continues; only Phase 6 is blocked.
- Growth bootstrap: load `legend-capability-scout` and keep a notepad of the **capability gaps** that emerge during the run (needed in Phase 7).
- 🥇 **"Unread gold" gate — before opening a new batch:**
  ```bash
  python3 framework/scripts/unread_gold.py .
  ```
  Lists `CORPUS` items with `Tier: A` **and** `relevance: HIGH/VERY HIGH` that were **never deep-dived**. `exit=2` → **read those first.** Real error of 2026-07-09: a CORPUS paper (Johannsen 2018) contained the experimental functional datum on a WWOX missense variant of interest (Q230P: normal transcript, **absent protein**), was marked Tier A / HIGH relevance, and had never been opened — while LEGEND was reconstructing the same conclusion in-silico from scratch. **The gold was not in a new study: it was in a study we had already filed and not read.**

### Phase 1 — INTAKE (🚦 MANDATORY GATE — first act, not skippable)
As soon as a list arrives (even 2 studies), the **very first** act — **before any fetch or deep-dive** — is dedup, and it is done **only with the dedicated script**, **never** with ad-hoc grep in the shell (in zsh, variables do not split without `${=VAR}` → false "all new"; a real error of 2026-07-05 that cost time and tokens).

```bash
python3 .claude/skills/legend-study-intake-triage/scripts/study_dedup_triage.py \
  --workspace "$(pwd)" --input <list.txt> --out staging/triage_<date>.md
```
The script (via `legend-study-intake-triage`, or the `study-intake-triage` subagent) normalizes 1→thousands of records and dedups by PMID/DOI/title/author/year against the paper registry, literature tracking log, inbox, full-text queue, commit queue — with a **block index + a global identifier index** (catching PMIDs outside the blocks too) and bare-PMID support.

**Retraction gate — right after dedup, before assigning any tier** (real error of 2026-07-09: the sweep ranked `CANONICAL_CANDIDATE`/`P1_HIGH` a paper retracted for western-blot manipulation, PMID 26041563):
```bash
python3 .claude/skills/legend-study-intake-triage/scripts/retraction_check.py --file <pmids.txt>
```
`exit=2` → flagged papers are forced to `archived`, **never** ranked high, **never** promoted to a claim. If the author group has serial retractions → watchlist in the researchers KB.
- Classes: `KNOWN_INTEGRATED` · `CORPUS_CATALOGUED` (catalogued but **never** deep-dived → gold not yet exploited) · `IN_PIPELINE` · **`NEW`** · `AMBIGUOUS` · `OUT_OF_SCOPE_LIKELY`.
- **`NEW` + `CORPUS_CATALOGUED`** proceed; `KNOWN_INTEGRATED`/`IN_PIPELINE` are skipped unless a full-text upgrade; `AMBIGUOUS` are resolved first.
- ⚠️ If triage seems to say "all new", **it is a bug** → stop, do not proceed. Regression: `python3 .../scripts/test_study_dedup_triage.py "$(pwd)"` must give 5/5.

### Phase 1.5 — BATCH INFERENTIAL SWEEP (do not lose needles)
- `legend-batch-inferential-sweep` → re-reads the whole triaged batch, retrieves PubMed metadata/abstracts when available, assigns operational classes (`CANONICAL_CANDIDATE`, `DISCOVERY_ONLY`, `REPURPOSING_SEED`, `SAFETY_SIGNAL`, `ENDPOINT_SEED`, `READ_QUEUE_TAIL`) and downloads **all** available free PMC full texts (the score decides the **order**, not who gets downloaded).
  🔴 **Classes order the reading queue; they never authorize not reading.** A study's disease context is not grounds for down-ranking: **oncology = ~20 years ahead** on WWOX mechanics (that is where the mechanism of the allele of interest lives), **adult neurology** = pathways and molecules already tested in humans, **WOREE** = consistent but largely **descriptive** (consistency ≠ usefulness). See `CLAUDE.md` → *parity of sources*.
- `legend-proband-priority-matrix` → applied automatically by the sweep when present: adds `proband_score`, `proband_priority_tier` and disease-targeted axes (missense mechanism, splice, proteostasis, ASO, gene therapy, network, neuroinflammation, myelin, repurposing, safety).
- Key rule: **OUT_OF_SCOPE does not mean out-of-discovery**. Oncology, neurology, immunology or adult studies can produce leads for the disease model/WWOX, biomarkers, safety or repurposing even if they never become canonical deep-dives.
- Success criterion: the batch must produce at least one of: insight, hypothesis, safety clue, mechanistic bridge, updated priority, failure mode, or capability micro-upgrade. If nothing obvious emerges, apply super-inference and record why the batch is genuinely low-yield.
- Output: `staging/batch_inferential_sweep_*.md` + optional `.json` + `staging/fulltext_pmc_*`. This report decides Phase 2/3 routing and feeds `legend-discovery`, `legend-hypothesis-forge` and `legend-safety-triage`.

### Phase 2 — ACQUIRE
- `legend-ingest` → quarantine in the inbox, classify each new source (deep-dive / queue / filter). Nothing skips quarantine.
- `find-fulltext` → retrieves the PDF/full-text of deep-dive items, prioritizing items flagged by the sweep as `CANONICAL_CANDIDATE`, `SAFETY_SIGNAL` or high-score repurposing/endpoint.
- If the corpus grew → **rebuild the index** of `legend-paperqa` (one-off; see `legend-paperqa/references/paperqa_setup.md`).
- Group credibility when needed → the `research-group-analyst` subagent (updates the researchers KB).

### Phase 3 — ANALYZE (double lens, per paper)
Before opening the paper, apply the duplicate-work gate in `framework/protocols/fulltext_read_receipt.md`: resolve PMID/DOI and reuse an adequate prior complete analysis. A repeated complete read needs an explicit `reread_reason`.
📖 **The gold is in the details of EVERY study.** Classification decides reading order, not a paper's intrinsic value. `grep`/keyword search is forbidden as a *method of study analysis*: it may serve only to find files, dedup, or do technical audit after reading, never to decide what a paper says. If a full text is available, it must always be interrogated in detail: Methods, Results, figures/tables, limits, materials/supplementary when present. PDF extraction only makes the text readable and citable; it does not license selective reading. Minimum output per full text: a section-by-section coverage map, checked details, unread/unavailable details, and a status (`partial_fulltext_read`, `complete_fulltext_read`, or `FULL TEXT LARGE — COMPLETE READING IN PROGRESS`). `Evidence depth: full text reviewed` is admissible only with `coverage_status: complete_fulltext_read`. If the study is `P0_FAST_TRACK`, `P1_HIGH`, `CANONICAL_CANDIDATE`, WWOX-direct, model-shifting, safety-relevant, therapy/GT/ASO-relevant, or the operator calls it important, the full reading must be completed before the final analysis.

💎 **Every study is gold — an inviolable rule.** Every paper (even on animals, the elderly, cancer, or non-WWOX) condenses years of research. **If you have the full text, you analyze it anyway**, at minimum **Methods + Conclusions** (+ key results), looking for: a reusable assay/reagent/model, a mechanism/pathway, a biomarker, a repurposing rationale, a safety signal, a failure mode, or a new research line. **"Zero leads" is not an admissible outcome when the full text is present**: it means shallow or missing analysis. If truly nothing obvious emerges, apply super-inference and **record in the discovery ledger *why* it is low-yield** (that too is information).
- `legend-deepdive` → canonical analysis + multi-hop expansion → a **COMMIT CANDIDATE** queued (never touches the current files). For WWOX-central / `CANONICAL_CANDIDATE`.
- `legend-discovery` → mines **every** full-text study for **needles**: WWOX functional-state biomarkers, correctable molecules/pathways, drug repurposing → the discovery ledger. It is the lens that guarantees "every study is gold".
- `legend-paperqa` (evidence engine, **local/free**) → cited answers and contradiction detection over the corpus, as verifiable support to both lenses. Questions on mechanism/variant only.

Every route that actually reads a full text must return a `FULLTEXT_READ_RECEIPT`. The autopilot/main session persists that receipt before it reports the paper as analysed or moves it out of reading debt. A read-only subagent returning a receipt is not enough until the caller persists it.

**`verbatim_locators` are captured while the document is open, not recovered afterwards.** New complete reads use schema-v2 work manifests. Every carried statement records what it is evidence *for*, the contiguous sentence quoted **verbatim**, its anchor, a non-abstract `surface`, and the fingerprinted local `artifact`. Text quotes are verified against that artifact at persistence time with an XML abstract separated from its body; figure evidence binds to the inspected image hash. `framework/scripts/deepdive_manifest.py` and the authoritative append primitive refuse missing validators, artifacts, locators, exact matches and declared gaps. A receipt attests reading; it does not make an abstract into the paper.

Persist it with the executable — never by hand-editing the ledger, which would break its hash chain and halt the system:

```bash
python3 framework/scripts/fulltext_receipts.py status --pmid <PMID>   # preflight: already read?
python3 framework/scripts/fulltext_receipts.py record --receipt <event.json>
```

`record` appends under an exclusive lock, verifies the whole prior history, and re-anchors the state manifest. If it fails, the outcome is `ANALYSIS_DONE_RECEIPT_NOT_PERSISTED`: report the failure and leave the paper in reading debt. Never report it as read.

### Phase 4 — THERAPEUTIC FAN-OUT (fires when leads/targets emerge)
Trigger: Phase 3 produces a therapeutic lead (target, correctable pathway, attackable variant, candidate molecule).
1. `legend-hypothesis-forge` → generate→critique→rank→evolve therapeutic hypotheses across the 5 levers → the therapeutic hypothesis ledger.
2. Lever 1 (splice correction, e.g. `c.1057-2A>G`) → `legend-aso-designer`.
3. Any **molecule** hypothesis (repurposing/small-molecule) → `legend-safety-triage` (**BLOCK-1 gate**: ADMET+BBB+alerts). An unresolved red flag → it does not advance.
4. Mature hypotheses → `proposed-to-portfolio` flag toward the therapeutic strategy tracker.

### Phase 5 — WORKSHOP (`_external_repos/medical_ai/`) — computational back-ends on demand
The workshop is **not run in bulk**: each tool is a back-end that the relevant skill invokes when needed, with output **always tagged `IPOTESI`/`ESPANSIONE`** (never auto-canonical). Routing in `references/officina_routing.md`.
- **Ready now (local, free):** `paper-qa` (via `legend-paperqa`).
- **Light/CPU, wireable on first use (pip):** `admet_ai`+`medchem` (for `safety-triage`), KG queries like PrimeKG, `biopython`/`bioservices`.
- **Heavy/GPU or big-data, on demand:** repurposing KG (`TxGNN`,`DRKG`,`RTX`/`RTX-KG2`,`matrix`,`repuragent`) · ASO chem (`ASOptimizer`) · protein/AAV design (`RFdiffusion`,`BindCraft`,`LigandMPNN`,`boltzgen`,`AAV_capsid_receptor`,`fit4function`) · CRISPR (`crisprDesign`,`PEGG`,`off_target_prediction`).
- **Rule:** on first use each tool is installed in an out-of-repo venv. If a tool needs a GPU/paid service → do not force it: flag the gap to Phase 7 and propose the local alternative.

Routing read trigger: as soon as a phase produces a lead (`target`, pathway, molecule, variant, biomarker, drug-repurposing clue, ASO/splice clue, chaperone/stabilizer clue), read `references/officina_routing.md` and pick the minimal useful backend. Do not ask the operator which repo to use unless cost/GPU/long setup or a blocking ambiguity.

### Phase 6 — COMMIT (gated) + views
- BATCH_COMMIT trigger (≥5 candidates AUTO · weekly AUTO · manual request) → `legend-commit` (LINT-gated, snapshot/restore, all-or-nothing). Otherwise leave queued.
- `BLOCK_BATCH_COMMIT` active → `legend-lint-repair-plan` produces the gate-aware repair plan (does not apply canonical fixes unless asked).
- Status/navigation → `legend-dashboard` updates the Obsidian views (non-canonical, never source of truth).

### Phase 7 — SELF-DIAGNOSIS (every analytical run, before growth)
- Run [`framework/protocols/session_self_evaluation.md`](../../../framework/protocols/session_self_evaluation.md): executable Part 1 first, then write the evidence-backed Part 2 diagnosis.
- Validate every completed PMID with `deepdive_manifest.py`; check source parity, research-group fit, field density, hidden findings, DATO/INFERENZA separation, ledger/wiki landing, skill decisions, process errors/retries, concurrency and residual reading debt.
- A Part 1 failure is `BLOCK_BATCH_COMMIT` and forbids a green closing statement. A weak Part 2 answer must produce a proportional micro-upgrade or an explicit owned debt before proceeding.
- Never draft the takeaways first: the diagnosis determines what capability must grow.

### Phase 8 — GROWTH (learn/evolve, every run)
- `legend-capability-scout` → **at least one micro-upgrade mandatory**, proportional to the session (an audited import, a new mini-procedure, a resource monitor, or an improvement to an existing skill) + a record in the capability scout log. Zero growth is not admissible.
- Apply the Discovery Power Principle: if a batch reveals a process limit, turn it into a stable procedure, skill, script, rubric, ledger or routing. The repo must grow in knowledge **and** in discovery capability.
- When useful, update the state manifest + the activity log, respecting the gates.

### Phase 9 — TAKEAWAYS (return to the operator)
- `legend-session-takeaways` → always close with the distillation of what the run learned: disease model/WWOX, biomarkers, therapies/repurposing, strategy, safety, capabilities gained, and the next step.
- This output is communicative/non-canonical: it creates no claim.

---

## Status updates in chat
At the end of a run, summarize compactly: intake (new/dup/ambiguous), how many deep-dives and COMMIT CANDIDATEs, discovery leads, therapeutic hypotheses generated/`proposed-to-portfolio`, BLOCK-1 signals, commit status (done/queued/blocked), the capability micro-upgrade recorded, and the `Session takeaway`.

## Honest limits (do not promise more than this)
- **Bounded autonomy, not uncontrolled self-rewrite:** "evolve/grow" = controlled `capability-scout` proposals + explicit builds, audited; not unsupervised rewriting of the system.
- **Heavy workshop = setup on first use:** many repos need venv/data/GPU; not all "just run". The first use of each is a small one-off wiring, then it becomes routine.
- **The epistemic gates and carve-outs stay inviolate** even in full autonomy: speed does not override BLOCK-1 or the canonical pipeline.

## Skill map (who does what)
`legend-start` gate · `legend-study-intake-triage` intake/dedup · `legend-batch-inferential-sweep` second lens over the whole batch · `legend-proband-priority-matrix` targeted biological ranking · `legend-ingest` quarantine · `find-fulltext` PDF/PMC · `legend-deepdive` canonical claims · `legend-discovery` needles/leads · `legend-paperqa` local cited RAG · `legend-hypothesis-forge` therapeutic hypotheses · `legend-aso-designer` splice-switching · `legend-safety-triage` ADMET/BLOCK-1 gate · `legend-commit` BATCH_COMMIT · `legend-lint-repair-plan` fix-plan · `legend-dashboard` views · `session_self_evaluation` diagnosis · `legend-capability-scout` growth · `legend-session-takeaways` cognitive return.
