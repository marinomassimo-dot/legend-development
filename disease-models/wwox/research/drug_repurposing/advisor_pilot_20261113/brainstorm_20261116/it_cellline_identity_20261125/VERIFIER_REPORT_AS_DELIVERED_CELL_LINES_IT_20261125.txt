<!-- As delivered by one blind delegate (legend-delegate, claude-sonnet-5-5, effort high). Not edited below this line. -->
# Blind verification: cell-line identity against Cellosaurus 57.0

Hypothesis-level; nothing here is medical advice. Register: local `cellosaurus.txt`, version 57.0 (22-October-2026), 169,026 entries, own parser (`scripts/parse.py`, output `out/matches.txt`). Article metadata and one full text are from PubMed / PMC.

## Task 1. Flagged lines among the 78 names

Eight names carry a "Problematic cell line" comment (for U87MG, only one of its two records).

| Name | Record | Exact comment |
|---|---|---|
| BGC-823 | CVCL_3360 | "Contaminated. Shown to be a HeLa derivative (CCRID; PubMed=26116706; PubMed=28851942). Originally thought to be a gastric adenocarcinoma." |
| SGC-7901 | CVCL_0520 | "Contaminated. Shown to be a HeLa derivative (PubMed=26116706; PubMed=28851942). Originally thought to originate from the lymph node of a 56 year old female patient with a gastric carcinoma." |
| SMMC-7721 | CVCL_0534 | "Contaminated. Shown to be a HeLa derivative (PubMed=26116706; PubMed=28807831). Originally thought to originate from a hepatocellular carcinoma." |
| HO-8910 | CVCL_6868 | "Contaminated. Shown to be a HeLa derivative (PubMed=26116706; CCRID). Originally thought to originate from the ascites of a 51 year old female patient with ovarian serous cystadenocarcinoma." |
| CNE2 | CVCL_6889 (CNE-2) | "Contaminated. On the basis of the STR profile (PubMed=18196576) it is identical to CNE-1 and seems to be a hybrid of HeLa and of cell line of unknown origin. Originally thought to originate from a 68 year old male patient with a nasopharyngeal carcinoma." |
| HepG2 | CVCL_0027 | "Misclassified. Originally thought to be a hepatocellular carcinoma cell line but shown to be from an hepatoblastoma (PubMed=19751877)." |
| SH-SY5Y | CVCL_0019 | "Partially contaminated. Some laboratories that are redistributing this cell line are in fact redistributing a contaminated cell line of mouse origin (PubMed=25182563)." |
| U87MG (ambiguous) | CVCL_0022 (U-87MG ATCC) | "Misidentified. This cell line is not the original glioblastoma cell line established in 1968 at the University of Uppsala. As described in PubMed=27582061 it is most probably also a glioblastoma cell line but whose origin is unknow. See U-87MG Uppsala (Cellosaurus=CVCL_GP63) for the original U-87MG cell line." |
| U87MG (ambiguous) | CVCL_GP63 (U-87MG Uppsala) | No Problematic comment. Both records list "U87MG" as a synonym. SX: ATCC = Male, age unspecified; Uppsala = Female, 44Y. |

### Flagged relatives (not in LINES.tsv; relevant if a paper used one)

- CNE-1 (CVCL_6888): "Contaminated ... identical to CNE-2 ... hybrid of HeLa". CNE-2Z and CNE2-IR: "Probably contaminated".
- HO-8910PM (CVCL_0310), HO8910-TAX/CBP, SGC-7901 sublines, BGC-823/DOX: "Contaminated" via the parent. U-87MG ATCC has many flagged derivatives.
- Ishikawa (Heraklio) 02 ER- ("Probably misclassified/misidentified") and MCF-7 TH ("Contaminated", OVCAR-8) are flagged; the parent names in the list are not.

### Ambiguous, resolved only by synonym, or not found

| Name | What the register gives (none of these is flagged) |
|---|---|
| AC16 | No unqualified ID. Two homonyms: "AC16 [Human hybrid cardiomyocyte]" CVCL_4U18; "AC16 [Mouse mesothelioma]" CVCL_LJ81 |
| XG218 | Only a synonym of a mouse ES clone (CVCL_PT50). If something else was meant, treat as not found. I found no use of the string in registries, ledgers or analysis |
| H1299 / L929 / RPE-1 / KHOS / K7M2 | Synonym only: NCI-H1299, NCTC clone 929, hTERT-RPE1, KHOS/NP, K7M2-WT |
| H9 (hESC) | WA09 CVCL_9773; the ID "H9" (CVCL_1240) is a different, cancer line |
| PC-3, PC12, HT-29, HAP1, HOS, SCC-9 | Homonyms exist (e.g. rat PC12 CVCL_0481 vs human PC-12; mouse HAP-1; dog HOS) |
| HEK293 family, CHO, MC3T3 | Families; matched at the parent record only (MC3T3-E1 is CVCL_0409) |

All other names matched a record with no Problematic comment (including HeLa itself).

## Task 2. Verdicts

| ID | Verdict | One line |
|---|---|---|
| K1 | SUPPORTED | All four "Contaminated ... HeLa derivative"; the stated tissue is what was "originally thought" |
| K2 | SUPPORTED | Understated: CNE-2 is also identical to CNE-1, which is flagged too |
| K3 | SUPPORTED, with a qualifier | "most probably" a glioblastoma. More than a name changes: donor unknown, sex differs from the Uppsala original |
| K4 | PARTLY | Misclassification: yes. "Label only" is too weak where a record's claim is HCC-specific |
| K5 | PARTLY | The register says a mouse-origin line is redistributed in its place by some labs, and says nothing about consequences |
| K6 | PARTLY (second half NOT SUPPORTED) | The abstract does give a WWOX result for SNU-719; it gives none for AGS |
| K7 | SUPPORTED | Same line, same Xuzhou department, same author; two drugs, one biological system |
| K8 | Answer: YES for SH-SY5Y | No neural statement rests on a HeLa-derived line; several rest on SH-SY5Y, one without naming it |

## Evidence

### K3, K4, K5
- K3: the Uppsala record's Caution says the line "distributed by most cell collections (including ATCC, CLS, ECACC, etc.) is a different cell line". A paper saying only "U87MG" cannot be assigned from the name.
- K4: hepatoblastoma is a different tumour entity from HCC. `discovery_ledger_current.md:455` says "modelli HCC" for PMID 28708106, whose lines are HepG2 and mouse Hepa1-6.
- K5: "changes no statement unless shown" is a policy choice. A paper with no authentication cannot show it either way: PMID 22193544 methods say "Human neuroblastoma SH-SY5Y cells were maintained in ..." and my keyword search of its body (ATCC, authentication, mycoplasma) showed no supplier or authentication statement.

### K6 (overturned in part)
According to PubMed, PMID 25720522 ([DOI](https://doi.org/10.1007/s12032-015-0525-y)) abstract: "Treatment with 5-aza-dC and/or TSA induced upregulation of RNA expression of **all five genes in SNU-719**; meanwhile, individual gene expression increased in EBVnGC cell lines."
- WWOX is one of the five, so the SNU-719 result is stated per line: WWOX transcript up.
- For SGC-7901, BGC-823 and AGS the abstract does not say which gene rose in which line. So AGS cannot support a WWOX result from the abstract. The gastric attribution of a WWOX increase rests on **SNU-719 alone**, not "SNU-719 and AGS".
- Same error in two repository places:
  - `analysis/wwox_expression_boost_census_20260922.md:144` (A7): "not separated per gene in abstract".
  - `research/discovery_ledger_current.md:3790`: PMID 25720522 "does not give WWOX's own result". NOT SUPPORTED for SNU-719. The treatment is "and/or", so the abstract does not say which drug arm did it.

### K7
According to PubMed, PMID 24137423 ([DOI](https://doi.org/10.3892/ol.2013.1438), full text PMC3789030): "The HO-8910 human ovarian cancer cell line was obtained from the Department of Obstetrics and Gynecology Laboratory of the Affiliated Hospital of Xuzhou Medical College". PMID 23464470 ([DOI](https://doi.org/10.7314/apjcp.2012.13.12.6429)) is by Yan Hong-Chao of the same department; Yan Hongchao is first author of the other. I saw no authentication statement in the 2013 full text.
- The census banner at line 132 already says neither row is ovarian. The row cells at lines 139 and 153 still read "human ovarian cancer line", and U4 (line 379) still says "probably not independent".

### K8. Records in registries/*_current.md and research/*_ledger_current.md
Paths are under `disease-models/wwox/`.

**A. Neural or neural-like statements (SH-SY5Y, partially contaminated flag)**

| Where | What leans on the line |
|---|---|
| `registries/claim_registry_current.md:729-750` (CLAIM 035; lines 734, 743) | Neuronal output (neurite outgrowth, including WWOX RNAi in retinoic-acid SH-SY5Y) from PMID 22193544. This **is a WWOX-depleted neural-like system** |
| `registries/working_model_current.md:76` | "restoring Tau-driven microtubule assembly and neurite outgrowth" (same source; line not named there) |
| CLAIM 016 in the claim registry | Cites CLAIM 035 / PAPER 056 as its added mechanism |
| `research/discovery_ledger_current.md:1660, 1696` (DL-MECH-064, -066) | SH-SY5Y neurite results; 1660 states the single-line limit |
| `research/dismissal_ledger_current.md:278` | WWOX-Tau non-interaction wording in SH-SY5Y |
| `research/therapeutic_hypotheses_ledger_current.md:100-102` (HYP-20260705-05) | Says the evidence is "in **NEURONI**" (in neurons). The source (PMID 35984507) says "mainly performed in differentiated SH-SY5Y neuroblastoma cells" (plus GK rat brain homogenates). A grep of that ledger for "SY5Y" or "neuroblastom" returns nothing |
| `research/discovery_ledger_current.md:285` | "in sistema neuronale ... cellule neuronali" for the same PMID; line not named |
| `registries/claim_registry_current.md:270`, `registries/working_model_current.md:152` | PMID 42395553 SH-SY5Y dose series used to qualify the neuron-arm dose |
| `research/dismissal_ledger_current.md:389` | gamma-H2AX in SH-SY5Y overexpression (same preprint) |

PMID 35984507: According to PubMed, [DOI](https://doi.org/10.1007/s00018-022-04508-7). PMID 22193544: [DOI](https://doi.org/10.1038/cdd.2011.188). Nothing I checked shows that any of these papers' stocks was the mouse contaminant, or that any was authenticated.

**B. Tissue label carries something, non-neural (or tumour glial)**

| Where | Line and label |
|---|---|
| `discovery_ledger_current.md:3790` | HO8910 (already relabelled as HeLa); SGC-7901/BGC-823 (noted); see K6 for the SNU-719 wording |
| `discovery_ledger_current.md:455` | HepG2 as "HCC models" (PMID 28708106; line not named) |
| `discovery_ledger_current.md:3457, 3566, 3568` | HepG2 reporter/EMSA for rs2548861; 3568 calls it "a hepatocyte line" (it is a hepatoblastoma line); it already says it speaks to nothing neural |
| `discovery_ledger_current.md:434-436` (DL-MECH-024) | PMID 27869163 used U87 (siWwox, HDR reporter), also HeLa and HEK293; U87 not named in the lines I read. A WWOX-depleted glioblastoma line; the record's neuron step is a proposed experiment |
| `discovery_ledger_current.md:1429-1430` | "quattro linee GBM" includes U87MG (stock identity per K3) |
| `claim_registry_current.md:270`, `working_model_current.md:152` | "1 of 4 glioblastoma lines" (PMID 37781246; the set includes U87MG) |
| `discovery_ledger_current.md:1484-1488` | PMID 36530994 used HepG2 with Huh7 and Alexander under an HCC label; I did not check which assay used which line |
| `paper_registry_current.md:3304-3305`, `4928`; `literature_tracking_log_current.md:7032, 7063, 9813` | CNE2 "nasopharyngeal" and SMMC-7721 "hepatoma" in titles; corpus placeholders, "Claim links: none" |
| `paper_registry_current.md:1556, 3777, 2155, 2481` | Flagged line **not visible in the record title**: HO8910 (PMID 32096174, also SKOV3; PMID 18953870), CNE1 (PMIDs 31966508, 31966718). Ovarian / nasopharyngeal titles |

**Outside LINES.tsv, found on the way.** `discovery_ledger_current.md:3790` says "hepatocellular lines with very low WWOX mRNA (PMID 15266310) report no increase". The full text does not name which lines were treated. Its low-expressor list includes **Chang** (Chang Liver, CVCL_0238: HeLa derivative), **SK-Hep-1** (CVCL_0525: misclassified, probably endothelial) and "7703" (QGY-7703, one candidate for that short name, is a HeLa derivative; identity not established). So "hepatocellular lines" is not secured for that negative.

## What I did not check

- Line use was screened from the PubMed abstracts of 860 PMIDs matched by a "PMID nnn" pattern in the eight files, and from PMC XML body text only for papers cited in the claim registry, working model and four ledgers that PMC served. 28 of those XML files had no body (including PMIDs 35984507, 42395553, 18460020) and 45 cited PMIDs had no PMC copy. Supplements and figures were not searched. Papers cited only in the paper registry or literature log were screened by abstract only. So section B is a lower bound; toosendanin HCC (PMIDs 34015398, 39894307), miR-153 and gastric PMID 20737170 were not resolved to lines.
- Records citing a paper without a PMID (by PAPER or CLAIM number only) were traced only where noted.
- Dependencies of CLAIM 016 and CLAIM 035 beyond the rows above were not walked; I did not judge whether those claims survive.
- Full text of PMIDs 25720522 and 23464470 not read (abstracts only). STR claims were not re-derived from the register's primary references (PMID 25182563 has no abstract in PubMed).
- No result report, commit candidate, or "advisor_pilot", "it_cellline" or "adv279" folder was opened. Repository records I read do carry dated notes labelled ADV-279 and an IT correction banner in the census; I judged from the register and the papers.
- No repository file edited; no e-mail address sent to any service (NCBI efetch was called with a generic tool name).
