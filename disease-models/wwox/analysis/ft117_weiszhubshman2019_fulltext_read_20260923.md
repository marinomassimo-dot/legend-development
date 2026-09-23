# FT-117 — PMID 30853297, Weisz-Hubshman 2019: first-hand full-text read of the RNA/splice evidence

**Node:** `FT-117_FULLTEXT_READ_PMID_30853297` · **Actor:** SCIENTIST-1 · **Date:** 2026-09-23
**Status:** non-canonical analysis file. **No registry, queue, `current_*.md`, ledger or state manifest was
edited. No receipt recorded. No commit. No git operation.**
**Public edition — no contact details, no identifying information of any living person. Not medical advice.**

---

## 0 · Public-edition redaction note — read this first

🔴 **Pedigree coordinates and transmission relationships have been removed from this file.** The source
publishes a family-tree figure with per-individual genotypes; that presentation is individual-level linkage,
which this edition excludes by design. Three classes of content were removed and replaced:

| Removed | Replaced by | Why |
|---|---|---|
| **Every pedigree coordinate** (generation/position identifiers) | **Role labels**, disambiguated per family — see the table below. Coordinates collide across families in the source, so no mechanical substitution was possible; each was resolved by hand against the pedigree figure | individual linkage |
| **Every transmission / line-of-descent attribution**, and any pairing of the two ancestries within a family | **Allele-level and family-level statements only.** Which relative transmitted which allele is **not retained**, and the two ancestral sides of a family are **never split apart** | individual linkage; the science does not need it |
| **Identifying clinical measurements** — birth weight, head-circumference values and percentiles, sex, exact birth order, Apgar scores | Qualitative findings only | these identify rather than inform |

**Kept, because they are genotype-class evidence and carry the file's value:** age at seizure onset, EEG
pattern, MRI finding, developmental-milestone status, survival status, and every molecular, RNA and
statistical result.

**Role labels used throughout** (the mapping from the source's coordinates is deliberately not recorded here):

| Label | Genotype | Status |
|---|---|---|
| `family 1 / homozygote A` · `family 1 / homozygote B` | `c.517-2A>G/c.517-2A>G` | affected |
| `family 1 / unaffected splice carriers` (two) | `c.517-2A>G/WT` | unaffected |
| `family 2 / compound heterozygote 1` · `family 2 / compound heterozygote 2` | `c.517-2A>G/c.689A>C` | affected |
| `family 2 / unaffected Q230P carriers` (two) | `c.689A>C/WT` | unaffected |
| `family 2 / unaffected splice carriers` (two) | `c.517-2A>G/WT` | unaffected |
| `family 2 / unaffected non-carrier` (one) | `WT/WT` | unaffected |
| `family 3 / homozygote A` — **the exome subject**, died in infancy | `c.517-2A>G/c.517-2A>G` | affected |
| `family 3 / homozygote B` — 🔴 **the individual carrying ALL the RNA data** (gel + qPCR) | `c.517-2A>G/c.517-2A>G` | affected |
| `family 3 / unaffected splice carrier — gel lane` | `c.517-2A>G/WT` | unaffected |
| `family 3 / unaffected splice carriers` (siblings and an earlier branch) | `c.517-2A>G/WT` | unaffected |
| `family 3 / unaffected non-carrier` (one) | `WT/WT` | unaffected |

**Inside a verbatim quote, `⟦…⟧` marks a redaction.** The characters inside the brackets are mine; everything
outside them is the source's. No other character of any quote has been changed.

---

## 1 · The headline, before the detail

**The paper was read first-hand, end to end, all nine pages (418–426), plus the publisher figure pack.**
Ten of the ten hypotheses handed to me are substantially confirmed **on their arithmetic and their numbers**.
But the read changes the *evidential grade* of the splice claim in three ways the preliminary read could not see:

| # | What changes | Direction |
|---|---|---|
| **H-1** 🔴 | **The exon-6 skip is demonstrated by PRODUCT SIZE, not by a reported junction sequence.** §3.4 reports two band sizes and says the result "is consistent with the prediction". The abstract's *"Complementary DNA sequencing demonstrated … skipping of exon six"* is **stronger than the Results text it summarises.** | **NARROWS** `CLAIM 018` |
| **H-2** 🔴 | **The two-band result asserted in §3.4 for the family-2 compound heterozygotes is shown in NO figure.** The only cDNA gel (Fig. 4C) is family 3 and contains no family-2 lane. | **NARROWS** |
| **H-3** ⭐ | **The RNA is from BLOOD, and it worked** — RT-PCR gave clean bands and qPCR gave a control mean of 10.7 relative units. This is a direct, first-hand answer to the `S-1` worry carried in the 2026-09-21 file (§6, `N-33`) that WWOX RNA cannot be assessed in blood or fibroblasts. | **CONTRADICTS** `S-1` as a blanket statement |

And one finding that matters more than any of them for the leakiness question:

> 🔴 **H-4 — the homozygote's single band is a GEL-LEVEL negative with no assay behind it capable of finding
> residual correct splicing.** No densitometry, no replicate, no allele-specific assay, no NMD block, and the
> one quantitative assay in the paper (qPCR) sits at **exons 8–9 — downstream of exon 6 — so it cannot
> distinguish a normally spliced transcript from an exon-6-skipped one.** The paper shows *no detected*
> correct splicing. It does not show *no* correct splicing, and it never claims to.

---

## 2 · Identity of the paper — settling the "Piard" attribution error

**DATO** — verbatim, from the publisher figure pack, slide 1 (`ppt/slides/slide1.xml`), which is a
space-bearing surface deposited by Elsevier:

> "Novel WWOX deleterious variants cause early infantile epileptic encephalopathy, severe developmental delay
> and dysmorphism among Yemenite Jews
> M. Weisz-Hubshman, H. Meirson, R. Michaelson-Cohen, R. Beeri, S. Tzur, C. Bormans, S. Modai, N. Shomron,
> Y. Shilon, E. Banne, N. Orenstein, O. Konen, D. Marek-Yagel, A. Veber, N. Shalva, E. Imagawa, N. Matsumoto,
> D. Lev, T. Lerman Sagie, A. Raas-Rothschild, B. Ben-Zeev, L. Basel-Salmon, D.M. Behar, G. Heimer
> European Journal of Paediatric Neurology
> Volume 23 Issue 3 Pages 418-426 (May 2019) DOI: 10.1016/j.ejpn.2019.02.003"

Corroborated inside the PDF itself: the running footer on **all nine pages** reads
`european journal of paediatric neurology 23 (2019) 418e426` (the `e` is the extractor's rendering of the
en-dash), and page 418 carries `https://doi.org/10.1016/j.ejpn.2019.02.003`. Joint first authors
**Weisz-Hubshman and Meirson**; joint senior authors **Behar and Heimer** (footnotes 1 and 2, p. 418).

🔴 **`Piard` does not appear anywhere in this paper.** Earned zero — the same search returned 49 hits for
`WWOX`, 18 for `splice`, 47 for `patient`.

**Therefore the attribution error is confirmed as an error.** `PMID 30853297` is **Weisz-Hubshman et al. 2019**,
*Eur J Paediatr Neurol* 23(3):418–426. **Piard J** is first author of a *different* 2019 WWOX paper,
**PMID 30356099**, *Genet Med* (the 20-case WOREE phenotypic-spectrum cohort), which this repository holds
separately. The two must never be merged.

⚠️ **Where the error still lives, for the operator to route** (I did not edit these):
- `disease-models/wwox/research/full_text_queue_current.md:62` — *"PMID 30853297 / DOI 10.1016/j.ejpn.2019.02.003 — Piard et al. 2019"*
- `paper_registry_current.md` → `PAPER 025` byline and short title (already diagnosed in
  `CC-20260921-PAPER025-IDENTITY-01` and in `tx001_public_rna_data_feasibility_20260921.md` C-1)
- `dismech_legend_evidence_crosswalk_v2.md:622` records `CLAIM 017`'s `Source` as *"Piard 2018"* resolving to
  `PAPER 025`

---

## 3 · Instrument declaration — read this before trusting any quote below

🔴 **The PDF text layer of this article contains NO space characters.** 33,277 characters extracted; the body
renders as `cDNAanalysisofthecompoundheterozygotepatients…offamily2yielded…`. Characters, digits,
punctuation and word order are faithful; **inter-word spacing is not present and has been reconstructed by me**
in every body-text quote below.

**Consequence, stated once and applied throughout:**
- **Body-text quotes are `DATO` for their characters, digits and word order; the spacing is mine.** I have
  changed no character, added no word, and removed none — except the bracketed redactions declared in § 0.
- **Figure-legend quotes are otherwise fully verbatim** and are taken from the figure pack's
  `notesSlides/*.xml`, which carries Elsevier's own spaced text. Where a legend also appears in the PDF I
  checked the two agree.
- 🔴 **The hyphen-deletion defect (`N-36` in the 2026-09-21 file) is LIVE on this artefact too.** The abstract's
  instance of the variant extracts as **`c.5172A>G`** — the hyphen is gone. Every other instance in the body
  extracts correctly as `c.517-2A>G`. **No variant coordinate in this file is quoted from the abstract's
  extraction**; all are taken from body instances and cross-checked against the figure pack, which renders
  `c.517-2A &gt; G` with the hyphen intact.
- Ligature loss: `fi` renders as `Þ` (`identiÞed`, `Þrst`, `signiÞcant`). Silently normalised in my quotes and
  flagged here instead.

**Tooling actually available:** no `pymupdf`, no `pdfplumber`, no poppler, no PIL, no numpy, no ImageMagick
(`tool_preflight.py`: 4 of 6 optional tools absent). Figures were read by decoding the `.pptx` zip and viewing
the deposited JPEGs at the resolution the reader renders them. **No figure was cropped or magnified**, and
every figure statement below is qualified accordingly.

**Artefacts read (sha256):**
- `files/fulltext/PMID30853297_WeiszHubshman2019.pdf` → `9cb9d2a27100ffde68cb60478cbd0e2bf5504d9dd46f2ed547849425851c06c4`
- `files/fulltext/PMID30853297_WeiszHubshman2019_figurepack.pptx` → `ec8fe4d2d637307b7b029ea8c24cdac07fae10ca08007eb0e693c033ca19115f`

**Completeness check:** page footers recovered for **419, 420, 421, 422, 423, 424, 425, 426** plus the p. 418
first-page block. **All nine pages are present.** Page attributions below are derived from those footers.

**Earned-zero declaration.** Two searches were run, each with positive controls that returned non-zero
(`WWOX` 49, `exon` 7, `blood` 2; `WWOX` 49, `splice` 18, `patient` 47). Only then are these zeros reported:
`fibroblast` **0** · `lymphoblast` **0** · `lymphocyte` **0** · `minigene` **0** · `cycloheximide` **0** ·
`puromycin` **0** · `densitometry` **0** · `residual` **0** · `leaky` **0** · `supplementary` **0** ·
`Western` **0** · `blot` **0** · `in-frame` **0** · `cryptic` **0** · `Piard` **0**.

---

## 4 · The ten items, verified

### Item 1 — `c.517-2A>G`: zygosity and who carries it

✅ **CONFIRMED, and now resolved to the level of role and genotype.**

**DATO** — Abstract (p. 418): *"four of the patients were homozygous for a novel WWOX c.517-2A>G splice-site
variant and two were compound heterozygous for this variant and a novel c.689A>C, p.Gln230Pro missense
variant."*

**DATO** — §3.2.1 (p. 422): *"The novel homozygote chr16:g.78420755A>G (GRCh37); c.517-2A>G (NM_016373)
variant was identified in the WWOX gene"* (the in-text call-out reads `(Fig. 3A)` — a **cross-reference
error**; the Sanger panel is `Fig. 4A`).

**DATO** — §3.3 (p. 423): *"Both variants were validated by Sanger sequencing and fully segregated with the
disease in all 3 families consistent with autosomal recessive inheritance"*.

**Genotypes, read directly off the Fig. 1 pedigree figure** (figure pack `media/image2.jpeg`; genotypes are
printed under each symbol) and restated here at role level:

| Family | Role | Genotype as printed | Affected |
|---|---|---|---|
| **1** | homozygote A | `c.517-2A>G/c.517-2A>G` | ✅ |
| **1** | homozygote B | `c.517-2A>G/c.517-2A>G` | ✅ |
| **1** | two unaffected splice carriers | `c.517-2A>G/WT` each | no |
| **2** | compound heterozygote 1 | `c.517-2A>G/c.689A>C` | ✅ |
| **2** | compound heterozygote 2 | `c.517-2A>G/c.689A>C` | ✅ |
| **2** | two unaffected Q230P carriers | `c.689A>C/WT` each | no |
| **2** | two unaffected splice carriers | `c.517-2A>G/WT` each | no |
| **2** | one unaffected non-carrier | `WT/WT` | no |
| **3** | homozygote A (exome subject) | `c.517-2A>G/c.517-2A>G` | ✅ |
| **3** | **homozygote B (RNA subject)** | `c.517-2A>G/c.517-2A>G` | ✅ |
| **3** | unaffected splice carrier — **gel lane** | 🔴 `c.517-2A>G/WT` | no |
| **3** | further unaffected splice carriers (sibship + an earlier branch) | `c.517-2A>G/WT` each | no |
| **3** | one unaffected non-carrier | `WT/WT` | no |

**So:** **6 affected across 3 families — 4 homozygous `c.517-2A>G` (families 1 and 3, two each), 2 compound
heterozygous `c.517-2A>G`/`c.689A>C` (family 2).** `c.517-2A>G` is carried in **all three families**;
`c.689A>C` in **family 2 only**. Every unaffected genotyped relative is a heterozygote or a non-carrier —
consistent with the autosomal-recessive segregation the paper states.

**DATO** — gnomAD, §3.2.1 / §3.3: *"This variant is extremely rare and its prevalence in the general population
according to gnomAD database was 0 (out of 245,866 alleles)."*

**Family 3 structure — DATO, §3.1.3, p. 422, at family level:** family 3 is **consanguineous** (a third-degree
cousin union) and carries a family history of epileptic encephalopathy with **infantile death in four of nine
children of an earlier branch**.

🔵 **INFERENZA (coordinate cross-check, resolved offline and it lands clean).** The paper gives
**`chr16:g.78420755A>G (GRCh37)`**. `disease-models/wwox/analysis/data/WWOX_clinvar_all_variants.csv` holds
`VCV003774965 NM_016373.4(WWOX):c.517-2A>G` at **chr16:78,386,858 (GRCh38 / NC_000016.10)**. The offset
78,420,755 − 78,386,858 = **33,897 bp**, which is the GRCh37→GRCh38 shift for this region. **The paper's
coordinate and LEGEND's derived exon table agree after liftover.** Recorded because a reader comparing the two
side by side would otherwise call it a contradiction.

---

### Item 2 — 593 bp / 504 bp / 89 bp, and whether 89 bp is exon 6

✅ **ALL THREE NUMBERS CONFIRMED EXACTLY, and 89 = exon 6 is now independently verified offline.**

**DATO** — §3.4, p. 423, *"Complementary DNA analysis in families 2 and 3"*:

> "cDNA analysis of the compound heterozygote ⟦family 2 / compound heterozygotes 1 and 2⟧ of family 2 yielded
> two PCR products sized 593 bp and 504 bp. In contrast, the homozygote ⟦family 3 / homozygote B⟧ of family 3
> yielded only the 504 bp band (Fig. 4C). This is consistent with the prediction that the mutated splice-site
> variant abolishes the acceptor splice-site between exons five and six resulting in an 89 bp deletion of exon
> six in the mutant allele."

**DATO** — Fig. 4C legend:

> "(C) cDNA analysis of the WWOX allele harboring the c.517-2A > G splice-site variant in family 3. A control
> sample yielded one PCR product sized 593 bp. The compound heterozygote ⟦family 3 / unaffected splice
> carrier — gel lane⟧, yielded two PCR products sized 593 bp and 504 bp. The homozygote ⟦family 3 /
> homozygote B⟧ yielded only the mutant 504 bp band."

- **WT product = 593 bp** ✅ (stated for the control sample, and for the upper band in the carrier lane)
- **Mutant product = 504 bp** ✅
- **Difference = 89 bp** ✅ (`593 − 504 = 89`, and the paper itself names *"an 89 bp deletion of exon six"*)

**🔵 INFERENZA — does 89 bp equal exon 6? YES, verified two independent ways without a sequence database:**

1. **From ClinVar coordinates already inside this repository.** `c.605+2T>C` sits at chr16:**78,386,950**
   (GRCh38) and `c.517-2A>G` at chr16:**78,386,858**. Therefore exon 6 spans **78,386,860–78,386,948**, i.e.
   `78,386,948 − 78,386,860 + 1 = ` **89 nt**.
2. **From HGVS arithmetic.** Exon 6 = `c.517`–`c.605` inclusive = `605 − 517 + 1 =` **89 nt**. Confirms the
   figure already held in `splice_allele_rna_evidence_20260922.md` §2.3 line 129.

🔴 **`89 mod 3 = 2` → skipping exon 6 is FRAMESHIFTING. The paper never says so.** `frameshift` occurs **once**
in the whole article, in the Introduction, listing prior variant *classes* — not about this allele. There is no
`in-frame`, no `premature stop`, no predicted protein consequence anywhere. **The frameshift is LEGEND's
arithmetic (`INFERENZA`), not the paper's `DATO`.** Stated because the preliminary read is entitled to know
that the source does not corroborate it.

---

### Item 3 — Is exon-6 skipping the *demonstrated* consequence? Tissue? Method?

**Tissue: BLOOD. Method: RT-PCR on total RNA + gel electrophoresis, with Sanger capability in the pipeline.**
🔴 **But "skipping" as a demonstrated event is weaker than the abstract states.**

**DATO** — §2.4 *"Complementary DNA analysis"*, p. 420, quoted in full:

> "Total RNA was isolated from blood using Trisol reagent (Ambion). cDNA was formed using random primers,
> Reverse-iT 1st Strand synthesis kit (ABgene, Surrey, UK). cDNA amplification was carried out with Redload Taq
> Master*5 (LAEOVA), followed by gel electrophoresis and sequencing by ABI Prism 3100 Genetic Analyzer
> (PerkinElmer). cDNA segment containing exon six was amplified with the primers
> 5'TGGTTGTGGTCACTGGAGCTA3' and 5'AGGATGCACTGCGTTCGAC3'."

- **Tissue = blood.** 🔴 Earned zeros: `fibroblast` **0**, `lymphoblast` **0**, `lymphocyte` **0**,
  `minigene` **0**. It is **whole blood**, not a derived or cultured cell. §2.5 says *"fresh blood"* for the
  qPCR RNA. No PAXgene or globin-depletion step is described; no RNA integrity metric is reported.
- **Method = RT-PCR across exon 6 + agarose gel; the Methods sentence names sequencing on an ABI Prism 3100**,
  so Sanger was part of the pipeline.

🔴 **The narrowing, stated precisely.** The **Results text never reports a sequence**. It reports two band
**sizes**, then says the result *"is consistent with the prediction"*. It does **not** say the 504 bp band was
sequenced, does **not** report an exon-5→exon-7 junction read, and does **not** exclude an alternative 89-nt
loss (e.g. use of a cryptic acceptor 89 nt into exon 6, which would give the identical size). The **abstract**
asserts *"Complementary DNA sequencing demonstrated that the WWOX c.517-2A>G splice-site variant causes
skipping of exon six"* — that is a **stronger claim than its own Results section supports**.

> 🔵 **INFERENZA (mine, and it is the charitable reading):** given the Methods names Sanger, the authors most
> likely did sequence the band. But **charity is not a locator.** What is *published* is a size shift of 89 bp
> plus a statement of consistency with prediction. `CLAIM 018` should carry that grade, not the abstract's.

⚠️ `cryptic` **0** occurrences — the alternative was never raised, let alone excluded.

---

### Item 4 — 🔴 THE LEAKINESS QUESTION, answered exactly

**What the paper asserts:** in the homozygote, **only the 504 bp product**. Twice, in two independent places:

- §3.4 (p. 423): *"In contrast, the homozygote ⟦family 3 / homozygote B⟧ of family 3 yielded **only the 504 bp
  band**"*
- Fig. 4C legend: *"The homozygote ⟦family 3 / homozygote B⟧ yielded **only the mutant 504 bp band**."*

**What I can see on the figure myself** (`media/image8.jpeg`, panel C; four lanes: a size marker, the family-3
homozygote B, the family-3 unaffected splice carrier, and a control; arrows annotate `593bp` and `504bp`):

- **Homozygote B: a single band**, at the lower (504 bp) level. **At the resolution at which this figure
  renders here, I see no band at the 593 bp level in that lane.**
- **Unaffected splice carrier: two bands**, upper aligned with the control band, lower aligned with the
  homozygote's band.
- **Control: one band**, at the upper (593 bp) level.

The gel is internally coherent and the band alignment supports the size assignments.

**🔴 What this is NOT, and this is the part that matters:**

| The question | The paper's answer |
|---|---|
| Is a WT product detectable in the homozygote? | **Not at the sensitivity of this gel.** |
| Was that absence **quantified**? | 🔴 **No.** `densitometry` **0**. No band-intensity ratio, no aberrant:normal fraction, no detection floor, no exposure series. |
| Replicates? A lane from the second family-3 homozygote? | 🔴 **No.** One lane, one individual, one gel. Family 3's homozygote A is absent (died in infancy). The family-1 homozygotes are absent from the gel entirely. |
| An assay able to find low-level correct splicing (allele-specific PCR, junction-specific qPCR, ddPCR, long-read, cloning)? | 🔴 **None.** |
| An NMD block, so that a degraded normal-or-aberrant fraction could be revealed? | 🔴 **No.** `cycloheximide` **0**, `puromycin` **0**; no inhibitor of any name appears in §2.4 or §2.5. |
| Does the paper claim residual correct splicing is absent? | It says *"only the 504 bp band"* — a **statement about what was seen on one gel**, not a claim of biological absence. `residual` **0**, `leaky` **0**. |

**🔵 INFERENZA — the decisive structural point about the quantitative assay.** The paper's one quantitative
measurement (§3.5, Item 6) amplifies **exons 8–9**, which lie **downstream of exon 6**. An exon-6-skipped
transcript **retains exons 8 and 9**. Therefore the exon-8–9 qPCR **cannot distinguish normally spliced from
exon-6-skipped WWOX mRNA**: it measures *total* WWOX transcript. **The ~10 % residual signal it reports in the
homozygote is NOT attributable to residual correct splicing** — and equally, **it is not evidence against it.**
The paper contains no assay whose readout is the aberrant:normal ratio.

> **Bottom line for `CLAIM 018` and for `TX-001`: this paper reports NO DETECTED residual correct splicing in a
> homozygote, by a qualitative gel, in blood, without an NMD block, in one individual, in one lane, without
> densitometry. It does not exclude leakiness. The distinction is the whole of the therapeutic question and the
> paper does not address it.**

---

### Item 5 — Which individuals show BOTH products? 🔴 The body and the figure disagree

✅ Hypothesis confirmed in the **body text**. 🔴 **But not shown in any figure, and the figure shows a
different set of people entirely.**

| Source | Who is said to show two bands |
|---|---|
| **§3.4 body text** (p. 423) | *"the **compound heterozygote** ⟦compound heterozygotes 1 and 2⟧ **of family 2**"* |
| **Fig. 4C legend + gel** | a **family 3** lane — see the labelling contradiction below |
| **§3.4 heading** | *"Complementary DNA analysis in **families 2 and 3**"* |
| **Fig. 4C legend opening** | *"cDNA analysis of the WWOX allele … **in family 3**"* |

🔴 **Two separate defects, both confirmed against the pedigree figure:**

1. **A lane is mislabelled.** The **Fig. 4C legend labels a lane as a compound heterozygote, while Fig. 1C
   prints that individual's genotype as `c.517-2A>G/WT`, a simple carrier.** The two-band pattern in that lane
   is exactly what a simple heterozygous carrier should give: one normal allele, one skipping allele.
2. **No family-2 lane exists.** The gel has four lanes — a size marker, the family-3 homozygote B, the
   family-3 unaffected splice carrier, and a control. **The §3.4 assertion about the family-2 compound
   heterozygotes is supported by no displayed data anywhere in the article**, and there is no supplementary
   material (`supplementary` **0**).

🔵 **INFERENZA:** the substantive biology is unaffected — a two-band pattern in a heterozygous carrier and in a
compound heterozygote are the same expectation, and the carrier lane demonstrates the assay resolves both
species. **But the sentence a LEGEND claim would want to cite — "the compound heterozygotes carrying Q230P in
trans show both products" — is a prose assertion with no shown gel.** Cite it as such.

---

### Item 6 — The qPCR, element by element

✅ **All five elements of the hypothesis CONFIRMED. Two internal defects found alongside them.**

**DATO** — §2.5 *"Quantitative real-time polymerase chain reactions"*, p. 420:

> "Total RNA from fresh blood was isolated using Trizol reagent (Ambion). cDNA was synthesized using random
> primers (qScript cDNA Synthesis Kit, Quanta). The qPCR was performed using the power SYBR Green PCR master
> MIX (Applied Biosystems) and run on the StepOnePlus (Applied Biosystems). The amplification was done with the
> following primers which amplified ex8-9: 5'CTTTCACCAAGTCCATGCAA3' and 5'CGTCTCTTCGCTCTGAGCTT3'.
> A total of 12 controls were compared to ⟦family 3 / homozygote B⟧ from family 3 in four different runs
> (4 different controls to each run). Every sample was analyzed in triplicate and gene expression was
> standardized against the GAPDH mRNA."

**DATO** — §3.5, p. 423:

> "Quantitative real time polymerase chain reaction (qPCR) was conducted to assess WWOX mRNA levels in
> ⟦family 3 / homozygote B⟧, family 3, and controls. qPCR analyses showed low level of WWOX mRNA expression in
> the patient compared to 12 controls (Fig. 4D). The results were analyzed by two tails T test and found to be
> highly significant (P = 0.0003)."

**DATO** — Fig. 4D legend:

> "(D) WWOX expression studies. The WWOX expression in ⟦family 3 / homozygote B⟧, family 3, measured with
> quantitative real-time PCR and standardized against GAPDH . The graph shows the normalized relative
> quantities values (Axis Y- ratio) of WWOX mRNA expression vs. a cohort of 12 controls. The bars indicate the
> average ratio of each group, asterisks denote a significant difference, as p = 0.0003 between the patient
> (Mean 1.08 ± 0.2) and the controls (Mean10.7 ± .1.8)."

| Element of the hypothesis | Verdict | Exact value |
|---|---|---|
| Assay is **exons 8–9** | ✅ | *"primers which amplified ex8-9"*, §2.5. Normaliser **GAPDH**. Chemistry **SYBR Green** (not a hydrolysis probe), platform StepOnePlus, **triplicate**. |
| Subject is **the homozygous splice patient** | ✅ | **Family 3 / homozygote B, `c.517-2A>G/c.517-2A>G`** per Fig. 1C. |
| **12 controls** | ✅ | *"A total of 12 controls"* (§2.5), *"compared to 12 controls"* (§3.5), *"a cohort of 12 controls"* (Fig. 4D). |
| **P = 0.0003** | ✅ | Stated three times. Test: *"an independent sample t-test (two tails)"* (§2.5); *"two tails T test"* (§3.5). |
| Fold / direction | ✅ **DECREASED, ≈ 9.9-fold** | Patient **1.08 ± 0.2** vs controls **10.7 ± 1.8**. `10.7 / 1.08 = 9.91`; the patient sits at **≈ 10.1 % of the control mean**. 🔴 **The paper never states a fold change** — only *"low level"*. The 9.9× is my arithmetic (`INFERENZA`) from the legend's means. |

**Quantification method, verbatim** (§2.5 → p. 421, Pfaffl-style efficiency-corrected ratio, rendered by the
extractor as): `ratio = Etarget^ΔCPtarget(control − sample) / Eref^ΔCPref(control − sample)`.

🔴 **Internal defect D-1 — the control count does not reconcile.** *"A total of 12 controls … four different
runs (4 different controls to each run)"*. **4 × 4 = 16, not 12.** Either three controls per run, or four runs
of four with overlap, or the total is wrong. Unresolvable from the text. **The headline `n = 12` is stated
three times and is the number to use; the run structure is uninterpretable.**

🔴 **Internal defect D-2 — the qPCR subject is misidentified in §3.5 and in the Fig. 4D legend.** Those two
places give a pedigree identifier that differs, by a transposition of the roman generation numeral, from the
one used in §3.4, in the Fig. 4C legend and in the Fig. 1C pedigree; the minority identifier corresponds to no
individual in that sibship. **Three concordant places identify the subject as family 3 / homozygote B, and that
is the reading to use.**

⚠️ **Three limits of the qPCR that a LEGEND claim must carry:**
- 🔵 **It is blind to the exon-6 junction** (see Item 4). It measures total WWOX, not correct splicing.
- 🔵 **One subject, no biological replicate at subject level.** *n* = 1 patient vs 12 controls; "triplicate" is
  technical. A two-tailed *t*-test with one observation in one arm is driven by the control variance;
  `P = 0.0003` is a statement about how far one value sits from a 12-point distribution, not about a difference
  between two sampled populations. **Report the effect, treat the *P* as descriptive.**
- 🔵 **Blood, no NMD block.** The interpretation is offered as a possibility, not a result: *"The decreased WWOX
  mRNA levels that were demonstrated in ⟦family 3 / homozygote B⟧ (Fig. 4D) **imply this might be attributed
  to** a nonsense-mediated mRNA decay (NMD) process affecting the mutated transcript"* (Discussion, p. 425).
  Note the double hedge — *imply* … *might be*.

> ⭐ **This means LEGEND's standing statement survives intact and is now confirmed at full-text depth:
> NO WWOX SPLICE ALLELE HAS EVER BEEN ASSAYED WITH AN NMD INHIBITOR.** This paper was the last candidate that
> could have falsified it. It does not. Earned zero: `cycloheximide` **0**, `puromycin` **0**.

---

### Item 7 — Q230P (`c.689A>C`, p.Gln230Pro): exactly who, and their clinical detail

✅ **CONFIRMED, and the count is exact.**

**How many distinct individuals carry `c.689A>C` in this paper: FOUR. All in family 2. None homozygous.**

| Role | Genotype | Status |
|---|---|---|
| **family 2 / compound heterozygote 1** | `c.517-2A>G/c.689A>C` | ✅ **affected** |
| **family 2 / compound heterozygote 2** | `c.517-2A>G/c.689A>C` | ✅ **affected** |
| **family 2 / unaffected Q230P carrier** (×2) | `c.689A>C/WT` | unaffected |

🔴 **ZERO Q230P homozygotes are reported in this paper.** The Q230P homozygotes LEGEND holds (Oliver 2023;
Banne 2021) come from **other** papers and must not be attributed here.

**DATO** — §3.2.2 (p. 422): *"a compound heterozygote state in the WWOX gene was identified and flagged due to
its clinical relevance. The identified variants included the splice-site c.517-2A>G variant and the novel
missense variant c.689A>C, p.Gln230Pro"* (the in-text call-out reads `(Fig. 2B)` — another **cross-reference
error**; the panel is `Fig. 4B`).

**DATO** — same §: *"The latter variant was found to be rare according to gnomAD, with an allele count of three
out of a total of 246,218 alleles in the general population and was assigned an 'Aggregated Predicted Severity
Score' of 0.75 out of 1, representing the fraction of prediction tools (13 tools in this case) that consider
the variant severe or the MetaLR score."*

**Family 2 — DATO, §3.1.2, p. 421, at family level:** family 2 comprises **eight members, of whom two are
affected and four are unaffected siblings**, and is **of mixed Yemenite, Moroccan and Kurdish Jewish ancestry**.

> ⭐ **`c.689A>C` is NOT the Yemenite founder allele — a property of the ALLELE, stated without reference to any
> line of descent.** The **1:177 carrier rate** (Item 9) is measured for **`c.517-2A>G` alone**, in 353 Yemenite
> Jewish samples. **The paper measures no population frequency for `c.689A>C` anywhere, and claims none.**
> `c.517-2A>G` is the only allele in this paper with a founder claim attached to it; the missense allele has
> none, and the 1:177 figure must never be carried over to it.

**Clinical detail of the two affected compound heterozygotes — DATO, §3.1.2, pp. 421–422:**

**Compound heterozygote 1** — born at term after an uneventful pregnancy. **Seizure onset at two weeks**:
*"tonic contractions with head and eye deviation"*.
**EEG: *"right fronto-central epileptic focal discharges"*.**
**MRI at seven months: *"demonstrated only thin CC"*** (corpus callosum). Extensive metabolic work-up normal.
*"Various antiepileptic drugs (AED) failed to control the seizures."*
At five months: truncal hypotonia with significant head lag, peripheral hypertonicity, normal deep tendon
reflexes. **At four years**: *"he did not acquire any developmental milestones, established no eye contact"*;
required **gastrostomy and tracheostomy** for feeding difficulty and repeated aspirations; **short stature and
acquired microcephaly**.
**Dysmorphism:** *"low anterior hairline, bushy eyebrows, long eyelashes, broad nasal bridge, short neck,
brachydactyly and tapering fingers"* (Fig. 3A–C).
**Survival: alive at last report.**

**Compound heterozygote 2** — born at term after an uneventful pregnancy, normal growth parameters.
**Seizure onset at three weeks**: *"tonic contractions accompanied with head and eye deviation that appeared in
clusters"*.
**EEG: *"multifocal bilateral epileptic activity, which transformed at the age of four months to a pattern of
modified hypsarrhythmia"*.**
🔴 **MRI: NOT PERFORMED** — the family declined. Metabolic investigation only *"partial"*.
At four months: dysmorphic features like the sibling's (Fig. 3D–F), lacking eye contact, truncal hypotonia with
peripheral hypertonicity, normal deep tendon reflexes.
**At three years: *"no developmental milestones were reached"*. Alive at last report.**
**No death is reported in family 2.**

🔵 **INFERENZA — the genotype–phenotype reading the paper itself offers.** The Discussion does **not**
distinguish the compound heterozygotes from the homozygotes clinically. It states the opposite:
*"The c.517-2A>G splice site variant described herein is associated with a severe developmental delay and,
accordingly, fits with the phenotypes that were previously observed in patients carrying two predicted null
alleles."* **So the paper treats Q230P-in-trans as phenotypically indistinguishable from homozygous null.**
🔴 **And it does so with no protein data at all:** `Western` **0**, `blot` **0**. **`CLAIM 030`'s
`PREMISE: DETECTION_FLOOR` is NOT resolved by this paper** — ask **A3** of the 2026-09-21 acquisition list
returns **empty**.

---

### Item 8 — Any other WWOX variants reported *by this paper*?

🔴 **NO. Exactly two, and both are novel to it.** `c.517-2A>G` and `c.689A>C` (p.Gln230Pro).

What the WES did turn up, and why it is not a third WWOX variant:
- **Family 1** — homozygosity mapping shortlisted three neuro genes (**`FA2H`, `KCTD7`, `WWOX`**);
  *"Sequencing of the FA2H and KCTD7 yielded no variants suspected to be pathogenic or likely pathogenic."*
  Shared LOH region ≈ **4.9 Mb**, **1,657 markers**, `chromosome 16:74085326–78980401`. Mean coverage **73×**.
- **Family 2** — significant shared variants in five genes; heterozygous variants in **`DNAH5`**, **`TGIF1`**,
  **`RYR1`**, and two homozygous variants in **`SARM1`**, all set aside as unrelated to the phenotype.
- **Family 3** — *"The homozygous WWOX splice-site c.517-2A>G variant described above was the only clinically
  relevant significant variant flagged in the exome"*. CMA found no CNV.

⚠️ **Table 1 (pp. 424–425) lists WWOX variants from EIGHT OTHER published series** — `c.131G>A p.W44*`,
`c.606-1G>A`, several 16q23.1 deletions, `c.1005G>A p.W335*`, `c.45_48delGGAC p.D16Sfs*63`, `c.140C>G p.P47R`,
`c.889A>T p.K297*`, `c.160G>T p.R54*`, `c.139C>A p.P47T`, `c.1114G>C p.G372R`. 🔴 **These are comparator
literature (Elsaadany 2016, Tabarki 2015, Valduga 2015, Ben-Salem 2015, Mignot 2015, Abdel-Salam 2014,
Mallaret 2014 / Gribaa 2007) and must NOT be attributed to PMID 30853297.** The table's own first column reads
*"This study"*, whose Mutations cell reads
*"F1/F3: homozygous c.517-2A>G · F2: comp. het. c.517-2A>G / c.689A>C; p.Q230P"*.

---

### Item 9 — The 1:177 carrier rate: denominator and ascertainment

✅ **CONFIRMED. Denominator = 353 individuals (706 chromosomes), 2 carriers.**

**DATO** — §2.3, p. 420 (ascertainment):

> "To calculate the carrier frequency of the novel WWOX c.517-2A>G splice-site variant, three different sets of
> individuals of Yemenite Jewish origin cumulatively available to the authors were screened. A total of 353
> (706 chromosomes) samples were either sequenced as described above or were subject to investigation by
> Restriction Fragment Length Polymorphism (RFLP)."

**DATO** — §3.3, p. 423 (result):

> "The prevalence of the c.517-2A>G splice-site variant among the general population according to the gnomAD
> database is 0 out of 245,866. However, this variant was detected in two out of the 353 (706 chromosomes)
> Yemenite Jewish control samples that were tested, establishing a carrier rate of 1:177 for this variant
> indicating a 95 % confidence interval of 0.0016–0.0204 for carrier frequency in this population, using the
> binomial exact confidence interval approach."

🔵 **INFERENZA — the point estimate checks out; the lower CI bound does not.**
- `2/353 = 0.00567` → `1 / 0.00567 = 176.5` → **1:177** ✅ reproduces exactly.
- Clopper–Pearson exact 95 % CI for 2/353, computed here: **0.00069 – 0.02032**.
- The paper's **upper bound 0.0204 matches** (0.02032). 🔴 **The paper's lower bound 0.0016 does NOT** — the
  exact lower limit is **0.00069**, a factor of 2.3 lower. **The stated interval is not reproducible under the
  method the paper names.** Recorded as an arithmetic discrepancy, not as a challenge to the point estimate.

🔴 **Ascertainment limits — all `INFERENZA`, because the paper states none of them:**
- **"cumulatively available to the authors"** is **convenience sampling** across three heterogeneous sets, not
  a population-random survey. **No recruitment period, no recruitment site, no inclusion criteria, no
  statement that the 353 are unrelated**, and **no statement that relatives of the three index families were
  excluded**. If any were included, the rate is upward-biased.
- **Two different assays** (Sanger and RFLP) with **no per-set breakdown** of how many by which, and **no
  analytical-sensitivity statement for the RFLP**.
- **"Yemenite Jewish origin"** is self-reported ancestry; the index families are explicitly *"full or partial"*,
  so the denominator's admixture structure is unstated.
- The rate is computed over **individuals** (`2/353`), which is correct for a carrier rate. The allele
  frequency would be `2/706 = 0.00283`. Both are stated; do not confuse them.

---

### Item 10 — The "first detailed description" claim, and the dysmorphism count

✅ **BOTH CONFIRMED. The "first" claim is made twice and is hedged the second time.**

**DATO** — Abstract, p. 418: *"We provide the first detailed description of patients harboring a splice-site
variant in the WWOX gene and propose that the clinical synopsis of WWOX related epileptic encephalopathy should
be broadened to include facial dysmorphism."*

**DATO** — Discussion, p. 425 (the hedged version, and the one to cite):

> "Although splice-site variants in WWOX are registered in ClinVar, to the best of our knowledge this is the
> first detailed report of patients harboring such variants in this gene."

**DATO** — Introduction, p. 418, the basis for the claim:

> "Although WWOX splice-site variants have been reported, there is no clinical report describing those patients
> and thus far only patients with missense, nonsense, frameshift, exon deletion, and gene deletion identified
> as part of a copy number variant have been described in details."

**Dysmorphism — 4 of 6. DATO, three concordant places:**
- Abstract: *"Importantly, four patients demonstrated facial dysmorphism."*
- Introduction: *"dysmorphism in four of the six patients"*
- Discussion, p. 425: *"Among the six patients described here, four exhibited distinct dysmorphic features. The
  common dysmorphic features described in families 1 and 2 were: long eyelashes, short neck, tapering fingers
  with brachydactyly and short stature. In addition, ⟦the family-1 homozygotes⟧ exhibit mild pectus carinatum
  and ⟦the family-2 compound heterozygotes⟧ exhibit broad nasal bridge, low anterior hairline and bushy
  eyebrows (Fig. 3)."*

**The four are the two family-1 homozygotes and the two family-2 compound heterozygotes.** 🔴 **The two family-3
`c.517-2A>G` homozygotes — the ones carrying the RNA data — are NOT among the dysmorphic four**, and §3.1.3
records no dysmorphic features for either. Photographs (Fig. 3) exist **only for the family-2 compound
heterozygotes**.

**The authors' own caveat, quoted because a LEGEND claim must carry it:**
> "While hypertrichosis could potentially be related to AED, and bi-temporal narrowing to microcephaly, long
> eyelashes, broad nasal bridge, brachydactyly, tapering fingers and short stature are features which are
> unlikely to be the byproduct of any drug treatment. We therefore suggest that the dysmorphic features
> presented could serve as additional clinical signs of WWOX related EIEE."

⚠️ *"facial dysmorphism"* in the abstract is looser than the finding: brachydactyly, tapering fingers, short
stature and pectus carinatum are **not facial**. Note also that this claim is the one **contradicted** by
Chong 2023 (PMID 36537114), per `ft125_chong2023_targeted_reread_20260921.md` D-2: *"In contrast, none of our
patients showed distinctive facial features."* The tension stands.

---

## 5 · 🔴 Where the preliminary and prior reads were WRONG, NARROWED, or CONFIRMED

### 5.1 · Against `analysis/splice_allele_rna_evidence_20260922.md`

| Line | Standing text | Verdict against the full text |
|---|---|---|
| **249** | *"What it reports is the presence of a skipped species. It reports **no fraction, no ratio, no residual normal band, and no statement that normal splicing was absent**."* | 🔴 **PARTLY CONTRADICTED — and this is the most consequential correction in this file.** (a) *"no residual normal band"* — **the paper DOES address it explicitly and twice**: *"yielded only the 504 bp band"* / *"only the mutant 504 bp band"*. (b) *"no statement that normal splicing was absent"* — **there IS such a statement**, at gel level. ✅ **What survives, and should replace the sentence:** no fraction, no ratio, **no densitometry, no replicate, no NMD block, and no assay capable of detecting low-level residual correct splicing.** The correct formulation is *"no detected residual normal band, by a qualitative single-lane gel"* — not *"no statement"*. |
| **174** | *"M-3 nevertheless **sequenced the skipped product**, so NMD is demonstrably not absolute for this allele."* | 🔴 **NARROWED on its warrant, CONFIRMED on its conclusion.** The Results section reports **band sizes**, not a sequence read; only §2.4's Methods names Sanger. So *"sequenced the skipped product"* overstates the published locator (see Item 3). **But the conclusion stands and is now stronger**: the 504 bp product is robustly **amplifiable from blood-derived RNA**, and §3.5 measures **≈ 10 % residual WWOX mRNA** in the homozygote. NMD is **not absolute** for this allele — now supported by a quantitative measurement rather than by inference from a band. 🔵 Add the caveat that the exon-8–9 assay cannot say what that 10 % *is*. |
| **M-3 row (45)** | *"patient material, tissue unstated in abstract"* · *"abstract-depth"* | ✅ **RESOLVED. Tissue = BLOOD** (§2.4 *"Total RNA was isolated from blood"*; §2.5 *"fresh blood"*). The depth annotation `abstract-depth` is now **superseded** — this is a full read. (Not edited; the file is not mine to change.) |
| **129 / 144** | Exon 6 = `c.517–c.605`, **89 nt**, `mod 3 = 2`, frameshifting. | ✅ **CONFIRMED THREE WAYS** — the paper's own *"89 bp deletion of exon six"*; `593 − 504 = 89`; and ClinVar coordinates 78,386,860–78,386,948 (GRCh38), which I re-derived here. Scientist A's and Scientist B's arithmetic were both right. 🔴 **With the caveat that the FRAMESHIFT is LEGEND's inference: the paper never states it.** |
| **149** | *"`c.517-2A>G` (exon 6) and `c.1057-2A>G` (exon 9) sit in opposite NMD regimes."* | ✅ **Untouched and now better anchored.** This paper's Discussion invokes NMD for the exon-6 allele (*"might be attributed to"*), which is the internal-exon regime. Nothing in it speaks to exon 9. |
| **73** | *"the census's standing statement — 'no WWOX splice allele has ever been assayed with an NMD inhibitor' — survives intact"* | ✅ **CONFIRMED AT FULL-TEXT DEPTH.** `cycloheximide` **0**, `puromycin` **0**. This was the last unread candidate that could have falsified it. It does not. |

### 5.2 · Against `analysis/ft117_pmid30853297_read_20260921.md`

| Item | Standing text | Verdict |
|---|---|---|
| **The central limit** | *"PMID 30853297 was NOT read. Task 2 was not performed."* | ✅ **DISCHARGED.** The paper is now read first-hand from a locally staged PDF + publisher figure pack. The retrievability analysis in §2 of that file remains a correct record of 2026-09-21; it is simply no longer the operative state. |
| **`N-33` / `S-1`** ⭐ | *"a published statement that WWOX RNA cannot be assessed in blood or skin fibroblasts"* — flagged as possibly invalidating the tissue choice in `DL-BIO-003`, `HYP-20260709-08` and Wave 3 §9 | 🔴 **CONTRADICTED AS A BLANKET STATEMENT, by direct measurement.** This paper **amplified WWOX cDNA across exon 6 from whole blood**, resolved **two** products on a gel in a carrier, and ran **exon-8–9 qPCR** with a control mean of **10.7** relative units. **WWOX transcript is detectable and measurable in blood.** ⚠️ The narrow version of S-1 may still hold — *adequacy of coverage for splice calling in a specific RNA-seq assay* is a different claim from *expression* — but **the tissue choice in `DL-BIO-003` is not invalidated, and blood now has a published precedent.** `fibroblast` **0** in this paper, so it says nothing either way about fibroblasts. |
| **Acquisition ask `A1`** | tissue? only product? any quantification? | ✅ **ANSWERED: blood; only product at gel level; the only quantification is the exon-8–9 qPCR, which is blind to the junction.** |
| **Acquisition ask `A2`** | NMD inhibitor used? | ✅ **ANSWERED: NO. Clean negative. The question is closed for this paper permanently.** |
| **Acquisition ask `A3`** | protein measurement on the Q230P compound heterozygotes? | 🔴 **ANSWERED: NONE.** `Western` **0**, `blot` **0**. **`CLAIM 030`'s `PREMISE: DETECTION_FLOOR` is NOT resolved here.** |
| **Acquisition ask `A4`** | family table with genotypes | ✅ **ANSWERED** — Item 1 table above, at role level. |
| **Acquisition ask `A5`** | recruitment period and ascertainment route | 🔴 **PARTLY ANSWERED, and the answer is thin.** Carrier screening is *"three different sets … cumulatively available to the authors"* — convenience. **No recruitment period is stated anywhere in the paper.** Molecular work-ups were done **independently and in parallel** (§2.1: *"The molecular investigations of the three families was conducted independently with the investigators unaware of their parallel efforts"*), which supports family independence but is not a recruitment window. |
| **§5, Banne overlap** | *"the two Yemenite compound heterozygotes in Banne are almost certainly the two from this target paper"* | ✅ **STRONGLY SUPPORTED and now specifiable: they are the two family-2 compound heterozygotes, `c.517-2A>G/c.689A>C`.** ⚠️ **With a correction to the ancestry label:** their Yemenite ancestry is **partial** — family 2 is of mixed Yemenite, Moroccan and Kurdish Jewish ancestry. Calling them "the two Yemenite compound heterozygotes" is a simplification the source does not make. **The standing warning against summing Q230P denominators across cohorts is reinforced, not relieved.** |
| **§5, are the four homozygotes re-reported elsewhere?** | unresolved | 🔴 **STILL UNRESOLVED.** Nothing in this paper's own text resolves it; it is a question for the other cohorts. |
| **`N-36`, hyphen deletion** | the defect was seen on a citing-corpus surface | ✅ **REPRODUCED ON THIS ARTEFACT'S OWN TEXT LAYER** — the abstract's instance extracts as `c.5172A>G`. The rule (never quote a coordinate from a lossy surface) is vindicated and was applied throughout § 3 above. |
| **`C-1`, the byline** | `PAPER 025` attributed to *"Piard et al."* with title ending *"…dysmorphic features"* | ✅ **CONFIRMED WRONG on both counts, first-hand** — § 2 above. Title ends *"…and dysmorphism among Yemenite Jews"*. |

---

## 6 · Internal defects of the source, collected

Recorded so a future reader does not spend the time twice. None of these changes the biology; all of them
change what may be cited and from where.

| # | Defect | Where |
|---|---|---|
| **D-1** 🔴 | *"12 controls … four different runs (4 different controls to each run)"* — **4 × 4 = 16 ≠ 12** | §2.5, p. 420 |
| **D-2** 🔴 | The qPCR subject is given **one pedigree identifier in §3.5 and the Fig. 4D legend and a different one** in §3.4, the Fig. 4C legend and the Fig. 1C pedigree — a transposition of the roman generation numeral; the minority identifier matches no individual in that sibship | §3.5, Fig. 4D |
| **D-3** 🔴 | **The Fig. 4C legend labels a lane as a compound heterozygote while Fig. 1C prints that individual's genotype as `c.517-2A>G/WT`, a simple carrier** | Fig. 4C legend |
| **D-4** 🔴 | §3.4 attributes the two-band result to the **family-2 compound heterozygotes**; the only gel shown is **family 3** (homozygote B, an unaffected splice carrier, and a control). **No family-2 lane exists and there is no supplementary material** | §3.4 vs Fig. 4C |
| **D-5** ⚠️ | **Fig. 2's legend assigns the two family-1 homozygotes to the two MRI panels in the opposite order from the body text.** The descriptive content (18 vs 33 months; mild vs moderate extra-ventricular dilatation) tracks the body, so the legend's identifiers are the transposed element | Fig. 2 legend vs §3.1.1 |
| **D-6** ⚠️ | Cross-reference errors: §3.2.1 cites `(Fig. 3A)` for a Sanger panel that is `Fig. 4A`; §3.2.2 cites `(Fig. 2B)` for a panel that is `Fig. 4B` | §3.2.1, §3.2.2 |
| **D-7** ⚠️ | The binomial-exact 95 % CI lower bound **0.0016** is not reproducible for 2/353 (Clopper–Pearson gives **0.00069**); the upper bound 0.0204 is correct | §3.3 |
| **D-8** ⚠️ | Abstract says *"facial dysmorphism"*; the features listed include brachydactyly, tapering fingers, short stature and pectus carinatum, which are not facial | Abstract vs Discussion |
| **D-9** 🔴 | **Abstract over-claims relative to Results**: *"Complementary DNA sequencing demonstrated … skipping of exon six"* against a Results section that reports band sizes and says *"consistent with the prediction"* | Abstract vs §3.4 |
| **D-10** ⚠️ | Reagent naming is inconsistent between the two RNA methods: **"Trisol"** in §2.4, **"Trizol"** in §2.5 | §2.4, §2.5 |

---

## 7 · What a future LEGEND claim may and may not say about this allele

| May say (`DATO`) | May **not** say |
|---|---|
| `c.517-2A>G` abolishes the intron-5 acceptor and yields an mRNA product **89 bp shorter** than wild type, in **blood-derived RNA**, by RT-PCR | that exon-6 skipping was **sequence-confirmed** in this paper (Results reports size + consistency-with-prediction, not a junction read) |
| In a **homozygote**, **only the 504 bp product was detected** on the published gel | that residual correct splicing is **absent** or **excluded** — no quantification, no replicate, no NMD block, no junction-level assay |
| In an **unaffected heterozygous carrier**, **both** 593 bp and 504 bp products are present | that the **compound heterozygotes** were **shown** to carry both products — asserted in prose, shown in no figure |
| **Total WWOX mRNA** (exons 8–9, GAPDH-normalised) in the homozygote is **≈ 10 % of a 12-control mean** (1.08 ± 0.2 vs 10.7 ± 1.8, *P* = 0.0003, two-tailed *t*) | that this quantifies **correct splicing** — the amplicon is downstream of exon 6 and detects the skipped transcript too |
| The authors **propose** NMD as an explanation (*"imply this might be attributed to"*) | that NMD was **demonstrated** — no translation block was used |
| **Carrier rate 1:177 (2/353) for `c.517-2A>G` among Yemenite Jews**, 95 % CI upper bound 0.0204 | that the sample was population-random or that relatedness to the index families was excluded; or that **1:177 applies to `c.689A>C`** — it does not, and no frequency is reported for that allele |
| **Four of six** affected had dysmorphic features; **neither family-3 homozygote is among them** | that dysmorphism is established for `c.517-2A>G` homozygotes generally — the two homozygotes carrying the RNA data are not among the dysmorphic four |
| **Zero Q230P homozygotes** are reported here; four individuals carry `c.689A>C`, two of them affected compound heterozygotes | anything about Q230P **protein** level or stability — **no protein assay of any kind** appears in this paper |

---

## 8 · What is still open after this read

| # | Open question | Why this paper cannot close it |
|---|---|---|
| **O-1** ⭐ | **Is `c.517-2A>G` leaky?** | The only gel is qualitative, single-lane, single-subject, undensitometered; the only quantitative assay is blind to the exon-6 junction. **A junction-specific / allele-specific measurement has never been made for this allele.** |
| **O-2** | **What fraction of the exon-6-skipped transcript is degraded?** | No NMD inhibitor. The ~10 % residual is total WWOX, undecomposed. |
| **O-3** | **Is the 504 bp product actually exon-5→exon-7?** | Not reported as a sequence. An 89-nt cryptic-acceptor product would be size-identical. `cryptic` **0**. |
| **O-4** | **WWOX protein where Q230P is present** | No Western, no antibody, no quantification. `CLAIM 030`'s detection-floor premise stands untouched. |
| **O-5** | **Do the four homozygotes appear in later series?** | Not answerable from within this paper. |
| **O-6** | **Fibroblast feasibility for `TX-001`** | This paper used **blood only**. The `S-1` worry is defeated for blood; **for fibroblasts it is neither confirmed nor refuted here.** |

🔵 **The one design consequence for `TX-001` / `DL-BIO-003`, stated plainly.** This paper is a **published
precedent that the exon-6 region of WWOX amplifies cleanly from whole-blood RNA and resolves the normal and
skipped species as distinct bands in a heterozygote.** That is a usable positive control and it lowers the
risk on the tissue axis. **But it is also the exact design LEGEND has already identified as insufficient** —
a qualitative gel with no NMD arm and a normaliser amplicon that sits downstream of the lesion. The planned
design (fragment-analysis peak areas → aberrant:normal ratio; junction qPCR against an exon 4–6 core
normaliser; ± cycloheximide with vehicle twins; Sanger of every band) is **exactly the set of things this
paper does not do**, and the read confirms rather than displaces it.

---

## 9 · Declaration

Author: **SCIENTIST-1**. Date: **2026-09-23**.
**READ-ONLY** toward every canonical file: no registry, no queue, no `current_*.md`, no ledger, no state
manifest, no commit candidate was created or amended. **No git operation was performed.** This file is the
single file written.

🔴 **No `FULLTEXT_READ_RECEIPT` was recorded.** The session brief scoped this node to a read plus this analysis
file and forbade ledger writes; recording a receipt is therefore left as an **outstanding operator action**
(`fulltext_receipts.py record`) and is named here so the omission is visible rather than silent.

🔴 **Public edition compliance.** No e-mail address, no contact detail, no institutional address, no name, no
date of birth. **Pedigree coordinates, transmission relationships and identifying clinical measurements have
been removed** — see § 0 for exactly what was taken out and what replaced it. Individuals appear only as role
labels attached to a genotype, and ancestry is stated at family level only.

**Not medical advice.**

**Surfaces read this session:** the locally staged full-text PDF (9 pp., sha256 above, all page footers
418–426 recovered) and the publisher figure pack (5 slides, 4 figure legends, Fig. 1 and Fig. 4 images viewed).
**No network call of any kind was made.** All zeros reported above are **earned zeros** from searches whose
positive controls returned non-zero, on this artefact, on 2026-09-23.

**DOI:** [10.1016/j.ejpn.2019.02.003](https://doi.org/10.1016/j.ejpn.2019.02.003) — **Weisz-Hubshman M,
Meirson H, … Behar DM, Heimer G.** *Eur J Paediatr Neurol* 2019;**23**(3):418–426. **PMID 30853297.**
**Not** Piard et al. (that is PMID 30356099, *Genet Med* 2019;21(7):1667–1671).
