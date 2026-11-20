# Interactome round: blind verification of the GSK3B partner row, report as delivered (legend-delegate, sonnet, effort high, blind, one round, no sub-delegation; delivered 2026-11-20; persisted verbatim by SCI from the subagent hand-back; the brief is `VERIFIER_BRIEF_GSK3B_PARTNER_ROW_SCI_20261120.md`). Verifier output; SCI has not re-read the primary sources. Hypothesis level only; not medical advice.

Blind verification, one round, hypothesis level, not medical advice. I read only the brief, the two held XMLs (Wang 2012, Cheng 2020) and PubMed tool records. No repository file was edited. Scratch: /home/desktop/.claude/jobs/2d2e7085/tmp/verifier_gsk3b_20261120/. Figure legends were checked from the XML `<fig>` elements. I ran no substring test on any statement string, because the brief supplies paraphrases. The quotes below were copied from the XML text.

**W1. VERIFIED_NARROWER.**
Binding assays in Wang 2012, with the sources used:
- (a) Co-IP in SH-SY5Y cells transiently transfected with WWOX-HA (Fig 2c). Anti-HA pulled down "endogenous GSK3β"; anti-GSK3β pulled down HA-WWOX.
- (b) The same co-IP in RA-treated versus untreated SH-SY5Y cells (Fig 2d). The amount of GSK3β pulled down was "similar" with and without RA.
- (c) Co-IP of GFP-WWOX versus GFP-WWOX-L404A with endogenous GSK3β, in both directions (Fig 3e).
- (d) GST pull-down. GST-WWOX fragments (full length, ww1 1–60, ww2 40–110, ww 1–110, ADH 110–414; also Δ389 and Δ286, and the point mutants L311A and L404A) were made in E. coli and "incubated with cell lysates" (Fig 3b–d). Neither the text nor the legend names the cell type of the lysate. The Methods do not give the lysate source either. Pull-down was therefore not recombinant-to-recombinant.
- (e) Mouse brain extract IP with anti-WWOX or anti-GSK3β (Fig 2e). Legend: "Mouse brain extract was subjected to immunoprecipitation using anti-WWOX or anti-GSK3β". Text: "both GSK3β and WWOX were precipitated by anti-GSK3β or anti-WWOX antibodies".
- (f) Supplementary Figure A: no WWOX–Tau co-IP. This is a negative result.
- (g) In silico docking and molecular dynamics of WWOX388–407 on GSK3β (Fig 3f–h). This is a model, not a binding assay.
- Immunofluorescence colocalisation (Fig 2b) is not binding.

Only (e) uses endogenous proteins from mouse brain. It is the sole endogenous-both-partners assay. The paper gives no strain, age, brain region, IgG control or n for it.

What the paper does not show: purified-recombinant binding. The recombinant His-GSK3β appears only in the kinase assay, which reads function.

**W2. VERIFIED_NARROWER on "required" and "strictly".**
- Motif sentence, verbatim: "WWOX296−320 and WWOX388−412 contain FXXXLI/VXRLE, a highly conserved GSK3β-binding motif" (Fig 2a, an alignment).
- Truncations: "neither WWOX-Δ389 (1–389 a.a.) nor WWOX-Δ286 (1–286 a.a.) were able to interact with GSK3β (Figure 3c). This indicates that WWOX amino acids 388–407 are required".
  - No internal deletion of 388–407 and no 1–407 construct was tested.
  - The "388–407" boundary is an inference from the truncations plus L404A.
  - The Δ389 construct removes 390–414 and keeps residues 388–389.
- L404A: "the mutation of L404A, but not L311A, completely abolishes the binding of WWOX to GSK3β" (Fig 3d, GST pull-down).
  - L404A was tested in pull-down (Fig 3d) and in co-IP (Fig 3e).
  - In co-IP the wording is weaker: "this interaction was diminished when L404 mutated to alanine".
  - "Strictly required" fits only the pull-down. The co-IP says "diminished".
- L311A, a residue in the 296–320 stretch, did not abolish binding. The 296–320 stretch itself was not shown to be dispensable.
- The authors checked L404A folding indirectly, by c-Jun co-IP (data not shown in the legends).
- The Discussion says WWOX "physically interacts with GSK3β only through the WWOX388−407 region", which is stronger than the data.

**W3. VERIFIED_NARROWER.**
- Manipulations:
  - Knockdown: RNAi against WWOX reduces neurite outgrowth and raises pTau S396 (Fig 1d,e).
  - Overexpression: WT WWOX and the L404A mutant in RA-treated SH-SY5Y cells.
  - Quote: "WWOX significantly increased the percentage of differentiated SH-SY5Y cells. However, this increase was abolished when L404 was mutated to alanine" (Fig 5f,g).
- Readout: percentage of cells with neurites longer than twice the cell-body length, from three independent experiments. In Fig 1b, βIII-tubulin and cyclin D1 follow RA over time.
  - Tau pS396 and pS404 were read by western blot (Fig 4c), where L404A abolishes the WWOX effect.
  - pS422 is unaffected by WWOX.
- Cells: SH-SY5Y cells exposed to RA. They are not pre-differentiated cells; RA causes the differentiation.
- Truncation mutants were NOT tested in differentiation. Only L404A was.
- Tau requirement: Tau siRNA (Fig 6a,b; the 6c western confirms knockdown).
  - Quote: "Neither WWOX overexpression nor GSK3β knockdown promoted neurite outgrowth in the Tau knockdown condition".
  - WWOX overexpression raised differentiation to 44% versus 18% in RA controls (lane 6). Tau knockdown abolished the increase (lane 5).
  - Caveat: the text says Tau knockdown also abolishes the RA-stimulated outgrowth by itself (lanes 1–3). The epistasis is therefore partly confounded by loss of the baseline RA response.
- GSK3β activity in cells was not measured directly; it is inferred from Tau phosphorylation.

**W4. NOT_SUPPORTED as worded.**
- The only pS9 statement is under RA treatment: "phospho-GSK3β S9 and phospho-β-catenin remained normal" (Fig 1b), where endogenous WWOX rises.
- No experiment manipulates WWOX and reads pS9. The paper does not claim "independent of S9". The statement is an inference from a correlative RA time course.
- A more faithful wording: pS9 did not change during RA-induced differentiation while WWOX increased.

**W5. VERIFIED_NARROWER.**
- Kinase assay, purified components (Fig 4a,b): "this phosphorylation is completely abolished in the presence of excess WWOX, but not GST or WWOX L404A".
  - "GSK3β-mediated Tau phosphorylation at S396 and S404 was reduced in a dose-dependent manner by GST–WWOX" (Fig 4b; 1, 3, 10 µg).
- Microtubule assay, purified tubulin, Tau, GSK3β and WWOX only (Fig 5e; Methods: "tubulin (0.2 mg/μl)… turbidity change at 350 nm").
  - Quote: "the new equilibrium reached a higher turbidity when treated with WT WWOX and GSK3β than with GSK3β alone… WWOX L404A, could not restore".
  - "Restore" is partial, by the authors' wording. The paper does not state that Tau phosphorylation was read inside the turbidity assay.
  - The Methods list only GTP; ATP is not mentioned for that assay.
  - The binding mechanism is inferred from L404A.
- The assay uses no WWOX-deficient or neural system.
- Paper inconsistencies: the text gives 0.3 µg GST-WWOX and the legend 0.2 µg; the Methods give 20 min at 30 °C and the legend 10 min at 20 °C.

**C1. VERIFIED_NARROWER.**
- Cheng 2020 Fig 7c legend: "Increased activation of GSK3β was determined in the cerebellum, hippocampus and cerebral cortex of Wwox−/− mice at postnatal day 20, as evidenced by dephosphorylation of GSK3β at Ser9".
- Quantification: "Quantitative densitometry… the numbers depict the ratio of phosphorylated or total GSK3β to β-actin". These are ratio numbers, with no statistical test.
- Replication: "The representative results of four independent experiments are shown". The number of mice (n) per genotype is not stated.
- The legend does not name the comparator genotype; the text refers generally to three genotypes.
- The Western blotting Methods section names only anti-WWOX, anti-DCX and anti-β-actin, at P14. The p-GSK3β antibody is not described there.
- The readout is Ser9 phosphorylation as a proxy for activity. Kinase activity itself was not measured.

**K1. PARTIAL. Lithium half reached at abstract level; inhibitor half UNREACHABLE at the isoform-specific level.**
- Klein and Melton 1996 (PMID 8710892, doi 10.1073/pnas.93.16.8455), abstract read via PubMed: "Lithium potently inhibits GSK-3 beta activity (Ki = 2 mM), but is not a general inhibitor of other protein kinases."
  - The PMC tool returned an empty full text.
  - Europe PMC fullTextXML for PMC38692 returned HTTP 500 twice.
  - The assay details are therefore not read.
- Candidate for an unrelated chemical class: SB-216763 (Coghlan 2000, PMID 11033082, doi 10.1016/s1074-5521(00)00025-9), abstract only.
  - Quote: "structurally distinct maleimides that inhibit GSK-3alpha in vitro, with K(i)s of 9 nM and 31 nM respectively [SB-216763, SB-415286], in an ATP competitive manner. These compounds inhibited GSK-3beta with similar potency."
  - The abstract has no beta-specific number. I report none.
- Ring 2003 (PMID 12606497, doi 10.2337/diabetes.52.3.588), abstract only: aminopyrimidine derivatives, "inhibit human GSK-3 potently (K(i) < 10 nmol/l)". The isoform is not specified.
- Cross 2001 (PMID 11279265): the abstract gives no numeric values.
- The Cell Press DOI route returned only a redirect stub. I did not try other routes.
- Net: no GSK-3β-specific IC50 or Ki for a non-lithium selective inhibitor was read in any primary source. The abstract-level GSK-3α Ki for SB-216763 is the closest available.

Sources (PubMed): doi 10.1073/pnas.93.16.8455, 10.1016/s1074-5521(00)00025-9, 10.2337/diabetes.52.3.588, 10.1046/j.1471-4159.2001.t01-1-00251.x.
