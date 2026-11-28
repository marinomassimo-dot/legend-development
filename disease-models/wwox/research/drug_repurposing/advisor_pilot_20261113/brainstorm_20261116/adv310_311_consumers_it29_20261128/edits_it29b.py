"""IT29: pup brief sizing corrections (ADV-311 Y1-Y3, ADV-310 X2, X3, X5) as exact-once fragments after one blind round (BLIND_REPORT_AS_DELIVERED_PUP_IT29.md). Seven fragments were rewritten after the round (T03, T06, T09, T11, T14, T20, T22). Optional edit Y5 not applied. Hypothesis level; nothing here is medical advice."""
X = [{'new': 'Knockout pups are scarce and fragile: the held counts give 5.1 and 6.5 percent knockouts among pups genotyped at postnatal day 5 to 12 from heterozygote intercrosses (Cheng 2020, '
         'supplementary Methods; DERIVED about 0.4 to 0.5 per litter of 7) and 19.5 percent at day 3 in another null line (Ludes-Meyers 2009; Mendelian-compatible), not the one in four (25 percent) '
         'of Mendelian expectation that an earlier sizing assumed (see "Sample size and animals needed").',
  'old': 'Knockout pups are scarce (about one in four from a heterozygote cross) and fragile.',
  'tag': 'T01_L61_scarce'},
 {'new': 'How are knockouts allocated within genotype and litter when a litter yields on average about 0.4 to 0.5 knockouts (Cheng 2020 frequency, DERIVED; 1.75 only if Mendelian)?**',
  'old': 'How are knockouts allocated within genotype and litter when a litter yields about 1.75 knockouts?**',
  'tag': 'T02_L105_Q46'},
 {'new': 'of the structural findings those at E12.5 (smaller embryo, elongated roof plate), E16.5 (fewer Ki-67-positive cells in the subventricular zone, thinner cortex) and birth (more '
         'BrdU-positive cells throughout the neocortex, more Ki-67-positive cells in the proliferative zones) **precede the seizures** the paper describes as "commonly observed after postnatal day '
         '12" (no onset age is given; the gross brain abnormalities reported "from live births" have no stated age and are not placed in this order). ',
  'old': 'of the structural findings **only the E16.5 cortical thinning precedes seizure onset** (seizures "commonly observed after postnatal day 12").',
  'tag': 'T03_L208_X2_structure_timing'},
 {'new': 'The paper proposes, without testing it, a chain from aberrant neuronal migration through reorganised networks to hyperexcitability (Discussion: the aberrant positioning of neurons "may '
         'cause reorganization of neuronal networks and alteration of cellular physiology that create hyperexcitable tissue"), and tests neither its order in time nor the link; "brain-wide" is not '
         'its word.',
  'old': 'The paper states no causal sequence, and "brain-wide" is not its word.',
  'tag': 'T04_L208_X3_causal_chain'},
 {'new': 'A preventive or early arm cannot be read as a reversal in respect of the findings that precede seizure onset (E12.5, E16.5 and birth).',
  'old': 'A preventive or early arm cannot be read as a reversal in respect of the E16.5 finding only.',
  'tag': 'T05_L208_X2_reversal_clause'},
 {'new': 'knockouts 12 to 16 (7 to 9 litters at the assumed 1.75 per litter, rounded to the nearest litter; 27 to 45 litters at the Cheng 2020 knockout frequency of 5.1 to 6.5 percent, DERIVED, '
         'rounded up: 34 to 45 at 5.1 and 27 to 36 at 6.5); wild-type 24 to 32 taken from the same heterozygote crosses would need 14 to 18 litters at 1.75 per litter, nearest (the wild-type '
         'frequency is not reported), so at the Cheng frequency the pilot size in litters is set by the knockout need, and the same litters would supply the wild types if these are about 25 percent '
         'of the pups (Q45).',
  'old': 'knockouts 12 to 16 (7 to 9 litters at 1.75 per litter); wild-type 24 to 32 taken from the same heterozygote crosses would need 14 to 18 litters, so the pilot size in litters is set by the '
         'wild-type need unless wild-type breeders supply them (Q45).',
  'tag': 'T06_L243_pilot_litters'},
 {'new': 'With few knockouts per litter (1.75 if Mendelian; about 0.4 to 0.5 at the Cheng 2020 frequency, DERIVED, so that most litters give no knockout and about 15 to 19 percent of the litters '
         'that give one give two or more) the bootstrap over litters is the primary interval;',
  'old': 'With about 1.75 knockouts per litter the bootstrap over litters is the primary interval;',
  'tag': 'T07_L322_interval_method'},
 {'new': 'only the authors could add one (source statement, not an inference). Knockout yield per litter: the sizing first assumed the Mendelian 25 percent of about 7 pups per litter, that is 1.75 '
         'knockouts (ASSUMED), but the observed frequency is lower. Cheng 2020 reports Wwox-/- at 5.1 percent of N = 177 (WD1 line; about 9 knockouts) and 6.5 percent of N = 785 (WD234 line; about '
         '51 knockouts) of pups genotyped at postnatal day 5 to 12 from Wwox+/- intercrosses (supplementary Methods, page 3), which at 7 pups per litter is 0.36 and 0.46 knockouts per litter '
         "(DERIVED from that frequency; the litter size of 7 is this brief's own figure and the knockout counts are the percentages times N). Another null line (exon 1 deleted by Cre) gave 30 "
         'knockouts among 154 pups genotyped at day 3 from heterozygote crosses (19.5 percent; 38.5 expected; p = 0.257, Mendelian-compatible; Ludes-Meyers 2009, Table 1); a different line and age, '
         'and the two are not reconciled here. Limits: the Cheng frequency pools pups of postnatal day 5 to 12; the frequency at the assay age is not reported and, if knockouts are lost no more '
         'slowly than their littermates, is at most that frequency; the paper states that some very severely affected embryos died embryonically but gives no count, so losses before genotyping are '
         'not quantified and would lower the yield further; the colony frequency of the laboratory governs the litter count. Litter figures below that depend on the yield are given at the assumed '
         '1.75 and at the Cheng frequency (litters = knockouts over 7 times the frequency, rounded up; DERIVED); the 1.75 figures are a Mendelian case, not the expected yield.',
  'old': 'only the authors could add one (source statement, not an inference); with a heterozygote cross and about 7 pups per litter, a litter yields about 1.75 knockouts.',
  'tag': 'T08_L347_yield_Y1_Y3_X4'},
 {'new': 'the supplement (24 pages) is held and gives no seizure methods and no seizure-group N (the group sizes it prints belong to the genotyping, with 177 and 785 genotyped pups, and to the '
         'morphology and histology panels), and no second source',
  'old': 'the supplement is held and contains no seizure methods and no N, and no second source',
  'tag': 'T09_L347_supplement_N_clarify'},
 {'new': 'about 700 to 1,300 animals and 350 to 630 knockouts (200 to 360 litters at the assumed 1.75 per litter; 770 to 1,765 litters at the Cheng 2020 knockout frequency, DERIVED) for one drug '
         'against vehicle',
  'old': 'about 700 to 1,300 animals and 350 to 630 knockouts (200 to 360 litters) for one drug against vehicle',
  'tag': 'T10_L356_interaction_floorbound'},
 {'new': '22 per cell, 88 animals, 25 litters at the assumed 1.75 per litter (rounded to the nearest litter; 44 knockouts / 1.75 = 25.1) (97 to 124 at the Cheng 2020 knockout frequency, DERIVED, '
         'rounded up) for one drug against vehicle',
  'old': '22 per cell, 88 animals, 25 litters for one drug against vehicle',
  'tag': 'T11_L357_interaction_optimistic'},
 {'new': 'at 11 per arm about 19 litters; at 31 per arm about 53; at 36 to 109 per arm, 108 to 327 knockouts, about 62 to 187 litters (all at the assumed 1.75 per litter; at the Cheng 2020 knockout '
         'frequency, DERIVED, 73 to 93 litters at 11 per arm, 205 to 261 at 31 and 238 to 916 at 36 to 109, the lower figure of each pair at 6.5 percent and the higher at 5.1)',
  'old': 'at 11 per arm about 19 litters; at 31 per arm about 53; at 36 to 109 per arm, 108 to 327 knockouts, about 62 to 187 litters',
  'tag': 'T12_L358_three_arms'},
 {'new': 'of which 33 to 150 knockouts (19 to 86 litters at the assumed 1.75 per litter; 73 to 421 litters at the Cheng 2020 knockout frequency, DERIVED: 93 to 421 at 5.1 percent and 73 to 330 at '
         '6.5)',
  'old': 'of which 33 to 150 knockouts (19 to 86 litters)',
  'tag': 'T13_L359_planning_total'},
 {'new': '(12 to 16 knockouts = 7 to 9 litters at the assumed 1.75 per litter (rounded to the nearest litter), 27 to 45 at the Cheng 2020 knockout frequency (DERIVED, rounded up); wild types from '
         'heterozygote crosses 14 to 18 litters at 1.75 (nearest), which at the Cheng frequency the knockout litters would already supply if wild types are about 25 percent of the pups (their '
         'frequency is not reported), or from wild-type pairs fewer)',
  'old': '(12 to 16 knockouts = 7 to 9 litters; wild types from heterozygote crosses 14 to 18 litters, or from wild-type pairs fewer)',
  'tag': 'T14_L363a_pilot_application_figure'},
 {'new': '= 62 to 187 litters of heterozygote crosses at the assumed 1.75 knockouts per litter, 238 to 916 at the Cheng 2020 knockout frequency of 6.5 to 5.1 percent (DERIVED); wild-type age series '
         'and panel 21 cells at 11 per cell = 231 animals, about 132 litters from heterozygote crosses at 1.75 per litter (at the Cheng frequency the knockout litters of this stage already exceed '
         'that number and would supply the wild types if these are about 25 percent of the pups; their frequency is not reported) or about 33 from wild-type pairs;',
  'old': '= 62 to 187 litters of heterozygote crosses at 1.75 knockouts per litter; wild-type age series and panel 21 cells at 11 per cell = 231 animals, about 132 litters from heterozygote crosses '
         'or about 33 from wild-type pairs;',
  'tag': 'T15_L363b_stage2_application_figure'},
 {'new': 'are the optimistic scale and, being counted at the assumed 1.75 knockouts per litter, also the Mendelian case; they should be read with the 36 to 109 bracket, at which three knockout arms '
         'need 62 to 187 litters at 1.75 per litter and 238 to 916 at the Cheng 2020 knockout frequency (DERIVED; see the sentence on the knockout yield per litter above).',
  'old': 'are the optimistic scale and should be read with the 36 to 109 bracket, at which three knockout arms need 62 to 187 litters.',
  'tag': 'T16_L373_planning_scale'},
 {'new': 'at the credible scale three knockout arms need 62 to 187 litters (36 to 109 per arm); all at the assumed 1.75 knockouts per litter, against 73 to 93, 97 to 124 and 238 to 916 litters at '
         "the Cheng 2020 knockout frequency (DERIVED). '75 litters' (3 x 44)",
  'old': "at the credible scale three knockout arms need 62 to 187 litters (36 to 109 per arm). '75 litters' (3 x 44)",
  'tag': 'T17_L375_R3C09_note'},
 {'new': 'against about 33 litters from wild-type pairs at 7 pups, and 33 knockouts need about 19 litters at 1.75 per litter (73 to 93 at the Cheng 2020 knockout frequency, DERIVED; the wild-type '
         'frequency is not reported, so 1.75 for wild types stays a Mendelian assumption).]',
  'old': 'against about 33 litters from wild-type pairs at 7 pups, and 33 knockouts need about 19 litters.]',
  'tag': 'T18_L387_C25_Q45_note'},
 {'new': 'against 33 litters from wild-type pairs at 7 pups; 33 knockouts need 19 litters at 1.75 per litter (73 to 93 at the Cheng 2020 knockout frequency, DERIVED; the wild-type frequency is not '
         'reported).]',
  'old': 'against 33 litters from wild-type pairs at 7 pups; 33 knockouts need 19 litters.]',
  'tag': 'T19_L391_Q45_note'},
 {'new': '4 cells 88 animals, 44 knockouts, 25 litters at the assumed 1.75 per litter (rounded to the nearest litter; 44 / 1.75 = 25.1) (97 to 124 at the Cheng 2020 knockout frequency, DERIVED, '
         'rounded up), for one drug against vehicle.',
  'old': '4 cells 88 animals, 44 knockouts, 25 litters, for one drug against vehicle.',
  'tag': 'T20_L397_C04_note'},
 {'new': 'The planning scale is (c); 11 per cell is a lower bound only. Correction 2026-11-28: the litter figures of (a) to (c) are at the assumed Mendelian 1.75 knockouts per litter; at the Cheng '
         '2020 knockout frequency (5.1 to 6.5 percent; DERIVED; litters rounded up) they are (a) three knockout arms 73 to 93 litters, interaction 97 to 124; (b) three knockout arms 205 to 261, '
         'interaction 273 to 348; (c) three knockout arms 238 to 916, interaction 319 to 1,219 at equal variability and 770 to 1,765 at floor-bound wild-type variability.]',
  'old': 'The planning scale is (c); 11 per cell is a lower bound only.]',
  'tag': 'T21_L399_C07_note'},
 {'new': '200 to 360 for one drug interaction at 175 to 315 per cell; both at the assumed 1.75 per litter (rounded to the nearest litter; 238 to 916 and 770 to 1,765 at the Cheng 2020 knockout '
         'frequency, DERIVED, rounded up). Note that the addendum itself calls sigma 0.3 not credible.]',
  'old': '200 to 360 for one drug interaction at 180 to 320 per cell. Note that the addendum itself calls sigma 0.3 not credible.]',
  'tag': 'T22_L411_Q33_note'},
 {'new': 'animal-level statistics, not yet an endpoint.** In the germline null a different in vivo conduction measure exists (Tc-MEP at 3 weeks, n = 10, 5 and 4 for wild type, heterozygote and null; '
         'latency 1.39 against 2.44 ms, amplitude 59.2 against 11.8 microvolts; Cheng 2020 Fig. 2; values in add-on (f)): it has no rescue arm, and the paper does not state that its animals were '
         'those of the histology (sciatic nerve electron microscopy at postnatal day 20, N = 3).',
  'old': 'animal-level statistics, not yet an endpoint.**',
  'tag': 'T23_L508_X5_Tc_MEP'}]
