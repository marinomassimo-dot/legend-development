# Intake wave 7 (2026-10-04), Scientist C2 — restoration-spec increments from three off-gene papers

`context_policy: SOURCE_FIRST` for the first pass of each paper; the comparison with earlier waves
(section 3) was written after the three dossiers. Nothing here is medical advice.

Papers (all peer-reviewed journal articles, none a preprint; WWOX occurs zero times in all three,
counted over each JATS body, so each is an earned null for the gene):

| PMID | Subject | Dossier | Manifest |
|---|---|---|---|
| 42511902 | four IV AAV capsids, neonatal wild-type mouse, eGFP | `fulltext_dossiers/PMID42511902.md` | `deepdive_manifests/PMID42511902.json` |
| 41134821 | DRG MRI as endpoint in a Fabry mouse, AAV9-GLA | `fulltext_dossiers/PMID41134821.md` | `deepdive_manifests/PMID41134821.json` |
| 42137291 | CSF-route AAV9 micro-dystrophin, mouse and NHP package | `fulltext_dossiers/PMID42137291.md` | `deepdive_manifests/PMID42137291.json` |

All three manifests validate (`deepdive_manifest.py --pmid N --verify-artifacts --require-current-schema`: VERDICT PASS).
Reading depth is `partial_fulltext_read` for each: figure panels were not inspected and supplements were not fetched (details in each dossier).

## 1 · What the selection note said, tested against the sources

| Selection sentence | Result |
|---|---|
| 42511902: "four capsids, one age, systemic route, CNS and PNS readouts ... no immune arm" | Correct. One dose, one age (P2), one harvest (P30); no immune arm, and the authors list that absence. The "treat before the window closes" question is not tested: there is no older arm, so no capsid preference can be tied to a window. |
| 41134821: "response to AAV treatment conflates benefit and injury in one number" | Wrong in its premise. The AAV effect is a normalisation of a storage-driven enlargement (DRG gets smaller toward wild type), with H&E, LAMP1, MPZ and hot-plate corroboration; it never measures vector injury. Nothing in the design could register a vector-induced lesion: there is no wild-type AAV-injected group. The title word "response" is therapeutic response only. |
| 42137291: "cargo is a secreted-irrelevant muscle protein" | Imprecise. Micro-dystrophin is intracellular, not secreted; the relevant fact is the muscle-derived MHCK7 promoter, which means DRG saw vector genomes without transgene RNA. "Closest process analogue" holds for document shape (dose levels, GLP mouse and NHP, DRG evaluation, shedding) only. |

## 2 · Findings per paper (class-level, transfer limit stated)

**42511902.** Wild-type neonatal mouse, IV temporal vein at P2, 1E10 vg per pup (authors' conversion about 5E12 vg/kg), CMV-eGFP, harvest at P30.
Capsid-specific tropism: AAV9 and MacpnS1 give wide CNS, DRG, heart and liver transduction; rAAV2-retro is confined to medulla and spinal motor neurons; PHP.eB is broad but depends on Ly6a and has no primate counterpart (authors).
DRG: AAV9 and MacpnS1 high, retro and PHP.eB 4- to 6-fold lower, by reporter intensity only. Liver: serum ALT and AST raised only with MacpnS1 at day 28 (single time point); the Results text says this does not establish hepatotoxicity, the Discussion calls it acute liver injury.
Internal inconsistencies worth carrying: stated injected volume 2 uL (Methods 2.1) against a ~22 uL mixture (Methods 2.2); n "at least four" against n = 6 and n = 8 in legends.
Transfer limit: wild-type neonatal mouse with a reporter; capsid ranking by eGFP intensity is not a restoration dose, not a window, and not a WWOX safety datum; IV is not the CSF route; mouse-to-human gestational age is an assumption the paper does not make.

**41134821.** A 7 T L4 DRG cross-sectional-area (CSA, maximum-intensity projection) endpoint; repeatability in five wild-type mice ICC 0.9, limits of agreement -0.060 to 0.066 mm2 on a mean of 0.257 mm2
(Table 2, extracted cell-wise). Fabry DRG about 25 % larger than wild type at 24 weeks (0.35 vs 0.28 mm2); AAV9-GLA at 6.25E12 vg/kg IV at 8 weeks: no difference from wild type at any time, smaller than untreated Fabry from 16 weeks.
Group sizes disagree (Table 1: 3, 5, 5; Results: "fifteen Fabry mice"; Methods: thirteen). The method was built for an enlargement lesion; its sensitivity to atrophy or neuronal loss is untested.
Transfer limit: a storage-lesion endpoint in a mouse; it does not supply a vector-injury endpoint, and mouse CSA does not carry numerically to human MRI. A DRG imaging endpoint for vector injury remains unmeasured in this corpus.

**42137291.** IND-directed package for a CSF-route AAV9 with a muscle-derived promoter. Efficacy in mdx from 2.0E+11 vg per mouse (ICV, about p28), plateau across doses attributed by the authors to treatment age.
GLP toxicology: wild-type mouse n = 45 per group, up to 8.0E+11 vg; NHP n = 3 per dose, up to 3.05E+14 vg, lumbar IT, 3 months; both NOAELs equal the highest dose tested, set by feasibility.
Mouse DRG: "healthy cells and normal histopathology" (one image, Fig 8E legend). DRG held vector genomes (mouse 6.408 vg/dg at 12 weeks, high dose) but no transgene mRNA or protein.
Immune: anti-AAV9 antibodies in all treated NHP by day 28; T-cell responses, CSF cell counts reported as without effect (methods and supplement unread); NHP pre-screen excluded titres above 1:50; no immunosuppression regimen described.
Dose translation: CSF-volume scale-up of 250 (0.04 to 10 mL); 8.0E+11 vg in mouse = 2.0E+14 vg in NHP (authors).
Transfer limit: muscle promoter means DRG, brain and cord safety here is genome presence plus capsid and procedure, not neuronal transgene expression; wild-type juvenile males; CSF-volume scaling is the authors' choice for a muscle target.

## 3 · Comparison with waves 3-6 (read after the first pass)

| Earlier record | What these sources do to it |
|---|---|
| `CC-20261003W3-C-RESTORATION-SPEC-01` (six parameters; route, off-target-organ-risk rows) | **Adds** an IV neonatal arm with named capsids to the route row (MacpnS1 and AAV9 reach DRG; retro and PHP.eB do not), and a muscle-promoter CSF package with a DRG evaluation to the off-target row. **Leaves untouched** the window row: no source here measures an age contrast (42511902 has one age). |
| `CC-20261003W5-A-WINDOW-STATUS-01` (window negative stands) | **Untouched.** 42511902 does not meet the revival trigger (no expression-matched age comparison); it is a one-age atlas. |
| `CC-20261003W5-C-DRG-ATTRIBUTION-01` (lesion requires a productive cassette; empty capsid and promoterless constructs produce none) | **Bounds, consistent in direction, weakly.** 42137291 has NHP and mouse DRG vector genomes without mRNA and no reported DRG lesion, but the NHP DRG-specific result is a general "histopathology" statement, n = 3 per dose, supplement unread. It cannot separate transcription from capsid dose and does not touch the immune-versus-dose question. |
| `CC-20261003W6-C-DRG-ATTRIBUTION-01` (mononuclear infiltrate at every dose in every no-immunosuppression study; degeneration above a threshold) | **Possible exception, unresolved.** 42137291 used no described immunosuppression and reports no DRG finding in NHP at up to 3.05E+14 vg per animal; the one DRG-specific text sentence is about mice. Whether NHP DRG infiltrate was graded and found absent cannot be read from the body. Do not count it as a counterexample until Table S5 and Fig S7 are read. |
| `CC-20261003W6-C-IMMUNOSUPPRESSION-LIMIT-01` | **Untouched.** No immunosuppressed arm exists in any of the three. |
| `CC-20261003W5-A-TRANSGENE-IMMUNITY-01` (CRIM-negative host untested in IND packages) | **Adds a second instance.** The only immune readouts in NHP are in wild-type animals expressing dystrophin; mdx (dystrophin-null) mice show reduced muscle CD8 and CD68 cells, n = 4, not significant. The DMD Introduction itself names immunogenic epitopes and immunosuppression as the open risk. |
| `CC-20261003W5-C-DOSE-SCALAR-01` (three non-convertible scalars) | **Adds two uses.** (a) A CSF-volume scalar of 250 (0.04 to 10 mL), an independent compilation point against the 371- and 375-fold values already held, here with a juvenile NHP CSF volume of 10 mL (not 15). (b) Per-body-weight scalar for neonatal IV (about 5E12 vg/kg, authors' conversion) and, in the same paper as the NHP per-animal totals, animals of different weight (1-2 kg GLP; 2-4 kg non-GLP) so one per-animal total is a different per-kg dose (INFERENZA arithmetic, in the dossier). |

## 4 · Where each paper stops saying anything about WWOX

All three at the first sentence: the word does not appear. The transferable questions are answered only in the narrow forms above.

## 5 · What would change the model, and what would falsify

- If Table S5 and Fig S7 of 42137291 show NHP DRG graded for infiltrate and found without it at 1E+14 vg or more under no immunosuppression, the W6 statement that the infiltrate appears at every dose in every non-immunosuppressed study needs a named exception and a promoter condition.
- If a DRG imaging endpoint (41134821's CSA or a successor) is run in a vector-injury model with a known histological lesion and detects it, the "endpoint" becomes an injury endpoint; the present paper cannot say it would.

## 6 · Not read

Figure image panels (all three), supplements of 41134821 (S1-S4) and 42137291 (Tables S1-S6, Figs S1-S8, video), and the references beyond retraction screening. Receipts therefore declare `partial_fulltext_read`.
