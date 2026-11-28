# Second reading: independence of the sources (blind)

Authors: PubMed esummary, one request, 2026-11-28. Files: `/home/desktop/legend-development/files/fulltext/PMID<number>*`.

| item | verdict | failing letters | largest independent set |
|---|---|---|---|
| A | FAILS | a, b, c | 1 at most; neither source has its own observation |
| B | FAILS (judgement call, see B) | a (31340538, 31543760) | 1 {32581702} |
| C | HOLDS | none | 2 {15070730, 21115974} |
| D | HOLDS | none for the passing pair; 18974271+17360458 fail b | 2 verified {19936220, 17360458 or 18974271}; 23254685 not held |
| E | UNSETTLED | 19500159 not held | 1 verified {19936220} |
| F | HOLDS | a (24456803) | 3 {34268881, 24369382, 29808465} |
| G | UNSETTLED | 17803050 not held | 1 verified {19936220} |

## Locators, shared authors, limits

**A.** a: both are reviews. c: both restate Mignot 2015 (J Med Genet 52:61), which is not a listed source and was not read. b: Aqeilan is last author of both.
- 33916893: Table 1 ("Published WOREE and SCAR12 patients"), p.Pro47Arg row, cells merged with p.Asp16fs (exon 1), cited [62] = Mignot; supplement Table 1 xlsx, rows 11-12, "Mignot et al., 2015".
- 26499798: Figure 2B patient vi (A16* / P47R); legend gives patients vi-ix to Ref. 63 = Mignot; text before Figs. 2 and 3A cites the same.

**B.** Only 32581702 observes brain development before birth.
- 32581702: Figure 2 (human fetus, 21 gestational weeks); Figure 3 and Results (lde rat; BrdU at E16.5, also P1).
- 31340538: observations at postnatal days 5, 10, 15, 21 (Figure 3 and others); embryos appear only as cited background. No prenatal observation.
- 31543760: shRNA knockdown in H9-derived neural progenitors in culture (Figures 2-10); no brain and no developmental stage in vivo.
- If that in-vitro model is accepted as an observation of the proposition, the verdict becomes HOLDS with {32581702, 31543760}. Even then, the transcriptome part of 32581702 (Figure 4) reanalyses 31543760's dataset GSE126075; only its fetal and rat data are separate.
- Shared: no shared first or last. 32581702 has as middle authors Tochigi and Suzuki H (first and last of 31340538) and Kosla and Bednarek (first and last of 31543760).

**C.**
- 15070730: "Wwox Sequesters p73 in Cytoplasm", Fig. 2; partner p73.
- 21115974: Figure 6 (WWOX-Tax interaction; block of IKKalpha recruitment to RelA and of RelA S536 phosphorylation), Figure 5; partners Tax/RelA pathway.
- Shared: Aqeilan, first of 15070730 and middle of 21115974. 21115974 cites earlier sequestration work only as background.

**D.**
- 19936220: own conditional-allele null mice; abstract and Results (death by 3-4 weeks, growth retardation, hypoglycemia, hypocalcemia, Table 3; reduced bone volume and mineralization defect).
- 17360458: Results (growth retardation, postnatal lethality, bone lesions). 18974271: abstract and Results (steroidogenesis, Leydig cell failure); its lethality and bone statement restates the group's earlier work.
- 18974271 and 17360458: same first (Aqeilan) and last (Croce); middle Hagan, Stein, Lian and others. 19936220 shares no author with them.
- 23254685 (not held): Abdeen first, Aqeilan last (first author of 18974271 and 17360458; noted). Its data and any restatement were not checked.

**E.**
- 19936220: nine 18-day null mice, necropsy, X-ray, histopathology, no neoplastic lesion; Discussion adds microCT. Own observation.
- 19500159: not held (`files/check_runs/PMID19500159.txt` is validator output with no source text). No shared first or last with 19936220.
- Secondhand only: 19936220 attributes "no osteosarcomas" in lde rats to its ref 27 = PMID 17803050, not to 19500159. 26499798 attributes "no tumor phenotype" in lde rats to Suzuki 2009 (its ref 23). Neither settles what 19500159 examined.

**F.**
- 34268881: Results and Figure EV4A (SCAR12 G372R organoids, barely any WWOX signal); WOREE organoids (splice genotype) with no detectable WWOX. Appendix Fig S6A (iPSC levels) not located or checked.
- 24369382: Figure 2B western blot, P47T patient fibroblasts, level similar to controls.
- 29808465: abstract and "Assessment of WWOX protein", patient 2 fibroblasts, protein absent with normal transcript.
- 24456803: no patient protein measurement found in the XML text (search for protein, western, expression, antibody, RNA); supplement pptx shows the variant only. Fails a.
- Shared: no shared first or last. Mahajnah is a middle author of both 34268881 and 24369382. The G372R family of 34268881 is the family reported in 24369382 (cited); the protein samples differ (24369382 blots P47T), but that family's clinical description is not new in 34268881.

**G.**
- 19936220: Table 3, BUN in null mice about two-fold higher (p = 0.01). Own measurement.
- 17803050: not held. 19936220 restates its rat BUN result (ref 27), so it is not a check of the rat half. No shared first or last (Suzuki H / Suzuki K versus Ludes-Meyers / Aldaz).
