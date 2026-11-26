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

# ---------------------------------------------------------------- rewritten after blind reader B (VERIFIER_REPORT_AS_DELIVERED_B_IT25.txt, kept in the window tmp folder and copied to this folder at landing)
_RB = {"X01", "X03", "X05", "X06", "X07", "X08", "X09"}
_OB = {x["id"]: (x["card"], x["old"]) for x in EDITS if x["id"] in _RB}
EDITS[:] = [x for x in EDITS if x["id"] not in _RB]
_NB = {x["id"]: x["old"] for x in NEEDS if x["id"] in {"N02", "N03"}}
NEEDS[:] = [x for x in NEEDS if x["id"] not in {"N02", "N03"}]

e("X01", *_OB["X01"][:1], "replace", _OB["X01"][1],
  "(10 sustained; the authors' Fisher exact test of a 9 angstrom distance classification gives P = 0.0698 when scored per individual with only sustained effects counted as positive and P = 0.0210 at variant level; neither tests the 14 of 19 against the comparator group, which is the P = 0.0049 of the next row, and that 14 counts the 4 individuals whose effect faded; 16 of the 19 are possible gain-of-function by the authors' threshold rules and three are likely)")

e("X03", *_OB["X03"][:1], "replace", _OB["X03"][1],
  "Benefit in 3 of 15 (the group of 15, which keeps #19 although the Results say it was excluded from further analyses, includes five individuals with variants the authors call non-pathogenic: Table 1 lists four of unknown significance (#8, #19, #29, #31) and one likely benign (#28), the supplementary table of ACMG classes lists all five as unknown significance, and the text counts them as five in one place and as six in another), mild and parent-reported (one also reported by the kindergarten); seizure reduction 2 of 10, not different from the gain-of-function group (P = 0.417), and both reductions come from two carriers (#28 and #29) of variants not tested for function and rated no effect by the authors, so counting them would make 5 of 15; neither reduction is isolated from other changes (antiseizure drug changes in #28 and a regimen of three drugs in #29), and none comes from a carrier with a tested loss-of-function or indeterminate variant.")

e("X05", *_OB["X05"][:1], "replace", _OB["X05"][1],
  "Recomputed from the deposit (one library per arm; PDK1 tags 263 against 51 in progenitors and 108 against 64 in day-14 neurons), the log2 ratio of the deposited TPM is -0.54 in progenitors and -1.07 in neurons. The neuron pair's gene-table column sums differ about threefold (summed TPM 89,581 against 264,496); normalising to those sums gives +0.49, while median re-centring over expressed genes gives -0.60 to -0.77 in progenitors and +0.34 to +0.50 in neurons depending on the gene filter (-0.74 and +0.41 with every gene detected in both libraries). The earlier centred values (-0.67 and +0.44) are matched to within 0.001 by median centring over genes with a pair-mean TPM of at least 10, a filter found after the fact, so they are filter-dependent rather than irreproducible; their original normalisation is not stated and their p of about 0.49 could not be reproduced. A Poisson half-width of about 0.45 around -0.67 excludes zero, and with one library per arm no decrease is demonstrated; the note is descriptive only. WWOX knockdown is shown by one Western blot in progenitors only (Supplementary Figure 1); the WWOX CAGE signal is 1.15 times control in progenitors and 0.20 in neurons (0.60 after normalising to the column sums). In the progenitor library PAX6, SOX2, HES5, FABP7 and SOX21 are lower while NES, VIM, HES1 and SLC1A3 are not, so the line differs in state from its control, which confounds every metabolic comparison in it.")

e("X06", *_OB["X06"][:1], "replace", _OB["X06"][1],
  "In the same cells lactate was higher in all four conditions, hexokinase activity in two (normoxia and hypoxia, both with normoglycaemia) and LDH activity in two (normoxia with normoglycaemia and with hyperglycaemia); hexokinase is visibly lower in the knockout in normoxia with hyperglycaemia and citrate synthase lower in hypoxia with hyperglycaemia, both unmarked. The PDH point estimates in the knockout are higher, not lower (about 30 percent in normoxia and 47 percent in hypoxia, with large error bars), so the PDH result is a low-power null; n is not stated. The hypoxia-hyperglycaemia 'no effect' coincides with no reduction of total WWOX by immunocytochemistry and mRNA, but control WWOX there already sits at the knockout level, and the fractionated blot does show WWOX depleted in that condition (Figure 6). WWOX overexpression lowers PDH activity in hypoxia (p < 0.001). The 'knockout' is a CRISPR guide pool with protein 8.5-fold and mRNA 3-fold lower, not a complete knockout, and the unresolved 'PDK' wording stays as stated above.")

e("X07", *_OB["X07"][:1], "replace", _OB["X07"][1],
  "one blot repetition is shown, with fractions prepared after 6 h in the tested conditions per Methods 4.6 (the Figure 6 caption says 48 h), and the cytoplasmic HIF-1alpha bands are very faint except in control hypoxia. Total HIF-1alpha by immunocytochemistry (Figure 8) is higher in the knockout in the two normoxic conditions. It is the cytoplasmic pool, whereas the MEF increase is nuclear: different compartments, so this neither confirms nor cleanly contradicts the MEF observation.")

e("X08", *_OB["X08"][:1], "replace", _OB["X08"][1],
  "(the authors' wording; not a demonstrated equivalence; a fractionated blot with one repetition shown, 6 h per Methods 4.6 and 48 h per the Figure 6 caption; total HIF-1alpha by immunocytochemistry is higher in the two normoxic conditions, so the null applies to the nuclear fraction, not to total protein; by eye the knockout nuclear bar is about 5-fold above control in normoxia and about 6-fold below it in hypoxia with hyperglycaemia, both non-significant with very large error, so the point estimates run in opposite directions; the authors' Discussion nevertheless states translocation to the nucleus, which this blot does not show; the HRE reporter is higher in 3 of 4 conditions and HIF1A mRNA significantly in 2 of 4).")

e("X09", *_OB["X09"][:1], "replace", _OB["X09"][1],
  "in mice a miR-485 agomir lowered the seizure grade together with HDAC5, HIF-1alpha and PFKFB3 protein, and its effects (seizure grade, apoptosis, oxidative and cytokine markers) were reversed in turn by overexpression of HDAC5, of HIF-1alpha or of PFKFB3, each tested separately (PMID 34021541, full text held); the paper does not lower HIF-1alpha or PFKFB3 alone, or with a drug, in a seizure or firing readout, and its in vivo readout is the acute pilocarpine Racine grade (10 mice per group);")

n("N02", "replace", _NB["N02"],
  "(the 15 include five individuals whose variants the authors call non-pathogenic; the two seizure reductions of the comparator come from two carriers of untested variants rated no effect, and counting them would make 5 of 15)")
n("N03", "replace", _NB["N03"],
  "but the progenitor values (-0.54 and -1.07 on the deposited counts; -0.60 to -0.77 and +0.34 to +0.50 after median centring, depending on the gene filter) show that the earlier -0.67 and +0.44 are filter-dependent and not demonstrated, the organoid's -0.39 is inside its single-gene null (p about 0.30), and one library per arm means no decrease is demonstrated;")

# ---------------------------------------------------------------- IT26 (2026-11-26): Y01 to Y06 rewritten after blind reader C (VERIFIER_REPORT_AS_DELIVERED_C_IT25.txt);
# Y07 to Y12 and N04 to N06 are carriers of the same statements. Where IT26 departs from reader C (Q230P is held: Johannsen 2018, PMID 29808465, which reader C
# had no PMID for; stiripentol cell-level concentrations; a U87 lysate LDH assay) the text went to a second blind check (BLIND_PACKET_D_IT26.txt), and the wording below is
# the one after its report (VERIFIER_REPORT_AS_DELIVERED_D_IT26.txt: D1 and D4 MUST CHANGE, D2 and D3 additions). The SNU387 sentence comes from IT26's dated search of 2026-11-26.
_YI = {"Y01", "Y02", "Y03", "Y04", "Y05", "Y06"}
_OY = {x["id"]: (x["card"], x["old"]) for x in EDITS if x["id"] in _YI}
EDITS[:] = [x for x in EDITS if x["id"] not in _YI]
def y(i, new, old=None): e(i, _OY[i][0], "replace", old or _OY[i][1], new)

# Y01 = reader C block C1 (card A01); Y06 = block C2 (E02 against); Y02 = block C3 (E02 next measurement); Y03 = C4 (F03); Y04 = C5 (F04); Y05 = C6 (K01)
y("Y01", "A required-fold limit: a boost can at best multiply the mutant's residual function (amount relative to wild type times function per molecule), so parity with wild type needs a fold gain equal to the reciprocal of that product. No held measurement read for this card gives a calibrated value of it for Q230P, P252A or P282A. Q230P: WWOX protein was not detected by Western blot in one patient's fibroblasts, whose WWOX transcript level was almost identical to that of three other cell lines (Johannsen 2018, PMID 29808465; no healthy fibroblast control, no detection limit stated, function not measured). P252A and P282A (Zhang 2025, PMID 41124647; over-expressed Flag-tagged protein in thyroid-cancer lines): P252A protein is about 0.16 to 0.36 of wild type at steady state (Fig 4C-F), with about 0.3 of the starting level left at 6 to 10 hours against about 0.7 to 0.9 for wild type (Fig 4B), and chloroquine or ammonium chloride raise it about 1.8 to 2 fold (Fig 4D, 4E; function not read); P282A is about 0.6 to 0.95 of wild type (Fig 4C-F) and is a common population variant (gnomAD allele frequency about 0.07, Supplementary Table 4). Neither mutant differs significantly from empty vector in the function assays that include one (for example colony number relative to empty vector in CAL-62: wild type about 0.57, P252A about 1.3, P282A about 1.05, Fig 2B); growth, colony and invasion read-outs sit at about the vector level, while in some other read-outs the mutant mean lies between vector and wild type (gamma-H2AX, Fig 5B; NHEJ for P282A, Fig 5C; BCPAP migration, Fig 2F), so non-significance is not equivalence and none of this gives a residual fraction (no dose-response, over-expression). A patient homozygous for both had no WWOX nervous-system disease, and the authors suggest the proteins may keep some function (a conjecture, not a measurement). Separately, a liver-cancer line carrying a P252A change of unknown zygosity (SNU387) has low WWOX transcript and low protein, which cannot be attributed to the variant (Park 2004, PMID 15266310). The observed gains in the non-WWOX precedents read run from about 1.05 (a non-significant butyrate bar, DeLeeuw Fig 5F) to about 19 to 21 fold on the GAT-1 Fig 4G bars (by pixel about 6, 7, 14 and 21 for D52Y, V125M, A357V and G566H, the last two with 15 to 25 percent error because the untreated bars are 7 to 8 pixels high; by eye about 5, 7, 10 and 15), and to tens-fold or 14-fold where the untreated baseline is at the assay floor (Shah Fig 3B, glycerol on G443D; fly G443V with 4-phenylbutyrate). Wild type is raised in some precedents (about 1.2 to 2.7 fold) and not significantly changed in others (flies, Shah Fig 6B, image only; GAT-1 wild-type uptake with phenylbutyrate or TUDCA, DeLeeuw Fig 4A, bars about 1.2).",
  old="A required-fold limit: a boost multiplies the mutant's residual function and does not change it; " + _OY["Y01"][1])

e("Y07", "A01_pba_class", "replace", "neither factor is measured for any WWOX allele.",
  "for Q230P neither factor has a calibrated value (protein not detected in one patient's fibroblasts with no detection limit stated, Johannsen 2018, PMID 29808465; function not measured), and the held P252A and P282A readings (over-expressed protein, Zhang 2025, PMID 41124647; for P252A also one cancer line, PMID 15266310) give no residual fraction.")

y("Y02", "IT8 P3 2026-10-29, restated IT9 P4a 2026-10-30, corrected 2026-11-26: stiripentol is not sufficiently supported as an LDH-engagement probe, because the enzyme-level data are weak and no potency has been fitted (7 percent inhibition at 2 millimolar; 9.9 percent for the racemate at 0.5 millimolar; the fuller list is in the evidence against), the US label names no LDH mechanism, and the cell-level readings found (four rows of a 2022 glycolate-oxidase and LDHA double-inhibitor series: relative oxalate output 0.27 to 0.70 at 10 micromolar in mouse hepatocytes; in the papers read, lactate production about halved at 500 micromolar and extracellular acidification and oxygen consumption lower at 25 and 50 micromolar in glioblastoma cells, and lower oxalate output in HepG2 cells at 5 to 100 micrograms per millilitre) do not separate LDH from other actions (complex I inhibition for the glioblastoma readings, Bouchez 2026; glycolate oxidase for the hepatocyte series), so they do not establish LDH engagement; the HepG2 report also gives lower urine oxalate in rats and patients, which is not direct LDH engagement either;",
  old="IT8 P3 2026-10-29, restated IT9 P4a 2026-10-30: stiripentol is not sufficiently supported as an LDH-engagement probe, because the readable enzyme data give 7 percent inhibition at 2 millimolar and about 10 percent at 0.5 millimolar (no fitted value: no enzyme-level support), the US label names no LDH mechanism, and the one cell-level signal found (four rows of a 2022 glycolate-oxidase and LDHA double-inhibitor series: relative oxalate output 0.27 to 0.70 at 10 micromolar in mouse hepatocytes) does not establish LDH engagement;")

y("Y03", "New: (1) the transcript-level ratio in the public human knockout deposit does not point to a depolarising gradient (descriptive, confounded: the SLC12A2 to SLC12A5 transcript ratio is 0.13 to 0.29 in knockout against 0.29 to 0.30 in wild type, not higher, and clearly lower only in the two knockout libraries that also carry more of the inhibitory-neuron markers GAD1 and SLC32A1, both of which the authors' own list gives as higher in knockout. The deposit is GSE156243, four knockout and two wild-type organoid libraries at 15 weeks from one embryonic stem cell line, two further wild-type libraries having been excluded by the authors for quality. A second human knockout record, E-MTAB-14792, exists but returned 403 Study not accessible on 2026-10-25);")

y("Y04", "NMDAR dependence is not NMDAR gain: depolarised resting potential (about -73.6 against -79.3 mV) and reduced inhibition suffice (not tested directly: no isolated NMDAR currents or NMDA to AMPA ratio; the only proxy, mEPSC decay recorded at -70 mV, is unchanged at 4.84 against 5.18 ms). Among the whole-cell synaptic measures the text quantifies, the largest relative change is inhibitory (sIPSC amplitude 27.5 against 57.3 pA in pooled controls, a derived 52 percent lower, and frequency 8.4 against 10.3 Hz, derived 18 percent lower; mean and SD over events) while sEPSC amplitude is a derived 6 percent higher; intrinsic properties in Table 1 change more (sag 118 percent higher) but are not synaptic. The delayed NMDA-receptor-dependent field-evoked response in layer II/III (layer V stimulation) is about four times larger in knockout slices (about 0.46 against 0.116 mV at 100 microamperes, pixel-read from Supplementary Fig S3B, whose axis starts at about 0.07 mV, so about nine times above that floor; p = 0.0038; 6 slices from 3 knockout and 7 slices from 4 wild-type animals) and d-APV lowers it to about 0.40 of baseline (Supplementary Fig S3C; washout overshoots to about 1.3), so no measure is called the largest across field and whole-cell recordings.",
  old="NMDAR dependence is not NMDAR gain: depolarised resting potential and reduced inhibition suffice (not tested). " + _OY["Y04"][1])

y("Y05", "and the Adm increase in the three forebrain regions is carried mainly by two animals (M6 and F8): the mean log2CPM difference is 0.96, 1.19 and 0.81 (hippocampus, cortex, PFC) with all five mutants, 0.49, 0.70 and 0.45 (derived) without M6, and 0.24, 0.41 and 0.03 (derived) without M6 and F8 (reproduced within 0.03 under total-count and under TMM scaling); of the other three mutants F10 (CPM 2.58) lies above, F9 (1.32) just below and M7 (2.22) at the upper edge of the hippocampal wild-type range 1.42 to 2.17 (M7 above or inside it depending on the normalisation), M7 (3.30) lies just above the cortical range 1.17 to 3.19, and all three lie inside the PFC range 1.92 to 3.36.")

y("Y06", "IT8 P3 (2026-10-29), corrected 2026-11-26: for stiripentol as a way to test the LDH node, the enzyme-level data are weak and no potency has been fitted - 7 percent inhibition of both human LDH5 and LDH1 at 2 millimolar (ChEMBL document CHEMBL4311969; the same document lists two 0.5 millimolar LDH rows with no value), 9.9 percent for the racemate at 0.5 millimolar in an independent report (Rico-Molina 2024) whose two enantiomers give 34 and 38 percent at the same concentration (the racemate lies below both, so the three figures are not mutually consistent; all three IC50 are printed as above 500 micromolar), about 40 percent at 0.5 millimolar attributed to Sada 2015 (second-hand), and an LDH assay on lysate of U87 glioblastoma cells that had been exposed to stiripentol, with LDH added per well (so not a direct enzyme-inhibition test), whose inhibition the authors call moderate, significant only at 250 and 500 micromolar, with no percentage given in the text (PMID 42035940); no fitted LDH potency among the 88 database rows read for it; a label that does not name LDH;")

e("Y08", "E02_ldh_inhibition", "replace", "one cell-level signal (mouse hepatocyte oxalate output at 10 micromolar, shared with glycolate oxidase)",
  "the database cell-level signal (mouse hepatocyte oxalate output at 10 micromolar: four rows, two cell models at 24 and 48 hours, relative output 0.27 to 0.70, in an assay labelled GO/LDHA, so shared with glycolate oxidase)")
e("Y09", "E02_ldh_inhibition", "replace", "of the 89 with a same-document LDHA and LDHB pair",
  "of the 89 with a same-document, same-activity-type LDHA and LDHB pair")
e("Y10", "F03_bumetanide_chloride_gradient", "replace", "their outcomes were NOT read here.",
  "their abstracts (PubMed, read 2026-11-26) report that NEMO was stopped early for serious adverse reactions and limited evidence of seizure reduction (hearing impairment in 3 of 11 surviving infants), that the phase 2 autism trial was negative on its primary outcome (one secondary outcome positive; adverse effects mainly diuretic), and that the phase 3 record gives baseline characteristics only.")
e("Y11", "K01_hif_axis_glycolytic_shift", "replace", "+0.1 to +0.6 log2", "+0.1 to +0.8 log2 across the three forebrain regions")
e("Y12", "K01_hif_axis_glycolytic_shift", "replace", "Bhlhe40 and Ndrg1 fall, Ddit4 and Ankrd37 are flat", "in the three forebrain regions Bhlhe40 and Ndrg1 fall and Ddit4 and Ankrd37 are flat or slightly lower (Ankrd37 about -0.3 in PFC), whereas in cerebellum all four are higher (about +0.06, +0.18, +0.21 and +0.31 log2)")
e("Y13", "K01_hif_axis_glycolytic_shift", "replace", "the six-gene selective set changes by", "the six-gene selective set (Adm, Bhlhe40, P4ha1, Ankrd37, Ddit4, Egln3; TMM-scaled log2 counts per million) changes by")

n("N04", "replace", "R is unmeasured for every WWOX allele, and for the Q230P class the only bound is the unquantified detection floor",
  "R has no calibrated value for Q230P, P252A or P282A (P252A and P282A over-expressed protein does not differ significantly from empty vector in function assays, with some intermediate means, which gives no residual fraction, PMID 41124647), and for the Q230P class the only bound is the unquantified detection floor")
n("N05", "replace", "Hk2, Ldha, +0.1 to +0.6 log2)", "Hk2, Ldha, +0.1 to +0.8 log2 across the three forebrain regions)")
n("N06", "replace", "the Adm rise is a two-animal effect (M6, F8)", "the Adm rise is carried mainly by two animals (M6, F8)")
n("N07", "replace", "a boost multiplies the residual function R (amount relative to wild type times function per molecule) and does not change it, so parity needs the reciprocal of R",
  "a boost can at best multiply the residual function R (amount relative to wild type times function per molecule), so parity needs a fold gain of 1/R")
n("N08", "replace", "the selective six-gene set changes by", "the selective six-gene set (Adm, Bhlhe40, P4ha1, Ankrd37, Ddit4, Egln3) changes by")
n("N09", "replace", "Bhlhe40 and Ndrg1 fall;", "Bhlhe40 and Ndrg1 fall in the three forebrain regions (higher in cerebellum);")
