# Items for the blind verifier (extracted by the Orchestrator; roles and conclusions withheld)

Non-canonical working note. Paths relative to the package folder. Source depth below is the producer's own statement, not yours.

## A. Decisive propositions (producer's decisive.tsv, columns reduced)

### D01 — onfasprodil (MIJ821)
- Statement: DATO (absence within the perimeter): no source reached states a receptor site for onfasprodil or its basis (competition with ifenprodil, mutagenesis, structure); the authors only declare it a selective NR2B negative allosteric modulator, and any chemotype resemblance to ifenprodil-site ligands is INFERENZA.
- Source: 40767837; 37817426; US 10239835 B2; 42976542 (abstract only) · locator: 40767837 Abstract and Introduction; 37817426 Introduction; patent description and claims; 42976542 abstract
- Producer status/depth: read (40767837, 37817426, patent); abstract_only (42976542) · partial_fulltext_read for 40767837 (publisher page main text; supplements unreachable; tables and figures not viewed); partial_fulltext_read for 37817426 (main text, supplements, Fig 2 viewed); patent description and assay example read through a local text copy; 42976542 abstract only (publisher stub)
- Kind/class: declared / absence
- System: Human trials and patent text; no recombinant site experiment (mutagenesis, ifenprodil occlusion, structure) found in any source reached; 42976542 abstract mentions ligand-receptor interaction insights for analogues, full text not reached

### D02 — onfasprodil (MIJ821)
- Statement: DATO: the registry value for onfasprodil (IC50 8.3 nM, pIC50 8.08) traces through BindingDB and ChEMBL to US 10239835 B2, an applicant patent whose only assay is a calcium-flux read on HEK293 cells expressing NR1/NR2B (3 uM glutamate, 3 uM glycine, 1 mM Ca2+ in Ca/Mg-free buffer, 10 min pre-incubation, read against MK801); the patent text lists one 8.30E-09 M entry but its structure column is an image, so the row-to-compound assignment is ChEMBL's and was not verified by me.
- Source: US 10239835 B2 (ChEMBL document CHEMBL5726760, assay CHEMBL5733282); GtoPdb 2026.3.1 row (no PubMed id) · locator: Patent Example 19 (Cell Assay) and Table 8 (NR2B NAM Assay); ChEMBL API activity record, IC50 8.3 nM
- Producer status/depth: read (patent text, ChEMBL record); registry row seen in the IT41 search_rows file · partial reading of the patent: assay example, Table 8 as text, claims header and description scanned by keyword; structures not readable; ChEMBL record read through its public API
- Kind/class: registry_or_patent / compound/class
- System: NR1/NR2B construct (species not stated in the patent text read), HEK293 tetracycline-induced, FDSS 6000 fluorescence, 3 uM glutamate and 3 uM glycine, 1 mM Ca2+, Ca/Mg-free buffer with 20 mM HEPES (pH not stated), no Zn2+ chelator stated, not voltage clamped; original measurement by the patent applicant, repeated as database copies in BindingDB, ChEMBL and GtoPdb

### D03 — onfasprodil (MIJ821)
- Statement: DATO (absence within the perimeter): maximum inhibition of onfasprodil on GluN1/GluN2B diheteromers and on GluN1/GluN2A/GluN2B triheteromers is not tested in the source: the patent reports an IC50 or an activity category per compound on NR1/NR2B only, and no clinical paper reports in-vitro pharmacology.
- Source: US 10239835 B2; 40767837; 37817426 · locator: Patent Table 8 legend and Example 19; the two clinical papers (no in-vitro section)
- Producer status/depth: read · partial_fulltext_read as in D01-D02
- Kind/class: registry_or_patent / absence
- System: Perimeter: the three sources above, PubMed and Europe PMC strings MIJ821, onfasprodil, MIJ821 with GluN2A/oocyte/slice terms (2026-11-10); 42976542 full text and any Novartis or Cadent poster not reached; no maximum effect and no triheteromer datum exists in anything opened; ifenprodil's 88 and 32 percent (24607230) are not carried to this compound

### D04 — onfasprodil (MIJ821)
- Statement: DATO (absence within the perimeter): subunit selectivity of onfasprodil over GluN2A, GluN2C and GluN2D and any off-target panel are not measured in any source reached; the word selective is declared by the sponsor-authored clinical papers without a citation, and GtoPdb records selectivity as Not Determined.
- Source: 40767837; 37817426; GtoPdb 2026.3.1 row; US 10239835 B2 · locator: 40767837 Abstract; 37817426 Introduction ('highly potent, selective, and reversible'); patent assay (one construct)
- Producer status/depth: read · partial_fulltext_read as in D01
- Kind/class: declared / absence
- System: Authors are Novartis employees or Novartis-funded (both trials); the 8.3 nM comes from a single NR1/NR2B assay; no NR1/NR2A or counter-screen in the patent text; the ChEMBL human GRIN2B activity list for this molecule holds one IC50 row

### D05 — onfasprodil (MIJ821)
- Statement: DATO: in adults with treatment-resistant depression (72 randomised, 70 treated, 53 completed, 18-65 years, primary endpoint MADRS change at 24 h, ketamine reference arm only in the Spanish sites) onfasprodil separated from placebo at 24 and 48 h and, in some arms, at week 6, with dizziness, transient amnesia and somnolence as commonest events and mild dissociative events; this is exposure and activity in another disease, not utility or safety in WOREE.
- Source: 40767837 (doi 10.4088/JCP.23m15246); NCT03756129 · locator: Abstract; Methods (design, population); Results (primary endpoint, Safety); Discussion (limitations)
- Producer status/depth: read · partial_fulltext_read (publisher page text, supplementary appendices and Tables 1-3 images not reached)
- Kind/class: clinical / transfer from other system
- System: Adult humans with major depressive disorder and failure of at least two antidepressants, multicentre US and Spain, randomised placebo-controlled; sample small by the authors' own limitation statement; a declared (not shown) projection of more than 90 percent brain NR2B occupancy from rodent PET is 'data on file'

### D06 — onfasprodil (MIJ821)
- Statement: DATO: in the first-in-human study in healthy adults (43 randomised to single administration and 12 to repeated administration; age 22-56) the compound was reported well tolerated with dose-dependent dissociative events, amnesia and dizziness, a CSF/free-plasma ratio estimated at 0.9, EEG changes read as distal target engagement, and a positive plasma concentration to QTcF relation whose Fig 2 caption reports an upper confidence bound above the 10 ms line (the text reports a different, lower estimate).
- Source: 37817426 (doi 10.1111/cts.13623, PMC10651655) · locator: Results (Safety, Cardiovascular safety, PK, Pharmacodynamics); Fig 2 viewed; Discussion limitations; supplementary data S1-S3 read
- Producer status/depth: read · partial_fulltext_read (main text and three supplementary documents read; Fig 2 viewed; Figs 1 and 3 captions only)
- Kind/class: clinical / transfer from other system
- System: Healthy adult volunteers (maximum age 56), single centre, Novartis-funded; QTcF analysis is exploratory regression on Holter data; no patient population, no non-psychiatric disease, no developmental or paediatric data

### D07 — onfasprodil (MIJ821)
- Statement: DATO (absence within the perimeter): no non-psychiatric clinical context for onfasprodil was found; the four ClinicalTrials.gov records returned for MIJ821 on 2026-11-10 are treatment-resistant depression, major depression with suicidal ideation (terminated by the sponsor, reason not given beyond that), and one imaging study in healthy men, and no registered or published use in epilepsy or a neurodevelopmental disorder appeared.
- Source: ClinicalTrials.gov API v2 query on intervention MIJ821; Europe PMC string (MIJ821 OR onfasprodil OR NP10679) AND (epilep* OR seizure*) · locator: Registry fields (condition, phase, status, enrolment) for NCT04722666, NCT05454410, NCT03756129, NCT05666687
- Producer status/depth: read (registry record fields only) · registry_fields_only (study records not read in full)
- Kind/class: clinical / absence
- System: Perimeter: ClinicalTrials.gov v2 API queries on MIJ821, onfasprodil, NP10679, NP-10679 and the Europe PMC strings of 2026-11-10; no search of national registries other than ClinicalTrials.gov, nor of company pipelines; unknown is not negative

### D08 — NP10679
- Statement: DATO (declared by developer-affiliated authors, not measured here): NP10679 is about 6-fold more potent at blocking the receptor at pH 6.9 than at pH 7.6 and has more than 100,000-fold selectivity for GluN2B over other GluN2 subunits; the GtoPdb value pIC50 7.64 (IC50 23 nM) is one oocyte measurement at pH 6.9 only, copied from the discovery paper (34493631), which I could not open, so no maximum effect and no second pH value is in any file.
- Source: 36642931 (doi 10.1002/cpdd.1217); 34493631 (abstract only); GtoPdb 2026.3.1 row · locator: 36642931 Introduction (second paragraph after the class discussion); 34493631 abstract; GtoPdb assay text 'at pH 6.9'
- Producer status/depth: read (36642931); abstract_only (34493631) · partial_fulltext_read for 36642931 (full text through the PMC route; tables and figures not viewed, no image in the open bucket); 34493631 abstract only: PMC page returned a bot check, publisher page a Cloudflare 403, Europe PMC pdf render a 403, efetch XML withheld by the publisher; none retried by another route
- Kind/class: declared / compound/class
- System: Registry row: human GluN2B in Xenopus oocytes, two-electrode voltage clamp, glutamate and glycine, pH 6.9 (other conditions not in the row); developer-affiliated authors (NeurOp, Emory) in 36642931, so the 6-fold and the selectivity figure are same-origin repeats of 34493631 or unpublished data, not independent confirmation

### D09 — 93-31 (series prototype; not NP10679)
- Statement: DATO: for the prototype of the NP10679 series (compound 93-31, not NP10679) on rat GluN1/GluN2B in oocytes the IC50 was 1.8 uM with a fitted maximum of 76 percent at pH 7.6 and 0.19 uM with 83 percent at pH 6.9, so potency moved about 9.5-fold while the maximum barely moved, and the series' fitted maxima ran 79-100 percent.
- Source: 25728572 (doi 10.1016/j.neuron.2015.02.008, PMC4368485) · locator: Table 2 first row (wild-type GluN2B) and Table 1 footnote d; Results 'pH-sensitive GluN2B-selective antagonists'
- Producer status/depth: read · partial_fulltext_read (Results, Methods, Discussion, Tables 1-2 read; figures captions only, no image in the open bucket; supplementary Tables S4-S6 and Figure S1 not reached)
- Kind/class: measured / compound/class
- System: Rat GluN1-1a/GluN2B in Xenopus oocytes, two-electrode voltage clamp at -40 mV, 23 C, 50-100 uM glutamate plus 30 uM glycine, 10 uM EDTA, Mg2+-free (0.5 mM Ba2+), pH 7.6 or 6.9 set with HCl at constant Na+; potency and maximum are separate columns in the table

### D10 — 93-31 and analogues (not NP10679)
- Statement: DATO: within the same series the pH sensitivity is a property of the individual molecule and not of the site alone, because changing the N-alkyl side chain moved the 7.6/6.9 potency ratio between 1.3 and 9.4 (n-butyl 9.4, iso-butyl 2.9) at similar amine pKa, and the R isomer of the prototype gave 3.8 against 10 for the S isomer.
- Source: 25728572 · locator: Table 1; Results 'Mechanism underlying pH sensitivity of GluN2B antagonists' and 'Potential role of Glu106:Glu235'
- Producer status/depth: read · partial_fulltext_read as in D09
- Kind/class: measured / compound/class
- System: Rat GluN1/GluN2B, oocytes, conditions as D09; ionisation of the ligand excluded as the cause by the authors' pKa table (calculated values, not measured)

### D11 — ifenprodil, CP-101,606, class
- Statement: DATO (class-level statements, partly in tension): the abstract of the 1998 oocyte paper declares that ifenprodil and CP-101,606 inhibit by making the receptor more sensitive to proton inhibition, and the 1997 oocyte abstract measured smaller ifenprodil inhibition at alkaline pH, whereas the 2015 discussion declares that CP-101,606 and other GluN2B antagonists lack substantial pH sensitivity (supplementary Table S6, not reached): pH dependence is a graded property of ifenprodil-site ligands, large only in the optimised series, not a uniform class value.
- Source: 10196581 (abstract only); 9143010 (abstract only); 25728572 (Discussion) · locator: 10196581 abstract; 9143010 abstract; 25728572 Discussion paragraph 3
- Producer status/depth: abstract_only (10196581, 9143010); read (25728572 Discussion) · abstract_only for the two older papers (publisher pages paywalled, not opened); Yuan Table S6 not reached, so the size of ifenprodil's own pH shift is not in any file
- Kind/class: declared / compound/class
- System: Recombinant NR1/NR2B in Xenopus oocytes (both old papers, abstract level); conditions (glutamate, glycine, holding potential, Mg2+, Zn2+) unread for the old papers

### D12 — 93-31, NP10075 (docking), NP10679 (inferred)
- Statement: DATO for the series, INFERENZA for NP10679: for compound 93-31 docking into the ifenprodil-site amino-terminal-domain interface plus mutation of GluN1 Gly112 and of GluN2B Glu106, Glu206 or Glu235 (the last three abolish the pH dependence) place the pH-sensing at that site, and an earlier NeurOp aryl-piperazine (NP10075) was docked to a similar pose; NP10679 itself is not tested for site, Mg2+, voltage or use dependence in any source reached, so its ifenprodil-site action rests on the series relation and on its aryl-piperazine propanolamine chemotype.
- Source: 25728572; 36642931 (chemical name in Methods) · locator: 25728572 Results 'Binding of pH-sensitive antagonists', 'Identification of pH-sensitive binding-site residues', Table 2; 36642931 Methods 'Drug substance and product'
- Producer status/depth: read · partial_fulltext_read as in D09; the NP10679 chemical-name string in 36642931 is garbled in the text copy (ring name truncated)
- Kind/class: measured / binding/action/benefit
- System: Docking into the Xenopus GluN1-ATD/rat GluN2B-ATD crystal model (pose scoring, computational); mutagenesis in rat GluN1/GluN2B oocytes at pH 7.6 and 6.9, Mg2+-free; no competition experiment between NP10679 and ifenprodil found

### D13 — 93-31 (measured); NP10679 (not tested in the source)
- Statement: DATO for the series, absence for NP10679: the prototype 93-31 kept a 4.4-fold potency gain at acidic pH on GluN1/GluN2A/GluN2B triheteromers (Figure S1, not reached), and no source reached tests NP10679, or reports any maximum effect, on triheteromers.
- Source: 25728572; 36642931 · locator: 25728572 Results first section (triheteromer sentence; Figure S1 cited); 36642931 (no triheteromer text)
- Producer status/depth: read (sentence); supplement not reached · partial_fulltext_read; Figure S1 not seen, so the triheteromer maximum at either pH is unknown
- Kind/class: measured / compound/class
- System: Rat GluN1/GluN2A/GluN2B triheteromers in oocytes made as in Hansen 2014 (retention-tag method, per the Methods); conditions as D09 where stated; ifenprodil's 88 and 32 percent maxima (24607230) are not carried to any compound here

### D14 — NP10679
- Statement: DATO (declared; the primary values are unpublished or in 34493631 which I could not open): NP10679 is a histamine H1 antagonist (IC50 73 nM, same units and perimeter as the authors), inhibits hERG about 30-fold more weakly than it inhibits GluN2B receptors (hERG IC50 620 nM), and shows no demonstrable activity at more than 40 CNS targets; sedation was the dose-limiting effect in rat and dog repeat studies.
- Source: 36642931 · locator: Introduction, paragraph describing selectivity and safety pharmacology
- Producer status/depth: read · partial_fulltext_read as in D08
- Kind/class: declared / compound/class
- System: Developer-affiliated authors; assay systems for the H1 and hERG values not stated in the passage; some neighbouring values are marked unpublished in the source; an H1 action is a confound for any behavioural, EEG or network readout in a sedation-sensitive preparation, not for an isolated recombinant or slice current

### D15 — NP10679
- Statement: DATO (absence within the perimeter): no slice or native-tissue datum for NP10679 (region, age, bath pH) was found; the only slice paper that names the compound (human neocortical slices exposed to subarachnoid-haemorrhage CSF, 41310384) cites it in the Discussion and did not apply it; the compound's in-vivo data are a mouse SAH model and a mouse MCAO model (neither a bath-pH experiment).
- Source: 41310384 (keyword passages); 39892986 (abstract only); 36642931 Introduction · locator: 41310384 Discussion; 39892986 abstract; PubMed and Europe PMC query list
- Producer status/depth: read (keyword passages of 41310384); abstract_only (39892986) · partial reading of 41310384; 39892986 abstract only (JPET publisher page not opened); 34493631 not opened, so a slice or native datum inside it or inside 39892986 cannot be excluded
- Kind/class: declared / absence
- System: Perimeter: PubMed NP10679 OR NP-10679 (6 hits), Europe PMC NP10679 (13 hits), NP10679 with slice or hippocampus or cortical (8 hits), NP10679 with WWOX (0), all 2026-11-10; titles and abstracts screened, only 41310384 opened

### D16 — NP10679
- Statement: DATO: in healthy adult volunteers (48 in the single-administration study, median age 33.5, and 24 in the repeated-administration study, median age 44.5) NP10679 was reported to cause dose-dependent, atypical somnolence with ready arousal, no dissociative signal on CADSS or cognitive-test signal, no serious adverse events and no ECG signal in the first study; it says nothing about efficacy, any patient population, tissue acidity in humans, epilepsy or children, and ClinicalTrials.gov lists only these two phase 1 studies under the compound's names.
- Source: 36642931; ClinicalTrials.gov NCT03565861 and NCT04007263 · locator: 36642931 Results (participants, adverse events, Discussion); registry condition and enrolment fields
- Producer status/depth: read · partial_fulltext_read (full text through the PMC route; supplementary item not read; no image in the open bucket); registry fields only
- Kind/class: clinical / transfer from other system
- System: Healthy male and female adults aged 18-55, single centre per study, developer-sponsored; the somnolence characterisation is the attending physician's view as reported by the authors; ECG statement is for the single-administration study (the repeated-administration paragraph does not repeat it)

## B. Design items (S3_design.md)
- S3-1 (section 1): the preparation description (34634460 facts as carried from ampa_nmda_discrim_20261108/output/observations.tsv) — check against that table, not against the paper unless you can reach it.
- S3-2 (section 3, table rows A0–A7): for each explanation, predicted observation, compatible-not-discriminating, weakening result, null-interpreting control — logically right given the cited D-rows?
- S3-3 (section 3, A4): the claim that NP10679 adds a within-preparation specificity signature (burst effect following the recombinant pH-potency shift) — is it logically supportable, what else could produce a pH-following effect (proton inhibition of NMDAR itself, tissue state), and does it presuppose a property the sources do not give?
- S3-4 (section 4): the start set of controls; is any indispensable control deferred, is any listed control redundant, is the order right?
- S3-5 (section 4/5): thresholds presented as data that are design assumptions; the unit of replication.
- S3-6 (section 5): wording that turns a burst reduction into recovery or a response into a defect.
