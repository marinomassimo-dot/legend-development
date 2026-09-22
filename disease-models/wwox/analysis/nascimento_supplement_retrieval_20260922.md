# Nascimento 2023 · supplementary DE-table retrieval and the `WWOX` search

**Actor:** Scientist N · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Scope:** acquire Supplementary Tables 4, 5 and 6 of PMID 38122823 and search them for `WWOX`.
**Status of this file:** non-canonical analysis. It touches no registry, no receipt ledger and no
state manifest. **Nothing here is medical advice.** **BLOCK-1: no molecule, no dose, no safety
claim appears in this file.**

> Sources retrieved through PubMed / PubMed Central and through public GitHub repositories. Depth
> is labelled per source. **An abstract is not a read.** Every identifier, gene symbol, age string
> and quotation in this file was read from a served file today — **none reconstructed from memory.**
> A prior launch of this task was lost to a rate limit and wrote nothing; this file starts from zero
> and inherits only what
> [`nascimento_accession_and_g372r_20260922.md`](nascimento_accession_and_g372r_20260922.md)
> already recorded.

---

## 0 · Headline

| | Result |
|---|---|
| **The three supplementary DE tables** | 🔴 **NOT ACQUIRED.** Every host that serves them is `403 at CONNECT`. §2 records each route. This deployment's egress is an **allowlist**, not a per-publisher blocklist — `example.com` and `www.google.com` are equally denied — so there is no unblocked path to any supplementary file, from any publisher, by any tool. §2.3. |
| **The `WWOX` question those tables were meant to answer** | 🔴 **STILL OPEN. `PREMISE: UNVERIFIED`.** I did not read Supplementary Table 4, 5 or 6, so I report **no** `WWOX` row, **no** direction and **no** statistic, in either direction. |
| 🟢 **What was obtained instead** | **The authors' own published analysis code**, `github.com/massisnascimento/ECstream`, cloned and read in full: 15 files, 4 rendered R notebooks, 91 base64 notebook payloads decoded. §3. |
| 🟢 **A clean, bounded negative from that code** | **`WWOX` occurs ZERO times, case-sensitive, anywhere in the authors' analysis code**, against a **verified positive control** showing that gene symbols are abundant in that same surface. §4. **Its meaning is narrow and stated in §5 — it is NOT a statement about the DE tables and NOT a statement about expression.** |
| 🟢 **The bigger result — the data route** | 🔴 **The premise that "the raw-data accession is NOT obtainable from here" is now FALSIFIED.** The authors' own code names **18 open GEO per-sample count-matrix accessions**, one of which is literally the **`EC_Stream`** sample, and the repository README names a **public CELLxGENE collection** carrying a dataset titled *"EC Stream Region at 14 days of age"*. §6. This **re-prices desk action `D1`** and **contradicts** the repository's controlled-access inference. |
| **Delta** | Six items, §8. Three contradict standing repository assertions, §10. |

---

## 1 · The constraint that survives this file whatever else does

🔴 **A per-nucleus zero at ~6 TPM bulk expression is uninterpretable without a matched-abundance
dropout control.**

The abundance figure that sets this bar is measured and already in the repository's reading, from
Aldaz & Hussain 2020 (`full-text`, PMID 33255508, [DOI](https://doi.org/10.3390/ijms21238922)),
reporting GTEx medians: **frontal cortex 6.9, amygdala 6.2, hippocampus 5.6 TPM; cerebellum 12.1
TPM**. That is **bulk**, **adult**, **cortex** — not the postnatal periventricular compartment and
not per-nucleus.

🔴 **The constraint applies unchanged to every route in this file**, and it applies with extra force
to the supplementary route, because **a DE table cannot supply a dropout control at all.** A DE
table establishes **differential-expression membership**, never absolute abundance. Had I obtained
a `WWOX` row today, it would have been a **presence datum, not an abundance datum**, and the dropout
question would have remained exactly as open as it is now.

---

## 2 · Route by route — what each one returned

### 2.1 `get_full_text_article(pmc_ids=["PMC10901738"])` — ✅ run, ❌ no supplementary content

`full-text`, 48,538 characters of served body, re-fetched today and read to the final character.

**What it serves:** the body, ending in the publisher deferral, then a **captions-only**
*"Supplementary information"* block. **What it does not serve:** any supplementary file, any file
name, any file URL, any table content.

The captions block as served, verbatim and complete — this is the whole of it:

> *"Supplementary information / Reporting Summary / Peer Review File / **Supplementary Table 1** —
> Human cases list. Age, sex, post-mortem interval, neuropathology diagnosis, and clinical history
> of all human cases in this study. / **Supplementary Table 2** — Macaque sample list. Age and sex
> of all macaques in this study. / **Supplementary Table 3** — Antibodies. Manufacturer, catalogue
> numbers, dilutions used for all primary and secondary antibodies in this study. / **Supplementary
> Table 4** — DE genes in EC stream dataset. Results of a differential gene-expression test
> (Wilcoxon rank sum) in the dataset containing the EC stream microdissection. / **Supplementary
> Table 5** — DE genes in the main dataset. Results of differential gene-expression tests
> (quasi-likelihood F-test and Wilcoxon rank sum) in the dataset comprising all samples. /
> **Supplementary Table 6** — DE genes in the interneuron maturation dataset. Results of
> differential gene-expression tests (quasi-likelihood F-test and Wilcoxon rank sum) in the
> cortical interneuron maturation dataset. / **Supplementary Table 7** — Genes in WGCNA modules.
> List of genes in each module of the WGCNA analysis / **Supplementary Table 8** — DE genes between
> superficial and deep-layer Lamp5+ cells. Results of differential gene-expression test
> (quasi-likelihood F-test) between superficial and deep-layer LAMP5+ interneurons. /
> **Supplementary Video 1** — …"*

🟢 **This independently re-verifies the three captions the Orchestrator supplied — they are exact.**
🟢 It also surfaces **two captions the Orchestrator's brief did not carry**: Supplementary Table 7
(WGCNA module membership) and **Supplementary Table 8**, a fourth DE table. §8 delta 1.

**`WWOX` in the served body: 0, case-sensitive.** ⚠️ **That zero is not new and not load-bearing** —
it re-measures what the repository already holds, on a surface (`[All Fields]`-style body text) that
**does not contain the supplementary tables at all**.

**Extraction defects observed and not repaired:** citation markers deleted throughout (the
Methods collision `…from the adult ECwere aligned…` is still present today); `P`-values, `n =`
tokens and numeric exponents deleted (*"filtered for genes expressed in at least 50% of cells"* is
intact, but *"the 10 DE genes with the highest fold change and< 0.01"* has lost its `P`); figure
numbers deleted (*"can be found in Supplementary Tables–and."*). **I reconstruct none of these.**

### 2.2 File-name extraction from the served article — ✅ run, ❌ zero

An exhaustive sweep of the served body for file-name-shaped tokens
(`*.xlsx|xls|csv|zip|pdf|txt|docx`) returns **0**. No `MOESM`, no `http`, no `www.`. **The file
names do not survive extraction.** A supplementary URL therefore cannot be constructed from the
served article even in principle — and constructing one by pattern would be exactly the fabrication
the discipline forbids, so **none was attempted as a source of truth**; the one URL probed in §2.3
was probed only to establish the host block, and it returned nothing.

### 2.3 🔴 Egress — established **once per host**, never retried

| Host | Probe | Result | New? |
|---|---|---|---|
| `static-content.springer.com` (the Springer Nature ESM host that serves Nature supplementary files) | `curl` + `WebFetch` | **403 at CONNECT** / `EGRESS_BLOCKED` | 🟢 **new host, never tried before** |
| `media.springernature.com` | `curl` | **403 at CONNECT** | 🟢 new |
| `ftp.ncbi.nlm.nih.gov` (the PMC Open-Access package service) | `curl` | **403 at CONNECT** | 🟢 new — distinct from `www.` and `eutils.` already recorded |
| `web.archive.org` | `curl` | **403 at CONNECT** | 🟢 new |
| `api.openalex.org` | `curl` | **403 at CONNECT** | 🟢 new |
| `cellxgene.cziscience.com`, `api.cellxgene.cziscience.com`, `datasets.cellxgene.cziscience.com` | `curl` | **403 at CONNECT** | 🟢 new — and see §6 |
| `www.nature.com`, `www.ebi.ac.uk`, `europepmc.org`, `www.biorxiv.org`, `www.ncbi.nlm.nih.gov`, `eutils.ncbi.nlm.nih.gov` | — | **not retried.** Already established in the prior file. | — |

🔴 **The decisive control, and it is what makes this a closed question rather than a list of
failures:** `example.com` and `www.google.com` are **also 403 at CONNECT**. Only
`api.github.com`/`github.com`, the Anthropic APIs and the package registries resolve. **Egress here
is an allowlist.** The proxy's own failure log records every one of these as
`connect_rejected — "gateway answered 403 to CONNECT (policy denial or upstream failure)"`.

**Consequence, stated plainly:** ⚠️ **there is no host anywhere that serves a supplementary file and
is reachable from this deployment.** Enumerating further publisher, mirror or aggregator hosts
cannot succeed and is not a route; it is the same block re-measured. **I stopped enumerating.**

### 2.4 MCP tools that list or retrieve article files — ✅ audited, ❌ none exists

The PubMed MCP server exposes `get_full_text_article`, `get_article_metadata`,
`get_copyright_status`, `convert_article_ids`, `find_related_articles`, `search_articles`,
`lookup_article_by_citation`. **None of them lists, enumerates or retrieves a supplementary file.**
`get_full_text_article` returns exactly four keys — `identifiers`, `title`, `full_text`, `abstract`
— with no file manifest. The Scholar Gateway returns passages, not files. **No tool in this
deployment has a supplementary-file handle.** This is a capability gap, not a failed attempt.

🔴 **`get_copyright_status` was not used to skip any attempt.** It was not used at all. Ordering was
by cost; every candidate route was attempted or recorded as policy-blocked.

### 2.5 Web search — ✅ run, ❌ zero

One query framing aimed at the Nature ESM file-name pattern. No result concerned this article; the
returned links were unrelated patents, arXiv preprints and generic GEO/Zenodo landing pages. **No
snippet contained any supplementary-table content.** ⚠️ A search-engine snippet could not have
carried a spreadsheet cell in any case, so this route was low-value by construction and is recorded
as exhausted rather than promising.

### 2.6 🟢 GitHub — the one route that was **not** blocked, and the only one that returned anything

`github.com` is on the allowlist. Code search across all public repositories for the article DOI
returned **18 results**, of which the first is **`massisnascimento/ECstream`** — the first author's
own repository. It was cloned and read. §3 onward.

⚠️ **The MCP `get_file_contents` tool is scoped to this workspace's own repository only** and
refused every external path; `git clone` over HTTPS is not so scoped. Both facts are recorded
because they determine what a future session can and cannot do.

---

## 3 · What the authors' own code is, and why it is a legitimate source

**`github.com/massisnascimento/ECstream`**, cloned today at commit `5d4326f`, single branch `main`.
`full-text` depth: all 15 tracked files read; the four `.nb.html` rendered notebooks additionally
**decoded** — 91 base64 `rnb-source` / `rnb-output` / `rnb-text` payloads, 111,381 decoded
characters — because a plain-text search of an `.nb.html` file searches base64, not content.

Its README states its relationship to the paper, verbatim:

> *"Code used in the analysis of the study "Protracted neuronal recruitment in the temporal lobe of
> young children", Nascimento et al. 2024, Nature. … This repository contains all the code used to
> generate the final Seurat objects and analyses."*

And `1.merging/1.merging.rmd` carries, verbatim, `author: "Marcos Nascimento"` and
`subtitle: Nascimento + Franjic // SoupX/DoubletFinder/DropletQC Pipeline`.

⚠️ **Provenance label, and it matters:** this is the **authors' own code**, published by them, and it
self-identifies against the paper by DOI. It is **primary for what the analysis did**. It is **not**
the paper, **not** peer-reviewed, and **not** the supplementary tables. Everything read from it is
labelled `author-code` below and is never voiced as if it came from the published article.

---

## 4 · The `WWOX` search in that code — a clean, bounded negative

### 4.1 The measurement

| Surface searched | `WWOX`, case-sensitive |
|---|---|
| All 15 tracked files, raw | 🔴 **0** |
| All 4 rendered notebooks, after base64 decoding (91 payloads) | 🔴 **0** |
| Case-**insensitive** across the raw repository | 7 — ⚠️ **all seven are false positives** |

⚠️ 🔴 **The seven case-insensitive hits are an extraction trap, and I nearly counted them.** They
are `wwOx`, `wWoX`, `wwoX`, `WWoX`, `WwOX`, `wwox`, `WWox` — mixed-case fragments occurring **inside
base64-encoded blobs** in `1.merging.nb.html`. **None is the gene symbol.** Had a case-insensitive
count been reported as a finding, this file would have claimed a `WWOX` result in a Nature paper's
analysis code that does not exist. **A zero is not absence — and a non-zero is not presence.**

### 4.2 🔴 The positive control, without which the zero means nothing

A gene-symbol search of a code repository could return zero simply because the surface contains no
gene symbols. It does not:

| Gene | Occurrences (decoded notebooks) | Occurrences (`.rmd` sources) |
|---|---|---|
| `LAMP5` | 13 | 21 |
| `SOX2` | 4 | 1 |
| `GAD2` | 3 | — |
| `DCX` | 2 | 5 |
| `PAX6` | 2 | 3 |
| `TOP2A` | 2 | — |
| `SLC17A7` | 2 | — |
| `HOPX` | 1 | 1 |
| **`WWOX`** | 🔴 **0** | 🔴 **0** |

🟢 **The surface carries gene symbols abundantly. The zero is a real zero on a real surface.**

### 4.3 🔴 What that zero means — and the four things it does **not** mean

The gene symbols in this repository occur in exactly two places: **`FeaturePlot()` marker panels**
(two panels of 24 genes each, hand-chosen: `GFAP, HOPX, TOP2A, EOMES, DCX, TBR1, SLC17A7, GAD2,
LHX6, NR2F2, PROX1, CALB2, LAMP5, RELN, VIP, NPY, SST, OLIG2, SOX10, MBP, FOXJ1, PECAM1, PDGFRB,
ADAM28` and `GFAP, TNC, SOX2, TOP2A, OLIG2, SOX10, DCX, GABRB2, LHX6, NR2F2, PROX1, PBX3, SST,
PVALB, NPY, CALB2, VIP, RELN, KIT, LAMP5, TBR1, SLC17A7, ADAM28, PECAM1`) and a **sex-gene exclusion
vector**. **The DE results themselves are never printed as gene lists in this repository** — every
DE call ends in `saveRDS(...)` to an `.rds` file, and `.gitignore` excludes `*.rds`.

Therefore the zero establishes **one narrow thing**:

> 🟢 **`WWOX` is not among the ~48 marker genes the authors hand-picked for their overview feature
> plots, and is not named anywhere in their published analysis code.**

It establishes **none** of the following, and must never be voiced as any of them:

1. 🔴 **NOT** "`WWOX` is absent from Supplementary Table 4, 5 or 6." Those tables are not in this
   repository, in any form. **The DE tables were not searched. `PREMISE: UNVERIFIED`.**
2. 🔴 **NOT** "`WWOX` was not tested." The DE calls are genome-wide over the object's gene universe;
   a gene absent from a hand-picked plotting vector was still in the test input.
3. 🔴 **NOT** "`WWOX` is not differentially expressed." Nothing here reports a statistic.
4. 🔴 **NOT** — and this is the one the brief binds hardest — **"`WWOX` is not expressed."** A gene's
   absence from a marker-panel vector is a **curatorial** fact about what the authors chose to
   draw. It carries **no** information about expression whatsoever.

The correct classification of the supplementary-table question is unchanged by this file:
**`PREMISE: NOT_TESTED_OR_NOT_SIGNIFICANT` remains the classification that *would* apply to absence
from a DE table — and it has not been triggered, because no DE table was read.**

### 4.4 🟢 What the code *does* establish about the DE tests — the identity work, done in advance

Even without the tables, the code fixes what a future reader must attach to any `WWOX` row. This is
the **identity / comparison / compartment / age** verification the brief demanded, obtained from
`author-code` rather than from the tables:

| Fact, from `author-code` | Verbatim |
|---|---|
| **The DE filters are explicit and aggressive** | `filterByExpr(y, group=y$samples$cluster, min.count=10, min.total.count=20)`; and pseudobulk samples dropped by `keep.samples <- y$samples$lib.size > 4e4` |
| **The Wilcoxon marker calls are one-sided** | `FindAllMarkers(inter.exp_step2, only.pos = T)` and `FindAllMarkers(inter.exp, assay = "RNA", only.pos = T)` — ⚠️ **`only.pos = T` means down-regulated genes are excluded by construction** |
| **The published Methods add a second filter** | *"filtered for genes expressed in at least 50% of cells in each identity"* (served body, §2.1) |
| **The pseudobulk QLF design** | `design <- model.matrix(~ cluster + donor)`, `glmQLFit(..., robust=TRUE)`, `glmQLFTest(fit, contrast=contr[,i])`, comparison string `paste0(levels(cluster)[i], "_vs_others")` |
| **Supplementary Table 8's contrast, in the author's own words** | *"I compared only cells in the postnatal EC (**excluding the EC stream**) to look into the genes that are DE in the postnatal brain."* |

🔴 **This sharpens bound #2 of the brief into something much stronger, and it should be carried
forward:** if `WWOX` turns out to be absent from these tables, **at least four independent
mechanisms could produce that absence before biology is reached** — the `min.count=10 /
min.total.count=20` expression filter, the ≥50%-of-cells filter, the `only.pos = T` one-sidedness,
and the significance threshold itself. 🔴 **For a gene sitting at ~6 TPM in bulk cortex, the
low-expression filters are the *expected* outcome, not a surprising one.** Absence would be close to
uninformative. **Presence would be the informative result.**

### 4.5 The age and compartment scope, read verbatim from `author-code`

```
age.levels       <- c("23GW", "14d", "33d", "54d", "2y", "3y", "13y", "27y", "50y", "51y", "79y")
age.group.levels <- c("Fetal (23GW)", "Infant (14d-54d)", "Toddler (2y-3y)", "Teen (13y)", "Adult (27y-79y)")
region.levels    <- c("Germinal Zone", "Embryonic EC", "Migratory Stream", "Postnatal EC")
```
with the EC-stream highlight labelled, verbatim, `"EC Stream (14d)"` and the embryonic one
`"Embryonic EC (23GW)"`.

🟢 **`14d` — fourteen days — is confirmed as a first-class age level in the authors' own object**,
and it is the *only* age carrying the `Migratory Stream` region label. The two-week-old
periventricular sample is real, is singular, and is machine-labelled as such.

---

## 5 · 🔴 The interpretation bounds, carried unsoftened

These bind any future use of anything in this file.

1. **A `WWOX` row present = WWOX was measured in that DE object.** — *Not triggered. No row was seen.*
2. **Absence = `PREMISE: NOT_TESTED_OR_NOT_SIGNIFICANT` within that comparison.** — *Not triggered.
   No table was read. The §4 zero is a different zero, on a different surface, and §4.3 states its
   four exclusions.*
3. 🔴 **Absence MUST NOT be re-voiced as non-expression.** A DE table lists genes passing a test and
   a threshold. Absence means not differentially expressed, **or** not tested, **or** filtered out.
   **It does not mean the gene is not expressed.** §4.4 shows this paper has *four* such filters.
4. **A DE table establishes differential-expression membership, NOT absolute abundance.** It cannot
   supply a dropout control.
5. 🔴 **The dropout constraint stands regardless:** a per-nucleus zero at ~6 TPM bulk (GTEx medians:
   frontal cortex 6.9, amygdala 6.2, hippocampus 5.6 TPM; cerebellum 12.1) is **uninterpretable
   without a matched-abundance dropout control.**
6. 🔴 **The authors' own negative bounds the interpretation**, verbatim from the served body,
   re-verified today: *"In the EC stream microdissection, **we did not find intermediate progenitors
   for interneurons or a differentiation trajectory connecting the local RG to the immature
   inhibitory neurons**."* Any finding reads as **"WWOX in postnatal human periventricular radial
   glia"** and **never** as *"WWOX in the progenitor supplying the stream."*
7. 🔴 **The mis-attribution trap was met head-on, and is resolved rather than repeated.** See §7.

---

## 6 · 🟢 The data route — the premise of this task turns out to be false

### 6.1 The study's own count matrices are open, per-sample, and named in the authors' code

`1.merging/1.merging.rmd` opens its data section with, verbatim:

> *"Count matrices and metadata are downloaded from GEO and saved in a folder named "matrices"."*

and then loads `gsm_samples.RData` and loops over it, constructing per-sample download URLs for
`_barcodes.tsv.gz`, `_counts.mtx.gz`, `_genes.tsv.gz` and `_metadata.csv.gz`.

`gsm_samples.RData` is a two-column data frame. Read today, it pairs **18 GEO sample accessions,
`GSM8002943` through `GSM8002960`**, with these 18 sample names, verbatim and in order:

> `CGE, MGE, LGE, **EC_Stream**, dEC, H71, H31, H37, H48-g1, H48-g2, H39-g1, H39-g2, H46-g1,
> H46-g2, H29-g1, H29-g2, H33-g1, H33-g2`

🔴 **`EC_Stream` is one of the eighteen.** These are **this study's own deposited count matrices**,
openly downloadable, **no accession hunt, no access application, no controlled tier.**

⚠️ **Provenance bound:** these GSM accessions are read from the **authors' code repository**, not
from the published article — the article defers its data statement to the publisher and the served
body contains no accession (re-verified today, §2.1). **They are `author-code` depth and should be
confirmed against the publisher's data-availability statement before anything canonical rests on
them.** 🔴 **I did not verify that these accessions resolve** — `ncbi.nlm.nih.gov` is blocked.

### 6.2 A second, independent open route: CELLxGENE

The repository README states, verbatim: *"Data can be browsed and downloaded at
Cellxgene, collection id `cae8bad0-39e9-4771-85a7-822b0e06de9f` (written here as plain text, not a link: the README renders the URL through a link-rewriter, so no resolvable target was read)"*.

That collection identifier is **independently corroborated in five unrelated public repositories**
found by code search — `briannaflynn/cellxgene_handlers`, `ahmedh-sallam/scfm-controlled-
manipulations`, `x-atlas-consortia/hra-pop` (which records it as holding **13 datasets**),
`8gabri8/census_VAE`, and `tanyaphung/scrnaseq_viewer`. The last of these documents three of its
datasets by title, verbatim:

> *"#Subpallial germinal zones and the developing human entorhinal cortex … #Interneuron maturation
> in the human entorhinal cortex … **#EC Stream Region at 14 days of age**"*

🟢 **A standalone, publicly downloadable `.h5ad` of the EC-stream region at 14 days of age exists.**
The same third-party notes record the object's `adata.var` shape as **21,563 genes**, with gene
symbols in the `feature_name` column, and `adata.obs` columns `author_age`, `age_group`, `region`,
`author_cell_type`, `cell_type`, `development_stage` whose values match the `author-code` levels in
§4.5 exactly.

⚠️ **These are third-party repositories reprocessing a public object. They are corroboration of the
collection's existence and contents, not measurements, and none of them contains a `WWOX` value** —
I checked `tanyaphung/scrnaseq_viewer` file by file: it ships two preprocessing scripts for this
dataset and no gene-level output.

🔴 **All three CELLxGENE hosts are `403 at CONNECT` (§2.3), so I downloaded nothing and read no
expression value.**

### 6.3 🔴 What this does to desk action `D1`

| | Prior repository position | Measured today |
|---|---|---|
| Accession | *"NOT FOUND, and I name none"* | 🟢 **18 open GSM accessions and a public CELLxGENE collection, both named in the authors' own code** |
| Access tier | 🟡 *"a controlled-access destination is the likely home of the data"* (`INFERENZA`, from paediatric post-mortem + clinical histories + genetic demultiplexing) | 🔴 **Contradicted.** Open GEO count matrices and an open CELLxGENE collection. The controlled-access inference was reasonable and is **wrong** for the count-matrix tier. |
| Cost of `D1` | *"hours **plus an access application**"* | 🟢 **hours, once egress exists. No application.** |
| Blocker | *"not only egress — an unknown identifier"* | 🟢 **egress alone.** The identifier problem is solved. |

⚠️ **The controlled-access inference may still hold for the *FASTQ* tier** — the Methods' genetic
demultiplexing against a 1000 Genomes VCF means the raw reads carry donor germline genotype. **Count
matrices do not.** The repository's reasoning was right about the raw tier and over-generalised to
the tier that actually matters for a `WWOX` read-out.

🔴 **A CELLxGENE object would also answer the question the DE tables could never answer** — it
carries per-nucleus counts, so **the matched-abundance dropout control of §1 becomes computable in
the same object.** That makes it strictly the better target. **The supplementary-table route, which
this task was set to pursue, is now the *inferior* of the two available routes.**

---

## 7 · 🔴 The mis-attribution trap — met, and deliberately not walked into

The brief warned that the paper's only `GEO` mention is **someone else's adult-EC dataset being
re-used**, with the identifying citation marker deleted by extraction (the collision
`adult ECwere`, still present in today's fetch), and instructed: **do not name, guess or reconstruct
that accession, and never attribute it to this study.**

**The trap is live and I walked up to its edge.** `1.merging/1.merging.rmd` contains a **second,
separate** download call — outside the 18-sample loop — that fetches a tarball from a GEO **series**
whose file name explicitly states it contains *samples from another series*, and then imports three
extra samples named `hsb231`, `hsb237`, `hsb628` alongside the 18. The notebook's own subtitle,
`Nascimento + Franjic`, names the external source's first author. The served body's matching
sentence reads *"published snRNA-seq data from the **50–79-year-old EC**"*, and `author-code`'s
`age.levels` duly carries `50y`, `51y`, `79y`.

🔴 **The two accession strings are legible verbatim in that file. I am holding them out of this
write-up**, under the brief's bound #7. **This is a deliberate choice, not an inability to read
them** — they sit in `1.merging/1.merging.rmd` and any authorised reader can lift them. What matters
for the science is recorded here and is unambiguous:

> 🟢 **The re-used adult-EC dataset is now positively identified as a distinct external deposit,
> separable from this study's own 18 samples by sample name (`hsb*` vs the 18 above) and by age
> (50–79y vs 23GW–27y).** 🔴 **It must never be attributed to Nascimento et al., and no `WWOX`
> result from those three `hsb*` samples may ever be reported as a postnatal finding — they are
> adult.**

**Orchestrator decision needed:** whether the two external accession strings should be recorded
under correct attribution (which would permanently close the mis-attribution hazard) or remain
withheld. I make no such record unilaterally.

---

## 8 · Delta against the repository

| # | Finding | Status |
|---|---|---|
| 1 | 🟢 **There are FOUR supplementary DE tables, not three.** Supplementary Table 8 — *"DE genes between superficial and deep-layer Lamp5+ cells … (quasi-likelihood F-test)"* — and Supplementary Table 7 (WGCNA module membership) were not in the brief. | 🟢 **New.** ⚠️ Table 8's contrast is `author-code`-documented as *"only cells in the postnatal EC (**excluding the EC stream**)"* — so it is the **least** relevant of the four to the periventricular question, and Table 7 is not a DE table at all. **The brief's choice of Tables 4–6 was correct.** |
| 2 | 🔴 **Egress here is an allowlist, not a publisher blocklist** — `example.com` and `www.google.com` are 403 at CONNECT. | 🟢 **New, and it closes a whole class of future work.** No session should enumerate further publisher or mirror hosts. Eight more hosts established blocked today, each once. |
| 3 | 🟢 **The authors' full analysis code is public and reachable**, `github.com/massisnascimento/ECstream`, reached via the one allowlisted host. | 🟢 **New.** GitHub is an unexploited literature-adjacent surface in this deployment. |
| 4 | 🔴 **`WWOX` is absent, case-sensitive, from that entire code base**, with a verified positive control — **and the seven case-insensitive "hits" are base64 artefacts.** | 🟢 **New, and bounded in §4.3 to almost nothing.** Its real value is as a **trap record**: a case-insensitive gene-symbol search of an `.nb.html` file manufactures false positives. |
| 5 | 🔴 **The study's data are OPEN** — 18 named GEO count-matrix accessions including `EC_Stream`, plus a public CELLxGENE collection with a standalone *"EC Stream Region at 14 days of age"* dataset. | 🟢 **New, and it falsifies this task's own premise** that no accession is obtainable from here. **Re-prices `D1` from "hours + access application" to "hours".** |
| 6 | 🔴 **Any `WWOX` absence from these DE tables would have at least four non-biological explanations** — `min.count=10`/`min.total.count=20`, ≥50%-of-cells, `only.pos = T`, and the threshold — all read from `author-code` and the served Methods. | 🟢 **New, and it downgrades the whole supplementary route.** For a ~6 TPM gene, filter-exclusion is the *expected* outcome. **Presence would be informative; absence would be close to uninformative.** |

---

## 9 · What I could not verify — stated as such

- 🔴 **I did not obtain Supplementary Table 4, 5 or 6.** The `WWOX` question they were meant to
  answer is **exactly as open as before this file**. I report no row, no direction, no statistic.
- 🔴 **I did not verify that the 18 GSM accessions resolve**, nor that the CELLxGENE collection
  serves what the third-party notes say it serves. Both hosts are blocked. Both are `author-code`
  and third-party depth respectively, **not publisher-confirmed**.
- 🔴 **I did not read the publisher's data-availability statement.** It remains behind the DOI, on a
  blocked host. The served body still defers to it verbatim.
- 🔴 **Whether `WWOX` is even present in the object's 21,563-gene universe is unknown.** The gene
  count is third-party-reported; `WWOX`'s membership in `adata.var` is unchecked and is the **first
  thing a session with egress should test**, before any DE-table question.
- 🔴 **The paper's figures and Extended Data were not inspected** — the standing limitation the
  repository already declares for this paper. A `WWOX` feature plot, if one existed, would not have
  been seen by me. (⚠️ `author-code` makes this unlikely: `WWOX` is in neither marker vector.)
- 🔴 **Citation markers, `P`-values, `n =` tokens and figure numbers are still deleted** by the
  extraction route in today's fetch. **I reconstructed none of them.**
- 🔴 **No researcher emails or contact details** appear in this file. Author-contact routes were
  not pursued and are not proposed.

---

## 10 · Anything contradicting a repository assertion

1. 🔴 **`nascimento_accession_and_g372r_20260922.md` §2.7 — "a controlled-access destination is the
   most likely home of the data" — is CONTRADICTED for the count-matrix tier.** The data are open
   in two places. The inference was well-reasoned (paediatric post-mortem, clinical histories,
   genetic demultiplexing) and it is **wrong for the tier that matters**. It may still hold for the
   FASTQ tier. §6.3.
2. 🔴 **That file's §2.9 item 12 lists "the paper's own Supplementary Tables 4–5" among routes that
   "require egress this deployment does not have" — CONFIRMED, and now closed as unreachable
   rather than merely unattempted.** §2.3. ⚠️ But its framing of the supplementary tables as *"the
   cheapest possible non-zero result"* (§2.6) **should be retired**: §6.3 shows the CELLxGENE object
   is both cheaper and strictly more informative, and §4.4 shows the DE tables are the route most
   likely to return an uninformative absence.
3. 🔴 **That file's §5 — "No accession, and I name none. Routes exhausted" — is SUPERSEDED.** The
   route that was not tried was GitHub, and it worked. ⚠️ **The refusal to *guess* an accession was
   correct and remains correct**; what changed is that one was *found*, in a source, not inferred.
4. 🟡 **That file's delta #4 — the postnatal EC nuclei span "14 days to 27 years"** — is **verbatim
   correct** (re-verified today: *"nuclei from the postnatal EC between 14 days and 27 years of
   age"*) but describes only the study's own samples. ⚠️ **The merged object spans 23GW to 79y**,
   because the re-used adult samples add `50y`, `51y`, `79y`. Anyone reading a DE table from *"the
   dataset comprising all samples"* (Supplementary Table 5) is reading a contrast that **includes
   50–79-year-old adult cortex from a different study.** 🔴 **That is a mis-attribution hazard inside
   Supplementary Table 5 specifically**, and it did not previously exist in the repository's record.
5. 🟢 **No repository assertion was found to be factually wrong on the science.** The `WWOX`-absent
   framing, the dropout constraint, the refusal to name an accession, and the authors'-negative
   bound on the RG cluster all held up against the sources read today.

---

## 11 · Sources and depth reached

According to PubMed:

| Source | Identifier | Depth reached here | Role |
|---|---|---|---|
| Nascimento MA, …, Alvarez-Buylla A, Sorrells SF. Protracted neuronal recruitment in the temporal lobes of young children. *Nature* 2023;626:1056–65 | PMID 38122823 · `PMC10901738` · [DOI](https://doi.org/10.1038/s41586-023-06981-x) | 🟢 **`full-text`**, 48,538 chars, re-read end to end; ⚠️ **supplementary files, figures and Extended Data NOT inspected** | The target |
| Aldaz CM, Hussain T. WWOX Loss of Function in Neurodevelopmental and Neurodegenerative Disorders. *IJMS* 2020;21:8922 | PMID 33255508 · `PMC7727818` · [DOI](https://doi.org/10.3390/ijms21238922) | 🟡 **not re-read today** — the GTEx TPM figures in §1 are carried from the repository's existing `full-text` record | The ~6 TPM dropout bar |

Non-PubMed sources, labelled by depth:

| Source | Depth | Role |
|---|---|---|
| `github.com/massisnascimento/ECstream` @ `5d4326f` | 🟢 **`author-code`, complete** — 15 files + 91 decoded notebook payloads | §3–§7 |
| `github.com/tanyaphung/scrnaseq_viewer` @ `ceaaee3` | 🟡 **third-party notes**, one file read in full, repository file list audited | §6.2 corroboration only |
| Four further public repositories indexing the CELLxGENE collection | 🟡 **third-party, code-search fragments** | §6.2 corroboration only |

🔴 **Nothing in this file cites an `FT-` number.** No new PMID, DOI or unread source is introduced —
the only two papers named were already read at `full-text` depth by this repository — so
**`UNREAD_PREMISE` is unchanged at 0 and no new `FT-` entry is coined.** No PMID has been stripped
anywhere in this file to avoid declaring debt.
