# Acquisition wave — 2026-09-22

**Actor:** `scientist-5` (ACQUISITION AND READING) · **Repo commit at state check:** `3aca32d1027f`
**Scope:** the five `unread_premises` blocking `BATCH_COMMIT` (LINT `unread_premises: 5/0`), plus one
open lead (`PMID 36828035`).

> **Not medical advice.** Public edition, genotype-class level. Alleles and models are never pooled.
> **This file writes no receipt.** § 6 holds *proposed* receipt payloads for the Orchestrator to
> consider. The ledger `fulltext_read_receipts.jsonl` was not touched, and `fulltext_receipts.py
> record` was not run.

---

## § 0 · The state check, before any fetch

Run first, exactly as the dispatch required:

```bash
python3 framework/scripts/reading_state.py --out /tmp/rs_s5.md     # 135 papers, 199 receipts
python3 framework/scripts/paper_packet.py packet --pmid <PMID>     # per target
```

| PMID | `reading_state.py` | `paper_packet.py packet` | verdict before fetching |
|---|---|---|---|
| 18676360 | **absent** — no row | `prior read: depth=none · receipts=0` · `manifest: none — this is a first reading` · `artefacts: 0 present` · `acquisition: no route recorded — nothing has been tried and logged` | genuinely unread |
| 36247526 | **absent** — no row | identical to above | genuinely unread |
| 19918364 | **absent** — no row | identical to above | genuinely unread |
| 40235507 | **absent** — no row | identical to above | genuinely unread |
| 41776383 | **absent** — no row | identical to above | genuinely unread |
| 36828035 (lead) | `partial_fulltext_read`, 2 receipts; owes `references=not_read`, `supplementary=unavailable`, `tables=not_read` | `manifest: disease-models/wwox/research/deepdive_manifests/PMID36828035.json` · `artefacts: 0 present, 10 declared-and-absent` · `acquisition: 10 route(s) already recorded` | partially read; artefacts absent from this checkout |

### 🔴 Already-read count: **0 of 5**

**The trap did not fire this time.** All five unread premises are *really* unread — no receipt, no
manifest, no artefact, no logged acquisition route. The prose was accurate here. That is itself the
finding the dispatch asked for: the checkpoint's "unread" labels on these five are correct, and no
re-fetch was wasted. (Contrast: `PMID 36828035` was correctly marked `partial_fulltext_read`, and the
state check also surfaced that **all 10 of its declared artefacts are absent from this checkout** —
the prior reading's bytes are not here, only its receipts.)

---

## § 1 · Per-paper acquisition result

### 🔴 Deployment-level constraint discovered first

Direct network egress to every scholarly host is **denied by organization policy** in this
deployment. Established by probe, not assumed:

```
curl https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9561749/fullTextXML
  → curl: (56) CONNECT tunnel failed, response 403
  → [agent-proxy] www.ebi.ac.uk:443 — connect_rejected (the egress proxy denied the CONNECT
    (organization policy) or could not reach the destination)
```

`curl -sS "$HTTPS_PROXY/__agentproxy/status"` shows prior `connect_rejected` entries at 22:15 for
`www.ncbi.nlm.nih.gov:443`, `www.ebi.ac.uk:443`, `www.europepmc.org:443`, `api.crossref.org:443`,
`api.openalex.org:443` — i.e. an earlier actor hit the same wall tonight. `WebFetch` is blocked too,
on a separate code path:

```
WebFetch https://www.ebi.ac.uk/…/fullTextXML   → EGRESS_BLOCKED  (www.ebi.ac.uk)
WebFetch https://pmc.ncbi.nlm.nih.gov/articles/PMC9561749/  → EGRESS_BLOCKED (pmc.ncbi.nlm.nih.gov)
WebFetch https://doi.org/10.2164/jandrol.108.005066         → EGRESS_BLOCKED (doi.org)
WebFetch https://journals.plos.org/plosone/…0007820         → EGRESS_BLOCKED (journals.plos.org)
```

**Consequence:** the `find-fulltext` cascade (Unpaywall → Europe PMC → OpenAlex → Semantic Scholar →
CORE/BASE → publisher landing → Google Scholar) is **inoperable in this deployment** — every tier of
it is an HTTP fetch to a blocked host. Only two literature routes survive:

1. `mcp__PubMed__get_full_text_article` (PMC deposits only)
2. `mcp__Scholar_Gateway__semanticSearch` (publisher-side passage retrieval, Wiley corpus)

This is a harness finding, not a paper finding, and it is the reason the route table below is short.

### Route table

| PMID | PMCID (`convert_article_ids`) | Route attempted | Outcome | Body obtained | Read depth achieved |
|---|---|---|---|---|---|
| **18676360** | **none** — `{"pmid":"18676360","requested-id":"18676360"}`, no `pmcid`, no `doi` field returned | ① PMC — impossible, no PMCID ② `doi.org` → `EGRESS_BLOCKED` ③ **Scholar Gateway** → **WORKED** | **Abstract + Introduction + complete Materials and Methods + Results (incl. Figure 1–8 legends) + most of Discussion**, across 2 queries | ~14 000 words of body | `partial_fulltext_read` — Methods **complete**; references absent; Discussion partial |
| **36247526** | `PMC9561749` | PMC → **WORKED** (body served) | full body served, **but damaged** (§ 2) | ~9 000 words | `partial_fulltext_read` — narrative complete, **supplementary unreachable** |
| **19918364** | `PMC2771921` | PMC → **WORKED** | 48 831 chars | complete narrative + Methods + figure legends + Supporting-Information captions | `complete_fulltext_read` of the served surface; references absent |
| **40235507** | `PMC11998783` | PMC → **served, but `full_text: ""`** | **abstract only** | 0 chars of body | ❌ **NOT A READ** — abstract only |
| **41776383** | **none** | ① PMC — impossible ② Scholar Gateway (Wiley) → paper not in corpus; 0 passages returned for it | **nothing** | 0 | ❌ **NOT A READ** — abstract only |
| **36828035** | `PMC10835625` | PMC → **WORKED** | 60 088 chars | complete narrative incl. Methods §4.14 and Results §2.8 **and §2.9** | `complete_fulltext_read` of the served surface; references absent, supplementary unreachable |

### 🔴 Surface trustworthiness — `extraction_damage_report.py`

```
$ python3 framework/scripts/extraction_damage_report.py /tmp/s5/pmid19918364.txt /tmp/s5/pmid36828035.txt

/tmp/s5/pmid19918364.txt  (49040 bytes)
  fused-token scars ........... 12   e.g. forHybridization, formRNA, humangene, inmRNA, mousegene
  empty cross-ref stubs ....... 42
  orphaned statistics ......... 17
  reference list .............. ABSENT
  VERDICT: ITALIC-CLASS COUNTS INADMISSIBLE … ROMAN-CLASS COUNTS ADMISSIBLE …
           AND THE REFERENCE LIST IS ABSENT

/tmp/s5/pmid36828035.txt  (60268 bytes)
  fused-token scars ........... 21   e.g. ain, andmice, forand, formice, fromand, frommice
  empty cross-ref stubs ....... 101
  orphaned statistics ......... 42
  reference list .............. ABSENT
  VERDICT: (identical)
```

**This verdict governs § 2 and § 3.** *Gene symbols are italic-class on these surfaces and are
deleted.* Therefore **a zero for `Wwox` on any PMC-served surface in this wave measures the
extractor, not the paper**, and is not offered as evidence of absence anywhere below.

---

## § 2 · What each paper actually says, on the question it was cited for

### 2.1 `PMID 18676360` — Takenaka et al. 2008, *J Androl* 29(6):669–678

Source: Scholar Gateway, publisher-side text, `https://onlinelibrary.wiley.com/ai/10.2164/jandrol.108.005066`.
Full answer in § 4. Summary: this is a **testicular** paper. The brain appears only as *cited prior
work*.

> *(Introduction)* "In a previous histological study, we found many extracellular vacuoles in the CA1
> region of the hippocampus and the amygdaloid body of the *lde*/*lde* brain at 28 days of age. These
> pathological lesions may be associated with epileptogenesis in *lde*/*lde* rats. … (Suzuki et al,
> 2007)"

> *(Introduction)* "In linkage analysis, we have located the *lde* locus on rat chromosome 19 (Suzuki
> et al, in preparation)."

🔴 **The hippocampal/amygdaloid vacuole finding is NOT this paper's data.** It is attributed to
*Suzuki et al, 2007*. Any claim resting on `18676360` for `lde/lde` brain pathology is resting on a
citation of a citation; the primary is **Suzuki et al. 2007**, which is a separate acquisition target
and is not in this wave.

Note also the retrieval hazard is confirmed in the strongest form: the paper's own text says the
locus was mapped only by linkage to **chromosome 19**, *"in preparation"* — there is no gene name in
this paper at all, and therefore **no `Wwox` token and no `lde`→`Wwox` mapping anywhere in it.** A
`Wwox`-keyed query cannot reach it, and this is not an extractor artifact — the mapping did not yet
exist in 2008.

### 2.2 `PMID 36247526` — Machado et al. 2022, *IBRO Neurosci Rep* 13:322–329

Cited by **Scientist 1** as LCM RNA-seq of rat CA1/CA2/CA3/DG, for a subfield-resolved `Wwox` value.

**Scientist 1's report of silent stripping is CONFIRMED, verbatim, on the served surface.** Two
quotes from the PMC body, exactly as served:

> *(Discussion)* "In an example of potential marker genes, we have identified the gene(peroxisomal
> biogenesis factor 5-like) for CA1, which is crucial to the establishment of a dendritic gradient of
> HCN1 channels…"

> *(Methods §2.2)* "The datasets generated here were deposited in the National Center for
> Biotechnology Information (NCBI) Gene Expression Omnibus (GEO), accession number."

The gene symbol (`Pex5l`) is gone from the first; the **GEO accession is gone from the second** — the
sentence ends on the words "accession number." with nothing after it. The same deletion recurs
throughout: *"we also found(regulatory factor X3) with higher expression in DG, which could directly
regulate(fibroblast growth factor 1)"*.

**What the paper's design means for the `Wwox` question.** Per Methods §2.1 and §2.3, this study
reports **pairwise DEG comparisons between subfields**, not per-subfield expression values:

> "We ran six pairwise comparisons in DESEQ2 (low counts filter > 10), comparing all subfields between
> themselves, and obtained the following DEGs results (adjusted p < 0,05) 2863 (CA1vsCA2), 4318
> (CA1vsCA3), 1847 (CA2vsCA3), 5361 (CA1vsDG), 4815 (CA2vsDG) and 7120(CA3vsDG). For a complete list
> of all DEGs refer to."

The complete DEG lists — the only place a `Wwox` value could live — are in supplementary tables
("refer to" + stripped pointer), and the GEO accession that would reach the counts is deleted.

🔴 **No `Wwox` value was recovered, and none is claimable as absent.** Per the damage verdict above,
`Wwox` is an italic-class token on this surface; its non-appearance is uninformative. Scholar Gateway
does not carry this paper (Elsevier title; a targeted query returned Datson 2004, Aoyama 2022, Piras
2017, Vincent 2002 — never `10.1016/j.ibneur.2022.09.009`). **`P7` is not scored by this wave.**

Sample frame, for the record: *"three month old male Wistar rats (n = 4)"*, 120 coronal sections,
Bregma −1.72 to −6.72 mm, Rnor6.

### 2.3 `PMID 19918364` — Li et al. 2009, *PLoS ONE* 4(11):e7820

Cited by **Scientist 2**, which used it to **weaken its own hypothesis**. Scientist 2's
characterisation: *sciatic-transection injury model in wild-type rats concerning small (nociceptive)
DRG neurons, whereas proprioceptive afferents are large.* Point by point, from the text:

**Model and strain** — SUPPORTED, verbatim (Methods, "Animals"):

> "Adult male Sprague-Dawley rats (250–300 g) were used. … the sciatic nerve was transected
> unilaterally at the mid thigh level. Approximately 2 mm of the distal stump was removed. … In sham
> controls the nerve was exposed but without transection."

These are ordinary Sprague-Dawley rats carrying no *Wwox* lesion. **Wild-type: SUPPORTED.**
One nuance Scientist 2 did not mention: the paper also runs a **mouse** sub-experiment —

> *(Methods, "p53 Knockout Mice")* "p53 wild-type C57BL/six (p53) and knockout p53N4-M (p53 and p53)
> mice were used. These mice were undergone sciatic nerve transection…"

**"Small" neurons** — SUPPORTED, and the paper gives an explicit size criterion (Results):

> "post sciatic nerve transection for 2 months, p-WOX1 was mainly accumulated in the nuclei of small
> neurons (<20 µm in diameter), rather than in medium (20–30 µm)-to-large (>30 µm) sensory neurons in
> both contralateral and ipsilateral sides"

> *(Figure 4 legend)* "dramatic co-activation of WOX1 (>65% of cells), CREB (>65%) and NF-κB (40–65%)
> occurred in small neurons at month 2 post-injury. Approximately 150 cells were counted from 4 tissue
> sections at 200× magnification."

**"Nociceptive"** — 🔴 **NOT IN THE PAPER.** Term census over the served body:

| term | hits |
|---|---|
| `nocicept*` | **0** |
| `proprio*` | **0** |
| `myelin` | **0** |
| `neurofilament`, `IB4`, `substance P`, `CGRP`, `TrkA` | **0** each |

These are **roman-class** words — ordinary method and modality vocabulary, not italicised gene
symbols — so by the damage verdict these zeros **are admissible**. The paper classifies DRG neurons
**by soma diameter only**. It never assigns a sensory modality, never stains a nociceptive or
proprioceptive marker, and never mentions myelin.

**A counter-detail Scientist 2 did not have.** The small-neuron story is not the whole story:

> "The average sizes of p-WOX1-expressing neurons were significantly larger in the operated sides than
> in the non-operated sides (ipsilateral neurons: 28.8±1.8 µm in diameter; contralateral neurons:
> 20.4±1.7 µm; <0.05)."

28.8 µm sits in the paper's own **medium** band (20–30 µm), not the small band. And by immuno-EM:

> "the protein levels (or the numbers of high-density particles) were higher in the medium-to-large
> neurons than in the small neurons"

So on the injured side, WOX1-positive neurons are on average *medium*-sized, and early WOX1 protein is
*higher* in medium-to-large neurons. The "small neuron" conclusion is specific to the **2-month**
timepoint and to the population undergoing delayed apoptosis.

**Also collected:** L4 and L5 DRG **and spinal cord** — *"The L4 and L5 DRG and spinal cord were
harvested and fixed overnight at 4°C. Serial tissue sections were 5 µm in thickness."*

### 2.4 `PMID 40235507` — Cheng et al. 2025, *Research Square* (preprint)

**Not read.** `PMC11998783` exists, but `get_full_text_article` returned `"full_text": ""` — the
Research Square deposit carries metadata and abstract only, no body. All other routes blocked.

From the **abstract alone** (declared as such, not as a read): single-nucleus multiome
(snRNA-seq + snATAC-seq) of 103 861 nuclei from **human cerebellum and frontal cortex** of AD/ADRD
patients and controls; 431 834 peak-to-gene linkages; `RORA` in Purkinje cells, `ELF1` in granule
cells; causal genes `SEZ6L2` (Purkinje) and `KANSL1` (granule); CRISPRi on `rs4788201` and
`rs62056801` in iPSC-derived neurons. **It is a preprint** (`article_types: ["Journal Article",
"Preprint"]`, `Res Sq`, `10.21203/rs.3.rs-6264481/v1`) — not peer-reviewed at this version.

I cannot say what Scientist 3 cited it **for**, because I could not open it and the citing text is not
mine to assume. § 3 records this honestly as NOT ASSESSABLE.

### 2.5 `PMID 41776383` — Corona et al. 2026, *Mult Scler* 32(7):747–758

**Not read.** No PMCID; SAGE title; Scholar Gateway (Wiley corpus) does not index it; all HTTP routes
blocked. From the **abstract alone** (declared as such): pharmacogenomic study of interferon-beta and
glatiramer acetate response in European-ancestry relapsing-remitting MS; 679 GA and 1614 IFN-β
patients; >6 million variants tested. The WWOX mention is one clause:

> "the top GA variant was rs2053696A in MAP3 K1 ( = 3.97*10), involved in key signaling pathways.
> **Another significant GA signal was in WWOX.**"

No rs number, no effect size and no p-value for the WWOX signal are given in the abstract — the
abstract's own p-value string is itself mangled (`= 3.97*10`, exponent lost). **Everything needed to
use this citation quantitatively is behind the paywall.**

### 2.6 `PMID 36828035` — Hussain/Aldaz et al. 2023, *Prog Neurobiol* 226:102425 (open lead)

**Both passages the dispatch asked for, quoted exactly.**

**Methods §4.14 — "RNA-Seq and data analysis":**

> "RNA was isolated from HPC, PFC, (parietal) CTX, and CB from and mice, 150–280 days of age, n = 5
> mice/group (2 males and 3 females). Mice were euthanized, brains were extracted, and different
> tissue regions were collected on a cold plate and flash frozen in liquid N."

(The stripped tokens after "from" and before "mice" are the italicised genotype labels — italic-class,
deleted by the extractor, per the damage verdict.)

**Results §2.8 — heading and opening sentence:**

> "**2.8. Transcriptome profiling provides further evidence of neuroinflammation and glial cell
> dysfunction in forebrains of Wwox P47T mice**
>
> To gain insight into transcriptional changes associated with P47T mutation phenotypes, we **first**
> performed bulk RNA sequencing (RNA-seq) on **forebrain tissue regions, prefrontal cortex (PFC),
> parietal cortex (CTX), and hippocampus (HPC)** from (n = 5) and (n = 5) mice."

### 🔴 2.6.1 The cerebellar result EXISTS — Results **§2.9**

The premise behind this lead is wrong. §2.8 is forebrain-only **by design** — its own title says
"forebrains", and its first sentence says "**first**". The cerebellum has its own section immediately
after:

> "**2.9. Transcriptome profiling of Wwox P47T cerebella provides further evidence of dysfunction**
>
> Since mice displayed motor abnormalities along with evidence of significant cerebellar atrophy and
> PC degeneration, we sought to evaluate the transcriptional changes associated with WW domain LoF in
> CB. Like the forebrain tissues, gene expression was comparable between wildtype and P47T homozygous
> CB samples () and in agreement with earlier described results (and). Unsupervised hierarchical
> clustering of CB RNA-Seq profiles segregated samples from P47T homozygous and wildtype mice ().
> **EdgeR analysis identified a total of 1059 DEGs (376 genes upregulated, 683 genes downregulated)
> comparing both groups at an FDR < 0.01** (). Annotation of CB transcriptional differences using IPA
> showed striking enrichment of diseases and biofunctions related to severe cerebellar dysfunction.
> Congenital neurological disorder and encephalopathy, motor dysfunction and movement disorder, and
> hypoplasia of the brain, were among the top enriched diseases and functions with a positive Z score
> in the range of 2.1 – 6.8 and highly significant p-values (−log10 p-values range of 3.6 – 10.9) ().
> … Interestingly, GSEA hallmark gene set analysis showed that the topmost enriched gene sets in CB
> belonged to **lipid metabolism and reactive oxygen species pathway** (). … We analyzed the expression
> of pro-inflammatory cytokines and by qRT-PCR in CB tissue and observed a significant ≥ 2-fold
> upregulation of mRNA of both cytokines (p-value < 0.05) in CB samples from mice (n = 6) compared to
> mice (n = 6)."

**So: yes, a cerebellar result appears in the paper — a full RNA-seq section with 1059 DEGs, IPA
annotation, GSEA, and a separate n=6/group cytokine qRT-PCR.** The Methods §4.14 / Results §2.8
"mismatch" is not a missing-data finding; §2.8 and §2.9 partition the same §4.14 sampling frame.

One genuinely notable methodological point *does* survive, and it is different from the one alleged:

> *(§2.8)* "Interestingly, GSEA of CTX, despite representing the transcriptome profile of a different
> brain region, was particularly informative relating to the **suppression of cerebellar biofunctions**
> not only associated with CB development but also with PC differentiation, morphogenesis, and PC
> layer development (). This is in strong agreement with our observations from CB imaging and
> phenotype of mice."

i.e. cerebellar *biofunction* enrichment was read out of **parietal cortex** tissue. That is an
inference across regions, and should be labelled as such wherever it is used.

---

## § 3 · Is each citing Scientist's use SUPPORTED?

| # | PMID | Citing actor | The use, as reported to me | Verdict |
|---|---|---|---|---|
| 1 | 19918364 | Scientist 2 | "sciatic-transection injury model in **wild-type** rats" | ✅ **SUPPORTED** — Sprague-Dawley, verbatim Methods |
| 2 | 19918364 | Scientist 2 | "concerning **small** DRG neurons" | ✅ **SUPPORTED** — explicit `<20 µm` criterion, at the 2-month timepoint |
| 3 | 19918364 | Scientist 2 | "small (**nociceptive**)"; "proprioceptive afferents are large" | ⚠️ **PARTIALLY SUPPORTED** — the size claim is the paper's; the **modality labels are not**. `nocicept*` and `proprio*` each occur **0** times (admissible roman-class zeros). Scientist 2 imported a standard DRG size→modality convention from outside this source. The inference is conventional and defensible, but it is **Scientist 2's, not Li et al.'s**, and must be attributed that way |
| 4 | 19918364 | Scientist 2 | overall: the paper weakens Scientist 2's own hypothesis | ✅ **SUPPORTED, and correctly self-critical** — and the paper is in fact *harder* on the hypothesis than Scientist 2 realised: injured-side WOX1-positive neurons average **28.8 µm** (medium band), and early WOX1 protein is **higher in medium-to-large** neurons by immuno-EM |
| 5 | 36247526 | Scientist 1 | LCM RNA-seq of rat CA1/CA2/CA3/DG | ✅ **SUPPORTED** — exactly what the paper is (Wistar, n=4, PALM LCM, HiSeq 2500) |
| 6 | 36247526 | Scientist 1 | "gene symbols and GEO accession are silently stripped from the served text; got zero values" | ✅ **SUPPORTED — independently reproduced, verbatim.** Confirmed a second way by `extraction_damage_report.py`: *ITALIC-CLASS COUNTS INADMISSIBLE*. Scientist 1 was right to refuse to report a zero |
| 7 | 40235507 | Scientist 3 | unknown to me | ⚪ **NOT ASSESSABLE** — PMC serves `full_text: ""`; I never opened the body. I will not grade a use I could not check. Flagging one thing the citing actor should verify: this is a **Research Square preprint**, not peer-reviewed |
| 8 | 41776383 | Scientist 2 | unknown to me | ⚪ **NOT ASSESSABLE** — paywalled, never opened. The abstract does confirm a WWOX signal exists for glatiramer acetate, with **no rs number, effect size or p-value disclosed** |
| 9 | 36828035 | Scientist 3 | "Methods §4.14 collected …and cerebellum (n=5/group), while Results §2.8 reports **only forebrain**" | 🔴 **PARTIALLY SUPPORTED, and the conclusion drawn from it is UNSUPPORTED.** Both halves of the observation are literally true. But the implied gap is not real: **Results §2.9 is a dedicated cerebellar transcriptome section** — 1059 DEGs (376 up, 683 down, FDR < 0.01), IPA, GSEA, plus n=6/group cytokine qRT-PCR. §2.8 is titled "…in **forebrains**…" and says "we **first** performed". Nothing is missing |

> 🔴 **Row 9 is addressed to the Scientist working the cerebellum lead in parallel**
> (`disease-models/wwox/analysis/cerebellar_measurement_census_20260922.md` is untracked in this
> worktree). A census keyed on §2.8 will report a cerebellar measurement as absent from
> `PMID 36828035`. **It is present, in §2.9.** The §2.9 text is quoted in full at § 2.6.1.

---

## § 4 · `PMID 18676360` — the sampling-frame answer, verbatim

**The Materials and Methods were obtained complete.** Source: Scholar Gateway publisher-side text of
Takenaka M, Yagi M, Amakasu K, Suzuki K, Suzuki H, *J Androl* 2008;29(6):669–678,
DOI `10.2164/jandrol.108.005066`.

### What was collected, verbatim

> "## Materials and Methods
>
> All rats were derived from the LDE inbred strain maintained in our laboratory. The *lde*/*lde* rats
> were identified by their dwarf phenotype at 21 days of age (Suzuki et al, 2007). Because most
> *lde*/*lde* rats died before maturation, the animals used in this study were mutant (*lde*/*lde*) and
> phenotypically normal (+/+ or +/*lde*) littermates at 21, 28, 35, and 56 days of age. …
>
> Blood samples were collected from the vena cava with a heparinized plastic syringe around 1700 hours
> under light ether anesthesia. Plasma samples were obtained and stored at 80C until assayed. **After
> collection of blood samples, rats were sacrificed by an overdose of ether, and autopsied to
> determine the weights of the male reproductive organs using an electric balance.** Because of the
> high lethality of immature *lde*/*lde* rats (Suzuki et al, 2007), **3 to 9 mutant rats at each day
> were used.** …
>
> **After weighing, all testes were fixed in Bouin solution overnight, embedded in paraffin (paraffin
> pellets; Wako, Osaka, Japan), and cut into serial sections at a thickness of 3 [µ]m** as described
> previously (Suzuki et al, 2004). The sections were deparaffinized in xylene, hydrated in a graded
> alcohol series, and immersed in water or 0.01 M phosphate-buffered saline… They were then stained
> with hematoxylin-eosin, the TUNEL method was used to identify apoptotic cells, and immunostaining
> was performed for 3[β]-hydroxysteroid dehydrogenase (3[β]HSD), 11[β]-hydroxysteroid dehydrogenase
> (11[β]HSD), and vimentin."

And the only other tissue sectioned, from the second Methods passage:

> "**Three normal and 3 mutant pituitary glands at 28 days of age** were fixed in Bouin solution for 1
> hour, and paraffin sections were cut as described for the preparation of testicular sections. …
> the polyclonal antibodies to rat FSH and LH (1/12 800, room temperature, overnight; Biogenesis Ltd,
> Poole, United Kingdom) were applied to the sections as the first antibodies."

> "Plasma concentrations of luteinizing hormone (LH), follicle-stimulating hormone (FSH), and
> testosterone were measured using the Rat Follicle Stimulating Hormone Biotrak Enzyme Immunoassay
> (EIA) System (Amersham Biosciences…), Rat Luteinising Hormone (rLH) Enzyme Immunoassay Biotrac (EIA)
> System (Amersham Biosciences), and Rodent Testosterone ELISA Test Kit (Endocrine Technologies…)"

### 🔴 The answer to the three questions two other Scientists hit a wall on

| Question | Answer from the Methods |
|---|---|
| **Cerebellum collected, sectioned or assayed?** | **NO.** Not mentioned anywhere in the paper. |
| **Brainstem?** | **NO.** Not mentioned. |
| **Spinal cord?** | **NO.** Not mentioned. |
| **Peripheral nerve?** | **NO.** Not mentioned. |
| **Muscle?** | **NO.** Not mentioned. |
| **Gait, ataxia or coordination measurement?** | **NONE.** No behavioural apparatus, no rotarod, no footprint, no beam, no clasping. The only behavioural description in the whole paper is seizure semiology, and it is *cited*, not measured here: "Seizures are first detected in this model between 16 and 63 days of age, and mostly begin as wild running and progress to generalized tonic-clonic convulsions." |
| **Myelin readout?** | **NONE.** No myelin stain, no MBP, no g-ratio, no electron microscopy of nerve. |
| **Ages** | **21, 28, 35 and 56 days** — all four timepoints, throughout. |
| **Cohort sizes** | **"3 to 9 mutant rats at each day were used"** (organ weights / testis histology). Pituitary immunostaining: **3 normal and 3 mutant, at 28 days only.** Cell counts: "At least 10 round sections of seminiferous tubules of each testis"; TUNEL: "a square field (0.3 mm^2^) … At least 10 areas were selected at random from histological sections of each testis". |

**The complete sampling frame is: blood (vena cava) → male reproductive organ weights at autopsy →
testes fixed and sectioned → pituitary glands (n=3+3, day 28 only) fixed and sectioned.** Pituitary
absolute weights also appear in Figure 1. **Nothing caudal to the pituitary — no hindbrain, no cord,
no nerve, no muscle — was taken.**

### 🔴 Transfer warning

**The `lde/lde` rat is not a human WWOX-DEE allele, and nothing here transfers.** It is a spontaneous
rat mutant whose locus, *in this paper*, is mapped only to **rat chromosome 19 by linkage**, with the
gene "in preparation" and unnamed. This wave establishes what Takenaka 2008 *measured*; it establishes
nothing about WWOX-DEE, and it must not be used to populate any cerebellar, myelin or motor premise
for the reference genotype. Its value to LEGEND is **negative evidence about a corpus**: the founding
laboratory's own `lde/lde` primary never looked at the hindbrain.

---

## § 5 · What remains unreachable — `HUMAN_REQUIRED`

| PMID | Identity | Exact failure | Status |
|---|---|---|---|
| **41776383** | Corona et al. 2026, *Mult Scler* 32(7):747–758, DOI `10.1177/13524585261417130` | `convert_article_ids` → `{"pmid":"41776383","requested-id":"41776383"}`, **no `pmcid`**. Scholar Gateway (Wiley) does not index the SAGE title — a targeted WWOX/glatiramer query returned only `10.1111/ene.70227`, `10.1111/jpc.70401`, `10.1002/mgg3.2500`, `10.1002/jnr.70148`. All HTTP routes → `EGRESS_BLOCKED` by organization policy | 🔴 **HUMAN_REQUIRED** — institutional SAGE access needed. Needed from it: the WWOX rs number, effect size and p-value for the GA arm |
| **40235507** | Cheng et al. 2025, *Research Square*, DOI `10.21203/rs.3.rs-6264481/v1`, PMCID `PMC11998783` | PMC deposit exists but `get_full_text_article` returns **`"full_text": ""`** — metadata + abstract only, no body served. All HTTP routes → `EGRESS_BLOCKED` | 🔴 **HUMAN_REQUIRED** — fetch the preprint PDF from researchsquare.com off-harness |
| **36247526** — supplementary only | Machado et al. 2022, PMCID `PMC9561749` | Narrative body obtained. **Supplementary DEG tables not served**, and the **GEO accession is deleted from the served text** ("…Gene Expression Omnibus (GEO), accession number." — sentence ends). Europe PMC / PMC / OpenAlex / Crossref all `EGRESS_BLOCKED`, so the accession cannot be recovered by another index | 🔴 **HUMAN_REQUIRED** — recover the GEO accession from the publisher page, then pull the per-subfield `Wwox` counts. **This is the specific unblock for `P7`** |
| **36828035** — artefacts | Hussain/Aldaz 2023, PMCID `PMC10835625` | Body obtained fresh this wave. Separately, `paper_packet.py` reports **10 declared artefacts absent from this checkout** (`PMID36828035_Hussain2023_PMC.xml` + 9 `nihms-1957654-f000*.jpg`), with `no recipe — no_note` / `figure_note_names_no_route` | ⚠️ Not blocking — the § 2.6.1 answer was obtained without them. Noted for `evidence_presence.py` |
| **18676360** — residue | Takenaka 2008 | Abstract, Introduction, complete Methods, Results and most of Discussion obtained. **Reference list not served**; a minority of Discussion paragraphs not surfaced by the two queries | ⚠️ Not blocking — the sampling-frame question is fully answered from the complete Methods |
| — | **Suzuki et al. 2007** (the `lde/lde` primary that Takenaka 2008 cites for the hippocampal/amygdaloid vacuoles, and for the growth-retardation-from-day-3 and GH-cell findings) | Not attempted — outside this wave's target list | ⚠️ **NEW ACQUISITION TARGET.** This, not `18676360`, is the primary for `lde/lde` brain pathology |

---

## § 6 · 🔴 PROPOSED receipt payloads — **NOT written to the ledger**

For the Orchestrator to accept, amend or reject. **No receipt was recorded. `fulltext_receipts.py
record` was not run. The ledger and its hash chain are untouched.**

### Proposal A — `PMID 18676360`

| field | proposed value |
|---|---|
| `pmid` | `18676360` |
| `doi` | `10.2164/jandrol.108.005066` |
| `depth` | `partial_fulltext_read` |
| `route` | `scholar_gateway_semantic_search` (publisher-side, Wiley), 2 queries |
| `surface` | `https://onlinelibrary.wiley.com/ai/10.2164/jandrol.108.005066` — passage retrieval, not a whole-body fetch |
| `abstract` | `read` |
| `introduction` | `read` |
| `methods` | **`read` — complete, both Methods passages recovered** |
| `results` | `read` (incl. Figure 1–8 legends) |
| `figures` | `captions_only` |
| `tables` | `not_present` |
| `discussion` | `partial` |
| `limitations` | `not_present` |
| `supplementary` | `not_present` |
| `references` | `unavailable` (not served by this surface) |
| `reader` | `scientist-5` |
| `prior_receipt` | none — first reading |
| `verbatim_locators` | the § 4 Methods block; the § 2.1 Introduction attribution to Suzuki et al 2007 |
| `caveat` | 🔴 no whole-body artifact persisted to `files/fulltext/`; retrieval was passage-wise. Re-derivable only through Scholar Gateway |

### Proposal B — `PMID 19918364`

| field | proposed value |
|---|---|
| `pmid` | `19918364` · `pmcid` `PMC2771921` · `doi` `10.1371/journal.pone.0007820` |
| `depth` | `complete_fulltext_read` *(of the served surface)* |
| `route` | `pubmed_mcp_get_full_text_article` → PMC |
| `body_length` | 48 831 chars |
| `abstract`/`introduction`/`methods`/`results`/`discussion` | `read` |
| `figures` | `captions_only` · `tables` `not_present` · `supplementary` `captions_only` (Figures S1–S9 legends served, images not) |
| `references` | `unavailable` — `extraction_damage_report.py`: *reference list ABSENT* |
| `surface_caveat` | 🔴 *ITALIC-CLASS COUNTS INADMISSIBLE* (12 fused-token scars, 42 empty cross-ref stubs, 17 orphaned statistics). The `nocicept*`/`proprio*`/`myelin` zeros in § 2.3 are **roman-class and therefore admissible**; state the class with every count |
| `verbatim_locators` | the `<20 µm / 20–30 µm / >30 µm` criterion; the `28.8±1.8 µm` ipsilateral mean; the Sprague-Dawley Methods sentence; the L4/L5 DRG + spinal cord harvest sentence |

### Proposal C — `PMID 36828035` (resumption of an existing partial read)

| field | proposed value |
|---|---|
| `pmid` | `36828035` · `pmcid` `PMC10835625` · `doi` `10.1016/j.pneurobio.2023.102425` |
| `depth` | `complete_fulltext_read` *(of the served surface)* — **resumes** the existing `partial_fulltext_read` |
| `prior_receipt` | the existing `PMID36828035` receipt(s) — 2 on record; Orchestrator to name the parent |
| `route` | `pubmed_mcp_get_full_text_article` → PMC · `body_length` 60 088 chars |
| sections | `abstract`/`introduction`/`methods`/`results`/`discussion` `read`; `figures` `captions_only`; `tables` `not_read`; `supplementary` `unavailable`; `references` `unavailable` |
| `settles` | the §4.14-vs-§2.8 lead — **Results §2.9 carries the cerebellar transcriptome** |
| `verbatim_locators` | Methods §4.14 block; Results §2.8 heading + first sentence; **Results §2.9 in full** (§ 2.6.1); the §2.8 "GSEA of CTX … cerebellar biofunctions" cross-region inference |
| `surface_caveat` | 🔴 *ITALIC-CLASS COUNTS INADMISSIBLE* (21 fused-token scars, 101 empty cross-ref stubs, 42 orphaned statistics; reference list ABSENT). Every genotype label in the quoted passages is a deleted italic |

### Proposal D — `PMID 36247526`

| field | proposed value |
|---|---|
| `pmid` | `36247526` · `pmcid` `PMC9561749` · `doi` `10.1016/j.ibneur.2022.09.009` |
| `depth` | `partial_fulltext_read` |
| `route` | `pubmed_mcp_get_full_text_article` → PMC |
| sections | `abstract`/`introduction`/`methods`/`results`/`discussion` `read`; `figures` `not_served`; `tables` `not_present` in body; **`supplementary` `unavailable`**; `references` `unavailable` |
| `settles` | **nothing about `Wwox`.** Confirms the study design and reproduces Scientist 1's stripping report verbatim |
| `surface_caveat` | 🔴 **A `Wwox` zero on this surface is inadmissible.** Gene symbols are deleted (`"the gene(peroxisomal biogenesis factor 5-like)"`) and the **GEO accession is deleted** (`"…(GEO), accession number."`). The subfield-resolved value lives only in the unserved supplement |
| `verbatim_locators` | the two stripping quotes; the six-pairwise-comparison DEG sentence; the Wistar n=4 / 120-section sampling frame |

### 🔴 No receipt proposed for

- **`PMID 40235507`** — `full_text: ""`. Abstract only. **Not a read.**
- **`PMID 41776383`** — paywalled, never opened. Abstract only. **Not a read.**

Both should stay on the unread-premise ledger. If the Orchestrator's aim is to clear
`unread_premises: 5/0`, this wave clears **3 of 5** (`18676360`, `36247526`, `19918364`); two remain
and are `HUMAN_REQUIRED`.

---

## § 7 · What I could not verify

1. **Whether `Wwox` is differentially expressed across rat hippocampal subfields.** Not recovered, and
   **not claimable as absent** — the token class is deleted on the only surface I could reach. `P7`
   remains supported on its qualitative half only.
2. **What Scientist 3 cited `40235507` for, and Scientist 2 `41776383` for.** I could open neither, so
   I graded neither. Rows 7 and 8 of § 3 are ⚪, not ❌ — an unopened paper is not a refuted one.
3. **Whether Takenaka 2008's Discussion contains any further tissue mention** beyond the paragraphs
   surfaced. Two queries returned Introduction, Abstract, complete Methods, Results and the
   Leydig/pituitary Discussion paragraphs; I cannot certify I saw every Discussion paragraph. **The
   Methods, which is where a sampling frame is binding, is complete** — so § 4 stands.
4. **Whether `36828035` has cerebellar *supplementary* material** beyond §2.9's in-text figures. The
   supplement was not served; §2.9's parenthetical figure pointers are all stripped.
5. **Whether the `lde` locus was ever published as `Wwox`.** Takenaka 2008 says only "rat chromosome
   19 … in preparation". I did not chase the later mapping paper; that is a separate acquisition.
6. **The 10 absent `36828035` artefacts.** I did not re-acquire them; I read a fresh PMC surface
   instead. Whether the prior receipts' locators still resolve against *that* surface is a
   `locator_audit.py` question I did not run — it would have required touching artefacts I am
   read-only toward.

---

## § 8 · Source attribution

According to PubMed, and by passage retrieval through Scholar Gateway:

| PMID | Citation | DOI |
|---|---|---|
| 18676360 | Takenaka M, Yagi M, Amakasu K, Suzuki K, Suzuki H. *Retarded differentiation of Leydig cells and increased apoptosis of germ cells in the initial round of spermatogenesis of rats with lethal dwarf and epilepsy (lde/lde) phenotypes.* J Androl. 2008;29(6):669–678 | [10.2164/jandrol.108.005066](https://doi.org/10.2164/jandrol.108.005066) |
| 36247526 | Machado JPD, Athie MCP, Matos AHB, Lopes-Cendes I, Vieira AS. *The transcriptome of rat hippocampal subfields.* IBRO Neurosci Rep. 2022;13:322–329 | [10.1016/j.ibneur.2022.09.009](https://doi.org/10.1016/j.ibneur.2022.09.009) |
| 19918364 | Li MY, Lai FJ, Hsu LJ, Lo CP, Cheng CL, Lin SR, Lee MH, Chang JY, Subhan D, Tsai MS, Sze CI, Pugazhenthi S, Chang NS, Chen ST. *Dramatic co-activation of WWOX/WOX1 with CREB and NF-κB in delayed loss of small dorsal root ganglion neurons upon sciatic nerve transection in rats.* PLoS One. 2009;4(11):e7820 | [10.1371/journal.pone.0007820](https://doi.org/10.1371/journal.pone.0007820) |
| 40235507 | Cheng F, Feng Y, Yang X, et al. *Genomic and epigenomic insights into purkinje and granule neurons in Alzheimer's disease and related dementia using single-nucleus multiome analysis.* Research Square (**preprint**). 2025 | [10.21203/rs.3.rs-6264481/v1](https://doi.org/10.21203/rs.3.rs-6264481/v1) |
| 41776383 | Corona A, Clarelli F, Pääkkönen K, et al. *Pharmacogenomics of response to interferon-beta and glatiramer acetate in Multiple Sclerosis: A multi-centric study.* Mult Scler. 2026;32(7):747–758 | [10.1177/13524585261417130](https://doi.org/10.1177/13524585261417130) |
| 36828035 | Hussain T, Aldaz CM, et al. *WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice phenocopying human SCAR12.* Prog Neurobiol. 2023;226:102425 | [10.1016/j.pneurobio.2023.102425](https://doi.org/10.1016/j.pneurobio.2023.102425) |

Full texts of `36247526`, `19918364`, `40235507` (abstract only) and `36828035` retrieved from PubMed
Central. Publisher-side passages for `18676360` retrieved by Scholar Gateway
(Wiley Online Library; AI-assisted retrieval — all quotations above were taken verbatim from the
returned passage text and none were paraphrased).

Scratch artifacts, **outside the repository**, not committed: `/tmp/s5/pmid19918364.txt`,
`/tmp/s5/pmid36828035.txt`, `/tmp/rs_s5.md`.

---

### Contact discipline

🔴 **No external action beyond fetching public literature was taken.** No author was emailed, no PDF
was requested from any person or laboratory, no form was filled, no repository was contacted. The two
paywalled items are marked `HUMAN_REQUIRED` and left for the operator.
