# Acquisition Packet A9 — PMID 35984507 (Carvalho et al. 2022, *Cell Mol Life Sci*)

**ACCESSIBLE: NO — `EVIDENCE_BLOCKED`.**

How established: `mcp__PubMed__get_full_text_article` was called on `PMC11071800` in this session
(2026-09-21). The call **succeeded** — it returned a record with title, identifiers, DOI and abstract —
but the `full_text` field was the empty string (`"full_text": ""`, **body length = 0 characters**).
`mcp__PubMed__get_copyright_status` on PMID 35984507 returned `license.type: null`,
`license.is_open_access: false`, and a summary block reading `"found_in_pmc": 0`,
`"open_access_count": 0`. This is the second independent measurement in this repository and it
**agrees with the first**: the PMC record for this article exists as a stub (identifier + abstract +
a supplementary-material pointer) with no deposited body. No further fetch attempt was made, per
instruction. WebFetch and curl were **not** used; both are blocked in this environment.

---

## §1 Complete bibliographic record

### 1.1 Identifiers — all verified in this session

| Field | Value | Verified by |
|---|---|---|
| PMID | `35984507` | `get_article_metadata` |
| PMCID | `PMC11071800` | `get_article_metadata` **and** `convert_article_ids` (both returned it independently) |
| DOI | `10.1007/s00018-022-04508-7` | `get_article_metadata`, `convert_article_ids` |
| PII | `10.1007/s00018-022-04508-7` | `get_article_metadata` |

`convert_article_ids` (id_type `pmid`, response-date 2026-09-21) returned exactly one record:
`{"pmcid":"PMC11071800","pmid":"35984507","doi":"10.1007/s00018-022-04508-7"}`. **No author-manuscript
PMCID variant was returned.** `find_related_articles` with `link_type: pubmed_pmc` returned the single
link `11071800` — i.e. PubMed knows of exactly one PMC record for this article, the same stub.

### 1.2 Citation

Carvalho C, Correia SC, Seiça R, Moreira PI.
*WWOX inhibition by Zfra1-31 restores mitochondrial homeostasis and viability of neuronal cells
exposed to high glucose.*
**Cellular and Molecular Life Sciences (Cell Mol Life Sci)**, volume **79**, issue **9**, article
**487**. Publication date recorded in PubMed: **2022-08-19**. Language: eng.
Article type as indexed: **Journal Article** (no "Review" tag — it is indexed as primary research).

> Note: PubMed returns a single `publication_date` of 2022-08-19 for this record. It does **not**
> expose separate print and electronic-publication dates through this tool, so the print/e-pub split
> could not be verified here and is **not asserted**.

### 1.3 Authors and affiliations — verbatim as returned

1. **Carvalho, Cristina (C)** — corresponding (email attached to every affiliation line)
   - "Center for Neuroscience and Cell Biology, University of Coimbra, 3004-504, Coimbra, Portugal. [corresponding-author address, in the PubMed affiliation string]."
   - "Center for Innovation in Biomedicine and Biotechnology (CIBB), Coimbra, Portugal. [corresponding-author address, in the PubMed affiliation string]."
   - "Institute for Interdisciplinary Research, University of Coimbra, Coimbra, Portugal. [corresponding-author address, in the PubMed affiliation string]."
2. **Correia, Sónia C (SC)**
   - "Center for Neuroscience and Cell Biology, University of Coimbra, 3004-504, Coimbra, Portugal."
   - "Center for Innovation in Biomedicine and Biotechnology (CIBB), Coimbra, Portugal."
   - "Institute for Interdisciplinary Research, University of Coimbra, Coimbra, Portugal."
3. **Seiça, Raquel (R)**
   - "Institute of Physiology, Faculty of Medicine, University of Coimbra, Coimbra, Portugal."
4. **Moreira, Paula I (PI)** — senior/corresponding (email attached to every affiliation line)
   - "Center for Neuroscience and Cell Biology, University of Coimbra, 3004-504, Coimbra, Portugal. [corresponding-author address, in the PubMed affiliation string]."
   - "Center for Innovation in Biomedicine and Biotechnology (CIBB), Coimbra, Portugal. [corresponding-author address, in the PubMed affiliation string]."
   - "Institute of Physiology, Faculty of Medicine, University of Coimbra, Coimbra, Portugal. [corresponding-author address, in the PubMed affiliation string]."
   - "Laboratory of Physiology, Faculty of Medicine, University of Coimbra, 3000-354, Coimbra, Portugal. [corresponding-author address, in the PubMed affiliation string]."

**Corresponding-author determination.** PubMed's affiliation strings carry e-mail addresses for
**Carvalho C** (`[corresponding-author address, in the PubMed affiliation string]`) and **Moreira PI** (`[corresponding-author address, in the PubMed affiliation string]`) and for
neither of the other two authors. In the NLM record an e-mail appended to an affiliation string is the
conventional marker of a corresponding author, so **both are corresponding**. These are published
addresses in the public PubMed record and are reproduced here for the ILL/author route only.

**Independence from the reagent's inventors — confirmed.** Every affiliation is University of Coimbra
/ CNC / CIBB / Faculty of Medicine, Portugal. **No author of this paper is affiliated with the Chang
(Nan-Shan Chang) laboratory at National Cheng Kung University, Tainan**, which invented Zfra and the
pY33/pS14-WWOX framework. A PubMed search `Moreira PI[Author] AND WWOX` returns `total_count: 1` —
this paper alone. The Coimbra group has, on the PubMed record, exactly one WWOX publication, and no
co-authorship with Chang. The claim that this is an independent laboratory therefore **holds**.

### 1.4 Keywords (author)

`Diabetes` · `Mitochondria` · `Neurodegeneration` · `Neuroprotection` · `WWOX` · `Zfra1-31`

### 1.5 MeSH terms

`Animals` · `Humans` · `Rats` · `Amyloid beta-Peptides` · `Glucose` · `Homeostasis` · `Mitochondria` ·
`Neuroblastoma` · `Oxidative Stress` · `Reactive Oxygen Species` · `Tumor Suppressor Proteins` ·
`WW Domain-Containing Oxidoreductase` · `Peptide Fragments`

> **Diagnostic reading of the MeSH set.** There is **no** `Gene Knockdown Techniques`, no
> `RNA, Small Interfering`, no `Gene Silencing`, no `RNA Interference` and no `Mice, Knockout` term.
> There is also no `Autophagy` and no `Mitophagy` term despite autophagy being analysed. MeSH
> indexing is not exhaustive and its absence is **not proof** — but it is a weak negative signal on
> checklist item §4.1 (existence of a genetic WWOX arm) and it is recorded here as such, tagged as
> inference, not as a finding.

### 1.6 Grant / funding identifiers

**PubMed returned no `grant` field for this record.** No funder identifier is available from the tool.
This is a real gap for the funder-mandate route in §2.

However, two conference abstracts by the same two authors reporting the precursor stages of this
work (see §3) carry explicit funding statements, reproduced verbatim:

> "This work was funded by European funds from FEDER, through the Programa Operacional Factores de
> Competitividade — COMPETE 2020 (HealthyAging2020: CENTRO-01-0145-FEDER-000012) and Fundação para a
> Ciência e a Tecnologia (PEst-C/SAU/LA0001/2013-2014 and work contract to scientific employment
> stimulus CEECIND/02201/2017 to C. Carvalho)" — EJCI 2021 abstract, DOI `10.1111/eci.13567`

> "This work was funded by European funds from FEDER, through the Programa Operacional Factores de
> Competitividade — COMPETE 2020 (HealthyAging2020 CENTRO-01-0145-FEDER-000012) and Fundação para a
> Ciência e a Tecnologia (PEst-C/SAU/LA0001/2013-2014 and fellowship SFRH/BPD/107741/2015 to
> C. Carvalho)" — EJCI 2019 abstract, DOI `10.1111/eci.13108`

These are the **probable** funders of the published paper. They are **not stated in the paper's own
PubMed record** and are therefore an inference from adjacent abstracts, not a verified fact about
this article. FCT and FEDER/COMPETE 2020 are European public funders with open-access expectations;
whether a deposit mandate attaches to this specific grant was **not** verified by any tool here.

### 1.7 Licence and deposit state — verbatim

`get_copyright_status(["35984507"])` returned:

```
pmid:        35984507
pmc_id:      PMC11071800
copyright.statement: "© 2022. The Author(s), under exclusive licence to Springer Nature Switzerland AG."
copyright.year:      "2022"
copyright.holder:    "authors"
license.type:        null
license.url:         null
license.is_open_access: false
source:          "pubmed"
checked_sources: ["pubmed"]
available_at.pubmed_url: https://pubmed.ncbi.nlm.nih.gov/35984507/
available_at.pmc_url:    https://pmc.ncbi.nlm.nih.gov/articles/PMC11071800/
available_at.doi_url:    https://doi.org/10.1007/s00018-022-04508-7
summary: total_checked 1 | found_in_pubmed 1 | found_in_pmc 0 | not_found 0 | open_access_count 0
```

Two things are load-bearing here. First, `checked_sources` is `["pubmed"]` **only** — the tool did
not obtain a PMC-side licence record, which is itself consistent with the PMC record having no
deposited body to license. (For contrast, on articles that *are* deposited the same tool returns
`source: "pmc"` and `checked_sources: ["pubmed","pmc"]`; see §3, where seven comparison records came
back that way.) Second, the copyright statement is **"under exclusive licence to Springer Nature"** —
this is the closed-access Springer statement, not a CC statement. The article is subscription
content.

The PMC accession number `PMC11071800` sits in a block assigned around 2024, i.e. roughly two years
after the 2022 publication. That pattern is **consistent with** a delayed or metadata-only deposit
rather than an at-publication open deposit. **This is an observation about the accession range, not a
fact reported by any tool, and it is not asserted as the mechanism.**

### 1.8 Supplementary material — present, not reachable

The `get_full_text_article` response, although its body was empty, carried the following closing text
inside the abstract field, verbatim:

> "Supplementary Information
> The online version contains supplementary material available at 10.1007/s00018-022-04508-7."

So the record **does** indicate supplementary files exist. **No supplementary file was reachable from
any tool available in this session.** Supplementary material for Springer articles is served from the
publisher landing page, which is not reachable here. The supplementary files are likely to matter:
in papers of this shape the peptide dose-response, the loading controls and the full uncropped blots
are frequently supplementary-only, and §4.2 and §4.3 below may be answerable *only* from them. Whoever
obtains the PDF must be told to **download the supplementary bundle as well** — the PDF alone may not
settle the question.

---

## §2 Routes

Each route below is marked **[TESTED HERE]** or **[TO BE TRIED BY A HUMAN]**. Nothing in this section
asserts that an untested route works.

| # | Route | Status | What is actually known |
|---|---|---|---|
| R1 | PMC via `get_full_text_article` on `PMC11071800` | **[TESTED HERE] — FAILED** | Call succeeded, `full_text` body length **0**. Re-measured once as instructed; not retried. |
| R2 | PMC open-access / licence check | **[TESTED HERE] — NEGATIVE** | `is_open_access: false`, `license.type: null`, `found_in_pmc: 0`. |
| R3 | Author-manuscript PMCID variant | **[TESTED HERE] — DOES NOT EXIST** | `convert_article_ids` returned one PMCID; `find_related_articles(pubmed_pmc)` returned one link, the same stub. No second PMC accession. |
| R4 | Scholar Gateway full-text corpus (`semanticSearch`) | **[TESTED HERE] — PARTIAL, INDIRECT** | Two queries run. The corpus does **not** contain this article. It **does** contain two precursor conference abstracts by the same authors (§3), whose passages were retrieved. That is the only substantive text about this work obtained in this session. |
| R5 | Publisher landing page (link.springer.com, DOI `10.1007/s00018-022-04508-7`) | **[TO BE TRIED BY A HUMAN]** | Not attempted. WebFetch returns `EGRESS_BLOCKED` and curl returns 403 in this environment; previous sessions confirmed this. A human with an institutional subscription to *Cell Mol Life Sci* can very likely obtain both the PDF and the supplementary bundle from here in one step. |
| R6 | Institutional subscription / university library proxy | **[TO BE TRIED BY A HUMAN]** | *Cell Mol Life Sci* is a mainstream Springer title held by most medical-school libraries. **This is the route most likely to succeed.** It is also the only route that reliably delivers the supplementary files alongside the PDF. |
| R7 | Corresponding author, direct request | **[TO BE TRIED BY A HUMAN]** | Two published corresponding addresses, from the public PubMed record: **Cristina Carvalho — `[corresponding-author address, in the PubMed affiliation string]`** and **Paula I. Moreira — `[corresponding-author address, in the PubMed affiliation string]`**. Author-copy sharing for personal scholarly use is normal practice. A request should ask explicitly for **the PDF *and* the Supplementary Information**, and — because the whole point is §4 — may reasonably ask the authors the one direct question: *was WWOX ever silenced genetically in this study, or was Zfra1-31 the only manipulation?* An author's answer would settle the objection faster than the PDF. |
| R8 | University of Coimbra institutional repository (Estudo Geral) | **[TO BE TRIED BY A HUMAN — existence not verified]** | The corresponding authors are at University of Coimbra / CNC / CIBB. Portuguese universities commonly run an institutional repository, and FCT-funded output is commonly deposited. **No tool in this session confirmed that such a repository holds this item.** Do not treat this as available; treat it as a plausible place to look. No URL is asserted. |
| R9 | Inter-library loan (ILL) | **[TO BE TRIED BY A HUMAN]** | Standard ILL request on: Carvalho C et al., *Cell Mol Life Sci* 2022; **79(9): 487**; DOI `10.1007/s00018-022-04508-7`. The volume/issue/article-number triple is verified above and is sufficient for any ILL form. ILL typically delivers the PDF but **often not** the supplementary files — so R6 or R7 remain preferable. |
| R10 | Europe PMC / Unpaywall / OpenAlex / CORE / preprint servers | **[TO BE TRIED BY A HUMAN — not reachable from this session]** | No MCP tool in this session reaches these. The repository's `find-fulltext` skill runs exactly this cascade and should be pointed at this PMID from a session that has network egress. Given the closed Springer licence and the absence of an author-manuscript PMCID, the probability that Unpaywall finds a legitimate OA copy is **low but not zero**. |

**Recommended order for a human:** R6 (library proxy) → R7 (author e-mail, with the §4.1 question
asked directly) → R9 (ILL) → R8 (Coimbra repository) → R10 (find-fulltext cascade).

---

## §3 Citation network

`find_related_articles` (`pubmed_pubmed`) returned 100 similar-article PMIDs — a computational
similarity list, **not** a citation list. No tool available in this session performs a true
"cited-by" lookup, so the table below is built from (a) the similarity list, (b) three targeted
PubMed searches, and (c) two Scholar Gateway semantic searches over a full-text corpus.

**Targeted searches run, with counts:**
- `Zfra AND (neuron OR SH-SY5Y OR mitochondria OR brain)` → **9 records** (all listed below or excluded as cancer-only)
- `Moreira PI[Author] AND WWOX` → **1 record** (this paper only)
- `WWOX AND (diabetes OR "high glucose")` → **16 records**
- `(WWOX OR Zfra) AND (mitochondria OR mitophagy OR autophagy) AND (neuron OR brain OR neurodegeneration)`, 2022+ → **9 records**

### 3.1 The two precursor abstracts — the most important finding in this section

Neither is a citing paper. Both are **conference abstracts by Carvalho C and Moreira PI reporting
earlier stages of this same work**, found only through Scholar Gateway. They are the closest thing to
the primary source obtained in this session, and they are **still not the primary source**: a
conference abstract has no methods section, no figures, no statistics and no peer-reviewed
verification, and its content routinely differs from the paper that follows.

| Item | DOI `10.1111/eci.13108` | DOI `10.1111/eci.13567` |
|---|---|---|
| Venue | *Eur J Clin Invest*, "Oral Talks", abstract **S8O3**, 29 Apr 2019 | *Eur J Clin Invest* **51(S1)**, "Symposium 1 — Mitochondria in Health & Disease", 09 Jun 2021 |
| Authors | Cristina Carvalho, Paula I. Moreira (Coimbra) | C. Carvalho, P.I. Moreira (Coimbra) |
| Open access | `isOpenAccess: False` | `isOpenAccess: False` |
| Retrievable here | **Passages yes, whole item no.** Chunk 84 of 95 retrieved in full. | **Passages yes, whole item no.** Chunks 28 and 29 of 256 retrieved; the Methods paragraph is **cut at the chunk boundary** and the concentration/duration text was not recoverable by a second targeted query. |
| Substantive? | **Yes, for the animal arm.** | **Yes, for the cell arm.** |

**What `eci.13108` (2019) says, verbatim in the load-bearing parts:**

> "we evaluated WWOX1 activation pattern in the brain cortex of 6 and 14-month-old Goto-Kakizaki (GK)
> rats, a non-obese, spontaneous model of T2D as well as in 3xTg-AD mice at different ages (3, 6, 9
> and 11-month-old), a model of AD. Moreover, studies in differentiated SH-SY5Y human neuroblastoma
> cells under hyperglycemic conditions were also performed…"

> "In GK rats, WWOX1 activation, evaluated through Tyr33 phosphorylation, occurs in younger animals
> while in older animals a significant decrease of WWOX1 activation was observed."

> "In differentiated SH-SY5Y cells under hyperglycemic conditions, WWOX1 activation occurs after 24
> hours of incubation. Interestingly, WWOX1 activation is associated with a loss of mitochondrial
> membrane potential and increased p53 levels."

Three things follow, each of which the reader with the PDF should check:
- The abstract says **6 and 14 months**; the published abstract says **6-month-old** versus
  **12-month-old** GK rats. **The ages do not match.** Either the cohort changed between 2019 and
  2022 or one of the two is a slip. Worth one line of attention in the Methods.
- The abstract says **brain cortex**; the paper says **cortical and hippocampal homogenates**. The
  hippocampal arm appears to have been added later.
- The 2019 abstract carries a **3xTg-AD mouse arm** that has **no counterpart in the published
  abstract**. It may have been dropped, or it may be in the paper unmentioned in the abstract. If it
  is in the paper it is additional, and independent, animal evidence.
- Everything described as done to the cells is **exposure and measurement**. No genetic manipulation
  is named anywhere in this abstract.

**What `eci.13567` (2021) says, verbatim in the load-bearing parts:**

> "We performed studies in differentiated SH-SY5Y human neuroblastoma cells exposed to high glucose
> treated (or not) with Zfra 1-31."

> "High glucose increased the levels of activated WWOX (phosphorylated at tyrosine 33 residue),
> promoted mitochondrial dysfunction, increased reactive oxygen species (ROS) production and cell
> death. Of note, the activation of WWOX preceded the other alterations."

> "high glucose promoted a decrease in mitofusin 1 (Mfn1) and NADH-ubiquinone oxidoreductase chain 1
> (ND1), despite the increase in nuclear respiratory factor 1 (NRF1) and mitochondrially encoded
> cytochrome c oxidase I (MTCO1) levels, which suggest that the activation of mitochondrial
> biogenesis try to compensate for the existing mitochondrial anomalies. Moreover, high glucose
> caused a decrease in PI3K class III and ATG7 levels suggesting a compromised autophagic clearance
> particularly at nucleation and elongation phases."

> "Interesting, inhibition of WWOX with Zfra 1-31 prevented the alterations promoted by high glucose."

Two things follow, and they bear directly on §4:
- The stated Methods sentence is **"exposed to high glucose treated (or not) with Zfra 1-31"** — a
  two-arm design. **No siRNA, shRNA, knockout, overexpression or rescue arm is named.** This is the
  strongest evidence obtained in this session on §4.1, and it points toward *"Zfra1-31 only"*. It is
  **an abstract's Methods summary, not the paper's Methods section**, and abstracts routinely omit
  arms. It does not settle the question. It raises the prior.
- The autophagy readouts named — **PI3K class III, ATG7, and inferred "compromised autophagic
  clearance"** — are **steady-state protein levels of upstream machinery**. No flux clamp
  (bafilomycin, chloroquine, tandem mCherry-GFP-LC3) is named, and the wording "suggesting a
  compromised autophagic clearance" is exactly the inference a steady-state measurement cannot
  license. This points toward §4.5 being answered *"steady-state only"*. Again: not settled.

### 3.2 Related and adjacent papers

| PMID | Yr | Journal | Senior author | Chang (Tainan) lab? | Retrievable here | Type | Describes *this* experiment? |
|---|---|---|---|---|---|---|---|
| `26355344` | 2015 | Cell Death Dis | Chang N-S | **Yes** | **YES — tested by fetch: non-empty body, ~5 kB** (CC BY 4.0) | **Commentary / News**, not primary | No |
| `27551439` | 2015 | Cell Death Discov | Chang N-S | **Yes** | OA CC BY 4.0, `PMC4981022` — body not fetched this session | Primary | No |
| `29067327` | 2017 | Alzheimers Dement (N Y) | Chang N-S | **Yes** | OA CC BY-NC-ND, `PMC5651433` — body not fetched this session | **Primary** (Zfra in 3xTg mice, in vivo) | No |
| `18403180` | 2008 | Cell Signal | Chang N-S | **Yes** | No PMCID | Primary (Zfra S8G mutant, mitochondria) | No |
| `18371080` | 2008 | Eur J Neurosci | Chang N-S | **Yes** | **No PMCID; `is_open_access: false`; `source: not_available`** | Primary (MPP+, pY33-WOX1) | No |
| `21212468` | 2010 | Aging (Albany NY) | Chang N-S | **Yes** | OA, `PMC3034171` | Review | No |
| `32764489` | 2020 | Cancers | Chang N-S | **Yes** | OA CC BY 4.0, `PMC7464583` | Primary (cancer/spleen, in vivo) | No |
| `30158849` | 2018 | Front Neurosci | Chang N-S | **Yes** | OA CC BY 4.0, `PMC6104168` | Review | No |
| `34359949` | 2021 | Cells | Chang N-S | **Yes** | OA CC BY 4.0, `PMC8304785` | Review | No |
| `35883580` | 2022 | Cells | Chang N-S | **Yes** | OA CC BY 4.0, `PMC9323965` | Review (Jul 2022 — **predates** this paper) | No |
| DOI `10.1002/gcc.22286` | 2015 | Genes Chromosomes Cancer | (not Chang) | No | Not OA; passages via Scholar Gateway | Primary (*Drosophila*; WWOX SDR and mitochondrial respiratory complex) | No |

**The central negative result of this section: no paper found in this session describes the
Carvalho 2022 experiment.** Every Chang-lab item predates it or is unrelated to high glucose; the two
Coimbra abstracts precede it and are by the authors themselves. There is **no independent secondary
description of this experiment to fall back on**, and there is therefore no substitute for the PDF.

**One retrievable item worth a human's time in its own right, for a different reason.** PMID
`26355344` (Sze CI, Chang NS, *Cell Death Dis* 2015, `PMC4650446`, CC BY 4.0) was fetched here and
returned a real body. It is a **commentary, not primary research** — PubMed types it `News` — so it
cannot carry weight on its own. But it states the Chang lab's own position in the direction
**opposite** to the categorical objection, in two sentences that are directly on point:

> "When WWOX is knocked down by siRNA, aggregation of TPC6AΔ and TIAF1 occurs in the mitochondria to
> induce apoptosis."

> "Restoration of WWOX is expected to help survival of neural cells by preventing accumulation of
> protein aggregates in neurons. A small Tyr33-phosphorylated WWOX peptide, which mitigates
> MPP+-mediated Parkinson-like syndrome in rats, may be of therapeutic use in the restoration of
> neural function under WWOX deficiency."

This is a **secondary source** and is flagged as such. Its value is that it shows the objection's own
three lines are not unanimous even inside the laboratory that generated them: the same group has
written that WWOX **loss** damages mitochondria and that **restoring** WWOX function is the
therapeutic direction under WWOX deficiency. Whoever runs this down should chase the **primary**
references behind those two sentences rather than citing the commentary.

---

## §4 THE EXACT SCIENTIFIC QUESTION

A numbered checklist. Answer each with the PDF **and the Supplementary Information** open. Write the
answer, the figure or page it came from, and the exact sentence. An answer of "the paper does not
say" is a real and reportable answer — record it as such rather than leaving the line blank.

---

**§4.1 — Is there a GENETIC WWOX manipulation anywhere in the paper?** *(This one question decides
most of the objection's weight.)*

Search the Methods and every figure legend for: siRNA, shRNA, siWWOX, CRISPR, knockout, knockdown,
silencing, transfection, lentivirus, overexpression, rescue.

- (a) Is there **any** arm in which WWOX **protein level** is lowered or raised by a genetic means?
- (b) If yes: what was the manipulation, what was the knockdown efficiency, and **which direction did
  viability and mitochondrial function go** in that arm — under normal glucose and under high glucose?
- (c) If no: **state plainly that Zfra1-31 is the only manipulation in the paper.**

Why it decides everything: Zfra is a covalent, promiscuous 31-mer with documented targets beyond
WWOX — it binds JNK1, TRADD and NF-κB, and it suppresses Bcl-2 and dissipates mitochondrial membrane
potential in its own right. *"Zfra protects"* and *"less WWOX protects"* are two different claims,
and **only a genetic arm separates them**. Without one, the paper licenses "Zfra1-31 is neuroprotective
against high glucose" and does **not** license "reducing WWOX is neuroprotective" — and it is only the
second claim that threatens a WWOX-deficient brain.
*Current expectation from §3.1: probably no genetic arm. Do not record that as the answer.*

---

**§4.2 — Does TOTAL WWOX change, or only pTyr33-WWOX?**

- (a) Is there a blot for **total WWOX** (pan-WWOX antibody), separate from pY33-WWOX?
- (b) Under high glucose, does **total** WWOX go up, down, or not move?
- (c) Under Zfra1-31, does **total** WWOX go up, down, or not move?
- (d) Is the reported quantity a **ratio** (pY33/total) or two independent absolute measurements?
  A ratio that moves tells you nothing about abundance.
- (e) Which antibody, which catalogue number, and what is the loading control?

Why it is load-bearing: the disease model's problem is **WWOX scarcity**, not WWOX activation state.
If only the phospho-form moves and total WWOX is flat, this paper is about a **signal** on an
otherwise normal complement of protein, and it says very little about a brain in which the protein is
largely absent. If **total** WWOX also falls under high glucose and Zfra1-31 protects anyway, the
objection gets substantially stronger and must be taken seriously.

---

**§4.3 — Zfra1-31 exposure: dose, time, vehicle, and above all the inactive-peptide control.**

- (a) Concentration(s) of Zfra1-31. Was there a dose-response, or a single dose?
- (b) Exposure duration, and its timing relative to high-glucose onset (pre-treatment? co-treatment?
  rescue after injury?).
- (c) Vehicle, and whether a **vehicle-only** arm was run.
- (d) **The decisive control: was a scrambled peptide or an S8G inactive-peptide control used?**
  The Chang lab's own 2008 work (`PMID 18403180`) established **S8G-Zfra** as the clean
  loss-of-function control — the S8G mutant fails to reach mitochondria and fails to kill. **If no
  scrambled or S8G arm exists, every "Zfra1-31 rescues X" result in this paper is uncontrolled for
  non-specific peptide effects**, and the paper cannot distinguish WWOX inhibition from peptide
  loading. Record this explicitly either way.
- (e) Is there any direct evidence in *this* paper that Zfra1-31 engaged WWOX in *these* cells — a
  pull-down, a co-IP, a thermal shift — or is engagement assumed from the Chang lab's prior work?
- (f) High glucose: what concentration, over what time, and what was the **osmotic control**
  (mannitol, L-glucose)? A missing osmotic control weakens the whole injury model.

---

**§4.4 — The Goto-Kakizaki rat arm: is it more than a correlation?**

- (a) **n per group**, for each age and each brain region.
- (b) Ages: the published abstract says **6-month-old versus 12-month-old**; the group's own 2019
  conference abstract says **6 and 14 months** (§3.1). **Which is it in the paper?**
- (c) Were **non-diabetic Wistar controls** run alongside the GK rats, or is the comparison only
  young-GK versus old-GK? A young-versus-old comparison inside one diabetic strain is an age
  comparison, not a diabetes comparison.
- (d) Exactly what was measured in cortex and in hippocampus — pY33-WWOX only, or total WWOX too, or
  mitochondrial endpoints as well?
- (e) **Was any intervention given to the animals?** Did any rat receive Zfra1-31, by any route, at
  any dose? If not, say so: the animal arm is then **purely observational** and contributes no
  causal or therapeutic evidence whatsoever — it shows a phospho-signal correlating with age in a
  diabetic strain, and nothing more.
- (f) Is the 3xTg-AD mouse arm from the 2019 abstract present in this paper?

---

**§4.5 — Autophagy and mitophagy: flux, or steady state?**

- (a) List every autophagy/mitophagy readout in the paper (LC3-II, p62/SQSTM1, Beclin-1, ATG7,
  PI3K class III, PINK1, Parkin, …).
- (b) **Is there a flux clamp anywhere?** Bafilomycin A1, chloroquine, E64d/pepstatin, or a tandem
  mCherry-GFP-LC3 / mito-Keima reporter.
- (c) If there is no clamp, then every autophagy statement in the paper is a **steady-state** result
  and **cannot distinguish increased induction from blocked degradation**. The two have opposite
  therapeutic implications. Record the claim the paper makes, and record whether its design can
  support it.
- (d) Is there any **mitophagy**-specific readout at all, or only bulk autophagy? (The MeSH set
  contains neither `Autophagy` nor `Mitophagy`.)

---

**§4.6 — Does the paper state a direction for WWOX-DEFICIENT cells anywhere?**

- (a) Is high glucose the **only** stress applied, with WWOX intact throughout?
- (b) Does the Discussion address what would happen in a cell or brain with **low or absent** WWOX?
  Quote it if so.
- (c) Does the paper anywhere acknowledge that WWOX **loss of function** causes human
  neurodevelopmental disease — and if it does, does it reconcile that with proposing WWOX inhibition
  as a therapy? Quote the reconciliation verbatim, or record that there is none.
- (d) Does the paper distinguish between inhibiting **pY33-WWOX signalling** and reducing **WWOX
  protein**? This is the distinction on which the entire transferability of its conclusion rests.

---

## §5 What hangs on it

If the answer to §4.1 is **"Zfra1-31 only, no genetic arm"**, then the categorical objection loses
most of its force at this pillar. The paper would then show that a covalent, multi-target 31-mer
protects neuronal cells against a glucose insult, in cells with a **normal complement of WWOX**, with
WWOX inhibition as the authors' proposed mechanism rather than a demonstrated one — and with the
specificity of that mechanism resting entirely on whether §4.3(d) found a scrambled or S8G control.
Under that reading, the objection's third and only non-cancer, primary, independent line collapses to
"a peptide helped stressed cells", which says nothing about whether removing WWOX helps or harms, and
therefore nothing about a brain that has already removed it. The three-line convergence would then
rest on two pTyr33-activation papers from a single laboratory — an argument about an **activation
signal in protein-replete neurons**, not about protein abundance — and the working model should
record the objection as **weakened and specific to WWOX activation state**, not as a general bar on
WWOX-directed therapeutics. If §4.2 additionally shows that only the phospho-form moved while total
WWOX stayed flat, that downgrade is reinforced: the paper is then about a signal, in a setting whose
defining feature is that the signal has a protein to act on.

If instead a **genetic WWOX arm exists and agrees** — siRNA or knockout lowering WWOX protein and
*improving* neuronal viability and mitochondrial function under high glucose — the objection becomes
much harder to dismiss and must be treated as a live and serious problem. It would then be
independently demonstrated, outside the reagent's inventing laboratory, that **less WWOX protein is
protective in neurons under a metabolic stress**, which is precisely the claim that a
WWOX-antagonist strategy needs and precisely the claim that is paradoxical in a WWOX-deficient brain.
The model would have to hold two findings that point in opposite directions — WWOX loss causing
human developmental encephalopathy, and WWOX loss protecting stressed neurons — and reconcile them,
most plausibly by separating developmental requirement from adult stress response, or by positing a
non-monotonic dose-response in which both too little and too much activated WWOX are harmful. Either
way, the therapeutic reasoning would have to be rebuilt around a **window** rather than a direction,
and every existing candidate in the portfolio that assumes "more WWOX function is better" would need
re-examination against it. The difference between these two worlds is one sentence in one Methods
section, and it is currently unread.

---

**Author:** Scientist A
**Date:** 2026-09-21
**Mode:** READ-ONLY. **No canonical file was modified.** No registry, queue, ledger or current file was
touched. No commit candidate was produced. No git command was run. This packet is the only file
written.

### Tools used, and what each returned

| Tool | Call | Returned |
|---|---|---|
| `mcp__PubMed__get_article_metadata` | `["35984507"]` | Full record: 4 authors with initials and all verbatim affiliations, 2 corresponding e-mails, journal, 79(9):487, pub date 2022-08-19, 6 keywords, 13 MeSH terms, all 4 identifiers. **No grant field.** |
| `mcp__PubMed__convert_article_ids` | `["35984507"]`, id_type pmid | One record: PMCID `PMC11071800`, DOI `10.1007/s00018-022-04508-7`. **No author-manuscript variant.** |
| `mcp__PubMed__get_copyright_status` | `["35984507"]` | `is_open_access: false`, `license.type: null`, Springer exclusive-licence statement, `checked_sources: ["pubmed"]`, `found_in_pmc: 0`. Reproduced verbatim in §1.7. |
| `mcp__PubMed__get_full_text_article` | `["PMC11071800"]` | Record returned; **`full_text` = "" (body length 0)**. Abstract present. Supplementary-material pointer present (§1.8). |
| `mcp__PubMed__find_related_articles` | `["35984507"]`, `pubmed_pubmed`, max 25 | 100 similarity PMIDs (not citations). Screened into §3.2. |
| `mcp__PubMed__find_related_articles` | `["35984507"]`, `pubmed_pmc` | Single link `11071800` — confirms only one PMC record exists. |
| `mcp__PubMed__search_articles` | `Zfra AND (neuron OR SH-SY5Y OR mitochondria OR brain)` | 9 records. |
| `mcp__PubMed__search_articles` | `Moreira PI[Author] AND WWOX` | **1 record — this paper only.** Establishes the Coimbra group's independence from the Chang lab. |
| `mcp__PubMed__search_articles` | `WWOX AND (diabetes OR "high glucose")` | 16 records. |
| `mcp__PubMed__search_articles` | `(WWOX OR Zfra) AND (mitochondria OR mitophagy OR autophagy) AND (neuron OR brain OR neurodegeneration)`, 2022+ | 9 records; none describes this experiment. |
| `mcp__PubMed__get_article_metadata` | 9 Zfra/neuron PMIDs; then 3 more | Metadata for the §3.2 table; identified which are Chang-lab and which are reviews. |
| `mcp__PubMed__get_copyright_status` | 8 comparison PMIDs; 2 more | 7 of 10 open access with `source: "pmc"` and `checked_sources: ["pubmed","pmc"]` — the contrast that makes the target's `checked_sources: ["pubmed"]` diagnostic. |
| `mcp__PubMed__get_full_text_article` | `["PMC4650446"]` | **Non-empty body (~5 kB)** — retrievability test passed for that item. Content is a commentary, quoted in §3.2. |
| `mcp__Scholar_Gateway__semanticSearch` | Query on Zfra1-31 / WWOX / high glucose / siRNA | 20 passages, 15 articles. **Surfaced the two Coimbra precursor abstracts** (`10.1111/eci.13108`, `10.1111/eci.13567`) — the single most useful result of the session. |
| `mcp__Scholar_Gateway__semanticSearch` | Query on Zfra1-31 concentration / time / vehicle / control peptide / siRNA | 11 passages. Returned `eci.13567` chunks 28 and 29 again; **the Methods paragraph is cut at the chunk boundary and the dose/duration text was not recoverable.** |

**Not used, and why:** `WebFetch` and `curl` — blocked in this environment (`EGRESS_BLOCKED`; 403 from
NCBI/EBI), confirmed by previous sessions; no attempt made. No git command was run.

> 🔴 **Redaction note, Orchestrator, 2026-09-21.** Corresponding-author e-mail addresses were removed from this packet. `public_release_gate.py` blocked publication on nine `EMAIL_ADDRESS` findings, and the gate is fail-closed by design — it does not distinguish a published corresponding-author address from any other. **My brief told the delegate the addresses could be included; that was wrong and the gate was right.** The addresses are in the PubMed record for `PMID 35984507` and a human pursuing route **R7** can read them there; nothing is lost operationally.
