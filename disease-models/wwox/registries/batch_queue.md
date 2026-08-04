# Batch queue — WWOX

> **Generated file — do not edit by hand.** Regenerate with:
> ```bash
> python3 framework/scripts/batch_queue.py --disease wwox \
>     --out disease-models/wwox/registries/batch_queue.md
> ```

## ▶ Start here

**272 records have not been processed.** **235** of them have a free full text and can be worked immediately.

| Verdict | Records | What it means |
|---|---:|---|
| 🟢 **`NEW`** | 42 | never seen by the system — **the front of the queue** |
| 🟢 **`CORPUS_CATALOGUED`** | 230 | catalogued and deduplicated, never analytically processed |
| 🟡 `OUT_OF_SCOPE_LIKELY` | 142 | no scope signal in the title — later in the queue, **never discarded** |
| 🟡 `AMBIGUOUS` | 6 | identifiers must be resolved before ingest |
| ⏳ `IN_PIPELINE` | 11 | already in flight |
| ✅ `KNOWN_INTEGRATED` | 28 | done — read depth in the table below |

The two green rows are the answer to *"where do I start?"*. The table further down lists
every record in this order, so a second person can take the next unclaimed row without
coordinating with anyone.

> **These verdicts are not computed here.** They come from the intake gate
> (`legend-study-intake-triage`), imported and run over the seed corpus, so the repository
> has exactly one classifier. An earlier version of this file answered with its own
> identifier join and left 45% of the corpus in an `unmatched` bucket that really meant
> "go and find out yourself" — a queue that hands the work back is not a queue.

## What this is for

If you want to run a batch and do not know where to take the papers from, take them
from here. This joins a **dated bibliography snapshot** against the registries and shows
what is still outstanding, most useful first.

Two files, two different natures. The seed corpus is a *snapshot* — it carries its date
and never claims to be current. The status column is *derived on every run*, so it cannot
quietly disagree with the canonical state. When a snapshot is exhausted, add another one
next to it; older snapshots stay valid as history.

**Seed corpus:** `corpus_seed_pubmed_20260705.tsv` — 459 records, 408 with free full text.
Coverage years: **2001–2026**; 161 records are from 2020 onward. This is therefore a
broad historical-plus-recent corpus, not a recent-only list.
The snapshots contain 459 export occurrences; 0 repeated occurrence(s) are deduplicated in this queue.

**Provenance and limit.** The current seed is an operator-curated PubMed Clipboard
export dated 2026-07-05. The exact upstream query and selection procedure were not
retained, so this is a useful worklist — **not a systematic or exhaustive WWOX search**.
`free_full_text=yes` records PubMed's `Free PMC article` flag at export time; it does
not redistribute or license the article text.

## Read depth of what *has* been touched

| Status | Records | Share |
|---|---:|---:|
| **Not found by identifier** — run the intake gate | 203 | 44% |
| **Catalogued, never processed** — the reading debt | 100 | 22% |
| Known to the tracking log only | 125 | 27% |
| Processed from the abstract | 8 | 2% |
| Partial full text read | 0 | 0% |
| Full text read | 23 | 5% |

⚠️ This second table combines registry state with the authoritative append-only
`fulltext_read_receipts.jsonl`. Historical registry-only full-text declarations remain
visible but are separated from receipt-backed completion in `coverage_report.md`.

> `unmatched` means the exact PMID/DOI join found nothing — not that the paper is new.
> Preprint-versus-published pairs, aggregate lines and title-only records need the intake
> gate, which does fuzzy matching and disambiguation this join deliberately does not:
> ```bash
> python3 .claude/skills/legend-study-intake-triage/scripts/study_dedup_triage.py \
>     --workspace . --input <your_export.txt> --out triage.md
> ```

## Complete outstanding queue

| PMID | Year | FT | Type | Status | Title |
|---|---:|:---:|---|---|---|
| [40191585](https://pubmed.ncbi.nlm.nih.gov/40191585/) | 2025 | ✅ | primary | unmatched | Identifying individuals with rare disease variants by inferring shared ancestral haplotypes from SNP array data |
| [37781246](https://pubmed.ncbi.nlm.nih.gov/37781246/) | 2023 | ✅ | primary | unmatched | Molecular landscapes of glioblastoma cell lines revealed a group of patients that do not benefit from WWOX tumor suppressor expression |
| [35715422](https://pubmed.ncbi.nlm.nih.gov/35715422/) | 2022 | ✅ | primary | unmatched | Analysis of clinical phenotypic and genotypic spectra in 36 children patients with Epilepsy of Infancy with Migrating Focal Seizures |
| [34948746](https://pubmed.ncbi.nlm.nih.gov/34948746/) | 2021 | ✅ | primary | unmatched | Effect of WW Domain-Containing Oxidoreductase Gene Polymorphism on Clinicopathological Characteristics of Patients with EGFR Mutant Lung Adenocarcinoma in Taiwan |
| [34204789](https://pubmed.ncbi.nlm.nih.gov/34204789/) | 2021 | ✅ | primary | unmatched | PLEK2, RRM2, GCSH: A Novel WWOX-Dependent Biomarker Triad of Glioblastoma at the Crossroads of Cytoskeleton Reorganization and Metabolism Alterations |
| [33520443](https://pubmed.ncbi.nlm.nih.gov/33520443/) | 2021 | ✅ | primary | unmatched | Identification of a novel association for the WWOX/HIF1A axis with gestational diabetes mellitus (GDM) |
| [32799870](https://pubmed.ncbi.nlm.nih.gov/32799870/) | 2020 | ✅ | primary | unmatched | Retraction Note: HGF and TGFβ1 differently influenced Wwox regulatory function on Twist program for mesenchymal-epithelial transition in bone metastatic versus parental breast carcinoma cells |
| [32509092](https://pubmed.ncbi.nlm.nih.gov/32509092/) | 2020 | ✅ | primary | unmatched | Aberrant expression of WWOX and its association with cancer stem cell biomarker expression |
| [31966058](https://pubmed.ncbi.nlm.nih.gov/31966058/) | 2020 | ✅ | primary | unmatched | Expression and clinical significance of WWOX, Elf5, Snail1 and EMT related factors in epithelial ovarian cancer |
| [31315632](https://pubmed.ncbi.nlm.nih.gov/31315632/) | 2019 | ✅ | primary | unmatched | A p53/TIAF1/WWOX triad exerts cancer suppression but may cause brain protein aggregation due to p53/WWOX functional antagonism |
| [31155927](https://pubmed.ncbi.nlm.nih.gov/31155927/) | 2019 | ✅ | primary | unmatched | Downregulation of WW domain-containing oxidoreductase leads to tamoxifen-resistance by the inactivation of Hippo signaling |
| [31008954](https://pubmed.ncbi.nlm.nih.gov/31008954/) | 2019 | ✅ | primary | unmatched | The clinicopathological significance of ubiquitin-conjugating enzyme E2C, leucine-rich repeated-containing G protein-coupled receptor, WW domain-containing oxidoreductase, and vasculogenic mimicry in invasive breast carcinoma |
| [31938155](https://pubmed.ncbi.nlm.nih.gov/31938155/) | 2018 | ✅ | primary | unmatched | Correlation of expression of WWOX and JNK with clinicopathologic features in human breast carcinoma |
| [30013442](https://pubmed.ncbi.nlm.nih.gov/30013442/) | 2018 | ✅ | primary | unmatched | Relationship of genetic variant distributions of WW domain-containing oxidoreductase gene with uterine cervical cancer |
| [29905011](https://pubmed.ncbi.nlm.nih.gov/29905011/) | 2018 | ✅ | primary | unmatched | Low expression of WW domain-containing oxidoreductase associates with hepatocellular carcinoma aggressiveness and recurrence after curative resection |
| [29675105](https://pubmed.ncbi.nlm.nih.gov/29675105/) | 2018 | ✅ | primary | unmatched | Association of WWOX rs9926344 polymorphism with poor prognosis of hepatocellular carcinoma |
| [29390993](https://pubmed.ncbi.nlm.nih.gov/29390993/) | 2018 | ✅ | primary | unmatched | Efficient strategy for the molecular diagnosis of intractable early-onset epilepsy using targeted gene sequencing |
| [29310145](https://pubmed.ncbi.nlm.nih.gov/29310145/) | 2018 | ✅ | primary | unmatched | Immunohistochemical WWOX Expression and Association with Angiogenesis, p53 Expression, Cell Proliferation and Clinicopathological Parameters in Cervical Cancer |
| [29069730](https://pubmed.ncbi.nlm.nih.gov/29069730/) | 2017 | ✅ | primary | unmatched | Inhibition of colorectal cancer genomic copy number alterations and chromosomal fragile site tumor suppressor FHIT and WWOX deletions by DNA mismatch repair |
| [28373548](https://pubmed.ncbi.nlm.nih.gov/28373548/) | 2017 | ✅ | primary | unmatched | Editorial Expression of Concern: WWOX gene restoration prevents lung cancer growth in vitro and in vivo |
| [27845895](https://pubmed.ncbi.nlm.nih.gov/27845895/) | 2017 | ✅ | primary | unmatched | Hyaluronan activates Hyal-2/WWOX/Smad4 signaling and causes bubbling cell death when the signaling complex is overexpressed |
| [27313745](https://pubmed.ncbi.nlm.nih.gov/27313745/) | 2016 | ✅ | primary | unmatched | Reduced expression of the WW domain-containing oxidoreductase in human hematopoietic malignancies |
| [27551470](https://pubmed.ncbi.nlm.nih.gov/27551470/) | 2015 | ✅ | primary | unmatched | Current questions and controversies in chromosome fragile site research: does WWOX, the gene product of common fragile site FRA16D, have a passive or active role in cancer? |
| [26055163](https://pubmed.ncbi.nlm.nih.gov/26055163/) | 2015 | ✅ | primary | unmatched | In Memoriam: Shur-Tzu (Su) Chen, a pioneer in tumor suppressor WWOX for neuroscience |
| [25659037](https://pubmed.ncbi.nlm.nih.gov/25659037/) | 2015 | ✅ | primary | unmatched | WWOX suppresses prostate cancer cell progression through cyclin D1-mediated cell cycle arrest in the G1 phase |
| [24959289](https://pubmed.ncbi.nlm.nih.gov/24959289/) | 2014 | ✅ | primary | unmatched | Evaluation of the mechanism of epithelial-mesenchymal transition in human ovarian cancer stem cells transfected with a WW domain-containing oxidoreductase gene |
| [24949445](https://pubmed.ncbi.nlm.nih.gov/24949445/) | 2014 | ✅ | primary | unmatched | The analysis of genetic aberrations in children with inherited neurometabolic and neurodevelopmental disorders |
| [24137423](https://pubmed.ncbi.nlm.nih.gov/24137423/) | 2013 | ✅ | primary | unmatched | Effects of 5-Aza-2'-deoxycytidine on the methylation state and function of the WWOX gene in the HO-8910 ovarian cancer cell line |
| [21347750](https://pubmed.ncbi.nlm.nih.gov/21347750/) | 2011 | ✅ | primary | unmatched | WWOX expression in colorectal cancer--a real-time quantitative RT-PCR study |
| [19918364](https://pubmed.ncbi.nlm.nih.gov/19918364/) | 2009 | ✅ | primary | unmatched | Dramatic co-activation of WWOX/WOX1 with CREB and NF-kappaB in delayed loss of small dorsal root ganglion neurons upon sciatic nerve transection in rats |
| [18974271](https://pubmed.ncbi.nlm.nih.gov/18974271/) | 2009 | ✅ | primary | unmatched | Targeted ablation of the WW domain-containing oxidoreductase tumor suppressor leads to impaired steroidogenesis |
| [18460020](https://pubmed.ncbi.nlm.nih.gov/18460020/) | 2008 | ✅ | primary | unmatched | Role of the WWOX gene, encompassing fragile region FRA16D, in suppression of pancreatic carcinoma cells |
| [18452537](https://pubmed.ncbi.nlm.nih.gov/18452537/) | 2008 | ✅ | primary | unmatched | Low levels of WWOX protein immunoexpression correlate with tumour grade and a less favourable outcome in patients with urinary bladder tumours |
| [17823927](https://pubmed.ncbi.nlm.nih.gov/17823927/) | 2007 | ✅ | primary | unmatched | WWOX hypomorphic mice display a higher incidence of B-cell lymphomas and develop testicular atrophy |
| [15070730](https://pubmed.ncbi.nlm.nih.gov/15070730/) | 2004 | ✅ | primary | unmatched | Functional association between Wwox tumor suppressor protein and p73, a p53 homolog |
| [35363364](https://pubmed.ncbi.nlm.nih.gov/35363364/) | 2022 | — | review | unmatched | Identification of epilepsy concomitant candidate genes recognized in Saudi epileptic patients |
| [29852413](https://pubmed.ncbi.nlm.nih.gov/29852413/) | 2018 | — | primary | unmatched | Diagnostic yield of targeted massively parallel sequencing in children with epileptic encephalopathy |
| [25517572](https://pubmed.ncbi.nlm.nih.gov/25517572/) | 2015 | — | primary | unmatched | The Functional Copy Number Variation-67048 in WWOX Contributes to Increased Risk of COPD in Southern and Eastern Chinese |
| [21276135](https://pubmed.ncbi.nlm.nih.gov/21276135/) | 2011 | — | primary | unmatched | Bmi1 regulates cell fate via tumor suppressor WWOX repression in small-cell lung cancer cells |
| [20542955](https://pubmed.ncbi.nlm.nih.gov/20542955/) | 2010 | — | review | unmatched | Signaling from membrane receptors to tumor suppressor WW domain-containing oxidoreductase |
| [12514174](https://pubmed.ncbi.nlm.nih.gov/12514174/) | 2003 | — | primary | unmatched | JNK1 physically interacts with WW domain-containing oxidoreductase (WOX1) and inhibits WOX1-mediated apoptosis |
| [11058590](https://pubmed.ncbi.nlm.nih.gov/11058590/) | 2001 | — | primary | unmatched | Hyaluronidase induction of a WW domain-containing oxidoreductase that enhances tumor necrosis factor cytotoxicity |
| [41124647](https://pubmed.ncbi.nlm.nih.gov/41124647/) | 2026 | ✅ | primary | catalogued only | Genetic and Functional Evidence Links Germline Biallelic Inactivating Variants in WWOX to Histological Mixed-Type Thyroid Cancer |
| [41141138](https://pubmed.ncbi.nlm.nih.gov/41141138/) | 2025 | ✅ | primary | catalogued only | Intertwined Relationship of WWOX and RUNX2 Proteins as a Biomarker for Predicting Response and Survival in Patients With Childhood Bone Cancer in North India: A Pilot Study |
| [38282791](https://pubmed.ncbi.nlm.nih.gov/38282791/) | 2024 | ✅ | primary | catalogued only | LncRNA HOTAIRM1 Inhibits the Proliferation and Invasion of Lung Adenocarcinoma Cells via the miR-498/WWOX Axis [Retraction] |
| [36498839](https://pubmed.ncbi.nlm.nih.gov/36498839/) | 2022 | ✅ | primary | catalogued only | Zfra Inhibits the TRAPPC6AΔ-Initiated Pathway of Neurodegeneration |
| [33691672](https://pubmed.ncbi.nlm.nih.gov/33691672/) | 2021 | ✅ | primary | catalogued only | In vitro and in silico assessment of the effect of WWOX expression on invasiveness pathways associated with AP-2 transcription factors in bladder cancer |
| [33536174](https://pubmed.ncbi.nlm.nih.gov/33536174/) | 2021 | ✅ | primary | catalogued only | Angiomotin Counteracts the Negative Regulatory Effect of Host WWOX on Viral PPxY-Mediated Egress |
| [32764489](https://pubmed.ncbi.nlm.nih.gov/32764489/) | 2020 | ✅ | primary | catalogued only | Therapeutic Zfra4-10 or WWOX7-21 Peptide Induces Complex Formation of WWOX with Selective Protein Targets in Organs that Leads to Cancer Suppression and Spleen Cytotoxic Memory Z Cell Activation In Vivo |
| [32606933](https://pubmed.ncbi.nlm.nih.gov/32606933/) | 2020 | ✅ | primary | catalogued only | LncRNA HOTAIRM1 Inhibits the Proliferation and Invasion of Lung Adenocarcinoma Cells via the miR-498/WWOX Axis |
| [32101017](https://pubmed.ncbi.nlm.nih.gov/32101017/) | 2020 | ✅ | primary | catalogued only | MiR-214 Mediates Cell Proliferation and Apoptosis of Nasopharyngeal Carcinoma Through Targeting Both WWOX and PTEN |
| [31933749](https://pubmed.ncbi.nlm.nih.gov/31933749/) | 2019 | ✅ | primary | catalogued only | The correlation of the expressions of WWOX, LGR5 and vasohibin-1 in epithelial ovarian cancer and their clinical significance |
| [31456594](https://pubmed.ncbi.nlm.nih.gov/31456594/) | 2019 | ✅ | primary | catalogued only | Circular RNA CircMTO1 Inhibits Proliferation of Glioblastoma Cells via miR-92/WWOX Signaling Pathway |
| [31428585](https://pubmed.ncbi.nlm.nih.gov/31428585/) | 2019 | ✅ | primary | catalogued only | Editorial: WW Domain Proteins in Signaling, Cancer Growth, Neural Diseases, and Metabolic Disorders |
| [31123603](https://pubmed.ncbi.nlm.nih.gov/31123603/) | 2019 | ✅ | primary | catalogued only | Strategies by which WWOX-deficient metastatic cancer cells utilize to survive via dodging, compromising, and causing damage to WWOX-positive normal microenvironment |
| [30746283](https://pubmed.ncbi.nlm.nih.gov/30746283/) | 2018 | ✅ | review | catalogued only | Novel Homozygous Mutation in the WWOX Gene Causes Seizures and Global Developmental Delay: Report and Review |
| [30335523](https://pubmed.ncbi.nlm.nih.gov/30335523/) | 2018 | ✅ | primary | catalogued only | The downregulation of WWOX induces epithelial-mesenchymal transition and enhances stemness and chemoresistance in breast cancer |
| [30307120](https://pubmed.ncbi.nlm.nih.gov/30307120/) | 2018 | ✅ | primary | catalogued only | Inhibition of miR-24 suppresses malignancy of human non-small cell lung cancer cells by targeting WWOX in vitro and in vivo |
| [30242144](https://pubmed.ncbi.nlm.nih.gov/30242144/) | 2018 | ✅ | primary | catalogued only | Expression of B Cell-Specific Moloney Murine Leukemia Virus Integration Site 1 (BMI-1) and WW Domain-Containing Oxidoreductase (WWOX) in Liver Cancer Tissue and Normal Liver Tissue |
| [29662317](https://pubmed.ncbi.nlm.nih.gov/29662317/) | 2018 | ✅ | primary | catalogued only | Association between WWOX and the risk of malignant tumor, especially among Asians: evidence from a meta-analysis |
| [29164763](https://pubmed.ncbi.nlm.nih.gov/29164763/) | 2018 | ✅ | primary | catalogued only | TMEM207 hinders the tumour suppressor function of WWOX in oral squamous cell carcinoma |
| [31966760](https://pubmed.ncbi.nlm.nih.gov/31966760/) | 2017 | ✅ | primary | catalogued only | Expression of ORAOV1, CD133 and WWOX correlate with metastasis and prognosis in gastric adenocarcinoma |
| [31966369](https://pubmed.ncbi.nlm.nih.gov/31966369/) | 2017 | ✅ | primary | catalogued only | Exogenous WWOX enhances apoptosis and weakens metastasis in CNE2 nasopharyngeal carcinoma cells through the intrinsic apoptotic pathway |
| [29152092](https://pubmed.ncbi.nlm.nih.gov/29152092/) | 2017 | ✅ | primary | catalogued only | The long non-coding RNA PARTICLE is associated with WWOX and the absence of FRA16D breakage in osteosarcoma patients |
| [28769061](https://pubmed.ncbi.nlm.nih.gov/28769061/) | 2017 | ✅ | primary | catalogued only | PARTICLE triplexes cluster in the tumor suppressor WWOX and may extend throughout the human genome |
| [28724435](https://pubmed.ncbi.nlm.nih.gov/28724435/) | 2017 | ✅ | review | catalogued only | WW domain-binding protein 2: an adaptor protein closely linked to the development of breast cancer |
| [28523049](https://pubmed.ncbi.nlm.nih.gov/28523049/) | 2017 | ✅ | primary | catalogued only | Expression of CD133, E-cadherin and WWOX in colorectal cancer and related analysis |
| [28521426](https://pubmed.ncbi.nlm.nih.gov/28521426/) | 2017 | ✅ | primary | catalogued only | Exploring the mechanism of WWOX growth inhibitory effects on oral squamous cell carcinoma |
| [28426730](https://pubmed.ncbi.nlm.nih.gov/28426730/) | 2017 | ✅ | primary | catalogued only | Functional genetic variant of WW domain-containing oxidoreductase (WWOX) gene is associated with hepatocellular carcinoma risk |
| [27655721](https://pubmed.ncbi.nlm.nih.gov/27655721/) | 2016 | ✅ | primary | catalogued only | Functional genetic variant in the Kozak sequence of WW domain-containing oxidoreductase (WWOX) gene is associated with oral cancer risk |
| [27339895](https://pubmed.ncbi.nlm.nih.gov/27339895/) | 2016 | ✅ | primary | catalogued only | Role of WW Domain-containing Oxidoreductase WWOX in Driving T Cell Acute Lymphoblastic Leukemia Maturation |
| [27190995](https://pubmed.ncbi.nlm.nih.gov/27190995/) | 2016 | ✅ | primary | catalogued only | WWOX CNV-67048 Functions as a Risk Factor for Epithelial Ovarian Cancer in Chinese Women by Negatively Interacting with Oral Contraceptive Use |
| [26929649](https://pubmed.ncbi.nlm.nih.gov/26929649/) | 2016 | ✅ | primary | catalogued only | Association of polymorphisms in WWOX gene with risk and outcome of osteosarcoma in a sample of the young Chinese population |
| [26910372](https://pubmed.ncbi.nlm.nih.gov/26910372/) | 2016 | ✅ | primary | catalogued only | Genetic association study identifies a functional CNV in the WWOX gene contributes to the risk of intracranial aneurysms |
| [26902998](https://pubmed.ncbi.nlm.nih.gov/26902998/) | 2016 | ✅ | primary | catalogued only | The role of WWOX polymorphisms on COPD susceptibility and pulmonary function traits in Chinese: a case-control study and family-based analysis |
| [26355344](https://pubmed.ncbi.nlm.nih.gov/26355344/) | 2015 | ✅ | primary | catalogued only | A cascade of protein aggregation bombards mitochondria for neurodegeneration and apoptosis under WWOX deficiency |
| [26302329](https://pubmed.ncbi.nlm.nih.gov/26302329/) | 2015 | ✅ | primary | catalogued only | Tumor Suppressor WWOX Contributes to the Elimination of Tumorigenic Cells in Drosophila melanogaster |
| [26120275](https://pubmed.ncbi.nlm.nih.gov/26120275/) | 2015 | ✅ | primary | catalogued only | Expression of WW domain-containing oxidoreductase WWOX in pterygium |
| [26041563](https://pubmed.ncbi.nlm.nih.gov/26041563/) | 2015 | ✅ | primary | catalogued only | HGF and TGFβ1 differently influenced Wwox regulatory function on Twist program for mesenchymal-epithelial transition in bone metastatic versus parental breast carcinoma cells |
| [25891642](https://pubmed.ncbi.nlm.nih.gov/25891642/) | 2015 | ✅ | primary | catalogued only | Effect of the WWOX gene on the regulation of the cell cycle and apoptosis in human ovarian cancer stem cells |
| [25789010](https://pubmed.ncbi.nlm.nih.gov/25789010/) | 2015 | ✅ | primary | catalogued only | Ectopic expression of the WWOX gene suppresses stemness of human ovarian cancer stem cells |
| [25710931](https://pubmed.ncbi.nlm.nih.gov/25710931/) | 2015 | ✅ | review | catalogued only | Versatile communication strategies among tandem WW domain repeats |
| [25708809](https://pubmed.ncbi.nlm.nih.gov/25708809/) | 2015 | ✅ | primary | catalogued only | MicroRNA-153 promotes Wnt/β-catenin activation in hepatocellular carcinoma through suppression of WWOX |
| [25703206](https://pubmed.ncbi.nlm.nih.gov/25703206/) | 2015 | ✅ | primary | catalogued only | Allostery mediates ligand binding to WWOX tumor suppressor via a conformational switch |
| [25662954](https://pubmed.ncbi.nlm.nih.gov/25662954/) | 2015 | ✅ | review | catalogued only | Structural insights into the functional versatility of WW domain-containing oxidoreductase tumor suppressor |
| [25649963](https://pubmed.ncbi.nlm.nih.gov/25649963/) | 2015 | ✅ | primary | catalogued only | Loss of wwox expression in zebrafish embryos causes edema and alters Ca(2+) dynamics |
| [25627656](https://pubmed.ncbi.nlm.nih.gov/25627656/) | 2015 | ✅ | review | catalogued only | Tyrosine phosphorylation of WW proteins |
| [25612104](https://pubmed.ncbi.nlm.nih.gov/25612104/) | 2015 | ✅ | primary | catalogued only | Epigenetic and genetic alterations affect the WWOX gene in head and neck squamous cell carcinoma |
| [25491415](https://pubmed.ncbi.nlm.nih.gov/25491415/) | 2015 | ✅ | review | catalogued only | The tumor suppressor WW domain-containing oxidoreductase modulates cell metabolism |
| [25488911](https://pubmed.ncbi.nlm.nih.gov/25488911/) | 2015 | ✅ | review | catalogued only | Strategies of oncogenic microbes to deal with WW domain-containing oxidoreductase |
| [25537520](https://pubmed.ncbi.nlm.nih.gov/25537520/) | 2014 | ✅ | review | catalogued only | WW domain-containing oxidoreductase in neuronal injury and neurological diseases |
| [25295115](https://pubmed.ncbi.nlm.nih.gov/25295115/) | 2014 | ✅ | primary | catalogued only | Alternating expression levels of WWOX tumor suppressor and cancer-related genes in patients with bladder cancer |
| [25024751](https://pubmed.ncbi.nlm.nih.gov/25024751/) | 2014 | ✅ | primary | catalogued only | Impact of decitabine on immunohistochemistry expression of the putative tumor suppressor genes FHIT, WWOX, FUS1 and PTEN in clinical tumor samples |
| [24938873](https://pubmed.ncbi.nlm.nih.gov/24938873/) | 2014 | ✅ | primary | catalogued only | Diverse effect of WWOX overexpression in HT29 and SW480 colon cancer cell lines |
| [24550385](https://pubmed.ncbi.nlm.nih.gov/24550385/) | 2014 | ✅ | primary | catalogued only | Characterizing WW domain interactions of tumor suppressor WWOX reveals its association with multiprotein networks |
| [24648952](https://pubmed.ncbi.nlm.nih.gov/24648952/) | 2013 | ✅ | primary | catalogued only | Methylation status of WWOX gene promoter CpG islands in epithelial ovarian cancer and its clinical significance |
| [24330824](https://pubmed.ncbi.nlm.nih.gov/24330824/) | 2013 | ✅ | primary | catalogued only | Correlation of WWOX, RUNX2 and VEGFA protein expression in human osteosarcoma |
| [24308844](https://pubmed.ncbi.nlm.nih.gov/24308844/) | 2013 | ✅ | primary | catalogued only | Molecular origin of the binding of WWOX tumor suppressor to ErbB4 receptor tyrosine kinase |
| [24137446](https://pubmed.ncbi.nlm.nih.gov/24137446/) | 2013 | ✅ | primary | catalogued only | Gene expression of WWOX, FHIT and p73 in acute lymphoblastic leukemia |
| [23459853](https://pubmed.ncbi.nlm.nih.gov/23459853/) | 2013 | ✅ | primary | catalogued only | Tumor Suppressor WWOX and p53 Alterations and Drug Resistance in Glioblastomas |
| [23370280](https://pubmed.ncbi.nlm.nih.gov/23370280/) | 2013 | ✅ | primary | catalogued only | Tumor suppressor WWOX binds to ΔNp63α and sensitizes cancer cells to chemotherapy |
| [23254685](https://pubmed.ncbi.nlm.nih.gov/23254685/) | 2013 | ✅ | primary | catalogued only | Conditional inactivation of the mouse Wwox tumor suppressor gene recapitulates the null phenotype |
| [22736928](https://pubmed.ncbi.nlm.nih.gov/22736928/) | 2012 | ✅ | primary | catalogued only | WWOX induces apoptosis and inhibits proliferation of human hepatoma cell line SMMC-7721 |
| [22634283](https://pubmed.ncbi.nlm.nih.gov/22634283/) | 2012 | ✅ | primary | catalogued only | Biophysical basis of the binding of WWOX tumor suppressor to WBP1 and WBP2 adaptors |
| [22479346](https://pubmed.ncbi.nlm.nih.gov/22479346/) | 2012 | ✅ | primary | catalogued only | Identification of IGF1, SLC4A4, WWOX, and SFMBT1 as hypertension susceptibility genes in Han Chinese with a genome-wide gene-based association study |
| [22071891](https://pubmed.ncbi.nlm.nih.gov/22071891/) | 2012 | ✅ | primary | catalogued only | A multi-exon deletion within WWOX is associated with a 46,XY disorder of sex development |
| [21731849](https://pubmed.ncbi.nlm.nih.gov/21731849/) | 2011 | ✅ | primary | catalogued only | Role of the WWOX tumor suppressor gene in bone homeostasis and the pathogenesis of osteosarcoma |
| [21685375](https://pubmed.ncbi.nlm.nih.gov/21685375/) | 2011 | ✅ | primary | catalogued only | Tumor suppressor genes FHIT and WWOX are deleted in primary effusion lymphoma (PEL) cell lines |
| [21115974](https://pubmed.ncbi.nlm.nih.gov/21115974/) | 2011 | ✅ | primary | catalogued only | The tumor suppressor gene WWOX links the canonical and noncanonical NF-κB pathways in HTLV-I Tax-mediated tumorigenesis |
| [21075834](https://pubmed.ncbi.nlm.nih.gov/21075834/) | 2011 | ✅ | primary | catalogued only | Drosophila orthologue of WWOX, the chromosomal fragile site FRA16D tumour suppressor gene, functions in aerobic metabolism and regulates reactive oxygen species |
| [20535528](https://pubmed.ncbi.nlm.nih.gov/20535528/) | 2011 | ✅ | primary | catalogued only | Molecular analysis of WWOX expression correlation with proliferation and apoptosis in glioblastoma multiforme |
| [20401669](https://pubmed.ncbi.nlm.nih.gov/20401669/) | 2011 | ✅ | primary | catalogued only | The prognostic significance of WWOX expression in patients with breast cancer and its association with the basal-like phenotype |
| [22615609](https://pubmed.ncbi.nlm.nih.gov/22615609/) | 2010 | ✅ | primary | catalogued only | Primary WWOX phosphorylation and JNK activation during etoposide induces cytotoxicity in HEK293 cells |
| [20942981](https://pubmed.ncbi.nlm.nih.gov/20942981/) | 2010 | ✅ | primary | catalogued only | WWOX gene is associated with HDL cholesterol and triglyceride levels |
| [20530675](https://pubmed.ncbi.nlm.nih.gov/20530675/) | 2010 | ✅ | primary | catalogued only | Frequent attenuation of the WWOX tumor suppressor in osteosarcoma is associated with increased tumorigenicity and aberrant RUNX2 expression |
| [19936220](https://pubmed.ncbi.nlm.nih.gov/19936220/) | 2009 | ✅ | primary | catalogued only | Generation and characterization of mice carrying a conditional allele of the Wwox tumor suppressor gene |
| [19484134](https://pubmed.ncbi.nlm.nih.gov/19484134/) | 2009 | ✅ | primary | catalogued only | Complement C1q activates tumor suppressor WWOX to induce apoptosis in prostate cancer cells |
| [19366691](https://pubmed.ncbi.nlm.nih.gov/19366691/) | 2009 | ✅ | primary | catalogued only | Transforming growth factor beta1 signaling via interaction with cell surface Hyal-2 and recruitment of WWOX/WOX1 |
| [19352382](https://pubmed.ncbi.nlm.nih.gov/19352382/) | 2009 | ✅ | primary | catalogued only | Hypermethylation-mediated reduction of WWOX expression in intraductal papillary mucinous neoplasms of the pancreas |
| [19130459](https://pubmed.ncbi.nlm.nih.gov/19130459/) | 2009 | ✅ | primary | catalogued only | Fragile histidine triad protein, WW domain-containing oxidoreductase protein Wwox, and activator protein 2gamma expression levels correlate with basal phenotype in breast cancer |
| [18629536](https://pubmed.ncbi.nlm.nih.gov/18629536/) | 2009 | ✅ | primary | catalogued only | Loss of WWOX expression in human extrahepatic cholangiocarcinoma |
| [18620777](https://pubmed.ncbi.nlm.nih.gov/18620777/) | 2008 | ✅ | primary | catalogued only | The JNK inhibitor SP600129 enhances apoptosis of HCC cells induced by the tumor suppressor WWOX |
| [18487609](https://pubmed.ncbi.nlm.nih.gov/18487609/) | 2008 | ✅ | primary | catalogued only | The WWOX tumor suppressor is essential for postnatal survival and normal bone metabolism |
| [18061530](https://pubmed.ncbi.nlm.nih.gov/18061530/) | 2008 | ✅ | primary | catalogued only | Molecular alterations in the tumor suppressor gene WWOX in oral leukoplakias |
| [18047428](https://pubmed.ncbi.nlm.nih.gov/18047428/) | 2007 | ✅ | primary | catalogued only | Association between decreased WWOX protein expression and thyroid cancer development |
| [17575124](https://pubmed.ncbi.nlm.nih.gov/17575124/) | 2007 | ✅ | primary | catalogued only | Inactivation of the Wwox gene accelerates forestomach tumor progression in vivo |
| [16152610](https://pubmed.ncbi.nlm.nih.gov/16152610/) | 2006 | ✅ | primary | catalogued only | Characterization of the tumor suppressor gene WWOX in primary human oral squamous cell carcinomas |
| [16187332](https://pubmed.ncbi.nlm.nih.gov/16187332/) | 2005 | ✅ | primary | catalogued only | Expression of common chromosomal fragile site genes, WWOX/FRA16D and FHIT/FRA3B is downregulated by exposure to environmental carcinogens, UV, and BPDE but not by IR |
| [15870886](https://pubmed.ncbi.nlm.nih.gov/15870886/) | 2005 | ✅ | primary | catalogued only | WWOX mRNA expression profile in epithelial ovarian cancer supports the role of WWOX variant 1 as a tumour suppressor, although the role of variant 4 remains unclear |
| [15692750](https://pubmed.ncbi.nlm.nih.gov/15692750/) | 2005 | ✅ | primary | catalogued only | Frequent loss of WWOX expression in breast cancer: correlation with estrogen receptor status |
| [15266310](https://pubmed.ncbi.nlm.nih.gov/15266310/) | 2004 | ✅ | primary | catalogued only | Frequent downregulation and loss of WWOX gene expression in human hepatocellular carcinoma |
| [25678599](https://pubmed.ncbi.nlm.nih.gov/25678599/) | 2015 | — | primary | catalogued only | The Tumor-Suppressor WWOX and HDAC3 Inhibit the Transcriptional Activity of the β-Catenin Coactivator BCL9-2 in Breast Cancer Cells |
| [25502636](https://pubmed.ncbi.nlm.nih.gov/25502636/) | 2014 | — | primary | catalogued only | WWOX suppresses cell growth and induces cell apoptosis via inhibition of P38 nuclear translocation in cholangiocarcinoma |
| [24969559](https://pubmed.ncbi.nlm.nih.gov/24969559/) | 2014 | — | primary | catalogued only | SENP2 regulated the stability of β-catenin through WWOX in hepatocellular carcinoma cell |
| [24510053](https://pubmed.ncbi.nlm.nih.gov/24510053/) | 2014 | — | review | catalogued only | WW domain-containing oxidoreductase's role in myriad cancers: clinical significance and future implications |
| [23534718](https://pubmed.ncbi.nlm.nih.gov/23534718/) | 2013 | — | primary | catalogued only | Expression of fragile histidine triad (FHIT) and WW-domain oxidoreductase gene (WWOX) in nasopharyngeal carcinoma |
| [21892104](https://pubmed.ncbi.nlm.nih.gov/21892104/) | 2011 | — | primary | catalogued only | Functional and clinical characterization of the putative tumor suppressor WWOX in non-small cell lung cancer |
| [19500159](https://pubmed.ncbi.nlm.nih.gov/19500159/) | 2009 | — | primary | catalogued only | A spontaneous mutation of the Wwox gene and audiogenic seizures in rats with lethal dwarfism and epilepsy |
| [19188760](https://pubmed.ncbi.nlm.nih.gov/19188760/) | 2009 | — | primary | catalogued only | Association between CpG island methylation of the WWOX gene and its expression in breast cancers |
| [17609426](https://pubmed.ncbi.nlm.nih.gov/17609426/) | 2007 | — | primary | catalogued only | Gene mapping and expression analysis of 16q loss of heterozygosity identifies WWOX and CYLD as being important in determining clinical outcome in multiple myeloma |
| [15798093](https://pubmed.ncbi.nlm.nih.gov/15798093/) | 2005 | — | primary | catalogued only | Components of DNA damage checkpoint pathway regulate UV exposure-dependent alterations of gene expression of FHIT and WWOX at chromosome fragile sites |
| [15073846](https://pubmed.ncbi.nlm.nih.gov/15073846/) | 2004 | — | primary | catalogued only | The fragile genes FHIT and WWOX are inactivated coordinately in invasive breast carcinoma |
| [41677633](https://pubmed.ncbi.nlm.nih.gov/41677633/) | 2026 | ✅ | primary | screened | WWOX Induction Promotes Bcl-XL and Mcl-1 Degradation Through a Lysosomal Pathway upon Stress Responses |
| [41254692](https://pubmed.ncbi.nlm.nih.gov/41254692/) | 2025 | ✅ | primary | screened | Integrative multi-omics and Mendelian randomization identify WWOX and THBS2 as potential therapeutic targets in mature T/NK-cell lymphoma |
| [41228229](https://pubmed.ncbi.nlm.nih.gov/41228229/) | 2025 | ✅ | review | screened | The Role of WWOX in Cancer Progression: Mechanisms and Therapeutic Potential |
| [41090157](https://pubmed.ncbi.nlm.nih.gov/41090157/) | 2025 | ✅ | primary | screened | B-cell-specific Wwox deletion promotes plasmablastic tumor development and proinflammatory signatures in myeloma model |
| [40327201](https://pubmed.ncbi.nlm.nih.gov/40327201/) | 2025 | ✅ | review | screened | Twenty-five years of WWOX insight in cancer: a treasure trove of knowledge |
| [39868255](https://pubmed.ncbi.nlm.nih.gov/39868255/) | 2025 | ✅ | preprint | screened | Partial Wwox Loss of Function Increases Severity of Murine Sepsis and Neuroinflammation |
| [39500530](https://pubmed.ncbi.nlm.nih.gov/39500530/) | 2024 | ✅ | primary | screened | WWOX tuning of oleic acid signaling orchestrates immunosuppressive macrophage polarization and sensitizes hepatocellular carcinoma to immunotherapy |
| [39473747](https://pubmed.ncbi.nlm.nih.gov/39473747/) | 2024 | ✅ | primary | screened | Loss of WWOX contributes to cisplatin resistance in triple-negative breast cancer cells by modulating miR-182 and miR-214 |
| [39416860](https://pubmed.ncbi.nlm.nih.gov/39416860/) | 2024 | ✅ | primary | screened | WWOX-related epileptic encephalopathy caused by a novel mutation in the WWOX gene: a case report |
| [38563965](https://pubmed.ncbi.nlm.nih.gov/38563965/) | 2024 | ✅ | primary | screened | Endothelial knockdown of the tumor suppressor, WWOX, increases inflammation in ventilator-induced lung injury |
| [38542478](https://pubmed.ncbi.nlm.nih.gov/38542478/) | 2024 | ✅ | review | screened | Zfra Overrides WWOX in Suppressing the Progression of Neurodegeneration |
| [38499540](https://pubmed.ncbi.nlm.nih.gov/38499540/) | 2024 | ✅ | primary | screened | Unveiling the relationship between WWOX and BRCA1 in mammary tumorigenicity and in DNA repair pathway selection |
| [38182577](https://pubmed.ncbi.nlm.nih.gov/38182577/) | 2024 | ✅ | primary | screened | WWOX promotes osteosarcoma development via upregulation of Myc |
| [38203337](https://pubmed.ncbi.nlm.nih.gov/38203337/) | 2023 | ✅ | primary | screened | Mechanistic Investigation of WWOX Function in NF-kB-Induced Skin Inflammation in Psoriasis |
| [37974179](https://pubmed.ncbi.nlm.nih.gov/37974179/) | 2023 | ✅ | primary | screened | Identification of compound heterozygous deletion of the WWOX gene in WOREE syndrome |
| [37897534](https://pubmed.ncbi.nlm.nih.gov/37897534/) | 2023 | ✅ | primary | screened | Loss of fragile WWOX gene leads to senescence escape and genome instability |
| [37519886](https://pubmed.ncbi.nlm.nih.gov/37519886/) | 2023 | ✅ | primary | screened | LINC01137/miR-186-5p/WWOX: a novel axis identified from WWOX-related RNA interactome in bladder cancer |
| [37324196](https://pubmed.ncbi.nlm.nih.gov/37324196/) | 2023 | ✅ | primary | screened | WWOX Polymorphisms as Predictors of the Biochemical Recurrence of Localized Prostate Cancer after Radical Prostatectomy |
| [37248434](https://pubmed.ncbi.nlm.nih.gov/37248434/) | 2023 | ✅ | primary | screened | WWOX binds MERIT40 and modulates its function in homologous recombination, implications in breast cancer |
| [36979157](https://pubmed.ncbi.nlm.nih.gov/36979157/) | 2023 | ✅ | primary | screened | Antineoplastic Nature of WWOX in Glioblastoma Is Mainly a Consequence of Reduced Cell Viability and Invasion |
| [36828035](https://pubmed.ncbi.nlm.nih.gov/36828035/) | 2023 | ✅ | primary | screened | WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice phenocopying human SCAR12 |
| [36572673](https://pubmed.ncbi.nlm.nih.gov/36572673/) | 2022 | ✅ | primary | screened | Loss of tumor suppressor WWOX accelerates pancreatic cancer development through promotion of TGFβ/BMP2 signaling |
| [36530994](https://pubmed.ncbi.nlm.nih.gov/36530994/) | 2022 | ✅ | primary | screened | WWOX-rs13338697 genotype predicts therapeutic efficacy of ADI-PEG 20 for patients with advanced hepatocellular carcinoma |
| [36364214](https://pubmed.ncbi.nlm.nih.gov/36364214/) | 2022 | ✅ | primary | screened | WWOX Modulates ROS-Dependent Senescence in Bladder Cancer |
| [35984507](https://pubmed.ncbi.nlm.nih.gov/35984507/) | 2022 | ✅ | primary | screened | WWOX inhibition by Zfra1-31 restores mitochondrial homeostasis and viability of neuronal cells exposed to high glucose |
| [35883580](https://pubmed.ncbi.nlm.nih.gov/35883580/) | 2022 | ✅ | review | screened | WWOX Controls Cell Survival, Immune Response and Disease Progression by pY33 to pS14 Transition to Alternate Signaling Partners |
| [35712340](https://pubmed.ncbi.nlm.nih.gov/35712340/) | 2022 | ✅ | primary | screened | Novel Mutation With Literature Review WW Domain-Containing Oxidoreductase (WWOX) Gene |
| [35563688](https://pubmed.ncbi.nlm.nih.gov/35563688/) | 2022 | ✅ | primary | screened | Determination of WWOX Function in Modulating Cellular Pathways Activated by AP-2α and AP-2γ Transcription Factors in Bladder Cancer |
| [35559044](https://pubmed.ncbi.nlm.nih.gov/35559044/) | 2022 | ✅ | primary | screened | EHBP1, TUBB, and WWOX SNPs, Gene-Gene and Gene-Environment Interactions on Coronary Artery Disease and Ischemic Stroke |
| [35409089](https://pubmed.ncbi.nlm.nih.gov/35409089/) | 2022 | ✅ | primary | screened | Wwox Binding to the Murine Brca1-BRCT Domain Regulates Timing of Brip1 and CtIP Phospho-Protein Interactions with This Domain at DNA Double-Strand Breaks, and Repair Pathway Choice |
| [35290621](https://pubmed.ncbi.nlm.nih.gov/35290621/) | 2022 | ✅ | primary | screened | TGFα-EGFR pathway in breast carcinogenesis, association with WWOX expression and estrogen activation |
| [35107375](https://pubmed.ncbi.nlm.nih.gov/35107375/) | 2022 | ✅ | primary | screened | WWOX-Mediated Degradation of AMOTp130 Negatively Affects Egress of Filovirus VP40 Virus-Like Particles |
| [34852950](https://pubmed.ncbi.nlm.nih.gov/34852950/) | 2022 | ✅ | primary | screened | Association between WWOX/MAF variants and dementia-related neuropathologic endophenotypes |
| [34831305](https://pubmed.ncbi.nlm.nih.gov/34831305/) | 2021 | ✅ | review | screened | WWOX-Related Neurodevelopmental Disorders: Models and Future Perspectives |
| [34359949](https://pubmed.ncbi.nlm.nih.gov/34359949/) | 2021 | ✅ | review | screened | WWOX and Its Binding Proteins in Neurodegeneration |
| [34210081](https://pubmed.ncbi.nlm.nih.gov/34210081/) | 2021 | ✅ | review | screened | Molecular Biology of the WWOX Gene That Spans Chromosomal Fragile Site FRA16D |
| [34204827](https://pubmed.ncbi.nlm.nih.gov/34204827/) | 2021 | ✅ | primary | screened | WWOX Loses the Ability to Regulate Oncogenic AP-2γ and Synergizes with Tumor Suppressor AP-2α in High-Grade Bladder Cancer |
| [34140629](https://pubmed.ncbi.nlm.nih.gov/34140629/) | 2021 | ✅ | primary | screened | Normal cells repel WWOX-negative or -dysfunctional cancer cells via WWOX cell surface epitope 286-299 |
| [33946771](https://pubmed.ncbi.nlm.nih.gov/33946771/) | 2021 | ✅ | review | screened | Molecular Functions of WWOX Potentially Involved in Cancer Development |
| [33718178](https://pubmed.ncbi.nlm.nih.gov/33718178/) | 2021 | ✅ | primary | screened | Fragile Gene WWOX Guides TFAP2A/TFAP2C-Dependent Actions Against Tumor Progression in Grade II Bladder Cancer |
| [33612478](https://pubmed.ncbi.nlm.nih.gov/33612478/) | 2021 | ✅ | primary | screened | Associations between TUBB-WWOX SNPs, their haplotypes, gene-gene, and gene-environment interactions and dyslipidemia |
| [33565365](https://pubmed.ncbi.nlm.nih.gov/33565365/) | 2021 | ✅ | primary | screened | Cellular Expression and Subcellular Localization of Wwox Protein During Testicular Development and Spermatogenesis in Rats |
| [33105088](https://pubmed.ncbi.nlm.nih.gov/33105088/) | 2021 | ✅ | primary | screened | Loss of Endothelial WWOX: A Risk Factor for ARDS in Smokers? |
| [33688485](https://pubmed.ncbi.nlm.nih.gov/33688485/) | 2020 | ✅ | primary | screened | Downregulated Expression of WWOX in Cervical Carcinoma: A Case-Control Study |
| [33255508](https://pubmed.ncbi.nlm.nih.gov/33255508/) | 2020 | ✅ | review | screened | WWOX Loss of Function in Neurodevelopmental and Neurodegenerative Disorders |
| [33195192](https://pubmed.ncbi.nlm.nih.gov/33195192/) | 2020 | ✅ | primary | screened | Wwox Deficiency Causes Downregulation of Prosurvival ERK Signaling and Abnormal Homeostatic Responses in Mouse Skin |
| [33129329](https://pubmed.ncbi.nlm.nih.gov/33129329/) | 2020 | ✅ | primary | screened | Characterization of WWOX expression and function in canine mast cell tumors and malignant mast cell lines |
| [32931356](https://pubmed.ncbi.nlm.nih.gov/32931356/) | 2020 | ✅ | primary | screened | LncRNA WWOX-AS1 sponges miR-20b-5p in hepatocellular carcinoma and represses its progression by upregulating WWOX |
| [32389029](https://pubmed.ncbi.nlm.nih.gov/32389029/) | 2020 | ✅ | review | screened | The WWOX gene in brain development and pathology |
| [32368285](https://pubmed.ncbi.nlm.nih.gov/32368285/) | 2020 | ✅ | primary | screened | Silencing of Wwox Increases Nuclear Import of Dvl proteins in Head and Neck Cancer |
| [32300104](https://pubmed.ncbi.nlm.nih.gov/32300104/) | 2020 | ✅ | primary | screened | Pleiotropic tumor suppressor functions of WWOX antagonize metastasis |
| [31752354](https://pubmed.ncbi.nlm.nih.gov/31752354/) | 2019 | ✅ | primary | screened | WWOX Possesses N-Terminal Cell Surface-Exposed Epitopes WWOX7-21 and WWOX7-11 for Signaling Cancer Growth Suppression and Prevention In Vivo |
| [31275852](https://pubmed.ncbi.nlm.nih.gov/31275852/) | 2019 | ✅ | primary | screened | Wwox Deletion in Mouse B Cells Leads to Genomic Instability, Neoplastic Transformation, and Monoclonal Gammopathies |
| [31075076](https://pubmed.ncbi.nlm.nih.gov/31075076/) | 2019 | ✅ | review | screened | Decoding the link between WWOX and p53 in aggressive breast cancer |
| [30755385](https://pubmed.ncbi.nlm.nih.gov/30755385/) | 2019 | ✅ | primary | screened | WWOX somatic ablation in skeletal muscles alters glucose metabolism |
| [30356099](https://pubmed.ncbi.nlm.nih.gov/30356099/) | 2019 | ✅ | review | screened | The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature |
| [30290271](https://pubmed.ncbi.nlm.nih.gov/30290271/) | 2019 | ✅ | primary | screened | Wwox deletion leads to reduced GABA-ergic inhibitory interneuron numbers and activation of microglia and astrocytes in mouse hippocampus |
| [30370248](https://pubmed.ncbi.nlm.nih.gov/30370248/) | 2018 | ✅ | review | screened | Modeling WWOX Loss of Function in vivo: What Have We Learned? |
| [30285739](https://pubmed.ncbi.nlm.nih.gov/30285739/) | 2018 | ✅ | primary | screened | VOPP1 promotes breast tumorigenesis by interacting with the tumor suppressor WWOX |
| [30214895](https://pubmed.ncbi.nlm.nih.gov/30214895/) | 2018 | ✅ | review | screened | Cancerous Protein Network That Inhibits the Tumor Suppressor Function of WW Domain-Containing Oxidoreductase (WWOX) by Aberrantly Expressed Molecules |
| [30211123](https://pubmed.ncbi.nlm.nih.gov/30211123/) | 2018 | ✅ | review | screened | WWOX Tumor Suppressor Gene in Breast Cancer, a Historical Perspective and Future Directions |
| [30158849](https://pubmed.ncbi.nlm.nih.gov/30158849/) | 2018 | ✅ | review | screened | WWOX Phosphorylation, Signaling, and Role in Neurodegeneration |
| [30154439](https://pubmed.ncbi.nlm.nih.gov/30154439/) | 2018 | ✅ | primary | screened | Loss of Wwox drives metastasis in triple-negative breast cancer by JAK2/STAT3 axis |
| [30082886](https://pubmed.ncbi.nlm.nih.gov/30082886/) | 2018 | ✅ | primary | screened | Somatic loss of WWOX is associated with TP53 perturbation in basal-like breast cancer |
| [29845204](https://pubmed.ncbi.nlm.nih.gov/29845204/) | 2018 | ✅ | primary | screened | LncRNA WWOX‑AS1 inhibits the proliferation, migration and invasion of osteosarcoma cells |
| [29724996](https://pubmed.ncbi.nlm.nih.gov/29724996/) | 2018 | ✅ | primary | screened | WWOX controls hepatic HIF1α to suppress hepatocyte proliferation and neoplasia |
| [29310447](https://pubmed.ncbi.nlm.nih.gov/29310447/) | 2018 | ✅ | review | screened | Phosphorylation/de-phosphorylation in specific sites of tumor suppressor WWOX and control of distinct biological events |
| [31966718](https://pubmed.ncbi.nlm.nih.gov/31966718/) | 2017 | ✅ | primary | screened | EBV-LMP1 regulating AKT/mTOR signaling pathway and WWOX in nasopharyngeal carcinoma |
| [31966508](https://pubmed.ncbi.nlm.nih.gov/31966508/) | 2017 | ✅ | primary | screened | WWOX suppresses proliferation and induces apoptosis via G2 arrest and caspase 3 pathway in nasopharyngeal carcinoma cells |
| [29200707](https://pubmed.ncbi.nlm.nih.gov/29200707/) | 2017 | ✅ | primary | screened | WWOX rs11644322 Polymorphism, Gemcitabine, and Pancreatic Cancer |
| [29085479](https://pubmed.ncbi.nlm.nih.gov/29085479/) | 2017 | ✅ | primary | screened | Correlation between osteosarcoma and the expression of WWOX and p53 |
| [28977834](https://pubmed.ncbi.nlm.nih.gov/28977834/) | 2017 | ✅ | primary | screened | Decreased WWOX expression promotes angiogenesis in osteosarcoma |
| [28749468](https://pubmed.ncbi.nlm.nih.gov/28749468/) | 2017 | ✅ | primary | screened | WWOX sensitises ovarian cancer cells to paclitaxel via modulation of the ER stress response |
| [28283473](https://pubmed.ncbi.nlm.nih.gov/28283473/) | 2017 | ✅ | primary | screened | Loss of lung WWOX expression causes neutrophilic inflammation |
| [28151481](https://pubmed.ncbi.nlm.nih.gov/28151481/) | 2017 | ✅ | primary | screened | Epigenetic regulation of HGF/Met receptor axis is critical for the outgrowth of bone metastasis from breast carcinoma |
| [28045433](https://pubmed.ncbi.nlm.nih.gov/28045433/) | 2017 | ✅ | review | screened | Functions and Epigenetic Regulation of Wwox in Bone Metastasis from Breast Carcinoma: Comparison with Primary Tumors |
| [27869163](https://pubmed.ncbi.nlm.nih.gov/27869163/) | 2017 | ✅ | primary | screened | Wwox-Brca1 interaction: role in DNA repair pathway choice |
| [27773744](https://pubmed.ncbi.nlm.nih.gov/27773744/) | 2017 | ✅ | primary | screened | Fhit and Wwox loss-associated genome instability: A genome caretaker one-two punch |
| [27999774](https://pubmed.ncbi.nlm.nih.gov/27999774/) | 2016 | ✅ | review | screened | HYAL-2-WWOX-SMAD4 Signaling in Cell Death and Anticancer Response |
| [27550453](https://pubmed.ncbi.nlm.nih.gov/27550453/) | 2016 | ✅ | primary | screened | WWOX and p53 Dysregulation Synergize to Drive the Development of Osteosarcoma |
| [26675548](https://pubmed.ncbi.nlm.nih.gov/26675548/) | 2016 | ✅ | primary | screened | WWOX modulates the ATR-mediated DNA damage checkpoint response |
| [27551439](https://pubmed.ncbi.nlm.nih.gov/27551439/) | 2015 | ✅ | primary | screened | WWOX dysfunction induces sequential aggregation of TRAPPC6AΔ, TIAF1, tau and amyloid β, and causes apoptosis |
| [27308504](https://pubmed.ncbi.nlm.nih.gov/27308504/) | 2015 | ✅ | primary | screened | WWOX guards genome stability by activating ATM |
| [26499798](https://pubmed.ncbi.nlm.nih.gov/26499798/) | 2015 | ✅ | review | screened | Pleiotropic Functions of Tumor Suppressor WWOX in Normal and Cancer Cells |
| [26256646](https://pubmed.ncbi.nlm.nih.gov/26256646/) | 2015 | ✅ | primary | screened | Tumor Suppressor WWOX inhibits osteosarcoma metastasis by modulating RUNX2 function |
| [25802472](https://pubmed.ncbi.nlm.nih.gov/25802472/) | 2015 | ✅ | primary | screened | Introduction to a thematic issue for WWOX |
| [25681467](https://pubmed.ncbi.nlm.nih.gov/25681467/) | 2015 | ✅ | review | screened | Alteration of WWOX in human cancer: a clinical view |
| [25595191](https://pubmed.ncbi.nlm.nih.gov/25595191/) | 2015 | ✅ | review | screened | Regulation of cell signaling and apoptosis by tumor suppressor WWOX |
| [25595186](https://pubmed.ncbi.nlm.nih.gov/25595186/) | 2015 | ✅ | review | screened | WWOX, the chromosomal fragile site FRA16D spanning gene: its role in metabolism and contribution to cancer |
| [25595185](https://pubmed.ncbi.nlm.nih.gov/25595185/) | 2015 | ✅ | review | screened | WWOX, large common fragile site genes, and cancer |
| [25538133](https://pubmed.ncbi.nlm.nih.gov/25538133/) | 2015 | ✅ | review | screened | WWOX: a fragile tumor suppressor |
| [25476151](https://pubmed.ncbi.nlm.nih.gov/25476151/) | 2015 | ✅ | review | screened | Roles of the WWOX in pathogenesis and endocrine therapy of breast cancer |
| [25432984](https://pubmed.ncbi.nlm.nih.gov/25432984/) | 2015 | ✅ | review | screened | Role of WW domain proteins WWOX in development, prognosis, and treatment response of glioma |
| [25416187](https://pubmed.ncbi.nlm.nih.gov/25416187/) | 2015 | ✅ | review | screened | The fragile site WWOX gene and the developing brain |
| [27308416](https://pubmed.ncbi.nlm.nih.gov/27308416/) | 2014 | ✅ | primary | screened | WWOX loss activates aerobic glycolysis |
| [25400415](https://pubmed.ncbi.nlm.nih.gov/25400415/) | 2014 | ✅ | primary | screened | WWOX suppresses KLF5 expression and breast cancer cell growth |
| [25245215](https://pubmed.ncbi.nlm.nih.gov/25245215/) | 2014 | ✅ | review | screened | The common fragile site FRA16D gene product WWOX: roles in tumor suppression and genomic stability |
| [25051421](https://pubmed.ncbi.nlm.nih.gov/25051421/) | 2014 | ✅ | primary | screened | WWOX modulates the gene expression profile in the T98G glioblastoma cell line rendering its phenotype less malignant |
| [24871327](https://pubmed.ncbi.nlm.nih.gov/24871327/) | 2014 | ✅ | primary | screened | The WWOX gene modulates high-density lipoprotein and lipid metabolism |
| [24520212](https://pubmed.ncbi.nlm.nih.gov/24520212/) | 2014 | ✅ | review | screened | Common Chromosomal Fragile Site Gene WWOX in Metabolic Disorders and Tumors |
| [27234396](https://pubmed.ncbi.nlm.nih.gov/27234396/) | 2013 | ✅ | review | screened | Role of WWOX and NF-κB in lung cancer progression |
| [24330518](https://pubmed.ncbi.nlm.nih.gov/24330518/) | 2013 | ✅ | primary | screened | The cancer gene WWOX behaves as an inhibitor of SMAD3 transcriptional activity via direct binding |
| [24008736](https://pubmed.ncbi.nlm.nih.gov/24008736/) | 2013 | ✅ | primary | screened | WWOX suppresses autophagy for inducing apoptosis in methotrexate-treated human squamous cell carcinoma |
| [22574198](https://pubmed.ncbi.nlm.nih.gov/22574198/) | 2012 | ✅ | primary | screened | Conditional Wwox deletion in mouse mammary gland by means of two Cre recombinase approaches |
| [20146584](https://pubmed.ncbi.nlm.nih.gov/20146584/) | 2010 | ✅ | review | screened | WWOX gene and gene product: tumor suppression through specific protein interactions |
| [16941225](https://pubmed.ncbi.nlm.nih.gov/16941225/) | 2006 | ✅ | primary | screened | WWOX protein expression in normal human tissues |
| [16223882](https://pubmed.ncbi.nlm.nih.gov/16223882/) | 2005 | ✅ | primary | screened | WWOX gene restoration prevents lung cancer growth in vitro and in vivo |
| [15982416](https://pubmed.ncbi.nlm.nih.gov/15982416/) | 2005 | ✅ | primary | screened | WWOX protein expression varies among ovarian carcinoma histotypes and correlates with less favorable outcome |
| [15064722](https://pubmed.ncbi.nlm.nih.gov/15064722/) | 2004 | ✅ | primary | screened | WWOX binds the specific proline-rich ligand PPXY: identification of candidate interacting proteins |
| [14526170](https://pubmed.ncbi.nlm.nih.gov/14526170/) | 2003 | ✅ | primary | screened | WWOX, the common chromosomal fragile site, FRA16D, cancer gene |
| [11572989](https://pubmed.ncbi.nlm.nih.gov/11572989/) | 2001 | ✅ | primary | screened | WWOX: a candidate tumor suppressor gene involved in multiple tumor types |
| [40198927](https://pubmed.ncbi.nlm.nih.gov/40198927/) | 2025 | — | primary | screened | WWOX attenuates the progression of gallbladder cancer by suppressing cellular glycolysis through the modulation of the P73/HIF-1α signaling pathway |
| [40139278](https://pubmed.ncbi.nlm.nih.gov/40139278/) | 2025 | — | primary | screened | Influence of WWOX/MAF genes on cognitive performance in patients with Parkinson's disease |
| [33455117](https://pubmed.ncbi.nlm.nih.gov/33455117/) | 2020 | — | primary | screened | Methylation of WWOX gene promotes proliferation of osteosarcoma cells |
| [32096174](https://pubmed.ncbi.nlm.nih.gov/32096174/) | 2020 | — | primary | screened | WWOX regulates the Elf5/Snail1 pathway to affect epithelial-mesenchymal transition of ovarian carcinoma cells in vitro |
| [23849374](https://pubmed.ncbi.nlm.nih.gov/23849374/) | 2013 | — | primary | screened | WWOX expression in giant cell lesions of the jaws |
| [23277037](https://pubmed.ncbi.nlm.nih.gov/23277037/) | 2013 | — | review | screened | Role of WWOX/WOX1 in Alzheimer's disease pathology and in cell death signaling |
| [22202011](https://pubmed.ncbi.nlm.nih.gov/22202011/) | 2012 | — | review | screened | Role of WWOX/WOX1 in Alzheimer's disease pathology and in cell death signaling |
| [20480411](https://pubmed.ncbi.nlm.nih.gov/20480411/) | 2010 | — | primary | screened | WWOX gene may contribute to progression of non-small-cell lung cancer (NSCLC) |
| [17704139](https://pubmed.ncbi.nlm.nih.gov/17704139/) | 2007 | — | primary | screened | Wwox suppresses prostate cancer cell growth through modulation of ErbB2-mediated androgen receptor signaling |
| [16818616](https://pubmed.ncbi.nlm.nih.gov/16818616/) | 2006 | — | primary | screened | A role for the WWOX gene in prostate cancer |
| [38355659](https://pubmed.ncbi.nlm.nih.gov/38355659/) | 2024 | ✅ | primary | unmatched | Correction: WWOX promotes osteosarcoma development via upregulation of Myc |
| [34513711](https://pubmed.ncbi.nlm.nih.gov/34513711/) | 2021 | ✅ | primary | unmatched | Corrigendum: Fragile Gene WWOX Guides TFAP2A/TFAP2C-Dependent Actions Against Tumor Progression in Grade II Bladder Cancer |
| [30783266](https://pubmed.ncbi.nlm.nih.gov/30783266/) | 2019 | ✅ | primary | unmatched | Correction: The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature |
| [30470736](https://pubmed.ncbi.nlm.nih.gov/30470736/) | 2018 | ✅ | primary | unmatched | Author Correction: WWOX controls hepatic HIF1α to suppress hepatocyte proliferation and neoplasia |
| [28708106](https://pubmed.ncbi.nlm.nih.gov/28708106/) | 2017 | ✅ | primary | unmatched | Evodiamine Exerts an Anti-Hepatocellular Carcinoma Activity through a WWOX-Dependent Pathway |
| [24503545](https://pubmed.ncbi.nlm.nih.gov/24503545/) | 2013 | ✅ | primary | unmatched | Expression of WW domain-containing oxidoreductase WOX1 in human nervous system tumors |
| [42327583](https://pubmed.ncbi.nlm.nih.gov/42327583/) | 2026 | ✅ | primary | unmatched | GALNT14-rs9679162 Genotypes Predict Post-immunotherapy Side Effect and Survival in Patients with Hepatitis B Virus-related Hepatocellular Carcinoma |
| [42266427](https://pubmed.ncbi.nlm.nih.gov/42266427/) | 2026 | ✅ | primary | unmatched | Genetic analysis of limbic-predominant age-related TDP-43 encephalopathy neuropathologic change in a population-based cohort of the oldest old |
| [41963310](https://pubmed.ncbi.nlm.nih.gov/41963310/) | 2026 | ✅ | primary | unmatched | Berry-derived gold nanoparticles induce integrated ROS-mediated apoptosis, immune modulation, and transcriptomic remodeling in 4T1 triple-negative cancer cells |
| [41425714](https://pubmed.ncbi.nlm.nih.gov/41425714/) | 2025 | ✅ | primary | unmatched | ETS Family Transcription Factors in Gastric Cancer and the Role of ELF3 in the Core Metaplasia Transcription Factor Network |
| [41378749](https://pubmed.ncbi.nlm.nih.gov/41378749/) | 2025 | ✅ | primary | unmatched | Folate Interaction With Genetic Risk for Neural Tube Defects Among Infants in Bangladesh |
| [41154849](https://pubmed.ncbi.nlm.nih.gov/41154849/) | 2025 | ✅ | primary | unmatched | Genome-Wide Association Study Revealed Candidate Genes Associated with Litter Size, Weight, and Body Size Traits in Tianmu Polytocous Sheep (Ovis aries) |
| [40507943](https://pubmed.ncbi.nlm.nih.gov/40507943/) | 2025 | ✅ | review | unmatched | Hyaluronan: An Architect and Integrator for Cancer and Neural Diseases |
| [40006511](https://pubmed.ncbi.nlm.nih.gov/40006511/) | 2025 | ✅ | primary | unmatched | Novel Hydrogel-Mediated Lentiviral Gene Delivery via Intravesical Administration for Bladder Cancer Treatment |
| [39955305](https://pubmed.ncbi.nlm.nih.gov/39955305/) | 2025 | ✅ | primary | unmatched | Integrating bulk RNA-seq and scRNA-seq data to explore diverse cell death patterns and develop a programmed cell death-related relapse prediction model in pediatric B-ALL |
| [39796213](https://pubmed.ncbi.nlm.nih.gov/39796213/) | 2025 | ✅ | review | unmatched | Atypical B-Cell Acute Lymphoblastic Leukemia with iAMP21 in the Context of Constitutional Ring Chromosome 21: A Case Report and Review of the Genetic Insights |
| [39087877](https://pubmed.ncbi.nlm.nih.gov/39087877/) | 2025 | ✅ | primary | unmatched | Novel susceptibility genes and biomarkers for obstructive sleep apnea: insights from genetic and inflammatory proteins |
| [39223676](https://pubmed.ncbi.nlm.nih.gov/39223676/) | 2024 | ✅ | primary | unmatched | Whole-genome de novo sequencing reveals genomic variants associated with differences of sex development in SRY negative pigs |
| [38886371](https://pubmed.ncbi.nlm.nih.gov/38886371/) | 2024 | ✅ | primary | unmatched | In vitro evolution and whole genome analysis to study chemotherapy drug resistance in haploid human cells |
| [38384455](https://pubmed.ncbi.nlm.nih.gov/38384455/) | 2024 | ✅ | primary | unmatched | A genome-wide association study on hematopoietic stem cell transplantation reveals novel genomic loci associated with transplant outcomes |
| [37930698](https://pubmed.ncbi.nlm.nih.gov/37930698/) | 2023 | ✅ | primary | unmatched | Neighborhood Deprivation and DNA Methylation and Expression of Cancer Genes in Breast Tumors |
| [37686047](https://pubmed.ncbi.nlm.nih.gov/37686047/) | 2023 | ✅ | primary | unmatched | Multi-Omics Analysis of NCI-60 Cell Line Data Reveals Novel Metabolic Processes Linked with Resistance to Alkylating Anti-Cancer Agents |
| [37583270](https://pubmed.ncbi.nlm.nih.gov/37583270/) | 2023 | ✅ | primary | unmatched | Landscape of genetic infantile epileptic spasms syndrome-A multicenter cohort of 124 children from India |
| [37501399](https://pubmed.ncbi.nlm.nih.gov/37501399/) | 2023 | ✅ | primary | unmatched | Population genetics of marmosets in Asian primate research centers and loci associated with epileptic risk revealed by whole-genome sequencing |
| [37461096](https://pubmed.ncbi.nlm.nih.gov/37461096/) | 2023 | ✅ | primary | unmatched | Landscape of germline pathogenic variants in patients with dual primary breast and lung cancer |
| [37328865](https://pubmed.ncbi.nlm.nih.gov/37328865/) | 2023 | ✅ | primary | unmatched | Shared genetic risk loci between Alzheimer's disease and related dementias, Parkinson's disease, and amyotrophic lateral sclerosis |
| [36975604](https://pubmed.ncbi.nlm.nih.gov/36975604/) | 2023 | ✅ | primary | unmatched | Epigenome-Wide Changes in the Cell Layers of the Vein Wall When Exposing the Venous Endothelium to Oscillatory Shear Stress |
| [36874126](https://pubmed.ncbi.nlm.nih.gov/36874126/) | 2023 | ✅ | primary | unmatched | Editorial: The role of STAT3 signaling pathway in tumor progression |
| [35383826](https://pubmed.ncbi.nlm.nih.gov/35383826/) | 2023 | ✅ | primary | unmatched | Plasma biomarkers and genetics in the diagnosis and prediction of Alzheimer's disease |
| [36587184](https://pubmed.ncbi.nlm.nih.gov/36587184/) | 2022 | ✅ | primary | unmatched | Single-cell resolved ploidy and chromosomal aberrations in nonalcoholic steatohepatitis-(NASH) induced hepatocellular carcinoma and its precursor lesions |
| [36572560](https://pubmed.ncbi.nlm.nih.gov/36572560/) | 2022 | ✅ | primary | unmatched | Glycogen Synthase Kinase-3 Interaction Domain Enhances Phosphorylation of SARS-CoV-2 Nucleocapsid Protein |
| [36553611](https://pubmed.ncbi.nlm.nih.gov/36553611/) | 2022 | ✅ | primary | unmatched | Detection of Association Features Based on Gene Eigenvalues and MRI Imaging Using Genetic Weighted Random Forest |
| [36316632](https://pubmed.ncbi.nlm.nih.gov/36316632/) | 2022 | ✅ | primary | unmatched | Genome-wide detection of RNA editing events during the hair follicles cycle of Tianzhu white yak |
| [36291747](https://pubmed.ncbi.nlm.nih.gov/36291747/) | 2022 | ✅ | primary | unmatched | Heat Shock Protein Upregulation Supplemental to Complex mRNA Alterations in Autoimmune Glaucoma |
| [36071494](https://pubmed.ncbi.nlm.nih.gov/36071494/) | 2022 | ✅ | primary | unmatched | Identification of recurrent variants implicated in disease in bicuspid aortic valve patients through whole-exome sequencing |
| [35655316](https://pubmed.ncbi.nlm.nih.gov/35655316/) | 2022 | ✅ | primary | unmatched | Genome-wide linkage search for cancer susceptibility loci in a cohort of non BRCA1/2 families in Sri Lanka |
| [35627222](https://pubmed.ncbi.nlm.nih.gov/35627222/) | 2022 | ✅ | primary | unmatched | Feature Fusion and Detection in Alzheimer's Disease Using a Novel Genetic Multi-Kernel SVM Based on MRI Imaging and Gene Data |
| [35571988](https://pubmed.ncbi.nlm.nih.gov/35571988/) | 2022 | ✅ | primary | unmatched | Mitochondrial 1555 G>A variant as a potential risk factor for childhood glioblastoma |
| [35460704](https://pubmed.ncbi.nlm.nih.gov/35460704/) | 2022 | ✅ | primary | unmatched | Whole-exome sequencing reveals damaging gene variants associated with hypoalphalipoproteinemia |
| [35053314](https://pubmed.ncbi.nlm.nih.gov/35053314/) | 2022 | ✅ | primary | unmatched | Correcting Differential Gene Expression Analysis for Cyto-Architectural Alterations in Substantia Nigra of Parkinson's Disease Patients Reveals Known and Potential Novel Disease-Associated Genes and Pathways |
| [35047994](https://pubmed.ncbi.nlm.nih.gov/35047994/) | 2021 | ✅ | primary | unmatched | Combination of Clptm1L and TMEM207 Expression as a Robust Prognostic Marker in Oral Squamous Cell Carcinoma |
| [33958783](https://pubmed.ncbi.nlm.nih.gov/33958783/) | 2021 | ✅ | primary | unmatched | Genome-wide survival study identifies a novel synaptic locus and polygenic score for cognitive progression in Parkinson's disease |
| [33919646](https://pubmed.ncbi.nlm.nih.gov/33919646/) | 2021 | ✅ | review | unmatched | Genetic Neonatal-Onset Epilepsies and Developmental/Epileptic Encephalopathies with Movement Disorders: A Systematic Review |
| [33854788](https://pubmed.ncbi.nlm.nih.gov/33854788/) | 2021 | ✅ | primary | unmatched | Metabolome-Genome-Wide Association Study (mGWAS) Reveals Novel Metabolites Associated with Future Type 2 Diabetes Risk and Susceptibility Loci in a Case-Control Study in a Chinese Prospective Cohort |
| [33074286](https://pubmed.ncbi.nlm.nih.gov/33074286/) | 2021 | ✅ | primary | unmatched | Novel Alzheimer Disease Risk Loci and Pathways in African American Individuals Using the African Genome Resources Panel: A Meta-analysis |
| [32922661](https://pubmed.ncbi.nlm.nih.gov/32922661/) | 2020 | ✅ | primary | unmatched | The NKL-code for innate lymphoid cells reveals deregulated expression of NKL homeobox genes HHEX and HLX in anaplastic large cell lymphoma (ALCL) |
| [32617189](https://pubmed.ncbi.nlm.nih.gov/32617189/) | 2020 | ✅ | primary | unmatched | Whole genome sequencing analysis identifies recurrent structural alterations in esophageal squamous cell carcinoma |
| [32552875](https://pubmed.ncbi.nlm.nih.gov/32552875/) | 2020 | ✅ | primary | unmatched | Immune characterization of metastatic colorectal cancer patients post reovirus administration |
| [32290755](https://pubmed.ncbi.nlm.nih.gov/32290755/) | 2020 | ✅ | review | unmatched | Clinical epigenetics and multidrug-resistant bacterial infections: host remodelling in critical illness |
| [32214227](https://pubmed.ncbi.nlm.nih.gov/32214227/) | 2020 | ✅ | primary | unmatched | First-line exome sequencing in Palestinian and Israeli Arabs with neurological disorders is efficient and facilitates disease gene discovery |
| [32180796](https://pubmed.ncbi.nlm.nih.gov/32180796/) | 2020 | ✅ | primary | unmatched | Genetic Architecture of Carcass and Meat Quality Traits in Montana Tropical® Composite Beef Cattle |
| [32081867](https://pubmed.ncbi.nlm.nih.gov/32081867/) | 2020 | ✅ | primary | unmatched | An integrated analysis of rare CNV and exome variation in Autism Spectrum Disorder using the Infinium PsychArray |
| [31745703](https://pubmed.ncbi.nlm.nih.gov/31745703/) | 2020 | ✅ | primary | unmatched | Transcriptome analysis reveals overlap in fusion genes in a phase I clinical cohort of TNBC and HGSOC patients treated with buparlisib and olaparib |
| [30820047](https://pubmed.ncbi.nlm.nih.gov/30820047/) | 2019 | ✅ | primary | unmatched | Genetic meta-analysis of diagnosed Alzheimer's disease identifies new risk loci and implicates Aβ, tau, immunity and lipid processing |
| [30805310](https://pubmed.ncbi.nlm.nih.gov/30805310/) | 2019 | ✅ | review | unmatched | WW Domain-Containing Proteins YAP and TAZ in the Hippo Pathway as Key Regulators in Stemness Maintenance, Tissue Homeostasis, and Tumorigenesis |
| [30529582](https://pubmed.ncbi.nlm.nih.gov/30529582/) | 2019 | ✅ | primary | unmatched | Large-Scale Genome-Wide Association Study of East Asians Identifies Loci Associated With Risk for Colorectal Cancer |
| [30385613](https://pubmed.ncbi.nlm.nih.gov/30385613/) | 2019 | ✅ | primary | unmatched | Genetic Variants of VEGFA and FLT4 Are Determinants of Survival in Renal Cell Carcinoma Patients Treated with Sorafenib |
| [29764119](https://pubmed.ncbi.nlm.nih.gov/29764119/) | 2019 | ✅ | primary | unmatched | Founder Mutations for Early Onset Melanoma as Revealed by Whole Exome Sequencing Suggests That This is Not Associated with the Increasing Incidence of Melanoma in Poland |
| [30619734](https://pubmed.ncbi.nlm.nih.gov/30619734/) | 2018 | ✅ | review | unmatched | WW-Domain Containing Protein Roles in Breast Tumorigenesis |
| [29581896](https://pubmed.ncbi.nlm.nih.gov/29581896/) | 2018 | ✅ | primary | unmatched | Chasing the signaling run by tri-molecular time-lapse FRET microscopy |
| [29481666](https://pubmed.ncbi.nlm.nih.gov/29481666/) | 2018 | ✅ | primary | unmatched | Identification of seven novel loci associated with amino acid levels using single-variant and gene-based tests in 8545 Finnish men from the METSIM study |
| [29551923](https://pubmed.ncbi.nlm.nih.gov/29551923/) | 2017 | ✅ | primary | unmatched | Establishment of optimal regulatory network of colorectal cancer based on p42.3 protein |
| [29108237](https://pubmed.ncbi.nlm.nih.gov/29108237/) | 2017 | ✅ | primary | unmatched | The circRNA interactome-innovative hallmarks of the intra- and extracellular radiation response |
| [29100284](https://pubmed.ncbi.nlm.nih.gov/29100284/) | 2017 | ✅ | primary | unmatched | Exosomes containing differential expression of microRNA and mRNA in osteosarcoma that can predict response to chemotherapy |
| [29067327](https://pubmed.ncbi.nlm.nih.gov/29067327/) | 2017 | ✅ | primary | unmatched | Zfra restores memory deficits in Alzheimer's disease triple-transgenic mice by blocking aggregation of TRAPPC6AΔ, SH3GLB2, tau, and amyloid β, and inflammatory NF-κB activation |
| [28943951](https://pubmed.ncbi.nlm.nih.gov/28943951/) | 2017 | ✅ | primary | unmatched | Recurrent alterations of the WW domain containing oxidoreductase gene spanning the common fragile site FRA16D in multiple myeloma and monoclonal gammopathy of undetermined significance |
| [28787462](https://pubmed.ncbi.nlm.nih.gov/28787462/) | 2017 | ✅ | primary | unmatched | Novel near-diploid ovarian cancer cell line derived from a highly aneuploid metastatic ovarian tumor |
| [28763065](https://pubmed.ncbi.nlm.nih.gov/28763065/) | 2017 | ✅ | primary | unmatched | Genome-wide association analysis identifies common variants influencing infant brain volumes |
| [28742274](https://pubmed.ncbi.nlm.nih.gov/28742274/) | 2017 | ✅ | primary | unmatched | Whole exome sequencing identified genetic variations in Chinese hemangioblastoma patients |
| [28496150](https://pubmed.ncbi.nlm.nih.gov/28496150/) | 2017 | ✅ | primary | unmatched | Long non-coding RNA PARTICLE bridges histone and DNA methylation |
| [28386190](https://pubmed.ncbi.nlm.nih.gov/28386190/) | 2017 | ✅ | primary | unmatched | Establishment of apoptotic regulatory network for genetic markers of colorectal cancer and optimal selection of traditional Chinese medicine target |
| [28386169](https://pubmed.ncbi.nlm.nih.gov/28386169/) | 2017 | ✅ | primary | unmatched | Establishment of apoptotic regulatory network for genetic markers of colorectal cancer |
| [28280357](https://pubmed.ncbi.nlm.nih.gov/28280357/) | 2017 | ✅ | primary | unmatched | A new tumor suppressor lncRNA RP11-190D6.2 inhibits the proliferation, migration, and invasion of epithelial ovarian cancer cells |
| [27572307](https://pubmed.ncbi.nlm.nih.gov/27572307/) | 2016 | ✅ | primary | unmatched | Oncogenic roles of the SETDB2 histone methyltransferase in gastric cancer |
| [27569545](https://pubmed.ncbi.nlm.nih.gov/27569545/) | 2016 | ✅ | primary | unmatched | Rare Inherited and De Novo CNVs Reveal Complex Contributions to ASD Risk in Multiplex Families |
| [27501229](https://pubmed.ncbi.nlm.nih.gov/27501229/) | 2016 | ✅ | primary | unmatched | Genomic Alteration in Head and Neck Squamous Cell Carcinoma (HNSCC) Cell Lines Inferred from Karyotyping, Molecular Cytogenetics, and Array Comparative Genomic Hybridization |
| [27162544](https://pubmed.ncbi.nlm.nih.gov/27162544/) | 2016 | ✅ | primary | unmatched | Combining Telomerase Reverse Transcriptase Genetic Variant rs2736100 with Epidemiologic Factors in the Prediction of Lung Cancer Susceptibility |
| [27075929](https://pubmed.ncbi.nlm.nih.gov/27075929/) | 2016 | ✅ | review | unmatched | Bubbling cell death: A hot air balloon released from the nucleus in the cold |
| [26070663](https://pubmed.ncbi.nlm.nih.gov/26070663/) | 2015 | ✅ | primary | unmatched | Unbalanced translocations arise from diverse mutational mechanisms including chromothripsis |
| [26010871](https://pubmed.ncbi.nlm.nih.gov/26010871/) | 2015 | ✅ | primary | unmatched | Death Receptor-Induced Apoptosis Signalling Regulation by Ezrin Is Cell Type Dependent and Occurs in a DISC-Independent Manner in Colon Cancer Cells |
| [25934800](https://pubmed.ncbi.nlm.nih.gov/25934800/) | 2015 | ✅ | primary | unmatched | Signatures of accelerated somatic evolution in gene promoters in multiple cancer types |
| [25779665](https://pubmed.ncbi.nlm.nih.gov/25779665/) | 2015 | ✅ | primary | unmatched | UV irradiation/cold shock-mediated apoptosis is switched to bubbling cell death at low temperatures |
| [25650666](https://pubmed.ncbi.nlm.nih.gov/25650666/) | 2015 | ✅ | primary | unmatched | Trafficking protein particle complex 6A delta (TRAPPC6AΔ) is an extracellular plaque-forming protein in the brain |
| [25595187](https://pubmed.ncbi.nlm.nih.gov/25595187/) | 2015 | ✅ | primary | unmatched | Modulation of Sonic hedgehog signaling and WW domain containing oxidoreductase WOX1 expression enhances radiosensitivity of human glioblastoma cells |
| [25539992](https://pubmed.ncbi.nlm.nih.gov/25539992/) | 2015 | ✅ | primary | unmatched | Synergy of leptin/STAT3 with HER2 receptor induces tamoxifen resistance in breast cancer cells through regulation of apoptosis-related genes |
| [25401976](https://pubmed.ncbi.nlm.nih.gov/25401976/) | 2015 | ✅ | primary | unmatched | FHIT loss-induced DNA damage creates optimal APOBEC substrates: Insights into APOBEC-mediated mutagenesis |
| [25418192](https://pubmed.ncbi.nlm.nih.gov/25418192/) | 2014 | ✅ | primary | unmatched | Investigation of osteosarcoma genomics and its impact on targeted therapy: an international collaboration to conquer human osteosarcoma |
| [25300511](https://pubmed.ncbi.nlm.nih.gov/25300511/) | 2014 | ✅ | review | unmatched | Very large common fragile site genes and their potential role in cancer development |
| [25238781](https://pubmed.ncbi.nlm.nih.gov/25238781/) | 2014 | ✅ | review | unmatched | Role of common fragile sites and corresponding genes in cancer development |
| [25198128](https://pubmed.ncbi.nlm.nih.gov/25198128/) | 2014 | ✅ | primary | unmatched | Identification of genes related to beak deformity of chickens using digital gene expression profiling |
| [24955146](https://pubmed.ncbi.nlm.nih.gov/24955146/) | 2014 | ✅ | primary | unmatched | Expanding the genetic basis of copy number variation in familial breast cancer |
| [24929828](https://pubmed.ncbi.nlm.nih.gov/24929828/) | 2014 | ✅ | primary | unmatched | Genome-wide association analysis identifies six new loci associated with forced vital capacity |
| [24748104](https://pubmed.ncbi.nlm.nih.gov/24748104/) | 2014 | ✅ | primary | unmatched | Genome-wide analysis of loss of heterozygosity in breast infiltrating ductal carcinoma distant normal tissue highlights arm specific enrichment and expansion across tumor stages |
| [24454681](https://pubmed.ncbi.nlm.nih.gov/24454681/) | 2014 | ✅ | primary | unmatched | The degree of segmental aneuploidy measured by total copy number abnormalities predicts survival and recurrence in superficial gastroesophageal adenocarcinoma |
| [27234387](https://pubmed.ncbi.nlm.nih.gov/27234387/) | 2013 | ✅ | primary | unmatched | Self-aggregating TIAF1 in lung cancer progression |
| [24098343](https://pubmed.ncbi.nlm.nih.gov/24098343/) | 2013 | ✅ | primary | unmatched | Genome-wide association study of gene by smoking interactions in coronary artery calcification |
| [24086726](https://pubmed.ncbi.nlm.nih.gov/24086726/) | 2013 | ✅ | primary | unmatched | Replication study for the association of 9 East Asian GWAS-derived loci with susceptibility to type 2 diabetes in a Japanese population |
| [23028374](https://pubmed.ncbi.nlm.nih.gov/23028374/) | 2012 | ✅ | primary | unmatched | De novo CNV formation in mouse embryonic stem cells occurs in the absence of Xrcc4-dependent nonhomologous end joining |
| [22860045](https://pubmed.ncbi.nlm.nih.gov/22860045/) | 2012 | ✅ | primary | unmatched | A comprehensive characterization of genome-wide copy number aberrations in colorectal cancer reveals novel oncogenes and patterns of alterations |
| [22855598](https://pubmed.ncbi.nlm.nih.gov/22855598/) | 2012 | ✅ | primary | unmatched | Genome-wide analysis reveals recurrent structural abnormalities of TP63 and other p53-related genes in peripheral T-cell lymphomas |
| [22806168](https://pubmed.ncbi.nlm.nih.gov/22806168/) | 2012 | ✅ | primary | unmatched | A multistage genetic association study identifies breast cancer risk loci at 10q25 and 16q24 |
| [22545673](https://pubmed.ncbi.nlm.nih.gov/22545673/) | 2012 | ✅ | primary | unmatched | Testing an aflatoxin B1 gene signature in rat archival tissues |
| [22536204](https://pubmed.ncbi.nlm.nih.gov/22536204/) | 2012 | ✅ | primary | unmatched | The C1q family of proteins: insights into the emerging non-traditional functions |
| [22534828](https://pubmed.ncbi.nlm.nih.gov/22534828/) | 2012 | ✅ | primary | unmatched | TIAF1 self-aggregation in peritumor capsule formation, spontaneous activation of SMAD-responsive promoter in p53-deficient environment, and cell death |
| [21965145](https://pubmed.ncbi.nlm.nih.gov/21965145/) | 2012 | ✅ | primary | unmatched | Copy number alterations in prostate tumors and disease aggressiveness |
| [21901168](https://pubmed.ncbi.nlm.nih.gov/21901168/) | 2011 | ✅ | primary | unmatched | Identification of an In Vivo MEK/WOX1 Complex as a Master Switch for Apoptosis in T Cell Leukemia |
| [21743832](https://pubmed.ncbi.nlm.nih.gov/21743832/) | 2011 | ✅ | review | unmatched | Human T-cell lymphotropic virus: a model of NF-κB-associated tumorigenesis |
| [21318118](https://pubmed.ncbi.nlm.nih.gov/21318118/) | 2011 | ✅ | review | unmatched | Common fragile site tumor suppressor genes and corresponding mouse models of cancer |
| [21069451](https://pubmed.ncbi.nlm.nih.gov/21069451/) | 2011 | ✅ | primary | unmatched | Aberrant expression of DNA damage response proteins is associated with breast cancer subtype and clinical features |
| [21212468](https://pubmed.ncbi.nlm.nih.gov/21212468/) | 2010 | ✅ | primary | unmatched | Zfra is a small wizard in the mitochondrial apoptosis |
| [21072196](https://pubmed.ncbi.nlm.nih.gov/21072196/) | 2010 | ✅ | primary | unmatched | Profiling gene expression induced by protease-activated receptor 2 (PAR2) activation in human kidney cells |
| [20651033](https://pubmed.ncbi.nlm.nih.gov/20651033/) | 2010 | ✅ | primary | unmatched | Genome-wide catalogue of chromosomal aberrations in barrett's esophagus and esophageal adenocarcinoma: a high-density single nucleotide polymorphism array analysis |
| [20629094](https://pubmed.ncbi.nlm.nih.gov/20629094/) | 2010 | ✅ | primary | unmatched | Identification of primary gene targets of TFAP2C in hormone responsive breast carcinoma cells |
| [20432460](https://pubmed.ncbi.nlm.nih.gov/20432460/) | 2010 | ✅ | review | unmatched | Shepherding AKT and androgen receptor by Ack1 tyrosine kinase |
| [19832807](https://pubmed.ncbi.nlm.nih.gov/19832807/) | 2010 | ✅ | primary | unmatched | Genome wide DNA-profiling of HIV-related B-cell lymphomas |
| [19700237](https://pubmed.ncbi.nlm.nih.gov/19700237/) | 2010 | ✅ | primary | unmatched | Oncosuppressor proteins of fragile sites are reduced in cervical cancer |
| [19774227](https://pubmed.ncbi.nlm.nih.gov/19774227/) | 2009 | ✅ | primary | unmatched | Image-based assessment of growth and signaling changes in cancer cells mediated by direct cell-cell contact |
| [19434452](https://pubmed.ncbi.nlm.nih.gov/19434452/) | 2009 | ✅ | primary | unmatched | Coordinate loss of fragile gene expression in pancreatobiliary cancers: correlations among markers and clinical features |
| [19144635](https://pubmed.ncbi.nlm.nih.gov/19144635/) | 2009 | ✅ | primary | unmatched | Down-regulation of active ACK1 is mediated by association with the E3 ubiquitin ligase Nedd4-2 |
| [19035517](https://pubmed.ncbi.nlm.nih.gov/19035517/) | 2009 | ✅ | primary | unmatched | Genome-wide linkage scan for prostate cancer susceptibility from the University of Michigan Prostate Cancer Genetics Project: suggestive evidence for linkage at 16q23 |
| [19011694](https://pubmed.ncbi.nlm.nih.gov/19011694/) | 2008 | ✅ | primary | unmatched | Integrative microRNA and proteomic approaches identify novel osteoarthritis genes and their collaborative metabolic and inflammatory networks |
| [18674750](https://pubmed.ncbi.nlm.nih.gov/18674750/) | 2008 | ✅ | primary | unmatched | WW-domain-containing oxidoreductase is associated with low plasma HDL-C levels |
| [18485879](https://pubmed.ncbi.nlm.nih.gov/18485879/) | 2008 | ✅ | primary | unmatched | Large-scale mutagenesis in p19(ARF)- and p53-deficient mice identifies cancer genes and their collaborative networks |
| [17890317](https://pubmed.ncbi.nlm.nih.gov/17890317/) | 2007 | ✅ | primary | unmatched | MicroRNA-29 family reverts aberrant methylation in lung cancer by targeting DNA methyltransferases 3A and 3B |
| [17679088](https://pubmed.ncbi.nlm.nih.gov/17679088/) | 2007 | ✅ | primary | unmatched | An AT-rich sequence in human common fragile site FRA16D causes fork stalling and chromosome breakage in S. cerevisiae |
| [17567906](https://pubmed.ncbi.nlm.nih.gov/17567906/) | 2007 | ✅ | primary | unmatched | Zfra affects TNF-mediated cell death by interacting with death domain protein TRADD and negatively regulates the activation of NF-kappaB, JNK1, p53 and WOX1 during stress response |
| [17546048](https://pubmed.ncbi.nlm.nih.gov/17546048/) | 2007 | ✅ | primary | unmatched | Epigenetic identification of ADAMTS18 as a novel 16q23.1 tumor suppressor frequently silenced in esophageal, nasopharyngeal and multiple other carcinomas |
| [16895604](https://pubmed.ncbi.nlm.nih.gov/16895604/) | 2006 | ✅ | primary | unmatched | A novel approach to simultaneously scan genes at fragile sites |
| [16280054](https://pubmed.ncbi.nlm.nih.gov/16280054/) | 2005 | ✅ | primary | unmatched | Expression analysis of candidate breast tumour suppressor genes on chromosome 16q |
| [12719539](https://pubmed.ncbi.nlm.nih.gov/12719539/) | 2003 | ✅ | primary | unmatched | Parkin, a gene implicated in autosomal recessive juvenile parkinsonism, is a candidate tumor suppressor gene on chromosome 6q25-q27 |
| [11960552](https://pubmed.ncbi.nlm.nih.gov/11960552/) | 2002 | ✅ | primary | unmatched | Transforming growth factor-beta1 blocks the enhancement of tumor necrosis factor cytotoxicity by hyaluronidase Hyal-2 in L929 fibroblasts |
| [42275215](https://pubmed.ncbi.nlm.nih.gov/42275215/) | 2026 | — | primary | unmatched | RNF138 promotes cisplatin resistance and PD-L1-mediated immune evasion via JAK2/STAT3 activation in nasopharyngeal carcinoma |
| [42135313](https://pubmed.ncbi.nlm.nih.gov/42135313/) | 2026 | — | primary | unmatched | Multi-locus genetic dosage shapes cognitive disease progression in Parkinson's patients: 15-year meta-analysis of 24 cohorts |
| [41966396](https://pubmed.ncbi.nlm.nih.gov/41966396/) | 2026 | — | primary | unmatched | Comprehensive multi-omics analyses reveal small intestinal genetic mechanisms regulating milk protein traits in yak |
| [39332629](https://pubmed.ncbi.nlm.nih.gov/39332629/) | 2024 | — | primary | unmatched | High Prevalence of Chromosomal Rearrangements and LINE Retrotranspositions Detected in Formalin-Fixed, Paraffin-Embedded Colorectal Cancer Tissue |
| [38232788](https://pubmed.ncbi.nlm.nih.gov/38232788/) | 2024 | — | primary | unmatched | 14-Week exercise training modifies the DNA methylation levels at gene sites in non-Alzheimer's disease women aged 50 to 70 years |
| [38056170](https://pubmed.ncbi.nlm.nih.gov/38056170/) | 2024 | — | primary | unmatched | Genome-wide scans identify biological and metabolic pathways regulating carcass and meat quality traits in beef cattle |
| [32669614](https://pubmed.ncbi.nlm.nih.gov/32669614/) | 2020 | — | primary | unmatched | The HNRNPA2B1-MST1R-Akt axis contributes to epithelial-to-mesenchymal transition in head and neck cancer |
| [31145772](https://pubmed.ncbi.nlm.nih.gov/31145772/) | 2019 | — | primary | unmatched | East Asian Genome-wide association study derived loci in relation to type 2 diabetes in the Han Chinese population |
| [25417742](https://pubmed.ncbi.nlm.nih.gov/25417742/) | 2015 | — | primary | unmatched | The Evaluation of WBP2NL-Related Genes Expression in Breast Cancer |
| [24935583](https://pubmed.ncbi.nlm.nih.gov/24935583/) | 2014 | — | primary | unmatched | Association of the rs1042522 polymorphism with increased risk of prostate adenocarcinoma in the Pakistani population and its HuGE review |
| [24127039](https://pubmed.ncbi.nlm.nih.gov/24127039/) | 2014 | — | primary | unmatched | WW domain containing oxidoreductase induces apoptosis in gallbladder-derived malignant cell by upregulating expression of P73 and PUMA |
| [23464470](https://pubmed.ncbi.nlm.nih.gov/23464470/) | 2012 | — | primary | unmatched | Effects of sodium valproate on the growth of human ovarian cancer cell line HO8910 |
| [23317259](https://pubmed.ncbi.nlm.nih.gov/23317259/) | 2012 | — | primary | unmatched | Ectopic overexpression of COTE1 promotes cellular invasion of hepatocellular carcinoma |
| [20190683](https://pubmed.ncbi.nlm.nih.gov/20190683/) | 2010 | — | primary | unmatched | Breast cancer relapse prediction based on multi-gene RT-PCR algorithm |
| [16888633](https://pubmed.ncbi.nlm.nih.gov/16888633/) | 2006 | — | primary | unmatched | Expression profiling of UVB response in melanocytes identifies a set of p53-target genes |
| [16393779](https://pubmed.ncbi.nlm.nih.gov/16393779/) | 2005 | — | review | unmatched | WW or WoW: the WW domains in a union of bliss |
| [16219768](https://pubmed.ncbi.nlm.nih.gov/16219768/) | 2005 | — | primary | unmatched | WOX1 is essential for tumor necrosis factor-, UV light-, staurosporine-, and p53-mediated cell death, and its tyrosine 33-phosphorylated form binds and stabilizes serine 46-phosphorylated p53 |
| [42082822](https://pubmed.ncbi.nlm.nih.gov/42082822/) | 2026 | ✅ | primary | unmatched | The Role of WWOX Gene Variant in Hypospadias and 46,XY Disorders of Sexual Development |
| [41984841](https://pubmed.ncbi.nlm.nih.gov/41984841/) | 2026 | ✅ | primary | unmatched | WWOX maintains epidermal identity and suppresses EMT to prevent aggressive cutaneous squamous cell carcinoma |
| [39952983](https://pubmed.ncbi.nlm.nih.gov/39952983/) | 2025 | ✅ | primary | unmatched | Genome-wide identification and functional validation of the WW domain containing oxidoreductase gene associated with sleep duration |
| [37095367](https://pubmed.ncbi.nlm.nih.gov/37095367/) | 2023 | ✅ | primary | unmatched | Whole-Genome Sequencing Among Kazakhstani Children with Early-Onset Epilepsy Revealed New Gene Variants and Phenotypic Variability |
| [35573960](https://pubmed.ncbi.nlm.nih.gov/35573960/) | 2022 | ✅ | primary | unmatched | A Phenotypic-Driven Approach for the Diagnosis of WOREE Syndrome |
| [33058734](https://pubmed.ncbi.nlm.nih.gov/33058734/) | 2021 | ✅ | primary | unmatched | Cigarette Smoke and Nicotine-Containing Electronic-Cigarette Vapor Downregulate Lung WWOX Expression, Which Is Associated with Increased Severity of Murine Acute Respiratory Distress Syndrome |
| [31618474](https://pubmed.ncbi.nlm.nih.gov/31618474/) | 2019 | ✅ | primary | unmatched | The Genetic Landscape of Epilepsy of Infancy with Migrating Focal Seizures |
| [17360458](https://pubmed.ncbi.nlm.nih.gov/17360458/) | 2007 | ✅ | primary | unmatched | Targeted deletion of Wwox reveals a tumor suppressor function |
| [40263068](https://pubmed.ncbi.nlm.nih.gov/40263068/) | 2025 | — | primary | unmatched | Corrigendum to "WWOX attenuates the progression of gallbladder cancer by suppressing cellular glycolysis through the modulation of the P73/HIF-1a signaling pathway" [Tissue Cell 95 (2025) 102885] |
| [39933386](https://pubmed.ncbi.nlm.nih.gov/39933386/) | 2025 | — | primary | unmatched | Infantile Epileptic Spasms Syndrome: Unveiling clinical and genetic variability in a case series from Argentina |
| [15126504](https://pubmed.ncbi.nlm.nih.gov/15126504/) | 2004 | — | primary | unmatched | Down-regulation of WW domain-containing oxidoreductase induces Tau phosphorylation in vitro. A potential role in Alzheimer's disease |
| [28123895](https://pubmed.ncbi.nlm.nih.gov/28123895/) | 2016 | ✅ | primary | unmatched | The non-inflammatory role of C1q during Her2/neu-driven mammary carcinogenesis |
| [21444760](https://pubmed.ncbi.nlm.nih.gov/21444760/) | 2011 | ✅ | primary | unmatched | The mouse QTL map helps interpret human genome-wide association studies for HDL cholesterol |
| [41561974](https://pubmed.ncbi.nlm.nih.gov/41561974/) | 2026 | ✅ | primary | screened | Genomic and ancestral variations linked to the development of post-acute sequelae of SARS-CoV-2 infection in Indian populations |
| [41007296](https://pubmed.ncbi.nlm.nih.gov/41007296/) | 2025 | ✅ | primary | screened | Prognostic Significance of WWOX/HIF1A Ratio in Cancer Subtypes: Insights into Metabolism, ECM, and EMT |
| [36271927](https://pubmed.ncbi.nlm.nih.gov/36271927/) | 2022 | ✅ | review | screened | WWOX and metabolic regulation in normal and pathological conditions |
| [41510857](https://pubmed.ncbi.nlm.nih.gov/41510857/) | 2026 | — | primary | screened | An Overview of Drug-Resistant Epilepsies Based on Advances in Genetics: A Cohort Study |

*(showing all 428 outstanding records)*

## Already processed from this seed

These records are not reading debt. Their row-level depth is still shown so an
abstract-only paper can be upgraded to a full-text deep dive without being mistaken
for an entirely unprocessed record.

| PMID | Year | FT | Evidence depth | Registry record | Title |
|---|---:|:---:|---|---|---|
| [38161429](https://pubmed.ncbi.nlm.nih.gov/38161429/) | 2023 | ✅ | full text | PAPER 046 | Neuroimaging features of WOREE syndrome: a mini-review of the literature |
| [34268881](https://pubmed.ncbi.nlm.nih.gov/34268881/) | 2021 | ✅ | full text | PAPER 039 | Modeling genetic epileptic encephalopathies using brain organoids |
| [33916893](https://pubmed.ncbi.nlm.nih.gov/33916893/) | 2021 | ✅ | full text | PAPER 040 | Neurological Disorders Associated with WWOX Germline Mutations-A Comprehensive Overview |
| [30362252](https://pubmed.ncbi.nlm.nih.gov/30362252/) | 2019 | ✅ | full text | PAPER 044 | Early infantile-onset epileptic encephalopathy 28 due to a homozygous microdeletion involving the WWOX gene in a region of uniparental disomy |
| [27495153](https://pubmed.ncbi.nlm.nih.gov/27495153/) | 2016 | ✅ | full text | PAPER 049 | W44X mutation in the WWOX gene causes intractable seizures and developmental delay: a case report |
| [26857392](https://pubmed.ncbi.nlm.nih.gov/26857392/) | 2016 | ✅ | full text | PAPER 050 | Relevance of Sp Binding Site Polymorphism in WWOX for Treatment Outcome in Pancreatic Cancer |
| [24932569](https://pubmed.ncbi.nlm.nih.gov/24932569/) | 2014 | ✅ | full text | PAPER 053 | WWOX at the crossroads of cancer, metabolic syndrome related traits and CNS pathologies |
| [24456803](https://pubmed.ncbi.nlm.nih.gov/24456803/) | 2014 | ✅ | full text | PAPER 043 | The supposed tumor suppressor gene WWOX is mutated in an early lethal microcephaly syndrome with epilepsy, growth retardation and retinal degeneration |
| [24369382](https://pubmed.ncbi.nlm.nih.gov/24369382/) | 2014 | ✅ | full text | PAPER 042 | The tumour suppressor gene WWOX is mutated in autosomal recessive cerebellar ataxia with epilepsy and mental retardation |
| [41153369](https://pubmed.ncbi.nlm.nih.gov/41153369/) | 2025 | ✅ | abstract only | PAPER 013 | Genetic Etiology of Developmental and Epileptic Encephalopathy in a Turkish Cohort: A Single-Center Study with Targeted Gene Panel and Whole Exome Sequencing |
| [35328751](https://pubmed.ncbi.nlm.nih.gov/35328751/) | 2022 | ✅ | abstract only | PAPER 023 | The WWOX/HIF1A Axis Downregulation Alters Glucose Metabolism and Predispose to Metabolic Disorders |
| [32581702](https://pubmed.ncbi.nlm.nih.gov/32581702/) | 2020 | ✅ | abstract only | PAPER 020 | Loss of Wwox Perturbs Neuronal Migration and Impairs Early Cortical Development |
| [31543760](https://pubmed.ncbi.nlm.nih.gov/31543760/) | 2019 | ✅ | abstract only | PAPER 022 | The WWOX Gene Influences Cellular Pathways in the Neuronal Differentiation of Human Neural Progenitor Cells |
| [31340538](https://pubmed.ncbi.nlm.nih.gov/31340538/) | 2019 | ✅ | abstract only | PAPER 021 | Loss of Wwox Causes Defective Development of Cerebral Cortex with Hypomyelination in a Rat Model of Lethal Dwarfism with Epilepsy |
| [25331887](https://pubmed.ncbi.nlm.nih.gov/25331887/) | 2014 | ✅ | abstract only | PAPER 027 | WWOX, the common fragile site FRA16D gene product, regulates ATM activation and the DNA damage response |
| [25012504](https://pubmed.ncbi.nlm.nih.gov/25012504/) | 2014 | ✅ | abstract only | PAPER 024 | Tumor suppressor WWOX regulates glucose metabolism via HIF1α modulation |
| [33914858](https://pubmed.ncbi.nlm.nih.gov/33914858/) | 2021 | — | abstract only | PAPER 004 | Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects |
| [42193054](https://pubmed.ncbi.nlm.nih.gov/42193054/) | 2026 | ✅ | full text | PAPER 012 | WWOX-Related Epileptic Encephalopathy (WOREE Syndrome): Clinical Case Study and Literature Review |
| [41562193](https://pubmed.ncbi.nlm.nih.gov/41562193/) | 2026 | ✅ | full text | PAPER 010 | Endogenous Processes Underlying Clock-Like Mutational Signatures |
| [39507621](https://pubmed.ncbi.nlm.nih.gov/39507621/) | 2024 | ✅ | full text | PAPER 015 | Case report: Adult patient with WWOX developmental and epileptic encephalopathy: 40 years of observation |
| [39420317](https://pubmed.ncbi.nlm.nih.gov/39420317/) | 2024 | ✅ | full text | PAPER 028 | Dissociation of the nuclear WWOX/TRAF2 switch renders UV/cold shock-mediated nuclear bubbling cell death at low temperatures |
| [39101447](https://pubmed.ncbi.nlm.nih.gov/39101447/) | 2024 | ✅ | full text | PAPER 016 | Developmental epileptic encephalopathy caused by homozygosity of a c.172+1G>C variant in the WWOX gene |
| [36779245](https://pubmed.ncbi.nlm.nih.gov/36779245/) | 2023 | ✅ | full text | receipt FTR-20260804-36779245-02 | WWOX developmental and epileptic encephalopathy: Understanding the epileptology and the mortality risk |
| [35716775](https://pubmed.ncbi.nlm.nih.gov/35716775/) | 2022 | ✅ | full text | PAPER 055 | Structural insights into the role of the WW2 domain on tandem WW-PPxY motif interactions of oxidoreductase WWOX |
| [34747138](https://pubmed.ncbi.nlm.nih.gov/34747138/) | 2021 | ✅ | full text | PAPER 005 | Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes |
| [34634460](https://pubmed.ncbi.nlm.nih.gov/34634460/) | 2021 | ✅ | full text | PAPER 031 | Altered neocortical oscillations and cellular excitability in an in vitro Wwox knockout mouse model of epileptic encephalopathy |
| [34214506](https://pubmed.ncbi.nlm.nih.gov/34214506/) | 2021 | ✅ | full text | PAPER 054 | Photoreceptor Cell Calcium Dysregulation and Calpain Activation Promote Pathogenic Photoreceptor Oxidative Stress and Inflammation in Prodromal Diabetic Retinopathy |
| [32000863](https://pubmed.ncbi.nlm.nih.gov/32000863/) | 2020 | ✅ | full text | receipt FTR-20260804-32000863-01 | Wwox deficiency leads to neurodevelopmental and degenerative neuropathies and glycogen synthase kinase 3β-mediated epileptic seizure activity in mice |
| [30619736](https://pubmed.ncbi.nlm.nih.gov/30619736/) | 2018 | ✅ | full text | PAPER 032 | Delineating WWOX Protein Interactome by Tandem Affinity Purification-Mass Spectrometry: Identification of Top Interactors and Key Metabolic Pathways Involved |
| [22193544](https://pubmed.ncbi.nlm.nih.gov/22193544/) | 2012 | ✅ | full text | PAPER 056 | WW domain-containing oxidoreductase promotes neuronal differentiation via negative regulation of glycogen synthase kinase 3β |
| [42128308](https://pubmed.ncbi.nlm.nih.gov/42128308/) | 2026 | — | full text | PAPER 029 | WWOX in brain development and disease: Molecular mechanisms and therapeutic opportunities |

*(showing all 31 processed records from the seed)*

## How to work one

```bash
# 1. is it really new? the intake gate decides, not this table
python3 .claude/skills/legend-study-intake-triage/scripts/study_dedup_triage.py \
    --workspace . --input one_record.txt --out triage.md
```

Then, in an agent runtime: *"deep dive PMID …"* for a canonical claim, or
*"squeeze PMID … for leads"* for the discovery ledger. See [`SKILLS.md`](../../../SKILLS.md).

**A low rank here is a queue position, never a verdict.** Nothing in this table authorizes
not reading something: the ranking exists to order the work, and an unread record stays
tracked until it is read. See [`gold_is_in_the_details.md`](../../../framework/master/gold_is_in_the_details.md).

## Add a newer PubMed Clipboard snapshot

Save the PubMed Clipboard email/export as plain text outside the repository, then run:

```bash
python3 framework/scripts/pubmed_clipboard_to_seed.py \
    --input /path/to/pubmed_clipboard.txt \
    --out disease-models/wwox/registries/corpus_seed_pubmed_YYYYMMDD.tsv
python3 framework/scripts/batch_queue.py \
    --out disease-models/wwox/registries/batch_queue.md
```

The converter emits bibliographic fields only; mail headers and sender/recipient data
are discarded. Keep the date in the filename. Repeated PMIDs across snapshots are
counted once in the queue, with every seed filename retained as provenance.

## Scope

Bibliographic metadata only — identifiers, titles, years, open-access flags and processing
state. No full texts are redistributed, and no individual-level information appears here.
