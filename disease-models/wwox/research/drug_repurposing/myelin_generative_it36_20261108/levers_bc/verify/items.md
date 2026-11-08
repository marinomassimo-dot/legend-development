# Items for a blind audit (IT36 P4 B/C)

Check every item against the source named (open routes only; held full texts, if any, under /home/desktop/legend-development/files/). Verdicts: SUPPORTED / OVERSHOOT / UNDERSHOOT / NOT_IN_SOURCE / UNVERIFIABLE with the verbatim locator you found and depth reached. Identity items are checked against ChEMBL (public REST) and, where useful, the primary pharmacology paper.

# Part 1: evidence rows

## N01
- source_id: PMID36834863
- evidence_class: in_vivo_mouse
- system: Mct8/Oatp1c1 double-knockout mouse (thyroid-hormone transport deficit, not WWOX)
- perturbation: receptor-agonist analogue given in the first three postnatal weeks
- cell_stage: cortex and corpus callosum, early postnatal to 10 weeks
- level: maturation and sheath proxy (MBP and FluoroMyelin intensity); interneuron count
- finding: Callosal myelin staining and parvalbumin-positive cell numbers reached wild-type range after early treatment; interneuron GABA-synaptic frequency also normalised
- locator_quote: Only Dko mice that received Triac during the first 3 postnatal weeks showed a full normalization of PV+ cell numbers
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: staining intensity, not EM or conduction; 3 to 5 mice per group; transport-deficit model, a transfer; the effective exposure was high (see N04)
- role: support

## N02
- source_id: PMID36834863
- evidence_class: in_vivo_mouse
- system: same
- perturbation: same analogue started at postnatal week 3
- cell_stage: corpus callosum, weeks 3 to 6
- level: maturation and sheath proxy (FluoroMyelin intensity)
- finding: Late start did not improve callosal myelin staining; parvalbumin recovered only partly
- locator_quote: in Dko mice that received Triac only between postnatal week 3 and 6, myelination was not improved
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: single late window; mechanism of the closed window is unexplained by the authors
- role: counter

## N03
- source_id: PMID36834863
- evidence_class: in_vivo_mouse
- system: same
- perturbation: genotype (untreated double knockout versus wild type)
- cell_stage: cortex, P12
- level: interneuron count (parvalbumin)
- finding: The transport-deficient mouse shows fewer parvalbumin-positive interneurons together with hypomyelination: two features also under study in neuron-targeted Wwox deletion
- locator_quote: Dko mice exhibited a highly reduced number of PV+ cells in both regions
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: co-occurrence in a different disease; says nothing about cause in WWOX material
- role: context

## N04
- source_id: PMID36834863
- evidence_class: in_vivo_mouse
- system: same
- perturbation: high-exposure arm
- cell_stage: P1 to P21
- level: thyroid axis
- finding: The exposure that normalised brain readouts fully suppressed the mouse thyroid axis and left hepatic and renal signs of excess thyroid-hormone action; authors discuss this as a translation barrier
- locator_quote: The high concentration of Triac needed for effective normalization of brain parameters in our mouse model resulted in a fully downregulated HPT axis
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: mouse; the low exposure arm gave little brain effect
- role: limit

## N05
- source_id: PMID36834863
- evidence_class: clinical_statement
- system: children with MCT8 deficiency (first Triac trial, as described in the Discussion)
- perturbation: analogue treatment for 12 months
- cell_stage: median age 7.1 years
- level: neurodevelopmental outcome
- finding: The human trial was not designed to detect neurodevelopmental effect; a trend in a subset was exploratory
- locator_quote: This Triac trial was not designed to detect any impact of the treatment on neurodevelopmental outcomes in human MCT8 deficiency
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: second-hand description of a trial that was not opened
- role: counter

## N06
- source_id: PMID37765015
- evidence_class: in_vitro_primary_culture
- system: neural-stem-cell-derived mouse OPC cultures
- perturbation: receptor-beta prodrug versus T3, cytokine mix during expansion
- cell_stage: 12 days of differentiation
- level: maturation (CNPase and MBP shares)
- finding: The prodrug restored the differentiation block that T3 did not
- locator_quote: TG68 rescued the cytokine differentiation block almost completely
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: in vitro; inflammatory block, not a neuron-null condition; mechanism not isolated (N08)
- role: support

## N07
- source_id: PMID37765015
- evidence_class: in_vitro_primary_culture
- system: same
- perturbation: same compound
- cell_stage: same
- level: mechanism
- finding: The authors report off-receptor pharmacology of the prodrug, with AMPK activation, so a receptor attribution needs a receptor-specific control
- locator_quote: Preliminary investigations have revealed the polypharmacology of both compounds tested in this study and, most importantly, the significant activity of TG68 on AMPK activation.
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: preliminary, as the authors say
- role: limit

## N08
- source_id: PMID37765015
- evidence_class: in_vitro_primary_culture
- system: same
- perturbation: T3 in the cytokine-block condition
- cell_stage: 12 days
- level: maturation
- finding: T3 itself did not rescue the cytokine-induced block (a context where the natural ligand is useless)
- locator_quote: Cytokine exposure generated a reduction in the number of early-mature OLs in the cultures not rescued by T3
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: cytokine mix is an inflammatory model, not WWOX
- role: counter

## N09
- source_id: PMID37765015
- evidence_class: introduction_statement
- system: review statement in the Discussion
- perturbation: none
- cell_stage: OPC
- level: receptor isoform
- finding: Receptor-beta is stated as believed chief for T3-mediated differentiation; INV-12 records rodent OPCs as receptor-alpha-leaning at abstract level: the two statements differ
- locator_quote: the latter believed to be the isoform chiefly responsible for T3-mediated differentiation induction
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: a belief with citations, not a measurement here; the INV-12 statement was not re-read
- role: context

## N10
- source_id: PMID37765015
- evidence_class: method_statement
- system: same
- perturbation: none
- cell_stage: OPC differentiation protocol
- level: medium
- finding: The standard OPC differentiation medium of this protocol contains T3 as the main trigger; relevant to how culture media decide whether a thyroid-hormone arm is informative
- locator_quote: the differentiation medium containing CNTF, NAC, and T3, the main trigger of OPC differentiation
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: other labs differ
- role: context

## N11
- source_id: PMID37765015
- evidence_class: clinical_statement
- system: review statement
- perturbation: none
- cell_stage: clinical development
- level: status
- finding: Most thyromimetics proposed for OPC differentiation have not passed clinical trials (examples named: sobetirome stopped at phase 1, eprotirome terminated)
- locator_quote: most thyromimetic drugs proposed for the promotion of OPC differentiation in demyelinating diseases have not passed clinical trials
- depth_reached: partial_fulltext (text read, figures and tables not viewed)
- limits: second-hand statement; adult demyelinating diseases, not developmental
- role: counter

## N12
- source_id: PMID21228163
- evidence_class: ex_vivo_slice
- system: cultured slices of developing mouse cortex with GFP-labelled oligodendrocyte lineage
- perturbation: low glucose; exogenous lactate
- cell_stage: developing cortex
- level: sheath proxy (myelination, cell number)
- finding: Low glucose lowered oligodendrocyte-lineage cell number and myelination in slices
- locator_quote: a low glucose concentration reduces the number of oligodendrocyte lineage cells and myelination
- depth_reached: abstract_only (full text unreachable: empty PMC body, publisher-blocked XML)
- limits: glucose concentrations, readouts and controls not read; cortical slices; not WWOX
- role: support

## N13
- source_id: PMID21228163
- evidence_class: ex_vivo_slice
- system: rat cerebellum and corpus callosum white matter
- perturbation: pH imaging of lactate uptake
- cell_stage: white matter
- level: transport
- finding: White-matter oligodendrocytes take up lactate through monocarboxylate transporters, identified as MCT1
- locator_quote: oligodendrocytes in the white matter of the rat cerebellum and corpus callosum take up lactate via monocarboxylate transporters (MCTs)
- depth_reached: abstract_only
- limits: as N12
- role: support

## N14
- source_id: PMID27664134
- evidence_class: in_vivo_zebrafish
- system: mct8 mutant zebrafish larvae (transport-deficit)
- perturbation: T3 treatment at different ages
- cell_stage: embryo versus older larva
- level: sheath proxy (myelin markers)
- finding: Hormone rescue worked before blood-brain-barrier maturation and not in older larvae
- locator_quote: but did not affect hypomyelination in older larvae
- depth_reached: abstract_only
- limits: abstract only; zebrafish; transfer
- role: counter

## N15
- source_id: PMID32477268
- evidence_class: review_statement
- system: clinical trials in MCT8 deficiency (review)
- perturbation: thyromimetics
- cell_stage: children
- level: neurological outcome
- finding: Review notes absence of neurological improvement as a recurrent trial observation
- locator_quote: A recurrent observation in clinical trials is the absence of neurological improvement.
- depth_reached: abstract_only
- limits: review abstract; primary trials not opened
- role: counter

## N16
- source_id: PMID18760695
- evidence_class: in_vivo_mouse
- system: conditional neuregulin-1 null mice
- perturbation: neuregulin-1 deletion from different neural stages
- cell_stage: CNS development
- level: sheath (myelin amount)
- finding: Mice lacking neuregulin-1 assemble normal amounts of CNS myelin
- locator_quote: Unexpectedly, these mice assemble normal amounts of myelin.
- depth_reached: abstract_only
- limits: abstract only; overexpression gives hypermyelination (not quoted)
- role: counter

## N17
- source_id: PMID18760695
- evidence_class: in_vivo_mouse
- system: oligodendroglial ErbB3 and ErbB4 double mutants
- perturbation: receptor deletion
- cell_stage: CNS development
- level: sheath
- finding: Double mutants myelinate without neuregulin stimulation: a neuregulin-ErbB axo-glial cue is not required for developmental CNS myelination
- locator_quote: double mutants lacking oligodendroglial ErbB3 and ErbB4 become myelinated in the absence of any stimulation by neuregulins
- depth_reached: abstract_only
- limits: abstract only; does not exclude a cue acting on neuronal ErbB4 or on non-myelination steps
- role: counter

## N18
- source_id: PMID24308844
- evidence_class: biophysics
- system: recombinant WW domains and ErbB4 intracellular-domain peptides
- perturbation: binding assays
- cell_stage: in vitro
- level: physical interaction
- finding: The first WW domain of WWOX binds PPXY motifs in the ErbB4 intracellular domain
- locator_quote: the WW1 domain of WWOX binds to PPXY motifs located within the ICD of ErbB4 in a physiologically relevant manner
- depth_reached: abstract_only (earlier partial receipts exist, not re-opened)
- limits: non-neural, purified fragments
- role: context

## N19
- source_id: PMID17909041
- evidence_class: human_tissue_and_cell_lines
- system: breast cancers and transfected cells
- perturbation: expression and interaction
- cell_stage: tumour
- level: association
- finding: Wwox interacts with ErbB4 and reduces nuclear translocation of its cleaved domain in cancer material
- locator_quote: Wwox interacts with the ErbB4 receptor, reduces nuclear translocation of the cleaved intracellular domain of ErbB4
- depth_reached: abstract_only
- limits: cancer, not neural; association
- role: context

## N20
- source_id: SEARCH Q13
- evidence_class: bounded_search
- system: PubMed
- perturbation: string: Wwox thyroid hormone
- cell_stage: 2026-11-08
- level: mechanism
- finding: No source linking WWOX to thyroid-hormone handling in neural cells was found; the single hit is a human GWAS with a suggestive association between a WWOX variant and circulating T3 (viewed, not used)
- locator_quote: NOT_FOUND after: PubMed tool, string Wwox thyroid hormone, 2026-11-08, 1 hit unrelated to neural tissue
- depth_reached: search_only
- limits: one PubMed string; not an absence in the literature
- role: counter

## C01
- source_id: PMID33914858
- evidence_class: method_statement
- system: mouse DRG neurons plus wild-type OPCs (held text re-read)
- perturbation: none
- cell_stage: 9 to 11 days
- level: medium
- finding: Co-culture medium is a B27 and N2 medium with N-acetyl-cysteine and forskolin; no thyroid hormone is named in it; whether B27 itself carries a hormone was not verified
- locator_quote: maintained in co-culture medium (DMEM containing B27 and N2
- depth_reached: partial_fulltext (Methods, cell culture; held text)
- limits: supplier composition of B27 and N2 not opened; medium glucose not stated; INV06:E12 covers the spheroid medium
- role: check

## C02
- source_id: PMID33914858
- evidence_class: method_statement
- system: same
- perturbation: forskolin in the co-culture medium
- cell_stage: same
- level: medium
- finding: Forskolin (a cyclic-AMP raiser) is in the medium of every arm, so the null-neuron deficit appears with that differentiation-promoting component present; unit printed as in the extracted text
- locator_quote: 5 mg/ml N-acetyl-cysteine, 5 mM forskolin
- depth_reached: partial_fulltext (held text)
- limits: unit as printed by the text extraction; INV06:X4 already flags forskolin as a confound for CREB-type arms
- role: check

## C03
- source_id: PMID33914858
- evidence_class: bounded_search
- system: held print text of the neuron-targeted paper
- perturbation: strings glucose, glycemi, hypoglyc
- cell_stage: 2026-11-08
- level: energy
- finding: No blood-glucose result of the neuron-targeted line appears in the text read (matches are buffer recipes)
- locator_quote: NOT_FOUND after: held print text, strings glucose glycemi hypoglyc, 2026-11-08
- depth_reached: search_only
- limits: text only; supplement and figures not searched
- role: counter

## C04
- source_id: PMID42422765
- evidence_class: abstract_statement
- system: global Wwox-null mice treated with vector
- perturbation: neuron-promoter vector
- cell_stage: neonatal
- level: network function
- finding: The abstract sentence used for a mosaic comparison is about hyperexcitability after vector treatment of global-null mice; the paper holds no mosaic-Cre comparison
- locator_quote: Early neuronal hyperexcitability was suppressed following treatment.
- depth_reached: partial_fulltext (abstract and Results passage, held text)
- limits: figures not viewed
- role: check

## C05
- source_id: PMID42422765
- evidence_class: in_vivo_mouse
- system: global Wwox-null mice, promoter comparison
- perturbation: myelin-basic-protein-promoter vector
- cell_stage: neonatal
- level: survival, weight, glucose
- finding: The oligodendrocyte-promoter arm had weak expression, so it is not a test of oligodendrocyte-directed restoration
- locator_quote: oligodendrocyte-specific WWOX expression driven by the MBP promoter resulted in weak expression and no phenotypic improvement
- depth_reached: partial_fulltext (Results, held text)
- limits: expression strength confounds the arm
- role: check

## C06
- source_id: PMID42422765
- evidence_class: bounded_search
- system: held text of the vector paper
- perturbation: strings mosaic and neighbo
- cell_stage: 2026-11-08
- level: design
- finding: No within-animal wild-type neighbour comparison found
- locator_quote: NOT_FOUND after: held text, strings mosaic neighbo, 2026-11-08
- depth_reached: search_only
- limits: text only
- role: counter

## C07
- source_id: PMID34747138
- evidence_class: in_vivo_mouse
- system: Wwox-null mice, control-vector and neuron-vector treated
- perturbation: genotype and vector
- cell_stage: second week to death
- level: energy (blood glucose)
- finding: Null and control-vector mice were hypoglycaemic from the second week; the myelin readout is at P17, so the order of the two is not set
- locator_quote: were hypoglycemic from the second week until they succumbed
- depth_reached: partial_fulltext (Results, held text)
- limits: tail-prick glucometer; no brain measure
- role: check

## C08
- source_id: PMID34747138
- evidence_class: in_vivo_mouse
- system: same
- perturbation: neuron-promoter vector with mouse or human cDNA
- cell_stage: same
- level: energy (blood glucose)
- finding: Neuron-targeted restoration gave normal blood glucose, bundled with the seizure and myelin rescue
- locator_quote: had normal blood glucose levels when compared to the
- depth_reached: partial_fulltext (Results, held text)
- limits: bundled rescue cannot order glucose, seizures and myelin
- role: check

## C09
- source_id: PMID34747138
- evidence_class: bounded_search
- system: held text of the restoration paper
- perturbation: string lactate
- cell_stage: 2026-11-08
- level: energy
- finding: No brain glucose or lactate measurement found
- locator_quote: NOT_FOUND after: held text, string lactate (0 hits), 2026-11-08
- depth_reached: search_only
- limits: text only
- role: counter

## C10
- source_id: PMID42686079
- evidence_class: abstract_statement
- system: Glut1-haploinsufficient mouse (abstract re-read; unguided receipt covers the abstract)
- perturbation: genotype
- cell_stage: young adult
- level: myelin programmes
- finding: The downregulation of oligodendrocyte and myelination genes was found by striatal profiling, not across brain regions as the unguided table words it
- locator_quote: Striatal transcriptomic profiling revealed a reactive astrocytic signature along with coordinated downregulation of genes involved in oligodendrocyte function
- depth_reached: abstract_only
- limits: abstract only; no new receipt
- role: check

## C11
- source_id: PMID42686079
- evidence_class: abstract_statement
- system: same
- perturbation: genotype
- cell_stage: young adult
- level: microstructure
- finding: MRI abnormalities were selective to one region
- locator_quote: diffusion MRI revealed selective microstructural abnormalities confined to the dorsolateral striatum
- depth_reached: abstract_only
- limits: as C10
- role: check

## C12
- source_id: PMID42686079
- evidence_class: abstract_statement
- system: same
- perturbation: early postnatal lactate supplementation
- cell_stage: young adult
- level: motor behaviour
- finding: Lactate partly rescued motor deficits; no myelin readout is reported for the rescue in the abstract
- locator_quote: partially rescued motor deficits in young adult
- depth_reached: abstract_only
- limits: symptom response, not myelin protection
- role: counter

# Part 2: hypothesis propositions (check the relations, identities, pharmacology facts and the stated counter-evidence)

## H1
- external_relation_used: A differently-caused hypomyelination (thyroid-hormone transport deficit) shows the same stage pattern (PMID37307933 abstract, see comparison ALT3), fewer parvalbumin interneurons (N03), callosal myelin staining normalised by a receptor agonist only when started in the first three postnatal weeks (N01, N02), a hormone rescue lost in older zebrafish larvae (N14) and receptor-beta ligand effects on OPCs in vitro (N06). This is a transfer
- compound_or_probe_if_sustainable: Tiratricol (CAT:CHEMBL41632) with liothyronine (CAT:CHEMBL1544) as comparator, as in INV-12; sobetirome (CAT:CHEMBL107400) only as a receptor-beta-leaning isoform control; DITPA (CAT:CHEMBL2348292) as a second analogue. TG68 and IS25 are absent from the catalogue (no identifier assigned) and TG68 has stated off-receptor activity (N07): not proposed
- identity_and_pharmacology: Source facts: tiratricol and DITPA activate thyroid receptors without MCT8-dependent entry (introduction of PMID36834863); sobetirome is the best-known receptor-beta-selective analogue and IS25 a receptor-beta agonist of nanomolar potency (PMID37765015). Caveats from sources: the exposure that normalised brain readouts suppressed the mouse thyroid axis (N04); the human trial of tiratricol had no neurodevelopmental endpoint (N05); sobetirome stopped at phase 1 and eprotirome terminated (N11); seizure effect mixed per INV-12 (not re-read). No dose, no regimen; a hormone is a lever of a process here, not a proposal to give it
- main_counterevidence: No WWOX material shows a thyroid-hormone deficit; the one WWOX-thyroid hit was an unrelated human GWAS (N20). The stage pattern is generic (also with creatine deficiency, comparison ALT3). Late start did not help in the model (N02) and nulls die at 3 to 4 weeks, leaving a narrow window. Trials show no neurological improvement as a recurrent observation (N15). T3 did not rescue a cytokine block in vitro (N08). Isoform dispute (N09)
- wwox_evidence_vs_transfer: WWOX: stage pattern (INV06:E08), co-culture deficit (INV06:E06), medium composition (C01, INV06:E12). Transfer: all thyroid-deprivation, rescue-window and ligand evidence (N01 to N15). The overlap of stage pattern and parvalbumin loss with a hormone-deprived brain is an INFERENZA, not a cause
- depth_of_sources: PMID36834863 and PMID37765015 partial full text (text read, figures not viewed); PMID27664134, PMID32477268, PMID37307933 abstract only; held PMID33914858 Methods only

## H2
- external_relation_used: Low glucose lowers oligodendrocyte-lineage cell number and myelination in cultured cortical slices, rescued by lactate; white-matter oligodendrocytes take up lactate by MCT1 (N12, N13, abstract only); Glut1 haploinsufficiency lowers brain glucose, glycogen and lactate with striatal myelin-gene downregulation and a motor-only lactate rescue (C10 to C12). Transfer from energy-deprivation systems
- compound_or_probe_if_sustainable: No compound sustained. Lactate is a metabolite probe in the sources (catalogue CAT:EC:01903, no status statement), used to test a process, not a supplementation proposal. No MCT1 blocker is named in any source read (the Rinholm full text was not reachable), so none is proposed
- identity_and_pharmacology: Source facts only: white-matter oligodendrocytes take up L-lactate through MCT1 (N13); early-postnatal lactate partly rescued motor deficits in a Glut1-deficient mouse (C12), a symptom response and not myelin protection. Caveat: a metabolic intervention in a child with seizures has developmental and acid-base effects not examined here. No dose
- main_counterevidence: Lactate rescue in Glut1 deficiency was motor, not shown for myelin (C12); myelin and MRI findings there were striatal (C10, C11); the Rinholm result is cortical slices under low glucose at abstract level; WWOX-side lactate points up not down; brain energy was never measured (C09); hypoglycaemia starts in week 2 and the myelin readout is P17, so order is unset (C07); the bundled rescue cannot separate glucose from seizures (C08)
- wwox_evidence_vs_transfer: WWOX: hypoglycaemia and bundled rescue (C07, C08), module lactate rows (non-neural cells, transcripts). Transfer: all oligodendrocyte-energy evidence (N12, N13, C10 to C12)
- depth_of_sources: PMID21228163 and PMID42686079 abstract only; held PMID34747138 and PMID33914858 partial (keyword searches and Results passages)

# Part 3: comparison claims about the unguided relations (source_check column is the claim)

## ALT1
- status: already_represented_and_used
- source_check: PMID24727982 not re-opened (abstract level in the unguided receipt). The unguided claim that the cultured neurons are pre-seizure peripheral neurons is the INV-06 statement (section 1: peripheral, seizure-free neurons)
- what_is_new: Only the optogenetic activity-promotes-myelination abstract (PMID24727982) is not in LEGEND; it is weaker than the two full-text activity sources INV-06 already uses. The unguided test "readouts at or before P9 in seizure-suppressed nulls" repeats INV-06 X0 and its note that the neonatal activity window ends near P8 while burst recordings are P13 to P17 (E11), so early hyperactivity is unrecorded

## ALT2
- status: already_represented_and_used
- source_check: Row 1 (PMID33914858 abstract sentence) is generic. Row 2 NOT SUPPORTED: PMID42422765 is a vector study in global-null mice; its quoted sentence concerns hyperexcitability after treatment and the text has no mosaic or neighbour comparison (C04, C06; held text, partial depth). The unguided README line that neuron-restricted delivery beat oligodendrocyte-directed delivery overshoots: the myelin-promoter arm had weak expression (C05)
- what_is_new: The within-animal wild-type-neighbour readout in mosaic Syn-Cre tissue is not among X0 to X4 and is a usable design element (limit: the Cre line is mosaic, INV06:E08). Nothing else is new

## ALT3
- status: already_represented_and_used
- source_check: PMID37307933 abstract matches the unguided quote (differentiation blockage, higher OPC share); full text not reachable (Elsevier, not open access in Europe PMC): depth stays abstract. PMID36732069 not re-opened
- what_is_new: The cross-system equivalence of the stage pattern (PMID37307933 abstract) is a new inference at pattern level, as is the creatine-deficiency parallel (PMID36732069 abstract, not re-opened). New from this phase: the co-culture medium has no named hormone (C01); window and PV co-occurrence (N01 to N03); the isoform statement in INV-12 is contested (N09). The unguided note that the tool class was unsourced describes the unguided run, not LEGEND: INV-12 holds it, so this alternative was not isolated from prior knowledge

## ALT4
- status: new_inference
- source_check: PMID42686079 abstract: the unguided row is accurate on lowered glucose, glycogen and lactate but generalises myelin-gene downregulation, which was found by striatal profiling, and MRI change confined to the striatum (C10, C11); lactate rescued motor deficits, no myelin readout in the abstract (C12). PMID34747138 held text (partial depth): glucose from the second week, normalised by neuronal restoration, no brain glucose or lactate measured (C07 to C09); no glucose result for the neuron-targeted line in the held text of the originating paper (C03)
- what_is_new: The link from glucose or lactate supply to oligodendrocyte-lineage development and myelination (N12, N13; abstract level) and the sign problem: WWOX-side lactate data point to more, not less, lactate

## ALT5
- status: already_represented_and_used
- source_check: Abstract only; not re-opened
- what_is_new: Nothing: the longer-sheath compensation (PMID37307933 abstract) comes from a different genotype

## ALT6
- status: already_represented_and_used
- source_check: Matches INV-06 rows; originating paper not re-read here
- what_is_new: Nothing: sample sizes quoted in the unguided row match E08, E09, E10

# Part 4: bridge row

- gene_a: WWOX
- hgnc_a: HGNC:12799
- relation: binds the intracellular domain of
- gene_b: ERBB4
- hgnc_b: HGNC:3432
- status: observed_other_context
- context: recombinant WW domain and PPXY-motif peptides (biophysics, abstract level) and breast-cancer tissue and transfected cells (association, abstract level); no neural or oligodendrocyte-lineage context
- evidence_ref: levers_bc evidence N18 and N19
- note: physical relation only, direction on any myelin endpoint undetermined; in oligodendroglia ErbB3/ErbB4 double mutants myelinate without neuregulin stimulation (levers_bc evidence N17), so this row must not be read as a lead for the myelin need
