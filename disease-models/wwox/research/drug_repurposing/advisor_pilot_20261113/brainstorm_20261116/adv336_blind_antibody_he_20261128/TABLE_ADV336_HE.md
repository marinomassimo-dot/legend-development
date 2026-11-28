# ADV-336: blind image reading of two antibody-control panels (HE, 2026-11-28)

Reader: HE (ACTOR_ID plan), session c72e94ee, claude-sonnet-5-5, effort high. No delegate. For IT's ADV-335.
Blind: IT's adv335_antibody_it_20261128/ folder, held reading notes and note files in the two supplement folders, and any expected answer were not
opened. Extraction only: what is seen and printed; no claim; not medical advice.

## Sources

| Paper | File (under files/fulltext/) | sha256 (first 16) | Read |
|---|---|---|---|
| Repudi 2021, PMID 33914858 | ..._operator_supplied_supplement/extracted/awab174-suppl_data/brain-2020-02464-File009.pdf | 686ebcd80ef31082 | p. 7 (figure, viewed and measured), p. 16 (legend) |
| Repudi 2021 | same folder, File014.xlsx (antibody table); PMID33914858_Repudi2021_Brain_operator_supplied.txt (immunofluorescence methods) | not hashed | those rows and paragraphs |
| Steinberg 2026, PMID 42397075 | PMID42397075_Steinberg2026_OUP-Supplement/brain-2025-03809-File012.pdf | 18864bfbdd8329a8 | p. 5 (uncropped 1K, viewed, native image measured), p. 2 (1B, viewed only) |
| Steinberg 2026 | same folder, File010 (figure p. 2, legend), File009 (immunoblot methods), File011 (antibody table) | not hashed | those parts |

## A. Repudi 2021, Supplementary Figure 1, panels A to C

These are **immunofluorescence images, not blots**: no band, no kDa, no ladder and no loading control (NOT PRINTED; panels A, B, C checked).

| Item | Panel A | Panel B | Panel C |
|---|---|---|---|
| Tissue | cortex | cerebellum | cortex |
| Rows | N-Control, N-KO (Nestin-Cre per legend title) | N-Control, N-KO | S-Control, S-KO (Synapsin I-Cre: neuronal) |
| Age (legend) | P16 | P16 | P17 |
| Channels | merge, WWOX (red), NeuN (green), merge | WWOX, Hoechst+WWOX, NeuN+WWOX | Hoechst, NeuN, WWOX (red), merge with white arrows |
| Scale bar (legend) | 100 µm | 100 µm | 20 µm |
| KO beside its control | yes | yes | yes: neuronal-specific KO row directly under its control |
| Stained structure, control | many NeuN-positive cells with red cytoplasm | a bright red cell row at the edge of the granule layer (Purkinje-cell position; no Purkinje marker in the panel) | red ring around the nucleus in NeuN-positive cells |
| As seen, KO | red near background | red absent to the eye | red strongly reduced, **not absent**: faint rings remain in some cells of the S-KO row; arrows mark NeuN-positive cells without visible red |
| WWOX channel mean, control / KO (0-255, my render at 200 dpi) | 38.7 / 5.4 (p99 147 / 27) | 30.8 / 0.9 (p99 230 / 7) | 42.9 / 10.9 (p99 127 / 61) |
| n animals | NOT PRINTED ("Representative images") | NOT PRINTED | NOT PRINTED |
| Quantification | none printed | none | none |

Intensities are read from the compressed published figure; acquisition and display settings are not printed, so they describe the picture, not protein amount.
Antibody (File014): "Rabbit anti-WWOX", 1:5000, catalogue "N.A" (no supplier printed). NeuN: mouse, Millipore MAB377, 1:500.
Methods: P17-P18 mice, 2% PFA perfusion, cryosections of 12-14 µm.

## B. Steinberg 2026, uncropped Supplementary Figure 1K

Page title: "Week 16 COs of WT vs WWOX-KO vs AAV9-hSyn-hWWOX rescued samples". Lanes, left to right: ladder, JH WT, JH WKO-1C, JH WKO-2C,
JH WKO-1C AAV9, JH WKO-2C AAV9, ladder. Two separate strips (HSP-90 above a dashed line, WWOX below); the lower strip starts at the 50 kDa marker and
ends a little under the 37 kDa marker.

Method: native image of the lower strip (649 x 203 pixels), vertical darkness profile per lane (median over 60 columns), peaks with prominence 2 or more
(script band_profile.py.txt). Ladder: the large top blob taken as 50 kDa (y 18 left, 40 right), the large bottom blob as 37 kDa (y 137 left, 151 right),
linear tilt across the strip, log-linear interpolation. An **unlabelled ladder band** between them computes to about 42.5-42.7 kDa. Precision is about
±1 kDa (saturated marker blobs); values above 50 kDa are extrapolated.

Apparent size in kDa (peak darkness 0-255; about 240 is saturated):

| Position | JH WT | WKO-1C | WKO-2C | WKO-1C AAV9 | WKO-2C AAV9 |
|---|---|---|---|---|---|
| strong upper band | 50.6 (241) | 50.4 (241) | 50.7 (241) | **absent**; only faint peaks at 53.1 (26) and 50.2 (36) | 51.0 (240) |
| companion just below, "near 48" | 48.4 (51) | 48.2 (68) | 48.3 (127) | 48.5 (14), very faint | no separate peak |
| "near 46" | **none** | **none** | **none** | **none** | **none** |
| diffuse faint band about 44.5 | none | none | none | 44.5 (46) | 44.7 (47) |
| band about 42 | **41.6 (154), strong** | 42.2 (17), trace | 42.4 (23), trace | none | 42.5 (23), trace |

- **No lane has a band measured at 46 kDa by this ladder.** The only strong band that is in WT and missing in the knockout lanes runs at about 41.6 kDa,
  at the level of the unlabelled ladder band; the page labels the strip "WWOX (46 kDa)".
- **The bands near 48 and 50 kDa are present in the knockout lanes** (WKO-1C and WKO-2C), as strong as or stronger than in WT. Both are missing or very
  weak in one lane only, WKO-1C AAV9.
- HSP-90 strip: one band in every lane, near the 75 kDa marker side of the strip; loading control present (intensity not measured).
- Uncropped 1B (iPSC lines, p. 2, viewed, not measured): the WT-only strong band again sits level with the unlabelled ladder band, with traces in knockout lanes.

### How the assembled figure and its legend differ from the uncropped strip

- Assembled panel K (File010 p. 2) shows a narrow WWOX strip: the strong WT band, and faint **higher** bands in the two AAV9 lanes. The strong bands at
  about 48-51 kDa are not inside that strip. Printed under it: 1 (WT), 0.8 and 1.4 (AAV9 lanes).
- Legend footnote: "* The specific WWOX bands are the lower 46kDa band and the upper band at ~48kDa."
- Inference (mine, from relative position): the legend's "upper ~48" band is most likely the faint band measured at about 44.5 in the AAV9 lanes, and its
  "46" the band measured at about 41.6, that is, the authors' sizes sit about 4 kDa above this ladder reading. The paper prints no arrow that settles which
  pixels the footnote means. The alternative reading (footnote = the measured 48.4 band) would name as specific a band that is present in knockout lanes.

### Printed method details

| Item | Printed |
|---|---|
| WWOX antibody (File011) | rabbit, WB 1:10,000, source "Aqeilan et al., 2004, PNAS"; no catalogue number |
| Loading control | HSP90, Cell Signaling #4874, rabbit, 1:1000 |
| Sample | cerebral organoids, week 16; 30-50 µg protein |
| Replicates | "Blots were repeated and quantified 2-3 times per experiment"; organoids or independent differentiations per lane: NOT PRINTED |
| Knockout lines | WKO-1C and WKO-2C (CRISPR, exon 1 per methods) |

## Receipt

Two receipts of depth queried_not_full_read recorded in disease-models/wwox/registries/fulltext_read_receipts.jsonl (workflow ADV-336).
