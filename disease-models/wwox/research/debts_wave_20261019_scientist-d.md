# Reading debts, wave 2026-10-19 — WWOX-direct primaries — scientist-d

**Actor:** `scientist-d` (stated assumption of the Orchestrator; one of four equivalent Scientists under `roles/scientist.md`). **Task:** `DEBT-WWOX-DIRECT-D-20261019`. **Branch:** `task/DEBT-WWOX-DIRECT-D-20261019`.
**Reading mode:** `PRIMARY_EVIDENCE_READ`. **Not medical advice.** Class-level statements only; no individual-level record. Nothing here touches the four scientific current files or `disease_model.md`.

(sections are appended paper by paper; the result table and the plain statement come last)

---

## Paper 1. Chen 2018, J Cancer (PMID 29675105): WWOX rs9926344 and hepatocellular carcinoma recurrence

`context_policy: QUESTION_DRIVEN` (held: a peer manifest's one-line description of this paper as "WWOX rs9926344 and HCC recurrence"). Surface: Europe PMC JATS plus the publisher PDF, Figures 1-3 and Tables 1-5 inspected as renders. Whole article read.

**What it measures.** One surgical HCC series (152 patients): an 8 versus 8 discovery comparison (recurrence within two years versus none) on a genome-wide SNP array, 32 candidate SNPs "data not shown", then 136 patients genotyped by mass spectrometry. rs9926344 carriers (AA+AG) have more recurrence (19 of 58 against 9 of 78; OR 3.7), shorter recurrence-free survival (Kaplan-Meier P = 0.004; adjusted HR 1.79, P = 0.035) and, in an immunostaining subset of 100, more often low tumour WWOX (12 of 16 AG against 36 of 82 GG). Everything is measured in tumour tissue.

**What it does not support.**
- *A WWOX loss-of-function effect of the allele.* The paper never states where rs9926344 lies or what it does to the transcript or protein; the only expression evidence is a 16-versus-82 immunostaining comparison with one representative image pair that carries no genotype label (Figure 3).
- *A germline claim.* DNA was extracted from "cancerous tissue", so a somatic change in the tumour cannot be separated from a germline variant; no normal-tissue genotype is reported.
- *A clean association.* The discovery set is 8 versus 8 with 32 passing SNPs not shown, so the number of variants examined before one was reported is unrecoverable and no multiplicity correction is mentioned. The recurrent/non-recurrent classes of the association step come from "early follow-up data", while the survival step uses follow-up to April 2015 (76 recurrences among 119); the two are not reconciled.
- *An overall-survival effect after adjustment.* Adjusted overall survival HR 1.62 has P = 0.097; the abstract's "independent prognostic factor" is true for recurrence only.
- Internal inconsistencies found at the source: Table 2 percentages are computed on denominators 85 and 61 instead of 78 and 58 (the odds ratios and P values use the counts); the text prints an upper limit of 2.816 where Table 5 prints 2.866; Table 4 percentages for rs9926344 use a third denominator; the Discussion gives "only 2 samples" for AA in immunostaining against four AA carriers genotyped. A recomputation from the printed counts (my own arithmetic, not the paper's) gives uncorrected chi-square P values equal to the printed ones (0.0025 for AA+AG, 0.0015 for the allele test), while exact tests give 0.0047 and 0.0020; the conclusion survives both, with four AA carriers and no test of them.
- Nothing metabolic. The Introduction cites "moderating the mitochondrial respiratory complex" to a reference list entry (Choo 2015) as one clause; no metabolic readout exists.

**System gap to the disease model.** Adult Chinese tumour cohort, common-variant association with tumour behaviour; the reference genotype is a biallelic loss of function in early development. The paper is a datum about HCC prognosis and a prior that a WWOX noncoding variant might alter tumour protein. It adds nothing to the metabolic theme except as the earlier paper of the group behind the WWOX/NME2/oleate report (Liu 2024), whose manifest names it as a debt.

**Reading debts it carries.** Choo 2015 (mitochondrial respiratory complex; no receipt anywhere; added to this lot) and Lee 2017 (the preceding WWOX/HCC risk-variant paper; no receipt).


## Paper 2. Hong 2007, BMC Mol Biol (PMID 17567906): Zfra, TNF and WOX1 (Lo 2015 ref 55)

`context_policy: QUESTION_DRIVEN` (held: a peer's note that the 2015 minireview points to this paper for Zfra and WWOX mitochondrial translocation). Surface: Europe PMC JATS plus the open-access PDF (Springer Link content URL; the BioMed Central counter URL returned a client challenge). All twelve figures opened as page renders; whole article read.

**Identity note.** The DOI that Europe PMC and PubMed carry for this PMID is the BioMed Central one; the repository's `pubmed_identity_check.py` first reported TITLE_MISMATCH for it because it took the last `ArticleId` DOI of the whole record, a cited paper's. Fixed and regression-tested in this wave (see the micro-upgrade); the record itself is a clean match.

**What it measures.** Overexpression of a 31-residue peptide (Zfra) and of mouse WOX1 or point mutants in cultured lines (L929, COS7, SK-N-SH, MCF7, MDA-MB-231, Molt4, ME180, HEK-293), with crystal-violet death percentages, GST pull-downs, a yeast Ras-rescue two-hybrid and cytosol/nucleus fractionation blots after TNF or UV. Readouts: Zfra overexpression kills most lines tested; Zfra binds the first WW domain (lost with a Tyr33-to-Arg substitution) and the SDR domain but not the mitochondria-targeting stretch inside it; TNF or UV raises Zfra binding to Tyr33-phosphorylated WOX1, JNK1 and NF-kappaB; Zfra keeps WOX1, p53, NF-kappaB and p-ERK out of the nucleus in SK-N-SH and MCF7 but not WOX1 in Molt4 without UV; Zfra and WOX1 given together do not add in death.

**What it does not support.**
- *Mitochondrial translocation of WWOX or Zfra.* This is the point that matters for the repository. The paper contains no mitochondrial fraction, no cytochrome c and no mitochondrial imaging. Its one mitochondrial statement is a pointer to "Hsu et al., submitted" (Discussion, paragraph 8). The 2015 minireview's pointer to this paper for Zfra and WWOX mitochondrial translocation and cytochrome c release is therefore carried by the companion Hsu 2008 paper (PMID 18403180), not by this one. A reader who follows the minireview's reference 55 will not find it.
- *Any WWOX loss-of-function effect.* There is no knockdown, knockout or hypomorph; every WOX1 manipulation is overexpression of the mouse cDNA or its Y33R mutant. The Y33R result tests the residue (it also loses apoptotic activity), not the phosphorylation; phosphorylation is not measured in yeast.
- *Enzymatic SDR function.* SDR alone neither kills cells nor responds to Zfra; SDR plus the C-terminal tail kills (about 26 percent, 62 percent with synthetic Zfra peptide, one experiment per condition shown). No substrate, cofactor or activity assay exists.
- *Quantified binding.* Figures 7 and 8 are single blots with no densitometry or replicates; "greater than 50 percent" appears only in the caption. Figure 9C is one histogram per condition (SubG1 52.1 percent WOX1, 29.9 percent WOX1 plus Zfra, 34.5 percent Zfra alone); 48-hour data and nuclear counts are stated as not shown.
- The authors' own frame is split: WOX1 is "pro-apoptotic" in these assays, and the Discussion says observations "support a pro-survival role of WOX1 in vivo".

**System gap to the disease model.** Mouse WOX1 and human Zfra overexpressed in tumour or transformed lines, acute TNF or UV stress, 24 to 48 hours. The reference genotype is a constitutive biallelic loss of function. This is a datum about what an overexpressed WWOX does to a stressed cell, not about what is lost when WWOX is absent, and it says nothing about metabolism.

**What it changes.** Nothing in a claim. It converts one sentence in a minireview from a restatement into an unsupported pointer, which is a transfer risk: the repository's mitochondria-related lines that lean on the minireview should cite the Hsu 2008 primary, which is not readable here (see parked list), so the mitochondrial-translocation statement stays at the level of "reported by one laboratory in stressed cultured cells, primary unread".

## Paper 3. Hsu 2009, J Biol Chem (PMID 19366691): TGF-beta1, Hyal-2 and WOX1 (Sze 2015 ref 9)

`context_policy: QUESTION_DRIVEN` (held: the Sze 2015 commentary, read by a peer, cites this paper as the basis for "TGF-beta1 probably uses membrane Hyal-2 to signal complex formation with WWOX and Smad4"). Surface: Internet Archive capture of the PMC page (the Europe PMC XML endpoint returned HTTP 500 and the PMC PDF sits behind a challenge) plus ten figure images from the PMC blob store; Figures 1-10 opened as images. Supplementary Figs S1-S6 (one index page in PMC) were not retrieved: depth is `partial_fulltext_read`, supplement `not_read`.

**What it measures.** In mouse L929 and human HCT116 cells (the latter lacking type II TGF-beta receptor): nuclear fractionation blots after TGF-beta1 (WOX1, Tyr33-phosphorylated WOX1, p-ERK, Smad4), immunogold electron microscopy of TGF-beta1 and WOX1 with Hyal-2 on microvilli, an anti-Hyal-2 antiserum and a Hyal-2 antisense construct, FRET between ECFP-WOX1 and the EYFP-Hyal-2 catalytic domain, a yeast two-hybrid and co-immunoprecipitations, and a Smad-promoter reporter counted as fluorescent cells per field.

**What it does not support.**
- *Any consequence of WWOX absence.* WWOX is overexpressed (mouse WOX1, human WWOX-EGFP); the loss-of-function arms are one dominant-negative WOX1 (the complex falls by 32 percent, n = 3, one blot) and a Hyal-2 antisense construct. No Wwox-null or knockdown cell is used.
- *A mitochondrial result.* The Discussion states that "WOX1 translocates to the mitochondria both in vitro and in vivo" and that "Hyal-2 and WOX1 are likely to co-translocate ... to the mitochondria"; the first rests on three references (retinal damage, MPP+ rat, cytochrome c release) from the same group, the second is an inference. No mitochondrial fraction is measured. Those three references are the unread primaries this wave was asked to chase.
- *A steady, quantified nuclear relocation.* Figure 1 shows a transient: in L929 cells nuclear WOX1 peaks about 160 percent at 10 minutes and returns to about 50 percent by 80 minutes; in HCT116 cells all four proteins fall to about 30 percent of baseline by 40 minutes. Figure 5C (electron-microscopy counts) is one bar per location and time with no error bars, and the 1-hour nuclear value is below the untreated one, while the text says nuclear accumulation increased with time.
- *Hyal-2 as the TGF-beta1 receptor.* "Cognate receptor" rests on one antiserum against a 15-residue peptide, a peptide competition and an antisense construct, in cells that also carry a TGF-beta receptor in L929; the authors themselves list the Hyal-2/receptor relationship as untested.
- *A functional promoter effect.* The reporter is a count of GFP-positive cells per field, and 95 to 98 percent of the promoter-positive cells in the two combinations are dead; WOX1 alone reads about as high as the kit positive control. The L929 replicate is "data not shown".
- Tyr33 phosphorylation as required for binding: the yeast result is a residue substitution and phosphorylation is not measured in yeast.

**System gap.** Overexpression in two tumour or transformed lines under acute TGF-beta1; the reference genotype is constitutive biallelic loss. The model in Sze 2015 (TGF-beta1 to Hyal-2 to WWOX/Smad4) therefore rests on overexpression, a yeast substitution, one dominant-negative blot and EM counts, and says nothing about what is lost in the absence of WWOX.

**What it changes.** No claim. It marks the TGF-beta/Hyal-2 part of the Sze 2015 model as one laboratory's overexpression evidence, and, with paper 2, shows the repository's mitochondrial-translocation line has no primary readable here: it ends in Chen 2005, Lo 2008 and Hsu 2008, all subscription.

## Paper 4. Huang and Chang 2018, Exp Biol Med (PMID 29310447): review of WWOX phosphorylation (Carvalho 2022 ref 21)

`context_policy: QUESTION_DRIVEN` (held: a peer's note listing this paper as a Carvalho 2022 reference with no receipt). Surface: Internet Archive capture of the PMC page (author manuscript; the Europe PMC XML returned HTTP 500) plus both figure images (both are schematics, opened as images). Depth `partial_fulltext_read`: the review has no methods or results and the supplementary table of WW-domain proteins (xlsx) was not retrieved.

**What it measures.** Nothing; it is a narrative review by the laboratory that produced most of the Tyr33, Ser14, Zfra and Hyal-2 literature. It restates mouse, rat and human WWOX data and proposes a pY33 (anti-cancer, protective in neurons) versus pS14 (cancer-promoting, neurodegeneration-enhancing) switch.

**What it does and does not carry on the metabolic theme.** Two sentences bear on it, and both are restatements:
- "Null mutations of WWOX/Wwox in humans, mice, and rats lead to severe neural diseases ..., metabolic disorders associated with lipid, cholesterol and glucose metabolism, and early death" cites four items, two of them reviews, one an editorial and one a commentary (refs 27, 28, 55, 56). None is a primary report of a human biallelic-loss case. The sentence puts human null mutations, mouse knockouts and the rat frameshift in one clause; the lde rat allele is a C-terminal frameshift, not a null, as the repository's earlier reading of the rat paper records.
- "Conditional Wwox knockout mice suffer severe metabolic defect, growth retardation, reduced bone volume, hypocapnia, impaired hematopoiesis, leukopenia, and splenic atrophy" cites the Ludes-Meyers 2009 allele-generation paper. Comparing with that paper's existing manifest (hypoglycaemia, uraemia and acidosis at postnatal day 18; leukopenia and anaemia on two animals; bone trend at P = 0.07): the direction is faithful, but the animals are the germline-deleted knockout derived from the floxed allele, not a conditional deletion, and "hypocapnia" is not a value I could confirm from that manifest.
- Also checked from the text itself: the knockout survival "three weeks" cites a paper on the Wwox and p73 association and a TRAPPC6A-delta paper, not a knockout report, and the companion Hsu 2009 paper gives "approximately 1 month".

**What it does not support.** Any new datum. The mitochondrial statements (a pY33-WWOX/IkappaB-alpha/ERK complex "in the cytoplasm and mitochondria" in resting MOLT-4 cells; WWOX relocating to mitochondria after phorbol ester dissociates a WWOX/MEK1 complex) are single-leukaemia-line results from the same laboratory. The pS14 model rests on one mouse experiment (Zfra peptide lowering pS14-WWOX, tumour growth and amyloid pathology together), which cannot separate pS14 from Zfra's other actions. The steroid-binding explanation of the rat testis phenotype is "not surprising" rather than shown.

**System gap and change.** Review of cultured-cell, rodent and human reports, with the senior author's own models foremost; no claim moves. It is worth having read because it is a pointer-rich secondary source cited by Carvalho 2022: the metabolic sentences it carries resolve to reviews and to one allele paper already read, so the Carvalho-to-Huang chain adds no independent evidence for a human metabolic phenotype of WWOX loss.

## Paper 5. Lee 2017, PLoS One (PMID 28426730): WWOX SNPs and hepatocellular carcinoma risk (Chen 2018 ref 17)

`context_policy: SOURCE_FIRST` (opened as a reference of paper 1; nothing about it held). Surface: Europe PMC JATS plus the PLOS printable PDF; Figure 1 (A to E) opened as a render; Tables 1-5 read. Whole article read.

**What it measures.** A hospital case-control series in Taiwan (354 HCC patients, 708 health-examination controls, blood DNA): five common WWOX SNPs, association with HCC risk and with clinicopathology and laboratory values, a homology model of the SDR domain and a GTEx eQTL plot for one SNP.

**What it does not support.**
- *Risk by an allele that lowers WWOX.* The single significant case-control result is protective: carriers of the rs73569323 minor allele are 6 of 354 patients against 39 of 708 controls (adjusted OR about 0.3). The other four SNPs show no association. The abstract's conclusion that WWOX variation is "a significant predictor of early HCC occurrence" is carried by this rare protective allele and by subgroup tests.
- *The vascular-invasion result as established.* It is 252 men, 28 carriers, 9 with invasion (P = 0.024), one of many clinical comparisons for five SNPs, with no multiplicity statement.
- *A consistent variant class.* rs12918952 is called an exonic SNP that "may result from amino acid changes", an Ala-179-Thr substitution, and a "synonymous variant in exon 6" in different sections.
- *An expression effect.* The Discussion says "we reported the additional finding that WWOX expression was downregulated in HCC"; no such measurement is in the paper. The eQTL trend is described as human HCC (Results), GTEx liver (Discussion) and whole blood (legend); the panel title names a liver eQTL; its class sizes (25, 40 and 32 donors) imply an alternate-allele frequency near 54 percent against about 5 percent A allele among the study's own controls, and the paper does not say which allele GTEx calls "Alt". Figure 1E is an overlapping boxplot trend, not a test.
- Nothing metabolic; the Introduction lists metabolic disease only as an HCC risk factor.

**System gap and change.** Common-variant association with a tumour in an adult East Asian series; the reference genotype is a biallelic loss of function. No claim moves; it is a small datum that HCC SNP literature on WWOX is internally inconsistent about what the variants do, and it supports the reading of paper 1 that a WWOX SNP association with tumour behaviour has no demonstrated effect on WWOX protein or function.

## Paper 6. Lin 2011, Genes Cancer (PMID 21901168): a WOX1/MEK1 complex in leukaemia T cells (primary behind two mitochondrial sentences)

`context_policy: QUESTION_DRIVEN` (held: the Huang 2018 review, paper 4, which cites this paper for WWOX relocating to mitochondria after the WWOX/MEK1 complex dissociates). Surface: Internet Archive capture of the PMC page plus seven figure images; Figures 1-7 opened as images; whole article read; supplementary Figs S1-S12 not retrieved (`partial_fulltext_read`). Not in any registry identity record.

**What it measures.** Micromolar PMA on Jurkat and Molt-4 T-leukaemia lines with and without the MEK inhibitor U0126: DNA fragmentation and sub-G1, JC-1 mitochondrial polarisation, one anti-MEK1 co-immunoprecipitation series, a dominant-negative WOX1 and an siRNA in Jurkat, confocal co-localisation of WOX1 with a mitochondrial dye and of MEK1 with a lysosomal and a lipid-raft marker, and a FRET series in COS7 cells.

**What it supports.** In Jurkat cells at 10 micromolar PMA, the WOX1 band in a MEK1 precipitate fades within 10 to 60 minutes, U0126 delays that and delays death, and confocal overlap of WOX1 with a mitochondrial dye is visible at 30 minutes and gone by 120. It is the readable primary behind the review sentence "dissociation of the WWOX/MEK1 complex ... leads WWOX to relocate to the mitochondria".

**What it does not support.**
- *Generality.* No other of eleven lines responds as Jurkat does; the death lacks phosphatidylserine exposure, shrinkage and blebbing (stated; data not shown), so "apoptosis" is the authors' word for a PMA-induced rupture at pharmacological dose.
- *Causality of WWOX.* The knockdown arm is one siRNA experiment (n = 3): U0126 protection is P = 0.0042, 0.0436 and 0.0465 in control, mock and scramble and P = 0.4403 in WOX1 siRNA, i.e. a significant-versus-non-significant contrast with control and mock themselves borderline; dominant-negative WOX1 lowers fragmentation by about a third (290 to 190). The Methods say every experiment was done three to five times while two bar graphs average two experiments. The authors themselves "do not exclude other possibilities".
- *Mitochondrial relocation as quantified.* Figure 6C is one confocal field per time point described by colour overlap; there is no co-localisation coefficient and no fractionation. The paper's summary says the death "is probably associated with" the relocation.
- *The co-immunoprecipitation as strong.* The WOX1 band in the MEK1 precipitate is faint, the non-immune control is shown for MEK1 only, and the experiment is one series per condition.
- Nothing metabolic; "mitochondrial polarisation-depolarisation" is a JC-1 dye read-out of an acute pharmacological stress.

**System gap and change.** Leukaemia T-cell lines under 10 micromolar PMA; the reference genotype is constitutive biallelic loss. The paper is the primary for one mitochondrial-relocation statement that the repository's secondary sources repeat, and shows that statement is a single-line, single-condition observation with borderline statistics. No claim moves; the mitochondrial-translocation line stays "reported by one laboratory in stressed cell lines" with this primary now read and the retinal (Chen 2005) and MPP+ (Lo 2008) primaries still unread.

## Paper 7. Huang 2016, J Biol Chem (PMID 27339895): IkappaB-alpha, ERK and WWOX in MOLT-4 maturation (primary behind the Ser14 and MOLT-4 mitochondrial statements)

`context_policy: QUESTION_DRIVEN` (held: paper 4, whose pY33/pS14 and MOLT-4 mitochondrial sentences cite this paper). Surface: Internet Archive capture of the PMC page plus nine figure images; Figures 1-9 opened as images; whole article read; supplementary Fig. S1 and Videos S1-S3 not retrieved (`partial_fulltext_read`). Registry holds a corpus placeholder only.

**What it measures.** In MOLT-4 T-ALL cells a nanomolar PMA with ionophore (IoP) induces CD3 and CD8: a 1.2 to 1.4-fold CD3 rise by blot, flow cytometry of surface CD3, cell-cycle shift to S and G2/M, ERK and IkappaB-alpha phosphorylation within minutes, WWOX phospho-site blots (Ser14 up, Tyr33 and Tyr287 down), anti-IkappaB-alpha co-immunoprecipitations, cytosolic and mitochondrial fractions and confocal co-localisation, yeast two-hybrid and FRET mapping of the WWOX WW domain to IkappaB-alpha, and a three-way FRET time course in COS7 cells.

**What it supports.** WWOX, IkappaB-alpha and ERK are detectable in a MOLT-4 mitochondrial fraction, with confocal co-localisation percentages falling after IoP (IkappaB-alpha about 82 to 50 percent, WWOX about 84 to 60 percent, n = 3, unchanged for WWOX with TNF), and WWOX phosphorylation at Ser14 rises while Tyr33 and Tyr287 fall.

**What it does not support.**
- *A WWOX loss-of-function phenotype.* Every WWOX manipulation is overexpression (EGFP-WWOX, a dominant-negative WW-domain mutant); the WWOX-absent comparator is MDA-MB-231, declared WWOX-negative from a cited reference rather than re-measured, and the rescue shown is one blot pair (IkappaB-alpha degradation 45 to 89 percent against 15 percent).
- *A purified mitochondrial compartment.* The fractionation blot (Figure 4C) has no mitochondrial or cytosolic purity marker row; cytochrome c appears only in Figure 4D, where it rises in the mitochondrial preparation at 2 to 3 hours while WWOX falls 91 percent at 1 hour and is back to 12 to 25 percent reduction later, a pattern the text calls release and re-uptake.
- *A strong complex.* In Figure 5A the WWOX band in the IkappaB-alpha precipitate is faint and the stated complex reduction is 0 until 95 percent at 120 minutes; Figure 7F to H (mouse spleen) are cropped single strips.
- *Ser14 function.* How pS14-WWOX works "is largely unknown" (the authors); the in vivo T-cell peptide experiment is "preliminary" and has no data in the paper. This is the paper behind the review's pS14 model (paper 4), which therefore rests on a blot series in one leukaemia line plus the peptide statement.
- Metabolism: one sentence ("WWOX is involved in mitochondrial respiration and metabolism") citing a read review and the parked Choo 2015 primary; nothing is measured.

**System gap and change.** T-ALL line under a differentiation stimulus, human and mouse cDNA overexpression; reference genotype is biallelic loss. No claim moves. Together with paper 6 it closes the loop on the review sentences of paper 4: the mitochondrial and pS14 statements resolve to single-line observations by one laboratory.

## Paper 8. Lee 2021, Cells (PMID 34210081): review of the WWOX gene, FRA16D and WWOX in metabolism (added from the Carvalho/Huang chain; the one metabolic-theme review not yet read)

`context_policy: QUESTION_DRIVEN` (held: papers 4 and 7, which cite the Drosophila respiratory-complex primary, and this repository's knowledge that most mammalian WWOX-metabolism primaries are already read). Surface: Europe PMC JATS plus two figure images (both opened); whole article read; the MDPI PDF returned HTTP 403 and was not used. Written by the Richards laboratory, which produced the Drosophila WWOX metabolism papers.

**What it measures.** Nothing. It narrates the discovery of WWOX at FRA16D, the unusually long introns (Figure 1: human intron 5 of 222570 and the last intron of 778855 bases against 18778 and 63559 in fugu), a "WWOX in Metabolism" section built on its own laboratory's Drosophila work, a section on population-genetic risk, and two open questions (why a fragile site lies in the gene; what the enzyme does).

**What it carries on the metabolic theme, and what it does not support.**
- *Drosophila.* WWOX-deficient flies show "no phenotypic consequences"; reduced WWOX worsens, and extra WWOX suppresses, tissue phenotypes caused by mitochondrial deficiency, in a way that needs the SDR active-site tyrosine (Y288F in the fly, residue 293 in human). The text then infers that human WWOX-deficiency pathology is "likely to be treatable" through a compensating pathway; no compensating pathway is named, so this is an `IPOTESI`.
- *Mammalian chain.* HIF1A and glucose, aerobic glycolysis, muscle ablation, HDL and lipids and an interactome enrichment are listed as one sentence of single-laboratory results; I checked that the primaries named there are already read in this repository (Abu-Remaileh 2014, Iatan 2014, Lee 2019 interactome, the muscle paper) except the two subscription items below.
- *Human risk.* "The genomic region containing the WWOX gene has been identified as a genetic risk factor in each of these metabolic diseases" attributes risk to the region, not the gene, and its twelve references include a lung-cancer copy-number paper and the SCAR12 family paper, neither a metabolic disease. The review mentions human biallelic loss-of-function families only in the enzyme-specificity section, and never links them to a metabolic phenotype.
- *The enzyme.* The substrate and product are unknown; the build-up-of-a-metabolite model is conjecture with the metabolite unidentified.

**System gap and change.** Flies and cultured cells for mechanism; population GWAS for human risk; nothing in the reference genotype class (constitutive biallelic loss in a developing brain). No claim moves. It is the best single statement that the WWOX-metabolism axis is a Drosophila and mouse-tissue axis without a human biallelic-loss metabolic datum, which is what the repository's own readings concluded; the unread primaries behind its Drosophila arm are Choo 2015 and Dayan 2013, both subscription (parked).
