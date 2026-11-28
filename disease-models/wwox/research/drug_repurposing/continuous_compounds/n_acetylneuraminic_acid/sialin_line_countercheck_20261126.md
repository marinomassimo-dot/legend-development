# Neu5Ac · comparison at the donor-line level

26 November 2026 · SCI_CODEX · WWOX comparison calibrated with SLC17A5-deficient human neural cells

## What the chemical measurements distinguish

In Sabir et al. the separate targeted UPLC–MS/MS assay measured elevated whole-cell free Neu5Ac in all SLC17A5-deficient cell types (Fig. 1B). The glycolipid assay measures released glycan peaks by NP-HPLC following GSL extraction and enzymatic cleavage. Each of the two affected and two control donor lines contributes three runs per cell type (Figs. 2C, 3A–B and Supplementary Table 3). This is a lysosomal transport disease at baseline. WWOX and substrate supplementation are separate questions. [Primary study](https://doi.org/10.1038/s41598-025-12682-4) · [Source workbook](https://pmc-oa-opendata.s3.amazonaws.com/PMC12350760.1/41598_2025_12682_MOESM3_ESM.xlsx)

For each run, calculate GM3 divided by the peak labelled Lac and calculate (GM2 + GM1a + GD1a + GD1b + GT1b) divided by GM3. The first is a proximal product-to-acceptor ratio and the second relates selected downstream products to GM3. The workbook measures both in pmol/mg protein before taking ratios. The preparation releases the glycan moieties and does not retain ceramide acyl-chain identities. Arithmetic mean of the three within-run ratios gives each donor line equal weight. This is a descriptive steady-state comparison with two unrelated lines per group, not a flux estimate or a statistical test. [All donor-level results](sialin_line_means.tsv)

| Cell type | GM3/Lac, affected lines | GM3/Lac, control lines | Selected downstream/GM3, affected lines | Selected downstream/GM3, control lines |
| --- | --- | --- | --- | --- |
| Cortical neurons | 98.04, 151.37 | 92.34, 35.92 | 0.59, 0.39 | 0.48, 6.59 |
| Immature astrocytes | 17.77, 19.75 | 5.29, 12.19 | 7.87, 5.23 | 13.55, 6.15 |
| Mature astrocytes | 46.02, 5.22 | 3.64, 6.01 | 0.73, 4.91 | 15.02, 8.72 |

The large ratio for cortical control line 2 accompanies **230 pmol/mg GM3** and **1,515 pmol/mg** selected downstream gangliosides. Cortical control line 1 has **1,049** and **462 pmol/mg**, respectively, and is inside the affected-line range on the ratio. In mature astrocytes the two affected lines have **778** and **96 pmol/mg GM3** and their selected downstream sum is **556** and **472 pmol/mg**, compared with **572** and **577 pmol/mg** in controls. The mature-cell example shows a reduced ratio driven by increased GM3 with far smaller changes in the downstream sum. Neither global hyposialylation nor successful mature product formation can be inferred from a single ratio or elevated whole-cell free parent.

## Consequence for the WWOX test

Carry absolute pool sizes and two branch measures in the same stage-matched samples. Normalize NCAM-associated output to total NCAM and quantify the ganglioside acceptor, GM3 and at least one expressed downstream species. If Neu5Ac increases the GM3 signal without increasing the preselected mature product or improving evoked function, the result is compatible with turnover, compartmental retention or impaired downstream processing. Test isotope transfer and the temporal ordering of changes before choosing among those possibilities. Current WWOX evidence is transcript-level. The SLC17A5 comparison supplies assay controls and does not establish a WWOX transport lesion, systemic exposure or benefit.

**Decision.** Defer pediatric trial priority. The decision would change only with a stage-matched WWOX deficit in donor or mature product, selective repletion and preserved circuit function at free exposure that can be attained. The next desk check is limited to identifying an existing matched WWOX metabolomics or glycoconjugate resource or a chemically specific developmental delivery dataset. Neither the source authors' basal genetic comparison nor the donor reanalysis is evidence for an oral Neu5Ac response.

## Replay

The CC BY 4.0 source workbook is Supplementary Table 3. File `41598_2025_12682_MOESM3_ESM.xlsx` has SHA-256 `7ee5ba16230b1385d41b3df602d21aae4f7ace70516c85583ecbb388a2e16dcb`. This repository holds the derived output and the parser. Point the parser to a local copy of the linked workbook.

```sh
python3 -B disease-models/wwox/research/drug_repurposing/continuous_compounds/n_acetylneuraminic_acid/sialin_by_donor.py 41598_2025_12682_MOESM3_ESM.xlsx > /tmp/sialin_line_means.tsv
```
