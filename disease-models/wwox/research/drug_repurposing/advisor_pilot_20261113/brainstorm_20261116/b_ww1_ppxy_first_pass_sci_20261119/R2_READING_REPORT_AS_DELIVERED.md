# R2 report (producer, SCI, 2026-11-19; hypothesis level; not medical advice; reference genotype class: WWOX loss of function in DEE)

Tool calls used: about 40 of 100. A Write of R2_REPORT.md was not attempted; the full report is in this message. Scratch copies of the fetched texts are in /tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/r2/dl/ (not repository files).

## 0. Reading depth and routes (read this first)
Depth key: FT-text = complete text of Methods, Results, tables and legends, but figure images not viewed. SUMM = complete page given to a fast summariser (WebFetch), so figures and tables are not verbatim, and the last ~32k characters of PMC3979411 and ~2-5k of the other pages were not covered. ABS = abstract only.

| Paper | PMID | Route | Depth |
|---|---|---|---|
| Ludes-Meyers 2004 (PPXY ligand) | 15064722 | held .txt in files/fulltext | FT-text, to Fig 4 results |
| Schuchardt 2013 | 24308844 | held PMC XML | FT-text, Tables 1-5 read |
| Rotem-Bamberger 2022 | 35716775 | the held file is MISSING from files/fulltext (no PMID35716775 or PMC9293652 name). Acquired by NCBI efetch db=pmc (PMC9293652) | FT-text, Tables 1-4 read |
| Aldaz 2014 review | 24932569 | not opened (brief: locating only) | not read |
| Aqeilan 2005 (WWOX/YAP/ErbB4) | 16061658 | not in PMC; publisher page returned HTTP 403, stopped | ABS only |
| Abu-Odeh 2014 JBC | 24550385 | Europe PMC XML gave HTTP 500; NCBI efetch "publisher does not allow XML"; PMC page via WebFetch | SUMM (two prompts) |
| Hussain 2018 TAP-MS | 30619736 | held Europe PMC XML | FT-text; Supplementary Files 1-3 (216-protein list) not available |
| Hussain 2023 P47T | 36828035 | held PMC XML; grepped only for the pull-down and PPxY passages | partial text |
| Pressey 2017 | 28235805 | efetch blocked; PMC page via WebFetch | SUMM, page complete |
| Mennesson 2019 | 30770891 | efetch blocked; PMC page via WebFetch | SUMM, ~5k chars unread |
| Mennesson 2020 | 32788298 | NCBI efetch PMC7470932 | FT-text, searched for WWOX/PPxY/ErbB4 terms and Discussion; Results not read line by line (abstract numbers used) |
| Saigo 2018 (PMID 30214895; a REVIEW, not primary) | 30214895 | NCBI efetch PMC6125347 | FT-text of the main body; relevant part read |
| Liang 2021 (angiomotin, viral PPxY) | 33536174 | efetch blocked; the WebFetch summariser refused the page (policy refusal, not retried) | ABS only |
| Aqeilan 2004 (AP-2gamma) | 15548692 | not in PMC | ABS only |
| Aqeilan 2007 (ErbB4, breast cancer) | 17909041 | not in PMC | ABS only (treated as unread) |

Correction to the brief: the held file `PMID25331887_AbuOdeh2014*` is the 2014 PNAS paper on ATM and ITCH, not the JBC WW-domain paper. The JBC paper is PMID 24550385 (PMC3979411). "Schuchardt 2013 (PMID not guaranteed)" and "the held PMID 24308844" are the same paper. "Rotem-Bamberger 2022" is PMID 35716775.

Neural-context searches (PubMed): "WWOX P47T knock-in mouse" gave 1 hit (Hussain 2023). "Wwox[Title] AND (ErbB4 OR Neto2 OR KCC2) AND (neuron OR brain OR interneuron)" gave 1 hit (Kosla 2011, glioblastoma specimens; abstract only, not a neuron study). "WWOX WW domain interacting protein neurons synapse PPxY co-immunoprecipitation brain" gave 0. Stopped there. No original on WWOX and ErbB4, NETO2 or KCC2 in neurons was found.

## (a) Interaction table
Columns: partner | motif / WW domain | assay (direct or proposed) | species, cell, tissue, age | neural? | functional consequence (endpoint, size, n) | lever named in the original | depth | locator.

1. ErbB4 ICD PY1/PY2/PY3 (PY3 = GTVLPPPPYRHRN) | PPxY; WW1 binds, WW2 alone does not | DIRECT, peptides with recombinant human WWOX domains: ITC, 25 C, pH 7. Kd WW1: PY1 383, PY2 362, PY3 144 uM (>=3 runs); WW1-WW2 tandem: 170, 175, 68 uM; WW2 Y85W: 680, 620, 54 uM; Ala scan of PY3: P0, P+1 and Y+3 give no binding (>1 mM). Rotem-Bamberger (ITC, NMR): tandem PY3 30 uM, WW1 PY3 78 uM, WW2 PY3 >>200 uM; dual-motif PY3PY3 3 uM; NMR Kd(WW1) PY3 10 uM | E. coli proteins, synthetic 12-13-mer peptides, no cells | no | binding affinity only (no cellular endpoint) | none; Schuchardt notes that WW domain engineering (Y85W) is relevant to therapy, a design remark, not a compound | FT-text (24308844; 35716775) | Schuchardt Tables 1-4; R-B Tables 2-4
2. ErbB4 (full length and CTF) | WW1 (abstract: first WW domain) | PROPOSED-to-DIRECT: Aqeilan 2005 abstract reports physical association via WW1 in HeLa; Abu-Odeh (SUMM) used ErbB4 as the positive control for GST-WW1 pull-down | human HeLa, MCF-7 | no (cancer lines) | per Aqeilan 2005 abstract: ErbB-4 retained in cytoplasm after TPA; suppresses YAP coactivation of CTF dose-dependently; a WWOX mutant lacking ErbB-4 binding has no effect (sizes and n not seen) | TPA (PKC-driven ICD cleavage; stimulus, not therapy) | ABS (16061658) plus SUMM | abstract; Schuchardt Introduction (secondary)
3. ErbB4 isoforms JM-a CYT-1/CYT-2 and membrane ErbB4 accumulation | not read | associated in vitro; Wwox raises full-length membrane ErbB4 | COS cells, breast cancer series | no | breast cancer, n = 556; Wwox-ErbB4 membranous co-expression correlates with outcome | none | ABS only (17909041) | abstract
4. SIMPLE | two PPSY motifs; WW1 | DIRECT: far-Western on a human-brain-cDNA protein array (bacterial His fusions), GST pull-down with PPXY mutants, endogenous SIMPLE pulled down from MCF-7 | human proteins in E. coli; MCF-7 | the array source is brain cDNA but binding was in vitro; not a neural observation | partial Golgi colocalisation (MCF-7); no functional endpoint | none | FT-text | Ludes-Meyers Figs 2-4, Table 1
5. WBP-1 (+ NF-kB-activating protein clone, COTE1, one unidentified clone) | PPXY (gtpPPPYtv in WBP-1); WW1 | WBP-1 DIRECT (peptide array and pull-down with PPXY mutants); the other three CONFIRMED by far-Western only, motif mutants not tested | as row 4 | no | none | none | FT-text | Ludes-Meyers Figs 1-3
6. DVL1, DVL2, WBP2, AMOT, AMOTL1, ITCH (LPxY), p73 | PPxY and LPxY; WW1; WW1 mutant WFPA (W44F/P47A-type) | GST-WW1 pull-down + MS in HEK293 (240 proteins WW1 not WFPA; 144 in stricter set; PPXY about 20% of hits vs about 5% proteome, 4.2-fold); phage display 2,733 unique peptides, extended (L/P)PxY. Validated: DVL1 (GST pull-down, Y553A mutant), AMOT and AMOTL1 (pull-down, PPEA mutant, endogenous IP), ITCH (LPXY mutants Y623A/Y839A reduce binding; endogenous IP). WBP2 and p73 were MS hits only, not validated here | human HEK293 | no | ITCH K63-ubiquitinates WWOX (mainly K274), WWOX nuclear and cell death increased (SUMM, sizes not given) | MG-132 (20 uM), cycloheximide, cisplatin (25 uM) used as assay tools | SUMM | Abu-Odeh Results, Figs 1-4
7. DVL2, WBP2, SEC23IP, VOPP1, AMOT, DVL1, SCAMP3, others (216 hits) | candidate PPxY/LPxY/PPxF motifs by PROSITE in 31% (67/216) | TAP-MS of full-length SFB-WWOX; DIRECT only for SEC23IP, SCAMP3, VOPP1: reciprocal co-IP; SEC23IP and SCAMP3 lost with GST-WW1 W44F/P47A, kept with WW2 Y85A/P88A. The rest PROPOSED. Overlap with the GST-WW1 dataset is 16 proteins | human HEK293T | no | none measured | none | FT-text; supplements not available | Hussain 2018 Table 1, Figs 3-4, Table 2
8. Dvl2 (HPYSPQPPPYHELSSY) and Wbp1 (SGSGGTPPPPYTVG) peptides | PPPY; Wwox WW1 | DIRECT, in vitro peptide pull-down: wild-type cerebellar lysate binds, P47T/P47T lysate does not | mouse cerebellum (n = 2 per genotype, either sex; age not extracted) | YES for tissue source (cerebellum), not for cell type | P47T abolishes PPxY-peptide affinity; the knock-in mice have reduced survival and hyperactivity (as quoted in the figure legend) | none | partial text | Hussain 2023 Fig 1a, Methods
9. TMEM207, VOPP1, WBP1 as endogenous competitors | PPxY; WW1 | review of primary work (PLA, yeast two-hybrid, co-IP); not primary here | cancer cells | no | proposed inhibition of WWOX tumour-suppressor function | none | FT-text of a review | Saigo 2018
10. Viral VP40 and LASV Z PPxY; AMOT competition | PPxY | GST-WW array hit; per abstract WWOX lowers VLP egress | human cells, viral proteins | no | per abstract only | none | ABS | Liang 2021
11. NETO2 | none identified | no WWOX binding reported. In Pressey, NETO2-KCC2 interaction via CUB domains, cited to an earlier paper | mouse hippocampal culture (P0-1 pups, transfection at DIV 8-10) | yes, but no WWOX | see (b) Q3 | PMA 200 nM (PKC activation, used to study GluK2 phosphorylation) | SUMM | Pressey Fig 3

## (b) Answers

Q1 Direct versus proposed. Direct with a defined domain, motif and species and measured affinity: WWOX WW1 with ErbB4 PY1/PY2/PY3 peptides (rows 1; human WWOX domains, ITC and NMR, weak-to-moderate affinity, 3-380 uM). WW2 alone does not bind single PPxY (Kd >> 200 uM); it stabilises WW1 and contributes when a peptide carries two PPxY motifs (R-B Tables 2-3). Direct by pull-down with motif mutants: SIMPLE and WBP-1 (row 4-5), DVL1, AMOT/AMOTL1 and ITCH (row 6), SEC23IP, SCAMP3 and VOPP1 (row 7). Direct for a mouse tissue lysate with peptides: Dvl2 and Wbp1 peptides (row 8). Only proposed or MS-level: most TAP-MS and GST-MS hits (about 69% of the 216 TAP-MS proteins contain no candidate WW1 motif at all, row 7), p73 and WBP2 in the Abu-Odeh screen, and NETO2 (no evidence in any original I opened). Intact WWOX binding to full-length ErbB4 in cells rests on Aqeilan 2005 (abstract only).

Q2 Pertinent neural systems. None of the interactions was observed in neurons with a WWOX readout. The closest are row 8 (mouse cerebellar lysate, n = 2 per group, peptide pull-down) and row 4 (a human brain cDNA protein array, but bacterially expressed, so not a neural observation). All ErbB4 and PPxY biophysics is on recombinant human domains; all cell-based WWOX-ErbB4 work is in HeLa, MCF-7, COS or HEK cells.

Q3 Functional consequences. Cellular: from the abstract only, WWOX keeps ErbB-4 in the cytoplasm and suppresses YAP coactivation (HeLa, MCF-7). ITCH-WWOX ubiquitination and p73 effects: SUMM, no sizes. P47T mice: reduced survival and hyperactivity, a whole-animal phenotype not tied to a specific partner. NETO2 side (no WWOX): Pressey, neurons: Neto2 alone did not alter total or surface KCC2; Neto2+GluK2 raised total KCC2 (p = 0.04, n = 9 cells) and surface KCC2 (p = 0.004); in COS-7, Neto2 raised total KCC2 (p = 0.029); the abstract is looser than the Results on this. Neto2-/- mice (Mennesson 2019, 8-12 weeks): higher cued-fear freezing and slower extinction, synaptosomal GluK2/3 -20.8% ventral hippocampus (p = 0.0053, n 7/7) and -36.5% mPFC (p = 0.038, n 4/5), GluK5 -23.8% ventral hippocampus (p = 0.026) and -16.9% amygdala (p = 0.0014); Mennesson 2020 (abstract): adult but not P23 amygdala shows 7.5% fewer PV-PNN cells and 23.1% lower PV intensity, with higher glutamatergic and lower GABAergic transmission. These tell us about NETO2, not WWOX.

Q4 Pharmacological lever. The originals identify no compound that acts on WW1-PPxY binding. Tool compounds appear only as assay reagents: TPA and PMA (PKC activation; TPA triggers ErbB-4 cleavage per Aqeilan 2005 abstract and Schuchardt Introduction; PMA raises KCC2 recycling via GluK2 S846/S868 in Pressey: E_GABA -69.6 to -89.1 mV, p = 0.007, wild-type neurons), MG-132, cycloheximide, cisplatin. None is characterised in these papers for selectivity or alternative actions, and none is a drug-versus-probe comparison. Natural inhibitors named: PPxY proteins (TMEM207, VOPP1) competing for WW1, in cancer cells (Saigo 2018 review). Schuchardt proposes WW domain engineering (Y85W) as a therapeutic concept only.

Q5 Unsupported transfers. (i) Cancer line to neuron: every WWOX-ErbB4, YAP and AP-2gamma functional result is from HeLa, MCF-7 or COS cells. (ii) Peptide to protein: Kd values for 12-13-mer peptides at 25 C do not give intact-protein affinity in a neuron. (iii) NETO2 as a WWOX partner: not supported; absent from Pressey's, Mennesson's and Hussain 2018's text (that absence is limited to the text I opened; the TAP-MS supplement list and Abu-Odeh supplementary tables were not seen). (iv) Viral PPxY (Liang 2021) to host biology: abstract only. (v) Brain "yes" for SIMPLE depends on a cDNA source only. (vi) Direction: loss of WWOX would, by the model in the abstract, release ErbB-4 from cytoplasmic retention, but no neural original shows that sign.

Q6 Improving a comparison or a new experiment. One hypothesis kept, at hypothesis level, no compound proposed.
- Observation: WWOX WW1 binds ErbB4 PPxY peptides directly but weakly (Kd 30-380 uM) and WW2 contributes only for dual-motif peptides; in HeLa and MCF-7, WWOX retains ErbB-4 and blocks YAP coactivation (abstract).
- Relation: WWOX competes with YAP for ErbB4 ICD.
- Hypothesised action: in WWOX loss of function, ErbB4 ICD escapes cytoplasmic retention and its nuclear function rises.
- Context: cultured mouse hippocampal or cortical neurons and interneurons after PKC-driven ErbB4 cleavage; unknown whether the ErbB4 ICD pathway operates in them at all.
- Pharmacological comparison: none justified yet. The reference point already in the originals is PKC activation as the trigger (TPA/PMA), and gamma-secretase processing as the step that releases the ICD (Schuchardt Introduction, secondary). No candidate drug is justified by these papers.
- Prediction: Wwox-null (or P47T) neurons show higher nuclear ErbB4 ICD after TPA than wild type, and the effect is reversed by wild-type WWOX but not by a WW1 mutant (W44F/P47A or P47T).
- Rejection: no genotype difference in ICD localisation, or ErbB4 not co-precipitating with Wwox from neuron lysate by PY3 peptide pull-down versus mutant peptide. The sign and size of any such effect are untested; "no compound is justified yet, and this measurement would change that" is the answer.

## (c) What the originals do not show
- No WWOX interaction measured in neurons or interneurons with a WWOX-specific readout; no endogenous WWOX-ErbB4 co-IP from brain.
- No NETO2-WWOX binding anywhere; the NETO2 papers (Pressey, both Mennesson) are about KARs and KCC2 and I found no WWOX, ErbB4 or PPxY words in the parts I read.
- No Kd below roughly 3 uM, and the physiological relevance of 30-380 uM peptide binding is asserted, not tested.
- No selective WW1-PPxY blocker or enhancer; no data on loss-of-function genotype class effects on any partner.
- Not seen: any figure image; Hussain 2018 supplements; Abu-Odeh Table S1; Aqeilan 2005, 2004 and 2007 Methods, figures and sample sizes; Liang 2021 body.

## (d) Not obtained
- Aqeilan 2005 (16061658), Aqeilan 2004 (15548692), Aqeilan 2007 (17909041): not open access; HTTP 403 on the publisher page, stopped; no browser or alternative host used.
- Liang 2021 (33536174): XML blocked; the summariser refused; not retried.
- Aldaz 2014 review (24932569): not opened.
- Rotem-Bamberger 2022: the held-file claim in the brief did not match the folder; text obtained by efetch instead.
- Unread by budget order: none of the priority list was skipped for budget; the gaps above are all access limits.