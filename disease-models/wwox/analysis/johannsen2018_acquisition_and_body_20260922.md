# Johannsen 2018 (`PMID 29808465`) — acquisition attempt and body extraction

**Date:** 2026-09-22 · **Actor:** Scientist A · **Status:** 🔴 **BODY NOT OBTAINED**
**File class:** non-canonical analysis. **Not a commit candidate. Not proposable for `BATCH_COMMIT`.**
**Reading debt:** ❌ **NOT discharged.** No `FULLTEXT_READ_RECEIPT` of class `complete_fulltext_read`
or `partial_fulltext_read` is earned by this session. Nothing below is a read of the body.

> ⚠️ **Nothing in this file is medical advice.**
> Bibliographic metadata and the one open-access full text quoted in §5 were retrieved from
> **PubMed / PubMed Central**. Target article DOI:
> [10.1007/s10048-018-0549-5](https://doi.org/10.1007/s10048-018-0549-5).
> Corroborating open-access article DOI:
> [10.3390/ijms21238922](https://doi.org/10.3390/ijms21238922).

---

## 0 · One-paragraph verdict

The body was **not** obtained, and this session establishes **why** with a control rather than
asserting it. **All outbound HTTP egress is blocked in this session** — `curl` and `WebFetch` both
fail their own `example.com` control — so the entire `find-fulltext` cascade (Tiers 1–9) is
**structurally unrunnable here**, not merely unsuccessful. Only three external routes are live:
the **PubMed MCP**, the **Scholar Gateway MCP**, and **WebSearch** (which returns titles/URLs and
a generated summary, and can fetch no page body). Within those three, the paper was pursued to
exhaustion: PubMed confirms **no PMCID and no retrievable copy**; Scholar Gateway's corpus was
probed with **three independent framings** and **does not contain the article at all**; and
**citation-chaining returned a decisive negative** — the field's leading review, from the
laboratory that discovered the gene, does **not** reproduce Johannsen's buffer, antibody or
HEK293 result, and in fact records the mechanism of the Q230P variant as *unknown*. Therefore
**all eleven Task-2 extraction targets remain `PREMISE: METHODS_INVISIBLE`**, and §6 is the
operative product of this session: an executable `HUMAN_ACQUISITION_PACKET`.

---

## 1 · Identifiers (complete, verified this session)

| Field | Value | Provenance |
|---|---|---|
| PMID | `29808465` | PubMed |
| DOI | `10.1007/s10048-018-0549-5` | `get_article_metadata` — **DATO** |
| PII | `10.1007/s10048-018-0549-5` | `get_article_metadata` |
| PMCID | **`null`** | `convert_article_ids` + `get_copyright_status`, both 2026-09-22 |
| Journal | *Neurogenetics* **19**(3):151–156 | PubMed |
| Publication date | 2018-05-28 | PubMed |
| Publisher | Springer (DOI prefix `10.1007`) | DOI prefix |
| Article types | `Case Reports`, `Journal Article` | PubMed |
| Language | eng | PubMed |
| Landing page | `https://doi.org/10.1007/s10048-018-0549-5` | — |
| PubMed record | `https://pubmed.ncbi.nlm.nih.gov/29808465/` | — |

### 1.1 Authors and affiliations — **the acquisition surface for a human**

| # | Author | Affiliation (verbatim from PubMed) |
|---|---|---|
| 1 | **Johannsen, Jessika** 🔴 **corresponding** | *Department of Pediatrics, University Medical Center Hamburg-Eppendorf, Hamburg, Germany.* **`the corresponding-author address printed on the paper (UKE Pediatrics; not reproduced here — see §PRIVACY)`** |
| 2 | Kortüm, Fanny | *Institute of Human Genetics, University Medical Center Hamburg-Eppendorf, Hamburg, Germany.* |
| 3 | Rosenberger, Georg | *Institute of Human Genetics, University Medical Center Hamburg-Eppendorf, Hamburg, Germany.* |
| 4 | Bokelmann, Kristin | *Institute of Clinical Pharmacology, University Medical Center Göttingen, Göttingen, Germany.* |
| 5 | Schirmer, Markus A | *Clinic of Radiotherapy and Radiation Oncology, University Medical Center Göttingen, Göttingen, Germany.* |
| 6 | Denecke, Jonas | *Department of Pediatrics, University Medical Center Hamburg-Eppendorf, Hamburg, Germany.* |
| 7 | Santer, René | *Department of Pediatrics, University Medical Center Hamburg-Eppendorf, Hamburg, Germany.* |

🔵 **INFERENZA (affiliation-based, not stated in the record):** authors **3 (Rosenberger, Human
Genetics, Hamburg)** and **4 (Bokelmann, Clinical Pharmacology, Göttingen)** are the two most
likely to have executed the **Western blot and qRT-PCR bench work** respectively — a clinical
paediatrics department is not usually where a lysis buffer is chosen. **This is a ranking heuristic
for who to ask, not a finding.** The corresponding author remains the correct first contact.

### 1.2 MeSH terms (complete, verbatim) — **evidence an experiment exists, never what it found**

`Afghanistan` · `Age of Onset` · `Cells, Cultured` · `Child` · `Consanguinity` ·
`Developmental Disabilities` · `Epilepsy` · `Family` · `Female` · **`HEK293 Cells`** · `Humans` ·
`Infant, Newborn` · `Mutation, Missense` · `Pedigree` · `Protein Domains` · **`RNA Stability`** ·
`Severity of Illness Index` · `Spasms, Infantile` · `Tumor Suppressor Proteins` ·
`WW Domain-Containing Oxidoreductase`

🔴 **BINDING — DO NOT INFER FROM MeSH.** `HEK293 Cells` and `RNA Stability` are **absent from the
abstract**, and their presence in the index is **`PREMISE: INDEXED_EXPERIMENT_EXISTS` only**.
They license exactly one statement: *an indexer, reading the body, judged these terms to apply.*
They license **none** of the following, all of which remain unknown:
- whether the HEK293 work used **Q230P** at all (it may be wild-type control, a tagged-construct
  validation, or an antibody specificity test);
- whether the HEK293 work **measured protein** or something else;
- whether `RNA Stability` reflects an **actual decay experiment** (actinomycin D / α-amanitin
  chase) or merely the indexer's summary of *"normal transcript levels by qRT-PCR"*;
- **which direction** any of those results ran.

`Cells, Cultured` is consistent with the patient fibroblasts the abstract names, and adds nothing.
`Afghanistan` + `Consanguinity` + `Pedigree` + `Family` + `Female` are the clinical half.

### 1.3 Abstract — recorded as the boundary of what is known, and as **not a read**

Verbatim, the two body-relevant sentences (PubMed abstract, `get_article_metadata`, 2026-09-22):

> *"Functional WWOX analysis was performed in fibroblasts of one patient. Transcription and
> translation were assessed by quantitative real-time PCR and Western blotting."*

> *"Functional studies showed normal levels of WWOX transcripts but absence of WWOX protein."*

> *"This could be explained by the functional data indicating an impaired translation or premature
> degradation of the WWOX protein."*

🔴 Three things the abstract itself already concedes, and which the canonical state must keep:
1. **`fibroblasts of one patient`** — **n = 1 cell line**, not two, although two patients are
   reported. The abstract says so explicitly.
2. **`absence of WWOX protein`** is a **detection statement**, and the abstract supplies **no
   floor** — no antibody, no loading control, no sensitivity. `PREMISE: DETECTION_FLOOR` stands.
3. **`impaired translation OR premature degradation`** — **the authors did not discriminate.**
   Any downstream claim that selects one branch is selecting something the source did not.
   🔴 This is the fork that decides whether the proteostasis arm has **anything to stabilise**:
   if the block is at **translation**, there is no pool to protect and a stabiliser arm is empty.

---

## 2 · TASK 1 — Routes attempted, with exact outcome

### 2.0 The blocked-egress diagnosis, established with its control **first**

| Probe | Tool | Literal result |
|---|---|---|
| **`https://example.com`** 🎯 **CONTROL** | `curl` (Bash) | `curl: (56) CONNECT tunnel failed, response 403` · `HTTP 000 size=0` |
| **`https://example.com`** 🎯 **CONTROL** | `WebFetch` | `{"error_type":"EGRESS_BLOCKED","domain":"example.com","message":"Access to example.com is blocked by the network egress proxy."}` |
| `$HTTPS_PROXY/__agentproxy/status` | Bash | **Denied by the auto-mode classifier** (`Containment Escape`) — proxy state could not be read |

🔴 **Both controls fail.** The block is **blanket and host-independent**, not
target-specific — so *every* row in §2.1 marked `EGRESS_BLOCKED` is **one single failure repeated**,
and **none of them is evidence about the paper**. Distinguishing this from a
paper-specific refusal is the whole point of running the control: a reader of this file must not
read nine blocked rows as nine independent findings about Johannsen 2018. **They are one finding
about this session's network.**

### 2.1 The `find-fulltext` cascade — invoked first, as instructed

The skill was invoked via the Skill tool before any other acquisition act. Its cascade is
reproduced below with the **literal** outcome of each tier.

| Tier | Route | Attempted as | Literal outcome |
|---|---|---|---|
| **0** | NCBI / PMC | `get_copyright_status(["29808465"])` | `pmc_id: null` · `license.type: null` · `is_open_access: false` · `source: "not_available"` · `found_in_pmc: 0` |
| **0** | NCBI idconv | `convert_article_ids(["29808465"])` | `records: [{"pmid":"29808465","requested-id":"29808465"}]` — 🔴 **PMID alone: no PMCID, and no DOI echoed** |
| **0** | PMC body fetch | `get_full_text_article` | ⛔ **Not attemptable** — the tool requires a PMCID; none exists |
| **1** | Unpaywall | `curl` + `WebFetch` → `api.unpaywall.org` | `EGRESS_BLOCKED` (both) |
| **2** | Europe PMC REST | `WebFetch` → `www.ebi.ac.uk/europepmc/...` | `EGRESS_BLOCKED` |
| **3** | OpenAlex | `curl` + `WebFetch` → `api.openalex.org` | `EGRESS_BLOCKED` (both) |
| **4** | Semantic Scholar | — | ⛔ Not attempted: same host class, control already failed. **Recorded as not-run, not as negative.** |
| **5** | Preprint servers | — | ⛔ Not applicable: a 2018 *Neurogenetics* case report with no preprint record. **Absence of a preprint is expected for this article type, and is not a finding.** |
| **6** | Google Scholar `[PDF]` | `WebSearch` (Scholar itself unfetchable) | No `[PDF]` host surfaced for the target. See §2.3. |
| **7** | CORE / BASE / OpenAIRE / Zenodo | `WebSearch` domain-restricted | **No repository copy surfaced.** See §2.3. |
| **8** | Publisher landing / HTML | `WebFetch` → `link.springer.com/article/10.1007/s10048-018-0549-5` | `EGRESS_BLOCKED` |
| **9** | Open web search | `WebSearch` ×4 | Live, but **returns no body**. See §2.3. |
| **10** | Manual handoff | — | ✅ **This is where the paper lands.** §6. |

🔵 **`get_copyright_status` returned `is_open_access: false` — and this was treated as a LICENCE
field, not a retrievability verdict.** Per standing rule, it was used to **ORDER** the remaining
attempts, never to **SKIP** them: every tier above was still attempted or explicitly recorded as
not-run with its reason. The `false` was not the reason any route failed.

### 2.2 Scholar Gateway — three independent framings, all negative, and the negative is *diagnostic*

The Orchestrator had already run one well-formed topical query that returned eight on-topic
WWOX-DEE records but **not** this one. That query was **not repeated**. Three new framings were run:

| # | Framing | Result |
|---|---|---|
| **A** | **Methods language** — *"Western blot analysis of WWOX protein in patient-derived skin fibroblasts showing normal WWOX messenger RNA levels by quantitative real-time PCR but complete absence of detectable WWOX protein, indicating impaired translation or premature protein degradation"* | 20 passages. 🔴 **Target absent.** Two passages *cite* Johannsen; none is the paper. |
| **B** | **Author + institution + allele + pedigree** — *"Johannsen Kortuem Rosenberger Bokelmann Schirmer Denecke Santer, University Medical Center Hamburg-Eppendorf, novel missense variant affecting conserved amino acid Gln230 ... two sisters of Afghan consanguineous family..."* | 20 passages / 13 articles, 2016-04-27–2025-12-11. 🔴 **Target absent**, despite the query naming **all seven authors and the institution**. |
| **C** | **Heterologous-expression framing** (aimed at the `HEK293 Cells` MeSH term) — *"Heterologous expression of mutant WWOX missense constructs in HEK293 cells ... steady-state protein level, proteasome inhibitor rescue and messenger RNA stability"* | 12 passages. 🔴 **Target absent.** Zero occurrences of `Johannsen`, `Neurogenetics`, `Gln230` or `Q230P` in the entire result. |

🔴 **DATO — the diagnosis, not merely the failure.** Every DOI returned across all three framings
carries a prefix of **`10.1002` / `10.1111` (Wiley)**, **`10.1016` (Elsevier)** or **`10.1684`
(JLE)**. **Not one `10.1007` (Springer) DOI appeared in any of the three result sets.**

🔵 **INFERENZA (strong, three-framing):** Scholar Gateway's indexed corpus **does not contain
Springer content**, and therefore **cannot ever return this paper** regardless of query quality.
**This converts four failed queries from "we didn't find it" into "this tool is the wrong
instrument for this publisher."** ⚠️ It is an inference from a sample of ~45 returned DOIs, not a
statement of the vendor's coverage policy. **Operational consequence: do not spend further
Scholar Gateway queries on any `10.1007` target.** That is a reusable routing rule, and it is the
one durable gain of §2.2.

### 2.3 WebSearch — the only live route, and what it can and cannot do

WebSearch **works** (it alone survives the egress block). It returns **titles, URLs and a
generated summary**. 🔴 **It cannot fetch a page body, and its summary is a language model's
paraphrase of snippets — it is never a verbatim locator and never a read.** Four queries:

| # | Query | Outcome |
|---|---|---|
| 1 | Exact title in quotes + `Johannsen pdf` | Top hits are the **PubMed record** and *other* WWOX papers. 🔴 **No PDF host for the target.** Summary concluded: *"you may need to use your institutional access or contact the journal directly."* |
| 2 | Domain-restricted to `core.ac.uk`, `base-search.net`, `ediss.sub.uni-hamburg.de`, `uke.de`, `ediss.uni-goettingen.de`, `zenodo.org`, `semanticscholar.org`, `europepmc.org`, `openalex.org` | Returned **UKE staff profile pages** for Johannsen, Kortüm, Rosenberger, Denecke and the **UKE research portal** `fis.uke.de`. 🔴 **No full-text file.** |
| 3 | `fis.uke.de` + exact title | **Confirms the publication is listed on UKE author profiles.** 🔴 **No deposited file surfaced.** |
| 4 | German-language thesis search (`Dissertation WWOX Gln230 ... Hamburg-Eppendorf ediss ... Western Blot`) | Returned **ten unrelated UKE dissertations**. See the warning immediately below. |

🔴🔴 **A trap, recorded because it nearly became a finding.** In query 4 the WebSearch summarizer
asserted that `ediss.sub.uni-hamburg.de/bitstream/ediss/7671/1/Dissertation.pdf` *"appears to be
the dissertation you're looking for"* and that it *"should contain the detailed research
including information about fibroblasten and Western Blot."*

**This is `IPOTESI` generated by a summarizer, and it is unverified and unverifiable here.** The
model matched *institution* + *department name* + *repository*, **not content**. `WebFetch` on
that exact URL returned `EGRESS_BLOCKED`, so **not one character of that PDF was seen**. The
phrase *"should contain"* is the summarizer's prediction, not a report.
⚠️ **Had this been copied forward, the laboratory would have acquired a fabricated Methods source.**
It is carried into §6 as a **candidate to check**, ranked and explicitly labelled unverified —
never as a located copy.

### 2.4 Citation-chaining — executed, and it returns a **decisive and useful negative**

**Method.** PubMed was searched for the allele; the one retrievable open-access downstream review
was pulled **in full** through the PMC route and read for any reproduction of Johannsen's Methods.

**Step 1 — allele search.** `WWOX AND (Gln230 OR Q230P OR "p.Gln230Pro" OR "c.689A>C")` →
`total_count: 2` — **`30853297`** and **`29808465`** (the target).
- 🔴 `30853297` (Weisz-Hubshman 2019, the *other* Q230P primary, `FT-117`) → `convert_article_ids`
  returns **PMID alone, no PMCID**. **Also unobtainable here.** Both Q230P primaries are closed.

**Step 2 — retrieve and read the downstream review.** `get_full_text_article(["PMC7727818"])`
succeeded — **Aldaz & Hussain, *"WWOX Loss of Function in Neurodevelopmental and Neurodegenerative
Disorders"*, Int J Mol Sci 2020, `PMID 33255508`, [DOI 10.3390/ijms21238922](https://doi.org/10.3390/ijms21238922)**
— the authoritative review from **the laboratory that discovered the gene**.

**The result of reading it for Johannsen's Methods:**

🔴 **DATO — the review reproduces none of the eleven targets.** No lysis buffer, no centrifugation,
no antibody, no epitope, no loading control, no detection floor, no HEK293 Q230P experiment, no
RNA-stability experiment. **Nothing in §4 is recoverable at second hand from it.**

🔴 **DATO — and it goes further than silence.** Verbatim, on the Q230P allele specifically:

> *"the p.Gln230Pro mutation was found both as a biallelic mutation and also in heterozygous
> compound cases combined with other mutations and has been reported in a total of 8 WOREE cases
> affecting a total of 6 different families."*

> *"This mutation is found within the large SDR domain of WWOX, not obviously affecting a critical
> enzymatic functional motif."*

> *"Currently, the mechanistic effects of most of the observed missense mutations on WWOX function
> are not known, therefore, it would be of interest to undertake studies exploring the functional
> impact of specific hotspot mutations since could lead to identify additional protein functional
> motifs and in turn provide further mechanistic insight."*

🔵 **INFERENZA — and this is the single most consequential line in this file.** A 2020 review from
the discovering laboratory, which **cites Johannsen 2018 elsewhere in the same article**,
nevertheless records the mechanistic effect of Q230P as **not known** and calls for exactly the
functional studies Johannsen is held to have performed. Two readings are compatible:
**(a)** the reviewers did not regard an n = 1 fibroblast Western blot as mechanistically
settling; or **(b)** they were reasoning, as everyone downstream has been, **from the abstract**.
⚠️ **Both are inferences about the reviewers' state of mind and neither is established.** What *is*
established is the operational point: **the field's own authority does not treat "complete loss of
WWOX protein" as a closed mechanistic finding.** The canonical state's existing
`PREMISE: DETECTION_FLOOR` and its `WM v2.1 → v3.0` retraction of
`mRNA normale + proteina assente = degradazione` are **corroborated from outside**, not weakened.

🔵 **INFERENZA (acquisition-relevant):** 47 citations across 7 canonical files, plus this review,
plus the citing papers in §2.2 — and **not one of them carries a Methods detail from this paper.**
This is the signature of a paper **whose citers have only ever read its abstract**. It means
citation-chaining is **exhausted as a class**, not merely unlucky: 🔴 **there is no second-hand
route to §4. The body itself is the only source, and a human must fetch it.**

**Step 3 — replication search.** `WWOX missense variant functional characterization protein
stability HEK293 transfection degradation` → **`total_count: 0`**.
🔴 **This zero is NOT evidence that no such paper exists.** It is a seven-clause `AND` chain over
`[All Fields]`, which **does not index Methods sections or supplements** — precisely the
established failure mode by which *"a reagent named only in Methods is invisible."* Recorded as
**uninformative**, not as a negative finding.

### 2.5 Routes deliberately NOT taken — hard-blocked for this session

| Route | Status |
|---|---|
| Emailing the corresponding author (`the corresponding-author address printed on the paper (UKE Pediatrics; not reproduced here — see §PRIVACY)`) | ⛔ **HUMAN_REQUIRED — not done.** Written as a human instruction in §6.3 only. |
| Contacting any author or institution by any channel | ⛔ **HUMAN_REQUIRED — not done.** |
| Requesting material / reagents | ⛔ **HUMAN_REQUIRED — not done.** |
| Purchasing the article, TDM keys, or committing any funds | ⛔ **HUMAN_REQUIRED — not done.** |
| Shadow-library mirrors | ⛔ Not queried. Outside the skill's contract; the operator's own choice. |
| `git` (including read-only) | ⛔ Not run. |
| Any `*_current.md`, registry, queue, ledger, receipt, state-manifest write | ⛔ Not touched. This file is the only write. |

---

## 3 · TASK 2 — Body extraction

🔴 **NOT PERFORMED. The body was never opened.** No verbatim locator from Johannsen 2018 exists in
this file, and none may be created from it. Per rule 5b, a reading that supports no statement
**waives with an argument**: the argument is that **zero characters of the article body were
available to this session**, for the reason established with a control in §2.0.

---

## 4 · The eleven targets — every one `PREMISE: METHODS_INVISIBLE`

**This table is the extraction sheet for whoever obtains the PDF. It is deliberately un-filled.**

| # | Target | Status | What is known, and strictly from where |
|---|---|---|---|
| 1 | **Heterologous Q230P expression** | 🔴 `METHODS_INVISIBLE` | `HEK293 Cells` is in MeSH, **absent from the abstract**. `PREMISE: INDEXED_EXPERIMENT_EXISTS`. **Whether the construct was Q230P, and what it showed, is unknown.** |
| 2 | **HEK293 Q230P protein measurements** | 🔴 `METHODS_INVISIBLE` | Same MeSH term. **No measurement, direction or magnitude is known.** |
| 3 | **RNA stability experiments** | 🔴 `METHODS_INVISIBLE` | `RNA Stability` is in MeSH, **absent from the abstract**. ⚠️ May index a real decay chase **or** merely the indexer's reading of *"normal levels of WWOX transcripts."* **Undetermined.** |
| 4 | **Translation measurements** | 🔴 `METHODS_INVISIBLE` | Abstract says translation was *"assessed by ... Western blotting"* — i.e. **assessed via steady-state protein**, not by a translation assay. **No polysome, no ribosome profiling, no ³⁵S/puromycin labelling is known to exist.** |
| 5 | **Degradation experiments** | 🔴 `METHODS_INVISIBLE` | Abstract offers *"premature degradation"* as **one of two unresolved explanations**. **No evidence any degradation experiment was performed.** |
| 6 | 🔴 **Lysis buffer composition** — **highest priority** | 🔴 `METHODS_INVISIBLE` | **Nothing.** Not in abstract, not in MeSH, not in any citing source. |
| 7 | 🔴 **Centrifugation speed / time; supernatant handling** | 🔴 `METHODS_INVISIBLE` | **Nothing.** |
| 8 | 🔴 **Insoluble fraction / pellet analysis** | 🔴 `METHODS_INVISIBLE` | **Nothing.** |
| 9 | **Proteasome / lysosome interventions** | 🔴 `METHODS_INVISIBLE` | **Nothing.** No MG-132, no chloroquine, no bafilomycin is known either way. |
| 10 | 🔴 **Antibody identity; epitope vs Gln230** | 🔴 `METHODS_INVISIBLE` | **Nothing.** No catalogue number, clone, host or immunogen. |
| 11 | 🔴 **Detection floor / dilution series / stated sensitivity** | 🔴 `METHODS_INVISIBLE` | **Nothing.** `CLAIM 030`'s `PREMISE: DETECTION_FLOOR` is **unmoved by this session.** |

### 4.1 Why items 6, 7, 8 and 10 are jointly the highest-value lines in the paper

🔵 **IPOTESI — a mechanism this session could not test and which the body may settle in one line.**
A misfolded SDR-domain missense product can partition into a **detergent-insoluble pellet**. If
Johannsen's protocol used a mild buffer (e.g. NP-40 / Triton X-100) and **blotted the supernatant
only, discarding the pellet**, then *"absence of WWOX protein"* would be a statement about the
**soluble fraction**, and an insoluble Q230P pool could exist, unmeasured. ⚠️ **This is a
hypothesis about an unread Methods section and nothing more.** It is recorded because it makes
items **6 + 7 + 8** a single decisive question rather than three bookkeeping fields — and because
**it changes the therapeutic reading**: an insoluble pool is a target for a folding/chaperone
strategy, whereas a translation block is not. Item **10** is its twin: an antibody raised against
an epitope **at or near residue 230** could fail to bind the mutant for **epitope reasons rather
than abundance reasons** — a false zero with the same appearance.

🔴 **None of these is asserted. They are the reason the questions in §6.4 are ordered as they are.**

---

## 5 · Collateral findings — separated by epistemic class

**DATO** (from the open-access review, `PMID 33255508`, [DOI](https://doi.org/10.3390/ijms21238922),
read in full this session):
- `p.Gln230Pro` is reported in **8 WOREE cases across 6 families**, both **biallelic** and in
  **compound-heterozygous** configurations.
- It lies *"within the large SDR domain of WWOX, **not obviously affecting a critical enzymatic
  functional motif**."*
- The review states the mechanistic effects of most WWOX missense mutations *"are not known."*

**DATO — citation drift observed directly, and it is the extraction-damage class:**
- One citing article (`10.1002/ajmg.a.63074`) writes ***"homozygous p.Gln239Pro"*** — a **digit
  substitution**, `230 → 239`, while citing Johannsen for the fibroblast result.
- Another (`10.1016/j.ijdevneu.2019.10.003`, Table 1) writes ***"c.689A>C(p.G230P)"*** — **`Q` → `G`**,
  a wrong amino acid, against the correct nucleotide change, in the same cell.
- 🔵 **INFERENZA:** the allele is being **mis-transcribed by its own citers in at least two
  independent directions**. ⚠️ **Operational consequence:** any PubMed or corpus search keyed on
  `Q230P` / `Gln230Pro` **will silently miss records carrying these corrupted spellings** — and
  §2.4 Step 1 returned only 2 records, so the true citing set is **larger than any allele-keyed
  search will show**. Search on **`c.689A>C`** as the primary key; it survived both corruptions.

**IPOTESI (explicitly not established):** §4.1, the soluble/insoluble partition and the epitope
hypothesis. Both are questions for the body, not findings.

---

## 6 · TASK 3 — `HUMAN_ACQUISITION_PACKET`

> 🔴 **Everything in this section is written as instructions for a human to execute.**
> **No action in it was taken by this session.** No email was sent, no author or institution was
> contacted, no material was requested, no funds were committed or proposed.

### 6.1 Copy-paste identifier block

```
Johannsen J, Kortüm F, Rosenberger G, Bokelmann K, Schirmer MA, Denecke J, Santer R.
A novel missense variant in the SDR domain of the WWOX gene leads to complete loss of
WWOX protein with early-onset epileptic encephalopathy and severe developmental delay.
Neurogenetics. 2018 Jul;19(3):151-156.   [published online 2018-05-28]

PMID:  29808465
DOI:   10.1007/s10048-018-0549-5
PMCID: none (verified 2026-09-22)
URL:   https://doi.org/10.1007/s10048-018-0549-5
       https://pubmed.ncbi.nlm.nih.gov/29808465/
Publisher: Springer  ·  Journal: Neurogenetics  ·  ISSN 1364-6745 (print) / 1364-6753 (online)
Corresponding author: Jessika Johannsen — the corresponding-author address printed on the paper (UKE Pediatrics; not reproduced here — see §PRIVACY)
  Department of Pediatrics, University Medical Center Hamburg-Eppendorf, Hamburg, Germany
```

### 6.2 Every route tried, with its precise failure mode

| Route | Failure mode — **precise** |
|---|---|
| `curl` → any host | `CONNECT tunnel failed, response 403`. **Control `example.com` fails identically** → blanket block, not target-specific. |
| `WebFetch` → any host | `EGRESS_BLOCKED`. **Control `example.com` fails identically** → blanket block. |
| Agent-proxy status endpoint | Denied by auto-mode classifier (`Containment Escape`). Proxy state unreadable; block could not be characterised further. |
| NCBI `convert_article_ids` | Returns **PMID alone**. No PMCID. Not a network failure — **the record genuinely has no PMC deposit**. |
| NCBI `get_copyright_status` | `pmc_id: null`, `source: "not_available"`, `found_in_pmc: 0`. **LICENCE field `is_open_access:false` — used to order, not to skip.** |
| PMC `get_full_text_article` | **Unusable by construction** — requires a PMCID that does not exist. |
| Unpaywall / OpenAlex / Europe PMC / Semantic Scholar | `EGRESS_BLOCKED` (or not-run for the same reason). 🔴 **These are one failure, not four.** |
| Springer landing page | `EGRESS_BLOCKED` on `link.springer.com`. **Paywall status never even reached.** |
| Scholar Gateway ×3 framings | Returned results; **target absent from all three**. Zero `10.1007` DOIs across ~45 returned. → **corpus lacks Springer content** (INFERENZA). |
| Google Scholar / CORE / BASE / repositories | Reachable only through WebSearch, which returns **no file**. No repository copy surfaced. |
| `ediss.sub.uni-hamburg.de` thesis candidate | `EGRESS_BLOCKED`. 🔴 **Candidate is UNVERIFIED — surfaced by a summarizer on institution-name match, content never seen.** |
| Citation-chaining (allele search + full read of `PMC7727818`) | **Succeeded as a procedure, returned a negative as a result.** No downstream source reproduces buffer, antibody, epitope, floor or the HEK293 result. |
| PubMed replication search | `total_count: 0` — **uninformative**: `[All Fields]` does not index Methods or supplements. |

### 6.3 Ranked routes a human can execute that this session cannot

> Ranked by **expected yield ÷ effort**. 🔴 **Each is an instruction. None was performed.**

**① Institutional / library access to Springer — highest yield, lowest effort, zero marginal cost.**
Open `https://doi.org/10.1007/s10048-018-0549-5` from a browser on a subscribing network, or via
the institution's proxy / OpenAthens / Shibboleth. *Neurogenetics* is a standard Springer
subscription title and is held by most medical-school libraries. **Six pages (151–156).**
⚠️ **Download the Supplementary Information too** — for a paper of this length, the Methods detail
in §4 is **more likely to sit in a supplement than in the printed body**, and the supplement is a
separate click that is easy to miss.

**② The authors' own institutional repository — free, legitimate, and specifically indicated here.**
German universities operate Pure/DSpace portals that frequently hold the **accepted manuscript**
under the publisher's green-OA embargo (12 months for Springer; **this paper is from 2018, so any
embargo has long expired**).
- **`fis.uke.de`** — the UKE research portal. **Confirmed this session to list the publication.**
  Whether a **file** is attached could not be determined (egress blocked). **Check the record for a
  downloadable accepted manuscript.**
- **Göttingen** — authors 4 and 5 are at UMG; check the Göttingen research information system and
  **GoeScholar**.
🔵 This route is ranked second because it is **free, requires no one's permission, and the
green-OA manuscript contains the full Methods section** — which is the entire object of §4.

**③ Interlibrary loan (ILL) / document delivery.** Standard ILL on the citation in §6.1; in
Germany, **SUBITO** serves this title directly. Turnaround typically 24–72 h.
⚠️ **ILL usually delivers the article body only — explicitly request the Supplementary Information**,
or route ② / ① may still be needed afterwards for the supplement.

**④ Direct request to the corresponding author — highest yield of all, but slowest, and it is a
human act.** `the corresponding-author address printed on the paper (UKE Pediatrics; not reproduced here — see §PRIVACY)`. 🔴 **This session did not and may not send it.**
🔵 **If a human does write, the message should ask for more than the PDF**, because the author can
answer in two sentences what the PDF may take a figure legend to settle:
> the **antibody** (vendor, catalogue number, clone, immunogen/epitope region relative to residue
> 230); the **lysis buffer composition**; whether the **insoluble pellet** was ever blotted; and
> whether any **proteasome or lysosome inhibitor** was tried.
⚠️ Co-authors **Rosenberger** (Human Genetics, Hamburg) and **Bokelmann** (Clinical Pharmacology,
Göttingen) are the plausible bench executants (§1.1, INFERENZA) and are reasonable alternates if
the corresponding author does not reply.

**⑤ Springer Nature SharedIt.** Authors of Springer papers receive a free read-only `rdcu.be`
sharing link. ⚠️ **Read-only, no download, and it may or may not expose the supplement** — useful
for reading the Methods, insufficient for a durable archived artifact. **Subordinate to ①–④.**

**⑥ The unverified Hamburg dissertation candidate — check, do not trust.**
`https://ediss.sub.uni-hamburg.de/bitstream/ediss/7671/1/Dissertation.pdf`
🔴 **This URL was produced by a WebSearch summarizer on an institution-name match and its content
was never seen.** The probability it concerns WWOX at all is **unquantified**. A human can open it
in seconds and discard it in seconds. ⚠️ **If it does concern this work, a German medical
dissertation typically reproduces the Methods in far greater detail than the paper** — which is
why a lead this weak is still worth a single click. **More general instruction:** search
`ediss.sub.uni-hamburg.de` and the Göttingen thesis repository for a dissertation on WWOX /
epileptic encephalopathy from the UKE Pediatrics or Human Genetics groups, 2016–2021.

**⑦ Publisher TDM API.** Springer's TDM API requires an account with institutional entitlement.
**If the human already has ①, this adds nothing.** Listed for completeness.

**⑧ WWOX Foundation / patient-advocacy network.** Used successfully for other WWOX clinical papers
in this corpus. 🔴 **A human act, not taken here.**

🔴 **Explicitly excluded and not recommended by this session:** any paid purchase (HUMAN_REQUIRED,
hard-blocked), and shadow-library mirrors (outside the skill's contract; the operator's own
choice, and not advocated here).

### 6.4 The exact ordered extraction list — **one pass, no second trip**

> 🔴 **Whoever obtains the body: work this list in order and answer every line, including the ones
> whose answer is "the paper does not say."** A recorded *"not stated"* is a finding and closes a
> premise; a skipped line silently reopens it and costs the acquisition twice. **Capture each
> answer verbatim with its locator — section, figure or table (rule 5b) — while the document is
> open.**

**Block A — the Western blot's detection floor (settles `CLAIM 019`, half of `CLAIM 030`):**
1. **Antibody**: vendor, catalogue number, clone, host species, monoclonal/polyclonal.
2. **Epitope / immunogen region** — and 🔴 **where it sits relative to residue 230**. (If the
   epitope spans Gln230, *"not detected"* may be an **epitope** failure, not an abundance failure.)
3. Dilution, blocking agent, incubation conditions.
4. **Loading control** used, and whether it is shown on the same membrane.
5. **How much total protein was loaded per lane**, and the number of lanes.
6. **Was a dilution series of wild-type lysate run to establish a detection floor?** If yes, the
   **lowest wild-type input still giving signal** — 🔴 *this single number is the floor, and the
   entire "not detected ≠ absent" premise turns on it.*
7. Exposure time(s); whether film or digital imager; whether a longer exposure was attempted.
8. Is the blot **quantified** (densitometry, with n and statistics) or shown as a single image?
9. **n** — how many independent lysates / passages / biological replicates. (Abstract says
   *"fibroblasts of one patient"* — 🔴 **confirm whether the second sister's line was blotted at all.**)
10. Control lines used: parental? carrier heterozygote? unrelated healthy fibroblasts? how many?

**Block B — sample preparation (items 6, 7, 8 — the highest-priority lines in the paper):**
11. 🔴 **Lysis buffer, full composition**: base, salt, **detergent identity and percentage**
    (RIPA vs NP-40 vs Triton X-100 vs SDS), reducing agent, protease/phosphatase inhibitors, pH.
12. 🔴 **Centrifugation**: speed (**record `g`, and note whether the paper states rpm instead**),
    duration, temperature.
13. 🔴 **Supernatant handling** — was the **supernatant alone** blotted?
14. 🔴 **Was the insoluble pellet retained, resolubilised (e.g. in SDS/urea) and blotted?**
    If it was not, **record that explicitly** — it is the finding, and it bounds every downstream
    claim to the **soluble fraction only**.
15. Cell type, passage number, culture and harvest conditions; any treatment before lysis.

**Block C — the HEK293 experiment (MeSH says it exists; nothing else is known):**
16. **What was expressed** — wild-type, Q230P, both? Tagged (which tag, which terminus) or untagged?
17. **Why** was it done — variant testing, antibody validation, or an unrelated control?
18. **What was measured**, and 🔴 **which way did the result run?**
19. Was **mutant protein detectable in HEK293** when it was not in fibroblasts? 🔴 **If yes, that
    single fact reframes the fibroblast result as cell-context-dependent rather than absolute.**
20. Transfection method, time to harvest, normalisation.

**Block D — RNA (MeSH `RNA Stability`):**
21. qRT-PCR: **how many amplicons**, and **where in the transcript** (5′ / 3′ / spanning the
    variant)? 🔴 *A single 3′ amplicon cannot exclude a 5′ defect.*
22. Reference gene(s); n; statistics; **absolute or relative quantification**.
23. 🔴 **Was an actual RNA-decay experiment run** (actinomycin D / α-amanitin chase with a
    time-course)? If yes: agent, concentration, timepoints, and the measured half-life.
    **If no — record `not performed`**, and the `RNA Stability` MeSH term is then explained as the
    indexer's reading of the qRT-PCR result, not as a decay experiment.
24. Any NMD assessment (e.g. cycloheximide/puromycin inhibition of NMD).

**Block E — turnover and route (items 5 and 9):**
25. 🔴 **Any proteasome inhibitor** (MG-132, bortezomib, lactacystin)? Concentration, duration,
    result — **including a negative**.
26. 🔴 **Any lysosome/autophagy intervention** (chloroquine, bafilomycin A1, NH₄Cl, leupeptin)?
    ⚠️ Per `gold_is_in_the_details`, a **proteasome-only negative is uninformative, not a
    refutation** — record which routes were tested **and which were not**.
27. Any **cycloheximide chase** / half-life measurement? Any **ubiquitination** assay?
28. Any **immunofluorescence / localisation** of WWOX in the patient fibroblasts?

**Block F — the fork the abstract leaves open (the decisive question):**
29. 🔴 **Does the body contain any experiment that discriminates *impaired translation* from
    *premature degradation*?** If it does not, **record that explicitly** — it converts the
    canonical `not discriminated` from an assumption into a **verified** property of the source.
30. What exactly do the Discussion and any Limitations paragraph concede about sensitivity,
    about **n = 1**, and about fibroblasts as a proxy for neurons?

**Block G — surface and provenance hygiene (rules 5c–5e):**
31. Record the **rendered page** as the reference surface; note whether a structured
    (XML/HTML) surface exists or only a PDF, and **declare the absence** if only a PDF.
32. 🔴 **Inspect every figure at original resolution — never through a text conversion.** Western
    blot panels, significance asterisks and lane labels are exactly what text extraction destroys.
33. Watch for: deleted superscripts and variant labels; **empty parentheses meaning a deleted
    token, not an absent one**; **E-notation as the only exponent-safe form**; case-sensitive
    false negatives; and the `Wwox⁻/⁻` vs `Wwox⁺/⁻` control-character class.
34. 🔴 **Download the Supplementary Information and treat it as part of the body** — for a
    six-page case report, Blocks B, C and E are more likely to live there than in the print pages.
35. Fingerprint both artifacts (`article_binary`, `article_text`), declare the extraction method,
    and emit the `FULLTEXT_READ_RECEIPT` before reporting the paper as read.

---

## 7 · What this session changes, and what it does not

**Unchanged — and deliberately so:**
- 🔴 No canonical file, registry, queue, ledger, receipt or state manifest was read-modified or
  written. This file is the session's only write.
- `CLAIM 019`, `CLAIM 030` and `PAPER 041` are **untouched**. `PREMISE: DETECTION_FLOOR` stands.
- **Reading debt is NOT discharged.** `29808465` remains `abstract_only` and unread.

**Added, as non-canonical analysis only:**
1. 🔵 **The unobtainability is now diagnosed rather than asserted** — with an `example.com` control
   proving the block is **blanket**, so the nine `EGRESS_BLOCKED` rows are **one** failure, and the
   earlier `unrecoverable_by_these_routes` verdict is confirmed **without being over-generalised**
   into *"irrecoverable."* 🔴 **The paper is obtainable — by a human with library access. It is
   this session that cannot reach it.**
2. 🔵 **A reusable routing rule:** Scholar Gateway's corpus returned **zero `10.1007` DOIs across
   three framings** → **do not spend Scholar Gateway queries on Springer targets.** This is the
   durable gain from four queries that all failed.
3. 🔴 **Citation-chaining is exhausted as a class, and that is itself the finding.** A full read of
   the discovering laboratory's own review reproduces **none** of the eleven targets and records
   the Q230P mechanism as *"not known"* — **independent external corroboration** of the canonical
   `WM v2.1 → v3.0` retraction, and proof that **no second-hand route to §4 exists.**
4. 🔵 **Search-key correction:** the allele is mis-transcribed by its own citers in **two**
   independent directions (`p.Gln239Pro`; `p.G230P`). **Key future searches on `c.689A>C`**, which
   survived both corruptions — any `Q230P`/`Gln230Pro` search is undercounting.
5. 🔴 **A fabricated-source trap was caught and quarantined** (§2.3): a WebSearch summarizer
   asserted a dissertation PDF *"should contain"* the Methods, on an institution-name match, with
   its content never seen. It is carried forward **only** as an unverified item ⑥ to click.

**Two live failure-mode instances observed this session**, consistent with the eight established:
- 🔴 **Silent OR-block drop:** `WWOX AND (Gln230 OR Q230P OR "p.Gln230Pro" OR "c.689A>C")` →
  `query_translation` shows only `"Gln230" OR "Q230P" OR "c.689A>C"`. **`"p.Gln230Pro"` was
  dropped with no error.** The count returned was **not the count of the query as written.**
- 🔴 **Quoted wildcards do not expand:** `fibroblast*` and `epilep*` inside quotes were translated
  as **literal strings** `"fibroblast*"[All Fields]`, collapsing a broad query to `total_count: 1`.
  A `1` that looks like precision and is an artifact.

---

## 8 · Provenance

Bibliographic metadata, identifier conversion, copyright status and the open-access full text
quoted in §2.4/§5 were retrieved from **PubMed / PubMed Central**.

- Target article — Johannsen J *et al.*, *Neurogenetics* 2018;19(3):151-156 · `PMID 29808465` ·
  [DOI 10.1007/s10048-018-0549-5](https://doi.org/10.1007/s10048-018-0549-5) — 🔴 **abstract and
  metadata only; body never opened.**
- Aldaz CM & Hussain T, *"WWOX Loss of Function in Neurodevelopmental and Neurodegenerative
  Disorders"*, *Int J Mol Sci* 2020;21(23):8922 · `PMID 33255508` · `PMC7727818` ·
  [DOI 10.3390/ijms21238922](https://doi.org/10.3390/ijms21238922) — full text retrieved and read
  **for the single question of whether it reproduces Johannsen's Methods.** It does not.
- Weisz-Hubshman M *et al.* · `PMID 30853297` — the other Q230P primary; **no PMCID, also
  unobtainable here.**

**Non-canonical. Not a commit candidate. Not proposable for `BATCH_COMMIT`.**

---

# 🔴 ORCHESTRATOR — PRIVACY REDACTION, 2026-09-22

**§PRIVACY.** This file originally carried the corresponding author's literal email address in four
places. `scripts/public_release_gate.py` returned **`BLOCK_PUBLICATION`, 4 blocks,
`EMAIL_ADDRESS`** — correctly. This is the **public edition**; a non-placeholder address is not
publishable here even when the same address is printed on the paper's own title page, because the
gate's rule is categorical and the repository is distributed.

All four occurrences are replaced with a pointer. **Nothing scientific is lost:** a human executing
the acquisition packet reads the address off the paper, which they must open anyway. Gate
re-run after redaction: **PASS, 0 blocks.**

**Rule for delegates, restated:** an acquisition packet names **routes and institutions**, never a
personal contact string. This is the second privacy-class item this session has had to correct at
the gate rather than at the source.

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V1 · 🟢 The egress diagnosis is confirmed at first hand, and it reframes the whole file

I ran the control myself: `https://example.com` → **`000`, connection failed**;
`https://link.springer.com/article/10.1007/s10048-018-0549-5` → **`000`, identical failure**.

🟢 **CONFIRMED, and the methodological point is the important one.** The nine blocked rows in §1
are **one failure repeated nine times**, not nine findings about this paper. A file that listed them
as nine independent negatives would have manufactured evidence of unobtainability out of a single
network fact. **Naming the control is what makes the difference between a diagnosis and a tally**,
and this file names it.

Consequence for the `find-fulltext` skill: its Tiers 1–9 are **structurally unrunnable in this
deployment**, and it lands correctly at the Tier-10 human handoff. That is the skill working, not
failing.

## V2 · The Scholar Gateway / Springer boundary — upgraded, but not to a rule

Across **four independently-framed probes** (three by this delegate, one by me earlier today) the
gateway returned roughly **53 records on WWOX-DEE topics and zero with a `10.1007` prefix.**

🟡 **`INFERENZA` (strong), not `DATO`.** The residual confound is **topicality**: all four probes
were WWOX-DEE queries, and it is conceivable — if unlikely — that Springer holds little on this
exact topic. What the probes establish firmly is the operational half: **a WWOX-DEE query will not
surface a Springer record on this route.**

🔴 **I decline to promote it to the routing rule the delegate proposes** (*"don't spend SG queries
on `10.1007` targets"*) until one cheap decisive test is run: a query on a subject whose literature
is **Springer-dominated and unrelated to WWOX**. If that also returns zero `10.1007`, the rule is
earned. `REVIVAL_TRIGGER`: that test. This is the same discipline the session applies to PubMed
zeros — a zero from a query is a fact about the query until it is shown to be a fact about the
corpus.

## V3 · 🟢 The citation-chaining negative is the file's real result

That the discovering laboratory's **own 2020 review** reproduces **none** of the eleven targets, and
states that *"the mechanistic effects of most of the observed missense mutations on WWOX function
are not known"*, does more than close a route. It means **the field's own summary of this allele
does not carry the experiment's conditions** — so no second-hand source can supply them. The body
is the only source. Recorded as a **measured exhaustion of a route class**, not as a failure to find
something.

## V4 · 🔴 Three escalations, all endorsed, one of them the most important thing in the file

1. 🔴 **The fabricated-source trap, caught.** A search summariser asserted that a Hamburg
   dissertation PDF *"should contain"* the fibroblast Western blot — on an **institution-name
   match, with the content never seen**, the URL being egress-blocked. Quarantining it as
   *unverified, click-to-check* is exactly right. **Had it been carried forward, this laboratory
   would have acquired a fabricated Methods source for its single most load-bearing measurement.**
   This is the clearest instance this session has produced of why a generated summary is not a read.
2. 🔴 **Citation drift breaks allele-keyed search.** Citers mis-transcribe in two independent
   directions — `p.Gln239Pro` (digit) and `p.G230P` (wrong amino-acid letter) — while **`c.689A>C`
   survives both.** 🟢 **Adopted as a standing search rule: key allele searches on the cDNA change,
   not the protein change.** Every `Q230P` / `Gln230Pro` search in this repository's history is
   therefore **undercounting by an unmeasured amount**, and that is a live, checkable debt rather
   than an abstraction.
3. 🔴 **Two live failure-mode instances**, both consistent with what this corpus already documents:
   a quoted term **silently dropped** from an `OR` block (the `query_translation` proves the
   returned count is not the query as written), and **quoted wildcards that do not expand**,
   collapsing a broad query to `total_count: 1` — *"a 1 that looks like precision and is an
   artifact."* That last formulation is new and worth keeping: this corpus has catalogued misleading
   **zeros** at length and had not until now catalogued a misleading **one**.

## V5 · What is NOT established, restated because the file's value depends on it

**All eleven extraction targets remain `PREMISE: METHODS_INVISIBLE`.** `HEK293 Cells` and
`RNA Stability` are logged as `PREMISE: INDEXED_EXPERIMENT_EXISTS` only — they do **not** establish
that `Q230P` was the construct, what was measured, which direction any result ran, or that a real
decay chase exists rather than an indexer's reading of *"normal levels of WWOX transcripts"*.
**No reading debt is discharged; `29808465` stays `abstract_only`; no receipt is earned.**

## V6 · Information gain and grade

**INFORMATION GAIN: MEDIUM.** The body was not obtained and the primary question is unmoved — but
the file converts an open question into a **bounded, human-executable one**, closes a route class by
measurement, catches a fabrication before it entered the model, and produces a search rule that
retroactively qualifies existing counts. A negative result delivered with its control named.

**Grade: B+.** Held below A only because the deliverable the task existed for — the Methods — is
absent, which is the environment's doing rather than the delegate's.

**No row is canonical; none is proposed for `BATCH_COMMIT`.** The author-contact route stays
`HUMAN_REQUIRED` and was correctly not attempted.
