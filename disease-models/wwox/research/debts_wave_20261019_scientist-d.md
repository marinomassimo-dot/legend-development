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
