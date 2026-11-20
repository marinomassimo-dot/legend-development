# GSK-3 shared-premise follow-up: blind verification of the harm-cell statements, report as delivered (legend-delegate, sonnet, effort high, blind, one round, no sub-delegation; delivered 2026-11-20; persisted verbatim by SCI from the subagent hand-back; the brief is `VERIFIER_BRIEF_HARM_CELL_TRIPLES_SCI_20261120.md`). Verifier output; SCI has not re-read the sources the verifier alone reached (Kim 2009 genotype strings from the NCBI E-utilities XML, Planel 2007 and Run 2009 abstracts). Read-back from the delegate's own transcript with `session_model_census.py`: claude-sonnet-5-5 on 10 of 10 turns, effort high on 10 of 10, 16 tool calls in the completion notice, 9,716 output tokens, 527,975 cache-read tokens, born at 22,643 tokens of context, peak 93,115. Hypothesis level only; not medical advice.

BLIND VERIFICATION, harm-cell statements (hypothesis level, not medical advice). Sources per PubMed full text, Ma 2017 (PMID 29234272, DOI 10.3389/fnmol.2017.00391), Kim 2009 (PMID 19801986, DOI 10.1038/nn.2408), Hashimoto 2003 (PMID 12605892, DOI 10.1016/s0306-4522(02)00577-8). Scratch: /home/desktop/.claude/jobs/93f134db/tmp/verifier_harm_cell_20261120/

Route notes: the PubMed full-text tool strips italics, superscripts and the symbols p/n (Ma and Kim). Europe PMC XML returned 500, and the PMC page returned a reCAPTCHA (stopped). I recovered Kim's genotype strings from the NCBI E-utilities efetch XML (kim_eutils.xml in the scratch folder). Figure panel letters are not in the text I read; I give figure numbers from the legends.

H1. VERIFIED, with caveats.
- Mouse: "The mice used in this study were ICR mice." Strain only; no sex or litter detail beyond "Electroporated mice were from the same litter."
- Electroporated: "Lateral ventricles of E14.5 embryos were injected with a mixture of 1 µl of pEX-4 (2.5 µg/µl) and 1 µl of siRNA (100 µM). siGSK3α/β and scrambled control siRNA were injected into different sides of lateral ventricles." The number of cells is not stated. The two sides carry the siRNA and the control.
- Readout (Fig 3): "We detected a higher percentage of GFP+ cells co-labeled with BrdU in the dorsal cortex of the mice electroporated with either siGSK3α or siGSK3β". BrdU 50 mg/kg ip into the dam at E18.5, brains taken 2 h later. Proliferation = "percentage of BrdU+GFP+ double positive cells among total cells positive for GFP".
- n: Fig 3 legend "n = 3 brains, n = 8 slices from each brain"; Methods "three pairs of electroporated brain littermates (n = 3...). For each brain, eight slices". So n=3 brains, with slices as repeated measures. Litters are not separately counted.
- Test: Fig 3 legend "Student's t-test". The Methods add "Two-tailed Student's t-test or one-way ANOVA... Bonferroni". The test cannot be assigned per panel from the text.
- Genetic (acute siRNA knockdown), not pharmacological. BrdU is only a label. Knockdown was lower in primary neurons than in CAD cells. Ma's own caveat: possible off-target effects.

H2. VERIFIED.
- Tbr2 (Fig 4): "The percentage of Tbr2+ and GFP+ double-positive cells were increased in the siGSK3α-transfected brains... brains transfected with pEX-4 and siGSK3β showed a substantial decrease in the percentage of Tbr2+GFP+cells".
- Cux1 (Fig 5): "the percentages of Cux1+GFP+cells were markedly reduced by siGSK3β but unaffected by siGSK3α".
- VZ (Fig 2): GSK3α "more cells remained in the VZ and the SVZ, and fewer cells migrated into the CP"; GSK3β "the percentage of GFP+cells remaining in the VZ was four times higher than that of control brains". The "four times" is only for beta, and it is a sentence figure, not a table value. No fold change is given for alpha.
- Same preparation as H1 (E14.5 to E18.5, n=3 brains x 8 slices). The test is Student's t or one-way ANOVA.

H3. VERIFIED_NARROWER, in four ways.
- Exact genotype as written (E-utilities XML): "Gsk3a−/−; Gsk3bloxP/loxP; nestin-cre". So alpha is a germline null and only beta is conditionally deleted (nestin-cre). The statement's "conditional deletion of both" is loose. The PubMed-tool text drops the genotype.
- Controls: "Gsk3a+/−; Gsk3bloxP/+; nestin-cre" littermates.
- Quotes: "Tbr2-positive cells was reduced by 64% (±2.7%)"; "Tuj1–positive neurons were decreased by about 60%". The sentences themselves give no age. Figs 2 and 3 legends say E13.5 for the cortical sections.
- Single deletions: "Neither Gsk3a null nor Gsk3bloxP/loxP; nestin-cre mice had major brain developmental malformations (W.-Y.K. and W.D.S., unpublished observations)". Discussion: "had no obvious effect". So the single-deletion claim is unpublished observation, and the single mutants are alpha-null (global) and beta-nestin-cre.
- Death: "mice had bigger heads... at every developmental stage from E12.5 until they died at P0". No cause is given.
- n: "six E12–16 mice for each experiment (control mice, n = 3; ... mice, n = 3). Random fields chosen from more than ten tissue sections from each embryo". Fig 2 and 3 legends: "n = 10 sections from each of three mutant and control embryos". Fig 2a has no n or test in its legend; Fig 3d has "P < 0.01". The Tbr2 64% rests on that small n.
- Pharmacology on animals: the only drug on animals is BrdU (20 mg/kg ip to the dam). DAPT and LY294002 were applied to dissociated progenitor cultures, not animals.

H4. VERIFIED, abstract level.
- Abstract: "BrdU incorporation was detected... in cerebellar granule cells prepared from postnatal rats and cerebral cortical cultures prepared from embryonic rats"; "lithium increased BrdU incorporation in cerebellar granule cells and cerebral cortical cultures".
- The abstract states no lithium concentration, no animal dose, and no culture age in days (only "postnatal" and "embryonic"). The abstract also says lithium prevented loss of proliferation after glutamate, glucocorticoids or haloperidol.
- Not read: full text, concentrations, n.

H5. Record: set_id 01c4facd-ed79-4078-ba33-2044de372d0f; id 5072144b-30c0-ed6a-e063-6394a90a2b9c; version 1; effective_time 20260427; manufacturer REMEDYREPACK INC. sha256 matched the brief (566a8682...c7292d). All five statements are supported:
- (a) VERIFIED. Boxed warning: "Lithium toxicity is closely related to serum lithium concentrations, and can occur at doses close to therapeutic concentrations."
- (b) VERIFIED. 5.1: "toxic concentrations for lithium (≥1.5 mEq/L) are close to the therapeutic range (0.8 to 1.2mEq/L)"; the text names ataxia and seizure. "In rare cases, neurological sequelae may persist despite discontinuing lithium treatment and may be associated with cerebellar atrophy." The label hedges ("may").
- (c) VERIFIED_NARROWER. 5.7: "Lithium is concentrated within the thyroid and can inhibit thyroid synthesis and release which can lead to hypothyroidism." The section is titled "Hypothyroidism or Hyperthyroidism", and hyperthyroidism cases are also reported.
- (d) VERIFIED. 8.1: "Lithium may cause harm when administered to a pregnant woman." Also "Lithium toxicity may occur in neonates who were exposed to lithium in late pregnancy. A floppy baby syndrome..." The label says the cardiac-malformation data are "insufficient to establish a drug-associated risk".
- (e) VERIFIED_NARROWER. 8.4: established "for monotherapy... of bipolar I disorder in pediatric patients ages 7 to 17"; "not been established in pediatric patients less than 7 years of age with bipolar I disorder". It is bipolar I monotherapy only.

H6. Both statements correct and not exceeded.
- (a) Fig 7 legend: "numbers depict the ratio of phosphorylated or total GSK3β to β-actin protein level... The representative results of four independent experiments are shown." It is not a phospho/total ratio. P20 mice, three regions.
- (b) Fig 7d legend, verbatim: "Pretreatment of a GSK3β inhibitor LiCl (60 mg/kg) suppressed PTZ-induced seizure activity in Wwox−/− mice." Results: "Injection of a potent GSK3β inhibitor lithium chloride significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice (Fig. 7d)." Neither names wild-type or heterozygous mice in the LiCl context. Methods: "LiCl (i.p., 60 mg/kg) were pretreated three times within 1 h before PTZ injection." Fig 7d panel contents (arms, n) are not in the text and I did not see the image. I cannot say whether the plot includes other genotypes. The Discussion says whether lithium rescues development "remains to be studied".

H7. One primary source found, abstract level: Planel 2007, PMID 17376970, DOI 10.1523/JNEUROSCI.4854-06.2007. Abstract: "anesthesia induced rapid and massive hyperphosphorylation of tau, rapid and prolonged hypothermia"; "Reestablishing normothermia during anesthesia completely rescued tau phosphorylation to normal levels"; it calls for "careful monitoring of core temperature during anesthesia in laboratory animals to avoid artifactual elevation of protein phosphorylation". Mouse brain. Supporting: Run 2009, PMID 19276556 (DOI 10.3233/JAD-2009-1003), anesthesia induces tau phosphorylation at several sites. Not found: no post-mortem-delay source. I ran one query and did not open the returned post-mortem hits. So hypothermia and anesthesia are covered; post-mortem delay is UNREACHABLE.

Not done: figure images, supplements, full-text locators for Hashimoto. No repository file edited.
