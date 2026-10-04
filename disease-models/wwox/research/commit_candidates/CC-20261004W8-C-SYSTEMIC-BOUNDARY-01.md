# CC-20261004W8-C-SYSTEMIC-BOUNDARY-01 — the systemic-dose boundary: primary behind the liver-UPR commentary, a fatal human case under sirolimus, and the liver load after ICV; wording checks and limits

`context_policy: SOURCE_FIRST`. **Author:** ACTOR_ID `scientist`, Scientist C of intake wave 8, 2026-10-04. **Change class: MINOR** (one research-line record; narrows no `consolidated baseline` claim). **Nothing here is medical advice.** WWOX occurs zero times in all three sources.
Sources: PMID 42137263 (`FTR-20261004-42137263-01`), PMID 42198847 (`FTR-20261004-42198847-01`), PMID 41438872 (`FTR-20261004-41438872-01`). All three manifests PASS. PMID 42198847 is described at class level only.

## 1 · Which carried statements now have a primary behind them

The wave-7 commentary on liver toxicity (PMID 42170349) is a commentary on PMID 42137263. Its statements, checked against the primary:

| Commentary statement (as recorded in `CC-20261004W7-C1-DRG-ATTRIBUTION-01`) | Primary | Verdict |
|---|---|---|
| Rats expressed the transgene less and lacked UPR induction; "strongly suggests" UPR tied to synthesis of the transgene product | Rat explanation is the authors' own (about tenfold lower transgene in rat liver, taken from the parent study), supported by correlation of transgene level with DDIT3 (r = 0.96) and CES1 (r = -0.89) across lobes and animals (Figure 2B, inspected) | **Holds in direction, wording stronger than the primary.** The primary's data are correlational, dose, expression and injury are collinear, no expression-null or dose-matched control arm; the statistical unit for fold changes is the lobe, four per animal, two animals per sex per dose |
| PERK-branch UPR magnitude associated with transgene expression, pro-apoptotic genes induced | Holds (PERK arm genes up at 5e13 vg/kg and above; ATF6 and IRE1-XBP1 not seen, shown as "data not shown") | **Holds**, with the not-shown limb |
| Vector DNA presents break-like ends; p53-type response | DNA-damage/p53 signature present already at the lowest dose and in rats | **Holds**; this arm is expression-independent in the primary's own framing, and is the one signature seen at every dose |
| Dose-related DRG toxicity is lower when transcriptional activity is lower | Not in this primary (liver, systemic, day 4) | **No primary behind it here**; the nearest support is PMID 35229008 (expression-null control without lesion) |
| Immune activation as an initiating step | Innate signature (TNF, IL1B, CXCL8, interferon-stimulated genes) at high dose; low dose shows an interferon/T-cell signature; histology in the parent study showed only mild infiltration at day 4 | **Holds as innate activation; says nothing about adaptive T-cell causation** (authors infer T-cell mediation unlikely at this early time) |

What is new against held records: the three-mechanism **dose ordering in primate liver** (p53/DNA damage and interferon response at the low dose, pro-apoptotic UPR and loss of hepatocyte identity only at 5e13 vg/kg and above, innate cytokines rising with dose), with the vector being AAV9-PHP.B-SMN1 **intravenous**, day 4, n = 2 per sex per dose.

## 2 · The human boundary (PMID 42198847), class level

One adolescent with advanced disease, intravenous AAV9-CAG with a human enzyme ORF at 2.2e14 vg/kg under prednisolone plus sirolimus begun a week earlier, no neutralising antibodies but a low total anti-capsid IgG: fever and raised D-dimer and liver enzymes days 3-4, complement (soluble C5b-9 above 1,650 against normal below 300) on day 5, cardiogenic shock day 5, death after withdrawal of care on day 8. Autopsy: acute circulatory failure, no myocarditis, no thrombotic microangiopathy. Retrospective cytokines showed a pre-existing inflammatory state. Vector copies per diploid genome about 7,700 in liver against 14 to 493 in CNS (Figure 3B, inspected); enzyme protein above donor controls in liver, spleen, heart, adrenal and at or below endogenous in several CNS regions at day 8.

- **What it adds** (not held): the first fatal human high-dose systemic AAV9 case with a **named immunosuppression regimen** and a measured lack of protection against the early innate phase; the authors say sirolimus "did not appear to mitigate early immune response", consistent with an adaptive-immunity drug acting on an innate/complement-mediated process.
- **What it cannot give**: a dose-risk function (one patient, one dose), a counterfactual, or separation of vector effect from disease inflammation and a recent bronchial congestion (the authors say these "remain difficult to disentangle").
- **Contrast** with PMID 42137263: the monkey liver data were interpreted by their authors as largely cell-intrinsic, the human case by its authors as innate/complement; both say immunity alone does not explain the severe early phase, and neither tests an intervention.

## 3 · The route and capsid boundary (PMID 41438872)

AAV-PHP.eB gives about five-fold higher cortical neuronal labelling than AAV9 after ICV in juvenile pigtail macaques (n = 3 per capsid; statistics over regions of interest) and about 1.5-fold in spinal cord. It measures **no toxicity endpoint**: no DRG examination, no liver enzymes (their own stated limitation), only necropsy histology with no finding. It does add that after ICV, liver vector genomes were about 100 to 250 per diploid genome in both capsid groups, about 100 times heart, kidney or muscle, with no capsid difference (Figure 5B, enlarged and read; panel agrees with text). So the selection note's idea that a more efficient capsid might lower the dose and shrink the dose-driven arm is **not testable from this source**: no dose-titration, no toxicity read-out. The rodent receptor mechanism for PHP.eB is absent in primates (authors).

## 4 · Transfer limits

PMID 42137263: liver, IV, PHP.B capsid, SMN1 cargo, cynomolgus, day 4, reanalysis of an earlier dataset. PMID 42198847: single fatal case, IV, adolescent, advanced disease. PMID 41438872: juvenile male pigtail macaque, ICV, nuclear reporter under a neuronal promoter, six weeks, n = 3. None addresses a CSF-delivered WWOX programme, a WWOX cassette or an infant. The CSF-route DRG question is not touched by any of the three.

## 5 · Ops (provisional)

### 5.1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record after the current final research-line record) |
| record | `RL-C-20261004w8c3 — Systemic-dose boundary: primate liver pathway ordering by dose, a fatal human high-dose case under sirolimus, and the liver vector load after ICV` |
| status | `open` |
| tag | `INFERENZA` (readings `DATO`) |
| body | §1 to §4 of this candidate verbatim |
| class | MINOR |

## 6 · What would change this

- **Strengthen:** a monkey study with a dose-matched expression-null or lower-expression arm showing the UPR and hepatocyte-identity signature absent while the p53 signature remains; or a second human systemic case series reporting complement and cytokine values at day 5.
- **Falsify the "expression drives UPR" reading:** the same UPR signature in the Null-genome arm at matched dose.

## 7 · Brief premises tested

- "Liver, not CNS or DRG": confirmed. "Toxic, high-dose AAV" without a vector name hid that the vector is an AAV9-PHP.B capsid given intravenously; the selection's "CSF-route" framing does not apply.
- "No toxicity endpoint named" for PMID 41438872: confirmed, and DRG are never mentioned.

### LOCATOR TRIPLES FOR BLIND AUDIT

Format: `(proposition | verbatim quote | anchor)`. Each artefact is on disk and each quote was verified by the manifest validator against the artefact named for the PMID in brackets. Figure entries are attestations of panels read at native resolution, not string matches.

- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (The data are a secondary transcriptomic analysis of liver RNA-seq generated in an earlier toxicology study, not a new dosing experiment. | These RNA-seq data were originally used only for SMN1 transgene expression analysis | Materials and methods, para 1)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (The vector was an AAV9-PHP.B capsid carrying CBh-SMN1, given intravenously, in cynomolgus monkeys and rats. | of AAV9PHP.B-CBh-SMN1 (AAV-SMN1) intravenously | Materials and methods, para 1)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (Group size in the monkey dataset was two per sex per dose, one male fewer at the mid dose. | The cynomolgus dataset included 2 males and 2 females per dose, except for the male mid-dose group, which included only one animal. | Materials and methods, para 1)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (Fold changes and p values treat the four liver lobes of one animal as biological replicates. | Fold changes and p values were calculated considering the 4 lobes from each animal as biological replicates. | Figure 1 legend)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (Unfolded-protein-response activation was found only at doses of 5e13 vg/kg and above, while DNA-damage/p53 and innate signatures were also present at the low dose and in rats. | UPR activation was observed only in animals receiving doses | Discussion, para 2)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (The DNA-damage/p53 signature was already present at the lowest dose. | Livers from low-dose-treated NHPs also exhibited activation of the DNA damage response and the p53 signaling pathway. | Results, first subsection, para 4)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (Transgene expression level correlated positively with the pro-apoptotic PERK effector DDIT3 and negatively with CES1. | SMN1 expression levels and vector dose (vg/animal) positively correlated with the pro-apoptotic PERK effector DDIT3 (CHOP) | Results, second subsection, para 4)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (The earlier study reported only mild immune-cell infiltration at the acute time point, from which the authors infer a vector-specific T-cell response is unlikely. | histological analysis revealed only mild immune cell infiltration, suggesting that a vector-specific, T cell-mediated response is unlikely | Introduction, para 3)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (The ATF6 and IRE1-XBP1 branches were not seen, and the data for that statement are not shown. | However, no activation of the ATF6 pathway or of the IRE1α-XBP1 pathway was detected (data not shown). | Results, second subsection, para 2)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (The authors give the rat result an expression-level explanation: about tenfold lower transgene expression in rat liver. | The absence of UPR activation in rats receiving high vector doses can be explained by the approximately 10-fold lower levels of transgene expression | Discussion, para 2)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (The authors say the dataset is mechanistic and not a temporal model of the clinical scenario. | these data should be interpreted as mechanistic insights rather than a direct temporal model of the clinical scenario | Discussion, para 7)
- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (The authors state the contribution of each pathway is not resolved. | Additional mechanistic studies are needed to identify the role of each pathway and the exact factors involved in their activation. | Discussion, para 9)
- [PMID 42198847, artefact `files/fulltext/PMID42198847_BoespflugTanguy2026_PMC.xml`] (Prophylactic immunosuppression was prednisolone plus sirolimus. | Prophylactic immunosuppressive therapy included prednisolone and sirolimus (Figure 1A). | Patient details and clinical findings, para 2)
- [PMID 42198847, artefact `files/fulltext/PMID42198847_BoespflugTanguy2026_PMC.xml`] (Anti-AAV9 neutralising antibodies were absent at screening, but a low total IgG titre to the capsid was found retrospectively before dosing. | whereas total low IgG antibodies were detected prior to vector injection | Patient details and clinical findings, para 2)
- [PMID 42198847, artefact `files/fulltext/PMID42198847_BoespflugTanguy2026_PMC.xml`] (Several cytokines were elevated before dosing, read by the authors as a pre-existing inflammatory state. | These findings indicate a pre-existing inflammatory state prior to dosing. | Laboratory and postmortem studies, para 1)
- [PMID 42198847, artefact `files/fulltext/PMID42198847_BoespflugTanguy2026_PMC.xml`] (Postmortem examination: acute circulatory failure as cause of death, no overt myocarditis or thrombotic microangiopathy. | Postmortem analysis identified acute circulatory failure as the cause of death, with no overt signs of myocarditis | Laboratory and postmortem studies, para 3)
- [PMID 42198847, artefact `files/fulltext/PMID42198847_BoespflugTanguy2026_PMC.xml`] (Vector copy number in CNS was 16- to 550-fold lower than liver. | showing a 16- to 550-fold decrease compared to the liver | Vector distribution and transgene expression)
- [PMID 42198847, artefact `files/figures/PMID42198847/gr3.webp`] (Figure 3B: vector copies per diploid genome about 7700 in liver, 2450 in spleen, 850 in lung, 810 in kidney, against 14 in cerebellum, 128 in cortex and 493 in thoracic cord. | [figure attestation — pixels cannot be quote-matched] Fig 3B bar chart read at native resolution: liver 7704, spleen 2448, lung 847, kidney 806, adrenal 466, left ventricle 374, cortex 128, cerebellum 14, thoracic spinal cord 493, lumbar dorsal root 460 vg per diploid genome. | Figure 3, panel B)
- [PMID 42198847, artefact `files/fulltext/PMID42198847_BoespflugTanguy2026_PMC.xml`] (The authors propose an early innate-immune, complement-mediated endothelial injury leading to capillary leak, shock and multi-organ failure. | We propose a mechanism driven by the early innate immune response | Discussion, para 3)
- [PMID 42198847, artefact `files/fulltext/PMID42198847_BoespflugTanguy2026_PMC.xml`] (The authors say sirolimus did not appear to mitigate the early immune response, consistent with its mainly adaptive-immunity action. | Importantly, sirolimus did not appear to mitigate early immune response in this patient | Discussion, para 6)
- [PMID 42198847, artefact `files/fulltext/PMID42198847_BoespflugTanguy2026_PMC.xml`] (The authors say the contribution of disease-related inflammation and recent bronchial congestion cannot be disentangled. | Although the respective contributions of SMA-PME-related inflammation and recent bronchial congestion without documented infection remain difficult to disentangle | Discussion, para 6)
- [PMID 41438872, artefact `files/fulltext/PMID41438872_Fortuna2025_PMC.xml`] (Necropsy and pathological evaluation found no vector-related macroscopic or microscopic findings. | Necropsy and pathological evaluation revealed no vector-related macroscopic or microscopic findings, indicating no treatment-related adverse effects. | Results, first paragraph)
- [PMID 41438872, artefact `files/fulltext/PMID41438872_Fortuna2025_PMC.xml`] (Cortical neuronal labelling median 11.1 percent for PHP.eB against 2.2 percent for AAV9, counted over regions of interest, not animals. | median PHP.eB value of 11.1% (6.56 | Results, AAV-PHP.eB yields higher neuronal transduction, para 1)
- [PMID 41438872, artefact `files/fulltext/PMID41438872_Fortuna2025_PMC.xml`] (The statistical unit is the region of interest: 336 and 343 regions from three animals per capsid. | Overall, 336 regions of interest (ROIs) | Results, AAV-PHP.eB yields higher neuronal transduction, para 1)
- [PMID 41438872, artefact `files/fulltext/PMID41438872_Fortuna2025_PMC.xml`] (The liver vector genome load after ICV is described as notably high. | and notably high in the liver (PHP.eB: 202.2 | Results, Significant portion of the virus leaks, para 1)
- [PMID 41438872, artefact `files/figures/PMID41438872/gr5.jpg`] (Figure 5B: liver vector genomes about 100 to 250 copies per diploid genome in both capsid groups against below 2 in heart, kidney and muscle; log axis. | [figure attestation — pixels cannot be quote-matched] Fig 5B log-axis bars, enlarged crop: liver PHP.eB and AAV9 bars at about 1e2 to 2.5e2 copies per diploid genome; heart about 1 to 2; kidney about 0.5; muscle about 0.3 to 0.4. | Figure 5, panel B)
- [PMID 41438872, artefact `files/fulltext/PMID41438872_Fortuna2025_PMC.xml`] (Serum liver enzymes and other clinical chemistry were not assessed. | as clinical chemistry parameters (e.g., serum liver enzymes) were not assessed in this study | Discussion, Potential limitations and challenges)
- [PMID 41438872, artefact `files/fulltext/PMID41438872_Fortuna2025_PMC.xml`] (The authors note PHP.eB's rodent advantage is attributed to LY6A binding, absent in primates. | binding to the LY6A receptor, which is absent in NHPs | Discussion, Key findings, para 2)
