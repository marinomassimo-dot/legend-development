# Can the RNA output of WWOX `c.517-2A>G` be measured from data that is already public?

**Node:** `TX001_RNA_EVIDENCE_FROM_PUBLISHED_DATA` · **Actor:** Scientist A · **Date:** 2026-09-21
**Status:** non-canonical analysis file. No canonical file edited, no registry written, no receipt claimed, no commit.
**Read-only toward every canonical file. Nothing was downloaded and no raw data was processed. Not medical advice.**

---

## 1 · Read depth, declared before any finding

| Source | Identity | Depth reached | Body length returned | Figures |
|---|---|---|---|---|
| **PMID 34268881** / **PMC8350905** | Steinberg DJ … Aqeilan RI, *EMBO Mol Med* 2021 — WWOX-KO and patient-derived cerebral organoids · `PAPER` record held, read in full by LEGEND previously | 🟢 **full deposit re-read this session**, targeted at Methods + Data availability | **82,755 B** (measured) | ❌ |
| **PMID 30853297** | Weisz-Hubshman M … Heimer G, *Eur J Paediatr Neurol* 2019;23(3):418–426 — the source of the `c.517-2A>G` transcript measurement · `PAPER 025` | 🔴 **abstract only.** No PMCID (`convert`/`get_copyright_status` return no `pmc` field; LEGEND's own splice census independently recorded `pmc_id: null`). Elsevier, egress blocked | n/a | ❌ |
| **PMID 42397075** | Steinberg DJ *et al.*, *Brain* 2026, DOI 10.1093/brain/awag239 — the patient-line organoid scRNA-seq paper | 🔴 **no PMC deposit.** LEGEND's manifest records this per rule 5d: *"No PMC deposit: esummary returns only pubmed, doi and pii, and elink to pmc returns nothing."* The local artifacts it cites (`files/fulltext/PMID42397075_*`) **do not exist in this environment** — `files/fulltext/` is absent. **Read only through LEGEND's own manifest and dossier** | n/a — not reachable | ❌ |
| **PMID 38161429** / PMC10757851 | Battaglia L *et al.*, *Front Pediatr* 2023 | 🟢 read in full **in Wave 1 of this session**; re-used here for the splice-variant list | ≈16 KB (Wave 1) | ❌ |
| LEGEND local | `deepdive_manifests/PMID42397075.json` (30 locator entries), `fulltext_dossiers/PMID42397075_partial_locators.md` (368 lines), `wwox_splice_transcript_census_20260921.md`, `claim_registry_current`, `discovery_ledger_current`, `paper_registry_current` | 🟢 read directly | — | — |
| Scholar Gateway | one semantic pass for the *Brain* 2026 single-cell methods and accession | ⚪ **returned nothing from that paper.** The one 10x passage it returned belongs to an unrelated article and is **not** attributed here | — | — |

🔴 **No figure panel was inspected in this environment.** The iPSC-line genotype table is a **figure attestation
recorded by a prior session that had panel access** (`Supplementary Figure 1, panel E`, rendered at 170 ppi). It is
treated throughout as **LEGEND's record**, never as something I have seen.

⚠️ **Extractor state.** The PMC8350905 surface **deletes hyperlinked accession strings**: its Data-availability
block reads *"Gene Expression Omnibus:()"* — an empty parenthesis where the accession was. **That is a parser
deletion, not an absent accession**, and it is handled as such in §3.

---

## 2 · The direct answer

**No. Not from data that is already public — and the reason is not access, it is that the allele's RNA was never
sequenced.**

There are exactly two WWOX organoid transcriptomic datasets in the literature, and they fail in opposite ways.
**The 2021 dataset has the right instrument and the wrong cells:** its library chemistry is bulk, poly-A-selected,
stranded, 75 bp — which *can* carry an exon-junction read — but the sequenced samples are **wild-type (n=2) versus
engineered knockout (n=4)**, and the `c.517-2A>G` patient line (WSM) appears in that paper only in qPCR of Wnt
target genes, never in RNA-seq. **The engineered knockout is a different lesion and carries no splice allele at
all**, so the deposited dataset contains **zero molecules of `c.517-2A>G` transcript**. **The 2026 dataset has the
right cells and, on every reachable indication, the wrong instrument:** it does include the patient lines, but the
paper has no PMC deposit, **no accession could be established from any surface reachable here**, and 28,208
sequenced cells is a throughput that belongs to droplet-based tag chemistry, whose ~90 bp reads sit at one end of
the transcript — while `c.517` lies ≥726 coding nucleotides from the stop codon, plus the 3′UTR, i.e. nowhere near
either end. On top of that, the transcript a splice assay is trying to see is the one **NMD is predicted to
destroy**, so even a dataset that could reach the junction would be measuring a depleted pool. **A clean negative:
the public data cannot answer this, and the next session should not spend time on it.** What the session *did*
establish is worth more than the negative — see §8 and the two corrections in §7.

⚠️ **And the question is not "does this unlock an ASO."** `DL-MOL-011` already argues — as **parked prior art,
pending external verification, with `TX-001` NOT demoted** — that no SSO can rebuild a destroyed invariant AG, and
that correcting such an allele is a DNA-editing problem. §2A records that entry, marks which half of it transfers
from `c.1057-2A>G` to `c.517-2A>G` and which half does not, and restates the measurement's value as **three** uses:
variant reclassification (ACMG `PS3`), a baseline for **any** correction strategy including editing, and the
unmeasured question of whether the aberrant product is wholly non-productive or **leaky**.

---

## 2A · What the measurement would be FOR — prior art, and the allele boundary on it

🔵 **This is prior art. It is recorded here so it is neither rediscovered nor contradicted, and it is NOT
adjudicated by this file.**

`discovery_ledger_current.md` **`DL-MOL-011`** (`Tag: INFERENZA forte`, `Status: open`) argues that **a
splice-switching oligonucleotide cannot rebuild a destroyed canonical acceptor**: SSOs act by *masking* elements —
cryptic sites, exonic silencers and enhancers, pseudoexons — and **do not create splice sites**; a variant hitting
the invariant **AG** dinucleotide leaves the spliceosome nothing to recognise, so the best an ASO could do is mask
a nearby cryptic site and force a *different aberrant product, not the wild-type transcript*. It closes the two
obvious escapes: modified **U1 snRNA** corrects **donor** (5′) sites, not acceptors; **ADAR** editing runs A→I
(read as G), **the wrong direction** when G→A is required. Its positive proposal is DNA-level: at −2 an `A>G` on
the sense strand is a `T→C` on the antisense, so a **cytosine base editor** doing C→T on the antisense restores the
sense `A` and **rebuilds the AG**; prime editing permits any point substitution.

⚠️ **Status, stated exactly as the ledger states it.** `DL-MOL-011` is explicitly **parked pending external
verification** — *"da sottoporre a verifica esterna prima di retrocedere formalmente TX-001"*, to be confirmed or
refuted by `legend-aso-designer`. **`TX-001` has NOT been demoted**, and the therapeutic file still frames ASO
versus editing as a live choice. **Nothing in this file adjudicates that, and nothing in this file should be read
as having demoted it.**

### 🔴 The allele boundary — which half of `DL-MOL-011` transfers to `c.517-2A>G`, and which half does not

`DL-MOL-011` and `DL-MECH-045` were written about **`c.1057-2A>G`**. This node's allele is **`c.517-2A>G`**. Both
destroy the invariant AG at −2, but they are **not equivalent in consequence**, and the split runs exactly along
the line between DNA-level and transcript-level reasoning:

| Argument | Level | Transfers to `c.517-2A>G`? |
|---|---|---|
| An SSO cannot rebuild a destroyed invariant AG | **mRNA-element level** — a statement about what SSOs do, independent of where in the gene the acceptor sits | ✅ **Transfers.** Nothing about it depends on the exon |
| U1 snRNA corrects donors, not acceptors; ADAR runs the wrong direction | mechanism-class level | ✅ **Transfers** |
| A CBE doing C→T on the antisense restores the sense `A` and rebuilds the AG; prime editing permits it too | **DNA level** — the variant is `A>G` at −2 in **both** alleles, so the base chemistry is identical | ✅ **Transfers cleanly**, because it is an argument about a base substitution, not about a transcript position |
| *"The acceptor allele is not a silent null but probably a **truncated unstable protein**"* (`DL-MECH-045`) | **transcript-position level** — it depends entirely on **exon 9 being the LAST exon**, so a PTC there **escapes NMD** | ❌ **DOES NOT TRANSFER.** `c.517` opens exon **6 of 9**. §3.3 computes the frame for that exon independently: 89 nt, `89 mod 3 = 2`, frameshift from codon 173, PTC far upstream of the final exon 8/9 junction ⇒ **NMD predicted, not NMD-escape.** LEGEND's own registry states the contrast directly: *"qui l'NMD avviene perché la lesione è sull'esone 6; l'esone 9 è l'ultimo, e un PTC nell'ultimo esone sfugge all'NMD"* |
| *"Mask the cryptic +8 site"* as the one thing an ASO could still do | allele-specific | ⚪ **No counterpart established.** The `+8` cryptic gain (SpliceAI DS_AG 0.64) is a `c.1057-2A>G` prediction. **No splice prediction of any kind exists for `c.517-2A>G`** (§3.4) |

⇒ **The two worked-example splice alleles sit in opposite NMD regimes.** For `c.1057-2A>G` the expected product is
a stable aberrant transcript and a truncated protein; for `c.517-2A>G` it is a degraded transcript and no protein.
**An assay designed for one would be mis-specified for the other**, and every statement in this file is labelled
with the allele it concerns.

### The three uses of the measurement — not one

Following `DL-MOL-011`'s own closing point — *"l'assay dell'esone 9 resta prezioso — non più come 'endpoint per
l'ASO', ma (a) per riclassificare la VUS (ACMG PS3) e (b) come baseline per qualunque strategia di correzione,
editing incluso"* — the feasibility question in this file is **not** "does this unlock an ASO". It is whether public
data can serve **three** distinct purposes:

1. **Variant reclassification.** A measured transcript consequence is **ACMG `PS3`**-grade functional evidence. This use survives regardless of which therapeutic lever is eventually correct.
2. **A baseline for ANY correction strategy, editing included.** A correction endpoint needs a pre-correction denominator. Base editing and prime editing need it exactly as much as an ASO would.
3. 🔵 **Whether the aberrant product is wholly non-productive or LEAKY** — the residual fraction of normally spliced transcript. **This is the only route by which a partially functional outcome survives for a carrier, and it is unmeasured for every WWOX splice allele.** It is the quantity §9 is built to report, and the one most easily destroyed by the NMD confound.

---

## 3 · Task 1 — The allele's coordinates, PREDICTED separated from MEASURED at every step

### 3.1 · Which exon does `c.517` open? — **MEASURED (reported), and the exon number is in the primary source**

| Locator | Quotation | Source · section | Status |
|---|---|---|---|
| **T-1** ⭐ | *"Complementary DNA sequencing demonstrated that the WWOX c.517-2A > G splice-site variant causes skipping of exon six."* | PMID **30853297**, abstract | **MEASURED and reported** — `abstract` |
| **T-2** | *"Exome sequencing revealed that four of the patients were homozygous for a novel WWOX c.517-2A > G splice-site variant and two were compound heterozygous for this variant and a novel c.689A > C, p.Gln230Pro missense variant."* | PMID **30853297**, abstract | `abstract` |

⚠️ **Token check.** The source writes `c.517-2A > G` with spaces around the `>`, and writes the exon as the word
**"exon six"**, not "exon 6". Both are reproduced exactly above. The measurement method named is **complementary
DNA sequencing** — not a minigene, not prediction.
⚠️ **Depth.** This is an **abstract**, on a paper LEGEND's own splice census marks unreachable. Reading it verbatim
raises confidence in the *tokens*; it does **not** convert abstract-depth into a full-text read, and nothing about
quantification, tissue, NMD control or aberrant:normal ratio can be claimed from it.

⭐ **Incidental, and it connects this node to Waves 1–2:** PMID 30853297 is *also* a primary source for
**`c.689A>C, p.Gln230Pro`** — the exemplar allele of the SDR node — in compound heterozygosity with `c.517-2A>G`.
The two worked-example allele classes of this repository meet in one 2019 case series.

### 3.2 · Independent corroboration of the exon boundaries — **PREDICTED, by arithmetic I performed**

From the Battaglia 2023 body read in Wave 1 of this session, §2 *Genetic findings*, listing reported splice-site
variants: *"c.173-1G>T, c.173-2A>G, c.409+1G>T, c.517-2A>G, and c.606-1G>A"*.

Reading the HGVS positions as boundary markers:

| Marker | What it fixes | Inference |
|---|---|---|
| `c.409+1` — a **donor**, +1 after `c.409` | an exon **ends** at `c.409` | the next exon begins at `c.410` |
| `c.517-2` — an **acceptor**, −2 before `c.517` | an exon **begins** at `c.517` | the preceding exon ends at `c.516` |
| `c.606-1` — an **acceptor**, −1 before `c.606` | an exon **begins** at `c.606` | the exon opened at `c.517` ends at `c.605` |

⇒ the exon opened by `c.517` spans **c.517–c.605 = 605 − 517 + 1 = 89 nt**.

✅ **This independently reproduces the exon length LEGEND already holds (89 nt) by a route that does not use it.**
Two sources agreeing is corroboration; it is **not proof**. ⚠️ **Declared weakness:** the Battaglia list is a list
of *reported variants*, and it does not assert that these are **consecutive** boundaries. The arithmetic assumes
adjacency. The agreement with LEGEND's independently held 89 nt is what makes the assumption safe enough to use,
and it is flagged rather than hidden. 🔴 **I could not consult RefSeq `NM_016373.4` exon coordinates directly** —
this environment has no sequence-database tool and no NCBI egress. That is the check that would settle it outright,
and it was not available.

### 3.3 · Frame consequence — **PREDICTED, by my own arithmetic; no tool, no source**

WWOX ORF and protein, from PMID 30158849 (read in Wave 1): *"an open reading frame (ORF) of 1245 base pairs long,
encoding a 414-amino-acid (46 kDa) protein."* (414 × 3 = 1242 coding + 3 stop = 1245 ✓.)

| Step | Arithmetic | Result |
|---|---|---|
| Codon containing `c.517` | 3 × 172 = 516, so `c.517` is base **1** of codon **173** | the exon **opens in frame** (phase 0) |
| Exon length | 89 nt · **89 mod 3 = 2** | the exon **does not** end in frame (phase 2) |
| Codon at `c.605` | 3 × 201 = 603 → `c.604`, `c.605` are bases 1–2 of codon **202** | confirms phase 2 |
| Skipping | new junction joins `c.516` (end of codon 172) directly to `c.606` (base **3** of old codon 202) | **downstream sequence read out of register — FRAMESHIFT** |

⇒ **Complete skipping of this exon is predicted to be a frameshift, not an in-frame deletion.** Predicted
consequence: `p.(?)fs` beginning at codon 173. ⚠️ **I do not name the residue at position 173** — I have no WWOX
sequence in this environment, and naming it would be fabrication.

**NMD — PREDICTED, with its rule named and its counter-evidence attached.** WWOX has **9 exons**; the lesion is in
exon **6**. A PTC arising after codon 173 lies far upstream of the final exon 8/exon 9 junction, so by the
**50–55 nt rule** the transcript is **predicted to be an NMD substrate**. 🔵 **LEGEND already holds both halves of
this and holds them correctly**, in `paper_registry_current` (the 22 kb exon-6 deletion case): *"the deletion led
to **nonsense-mediated decay** of the NM_016373.3 transcript"*, together with the explicit contrast —
*"qui l'NMD avviene perché la lesione è sull'esone 6; l'esone 9 è l'ultimo, e un PTC nell'ultimo esone sfugge
all'NMD"*. **The two worked-example splice alleles of this repository sit in opposite NMD regimes.** See correction
C-2.

⚠️ **The counter-evidence, which must travel with the prediction.** Weisz-Hubshman *detected the skipped product by
cDNA sequencing* (T-1). A transcript that can be sequenced was not completely degraded. So NMD is **predicted but
demonstrably not absolute** — and **no WWOX splice allele has ever been assayed with an NMD inhibitor** (LEGEND's
splice census, roman-class zeros for `cycloheximide`, `emetine`, `actinomycin`, `nonsense-mediated`). The degraded
fraction is unknown for this allele, as it is for every WWOX allele.

### 3.4 · Cryptic acceptor — **NOT ASSESSED. Stated as not assessed rather than guessed.**

I have **no** SpliceAI, MaxEntScan or Pangolin run for `c.517-2A>G`, and no access to the intron 5 / exon 6
sequence. LEGEND holds such predictions for the *other* acceptor allele (`c.1057-2A>G`: SpliceAI DS_AL 0.96,
MaxEntScan Δ−7.95, cryptic acceptor gain +8 nt DS_AG 0.64) and **holds none for `c.517-2A>G`**. Plausibility here
would be invention. What can be said is bounded and comes from LEGEND's census: across all four measurements of any
WWOX splice-affecting allele, **every reported product was an exon-skipping event** — no intron retention, no
cryptic site reported — but the census also records that the only readable instrument was a shortened-intron
two-exon minigene, which is **a poor instrument for detecting the other two possibilities**, so absence there is
not exclusion.

---

## 4 · Task 2 — Is the sequencing data deposited?

### 4.1 · PMID 34268881 / PMC8350905 (2021, *EMBO Mol Med*) — **YES, one dataset, and LEGEND already had the accession**

The Data-availability block, read verbatim this session:

| Locator | Quotation | Source · section | Depth |
|---|---|---|---|
| **T-3** ⭐ | *"Data and code availability — The RNA‐seq dataset produced in this study is available in the following databases: RNA‐seq data for week 15 cerebral organoids: Gene Expression Omnibus:()."* | PMID **34268881**, Data and code availability | **`body`** |

🔴 **The accession string is empty — deleted by the extractor**, which strips hyperlinked identifiers. `GSE156243`
occurs **0 times** on this surface, and `accession` and `deposit` occur 0 times. **None of those zeros is evidence
of absence**; the sentence itself proves a GEO accession exists. **LEGEND independently holds the accession**:
`discovery_ledger_current` `DL-MECH-034` records *"RNA-seq pubblico su GEO **GSE156243**"* and `DL-MOL-010` repeats
it. ⚠️ **I did not read `GSE156243` verbatim from the paper**, and I did not query GEO — no tool, no egress. The
accession is carried here **on LEGEND's authority, not on mine.**

**Scope: exactly one dataset — week-15 cerebral organoids. No second deposit, no raw-data repository, no
controlled-access entry.** Terms: GEO is open access.

### 4.2 · PMID 42397075 (2026, *Brain*) — **UNKNOWN, and unknown is not the same as absent**

- **No PMC deposit.** LEGEND's manifest records the test rather than assuming it: *"No PMC deposit: esummary returns only pubmed, doi and pii, and elink to pmc returns nothing."*
- The local artifacts the manifest fingerprints (`files/fulltext/PMID42397075_Aqeilan2026.pdf`, `_fitz.txt`, and the rendered supplementary pages) **are not present in this environment**; `files/fulltext/` does not exist here.
- Neither the 30-entry manifest nor the 368-line dossier records a data-availability statement, an accession, or a sequencing platform. I searched both for `availab`, `accession`, `GEO`, `deposit`, `10x`, `Chromium`, `library`, `sequenc` — the only hit is the PMC-absence note.
- A Scholar Gateway semantic pass aimed at this paper's single-cell methods and accession **did not return it**.

⇒ **No accession established. Whether the 2026 single-cell data is deposited, and whether openly or under
controlled access, is UNDETERMINED from here.** Per the brief, that distinction decides everything downstream, and
it is left open rather than guessed.

### 4.3 · The bioRxiv preprint — **no accession recorded**

LEGEND holds it as **`PAPER 001`** — *"Steinberg 2024 organoids · WWOX deficiency impairs neurogenesis and neuronal
function in human organoids · bioRxiv · **Identifier: preprint**"*, with no DOI and no accession in the record.
Not reachable from here. Whether the preprint and the *Brain* version differ in what they deposit is **untested**.

---

## 5 · Tasks 3 and 4 — Would either dataset answer the question?

### 5.1 · The 2021 bulk dataset — **right instrument, wrong cells. This is the decisive finding.**

**The chemistry is suitable**, read verbatim this session:

| Locator | Quotation | Source · section | Depth |
|---|---|---|---|
| **T-4** | *"For mRNA library preparation, 1 µg of RNA per sample was processed using KAPA Stranded mRNA‐Seq Kit with mRNA Capture Beads (Kapa Biosystems; KK8421)."* | PMID **34268881**, Library preparation and RNA sequencing | **`body`** |
| **T-5** | *"Multiplex sample pool (1.5pM including PhiX 1.5%) was loaded in NextSeq 500/550 High Output v2 Kit (75 cycles) cartridge (Illumina; FC‐404‐1005) and loaded on NextSeq 500 System Machine (Illumina), with 75 cycles and single‐read sequencing conditions."* | PMID **34268881**, same section | **`body`** |

Bulk, poly-A selected, **stranded**, **75 bp single-end**. Coverage is spread across the transcript body rather
than piled at one end, and 75 nt is long enough for a read to straddle a junction with ~25–30 nt of anchor on each
side. **This chemistry could in principle carry the c.516/c.606 junction.**

🔴 **But the samples are wrong, and the paper says so twice:**

| Locator | Quotation | Source · section | Depth |
|---|---|---|---|
| **T-6** ⭐ | *"RNA sequencing (RNA‐seq) of week 15 COs and transcriptome analysis (WT:= 2, KO:= 4)."* (the extractor has dropped the italic *n* before each `=`) | PMID **34268881**, Figure 4 legend | **`body`** |
| **T-7** | *"Therefore, we reprogrammed peripheral blood mononuclear cells (PBMCs) donated from two families with WWOX‐related diseases, differing in their severity: The first family carries a c.517‐2A>G splice site mutation (Weisz‐Hubshman,) that results in the WOREE syndrome (DEE28) phenotype in the homozygous patient (referred to as WSM family)"* | PMID **34268881**, Results | **`body`** |

⚠️ **Token note on T-7:** the extracted surface uses a non-ASCII hyphen, `c.517‐2A>G`. The coordinate, the
zygosity ("homozygous patient") and the family label (WSM) are reproduced exactly. **This independently confirms,
from a TEXT surface, the genotype that LEGEND otherwise holds only as a figure attestation from the 2026 paper.**

**`WSM` occurs 86 times in this body. It co-occurs with any RNA/sequencing/PCR term in exactly two sentences, and
both are qPCR:** *"The status of the Wnt pathway was also assessed using qPCR, with findings suggestive of
activation in week 10 WSM S COs…"* and the corresponding legend *"qPCR analysis for selected Wnt target genes in
week 10 WSM COs."*

⇒ **The patient line was never RNA-sequenced in the 2021 study.** The deposited dataset is wild-type versus
**engineered** knockout — a CRISPR lesion in WiBR3 hESC, **not a splice allele**. **GSE156243 therefore contains no
`c.517-2A>G` transcript at all, and no amount of reanalysis can extract one.** Closed.

### 5.2 · The 2026 single-cell dataset — **right cells, and on every reachable indication the wrong instrument**

**I could not establish the chemistry.** No methods surface was reachable (§4.2). What follows is **INFERENCE, with
its basis stated**, not a reading:

1. **Throughput.** LEGEND's manifest records **28,208 cells sequenced, 26,352 after QC, 12 clusters**, across a panel that includes WT, engineered KO, and WOREE and SCAR12 patient lines. Plate-based full-length protocols (Smart-seq2/3) operate at hundreds to low thousands of cells; **28,208 cells across that many lines is droplet-scale throughput.** Inference: droplet-based tag chemistry, 3′ or 5′.
2. **Where the variant sits.** WWOX CDS is 1,242 coding nt (414 aa). `c.517` leaves **1,242 − 516 = 726 coding nucleotides downstream**, plus the entire 3′UTR, before the poly-A site; and 516 nt plus the 5′UTR upstream of the cap. **`c.517` is near neither end of the transcript.** A 3′-tag read (~90 bp from the poly-A end) and a 5′-tag read (~90 bp from the cap) both fall hundreds of nucleotides short of the exon 5/6 and 6/7 junctions.
3. **Depth per cell.** Droplet scRNA-seq recovers a small fraction of each cell's transcripts, and WWOX is not a high-expressor. Even with a junction-spanning chemistry, per-cell junction read support would be at or near zero.
4. 🔴 **And the confound that does not care about chemistry.** The transcript a splice assay is trying to observe is the one **NMD is predicted to destroy** (§3.3). Poly-A-capture scRNA-seq measures the **steady-state surviving pool**. **An absent aberrant transcript is not an absent aberrant splicing event** — it is the expected appearance of a successfully degraded one.

⇒ **Stated plainly, as the brief asks: no, this chemistry almost certainly cannot see that junction, and the idea
closes here.** ⚠️ **The one thing that would overturn this is cheap and specific:** a methods sentence naming the
kit. If the 2026 paper used a full-length or a targeted/long-read protocol, points 1–3 fall and only point 4
remains. **That single sentence is the whole question**, and it is not reachable from this environment.

### 5.3 · Task 4 — Is there bulk RNA-seq in the 2026 paper?

**Undetermined, and the one indication points away from it.** The phrase the brief quotes —
*"we applied molecular profiling and single-cell transcriptomics"* — does not name bulk RNA-seq. LEGEND's manifest
entry 19 records the study's own statistics sentence: *"Experiments were performed in independent differentiations,
except for single-cell RNA-"* (fragment ends at a line break), with the manifest noting the exceptions are
**single-cell RNA-seq, MYC inhibition and NSCs ChIP-seq**. That names a **ChIP-seq** and a **single-cell** assay;
**no bulk RNA-seq is named anywhere in LEGEND's record of this paper.** Manifest entry 26 reports
**pseudobulk** logFC values computed *from the single-cell data* — which is a derived quantity, not a separate bulk
library, and pseudobulk inherits the parent chemistry's coverage limits exactly. **If a bulk library exists it is
not visible from here.**

---

## 6 · Task 5 — Any other public dataset containing a WWOX splice-allele carrier's RNA?

**None found.** All of the following are **query censuses on 2026-09-21, not biological zeros**, and I had **no GEO,
SRA, ArrayExpress or EGA query tool** — so this is a census of the *literature*, which is a weaker instrument than a
census of the *repositories*.

| Probe | Result |
|---|---|
| `WWOX organoid iPSC single-cell transcriptome WOREE SCAR12` | **1** record — PMID 42397075 only |
| `WWOX patient fibroblasts RNA sequencing transcriptome WOREE deposited` | **0** records |
| GEO accessions anywhere in LEGEND (repo-wide scan) | **5** — `GSE156243` (WWOX-KO organoids, §4.1), `GSE117387`, `GSE126075`, `GSE193659`, `GSE31684`. None of the other four is recorded as carrying a WWOX splice-allele carrier |

**The Genoa group (PMID 35573960).** Per the brief this is `HUMAN_REQUIRED` and **no contact was attempted**. For
the record: the paper is **absent from LEGEND's paper registry and tracking log** — it appears only as a queue item
in `FT-032` with surface `absent`, so LEGEND has **not** read it. **Whether they deposited anything is undetermined
from here** and would require a repository query this environment cannot make.

---

## 7 · Corrections against prior LEGEND text — and one against the brief

| # | Standing text | Correction | Basis |
|---|---|---|---|
| **C-1** 🔴 | **`PAPER 025`** carries `Short title: Piard 2019 EJPN exon 6 / Q230P`, `Authors: Piard et al.`, and `Full title: Novel WWOX deleterious variants cause early infantile epileptic encephalopathy, severe developmental delay and dysmorphic features`. | **Right identifier, wrong author, wrong title.** PMID 30853297 / DOI 10.1016/j.ejpn.2019.02.003 is **Weisz-Hubshman M, Meirson H, … Heimer G**, and the title ends **"…and dysmorphism among Yemenite Jews"**, not "dysmorphic features". *(LEGEND's own splice census already lists this PMID under "Heimer G. / Basel-Salmon L. · Sheba & Schneider, Israel", so the registry and the census disagree with each other.)* This matters because `PAPER 025` is the cited source of **`CLAIM 018` and `CLAIM 019`** — one of them a `consolidated baseline`. **Flagged, not edited — read-only actor.** | PubMed metadata, retrieved this session |
| **C-2** 🔴 | **The brief states** that `c.517-2A>G` destroys *"the same acceptor whose −3 neighbour LEGEND has been reasoning about."* | **Not the same acceptor.** LEGEND's acceptor of interest is **`c.1057-2A>G` = the exon 9 acceptor**; `c.517-2A>G` is the **exon 6** acceptor, ~540 coding nucleotides away. No `−3` neighbour variant exists in LEGEND for either. 🔴 **The distinction is load-bearing, not pedantic:** LEGEND's own registry records that an exon-6 lesion **undergoes NMD** while **exon 9 is the last exon, so a PTC there escapes NMD**. **The two alleles sit in opposite NMD regimes**, and conflating them would invert the predicted outcome and mis-specify the assay. LEGEND itself keeps them properly separate (`CLAIM 002`: *"Il rescue del modello con variante splice `c.517-2A>G` … non dimostra che un ASO corregga `c.1057-2A>G`"*). | this session |
| **C-3** ⚠️ | **`CLAIM 018`** — *"The exon 6 splice-site variant c.517-2A>G is pathogenic and causes exon 6 skipping in humans"* — status **`consolidated baseline`**, type **`DATO`**. | **The claim is substantively correct and its exon number is now verified verbatim (T-1). Its evidence depth is not `DATO`-grade.** The `Source` line says `abstract-supported`, and LEGEND's splice census is blunter: *"È una frase di abstract su un paper irraggiungibile: riportato-come-misurato ma non letto, censimento e non evidenza."* A `consolidated baseline` resting on one unread abstract is a status/depth mismatch. **Reading the abstract verbatim this session raises token confidence and changes nothing about depth.** | this session; `wwox_splice_transcript_census_20260921.md` |
| **C-4** ℹ️ | The brief cites the genotype table as **manifest entry 27** and the platform validation as **entry 29**. | **They are entries 28 and 30** in `verbatim_locators.entries` (1-indexed; the list has 30). Almost certainly 0-vs-1 indexing. Content is exactly as quoted. **I record my own error too:** my first parse read `verbatim_locators` as a list and reported only 6 entries — it is a dict whose `entries` key holds the 30. The brief's provenance was sound; my parse was not. | this session |

---

## 8 · What LEGEND already knew, separated from what is new

**Already held — not re-reported as new:**
- `CLAIM 018` (c.517-2A>G → exon 6 skipping), `CLAIM 002` (organoid rescue, with the explicit warning not to transfer it to `c.1057-2A>G`), `CLAIM 019` (Q230P).
- The whole splice-transcript census: 20 records, 3 measured / 2 annotated, one reachable paper, no NMD inhibitor ever used on any WWOX splice allele, no aberrant:normal ratio anywhere, no protein ever observed from a WWOX splice allele, and `TX-001`'s efficacy endpoint therefore having no baseline.
- `GSE156243` as a public GEO dataset from the 2021 paper (`DL-MECH-034`, `DL-MOL-010`).
- That the Aqeilan lab holds the WSM (`c.517-2A>G` homozygous) and WPM (G372R) patient iPSC lines (`DL-MOL-010`).
- That exon 6 lesions undergo NMD while exon 9 is the last exon and escapes it (`DL-MECH-045`).
- That exon 6 is 89 nt.
- 🔵 **`DL-MOL-011` in full** — that an SSO cannot rebuild a destroyed invariant AG, that U1 snRNA corrects donors not acceptors, that ADAR runs the wrong direction, that a CBE on the antisense (or prime editing) is the mechanistically valid lever, that this is **parked pending external verification with `TX-001` not demoted**, and that the assay's value survives as **VUS reclassification (ACMG `PS3`) plus a baseline for any correction strategy including editing**. **None of this is re-derived here** (§2A).
- The 2026 paper's line genotypes and the 28,208/26,352/12-cluster platform numbers (manifest entries 28 and 30, figure attestations).

**New this session:**

| # | Finding |
|---|---|
| **N-18** ⭐ | **`GSE156243` cannot answer the question, and the reason is definitive, not probabilistic:** the 2021 RNA-seq is **WT n=2 vs engineered KO n=4** (T-6), and the WSM patient line appears in that paper only in **Wnt qPCR** — never in RNA-seq. **The deposited dataset contains no `c.517-2A>G` transcript.** LEGEND held the accession and had never established what was *in* it. |
| **N-19** ⭐ | **The 2021 library chemistry is recorded for the first time** — KAPA Stranded mRNA-Seq, poly-A capture, **75 bp single-end** on NextSeq 500 (T-4, T-5). This is the *correct* instrument for junction detection, which is what makes N-18 a genuinely near miss rather than a non-starter. |
| **N-20** ⭐ | **Independent, TEXT-surface confirmation of WSM = `c.517‐2A>G` homozygous** (T-7). LEGEND previously held this genotype only as a **figure attestation**; it now has a prose source. |
| **N-21** | **The exon boundaries reproduce independently**: acceptor-to-acceptor arithmetic gives **c.517–c.605 = 89 nt**, matching LEGEND's held value by a route that does not use it; and `c.517` is base 1 of codon 173, so **the exon opens in frame and ends phase 2 — skipping is a frameshift, not an in-frame deletion.** |
| **N-22** | **The 2021 Data-availability block lists exactly one dataset**, and the **accession string is deleted by the extractor** (T-3) — a concrete instance of a parser deletion that would read as an absent accession. |
| **N-23** | **No accession is establishable for the 2026 *Brain* paper** from any surface reachable here, and **no bulk RNA-seq is named anywhere in LEGEND's record of it** — the pseudobulk values in manifest entry 26 are derived from the single-cell data, not a separate library. |
| **N-24** | **PMID 30853297 is also a Q230P primary** (T-2) — the two worked-example allele classes of this repository meet in one 2019 case series. |
| **N-25** ⭐ | **The allele boundary on `DL-MOL-011` is drawn for the first time** (§2A): its SSO, U1, ADAR and base/prime-editing arguments **transfer** to `c.517-2A>G` because they are mRNA-element-level and DNA-level arguments; its `DL-MECH-045` companion conclusion — *acceptor allele ⇒ truncated unstable protein* — **does NOT transfer**, because it depends on exon 9 being the last exon. §3.3's independent frame calculation puts `c.517-2A>G` in the **opposite NMD regime**. The `+8` cryptic-masking sub-argument has **no counterpart** for this allele, since no splice prediction for it exists. |

---

## 9 · Task 6 — What a bioinformatician would do, **if** an open accession existed

**Stated conditionally, because §4.2 leaves the accession undetermined and §5.1 has already closed the only
accession that is known.**

Given an open GEO/SRA accession for the 2026 *Brain* single-cell experiment, the analyst would pull the samples for
the **WOREE WSM S line (`c.517-2A>G` homozygous)** as the test, the **WOREE WCH S line** (`c.517-2A>G` in trans
with `c.410G>T`) as a second independent carrier, and — indispensably — the **wild-type lines differentiated in the
same experiment** as the control, because a splice ratio is only interpretable against the normal splicing rate of
the same protocol, batch and cell type; the engineered KO is **not** a usable comparator here, since it carries no
splice allele and its WWOX locus is disrupted by a different lesion. Alignment would use a splice-aware aligner
against the reference with **WWOX-specific junction counting at the exon 5/6 and exon 6/7 boundaries**, and the
quantity reported would be a **ratio, not a count**: junction-spanning reads supporting the normal `c.516|c.517`
and `c.605|c.606` junctions versus reads supporting the skipped `c.516|c.606` junction, in the same library, with
the WT ratio as the denominator. Evidence would require **junction-spanning reads with a real anchor on both sides**
(≥20 nt, uniquely mapping, not soft-clipped into the intron) in **multiple independent cells or samples** — a
handful of reads in one library is an artefact, not a measurement. The four outcomes are distinguishable and must
be pre-specified: **exon skipping** = reads joining `c.516` to `c.606`; **intron retention** = continuous coverage
extending into intron 5 past the disrupted acceptor; **a cryptic acceptor** = a novel junction whose 3′ end sits at
neither `c.517` nor `c.606`, which would also shift the frame arithmetic in §3.3 and must be re-derived, not
assumed; **leaky normal splicing** = normal-junction reads still present in the carrier, whose *fraction* is use 3
of §2A — the only route by which a partially functional outcome survives, and unmeasured for every WWOX splice
allele. ⚠️ **The output serves all three uses of §2A and is neutral between therapeutic levers:** a measured
transcript consequence is `PS3`-grade evidence for reclassification and a pre-correction denominator for **any**
strategy, ASO or base/prime editing alike. **Nothing here presumes which lever is correct**, and `DL-MOL-011`
remains parked pending external verification.

🔴 **The confounds, named.** **(1) NMD depletes the very transcript being counted** — an absent aberrant junction
is *the predicted appearance of a successfully degraded transcript*, not evidence that splicing was normal, and no
NMD-inhibitor arm exists in any published WWOX dataset to calibrate against. **(2) Coverage is not uniform** — in a
tag-based chemistry the mid-gene region has no reads at all, so a zero there measures the protocol, exactly as a
parser zero measures the extractor. **(3) Poly-A capture** selects for stable, polyadenylated species and therefore
against the degradation intermediates. **(4) Allelic ratio ≠ splicing ratio** in a homozygote: with both alleles
mutant there is no internal wild-type control within the sample, which is why the same-experiment WT lines are not
optional. **(5) Pseudobulk does not rescue coverage** — summing cells raises depth but cannot create reads where the
chemistry places none.

**Verdict on the whole route: not actionable today.** The one open dataset is closed by N-18. The one dataset with
the right cells has no established accession and, on chemistry grounds, almost certainly no reads at the junction.
🔵 **The cheapest thing that would change this answer is not a reanalysis — it is one sentence.** Obtain the
*Brain* 2026 Methods paragraph naming the single-cell kit and the data-availability accession. If it names a
full-length, targeted or long-read protocol and an open accession, §9 becomes executable; if it names 10x 3′ or 5′,
this node is closed permanently and cheaply. **That is an acquisition task, not an analysis task.**

---

## 10 · Declaration

Author: **Scientist A**. Date: **2026-09-21**. **READ-ONLY** toward every canonical file, registry, ledger and
queue: nothing was edited, no registry record created or amended (C-1, C-3 flagged only), no receipt recorded, no
commit candidate produced, no git operation performed. **Nothing was downloaded and no raw data was accessed or
processed** — availability and terms only, as instructed. **No contact was made with any research group.** This
file is the single file written. **Not medical advice.**

**Declared limits.** No figure panel inspected; the iPSC-line genotype table is LEGEND's prior figure attestation,
not my observation. PMID 30853297 was reachable **only at abstract depth** and PMID 42397075 **not at all** — the
local artifacts its manifest fingerprints are absent from this environment. **No sequence database, no RefSeq exon
table, and no GEO/SRA/ArrayExpress/EGA query tool was available**, so the exon-boundary arithmetic in §3.2 is
corroborated but not independently verified against `NM_016373.4`, and §6 is a census of the literature rather than
of the repositories. The frame and NMD consequences in §3.3 are **my own arithmetic and a rule of thumb**, labelled
`PREDICTED` throughout and never presented as measured. The 2026 chemistry judgement in §5.2 is **inference from
throughput and transcript geometry**, with the single sentence that would overturn it named. All "zero" statements
are **PubMed query censuses on 2026-09-21**, not biological zeros, and no negative rests on a string count in
extracted body text — the one striking zero encountered (`GSE156243` = 0 occurrences in PMC8350905) is explicitly
identified as a **parser deletion**, not an absence.

*Article metadata and full texts **retrieved from PubMed / PubMed Central**; one semantic pass via Scholar Gateway
which returned nothing attributable to the target paper.*

**DOIs** (read from PubMed metadata records retrieved this session, except as noted):
[30853297](https://doi.org/10.1016/j.ejpn.2019.02.003) ·
[34268881](https://doi.org/10.15252/emmm.202013610) *(DOI from PMC record identifiers; journal EMBO Mol Med 2021)* ·
[38161429](https://doi.org/10.3389/fped.2023.1301166) ·
[30158849](https://doi.org/10.3389/fnins.2018.00563) ·
[42397075](https://doi.org/10.1093/brain/awag239) *(DOI as recorded in LEGEND's manifest; the paper was not reachable this session)* ·
[35573960](https://doi.org/10.3389/fped.2022.847549) *(DOI as recorded in LEGEND's `FT-032`; not independently re-verified)*.
