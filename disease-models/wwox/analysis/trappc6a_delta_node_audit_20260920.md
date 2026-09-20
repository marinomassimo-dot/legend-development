# TRAPPC6AΔ node audit — does the first mechanistic node of the Chang/NCKU chain exist as claimed?

**Date:** 2026-09-20 · Scientist A, batch `SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION`
**Status:** non-canonical analysis. No canonical file read-modified, no commit candidate produced,
no therapeutic extrapolation drawn.

**Target:** Chang JY, Chang NS *et al.* 2015, *Oncotarget* 6(6):3578–89 —
"Trafficking protein particle complex 6A delta (TRAPPC6AΔ) is an extracellular plaque-forming
protein in the brain." **PMID 25650666**, PMCID PMC4414138.
Source: retrieved from **PubMed** / PMC open access. DOI: [10.18632/oncotarget.2876](https://doi.org/10.18632/oncotarget.2876)

---

## 0 · Read-depth declaration — honest

**What I read.** The complete PMC open-access deposit of PMID 25650666, end to end: Abstract,
Introduction, all five Results sections, the full Discussion, all of Materials and Methods
(including the cloning, mutagenesis, antibody-production, filter-retardation and knockout-mouse
subsections), and the **full legends of Figures 1–6**. Legend text is the single richest source in
this paper and I have used it heavily; every quote below is from that deposit.

**What I could not read, and therefore do not claim.**

| Not obtained | Consequence |
|---|---|
| **Any figure panel image.** There are no figure files in the extraction and no PDF tooling in this deployment. | I have **not inspected a single blot, gel, micrograph or dot-blot**. Wherever an answer needs a panel, I mark it UNRESOLVED and say so. I make no statement about band sharpness, background, staining pattern or plaque morphology. |
| **Supplementary Figures.** The deposit ends with a bare heading `SUPPLEMENTARY FIGURES` and no content. | The Results say "Data are provided to show the production of our homemade antibodies ()" and "the validity and protein aggregation are shown under various experimental conditions ()" — those pointers are to supplementary material I could not open. **The antibody-validation evidence may be richer than the main text states, and I cannot exclude that.** This is the single largest caveat on Question 2. |
| **Reference list and all in-text citation markers.** The PMC extraction strips reference markers, leaving bare `[]` and `[–]`. | I cannot say *which* prior paper any self-citation points to. Where the text cites itself for the TIAF1 results, I treat that as unverified. |
| **GenBank accession numbers.** The extraction strips them — the text reads "(Genbank accession)" three times with the number removed. | I can confirm accessions were **cited**, but I cannot read them or verify the deposited sequence. |
| **Figure callouts.** Stripped to bare `(Figure)`. | I often cannot tell which panel a sentence refers to. Where panel attribution matters I say the attribution is indeterminate. |
| **Gene symbols italicised in the original.** The extraction deletes italicised gene names mid-sentence, leaving e.g. "Human gene is involved in nonverbal reasoning". | I reconstruct the intended symbol from context and flag it when I do. |

**Nothing below rests on a figure panel.** Everything rests on running text or legend text, quoted.

---

## 1 · Question 1 — How was the isoform's existence established?

**Answer: by subtraction-cDNA-library cloning from a non-neural cell line, plus two in-silico splice
predictions, plus an EST-database count — and at the protein level by nothing but the lab's own
peptide antisera. There is no mass spectrometry anywhere in the paper, and no RT-PCR of the Δ
transcript from any tissue, including brain.**

### 1a · The cDNA — cloned, from monocytes, under TGF-β1

> "TPC6AΔ was originally isolated from TGF-β1-treated monocytic U937 cells in a subtraction cDNA
> library screen." — PMID 25650666, Results

> "We constructed a cDNA library by treating human monocytic U937 cells with TGF-β1. The TPC6AΔ
> cDNA was isolated from this library (with deletion at amino acids #29–42; GenBank accession)."
> — PMID 25650666, Methods, *Isolation of TPC6AΔ cDNA and construction of full-length TPC6A*

Two things follow, and they cut in opposite directions.

- **In favour:** a cDNA clone with a GenBank accession is a real molecular object, not a prediction.
  The accession is cited (I cannot read it — stripped).
- **Against:** the source tissue is **human monocytic U937 cells stimulated with TGF-β1**. The paper
  never isolates the Δ cDNA, or any Δ transcript, **from brain**. Every pathological claim in this
  paper is about brain.

Note also *what* the Methods say was sequence-verified. The only explicit sequencing step in that
subsection is the last sentence, and it belongs to the **reconstructed wild-type** clone, not to the
Δ clone:

> "The PCR product was digested with DpnI (New England BioLabs) at 37°C for 3 hr to remove the
> original templates, and the amplified cDNA was transformed to Top 10 (Invitrogen). Positive clones
> were isolated and identified by sequencing analysis." — PMID 25650666, Methods

Read in context, that sentence is the end of the **full-length TPC6A construction** protocol (insert
the missing 42 bases back into the Δ cDNA). The paper therefore documents sequence verification of
the *wild-type construct it built* more explicitly than of the *Δ clone it discovered*. The Δ clone's
sequence is asserted via an accession I cannot read. I mark this **as a gap in the reported text,
not as evidence of absence.**

### 1b · The deletion is genomic — ruled out, properly

This is the strongest experiment in the paper on this question, and it is a negative one done at
scale:

> "Thirty hippocampal samples, including 12 controls and 18 AD patients from postmortem Caucasians,
> were examined. None of the genomic DNA samples were deleted in the exon 1 of human gene (Figure).
> Similar results were observed by examining 50 genomic DNA samples in a random Asian population in
> Taiwan (data not shown)." — PMID 25650666, Results

80 genomic DNA samples across two populations, with primers and amplicon fully specified in Methods
(213 bp amplicon, forward 5′-GTTTCTTCACACGGAGATGG in exon 1, reverse 5′-CCACTTTCCAAAGGAGGAAG in
intron 1–2). This correctly excludes the trivial alternative that TPC6AΔ is a genomic deletion allele.
Caveat: 50 of the 80 are "(data not shown)".

### 1c · The splice event itself — predicted in silico, counted in ESTs, never RT-PCR'd

> "Computational analyses using 1,400 genomic sequences starting from the CDS sequence on exon 1
> were performed [,]. Results from 2 different web-based tools (NNSplice and NetGene) all predicted
> that the nt position 85 can be used as an alternative 5′ donor site to initiate splicing and leads
> to a 42-bp deletion on exon 1 sequence. Additional evidence from EST database searching showed
> that 13 TPC6A cDNAs out of 55 in total in humans are with the 42-bp deletion."
> — PMID 25650666, Results

This is the **only genuinely third-party evidence in the entire paper**. The EST entries in GenBank
were deposited by other groups; 13/55 (24%) is not a trace-level event. It is the reason my verdict
is not "poorly evidenced" at the transcript level.

But note precisely what it is *not*. It is a database count, not an experiment performed here. And
the substitution is explicit in the text's own logic: the paper says it set out to test the splicing
hypothesis —

> "Based upon the aforementioned observations, we determined whether mRNA undergoes alternative
> splicing." — PMID 25650666, Results

— and then satisfies that determination with **prediction software and a database query**, not with
RT-PCR across the junction, not with RACE, not with a Northern blot, and not in brain. A junction-
spanning RT-PCR on hippocampal RNA would have been a two-day experiment using the same post-mortem
collection they already had in hand (they extracted genomic DNA from it, §1b). It was not done, or
not reported.

### 1d · The protein — antibody band only

> "Proteins corresponding to wild type TPC6A and TPC6AΔ are shown in cells (Figure), which supports
> the occurrence of alternative splicing of mRNA." — PMID 25650666, Results

> "By Western blotting, the 20-kDa wild type protein was identified by the specific antibody
> (duplicate loading; Figure). Antibodies against TPC6AΔ and its phosphorylated form probed the
> 17-kDa TPC6AΔ and polymerized pS35-TPC6AΔ, respectively, in the neuroblastoma SK-N-SH cells
> (Figure)." — PMID 25650666, Results

A 20-kDa band and a 17-kDa band, discriminated by two homemade rabbit antisera. That is the entire
protein-level case for the endogenous Δ isoform. **The words "mass spectrometry", "MS", "LC-MS",
"proteomic", "immunoprecipitation" and "Edman" do not occur anywhere in this paper.** I checked the
full deposit.

**Finding 1.** Transcript: cloned cDNA + 24% EST support + two concordant splice predictors +
genomic deletion excluded in 80 samples → the *transcript* is plausibly real. Protein: an antibody
band and nothing else → the *protein* is asserted, not demonstrated. And the brain — the tissue the
whole downstream chain is about — has **neither** a transcript demonstration nor a non-antibody
protein demonstration.

---

## 2 · Question 2 — Were the anti-TPC6AΔ and anti-pSer35 antibodies validated against a genetic negative control?

**Answer: No. Peptide blocking only, explicitly and exclusively. And the Δ-specific epitope is
structurally ill-suited to the job it is asked to do.**

### 2a · The validation actually performed

> "Specificity of the antisera was tested using the synthetic peptides to block immunostaining."
> — PMID 25650666, Methods, *Antibodies and antibody production in rabbits*

That is the complete validation statement in Methods. It is echoed in Results:

> "Our antibody is specific, as each immunizing peptide blocked the corresponding immunoreactivity
> (Figure)." — PMID 25650666, Results

and in the Figure 2 legend:

> "In controls, immunizing peptides were used to block the immunoreactivity. Also, in negative
> controls (see D), no primary antibodies were used in the IHC." — PMID 25650666, Figure 2 legend

Both named controls are the two weakest available. Peptide blocking demonstrates that the antiserum
binds its immunising peptide — which is guaranteed by construction, since the animal was immunised
with it. Secondary-only controls demonstrate that the secondary antibody is not the source of the
signal. **Neither control can distinguish the target protein from any other protein in the tissue
that the antiserum happens to bind.** The statement "our antibody is specific, as each immunizing
peptide blocked the corresponding immunoreactivity" is a non-sequitur: peptide competition and
off-target tissue binding are fully compatible.

### 2b · The genetic negative controls existed in this lab and were not used for this

This is the sharpest point in the section. The paper has, in hand, in the same figures:

- a **`Wwox` knockout mouse** (Figure 5) — wrong gene, so not a control for TPC6A antibodies, but it
  establishes the lab's access to targeting technology;
- a **TPC6A siRNA construct**, used in Figure 6:

> "COS7 cells were transfected with expression plasmid constructs for EYFP-TPC6AΔ, EYFP-TIAF1, or
> EYFP, in the presence of one of the siRNA-expressing constructs, including scramble, WOX1si,
> TIAF1si and TPC6Asi." — PMID 25650666, Figure 6 legend

**`TPC6Asi` exists and is deployed in this paper — but as a perturbation in an aggregation-counting
assay on overexpressed EYFP fusions, never as a validation control showing that the 17-kDa band or
the plaque staining disappears.** A single panel — `TPC6Asi` or a Δ-junction-targeted siRNA, then
blot with the anti-TPC6AΔ antiserum, showing the 17-kDa band collapse — would have converted the
antibody from asserted to validated. It is not in the main text or its legends. (It could conceivably
be in the unreadable Supplementary Figures; see §0. I flag this as the one place where my read depth
could be wrong, and I do not claim it is absent — I claim **it is not reported in the readable text**.)

### 2c · The Δ-specific epitope shares 10 of 15 residues with wild-type TPC6A — derived, not quoted

The paper gives all four immunising peptides and the exact boundaries of the deletion. Putting them
together yields a finding the paper does not state.

> "Four TPC6A or TPC6AΔ peptides were synthesized (Figure): 1) KDLWVAVFQKQMDSLR, amino acid #84–100
> for pan-specific antibody production; 2) DPGPGGQKMSLSVLE, amino acid #24–38 for antibody against
> TPC6AΔ; 3) DPGPGGQKMSLVLE, amino acid #24–38 with phosphorylation at Ser35 for antibody against
> p-TPC6AΔ; 4) VSAGLRGEEAGATK, amino acid #29–42 for antibody against wild type TPC6A."
> — PMID 25650666, Methods

> "The deduced protein possesses an internal frame deletion of amino acids #29–42 at the-terminus"
> — PMID 25650666, Results

> "The possibly deleted region in chromosome 19q13.32 is
> 5′-GTGAGCGCCGGGCTCCGTGGGGAGGAAGCGGGGGCCACCAAG, encoding amino acid #29–42 in the wild type TPC6A."
> — PMID 25650666, Methods

Translating that 42-mer gives **VSAGLRGEEAGATK**, which is exactly peptide 4. So the internal
arithmetic is consistent, and the wild-type-specific antibody is well designed: its epitope is the
deleted segment itself, present in WT and absent in Δ. **That antibody can discriminate.**

The Δ-specific antibody cannot be reasoned about the same way. In Δ numbering, residues 29 onward
correspond to wild-type residues 43 onward (offset 14). The Δ immunising peptide
`DPGPGGQKMSLSVLE` (Δ #24–38) therefore decomposes as:

| Δ residues | Sequence | Status in wild-type TPC6A |
|---|---|---|
| 24–28 | `DPGPG` | present (WT 24–28) |
| 29–38 | `GQKMSLSVLE` | **present** (WT 43–52) |

**Ten of the fifteen residues — a contiguous 10-mer — are present, in that order, in wild-type
TPC6A.** Only the junction point itself is novel, and a polyclonal serum raised against a 15-mer
will predominantly recognise sub-epitopes, most of which are shared. A junction-spanning peptide
antigen is the standard way to raise an isoform antibody, but it is also the case that such an
antiserum routinely cross-reacts with the parent protein, which is why a genetic negative control is
not optional for this class of reagent — it is the only control that works.

And peptide blocking cannot rescue it: the competing peptide contains the shared 10-mer, so it would
block a cross-reactive wild-type signal exactly as efficiently as a true Δ signal.

**I mark this a DERIVED finding, confidence HIGH on the arithmetic (it follows from three quotes in
the paper) and MEDIUM on the immunological consequence (I cannot see the blots and cannot know how
the serum behaves).**

### 2d · Minor numbering irregularities in the peptide table

Recorded for completeness, both low-weight, both possibly extraction artefacts:

- Peptide 1, `KDLWVAVFQKQMDSLR`, is **16 residues** but is labelled "amino acid #84–100", a
  **17-residue** span. Off by one.
- Peptide 3, `DPGPGGQKMSLVLE`, is **14 residues** and is labelled with the same "#24–38" span as
  peptide 2, which is 15 residues. The missing residue is precisely the serine at position 35. This
  is almost certainly the phospho-markup `(pS)` being stripped by the PMC extraction (§0), **so I do
  not count it as a paper error.** I record it only so a later reader with the typeset PDF can check.

### 2e · Consequence for the human post-mortem plaque data

Direct, and it is the reason this question was ranked second. The human post-mortem plaque claim is
an immunostaining claim. Its entire weight rests on antisera whose only reported validation is
circular, and whose Δ-specific member shares two-thirds of its epitope with the protein it must be
distinguished from. **The human plaque data cannot be scored higher than the antibodies that
generated it.**

---

## 3 · Question 3 — The filter retardation assay on human post-mortem hippocampi

**Answer: n is given (42 controls, 96 AD) but the samples were pooled into 3 and 4 groups, so the
analytical n is 3 vs 4; no blinding is stated anywhere; the comparator group is NOT age-matched and
the paper says so itself; and — decisively — the assay was run with the PAN-specific antibody, so it
does not resolve the Δ isoform at all.**

### 3a · Numbers, ages, groups

> "Total samples from nondemented, younger controls (59±17 years old; = 42) and older AD patients
> (80±8.8 years old; = 96) were randomly divided into 3 and 4 groups, respectively."
> — PMID 25650666, Results

> "No significant difference was shown in TPC6A or TIAF1 aggregation for samples between younger
> nondemented controls (14 samples per group; total 3 groups; 42 to 76 years old) and older AD
> patients (24 samples per group; total 4 groups; 71 to 90 years old)."
> — PMID 25650666, Figure 3 legend

Arithmetic checks: 14 × 3 = 42, 24 × 4 = 96. The two statements agree.

- **Subjects:** 42 non-demented controls, 96 AD. That is a large post-mortem series, and I credit it.
- **Ages:** controls mean 59 ± 17, range 42–76. AD mean 80 ± 8.8, range 71–90.
- **Groups:** 3 control groups, 4 AD groups. The phrase "14 samples per group" indicates the
  individuals were combined into groups for the assay. **The unit of analysis is therefore the group,
  not the subject: effectively n = 3 vs n = 4.** Any Student's t-test on these is a test on 3 versus
  4 observations, not 42 versus 96. The paper does not acknowledge this.

### 3b · The comparator is not age-matched, and the paper concedes it

Mean age difference ≈ 21 years; the ranges barely overlap (42–76 vs 71–90). The paper's own wording
is "younger nondemented controls" and "older AD patients". **Diagnosis and age are fully confounded
in this design.** No result from this assay can distinguish an AD effect from an ageing effect.

This also sits awkwardly with the Figure 2 cortex cohort, described as:

> "Human brain cortical tissue sections from AD patients and age-matched controls, along with
> lysates from cell lines, were used for IHC and Western blotting" — PMID 25650666, Figure 2 legend

> "In comparison, much less aggregation was shown for the wild type TPC6A in the brain cortex in
> age-matched control samples (Figure)." — PMID 25650666, Results

These are a different sample set (fixed cortical sections vs frozen hippocampus), so this is not a
strict contradiction. But **no ages are ever given for the Figure 2 cortex cohort**, so the
"age-matched" claim there is unverifiable from the paper, while the one cohort whose ages *are*
given is explicitly not age-matched.

### 3c · Blinding

**The words "blind", "blinded", "blinding" and "masked" do not appear anywhere in the paper.** No
blinding of scoring, of group assignment, or of image analysis is stated. Given that quantification
was performed by densitometry in a general-purpose image editor —

> "Adobe Photoshop CS5 software was used to analyze the extent of protein expression from Western
> blots." — PMID 25650666, Methods

— unblinded scoring is a material concern, not a formality.

### 3d · The numbers reported

> "TPC6A aggregates were found in both control and AD groups to a similar extent (~40% positive)
> (Figure), suggesting that TPC6A aggregates are relatively stable in the brain."
> — PMID 25650666, Results

> "In agreement with our previous reports [,], the levels of protein aggregates for
> Tyr33-phosphorylated WWOX (p-WWOX) were significantly reduced by ~40% in the AD samples, compared
> to nondemented controls (Figure). The extent of protein aggregation for NFT and Aβ was
> significantly increased in the AD samples, compared with the nondemented controls (Figure)."
> — PMID 25650666, Results

What is given: one number, "~40% positive", for TPC6A, identical in both arms. What is not given
anywhere in the running text or the Figure 3 legend: per-group values, standard deviations, exact p
values, or the effect size for NFT and Aβ. "Significantly reduced by ~40%" and "significantly
increased" are assertions of significance with no statistic attached. The only statistical annotation
in the whole of Figure 3's legend belongs to a different panel (the APP/PS1 mouse immunofluorescence):

> "Immuno-intensity was measured and normalized to negative controls (mean ± standard deviation, = 5;
> **< 0.05, student's test)." — PMID 25650666, Figure 3 legend

(Noting in passing that `**` conventionally denotes p<0.01, not p<0.05.)

### 3e · The decisive defect — this assay used the pan-specific antibody

> "Both wild type TPC6A and TPC6AΔ are present in the aggregates, as determined using the TPC6A
> (84–100) peptide antibody." — PMID 25650666, Results

> "Western blotting was then carried out using specific antibodies for TPC6A (pan-specific), TIAF1,
> Tyr33-phosphorylated WWOX (p-WWOX), NFT and Aβ." — PMID 25650666, Figure 3 legend

Peptide 84–100 is, by the paper's own Methods, the **pan-specific** reagent: "amino acid #84–100 for
pan-specific antibody production". It lies outside the deleted segment and therefore **cannot
distinguish TPC6AΔ from wild-type TPC6A by construction.**

So the human post-mortem filter retardation experiment measures **total TPC6A aggregate**, and the
Results section is correspondingly and correctly titled *"Aggregation of TPC6A and TIAF1 in
nondemented human hippocampi"* — TPC6A, not TPC6AΔ. See §5a for what the Abstract then does with it.

**Finding 3.** Subject numbers are good; analytical n is 3 vs 4; comparator is age-confounded; no
blinding; one descriptive number and no inferential statistics for the TPC6A arm; and the isoform is
not resolved. Whether individual dot-blot intensities were graded on a panel I **cannot assess — no
figure image was available.** Marked UNRESOLVED on that sub-point.

---

## 4 · Question 4 — Ectopic overexpression versus endogenous protein

**Answer: 100% of the causal/mechanistic claims are ectopic overexpression of fluorescent-protein
fusions; 100% of the endogenous evidence is antibody-based imaging or blotting with the antisera of
§2; and the two sets never touch — no endogenous experiment tests any mechanism, and no ectopic
experiment involves an endogenous protein.**

I attribute below from running text and legends only. Panel-level attribution is sometimes
indeterminate because figure callouts are stripped (§0); where so, I say it.

### 4a · Ectopic — overexpressed fusion constructs

> "Neuroblastoma SK-N-SH cells were transiently overexpressed with ECFP or ECFP-TPC6AΔ. After
> culturing for 24 hr, the cells were treated with TGF-β1 (5 ng/ml) for 6–12 hr. TGF-β1
> significantly increased the production of Aβ in the ECFP-TPC6AΔ-expressing cells in 12 hr"
> — PMID 25650666, Results  *(→ the Aβ-production claim)*

> "Transiently overexpressed wild type TPC6A or TPC6AΔ was equally potent in causing cell death
> (~50–75% apoptosis of SK-N-SH and other cell lines using 10 μg expression constructs)."
> — PMID 25650666, Results  *(→ the cell-death claim; note the 10 μg construct load)*

> "When ectopic TPC6AΔ became aggregated in SK-N-SH cells, TPC6AΔ induced caspase 3 activation
> (Figure). Without aggregation, TPC6AΔ did not induce activation of caspase 3 (Figure). TGF-β1
> increased TPC6AΔ aggregation and subsequent caspase 3 activation (Figure)."
> — PMID 25650666, Results  *(→ the whole aggregation→caspase axis)*

> "By site-directed mutagenesis, the S35G mutant of TPC6AΔ significantly lost its capability in
> aggregation and did not activate caspase 3 (Figure). The Y112F mutant had a reduced effect in
> aggregation and causing caspase 3 activation (Figure)."
> — PMID 25650666, Results  *(→ the entire Ser35-dependence claim, the node the chain needs)*

> "COS7 cells were co-transfected with small interfering RNA (siRNA)-targeting WWOX and
> EYFP-TPC6AΔ, EYFP-TPC6A, or EYFP. The cells were then cultured for 24 hr. When WWOX was knocked
> down by siRNA (WOX1si), ectopic TPC6AΔ and TIAF1 became aggregated by greater than 80% of cells"
> — PMID 25650666, Results  *(→ the WWOX-controls-aggregation claim)*

Every one of these is a transiently transfected ECFP/EGFP/EYFP N-terminal fusion. The WWOX-knockdown
experiment — the one that connects TPC6AΔ to this laboratory's core protein — is run in **COS7
monkey kidney fibroblasts**, a non-neural cell of a different species, scored by counting
fluorescent puncta in ~100–150 cells. A GFP-family fusion tag is itself a weakly self-associating
moiety, and "aggregation" scored as puncta in an overexpressing cell is a readout with a known
false-positive mode that the paper does not address.

### 4b · Endogenous — antibody-dependent, and unquantified where it is isoform-specific

> "By immunohistochemistry (IHC), we showed the presence of extracellular TPC6AΔ aggregates or
> plaques with phosphorylation at Ser35 in the human AD cortex (Figure)."
> — PMID 25650666, Results  *(Fig 2 — the central endogenous Δ claim; no n, no quantification, no statistics anywhere in text or legend)*

> "TPC6A aggregates (green) are present in the mitochondria of degenerative neurons in the AD
> hippocampus." — PMID 25650666, Figure 4 legend  *(pan-specific antibody — "pan-specific antibody for TPC6A (green)")*

> "Colocalization of S35-phosphorylated TPC6AΔ with activated caspase 3 in the AD hippocampal tissue
> sections. A representative data is shown." — PMID 25650666, Figure 4 legend
> *(the only endogenous evidence linking pSer35-Δ to caspase — and it is one representative image, explicitly)*

> "Hippocampal tissue sections of APP/PS1-transgenic mice were stained with aliquots of TPC6A
> pan-specific antiserum" — PMID 25650666, Figure 3 legend  *(pan — not isoform-resolved)*

### 4c · The split, stated plainly

| Claim | Evidence class | Isoform-resolved? | Quantified? |
|---|---|---|---|
| Δ aggregates → caspase 3 | ectopic, EYFP fusion, SK-N-SH | yes (construct) | yes (n=3, ~50 cells) |
| Ser35 required (S35G) | ectopic, EYFP fusion | yes (construct) | yes |
| Tyr112 contributes (Y112F) | ectopic, EYFP fusion | yes (construct) | yes |
| TGF-β1 → Δ aggregation → Aβ | ectopic, ECFP fusion | yes (construct) | yes (n=5) |
| WWOX knockdown → Δ aggregation | ectopic, EYFP fusion, COS7 | yes (construct) | yes (~100–150 cells) |
| **Δ plaques in human AD cortex** | endogenous IHC | claimed, via §2 antisera | **no** |
| **Total TPC6A aggregate in human hippocampus** | endogenous filter retardation | **no — pan antibody** | partly (~40%) |
| **TPC6A in AD mitochondria** | endogenous IHC | **no — pan antibody** | no |
| **TPC6A in APP/PS1 mouse neurons** | endogenous IF | **no — pan antibody** | yes (n=5) |
| **pSer35-Δ with active caspase 3** | endogenous IHC | claimed | **no — "representative"** |

The pattern is exact and it is the crux of this audit: **wherever the evidence is endogenous it is
either not isoform-resolved or not quantified; wherever it is isoform-resolved and quantified it is
an overexpressed fusion protein.** There is no cell in this paper in which the endogenous Δ isoform
was manipulated and a consequence measured.

### 4d · "Data not shown" — six instances, several load-bearing

Counted in the readable text: the 50 Asian genomic DNAs; cerebellar TPC6AΔ localisation;
hippocampal TPC6AΔ in the `Wwox` KO (Figure 5 legend); the weak TPC6AΔ–TPC6Awt binding; and, most
significantly, an entire *Wwox*-null phenotype in the Discussion:

> "We found that knockout −/− MEF cells are prone to possess aggregates of TPC6A, TIAF1, JNK1 and
> upregulated expression of β-secretase and Tau tangles (data not shown), suggesting a role of WWOX
> in stabilizing proteins and blocking their aggregation." — PMID 25650666, Discussion

Five distinct molecular claims in one sentence, none shown.

---

## 5 · Internal contradictions and unsupported transitions

Five recorded. Both sides quoted verbatim, as instructed.

### 5a · The Abstract converts a pan-antibody result into an isoform result — and converts a null result into a temporal one

> **Abstract:** "Filter retardation assays revealed that aggregate formation of TPC6AΔ occurs
> preceding Aβ generation in the hippocampi of middle-aged postmortem normal humans."
> — PMID 25650666

> **Results:** "Both wild type TPC6A and TPC6AΔ are present in the aggregates, as determined using
> the TPC6A (84–100) peptide antibody." — PMID 25650666

> **Results:** "TPC6A aggregates were found in both control and AD groups to a similar extent (~40%
> positive) (Figure), suggesting that TPC6A aggregates are relatively stable in the brain."
> — PMID 25650666

Two separate over-statements in one Abstract sentence.
**(i)** The Abstract attributes to **TPC6AΔ** a result the Results attribute to the **pan-specific
antibody**, which by the paper's own Methods cannot distinguish the isoforms.
**(ii)** The Abstract says the aggregation "occurs **preceding**" Aβ generation. The underlying
result is a **null**: equal aggregate in young controls and old AD. A cross-sectional post-mortem
comparison of a younger non-demented group against an older AD group cannot establish temporal
order in any individual, and a null difference does not establish it either. The Results' own
inference from that null is different and more modest — "relatively stable in the brain".

This is the most consequential discrepancy in the paper, because the "TPC6AΔ aggregates precede Aβ"
sentence is the one that gets cited downstream as the origin of the chain.

### 5b · "TPC6AΔ, but not the wild type, forms cortical plaques" versus wild-type TPC6A aggregating in three places

> **Discussion:** "TPC6AΔ, but not the wild type, forms cortical plaques." — PMID 25650666

against, in the same paper:

> **Results (Fig 3):** "Both wild type TPC6A and TPC6AΔ are present in the aggregates" — PMID 25650666

> **Results (Fig 2):** "However, TPC6A became polymerized in the nucleus (Figure)." — PMID 25650666

> **Results (Fig 4):** "Overexpressed wild type TPC6A underwent aggregation and caused apoptosis, but
> did not induce caspase 3 activation (Figure)." — PMID 25650666

> **Discussion:** "Importantly, overexpressed wild type TPC6A may undergo aggregation, but fails to
> activate caspases." — PMID 25650666

> **Discussion:** "However, both proteins become aggregated in the nucleolus upon stimulation with
> TGF-β1." — PMID 25650666

A charitable reading rescues the Discussion sentence on compartment: *cortical extracellular*
plaques specifically may be Δ-restricted, while WT aggregates in nucleus, nucleolus and hippocampal
insoluble fraction. But the sentence is stated flatly and unqualified, and the paper's selectivity
claim is thereby weaker than the Discussion and Title present it. **Wild-type TPC6A aggregates too.
What is Δ-restricted, on this paper's evidence, is not aggregation but caspase-3 activation — and
that is an ectopic-overexpression result (§4a).**

Relatedly, on potency the paper states the opposite of selectivity outright:

> "Transiently overexpressed wild type TPC6A or TPC6AΔ was **equally potent** in causing cell death"
> — PMID 25650666, Results (emphasis mine)

### 5c · APP/PS1 in Results and Figure 3, APP/PS2 in Methods

> **Results:** "We also showed the significantly increased levels of TPC6A aggregates in the
> degenerative neurons of hippocampi of **APP/PS1-transgenic** mice, as determined by
> immunofluorescence microscopy (Figure)." — PMID 25650666

> **Figure 3 legend:** "Hippocampal tissue sections of **APP/PS1-transgenic** mice were stained with
> aliquots of TPC6A pan-specific antiserum" — PMID 25650666

> **Methods:** "Frozen hippocampal sections of **APP/PS2 transgenic** mice were prepared as
> described []." — PMID 25650666

A clean, unambiguous mismatch of the transgenic line between Methods and Results/Figure. APP/PS1 and
APP/PS2 are different models. This is the same class of defect earlier waves recorded in this
laboratory's output (Tyr112/Tyr216; aggregates/does-not-aggregate two sentences apart). **The reader
cannot know which mouse was used.**

### 5d · Hippocampal TPC6AΔ is claimed in the Abstract and is "data not shown" in the Results

> **Abstract:** "In a gene knockout mouse model, we showed the plaques of pT181-Tau and TPC6AΔ in the
> cortex **and hippocampus** in 3-week-old mice" — PMID 25650666

> **Results:** "However, pS35-TPC6AΔ and TPC6AΔ are located in the adjacent stratum oriens and
> stratum radiatum, and the proteins appear as extracellular aggregates (see arrows, Figure;
> **data not shown for TPC6AΔ**)." — PMID 25650666

> **Figure 5 legend:** "pS35-TPC6AΔ and TPC6AΔ are present in the extracellular matrix of adjacent
> stratum oriens and stratum radiatum as aggregates (see red arrows; **data not shown for TPC6AΔ**)."
> — PMID 25650666

The Abstract asserts as shown what the Results twice mark as not shown.

### 5e · Y112F — "reduced effect" versus "slightly reduces (<30%)"

> **Results:** "The Y112F mutant had a reduced effect in aggregation and causing caspase 3
> activation (Figure)." — PMID 25650666

> **Discussion:** "Alteration of Tyr112 to Phe112 **slightly** reduces TPC6AΔ aggregation (<30%) in
> the presence or absence of TGF-β." — PMID 25650666

Minor: a magnitude qualifier appears only in the Discussion, and the caspase-3 half of the Results
claim is dropped there. Recorded for completeness; low weight.

### 5f · NOT a contradiction — recorded because an earlier wave flagged this residue pair elsewhere

The Tyr112/Ser35 numbering is **internally coherent** in this paper:

> "Two potential phosphorylation sites are Ser49 and Tyr126 for TPC6A, or Ser35 and Tyr112 for
> TPC6AΔ." — PMID 25650666, Figure 1 legend

35 + 14 = 49 and 112 + 14 = 126, matching the 14-residue deletion exactly. Ser35 is likewise the
second serine of the Δ #24–38 peptide, as required. **No Tyr112/Tyr216-class error in this paper.**
The earlier wave's finding concerned a different Chang-lab paper and should not be transferred here.

---

## 6 · Additional recorded observations

### 6a · The `Wwox` knockout mouse data — pT181-Tau is quantified with controls; TPC6AΔ is not quantified at all

> "The numbers of pT181-Tau aggregates were counted in the brain hemisphere sections of +/+. −/+, and
> −/− mice (= 5). **Two representative pictures are shown** for the brain tissue sections of Wwox −/−
> mice, and one for Wwox +/+ mice." — PMID 25650666, Figure 5 legend

> "In parallel, pT181-Tau aggregates were significantly increased in the brain hemisphere sections of
> the 3-week-old knockout mice, as compared to wild type and heterozygous mice (Figure)."
> — PMID 25650666, Results

**pT181-Tau:** n = 5, three genotypes (+/+, +/−, −/−) — so proper littermate controls including the
heterozygote, and an actual count as the readout. This is the best-controlled endogenous experiment
in the paper. Its weaknesses: no p value in the legend, "brain hemisphere sections" is not a
regionally resolved unit, and no blinding is stated.

**TPC6AΔ in the same mice:** by contrast, purely descriptive.

> "The wild type TPC6A is mainly expressed in the perinuclear areas of neurons in the brain cortex of
> 3-week-old knockout mice (Figure). In contrast, TPC6AΔ aggregates are expressed in the
> extracellular matrix of the cortex (Figure)." — PMID 25650666, Results

No n, no count, no comparison against wild-type or heterozygous littermates, no statistics — and for
the hippocampus, explicitly "data not shown" (§5d). **The `Wwox`-KO TPC6AΔ plaque claim is
representative-image evidence.**

Two further unaddressed problems with this experiment:

1. **Which knockout?** Methods describe constructing **two** targeting vectors — "we have designed
   insertion of LoxP sites to a vector for targeting exon 1 and 2/3/4, respectively" with two
   distinct genotyping primer sets. The Figure 5 legend says "Ablation of gene at the exon 1 was
   carried out in mice." The Results never state which line the imaging used. Indeterminate.
2. **Species transfer of the isoform, never tested.** The Δ isoform was cloned from human U937 cells;
   the splice prediction used human genomic sequence; the EST count was "in humans"; the deletion
   maps to "chromosome 19q13.32", a human coordinate; and all four antisera were raised against
   **human** peptide sequences. These reagents are then applied to **mouse** brain. The paper never
   demonstrates that mouse *Trappc6a* undergoes the same alternative splice, never shows the mouse Δ
   transcript or protein, and never establishes epitope conservation. **The mouse arm of the isoform
   claim presupposes exactly what the paper set out to establish.** This compounds §2 rather than
   substituting for it.

### 6b · Gene versus isoform conflation — three distinct instances

**(i) In the Introduction, the human genetics of the *gene* is imported to motivate the *isoform*:**

> "Human gene is involved in nonverbal reasoning in 2 Scottish cohorts, and is suggested for a role
> in AD []." — PMID 25650666, Introduction

(The gene symbol is stripped by the extraction; context makes it `TRAPPC6A`, and the "2 Scottish
cohorts" is the Lothian Birth Cohort work.) This is the paper's only citation of independent human
genetic evidence, and it is evidence about **TRAPPC6A the locus**. It is placed immediately before
the paper's own isoform work with no distinction drawn between them. **The genetic support for the
gene does not transfer to the Δ isoform, and the paper does not say that it does not.** This is the
exact inferential seam the batch brief asked about, and it is present.

**(ii) In the Results, "TPC6A" is used for pan-antibody measurements and then read as isoform-
specific elsewhere.** The Results section heading is *"Aggregation of TPC6A and TIAF1 in nondemented
human hippocampi"* and its content is pan-antibody; the Abstract renders the same experiment as
TPC6AΔ (§5a).

**(iii) In the Discussion, the two are alternated within single arguments:**

> "Importantly, we demonstrated the presence of **TPC6A plaques** and pT181-Tau aggregates in the
> cortex of −/− mouse brain." — PMID 25650666, Discussion

versus the Results and Figure 5, where the cortical extracellular plaques are attributed specifically
to **TPC6AΔ** and wild-type TPC6A is explicitly perinuclear. Within the Discussion the plaque is
called "TPC6A"; three sentences earlier in the same Discussion it is "TPC6AΔ and Tau plaques". The
usage is not disciplined.

### 6c · Reproducibility defect — neither published mutagenesis primer pair is a valid pair

> "Site-directed mutagenesis was also employed to alter conserved phosphorylation sites Tyr112 and
> Ser35 using the following primer sets: 1) S35G, forward 5′-ATGAGCCTGGGAGTCCTGGA and reverse
> 5′-AGGTCCTGAGGGTCCGAGTA; 2) Y112F, forward 5′-TGGCCTGCAGTTTCTGGAGG and reverse
> 5′-ACCGGACGTCAAAGACCTCC." — PMID 25650666, Methods

Site-directed mutagenesis of this type requires the two primers to be **reverse complements**. As
printed, neither pair is:

- **Y112F:** the printed reverse, `ACCGGACGTCAAAGACCTCC`, is the base-by-base **complement** of the
  forward read in the forward's own direction — i.e. the correct strand written 3′→5′ but labelled
  5′-. The true reverse primer should read `CCTCCAGAAACTGCAGGCCA`.
- **S35G:** the printed reverse, `AGGTCCTGAGGGTCCGAGTA`, read backwards is
  `ATGAGCCTGGGAGTCCTGGA` — **the forward primer itself**. It is the same strand reversed, not the
  complementary strand at all. The true reverse primer should read `TCCAGGACTCCCAGGCTCAT`.

The mutations themselves are correct in the forward primers: `ATGAGCCTG**GGA**GTCCTGGA` encodes
M-S-L-**G**-V-L-E (Ser35→Gly), and `TGGCCTGCAG**TTT**CTGGAGG` encodes the Phe codon for Tyr112→Phe.
So the intended constructs are unambiguous; what is defective is the published protocol.

**Weight: MEDIUM, and this is a reproducibility defect, not a scientific contradiction.** A reader
attempting to remake the S35G and Y112F mutants from the published Methods cannot do so. I could not
inspect the typeset PDF, so I cannot fully exclude a typesetting error introduced downstream of the
authors — but the strings are plain ASCII in a Methods paragraph and the PMC extraction strips
markup, not letters.

### 6d · Zfra appears in Methods and in no experiment

> "Fluoro-Jade C Red was from Chemicon/Invitrogen. **The full length Zfra peptide was synthesized
> (GeneMed Synthesis).**" — PMID 25650666, Methods

The string "Zfra" occurs **exactly once in the entire paper** — in the reagents paragraph. No Zfra
experiment, result, figure or discussion exists. An orphan reagent declaration. Recorded because
this batch concerns the Chang laboratory's peptide-intervention line, of which Zfra is the centre;
its appearance here indicates Zfra work was contemporaneous, but this paper contains **zero Zfra
data** and cannot be cited for any.

### 6e · Sample provenance — the human post-mortem evidence across this laboratory's chain is one collection

> "Human postmortem frozen hippocampal tissues, as well as fixed tissue sections from hippocampi,
> were obtained from the Department of Pathology, University of Colorado Health Sciences Center (by
> Dr. CI Sze, before 2005) [,]. IRB approval was waived. Informed consents were obtained from the
> family members of the deceased patients." — PMID 25650666, Methods

A single institutional collection, assembled before 2005 by a co-author, re-probed here. The paper
itself repeatedly cross-references its own earlier TIAF1 results on what reads as the same material
("In agreement with our previous observations []"). **For node-independence purposes: the TIAF1
human post-mortem data and the TPC6A human post-mortem data are not independent replications. They
are the same cohort, the same laboratory, different antibodies.** A concordance between them is
close to uninformative.

### 6f · Terminology

The Discussion calls tau deposits "plaques" — "TPC6AΔ and Tau plaques can be found in the brain
cortex of knockout mice of less than 3 weeks old." Tau forms tangles/neuropil threads, not plaques.
Trivial in itself; noted because the paper's central claim is a claim about plaque identity.

---

## 7 · Verdict

### `THE ISOFORM IS PLAUSIBLE BUT UNDERDETERMINED`

— with an asymmetry that must travel with the verdict, because the two halves score differently:

**The Δ *transcript* is plausibly real, and partly on third-party evidence.** A cDNA was cloned and
deposited with a GenBank accession; **13 of 55 human TPC6A ESTs in the public database carry the
42-bp deletion** — deposited by other groups, the only non-NCKU evidence in the paper; two
independent splice predictors concur on the same alternative 5′ donor at nt 85; and a genomic
deletion was correctly excluded across 80 DNA samples from two populations. That is a respectable
case for an alternative splice event at this locus. It is not nothing, and it is why this verdict is
not `POORLY EVIDENCED`.

**The Δ *protein*, in brain, is not established — and that is the entity the Chang chain requires.**
Every proposition the downstream chain inherits is a proposition about a protein:

- Its existence in tissue rests on **one band size** (17 kDa vs 20 kDa) seen with rabbit antisera
  whose only reported validation is competition with their own immunising peptide. **No knockout, no
  knockdown, no mass spectrometry, no immunoprecipitation.** The lab's own `TPC6Asi` construct was
  used for a phenotype assay and never for this.
- The Δ-specific antiserum's 15-mer epitope shares a **contiguous 10-mer with wild-type TPC6A**
  (derived, §2c) — and peptide blocking is constitutionally unable to detect that failure mode.
- The Δ transcript has **never been amplified from brain** by anyone in this paper. It was cloned
  from TGF-β1-stimulated monocytes.
- The human post-mortem quantification that the Abstract attributes to TPC6AΔ was performed with the
  **pan-specific** antibody (§3e, §5a).
- Every mechanistic property of the isoform — Ser35 dependence, polymerisation, caspase-3
  activation, Aβ production, WWOX-dependence — is a property of an **ECFP/EYFP fusion transiently
  overexpressed at 10 μg construct**, largely in **COS7 monkey kidney fibroblasts** (§4).
- The mouse arm applies human-sequence antisera to mouse brain **without establishing that the mouse
  orthologue splices this way at all** (§6a).
- And the paper contains a Methods/Results mismatch on the transgenic line used (APP/PS1 vs
  APP/PS2, §5c), an Abstract claim marked "data not shown" twice in the Results (§5d), an Abstract
  that converts a null cross-sectional result into a temporal one (§5a), and two unusable
  mutagenesis primer pairs (§6c).

**Net:** a probably-real splice variant carrying a mechanistic superstructure that its own evidence
cannot support. The node exists as a transcript; **it does not exist as a validated brain protein**,
and every downstream inference — Ser35 → polymerisation → TIAF1 → caspase → Aβ — is therefore
anchored to an entity that has been detected only by reagents that were never tested against a
sample known not to contain it.

**Independence note for the chain.** The gene-level human genetics (Lothian Birth Cohorts;
ADNI/AddNeuroMed; UCLA/All-of-Us late-onset-epilepsy/AD locus) does **not** corroborate this node.
It corroborates `TRAPPC6A` the locus. The Δ isoform is a separate claim, made by one laboratory, and
the paper itself imports the cohort evidence in its Introduction without marking the gap (§6b-i).
Treating gene-level replication as isoform-level replication would be the single most consequential
error available here.

### The one experiment that would settle it

**Isoform-resolved targeted mass spectrometry on human brain tissue — PRM/MRM quantification of the
tryptic peptide spanning the TPC6AΔ splice junction and, in the same run, of the wild-type-only
peptide encoded by codons 29–42 — performed on the insoluble/plaque-enriched fraction of AD and
age-matched control hippocampus.**

Why this and not another: it is the only experiment that removes every dependency identified above
in one step. It needs no antibody, so §2 evaporates. It reads the endogenous protein, so §4
evaporates. It resolves the two isoforms by primary sequence, so §3e and §5a evaporate. It is
performed in brain, so §1's tissue gap closes. And it is quantitative, so "~40% positive" becomes a
ratio of Δ to wild-type — which is precisely the quantity the paper's own Discussion says is the
decisive one ("the ratio of wild type TPC6A versus TPC6AΔ isoform is likely to determine the
tendency of AD pathogenesis in normal individuals") and never measures.

Secondary, if brain MS is out of reach: **long-read (or junction-spanning RT-PCR + Sanger) sequencing
of `TRAPPC6A` transcripts from human hippocampus**, which would at least establish that the splice
event this paper predicted in silico actually occurs in the tissue the chain is about.

**Not settling it:** another immunostaining series with the same antisera, in any species, at any n.

---

*No canonical file was read-modified in producing this audit. No commit candidate is proposed. No
therapeutic inference is drawn. Full text retrieved from PubMed Central (PMID 25650666);
DOI [10.18632/oncotarget.2876](https://doi.org/10.18632/oncotarget.2876).*
