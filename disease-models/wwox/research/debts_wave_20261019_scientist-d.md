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
- "Null mutations of WWOX/Wwox in humans, mice, and rats lead to severe neural diseases ..., metabolic disorders associated with lipid, cholesterol and glucose metabolism, and early death" cites four items that are, by title and venue (an inference; no reference type is printed), two reviews, an editorial and a commentary (refs 27, 28, 55, 56). None is a primary report of a human biallelic-loss case. The sentence puts human null mutations, mouse knockouts and the rat frameshift in one clause; the lde rat allele is a C-terminal frameshift, not a null, as the repository's earlier reading of the rat paper records.
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
- *Human risk.* "The genomic region containing the WWOX gene has been identified as a genetic risk factor in each of these metabolic diseases" is phrased about the region (a later paragraph does say genetic variation of WWOX is a risk factor), and its twelve references include a lung-cancer copy-number paper and the SCAR12 family paper, neither a metabolic-disease association study by conventional definition (the review itself counts cancer among metabolic-dysfunction diseases; narrowed after the blind audit below). The review mentions human biallelic loss-of-function families only in the enzyme-specificity section, and never links them to a metabolic phenotype.
- *The enzyme.* The substrate and product are unknown; the build-up-of-a-metabolite model is conjecture with the metabolite unidentified.

**System gap and change.** Flies and cultured cells for mechanism; population GWAS for human risk; nothing in the reference genotype class (constitutive biallelic loss in a developing brain). No claim moves. It is the best single statement that the WWOX-metabolism axis is a Drosophila and mouse-tissue axis without a human biallelic-loss metabolic datum, which is what the repository's own readings concluded; the unread primaries behind its Drosophila arm are Choo 2015 and Dayan 2013, both subscription (parked).

---

## Blind audit (legend-locator-audit, run blind on eight load-bearing triples)

A separate agent with no session history received only eight (proposition, quote, anchor) triples and the source files. No baseline claim is narrowed, so the audit was not mandatory; it was run because the Orchestrator asked for it on load-bearing triples and because several propositions here are absence claims.

| # | Source | Verdict | What the audit added |
|---|---|---|---|
| 1 | Hong 2007: no mitochondrial measurement; the statement points to a "submitted" paper | SUPPORTED | The only fractionation in its Methods is cytosol and nucleus; Figure 6 is a yeast two-hybrid map of the SDR domain. |
| 2 | Lin 2011: siRNA arm, P = 0.0042, 0.0436, 0.0465, 0.4403 | SUPPORTED | No knockdown-validation blot is shown in Figure 5; the analysis is separate within-condition P values with no interaction test; the siRNA bars still drop about 9 points with U0126. |
| 3 | Huang 2016: Figure 4C has no mitochondrial marker row | SUPPORTED | alpha-tubulin sits on the cytosol side only; mitochondrial localisation is also imaged with a dye in 4E, which is not a blot. |
| 4 | Huang 2018: refs 27, 28, 55, 56 are reviews, an editorial and a commentary | UNDERSHOOT | The reference type is not printed; it is inferred from title and venue (now stated in the text above). |
| 5 | Lee 2017: the Discussion claims an expression finding the paper does not contain | SUPPORTED | The Results phrase "in human HCC" for GTEx describes a genotype-versus-expression comparison, not tumour against normal. |
| 6 | Chen 2018: Table 2 percentages use denominators 61 and 85 | SUPPORTED | The same denominators apply to every genotype percentage in Table 2, not only AA+AG; the Results text also calls the non-recurrence group "control subjects". |
| 7 | Hsu 2009: the mitochondrial sentence is an inference | SUPPORTED | None. |
| 8 | Lee 2021: region versus gene; two non-metabolic references | OVERSHOOT | A following paragraph does say variation of WWOX is a risk factor, and the review counts cancer among metabolic-dysfunction diseases. The manifest proposition was narrowed with a declared `contradicts_locator` (audit object attached); the text above was narrowed. |

Disposition: one overshoot caught by the auditor (not by me), one undershoot; both corrected before landing.

## Parked papers and the cascade (full wishlist in `CC-20261019-SCIENTISTD-DEBT-01.md`, section 4)

Fifteen papers have no lawful body obtainable here. Cascade for each: PubMed identity check, Unpaywall, Europe PMC search and full text, OpenAlex, CORE, Internet Archive, publisher landing and PDF with and without a browser-like User-Agent, HAL, one Semantic Scholar try (HTTP 429), web search for the two highest-value Chang-laboratory items. Three of them (Sze 2004, Yang 2021, Aqeilan 2004) are free to read but sit behind a publisher bot challenge: a browser download by the operator suffices. Best-value order: Choo 2015 (respiratory complex), Mignot 2015, Tabarki 2015, Sze 2004, Hsu 2008, Lo 2008, Chen 2005, Choi 2026, Dayan 2013, Yang 2021, Aqeilan 2004, Teng 2012, Chang 2003, Chang 2007, Lin 2017.

## Result table

| PMID | Paper | Depth | Receipt JSON (staged) | Manifest | Locators |
|---|---|---|---|---|---|
| 29675105 | Chen 2018 (WWOX SNP, HCC) | complete | `FTR-20261019-29675105-01` | PASS | 11 |
| 17567906 | Hong 2007 (Zfra, TNF, WOX1) | complete | `FTR-20261019-17567906-01` | PASS | 15 |
| 19366691 | Hsu 2009 (TGF-beta1, Hyal-2, WOX1) | partial | `FTR-20261019-19366691-01` | PASS | 13 |
| 29310447 | Huang 2018 (phosphorylation review) | partial | `FTR-20261019-29310447-01` | PASS | 10 |
| 28426730 | Lee 2017 (WWOX SNPs, HCC risk) | complete | `FTR-20261019-28426730-01` | PASS | 7 |
| 21901168 | Lin 2011 (MEK1/WOX1, leukaemia) | partial | `FTR-20261019-21901168-01` | PASS | 11 |
| 27339895 | Huang 2016 (IkappaB-alpha/ERK/WWOX) | partial | `FTR-20261019-27339895-01` | PASS | 12 |
| 34210081 | Lee 2021 (WWOX gene and metabolism review) | complete | `FTR-20261019-34210081-01` | PASS | 9 |

All receipts are under `receipt_staging/scientist-d/` and validated in isolation (`validate_receipt` plus `validate_new_receipt`). Every figure of every paper read was opened as an image (Hsu 2009 figures 2 and 4 and Hong 2007 figure 12 viewed but not declared as artefacts); none was read from a caption alone.

## The plain statement

**The debt chase found no WWOX-direct primary that measures a metabolic consequence of WWOX loss.** What it found instead is where the secondary literature's mitochondrial and phosphorylation statements end: single-laboratory observations in cultured leukaemia, fibroblast and tumour lines under pharmacological or acute stress, with overexpression and dominant-negative constructs and no Wwox-null cell. The Lo 2015 pointer for Zfra/WWOX mitochondrial translocation resolves, for Hong 2007, to a paper that says "submitted"; the TGF-beta/Hyal-2 model of Sze 2015 rests on an overexpression and yeast-substitution paper with one dominant-negative blot; the mitochondrial relocation after phorbol ester is one confocal series in Jurkat cells; the pS14 model is a blot series in one T-ALL line plus an undisclosed peptide experiment. The primaries that would test the mitochondrial leg directly (retinal, MPP+, Zfra/cytochrome c) and the Drosophila respiratory primary (Choo 2015) are subscription and are the operator's first four requests. The HCC SNP papers (Chen 2018, Lee 2017) are internally inconsistent about what their variants do and carry no loss-of-function readout. No claim moves; CLAIM 009 receives one MINOR annotation.

## Micro-upgrade shipped

`framework/scripts/pubmed_identity_check.py` took the last `ArticleId` DOI of the whole PubMed record, which for an article with no `ELocationID` is a cited paper's DOI: it reported a clean record (PMID 17567906) as TITLE_MISMATCH against a paper it cites. It now reads the article's own identifiers only; regression `test_doi_comes_from_the_article_not_its_reference_list` (5 tests, OK). Disease-agnostic: any PubMed record with a reference list and no `ELocationID`.

---

# Wave 2 (2026-10-20): the open, unread, gene-direct items listed in `CC-20261019-SCIENTISTD-DEBT-01`

Second lot under the same task contract. Nine readings (six new, three resumes of partial receipts) of the open items my first candidate queued, WWOX-direct and lawful body only. Two items on my own queue list were wrong and are corrected here: Hong 2009 (PMID 19484134) was already resumed by `scientist-a` in another task branch (its manifest sits in `interv-h1-a`), and Park 2004 (PMID 15266310) and the Zfra "small wizard" commentary already have complete receipts; Li 2009 (PMID 19918364) and Hong 2009 had partial receipts, not "none". Identifiers, receipts and manifests were checked against the ledger and the worktrees before reading.

## Paper 9. Tabarki 2015, Exp Biol Med (PMID 25416187): commentary on WWOX and the developing brain (queue entry FT-090)

`context_policy: SOURCE_FIRST`. The queue holds this paper as `FT-090`, the item the registry calls the single reference that carries a sister paper's only sentence about germline WWOX loss and neuronal disease; its status there is `EVIDENCE_BLOCKED` by licence. The lawful route that worked is the Internet Archive capture of the PMC author-manuscript page (Europe PMC XML fails for this deposit); the capture is the whole text, with no figure, table or supplement. Whole article and 17 references read.

**What it carries.** A narrative summary of the human and rat literature on WWOX in the nervous system: expression in the developing mouse brain, the lde/lde rat (a 13-base-pair deletion frameshifting the last 44 codons), the SCAR12 families (Mallaret 2014, a missense in the first WW domain with normal protein amounts but loss of PPPY-peptide binding, and a second family with a C-terminal missense), the nonsense family of Abdel-Salam 2014 (two siblings, early death, atrophy, thin cortex), and one unpublished Saudi sibling family with refractory seizures, spasticity, microcephaly and early death.

**What it settles for FT-090.** It does support, as a summary of three reports, that germline WWOX variants are associated with neurological disease in humans, the sentence the queue entry needs. It does so by restatement: the commentary adds no data except an unpublished family with no data shown.

**What it does not support.** (1) A metabolic phenotype of biallelic loss: metabolic syndrome is one clause with one citation (a review), the abstract has an uncited phrase about metabolic conditions, and no family is described as having a metabolic feature (failure to thrive and growth retardation are described without measurement). (2) The mechanism of the seizures: the mitochondrial pathway is offered through Bcl-2 and Bcl-xL down-regulation by overexpressed WOX1 in cell lines and an MPP+ rat paper. (3) "Functional null": the lde/lde allele is, by the commentary's own earlier sentence, a C-terminal frameshift. (4) The "virtual full knockout" description of the nonsense family: no RNA or protein result is cited.

**What it changes.** `FT-090` can be closed by this reading (a complete read, route recorded); the registry's reading of the sister paper's sentence is confirmed as resting on a restatement, with the evolutionary-argument inversion the entry describes untouched.

## Paper 10. Hsu 2016, Front Cell Dev Biol (PMID 27999774): HYAL-2/WWOX/SMAD4 review

`context_policy: QUESTION_DRIVEN` (held: papers 3, 6 and 7). Europe PMC JATS plus the Frontiers PDF; both figures (schematics) opened as renders; whole article and 133 references enumerated. The Chang laboratory's review of its own hyaluronan, TGF-beta and Zfra work.

It restates, with no data of its own: the Hsu 2009 model (8 to 9-fold reporter, over 95 percent death of promoter-positive cells); bubbling cell death; and the Zfra peptide "Z cell" programme. Points that matter here: (1) its sentence that null mutations in humans and animals cause metabolic disorders cites, by title and venue, two reviews, one case report and one consanguineous-family study (one of them closed-access; no metabolic measurement is quoted); (2) it states that overexpressed WWOX sequestering transcription factors "does not work effectively in vivo", citing a rat nerve-injury paper, i.e. the laboratory's own premise for much of its cell-line work is qualified in its own review; (3) it repeats that a Zfra peptide "completely cures" tumours in heterozygous Wwox mice, which the primary (paper 11) shows as one curve of one mouse; (4) "malignant cancer cells are generally devoid of WWOX, SMAD4 and p53" sits against the same laboratory's description of WWOX up-regulation in early lesions. No claim moves.

## Paper 11. Lee 2015, Oncotarget (PMID 25686832): Zfra peptide, spleen "Z cells" and a Wwox heterozygote cure (primary behind Hsu 2016)

`context_policy: QUESTION_DRIVEN` (held: paper 10). Europe PMC JATS plus ten figure images from the PMC blob store; Figures 1-10 opened as images; whole article and 28 references read; supplementary Figures S1-S7 not retrieved (`partial_fulltext_read`).

**What it measures.** Synthetic Zfra peptides given by tail vein to nude, BALB/c and NOD-SCID mice before subcutaneous or intravenous tumour cell inoculation: tumour-volume curves (two flanks per mouse), spleen-cell transfer, flow sorting of peptide-binding spleen cells ("Z cells", 25 to 29 percent of normal spleen, 0 to 3 percent in tumour-bearing mice), and one heterozygous Wwox mouse.

**What it does not support.**
- *The Wwox claim.* The only Wwox genotype in the paper is one heterozygous mouse (Figure 5E: one tumour curve falling from about 2000 to about 100 cubic millimetres over 50 days after four injections, no untreated heterozygote curve, no genotype panel). The text calls the cure rate 70 percent of ten mice, the Figure 5E legend 75 percent of ten, and the Discussion 70 percent; 75 percent of ten is not possible. The tumour onset age is "around 9 months" here and "approximately age one" in the laboratory's review. The Discussion itself concedes that spontaneous tumours in heterozygotes "need further investigation, since the wild type mice tend to spontaneously grow tumors", and that the result is "in contrast to a previous report".
- *Adoptive transfer.* In Figure 6B the Zfra-donor group has one flank near 1700 and one near 500 cubic millimetres against 2900 and 1700 for controls; in Figure 6C the groups overlap (control ends near 1000 and 300, Zfra-donor near 800 and 600) although the text cites both panels for increased resistance; no number of mice is stated.
- *Statistics and controls.* Curves are "representative data from 2 to 6 experiments", end-point t tests, no randomisation or blinding stated, many results and the toxicity and lifespan statements are "data not shown".
- The WWOX-specific mechanism (Zfra blocks WWOX-induced cytochrome c release) is a restatement of the Cell Signal paper, itself unread (parked).

**What it changes.** Nothing in a claim. It is the readable primary for the "cure" sentence of paper 10, and shows it is a single-animal observation with inconsistent counting, so any citation of a Zfra "cure of Wwox heterozygote tumours" should be treated as one mouse.

## Paper 12. Zhang 2012, Mol Med Rep (PMID 22484428): WWOX overexpression in A549 cells and the mitochondrial pathway

`context_policy: QUESTION_DRIVEN` (held: paper 9, which cites it for the seizure mechanism). Spandidos publisher PDF (bronze open access), text by `pdftotext`, page 3 (Figures 1-4) rendered and opened; whole 4-page article and 17 references read. PubMed names Zhang as first author and Crossref names Fan; the PDF title page names Zhang, so the identity check's AUTHOR_MISMATCH is an author-order difference, not a hybrid record.

Transient WWOX cDNA in one lung adenocarcinoma line reduces MTT viability to about 73 to 86 percent of empty vector, raises early apoptosis to 16.6 against 3.0 percent, raises cytosolic cytochrome c on one blot and gives cleaved caspase-9 and -3 bands in the WWOX lane only. Not supported: a mitochondrial compartment (the blot is a 10,000 g supernatant with beta-tubulin; no mitochondrial fraction, marker or purity control); a comparison of pathways (no caspase-8 or extrinsic readout, so "mainly" is interpretation); any loss of function; WWOX localisation (the translocation sentence is "we speculated"). Methods give the MTT wavelength as 540 nm and the legend 570 nm. Its one metabolic sentence describes the SDR domain's function as related to lipid hormones and metabolic mediators, with a general citation.

## Paper 13. Cheng 2016, Oncotarget (PMID 27655721): WWOX SNPs and oral cancer, with a Kozak-sequence variant

`context_policy: SOURCE_FIRST`. Europe PMC JATS plus two figure images; both figures (all panels) and Tables 1-4 read; whole article and 56 references read. Same group and same five SNPs as paper 5 (Lee 2017).

761 male oral cancer patients from two hospitals against 1199 Taiwan Biobank controls, with very unequal exposure (betel-quid chewing 80 against 17 percent, smoking 88 against 53). One SNP (rs11545028, a 5'UTR C to T) is associated with risk through the TT genotype (55 cases, 52 controls; OR 1.82). The authors then argue that the T allele lowers WWOX translation through a suboptimal Kozak context.

**What is and is not supported.** The GTEx eQTL medians shift slightly with overlapping boxes (blood P = 0.011, muscle 0.0016, oesophagus 0.027), tumour mRNA is lower in C/T or T/T (34 patients, P = 0.042 on the panel, not in the text), and IHC is weak/strong 11 and 22 for C/C against 12 and 6 for C/T or T/T (P = 0.022, an uncorrected chi-square; a Fisher exact test of the same counts gives about 0.038). The mechanism leaps beyond that: (1) the reporter is described only as a promoter-region construct in a pGL3-Enhancer vector (insert boundaries not given); the paper reads it as translation initiation, whereas such a construct would ordinarily report transcriptional output (my inference), and its effect size is about 35 percent in two lines and about 90 percent in one; (2) the variant is called a "nonsense polymorphism in exon 1" in the Discussion and a 5'UTR variant in Table 1; (3) the HCC paper of the same group reports the same allele associated with smaller tumours and lower alpha-fetoprotein, the opposite direction. Paper 14 (Ekizoglu 2015) found no effect of the same variant on WWOX expression in head and neck tumours.

## Paper 14. Ekizoglu 2015, PLoS One (PMID 25612104): WWOX expression, promoter methylation and sequence variants in head and neck cancer

`context_policy: SOURCE_FIRST` (opened as a reference of paper 13). Europe PMC JATS plus the PLOS PDF; Figure 1 and Table 6 read as a render, Tables 1-5 as text; whole article and 37 references read; supplementary Figures S1-S16 (a gel and chromatograms) not retrieved (`partial_fulltext_read`).

80 tumours with paired normal tissue (one hospital): WWOX mRNA is lower in 61 of 80 (about 3.5-fold on the mean), associated with stage and histology, not with grade, age or site; promoter methylation is not more frequent in tumour than normal (54 against 37 percent) and associates with low mRNA only inside the tumour group; miR-134 does not differ and its 3'UTR binding-site variant (25 het, 10 hom of 65) has no effect on expression; ten coding alterations in 65 tumours, mostly in exons 6-8, two of them known polymorphisms; the Kozak minus-5 C to T (23 het, 6 hom) "has no effect on the expression level".

**What is not supported.** A somatic-versus-germline split (matched normal DNA was sequenced but no table reports it); "functional inactivation by mutation" (no function is tested; PolyPhen-2 labels differ between text and table: R120P against Arg120Trp, "possibly" against "probably damaging"). **Why it matters here:** it is the one reading in this lot that tests the Kozak variant of paper 13 against expression in tumour tissue directly, and finds nothing; the two papers cannot both be right about that allele unless the tissue differs.

## Paper 15. Li 2009, PLoS One (PMID 19918364): resume (supplementary Figures S2, S4, S5)

Resume of the earlier partial reading; prior receipt `FTR-20261003-19918364-01` named, `reread_reason: inadequate_prior_coverage`. The supplementary TIFFs already in the shared tree (ImageMagick crashes on them; PyMuPDF renders) were each opened as an image. S2: single WOX1-stained fields at four times, nuclear WOX1 arrowed in one ipsilateral 6 h field, no counts. S4: Wwox mRNA in situ hybridisation and WOX1 staining in the dorsal and ventral horn look alike on both sides three days after transection, as the legend says. S5: p-WOX1 in ventral horn neurons on both sides, no counts. Nothing contradicts the earlier reading (whose own manifest notes that the headline nuclear p-WOX1 rise is not lateralised: Figure S3 gives about 72 percent of small contralateral neurons and about 71 percent ipsilateral at two months). Depth now `complete_fulltext_read`.

## Paper 16. O'Keefe 2015, PLoS One (PMID 26302329): resume (reference list and supplementary Figures S1-S4)

Resume; prior receipt `FTR-20261003-26302329-01`. The 70-entry reference list was read (gene-direct entries checked: the two mouse-model primaries read; Choo 2015 and Dayan 2013, the same programme's respiratory and metabolic-reprogramming papers, unread and parked; O'Keefe 2005 unreceipted); S1 to S4 opened as images. S1 gives adult eye size under Egr/TNF-alpha expression of about 26.5, 29 and 32 (times 10^4 pixels) for wild type, Wwox1/+ and Wwox2/+ with about ten flies each and one and four asterisks, i.e. heterozygous Wwox loss enlarges the eye, the basis of "WWOX contributes to Egr/TNF-alpha-mediated cell death"; the blots show one lane per condition. S2 to S4 are single photographs (p53 and hid overexpression, cytoplasmic WWOX staining, Scrib clones with Wwox loss) with no quantification. Depth now `complete_fulltext_read`.

## Paper 17. Tsai 2013, Cell Death Dis (PMID 24008736): resume (the article's own supplement, previously "not retrievable")

Resume; prior receipt `FTR-20261003-24008736-02`. The earlier manifest records a deposit defect: the file the PMC deposit serves as the supplement belongs to a different article (a leukaemia kinase-inhibitor paper). The article page on the publisher's site links this article's own supplementary PDF (12 pages, Supplementary Methods and Figures 1-7); it was retrieved with a browser-like User-Agent, fingerprinted, rendered at 90 dpi and read page by page. The earlier statement that Supplementary Figures 1-7 are not retrievable is superseded (noted in the manifest artefact entry).

What it shows: the only germline Wwox arm (Supplementary Figure 7) is a single pair of blots of mouse embryonic fibroblasts: WWOX 1.0, 0.5 and 0.0 for +/+, +/-, -/-, and LC3-II 1.0, 1.9 and 1.7, with no replicate, statistic or lysosomal-inhibitor flux control, so higher LC3-II cannot be read as more autophagy rather than slower turnover, and the heterozygote value is slightly above the null. The mTOR interaction (Supplementary Figure 6b) is a faint WWOX band in an anti-mTOR precipitate from cells expressing both tagged proteins, one experiment; methotrexate lowers the Atg12-Atg5 conjugate (to 0.2) and LC3 (to 0.3) in SCC-15 cells; methotrexate-resistant SCC-9 has no DNA ladder; 5-FU raises WWOX about 1.6 to 2.0-fold on one blot. Depth now `complete_fulltext_read`.

## Blind audit, wave 2 (eight triples; separate agent, triples and source files only)

Six SUPPORTED, one SUPPORTED with a note, one OVERSHOOT (the word "only" in a Tabarki proposition), plus two narrowings (wording). Applied to the uncommitted manifests and to this note before committing, so no `contradicts_locator` was needed.

| # | Source | Verdict | Applied |
|---|---|---|---|
| 1 | Lee 2015: cure rate 70 against 75 percent of ten | SUPPORTED | none; the figure is one mouse, so neither number can be checked against it |
| 2 | Lee 2015: Figure 6C no visible difference | SUPPORTED, panel C only | the claim stays limited to 6C; panel B does show a donor effect in one of two flanks; n = 2 and no statistics |
| 3 | Tsai 2013 supplement: Wwox MEF blots single, no flux control | SUPPORTED | the main text claims only "increased LC3-II", not autophagy induction (stated) |
| 4 | Cheng 2016: promoter-reporter against a translational claim | SUPPORTED for the construct facts | narrowed: the source gives the vector name and "promoter region" only; "reports transcriptional output" is my inference, now marked as such |
| 5 | Ekizoglu 2015: Kozak variant "no effect", no table | SUPPORTED with one inference | the link to the Kozak row is by position and the minus-5 label; the "no effect" is unquantified |
| 6 | Hsu 2016: metabolic sentence, four references | SUPPORTED, wording | Alkhateeb 2016 is a family study, not a case report: now "two reviews, one case report and one family study" |
| 7 | Zhang 2012: cytosolic blot, no mitochondrial marker, "mainly" | SUPPORTED | A549 only, single blots (stated) |
| 8 | Tabarki 2015: no metabolic phenotype described; metabolism one clause | OVERSHOOT on "only" | narrowed: one cited clause plus an uncited abstract phrase; failure to thrive and growth retardation are described without measurement |

## Parked in wave 2 (added to the wishlist in `CC-20261019-SCIENTISTD-DEBT-02.md`)

Chang 2001, 2003 (JNK1) and 2005 (TNF/p53) JBC primaries: free to read, publisher bot challenge, no repository copy (browser download); Hsu 2005 Zfra cloning and Chang 2005 estradiol: closed; Alkhateeb 2016: closed; Cancemi 2011 and Guo 2013 (references of the oral-cancer and head-and-neck papers) were not triaged for access.

## Wave-2 result table

| PMID | Paper | Depth | Receipt (staged) | Manifest |
|---|---|---|---|---|
| 25416187 | Tabarki 2015 commentary | complete | `FTR-20261019-25416187-01` | PASS |
| 27999774 | Hsu 2016 review | complete | `FTR-20261019-27999774-01` | PASS |
| 25686832 | Lee 2015 Zfra and Z cells | partial (supplement not read) | `FTR-20261019-25686832-01` | PASS |
| 22484428 | Zhang 2012 A549 | complete | `FTR-20261019-22484428-01` | PASS |
| 27655721 | Cheng 2016 oral cancer Kozak | complete | `FTR-20261019-27655721-01` | PASS |
| 25612104 | Ekizoglu 2015 head and neck | partial (supplement not read) | `FTR-20261019-25612104-01` | PASS |
| 19918364 | Li 2009 resume (supplement S2, S4, S5) | complete | `FTR-20261019-19918364-02` | PASS |
| 26302329 | O'Keefe 2015 resume (references, S1-S4) | complete | `FTR-20261019-26302329-02` | PASS |
| 24008736 | Tsai 2013 resume (own supplement retrieved) | complete | `FTR-20261019-24008736-03` | PASS |

## The plain statement, wave 2

**Still no WWOX-direct primary that measures a metabolic consequence of WWOX loss.** What the second lot adds is the state of the secondary-to-primary chains: the Zfra "cure" of Wwox-heterozygote tumours is one mouse with inconsistent counting; the oral-cancer paper's translational mechanism for a Kozak variant is a promoter-reporter plus tissue associations, and an independent tumour series finds no expression effect of the same variant; the one germline Wwox arm of the autophagy paper is a single LC3 blot of mouse embryonic fibroblasts without a flux control, retrievable only from the publisher's own supplement because the PMC deposit carries another article's; and the commentary that the queue marks as carrying the only germline-loss sentence of a sister paper does support that sentence, as a restatement of three reports, with no metabolic phenotype anywhere.
