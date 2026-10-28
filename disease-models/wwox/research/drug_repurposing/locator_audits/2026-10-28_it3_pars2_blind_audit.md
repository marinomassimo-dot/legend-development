# Blind locator audit: Xu 2026 (fly PARS2 deficiency, ISR), PMID 41380592 (PMC12754399)

Auditor: scientist-d (did not produce the reading). Date: 2026-10-28. Read-only toward canonical files.

Blindness: verdicts and the independent answers (Part A, B, C) were written from the source
artefacts before the reading notes (`isr_pars2_reading_it3_20261027.md`,
`complex_i_ldh_pdh_it3_20261027.md`, the receipt notes) were opened. Part D (comparison) was added
afterwards. Triples came from `deepdive_manifests/PMID41380592.json` (49 entries: 30 body, 19
figure/supplement-image). Note: the shared brief `it3_common.md` named in the task was not present
at the given scratchpad path; the audit used the skill text only.

Source surfaces used (sha256 prefixes matched the manifest): JATS XML `5c7fffb1f44fd45d`; images
`files/figures/PMID41380592_r2/gr1..gr9.jpg`; `files/supplement/PMID41380592_r2/extracted/S1..S9.png`.
Body quotes were string-matched against the XML text (all 30 found verbatim, including the
Discussion, Methods, license and COI sentences; whitespace-normalised).

Scope: all 30 body locators, and ALL 19 figure/supplement locators (not a sample); every image
was opened and plot values read by eye from JPEG/PNG renderings (no vector data). Readings carry a
visual uncertainty of about +/-3 percentage points on bar heights read from 0-100 axes, about
+/-5 on the 0-200 and 0-300 axes, and +/-0.3 day on the pupariation curves, unless stated.

## Part A. Verdicts, body locators (index = manifest `entries[i]`)

Verdict vocabulary: SUPPORTED, OVERSHOOT, UNDERSHOOT, NOT_IN_SOURCE, UNVERIFIABLE_SURFACE.
"Quote carries half" means the proposition has a second clause that the quoted sentence does not
contain, but the adjacent source text does; that is a quote-scope note, not an error.

| # | Verdict | Proposition (short) | What the source supports |
|---|---|---|---|
| 0 | SUPPORTED | GCN2 RNAi "largely" suppresses delay; Fig 6H still lags | Quote verbatim. The "still lags" clause is not in the sentence; it is the figure (see 31). |
| 1 | SUPPORTED | GCN2 RNAi reduces bang sensitivity and recovery time | Verbatim, "largely reduced or suppressed". |
| 2 | SUPPORTED | Authors attribute both phenotypes to the GCN2 branch | Verbatim causal sentence. The causal word is the authors'; the data are one RNAi line, partial knockdown (S7), no second line. |
| 3 | SUPPORTED | ATF4 knockdown "largely" rescues delay and seizure; qPCR in S8 | Verbatim; S8 citation is in the next sentence. |
| 4 | SUPPORTED | P-GCN2 up, P-PERK not, total GCN2 unchanged | Quote carries the first two; total GCN2 is the next sentence. |
| 5 | SUPPORTED | P-eIF2a up, puromycin down in the head | Quote carries half (P-eIF2a); puromycin sentences follow ("remarkably reduced"). |
| 6 | SUPPORTED | ISR target list annotated manually from a mouse study | Verbatim, ref [27]. Fig 5E legend calls the list "prespecified"; the text says "manually annotated". |
| 7 | SUPPORTED | Ldh transcript and protein up; no activity/lactate/pyruvate/flux | Verbatim. Absence claim checked: "lactate" occurs once, in the enzyme name; "pyruvate", "flux", "PDH", "PDK" occur zero times; the only respiration word is "respiratory chain activity". |
| 8 | SUPPORTED | ATF4-to-Ldh step borrowed from S2-cell ER-stress study; Ldh not measured after ATF4/GCN2 knockdown | Verbatim ref [48]. I read every Results sentence of the ATF4 and GCN2 subsections: Ldh appears only in the Fig 7A-C sentences. |
| 9 | SUPPORTED | OXPHOS subunit protein reductions by complex; ATP5A not reduced | Quote carries MT-ND1 and MT-CO2; NDUFS1/3, SDHB, UQCRFS1 and ATP5A are in the next sentences. |
| 10 | SUPPORTED (figure caveat) | Complex I activity is by in-gel stain, reduced in heads and larvae | Text states the decrease for heads and larvae verbatim; Methods show only NBT gel staining, no respiration/NADH-oxidation assay. Caveat: in my reading of Fig 4A the head bands for CII and CIV look nearly equal and CI only subtly weaker; the text is stronger than the head image (see 39). |
| 11 | SUPPORTED | CI assay = native gel + NADH + NBT | Verbatim, Methods. |
| 12 | SUPPORTED | Authors hypothesise ISR rather than mitochondrial defect drives disease; mito readouts not re-measured after GCN2/ATF4 suppression | Verbatim, Discussion. The absence is true of the Results (no OXPHOS, TEM or activity readout in either suppression arm). |
| 13 | SUPPORTED | "ISR detrimental" on GCN2 inhibition (paired with ATF4) | Verbatim; the ATF4 half is the later sentences of the paragraph. |
| 14 | SUPPORTED | Route from mt-tRNA defect to GCN2 unknown; tRNA export, ROS, protease; OMA1-DELE1-HRI | Verbatim plus the surrounding paragraph. The paragraph also cites halofuginone (cytoplasmic ProRS inhibitor) as precedent; not tested here. |
| 15 | SUPPORTED | Mechanism ISR-to-seizure not determined; ATF4 a clue | Verbatim. |
| 16 | SUPPORTED | Not complete phenocopies | Verbatim. |
| 17 | SUPPORTED | Therapy statement prospective; no compound tested | Verbatim; also "ISR inhibition may have broader therapeutic potential". No compound was tested (Q2). |
| 18 | SUPPORTED | RNAi stock identifiers | Verbatim: GCN2 BDSC 35355, ATF4 THFC THU5856 (dPARS2 RNAi is VDRC 330525). |
| 19 | SUPPORTED | Seizure age 5-7 d (Results); sex not stated | Verbatim. Sex is not named in the bang-sensitivity paragraph or the Results. |
| 20 | SUPPORTED | Methods 4-6 d, no sex | Verbatim; conflicts with Results 5-7 d as stated. |
| 21 | SUPPORTED | 5 s maximum-speed vortex; readouts fraction and righting time | Verbatim; the readouts are the next two Methods sentences. |
| 22 | OVERSHOOT (wording, minor) | "The only sex named anywhere is for the RNA-seq heads (5-day-old females)" | Quote verbatim. But sex is also named in the genetics Methods ("eclosed virgin female F1 progeny", "male F2/F3/F4 progeny") and in the S1C/F cross diagrams. True and unaffected for the experimental animals' assay readouts; the sentence should read "the only sex named for any assayed flies". |
| 23 | SUPPORTED | Fisher's exact test for seizure proportions; 3 vials of 10 | Verbatim; the "3 vials of 10" comes from the legends (N = 3, n = 10). Multi-group tests are one-way ANOVA with Tamhane's test, not Fisher (see Part B). |
| 24 | SUPPORTED | GFP-transgene titration control exists for the dPARS2 rescue; none stated for GCN2/ATF4 arms | Verbatim. No Results sentence reports an equivalent control for the double arms. See Part B for the S4 point. |
| 25 | SUPPORTED | Human V95I HEK293T: P-eIF2a, puromycin, ATF4, P-GCN2 up, P-PERK unchanged | Quote carries P-GCN2/P-PERK; the rest in the same subsection. HEK293T is "human embryonic kidney". |
| 26 | SUPPORTED (uncertainty declared) | Single homozygous clone, low-efficiency knock-in | Verbatim ("the single cell derived clone"). Uncertainty: the same paragraph earlier says "generated cell lines homozygous" (plural) and Methods "PARS2V95I/V95I HEK293T cell lines"; the number of clones used for the blots is not stated beyond "the single cell derived clone". |
| 27 | SUPPORTED | Complex I reduced, II not obviously altered in V95I cells, unlike fly | Quote carries the complex II half ("no effect on the activity of complex II"); complex I/IV reduced is the Results (Fig 8G) and the next Discussion sentence. The proposition's wording "not obviously altered" matches Results; the Discussion's "no effect" is stronger. |
| 28 | SUPPORTED | CC BY-NC | Verbatim. |
| 29 | SUPPORTED | No COI; funding public | COI verbatim. Funding (National Key R&D Program of China; NSFC 32170559) is in Acknowledgments, not in the quote. |

Body counts: SUPPORTED 29 (two carry a declared caveat: 10 and 26), OVERSHOOT 1 (entry 22,
wording), UNDERSHOOT 0, NOT_IN_SOURCE 0.
Every body quote was found verbatim.

## Part A2. Figure and supplement-image locators (all 19)

These are attestations of pixel readings, so by the skill's rule the verdict is declared
UNVERIFIABLE_SURFACE; the next column is my own independent reading and whether it agrees.

| # | Verdict | Manifest value | My reading (uncertainty) | Agreement |
|---|---|---|---|---|
| 30 | UNVERIFIABLE_SURFACE | Fig 6J-K: bang ~0 / 87 / 30 / 4; recovery ~100 vs ~10 s | 6J: 0 / 87 / 30 (three points tight at 30) / 4; 6K means ~98 vs ~10; 30 flies per bar (+/-3, +/-5 s) | AGREE |
| 31 | UNVERIFIABLE_SURFACE | Fig 6H-I: double 33% day 5, 95% day 6; dPARS2 alone 2 at d6, 75 at d7; eclosion near control by d10-11 | 6H: day 5 control ~62, double ~33, dPARS2 0; day 6 double ~95, dPARS2 ~2; day 7 dPARS2 ~75, 100 by day 8. 6I: day 9 double ~20 vs control ~45, day 10 double ~93 vs 100; dPARS2 alone ~42 at d11. GCN2 RNAi alone overlaps control. (+/-3, +/-0.3 d) | AGREE |
| 32 | UNVERIFIABLE_SURFACE | Fig 6C-F: P-eIF2a 100/140/109/55; puromycin 100/28/60 | 6D: 100 / 140 / 109 / ~57 (GCN2 RNAi alone has a wide spread, 40-72); 6F: 100 / 29 / 60; N = 3 per bar. No comparison mark between GCN2-alone and control | AGREE |
| 33 | UNVERIFIABLE_SURFACE | Fig 6A-B: P-GCN2 ~155 vs 100; key inverted; P-PERK and total GCN2 unchanged; N 3-4 | 6B: key assigns solid orange to dPARS2RNAi and hatched to Ctrl; the solid-orange bar is ~100 and the hatched bar ~155 (so read literally, Ctrl is higher). The key in 6D has the reverse assignment (Ctrl solid). Gel 6A lane order is Ctrl, dPARS2RNAi. P-GCN2 N = 3 points, GCN2 and P-PERK N = 4 | AGREE; inversion confirmed. I cannot decide from the panel alone which bar is which genotype: the text resolves it (an error in the key, or in the bar order, cannot be told apart) |
| 34 | UNVERIFIABLE_SURFACE | Fig 7D-H: bang 93 / 46 (30-62) / 10 / 0; recovery 100 vs 15; pupariation double ~0 d5, ~100 d6 | 7G: 93 / ~46 (three vials ~30, ~42, ~62) / ~10 / 0; 7H: ~100 vs ~15; 7E: day 5 control ~63, double ~1, ATF4 RNAi alone ~90; day 6 double ~100, dPARS2 alone ~0; day 7 dPARS2 alone ~82. 7F eclosion: double ~60 at d10, ~98 at d11 | AGREE; the source also shows ATF4 RNAi alone pupariating earlier than control (~90 vs ~63 at day 5), which the manifest omits |
| 35 | UNVERIFIABLE_SURFACE | Fig 7A-C: Ldh + 14 glycolytic transcripts up; protein ~1030% N = 3 | 7A lists 15 genes: Ldh, CG2767, Pfk, Hex-A, Pgi, Gapdh2, CG31075, Pglym78, Aldh7A1, Tpi, Eno, Ald1, Pgm1, Pgm2a, Pgk (Ldh + 14). 7C: ~1030 (error bar ~1000-1180), 3 points; one band in control faint | AGREE |
| 36 | UNVERIFIABLE_SURFACE | Fig 5A-E | 5B ~142 (4 points); 5D ~21 (3 points); heatmap gene lists exactly as given (19 up incl. crc, 8 down); 3 libraries per genotype; crc is lighter in the third dPARS2 replicate but Padj ***. Both "Ldh" and "ldh" rows present | AGREE |
| 37 | UNVERIFIABLE_SURFACE | Fig 1: KO larval lethal; neuronal delay 1-2 d; bang ~90 vs 0 vs ~3; recovery ~110 s | Fig 1A KO arrests as larva at day 10; 1G control 100% by day 6, dPARS2 ~78% day 7, ~100% day 9; 1H eclosion control ~99 by day 10, dPARS2 ~45 day 11, ~90 by day 13; 1J: ~90 / 0 / ~3; 1K: ~108, n = 30 | AGREE. Wording: the third arm "dPARS2RNAi/+" is the UAS-only (no driver) control, not "heterozygous-like" |
| 38 | UNVERIFIABLE_SURFACE | Fig 2 and 3 values | 2C: MT-ND1 ~74, MT-CO2 ~65; 2E: NDUFS1 ~62, NDUFS3 ~65, SDHB ~78, UQCRFS1 ~50, ATP5A ~89 (ns); 3B: CI ~52, CII ~70, CIII ~43, CIV ~58, CV ~61. Ns of 3-5 | AGREE. Source nuance: ATP5A subunit abundance is not reduced (Fig 2E) while assembled complex V is reduced (3B) |
| 39 | UNVERIFIABLE_SURFACE | Fig 4: head in-gel bands only modestly weaker; larval clearly weaker; TEM ~93 vs ~12, n 14 / 23 | Head gels: CI band modestly weaker at best, CII and CIV look near-equal (I would call these "no visible difference" at this resolution); larval gels clearly weaker for CI, II, IV; 4D ~93 vs ~12, dots ~14 and ~23 | AGREE with a caveat: for CII and CIV in heads, my reading is weaker than "modestly weaker". No quantification plotted for 4A-B |
| 40 | UNVERIFIABLE_SURFACE | Fig 8 values | 8D PARS2 ~58; 8F MT-CO2 ~32, MT-ATP8 ~78, NDUFS1 ~59, NDUFS3 ~80, UQCRFS1 ~44, ATP5A ~100 (ns); 8I ~172; 8M ~163; 8O ~158; 8K ~8; 8Q ns (~100). 8G CI band weaker, CII similar, CIV weaker. Also 8B: V95I exogenous ~72, E203K and S279L ~5 | AGREE |
| 41 | UNVERIFIABLE_SURFACE | Fig 9 is a cartoon, no data | Cartoon confirmed; it also draws a TCA cycle with crossed arrows in the dPARS2-deficient mitochondrion, which no panel measures | AGREE |
| 42 | UNVERIFIABLE_SURFACE | S4: bang 97 vs 100; recovery 135 vs 130; pupariation/eclosion overlap | S4D ~96 vs 100 (ns); S4E ~135 vs ~130 (ns); S4B-C overlap | AGREE |
| 43 | UNVERIFIABLE_SURFACE | S7 / S8 knockdown values | S7: 48 / 43 / 63; S8: 58 / 59 / 73; measured in elav>RNAi single lines, normalised control = 100 with near-zero variance | AGREE |
| 44 | UNVERIFIABLE_SURFACE | S2: 20 / 30; S1D-E ~15 / ~9 | S2: ~20 (larva), ~30 (pupa); S1D ~16, S1E ~9 | AGREE |
| 45 | UNVERIFIABLE_SURFACE | S3: dPARS2 transgene rescue, bang ~3% | S3G ~3 (rescue), CDS alone ~7; Da-GAL4 pupariation rescue is slightly delayed on day 5 (~30 vs 62) and complete by day 6; elav rescue near complete | AGREE. "establishes ... not an off-target effect" is the authors' inference ("confirm the specificity"); a single RNAi line plus a transgene rescue supports it, but is not a second independent RNAi |
| 46 | UNVERIFIABLE_SURFACE | S5: three unchanged, UQCRFS1 ~148 | NDUFS1 ~91, NDUFS3 ~102, SDHB ~97 (all ns); UQCRFS1 ~148 (***) | AGREE |
| 47 | UNVERIFIABLE_SURFACE | S6 KEGG lists | Up: glycine/serine/threonine, carbon metabolism, alanine/aspartate/glutamate, lysosome, fructose/mannose, galactose, ECM-receptor, biosynthesis of amino acids, glycolysis/gluconeogenesis, DNA replication; down: longevity regulating pathway, neuroactive ligand-receptor. No pyruvate/PDH/PDK/TCA term | AGREE (the manifest lists a subset of the up terms, which is not an error) |
| 48 | UNVERIFIABLE_SURFACE | S9 Sanger c.283G>A homozygous | Trace labelled c.283G>A (p.Val95Ile); the mutant read shows A with no overlapping peak (consistent with homozygous) and an additional C>G change at the first shown base, not described in the text | AGREE. Extra change is unreported in the text (probably a PAM or blocking edit from the ssODN); unresolved from the image |

Figure counts: 19 of 19 audited by reading; verdict UNVERIFIABLE_SURFACE (declared) for all 19;
agreement with my own reading 19 of 19; 2 carry a caveat on interpretation (33 key inversion, 39
head gels) and 3 a source-says-more or wording note that changes no value (34, 37, 48). No value disagreed beyond the
stated uncertainty.

## Part A3. Verdict totals

| Verdict | Count |
|---|---|
| SUPPORTED | 29 (body) |
| OVERSHOOT | 1 (body, entry 22, wording only) |
| UNDERSHOOT | 0 |
| NOT_IN_SOURCE | 0 |
| UNVERIFIABLE_SURFACE (declared attestation) | 19 (figure/supplement), all agreeing with my reading |

Error versus uncertainty: the only error found is the entry-22 wording. Uncertainties are
(a) 26: one clone or several, (b) 33: which bar belongs to which genotype in the panel, (c) 39:
how much weaker the head in-gel CII/CIV bands are, (d) 48: the extra base.

## Part B. Independent answers from the source

### Q1. The GCN2 RNAi and ATF4 RNAi rescue experiments

- Design. Double knockdown in the nervous system: elav-GAL4 driving UAS-dPARS2 RNAi (VDRC 330525) together with UAS-GCN2 RNAi (BDSC 35355) or UAS-ATF4 RNAi (THFC THU5856). Arms: Ctrl, dPARS2 RNAi, dPARS2 RNAi + GCN2 (or ATF4) RNAi, GCN2 (or ATF4) RNAi alone. The Ctrl genotype is not defined in the text (a driver-only or a w1118 cross is not said). 25 C, 12:12.
- Knockdown efficiency. qRT-PCR in the single-RNAi lines under elav (S7, S8): GCN2 mRNA 48% (larva), 43% (pupa), 63% (adult) of control; ATF4 58, 59, 73%. Not measured in the double lines; ATF4 protein not measured in fly.
- GCN2 readouts (Fig 6). P-eIF2a in heads (6C-D, N = 3): 100 / 140 / 109 / ~57 (Ctrl / dPARS2 / double / GCN2 alone); puromycin incorporation (6E-F, N = 3): 100 / 29 / 60. Pupariation (6H, N = 3, n = 28-30): double ~33% day 5 and ~95% day 6; dPARS2 alone 0 day 5, ~2% day 6, ~75% day 7. Eclosion (6I): double ~93% by day 10, dPARS2 alone ~42% day 11. Bang sensitivity (6J, N = 3 vials of 10 flies): 0 / 87 / 30 / 4%. Recovery time (6K, n = 30 flies): ~98 s dPARS2 alone, ~10 s double.
- ATF4 readouts (Fig 7D-H). Pupariation (7E, N = 3, n = 28-30): double ~0% day 5, ~100% day 6, dPARS2 alone 0 at day 6 and ~82% day 7; ATF4 RNAi alone ~90% at day 5 (faster than control ~63%). Eclosion (7F): double ~60% at day 10, ~98% day 11. Bang (7G): 0 / 93 / ~46 (vials ~30-62) / ~10%. Recovery (7H): ~100 s vs ~15 s. No P-eIF2a, puromycin, Ldh or mitochondrial readout in the ATF4 arm.
- Controls absent or untested. No mitochondrial readout (OXPHOS, TEM, in-gel) after either suppression. No second RNAi line for either gene. No statistics reported for the double versus control comparison (the residual ~30-46% bang sensitivity versus 0% is not tested). The GFP-transgene titration control (S4) is reported only for the dPARS2 transgene rescue; it has two UAS constructs and is the relevant analogue for the double arms, but the authors do not cite it for them.
- Statistics. Fisher's exact for seizure proportions; one-way ANOVA with Tamhane for multi-group comparisons (t, Welch or Mann-Whitney for two groups); Shapiro-Wilk for normality. Marks: 6D * and **, 6F * and ***, 6J and 6K ****, 7G **** and ***, 7H ****. No marks on the pupariation or eclosion curves.
- Age and sex. Seizure assay: 5-7 d (Results) or 4-6 d (Methods); no sex stated anywhere for the bang, pupariation or western experiments. RNA-seq heads are 5-day-old females only.
- Reading: partial genetic rescue of the dPARS2 developmental delay (about one day left) and of seizure, in a neuronal RNAi model, with partial knockdowns; the authors' wording is "largely".

### Q2. Compound / ISR pharmacology

None tested. No drug, no ISR inhibitor (ISRIB, a PERK or GCN2 inhibitor) and no integrated-stress compound appears in the text (zero hits for ISRIB or "drug"; "inhibitor" occurs only for protease/phosphatase inhibitors and generic "translation inhibitors"). Puromycin (600 uM fed for 24 h; 0.5 ug/mL for 15 min in cells) is an assay reagent. Halofuginone is cited as a literature precedent (induces GCN2-mediated ISR via uncharged tRNAPro [49]). Therapeutic statements are prospective ("can be used to ... screen potential therapeutic agents"; "ISR inhibition may have broader therapeutic potential").

### Q3. Ldh or WWOX content

WWOX: none (zero occurrences). Ldh: Fig 7A shows Ldh among 15 glycolytic transcripts raised in dPARS2-deficient heads (Fig 5E heatmap also lists Ldh/ldh); Fig 7B-C shows Ldh protein ~10-fold by western with one anti-LDH antibody (N = 3). The text reads this as ATF4 activation, citing an S2-cell ER-stress precedent. No Ldh activity, lactate, pyruvate, NAD+/NADH ratio, PDH/PDK or flux measurement; no Ldh readout after ATF4 or GCN2 knockdown; the KEGG terms (S6) have no pyruvate-metabolism term.

## Part D. Comparison with the reading notes (written after the verdicts)

Compared against `isr_pars2_reading_it3_20261027.md` and `complex_i_ldh_pdh_it3_20261027.md`. The
notes' numbers (87 to 30, 93 to 46 with vials 30-62, 100 to 10 and 100 to 15 s, 140 to 109,
puromycin ~60, Ldh ~10-fold, knockdown losses 37-57% GCN2 and 27-42% ATF4, 49 locators = 30 + 19)
all reproduce from the source. Disagreements and gaps, none of which changes a conclusion:

1. Head in-gel activity. Notes say "in-gel activity stains lower (qualitative for heads)". My
   reading of Fig 4A is that CII and CIV head bands show little or no visible difference and CI
   is subtly weaker; only the larval gels are clearly lower. The text asserts a decrease in
   heads; the notes follow the text. Suggest wording "head in-gel difference is faint and
   unquantified". Bearing on the complex I note: "a complex I-reduced ... fly neuron model" is
   supported by subunit protein (MT-ND1 ~74, NDUFS1 ~62, NDUFS3 ~65) and BN-PAGE (CI ~52), not by
   the head activity stain.
2. Control genotype. The notes list "control 0 percent" without saying the Ctrl cross is not
   defined in the text; I record it as a gap (the controls cannot be reconstructed from the paper).
3. Statistics. The notes give "Fisher exact" for the arms. That covers the bang proportions
   only; P-eIF2a/puromycin/other multi-group comparisons use one-way ANOVA with Tamhane; the
   pupariation and eclosion curves carry no test at all, and the double-versus-control residual
   (30% and 46% bang-sensitive versus 0%) is untested.
4. GFP titration control. The notes say it "exists only for the dPARS2 transgene rescue (S4)".
   Correct as far as the authors cite it. I add that S4 is structurally the relevant control for
   the double arms (two UAS constructs) and its result (97 vs 100% bang, overlapping curves)
   would be the dilution reference, so the gap is "not cited", not "not run in a comparable
   configuration".
5. ATF4 RNAi alone pupariates earlier than control (~90 vs ~63% at day 5; Fig 7E). The notes list
   only "ATF4 RNAi alone about 10 percent" bang. Not mentioned in the notes; it bears on reading
   the double arm as a clean rescue.
6. Human clone number. The notes say "single clone". The text says both "cell lines" and "the
   single cell derived clone"; I keep it as uncertain, not as an error.
7. Sex. The notes say "sex not stated" for the assays, which is correct. The manifest entry 22
   ("the only sex named anywhere") overstates: crosses name female and male parents.
8. Manifest wording, entry 37: the "RNAi/+" arm is the UAS-only control, not "heterozygous-like".
9. Not checked by me (outside the 49 triples): the note's statements on the reference list (60
   references, no WWOX; WWOX zero hits in the body text is confirmed), the Retraction Watch
   snapshot, and the WWOX-side facts in the notes' last paragraph (fly Atf4 and amyloid, organoid
   ISR targets). Confirmed negatives: no lifespan, climbing or EEG measurement in the text (zero
   hits), no PERK perturbation.

Disposition: nothing here blocks the reading from touching canonical state (no NOT_IN_SOURCE, no
UNDERSHOOT). One wording fix (entry 22) and the head in-gel softening (point 1) are the
proportionate answers before any BATCH_COMMIT; the rest are additions the reader may take or
argue.
