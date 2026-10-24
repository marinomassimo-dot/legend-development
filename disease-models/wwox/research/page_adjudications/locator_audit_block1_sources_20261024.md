# Locator audit, block-1 sources of 2026-10-24 (blind, 2026-10-24)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and ledger. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` and judged against the native artefacts under `files/`. Figure surfaces were chosen with `framework/scripts/paper_packet.py rank` and read against their axis ticks. Nothing was repaired.

## Scope

The two manifests that had never had a blind audit and that a held research candidate rests on. The commission asked for about 40 percent of each manifest, weighted toward numerals, negations, quantifiers and text-versus-figure relations, plus every entry carrying a `contradicts_locator` declaration. **Neither manifest carries a `contradicts_locator` declaration** (zero occurrences in either JSON), so that sub-scope is empty; the weighted sample would have been 9 and 8 entries, but because the two named propositions reach across nearly every entry, the audit was taken to **exhaustive over both manifests** instead.

| PMID | Entries in scope | Why |
|---|---|---|
| 42154236 (Verteneuil, Cdk7-cKO) | 0 to 22 (all 23) | never audited; proposition A rests on entries 0, 2, 3, 4, 18, 19, 20, 22 and on the absence of any EEG surface |
| 42401046 (Helton, SB415286) | 0 to 19 (all 20) | never audited; proposition B rests on entries 0, 1, 4, 5, 6, 7, 11, 13, 14, 19 |

## Image reads

All image reads returned real images; no placeholder and no missing artefact. 42154236 main figures were read from the 300 ppi embedded rasters under `files/figure_renders/PMID42154236_r3c/` (Fig 1 p03 2056x1724, Fig 2 p04 2056x2224, Fig 3 p06 2056x2069, Fig 4 p07 2056x1974, Fig 5 p08 2056x2750, Fig 6 p10 2056x2591); supplementary panels from the ESM PNGs (`18_2026_6139_Fig9_ESM.png` 902x460 Wnt5a/YKL, `Fig12_ESM` 2022x1537 toluidine cortical thickness, `Fig15_ESM` 2155x2652 open field and novel object). 42401046 figures were read from the NIHMS JPEGs, each of which `paper_packet.py rank` pairs to the PDF embed at 0.0000 relative aspect and 300 ppi (f0001 1795x670, f0002 1345x804, f0003 1795x1871, f0004 1601x2100, f0005 1796x1767, f0006 1797x773) and the supplement JPEG `NIHMS2199027-supplement-MMC1.jpg` 1667x1542 (rank: about 238 ppi assumed, no printed size on disk).

## Counts

| PMID | Judged | SUPPORTED | Adverse (OVERSHOOT or UNDERSHOOT) | UNVERIFIABLE | Anchor-level only |
|---|---|---|---|---|---|
| 42154236 | 23 | 23 | 0 | 0 | 1 |
| 42401046 | 20 | 20 | 0 | 0 | 1 |
| Total | 43 | 43 | 0 | 0 | 2 |

Adverse rate: **0 of 43 judged triples (0.0 percent)**. Mode: exhaustive over both manifests (100 percent of entries, against the about 40 percent weighted sample commissioned); adverse = OVERSHOOT or UNDERSHOOT; no entry was excluded from the denominator. Counting the two anchor-level defects as well: 2 of 43 (4.7 percent).

## Adverse triples

None. No proposition in either manifest claims more or less than its quote and its artefact carry.

Anchor-level only (the proposition is supported; the printed location or surface metadata is wrong):

| Manifest | Entry | Reason |
|---|---|---|
| 42154236 | 22 | The label "Supplementary Figs 7, 8, 10-15" mixes two numbering systems: the article has nine supplementary figures, and the ESM *file* numbers are not the supplementary numbers (`Fig9_ESM` is Supplementary Fig. 9, `Fig12_ESM` is Supplementary Fig. 2, `Fig15_ESM` is Supplementary Fig. 6). Every content statement in the entry was verified against the files it names. |
| 42401046 | 18 | "ESM Fig 1 (about 500 ppi)": `NIHMS2199027-supplement-MMC1.jpg` is 1667x1542, about 238 ppi assumed; the 500 ppi figure of this corpus is MMC2 (3500x1070). The panel values read correct. |

One quote-coverage note, below the anchor level: 42401046 entry 5 states three results (dispersion, migration, and the contralateral cell-count increase), and its quote carries only the first two. The third is carried by Fig 3E (contralateral about 205,000 to about 143,000, marked \*) and by the Fig. 3 legend sentence "SB415286 treatment significantly reduced aberrant neurogenesis after IHK compared to vehicle treated mice", so the source supports the proposition as written; only the chosen quote is narrower than it.

## The two named propositions

**A — Cdk7 loss in postmitotic cortical neurons costs dendrite and axon growth, cortical thickness and social behaviour, with morphology and behaviour measured and no EEG: SUPPORTED AS WRITTEN.** The deletion is Nex-Cre, postmitotic cortical projection neurons. Dendrites: Golgi-Cox total length and branching reduced in vivo (Fig 2l-n; n = 30 neurons from 3 animals per genotype) and in vitro (Fig 3c, about 615 vs about 305 micrometres, \*\*\*; n = 15 GFP and 11 Cre-GFP from two cultures). Axons: in utero mGFP electroporation at E15.5 read at P7 gives ipsilateral enrichment with progressive weakening across the corpus callosum and contralaterally (Fig 2o-p, P < 0.0001, F 1,3560 = 25.31), which the authors state as an axonal growth defect. Cortical thickness: Fig 2d about 1355 vs about 1130 micrometres and Fig 2e corpus callosum about 228 vs about 172, both marked \* only. Behaviour: three-chamber interactions about 44.5 vs about 25 (\*\*) and time about 127 vs about 52 s (\*\*\*\*), olfactory dishabituation lower for urine G3 (\*\*) and G4 (\*); marble burying, T-maze, open field and novel-object recognition all ns. EEG: the strings EEG, electroencephalograph and electrocorticograph do not occur anywhere in the article, title to references — no electrophysiology was recorded. Two caveats the entries themselves state and the audit confirms: the thickness, callosum and density measures are n = 3 per genotype under a one-sided Mann-Whitney whose smallest attainable value is P = 0.05, and the Cdk7 and cyclin H Western blots rest on one sample per age and genotype.

**B — whatever the GSK3-inhibitor paper measures in adult temporal-lobe epilepsy: SUPPORTED AS WRITTEN, and the manifest's scoping of it is correct.** 8-10-week-old adult C57Bl6/J and POMC-eGFP mice; SB415286 10 mg/kg/day i.p. in 10 percent DMSO / 45 percent PEG400 / 45 percent saline, one dose level, daily for 14 days beginning 24 h after kainate, histology at day 14 (Fig 2 timeline). What is measured is histological and immunohistochemical only: Axin2 immunoreactivity as Wnt activity (Figs 1, 5, 6), granule cell layer width, immature granule cell migration, granule cell count and primary dendrite angle (Figs 3, 4), plus body weight (MMC1). Seizures were scored behaviourally by modified Racine for 2 h at induction only, to define status epilepticus; there is no EEG and no spontaneous-seizure or seizure-burden outcome in this study — the only EEG and seizure-burden statements in the article are citations to prior work in the reference list and the Introduction's account of Chir99021. n = 6 per group, sexes pooled.

## Notes on triples judged SUPPORTED

- 42154236 entries 0 to 13 are body quotes; `locator_audit.py` matched 14 of 14 text quotes in the JATS and the strength scan flagged none. Each numeral was checked against its own legend: entry 5's "4 of 7" reproduces (Fzd10 0.1972, Nfatc1 0.0286, Plcb3 0.0361, Plcb4 0.4556, Plce1 0.0472, Prkcd 0.0145, Wnt5a 0.0601, one-sided tests, no multiplicity correction stated); entry 9's Dunn value "> 0.9999" is verbatim; entry 8's 52.4 percent is verbatim and is consistent with the Fig 6c medians (about 75 to about 115 against a GFP control of about 230, "roughly half of control").
- 42154236 entry 6 quotes the body sentence that cites "(Supplementary Fig. 8)" for the YKL-5-124 result. That cross-reference is the article's own slip — Supplementary Fig. 8 is the IPA Axonal Guidance diagram and the YKL-5-124 RT-qPCR is Supplementary Fig. 9 (the article's supplementary citations run one short from Supp. Fig. 5 onward, and the Supp. 4 and Supp. 5 legends are duplicates). The proposition names no number, so it is unaffected; entries 7 and 17 anchor the panel correctly.
- 42154236 entry 17: ESM Fig9 read against its ticks — vehicle 1.00 at 2 h, about 1.46 at 4 h, about 0.91 at 8 h, about 0.56 at 24 h; YKL 100 nM about 0.57, 0.63, 0.70, 0.77; at 24 h the 100 nM bar does sit above vehicle; one to two dots per bar, SD bars, no test marker. The entry's reading of a non-monotone vehicle course is the honest one.
- 42154236 entries 16 and 19: 976 DEGs, 114 (11.7 percent) up and 862 (88.3 percent) down at FDR < 0.1 with five animals per genotype are printed on Fig 5b-c and the heatmap columns; Fig 2b brain weight about 420 vs about 347 mg (\*\*\*), Fig 2h NeuN density up (\*), Fig 2g, j, k ns.
- 42154236 entry 21: Fig 1c bars read 0.86, 0.48, 0.30, 0.61 for cKO at E15.5, P0, P7, P30 — the entry's four values are right, and its word "progressively" is qualified by the values it then lists (P30 recovers above P7).
- 42401046: `locator_audit.py` matched 13 of 13 text quotes; the strength scan flagged none. Figure values reproduce against the ticks — Fig 1C vehicle about 5.3 and 6.3 against SB about 25 and 32 with \*\* between the two SB bars; Fig 3C about 148 vs about 112 (\*\*), 3D about 58 vs about 29 (\*\*\*), 3E ipsilateral about 10,000 vs about 37,000 ns against saline about 115,000, contralateral about 205,000 to about 143,000 (\*); Fig 4B ns, 4C about 21 vs about 21.5 against IPS about 14.5, 4D about 157,000 vs about 153,000 against IPS about 85,000, 4E the only separating panel; Fig 5B about -6 (points -28 to +23), about 24.5, about 15, about 33, Fig 5D about 14, about 21.5, about 14, about 30 (\*); Fig 6B about 5, about 20.5, about 17.5, about 31; MMC1 IHK arms about +6.7 and +9.3 percent at day 14 against saline near zero, IPK about -11 percent at day 1 with recovery, treated and vehicle arms overlapping in both models.
- 42401046 entry 3's "about 5- and 7-fold" are the article's own figures, printed in the Results sentence and repeated in the Fig. 1 legend; the ratio of the Fig 1C bars (about 4.7 and about 5.1) is lower, which is the usual gap between a per-animal fold change and a ratio of group means, and the entry attributes the numbers to the paper rather than to the bars.
