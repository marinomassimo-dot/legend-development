# COMMIT CANDIDATE — CC-20261004w8-C-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist`, Scientist C of intake wave 8, 2026-10-04.
**Change class:** **MINOR.** It creates registry presence for six papers that have none; narrows no claim, reverses none.
`context_policy: SOURCE_FIRST`. **Not medical advice.**

## 0 · Why

`paper_packet.py packet --pmid N` for each PMID at the start showed no identity, no manifest, no receipt. Each PMID needs a `PAPER` and a `LIT` record in the same section (PMID in both) to avoid `ORPHAN_COMPLETE_READ`. All six are off-WWOX by measurement (zero occurrences in each JATS).

## 1 · Numbers are provisional

`registry_records.py catalog` in this worktree at main commit 520c7266da8f: highest `PAPER 200`, highest `LIT-0493`. Wave-7 and other wave-8 candidates also claim 201 onward, so this candidate uses a disjoint provisional block, **PAPER 281-286 and LIT-0581-0586**; the integrator renumbers into the next free numbers in event order.

## 2 · Ops — `disease-models/wwox/registries/paper_registry_current.md` (op `append`, new record each, no `old`)

| provisional id | PMID | record text |
|---|---|---|
| `PAPER 281` | 42137263 | **Title:** DNA damage/p53, innate immune, and unfolded protein responses are activated in primate liver after toxic, high-dose AAV-SMN1 delivery · **Year:** 2026 · **Journal:** Mol Ther Nucleic Acids · **DOI:** 10.1016/j.omta.2026.201682 · **PMCID:** PMC13148890 · **WWOX content:** none (zero occurrences) · **Why held:** primary behind the liver-UPR commentary; reanalysis of monkey and rat liver RNA-seq after intravenous AAV9-PHP.B-SMN1, n = 2 per sex per dose · **Reading:** `FTR-20261004-42137263-01` (partial_fulltext_read) · **Dossier:** `research/fulltext_dossiers/PMID42137263.md` |
| `PAPER 282` | 30073179 | **Title:** Toxicology Study of Intra-Cisterna Magna Adeno-Associated Virus 9 Expressing Human Alpha-L-Iduronidase in Rhesus Macaques · **Year:** 2018 · **Journal:** Mol Ther Methods Clin Dev · **DOI:** 10.1016/j.omtm.2018.06.003 · **PMCID:** PMC6070681 · **WWOX content:** none · **Why held:** first of two rhesus ICM toxicology primaries; three-animal immunosuppression arm; single day-90 necropsy for DRG · **Reading:** `FTR-20261004-30073179-01` (partial_fulltext_read) · **Dossier:** `research/fulltext_dossiers/PMID30073179.md` |
| `PAPER 283` | 30073178 | **Title:** Toxicology Study of Intra-Cisterna Magna Adeno-Associated Virus 9 Expressing Iduronate-2-Sulfatase in Rhesus Macaques · **Year:** 2018 · **Journal:** Mol Ther Methods Clin Dev · **DOI:** 10.1016/j.omtm.2018.06.004 · **PMCID:** PMC6070702 · **WWOX content:** none · **Why held:** companion with a different cargo, same capsid, promoter, route and species; five-animal immunosuppression arm · **Reading:** `FTR-20261004-30073178-01` (partial_fulltext_read) · **Dossier:** `research/fulltext_dossiers/PMID30073178.md` |
| `PAPER 284` | 35229008 | **Title:** Characterization of AAV-mediated dorsal root ganglionopathy · **Year:** 2022 · **Journal:** Mol Ther Methods Clin Dev · **DOI:** 10.1016/j.omtm.2022.01.013 · **PMCID:** PMC8851102 · **WWOX content:** none · **Why held:** controlled cynomolgus ICM experiment with an expression-null AAV9 arm, three purification routes, nerve conduction, IENFD and MRI; sponsor-authored · **Reading:** `FTR-20261004-35229008-01` (partial_fulltext_read) · **Dossier:** `research/fulltext_dossiers/PMID35229008.md` |
| `PAPER 285` | 41438872 | **Title:** AAV-PHP.eB achieves superior neuronal transduction over AAV9 in pigtail macaques following intracerebroventricular administration · **Year:** 2025 · **Journal:** Mol Ther Methods Clin Dev · **DOI:** 10.1016/j.omtm.2025.101636 · **PMCID:** PMC12721033 · **WWOX content:** none · **Why held:** capsid-versus-capsid transduction comparison after ICV, n = 3 per capsid; no toxicity endpoint · **Reading:** `FTR-20261004-41438872-01` (partial_fulltext_read) · **Dossier:** `research/fulltext_dossiers/PMID41438872.md` |
| `PAPER 286` | 42198847 | **Title:** Death following high-dose AAV9 gene therapy in a patient with advanced SMA-PME · **Year:** 2026 · **Journal:** Mol Ther · **DOI:** 10.1016/j.ymthe.2026.05.016 · **PMCID:** PMC13464153 · **WWOX content:** none · **Why held:** human boundary case for high-dose systemic AAV9; single fatal case, class-level description only · **Reading:** `FTR-20261004-42198847-01` (partial_fulltext_read) · **Dossier:** `research/fulltext_dossiers/PMID42198847.md` |

## 3 · Ops — `disease-models/wwox/registries/literature_tracking_log_current.md` (op `append`, new record each)

| provisional id | PMID | record text |
|---|---|---|
| `LIT-0581` | 42137263 | Intake wave 8, 2026-10-04, Scientist C. Status `read — partial`. Off-WWOX by measurement; held as the primary behind the liver-UPR commentary. Receipt `FTR-20261004-42137263-01`. Manifest `.../deepdive_manifests/PMID42137263.json` (PASS). Registry twin: `PAPER 281`. |
| `LIT-0582` | 30073179 | Same wave and scientist. Status `read — partial`. Receipt `FTR-20261004-30073179-01`; manifest PASS; twin `PAPER 282`. |
| `LIT-0583` | 30073178 | Same. Receipt `FTR-20261004-30073178-01`; manifest PASS; twin `PAPER 283`. |
| `LIT-0584` | 35229008 | Same. Receipt `FTR-20261004-35229008-01`; manifest PASS; twin `PAPER 284`. |
| `LIT-0585` | 41438872 | Same. Receipt `FTR-20261004-41438872-01`; manifest PASS; twin `PAPER 285`. |
| `LIT-0586` | 42198847 | Same. Receipt `FTR-20261004-42198847-01`; manifest PASS; twin `PAPER 286`. |

## 4 · Reading debts discharged

The two 2018 primaries were named as "not read here" behind the wave-7 rebound relay; the liver primary stood behind the liver commentary. Wording checks are in `CC-20261004W8-C-IMMUNOSUPPRESSION-PRIMARIES-01` and `CC-20261004W8-C-SYSTEMIC-BOUNDARY-01`. FT-193's note that the Grubor 2025 source is "unread" is outside this group (wave 7 / other scientists).

### LOCATOR TRIPLES FOR BLIND AUDIT

No scientific proposition is changed by this candidate; identity facts only.

- [PMID 42137263, artefact `files/fulltext/PMID42137263_Moeini2026_PMC.xml`] (The data are a secondary analysis of earlier liver RNA-seq. | These RNA-seq data were originally used only for SMN1 transgene expression analysis | Materials and methods, para 1)
