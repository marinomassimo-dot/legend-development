# ADV-287 extension, A01: FIRST READER report as delivered (legend-delegate; models {'claude-sonnet-5-5': 115}; effort {'high': 115}; reply text extracted verbatim from its transcript hand-back call; 2026-11-26)

FIRST READER REPORT, card A01 (A01_pba_class), 14 sentences. Date of all searches and checks: 2026-11-26. Effort high, model sonnet.

COUNTS: CORRECT 9 (A01-02, 05, 06, 07, 10, 11, 13, 14, 16); ADD 3 (A01-08, 09, 15); INCOMPLETE 2 (A01-03, 04); WRONG 0; NOT ASSESSABLE 0.
Partly not assessable inside a class: A01-10 (only repository tables held, the ChEMBL answers are not in files/); A01-06 (the clause "dominant-negative mechanism WWOX does not have" is a WWOX premise, not a Guiberson fact; the paper does state dominant-negative); A01-07 (the "reader error" is the repository reader's own estimate).

MEASUREMENT METHOD (all Guiberson 2018 figure values). Main figures were held only as low-resolution JPGs (Fig 6 is 686 px wide), so I measured pixel bar heights from the control bar and the axis, and I looked at upscaled crops. Error is about ±1 px, which is ±1.5 to 2 percent of axis. Supplementary Fig 12 was rendered at 8x from the vector PDF and read by eye (about ±5 units). The repository tables munc18_quantity_function_arithmetic and munc18_cytosolic_precedent_panel_readings were opened only after my own measurements, as pointers. My pixel values agree with their values.

Values I measured in Guiberson 2018 (mouse cortical neurons, lentiviral human cDNA, Munc18-1-null background unless stated), used in several blocks:
- Fig 3a (n=3 independent experiments; total protein as % of WT): P335L 65, R406H 7, P480L 3.5, G544D 5, G544V 9 (±2 points).
- Fig 6a (n=5; 4-PBA fold of the control bar): WT 1.27 (*), P335L 1.84 against its own control bar, which sits at about 84 rather than 100, or 1.39 against 100 (**), R406H 1.30 (*), P480L 1.03 (no mark), G544D 1.64 (**), G544V 1.33 (no mark).
- Fig 6b (n=5; Triton-soluble % of total, control to 4-PBA): P335L 75 to 77; R406H 31 to 55 (*), ratio 1.77; P480L 14 to 34 (*), 2.4; G544D 31 to 70 (**), 2.26; G544V 22 to 38 (*), 1.7.
- Fig 6d (n=4; antibody-uptake pixel count): WT about 57.8; control about 47 (P335L), 31 (R406H), 22 (P480L), 34 (G544D), 35 (G544V); 4-PBA about 44 (R406H), 82 (P480L), 74 (G544D), 74 (G544V).

---

A01-02. CORRECT.
Opened: full text (Shah 2025 PMC XML), figure image (Fig 6, file g004.jpg, panels G and H).
Evidence: Shah Fig 6G, G443D flies: control about 46 percent, 10% glycerol about 42, 1 mM 4-PBA about 49, no mark; the text says glycerol "statistically insignificant" for both mutants.

A01-03. INCOMPLETE.
Opened: Supp Fig 12a, 12b and 12c (vector PDF page 19, rendered 8x, by eye), main Fig 6a, full text.
What holds: every number in the sentence.
- Fig 12b (HEK293T, n=3 independent experiments, 200 mM): G544D sorbitol about 105 percent of control, unmarked; G544D trehalose about 235 (*).
- Fig 12a, G544D, 400 mM: sorbitol about 78, trehalose about 90.
- The mismatch with 12a is real: 12a shows 200 mM sorbitol at about 178 (*).
What is left out: "no sorbitol effect is established" and "the osmolyte arm rests on trehalose" hold only for G544D in HEK293T. The same source shows sorbitol effects elsewhere.
- Fig 12b, other variants: R406H about 199 (***), G544V about 157 (**).
- Fig 12c, yeast: G544D about 270 (**).
- Fig 6a, neurons (mouse, n=5): P335L about 2.1 against its own control bar (**), P480L about 1.16 (*), G544V about 1.24 (*).
The note's own next sentence ("Both were also raised in yeast") conflicts with the printed wording.
Replacement: "In HEK293T, G544D protein with sorbitol was about 1.8 fold in Supp Fig 12a (marked, n=3) but about 1.0 fold, unmarked, in 12b, and 400 mM of either gave no rise in 12a, so no sorbitol effect on G544D is established in HEK293T; sorbitol did raise R406H (about 2.0) and G544V (about 1.6) in 12b, G544D in yeast (about 2.7, 12c) and several mutants in neurons (Fig 6a), so the osmolyte arm does not rest on trehalose alone."

A01-04. INCOMPLETE.
Opened: Supp Fig 12a, 12b, main Figs 6a, 6b, 6d, full text, reviewer file (MOESM2).
What holds: the doubling of the soluble fraction (Fig 6b, 1.7 to 2.4 fold in the four low-protein variants) and the function clause (see A01-11).
What is left out:
- Butyrate. Sodium butyrate 5 mM was tested only in HEK293T, on G544D and WT, n=3 (Supp Fig 12a). G544D was about 103, unmarked, so "did not" holds there. WT was about 195, unmarked with wide spread. It was not tested in neurons or on the other four mutants.
- 4-PBA in neurons (Fig 6a) is marked for only 3 of 5 mutants (P335L, R406H, G544D). P480L (1.03) and G544V (1.33) are unmarked. In HEK293T (12b) all five are marked, about 1.5 to 2.1.
- Sorbitol on G544D in HEK293T was unmarked in 12b (see A01-03).
Replacement: "In the soluble cytosolic client (Guiberson 2018), 4-PBA raised all five mutants in HEK293T (Supp Fig 12b, about 1.5 to 2.1 fold) and three of five in neurons (Fig 6a); trehalose and, variant-dependently, sorbitol raised mutants in HEK293T, neurons and yeast; sodium butyrate 5 mM, tested only on G544D and WT in HEK293T (n=3), did not raise G544D (about 1.0 fold); the soluble fraction about doubled and uptake reached or exceeded untreated WT in three of four low-protein variants."

A01-05. CORRECT.
Opened: figure images (Fig 3a, Fig 6a, pixel), full text.
Evidence: Fig 3a (neurons, n=3): R406H 7, P480L 3.5, G544D 5, G544V 9 percent of WT; P335L 65. Fig 6a, 4-PBA fold: 1.03, 1.30, 1.33, 1.64.
Note for the reviewer: the G544V value by pixel is 9, not 8, but the paper says "below 10%". The P335L fold is 1.39 against 100 or 1.84 against its own control bar, and it is the excluded fifth variant. Authors' reply file says "10 to 60 percent" total-protein increase.

A01-06. CORRECT. The WWOX-premise clause is not assessable here.
Opened: full text, supplement text, figure images (Fig 6a).
Evidence:
- WT raised: Fig 6a WT 1.27 (*), Supp Fig 12 WT 1.8 to 2.05.
- Four low mutants 1.03 to 1.64, with two of the four unmarked.
- Negatives, searched 2026-11-26 in the article XML and the supplement PDF text. Query "MG132|lactacystin|bortezomib|proteasom|bafilomycin|chloroquine (treatment)|leupeptin|NH4Cl": no route-inhibitor arm. Query "mRNA|qPCR": mRNA measured only untreated (Supp Fig 4a-c, WT vs mutant). No enzyme client.

A01-07. CORRECT.
Opened: figure images (Fig 3a, 3b, 6a, 6b), full text legends.
Evidence: normalisers differ (Fig 6a PSD-93, Fig 6b percent of total, Fig 3a SypI, Fig 3b alpha-tubulin). P480L 4-PBA fold 1.03, unmarked. My pixel error is ±1.5 to 3 percent of axis, so the stated ±10 percent is conservative.

A01-08. ADD.
Opened: Supp Fig 12a and 12b (rendered), main Fig 6a, full text.
Evidence: G544D 4-PBA 5 mM is about 183 (*) in 12a (n=3), so 1.8 holds. The same experiment type in 12b gives about 155 (**), n=3, i.e. 1.55 fold. Neurons (Fig 6a, n=5, mouse) give 1.64 (**).
Addition: "...about 1.8 fold in Supp Fig 12a and about 1.55 fold in Supp Fig 12b (HEK293T, n=3 each); 1.64 fold in neurons (Fig 6a)."

A01-09. ADD.
Opened: Fig 3a, 3b, 3f, Supp Fig 4f, 4i, 4j (rendered), repository table as pointer.
Recomputed:
- Deficit: 100 over 4 to 8 percent gives 12 to 25 fold. By pixel (3.5 to 9 percent, ±2 points) it is 11 to 29.
- Fig 3b (neurons, CHX, n=3): WT about 44 percent left at 24 h, mutant lines end at about 7 to 26. First-order rate ratio is about 1.7 to 3.3, so 1.5 to 3 holds. Which line belongs to which variant could not be separated.
Addition: other turnover assays give different ratios.
- Fig 3f (HEK293T, Dendra2): red signal at 24 h about 50 to 80 percent of WT, i.e. 1.2 to 2 fold.
- Supp Fig 4f (HEK293T, CHX): WT about 85 percent left at 24 h, mutants about 35 to 57, rate ratio about 3.5 to 6.
- Supp Fig 4j (neurons, Dendra2): about 60 to 83 percent of WT.
In all of them the explained fold is far below 12 to 25.

A01-10. CORRECT, on repository tables only.
Opened: repository tables proteostasis_pba_a01.tsv and hdac_enzyme_potency_chembl_20261029.tsv only. The ChEMBL raw answers are not held. Search 2026-11-26 over files/ (Obeid files excluded): grep for CHEMBL1671826, CHEMBL5136998, CHEMBL5096206, CHEMBL1680132, CHEMBL5138330, CHEMBL5138331, CHEMBL5098748 gave no hits.
Evidence from the table rows:
- Document CHEMBL1671826, PBA over butyric acid IC50: HDAC1 64/16 = 4.0, HDAC2 65/12 = 5.4, HDAC3 260/9 = 28.9, HDAC8 93/15 = 6.2, so 4 to 29. Butyrate on HDAC6 is above 2 mM (PBA 240 µM).
- Document CHEMBL5096206 (sodium butyrate): 16, 12, 9, 15 µM, the same low values.
- Document CHEMBL5136998: sodium PBA 162 µM on HDAC1 against butyric acid 300 µM.
- Not verifiable here: that document CHEMBL5096206 "lists no phenylbutyrate". The pull held only shows no PBA row from it.
- Fourth document, HeLa extract (CHEMBL1155249), not named in the sentence: Ki 2.8 µM PBA, 6.3 µM sodium PBA, 136 µM butyric acid.

A01-11. CORRECT.
Opened: figure image (Fig 6d, pixel).
Evidence: Fig 6d (n=4), 4-PBA: P480L about 82, G544D 74, G544V 74 against untreated WT about 57; R406H 44, below WT.

A01-13. CORRECT.
Opened: full text (PMC XML r2), Table 1.
Evidence, week 12 from Table 1 means: sham 1341.01 µM (n=2), treated 749.41 µM, WT 250.27 µM. Fall is 44.1 percent; 749/250 = 2.99.
Note: row means differ from the printed means. Treated rows 672.1, 758.8, 866.9 average 765.9 (fall 42.9 percent); WT rows average 257.1 (ratio 2.98). The text prints sham 1341.59 against the table's 1341.01. The authors say "approximately 50%".

A01-14. CORRECT.
Opened: figure images (Fig 3a, 6d, pixel).
Evidence: P335L is 65 percent of WT in Fig 3a. Fig 6d control is about 47 against WT 57, unmarked, while the other four variants show ## or ###.

A01-15. ADD.
Opened: figure images (Fig 6a, 6b, pixel).
Recomputed, four low-protein variants: soluble fraction ratio 1.7 to 2.4. Pool fold = total fold × soluble ratio: R406H 1.30 × 1.77 = 2.3; P480L 1.03 × 2.4 = 2.5; G544D 1.64 × 2.26 = 3.7; G544V 1.33 × 1.7 = 2.3. The 2 to 4 range holds.
Addition: the fifth variant does not double. P335L soluble fraction is 75 to 77 (1.03), and its pool is about 1.4 to 1.5. If the sentence is read as covering all five variants, it is INCOMPLETE.
Added wording: "(four low-protein variants; P335L soluble fraction unchanged, pool about 1.5 fold)".

A01-16. CORRECT.
Opened: Supp Fig 12a and 12b (rendered), Fig 6a.
Evidence: WT 4-PBA about 178 (*) in 12a (n=3), about 205 (***) in 12b; neurons WT 1.27 (*).

---

FILES OPENED (none under Obeid or 42422765):
- PREREG_ADV287EXT_SCI_20261126.md, section "One matching rule"
- PACKET_A01.md, both in the named folder
- drug_repurposing/cards/A01_pba_class.packet.json (fields drug_assertions[2,5,7,8,9], p4_card/evidence_for_and_against, p4_card/pharmacology)
- framework/protocols/delegation_budget.md (sections 2 and 7)
- files/fulltext/PMID30266908_Guiberson2018_PMC6162227.xml
- files/fulltext/PMID40485335_Shah2025_PMC12146831.xml
- files/fulltext/PMID41274966_Tubastatin2025_PMC_r2.xml
- files/figures/PMID30266908/ Fig3, Fig6 JPGs, SuppFig12_p19.png, SuppFig4_p7.png
- files/figures/PMID40485335/ g002, g004, g006 JPGs
- files/supplement/PMID30266908/41467_2018_6507_MOESM1_ESM.pdf (Supp Figs 4 and 12 pages rendered, legends)
- files/supplement/PMID30266908/41467_2018_6507_MOESM2_ESM.pdf (reviewer file)
- Pointers only: missense_recovery_it5_p8_20261029/munc18_quantity_function_arithmetic_20261029.tsv, munc18_cytosolic_precedent_panel_readings_20261029.tsv, hdac_enzyme_potency_chembl_20261029.tsv, README.md (grep lines only); pharmacology_it5_20261029/proteostasis_pba_a01.tsv

Scripts and renders are in /home/desktop/.claude/jobs/c6d4dd83/tmp/a01_first/. Nothing was edited in the repository or files/. No web requests were made.
