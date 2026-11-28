BLIND READER B2R1, PMID 32719346 (first author on the paper is Cao, not "Liu"; see section 4), read 2026-11-28. Hypothesis-level; not medical advice.

Clause tested, verbatim: "a Neuroligin 2 line (PMID 32719346) shows a restriction that follows the SWD phenotype (no effect in wild type or in two non-SWD mutants);"

Matching rule (PREREG "Matching rule"): MUST CHANGE = false or unsupported as written. ADD = a window, dose, species, unit or evidence level must be added. A negative is verified only with a dated search, otherwise UNSETTLED.

## 1. Statements and verdicts

Replicate units. Behaviour (Fig 5, Supp Figs 7-9): n = animals (Methods, Statistical analyses). Slice electrophysiology (Supp Fig 10): n = neurons.

Strain. NLG2 KO (Jackson #008139) is on a 129Sv x C57BL/6 mixed background. PAK3 Tg is C57BL/6J. FMR1 KO and its WT are FVB.

All p values below are my recomputation from the source-data workbook (MOESM4, sheets "Fig. 5", "Fig. S7" to "Fig. S10"). Nothing was read by eye except the Fig 5 and Supp Fig 8 and 10 images, which I viewed to confirm labels and layout.

| id | statement | verdict |
|---|---|---|
| R6-S01 | "a Neuroligin 2 line ... shows [an ETX effect]" (implicit: in the NLG2 line ETX changes something) | NO CHANGE for the facts; the wording is folded into the corrected sentence |
| R6-S02 | "a restriction" (what is restricted is never named) | ADD |
| R6-S03 | "no effect in wild type" | ADD |
| R6-S04 | "no effect ... in two non-SWD mutants" (two mutants, "no effect") | ADD |
| R6-S05 | "non-SWD" status of the two mutants | ADD (evidence level) |
| R6-S06 | "a restriction that follows the SWD phenotype" (connector "follows") | ADD |

**R6-S01 (NLG2 line, ETX effect). NO CHANGE for the facts.**
- Quote: "ETX significantly increased total travel distance, mean speed, mobile time, and time spent in center zone ... in NLG2 KO mice (Fig. 5a)".
- Locator: Fig 5a, 12 KO mice. Systemic ETX was 200 mg/kg IP, before versus after in the same animals.
- Recomputed paired t-tests reproduce the reported p exactly. Distance 12.7 to 37.7 m, p = 0.0022. Freezing 329 to 219 s, p = 0.0005.
- Fig 5b (EPM, n = 12): open-arm time p = 0.0484.
- Fig 5e (local thalamic ETX, n = 10): distance p = 0.0005.
- The effect is partial. Methods and Discussion: "only partially rescue motor deficits".
- Design caveat: Fig 5a, b and e have a before/after design with no vehicle arm.

**R6-S02 ("a restriction"). ADD.**
- The clause never says what is restricted. Two readings exist:
  - (i) ETX's behavioural benefit (open field, elevated plus maze, three-chamber social recognition). Supported with limits, see S03 to S06.
  - (ii) ETX suppression of SWDs. Not testable in any comparator. WT has no SWDs, and no EEG was recorded after ETX in WT, PAK3 or FMR1.
- Quote: "The SWDs and behavioral arrests were not observed in WT, NLG1 KO, or NLG3 KO mice" (Results, Fig 1).
- Corrected sentence below.

**R6-S03 ("no effect in wild type"). ADD.**
- Supported for in-vivo behaviour. Source data reproduce the reported p values exactly:
  - Supp Fig 7a, open field, WT n = 13, paired before/after: distance 31.0 to 34.4 (p = 0.4772); speed p = 0.4833; mobile time p = 0.5539; freezing 117.4 to 124.8 s (p = 0.8073); periphery p = 0.9018; centre p = 0.8903.
  - Supp Fig 7b, EPM, WT n = 10: open-arm time 79.7 to 85.6 s (p = 0.7839); open-arm entries p = 0.7961; the other four measures p = 0.4888 to 0.9291.
  - Fig 5c, d, three-chamber, WT n = 7. This n is in the workbook only. The Fig 5 legend gives "n = 8" for KO and no WT n.
    - Stage 3, S2 share before versus after: 82.8% to 82.5%, paired p = 0.98.
    - Versus 50%: before p = 0.0016, after p = 0.0062. The paper's tests are within-condition against chance, not before versus after.
- The unqualified "no effect" is contradicted at slice level. Supp Fig 10c, WT thalamic neurons, 500 uM ETX in the bath: "There is significant reduction in the number of action potentials in both WT (p = 0.0012) and NLG2 KO (p = 0.0001) neurons after the ETX treatment".
  - Recomputed, unpaired, Student t. WT untreated (Supp Fig 10b, n = 13) versus ETX (10c, n = 20): t = 3.55, df = 31, p = 0.0012.
  - KO untreated (10b, n = 17) versus ETX (10c, n = 34): p = 0.0001.
  - Outcome: action potentials in the rebound burst after hyperpolarisation to -80 mV.
  - Replicate unit is the neuron, and the comparison is between separate cell populations.
- Not in the paper: ETX on SWDs in WT (no SWDs there), ETX in WT at any dose other than 200 mg/kg, a vehicle arm for the behavioural before/after design.
- If "no effect" is read to cover any ETX effect, this becomes MUST CHANGE. As the behavioural restriction it is ADD.

**R6-S04 ("no effect ... in two non-SWD mutants", the effect part). ADD.**
- The two mutants are PAK3 transgenic (n = 12, WT littermates n = 8) and FMR1 KO (n = 7, WT n = 9). Only the three-chamber social-recognition test was run. No open field or EPM was run in either mutant.
- Supp Fig 8b, PAK3 Tg, S2 share:
  - before 46.5%, after 48.6%.
  - Versus 50%: p = 0.5266 and p = 0.886, as reported.
  - Paired before versus after: p = 0.87.
- Supp Fig 9b, FMR1 KO, S2 share:
  - before 52.0%, after 56.3%.
  - Versus 50%: p = 0.8359 and p = 0.6543, as reported.
  - Paired before versus after: p = 0.80.
- Their WT littermates (Supp Figs 8b, 9b) keep a normal S2 preference with ETX (paired p = 0.74 and p = 0.91).
- The outcome in these mutants is "no rescue of a baseline deficit". In WT it is "no change from a normal baseline", so the two "no effects" are different kinds of result.
- n = 7 for FMR1 is small, and the "after" values scatter widely (4.8% to 95.2%, read from the workbook). There is no power statement.
- The NLG1 KO and NLG3 KO lines also lack SWDs, but they were not given ETX. A reader must not take them for the "two mutants".

**R6-S05 ("non-SWD" status of the two mutants). ADD (evidence level).**
- No EEG was recorded in PAK3 Tg or FMR1 KO in this paper. The status comes only from citations.
- Quotes:
  - "PAK3 transgenic mice, which exhibit similar social recognition memory deficits but have no seizures46".
  - "The FMR1 KO mice also have increased susceptibility to seizures, which differ from absence seizures48".
  - Discussion: "two other ASD mouse models, that do not have the SWDs or absence seizures".
- Ref 46 is Leung 2018, Cell Rep, an entorhinal-to-dentate social-memory paper. Ref 48 is Berry-Kravis 2002, a clinical review of epilepsy in fragile X syndrome. The peer-review file says "without SWD (Leung 2018)".
- FMR1 KO is described as seizure-prone, so "non-SWD" holds only for absence-type SWDs, by citation.
- Dated negative search, 2026-11-28, run one keyword at a time:
  - "PAK3" in the main text extract. Hits: Results (ETX paragraph) and Methods (genotyping and the line); no EEG recording of PAK3.
  - "FMR1" in the main text extract. Hits: Results (ETX paragraph, Supp Fig 9) and Methods (source of the line); no EEG recording of FMR1.
  - "PAK3" and "FMR1" in the MOESM1 text (8 hits). All 8 are in the Supp Fig 8 and 9 captions, which report behaviour only.
  - "EEG" in the peer-review docx, in lines naming PAK3 or FMR1. 0 hits.
  - The workbook has no EEG sheet for these lines. Its sheets are Fig 1 to 7, S1, S3 to S11 and S13.
- Within this paper, no SWD recording in either mutant exists.

**R6-S06 (connector "follows the SWD phenotype"). ADD.**
- Only one SWD-positive line (NLG2 KO) was tested with ETX. SWD presence is therefore completely confounded with NLG2 loss. The comparators are WT, PAK3 and FMR1, whose "no SWD" status is cited, not measured (S05).
- The authors' own wording is hedged:
  - "these results suggest that ETX alleviates the behavioral deficits of NLG2 KO mice through blocking the SWDs".
  - "we cannot rule out the possibility that ETX may also act through other mechanisms independent of the SWDs and/or other brain regions also contribute".
- SWD burden was not recorded in the animals during the ETX behavioural tests, so SWD and behaviour were never linked per animal.
- The KO "rescue" in Fig 5d (n = 8) is a within-condition test against chance, not a before/after contrast.
  - The reported p = 0.0084 is S2 share after ETX versus 50% (77.8%).
  - Before: 52.9%, p = 0.6516.
  - Direct paired before versus after, my recompute: t = 2.44, df = 7, p = 0.045 (not corrected for multiple comparisons).
- The 200 mg/kg dose abolishes SWDs in KO (Fig 2a, n = 8 versus vehicle n = 8).
- Not false, but it should say "is consistent with", not "follows".

## 2. Corrected sentences

- **R6-S02 / S03 / S04 / S05 / S06 combined (ADD).** Replace the clause with:
  "in an NLG2-knockout mouse line (PMID 32719346; 129Sv x C57BL/6 mixed background) with spontaneous 5-8 Hz spike-wave discharges, ethosuximide 200 mg/kg IP (before/after design, no vehicle arm) improved open-field, elevated-plus-maze and three-chamber social-recognition scores (Fig 5; n = 8 to 12 animals), while it changed none of the open-field, elevated-plus-maze or social-recognition measures in WT mice (Supp Fig 7, n = 10 to 13; Fig 5c, d, n = 7) and did not rescue the social-recognition deficit in PAK3-transgenic (n = 12) or FMR1-knockout (n = 7) mice, which the authors, citing earlier work, regard as lacking absence-type SWDs (SWDs were not recorded in them); this pattern is consistent with, but does not prove, an SWD-dependent effect, and in WT thalamic slices 500 uM ethosuximide still reduced rebound burst firing (Supp Fig 10c, p = 0.0012, neurons)."
- **R6-S03 alone (ADD):** "no behavioural effect in WT mice (open field, elevated plus maze, three-chamber); ethosuximide did reduce rebound burst firing in WT thalamic slices (500 uM, Supp Fig 10c)."
- **R6-S01:** NO CHANGE for the facts; the dose and route are added in the sentence above.

## 3. Counts

- Statements judged: 6. NO CHANGE 1 (S01). ADD 5 (S02 to S06). MUST CHANGE 0. UNSETTLED 0.
- Strict (MUST CHANGE) count under the PREREG rule: 0.
- Loose (strict + ADD) count: 5 of 6.
- S03 would become MUST CHANGE only if "no effect" is read as any ETX effect, in which case the Supp Fig 10c WT slice reduction contradicts it.
- Every p value I cite was recomputed from the workbook and matched the figure or supplement legend.
  - Matched in the workbook: Fig 5a, b, e; Fig 5c, d (within-condition tests); Supp Figs 7a, 7b, 8a, 8b, 9a, 9b, 10c.
  - One extra check: the Supp Fig 10a, b WT versus KO comparison. Welch t on the workbook gives p = 0.68 for 10a and Student t gives p = 0.65 for 10b, against the caption values 0.5134 and 0.6464. Student matches 10b. I did not reproduce 10a: the workbook rows give different n than the caption (WT 11, KO 15 versus WT 9, KO 17). This does not affect any verdict.
- The only numbers not in the paper are the paired before-versus-after tests I computed, labelled "recompute".

## 4. What I opened and what I did not

- **Opened, repository files:** the PREREG "Matching rule" section only, and the blind packet (all of it).
- **Opened, held sources, in the root checkout:**
  - files/fulltext/PMID32719346_Liu2020_PMC_r2.xml, whole text including all legends.
  - files/figures/PMID32719346_r2/ Fig 5 (viewed).
  - MOESM1 text extract (whole), plus Supp Figs 8 and 10 viewed as page images at 70 to 80 dpi.
  - MOESM2 docx (peer-review file), text extracted and searched with the keywords above, not read end to end.
  - MOESM3 (Reporting Summary), page 1 viewed.
  - MOESM4 xlsx: Fig 5, S6 to S10 sheets parsed and used. Fig 1 to 4, 6, 7, S1, S3 to S5, S11 and S13 were parsed but not used for any verdict.
  - PMC7385104.1.pdf: text extracted for a keyword scan of the ETX lines; not read in full.
- **Figures not viewed:** Figs 1 to 4, 6 and 7 as images. Their legends are in the full text, which I read.
- **Not opened:** any other file of the packet folder, any registry, ledger, receipt, note, protocol or memory file, and PMID 42422765.
- **Failure and accident.** My `ls ..` call while listing my scratch folder also printed the contents of the parent tmp directory: a few extract and log files. I opened none of them, so nothing there unblinded me. Nothing else failed.
- **Author name.** The XML author list starts "Cao; Liu; ...". The paper's own title page and the supplement header say "Cao et al.". The packet and the file name use "Liu 2020". This is only a labelling mismatch, not a verdict.
- **Disk.** About 0.8 MB written (scratch text, 3 page PNGs, scripts); nothing written in the repository. I deleted the scratch folder `/home/desktop/.claude/jobs/8fe7aef9/tmp/b2r1blind/` and `/tmp/b2scripts/`, and checked that both are gone.
