# Locator audit, the narrowed entries with zero auditors (blind, 2026-10-24)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and ledger. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` and judged against the native artefacts under `files/`. Nothing was repaired.

## Scope

Every entry carrying `contradicts_locator` with zero auditors — in these five manifests no entry carries an `audit` block at all, so the condition reduces to "carries `contradicts_locator`". The set was enumerated from the manifests themselves, not from any note about them.

| PMID | Entries in scope | Count |
|---|---|---|
| 36779245 (Oliver) | 38 to 46 | 9 |
| 30361190 (Shaukat) | 14, 15, 17, 18, 19 | 5 |
| 24456803 (Abdel-Salam) | 11 | 1 |
| 30362252 (Davids) | 5 to 9 | 5 |
| 42397075 (Steinberg) | 2, 4, 6, 13 | 4 |
| Total judged | | 24 |

Separately, entries 15 and 21 to 29 of 42397075 (ten entries) carry `artifact_status` ABSENT_ON_HOST and no `contradicts_locator`. They were not re-judged; the declaration itself was tested (see below).

## Artefact checks

`locator_audit.py --pmid` over the five manifests: every in-scope quote occurs in its declared artefact (36779245 42/42 text, 30361190 21/21, 24456803 11/12 — the one miss is entry 1, out of scope, 30362252 7/7, 42397075 28/28).

All image reads returned real images. 36779245 Figure 4A was read from the native 709x226 JPEG, panel A calibrated on the 0.00/0.25/0.50/0.75/1.00 ticks (33.5 px per 0.25) and the 0/5/10/15/20/25-year ticks (11.9 px per year). 42397075 Figure 2F was read from `fig2F_600dpi.png` (2448x1584) with the axis ticks at -3/-2/-1/0/1 giving 152.75 px per log2 unit and zero at x = 1244; Figure 2D/E from the 1217x776 embedded raster; Figure 4C from the 1430x749 raster, ticks -0.4/0.0/0.4/0.8 at 199 px per unit; Figure 5F from the 1430x795 raster, ticks 0.0/0.5/1.0 at 216 px per unit. No read returned "media removed" or a non-image.

One counter-check matters for 30362252. Its two "figure" files on disk, `files/figures/PMID30362252_r2/nihms-994754-f0001.jpg` and `-f0002.jpg`, are HTML documents, not JPEGs — a download that saved an error page. The host therefore does **not** hold the figure images of that paper, which is what entry 5 states.

## Counts

| PMID | Judged | SUPPORTED | Adverse (OVERSHOOT or UNDERSHOOT) | UNVERIFIABLE | Anchor-level only |
|---|---|---|---|---|---|
| 36779245 | 9 | 9 | 0 | 0 | 0 |
| 30361190 | 5 | 5 | 0 | 0 | 1 |
| 24456803 | 1 | 1 | 0 | 0 | 0 |
| 30362252 | 5 | 5 | 0 | 0 | 0 |
| 42397075 | 4 | 3 | 1 | 0 | 0 |
| Total | 24 | 23 | 1 | 0 | 1 |

Adverse rate: 1 of 24 judged triples (4.2 percent). Mode: exhaustive over the declared scope (every `contradicts_locator` entry with zero auditors in the five manifests); adverse = OVERSHOOT or UNDERSHOOT; no triple was UNVERIFIABLE, so the denominator is the whole judged set. Counting the one anchor-level defect as well: 2 of 24 (8.3 percent).

The ten ABSENT_ON_HOST entries of 42397075 are outside this denominator and remain UNVERIFIABLE on the host.

## Adverse triples

| Manifest | Entry | Verdict | Reason |
|---|---|---|---|
| 42397075 | 2 | OVERSHOOT (scope) | The headline "the central phenotype is almost entirely in the engineered knockout, not in the patient lines" is general; the quote and Figure 2D-F carry composition only, and the same paper's Figure 5F shows both patient lines inverting the early/late neuronal balance against wild type (measured 0.333 WT, 0.662 WOREE, 0.681 SCAR12 early). Every numeral in the quote is exact (see below); it is the unqualified first sentence, not the figures, that exceeds the source. |

Anchor-level only (the proposition is supported by the quote; the printed location is wrong):

| Manifest | Entry | Reason |
|---|---|---|
| 30361190 | 18 | "and epileptic spasms were captured. Vigabatrin was" sits in the **left column of page 404** (the page whose footer follows it), not "page 403 left column to page 404". The same entry points at entry 19 for the outcome, but the sentence continues at the top of the right column — "added with a partial response" — which is not entry 19's quote. |

## Notes on triples judged SUPPORTED

- 36779245 entry 38: Figure 4A reproduces at the ticks. Blue null/missense 1.00 to about 2.7 y then 0.90 flat to about 12 y with censoring marks; green missense/missense 0.75 from about 3.3 y and 0.62 from about 8.3 y to about 24 y (measured 0.62 at x = 8.6 y and 15.4 y); red null/null 0.46 at about 3.1 y, 0.34 at about 6.8 y and 0.26 from about 9 y to about 12.3 y. One three-group log-rank p = 0.0085 is printed and no pairwise test. The band overlap holds: at 15.4 y the missense/missense ribbon runs down to about 0.37 and the null/null ribbon up to about 0.58 at 7.8 y, so the two bands overlap over roughly 0.37 to 0.58.
- 36779245 entries 40 to 44: the thirteen cells of the Table 2 row "ASMs trialed (current)" parse as quoted, Patient 5's cell (VPA, LEV) standing between Patient 4's and Patient 6's. Patients 6 and 7 carry fourteen entries each. Recounted independently from the row: the patients listing at least one of PHT/CBZ/OXC/LTG/LAC/ZNS/ESM are 1, 2, 4, 6, 7, 9, 11, 13 (eight) and, dropping lamotrigine-only, 1, 2, 4, 6, 7, 9, 11 (seven); Patients 3, 5, 8, 10, 12 list none. Vigabatrin appears in the cells of Patients 1, 3, 6, 7, 8, 10, 11, 13 (eight).
- 36779245 entry 39: the quoted sentence is verbatim and reports no per-drug or per-class response. Qualification recorded, not scored adverse: the same paragraph reports drug-level **retention** ("Only 1 of 3 individuals who started the ketogenic diet continued it. In contrast, all four patients who had cannabidiol continued that ASM") and Table 2 carries a per-patient "Drug-resistant" row; neither is a response by drug or class, and neither touches a sodium-channel blocker.
- 36779245 entry 43: "no sodium-channel-blocking drug" for Patient 5 rests on a class assignment the entry declares as the reader's; valproic acid's own sodium-channel action is the usual edge of that assignment, and the entry is explicit that the paper assigns no class.
- 36779245 entry 45: "Vigabatrin was used in 7 of 10 patients for the treatment of ES" is verbatim. The Table 2 seizure-type row gives ES at onset in Patients 1, 2, 3, 4, 7, 8, 10, 11, 12, 13 (ten, matching "10 of 13" in the body); of those, seven carry vigabatrin (1, 3, 7, 8, 10, 11, 13). The eighth vigabatrin cell is Patient 6, who has no ES at onset. Sentence and table agree.
- 36779245 entry 46: the STXBP1 sentence with the 30 percent burst-suppression figure is verbatim in the differential-diagnosis paragraph of the Discussion.
- 30361190 entries 14, 15, 17, 19: each quote is a verbatim fragment and each anchor resolves. The first child's list (page 403, right column) is lactate, ammonia, acylcarnitine, uric acid, homocysteine, plasma amino acids, urine organic acids, transferrin isoforms — blood and urine chemistry throughout, as entry 15 reads it. The second child's list (page 405, left column) ends "and urine sulfocystine" and carries no transferrin isoforms; it opens with echocardiogram, which entry 17 does not claim otherwise. Entry 19's continuation names sodium valproate, clobazam and phenobarbital and the right hemispasms in clusters, all on page 404 right column.
- 24456803 entry 11: the quoted list is verbatim in the first paragraph of the Results section, in the clinical description of II:4, and it does name ammonia, serum lactate, amino and organic acids and very long chain fatty acids.
- 30362252 entries 5 to 9: all five quotes are verbatim. "spectroscop" and "lactate" occur once each in the whole XML, both inside entry 5's sentence, and the two figure legends (Figure 1 genetic analysis, Figure 2 expression) do not mention MRS; the figure images are not held (see above). "vigabatrin" and "sodium channel" occur zero times in the paper. Gestational diabetes is in the same paragraph as entry 8's laboratory sentence (no paragraph break between them). The HSPG2 attribution follows entry 6's sentence inside the same paragraph. One anchor remark, not scored: this XML carries no body section titles at all, so entry 6's "Results" and entry 9's "Discussion" are the reader's labels for two consecutive interpretive paragraphs; both anchors resolve by their positional wording.
- 42397075 entry 2: every numeral in the attestation is exact at 600 dpi. Measured on panel F: WWOX-KO RGs +0.995 and Neu -2.383; SCAR12 RGs -0.275 and Neu +0.190; WOREE RGs +0.079 and Neu -0.065. Panel D cell counts read 5649, 3020, 3422, 5916. Panel E neuronal fractions read about 0.43, 0.08, 0.58, 0.44. The composition reading is sound; only the generalising headline is adverse.
- 42397075 entry 4: panel F measured 0.333 / 0.662 / 0.681 early for WT / WOREE / SCAR12, panel G early positive and late negative in both patient lines, n = 9094 printed on panel B. Qualification recorded, not scored adverse: panel F's own title is "organoid composition", so the composition-versus-maturation separation is the reader's framing of two different measurements, not the paper's wording.
- 42397075 entry 6: Figure 4C measured S +0.766, G2M +0.510, G1/G0 -0.294, M -0.389, with no error bars and no significance markers. Figure 4D: S strongly red and M strongly blue in the WWOX-KO column, all four WT cells near zero with G1/G0 the only faintly positive one. Figure 4A: the two densities run together over the bulk of the pseudotime axis and separate only on the steep flanks at 0 and 2 pi, where the WT trace sits above the KO trace; "near-superimposed" is a fair description of the panel. The panel-A legend prints n = 2396 KO and n = 2152 WT.
- 42397075 entry 13: the quoted line is verbatim in the Results, and the sentence it opens ends "approach." on the next line; the paragraph does offer the absence of radial-glia effects (Supplementary Fig. 10C-F) as the safety profile of the AAV9-WWOX approach.
- 42397075 ABSENT_ON_HOST declaration: **truthful**. The fourteen Aqeilan-asset SHA-256 digests this manifest declares were hashed against every file under `files/`, `Downloads` and `.claude` — zero matches. `files/fulltext/PMID42397075_Aqeilan2026_assets/` holds only `figs/`, whose six rasters are byte-identical to the Steinberg main-article figures; none of the ten cited supplement paths exists, and no file named `brain-2025-03809-File009/010.pdf` exists anywhere on the host (the only `File009.pdf` hits belong to PMID 33914858's supplement, `brain-2020-02464`). Entries 15 and 21 to 29 remain UNVERIFIABLE until the supplementary-figures volume is re-acquired.
