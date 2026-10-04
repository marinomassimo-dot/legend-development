# CC-20261004W9-B-REGISTRY-01 — registry landing for the six group-B PMIDs of intake wave 9

- `context_policy: SOURCE_FIRST`
- Change class: **MINOR.** No claim is created, narrowed or reversed. The candidate gives each PMID a structured landing so none becomes an orphan complete-read (`ORPHAN_COMPLETE_READ`).
- Sources: PMID 23179753, 24935251, 26272509, 27188386, 32355866, 35333110. All six are first readings; every manifest `VERDICT: PASS` (`deepdive_manifest.py --pmid <PMID> --verify-artifacts --require-current-schema`). **All six are `partial_fulltext_read`** (figures and supplements are `captions_only` or `not_read` in the receipts; none claims a complete read).
- Receipts prepared and not appended: `scratchpad/receipts_pending_w9/sciB_<pmid>_1.json`, event ids `FTR-20261004-<pmid>-01`.
- **Nothing here is medical advice.** **None of the six mentions WWOX in its running text.** The four valproate primaries carry WWOX only as probe-set rows in supplementary tables (see `CC-20261004W9-B-VPA-DIRECTION-01`); the two gene-therapy papers do not carry the gene at all.

## Registry presence needed, per PMID

`registry_records.py get --pmid <PMID>` returned no `PAPER` and no `LIT` record for any of the six, and `fulltext_receipts.py status --pmid <PMID>` returned no receipt. Each needs **both** a `PAPER` and a `LIT` record. No existing registry statement rests on any of the six, except the cited-and-unread rows below.

## Next-free identifiers — PROVISIONAL

Measured with `registry_records.py catalog` after merging `main` at `781a3d2`, 2026-10-04: `PAPER` max **216**, `LIT` max **LIT-0508**. Declared provisional; other branches land continuously (wave 8 already asks for `PAPER 222`) and the integrator renumbers.

| # | PMID | Provisional PAPER | Provisional LIT |
|---|---|---|---|
| B1 | 23179753 | PAPER 217 | LIT-0509 |
| B2 | 24935251 | PAPER 218 | LIT-0510 |
| B3 | 26272509 | PAPER 219 | LIT-0511 |
| B4 | 27188386 | PAPER 220 | LIT-0512 |
| B5 | 32355866 | PAPER 221 | LIT-0513 |
| B6 | 35333110 | PAPER 222 | LIT-0514 |

## Ops

### 1 · `disease-models/wwox/registries/paper_registry_current.md`

Op: `insert-after` chained from the current final `PAPER` record (the integrator authors the records from the persisted artefacts' JATS front matter, as in earlier waves). Field set of `PAPER 132`: Short title · Full title · Authors · Year · Source type · Journal/source · Identifier · Status · Record provenance · Evidence depth · Primary pathway · Model/species · Genotype/model · Transferability · clinical relevance · Claim links · Role · LIT link · Note.

Common to all six: `Status: processed`; `Record provenance: created by CC-20261004W9-B-REGISTRY-01 (intake wave 9 2026-10-04, Scientist B)`; `Evidence depth: partial_fulltext_read` with the `FTR-20261004-<pmid>-01` receipt and the manifest and dossier paths; `Genotype/model: no WWOX allele; WWOX not mentioned in the text`; `Transferability: T3`; `clinical relevance: BACKGROUND — transferable lesson only, not evidence`; `Claim links: none — no canonical claim is touched`; `Note: class-level record; no individual-level detail is carried in this public edition. Not medical advice.`

| record | Short title (measured) | Journal, year, volume | Primary pathway | Model/species | Role |
|---|---|---|---|---|---|
| PAPER 217 | Krug 2013 Arch Toxicol — hESC-derived test systems for developmental neurotoxicity: a transcriptomics approach | Arch Toxicol 2013;87(1):123-43 (DOI 10.1007/s00204-012-0967-3) | none (toxicogenomics background; no WWOX pathway) | H9 human embryonic stem cells, five differentiation systems | Platform paper behind a curated valproate row; supplement lists WWOX probe sets up with valproate at 1.05 to 2 mM in two neural-lineage systems; text silent on WWOX |
| PAPER 218 | Balmer 2014 Arch Toxicol — transient transcriptome responses to disturbed neurodevelopment: histone acetylation and methylation | Arch Toxicol 2014;88(7):1451-68 (DOI 10.1007/s00204-014-1279-6) | none (as above) | H9 hESC to neuroepithelial precursors | HDAC-inhibitor time-course; one WWOX probe set up (1.574, adjusted p 0.042) at 600 uM valproate for 4 days; one untreated developmental WWOX row down (0.59); text silent on WWOX |
| PAPER 219 | Rempel 2015 Arch Toxicol — transcriptome-based classifier for developmental toxicants, HDAC inhibitors | Arch Toxicol 2015;89(9):1599-618 (DOI 10.1007/s00204-015-1573-y) | none (as above) | H9 hESC neural induction, 12 compounds | Genome-wide supplementary table: three of five WWOX probe sets up with valproate (1.33 to 1.68; adjusted p 0.007 to 0.027) at 600 uM, 6 days; text silent on WWOX |
| PAPER 220 | Shinde 2017 Arch Toxicol — transcriptome-based developmental indices, STOP-Toxukn and STOP-Toxukk | Arch Toxicol 2017;91(2):839-864 (DOI 10.1007/s00204-016-1741-8) | none (as above) | H9 hPSC, two systems | Signed-fold supplementary table: WWOX up with valproate in both systems (+2.127, +1.683); Table 7 lists the probe set at 1000 uM without direction; shares data with PAPER 219 and PAPER 217 |
| PAPER 221 | Bey 2020 Mol Ther Methods Clin Dev — intra-CSF AAV9 and AAVrh10 in nonhuman primates | Mol Ther Methods Clin Dev 2020;17:771-784 (DOI 10.1016/j.omtm.2020.04.001) | P7 gene-therapy design / BLOCK-1 safety | cynomolgus macaque (n = 8), GFP reporter | Descriptive DRG baseline for lumbar-intrathecal and ICV AAV9/AAVrh10 under triple immunosuppression, 3 weeks. **First author is Bey; not Hordeaux.** One cited reference (a retracted 2022 SMA paper) is a citation-only dependency |
| PAPER 222 | Hordeaux 2022 Hum Gene Ther — efficacy and safety of a Krabbe disease gene therapy | Hum Gene Ther 2022;33(9-10):499-517 (DOI 10.1089/hum.2021.245) | P7 gene-therapy design / BLOCK-1 safety | Twitcher mouse, Krabbe dog, rhesus macaque (GLP) | ICM AAVhu68 dose-response DRG baseline without immune suppression, 3 and 6 months, secreted-enzyme cargo; DRG score at most 1, dorsal axonopathy up to 3 at the high dose |

### 2 · `disease-models/wwox/registries/literature_tracking_log_current.md`

Op: `insert-after` chained from the current final `LIT` record, `LIT-0509` to `LIT-0514`. Field set of `LIT-0431`: Short title · Authors · Year · Source type · Journal/source · Identifier type · Identifier value · Date discovered · Date processed · Discovery source (`intake wave 9 selection record, group B`) · Status (`processed`) · Status note · Primary pathway · Species · Transferability (`T3`) · clinical relevance (`BACKGROUND`) · PAPER link (`PAPER 217` to `PAPER 222`).

## Registry statements about these papers compared with the sources

- `PAPER 222` of wave 8 (PMID 41254692) and the lead `DL-REPO-003` rest on the four valproate primaries: the CTD row says "Decreases expression" while all four primaries show WWOX up or silent (`CC-20261004W9-B-VPA-DIRECTION-01`). That candidate proposes the exact correction to the lead.
- The wave-9 selection's label "Hordeaux 2020" for PMID 32355866 is wrong; the paper is Bey 2020 with Hordeaux as a mid-list author. No held record carries the wrong label (`git grep` of the PMID finds none outside this wave), so nothing is corrected in the registries; the correction is carried by the new `PAPER 221` title.

## Reading-debt discharge

Four of the five primaries behind the valproate row of PMID 41254692 Table S7 are now read; the fifth (PMID 28001369) remains unread and paywalled. The two gene-therapy papers are references of the DRG reference chain around PMID 42137271 and discharge no registry statement by themselves (no held statement names them).
