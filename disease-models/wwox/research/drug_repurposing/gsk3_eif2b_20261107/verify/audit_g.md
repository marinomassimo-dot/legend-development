# Package G (WWOX, GSK3 beta, eIF2B): independent blind audit

Role: independent blind verifier. Date 2026-11-07. Not medical advice. Blind: nothing under
`gsk3_eif2b_20261107/` (other than this file) and none of the IT15/IT28/WO-06 READMEs was opened. Input was
the items file only. No agents were started; no account, e-mail address or access challenge was involved.

Sources reached and depth, per PMID:

| Source | Route | Depth I reached |
|---|---|---|
| 32000863 | held full text `files/fulltext/PMID32000863_Cheng2020_PMC.xml`, manifest `deepdive_manifests/PMID32000863.json`, held Figure 7 PNG (looked at it myself) | quote search in the XML; manifest entries; Fig 7 panels a-d viewed |
| 15126504 | PubMed tool (abstract). Not in PMC (Europe PMC `inEPMC=N`) | abstract only |
| 12133000 | PubMed tool abstract. PMC1222905 exists, but Europe PMC `fullTextXML` returned HTTP 500 and the NCBI efetch XML says "The publisher of this article does not allow downloading of the full text in XML form" (the PubMed full-text tool returned an empty body). I stopped there and tried no other route | abstract only |
| 15001529 | PubMed tool abstract (not in PMC) | abstract only |
| 26974342 | Europe PMC `fullTextXML` (PMC4805534), converted to text and searched | Results on eIF2B epsilon, Fig 5 and Fig 7 legends, Fig 5 supplements, Methods (OPP, rapamycin), Discussion paragraph; reviewer-response section skimmed. No figure images |
| 33220178 | Europe PMC `fullTextXML` (PMC7837216) | abstract, Fig 1 and Fig 6 Results and legends, Discussion; no cryo-EM or binding methods |
| 29489452 | Europe PMC `fullTextXML` (PMC5829914) | abstract, Results on VWMD mutants, SEC, GEF, pocket mutants, cell lines, Discussion; no figure images |
| UniProt | open REST JSON (reviewed entries Q64350, Q13144, Q8CHW4, P47823, P49841, P49840, Q9WV60, P18266; TrEMBL A0A9J7FZF5) | feature tables plus my own sequence windows and a Needleman-Wunsch alignment (match 2, mismatch -1, gap -2, no end-gap correction) |

## 1. Evidence rows

Counts (rows asked for): 20 decisive + 3 sampled plain = 23. SUPPORTED 22, OVERSHOOT 1 (E02), UNDERSHOOT 0,
NOT_IN_SOURCE 0, UNVERIFIABLE 0. Rows E19, E23, E24, E27, E28 were not asked; I looked at them in passing (below) and all
stand. Rows not asked and not checked beyond that: none other (the file contains only E01-E28).

"Depth" is what I reached, not what the producer claimed.

| id | verdict | what I checked | depth | reason |
|---|---|---|---|---|
| E01 | SUPPORTED | Quote string in the held XML (Fig 7 caption, panel c) and in the manifest. Figure 7c PNG: pGSK3b(Ser9) 2.7/3.1/1.3 (cerebellum), 3.6/3.5/2.0 (hippocampus), 3.9/3.8/2.5 (cortex) for +/+, +/-, -/-; total GSK3b 2.2/2.4/2.4, 2.3/2.4/2.6, 2.2/2.4/2.6 | held full text + image | Quote present. Finding says no more than the panel: Ser9 phospho falls in -/- in all three regions, total flat. One lane per genotype per region, no error bars, no n, no marker on panel c (the stated limits are right). The finding keeps "by this proxy". See section 5 (P20 is after seizure onset) for a confound the row does not carry. |
| E02 | OVERSHOOT | Same figure and same manifest entry. The producer's quote ("In every region the +/- value sits at or above the +/+ value on the phospho blot") is in the manifest. Its own numbers contradict it: cerebellum 3.1 vs 2.7 (above), hippocampus 3.5 vs 3.6 (below), cortex 3.8 vs 3.9 (below). I read the same figures off the PNG | held full text + image | The quoted sentence is false in 2 of 3 regions (by 0.1 densitometry unit, which is within any plausible lane noise). The finding itself, "the heterozygote is not intermediate", is supported: the +/- values sit near +/+ (a midpoint would be 2.0, 2.8, 3.2) and far from -/-. Repair: say "the +/- value is within 0.1 of the +/+ value in hippocampus and cortex and 0.4 above it in cerebellum; none is intermediate". Do not carry the sentence as written (it is also the product of a previous manifest correction that fixed two transcription errors in the other direction, so the sentence deserves one more look in the manifest). |
| E03 | SUPPORTED | Figure 7d image: three panels, each with a "****" bracket between PTZ and PTZ+LiCl (N 12/8, 12/12, 6/7). Caption and Results text name only the -/- panel (XML text) | held full text + image | Quote true of the figure. Two limits the finding could add: (a) the effect in the null is visibly larger in magnitude (peak stage about 3.5 vs about 1.2 in +/+), and the paper's only test is one-way ANOVA with no genotype-by-drug term (manifest Methods entry), so "not shown to be Wwox-specific" is the safe wording, "is not a Wwox-specific rescue" is slightly stronger; (b) the wild-type response is near floor. Neither changes the verdict. |
| E04 | SUPPORTED | Abstract text via PubMed tool | abstract | The quoted phrase is in the abstract. The abstract also says phospho-GSK-3b co-binds phospho-Tau and that GSK-3b phosphorylation is raised in AD hippocampi, but never names Ser9 or Tyr216. The finding states exactly that limit. If the residue turns out to be Ser9, knock-down raises the inhibitory mark, which would point the opposite way from E01 (Wwox null lowers Ser9); that conflict is a live possibility, not a resolved one. |
| E05 | SUPPORTED | Abstract of 12133000 | abstract | Quote is in the abstract; CHO cells; LiCl, SB-415286, SB-216763 produced Ser535 dephosphorylation. Extent, antibody and method not stated, as the row says. |
| E06 | SUPPORTED | Same abstract | abstract | "did not elicit significant activation of eIF2B ... additional inputs are required" is in the abstract. The abstract does not say which eIF2B assay was used, how large the (non-significant) change was, or whether Ser535 dephosphorylation was complete. The title frames the question as insulin activation ("insufficient for the activation of eIF2B by insulin"). The finding makes no claim beyond the abstract. |
| E07 | SUPPORTED | Same abstract | abstract | Quote present word for word. It does not say whether protein synthesis went up or down; the finding does not say either. |
| E08 | SUPPORTED (sample) | Same abstract | abstract | Quote present; it is a background sentence, as stated. |
| E09 | SUPPORTED | Abstract of 15001529 | abstract | Quote present. Mild wording point: "when GSK3 beta was inhibited" is the authors' description of LiCl and isoproterenol as "a treatment known to inhibit GSK-3beta"; no GSK3b-specific manipulation is reported for the pS535 blot in the abstract (overexpression is used only for the kinase-activity read-out). The rat in-vivo hypertrophy model is in the abstract. |
| E10 | SUPPORTED | Same abstract | abstract | Quote present; substrate is GST-eIF2Bepsilon (recombinant); LiCl or ISO decreased it. |
| E11 | SUPPORTED (sample) | Same abstract | abstract | Quote present; S535A +107 percent vs ISO +95 percent in cell size. Cell size, not eIF2B activity (the abstract's closing sentence about "protein synthesis" is an interpretation, not a measurement in the abstract). |
| E12 | SUPPORTED | Same abstract | abstract | Quote present word for word. |
| E13 | SUPPORTED | Results paragraph and Fig 5A-B legend in PMC4805534 | partial full text | Quote present. Immunofluorescence on retinal sections, n=5 per group, two-way ANOVA, with or without nerve crush. Conditional AAV-Cre deletion in adult Gsk3b-floxed mice. Methods text on the antibody was not located in the sections I read (not a defect in the row). |
| E14 | SUPPORTED | Same paragraph and Fig 5 supplement 2 legend | partial full text | Quote present. Caveat the row only half carries: the alpha comparison is a germline Gsk3a knockout (n=5), whereas beta is an acute adult AAV-Cre deletion; a null result from a developmental knockout with n=5 is weak evidence of "alpha does not act". The authors themselves word it "suggesting that GSK3alpha may not regulate eIF2Bepsilon activity in RGCs". |
| E15 | SUPPORTED | Same paragraph, Fig 5E-F legend, Methods (OPP) | partial full text | Quote present word for word. OPP is a puromycin-analogue labelling assay (Methods), not an exchange assay; E572A is described as a dominant-negative mutant lacking catalytic activity. The text I read does not say whether the OPP experiment was done after crush (the row's "stage" says "after nerve crush"). Only the claim "translation gain depended on eIF2B catalytic function in this system" is made, and the text supports it. |
| E16 | SUPPORTED | Results paragraph, Fig 7A-B legend | partial full text | Quote present. The paper calls S535A "a constitutively active mutant" with a citation (Pap and Cooper 2002); the activity is not measured in this paper. n=5, Student t test. |
| E17 | SUPPORTED | Same paragraph | partial full text | Quote present word for word; survival assessed 2 weeks after crush. |
| E18 | SUPPORTED (sample) | Results paragraph, Fig 5 supplement 1 | partial full text | Quote present. The supplement shows P7, P21 and P60 (one-way ANOVA against P7), "adult" in the text; the row lists "P7, 21, 60 and adult", a trivial over-listing. The authors read the higher adult pS535 as "elF2Bepsilon-controlled translation is maintained at a low basal level in adult RGCs", which is an inference, not a measurement. |
| E20 | SUPPORTED | Abstract of PMC7837216 | partial full text | Quote present (abstract). Finding is in line with the abstract and with the Fig 1 and Fig 6 Results. |
| E21 | SUPPORTED, with a use warning | Results ("ISRIB only minimally accelerated ... in an assay devoid of eIF2(alphaP)", citing Tsai 2018) | partial full text | Quote present. The assay uses wild-type recombinant human eIF2B and non-phosphorylatable eIF2(alphaS51A) as substrate, so no eIF2B defect is present at all. The finding's last clause ("an eIF2B defect that is not phospho-eIF2 inhibition is not shown to be corrected") is true only as "not tested". It must not be used as evidence that ISRIB would fail on a defective eIF2B: E25 (and this paper's own Discussion, "stabilization ... may therefore contribute to the salubrious role of ISRIB ... in ... mutations in eIF2B that lower its enzymatic activity by destabilizing the decamer") point the other way for stability lesions. |
| E22 | SUPPORTED | Fig 6 legend and Results | partial full text | Quote present. System is Eif2S1 S51A mutant CHO cells with CRISPR disruption of eIF2B beta, delta or epsilon genes (also, in panel C, eIF2alpha itself). The row's "CHO cells lacking phosphorylatable eIF2 alpha, eIF2B subunits depleted" is right. Panel C is n=2 (stated in legend). |
| E25 | SUPPORTED, with an omission | Abstract; Results (SEC, GEF, HEK293T lines); Discussion | partial full text | Quote present. Epsilon mutants epsilon-R113H and epsilon-R195H were destabilised (R10/4 4.6 and 4.0 vs 5.2) and ISRIB raised R10/4 for every construct; ISRIB-rescued GEF activity of every mutant except alpha-V183F exceeded basal wild-type activity (and ISRIB also stimulates wild-type about 2-fold, so "restored to wild-type levels" is a statement about basal wild-type). Omission that matters to H4: all VWMD GEF assays in this paper "included a small fraction of unlabeled phospho-eIF2 (5 nM ...) to increase the dynamic range of the response to ISRIB" (Results). The rescue was therefore measured with a little phospho-eIF2 present, and the cell read-outs (ATF4, reporter, protein synthesis) used tunicamycin or thapsigargin stress, i.e. phospho-eIF2-driven. E25 shows rescue of stability lesions, not phospho-eIF2-free rescue. The epsilon lesions are R113H and R195H, none near Ser535 (the GSK3 site lies in the C-terminal region). |
| E26 | SUPPORTED, with a wording point | Fig 3 legend and Results | partial full text | Quote present word for word. The two mutants are delta-L179F (from the Sekine 2015 ISRIB-resistant screen, with wild-type GEF activity) and the designed delta-L487W (25 percent of wild-type activity). Only delta-L487W (and the delta-L179F plus alpha-V183F combination) is a lesion that is not rescued; delta-L179F has no defect to rescue. "Mutants in or near the ISRIB pocket" is the producer's gloss on "ISRIB-resistant mutants ... cavity-facing residue"; supported by the Results text. |

Not asked, seen in passing: E19 (quote and sense present in the Fig 7 supplement text), E23 (sentence present in the
Discussion of 33220178: "such as regulation of eIF2B by subunit phosphorylation (Wang et al., 2001)", reads as speculation),
E24 ("eIF2(alphaP) and ISRIB are incompatible ligands of eIF2B" present in the Discussion; the cryo-EM section itself not read), E27
(sentence present in the Discussion of 29489452), E28 (UniProt features: see section 3). No problem found.

## 2. Chain items

| id | judgement |
|---|---|
| CH01 | Label "measured (weak)" is right and no stronger than the evidence. Two additions: (a) the sentence in E02 must be corrected before it supports the "heterozygote not intermediate" remark (section 1, E02); (b) the break list omits that P20 is after spontaneous seizures start (after postnatal day 12 per the manifest) in a brain with malformations, hypomyelination and a roughly five-fold apoptosis excess (manifest entries). Ser9 dephosphorylation in bulk lysate at P20 could be secondary (seizure activity, cell composition, neuronal loss). The row says "cell type unknown" but not "timing relative to seizures". |
| CH02 | "unresolved" is right. The abstract supports nothing more. If the residue is Ser9 the direction may oppose CH01 (see E04). |
| CH03 | Carried from the module; I did not check it (nothing in my sources covers SH-SY5Y or the Tau docking mechanism). Not assessed. |
| CH04 | Right on class and label. Evidence E05 and E08 do what the link says. Species note: the number 535 is the rat numbering used for CHO (hamster entry A0A9J7FZF5 also has Ser535). |
| CH05 | Right. Rat cardiomyocytes; abstract level; the isoproterenol arm is not GSK3-specific (stated). Not neurons. |
| CH06 | Right. The one wording point: "GSK3 alpha no" is a germline-knockout negative at n=5 (E14), not a demonstrated absence of alpha action. |
| CH07 | Label "measured ... counter" is right. The row lists E06 and E07 only; it could also cite the abstract's own framing (insulin activation insufficient), which is the central counter to "site removal activates eIF2B". In 11500362 (abstract seen in passing) the C-terminal casein kinase 2 sites (Ser712/713) are said to be required for eIF2 binding and activity in vitro, which is one concrete example of the "additional inputs" the authors point to. |
| CH08 | Right: protein-synthesis labelling only. E19 is listed in the ids but is an axon-regeneration/rapamycin row, not an OPP row; harmless, but the "readout performed" line then covers only E15 and E16. |
| CH09 | "unresolved" is right. In the one paper I read in full (26974342) phospho-eIF2alpha, eIF2alpha and Ser51 are not mentioned (text search), so no source in this package measured it next to the GSK3 site. Lead I saw but did not read: a 2020 review titled on GSK-3 and the eIF2alpha kinase PKR (Europe PMC id 32512016). If GSK3 interacts with an eIF2alpha kinase, a GSK3 manipulation could move phospho-eIF2alpha too, so independence cannot be assumed either way. |
| CH10 | Right. The "no translation or eIF2B measurement in any WWOX model" statement matches my own two-route search (section 4, H1), with one near-miss to carry (Atf4 in a Drosophila Wwox knockdown). |
| CH11 | Right: E03 as read. |
| CH12 | Right on class and label. It lists E21 and E22 as limits; add that E25's rescue assay contained 5 nM phospho-eIF2. |
| CH13 | Right. |

## 3. Residue items (UniProt, 2026-11-07, own windows and alignment)

| id | result |
|---|---|
| RS01 | Correct. Q64350, 716 aa, reviewed, Ser535, window EELDS(535)RAGS(539)PQLDD. UniProt evidence for Ser535 is a combined mass-spectrometry record (PubMed 22673903). Hamster A0A9J7FZF5 (716 aa, TrEMBL) also has Ser535. |
| RS02 | Number and window correct (Q13144, 721 aa, Ser540, EPDS(540)RGGS(544)PQMDD). Two errors/omissions. (a) Wrong offset: the human/rodent difference is at the +2 residue (human Gly542, rat/mouse Ala at +2), not +3; at +3 human and rodents are both Gly. The hamster Val IS at +3 (RS05 says so correctly). So the sentence in RS02 mixes two offsets. (b) The human Ser540 phosphoserine is annotated only "by similarity" to rat Q64350 (ECO:0000250); human Ser544 carries mass-spectrometry records. The row says "phosphoserine (UniProt)" without that qualifier. My 32-residue window (-12 to +19 around the serine) gives 25 of 32 identical for human vs mouse and vs rat (the row says 24 of 32; the window definition is not stated, so not an error as such). |
| RS03 | Correct. Q8CHW4, 717 aa, Ser536, EELDS(536)RAGS(540)PQLDD, phosphoserine by similarity to rat. Mouse numbering is one higher than rat. Mouse vs rat window 31 of 32 identical (my window). 26974342 uses "Ser535" for mouse neurons (rat-based plasmid from the Cooper lab); the mutation label is the cited-literature convention, not the mouse UniProt number. |
| RS04 | Correct. P47823, 721 aa, reviewed, Ser540, EELDS(540)RAGS(544)PQLDD. UniProt rabbit Ser540 is also "by similarity". |
| RS05 | Correct. A0A9J7FZF5, 716 aa, TrEMBL, Ser535, EELDS(535)RAVS(539)PQLDD, +3 residue Val. |
| RS06 | Correct as sequence. UniProt marks Ser539 (rat), Ser540 (mouse), Ser544 (human, rabbit) "Phosphoserine; by DYRK2". For rat the DYRK2 evidence is experimental (ECO:0000269, PubMed 11311121). The abstract of 11311121 (title and abstract read via Europe PMC) states Ser539 phosphorylation by DYRK2 and DYRK1A and the +4 requirement of GSK3 for a prior phosphoserine, with "potential role for DYRK as a GSK3-priming kinase". So the priming reading has abstract-level literature support; it is not a measurement in this package, and the row labels it an inference, which is right. In the same literature (abstract of 11500362) GSK3 phosphorylation of Ser535 "requires both ... Ser539 and a distal region" which recruits GSK3. |
| RS07 | Correct. UniProt Q13144: W2 domain 543-720, Disordered region 523-547. Prediction, as stated. |
| RS08 | Human vs mouse 637/721 identical (agrees), mouse vs rat 673 (agrees), human vs rat 637 (the row says 638; one-residue tie-break difference, immaterial). |
| RS09 | Correct. P49841, 420 aa; Ser9 in MSGRPRTTS(9)FAESC; UniProt: "Phosphoserine; by PKB/AKT1, RPS6KA3, SGK3 and NME7". Mouse Q9WV60 and rat P18266 are 420 aa with Ser9 in an identical window; identity to human 416 and 415 of 420 (agrees). |
| RS10 | Correct. P49840, 483 aa; Ser21 in RARTSS(21)FAE; UniProt evidence for Ser21 is by similarity (Q2NL51). The N-terminal extension is 483 - 420 = 63 residues (the alignment shape is consistent). |
| RS11 | Correct. Tyr216 (beta) and Tyr279 (alpha), identical window EPNVSYICSRYY. |
| RS12 | Kinase-domain figure reproduced: 260 of 285 (about 91 percent) over the UniProt domain boundaries. Tails: I get 34 identical of 80 aligned (43 percent), the row has 37 of 76 ("about half"); a boundary difference, not an error. The commonly quoted higher kinase-core identity was not re-derived. IT15 isoform-ratio statement not checked (blind). |
| RS13 | Correct against E13 and E14 (see section 1 for the E14 caveat). |

## 4. H1 and H2 (absence claims), H3 and H4 (attribution)

### H1 (absence): no WWOX-deficient study measures translation, eIF2B activity or eIF2B subunit phosphorylation

I confirm the narrow claim on two routes and add near-misses the statement should name.

Route A, PubMed tool (strings run; result counts in brackets):
`WWOX AND eIF2B` [0]; `WWOX AND "integrated stress response"` [0];
`WWOX AND ("eukaryotic initiation factor" OR eIF2alpha OR eIF2A OR "eIF2B" OR "initiation factor 2")` [1: PMID 25502636];
`(WWOX OR WOX1 OR "WW domain-containing oxidoreductase") AND (puromycin OR polysome OR "ribosome profiling" OR "global protein synthesis" OR "mRNA translation")` [0];
`(WWOX OR WOX1) AND (ISRIB OR ATF4 OR "unfolded protein response" OR PERK OR "phospho-eIF2")` [3: PMIDs 42909904, 31752354, 28749468];
`WWOX AND ("vanishing white matter" OR EIF2B5 OR "leukodystrophy")` [0];
`(WWOX OR Wwox) AND (GSK3 OR "GSK-3" OR "glycogen synthase kinase")` [5: 36572560, 34058790, 32000863, 22193544, 15126504; the last two are E01 and E04; the others I did not open];
`(WWOX OR WOX1) AND (translation OR "protein synthesis" OR "eIF2")` [100, all noise: "translation" is expanded to translational/translator/translate].

What the PubMed tool does with OR and parentheses: it keeps the Boolean structure and the parentheses (the returned `query_translation` shows each OR group intact) and runs automatic term mapping inside each term. Consequences: (i) a generic word such as "translation" is expanded to translational/translator and floods the result, so only unambiguous strings are usable; (ii) a quoted phrase that is not in the phrase index (I saw "eIF2B epsilon phosphorylation") is split into a conjunction of its words (eIF2B epsilon AND phosphoryl*), which silently broadens a query; (iii) "WWOX" is mapped to a supplementary concept OR all-fields; (iv) no wildcard allowed. An empty result on a short unambiguous string is therefore meaningful; a large result on an ambiguous OR group is not.

Route B, Europe PMC REST (full-text indexed):
`(WWOX OR WOX1) AND eIF2B` [4: 35794133 antibody cross-reactivity paper, 25688261 GSK3b CNS review, 26347199 ursolic acid, a conference abstract book; none is a WWOX-deficiency measurement as far as the titles go];
`(WWOX OR WOX1) AND ("eIF2B" OR "eIF2alpha" OR "eIF2α" OR "ISRIB")` [33; first two are the Drosophila Wwox paper and its preprint, the rest reviews and unrelated cancer papers];
a title/abstract string with WWOX and eIF2/eIF2B/translation initiation/protein synthesis/integrated stress [4, none on point];
a broad full-text string [308, noise].

Near-misses to carry in the absence statement (I read the abstracts and, for the first, searched the full text):
1. PMID 42909904 (Brain Commun 2026, Drosophila; preprint PPR1015434): neuronal Wwox knockdown in an amyloid-beta model raised Atf4 (immunostaining, brains of day-14 flies) and the authors infer the PERK-Atf4 branch of the ISR/UPR ("these data suggest ...", with Xbp1 splicing unchanged). I searched the full text: no eIF2, eIF2B, puromycin, ISRIB or GSK terms. It is an ISR-adjacent output in a WWOX-deficient neural system, at protein level for Atf4, in a different species, and is not a translation, eIF2B or eIF2B-phosphorylation measurement. The absence claim stands; the statement should name this paper as the closest thing and say what it is not.
2. PMID 25502636: WWOX over-expression reduced phosphorylation of eIF-4E and ATF2 through p38 in cholangiocarcinoma cells; eIF4E, not eIF2B, over-expression, non-neural.
3. PMID 28749468: WWOX modulates the ER-stress response (PERK and IRE1 activation by paclitaxel) in ovarian cancer cells; ER stress, not eIF2B.
These do not refute H1's absence claim. The claim is limited to what two routes and the strings above returned: it is "not found", not "does not exist".

### H2 (absence): no primary source tests ISRIB or another eIF2B activator on a lesion caused by phosphorylation at the GSK3 site

Confirmed on two routes, with the same limit ("not found").
PubMed tool: `ISRIB AND (GSK3 OR "glycogen synthase kinase")` [0]; `(Ser535 OR S535) AND (eIF2B OR eIF2Bepsilon) AND (GSK3 OR "glycogen synthase kinase 3")` [7: 24023715, 15001529, 12133000, 11500362, 11311121, 10913625, 10216953; I checked titles/abstracts of 24023715, 11500362, 11311121 via Europe PMC: DYRK2 and cardiac S535A transgenic work and a 2001 multi-site paper; all pre- or non-ISRIB, none tests an eIF2B activator]; `(ISRIB OR 2BAct OR "eIF2B activator") AND (Ser535 OR S535 OR "eIF2Bepsilon phosphorylation" OR "eIF2B epsilon phosphorylation")` [22, noise from the phrase being split, see above; contains 33220178 and VWMD papers, none about the GSK3 site].
Europe PMC: `ISRIB AND (GSK3 OR GSK-3 OR "glycogen synthase kinase")` [177, full-text noise, titles are ISR/cancer papers and reviews]; `(ISRIB OR 2BAct OR "eIF2B activator" OR "eIF2B agonist") AND (Ser535 OR S535 OR "Ser-535" OR "Ser(535)")` [2, both reviews: 35579296 on eIF2B in neurological and metabolic disorders, 40869184 on translational control in cardiac pathophysiology]; `(ISRIB OR 2BAct) AND (lithium OR "SB-216763" OR CHIR99021 OR "GSK3 inhibitor") AND (eIF2B OR "eIF2B epsilon")` [23, titles are ISR reviews and unrelated, none on point].
I did not open the two reviews. If either states an ISRIB result on a Ser535 lesion it would be secondary; the primary would then need finding. Not found by me.

### H3 (decisive negative-result statement, PMID 12133000)

What the abstract states (verbatim sentence): "However, these compounds did not elicit significant activation of eIF2B, indicating, consistent with conclusions from one of our previous studies, that additional inputs are required for the activation of eIF2B." Preceded by: LiCl, SB-415286 and SB-216763 "brought about the dephosphorylation of Ser(535), which strongly indicates that this site is indeed a target for GSK3 in vivo". The title reads "Evidence that the dephosphorylation of Ser(535) ... is insufficient for the activation of eIF2B by insulin".
Not stated in the abstract (full text blocked, not worked around): which eIF2B assay; the size of the non-significant change; how many replicates; whether dephosphorylation was complete or matched insulin's; whether all three compounds were tested in the activity assay; the time points; which "additional inputs". The producer's H3 sentence ("dephosphorylation ... by GSK3 inhibition was not sufficient to activate eIF2B significantly") is a fair paraphrase of the title and abstract and says no more. Do not strengthen it to "the site is irrelevant to activity": a non-significant result in one hamster cell line with non-specific compounds (the abstract's own caution) shows insufficiency, not irrelevance.

### H4 (attribution, PMID 26974342)

Source: Guo X et al. 2016 (eLife; PMC4805534), mouse retinal ganglion cells. Clause by clause: (i) Gsk3b deletion lowers phospho-eIF2Bepsilon Ser535: yes (Fig 5A-B, markedly reduced, with and without injury, n=5). (ii) Gsk3a deletion does not: yes, "did not change", germline knockout, n=5 (Fig 5 supplement 2), so a weak negative. (iii) S535A raises protein-synthesis labelling: yes, OPP, n=5, t test, Fig 7A-B, in adult wild-type retina. (iv) A catalytically dead epsilon removes the gain: "largely negated" by E572A (Fig 5E-F); a dominant-negative that "lacks catalytic activity but is capable of forming heteropentameric eIF2B complex". All four clauses hold at the level stated. Not in the clauses: the OPP injury state is not given in the text I read; phospho-eIF2alpha was not measured; survival was not changed.

## 5. Hypothesis items

| id | judgement |
|---|---|
| H1 (hypothesis) | The prediction is conditional and not favourable by itself; the refuters (a) to (d) and the "requires first" step are stated. The documented action on the node is real only for the older compounds: LiCl, SB-415286, SB-216763 (12133000, abstract) and for genetic Gsk3b loss (26974342). For the compounds the item names from the other package (LY-2090314, laduviglusib, TDZD-8) no source in this audit documents Ser535 dephosphorylation: one Europe PMC string (`(CHIR99021 OR laduviglusib OR LY2090314 OR "LY-2090314" OR TDZD-8 OR tideglusib) AND (eIF2B ...)`) returned only reviews and unrelated titles, one route only. The statement should say the action of these three on pS535 is a class expectation, not documented. TDZD-8 is, as far as I recall, described as non-ATP-competitive, which conflicts with the item's phrase "an ATP-site GSK3 inhibitor of a defined chemotype, and a second ... of a different class" only in that the second class is named by recollection, not by a source I read. No compound is presented as established; the abstention is kept. Missing premise stated. |
| H2 (hypothesis) | The retinal isoform result is real but one tissue, adult, one antibody, one negative at n=5 from a different deletion mode. The item states this ("the retinal result does not transfer" as a refuter). Fine. |
| H3 (hypothesis) | Numbering is right (human 540, mouse 536, rat 535). One internal inconsistency: the item says the Ala form "separates GSK3 from other kinases acting on the same site (DYRK2 is annotated at the priming serine)". DYRK2 acts at the priming serine, a different residue (rat 539, mouse 540, human 544), so S535A cannot separate GSK3 from DYRK2; that needs a Ser539 (or species equivalent) construct. Also in this package the "S535A is constitutively active" is cited (Pap and Cooper 2002), not measured (E16 limit). The refuter (Ala alone raises translation in controls) is stated. |
| H4 (hypothesis) | The prediction is "little correction" if the lesion is independent of phospho-eIF2, "some" if a stability or conformational component exists: a discriminating probe, not a favourable claim, and a refuter is named. Two additions it needs. (1) E25's rescue assay contained 5 nM phospho-eIF2 and its cell assays used phospho-eIF2-driven stress, so E25 does not show phospho-eIF2-free rescue; the prediction rests on E20 to E22 (wild-type enzyme or eIF2B-depleted cells). (2) The "phospho-mimetic epsilon as a positive test" assumes a Ser535 phosphomimetic reproduces the inhibition; no source read here shows that, and GSK3 itself needs the primed Ser539 (RS06). The phosphomimetic needs its own validation. |
| H5 | A null stated before the measurement; no source needed. |

## 6. Omitted decisive points

1. E02: the sentence "at or above ... in every region" is false in hippocampus and cortex by 0.1 (own reading of Fig 7c, equal to the manifest's printed numbers). Correct before use.
2. E25: all VWMD GEF assays contained 5 nM phospho-eIF2; the rescue is not phospho-eIF2-free. This matters for how H4 weighs E21 against E25.
3. E21 is a wild-type-enzyme assay; it cannot be read as "ISRIB would fail on a defective eIF2B".
4. CH01/E01: P20 is after seizure onset in a malformed, hypomyelinated brain; Ser9 change may be secondary.
5. E04 could reverse the direction of CH02 against CH01 if the residue is Ser9; unread.
6. Drosophila Wwox knockdown raises Atf4 (42909904): a WWOX-deficient ISR-adjacent protein-level readout the absence statement should name.
7. H3 numbering/priming: S535A does not distinguish GSK3 from DYRK2 (priming at Ser539); a phosphomimetic at 535 is unvalidated.
8. 12133000's own limit: non-specific compounds, one hamster line, insulin context; the "additional inputs" are not identified in the abstract (11500362's CK2 Ser712/713 sites are one candidate class).
9. RS02 offset error (+2, not +3) and "by similarity" status of human Ser540.

## 7. What I did not check

- The full text of 12133000 (publisher blocks XML download; no other route tried), 15001529 and 15126504 (not open): every statement about them is abstract-level.
- Antibody, Methods and statistics for 26974342 beyond the legends read; no figure images for 26974342, 33220178, 29489452; no cryo-EM or binding sections of 33220178; the 29489452 Methods.
- Rows E19, E23, E24, E27, E28: only the sentence or feature was verified, not the full context; E28 database features were checked in full for the eight reviewed entries (not for the cited papers behind them except the abstract of 11311121 and the title of 24023715).
- CH03 (SH-SY5Y, Tau docking) and the IT15 isoform-ratio figures (blind).
- PMIDs 36572560, 34058790, 22193544 (GSK3 + WWOX hits, not opened); the reviews 35579296, 40869184, 25688261 and 32512016; the DYRK2/cardiac papers beyond title and abstract.
- Europe PMC full-text queries are noisy; I did not page through the 177, 308 and 33 hit lists beyond the first page. The two absence claims are "not found on two routes", not proven.
- The TDZD-8 mechanism class statement above is from memory and was not sourced.
