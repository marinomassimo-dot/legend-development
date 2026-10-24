# Locator audit, the R1 repairs of 2026-10-22 (blind, 2026-10-24)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and
ledger. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` and
judged against the native artefacts under `files/`. The authors' notes, the task records and the
reasoning of the earlier audit were not read. Nothing was repaired.

## Scope

The 21 entries that carry `contradicts_locator` citing `locator_audit_R1_20261022.md` — the audit
that condemned the entry — across the six manifests below. Each was rewritten in response to that
condemnation and has never been judged in its present wording. The scope is exhaustive: every
`contradicts_locator` entry in these six manifests cites R1, and all 21 were judged.

| PMID | Entries in scope |
|---|---|
| 31402619 (Abbink, VWM / eIF2B) | 1, 2, 3 |
| 32023956 (Lukas, GLA / DGJ amenability) | 4, 5, 7, 12 |
| 38378758 (Clausen, Parkin VAMP-seq) | 1, 2, 4, 7, 13, 15 |
| 38731820 (Poliquin, Gabrg2 Q390X / ZNS) | 3, 10, 17 |
| 42157447 (De Leeuw, SLC6A1 / GAT-1) | 8, 16, 17, 18 |
| 42875792 (Rathan Kumar, HIKESHI) | 2 |

## Image reads

All image reads returned real images; none was a placeholder and none had to be retried through a
second surface. `paper_packet.py rank` reports no publisher PDF on disk for 32023956, 38731820 or
42157447, so each figure was read from the native JPEG with Lanczos upscaling, values taken against
the printed axis ticks. 32023956 Figure 1 is the 731 x 1511 raster; the panel-B statistics box is
printed text and was read directly. 38378758 Figure 3 is the 700 x 365 raster, panels A to C read
with the inset that the panel itself carries; its supplement PDF holds higher-resolution copies of
other figures but none of Figure 3. 38731820 Figures 3 and 6 are the 783 x 344 and 771 x 599
rasters; Figure 3D-F calibrated on 0.0 / 0.5 / 1.0 and Figure 6C-E on their own ticks. 42157447
figure files are numbered independently of the figure labels — the JATS `<fig>` graphics map
Figure 5 to `ACN3-9999-0-g004.jpg` and Figure 1 to `g005.jpg` — so the mapping was taken from the
JATS and not from the filename; Figure 5F and 5G were calibrated on 0 / 1 / 2 / 3 / 4 and
0 / 2 / 4 / 6.

## Counts

| PMID | Judged | SUPPORTED | Adverse (OVERSHOOT or UNDERSHOOT) | UNVERIFIABLE | Anchor-level only |
|---|---|---|---|---|---|
| 31402619 | 3 | 3 | 0 | 0 | 0 |
| 32023956 | 4 | 4 | 0 | 0 | 0 |
| 38378758 | 6 | 6 | 0 | 0 | 0 |
| 38731820 | 3 | 3 | 0 | 0 | 0 |
| 42157447 | 4 | 4 | 0 | 0 | 0 |
| 42875792 | 1 | 1 | 0 | 0 | 0 |
| Total | 21 | 21 | 0 | 0 | 0 |

Adverse rate: 0 of 21 judged triples (0.0 percent). Mode: exhaustive over the declared scope —
every `contradicts_locator` entry citing R1 in the six manifests; adverse = OVERSHOOT or UNDERSHOOT;
no triple was excluded from the denominator.

## Adverse triples

None.

## Quote-occurrence note

`locator_audit.py --pmid 31402619` reports entry 2's quote as NOT FOUND. The quote is verbatim in
its declared artefact: `files/supplement/PMID31402619/ACN3-6-1407-s009.docx`, Supplementary
Materials and Methods, Sample preparation — "triturated three times with a 23G needle and
centrifuged for 10min at 4°C to remove nuclei, membranes and debris". The tool does not read
`.docx`, so this is a reader limitation of the check, not a defect of the locator. The five other
manifests report every text quote matched.

## Notes on the triples judged SUPPORTED

- **31402619 entry 1.** Results paragraph 1 gives "differential distribution between the monosome
  and polysome fractions ... for 33 mRNAs"; paragraph 2 gives "176 mRNAs with altered level of
  polysome association ... indicating altered synthesis of the encoded proteins" (115 up, 61 down).
  The proposition's separation of the two regimes is the paper's own.
- **31402619 entry 2.** The supplementary section states no g-force, and no form of
  soluble/insoluble or pellet retention appears anywhere in it, so the restraint is accurate. The
  section heading says "Tissue lysates" generically; the body fixes the tissue as forebrain
  ("polysomal profiling with forebrains of 4-month-old WT and 2b5ho mice"), so the proposition's
  "forebrain lysate" is not a stretch.
- **31402619 entry 3.** The quote is verbatim in Discussion paragraph 6. The absence claim holds:
  no eIF2B protein-level or solubility measurement appears in the body, in the ten supplementary
  figure captions (S1 to S10), in the supplementary methods, or in the Data S1 primer-and-antibody
  workbook — the only `EIF2B` strings in the workbooks are patient genotypes in s006. The
  read-outs the proposition does list all exist: eIF2alpha phosphorylation (Figure S2 raw Western
  blot data), 4E-BP1, myelin markers by Western blot (Figure S9), and "Protein synthesis rates were
  measured in mouse astrocytes" in the supplementary methods.
- **32023956 entry 4.** The panel box reads exactly as the proposition states: Pearson r 0.8771,
  95 percent confidence interval 0.8381 to 0.9071, R squared 0.7692. The body gives r = 0.9448 for
  Figure 1B. The arithmetic settles it independently: panels A and C are internally consistent
  (0.8729 against R squared 0.7620; 0.7992 against 0.6388), while 0.9448 squared is 0.8927, not
  the 0.7692 the same sentence reports for this panel, and the square root of 0.7692 is 0.8771.
  The text value is the outlier, as the entry says.
- **32023956 entries 5, 7, 12.** All three quotes are verbatim. The Results 2.3 paragraph continues
  "These variants may be benign with an uncertain clinical significance", which is what entry 7
  attributes; 8 of 23 is a third, and the paper claims no majority. Entry 5's "3% threshold" is
  generalised to "the absolute activity threshold" without loss. "Shire" occurs once in the whole
  article, in the Conflicts of Interest, with no statement of what that company makes.
- **38378758 entries 1, 2, 7, 13, 15.** Every quote is verbatim and every hedge is the source's own
  ("likely", "suggests"). Entry 2's Discussion attribution is confirmed: "in addition to the
  unfolding of the UBL domain, induced by R42P". Entry 7's scope is confirmed by the methods and
  the Figure 3F legend — 10 micromolar BIO-2007817 for 24 hours, a pooled flow histogram of the
  library (untreated 407,000 cells, treated 426,000), no per-variant sequencing read — and the
  concession "might only stabilize variants localized to the region or domain where the compound
  binds" is in the same paragraph. Entry 13's counts (28 of 63, at solvent-exposed positions with
  predicted delta-delta-G below 1 kcal/mol) are the paper's, and no sentence anywhere in the
  article says a folding chaperone would fail on them — the only chaperone sentence is the
  therapeutic one quoted in entry 15. Entry 15's panel attributions check out against the body:
  bortezomib 3A, siPSMD14 3B, 29 degrees 3E.
- **38378758 entry 4.** Figure 3A: the untreated grey peak reaches about 28k and the bortezomib red
  peak about 21k, with the legend's 559,000 against 436,000 cells. The panel's own inset shows grey
  above red across the low-ratio shoulder and red above grey in a narrow bump at the foot of the
  main peak — a rightward shift, as the entry says, not a lift of the shoulder as a whole. Figure
  3C: the two chloroquine traces coincide, matching the quoted sentence.
- **38731820 entry 3.** Every figure in the proposition is verbatim in Results 2.3: gamma2 0.572
  against 0.474 with p = 0.106 and still below wild type; alpha1 0.998 against 0.747 with p = 0.033
  and indistinguishable from wild type; beta2 0.934, not different from wild type (p = 0.978), the
  rise over untreated Q390X failing at p = 0.088.
- **38731820 entry 10.** The legend quote is verbatim. Figure 6C draws six animals in six colours at
  baseline — about 37, 20.7, 13, 12, 10 and 0.8 seizures — whose mean is 15.58 and whose standard
  error is about 5.0; the body reports 15.58 plus or minus 4.987. The figure is therefore n = 6 and
  the legend's "N = 3 female" is the outlier, as the entry says. Methods 4.6 reads "male and female
  Gabrg2+/Q390X mice were surgically implanted".
- **38731820 entry 17.** The Discussion quote is verbatim and is offered as a possibility ("may
  offset"). Figure 3D-F read against the ticks: gamma2 pcDNA about 0.47 against HRD1 about 0.29;
  alpha1 about 0.75 against about 0.50; beta2 about 0.67 against about 0.41 — HRD1 co-expression
  lowers surface expression of all three subunits, so the surface data do run against the
  hypothesis. No current or mIPSC read-out occurs anywhere in the article; the only "current" string
  is "the current study".
- **42157447 entry 8.** The quote is verbatim. Figure 5F butyrate: WT about 2.1, S295L about 2.8,
  V511M about 2.2, A288V about 1.05 and ns — "rose in wild type, S295L and V511M but not A288V"
  holds. The 7 to 18 percent uptake range is the paper's own sentence ("a modest increase ranging
  from 7.4%–17.8% relative to untreated across all 32 variants"). Figure 5G S295L: vehicle about
  0.88, butyrate about 2.78; the entry's "about 2.7-fold" matches the bar's value rather than the
  fold change, which measures about 3.1 — a conservative reading inside a clause whose office is to
  limit the proposition, so the entry is not overstated by it.
- **42157447 entry 16.** The quote is verbatim in Discussion 4.3. The restraint is warranted: no
  supplement is cited in the article and none is on disk for this PMID, and the article carries no
  thermal-stability, melting or binding assay of any kind. Figure 7, which the entry declares
  unopened, carries chaperone over-expression and Bix treatment — GABA uptake and Western blot, per
  its legend and its body paragraph — so it holds no such measurement and would not have changed
  the entry either way.
- **42157447 entry 17.** The quote is verbatim and carries function only. Figure 5F salubrinal,
  against the ticks: WT about 2.1, A288V about 0.6, S295L about 0.5, V511M about 0.9. The body and
  the Figure 5F legend both report salubrinal as significantly increasing total protein in WT,
  A288V and S295L, so the panel does run against the text for the two variants, as the entry says.
- **42157447 entry 18.** The quote is verbatim, and the Figure 7E legend's own p values carry the
  pattern the entry describes: wild type ns at 1, 2.5 and 5 micromolar then significant at 10 and
  20 (a threshold), S295L significant at 1 and 2.5, ns at 5, significant at 10 and 20
  (non-monotonic), while the body calls the effect dose-dependent. The entry files that pattern as
  a panel reading when the legend in fact states it in words — an understatement of what the source
  carries, not of what the proposition claims.
- **42875792 entry 2.** The quote is verbatim. The next sentence is the attribution the entry
  describes ("suggests the V54L mutation results in protein instability and may result in rapid
  degradation, possibly by the ubiquitin-mediated proteasome"), followed by "To test this
  hypothesis, we treated the cells with proteasome inhibitors". The paper does run its own bulk
  RNA-Seq across oligodendrocyte differentiation, and that section reports differentially expressed
  genes, gene-ontology pathways and SOX10 but never HIKESHI's own transcript level — so "NOT
  STATED" is exact.
