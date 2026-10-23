# Locator audit, module rows of three manifests (blind, 2026-10-23)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and ledger. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` and judged against the native artefacts under `files/`. Nothing was repaired.

## Scope and sampling

- Zero-auditor `contradicts_locator` entries: none exist. Every entry that carries `contradicts_locator` in the three manifests already records one auditor (30619736 entry 33; 36779245 entry 38; 42422765 entries 38, 40, 41, 45). None was re-judged here.
- Sample of the other entries: 28 of 126 (22 percent), chosen by hand, weighted toward numerals, negations, quantifiers and text-versus-figure relations (figure and supplement-figure rows first, then numeric body rows). Not random.

## Image reads

Every image read returned a real image (no "media removed"). Figures were ranked with `paper_packet.py rank`. 42422765 panels were read from the embedded 2,906-px rasters of mmc2.pdf, the vector Figure 7 from a 130 dpi page render, and supplement panels from page renders of mmc1.pdf (S8 at 400 dpi). 30619736 figures were read from the native embedded JPEGs; Figure 2 and Figure 5B names were cross-checked against Data_Sheet_2 (216 prey; DBT absent). 36779245 figures were native 709-px JPEGs. No triple is UNVERIFIABLE.

## Counts

| PMID | Entries judged | SUPPORTED | Adverse | UNVERIFIABLE |
|---|---|---|---|---|
| 30619736 | 5, 9, 14, 16, 20, 22, 31, 34, 42 (4 figure, 5 text) | 9 | 0 | 0 |
| 36779245 | 15, 17, 18, 20, 22, 27, 30, 37 (2 figure, 6 text/table) | 8 | 0 | 0 |
| 42422765 | 0, 3, 6, 10, 12, 14, 28, 32, 33, 37, 42 (9 figure, 2 text) | 9 | 2 | 0 |
| **All** | **28** | **26** | **2** | **0** |

Adverse rate: 2 of 28 judged triples (7.1 percent). Mode: hand-weighted 22 percent sample of the non-`contradicts_locator` entries of the three manifests, plus the empty zero-auditor set; adverse = OVERSHOOT or UNDERSHOOT; UNVERIFIABLE excluded from the denominator (none). Figure triples alone: 2 of 15.

## Adverse triples

| Manifest | Entry | Verdict | Reason |
|---|---|---|---|
| 42422765 | 14 | OVERSHOOT | Figure 2B (mmc2 p.4 raster) shows KO+AAV-hWWOX 8E10 (n=5, pink) at 100 percent with a marker at about day 27, and KO+AAV-WWOX-WPRE 4E10 (n=3, grey) at 100 percent to about day 31. The quote says 8E10 was "dead ~17 days" and that the WPRE 4E10 arm was "~33% at ~25 days"; the 33 percent step at about day 25 is the yellow KO+AAV-hWWOX 4E10 arm. The proposition "at 4E10 and 8E10 no treated arm survives" is therefore not what the panel shows, and the running text says 8E10 without WPRE rescued lethality. |
| 42422765 | 10 | OVERSHOOT (quote-level) | Supplementary S8B, read at 400 dpi: P1 (n=6) sits at 100 percent to day 300 and only P5 (n=7) plateaus at 75 percent from about day 35. The quote says "P1 and P5 plateau near 75% to 300 days". The proposition's own wording (survival to 300 days, only P1 and P5 on the 300-day plot, P3 an n=3 arm that falls to about 67 percent) survives; the figure reading inside the quote does not. |

## Notes on triples judged SUPPORTED

- 30619736 entry 5: 795 and 594 proteins, 7,589 peptides and the 383 shared proteins occur in the same paragraph. Entry 16: text says only SEC23IP and SCAMP3 were pulled down; VOPP1 is not tested by pull-down. Entry 42: quote verbatim. Entry 20: the quote is verbatim, and recomputation from Data_Sheet_2 reproduces 67 vs 149 prey, means 0.1875 and 0.1287, Student t = 3.36, Welch t = 2.64, Mann-Whitney z = 2.26. Entry 34: scores 0.138, 0.188, 0.044, 0.115 and ranks 89, 41, 203, 114 reproduce exactly.
- 30619736 entry 9: Figure 2 has 32 bars (14 green, 18 blue); SEC23IP, VOPP1 and SCAMP3 green; BCKDHA blue about 0.21 with a raised CRAPome point; no other Figure 5B enzyme among them. Entry 14: IgG lanes blank in all six strips, VOPP1 anti-WWOX band weakest, no kDa ladder in A. Entry 22: whiskers about 0.65 and 1.07, double asterisk; caption says "median", test is a t-test on means. Entry 31: 17 red names, 8 bars of -log10 p (Val/Leu/Ile about 6.3), DBT not in the 216, no measurement panel.
- 36779245 entries 15, 17, 20, 22, 27, 30: quotes verbatim; Table 1 columns give Patient 2 (23 y 11 m, missense/missense, Q230P homozygous) and Patient 5 (8 y 3 m deceased, missense/missense, Q230P homozygous); split 45/15/15. The absence claims in entries 27 and 30 hold (no age at diagnosis; no efficacy outcome for ketogenic diet or cannabidiol). Entry 18: curve order and overlapping upper bands as stated, p = 0.0085 and 0.65. Entry 37: the high-amplitude rhythm sits on C4-P4, P4-O2, T8-P8, P8-O2 while the caption says left parietal-occipital.
- 42422765 entry 0: 4D and 4E carry one asterisk each (about 9.5 vs 11.5; about 3,400 vs 4,200), 4F-4J ns; 4K (rotarod) also carries an asterisk; the text says no significant difference in velocity and distance. Entry 3: 0.2000 printed over the WT-KO bracket in 7C without asterisk; the text calls it a significant elevation; 7E **** / **** / ns. Entry 42: 7E values and the three-group layout as stated. Entry 12: seven of eight DNA and mRNA comparisons ns, hippocampal DNA one asterisk; blot values reproduce (cerebellum LD lane order differs trivially). Entry 37: Figure 3E-H values and brackets match. Entry 6: S7I has no graph; Figure 6E is WT vs KO only; 6F images only. Entry 28: S5 A-D mark one HD and three LD as dead; S5J reads 1, 0.2, 8.2, 10.7, 5.6, 1.4. Entry 32: quote verbatim in the Methods. Entry 33: no `vg`, `1.23`, `2.63` or exponent form in the Methods span; the only vector sentence is the titre assay.
