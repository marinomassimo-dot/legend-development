# Blind audit, INV-06 (myelination), verifier vf-06, task ORCH-IT38OS-20261108

Date 2026-11-08. Written before opening the producer's `README.md`, `phase1_note.md` or `chains.tsv`; none of the three was opened at any point. I did open `decisive.tsv` only through a single grep line on P12 (same text as `verify/items.md`). Sources were reached by open routes only: the operator-supplied full text and supplement legends of PMID 33914858 under `/home/desktop/legend-development/files/fulltext/`, the PubMed tools (metadata and PMC full text), and Europe PMC `fullTextXML` (curl, retried when it returned HTTP 500). No page summariser (WebFetch) was used for any source, so no confidence is lowered for that reason. Two limits apply: the PubMed full-text tool strips italicised gene symbols (I re-read PMC7811968 through Europe PMC to get the symbols back), and no figure image was viewed for any paper (legends, Results and Methods text only). Claims were made for PMIDs 33914858, 33015737, 28469664, 21319221, 42334020, 24391468 as `vf-06`; the other claim attempts printed "ALSO" lines for other actors, which I did not act on.

## Part A. Decisive propositions

Depth key: FT = full text read as text (Methods, Results, legends), figures not viewed; AB = abstract only.

| Id | Verdict | Source and depth | What I found |
|---|---|---|---|
| P01 | SUPPORTED | 33914858 FT + supplement legends | S-KO (Synapsin-Cre) CC1 cells 2-fold lower, PDGFRa cells higher in corpus callosum, n = 3 v 3 mice (Fig 4 legend). Myelinated axons 3.5-4-fold fewer, g-ratio higher, n = 3 v 3 (Fig 5). N1 latency longer, slices 8 v 8 (Fig 5D legend). Intact WWOX is shown only in CC1 cells (Supp Fig 1D), not in OPCs. The word "mosaic" is not in the paper: it is an INFERENZA, and a fair one, because all conditional lines carry a Rosa26-tdTomato reporter yet no recombination efficiency is given in the text I read. |
| P02 | SUPPORTED, with one refinement | 33914858 FT; report lines L9, L19, L63-64, L142 | The report's Summary and Finding 1 ("decisive", "proximate origin non-cell-autonomous") are stronger than its Finding 7 and Limitations ("formally silent" on an intrinsic requirement): internal inconsistency confirmed. The report never mentions the Olig2-Cre or GFAP-Cre arms or the DRG co-culture. Refinement: the co-culture in the paper is a real test of non-cell-autonomy (wild-type OPCs on Wwox-null v wild-type DRG neurons, DRG cultures treated with fluorodeoxyuridine against non-neuronal cells, n = 4 v 4, two experiments). The authors call their own evidence "in vitro and in vivo" and still say they cannot exclude a cell-autonomous role. The producer's text should say that contact, substrate and soluble product are not separated (true), without implying the co-culture is weak support. Same origin as P01 (one paper), so it is not independent confirmation. |
| P03 | SUPPORTED | 33914858 FT + Supp Fig 1E/Fig 8 legends | Olig2-Cre (O-KO) exists; WWOX absence shown in CC1 cells at P18 (one field with arrowheads); "found no major changes" in MBP at P17 (Supp Fig 8: whole sagittal sections, cortex fields, no count and no n in the legend). The report's "Arm B has not been performed" and "untested" are therefore wrong in part. The producer should also record that O-KO and G-KO show no growth, weight or survival phenotype (Fig 1J-O, O-KO n = 10-11, log-rank P = 1.0), which is more than the MBP panel. EM, nodes, conduction in O-KO: not in the paper, so NON RISOLTO is right. |
| P04 | PARTLY | 21319221 AB only (full text behind subscription, no open route found); 42274605 FT; 33015737 FT | (a) Direction of the transfers is as stated. (b) "Postnatal wild-type mouse" is not in the 21319221 abstract: it says lateral-ventricle injection into postnatal mice plus ex vivo organotypic optic nerve of rodent, and MeSH lists "Mice, Transgenic". The optic-nerve result is ex vivo, not in vivo, so the report's "in vivo ... postnatal mouse brain and optic nerve" also blends two systems. (c) 42274605 section 3 does say "Continuous Wnt signaling reduces differentiation" (EV05 verified), but the same section says lithium inhibition of GSK-3beta "promotes oligodendrocyte differentiation" in experimental models; section 6 says patient lithium effects are mainly immunomodulatory. The producer cites only the unfavourable sentences of this review. Fix wording of (b) and add the favourable sentence. |
| P05 | SUPPORTED | 32000863 FT (Europe PMC XML) | Increased GSK3beta activation, shown as Ser9 dephosphorylation on westerns, in cerebellum, hippocampus, cortex at P20; lithium chloride suppresses PTZ-induced seizure (Fig 7c, 7d). Severe CNS hypomyelination is in the abstract. Lithium: no myelin readout in the text. The paper's own Discussion says whether lithium rescues migration and differentiation deficits "remains to be studied". Note: "WWOX restrains GSK-3beta" is mechanism wording; the paper shows a correlate (Ser9 loss in a germline knockout), not a restraint mechanism. Germline model, not neuron-specific. |
| P06 | SUPPORTED | 41980417 FT (grep-level, Europe PMC XML); 35372341 FT (PubMed tool) | 41980417: Pdk1 deleted in OPCs by inducible NG2-CreERT2; "did not exhibit spontaneous seizures or early lethality"; clemastine from P21 raised Olig2+, ASPA+ cells and MBP+ area (n = 3-5), synaptic and behaviour outcomes; no EM or conduction after treatment seen in the text I read. 35372341: wild-type mice, clemastine P5-P21, more CC1 cells, callosal N1 conduction velocity lower (P < 0.01, n = 10-12), fewer myelinated axons and nodes. The item is accurate. The Pdk1 defect is OPC-intrinsic, so the rescue is not a model of a neuron-driven defect. |
| P07 | SUPPORTED | 26725831 AB; 40246008 AB; 33914858 Methods | 40246008: thyroid hormones fell after S-ketamine (neonatal rat), T3 supplement replaced them. 26725831: adult mice, 12-week cuprizone, PDGFRa "not affected"; the report glosses this as "proliferation markers", which is a progenitor-identity marker. In 33914858 Methods the spheroid differentiation medium contains 40 ng/ml T3 and KO spheroids are still hypomyelinated at weeks 30 and 37 (Fig 7G-I); no T3-free arm. B27 content not checked by me; the "undetermined" status is a fair statement. 16112266 abstract read: a review of T3 and maturing oligodendrocytes; it is not data. I did not open `myelin_premises` media.tsv M01-M06. |
| P08 | SUPPORTED | 24391468 FT (Europe PMC XML) | Neuregulin gives NMDA-evoked currents about 6-fold larger in OPCs and differentiated oligodendrocytes (p = 0.02, 0.03). DRG cells from E14-E16 rats, OPCs from P0-P2 rats. MK-801 had no effect without neuregulin and cut myelination by 82% with it (to 25% of the no-neuregulin control); BDNF does the same (76%). The abstract sentence quoted by the report names neuregulin only; title and Fig 7G include BDNF. Small wording point: "removed" overstates "reduced by 82%". The authors say the NRG/NMDA mode "may dominate later in development" (tentative), whereas the report calls it "the adult configuration". Adult evidence is the lysolecithin/ethidium lesion in rat, n = 3 EM lesions. |
| P09 | SUPPORTED | 42334020 FT; 33914858 legends | Markers only (PDGFRa, BCAS1, PLP1, CC1); no sheath measure (the word "sheath" does not occur). Windows: naris occlusion P0 to P5, DREADD P0-1 to P8, slices from P4 with NBQX 48 h mimicking silencing. S-KO bursts recorded P13-P17 in vivo and in vitro (Fig 2 legend). Add to the item: the paper states S-KO seizures begin at P9, which is the nearest datum after the P0-P8 window. Absence of early-hyperactivity data stays an absence of evidence, not a negative. |
| P10 | SUPPORTED | 34634460 AB + FT (Europe PMC XML) | Methods: Synapsin I-Cre (JAX 003966) x Wwox flox, mice P13-P17, the same S-KO line as 33914858 (same authors). Bursts were also seen in heterozygotes. This answers the "Cre line and ages" gap in the item. Consequence: 33914858 and 34634460 are one mouse line, so the report's "(KB; PMID 34634460, 33914858)" pairs are not independent, and "same animals" (report L59) is not shown (recordings P13-P17, histology P17, different animals). |
| P11 | SUPPORTED | report text only | Report L64 gives no citation for the SDR statement; L146 gives none for the lithium narrow-therapeutic-index statement (perimeter: the whole report text and its PMID table). Diagram (L78) places "Loss of SDR/lipid scaffold function" under neuronal loss, while Finding 7 (L64) makes the lipid route oligodendrocyte-intrinsic. WWOX does contain an SDR domain as general knowledge, but the report's WWOX-to-PPARalpha route has no WWOX datum. |
| P12 | PARTLY | 34747138 FT (Europe PMC XML) | The inference is right and strong: AAV9-hSynI-WWOX in germline-null mice leaves OPCs Wwox-null, yet CC1 cells rise, MBP improves and EM improves, so neuron-restricted rescue is informative on cell of origin and "non-probative" overstates. But the DATO "treated arms unquantified" is not true of this paper: CC1 and PDGFRa counts (Fig 4C, n = 3 per arm) and EM myelinated-axon counts and g-ratio (Fig 5B, 5C, 5E, 5F, 5H, 5I) are quantified, with "minor differences" from wild type at P17 and 6 months (so "partly" is defensible). Only the MBP immunostaining panel (Fig 4A) is shown as images. In LEGEND the phrase "treated arms ... unquantified" comes from `woree_rescue_reference_scaffold.md` (PMID 42422765, a dose-dependent study), not from 34747138; the ranking text in `ranking_it8_p9_20261029/investigations.tsv` row INV-06 does not name its source. Figures not viewed by me. |
| P13 | SUPPORTED | 28469664 FT; 31808502 AB | Abstract: naringin "inhibited beta-catenin expression and GSK-3beta phosphorylation"; Results (Fig 6B, 6C): Ser9 phosphorylation and beta-catenin significantly increased, n = 7, westerns on 4-week injured adult rat spinal cord. No GSK-3beta inhibitor or genetic arm. Authors' own limit: no time course of remyelination. Glycyrrhizic acid abstract says it "modulat[es] GSK-3beta signaling pathways" with no direction or manipulation. Neither is proof of a GSK-3beta route. Side point: the Ser9 increase is the direction expected of GSK-3beta inhibition, so the Results are a correlate in favour, not against; the producer states this correctly as "an association". |
| P14 | SUPPORTED | 33015737 FT (Europe PMC XML, symbols preserved); Fig 7 not viewed | Foxg1 knockdown in rat OPC culture raised GSK-3beta mRNA and protein, lowered beta-catenin, and raised CNPase+ cells; SB216763 "reversed" beta-catenin and "decreased the proportion of CNPase" while raising EdU, NG2 and O4 shares. Discussion: "inhibition of GSK-3beta expression ... inhibits the differentiation of OPCs". So the inhibitor lowered differentiation, opposite to the report's use at L135 ("abolished by ... SB216763" as support). Foxg1 deletion in vivo is Nestin-CreER in NSPCs under cuprizone. The paper's Introduction and Discussion contradict each other on the sign of GSK-3beta in differentiation. |

Counts: SUPPORTED 12 (P01, P02, P03, P05, P06, P07, P08, P09, P10, P11, P13, P14); PARTLY 2 (P04, P12); NOT SUPPORTED 0; UNVERIFIABLE 0.

Extra care items you asked for:
1. Foxg1/SB216763 runs opposite to the report's use: confirmed (P14), at Results and Discussion level, with symbols preserved. Fig 7 panels not viewed.
2. 33914858 already holds Olig2-Cre and GFAP-Cre arms: confirmed (P03). Olig2-Cre: P17 MBP "no major changes" (qualitative) and no growth or survival phenotype. GFAP-Cre: no phenotype in Fig 1M-O.
3. 34634460 is a neuronal deletion model: confirmed (P10), and it is the same Synapsin-Cre line as 33914858.

## Part B. Coverage audit (first extraction)

I read the whole original report, then picked these 12 points, with all six Limitations caveats, ends of lists and compounds named in passing.

| # | Report anchor and point | Extraction row | Result |
|---|---|---|---|
| 1 | L140 neuron-to-OPC signal still unidentified (caveat) | E53 | PRESENT |
| 2 | L142 "Arm B of the proposed design has not been performed" (caveat) | E47 (anchor L142), E37 | PRESENT_NARROWED: E47 text says "untested" and "silent" but does not carry the sentence about Arm B not performed, which is the sentence P03 contradicts. Add it to E47. |
| 3 | L144 no direct test of a GSK-3beta inhibitor on the WWOX myelin phenotype (caveat) | E19 | PRESENT |
| 4 | L146 lithium pleiotropic, narrow therapeutic index (caveat) | E18 | PRESENT |
| 5 | L148 stage specificity under-controlled (caveat) | E54 | PRESENT |
| 6 | L150 55+ dismech disorders, comparison not completed (caveat) | E55 | PRESENT |
| 7 | L13 end of inhibitor list: ARA-014418, indirubin, L803-mt | E16 | PRESENT |
| 8 | L135 end of the supporting list: BSYS-exosome, miR-15b/Wnt/beta-catenin, 39733800 | E58 | PRESENT |
| 9 | L135 SB216763 named in passing | E56 | PRESENT |
| 10 | L27 side sentence "remyelination after white-matter damage is NMDA-receptor-dependent" | E22 | PRESENT |
| 11 | L6 header disease identifier "MONDO:0014533" | none (E65 covers only the question restatement and UI residue) | MISSING. I checked the ontology service: MONDO:0014533 is "developmental and epileptic encephalopathy, 28", synonym WOREE syndrome, so the identifier is correct. Low weight, but the extraction has no row for it. |
| 12 | L48 sheath readout "g-ratio; MBP+ internode length on EM" | E38 | PRESENT, with a carried defect: MBP immunolabel is not an EM measure (internode length by MBP and Caspr is immunofluorescence, as in 35372341). E38 repeats the report wording without a flag. |

Result: 11 of 12 present (10 PRESENT, 1 PRESENT_NARROWED), 1 MISSING (point 11).

Extension scan after the MISSING: I scanned the remaining report lines for the same kind of content (identifiers, ontology codes, header metadata, numerals). All 18 PMIDs in the report are in the extraction (E01, E05-E10, E12, E21, E26-E27, E29-E31, E35, E42-E43, E56-E58); GO ids in E34; "6-fold" in E21; "55+" in E55; "FDA-approved" in E25. No further misses. Smaller observations that are not misses: E29 silently relabels the report's "OPC proliferation markers" as "progenitor markers" (the relabel is recorded only in `reconcile.tsv` row E29, not in `extraction.tsv`), and E50-E52 do not carry the diagram's separate "[missing +cue]" tag; both are present in substance.

## Part C. Reconciliation sample (8 rows of `reconcile.tsv`)

Classes of the file: new_to_legend 4 rows (E09, E17, E36, E63), already_present_and_used many, present_not_used 3 (E49, E55, E61), superseded_or_contradicted 5. Minimum counts were available for every class, so no class was short.

| Row | Class | Pointer check | Result |
|---|---|---|---|
| E09 | new_to_legend | `evidence.tsv` EV08 and receipt FTR-20261108-31808502-34 exist; EV08 quote verbatim; `git grep` for 31808502 outside this package returns nothing | OK |
| E36 | new_to_legend | "none for the argument"; `git grep` of "non-probative", "positive control only", "cell of origin" in the three myelin packages returns nothing | OK for that perimeter. Content note: the INFERENZA is correct (see P12) but the row calls the vector "mosaic and partial" with no source; 34747138 text I read says only that it targets Synapsin-positive neurons. |
| E63 | new_to_legend | `dismech_it34_20261107/README.md` exists and is a single-entry comparison | OK. Note E55 points to the same README but is labelled present_not_used; the README does not contain "55+", so E55 is only "DisMech was used before", which is how the row words it. Acceptable. |
| E04 | already_present_and_used | `ranking_it8_p9_20261029/investigations.tsv` row INV-06 contains the question "Is there an axonal signal left for a pro-myelinating agent to act on"; `NEED-MYELINATION` exists in `batch_sci_20261105/BRIEF_A1.md` and `BRIEF_B1.md` | OK |
| E12 | already_present_and_used | `myelin_inv06_20261107/output/evidence.tsv` E19-E22 exist, abstract_only, as the row says; receipt FTR-20261107-21319221-95 exists | OK |
| E49 | present_not_used | `investigations.tsv` INV-06 text lists "lipid-synthesis" among intrinsic routes; no WWOX SDR datum anywhere | OK |
| E55 | present_not_used | see E63 | OK, weak pointer |
| E56 | superseded_or_contradicted | `myelin_inv06` evidence E13-E15 exist and match my reading of 33015737 (SB216763 lowered the CNPase share) | OK |

prior_brief_fate checked for 4 rows against `myelin_inv06_20261107/BRIEF.md` (found with `git grep -l "INV-06" -- disease-models`):
1. E04 "kept": brief says "Do not require WWOX restoration as the only possible solution" - matches.
2. E12 "modified": brief item 2 separates proliferation, survival, differentiation, and the Wnt, CREB, Notch arms - matches.
3. E56 "modified": brief item 2 says the Foxg1 paper "must not count automatically as confirmation of GSK3 inhibition" - matches.
4. E49 "omitted": the brief has zero hits for SDR, dehydrogenase, PPAR, lipid - matches. (E36 "omitted" also matches: no AAV or gene-therapy text in the brief. E44 quote on "adult"/"neonatal" labelling also matches.)

One reconcile row needs correction: E35 (not in my 8). It says the report states the rescue "without the 'partial, unquantified' limit". As shown in P12, "unquantified" is not true of 34747138.

## Part D. Evidence sample (`evidence.tsv`, all 15 rows)

All 15 quotes are verbatim in the source. Section stated for EV05 (section 3) and EV07 (section 6) of 42274605 verified from the section headings. EV01, EV02 (28469664 abstract versus Results Fig 6), EV06, EV08-EV15 verified against abstracts or text I read. EV13 is the neuronal Wwox-deletion abstract sentence (34634460). EV14, EV15 are in the 32000863 abstract and I also found them in the full text.

Do they carry the propositions? Yes for P04, P05, P07, P10, P13. Two defects:
1. EV05 and EV07 are both counter-quotes from the review; the same section 3 has the sentence "pharmacological inhibition of GSK-3beta by lithium ... promotes oligodendrocyte differentiation" and no EV row records it. The set is one-sided for a review that is mixed.
2. No `evidence.tsv` row backs P01, P02, P03, P06, P08, P09, P12 or P14; they rest on rows of the earlier package (checked above, they match) or on nothing. P12 has no row at all, and its DATO is partly wrong.

## Corrections the producer must make

1. `verify/items.md` P12 and `decisive.tsv` P12: replace "with the treated arms unquantified in the module's reading" by: "CC1/PDGFRa counts (Fig 4C) and EM myelinated-axon counts and g-ratio (Fig 5) are quantified, n = 3 per arm, with minor differences from wild type; the MBP immunostaining panel is shown as images". Keep the INFERENZA.
2. `reconcile.tsv` row E35, column `note`: drop "without the 'partial, unquantified' limit"; the unquantified-arm phrase belongs to PMID 42422765 (`woree_rescue_reference_scaffold.md`), and `evidence.tsv` needs a new row for the 34747138 Fig 4C / Fig 5 quotes.
3. P04 wording in `decisive.tsv` and `items.md`: remove "wild-type" for 21319221 (abstract does not say it; MeSH lists transgenic mice), say that the optic-nerve arm is ex vivo organotypic, and add the favourable review sentence ("lithium ... promotes oligodendrocyte differentiation", section 3) with a new `evidence.tsv` row.
4. `extraction.tsv` E47: add the report sentence "Arm B of the proposed design has not been performed" (L142).
5. `extraction.tsv`: add a row for the header identifier MONDO:0014533 (L6) or widen E65.
6. `extraction.tsv` E38: add a note that "MBP+ internode length on EM" is not an EM measure.
7. P03 and P01 notes: record that O-KO and G-KO show no growth, weight or survival phenotype (Fig 1J-O), and that N-KO (Nestin-Cre) reproduces the S-KO hypomyelination (Supp Fig 5D-H). Say that "mosaic" is an inference (no recombination efficiency in the main text), not a statement of the paper.
8. P09 note: add the paper's own S-KO seizure onset at P9.
9. P10 / `reconcile.tsv` E23, E43: state that 34634460 and 33914858 use the same Synapsin-Cre S-KO line, so they are one origin; "same animals" at report L59 is unsupported.
10. P08: replace "removed" by "reduced by 82% (to 25% of the no-neuregulin control)" and note that the authors call the NRG/NMDA mode possibly later in development, not "adult".
11. Add evidence rows for P01, P02, P03, P06, P08, P09, P14 or point each to the earlier-package row (`myelin_inv06_20261107/output/evidence.tsv` E01-E02, E08-E10, E13-E15, E30-E33, E25-E28, E39-E40).

## Open uncertainties

1. 21319221 (the report's "strongest single piece") was reached only at abstract level; no open full text found. Whether GSK-3beta effects there are on oligodendrocytes or on aggregate brain measures is not decided by me.
2. No figure image was viewed for any source; panel-level claims (Supp Fig 1C-F, Fig 7 of 33015737, Fig 4 and 5 of 34747138, Fig 6 of 28469664) rest on legends and Results text.
3. Whether Synapsin-Cre is mosaic in OPCs: not shown in the main text of 33914858; the reporter allele exists, so the question is answerable from the authors' material but not from what I read.
4. 41980417 was read by keyword search on the XML, not end to end; the conduction and EM statements are "not found in the text I read", with that perimeter.
5. `myelin_premises` media.tsv M01-M06 and the receipts' internal content were not opened; B27 T3 content not checked.
6. The ranking text's "the treated arms of the source are unquantified" has an unnamed source; I located the phrase in a different paper's scaffold but did not read 42422765 itself.
