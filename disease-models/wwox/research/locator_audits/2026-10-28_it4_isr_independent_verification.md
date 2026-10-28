# Independent verification of the ISR interactome and Atf4 findings, 2026-10-28

Producer: scientist-c (isr_kinase_interactome_atf4_reconciliation_it4_20261028.md). Verifier: independent subagent, sources first, producer note read afterwards. Verdict: propositions P1-P4 SUPPORTED, no overshoot found; two omissions (Sassano caption, AMOT/DVL2) added to the note.

# Independent verification: ISR / GCN1 / PERK propositions (2026-10-28)

Method: own reading of sources first (local Hussain Data Sheets 1-4 and Europe PMC XML PMC6300487; Sassano PMC10243573 XML; Lucas-Clarke PMC13684411 XML plus supplementary docx/xlsx, each fetched into its own scratchpad dir and parsed with python -I). Producer notes were opened only after the findings below were written. No e-mail address or credential sent anywhere.

## Table

| # | Proposition | Verdict | Source location / quote / value |
|---|---|---|---|
| P1a | GCN1 row: 2 and 8 spectra, IS 0.133, CRAPome 0.16 | SUPPORTED | Data_Sheet_2.tsv line 96: "94 GCN1L_HUMAN 10985 GCN1 ... 1 1 2 8 10 0.13302 0.22095 0.16035" (PPX=1, LPX=1, rep1=2, rep2=8, total 10, IS 0.1330, prey score 0.221, CRAPome 0.160). Rank 94 of 217 rows (bait + 216 filtered preys, rows 1-217 sorted by IS). Data_Sheet_1: rep1 GCN1L1 unique 2 / total 2; rep2 unique 7 / total 8 |
| P1b | Thresholds 0.2 good candidate, 0.3 high confidence | SUPPORTED | Results: "14 proteins with TAP-MS interaction scores (IS) > 0.3 ... very high likelihood of being direct WWOX physical binding partners ... 18 good candidate ... IS < 0.3 and > 0.2". GCN1 (0.133) is below both |
| P1c | GCN1 not discussed/validated | SUPPORTED | No "GCN" string anywhere in the main text (searched full XML) |
| P1d | Only SEC23IP, SCAMP3, VOPP1 validated by co-IP | SUPPORTED | "We validated the direct physical interaction of WWOX with these three proteins by means of co-immunoprecipitation"; Fig 3A. (Other known interactors are cited from literature, not co-IPed.) |
| P1e | Bait = C-terminal SFB full-length WWOX, stable, HEK293T | SUPPORTED | Methods: "HEK293T cells stably expressing ... SFB triple-tagged WWOX"; "C-terminal triple (S tag-Flag tag-SBP tag, i.e., SFB) tagged fusion protein"; cDNA "full reading frame" |
| P1f | PERK, GCN2, HRI, PKR, eIF2alpha, ATF4 absent | SUPPORTED | Case-insensitive symbol/UniProt-ID search of all four Data Sheets: no EIF2AK1-4 (E2AK*), EIF2S1, ATF4. Only EIF2 hit is IF2GL (EIF2S3L, a gamma-like subunit) in Data Sheet 1 only |
| P1 extra | (not in proposition) | note | Paper's funnel: 383 shared -> 253 with CRAPome < 0.2 -> 216 after score filter. GCN1 (CRAPome 0.160) is inside the 216-protein list. Data Sheet 3 gives GCN1 one PPkY (238-241) and one LPvF (1296-1299) motif. The sheet file has 574 data rows; only rows 1-217 are the paper's shortlist |
| P2a | BioID, PERK-BirA*, HEK293-T | SUPPORTED | "PERK-BirA* in HEK293-T cells"; C-terminal tag |
| P2b | Control = mock-transfected parental cells, not BirA* alone | SUPPORTED | "using mock-transfected parental HEK293-T cells treated in the same way (50 uM biotin for 24 h), as a control"; Discussion concedes later studies used untagged BirA*/TurboID controls |
| P2c | WWOX Q9NZC7: 3 spectra, 3 unique peptides, none in control | SUPPORTED | Table 1 row: "WW domain-containing oxidoreductase ... Q9NZC7 WWOX 47 kDa 3 3 0 0 99% 0" (PERK-BirA spectra 3, unique 3, control 0, 0; probability 99%/0) |
| P2d | GCN1 stronger, 10 spectra | SUPPORTED | "eIF-2-alpha kinase GCN1 ... Q92616 GCN1 293 kDa 10 10 0 0 100% 0" (10 spectra, 10 unique, control 0). Also 2/2 as many spectra as WWOX x3.3 |
| P2e | Many ribosomal/translation proteins in list | SUPPORTED | My parse: 27 "ribosomal protein" rows (RPS3, RPL15, RPL10, RPL38, RPS27A ... of 274 parseable of 276) and about 20 translation/elongation factor rows (EIF4G1/2, EIF4B, EIF5, EIF5B, EIF3D, EEF2, EEF1A1...). Only 4 ribosomal rows sit in the control-zero block; others have 1+ control spectra |
| P2f | WWOX row = proximity labelling only | SUPPORTED (and slightly more) | WWOX is not mentioned in text; only VAPB (N=3) and SERCA2 (N=2) were co-IP validated. Caveat found: the Table 1 caption says all hits are "not in control", but the table also contains rows with control counts of 1 (e.g. MTDH 24 vs 1); the WWOX row is in the control = 0 block (about 66th of 125 control-0 rows by my parse) |
| P2 extra | (not in proposition) | note | AMOT (Q4VCS5) and DVL2 (2 spectra each, control 0), both known WWOX WW-domain binders, are also in the PERK list, as is GCN1 |
| P3a | Atf4 ICC: U = 0, P = 0.0022, Fig 5H-I, 6 vs 6 | SUPPORTED (6 vs 6 inferred) | Results: "significant upregulation of Atf4 levels in Abeta42 flies upon Wwox knockdown (U = 0 P = 0.0022, Fig. 5H and I, N = 6)"; Fig 5 legend: "Mann-Whitney Test (panel I)". The text gives N = 6 brains, not per group. 6 vs 6 follows from the P value (see P3e) |
| P3b | LacZ comparison not significant; give test | SUPPORTED, with the number | Main text: "not observed in LacZ-expressing Wwox knockdown flies (Supplementary Fig. 5D-E)". Supplementary docx, Supp Fig 5 legend: "no upregulation of Atf4 ... in the absence of Abeta42 (mean +/- SD, N = 6 brains, statistics = two-tailed unpaired t-test t = 0.0894 p = 0.9305)" |
| P3c | Xbp1 reporter t = 1.365, P = 0.1954 (Supp Fig 5F-G) | SUPPORTED | Main text and supp legend: "t = 1.365, P = 0.1954 ... N = 6-9"; legend: "two-tailed unpaired t-test, N = 6-9 brains" |
| P3d | No interaction test for Atf4; no p-eIF2alpha, PERK, GCN2 measurement | SUPPORTED | Main text, supp docx and xlsx searched: no phospho, p-eIF2, Pek/PERK/Gcn2 measurement. Two-way ANOVA is used for lactate (interaction F = 23.606, Padj = 0.0174) and ATP, not Atf4. The Discussion says "we did not determine whether WWOX is activating this pathway directly" |
| P3e | Minimal exact two-sided P, 6 vs 6 MWU = 2/924 = 0.0022 | SUPPORTED (computed) | C(12,6) = 924 arrangements; by exhaustive enumeration P(U = 0) = 1/924, two-sided 2/924 = 0.0021645 (0.0022). Reported P equals the floor, so U = 0 means complete separation. 5 vs 7 would give 2/792 = 0.0025, so the reported 0.0022 does point to 6 vs 6 |
| P4a | Sig in one, not in other, is not a demonstrated difference | SUPPORTED (valid statistical point) | Two separate two-group tests (Mann-Whitney in Abeta42, t-test in LacZ). The supp title nevertheless says "Abeta42-dependent increase" and the main text says "which were not observed" (implied dependence) |
| P4b | Non-significant Xbp1 reporter cannot exclude IRE1 | SUPPORTED | N = 6-9, one time point, one background, no positive control described; the authors nevertheless write "These data suggest that neuronal Wwox knockdown specifically upregulates the PERK-Atf4 branch" |
| P4c | Sources alone show neither direct WWOX-GCN1 binding nor WWOX-PERK functional link | SUPPORTED | See P1, P2 above. Notably, Lucas-Clarke itself writes "WWOX has also been shown to directly bind GCN1, 56" with ref 56 = Hussain 2018, and cites Sassano (ref 58) for "interact in proximity with PERK". The first is an overreach of Hussain (IS 0.133, unvalidated, unmentioned) |

## Statements I could not reproduce or could only partly check
- Group sizes "6 vs 6" are not stated per group in the paper (only "N = 6 brains"); inferred from U = 0, P = 0.0022.
- Fig 5 legend lists "independent brains (panels G, J)" and omits panel I; unit of analysis for Atf4 is nonetheless stated in Methods as four ROIs averaged per brain.
- Direction of the Xbp1 difference not given in the legend text; Fig 5H-I effect size not read (images not opened).
- Sassano: 12 of 276 rows were not parsed by my regex (274/276 name matches); counts of ribosomal rows are therefore approximate (>=27).
- Not independently checked: t-test df values and the post-hoc confidence-interval figures in the producer note.

## Comparison with the producer's notes (read afterwards)
Agreement: every P1-P3 figure in proposition and in the producer note (GCN1 row, 0.133, 0.160, 2/8 spectra with 2/7 unique peptides, rank 94 of 217; WWOX 3/3/0; GCN1 10/10/0; t = 0.0894, P = 0.9305; Xbp1 t = 1.365, P = 0.1954; 2/924) match the sources.

Disagreements / over- or understatements:
1. NOT a disagreement: the producer already identifies Hussain as "fly ref 56" and concludes it does not support "directly binds GCN1"; I confirm the fly paper Discussion sentence is "WWOX has also been shown to directly bind GCN1, 56" (ref 56 = Hussain 2018), a documented overreach of that source.
2. UNDERSTATED: Sassano Table 1 is internally inconsistent with its own caption (rows with control spectra 1 are present; 276 listed vs a caption "only detected with PERK-BirA"). The producer mentions the 276/129/FDR inconsistencies but not this; WWOX itself is within the control-0 block, so P2 holds.
3. UNDERSTATED: the PERK BioID list also contains AMOT and DVL2, known WWOX WW1 partners, alongside WWOX and GCN1; this slightly strengthens the "cluster of WWOX-binding proteins near PERK" reading and should not be left out when judging whether the WWOX row is noise.
4. POSSIBLE OVERSTATEMENT in producer note: "SEC23IP and SCAMP3 [validated] by WW1-dependent GST pull-down" and "no empty-vector purification is described" - I did not verify these (outside the propositions); and "about 1.0 to about 1.28 normalised" was read from a figure I did not open.
5. Producer's statement that the supp legend title "Abeta42-dependent" is not supported by an interaction test is correct (my P4a).
6. No producer overstatement found on P1-P3 core numbers. The verdict wording in P4 (c) is, in my reading, correct and appropriately conservative.
