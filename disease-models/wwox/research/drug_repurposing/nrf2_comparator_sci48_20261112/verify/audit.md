# SCI48 blind verification V10 (claim actor nr-y, 2026-11-12)

Non-canonical research material. Not medical advice; no dose, ranking or recommendation. Labels DATO (read in a source), INFERENZA (mine). Information from PubMed or its full-text tool is cited as "According to PubMed" with the DOI of each article. Paths are relative to `disease-models/wwox/research/drug_repurposing/nrf2_comparator_sci48_20261112/`. Files: `verify/verdicts.tsv` (100 rows), `verify/recompute_figures.tsv`, `verify/queries_verifier.tsv`, `verify/receipts/` (25 staged receipts, all validated OK, prior receipt = the producer's `-74` id where one exists, `reread_reason` adversarial_reanalysis; not recorded).

Read before the verdicts were written: `BRIEF_P.md`, `S0_before_search.md`, `COLUMNS.md`, `winkel_table.tsv`, `sfn_table.tsv`, `matrix.tsv`, `evidence.tsv`, `figure_notes.tsv`, `queries.tsv`. `answers.md`, `phase_note.md`, `minimum_comparison.md` were opened only after `verdicts.tsv` existed (section 6).

## 1 · Verdicts

| Item | Rows checked | Correct | Defective | Other | Verdict |
|---|---|---|---|---|---|
| 1 Winkel, row by row (W01-W33) | 33 | 31 (9 with a note) | 1 (W22, minor) | 1 unverifiable (W02, ChEMBL REST not requested by me) | **Holds.** Every decisive proposition reproduces from the text and the nine figures. |
| 2 Sulforaphane sources (S01-S23: 18 text-depth rows, 5 abstract rows) | 23 | 22 | 1 (S14, minor, abstract over-specified) | 0 | **Holds** for what the table states; the table is **incomplete** (item 3). |
| 3 Absence claims | 3 claims | 1 (3c, second reagent class) | 2 (3a, neural SFN loss-arm list; 3b, RA839 neural absence) | 11 new candidate rows (`source_silent` = abstract or text silent on loss verification) | **Both absence claims fail as stated**; see 3. |
| 4 Matrix roles and wording (M01-M29) | 29 | 23 | 2 (M06, M13) | 4 unverifiable (M20-M23, reused SCI46 rows not re-read); 1 gap finding (missing rows) | One row more favourable than its source (M13); no row classed not-interpretable by depth without saying so (M15-M19 are all labelled as abstract-depth). |

## 2 · The decisive findings

1. **Winkel: no check of the Nrf2 knock-out is printed anywhere. CONFIRMED.** Whole text searched for `knock-out`, `knockout`, `-/-`, `genotyp`, `Western`, `immunoblot`, `Nqo1`, `Hmox1`: `genotyp` and `Hmox1` have zero hits; `Western`/`immunoblot` occur only in the Keap1-Nrf2 pull-down (Methods, Fig. 5) and the Nos2 sentence; `-/-` occurs only in the BMDM sentence; `Nqo1` occurs only in wild-type or siKeap1 contexts. All nine figures opened (1 structures; 2 FP, reporter, translocation, ARE binding; 3 crystal; 4 ITC; 5 pull-down; 6 Venn; 7 NO/Nos2/Nqo1 wild type; 8 siKeap1 arm; 9 liver): none has a knock-out panel. The Nrf2 qPCR primer set is displayed only in liver (Fig. 9). The knock-out is "12-week-old Nrf2+/+ and Nrf2-/- mice in the C57BL/6J background", with no allele or source. Supplements S1-S4 (four xlsx, one docx are listed on the page) were not requested by either of us, so the only residual doubt is a baseline in S3.
2. **CDDO-Me is absent from the knock-out arm and from the array. CONFIRMED.** CDDO-Me occurs only in Abstract, Introduction, Fig. 2 (HepG2, U2OS), Fig. 7 (wild type, 50 nM) and Discussion. Fig. 6 holds siKeap1-1, siKeap1-2, RA839. Also no knock-out arm for NO or Nos2 with any reagent.
3. **Array numbers and direction:** 105 probe sets in wild type (34+9+59+3), "only two genes, Zfp192 and Pank1" in knock-out (the paper changes unit from probe sets to genes; group size and direction not printed; "not regulated in wild-type macrophages" is the authors' statement); text gives 292 and 322 for siKeap1-1 and -2 whereas the Venn gives 322 and 292 (reverse), overlap 192 reproduced.
4. **Keap1 silencing:** about 75 and 80% (mRNA only; no protein); timing given two ways (Methods: medium change 1 day after transfection, then 48 h; Discussion: expression analysed 48 h after transfection).
5. **Kd and FP:** ITC Kd 6 +/- 1.2 uM (S.E., n=3), FP IC50 0.14 +/- 0.04 uM (S.D., n=6), PDB 5CGJ at 3.36 A. New internal observation (mine, `recompute_figures.tsv` R05): the tabulated DeltaH (-28) and TDeltaS (-22 kcal/mol) give DeltaG -6, i.e. Kd about 40 uM, not 6 uM; the ETGE row is self-consistent. Inside the +/-5 kcal/mol error of TDeltaS, so not an error of the producer, but the "multiples of Kd" depend on which Kd is used.
6. **Sulforaphane sources at text depth** reproduce (Li, Yao, He, Mao), including Mao's figures 1, 2, 5, 6 (I did not open 3 and 4). Yao's knock-out arm is unmatched (confirmed verbatim: "SFN alone did not affect the immobility time during the TST and FST in control mice"; SFN's effect in wild type is shown only after LPS; no LPS arm and no matched wild-type arm in the knock-out experiment).
7. **The producer's absence claims fail** (3a, 3b below): at least nine neural-class papers with SFN in wild-type and Nrf2-null mice under the same insult were not in the table, and RA839 has been used in glioma lines and an immortalised astrocyte line.
8. **Matrix M13 is more favourable than its source**: the siRNA-Nrf2 result for SFN in BV2 is never stated in He 2022's text; only the Fig. 1B legend lists it.

## 3 · Absence claims, by my own strings

### 3a · Neural-class SFN with a genetic Nrf2 loss arm not listed by the producer

Perimeter: Europe PMC V1-V7 (queries_verifier.tsv; V1 first 100 of 199 records screened by regex on title and abstract; V3 and V4 were query defects, 1584 and 1102 free-text hits, not screened), PubMed strings V8-V9 (207 and 202 hits, 60 returned each), 15 abstracts opened (V11), three PMC pages opened beyond the abstract (V12). Regex screening misses wording I did not anticipate; this is a census of what my strings return, not a proof of completeness.

| PMID (year) | Class and design | What the abstract (or text) says about a loss arm | Depth |
|---|---|---|---|
| 27401964 (2016) | in vivo mouse brain microcirculation, LPS; SFN 5 and 50 mg/kg in WT and Nrf2-KO; human brain endothelial cells in vitro | SFN effect on leukocyte adhesion lost in KO at 5 mg/kg; at 50 mg/kg "partial effect" (adhesion down 40%); authors: SFN works in part independently of Nrf2; KO from a vendor, no verification printed | PMC text (targeted), DOI 10.1016/j.vph.2016.07.004 |
| 20953205 (2010) | in vivo mouse, traumatic brain injury; four groups n=8 (vehicle/SFN x Nrf2+/+, Nrf2-/-) | oxidative markers (24 h) and neurologic score (7 d): SFN effect present in +/+, absent in -/-; KO had worse baseline; genotype confirmed by PCR of blood DNA (allele check; no brain Nrf2 protein/mRNA check in KO) | PMC text (targeted), DOI 10.1038/aps.2010.101 |
| 25328080 (2015) | primary rat microglia; ICH in rat and mouse; SF in WT and Nrf2-KO; ARE decoy oligonucleotide in vitro | hematoma clearance improved by SF in WT, not in KO; KO from Chan 1996, no verification printed; a second reagent class (ARE decoy, an NRF2 inhibitor, not a KEAP1 binder) | PMC text (targeted), DOI 10.1111/jnc.12974 |
| 17962605 (2007) | mouse ICH, SFN, Nrf2-deficient | Nrf2-deficient mice more severe and "did not benefit" from SFN (behavioural deficits, neutrophils) | abstract, DOI 10.1161/strokeaha.107.486506 |
| 21254817 (2011) | mouse MPTP parkinsonism, SFN, Nrf2-KO | SFN protected nigral dopaminergic neurons in WT, not in KO (viability in neurons in vivo) | abstract, DOI 10.1089/ars.2010.3731 |
| 21764072 (2011) | mouse spinal cord injury, SFN, Nrf2-/- | locomotor score, edema, dying neurons: no benefit from SFN in Nrf2-/- | abstract, DOI 10.1016/j.jss.2011.05.049 |
| 24333359 (2014) | rat and Nrf2-deficient mice, amygdala kindling, SF | abstract states SF effects in rats and names deficient mice; the SFN-in-deficient result is not stated | abstract, DOI 10.1016/j.brainres.2013.12.004 |
| 18619545 (2008) | hippocampal slices, WT versus Nrf2-null, kainate; SFN plus lithium | combined SFN + lithium protected WT slices, not Nrf2-null littermates; second reagent class (GSK-3 inhibitor) | abstract, DOI 10.1016/j.mcn.2008.06.007 |
| 24948812 (2014) | brain capillaries ex vivo (endothelial), Nrf2-null | SFN effects absent in Nrf2-null capillaries | abstract, DOI 10.1523/jneurosci.2935-13.2014 |
| 26433376, 23864927, 26827637, 32949969 | lines: C6 astroglioma, SH-SY5Y, THP-1 microglia-like, bEnd.3 | Nrf2 siRNA abolished or diminished SFN protection | abstracts only (lines, own class) |
| 22911746 (2012) | mouse photothrombosis, SFN | no Nrf2-loss arm; SFN without effect on infarct or function (negative in WT) | abstract |

Consequences: the producer's table lists four text-depth neural sources (Li, Yao, He, Mao); the literature has at least **nine more in vivo neural-class SFN-in-null designs**, several with matched SFN arms in both genotypes under the same insult and with behavioural endpoints (TBI neurologic score, ICH deficits, SCI locomotion). Genotype PCR (TBI) is an allele check, not a protein/mRNA check at the endpoint. One source (27401964) records a partial persistence of SFN's effect at the higher dose in the null mouse: the only reached source that records an NRF2-independent component. Exposure datum: 21681606 (2011) reports SFN metabolites by tissue including brain in WT and Nrf2-/- mice (abstract only).

### 3b · RA839 in neural cells

Europe PMC all-field `RA839`: 36 hits (the same 36 as the producer's Q14); `"RA-839" OR "RA 839"`: 14 hits; PubMed [tiab] with the three spellings AND neural/glial words: 0 (the first version with six truncations was refused by the tool). Hits that are glial-lineage:
- **PMC6144715** (2018 Neuro-Oncology conference abstract, "Nrf2 mediates hypoxic tolerance in human glioblastoma cells"): "two selective small-molecule inhibitors of the Nrf2-Keap1-interaction, ML334 and RA839" in LNT-229, LN-308, T98G and the immortalised astrocyte line SVG; target genes and hypoxia-induced cell death; the abstract states Nrf2 activation followed by target gene expression and protection from hypoxia-induced death. No loss arm stated.
- **32203214** (2020, glioblastoma serine-metabolism paper; PMC7188854; journal and DOI not checked here): "RA 839, a Nrf2 activator, [was] purchased from Tocris"; induction of PHGDH and SHMT2 by RA 839 in LNT-229 and G55 glioblastoma cells (Suppl Fig 2B); read at passage depth only (one fullTextXML request, 200); no Nrf2-loss arm seen.
- Other neural-word hits (38409216, 40779837, 33854358, 32714135, 36086898, PMC6144739) do not use RA839 in their abstracts; why they match in the full text is unresolved (not opened).
INFERENZA: the producer's M06 and prior S4 hold for primary neurons, astrocytes and microglia but fail for glioma lines and an immortalised astrocyte line. None of these has a loss arm in what I read. (I opened 32203214's XML beyond the three allowed new-candidate openings; counted as a fourth opening and stated.)

### 3c · Second reagent class beside SFN in a loss design

Holds at text depth for Li, Yao, He, Mao (none uses a second reagent class beside SFN; He's TREM2 oligonucleotide acts downstream and the paper itself shows it lowers Nrf2). Qualified: Moretti 2021 (33096251, abstract) pairs SFN with a reversible non-covalent KEAP1 binder in primary neurons and astrocytes (loss arm not stated in the abstract; full text unread by anyone); Innamorato 2008 (18619545, abstract) combines SFN with lithium in WT versus Nrf2-null slices; Zhao 2015 (25328080) uses an ARE decoy next to SF in primary microglia. None of these is a non-covalent KEAP1 binder in an NRF2-loss design with SFN at text depth. Winkel pairs RA839 with CDDO-Me but CDDO-Me never enters the loss arm.

## 4 · Rows overturned or corrected

| Row | Producer | Correction |
|---|---|---|
| W22 | "only RA839 at 5, 10, 20 uM was tested" | Fig. 7A also has a 2.5 uM point (about 0.53); the same row's exposure column says 2.5-20 uM. |
| S14 | Innamorato abstract: SFN effects "in WT animals" | the abstract does not state the genotype of SFN-treated animals. |
| M06 | no neural RA839 study, title level | true for primary neural cells; glioma lines and SVG astrocyte line use RA839 (3b). |
| M13 | He BV2: "dependence ... (declared)", comparator | the siRNA-Nrf2 result is not stated in the text; only Nrf2 over-expression is described; role to not interpretable (depth: Fig. 1B unopened). |
| M21 | KI-696 viability, probe | reused row; the row's own floor-effect caveat conflicts with "dependence shown"; I would write comparator unless the floor effect is excluded (not re-read). |
| M04 | "does not allow a match of on-target response" | Nqo1 was measured for both reagents in wild type (about 55 and 44 versus LPS-vehicle 12, Fig. 7D); say "single-gene match only". |
| gap | matrix lacks rows for the 3a sources | add rows (roles in verdicts.tsv). |
| answers.md headline | "no printed verification of the loss" for Li, Yao, He | Yao's figure legends list an Nrf2 blot in the knock-out (Fig. 4A) and Nrf2 mRNA/protein for the siRNA experiment (Fig. 1); the producer's own S07/S08 say so; figures unopened by either of us. The headline over-generalises. |

Unflagged discrepancies inside the source that the producer did not flag but did not misstate: Fig. 6 legend "two-way ANOVA" versus Methods "pairwise ANOVA" (W15); translocation n=3 in text versus n=6 in the Fig. 2 legend (W09); Table 3 value "2.08E" truncated (W19); Keap1 silencing 75/80% fits the LPS bars versus the no-LPS control only (W14).

## 5 · Priors S1-S8 re-scored from my reading

| Prior | Producer | Mine | Basis |
|---|---|---|---|
| S1 reachable | partly | **partly** | stored PMC page complete; tool and Europe PMC XML routes not mine to retry; the "transient" half failed |
| S2 germline KO, adequacy by absent target-gene induction | partly | **partly** | germline KO in BMDM held (W11); adequacy by printed target-gene or protein absence failed (W12; only 2 versus 105 probe sets, indirect); S3 supplement unread |
| S3 CDDO-Me not in KO arm | held | **held** (stronger: no KO arm for NO/Nos2 either) | W21, W25 |
| S4 no RA839 use in neuron/astrocyte/microglia | held (title level) | **partly failed** | primary neural cells: none found; immortalised astrocyte line (SVG) and glioma lines: yes (3b) |
| S5 several null/knockdown papers; none functional with an adequately verified loss | partly | **partly** | functional endpoints with genetic loss exist in at least Li, Yao (sEPSC/sIPSC), TBI, ICH, SCI; "adequately verified" (protein/mRNA at endpoint) is met by none read; allele PCR (TBI) only |
| S6 ARE and viability protection lost under null; some microglia endpoints persist | partly | **partly** | lost: Li (HO-1 increment, neurons, TUNEL), TBI/ICH/SCI abstracts; persisted: Mao endothelium (73% of the SFN gain retained, R16), Holloway 50 mg/kg (partial); microglia SFN-in-null: ICH-microglia lost; no neural "mixed" microglia anti-inflammatory result read |
| S7 micromolar SFN, second reagent class needed | partly | **held** | 1-1.5 uM (Li, Mao, He), 5 uM (Danilov abstract), 1-100 uM (Holloway in vitro); in vivo 5-50 mg/kg; no text-depth source with a second reagent class |
| S8 no SFN + non-covalent binder in one loss design, neural | held | **held at abstract depth, not closed** | Moretti pairs them without a loss arm in the abstract; full text unread |

## 6 · The minimum comparison: are its premises the verified ones?

Opened after the verdicts. Premises checked against my reading:
- **50 nM versus 20 uM** (CDDO-Me versus RA839 in Winkel's Fig. 7): verified (Fig. 7B-D). Nqo1 induction at those concentrations was about 55 and 44 over LPS-vehicle 12 (my read), so a one-gene on-target match exists in wild type.
- **"10-20 uM is 1.7-3.3 times its ITC Kd, 71-143 times its FP IC50"**: arithmetic verified (R07, R08) on the printed 6 uM and 0.14 uM; caveat R05: the tabulated thermodynamics imply a Kd near 40 uM, which would put 10 uM below that Kd. Say both.
- **Winkel RA889/RA912 the only inactive scaffold controls, not run under loss**: verified (W06).
- **Mao neurons lack an OGD+sh-Nrf2 arm and a Sfn-alone arm**: verified from Fig. 2d,e.
- **"No verification printed" for the SFN loss arms**: verified for Li (text; figure legends absent from the tool text), He (KO), Mao (all of Figs 1-6 and text); **not verified as stated for Yao**, whose legends list an Nrf2 blot in the KO (Fig. 4A) and Nrf2 mRNA/protein in the siRNA experiment (Fig. 1).
- **"The only neural-class entries with an adequate loss are KI-696 in primary rat microglia ... and none for sulforaphane"**: reused SCI46 row not re-verified by me (M20-M23 unverifiable); the sulforaphane half is overtaken by 3a: matched SFN-in-both-arms designs with functional endpoints exist (TBI with PCR genotyping, ICH, SCI, MPTP, kainate slices), none with an endpoint-time protein/mRNA check at the depth read.
- **"Viability only as a toxicity control"** and the acute-versus-germline preference are proposals, not facts; they stand.
- The Winkel "contrast proposed but not run" (binder matches Keap1 loss, electrophile persists under loss) is the authors' suggestion in the Discussion (RA839 "might also allow the identification of potentially different effects of covalent and noncovalent Keap1 inhibitors"), not a result.
- `answers.md` still says "26 rows" with comparator 9 and not interpretable 12 in its headline; `phase_note.md` (29 rows: probe 2, comparator 11, not interpretable 13, conditional 3) matches the matrix I counted. The headline in answers.md is stale after the Mao extension.

## 7 · What I could not reach, and by which route

- ChEMBL id of RA839 (producer HTTP 500; not requested by me, per the brief).
- Winkel supplement Tables S1-S4 (PMC interstitial, Europe PMC supplementaryFiles "not open access"; not requested).
- Li 2022 main-figure legends and images (the PubMed tool returned text without them; Europe PMC XML gave HTTP 500 for the producer; not retried by another route): a loss check inside a main figure cannot be excluded for Li.
- Yao 2021, He 2022 figure images (legends only); Mao figures 3 and 4 not opened; Danilov 2009, Innamorato 2008 (LPS), Bergstrom 2011, Zhang 2021, Qiu 2023, Moretti 2021 at abstract depth (no PMC id for five; Moretti full text unread).
- Wu 2024, Costa 2024, Tran 2019, Davies 2016 (not re-read, per the brief): M20-M23 unverifiable by me.
- Candidates 17962605, 21254817, 21764072, 24333359, 18619545, 24948812 and the line-class four: abstract depth only; the first three of the PMC-text candidates read in targeted sections, not completely (discussion and introduction not read in full).
- The H1-H6 labels of the matrix are not defined in S0 section 5 as I read it (it names H1/H3 and H5 only); I could not check them against a definition.

## 8 · What I changed my mind on

I expected the producer's Winkel headline (no knock-out check) to be the weakest part; it is the strongest and reproduces fully. I expected the sulforaphane candidate list to be nearly complete after two search rounds; it was not (nine in vivo neural SFN-in-null papers missing, one of them recording a partial NRF2-independent effect). I expected "no neural RA839" to hold; it holds only for primary neural cells.

## 9 · Process state

Claims taken for 20 PMIDs plus the five text-depth ones (actor nr-y); 25 receipts staged and validated with `--check-doi`; nothing recorded in the ledger; no commits, gates, lint or tests; no agents started; no e-mail or registration service used; plain curl with the default user agent only (Europe PMC REST and fullTextXML, PMC article pages); no bot check, 403 or 429 was met. The three PMC article pages and the two Europe PMC XML responses were kept in the scratchpad only.
