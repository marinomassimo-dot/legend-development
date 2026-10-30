# P3-19 lenalidomide (artefact control; same edge as pomalidomide)

Decision: **REFERENCE-ONLY, artefact CONFIRMED.** Why: (1) it reaches the seed through the mislabelled "CRL4(CRBN) inhibitor" coding and the single TRPC4AP-based CUL4 record, not through a mechanism the compound uses; (2) the IMiD mechanism (IKZF1/3 degradation) lowers MYC in myeloma, the opposite of the coded sign; (3) the catalogue links it to 8 signed targets and the same edge as pomalidomide, so it adds no independent line of evidence (a count of compounds on one edge is not a result).

* Identity: CHEMBL848, InChIKey GOTYRUGSSMKFNF-UHFFFAOYSA-N (racemic mixture); PubChem by name and by key agree; **VERIFIED**; the hydrochloride monohydrate is a separate record (CHEMBL6068337).
* Measures (human, nM, type B): CRBN Kd 57 to 178, IC50 81 to 37,800 (11 rows, 10 documents), Ki 800 to 16,300; IKZF1 DC50 90 to 120, IKZF3 EC50 50 to 87; IRF4 IC50 only as ">" (one censored row); TNF IC50 220 and IL1B 390 (single rows). ChEMBL mechanism: same "CRL4(CRBN) inhibitor" coding as pomalidomide.
* Label (Aurobindo generic, 2023): boxed warning embryo-fetal toxicity ("caused limb abnormalities in a developmental monkey study"), haematological toxicity, venous and arterial thromboembolism; half-life 3 h healthy and 3 to 5 h in patients; "safety and effectiveness have not been established in pediatric patients"; REMS. No seizure term in the retrieved sections; FAERS seizure 806 of 420,080 (0.19 percent; reports).
* Trials: 1,322 studies in total; epilepsy/seizure slice 1 hit that is a Japanese post-marketing lymphoma surveillance record (a text-match false positive, NCT03098589); neurodevelopment 1 (an autism trial in children, completed, NCT00996931; outcome not retrieved); CNS tumour 34; paediatric terms 73.
* Expression and edge: as pomalidomide.
* Use: keep as a **negative control** for any future glue experiment (it shares the IKZF1/3 mechanism and edge). No next experiment of its own.
