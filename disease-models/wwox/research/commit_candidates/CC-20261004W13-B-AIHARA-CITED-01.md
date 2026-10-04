# CC-20261004W13-B-AIHARA-CITED-01 - PMID 41257285 re-read: the "cited, not measured" chain survives every surface; "seronegative-only" is not the paper's wording; the capsid-versus-expression toxicity attribution is cited to two reviews, and the paper's own RNA-seq counts qualify its "minimal impact" abstract sentence for promoterless vector in liver and muscle

`context_policy: QUESTION_DRIVEN` (re-read of owed figures and supplements, intake wave 13, 2026-10-04, Scientist B). **Not medical advice. WWOX occurs zero times in the source.**
**Change class: MINOR.** PAPER 179 is a corpus record; no `consolidated baseline` claim is narrowed or reversed. (If the integrator judges the promoterless qualification to touch a baseline sentence of the working model, it is MAJOR and the blind-audit triples below apply; this candidate does not edit any such sentence.)
**Target records:** `disease-models/wwox/registries/paper_registry_current.md` `PAPER 179` (three `replace-within` ops on its Role field).
Receipt: `FTR-20261004-41257285-02` (prepared, not recorded) - manifest PASS (16 locators, 24 artefacts; the five previously waived blocks are now filled) - dossier part 2.

## 1 - The negative tested (FIND-X)
"The NfL correlation, the histopathology and all in-life toxicity are CITED to the authors' prior report, not measured here." Surfaces searched (NfL, neurofilament, histopath*, necrosis, ALT, AST, creatine kinase, in-life, clinical chem*, immunosuppress*, glucocorticoid, prednis*, dexameth*, neutraliz*, ELISpot): running text; Figures 1-8; Figures S1-S6 (captions, and S1-S4 as rendered pages); Table S1 cell-wise; Tables S2-S12 string tables; Document S2 text. **The negative survives.** Not read row by row: Tables S2-S12 (RNA-seq results); Figures S5-S6 pixels. Table S1 is a design table with no clinical-sign, chemistry, NfL or histology column, though the Results sentence on in-life tolerability points to it.

## 2 - Measured details
- Methods: animals "preselected based on their total anti-AAV9 antibody titers. Animals with the lowest titers were included" - no titre, cut-off or seronegativity statement.
- The toxicity attribution "Hepatic and DRG toxicities were only detected after administration of full AAV9 viral particles, but not empty capsids or Promoterless test articles" carries references 8 and 14 (two reviews), not a primary.
- RNA-seq DEG counts (raw P < 0.05, |log2FC| > 1, four females per arm), up / down: DRG promoterless 78 / 85 (full 383 / 50 and 374 / 29, empty 25 / 22); liver promoterless 286 / 573 (full 504 / 539, empty 279 / 180); skeletal muscle promoterless 305 / 143 (full 272 / 127, empty 104 / 33); heart promoterless 121 / 144 (full 196 / 135, empty 76 / 70). The abstract's "across all tissues considered, the impact of empty capsids or of the Promoterless vector was minimal" is qualified for promoterless in liver and muscle.
- Selection-title premise: "12-month" is an age (study B 12-17 months; study A 27-33 months); both studies last 4 weeks (Table S1).

## 3 - Ops (record-scoped, PAPER 179 Role)
### Op 1 - `replace-within`
- `old` (verbatim, measured unique in the file): `are CITED to the authors' prior report, not measured here`
- `new`: `are CITED to the authors' prior report (reference 10 in the Results paragraph; reference 11 is the NfL primary) and are not measured here: Table S1 is a design table with no clinical-sign, chemistry, NfL or histology column, and no figure or supplement carries such a panel (the neurofilament-light gene transcript in the DRG RNA-seq is a different quantity)`

### Op 2 - `replace-within`
- `old` (verbatim, measured unique in the file): `Female-only, seronegative-only;`
- `new`: `Female-only (four per group, 40 in all); preselected for the LOWEST anti-AAV9 titres, with no titre, cut-off or seronegativity statement printed;`

### Op 3 - `replace-within`
- `old` (verbatim, measured unique in the file): `not with empty capsids and not with a promoterless genome at comparable capsid dose.**`
- `new`: `not with empty capsids and not with a promoterless genome at comparable capsid dose** - an attribution the paper cites to two reviews (references 8 and 14) and does not measure; its own RNA-seq counts (raw P, four females per arm) show promoterless DEG counts of 78 up and 85 down in DRG but 286 up and 573 down in liver and 305 up and 143 down in skeletal muscle, against 504 and 539, and 272 and 127, for the full vector in study B, so its abstract's "minimal" impact holds for empty capsid and DRG and is qualified for promoterless in liver and muscle.**`

## 4 - Defaults taken
- No edit to the sentence on interferon/JAK-STAT or on the tension with PAPER 182; not re-tested.
- The DRG NEFL and ATF3 transcript values (Table S7) are in the dossier with their limits and are not carried into the registry.

### LOCATOR TRIPLES FOR BLIND AUDIT
- (Preselection on lowest anti-AAV9 titres, no seronegativity statement | Prior to study assignment, animals were preselected based on their total anti-AAV9 antibody titers. Animals with the lowest titers were included in the study. | Materials and methods, Animals, `files/fulltext/PMID41257285_Aihara2025_PMC.xml`)
- (In-life tolerability sentence points to Table S1 | was generally tolerated with minimal clinical signs observed | Results, In-life summary and organ toxicities, `files/fulltext/PMID41257285_Aihara2025_PMC.xml`)
- (Table S1 has design columns only | `[spreadsheet attestation]` Header: Study, Group, Test article, Route of Administration, Dose, Targeted Concentration, Age at Injection, Study Duration, # of Animals, Sex | `files/supplement/PMID41257285/mmc2.xlsx`)
- (Abstract: minimal impact of empty capsid and promoterless across all tissues | across all tissues considered, the impact of empty capsids or of the Promoterless vector was minimal | Abstract, `files/fulltext/PMID41257285_Aihara2025_PMC.xml`)
- (Liver promoterless 286 up and 573 down | `[panel attestation]` Figure 3 panel E Promoterless: Down 573, Up 286 | `files/supplement/PMID41257285/gr3.jpg`)
- (Skeletal muscle promoterless 305 up and 143 down | `[panel attestation]` Figure S2 panel E Promoterless: Down 143, Up 305 | `files/supplement/PMID41257285/mmc1.pdf`)
- (DRG promoterless 78 up and 85 down | `[panel attestation]` Figure 2 panel E Promoterless: Down 85, Up 78 | `files/supplement/PMID41257285/gr2.jpg`)
