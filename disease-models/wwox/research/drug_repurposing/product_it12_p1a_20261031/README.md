# IT12 P1-main: which WWOX models make protein, and where a product-dependent lever could be tested (scientist-a, 2026-10-31)

Non-canonical research material. Exploratory, not medical advice; no wet-lab, efficacy or safety claim. Reference genotype class only. No e-mail or personal datum sent; key-less endpoints; no spend. Nothing here edits a card, need, ranking, registry, current file or the ledger.

## Read before forming questions (not blind)
IT10 P2.3 README and search_log; IT11 P2.4 README, design, step table, search log; IT9 Q1 and seeds S001-S016 (S004 "very low, unread" was my starting point); N12; heading/need level of cards A01-A05, B01, B02, C02, C03 (JSON, abstention fields only); IT5 P8 README; I did not re-read wwox_function_reference_it6 in depth.

## 1. Decision
* **No neural WWOX model has a confirmed variant protein.** Neural WWOX-present: WT hESC/iPSC NSCs and organoids, AAV add-back (WT sequence). Variant-bearing: only the SCAR12 G372R line shows a faint band (0.1-0.3 of an unrelated WT; one membrane; on a second blot (EV6F) SCAR12, WOREE and the two KO lanes all show similar faint bands) so it is not shown above the assay floor. WOREE lines (c.517-2A>G; c.864G>A/deletion): no visible band in wk16 organoids; their iPSC blot cannot separate them from heterozygote parents (1.1-1.5x).
* **Correction of the carried datum S004:** "SCAR12 lines (two individuals)" are two siblings with ONE allele (p.Gly372Arg), a C-terminal missense, not the reference class (Q230P) and not "SCAR12 missense lines" in general. WCH (p.Gly137Val + c.517-2A>G) is WOREE-class, iPSC only, faint bands.
* **Best substrates for a product-dependent lever:** (i) G372R neural line, UNKNOWN until gate G0; (ii) WWOX-present neural cells (WT NSCs, controllable AAV level) for the mechanism question. Q230P fibroblast: UNKNOWN/not applicable until a band is shown.
* **P47T:** protein present at control-like level (fibroblasts, cerebellum): not a deficit model. **lde/lde rat:** trace frameshift protein with an aa 32-110 antibody (earlier antibody: none): "null" depends on the antibody; paper contradicts itself on mobility. **Hypomorph gt/gt:** blot-undetectable yet viable (abstract). All of this reinforces that a missing band is not zero protein.
* **N12:** priority not raised; scope narrowed (no confirmed variant substrate). See `priority_triggers_it12_p1a.md`. No card proposed.

## 2. Files
`models_wwox_protein_it12_p1a.tsv` (17 models) · `evidence_locators_it12_p1a.tsv` · `design_it12_p1a.md` · `priority_triggers_it12_p1a.md` · `text_amendments_it12_p1a.md` · `search_log_it12_p1a.tsv`

## 3. Key sources and depth
PMID 42397075 Brain 2026: accepted-manuscript text read; immunoblots are in its Supplementary Fig. 1J-N which I could NOT reach; I used the bioRxiv v2 (Sep 2025, PPR960425) EV1 figures from the corpus as the analogue (figures viewed). Version differences UNVERIFIED. WWOX antibody for 2026 not stated; 2021 same-group in-house rabbit polyclonal (Table EV4). PMC8350905 supplement fetched. 29808465, 24369382, 36828035, 31340538, 41124647, 42422765, 33914858 read as in the table; 17823927 abstract only; 31543760 sentence only.

## 4. Self-audit (re-read at source)
1. EV1N values 0.1/0.1/0.3 and EV6F floor: re-cropped and viewed at 300-450 dpi; values confirmed; note WT lane of EV1M looks saturated and AAV ratios (0.9, 1.4) exceed the visual band, so ratios are not linear.
2. "SCAR12 = one allele": EV1E crop viewed: WPM S and WPM D both c.1114G>C homozygous; 2021 text names G372R. Confirmed.
3. lde/lde and Q230P: Tochigi sentences re-read verbatim (inconsistency confirmed); Johannsen Fig. 3c viewed (patient actin lane heavier, no WWOX-null-fibroblast control lane; PaTu WT band faint).
Not self-audited: EV1G numbers' reference lane (inferred LM-iPS=1, UNVERIFIED).

## 5. UNVERIFIED
Brain 2026 supplement content; 2026 WWOX antibody and epitope; sc-20528 epitope (probably N-terminal, same as Mallaret's anti-aa 1-19: not confirmed); whether G372R band exceeds KO floor; WWOX RNA in organoids (not reported in text read); WCH organoid use; Tnk2/ACK1 expression in these neural cells; Q230P-class protein fate; Fig. S3B/S5 of Obeid not opened; Fig. 2 of Tochigi not opened; hNPC shWWOX knockdown level; 0.9 Mbp vs 93 kb deletion discrepancy in EV1.

## 6. Disclosures
Not blind. Searches screened by title; counts in log. No browser-identity tricks; Brain supplement blocked: reopening condition = library/operator access or PMC release. Preprint full-text API returned 500, not retried. Receipts not written. Branch task/it12-p1a.

## 7. For the batch path
See `text_amendments_it12_p1a.md` (N12, S004/context matrix, Q1, R9, receipts).
