# Independent verification of package HYPCURRENT (scientist-b, landed ec7be923)

Verifier: scientist-d role, task `SD-IT2-VERIFY-HYPCURRENT-20261027`. EXPLORATORY audit; read-only toward every canonical file. Nothing here is medical advice.

## Reading depth (stated)
- PMID 35328751 (Baryla 2022): derived PMC XML text read at the sentences on enzyme activity, Figure 5 legend, WWOX KO/OE methods (a sentence-level read, not a full re-read; figure bars not inspected).
- PMID 25012504 (Abu-Remaileh 2014): **dossier and manifest only** (receipt `FTR-20260814-25012504-01`). The PMC full text was not retrievable here (the local XML copies are 2.6 kB stubs; Europe PMC full-text endpoint returned nothing; not retried). So digoxin n and the PDK1 tissue list rest on the dossier plus `DL-MECH-095`, not on the paper.
- PMID 30361190 (Shaukat 2018) and PMID 24456803 (Abdel-Salam 2014): source text layers searched directly (quoted below). PMID 38161429 (Battaglia 2023) and Davids 2019: dossier/ledger only.
- UniProt P08559 (ODPA_HUMAN), REST JSON, read in full for modified residues.
- Dry run of `apply_ledger_edits.py` against the main ledger.

## Verdicts
| # | Claim | Verdict | Basis |
|---|---|---|---|
| 1a | "Seahorse is the only falsifier / normal Seahorse makes HYP-01 fall" was an overstatement and is correctly withdrawn | SUPPORTED | Seahorse OCR/ECAR reads whole-cell respiration and acidification; it is not a PDH measure (general method knowledge, ESPANSIONE). The repository's own `DL-MECH-095` ("Impatto") and the 25012504 dossier (section on assays) already name phospho-PDH, PDH phosphorylation, PDK activity and labelled flux; HYP-01 ignored them. A normal result in non-neural cells being non-significance is consistent with the Baryla Results text (no n stated). |
| 1b | Ser293 of PDHA1 | SUPPORTED | UniProt P08559 feature "Modified residue 293, Phosphoserine; by PDK1, PDK2, PDK3 and PDK4" (evidence PubMed 11486000, 17474719). Numbering is UniProt precursor numbering (transit peptide 1-?); sites 232 and 300 are the other PDK sites. The package's "numbering to be checked" is now closed: say "Ser293 (UniProt P08559 numbering)". Minor UNDERSHOOT: the package does not mention Ser232/Ser300, which also gate PDH. |
| 2 | PDK1 is a transcript; PDH step inferred | SUPPORTED | Dossier 25012504: "PDH phosphorylation/activity and carbon flux through PDH were not measured." Baryla: PDK measured as RT-qPCR; the enzyme-activity paragraph says "pyruvate dehydrogenase kinase (PDK) ... not changed" but Fig 5b is PDH (the mislabel the ledger already records). |
| 2b | PDH-activity datum is skin fibroblast (non-neural); PDK1 transcript is mouse MEF | SUPPORTED with a precision gap | 1BR.3.N is a skin-fibroblast line; KO is CRISPR/Cas9, WWOX mRNA only ~3x lower (partial); no n or replicate count stated; "WWOX silencing exhibited no significant effect" in hypoxia-hyperglycaemia. The PDK1 rise in 25012504 is in "KO cells and tissues" (dossier); the tissues are not named in what I read, so "MEF only" in the CURRENT READING is slightly narrower than the paper (UNVERIFIABLE which tissues; none known neural). |
| 3 | Digoxin qualifier | SUPPORTED | Dossier + `DL-MECH-095`: glucose experiment n=3/group at 40 min, one acute dose, printed "100 mg/kg" in HTML and PDF; supplementary transcript panel n=2, no statistics, GLUT1 and PHD3 not PDK1. The package omits one further `DL-MECH-095` limit (WT glycaemia visibly falls ~105 to ~75 after digoxin, no test), a minor UNDERSHOOT. |
| 4 | 12/15 CURRENT vs 13/15 HISTORICAL | SUPPORTED | Ledger HYP-20260709-01 lines: "Ranking (aggiornato 2026-09-21)" = 3+1+3+3+2 = 12 (evidence 2/3 to 1/3), justified in the 09-21 bullet by the first reading of PMID 35328751 (PDH activity unchanged, PDK transcript only). The "precedente 2026-07-10c" line = 3+2+3+3+2 = 13 (earlier, evidence 2/3). Later and justified; the 10-26 bullets state "no ranking line is changed". Arithmetic of both lines checks. |
| 5 | Dry run | SUPPORTED | `apply_ledger_edits.py` on the main ledger: "all edits apply (dry run)" (19 pairs). Direct edits in the map and prediction note read against the diff d85d6a55..ec7be923: each wording change matches a withdrawn overstatement; none strengthens a claim. |
| 6 | No over-correction | SUPPORTED | No score/status changed; historical text kept in place; 5 of 19 edits are pointers. The qualifier "digoxin is target validation, not a candidate" restates `DL-MECH-095`. |

## The disputed count (DL-BIO-009 "four independent normal" versus DL-BIO-008/N-06 "one complete screen plus one MRS case")
Both are wrong, in opposite directions. Resolved from the sources:
- **Abdel-Salam 2014 (PMID 24456803):** one genotyped child (II:4); "Normal results were found in metabolic screening including liver and renal function tests, ... ammonia, serum lactate, ... urine and serum amino and organic acids, and very long chain fatty acids." Blood/urine chemistry only. The strings "biops" and "muscle" do not occur in the article; "mitochond" only in Discussion and reference titles. So `DL-BIO-009` "biopsia muscolare inclusa" and the HYP-01 07-10c phrase "screening metabolico **e mitocondriale** completo" are NOT_IN_SOURCE (a real error, not left uncorrected by the package: it is neither noticed nor edited).
- **Shaukat 2018 (PMID 30361190, PAPER 045):** both children. Child 1: "The following investigations were normal: lactate, ammonia, acylcarnitine, uric acid, homocysteine, plasma amino acids, urine organic acids, and transferrin isoforms." Child 2: "echocardiogram, lactate, ammonia, acylcarnitine profile, uric acid, homocysteine, plasma amino acids, urine organic acid, and urine sulfocystine." This is a second primary human source with normal blood/urine screens (2 patients). `DL-BIO-008` and `N-06` ("exactly one complete human screen") omit it: N-06's count of ONE is an undercount (UNDERSHOOT); the scientist-b/c reasoning "the other three sources are identified nowhere" is wrong, they ARE identified in `DL-BIO-009` itself.
- **Battaglia 2023 (PMID 38161429):** a narrative mini-review; its single "normal MRS" is a secondary report of one patient from Johannsen (primary not read here); it is not independent of that primary and adds no new patient.
- **Davids 2019:** MRS cerebral lactate "extremely low" (opposite direction, HSPG2 confounder); the DL-BIO-009 tally counts it among "four ... normal" though its own text calls it the outlier.

Best supportable statement: **two primary human sources (3 patients: 1 + 2) report normal blood/urine metabolic screens; one secondary report of a normal MRS (one patient, primary unread); one primary MRS case with the opposite direction.** Not "four independent normal", not "one". None of these is a mitochondrial or muscle study, and none is neural tissue chemistry beyond the two MRS reports. Package wording ("reported normal where checked; count disputed") is safe; it can now be replaced with the above.

## Residuals for the integrator (errors, not uncertainty)
1. `DL-BIO-009` still says four sources, "biopsia muscolare inclusa", "quattro volte", and "l'unico test che puo falsificare ... Seahorse" (acknowledged by the package).
2. HYP-01 07-10c bullet still says "screening metabolico e mitocondriale completo" for Abdel-Salam (not in source).
3. `N-06` "exactly one complete human screen" should read two (add PAPER 045).
4. The sentence "Se il profilo bioenergetico e normale, il razionale WWOX-specifico cade" in the "Esperimento minimo" bullet survives next to the new bracket (bracket withdraws "unico" but not "cade"; edit 7 covers 'falls' only in the 07-10c bullet).
5. Enunciato falsificabile and Note L9 still name Seahorse as the falsifying test (a prediction, tolerable, but not aligned).

Uncertainty (not error): which tissues carry the PDK1 rise in 25012504; whether the Baryla lysate preserves PDH phosphorylation (assay kit detail not read).
