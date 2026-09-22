# Nascimento 2023 data accession · and the `G372R` protein-level arbitration

**Actor:** Scientist L · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Scope:** two tasks, in priority order. (1) Locate the data accession for PMID 38122823 so that the
proposed WWOX read-out becomes a desk analysis. (2) Arbitrate the two-source disagreement about
`G372R` WWOX protein level.
**Status of this file:** non-canonical analysis. It touches no registry, no receipt ledger and no
state manifest. Nothing here is medical advice.

> Sources retrieved through PubMed / PubMed Central. Depth is labelled per source: `full-text`
> means a served body was read; `abstract-depth` means an abstract only. **An abstract is not a
> read.**

---

## 0 · Headline, both tasks

| | Result |
|---|---|
| **Task 1 — accession** | 🔴 **NOT FOUND, and I name none.** Every route reachable from this deployment is exhausted and listed in §2. The data-availability statement is **not in the PMC body as served** — it is deferred, verbatim, to the publisher DOI, which is 403 at CONNECT. No citing or reanalysing paper reachable from here names it. **No accession is guessed, constructed or pattern-matched.** |
| **Task 1 — partial win** | 🟢 A **cheaper route to a partial answer that does not need the accession at all**: the paper ships **Supplementary Tables 4 and 5, which are differential-expression gene tables over the EC-stream dataset and over the whole dataset**. A `WWOX` row in either is a WWOX measurement in this object, obtainable from a free supplementary file rather than from raw data. §2.6. |
| **Task 2 — verdict** | **Option (2), with option (1) as the bounded fallback. Option (3) is excluded.** The Aldaz & Hussain sentence is **not a measurement**; it is a review sentence describing Mallaret 2014, and it extends to `G372R` a fibroblast result that the repository's own held verbatim documents **for `P47T` only**. §3. |
| **Task 2 — consequence** | 🔴 **`DL-MECH-037`'s `G372R` row must NOT be flipped to "protein normal", and the burial argument must NOT be simplified on this evidence.** Doing so would overturn a *measured* immunofluorescence result on the strength of a *review sentence* whose primary body nobody in this repository has read at complete depth. §3.5. |

---

## 1 · The constraint that must survive this file whatever else does

🔴 **A per-nucleus zero at ~6 TPM bulk expression is uninterpretable without a matched-abundance
dropout control.**

Any reanalysis that reads `WWOX` out of the Nascimento single-nucleus object — or out of any
snRNA-seq object — **must carry that control, or it produces nothing.** Concretely: at least one
control gene of matched bulk abundance in the same tissue, with the same capture chemistry, whose
per-nucleus detection rate is reported alongside `WWOX`'s. Without it, a `WWOX` count of zero in a
radial-glia cluster is indistinguishable from dropout, and the analysis yields no interpretable
result in either direction.

The abundance figure that sets this bar is measured and in the repository's reading already, from
Aldaz & Hussain 2020 (`full-text`, PMID 33255508, [DOI](https://doi.org/10.3390/ijms21238922)),
reporting GTEx medians verbatim:

> *"cerebellum is the CNS structure with the highest expression levels in adults (median = 12.1 TPM)
> and the expression of this gene is observed throughout the various CNS tissues with the frontal
> cortex, amygdala, and hippocampus expressing 57–46% of the levels seen in the cerebellum (median
> for FC = 6.9, AMY = 6.2, HIP = 5.6 TPM)."*

That is **bulk** tissue, **adult**, **cortex** — not the postnatal periventricular compartment and
not per-nucleus. It is the right order of magnitude for sizing the dropout risk and nothing more.

**A zero is not absence.** This applies to the planned reanalysis exactly as it applies to the
query-count zeros in §2.

---

## 2 · Task 1 — the accession hunt, route by route

### 2.1 What the served body actually contains

PMID 38122823 — Nascimento MA, …, Alvarez-Buylla A, Sorrells SF. *Protracted neuronal recruitment in
the temporal lobes of young children.* *Nature* 2023;626(8001):1056–1065.
[DOI](https://doi.org/10.1038/s41586-023-06981-x) · `PMC10901738` · **`full-text`, re-fetched today**,
48,538 characters of served body, read to the final character including everything after the
references.

The body **ends** with this, verbatim:

> *"Any methods, additional references, Nature Portfolio reporting summaries, source data, extended
> data, supplementary information, acknowledgements, peer review information; details of author
> contributions and competing interests; and **statements of data and code availability are available
> at 10.1038/s41586-023-06981-x**."*

🔴 **That is the whole data-availability statement in the PMC body: a pointer to the publisher.** It
is not a truncation artefact and it is not beyond where a previous reader looked — it is the last
substantive sentence before the supplementary-file captions.

Exhaustive token sweep over the served body, all zero hits except as noted:

| Token searched | Hits in served body |
|---|---|
| `GSE` | 🔴 **0** |
| `phs` / `dbGaP` | 🔴 **0** |
| `EGA` | 🔴 **0** |
| `accession` | 🔴 **0** |
| `deposit` / `Deposit` | 🔴 **0** |
| `Zenodo` / `figshare` / `Synapse` / `cellxgene` / `NeMO` / `BICCN` | 🔴 **0** |
| `github` | 🔴 **0** |
| `availabil` | 1 — the deferral sentence above |
| `GEO` / `Gene Expression Omnibus` | 1 — **and it is not their own deposit**; see §2.2 |
| `http` / `www.` | 🔴 **0** |
| `10.` (DOI-like) | 3 — two **protocols.io** protocol DOIs (`10.17504/…`) and the article's own DOI. Protocols, not data. |

### 2.2 🔴 The one GEO mention in the paper is a trap — do not misread it

Verbatim, Methods:

> *"FASTQ files generated in this study and those **retrieved from the Gene Expression Omnibus (GEO)
> from a previous study from the adult EC** were aligned and pre-processed using the same workflow."*

This is the **adult 50–79-year-old EC dataset they re-used from someone else**, not their own
deposit. ⚠️ **And the reference marker identifying that previous study has been deleted by the
extraction route** — the served text reads `…from the adult ECwere aligned…`, with the superscript
citation silently removed. **Therefore I cannot name which adult-EC accession that is, and I do
not.** Any reader who pattern-matches a plausible adult-EC `GSE` number onto this sentence sends a
reanalysis to the wrong dataset, which is the precise failure mode the discipline forbids.

This is the **GEO-accession-deletion hazard operating live**, in the very paper where it matters
most. It is also the reason a *negative* token sweep on this body cannot fully exclude that an
accession was present and was deleted — though the deferral sentence in §2.1 makes deletion the
less likely explanation, because Nature-portfolio PMC deposits routinely carry no
data-availability section at all.

### 2.3 Egress — established once, not retried

| Host | Result | Established |
|---|---|---|
| `www.nature.com` | `EGRESS_BLOCKED` | today, first attempt |
| `www.ebi.ac.uk` (Europe PMC REST full-text XML) | `EGRESS_BLOCKED` | today, and already in the proxy's own recent-failure log |
| `europepmc.org` | `EGRESS_BLOCKED` | today |
| `www.biorxiv.org` (the preprint — see §2.4) | `EGRESS_BLOCKED` | today |
| `www.ncbi.nlm.nih.gov`, `eutils.ncbi.nlm.nih.gov`, `www.proteinatlas.org`, `www.brainspan.org`, `gtexportal.org` | 403 at CONNECT | already in the proxy log from earlier today; **not retried** |

The proxy status endpoint confirms the pattern is policy denial at CONNECT, not TLS or tooling. The
only readable literature routes from here are the PubMed MCP server, the Scholar Gateway and web
search snippets. All three were used.

### 2.4 The preprint route — identified, and blocked

A preprint of this work exists and is a distinct document:

> *"Persistent postnatal migration of interneurons into the human entorhinal cortex"* — bioRxiv
> `10.1101/2022.03.19.484996`, authors including Nascimento, Biagiotti, Herranz-Pérez,
> Alvarez-Buylla and Sorrells.

Surfaced by web search; **`www.biorxiv.org` is `EGRESS_BLOCKED`**, and bioRxiv preprints are not
deposited in PMC, so `get_full_text_article` has no handle on it. 🟢 **This is the single most
promising unexhausted route for anyone with egress**: preprint data-availability statements are
frequently more explicit than the journal version's, and this one predates the Nature deferral
convention. It is recorded here as a named next action, not as a result.

### 2.5 Citing and reanalysing papers — four checked, none names it

| Paper | Depth reached | `GSE`/`phs`/`EGA` in body | Names Nascimento's accession? |
|---|---|---|---|
| PMID 40659844 — *An expanded subventricular zone supports postnatal cortical interneuron migration in gyrencephalic brains*, *Nat Neurosci* 2025, `PMC12321571`, [DOI](https://doi.org/10.1038/s41593-025-01987-2) — **same lineage of groups** | `full-text`, 55,611 chars | 🔴 **0** | 🔴 **No.** Its own data-availability statement is deferred to the publisher in the identical Nature-portfolio pattern. Its reference markers are also deleted, so it does not even render the Nascimento citation as text. |
| PMID 41659519 — *A Single-Cell and Spatial 3D Multi-omic Atlas of Developing Human Basal Ganglia and Inhibitory Neurons*, `PMC12874046`, [DOI](https://doi.org/10.64898/2026.01.28.702385) | `full-text` | 🔴 **0** | 🔴 **No** — the string `Nascimento` does not occur in the served body at all. |
| PMID 41538440 — *Subventricular zone radial glial cells maintain inhibitory neuron production in the human brain*, *Science* 2026 | metadata only | — | 🔴 **Unreachable.** `convert_article_ids` returns **no PMCID**; the publisher host is blocked. Recorded as an unexhausted route. |
| Scholar Gateway passages citing Nascimento (two review/primary papers, `ejn70136`, `cne70130`) | passage-depth | accessions present but **belonging to other studies** | 🔴 **No.** Each cites Nascimento only in prose about postnatal migration. |

⚠️ **The accessions that surfaced in Scholar Gateway passages are other papers' deposits.** I list
none of them against Nascimento. A `GSE` number that appears in the same search result as a paper is
not that paper's accession, and treating it as one is exactly the fabrication the task forbids.

### 2.6 🟢 The route that does not need the accession

The served body's supplementary-file captions name, verbatim:

> *"**Supplementary Table 4** — DE genes in EC stream dataset. Results of a differential
> gene-expression test (Wilcoxon rank sum) in the dataset containing the EC stream microdissection."*
>
> *"**Supplementary Table 5** — DE genes in the main dataset. Results of differential gene-expression
> tests (quasi-likelihood F-test and Wilcoxon rank sum) in the dataset comprising all samples."*

**A `WWOX` row in Supplementary Table 4 or 5 is a WWOX measurement in this object**, with a fold
change and a test statistic, obtainable from a **free supplementary file** — no accession, no raw
data, no controlled-access application. It answers less than a full reanalysis (a DE table reports
genes that passed a test, so `WWOX`'s absence from it is **not** evidence of non-expression — it is
`PREMISE: NOT_TESTED_OR_NOT_SIGNIFICANT`), but it is the cheapest possible non-zero result.

🔴 **The dropout constraint of §1 applies to this route too, in a modified form:** a DE table cannot
supply a matched-abundance dropout control, so a `WWOX` row found there bounds nothing about
per-nucleus detectability. It would be a presence datum, not an abundance datum.

This refines the repository's existing desk action **D5** in
`wwox_postnatal_svz_expression_20260922.md`, which correctly anticipated a supplementary-table
route; what is added here is **which two tables**, by caption, and why `WWOX`-absent is
uninterpretable.

### 2.7 Why a controlled-access deposit is the most likely destination — labelled as inference

🟡 **`INFERENZA`, not measured.** Three facts from the served Methods, verbatim or near, point this
way:

- *"Fifty-three post-mortem specimens and two post-operative neurosurgical resections were collected
  for this study"*, under four named human-subjects protocols across UCSF, Hospital la Fe /
  University of Valencia, and the University of Pittsburgh (CORID, plus IRB consents with HIPAA
  authorizations signed by parents or guardians).
- Supplementary Table 1 is a *"Human cases list. Age, sex, post-mortem interval, neuropathology
  diagnosis, and clinical history of all human cases in this study."*
- Demultiplexing was **genetic**: *"Freemuxlet, a genetic demultiplexing tool in the popscle suite
  … a customized VCF file from the 1000 genomes data … as a reference for SNPs."* The libraries
  therefore carry donor-identifying germline genotype.

Paediatric post-mortem brain with clinical histories, plus genotype-bearing libraries, is the profile
that normally lands in a **controlled-access** archive rather than open GEO. 🔴 **This is a prediction
about where to look, not a finding, and it names no identifier.** If it is right, the accession will
be a `phs…`-class or equivalent controlled identifier and the reanalysis carries an access
application, not a download — which changes the cost of desk action **D1** materially and should be
priced in before D1 is scheduled as "hours".

### 2.8 Query hygiene — the zeros I am reporting, and the ones I discarded

Every PubMed query below is reported with its translation, because a zero whose translation is wrong
is not a zero.

| Query | Returned | Translation verdict |
|---|---|---|
| `expanded subventricular zone postnatal cortical interneuron migration gyrencephalic` | 1 (PMID 40659844) | ✅ Translation expanded `subventricular zone` correctly via `"lateral ventricles"[MeSH]`; `gyrencephalic` stayed `[All Fields]`. **Positive control: it returned the intended paper.** Counted. |
| `Subventricular zone radial glial cells maintain inhibitory neuron production human brain` | 1 (PMID 41538440) | ⚠️ Translation mangled `production` into `"economics"[MeSH] OR "efficiency"[MeSH] OR "productivity" …` and `human brain` into the journal `"hum brain"[Journal]`. The hit is nonetheless the intended paper, so the **result** is usable as a title lookup; the **count** is not evidence of anything and is not used as one. |
| — | — | 🔴 **No bare-number query was issued** (a bare number becomes `NNNN[UID]`, a record lookup, not a search). |
| — | — | 🔴 **No `[All Fields]` count is offered anywhere in this file as evidence about accessions**, because `[All Fields]` does not index Methods, supplements or data-availability statements. That is precisely why the accession question cannot be settled by PubMed counting at all, and why §2.1–2.5 are body reads rather than searches. |

`get_copyright_status` was **not** used to skip any attempt in this task. It was not used at all
here; ordering was by cost, and every candidate route was attempted or recorded as blocked.

### 2.9 Routes exhausted — the closing list

1. ✅ **PMC body of `PMC10901738` re-fetched and read to the end**, past the references, including
   the supplementary captions. Deferral sentence found; no accession; token sweep in §2.1.
2. ✅ **Europe PMC full-text XML** (`www.ebi.ac.uk`) — blocked.
3. ✅ **Publisher page** (`www.nature.com`) — blocked.
4. ✅ **Europe PMC web** (`europepmc.org`) — blocked.
5. ✅ **bioRxiv preprint**, identified by DOI — blocked. **Unexhausted for anyone with egress.**
6. ✅ **Same-group follow-up in PMC** (`PMC12321571`) — read in full; no accession; same deferral.
7. ✅ **A 2026 developing-inhibitory-neuron atlas preprint in PMC** (`PMC12874046`) — read; does not
   cite Nascimento at all.
8. ✅ **PubMed record metadata** for 38122823 — **carries no databank/accession field**.
9. ✅ **PubMed `elink` to nucleotide** — returns four `pubmed_nuccore_refseq` links, i.e. RefSeq gene
   records, **not sequence deposits**. No SRA/BioProject link exists to follow.
10. ✅ **Scholar Gateway semantic search**, two differently-framed queries aimed squarely at a
    reanalysis Methods sentence — 12 and 20 passages; no passage names a Nascimento accession.
11. ✅ **Web search**, five query framings including domain-restricted to `ncbi.nlm.nih.gov` and to
    preprint/aggregator domains — no accession in any snippet.
12. 🔴 **Not attempted, and named as the remaining routes**: the bioRxiv preprint body; the *Science*
    2026 paper (PMID 41538440, no PMCID); the paper's own Supplementary Tables 4–5 (§2.6); the
    Reporting Summary and Peer Review File, both of which are free supplementary items on the
    blocked hosts. **All four require egress this deployment does not have.**

---

## 3 · Task 2 — `G372R` protein level, arbitrated from sources

### 3.1 Source A — Aldaz & Hussain 2020 · `full-text` · **secondary**

PMID 33255508, `PMC7727818`, [DOI](https://doi.org/10.3390/ijms21238922). Read in served full text
today, end to end. It is a **narrative review**; the repository's own dossier already classes it
`T2 / MODERATE` with *"no primary measurement"*.

The sentence at issue, and — decisively — **its immediate context**, verbatim:

> *"In 2014, by means of whole-exome sequencing, it was determined that the four affected children
> harboured a homozygous missense mutation of the gene. The novel p. Pro47Thr mutation affects a
> highly conserved proline residue and critical component for the function of the first WW domain of
> the protein … **In the same study**, a second consanguineous Israeli-Palestinian family with two
> affected children was described. It was observed that both patients carried a homozygous mutation
> at another highly conserved WWOX protein residue, pGly372Arg … The pGly372Arg mutation affects a
> glycine at the C-terminus in the short-chain dehydrogenases/reductases domain of WWOX and **its
> functional consequence is unclear at this point**. **Analysis from patient fibroblasts showed that
> both described missense mutations do not alter WWOX protein expression and instead result in the
> production of a defective, partially functional WWOX protein (i.e., hypomorphic mutations).**"*

What this establishes, and what it does not:

| Field | Value |
|---|---|
| **What was measured here** | 🔴 **Nothing.** This is a review sentence. |
| **Whose measurement is described** | **Mallaret 2014** — the antecedent is explicit: *"In the same study"*. The trailing citation marker is deleted by the extraction route, but the antecedent is textual, not reconstructed. |
| **Matrix described** | *"patient fibroblasts"* |
| **Method described** | 🔴 **Not stated.** The word "Western" does not appear. |
| **`n`** | 🔴 **Not stated.** |
| **Controls** | 🔴 **Not stated.** |
| **Coverage claimed** | *"both described missense mutations"* — i.e. `P47T` **and** `G372R` |
| **Author relationship to the primary** | ⚠️ **Aldaz is a co-author of Mallaret 2014.** This is a self-report, which raises its credibility above an arm's-length review — and does **not** convert it into a measurement, nor supply the `n`, method and controls it omits. |
| **Internal tension worth noting** | Two sentences earlier the same authors write that `G372R`'s *"functional consequence is unclear at this point"*. Unaltered abundance plus unclear function is coherent, but it means the review itself asserts **no functional characterisation of `G372R`** — so "partially functional … hypomorphic" is carried by `P47T`, for which the same review does describe a mechanism (abolished PPxY binding). |

### 3.2 Source B — Steinberg 2021 · `full-text` · **primary, measured**

PMID 34268881, `PMC8350905`, *EMBO Mol Med*, [DOI](https://doi.org/10.15252/emmm.202013610). Read in
served full text today; 81,107 characters. The repository already holds this as `full text letto`
with an honest `partial_fulltext_read` status (Appendix Figures S1–S6 are **not distributed** in the
PMC package — that limitation is load-bearing below).

The variant, verbatim from the primary: *"the second family carries a **c.1114G>C (G372R)** mutation
(Mallaret,) that results in the SCAR12 phenotype in the homozygous patient (referred to as **WPM**
family)"*.

The measurement, verbatim:

> *"We generated FOs from the healthy heterozygous father and mother (WPM F2 and WPM M3) and their
> affected homozygous daughter and son (WPM D1 and WPM S1). As expected, FOs were indistinguishable
> in terms of morphology, growth, and expression of β3-Tubulin and SOX2 (Fig), but **while in the VZ
> of WPM F2 and WPM M3, WWOX was detected, barely any signal was observed in WPM D1 and S1,
> consistent with WWOX levels in the iPSCs** (Appendix Fig)."*

| Field | Value |
|---|---|
| **What was measured** | 🟢 **WWOX immunoreactivity**, in situ |
| **Matrix** | **Forebrain organoids (FOs)** derived from patient iPSCs, scored specifically **in the ventricular zone (VZ)** — a neuroepithelial progenitor compartment, not a differentiated somatic cell |
| **Method** | **Immunostaining / immunofluorescence.** 🔴 **Not a Western blot, and not quantified in the served text** — no densitometry, no intensity ratio, no statistic is given for this comparison. *"Barely any signal"* is the authors' own qualitative wording. |
| **`n`** | **2 affected homozygotes** (WPM D1, daughter; WPM S1, son) vs **2 comparators** (WPM F2, father; WPM M3, mother). Same family. |
| **Controls** | ⚠️ **The comparators are the heterozygous carrier parents, not wild-type homozygotes and not unrelated controls.** This matters: the same paper's Discussion — as already held in the repository — observes that WWOX expression *varies widely* among healthy heterozygous parents. So the baseline against which *"barely any signal"* is scored is itself variable. |
| **Corroboration offered** | *"consistent with WWOX levels in the iPSCs (Appendix Fig)"* — 🔴 **unverifiable here.** The Appendix Figures are the exact surface the repository's own dossier records as absent from the PMC package. The iPSC corroboration is therefore a **reading debt**, not a second read-out. |
| **Adjacent measured context (not abundance)** | In the same FOs: glutamatergic/GABAergic marker ratio *"did not show any clear difference"*; cortical-layer markers comparable, *"supported the notion of normal neuronal and cortical development"*; astrocytic immunostaining and qPCR *"did not reveal significant differences"*; DDR foci — *"we did not observe major differences in accumulation of DNA damage foci between healthy and sick SCAR12 individuals"*. Wnt-gene RNA *"did show a pattern suggestive of the Wnt pathway activation"*. |

### 3.3 Source C — Mallaret 2014 · the primary both sources point at · 🔴 **NOT READABLE**

PMID 24369382, `PMC3914474`, *Brain* 2014;137(Pt 2):411–9,
[DOI](https://doi.org/10.1093/brain/awt338).

🔴 **`get_full_text_article(["PMC3914474"])` returns `full_text: ""`.** A PMCID exists; a body does
not. The repository has already established the cause and it is **licensing, not routing** —
`FT-128` records `license.is_open_access: false` with an all-rights-reserved statement, and states
plainly that *"a PMCID is not a body"* and that **acquisition is a human action**. I did not retry
blocked publisher hosts for it.

Its abstract (`abstract-depth`) reports `P47T`, reports `G372R` with *"prominent upper motor neuron
disease"*, and reports the mouse audiogenic-seizure observation. 🔴 **The abstract says nothing about
protein levels in fibroblasts for either variant.** It cannot arbitrate.

**What the repository already holds from this body** — `paper_registry_current.md`, PAPER 042,
verbatim quotations:

> Western blot on the **`P47T`** patient's fibroblasts (**passages 10/13/14 vs 4 controls**) →
> *"similar amounts of the mutant and wild-type WWOX protein"*; *"the mutation does not alter global
> protein levels"*. Peptide pull-down → *"only the wild-type and not the mutant fusion peptides were
> efficiently pulled down with the PPPY containing oligopeptide"*.

🔴 **That held record is `P47T`-specific. It documents no `G372R` fibroblast blot.**

⚠️ **And I must not over-read that absence.** The held record derives from a
`legacy_reconstruction` / `partial_fulltext_read` whose coverage fields are all `unknown_legacy`
(`FT-128`). **Absence of a `G372R` blot from a partial read is not absence of a `G372R` blot from the
paper.** This is the same rule as §1: a zero is not absence. The honest statement is
`PREMISE: UNVERIFIED` on whether Mallaret ran a fibroblast Western for the `G372R` family.

### 3.4 The verdict

**Option (2) — one source is a secondary mis-description of the other — with option (1) as the
bounded fallback. Option (3) is excluded.**

**Why (3) is excluded, first and cleanly.** Option (3) requires two measurements of the same thing
that disagree. There is only **one** measurement of `G372R` protein level readable today: Steinberg's
organoid-VZ immunofluorescence. Aldaz & Hussain contribute **no measurement at all** — they describe
someone else's. Two things cannot conflict on the same measurement when only one of them is a
measurement. **There is no genuine same-measurement conflict to adjudicate.**

**Why (2) is the primary verdict.** The chain is:

1. Aldaz & Hussain's sentence attributes a **fibroblast** protein-expression result to Mallaret 2014,
   covering *"both described missense mutations"*.
2. The only documented fibroblast Western from Mallaret 2014 — held in this repository as verbatim
   quotation, with passages and control count — is for **`P47T` only**.
3. Therefore the review sentence **extends to `G372R` a coverage the primary is not documented to
   have.** That is an over-generalisation in a secondary source: precisely option (2).
4. It is *not* proven to be an error, because Mallaret's body is unreadable and may contain a `G372R`
   blot. So (2) is the verdict **at the evidentiary depth available**, held as
   `PREMISE: UNVERIFIED` rather than as a demonstrated misstatement.

**Why (1) is the fallback and not the headline.** If Mallaret's unread body *does* contain a `G372R`
fibroblast Western, then the two sources are measuring different things and **both stand, strictly
bounded**:

| | Source A route (as described) | Source B route (as measured) |
|---|---|---|
| Matrix | patient **skin fibroblast** — differentiated somatic cell | **iPSC-derived forebrain-organoid VZ** — neuroepithelial progenitor |
| Method | Western blot (inferred from the repository's `P47T` record; **not stated in the review**) | immunofluorescence, in situ |
| Scale | lysate abundance, whole population | signal in a spatial compartment |
| Comparator | *"4 controls"* for `P47T`; unstated for `G372R` | **heterozygous parents of the same family** |
| Quantified | yes, for `P47T` (*"similar amounts"*) | 🔴 **no** — qualitative wording only |

These are **not commensurable**, which the repository already knows and has already written down as
`FM-014`: *"Abbondanza ≠ funzione, e le misure di abbondanza non sono confrontabili tra loro … la
regola: quando si costruisce una serie genotipo-fenotipo, verificare che le misure siano la stessa
misura."* **`FM-014` is the correct governing rule here and it was already in the repository before
today.** What this file adds is that for `G372R` the mismatch is worse than `FM-014` states: one side
of the comparison is not a measurement at all.

🔴 **There is also a real biological reading under which both are simply true and neither is an
error:** WWOX abundance is compartment-dependent, and Aldaz & Hussain's own review documents that
`WWOX` expression differs strongly by cell type and developmental stage. A hypomorphic missense whose
protein is stable in a passaged fibroblast and poorly detectable in a neuroepithelial progenitor is
not a contradiction — it is a matrix effect. **Labelled `INFERENZA`. Nothing measured supports it
today**, and it must not be used to dissolve the disagreement by assertion.

### 3.5 🔴 Consequence for `DL-MECH-037` — and it is not the tidy one

The Orchestrator's brief states correctly that if `G372R`'s protein is in fact normal, the
burial-discriminates argument gets **simpler**: `P47T` and `G372R` both surface, both protein-normal,
both mild, against buried `Q230P` with absent protein.

**That simplification is not available on this evidence, and taking it would be the error this task
was set to catch.**

- The only **measured** `G372R` protein read-out is *"barely any signal"* (Steinberg, `full-text`,
  organoid VZ IF, n=2 vs 2 heterozygous parents, qualitative).
- The "protein normal" alternative rests entirely on a **review sentence** whose primary body **no
  one in this repository has read at complete depth**, and whose documented fibroblast measurement
  covers a **different variant**.
- Flipping a measured immunofluorescence result to its opposite on that basis would be promoting a
  secondary over-generalisation above a primary measurement **because the result is convenient**.

**The correct status of the `G372R` protein-abundance cell is therefore: matrix-split and
unresolved.** Recommended handling, for the Orchestrator to accept or reject — I hold no authority
over the registries and have touched none:

1. **Keep** the measured cell as it stands, but **re-label it with its full bound**: *"barely any
   signal" — IF, patient-derived forebrain-organoid VZ, n=2 affected vs n=2 heterozygous parents,
   qualitative, iPSC corroboration in an Appendix figure PMC does not distribute.*
2. **Add** the Aldaz & Hussain assertion as a **flagged secondary counter-statement at `T2` depth**,
   explicitly marked as describing Mallaret 2014 and as `P47T`-documented / `G372R`-unverified.
3. **Mark `DL-MECH-037`'s `G372R` row as resting on a matrix-split datum**, so that the burial
   argument's reliance on it is visible rather than implicit. The burial argument's *decisive*
   control is already recorded in the repository as **`P47T`/`P47R`** — same residue, near-identical
   ΔΔG, opposite phenotypes — **not** `G372R`. That is where its weight should sit, and it is
   unaffected by this arbitration either way.
4. **Do not open a new reading-debt entry.** 🔴 `FT-128` **already exists and already covers exactly
   this**, including, as its own item 3, *"Whether `P47T`'s normal Western blot … is in the body with
   `n` and controls"*, and, as item 4, *"The `G372R` family's neurological detail."* This file adds a
   fifth question to that same debt rather than duplicating it:

   > **`FT-128`, new question for the read, if the body is ever acquired:** *does Mallaret 2014
   > contain a fibroblast Western blot for the **`G372R`** family, with `n`, passages and controls —
   > or is Aldaz & Hussain 2020's "both described missense mutations do not alter WWOX protein
   > expression" an extension of a `P47T`-only measurement?* **This single question decides whether
   > the `G372R` disagreement is verdict (2) or verdict (1).**

   Nothing in this file cites an `FT-` number that does not exist. `FT-128`, `FT-133` and `FT-134`
   all exist in `full_text_queue_current.md`. **No `G372R`/Task-2 debt entry is coined**, because
   `FT-128` already holds it; the one new entry, **`FT-134`, belongs to Task 1** and declares the
   three non-WWOX accession-route papers this file names (PMID 40659844, 41659519, 41538440), which
   raised `UNREAD_PREMISE` from 0 to 3 when this file was first written. 🔴 **No PMID has been
   stripped anywhere in this file to avoid declaring debt** — the identifiers were kept and the debt
   was declared, per the `FT-133` precedent. After `FT-134`,
   `python3 framework/scripts/growth_anchors.py check` returns
   `unread_premises=0 · VERDICT: PASS`, and
   `python3 framework/scripts/manifest_queue_id_crosscheck.py --prose` returns
   `prose FT references unresolved: 0`.

---

## 4 · Delta against the repository

| # | Finding | Status vs repository |
|---|---|---|
| 1 | The Nascimento data-availability statement is **deferred to the publisher and the body contains no accession** — now established by a **full re-read past the references** with an exhaustive token sweep, not by inference | 🟡 **Confirms and hardens** `wwox_postnatal_svz_expression_20260922.md` §8, which stated this from a single earlier read. The repository's refusal to name an accession was correct. |
| 2 | 🔴 **The one `GEO` mention in the Nascimento Methods refers to a re-used adult-EC dataset, not their own deposit — and its citation marker is deleted by extraction** | 🟢 **New.** Not in the repository. This is a live instance of the GEO-deletion hazard sitting inside the very paper the hazard threatens, and it is a concrete mis-attribution trap for any future reader. |
| 3 | 🟢 **Supplementary Tables 4 and 5 are DE-gene tables over the EC-stream and whole datasets** — a named, free, accession-free route to a partial `WWOX` answer | 🟢 **Sharpens** desk action **D5**, which anticipated "a supplementary table" generically. Now: which tables, by caption — plus the bound that `WWOX`-absent from a DE table is `NOT_TESTED_OR_NOT_SIGNIFICANT`, not non-expression. |
| 4 | ⚠️ **The postnatal EC nuclei in the merged object span `14 days to 27 years`**, verbatim: *"nuclei from the postnatal EC between 14 days and 27 years of age"* | 🟡 **Corrects a bound.** Desk action **D1** carries *"n = 1 postnatal donor"*. That is right for the **EC-stream microdissection** (a single two-week-old sample) but **understates the object**: the postnatal EC arm is an age series. D1's achievable scope is larger than recorded — though the *periventricular/stream* compartment, which is the whole point, does remain n=1. |
| 5 | 🔴 **In the EC-stream microdissection the radial-glia cluster is NOT connected by trajectory to the migrating interneurons**, verbatim: *"In the EC stream microdissection, we did not find intermediate progenitors for interneurons or a differentiation trajectory connecting the local RG to the immature inhibitory neurons."* | 🟢 **New, and it bounds the prize.** The repository's framing — *"the first WWOX measurement in a human postnatal germinal compartment"* — survives, because the RG cluster is real and postnatal. But any onward claim that WWOX in that cluster speaks to *neurogenesis feeding the stream* is **blocked by the authors' own negative result**. Read `WWOX` in the RG cluster as *"WWOX in postnatal human periventricular radial glia"*, **not** as *"WWOX in the progenitor supplying the stream."* |
| 6 | 🟡 **A controlled-access destination is the likely home of the data** (paediatric post-mortem + clinical histories + genetic demultiplexing against a 1000 Genomes VCF) | 🟢 **New, and it re-prices D1.** Labelled `INFERENZA`. If right, D1 is "hours **after** an access application", not "hours". |
| 7 | 🔴 **The `G372R` disagreement is verdict (2), not (3)** — Aldaz & Hussain is a **secondary description of Mallaret 2014**, and the fibroblast Western this repository holds verbatim from Mallaret covers **`P47T` only** | 🟢 **New.** `CC-20260922-POSTNATAL-SVZ-01` §(c) had correctly flagged *"different matrices?"* as the likely resolution. The actual resolution is one step earlier and sharper: **one side is not a measurement.** |
| 8 | 🔴 **`DL-MECH-037`'s burial argument must not be simplified**; the `G372R` row is matrix-split, and the argument's decisive control is `P47T`/`P47R`, already in the repository | 🟢 **New as an explicit instruction.** It is the opposite of the tidy outcome. |
| 9 | ⚠️ **Steinberg's `G372R` comparators are the heterozygous parents**, against a baseline the same paper describes as widely variable among healthy heterozygotes | 🟢 **New.** The repository records the measurement and records `FM-014`'s incommensurability, but not that the *comparator arm itself* is a carrier genotype on a variable baseline. This weakens the `G372R` abundance datum from *both* directions. |
| 10 | 🟢 **Mallaret 2014's PMC body is empty for licence reasons** — re-measured today, `full_text: ""` | 🟡 **Confirms `FT-128`** exactly, including its *"a PMCID is not a body"* finding. No new debt entry needed. |

---

## 5 · What I could not verify — stated as such

- 🔴 **No accession, and I name none.** Routes exhausted in §2.9. The unexhausted routes all require
  egress this deployment does not have: the bioRxiv preprint body, the *Science* 2026 paper (no
  PMCID), and the paper's own free supplementary files, Reporting Summary and Peer Review File.
- 🔴 **Mallaret 2014's body (PMID 24369382) is unread**, licence-blocked, and it is the **single
  document that decides Task 2 between verdict (2) and verdict (1).** `FT-128` holds the debt; a
  fifth question has been proposed for it in §3.5.4.
- 🔴 **Steinberg's iPSC corroboration of the `G372R` result is unverified** — it sits in an Appendix
  figure the PMC package does not distribute.
- 🔴 **Steinberg's `G372R` IF is not quantified in the served text.** No densitometry, no intensity
  ratio, no statistic for that specific comparison. *"Barely any signal"* is the authors' wording and
  must be quoted, never converted into a number.
- 🔴 **The adult-EC dataset Nascimento re-used is unidentified** because its citation marker was
  deleted by the extraction route. I do not name it.
- 🔴 **Nascimento's figures and supplementary tables were not inspected** — same standing limitation
  the repository already declares for this paper under `FT-133`. A `WWOX` row in Supplementary Table
  4 or 5 would not have been seen by me.
- 🟡 **Whether an accession exists at all in the published record is not settled by this file** — only
  that it is not reachable from here. The publisher's deferral sentence implies a statement exists
  behind the DOI.
- 🔴 **No researcher contact details are recorded in this file**, by design. Author-contact routes
  were not pursued and are not proposed.

---

## 6 · Anything contradicting a repository assertion

1. 🔴 **Desk action `D1`'s cost label.** Recorded as *"desk, hours — once egress exists"*. §2.7 makes
   a controlled-access deposit the likely case, in which case D1 is **hours plus an access
   application**, and §2.9 shows the accession is not obtainable from here at all. **The blocker for
   D1 is not only egress — it is an unknown identifier.** D1 should not be scheduled as a
   hours-scale task until the accession is in hand.
2. 🟡 **Desk action `D1`'s `n = 1` bound** is right for the stream and understates the merged object
   (delta #4).
3. 🔴 **The implied path from "WWOX in the Nascimento RG cluster" to postnatal neurogenesis feeding
   the EC stream is blocked by the authors' own negative trajectory result** (delta #5). No
   repository text asserts that path outright, but the framing invites it, and it should be closed
   before a reanalysis is designed around it.
4. 🔴 **`CC-20260922-POSTNATAL-SVZ-01` §(c) frames the `G372R` disagreement as possibly
   "different matrices … both stand"** — correct as a fallback, but it treats Aldaz & Hussain as one
   of two measurements. **It is not a measurement.** The commit candidate's framing should be
   tightened before it lands.
5. 🟢 **No repository assertion was found to be factually wrong.** `FM-014`, `FT-128`, the
   `non rilevata` vs `assente` distinction in `candidate_adjudication_20260921.md`, and the
   `wwox_postnatal_svz_expression_20260922.md` refusal to name an accession all held up against the
   primary sources read today. In particular the repository's hedged wording for `G372R` —
   *"proteina **quasi non rilevabile** all'IF"* — is the correct hedge, and matches Steinberg's
   *"barely any signal"* rather than over-reading it.

---

## 7 · Sources and depth reached

According to PubMed:

| PMID | Source | DOI | Depth reached here | Role in this file |
|---|---|---|---|---|
| 38122823 | Nascimento MA, …, Alvarez-Buylla A, Sorrells SF. Protracted neuronal recruitment in the temporal lobes of young children. *Nature* 2023;626:1056–65 | [DOI](https://doi.org/10.1038/s41586-023-06981-x) | 🟢 **`full-text`**, `PMC10901738`, re-read end-to-end; figures and supplements **not** inspected | Task 1 target |
| 40659844 | An expanded subventricular zone supports postnatal cortical interneuron migration in gyrencephalic brains. *Nat Neurosci* 2025 | [DOI](https://doi.org/10.1038/s41593-025-01987-2) | 🟢 **`full-text`**, `PMC12321571` | Task 1 route — no accession |
| 41659519 | A Single-Cell and Spatial 3D Multi-omic Atlas of Developing Human Basal Ganglia and Inhibitory Neurons | [DOI](https://doi.org/10.64898/2026.01.28.702385) | 🟢 **`full-text`**, `PMC12874046` | Task 1 route — does not cite the target |
| 41538440 | Subventricular zone radial glial cells maintain inhibitory neuron production in the human brain. *Science* 2026 | — (no PMCID returned) | 🔴 **metadata only** | Task 1 route — unreachable, recorded |
| 33255508 | Aldaz CM, Hussain T. WWOX Loss of Function in Neurodevelopmental and Neurodegenerative Disorders. *IJMS* 2020;21:8922 | [DOI](https://doi.org/10.3390/ijms21238922) | 🟢 **`full-text`**, `PMC7727818` — **review, secondary** | Task 2 Source A; also the ~6 TPM figure in §1 |
| 34268881 | Steinberg DJ, …, Aqeilan RI. Modeling genetic epileptic encephalopathies using brain organoids. *EMBO Mol Med* 2021 | [DOI](https://doi.org/10.15252/emmm.202013610) | 🟢 **`full-text`**, `PMC8350905`; ⚠️ Appendix Figures not distributed in the PMC package | Task 2 Source B — the one measurement |
| 24369382 | Mallaret M, …, Aldaz CM, Koenig M. The tumour suppressor gene WWOX is mutated in autosomal recessive cerebellar ataxia with epilepsy and mental retardation. *Brain* 2014;137:411–9 | [DOI](https://doi.org/10.1093/brain/awt338) | 🔴 **`abstract-depth`** — `PMC3914474` returns `full_text: ""`, licence-blocked | Task 2 Source C — **the document that would settle it**; debt held in `FT-128` |
| — | bioRxiv preprint, *Persistent postnatal migration of interneurons into the human entorhinal cortex*, `10.1101/2022.03.19.484996` | — | 🔴 **not retrieved** — host `EGRESS_BLOCKED` | Task 1 — best unexhausted route |

**BLOCK-1:** no molecule, no dose, no safety claim appears in this file. **Nothing here is medical
advice.** Genotype classes (`P47T`, `G372R`, `Q230P`, `c.517-2A>G`, `c.1114G>C`) and matrices
(patient fibroblast, patient-derived iPSC, forebrain-organoid VZ, post-mortem human temporal lobe,
mouse, rat) are kept rigidly separate throughout, and every variant string and identifier in this
file was read from a served source today — **none reconstructed from memory.**
