# src_04 — E02 p4_card.pharmacology: "one comparator document with LDH5 and LDH1 inhibition of 7 percent at 2 millimolar and no value at 0.5 millimolar;"

Card: E02_ldh_inhibition, /p4_card/pharmacology (stiripentol paragraph: "IT8 P3 2026-10-29 (ChEMBL molecule-first on the racemate: 28 rows under the type filter ... 88 unfiltered, none a fitted LDH potency; one comparator document with LDH5 and LDH1 inhibition of 7 percent at 2 millimolar and no value at 0.5 millimolar; ..."). Pointer: pharmacological_qualification_it8_p3_20261029 (collected.json.gz = the raw ChEMBL pull, Q03; measures_detail.tsv; README case Q03). Species: human enzymes (cell-free, UV-vis, pyruvate substrate); compound = stiripentol racemate CHEMBL1983350. Reading depth: table (raw ChEMBL rows from collected.json.gz, every row of Q03 'rows' + 'rows_other' scanned, 86 rows).

## Every ChEMBL row in the held pull that concerns LDH (Q03, racemate CHEMBL1983350)
| ChEMBL assay | document | description (verbatim) | type | relation | value | unit |
|---|---|---|---|---|---|---|
| CHEMBL4313737 | CHEMBL4311969 | Inhibition of human LDH5 at 2 mM using sodium pyruvate as substrate by UV-VIS spectrophotometry method relative to control | Inhibition | = | 7.0 | % |
| CHEMBL4313693 | CHEMBL4311969 | Inhibition of human LDH1 at 2 mM, same method | Inhibition | = | 7.0 | % |
| CHEMBL4313692 | CHEMBL4311969 | Inhibition of human LDH5 at 0.5 mM, same method | Inhibition | (none) | (none) | % |
| CHEMBL4313691 | CHEMBL4311969 | Inhibition of human LDH1 at 0.5 mM, same method | Inhibition | (none) | (none) | % |
| CHEMBL5123610 / 5123611 | CHEMBL5120856 | GO/LDHA inhibition, Grhpr-knockdown PH2 mouse hepatocyte, relative oxalate output at 10 uM, 24 / 48 h | FC | = | 0.27 / 0.33 | fold change (mouse, cell level) |
| CHEMBL5123612 / 5123613 | CHEMBL5120856 | same, Hoga1-knockdown PH3 mouse hepatocyte, 24 / 48 h | FC | = | 0.70 / 0.49 | fold change |
Human LDHA target-first pull (CHEMBL4835, IC50/Ki/Kd, 1000 rows): no row for stiripentol among the molecule names printed (named rows are oxamate, gossypol, carboxynaphthol, adenosine phosphate ...); no fitted LDH potency for stiripentol anywhere. Other held LDH datum not in this pull: README Q03 (b) recombinant human LDHA, about 10 percent at 500 micromolar (PMID 39769031 abstract; 9.9 percent in the earlier partial full-text receipt FTR-20261026-39769031-01; not re-read).

## Recomputation
measures_detail.tsv Q03 line: standard_type Inhibition, n_rows 4, n_documents 1, min = median = max = 7 (computed over the two rows that carry a value). Count: 4 rows in one document, two with 7.0 percent at 2 mM (LDH5 and LDH1), two without any number at 0.5 mM. The sentence matches the whole LDH-related row set of that document: same value on both isozymes, same single document, no value at 0.5 mM. "Comparator document" = the one document in the pull that carries LDH inhibition at all (the label "comparator" is the card's; the document is not stiripentol-specific). No printed arithmetic.
