#!/usr/bin/env python3
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print("IT22 P6 EZH2/glia dossier builder (build_table_ezh2_glia_p6_it22.py); run with no argument from this folder; writes only files next to it.")
    raise SystemExit(0)
"""Writes qualification_ezh2_glia_it22_p6.tsv (one row per compound). Run: python3 build_table_ezh2_glia_p6_it22.py"""
import pathlib
D=pathlib.Path(__file__).resolve().parent
cols=["compound","identity_form","action_and_typed_measures","cns_exposure_evidence","wwox_relevant_evidence","inference_chain","decisive_assumption","counter_evidence_opposite_effects","minimum_discriminating_experiment","result_that_closes_it","missing_data","feasibility","novelty_for_legend","evidence_strength","wwox_relevance","feasibility_grade","reading_depth"]
G="as GSK343"
R=[]
R.append(dict(
compound="GSK343 (GSK-343)",
identity_form="CHEMBL2204995; tool compound, free base; research use only (no human data)",
action_and_typed_measures="EZH2/PRC2 IC50 4 nM (catalogue, assay class unknown); EZH1 IC50 240 nM (same type, 60-fold; the catalogue prints '0.0x' for the inverted ratio); cell H3K27 methylation IC50 174 nM (IT21 P4a, human HCC1806 72 h); fetal NSC viability IC50 9 uM 48 h (one row)",
cns_exposure_evidence="none measured. Efflux substrate of P-gp and BCRP in vitro (PMID 25868794, abstract level). In vivo mouse brain effects (PMID 37391829, read) are pharmacodynamic; the paper states 'little is known about its ability to cross the BBB' (L5). Absence of data, not evidence of absence",
wwox_relevant_evidence="none in a Wwox system. No EZH2, H3K27me3 or GSK343 measurement in Wwox-deficient glia found in the records reviewed (not an exhaustive search). Local human neural data: EZH2 11-19 cpm in the KO/WT organoid (KO/WT 0.93), EZH1 higher (60-71 v 42-46 cpm, 1.49x); no IL6/TNF reads there. Seed side: Il6 up in null hippocampus (significant, about 1.48-fold, n 4 v 4); Tnf there NOT significant; Tnf/Il1b >=2-fold in P47T cerebellum (transcript, n 6, distributions overlap WT)",
inference_chain="Wwox loss -> glial Il6 (and Tnf/Il1b) transcript up -> inflammatory tone could be EZH2-dependent -> EZH2 inhibition lowers Il6/Tnf. Every arrow after the first is borrowed from other contexts",
decisive_assumption="that the sign of EZH2 -> IL6/TNF seen in an injury model (MPTP) holds in Wwox-deficient glia, in the cell type that makes the cytokine, at a concentration that engages EZH2 and not EZH1",
counter_evidence_opposite_effects="PMID 29132376 (read) used DZNep and siEZH2, NOT GSK343 (L1); IL1B/IL6 rose in the glioblastoma cells (L2), whereas in microglia IL1B/IL6 did not change and TNF/iNOS rose only through tumour-cell conditioning (L3); TNF was undetectable in the tumour cells (L4): an indirect, non-microglial contrast, weaker than the IT21 wording. Supportive: GSK343 lowered brain IL-1b/IL-2/IL-6/IL-17A in MPTP mice (L7), whole-tissue ELISA (L6), uninjured-animal cytokines not shown (L8); DZNep lowers microglial IL-6/TNF after stroke (PMID 31202798, abstract). Ezh2 can license inflammasomes independently of methyltransferase activity (PMID 35568718, abstract), so a catalytic inhibitor need not mimic loss. OPC side: EZH2/PRC2 inhibition expected to delay OL differentiation and de-repress Wnt/Notch (L9-L11); the authors' own reading (L12) is the opposite of inhibition for myelin",
minimum_discriminating_experiment="Wwox-null and WT primary microglia and astrocytes separately (plus neuron-conditioned medium); arms: vehicle, GSK343 0.17 and 1 uM (174 nM = cell H3K27 IC50; 1 uM brackets EZH1 240 nM), a second chemotype, Ezh2 siRNA/CRISPR, an EED inhibitor as PRC2 control; readouts H3K27me3 (immunoblot, ChIP-qPCR at Il6/Tnf) at day 4-7, Il6/Tnf mRNA AND secreted protein; a parallel OPC differentiation arm (Mbp, Myrf, Hes5, Axin2) with the same compounds",
result_that_closes_it="Il6/Tnf fall with H3K27me3 down, reproduced by Ezh2 knockdown and the second chemotype, only (or more) in Wwox-null glia = survives as a conditional glial finding. Cytokines rise or do not move with H3K27me3 down = H_HARM closes for this axis. Falls with the compound but not with knockdown = off-target or non-catalytic, closes",
missing_data="EZH2/H3K27me3 level in Wwox glia; cell-type origin of the Il6/Tnf rise in vivo; GSK343 H3K27me3 effect in primary glia; brain exposure; protein-level cytokines",
feasibility="in vitro high (purchasable tool compound); in vivo low (no exposure data, efflux substrate)",
novelty_for_legend="molecule: not new (excluded F5/E6 in IT9; KEPT_CONDITIONAL in IT21). relation: not new (IT9 thread). context: narrowed (counter-evidence now localised to a different cell type and inhibitor). combination: none",
evidence_strength="hypothesis only; mouse injury-model support (full text read) against indirect co-culture data; no Wwox datum",
wwox_relevance="low (links borrowed, not measured in Wwox)",
feasibility_grade="in vitro high; in vivo low",
reading_depth="partial full text (37391829, 29132376); abstract (25868794)"))
R.append(dict(
compound="GSK126 (= GSK2816126, same substance; counted once)",
identity_form="CHEMBL3287735; clinical-stage (phase 1 oncology) per name, not verified; free base",
action_and_typed_measures="EZH2 IC50 9.9 nM (biochemical); no EZH1 row in the catalogue, so no same-type selectivity ratio from this source (not comparable). Not ranked against GSK343 on potency: separate depositions, undeclared assay conditions",
cns_exposure_evidence="limited: Abcb1 and Abcg2 restrict brain accumulation; oral bioavailability 0.2% in wild-type mice, 14.4% in Abcb1;Abcg2 knockout; authors question clinical usefulness (PMID 25868794, abstract level). A claim that it permeates intracranial tumour is cited second-hand in PMID 37391829 and was not checked at source",
wwox_relevant_evidence="none in Wwox",
inference_chain=G+" (same target)",
decisive_assumption=G,
counter_evidence_opposite_effects=G+"; plus low oral exposure",
minimum_discriminating_experiment="interchangeable with GSK343 as the second-chemotype control in the in vitro arm",
result_that_closes_it=G,
missing_data="no EZH1 value in the catalogue; no brain/plasma value read",
feasibility="in vitro high; in vivo low (efflux, 0.2% oral bioavailability in wild-type mice)",
novelty_for_legend="molecule: same substance as the GSK2816126 alias; not new in the class; relation not new",
evidence_strength=G+", no extra",
wwox_relevance=G,
feasibility_grade="in vitro high; in vivo low",
reading_depth="abstract (25868794)"))
R.append(dict(
compound="tazemetostat (= EPZ-6438, same substance; counted once)",
identity_form="approved per the release flag (epithelioid sarcoma, follicular lymphoma; label not re-read here); no ChEMBL id in the catalogue row",
action_and_typed_measures="EZH2 IC50 11 nM (assay class unknown); no EZH1 row, no same-type ratio. Not 'more potent' or 'less potent' than GSK343 (4 nM) or GSK126 (9.9 nM): same type, different undeclared assays",
cns_exposure_evidence="partial: efflux limited by P-gp only, abrogated by elacridar in mice (PMID 25868794, abstract); given to children with CNS tumours (8 of 20 had atypical teratoid rhabdoid tumour; PMID 37228094, abstract), no CNS exposure in the abstract; PMID 35300079 authors call the class poorly brain penetrant (abstract). No CSF or brain concentration read",
wwox_relevant_evidence="none in Wwox. A neuropathic-pain paper reports EPZ6438 changes spinal Timp1 and microglial NLRP3 in mice (PMID 40209863, abstract), i.e. a CNS pharmacodynamic effect of an approved agent",
inference_chain=G+", with a human exposure statement available",
decisive_assumption=G+"; plus that a systemic dose reaches glia",
counter_evidence_opposite_effects=G+"; class on-target liabilities in people (second malignancies per label, from memory) NOT verified here",
minimum_discriminating_experiment=G+" (in vitro arm); no in vivo step proposed",
result_that_closes_it=G,
missing_data="brain/CSF concentration; H3K27me3 in CNS tissue of treated people; paediatric tolerability (full text of 37228094 not read)",
feasibility="in vitro high (commercial); any human use is an oncology prescription and needs a treating team, not a LEGEND proposal",
novelty_for_legend="molecule: approved, in the catalogue; relation to Wwox glia: new as a question only; class not new",
evidence_strength="hypothesis only; human safety data exist in oncology but are not WWOX evidence",
wwox_relevance="low",
feasibility_grade="in vitro high; clinical: not assessable here",
reading_depth="abstract (37228094, 25868794, 40209863)"))
R.append(dict(
compound="mevrometostat (PF-06821497)",
identity_form="CHEMBL4080228; clinical-stage per name, status not verified",
action_and_typed_measures="EZH2 Ki < 0.1 nM (relation '<', biochemical). Ki is a different type from the IC50 rows: NOT compared, NOT converted",
cns_exposure_evidence="none found",
wwox_relevant_evidence="none",
inference_chain=G,decisive_assumption=G,
counter_evidence_opposite_effects="not searched beyond the catalogue",
minimum_discriminating_experiment=G,result_that_closes_it=G,
missing_data="EZH1 value, CNS exposure, any glial data",
feasibility="in vitro: reagent availability unverified",
novelty_for_legend="molecule: not among the IT9 excluded EZH2 compounds in the files grepped (new to this thread)",
evidence_strength="none for this question",wwox_relevance="none",feasibility_grade="unknown",reading_depth="catalogue row only"))
R.append(dict(
compound="valemetostat, tulmimetostat, zeprumetostat (dual EZH1/EZH2 members; named because the OPC biology makes them the highest-risk members)",
identity_form="valemetostat CHEMBL4597193 and zeprumetostat flagged approved in the release (not verified against labels); tulmimetostat CHEMBL5095231 clinical-stage",
action_and_typed_measures="EZH1 v EZH2 IC50, same type: valemetostat 16 v 5.1 nM (3.1x); zeprumetostat 19.1 v 4 nM (4.8x); tulmimetostat 0.06 v 0.02 nM (3.0x); GSK343 240 v 4 nM (60x). The dual members hit EZH1 within 3-5-fold of EZH2",
cns_exposure_evidence="none read",wwox_relevant_evidence="none",
inference_chain="a dual inhibitor removes the EZH1 compensation that rescued OL differentiation in the Ezh2-only knockout (L9, L10)",
decisive_assumption="n/a: proposed only as a hazard",
counter_evidence_opposite_effects="Wang 2020 (read): Ezh1+Ezh2 (Eed) loss gives no recovery and lethal dysmyelination (L10, L13); EZH2 loss alone is compensated by EZH1 by P10. A genetic result in developing spinal cord, not a drug result",
minimum_discriminating_experiment="only in the OPC-differentiation arm, as a negative control for the OL axis",
result_that_closes_it="n/a",missing_data="OPC exposure; transfer to brain and postnatal age",
feasibility="n/a",novelty_for_legend="not recommended for the glial question; class-level hazard",
evidence_strength="n/a",wwox_relevance="n/a",feasibility_grade="n/a",reading_depth="partial full text (32937136)"))
R.append(dict(
compound="UNC1999, EPZ011989, EPZ005687, EI1, CPI-1205, JQEZ5, EBI-2511, SKLB-03220 (other class members)",
identity_form="catalogue rows only; several had no human-exposure statement in IT9 and were excluded there",
action_and_typed_measures="EZH2 IC50 (nM): SKLB-03220 1.72; UNC1999 2.0; CPI-1205 2.0; EBI-2511 8.0 (cell); EI1 9.4; JQEZ5 11. Ki (nM): EPZ011989 <3.0; EPZ005687 24. Types not pooled",
cns_exposure_evidence="UNC1999 and EPZ005687 are efflux-limited or transported (abstract, 25868794); UNC1999 shows an in vivo glioblastoma effect with dexamethasone (PMID 27449082, abstract). TDI-6118 is reported brain penetrant (abstract, PMID 35300079) but is not in the catalogue and no values were read",
wwox_relevant_evidence="none",inference_chain=G,decisive_assumption=G,counter_evidence_opposite_effects=G,
minimum_discriminating_experiment=G,result_that_closes_it=G,
missing_data="TDI-6118 brain/plasma and EZH2 potency; no catalogue row for it",
feasibility="low priority",novelty_for_legend="not new",evidence_strength="none",wwox_relevance="none",feasibility_grade="low",reading_depth="abstract"))
rows=["\t".join(cols)]+["\t".join(r[c].replace("\t"," ") for c in cols) for r in R]
(D/"qualification_ezh2_glia_it22_p6.tsv").write_text("\n".join(rows)+"\n")
