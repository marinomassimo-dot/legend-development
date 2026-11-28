# N,N-Dimethylglycine in WWOX loss of function

28 November 2026 UTC · SCI_CODEX · INV-07 · question-driven. [Opening checkpoint](pretest.md) · [Printable brief](../../view/research_reports/dimethylglycine.pdf).

**Decision.** Park systemic pediatric WWOX development. Retain N,N-dimethylglycine (DMG) as a conditional tracer for separating neural substrate use from peripheral production of downstream metabolites. The held WWOX models consistently give scarce neural DMGDH RNA, and the short crossover in children with another mitochondrial disorder found a blood response with an unresolved oxygen-consumption effect.

## Evidence and its limits

| Source | Observation | Boundary |
|---|---|---|
| [Augustin et al.](https://doi.org/10.1111/febs.13828), Fig. 3, Table 1 and their definition of the ETF branch | In purified human DMGDH, the parent yields sarcosine while FAD accepts electrons and THF can capture the removed carbon. The physiological route passes via ETF and ETFDH into the ubiquinone pool. The lower apparent WT DMG Kₘ was 0.3 mM with DCPIP and 1.4 mM with ferrocene. Both are artificial acceptors. The H109R comparison gives substantially higher apparent Kₘ with both acceptors. | The reported efficiency column and division of displayed kcat by Kₘ agree on the direction and differ on the exact magnitude. For DCPIP the WT/variant ratio is 7.30 as printed and 7.58 on recalculation, for ferrocene 12.45 and 9.01. These summaries describe purified enzyme turnover and give no native respiratory or ATP rate. The lower-component DCPIP replay leaves the second apparent kinetic component outside the calculation. |
| [Binzak et al.](https://doi.org/10.1086/319520), Abstract and targeted Results | A human DMGDH deficiency report documents parent accumulation in peripheral fluids, with severe loss of apparent enzyme activity in its recombinant assay. | Increased parent can accompany impaired clearance. This genetic defect is distinct from WWOX loss, and matrix or retained protein abundance cannot be inferred from peripheral levels. |
| [Liet et al.](https://pubmed.ncbi.nlm.nih.gov/12520257/), primary abstract only | Five selected children with SLSJ cytochrome-c oxidase deficiency completed randomized, blinded three-day comparison periods separated by a two-week washout. Indirect calorimetry mean changes were −1 for parent and −6 for placebo in mL/min/m². The descriptive difference of period changes is +5. The authors report no substantial increase in oxygen consumption and no detected change in lactate, pyruvate, bicarbonate or pH. Mean daily caloric intake changed +44 in the parent period and −220 kcal/m² in the placebo period. | The underlying paired data, sequence effects and a paired uncertainty estimate remain unavailable from the abstract. The report describes increased blood DMG in all five, but the published abstract displays 617 mmol/L, which would be 63.6 g/L at the parent molecular mass. The unit is unresolved and excluded from quantitative exposure interpretation. This is selected systemic physiology in a complex-IV disorder, with no neural DMG or ATP measurement. |
| [Gascon et al.](https://pubmed.ncbi.nlm.nih.gov/2463912/), primary abstract only | Randomized placebo comparison in 19 institutionalized participants with frequent generalized or akinetic/myoclonic seizures over 28 days. The authors report no detected difference in seizure frequency between groups or versus baseline. | This is a short heterogeneous cohort. The abstract leaves exact age, genotype, arm counts, seizure ascertainment and chronic safety unresolved. |
| [Kern et al.](https://pubmed.ncbi.nlm.nih.gov/11305684/) and [Bolman and Richmond](https://pubmed.ncbi.nlm.nih.gov/10425581/), primary abstracts only | Four-week randomized comparison in 37 children aged 3–11 with autism/pervasive developmental disorder, and a separate crossover with eight completers ranging from childhood to adulthood. Both report no discernible treatment–placebo difference on the reported behavioral comparisons. | The trials support limited exposure experience. Behavioral scales do not measure respiration or WWOX circuit recovery. |
| [Saito et al.](https://doi.org/10.3390/metabo10050185), Table 1 and Supplemental Tables S1–S2 | Nine healthy adult men each gave matched fasting and post-meal plasma and lumbar CSF. Three participants were sampled at each assigned interval. At three hours the CSF ratio of means reproduced at **2.164** with nominal paired p **0.272**, versus **1.026** and p **0.828** in simultaneous plasma. CSF rises in two of three pairs and omission of one participant gives **1.50–2.83**. The 1.5- and 6-hour ratios were 1.03 and 0.92 with different participants. | Median-scaled abundances are relative inside each matrix. The meal is a mixed perturbation without an administered DMG tracer. The apparent CSF change does not establish oral DMG delivery, an absolute concentration or a time course in a common group of individuals. |
| [Schraw et al.](https://doi.org/10.1038/s41598-021-99147-6), Plasma/CSF Results and Methods | End-of-induction samples from a cohort of ten children with B-cell acute lymphoblastic leukemia gave a positive plasma–CSF association for relative DMG abundance (Spearman r = 0.84, FDR q = 0.04). The paper's minimum for paired detection analysis was three. | Disease, treatment and systemic covariance could influence both matrices. A positive rank association supplies neither a transfer rate nor a CSF/plasma concentration ratio. |

The kinetic replay computes the ratio of displayed parameters and a minimal single-component Michaelis–Menten sensitivity under fixed hypothetical substrate values. It preserves the printed values separately and uses no circulating concentration as an input to a neural model. The crossover replay subtracts published means only. [Input locators](source_inputs.tsv) · [Numeric comparison](comparisons.tsv) · [Meal study replay](csf_meal.tsv).

## Original WWOX analysis

| Dataset | Observation | What it changes |
|---|---|---|
| P17 mouse [cortex GSE158682](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682) and [hippocampus GSE158681](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) | Mean DMGDH 0.071→0.111 TPM (4 WT/3 KO) and 0.163→0.098 TPM (2 WT/3 KO). Both comparisons stay below one TPM and change sign on single-library omission. SARDH has greater coverage. In hippocampus, ETFA 25.02→16.04, ETFB 99.48→55.68 and ETFDH 12.27→10.35 TPM, all with the same sign on omission. Cortex signs differ between ETFA and ETFB. | Hippocampal electron-transfer capacity is a possible second bottleneck. The mixed tissue directions give priority to direct enzyme and mitochondrial-respiration assays over a pan-neural RNA interpretation. |
| Untreated week-15 [human cerebral organoids GSE156243](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243), 2 WT/4 KO | DMGDH 0.884→0.770 CPM, both arms below the abundance floor. SARDH 6.11→7.16 CPM. ETFA and ETFB rise with stable sign and ETFDH falls modestly 5.86→5.51 CPM. | The human organoids do not reproduce the entire mouse hippocampal ETF pattern. They supply neither juvenile central exposure nor a direct flux estimate. |
| Raw and assigned pooled hippocampal nuclei [GSE158684](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684) | Dmgdh positive counts are 7/3,182 control and 13/2,920 KO in the entire deposited matrices, before depth or class filters. Etfb's annotated feature is present with zero counts in both raw pools. Etfdh decreases in assigned excitatory, inhibitory and astrocyte classes. | The Dmgdh ratio is dominated by sparse observations from two pools and supplies no replicate-level direction. ETFB bulk transcript has clear coverage, so the nuclear zero is a technical coverage boundary. |

The abundance floor is a descriptive guard and absence of detected RNA cannot establish absence of enzyme function. Individual-library omission addresses sensitivity rather than significance. TPM, CPM and nuclear UMI values retain their original scales. [Bulk](native_bulk.tsv) · [Nuclear coverage](nuclear_coverage.tsv) · [Cell classes](cell_types.tsv) · [Class decomposition](mixture.tsv).

## Inference and discriminating prediction

**Hypothesis.** A narrow subset with low intracellular parent and retained DMGDH/ETF activity could improve substrate-linked ATP recovery. A competing explanation is conversion outside the brain, with sarcosine, glycine or one-carbon products affecting neural function. A second local explanation is a downstream bottleneck in electron transfer or terminal respiration. DMG-derived electrons enter at ubiquinone after ETFDH and still depend on downstream respiration, including complexes III and IV. A rise in labeled product or oxygen consumption alone leaves productive ATP recovery unresolved.

**One comparison.** In WWOX-deficient and isogenic control neural preparations, match intracellular parent and physiological workload. Use methyl-labeled DMG to track parent, newly labeled sarcosine and one-carbon product such as formate. Pair that measurement with mitochondrial oxygen use, ATP recovery and subsequent evoked recruitment. Compare interruption of the local DMGDH reaction with a respiratory-pathway control and exposure-matched downstream sarcosine/glycine. Verify that the controls preserve comparable basal viability and functional headroom.

- Parent-specific substrate use predicts that isotope transfer and improved ATP recovery disappear with local DMGDH interruption. A controlled ETFDH bottleneck can separate formation of labeled product from productive electron transfer.
- A downstream-product explanation predicts that matched sarcosine or glycine reproduces the functional response when local DMG conversion is unavailable. This would justify asking where the products originate before inferring parent delivery.
- Accumulated intracellular parent with little newly labeled product, or labeled product with unchanged ATP recovery and recruitment, lowers the candidate's priority.

## Pediatric feasibility and reopen condition

The relevant entity is N,N-dimethylglycine (free parent [PubChem CID 673](https://pubchem.ncbi.nlm.nih.gov/compound/673)), with salt identity and content requiring verification for any product comparison. Short studies document exposure experience in other conditions but lack a verified unbound juvenile neural level, sustained tolerability for WWOX polytherapy, interaction data with background antiseizure agents, or a WWOX functional endpoint. The current exposure unit and assay divergences would remain consequential even if a behavior signal were reported in a different population.

Reopen for a verified parent-specific neural tracer result and functional recovery at matched physiological workload, or for a defined native WWOX subgroup with measured substrate limitation and retained DMGDH–ETF activity. An independent review of an absolute site-exposure or paired flux/ATP dataset could change this decision. The aggregate reports alone cannot resolve it.

## Reproduce

Use the canonical held GEO inputs listed in the [module manifest](../../memantine_magnesium_20261123/inputs.tsv) and the free [Saito supplement](https://mdpi-res.com/d_attachment/metabolites/metabolites-10-00185/article_deploy/metabolites-10-00185-s001.zip). The supplement replay requires openpyxl (tested with 3.1.5). The workbook is read without exporting participant-level values.

```bash
drug=disease-models/wwox/research/drug_repurposing
dossier="$drug/continuous_compounds/dimethylglycine"
held=/home/desktop/legend-development/files
out=$(mktemp -d)
python3 -B "$dossier/replay_expression.py" "$drug" "$held" "$out"
python3 -B "$dossier/replay_csf.py" "$held/deepening_downloads/dimethylglycine_20261128/metabolites-10-00185-s001.zip" > "$out/csf_meal.tsv"
python3 -B "$dossier/replay_comparisons.py" > "$out/comparisons.tsv"
for table in native_bulk cell_types mixture nuclear_coverage csf_meal comparisons; do
  cmp "$out/$table.tsv" "$dossier/$table.tsv"
done
```

Only derived aggregate values and source locators are included in the repository. Publisher files and the original workbook stay in their licensed locations.
