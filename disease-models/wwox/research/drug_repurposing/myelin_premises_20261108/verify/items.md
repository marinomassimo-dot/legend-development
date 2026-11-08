# Items for a blind audit (Package B)

Check each item against the named source (open routes only; held text under /home/desktop/legend-development/files/; module tables are named inside the rows). Verdicts: SUPPORTED / OVERSHOOT / UNDERSHOOT / NOT_IN_SOURCE / UNVERIFIABLE with verbatim locator and depth. Vendor pages: two items were relayed by a page summariser; fetch the RAW page text yourself with plain `curl -sL` (default user-agent, no browser string; one request per page; if it returns a challenge, 403 or a script-only shell, stop and record it) and re-read the formulation statement; distinguish the CURRENT product page from the formulation used in 2021. Figures: look at them if reachable without a challenge, else say caption only.

# Part 1: media reconstruction rows

## S1 DRG-OPC co-culture
- phase: DRG neuron plating and maintenance, DIV0 to DIV15
- component: Neurobasal basal medium (NB medium)
- source_in_study_locator: Methods, Cell culture and plasmids, first co-culture paragraph (PMID33914858)
- formulation_or_code: catalogue not stated in the study
- vendor_or_primary_doc_locator: not read (no vendor formulation page opened for Neurobasal)
- thyroid_component_status: not assessed
- status_class: composition_not_determinable
- limit: basal medium composition not read here; a basal-medium contribution is neither assumed nor excluded

## S2 DRG-OPC co-culture
- phase: DRG neuron plating and maintenance, DIV0 to DIV15
- component: B27 supplement in NB medium
- source_in_study_locator: Methods, same paragraph: NB medium (Neurobasal, B27 supplement, L-glutamine, penicillin-streptomycin)
- formulation_or_code: version and concentration not stated in the study; the same laboratory's earlier protocol lists Gibco 17504-044
- vendor_or_primary_doc_locator: protocol paper PMID30551998 key resources table (code); vendor formulation page for the code, relayed by a page summariser (current formulation only)
- thyroid_component_status: current vendor formulation lists T3 (concentration given as confidential)
- status_class: presence_possible
- limit: current formulation of the product is not the formulation of the lot used; no measurement of T3 in the medium exists; concentration unknown so biological relevance unknown

## S3 DRG-OPC co-culture
- phase: FUdR treatment DIV2 to DIV6 and half-medium changes
- component: fluorodeoxyuridine, L-glutamine, penicillin-streptomycin
- source_in_study_locator: Methods, same paragraph
- formulation_or_code: single compounds, no codes
- vendor_or_primary_doc_locator: by identity of the compound
- thyroid_component_status: none by identity
- status_class: absence_documented
- limit: absence by compound identity only; says nothing about the medium as a whole

## S4 DRG-OPC co-culture
- phase: OPC isolation from mixed glia, DIV0 to DIV10 of the glial flasks
- component: DMEM with 10 percent foetal bovine serum
- source_in_study_locator: Methods: glial plating medium [DMEM containing 10% foetal bovine serum, penicillin-streptomycin]
- formulation_or_code: serum lot and DMEM code not stated
- vendor_or_primary_doc_locator: not read
- thyroid_component_status: serum is a possible source of thyroid hormone (general knowledge; no source read here: IPOTESI)
- status_class: presence_possible
- limit: OPCs are shaken off, then seeded onto neurons; carry-over of serum hormone into the co-culture is not documented and not excluded

## S5 DRG-OPC co-culture
- phase: Co-culture, OPCs added DIV15, 9 to 11 days
- component: co-culture medium: DMEM with B27 and N2
- source_in_study_locator: Methods: maintained in co-culture medium (DMEM containing B27 and N2 supplements, N-acetyl-cysteine, forskolin, penicillin-streptomycin)
- formulation_or_code: B27 and N2 versions and concentrations not stated in the study; protocol paper lists Gibco 17504-044 and 17502048
- vendor_or_primary_doc_locator: protocol paper PMID30551998 key resources (codes); vendor B-27 formulation page (T3 listed); N-2 vendor product page (no component list shown)
- thyroid_component_status: B27 route: T3 listed in the current vendor formulation; N2 route: composition not shown on the page read
- status_class: presence_possible
- limit: the study's text names no hormone, but a hormone not named is not absent; hormone content at the OPC unmeasured; the deficit appears with every arm in this same medium

## S6 DRG-OPC co-culture
- phase: Co-culture
- component: N2 supplement
- source_in_study_locator: same sentence
- formulation_or_code: protocol paper lists Gibco 17502048
- vendor_or_primary_doc_locator: vendor product page read shows no component list and no mention of T3 or T4
- thyroid_component_status: not shown
- status_class: composition_not_determinable
- limit: absence of a mention on a page that lists no components documents nothing

## S7 DRG-OPC co-culture
- phase: Co-culture
- component: N-acetyl-cysteine and forskolin
- source_in_study_locator: same sentence
- formulation_or_code: 5 mg/ml and 5 mM as printed in the study text (units as printed)
- vendor_or_primary_doc_locator: single compounds
- thyroid_component_status: none by identity
- status_class: absence_documented
- limit: forskolin raises cyclic AMP and is in every arm (already flagged in the module as a confound for CREB-type arms)

## S8 Isolated oligodendrocyte culture of the protocol paper (not a Repudi arm)
- phase: Sato medium, 9 to 11 days
- component: T3 and T4 added explicitly beside B-27
- source_in_study_locator: Methods, Primary cultures (PMID30551998); not reported in the WWOX paper
- formulation_or_code: 0.34 and 0.4 ug/ml as printed there; B-27 Gibco 17504-044 in the key resources
- vendor_or_primary_doc_locator: PMID30551998 full text via PMC
- thyroid_component_status: T3 and T4 named as added
- status_class: presence_documented
- limit: a different culture of a different paper from the same laboratory; shows only that the laboratory adds named hormones where it wants them, which does not show the co-culture medium was judged hormone-free

## S9 Oligocortical spheroid
- phase: Day 0 to 6, embryoid body formation
- component: DMEM/F12 with knockout serum replacement 20 percent, dorsomorphin or LDN-193189, SB-431542, ROCK inhibitor
- source_in_study_locator: Methods, Oligocortical spheroid generation
- formulation_or_code: KOSR Gibco 10828-028 as listed in the feeder-culture paragraph
- vendor_or_primary_doc_locator: not read
- thyroid_component_status: not assessed
- status_class: composition_not_determinable
- limit: serum-replacement composition is proprietary; the stage precedes the oligodendroglial stages

## S10 Oligocortical spheroid
- phase: Day 7 to 50, neural medium (NM)
- component: Neurobasal with 2 percent B27 supplement
- source_in_study_locator: Methods: NM composed of Neurobasal medium, 2% B27 supplement (Gibco; 17504044), 1% GlutaMAX, 1% P/S
- formulation_or_code: Gibco 17504044 (stated)
- vendor_or_primary_doc_locator: vendor B-27 formulation page (same catalogue code), relayed by a page summariser
- thyroid_component_status: T3 listed in the current vendor formulation; concentration confidential
- status_class: presence_possible
- limit: this is the study's stated product code, but the current page is not the lot used; Day 27 to 40 BDNF and NT-3, Day 41 to 50 NM without supplementation, all contain B27

## S11 Oligocortical spheroid
- phase: Day 51 onward, oligo maturation medium (base of every later medium)
- component: Neurobasal with 1 percent B27 supplement, GlutaMAX, P/S, 1 percent Matrigel
- source_in_study_locator: Methods: From Day 51 onwards, all mediums were based on oligo maturation medium
- formulation_or_code: B27 code not restated for this medium
- vendor_or_primary_doc_locator: as above
- thyroid_component_status: T3 listed in current vendor formulation of the code used for NM; code for this medium not stated
- status_class: presence_possible
- limit: assumed to be the same product as NM only by inference from the single code the study prints

## S12 Oligocortical spheroid
- phase: OPC expansion, Day 51 to 60 (Day range read from the scheme, Supp Fig 9A)
- component: oligo maturation medium plus PDGF-AA and IGF-1
- source_in_study_locator: Methods; Supp Fig 9A viewed
- formulation_or_code: R&D codes as printed
- vendor_or_primary_doc_locator: not applicable
- thyroid_component_status: no added T3
- status_class: absence_documented
- limit: added-supplement level only; B27 stays in the base

## S13 Oligocortical spheroid
- phase: Oligo differentiation, Day 60 to 70 (scheme)
- component: added T3 supplement on top of oligo maturation medium
- source_in_study_locator: Methods: oligo maturation medium was supplemented with 40 ng/ml T3 (Sigma; T2877), making up the oligo differentiation medium
- formulation_or_code: Sigma T2877 (stated)
- vendor_or_primary_doc_locator: not applicable
- thyroid_component_status: T3 supplement added
- status_class: presence_documented
- limit: the day range is read from the scheme and not stated in the text; same medium for knockout and control spheroids (same batch statement in Methods)

## S14 Oligocortical spheroid
- phase: Oligo maturation, Day 71 onward (readouts weeks 30 to 37)
- component: added T3 supplement
- source_in_study_locator: Methods: from Day 71 onward, spheroids were cultured in oligo maturation medium
- formulation_or_code: none
- vendor_or_primary_doc_locator: not applicable
- thyroid_component_status: no added T3 supplement after Day 70
- status_class: absence_documented
- limit: documents the supplement only; the medium still contains B27

## S15 Oligocortical spheroid
- phase: Oligo maturation, Day 71 onward (readouts weeks 30 to 37)
- component: B27 supplement within the oligo maturation medium
- source_in_study_locator: same sentence as the Day 51 row: the maturation medium is the Neurobasal and B27 base
- formulation_or_code: version not restated; formulation in the lot used unknown
- vendor_or_primary_doc_locator: vendor B-27 formulation page; Brewer 1993 abstract names 20 components but no hormone
- thyroid_component_status: T3 listed in current vendor formulation; may remain present after Day 70
- status_class: presence_possible
- limit: consequence: a hormone-withdrawal reading after Day 70 is not documented; hormone exposure after Day 70 is undetermined, not zero

## S16 Original spheroid protocol (reference 24, Madhavan 2018)
- phase: T3 Day 60 to 70, then maintenance
- component: T3 supplement then Neurobasal-A spheroid media with B-27 without vitamin A
- source_in_study_locator: Methods, Oligocortical Spheroid Differentiation (PMID30046099)
- formulation_or_code: B-27 without vitamin A, Invitrogen 12587 as printed
- vendor_or_primary_doc_locator: PMID30046099 full text via PMC
- thyroid_component_status: T3 supplement in Day 60 to 70; maintenance medium holds a B-27 variant whose T3 status was not read
- status_class: composition_not_determinable
- limit: the WWOX study used the B27 with vitamin A code for NM, so the original and the WWOX formulations differ; whether the without-vitamin-A product carries T3 was not determined here

## S17 Study supplement
- phase: whole
- component: any medium composition in the supplementary methods
- source_in_study_locator: Supplementary Materials and Methods (held File009 text, strings B27, N2, T3, thyro, medium, supplement)
- formulation_or_code: none found
- vendor_or_primary_doc_locator: not applicable
- thyroid_component_status: not stated
- status_class: composition_not_determinable
- limit: bounded: held text only, figures other than Supp Fig 9A not viewed; not found is not not done

# Part 2: feasibility rows

## E1 EX1
- deposit_accession: GSE158684 (nuclei); series GSE158685 groups it with GSE158681 and GSE158682
- public_access: GEO series text and six supplementary files public (GEO page states Public on Oct 01 2026); the paper states data are available on reasonable request and gives no accession; the GEO brief record shows no publication line, so the link to PMID33914858 rests on identical nucleus numbers (module census); raw reads SRX9206272 to SRX9206279 still status hup (8 of 8 re-queried 2026-11-08, no runs listed)
- files_and_size: ctrl matrix 26,395,588 bytes; ko matrix 23,103,829 bytes; features 279,361 bytes each; barcodes 17,334 and 16,000 bytes; already held locally in the shared files area with a checksum list, nothing downloaded in this package
- samples: 8 GSM (4 per arm) but only two matrices (one per arm); the paper states n = 1 per arm; 3182 control and 2920 knockout nuclei
- biological_replicates_independent: no (at most 1 per arm by the paper; nuclei are not animals)
- pooled: yes: one Cell Ranger output per arm; one library registered four times, four animals pooled in one load, or four merged libraries cannot be told apart without reads
- tissue_and_stage: hippocampus nuclei, P17, Synapsin-Cre neuron-targeted deletion against Cre-only control, mixed background, seizing animals near their short lifespan
- cell_populations_present: own crude marker rule (not the module's class labels): neuron-like (Snap25 at least 2 UMI) 1880 control and 1724 knockout; OPC-like (Pdgfra at least 2, Snap25 below 2) 47 and 76; mature-oligodendrocyte-like (Mog or Plp1 high) 301 and 71; Hr, the hormone-target gene named in the module's source, is detected in 13 and 6 mature-oligodendrocyte-like and 0 and 1 OPC-like nuclei (Thra and Klf9 in many more, e.g. Thra in 169 and 44 mature-like nuclei); evidence rows G05 and G06
- already_analysed_in_module: oligodendrocyte-lineage composition, Pvalb, immature markers (IT13b); identity and pooling (IT14 P1a). Hormone-target and transporter genes were not read in the nuclei by any package; in the bulk deposits a thresholded table already lists Hr, Dio3, Dio2 and Slco1c1 as lower in some contrasts (evidence rows T01 to T03)
- can_it_discriminate_what: pooled nuclei give description only: they cannot separate a hormone-deprivation-like response from lineage composition (oligodendrocytes are 5-fold fewer in the knockout pool), from stress or from a pool-level technical difference; the neuron-like class shows flat Hr, Klf9 and Thrb per nucleus (one pool, low counts)
- verdict: RUN as description only (done, small counts, no test, evidence rows G05 and G06); do not extend. The independent-animal bulk tables (GSE158681, GSE158682, 2 to 4 animals per arm, files 4.8 MB and 2.6 MB) are the better route for a hormone-target read, but a transcript-to-gene map (Ensembl release 92 cDNA, about 50 MB) is needed and was not downloaded; it was run once by IT24, whose output keeps only genes above a threshold

## E2 EX1_alt_bulk
- deposit_accession: GSE158681 (hippocampus, 14 GSM); GSE158682 (cortex, 7 GSM)
- public_access: public TPM tables fetched over GEO FTP and checksummed in this package (sha256 equal to the module's recorded values); no access challenge
- files_and_size: GSE158681 TPM table 4,819,338 bytes; GSE158682 TPM table 2,614,428 bytes; transcript-level rows (Ensembl transcript identifiers), so gene mapping needs a transcript list not at hand
- samples: hippocampus: WT 3 v null 2, S-Ctrl 2 v S-KO 3, N-WT 2 v N-KO 2; cortex: S-Ctrl 4 v S-KO 3
- biological_replicates_independent: yes at animal level by the deposit design (2 to 4 per arm); too few for inference
- pooled: no (one sample per animal as deposited, bulk tissue)
- tissue_and_stage: P17 whole hippocampus or cortex, three genetic contrasts
- cell_populations_present: bulk tissue: every cell type averaged, so lineage composition and neuronal state are confounded by design
- already_analysed_in_module: IT24 P4 and IT27 P1 hold thresholded gene tables (log2 ratio beyond 0.585, descriptive only): Hr lower in S-KO cortex and N-KO hippocampus; Dio3 lower in S-KO and null hippocampus; Dio2 and Slco1c1 lower in some contrasts. No package linked them to a thyroid reading
- can_it_discriminate_what: a lowering of Hr, Dio3 and Dio2 is the direction expected if hormone-responsive transcription were lower; it cannot distinguish that from oligodendrocyte depletion (Hr is read in oligodendroglial nuclei here), from activity or seizure effects, or from delayed maturation
- verdict: NOT RUN (not asked to download 50 MB; replication of 2 to 3 animals supports description and exploration only). Reading the already-held thresholded rows is done (evidence rows T01 to T03)

## E3 EX5
- deposit_accession: GSE158684 (nuclei); series GSE158685 groups it with GSE158681 and GSE158682
- public_access: GEO series text and six supplementary files public (GEO page states Public on Oct 01 2026); the paper states data are available on reasonable request and gives no accession; the GEO brief record shows no publication line, so the link to PMID33914858 rests on identical nucleus numbers (module census); raw reads SRX9206272 to SRX9206279 still status hup (8 of 8 re-queried 2026-11-08, no runs listed)
- files_and_size: ctrl matrix 26,395,588 bytes; ko matrix 23,103,829 bytes; features 279,361 bytes each; barcodes 17,334 and 16,000 bytes; already held locally in the shared files area with a checksum list, nothing downloaded in this package
- samples: 8 GSM (4 per arm) but only two matrices (one per arm); the paper states n = 1 per arm; 3182 control and 2920 knockout nuclei
- biological_replicates_independent: no (at most 1 per arm)
- pooled: yes: one Cell Ranger output per arm; one library registered four times, four animals pooled in one load, or four merged libraries cannot be told apart without reads
- tissue_and_stage: hippocampus nuclei, P17, Synapsin-Cre neuron-targeted deletion against Cre-only control, mixed background, seizing animals near their short lifespan
- cell_populations_present: OPC-like 47 control and 76 knockout nuclei, mature-oligodendrocyte-like 301 and 71 (own crude rule); Slc16a1 (MCT1) detected in 11 and 7 mature-oligodendrocyte-like nuclei, 0 and 2 OPC-like; Slc2a1 in 18 and 6, 3 and 4 (evidence row G06)
- already_analysed_in_module: none for transporters or glycolytic genes in these nuclei; the P47T knock-in hippocampal glycolysis module (O5, p near 0.06) and fibroblast lactate are other systems
- can_it_discriminate_what: expression of a transporter transcript is not uptake, not flux and not utilisation; oligodendroglial counts per arm are too low for any gene-level comparison, and the knockout pool has few mature oligodendrocytes; neuron-like per-nucleus rates differ (Slc16a7 about 0.55-fold, tracking Slc17a7 about 0.77-fold, so excitatory-neuron composition may explain it)
- verdict: NOT EXTENDED: gene presence in the lineage is all the data can state (the machinery is detectable in neuron-like nuclei and in a handful of oligodendroglial nuclei); nothing about supply, direction or function

## E4 EX5_alt_bulk
- deposit_accession: GSE158681; GSE158682
- public_access: as EX1_alt_bulk
- files_and_size: as EX1_alt_bulk
- samples: as EX1_alt_bulk
- biological_replicates_independent: yes at animal level (2 to 4 per arm)
- pooled: no
- tissue_and_stage: P17 bulk hippocampus and cortex
- cell_populations_present: bulk: composition-confounded
- already_analysed_in_module: IT24 P4 and IT27 P1 thresholded rows: Slc16a7, Eno1, Pgk1 lower and Pdk2 higher in S-KO hippocampus; Slc16a1, Ldha, Pgk1, Hk1 and Pkm moved in N-KO hippocampus with mixed signs; Slc2a1 and Pdk4 lower in the null hippocampus; the sign is not uniform across contrasts (evidence row T04)
- can_it_discriminate_what: mixed transcript signs of glycolytic genes, none of them a measure of lactate, glucose or flux; fits neither a plain supply deficit nor an overflow by itself
- verdict: NOT RUN beyond reading the held rows; replication of 2 to 3 animals supports description only

# Part 3: new-read evidence rows

## R1 M01
- source_id: PMID33914858
- evidence_class: method_statement
- system: mouse DRG neurons, Wwox genotypes
- perturbation: none
- cell_stage: DRG from E13.5 embryos, DIV0 to DIV15
- level: medium
- finding: The DRG neurons are plated and kept in NB medium that includes B27 supplement before OPCs are added, so B27 is in the neuronal culture phase too (the module held the co-culture medium only)
- locator_quote: resuspended in NB medium (Neurobasal, B27 supplement, 0.5 mM L-glutamine, and penicillin-streptomycin)
- depth_reached: partial_fulltext (Methods, held browser-print text)
- limits: B27 version and concentration not stated
- role: support

## R2 M02
- source_id: PMID33914858
- evidence_class: method_statement
- system: human oligocortical spheroids, hESC line, whole-cell WWOX knockout
- perturbation: none
- cell_stage: Day 7 to 50
- level: medium
- finding: Neural medium for Day 7 to 50 contains 2 percent B27 supplement with the code Gibco 17504044; Day 27 to 40 BDNF and NT-3 and Day 41 to 50 no supplement ride on this base
- locator_quote: 2% B27 supplement
- depth_reached: partial_fulltext (Methods, held browser-print text; code in the same sentence)
- limits: the code printed in the text is the one fact about B27 version in this study
- role: support

## R3 M03
- source_id: PMID33914858
- evidence_class: method_statement
- system: human oligocortical spheroids
- perturbation: none
- cell_stage: Day 51 onward
- level: medium
- finding: Every medium from Day 51 is based on an oligo maturation medium that includes 1 percent B27 supplement (code not restated)
- locator_quote: From Day 51 onwards, all mediums were based on oligo maturation medium
- depth_reached: partial_fulltext (Methods, held browser-print text; supplement named in the next sentence block)
- limits: extraction places a trademark glyph inside the sentence; the B27 fraction is read from the following lines
- role: support

## R4 M04
- source_id: PMID33914858
- evidence_class: method_statement
- system: human oligocortical spheroids
- perturbation: T3 supplement
- cell_stage: oligo differentiation stage
- level: medium
- finding: T3 40 ng per ml is added to the oligo maturation medium to make the oligo differentiation medium; the day range is not stated in the text
- locator_quote: oligo maturation medium was supplemented with 40 ng/ml T3 (Sigma; T2877), making up the oligo differentiation medium
- depth_reached: partial_fulltext (Methods)
- limits: knockout and control spheroids share the batch statement; no T3-free arm
- role: support

## R5 M05
- source_id: PMID33914858
- evidence_class: figure_scheme
- system: human oligocortical spheroids
- perturbation: none
- cell_stage: Days 1 to 70 and after
- level: medium
- finding: Supp Fig 9A scheme lists Oligo Differentiation with T3 at Days 60-70 and Oligo Maturation from Days 70-
- locator_quote: Days 60-70
- depth_reached: figure viewed (rendered page of the supplement, panel A only)
- limits: scheme of the workflow, not a Methods statement; panels B to D not used
- role: support

## R6 M06
- source_id: PMID33914858
- evidence_class: method_statement
- system: human oligocortical spheroids
- perturbation: none
- cell_stage: Day 71 onward (readouts weeks 30 to 37)
- level: medium
- finding: The text states a switch to oligo maturation medium at Day 71; it states no removal of B27, so only the added T3 supplement stops
- locator_quote: from Day 71 onward, spheroids were cultured in oligo maturation medium, with complete medium changes every 2 days
- depth_reached: partial_fulltext (Methods)
- limits: not a statement about hormone content of the medium either way
- role: counter

## R7 M07
- source_id: PMID33914858
- evidence_class: bounded_search
- system: held supplement text (File009)
- perturbation: strings B27, N2, T3, thyro, medium, supplement
- cell_stage: n/a
- level: medium
- finding: No medium-composition sentence in the supplementary methods text; they cover RNA-seq and nuclei isolation
- locator_quote: NOT_FOUND after: held File009 text, strings B27 N2 T3 thyro medium supplement, 2026-11-08
- depth_reached: bounded text search plus one rendered page
- limits: figures other than Supp Fig 9A not viewed; not found is not not done
- role: limit

## R8 M08
- source_id: PMID33914858
- evidence_class: method_statement
- system: paper
- perturbation: none
- cell_stage: n/a
- level: data access
- finding: The paper's data statement points to the corresponding author and gives no repository accession
- locator_quote: available from the corresponding author upon reasonable request
- depth_reached: partial_fulltext (Data and code availability)
- limits: the GEO deposit exists separately; no source read links it to the paper by accession
- role: limit

## R9 E01
- source_id: PMID30551998
- evidence_class: method_statement
- system: mouse DRG neurons plus OPCs (the protocol cited as reference 23 by the WWOX paper)
- perturbation: none
- cell_stage: co-culture 9 to 11 days
- level: medium
- finding: The cited protocol uses the same co-culture medium and lists B27 as Gibco 17504-044 and N2 as Gibco 17502048 in its key resources
- locator_quote: DMEM containing B27 and N2 supplements, 5μg/ml N-Acetyl-Cysteine, 5μM forskolin, penicillin-streptomycin
- depth_reached: partial_fulltext (STAR Methods, key resources; PMC text via the PubMed tool)
- limits: codes of a 2019 paper by the same laboratory do not prove the lot used in 2021
- role: support

## R10 E02
- source_id: PMID30551998
- evidence_class: method_statement
- system: isolated mouse and rat oligodendrocytes (a different culture in the cited paper)
- perturbation: none
- cell_stage: 9 to 11 days
- level: medium
- finding: For isolated oligodendrocytes the laboratory names T3 and T4 explicitly in a Sato medium that also has B-27; the co-culture recipe names neither
- locator_quote: Sato medium (DMEM containing B-27 supplement, Glutamax, penicillin-streptomycin, 1% horse serum, sodium pyruvate, 0.34μg/ml T3 and 0.4 μg/ml T4)
- depth_reached: partial_fulltext (STAR Methods)
- limits: not a Repudi arm; reading the contrast as proof of hormone-free co-culture would be an inference not supported
- role: counter

## R11 E03
- source_id: PMID30046099
- evidence_class: method_statement
- system: human oligocortical spheroids (reference 24, the protocol the WWOX paper followed)
- perturbation: T3 Day 60 to 70
- cell_stage: Day 50 to 70
- level: medium
- finding: In the original protocol T3 is added Day 60 for 10 days and after Day 70 spheroids are kept in the Neurobasal-A spheroid medium, which carries a B-27 supplement
- locator_quote: After day 70, spheroids were matured and maintained in Neurobasal-A spheroid media
- depth_reached: partial_fulltext (Results and Online Methods; PMC text via the PubMed tool)
- limits: the WWOX paper's own Day 71 sentence is the study's statement; this row shows the origin of the pattern
- role: support

## R12 E04
- source_id: PMID30046099
- evidence_class: method_statement
- system: same
- perturbation: none
- cell_stage: Day 7 onward
- level: medium
- finding: The original maintenance medium uses a B-27 without vitamin A (Invitrogen 12587), a different product from the WWOX paper's stated code
- locator_quote: Neurobasal-A medium (Invitrogen #10888022) with added B-27 serum substitute without vitamin A (Invitrogen #12587)
- depth_reached: partial_fulltext (Online Methods)
- limits: T3 content of that variant was not read
- role: limit

## R13 B01
- source_id: PMID8377226
- evidence_class: abstract_statement
- system: rat embryonic hippocampal neurons
- perturbation: B27 development
- cell_stage: 4 day and 4 week cultures
- level: composition
- finding: B27 is a defined serum-free supplement optimised over 20 components; the abstract names no hormone
- locator_quote: We have systematically optimized the concentrations of 20 components of a previously published serum-free medium
- depth_reached: abstract_only (PubMed record)
- limits: the 1993 composition table was not read; abstract cannot show T3 presence or absence
- role: limit

## R14 B02
- source_id: Thermo Fisher media formulation page for catalogue 17504001 and 17504044
- evidence_class: vendor_document
- system: B-27 Serum-Free Supplement (50X) liquid, current formulation
- perturbation: none
- cell_stage: n/a
- level: composition
- finding: The current vendor formulation lists T3 among its other components; concentration given as confidential and as proprietary
- locator_quote: T3 (triodo-I-thyronine)
- depth_reached: vendor page relayed by the fetch tool's page summariser, raw page not seen
- limits: summariser quote not guaranteed verbatim to the raw page: re-read the raw page in verification; current product, not the lot used in 2021; no version or date on the page; the PDF manual route returned HTTP 403 and was not retried
- role: support

## R15 B03
- source_id: Thermo Fisher product page for catalogue 17504044
- evidence_class: vendor_document
- system: B-27 supplement product page
- perturbation: none
- cell_stage: n/a
- level: composition
- finding: The product page lists no composition; it mentions alternative formulations and an insulin-free version
- locator_quote: Yes, we do offer B-27 Supplement, minus insulin
- depth_reached: vendor page relayed by summariser
- limits: no composition to cite; alternative formulations exist, so the product line varies
- role: limit

## R16 B04
- source_id: Thermo Fisher product page for catalogue 17502048
- evidence_class: vendor_document
- system: N-2 supplement product page
- perturbation: none
- cell_stage: n/a
- level: composition
- finding: The page read lists no components and does not mention T3 or T4; it says the supplement is based on a published N-1 formulation
- locator_quote: N-2 Supplement ist ein chemisch definierter serumfreier Ergänzungsstoff
- depth_reached: vendor page relayed by summariser
- limits: nothing about N2 hormones can be concluded: no component list shown
- role: limit

## R17 B05
- source_id: PMID31396286
- evidence_class: secondary_statement
- system: human retinal organoids and Muller-cell-derived stem cells
- perturbation: none
- cell_stage: n/a
- level: composition
- finding: An unrelated open paper states that the B27 supplement contains T3 and uses it as the source of thyroid-receptor signal in retinal organoids
- locator_quote: the presence of triiodothyronine (T3), the most active form of thyroid hormone in the B27 supplement
- depth_reached: partial_fulltext (Discussion sentence; the Europe PMC text searched for T3, thyroid and B27)
- limits: secondary statement, not a composition table; no concentration; a different lot and decade
- role: support

## R18 G01
- source_id: GSE158684
- evidence_class: public_deposit
- system: mouse hippocampal nuclei, snRNA-seq
- perturbation: Synapsin-Cre neuronal Wwox deletion
- cell_stage: P17
- level: design
- finding: The series holds S-Control 3182 and S-KO 2920 nuclei, eight sample records and two matrices
- locator_quote: hippocampal nuclei were isolated from S-Control (total number of nuclei, 3182) and S-KO (total number of nuclei, 2920)
- depth_reached: GEO series text read
- limits: no replicate or animal index; paper n = 1 per arm (module IT14)
- role: limit

## R19 G02
- source_id: SRA experiments SRX9206272 to SRX9206279
- evidence_class: public_deposit
- system: raw reads of GSE158684
- perturbation: n/a
- cell_stage: n/a
- level: access
- finding: All eight snRNA experiments remain status hup with empty run lists on 2026-11-08
- locator_quote: status="hup"
- depth_reached: NCBI esummary read for the eight identifiers
- limits: a status, not a statement about when reads will appear
- role: limit

## R20 G03
- source_id: GSE158681 and GSE158682
- evidence_class: public_deposit
- system: bulk RNA-seq, mouse P17
- perturbation: genetic contrasts
- cell_stage: P17
- level: design
- finding: Independent-animal bulk TPM tables exist for hippocampus (S-Ctrl 2 v S-KO 3, N 2 v 2, WT 3 v null 2) and cortex (S 4 v 3)
- locator_quote: Samples are grouped. WT (n=3) vs KO (n=2), S-Ctrl (n=2) vs S-KO (n=3), N-WT (n=2) vs N-KO (n=2)
- depth_reached: GEO series text read; table headers and checksums read
- limits: 2 to 4 per arm; transcript-level rows need a gene map; per-sample animal identity as deposited
- role: support

## R21 G05
- source_id: GSE158684
- evidence_class: own_descriptive_count
- system: hippocampal nuclei, neuron-like class by Snap25 at least 2 UMI
- perturbation: none (descriptive)
- cell_stage: P17
- level: transcript, pooled
- finding: Per-nucleus UMI in the neuron-like class, knockout over control: Hr 1.07, Klf9 0.99, Thrb 1.00, Thra 1.39, Dio2 1.66, Slc16a2 0.65, Slco1c1 1.42, Slc16a1 1.11, Slc2a3 0.83, Slc16a7 0.55 (Slc17a7 0.77, Snap25 1.10)
- locator_quote: OWN_COUNT scratch count of the held matrices, no source quote
- depth_reached: own count, one pool per arm, crude class rule, no test
- limits: low counts for Hr (47 and 46 UMI) and Dio2; neuronal ambient and composition effects not removed; Slc16a7 tracks the excitatory-neuron marker, so composition is a rival
- role: counter

## R22 G06
- source_id: GSE158684
- evidence_class: own_descriptive_count
- system: hippocampal nuclei, OPC-like and mature-oligodendrocyte-like classes (own crude rule)
- perturbation: none (descriptive)
- cell_stage: P17
- level: transcript, pooled
- finding: OPC-like nuclei 47 control and 76 knockout; mature-oligodendrocyte-like 301 and 71; in those classes Hr is detected in 0 and 1 (OPC) and 13 and 6 (mature) UMI, Slc16a1 in 0 and 0 and 12 and 31 UMI
- locator_quote: OWN_COUNT scratch count of the held matrices, no source quote
- depth_reached: own count, crude class rule, not the module's labels (IT13b: 12.0 versus 2.4 percent oligodendrocyte-called nuclei)
- limits: gene-level comparison in oligodendroglial nuclei is not supportable at these counts
- role: limit

## R23 T01
- source_id: module: IT24 P4 and IT27 P1 tables
- evidence_class: held_table_row
- system: mouse P17 cortex, Synapsin-Cre deletion (3 v 4 animals)
- perturbation: neuronal deletion
- cell_stage: P17
- level: transcript, bulk
- finding: Hr 14.60 TPM against 35.42, log2 ratio -1.048; also lower in N-KO hippocampus (3.98 against 9.16, -0.842); Slco1c1 lower in S-KO cortex and N-KO hippocampus
- locator_quote: C_S Hr 14.60 35.42 -1.048 3 4
- depth_reached: held thresholded table read (genes beyond 0.585 only)
- limits: descriptive_only flag in the table; a gene absent from the table is untested or below threshold, not unchanged
- role: support

## R24 T02
- source_id: module: IT24 P4 and IT27 P1 tables
- evidence_class: held_table_row
- system: mouse P17 hippocampus, Synapsin-Cre deletion (3 v 2) and germline null (2 v 3)
- perturbation: neuronal deletion; germline null
- cell_stage: P17
- level: transcript, bulk
- finding: Dio3 0.45 against 3.16 TPM in S-KO (log2 -1.559) and 0.63 against 2.04 in null (-0.947); Dio2 lower in null (9.76 against 21.01) and N-KO (3.55 against 10.81)
- locator_quote: H_S Dio3 0.45 3.16 -1.559 3 2
- depth_reached: held thresholded table read
- limits: very low TPM for Dio3; 2 to 3 animals; the table is not linked to a thyroid reading in any module file searched (git grep, strings Dio3, Dio2, Hr with thyroid words)
- role: support

## R25 T03
- source_id: module: IT24 P4 and IT27 P1 tables
- evidence_class: held_table_row
- system: same
- perturbation: same
- cell_stage: P17
- level: transcript, bulk
- finding: Hormone-axis transcripts are lower in several contrasts but Thra is higher in N-KO hippocampus (1026.56 against 778.54): the direction is not uniform
- locator_quote: H_N Thra 1026.56 778.54 0.667 2 2
- depth_reached: held thresholded table read
- limits: 2 per arm; composition and activity unadjusted
- role: counter

## R26 T04
- source_id: module: IT24 P4 and IT27 P1 tables
- evidence_class: held_table_row
- system: same plus S-KO cortex
- perturbation: same
- cell_stage: P17
- level: transcript, bulk
- finding: Energy-pathway transcripts move with mixed signs: Eno1 -0.971 and Pgk1 -0.622 and Slc16a7 -0.610 in S-KO hippocampus, Ldha -0.994 and Slc16a1 -1.052 and Pkm +1.128 in N-KO hippocampus, Slc2a1 -0.814 in null
- locator_quote: H_S Eno1 463.05 1189.12 -0.971 3 2
- depth_reached: held thresholded table read
- limits: transcripts, not lactate or flux; thresholded rows only
- role: counter

# Part 4: lever cards (check identity, action, precedent claims, counter-evidence and the novelty class against what the module already holds)

## C1 CARD-H1-01
- compound_or_probe: Tiratricol with liothyronine as comparator and sobetirome as isoform control (module identifiers CHEMBL41632, CHEMBL1544, CHEMBL107400); a ligand of a process, not a supplementation proposal
- action: Required: more thyroid-receptor activation in oligodendrocyte-lineage cells, only if the block is receptor-limited. Documented elsewhere: a thyromimetic normalised callosal myelin staining and interneuron differentiation in a hormone-transport-deficit mouse only when started in the first postnatal weeks (module N01, N02; abstract and partial text). Documented in WWOX material: nothing
- context: Cell-level: seizure-free DRG neuron plus OPC co-culture (medium with B27 and N2, forskolin and N-acetyl-cysteine) and the oligocortical spheroid (T3 supplement Day 60 to 70 then B27 base); in vivo only after a null-specific dish result
- hypothesised_benefit: Differentiation of the oligodendroglial lineage (stage shares) and, if wrapping or EM is read, sheath formation. Conduction, network activity, development and quality of life are not addressed by any step. Kind of value if it works: compensation or partial release of the observed block; not recovery of WWOX function
- wwox_starting_observation: Fewer myelinating-class cells on null neurons in the co-culture; stage pattern in the neuron-targeted deletion; knockout spheroids stay hypomyelinated after a T3 supplement given to every spheroid (media row Day 60 to 70); bulk Hr and Dio3 transcripts lower in several contrasts (evidence T01, T02), a composition-confounded descriptive lead; neuron-like nuclei show flat Hr, Klf9 and Thrb per nucleus (G05, one pool)
- external_precedent: PMID36834863 and PMID37765015 (partial full text, module N01 to N04); PMID37307933 (abstract only, stage pattern); zebrafish T3 and analogue result (module N14) conflicts with the mouse late-start result
- inferred_steps: (1) the dish is not hormone-free: B27 may carry T3 at an unknown level and OPCs pass through serum; (2) the block is receptor-limited rather than cue- or activity-limited; (3) transfer of the early-window effect from a transport defect to a WWOX defect
- identity_and_action: Tiratricol and DITPA activate thyroid receptors without MCT8-dependent entry (source: introduction of PMID36834863, module N-rows); liothyronine is the natural ligand; sobetirome is receptor-beta-leaning and the isoform dispute is unsettled (open question OQ2). In a dish whose neurons and glia have intact transporters liothyronine already tests receptor responsiveness; tiratricol adds information only if transport is limiting. Nuclear data show Slc16a2 and Slco1c1 transcripts present (G05), which is not transport function
- comparator: Genotype (null and wild-type neurons) by medium baseline (complete medium with T3 measured; a defined B27-free arm only once its hormone content is known) by ligand class by vehicle; fixed-null-neuron, activity-block and non-receptor-enhancer arms from INV06 X1 to X3 as mechanism and functional comparators; receptor-target transcript in OPCs as engagement. Reading: improvement in both genotypes equals generic maturation (weakens WWOX-specific attribution, does not by itself exclude a partial benefit); improvement toward wild-type level in the null arm only equals compensation or recovery of the dish defect; attribution to the receptor needs engagement plus the isoform control
- main_counterevidence: No WWOX-side hormone deficit is shown; knockout spheroid hypomyelination persists with T3 supplied in both arms (it may be receptor-unresponsive, or limited elsewhere); late start failed in the model and nulls live 3 to 4 weeks; seizure effect of thyromimetics mixed; T3 failed under a cytokine block in vitro (module N08); the bulk hormone-axis lowering fits oligodendrocyte depletion equally
- result_that_would_weaken_it: Equal effect in both genotypes; no effect once medium T3 is measured and engagement is shown; effect only when B27 is removed (medium artefact); receptor-target transcripts not lower in null OPCs
- next_experiment: Step 0 before any ligand: measure total and free T3 and T4 in complete co-culture and spheroid medium and in B27 and N2 stock dilutions (a measurement, not described as done); then INV-12 with a measured baseline
- consequence_for_existing_investigation: INV-12: add the medium measurement as step 0; the 'against hormone-depleted medium' arm is not executable with B27 and N2 until the baseline is known (a defined medium without B27 would change the neurons as well); a null result in complete medium may reflect a ceiling; liothyronine is the primary comparator, tiratricol the transport-independent one; INV-06 E12 narrowed (consumer_delta.md). Stays conditional, rank unchanged
- novelty_class: already_in_legend

## C2 CARD-H2-01
- compound_or_probe: L-lactate as a process probe (module catalogue entry CAT:EC:01903, no status statement) with a lactate-transport blocker chosen only after a source describing it is read; not a supplementation proposal
- action: Required: higher glucose or lactate availability to the oligodendrocyte lineage, only if the null-neuron dish is supply-limited. Documented elsewhere: low glucose lowered oligodendrocyte-lineage number in cortical slices and lactate rescued it (module N12, abstract); early lactate partly rescued motor deficits in a Glut1-deficient mouse (symptom, not myelin; module C12). Documented in WWOX material: nothing at the oligodendrocyte
- context: Co-culture base medium and conditioned or fixed-neuron variants (INV06 X1); the glucose value of the DMEM and Neurobasal media is not determinable from the sources read (media rows)
- hypothesised_benefit: Oligodendroglial differentiation and wrapping in the dish if supply-limited; not conduction, network activity or development. A symptom response in a Glut1 model does not carry to myelin
- wwox_starting_observation: Systemic hypoglycaemia in the null from week 2 and bundled rescue with neuronal restoration; but the dish deficit arises where systemic glucose cannot act; WWOX-side lactate points up not down; bulk glycolytic transcripts move with mixed signs (T04); Slc16a1 and Slc2a1 are detectable in only a handful of oligodendroglial nuclei per arm (G06)
- external_precedent: Module N12, N13 (abstract only), C10 to C12; the fly neuronal wwox knockdown paper with raised lactate (abstract only, found by the module's auditor)
- inferred_steps: (1) null neurons consume or release differently from wild type; (2) the oligodendrocyte-lineage deficit tracks that difference; (3) added lactate reaches the oligodendrocyte through MCT1 and is used
- identity_and_action: L-lactate as a metabolite substrate and, in the cited slice work, an MCT1-carried one; a transporter transcript measures neither uptake nor flux, and metabolite abundance in another organism does not decide energy supply to oligodendrocytes
- comparator: Null and wild-type DRG at matched axon density: glucose consumption, lactate release and respiration or acidification in the same base medium (EX6) before any lactate arm; then EX7 with glucose and lactate arms, fixed neurons and activity block; separate generic effect (both genotypes), compensation (null toward wild-type) and cue-versus-supply attribution (conditioned medium and transwell)
- main_counterevidence: WWOX-side lactate is up and a supply deficit would predict down; the medium may already be glucose-rich (unread); acid load in the dish; the lactate-rescue literature is abstract-level
- result_that_would_weaken_it: Null and wild-type neurons show the same consumption and release in the medium and the energy arms leave the deficit unchanged; fixed null neurons reproduce the deficit
- next_experiment: Read the vendor formulation of the DMEM and Neurobasal codes for glucose (the study prints no DMEM code; the protocol paper prints one cut-off code) and record the value; then EX6
- consequence_for_existing_investigation: EX6 and EX7 unchanged in design; add the medium glucose value as a precondition; the energy thread stays two conditional arms with no compound sustained
- novelty_class: already_in_legend

## C3 CARD-H2-02
- compound_or_probe: Dichloroacetate and PDK inhibition (module investigation INV-07), as the lever of the energy thread's second arm only; pharmacology as stated in INV-07, not re-read here
- action: Required: lower glycolytic output or more oxidative use, only if a PDH block exists in null neurons. Documented in this module: no PDH block shown in a WWOX-deficient human neural cell; no myelin-specific source read in this package
- context: Cultured neurons or neural cells; the myelin link would run through the co-culture arms
- hypothesised_benefit: Not stated; at most a conditional route to less glycolytic overflow. No oligodendroglial or myelin endpoint is supported
- wwox_starting_observation: Bulk descriptive transcripts: Pdk2 higher in S-KO and N-KO hippocampus (109.62 against 83.27 and 109.44 against 81.31 TPM) while Pdk4 is lower in the null (T04); direction mixed and not a PDH measurement
- external_precedent: none read for myelin in this package
- inferred_steps: (1) PDH is inhibited in null neurons; (2) lowering lactate output helps the oligodendrocyte lineage; (3) transfer from non-myelin systems
- identity_and_action: A PDK inhibitor raises pyruvate dehydrogenase activity; the target-direction question is INV-07's own
- comparator: Not designed here: INV-07's premise measurement (PDH activity and flux with lactate and pyruvate measured directly, per its IT36 note) is the comparator step; the co-culture arm would follow only if that premise holds
- main_counterevidence: No myelin-specific source; WWOX-side lactate is up, which fits the arm only if flux is reversed; acid and metabolic effects not examined
- result_that_would_weaken_it: No PDH block in null neurons, or flux unchanged
- next_experiment: INV-07 premise measurement as already specified
- consequence_for_existing_investigation: INV-07 unchanged; this card only records that the energy thread's second arm depends on that premise; not carried as a lever
- novelty_class: already_in_legend
