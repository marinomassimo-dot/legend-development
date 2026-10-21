# Reconciliation of the external drug-repurposing plan with what is measurably here — 2026-10-20

> **What this document is.** A measurement, taken by Harness Engineering (`plan`) on 2026-10-20
> in task `PLAN-REPURPOSING-INTEGRATION-20261020`, of every component, step and asset named by
> the operator-supplied roadmap v4 r14 and its cumulative scout register r20, both of which are
> placed verbatim in this directory. It is **not** a reading record, carries no receipt, makes no
> scientific claim, and changes none of the four scientific current files.
>
> **The one distinction this document exists to enforce:** *adopted in the plan* ≠ *installed* ≠
> *verified to work*. The external deliverables use `ADOTTATO NEL_PIANO` for the first and
> reserve `IMPLEMENTAZIONE_VERIFICATA` for the third; they are explicit that the state of this
> server was `UNKNOWN` to them throughout. This document resolves that `UNKNOWN` by measurement.

Vocabulary used below, one of four per item, and nothing else:

| Verdict | Meaning |
|---|---|
| `PRESENT_AND_RUNNABLE` | the asset is in this repository (or on this host) **and** a command was run here whose output is quoted |
| `PRESENT_NOT_RUNNABLE` | the asset is here but could not be made to produce its output, with the reason named |
| `ABSENT` | not in this repository and not on this host. Absent is not rejected: the plan may still be right about it |
| `NOT_CHECKED` | deliberately not measured, with the reason named (usually: a scientific act reserved to the Scientists, or an act this task forbade) |

---

## 1 · Headline: how much of the plan is real

| | Items | |
|---|---:|---|
| `PRESENT_AND_RUNNABLE` | 11 | the LEGEND-side reuse surfaces, plus the rescue reference, plus the bridge, plus the ClinicalTrials.gov census that landed the same day (§ 4.4) |
| `PRESENT_NOT_RUNNABLE` | 2 | `legend-safety-triage` (its two predictors are not installed), `_external_repos/MANIFEST.md` as a component census (one row measurably overstates its scope) |
| `ABSENT` | 14 | every third-party component the plan names: OptimusKG, Open Targets client, MATRIX, ADMET-AI, medchem, drugfindR, ToolUniverse, MAP, NOCAP-AIVC, NetworkCommons/MOON, Spectrum code, RepurposeAgent, AetherCell, GSE156243 bytes |
| `NOT_CHECKED` | 4 | P3 axis selection, P5 ranking, P6d real inference, P8b delegation comparison — three are scientific acts, one needs an install |

> **Dated as of 2026-10-20, and two rows moved the same day.** The clinical-census actor working
> in parallel landed a ClinicalTrials.gov connector (`91f8e60c`) and corrected the Spectrum
> manifest row (`461bcc28`) after these counts were taken; both changes are folded into § 4.3,
> § 4.4 and § 7 rather than silently rewritten, because a reconciliation whose verdicts drift
> without their date stops being a measurement.

Three sentences, which is the honest summary:

1. **Nothing the plan proposed to install is installed.** `_external_repos/` contains exactly one
   file, `MANIFEST.md`; no third-party repository is vendored and no third-party package of the
   repurposing stack is importable on this host. The plan's own `UNKNOWN` resolves to ABSENT.
2. **Everything the plan proposed to *reuse* exists and runs.** The pathograph, its export, the
   Monarch/DGIdb adapter, the mechanism-intervention map, the four research ledgers and the
   candidate bridge all produced output here today.
3. **On one item reality is far ahead of the plan.** The `WOREE_RESCUE_REFERENCE` the plan asks
   P3 to build out of an abstract is, in this repository, a read paper: PMID 42422765 carries
   **twelve** receipts including one `complete_fulltext_read` with 29 locators, a deep-dive
   manifest, a 55 KB locator dossier, `PAPER 011` and a `CLAIM 011` that is flagged for review
   over the very phrase the plan transcribes ("dose-dependent"). See § 5.

---

## 2 · The real P0, measured

All figures taken on 2026-10-20 on this host, in the task worktree
`.claude/worktrees/plan-repurposing-integration-20261020`.

| Quantity | Measured | Command |
|---|---|---|
| Repository SHA | `c9ce22bf2aa199e41b7d1eb23211f8b11f2919e8`, branch `main`, committed 2026-10-20 20:44:15 +0000 | `git rev-parse HEAD` · `git log -1 --format=%ci` |
| Working branch | `task/plan-repurposing-integration-20261020`, cut from `main` at that SHA | `git worktree add -b …` |
| Python | 3.12.3, `/usr/bin/python3`, GCC 13.3.0 build of 2026-08-31 | `python3 -VV` |
| Package manager | pip 24.0 (system, `/usr/lib/python3/dist-packages`); `uv` present at `~/.local/bin/uv`; **no** conda, mamba, pipx, docker, git-lfs | `python3 -m pip --version` · `command -v` |
| R / Bioconductor | **absent** — no `R`, no `Rscript` on this host | `which R Rscript` → not found |
| CPU | 4 cores, AMD EPYC 9355P | `nproc` · `/proc/cpuinfo` |
| RAM | 16,376,008 kB total (≈15.6 GiB); 10,868,248 kB available at measurement | `/proc/meminfo` |
| Disk | `/dev/sda1` 193 G total, 32 G used, **161 G available**, 17 % | `df -h /home/desktop` |
| GPU | not measured; the plan declares GPU optional for this increment | — |
| External extractors | 7 routed, 6 present, `ffmpeg` absent (zero-spend route documented in the tool itself) — VERDICT "usable" | `python3 framework/scripts/tool_preflight.py` |
| Repurposing packages importable | none of `admet_ai`, `medchem`, `datamol`, `tooluniverse`, `torch`, `chemprop`, `rdkit`, `networkcommons`, `decoupler`, `anndata`, `scanpy`, `pandas`. Present and relevant: `numpy` 2.5.3, `requests` 2.31.0 | `python3 -m pip list` |
| Credentials | none read, none written, none needed: every probe below is unauthenticated and read-only | — |
| Public / private boundary | this is the public edition; no individual-level record exists here and none was created. No query below carried any identifier | `CLAUDE.md` § 0 |

### 2.1 Connectivity, to the services the plan names and to nothing else

Twelve unauthenticated read-only probes, one per service the plan actually needs. All twelve
returned HTTP 200. No payload carried any identifier; no data set was downloaded.

| Service the plan names | Method | Status | Latency |
|---|---|---:|---:|
| Open Targets GraphQL (`api.platform.opentargets.org/api/v4/graphql`) | POST | 200 | 208 ms |
| Monarch API v3 (`api-v3.monarchinitiative.org`) | GET | 200 | 618 ms |
| DGIdb GraphQL (`dgidb.org/api/graphql`) | POST | 200 | 588 ms |
| openFDA drug label (`api.fda.gov/drug/label.json`) | GET | 200 | 850 ms |
| ClinicalTrials.gov **API v2** (`clinicaltrials.gov/api/v2/studies`) | GET | 200 | 122 ms |
| GEO supplementary directory for GSE156243 | HEAD | 200 | 855 ms |
| Europe PMC REST | GET | 200 | 431 ms |
| iLINCS API | GET | 200 | 617 ms |
| Hugging Face dataset API (`everycure/matrix-scores`) | GET | 200 | 286 ms |
| PyPI (`tooluniverse`) | GET | 200 | 173 ms |
| Bioconductor package page (`drugfindR`) | HEAD | 200 | 869 ms |
| GitHub API (rate limit) | GET | 200 | 12 ms |

Two facts follow that the plan could not establish. First, **the network is not the blocker**:
every service it needs is reachable from here today. Second, **PyPI's latest `tooluniverse` is
1.5.7, uploaded 2026-10-13T04:37:28** — which confirms the register's 17–18 October finding that
the `#812` / `#813` SMCP fixes are **not** in the installable wheel, measured rather than
inferred.

---

## 3 · The figures the plan asserts, re-measured

### 3.1 Pathograph counts — the plan's numbers are still correct

The roadmap states, in "Cosa riutilizzare": *"Il pathograph ispezionato dichiara 47 claim, 73
collegamenti diretti distinti, zero archi con relazione annotata e zero nodi con scala biologica
annotata. Rimisurare al momento dell'esecuzione."* Re-measured as instructed:

```
python3 framework/scripts/pathograph.py --json \
  --inputs-dirty-because "measurement for drug-repurposing reconciliation"
```

| Figure | Roadmap says | Measured 2026-10-20 at `c9ce22bf` | Verdict |
|---|---:|---:|---|
| claims | 47 | **47** (`coverage.claims_total`) | confirmed |
| distinct direct claim links | 73 | **73** (`coverage.claim_links_directed_distinct`) | confirmed |
| edges with an annotated relation | 0 | **0** — all 46 undirected edges are `relation_type: UNTYPED`, basis `NO_DECLARED_RELATION_ANNOTATION`, review state `AWAITING_SCIENTIST_TYPING` | confirmed |
| nodes with an annotated biological scale | 0 | **0** — all 47 nodes are `biological_scale: NOT_ANNOTATED` | confirmed |

**No correction is owed on these four numbers.** They are not stale: five days and 323 commits
after the baseline the plan last saw, the pathograph is unchanged on exactly the dimensions the
plan cares about — which is itself the finding, because it means the typing work P3 presupposes
has not been started by anyone.

Figures the plan does not carry and a filler will want, same run: 46 undirected edges · 104
claim-link occurrences · 6,921 propositions scanned · 1,440 candidate propositions emitted (441
normal, 999 low priority) · 1,400 locator candidates of which **403 bound to a claim** · 452
manifests of which **105 bound to a claim** · input digest `597d195c8bf7…` over 455 files · zero
declared losses. The export the plan names as its input,
`disease-models/wwox/analysis/data/pathograph_export.jsonl`, is present: 1,544 lines, 2.3 MB.

### 3.2 Baseline SHA — this is the stale figure, and it is stale by 323 commits

| What the plan names | Measured here |
|---|---|
| Intro: *"Snapshot originario ispezionato: `a405efc305502fb1ab…`"* | the commit **exists** in this repository's history |
| Intro: *"Ultima baseline pubblica verificata dagli scout 9–11 ottobre: `a4f1623e3e269b74…`"* | exists; this is the SHA the register repeats as "main pubblico invariato" from 8 to 15 October |
| P3, 16 October: *"baseline pubblica ora `2ec8444a9a1cc867…` (15 ottobre), che supersede lo snapshot pubblico riportato nell'introduzione"* | exists, committed **2026-10-15 14:13:51 +0000** |
| Q230P recovery commit `cd8788d506dc2a48…` | exists |
| — | **HEAD today is `c9ce22bf2aa1…`, 2026-10-20 20:44:15 +0000, which is 323 commits ahead of `2ec8444a`** (`git rev-list --count 2ec8444a..HEAD`) |

So: every SHA the plan names is real — none was invented — and the newest of them is **323
commits and five days behind** the state this reconciliation measures. The plan's own rule
("non usare lo snapshot della chat come stato vivo") is the right rule and this is the correction
it calls for. The quoted documents were deliberately left uncorrected.

### 3.3 Two further assertions worth correcting

- **"Il lavoro non compare nella roadmap corrente"** (register, 2026-10-10, on the rescue paper).
  True of the roadmap; **false of this repository**, which has read the paper. § 5.
- **Monarch/DGIdb "PARTIAL"** (register, repeatedly, as of the public baseline). Re-measured:
  the adapter is `PRESENT_AND_RUNNABLE` and three of the six P2 improvements the plan asks for
  are already in it (typed identifiers, raw-response retention, explicit error/coverage states);
  pagination genuinely is not. § 4, row P2.

---

## 4 · Component-by-component, step-by-step

### 4.1 The executable queue P0–P8

| ID | What the plan asks | Verdict | Evidence measured now |
|---|---|---|---|
| **P0** | preflight on the server: environment, resources, repo/SHA, integrations present | `PRESENT_AND_RUNNABLE` | § 2 of this document, in full. `tool_preflight.py` → "usable, 1 optional tool absent". No credential read |
| **P1** | install OptimusKG, Open Targets, MATRIX sample; verify ADMET-AI/medchem | `ABSENT` | `_external_repos/` holds only `MANIFEST.md`; none of the five is importable or on disk (§ 4.3). Installing was forbidden to this task; the services are reachable (§ 2.1), so the blocker is a decision, not the network |
| **P2** | strengthen Monarch/DGIdb: identifiers, pagination, actions, provenance, structured output, explicit error/incompleteness | `PRESENT_AND_RUNNABLE`, partially satisfied | `python3 .claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py WWOX --limit 5` → `seed WWOX (HGNC:12799)` · `Monarch coverage: INCOMPLETE` · `Monarch KG neighbours: 0` · `neighbours with known DGIdb drugs: 1/1` · `WWOX [seed] — 3 interactions, 2 approved` · `approved: GEMCITABINE, SORAFENIB`. `--json` retains raw responses, actions and query provenance. `NO_MATCH_FOUND` / `QUERY_ERROR` / `INCOMPLETE` are implemented and regression-tested. **Pagination is not implemented**; the tool declares truncation instead. *This file was reserved to another actor in this wave and was not touched here.* |
| **P3** | select three axes, qualify 10–20 relations | `NOT_CHECKED` — scientific act, reserved to the Scientists | Its named inputs are all present and runnable: `mechanism_intervention_map.md` (93.6 KB), pathograph + export (§ 3.1), `claim_registry_current.md` (47 claims), `discovery_ledger_current.md` (286 records), `dismissal_ledger_current.md` (50), `experiment_ledger_current.md`, `therapeutic_hypotheses_ledger_current.md`, and the three recovered Q230P dossiers under `research/vps_recovery_20260925/residue_q230p_20260922/`. The rescue reference is ahead of the plan (§ 5) |
| **P4** | minimal candidate card, 20 fields | `PRESENT_AND_RUNNABLE`, partially | `framework/scripts/repurposing_bridge.py` builds a non-canonical `IPOTESI` card offline. Extended today with the two things the plan names and the code lacked (§ 6). Fields the card models: identity, route, mechanism/direction with context, sources, counterevidence, translation block (all UNKNOWN until qualified), label-search provenance, endpoint pursued, functional evidence, temporal/model limit, cellular context. Fields that remain narrative, not modelled: novelty-for-WOREE with its dated search, state of known roads, verification scope, question history, prediction engine/version/score semantics, status, added value |
| **P5** | two rankings, non-dominated candidates, no single uncalibrated score | `ABSENT`, and deliberately so | no ranking code exists in this repository and none was added: the bridge invents no score and pools none. The plan's own constraint and this task's instruction agree here |
| **P6 a–e** | AetherCell pilot, contract fixtures, CLUE coverage, one real run, incremental comparison | `ABSENT` (P6a–c), `NOT_CHECKED` (P6d–e) | AetherCell is not present, its weights are not downloaded, its Research License v1.0 restricts the use its own § 5 lists, and no `torch` exists on this host. P6d needs a real inference and is therefore out of reach without an install |
| **P7** | open evaluation: `NOT_IN_GOLD` is not FALSE, versioned reference, out-of-reference result not automatically false | `ABSENT` as a mechanism | the repository has `framework/eval/` (`learned_gates_registry.md`, `failure_taxonomy.md`, benchmarks) but no gold-set comparison surface carrying the NOT_IN_GOLD / UNRESOLVED distinction. Not implemented here: it has no first real evaluation to attach to yet, which is the plan's own precondition ("P7 si realizza nella prima valutazione utile") |
| **P8a** | cellular context and reasons for prior results on the cards | `PRESENT_AND_RUNNABLE`, partially | `p4_fields.cellular_context` now exists in the card with `target_expression`, `cells_tissue_stage`, `coverage`, `limits`, each UNKNOWN rather than absent (§ 6). No data source feeds it: CELLxGENE / Virtual Biotech tools are `ABSENT` |
| **P8b** | optional micro-delegation and task-local tool routing comparison | `NOT_CHECKED` | the runtime has subagent delegation, but the comparison the plan specifies needs ToolUniverse (`ABSENT`) for the tool-routing arm, and measuring the delegation arm is a research-loop experiment, not part of this task |

### 4.2 The "Cosa riutilizzare" table — all eight rows

| Surface the plan names | Verdict | Evidence |
|---|---|---|
| `framework/scripts/pathograph.py` | `PRESENT_AND_RUNNABLE` | § 3.1: ran, exit 0, counts quoted |
| `disease-models/wwox/analysis/data/pathograph_export.jsonl` | `PRESENT_AND_RUNNABLE` | 1,544 lines, 2.3 MB, regenerated by the run above; `--verify` exists to detect drift |
| DisMech sidecar and its scripts | `PRESENT_AND_RUNNABLE` as a *reuse surface*, `ABSENT` as a vendored dependency | referenced by `framework/scripts/candidate_tree_freshness.py`, `pathograph.py`, `trace_claim_foundation.py`; `MANIFEST.md` records it `AUDITED` 2026-07-22, BSD-3-Clause, **not vendored**, and records that WWOX/WOREE/SCAR12 is absent from its knowledge base |
| `.claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py` | `PRESENT_AND_RUNNABLE` | § 4.1 row P2, live output quoted. Not modified here (reserved to another actor this wave) |
| `_external_repos/MANIFEST.md` | `PRESENT_NOT_RUNNABLE` as a component census | the file is present and lists versions, licences and states; but its `spectrum-drug-tracker` row still reads "monogenic-DEE trial drugs and endpoints", status `AUDITED`, which the register's 11 October audit shows overstates WOREE coverage. **The correction is assigned to another actor in this same wave and was deliberately not made here.** MATRIX is pinned at `e22099a1ee39`, which is *not* the `25e1272f` drug_list commit the roadmap discusses |
| `mechanism_intervention_map.md` | `PRESENT_AND_RUNNABLE` | 93,630 bytes at `disease-models/wwox/analysis/mechanism_intervention_map.md` |
| hypothesis / discovery / dismissal / experiment registries | `PRESENT_AND_RUNNABLE` | `registry_records.py index` at `c9ce22bf`: discovery 286 records, dismissal 50, full-text queue 244, claims 54, papers 815, literature 704, working model 18; plus `experiment_ledger_current.md` and `therapeutic_hypotheses_ledger_current.md` |
| `legend-safety-triage` | `PRESENT_NOT_RUNNABLE` | the skill and its references are present; **both predictors it routes to are not installed** — ADMET-AI (`MANIFEST.md`: `c65bf0418e19`, MIT, `DESCRIBED`) and medchem (`UNPINNED`, "VERIFY UPSTREAM BEFORE USE", `DESCRIBED`), and neither `admet_ai`, `medchem`, `datamol`, `rdkit` nor `torch` is importable here. Its BLOCK-1 reasoning route is usable; its computational route is not |

### 4.3 The named external assets

| Asset | Verdict | Measured |
|---|---|---|
| **OptimusKG** | `ABSENT` | not in `MANIFEST.md`, not on disk, not importable. Upstream reachable |
| **Open Targets** | `ABSENT` as a client; service `PRESENT_AND_RUNNABLE` | no adapter in this repository; the GraphQL endpoint answered in 208 ms (§ 2.1) |
| **MATRIX** | `ABSENT` locally | `MANIFEST.md` row: `DESCRIBED`, `e22099a1ee39`, Apache-2.0 + source-data terms. No parquet, no scores, no drug_list on disk. The HF dataset API answered 200 for `everycure/matrix-scores`. The roadmap's drug_list v1.9.3 drift discussion is therefore about an asset this host has never held |
| **ADMET-AI** | `ABSENT` | § 4.2, `legend-safety-triage` row |
| **medchem** | `ABSENT` | § 4.2, `legend-safety-triage` row |
| **drugfindR** | `ABSENT`, with a hard local blocker | needs R ≥ 4.5 and Bioconductor; **this host has no R interpreter at all** (`which R Rscript` → not found). The Bioconductor page is reachable. The plan's "verificare la coppia R/Bioconductor nel preflight" is answered: there is no pair to verify yet |
| **ToolUniverse** | `ABSENT` | not importable; not in `MANIFEST.md`. PyPI latest measured 1.5.7 of 2026-10-13, so `#812`/`#813` are not in the wheel — the register's inference, now measured |
| **MAP** (MAGIC-AI4Med) | `ABSENT` | not present; its demo needs preprocessed control cells and a checkpoint. No `torch` here |
| **NOCAP-AIVC** (Brain-Organoid-AIVC) | `ABSENT` | not present; the register's own note that the CellFM checkpoint is ~67 GB stands unchallenged — 161 G free would hold it, which is a resource fact, not a reason |
| **NetworkCommons / MOON** | `ABSENT` | not present; its declared dependencies (`decoupler` 1.x, `anndata` ≤ 0.10.8) are not installed, and `MANIFEST.md` carries no row for it. Its GPL-3 licence makes external use, not vendoring, the right shape — as the register says |
| **Spectrum drug tracker** | `ABSENT` as code; its manifest row **corrected 2026-10-20** | no clone on disk; `MANIFEST.md` row at `200238a6c692`, MIT. When this reconciliation was first written the row still read "monogenic-DEE trial drugs and endpoints" with status `AUDITED`, which overstated its WOREE coverage; the correction landed the same day in `461bcc28` (capability overstated, WOREE suitability excluded, status unchanged), by the actor who held that file. Its legacy ClinicalTrials.gov endpoint is retired |
| **ClinicalTrials.gov access** | **`PRESENT_AND_RUNNABLE` since `91f8e60c`** | when this reconciliation was first written there was no client of any kind here. `framework/scripts/clinical_census.py` now exists with its regressions — public API v2, read-only, key-less, standard library, zero spend — and its 2026-10-20 run is in this directory (§ 4.4) |
| **GSE156243** | `ABSENT` | no file matching `*GSE156243*` anywhere under `files/`. The GEO supplementary directory is reachable (HEAD 200); the three originals the plan qualifies total ≈0.54 MB. Not fetched here: qualifying an observed input is a Scientist's act, and this task fetched no data |
| **RepurposeAgent** (NLM-DIR) | `ABSENT` | not present. Its external `data.zip` is ~5.1 GB by the register's reading of the FTP index; not fetched. Licence still unidentified upstream, so vendoring remains undecidable, exactly as the register says |
| **AetherCell** | `ABSENT` | not present, no weights, no `torch`. Research License v1.0 restricts the uses its § 5 lists, including use of outputs for treatment selection — which this repository would not do anyway |
| **Obeid et al. rescue reference** | **`PRESENT_AND_RUNNABLE`** | § 5 |

### 4.4 The clinical census the plan's P4/monitoring branch asked for — measured, not by this record

The roadmap's "Censimento clinico" asks for separate queries on WOREE, WWOX-related epileptic
encephalopathy, EIEE28, DEE28, WWOX, MZ-9138 and the relevant sponsor, with no phase or placebo
pre-filter, keeping the synonym that found each record and distinguishing MATCH / NO_MATCH /
QUERY_ERROR / COVERAGE_INCOMPLETE. **That census was run on 2026-10-20 by the actor who held the
clinical-census task, not by this record**, and its result is a hard input here rather than
something to re-run: [`clinical_census_20261020.md`](clinical_census_20261020.md), its data file
and its stored per-page responses. Reproduced as a measurement, with its own limits intact:

- Seven queries, no pre-filter, all pagination exhausted; **no query ended `QUERY_ERROR` or
  `COVERAGE_INCOMPLETE`**; 84 distinct identifiers after deduplication.
- **There is no registered WOREE interventional study on this registry.** WOREE, the spelled-out
  name and EIEE28 all resolve to **one** identifier, `NCT01793168` — an observational
  rare-disease registry and natural-history study whose condition list carries many disorders.
- **DEE28 and MZ-9138 return nothing.** The sponsor query returns `NCT07135050`, a phase 1/2
  AAV9 study for **a different condition with a different candidate** (MZ-1866, Pitt Hopkins
  Syndrome) — recorded because the sponsor query returned it, not because it bears on WOREE.
- A missing hit is an answer about seven queries against one registry on one date: it does not
  prove no study exists, and `NO_MATCH` is not absence.

What this settles for the plan: its MZ-9138 bookkeeping was right to keep PROJECT_ACTIVE apart
from TRIAL_REGISTRATION / ENROLLMENT / FIRST_DOSE, and the registry now answers the registration
question with a measured `NO_MATCH` rather than an `UNKNOWN`. It settles nothing about an IND,
which need not be public, and nothing about the compassionate event the roadmap records.

---

## 5 · The item where this repository is ahead of the plan

The plan's "Riferimento di rescue e obiettivi funzionali" proposes to build a
`WOREE_RESCUE_REFERENCE` in P3 from the abstract of Obeid et al., DOI
10.1016/j.omta.2026.201791, PMCID PMC13343157, and the register introduces it as new to the
radar. Measured here:

```
python3 framework/scripts/fulltext_receipts.py status --pmid 42422765
python3 framework/scripts/registry_records.py get --pmid 42422765
```

- **PMID 42422765** is that paper (*Mol Ther Adv* 2026;34:201791). It is **`PAPER 011`** in the
  paper registry, "Obeid 2026 neuron-specific gene therapy", and the subject of **`CLAIM 011`**,
  typed `DATO preclinico (full text reviewed)`.
- **Twelve receipts** exist: `FTR-20260814-42422765-06` is a `complete_fulltext_read` with 29
  locators (16 figure attestations, 13 body snippets), and eleven further
  `partial_fulltext_read` events run from 2026-07-26 to 2026-10-20.
- Its outputs are on disk: `research/deepdive_manifests/PMID42422765.json`,
  `research/fulltext_dossiers/PMID42422765.md`, `…_partial_locators.md` (55 KB), the JATS full
  text (`files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml` and `…_r2.xml`) and both
  supplement PDFs.
- **`CLAIM 011` is flagged for review over the very phrase the plan transcribes.** Its flag
  argues that the low-dose arm does not rescue survival, that the panel places a *threshold*
  between the two doses, and that a continuum reading and a threshold reading recommend
  different trials. It also records that the primary never declares its dose-unit convention,
  leaving the absolute dose uncertain by a factor of exactly two while the HD/LD ratio is
  invariant.

**Consequence for the plan, stated without softening it:** adopting the roadmap's rescue-reference
sentences as the starting point would import a summary of an abstract over a receipted complete
read *and* would carry a phrasing this repository has already flagged. The scaffold built today —
[`woree_rescue_reference_scaffold.md`](woree_rescue_reference_scaffold.md) — therefore pre-fills
only what the roadmap itself attributes, marks every such cell
`TRANSCRIBED_FROM_ROADMAP · UNVERIFIED_BY_THIS_RECORD`, and routes the filler to the receipts and
locators instead. It states plainly that this is **not Q230P evidence** (the model is a *Wwox*-null
full knockout) and **not a reusable RNA-seq rescue signature** (the primary's data-availability
statement is "not relevant"; GSE156243 is a knockout-versus-wild-type organoid contrast, not this
study's rescue arm).

---

## 6 · What was implemented today, and what that does not mean

Implemented, each with a regression, in the roadmap's own priority order and with zero external
spend, no new dependency, no new framework, no new gate and no new registry:

| Increment | Status | Evidence |
|---|---|---|
| Bridge: the four explicit label-search states, outcome and coverage on separate axes (roadmap § "Stati nel raccordo e nella scheda", P4 "Ricerca delle schede farmacologiche") | **DONE** | `framework/scripts/repurposing_bridge.py`; `test_label_lookup_states_stay_four_different_facts` |
| Bridge: the later P4 fields — endpoint pursued, functional evidence available, temporal/model limit, cellular context — present and UNKNOWN rather than absent | **DONE** | same file; `test_later_p4_fields_are_present_and_unknown_not_absent` |
| Bridge: an empty assertion list reported as an abstention, distinct from a search that returned nothing | **DONE** | `test_empty_assertion_list_is_an_abstention_not_an_empty_lookup` |
| `WOREE_RESCUE_REFERENCE` scaffold with the five endpoint families and eight demanded columns | **DONE** | [`woree_rescue_reference_scaffold.md`](woree_rescue_reference_scaffold.md) |
| P5 ranking, P6 install, P7 gold-set surface, ClinicalTrials.gov client, GSE156243 fetch | **declared BLOCK / not done** | § 7 |

`python3 framework/scripts/test_repurposing_bridge.py` → **8 tests, OK** (was 5).

What the bridge increment does **not** mean: no lookup is performed (the tool has no network),
no state is inferred, no outcome moves the directional comparison, nothing is ranked, no score is
invented, and `NO_MATCH_FOUND` neither drops a candidate nor becomes biological counterevidence.
The card remains `IPOTESI`, `canonical: false`. Its discipline — no network, no promotion,
direction only on the same target/endpoint/context — is unchanged.

---

## 7 · Declared blocks

Each is recorded with its reason and the next action, per the plan's own rule that an absent
branch blocks no other branch.

1. **Installing anything (P1, P6, drugfindR, ToolUniverse, MATRIX, NetworkCommons)** — forbidden
   to this task. The reachability measurement in § 2.1 is what an installing session needs; the
   decision is the Orchestrator's.
2. **drugfindR specifically** — blocked twice over: no R interpreter on this host, and installing
   one is an install. Next action if wanted: decide whether an R/Bioconductor environment is
   worth provisioning *before* any iLINCS work, since drugfindR is otherwise unreachable.
3. **A ClinicalTrials.gov census** — *block lifted the same day, by the actor who held it.*
   When this reconciliation was first written no client existed here. `clinical_census.py` and
   its 2026-10-20 run now answer the plan's census step; § 4.4 records the result, and this
   record did not re-run it.
4. **GSE156243 qualification** — the bytes are absent and fetching plus qualifying them is a
   Scientist's act on an observed input, not a harness act.
5. **P5 and P7** — P5 would require inventing a ranking the plan forbids; P7 has no first real
   evaluation to attach to. Both stay open on purpose.
6. **The `spectrum-drug-tracker` manifest row** — measurably overstated when measured here, and
   reserved to another actor in this wave, so recorded rather than edited. *That actor corrected
   it the same day (`461bcc28`); the block is closed and no edit by this record was needed.*

---

## 8 · What this reconciliation did not touch

The four scientific current files, `disease_model.md`, `_external_repos/MANIFEST.md`,
`kg_thin_slice.py`, any registry, any ledger, any receipt, and any gate. No computational output
was promoted to `DATO`. No molecule was named as a candidate. No dose, administration or
individual recommendation appears anywhere in this directory. Nothing here is medical advice.
