# CC-20261004W7-C2-DRG-GENOME-01 — a CSF-route AAV9 with a muscle-restricted promoter put vector genomes in DRG without transgene RNA and without a reported DRG lesion; a weak, bounded datum for "capsid load alone is insufficient"

`context_policy: SOURCE_FIRST` (first pass of PMID 42137291 written before waves 3-6 were opened; comparison afterwards)
**Date:** 2026-10-04 · **Author:** Scientist C2, intake wave 7 · **Change class:** MINOR
**Target records:** `disease-models/wwox/research/discovery_ledger_current.md` (append one lead)
Receipt: `FTR-20261004-42137291-01` (prepared, not recorded) · Manifest `deepdive_manifests/PMID42137291.json` (VERDICT PASS) · Dossier `fulltext_dossiers/PMID42137291.md`
**Nothing here is medical advice. WWOX occurs zero times in the source; this is an earned null for the gene and a transferable observation only.**

## 1 · What it adds to, bounds, and leaves untouched

- **Adds** to `CC-20261003W5-C-DRG-ATTRIBUTION-01` (the lesion requires a transcriptionally productive cassette): a second design in which the DRG received vector genomes and no transgene RNA, here by promoter restriction rather than by promoter scrambling.
- **Bounds** that addition: the NHP DRG-specific result is a general "histopathology" statement; n = 3 per dose; Table S5 and Fig S7 were not fetched; the mouse DRG evidence is one image (Fig 8E legend).
- **Leaves untouched** `CC-20261003W6-C-DRG-ATTRIBUTION-01` and `...IMMUNOSUPPRESSION-LIMIT-01`: the mononuclear-infiltrate-at-every-dose pattern is not tested here until the supplement is read, and no immunosuppressed arm exists.

## 2 · Op — discovery_ledger_current.md

`op: APPEND` one lead at the end of the lead list. No `old` text.

```
### DL-MECH-xxx (provisional) — A muscle-restricted AAV9 given into CSF reached DRG as genomes only: no transgene RNA, no reported DRG lesion in mouse; NHP DRG covered only by a general histopathology statement

**Tag:** INFERENZA
**Status:** open
**Created:** 2026-10-04 · intake wave 7, Scientist C2
**Causal statement:** In one sponsor package for a CSF-route AAV9 carrying a muscle-derived promoter, DRG tissue held vector genomes
(mouse 6.408 vg per diploid genome at 12 weeks, high dose) but no transgene mRNA or protein, and the mouse DRG was reported as healthy
cells with normal histopathology at the high dose; NHP (n = 3 per dose, up to 3.05E+14 vg per animal) showed no INS1201-related histopathology
in the general statement, and no transgene RNA in DRG or spinal cord. This is compatible with, but does not demonstrate, the proposal that DRG
harm needs a transcriptionally productive cassette rather than capsid or genome load alone.
**Reasoning chain:**
1. The construct uses the muscle-derived MHCK7 promoter; the authors state DRG showed vector genomes and an absence of mRNA.
2. Mouse DRG histology: "healthy cells and normal histopathology", one image from one high-dose animal.
3. NHP: no INS1201-related histopathology across organs; DRG-specific grading not printed in the body; mRNA not detected in DRG or spinal cord.
4. No immunosuppression regimen is described; anti-AAV9 antibodies were present in all treated NHP by day 28.
**Counter-evidence / what would refute this lead:** a DRG-specific NHP table (Table S5, Fig S7) showing graded mononuclear infiltrate or neuronal
degeneration at the tested doses would remove the observation; a mechanism by which the lesion arises from capsid-genome presence alone would make
promoter restriction irrelevant.
**Falsifying experiment:** the same capsid and dose with a neuronal promoter against a muscle promoter, DRG graded blind with concurrent vehicle controls.
**Transfer limit to WWOX:** a muscle target, wild-type juvenile male animals, a promoter that cannot drive neuronal expression. It says nothing about the
DRG safety of a neuronal WWOX cassette, whose DRG exposure and expression are the question.
**Not medical advice.**
```

### LOCATOR TRIPLES FOR BLIND AUDIT

- (DRG held many vector genomes but no transgene mRNA | although high numbers of vector genomes were identified in the DRG, there was an absence of INS1201 mRNA expression | Results, Biodistribution of INS1201 in WT mice and NHPs, `files/fulltext/PMID42137291_Thomsen2026_PMC.xml`)
- (Mouse DRG histology was normal at the high dose | a careful analysis of DRG tissue sections from mice in the high-dose group revealed healthy cells and normal histopathology | Results, Assessment of INS1201 toxicity, `files/fulltext/PMID42137291_Thomsen2026_PMC.xml`)
- (The DRG histology figure is one image from one animal | (image is from animal administered highest dose, 8.0E+11 vg) | Figure 8 legend panel E, `files/fulltext/PMID42137291_Thomsen2026_PMC.xml`)
- (NHP transgene RNA was not found in spinal cord or DRG | INS1201 mRNA expression was not detected within any region of the spinal cord or DRG or injection site in NHPs dosed with INS1201 or vehicle | Figure 8 legend panel C, `files/fulltext/PMID42137291_Thomsen2026_PMC.xml`)
- (NHP GLP design: three animals per dose, three vehicle | by lumbar IT injection (n = 3 per group); vehicle control NHPs (n = 3) were also included | Methods, Nonhuman primates, `files/fulltext/PMID42137291_Thomsen2026_PMC.xml`)


---

## BATCH DISPOSITION

**Verdict:** `PROPAGATED` by `BATCH_20261004_001` (2026-10-04, MINOR, WM_v7.13 → WM_v7.14; ACTOR_ID `scientist`, Scientist K, batch integrator).
**Surfaces written:** discovery_ledger_current.md

Created as **`DL-MECH-114`** in the discovery ledger; the candidate's op named a provisional `DL-MECH-xxx` and the integrator assigned the next free number (`DL-MECH-113` was the ceiling).
**Deduplication pass, as the dispatch required.** Measured against the landed `DIS-031`, `DL-METH-118`, `DL-METH-120`, `RL-C-20261003w4a` and `RL-C-20261003w6`, and against the wave-5 `DRG-ATTRIBUTION` candidate: **additive**. It is a second design in which the DRG received vector genomes and **no transgene RNA** — here by **promoter restriction** rather than promoter scrambling — and the record names the three records it does **not** supersede, because the mononuclear-infiltrate pattern is untested here until the supplement is read and no immunosuppressed arm exists.
The lead is written so it cannot be read as a demonstration: *«compatible with, and does not demonstrate»*. **Reading debt is declared on the record itself** — Table S5 and Figure S7 carry the DRG-specific macaque grading and were never fetched — rather than left implicit, which is what keeps the unread-premise check honest.
One integrator amendment from the blind audit: the efficacy plateau is offered by the authors as something that *«could be due to»* treatment age at p27–35, hedged three times in the source, and is recorded as a suggestion rather than an attribution.
