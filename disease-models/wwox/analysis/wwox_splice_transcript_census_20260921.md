# WWOX splice-allele transcript census — and one read

**VERDICT — Yes, barely: four papers have measured a transcript from a WWOX splice-affecting allele, but only one of them is reachable here; it is a heterologous minigene showing exon skipping, with no NMD block, no quantification, no protein measurement and no correction arm — so the transcript consequence of the reference genotype's allele class is reported but essentially unquantified, and the acceptor-specific measurement that exists is behind a paywall.**

Scientist B · 2026-09-21 · READ-ONLY · no canonical file modified.

Source of all bibliographic records below: **PubMed**. DOI links are given per record.

---

## § 0 · What this document is and is not

§ 1 is a **census**. A census is a list of what exists, built from titles and abstracts. It is not evidence.
**An abstract is not a read.** Where the MEASURED column below rests on an abstract sentence alone, the
census records that a measurement is *reported*, not that LEGEND has seen it.

The census turns on one distinction, and it is the whole point of the exercise:

- **ANNOTATED** — a variant is called "splice-site" by position, by a diagnostic pipeline, or by a
  predictor (SpliceAI, Pangolin, MaxEntScan). This is a **prediction**. No RNA was looked at.
- **MEASURED** — RNA or cDNA from that allele was actually run: RT-PCR, minigene, cDNA sequencing,
  RNA-seq. A gel or a read count. This is an **observation**.

LEGEND's standing position before today was that it had never read a paper that measured a WWOX
splice allele's transcript. That position is now changed by one paper, and only one.

---

## § 1 · The census

Four queries, run verbatim as recorded in § 4. Total distinct records surfaced: 19 (Q1) + 0 (Q2) +
36 (Q3, of which 30 returned) + 4 (Q4, a strict subset of Q1). The splice-relevant set is small.
**The correct output here is a short list, and this is a short list.**

### 1a · Papers that MEASURED a transcript from a splice-affecting WWOX allele

These are the only four. All four concern a *cis* allele in the gene.

| PMID | Year | Journal | Senior author · affiliation | Chang lab? | Allele | MEASURED — how | Retrievable? tested how |
|---|---|---|---|---|---|---|---|
| **39101447** | 2024 | Mol Genet Genomic Med | Li Baoguang · Hebei Children's Hospital, Shijiazhuang, China | **Outside** | `c.172+1G>C` — canonical **donor**, intron 2 | **MEASURED** — minigene splicing assay in HEK293T, RT-PCR + Sanger sequencing of the spliced product | **YES — fetched PMC11298992, non-empty body, 21,833 bytes.** Read in § 2. [DOI](https://doi.org/10.1002/mgg3.2500) |
| 38407561 | 2024 | Am J Med Genet A | Takada Hidetoshi · Univ. of Tsukuba, Japan | Outside | `NM_016373.4:c.516+1G>A` — canonical **donor** | **MEASURED (reported)** — "WWOX mRNA sequencing using peripheral blood RNA"; **patient tissue** | **NO.** `get_copyright_status` returned `pmc_id: null`; there is no PMC handle to fetch, so no fetch was possible. Wiley, all rights reserved. [DOI](https://doi.org/10.1002/ajmg.a.63575) |
| 30853297 | 2019 | Eur J Paediatr Neurol | Heimer G. / Basel-Salmon L. · Sheba & Schneider, Israel | Outside | `c.517-2A>G` — canonical **ACCEPTOR** (+ `c.689A>C` p.Gln230Pro) | **MEASURED (reported)** — "Complementary DNA sequencing demonstrated…" | **NO.** `pmc_id: null`; no PMC handle, no fetch possible. Elsevier. [DOI](https://doi.org/10.1016/j.ejpn.2019.02.003) |
| 22071891 | 2011 | Eur J Hum Genet | Sinclair Andrew · Murdoch Childrens, Melbourne | Outside | multi-exon **genomic deletion** exons 6–8 — *not a splice-site allele* | MEASURED — "cDNA analysis confirmed … exon 5 being spliced directly onto exon 9" | **Tested and FAILED.** PMCID PMC3283189 resolved but `get_full_text_article` returned a **zero-length body**. Abstract only. [DOI](https://doi.org/10.1038/ejhg.2011.204) |

Row 4 is included because it is a real measurement of a WWOX transcript, and excluded from the
answer to DL-BIO-002 because a genomic multi-exon deletion is not a splice allele: nothing was asked
of the spliceosome that it could get wrong.

**Note the retrievability asymmetry.** `is_open_access: false` was returned for *every* one of these,
including the one that fetched cleanly. For PMID 39101447 the flag came back `false` with
`checked_sources: ["pubmed"]` — PMC was never consulted — and the body nonetheless retrieved in full.
For PMID 22071891 the flag came back from PMC itself and the PMCID resolved, and the body was empty.
**The flag carried no information in either direction. Only the fetch did.**

### 1b · Papers that merely ANNOTATED a splice-site allele — no RNA looked at

| PMID | Year | Journal | Senior author · affiliation | Chang lab? | Allele | Status | Retrievable? |
|---|---|---|---|---|---|---|---|
| 42721537 | 2026 | Seizure | Caraballo Roberto / Juanes Matias · Hosp. Garrahan, Buenos Aires | Outside | `NM_016373.4:c.107+1G>A` in **five patients**, proposed founder effect | **ANNOTATED ONLY.** NGS + ACMG. No transcript work in the abstract. | **NO.** `pmc_id: null`, Elsevier "All rights reserved". [DOI](https://doi.org/10.1016/j.seizure.2026.08.027) |
| 21983861 | 2011 | Med Oncol | Buyru Nur · Istanbul Univ. | Outside | "one base substitution at the intron 6 splice site (+1 G-A)" in breast tumour **DNA** | **ANNOTATED ONLY.** PCR + direct genomic sequencing. | Not tested — annotation-only, out of scope for Part 2. [DOI](https://doi.org/10.1007/s12032-011-0080-0) |

PMID 42721537 is worth flagging to the operator independently of this census: it is a **2026 cohort of
five patients sharing one canonical donor allele** — the largest single-allele WOREE cluster in the
census after PMID 26345274 — and nobody looked at their RNA.

### 1c · Measured WWOX transcripts, but not from a splice allele (context, not evidence)

The bulk of the "WWOX and splicing" literature is oncology, and it measures *aberrant* or *alternative*
transcripts arising from fragile-site instability, genomic deletion, or *trans*-acting splicing factors
— never from a patient's *cis* splice-site allele. Listed once, compactly, so the census is honest
about why it is short.

| PMID | Year | Senior author · affiliation | Chang lab? | What was measured |
|---|---|---|---|---|
| 11719429 | 2001 | Aldaz C.M. · MD Anderson, Smithville TX | Outside | RT-PCR: aberrant transcripts deleting exons 5–8 / 6–8 in carcinoma and myeloma lines |
| 11572989 | 2001 | Watson J.E. / Gabra H. · Edinburgh | Outside | internally deleted WWOX transcript from a primary ovarian tumour |
| 11896615 | 2002 | Frengen Eirik · Oslo | Outside | RT-PCR: two alternative WWOX transcripts in breast tumours |
| 14526170 | 2003 | Aldaz C.M. · MD Anderson | Outside | **Review** — aberrantly spliced WWOX mRNAs, dominant-negative hypothesis |
| 15870886 | 2005 | Gabra H. · Edinburgh / Imperial | Outside | RT-PCR of WWOX variant 1 vs variant 4 (lacks exons 6–8) in ovarian tumours |
| 16288044 | 2005 | Earp H.S. · UNC Chapel Hill | Outside | WwoxΔ5-8 splice variant used as a phosphorylation-resistant tool |
| 21586613 | 2011 | Karni Rotem · Hebrew Univ. | Outside | hnRNP A2/B1 (**trans**-acting) regulating WWOX splicing in glioblastoma |
| 32669614 | 2020 | Shukla Sanjeev · IISER Bhopal | Outside | HNRNPA2B1 knockout misregulates alternative splicing of MST1R, **WWOX**, CFLAR |
| 33688485 | 2021 | Roy Jagat Kumar · Banaras Hindu Univ. | Outside | RT-PCR/Southern: aberrant WWOX transcript deleting exons 6–8 in cervical carcinoma |
| 25650666 | 2015 | **Chang, Nan-Shan · NCKU, Tainan** | **INSIDE** | Alternative splicing of **TRAPPC6A**, not WWOX; WWOX handled as protein |
| 25595186 | 2015 | Richards Robert I. · Adelaide | Outside | **Review** — "Alternative splicing also accounts for a variety of aberrant transcripts" |
| 41661231 | 2026 | Kumar Singhal D. · ICMR-NICPR, Noida | Outside | RNA-seq meta-analysis; novel `WWOX_FUT1` fusion. Not a splice allele |
| 16007179 | 2005 | Richards Robert I. · Adelaide | Outside | *Drosophila* orthologue, irradiation sensitivity. No human transcript |
| 14614460 | 2003 | Smith David I. · Mayo | Outside | Parkin exon rearrangements; WWOX cited by analogy |

**Homonym and independence check.** Exactly **one** record in this entire census is inside the
Chang Nan-Shan laboratory (National Cheng Kung University, Tainan): PMID 25650666, whose last author
is Chang, Nan-Shan and whose first author Chang, Jean-Yun is of the same institute. Every other
"Chang" encountered is unrelated: Chen Zihan et al. (PMID 38902482, Xuzhou) is not a Chang at all,
and the "Chang et al." references cited *inside* PMID 39101447's discussion point to the NCKU lab as
a third-party citation, not as authorship. **The measured-transcript evidence in § 1a is therefore
entirely outside the Chang laboratory** — the four splice-allele measurements come from Hebei,
Tsukuba, Israel and Melbourne, four mutually independent groups.

### 1d · Census arithmetic

- Splice-relevant records assessed: **20** (14 context + 4 measured-on-allele + 2 annotated-only).
- Papers that **MEASURED** a transcript from a *cis* splice-affecting WWOX allele: **3**
  (PMIDs 39101447, 38407561, 30853297), plus 1 boundary case (22071891, genomic deletion).
- Papers that merely **ANNOTATED**: **2** (42721537, 21983861), covering **six patients**
  across two canonical alleles whose RNA was never examined.
- **Retrievable:** 1 of 4. Tested by fetching: **2** (PMC11298992 → 21,833 bytes; PMC3283189 →
  zero-length body). The other 2 (38407561, 30853297) returned `pmc_id: null`, so no fetch
  target existed; their unavailability is established by the absence of a PMC handle, not by a
  failed transfer, and I say so rather than claiming I tested them.
- Papers measuring a transcript from a canonical **ACCEPTOR** allele — the reference genotype's
  class: **exactly one, PMID 30853297, and it is unreachable here.**

---

## § 2 · The read — PMID 39101447

**You Y, Wu W, Du Y, Hu J, Li B. "Developmental epileptic encephalopathy caused by homozygosity of a
c.172+1G>C variant in the WWOX gene." Mol Genet Genomic Med 2024;12(8):e2500.**
According to PubMed. [DOI](https://doi.org/10.1002/mgg3.2500) · PMC11298992

Artefact: `/home/user/legend-development/files/fulltext/PMID39101447_PMC_MCPtext.txt`
Bytes: **21,833** · sha256: `0f9d97890975a6d1555cb90fe86251e20b3447c39db1bd36a38798438fea01e0`
Body only. The abstract arrived as a separate JSON field and is reproduced in § 2.6 below, not in the
artefact, because the artefact is fingerprinted.

### 2.0 · Instrument check, performed before relying on any count

The extractor's italic-deletion failure is **visibly active** in this artefact: the string `thegene`
occurs **9 times**, each one a place where the italicised gene symbol *WWOX* was deleted between
"the" and "gene". Sentences such as "In 2000, it was first reported thatis related to breast cancer"
and "the c.172+1G>C substitution ofcaused a splicing abnormality" have lost their subject or object.
`WWOX` survives as a bare string only **9 times**, all in roman-type contexts (figure legend, primer
names, one discussion sentence). **A count of "WWOX" in this file is an instrument reading, not a
measure of how often the paper names the gene.**

**HGVS tokens did survive.** `c.172+1G>C` appears **11 times** intact in the body and `c.[0-9]`
matches **12 times**. But the *title* was corrupted to "c.172+>C" — the `1G` vanished there. So HGVS
survives in body prose and fails in the title; counts drawn from the body are usable, the title is not.

**Roman-type method words — these zeros ARE informative:**
cycloheximide **0** · emetine **0** · SMG1/SMG1i **0** · puromycin **0** · actinomycin **0** ·
"nonsense-mediated" **0** · NMD **0** (word-boundary; the single substring hit was "NMDAR") ·
western **0** · blot **0** · immunoblot **0** · densitomet\* **0** · quantif\* **0** · percent **0** ·
antisense **0** · oligonucleotide **0** · ASO **0** (word-boundary; the five substring hits were
"ultrasound" ×4 and "basolateral") · rescue **0** · fibroblast **0** · lymphoblast **0**.
Present: minigene **16** · RT-PCR **3** (only with the U+2010 hyphen; the ASCII spelling scores 0,
which is an encoding artefact and not a negative) · Sanger **4**.

Per **D-14**: the paper's central result is stated in prose as well as in Figure 8, so it is
adjudicable. Anything visible only in the gel image of Figure 8b — in particular whether a faint
second band exists in either lane — is **not** adjudicable here, and I make no claim about it.

### 2.1 · Which variant, and what was measured — method, tissue, NMD inhibitor

**Variant:** `WWOX c.172+1G>C`, homozygous, arising through **maternal uniparental disomy of
chromosome 16**. It is a canonical **donor** (5′) site, not an acceptor:

> "this variation occurred in intron 2 of transcript, which destroyed the classical donor splice site."

> "A variation was found in intron 2 located in the first WW domain."

**Method — a heterologous minigene, not patient RNA.** The construct spans exons 1–3 with an
artificially shortened intron 1:

> "The Minigene plasmid was designed to insert the genome sequence region of exon 1 to exon 3 of thegene ()."

> "A shortened version of intron 1 was assembled consisting of the first 348 bp from the 5′ end of the intron in the first PCR product merged with the last 428 bp from the 3′ end of the intron in the second PCR product."

> "Wild‐type and variant minigene plasmids were transiently transfected into human embryonic kidney 293T cells (HEK293T) using Lipofectamine 2000 (Invitrogen, Carlsbad, CA, United States). After 48 h, total RNA was extracted from cells using TRIzol reagent"

> "reverse transcription‐PCR (RT‐PCR) amplification was performed. Sanger sequencing was conducted, and minigene transcription ofmRNA sequence was determined."

**Tissue: none from the patient.** The patient's blood was used for **DNA only** —

> "The child's peripheral venous blood (2 mL) was collected (EDTA anticoagulation), and genomic DNA was extracted"

— and the variant was confirmed by Sanger on genomic DNA. **No patient RNA, no fibroblast, no
lymphoblast, no brain.** The measured transcript is a plasmid transcript in an embryonic kidney cell
line. This is a real measurement and it is a weak proxy for the patient's neurons.

**NMD inhibitor: none, and none was possible.** Zero occurrences of cycloheximide, emetine, SMG1,
puromycin, actinomycin, "nonsense-mediated" or NMD. This matters exactly as the brief states: without
an NMD block, an absent transcript and a degraded transcript are indistinguishable. It matters *less*
than usual here for one structural reason worth recording — a minigene reports on the **spliceosome's
choice**, and the truncated construct (exons 1–3 only) has no downstream exon junction to trigger
NMD, so the assay is by design blind to degradation. **It tells us what the spliceosome does. It
tells us nothing whatsoever about how much of that product survives in a cell.**

### 2.2 · What the allele actually produced — the result, not the interpretation

**Exon 2 skipping.** Not intron retention. Not a cryptic site. Not "nothing detectable."

> "Minigene product sequencing demonstrated that the wild‐type minigene formed normal mRNA ern (Figure), but the c.172+1G>C substitution ofcaused a splicing abnormality, which abrogated the intron 2 canonical splice site and led to a loss of exon 2 (Figure)."

Repeated in the Figure 8 legend, which survived extraction:

> "Minigene product sequencing demonstrated that the wild‐type minigene formed normal mRNA (i), but the c.172+1G>C substitution of WWOX caused a splicing abnormality, which abrogated the intron 2 canonical splice site and led to a loss of exon2 (ii)."

("normal mRNA ern" in the body is an extraction artefact; the legend gives the clean sentence.)

The gel is described in prose as **one band per construct**, not two bands in one lane:

> "The gel‐electrophoresis of RT‐PCR revealed a band for wild‐type and another for mutant‐type, as shown in Figure."

I therefore record: **the paper reports no residual correctly-spliced product from the mutant
construct, and it also never states that there was none.** Whether a minor normal band is visible in
Figure 8b is a figure-only question and, per D-14, is not adjudicated here. **No intron retention and
no cryptic site are reported — but neither is explicitly excluded in prose, and a two-exon minigene
with a truncated intron is a poor instrument for detecting either.** Absence of a reported cryptic
site in this construct is not evidence of its absence at the endogenous locus.

### 2.3 · Was protein measured?

**No. Not at any point.** Zero occurrences of western, blot, immunoblot. The protein consequence is
**translated in software**, from the nucleotide sequence:

> "Finally, Snapgene software was used to translate nucleotide sequences into protein sequences, and the influence of variation on the protein translation process was analyzed."

The Conclusion nonetheless states:

> "A minigene assay used to confirm the variation site revealed that the variation resulted in protein truncation, further demonstrating the pathogenicity of the variation."

**A minigene assay cannot reveal protein truncation.** It reveals a spliced RNA; SnapGene then
predicts a reading frame. **This is an in-silico inference presented in the indicative as an assay
result.** Flagged. No WWOX protein from this allele — truncated, reduced or absent — was ever
observed by anyone in this paper.

### 2.4 · Was any quantification done?

**No. It is a qualitative gel plus Sanger sequencing.** Zero occurrences of densitomet\*, quantif\*,
percent, or any ratio. The entire quantitative content of the splicing result is the sentence quoted
in § 2.2: "revealed a band for wild‐type and another for mutant‐type." **There is no fraction, no
percentage aberrant, no aberrant:normal ratio, no replicate count, no statistic.**

This is the single most consequential gap for TX-001 and it is recorded as measured-absent, not
presumed: **the paper does not report how much correctly-spliced WWOX transcript the allele makes.**

### 2.5 · Is there any rescue or correction arm?

**No.** Zero occurrences of antisense, oligonucleotide, ASO (word-boundary), or rescue. There is no
splice-switching arm, no small molecule, no minigene repair construct. The only restoration language
in the paper is a **citation to third-party rodent work**, not an experiment performed here:

> "Repudi, Kustanovich, et al. () confirmed that the knockdown of thegene in rodents could lead to intractable epilepsy in mice, and restoration ofexpression could reduce brain excitability and seizures."

> "The reintroduction ofprevented these changes to a certain extent. Gene therapy is still undergoing animal testing and has not been used in clinical settings."

That is *Wwox* re-expression in rodents, cited. It is not splice correction, and it is not this
paper's data.

### 2.6 · Abstract-versus-results, and the grammatical mood of the central claims

**There IS a divergence. It is not large, but it is real, and it runs in the direction the brief
warned about — in-silico and speculative content re-voiced in the indicative as finding.**

The abstract (from the separate JSON field, reproduced here and not in the artefact) states:

> "Further minigene assay confirmed that the variation site affected splicing, causing protein truncation and affecting its function."

> "Clinical phenotype and minigene results suggest thatgene homozygous variation c.172+1G>C can cause severe DEE. We also concluded that vigabatrin can effectively treat seizures."

Set against Results and Methods:

1. **"affected splicing"** — supported. This is the one claim the assay actually measured, it is
   stated in the indicative, and the indicative is earned. No divergence.
2. **"causing protein truncation"** — **NOT measured.** Methods say SnapGene translated the sequence
   (§ 2.3). The abstract's participle asserts it as an observed consequence of the assay. The
   Discussion repeats the elision: "According to our minigene results, thegene variation, in our case,
   was a splicing variation that caused protein truncation." **An in-silico translation voiced as an
   assay finding.**
3. **"and affecting its function"** — **no functional assay of any kind was performed.** Not
   oxidoreductase activity, not binding, not localisation, not cell phenotype. This is the sharpest
   overreach in the paper: an unmeasured claim in the indicative mood, in the abstract.
4. **"We also concluded that vigabatrin can effectively treat seizures."** — In the **Discussion**
   this is correctly hedged in the conditional: *"suggesting that vigabatrin **may** be an effective
   management option."* In the **abstract** the hedge is dropped and it becomes "concluded … can
   effectively treat." This is an n-of-1 under concurrent levetiracetam, phenobarbital and
   topiramate, with no control and no withdrawal. **A speculation promoted to a conclusion by mood
   change between Discussion and abstract.** This is precisely the failure mode named twice today,
   caught here in a third instance, and LEGEND must not re-voice it: this paper is not evidence that
   vigabatrin works in WOREE.

Other properly-hedged Discussion language that must **not** be promoted if this paper is ever cited:
"This **may** be becauseaffects lipid metabolism and damages the integrity of the myelin sheath";
"gene variation **could** cause central nervous system and peripheral nerve injury."

**Summary of 2.6:** the splicing result itself survives scrutiny and is reported honestly. The
protein-truncation, function and vigabatrin claims do not; two of them are in-silico or absent, and
one is a mood upgrade between sections. **Take the exon-skipping. Leave the rest.**

---

## § 3 · What DL-BIO-002 and TX-001 may now assume, and what remains unmeasured

### 3.1 · Newly measured — DL-BIO-002 may now rest on this

- **A canonical WWOX splice-site allele has been shown, by direct sequencing of its spliced product,
  to cause exon skipping.** For `c.172+1G>C` (donor, intron 2) the product is a transcript lacking
  exon 2, in a HEK293T minigene (PMID 39101447, read in full). This is the **first measured WWOX
  splice-allele transcript in this repository's possession.** It is an observation, not a prediction.
- **Exon skipping is the only outcome reported for any WWOX splice allele in the reachable
  literature.** Across all four measurements in § 1a — c.172+1G>C → loss of exon 2 (read),
  c.516+1G>A → exon 5 deleted (abstract only), c.517-2A>G → skipping of exon 6 (abstract only),
  exons 6–8 genomic deletion → exon 5 joined to exon 9 (abstract only) — **every reported product is
  an exon-skip.** No WWOX paper in this census reports intron retention or a cryptic splice site.
- **A canonical ACCEPTOR allele has been measured once**, and it produced exon skipping:
  `c.517-2A>G` → skipping of exon 6 (PMID 30853297). This is the closest published analogue to the
  reference genotype's allele class. **LEGEND must record it as reported-measured-but-unread**: the
  paper is not retrievable here and the statement is an abstract sentence. It is census, not evidence.
- **Independence is good.** The four measurements come from four mutually independent groups in four
  countries, and **none is inside the Chang Nan-Shan laboratory.** This is not a single-lab result.

### 3.2 · Still unmeasured — neither DL-BIO-002 nor TX-001 may assume any of this

- **No WWOX splice allele has ever been assayed with an NMD inhibitor.** Cycloheximide, emetine and
  SMG1i are absent from the entire census. Consequently **the fraction of aberrant WWOX transcript
  that survives versus is degraded is unknown for every allele, including the reference genotype's.**
  An exon-skipped transcript that is 95% degraded and one that is stable and dominant-negative are,
  on this evidence, the same observation.
- **No quantification exists anywhere.** Not one paper in the census reports an aberrant:normal
  transcript ratio for a WWOX splice allele. The read paper is a qualitative gel (§ 2.4).
  **TX-001's efficacy endpoint — "fraction of correctly spliced transcript" — currently has no
  measured baseline in any WWOX allele in any tissue.** There is no denominator to improve on.
  This is the single largest hole the session found.
- **No protein has ever been measured from a WWOX splice allele.** The truncated product is an
  in-silico translation (§ 2.3). Whether these alleles yield a truncated protein, a destabilised one,
  or nothing at all is **predicted, never observed.** DL-BIO-002's protein half of the question is
  wholly unanswered.
- **No splice-correction arm exists in the WWOX literature.** Zero ASO, antisense, oligonucleotide or
  minigene-repair experiments across the whole census. **TX-001 has no in-gene precedent whatsoever**;
  its entire rationale remains cross-gene transfer plus in-silico prediction. That is not a reason to
  drop it, and it is a reason not to describe it as supported by WWOX data.
- **Endogenous-context data are almost absent.** The one measurement LEGEND has actually read is a
  two-exon minigene with an artificially shortened intron, in embryonic kidney cells. It cannot report
  on cryptic sites elsewhere in the endogenous locus, on tissue-specific splicing, on neuronal
  context, or on transcript stability. **The only patient-tissue measurement in the census
  (PMID 38407561, peripheral blood RNA) is unreachable.**
- **The reference genotype's own splice allele has not been measured by anyone.** Nothing in this
  census substitutes for measuring it. The in-silico status of DL-BIO-002 for *that specific allele*
  is unchanged; what changed is that the allele *class* now has an empirical precedent.

### 3.3 · The tractable move this census exposes

Three facts now sit adjacent, and they were not adjacent before today:

1. A group in Genoa (PMID 35573960, read today) **holds WOREE patient fibroblasts and already runs
   RT-PCR on WWOX transcripts.** The assay exists, in the right cells, in the field.
2. **No one has ever run that assay on a WWOX splice allele with an NMD block and a quantified
   aberrant:normal ratio.** The gap is not technical difficulty; it is that nobody has done it.
3. There is a **2026 Argentine cohort of five patients sharing one canonical donor allele**
   (`c.107+1G>A`, PMID 42721537) and a **2015 cohort of five patients homozygous for a canonical
   acceptor allele** (`c.606-1G>A`, PMID 26345274) — **ten patients across two alleles whose RNA has
   never been examined.**

The concrete ask that follows is small, specific and cheap: **patient fibroblast RT-PCR across the
splice junction, ± cycloheximide, with band quantification.** That single experiment would convert
DL-BIO-002 from in-silico to measured and would give TX-001 its missing baseline denominator. This is
a collaboration ask, not a LEGEND experiment, and it is recorded here as a lead, not a plan.

---

## § 4 · Provenance, method and declared limits

**Author:** Scientist B. **Date:** 2026-09-21. **Mode:** READ-ONLY.
**No canonical file was modified.** No registry, queue, ledger or current file was touched. No git
command was run. No commit candidate was produced. The only file written outside this analysis
document is the full-text artefact `files/fulltext/PMID39101447_PMC_MCPtext.txt`.

### Queries actually run, verbatim

Via `mcp__PubMed__search_articles`:

1. `WWOX AND (splicing OR "splice site" OR "exon skipping")` — 19 results, all 19 returned.
2. `WWOX AND ("aberrant transcript" OR "intron retention" OR "cryptic splice" OR "aberrant splicing")` — **0 results.**
3. `WWOX AND (RT-PCR OR "transcript analysis" OR cDNA) AND (patient OR fibroblast OR lymphoblast)` — 36 results, 30 returned.
4. `WWOX AND (WOREE OR "epileptic encephalopathy" OR SCAR12) AND (splice OR splicing)` — 4 results, all returned; a strict subset of query 1.

Four queries. No citation-network chasing, no expansion into WWOX-and-cancer generally, no further
iterations.

### Retrievability tests actually performed

- `mcp__PubMed__get_copyright_status` in one batch of 5: PMIDs 39101447, 38407561, 30853297,
  22071891, 42721537.
- `mcp__PubMed__get_full_text_article` on **PMC11298992** → non-empty body, 21,833 bytes written.
- `mcp__PubMed__get_full_text_article` on **PMC3283189** → **resolved, zero-length body.**
- PMIDs 38407561, 30853297 and 42721537 returned `pmc_id: null`, so no fetch target existed and
  **no fetch was attempted**; I do not claim to have tested them by transfer.
- `mcp__PubMed__get_article_metadata` on 25 PMIDs across three batches.

### Declared limits

1. **This is a census plus one read.** Nineteen of the twenty splice-relevant records were assessed
   from title and abstract only. **An abstract is not a read.** Every MEASURED verdict in § 1a other
   than PMID 39101447 rests on an abstract sentence and is marked as reported, not verified.
2. **Query 2 returned zero.** The absence of "intron retention" and "cryptic splice" from the WWOX
   literature is therefore a **search-term result**, and only weak evidence that no such finding
   exists under other wording. It is consistent with § 3.1's exon-skipping pattern; it does not
   prove it.
3. **The one paper read is a heterologous minigene**, not patient tissue, not brain, not a full-length
   construct. Its generalisation to the endogenous locus is an assumption, and I have marked it as one.
4. **The extractor's italic-deletion fault was confirmed active** in this artefact (`thegene` ×9), so
   every string count in § 2.0 is labelled by class: HGVS tokens survived in the body and failed in
   the title; roman-type method-word zeros are informative; the bare `WWOX` count is an instrument
   reading and is not treated as a negative.
5. **Per D-14, no negative asserted only by a figure is adjudicated.** Figure 8b is a gel image; its
   band pattern beyond the prose sentence quoted in § 2.2 is not inspectable and no claim is made
   about it.
6. **Nothing here is medical advice.** The vigabatrin claim in PMID 39101447 is explicitly flagged in
   § 2.6 as an unhedged n-of-1 conclusion under polypharmacy and must not be carried forward as
   therapeutic evidence.

Bibliographic source: **PubMed**. All DOIs are linked at their first citation in § 1.
