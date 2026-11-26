"""IT 2026-11-26 (IT28): wording from SCI's ADV-287 extension (RESULT_ADV287EXT_SCI_20261126.md sections 2, 3 and 4) as FRAGMENT replacements inside the card packets.
Entries: (card, where, old_fragment, new_fragment). 'where' is an assertion id plus field ('DR-H02-005:note') or a dotted path into the packet ('P:p4_fields.cellular_context.target_expression',
'P:p4_card.evidence_for_and_against.for[2]'). The old fragment must occur exactly once in the field. Hypothesis level; reference genotype class; nothing here is medical advice.
No dose, route or schedule token may appear (check_cards.py)."""
X = []
def f(card, where, old, new, tag): X.append(dict(card=card, where=where, old=old, new=new, tag=tag))

# ---- section 2: verified MUST CHANGE
f("H02_gabaat_inactivator_myelin_exposure", "DR-H02-005:note",
  "the cited study itself was not read, so the 22 and 4 percent figures are the label's statement of it.",
  "the label gives the 22 and 4 percent figures without naming a publication (the cited 2026-06-15 version is not held; held sibling labels were searched on 2026-11-26), and the study they match (PMID 19054414, an identification inferred from the numbers) was read at abstract level only (22 against 4 percent, vigabatrin-naive comparator), not in full text.",
  "H02-26")
f("A01_pba_class", "P:p4_card.evidence_for_and_against.for[2]",
  "In the soluble cytosolic client, the class and two HDAC-free osmolytes raised the mutant while a class-I HDAC inhibitor did not, and the soluble fraction roughly doubled with a vesicle-recycling read-out at or above the untreated wild-type range for three of the four low-protein variants",
  "In the soluble cytosolic client (Guiberson 2018), phenylbutyrate raised the G544D mutant total protein about 1.8 fold (Supplementary Figure 12a) and about 1.5 fold (12b) and trehalose about 2.35 fold in both; sorbitol raised it in 12a (about 1.8 fold, marked) but carries no significance mark in 12b (about 1.0) or in neurons (Figure 6a, about 1.6); sodium butyrate, tested only on G544D and wild type in HEK293T (three experiments), did not raise G544D (about 1.0; wild type about 1.9, unmarked); with phenylbutyrate the soluble fraction rose about 1.7 to 2.4 fold in the four low-protein variants and the vesicle-recycling read-out was at or above the untreated wild-type range for three of the four",
  "A01-04")
f("A03_client_binding_chaperone", "P:abstention_card.adjacent_context_not_wwox_evidence[1]",
  "'amenable' call differs for 12.9 percent of variants between two near-identical assays and no clinical correlation is established (Fabry GLA)",
  "'amenable' call differs for 12.9 percent (23 of 178) of GLA variants between a validated good-laboratory-practice assay and a similar in-house HEK assay that differs in cell line, incubation time, chaperone concentration and criteria, and there is no established correlation between the in-vitro activity increase and clinical benefit (the paper cites a few clinical cases, some concordant and some not) (Fabry GLA)",
  "R-34")
f("D01_a51" , "P:p4_fields.cellular_context.target_expression",
  "transcript only, raw p, 2 WT versus 4 KO organoids; the activation step (reporter, nuclear beta-catenin) is unmeasured.",
  "RNA-seq, raw p in the card's source table (the deposited differential lists also carry adjusted p, below 0.05 for several Wnt genes), 2 WT versus 4 KO organoids, with the nuclear-to-cytosolic beta-catenin band ratio about 1.7 fold of wild type by immunoblot after fractionation (Fig 4E, week 16, 2 WT and 4 KO organoids from two runs, no test shown); no reporter assay.",
  "R-37")
# ---- section 3: held apart (offered by SCI; applied after the blind round)
f("E04_ketogenic_lactate_axis", "P:not_known[2]",
  "A ketogenic-diet response is reported in 3 of 5 WOREE individuals (lactate 2.4 to 3.3 mmol/L in one individual; registry statement, no held source passage, ADV-259)",
  "In a held report of five paediatric WOREE patients (Chong 2023, PMID 36537114) epilepsy responded to a ketogenic diet in three (patients 1, 2 and 4); the lactate range of 2.4 to 3.3 mmol/L in one individual is a registry statement (ADV-259) not found in the held text (8 delivered chunks only; the case narratives of patients 1 to 4 are not held; searched 2026-11-26 for lactate, lactic and mmol); other held WOREE reports are less favourable",
  "R-35")
f("A01_pba_class", "DR-A01-008:measured_result_note",
  "the osmolyte arm rests on trehalose",
  "the osmolyte arm for G544D rests on trehalose (sorbitol is marked for G544D in 12a and in yeast and for R406H and G544V in 12b, but not for G544D in 12b or in neurons)",
  "A01-03")
f("A02_proteasome_inhibitor_class", "P:p4_card.evidence_for_and_against.against[0]",
  "(CBS wild-type half-life up about 7.7-fold under proteasome inhibition): a boost multiplies residual function and does not repair it.",
  "(CBS wild-type half-life up about 7.7-fold under proteasome inhibition; wild-type probe signal rose only as a trend, about 174 percent of its vehicle, against about 259 and 574 percent of their own vehicle in T191M and I278T; a live-cell probe signal, not enzyme activity): a boost multiplies residual function, and whether it repairs it is not shown here.",
  "R-24")
# ---- section 4: ADD
f("H02_gabaat_inactivator_myelin_exposure", "DR-H02-005:note",
  "4 percent of naive infants in the controlled study)",
  "4 percent of vigabatrin-naive infants in a retrospective ten-site comparison)", "H02-05")
f("H02_gabaat_inactivator_myelin_exposure", "DR-H02-032:note",
  "had the finding and all 12 unexposed children were normal;",
  "had the finding and all 12 unexposed children were normal; 14 further children were imaged before, during and after exposure and 4 of them were abnormal (29 of 95 exposed, 30.5 percent, derived);", "H02-03")
f("H02_gabaat_inactivator_myelin_exposure", "DR-H02-012:note",
  "by aetiology 8 of 80 with tuberous sclerosis against 30 of 92 with other causes.",
  "by aetiology 8 of 80 with tuberous sclerosis against 30 of 92 with other causes; within tuberous sclerosis 3 of 60 with rapamycin against 5 of 20 without, and no child with other causes received it.", "H02-17")
f("H02_gabaat_inactivator_myelin_exposure", "P:p4_fields.cellular_context.cells_tissue_stage",
  "at P17.", "at P17 (per electron-microscopy field, 3 mice per genotype; the paper's text says 3.5 to 4 fold).", "H02-29")
f("A01_pba_class", "DR-A01-006:measured_result_note",
  "Total mutant protein about 1.8 fold of its own untreated control (three experiments, significance mark printed); wild type rose about 1.8 fold as well,",
  "Total G544D mutant protein about 1.8 fold of its own untreated control in Supplementary Figure 12a, about 1.55 fold in 12b (HEK293T, three experiments each) and about 1.64 fold in neurons (Figure 6a, five experiments), significance mark printed in each; wild type rose about 1.8 to 2.05 fold in HEK293T and about 1.3 fold in neurons as well,", "A01-08, A01-16")
f("A01_pba_class", "DR-A01-009:measured_result_note",
  "(R406H about 44 against about 55 does not; the fifth variant, P335L, has about 65 percent protein and little baseline deficit)",
  "(R406H about 44 against about 55 does not with the class, and reaches about 58 with sorbitol; the fifth variant, P335L, has about 65 percent protein, an intermediate and not absent deficit, and its soluble fraction shows no marked change)", "A01-11, A01-14, A01-15")
f("A01_pba_class", "DR-A01-010:measured_result_note",
  "plasma phenylalanine fell about 44 percent from sham",
  "plasma phenylalanine fell about 43 to 44 percent from sham at week 12 (44.1 from the printed group means, 749.41 against 1341.01; 42.9 from the mean of the three tabulated treated values, 765.9, against the two tabulated sham values)", "A01-13")
f("L01_nrf2_axis", "P:p4_card.evidence_for_and_against.against[1]",
  "(NFE2L2 0.75x, NQO1 0.73x)",
  "(NFE2L2 0.75x, NQO1 0.73x, but HMOX1 1.67x, SRXN1 1.33x and GSR 1.20x higher on mean counts per million, 4 knockout against 2 wild-type libraries; NFE2L2 is the factor itself, not a target; none of NQO1, HMOX1, SRXN1 and GSR appears in the deposited differential lists, the HMOX1, SRXN1 and GSR knockout libraries overlap the two wild-type libraries, and NFE2L2 itself is lower, adjusted p 0.014)", "R-29")
f("L01_nrf2_axis", "DA-L01-002:measured_result_note",
  "IL1b is about 1.9x and TNF about 3.3x", "IL1b is about 2.0x and TNF about 3.3x", "R-04")
f("A02_proteasome_inhibitor_class", "DR-A02-008:measured_result_note",
  "(wild type trend only)", "(wild type trend only, about 174 percent against about 259 and 574 percent of their own vehicle in T191M and I278T)", "R-06")
f("M01_neurogenic_output_myc_window", "DA-M01-003:measured_result_note",
  "about +0.05 against about +0.9 in the knockout (a text/figure mismatch, flagged, not resolved), wild-type-like in SCAR12;",
  "about +0.07 against about +1.0 in the knockout (a text/figure mismatch, flagged, not resolved), and about -0.27 in SCAR12 (the text calls SCAR12 similar to wild type; the panel is one pooled run with no replicate or test);", "R-07")
f("D01_a51", "DR-D01-002:measured_result_note",
  "so SATB2 recovery is neither shown nor excluded;",
  "so SATB2 recovery is neither shown nor excluded (the plotted dots are not organoids: the legend gives n = 4, 4, 6 and 7 against about 6, 6, 16 and 11 dots, and knockout against knockout plus A51 is not significant);", "R-08")
f("P11_magnesium_nmdar_gate", "DR-P11-004:measured_result_note",
  "EEG improvement p 0.04 in the Results and p 0.003 in the Discussion (internal inconsistency).",
  "EEG improvement p 0.04 in the Results and p 0.003 in the Discussion (internal inconsistency; the 0.003 does not reproduce from Table 2 and is the value the paper gives for initial serum magnesium against response in Table 3; the EEG rows rest on 13 plus 13 children).", "R-11")
f("J01_glial_reactivity_modulation", "P:disease_assertions[DA-J01-007].context.genotype",
  "WWOX knockout versus wild type (4 versus 2 libraries, one laboratory)",
  "WWOX knockout versus wild type (4 versus 2 libraries, one laboratory; two of four wild-type libraries were removed, one for failed quality control and one as a post hoc outlier that clustered with neither group)", "R-19")
f("F01_glutamate_receptor_node", "DR-W2-003:locator",
  "Fisher test reported 14 of 19 versus 3 of 15",
  "Fisher test reported 14 of 19 versus 3 of 15; scoring #28 and #29 as improved gives 14 of 19 against 5 of 15, p 0.036 (a sensitivity re-scoring, not the authors' analysis: their conclusion for both is no effect; #28 is a synonymous variant and #29 a missense variant of uncertain significance, neither tested functionally)", "R-05")
f("H02_gabaat_inactivator_myelin_exposure", "DR-H02-012:note",
  "143 exposed children without an eligible examination were excluded;",
  "143 exposed children without an eligible examination, and a further 218 imaged children (exposure under 30 days 18, over 1 year 193, no pre-rapamycin MRI 7), were excluded;", "H02-17b")

f("A01_pba_class", "DR-A01-010:measured_result_note",
  "a higher exposure level caused kidney enlargement, ascites and deaths;",
  "a higher dose caused abdominal oedema and deaths (that group was excluded from the analysis; kidney enlargement and ascites at necropsy); the tables list two sham animals although the Methods state three per group;", "A01-13b")
f("A01_pba_class", "DR-A01-010:measured_result_note",
  "Shows that a cytosolic mutant enzyme can respond to an HDAC6 lever, which butyrate does not engage.",
  "Suggests, in one small study (Pah enu2 F263S mice, two tabulated sham against three treated animals), that a mutant liver enzyme can respond to an HDAC6 inhibitor; this paper does not test whether butyrate engages HDAC6.", "A01-13c")
# ---- HE's ADV-293 sentence (file IT_SENTENCE_M01_tazemetostat_exposure_20261126.md, main 8637c9d78)
f("M01_neurogenic_output_myc_window", "P:p4_card.pharmacology",
  "no brain concentration figure found by these routes;",
  "no absolute brain or CSF concentration found by these routes; the abstract of PMID 32674144 reports one ratio, in brainstem tumour (a human diffuse intrinsic pontine glioma xenograft in mice), not brain parenchyma and not CSF: 3.74 percent of the serum concentration after systemic (intraperitoneal) EPZ-6438 (dose, time point and number of animals not given in the abstract; full text not read);",
  "M01-HE")

f("L01_nrf2_axis", "DA-L01-002:measured_result_note",
  "overlap with WT is marginal for IL1b and absent for TNF",
  "overlap with WT is clear for IL1b (one WT point about 3.1 lies above two of six P47T points) and absent for TNF (gap about 0.15)", "R-04b")
f("A02_proteasome_inhibitor_class", "DR-A02-008:measured_result_note",
  "the ERAD inhibitor raised both half-life (about 1.6-fold)",
  "the ERAD inhibitor raised both half-life (about 1.6-fold as stated in the text, the same value as for lysosome inhibition; the figure is not held)", "R-06b")
