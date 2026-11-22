# ADV-171 result: the unread sheets of the Ma et al. 2025 S1 Data hold no pre-onset lipid, proteome or energy sign; nothing new for RP-036 and RP-039 (SCI successor Z, 2026-11-22; hypothesis level; adjacent mouse model, Cyfip2 R87C; not a WWOX result; no compound, dose or rank change; no new source; no contact; no e-mail address to any service; not medical advice)

Pre-registration: `PREREGISTRATION_ADV171_SCI_20261122.md` (commit `1344f0379`; it lists what had been seen: the six ADV-165 sheets, the sheet labels and the Fig 3, 6 and 8 legends, no numeric value of the unread sheets). Script: `cyfip2_unread_checks.py` (stdlib; `python3 -I cyfip2_unread_checks.py <S1 Data workbook> [extra]` prints every number below; the `extra` block is POST-HOC and labelled so). Workbook SHA-256 `906de753...e9d6d` verified before use.

## Answer first
**Rule 1 applies: CLOSE as "nothing new for RP-036 and RP-039"; the dataset stays closed for the metabolic family. L-late holds (rejecting observation 2 of the assignment). The only PWK 7 per-animal signs are of a different family (the mutated complex proteins, and a weak, regionally opposite synaptic-transcript set), and ADV-165 already established that PWK 7 is not a pre-onset age in this model.**

## STEP 1: inventory of the 28 unread sheets (shapes and labels; WT comparator and unit)
| Block | Sheets | Ages | Unit | WT comparator |
|---|---|---|---|---|
| Synapse transcripts (qRT-PCR) | Fig3A | PWK 1, 7, 14, 28; cortex and hippocampus; 23 genes per region | animal (5 to 6 per gene-age) | **R87C animals only, values relative to the WT mean; WT animals are not in the sheet** |
| Synapse proteins (western, synaptosomes) | Fig3B, FigS4 (PWK 28 only) | PWK 1, 7, 14, 28 (Fig3B) | animal (6 to 10) | WT and R87C columns, per animal |
| Synapse imaging | Fig3C, FigS6B, Fig3D, Fig3E | PWK 14 and 28 (3C, S6B); PWK 28 (3D electron microscopy, 3 mice, images as rows; 3E PSD areas as rows) | animal; image or PSD | present |
| Glia morphology and markers | Fig5A, 5B, 5C, 5E, Fig6A, FigS7A, 7B, S9 to S12 | PWK 14 and 28 where labelled; S9 has PWK 1, 7, 14, 20 (cleaved caspase 3); several sheets carry no age label | animal, cell, axon | present |
| Lipid droplets and crystals | Fig6D (PWK 28), Fig6F (PWK 28), FigS13 (PWK 14) | later ages | animal | present |
| Proteome | Fig8A (PCA), Fig8C (Apod, Ptgds) | **PWK 14 and PWK 28 only** | animal (8 per genotype) | present |
| Lipidome and metabolome | Fig8G (PCA), Fig8I (z-scores of lipid groups) | **PWK 14 and PWK 28 only** | animal (9 to 14) | present |
| Behaviour and body | Fig1D, FigS1, FigS2 | not age-labelled in the sheets | animal | present |
No sheet holds a lipid, proteome or energy value at PWK 1 or PWK 7. The proteome and lipid sheets are, by their own labels and legend, PWK 14 and 28 only, and the proteome and lipid species tables (S6 Table and the lipid lists) are separate files, not in this workbook.

## STEP 2 (the only PWK 7 per-animal material: the synapse sheets)
| Readout | PWK 1 | PWK 7 | PWK 14 | PWK 28 |
|---|---|---|---|---|
| Fig3A cortex: genes with P < 0.05 against 1 (of 23; chance about 1.2) | 1 (down) | **3 up** (Synpo, Grm2, Syngap1; Synpo all six animals above 1) | 12 down | 19 down |
| Fig3A hippocampus (of 23) | **10 up** (all up) | **4 down** (Dlg2, Kalrn, Git1, Homer2; Dlg2 and Kalrn every animal below 1) | 12 down | 8 down |
| Fig3B cortex proteins with Welch P < 0.05 (of 10; chance about 0.5) | 2 | 3 (WAVE1, Shank3, CYFIP2) | 6 | 7 |
| Fig3B hippocampus proteins (of 10) | 2 | 2 (WAVE1, CYFIP2) | 5 | 7 |
* **The PWK 7 protein signs are the mutated complex itself, not a downstream sign.** CYFIP2 and WAVE1 are already lower at PWK 1 and stay lower at every age (POST-HOC, R87C/WT: cortex CYFIP2 0.76, 0.59, 0.52, 0.57; cortex WAVE1 0.42, 0.25, 0.37, 0.32; hippocampus CYFIP2 0.71, 0.63, 0.81, 0.60; hippocampus WAVE1 0.41, 0.31, 0.34, 0.29). A genotype effect that is constant from PWK 1 cannot pre-date a chronology: it is present before everything.
* **The transcript signs at PWK 7 are weak and opposite by region.** By the pre-registered S-early rule (three or more in one direction, one with every animal beyond, two with an interval excluding no change) both regions formally qualify (cortex up, hippocampus down), but with unadjusted P values: 3 of 23 and 4 of 23 against about 1.2 expected (binomial tail for at least 3 of 23 at 0.05: 0.11; for at least 4: 0.03); the genes differ by region and change sign; there are no WT animals in the sheet, so "beyond every WT animal" cannot be checked, only "beyond the normalised WT mean". The large, coherent, one-direction transcript change comes later (cortex 12 and 19 genes down at PWK 14 and 28, after documented daily seizures) and, in the hippocampus, at PWK 1 (10 of 23 up), which sits on the neonatal clock already found for IBA1 in ADV-165. I call the PWK 7 synaptic transcript set weak and non-coherent; it is of the synaptic family, not of the metabolic one.
* **Lipid, again, after.** Astrocytic lipid droplets are not significantly different at PWK 14 (Fig. S13: WT eight animals all zero; R87C seven animals with two non-zero, 2.9 and 4.2 spots; Welch P 0.18, complete separation absent) and are higher at PWK 28 (Fig6D: WT 0.97, 2.92, 2.92 against R87C eight animals with a mean of 19.9, six of eight above every WT value; P 0.035 with three WT animals; text confirms "but not at PWK 14"). Crystals are scored only at PWK 28 ("crystal analysis was not performed at that time point" at PWK 14). So in this model the lipid sign follows the glial and seizure chronology; it is not a sign before onset, and no lipid value exists at PWK 1 or 7.
* **PWK 7 is not pre-onset here.** ADV-165 established that behavioural recurrence is already daily at the first documented age (PWK 14) and that the authors propose neonatal spasm-like seizures to explain the PWK 7 Olig2 rise; so even a clean PWK 7 sign would be "early", not "before the first seizure".

## Rules against the pre-registration
* L-late holds: lipid and proteome values exist only at PWK 14 and 28, droplets only differ at PWK 28.
* Synapse PWK 7: formally S-early by the written rule in both regions, but of the synaptic family, with chance-level counts and opposite regional signs; no metabolic gene sits among the PWK 7 changes (the Fig 3A panel is synaptic genes by design: Cttn, Cacng7, Dlg1/2, Shank2/3, Homer2, Grm2, Syngap1, Unc13a, Kalrn, Git1, Gria2, Grid1, Lrrtm3 and others).
* Rule 1 therefore applies (L-late AND S-early of the synaptic family only). Rule 2 does not: no lipid, proteome or energy value at PWK 7 with a WT comparator exists, and no metabolic gene is among the PWK 7 transcript changes. Rule 3: the seizure-to-marker link stays missing; the sheets use "Animal n" labels per sheet with no identity key across sheets (and the seizure and marker cohorts are different).

## Consequence for the roadmap (ADV places the line; no IT work)
One dated line for RP-036 and RP-039: "ADV-171 (SCI, 2026-11-22, Ma 2025 S1 Data, 28 unread sheets inventoried; receipt FTR-20261122-41066510-02): no lipid, proteome or energy value exists at PWK 1 or 7; astrocytic lipid droplets are not different at PWK 14 and rise at PWK 28 (P 0.035, three WT animals); proteome and lipidome are PWK 14 and 28 only; the PWK 7 per-animal signs are the Cyfip2 complex proteins (constant from PWK 1) and a weak, region-opposite synaptic-transcript set. In this adjacent series the lipid sign follows onset; it supplies no 'abnormal lipid sign before onset' for RP-036 and no pre-onset energy sign for RP-039. Dataset closed for the metabolic family." RP-036's resume condition is not met by this series, and the held WWOX glucose history is unaffected.

## Limits and what would change this
Adjacent, non-WWOX, heterozygous missense knock-in; per-animal summaries, no per-cell data; Fig 3A holds only R87C animals normalised to the WT mean; PWK 14 is already post-onset; the proteome and lipid species tables are not in the workbook and were not opened; I did not recompute the paper's two-way ANOVA. What would change it: a lipid or energy readout at PWK 1 to 7 with WT animals (not in this paper), or a per-animal identity key linking the seizure and marker cohorts.

## Rejecting observation (restated)
A lipid, proteome or energy value at PWK 7 with WT and R87C animals would have overturned L-late; none exists. A metabolic gene among the PWK 7 transcript changes would have triggered rule 2; none is listed.
