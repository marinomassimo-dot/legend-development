# P3-02 ramelteon: DROP (insufficient support; potent at its receptor, no supporting record, target not detected)

Scientist-a3, 2026-10-30. Not medical advice.

**Proposal as generated.** Seed BNIP3 transcript up (S021). Path MTNR1A -> GNAO1 -> HES1 -> BNIP3 (net +1); action "mimics" (Z total -4.26, in-degree -3.76): the compound would RAISE the BNIP3-type signal, i.e. push toward the WWOX-loss pattern.

## 1 Identity
CHEMBL1218, InChIKey YLXDSYKOBKBWJQ-LBPRGKRZSA-N; PubChem CID 208902 by the same key and by name; synonyms Rozerem, TAK-375. Parent, no salt.

## 2 Target, action, measures
Curated mechanism: melatonin receptor agonist (label reference). Human MT1 Ki 0.0138 and 0.014 nM, MT2 Ki 0.045 and 0.112 nM (CHO or recombinant, two documents CHEMBL1135782 2002 and CHEMBL4834409 2021); cAMP IC50/Ki ratio 1.51 for MT1. 334 of 334 rows (complete). Off-target single rows are screens (HDAC6 inhibition, AC50 on COX-1, M1, alpha-1A, thromboxane receptor); not interpreted. Ion channels: in Neuro-2a cells INa IC50 8.7 uM and IK(DR) IC50 2.9 uM (abstract, PMC11452446).

## 3 Exposure and nervous system
Label: absolute oral bioavailability 1.8 percent (absorption at least 84 percent, extensive first pass), Tmax 0.75 h, half-life 1-2.6 h, M-II 20-100 fold the parent exposure, protein binding about 82 percent; paediatric safety and effectiveness not established. Rat 10 mg/kg i.p. at 1 h: brain 390 nM, plasma 580 nM (ChEMBL document CHEMBL1667823; one time point). No human CSF datum found. One case report of ultra-low-dose use in a severely handicapped child (PubMed title).

## 4 Safety and counter-evidence
Anticonvulsant effects in two rodent models (rat kindling, Kcna1-null mouse; 30 and 100 mg/kg i.p. twice daily) and attenuation of kainate-induced neuronal loss (abstracts). Label: decreased testosterone and increased prolactin; "effect on reproductive axis in developing humans is unknown". openFDA counts (no rates): 7,349 reports; seizure 61, convulsion 44, epilepsy 30, status epilepticus 5, generalised tonic-clonic seizure 6. Seizure-provoking evidence: none found; neurodevelopmental toxicity study: none found.

## 5 Edge provenance (the decisive part)
`edge_provenance_judged.tsv`. The chain has three records from three unrelated contexts:
1. MTNR1A -> GNAO1 (+1), SIGNOR, PMID 31160049 (Cell 2019, G-protein coupling selectivity of GPCRs): a coupling record, not a change in GNAO1 amount or a transcript.
2. GNAO1 -> HES1 (-1), SIGNOR, PMID 39580518 (Oncogene 2025, abstract): GNAO1 OVEREXPRESSION in glioma stem-like cells recruits TRIM21, degrades CREB, lowers H3K27ac at the HES1 promoter. Real in its context; it is about GNAO1 abundance, which an agonist does not alter.
3. HES1 -> BNIP3 (-1), CollecTRI, PMID 24402046 (J Invest Dermatol 2014, abstract): Hes1-null mouse epidermis transcriptome; keratinocytes.
No record measures receptor activation followed by a BNIP3 transcript change. As a prediction that ramelteon changes BNIP3 in neural cells the chain is a context-free artefact. MTNR1B -> GNAO1 gives the same chain, so no independent second route.

## 6 Expression
WWOX-KO organoid (4 KO, 2 WT, CPM): MTNR1A 0.00-0.10, MTNR1B 0.00-0.10; both absent from the hNPC CAGE table. HPA adult: MTNR1A not detected in brain snRNA; MTNR1B 1.6-5.3 nCPM in inhibitory neurons, ependymal cells, medium spiny neurons. The seizure-model paper reports melatonin-receptor induction in astrocytes (abstract), a context not present in the WWOX data. Sensitivity limits of bulk and snRNA data are acknowledged.

## 7 Trials registry
2026-10-30: ramelteon 80 studies; 0 with each neurological or neurodevelopmental condition searched.

## 8 Feasibility and decision
Experiment feasible but pointless in these systems (no receptor transcript). Promise LOW; depth MEDIUM; feasibility HIGH to run, but no target in the system; priority NONE. "Insufficient support", not "no activity" of the compound. Transfer limits: one transcript seed; mimics direction.
UNVERIFIED: the cell line of the coupling record; full texts of PMID 31160049, 39580518, 24402046 not opened; receptor protein not measured anywhere.
