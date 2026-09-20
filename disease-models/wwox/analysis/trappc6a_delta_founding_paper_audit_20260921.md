# TRAPPC6AΔ founding-paper audit — PMID 25650666 (Chang JY & Chang NS 2015)

**Actor:** Scientist A · **Date:** 2026-09-21 · **Mode:** READ-ONLY toward every canonical file. **No commit candidate. No canonical edit. No registry, queue, ledger or current file touched. No therapy proposed.**

Source: PubMed / PMC. According to PubMed, the article is Chang J-Y, Chang N-S. "Trafficking protein particle complex 6A delta (TRAPPC6AΔ) is an extracellular plaque-forming protein in the brain." *Oncotarget* 2015;6(6):3578–89. PMCID PMC4414138. [DOI](https://doi.org/10.18632/oncotarget.2876) · Licence: Creative Commons CC BY 2.5, `is_open_access: true`, source `pmc`.

Persisted artefact: `files/fulltext/PMID25650666_PMC_MCPtext.txt` (35,217 bytes; sha256 `c6e336a927b1ae69779c820b2132010152f3f5c865ba73ec03c55e5c1c41191c`).

---

## VERDICT

> **SINGLE-LAB, UNCORROBORATED** — the TPC6AΔ isoform's splicing origin is *computationally predicted*, never junction-sequenced; its protein existence rests entirely on four in-house rabbit antisera validated by peptide competition alone with **no genetic negative control**; every causal step (aggregation → caspase 3 → Aβ; Ser35 dependence; WWOX-loss → aggregation) is ectopic overexpression of a fluorescent-protein fusion; the human post-mortem arm is **unblinded and age-confounded** (controls 59±17 y vs AD 80±8.8 y) and returned a **null** difference that the Abstract reports as a temporal ordering; and the WWOX↔TPC6AΔ physical interaction on which the entire node depends is asserted in the Abstract and in the Discussion's own summary paragraph while the *same Discussion* states, verbatim, that it is **"unknown."**

---

## 0 · Surface integrity — what the extractor delivered and what it destroyed

| Field | Value |
|---|---|
| **Declared read depth** | ✅ **FULL BODY READ.** Introduction, all six Results sections, Discussion, Materials and Methods, and the legends of Figures 1–6 were delivered as text and read end to end. The Abstract was delivered as a separate JSON field and read. |
| **Body obtainable?** | **Yes.** `get_full_text_article(pmc_ids=["PMC4414138"])` returned a populated `full_text` on the first call. No WebFetch, no curl. |
| **Tables** | None in this paper. Nothing lost on that axis. |
| **References** | 🔴 **Entirely destroyed.** Every citation is delivered as an empty bracket — `[]`, `[,]`, `[–]`. I cannot identify a single work this paper cites. Consequences noted in § 9. |
| **Supplementary** | 🔴 The heading `SUPPLEMENTARY FIGURES` is present with **zero content beneath it**, and the three prose pointers to supplementary material are empty parentheses (see § 0a). Supplementary data exist and I have not seen them. |
| **Figures** | 🔴 **No figure image inspected. No PDF tooling. No panel viewed.** I have the six legends as text and the Results prose. Every statement below about what a figure "shows" is a statement about what the **legend or the prose asserts**, never about pixels. Per rule **D-14** I adjudicate no negative that is asserted only by a figure, and I mark each place where that limit bites. |

### 0a · Exactly what the extractor deleted — verified, load-bearing

The MCP surface silently deleted every italicised token. In this paper the italicised tokens include **every gene symbol**, so the failure is severe and the reader must be warned before any string count is trusted.

| Delivered string | Almost certainly | Evidence |
|---|---|---|
| "deletion of␣gene induces a phenotype with mosaic loss of coat pigment" | *Trappc6a* | grammar requires a gene name |
| "Human␣gene is involved in nonverbal reasoning in 2 Scottish cohorts" | *TRAPPC6A* | ditto |
| "deletion of exon 1 of human␣gene" (×4) | *TRAPPC6A* | ditto |
| "we generated␣gene knockout mice"; "In a␣gene knockout mouse model" | *Wwox* / *WWOX* | genotyping primers and MEF data name Wwox |
| "the cortex of␣−/− mouse brain"; "␣−/− mice can only survive for one month" | *Wwox* | ditto |
| "without WWOX␣and␣, TPC6A and TIAF1 start to polymerize" | probably "WWOX *and* WOX1" or a second italic gene | **not reconstructible** — flagged, not guessed |
| "To support this hypothesis,␣analysis revealed" (Abstract) | *in vitro* | standard phrasing |
| "␣= 42", "␣= 96", "␣= 5", "␣= 3" | *n* = | italic *n* |
| "`**< 0.05`" | *P* < 0.05 | italic *P* |
| "Student's␣-tests" / "Student's␣test" | Student's *t*-test | italic *t* |
| "an␣-terminal internal deletion isoform"; "the␣-terminal SDR domain" | *N*- / *C*-terminal | known architecture |
| "(Genbank accession)" ×3 | the accession numbers themselves | 🔴 **I cannot report the GenBank accessions for either isoform.** |
| 37 instances of "(Figure)" | numbered panel pointers | prose→legend mapping destroyed |

🔴 **Instrument rule, stated for the cold reader.** `TRAPPC6A` as a *gene symbol* occurs **zero** times in the delivered body. That is an **instrument reading about the extractor**, not a fact about the paper — the paper is entirely about that gene. No negative below is ever built on a string count of an italicisable token. The one exception I do rely on is the word **"blind"**, which occurs zero times: "blind"/"blinded"/"blinding" is never italicised in a Methods section, so its absence is informative. I state that reasoning explicitly rather than hiding it.

⚠️ Two peptide sequences in Methods are internally inconsistent in the delivered text — the anti-TPC6AΔ peptide is given as `DPGPGGQKMSLSVLE` (15 residues) and the anti-pSer35 peptide as `DPGPGGQKMSLVLE` (14 residues), i.e. the phospho-serine is **missing from its own phospho-peptide**. This is almost certainly the extractor deleting a superscripted or specially-formatted residue. I treat it as an artefact and **not** as an error by the authors.

---

## 1 · How was the isoform's existence established?

**Answer: by a subtraction-library cDNA clone plus a computational splice *prediction*. No splice junction was sequenced from the tissue in which the isoform is claimed to matter. No mass spectrometry anywhere in the paper.**

The discovery route, verbatim (Results, "Isolation of an N-terminal frame deletion isoform TPC6AΔ in mammalian cells"):

> "TPC6AΔ was originally isolated from TGF-β1-treated monocytic U937 cells in a subtraction cDNA library screen."

> "The deduced protein possesses an internal frame deletion of amino acids #29–42 at the [N]-terminus (Genbank accession)."

Note the word **"deduced."** The protein is inferred from an open reading frame, not observed by sequencing a peptide.

The genomic question was asked and answered — negatively, and this is one of the paper's cleaner results (Results, same section):

> "Thirty hippocampal samples, including 12 controls and 18 AD patients from postmortem Caucasians, were examined. None of the genomic DNA samples were deleted in the exon 1 of human [TRAPPC6A] gene."

So the 42-bp absence is **not** a genomic deletion. That leaves splicing — and splicing is where the evidence becomes prediction:

> "Based upon the aforementioned observations, we determined whether [TRAPPC6A] mRNA undergoes alternative splicing. Computational analyses using 1,400 genomic sequences starting from the CDS sequence on [TRAPPC6A] exon 1 were performed. Results from 2 different web-based tools (NNSplice and NetGene) all predicted that the nt position 85 can be used as an alternative 5′ donor site to initiate splicing and leads to a 42-bp deletion on [TRAPPC6A] exon 1 sequence."

And the corroboration offered is a database count, not an experiment:

> "Additional evidence from EST database searching showed that 13 TPC6A cDNAs out of 55 in total in humans are with the 42-bp deletion."

And the closing inference:

> "Proteins corresponding to wild type TPC6A and TPC6AΔ are shown in cells (Figure), which supports the occurrence of alternative splicing of [TRAPPC6A] mRNA."

**What was actually done, itemised:**

| Method | Performed? | Locator |
|---|---|---|
| Subtraction cDNA library screen in U937 | ✅ Yes | Methods, "Isolation of TPC6AΔ cDNA…" |
| Sequencing of the isolated cDNA | ⚠️ Implied by GenBank deposition; the explicit "identified by sequencing analysis" sentence in Methods describes the **reconstructed full-length** construct, not the Δ clone | Methods, "Isolation of TPC6AΔ cDNA…" |
| **Junction-spanning RT-PCR on brain / any tissue** | 🔴 **No. Not reported anywhere.** | — |
| **Splice-junction sequencing** | 🔴 **No.** | — |
| **Mass spectrometry of the 17-kDa species** | 🔴 **No. The string "mass spec" does not occur, and "spectrometry" is not an italicisable token.** | — |
| Genomic PCR + sequencing (30 human samples, 50 Taiwanese) | ✅ Yes — and **negative** | Results ¶2; Methods, "PCR analysis of partial exon 1 deletion" |
| Splice-site prediction (NNSplice, NetGene2) | ✅ Yes — **this is the sole direct evidence for the splicing mechanism** | Results ¶3; Methods, "Computational analysis" |
| EST database census | ✅ Yes (13/55) | Results ¶3 |
| Antibody detection of a 17-kDa band | ✅ Yes, homemade antisera | Results §"TPC6AΔ aggregates in human AD hippocampal…" |

**A band-size arithmetic problem the prose itself creates.** The paper states a 20-kDa wild-type species and a 17-kDa Δ species:

> "By Western blotting, the 20-kDa wild type protein was identified by the specific antibody (duplicate loading; Figure). Antibodies against TPC6AΔ and its phosphorylated form probed the 17-kDa TPC6AΔ and polymerized pS35-TPC6AΔ, respectively, in the neuroblastoma SK-N-SH cells (Figure)."

A 14-residue internal deletion removes roughly **1.4 kDa**, not 3 kDa. The claimed gel separation is about twice what the stated deletion predicts. This does not refute the isoform — SDS-PAGE mobility is not mass, and a proline/glycine-rich deleted segment (`VSAGLRGEEAGATK`, and the genomic segment is given as GC-rich) can shift anomalously. But it means the **band size alone does not identify the species**, and no orthogonal identification (MS, or the Δ-specific band disappearing under TRAPPC6A knockdown) is provided.

**Bottom line for Q1.** The isoform is real as a *cDNA clone* and plausible as a *transcript* (13/55 ESTs is not nothing). Its existence as a *protein in human brain* is established by nothing except the antibodies audited in § 2. The splicing mechanism named in the title-level claim is a **prediction from two web tools**.

---

## 2 · Were the anti-TPC6AΔ antibodies validated against a genetic negative control?

**Answer: No. Peptide competition only, plus no-primary-antibody controls. There is no knockout, no knockdown, and no full-length-only background anywhere in the antibody validation.**

The complete validation, verbatim (Methods, "Antibodies and antibody production in rabbits"):

> "Specificity of the antisera was tested using the synthetic peptides to block immunostaining."

That is the entire sentence. And in Results:

> "Our antibody is specific, as each immunizing peptide blocked the corresponding immunoreactivity (Figure)."

Peptide competition tests that the antiserum binds the peptide it was raised against. It does **not** test that the signal in tissue is the intended protein. A knockout or knockdown control does; none was run, and the omission is conspicuous because **the lab had both reagents in hand in this very paper**:

- A `TPC6Asi` siRNA construct exists and is used in Figure 6 — "including scramble, WOX1si, TIAF1si and TPC6Asi" — but is never reported as an antibody control.
- `Wwox −/−` mice were generated for this paper. Wild-type *Wwox* MEF cells were used as a staining substrate — "wild type Wwox MEF cells stained with the wild type specific TPC6A (29–42) peptide antibody" — which is a **WWOX** genotype control, not a **TRAPPC6A** one. It tells us nothing about whether the anti-TPC6A signal is TPC6A.

The only other negative controls are secondary-only:

> "Also, in negative controls (see D), no primary antibodies were used in the IHC." (Figure 2 legend)
> "In negative controls, the sections were stained with the secondary antibody only…" (Figure 3 legend)
> "In negative controls, no primary antibody was used in the immunostaining." (Figure 4 legend)

**Why this matters more than usual here.** The antibody design is, in principle, good: the wild-type-specific antibody is raised against `VSAGLRGEEAGATK` = exactly the deleted residues #29–42, and the Δ-specific antibody against `DPGPGGQKMSLSVLE` = residues #24–38 in Δ numbering, i.e. **spanning the neo-junction**. A junction-spanning polyclonal is the right instrument. But a junction-spanning polyclonal is also the instrument most likely to cross-react, because the epitope is short, the flanks are shared with the parent protein, and the deleted segment is compositionally unusual. **Exactly this design requires a genetic null to be believed, and exactly this design did not get one.**

Every downstream claim in the paper — the extracellular plaques, the wild-type/Δ anatomical segregation, the pSer35 plaques, the *Wwox*-null cortical aggregates — is read out through these four unvalidated antisera.

🔴 **D-14 limit.** Whether the peptide-competition panel is convincing as an *image* I cannot say; I did not inspect it. My finding is about what the Methods **declare was done**, which is peptide competition and nothing else. That is a statement about the stated protocol, not about a figure.

---

## 3 · The filter retardation assay on post-mortem human hippocampus

**Answer: no blinded arm is reported; 42 controls and 96 AD cases; controls are NOT age-matched to cases — they are two decades younger by design — and no scorer blinding, scoring rule, threshold, post-mortem interval, sex distribution or multiple-comparison correction is stated.**

Numbers, verbatim (Results, "Aggregation of TPC6A and TIAF1 in nondemented human hippocampi"):

> "Total samples from nondemented, younger controls (59±17 years old; [n] = 42) and older AD patients (80±8.8 years old; [n] = 96) were randomly divided into 3 and 4 groups, respectively."

Figure 3 legend, consistent with the above (3 × 14 = 42; 4 × 24 = 96):

> "No significant difference was shown in TPC6A or TIAF1 aggregation for samples between younger nondemented controls (14 samples per group; total 3 groups; 42 to 76 years old) and older AD patients (24 samples per group; total 4 groups; 71 to 90 years old)."

| Axis | What the paper reports |
|---|---|
| **n** | 42 controls, 96 AD; pooled into 3 and 4 dot-blot groups |
| **Blinding of the scorer to diagnosis** | 🔴 **Not reported. The words "blind", "blinded", "blinding", "masked" do not appear in the delivered text.** |
| **Age matching** | 🔴 **Explicitly absent.** Controls 59±17 y (range 42–76); AD 80±8.8 y (range 71–90). The group means differ by ~21 years and the ranges barely overlap. The authors describe the controls as "younger" — matching was not attempted for this assay. |
| **Sex, post-mortem interval, Braak stage, APOE, agonal state, storage time** | 🔴 **None reported.** |
| **Diagnostic confirmation of "AD"** | 🔴 Not described. Source is one pathology department; see below. |
| **Scoring rule for "~40% positive"** | 🔴 **Not described.** No threshold, no densitometry method for this panel, no inter-rater measure. Elsewhere the paper says "Adobe Photoshop CS5 software was used to analyze the extent of protein expression from Western blots." |
| **Statistics** | "Student's [t]-tests were carried out for statistical analysis." No correction for the multiple proteins probed (TPC6A, TIAF1, p-WWOX, NFT, Aβ), no age covariate. |
| **Loading** | 10 / 30 / 60 μg per sample, filtered through 0.2 μm cellulose acetate — a dose series, which is good practice |
| **Ethics** | "IRB approval was waived. Informed consents were obtained from the family members of the deceased patients." |

**The design flaw is structural, not cosmetic.** Diagnosis and age are perfectly confounded. Every between-group difference reported from this assay — including the two that the paper treats as positive findings —

> "the levels of protein aggregates for Tyr33-phosphorylated WWOX (p-WWOX) were significantly reduced by ~40% in the AD samples, compared to nondemented controls"

> "The extent of protein aggregation for NFT and Aβ was significantly increased in the AD samples, compared with the nondemented controls"

— is equally consistent with a two-decade age difference as with disease. And the **primary** result of the assay, the TPC6A one, is a **null**:

> "TPC6A aggregates were found in both control and AD groups to a similar extent (~40% positive) (Figure), suggesting that TPC6A aggregates are relatively stable in the brain."

⚠️ **Additional limit on interpreting this assay at all:** the readout was generated with the **pan-specific** antibody, which cannot distinguish the isoform from wild type. The paper says so:

> "Both wild type TPC6A and TPC6AΔ are present in the aggregates, as determined using the TPC6A (84–100) peptide antibody."

So the filter retardation assay **does not measure TPC6AΔ**. It measures TPC6A-plus-TPC6AΔ. This is load-bearing for § 5.

**Provenance note.** The tissue is the same bank used for this group's prior TIAF1 work (Methods, "Cell lines, chemicals and human postmortem hippocampal tissues"):

> "Human postmortem frozen hippocampal tissues, as well as fixed tissue sections from hippocampi, were obtained from the Department of Pathology, University of Colorado Health Sciences Center (by Dr. CI Sze, before 2005)."

One source, one collection, pre-2005, one lab. See § 9 for why this collapses two supposedly independent nodes into one.

---

## 4 · Ectopic overexpression versus endogenous protein

**Answer: every causal and mechanistic result in the paper is ectopic overexpression of a fluorescent-protein fusion. Every endogenous result is descriptive localisation or a dot-blot census. There is not one experiment in which endogenous TPC6AΔ is manipulated and an outcome is measured.**

| Figure / experiment | System | Ectopic or endogenous? | What it can support |
|---|---|---|---|
| **Fig 1** — genomic PCR + sequencing, 30 human samples | human genomic DNA | **Endogenous** | A negative: no genomic deletion. Clean. |
| **Fig 1** — NNSplice / NetGene2 / EST census | *in silico* | **Neither — prediction** | A hypothesis about splicing |
| **Fig 2** — IHC of human AD and control cortex, 4 antisera | human tissue | **Endogenous** | Localisation only; wholly dependent on § 2 |
| **Fig 2** — WB of SK-N-SH, wt *Wwox* MEF, rat glial lysates | cell lines | **Endogenous** | Band presence at 20 / 17 kDa |
| **Fig 3A** — filter retardation, 42 + 96 human hippocampi | human tissue | **Endogenous**, but **pan-antibody** | TPC6A-total aggregation; **null** between groups |
| **Fig 3B** — non-reducing SDS-PAGE, soluble aggregates | human tissue | **Endogenous** | Descriptive |
| **Fig 3C** — APP/PS1 transgenic mouse hippocampus IF | mouse, transgenic APP/PS1 | **Endogenous TPC6A** on a transgenic background | Correlation with degenerating neurons |
| **Fig 4A** — ECFP-TPC6AΔ in SK-N-SH + TGF-β1 → Aβ | **ECTOPIC** | ECFP fusion, transient | Sufficiency at most |
| **Fig 4B–C** — TPC6A in mitochondria of AD neurons | human tissue | **Endogenous** | Localisation; the paper's own wording is "suggests" |
| **Fig 4D–G** — EYFP-TPC6AΔ / EYFP-TPC6Awt aggregation → caspase 3 | **ECTOPIC** | EYFP fusion, 10 μg construct | Sufficiency at most |
| **Fig 4H** — S35G, Y112F mutants, quantified | **ECTOPIC** | site-directed mutants of the fusion | Structure–activity within an overexpression system |
| **Fig 4I** — pS35-TPC6AΔ colocalised with active caspase 3 | human tissue | **Endogenous** | Colocalisation; "A representative data is shown" |
| **Fig 5A–C** — *Wwox* −/− mouse brain IHC | mouse, genetic null | **Endogenous** | The only endogenous genetic arm; descriptive (see § 5) |
| **Fig 5D** — pT181-Tau counts across +/+, −/+, −/− | mouse, genetic null | **Endogenous**, quantified, genotype-contrasted | The single strongest result in the paper — **but it is about Tau, not TPC6AΔ** |
| **Fig 6** — WWOX siRNA + EYFP-TPC6AΔ / EYFP-TIAF1 in COS7 | **ECTOPIC**, in **monkey kidney fibroblasts** | EYFP fusion | Sufficiency, in a non-neural, non-human cell |

**Tally.** Of the mechanistic chain the Abstract asserts — splicing → protein → Ser35 phosphorylation → polymerisation → caspase 3 → Aβ, restrained by WWOX — **every link that is a causal claim is ectopic**, and the only genotype-contrasted quantification in the paper (Fig 5D) measures **pT181-Tau**, a different protein.

**Two internal facts that further limit the overexpression arm.**

First, the dose is very large and the toxicity is not isoform-specific:

> "Transiently overexpressed wild type TPC6A or TPC6AΔ was equally potent in causing cell death (~50–75% apoptosis of SK-N-SH and other cell lines using 10 μg expression constructs)."

Wild type and Δ kill cells **equally**. The isoform-specific claim survives only on the narrower readout of caspase-3 activation:

> "In contrast, overexpressed wild type TPC6A, with or without aggregation, did not induce caspase 3 activation (Figure)."
> "Overexpressed wild type TPC6A underwent aggregation and caused apoptosis, but did not induce caspase 3 activation (Figure)."

So the paper's own data say: wild-type TPC6A also aggregates, and also causes apoptosis, and differs from Δ only in caspase-3 engagement. The title-level dichotomy — Δ is the plaque-forming pathogenic species, wild type is the innocent cytosolic one — is **not supported by the cell-death data in the same figure**.

Second, the aggregation counts rest on small manual scoring: "~50 cells counted per experiment" ([n] = 3), "~100 cells counted", "~150 cells counted" — by fluorescence microscopy, with no stated blinding and no stated scoring criterion for what counts as a "punctum".

**Consequence, in the terms the Chang↔Aldaz adjudication established this session:** nothing in this paper licenses a necessity claim. Overexpressing a GFP-tagged 17-kDa protein at 10 μg per electroporation until half the cells die demonstrates that the construct is *sufficient* to do something in that system. It does not show that endogenous TPC6AΔ does that, at endogenous abundance, in a neuron.

---

## 5 · Abstract versus Results

**There is no shortage of divergence. I found seven, one of which is an outright internal contradiction within the paper's own Discussion.** This is not a "no finding" case.

### 5.1 🔴 Attribution inversion — the filter retardation assay did not measure TPC6AΔ

Abstract:
> "Filter retardation assays revealed that aggregate formation of TPC6AΔ occurs preceding Aβ generation in the hippocampi of middle-aged postmortem normal humans."

Results, same assay:
> "Both wild type TPC6A and TPC6AΔ are present in the aggregates, as determined using the TPC6A (84–100) peptide antibody."

The (84–100) antibody is the **pan-specific** one — Figure 1's legend: "TPC6A (84–100) (green) peptide antibody for wild type and TPC6AΔ." The Results prose and the Figure 3 legend both name the analyte as **"TPC6A"**, unqualified. The Abstract renames it **"TPC6AΔ"**. The assay is isoform-blind and the Abstract reports it as isoform-specific.

### 5.2 🔴 Temporal claim from a null, cross-sectional result

The same Abstract sentence asserts that TPC6AΔ aggregation **"occurs preceding"** Aβ generation. What the body reports is the opposite of a temporal ordering — it is a **non-difference**:

> "TPC6A aggregates were found in both control and AD groups to a similar extent (~40% positive) (Figure), suggesting that TPC6A aggregates are relatively stable in the brain."

Figure 3 legend: **"No significant difference was shown in TPC6A or TIAF1 aggregation…"**

The design is cross-sectional post-mortem tissue from two non-overlapping age bands. No subject was measured twice. "Preceding" is an inference from (aggregate is already present in younger controls) + (Aβ is higher in older AD cases), across two confounded groups, with no within-subject ordering. The body never claims precedence; the Abstract does.

### 5.3 🔴 The *Wwox*-knockout arm has no genotype contrast for TPC6AΔ

Abstract:
> "In a [Wwox] gene knockout mouse model, we showed the plaques of pT181-Tau and TPC6AΔ in the cortex and hippocampus in 3-week-old mice, suggesting a role of WWOX in limiting TPC6AΔ aggregation."

Body (Results, "[Wwox] gene ablation induces TPC6AΔ and tau aggregation…"), read carefully: every TPC6AΔ observation is **inside the knockout animal**, and the contrast drawn is between **two proteins in the same animal**, not between genotypes:

> "The wild type TPC6A is mainly expressed in the perinuclear areas of neurons in the brain cortex of 3-week-old knockout mice (Figure). In contrast, TPC6AΔ aggregates are expressed in the extracellular matrix of the cortex (Figure)."

The only genotype-contrasted, quantified measurement in the section is Tau:

> "In parallel, pT181-Tau aggregates were significantly increased in the brain hemisphere sections of the 3-week-old [Wwox] knockout mice, as compared to wild type and heterozygous mice (Figure)."
> Figure 5 legend: "The numbers of pT181-Tau aggregates were counted in the brain hemisphere sections of [Wwox] +/+. −/+, and −/− mice ([n] = 5)."

Figure 5's legend for the TPC6AΔ panels likewise describes only knockout tissue, and its only +/+ material is attached to the **Tau** panel: "Two representative pictures are shown for the brain tissue sections of Wwox −/− mice, and one for Wwox +/+ mice."

🔴 **D-14 limit, stated plainly.** A wild-type-versus-knockout TPC6AΔ comparison could exist as an unlabelled panel that I cannot see. **I do not adjudicate that negative from a figure.** What I adjudicate is the prose and the legend, and neither reports a TPC6AΔ genotype contrast, quantified or otherwise. On the delivered text, the Abstract's "suggesting a role of WWOX in limiting TPC6AΔ aggregation" is supported *in vivo* only by analogy to the Tau panel.

### 5.4 🔴 Outright internal contradiction — the WWOX↔TPC6AΔ dissociation

Abstract:
> "…[in vitro] analysis revealed that TGF-β1 induces dissociation of the ectopic complex of TPC6AΔ and WWOX in cells…"

Discussion, summary paragraph:
> "We determined that TGF-β1 causes dissociation of WWOX from TPC6AΔ, thus leading to the aggregation of TPC6AΔ and TIAF1 and subsequent events including activation of caspases, and Aβ production."

Discussion, **two paragraphs later**:
> **"Whether TGF-β1 regulates the binding of WWOX with TPC6AΔ is unknown and is being determined in this laboratory."**

These cannot both be true. The paper asserts the dissociation twice as a result and once as an open question, within the same Discussion.

Further: **no binding assay is reported anywhere in the delivered Results or Methods.** There is no co-immunoprecipitation, no pull-down, no FRET-binding experiment in the Methods. The only FRET use is morphological — "By time-lapse FRET microscopy, generation of cytosolic TPC6AΔ aggregates (see puncta) occurred" — which images puncta, not interaction. The Introduction states the interaction as established prior work — "We showed that TPC6A physically interacted with tumor suppressor WW domain-containing oxidoreductase" — with the citation destroyed by the extractor.

⚠️ **Honest limit:** the interaction and dissociation data may live in the supplementary figures, which were delivered as an empty heading (§ 0). The prose pointers "Data are provided to show the production of our homemade antibodies ()" and "the validity and protein aggregation are shown under various experimental conditions (and)" confirm supplementary material exists. **I have not seen it and make no claim that it is absent from the paper as published.** What I can state with certainty is that the paper's own Discussion calls the regulation "unknown", which no supplementary figure can undo.

### 5.5 ⚠️ "Ectopic" declared once, dropped once

The Abstract is commendably explicit about the complex being ectopic — "the **ectopic** complex of TPC6AΔ and WWOX" — and then drops the qualifier for the very next experiment:

> "Similarly, knockdown of WWOX by siRNA resulted in dramatic aggregation of TPC6AΔ."

The body keeps the qualifier: "**ectopic** TPC6AΔ and TIAF1 became aggregated by greater than 80% of cells". A reader of the Abstract alone would take this as endogenous TPC6AΔ in a neural cell; it is an EYFP fusion in a monkey kidney fibroblast line.

### 5.6 ⚠️ Splicing asserted as fact in the Abstract, predicted in the body

Abstract: "We isolated an [N]-terminal internal deletion isoform, TPC6AΔ, **derived from alternative splicing** of the [TRAPPC6A] gene transcript."
Body: two web tools "**predicted**" the alternative donor site; the protein data "**supports** the occurrence of alternative splicing". No junction was sequenced (§ 1).

### 5.7 ⚠️ An unmeasured link in the Abstract's closing causal chain

Abstract: "…becomes aggregated for causing caspase activation that **leads to Tau aggregation** and Aβ formation."
No experiment in the paper connects caspase activation to Tau aggregation. The Tau data is one panel of pT181 counts in *Wwox*-null mice, in which caspase activity is never measured. The Aβ link is measured only in ECFP-TPC6AΔ-overexpressing SK-N-SH cells.

### 5.8 What the Abstract does **not** overstate

For balance: the Abstract's claim that "TPC6AΔ proteins are present as aggregates or plaques in the extracellular matrix of the brain such as in the cortex" is a fair restatement of the IHC prose, and the Abstract's framing of the KO result as "**suggesting** a role of WWOX" is appropriately hedged even though the underlying measurement is weaker than stated. The Ser35-dependence claim is also fairly transmitted — the body's "the S35G mutant of TPC6AΔ significantly lost its capability in aggregation and did not activate caspase 3" matches "Ser35 phosphorylation-dependent polymerization", within the overexpression system both describe.

---

## 6 · Does anything in this paper require WWOX?

**Classification: WWOX-INHIBITORY for *aggregation only*, on a single-lab, ectopic, non-neural basis — with the *in vivo* arm UNCLEAR and the *formation* and *toxicity* steps WWOX-INDEPENDENT as measured.**

Decomposing the node into its three sub-claims, because they do not classify together:

| Sub-claim | Is WWOX manipulated? | Classification | Basis |
|---|---|---|---|
| **TPC6AΔ *formation*** (the splicing event) | 🔴 **No. WWOX is never manipulated in any splicing experiment.** | **WWOX-INDEPENDENT as measured** — indeed untested. The isoform was cloned from TGF-β1-treated U937 cells with no WWOX perturbation at all. | § 1 |
| **TPC6AΔ *polymerisation / aggregation*** | ✅ Yes — siRNA knockdown (COS7) and *Wwox* −/− mouse | **WWOX-INHIBITORY** — WWOX restrains it | Fig 6; Fig 5 |
| **TPC6AΔ *toxicity*** (caspase 3, Aβ) | 🔴 **No.** All caspase-3 and Aβ experiments were run in SK-N-SH cells with **normal endogenous WWOX**, manipulating only TGF-β1 and the TPC6AΔ construct. | **WWOX-INDEPENDENT-DOWNSTREAM** — toxicity followed aggregation in WWOX-competent cells | Fig 4 |

The WWOX-inhibitory evidence, verbatim (Results, "Knockdown of WWOX by siRNA induces aggregation of TPC6AΔ and TIAF1"):

> "When WWOX was knocked down by siRNA (WOX1si), ectopic TPC6AΔ and TIAF1 became aggregated by greater than 80% of cells (~100 cells counted; Figure). In appropriate controls, no aggregation (0%) was observed with EYFP alone in the presence of WOX1si or WWOXsi or scramble. Also, when cells were transfected with a 'scramble DNA' construct, less than 10% protein aggregation was shown for TIAF1 and TPC6A (Figure)."

> "Together, the aforementioned observations are in parallel with the results from the mouse [Wwox] knockout model, suggesting that without WWOX [and WOX1], TPC6A and TIAF1 start to polymerize or aggregate."

**This is the paper's real finding and it should be stated at its true strength: >80% versus <10% is a large effect with an internal EYFP-only control at 0%.** It is also: one cell line (COS7 — monkey kidney fibroblast, not neural, not human), one transfection window (24 h), an EYFP fusion rather than endogenous protein, manual scoring of ~100 cells, no knockdown-efficiency quantification reported in the delivered text, and no rescue arm (WWOX re-expression reversing the aggregation). A rescue would have converted this from suggestive to strong; it was not done.

**The *in vivo* arm is UNCLEAR, not supporting.** As established in § 5.3, the *Wwox* −/− mouse shows TPC6AΔ extracellular aggregates, but the delivered text reports **no wild-type comparison for TPC6AΔ**. Without that contrast, "*Wwox* −/− brains contain TPC6AΔ plaques" does not establish that *Wwox* +/+ brains do not. I hold this as UNCLEAR under D-14 rather than scoring it either way.

**Is TPC6AΔ formation WWOX-dependent? No evidence, and a reason to doubt.** The isoform was isolated from U937 monocytic cells — WWOX-competent, non-neural, treated with TGF-β1. The EST evidence (13/55 human cDNAs) comes from public databases with no WWOX status attached. Nothing in this paper suggests WWOX influences whether the Δ transcript is made; the claim is only that WWOX influences whether the protein, once made, stays soluble.

---

## 7 · Direction of effect for a loss-of-function genotype

**Answer: the mechanism, as measured, gets WORSE when WWOX protein is scarce. The authors state this unambiguously and repeatedly.**

Verbatim:

> "When WWOX was knocked down by siRNA (WOX1si), ectopic TPC6AΔ and TIAF1 became aggregated by greater than 80% of cells…" (Results, Fig 6)

> "…suggesting that without WWOX [and WOX1], TPC6A and TIAF1 start to polymerize or aggregate." (Results, Fig 6)

> "WWOX is frequently downregulated in the hippocampi of AD patients, suggesting that **WWOX is crucial in preventing the aggregation of TPC6AΔ and Tau**." (Discussion)

> "We found that knockout [Wwox] −/− MEF cells are prone to possess aggregates of TPC6A, TIAF1, JNK1 and upregulated expression of β-secretase and Tau tangles (**data not shown**), suggesting a role of WWOX in stabilizing proteins and blocking their aggregation." (Discussion)

> "Importantly, we demonstrated the presence of TPC6A plaques and pT181-Tau aggregates in the cortex of [Wwox] −/− mouse brain. [Wwox] −/− mice can only survive for one month. **That is, plaques quickly form in less than a month.**" (Discussion)

> "The likely scenario is that **WWOX may act as a chaperone**, which stabilizes proteins from misfolding and being degraded by the ubiquitin/proteasome system." (Discussion, closing)

**Direction, stated for the reference genotype.** Less WWOX protein → more TPC6AΔ polymerisation. For a WWOX-DEE genotype class — severe biallelic loss of function — this paper's direction of effect is **adverse**: it predicts increased aggregation of at least one client protein, with a stated time constant of weeks rather than decades in the murine null.

**Four caveats that must travel with that direction, or the direction will be over-read.**

1. **The MEF result is "data not shown."** The single sentence most directly describing an endogenous, genetic, loss-of-function consequence carries no figure at all.
2. **The mouse is a complete null that dies at ~1 month.** "The mice can only survive for about a month." Aggregates appearing in an animal in terminal systemic collapse are not cleanly attributable to a cell-autonomous chaperone deficit; a dying-animal confound is not addressed.
3. **The frame of the whole paper is Alzheimer's disease, not developmental encephalopathy.** Every human sample is an aged AD or aged-control hippocampus; the mouse readouts are pT181-Tau and extracellular plaques. Whether a proteostatic vulnerability that manifests as plaque formation in an AD frame is the same lesion that produces early-onset epileptic encephalopathy is **not addressed by this paper and must not be assumed**.
4. **The "WWOX is downregulated in AD" premise is not measured here as total protein.** This paper's own human measurement is of *aggregated Tyr33-phosphorylated* WWOX — "the levels of protein aggregates for Tyr33-phosphorylated WWOX (p-WWOX) were significantly reduced by ~40% in the AD samples" — which is a different quantity from WWOX abundance, in an age-confounded comparison (§ 3). The downregulation premise is carried by citation to the lab's own prior work, and the citation was destroyed by the extractor.

---

## 8 · Editorial venue

*Oncotarget*, volume 6, issue 6, 2015. Open access, CC BY 2.5.

I record this as **a weight on the prior, not as an argument**. *Oncotarget* in 2015 was a high-volume journal that subsequently became the subject of indexing controversy; that history bears on how much unreplicated weight a single paper from it should carry, and on nothing else. It is not evidence about this paper's contents, and **no finding in §§ 1–7 above rests on it.** Every criticism in this audit is sourced to a quotation from the paper itself and would stand unchanged if the paper had appeared anywhere.

Two structural observations that do more work than the venue does, and should be preferred to it in any downstream reasoning:

- **Both authors are from the same group** (Chang J-Y and Chang N-S), and the paper is the founding member of a self-referential series: the Introduction and Discussion cite the group's own TIAF1, WWOX–GSK-3β and WWOX–MEK1 work throughout, and the human tissue, the antibodies and the assays are all continuous with that series.
- **The received/accepted dates were not delivered by the extractor**, so I cannot comment on review turnaround, and I decline to speculate about it.

---

## 9 · What this does to the node-independence status of TPC6AΔ

This is the section the batch was queued for, and the answer is a downgrade on two axes.

### 9.1 TPC6AΔ and TIAF1 are not independent nodes. They are one node.

The Wave-2 node-independence work treats TPC6AΔ and TIAF1 as separate mechanistic nodes in the Chang/NCKU cascade. This paper shows they cannot be counted separately, because they share every source of error:

| Shared component | Evidence from this paper |
|---|---|
| **Same laboratory** | Chang J-Y & Chang N-S, NCKU |
| **Same human tissue** | "obtained from the Department of Pathology, University of Colorado Health Sciences Center (by Dr. CI Sze, before 2005)" — the same bank as the prior TIAF1 filter-retardation work, which the paper explicitly invokes: "By filter retardation assay, we have recently demonstrated the presence of water-insoluble TIAF1 aggregates in the hippocampi of nondemented humans at 40–75 years old" |
| **Same assay and same membranes** | TPC6A, TIAF1, p-WWOX, NFT and Aβ were probed on the *same* filter-retardation preparations: "Western blotting was then carried out using specific antibodies for TPC6A (pan-specific), TIAF1, Tyr33-phosphorylated WWOX (p-WWOX), NFT and Aβ" |
| **Same result** | "Similar results were observed with TIAF1 aggregates" |
| **Same overexpression system and same figure** | Fig 6 runs EYFP-TPC6AΔ and EYFP-TIAF1 side by side in COS7 under the same siRNA |
| **Same in-house antibody practice** | peptide-competition validation, no genetic control, for both |

Two measurements on the same specimens, by the same hands, with the same unvalidated reagent class, on the same membrane, are **one observation reported twice**. Counting TPC6AΔ and TIAF1 as two corroborating nodes double-counts a single line of evidence. **Recommended status change: merge to a single node, "Chang proteostatic-aggregation axis," with corroboration weight of one.**

### 9.2 TPC6AΔ does not clear the bar for an independent mechanistic node in its own right

Independence requires, at minimum, that the entity exist outside the lab that described it. On the delivered evidence:

- **The transcript** has independent support — 13 of 55 human ESTs carry the 42-bp deletion. That is a genuine external datum, though a 2015 EST census is weak by current standards and was not re-derived here.
- **The protein** has **no independent support in this paper**. Its detection depends entirely on four rabbit antisera made by this lab and validated only by competition with their own immunising peptides (§ 2). No mass spectrometry, no commercial or second-source antibody, no orthogonal detection.
- **The plaque phenotype** — the paper's title claim — is IHC with those same antisera.
- **The causal role** is ectopic overexpression (§ 4).

**Recommended status: SINGLE-LAB, UNCORROBORATED. Not promotable to a consolidated baseline claim on this paper.** The node may be real; this paper does not establish it.

### 9.3 What would raise it, in order of decisiveness

1. **A genetic negative control for the antibodies.** *TRAPPC6A* knockdown or knockout material in which the 17-kDa band and the plaque staining disappear. This is the single cheapest experiment that would change the verdict, and the lab possessed the siRNA reagent in this very paper.
2. **Junction-spanning RT-PCR, sequenced, from human brain.** Converts a prediction into an observation, and would also fix § 1.
3. **A WWOX re-expression rescue** of the siRNA aggregation phenotype in Fig 6.
4. **A wild-type-versus-*Wwox*-null contrast for TPC6AΔ**, quantified as the Tau panel already is.
5. **Independent detection of TPC6AΔ peptide by mass spectrometry** in any human brain proteomics dataset — including, critically, whether the neo-junction peptide is represented in any public resource. This is checkable outside the paper and should be queued.
6. **A non-NCKU replication** of the plaque phenotype on a different tissue bank.

### 9.4 Standing caveat for the reference genotype

Everything above concerns a proteostatic mechanism described in an **Alzheimer's disease** frame, using aged human hippocampus and an AD-transgenic mouse. The reference WWOX-DEE genotype class is a developmental, early-onset, biallelic loss-of-function condition. The **direction** of the WWOX effect (§ 7) is concordant — less WWOX, more aggregation — but the **relevance** of an AD-plaque readout to DEE pathophysiology is an open transfer question that this paper neither asks nor answers, and it should not be closed by inheritance from this node.

---

**Author:** Scientist A. **Date:** 2026-09-21. **Mode:** READ-ONLY — no canonical file modified; no registry, queue, ledger or current file touched; no commit candidate produced.

**Declared limits.** (1) 🔴 **No figure image was inspected** — no panel of Figures 1–6 was viewed, and no supplementary figure was available (the `SUPPLEMENTARY FIGURES` heading was delivered empty). Per **D-14**, no negative asserted only by a figure is adjudicated here; the two places where that limit bites are marked in § 5.3 and § 2. (2) 🔴 **The extraction defect is PRESENT and severe** — every italicised token was silently deleted, including all gene symbols (`TRAPPC6A` and `Wwox` as gene symbols occur zero times in the delivered body, which is an instrument reading and not a fact about the paper), all three GenBank accession numbers, the italic *n*, *P* and *t* in every statistic, *in vitro* / *in vivo*, and all 37 inline figure cross-references; the entire reference list was destroyed, so no citation in this paper is identifiable. (3) All quotations above are verbatim from the persisted artefact `files/fulltext/PMID25650666_PMC_MCPtext.txt`; square brackets mark the only editorial insertions, which restore extractor-deleted italic tokens and are never silent.
