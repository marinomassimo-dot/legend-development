"""IT 2026-11-25 (IT25): wording edits for ADV-287 (cards H02, A01, A02, B01) and ADV-282 increment 3 (cards F01, I01, K01 and needs.json).
Same schema as the IT23/IT24 edit files. Data only; applied by apply_it25.py AFTER the blind check, with the verifiers' own wording where they changed it.
Hypothesis level; nothing here is medical advice; reference genotype class only.
Wording rule (ADV, 2026-11-25): no 'the one / only / largest / N independent / not at all / not stated' without every row and every other cohort of the source table read.
Card text may not carry a number with a concentration or mass unit (check_cards.py): written in words."""
EDITS = []
NEEDS = []
def e(i, card, mode, old, new): EDITS.append(dict(id=i, card=card, mode=mode, old=old, new=new))
def n(i, mode, old, new): NEEDS.append(dict(id=i, mode=mode, old=old, new=new))

# ---------------------------------------------------------------- ADV-287 (SCI sample of 20 statements; six wrong or incomplete by two readers)
e("W01", "H02_gabaat_inactivator_myelin_exposure", "replace",
  "Batch ORCH-SCIBATCH-DR-20261105 (B1): three independent centres put the rate among imaged children between 22.1 and 44.7 percent (one at partial full-text depth, the others at abstract level); the one cohort reporting its exposed denominator gives about 26 percent per exposed child; and unexposed comparators exist",
  "Batch ORCH-SCIBATCH-DR-20261105 (B1), corrected 2026-11-25 (ADV-287, every row of the batch table read): eight rates among children imaged during exposure lie between 22.1 and 44.7 percent (PMID 36601084: 38 of 172, 22.1 percent, the children left of 390 imaged after excluding 193 exposed more than a year, 18 exposed under 30 days and 7 others; PMID 34786694: 25 of 77, 32.5; PMID 42735667: 18 of 64, 28.1; PMID 40527948: 34 of 76, 44.7; PMID 20384718: 25 of 81, 30.9; PMID 18783433: 7 of 22, 32; PMID 39570186: 17 of 56, 30.4; PMID 39641935: 27 of 76, 35.5, a tuberous sclerosis cohort), and three smaller or selected sets give about 15 percent (PMID 28230253: 6 of 40 asymptomatic imaged children; PMID 35183975: 2 of 13 imaged; PMID 35180571: 44 of 288 children seen with West syndrome, not all exposed or imaged); the reports are not shown to be independent (two come from one department), and only PMID 36601084, 39570186 and 39641935 were read beyond the abstract; where an exposed denominator is stated or can be derived the rate per exposed child runs from about 7 percent (38 of 533 screened, an undercount) through 16 percent (17 of 108, PMID 39570186) to about 26 percent (34 of about 132, derived from 57.6 percent imaged, PMID 40527948; 25 of 95, derived, PMID 20384718), and the tuberous sclerosis cohort gives no separate exposed denominator (its 80 are children imaged during treatment); and unexposed comparators exist")

e("W02", "H02_gabaat_inactivator_myelin_exposure", "replace",
  "infancy (infantile spasms; the labelled indication age is 1 month to 2 years, the age range of the N=205 study is not stated)",
  "infancy (infantile spasms; the labelled indication age is 1 month to 2 years; the label does not state the age range of the N=205 study, but the abstract of the study these figures match, PMID 19054414, gives infants aged 24 months or less)")

e("W03", "A01_pba_class", "replace",
  "the levels applied in cells were about 8 to 78 times the class's HDAC enzyme IC50 (arithmetic, not occupancy);",
  "in the two precedents analysed (applied at 2 and 5 millimolar) the levels were about 8 to 78 times the phenylbutyrate recombinant HDAC1 and HDAC6 IC50 (64, 162 and 240 micromolar; arithmetic, not occupancy); over all applied cell levels (0.5 to 10 millimolar) and all held recombinant phenylbutyrate IC50 rows (HDAC1, 2, 3, 6 and 8, 64 to 260 micromolar) the ratio is about 2 to 156, against the HeLa-extract Ki rows (2.8 and 6.3 micromolar) about 80 to 3,600, and for butyrate on HDAC1 in the same two precedents 6.7 to 312 (on HDAC6 only a bound);")

e("W04", "A02_proteasome_inhibitor_class", "replace",
  "one not at all in the mouse (T191M), and a stable but inactive allele (G307S) not at all;",
  "one not significantly in the mouse (T191M; neither inhibitor restored significant activity, although bortezomib seemed to stimulate a very small amount), and a stable but inactive allele (G307S; not tested in this paper, which cites earlier work of the same laboratory, not read here, in which bortezomib was not effective) not at all;")

e("W05", "B01_amlexanox", "replace",
  "About 57 percent of classifiable individuals in the largest genotype-classified cohort are null/null (56.8 percent in the abstract of the 2025 Neurology cohort of 50 individuals from 45 families, PMID 40875931, confirmed by PubMed abstract on 2026-10-21;",
  "About 57 percent of classifiable individuals in the 2025 Neurology cohort of 50 individuals from 45 families (PMID 40875931; 25 of 44 genotype-classified) are null/null (56.8 percent in its abstract, confirmed by PubMed abstract on 2026-10-21); Oliver 2023 (PMID 36779245) genotype-classified 75 cases, 13 new and 62 from the literature, of which 45 (60.0 percent) are null/null, so the 2025 cohort is not the largest classified set and the two sets are not to be summed;")

# ---------------------------------------------------------------- ADV-282 increment 3 (SCI; three verified errors first)
e("X01", "F01_glutamate_receptor_node", "replace",
  "(10 sustained; at variant level counting sustained effect only the authors report P = 0.0698, not significant)",
  "(10 sustained; the authors' Fisher exact test of a 9 angstrom distance classification gives P = 0.0698 when scored per individual with only sustained effects counted as positive and P = 0.0210 at variant level; neither tests the 14 of 19 against the comparator group, which is the P = 0.0049 of the next row)")

e("X02", "F01_glutamate_receptor_node", "replace",
  "(the comparator group also holds 4 variants the authors call non-pathogenic)",
  "(the comparator group also holds five individuals whose variants the authors call non-pathogenic)")

e("X03", "F01_glutamate_receptor_node", "replace",
  "Benefit in 3 of 15 (group of 15 includes 4 non-pathogenic variants), mild and parent-reported only; seizure reduction 2 of 10, not different from the gain-of-function group.",
  "Benefit in 3 of 15 (the group of 15 includes five individuals with variants the authors call non-pathogenic: Table S1 lists variants of unknown significance in #8, #19, #28, #29 and #31, while the text says five of unknown significance and one likely benign), mild and parent-reported (one also reported by the kindergarten); seizure reduction 2 of 10, not different from the gain-of-function group, and both reductions come from two carriers (#28 and #29) of variants not tested for function and rated no effect by the authors, none from a carrier with a tested loss-of-function or indeterminate variant.")

e("X04", "F01_glutamate_receptor_node", "replace",
  "the drug is not isolated, the exposure and timing are unknown.",
  "the drug is not isolated; the paper lists the antiseizure drugs prescribed over the years and the current regimen (valproic acid, levetiracetam and perampanel, with doses), so the exposure is not unknown, but the timing of each drug is not given, and the statement is about sustained benefit, so a transient benefit is not excluded.")

e("X05", "I01_pdk_inhibition_dca_premise_seizure_glycaemia", "replace",
  "Progenitors -0.67, LOWER IN SIGN ONLY: inside the single-gene null (p about 0.49) and the interval (about 0.45, Poisson) spans zero; the day-14 neuron stage shows +0.44 (same interval), so the sign is not concordant across stages and no decrease is demonstrated. n = 1 per arm: descriptive only.",
  "Library-size-normalised shifts of PDK1 recomputed from the deposit: -0.54 in progenitors and -1.07 in day-14 neurons, both decreases; the neuron pair's column totals differ about threefold (summed TPM 89,581 against 264,496), so the neuron value depends on the normalisation, and after median re-centring the values are -0.74 and +0.38; n = 1 library per arm, so no decrease is demonstrated and the note is descriptive only. The earlier values (-0.67 with p about 0.49 and a Poisson interval of about 0.45, and +0.44 in neurons) do not reproduce from the deposit, their normalisation is not stated, and the statement that the interval spans zero was wrong for them (-0.67 with a half-width of 0.45 excludes zero). WWOX knockdown is shown by Western blot in progenitors only (Supplementary Figure 1); the WWOX CAGE signal is 1.15 times control in progenitors and 0.20 in neurons.")

e("X06", "I01_pdk_inhibition_dca_premise_seizure_glycaemia", "replace",
  "In the same cells hexokinase activity, LDH activity and lactate were higher.",
  "In the same cells lactate was higher in all four conditions, hexokinase activity in two (normoxia and hypoxia, both with normoglycaemia) and LDH activity in two (normoxia with normoglycaemia and with hyperglycaemia); the hypoxia-hyperglycaemia 'no effect' coincides with no reduction of total WWOX in those cells (Figure 8), and WWOX overexpression lowers PDH activity in hypoxia (p < 0.001), so the assay can move; the unresolved 'PDK' wording stays as stated above.")

e("X07", "K01_hif_axis_glycolytic_shift", "replace",
  "one blot repetition is shown. It is the cytoplasmic pool, whereas the MEF increase is nuclear: different compartments, so this neither confirms nor cleanly contradicts the MEF observation.",
  "one blot repetition is shown, with fractions prepared after 6 h in the tested conditions. Total HIF-1alpha by immunocytochemistry (Figure 8) is higher in the knockout in the two normoxic conditions. It is the cytoplasmic pool, whereas the MEF increase is nuclear: different compartments, so this neither confirms nor cleanly contradicts the MEF observation.")

e("X08", "K01_hif_axis_glycolytic_shift", "replace",
  "(the authors' wording; not a demonstrated equivalence).",
  "(the authors' wording; not a demonstrated equivalence; a 6 h fractionated blot with one repetition shown; total HIF-1alpha by immunocytochemistry is higher in the two normoxic conditions, so the null applies to the nuclear fraction, not to total protein).")

e("X09", "K01_hif_axis_glycolytic_shift", "replace",
  "lowering HIF-1alpha, HDAC5 and PFKFB3 together accompanied fewer seizures;",
  "in mice a miR-485 agomir lowered the seizure grade and, in cultured neurons, its effects were reversed by overexpression of HDAC5, of HIF-1alpha or of PFKFB3, tested node by node (PMID 34021541, full text held; the held paper does not lower the three together);")

e("X10", "K01_hif_axis_glycolytic_shift", "replace",
  "Abstract level for most rows;",
  "Abstract level for PMIDs 24889205, 36655171 and 42276303 (no file of them is held in files/fulltext); PMID 34021541 was read in full text;")

# ---------------------------------------------------------------- needs.json copies (the pages render these)
n("N01", "replace",
  "at variant level counting sustained effect only P = 0.0698;",
  "the Fisher P of 0.0698 belongs to a 9 angstrom distance classification scored per individual (0.0210 at variant level) and does not test the 14 of 19;")
n("N02", "replace",
  "(the 15 include 4 variants the authors call non-pathogenic)",
  "(the 15 include five individuals whose variants the authors call non-pathogenic; both seizure reductions of the comparator come from two carriers of untested variants rated no effect)")
n("N03", "replace",
  "but both are inside the single-gene null (p about 0.49 and 0.30) and the hNPC Poisson interval spans zero;",
  "but the progenitor -0.67 and its p of about 0.49 do not reproduce from the deposit (library-size-normalised -0.54 in progenitors and -1.07 in neurons, both decreases, the neuron value depending on normalisation; normalisation of the earlier figure not stated), the organoid's -0.39 is inside its single-gene null (p about 0.30), and one library per arm means no decrease is demonstrated;")

# ---------------------------------------------------------------- ADV-287 step 2 (SCI, adv287_step2_marked_statements_sci_20261125): the corrected wording is read from SCI's table
import csv as _csv
_S = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv287_step2_marked_statements_sci_20261125/"
_st = {x["k"]: x for x in _csv.DictReader(open(_S + "producer/STEP2_TABLE.tsv", encoding="utf-8"), delimiter="\t")}
_cs = {x["k"]: x for x in _csv.DictReader(open(_S + "CORRECTED_SENTENCES_ADV287_STEP2_SCI_20261125.tsv", encoding="utf-8"), delimiter="\t")}
# k=20: SCI's corrected unit begins with 'and the Adm increase ...', which restates the lead already in the packet: the old unit is widened to the lead
_LEAD20 = "and the Adm increase in the three forebrain regions is a two-animal effect (M6 and F8; "
for _k, _id in (("2", "Y01"), ("8", "Y02"), ("10", "Y03"), ("12", "Y04"), ("20", "Y05"), ("7", "Y06")):
    _old = _st[_k]["sentence"]
    if _k == "20": _old = _LEAD20 + _old
    e(_id, _st[_k]["card"], "replace", _old, _cs[_k]["corrected_sentence"])


# ---------------------------------------------------------------- rewritten after blind reader A (VERIFIER_REPORT_AS_DELIVERED_A_IT25.txt): W01 to W05 replaced
_REWRITTEN = {"W01", "W02", "W03", "W04", "W05"}
_OLD = {x["id"]: x["old"] for x in EDITS if x["id"] in _REWRITTEN}
_CARD = {x["id"]: x["card"] for x in EDITS if x["id"] in _REWRITTEN}
EDITS[:] = [x for x in EDITS if x["id"] not in _REWRITTEN]

e("W01", _CARD["W01"], "replace", _OLD["W01"],
  "Batch ORCH-SCIBATCH-DR-20261105 (B1), corrected 2026-11-25 (ADV-287, then a blind check): eight rates with counts, among children imaged during exposure, lie between 22.1 and 44.7 percent (PMID 36601084: 38 of 172, 22.1 percent, the children left of 390 imaged after excluding 193 exposed more than a year, 18 exposed under 30 days and 7 others; PMID 34786694: 25 of 77, 32.5; PMID 42735667: 18 of 64, 28.1; PMID 40527948: 34 of 76, 44.7; PMID 20384718: 25 of 81, 30.9; PMID 18783433: 7 of 22, 32; PMID 39570186: 17 of 56, 30.4; PMID 39641935: 27 of 76, 35.5, a tuberous sclerosis cohort); a ninth report, PMID 19054414 (205 infants, ten sites), gives 22 percent in exposed against 4 percent in naive infants with no counts in its abstract. Three smaller or selected sets give about 15 percent (PMID 28230253: 6 of 40 asymptomatic imaged children, a subset: the same abstract counts 4 further symptomatic cases, so among all children imaged during exposure the rate is probably nearer 10 of 45, about 22 percent, derived and not stated; PMID 35183975: 2 of 13 imaged, of 15 treated; PMID 35180571: 44 of 288 children in a West syndrome database, the abstract not stating how many were exposed or imaged). The reports are not independent: PMID 36601084 states that it extended the cohort of the earlier report from the same hospital (PMID 34786694), and PMID 28230253 and 39570186 come from one group (the later reports no patient overlap), so the eight rates are at most seven independent cohorts; only PMID 36601084, 39570186 and 39641935 were read beyond the abstract. Where an exposed denominator is stated or can be derived the rate per exposed child runs from about 7 percent (38 of 533 screened, an undercount) through 13 percent (2 of 15 treated, PMID 35183975) and 16 percent (17 of 108, PMID 39570186) to about 26 percent (34 of about 132, derived from 57.6 percent imaged, PMID 40527948), about 30.5 percent (29 of 95 exposed, PMID 20384718: 25 of the 81 imaged during but not before treatment plus 4 of the 14 imaged before, during and after; 81 plus 14 is 95, so every exposed child had a scan during treatment) and about 39 percent (31 of 80 treated infants imaged during treatment, PMID 39641935, crude; 27 of 76 after excluding four with the abnormality before treatment); and unexposed comparators exist and differ: none in 12 (PMID 20384718) and none in 56 (PMID 18783433), and the two given next")

e("W02", _CARD["W02"], "replace", _OLD["W02"],
  "infancy (infantile spasms; the labelled indication age is 1 month to 2 years; the label does not state the age range of the N=205 study and cites no source; the study its figures match (205 infants, 22 percent against 4 percent), PMID 19054414, gives infants aged 24 months or less, an identification inferred from the three matching numbers and not stated by the label; the label's separate older-patient figure, N=656 from placebo-controlled trials, does not match that paper's older arms)")

e("W03", _CARD["W03"], "replace", _OLD["W03"],
  "in the two precedents analysed (applied at 2 and 5 millimolar) the levels were about 8 to 78 times the phenylbutyrate recombinant HDAC1 and HDAC6 IC50 (64, 162 and 240 micromolar; arithmetic, not occupancy); over the five applied-concentration rows of the table (0.5 to 10 millimolar; cells and, for 5 millimolar, a worm-plate level the table records as C. elegans) and all six held recombinant phenylbutyrate IC50 rows (HDAC1 twice, 2, 3, 6 and 8, 64 to 260 micromolar) the ratio is about 2 to 156, against the HeLa-extract Ki rows (2.8 and 6.3 micromolar) about 80 to 3,600, and a qualitative cell record at 0.1 millimolar in the same table would put the low end below 1 against the recombinant IC50 (about 0.4 against 260 micromolar); for butyrate on HDAC1 in the same two precedents the ratio is 6.7 to 312 (on HDAC6 only a bound);")

e("W04", _CARD["W04"], "replace", _OLD["W04"],
  "one not significantly in the mouse (T191M; the Results state that neither inhibitor restored significant enzymatic activity, although bortezomib did seem to stimulate a very small amount; the activity figure is not held), and a third allele (G307S; not tested in this paper, whose Introduction says only that in earlier work of the same laboratory, not read here, bortezomib was not effective in restoring function to it; the paper does not say whether that protein is stable or active);")

e("W05", _CARD["W05"], "replace", _OLD["W05"],
  "About 57 percent of classifiable individuals in the 2025 Neurology cohort of 50 individuals from 45 families (PMID 40875931; 44 of the 50 genotype-classified, 25 of them null/null; the article is not held, the manifest locators carry the 25 and the 44 and the abstract the class percentages 56.8, 29.5 and 13.6) are null/null (56.8 percent in its abstract, confirmed by PubMed abstract on 2026-10-21); Oliver 2023 (PMID 36779245) genotype-classified 75 cases, 13 new and 62 from the literature, of which 45 (60.0 percent) are null/null, so the 2025 cohort is not the largest classified set and the two sets are not to be summed;")
