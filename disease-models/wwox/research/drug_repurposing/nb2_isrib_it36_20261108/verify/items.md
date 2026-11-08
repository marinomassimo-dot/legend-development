# Items for a blind audit (IT36 P2/P3)

Check every item against the source named (open routes only; held full texts, if any, under /home/desktop/legend-development/files/). Verdicts per item: SUPPORTED / OVERSHOOT / UNDERSHOOT / NOT_IN_SOURCE / UNVERIFIABLE with the verbatim locator you found and the depth you reached. Roles 'counter' and 'context' are included; check them too.

# Part 1: NB-2 evidence rows (Tau and beta-catenin under GSK3 inhibitors)

## R1 (N1)
- paper_pmid: 21671254
- system: differentiated human SH-SY5Y (retinoic acid then BDNF), 1 h exposures to HTLV-I-infected MT-2 cell supernatant or K562 control supernatant
- inhibitors: LiCl (non-ATP-competitive); TDZD-8 (thiadiazolidinone, non-ATP-competitive class as the field classes it; the paper does not state a class)
- tau_readout: pT181 / total tau, Western: LiCl lowered basal pT181 and attenuated the MT-2 rise (five-fold to two-fold); no tau readout under TDZD-8
- catenin_readout: none under any inhibitor
- class_split: no: the two readouts were never measured under the same inhibitor in this paper
- locator_quote_max25words: Control cell preincubation with LiCl led to a significant decrease in T181 phosphorylation
- source_depth: partial_fulltext (PMC record via NCBI efetch: abstract, Introduction, Methods, Results, Discussion, Table I read; figure images not read, captions read)
- note: ROLE=counter (near miss). Two classes were used (LiCl, TDZD-8) and both tau and beta-catenin were blotted in one culture system, but the inhibitors were applied only to neurite length (both) and pT181 (LiCl only); beta-catenin was blotted only for MT-2 versus K562 supernatant, with no inhibitor. This is not a paired readout under inhibitor classes.

## R2 (N2)
- paper_pmid: 21671254
- system: same
- inhibitors: none
- tau_readout: not applicable
- catenin_readout: beta-catenin total protein, Western, normalised to total protein; MT-2 versus K562 only (Fig 4C)
- class_split: not applicable
- locator_quote_max25words: We observed no change in either phosphorylation or β-catenin (Fig. 4)
- source_depth: partial_fulltext (as N1)
- note: ROLE=context. Caption of Fig 4 states beta-catenin is expressed as pixel ratio to total protein; the readout is total, not nuclear or reporter activity. The paper uses the lack of change as an inference of unchanged GSK3 activity.

## R3 (N3)
- paper_pmid: 21671254
- system: same
- inhibitors: LiCl and TDZD-8
- tau_readout: pT181 read for LiCl only; TDZD-8 read for neurite length only
- catenin_readout: none
- class_split: none
- locator_quote_max25words: Neither LiCl nor TDZ-8 preincubations prevented the neurite retraction in SH-SY5Y cells treated with MT-2 cell supernatant
- source_depth: partial_fulltext (as N1)
- note: ROLE=counter. The two inhibitor classes agree on neurite length (no rescue), and the paper concludes CDK5 not GSK3 beta drives the pT181 rise; the lithium effect on pT181 is discussed by the authors as possibly via lowered CDK5/p25 rather than GSK3, so even the lithium tau result is not clean as a GSK3 readout.

## R4 (N4)
- paper_pmid: 16014628
- system: CHO cells and rat cultured cortical neurons
- inhibitors: LiCl; SB415286 (ATP-competitive)
- tau_readout: tau phosphorylation decreased under LiCl (site and assay not in abstract); SB415286 tau not stated
- catenin_readout: nuclear translocation of beta-catenin under LiCl and under SB415286
- class_split: undetermined
- locator_quote_max25words: the inhibition of GSK3 by LiCl induced the nuclear translocation of beta-catenin in Chinese hamster ovary cells and rat cultured neurons
- source_depth: abstract_only (carried from the IT35 row R1; full text NOT reached)
- note: ROLE=support (undecided). Prime source; unchanged by this session. Route this session: Europe PMC lists an open copy at a jbc.org PDF address (flag from its link list); one request returned a Cloudflare 'Just a moment' page, HTTP 403, 5,478 bytes. Stopped for the source. No PMC copy, not in the held corpus.

## R5 (N5)
- paper_pmid: 33621689
- system: differentiated human SH-SY5Y
- inhibitors: BIO (ATP-competitive), SB216763 (ATP-competitive), lithium
- tau_readout: Tau 1 (dephospho epitope) reduction by arsenite reversed by all three inhibitors
- catenin_readout: beta-catenin reduced in membrane fraction by arsenite; catenin under the inhibitors not stated in abstract
- class_split: undetermined
- locator_quote_max25words: GSK3 inhibitors, BIO, SB216763, and lithium, reversed the Tau 1 reduction by sodium arsenite
- source_depth: abstract_only (carried from the IT35 row R4; full text NOT reached)
- note: ROLE=support (undecided). Prime source; unchanged. Elsevier journal, Europe PMC shows no PMC copy or open flag, no preprint found (Europe PMC preprint-source title search: 0 hits); the DOI page was not requested because the publisher is subscription-only per Europe PMC.

## R6 (N6)
- paper_pmid: 20362550
- system: rat neurons treated with okadaic acid (PP2A inhibition), Western
- inhibitors: LiCl (non-ATP-competitive); 6-BIO (ATP-competitive, indirubin class)
- tau_readout: tau phosphorylation raised by okadaic acid and reversed by both inhibitors (site not in abstract)
- catenin_readout: beta-catenin phosphorylation raised by okadaic acid and reversed by both inhibitors (phosphorylation, not total or nuclear or reporter)
- class_split: no split reported: both readouts move together under both classes
- locator_quote_max25words: GSK3beta inhibitors such as lithium chloride and 6-bromoindirubin-3'-monoxime (6-BIO) reversed those phosphorylation events and protected neurons
- source_depth: abstract_only (PubMed record; no PMC copy)
- note: ROLE=support for 'move together' and the closest partial precedent: two classes, both readouts, one rat-neuron preparation. Limits: abstract; the catenin readout is its phosphorylation (a degron-priming readout), which does not separate total, nuclear and transcriptionally active catenin; 6-BIO also inhibits CDKs; sites, antibodies, magnitudes unknown.

## R7 (N7)
- paper_pmid: 11696357
- system: PC12 cells (neuron-like)
- inhibitors: SB-216763 and SB-415286 (ATP-competitive) versus FRAT1 overexpression (protein; GSK3 inhibition towards Axin/beta-catenin, not a small molecule)
- tau_readout: GSK3 activity towards Tau inhibited by FRAT1 and by both small molecules
- catenin_readout: GSK3 activity towards beta-catenin inhibited by FRAT1 and by both small molecules
- class_split: substrate-selective split exists but on glycogen synthase, not on Tau versus catenin: FRAT1 did not modulate GS, the small molecules did
- locator_quote_max25words: inhibition of GSK-3 activity towards Tau and beta-catenin, but not modulation of glycogen synthase (GS) activity
- source_depth: abstract_only (PubMed record; no PMC copy)
- note: ROLE=support (partial). Shows that substrates of one kinase can be separated by inhibitory mode in a neuron-like line; the split is GS versus Tau/catenin, so Tau and catenin still moved together. FRAT1 is a genetic perturbation, not an inhibitor class in the pharmacological sense.

## R8 (N8)
- paper_pmid: 11696357
- system: PC12 cells
- inhibitors: SB-216763 and SB-415286
- tau_readout: as N7
- catenin_readout: as N7
- class_split: as N7
- locator_quote_max25words: correlated with inhibition of GSK-3 activity towards GS in addition to Tau and beta-catenin
- source_depth: abstract_only
- note: ROLE=context. The small molecules hit all three substrates; neuroprotection was stronger with the small molecules than with FRAT1 per the abstract.

## R9 (N9)
- paper_pmid: 11279265
- system: primary central and peripheral neurones in culture, death induced by reduced PI 3-kinase activity
- inhibitors: SB-415286 and SB-216763 (two ATP-competitive compounds, one class)
- tau_readout: tau modulation correlated with protection
- catenin_readout: beta-catenin modulation correlated with protection
- class_split: not testable: one class
- locator_quote_max25words: correlated with inhibition of GSK-3 activity and modulation of GSK-3 substrates tau and beta-catenin
- source_depth: abstract_only (PubMed record; no PMC copy)
- note: ROLE=support for 'move together', single class. Which arm gave which magnitude is not in the abstract.

## R10 (N10)
- paper_pmid: 18266928
- system: human SH-SY5Y exposed to TRAIL
- inhibitors: SB216763 (ATP-competitive), one inhibitor
- tau_readout: tau phosphorylation raised by TRAIL; the effect of SB216763 on tau not stated in the abstract
- catenin_readout: cytoplasmic beta-catenin degradation raised by TRAIL; the effect of SB216763 on catenin not stated in the abstract
- class_split: not testable: one class, inhibitor effect on both readouts not stated
- locator_quote_max25words: both phosphorylation of glycogen synthase kinase 3 beta and degradation of cytoplasmic beta-catenin were increased, as well as phosphorylation of the tau protein
- source_depth: abstract_only (PubMed record; no PMC copy)
- note: ROLE=context. Insult pairs tau and catenin in one preparation; the inhibitor is used only for apoptosis rescue per the abstract.

# Part 2: ISRIB evidence rows

## R1 (EI01)
- source_id: 23741617
- system: chemical description in the first report of the compound
- finding: ISRIB is described as a symmetric bis-glycolamide with a central cyclohexane that exists as cis and trans diastereomers; the compound was a screen hit from a library of about 10^5 compounds.
- locator_quote: symmetric bis-glycolamide, containing a central bi-substituted cyclohexane, and can exist as two diastereomers, cis and trans
- depth: partial_fulltext (PMC record via NCBI efetch; Results, Methods chemistry and Discussion read; figure images not read, so the drawn structure in Figure 2A was not looked at)
- limits: text only; identical structure to the registry copies is argued from the name and synthesis, not from the drawing
- role: support

## R2 (EI02)
- source_id: 23741617
- system: Methods, chemical synthesis of the two isomers
- finding: The trans isomer is named with (1r,4r) cyclohexane stereodescriptors and made from the 1r,4r diamine; the cis isomer carries (1s,4s). The name matches the registry title 'trans-1,4-cyclohexanediyl' bis-amide.
- locator_quote: trans-ISRIB: 2-(4-Chlorophenoxy)-N-[(1r,4r)-4-[2-(4-chlorophenoxy)acetamido] cyclohexyl] acetamide
- depth: as EI01
- limits: the paper first describes the library hit and then states that both isomers were synthesised; it does not say that the screen sample was itself shown to be trans, only that trans is the potent isomer
- role: support

## R3 (EI03)
- source_id: 23741617
- system: HEK293T ATF4-luciferase reporter, thapsigargin-induced
- finding: Trans-ISRIB was about 100-fold more potent than cis in the cell reporter (in-vitro potency as source fact).
- locator_quote: Trans-ISRIB proved 100-fold more potent (IC50 = 5 nM) than cis-ISRIB (IC50 = 600 nM)
- depth: as EI01
- limits: the paper cautions that cis activity may be over-estimated by trans contamination
- role: support

## R4 (EI04)
- source_id: 23741617
- system: HEK293T and U2OS cells under ER stress
- finding: ISRIB does not block eIF2 alpha phosphorylation; it acts downstream of it.
- locator_quote: Unexpectedly, ISRIB did not block eIF2α phosphorylation under either of these ER stress-inducing conditions.
- depth: as EI01
- limits: cell lines, not neurons
- role: support

## R5 (EI05)
- source_id: 23741617
- system: MEFs with the mTOR inhibitor Torin-1
- finding: ISRIB did not restore translation lowered by mTOR inhibition: its translation effect is tied to eIF2 alpha phosphorylation, not to any translational block.
- locator_quote: addition of ISRIB did not reverse the effect of Torin-1 on translation
- depth: as EI01
- limits: one non-eIF2 block tested; does not cover a lowered eIF2B activity from other routes
- role: counter

## R6 (EI06)
- source_id: 23741617
- system: Figure 3 supplement 1 caption, HEK293T
- finding: The caption lists a Western blot for phospho S539-eIF2B epsilon and total eIF2B epsilon in cells with or without ER stress and ISRIB. The result is not described in the text read; the figure image was not looked at.
- locator_quote: phospho S539-eIF2Bε and total eIF2Bε in HEK293T cells treated with or without 2 µg/ml of tunicamycin
- depth: as EI01 (caption only)
- limits: S539 is the paper's label; its species numbering and its relation to the GSK3 site (rat 535, human 540) is not resolved here; module row E28 places the DYRK-annotated priming serine at rat 539 / human 544; no direction or magnitude read
- role: context

## R7 (EI07)
- source_id: 25875391
- system: reporter-based shRNA screen plus biochemistry; HEK293T and extracts
- finding: ISRIB is reported as an activator of eIF2B.
- locator_quote: We now report that ISRIB is an activator of eIF2B.
- depth: partial_fulltext (PMC record via NCBI efetch; Abstract, Results and Discussion read by section-directed passages; Methods and figure images not read)
- limits: as the authors' summary; the activator wording describes the abstract's own conclusion
- role: support

## R8 (EI08)
- source_id: 25875391
- system: HEK293T extracts, sucrose gradient
- finding: ISRIB shifts eIF2B to a larger complex consistent with dimerisation of the four-subunit assembly; eIF2B4 (delta) is named as contributing to the binding site.
- locator_quote: show ISRIB-mediated stabilization of activated eIF2B dimers, and suggest that eIF2B4 (δ-subunit) contributes to the ISRIB binding site
- depth: as EI07
- limits: the 2018 structures later place the pocket at the beta-delta interface; 'dimers' here means two tetramer-sized units in the authors' gradient
- role: support

## R9 (EI09)
- source_id: 25875391
- system: HEK293T shRNA reporter screen
- finding: Knock-down of eIF2B4 and of eIF2B5 (epsilon) lowered cells' sensitivity to ISRIB without changing reporter induction; the authors read this as less enzyme available to activate. This is a requirement for the subunit, not evidence of ISRIB binding to epsilon.
- locator_quote: two subunits of eIF2B, eIF2B4 and eIF2B5, that significantly reduced the sensitivity
- depth: as EI07
- limits: knock-down result; not binding; no phospho-epsilon measurement
- role: context

## R10 (EI10)
- source_id: 25875391
- system: in-vitro exchange with phosphorylated eIF2 mixed in
- finding: ISRIB stimulated exchange when unphosphorylated eIF2 outnumbered phosphorylated eIF2 three to one, and hardly at one to one: the ratio of substrate to inhibitor sets how much ISRIB can do.
- locator_quote: whereas we observed hardly any stimulation at the 1:1 ratio
- depth: as EI07
- limits: partially purified rabbit eIF2B and recombinant substrates; two replicates
- role: counter

## R11 (EI11)
- source_id: 25875391
- system: in-vitro exchange, partially purified eIF2B, no phosphorylated eIF2
- finding: Without phosphorylated eIF2 present, ISRIB made exchange about three-fold faster in this assay.
- locator_quote: GDP release was threefold faster upon addition of ISRIB (t1/2 = 1.1 min)
- depth: as EI07
- limits: contradicted at the recombinant-decamer level by EI15 and by module row E21; assay preparations differ
- role: counter

## R12 (EI12)
- source_id: 25875391
- system: in-vitro exchange
- finding: ISRIB does not make phosphorylated eIF2 a substrate.
- locator_quote: determined that ISRIB does not enable eIF2B to use eIF2-P as a substrate
- depth: as EI07
- limits: 
- role: support

## R13 (EI13)
- source_id: 29599245
- system: cryo-EM of endogenous human eIF2B from HeLa cells with ISRIB
- finding: ISRIB sits at the interface of the beta and delta regulatory subunits.
- locator_quote: with an ISRIB molecule bound at the interface between the β and δ regulatory subunits
- depth: partial_fulltext (PMC record via NCBI efetch; author manuscript, main text incl. Results and Discussion; supplementary figures not read)
- limits: 4.1 angstrom map; the catalytic epsilon domain is not resolved
- role: support

## R14 (EI14)
- source_id: 29599245
- system: structure discussion
- finding: The authors note that the catalytic domain of epsilon is resolved in neither structure, so an allosteric effect on epsilon could have been missed.
- locator_quote: the critical catalytic domain of the ε subunit is resolved in neither structure
- depth: as EI13
- limits: a limit stated by the authors, not a result
- role: context

## R15 (EI15)
- source_id: 29599213
- system: recombinant human eIF2B decamer, nucleotide exchange assay (no phosphorylated eIF2)
- finding: At the recombinant decamer level ISRIB did not significantly accelerate exchange, in contrast to the earlier three-fold report (EI11).
- locator_quote: ISRIB did not significantly activate the recombinant eIF2B decamer
- depth: partial_fulltext (PMC record via NCBI efetch; Abstract, Results (assays, structure, mutants) read; later Results and Discussion by selected passages; Methods, supplement and figure images not read)
- limits: one substrate concentration (sub-saturating, per the text)
- role: counter

## R16 (EI16)
- source_id: 29599213
- system: cryo-EM 2.8 angstrom, human decamer with ISRIB
- finding: ISRIB bridges the two tetramers across the central symmetry interface and favours decamer assembly.
- locator_quote: ISRIB promoted this step by cross-bridging a central symmetry interface
- depth: as EI15
- limits: 
- role: support

## R17 (EI17)
- source_id: 29599213
- system: in-vitro tetramer assembly
- finding: Dose-response is bell-shaped in vitro: ISRIB promoted octamer assembly at a lower concentration and failed at a ten-fold higher one (source concentrations, in-vitro only).
- locator_quote: ISRIB promoted eIF2B(βγδε)2 assembly at 1 μM but failed to do so at 10 μM
- depth: as EI15
- limits: an in-vitro, tetramer-only system; the ten-fold higher cell range tested elsewhere (EI21) shows the survival effect over a wide range, so the in-vitro shape is not shown to hold in neurons
- role: counter

## R18 (EI18)
- source_id: 29599213
- system: structure text
- finding: The catalytic HEAT domain of epsilon is not resolved in the structure; ISRIB contacts the beta and delta subunits, not epsilon.
- locator_quote: the catalytic HEAT domains of the ε subunits were not resolved
- depth: as EI15
- limits: absence of density, not absence of an epsilon effect
- role: context

## R19 (EI19)
- source_id: 29599213
- system: structure text, drawn modelling of the ligand
- finding: The modelled ligand is described with its side chains on 'the same face' of the cyclohexane ring in the chair form. Without the figure this wording cannot be read as cis or trans; it is flagged, not concluded.
- locator_quote: with the side chains projecting to the same face of the cyclohexane ring
- depth: as EI15; figure not looked at
- limits: wording only; the figure and supplement S4-S5 would settle it; the trans identity in this entry rests on EI02 and the registry title
- role: counter

## R20 (EI20)
- source_id: 29599213
- system: Discussion, mechanism
- finding: A limiting amount of phosphorylated eIF2 would be offset by the extra exchange activity ISRIB provides: ISRIB is framed as a partial offset of the phospho-eIF2 brake.
- locator_quote: The inhibition resulting from a limiting amount of phosphorylated eIF2 would be reduced by the surplus of GEF activity provided by ISRIB.
- depth: as EI15
- limits: author interpretation
- role: support

## R21 (EI21)
- source_id: 32457286
- system: primary rat cortical neurons expressing mutant SOD1 (G93A), longitudinal single-neuron imaging; HEK293 for comparison
- finding: ISRIB raised survival of neurons expressing the mutant protein over a wide concentration range; the readout is survival by longitudinal microscopy plus a UPR transcriptional reporter.
- locator_quote: significantly enhanced the survival of G93A SOD1-expressing neurons
- depth: partial_fulltext (PMC record via NCBI efetch; Abstract, Results and Discussion by selected passages; Methods mostly not read, figure images not read)
- limits: mutant-SOD1 model; the paper itself notes it cannot exclude eIF2 alpha kinases other than PERK
- role: support

## R22 (EI22)
- source_id: 32457286
- system: same, thapsigargin ER stress
- finding: In these neurons ISRIB did not reduce ATF4 (nor CHOP translation) as it did in HEK293; GSK2606414 did. ISRIB still relieved the general translation block. The ATF4 readout is therefore not a reliable engagement readout in cultured rat cortical neurons.
- locator_quote: unlike in HEK293 cells, ISRIB did not reduce ATF4 expression in Thap-treated neuronal cultures
- depth: as EI21
- limits: one neuronal type, one stressor
- role: counter

## R23 (EI23)
- source_id: 32457286
- system: same, alpha-synuclein E46K neurons
- finding: The survival effect was selective: ISRIB did not help neurons expressing the other toxic protein.
- locator_quote: ISRIB did not improve the survival of E46K aSyn expressing neurons
- depth: as EI21
- limits: 
- role: counter

## R24 (EI24)
- source_id: 32457286
- system: Discussion (citing Rabouw et al.)
- finding: A cited finding that ISRIB works only below a critical level of phosphorylated eIF2 alpha; the authors also raise that neuronal eIF2B phosphorylation could change translation initiation. Both are statements in a discussion, not tests.
- locator_quote: ISRIB antagonizes the ISR only when p-eIF2α levels are below a critical threshold
- depth: as EI21
- limits: citing_primary: the source is another paper, not read here
- role: context

## R25 (EI25)
- source_id: 33531382
- system: mouse AD models; ex vivo hippocampal slices exposed to amyloid-beta oligomers; SUnSET protein synthesis
- finding: ISRIB corrected the oligomer-driven lowering of hippocampal protein synthesis; readout SUnSET puromycin labelling, with memory and synaptic readouts in vivo.
- locator_quote: ISRIB corrects AβO-instigated eIF2α-P-dependent hippocampal translational repression
- depth: partial_fulltext (PMC record via NCBI efetch; Abstract, Results, Discussion by selected passages; Methods and figure images not read)
- limits: models of eIF2 alpha phosphorylation; no GSK3 or WWOX link
- role: support

## R26 (EI26)
- source_id: 33531382
- system: wild-type mice
- finding: The authors report no noticeable biochemical or cognitive effect of their regimen in wild-type control animals, in line with ISRIB acting under raised phosphorylated eIF2 alpha.
- locator_quote: without noticeable biochemical or cognitive effects in WT control mice
- depth: as EI25
- limits: the statement is the authors' summary; no administered-dose number reproduced here
- role: support

## R27 (EI27)
- source_id: 33531382
- system: mice given the eIF2 alpha phosphatase inhibitor salubrinal
- finding: ISRIB did not stop phosphorylated eIF2 alpha from rising: it acts downstream of the modification, in vivo as in cells.
- locator_quote: ISRIB did not prevent the increase in hippocampal eIF2α-P caused by salubrinal administration in mice
- depth: as EI25
- limits: 
- role: support

## R28 (EI28)
- source_id: 33220178
- system: recombinant eIF2B and CHO cells (module row E20, carried; not re-read here)
- finding: In cells ISRIB's efficacy as an ISR inhibitor depends on the presence of phosphorylated eIF2.
- locator_quote: ISRIB’s efficacy as an ISR inhibitor in cells also depends on presence of eIF2(αP)
- depth: carried from module row E20 (partial_fulltext in the earlier package)
- limits: not re-read in this session
- role: support

## R29 (EI29)
- source_id: 29489452
- system: recombinant eIF2B and HEK293T lines with vanishing-white-matter mutations (module row E25, carried)
- finding: ISRIB can restore stability and residual activity of destabilised mutant eIF2B including epsilon-subunit mutations; rescue assays included phosphorylated eIF2.
- locator_quote: ISRIB stabilizes VWMD mutant eIF2B in the decameric form and restores the residual catalytic activity to wild-type levels
- depth: carried from module row E25
- limits: not re-read in this session; the epsilon mutants rescued are not near the GSK3 serine per the module audit
- role: context

## R30 (EI30)
- source_id: 12133000
- system: CHO cells, GSK3 inhibitors (PMC record abstract; second route to the same depth)
- finding: Dephosphorylation of the GSK3 serine by three inhibitors did not give significant activation of eIF2B: the GSK3 serine alone did not raise exchange in this system.
- locator_quote: these compounds did not elicit significant activation of eIF2B
- depth: abstract_only again: NCBI efetch of the PMC record returned the abstract and metadata, no body
- limits: the earlier failures (Europe PMC XML 500, PMC page challenge) are not repeated; this is a new route with the same depth
- role: counter

## R31 (EI31)
- source_id: identity
- system: registry copies (module note, branch task/isrib-identity)
- finding: The ChEMBL and FDA-SRS records share the full InChIKey; the SRS molfile title says trans-1,4-cyclohexanediyl.
- locator_quote: N,N'-trans-1,4-Cyclohexanediylbis[2-(4-chlorophenoxy)acetamide]
- depth: database_record (read from the identity note on its branch)
- limits: registry copies; the note itself says agreement of two registries is not independent confirmation
- role: support

## R32 (EI32)
- source_id: repo
- system: repository chain table (module gsk3_eif2b README, carried)
- finding: No WWOX system has been measured for the GSK3-to-eIF2B-epsilon link or for ISRIB.
- locator_quote: The chain is not established.
- depth: carried from the module README
- limits: 
- role: counter

## R33 (EI33)
- source_id: repo
- system: repository chain table (module gsk3_eif2b README, carried)
- finding: Compensation of a GSK3-site defect by ISRIB is a prediction to test, not a premise.
- locator_quote: ISRIB compensating a GSK3-site defect is therefore a prediction to test, not a premise.
- depth: carried from the module README
- limits: 
- role: counter

# Part 3: ISRIB probe entry statements by layer

## PE1
- layer: identity
- statement: ISRIB is the trans-1,4-cyclohexane bis(4-chlorophenoxyacetamide); the first report names the trans isomer with (1r,4r) descriptors and shows it as the 100-fold more potent isomer. Evidence rows EI01 to EI03.
- source_id: 23741617
- source_kind: primary
- independence_group: paper_sidrauski2013
- locator_quote_max25words: trans-ISRIB: 2-(4-Chlorophenoxy)-N-[(1r,4r)-4-[2-(4-chlorophenoxy)acetamido] cyclohexyl] acetamide
- depth: partial_fulltext (name, synthesis and potency read; the drawn structure in Figure 2A not looked at)
- limit: the paper's text gives the same constitution and trans configuration as the registry title; whether the registry title was itself taken from this literature is not known, so the match is not shown to be independent of the registry copies (the registries may have copied the paper, or the paper's structure; they could not be shown to be separate derivations)
- not_shown: the identity of the sample first screened with the synthesised trans isomer; the figure; a statement that the registry copied or did not copy the paper

## PE2
- layer: identity
- statement: ChEMBL CHEMBL4303573 and the FDA-SRS record named ISRIB (UNII S6SZR97SBZ) share the full InChIKey; reused as given from the branch note.
- source_id: identity:task/isrib-identity
- source_kind: database
- independence_group: registry_copies
- locator_quote_max25words: N,N'-trans-1,4-Cyclohexanediylbis[2-(4-chlorophenoxy)acetamide]
- depth: database_record (identity note on its branch read)
- limit: the two registries are not independent of each other or necessarily of the paper (EI31)
- not_shown: a mechanism, target, activity or approval; the molecule's absence from the catalogue is the earlier note's finding

## PE3
- layer: identity
- statement: Cryo-EM density was fitted by a model of the ligand (chair cyclohexane); the text also says the side chains project 'to the same face' of the ring, which cannot be read as cis or trans without the figure. Flagged, not resolved.
- source_id: 29599213
- source_kind: primary
- independence_group: structure_B_zyryanova2018
- locator_quote_max25words: with the side chains projecting to the same face of the cyclohexane ring
- depth: partial_fulltext (text; supplement figure not looked at)
- limit: a map at this resolution fits a modelled ligand; it is an independent dataset from the 2013 chemistry only in the sense that it is a different method
- not_shown: the cis or trans assignment from the structure; figure S4-S5

## PE4
- layer: mechanism
- statement: ISRIB binds eIF2B at the interface between the beta and delta regulatory subunits (cryo-EM of endogenous human complex). LINK SUPPORTED: binding to the eIF2B complex. LINKS NOT SUPPORTED by this source: action on the epsilon subunit, the GSK3 serine, any WWOX system. Rows EI13.
- source_id: 29599245
- source_kind: primary
- independence_group: structure_A_tsai2018
- locator_quote_max25words: with an ISRIB molecule bound at the interface between the β and δ regulatory subunits
- depth: partial_fulltext (author manuscript; supplement not read)
- limit: 4.1 angstrom; catalytic epsilon domain not resolved; independence from the structure_B paper is by the papers' own account (a companion pair) and author overlap was not checked
- not_shown: a binding site on epsilon; any phospho-state dependence of binding

## PE5
- layer: mechanism
- statement: ISRIB cross-bridges the central symmetry interface of the decamer and favours assembly from two tetramers; at the recombinant decamer it did not significantly raise exchange, unlike the 2015 extract assay. LINK SUPPORTED: binding to and stabilising the eIF2B complex. Rows EI15, EI16, EI18.
- source_id: 29599213
- source_kind: primary
- independence_group: structure_B_zyryanova2018
- locator_quote_max25words: ISRIB promoted this step by cross-bridging a central symmetry interface
- depth: partial_fulltext (selected Results, Discussion passages)
- limit: the exchange result depends on preparation (EI11 versus EI15); the epsilon HEAT domain is unresolved
- not_shown: the effect of ISRIB on a decamer carrying the GSK3 serine in any state

## PE6
- layer: mechanism
- statement: ISRIB is reported as an activator of eIF2B, stabilises its larger assembly, and its effect shrinks when phosphorylated eIF2 equals the substrate (1:1) while it works at 3:1. Nature of the action: an activator that offsets the phospho-eIF2 brake by allostery/assembly, not an eIF2 alpha dephosphorylator (it does not block the phosphorylation, EI04). LINK SUPPORTED: binding/activation of the complex; partial-brake dependence. Rows EI07, EI10, EI12.
- source_id: 25875391
- source_kind: primary
- independence_group: paper_sidrauski2015
- locator_quote_max25words: whereas we observed hardly any stimulation at the 1:1 ratio
- depth: partial_fulltext (selected Results and Discussion passages)
- limit: partially purified rabbit eIF2B in the exchange assay; two replicates
- not_shown: reversibility of the effect (not found in the passages read); behaviour in a resistant (high phospho-eIF2) ISR beyond the 1:1 assay

## PE7
- layer: mechanism
- statement: What ISRIB does without phosphorylated eIF2: in cells and animals it is reported to modify the ISR under raised phosphorylated eIF2 alpha and not under basal conditions; in a recombinant assay devoid of phosphorylated eIF2 it only minimally accelerated exchange; in the 2015 extract assay with no phosphorylated eIF2 it gave a three-fold gain. The sources disagree on the basal exchange effect. Rows EI11, EI15, EI26, EI28.
- source_id: 33531382
- source_kind: citing_primary
- independence_group: paper_oliveira2021
- locator_quote_max25words: without noticeable biochemical or cognitive effects in WT control mice
- depth: partial_fulltext (selected passages)
- limit: the in-vivo sentence is the authors' summary; the basal in-vitro result differs between assays (EI11 versus EI15)
- not_shown: a systematic test of ISRIB with the ISR off in a neuron; the effect of ISRIB on a non-phospho-eIF2 lesion of eIF2B (the module found none, except structural lesions where phosphorylated eIF2 was present)

## PE8
- layer: mechanism
- statement: Resistant or partial ISR: a cited finding that ISRIB antagonises the ISR only below a threshold of phosphorylated eIF2 alpha; the in-vitro 1:1 data fit this. Dose-response is bell-shaped in the tetramer system (stimulation at the lower in-vitro concentration, none at the ten-fold higher one), source facts only. Rows EI10, EI17, EI24.
- source_id: 32457286
- source_kind: citing_primary
- independence_group: paper_rabouw_cited_via_cruz2020
- locator_quote_max25words: ISRIB antagonizes the ISR only when p-eIF2α levels are below a critical threshold
- depth: partial_fulltext (the quoted sentence is in a Discussion that cites another paper, not read here)
- limit: a cited statement; the bell shape is in vitro and a tetramer-only system
- not_shown: reversibility after washout; any statement of what the threshold is in a neuron

## PE9
- layer: mechanism
- statement: Epsilon subunit and the GSK3 serine: ISRIB reduces its own effect when eIF2B5 (epsilon) is knocked down (an abundance requirement), the pocket is on beta and delta, the epsilon catalytic domain is unresolved, and the 2013 paper's Western panel includes a phospho-epsilon blot at a serine labelled 539 whose result was not read. LINK NOT SUPPORTED: ISRIB action on the single subunit EIF2B5 as binding; ISRIB effect on the GSK3-regulated serine (rat 535 / human 540). Rows EI06, EI09, EI14, EI18.
- source_id: 25875391
- source_kind: primary
- independence_group: paper_sidrauski2015
- locator_quote_max25words: two subunits of eIF2B, eIF2B4 and eIF2B5, that significantly reduced the sensitivity
- depth: partial_fulltext (selected passages; caption of the 2013 supplement figure read, image not)
- limit: the 2013 phospho-epsilon panel result is not read; species numbering of S539 unresolved
- not_shown: any measurement of phospho-epsilon at the GSK3 serine under ISRIB; any ISRIB binding to epsilon

## PE10
- layer: function
- statement: Neural system 1: primary rat cortical neurons with a mutant SOD1 allele: ISRIB raised survival (longitudinal microscopy) and lowered a UPR reporter; in the same neurons ISRIB did not lower ATF4 under thapsigargin. Readouts named: neuron survival, UPR transcriptional reporter, ATF4, global translation. Rows EI21, EI22.
- source_id: 32457286
- source_kind: primary
- independence_group: paper_cruz2020
- locator_quote_max25words: unlike in HEK293 cells, ISRIB did not reduce ATF4 expression in Thap-treated neuronal cultures
- depth: partial_fulltext (selected passages)
- limit: rat cortical neuron culture, mutant SOD1 model; the authors cannot exclude other eIF2 alpha kinases
- not_shown: an effect on a WWOX-deficient neuron; engagement by a direct eIF2B assay in these neurons

## PE11
- layer: function
- statement: Neural system 2: mouse hippocampal slices and AD-model mice: ISRIB corrected the oligomer-driven lowering of protein synthesis (SUnSET readout), and rescued plasticity and memory readouts. Readout named: SUnSET puromycin labelling. Rows EI25 to EI27.
- source_id: 33531382
- source_kind: primary
- independence_group: paper_oliveira2021
- locator_quote_max25words: ISRIB corrects AβO-instigated eIF2α-P-dependent hippocampal translational repression
- depth: partial_fulltext (selected passages)
- limit: eIF2 alpha phosphorylation models; no GSK3 content
- not_shown: a developmental or seizure model; any cellular readout of a GSK3 serine

## PE12
- layer: function
- statement: Counter: the survival benefit was model-specific (not seen with the alpha-synuclein variant) and the ATF4 readout did not follow in neurons.
- source_id: 32457286
- source_kind: primary
- independence_group: paper_cruz2020
- locator_quote_max25words: ISRIB did not improve the survival of E46K aSyn expressing neurons
- depth: partial_fulltext (selected passages)
- limit: same paper as the support row; counter rows from one paper do not make a second source
- not_shown: a general neuroprotective claim

## PE13
- layer: wwox_transfer
- statement: Repository support for a WWOX use: a single-lane Ser9 blot in Wwox-null mouse brain, a knock-down abstract in SK-N-SH, and GSK3-to-eIF2B-epsilon precedents in other contexts. The module's own summary is that the chain is not established.
- source_id: repo:gsk3_eif2b_20261107/output/README.md
- source_kind: database
- independence_group: repository_record
- locator_quote_max25words: The chain is not established.
- depth: repository text (module README read)
- limit: no WWOX translation, eIF2B or ISR-axis measurement found by the module; P20 follows seizure onset in a malformed brain
- not_shown: any ISRIB experiment in a WWOX system

## PE14
- layer: wwox_transfer
- statement: Repository does not support: the GSK3-site phosphorylation did not give significant eIF2B activation in the system that tested it (abstract), ISRIB has not been tested on a phospho-epsilon lesion, and compensation is a prediction. Rows EI30, EI33.
- source_id: 12133000
- source_kind: primary
- independence_group: paper_12133000
- locator_quote_max25words: these compounds did not elicit significant activation of eIF2B
- depth: abstract_only (a second route, PMC efetch, again returned the abstract only)
- limit: abstract only; the earlier Europe PMC XML 500 and PMC page challenge are not repeated
- not_shown: the full text and the exchange assay

## PE15
- layer: wwox_transfer
- statement: Discriminating use: an ISRIB arm in the same preparation distinguishes a phospho-eIF2-driven ISR from a GSK3-to-eIF2B-epsilon route only if three things are measured beside it: phospho-eIF2 alpha, phospho-epsilon at the GSK3 serine, and an ISRIB-engagement check in a positively stressed arm of the same culture. Outcome grid in the README. IPOTESI, no source tests it.
- source_id: repo:gsk3_eif2b_20261107/output/README.md
- source_kind: database
- independence_group: repository_record
- locator_quote_max25words: ISRIB compensating a GSK3-site defect is therefore a prediction to test, not a premise.
- depth: repository text (module README read)
- limit: a design proposal; ISRIB's neuron ATF4 readout is unreliable (EI22) and its bell-shaped in-vitro dose-response argues for a dose series, not a single concentration
- not_shown: its result; whether the engagement control works in a WWOX-deficient human neuron

## PE16
- layer: wwox_transfer
- statement: When ISRIB would be uninformative or confounding: (1) the ISR is not on and phospho-eIF2 alpha is not raised (nothing to offset); (2) ATF4 is used as the only readout in neurons; (3) a rescue appears without raised phospho-eIF2, which fits a general rise of eIF2B activity (EI11, EI29) and does not exclude the GSK3 route; (4) a translation defect of mTOR type, which ISRIB does not repair (EI05); (5) a single high dose in the range where the in-vitro effect fades (EI17); (6) GSK3 inhibitors that change protein synthesis by routes other than epsilon (module row E07).
- source_id: 33531382
- source_kind: citing_primary
- independence_group: paper_oliveira2021
- locator_quote_max25words: ISRIB did not prevent the increase in hippocampal eIF2α-P caused by salubrinal administration in mice
- depth: partial_fulltext (selected passages)
- limit: the quote shows ISRIB leaves phospho-eIF2 alpha intact, so phospho-eIF2 alpha must be measured beside it; the list is the reviewer's inference from rows cited
- not_shown: none of these conditions was tested in a WWOX system

# Part 4: propositions to check as units (these decide)
- U1. The ISRIB-binding pocket of eIF2B is formed by the beta and delta subunits at the interface of the decamer, not by the epsilon subunit; the epsilon catalytic domain is not resolved in the structures. Sources: PMID 29599245 and PMID 29599213.
- U2. ISRIB leaves phospho-eIF2alpha unchanged and acts by restoring eIF2B activity under phospho-eIF2alpha inhibition; sources disagree on basal exchange activity without stress (an extract assay versus a recombinant decamer).
- U3. In rat cortical neurons ISRIB did not lower ATF4 under thapsigargin (unlike HEK293) while relieving the translation block (PMID 32457286 and/or 33531382: check which, and the exact system).
- U4. The trans-1,4-cyclohexane isomer of ISRIB is about 100-fold more potent than the cis isomer in the cell reporter (PMID 23741617); the paper names the trans isomer with (1r,4r) descriptors.
- U5. In PMID 21671254 LiCl and TDZD-8 were used, both Tau and beta-catenin were blotted, but the two readouts were not crossed under both inhibitors (pT181 only under LiCl, beta-catenin only without an inhibitor, TDZD-8 only on neurite length).
- U6. In PMID 20362550 (abstract), in okadaic-acid-treated rat neurons lithium and 6-BIO both reversed the phosphorylation of Tau, beta-catenin and CRMP2.
