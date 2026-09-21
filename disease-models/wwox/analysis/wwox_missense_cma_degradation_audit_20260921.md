# Audit — PMID 41124647: does a missense WWOX allele become null by chaperone-mediated autophagy?

**Source.** PMID 41124647 · PMCID PMC12767083 · DOI 10.1002/advs.202507602 · *Advanced Science* (Weinheim), 2025, vol. 13, issue 1, e07602.
**Title (as PubMed records it).** "Genetic and Functional Evidence Links Germline Biallelic Inactivating Variants in WWOX to Histological Mixed-Type Thyroid Cancer."
**Artefact audited.** `files/fulltext/PMID41124647_PMC_MCPtext.txt` — 69,809 bytes / 68,491 characters, sha256 `7ba05197fc4a49ad00c15d06c101480d2cdeab25f0e1aecd73283763241b6937`, body text only, verbatim from `mcp__PubMed__get_full_text_article` on PMC12767083.
**Licence.** `get_copyright_status` returns: statement "© 2025 The Author(s). Advanced Science published by Wiley-VCH GmbH.", holder "authors", `license.type: null`, `license.url: null`, `is_open_access: false`, `found_in_pmc: 0`. The article is in PMC and the body was retrievable; the API reports no machine-readable licence type. Treat as author-copyright with unspecified reuse terms — quote, do not redistribute the artefact.

---

## VERDICT

**PARTIAL — the paper establishes that one missense WWOX allele (P252A) is lost post-transcriptionally by lysosome-dependent degradation and that the mutant protein binds HSC70, and it names a step that is blockable *pharmacologically at the protein-level readout* (chloroquine 40 µM / NH4Cl 250 µM, 24 h, CAL-62 cells, restoring mutant protein but with no functional rescue tested); it does NOT establish chaperone-mediated autophagy as the route, because the KFERQ-like motif is identified by sequence inspection only and is never mutated, and LAMP2A — the defining CMA receptor — is neither knocked down, overexpressed, nor mentioned anywhere in the paper.** The reason the verdict is not stronger is that "lysosome-dependent" and "chaperone-mediated autophagy" are separated by exactly the experiments the paper did not do, and the paper's own Results say so in the subjunctive ("we speculated", "likely exposes").

---

## 0 · Identifier and subject verification (the census claim, checked)

The census description was **substantially correct but imprecise in one way that matters**. Correct: CAS Hefei group; germline missense WWOX variants; accelerated degradation attributed to chaperone-mediated autophagy; KFERQ-like motif at residues 187–191; HSC70. Imprecise: the variants are **homozygous**, not compound heterozygous, and only **one of the two** (P252A) is the degraded one — the census's singular "WWOX mutant" is right but its referent is invisible in extracted text because the superscript variant labels are deleted by the extractor. The census's verbatim sentence is genuine and appears in the paper's concluding Discussion paragraph:

> "Mechanistically, WWOXmutant undergoes accelerated degradation via chaperone‐mediated autophagy in the lysosome, directly linking protein instability to loss‐of‐function."
> — Discussion, final summary paragraph. (The deleted superscript is "P252A".)

No mismatch of identifiers or subject. Proceed.

### Instrument state (mandatory declaration)

The extraction defect **is present and severe in this article**, and it is visible in the title itself: PMC returns the title as "Genetic and Functional Evidence Links Germline Biallelic Inactivating Variants **into** Histological Mixed-Type Thyroid Cancer" — the italic gene symbol *WWOX* between "in" and "to" has been deleted. Consequences for this audit:

- Every italicised gene symbol is gone: "The gene encoding(WW domain-containing oxidoreductase)", "Thegene is located within the FRA16D chromosomal region", "germline homozygousvariants".
- Every **superscript** variant label on a protein name is gone: "WWOXand WWOXmutants", "the WWOXmutant protein". Attribution of each result to P252A or P282A therefore had to be recovered from the surrounding roman-type sentences, which do survive (e.g. "These results suggest that the P252A mutation causes rapid degradation of WWOX protein through a lysosome-dependent pathway").
- Bare "P252A" survives 28 times and "P282A" 25 times in roman type; these counts are reliable. Superscripted occurrences are not counted at all.
- Inline figure and reference cross-references arrive as empty parentheses: "(Figure)", "(Figure, Supporting Information)". Panel letters are lost, so no locator in this audit can name a panel.
- Italic *P* in p-values is deleted: "< 0.05 was considered as statistical significance (< 0.05,< 0.01,...)"; units lose italic/superscript ("50 µg mLCHX", "20 µ, 6 h", "NHCl" for NH4Cl).
- **Contrary to the standing warning, figure legends were NOT dropped** in this extraction: full legends for Figures 1–6 are present, and several load-bearing details (drug concentrations, exposure times, n, tests) exist only there. Tables and the reference list are absent.
- **Counts used as evidence below are all roman-type method words** (LAMP2A, bafilomycin, siRNA, blinded, randomised). Zeros for those are informative. No zero for a gene symbol or an italicised token is used as evidence anywhere in this file.
- **No figure image was inspected.** Per rule D-14, no negative asserted only by a figure is adjudicated here.

---

## 1 · What the paper is about, and its disease context

It is a **cancer paper**, framed end to end as oncology. It is a single-proband germline-variant report plus cell-line and xenograft functional work.

> "A 35‐year‐old Chinese male patient was admitted to The First Affiliated Hospital of USTC (University of Science and Technology of China) on November 6, 2015, presenting with a large mass in the right neck region"
> — Results 2.1.

> "Finally, the tumor in the right neck region of the patient was diagnosed as a thyroid mixed tumor of papillary and anaplastic carcinoma." … "The patient passed away two years after diagnosis."
> — Results 2.1.

The variants are **germline**, confirmed in non-tumour tissue and segregating in the family:

> "By Sanger sequencing, we further confirmed the homozygosity of the twogermline variants using the genomic DNA from the adjacent muscle normal tissue of the patient's tumor. In addition, the son of the patient harbored heterozygous alleles and had no cancer phenotype. The wife of the patient harbored wild‐type alleles"
> — Results 2.1.

They are germline **in a patient**, and then **engineered** for every functional experiment: all functional work is stable **over-expression** of Flag-tagged WT / P252A / P282A / P252A+P282A constructs in CAL-62 and BCPAP thyroid cancer cell lines, plus transient transfection in HEK293T, plus CAL-62 nude-mouse xenografts. No patient-derived cell line, no knock-in, no endogenous-locus model.

> "CAL‐62 and BCPAP cells were transfected with pCMV‐Flag empty vector, pCMV‐Flag‐WWOX, pCMV‐Flag‐WWOXand pCMV‐Flag‐WWOXvectors."
> — Experimental Section, "The Generation of Cell Lines with Stable Expression of Wild-Type and Mutant WWOX".

---

## 2 · Which variants, exactly, and where in the protein

Two germline homozygous missense variants:

> "In the study, by whole‐exome sequencing (WES), we identified two germline homozygousvariants (p.P252A and p.P282A) in a young male presenting with a histological mixed‐type thyroid cancer (co‐existing papillary and anaplastic carcinoma)."
> — Introduction, final paragraph.

> "Integrative Genomics Viewer (IGV) displayed that the variant was located on exon 7 in thegene, resulting in a homozygous C‐to‐G missense variant (:c.C754G:p.P252A). Besides the P252A variant, WES identified the other homozygous variant in thegene that was located on exon 8, resulting in a C‐to‐G missense variant (:c.C844G:p.P282A)"
> — Results 2.1.

So: **c.754C>G p.(Pro252Ala)**, exon 7; **c.844C>G p.(Pro282Ala)**, exon 8. P282A is a known common SNP:

> "Case‐control association studies have revealed that a single nucleotide polymorphism (SNP) rs3764340 (p.P282A) was associated with a higher risk of cervical, thyroid, esophageal, and lung cancers."
> — Introduction.

**Domain position.** Residues 252 and 282 both fall within the SDR / short-chain dehydrogenase-reductase (ADH) domain (conventionally ~aa 121–330), well clear of the two WW domains (~aa 1–100). **This is my placement, not the paper's.** The paper never uses "SDR", never uses "ADH", never uses "short-chain": these are roman-type strings and their counts are 0, 0 and 0 respectively, which is an informative negative. The only domain vocabulary in the whole body is the gene-name expansion "(WW domain-containing oxidoreductase)" in the Introduction and one citation-borrowed "WWOX, via its WW1 domain, interacts with ATM" in the Discussion. A domain schematic exists as Figure 1D — "Schematic diagram for the locations of P252A and P282A variants in thetranscript (top panel) and WWOX protein (bottom panel)" — but it is an image and was not inspected (D-14).

**Relevance to this repository.** Both variants sit in the same domain as the reference genotype's missense allele. That is a genuine structural adjacency and the main reason this paper is worth reading here. It is not more than adjacency: neither variant is the reference allele, and neither is a WOREE allele.

The paper does mention the WOREE missense variants in passing, once, with no data:

> "The missense variants (P47R, Q230P, and G137E) were also observed in WOREE syndrome individuals."
> — Introduction. (Q230P appears exactly once in the body; there is no experiment on it.)

🔴 **And nothing in this paper may be carried across to `Q230P`'s protein-loss mechanism, which
remains unresolved.** The canonical record for that allele — `DL-MECH-029`, `CLAIM 019`
(`consolidated baseline`) and `HYP-20260709-08` — holds **normal transcript with protein not
detected**, and Johannsen's own reading of it is *"**impaired translation** or premature
degradation"*: **two competing causes, neither discriminated by anyone.** A third possibility,
**insolubility** rather than loss, is also live and equally untested, because a western blot of a
soluble fraction cannot see a protein that has partitioned into an insoluble one.

**What `P252A` demonstrates is that the degradative branch is REAL FOR SOME SDR-span missense
substitution — not that it is the branch `Q230P` takes.** Reading this paper as settling `Q230P`
would collapse `impaired translation | premature degradation | insolubility` into `degradation`,
which is precisely the conflation the canonical record refuses to make and which the
`test_q230p_protein_loss_cause_remains_unresolved` guard exists to catch. ⚠️ **The distance is
also large in every other dimension** — a thyroid-cancer line, a stably over-expressed Flag
transgene, no knock-in, no patient-derived material, and a different substitution at a different
residue. The transferable object is **a mechanism class and a diagnostic question**, and the
question is the one already written into `HYP-20260709-08`: *is the protein synthesised at a normal
rate and degraded prematurely, is synthesis reduced, or is it made and insoluble?* A
lysosomal-inhibitor arm is now worth adding to that discrimination — **as one arm of it, not as its
answer.**

---

## 3 · The KFERQ-like motif

The paper locates one, gives a sequence and residues, and **never tests it**.

> "In chaperone‐mediated autophagy (CMA), cytosolic chaperone HSC70 recognizes substrate proteins by binding to their KFERQ‐like motif, leading to their translocation into the lysosome for degradation.Since the KFERQ‐like motif (LRSVQ at 187‐191 amino acids) exists on WWOX, we speculated that lysosomal degradation of WWOXmutant protein occurred through chaperone‐mediated autophagy."
> — Results 2.3.

> "The KFERQ‐like motif (LRSVQ, amino acids 187‐191) in WWOX is situated in close proximity to the site of the P252A variant."
> — Discussion.

**Identified by sequence inspection only.** The motif is never mutated, never deleted, never transplanted. "LRSVQ" occurs twice in the entire body, both in the sentences quoted above; there is no mutagenesis section for it, and the Experimental Section's mutagenesis paragraph lists only "P252A, P282A single and double mutations". **A motif-ablation experiment is the standard test that the motif is the recognition element, and it was not done.**

**HSC70 binding is measured, not merely asserted** — by co-IP, in both directions of the comparison:

> "As shown in Figure, co‐immunoprecipitation (co‐IP) revealed an interaction between HSC70 and WWOXmutant protein, but not wild‐type WWOX protein and WWOXmutant protein."
> — Results 2.3.

> "Co‐IP analysis of protein interaction between WWOX and HSC70. Cell lysates of CAL‐62 cells with stable over‐expression of Flag‐tagged wild‐type (WWOX) or mutant WWOX (WWOXor WWOX) were immunoprecipitated with anti‐FLAG antibody, followed by western blot with anti‐HSC70 antibody."
> — Figure 4I legend.

This is an over-expression co-IP with endogenous HSC70 detected; no proximity assay, no reciprocal IP of endogenous HSC70, no recombinant binding. The link from "HSC70 binds the mutant" to "HSC70 binds *this motif*" is not made experimentally. The bridge the paper offers is docking:

> "The docking results showed that compared with wild‐type WWOX, the P252A mutation enhanced the binding energy of WWOX to HSC70" … "Therefore, conformational change in WWOXmutant likely exposes the KFERQ‐like motif for HSC70 binding."
> — Results 2.4 and Discussion. In silico, and voiced as "likely".

Note also that 187–191 and 252 are 61 residues apart in linear sequence; "close proximity" is a claim about folded structure supported only by the PyMOL/CASTp/docking work, not by any structure determined here.

---

## 4 · The degradation claim — what exists and what does not

**Present:**

1. **mRNA control, to make the loss post-transcriptional.**
> "In CAL‐62 cells over‐expressing WWOX, WWOXand WWOX, WWOX mRNA levels showed a remarkable induction compared with empty vector‐transfected cells, while the mRNA level of WWOXmutant was not decreased ()." … "Thus, we hypothesized that the reduced expression of the WWOXmutant resulted from accelerated turnover rather than an impairment in transcription."
> — Results 2.3. (Note the mood: "we hypothesized".)

2. **Cycloheximide chase.**
> "The results demonstrated that the WWOXmutant exhibited significantly enhanced protein degradation, compared to its wild‐type counterpart and the WWOXmutant"
> — Results 2.3. Method: "cells were treated with 50 µg mLCHX … and cell protein lysate was collected at 0, 2, 4, 6, 8, and 10 h post‐treatment" (Experimental Section). **No half-life value is reported anywhere.** The string "half-life" occurs once in the entire body, in the Methods sentence stating the intent ("To determine the half-life of wild-type WWOX and the two mutated WWOX proteins, a CHX chase assay was performed"). The quantity the assay was performed to obtain is never given in the text; if it is in a figure, it was not inspected (D-14).

3. **Proteasome-inhibitor control, negative — this is the load-bearing exclusion.**
> "We found that the proteasome inhibitor, MG‐132 treatment, did not induce the accumulation of WWOX, WWOX, and WWOXproteins (Figure)."
> — Results 2.3. Concentration from Figure 4C legend: "Treatment of proteasome inhibitor MG‐132 (20 µ, 6 h)" (the "M" of µM is deleted by the extractor; read as 20 µM).

4. **Lysosomal inhibitors, positive.** See §6 below — chloroquine and NH4Cl.

5. **Autophagosome inhibitor, negative — the step that narrows "lysosomal" toward "non-macroautophagic".**
> "whereas no significant effect was observed upon treatment with autophagosome inhibitor 3‐methyladenine (3‐MA)"
> — Results 2.3. Figure 4F legend: "3‐MA (10 m, 12 h)" (read as 10 mM).

6. **Combined CHX + CQ.**
> "Furthermore, CQ prevented the degradation of WWOXmutant protein in the presence of CHX (Figure, Supporting Information)."
> — Results 2.3.

7. **Ubiquitin chain typing.**
> "The level of polyubiquitylation chain was stronger in the WWOXmutant protein, compared to wild‐type and WWOXmutant proteins" … "we found that the K63‐linked ubiquitin was the predominant form" … "a K63R mutant type of ubiquitin reduced the polyubiquitination of the WWOXmutant protein."
> — Results 2.3.

8. **Lysosomal co-localisation by immunofluorescence, with LAMP1.**
> "Immunofluorescence analysis indicated that the WWOXmutant protein was transferred to lysosomes, displaying co‐localization with lysosomal marker LAMP1 (Figure)."
> — Results 2.3. The Figure 4J legend is notably weaker than the Results sentence: "Immunofluorescence shows that the WWOXmutant protein **has a trend to be transferred to lysosomes**." Same experiment, two strengths of claim, in the same paper.

**Absent:**

- **LAMP2A: zero occurrences.** "LAMP2A", "LAMP-2A", "LAMP‐2A" and "LAMP2" all return 0 in the body — roman-type strings, so this is an informative negative, not an instrument reading. There is no LAMP2A knockdown, no LAMP2A over-expression, no LAMP2A blot. The lysosomal marker used is LAMP1 (2 occurrences), which marks lysosomes generally and is not the CMA receptor.
- **HSC70/HSPA8 knockdown or inhibition: none.** HSC70 appears 13 times, all in the co-IP, docking and discussion context; there is no loss-of-function test of HSC70.
- **Bafilomycin A1: zero occurrences.**
- **KFERQ-motif mutagenesis: none** (see §3).
- **Isolated-lysosome uptake assay, CMA reporter (e.g. KFERQ-PS-Dendra), lysosomal protease inhibitors: none.**

**Reading.** Points 1, 2, 3, 4, 5 and 6 together establish, at a respectable standard, that **P252A WWOX protein is lost post-transcriptionally, faster than wild type, by a route that is lysosome-dependent, MG132-insensitive and 3-MA-insensitive.** That is a real and useful result. Points 7, 8 and the HSC70 co-IP are *consistent with* CMA. But the specific claim "via chaperone-mediated autophagy" rests on: a motif found by inspection, a co-IP, a LAMP1 co-localisation described as "a trend" in its own legend, and docking — with the CMA receptor LAMP2A never touched. **"Degraded faster by a lysosomal route" is shown. "Degraded faster by CMA" is inferred.** The paper's own Results sentence is explicit about which of the two it is doing: "we speculated that lysosomal degradation … occurred through chaperone-mediated autophagy."

---

## 5 · Is the protein-level loss shown to be a FUNCTION loss?

**Yes — functional loss is shown independently of, and more thoroughly than, the stability result.** Stability is not the only readout. For both mutants:

> "when WWOXor WWOXmutant was stably expressed in CAL‐62 and BCPAP thyroid cancer cells, the two mutants were not able to inhibit colony formation" … "the over‐expression of wild‐type WWOX inhibited the growth of thyroid cancer cells, but WWOXor WWOXmutants lost the ability to inhibit growth" … "the inhibition of cell invasion was not observed in CAL‐62 and BCPAP cells stably overexpressing WWOXor WWOXmutant" … "wound healing assay revealed that the over‐expression of wild‐type WWOX was able to inhibit cell migration significantly in both thyroid cancer cells, but this inhibitory effect was not observed in the WWOXor WWOXmutant cells"
> — Results 2.2.

> "over‐expression of wild‐type WWOX significantly suppressed tumor growth in vivo, compared with the group of empty vector (). However, the WWOXor WWOXmutant did not have the inhibitory effect on tumor growth"
> — Results 2.2 (xenografts).

> "Stable expression of wild‐type WWOX significantly attenuated UV‐induced tail moment in CAL‐62 and BCPAP cells; in contrast, cells expressing the WWOXor WWOXmutant exhibited DNA damage levels similar to the empty vector control ()." … "the over‐expression of wild‐type WWOX increased the repair efficiency of NHEJ, while the repair efficiency of NHEJ in CAL‐62 cells stably expressed with WWOXor WWOXmutant was the same as that in CAL‐62 cells stably expressed with an empty vector."
> — Results 2.4 (comet assay; γH2AX foci; I-SceI/EJ2GFP NHEJ reporter).

**The important caveat is causal, not evidential.** For P252A, the functional assays and the stability defect are confounded: there is less mutant protein, so "no tumour-suppressive activity" and "not enough protein" are not separated. The paper says so itself about the POLE4 interaction —

> "The interaction between POLE4 and the WWOXmutant was also markedly reduced, likely due to the low abundance of the unstable WWOXmutant (Figure, Supporting Information)."
> — Results 2.4

— and it asserts the causal direction for tumour suppression without an experiment that separates them:

> "The impaired expression of WWOXmutant directly correlated with a marked attenuation of its tumor‐suppressive capacity."
> — Discussion. "Directly correlated" is a correlation word doing causal work.

For **P282A**, by contrast, function is lost **without** a stability defect — its protein level is not reduced — which makes it a clean intrinsic-function mutant, mechanistically attributed to loss of POLE4 binding.

---

## 6 · Is there any rescue? (the therapeutically load-bearing question)

**Yes, at the protein-level readout only, with two lysosomotropic agents in one cell line. No functional rescue is tested.**

> "Importantly, lysosome inhibitors, chloroquine (CQ) and NHCl treatment, restored WWOXprotein level (Figure)"
> — Results 2.3. ("restore" occurs exactly once in the whole body; this is it.)

Concentrations and system, from the figure legends (the only place they exist):

> "Treatment of CAL‐62 cells stably overexpressing wild‐type or mutant WWOX proteins with the lysosome inhibitor chloroquine (CQ; 40 µ, 24 h) induces accumulation of WWOXmutant protein."
> — Figure 4D legend (read as 40 µM).

> "Treatment of CAL‐62 cells stably overexpressing wild‐type or mutant WWOX proteins with the lysosome inhibitor NHCl (250 µ, 24 h) induces accumulation of WWOXmutant protein."
> — Figure 4E legend (read as 250 µM NH4Cl).

> "Furthermore, CQ prevented the degradation of WWOXmutant protein in the presence of CHX (Figure, Supporting Information)."
> — Results 2.3.

**Stated exactly as it is: this is chloroquine at 40 µM and ammonium chloride at 250 µM for 24 hours, in a single anaplastic thyroid carcinoma cell line (CAL-62) that is over-expressing a transfected Flag-tagged construct, read out by western blot band intensity.** 40 µM chloroquine is a cell-biology concentration used to block bulk lysosomal acidification, not a pharmacological CNS exposure. Neither agent is selective for CMA; both raise lysosomal pH and would block every lysosomal route at once. No chemical chaperone (no 4-PBA, no TUDCA, no glycerol), no HSP70/HSC70 modulator, no LAMP2A manipulation, no proteostasis drug of any kind was tried.

**And critically: nothing in the paper tests whether restored P252A protein does anything.** There is no colony-formation, invasion, comet, γH2AX or NHEJ assay under CQ or NH4Cl. So the paper shows that the mutant protein can be made to *accumulate*, and shows nothing at all about whether the accumulated protein is *functional*. Given that the paper's own Discussion attributes P282A's loss to an intrinsic binding defect rather than abundance, the possibility that P252A protein is also intrinsically impaired — and that rescuing its level rescues nothing — is live and untested. **The degradation route is blockable; the functional consequence of blocking it is unknown.**

---

## 7 · Does the paper reach any neural, developmental or non-cancer phenotype?

**No.** It is cancer-framed throughout: thyroid carcinoma histology, xenografts, TCGA, EMT, mutational signatures. "seizure" occurs 0 times. "epilep" occurs 3 times and "WOREE" 7 times, all in the Introduction and Discussion as background or speculation — never attached to data.

The only neuro-adjacent statement in the paper is an explicit speculation, and it is the single most consequential sentence here for this repository:

> "In this study, the cancer patient harboring germline homozygousP252A and P282A variants did not suffer from WWOX‐related nervous system disease. We speculate that the complete functional loss of the WWOX mutated protein is expected to lead to severe WOREE syndrome‐related phenotypes. However, WWOXand WWOXmutants may have some residual protein function to maintain the development of the neurological system."
> — Discussion.

Read carefully, this is a **clinical observation plus an inference**. The observation is hard and useful: a 35-year-old man homozygous for P252A + P282A had **no neurological disease** — he presented with thyroid cancer and died of it at 37. The inference ("may have some residual protein function") is the authors' proposed explanation, in the subjunctive, with no measurement of residual function behind it.

**What this means for citation here.** This paper may be cited for: (a) a germline missense WWOX genotype that is protein-destabilising and tumour-suppressor-dead in cell assays yet **neurologically silent in a living adult**; (b) the existence of a lysosome-dependent degradation route for a SDR-domain missense WWOX protein; (c) the CQ/NH4Cl level-restoration result, with its concentrations. It may **not** be cited as evidence about WOREE, SCAR12, seizures, or any neurodevelopmental endpoint — it contains no such data. And note the direct tension with the paper's own abstract: the abstract says "complete loss of tumor-suppressive activity", the discussion says the same alleles "may have some residual protein function". Both cannot be used at once.

---

## 8 · WWOX-dependence

**WWOX-DEPENDENT.** WWOX is the subject of every experiment, not a bystander or an upstream input. The degradation phenotype is a property of a WWOX protein variant; the co-IP partners (HSC70, POLE4) are assayed against WWOX baits; the tumour-suppression readouts compare WWOX constructs to empty vector; the EMT result is produced by WWOX siRNA.

> "Cell lysates of CAL‐62 cells with stable over‐expression of Flag‐tagged wild‐type (WWOX) or mutant WWOX (WWOXor WWOX) were immunoprecipitated with anti‐FLAG antibody, followed by western blot with anti‐HSC70 antibody."
> — Figure 4I legend.

> "Western blot indicates that knockdown of WWOX using two independent siRNAs for 48 h in CAL‐62 cells results in down‐regulation of E‐cadherin, and up‐regulation of Vimentin and Fibronectin."
> — Figure 6H legend.

Direction: **restoring or preserving WWOX is the beneficial direction** in this system (wild-type WWOX suppresses growth, invasion and migration and improves DNA repair; WWOX knockdown drives EMT and invasion). That is the same directional polarity this repository's model uses, which is why the degradation finding is relevant at all. The one asymmetry to keep in view: all of it is an over-expression system in cancer cell lines, where the direction is easy to observe and the magnitudes mean little.

---

## 9 · Abstract-versus-Results check, and grammatical mood

**Softening/overstatement IS present. Four instances, all in the same direction (abstract stronger than Results).**

1. **"via HSC70 chaperone-mediated autophagy" (abstract) vs "we speculated" (Results).** Abstract: "The WWOXmutant undergo accelerated degradation via HSC70 chaperone‐mediated autophagy in the lysosome." Results: "Since the KFERQ‐like motif (LRSVQ at 187‐191 amino acids) exists on WWOX, **we speculated** that lysosomal degradation of WWOXmutant protein occurred through chaperone‐mediated autophagy." This is the named failure mode exactly: **the source's own hypothesis, re-voiced in the abstract as the source's finding.** The Discussion does the same in the indicative: "Mechanistically, WWOXmutant undergoes accelerated degradation via chaperone-mediated autophagy in the lysosome, directly linking protein instability to loss-of-function." The intermediate mechanistic step is stated in the subjunctive throughout: "conformational change in WWOXmutant **likely** exposes the KFERQ‐like motif for HSC70 binding"; "This modification **may** enhance its interaction with HSC70".

2. **"complete loss of tumor-suppressive activity" (abstract) vs "may have some residual protein function" (Discussion).** Abstract: "both WWOXand WWOXmutants exhibit **complete** loss of tumor‐suppressive activity". The assays show mutant indistinguishable from empty vector — an assay floor, not a demonstration of completeness — and the Discussion then argues the opposite for the neurological axis. Internal inconsistency, unflagged by the authors.

3. **"POLE4 … not with the WWOX mutant" (abstract) vs "appeared to lose" (Results).** Abstract: "A nucleotide excision repair‐related protein, POLE4, is identified to interact with WWOX, but not with the WWOXmutant." Results: "the WWOXmutant **appeared to** lose its interaction with POLE4". Further, **no nucleotide excision repair assay is performed in this paper** — POLE4's NER role is carried in from citation, and the Discussion concedes it: "the functional relevance of WWOX‐POLE4 interaction in nucleotide excision repair remains to be elucidated, necessitating further investigation".

4. **"drive cancer pathogenesis" (abstract) vs "probably predisposing" (Discussion).** Abstract: "germline WWOX loss‐of‐function variants **drive** cancer pathogenesis by perturbing multiple tumor‐suppressive mechanisms." Discussion: "thereby **probably predisposing** carriers to cancer through genomic instability" — and "suggesting a driver role". The evidence base is one proband plus over-expression assays; "drive" outruns it.

**A fifth, internal to the Results:** the LAMP1 co-localisation is "the WWOXmutant protein **was transferred** to lysosomes" in the Results text but "**has a trend to be** transferred to lysosomes" in the Figure 4J legend.

**Mood summary.** The tumour-suppressor-loss claims and the lysosome-dependence claims are stated as demonstrated, and the data support that. The CMA-specific claims, the motif-exposure claim and the K63-ubiquitin-enhances-HSC70-recognition claim are stated as **proposed** in Results and Discussion, and as **demonstrated** in the abstract and the concluding paragraph. Anyone quoting the abstract or the final Discussion paragraph of this paper — which is what the census did — will import a hypothesis as a finding.

---

## 10 · Authors, laboratory, independence

Nine authors. First author **Xiaopeng Zhang**. Corresponding/senior authors are not marked in the extracted body, but the Author Contributions statement identifies the design-and-writing leads:

> "B.H., H.W., and X.Z. designed the study." … "X.Z. and B.H. wrote the manuscript. X.Z. and B.H. edited the manuscript."
> — Author Contributions.

**Senior author: Bo Hong (B.H.)**, with **Hongzhi Wang (H.W.)** as co-senior.
**Affiliation:** Hefei Cancer Hospital of CAS, Institute of Health and Medical Technology, Hefei Institutes of Physical Science, Chinese Academy of Sciences, Hefei, Anhui 230031, China; and Science Island Branch, Graduate School of the University of Science and Technology of China. One author (Ao Xu) is at the Department of Pathology, First Affiliated Hospital of USTC.

**Independence: yes, fully independent of the Chang / NCKU (Taiwan) group.** No author is affiliated with National Cheng Kung University or any Chang-lab institution; the work is entirely CAS Hefei / USTC. Competing interests: "The authors declare no conflict of interest." This is a genuinely independent line of WWOX mechanistic work, which raises rather than lowers its evidential value for this repository, since most WWOX mechanism derives from a single group.

**Methodological rigour flags.** "blind" occurs 0 times and "random" 0 times in the body (roman-type strings, informative negatives): no blinding and no randomisation is declared for the IHC scoring, the xenograft allocation, or the image quantifications. All quantitative data are "mean ± SEM from three biological replicates" with two-tailed unpaired Student's t-tests; SEM rather than SD, n = 3, and repeated pairwise t-tests without multiplicity correction across many panels. The clinical genetics rests on **n = 1 proband** (plus 25 unrelated thyroid cancer specimens for the IHC correlation and 12 for the paired scoring).

---

## 11 · What this repository may and may not now infer for a missense SDR-domain allele

**May infer.**

1. **A missense substitution in the WWOX SDR domain can abolish protein abundance post-transcriptionally while mRNA is unaffected.** This is demonstrated here for P252A with an mRNA control, a CHX chase, and two orthogonal lysosomal inhibitors, with MG132 and 3-MA negative. This is a real mechanism class to hold open for any SDR-domain missense allele: **"present in transcript, absent in protein"** is a distinct failure mode from "impaired catalytic or binding function", and the two require different interventions. Before this paper, this repository's missense-allele reasoning did not have a documented lysosomal-degradation route for WWOX.
2. **A degradation-mediated loss of a missense WWOX protein is pharmacologically blockable at the level of protein abundance** — chloroquine 40 µM or NH4Cl 250 µM for 24 h restored P252A protein in CAL-62 cells. As an **intervention point**, this is worth recording. As a **therapeutic lead**, it is at the lowest possible maturity: a non-selective lysosomotropic agent, one cancer cell line, an over-expressed construct, a western-blot readout, and no functional rescue.
3. **Two SDR-domain missense alleles, homozygous, produced no neurological disease in a 35-year-old man.** This is a clinical data point about SDR-domain missense tolerance, and it belongs in the repository's reasoning about where a missense allele sits between the pure-null and hypomorphic extremes — as evidence that *some* SDR missense alleles retain enough function for normal neurodevelopment even when biallelic and even when tumour-suppressor-dead in a cancer assay.
4. **An independent-group corroboration** that wild-type WWOX suppresses growth, invasion and migration and supports DNA repair, in the direction this repository's model already holds.

**May NOT infer.**

1. **Do not import "chaperone-mediated autophagy" as an established route.** The paper did not test LAMP2A (0 occurrences), did not mutate the KFERQ-like motif, and voiced the CMA step as speculation in its own Results. Record the finding as **lysosome-dependent, proteasome-independent, macroautophagy-independent degradation, with HSC70 co-IP and a sequence-predicted KFERQ-like motif at LRSVQ 187–191** — that is what was shown. Any downstream hypothesis targeting CMA machinery (LAMP2A, HSC70 modulators) must be tagged as resting on an untested inference from this source.
2. **Do not transfer P252A or P282A to the reference genotype's missense allele.** These are different residues, in a different clinical context, in a different assay system. Same domain is not same allele. The only thing that transfers is the *mechanism class*, as a hypothesis to test for any specific allele — and the test is specific: does the allele's protein show reduced abundance with normal mRNA, and is that abundance restored by a lysosomal inhibitor?
3. **Do not infer that blocking degradation restores function.** The paper restores protein level and never measures function under rescue. For a therapeutic argument, level-restoration is necessary and nowhere near sufficient. If the reference genotype's missense protein is intrinsically impaired as well as unstable, stabilising it buys nothing.
4. **Do not treat "the missense allele has residual function" as evidence from this paper.** That sentence is a speculation the authors offer to explain why their proband had no neurological disease. The *absence of neurological disease* is the datum; "residual protein function" is their proposed explanation, and no residual-function measurement was made.
5. **Do not cite this paper for any neurodevelopmental, seizure or WOREE/SCAR12 endpoint.** It contains none.

**The distance to state explicitly.** Between this paper's subject and this repository's reference genotype there are at least five gaps stacked: (i) somatic-tissue cancer biology vs germline neurodevelopment; (ii) homozygous for two SDR missense alleles vs compound heterozygous with one null-like splice allele; (iii) different residues; (iv) over-expressed Flag-tagged construct in a thyroid carcinoma line vs endogenous expression in developing neurons; (v) a proband who lived to 35 without neurological disease vs a severe neurodevelopmental phenotype. The useful transfer across those five gaps is **one mechanism class and one diagnostic test**, not a conclusion and not a therapy.

**The one thing this paper genuinely sharpens** is the question the repository should ask about its own missense allele, which it was not asking in this form before: **is the reference missense allele's protein present at normal abundance, or is it being degraded?** Those are different diseases at the molecular level and they have different intervention points, and this paper shows the second possibility is real for a WWOX SDR missense substitution.

---

## Declaration

Author: **Scientist A**. Date: **2026-09-21**. **READ-ONLY** session — no canonical LEGEND file, registry, queue, ledger or current file was read-modified or written. Two files were written: the verbatim full-text artefact `files/fulltext/PMID41124647_PMC_MCPtext.txt` and this analysis.

Declared limits:
- **No figure image was inspected.** All figure-derived content in this audit comes from the figure *legends*, which survived extraction. No negative asserted only by a figure image is adjudicated (rule D-14).
- **Extraction defect: PRESENT and severe.** Italic gene symbols, superscript variant labels on protein names, italic *P*, units and all inline figure/reference cross-references are deleted; tables and the reference list are absent. Figure legends were retained, contrary to the standing expectation. Every count offered as evidence in this file is a count of roman-type method words (LAMP2A 0, LAMP2 0, bafilomycin 0, blind 0, random 0, SDR 0, ADH-as-domain 0, siRNA 11, HSC70 13, KFERQ 5, LRSVQ 2, restore 1, half-life 1, seizure 0, P252A 28, P282A 25). No zero for a gene symbol or an italicised token is used as evidence anywhere above.
- **Licence:** © 2025 The Author(s), Advanced Science published by Wiley-VCH GmbH; `get_copyright_status` reports no machine-readable licence type and `is_open_access: false`. Quotation for audit purposes only.
- **Supplementary material was not retrieved**; several cited results (CQ+CHX combination, double mutant, K63R replicate, docking, structural analysis, mutational signatures) exist only in Supporting Information and are reported here as the body text describes them, not as read.
