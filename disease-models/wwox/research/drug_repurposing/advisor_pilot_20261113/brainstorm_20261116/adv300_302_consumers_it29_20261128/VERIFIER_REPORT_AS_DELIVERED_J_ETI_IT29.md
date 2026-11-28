# Blind check report, sentences S1-S7 (2026-11-28)

Scope actually completed: S1, S2, S3, S4, S7. NOT completed: S5 and S6 (see "Not done").
Sources used: only files in /home/desktop/.claude/jobs/c6caa74e/tmp/j/src/ (plus two crops/renders of the supplied images in .../j/work/).

## Not done

S5 and S6 are NOT verified. My response while checking them was stopped by a safety classifier; I did not retry or reword it. Nothing in this report says anything about S5 or S6. Re-run them with another verifier.

## Summary

| id | verdict | reason |
|---|---|---|
| S1 | MUST CHANGE | mouse blot is "representative results of four independent experiments" (Fig 7c legend), omitted; CAL-29 reduction exists only after GAPDH normalisation (raw band is higher in WK) |
| S2 | MUST CHANGE | same four-experiment qualifier missing; "GSK3beta is broadly expressed" is not stated in the source; age conflict (legend P20 vs Methods P14) unflagged |
| S3 | MUST CHANGE | "n e tipo di errore non indicati" is false for the text value: Methods say text values are mean +/- SEM; only the Fig 3A legend lacks n and error type |
| S4 | KEEP | commentary on PMID 42397075, no own measurement |
| S5 | NOT VERIFIED | see above |
| S6 | NOT VERIFIED | see above |
| S7 | KEEP | numbers match Table 5.2; no test named for P; CI vs P inconsistent |

## S1 (p35563688 + p32000863)

Numbers, confirmed from the printed Figure 6D (RT-112, HT-1376, CAL-29; KK, WK, KC; band row over GAPDH row). I re-derived every mean from the printed lane densitometry (band/GAPDH per lane, then mean of three lanes) and they reproduce the text's means exactly:
- RT-112: KK 2.298, WK 0.741 -> WK/KK 0.3226 (0.32). Text: 2.2982 and 0.7414.
- HT-1376: KK 0.7607, WK 0.3937 -> 0.5176 (0.52). Text: 0.7606 and 0.3938.
- CAL-29: KK 0.6696, WK 0.5818 -> 0.8689 (0.87). Text: 0.6696 and 0.5818.
Stars WK vs KK in Fig 6D: RT-112 **, HT-1376 ***, CAL-29 * (readable in the image).
Labels (RT-112, HT-1376, CAL-29; bladder carcinoma; WK = WWOX overexpression with control vector; GAPDH loading control; "biological and technical triplicates"): all confirmed (Methods 2.1, 2.2; Fig 6).
"pSer9 e attivita chinasica non sono state misurate": confirmed. Antibody list in Methods 2.2 has only anti-GSK3B 22104-1-AP (no phospho antibody); Fig 6D shows only GSK3B and GAPDH; the supplement list (Methods) is KEGG and network figures only. Discussion line: "WWOX was found to repress GSK3B activity ... direct binding [101,102]" is literature, not a measurement.
Mouse numbers: Fig 7c (zoomed): total GSK3b ratio to beta-actin: cerebellum 2.2/2.4/2.4, hippocampus 2.3/2.4/2.6, cortex 2.2/2.4/2.6 (+/+, +/-, -/-). Null/WT = 1.091, 1.130, 1.182 -> +9, +13, +18 %. Confirmed from the image.

Problems:
1. Fig 7c legend (p32000863): "Quantitative densitometry of the immunoblots was performed, and the numbers depict the ratio of phosphorylated or total GSK3b to beta-actin protein level ... The representative results of four independent experiments are shown." The sentence says "densitometria a corsia singola ... non testata" and never says the blot is a representative of four independent experiments. A reader will take n = 1. The per-experiment values and any test are not reported (Statistical analysis section names one-way ANOVA generally; no marks on Fig 7c total GSK3b). So the conclusion "neither a change nor no change is established by the printed data" stands, but the qualifier must be present.
2. CAL-29 (essential qualifier): raw GSK3B band intensities KK 3224/3200/3152 vs WK 3957/2846/3875 -> WK raw mean is 1.12 x KK; GAPDH is 1.28 x higher in WK lanes. The "0.87" reduction exists only after GAPDH normalisation. For RT-112 (raw 0.58, GAPDH 1.75 x) and HT-1376 (raw 0.34, GAPDH 0.65 x) the raw bands are lower. "riduce ... in tre linee" should say that in CAL-29 the reduction comes from the normalisation. GAPDH in RT-112 KK lane 1 (1782) is far below lanes 2-3 (4142, 4299), so GAPDH loading is uneven within a group; this supports a cautious wording.
3. Optional: age of mice (P20 per legend), and that pSer9 was measured in mouse (reduced) but not in the human lines.

Replacement (Italian):
«La de-repressione (perdita di un freno fisico) non esclude però un effetto sull'abbondanza: in tre linee umane di carcinoma vescicale (RT-112, HT-1376, CAL-29) la sovraespressione stabile di WWOX riduce anche la GSK3β totale dopo normalizzazione sul controllo di carico GAPDH (Western, triplicati; WK/KK 0,32, 0,52 e 0,87; in CAL-29 l'effetto è modesto e nasce dalla normalizzazione, perché il segnale grezzo della banda GSK3β non è più basso nei lisati WK); pSer9 e attività chinasica non sono state misurate (PMID 35563688). È un guadagno di funzione in cellule tumorali: nel topo Wwox-null la densitometria stampata della GSK3β totale (+9, +13 e +18 % in cervelletto, ippocampo e corteccia, rapporto su β-actina, una corsia per genotipo e regione, da un blot indicato come rappresentativo di quattro esperimenti indipendenti, senza barre d'errore né test riportato) non stabilisce né un cambiamento né l'assenza di cambiamento dell'abbondanza (PMID 32000863).»
Deciding locators: p32000863 Fig 7 legend, panel c, last two sentences; p35563688 Fig 6D lane numbers (CAL-29 raw row 3224, 3200, 3152, 3957, 2846, 3875; GAPDH row).

## S2 (p32000863)

- Percentages 9/13/18: confirmed (above), from Fig 7c, "GSK3b" row, labels cerebellum, hippocampus, cortex. One lane per genotype per region, no error bars, no significance marks: confirmed in the image.
- Rounding: printed to one decimal, so 2.4/2.2 can be anywhere from about +4 % to +14 %; the quoted percentages are point values from rounded numbers (optional to say).
- "at postnatal day 20": Fig 7 legend says "at postnatal day 20". Methods "Western blotting" say tissues "at postnatal day 14" and list only anti-WWOX, anti-DCX, anti-beta-actin (no GSK3b or pSer9 antibody). The supplementary methods are not in the source set. Say "legend: P20" and note the discrepancy (optional but advisable).
- "GSK3beta is broadly expressed": not stated anywhere in p32000863 (search for broadly, ubiquit, widely: no hit). The blot shows a band in three brain regions at one age; that is all. Unsupported as a general statement; remove or attribute.
- Missing qualifier: "representative results of four independent experiments are shown" (same as S1).
- "not tested": no test is reported for total GSK3b in Fig 7c; acceptable if worded "no test reported".

Replacement (English):
"In the printed densitometry of Figure 7c (legend: postnatal day 20, ratio to beta-actin) total GSK3beta is 9, 13 and 18 per cent higher in Wwox-null than in wild-type cerebellum, hippocampus and cortex (2.4 vs 2.2, 2.6 vs 2.3, 2.6 vs 2.2; one lane per genotype per region, no error bars, no test reported; the legend calls the blot representative of four independent experiments whose individual values are not given), so neither a change nor the absence of one is established."
Deciding locator: Fig 7 legend, "Quantitative densitometry ... The representative results of four independent experiments are shown."; Methods, Western blotting ("postnatal day 14").

## S3 (p28769061 + supp)

Confirmed:
- Knockdown raises WWOX mRNA, overexpression lowers it: text "Upon PARTICLE knockdown ... significantly elevated WWOX expression (0.7 +/- 0.1 fold increase compared to negative siRNA control (NC2), p = 0.03; Fig. 3A ...)"; "Overexpression ... concomitant reduction in WWOX expression (p = 0.03, Fig. 3A)". Fig 3A image: WWOX (black) PK about 1.9 (star), NC2 about 1.0, PO about 0.2 (star).
- Fig 3A legend names U2OS; Discussion says "PARTICLE knockdown resulted in increased WWOX transcript levels in the breast cancer cell line MDA-MB-361". Methods: siRNA in MDA-MB-361; overexpression "MDA-MB-361 or U2OS". Fig S2A (second siRNA) legend: U2OS. Confirmed.
- "documentata solo sul trascritto": no Western or protein measurement of WWOX in the paper (search: western, immunoblot, protein level: none). Fig S5 is a proteomics meta-analysis of irradiation, not a PARTICLE-WWOX protein test.
- "Specificità allelica non testata": no allele, SNP, haplotype experiment (the only "allel" hits are "parallel"). The SPR/EMSA controls test sequence specificity (scrambled, single-strand, shuffled), not allele specificity.

Wrong: "n e tipo di errore non indicati". Methods, Statistical Analysis: "Values in the text are expressed as the mean +/- S.E.M., and n refers to the number of independent biological replicated data." So the 0.7 +/- 0.1 is an SEM. What is missing is n and the error-bar type in the Fig 3A legend itself (legend gives mean +/- SEM (n = 3) only for panels C-E; Fig S2 legend likewise for C-E).
Also note (interpretation, not an error): "0.7 fold increase" read as +0.7 over control would be 1.7, against bars at about 1.9 vs 1.0 (Fig S2: text 0.8, bar about 2.0 vs 1.0); the error bar on the knockdown WWOX bar looks about +/-0.4 by eye, larger than the stated 0.1.

Replacement (Italian):
«Una quarta leva, documentata solo sul trascritto e in linee tumorali: il lncRNA PARTICLE (il knockdown alza l'mRNA di WWOX, la sovraespressione lo abbassa; per la Figura 3A la legenda indica U2OS e la Discussione MDA-MB-361; il testo scrive «0.7 ± 0.1 fold increase» (media ± SEM secondo i Metodi) mentre le barre stanno a circa 1,9 contro 1,0; la legenda della Figura 3A non indica né n né il tipo di barra d'errore). Specificità allelica non testata (PMID 28769061).»
Optional additions: (a) Fig S1 (MDA-MB-361, irradiation): WWOX transcript rises together with PARTICLE at 2-4 h (0.25 Gy, 2 h: PARTICLE about 14, WWOX about 22), so the inverse relation holds only for the manipulations; (b) knockdown lowers viability (Fig S2 title; Fig 3E), a cost for any "lever".
Deciding locators: Methods "Statistical Analysis"; Fig 3 legend panel A.

## S4 (p43036373)

KEEP. The text is an Epilepsy Currents "Current Literature in Basic Science" commentary ("Commentary" section) on "Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids" (Brain 2026, PMID: 42397075; the PMID 42397075 is printed in the header). The body only describes "Steinberg et al." findings and open questions; no own experiment, table or number. PMID 43036373 appears in the record identifiers. I cannot verify from the source the statement "read on 2026-11-28 (PMC XML)" (the source is a plain-text extraction of the XML, PMC13769701); that is the caller's own record.

## S7 (p_sirimontakan)

KEEP. Table 5.2 (columns: SZ frequency / Follow-up time (month) / Incidence rate / IRR (95%CI) / Efficacy(95%CI)): etifoxine 290, 43.54, 6.66; placebo 348, 45.11, 7.71; IRR printed 0.863; "13.7% (-1.1-26.4)*"; footnote "IRR - incidence rate ratio, * p-value=0.027".
- Crude IRR from counts and person-time: (290/43.54)/(348/45.11) = 0.8634 -> 0.863. Efficacy 1 - 0.863 = 13.7 %. Confirmed.
- CI -1.1 to 26.4 includes 0 (no effect). Confirmed. A crude Wald interval on the counts gives IRR 0.74-1.01 (efficacy -0.9 % to 26.1 %), close to the printed interval; the matching Wald p is about 0.065, not 0.027. So the sentence "the two do not agree" holds.
- "table does not say which test gave the P value": the Methods name Chi-square or Fisher, independent t-test or Mann-Whitney, paired t, Friedman, Wilcoxon, SPSS 26.0; none is named for the IRR (search Poisson, negative binomial, Wald, likelihood: none). The IRR column header says "(95%CI)" but prints only 0.863.
- "small adult focal epilepsy trial": 40 randomised (20/20), inclusion "Age >= 20 years", "medically resistant focal epilepsy", mean age about 34-35. Table 5.1 analysis uses 16 vs 16 (per-protocol 17 vs 17 elsewhere); optional to state.
No change required.
