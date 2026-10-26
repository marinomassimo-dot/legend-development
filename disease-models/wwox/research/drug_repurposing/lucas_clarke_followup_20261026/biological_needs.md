# Biological needs derived from Lucas-Clarke 2026 — WWOX-relevant strands to verify

Scientist `scientist-c`, 2026-10-26. Exploratory, non-canonical, class level. Not medical advice; no dose, route or
suitability statement. Everything taken from the paper is **NOT WWOX-DEE EVIDENCE**: it is a *Drosophila* model of
Alzheimer's amyloid pathology (secreted Arctic Abeta42 in neurons), partial neuronal RNAi (about 0.55 of control mRNA, no protein
level) or CRISPRa (about 1.77-fold mRNA), whole-head readouts, one omics age (day 14, females).

Source for every row: dossier `research/fulltext_dossiers/PMID42909904.md` (PAPER 567; receipt `FTR-20261026-42909904-01`),
manifest `research/deepdive_manifests/PMID42909904.json`, `verbatim_locators.entries[i]` (index in brackets), blind audits
`research/locator_audits/2026-10-26_PMID42909904_*`. Entries 31, 49, 89, 94 are SUPPORTED, entry 95 was narrowed after an OVERSHOOT
finding. Scientist A's preprint-versus-published comparison
(`research/lucas_clarke_preprint_vs_published_20261026.md`, landed on `main` while this was being written) is reused, not redone; its section 0 ties each Ldh log2 figure to its contrast and agrees with the figures quoted here (KD+A versus A 1.29; A versus control 1.11 in the table and 1.19 in the text).

## How to read a strand

Each strand is a **need** (what a therapy would have to move), stated as: *contrast* (what was compared) · *direction* (what moved, in
which tissue) · *context* (model, background, age) · *evidence status* (what is measured, what is the authors' inference, what is not
tested) · *to verify* (the datum that would settle it). A strand is **not** a premise about WWOX-DEE, and none is promoted to a premise
by this file.

## Per-contrast observations (the table every strand rests on)

| # | Contrast | What moved (direction) | Statistic (n) | Status | Entries |
|---|---|---|---|---|---|
| C1 | Neuronal Wwox reduction vs control, **no amyloid** (LacZ background) | lifespan shorter (57 vs 42 d); climbing unchanged; sleep pressure up; wing ROS up; 54 genes down / 44 up; **Atf4 immunofluorescence unchanged** (t 0.0894, P 0.9305, n 6); **lactate down nominally** (-0.43 log2; simple effect not tested); **Ldh not among changed genes** | N 91-105 flies; n 4 head pools; n 5 head pools | DATO, partial RNAi, one RNAi line | 8, 10, 11, 15, 26, 37, 39, 40, 58 |
| C2 | Neuronal Wwox reduction vs control, **with Abeta42** | lifespan shorter (41 vs 26 d); climbing lower; total and soluble Abeta42 higher by MSD; **Atf4 immunofluorescence up** (about 1.0 to about 1.2-1.3, U 0, P 0.0022, n 6); **Ldh transcript up** (+1.29 log2 over Abeta42 alone, padj 1.18e-11, n 4 pools); **lactate up** (interaction F 23.606, padj 0.0174, +1.30 log2); sima:GFP unchanged (P 0.5185); Xbp1 splicing unchanged (P 0.1954) | as listed | DATO for each; the chain between them is not tested | 17, 19, 24, 29, 39, 40, 43, 57, 59, 61, 66, 69 |
| C3 | Abeta42 vs no Abeta42 (main effect) | lactate up, 2-hydroxyglutarate up, Ldh up (+1.11 log2 table, text 1.19) | F 27.846 padj 0.0050; F 49.551 padj 0.0006 | DATO. Ldh: up with Abeta42 versus LacZ (+1.11 table, 1.19 text). Lactate: the Abeta42 main effect is significant, but Fig 5C shows Abeta42 with control RNAi at the LacZ level and the rise only in the knockdown-plus-Abeta42 cell, so an Abeta42-alone lactate rise is not shown | 30, 31, 38 |
| C4 | Ldh RNAi added to (Abeta42 + Wwox RNAi) vs (Abeta42 + Wwox RNAi) | climbing better at 14/21/28 d to or above the control line | t 3.182, 6.832, 5.198; N 4-6 vials | DATO, once; no Ldh-alone arm, no Wwox-mRNA check in the double line, lactate not measured in it, lifespan and Abeta42 not tested | 50-56 |
| C5 | Neuronal Wwox **over**expression vs control, **no amyloid** | no lifespan or climbing effect; 6 genes down, none up; L-methionine **down** | P 0.1420; P 0.8770 | DATO | 71, 78, 84 |
| C6 | Neuronal Wwox overexpression vs control, **with Abeta42** | lifespan longer (47.5 vs 29 d); climbing better; plaque size and number lower; total Abeta42 lower; 305 genes down / 59 up, anti-correlated with the Abeta42 signature (r -0.83); glycolytic enzyme transcripts Gapdh1, Eno, Pgk, Pgi, Tpi **lower** (log2 -0.59 to -0.70); **Ldh not reversed**; lactate not shown; L-methionine not lowered | n 5-7 brains; n 3-4 pools | DATO; rescue occurs without lowering Ldh or 2-hydroxyglutarate | 72, 75, 79-86, 99-103 |
| C7 | Glial Wwox reduction, with and without Abeta42 | no climbing effect; lifespan 22 vs 24 d (with) and 70 vs 74 d (without) | N 98-115 | DATO; Wwox mRNA is highest in glial clusters (Fig 1A), yet neuronal knockdown is the manipulation that matters here | 2, 9, 21, 74, 95 |

## Strands

### S1 — Integrated stress response (ATF4 arm): conditional on amyloid, and not reproduced by a human WWOX knockout
- **Contrast / direction.** C2: Atf4 protein signal up with Wwox reduction plus Abeta42. C1: unchanged without Abeta42.
- **Context.** Fly brain, whole-mount immunofluorescence, one antibody, four small regions of interest, y axis starting at 0.5, n 6 brains, day 14.
- **Evidence status.** MEASURED, correlational, one condition. The PERK/eIF2 alpha-phosphorylation step is **not measured** (the paper says it did not determine whether
  WWOX acts on the pathway directly; Xbp1 splicing unchanged is a negative on a different arm). **Atf4 is never perturbed**: the step Atf4 -> Ldh is the authors'
  inference (cited prior fly report; "this could be the mechanism") — there is no Atf4 knockdown or activation in the paper.
- **Human check on hand (exploratory, mine).** In the one WWOX-knockout human neural transcriptome (organoids, no amyloid, 4 KO vs 2 WT libraries, one laboratory) the
  ATF4/ISR target set is **lower** than 10,000 random sets (mean shift -0.288, P(random <= observed) 0.0005); CHAC1, TRIB3, PHGDH, SESN2 down; ATF4, ATF5, DDIT3, ASNS not individually changed
  (`gse156243/prediction_isr_ldh_chain_20261026.md`). This is an **exploratory negative** about the transcript signature in one tissue without amyloid. It does not show the ISR is
  normal at the level of eIF2 alpha phosphorylation or protein, and it does not contradict the fly result (the fly effect is amyloid-conditional).
- **To verify.** eIF2 alpha phosphorylation and ATF4 protein in a WWOX-deficient human neural system, with and without a proteotoxic load; an Atf4 loss-of-function arm in the fly with the Ldh and lactate readouts.

### S2 — LDH / lactate arm: Ldh-lowering helped locomotion once, in the amyloid-plus-Wwox-reduction genotype only
- **Contrast / direction.** C2: Ldh transcript and lactate up. C4: adding Ldh RNAi improved climbing. C1: Ldh not changed and lactate nominally down. C6: Wwox overexpression does not reverse Ldh.
- **Context.** Female heads, whole head (glia carry the highest Wwox mRNA, so a neuronal origin of lactate is not established); metabolomics N 5 pools of 10, two-way ANOVA on the top 200 features by variance, 10% FDR.
- **Evidence status.** Ldh up and lactate up: MEASURED. Ldh causes the lactate rise: ASSERTED from enzymology plus coincidence (no isotope tracing, no flux, no NAD/NADH). Ldh rescues locomotion: TESTED ONCE with missing controls
  (no Ldh-alone arm; both hairpins on chromosome 3; Wwox mRNA not reported in the double line; lactate not measured in it; the authors themselves cite Ldh knockdown as detrimental in other fly Abeta42 models and call the rescue partial).
  Ldh may be a cost-bearing node, not a free target.
- **Human check on hand (exploratory, mine).** LDHA is up in the KO organoid (+0.75 to +0.91) but also falls with elapsed culture time in WWOX-unperturbed spheroids, so the rise is as consistent with a less advanced tissue as with a WWOX effect. Human brain MRS lactate in one WWOX patient is reported extremely low (DL-BIO-008), and human metabolism measured in WWOX deficiency is normal in four sources (DL-BIO-009); the paper neither supports nor contradicts either.
- **To verify.** Lactate (enantiomer- or isotope-resolved) in the double-RNAi genotype; an Ldh-alone arm; a second Wwox RNAi line or a null; lactate and Ldh in a WWOX-deficient human neural system with a tissue-composition control.

### S3 — The pyruvate -> acetyl-CoA branch (PDH / PDK): NOT something this study measured. Kept separate.
- **What the study measured.** Nothing on PDH, PDK, pyruvate, flux, oxygen consumption or NAD/NADH. Pyruvate is not reported in any panel, list or legend (whether it was tested is unknown; the MetaboLights deposit, which could say, is not publicly retrievable — `mtbls12344.md`). Pdk, Pdha, Pdhb are absent from the significant gene lists, which is not a test. The Figure 5D schematic draws a TCA node with no data attached. The paper's own heading and abstract speak of pyruvate metabolism, but that rests on transcript pathway over-representation (KEGG pyruvate metabolism, Supp Table 3, a gene set that includes Ldh itself; Pepck2, CG11052 and Adh are lower), not on a pyruvate, PDH or PDK measurement.
- **What it implies only by logic.** A raised Ldh would divert pyruvate toward lactate; PDK inhibition would then be a rationale only if pyruvate were being diverted from oxidation. Unmeasured; an inference two steps from the data.
- **My transcript tests (exploratory negatives).** In the KO organoid: PDK1 transcript down (-0.34), PDK/PDH set +0.17 (P 0.22), LDH-to-PDH ratio not shifted (KO minus WT -0.138, inside the spread of the two WT libraries), pyruvate-fate transcripts not separated from chance
  (`gse156243/prediction_hif1a_pdk_chain_20261025.md`, `prediction_pyruvate_fate_20261026.md`). These do **not** show that PDH activity or lactate are normal: transcripts are not activity, flux or metabolite. The HYP-20260709-01 recalibration of 2026-09-21 (ledger bullet on the PDK-to-PDH block) states that PDH activity and citrate synthase were measured unchanged in four human-cell conditions; I could not trace that statement to a named panel in this session (the bullet cites the two metabolism readings FTR-20260921-35328751-01 and FTR-20260921-36271927-01 without a locator), so it is carried as the ledger's statement, unverified here. The HIF1A-to-PDK-to-PDH step remains unmeasured in any WWOX-deficient human neural system.
- **To verify.** PDH activity (or phosphorylated PDHA1 serine residues) and pyruvate/lactate/acetyl-CoA labelling in WWOX-deficient neural cells; pyruvate rows of MTBLS12344 if ever released.

### S4 — Wwox dose and glycolytic-gene restraint (overexpression arm)
- **Contrast / direction.** C6: more Wwox with amyloid lowers transcripts of Gapdh1, Eno, Pgk, Pgi, Tpi; Ldh unchanged; no effect without amyloid (C5). Reduction (C2) raises Ldh. The two arms are not mirror images: lactate under overexpression is not shown, and the Abeta42 main effect did not raise lactate in that cohort, so there was no rise to reverse.
- **Evidence status.** Transcript direction MEASURED (N 3-4 pools, padj 1.5e-3 to 7.8e-3); the reading "Wwox restrains glycolysis" is my INFERENZA, untested; not discussed by the authors.
- **To verify.** The same transcripts in WWOX-restored human neural cells; flux.

### S5 — Methionine / one-carbon arm
- **Contrast / direction.** C5: overexpression lowers L-methionine (padj 0.0047, 0.0091) without amyloid; C6: not with amyloid; Abeta42 alone lowers methionine by about half in the control arm (main effect not significant). Transcripts of Phgdh, Got1, Got2, Mdh1, Cbs, SpdS fall with overexpression plus Abeta42.
- **Status.** DATO; the "interaction" is the absence of the overexpression-induced fall under Abeta42. Human KO organoid: methionine/cysteine gene set not different from chance (mean +0.011, exploratory).
- **To verify.** Whether any intervention on this arm is separable from the ISR arm (the paper's Discussion links it to GCN1/GCN2, untested).

### S6 — What is NOT a premise here
- **Wnt/TCF7L2, mitochondrial or GSK3 beta deficits are not assumed.** In the analysed WWOX-knockout transcriptome the Wnt readouts are raised, but whether that is a WWOX effect or tissue composition/maturation is unresolved (`gse156243/independent_reanalysis_wnt_vs_maturation_20261025.md`; HYP-20261025-09 parked). This follow-up neither uses nor tests them.
- **No WWOX protein is measured in the fly**, and the fly-to-human link is a sequence-similarity and ortholog-prediction statement plus lifespan-level rescue by human WWOX cDNA.
- **Direction is not uniform across contexts**: every strand above carries a different sign without versus with amyloid. A therapy chosen for "WWOX loss raises ATF4/LDH/lactate" would be chosen on a context (amyloid load) that WWOX-DEE does not obviously share.

## What would make any strand actionable for the reference genotype

All four of the mission's preconditions (mission section 5) have to hold per node: (1) which WWOX function is lost, (2) a **signed** map with direction in the relevant human cell, (3) a proximal readout, (4) CNS exposure and paediatric safety. For ISR, LDH and PDK the status today is: (1) unresolved; (2) fly-only and amyloid-conditional, human transcript contrary (ISR) or confounded (LDH, PDK); (3) not defined; (4) compound-specific, in the cards.
