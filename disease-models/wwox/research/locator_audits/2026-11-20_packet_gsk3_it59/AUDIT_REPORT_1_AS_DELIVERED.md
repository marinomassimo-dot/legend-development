# Blind audit 1 of the GSK-3 packet change (G01, D02), IT59: delegate report, verbatim

Fresh legend-delegate, claude-sonnet-5-5, effort high (read back from its transcript). Packet AUDIT_PACKET.md (sha256 in AUDIT_PACKET.sha256). Persisted by IT before any repair; not edited. Result: SUPPORTED 3 (P2, P3, P6), SUPPORTED_WITH_LIMIT 4 (P1, P4, P5, P7) with clauses to repair; repairs applied in the packet change; second check on AUDIT_PACKET_2.md.

BLIND AUDIT, GSK-3 packet change (G01/D02), IT59. One round, no sub-delegation, no repository file edited. Scratch only in /home/desktop/.claude/jobs/96cc479a/tmp/blind_packet/. Every quoted string was tested as a substring of its stripped anchor by script (all passed). Ma 2017 quotes were tested against an excerpt I typed from the PubMed full-text tool output, so that check is only as good as my transcription.

| # | Verdict | Main reason (anchor, locator) |
|---|---|---|
| P1 | SUPPORTED_WITH_LIMIT (one clause OVERSHOOT) | See notes 1 and 2 |
| P2 | SUPPORTED | Boxed warning, 5.1, 5.7 and 8.1 text match; one repackager SPL for lithium carbonate |
| P3 | SUPPORTED | 8.4 Pediatric Use matches; the second clause is interpretation |
| P4 | SUPPORTED_WITH_LIMIT (one clause OVERSHOOT-prone) | See note 3 |
| P5 | SUPPORTED_WITH_LIMIT | Sheet searched rodent exposure only, by title |
| P6 | SUPPORTED | Matches the sheet |
| P7 | SUPPORTED_WITH_LIMIT | Wording true; see note 6 |

**Notes**
1. P1, overshoot. The packet says "no kinase-activity assay exists in a WWOX system". Wang 2012 contains one: "We performed an in vitro kinase assay to examine whether WWOX interferes with GSK3 β -mediated Tau phosphorylation." The result reads "this phosphorylation is completely abolished in the presence of excess WWOX, but not GST or WWOX L404A". The paper concludes "WWOX negatively regulates GSK3 β kinase activity on the neuron-specific microtubule-binding protein Tau in SH-SY5Y cells". The assay is cell-free with recombinant proteins and a Tau substrate. The packet should narrow its lead to "none in WWOX-deficient cells or tissue". The SCI file line "GSK3-beta activity itself was not measured" also needs that qualifier.
2. P1, the rest holds. Wang: "the phosphorylation levels of phospho-GSK3 β S9 and phospho- β -catenin remained normal"; "S9-independent" occurs 0 times. WWOX knockdown and overexpression read pTau S396 and neurites, and the text names no Ser9 read there. Absence is from text and legends only; I could not view the blot images. Cheng 2020, Fig 7c legend: "Increased activation of GSK3β was determined in the cerebellum, hippocampus and cerebral cortex of Wwox −/− mice at postnatal day 20, as evidenced by dephosphorylation of GSK3β at Ser9". The legend also says "ratio of phosphorylated or total GSK3β to β-actin ... representative results of four independent experiments". So "number of animals not stated" is true, but a count of "four independent experiments" is stated with its unit unclear. Cheng Methods say tissue was taken "at postnatal day 14", against day 20 in the legend. The legend's cerebellum, hippocampus and cortex all fall under "brain".
3. P4. Unit A says the GSK-3 premise is "not supported in the organoid and not distinguishable from random sets in the cortex". Cortex Wnt is the same sign as the premise: adjusted -0.71, inside the null band, n 3 v 4. The blind recompute calls it "borderline against random sets either way, same sign". So "not supported in the cortex" is a fair but firm reading. "Neuronal-deletion mouse" for the held data is not stated in either SCI file; "neuronal-deletion ... pups at P17" appears only for the planned v2 experiment. For that qualifier I give UNVERIFIABLE from these anchors. The GSK3-beta narrowings match the interactome file ("Directness not established"). "Points the other way from the cell-line wording" is loose. Cheng's lower pS9 means more active GSK3beta in the null, which agrees in direction with Wang's WWOX-inhibits-GSK3beta. The tension is about Ser9 as mechanism; the SCI file says "in tension, not in agreement". "No GSK-3 substrate measurement exists in a Wwox-deficient neuron" matches the SCI file, but Wang does read pTau S396 after WWOX RNAi in SH-SY5Y, a cell line.
4. P5 and P6. The sheet says "None of the five has a brain or plasma concentration found by these routes" and defines the search as "in rodents", PubMed titles only. P5's "any ... adult or juvenile" does not say rodent; human plasma was not searched. P6 "low-nanomolar to micromolar": the sheet's own range is 0.7 nM (sub-nanomolar) to 2 µM, plus a 330 µM FRET outlier. Its summary says "low-nanomolar to sub-micromolar". The 1.4- to 2.5-fold figure matches. The 2011 AR-A014418 pair (70 µM alpha against 330 µM beta) is a within-document ratio the sheet excludes as a different assay. The tideglusib, openFDA and paediatric-registry statements match the sheet.
5. P2 and P3. Label record: openFDA SPL set_id 01c4facd-ed79-4078-ba33-2044de372d0f, REMEDYREPACK, effective 20260427, lithium carbonate. The cerebellar-atrophy sequelae sentence is in section 5.1, not the boxed warning proper; the packet lists it among label facts and hedges it correctly.
6. P7, Ma 2017. ICR mice; electroporation at E14.5, analysed at E18.5; "= 3 brains, = 8 slices from each brain". BrdU+ GFP+ cells were higher with siGSK3α or siGSK3β. siGSK3β gave "a substantial decrease in the percentage of Tbr2 GFP cells" and Cux1 "markedly reduced by siGSK3β but unaffected by siGSK3α". The packet omits that α knockdown raised Tbr2. The paper adds: "we cannot entirely rule out off-target effects of the knockdown reagents". This is siRNA knockdown, not knockout.
7. P7, Kim 2009. Genotype from PMC efetch XML: Gsk3a−/−; Gsk3b loxP/loxP; nestin-cre. Text: "had bigger heads ... until they died at P0". Both isoforms are effectively deleted in progenitors, and "The elimination of either GSK-3 family member alone ... had no obvious effect". Kim attributes the phenotype to GSK-3 deletion, not to beta alone, so the packet's phrasing is accurate but should not be read as a beta-specific effect.

**Not reached**
- Figure images, blot ratios and supplements for Wang, Cheng, Ma and Kim.
- The Ma and Kim p-values (symbols stripped by the tool).
- Kim PubMed-db efetch (abstract only); the genotype came from the PMC-db efetch route (HTTP 200, no CAPTCHA or block).

**Files read**
- AUDIT_PACKET.md
- /home/desktop/legend-development/files/fulltext/PMID22193544_Wang2012_PMC.xml
- /home/desktop/legend-development/files/fulltext/PMID32000863_Cheng2020_PMC.xml
- /home/desktop/.claude/jobs/93f134db/tmp/gsk3/label_sections_for_verifier.txt
- PREMISE_SCREEN_RESULT_UNIT_A_ADV095_SCI_20261119.md
- INTERACTOME_AND_SECOND_SYSTEM_RESULT_SCI_20261120.md
- BATCH9_GSK3_nonlithium_..._HE_20261120.md (resolves to advisor_pilot_20261113/adv098_agent_sheets_he_20261119/)
- Ma 2017 (PMC5712306) and Kim 2009 (PMC5328673) via PubMed full text
- NCBI efetch XML for Kim

According to PubMed: Ma 2017 https://doi.org/10.3389/fnmol.2017.00391; Kim 2009 https://doi.org/10.1038/nn.2408.
