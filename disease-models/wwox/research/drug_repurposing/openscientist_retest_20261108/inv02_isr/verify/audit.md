# Blind audit INV-02 (ISR) - actor vf-02, 2026-11-08 (draft: parts A and B written before opening README.md, phase1_note.md, chains.tsv)

Depth statement. Sources reached by me: 42909904 (PMC full text, Results and Discussion text layer; figure images not viewed); 32000863 (PMC full text, Figure 7 image viewed); 12133000 (title and abstract only, PMC full text empty); 15001529 (title and abstract only); 33531382 (PMC full text, Results and Discussion); 40296303 (PMC full text, Results 3.4 to 3.8, Methods, Discussion; figure images not viewed); 33914858 (abstract plus operator-supplied PDF `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf` pages 12-14, text layer incl. Fig 7 legend); 32894619, 42097410, 28696288 (abstract only); 33300063 (abstract plus operator-supplied text `files/fulltext/PMID33300063_Zhao2020_Spandidos.txt`, Results/Discussion grep and lines 300-345). Claims placed for all 11 PMIDs under vf-02. Identity check run for all 19 PMIDs cited by the report: all MATCH.

## Part A - verdicts

| Item | Verdict | Basis (what I read) |
|---|---|---|
| P01 | SUPPORTED | 42909904 text: "immunocytochemistry revealed a significant upregulation of Atf4 levels in Abeta flies upon knockdown", "not observed in LacZ-expressing" knockdown flies. Adult fly brain, amyloid background only. Report L17 ("no studies ... in a WWOX model") and L9 ("zero primary data") are therefore too wide; the human-protein absence at L19/L155 stands. Also held: needs.json O2 organoid ATF4 target set is LOWER than chance (transcript), i.e. not in the direction of an elevated ISR; the report's silence on it is a gap, not an error. |
| P02 | SUPPORTED | Fig 7c (image viewed) and legend: pSer9-GSK3b lower in -/- cortex, hippocampus, cerebellum at P20; one lane per genotype per region shown (densitometry 2.7/3.1/1.3 cerebellum; 3.6/3.5/2.0 hippocampus; 3.9/3.8/2.5 cortex); total GSK3b flat (2.2 to 2.6); legend says "representative results of four independent experiments". It is a Ser9 regulatory-site readout, not activity on eIF2Be. |
| P03 | SUPPORTED | Fig 7d (viewed): LiCl lowers PTZ stage in +/+ (N 12 vs 8), +/- (12 vs 12) and -/- (6 vs 7), all marked ****. So lithium lowers seizure score in controls too. "Abolishes" (report L34, L87, L153) is stronger than the plot: -/- + LiCl still peaks near stage 1 early. The paper never measures eIF2B. |
| P04 | SUPPORTED (abstract depth) | 12133000 title and abstract: CHO cells; LiCl and two GSK3 inhibitors dephosphorylate Ser535 but "did not elicit significant activation of eIF2B". The report quotes only the background sentence of that abstract (in vitro substrate) and calls the paper "the biochemical bridge" (L109); the paper's own result is the opposite of a bridge. 15001529 abstract: neonatal rat cardiac myocytes, LiCl or isoproterenol lowers S535 phosphorylation. Neither is neuronal or WWOX. Full text of 12133000 not reachable by me. |
| P05 | SUPPORTED, one narrowing | 33531382 Results: the salubrinal arm is in C57BL/6 wild-type mice (1 mg/kg daily, 5 days): salubrinal impaired memory (NOR, CFC); ISRIB prevented it and blocked ATF4 without lowering eIF2a-P. So "single adult mouse study" is right, but the salubrinal result is memory only in wild-type mice, not in an AD model and not a synaptic readout (no plasticity for salubrinal in the text read). Report L27 "worsened synaptic/memory outcomes" over-reads; "contraindicated" is a clinical word for this. |
| P06 | SUPPORTED | 40296303 Results 3.4 and 3.7 (text): MBP higher at week 10, "G-ratio ... decreased significantly after ISRIB treatment"; Discussion: "Only two cases of VWM patient-derived iPSCs and two normal control iPSCs"; 3.8: "ISRIB functions as an inhibitor of the UPR signaling pathway". Methods: 500 uM ISRIB (as written). n = 8 organoids per group from three experiments. Figure images not viewed. |
| P07 | SUPPORTED | The quoted sentence is in the structured abstract "Aim" and in the Introduction as background ("ISRIB is a specific eIF2B activator that inhibits the phosphorylation of eIF2"); no result of the paper measures p-eIF2. 33531382 Results: "ISRIB did not prevent the increase in hippocampal eIF2a-P caused by salubrinal" (verbatim, matches held row EI27). So the report's mechanism sentence conflicts with the held mechanism. |
| P08 | SUPPORTED | 33914858 abstract: "Brain hyperexcitability and hypomyelination were also revealed in human brain organoids with a WWOX deletion". PDF page 14 legend: RMP n = 3 vs 4 organoids; Fig 7I "OS-WT (n = 2) and OS-WWOX-KO (n = 3)"; page 12 text: "less negative than typical mature neurons, suggesting that these cells are still in the process of development" and "suggesting a developmental delay in the OS-WWOX-KO". No translation measurement. |
| P09 | SUPPORTED (abstract only) | Abstract: primary rat OPCs; elvitegravir inhibited differentiation, raltegravir none; "activated the integrated stress response ... completely blocked by pretreatment with ... Trans-ISRIB". Drug-induced ISR, rat cells, adult mouse cuprizone arm. Full text not opened. |
| P10 | SUPPORTED (abstract only) | 42097410 abstract: sentence verbatim; review, aging-related cognitive disorders, published 2026-05, identity MATCH. The developmental step is the report's. Note: a single review sentence with "may", not independent confirmation of anything WWOX. |
| P11 | PARTLY | "Untested" is right (no source tests ISRIB against a phospho-eIF2Be lesion). The "expected small" half rests on 33531382 Discussion ("modifies the ISR under conditions of increased eIF2a-P, but not under basal conditions") and on held EI24, a citing-secondary statement; held EI11 (three-fold faster exchange without phospho-eIF2, 1.1 min half-time) points the other way at the partially purified level and is itself contradicted by EI15 at the decamer level. Held rows EI10 EI11 EI15 EI24 EI27 exist and say what the producer writes. An inference with contested support; fine as INFERENZA, not as a settled expectation. |
| P12 | SUPPORTED, one addition | 33300063: abstract: "WWOX activated mTOR whilst inhibiting autophagy"; text lines ~319-326: siRNA WWOX knockdown lowered p-mTOR in A2780 cells (Fig 4C), overexpression raised it (Fig 4D); no densitometry words found in the text (grep: no hit for densitom; "quantif" only for viability). Cells are paclitaxel-treated ovarian carcinoma lines. The quote the report uses ("has been predicted to serve ... to suppress autophagy in various tumor cell types") is a background prediction of the abstract. TSC2 statement (report L46) has no cited source. The paper does contain a WWOX-loss arm pointing the same way as the report's inference; the item omits that and it should say so. |
| P13 | SUPPORTED | pubmed_identity_check: all 19 PMIDs (11 in the evidence table, 6 in the L113 bare list, 2 context) return MATCH, incl. 42097410 (2026-05) and 12376332 (title overlap 0.889, still MATCH). No wrong identifier. A relevance problem exists for one of the six: 18583310 (placenta, Yung) has no eIF2B or GSK3 sentence in its abstract (it concerns ER stress/translation inhibition), so it does not corroborate "GSK-3b to eIF2B in placenta" (report L113, L118). The other five abstracts do mention GSK3 and eIF2Be (18701453, 18252708, 17901358, 12376332) or the pathway (16545079 review). |
| P14 | SUPPORTED (abstract only) | 28696288 abstract: "TBI persistently activates the integrated stress response" and ISRIB "reversed the hippocampal-dependent cognitive deficits ... in two different injury mouse models"; adult mice; ISRIB given weeks after injury. Premise measured in TBI, not in WWOX. |

Counts: SUPPORTED 13 (P01 P02 P03 P04 P05 P06 P07 P08 P09 P10 P12 P13 P14), PARTLY 1 (P11), NOT SUPPORTED 0, UNVERIFIABLE 0.

## Part B - coverage audit of extraction.tsv (read the complete report, L1-L155)

Twelve distinct points, spread from header to the last paragraph:

| # | Report point (line) | Extraction row | Result |
|---|---|---|---|
| 1 | Question as posed: compare p-eIF2a, ATF4 protein, translation, function rather than transcript (L2) | E55 | PRESENT |
| 2 | Header: WOREE/DEE28/EIEE28, MONDO:0014533, date 2026-11-07 (L6) | E57 | PRESENT |
| 3 | Hyal-2/WWOX/Smad4 failure and disrupted cortical migration named as knowledge-base arms (L17) | E03 | PRESENT |
| 4 | Premise that oligodendrocyte maturation and synaptic plasticity are high-rate protein-synthesis processes (L22) | E07 | PRESENT |
| 5 | MEHMO eIF2g mutation suppressed by ISRIB in patient iPSC (L29, L107) | E14 | PRESENT |
| 6 | Prediction that both ISRIB and lithium would disinhibit translation (L38) | E17, E23, E24 (no row states the joint prediction) | PRESENT_NARROWED |
| 7 | GSK-3b suppresses mTORC1 via TSC2 (L46) | E31 | PRESENT |
| 8 | Comparison table cells for AD/TBI: eIF2B function "ISR-elevated", phenotype "plasticity/memory loss", ISRIB rescues (L95-99) | E35 (AD/TBI reduced to "mouse") | PRESENT_NARROWED |
| 9 | Six extra PMIDs by tissue incl. airway smooth muscle, and two WWOX context PMIDs (L113) | E36, E49, E50 | PRESENT |
| 10 | Low p-eIF2a / modest ATF4 though translation suppressed (L120) | E37, E56 | PRESENT |
| 11 | Decision rule: translation down with p-eIF2Be-S535 up, or translation up with low p-eIF2Be (L137) | E41 | PRESENT |
| 12 | Salubrinal as predicted-negative control in organoid experiment (L145) | E18 | PRESENT |

Result: 10 PRESENT, 2 PRESENT_NARROWED, 0 MISSING (12 of 12 at least partly present, none absent). No MISSING, so the extension scan was run only on the same kind as the two narrowed points (predictions stated inside findings, and table cells). Further narrowings found: (a) L98 table cell "ISRIB effect: predicted rescue (untested)" for WOREE is in E35 only as a summary; (b) L96 cell "eIF2B function: initiation defect" for MEHMO is in E35 as a summary. Neither adds a claim missing elsewhere. Suggested fix: add the L38 joint prediction as an inference row, and expand E35 to list the AD/TBI cells.

(After parts A and B were written I opened `phase1_note.md` and `README.md`; both agree with my A and B findings and I changed no verdict because of them.)

## Part C - reconciliation sample (`reconcile.tsv`, 8 rows)

Class census of the file: already_present_and_used 8, present_not_used 6, verified_or_corrected 4, unverified 3, new_to_legend 2, superseded_or_contradicted 1 rows (all 57 items appear exactly once). The brief asks for at least 3 `new_to_legend`; the file has only 2 such rows (E08; E09+E15+E34+E16), so I took both and filled the third with a `verified_or_corrected` row.

| Row (items) | Class | Pointer check | Prior-brief check | Result |
|---|---|---|---|---|
| E08 | new_to_legend | `inv02_isr/evidence.tsv` EV05 EV06 exist; verbatim in abstract. `git grep` for 32894619 outside this folder: 0 files, so new is true | omitted (no earlier brief); n/a | OK |
| E09;E15;E34;E16 | new_to_legend | EV07 exists; 42097410 outside this folder: 0 files; `batch_it28_p4_isr_role_20261105/README.md` rule 1 says "ISR protective or harmful is not well posed" | "narrowed" - checked against that README line: matches | OK |
| E26;E27;E28;E35 | verified_or_corrected (third "new" substitute) | EV01 to EV04 exist; `batch_it28_p4_isr_role_20261105/A_glia_myelin/README.md` has the section "ISRIB VWM organoids" (line 171) and the table line "weak design (two patient lines; no p-eIF2alpha reported in the text read)" | "kept ... VWM as a locked-on ISR": README line 6 supports | OK |
| E06 | already_present_and_used | `deepdive_manifests/PMID33914858.json` exists; receipt FTR-20260923-33914858-01 is in `registries/fulltext_read_receipts.jsonl`; "3 versus 4" and "2 versus 3" and the delay reading match the manifest and the PDF legend I read | kept - not separately checked | OK |
| E19;E20;E48 | already_present_and_used | `gsk3_eif2b_20261107/output/evidence.tsv` E01 E02 E03 exist and say single lane, Ser9 proxy, P20, lithium significant in +/+ and +/- too; receipt FTR-20260804-32000863-01 present; matches my Fig 7 reading | "narrowed" vs `gsk3_inv09_20261107/BRIEF.md` premise C: text matches (Ser9 regulatory indicator from a limited blot; effect in controls limits specificity) | OK |
| E07;E33;E10 | present_not_used | `gsk3_eif2b_20261107/output/chain.tsv` L4 and L5 exist ("no translation or eIF2B measurement in any WWOX model was found ... hypomyelination is not evidence of reduced translation") | "modified": `gsk3_eif2b_20261107/BRIEF.md` line 15 says "Do not conclude 'the ISR is harmful' from chronicity, 'translation is reduced' from hypomyelination" - matches | OK |
| E11;E12;E18 | present_not_used | `nb2_isrib_it36_20261108/output/evidence_isrib.tsv` EI25 EI26 EI27 exist (EI27 quote verbatim in 33531382 full text I read) | "modified": same BRIEF line 15 ends "nor classify salubrinal as clinically contraindicated from these analogies"; IT28 README rule 4 (potentiators contested): matches | OK; note the producer's "salubrinal worsening ... not separately checked in the held rows" is now settled by my read: memory impairment in wild-type mice (NOR, CFC), no plasticity readout in the text I read |
| E37;E56 | superseded_or_contradicted | `isrib_discrim_20261108/output/README.md` line 11 (grid corrected: "little ISRIB response is expected whatever the cause") exists | "modified" - consistent | OK in pointer; WORDING issue: that README line is an INFERENZA, not a measurement, so "superseded_or_contradicted" overstates; "contested by a held inference; untested" is accurate (matches P11 PARTLY) |

Prior-brief fates checked (4 required): E07 row, E11 row, E09 row, E19 row - all four match the cited briefs. Additional pointer checks passed: E01 row (`needs.json` NEED-ISR-ATTENUATION O1 and O2 exist and say what the row says; O1 even states the no-amyloid arm is non-significant, matching my read of 42909904; O2 says the organoid ATF4 target set is lower than chance); E14 row (B_neurons README M2 and M5 quotes present); E29-E32 row (receipt FTR-20261003-33300063-01 present).

## Part D - evidence sample (`evidence.tsv`, all 9 rows)

| Row | Quote verbatim at stated place? | Carries the proposition? |
|---|---|---|
| EV01 (40296303) | Yes, Results 3.7 (hyphen variant of "G-ratio"). The note says 500 uM "in Methods and legends": Methods 2.3 reads "500 uM"; the figure legends in the text layer read "(500 um)" (micrometre sign), so "legends" is as written but internally inconsistent in the source | Yes (P06) |
| EV02 (40296303) | Yes, Introduction (also in the structured abstract "Aim" with "by inhibiting") | Yes for P07; but `proposition_ids` says "P06; P15" - P15 does not exist in `decisive.tsv` and the row should point to P07 |
| EV03 | Yes, Results 3.8 last sentence; Fig 4 legend lists ATF4, ATF6, XBP1-S, no p-eIF2 | Yes (P06 context, and P07) |
| EV04 | Yes, Discussion (limitations); apoptosis by week 16 also stated | Yes |
| EV05 (32894619) | Yes, abstract, verbatim | Yes (P09) |
| EV06 | Yes, abstract, verbatim | Yes (P09); drug-induced ISR, rat cells |
| EV07 (42097410) | Yes, abstract; date 2026-05-05; review | Carries P10; `proposition_ids` says "P08; P13": P08 is the WWOX organoid item, wrong; P13 (identity) is acceptable. Should read "P10; P13" |
| EV08 (28696288) | Yes, abstract | Yes (P14); "persistently activates the ISR" is in the abstract |
| EV09 (42909904) | Query reproduced by me: 1 hit (42909904), 2026-11-08 | Yes (P01); the paper reached via its PMC text: Atf4 up in amyloid flies only |

No quote failed. Gap: propositions P02, P03, P04, P05, P08, P11, P12 have no row in `evidence.tsv` (decisive.tsv marks them "not_read (carried)" or abstract only). I independently confirmed P02, P03, P05, P08, P12 from primary text (see part A), so the producer can add rows without new reading: 32000863 Fig 7 legend ("Quantitative densitometry of the immunoblots was performed", "representative results of four independent experiments"; Fig 7d significance in all three genotypes); 33531382 Results ("Treatment with salubrinal impaired long-term memory in both NOR and CFC tests"); 33914858 Fig 7 legend ("OS-WT (n = 2) and OS-WWOX-KO (n = 3)"); 33300063 ("siRNA-mediated WWOX-knockdown", lower p-mTOR); 12133000 abstract ("did not elicit significant activation of eIF2B").

## Verdict table (proposition, verdict)

| P | Verdict | P | Verdict |
|---|---|---|---|
| P01 | SUPPORTED | P08 | SUPPORTED |
| P02 | SUPPORTED | P09 | SUPPORTED (abstract) |
| P03 | SUPPORTED | P10 | SUPPORTED (abstract) |
| P04 | SUPPORTED (abstract) | P11 | PARTLY |
| P05 | SUPPORTED (one narrowing) | P12 | SUPPORTED (one addition) |
| P06 | SUPPORTED | P13 | SUPPORTED |
| P07 | SUPPORTED | P14 | SUPPORTED (abstract) |

## Corrections the producer must make

1. `inv02_isr/evidence.tsv` EV02, column `proposition_ids`: replace "P06; P15" by "P07" (add P06 only if kept deliberately; P15 does not exist).
2. `inv02_isr/evidence.tsv` EV07, column `proposition_ids`: replace "P08; P13" by "P10; P13".
3. `inv02_isr/evidence.tsv` EV01 note: write "Methods 2.3 reads 500 uM; the figure legends read 500 um (micrometre sign) in the text layer"; do not say legends read micromolar.
4. `inv02_isr/reconcile.tsv` row E37;E56: change `legend_class` from `superseded_or_contradicted` to a class meaning "contested by a held inference, untested" (or keep the class and add to `note`: the LEGEND position is an INFERENZA, not a measurement). The note already says "LEGEND holds that as untested", which contradicts the class label.
5. `inv02_isr/reconcile.tsv` row E11;E12;E18, column `prior_verification`: replace "salubrinal worsening outcomes as a stated outcome not separately checked" by the now-checked fact: in 33531382 salubrinal arm = wild-type C57BL/6 mice, memory impairment (NOR, CFC), ISRIB prevented it without lowering eIF2a-P; no synaptic-plasticity readout for salubrinal in the text. And in `decisive.tsv` P05 say "wild-type mice" rather than "AD-mouse" for the salubrinal arm.
6. `inv02_isr/decisive.tsv` P01 and `README.md` answer-first bullet 1: add that the fly datum is conditional (Atf4 up with neuronal Abeta42, not in LacZ flies, separate tests, no interaction test) - the held needs.json O1 already says so; the README says "only with amyloid" which is slightly stronger than "not significant without amyloid". Also add that PubMed holds WWOX plus PERK data in ovarian carcinoma cells (PMID 28749468: paclitaxel activates IRE1 and PERK, WWOX modulates the response; non-neural), so the report's "no study ... in a WWOX model" fails outside neural cells too; scope the correction accordingly.
7. `inv02_isr/decisive.tsv` P12 and the E36;E49 reconcile row: add that 33300063 contains a WWOX loss arm (siRNA knockdown lowering p-mTOR, Fig 4C) pointing the same way as the report's inference, so the point to make is the cell type (paclitaxel-treated ovarian carcinoma) and the absence of densitometry, not that the inference lacks any WWOX-loss datum. Add that 18583310 (placenta) shows no GSK3 or eIF2B sentence in its abstract, so it does not corroborate the GSK3-eIF2B axis the report cites it for; the other five abstracts do (abstract depth only).
8. `inv02_isr/extraction.tsv`: add one inference row for L38 (both ISRIB and lithium predicted to disinhibit translation) and expand E35 to list the AD/TBI table cells (part B).
9. `inv02_isr/reconcile.tsv`: only 2 rows are `new_to_legend`; no change required, but the README count "new_to_legend 5" is a count of items, not rows; say "items" to avoid confusion.

## Open uncertainties

* 12133000 and 15001529 read at abstract depth only; the 12133000 Results (what "insufficient" means quantitatively; which eIF2B assay) were not reachable (PMC full text empty, Europe PMC returned an error). The proposition is supported by title and abstract, not by Results.
* 33914858 has no open-access full text; I used the operator-supplied PDF in `files/fulltext/`, legend and text layer only, no figure image.
* 40296303 figure images not viewed; the gene names (EIF2B4/EIF2B5 in the report) are stripped from the text layer I read, so I could not confirm which subunits were mutated (the cDNA changes and "VWM1/VWM2" are present).
* 32894619, 42097410, 28696288: abstracts only. 42909904: Results text read; figure images not viewed, so the effect size and the axis starting point (held in needs.json O1) are not independently checked.
* P11: the size of an ISRIB effect without raised phospho-eIF2a is contested at the in-vitro level (held EI11 versus EI15); I did not re-read those sources.
* Claims of absence: my own PubMed checks were two strings on 2026-11-08 (WWOX with ATF4 or integrated stress response or eIF2alpha: 1 hit; WWOX with PERK, GCN2, UPR, ER stress, eIF2, protein synthesis: 5 hits, all non-neural: four cancer-cell records, of which 28749468 reports PERK and IRE1 activation with WWOX in ovarian carcinoma cells, plus one yak milk-protein genetics record). No Europe PMC second route for absence; the human neural-cell absence is therefore "none found by me in two PubMed strings", not proved.
* The dismech knowledge base (report L9, L17) was not opened by either the producer or me.
