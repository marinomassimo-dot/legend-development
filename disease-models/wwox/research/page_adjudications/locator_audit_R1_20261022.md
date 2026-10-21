# Blind locator audit — group R1 (missense proteostasis) — 2026-10-22

**Auditor.** Blind adversarial locator auditor. Received only the `(proposition, quote, anchor)` triples of
`disease-models/wwox/research/deepdive_manifests/PMID<id>.json` for the six papers below (printed by
`python3 framework/scripts/locator_audit.py --pmid <PMID> --triples 0`) and the persisted source
artefacts. Not opened: the dossiers, the reader's note, its commit candidate, the reader's
self-evaluation, the group's answers in the selection file. Read-only toward every canonical file; the
only file written is this one.

**Method.** Every artefact was digested on disk and matched its manifest `sha256` before reading
(table below; all matched). Figures were read from the surface on disk; `paper_packet.py rank` was run
for each paper. For 31402619 the ranking is dominated by a supplementary PDF and lists no better surface
for the main figures than the 709 px JPEG; for 42157447 and 38731820 it reports no PDF on disk, so the
JPEG is the best surface (709 to 787 px wide, raster, not a vector page); for 38378758 the ranking points
to supplementary PDF pages that do not carry Figure 3 or Figure 6, so the 700 px JPEG was used; for
42875792 the webp and TIFF files are raster (the TIFF is 2253 by 2059 and was rendered to compare with the
PNG render, which it matches). Where a panel was small I upscaled a crop with ImageMagick; upscaling adds
no information, so every digit read from a 700 px JPEG is stated with that limit. Marker counts were made on
distinct markers, not on bars; overlap is stated where it applies.

## Source surfaces, verified before reading

| Paper | Artefact | SHA-256 (full) | Match |
|---|---|---|---|
| 31402619 | files/fulltext/PMID31402619_Abbink2019_PMC6689685.xml | 52eb6a4e75c1b84acd479e549794c9df43597b08cd98dc446428d31d4a0bbcb2 | yes |
| 31402619 | files/figures/PMID31402619/ACN3-6-1407-g001.jpg | f6a9952c60c165f69d186e6105ad90a854285e4480c48616272f8270126149ca | yes |
| 31402619 | files/figures/PMID31402619/ACN3-6-1407-g005.jpg | 982ed96b1f0d5a4b2c1d30b1e5c660bd94aa72b33f9275ad68a6043e820d44fe | yes |
| 31402619 | files/figures/PMID31402619/ACN3-6-1407-g006.jpg | 7ddc56e87ccb4130fe348154ddb61cf249693a3943e3395dd747744e82ef7c2f | yes |
| 31402619 | files/supplement/PMID31402619/ACN3-6-1407-s009.docx | 5dbfa78fc2b3f1b1c667a4a00525a28ac738037e721b03d4b1c8af703ea7b864 | yes |
| 31402619 | files/supplement/PMID31402619/ACN3-6-1407-s001.pdf (read for captions; not declared in the manifest) | f995e725ceb18aa180cf5066c241e53e72bf32e385cbec7bb839637b19bb8297 | n/a |
| 31402619 | files/supplement/PMID31402619/ACN3-6-1407-s002.xlsx (antibody table; not declared) | c246a37091039c48968739951ea51b5bf3509117a06154a43ee4724e39e189a2 | n/a |
| 31402619 | files/supplement/PMID31402619/ACN3-6-1407-s008.pdf (reference qPCR data; not declared) | 3f240f4be8a0154b007d1ff150da3864d156d4a38f4424eeba30ea5b498bf607 | n/a |
| 42157447 | files/fulltext/PMID42157447_DeLeeuw2026_PMC13394997.xml | 9090b797bb7084def2c13d2c5e5c35bbac5af2e6cb7415375490b33398c70232 | yes |
| 42157447 | files/figures/PMID42157447/ACN3-9999-0-g001.jpg | f58ec9adc00ac47e4271f1a5d99bdae8026c54b402424a24acc1883d98259bb8 | yes |
| 42157447 | files/figures/PMID42157447/ACN3-9999-0-g003.jpg | 13c4a55cbf083cc84373c6c1228e930a2cea67cf3d498bcd7f885dcc642b167b | yes |
| 42157447 | files/figures/PMID42157447/ACN3-9999-0-g004.jpg | d171312de573b0d2f13cd10148c4f7b14460db2cbfe141cedffa692928b8df7d | yes |
| 42157447 | files/figures/PMID42157447/ACN3-9999-0-g005.jpg | 12f4d025761a0e326c876771696415ff933607bb6320ca30562a5090545dfbdd | yes |
| 42157447 | files/figures/PMID42157447/ACN3-9999-0-g006.jpg | 503e66837e83f7845251d9ecf8b2a53b0573e977142ad02e50eb13abf2b9acd1 | yes |
| 42157447 | files/figures/PMID42157447/ACN3-9999-0-g007.jpg | 51f5e75f00e84cfa5d90aec91478181445535881e901cb63885df3cb6738499d | yes |
| 42157447 | files/figures/PMID42157447/ACN3-9999-0-g008.jpg | 8bbddf81c1fd1c313004b61bbe336210eafc6f8011d72da3ceec1d03095b3bd4 | yes |
| 38731820 | files/fulltext/PMID38731820_Poliquin2024_PMC11083348.xml | 56c4d87b5eeda80116ba5be971b2c3440034a759038839e7bd46d8bf530ff335 | yes |
| 38731820 | files/figures/PMID38731820/ijms-25-04601-g002.jpg | bd192c7ae1e306852faf95d21b703fde85b4cda59fbee0f990fd33f8a319be01 | yes |
| 38731820 | files/figures/PMID38731820/ijms-25-04601-g003.jpg | ae93a868405791ac8e4ccde76a37aaa9e59334092c0415c531ee329973f6a58b | yes |
| 38731820 | files/figures/PMID38731820/ijms-25-04601-g005.jpg | f5d91efbdf833de50eac2899b16a300456ac07c3c9839c57320950caf257671f | yes |
| 38731820 | files/figures/PMID38731820/ijms-25-04601-g006.jpg | c80290f58f96365fc7505d64b6a9b6da43c0519e9356ac1d47c16396299c853c | yes |
| 32023956 | files/fulltext/PMID32023956_Lukas2020_PMC7037350.xml | b2e27552a0c0f3ad7f44a103cadc4ea121725f8aab3d72466fba46af3d8f676e | yes |
| 32023956 | files/figures/PMID32023956/ijms-21-00956-g001.jpg | 91e386e6b33cfee9730182d3d00b8fe6973d898e2ead1ed24998ce53355341fc | yes |
| 32023956 | files/figures/PMID32023956/ijms-21-00956-g002.jpg | 89285a45cce1490bb55fa0a2a052ef97976c9c9208a359febb7ce50cebb2e550 | yes |
| 38378758 | files/fulltext/PMID38378758_Clausen2024_PMC10879094.xml | a8e2eba966a9424550f918669a4f320d66ee594b9b736831f30f1910501b6510 | yes |
| 38378758 | files/figures/PMID38378758/41467_2024_45829_Fig3_HTML.jpg | f622a6daf4a84774c080e79a5721c39390541c04675ab5ef7f3cb93d67bbb04e | yes |
| 38378758 | files/figures/PMID38378758/41467_2024_45829_Fig6_HTML.jpg | cb0d70039678ef3fa7435355fea74f4d05a2f143e531058e6a7bc541197498f5 | yes |
| 42875792 | files/fulltext/PMID42875792_RathanKumar2026_PMC13670827.xml | 4c16ca12f9cf10ad23f2236a840865c11118c933e033d23802f120e015c3d88d | yes |
| 42875792 | files/supplement/PMID42875792/12967_2026_8708_Fig1_HTML.webp | d717799737a3c9695d634c1e3cd3b31399db70209e266b9e5206b8fc08eda15a | yes |
| 42875792 | files/supplement/PMID42875792/12967_2026_8708_Fig4_HTML.webp | 1adf6876509ffa1f1606e3cf541613e03a9e56bda9a641636b9bfda78ee3d2db | yes |
| 42875792 | files/supplement/PMID42875792/12967_2026_8708_Fig5_HTML.webp | 8d3276bb20f24e5e4e1791198f6655b509b2e1ca8e22c8d88fd425be0e1d80ea | yes |
| 42875792 | files/figures/PMID42875792/SuppFig3_render.png | 17389413eb456fd4e9019c6a5dc1b41b487af44cb45343841bcd70b68b715d5d | yes |
| 42875792 | files/figures/PMID42875792/12967_2026_8708_MOESM3_ESM.tif | 40d9f4786b8e91c9e2dc1077c35316e346082a3550f14e9adc36bffd79d6bb76 | yes |

Mechanical pre-check (`locator_audit.py`, default run): 31402619 reported one quote not found in the XML
(entry 2); that quote is a supplementary-methods sentence and does occur in the declared docx, so the
mismatch is a surface mismatch, not an absent quote. The other five papers matched every text quote.

## Counts per verdict per paper

| Paper | Triples | SUPPORTED | OVERSHOOT | UNDERSHOOT | UNVERIFIABLE |
|---|---|---|---|---|---|
| 31402619 | 14 | 11 | 3 | 0 | 0 |
| 42157447 | 20 | 16 | 3 | 0 | 1 |
| 38731820 | 18 | 16 | 1 | 1 | 0 |
| 32023956 | 13 | 10 | 3 | 0 | 0 |
| 38378758 | 16 | 10 | 5 | 1 | 0 |
| 42875792 | 14 | 13 | 0 | 0 | 1 |
| Total | 95 | 76 | 15 | 2 | 2 |

## The two numeric text-versus-panel conflicts, resolved by reading the panel

**32023956, Figure 1B: panel and text disagree; the panel is the consistent one.** The panel box prints
Pearson r 0.8771, 95 percent interval 0.8381 to 0.9071, R squared 0.7692. The text gives r 0.9448 for the
same comparison. Panels 1A and 1C match the text (0.8729 and 0.7992) and each prints an R squared equal to its
r squared (0.7620 and 0.6388). The text itself gives R squared 0.7692 for this panel in the same paragraph,
which is 0.8771 squared and not 0.9448 squared. The printed interval is the interval Fisher's transform gives
for r 0.8771 at about 178 variants; for 0.9448 it would be about 0.93 to 0.96. I also measured the panel: I
located the plot axes and tick positions, extracted marker centroids from the JPEG (731 by 1511 pixels),
calibrated them to the axis scales and computed Pearson r over the extracted points (overlapping markers near
the origin were counted by blob area, so this is distinct blobs weighted by area, not a count of animals or
of variants). Panel B gives about 0.86; panels A and C, extracted the same way, give 0.90 and 0.81 against
printed 0.8729 and 0.7992, so the method carries an error of roughly 0.03. The measurement cannot reach
0.9448. Resolved in favour of the panel (0.8771); the text value 0.9448 is the outlier.

**38731820, Figure 6: the panel draws six animals; the legend says N=3.** In panels C and E I counted
distinct coloured markers at baseline: purple, green, red, orange, blue, yellow = six, none overlapping at
baseline in C (about 37, 20.5, 13, 12, 10, 1 events) and none in E (about 260, 110, 88, 50, 33, 0 seconds);
panel D carries the same six colours. The arithmetic corroborates the count independently: the six baseline
values in C average 15.58, the mean the text reports, and their standard error with n = 6 is 4.99, which is the
reported 4.987; a mean of the same three values would not give that error. The same holds for the treated
mean (about 3.67) and the time-seizing mean (about 90). The panel is the consistent surface; the legend
(`N = 3 female heterozygous ...`) is the outlier, and the Methods separately say male and female mice were
implanted, which the legend's "female" also contradicts. Resolved in favour of the panel: six animals.

**42157447, Figures 6 and 8 text versus panel (both confirmed as the reader recorded).** Figure 6: the panel
letters on the image are A = PBA and B = butyrate for A288V, and C = PBA and D = butyrate for S295L; the legend
and text assign the opposite letters; the significant bars are the PBA bars on the image (asterisks on A and C,
ns on B and D), so conclusions agree and lettering does not. Figure 8: the red P values printed on the panels
are 0.0004 (S295L butyrate), 0.0003 (S295L PBA), 0.7252 (A288V butyrate) and below 0.0001 (A288V PBA); the
text and legend give 0.0119 and 0.1046 for the two butyrate comparisons. Direction and conclusion are the same.
The digits come from a 709 px JPEG upscaled for reading; I read 0.0004 and 0.7252 clearly but the surface does
not rule out a one-digit misreading of the last digit of 0.0004. The star counts (three stars and ns) agree
with the printed values and not with 0.0119 (one star).

## 31402619 — eIF2B missense, polysome profiling and ISRIB (the narrowing)

Surface: article XML (text), Supplementary Methods docx, supplementary file captions and antibody table (text);
Figures 1, 5 and 6 as 709 px JPEG (raster, no vector page on disk).

| Idx | Verdict | Quote as it stands | Surface and resolution | Why |
|---|---|---|---|---|
| 0 | SUPPORTED | The polysomal profiles from WT and 2b5ho samples were similar, showing that bulk mRNA translation was not grossly affected by the mutation (Fig. S1). | XML body | The sentence carries the proposition exactly. |
| 1 | OVERSHOOT | Most mRNAs with altered translation rates were increased in monosome and polysome fractions from 2b5ho mouse brains, indicating that these mRNAs were regulated at transcript level. | XML body; Fig. 1B at 709 px JPEG | The quote refers to the 33 mRNAs the authors flagged by monosome-versus-polysome distribution and verified by qPCR on several candidates, not to the 176; for the 176 the authors say they ignored distribution and read it as "altered synthesis of the encoded proteins", the opposite of what the proposition attributes to them. |
| 2 | OVERSHOOT | triturated three times with a 23G needle and centrifuged for 10min at 4 | supplement docx, Sample preparation | The quote carries only the spin; the detergents and the gradient load are in the neighbouring sentences and are correctly described, but the source says the spin removes "nuclei, membranes and debris" at an unstated g-force, not that any insoluble pool is discarded. |
| 3 | OVERSHOOT | ISRIB stabilizes the eIF2B complex formation through interaction with the eIF2Bδ:eIF2Bβ interface33, 34. | XML body, legends, supplement methods docx, antibody table (xlsx), supplement captions | The quote says nothing about measurement; the negative itself holds across everything searched (no eIF2B antibody, no occurrence of "abundance" or "eIF2B protein"), but the parenthetical inventory "Western blots for eIF2alpha phosphorylation and 4E-BP1 only" is wrong: Supplementary Figure 9 reports an MBP immunoblot. |
| 4 | SUPPORTED | Motor tests at the end of the experiment revealed that ISRIB improved performance of VWM mice in Balance Beam tests (Fig. 5C). | XML body; Fig. 5C at 709 px JPEG | Bars read about 16 to 5.5 (2b5ho), 19 to 1.3 (2b4ho2b5he), 1.3 to 2.5 (wild type), as stated. |
| 5 | SUPPORTED | average number of slips on balance beam | Fig. 5C-D at 709 px JPEG; phrase is from the legend | Placebo bars far from wild type; treated 2b4ho2b5he bars near wild type on slips, support diagonal, speed, cadence and stance; 2b5ho partway (speed about 6 to 11, support diagonal about 31 to 45). |
| 6 | SUPPORTED | ISRIB effects on gait parameters were less consistent and less pronounced in 2b5ho than in 2b4ho2b5he mice (Fig. 5D, Fig. S8). | XML body | Verbatim. |
| 7 | SUPPORTED | ISRIB did not affect eIF2α phosphorylation levels in 2b5ho and 2b4ho2b5he mice, despite reduced Gadd34 mRNA levels (Fig. 6A). | XML body; Fig. 6A | The second clause is carried by the adjacent sentence "most consistently in 2b4ho2b5he mice" and by the panel (Ddit3, Eif4ebp1 and 4E-BP1 fall only there). |
| 8 | SUPPORTED | ISRIB effects on myelin in VWM mice were evident in mature myelin Mbp and Mog mRNA levels, MBP protein levels and MOG immunohistochemistry in 2b4ho2b5he mice only (Fig. 6F and G, Fig. S9). | XML body | Verbatim. |
| 9 | SUPPORTED | ISRIB restored levels of mature myelin mRNA markers in 2b4ho2b5he mice. | Fig. 6F-G at 709 px JPEG | Mbp about 2.1 to 3.25 against wild type about 3.3; Mog about 0.08 to 0.128 against 0.11; 2b5ho Mbp about 2.7 and 3.1; MOG stain strong in treated. The treated Mbp bar returns to, not above, wild type. |
| 10 | SUPPORTED | Both findings suggest that ISRIB treatment does not fully normalize eIF2B activity, but leads to a better compensated system that still in part depends on reduced eIF2α phosphorylation. | XML body | Verbatim. |
| 11 | SUPPORTED | cannot be attributed to differences in ISRIB bioavailability in brain. | XML body | Brain exposure was measured post mortem in olfactory bulb with two wild-type animals, and blood in VWM mice was lower than in wild type; the claim as written (genotype difference not an exposure difference between the two VWM lines) holds. |
| 12 | SUPPORTED | ISRIB may preferentially impact eIF2B with | XML body | The quote is a fragment cut before its object; the same sentence completes it with "complex-destabilizing mutations" and the next paragraph carries the patient-cell caveat. |
| 13 | SUPPORTED | Additionally, ISRIB has low solubility and its bioavailability in humans needs optimization. | XML body | The soluble derivative follows in the next sentence. |

**Which verdicts bear on the narrowing of the dossier premise (31402619).** Entries 1, 2 and 3 are the
narrowing and all three are OVERSHOOT. Entry 3 (the paper does not measure the mutant protein) stands on its
core as a negative established across the XML, legends, supplementary methods, antibody table and supplement
captions; only its inventory of Western blots is wrong and the quote does not carry it. Entry 1 is the
proposition "polysome profiling by itself does not separate translational from transcript regulation". Both
halves checked. First half, can the method as the paper describes it separate them: the 176-mRNA analysis
cannot (the authors say they ignored distribution), but the paper also runs a monosome-versus-polysome
distribution analysis (33 mRNAs, called translation efficiencies by the authors) and a fraction-resolved qPCR.
Second half, does the paper add a control that does: Figure 1B shows Trib3, Eif4ebp1 and Slc1a5 raised in the
monosome fraction as well as the polysome fractions, whereas Slc3a2 and Psat1 are raised in the heavy polysome
fraction only and Ddit3 in the light polysome fraction only; that is an in-paper separation of the two
regimes at the mRNA level, and the authors read some candidates each way. Total-tissue mRNA over development
(Fig. 2B), human total-RNA microarray, 4E-BP1 protein by immunostaining and immunoblot (Fig. 6A), MBP protein
by immunoblot (Suppl. Fig. 9) and protein-synthesis measurements in astrocytes (Fig. 7C-D) are further
controls on the product side. None of them reads mutant eIF2B protein (entry 3). So the proposition holds
for the 176-mRNA headline and for the absence of any mutant-protein read; it overshoots as a statement about
the method as the paper deploys it, and it misattributes to the authors a transcript-level reading of the 176.
Entry 2 bears because "any insoluble pool is discarded by design" is not in the source.

## 42157447 — SLC6A1, pharmacochaperones versus HDAC inhibitors

Surface: article XML; Figures 1 to 6 and 8 as 709 px JPEG (raster; no PDF on disk).

| Idx | Verdict | Quote as it stands | Surface and resolution | Why |
|---|---|---|---|---|
| 0 | SUPPORTED | The remaining GABA uptake activity averaged 56.5% to 80.2% of WT levels, corresponding to a 19.8% to 43.5% loss of function. | XML body | All 32 variants significantly reduced in both conditions; the range is the authors'. |
| 1 | SUPPORTED | Baseline GABA uptake function in heterozygous SLC6A1 variants compared to WT. | Fig. 1C (file g005), 709 px JPEG | Bars run from about 0.56 (E16X) and about 0.6 (K448X) to about 0.8 (G234S); all below 1. |
| 2 | SUPPORTED | Densitometry quantification revealed that both PBA and TUDCA significantly increased total GAT‐1 protein in all four variants (Figure 4G). | XML body | The quote carries the rise; "from a small fraction of wild type" is carried by the panel read in entry 3. |
| 3 | SUPPORTED | Densitometric quantification showed that both PBA and TUDCA significantly increased total GAT | Fig. 4G (file g003), 709 px JPEG | Vehicle about 0.17, 0.15, 0.1, 0.1; PBA about 0.92, 1.0, 1.05, 1.38; TUDCA about 0.7, 0.72, 0.95, 1.02, as stated; the legend names no reporting allele. |
| 4 | SUPPORTED | PBA treatment resulted in a significant increase in uptake across all 32 variants, with the increase in uptake ranging from | XML body | The quote is cut before the numbers; the next words give 19.2% to 39.5%, and 15.8% to 32.2% for TUDCA in the following sentence. |
| 5 | SUPPORTED | PBA significantly increased GABA uptake across all 32 variants, restoring function to or above WT levels. | Fig. 2B-C (file g007), 709 px JPEG | Variant bars about 1.2 to 1.4 (B) and 1.16 to 1.32 (C), wild type about 1.14 (B); the cross-figure product 0.55-0.8 times 1.2-1.4 gives 0.66 to 1.12. Minor slip in the proposition: the wild-type bar in panel C is about 1.27, not 1.12 to 1.15. |
| 6 | SUPPORTED | inhibition is insufficient to rescue transporter function in the context of SLC6A1 variants. | XML body | Butyrate gave 7.4% to 17.8%, SAHA −5.2% to 13.4%. |
| 7 | SUPPORTED | Controls included empty-vector (pcDNA) and WT treated with CI-966 [50 μM], a known GAT-1 inhibitor. | Fig. 3B-C (file g008), 709 px JPEG | The quote is a control sentence and carries nothing of the readings; the panel read holds (butyrate about 1.05 to 1.2, wild type about 1.15; SAHA about 0.9 to 1.2, labelled ns). The butyrate panel marks only G232V as ns, so "all labelled not significant" is true for SAHA only. |
| 8 | OVERSHOOT | In contrast, butyrate significantly increased the total amount of immature protein, suggesting that it drives non‐specific protein accumulation rather than productive trafficking. | XML body; Fig. 5F-G (file g004) | In S295L butyrate raised the mature-to-immature ratio about 2.7-fold (four asterisks) and in V511M weakly, so "without trafficking" is not general; total protein rose in wild type, S295L and V511M but not A288V; butyrate also raised uptake 7% to 18% across variants, so the dissociation of quantity from function is partial. |
| 9 | SUPPORTED | Butyrate failed to increase this ratio in WT (p = 0.9572), A288V (p = 0.3665), and showed only a weak effect in V511M (*p = 0.0190). | Fig. 5F-G (file g004), upscaled crop | PBA total about 1.3 to 2.5 and ratio about 3.3 to 4.6; butyrate total about 2.8 in S295L and 1.05 in A288V; ratio about 1.1 to 1.2 in wild type and A288V and about 2.7 in S295L. The text paragraph omits S295L. |
| 10 | SUPPORTED | restoring 64.7% of WT transporter activity (Figure 6B) | XML body | A288V 64.7%, S295L 82.4%; synaptosomes are forebrain. |
| 11 | SUPPORTED | (A) 3H GABA uptake in crude synaptosomes from Slc6a1+/A288V knock-in mice. | Fig. 6 (file g001), 709 px JPEG | On the image A and C carry PBA (asterisks), B and D carry butyrate (ns); text and legend have the opposite assignment; five markers per group. |
| 12 | SUPPORTED | butyrate treatment significantly increased the number of seizure events compared to baseline (p = 0.0119) | XML body | The proposition is about the text value, which is as stated; the panel prints a different value (entry 13). |
| 13 | SUPPORTED | Quantification of seizure events in Slc6a1+/S295L mice (4-8 Hz frequency range). | Fig. 8C and 8F (file g006), 709 px JPEG upscaled | Panel prints P=0.0004 (baseline about 50 to about 102) and P=0.7252; text and legend give 0.0119 and 0.1046. |
| 14 | SUPPORTED | PBA treatment led to a significant reduction in seizure frequency in the same Slc6a1+/S295L mice | XML body; Fig. 8D and 8G | S295L about 143 to 35 and A288V about 92 to 28; the A288V result is in the next paragraph. |
| 15 | SUPPORTED | Mice were then treated daily with either butyrate or PBA | XML body | Paired t-tests in the legends carry the within-animal comparison; baselines for butyrate (about 50) and PBA (about 143) in the same S295L line differ, which the text does not explain. |
| 16 | UNVERIFIABLE | This interpretation is strengthened by the fact that TUDCA, which lacks HDAC inhibitory activity, achieved a similar magnitude and pattern of variant rescue as PBA. | XML body, legends, Methods searched for binding, thermal stability, folding, chase; figures read except Fig. 7 (file g002) | The positive claim holds, but the negative (no direct binding, thermal-stability or folding measurement) is not established: no supplement is cited or on disk, and Fig. 7 was not opened. |
| 17 | OVERSHOOT | These results suggest that both pharmacochaperoning and ER stress modulation can partially rescue function, although the effect is variant‐dependent. | XML body; Fig. 5F (file g004) upscaled | The function claim holds (salubrinal strongest in S295L, A305V, G362R), but the quote is function only: in Fig. 5F salubrinal raises wild-type-allele total protein about 2-fold and lowers it in A288V (about 0.65) and S295L (about 0.5), although the text says increased, so "quantity raised" is not carried. |
| 18 | OVERSHOOT | No significant increase was observed at 5 μM in either condition. | XML body | In S295L the response is non-monotonic (1, 2.5, 10, 20 significant), but in wild type only 10 and 20 are significant, a threshold; the authors call the response dose-dependent. |
| 19 | SUPPORTED | Due to the scale of experimental conditions tested, control values (pcDNA and CI‐966 treated) were reused across certain experiments | XML body | Verbatim. |

## 38731820 — GABRG2(Q390X), HRD1 and zonisamide

Surface: article XML; Figures 2, 3, 5 and 6 as 744 to 787 px JPEG (raster). Supplementary Figures S1 to S4 are cited and not on disk.

| Idx | Verdict | Quote as it stands | Surface and resolution | Why |
|---|---|---|---|---|
| 0 | SUPPORTED | Likewise, HRD1 overexpression reduced the γ2(Q390X) subunit expression, while other E3 ligases had no effect on the γ2(Q390X) subunit. | XML body | Four ligases tried (HRD1, UBE3A, NEDD4L, RNF34); only HRD1 lowered Q390X monomer, dimer and total. |
| 1 | SUPPORTED | reduced the levels of wildtype and mutant protein equally | XML body | "Equally" rests on a non-significant difference (0.646 against 0.688, p = 0.906), the authors' word. |
| 2 | SUPPORTED | A graph of the IDVs of the γ2(Q390X) dimers | Fig. 2B-H (file g002), 744 px JPEG | WT monomer about 0.55, Q390X monomer about 0.68, dimer about 0.6, total about 0.66; mixed total about 0.68, wild type in mixed about 0.65. |
| 3 | OVERSHOOT | However, for the α1 subunit, ZNS treatment rescued the reduction seen in the Q390X condition | XML body; Fig. 3D-F (file g003) | The quote carries only α1; β2 rises to 0.934 but the text says the rise over untreated Q390X is not significant (p = 0.088), which the proposition omits; γ2 0.572 against 0.474 is correctly marked not significant. |
| 4 | SUPPORTED | Membranes were immunoblotted for γ2 | Fig. 3A-F (file g003), 783 px JPEG | All values as listed; HRD, SEL and HRD+SEL fall below the Q390X bar on all three subunits. |
| 5 | SUPPORTED | ZNS treatment did not change γ2(Q390X) subunit expression in the mutant conditions | XML body | Verbatim. |
| 6 | SUPPORTED | However, we failed to observe the upregulation of HRD1 in the cells expressing the wildtype α1β2γ2 or the mutant α1β2γ2(Q390X) receptors. | XML body; Fig. 5A-B | Small rise at 3 and 10 μM, cell loss at 30 μM. |
| 7 | SUPPORTED | HRD1 and Sel1L expression were unchanged | XML body | The supporting figure is Supplementary S4, not on disk, so only the text statement is checked. |
| 8 | SUPPORTED | The γ2(Q390X) subunit protein was reduced to a greater degree with a higher amount of HRD1 cDNA at all three | XML body; Fig. 5C-E | Both bars are HRD1 0.25 µg (fixed at 1) against 0.5 µg; the blot has an untransfected lane and no empty-vector arm; the legend and text confirm. |
| 9 | SUPPORTED | mice 3 months of age that were treated with ZNS had fewer | XML body | p = 0.0358 and p = 0.0176, within animal against baseline. |
| 10 | SUPPORTED | N = 3 female heterozygous Gabrg2+/Q390X mice. One-tailed paired t-tests were used to determine significance. | XML legend | Verbatim; but see entry 11 and the resolution above. |
| 11 | SUPPORTED | Total number of 5-7 Hz SWDs in 24 h, during baseline and after ZNS treatment. | Fig. 6C-E (file g006), 771 by 599 px JPEG | Six distinct markers (counted, no overlap at baseline in C or E), baseline mean 15.58 and standard error 4.99 reproduce with n = 6; the yellow animal goes from about 1 to about 0 in C; duration (D) rises in one animal. |
| 12 | SUPPORTED | After recovering from headmount surgery for 7 days, a 24 h baseline recording was acquired | XML Methods, Results, legend, Fig. 6A | No vehicle arm in any of those four places. |
| 13 | SUPPORTED | male and female Gabrg2+/Q390X mice were surgically implanted with headmounts | XML Methods | EEG animals about 2 to 3 months; lysate animals 1 to 1.5 months and killed after treatment. |
| 14 | SUPPORTED | In addition to its direct effect on ion channels via altering the fast inactivation threshold of voltage-dependent sodium channels | XML Discussion | Gap-junction effects are listed as well. |
| 15 | SUPPORTED | This is at least partially due to the fact that ZNS can reduce ER stress and moderately enhance HRD1. | XML Discussion | Hedged; HRD1 unchanged in mouse (S4), BiP unchanged in het mice (1.282 against 1.272). |
| 16 | SUPPORTED | The elevated expression of BiP at baseline and lack of response to ZNS raise the possibility of a ceiling effect | XML Discussion | Verbatim. |
| 17 | UNDERSHOOT | Although increased HRD1 activity may reduce the total amount of wildtype γ2 further, the increase in surface trafficking of functional receptors by removing γ2(Q390X) may offset the decrease in the total γ2 subunit. | XML Discussion; Fig. 3D-F | There is no current or mIPSC read-out here, but surface trafficking under HRD1 was measured and went the other way (surface γ2 about 0.29 against 0.47, α1 0.5 against 0.75, β2 0.42 against 0.67), so "not measured" understates what the source holds. |

## 32023956 — GLA amenability, two cell assays

Surface: article XML; Figures 1 and 2 as 731 and 752 px JPEG.

| Idx | Verdict | Quote as it stands | Surface and resolution | Why |
|---|---|---|---|---|
| 0 | SUPPORTED | The relatively weak inter-assay correlation observed in the Bland | XML body | The sentence continues with 12.9% (23/178). |
| 1 | SUPPORTED | This analysis indicated significant disagreement in the measurement of enzyme activity depending on the examining laboratory. | XML body; Fig. 2 | Limits −194.3 to 178.7, −150.7 to 175.6, −242.5 to 228.3 as stated. |
| 2 | SUPPORTED | analysis of α-Gal A activity for GLA variants expressed as percentage difference in activity (%WT) | Fig. 2a-c, 752 px JPEG | Scatter about ±200 at low activity, narrowing at high; one red point near −750 in panel c; limits printed as listed. |
| 3 | SUPPORTED | Moreover, a similar correlation was observed between the two datasets comparing the α-Gal A activity with DGJ (r = 0.9448 | XML body | The conflict is as recorded; the text value is the outlier (resolved above). |
| 4 | SUPPORTED | Linear correlation analysis of α-galactosidase A (α-Gal A) activity presented as absolute increase | Fig. 1B, 731 px JPEG | Printed r 0.8771, interval 0.8381 to 0.9071, R squared 0.7692; marker-centroid estimate about 0.86. |
| 5 | OVERSHOOT | The most frequent finding among the non | XML body | The numbers hold (9.6%, 17 variants; zero baseline), but the headline "matters as much as the assay" is not carried: the authors conclude the 18.0% residual discordance "argues for an experimental discrepancy rather than one of definition". |
| 6 | SUPPORTED | Interestingly, the best achievable agreement was found at a threshold of 7%. | XML body | Amenable variants fall to 76 or 80 from 88. |
| 7 | OVERSHOOT | may be benign with an uncertain clinical significance | XML body | 8 of 23 (34.8%) is "a high percentage", not a majority; the authors do not say they dominate. |
| 8 | SUPPORTED | To date, there is no established correlation between the biochemical enzyme activity increase induced by DGJ and the clinical benefit. | XML body | Verbatim. |
| 9 | SUPPORTED | did not show a beneficial outcome | XML body | L294S and the S276N switch back to replacement therapy are both in the paragraph; "quantity-up, function-flat" is the proposition's gloss. |
| 10 | SUPPORTED | It should also be considered that DGJ is an active site | XML body | Lyso-Gb3 rose in non-amenable variants in the earlier cohort. |
| 11 | SUPPORTED | A less pronounced correlation was determined when comparing enzyme activity between overexpression systems and cells derived from patients. | XML body | Verbatim. |
| 12 | OVERSHOOT | The authors A.R. and J.L. received financial support from Shire Pharmaceuticals in the past. | XML back matter | The source names Shire and does not call it the manufacturer of the chaperone; two authors are tied to a diagnostics company as stated. |

## 38378758 — Parkin abundance map (the published negative)

Surface: article XML; Figures 3 and 6 as 700 px JPEG (the main figure on disk; the supplementary PDF pages the ranker lists do not carry them).

| Idx | Verdict | Quote as it stands | Surface and resolution | Why |
|---|---|---|---|---|
| 0 | SUPPORTED | In the present study we therefore rely on overexpression of the Parkin variants. | XML Discussion | The limit is named in the following sentence. |
| 1 | OVERSHOOT | As we were unable to detect endogenous Parkin in the cells (Supplementary Fig. 1D), measurement of the cellular abundance of recombinant Parkin variants is likely independent of endogenous Parkin. | XML body | The authors write "likely"; the proposition states it as fact and derives it from non-detection. |
| 2 | OVERSHOOT | This is likely due to R42P being overexpressed in our system (Supplementary Fig. 1D) and suggests that the pathogenicity of the R42P variant is linked to its low abundance. | XML body | "Function intact" rests on one mitophagy read-out in overexpression, hedged by "likely" and "suggests"; the Discussion describes R42P as unfolded at the ubiquitin-like domain. |
| 3 | SUPPORTED | The flow cytometry profile of the PRKN library showed that proteasome inhibition (Fig. 3A) shifted the peak of low abundance variants towards a higher GFP:mCherry ratio, an effect which was also observed upon knock-down of the proteasome subunit PSMD14 with siRNA (Fig. 3B). | XML body | Verbatim; chloroquine is in the next sentence. |
| 4 | OVERSHOOT | Conversely, no substantial changes were observed with chloroquine (Fig. 3C). | Fig. 3A-C, 700 px JPEG upscaled | With bortezomib the lower-ratio part of the shoulder is reduced and a bump near 0.4 to 0.6 is raised, i.e. a rightward shift, not a rise above the untreated trace; the wild-type peak count differs (about 28k against 21k) with 559,000 against 436,000 cells; chloroquine traces coincide. |
| 5 | SUPPORTED | Presumably this effect is the result of both an increased thermodynamic stability of the Parkin variants and a general reduction of protein turnover at the lowered temperature. | XML body | "Almost disappeared entirely" is the authors'; no separating control is described. |
| 6 | SUPPORTED | Representative flow cytometry profiles for landing pad cells expressing the PRKN library | Fig. 3D-E, 700 px JPEG | At 29 °C the low shoulder is nearly gone and the main peak sharpens and moves right to about 2.5; at 39.5 °C the shoulder deepens. |
| 7 | OVERSHOOT | However, treatment with the activator did not confer any substantial differences in Parkin abundance (Fig. 3F). | XML body; Fig. 3F | "Did not change variant abundance across the library" drops the authors' "substantial" and "significantly increased … globally": one compound, 10 μM, 24 hours, a pooled flow histogram with no per-variant sequencing in the methods or text, and the authors themselves allow a local effect. |
| 8 | SUPPORTED | Accordingly, we note that BIO-2007817 was also unsuccessful in increasing mitophagy in cell-based studies48, and might only stabilize variants localized to the region or domain where the compound binds. | XML body | Verbatim; the mitophagy result is cited, not the authors' own. |
| 9 | SUPPORTED | Representative flow cytometry profiles for landing pad cells expressing the PRKN library untreated (-) (n = 407,000 cells) or treated (+) (n = 426,000 cells) with 10 μM Parkin activator BIO-2007817 for 24 hours. | Fig. 3F, 700 px JPEG upscaled | The two traces overlie across the range including the shoulder near 0.7 to 1. |
| 10 | SUPPORTED | The ability of the abundance score to predict disease variants was analysed by a receiver operating characteristic (ROC) resulting in an area under the curve (AUC) of 0.69 (Fig. 6C). | XML body; Fig. 6C | Rosetta and GEMME both 0.79; six of twelve disease variants WT-like. |
| 11 | SUPPORTED | Because high abundance is a necessary, but not sufficient criterion for a variant to be functional, the abundance score is on its own not sufficiently powerful to separate all pathogenic and benign variants. | XML Discussion | Identical sentence. |
| 12 | SUPPORTED | The benign variants all displayed abundance scores similar to WT, while half of the PD-linked variants (6 of 12) displayed abundance scores lower than 0.5 (Fig. 6B). | Fig. 6B, 700 px JPEG | Pathogenic about 0 to 1.17, median about 0.52, six above and six below 0.5; benign about 0.48 to 1.03. |
| 13 | OVERSHOOT | This suggests that these variants (at already solvent-exposed positions) cause low abundance by degron formation rather than affecting thermodynamic stability. | XML body | 28 of 63 is correct and the degron is predicted, hedged by "suggests"; the clause that a folding chaperone would not repair them is not in the source. |
| 14 | SUPPORTED | Recent estimates indicate that as much as 60% of pathogenic missense variants cause loss of protein abundance33,34 | XML Introduction | Cited; the paper's own figure is 6 of 12. |
| 15 | UNDERSHOOT | Hence, potentially blocking Parkin degradation or developing small molecule stabilizers or pharmacological chaperones, such as those for TP53 and CFTR84,85, may restore cellular abundance and increase function above the pathogenic threshold. | XML Discussion; Fig. 3A-B, 3E | The activator was the only candidate stabiliser, but bortezomib and siRNA (blocking degradation) and cold incubation were also tested as probes and shifted the low-abundance population. |

**Which verdicts bear on the scope of the published negative (38378758).** Entries 7 and 8 are the negative
and its bound. Entry 8 is SUPPORTED and states the bound correctly. Entry 7 is OVERSHOOT because its wording
("did not change variant abundance across the library") is stronger than the source's "did not confer any
substantial differences" and "unable to confer significantly increased … abundance globally"; the experiment
is one pooled flow histogram, one concentration and one time, and the authors say the compound might still
stabilise variants near its binding domain. Entry 9 (the histograms overlie) is SUPPORTED. Entry 15 is
UNDERSHOOT and bears on the negative's reach: the paper does not say that only the activator was tried to
raise abundance. Read as bounded by the source, the negative is: one allosteric activator of wild-type
Parkin, one dose, one pooled readout, not a global stabiliser.

## 42875792 — HIKESHI, proteasome inhibitors

Surface: article XML; Figures 1, 4 and 5 as 1600 px webp; Supplementary Figure 3 as a 541 px render, compared with the 2253 by 2059 TIFF it was rendered from (same content).

| Idx | Verdict | Quote as it stands | Surface and resolution | Why |
|---|---|---|---|---|
| 0 | SUPPORTED | Immunoblotting for HIKESHI and HSPs (Fig. 1A) demonstrated a lack of detectable HIKESHI protein in HIKHOM extracts from iPSCs | XML body; Fig. 1B | Bar about 3% of control, heterozygous about 30%; the text's "lack of detectable" is stronger than the panel and the proposition's "barely detectable" matches the panel. |
| 1 | SUPPORTED | Immunoblotting quantification demonstrates a lack of detectable HIKESHI protein in HIKHOM iPSC cells | Fig. 1B-C, 1600 px webp | Four dots per genotype; control 100, heterozygous about 30, homozygous about 3; the four heat-shock proteins are ns. |
| 2 | UNVERIFIABLE | It was previously reported that the relative expression level of HIKESHI mRNA is unchanged across CON, HIKHet, and HIKHOM genotypes | XML body | The cited-report and hypothesis parts hold; "not measured here" is a negative I could not establish, because the paper runs bulk RNA-seq on these lines and does not state whether HIKESHI transcript was examined. |
| 3 | SUPPORTED | Immunoblotting found restoration of HIKESHI protein to around 20% of CON cell amount at 100 nM carfilzomib treatment for 48 h. | XML body | Described as preliminary data. |
| 4 | SUPPORTED | Preliminary data treating HIKHOM cells at 24, 48, and 72 h across concentrations from 1 nM to 10 | Suppl. Fig. 3A render; TIFF compared | HIKESHI about 23.5 at 100 nM 48 h, about 17.6 and 18.5 at 1 and 10 μM, about 10 at 24 h, about 11.5 at 72 h and 10 μM; HSP70 about 85 to 355 at 24 h; one line per time point, no error bars. |
| 5 | SUPPORTED | Therefore, this increase could be a result of the normal cell response rather than restoration of HIKESHI. | XML body | Verbatim. |
| 6 | SUPPORTED | However, carfilzomib treatment restored nuclear localization of HSP70. | XML body; Suppl. Fig. 3B | Representative images only; the Discussion says the percentage of cells "could also be analyzed". |
| 7 | SUPPORTED | Carfilzomib-treated HIKHOM cells had a significant increase in MBP+ protein compared to Vehicle-treated HIKHOM cells (Fig. 4B). | XML body; legend | Three lines, 13 to 25 images per line. |
| 8 | SUPPORTED | 30-day Carfilzomib Treatment results in improvement of physiology and myelination of HIKHOM oligodendrocytes. | Fig. 4B-C, 1600 px webp | MBP about 2.4 million (vehicle), about 16.5 million (treated), about 11 million (control vehicle), about 16.5 million (control treated); Olig2 fraction about 0.11, 0.23, 0.24. |
| 9 | SUPPORTED | 60 days of treatment from Day 30–90 appeared toxic and resulted in lack of detectable Olig2+ cells and MBP+ cells. | XML body | The neighbouring sentences cover all genotypes. |
| 10 | SUPPORTED | The 60-day marizomib treatment appeared to be less toxic than the 60-day carfilzomib treatment. | Fig. 5B-C, 1600 px webp | MBP about 8.2 million, Olig2 fraction about 0.29. |
| 11 | SUPPORTED | Proteasome inhibitors would be expected to alter levels of many proteins and specificity of these drugs to only Hikeshi rescue seems unlikely. | XML Discussion | Ubiquitination work is called future. |
| 12 | SUPPORTED | We attempted to generate isogenic iPSC to further circumvent this issue but the presence of several HIKESHI pseudogenes has thwarted specific CRISPR based targeting. | XML Discussion | Culture stress and genomic background are listed in the preceding sentences. |
| 13 | SUPPORTED | we speculate that any treatment for HAL may be most efficacious and well tolerated as a short-term intervention during febrile illness or infections | XML Discussion | The proposition drops "speculate" into "suggest"; the electron-microscopy failure is in the preceding paragraph. |

## Not established

- 42157447 entry 16: the negative (no binding, thermal-stability or folding measurement) holds in the XML text,
  legends and Methods; Figure 7 was not opened and no supplement is on disk.
- 42875792 entry 2: "mRNA not measured here" could not be established.
- 38731820 entry 7: the unchanged HRD1 and Sel1L result rests on a supplementary figure not on disk.
- 31402619 entry 3: established on the text surfaces and the supplementary captions; the supplementary
  figure images themselves were not opened.
