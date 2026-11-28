# ADV-300 blind check of records 2 and 6

legend-delegate, claude-sonnet-5-5, effort high on 3 of 3 model turns read back. Model output, hypothesis level, not medical advice; saved verbatim.

---

| Item | Verdict |
|---|---|
| H1 | NO (borderline) |
| H2 | YES |

**H1: NO**
- **Datum (line 57; Table 4, lines 60-66):** "ErbB4 JM-a | 0.7102 | <0.0001" and "ErbB4 JM-b | 0.2108 | NS (0.1029)", for correlation with WWOX mRNA. It is the paper's own result (condition 1 holds).
- **Fails conditions 2 and 3:** this is a correlation across glioblastoma tumours. It involves no WWOX loss or mutation, no PV interneurons and no developmental model.
  - It does not reverse or narrow the two stated mouse nulls.
  - It does not fill the hNPC comparison.
  - It measures no ErbB4 protein.
  - The proposed minimal measurement already names JMa.
  - Adding it would be adding human tumour background.
- **Why borderline:** a literal reading of "add a species" would admit a clause such as "in human glioblastoma, WWOX mRNA correlates with JM-a but not JM-b (correlation only)". I do not count it, because it is not a deficit measurement.
- **Evidence level:** correlation only (Spearman). No scatter plot or interval is shown.
- **Internal consistency:** the text and Table 4 agree on the coefficient (line 78). However, line 57 says "67 patients", while the printed P values fit about 61 samples. This is my approximate t-recalculation: for r = 0.2108, n = 61 gives P about 0.103 and n = 67 about 0.087. EGFR and Bax also fit 61.

**H2: YES**
- **Paper's words:**
  - Line 41: "WK and KC affected GSK3B expression in opposite directions".
  - Line 41, mean KK against WK: RT-112 2.2982 ± 0.2843 against 0.7414 ± 0.1291; HT-1376 0.7606 ± 0.0318 against 0.3938 ± 0.0148; CAL-29 0.6696 ± 0.0284 against 0.5818 ± 0.0257.
  - Line 50: "GSK3B and CTNNB1, were downregulated by WWOX" (CAGE-seq).
- **Recomputed WK/KK:** 0.32, 0.52 and 0.87.
- **Why it counts:** it is the paper's own measurement. It adds a human cell system in which WWOX gain also lowers total GSK3β. The paragraph's move from abundance to de-repression therefore cannot be read as replacing abundance.
- **Changed sentence (to follow or qualify "L'affermazione causale si sposta quindi..."):**
  > «La de-repressione (perdita di un freno fisico) non esclude però un effetto sull'abbondanza: in tre linee umane di carcinoma vescicale (RT-112, HT-1376, CAL-29) la sovraespressione di WWOX riduce anche la proteina GSK3β totale (Western, normalizzato sul controllo di carico GAPDH, triplicati; WK/KK 0,32, 0,52 e 0,87, quest'ultimo effetto modesto); pSer9 e attività chinasica non sono state misurate (PMID 35563688).»
- **Unchanged:** the statements about S9 independence and about total abundance being `NOT_ASSERTED` in Wang's system stand. This paper does not test that system.
- **Not evidence from this paper:** the Discussion sentence (line 52), "WWOX was found to repress GSK3B activity; such outcome results from direct binding", cites refs 101 and 102. It fails condition 1.
- **Evidence level:** shown data with blots, per-lane intensities, ± values and significance stars. n = 3 lanes per variant ("biological and technical triplicates", line 13). I did not find whether ± is SD or SEM. This is gain of function in cancer cells, not WWOX deficiency or neural tissue.
- **Checks against Figure 6D:**
  - Recomputing GSK3B/GAPDH from the printed lane values reproduces the WK and KK means.
  - The figure's KK-WK stars are ** (RT-112), *** (HT-1376) and * (CAL-29).
- **Caveats from those lane values:**
  - In CAL-29 the raw GSK3B band is higher in WK (mean about 3560 against 3192). The 13% fall comes entirely from the GAPDH normalisation.
  - In RT-112, GAPDH is uneven (KK lanes 1782, 4142, 4299). The raw WK/KK is about 0.58, against 0.32 normalised.
  - The text calls the opposite-direction effect "prominent in all cell lines" (line 41). For the WWOX arm in CAL-29 the paper's own numbers do not support "prominent".
- **Figure 5:** the GSK3B arrows and shading are too small to verify reliably at this resolution.

**Not assessed (not provided):** Wang's paper (PAPER 056) and CLAIM 035; the rest of CLAIM 016; the P47T, snRNA and hNPC analyses behind H1; the rest of the portfolio row; the supplements of 35563688 and GSE193659. I also did not see images or Figure files for 20535528.

Files read, all in `/home/desktop/.claude/jobs/919d2041/tmp/blind1/`: `PACKET.md`, `paper_20535528.txt`, `paper_35563688.txt`, `fig5.jpg`, `fig6.jpg`. I wrote no files and used no web tools.

