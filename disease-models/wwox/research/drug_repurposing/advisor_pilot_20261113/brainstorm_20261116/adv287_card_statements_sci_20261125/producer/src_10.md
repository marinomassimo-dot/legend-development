# src_10 — P11 DR-P11-002 measured_result_note: "The block grows steeply with hyperpolarisation: the half-inhibitory external Mg2+ concentration is about threefold smaller at -70 than at -50 mV, and about 2.5-fold smaller at -90 than at -70 mV."

Card: P11_magnesium_nmdar_gate, /drug_assertions/1/measured_result_note (DR-P11-002; J Physiol 2014, PMID 24614743, PMC4027860; reading_depth queried_not_full_read). Species/preparation: rat (P7), substantia nigra pars compacta dopaminergic neurones, whole-cell NMDA-evoked current; mixed GluN2B/GluN2D population (card context).
Pointer: "quotation L12 of supplement_diet_it6_p11_20261029/locators.tsv"; "local copy sha256 1ecd1c7d8cdc744a7354557fbf71b218ef330da9eae77636e54a5c9c78dce28b".
Access checked: (1) the quotation table drug_repurposing/supplement_diet_it6_p11_20261029/locators.tsv (all 26 rows scanned; L12 is the only row for this paper); (2) the staged receipt receipt_staging/scientist-b/FTR-20261029-24614743-01.json (coverage: abstract read, every other section not_read); (3) a SHA-256 search over every file under /home/desktop/legend-development/files (find files -type f -size -4M | sha256sum | grep 1ecd1c7d8cdc), run 2026-11-25: no match; a name and grep search of files/ for "PMC4027860" and "24614743" returned only two unrelated XMLs (PMC6080888 and PMC6858497). So the article bytes are not held; reading depth here = the verbatim abstract quotation in locators.tsv (table).

## The whole held answer (verbatim, locators.tsv L12, section Abstract)
"external Mg2+ significantly inhibits the whole cell NMDA-evoked current in a voltage-dependent manner with IC50 values of 20.9 uM, 53.3 uM and 173 uM at -90 mV, -70 mV and -50 mV, respectively"
| holding potential | IC50 of external Mg2+ (uM) | system |
|---|---|---|
| -90 mV | 20.9 | rat P7 SNc dopaminergic neurone, whole cell |
| -70 mV | 53.3 | same |
| -50 mV | 173 | same |
No other voltage and no per-subunit IC50 is quoted in the held material (the rest of the article is not held).

## Recomputation
173 / 53.3 = 3.246 (the sentence: "about threefold smaller at -70 than at -50 mV": IC50 at -50 is 3.2 times that at -70, so the statement is a round-down of 3.25); 53.3 / 20.9 = 2.550 ("about 2.5-fold": matches). Direction: IC50 falls with hyperpolarisation (173, 53.3, 20.9): "grows steeply with hyperpolarisation": matches. Cumulative -50 to -90: 173/20.9 = 8.3-fold (not printed in the sentence). Limit: only the abstract's three IC50s are held; the paper's own panels and the subunit composition are not.
