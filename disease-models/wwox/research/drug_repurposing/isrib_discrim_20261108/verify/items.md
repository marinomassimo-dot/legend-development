# Items for a blind audit (Package A)

Check each item against the named source (open routes only; the PMC XML of PMID 23741617 can be fetched with NCBI efetch db=pmc; held text under /home/desktop/legend-development/files/ if any). Verdicts: SUPPORTED / OVERSHOOT / UNDERSHOOT / NOT_IN_SOURCE / UNVERIFIABLE, with the verbatim locator and depth reached. Figure images: look at them if you can reach them without a challenge, otherwise say 'caption only'.

# Part 1: phospho-site rows

## PS1 the measured band (tunicamycin panel)
- system_species: human HEK293T cells (Methods, Cell culture list; the figure supplement caption names HEK293T)
- construct: none stated: endogenous protein; no tag, no mutant and no isoform named in the text read
- numbering_used: S539 (the label in caption, Discussion, decision-letter reply and antibody name)
- numbering_source: not stated in the paper as a numbering convention; the Discussion attributes the site to the 2012 TLR paper (Woo et al.); that paper, in the text retrieved, calls the site Ser GSK and gives no number
- antibody: phospho-S539 eIF2Bepsilon, 1/1000, Abcam (Methods antibody list); catalogue number not given; total eIF2Bepsilon: Santa Cruz B-7, 1/500
- epitope_documented: No. The paper gives no immunogen, no peptide sequence, no catalogue number, no validation (no phosphatase, no Ser-to-Ala lane). Supplier data sheet not reached (see queries.tsv Q07)
- residue_identified_as: undetermined
- correspondence_in_residues_tsv: Human Q13144: residue 539 is Asp (positions 531-548 read QSMDSEEPDSRGGSPQMD: 539 D, 540 S, 544 S); so S539 is not a human serine. The GSK3 serine is human Ser540 and the priming serine human Ser544; rat Ser535 and Ser539; mouse 536 and 540; rabbit 540 and 544. The label S539 matches a serine only at the rat or hamster priming position (rows 7 and 5 of residues.tsv)
- caption_says: Caption: "phospho S539-eIF2Bε and total eIF2Bε in HEK293T cells treated with or without 2 µg/ml of tunicamycin or 100 nM thapsigargin" and, in the same sentence, "in the presence or absence of 200 nM ISRIB". Discussion: ISRIB "did not reduce phosphorylation of S539 in the eIF2B ε-subunit"
- image_shows: Figure 3 figure supplement 1, viewed as a 447 x 228 pixel image (the only size reachable): left panel is tunicamycin (lanes control, ISRIB, Tm 1 to 4 h, Tm+ISRIB 1 to 4 h) with rows PERK, XBP1s, ATF4, phospho S51 eIF2alpha, total eIF2alpha, phospho S539 eIF2Bepsilon, total eIF2Bepsilon (both near 70 kD). The phospho-S539 band is present in every lane and I could not see a change between lanes at this resolution; this is a visual impression, not a measurement
- controls: ISRIB-alone and untreated lanes are present; total eIF2Bepsilon row is the loading comparator; no peptide competition, phosphatase or mutant control in the image; no phospho-protein positive control that moves
- limit: no quantification, no replicate number for this blot in the text or caption; one experiment shown; image resolution does not allow a densitometry judgement; direction stated is "not reduced" (the text does not say unchanged or increased)
- status: site_identification: undetermined. Measurement exists (HEK293T, ER stress, ISRIB present, band not reduced). Missing to settle it: the Abcam catalogue number and its immunogen sequence (does it contain the DSRAGS window, and which serine carries the phosphate); whether the supplier numbering is rat (then the antibody reads the priming serine) or another; any phosphatase or point-mutant validation of that antibody

## PS2 the thapsigargin panel
- system_species: same
- construct: none
- numbering_used: S539 in the caption
- numbering_source: as PS1
- antibody: as PS1
- epitope_documented: as PS1
- residue_identified_as: not applicable: no band
- correspondence_in_residues_tsv: not applicable
- caption_says: The caption lists phospho S539 eIF2Bepsilon and phospho S51 eIF2alpha among blots for cells treated with tunicamycin or thapsigargin
- image_shows: Right panel (thapsigargin; lanes control, ISRIB, Tg 1 to 4 h, Tg+ISRIB 1 to 4 h) shows rows PERK, XBP1s, ATF4 and total eIF2alpha only; no phospho S539 or total eIF2Bepsilon row is drawn in that panel
- controls: as PS1
- limit: the S539 result rests on the tunicamycin panel alone although the caption suggests both stressors; the Discussion sentence is supported by one stressor only
- status: observed_mismatch

## PS3 what the cited work says about S539
- system_species: rat (rat eIF2Bepsilon in vitro and cells; Woods 2001, Wang 2001)
- construct: recombinant and cellular rat protein
- numbering_used: Ser539 and Ser535 (rat numbering)
- numbering_source: Woods 2001 abstract; Wang 2001 abstract (both abstract level)
- antibody: not applicable to these papers as read (abstracts)
- epitope_documented: not applicable
- residue_identified_as: Ser539 = the DYRK2/DYRK1A priming site, followed by proline; Ser535 = the GSK3 site; GSK3 needs Ser539 phosphorylated first
- correspondence_in_residues_tsv: row 7 (priming, rat 539 / human 544) and row 2 (GSK3 site, rat 535)
- caption_says: Woods 2001 abstract: eIF2Bepsilon "is highly phosphorylated at Ser(539) in vivo"; Wang 2001 abstract: "GSK3 is responsible for phosphorylating Ser535"
- image_shows: not applicable (no image read)
- controls: not applicable
- limit: abstract level only; the rat numbering in these papers fixes S539 as the priming serine, not as the GSK3 serine
- status: DATO

## PS4 the other numbering for the GSK3 serine
- system_species: rabbit eIF2B and CHO cells (Welsh 1998)
- construct: native or recombinant, as in the paper (abstract level)
- numbering_used: Ser540
- numbering_source: Welsh 1998 abstract
- antibody: not applicable
- epitope_documented: not applicable
- residue_identified_as: GSK3 site, numbered 540 in that work
- correspondence_in_residues_tsv: row 5 (rabbit 540) and row 3 (human 540)
- caption_says: Welsh 1998 abstract: "we identify the phosphorylation site in eIF2Bepsilon as Ser540"
- image_shows: not applicable
- controls: not applicable
- limit: abstract level; this numbering equals the human numbering, so a reader meeting "Ser540" and "Ser535" and "S539" has three labels for two serines
- status: DATO

## PS5 how the 2012 TLR paper names the site
- system_species: mouse macrophages and MEFs; human or rat constructs (Woo 2012)
- construct: S-A and S-D point mutants of the GSK site and of an upstream DYRK-dependent serine, human and rat constructs
- numbering_used: Ser GSK (no residue number in the text retrieved)
- numbering_source: cites Welsh 1998 and Wang and Proud 2008 for the site
- antibody: p-eIF2Bepsilon antibody not named in the text retrieved (the Methods section is not in the retrieved text)
- epitope_documented: No
- residue_identified_as: the GSK3 site, described with an upstream DYRK-primed serine
- correspondence_in_residues_tsv: row 2 and row 7
- caption_says: not applicable
- image_shows: Figures not viewed (captions only)
- controls: immunoblot panels with n = 3 and densitometry in the captions
- limit: the paper the 2013 text relies on gives no residue number in the retrieved text, so it does not settle which numbered residue the Abcam antibody reads
- status: observed_gap

## PS6 drift of the label in later literature
- system_species: human and mouse cells (PMC9462064, a 2022 article)
- construct: none
- numbering_used: S539 used for the inhibitory site
- numbering_source: one introductory sentence only
- antibody: not applicable
- epitope_documented: not applicable
- residue_identified_as: used as the inhibitory (GSK3) serine
- correspondence_in_residues_tsv: not applicable
- caption_says: "Decreased phosphorylation of eIF2Bϵ at S539 increases the GDP/GTP exchange activity of eIF2B"
- image_shows: not applicable
- controls: not applicable
- limit: shows that S539 is read in the field as the inhibitory serine; this does not fix what the antibody binds; a citation habit, not an experiment
- status: context

# Part 2: new-read evidence rows

## EN01
- source_id: 23741617
- evidence_class: ISRIB first report (reread for the phospho-site question)
- system: human HEK293T cells
- perturbation: antibody list in Methods
- cell_stage: cell line
- level: 2
- finding: The phospho-epsilon blot used an Abcam phospho-S539 eIF2Bepsilon antibody (no catalogue number) and a Santa Cruz B-7 total eIF2Bepsilon antibody.
- locator_quote: phospho-S539 eIF2Bε (1/1000) (Abcam)
- depth_reached: partial_fulltext (PMC record through NCBI efetch XML: Methods, Results, Discussion, the decision-letter text inside the record and figure captions read; one figure image viewed, Figure 3 figure supplement 1 at 447 x 228 pixels; other figures captions only; supplements none)
- limits: no immunogen, no validation, no catalogue number in the text
- role: context

## EN02
- source_id: 23741617
- evidence_class: ISRIB first report
- system: HEK293T, tunicamycin panel
- perturbation: ISRIB 200 nM with or without tunicamycin
- cell_stage: cell line
- level: 2
- finding: The authors state that ISRIB did not reduce phosphorylation of S539 of eIF2Bepsilon and conclude that ISRIB does not use this phosphorylation to raise GEF activity; direction is "not reduced" only.
- locator_quote: ISRIB did not reduce phosphorylation of S539 in the eIF2B ε-subunit
- depth_reached: partial_fulltext (PMC record through NCBI efetch XML: Methods, Results, Discussion, the decision-letter text inside the record and figure captions read; one figure image viewed, Figure 3 figure supplement 1 at 447 x 228 pixels; other figures captions only; supplements none)
- limits: one blot, no quantification and no replicate number stated; the sentence is in the Discussion; the site identity is undetermined (phosphosite.tsv PS1)
- role: context

## EN03
- source_id: 23741617
- evidence_class: ISRIB first report, decision-letter reply inside the PMC record
- system: HEK293T
- perturbation: reviewer request for phospho-eIF2B readouts
- cell_stage: cell line
- level: 2
- finding: The authors queried one site with a commercial antibody and gloss it as constitutively GSK-phosphorylated and inhibitory; they state no other commercial phospho-specific eIF2B antibodies exist.
- locator_quote: This site is constitutively phosphorylated by GSK and negative regulates eIF2B activity.
- depth_reached: partial_fulltext (PMC record through NCBI efetch XML: Methods, Results, Discussion, the decision-letter text inside the record and figure captions read; one figure image viewed, Figure 3 figure supplement 1 at 447 x 228 pixels; other figures captions only; supplements none)
- limits: a reply letter, not a Methods or Results statement; the gloss attributes the S539 label to GSK, whereas rat Ser539 is the DYRK priming site (EN08)
- role: context

## EN04
- source_id: 23741617
- evidence_class: ISRIB first report, Figure 3 figure supplement 1 image against its caption
- system: HEK293T
- perturbation: tunicamycin and thapsigargin panels
- cell_stage: cell line
- level: 2
- finding: The image shows phospho S539 and total eIF2Bepsilon rows only in the tunicamycin panel; the thapsigargin panel carries PERK, XBP1s, ATF4 and total eIF2alpha rows only.
- locator_quote: phospho S539-eIF2Bε and total eIF2Bε in HEK293T cells treated with or without 2 µg/ml of tunicamycin or 100 nM thapsigargin
- depth_reached: partial_fulltext (PMC record through NCBI efetch XML: Methods, Results, Discussion, the decision-letter text inside the record and figure captions read; one figure image viewed, Figure 3 figure supplement 1 at 447 x 228 pixels; other figures captions only; supplements none)
- limits: resolution does not allow judging band intensities; my reading of the image is not a quantification
- role: limit

## EN05
- source_id: 22231169
- evidence_class: TLR-eIF2B paper (Woo 2012)
- system: mouse macrophages and MEFs
- perturbation: LPS before tunicamycin
- cell_stage: primary cells and cell line
- level: 2
- finding: The 2012 paper names the inhibitory serine Ser GSK, not by number, and reports that LPS partly lowers pSer GSK-eIF2Bepsilon in a TRIF-dependent way.
- locator_quote: LPS pre-treatment partially decreased the pSer GSK -eIF2Bε
- depth_reached: partial_fulltext (PMC XML through NCBI efetch: Results and figure captions read; the Methods section is not in the retrieved text; figures captions only)
- limits: antibody not named in the retrieved text; no residue number in the retrieved text
- role: context

## EN06
- source_id: 22231169
- evidence_class: TLR-eIF2B paper (Woo 2012)
- system: mouse macrophages and MEFs
- perturbation: LPS; PI3-kinase inhibitor
- cell_stage: primary cells and cell line
- level: 2
- finding: In this system a drop in GSK3 activity was tested as the explanation for the lower phospho-site and excluded for LPS: the inactive phospho-GSK3beta form did not rise and the PI3-kinase inhibitor did not prevent CHOP suppression. A phosphatase route (PP2A) was found instead.
- locator_quote: we found that LPS did not increase the inactive phosphorylated form of GSK3β
- depth_reached: as EN05
- limits: shows the site can be removed without GSK3 inactivation in macrophages; not a statement about neurons or WWOX; one cell context
- role: counter

## EN07
- source_id: 22231169
- evidence_class: TLR-eIF2B paper (Woo 2012)
- system: MEFs with Eif2be silencing and human construct
- perturbation: S-A and S-D mutants of the GSK site and the upstream DYRK-dependent serine
- cell_stage: cell line
- level: 3
- finding: A construct with Ser-to-Ala at both serines lowered CHOP under tunicamycin and LPS gave no further fall; the Ser-to-Asp (phospho-mimetic) construct did not restore the LPS effect.
- locator_quote: using S-D mutants to mimic constitutive phosphorylation, we showed that transfection with S-D GSK/DYRK EIF2BE did not restore LPS-induced CHOP suppression
- depth_reached: as EN05
- limits: the readout is CHOP, an ISR output, not translation; double mutant (GSK and DYRK sites together), so it does not separate the two serines; a phospho-mimetic here behaved as no more than a non-restoring control
- role: support

## EN08
- source_id: 11311121
- evidence_class: DYRK priming paper (Woods 2001), abstract
- system: rat eIF2Bepsilon, recombinant and cellular
- perturbation: kinase assays in vitro
- cell_stage: in vitro
- level: 2
- finding: Rat Ser539 is phosphorylated by DYRK2 and DYRK1A, permits GSK3 to phosphorylate Ser535 in vitro and is highly phosphorylated in vivo.
- locator_quote: eIF2Bepsilon is highly phosphorylated at Ser(539) in vivo
- depth_reached: abstract_only (PubMed record through the PubMed tools)
- limits: abstract only; fixes rat Ser539 as the priming serine; the paper was not read for methods
- role: support

## EN09
- source_id: 11500362
- evidence_class: eIF2Bepsilon phosphorylation sites (Wang 2001), abstract
- system: rat and human eIF2Bepsilon
- perturbation: kinase and mutant work
- cell_stage: cells and in vitro
- level: 2
- finding: GSK3 phosphorylates Ser535 and the event needs Ser539 and a distal recruitment region; five sites are phosphorylated in the complex in vivo.
- locator_quote: Glycogen synthase kinase 3 (GSK3) is responsible for phosphorylating Ser535.
- depth_reached: abstract_only (PubMed record through the PubMed tools)
- limits: abstract only; species mix not resolvable from the abstract
- role: support

## EN10
- source_id: 9468292
- evidence_class: GSK3 site discovery (Welsh 1998), abstract
- system: rabbit eIF2B and CHO cells
- perturbation: GSK3 treatment of eIF2B; insulin
- cell_stage: in vitro and cell line
- level: 2
- finding: The same GSK3 serine was first numbered 540; treating eIF2B with GSK3 inhibited its activity and the site was dephosphorylated by insulin.
- locator_quote: Here we identify the phosphorylation site in eIF2Bepsilon as Ser540
- depth_reached: abstract_only (PubMed record through the PubMed tools)
- limits: abstract only
- role: support

## EN11
- source_id: 36091130
- evidence_class: 2022 article using the label (Europe PMC search hit, one sentence read)
- system: human and mouse cells
- perturbation: none (introductory statement)
- cell_stage: not applicable
- level: 2
- finding: A later article writes S539 as the inhibitory phosphorylation site of eIF2Bepsilon.
- locator_quote: Decreased phosphorylation of eIF2Bϵ at S539 increases the GDP/GTP exchange activity of eIF2B
- depth_reached: partial_fulltext (PMC XML through NCBI efetch, one introductory passage found by keyword; the rest not read)
- limits: citation habit; not an experiment on the antibody
- role: context

## EN12
- source_id: 16959561
- evidence_class: commentary on GSK3 and TSC2 (Choo 2006), abstract
- system: mammalian cells (commentary on Inoki 2006)
- perturbation: none (commentary)
- cell_stage: cell lines
- level: 3
- finding: GSK3 and AMPK cooperate to activate TSC2 and so inhibit mTOR; Wnt signalling suppresses the GSK3 phosphorylation of TSC2. A GSK3 substrate with a documented role in protein synthesis other than eIF2Bepsilon.
- locator_quote: the kinases GSK3 and AMPK cooperate in the activation of TSC2 to inhibit mTOR activity
- depth_reached: abstract_only (PubMed record through the PubMed tools; the commentary, not the primary Inoki paper)
- limits: commentary abstract; the primary paper was not read; direction on translation in neurons not shown
- role: counter

## EN13
- source_id: 18160716
- evidence_class: amino-acid control of eIF2B (Wang and Proud 2008), abstract
- system: human cells
- perturbation: amino acid deprivation
- cell_stage: cell lines
- level: 2
- finding: eIF2Bepsilon carries another regulated serine (Ser525) whose phosphorylation controls eIF2B independently of eIF2 phosphorylation and of mTORC1; an epsilon-site input other than the GSK3 serine.
- locator_quote: We identify this site as Ser525, located adjacent to the known phosphoregulatory region in eIF2Bepsilon.
- depth_reached: abstract_only (PubMed record through the PubMed tools); opened as the seventh source beyond the module, one over the cap of six
- limits: abstract only; shows another epsilon site exists, nothing about WWOX or neurons
- role: context

# Part 3: evidence-level assignments

## EI13
- claim: ISRIB sits at the interface of the beta and delta regulatory subunits of human eIF2B
- level: 1
- source_id: 29599245
- system: endogenous human eIF2B, cryo-EM
- locator_quote_max25words: ISRIB molecule bound at the interface between the β and δ regulatory subunits
- depth: full text of the PMC record, figure images not viewed (module)
- what_it_does_not_show: binding to the epsilon subunit or to its GSK3 serine; any effect on activity

## EI18
- claim: The catalytic HEAT domain of epsilon is unresolved in the ISRIB-bound structure
- level: 1
- source_id: 29599213
- system: recombinant human decamer, cryo-EM
- locator_quote_max25words: the catalytic HEAT domains of the ε subunits were not resolved
- depth: as EI13
- what_it_does_not_show: that ISRIB does not touch epsilon: absence of density only

## EI08
- claim: ISRIB stabilises active eIF2B dimers and the delta subunit contributes to its site
- level: 2
- source_id: 25875391
- system: human eIF2B, cells and in vitro
- locator_quote_max25words: show ISRIB-mediated stabilization of activated eIF2B dimers, and suggest that eIF2B4 (δ-subunit) contributes to the ISRIB binding site
- depth: partial (module)
- what_it_does_not_show: translation or any GSK3-site effect

## EI16
- claim: ISRIB promotes decamer assembly by bridging the symmetry interface
- level: 2
- source_id: 29599213
- system: recombinant human tetramers
- locator_quote_max25words: ISRIB promoted this step by cross-bridging a central symmetry interface
- depth: as EI13
- what_it_does_not_show: activity in cells

## EI17
- claim: Assembly effect is bell-shaped in the tetramer system
- level: 2
- source_id: 29599213
- system: recombinant human tetramers
- locator_quote_max25words: ISRIB promoted eIF2B(βγδε)2 assembly at 1 μM but failed to do so at 10 μM
- depth: as EI13
- what_it_does_not_show: any other preparation; a one-concentration arm can miss it

## EI10
- claim: Stimulation of exchange depends on the ratio of phosphorylated to unphosphorylated eIF2
- level: 2
- source_id: 25875391
- system: partially purified rabbit eIF2B, in vitro
- locator_quote_max25words: hardly any stimulation at the 1:1 ratio
- depth: partial (module)
- what_it_does_not_show: what happens in a cell with its own ratio

## EI11
- claim: Exchange was threefold faster with ISRIB in the partly purified system without phospho-eIF2
- level: 2
- source_id: 25875391
- system: partially purified rabbit eIF2B, in vitro
- locator_quote_max25words: GDP release was threefold faster upon addition of ISRIB
- depth: as EI10
- what_it_does_not_show: that the recombinant human decamer behaves so (EI15 differs)

## EI15
- claim: The recombinant decamer was not significantly activated by ISRIB
- level: 2
- source_id: 29599213
- system: recombinant human decamer, in vitro
- locator_quote_max25words: ISRIB did not significantly activate the recombinant eIF2B decamer
- depth: as EI13
- what_it_does_not_show: that cells without phospho-eIF2 are unaffected (EI11 and EI26 disagree)

## E21
- claim: Without phospho-eIF2 ISRIB only minimally accelerated exchange
- level: 2
- source_id: 33220178
- system: recombinant human eIF2B, in vitro
- locator_quote_max25words: ISRIB only minimally accelerated the exchange of nucleotide mediated by eIF2B in an assay devoid of eIF2(αP)
- depth: partial (module)
- what_it_does_not_show: a phospho-epsilon lesion: wild-type enzyme only

## EI28
- claim: The in vitro acceleration is seen preferentially with phospho-eIF2
- level: 2
- source_id: 33220178
- system: recombinant human eIF2B and CHO cells
- locator_quote_max25words: ISRIB-mediated acceleration of eIF2B’s nucleotide exchange activity in vitro is observed preferentially in the presence of eIF2(αP)
- depth: partial (module)
- what_it_does_not_show: exclusivity: the word is preferentially

## EI29
- claim: ISRIB restores the activity of destabilised vanishing-white-matter mutant decamers
- level: 2
- source_id: 29489452
- system: recombinant mutants and HEK293T lines
- locator_quote_max25words: ISRIB stabilizes VWMD mutant eIF2B in the decameric form and restores the residual catalytic activity to wild-type levels
- depth: partial (module)
- what_it_does_not_show: a lesion by phosphorylation; that rescued mutants lie near the GSK3 serine (they do not, module audit)

## E05
- claim: GSK3 inhibitors dephosphorylate the GSK3 serine of epsilon in hamster cells [GSK3-site axis]
- level: 2
- source_id: 12133000
- system: CHO cells
- locator_quote_max25words: which strongly indicates that this site is indeed a target for GSK3 in vivo
- depth: abstract only (module)
- what_it_does_not_show: translation, or any ISRIB interaction

## E06
- claim: Dephosphorylation of that serine did not significantly activate eIF2B [GSK3-site axis]
- level: 2
- source_id: 12133000
- system: CHO cells
- locator_quote_max25words: these compounds did not elicit significant activation of eIF2B
- depth: abstract only (module)
- what_it_does_not_show: why: additional inputs are named, not shown

## EN08
- claim: Rat Ser539 is the DYRK priming serine; Ser535 the GSK3 serine [GSK3-site axis]
- level: 2
- source_id: 11311121
- system: rat eIF2Bepsilon, in vitro and in vivo
- locator_quote_max25words: eIF2Bepsilon is highly phosphorylated at Ser(539) in vivo
- depth: abstract only (new read)
- what_it_does_not_show: human numbering; any ISRIB effect

## EN10
- claim: The GSK3 serine is Ser540 in the rabbit numbering [GSK3-site axis]
- level: 2
- source_id: 9468292
- system: rabbit eIF2B, CHO cells
- locator_quote_max25words: Here we identify the phosphorylation site in eIF2Bepsilon as Ser540
- depth: abstract only (new read)
- what_it_does_not_show: which numbering the S539 antibody uses

## EN02
- claim: ISRIB did not reduce a phospho-S539 epsilon signal under ER stress [GSK3-site axis, site undetermined]
- level: 2
- source_id: 23741617
- system: HEK293T cells, one blot
- locator_quote_max25words: ISRIB did not reduce phosphorylation of S539 in the eIF2B ε-subunit
- depth: partial_fulltext (new reread, one image viewed)
- what_it_does_not_show: that the GSK3 serine is unchanged: the site is undetermined and the blot is unquantified

## EN05
- claim: LPS lowers pSer GSK-eIF2Bepsilon in macrophages [GSK3-site axis]
- level: 2
- source_id: 22231169
- system: mouse macrophages and MEFs
- locator_quote_max25words: LPS pre-treatment partially decreased the pSer GSK -eIF2Bε
- depth: partial_fulltext (new read)
- what_it_does_not_show: GSK3 involvement: a phosphatase route is shown (EN06)

## EN13
- claim: Another epsilon serine (Ser525) controls eIF2B separately from eIF2 phosphorylation
- level: 2
- source_id: 18160716
- system: human cells
- locator_quote_max25words: We identify this site as Ser525, located adjacent to the known phosphoregulatory region in eIF2Bepsilon.
- depth: abstract only (new read, one over the source cap)
- what_it_does_not_show: relevance to WWOX or neurons

## EI03
- claim: Reporter potency of the trans isomer in the ATF4 luciferase cell reporter
- level: 3
- source_id: 23741617
- system: HEK293T ATF4-luciferase reporter
- locator_quote_max25words: Trans-ISRIB proved 100-fold more potent (IC50 = 5 nM) than cis-ISRIB (IC50 = 600 nM)
- depth: partial_fulltext (module)
- what_it_does_not_show: a molecular step: a reporter output is pharmacodynamic

## EI04
- claim: ISRIB did not block phosphorylation of eIF2alpha under ER stress
- level: 3
- source_id: 23741617
- system: U2OS (assay), HEK293T (blot)
- locator_quote_max25words: ISRIB did not block eIF2α phosphorylation under either of these ER stress-inducing conditions.
- depth: partial_fulltext (module)
- what_it_does_not_show: translation as such; phospho-eIF2alpha rose further at 120 min with tunicamycin and ISRIB

## EI05
- claim: ISRIB did not reverse the translation block of Torin-1
- level: 3
- source_id: 23741617
- system: mouse embryonic fibroblasts
- locator_quote_max25words: addition of ISRIB did not reverse the effect of Torin-1 on translation
- depth: partial_fulltext (module)
- what_it_does_not_show: neurons; mTORC1-specific effects (Torin-1 acts on mTOR kinase)

## EI22
- claim: In rat cortical cultures ISRIB did not lower ATF4 under thapsigargin
- level: 3
- source_id: 32457286
- system: primary rat cortical neurons versus HEK293
- locator_quote_max25words: unlike in HEK293 cells, ISRIB did not reduce ATF4 expression in Thap-treated neuronal cultures
- depth: partial_fulltext (module)
- what_it_does_not_show: that ATF4 fails to follow ISRIB elsewhere (it followed in mouse hippocampus, EI27)

## EI25
- claim: ISRIB corrected amyloid-oligomer driven fall in protein synthesis in slices
- level: 3
- source_id: 33531382
- system: mouse hippocampal slices, SUnSET
- locator_quote_max25words: ISRIB corrects AβO-instigated eIF2α-P-dependent hippocampal translational repression
- depth: partial_fulltext (module)
- what_it_does_not_show: a repair of an eIF2B lesion; the repression is phospho-eIF2alpha-driven

## EI26
- claim: No noticeable effect in wild-type mice under that regimen
- level: 3
- source_id: 33531382
- system: wild-type mice, one low-exposure regimen
- locator_quote_max25words: without noticeable biochemical or cognitive effects in WT control mice
- depth: partial_fulltext (module)
- what_it_does_not_show: that ISRIB is inert at basal state: the same paragraph cites an effect at a higher single exposure

## EI27
- claim: ISRIB did not prevent the salubrinal-induced rise of phospho-eIF2alpha but blocked ATF4 accumulation
- level: 3
- source_id: 33531382
- system: mouse hippocampus
- locator_quote_max25words: ISRIB did not prevent the increase in hippocampal eIF2α-P caused by salubrinal administration in mice
- depth: partial_fulltext (module)
- what_it_does_not_show: protein synthesis

## EI24
- claim: ISRIB antagonises the ISR only below a threshold of phospho-eIF2alpha (cited, not read)
- level: 3
- source_id: 29489452 citing Rabouw
- system: review of cited finding
- locator_quote_max25words: ISRIB antagonizes the ISR only when p-eIF2α levels are below a critical threshold
- depth: citing_primary in 32457286 (module)
- what_it_does_not_show: the primary paper was not read

## E07
- claim: The GSK3 inhibitors used change overall protein synthesis apart from GSK3
- level: 3
- source_id: 12133000
- system: CHO cells
- locator_quote_max25words: each of the inhibitors used affects overall protein synthesis
- depth: abstract only (module)
- what_it_does_not_show: which substrates mediate it

## E15
- claim: The translation gain from Gsk3b deletion was largely negated by catalytically dead epsilon
- level: 3
- source_id: 26974342
- system: mouse retinal ganglion cells in vivo
- locator_quote_max25words: Gsk3b deletion resulted in a significant increase in OPP-labeled new synthesized proteins, which was largely negated by eIF2Bε E572A treatment
- depth: partial_fulltext (module)
- what_it_does_not_show: exchange activity (a labelling assay); overexpressed mutant; adult neuron

## E16
- claim: The phospho-resistant epsilon raised protein synthesis
- level: 3
- source_id: 26974342
- system: mouse retinal ganglion cells in vivo
- locator_quote_max25words: expression of eIF2Bε S535A significantly increased protein synthesis in RGCs
- depth: partial_fulltext (module)
- what_it_does_not_show: that the mutant is constitutively active (cited, not measured)

## EN07
- claim: Ser-to-Ala at the GSK and DYRK serines lowered CHOP; the Ser-to-Asp form did not restore the LPS effect
- level: 3
- source_id: 22231169
- system: MEFs, human construct
- locator_quote_max25words: using S-D mutants to mimic constitutive phosphorylation, we showed that transfection with S-D GSK/DYRK EIF2BE did not restore LPS-induced CHOP suppression
- depth: partial_fulltext (new read)
- what_it_does_not_show: translation; separation of the two serines

## EN12
- claim: GSK3 phosphorylation of TSC2 restrains mTOR, a translation regulator other than eIF2B
- level: 3
- source_id: 16959561
- system: mammalian cells (commentary)
- locator_quote_max25words: the kinases GSK3 and AMPK cooperate in the activation of TSC2 to inhibit mTOR activity
- depth: abstract only (new read)
- what_it_does_not_show: neurons; direction of net translation effect of a GSK3 inhibitor

## EI21
- claim: ISRIB raised survival of mutant SOD1 expressing rat cortical neurons
- level: 4
- source_id: 32457286
- system: primary rat cortical neurons, ALS-protein model
- locator_quote_max25words: ISRIB enhanced the survival of G93A SOD1-expressing neurons within a wide dose range
- depth: partial_fulltext (module)
- what_it_does_not_show: WWOX; any link to eIF2B phosphorylation sites

## EI23
- claim: ISRIB did not improve survival with the other toxic protein tested
- level: 4
- source_id: 32457286
- system: same neurons, E46K alpha-synuclein
- locator_quote_max25words: ISRIB did not improve the survival of E46K aSyn expressing neurons
- depth: partial_fulltext (module)
- what_it_does_not_show: why; a selective benefit

## E17
- claim: Removing the GSK3 site did not change survival of injured neurons
- level: 4
- source_id: 26974342
- system: mouse retinal ganglion cells after crush
- locator_quote_max25words: AAV-eIF2Bε S535A injection did not change the rate of RGC survival
- depth: partial_fulltext (module)
- what_it_does_not_show: axon regrowth was the only gain; adult injury model

## E03
- claim: Lithium suppressed a provoked-seizure score in the Wwox null mouse, but equally in controls
- level: 4
- source_id: 32000863
- system: Wwox null mouse, wild-type, heterozygote
- locator_quote_max25words: each carries its own **** significance bracket
- depth: full text, locator from the image (module)
- what_it_does_not_show: attribution to GSK3, eIF2B or translation; WWOX specificity

# Part 4: grid patterns (check that each cited evidence id supports what the pattern assumes, and whether any pattern claims more than its sources allow)

## G01 (earlier grid row 1, kept)
- observation_pattern: phospho-eIF2alpha raised against its total; translation lowered; ISRIB restores translation; engagement control works
- explanations_supported: ISR-P
- explanations_still_compatible: STAB; GSK3-eps and GSK3-other can add to it (ISRIB working says nothing about them)
- uninformative_if: phospho-eIF2alpha and translation not read in the same wells; ISRIB at one concentration only in a bell-shaped range
- control_that_separates: a GSK3 inhibitor arm and the epsilon serine readout on the same wells; ISRIB concentration series
- depends_on_evidence_ids: EI04; EI10; EI17; E20; EI24

## G02 (earlier grid row 2, narrowed)
- observation_pattern: phospho-eIF2alpha not raised; phospho-epsilon at the GSK3 serine raised (antibody validated); translation lowered; two GSK3 inhibitors of different chemotype raise translation and lower the phospho-site; ISRIB gives little although engagement control works
- explanations_supported: GSK3-eps is a candidate reading; ISR-P is not supported (phospho-eIF2alpha not raised)
- explanations_still_compatible: GSK3-other (TSC2 and mTOR, EN12, and any substrate not yet named); CMPD (each inhibitor changes overall protein synthesis, E07); STAB with a minimal ISRIB effect; the earlier grid called this pattern the one ISRIB discriminates cleanly: it does not, see G10
- uninformative_if: the phospho-epsilon antibody is not validated (no Ser-to-Ala or phosphatase lane); the second inhibitor is not shown to dephosphorylate the site; ISRIB engagement is not shown in the same plate
- control_that_separates: phospho-resistant epsilon (species numbering checked) with the GSK3 inhibitor: no further gain in the mutant if the node carries the effect; catalytically dead epsilon; rapamycin or Torin arm (mTOR route); GSK3B versus GSK3A knock-down
- depends_on_evidence_ids: E05; E06; E07; E13; E14; E15; E16; E19; EN12; EN07; E21; EI28

## G03 (earlier grid row 3, kept)
- observation_pattern: phospho-eIF2alpha not raised; translation lowered; ISRIB raises translation
- explanations_supported: not decisive: a pharmacodynamic gain
- explanations_still_compatible: general eIF2B activation (EI11 against EI15: sources disagree); STAB (EI29); GSK3-eps with ISRIB compensating a brake; mTOR-type is not compatible if the ISRIB gain is full (EI05)
- uninformative_if: engagement control missing; exposure not effective
- control_that_separates: ISRIB engagement readout (sedimentation shift, EI08, EI16) and phospho-eIF2alpha in the same wells; a second eIF2B activator of another chemotype would add a control not yet qualified
- depends_on_evidence_ids: EI11; EI15; EI28; EI29; EI05

## G04 (earlier grid row 4, over-stated)
- observation_pattern: phospho-eIF2alpha not raised; translation not lowered in the preparation tested
- explanations_supported: no eIF2B-limited defect in this preparation at this stage and by this readout
- explanations_still_compatible: a defect at another stage (adult retina shows more brake than developing retina, E18); a defect hidden in a bulk readout; a cell type not sampled
- uninformative_if: the readout is a bulk labelling in a mixed culture; the stage differs from the one where GSK3 activity is up (E01 is postnatal day 20 brain)
- control_that_separates: a stage series; cell-type-resolved translation readout
- depends_on_evidence_ids: E18; E01

## G05 (earlier grid row 5, kept and widened)
- observation_pattern: ISRIB gives nothing; the engagement control also fails
- explanations_supported: nothing
- explanations_still_compatible: everything
- uninformative_if: always: dose, bell-shaped response (EI17), a resistant system, an inactive sample (the first report notes trans/cis mixture in the library sample)
- control_that_separates: a positive stress arm in the same plate and an assembly readout
- depends_on_evidence_ids: EI17; EI03

## G06 (new)
- observation_pattern: phospho-eIF2alpha not raised; ISRIB gives little; engagement control works
- explanations_supported: ISR-P is not the operating brake
- explanations_still_compatible: GSK3-eps and GSK3-other remain open; the result is the expected one if no phospho-eIF2alpha is present, so it neither supports nor refutes the GSK3 chain
- uninformative_if: engagement control not run in the same plate
- control_that_separates: phospho-eIF2alpha readout; then the GSK3 arms
- depends_on_evidence_ids: EI15; EI28; E21; E22

## G07 (new)
- observation_pattern: ISRIB gives little; engagement control absent or exposure not shown effective
- explanations_supported: nothing: not a refutation of the ISR route, nor of the GSK3 route
- explanations_still_compatible: all
- uninformative_if: always
- control_that_separates: engagement control and an exposure statement (in-vitro concentration range measured, not assumed)
- depends_on_evidence_ids: EI17; EI22; EI26

## G08 (new)
- observation_pattern: GSK3 inhibitor raises translation; phospho-epsilon at the GSK3 serine not changed or not measured
- explanations_supported: GSK3-other or CMPD
- explanations_still_compatible: GSK3-eps through the priming serine or another epsilon serine (EN13) with a readout that missed it
- uninformative_if: the phospho-epsilon antibody is not validated
- control_that_separates: phospho-resistant epsilon plus inhibitor; rapamycin and Torin arms; phospho-S6 kinase and 4E-BP1 readouts as the mTOR branch markers
- depends_on_evidence_ids: E07; E05; E06; EN12; EN13

## G09 (new)
- observation_pattern: GSK3 inhibitor lowers phospho-epsilon at the GSK3 serine but translation does not rise
- explanations_supported: GSK3-eps is not sufficient
- explanations_still_compatible: additional inputs act (E06); site labelled wrongly
- uninformative_if: the site identification (phosphosite.tsv) is undetermined
- control_that_separates: a validated antibody; epsilon mutants
- depends_on_evidence_ids: E06; E05

## G10 (new, correcting the earlier grid)
- observation_pattern: GSK3-eps pattern of G02 and ISRIB gives little
- explanations_supported: ISRIB little is predicted by absence of phospho-eIF2alpha, so it follows from ISR-P being off and says nothing on the GSK3 serine
- explanations_still_compatible: everything listed in G02
- uninformative_if: always while phospho-eIF2alpha is not raised
- control_that_separates: GSK3 arms and epistasis, not ISRIB
- depends_on_evidence_ids: EI15; E21; EI28; EN03

## G11 (new)
- observation_pattern: only lithium works among the GSK3 inhibitors; a second chemotype does not
- explanations_supported: CMPD (lithium has other actions; seizure effect equal in controls)
- explanations_still_compatible: GSK3-other
- uninformative_if: one chemotype only
- control_that_separates: a second chemotype and genetic GSK3B knock-down
- depends_on_evidence_ids: E03; E07

## G12 (new)
- observation_pattern: phospho-eIF2alpha raised and a GSK3 inhibitor also improves translation
- explanations_supported: ISR-P plus GSK3-eps or GSK3-other not separated
- explanations_still_compatible: mTOR route; the two inhibitors act on the ISR through a substrate other than epsilon
- uninformative_if: phospho-eIF2alpha not measured in the same wells
- control_that_separates: GSK3 inhibitor plus ISRIB combination readout to see additivity; epsilon mutants
- depends_on_evidence_ids: E07; EI04; EI25; EN12

# Part 5: units to check as sources allow
- U1. Human residue 539 of EIF2B5 (UniProt Q13144) is Asp, not Ser; the GSK3 site is Ser540 and the neighbouring priming serine Ser544.
- U2. In rat numbering the GSK3 serine of eIF2B epsilon is Ser535 and the priming serine Ser539 (DYRK).
- U3. In PMID 23741617 the phospho-S539 and total epsilon blot rows appear only in the tunicamycin panel of Figure 3 figure supplement 1 although the caption names thapsigargin as well; no quantification and no antibody validation are given.
- U4. The antibody for phospho-S539 in PMID 23741617 is from Abcam; the paper gives neither catalogue number nor immunogen.
