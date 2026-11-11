# IT45 P9: S2 (HCN / Ih) — a pointer on a different relation, qualified by the same path

Non-canonical working note. Not medical advice; no dose, schedule or route. Same `activity_search.py`, dose-response types only, `--max-pages 20`; relation row S2 of `generation_it41_20261109/relations_it41.tsv` (targets HCN1–HCN4; all four COMPLETE). Verdict of every row: ACTIVITY_ONLY.

## What the read gives (catalogue-status molecules only; 6 of 57 molecule x relation rows)
| Molecule (catalogue) | Rows | Reading |
|---|---|---|
| a tool probe (ChEMBL id CHEMBL6195028, no preferred name; document title "Data for DCP probe RO-275", a 2025 deposit with no PubMed id) | HCN1 IC50 43–49 nM (automated patch clamp, inducible HEK293 line), 269 nM (manual electrophysiology); HCN2 14.3 µM; HCN3 4.6 µM; HCN4 13.9 µM — all in **one deposit and one cell system** | HCN1-selective in that deposit by about 100- to 300-fold over the other three isoforms. Within one document the potencies are comparable by the engine's rule; across documents they are not. |
| ivabradine, zatebradine | HCN4 EC50 4.3 and 8.6 µM, "blockade of human HCN4 in HEK293 at −120 mV", one paper (PMID 20795648) | blockers of the cardiac isoform in a paper on isoform-selective f-current blockers; the label "EC50" is the paper's; the direction is a block. |
| a CHK1 inhibitor in clinical development, a neurosteroid, a neuropsychiatric clinical candidate | HCN4 or HCN2 IC50 "greater than" 10–30 µM | counter-screens that found no inhibition; they are negative-selectivity rows, not candidates. |

## What it adds to INV-18 (INFERENZA)
* INV-18 asks for Ih blockers "of at least two chemotypes" and lists an "ortholog and isoform census of the tools" as possible in silico work. The census now exists for the catalogue: the activity rows hold two clinical-stage blockers measured on HCN4 only (micromolar) and **one HCN1-selective probe** measured on all four isoforms; isoform selectivity of the other tools named in the repository was not read here.
* RNA by cell class (SCI44 coda): Hcn1 neurons 2.62 against astrocytes 0.10; Hcn2 neurons 17.9 against 1.1 (mouse P7 FPKM). An HCN1-selective probe can in principle separate an HCN1-carried from an HCN2-carried sag in the same slices, which a non-selective blocker cannot; the sag growth with gene dose (INV-18) then gets an isoform question.
* Limits: the primary source is a probe data deposit, not a paper (no methods text was read); the probe's behaviour in neurons, its stability in slices and its off-target profile are not held; ChEMBL's selectivity is within one assay system; nothing here nominates a tool.

## Question reopened
IT45-Q04 (open-questions map): does an HCN1-selective probe separate the HCN1-carried from the HCN2-carried part of the knockout sag at matched potential? Needs the probe's own page or paper read first (a reading task), then the matched recording (a new measurement).
