# Blind reader verdicts: GSK3 / eIF2B hypotheses package (IT47 P4)

Reader: independent delegate (sonnet, high effort, no sub-agents). Date of reading: 2026-11-12. Public sources only, zero spend, nobody contacted, no e-mail address sent to any service, no browser-header spoofing. Biomedical literature accessed through PubMed (NCBI) records; every PubMed-derived item below carries its DOI.

Opened under `generation_it47_20261112/`: only `verify/BRIEF.md` and `verify/decisive_propositions.tsv`. Opened under the package folder `gsk3_eif2b_20261107/output/`: `README.md`, `hypotheses.tsv` (R0), and, to resolve the residue and numbering items, `evidence.tsv` and `residues.tsv`. Not opened: any `conditional_proposals*`, any other IT47 file.

Depth labels used: FULL = complete article text read (body, Methods, figure legends; figure images where stated); ABSTRACT = abstract only; DATABASE COPY = UniProt record.

## What I read first

1. `README.md` and `hypotheses.tsv` of the package (R0).
2. The eight propositions (`decisive_propositions.tsv`).
3. Original papers. PMC text through the PubMed tool for 32000863 (PMC6990504) and 26974342 (PMC4805534); Europe PMC fullTextXML for the figure legends of both (the XML download works for those two PMC ids); figure images: Wwox paper Fig. 7 (publisher static media), eLife Fig. 5, Fig. 7 and Fig. 5-supplement 2 (eLife IIIF image server). Abstract-level reads for 15126504 and 12133000 (full text not reachable, routes in "What I could not check").
4. For R9 to R11: PubMed records (abstracts) and one open full text (PLoS One, 24023715), UniProt REST JSON for the three EIF2B5 entries.

## R0. The package's own definitions

**Verdict: the four column names are not defined anywhere in `README.md`; only the content of the cells defines them. Depth: DATABASE COPY (package files). Quotes are from the package.**

README locator: section "IPOTESI" in `README.md`: "IPOTESI (compound, action, context, benefit, what refutes it: `hypotheses.tsv`)". That is the only README sentence that describes the hypothesis columns, and it never uses the four column names. A text search of the whole `gsk3_eif2b_20261107` folder for `requires_first`, `refuted_or_replaced_by`, `benefit_if_true`, `documented_action` returns only the header line of `hypotheses.tsv`. So any definition below is read from cell content, not stated by the package.

What the cells show:

- `documented_action_on_the_node`: the existing evidence that the tool acts on the node. H1: "GSK3 inhibition and dephosphorylation of Ser535 documented for LiCl, SB-415286 and SB-216763 in CHO cells (abstract level) and for genetic Gsk3b loss in mouse neurons ... For LY-2090314, laduviglusib and TDZD-8, Ser535 dephosphorylation is not documented in any source seen; the documented action is for LiCl, SB-415286 and SB-216763 only (audit)." H5: "n/a".
- `benefit_if_true`: what would be gained if the hypothesis held. H1: "a correction of translation and one functional read-out specific to the null (not seen in controls)". H4: "separates a GSK3-site mechanism from the generic ISR mechanism, which is the question asked".
- `refuted_or_replaced_by`: the outcome that would falsify or replace the hypothesis; H1 lists four: "(a) pS535 not raised at baseline: the chain breaks at L1 or L2; (b) pS535 falls but exchange and translation do not move (the CHO result, E06): site not sufficient; (c) effect also in corrected cells or unchanged by S535A: off-target (E07); (d) effect disappears when phospho-eIF2 alpha is lowered: the ISR route". H5: "This is the null of H1 and H3, to be stated before the measurement".
- `requires_first`: H1 "repeat of the single-lane Ser9 blot with replicate lanes and total GSK3 (E01 limits)"; H2 "H1 baseline"; H3 "H1 baseline"; H4 "H3 constructs"; H5 "H1 baseline". The README's priority paragraph confirms the gating sense: "Priority: is phospho-epsilon at the GSK3 site raised in WWOX-deficient neurons at matched stage ... If not, the chain breaks at L1 or L2 and H1 to H4 stop."

**Answer to the brief's question: `requires_first` names a prerequisite to be met before the hypothesis can be tested (a baseline measurement, a repeated blot, constructs that must exist). The measure that discriminates the hypothesis from its rivals is in `refuted_or_replaced_by`, not in `requires_first`.**

One deviation worth knowing: the audit sentences appended in two cells are cautions, not prerequisites. H3 `requires_first` ends with "S535A cannot separate GSK3 from DYRK2, which acts at the priming Ser539, a different residue (audit)", and H4 `requires_first` ends with "A phosphomimetic at 535 is unvalidated (audit)". The first is a limit of the design (no arm in H3 discriminates GSK3 from the priming kinase, such as an S539A or DYRK2 knock-down arm), the second is closer to a true prerequisite (the construct would need validating first). So the column is not purely prerequisites in H3 and H4.

## R1 to R8. The eight decisive propositions

Summary table first, then the detail.

| Item | Row | Source | Depth | Verdict | Quote agrees | Finding agrees |
|---|---|---|---|---|---|---|
| R1 | E01 | 32000863 | FULL (text, legends, Fig. 7 image) | SUPPORTED, with one limit understated | yes, verbatim (Fig. 7c legend) | yes; "no n" is imprecise, see below |
| R2 | E04 | 15126504 | ABSTRACT | SUPPORTED at abstract level | yes, verbatim | yes (hedged as in the package) |
| R3 | E06 | 12133000 | ABSTRACT | SUPPORTED at abstract level | yes, verbatim | yes |
| R4 | E07 | 12133000 | ABSTRACT | SUPPORTED at abstract level | yes, verbatim | yes |
| R5 | E13 | 26974342 | FULL (text, legends, Fig. 5 image) | SUPPORTED | yes, gene symbol restored | yes |
| R6 | E14 | 26974342 | FULL (text, legends, Fig. 5-supp. 2 image) | SUPPORTED | yes, gene symbol restored | yes |
| R7 | E15 | 26974342 | FULL (text, legends, Fig. 5 image) | PARTLY: quote and number agree; a missing control not named by the package | yes, gene symbol restored | direction yes; the dependence claim lacks the dominant-negative-alone arm |
| R8 | E16 | 26974342 | FULL (text, legends, Fig. 7 image) | SUPPORTED | yes, verbatim | yes |

### R1. E01, Wwox-null mouse, GSK3 beta Ser9 (PMID 32000863, doi 10.1186/s40478-020-0883-3). Depth FULL.

Verbatim, Fig. 7 legend, part c: "Increased activation of GSK3β was determined in the cerebellum, hippocampus and cerebral cortex of Wwox−/− mice at postnatal day 20, as evidenced by dephosphorylation of GSK3β at Ser9. β-actin was used as an internal control in western blotting. Quantitative densitometry of the immunoblots was performed, and the numbers depict the ratio of phosphorylated or total GSK3β to β-actin protein level in the brain tissues. The representative results of four independent experiments are shown."
Results sentence: "we determined dephosphorylation of GSK3β at Ser9 (active GSK3β) in Wwox-/- mouse cerebellum, hippocampus and brain cortex by western blotting (Fig. 7c)." (the Wwox/italic gene symbols are stripped in the PMC text but present in the legend).

Package `locator_quote` "as evidenced by dephosphorylation of GSK3β at Ser9": identical to the legend. Species mouse, genotypes +/+, +/-, -/-, regions cerebellum, hippocampus, cortex: agree.

Figure image check (Fig. 7c, read by eye from the published image): phospho-Ser9 numbers under the blot are cerebellum 2.7 / 3.1 / 1.3, hippocampus 3.6 / 3.5 / 2.0, cortex 3.9 / 3.8 / 2.5 for +/+, +/-, -/-; total GSK3 beta numbers are 2.2 / 2.4 / 2.4, 2.3 / 2.4 / 2.6, 2.2 / 2.4 / 2.6. These match the package's E02 values exactly. "Total unchanged" is approximately right: total is not lower in the null (equal or 0.2 to 0.4 higher), so the Ser9 fall is not a loss of protein. One lane per genotype per region: confirmed on the image.

Mismatches and limits to carry:
1. The package limit "no n on the panel" is true of the panel but the legend does state "representative results of four independent experiments"; the replicate data are not shown or quantified. The limit should read: representative of four experiments, no quantification across them shown.
2. The Methods paragraph for Western blotting says tissues were taken at "postnatal day 14" (antibodies listed there: anti-WWOX, anti-DCX, anti-β-actin; no phospho-GSK3 antibody is listed), while the Fig. 7c legend says postnatal day 20. The package uses P20 from the legend; that is the right locator for this panel, but the paper is internally inconsistent about age on blots (Fig. 6a legend: "postnatal day 14 or 20").
3. The text is a western blot of whole tissue lysate: cell type is not resolved (neurons, glia), as the package already notes.
4. Ser9 phosphorylation fall is "increased activation" by the authors' reading; no kinase activity assay. Agrees with the package limit.

### R2. E04, WOX1 knock-down in SK-N-SH cells (PMID 15126504, doi 10.1074/jbc.M401399200). Depth ABSTRACT.

Verbatim abstract: "Remarkably knock-down of WOX1 expression by small interfering RNA in neuroblastoma SK-N-SH cells spontaneously induced Tau phosphorylation at Thr212/Thr231 and Ser515/Ser516, enhanced phosphorylation of glycogen synthase kinase 3beta (GSK-3beta) and ERK, and enhanced NFT formation."
Package quote "enhanced phosphorylation of glycogen synthase kinase 3beta (GSK-3beta) and ERK": verbatim. The abstract names neither Ser9 nor Tyr216 and gives no direction on activity: the package's hedged finding agrees. The abstract adds "Also an increased binding of phospho-GSK-3beta with phospho-Tau was observed in these WOX1 knock-down cells", which the package does not use; it does not settle the direction either. Full text: not reached (publisher returned HTTP 403; I did not try another route round it). So residue and direction remain unread.

### R3. E06, GSK3 inhibitors in CHO cells, eIF2B not activated (PMID 12133000, doi 10.1042/BJ20020677). Depth ABSTRACT.

Verbatim abstract: "Treatment of cells with LiCl or with either of two recently developed GSK3 inhibitors, SB-415286 and SB-216763, brought about the dephosphorylation of Ser(535), which strongly indicates that this site is indeed a target for GSK3 in vivo. However, these compounds did not elicit significant activation of eIF2B, indicating, consistent with conclusions from one of our previous studies, that additional inputs are required for the activation of eIF2B."
Package quote "these compounds did not elicit significant activation of eIF2B": verbatim. Finding "Despite Ser535 dephosphorylation, eIF2B was not significantly activated; additional inputs are required": agrees. Cell type Chinese-hamster ovary: agrees (also MeSH "CHO Cells; Cricetinae"). Not readable at abstract: assay type, magnitude, replicate numbers, controls, stimulation context. The paper's stated question is insulin activation (title: "insufficient for the activation of eIF2B by insulin"); the package's wording is a fair reduction. Verdict: SUPPORTED at abstract level only; the package already labels it so.

### R4. E07, inhibitors affect protein synthesis and unrelated signalling (same paper). Depth ABSTRACT.

Verbatim: "Our results also show that each of the inhibitors used affects overall protein synthesis and have additional effects on translation factors or signalling pathways apparently unrelated to their effects on GSK3, indicating that caution must be exercised when interpreting data obtained using these compounds."
Package quote: verbatim. Package finding: agrees (the "so a compound-only attribution is unsafe" is the abstract's own "caution"). "Each of the inhibitors used" includes LiCl, SB-415286, SB-216763 as per the sentence before. Details not readable.

### R5. E13, Gsk3b deletion lowers phospho-Ser535 in retinal ganglion cells (PMID 26974342, doi 10.7554/eLife.11903). Depth FULL (text with Methods, figure legends, Fig. 5 image).

Verbatim Results: "By contrast, phospho-eIF2Bε (Ser535) immunoreactivity was markedly reduced in-deleted RGCs in the presence or absence of axon injury (), indicating increased eIF2Bε activity for protein translation." The gene symbol is missing from this PMC text copy (italic stripped); the Fig. 5 legend restores it: "Quantification of phospho-eIF2Bε immunofluorescence intensity. Data are presented as mean ± s.d., n=5 per group. *p<0.001, Two-way ANOVA with Bonferroni post hoc test." and panel A "Gsk3bf/f mice injected with AAV-GFP (Control) or AAV-Cre (Gsk3b-/-), with or without optic nerve injury."
Package quote: agrees (with the gene symbol restored from the legend). Package finding "fell in Gsk3b-deleted neurons, injured or not": agrees. Image: relative intensity about 1.0 in controls against about 0.5 in Gsk3b-/- at uninjured, 1, 3 and 5 days post crush, all marked significant. So "markedly reduced" is about a halving, not abolition.
Limits confirmed: one antibody (EMD Millipore p-eIF2Bε, Methods), immunofluorescence, n=5. Not stated in text or legends: any antibody-specificity control (phosphatase treatment, S535A tissue). The immunofluorescence antibody is raised against the rat-numbered site; mouse numbering is 536 (R10). Retina, adult: agree. Verdict SUPPORTED.

### R6. E14, Gsk3a knockout does not change phospho-Ser535 (same paper). Depth FULL.

Verbatim Results: "deletion did not change eIF2Bε phosphorylation (), suggesting that GSK3α may not regulate eIF2Bε activity in RGCs." (gene symbol stripped in the PMC text copy). Fig. 5-supplement 2 legend: "Analysis of eIF2Bε phosphorylation in Gsk3a knockout mice. (A) ... phospho-eIF2Bε in Gsk3a-/- mice or their wild type litter mates as a control, with or without optic nerve injury ... (B) ... n= 5 per group." Image: control about 1.0 and Gsk3a-/- about 0.95 to 1.0 at un, 1, 3, 5 dpc, no significance marks.
Package quote "Gsk3a deletion did not change eIF2Bε phosphorylation": agrees after restoring the symbol. Package finding and the audit note ("germline knockout at n = 5, against an acute beta deletion") agree: the Gsk3a animals are a genetic knockout compared with wild-type littermates, the beta change is an AAV-Cre deletion in floxed adults. The authors' own wording is "may not regulate", which the package's "did not change" does not overstate. Verdict SUPPORTED.

### R7. E15, catalytically dead eIF2B epsilon E572A negates the Gsk3b-deletion gain in OPP labelling (same paper). Depth FULL.

Verbatim Results: "While the basal level of protein translation in RGCs was suppressed by treatment with the protein synthesis inhibitor anisomycin, [Gsk3b] deletion resulted in a significant increase in OPP-labeled new synthesized proteins, which was largely negated by eIF2Bε E572A treatment ()." The same text describes E572A as "a dominant negative mutant of eIF2Bε that lacks catalytic activity but is capable of forming heteropentameric eIF2B complex", given by AAV co-injection.
Fig. 5E-F legend: "OPP Alexa Fluor 594 protein synthesis assay in retinal whole-mounts from Gsk3bf/f mice injected with AAV-GFP (Control), AAV-Cre (Gsk3b-/-) + AAV-GFP, or AAV-Cre + AAV-eIF2Bε E572A or treated with anisomycin ... n=5 per group. *p<0.01, One-way ANOVA with Tukey's test."
Image, Fig. 5F: control 1.0; anisomycin about 0.1; Gsk3b-/- + GFP about 1.4; Gsk3b-/- + E572A about 0.95.
Package quote: agrees. Direction and "largely negated" agree: the E572A group returns to about the control level, from a gain of about 40 percent. Mismatch or missing control, precisely: the OPP experiment has four arms and none is a dominant-negative-alone arm in Gsk3b-intact (AAV-GFP) retina. So the package's reading "the translation gain depended on eIF2B catalytic function" is not separated from a non-specific lowering of translation by any dominant-negative eIF2Bε; the observation that E572A lands at control level and not below it weakens that alternative but does not remove it. The text also does not say whether OPP was measured after crush (the legend gives no crush information; panel A of Fig. 5 does include crushed time points for the phospho read-out), which agrees with the audit note. Verdict PARTLY: quote, number and direction supported; the dependence inference lacks a control the package should list.

### R8. E16, eIF2B epsilon S535A raises protein synthesis (same paper). Depth FULL.

Verbatim Results: "we injected AAV-eIF2Bε S535A, a constitutively active mutant of eIF2Bε that is resistant to GSK3β phosphorylation (), in the adult wild-type retina. As expected, expression of eIF2Bε S535A significantly increased protein synthesis in RGCs compared with AAV-GFP injection as a control ()." Fig. 7A-B legend: OPP assay, "n=5 per group. *p<0.01, Student's t test". Image: AAV-GFP 1.0, S535A about 1.4.
Package quote: verbatim. Finding agrees. "Described as constitutively active, with a citation" and "activity of the mutant is cited, not measured here": confirmed (the text gives a citation, no assay of mutant exchange activity). The Methods say the S535A plasmid came from the Cooper laboratory; the species of the cDNA is not stated. The construct is overexpressed on top of endogenous protein. Whether the OPP experiment was done with or without crush is not stated (the control is a uninjured wild-type retina by the text "in the adult wild-type retina"). Verdict SUPPORTED.

Also confirmed incidentally from the same full text (not asked): E17 (survival not changed: text "did not change the rate of RGC survival"; Fig. 7F about 27 vs 29 percent) and E18 (phospho-Ser535 higher in adult than developing retina) are in the text.

## R9. Ser-to-Ala at the epsilon GSK3 site, DYRK2 at the priming serine, and a phosphomimetic

**Verdict on the package's two audit sentences: sentence 1 (S535A cannot separate GSK3 from DYRK2, which acts at the priming Ser539, a different residue) SUPPORTED as logic and as to the residue, with the in-cell requirement for DYRK2 only weakly shown; sentence 2 (a phosphomimetic at 535 is unvalidated) PARTLY: I found no Ser535-to-Asp/Glu in the sources reachable, but the absence rests on abstract-level searches (two routes) and on the full text of Wang et al. 2001 not being reachable.**

(a) DYRK2 and Ser539 priming.

1. Woods et al. 2001, Biochem J (PMID 11311121, doi 10.1042/bj3550609). Depth ABSTRACT (full text blocked, see below). Verbatim: "Here we show that Ser(539) of eIF2Bepsilon, which is followed by proline, is phosphorylated specifically by two isoforms of dual-specificity tyrosine phosphorylated and regulated kinase (DYRK2 and DYRK1A), but only weakly or not at all by other 'proline-directed' protein kinases tested. We also establish that phosphorylation of Ser(539) permits GSK3 to phosphorylate Ser(535) in vitro and that eIF2Bepsilon is highly phosphorylated at Ser(539) in vivo." Shows: in vitro, DYRK2 (and DYRK1A) phosphorylate Ser539; Ser539 phosphorylation permits GSK3 to phosphorylate Ser535. Rat numbering. Priming kinase is not unique: DYRK1A also does it.
2. Wang et al. 2001, EMBO J (PMID 11500362, doi 10.1093/emboj/20.16.4349). Depth ABSTRACT. Verbatim: "Glycogen synthase kinase 3 (GSK3) is responsible for phosphorylating Ser535. This regulatory phosphorylation event requires both the fourth site (Ser539) and a distal region, which acts to recruit GSK3 to eIF2Bepsilon in vivo." Shows: in cells, Ser535 phosphorylation depends on Ser539 and a docking region. The kinase at Ser539 in cells is not named in the abstract.
3. Campbell and Proud 2002, FEBS Lett (PMID 11755526, doi 10.1016/s0014-5793(01)03221-5). Depth ABSTRACT. Verbatim: "We recently showed that DYRK2 phosphorylates the translation initiation factor eIF2B at Ser539 in its epsilon-subunit and thereby 'primes' its phosphorylation by glycogen synthase kinase-3." Substrate-specificity work with peptides.
4. Weiss et al. 2013, PLoS One (PMID 24023715, doi 10.1371/journal.pone.0070848). Depth FULL (PMC3762802, text and legends; images not opened). Verbatim: "Further, after siRNA mediated knockdown of DYRK2 phosphorylation of eIF2Bε was reduced () whereas it was increased after adenoviral induced overexpression of DYRK2 in cultivated cardiomyocytes". Figure 4 legend: "siRNA mediated knockdown of DYRK2 lead to reduced phospho(S535)-eIF2Bε levels in vitro. Exemplary immunoblots of three individual experiments." Shows: in neonatal rat cardiomyocytes DYRK2 knock-down lowers, and overexpression raises, phospho-Ser535; in mouse heart a correlation. Limits: a single siRNA sequence in Methods, no rescue, no S539 mutant, cardiomyocytes, not neurons. The paper itself writes "serine 535 (corresponds to serine 540 in the human sequence)".
So: DYRK2 phosphorylating the priming Ser539 and Ser539 being needed for GSK3 at Ser535 are shown in vitro and (the Ser539 requirement) in cells; DYRK2 being required in cells is shown only in one cardiac system by knock-down. Nothing in neurons, nothing in WWOX models.
Logic of the package sentence: S535A removes the GSK3 site itself, so an S535A phenotype shows the residue matters whichever kinase writes it; it cannot say whether GSK3 or the priming route (DYRK2/DYRK1A at Ser539) is rate-limiting, since the priming serine remains. This is a reasoned inference, consistent with the sources, not a result any of them states.

(b) Phosphomimetic at the GSK3 site.

- In the abstract of 24023715 (and in the 26974342 full text) the Ser535 mutant used is Ser-to-Ala; the abstracts of 11311121 and 11500362 name no Ser535 mutant.
- Jefferson et al. 1999 (PMID 10216953, doi 10.1016/s1357-2725(98)00141-1), Depth ABSTRACT. Verbatim: "The first variant contained a point mutation in the eIF2B epsilon cDNA that converted the glycogen synthase kinase-3 (GSK-3) phosphorylation site, Ser535, to a nonphosphorylatable Ala residue. In the second variant, the putative GSK-3 'priming' site, Ser539, was converted to Asp." So a phosphomimetic exists for the priming serine (S539D), used as a substrate in kinase assays; the same abstract reports no Ser535 phosphomimetic.
- Two PubMed query routes (Ser535 with Asp, Glu, S535D, S535E or phosphomimetic; Ser535 with mutation or mutant) returned no abstract describing a Ser535 phosphomimetic. Absence claim: not found at abstract level by two routes; full texts of 11500362 and 11311121 were not reachable (Europe PMC XML returned HTTP 500; NCBI efetch returned a stub because the publishers do not allow XML download), so a mutant named only in the Methods or figures of those papers is not excluded.
Verdict: "unvalidated" is consistent with what I could reach, but cannot be called settled.

## R10. Numbering (human 540, mouse 536, rat 535)

**Verdict: SUPPORTED. Depth DATABASE COPY (UniProt REST JSON, fetched 2026-11-12) plus one paper.**

From the UniProt feature tables ("Modified residue"):
- Human EIF2B5, Q13144, 721 aa, reviewed: Ser540 "Phosphoserine" (evidence: by similarity to Q64350, ECO:0000250) and Ser544 "Phosphoserine; by DYRK2" (high-throughput phosphoproteomics evidence). Local sequence EEPDS(540)RGGS(544)PQ.
- Mouse Q8CHW4, 717 aa, reviewed: Ser536 "Phosphoserine" (by similarity to rat) and Ser540 "Phosphoserine; by DYRK2". Local sequence EELDS(536)RAGS(540)PQ.
- Rat Q64350, 716 aa, reviewed: Ser535 "Phosphoserine" and Ser539 "Phosphoserine; by DYRK2" (evidence for Ser539 includes PMID 11311121). Local sequence EELDS(535)RAGS(539)PQ.
Package table (`residues.tsv`) lists the same accessions, lengths and windows: all agree. The package's own caveat that human Ser540 is annotated only by similarity to rat is also correct. Weiss et al. 2013 (R9) independently writes "serine 535 (corresponds to serine 540 in the human sequence)". Implication already noted by the package: papers' "Ser535" in mouse neurons (26974342) is the rat label; the mouse residue is 536, and which species the S535A cDNA came from is not stated in that paper.

## R11. The named tools, lithium

Two to four sources were requested; I give more because no single abstract covers all tools.

| Tool | ATP-competitive GSK3 inhibitor? | Source and depth |
|---|---|---|
| SB-216763, SB-415286 | Yes | Coghlan et al. 2000, Chem Biol (PMID 11033082, doi 10.1016/s1074-5521(00)00025-9), ABSTRACT: "SB-216763 and SB-415286 are structurally distinct maleimides that inhibit GSK-3alpha in vitro, with K(i)s of 9 nM and 31 nM respectively, in an ATP competitive manner. These compounds inhibited GSK-3beta with similar potency." |
| CHIR-99021 (laduviglusib) | Yes for CHIR99021 | Pan et al. 2011, Neuropsychopharmacology (PMID 21389981, doi 10.1038/npp.2011.24), ABSTRACT: "selective and direct GSK-3 inhibition by the ATP-competitive inhibitor CHIR99021". The origin paper of the series (Ring 2003, PMID 12606497, doi 10.2337/diabetes.52.3.588, ABSTRACT) describes aminopyrimidine GSK-3 inhibitors with Ki below 10 nM and "at least 500-fold selectivity against 20 other protein kinases" but its abstract does not name CHIR99021 nor state ATP competition. That "laduviglusib" is the INN of CHIR-99021 is not stated in any source I read; the equivalence is the package's and the brief's. |
| LY-2090314 | Described as ATP-competitive, secondary only | Vergoten and Bailly 2022 (PMID 35686814, doi 10.1002/jbt.23130), ABSTRACT, docking paper: "reference GSK-3β ATP-competitive inhibitors LY2090314 (3) and AR-A014418 (2)". Diaz-Martin et al. 2025, Nat Commun (PMID 41193440, doi 10.1038/s41467-025-64701-7), ABSTRACT: X-ray structure of LY2090314 bound to Toxoplasma TgGSK3 "reveals an interaction mode characteristic of type I ATP-competitive inhibitors" (parasite kinase, not human GSK3). I did not reach a primary human-GSK3 enzymology paper for LY-2090314: PARTLY. |
| TDZD-8 | Not ATP-competitive (class-level) | Martinez et al. 2002, J Med Chem (PMID 11881998, doi 10.1021/jm011020u), ABSTRACT: "we describe the synthesis, biological evaluation, and SAR of the small heterocyclic thiadiazolidinones (TDZD) as the first non-ATP competitive inhibitor of GSK-3beta ... IC(50) values in the micromolar range". The abstract speaks of the TDZD class; it does not name TDZD-8 individually. Later disputes about TDZD mechanism were not checked. |
| ISRIB | Not a GSK3 or any kinase inhibitor; an eIF2B activator | Sidrauski et al. 2015, eLife (PMID 25875391, doi 10.7554/eLife.07314), ABSTRACT: "We now report that ISRIB is an activator of eIF2B." Tsai et al. 2018, Science (PMID 29599213, doi 10.1126/science.aaq0939), ABSTRACT: "ISRIB, a drug-like eIF2B activator ... ISRIB promoted this step by cross-bridging a central symmetry interface." |

Package statement check: the package/brief grouping is right for SB-216763, SB-415286 and for CHIR99021; TDZD-8 non-ATP-competitive is supported at class level; ISRIB is not a GSK3 inhibitor; LY-2090314 is only secondarily sourced here. Another caution from the sources read: Coats et al. 2023 (PMID 37316860, doi 10.1186/s12964-023-01147-8, ABSTRACT) calls CT99021, SB216763 and LY2090314 "selective, structurally distinct GSK3 inhibitors", but its subject is elraglusib, an ATP-competitive GSK3 inhibitor whose lymphoma effect is not attributable to GSK3: an example that a tool's cell effect cannot be assigned to GSK3 without read-outs of GSK3 targets.

Lithium.
- In vitro mechanism: Ryves and Harwood 2001, BBRC (PMID 11162580, doi 10.1006/bbrc.2000.4169), ABSTRACT: "Li(+) is a competitive inhibitor of GSK-3 with respect to magnesium (Mg(2+)), but not to substrate or ATP." Ryves et al. 2002 (PMID 11798168, doi 10.1006/bbrc.2001.6305), ABSTRACT: "Li(+) inhibits GSK-3 by competition for magnesium (Mg(2+)), but not ATP or substrate", with two Mg sites proposed. So lithium is not ATP-competitive.
- In cells and organisms: Klein and Melton 1996, PNAS (PMID 8710892, doi 10.1073/pnas.93.16.8455), ABSTRACT: "Lithium potently inhibits GSK-3 beta activity (Ki = 2 mM), but is not a general inhibitor of other protein kinases ... lithium treatment phenocopies loss of GSK-3 beta function in Xenopus and Dictyostelium." Wang et al. 2002 (R3) in CHO cells: LiCl dephosphorylates Ser(535), together with the two ATP-competitive inhibitors.
- Second target: the same Klein and Melton abstract: "the favored hypothesis is that lithium acts through inhibition of inositol monophosphatase (IMPase). We show here that complete inhibition of IMPase has no effect on the morphogenesis of Xenopus embryos"; Phiel and Klein 2001 review (PMID 11264477, doi 10.1146/annurev.pharmtox.41.1.789), ABSTRACT: "A number of enzymes have been proposed as potential targets of lithium action, including inositol monophosphatase ... and the protein kinase glycogen synthase kinase-3 ... generally inhibited by lithium in an uncompetitive manner, most likely by displacing a divalent cation." The 26974342 full-text Introduction also says "many other potential targets including a number of vital enzymes are also inhibited by lithium in an uncompetitive manner". Lithium therefore inhibits GSK3 and IMPase, plus other Mg-dependent enzymes: SUPPORTED.
- Lithium is not equivalent to direct GSK3 inhibition: Pan et al. 2011 ABSTRACT: "These results distinguish the mechanism of action of lithium from direct GSK-3 inhibition both in vivo and in vitro" (AKT activity required for lithium's behavioural effects in mice). This bears on the package's use of lithium only as a labelled non-specific comparator, which is consistent.

## Other findings of use to the author (not asked)

- E02 densitometry in the package matches the printed Fig. 7c numbers exactly; the correction to the manifest sentence stands.
- The package E15 and E16 OPP magnitudes: both gains are about 40 percent over their controls (1.4 against 1.0), E572A restores about the control value (0.95).
- The package's README says 12133000 had its full text blocked at both attempts; I reached the same abstract-only depth by three further routes (see below). No paper in R1-R8 was reached beyond abstract except 32000863 and 26974342 (full).

## What I could not check

- 15126504 (E04) full text: JBC article page returned HTTP 403; not retried or worked around. Which GSK-3 beta residue the siRNA experiment measured, and the antibody, remain unread.
- 12133000 (E05 to E07) full text: PubMed full-text tool returned an empty body; Europe PMC fullTextXML HTTP 500; NCBI efetch (db=pmc) returns a stub noting the publisher does not allow XML download; Portland Press page returned a browser challenge (not worked around). The assay type and magnitude behind "did not elicit significant activation" are unread.
- 11311121 and 11500362 full texts (R9): Europe PMC XML HTTP 500, efetch stub. So the Methods and figures that would show any phospho-site mutants beyond the abstracts are unread; the "no Ser535 phosphomimetic" absence is abstract-level.
- 15001529 (cardiac S535A, E09 to E12) was not in scope here and was not read.
- Fig. 7c of 32000863 was read by eye from the image: numbers are as printed; band quality and exposure cannot be judged from a web-size image.
- Antibody specificity for the phospho-Ser535 immunofluorescence in 26974342 is not addressed in the text or legends I read; Methods are brief and I did not look for a supplementary validation.
- LY-2090314 ATP-competition against human GSK3 from a primary enzymology paper; the INN equivalence laduviglusib = CHIR-99021; the later TDZD-8 mechanism literature.
- DYRK2 in neurons or in any WWOX context: nothing found in the routes tried (two PubMed queries for DYRK2 with eIF2B epsilon returned the cardiac paper only).

## Tool calls and approximate tokens

About 55 tool calls (6 file reads and image views of repository files and downloaded figures; about 17 PubMed search, metadata, ID-conversion and full-text calls; about 22 shell calls for HTTP fetches of Europe PMC XML, UniProt JSON, figure images and local parsing; 3 web-fetch attempts, 2 of which were refused or redirected to a sign-in step and were not followed). Token figures are estimates, not census numbers: roughly 190,000 input tokens read across the session (largest single items: two PMC full texts of about 12,000 to 16,000 tokens each, one open-access cardiac full text of about 10,000, five figure images) and roughly 14,000 tokens written, including this file. No model or effort read-back was taken from a transcript.
