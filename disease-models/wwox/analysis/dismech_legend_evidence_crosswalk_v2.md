# DISMECH ↔ LEGEND EVIDENCE CROSSWALK — v2

> **Non-canonical analysis.** This document reads. It writes nothing into the four scientific
> current files, modifies no DisMech source, and rewrites no pathograph. It is preparation for
> Scientist adjudication, not adjudication.
>
> **Two files outside this document were written, and here is why.** Naming `PMID:27845895` in an
> analysis-layer file makes it a reasoning-layer citation for
> `session_self_eval.unread_premises()`, which took the unread-premise count from 4 to 5 and
> turned `legend_lint` from `PASS` to `BLOCK_BATCH_COMMIT`. The gate is right and was not worked
> around: the identifier is written plainly, and the debt it exposes is real. It was discharged
> the way the gate itself provides for — **`FT-073` appended to `full_text_queue_current.md`**,
> which the state manifest records as *"not a canonical scientific file"* and which admitted
> `FT-048` and `FT-049` outside a `BATCH_COMMIT` on the same rule.
>
> **The append had a downstream effect I had not anticipated, and the regression suite caught
> it.** `framework/scripts/test_batch_queue.py` went from `OK` to `FAIL` — attributed by
> restoring the tree to `HEAD` and re-running, where it passed. `batch_queue.md` is a
> **generated** file (*"do not edit by hand"*) derived from the registries and the queue, and
> FT-073 moves `27845895` out of `NEW` and into `IN_PIPELINE`. Regenerated with the command the
> test itself names; the whole delta is four counter lines
> (unprocessed 415→414, free-full-text 233→232, `NEW` 73→72, `IN_PIPELINE` 25→26) and one row
> relocating from line 131 to line 712 with its content byte-identical. Nothing was hand-edited.
>
> Post-append and post-regeneration: `legend_lint` **PASS** · `growth_anchors check` **PASS**
> (`unread_premises=4`, back to baseline) · `fulltext_receipts verify` **OK, 128 chained, tail
> anchored** — the receipt ledger was not touched · `test_batch_queue.py` **OK, 36 tests** ·
> `test_documented_commands.py` **OK** · `dismech_independent_protocol verify-baseline`
> **PROTOCOL VERIFIED**.
>
> **What this analysis did *not* fix, and why.** `scripts/run_release_regressions.py` reports
> five other failing suites — `test_locator_obligation_reaches_every_route`,
> `test_abstract_corpus_is_not_evidence`, `test_release_surface`, `test_fulltext_trace_contract`,
> `test_session_self_eval`. All five fail identically on a tree restored to `HEAD`, so none is
> this analysis's. The two inspected both assert that `CLAUDE.md` contains strings
> (`verbatim_locators`, `pubmed_corpus_harvest`) that the 2026-08-16 router migration moved into
> the normative files — the tests still measure the pre-router `CLAUDE.md`. Separately,
> `public_release_gate.py` returns `BLOCK_PUBLICATION` on three `DIRECT_IDENTIFIER` hits in
> `learning/plan/FIRST-SCIENTIST-PILOT-READINESS-AUDIT-001.md`, an **untracked** file present at
> session start and never opened here. Reported, not touched.
>
> Public, disease-level, de-identified throughout. Nothing here is medical advice.
>
> **Correspondence ≠ scientific endorsement.** Every mapping below says *these two objects are
> about the same thing*. None of them says *this assertion is correct*.

**Analysis date:** 2026-08-25 · **Supersedes:** the v1 analysis run against the repository-pinned
DisMech state. v1 is **not withdrawn** — its measurement was correct of the object it measured,
and that object is preserved here as §A.

**LEGEND side inspected at:** worktree `.claude/worktrees/evidence-index`, branch
`plan-orchsurf-r4-transcription`, HEAD `e4aa80c`. This branch is 56 commits ahead of local `main`
and 2 behind it; the two commits it lacks touch `roles/`, `scripts/` and `reviews/plan/`, not the
disease model. Every LEGEND figure below is true of `e4aa80c` and of no other tree.

---

## 0 · The finding that survives the correction

**A pinned external benchmark can be reproducible and still be stale.**

The LEGEND-pinned DisMech reference predates the creation of the current WWOX DisMech disease
entry by fifteen days. The pin is *sound* — it resolves, it is content-addressed, and
`verify-baseline` returns `PROTOCOL VERIFIED` against it today. It is also *no longer a
description of the upstream world*.

    REPRODUCIBLE PINNED STATE   ≠   CURRENT EXTERNAL BENCHMARK STATE

This is not an argument against pinning. It is an argument that a system consuming an external
repository needs three distinct facts, and this repository currently records only the first:

| Fact | Where it lives today | State |
|---|---|---|
| the state we froze and derived against | `dismech_export_spec.md` §0, `dismech_phase2_baseline.json`, `export_dismech_dryrun.py:42` | **recorded** |
| the state upstream is in now | nowhere | **not recorded** |
| when we last looked | `dismech_export_spec.md` §0 row *Inspected: 2026-08-04* — the pin date, not a re-check date | **conflated with the pin** |

The three labels used in the operator's brief (`PINNED_REFERENCE_STATE`, `CURRENT_UPSTREAM_STATE`,
`LAST_UPSTREAM_VERIFICATION`) are **explanatory only in this document** and are deliberately not
introduced as governed vocabulary. Naming them is a governance act with an owner; this file has no
such authority and does not design the external-repository architecture that would follow.

---

## A · HISTORICAL PINNED DISMECH STATE

### A.1 What was pinned

| Item | Value | Verified how |
|---|---|---|
| Repository | `monarch-initiative/dismech` | — |
| Commit | `c43343af4054eeeab847621eaab1e10da7efde84` | GitHub commits API, 2026-08-25 |
| Commit date | **2026-08-04T03:58:08Z** | same |
| Commit subject | *Add Bannayan-Riley-Ruvalcaba Syndrome (PTEN) (#7916)* | same |
| Schema path | `src/dismech/schema/dismech.yaml` | — |
| Schema blob SHA | `e1a5bde3b0d35b23808018648a8fc267dc96b10c` (251 151 B) | declared in `dismech_export_spec.md:126` |
| `kb/disorders/*.yaml` at the pin | **1 828** entries | git trees API, `recursive=1`, `truncated: false` |
| WWOX disease entry at the pin | **absent** | contents API returns HTTP **404** for `kb/disorders/WWOX-Related_Developmental_and_Epileptic_Encephalopathy.yaml?ref=c43343af…` |
| WWOX-named paths anywhere at the pin | **0 of 1 828** disorder files, 0 in the whole tree | tree scan for `WWOX`/`wwox` |

Pin sites in this repository: `disease-models/wwox/analysis/dismech_export_spec.md:126` ·
`disease-models/wwox/analysis/scripts/export_dismech_dryrun.py:42` ·
`disease-models/wwox/analysis/dismech_phase3_dryrun_result.md:9` ·
`DATA_SOURCES.md:64`.

### A.2 Why v1 correctly saw no WWOX entry

Because there was none. The absence was a true property of `c43343af`, not a measurement error,
not a path mistake, and not a search that looked in the wrong place. The 404 is reproducible
today at that ref.

### A.3 What the pin *still* correctly anchors

The v1 work is a provenance control and stays that way:

- The **derivation** (`dismech_sidecar_016_024_035.jsonl`) re-derives byte-for-byte and
  `verify-baseline` passes — reproducibility is intact.
- The **field mapping** in `dismech_export_spec.md` was written against a schema that has since
  moved (see §F.1), so it is a mapping to a *historical* contract, not a current one.
- The **absence claim** in the spec is now half-false and must be read with its date:

  > `dismech_export_spec.md:145` — *"The two WWOX disease targets do not exist upstream"*
  > `dismech_export_spec.md:175` — WOREE / DEE28 `MONDO:0014533` — **absent** from `kb/disorders/`
  > `dismech_export_spec.md:176` — SCAR12 `MONDO:0013687` — **absent** from `kb/disorders/`

  At `946d4968` (2026-08-25): line 175 is **now false** — the entry exists. Line 176 is **still
  true** — no SCAR12 entry exists. Line 145 is therefore true of one target and false of the other.

---

## B · CURRENT UPSTREAM DISMECH WWOX STATE

### B.1 The exact inspected object

| Item | Value |
|---|---|
| Repository | `monarch-initiative/dismech` |
| Branch | `main` |
| **Commit inspected (frozen for this analysis)** | `946d496822e882893f97643332c72322a0455e8a` |
| Commit date | 2026-08-25T06:37:42Z (subject: *Add psilocybin-assisted therapy for treatment-resistant MDD (#8176)*) |
| Path | `kb/disorders/WWOX-Related_Developmental_and_Epileptic_Encephalopathy.yaml` |
| **File blob SHA (git)** | `d61eff6b37de0c280908c269814b798065e32959` |
| SHA-256 of retrieved bytes | `332e72e8897ad8a9618783c5e70a8f382ad3ba5b87bcad37ef30640265b0c1ff` |
| Size | 90 354 bytes · 1 772 lines |
| Retrieved | **2026-08-25**, GitHub contents API + `raw.githubusercontent.com` at the frozen commit |
| Integrity check | `git hash-object` of the retrieved file **equals** the blob SHA the API reports — the bytes analysed are the bytes upstream holds |
| `creation_date` declared **inside** the YAML | **`2026-08-19T19:10:00Z`** |
| Disease term | **`MONDO:0014533`** — *developmental and epileptic encephalopathy, 28* |
| `kb/disorders/*.yaml` at this commit | **2 232** (subtree listing, `truncated: false`) — **+404** since the pin |

**Movement during the task — reported, not absorbed.** `main` moved. It was
`946d496822e882893f97643332c72322a0455e8a` at first contact and
`179ba219f825c3d5e0dda70df1ed2583933ea6ea` at the closing re-check the same day; the repository
takes bot-authored curation commits at a high rate, so this is expected traffic and not a signal
about WWOX.

**The WWOX blob did not move.** Re-queried at `?ref=main` after the head advanced, it still
resolves to `d61eff6b37de0c280908c269814b798065e32959` — the same object measured throughout. The
analysis is nonetheless frozen at `946d4968`, and every figure below is a property of that commit
and of blob `d61eff6b…`. **This is the §0 lesson arriving inside its own analysis:** the head a
measurement was taken against and the content it measured are two facts, and one of them moved
while the other did not.

### B.2 Provenance of the entry itself

| Item | Value |
|---|---|
| Commits touching the file | **exactly 1** |
| Creating commit | `4ca217ff336ebf663ea1a3c3aee72e2231bf7e9c`, 2026-08-19T23:58:06Z |
| Subject | *curate(WWOX DEE28/WOREE): new entry with four de-bundled mechanism arms (#8986)* |
| PR | #8986, merged 2026-08-19T23:58:06Z, author `caufieldjh`, 21 files / 6 981 additions |
| Curation route declared in the PR | `just research-disorder claude_code` |
| Curation history snapshots upstream | 3, all under `history/disorders/WWOX-…/`, all stamped `claude-code`: `2026-08-19T203549Z`, `2026-08-19T213711Z`, `2026-08-19T221317Z` |
| Rendered pages upstream | `pages/disorders/WWOX-….html`, `pages/research/WWOX-…-claude_code.html` |

Two things follow, and they cut in opposite directions.

**The upstream entry is agent-curated, and says so.** The PR body names the run command, lists six
HPO labels the research report got wrong and that were corrected against OAK before use, names a
PMID the report cited that resolves to a paper about paediatric blood pressure and was therefore
not cited, and records that the report's own validator returned `needs_review: true` with every
flag respected. That is a disclosed and auditable pipeline, not a hidden one.

**Its evidence layer is nonetheless abstract-derived.** Measured, not inferred — see §F.3.

### B.3 Inventory of the current YAML

Seventeen top-level keys. Counts are of the frozen blob.

| Section | n | Notes |
|---|---:|---|
| `name`, `creation_date`, `category`, `description` | — | category `Mendelian`; description 1 041 chars |
| `synonyms` | 5 | WOREE syndrome · WWOX-related epileptic encephalopathy · DEE28 · EIEE28 · *Developmental and epileptic encephalopathy 28* |
| `disease_term` | 1 | `MONDO:0014533` |
| `parents` | 2 | Epilepsy · Neurological Disease |
| `inheritance` | 1 | Autosomal recessive, `HP:0000007`, 1 evidence item |
| **`pathophysiology`** | **17** nodes | 15 downstream edges · `biological_scale` on all 17 · `conforms_to` on 5 · `cell_types` on 5 · `biological_processes` on 6 |
| `phenotypes` | 24 | all HPO-bound; 23 carry `frequency`; 25 evidence items |
| `genetic` | 1 | WWOX `hgnc:12799`, `relationship_type: CAUSATIVE`, 3 evidence items |
| `animal_models` | 3 | Wwox-null germline KO · Synapsin-Cre neuronal conditional · AAV9-SynI-WWOX gene replacement; 13 evidence items |
| `experimental_models` | 1 | WWOX-deleted human brain organoid; 2 evidence items |
| `prevalence` | 1 | `CASES_IN_LITERATURE`, `ULTRA_RARE`; 2 evidence items |
| `diagnosis` | 3 | WES `NCIT:C101295` · MRI `NCIT:C16809` · EEG `NCIT:C38054`; 4 evidence items |
| `treatments` | 4 | Antiseizure Medication · WWOX Gene Replacement Therapy · Nutritional Support · Genetic Counseling; 6 evidence items |
| `discussions` | 4 | 1 CONTROVERSY, 1 HUMAN_MODEL_MISMATCH, 2 KNOWLEDGE_GAP — all `OPEN`, each with ≥1 proposed experiment; 8 evidence items |

**Evidence layer:** **87** evidence items, **52** distinct `(reference, snippet)` pairs, **10**
distinct references — all PMIDs, no DOI-only citations, no unreferenced assertions.

*(The PR reports `Snippets checked: 67/67 verified`. That is the validator's own count over the
21-file changeset and is **not** the same population as the 52 distinct pairs or the 87 items in
this one blob. The two numbers are reported side by side and not reconciled, because reconciling
them would require the validator's definition, which this analysis does not hold.)*

**Reference frequency in the current entry**

| PMID | items | distinct snippets | sections touched | short title |
|---|---:|---:|---|---|
| 30356099 | 24 | 16 | diagnosis, genetic, patho, phenotypes, prevalence, treatments | Piard 2019 — phenotypic spectrum, 20 additional WOREE cases |
| 36779245 | 15 | 7 | diagnosis, discussions, genetic, patho, phenotypes | Oliver 2023 — epileptology and mortality risk |
| 32000863 | 10 | 6 | animal_models, discussions, patho | Cheng 2020 — GSK3β seizure axis |
| 33914858 | 10 | 5 | animal_models, discussions, experimental_models, patho | Repudi 2021 *Brain* — neuronal deletion, epilepsy and myelin |
| 34634460 | 10 | 6 | animal_models, discussions, patho | Breton 2021 — neocortical oscillations and excitability |
| 33916893 | 6 | 4 | discussions, inheritance, patho, phenotypes, prevalence | Banne 2021 — comprehensive overview |
| 34747138 | 5 | 3 | animal_models, treatments | Repudi 2021 *EMBO MM* — neonatal neuronal gene therapy |
| 24456803 | 3 | 1 | patho, phenotypes, treatments | Abdel-Salam 2014 — early lethal microcephaly syndrome |
| 39507621 | 3 | 3 | discussions, patho, phenotypes | Teplyshova 2024 — adult patient, 40 years |
| 27845895 | 1 | 1 | patho | Hsu 2017 — Hyaluronan activates Hyal-2/WWOX/Smad4 |

---

## C · CURRENT NODE / EDGE CROSSWALK

LEGEND has **no object called a pathograph**. The nearest structures are
`working_model_current.md` § *Mechanistic architecture* (7 prose blocks) and the `P1`–`P7` pathway
vocabulary carried on every claim. Where the table says *Pathograph correspondence*, it means that
structure and nothing more.

LEGEND population being mapped against, at `e4aa80c`: **39** claims in
`claim_registry_current.md`; in `paper_registry_current.md`, **70** `## PAPER` blocks plus **168**
`## CORPUS-STUB-n` and **188** `## CORPUS Pn` placeholders — the latter two summing to the **356**
that `growth_anchors check` reports as `corpus`, so the three figures are one population counted
at two granularities and must not be read as competing totals; **128** receipts over **82** papers
in `fulltext_read_receipts.jsonl`; **64** deep-dive manifests.

### C.1 The seventeen nodes

| # | DisMech node | scale | LEGEND claim(s) | LEGEND pathway | Readiness (§D) |
|---|---|---|---|---|---|
| PP01 | Biallelic WWOX Loss-of-Function Lesion | MOLECULAR | 008, 017, 030, 032 | clinical spectrum / genotype | **B + E** |
| PP02 | Loss of WWOX Scaffold Function | MOLECULAR | 023, 024, 028 | routing / scaffold; domain cooperativity | **A** |
| PP03 | Wnt/GSK-3beta Signalling Dysregulation | MOLECULAR | **016** (in observation), **035** | emerging node — GSK3β | **A** ⚠ see §C.4 |
| PP04 | Hyal-2/WWOX/Smad4 Complex Failure | MOLECULAR | 027 (in observation) | ECM / membrane signalling | **E + F** |
| PP05 | Impaired Oligodendrocyte Maturation | CELLULAR | **003** (consolidated baseline) | P4 — myelination | **D** |
| PP06 | CNS Hypomyelination | TISSUE | 003, 004 | P4 — myelination | **D** (arm) / **A** (rescue) |
| PP07 | Impaired Axonal Conductivity | TISSUE | 003 (implicit) | P4 | **D** |
| PP08 | Disrupted Cortical Neuronal Migration | TISSUE | 014, 015, 022 | P3 — prenatal structure | **A** |
| PP09 | Increased Excitatory Synaptic Drive | CELLULAR | **021** | P1 — network | **A** ⚠ |
| PP10 | Reduced Inhibitory Synaptic Drive | CELLULAR | **021**, 005 | P1 / P2 | **A** |
| PP11 | Intrinsic Neuronal Hyperexcitability | CELLULAR | **021** | P1 | **A** ⚠ |
| PP12 | Cortical Excitation-Inhibition Imbalance | TISSUE | **021**, 002 | P1 | **A** |
| PP13 | Neocortical Network Hypersynchrony | TISSUE | **021**, 002 | P1 — ACTIVE 1 | **A** ⚠ |
| PP14 | Early-Onset Drug-Resistant Seizures | ORGANISM | 013, 031, 001, 037 | P2 / clinical course | **B** |
| PP15 | Progressive Cerebral and Optic Atrophy | TISSUE | 012, 020 | clinical spectrum | **A/B** |
| PP16 | Profound Developmental Impairment | ORGANISM | 031, 017 | clinical course | **D + E** |
| PP17 | Genotype-Stratified Mortality Risk | ORGANISM | **033** (in observation), 013, 019, 030 | genotype-phenotype | **A** ⚠ |

⚠ = a LEGEND figure-level locator qualifies what DisMech asserts. Enumerated in §G.

`conforms_to` is declared on five nodes (PP09, PP10, PP11, PP12, PP13) and all five resolve:
`kb/modules/epilepsy_excitation_inhibition_imbalance.yaml` exists at `946d4968` and contains all
four referenced section names. LEGEND has no equivalent module layer.

### C.2 The fifteen edges

10 `DIRECT`, 5 `INDIRECT_UNKNOWN_INTERMEDIATES`. Every `target` resolves to a node in the same
file — no dangling edges.

| edge | type | DisMech's stated warrant | LEGEND correspondence |
|---|---|---|---|
| PP01 → PP02 | DIRECT | both alleles fail, no functional protein | CLAIM 030 — severity tracks residual **function**, not abundance |
| PP02 → PP03 | DIRECT | loss of hub releases GSK-3β from restraint | **CLAIM 035** supplies the mechanism DisMech asserts without one: a residue-mapped Axin-like docking motif 388–407, L404 required |
| PP02 → PP04 | DIRECT | WWOX is the bridge subunit | CLAIM 027, `in observation`, sourced on a placeholder (§D) |
| PP02 → PP05 | INDIRECT_UNKNOWN | neuronal loss lowers myelination transcripts; steps unknown | CLAIM 003 — same shape, same missing intermediate |
| PP02 → PP08 | INDIRECT_UNKNOWN | malformations follow, no arm accounts for them | CLAIM 014 / 015 — LEGEND reads the same gap as "misassembled prenatal substrate" |
| PP03 → PP13 | INDIRECT_UNKNOWN | *"GSK-3beta inhibition suppresses induced seizures, placing this arm upstream of network-level hyperexcitability"* | **This is the edge §C.4 is about.** |
| PP05 → PP06 | DIRECT | fewer mature oligodendrocytes → less myelin | CLAIM 003 |
| PP06 → PP07 | DIRECT | reduced myelin degrades conduction | CLAIM 003 |
| PP08 → PP16 | INDIRECT_UNKNOWN | malformed cortex *plausibly* contributes | CLAIM 031 — DEE, seizure control does not rescue development |
| PP09 → PP12 | DIRECT | more excitatory drive shifts balance | CLAIM 021 |
| PP10 → PP12 | DIRECT | less inhibition shifts the same balance | CLAIM 021, CLAIM 005 |
| PP11 → PP13 | DIRECT | more excitable neurons fire into the network | CLAIM 021 ⚠ |
| PP12 → PP13 | DIRECT | excitation-shifted cortex supports bursting | CLAIM 021 |
| PP13 → PP14 | DIRECT | hypersynchronous cortex generates seizures | CLAIM 021, working model ACTIVE 1 |
| PP14 → PP16 | INDIRECT_UNKNOWN | seizure burden *plausibly* compounds | CLAIM 031 |

### C.3 Graph topology — a structural observation, offered as a question

The pathograph has **six root nodes**, of which only one is the lesion:

    roots  : PP01 Biallelic lesion · PP09 Increased Excitatory Drive · PP10 Reduced Inhibitory Drive
             PP11 Intrinsic Hyperexcitability · PP15 Progressive Atrophy · PP17 Mortality Risk
    leaves : PP04 · PP07 · PP15 · PP16 · PP17

`PP02 Loss of WWOX Scaffold Function` has exactly four downstream edges: **Wnt/GSK-3beta**,
**Hyal-2/WWOX/Smad4**, **Impaired Oligodendrocyte Maturation**, **Disrupted Cortical Neuronal
Migration**. The excitation–inhibition subgraph (PP09/PP10/PP11 → PP12 → PP13) has **no inbound
edge from the lesion or the scaffold node**, and neither does the degenerative arm (PP15) or the
mortality node (PP17).

The PR body describing this entry states: *"One scaffold-loss node feeds four separable arms:
Wnt/GSK-3beta signalling, the Hyal-2/WWOX/Smad4 TGF-beta route, oligodendrocyte maturation
failure, and cortical excitation–inhibition imbalance."* In the committed YAML the fourth arm off
the scaffold node is **migration**, not E/I. The prose and the graph name different fourth arms.

This is reported as a structural fact about the blob, not as an error claim. There are at least
two innocent readings — the E/I arm may be deliberately left unattached because no source
establishes precedence from the scaffold to it, which would be the same discipline the myelin
controversy is handled with; or the prose may be summarising intent rather than encoding. Which
one it is, is not this document's call. It is §G-6.

### C.4 Calibration case — lithium / GSK-3β / PMID 32000863 (required positive control)

**What the current DisMech YAML says.**

- Node `PP03 Wnt/GSK-3beta Signalling Dysregulation`, `biological_processes: GO:0016055
  Wnt signaling pathway [DYSREGULATED]`, description: *"…This arm is separated from the others
  because it carries its own pharmacological test: inhibiting GSK-3beta with lithium abolishes
  induced seizures in these animals."*
- Node evidence, `PMID:32000863`, `SUPPORT`, `MODEL_ORGANISM`, snippet:
  **"Inhibition of GSK3β by lithium ion significantly abolishes the onset of PTZ-induced seizure
  in Wwox-/- mice."** — explanation: *"The pharmacological result that makes this a causal arm for
  seizures rather than a correlated biochemical change."*
- Edge `PP03 → PP13`, `INDIRECT_UNKNOWN_INTERMEDIATES`: *"GSK-3beta inhibition suppresses induced
  seizures, placing this arm upstream of network-level hyperexcitability."*
- `animal_models[0].modeled_mechanisms[1]` — readout *"Induced-seizure onset after GSK-3beta
  inhibition"*, `direction: ABOLISHED`; `limitations`: *"The rescue was measured against
  pentylenetetrazol-**induced** seizures, not the spontaneous seizures that define the human
  disease… Lithium is also not a selective GSK-3beta inhibitor."*
- `discussions[2] gap_gsk3b_as_a_druggable_node`, `KNOWLEDGE_GAP`, `OPEN`, attached to PP03, with
  a proposed experiment: selective GSK-3β inhibition against **spontaneous** seizures on video EEG.

**Exact cited primary source:** PMID 32000863, Cheng et al. 2020, *Acta Neuropathol Commun*
8:6, DOI 10.1186/s40478-020-0883-3. One reference, ten evidence items, six distinct snippets.

**What LEGEND says.** `PAPER 019` (status `processed`, claim links 015 / 016) ·
`CLAIM 016` *"GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency"*,
status **`in observation`** · receipt `FTR-20260804-32000863-01`, `complete_fulltext_read`,
figures `read`, supplementary `read`, fingerprint present · manifest
`deepdive_manifests/PMID32000863.json`, schema v2, **25 verbatim locators** (20 body, 5 figure;
17 `text_only`, 3 `text_confirmed_by_panel`, 5 `panel_only`), **4 declared artifacts**.

**Where the primary locator actually points.**

| | figure | what it shows, read from the image |
|---|---|---|
| lithium (LiCl 60 mg/kg) | **Figure 7d** | three stacked genotype panels `+/+`, `+/−`, `−/−`, each plotting PTZ vs PTZ+LiCl, **each carrying its own significance bracket**. The wild-type panel is marked as significantly as the null one. |
| ethosuximide (150 mg/kg) | **Figure 7b** | `n.s.` in `+/+` and `+/−`, significant only in `−/−` — genotype-specific |
| GSK3β blots | Figure 7c | pGSK3β(Ser9) falls in `−/−`; **total GSK3β flat** across genotypes and regions |

The paper's own Results sentence, quoted verbatim in the manifest, is: *"Injection of a potent
GSK3β inhibitor lithium chloride significantly suppressed PTZ-induced epileptic seizure in
Wwox−/− mice **(Fig. 7d)**."*

**The existing LEGEND observation from the figure.** Manifest entry, `surface: figure`,
`panel_text_relation: panel_only`, artifact
`files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png`:

> *"The lithium experiment does not establish a Wwox-specific rescue: the same suppression is
> significant in both control genotypes, which the caption and the Results text never say."*

**The existing LEGEND limitation on WT versus Wwox genotypes.** `CLAIM 016`, propagated
2026-08-10 under `BATCH_20260810_005`, carries a 🔴 *Evidence boundary* block stating that the
lithium arm is **not genotype-specific**, that the experiment therefore *"shows an anticonvulsant
that works, in a model that has seizures"*, a `PREMISE_TAG` on every inference of the form
*"lithium helps because the target is de-repressed GSK3β"*, and a `REVIVAL_TRIGGER` requiring an
explicit tested `−/−` vs `+/+` comparison. It also records that the review Steinberg & Aqeilan
2021 (PMID 34831305) transmits the genotype-specific reading the panel does not support.

**The 7b / 7d pointer defect — reported, not repaired.**

`claim_registry_current.md:300` attributes the three-genotype lithium observation to
**`(Fig. 7b; …)`**. The manifest and the primary text both place lithium at **Figure 7d**, and
Figure 7b is the *ethosuximide* panel — the one that **is** genotype-specific. The same
parenthesis then goes on to discuss ethosuximide, so the sentence reads as if one figure carried
both results.

- The **claim's conclusion is unaffected**: the substantive statement (lithium suppressed PTZ
  seizures in all three genotypes; ethosuximide only in the null) matches the manifest exactly.
- The **pointer is wrong**, and it points at the panel that would appear to *contradict* the
  claim's own argument — a reader following `Fig. 7b` finds genotype specificity.
- **Not repaired here.** `claim_registry_current.md` is one of the four scientific current files
  and changes only through `BATCH_COMMIT`. Filed as §G-1.

**The comparison, stated flat.**

| | DisMech (current blob) | LEGEND (`e4aa80c`) |
|---|---|---|
| lithium abolishes PTZ seizures in `Wwox−/−` | asserted, abstract snippet | same, plus the Results sentence with its figure pointer |
| the same suppression occurs in `+/+` and `+/−` | **not present anywhere in the entry** | recorded from the image, `panel_only`, artifact-bound |
| PTZ-induced ≠ spontaneous | recorded, in `limitations` and in the KNOWLEDGE_GAP | recorded in CLAIM 016 |
| lithium is not selective for GSK-3β | recorded | recorded, plus the paper's own Discussion naming lithium's Wnt and remyelination actions in this system |
| GSK3β is **de-repressed**, not more abundant (S9-independent) | not present — the entry says *"significantly increased activation"* | **CLAIM 035 / PAPER 056** (Wang 2012, PMID 22193544), residue-mapped, with the measurement warning that S9 westerns would miss it |
| edge PP03 → PP13 warranted by the rescue | asserted | the warrant is the observation LEGEND's figure locator qualifies |

Adjudication is a Scientist task. What this section establishes is that **the material to
adjudicate exists, is artifact-bound, and has never reached DisMech.**

---

## D · PRIMARY-EVIDENCE READINESS MATRIX

Local analytical descriptions, not governed vocabulary.

| class | meaning |
|---|---|
| **A** | primary source fully read **and** exact locator / verbatim / figure evidence available |
| **B** | primary source read, but the exact assertion chain is incomplete |
| **C** | primary source only partially read |
| **D** | source exists but **no valid full-text read** |
| **E** | identifier / registry normalisation defect prevents reliable linkage |
| **F** | **NOT FOUND IN INSPECTED LEGEND SURFACES** |

Surfaces inspected: `claim_registry_current.md`, `paper_registry_current.md` (PAPER + CORPUS-STUB
+ CORPUS P blocks), `fulltext_read_receipts.jsonl`, `reading_state.md`,
`research/deepdive_manifests/`, `research/full_text_queue_current.md`, `research/surface_census.md`,
`working_model_current.md`, `therapeutics/therapeutic_strategies_current.md`, `registries/batch_queue.md`,
`registries/corpus_seed_pubmed_*`.

| DisMech assertion (node) | cited primary | class | why |
|---|---|:---:|---|
| PP01 biallelic lesion, mixed SNV/CNV architecture | 30356099, 24456803 | **B + E** | 30356099: `partial_fulltext_read`, figures `captions_only`, manifest with 10 body locators — **but its only registry record is `CORPUS-STUB-059`, status `not_processed`, claim links `none`, next action "screening / triage required"**. 24456803 → `PAPER 043`, but its only receipt is a `legacy_reconstruction` with `unknown_legacy` in every coverage slot and **no source fingerprint**, while the PAPER block declares *"Evidence depth: full text reviewed (coverage_status: complete_fulltext_read)"*. |
| PP02 scaffold, WW1/WW2 + SDR, substrate unknown | 39507621 | **A** | `complete_fulltext_read` `FTR-20260804-39507621-01`, 19 locators (16 body, 3 figure), 3 artifacts. The exact DisMech snippet is one of the **body** sentences (verified against the local JATS). Reinforced by CLAIM 024 / `PAPER 055` (35716775) on tandem cooperativity. |
| PP03 Wnt/GSK-3β dysregulation | 32000863 | **A** | 25 locators, 5 figure, 4 artifacts, complete read. **LEGEND holds more than DisMech asserts, in both directions** — see §C.4. |
| PP04 Hyal-2/WWOX/Smad4 complex failure | **27845895** | **E + F** | **`PMID:27845895` has no `PAPER` record, no `CORPUS-STUB`, no receipt, no manifest.** *As measured before this analysis wrote anything*, it appeared in exactly five files — `corpus_seed_pubmed_20260705.tsv`, `…_20260805.tsv`, `…_20260806.tsv`, `…_20260806.jsonl`, and `batch_queue.md:131` marked `unmatched`. Two files now also carry it: `FT-073` and this document, both of them *records of the absence*, and a reproduction that counts them re-measures the report instead of the state (`grep -rIl 27845895 --exclude=full_text_queue_current.md --exclude=dismech_legend_evidence_crosswalk_v2.md`). LEGEND's nearest object is **CLAIM 027** (`in observation`), whose sole source is `CORPUS P214` — **`Identifier: PENDING`**. So the DisMech assertion is `F` on its cited source and `E` on LEGEND's parallel object. **NOT FOUND IN INSPECTED LEGEND SURFACES ≠ biological evidence does not exist.** Debt now declared as `FT-073`; the `E` half is unresolved. |
| PP05 impaired oligodendrocyte maturation | **33914858** | **D** | see the block below |
| PP06 CNS hypomyelination | 33914858 (×2, incl. organoid) | **D** on the arm; **A** on the rescue side via 34747138 | the myelin *measurement* rests on an unread paper; the myelin *rescue* rests on `FTR-20260810-34747138-01`, `complete_fulltext_read`, 20 locators, 10 artifacts |
| PP07 impaired axonal conductivity | 33914858 | **D** | same source, same suspension |
| PP08 disrupted cortical neuronal migration | 32000863 | **A** | manifest carries the malformation locators plus two DisMech does not use: holoprosencephaly-range forebrain patterning, and cortical thinning already at E16.5 |
| PP09 / PP10 increased E / reduced I drive | 34634460 | **A** | `FTR-20260810-34634460-02`, `complete_fulltext_read`, 21 locators (15 body, 6 figure), **7 artifacts**, incl. per-figure JPEGs |
| PP11 intrinsic hyperexcitability | 34634460 | **A** ⚠ | LEGEND's Figure 6 locator records that the paper attributes the effect to a **depolarised resting potential**, the F–I slope not differing once shifted to rheobase |
| PP12 cortical E/I imbalance | 34634460 | **A** | node evidence is the authors' *"essential role in balancing neocortical excitability"* — an interpretive sentence, not a measurement |
| PP13 neocortical network hypersynchrony | 34634460 (×2) | **A** ⚠ | two LEGEND figure locators bear directly on this node — §G-3 and §G-4 |
| PP14 early-onset drug-resistant seizures | 36779245, 30356099 | **B** | 36779245 is `A` (complete read, 20 locators, 3 artifacts); 30356099 is `B + E` as at PP01 |
| PP15 progressive cerebral / optic atrophy | 36779245, 32000863 | **A / B** | both primaries completely read; the human MRI snippet is abstract-sourced |
| PP16 profound developmental impairment | **33916893** | **D + E** | Banne 2021 → `PAPER 040`, status `claim_linked`, claim links 008/019/033. Its **only** receipt is `FTR-20260726-33916893-01`, `record_kind: legacy_reconstruction`, `partial_fulltext_read`, **`unknown_legacy` in all nine coverage slots, no source fingerprint**. **No deep-dive manifest.** There is no valid full-text read behind it. |
| PP17 genotype-stratified mortality | 36779245, 30356099 | **A** ⚠ | 36779245 complete read **with a Figure 4 panel locator** that constrains how the survival result may be read — §G-5 |

### D.1 The single largest readiness gap: PMID 33914858

DisMech's entire myelin arm — **PP05, PP06, PP07**, the *Synapsin-Cre neuronal conditional* animal
model, the *WWOX-deleted human brain organoid* experimental model, and one of the two evidence
items on the myelin-versus-synaptic CONTROVERSY — rests on **10 evidence items from PMID 33914858**.

LEGEND's state for that PMID, measured at `e4aa80c`:

| | |
|---|---|
| registry | `PAPER 004` — *Repudi 2021 Brain myelination*, status **`integrated`**, claim links **003** |
| CLAIM 003 status | **`consolidated baseline`** |
| receipts | **0.** `study_id.pmid == "33914858"` matches **0 of 128** ledger records. (A raw `grep` returns 5 hits; all five are *prose mentions inside other papers' receipts*. The count that matters is 0.) |
| `reading_state.md` row | **absent** — it is one of the few DisMech-cited PMIDs with no row at all |
| deep-dive manifest | **absent** |
| queue | `FT-044`, priority **ALTA**, **`🔴 LETTURA SOSPESA 2026-08-09 — NESSUNA RECEIPT EMESSA`** |
| reason for suspension | **textual-surface invalidity, not budget.** Deterministic extraction returns `Results were considered significant when P 5 0.05` where the page prints `P < 0.05`; zero occurrences of `<`, `>`, `≤`, `≥` in the whole document against 14 of `P 5 0.0…`. `fitz`, `pdfplumber` and `pypdf` all agree on the wrong character, so cross-checking two extractors does not detect it. |
| `surface_census.md:87` | `PMID 33914858 · FT-044 · pdf_only · SUSPECT — contains the C0 control U+0002` |

So: **a `consolidated baseline` LEGEND claim and three DisMech pathophysiology nodes rest on the
same paper, and neither system has a verified full-text read of it.** DisMech's five snippets from
it are abstract-derived (§F.3 method); LEGEND's read is refused at the surface.

This is the one item where the two systems fail in the *same* place, and it is the highest-value
target on the queue: acquiring a valid surface for 33914858 would upgrade `PP05/PP06/PP07` from
**D** and would discharge `FT-044`, the oldest ALTA-priority debt bearing on a baseline claim.

---

## E · DISMECH-USED PUBLICATION MATRIX

All ten publications cited by the current WWOX DisMech entry, against LEGEND state at `e4aa80c`.
`PAPER` is resolved **strictly from the `**Identifier:**` line** of each registry block — a PMID
appearing anywhere else in a block (reference lists, notes) is not an identity claim. Under that
rule, 65 of 70 `PAPER` blocks carry ≥1 PMID on their identifier line, 64 distinct PMIDs are
claimed, and exactly one PMID (`25331887`) is claimed by two blocks (`PAPER 027`, `PAPER 030`).

| PMID | LEGEND PAPER | registry status | receipts | deepest depth | figures | suppl. | manifest | locators (body/fig) | artifacts |
|---|---|---|---:|---|---|---|---|---|---:|
| **30356099** | ✗ — **`CORPUS-STUB-059`** | **`not_processed`**, claim links `none` | 1 | `partial_fulltext_read` | **`captions_only`** | `unavailable` | ✅ v2 | 10 (10 / 0) | 1 |
| **36779245** | `PAPER 018` | `filtered_in`, claim links **`pending`** | 3 | `complete_fulltext_read` | `read` | `unavailable` | ✅ v2 | 20 (17 / 2 + 1 table) | 3 |
| **32000863** | `PAPER 019` | `processed`, claims 015 / 016 | 1 | `complete_fulltext_read` | `read` | `read` | ✅ v2 | **25 (20 / 5)** | 4 |
| **33914858** | `PAPER 004` | **`integrated`**, claim 003 | **0** | **none** | — | — | **✗** | **0** | 0 |
| **34634460** | `PAPER 031` | `integrated`, claim 021 | 2 | `complete_fulltext_read` | `read` | `unavailable` | ✅ v2 | **21 (15 / 6)** | **7** |
| **33916893** | `PAPER 040` | `claim_linked`, claims 008/019/033 | 1 | `partial_fulltext_read` **(legacy_reconstruction, `unknown_legacy` ×9, no fingerprint)** | `unknown_legacy` | `unknown_legacy` | **✗** | **0** | 0 |
| **34747138** | `PAPER 005` | `integrated`, claim 004 | 4 | `complete_fulltext_read` | `read` | `read` | ✅ v2 | 20 (16 / 4) | **10** |
| **24456803** | `PAPER 043` | `claim_linked`, claims 030/032 | 1 | `partial_fulltext_read` **(legacy_reconstruction, `unknown_legacy` ×9, no fingerprint)** | `unknown_legacy` | `unknown_legacy` | **✗** | **0** | 0 |
| **39507621** | `PAPER 015` | `integrated`, claim links **`none`** | 2 | `complete_fulltext_read` | `read` | `not_present` | ✅ v2 | 19 (16 / 3) | 3 |
| **27845895** | **✗ — no registry object of any kind** | — | **0** | **none** | — | — | **✗** | **0** | 0 |

**Reassessment of PMID 33914858 from current repository state:** see §D.1. Stated plainly and
without reusing any historical label: **`PAPER 004` is marked `integrated` and supports a
`consolidated baseline` claim while the ledger holds zero receipts for it, `reading_state.md` has
no row for it, no deep-dive manifest exists, and its queue entry records the reading as
explicitly suspended for surface invalidity.** The registry status and the reading ledger disagree,
and the ledger is the one with the evidence.

**Four further registry/ledger disagreements surfaced by this pass** (all class **E**):

1. **30356099** — the most-cited source in the DisMech entry (24 items, 16 snippets) has a
   receipt and a schema-v2 manifest in LEGEND but no `PAPER` record; it is a corpus placeholder
   whose declared next action is *"screening / triage required"*. Reading has overtaken the
   registry.
2. **24456803 / `PAPER 043`** — block declares `complete_fulltext_read`; ledger holds only a
   legacy partial with no fingerprint.
3. **33916893 / `PAPER 040`** — supports three claims including `CLAIM 008`
   (`consolidated baseline`) on a legacy partial with `unknown_legacy` coverage throughout.
4. **`PAPER 004`** — its own note records *"⚠️ Duplicato corpus **CORPUS-STUB-087** (stesso DOI)
   → mergiare in un prossimo BATCH_COMMIT"*, i.e. a known unresolved duplicate on the very paper
   carrying DisMech's myelin arm.

**One more, on the other side of the ledger:** `PAPER 018` (36779245) is `filtered_in` with claim
links **`pending`**, yet `CLAIM 033` and `CLAIM 017` both wikilink it and DisMech draws 15
evidence items from it. The paper is completely read with 20 locators; the *link* is what is
missing.

---

## F · STRUCTURAL / PROVENANCE DELTAS

### F.1 The schema pin has moved

| | pinned (`c43343af`) | current (`946d4968`) |
|---|---|---|
| `src/dismech/schema/dismech.yaml` blob | `e1a5bde3b0d35b23808018648a8fc267dc96b10c` | **`ff3d1ee0062937b8fffa1abc810a9bf493670dc0`** |
| size | 251 151 B | **285 180 B** (+34 029 B) |

`dismech_export_spec.md` §0 states: *"The exporter must fail closed if the schema blob SHA at run
time differs from the pinned value. A changed schema is a specification review event, not a
runtime warning."* That condition is now **met**. The field mapping in the spec is a mapping to a
superseded schema until re-verified. This is the pin discipline **working**, not failing — but
nothing has triggered it, because nothing re-checks upstream.

### F.2 The four delta classes (§9 of the brief)

**Class 1 — DisMech has structure or content that LEGEND currently lacks.**

| item | detail |
|---|---|
| A typed, machine-readable pathograph | 17 nodes, 15 typed edges, `biological_scale` on every node, `conforms_to` into a shared epilepsy module. LEGEND's equivalent is **seven prose paragraphs** under *Mechanistic architecture* plus `P1`–`P7` labels on claims. LEGEND cannot answer *"what is downstream of the scaffold node"* mechanically. |
| Ontology binding at scale | 24 HPO terms with frequency, 6 GO processes with direction modifiers, 5 CL cell types, 3 NCIT diagnosis terms, 4 NCIT/treatment terms, MONDO disease term. LEGEND has a **10-row MAXO crosswalk** and a 40-row HPO neighbour ranking — neither is a per-assertion binding. |
| Structured model→mechanism fidelity | `animal_models[].modeled_mechanisms[]` with `relationship` (RECAPITULATES / RESCUES), `fidelity`, per-readout `direction`, and a **`limitations` string on every one**. LEGEND records limitations in claim prose, not as a field. |
| Typed, attached open questions | `discussions[]` with `kind`, `status`, `attaches_to[]` and `proposed_experiments[]`. LEGEND's nearest is `research_candidates_current.md` + `dismissal_ledger_current.md`, neither of which attaches to a mechanism node. |
| Cross-disease module reuse | `conforms_to: epilepsy_excitation_inhibition_imbalance#…` places WWOX inside a shared epilepsy mechanism. LEGEND is single-disease by construction. |

**Class 2 — LEGEND has primary-evidence detail that DisMech currently lacks.**

| item | detail |
|---|---|
| **Panel-level evidence** | 5 `panel_only` + 3 `text_confirmed_by_panel` locators on 32000863; 6 figure locators incl. **2 `text_contradicted_by_panel`** on 34634460; 3 on 39507621; 2 on 36779245. DisMech has **no figure-evidence surface at all** — every one of its 87 evidence items is a text snippet. |
| **The lithium genotype qualification** | §C.4. Absent from DisMech. |
| **Residue-level GSK-3β mechanism** | `CLAIM 035` / `PAPER 056` (Wang 2012, PMID 22193544): Axin-like docking motif 388–407, **L404 strictly required**, inhibition **S9-independent**. DisMech asserts the arm with no mechanism and cites *"increased activation"* — which the S9-independence result says a standard western would misreport. **PMID 22193544 is not cited by DisMech.** |
| **Vigabatrin safety** | `CLAIM 001` (`conflicting evidence`): VABAM documented in WWOX-DEE (Choi 2026), against seizure reduction reports. DisMech's `Antiseizure Medication` treatment names no agent and carries no safety signal. This is the delta with the most clinical weight in the whole crosswalk. |
| **Ketogenic diet** | LEGEND records 3/5 WOREE patients improved (Chong 2023). DisMech has no KD treatment entry. |
| **Gene-therapy dose threshold** | `CLAIM 011` (`flagged for review`), Obeid 2026: AAV9-hSynI-hWWOX rescue is a **threshold, not a gradient** — Figure 3B, low dose moves death from ~20 to ~90 days and then reaches zero; high dose plateaus ~80% to 300 days. DisMech's gene-therapy entry rests only on the 2021 result. |
| **First-in-human** | LEGEND `TX-007` records a news-level compassionate-use n-of-1, explicitly tagged as not peer-reviewed, with a 5-row monitor. DisMech saw the same reports and **deliberately excluded** them, recording the exclusion in `treatments[].notes`. **Both systems handled this correctly and differently** — LEGEND tracks it as a watchlist item outside the evidence layer, DisMech refuses it at the evidence layer. Worth naming as a design contrast, not a defect. |
| **Genotype-class cohort statistics** | `CLAIM 013` (Gao 2025, n=50): hypertonia 72/23/17 %, seizures 100/92/67 %, respiratory complications 76/31/50 % across N/N, N/M, M/M, FDR-corrected. DisMech's genotype axis is survival only. |
| **Q230P** | `CLAIM 019` (`consolidated baseline`): normal transcript, protein not detected. DisMech records `p.(Gln230Pro)` only as *"recurrent in four families"*. |

**Class 3 — both represent essentially the same mechanism.**

PP05→PP06→PP07 ≡ CLAIM 003 (including the non-cell-autonomy, which both systems foreground) ·
PP09/PP10/PP11/PP12/PP13 ≡ CLAIM 021 · PP08 ≡ CLAIM 014/015 · PP14 ≡ CLAIM 031 ·
PP01 ≡ CLAIM 008/030 · gene replacement ≡ CLAIM 004 · the myelin-vs-synaptic controversy ≡ the
working model's own hedge (*"hypomyelination as a possible **amplifier** — requires imaging
confirmation"*). **Both systems independently refuse to place myelin upstream of excitability.**

**Class 4 — materially different, requires Scientist adjudication.** → §G.

### F.3 A measured structural difference in how evidence is bound

**Method.** For the three DisMech-cited papers whose full text is present in this working tree as
structured JATS, every distinct DisMech snippet was normalised (NFKD, unicode minus/dash folding,
case-folded, non-alphanumerics stripped) and located against the `<abstract>`, `<body>` and
`<back>` of the local XML.

**Denominator: 16 of the 52 distinct `(reference, snippet)` pairs, covering 3 of the 10 cited
publications** — those, and only those, whose full text is on this disk.

| paper | snippets tested | in abstract | in body |
|---|---:|---:|---:|
| 32000863 Cheng 2020 | 6 | **6** | 0 |
| 36779245 Oliver 2023 | 7 | **7** | 0 |
| 39507621 Teplyshova 2024 | 3 | 2 | **1** |
| **total** | **16** | **15** | **1** |

Fifteen of sixteen come from the abstract. The PR body corroborates the mechanism from the other
side: it reports a claim that *"could not be verified against **either abstract** it was attributed
to"* and was consequently not curated.

This is not a criticism of the upstream entry — abstract-bound snippets are exactly verifiable,
which is the property DisMech's validator enforces, and 67/67 passed. It is the **structural
reason** DisMech carries no panel-level qualification: the surface it verifies against does not
contain figures. And it is the precise shape of the contribution LEGEND could make.

**Caveat, stated because it bounds the claim:** this is measured over 3 papers, not 10. The
remaining 7 may distribute differently. Extending the measurement requires acquiring their full
texts, which this analysis did not do.

### F.4 Re-test of the v1 findings under the corrected premise

Every finding re-run against `e4aa80c` and `946d4968` today. None was carried over on the strength
of the earlier report.

| # | v1 finding | verdict now | evidence |
|---|---|---|---|
| 1 | **Sealed derivation drift around CLAIM 016** | **STILL TRUE** | `scope_drift()` returns **exactly 1** drifted block: `CLAIM 016`, sealed `caa8b36e7ca4…` → live `a419a56049fd…`. `unresolved_drift()` = 1. `assert_exportable()` returns 1 blocking message. |
| 2 | **Figure 7b vs Figure 7d pointer discrepancy** | **STILL TRUE, uncorrected** | `claim_registry_current.md:300` says `(Fig. 7b; …)`; manifest entry and the paper's own Results sentence both say **Fig. 7d**; 7b is the ethosuximide panel. §C.4. |
| 3 | **Exporter inversion — the best panel-level evidence is rejected** | **STILL TRUE, and sharper than reported** | Both `CLAIM 016` occurrences on PMID 32000863 terminate at **`LINK_ROLE_NON_SUPPORTING`** (`normalised_role: UNQUALIFIED_REFERENCE`, from `raw_link_role: wikilink_only`) with **`locator_status: NOT_EXTRACTED`**, `locator: {snippet: null}`, `locator_fingerprint: "LF-none:unsought"`. The strings `panel`, `surface`, `figure` and `Fig. 7` occur **0 times** in the whole 53-record sidecar. Meanwhile 17 occurrences export on body-text locators from 35716775 and 22193544. **The paper with the richest figure evidence in the bundle is the only one that exports nothing — and its figure evidence was never sought, not merely rejected.** |
| 4 | **`verify-baseline` checks frozen blobs, not current scope drift** | **STILL TRUE — and it is deliberate, documented, and demonstrable** | `dismech_independent_protocol.py:253-266` marks `sealed_scope` inputs *"Deliberately NOT an error"*, checking only that the scope still resolves. Run today: `verify-baseline` → **`PROTOCOL VERIFIED`, exit 0**, while `assert_exportable()` → **1 unresolved drift on CLAIM 016**. The green check and the red gate are looking at the same tree. |
| 5 | **No gate coverage for `scope_drift()`** | **STILL TRUE** | `assert_exportable` appears in exactly **3** places: its own definition (L388), one comment (L257), and one unit test (`test_dismech_independent_protocol.py:723`). **No production call site. No CLI subcommand** — the parser registers 8 subcommands and none is `scope-drift` or `assert-exportable`. `framework/protocols/unattended_delegation_readiness.md:44` still lists *"P1 — Wire `assert_exportable()` into the export path"* as outstanding, `delegable`. |
| 6 | **Gitignored `files/` — local artifact verification ≠ clean-clone reproducibility** | **STILL TRUE, and worse than stated** | `.gitignore:7` = `files/`; `git ls-files files/` → **0**. Of the artifacts the **committed** sidecar names by SHA-256, `PMID35716775_Rotem-Bamberger2022.pdf` and `PMID22193544_Wang2012_PMC_JATS.xml` are **not present on this disk at all** — and `verify-baseline` still returns `PROTOCOL VERIFIED`, because the baseline seals the sidecar output and the tracked repo inputs, not the third-party artefacts. It is not only that a clean clone cannot re-verify a locator snippet: **this working tree cannot either, and nothing reports it.** Only 32000863's artifacts (XML, supplementary PDF, figure PNGs) survive locally. |
| 7 | **PMID 33914858 status** | **STILL TRUE, and it is the load-bearing gap** | §D.1 and §E. Re-derived from current repository state, not from any historical label. |
| 8 | **CLAIM 017 read-status drift** | **STILL TRUE, two distinct defects** | (a) `CLAIM 017` (`consolidated baseline`) states *"Abdel-Salam 2014 **corpus, non in registry**"* — but **`PAPER 043` exists** with `Identifier: PMID 24456803`, and it is the paper meant. The claim's own linkage statement contradicts the registry. (b) The link is one-way: `PAPER 043` lists `Claim links: 030, 032` and wikilinks CLAIM 030 · CLAIM 032 — **not 017**. (c) The underlying read is a legacy partial with `unknown_legacy` coverage and no fingerprint, while `PAPER 043` declares `complete_fulltext_read`. Additionally the claim's `Source` names *"Piard 2018"* while its wikilink resolves to `PAPER 025` = **PMID 30853297** (EJPN 2019), a *different* Piard paper from the Genet Med **30356099** that DisMech leans on 24 times and that LEGEND holds only as `CORPUS-STUB-059`. |

**Two of the eight are worse than v1 reported (3 and 6). None is refuted. None was
over-corrected.**

---

## G · SCIENTIST ADJUDICATION QUEUE

Ordered by consequence. Each item names what DisMech asserts, what LEGEND holds, and the question
that remains. **None of these is decided here.**

---

**G-1 · The lithium arm is not genotype-specific, and DisMech does not know it.** *(class 4)*

- **DisMech:** PP03 description — *"inhibiting GSK-3beta with lithium abolishes induced seizures
  in these animals"*; edge PP03→PP13 warranted as *"placing this arm upstream of network-level
  hyperexcitability"*; `gap_gsk3b_as_a_druggable_node` names PTZ-vs-spontaneous and lithium's
  non-selectivity, but **not** the genotype question.
- **LEGEND:** Figure 7d, image-inspected, `panel_only`, artifact-bound: the same suppression is
  significant in `+/+` and `+/−`. `CLAIM 016` carries this as a declared evidence boundary with a
  `PREMISE_TAG` and a `REVIVAL_TRIGGER`.
- **Question:** does the PP03→PP13 edge survive as written, or does its warrant need to become
  *"GSK-3β inhibition raises PTZ seizure threshold in this model, in a manner not shown to be
  WWOX-dependent"*? And separately: does `claim_registry_current.md:300`'s `Fig. 7b` pointer get
  corrected to `Fig. 7d` in the next `BATCH_COMMIT`?

---

**G-2 · The myelin arm rests on a paper neither system has properly read.** *(class 4, highest
operational value)*

- **DisMech:** PP05, PP06, PP07, the Synapsin-Cre model, the organoid model and one CONTROVERSY
  evidence item — 10 items, 5 snippets, all from PMID 33914858, all abstract-derived by the §F.3
  method.
- **LEGEND:** `CLAIM 003` is `consolidated baseline`. Receipts for 33914858: **0 of 128**.
  `FT-044` suspended for textual-surface invalidity since 2026-08-09. No manifest.
- **Question:** acquire a valid surface (publisher HTML/JATS, or PMC, or a re-rendered PDF passing
  the `\([Pp]\s+\d` sentinel on raw text) and read it. Until then, does `CLAIM 003` hold its
  `consolidated baseline` status, and do PP05/PP06/PP07 hold their evidence?

---

**G-3 · The pannexin arm: 2.5-fold up, described as no effect.** *(class 4)*

- **DisMech:** PP13 node evidence — *"These bursts were NMDAR and gap junction dependent."*
- **LEGEND:** 34634460 Figure 3D-d1, `text_contradicted_by_panel`, read at 6× from native pixels:
  normalised burst frequency 1.0 baseline, **0** under d-APV, **~0.15** under CBX (matching the
  text's 87 % decrease), **~2.55 under BB-FCF** — carrying no marker, and rising to ~2.6 at
  washout. The Results and the Discussion describe that as an absence of effect.
- **Question:** the NMDAR and gap-junction dependencies stand. Does the pannexin result belong in
  the node — as a dependency of the opposite sign — or is a 2.5-fold point estimate with wide
  error and no reported test simply not reportable?

---

**G-4 · Is the neocortex-only framing intact?** *(class 4)*

- **DisMech:** PP13 description — *"Spontaneous bursting appears in neocortical but not
  hippocampal slices … so the neocortex, and specifically its superficial layers, is the driver."*
- **LEGEND:** 34634460 Figure 5D, `panel_only`: the panel prints **`p = 0.0312` with an asterisk**
  on the CA1→CA3 population spike, and **its own caption reads "No significance"**. Text and panel
  agree the measure is elevated in the knockout; the caption contradicts both. Separately, Figure
  1B — the panel establishing the neocortex/hippocampus dissociation — labels the heterozygote's
  second channel **`ch?`** where every other row reads `ch1`/`ch2`, adjudicated at 10× on native
  pixels.
- **Question:** does *"not hippocampal"* survive a positive hippocampal result on the paper's own
  face? And does the dissociation panel's placeholder need raising upstream?

---

**G-5 · Survival: two classes or three steps?** *(class 4, and probably concordant)*

- **DisMech:** PP17 — *"biallelic null genotypes have significantly lower survival probability
  than genotypes carrying at least one presumed hypomorphic missense allele."* `genetic.notes`
  explicitly declines the stronger version. `gap_are_missense_alleles_truly_hypomorphic` is `OPEN`.
- **LEGEND:** `CLAIM 033` (`in observation`) carries the numbers — log-rank **p = .0085**; 5-year
  <50 % vs >75 %; 10-year ~25 % vs >60 %; splice-site coded as null; overall mortality ~35 %,
  dominant cause respiratory. Its Figure 4 panel locator adds: null/missense sits **above**
  missense/missense, and the **95 % bands of the upper two overlap across the whole followed
  range** — consistent with the text's own statement that one versus two missense variants made no
  difference, and *inconsistent with reading p = .0085 as a graded three-step ranking*.
- **Question:** the two statements appear compatible — both are two-class. Confirm that, and
  decide whether the *non*-gradient is worth stating explicitly in PP17, since the node's own
  description invites a dose-response reading (*"the milder allelic disorder SCAR12 sits at the
  missense end of the same spectrum"*).

---

**G-6 · The E/I arm is not attached to the lesion.** *(class 1 / class 4, structural)*

- **DisMech:** PP02's four downstream edges are Wnt/GSK-3β, Hyal-2/Smad4, oligodendrocyte
  maturation, **migration**. PP09, PP10, PP11 are graph roots. The PR prose names E/I as the
  fourth arm off the scaffold node.
- **LEGEND:** `CLAIM 021` is `consolidated baseline` and the working model elevates network-state
  pathology to **core-pathway status** (ACTIVE 1) — i.e. LEGEND treats the E/I arm as primary, not
  as an unattached observation.
- **Question:** is the detachment deliberate epistemic discipline (no source establishes
  precedence from the scaffold to E/I) or an encoding gap? If the former, LEGEND's ACTIVE-1
  framing may be the more committed of the two and should say so.

---

**G-7 · Intrinsic excitability: membrane property or resting potential?** *(class 4, narrow)*

- **DisMech:** PP11 — *"depolarised resting membrane potential, increased action-potential
  frequency, increased sag current and post-inhibitory rebound … a membrane-property change."*
- **LEGEND:** 34634460 Figure 6, `text_contradicted_by_panel`: the exemplars show a clean
  genotype gradient (~4 / 9 / 13 APs at the same injection) which **the paper's own analysis
  removes**, attributing the hyperexcitability to the depolarised resting potential because the
  F–I slope does not differ once shifted to rheobase.
- **Question:** does *"increased action-potential frequency"* belong in the node as a separate
  property, or is it downstream of the resting-potential shift the same paper identifies?

---

**G-8 · Hyal-2/WWOX/Smad4: neither system has the primary properly.** *(class 4 + readiness)*

- **DisMech:** PP04 rests on a single evidence item from **PMID 27845895** (Hsu 2017,
  *Oncotarget*), `IN_VITRO`, *"In WWOX-deficient cells, HA failed to induce Smad2/3/4 relocation
  to the nucleus."*
- **LEGEND:** **no object for 27845895 on any inspected surface** — no PAPER, no stub, no receipt,
  no manifest. Before this analysis wrote anything it lived in four corpus-seed files and as
  `unmatched` in `batch_queue.md:131`; `FT-073` and this document have since been added and are
  records *of* the absence, not resolutions of it. `CLAIM 027` is `in observation` and its only
  source is `CORPUS P214`, `Identifier: PENDING`.
- **Question:** ingest 27845895 through the normal pipeline, and resolve `CORPUS P214`'s
  identifier. Until then LEGEND cannot check DisMech's only TGF-β-arm assertion, and DisMech's
  arm has one item behind it.
- **Already actioned, partially:** the reading debt is now declared as **`FT-073`** in
  `full_text_queue_current.md` (priority MEDIA, PMC route named, surface sentinel required before
  reading). The **`CORPUS P214` identifier remains `PENDING`** and is deliberately *not* guessed —
  whether P214 is this paper, the 2019 HYAL-2/WWOX/SMAD4 review at
  `paper_registry_current.md:1027`, or a third source, is registry work for a `BATCH_COMMIT`.

---

**G-9 · Two safety-relevant absences in DisMech.** *(class 2, flagged for judgement, not action)*

- **Vigabatrin / VABAM.** LEGEND `CLAIM 001` is `conflicting evidence` and the working model
  carries *"strong caution / avoid unless alternatives are exhausted"* under ACTIVE 2. DisMech's
  `Antiseizure Medication` entry deliberately names no agent, *"because the cited cohorts report
  drug resistance as a class property rather than comparing individual drugs"* — a defensible
  curation rule that nonetheless leaves a documented safety signal unrepresented.
- **Ketogenic diet.** LEGEND records 3/5 improved (Chong 2023); DisMech has no entry.
- **Question:** is either within DisMech's curation scope, and if so what would the evidence bar
  be? This is a question about the *other* system's contract and belongs to whoever owns that
  conversation — not to this repository unilaterally.

---

**G-10 · Provenance hygiene, LEGEND side.** *(not scientific — infrastructure)*

Five registry/ledger disagreements, none of which changes a biological conclusion and all of which
degrade auditability: `CORPUS-STUB-059` (30356099) read but unregistered · `PAPER 043` declaring a
depth the ledger does not hold · `PAPER 040` supporting a baseline claim on a legacy partial ·
`PAPER 004`'s known duplicate `CORPUS-STUB-087` · `PAPER 018` `filtered_in` with claim links
`pending` while two claims already wikilink it. Plus the four infrastructure findings that
survived re-test: `CLAIM 016` unresolved scope drift, `assert_exportable()` with no production
call site, the exporter's blindness to figure surfaces, and untracked `files/` making locator
verification unreproducible from any clone — including this one.

---

## Success condition — worked, on one node

> *A Scientist must be able to take any current DisMech WWOX mechanistic node or causal edge and
> immediately answer six questions.*

Taking **PP03 Wnt/GSK-3beta Signalling Dysregulation**:

| question | answer |
|---|---|
| What exactly does DisMech currently assert? | GSK-3β activation is significantly increased across cortex, hippocampus and cerebellum in Wwox-null mice; the arm carries its own pharmacological test; it sits upstream of neocortical hypersynchrony through unmapped intermediates. Blob `d61eff6b…`, `pathophysiology[2]`. |
| Which primary publication supports it there? | PMID 32000863 (Cheng 2020), one evidence item on the node, plus 9 more across `animal_models` and `discussions`. |
| Has LEGEND actually read that publication? | Yes. `FTR-20260804-32000863-01`, `complete_fulltext_read`, figures `read`, supplementary `read`, source fingerprint present. |
| Where is LEGEND's exact locator / verbatim / figure evidence? | `deepdive_manifests/PMID32000863.json`, 25 locators, 4 declared artifacts; the load-bearing one is `surface: figure`, `panel_only`, artifact `…_assets/40478_2020_883_Fig7_HTML.png`, anchor *"Figure 7d, image inspected at the native 1946×1627 pixels"*. |
| What limitation has LEGEND already observed? | `CLAIM 016`, 🔴 Evidence boundary, `BATCH_20260810_005`: the lithium arm is **not genotype-specific**; `PREMISE_TAG` on any GSK-3β-mediated inference; `REVIVAL_TRIGGER` = an explicit tested `−/−` vs `+/+` comparison. Status held at `in observation`, not promoted. |
| What scientific question remains? | **G-1.** |

The same six answers are available for every node in §C.1 except **PP04**, **PP05**, **PP06**,
**PP07** and **PP16**, where question three answers *no* and the reason is named in §D.

---

## Reproduction

```bash
# current upstream object, frozen
curl -sSL "https://raw.githubusercontent.com/monarch-initiative/dismech/946d496822e882893f97643332c72322a0455e8a/kb/disorders/WWOX-Related_Developmental_and_Epileptic_Encephalopathy.yaml" -o wwox.yaml
git hash-object wwox.yaml            # -> d61eff6b37de0c280908c269814b798065e32959
shasum -a 256 wwox.yaml              # -> 332e72e8897ad8a9618783c5e70a8f382ad3ba5b87bcad37ef30640265b0c1ff

# the pinned state, and the absence that v1 correctly measured
curl -s -o /dev/null -w "%{http_code}\n" "https://api.github.com/repos/monarch-initiative/dismech/contents/kb/disorders/WWOX-Related_Developmental_and_Epileptic_Encephalopathy.yaml?ref=c43343af4054eeeab847621eaab1e10da7efde84"   # -> 404

# the drift the green check does not report
python3 disease-models/wwox/analysis/scripts/dismech_independent_protocol.py verify-baseline   # -> PROTOCOL VERIFIED
python3 -c "import sys; sys.path.insert(0,'disease-models/wwox/analysis/scripts'); import dismech_independent_protocol as p; print(p.assert_exportable())"   # -> 1 UNRESOLVED_DRIFT on CLAIM 016

# zero receipts for the myelin arm's source
python3 -c "import json; print(sum(1 for l in open('disease-models/wwox/registries/fulltext_read_receipts.jsonl') if l.strip() and (json.loads(l).get('study_id') or {}).get('pmid')=='33914858'))"   # -> 0
```

## Related

[`dismech_export_spec.md`](dismech_export_spec.md) · [`dismech_phase3_dryrun_result.md`](dismech_phase3_dryrun_result.md) ·
[`dismech_independent_derivation_design.md`](dismech_independent_derivation_design.md) ·
[`../../../DISMECH_INTEGRATION.md`](../../../DISMECH_INTEGRATION.md) ·
[`../research/full_text_queue_current.md`](../research/full_text_queue_current.md) (FT-044) ·
[`../../../framework/eval/learned_gates_registry.md`](../../../framework/eval/learned_gates_registry.md) (`FREEZE_SCOPE_GATE`) ·
[`../../../framework/protocols/unattended_delegation_readiness.md`](../../../framework/protocols/unattended_delegation_readiness.md) (P1)
