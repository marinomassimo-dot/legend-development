FIRST READER REPORT, Record 5, PMID 41210171 (Vono 2025, PAPER 178, consumer DL-METH-118). Date 2026-11-26. Hypothesis-level reading, not medical advice.

Overall: no statement is WRONG as written. Of 15 judged units: 4 CORRECT, 9 ADD, 1 ADD and AMBIGUOUS-SOURCE, 1 NOT ASSESSABLE. Three ADDs are borderline MUST-CHANGE candidates for the blind reader (section 3).

Vono facts used throughout (full text, XML lines named "L" refer to my plain-text conversion vono_struct.txt of the held XML):
- Animals and groups: 15 female cynomolgus macaques (Mauritius), about 41 months, no immunosuppression. 12 got scAAV9-CBA-mCherry (3 groups of n=4: low, medium, high pre-existing anti-AAV9 TAb). 3 got vehicle (TFF3 buffer, same volume). Methods L76 and L82.
- Dose and route: 1.2 x 10^13 vg/animal in 1.2 mL (nominal 1 x 10^13 vg/mL, actual 9.8 x 10^12). Single intrathecal injection by lumbar puncture at L5-L6 (L85). Computed: 9.8 x 10^12 x 1.2 = 1.18 x 10^13 vg.
- Timing: dosing day 1, necropsy 4 weeks post-dose (L36, L55). Last serum and CSF titre sample day 30.
- Antibody type: binding total antibody (bridging ECLIA, "TAb"), not neutralizing antibody. Assignment used day -9 or day -14 titres.

## (1) Table of units

| ID | Verbatim statement | Verdict | Grounds and locator |
|---|---|---|---|
| R5-S01 | "In a second, independent NHP study" (step 2) | NOT ASSESSABLE for "second, independent"; "NHP" is correct | The step-1 study is not in my scope, so independence from it cannot be judged. Vono is cynomolgus macaque, "15 female cynomolgus macaques (Mauritius)" (L76). |
| R5-S02 | "the only quantified histopathology shows meningeal mononuclear infiltrate in two of three vehicle animals" | ADD (the count is correct) | Figure 6C (held render, read by eye at 3x): "Brain / Infiltrate, mononuclear cell, meninges / Number examined 3 / Total number affected 2 / Minimal 2 / Slight 0 / Moderate 0" for group 1 (vehicle). Caption: "Summary of the incidence and severity of scAAV9-CBA-mCherry-related microscopic findings in the brain (C)". "Only quantified" is supported (searches in the Negatives box below). The statement omits sex, dose, route, timing and the treated comparison. See the full recomputation below. |
| R5-S03 | "while the running text classes that lesion among test-article-related findings" | ADD | L59: "Test-article–related microscopic findings ... included mononuclear cell infiltrate, neuronal degeneration, axonal degeneration, and gliosis in the brain, intrathecal injection site, spinal cord, cauda equina/spinal nerve roots, and/or DRG". Same paragraph: "In the brain, there were trends toward increased severity of mononuclear cell infiltration in the meninges and/or perivascular region ... compared with control animals". Fig 6B caption: "Top: minimal severity in a control animal". L62: "increased incidence of mononuclear cell infiltration in the brain of AAV9-treated animals". The authors know controls show the lesion. What they class as test-article-related is the increase (incidence 12/12 vs 2/3; severity), judged non-adverse. "While" implies an inconsistency the authors do not commit. |
| R5-S04 | "That same study reports DRG lesions in prose keyed to a representative photomicrograph" | CORRECT | L59 names DRG among test-article-related findings and cites "(Figure 6A)". Fig 6A caption: "Representative photomicrograph ... Top: DRG (sacral): neural and axonal degeneration that accompanied mononuclear cell infiltration in the ganglia, nerve root, and perineurium/fascia". Add: the DRG image is labelled group 3 (one animal, sacral level, read by eye from the panel label). No vehicle DRG image is shown. |
| R5-S05 | "with no incidence and no control comparison **for that tissue**" | CORRECT (scope: histopathology) | Negative searches are in the Negatives box. The DRG-specific negative holds in all held text and the supplement. Add: the vehicle group does appear in DRG vector-genome biodistribution (Fig 2 caption: "values below the LOQ, such as with the vehicle group"). Fig 2 is not held as an image. That is vector load, not histology. |
| R5-S06 | "the article does give a qualitative severity range (*«mostly minimal to slight … with high individual variabilities»*)" | ADD | The quote is verbatim (L59). The sentence covers all listed tissues together (brain, injection site, spinal cord, cauda equina/roots, DRG), not DRG alone. Treated brain meninges (Fig 6C) reach moderate in 1 of 4 high-titre animals, so "minimal to slight" is not a DRG range. |
| R5-S07 | "does tabulate incidence and severity, but **for brain only**" | CORRECT (with ADD) | The XML has no table-wrap and no `<table` (0 hits). The only incidence/severity table is image panel 6C, headed "Brain". It has only two finding rows: mononuclear infiltrate in meninges, and in neuropil/perivascular. It has no brain neuronal degeneration, axonal degeneration or gliosis row, although L59 lists those findings (the list spans tissues). The supplement has no histopathology. |
| R5-S08 | "the absence is DRG-specific, not article-wide" | ADD (borderline) | "Not article-wide" is right: brain is tabulated. "DRG-specific" over-narrows. The same absence holds for spinal cord, cauda equina/nerve roots, intrathecal injection site and heart, all named as findings (L59; heart in L71 only). It is "every tissue except brain". |
| R5-S09 | "Its methods confirm DRG at four spinal levels were sectioned and stained" | CORRECT | L95: "Paraffin-embedded tissues (brain, spinal cord [cervical, thoracic, and lumbar], intrathecal injection site, cauda equina/nerve root, DRG [cervical, thoracic, lumbar, and sacral], liver, and heart) were routinely processed, sectioned, and stained with hematoxylin and eosin (H&E). Macroscopic and microscopic examinations were conducted by ... ACVP-board-certified veterinary pathologists". |
| R5-S10 | "so the unreported data were generated" | ADD | This is an inference. Methods list the tissues and say examinations were conducted. They do not say that all four DRG levels were graded in each of the 15 animals, or in the vehicle group. Generation is likely but not stated at animal or group level. |
| R5-S11 | "The lesion is explicitly stated by one of these studies to occur independently of pre-existing anti-capsid antibody titre, so it is not the pre-existing-immunity component." (AMBIGUOUS-SOURCE: Vono is the only pre-existing-immunity paper I can see; I judge what Vono shows.) | ADD | The explicit statement is in a legend: Fig 6A, "findings observed in animals across scAAV9-CBA-mCherry-administered groups without impact of pre-existing AAV9-Ab titers". The Discussion "independent of the pre-existing AAV9 antibody titers" (L71) is grammatically attached to "minor liver and hematology perturbations", with the microscopic findings listed earlier in the same sentence. No DRG incidence by titre group is given; the DRG image comes from one group-3 animal. The same article reports a titre trend for brain infiltrate (L59; Fig 6C: group 4 moderate, 1 of 4) and reduced DRG vector load in high-titre animals (L39, L65; Fig 2 not held). Titre bands: antibody is binding TAb; groups are small (n=4); day-1 low and medium groups overlap (Table S1: group 2 <20 to 320, group 3 <20 to 640; P0202 was <20 on day 1); only group 4 is clearly separate (20,480 to 327,680). The vehicle group had pre-dose titres 20, 1280 and 640 (Table S1). "Not the pre-existing-immunity component" goes beyond a legend assertion without DRG data. |
| R5-S12 | "Where a concurrent-control incidence is reported, it has been of the same order as the treated incidence in the studies cited in this chain" (AMBIGUOUS-SOURCE; judged for Vono) | ADD | In Vono the only reported concurrent-control incidence is brain, not DRG: meninges vehicle 2/3 vs treated 12/12; perivascular vehicle 0/3 vs treated 3/12 (Fig 6C). For DRG, Vono reports none. So Vono is not an example of a same-order DRG control incidence. Its brain numbers are same order for meningeal incidence (67% vs 100%) but not for severity (vehicle all minimal; treated 3 slight and 1 moderate). |
| R5-S13 | "where it is not reported — the common case — the attribution to the vector is not established by the paper making it" | ADD | Vono is an instance: it attributes DRG findings to the vector ("Test-article–related", L59) and shows no DRG vehicle data. "Not established by the paper" means "not shown in the article". The authors compared against a concurrent vehicle group (n=3) whose DRG histology is not shown, so their attribution may rest on an unreported comparison. |
| R5-S14 | "control arms of n = 3 and n = 4" (n = 3 part) | CORRECT | Vono vehicle group n=3 females (L76, L82; Fig 6C "Number examined 3"). The n=4 part belongs to another paper. |
| R5-S15 | "none of the sources mentions WWOX" (Vono part) | CORRECT | Searched 2026-11-26. Case-insensitive "wwox" gave 0 hits in the Vono XML text and 0 in the supplement text. |

Statements excluded, with reasons:
- Step 1 (40% overall, 2/4 saline controls, Figure 5A caption): another study, not Vono.
- Step 5 (human CLN7 and intracisternal reports): not Vono.
- Causal sentence 1, "Minimal-to-mild DRG lesions occur in vehicle-dosed cynomolgus macaques at a rate high enough ...": rests on the step-1 study. Vono reports no vehicle DRG data, so it neither supports nor contradicts it. Anyone citing Vono for it would have no support.
- The PMID 35229008 sentence ("not in a further one ... vehicle 1/4 against 3/4 to 4/4", grade >= 2 threshold), the Buss appends (lines 3723, 3730), the "convergence" paragraph, and the Null and promoterless limbs: Buss. Vono's cassette is a CBA-promoter expressing cassette with one dose and no empty-capsid or promoterless arm, so it cannot speak to capsid versus expression.
- Lines 3728 and 3729 (PMIDs 41257285 and 37515322, Aihara) and the "Transfer limit" and "falsifying experiment" blocks: other papers or generic design.
- Counter-evidence on regulatory holds and human adults: other sources.

Recomputed counts, Figure 6C (held render, cynomolgus, unit = animal, females only, read by eye at 3x upscale; every row sums):

| Row | G1 vehicle (n=3) | G2 (n=4) | G3 (n=4) | G4 (n=4) | Treated pooled (n=12) |
|---|---|---|---|---|---|
| Brain, meninges, total affected | 2 | 4 | 4 | 4 | 12/12 |
| Minimal | 2 | 3 | 3 | 2 | 8 |
| Slight | 0 | 1 | 1 | 1 | 3 |
| Moderate | 0 | 0 | 0 | 1 | 1 |
| Brain, neuropil perivascular, total affected | 0 | 0 | 2 | 1 | 3/12 |
| Minimal | 0 | 0 | 2 | 1 | 3 |

- Meninges check: G1 2 = 2+0+0; G2 4 = 3+1; G3 4 = 3+1; G4 4 = 2+1+1.
- Perivascular is minimal only, and not monotonic in titre (G2 0, G3 2, G4 1).
- Vehicle fraction 2/3 = 67%.
- Figure 6D (CSF IL-12p40) is not used for any judged statement.

Negatives box. Every negative below is a search I ran on 2026-11-26. I derived `vono_struct.txt` from the held XML; supplement text came from `pdftotext`, and I also looked at all 8 supplement pages as images. Each keyword was searched alone.
- Query "DRG" on `vono_struct.txt`: 8 hits. I read every context (L38, 39, 59, 61, 65, 71, 95). None gives a DRG incidence count or a vehicle DRG finding.
- Query "incidence": 3 hits. L56 is clinical observations ("comparable with incidences as controls"), L61 is the Fig 6C caption (brain), L62 is brain infiltrate. None concerns DRG.
- Queries "<table" and "table-wrap" on the raw XML: 0 hits each.
- Supplement PDF, 8 of 8 pages viewed: Figure S1 (T-cell gating), Figure S2 (ALT/GLDH), Tables S1 to S3 (serum and CSF titres). No histopathology.
- "WWOX" and "promoterless": 0 hits each in the text.
- "ganglion": 0 hits.

## (2) Corrected sentences (every ADD; none is WRONG)

- R5-S02: "In a second NHP study (Vono 2025: 15 female cynomolgus macaques; one intrathecal lumbar dose of 1.2 x 10^13 vg scAAV9-CBA-mCherry in groups 2 to 4, n=4 each, or vehicle, n=3; necropsy at 4 weeks) the only quantified histopathology, Figure 6C, covers brain only and shows meningeal mononuclear infiltrate in 2 of 3 vehicle animals (both minimal) against 12 of 12 treated animals, and perivascular infiltrate in 0 of 3 vehicle against 3 of 12 treated."
- R5-S03: "The running text classes mononuclear infiltrate among test-article-related findings and describes a trend to greater severity and incidence than in controls (control infiltrate minimal), considered non-adverse; it does not class the vehicle animals' infiltrate as test-article related."
- R5-S06: "The article gives one pooled qualitative range for all listed tissues, 'mostly minimal to slight in severity with high individual variabilities', and none specific to DRG."
- R5-S07: "Incidence and severity are tabulated only in image panel 6C, for brain only and for two findings (meningeal and perivascular mononuclear infiltrate)."
- R5-S08: "The absence of incidence and control data applies to every tissue except brain (DRG, spinal cord, cauda equina/nerve roots, injection site, heart), not to DRG alone."
- R5-S10: "Its methods list DRG at four levels (cervical, thoracic, lumbar, sacral) as processed, sectioned and H&E stained and examined by board-certified pathologists; per-animal and per-group grading of those levels is not stated."
- R5-S11: "The figure 6A legend states that the representative findings (DRG, nerve root, spinal cord) were observed across the vector groups without impact of pre-existing anti-AAV9 total-antibody titre, but no DRG incidence by titre group is given (n=4 per group, overlapping low and medium bands; the DRG image is from one group-3 animal), brain infiltrate in the same article trends with titre, and DRG vector load was lower in high-titre animals."
- R5-S12 (Vono): "In Vono the concurrent-control incidence is reported for brain only (meninges 2/3 vehicle vs 12/12 treated); no DRG control incidence is reported."
- R5-S13 (Vono): "Vono attributes DRG findings to the vector without showing the DRG findings of its vehicle group, so the attribution is not shown in the article."

## (3) Strict candidates (WRONG as written)

None. Borderline items for the blind sentence-level reader. They are not WRONG on facts, but the wording may draw MUST CHANGE:
- R5-S08, "DRG-specific".
- R5-S03, the "while" connector, which implies an inconsistency the authors do not commit.
- R5-S11, "explicitly stated ... so it is not the pre-existing-immunity component".

## (4) ADDs no consumer holds that matter

- The vehicle animals carried pre-existing anti-AAV9 TAb: serum 20, 1280 and 640 on day 1 (Table S1). The vehicle group is not seronegative, and the two vehicle animals with meningeal infiltrate are not identified in any held file.
- Day-1 titre bands overlap: group 2 <20 to 320, group 3 <20 to 640. The text says two group-2 animals reached medium-range titres before dosing (Table S2).
- The cargo is an expressing CBA-mCherry vector at one dose (1.2 x 10^13 vg), 4 weeks, females only. There is no promoterless or empty-capsid arm, so the capsid-versus-expression question is not addressed.
- DRG vector genomes were reduced in high-titre animals (L39, L65), while the representative DRG lesion is called titre-independent. Dose is not varied, so the study cannot speak to dose.
- Heart microscopic findings are mentioned only in the Discussion (L71) and are not quantified.
- The correction notice PMC13148915 (Mol Ther Adv, 2026) corrects only a missing space in the title. It has no effect on the content.
- One group-3 animal got a slightly lower dose (L28, from Figure 1A, which is not held as an image).
- The study had split cohorts (pre-dose day -9 vs day -14).

## (5) What I opened, could not read, failures

Opened and read in full:
- The consumer text from "## Record 5" to the end, and the "## Matching rule" section of PREREG.
- PAPER 178 in the registry (about 21 lines), used as a mapping aid only.
- The complete held full text XML: all captions, Methods and Discussion.
- The supplement PDF, all 8 pages (text and images).
- The Figure 6 render (759x739), viewed myself, with panel C enlarged to 1320x780.
- The notice XML PMID41210171_notice_PMC13148915.xml (found by file name).
- `framework/protocols/delegation_budget.md` through the Read tool.

Held-source search results:
- File-name search of files/ for "41210171", "PMC12590263" and "Vono": only the three named held files plus the notice XML.
- PDF text search: 707 of 714 PDFs under files/ by `pdftotext`. The 7 not scanned were excluded by a file-name filter that avoids Obeid/42422765 material. Hits: "41210171" and "PMC12590263" in none; "Vono" in the Vono supplement and in one other supplement PDF under the Amaral 2026 folder (mmc3.pdf). I did not open that other file; it is not the Vono article. Image-only PDFs would not be detected by this method.
- No article PDF or Figures 1 to 5 images are held for PMID 41210171.

Unread, exactly:
- The pixel content of main Figures 1 to 5. Only their captions and the text citing them were read. Their captions concern design, titres, vector-genome biodistribution including DRG, T cells and cytokines, not histology, but Fig 2A values for DRG and vehicle were not seen.
- The histology images in Fig 6A and 6B. At 759x739 they are not gradeable, and I did not grade them.
- The published article PDF layout.

Failures and cautions:
- One Bash call to grep `delegation_budget.md` headings was denied by the auto-mode classifier. I used the Read tool for the same file instead.
- Fig 6C numbers are read by eye from a 759-px-wide JPG render. Every row sums, but they are not machine-read.
- Group-3 labelling of the Fig 6A DRG image is read by eye from a rotated panel label.
- The XML contains a corresponding-author e-mail address. I did not copy or use it anywhere.
- No network access, downloads or repository writes, and Obeid/PMID 42422765 was never opened. Scratch files are in /home/desktop/.claude/jobs/8fe7aef9/tmp/rec5/ (scripts in /home/desktop/.claude/jobs/8fe7aef9/scripts/).
