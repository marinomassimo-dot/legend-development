# Sixty hypotheses (statement and discriminating manipulation only)

## Z01
Statement: Pentamer assembly and export are limited by biogenesis factors (EMC and LHFPL4-class), so raising the factor, but not the partner subunit supply, raises mutant surface and current.
Discriminating manipulation (vs H7 and (a rival), partner overexpression): knock out the factor and test the mutant with partner levels held constant, in a partner-null background. Predicted: the mutant's surface and current fall further, and the factor (not the partner) rescues them. Partner overexpression raises partner surface but not the tagged-mutant surface.

## Z02
Statement: The mutant does reach the plasma membrane, but faster clathrin/AP2- and dynamin-dependent endocytosis removes it. The loss is post-ER, and blocking endocytosis raises surface subunit and current.
Discriminating manipulation: Acute dynamin/AP2 blockade versus ER-export enhancement (H1). Use a tagged mutant so the effect on wild-type receptors can be excluded. - Genetic blockade: dominant-negative dynamin, or AP2μ2 knockdown. - Under endocytic block: surface ↑ and current ↑ in proportion to functional channels. The EndoH-resistant (post-ER) pool of the mutant is detectable beforehand. - Under H1: surface ↑ with no dependence on endocytosis. - If the loss is ER-based: dynamin block leaves mutant surface and current flat.

## Z03
Statement: Folded mutant subunits are held back by a defect in ER export, specifically palmitoylation-dependent or COPII-dependent exit, so enhancing export raises surface expression.
Discriminating manipulation vs H1: raise the activity of the palmitoyl-transferase ZDHHC3/7 (genetic) in the mutant neuron. Predicts total protein unchanged, surface up, and GABA-evoked current up in proportion. H1 predicts no effect, since H1's lesion is clearance upstream of export.

## Z04
Statement: Hsp90 engagement commits the mutant to degradation, so inhibiting it raises surface subunit and current. Hsp70-axis induction does not rescue and can accelerate loss.
Discriminating manipulation: Hsp90 loss (genetic isoform knockdown with HSF1 held constant, to avoid heat-shock co-induction) versus Hsp70 gain. - Hsp90 loss: total ↑, surface ↑, current ↑. - Hsp70 gain: surface flat or ↓, current flat or ↓. The ER (BiP) arm and the cytosolic arm must be separated.

## Z05
Statement: The variant subunit is recognised as misfolded and removed by ER-associated degradation although it is partly assembly-competent, so slowing that clearance (an ERAD E3, SEL1L/HRD1 or p97 manipulation) raises ER pool, surface expression and current.
Discriminating manipulation (vs H1): genetic knockdown of HRD1/SEL1L (or a p97 class) with a folding-chaperone arm held constant. Predicted: surface and current rise only if the retained pool is exportable. Under H1 the same knockdown produces no additional surface gain.

## Z06
Statement: Selective activation of the ATF6 arm of the unfolded-protein response raises ER folding capacity (BiP, calnexin, PDI), which increases the post-ER fraction, surface subunit and GABA-evoked current of the missense subunit.
Discriminating manipulation (vs nearest rival H6, the HDAC-class chemical chaperone): inducible ATF6 active fragment in the mutant background, PERK and IRE1 held constant, with BiP knocked down in a parallel arm. Predicted: surface and current rise together, and the rise is lost with BiP knockdown. The rival (HDAC-class, transcription-dependent) would be insensitive to BiP knockdown. Both would raise surface and current if either works. Only BiP dependence separates them.

## Z07
Statement: Much of the mutant's loss goes through a K63-ubiquitin / lysosomal route, not proteasomal ERAD, so blocking ERAD/p97 raises total protein but leaves surface and current unchanged.
Discriminating manipulation (vs (a rival), SEL1L-HRD1 knockdown): run the SEL1L/HRD1 knockdown and a lysosomal-acidification/ER-phagy block side by side in the same cells. Predicted for this reading: only the lysosomal arm lengthens half-life and raises surface and current, and the ERAD arm raises total protein only. ERAD-first predicts the reverse.

## Z08
Statement: Prolonged calnexin/UGGT1 reglucosylation cycling retains the mutant in the ER, so shortening the cycle (UGGT1 loss, or a glucosidase-inhibitor class) releases it for export and raises surface and current.
Discriminating manipulation (vs nearest rival H8, clearance by a lysosomal route): UGGT1 knockout in the mutant background. Predicted: the Endo-H-resistant fraction and surface rise with no change in half-life, and current rises in step with surface. The rival would show no change in the Endo-H-resistant fraction, because it acts after export.

## Z09
Statement: A ligand-site pharmacological chaperone, washed out before recording, stabilises the folding intermediate and raises surface subunit. Current rises only if the rescued mutant gates.
Discriminating manipulation: A ligand-site chaperone class with washout versus a gating-only positive allosteric modulator present during recording (a rival). - Chaperone after washout: surface ↑, and current ↑ if gating is intact. If surface rises and current stays flat, the receptor is the GABA-A analogue of stable-but-inert. - PAM, with no washout: surface unchanged, current ↑ only while the drug is present, and it vanishes on washout.

## Z10
Statement: A ligand-binding-site-competent variant can be stabilised in the ER by a ligand-site pharmacological chaperone (an orthosteric or allosteric-site binder class), so surface density rises, and current rises once the ligand is washed out.
Discriminating manipulation (vs H1): a binding-site-dead double mutant (genetic). H10 predicts the gain vanishes when the site is dead and survives only if the site is intact. H1's non-site-specific folding gain is the same in either construct. Current prediction: under H10, evoked current rises only after washout. **Cross-cutting control (INFERENZA from the folder).** GABA-evoked current depends on driving force as well as on receptor number. Perforated-patch E_GABA and V_rest in the same cell (`research/commit_candidates/CC-20260826-EGABA-EXPERIMENT-01.md` §2, `CC-20260826-EGABA-CLOSURE-01.md` §2) are needed to separate a chloride-gradient change from a surface-density change. Otherwise a current gain under any lever above can be misread as a surface effect. Recording temperature matters (KCC2 transport is temperature-dependent; same file, §3b). **What this folder cannot support.** Whether these subunit variants lose protein by degradation or by stalled synthesis is undiscriminated. The folder's own WWOX repair shows that conflation is a standing error (`proteostasis_rationale.md` §4: "Synthesis, insolubility and turnover are three separate questions"). Ranking H1 to H10 against each other would be false precision.

## Z11
Statement: The variant causes haploinsufficiency, so adding a wild-type copy under a neuron-restricted promoter restores surface receptors and current in proportion to dose.
Discriminating manipulation (vs H5): AAV or genetic expression of the wild-type subunit under a pan-neuronal vs interneuron-restricted promoter. Predicted: surface and current rise only if haploinsufficient. Under a dominant-negative mutant, surface and current stay low or fall.

## Z12
Statement: Surface residency of the variant depends on phosphorylation of the intracellular loop (a PKA/PKC/Akt or phosphatase-class balance), so shifting kinase-phosphatase balance stabilises surface receptors and current.
Discriminating manipulation (vs H7): phospho-null and phospho-mimetic variants of the same site. H9 predicts surface and current follow the phospho-state independently of dynamin block. H7 predicts the effect disappears when internalisation is blocked.

## Z13
Statement: Function is restored by upregulating a paralogous subunit (for example another β or α) that substitutes for the lost subunit, in the cell type where loss matters most (inhibitory interneurons rather than pyramidal cells).
Discriminating manipulation: Versus H1–H6, cell-type-specific viral or CRISPRa upregulation of the paralog, with the mutant allele silenced. Predicts mutant-subunit surface unchanged and current up. Any H1–H6 lever predicts mutant surface up.

## Z14
Statement: Raising expression of the wild-type allele (promoter/enhancer-directed dCas9 activation) compensates for haploinsufficiency. Surface and current rise in proportion to dose when the wild-type protein itself is processed normally. It fails if partner assembly or post-translational loss is limiting.
Discriminating manipulation: Wild-type-allele-specific activation versus co-expression of the missing partner subunits at fixed wild-type dose (a rival). - If dosage-limited: WT activation gives surface ↑ and current ↑ with a graded dose-response, and extra partner adds nothing. - If assembly-limited: partner co-expression rescues and WT activation plateaus.

## Z15
Statement: Post-ER disposal of the mutant is lysosomal (autophagic, ER-phagy or Golgi-to-lysosome), not proteasomal. Blocking it raises total mutant. Surface and current rise only if the retained pool is export-competent.
Discriminating manipulation: Lysosomal-proteolysis blockade (acidification/protease-block class), with ATG5 loss versus FAM134B loss to split macroautophagy from ER-phagy, against a proteasome-inhibitor class. - Lysosome block: total ↑, and the EndoH-resistant pool, surface and current ↑ only if the mutant exports. - Proteasome block: ER pool (EndoH-sensitive) ↑, surface flat, current flat.

## Z16
Statement: Post-ER trafficking is the block: palmitoylation (ZDHHC3/GODZ) and Golgi export (e.g. BIG2/ARF-dependent) are limiting, so raising them forwards more mutant-containing receptors to the surface.
Discriminating manipulation (vs. H2): ZDHHC3 overexpression versus palmitoylation-site mutation, with the ERAD pathway unaffected. It predicts surface expression up and current up only where the mutant already has endoglycosidase-H-resistant forms. No effect if the mutant is ER-retained.

## Z17
Statement: Mutant receptors reach the cell surface but fail to be retained at inhibitory synapses because of scaffold (gephyrin/collybistin/neuroligin-2) engagement, so the loss is of synaptic rather than total surface receptor.
Discriminating manipulation vs H6: raise gephyrin or collybistin expression (genetic) in the mutant neuron. Predicts total surface biotinylation unchanged, synaptic cluster fraction up, mIPSC amplitude up and the whole-cell GABA-puff current largely unchanged. H6 predicts total surface up and puff current up.

## Z18
Statement: A ligand binding the orthosteric or an allosteric site acts as a pharmacological chaperone, stabilising the mutant during assembly and raising surface expression independently of its effect on channel gating.
Discriminating manipulation vs H2: a competitive antagonist exposed during biosynthesis and then washed out (a class that binds but does not gate). Predicts surface expression up. GABA-evoked current is absent during exposure and recovers to above the baseline after washout in proportion to the surface rise. H2 predicts no ligand-site dependence, and a site-dead double mutant should abolish only H4's effect.

## Z19
Statement: The mutant subunit is recognised as misfolded in the ER and cleared by ER-associated degradation (ERAD) before it assembles, so lowering ERAD flux raises the ER-resident pool and, if the folded fraction can exit, the surface pool.
Discriminating manipulation vs nearest rival H2 (ER folding capacity): conditional loss of the ERAD E3 complex, genetic (SEL1L/HRD1), or an ERAD-inhibition class acting on the p97/VCP step. Predicts total and ER-retained mutant subunit up. Surface expression rises only if a folded fraction exists, and is expected to stay flat or rise modestly. GABA-evoked current is unchanged or modestly up, and it is not expected to match the rise in total protein, because the added protein is largely trapped. The rival H2 instead predicts surface and current rising together with only a modest rise in total.

## Z20
Statement: Surface expression is largely intact but the mutant channels are gating-impaired, so the "loss of surface" premise is wrong and a positive allosteric modulator class would restore current without changing surface protein.
Discriminating manipulation vs H4: acute application of a PAM class to cells already expressing the mutant. Predicts surface expression unchanged, because no biosynthesis or trafficking is involved, and GABA-evoked current up by a factor independent of surface number. H4's predictions are surface up before any acute application, with washout dependence.

## Z21
Statement: Partial, physiological-level restoration of the wild-type subunit in neurons is enough, because a graded threshold below full restoration holds. If the mutant is also a dominant-negative sink, selective silencing of the mutant allele adds gain beyond what dosage alone gives.
Discriminating manipulation (vs (a rival) global replacement, and vs a haploinsufficiency-only model): compare a Synapsin-promoter vector at graded expression against a Dlx-enhancer (interneuron) vector and a CaMKII (pyramidal) vector, plus allele-specific silencing of the mutant. Predicted: the Synapsin graded arm recovers surface and IPSC amplitude at sub-50% wild-type expression, the Dlx arm raises interneuron surface and IPSCs with pyramidal tonic current unchanged, and the CaMKII arm does the reverse. Allele silencing raises wild-type surface and current above the 50% level only if the mutant is a dominant-negative sink. Under pure haploinsufficiency it gives no gain.

## Z22
Statement: ER calcium handling (class: L-type Ca2+ channel blockers, SERCA activation) lowers ERAD flux and raises ER chaperone function, increasing surface mutant subunit through a calcium-dependent route rather than a direct folding route.
Discriminating manipulation (vs. H2): Genetic SERCA2 overexpression or an ER-Ca2+ clamp in HRD1-deficient cells. If the effect needs an intact ERAD pathway, it is upstream of ERAD. It predicts surface expression up and GABA-evoked current up in the ERAD-intact cells only; in the ERAD-deficient cells it predicts no additional gain.

## Z23
Statement: The mutant protein is limited by the availability of partner subunits and assembly factors (alpha/beta/gamma stoichiometry; LHFPL4/GARLH4-type auxiliary proteins), so raising these raises surface assembly.
Discriminating manipulation (vs. H1): Co-expression of partner subunit(s) at a fixed mutant dose, in HEK cells, then repeated in iPSC-derived neurons. It predicts surface expression up and GABA-evoked current up if the mutant is assembly-competent. If it does not rise, folding is the block.

## Z24
Statement: A binding-site ligand acting as a pharmacological chaperone raises surface during synthesis and its benefit persists after washout, whereas a pure positive allosteric modulator raises current only while present. The chaperone effect can still fail by occluding gating.
Discriminating manipulation (vs (a rival), an acutely applied modulator): pre-incubate during synthesis, then wash out fully before recording. Predicted: surface rises and a washout-persistent current component remains; the pure modulator gives neither. Record current by perforated-patch so the chloride gradient does not distort it (research/commit_candidates/CC-20260826-EGABA-EXPERIMENT-01.md:146,160).

## Z25
Statement: The mutant reaches the plasma membrane but is lost by accelerated endocytosis and lysosomal degradation, driven by altered phosphorylation or ubiquitination (PKC/PKA at the β3 intracellular loop, BDNF–TrkB signalling, AP2/clathrin). Blocking this restores surface and current.
Discriminating manipulation: Versus H1–H3, block clathrin/dynamin-dependent endocytosis (class) or a TrkB-signalling class. Predicts surface and current up if the mutant is post-ER. Surface stays flat if it is ER-retained, where H1–H3 apply.

## Z26
Statement: Increased endocytosis and lysosomal turnover (clathrin/AP2, with phosphorylation-dependent beta-subunit internalisation) remove mutant receptors that did reach the surface, so inhibiting internalisation raises their surface residency.
Discriminating manipulation (vs. H2): Phospho-null beta-subunit (S408/409A-type) or a dynamin-class endocytosis block, versus a proteasome block. It predicts surface expression up only if mutant receptors reach the surface, and GABA-evoked current up in proportion. If surface half-life is normal, no change is predicted.

## Z27
Statement: The mutant subunit assembles with wild-type partners and traps them in the ER (dominant-negative). Allele-specific silencing of the mutant releases the wild-type pool, so wild-type-containing surface receptors and current rise.
Discriminating manipulation: Allele-specific silencing of the mutant (ASO/siRNA class) versus wild-type-allele upregulation (H9). - If dominant-negative: silencing raises tagged-WT surface and current toward wild-type, while WT upregulation adds ER-trapped subunit and fails to raise current. - If haploinsufficient: silencing lowers or leaves current flat, and WT upregulation raises it.

## Z28
Statement: The defect is upstream of folding, in synthesis (translation, ribosome-associated quality control, or an integrated-stress-response brake), so the surface deficit shrinks when translation of the mutant is allowed to run.
Discriminating manipulation vs H1: an integrated-stress-response inhibitor class (acting on eIF2alpha dephosphorylation) while ERAD is left intact. Predicts total mutant protein up. Surface rises only if folding capacity is not exceeded, otherwise the added protein is cleared and the effect can reverse. GABA-evoked current follows surface and not total protein. H1 predicts no change in synthesis with ERAD block.

## Z29
Statement: The sign of an Hsp70 lever depends on which co-chaperone is raised: nucleotide-exchange or folding-promoting partners shift the mutant toward ER export, while E3/degradation-promoting partners shift it toward clearance.
Discriminating manipulation (vs H8): overexpress a folding-promoting Hsp70 partner (nucleotide-exchange factor) versus a CHIP-type ubiquitin-ligase partner. Predicted: the first raises post-ER fraction, surface and current with little change in half-life. The second lowers all three. H8 would instead leave the post-ER fraction unchanged and act only through half-life.

## Z30
Statement: The variant reaches the surface but is internalised and routed to lysosomes faster than wild-type, so reducing endocytosis (a clathrin/AP2-phospho-site or ubiquitin-ligase manipulation) raises surface density and current.
Discriminating manipulation (vs H6): acute dynamin/clathrin block class in cells expressing the variant. H7 predicts surface rises within minutes to hours and current follows if the channel is intact. H6 predicts no rise, because the receptor never reached the surface.

## Z31
Statement: The mutant reaches the surface but is cleared faster by a K63-ubiquitin and AP2/clathrin-dependent endolysosomal route, so acute endocytosis block raises surface and current within minutes.
Discriminating manipulation (vs H1 and H2, ER-level levers): acutely block dynamin or AP2 binding. Predicted: surface rises within minutes, the Endo-H-sensitive fraction is unchanged, and current rises in proportion. ER-level levers act over hours and shift the Endo-H-resistant fraction first.

## Z32
Statement: Blocking ER-associated degradation of the misfolded mutant subunit (Hrd1/Sel1L–VCP/p97–proteasome axis) increases the mutant pool available for assembly and export, so surface expression and current rise.
Discriminating manipulation: Versus H2 (more folding help), use Hrd1/Sel1L loss of function, or a p97 inhibitor class, in cells with chaperone capacity held constant. Predicts total up, surface up only modestly and only if H2-type folding is intact, and current up in proportion to surface. If the rival H2 is right, surface stays flat and current is unchanged.

## Z33
Statement: The shortfall is partner-limited assembly, so raising the supply of co-assembling subunits or assembly factors (for example the β/γ partner, or LHFPL4/Shisa/NACHO-like helpers) restores pentamer formation and surface expression.
Discriminating manipulation: Versus H1/H2, overexpress the partner subunit alone, then do a subunit-specific knockdown. Predicts mutant-containing surface and current rise with partner excess, and fall with partner knockdown. A folding lever (H2) would be partner-independent.

## Z34
Statement: The variant reaches the surface but lacks synaptic retention, because the scaffold and cell-adhesion link (gephyrin, collybistin, neuroligin-2) fails to cluster it, so the receptor diffuses away and is removed. Stabilising the scaffold restores synaptic density and mIPSC amplitude.
Discriminating manipulation (vs H7): knock down gephyrin or use a collybistin dominant negative. H8 predicts total surface unchanged or only mildly reduced, with synaptic cluster and mIPSC amplitude falling. H7 predicts total surface falls and a dynamin block restores it.

## Z35
Statement: The variant subunit leaves the ER but is slowed in COPII-dependent export or Golgi passage, so increasing export machinery (COPII-cargo adaptor or Golgi-processing lever) raises surface expression and current.
Discriminating manipulation (vs H1): block COPII export genetically (a Sec24-family or Sar1-GTPase dominant negative) and compare with folding enhancement. H6 predicts that export block removes the gain from any treatment and that raising export raises surface and current without changing the endoglycosidase-H pattern. H1 predicts the gain appears at the ER form first.

## Z36
Statement: The variant is dominant-negative: it co-assembles with the wild-type product and traps it intracellularly. Selective silencing of the variant allele (ASO or siRNA class, allele-specific) raises surface and current.
Discriminating manipulation (vs H4): selective knockdown of the variant allele. Predicted: under dominant-negative action, surface and current rise. Under haploinsufficiency, both fall to roughly half, which is the opposite of H4's wild-type-copy prediction.

## Z37
Statement: Reduced palmitoylation by Golgi palmitoyl-transferases (ZDHHC3/7, GODZ) limits Golgi export of the mutant. Restoring palmitoylation raises surface subunit and current.
Discriminating manipulation: ZDHHC3/7 gain (genetic) versus depalmitoylase (APT/ABHD17-class) inhibition. These give the same sign but different stages. - ZDHHC gain: EndoH-resistant fraction ↑, surface ↑, current ↑. - Depalmitoylase block: surface ↑ only through longer residence, the EndoH-resistant fraction is unchanged, and wild-type receptors also rise. - Using the Cys→Ser double mutant shows whether the effect needs the modification site.

## Z38
Statement: Transcriptional up-regulation of the wild-type allele (HDAC inhibition or targeted gene activation on that allele) compensates for the mutant allele's loss and restores total surface receptor.
Discriminating manipulation (vs. H10): Allele-specific activation of the wild-type allele (CRISPRa) in heterozygous iPSC neurons. It predicts surface expression up and GABA-evoked current up with the wild-type-assembled receptors. If the mutant exerts dominant-negative effects (H10), the gain is smaller than the dosage predicts.

## Z39
Statement: Remodelling the cytosolic and ER chaperone network (more Hsp70/BiP-type folding, less Hsp90/Hsp40-driven degradation triage) shifts mutant subunits from degradation to productive folding and assembly, raising surface and current.
Discriminating manipulation: Versus H1, use Hsp90 inhibition (class), which promotes client degradation, against Hsp70 co-chaperone activation. Predicts that Hsp70 activation raises surface and current, while Hsp90 inhibition lowers both. If H1 is right, Hsp90 inhibition has no net effect once ERAD is blocked.

## Z40
Statement: Missense variants that reduce S-palmitoylation of the subunit (for γ2 via ZDHHC3/7-class acyltransferases) lower Golgi exit and synaptic stability, so raising palmitoylation raises surface, and mainly synaptic current.
Discriminating manipulation (vs nearest rival H5, post-delivery endocytosis): overexpress the acyltransferase against a palmitoylation-site mutant of the subunit. Predicted: surface and synaptic IPSC amplitude rise, the effect is lost with the site mutant, and extrasynaptic whole-cell current changes less. The rival (H5) would raise the whole-cell current and extrasynaptic pool equally.

## Z41
Statement: The mutant reaches the surface normally, but is removed faster by regulated endocytosis and lysosomal degradation, so slowing internalisation restores the surface pool.
Discriminating manipulation vs H1: block regulated endocytosis of the beta-subunit AP2 site (genetic, for example a phospho-site mutation that prevents AP2 binding, general knowledge, not held). Predicts surface expression up with total protein up only by the surface fraction, because ER-resident protein is not affected. GABA-evoked current rises if the surface mutant is gating-competent. H1 predicts that only ERAD manipulation, not endocytosis, works.

## Z42
Statement: Surface loss is an assembly-stoichiometry problem. The variant subunit is limited by its partner subunits (for example α/β/γ supply), so raising partner-subunit supply restores surface pentamers and current.
Discriminating manipulation (vs H1): partner-subunit overexpression (genetic) in cells with a cell-type-specific subunit make-up, such as interneuron vs pyramidal neuron. H3 predicts a surface and current gain scaled to the partner, without any chaperone. H1 predicts the gain depends on the folding enhancer and not on the partner.

## Z43
Statement: The mutation affects synaptic anchoring and lateral diffusion (gephyrin, neuroligin-2, calcineurin-dependent gamma2 S327 dephosphorylation) rather than total surface protein, so the functional deficit is at synapses while whole-cell surface expression is near normal.
Discriminating manipulation (vs. H7): Gephyrin knockdown (or a calcineurin-inhibitor class) in neurons. It predicts total surface expression unchanged, synaptic clusters and mIPSC amplitude changed, and whole-cell GABA-evoked current from exogenous agonist unchanged (or tonic current changed).

## Z44
Statement: A missense subunit is folding-competent but kinetically trapped, so raising ER folding capacity (a chemical-chaperone or ER-lumen-folding class) increases ER exit, surface density and current.
Discriminating manipulation (vs H2, ERAD relief): knock down the ER-lumen chaperone BiP, or the calnexin/calreticulin cycle, and compare with a folding enhancer. H1 predicts surface subunit and evoked current fall with BiP knockdown and rise with the enhancer. The rival H2 predicts no dependence on BiP.

## Z45
Statement: A 4-phenylbutyrate-class compound lifts mutant surface by two separable actions, a chaperone-like effect and an HDAC-dependent chaperone-gene program, and only the transcriptional part persists when transcription is blocked.
Discriminating manipulation (vs H1): compare the HDAC-inhibitor class with a pure osmolyte chemical chaperone, both with transcription blocked. Predicted: the HDAC class loses its surface and current gain, and the osmolyte keeps it. An ATF6 arm (H1) would instead be BiP-dependent.

## Z46
Statement: Reduced palmitoylation (ZDHHC3/GODZ) impairs Golgi-to-surface delivery and synaptic retention (with gephyrin/neuroligin-2 clustering), and boosting palmitoylation raises synaptic surface expression and current.
Discriminating manipulation: Versus H8, ZDHHC3 overexpression against inhibition of the depalmitoylase class (ABHD17-type). Predicts synaptic surface and synaptic current up with more palmitoylation, and a loss with ZDHHC3 knockdown. H8 predicts no palmitoylation dependence.

## Z47
Statement: Selective activation of the ATF6 arm of the unfolded-protein response raises ER folding and export capacity, so EndoH-resistant mutant subunit, surface subunit and GABA-evoked current all increase. It works only if the mutant has a partly foldable intermediate.
Discriminating manipulation: ATF6-arm activation (genetic active fragment, or an ATF6-selective small-molecule class) versus IRE1/XBP1s-arm activation. - ATF6 prediction: total mutant subunit ↑, EndoH-resistant ↑, surface ↑, GABA-evoked current ↑ at fixed driving force. - IRE1/XBP1s prediction: it also induces ERAD, so total is flat or ↓, surface is flat, and current is flat.

## Z48
Statement: Raising ER folding capacity (BiP/Hsp70 chaperone cycle, driven by the ATF6 arm of the UPR) increases the folded, assembly-competent fraction of the mutant subunit, so more of it reaches the surface and the current rises.
Discriminating manipulation (vs. H2, ERAD block): Genetic ATF6 activation or BiP overexpression, with the degradation machinery left intact. It predicts surface expression up and an increase in GABA-evoked current in proportion to the surface rise. If the ERAD block (H2) alone gave the same result, folding would not be the limiting step.

## Z49
Statement: A membrane-permeant ligand that binds the assembled interface (a positive allosteric modulator class, or a pharmacological chaperone) stabilises the folded or assembling subunit in the ER, raising surface expression and also potentiating channel gating.
Discriminating manipulation (vs. H1): Binding-site-dead mutation in cis, plus permeant versus impermeant ligand of the same class. It predicts surface expression up with the permeant ligand only (not with the impermeant one), and current up more than surface expression (surface rise plus potentiation). A current gain with no surface gain means gating modulation, not chaperoning.

## Z50
Statement: Part of the surface loss is non-cell-autonomous, driven by glia-derived inflammatory or neurotrophic signalling that downregulates GABA-A surface expression, so the loss is partly a response to a state and not a property of the mutant.
Discriminating manipulation vs H1: depletion of microglia or blockade of the IL-6/JAK-STAT axis (a signalling-class manipulation) in a co-culture or slice, with the mutant genotype fixed. Predicts surface expression up in the mixed preparation only (not in the isolated neuron) and GABA-evoked current up modestly and in step with it. H1 predicts a deficit that persists in isolation and responds only to ERAD or folding manipulation.

## Z51
Statement: The subunit folds, but assembly with its partner subunits fails, so surface loss is a stoichiometry problem that extra partner subunit corrects.
Discriminating manipulation vs H1: a genetic increase in the partner subunit in the same neuron or cell, with no change to quality-control machinery. Predicts surface expression up and, if the mutant incorporates into a gating-competent pentamer, GABA-evoked current up. Total mutant protein is unchanged because it was never degraded. H1 predicts the opposite, with partner overexpression doing nothing and ERAD block raising total protein.

## Z52
Statement: The missense lowers co-translational folding yield or synthesis, so little receptor is made. No degradation blocker recovers it. Only a biogenesis-stage manipulation raises surface subunit and current.
Discriminating manipulation: A short pulse followed by immunoprecipitation, with and without combined proteasome and lysosome blockade. - If synthesis- or yield-limited: time-zero signal is low, the blocks do not raise total, and surface and current stay flat. - Slowing translation elongation (low temperature, as a diagnostic) then raises folding yield: surface ↑ and current ↑. - If degradation-limited: time zero is normal and the blocks raise total.

## Z53
Statement: A dosage shortfall of total (WT plus mutant) subunit can be offset by raising transcription of the gene, which pushes more folded receptors to the surface, unless the mutant is dominant-negative.
Discriminating manipulation: Versus H6, CRISPRa of the gene against allele-selective silencing of the mutant allele. Predicts CRISPRa raises surface and current only if loss of function is haploinsufficient. Under dominant-negative action, mutant silencing raises current and CRISPRa lowers or does not change it.

## Z54
Statement: The ER's folding and assembly capacity is the limit, so raising it lets more mutant subunit fold and reach the surface.
Discriminating manipulation vs H1: induce the ATF6 arm of the unfolded-protein response (a class acting on BiP/foldases) while leaving ERAD intact. Predicts total mutant protein modestly up, surface fraction up, and GABA-evoked current up in proportion to surface, provided the folded subunits assemble. Under H1 the same manipulation changes little and ERAD block is required.

## Z55
Statement: A ligand that binds the orthosteric or an allosteric site stabilises the folded pentamer (a pharmacological chaperone), raising assembly and surface expression, while function depends on whether the ligand leaves the receptor.
Discriminating manipulation: Versus H2 and H3 (non-specific), compare an agonist-site ligand class with a non-binding positive modulator class. Predicts that the agonist-site class raises surface but evoked current is blocked or desensitised until washout. The modulator class raises current without raising surface. A general chaperone raises surface and current together.

## Z56
Statement: Selective activation of the ATF6 arm of the unfolded protein response raises ER folding and export capacity, rescuing mutant surface expression without general proteostasis stress.
Discriminating manipulation: Versus H2, activate ATF6 with BiP or ATF6 targets knocked down, or use an ATF6-selective class against an IRE1/PERK class. Predicts surface and current up with ATF6-selective activation, and no gain or a loss with PERK/IRE1 activation. H2 alone would not depend on ATF6 transcription.

## Z57
Statement: Reducing Ca2+ entry through L-type Ca2+ channels, or reshaping ER Ca2+ handling, modulates ER-chaperone activity and ER exit and raises mutant surface expression.
Discriminating manipulation: Versus H3, block L-type channels (class) with ATF6 held fixed. A genetic L-type channel knockdown and an ER Ca2+ store depletion class discriminate. Predicts surface and current up with L-type block, and a smaller effect or none when ER Ca2+ is depleted. H3 predicts the same surface rise with no Ca2+ dependence.

## Z58
Statement: Degradation of the mutant subunit by the SEL1L-HRD1 ERAD pathway (with p97 extraction and the proteasome) is the dominant loss route, so reducing it gives more mutant protein a chance to assemble and exit the ER.
Discriminating manipulation (vs. H1): HRD1 or SEL1L knockout, or a dominant-negative p97, with the folding machinery unchanged. It predicts total protein up and surface expression up only modestly. It predicts GABA-evoked current up less than surface expression if the rescued protein is gating-defective. A current lower than the surface rise predicts is the signature that separates trafficking from function.

## Z59
Statement: The mutant subunit acts as a dominant-negative in the ER by co-assembling with wild-type subunits and dragging them into degradation, so silencing only the mutant allele frees wild-type protein and raises surface expression above the level expected from haploinsufficiency alone.
Discriminating manipulation (vs. H9): Allele-specific silencing (siRNA or ASO) of the mutant transcript in heterozygous neurons. It predicts surface expression up above 50% of normal and GABA-evoked current up, more than haploinsufficiency would predict. If it rises only by dosage, H9 fits better.

## Z60
Statement: The mutant's defect is mainly in synaptic anchoring (gephyrin, neuroligin-2, LHFPL4, Shisa7), so whole-cell surface subunit is near normal while the synaptic pool is lost. Rescue should therefore depend on cell type (interneuron-targeted versus pyramidal).
Discriminating manipulation: Gephyrin/NLGN2 gain restricted to interneuron-targeted versus pyramidal-targeted neurons, against ER-export enhancement (H1). - Scaffold gain: whole-cell surface unchanged, synaptic puncta ↑, mIPSC amplitude ↑ (cell-type dependent), and the extrasynaptic isoguvacine-evoked current unchanged. - H1: whole-cell surface ↑ and extrasynaptic current ↑.
