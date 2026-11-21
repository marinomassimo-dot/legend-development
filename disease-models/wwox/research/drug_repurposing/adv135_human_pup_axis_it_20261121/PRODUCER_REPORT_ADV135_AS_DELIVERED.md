# ADV-135 producer report, as delivered (held human reports)

Delegate: legend-delegate, model sonnet, effort high (stated in the dispatch). Input: the pre-registered definitions, the list of 24 held human reports and four reviews, and the keyword listing as a cross-check only. The report below is the delegate's final message, persisted from the hand-back (the harness refuses subagent files); the harness's indentation is removed. Nothing in it is edited. Model and effort are read back in `RESULT_ADV135_IT_20261121.md`.

ADV-135 producer table: laboratory findings in human WWOX-DEE/WOREE/SCAR12 reports (sonnet, effort high, one delegate, local files only, no repository file edited)

LIMIT FIRST: I am the same model family as the Orchestrator; no clinician has read these sources.

READING METHOD AND DEPTH (what "full" means here)
- I converted every .xml/.html to plain text with a small python3 -I script (/tmp, outside the repo) and used the .txt files directly. For each report I ran a whole-text keyword scan with context, then read the case/clinical/results sections of the primary reports in full.
- The scan used the brief's terms plus: blood, urine, CSF, serum, screen, investigat, work-up, test, normal, unremarkable, hormon, endocrin, hypogly, insulin, electrolyt, TORCH, liver, renal, enzym, creatin.
- I did NOT read every line of Methods or reference lists, nor every paragraph of the four reviews. For the reviews I read the WWOX clinical paragraphs and every keyword hit.
- Quotes: ligatures (fi) and PDF end-of-line hyphenation are normalised; wording is otherwise verbatim. Ages and counts are as printed.
- The candidate TSV was used only as a cross-check; every sentence below comes from my own reading.

1. REPORT LIST
PMID | first author year | cohort (WOREE/SCAR12 cases) | reading depth | overlap
- 30356099 | Piard 2019 | 20 new WOREE (18 families) + literature review | text complete; Supp Tables 1-4 (xlsx) searched (all string cells; none contain a keyword) | Probable overlap with 28721938 (see below)
- 35792847 | Al Baradie 2022 | 9 new WOREE (Saudi, homozygous) + 61 literature cases in tables | complete (html text; case section read in full) | The 61 literature cases are a restatement of earlier reports. No stated overlap with other listed reports. Shared recurrent variants only (c.139C>A, c.160C>T, c.606-1G>A, c.689A>C); identity cannot be resolved from the text.
- 36779245 | Oliver 2023 | 13 WWOX-DEE | complete by scan; Tables 1-2 read; supplement not in files (only 2 jpg) | None stated in the main text
- 28721938 | Tarta-Arsene 2017 | 1 | complete | Probably the same patient as one Piard 2019 case. Piard Supp Table 1 has a Romanian patient with c.[173-1G>T];[c.918del], the same genotype and country as this report. Piard's author list includes Tarta Arsene. Not stated in either text.
- 27495153 | Elsaadany 2016 | 2 (siblings, Qatar) | complete (images only in supplement) | None stated
- 30853297 | Weisz Hubshman 2019 | 6 (3 families) | complete | None stated (shares p.Gln230Pro with others; not the same families)
- 35573960 | Riva 2022 | 1 | complete | None stated
- 30361190 | Shaukat 2018 | 2 | complete (two-column pdftotext; Table 1 read) | Table 1 restates earlier literature cases
- 42193054 | Sapuppo 2026 | 1 + 20-case literature table | complete | Literature table restates earlier reports
- 35712340 | Sukkar 2022 | 1 (homozygous c.406A>G; mild phenotype, no seizures) | complete; Tables 1-3 read | None. Borderline for the "WOREE/SCAR12 spectrum" definition: the authors call it "the first case of a WWOX-related phenotype" and rely on in silico pathogenicity.
- 42092735 | Serce Pehlevan 2026 | 1 neonate | complete | None
- 39416860 | Feng 2024 | 1 (5-month-old) | complete | None
- 39507621 | Teplyshova 2024 | 1 (40-year-old adult) | complete | None
- 37974179 | Dong 2023 | 1 | complete | None
- 36537114 | Chong 2023 | 5 (3 new + 2 previously published, "data updated") | PARTIAL. The file holds only Scholar Gateway chunks 0,1,2,18,22,23,24,25: abstract, Table 1, parts of Methods and Discussion. The narrative case descriptions of Patients 1-4 are not in the file. A JSON sibling exists; I did not read it (not named in the brief). | Which 2 patients were previously published is unresolved. Table 1's "reported in other studies" row cites Piard, Shaukat and Ben-Salem for variants.
- 29808465 | Johannsen 2018 | 2 (cousins) | complete | None
- 24369382 | Mallaret 2014 | 6 SCAR12 (Family 1: 4; Family 2: 2) | complete text; this file contains no patient-level clinical description beyond brief statements | Family 1 is the family of Gribaa 2007 (not a listed report)
- 24456803 | Abdel-Salam 2014 | 1 genotyped (II:4) + 1 phenotype-only sibling (II:1, not genotyped) | complete; Table 1 read; supplement pptx not read | None
- 25416187 | Tabarki 2015 | Review restating Mallaret (6) and Abdel-Salam (2), plus 3 unpublished Saudi siblings | complete | Restates 24369382 and 24456803
- 39101447 | You 2024 | 1 (13 months) | complete | None
- Reviews restating cases:
  - 33919646 Spagnoli 2021: neonatal-onset systematic review; WWOX paragraph "5/20 cases"; keyword scan complete, WWOX paragraphs read
  - 33255508 Aldaz 2020: scan complete, sections 3.1-3.2 read
  - 38161429 Battaglia 2023: neuroradiology review; scan complete, genetics section read
  - 33916893 Banne/Aqeilan 2021: "56 WOREE + 6 SCAR12 + 10 DECIPHER/ClinVar"; scan complete, Tables 1-2 read

2. FINDINGS PER REPORT
Only analyte rows with a stated finding are listed; the other rows are in section 3.
Abbreviations: Ca = calcium/PTH/vitamin D row; Phos = phosphate; Glu = glucose; Lip = lipids; Cort = cortisol/ACTH/adrenal; Thy = thyroid; GH = growth hormone/IGF-1; Gen = general work-up; G/F = growth/feeding.

AL BARADIE 2022 (35792847)
- Thy, ABNORMAL, neonatal (infant by definition), 1 of 9 (Patient 1.1). Locator: Case descriptions, Patient 1.1; preceding: "There is a history of polyhydramnios, but..."
  - "The mother has hypothyroidism, which was treated during pregnancy, and the baby had transient neonatal hypothyroidism."
  - No TSH/T4 value is given.
- Gen, NORMAL, 9 of 9. Age of testing is not printed for any patient (patients are described at 2y5m-15y). Not infant by definition.
  - P1.1 (preceding "His hearing and ophthalmological assessment were normal."): "Routine blood tests and basic metabolic screens for blood and urine, serum ammonia and lactate, and cerebrospinal fluid (CSF) neurotransmitters were unremarkable."
  - P1.2 (paragraph following her description, headed by "She has coarse facial features and a short neck."; preceding "She has two café-au-lait spots, severe spasticity..."): "Metabolic screens for blood and urine, ammonia, and lactate (serum and CSF) and basic laboratory tests were all unremarkable."
  - P2.1 (preceding "An ophthalmological assessment showed bilateral optic nerve atrophy."): "His basic laboratory tests, metabolic blood and urine screening, and very long chain fatty acids (VLCFAs) were all unremarkable."
  - P2.2 (preceding "She has marked hypertonia, DTRs of 2+, contracture..."): "Her basic laboratory tests, TORCH screening, blood and urine metabolic screening, serum ammonia, lactate, and VLFFAs were all unremarkable."
  - P3.1 (preceding "He has no spontaneous movement, marked hypertonia..."): "Metabolic screening for blood and urine, ammonia, and lactate were all unremarkable."
  - P3.2 (preceding "He has contracture in multiple joints and clubbed feet."): "His basic laboratory tests, blood and urine metabolic screening, lactate, and ammonia were unremarkable."
  - P4 (preceding "His ophthalmological examination was normal."): "Metabolic screening for blood and urine, ammonia, and lactate were all unremarkable."
  - P5 (preceding "An ophthalmological examination revealed bilateral optic atrophy."): "All basic laboratory tests and metabolic screening for blood and urine, ammonia, and lactate were unremarkable."
  - P6 (preceding "He is microcephalic with an HC of 45 cm; he is also hypertonic..."): "His basic laboratory tests and metabolic screening for blood and urine, serum ammonia, lactate, and VLFFAs were all unremarkable."
  - Calcium, glucose and lipids are never named in "basic laboratory tests" (not counted for those rows).
- G/F (not lab): failure to thrive 2 of 9 (P2.1, P2.2). Example: "She presented with severe failure to thrive and vomiting."
- ACTH appears only as a treatment abbreviation in Table 3 (not an adrenal finding).

ELSAADANY 2016 (27495153)
- Gen, NORMAL, 2 of 2.
  - Patient 1, age of testing not printed (patient is 7 years at report; she was in a vegetative state "currently"). Preceding: "Currently, she is severely impaired with intractable seizure and in a vegetative state." Quote: "Metabolic investigations including ammonia, lactate, plasma amino acids, urine organic acids, carnitine profile, plasma very long chain fatty acids, lysosomal enzymes studies, and CSF neurotransmitters, all were normal."
  - Patient 2, see Thy and Ca below.
- Ca (vitamin D only), NORMAL, 1 of 2 (Patient 2). Age not printed (20-month-old at report; the sentence follows the 16-month admission paragraph: not infant by definition, ambiguous). Preceding: "She had positive Babinski bilaterally." Quote: "She had plasma lactate, T4, TSH, AST, ALT, vitamin D, urine for organic acids, plasma and urine amino acids, CGH array, all were normal."
- Thy, NORMAL, 1 of 2 (same sentence; T4 and TSH named). Age as above.
- G/F (not lab): P2 "weight was 5.95 (-2.2 SD)" at 6 months; both patients needed nasogastric/gastrostomy feeding (P1 at 9 months, P2 at 8 months). P2 "healing right proximal humerus fracture" at 16 months (bone, not a lab finding).

WEISZ HUBSHMAN 2019 (30853297)
- Gen, 5 of 6 with a statement, no age printed for any test.
  - Family 1 elder sister, labelled II-1 in the text (see ambiguity 7). Preceding: "Developmental delay followed." Quote: "Extensive metabolic workup including muscle biopsy yielded no diagnostic findings." (Not the word normal: ambiguous.)
  - Family 2 proband II-5 (seizures from 2 weeks; MRI at 7 months follows). Preceding: "EEG showed right fronto-central epileptic focal discharges." Quote: "Extensive metabolic investigation was normal and brain MRI at the age of seven months demonstrated only thin CC."
  - Family 2 sister II-6. Preceding: "EEG showed multifocal bilateral epileptic activity, which transformed at the age of four months..." Quote: "Partial metabolic investigation was normal, and a head MRI was not performed due to parents' refusal."
  - Family 3 proband VI-3 (died at 9 months, so the test falls within the first 9 months, inferred not printed). Preceding: "EEG showed bilateral multi focal spikes and sharp waves." Quote: "Extensive metabolic investigation was within normal limits."
  - Family 3 brother VI-4 (last examination at 6 months; inferred within 6 months). Preceding: "EEG showed right centro-temporal epileptic focal discharges." Quote: "A comprehensive metabolic investigation was within normal limits."
  - Family 1 proband (II-2 in text): no statement.
- G/F (not lab): Family 1 proband "At the age of three months, she presented with failure to thrive, recurrent vomiting, and recurrent episodes of convulsions." (1 of 6, infant). Family 3 proband: "Examination at three months of age demonstrated poor growth with weight at -2SD".

RIVA 2022 (35573960)
- Glu, ABNORMAL, hours after birth (infant), 1 of 1. Preceding: "Birth weight was 3,100 g (90°centile), length 51 cm (97°centile)..." Quote: "A few hours after birth, he presented hypoglycemia, respiratory distress associated to tonic-clonic seizures, and horizontal nystagmus." No glucose value is given.
- Gen, NORMAL, 1 of 1, age not printed (the paragraph follows the description of the patient's course after age 3 years). Preceding: "The multi-daily seizures, up to 50 attacks per day, strongly disturbed his sleep." Quote: "Specific tests for metabolic disorders (including neurotransmitters, folate, pterins, amino and organic acids, carnitine profile, plasma very long-chain fatty acids) were performed both on cerebrospinal fluid (CSF), blood and urine samples resulting within normal limits."
- Brain MR spectroscopy "small lactate peaks" at 4 months and "absence of lactate peaks" at 2y4m are imaging, not a blood/CSF lactate.
- G/F (not lab): "At 3 years, gastrostomy was placed due to failure to thrive and severe gastroesophageal reflux."
- "three cycles of ACTH" is treatment, not an adrenal finding.

SHAUKAT 2018 (30361190)
- Gen, NORMAL, 2 of 2. No test age printed. Reading-order ambiguity from the two-column layout.
  - Child 1 (its first column ends "...one of them died at the age of four years."): "The following investigations were normal: lactate, ammonia, acylcarnitine, uric acid, homocysteine, plasma amino acids, urine organic acids, and transferrin isoforms."
  - Child 2 (12-month-old at report; evaluated at 11 months; preceding "The child was the first born to first-cousin parents, with unremarkable family history."): "The following investigations were normal: echocardiogram, lactate, ammonia, acylcarnitine profile, uric acid, homocysteine, plasma amino acids, urine organic acid, and urine sulfocystine."
- G/F (not lab): both "consistent with failure to thrive and acquired microcephaly" (child 1 at 6 months, child 2 at about 11 months) = 2 of 2, infant. Example: "weight 5.1 kg (SD: -3.95), length 61.6 cm (SD: -2.86)".

SAPUPPO 2026 (42193054)
- Gen, NORMAL, 1 of 1. The age of testing is not printed; the narrative places it in the neonatal admission (after "8 days of life", before "Brain MRI at 10 days of age"; the infant died after about 3 months). Infant by context, not by a printed age. Preceding: "The EEG pattern strongly indicated early infantile epileptic encephalopathy." Quote: "Blood tests for metabolic disorders were performed, resulting within normal limits." No analyte is named.
- G/F: only "vomiting" (neonatal seizures "accompanied by vomiting") and microcephaly. No lab finding.

SUKKAR 2022 (35712340). Age of testing not printed; patient is 21 months at the time of writing, so not infant by definition.
- Lip, ABNORMAL (low), 1 of 1. Preceding: "Liver profiles, including ALT and GTT, were normal, whereas AST, albumin, total bilirubin..." Quote: "The lipid profile revealed low cholesterol triglyceride levels." Table 1 lists only "Triglyceride - Low"; cholesterol is not in the table (ambiguous).
  - Discussion: "As shown in our case, the lipid profile was low, which can be attributed to the WWOX gene, as it has been reported to be involved in the regulation of lipid homeostasis and metabolism [13,14]."
- Thy, NORMAL, 1 of 1. Preceding: "Anti-smooth muscle antibody test showed the following results..." Quote: "The TSH and free T4 levels were within the normal range."
- Ca (vitamin D only), ABNORMAL (high), 1 of 1. Preceding: "Creatine kinase was high." Quote: "25-OH vitamin D and vitamin B12 levels were high." Table 1: "25-OH vitamin D - High".
- Gen, MIXED, 1 of 1. Preceding: "Bowing of the legs and flat feet were noticed." Quote: "Metabolic investigations revealed normal levels of urine organic acids and all plasma amino acids except for slightly elevated alpha aminobutyric acid and a marked decrease in cystine level (Table 1)." Table 2 lists amino-acid values with reference ranges.
- Other laboratory findings (not among the 8 rows): AST, albumin, total and direct bilirubin high, globulin low, creatine kinase high, vitamin B12 high.
- Calcium, phosphate, PTH, glucose, cortisol and GH are not named. "Bowing of the legs" is a physical sign (bone), not a lab finding.

SERCE PEHLEVAN 2026 (42092735). Neonate; events dated by postnatal day.
- Thy, NORMAL, 1 of 1. Age: between "On day 14" and discharge on postnatal day 23 (infant by context). Preceding: "Phenobarbital was initiated with a loading dose followed by maintenance therapy at 5 mg/kg/day..." Quote: "Auditory brainstem response testing and thyroid function tests were within normal limits."
- Gen, NORMAL, 1 of 1, same window. Preceding: "Ophthalmologic evaluation showed no signs of optic atrophy or additional structural abnormalities." Quote: "A comprehensive metabolic evaluation, including serum ammonia and creatine phosphokinase levels, blood gas analysis, acylcarnitine profile, plasma and urine amino acids, and urine organic acids, revealed no abnormalities."
  - CSF neurotransmitters: "Cerebrospinal fluid (CSF) neurotransmitter analysis was not performed."
  - Discussion (general, cites ref [4]): "However, metabolic investigations are typically normal in WWOX deficiency, highlighting the importance of early genetic testing for accurate diagnosis [4]."
- G/F: "poor feeding" on admission. "A right clavicle fracture was noted." is not a lab finding.

JOHANNSEN 2018 (29808465)
- Gen, NORMAL, first year of life (infant), 1 of 2 (Patient 1). Preceding: "She has not acquired any developmental milestones." Quote: "In the first year of life, extensive neurometabolic work-up in blood, urine, and cerebrospinal fluid revealed no abnormalities."
- Patient 2: no result stated. The Methods only say charts were reviewed for "the laboratory (including metabolic and genetic)".
- G/F (not lab): "gastrostomy was placed due to feeding difficulties and failure to thrive" (Patient 1, age 5 years); "gastrostomy was placed due to failure to thrive" (Patient 2) = 2 of 2.

ABDEL-SALAM 2014 (24456803)
- Gen, NORMAL, 1 of 1 genotyped patient (II:4). Test age not printed (died at 16 months). Preceding: "Chromosomal examination from peripheral blood lymphocytes revealed a normal female karyotype, 46,XX." Quote: "Normal results were found in metabolic screening including liver and renal function tests, complete blood count, blood gas analyses, ammonia, serum lactate, plasma urea, electrolytes, urine and serum amino and organic acids, and very long chain fatty acids."
  - Calcium, glucose and lipids are not named; "electrolytes" is unspecified (ambiguity 3).
  - Table 1, patient II:4 row: "No metabolic disorder", "Normal blood count".
  - Discussion: "Metabolic disease has been reported in Wwox-deficient mice (see legend for Table 1), but was not evident during her short life in patient II:4."
- NON-HUMAN statements in the same paper (excluded from all counts): Table 1 footnote 3 for the knockout mouse: "Hypoproteinemia, hypoglycemia, hypocalcemia, hypotriglyceridemia, hypocholesterolemia, hyponatremia, hyperkalemia, hypochloremia". Table 1 also lists "Bone metabolic disease (mild)" for the rat and "(severe)" for the mouse.
- G/F (not lab): "neonatal growth retardation"; at 12 months weight "-3.6 SD", length "-2.9 SD". Sibling II:1 not examined.

YOU 2024 (39101447)
- Gen, NORMAL, 1 of 1. Test age not printed (13-month-old at last follow-up, so within about 13 months: infant status ambiguous). Preceding: "Brainstem auditory evoked potentials revealed a delayed right auditory conduction pathway (Figure 6), and EMG of the upper and lower limbs suggested peripheral nerve damage (Figure 7)." Quote: "Blood and urine tandem mass spectrometry showed no abnormalities." (Methods: "urine tandem GC/MS"; analytes not named.)
- G/F (not lab): "malnutrition"; "Before the last follow-up, at 13 months old, she weighed 4000 g."

TARTA-ARSENE 2017 (28721938)
- Gen, NEGATIVE (wording is "negative", not "normal"), 1 of 1. The paragraph follows the MRI at 2.6 years (not infant by context, ambiguous). Preceding: "Considering the aspect of cerebral MRI, which showed a neurodegenerative disease affecting mainly the grey matter, metabolic disorders were taken into consideration in the differential diagnosis."
  - Quote 1: "Specific tests for disorders of small molecules (involving amino and organic acids, fatty acids, neurotransmitters, the urea cycle, vitamins, cofactors, and mitochondria)" [then lysosomal, peroxisomal and glycosylation tests, omitted] "...were performed."
  - Quote 2: "These results were negative, and a genetic aetiology of the epileptic encephalopathy was considered"
  - Abstract: "Metabolic disease was excluded."
  - "Vitamins" is named generically; vitamin D is not named.
- ACTH: "Synthetic ACTH was added" is treatment (not an adrenal finding).
- G/F: "normal somatic growth" at 2.6 years (no failure to thrive).

CHONG 2023 (36537114), PARTIAL text
- No finding for the 8 rows in the delivered chunks.
- Other lab findings: "Recurrent pancreatitis was found in one of the subjects ... pancreatic enzymes were persistently elevated and did not resolve with change of anticonvulsant medications." (1 of 5; age not stated; the patient is "Alive at 8years").
- Table 1 "Abdominal" row: "Mild microvesicular and macrovesicular hepatosteatosis, mild hepatosplenomegaly on autopsy" (1 of 5).
- G/F (not lab): Table 1 "Failure to thrive: Yes, from 12months / Yes / Yes / Yes / Yes" = 5 of 5. Discussion: "each of them eventually developed failure to thrive and exhibited growth delay."

3. NOT REPORTED
Terms searched, as listed in the brief: calcium, calcemi, Ca, phosph, PTH, parathyroid, vitamin D, glucose, glyc, sugar, lipid, cholest, triglycer, cortisol, adrenal, ACTH, thyroid, TSH, T4, growth hormone, IGF, metabolic, laborator, biochem, lactate, ammonia, amino acid, organic acid, carnitine, VLCFA, bone, rickets, osteopen.
Hits that were not human laboratory findings are listed here by name:
- Gene/protein text: "amino acid" (protein residues), "phosphorylation", "glycogen synthase kinase", "glycine".
- Treatment, not an adrenal finding: ACTH (Oliver, Al Baradie Table 3, Tarta-Arsene, Riva, You Discussion).
- Institution names containing "Laboratory/Metabolic".
- Mouse/rat statements: Abdel-Salam, Aldaz, Battaglia, Aqeilan, Teplyshova.

Per-report NOT REPORTED rows (complete text searched for the terms above, except Chong which is partial):
- Piard 2019 (main text + Supp Tables 1-4): NR for Ca/PTH/vit D, Phos, Glu, Lip, Cort, Thy, GH, Gen.
  - Closest items: Supp Table 1 row "Neonatal findings (except seizures)" lists "feeding problems (weight loss), jaundice" (1 patient; jaundice is not among the 8 rows); text "jaundice (each in one case)".
  - G/F: "Feeding difficulties were observed in most of the patients and 13/19 (70%) required a feeding tube" (preceding "Scoliosis or kyphosis was present in 13 of 20 (65%) patients."). "Mean height was -1,1 SD with only one patient under 3 SD (1/17; 6%)."
- Oliver 2023: NR for all 8 rows. Gen is also NR (no metabolic work-up named). G/F, Table 1: "Short stature" Yes 7 of 13 (footnote: height 3 SD below the mean), "Feeding tube" Yes 11 of 13.
- Al Baradie: NR for Ca, Phos, Glu, Lip, Cort, GH.
- Elsaadany: NR for Ca (calcium/PTH), Phos, Glu, Lip, Cort, GH.
- Weisz Hubshman: NR for Ca, Phos, Glu, Lip, Cort, Thy, GH.
- Riva: NR for Ca, Phos, Lip, Cort, Thy, GH.
- Shaukat: NR for Ca, Phos, Glu, Lip, Cort, Thy, GH.
- Sapuppo: NR for Ca, Phos, Glu, Lip, Cort, Thy, GH.
- Sukkar: NR for calcium/PTH, Phos, Glu, Cort, GH.
- Serce Pehlevan: NR for Ca, Phos, Glu, Lip, Cort, GH.
- Feng 2024: NR for all 8 rows, including Gen. The only blood value named is a phenobarbital blood concentration (a drug level). G/F: "The child exhibited good physical development".
- Teplyshova 2024: NR for all 8 rows. Wwox-null mouse "hypoglycemia" appears only in a gene-therapy paragraph (mouse, excluded).
- Dong 2023: NR for all 8 rows. G/F: "The affected individual growth retardation and developmental delay"; at death (2.5 y) "69 cm (-6SD) in height and 8 kg (-4SD) in weight".
- Johannsen: NR for Ca, Phos, Glu, Lip, Cort, Thy, GH (Gen stated for 1 of 2 only).
- Mallaret 2014: NR for all 8 rows. Only clinical item: "muscle biopsy showed vacuolization of the sarco-tubular system" (restating earlier work; not among the rows).
- Abdel-Salam: NR for Ca (not named; electrolytes unspecified), Phos, Glu, Lip, Cort, Thy, GH in humans.
- Tabarki 2015 (review + 3 unpublished siblings): NR for all 8 rows. G/F: "refractory seizures, spasticity, microcephaly, failure to thrive, and early death" (3 siblings; group statement) and, restating Abdel-Salam, "severe failure to thrive".
- You: NR for Ca, Phos, Glu, Lip, Cort, Thy, GH. The Discussion line "WWOX affects lipid metabolism and damages the integrity of the myelin sheath" is mechanistic, not a case result.
- Chong: NR within the delivered chunks only. The case narratives were not delivered, so NR here is limited to Table 1, Abstract and Discussion.
- Review restating (Spagnoli 2021, Aldaz 2020, Battaglia 2023, Aqeilan/Banne 2021): NR for all 8 rows in human cases. Mouse-only statements, excluded from every count:
  - Aldaz: "Wwox-KO mice display significant growth retardation (dwarfism) and metabolic deficits, including severe hypoglycemia, hypocalcemia, as well as signs of metabolic acidosis and kidney failure [33]."
  - Battaglia: "growth retardation, hypoglycemia, hypolipidemia, impaired steroidogenesis, bone defects" (-/- mice).
  - Aqeilan/Banne: "severe metabolic disorder (hypoglycemia, hypolipidemia, impaired steroidogenesis, and bone metabolic phenotypes)" (WWOX KO mouse).
  - Aldaz also cites human GWAS "association between low levels of HDL-C and WWOX", which is not a WOREE/SCAR12 case finding.
  - Spagnoli: no WWOX lab statement.
- No report in the set mentions phosphate (human), cortisol/adrenal findings, or growth hormone/IGF-1 (searched: phosph, cortisol, adrenal, ACTH, growth hormone, IGF).

4. CROSS-TAB
Codes: N = normal, A = abnormal, NR = not reported. Fractions are n of N cases in the report's own denominator. "(inf)" = infant age by definition or by narrative context; "(ni)" = age not printed or beyond 12 months. Calcium and PTH are NR in every report. The Ca column below therefore shows vitamin D only.

PMID | Ca/PTH (vit D) | Phos | Glu | Lip | Cort/ACTH | Thy | GH/IGF | Gen
- 30356099 Piard | NR | NR | NR | NR | NR | NR | NR | NR
- 35792847 Al Baradie | NR | NR | NR | NR | NR | A 1/9 (inf, neonatal hypothyroidism) | NR | N 9/9 (ni)
- 36779245 Oliver | NR | NR | NR | NR | NR | NR | NR | NR
- 28721938 Tarta-Arsene | NR | NR | NR | NR | NR | NR | NR | N (negative) 1/1 (ni by context)
- 27495153 Elsaadany | N (vit D) 1/2 (ni) | NR | NR | NR | NR | N 1/2 (ni) | NR | N 2/2 (ni)
- 30853297 Weisz Hubshman | NR | NR | NR | NR | NR | NR | NR | N 5/6 (age not printed; 2 of the 5 within the first 9 months by inference; 1 of the 5 worded "no diagnostic findings")
- 35573960 Riva | NR | NR | A 1/1 (inf) | NR | NR | NR | NR | N 1/1 (ni)
- 30361190 Shaukat | NR | NR | NR | NR | NR | NR | NR | N 2/2 (age not printed; cases are 12 months or younger at report for child 2)
- 42193054 Sapuppo | NR | NR | NR | NR | NR | NR | NR | N 1/1 (inf by context)
- 35712340 Sukkar | A (vit D high) 1/1 (ni) | NR | NR | A 1/1 (ni) | NR | N 1/1 (ni) | NR | mixed 1/1 (ni)
- 42092735 Serce Pehlevan | NR | NR | NR | NR | NR | N 1/1 (inf by context) | NR | N 1/1 (inf by context)
- 39416860 Feng | NR | NR | NR | NR | NR | NR | NR | NR
- 39507621 Teplyshova | NR | NR | NR | NR | NR | NR | NR | NR
- 37974179 Dong | NR | NR | NR | NR | NR | NR | NR | NR
- 36537114 Chong (partial) | NR | NR | NR | NR | NR | NR | NR | NR
- 29808465 Johannsen | NR | NR | NR | NR | NR | NR | NR | N 1/2 (inf, "first year of life")
- 24369382 Mallaret | NR | NR | NR | NR | NR | NR | NR | NR
- 24456803 Abdel-Salam | NR | NR | NR | NR | NR | NR | NR | N 1/1 (age not printed)
- 25416187 Tabarki | NR | NR | NR | NR | NR | NR | NR | NR
- 39101447 You | NR | NR | NR | NR | NR | NR | NR | N 1/1 (age not printed, at most 13 months)
- Reviews (4) | NR | NR | NR | NR | NR | NR | NR | NR

CALCIUM
- Independent reports stating normal at an infant age: 0.
- Independent reports stating abnormal at an infant age: 0.
- Reports naming calcium at all for humans: 0.
- Work-ups that might include calcium but do not name it (not counted per definition): "electrolytes" in Abdel-Salam; "basic laboratory tests" / "routine blood tests" in Al Baradie.
- Mouse hypocalcemia is stated in Abdel-Salam (Table 1 footnote) and Aldaz (excluded from counts).
- Vitamin D (the only member of that row ever named): normal 1 of 2 in Elsaadany (age not printed, about 16-20 months by context); high 1 of 1 in Sukkar (age not printed, 21 months at writing).

LIPIDS
- Independent reports stating normal at an infant age: 0.
- Independent reports stating abnormal at an infant age: 0.
- The only human lipid statement is Sukkar (low; age not printed; 21 months at writing; the paper's pathogenicity claim and spectrum membership are borderline).
- Mouse hypolipidemia is stated in Battaglia and Aqeilan/Banne (excluded from counts).

OVERLAP FOUND
- Tarta-Arsene is probably the same patient as one Piard case. Neither report states calcium or lipids, so this does not change any tally.
- Chong includes 2 previously published patients (unidentified).
- Tabarki restates Mallaret and Abdel-Salam.
- Reviews and the literature tables of Al Baradie and Sapuppo restate earlier cases.
- Outside Chong's two unidentified patients, no other overlap is stated in any text; overlap by shared recurrent variants cannot be resolved from the files.

5. AMBIGUOUS SENTENCES
1. Age of testing is not printed for the general work-up statements in Al Baradie (9 patients), Elsaadany (2), Riva, Shaukat (2), Abdel-Salam, You, Weisz Hubshman (5), Tarta-Arsene. I coded these "(ni)", or by inference where a death or last-examination age bounds the test. The inference-only cases are Weisz Hubshman Family 3 (test within 9 months and within 6 months) and You (13 months at last follow-up). Sapuppo and Serce Pehlevan are infant only by narrative sequence (neonatal admission), not by a printed test age.
2. Weisz Hubshman Family 1 elder sister: "Extensive metabolic workup including muscle biopsy yielded no diagnostic findings." The word is not "normal"; the sentence does not state that any named analyte was normal.
3. "Electrolytes" (Abdel-Salam), "basic laboratory tests" and "routine blood tests" (Al Baradie), "all basic laboratory tests" and "metabolic screening" (generic): none names calcium, glucose or lipids, so none is counted for those rows. Whether the unspecified panels include them is not stated.
4. Tarta-Arsene: "These results were negative" ("negative", not "normal"), and the sentence follows the 2.6-year MRI, so its age is probably not infant. The list includes "vitamins" without naming vitamin D. The abstract says "Metabolic disease was excluded".
5. Sukkar: the text says "ALT and GTT were normal"; Table 1 says "ALT - Low, GGT - Low". The text says "low cholesterol triglyceride levels"; Table 1 lists "Triglyceride - Low" only. Table 3 and the Discussion state a "low lipid profile", with no value or reference range. Age of the investigations is not printed. Whether this case belongs to the WOREE/SCAR12 spectrum is borderline.
6. Al Baradie P1.2's work-up sentence sits in a paragraph that begins "She has coarse facial features...", detached from her case paragraph by HTML order. I attributed it to P1.2 from the 15-year age and p.Pro47Thr. P3.2's and P6's continuations were attributed the same way.
7. Weisz Hubshman: the text calls the elder sister II-1 and the proband II-2; the Fig. 2 legend labels the 18-month MRI as II-1 and the 33-month MRI as II-2, the reverse of the text. Which sister the work-up sentence belongs to is therefore uncertain (the family has 2 affected sisters; the count 5 of 6 is unaffected).
8. Shaukat's two-column text interleaves in the extracted layout. I assigned "The following investigations were normal ..." to child 1 and child 2 by column order; verify against the PDF if used for a headline.
9. Al Baradie P1.1: "the baby had transient neonatal hypothyroidism" is a history statement. No TSH/T4 value, no date and no basis for the diagnosis are given.
10. Riva's "small lactate peaks" and "absence of lactate peaks" are MR spectroscopy (imaging), not a laboratory lactate.
11. Chong: partial text. The two "previously published" patients and any narrative laboratory statements in Patients 1-4 are not in the file. NR is therefore valid only for the delivered chunks.
12. Elsaadany Patient 2: the thyroid/vitamin D sentence appears after the 16-month admission paragraph, so its age is probably 16-20 months, but it is not printed.
13. Abdel-Salam: the "No metabolic disorder" cell in Table 1 and the Discussion sentence refer to the single patient II:4; the sibling II:1 was not examined. The mouse footnote (hypoglycemia, hypocalcemia, hypotriglyceridemia, hypocholesterolemia) is a mouse finding and is quoted only so it is not mis-counted.
14. Tabarki: "failure to thrive" is a group statement for 3 unpublished siblings (count 3 of 3 assumed, not stated per sibling).
15. Mallaret's file text contains no patient-level clinical table. The absence of lab statements applies to this file's text only.

ROUTE NOTES (not defects in the sources)
- Not read as text: Piard figures; Abdel-Salam supplement pptx (S1) and jpg; Elsaadany and Oliver image assets; Chong JSON sibling.
- Piard EPMC xml was not opened (same article as the PMC xml; Supp Tables 1-4 xlsx were read as text).
- No external service, web fetch or PubMed call was made; no repository file was edited; no e-mail address was sent anywhere.
- Scratch files are in /tmp (p135_txt, p135_conv.py, p135_grep.py, p135_grep2.py) and can be deleted.
