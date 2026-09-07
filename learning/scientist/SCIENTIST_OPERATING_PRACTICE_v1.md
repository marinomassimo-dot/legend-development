---
artifact: LEGEND learning — the Scientist operating practice that already exists, reconstructed from its own artifacts
analysis_id: SOP-v1
version: 1
authored_by: scientist-c
authored_in: worktree lettore-c, branch lettore-c, HEAD 908197b
authored_on: 2026-08-25
governance_version_in_this_checkout: 3.1.1
authority: none — this is a reconstruction. It assigns nothing, activates nothing, amends nothing.
mode: REHEARSAL
standing: none — retained, not evidence
absent_objects: [TASK_ASSIGNMENT, TASK_ACK, TASK_CLAIM, CHECKPOINT, LEDGER_EVENT, REVIEW]
independence_spent: none — no scientific source was opened for this work
related: SCIENTIFIC_WORKFLOW_MODE_ANALYSIS_v1.md (SWMA-v1, same actor, same worktree)
---

# The Scientist practice LEGEND already has

## 0 · What this is, and what it was built from

### 0.1 · Its own standing

Same declaration as [`SCIENTIFIC_WORKFLOW_MODE_ANALYSIS_v1.md`](SCIENTIFIC_WORKFLOW_MODE_ANALYSIS_v1.md)
§ 0.1, and for the same reason: no `TASK_ASSIGNMENT` names this file, no `TASK_ACK` accepted it,
no checkpoint binds it, `roles/scientist.md` is still `PROPOSED`. It is retained, and it is not
evidence. A document that reconstructs an evidence discipline must not exempt itself from it.

### 0.2 · The evidentiary base, enumerated before it was measured

This reconstruction is **not** an introspection. It was derived from durable artifacts in this
checkout, counted before being described. Everything numeric below is object-derived — it
describes files that exist at `908197b`, not a population that decays:

| Artifact class | Location | Count |
|---|---|---|
| Deep-dive work manifests | `disease-models/wwox/research/deepdive_manifests/` | **64** (60 schema v2, 4 legacy) |
| Verbatim locator entries inside them | same | **1002** |
| Full-text prose dossiers | `disease-models/wwox/research/fulltext_dossiers/` | **33** |
| Read-receipt ledger events | `disease-models/wwox/registries/fulltext_read_receipts.jsonl` | **128**, over **89** distinct `study_id` |
| Post-batch session evaluations | `disease-models/wwox/research/session_evaluations/` | **22** |
| Commit candidates | `disease-models/wwox/research/commit_candidates/` | **16** |
| Learned gates | `framework/eval/learned_gates_registry.md` | **79** rows |
| Page adjudications | `disease-models/wwox/research/page_adjudications/` | **3** papers |
| Pattern audits | `disease-models/wwox/research/pattern_audits/` | **1** paper, 2 files |

Normative texts read in full: `framework/instruction/LEGEND_CORE.md`,
`framework/instruction/epistemic_discipline.md`, `framework/master/gold_is_in_the_details.md`,
`framework/manuals/deep_dive_manual.md`, `framework/protocols/fulltext_read_receipt.md`
(§§ 1–165), `framework/eval/learned_gates_registry.md`, `framework/eval/failure_taxonomy.md`,
`roles/scientist.md`, `.claude/skills/legend-deepdive/SKILL.md`,
`.claude/skills/legend-locator-audit/SKILL.md`, and the module docstrings of eleven scripts in
`framework/scripts/`. Reading traces read as worked examples: the commit bodies of
`lettore` (`848db6e`, `d756b65`, `84b3cd6`, `2c15a8a`, `9b0cf47`) and the
`PMID 42422765` dossier in full.

**Deliberately not read:** `learning/plan/`, `learning/scientist-b/` and
`runtime/handoff/**` on branches this worktree is behind — including
`SCIENTIFIC-PIPELINE-PREPARATION-001.md`, whose existence is recorded here and whose content is
not. Part 4 of this document proposes contract topics; a peer's proposal for the same pipeline,
read first, converts an independent derivation into an echo. If the two converge, that is a
signal only if they did not consult each other.

### 0.3 · Method, and its one weakness

The workflow below was reconstructed from three kinds of trace, in decreasing order of trust:

1. **machine-checked structure** — manifest fields, receipt coverage maps, validator refusals.
   These record what the practice *did*, and could not have been written otherwise;
2. **contemporaneous prose** — dossiers and commit bodies written while the paper was open;
3. **normative text** — the manual and the protocols. Read *last*, so that the practice was
   reconstructed from behaviour and then compared to the rule, rather than the reverse.

The weakness: this actor has read these documents and cannot un-read them. Where a practice is
inferred from prose rather than measured, this document says so.

---

# PART 1 — The current implicit Scientist workflow

A LEGEND Scientist reading a new WWOX paper runs, in this order, thirteen phases. Six of them
happen **before a single line of the paper is read**, which is the single most distinctive
property of the practice.

---

## 1.0 · Phase 0 — Before the paper: has this already been read?

The first gesture is not acquisition. It is the **duplicate-work gate**
(`fulltext_read_receipt.md` § "Before reading"): resolve PMID *and* DOI, then query the receipt
ledger.

- an existing `complete_fulltext_read` with adequate coverage → reuse, do not re-read;
- an existing partial receipt → **resume from the uncovered sections**, do not restart;
- a new complete read requires an explicit `reread_reason` from a closed list.

Measured: **all 128** ledger events carry a `reread_reason` field. The gate is not advisory.

This is the cheapest failure this system can have and the one it treats most severely, because
the opposite error is worse: `unread_gold.py` exists because on 2026-07-09 (FM-011) LEGEND
re-derived *in silico* a functional datum on a WWOX missense variant that was already sitting in
its own corpus as an unread `Tier A` / `Relevance HIGH` placeholder. Triage had classified it
correctly; **reading priority, not triage, was the defect**. The script's default output is
exactly that set: Tier A + HIGH/VERY HIGH, never deep-dived, *to be read before any new batch is
opened*.

> **The first question is not "is this paper good?" It is "what do I already hold that I have not
> read?"**

## 1.1 · Phase 1 — Who wrote it (area 9)

`deep_dive_manual.md` § 6.0 makes group analysis **STEP 0, executed first**, before the full-state
scan and before the text. Four operations:

1. **Disambiguate the authors.** Same surname + different initial = potentially distinct people.
   The manual names the high-risk set explicitly (Wang, Kim, Chen, Liu, Hsu, Lo, Chang) and fixes
   the discriminator: **affiliation**, plus ORCID / corresponding email / co-author overlap.
   Unresolved identity is recorded as `AMBIGUOUS — verify`, never guessed.
2. **Profile the senior/corresponding group**: real experimental research (lab / models / therapy
   / trials) versus observational-only versus *academic production* — synthesis with no new
   message. Funding, conflicts, track record.
3. **Weight, do not decide.** The manual states it flatly: group credibility *"NON decide la
   verità del claim"* — it raises or lowers **priority and depth of analysis**, nothing else.
4. **Emit an ALERT** for a high-credibility, high-relevance group so the reading gets more depth,
   not more trust.

Measured, and stronger than the manual: **all 64 manifests carry a `group_assessment` block**,
and **all 64 carry `field_density`, `multihop`, `corpus_crossquery` and `retraction_check`**.
These four are the `OBLIGATION_WITHOUT_ARTIFACT_GATE` in force — a required step that would
otherwise leave no trace is given a mandatory field, so "I assessed the group" cannot be asserted
without a record of what was assessed.

Two refinements the practice actually applies, visible in the artifacts:

- **counts, not impressions.** `PMID25491415.json` records
  `Aqeilan RI[Author] = 137; … AND WWOX[Title/Abstract] = 64`, with the route and date of the
  query. A group is characterised by a measurement, not an adjective.
- **credibility can be *negative* and it travels.** The discovery ledger carries a
  ⚠️ *cautela credibilità* on a specific HIF1α/WWOX branch worked by a group under a serial-
  retraction watch, with the operative consequence spelled out: *do not use that line as
  independent corroboration.* Group context enters as a **constraint on how evidence may be
  combined**, not as a score.
- **retraction status is checked per paper**, dated and routed (`retraction_check.at`,
  `.route`, `.result`, `.hold`) — `SOURCE_INTEGRITY` in the failure taxonomy.

🔴 **Gap:** the persistent knowledge base the manual names (`researchers.md`) **does not exist in
this edition**; the discovery ledger refers to it as *"research-group knowledge base (not
published)"*. The obligation is enforced per-manifest; the accumulation across papers is not
public, so a new Scientist cannot inherit it.

## 1.2 · Phase 2 — Surface preflight, before anything is opened (area 1)

`deep_dive_manual.md` § 4bis: *"**Prima di leggere una riga**, cerca la superficie strutturata, e
registra l'esito in entrambi i casi."*

The rule it operationalises is `gold_is_in_the_details.md` 5d: **prefer XML/HTML PMC over the PDF,
always, and record the absence.** The manual's own diagnosis of why the rule kept failing is the
useful part: 5d described a *preference* and not a *gesture*, so nobody knew **when** to look, and
the look happened after the PDF was already open — that is, never.

Three routes are interrogated, **all three, every time**, and their disagreement is recorded as
data:

```
oa.fcgi        https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=<PMCID>
Europe PMC     https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML
efetch         https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<PMCID>
```

Because on `PMID 24308844` two of the three said no and `efetch` returned 174 KB of complete
JATS. **An announcement is not a delivery and a refusal is not an absence.**

And two facts that a single check conflates: five corpus entries carry `inPMC: Y` together with
`isOpenAccess: N` — author manuscripts. **The structured surface exists and the paper is not open
access**, and any gate reading one field decides the other one wrongly.

Why it is first and not second: a manifest built against the wrong surface **does not look
wrong**. On 2026-08-10 the extractor fabricated a space at every markup boundary; on
`PMID 24550385` that produced 2 occurrences of `PPXY` instead of 31 and *zero* figure citations
instead of 32. A reader on that surface does not fail — *"sceglie le citazioni che il difetto
lascia passare"*. The evidence is fitted to the instrument, invisibly, by someone doing their
best.

`surface_census.py` derives, per paper, which surface exists and whether it can be trusted, and
writes the split into the queue — because *"Rule 5d's preference was recorded. The absence was
not."*

## 1.3 · Phase 3 — Acquisition, and what a refusal actually means (area 1)

- **Abstract first or full text first?** Neither, as posed. The abstract is used for *triage
  ordering only*, and `gold_is_in_the_details.md` rule 8 is unusually blunt about the hazard:
  *"Un abstract non è una lettura"*, and a local abstract corpus is *"a map, never the
  territory"* — enforced at the append primitive (`corpus_firewall.py`) rather than asserted,
  precisely because hundreds of greppable local abstracts make answering from them **feel** like
  working. `abstract` is not an evidentiary `surface` anywhere in the manifest schema
  (measured: of 1002 locator entries, **0** declare surface `abstract`).
- **When is an abstract insufficient?** Always, for anything that lands. It is sufficient only to
  place a paper in a queue.
- **Retrieval cascade** for full text and for figures separately (`deep_dive_manual.md` § 10bis):
  OA package → Europe PMC `supplementaryFiles` → publisher CDN. Each with its known trap.
- **Inaccessible papers.** The practice distinguishes four states that are routinely conflated:
  *not retrieved by me* / *not retrievable by any route tried* / *not open access* / *not
  present*. Three worked examples:
  - `84b3cd6`: nine figures were waived because *"the article is not open access."* The commit
    that corrects it names the category error in its subject line — **"Not open access
    constrains redistribution, not inspection"**. Images may be held locally, gitignored, with
    hash and recipe recorded and the bytes never committed. **The waiver cost two findings**, and
    the re-read recovered exactly the residual risk the waiver itself had named.
  - `d756b65`: the same waiver, repeated an hour after being refused, cost *"the most
    consequential finding in the paper, in the one figure a repurposing track would reach for."*
  - `PMID42422765_partial_locators.md`: supplementary declared `unavailable` after five failed
    routes — while the files were already in the shared `files/` tree, fetched by another actor.
    `files/` is gitignored, so a worktree cannot see a peer's evidence. The operative rule
    derived: **before declaring anything unavailable, look in the shared `files/`.** And the
    deeper one, stated in the dossier: *"I checked whether **I** could fetch it and recorded the
    answer as a property of the artifact."*
- **When every route is closed**, the paper enters a *different class* and the queue must say so
  — it is not a bad reading, it is a declared one (`PMID 17803050`: no DOI, no PMCID, no open
  deposit, and *the fact that this is declared* is what makes the difference).
- **Paywalled but held**: rule 5e. The reading proceeds on the rendered page; what gets published
  is the **recipe** (source digest, page, crop rectangle in PDF points, dpi, image SHA-256) and
  `regenerate_adjudications.py` reproduces identical bytes from the reader's own copy. Three
  papers currently have such adjudications, each carrying an explicit `rights` block with
  `redistribution: NOT_REDISTRIBUTED` and a reasoned `why`.

**How the deep-analysis decision is actually made.** Not by score. `gold_is_in_the_details.md`
rule 1: no tier, score or category authorises *not* reading; `background`, `Tier C`,
`out_of_scope_likely` mean **"later in the queue", never "never"**. Rule 2: *"If a ranking ends up
discarding a study, the ranking is broken — fix the ranking, don't lose the study."* Depth is
escalated (§ 6.2) when the paper is WWOX-direct, model-shifting, claim-shifting, safety-relevant,
or opens a research line — and the escalation criterion is stated as a question about the system,
not about the paper: *"capire cosa il paper permette di vedere che prima il sistema non vedeva
bene."*

## 1.4 · Phase 4 — Declare the reading budget before spending it (area 3)

`deep_dive_manual.md` § 4ter, and it is the sharpest piece of self-knowledge in the repository:

> `coverage.figures: read` senza un solo locator su una figura **non regge**. È la casella più
> facile da spuntare e la più difficile da contestare a posteriori, perché nulla nel record dice
> quante figure c'erano.

So: **every main figure receives a locator or a named waiver**, and — the load-bearing sentence —
**the denominator is panels, not the reader**:

> *Pannelli coperti su pannelli presenti*, con `figures_present` derivato dalle didascalie — un
> rapporto `figure per paper` misura quanto è stato letto **diviso quanto quel lettore ha deciso
> di guardare**, che è una misura di sé stessi.

No fixed threshold is written down, deliberately: *"una soglia ricordata da una persona è una
soglia che si aggiorna per far tornare il verde."*

Resolution is part of the budget, not an afterthought. `figure_ppi_preflight.py` inventories a
PDF's raster ceiling **before** rendering; the resolution actually read goes into the locator's
`anchor` with native dimensions. Because the CDN serves 760 px where the authors deposited 1397,
and on a statistics panel that is *"la differenza fra leggere un asterisco e indovinarlo"* — and
a guessed asterisk is the exact error class that on 2026-08-06 sat between **"not significant"**
and **"not tested"**.

## 1.5 · Phase 5 — The two passes (area 5)

`deep_dive_manual.md` § 6.3.2, `DUE PASSATE`:

1. **Vertical, neutral** — the paper in itself, with epistemic tags and anchors, *without yet
   looking at LEGEND state*. Explicitly to avoid contamination.
2. **Horizontal** — only afterwards: dedup, claim/meta/working-model impact, wikilinks, tensions.

This is not aspirational. `PMID34831305_observation_freeze.md` is a **hashed, timestamped
observation freeze**: twelve neutral observations recorded at `07:43Z`, SHA-256'd, and only then
was the named pattern ("the comparison that matters is not drawn") put to the reader, adjudicated
at `08:02Z`. The verdict was **negative** — *"No valid third occurrence"* — and the method note
records the residual contamination risk that could not be removed (*"Prior conversational
knowledge could not be erased"*).

That is the practice at its best: **a procedure designed so that the expected answer can lose.**

The questions the vertical pass answers are not "what are the conclusions":

- what question is this paper answering, and is it the question I came with? On `PMID 25012504`
  the assignment reframed it — *"not 'is HIF1alpha on the partner list' but does it carry the
  PXPPXYY motif and with what affinity"* — and the finding was that **the paper does not ask**:
  `"PPXY"` does not occur in it (`848db6e`);
- which experiment supports which conclusion, one at a time (`9b0cf47`: *"Each of CLAIM 023's
  four clauses is faithful to the paper; I checked them one at a time"*);
- which sentence carries the real message, and where the hedging lives. On `PMID 15070730` the
  modal verb **dies inside the paper**: Results say *"suggesting that phosphorylation enhances
  this interaction"*, Discussion says *"demonstrated"*, figure title and abstract are flat.

**Paper summary versus LEGEND reconstruction.** The manual names the failure mode:
*"AMMINISTRAZIONE MASCHERATA DA ANALISI"* — output that is orderly and empty — and § 12 makes
the final check a question to oneself: *"Sto facendo il lavoro di un ricercatore esperto o sto
catalogando uno studio?"* A summary reproduces the authors' emphasis. A reconstruction
re-derives what the experiments support, in the system's own vocabulary, and is allowed to
disagree with the abstract.

## 1.6 · Phase 6 — Primary evidence extraction (area 2)

What a valuable mechanistic observation has, that a generic statement lacks — as the practice
enforces it:

| Dimension | Enforced where |
|---|---|
| the acting enzyme/process, the substrate whose abundance or half-life changes, the **sign**, and any modulator | `legend-deepdive` **directed-mechanism gate**: never compress `A antagonizes E3-mediated degradation of B` into `E3 stabilization` |
| the **preparation** the number was measured in | `FT-064` predicate (below) |
| the **regime** — endogenous vs overexpression | `d756b65`: *"Every rescue in the paper runs at 23 to 32 fold overexpression — readable only in the left sub-panels of Figures 3b, 4d and 4e"* |
| the **species and developmental stage** | `trace_claim_foundation.py`, built after two citation hops converted an explicit negative about a **rat** into a positive assertion about a **mouse**, carried on five canonical surfaces |
| the **dose and its plausibility against an independent source** | `848db6e`: the legend prints *"Digoxin (100 mg/1 kg weight)"*; the paper's own cited source used ~1 mg/kg/day — **a hundredfold** |
| the **timescale against the proposed mechanism** | `d756b65`: glucose read at 40 minutes, offered as HIF1α-synthesis inhibition, which requires existing protein lost and target gene products decayed — hours. *"Timescale and dose point the same way."* |
| what the control actually validates | `CONTROL_SPECIFICITY_RULE`, `CONTROL_TOPOLOGY_CHECK` |
| whether the mutation used can separate the hypotheses | `848db6e`: WW1-dependence rests on `W44F/P47A` — the mutation the biophysics describes as abolishing binding to **all** partners, *"so it cannot separate a direct contact from a bridged one"* |

Methods are not a formality. They are read for the things that change the weight of the whole
paper, and the `PMID 42422765` dossier's Methods section is the model: injection technique
changed between the two papers of the same lab (free-hand → stereotaxic); anaesthesia changed, so
a previously recorded caveat **does not transfer**; blinding weakened from unconditional to
*"when feasible"*; and three authors are employed by the company that funded the study, where the
2021 paper declared none. Each is recorded as a fact the reader is entitled to, *invalidating
nothing*.

`PDF_PAGE_COUNT_RECONCILIATION_GATE`: page counts from `file`, PDF metadata, viewer or landing
page are **not** coverage evidence. Open the document with the same parser used for the reading,
record `len(document)`, reconcile every divergence before the receipt. Worked instance:
`file` reported 11 pages where PyMuPDF enumerated 27; *"the discrepancy is recorded rather than
silently resolved from file metadata."*

## 1.7 · Phase 7 — Figures and tables (area 3)

**The figure is a separate evidentiary surface, never read through a text conversion**
(rule 5c). And it is not optional: among the **63** complete-read events in the ledger,
`coverage.figures` is `read` in **63 of 63**. `captions_only` exists and **downgrades the receipt
to partial** — because a caption is not its figure.

That distinction was paid for. On 2026-07-26, Wang 2012 (`PMID 22193544`) describes its
Supplementary Figure A — in the main text **and** in the published legend — as the co-IP proving
*"WWOX does not associate with Tau"*, while the image contains **no Tau blot at all**. Text and
caption agreed with each other and both were wrong; only opening the image could catch it. Had
the caption been trusted, LEGEND would have registered a false contradiction against a live
mechanism (`D-14`).

**How often the figure changes the interpretation — measured, with its denominator.** Every
locator carries a `panel_text_relation`. Across 1002 entries:

| `panel_text_relation` | entries |
|---|---|
| `text_only` | 417 |
| `panel_only` | 148 |
| `text_confirmed_by_panel` | 128 |
| **`text_contradicted_by_panel`** | **47** |
| `panel_qualifies_text` | 32 |
| *(untagged — legacy)* | 230 |

**21 of the 57 papers that carry at least one figure-surface locator contain at least one
locator where the panel contradicts the running text.** That is the empirical case for the whole
figure discipline, and it is a property of the literature, not of one paper.

Worked instances, by experiment type:

- **Dose–response / rescue** — `PMID 42422765` Fig. 3B: the paper says *"dose-dependent"*,
  *"graded improvement"*, *"a clear dose-response relationship"*. The panel shows the low dose
  reaching **zero survival at ~90 days** while the high dose plateaus at ~80% to 300 days. All
  three phrases are true and all three describe a continuum; the curve shows a **threshold**.
  *"A reader who never opens panel B will carry 'more dose, more benefit' instead of 'below
  threshold, no survival at all' — and those two beliefs recommend different trials."*
- **Genotype comparison** — same paper, Fig. 6: panels C/D/E carry all quantification and contain
  **only WT and KO**; panel F contains the treated animals and carries no statistics at all.
- **Pharmacology** — `PMID 25012504` panel 5c: digoxin moves **both** arms, KO up ~10→118 mg/dl
  and **wild type down ~105→72**, while the text says the increase was *"specifically in KO
  mice"* (`d756b65`).
- **Microscopy** — `PMID 42422765` Fig. 1M: the MBP-driven vector *"barely produced detectable
  WWOX at all"*, which converts the authors' polite caveat about tropism into an observation and
  keeps the oligodendrocyte question **open** rather than answered.
- **Electrophysiology / statistics** — Fig. 7C prints `0.2000` above a bracket with no asterisk
  **and without the word `ns`**. *"A number floating above a bracket reads as a result; this one
  is a non-result."* The text calls it significant.
- **Blots** — Fig. 5J: hippocampal protein 9–19× over wild type, and the KO lane reads `1.1`
  where it reads `0.02–0.08` in three other regions. Recorded as a probable non-specific band or
  normalisation artefact, *"not flagged in the figure and not mentioned in the text"*, and
  explicitly noted as **not changing the paper's conclusions** — the kind of internal
  inconsistency a reader quoting hippocampal fold-change would carry forward unknowingly.
- **Tables** — `FTR-20260814-20530675-01`: Figure 5 is titled *"Inverse association of WWOX and
  RUNX2 expression in osteosarcoma"* and the Results two paragraphs later say the inverse
  association *"was not evident when paired comparisons were performed on the 56 available
  cases"*; the printed numbers run the other way. **The paper prints its own refutation of its
  own figure title.**

Three procedural rules that come from figure work specifically:

1. 🔴 **A figure is not read until its caption is read**, and a cross-figure comparison is not
   valid until both captions have been checked for identical construct, dose and units. Derived
   the hard way: *twice on one paper* a criticism was built from panels read without captions,
   both times in the direction of finding a defect. The dossier records the diagnosis —
   *"Panels carry numbers; captions carry what the numbers are of"* — and the audit result:
   **every claim that died was a cross-figure inference; every one that survived rested on a
   single figure with its caption.**
2. **Verify the download.** `md5 -q <dir>/*.png | sort -u | wc -l` must equal the number of
   figures, and `file -b` must never say "HTML document". Twice in one day a loop produced seven
   identically-sized HTML error pages that would have been fingerprinted and declared as figures.
   *"Digest tutti uguali = nessuna figura scaricata."*
3. **Measure every retrieval route and take the best**, because which route wins is not stable:
   on `PMID 34747138` the article PDF held 200 ppi against the OA bundle's 100; on
   `PMID 42422765` every PDF route is closed and a 104 ppi CDN copy is all there is.
   `caption_census.py` adds the companion hazard: on 7 of 34 parseable XML surfaces **every**
   `<fig>` element sits outside `<body>`, so an extractor scoped to `<body>` shows no caption at
   all, raises no error, and returns text that reads as complete.

## 1.8 · Phase 8 — Verbatim and locators (area 4)

**Capture the verbatim locator while the document is open.** Mandatory since 2026-08-04, when an
export found that **no verbatim locator existed anywhere in the canonical state**, across every
complete read in the ledger — fourteen had to be recovered by reopening papers already read.

> *Catturare la frase mentre il documento è aperto costa secondi; recuperarla dopo costa la
> lettura una seconda volta.*

A locator is four fields plus its binding:

| field | content | failure it prevents |
|---|---|---|
| `proposition` | what the quote is evidence **for** — *"se non lo sai dire, la citazione è decorativa"* | a quote that supports nothing |
| `snippet` | verbatim, ≥30 contiguous characters | reconstruction |
| `anchor` | section / figure / table, **plus the resolution read at** | an unlocatable or unreproducible claim |
| `surface` | `body` / `figure` / `table` / `supplement` — **never `abstract`** | abstract material entering as evidence |
| `artifact` | repository-relative path + `kind` + SHA-256 | a quote bound to nothing |

**What makes a locator reliable is the artifact it is matched against, not the care of the
reader.** Rule 5c: a model that converts a PDF to Markdown *reconstructs* — normalises, reflows,
occasionally paraphrases — and a quote checked against that output can pass while matching **the
reconstruction and not the paper**. *"That is the worst class of false positive this system can
produce, because it is silent and wears the badge of having been checked."* ML converters are
legitimate reading aids and **must never be declared as the artifact behind a locator**.

Two measured consequences:

- `locator_audit.py`, run 2026-08-10, found **5 of 22** locators on `PMID 32000863` that did not
  occur in its own XML — all transcribed *as the page reads* rather than extracted *as the
  artifact contains*: lost superscript spacing, lost figure numbers, vanished citation markers.
- `recapture_snippets.py`: when the extractor was fixed, **16 of 54** snippets stopped verifying
  — correctly, because they had stopped being the author's characters. A repair inherits the
  correctness of the tool it was verified against.

**Figure locators are attestations, not verified quotes**, and must be declared as such
(`UNVERIFIABLE_SURFACE` in the blind audit). They bind to the inspected image hash.

**Waiving is legitimate; silence is not.** A reading that supports no proposition waives the
section with an argument of ≥40 characters, and the waiver surfaces as `[DECLARED GAP]` in
`session_self_eval.py`.

The forward-looking reason, which the manual says matters more than the historical one: the
DisMech export **cannot emit a proposition without the sentence that supports it**. A reading done
today without locators is a reading that must be **redone** before it can be exported — a debt
proportional to the work done.

🔴 **The unguarded surface:** `dossier_quote_audit.py` exists because a manifest is the only place
a quote is bound to a fingerprinted artifact, while the **dossier** — the prose written while the
paper was open — carries quotations with no artifact, no surface and no fingerprint. They are
load-bearing and, until promoted into a manifest, unexamined.

## 1.9 · Phase 9 — Evidence, author interpretation, LEGEND interpretation (area 6)

The three-way separation the task names is present, and it is carried by **structure**, not by
prose discipline:

- **(A) Direct observation** → a locator with `surface: figure|body|table` and a verbatim
  snippet. *"EPSC amplitude increased"* lives here, with its panel and its resolution.
- **(B) Author interpretation** → also a locator, tagged by its relation to the panels
  (`text_confirmed_by_panel`, `panel_qualifies_text`, `text_contradicted_by_panel`). This is the
  key design choice: **the authors' sentence is recorded as evidence of what the authors said,
  never as evidence of what happened**, and its relation to the data is a machine-readable
  field.
- **(C) LEGEND interpretation** → `DATO` / `INFERENZA` / `IPOTESI` / `ESPANSIONE`, in the dossier,
  the discovery ledger and the commit candidate — never in the same slot as (A) or (B).

Worked example of all three on one result (`PMID 42422765`, Fig. 4):

> **(A)** open-field velocity WT ≈9.5 → treated ≈11.5, `*`; total distance ≈3400 → ≈4300, `*`;
> rotarod latency ≈85 s → ≈145 s, `*`; four anxiety measures `ns`.
> **(B)** the section is titled *"Neuronal WWOX restoration normalizes neurobehavioral
> function"*, and the running text states *"no significant differences between groups (Figures
> 4B, 4D–4G)"* for panels that carry `*`.
> **(C)** *"A significant difference from wild type is not normalisation, and its direction does
> not change that."* Three readings stay open — hyperactivity, overexpression overshoot, or
> marginal statistics (eight comparisons in one figure, no declared multiplicity correction, all
> three positives at the weakest level) — **and the reading does not choose**. The defensible
> statement is written out: anxiety-related behaviour indistinguishable from WT on four measures;
> locomotor and rotarod marked significant, in the direction of *more*.

Three habits make the separation hold:

1. **The vocabulary is audited separately from the data.** *"'Near significant' is not a
   state."* The dossier records three distinct ways a non-significant result was presented as
   almost-something in a single paper: an unmarked printed P, a comparison not drawn, an explicit
   softening in a caption. *"All three are legitimate authorial choices; none of them may be
   carried into this state as support."*
2. **Chain of custody is checked separately from correctness.** `9b0cf47`: every clause of
   CLAIM 023 was faithful to the paper, and the source pointer was a placeholder naming no
   paper. *"What is absent is the chain of custody. A misreading would have been easier to
   find."*
3. **Blind adversarial audit** at the boundary where interpretation becomes canonical
   (`legend-locator-audit`). The auditor gets only `(proposition, quote, anchor)` triples and the
   source — **never the dossier, the reader's identity, or the conclusions** — and answers two
   mechanical questions: does *this sentence* carry *this claim*, and does the source say **more
   or less** than the proposition. Verdicts: `SUPPORTED` / `OVERSHOOT` / `UNDERSHOOT` /
   `NOT_IN_SOURCE` / `UNVERIFIABLE_SURFACE`. It is mandatory only where the stakes are canonical,
   with the reason stated: *"A gate that fires on everything is a gate that gets switched off."*
   Blindness is the active ingredient — two informed reviewers passed the same pipeline back and
   forth twice; a reviewer who did not know who wrote what found eight more defects in an hour.

## 1.10 · Phase 10 — From observation to mechanism (area 7)

The rule is negative first: **do not build causal chains that were not measured.** The machinery:

- **The four levels**, with the ban stated in both directions: never inferences as data, never
  extensions or hypotheses as robust inferences.
- **`PREMISE_TAG`** — every rejection *and every non-trivial conclusion* must **name** its
  load-bearing premise and tag it `DATO` / `INFERENZA` / 🔴 `DEFAULT_FROM_TEXTBOOK`. And a
  `DEFAULT_FROM_TEXTBOOK` *"is not a foundation: it is a research target"*; a conclusion resting
  on one is **provisional by construction**.
- **The `DEFAULTS THAT BIT US` table**, consulted before discarding anything: polyUb → proteasome
  (linkage and context matter); misfolded → ERAD/4-PBA rescue (the route must be measured); *"it
  is a chaperone" → it helps* (a chaperone can escort a client to degradation); stabilise →
  restore function (*"stable but inert" is a demonstrated phenotype*).
- **79 learned gates**, each a real observed failure converted into a decision rule. The
  mechanism-relevant ones read as a checklist for exactly this phase:
  `MECHANISM_TRANSFER_FIREWALL` (a causal edge crossing variants/models/systems remains a
  **bridge hypothesis** until measured in the target), `MECHANISM_DIRECTNESS_GATE` (marker +
  phenotype is not an unmeasured intermediate), `TARGET_ATTRIBUTION_GATE` (a pharmacological
  rescue does not identify the target), `PROTEIN_STATE_IDENTITY_GATE` (abundance ≠ function),
  `DEGRADATION_DIRECTION_GATE` (name the direction), `STIMULUS_CONDITIONAL_RESCUE_GATE`,
  `STAGE_MATCHED_COMPARATOR_GATE`, `SYNTHESIS_MEDIATION_GATE` (a review combining separately true
  observations into a **new arrow** is not a datum), `KG_EDGE_HAS_NO_SIGN`.
- **The founding case of the whole discipline**, from `gold_is_in_the_details.md`: a thyroid-
  cancer paper filed Tier C carried the degradation biology of an SDR missense variant —
  **P252A, and not Q230P** — normal mRNA, accelerated turnover, no rescue with MG-132, rescue
  with lysosomal probes, HSC70 co-IP, LAMP1 colocalisation. The method consequence was decisive:
  a degradation assay limited to the proteasome cannot exclude other routes, so a negative there
  risks being a **false negative** rather than an uninformative result. It forced separating
  **synthesis, solubility, turnover, route and function** as distinct questions. *And the
  subsequent transfer of that route to Q230P → CMA was itself corrected on audit.* The case
  demonstrates **both** the value of cross-context reading **and** the risk of mechanistic
  over-transfer, and the repository keeps both halves.

**How the four verdicts are actually assigned**, as the discovery ledger shows them
(`DL-BIO-002`): *"**ALTO** sul disrupt dell'accettore (SpliceAI DS_AL 0.96 + MaxEntScan Δ−7.95,
2 metodi ortogonali); **medio** sull'esito"*. Belief is **decomposed per link of the chain**, not
assigned to the conclusion — and the demonstrated / probable / speculative boundary falls
*inside* one causal statement, not between statements.

- **demonstrated** — measured in the system being claimed about, on a surface that was inspected;
- **probable** — convergent, orthogonal methods on the same link (two independent predictors; a
  metabolic observation supported by uptake + lactate + Seahorse + ATP + NADH + an independent
  metabolite panel);
- **speculative** — the link exists in another preparation, variant, species or stage;
- **requires further experiment** — and the practice **names the experiment**. `PMID 42422765`:
  *"an intermediate dose arm between 1.23 and 2.63 × 10¹¹ vg would locate the threshold and is
  the single most informative experiment this paper implies."*

## 1.11 · Phase 11 — Negatives, limits and the things nobody drew (area 10)

This is where the practice is furthest from ordinary literature work, and it rests on one
asymmetry:

> a **false positive** gets tested and dies. A **false negative** is silent, permanent and
> self-reinforcing. In a system that compounds, *"a false positive is a cost; a false negative is
> a compounding loss."* And tiers, gates, filters, `refuted` and *"do not assume that…"* are
> **all machinery that produces negatives**.

Hence: **every rejection is recorded with a `REVIVAL_TRIGGER`** — what evidence would reopen it —
in one named destination (`dismissal_ledger_current.md`), because *"a rejection recorded anywhere
else is a rejection nobody will re-scan"*. And the **re-audit rule**: every time a new mechanistic
`DATO` arrives, re-scan the dismissal ledger for rejections whose premise it touches. *"Without
this step you have self-correction, not self-improvement."*

What the Scientist actively looks for:

- **Missing controls and undrawn comparisons.** The distinction that matters is between *tested
  and found absent* and *never tested*: `ns` is absence of detected difference, **not
  equivalence**; a comparison the figure does not draw is not a negative result. On `S8`:
  *"There is **no drawn treated-vs-KO comparison** … `ns` is absence of detected difference, not
  an equivalence test."*
- **Alternative explanations for a failure.** *"A failed rescue by a vector with poor tropism for
  the target cell is not evidence that the target cell does not matter."*
- **The negative caused by the model rather than by the biology.** The best worked example in the
  corpus, and the dossier says so explicitly: the therapeutic window beyond P5 is unmeasured
  *because Wwox-null mice die*, not because therapy fails. *"A system that files 'window =
  P0–P5' as a fact would have manufactured a false negative of exactly the kind
  `epistemic_discipline` describes."* The correct entry: **efficacy demonstrated P0–P5; upper
  bound unknown and unmeasurable in this model.**
- **Species and preparation differences**, as a standing predicate rather than a caveat.
  `FT-064` is a *written-out search predicate* left in the queue for whoever takes it:
  > a paper is an instance if it **measures the same quantity in a tissue preparation and in an
  > autonomous cell preparation**, calls them **by the same name**, and the two have **opposite
  > sign** — or the same sign but the conclusion cites only one.
  Two known instances calibrate it (`Runx2` bone in vivo **+50%** vs calvarial osteoblasts
  **−70%**, with the Discussion's summary sentence carrying the wrong sign; an organoid metabolic
  signature confounded with a differentiation defect, declared in a figure title and not in the
  conclusion). The generalised question is then asked of **every** node of the therapeutic
  portfolio: *"Su quale preparazione si misura l'endpoint, e quel readout ha lo stesso segno del
  bersaglio terapeutico?"*
- **Overinterpretation**, including one's own. The `PMID 42422765` dossier contains two
  self-corrections, one **withdrawal of a withdrawal**, and a statement of the failure mode:
  *"I had retracted a true statement because I mistook my own inability to retrieve for the
  absence of evidence."* Corrections are **struck, not deleted** — *"Struck rather than deleted:
  what it cost to reach is the reason the retrieval rule above exists."*
- **Reading debt**, partitioned and never rounded off. `READING_DEBT_PARTITION_GATE` refuses a
  single residual count. The `PMID 42422765` record enumerates 35 unknown PMIDs out of 73 with a
  PMID — 48% of the bibliography — and declines to triage them, on the grounds that *"enumeration
  is not classification"*.
- **Merges never choose between two readings.** `reading_state.py` exists because two actors read
  the same paper in parallel and both legitimately continued the same earlier receipt; taking
  either side silently erases the other's work *in the list that exists to record what has not
  been read*, where an erasure survives longest. **Sum, never choose.** And the sum is a *view*,
  not a receipt, because a receipt signed by a merge process would be *"a fabricated
  attestation"*.

## 1.12 · Phase 12 — Ranking papers (area 8)

The ranking axes are **two, orthogonal, never collapsed** (`deep_dive_manual.md` § 6.3.1):

- **TYPE** → evidential strength. A review **corroborates baselines, it does not create `DATO`**;
  a preprint is `observation` until peer-reviewed;
- **RECENCY** → importance and currency. *"NON declassare uno studio perché recente. 'Nuovo non è
  migliore, ma nuovo è nuovo'"* — a recent paper starts from the best of the prior work and adds,
  so it can be the **FRONTIER**. Recency raises **priority and inferential ambition**, never
  certainty. Where a recent paper conflicts with an old baseline, weigh method and replication —
  *"non deferire d'ufficio al vecchio"*.

And the superordinate rule that overrides every score: **no hierarchy of importance among
studies; no study that "does not deserve" to be read.** `gold_is_in_the_details.md` inverts the
intuitive ordering explicitly:

- 🧬 **oncology** — often *decades ahead* on folding, stability, degradation routes, partners,
  localisation, rescue. For a tumour-suppressor gene, the biology needed to interrogate an allele
  may live there, more than in case reports;
- 🧠 **adult neurology** — shared pathways, proteostasis, biomarkers, endpoints, human-tested
  drugs;
- 📋 **syndrome case reports** — most phenotype-consistent, largely descriptive. *"Consistency ≠
  usefulness"*;
- 🐄 **"noise"** — still material to squeeze for a method, an assay, a partner, a heuristic.

**How non-WOREE oncology is handled**, concretely: it is read at full depth for mechanism, and
firewalled at transfer. The mechanism is extracted; the transfer is declared on three axes —
genotype, model, developmental stage (§ 6.3.5) — and remains a bridge hypothesis until measured
in the target system. The P252A case is both the reason to read oncology *and* the reason the
firewall exists.

Independent replication is treated as a claim about **lineage**, not about count:
`EVIDENCE_REUSE_GATE` fires when a review, a reused cohort or a same-lineage publication *appears*
to replicate a finding; `CROSS_LINE_REPLICATION_GATE` when different cell lines are pooled as
replicates; `SYNTHETIC_REPLICATE_GATE` when bootstrap or augmentation inflates apparent n. And
`PMID 25491415`'s dossier applies it: the review's HIF1α/glucose account *"is a secondary
synthesis of PMID 25012504, not independent support"*.

**What makes a study valuable for LEGEND** — the actionability contract (`LEGEND_CORE.md` § 1.1).
Every claim declares `therapeutic_relevance`, `beneficiary_scope`, `lever`,
`next_decisive_experiment_or_decision`, `what_changes_if_true`. If it changes no lever,
experiment, decision, safety, monitoring or access, it stays `none_background` — *kept for
completeness and as a guardrail*, but it may not occupy P0/P1, generate a Working Model headline
on its own, or drive a clinical-strategic choice. Note the shape: the low verdict constrains
**priority**, and never authorises discarding.

## 1.13 · Phase 13 — Brainstorming, and the wall that keeps it separate (area 11)

`deep_dive_manual.md` § 10 forbids the opposite error too: *"È vietato essere eccessivamente
conservativi … rifugiarsi in output prudenti ma sterili."* Generation is **mandatory**
(§ 7.9 Research Expansion, § 7.10 Strategy Space, § 8.1 hidden-message extraction), with the
obligatory question:

> *"Se questo paper fosse letto da un ricercatore molto esperto, quale messaggio importante
> potrebbe vedere che il lettore standard perderebbe?"*

Separation is achieved by **destination**, not by tone. The five things the task asks to keep
apart live in five different files with different write rules:

| What | Where it lands | Write rule |
|---|---|---|
| what the study demonstrates | manifest locators + dossier | verbatim, artifact-bound, validator-gated |
| what emerges as a question | `full_text_queue_current.md` (`FT-###`) | with a **written-out predicate**, so the next reader searches rather than reconstructs |
| possible experiments | discovery ledger `Esperimento proposto` + `REVIVAL_TRIGGER` | names the readout and whether it is feasible |
| therapeutic implications | `therapeutic_hypotheses_ledger_current.md` | labelled `supporto di razionale` / `candidate idea` / `repurposing hypothesis` / `non-operational hypothesis` |
| LEGEND hypotheses | `discovery_ledger_current.md` | `IPOTESI`/`ESPANSIONE`, append-only on leads, status never deletion |

**None of these is canonical.** Promotion to the four current files happens only through a
`COMMIT CANDIDATE` and a `BATCH_COMMIT` — *"Current files are never updated during a deep dive."*

The discovery-ledger entry format is itself the discipline: `Status` · `Tag` · what is measured ·
matrix · proximity to the gene · source · **ABC map** (A = the loss, B = the mechanism, C = the
measurable readout) · a **causal statement written as signed edges** (`Q230P
—predicted_destabilizes→ WWOX_SDR_fold`) · **belief, graded per edge** · reasoning chain ·
evidence *supports / refutes / neutral* · proposed experiment with expected readout and
feasibility · transfer rationale · novelty · disease relevance · interconnections. Leads are
**never deleted, only re-statused** (`open · maturing · promoted-to-CC · parked · refuted`), and
several entries carry a *"Riflessione di processo"* — what reading this taught about reading.

And the cross-domain expansion has a hard traceability condition (§ 9): every expansion must trace
back `pathway → WWOX claim → originating paper`. *"Se la tracciabilità si perde, l'espansione non
è valida."*

## 1.14 · Phase 14 — Landing, and the diagnosis that must precede the good news

- **`READING_MUST_LAND_GATE`** — a full text recorded as completely read must have produced
  something durable. The `landing` array is present in all 64 manifests.
- **`FULLTEXT_READ_RECEIPT`**, persisted by the calling session *before* reporting the paper as
  read, with a nine-key coverage map (Abstract, Introduction, Methods, Results, Figures, Tables,
  Discussion, Limitations, Supplementary; `references` optional and ratcheting). A complete
  receipt **may not contain `not_read`** — measured: among the 63 complete-read events,
  `supplementary` is `not_present` 30×, `read` 23×, `unavailable` 10×, and **`not_read` 0×**.
- **Post-batch self-diagnosis before takeaways** (`LEGEND_CORE.md` § 6.1), in this order:
  executable checks → **written judgement diagnosis** → a proportional micro-upgrade or an
  explicitly owned blocking debt. *"A summary is not a diagnosis. Takeaways may report a clean
  close only after the executable part passes."* And `SELF_ASSESSMENT_IS_NOT_EVIDENCE_GATE`
  guards the obvious hole in that.
- **The one judgement no gate makes**: before any push to a public remote, read
  `git diff origin/main..main --stat -- disease-models/` yourself. *"`public_release_gate.py`
  looks for patient re-identification and does it well; copyright is outside its domain"*, and
  publishing is not reversible.

---

# PART 2 — Hidden rules

Operational rules that recur across the artifacts, stated in the form the practice actually uses.
Each is attested by at least one worked instance in this repository.

### Acquisition and surface

**Rule 1 — Look for what you already hold before you look for what is new.**
*Why it matters:* the corpus generates false negatives faster than the literature generates
papers, and an unread paper in the corpus is invisible in exactly the way a missing paper is not.
*Example:* FM-011 — a Tier A / Relevance HIGH placeholder held the experimental datum LEGEND then
re-derived in silico from scratch (`unread_gold.py`).

**Rule 2 — Find the structured surface before opening anything, and record the absence as loudly
as the presence.**
*Why:* a manifest built on the wrong surface does not look wrong, and the reader adapts the
evidence to the defect without noticing.
*Example:* the space-fabricating extractor turned 31 `PPXY` occurrences into 2 and 32 figure
citations into 0 on `PMID 24550385`.

**Rule 3 — Query all three PMC routes and record the disagreement.**
*Why:* an announcement is not a delivery and a refusal is not an absence.
*Example:* `PMID 24308844` — `oa.fcgi` says non-OA, Europe PMC 404s, `efetch` returns 174 KB of
complete JATS.

**Rule 4 — "Not open access" constrains redistribution, not inspection.**
*Why:* the conflation silently converts a licensing fact into a reading gap, and reading gaps
cost findings.
*Example:* `84b3cd6` — nine figures waived on that reasoning; the re-read recovered exactly the
residual risk the waiver had named, twice in two papers.

**Rule 5 — Before declaring anything unavailable, check whether it is a property of the artifact
or a property of you.**
*Why:* `files/` is gitignored, so a worktree cannot see a peer's evidence; five failed routes of
your own prove nothing about the object.
*Example:* `mmc1.pdf` / `mmc2.pdf` were in the shared tree at 12:13 and declared unavailable at
13:26.

### Reading

**Rule 6 — Two passes, vertical then horizontal, and the vertical one does not look at LEGEND.**
*Why:* knowing what the system expects changes what a reader sees, and the change is invisible
from the inside.
*Example:* the `PMID 34831305` observation freeze — twelve observations hashed at 07:43Z, the
pattern question asked at 08:02Z, verdict **negative**.

**Rule 7 — `grep` is forbidden as a method of analysis.**
*Why:* keyword search decides what a paper says by what the reader already suspected. Permitted
only to locate files, dedup registries, verify IDs, or audit *after* reading.
*Example:* stated in `gold_is_in_the_details.md` rule 4 and repeated in the manual, the skill and
the corpus firewall — three independent enforcement points because a name is not a fact.

**Rule 8 — An abstract is not a reading, and a local abstract corpus is a map, never the
territory.**
*Why:* hundreds of greppable local abstracts make answering from them *feel* like working.
*Example:* enforced at the append primitive and mutation-tested (`corpus_firewall.py`), not merely
stated.

**Rule 9 — Declare the panel budget before spending it, and let the denominator be panels, not
your own choices.**
*Why:* `figures: read` is the easiest box to tick and the hardest to contest afterwards, because
nothing in the record says how many figures there were.
*Example:* `figures_present` derived from captions; a `figures per paper` ratio measures the
reader, not the reading.

**Rule 10 — A figure is not read until its caption is read; a cross-figure comparison is not valid
until both captions are checked for identical construct, dose and units.**
*Why:* panels carry numbers, captions carry what the numbers are *of*.
*Example:* `PMID 42422765` — two criticisms built from caption-less panels, both in the direction
of finding a defect; **every claim that died was a cross-figure inference.**

**Rule 11 — A pattern that has held three times is exactly when the fourth case stops being
examined.**
*Why:* the reader begins finding instances by looking for them.
*Example:* the same dossier, in the author's own words, after naming the failure and then
repeating it two figures later. The remedy that worked was procedural (Rule 10), not
resolutional.

**Rule 12 — Verify that a downloaded figure is a figure.**
*Why:* HTML error pages fingerprint and declare as cleanly as images do.
*Example:* seven identically-sized HTML files, twice in one day. `md5 … | sort -u | wc -l` must
equal the figure count.

### Evidence standard

**Rule 13 — Capture the verbatim locator while the document is open.**
*Why:* seconds now, a second full reading later — and the export cannot emit a proposition
without its sentence.
*Example:* 2026-08-04 — no verbatim locator existed anywhere in the canonical state; fourteen
recovered by reopening two papers.

**Rule 14 — A quote is verified only against deterministically extracted text from a fingerprinted
artifact; an ML conversion is a reading aid and never the declared artifact.**
*Why:* a quote checked against a reconstruction passes while matching a sentence nobody wrote —
a false positive wearing the badge of having been checked.
*Example:* `PMID 32000863` — 5 of 22 locators absent from the paper's own XML, all transcribed as
the page reads.

**Rule 15 — A receipt attests reading; it does not attest quotation. They are different facts.**
*Why:* every structural check can pass while the proposition overshoots its sentence.
*Example:* `PMID 30290271` — a dossier recorded *"NPY: whole hippocampus not significant"* where
the paper reports **no statistic at all** for that comparison.

**Rule 16 — A caption is not its figure; `captions_only` downgrades the receipt.**
*Why:* text and caption can agree with each other and both be wrong about the image.
*Example:* Wang 2012 — a co-IP described as proving "WWOX does not associate with Tau" in a panel
containing no Tau blot (`D-14`).

**Rule 17 — Waiving is legitimate; silence is not.**
*Why:* an argued absence is auditable, an unargued one is indistinguishable from an omission.
*Example:* `[DECLARED GAP]` in `session_self_eval.py`; the ≥40-character waiver argument.

### Interpretation

**Rule 18 — Record what the authors said as evidence of what the authors said, and tag its
relation to the panels.**
*Why:* it preserves both facts without letting either stand in for the other.
*Example:* `panel_text_relation` — **47** locators over **21 of 57** figure-inspected papers are
`text_contradicted_by_panel`.

**Rule 19 — `ns` is absence of detected difference, never equivalence; a comparison not drawn is
not a negative result.**
*Why:* the two are the raw material of manufactured false negatives.
*Example:* `S8` panels C/D draw WT-vs-KO and WT-vs-P5 and never treated-vs-KO — so the rescue is
*shown* and never *tested* there.

**Rule 20 — When two readings of a result are open, write both and choose neither.**
*Why:* a premature choice is unfalsifiable downstream; an open pair is a research question.
*Example:* Fig. 4 behavioural overshoot — hyperactivity vs overexpression vs marginal statistics,
*"and this reading does not choose"*.

**Rule 21 — Name the load-bearing premise of every rejection and of every non-trivial conclusion,
and tag it.**
*Why:* the errors all had the form `P → C` where C is a rejection and P was never checked because
P was the obvious part.
*Example:* the `DEFAULTS THAT BIT US` table; a `DEFAULT_FROM_TEXTBOOK` is a research target, not a
foundation.

**Rule 22 — Nothing dies in silence: every rejection carries what would revive it, in one named
place.**
*Why:* a rejection recorded anywhere else is one nobody will re-scan; and every new mechanistic
`DATO` triggers a re-scan.
*Example:* `dismissal_ledger_current.md`; and the trigger that fired — *"a post-natal dosing
experiment in this model would change the reading of the whole paper. It exists, and it is
here."*

**Rule 23 — A causal edge that crosses variant, model, species, stage or preparation is a bridge
hypothesis until measured in the target.**
*Why:* the corpus contains both a discovery that came from cross-context reading and an error
that came from over-transferring it.
*Example:* P252A's lysosomal route — the reason to read oncology, and the transfer to Q230P → CMA
that had to be corrected on audit.

**Rule 24 — Check the dose, the timescale and the preparation against something outside the
paper.**
*Why:* the number a downstream track will reach for first is the one most worth checking.
*Example:* digoxin printed as 100 mg/kg against ~1 mg/kg/day in the paper's own cited source;
40-minute glucose readout for a mechanism that needs hours.

### System behaviour

**Rule 25 — Ranking orders reading; it never authorises not reading. If a ranking discards a
study, the ranking is broken.**
*Why:* every filter is a machine for producing silent negatives.
*Example:* the thyroid-cancer Tier C paper that carried the SDR degradation biology.

**Rule 26 — Sum, never choose, when two readings of the same paper meet.**
*Why:* whichever finished second erases the other, in the list that records what has *not* been
read — where an erasure survives longest.
*Example:* `reading_state.py`; and *"three branches described this one list at three different
moments and none of them was wrong when written."*

**Rule 27 — Corrections are struck, not deleted; and a withdrawal can itself be withdrawn.**
*Why:* what a finding cost to reach is why the rule exists, and deleting it erases the lineage.
*Example:* the S7I retraction, reopened — *"I had retracted a true statement because I mistook my
own inability to retrieve for the absence of evidence."*

**Rule 28 — Enumeration is not classification, and declaring a debt does not pay it.**
*Why:* both feel like progress and neither is.
*Example:* 35 unknown PMIDs of 73 enumerated and explicitly not triaged; a receipt declaring
`complete_fulltext_read` while its 28-item reference list had never been enumerated — and the
list contained a paper that qualified the reading's own inferences.

**Rule 29 — Blind the reviewer.**
*Why:* knowing the author makes a reviewer reconstruct intent instead of testing behaviour.
*Example:* two informed reviewers passed the same pipeline twice; a blind one found eight further
defects in an hour.

**Rule 30 — A gate that fires on everything gets switched off.**
*Why:* the adversarial audit is mandatory only at the canonical boundary precisely so that it
survives.
*Example:* `legend-locator-audit` — mandatory on baseline-touching readings, MAJOR change class,
and rejections that close a research direction; not required elsewhere.

---

# PART 3 — Missing formalization

## 3.1 · Already encoded, and machine-enforced

These do not need a contract to exist; a contract would only make them **owed by a role**.

| Practice | Enforcement |
|---|---|
| Duplicate-work gate before reading | receipt ledger + `reread_reason` (128/128 events) |
| Evidence-depth vocabulary and coverage map | `fulltext_receipts.py`; `not_read` refused in a complete receipt (0/63) |
| Locator schema v2: proposition, ≥30-char snippet, anchor, non-abstract surface, fingerprinted artifact | `deepdive_manifest.py --verify-artifacts --require-current-schema` (60/64 manifests) |
| Text-surface corruption screen; `SUSPECT` refused, never normalised | `deepdive_manifest.py` C0/printable/absence screens |
| Corpus-of-abstracts refusal at three independent points | `corpus_firewall.py` |
| Obligation-without-artifact fields (group, field density, multi-hop, cross-query, retraction) | present in **64/64** manifests |
| Reading must land | `READING_MUST_LAND_GATE` |
| Append-only ledger with hash chain + tail anchor | `fulltext_receipts.py verify` |
| Reading state as a **derived view**, summed across receipts | `reading_state.py` |
| Reading debt with an honest denominator | `coverage_report.py` |
| Claim → species/depth traversal | `trace_claim_foundation.py` |
| Page adjudication as recipe, `crop_contains_span` machine-checked | `regenerate_adjudications.py` |
| Post-batch self-diagnosis reaching the workflow | `SELF_EVALUATION_MUST_REACH_WORKFLOW_GATE`, `session_self_eval.py` |
| Public-release privacy gate | `public_release_gate.py` |

**20 of the 79 learned gates are `ACTIVE_EXECUTABLE`.**

## 3.2 · Partially encoded — the rule exists in prose, the check does not, or the artifact is
absent

| Practice | State of formalization | The specific gap |
|---|---|---|
| **The two passes (vertical neutral → horizontal)** | manual § 6.3.2; **one** hashed observation freeze exists in the whole corpus | no artifact slot, no schema, no trigger. It was done once, well, and by hand |
| **Panel budget / figure denominator** | manual § 4ter states the rule and *deliberately* states no threshold | `figures_present` from captions is described, not derived by a committed script; `caption_census.py` measures a *related* hazard. Open item 1 of `fulltext_read_receipt.md` says outright: *"the figure denominator has no basis, and today it has no schema either"* |
| **Caption-before-panel; cross-figure construct/dose/unit identity** | derived in a dossier, stated as *"the operative rule now"* | not in the manual, not in a gate, not in any validator. It is currently carried by one paragraph in one file |
| **Group analysis knowledge base** | manual § 6.0 mandates reading and updating `researchers.md`; the per-paper `group_assessment` field is enforced | **the KB does not exist in this edition.** Accumulation across papers is not inheritable |
| **Blind locator audit** | full skill, verdict vocabulary, mandatory-trigger list | `LOCATOR_OVERSHOOT_GATE` is `ACTIVE_METHOD`; nothing detects that a reading *should* have been audited and was not |
| **Dossier quotations** | `dossier_quote_audit.py` exists and is *deliberately non-blocking* | quotes in prose dossiers carry no artifact, no surface, no fingerprint — load-bearing and unexamined until promoted |
| **Multi-hop reference enumeration** | `references` is an **optional tenth** coverage key; `session_self_eval.py` reports its absence | optional by construction, because an append-only ledger cannot be retro-fitted. New reads *should* declare it |
| **`REVIVAL_TRIGGER` re-audit loop** | obligation stated; destination named | the re-scan on each new mechanistic `DATO` is a human act with no trigger and no record of having run |
| **Retrieval-route measurement for figures** | derived and written into a dossier as a rule the session *"deliberately did not write"* into `CLAUDE.md` | rule 5d still says only "prefer XML/HTML over PDF" — true for text, and the ranking **inverts** for figures |
| **Actionability contract** | `LEGEND_CORE.md` § 1.1 lists five required fields | not a manifest field; no validator refuses a claim that declares none |

**55 of the 79 gates are `ACTIVE_METHOD`** — i.e. the dominant enforcement mechanism in this
system is *a reader who remembers*. That is the central formalization finding of this document.

## 3.3 · Not formally encoded anywhere

1. **The reading-depth dial.** Nothing states *how deep* a given paper must be read as a function
   of what it is. Escalation criteria exist in prose (§ 6.2); a Scientist deciding between a
   complete read and a targeted one has no contract to point at.
2. **Belief decomposition per causal edge.** The discovery ledger *does* it (`ALTO` on one link,
   `medio` on the next) and no schema requires it. Two entries could grade the conclusion instead
   of the chain and nothing would notice.
3. **Two-readings-open as a first-class outcome.** `INFERENCE_A + INFERENCE_B +
   DISAGREEMENT_UNRESOLVED` is legitimate for *peers* (body § 27); an unresolved pair produced by
   **one** reader has no status vocabulary, so it survives only as prose.
4. **The self-correction record.** The corpus's most valuable artifact — a reader documenting how
   their own method failed, twice, on one paper — has no home. It landed in a dossier because
   there was nowhere else.
5. **What a Scientist owes when the answer is "nothing".** A reading that supports no proposition
   can waive locators; there is no equivalent for a reading whose *scientific* result is that the
   paper adds nothing. The practice records those (`none_background`) without a defined form.
6. **Conflict-of-interest and funding as a recorded field.** Read and reported in prose
   (`"R.I.A. is a consultant for…"`), captured in no schema.
7. **Cross-reader convergence.** Three Scientists exist; nothing defines when two independent
   readings of the same paper count as corroboration versus duplication, or how their coverage
   maps merge beyond `reading_state.py`'s sum.
8. **The `FT-###` predicate as an object.** `FT-064` demonstrates the most transferable technique
   in the corpus — leaving a *written-out search predicate* for whoever takes the entry — and it
   is a prose convention inside one queue file, not a schema.

---

# PART 4 — Proposed Scientist Contract topics

Areas that should become formal requirements. **No contract text is proposed here**, and none of
these should be drafted before the activation state of `roles/scientist.md` is resolved — a
requirement added to a `PROPOSED` contract binds nobody and hides that fact.

**A · Pre-reading obligations**
1. Duplicate-work resolution and the closed list of `reread_reason` values.
2. Surface preflight: three routes, disagreement recorded, absence declared as a class.
3. Research-group assessment: what must be measured, what must be disambiguated, and where the
   accumulation lives.
4. Declared reading and panel budget before the first page.

**B · Reading discipline**
5. The two passes, and what makes the first one auditably neutral (freeze artifact, hash,
   timestamp).
6. Depth tiers: which paper properties oblige a complete read, and what a partial read must name.
7. The ban on keyword search as analysis, and the permitted technical uses.
8. Methods obligations: page reconciliation, blinding, anaesthesia/preparation, funding and
   declared interests.

**C · Evidentiary standard**
9. Locator schema, and the artifact-binding rule for text versus figure surfaces.
10. Caption-before-panel, and cross-figure identity of construct, dose and units.
11. Resolution declaration, and the retrieval-route measurement rule for figures.
12. Waiver form and threshold; what a declared gap must contain.
13. Dossier quotations: whether prose quotes must be promotable, and what audits them.

**D · Epistemic separation**
14. The three-way separation (observation / author interpretation / LEGEND interpretation) as a
    structural requirement, not a stylistic one.
15. `panel_text_relation` as a required field wherever a figure was inspected.
16. Belief graded **per causal edge**, and the vocabulary for demonstrated / probable /
    speculative / requires-experiment.
17. Two-readings-open as a legitimate terminal state for a single reader, with a status name.

**E · Negatives**
18. `PREMISE_TAG` on every rejection and every non-trivial conclusion.
19. `REVIVAL_TRIGGER` with a named destination, and the re-audit loop's trigger and record.
20. The `ns` / not-drawn / not-tested distinction as a required declaration.
21. Reading debt: partitioned, enumerated, and never resolved by rounding.

**F · Adversarial review**
22. When a blind locator audit is mandatory, who may not be the auditor, and what the auditor may
    not see.
23. The verdict vocabulary and the disposition of each verdict before `BATCH_COMMIT`.
24. What a Scientist owes in `AUTHOR_RESPONSE`, given that silence is not acceptance.

**G · Landing and closure**
25. The receipt as a precondition for reporting a paper read, and coverage-map completeness.
26. Which artifacts a reading must produce before it may be called finished.
27. Post-batch self-diagnosis before takeaways, and the micro-upgrade-or-owned-debt rule.
28. Correction discipline: strike, never delete; withdrawals may be withdrawn.

**H · Multi-Scientist coordination**
29. Sum-never-choose on merged coverage, and why the sum may not be a receipt.
30. Evidence locality: where probatory artifacts must be written, and the shared-`files/` check
    before declaring anything unavailable.
31. When two independent readings of one paper constitute corroboration rather than duplication.

**I · The one that is not a rule**
32. The standing obligation that produced everything above: **a reading that discovers a defect in
    its own method must record it where the next reader will meet it.** Every rule in Part 2 exists
    because someone did that. It is the only one that cannot be enforced by a validator, and it is
    the one worth writing down first.

---

## Closing note

The gap this reconstruction found is not a missing practice. The practice is unusually complete —
more complete than its own documentation, and considerably more complete than the tooling that
checks it. The gap is **ownership**: 55 of 79 gates, the two-pass structure, the panel budget, the
caption rule and the re-audit loop are all carried by a reader who remembers, in a system whose
own founding observation is that *what gets discarded silently is what compounds*.

A Scientist contract's job is not to invent this workflow. It is to make it **owed**.

*Not medical advice. This document is a rehearsal product and carries no standing.*
