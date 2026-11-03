# IT22 P6: qualification of "EZH2 inhibition lowers IL6/TNF in Wwox-deficient glia" (2026-11-03)

Non-canonical research material. Public edition: the WWOX-DEE reference genotype class, never an individual. **Not medical advice.** Zero spend, no registration; no e-mail address or contact string was sent to any service. No existing file edited, no receipt recorded (six receipt JSONs are prepared for the integrator, none appended). Starting point: `qualification_it21_p4a_20261103` (IT21P2-0195 GSK343, KEPT_CONDITIONAL).

## 1. Decision (first)

**Status: stays CONDITIONAL, not promoted, and its sign is not predicted. Narrowed: it is a cell-type-resolved in vitro question, not an in vivo proposal.** Nothing here qualifies the hypothesis: no step of the chain has been measured in a Wwox system.

1. **Does it survive?** Yes, as a conditional question. The counter-evidence in the IT21 record turns out weaker than worded, and a supportive in vivo datum exists (GSK343 lowered brain IL-1b, IL-2, IL-6, IL-17A in MPTP mice), but neither is a Wwox result.
2. **Weakest link.** The cell type and the sign: whether EZH2 catalytic inhibition lowers Il6/Tnf *in the glia that make them* in Wwox-null tissue. The Wwox seed is one significant Il6 reading (about 1.48-fold, n 4 v 4) and a non-significant Tnf in the null hippocampus; the Tnf/Il1b P47T cerebellum rise overlaps the wild-type range. No EZH2 or H3K27me3 measurement in any Wwox glia was found. Second weakest: brain exposure (GSK343 none measured; efflux substrate).
3. **Does the OPC-maturation biology reverse the sign?** It does not reverse the cytokine sign; it **reverses the sign of the net benefit on the myelin axis**. EZH2/PRC2 is needed for oligodendrocyte differentiation (Ezh2 loss delays it, Ezh1 compensates; Ezh1+Ezh2 loss blocks it and is lethal in mice; mechanism Notch/Wnt de-repression). The IT14 line is a differentiation block on a Wnt-restraint question (candidate C5). An EZH2 inhibitor, especially a dual EZH1/EZH2 one, would be expected to add to that block, so any cytokine gain would have to be weighed against it. This is an inference from a developmental mouse knockout, not a drug result and not a Wwox result.

## 2. What was read (depth stated; `reading_depth` is also in the receipts)

| PMID | Paper | Depth | Used for |
|---|---|---|---|
| 29132376 | Yin 2017, J Neuroinflammation | partial full text (text sections; figures, legends, additional files not served) | the edge reference: inhibitor, cell types, sign |
| 37391829 | Mannino 2023, J Neuroinflammation | partial full text (same limits; effect sizes in figures not read) | GSK343 in vivo cytokines, exposure gap |
| 32937136 | Wang 2020, Cell Rep | partial full text (figures, key resources, supplement not served; italics stripped in the served text) | PRC2 in OL differentiation |
| 25868794, 35300079, 37228094 | Int J Cancer 2015; ACS Med Chem Lett 2022; JNCI 2023 | abstract | efflux and brain-penetration statements; paediatric tazemetostat |
| 31202798, 35568718, 40209863, 27449082, 22808153, 28041882, 22821416, 41097006 | various | abstract/metadata only, named as such | context only |

No "complete" read is claimed: the PubMed full-text tool returned article text without figure images or supplements, and the text was not snapshotted to `files/`, so the 13 full-text locators (`locators_ezh2_glia_it22_p6.tsv`, L1-L13) were quoted from the served text and cannot be machine-matched against a local artefact (stated in each receipt; `source_kind` is `fulltext_remote`).

## 3. The two lines of biology

**A. Cytokine line (the hypothesis).**
* Seeds (Q5; correction note IT10 read): only Il6 is significant in the null hippocampus; Tnf is a non-significant rise there; Tnf/Il1b >=2-fold in P47T cerebellum (transcript). The hypothesis therefore rests on Il6 in one tissue and a TNF rise that is not statistically supported in the null.
* PMID 29132376 (read), the edge reference IT21 cited as "EZH2 inhibition elevated IL1b/IL6 in glioblastoma cells and TNF/iNOS in murine microglia". Correct reading: the tools were **DZNep and siEZH2, not GSK343** (L1); IL1B and IL6 rose **in the tumour cells** (L2); in **microglia IL1B and IL6 did not change** and TNF and iNOS rose when microglia sat with medium from EZH2-suppressed tumour cells (L3); TNF was undetectable in the tumour cells (L4). So it is an indirect, non-microglial, non-GSK343 contrast. It does not show that direct EZH2 inhibition raises microglial IL6, but it also shows that conditioning by EZH2-inhibited neighbours can raise a TNF signal: a cross-talk route the single-cell-type test below must separate.
* PMID 37391829 (read): GSK343 i.p. 1/5/10 mg/kg for 7 days lowered whole-brain ELISA IL-1b, IL-2, IL-6, IL-17A in MPTP-injured adult male mice (L6, L7); uninjured-animal cytokines not shown (L8); brain exposure not measured (L5). Supports a lowering in injury inflammation, says nothing about cell type, development or Wwox.
* Others (abstracts only): DZNep lowers microglial IL-6/TNF in stroke (31202798); EPZ6438 changes spinal microglial NLRP3 via Timp1 (40209863); Ezh2 licenses inflammasomes independently of its methyltransferase activity (35568718), a reason a catalytic inhibitor may not mimic knockdown.

**B. Oligodendrocyte-lineage line (could alter the sign).** Wang 2020 (read): Ezh2 loss delays OL generation without changing OPCs and recovers by P10 (L9); H3K27me3 recovers by P3 with Ezh1 up; dual PRC2 loss (Eed) gives no OL recovery by P10 and dysmyelination with death at P13-P17 (L10, L13, same section); PRC2 represses Notch and Wnt genes, and Notch or Wnt inhibition rescues Mbp expression in the Eed-null OL lineage (L11); the authors conclude the therapeutic direction is boosting PRC2 for remyelination (L12). Abstracts agree in direction: Ezh2 sustains neural stem cell and oligodendrocyte phenotype (22808153), Suz12/lncOL1 drives maturation (28041882), Ezh2 loss gives no change in zebrafish OPC markers (41097006, whole-mount, abstract). Link to LEGEND: the IT14 package restricts the myelin line to a role-resolving question, lists WNT restraint as a held candidate, and finds the myelin deficit secondary to neurons in vivo. A de-repressed Wnt signal from EZH2 inhibition is the opposite of that held candidate. **Not shown:** that a catalytic inhibitor at glial-active doses delays OL maturation in Wwox-deficient tissue; that postnatal EZH1 compensation would cover a selective EZH2 inhibitor (it would, by the mouse data, unless the compound also reaches EZH1: GSK343 EZH1 IC50 240 nM v cell H3K27 IC50 174 nM, so the window is narrow in cells).

## 4. Class alternatives (measured, typed values only)

`class_alternatives_ezh2_ezh1.tsv` is the raw output of `generation_it22_p1_20261103/class_alternatives_it22.py --targets EZH2,EZH1` (catalogue cache as instructed; 21 rows). Types are never pooled or converted. Main facts: all measured rows are IC50 or Ki; **IC50 EZH1 v EZH2 (same type)**: GSK343 240 v 4 nM (60x EZH2-selective); valemetostat 16 v 5.1 (3.1x); zeprumetostat 19.1 v 4 (4.8x); tulmimetostat 0.06 v 0.02 (3.0x). GSK126, tazemetostat, mevrometostat, EPZ011989 and others have no EZH1 row, so selectivity is "not comparable". EZH2 IC50 values (4, 9.9, 11 nM for GSK343, GSK126, tazemetostat) come from separate depositions with unstated assay conditions, so no potency ranking is claimed; mevrometostat is a Ki (<0.1 nM) and is not ranked against IC50 rows. **No toxicity or "less toxic" statement is made for any compound**: the only toxicity rows are the single GSK343 fetal NSC viability value (9 uM, 48 h) and an uninjured-mouse statement without data (L8). **GSK2816126 is GSK126 and EPZ-6438 is tazemetostat (aliases, counted once).**

Exposure summary: GSK343 none measured; GSK126 Abcb1/Abcg2 restricted, 0.2% oral bioavailability in WT mice (abstract); tazemetostat P-gp-only restriction, elacridar abrogates (abstract), children with CNS tumours were treated (abstract) without CNS exposure data in it; mevrometostat and the dual members nothing; TDI-6118 is stated brain penetrant (abstract), outside the catalogue and unread. **On-target toxicity:** only genetic data read (Wang 2020, above); clinical class liabilities were not verified from a label here.

## 5. Final table per compound (kept separate: novelty, evidence strength, WWOX relevance, feasibility)

| Compound | Novelty for LEGEND | Evidence strength | WWOX relevance | Feasibility |
|---|---|---|---|---|
| GSK343 | not new as molecule or relation (IT9 excluded, IT21 KEPT_CONDITIONAL); context narrowed to cell-type-resolved mouse glia | hypothesis only; mouse injury model (read) v indirect DZNep co-culture (read) | low (no Wwox datum on EZH2) | in vitro high; in vivo low (no exposure, efflux) |
| GSK126 (= GSK2816126) | same substance under two names; second chemotype for the experiment | as GSK343, no extra | low | in vitro high; in vivo low (0.2% oral F, WT mice) |
| tazemetostat (= EPZ-6438) | approved molecule; question new, class not | hypothesis only; oncology human data are not WWOX evidence | low | in vitro high; clinical use not assessable here |
| mevrometostat | new to this thread | none for this question | none | unknown |
| valemetostat, tulmimetostat, zeprumetostat (dual) | hazard flag only | genetic (mouse) only | n/a (would add to the IT14 block) | not recommended |
| other class members | not new | none | none | low |

## 6. Missing data and what could not be verified (consolidated)

No EZH2 or H3K27me3 reading in any Wwox-deficient glia (searched records, not exhaustive). No brain exposure for GSK343, mevrometostat or the dual members; no tissue-to-plasma number was read for any compound. Figures, effect sizes and n per group of PMID 37391829, and the figure data of 29132376 and 32937136, were not read. Tazemetostat label, class second-malignancy risk, paediatric tolerability (full text of 37228094), approval flags of valemetostat and zeprumetostat, and the clinical stage of mevrometostat are unverified here. Catalogue assay classes are mostly "unknown". The Ezh1 compensation finding is from developing mouse spinal cord and chick; transfer to postnatal brain glia in Wwox deficiency is an inference. PubMed searches use the tool's term mapping, which silently dropped conditions in some queries (e.g. zero-hit compound queries), so absence of a hit is not absence of a paper.

## 7. Files

`qualification_ezh2_glia_it22_p6.tsv` (one row per compound or group, all requested fields), `class_alternatives_ezh2_ezh1.tsv` (raw tool output), `locators_ezh2_glia_it22_p6.tsv` (13 full-text and 5 abstract-level verbatim quotes), `receipts/` (5 files: 3 partial full text, 2 abstract-only; event IDs `FTR-20261103-<pmid>-02`; the 25868794 abstract already has `-01` from IT21 P4a; each passed `fulltext_receipts.py record --dry-run`), `make_ezh2_glia_p6_it22.py` (locators and receipts), `build_table_ezh2_glia_p6_it22.py` (table).
