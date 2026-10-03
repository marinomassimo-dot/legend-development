# COMMIT CANDIDATE — CC-20261003-C-RESCUE-READOUT-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist C), intake wave 2 2026-10-03, branch `task/sci-C-20261003`.
**context_policy:** `SOURCE_FIRST` for all six readings; the comparison with LEGEND's records was made after each first pass (`research/intake_wave_20261003_C.md` § 1).
**Not medical advice.** Class-level statements about published models and genotypes only.

## Question this answers

Which endpoint in a tractable WWOX-loss model could serve as a **rescue readout** for a
therapeutic test, rather than only as a description of the defect — and with what transfer limit
to the WWOX-DEE genotype class.

## Target

- `research/discovery_ledger_current.md`: **create** one lead, provisionally `DL-METH-114`, carrying the
  ranked readout table and the §13 rejections. *(Next free DL number measured 2026-10-03 with
  `registry_records.py catalog`: the DL families share one sequence whose maximum is 113.)*
- No claim, no working-model block, no paper-registry field is touched by this candidate.

**Numbers are provisional.** Peer scientists of the same wave may claim the same number; the
integrator renumbers in event order.

## Change class

**MINOR** (§ 7 of `prompt_batch_commit.md`) — a new research-layer lead. It narrows no
`consolidated baseline` claim and reverses none. The one adjacent canonical record,
`DL-MECH-021`, is left unchanged: this lead **points at** it rather than editing it.

## Ordering

The six receipts `FTR-20261003-<pmid>-NN` prepared in `scratchpad/receipts_pending_w2/` must be
appended before this record lands, so that no registry record declares a reading whose receipt is
not in the ledger.

## The finding

Across the five model sources read in this group, exactly **three** endpoints behave like a rescue
readout — large effect, a drawn rescue arm, and a measurement rather than a picture — and each
sits in a different model.

| Rank | Readout | Source | Effect | Rescue arm | What limits it |
|---|---|---|---|---|---|
| 1 | **Single-neuron spontaneous firing rate**, patient-derived cerebral organoids, week 7, cell-attached | PMID 34268881 Fig 5C | 0.41 → 1.65 → 0.46 Hz (≈4×) | **yes**, AAVS1-driven WWOX; rescued vs parental `P = 0.7681` | n is neurons (24 / 41 / 40) from 4 / 3 / 3 organoids — organoid-level n is 3–4; one family; no blinding |
| 2 | **LFP oscillatory power, 0.25–1 Hz AUC**, week 7 organoid slices | PMID 34268881 Figs 2C, 2G | ≈0.030 → ≈0.066 → ≈0.025 | **yes**, and uniquely by **post-hoc mosaic lentivirus** delivered to day-35 tissue | no P-value is distributed, only asterisk bands; 14 slices per arm |
| 3 | **Eye diameter at 48 hpf**, zebrafish | PMID 25649963 Fig 2E | ≈265 → ≈205 → ≈270 µm (≈−23 %) | **yes**, and the rescuing construct is the **SDR/ADH domain alone** | morpholino/siRNA era, no protein-level validation, non-neural tissue |

Two further endpoints are **large but unusable as published**:

* **3-D network formation of human neural progenitors in a thick ECM scaffold**
  (PMID 31543760, Figs 5 and 6) — near-binary, human neural lineage, reproduced in three
  experiments and seeding-density-independent, but **unquantified, un-n'd, untested and
  un-rescued**, with the knockdown depth stated nowhere in the paper.
* **Daytime sleep duration in *Drosophila*** (PMID 39952983, Fig 2C) — ≈500 → ≈300 min, `****`,
  n = 32, automated, continuous and non-terminal, but with **no rescue arm**, one allele, one
  background and males only.

## The delivery contrast, which is the therapeutically informative part

PMID 34268881 contains two different restorations and they are not equivalent. The AAVS1 line
expresses WWOX ubiquitously and supraphysiologically **from pluripotency**, and gives a partial,
marker-selective rescue that **overshoots** wild type on cortical-layer markers. The lentiviral
arm reached **already-patterned week-5 organoids**, produced sparse mosaic WWOX, and normalised
the network readout completely. Taken together: the electrophysiological phenotype is not locked
in once cortical patterning has begun, and it does not require every cell to be corrected. That is
a statement about **timing and coverage**, which is what a delivery strategy needs and what a
constitutive knock-in cannot supply.

## Rejected candidate readouts, with the reason recorded

Under [`LEGEND_CORE.md` § 13](../../../../framework/instruction/LEGEND_CORE.md#13-biomarker-scope-hard-rule)
a disease biomarker must measure the functional state of the target gene. None of the following is
Tier 1 or Tier 2, and none can be sampled in a living patient's neurons. They are written here as
rejected so the rejection is not re-done.

| Rejected | Source | Reason |
|---|---|---|
| Intracellular Ca²⁺ by yellow-cameleon FRET | PMID 25649963 Fig 4 | **Tier 3**, and in this source it is one representative colour-coded image per condition with no axis, n, statistic or rescue arm; imaged **after** the oedema forms, in a circulation the authors attribute to cardiac failure |
| Resazurin reduction ("mitochondrial redox potential") | PMID 31543760 Fig 2 | **Tier 3**; scales with viable-cell number and is not normalised to cell count here, so a ≈32 % lower signal is equally consistent with fewer or slower cells |
| Secreted pro-MMP2 / pro-MMP9 | PMID 31543760 Fig 4 | **Tier 3**; distal, shared with every migration phenotype; no disease-population sensitivity or specificity |
| Cleaved caspase-3 area | PMID 26302329 Fig 5G, PMID 34268881 Fig EV2H | **Tier 3**, terminal, and in PMID 26302329 the only supporting quantification is labelled in the opposite sense to the text (see `CC-20261003-C-APOPTOSIS-DIRECTION-01`) |
| GRP78 induction, phospho-IRE-1, PERK band shift | PMID 28749468 Figs 4a, 5a, 5b | **Tier 3** generic ER-stress markers, never quantified in that paper; the paper itself states PERK activation is unchanged by WWOX status |
| γH2AX / 53BP1 foci per nucleus | PMID 34268881 Fig 3F | Clean and dose-sensitive (0.78 → 1.5 → 0.58) but a **generic DNA-damage** marker shared with every DDR condition; requires fixed sectioned tissue |
| Self-reported sleep duration | PMID 39952983 Tables 2, 3 | **Tier 3** distal clinical endpoint; the effect is 12–18 min at suggestive significance, co-moves with time in bed, and sleep efficiency and the Epworth score are flat |
| *WWOX* mRNA as a chemotherapy-response predictor | PMID 28749468 Figs 6, 7 | A **tumour** chemosensitivity association, not a measure of WWOX functional state in a person with a germline WWOX disorder |

## Transfer limits that travel with the lead

* Every ranked readout comes from a **null** — a CRISPR exon-1 frameshift, a homozygous
  splice-acceptor allele, or a morpholino/siRNA knockdown. **None is a missense allele**, and a
  null models neither P47T nor Q230P nor G372R nor A141T nor P252A.
* No ranked readout can be sampled in a living patient. They are **model rescue readouts**, a
  different and legitimate object from a biomarker, and this lead does not call any of them one.
* PMID 34268881's own SCAR12 arm (G372R, homozygous) shows **weaker** organoid phenotypes than the
  WOREE arm, so the transfer of any of these readouts to a milder missense class is untested in
  the direction that matters.
* `DL-MECH-021` already records the zebrafish SDR-only rescue. This lead does not restate it as
  new; it uses it.

## Op list — `discovery_ledger_current.md` (record-scoped; dry run 2026-10-03 against `0ed6ad4` (main `eb01d5f` merged))

```json
[
 {
  "op": "append",
  "text": "\n### DL-METH-114 — Which WWOX-loss endpoints are rescue READOUTS, and which are descriptions of the defect\n\n- **Status**: open · **Tag**: INFERENZA (the ranking) over DATO (each effect size) · **Fonte**: intake wave 2 2026-10-03, Scientist C — PMID 34268881, PMID 25649963, PMID 31543760, PMID 39952983, PMID 26302329, PMID 28749468, all read first-hand with figure panels inspected.\n- **Causal statement**: of the endpoints published for WWOX loss in a tractable model, only three carry a *drawn rescue arm* on a *quantified* measurement: single-neuron firing rate in patient-derived cerebral organoids (0.41 to 1.65 to 0.46 Hz, rescued-vs-parental P = 0.7681, PMID 34268881 Fig 5C); LFP oscillatory power at 0.25-1 Hz (about 0.030 to 0.066 to 0.025, PMID 34268881 Figs 2C and 2G); and zebrafish eye diameter at 48 hpf (about 265 to 205 to 270 micrometres, PMID 25649963 Fig 2E, rescued by the SDR/ADH domain alone, as already recorded in DL-MECH-021). Two further endpoints are large and human but unusable as published: 3-D network formation of hNPC in a thick ECM scaffold (PMID 31543760 Figs 5-6) is near-binary and unquantified, un-n'd, untested and un-rescued, with the knockdown depth stated nowhere; and Drosophila daytime sleep (PMID 39952983 Fig 2C, about 500 to 300 minutes, ****) has no rescue arm.\n- **The delivery contrast is the transferable part**: in PMID 34268881 a constitutive AAVS1 WWOX knock-in expressed from pluripotency gives a partial, marker-selective rescue that OVERSHOOTS wild type on cortical-layer markers, while a lentivirus delivered to ALREADY-PATTERNED week-5 organoids, producing sparse mosaic WWOX, normalises the network readout completely. The electrophysiological phenotype is therefore not locked in once cortical patterning has begun, and it does not need every cell corrected.\n- **Rejected candidate readouts, recorded so the rejection is not re-done** (LEGEND_CORE §13: a biomarker must measure the functional state of the target gene; none of these is Tier 1 or Tier 2, and none can be sampled in a living patient's neurons): intracellular Ca2+ by yellow-cameleon FRET (PMID 25649963 Fig 4 — one representative colour-coded image per condition, no axis, n, statistic or rescue arm, imaged after the oedema forms); resazurin reduction called 'mitochondrial redox potential' (PMID 31543760 Fig 2 — not normalised to cell number); secreted pro-MMP2/9 (PMID 31543760 Fig 4); cleaved caspase-3 area (PMID 26302329 Fig 5G, PMID 34268881 Fig EV2H); GRP78, phospho-IRE-1 and the PERK band shift (PMID 28749468 Figs 4a, 5a, 5b — never quantified, and the paper states PERK activation is unchanged by WWOX status); gamma-H2AX and 53BP1 foci (PMID 34268881 Fig 3F — clean and dose-sensitive at 0.78 to 1.5 to 0.58, but a generic DNA-damage marker needing fixed sectioned tissue); self-reported sleep duration (PMID 39952983 — 12 to 18 minutes at suggestive significance, co-moving with time in bed while sleep efficiency and the Epworth score are flat); and WWOX mRNA as a chemotherapy-response predictor (PMID 28749468 Figs 6-7 — a tumour chemosensitivity association, not a measure of WWOX functional state in a germline WWOX disorder).\n- **Counter-evidence and limits**: every ranked readout comes from a NULL - a CRISPR exon-1 frameshift, a homozygous splice-acceptor allele, or a morpholino/siRNA knockdown - so none models a missense allele of the reference genotype class. PMID 34268881's own SCAR12 arm (homozygous G372R) shows weaker organoid phenotypes than its WOREE arm, so transfer to a milder missense class is untested in the direction that matters. No P-value for any main or Expanded-View figure of PMID 34268881 is distributed anywhere: the effect sizes above are read from asterisk-banded panels.\n- **Falsifier**: a titrated WWOX restoration series in patient-derived organoids, with a wild-type comparator drawn at every dose, reporting firing rate and 0.25-1 Hz power together. If the two readouts do not move together across the series, 'the electrophysiological phenotype' is not one endpoint and this ranking collapses into two.\n- **Not medical advice.** No clinical inference about vector, route, dose, window or safety follows from any of this.\n"
 }
]
```

## `### LOCATOR TRIPLES FOR BLIND AUDIT`

```
(The patient-derived single-neuron firing rate is restored by WWOX re-introduction to a level statistically indistinguishable from the healthy parental lines. | There was no significant difference between the firing rate of WSM P and WSM S W‐AAV COs' neurons (P = 0.7681). | PMID 34268881, Results, "Brain organoids of patient-derived WWOX-related developmental and epileptic encephalopathies", para 3; files/fulltext/PMID34268881_Steinberg2021_PMC.xml)

(The electrophysiological rescue in the hESC arm was obtained with a lentivirus delivered to organoids that had already formed, not with a constitutive knock-in. | At day 35 of culture, individual COs were transferred to an Eppendorf tube containing CMM with 1:100 of virus‐containing medium | PMID 34268881, Materials and Methods, "Cerebral organoid generation, culture, and lentiviral infection", final paragraph; files/fulltext/PMID34268881_Steinberg2021_PMC.xml)

(The authors state that their restoration is supraphysiological and only partial, and ask for population-targeted delivery and fine-tuned expression. | This resulted in supraphysiological expression of WWOX in all cell populations seen in COs and a partial rescue. | PMID 34268881, Discussion, para 6; files/fulltext/PMID34268881_Steinberg2021_PMC.xml)

(The zebrafish rescue construct is the ADH/SDR domain alone, not full-length wwox. | RNA rescue experiments were performed after preparing wwox mRNA (ADH domain region) by replacing pTAC-2 with the pCS-2 vector | PMID 25649963, Materials and Methods, "Polymerase chain reaction (PCR) and complementary DNA (cDNA) cloning"; files/fulltext/PMID25649963_Tsuruwaka2015_PMC.xml)

(The zebrafish calcium imaging is performed after the oedema has already formed. | dynamics after edema formation in embryos that had been simultaneous transfected with yellow cameleon | PMID 25649963, Results, "Analysis of intracellular Ca2+ dynamics after edema formation", para 1; files/fulltext/PMID25649963_Tsuruwaka2015_PMC.xml)

(The calcium figure carries no axis, sample size, error bar or significance marker, while the morphometric figure in the same paper carries all of them. | [figure attestation] Figure 4 contains four sub-panels - bright-field and colour-coded ratio image for wild type and for knockdown - and no axis, error bar, sample size or significance marker anywhere; Figure 2E plots body length and eye size with error bars and drawn significance brackets for WT, control, phenotype and rescue. | PMID 25649963, Figure 4 compared with Figure 2E; files/fulltext/PMID25649963_assets/peerj-03-727-g004.jpg and peerj-03-727-g002.jpg)

(The hNPC knockdown depth is stated nowhere: the paper says only that it was assessed by Western blot. | The gene silencing efficiency was assessed with Western blot | PMID 31543760, Materials and Methods, "WWOX Gene Silencing", final sentence; files/fulltext/PMID31543760_Kosla2019_EPMC.xml)

(The single validation blot shows a reduced but clearly present WWOX band in the silenced line, with no numeric value or replicate. | [figure attestation] Supplementary Figure 1 is a single three-lane blot labelled hNPC, hNPC/shScrambled and hNPC/shWWOX with WWOX and GAPDH rows; the WWOX band is present in all three lanes, weakest in shWWOX and strongest in shScrambled, and no numeric value, error bar or replicate is shown. | PMID 31543760, Supplementary Figure 1, page 1 of Data_Sheet_1.pdf; files/fulltext/PMID31543760_assets/Data_Sheet_1.pdf)

(The 3-D phenotype is described as isolated single cells; the panels show small multicellular clusters, and all four panels carry one scale bar for two declared magnifications. | [figure attestation] Figure 6 panels C and D show scattered clusters of several cells each, not single cells, against the confluent networks of panels A and B; all four panels print a scale bar labelled 50 micrometres although the legend declares 200x for A and C and 40x for B and D. | PMID 31543760, Figure 6, panels A-D; files/figures/PMID31543760/fncel-13-00391-g006.jpg)

(The adhesion result on the ECM protein mixture is non-significant by the paper's own figure. | demonstrated considerably stronger adhesion to the ECM protein mixture (p = 0.0626) | PMID 31543760, Results, "WWOX Depletion Alters the Main Biological Functions of hNPC", para 2; files/fulltext/PMID31543760_Kosla2019_EPMC.xml)
```
