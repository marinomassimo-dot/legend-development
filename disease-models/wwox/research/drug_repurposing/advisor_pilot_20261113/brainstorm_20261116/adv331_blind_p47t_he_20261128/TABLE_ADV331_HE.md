# ADV-331: blind reading of Hussain 2023, Prog Neurobiol (PMID 36828035), blood values (HE, 2026-11-28)

Reader: HE (ACTOR_ID plan), session c72e94ee, claude-sonnet-5-5, effort high. No delegate.
Blind: IT's ADV-330 folder and PREREG, dossier item 9 and notes on the expected answer were not opened. Extraction only; no claim;
not medical advice. Version read: the held NIHMS author manuscript, not the publisher's version of record.

## What was and was not read

| Source (under files/) | Read | sha256 (first 16) |
|---|---|---|
| fulltext/PMID36828035_Hussain2023.pdf (39 pages) | Results 2.2, Methods 4.1 (housing, survival cohort), 4.3 and statistics, Fig 1 legend; whole text layer term-searched | f51db304ab2938a0 |
| supplement/PMID36828035/...Supplementary_tables.docx | Supplementary Tables 1-4, whole file | fd5b3926a5cf0c33 |
| supplement/PMID36828035/...Supplementary_figures.pdf (15 pages) | S2 legend; figure legends and text layer term-searched; images not viewed | 6d48816e9281645c |
| supplement/PMID36828035/...Supplementary_data.xlsx, sheets PFC, CTX, HPC, CB | sheet names, headers, term search (expression tables) | 34486b446a116ae2 |
| supplement/PMID36828035/...Supplementary_gene_data.xlsx, sheet Sheet1 | headers, term search (expression table) | 8221d68dd64a5137 |
| fulltext/..._assets/nihms-1957654-f0001.jpg (Fig 1) | viewed | 3a8e73046dd28bb4 |
| Main figures 2-9 images | NOT VIEWED (term search of their text only) | |

Terms searched: albumin, glucose, calcium, urea, BUN, bicarbonate, CO2, blood, serum, plasma, chemistry, fasting, pool, weight, survival.
No other printed blood-chemistry or serum analyte was found outside Supplementary Table 2.

## 1. Blood chemistry: every row of Supplementary Table 2

Printed as "Average ± SEM". Median: NOT PRINTED for any analyte. Statistic: the column is "p value" and every row reads "ns"; no exact P and no
test is named in the table (the general statistics section, PDF p. 20, names ANOVA with Tukey for more than two groups). Per-analyte n: NOT PRINTED
(the group n in the header). No plot of these analytes was found. Units are copied as printed, including "U/L" for creatinine.

| Table, row | Analyte (unit, as printed) | WT/WT (n=9) | P47T/WT (n=16) | P47T/P47T (n=16) | P, as printed | Sample; stage |
|---|---|---|---|---|---|---|
| S2, r1 | Albumin (g/dL) | 3.93 ± 0.13 | 3.58 ± 0.13 | 3.53 ± 0.13 | ns | serum; see section 3 |
| S2, r2 | Alkaline phosphatase (U/L) | 70.11 ± 13.14 | 88.13 ± 33.62 | 55.2 ± 4.39 | ns | serum; see section 3 |
| S2, r3 | Alanine aminotransferase (U/L) | 79 ± 33.80 | 98.25 ± 30 | 48.73 ± 3.79 | ns | serum; see section 3 |
| S2, r4 | Amylase (U/L) | 1081.55 ± 48.40 | 1206.81 ± 71.01 | 1145.28 ± 40.91 | ns | serum; see section 3 |
| S2, r5 | Total bilirubin (mg/dL) | 0.3 ± 0 | 0.31 ± 0.04 | 0.29 ± 0.01 | ns | serum; see section 3 |
| S2, r6 | Urea nitrogen (mg/dL) | 19.11 ± 1.14 | 22.26 ± 2.98 | 20.86 ± 1.24 | ns | serum; see section 3 |
| S2, r7 | Calcium (mg/dL) | 11.57 ± 0.15 | 11.5 ± 0.31 | 11.26 ± 0.26 | ns | serum; see section 3 |
| S2, r8 | Phosphorus (mg/dL) | 11.66 ± 0.78 | 13.4 ± 0.65 | 12.62 ± 0.79 | ns | serum; see section 3 |
| S2, r9 | Creatinine (U/L) | < 0.24 | < 0.36 | < 0.31 | ns | serum; see section 3 |
| S2, r10 | Glucose (mg/dL) | 296 ± 25.47 | 267.25 ± 30.25 | 254.33 ± 22.52 | ns | serum; see section 3 |
| S2, r11 | Sodium (mmol/L) | 153.66 ± 1.25 | 154.56 ± 1.18 | 152.86 ± 1.49 | ns | serum; see section 3 |
| S2, r12 | Potassium (mmol/L) | >8.48 | > 9.38 | >9.22 | ns | serum; see section 3 |
| S2, r13 | Total protein (g/dL) | 5.51 ± 0.22 | 5.63 ± 0.14 | 5.38 ± 0.08 | ns | serum; see section 3 |
| S2, r14 | Globulin (g/dL) | 1.78 ± 0.08 | 2.05 ± 0.15 | 1.83 ± 0.14 | ns | serum; see section 3 |

Creatinine and potassium are printed as bounds ("<", ">") with no spread.

## 2. Glucose, total CO2, BUN, calcium

| Analyte | WT/WT | P47T/WT | P47T/P47T | Where |
|---|---|---|---|---|
| Glucose (mg/dL) | 296 ± 25.47 | 267.25 ± 30.25 | 254.33 ± 22.52, ns | Table S2 |
| Total CO2 / bicarbonate | NOT PRINTED | NOT PRINTED | NOT PRINTED | absent from all 14 rows of Table S2 and from Table S3; not found in the PDF, supplement figure text or workbooks ("CO2" occurs for asphyxiation and cell incubation) |
| Urea nitrogen, BUN (mg/dL) | 19.11 ± 1.14 | 22.26 ± 2.98 | 20.86 ± 1.24, ns | Table S2 |
| Calcium (mg/dL) | 11.57 ± 0.15 | 11.5 ± 0.31 | 11.26 ± 0.26, ns | Table S2 |

Stage (one stage only; no second time point and no presymptomatic sample is printed):
- Methods 4.3 (PDF p. 16): "Mice were euthanized by CO2 asphyxiation at moribund stage. Blood was collected immediately following euthanasia by
  intracardiac puncture on the left ventricle."
- Results 2.2 (PDF pp. 4-5) states it differently: "Mice were necropsied and histology samples were collected either at the end of the experimental
  period or after euthanasia due to poor health. Animal weight was monitored, and blood samples were collected".
- Which of the n animals were moribund and which were sampled at the end of the experiment: NOT PRINTED. So "moribund" is the Methods wording for the
  blood draw; it cannot be assigned animal by animal. Age at sampling, per group or per animal: NOT PRINTED.

## 3. Sample, fasting, numbers, pooling

| Item | Printed | Where |
|---|---|---|
| Chemistry sample | serum: clot 30 min at room temperature, 10 min at 14,000 rpm; left-ventricle puncture after euthanasia | Methods 4.3 |
| Hematology sample | fresh whole blood | Methods 4.3 |
| Analyzers | ABAXIS VETSCAN VS2 (chemistry), HM5 (hematology); rotor or panel NOT PRINTED | Methods 4.3 |
| Fasting state | NOT PRINTED (no "fast/fasted/fasting" in the PDF text); diet "regular commercial mouse diet" | Methods 4.1 |
| Time of day | NOT PRINTED (only the 12 L:12 D cycle) | Methods 4.1 |
| Pooling | none stated; "Serum from each individual mouse was analyzed"; no pooled sample found | Methods 4.3 |
| Animals, weight and blood | WT/WT n=9 (4 M, 5 F); P47T/WT n=16 (13 M, 3 F); P47T/P47T n=16 (8 M, 8 F) | Methods 4.3 |
| Animals, survival | WT/WT n=14 (7 M, 7 F); P47T/WT n=30 (21 M, 9 F); P47T/P47T n=25 (15 M, 10 F) | Methods 4.1; Fig 1b |
| Overlap of the two sets | NOT PRINTED. The blood and weight n are smaller; whether they are a subset of the survival cohort is not stated | |

## 4. Body weight and survival

| Measure | WT/WT | P47T/WT | P47T/P47T | Statistic | Where |
|---|---|---|---|---|---|
| Body weight, g, "mean (±)" in text | 41.17 (±9.52), n=9 | 37.39 (±6.08), n=16 | 29.22 (±4.28), n=16 | P47T/P47T vs each other group, p < 0.005; One-Way ANOVA, Tukey (Fig 1 legend) | Results 2.2; Fig 1c |
| Body weight median, g (read from the box plot, about) | 42 | 37 | 29.5 | | Fig 1c image |
| Box 25th-75th, g (read, about) | 34.5-48 | 33-42.5 | 25-33 | | Fig 1c image |
| Whiskers min-max, g (read, about) | 24.5-55.5 | 27-49 | 22-37 | | Fig 1c image |
| Mean survival, days "(±)" | 542 (±8), n=14 | 495 (±23), n=30 | 393 (±32; printed "32ds."), n=25 | log-rank p=0.001, P47T/P47T vs the two other groups; P47T/WT vs WT/WT not significant | Results 2.2; Fig 1b |
| Surviving fraction at the end of the curve, about day 590 (read) | 0.89 | 0.74 | 0.28 | censored | Fig 1b image |
| Median survival | NOT PRINTED | NOT PRINTED | NOT PRINTED | | |
| Age at weighing | NOT PRINTED | NOT PRINTED | NOT PRINTED | | |

- The spread type of the weight and survival "±" is not labelled where it is printed. The statistics section says "All data are presented as mean ± SEM",
  but for weight that cannot hold (inference from arithmetic: SEM 9.52 with n=9 means SD 28.6 g, while the plotted WT range is about 31 g), so the weight
  "±" reads as SD. The paper does not say so.
- Related organ values: Supplementary Fig S2b-f, relative organ weights (kidney and liver higher in P47T/P47T, p < 0.05); bar values not read.

## 5. Hematology: every row of Supplementary Table 3 (whole blood; not serum chemistry)

Same header, "Average ± SEM", every row "ns"; count units are printed with flattened exponents (103, 106 cells per µL).

| Table, row | Analyte (unit, as printed) | WT/WT (n=9) | P47T/WT (n=16) | P47T/P47T (n=16) | P, as printed | Sample; stage |
|---|---|---|---|---|---|---|
| S3, r1 | White blood cells (103 cells/µL) | 5.71 ± 0.74 | 4.99 ± 0.60 | 4.08 ± 0.45 | ns | whole blood; see section 3 |
| S3, r2 | Neutrophils (103 cells/µL) | 1.99 ± 0.33 | 2.15 ± 0.56 | 1.53 ± 0.26 | ns | whole blood; see section 3 |
| S3, r3 | Lymphocytes (103 cells/µL) | 3.28 ± 0.35 | 2.5 ± 0.27 | 2.28 ± 0.23 | ns | whole blood; see section 3 |
| S3, r4 | Monocytes (103 cells/µL) | 0.23 ± 0.04 | 0.2 ± 0.02 | 0.19 ± 0.02 | ns | whole blood; see section 3 |
| S3, r5 | Eosinophils (103 cells/µL) | 0.16 ± 0.06 | 0.09 ± 0.02 | 0.07 ± 0.01 | ns | whole blood; see section 3 |
| S3, r6 | Basophils (103 cells/µL) | 0.05 ± 0.02 | 0.02 ± 0.01 | 0.02 ± 0 | ns | whole blood; see section 3 |
| S3, r7 | Neutrophils (%) | 33.79 ± 2.17 | 38.27 ± 4.77 | 35.52 ± 2.89 | ns | whole blood; see section 3 |
| S3, r8 | Lymphocytes (%) | 59.18 ± 1.97 | 54.41 ± 4.39 | 56.8 ± 2.82 | ns | whole blood; see section 3 |
| S3, r9 | Monocytes (%) | 4.15 ± 0.73 | 5.02 ± 0.89 | 5.37 ± 0.64 | ns | whole blood; see section 3 |
| S3, r10 | Eosinophils (%) | 2.21 ± 0.57 | 1.81 ± 0.31 | 1.84 ± 0.23 | ns | whole blood; see section 3 |
| S3, r11 | Basophils (%) | 0.65 ± 0.18 | 0.46 ± 0.09 | 0.45 ± 0.07 | ns | whole blood; see section 3 |
| S3, r12 | Red blood cells (106 cells/µl) | 9.22 ± 0.26 | 8.99 ± 0.49 | 9.26 ± 0.30 | ns | whole blood; see section 3 |
| S3, r13 | Hemoglobin (g/dL) | 11.31 ± 0.39 | 10.93 ± 0.53 | 11.7 ± 0.45 | ns | whole blood; see section 3 |
| S3, r14 | Hematocrit (%) | 45.15 ± 1.39 | 44.32 ± 2.08 | 46.37 ± 1.40 | ns | whole blood; see section 3 |
| S3, r15 | Mean corpuscular volume (fL) | 48.95 ± 0.19 | 50.08 ± 1.17 | 50.15 ± 0.34 | ns | whole blood; see section 3 |
| S3, r16 | Mean corpuscular Hb (pg) | 12.26 ± 0.21 | 12.28 ± 0.25 | 12.65 ± 0.28 | ns | whole blood; see section 3 |
| S3, r17 | MCHC (g/dL) | 25.05 ± 0.44 | 24.59 ± 0.42 | 25.21 ± 0.55 | ns | whole blood; see section 3 |
| S3, r18 | Red cell distribution width (%) | 16.68 ± 0.15 | 19.14 ± 1.31 | 17.39 ± 0.25 | ns | whole blood; see section 3 |
| S3, r19 | Platelets (103 cells/µL) | 1342.7 ± 128.01 | 1378.87 ± 138.92 | 1098.5 ± 93.72 | ns | whole blood; see section 3 |
| S3, r20 | Mean platelet volume (fL) | 5.4 ± 0.06 | 5.51 ± 0.07 | 5.36 ± 0.09 | ns | whole blood; see section 3 |

## Receipt

Partial read; receipt recorded in disease-models/wwox/registries/fulltext_read_receipts.jsonl (workflow ADV-331 blind extraction).
