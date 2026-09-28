> Persisted verbatim by the Orchestrator's dispatch of 2026-09-27 (BATCH_20260927_004 wave-2 blind audit round). The auditor was **blind**: it received only the `(proposition, quote, anchor)` triples of the packets below, the source artefacts under `files/fulltext/`, and the current text of the target claims — no candidate, no dossier, no reader identity, no conclusions. Packets covered: CC-20260826-GSK3B-S9-AXIS-01, CC-20260922-TAU-DIRECTION-01.

# Blind locator audit — auditor C

Sources consulted: `files/fulltext/PMID32000863_Cheng2020_PMC.xml`, `files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png`, `files/fulltext/PMID22193544_Wang2012_PMC.xml`.

## CC-20260826-GSK3B-S9-AXIS-01.triples.md

| # | Proposition (short) | Verdict | Reason |
|---|---|---|---|
| 1 | Fig. 7c densitometry carries no statistic (one lane/genotype/region, no error bars, no n, no significance marker, "representative" legend) | SUPPORTED | Quote verbatim in the Fig. 7 legend, panel c. Panel image confirms 9 single lanes (3 regions × +/+, +/−, −/−) with one densitometry number per lane, no error bars, no n, no asterisks; the legend's `means ± SEM`, `n.s.` and `*** P < 0.001` belong to panel d. |
| 2 | Stated evidence is activation via Ser9 dephosphorylation, not abundance | SUPPORTED | Quote verbatim ("…as evidenced by dephosphorylation of GSK3β at Ser9"). Note: the same legend adds "the ratio of phosphorylated **or total** GSK3β to β-actin", and the panel does print total-GSK3β numbers (2.2–2.6, visually flat) — the source shows a bit more than the proposition, without contradicting it. |
| 3 | Abstract states activation, not abundance | SUPPORTED | Verbatim in the Abstract: "We determined that a significantly increased activation of glycogen synthase kinase 3β (GSK3β) occurs in Wwox−/− mouse cerebral cortex, hippocampus and cerebellum." |
| 4 | Lithium = panel 7d, ethosuximide = panel 7b, distinct experiments | SUPPORTED | Quote verbatim for d; legend panel b reads "Pretreatment of ethosuximide (ETS, 150 mg/kg) suppressed PTZ-induced seizure activity in Wwox−/− mice." Different drugs, doses and N per panel in the figure. |
| 5 | Ethosuximide's genotype specificity stated in running text | SUPPORTED | Verbatim in Results, seizure/GSK-3β section, including the "…although ethosuximide pretreatment had no effects on the behavior changes in Wwox+/+ and Wwox+/− mice treated with a low dose of PTZ." clause. |
| 6 | Methods date the western tissue to postnatal day 14 | SUPPORTED | Verbatim in Methods, "Western blotting". Note: that paragraph names only "anti-WWOX, anti-DCX (GeneTex), and anti-β-actin (Sigma) antibodies" — no GSK3β antibody appears anywhere in Methods — so the paragraph's link to the Fig. 7c blot is not stated by the source. |
| 7 | Fig. 7c legend dates the same blot to P20, so the age is not settled | SUPPORTED | Legend quote verbatim; P14 (Methods) vs P20 (Fig. 7c legend) discrepancy is real at text level. Note only: "the same blot" is the auditor-visible inference, since the Methods antibody list does not cover GSK3β (see #6). |
| 8 | In Wang 2012 the only reported invariance is p-Ser9 and phospho-β-catenin; total GSK3β abundance is never reported | OVERSHOOT | Running-text quote is verbatim ("We found that the phosphorylation levels of phospho-GSK3β S9 and phospho-β-catenin remained normal."), but the negative half is contradicted by the Figure 1 legend: "Western blots were conducted to measure the levels of pTau S404, pTau S422, pTauS396, Tau, WWOX, cyclin D1, phospho-GSK3β S9, **GSK3β**, β-catenin, phospho-β-catenin and actin. (c) Western blot results of Figure 2b were quantified by scanning the autoradiogram using a densitometer." Total GSK3β is blotted and densitometered; only its *narrative* invariance is absent (the panel values themselves are a figure surface). |
| 9 | The conserved GSK3β-docking motif is contained in WWOX388−412 | SUPPORTED | Verbatim in Results/Fig. 2a. Note: the same sentence gives two regions — "WWOX296−320 **and** WWOX388−412 contain FXXXLI/VXRLE" — so the source names one more motif-bearing interval than the proposition does; the proposition claims no exclusivity. |
| 10 | The interval required for the interaction is WWOX 388–407, a different interval | SUPPORTED | Verbatim: "This indicates that WWOX amino acids 388–407 are required for its interaction with GSK3β." Corroborated downstream: "…interacts with GSK3β in vitro through the L404-containing motif within the WWOX388−407 region." |
| 11 | The microtubule-assembly limb is measured cell-free, purified tubulin in a cuvette | SUPPORTED | Verbatim in Methods, "Microtubule assembly assay"; the continuation ("GSK3β was pre-incubated with Tau in the presence of WWOX…, polymerisation was then initiated by the addition…") confirms a purified, cell-free system. |

Counts: SUPPORTED 10 · OVERSHOOT 1 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 0 (11 triples).

## CC-20260922-TAU-DIRECTION-01.triples.md

| # | Proposition (short) | Verdict | Reason |
|---|---|---|---|
| 1 | Tau-mediated microtubule assembly restored by WT WWOX, not by WWOX L404A | SUPPORTED | Quote verbatim in Results (Fig. 5e), and the source's own next sentence agrees: "our data demonstrated that WWOX could restore the ability of Tau to promote microtubule formation by inhibiting GSK3β activity." Note: restoration is partial ("the new equilibrium reached a higher turbidity"), not to baseline. |
| 2 | That measurement is cell-free: purified tubulin in a cuvette read by turbidity | SUPPORTED | Verbatim in Methods, "Microtubule assembly assay"; no cell appears in the assay description. |
| 3 | Tau is the effector of both WWOX and GSK3β on neurite outgrowth; removing Tau removes both benefits | SUPPORTED | Verbatim in Results (Fig. 6a–b): "Neither WWOX overexpression nor GSK3β knockdown promoted neurite outgrowth in the Tau knockdown condition, indicating that Tau is the effector of both WWOX and GSK3β". |
| 4 | RA-stimulated neurite outgrowth itself depends on Tau | SUPPORTED | Verbatim in the same section: "Figures 6a and b (lanes 1–3) show that the neurite outgrowth stimulated by RA was abolished when Tau was knocked down." |

Counts: SUPPORTED 4 · OVERSHOOT 0 · UNDERSHOOT 0 · NOT_IN_SOURCE 0 · UNVERIFIABLE_SURFACE 0 (4 triples).
