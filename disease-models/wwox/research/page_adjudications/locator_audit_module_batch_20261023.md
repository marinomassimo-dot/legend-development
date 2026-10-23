# Locator audit, manifests of the 2026-10-23 module batch (blind, 2026-10-23)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and ledger. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` and judged against the native artefacts under `files/`. Nothing was repaired.

## Scope and sampling

- First reads: 23611579, 30497978, 31597037, 33053775, 33201535, 36432491, 37438524, 40139194, 42397075, 42661025, 25708809. The small manifests (5 to 12 entries) were judged in full or nearly so; 42397075 (49 entries) was sampled (15 of 49), weighted toward figure readings, numerals, absence claims and text-versus-figure relations. Not random.
- Resumes: the entries added in 34268881 (43 to 51), 30362252 (5 to 9), 36779245 (39 to 46), 30361190 (14 to 19), 24456803 (11 to 12), found by comparing each manifest with its version before the batch. All added entries were judged.
- Preprint PPR1124524: there is no manifest for it; the completing pass is a staged receipt. Its four new figure readings (Figure 3c, Figure 3d right panel, Figure 6f, Figure 4a) were judged against the PDF.
- 42422765: entries 10, 14 and 15.

## Image reads

Every image read returned a real image (no "media removed"). Figures were ranked with `paper_packet.py rank` where it applied (42422765: embedded 2,906-px rasters of mmc2.pdf page 4, extracted with PyMuPDF; Supplementary S8 from a 300 dpi render of mmc1.pdf page 10). 37438524, 25708809 and 42397075 main figures were read from the native embedded rasters; PPR1124524 panels from 150 to 300 dpi page renders and the embedded Figure 6 raster.

Artefact findings:
- 42397075: the manifest's artefact paths for entries 0 to 29 (`PMID42397075_Aqeilan2026_*`) do not resolve in this checkout; the same article text and figures exist as `PMID42397075_Steinberg2026_*` (same SHA-256 on the figure checked) and every body quote sampled was found there. The supplementary-figures volume (16 declared artefacts, `evidence_presence.py` PARTIAL, nothing recoverable by `--search`) is absent, so supplementary-figure entries 15 and 21 to 29 cannot be verified here.

## Counts

| PMID | Entries judged | SUPPORTED | Adverse | UNVERIFIABLE |
|---|---|---|---|---|
| 23611579 | 0 to 7 (8 text) | 7 | 1 (quote-level) | 0 |
| 30497978 | 0 to 6 (7 text) | 6 | 1 (quote-level) | 0 |
| 31597037 | 0 to 6 (7 text) | 7 | 0 | 0 |
| 33053775 | 0 to 9 (1 table, 9 text) | 10 | 0 | 0 |
| 33201535 | 0 to 10 (11 text) | 10 | 1 (quote-level) | 0 |
| 36432491 | 0 to 7 (8 text) | 8 | 0 | 0 |
| 37438524 | 0 to 5 (1 figure, 5 text) | 6 | 0 | 0 |
| 40139194 | 0 to 7 (3 body, 5 supplement text) | 7 | 1 (quote-level) | 0 |
| 42397075 | 0, 2, 10, 11, 18, 22, 28, 32, 34, 35, 36, 37, 38, 39, 41 (8 figure, 5 text, 2 supplement figure) | 12 | 1 | 2 |
| 42661025 | 0 to 11 (12 text) | 12 | 0 | 0 |
| 25708809 | 0 to 11 (3 figure, 9 text) | 12 | 0 | 0 |
| 34268881 (resume) | 43 to 51 (8 table/supplement text, 1 body) | 8 | 1 | 0 |
| 30362252 (resume) | 5 to 9 | 5 | 0 | 0 |
| 36779245 (resume) | 39 to 46 (5 table, 3 body) | 8 | 0 | 0 |
| 30361190 (resume) | 14 to 19 | 6 | 0 | 0 |
| 24456803 (resume) | 11 to 12 | 2 | 0 | 0 |
| PPR1124524 (receipt) | Figure 3c, 3d, 4a, 6f | 4 | 0 | 0 |
| 42422765 | 10, 14, 15 (3 figure) | 2 | 1 | 0 |
| **All** | **141** | **132** | **7** | **2** |

Adverse rate: 7 of 139 judged triples (5.0 percent). Mode: hand-weighted sample (all or nearly all entries of the small manifests, 15 of 49 for 42397075, all added resume entries, 4 preprint readings, 3 repaired entries); adverse = OVERSHOOT or UNDERSHOOT; UNVERIFIABLE excluded from the denominator (2). Substantive adverse only (quote-level excluded): 3 of 139 (2.2 percent). Figure triples alone (19 judged, supplementary-figure UNVERIFIABLE excluded): 2 of 19.

## Adverse triples

| Manifest | Entry | Verdict | Reason |
|---|---|---|---|
| 42397075 | 2 | OVERSHOOT (numerals) | Figure 2F (fig_p33 raster, ticks at -3 to +1) gives WWOX-KO RGs about +0.99 and Neu about -2.38; SCAR12 RGs about -0.27 and Neu about +0.18; WOREE RGs about +0.08 and Neu about -0.07. The quote reads KO RGs about +0.55 and Neu about -2.6, and SCAR12 Neu about -0.2 (sign wrong). The proposition's core (the phenotype sits in the engineered knockout, patient lines near wild type) holds and panel D counts (5649, 3020, 3422, 5916; sum 18007) are right; entry 35 of the same manifest reads the same panel correctly. |
| 34268881 | 50 | OVERSHOOT | The proposition says mTOR, autophagy, 4E-BP and rapamycin occur zero times in the article JATS. The Results (RNA-seq paragraph on the top 100 downregulated genes) name autophagy (IFI16, MDM2, RB1, PLAT, RB1CC1) and the mTOR pathway (EIF4EBP1, PIK3CA, RB1CC1); mTOR, autophag and EIF4EBP each occur once in PMC.xml and PMC_r2.xml. Rapamycin occurs zero times. The quoted first sentence itself is as stated. |
| 42422765 | 15 | OVERSHOOT | Figure 2E lane values reproduce the quote exactly, but the proposition's first clause, that WPRE removal did not lower transgene burden, is contradicted by the same lanes: at 2E10 protein is 0.8/0.9/0.3/0.1 without WPRE against 11.6/11.9/4/2.4 with it, and at 4E10 4.7/5.9/1.5/0.4 against 25.6/22.3/11.6/6.2; the Results text says expression was reduced without WPRE. The six-fold dose increase is in neither the quote nor panel E (doses shown: 2E10 and 4E10). |
| 23611579 | 6 | OVERSHOOT (quote-level) | Quote carries only the delay and epilepsy sentence (Results 3.1.1); the proposition's "all but one achieved milestones" is in 3.1.5 and holds there, "uncontrolled" is the reader's inference. |
| 30497978 | 6 | OVERSHOOT (quote-level) | Quote is only "Arimoclomol-citrate is a proprietary compound owned by Orphazyme A/S". The ex vivo statement and the in-vitro-to-human dose caveat sit in the abstract and Discussion (both exist); neither is in the quote or its section. |
| 33201535 | 3 | OVERSHOOT (quote-level) | Quote gives the 2 of 26 and 0 of 13 hearing counts and gentamicin. "The trial states it could not establish the drug's contribution" is a Discussion sentence ("Neither bumetanide trial enrolled sufficient subjects to establish definitively ...") outside the quote. |
| 40139194 | 0 | OVERSHOOT (quote-level) | Quote supports "not all variants can be targeted; targetable ones differ in strength". The five-class list (eligible, likely eligible, unlikely eligible, not eligible, unable to assess) is in the Abstract; the Introduction quote does not carry it. |

## Notes on triples judged SUPPORTED

- Numerals recomputed: 33053775 entry 2 (Fisher exact 0.0092, 0.0055, 0.0015 and uncorrected chi-squared 0.0051, 0.0028, 0.0008 reproduce from the Table 1 counts); 36779245 entries 40 to 45 (Table 2 ASM row parsed cell by cell: broad set 8 of 13, strict set 7 of 13, vigabatrin in 8 patients, 7 of the 10 spasm patients); 34268881 entries 43 to 49 (every EV1/EV2 row and the absent-symbol search reproduce; 2,269 rows parsed); 42422765 entry 14 (Figure 2B arms and day marks) and entry 10 (S8A and S8B: P1 at 100 percent to day 300, only P5 at 75 percent; P3 n=3 at 67 percent from about day 24; S8C and S8D ns brackets); 42397075 entries 35, 36, 37, 39, 41 and 11 (Figure 2F bars, 3B medians, 3K and 3L, 4C values and n 2396 and 2152, 4J WT marks outside and KO marks inside the null, 6A(ii) brackets), entry 32 (6E bars), entry 38 (n 7, 5, 8, 11).
- 25708809: Figures 3B to 3D, 5C and 6C read as stated (6C: higher-miR-153 curve to zero by about month 20, lower curve 100 percent to about month 14, then 75 and 50 percent); the miR-163 and miR-300 typographical errors exist in the text; no brain or neural term occurs in the article.
- 37438524 entry 1: Figure 2 arrows as stated (the figure also routes no or little damage with skipping or retention to possibly amenable, which the proposition does not deny).
- 30362252 entry 5: the only occurrence of lactate in the article is that sentence. 24456803 entry 12: biops and muscle occur zero times; mitochond occurs three times (one Discussion sentence on murine retina, two reference titles).
- 30361190 entries 14 to 19: both children's investigation lists, vigabatrin outcomes (first child resolved, second child "added with a partial response") and the 11-month four-drug sentence read as stated.
- PPR1124524: Figure 3c bars about 60, 34, 31, 59, 36 with N=3, 2, 2, 3, 3 and no O-KO normal-diet bar; Figure 3d right panel about 117 and 125, 53 and 56, 106 and 58; the Results text gives 59.1 and 36.1 per FOV for remyelination, which equal the Figure 3c MBP-intensity bars, not the 3d axon counts (the receipt's text-versus-bars disagreement stands; this possible mislabel is mine, not stated by the paper). Figure 4a N=2, 2, 3 with six nuclei counts summing to the printed 40,906. Figure 6f: WWOX band faint but present in all six KO lanes (embedded raster).
- 40139194 entry 5: the quote stops at "considered" and the verdict "not eligible" follows in the next two words; counted SUPPORTED.
- 42397075 entries 22 and 28 (supplementary figures 10 and 1) are UNVERIFIABLE: the supplementary-figures volume is absent from the checkout and from the SHA-256 search. No guess was made.
