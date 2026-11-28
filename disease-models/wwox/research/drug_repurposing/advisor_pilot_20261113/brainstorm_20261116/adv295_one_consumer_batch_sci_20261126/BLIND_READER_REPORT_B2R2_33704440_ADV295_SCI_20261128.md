# ADV-295 block 2, record 2 (PMID 33704440): blind reader report, verbatim

Subagent hand-back saved verbatim by SCI on 2026-11-28 (legend-delegate, claude-sonnet-5-5, effort high read back from the transcript). Model output, hypothesis level, not medical advice; not edited.

---

**Blind sentence-level reading: ADV-295 block 2, record 7 (PMID 33704440, El Ghaleb 2021; consumer DL-MECH-170)**

This is hypothesis-level research on public literature, not medical advice. PMID 40825030 is not held for this packet, so anything resting on it is not judged as true or false.

## 1. Verdicts

Verbatim bullet: "**Symptomatic in every paper that looks.** Genotype decides whether a T-type block is mechanism-matched: gain-of-function T-type variants cause seizures and loss-of-function variants cause neurodevelopmental disease without seizures (PMID 33704440, PMID 40825030)."

| id | verbatim statement or element | verdict | grounds (quote, locator) |
|---|---|---|---|
| R7-S01 | "Symptomatic in every paper that looks." | UNSETTLED | The bullet does not say what is symptomatic or which papers "look". I assume it means T-type block acts on symptoms only. The one treatment datum in 33704440 is "targeted treatment of Patient 1 ... with ethosuximide resulted in improved control of seizures, in particular in a reduction of myoclonic seizures" (Discussion, last paragraph; human, n=1, uncontrolled). I found no dose, duration, quantification or developmental outcome on the drug. The paper does not test disease modification, so it should not be counted as a paper that "looked" for it. To settle this: the referent and the list of papers. |
| R7-S02 | "Genotype decides whether a T-type block is mechanism-matched" | ADD (evidence level, unit) | The paper supports a rationale only: GoF "makes Cav3.3 an attractive target for ... licensed T-type channel blockers" and "Further studies are required" (Discussion). The direction was measured per variant, by patch clamp of transfected HEK293T cells (Figs 2-5, Supp Table S3, n=6-9 cells per construct). No blocker was tested on any variant channel in the methods, results or figures. |
| R7-S03 | Colon: the seizure split that follows is the reason genotype decides | MUST CHANGE (same defect as S07, not an independent error) | A match between block and variant rests on the measured direction of channel function, not on whether seizures occur. The offered split does not hold on the GoF side (S04, S07). The paper has no loss-of-function arm. |
| R7-S04 | "gain-of-function T-type variants cause seizures" | MUST CHANGE | Supp Table S1, row "Seizures", individuals 1-6: Yes, Yes, No, No, Yes, Yes. So 4 of 6 human carriers had seizures. By variant: I860N 1/1 (onset 4 m), I860M 1/3 (onset 58 y), I1306T 1/1 (2 wk), M1425I 1/1 (2 y). Patients 3 and 4 (I860M, 28 y 11 m and 31 y) had none. I860M is shown to be GoF: V1/2 activation -49.1±0.4 vs -40.9±1.1 mV, n=7 vs 6 HEK293T cells (Supp Table S3; Fig 2N). The authors write "with or without epilepsy" (Discussion) and hedge even for I860N: "could explain seizures" (Abstract). The Introduction also says of CACNA1G/H variants proposed in inherited epilepsy that "none ... have been undoubtable identified as causing seizure phenotypes". |
| R7-S05 | "loss-of-function variants cause neurodevelopmental disease" | UNSETTLED | The carrier would be 40825030, not held. 33704440 has no loss-of-function patient. Its only relevant line, citing others, is "CACNA1I loss-of-function variants ... may contribute to the development of schizophrenia, autism and/or other complex neuropsychiatric disorders" (Introduction). That is a possible risk contribution, not causation. |
| R7-S06 | "... without seizures" (loss-of-function) | UNSETTLED | Not addressed in 33704440 (search below). The carrier would be 40825030, not held. |
| R7-S07 | "and" (contrast): seizures separate GoF from LoF, and neurodevelopmental disease without seizures marks LoF | MUST CHANGE | All six GoF carriers had impaired cognition (Results, first section: "impaired cognitive function in all six affected individuals"). Patients 3 and 4 had intellectual disability (IQ 50-70; IQ 36-51) and no seizures (Supp Table S1). GoF therefore also produces the phenotype the sentence gives to LoF. |
| R7-S08 | Scope "T-type variants", both clauses, no gene | ADD (gene, species) | 33704440 studies only CACNA1I (Cav3.3), four heterozygous missense variants in humans. Its Introduction and Discussion give a different phenotype for some CACNA1H GoF variants: "early-onset hypertension and hyperaldosteronism with incomplete penetrance", with no seizures mentioned there. It cannot carry a family-wide rule. |
| R7-S09 | "(PMID 33704440, PMID 40825030)" as joint support | ADD (which PMID carries which, evidence level) | 33704440 can support only: CACNA1I GoF with variable neurodevelopmental disorder, with seizures in some carriers. It supports nothing about LoF seizure status. |

**What PMID 40825030 would have to carry:**
- the T-type gene or genes studied;
- loss of function shown functionally for each variant;
- a causal (not merely risk) neurodevelopmental phenotype in individuals;
- seizure status actually ascertained for each carrier (age, follow-up, EEG), with none having seizures;
- enough genes to justify "T-type" in general, otherwise the gene must be named;
- for S01, whatever it shows about symptomatic versus disease-modifying effect.

## 2. Corrected sentences

- **S02:** "The measured functional direction of the individual variant decides whether a T-type block opposes the channel defect; for CACNA1I this is an inference from gating data in transfected HEK293T cells (four variants), with one patient's uncontrolled report of fewer seizures on ethosuximide, and is not a demonstration of efficacy."
- **S03:** "... mechanism-matched, because the block can oppose increased channel function; whether a carrier has seizures does not establish that direction:"
- **S04:** "CACNA1I gain-of-function variants are associated with a neurodevelopmental disorder in which seizures occur in some carriers: 4 of 6 individuals (4 variants); two of three I860M carriers, aged about 29 and 31 years, had none (PMID 33704440, Supp Table S1)."
- **S07:** "Seizure presence does not separate the two directions: CACNA1I gain-of-function carriers can also have neurodevelopmental disease without seizures."
- **S08:** name the gene in each clause: "human CACNA1I (Cav3.3) gain-of-function variants ...". The LoF clause needs the gene studied in 40825030.
- **S09:** "(gain of function, CACNA1I: PMID 33704440; loss of function: PMID 40825030, to be checked on that paper)."

## 3. Counts

9 statements:
- **MUST CHANGE:** 3 (S03, S04, S07). S03 and S07 are one defect, so there are two distinct errors: the universal "cause seizures" and the seizure-based split.
- **ADD:** 3 (S02, S08, S09).
- **NO CHANGE:** 0.
- **UNSETTLED:** 3 (S01, S05, S06).

## 4. Search record for the negatives

Date 2026-11-28, case-insensitive, one keyword per search.

Files searched:
- `ft.txt`: my extraction of `PMID33704440_ElGhaleb2021_PMC_r2.xml`, reference list excluded.
- `supp.txt`: copy of `awab101_Supplementary_Data.txt`.
- `art_pdf.txt`: `pdftotext -layout` of `PMC8422349.1.pdf`.

Queries on all three: `ethosuximide`, `eizure`, `pilep`, `loss`, `blocker`. `suximide` was also run on `art_pdf.txt` and `supp.txt`.

Results:
- `ethosuximide`: ft 1, supp 0, PDF 1.
- `loss`: ft 4, supp 5, PDF 6 lines. I read the ft and supp contexts, and the PDF lines matched by my pattern search. None reports a T-type loss-of-function patient or such a patient's seizure status. The supplement hits are hearing loss, seal loss and reference titles.

## 5. What I opened, limits and disk

**Opened:**
- the "Matching rule" section of the PREREG and the whole B2R2 packet;
- the article XML, read in full as extracted text (reference list excluded);
- all 7 main figure images;
- the supplement text (all of it), and supplement PDF pages 12-17 rendered at 60 dpi (Supp Figs S1-S6).

**Not read:**
- PMID 40825030, which is not held;
- the article's reference list;
- the PMC PDF page by page (keyword searches and a pattern check only);
- supplement PDF pages 1-11 and 18-19 as images (read as text).

I opened no other file of that folder, no registry, ledger or protocol, and nothing of PMID 42422765. I did no repository search and used no network.

**Failures:** one context `grep` failed on a pattern-complexity limit. I replaced it with a Python script.

**Side observation, affects no verdict:** the paper is internally inconsistent on activation shifts. The Fig 3 caption gives 6.6 mV (I1306T) and 5.9 mV (M1425I), while the text gives 14.5 and 13.7 mV, matching Supp Table S3. For I860N the text says 15.5 mV, but the Table S3 means differ by 16.5 mV.

**Disk:** about 0.85 MB written under `/home/desktop/.claude/jobs/fc428159/tmp/b2r2blind/` and `b2r2blind_scripts/`; both are deleted. No repository file was written. Free space on `/` was 2.6 GB at the start and 1.2 GB at the end. My files do not account for that drop, and it is close to the 1.0 GB floor, so check it before further conversions.
