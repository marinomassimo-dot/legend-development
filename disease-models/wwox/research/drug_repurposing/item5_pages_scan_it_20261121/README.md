# Item 5 of the operator decision page: the other two "blocked" pages, scanned with three identifiers (IT, 2026-11-21, ADV-149 step 2)

Question (ADV): are IT49-Q11 (VU6080824 SI) and IT55-Q02 part 2 (2015 OPC screen supplement) in fact held or readable by the same route as IT45-Q07, before they stay on the operator's list? Public, disease-level; not medical advice; no dose, no ranking change.

## Scan with PMID, PMC id and held bytes
| Page | PMID | PMC id | Ledger and repo before this session | Bucket (`pmc-oa-opendata`) holds |
|---|---|---|---|---|
| IT49-Q11 | 40959251 | PMC12434521 | receipts FTR-20261112-40959251-71 and FTR-20261115-40959251-01 (main text; SI "not read", proof-of-work on the PMC SI request) | `ml5c00297_si_001.pdf` (776,129 bytes, 25 pages) |
| IT55-Q02 part 2 | 25896324 | PMC4528969 | receipt FTR-20261105-25896324-06 (Results, Discussion, in-vitro and slice methods; figures and extended data not read) | supplement docx, Table S1 pdf, Supplementary Tables 2 and 3 (xlsx), all 14 figure images |

Both were closable by the same lawful route: one plain request per file, HTTP 200, no challenge page. Hashes and quotation checks: `verify_held_bytes.py` (files not stored here).

## IT49-Q11 result (VU6080824 = compound 5s, Kir2.1 inhibitor; decision: can it be a probe)
- Prediction fixed before the fetch: the SI contains no counter-screen of 5s against hERG, Kir6.2, Kir7.1, Kir2.4 or K2P. HELD (no such data; the search terms hit only the reference list, i.e. absence by two routes in the held set: main text 2026-11-15 and SI 2026-11-21).
- SI Table S2: Kir2.1 thallium flux IC50 5.9 uM (101 percent inhibition); manual patch clamp IC50 0.35 uM (100); Kir2.1/Kir2.2 selectivity 2.1-fold and Kir2.1/Kir2.3 2.5-fold (manual patch clamp), so the main text's "1 to 3-fold" holds for 5s itself and not only for its deuterated analogs. Manual patch clamp conditions (SI): human Kir2.1 in T-REx HEK293, whole cell, room temperature, pH 7.35 both sides, normalised to 2 mM Ba2+ (the main text said pH 7.4: a small difference to note). Kir1.1 and Kir4.1 thallium flux are described only as "previously described"; the SI carries no table for them. INFERENCE: thallium flux is about 17 times weaker than manual patch clamp for 5s (5.9 against 0.35), the same order as for the other compounds of the table (13 to 26 times).
- Decision: unchanged and now firmer. VU6080824 is a family-level Kir2 inhibitor (measured within-family selectivity 2 to 3-fold), rodent PK from the same SI (Kp 1.81), not an isoform probe; the counter-screen that the 2026-11-15 note could not read is not in the SI either. For INV-18's Kir2 tool arm: use at family level only, with the SI conditions above.

## IT55-Q02 part 2 result (does the 2015 screen supplement or paper give a differentiation value for clobetasol, ketoconazole, miconazole, liothyronine)
- The supplement does NOT: the docx index lists Table S1 (blood-brain-barrier ratios and western scans), Supplementary Table 2 (kinase profiling, clobetasol and miconazole only at 1000 nM) and Supplementary Table 3 (phosphoproteomics, clobetasol and miconazole against DMSO at 1 and 5 hours): none is a differentiation readout.
- BUT the paper's **Extended Data Fig. 2a** (cited in the main text for the slice ranking; image `nihms665856f6.jpg`, PMC4528969.1; identified as that figure by its content, since the main text cites Extended Data Fig. 2a for the ranking of eleven drugs in slices and the table's High group is four drugs at about 150 percent; the caption itself was not read) is a table of printed numbers that the 2026-11-15 reading (text only) did not see. Printed values, read from the image and confirmed by an independent blind reader (sonnet, effort high read back; `blind_reading/`; all values agree, confidence "certain"):

| Compound | Single-dose rank (in vitro) | EC50 uM (in vitro) | 50 percent tox uM | Primary tier | Brain slice percent MBP of control (ex vivo) | Slice group |
|---|---|---|---|---|---|---|
| clobetasol | 7 | 0.4 | >6.7 | A | 169 | High |
| miconazole | 5 | 0.5 | >6.7 | A | 148 | High |
| ketoconazole | 4 | 0.5 | 2.4 | C | 117 | Medium |
| benztropine (for reference) | 22 | 0.6 | 4.2 | B | 96 | Low |
| liothyronine | not a row; "thyroid hormone" is only the label of one image column of panel b (the paper's positive control), no number | | | | | |
| mevastatin, quetiapine, ipratropium | not in the figure | | | | | |
Ketoconazole is named once in the main text, in the Methods list of drugs tested in cerebellar slice culture (1 uM). The paper's own "high" group is four drugs at about 150 percent or more.
- **This overturns my 2026-11-15 reading** (`it55_q02_signs_it55_20261115/README.md`: clobetasol, ketoconazole, miconazole "not in the paper's text; no readout"): that was true of the text and of the xlsx tables, not of the figure. Against the frozen case-1 signs (favourable for all three): clobetasol AGREES (strong), miconazole AGREES (strong), ketoconazole AGREES weakly (117 percent of control, "Medium", narrow window: toxic at 2.4 uM). Liothyronine and mevastatin stay without a readout. Slice values are one assay (ex vivo cerebellar slice, MBP-positive aligned fibres, blinded); the in-vitro EC50 is the primary OPC screen. A dated line is added to the 2026-11-15 README and to the map row; the old text is kept.
- Decision (IT55-Q02): the case-1 comparison CAN cite a printed differentiation readout for clobetasol, miconazole and ketoconazole in addition to the six compounds of the other paper's Table 1; it still cannot for liothyronine or mevastatin. Public MEA screens were not searched (unchanged).

## Receipts
FTR-20261121-40959251-01 (supplementary information read: Tables S1 and S2, thallium-flux and manual-patch-clamp conditions, PK; synthetic chemistry characterisation not read) and FTR-20261121-25896324-01 (supplement files and Extended Data Fig. 2a; main text re-checked for the passages only, extended data figures other than 2a not viewed): `receipts/`.
