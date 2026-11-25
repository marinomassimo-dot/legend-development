# ADV-098 broad batch 7: benztropine, miconazole, clobetasol, bexarotene (the oligodendrocyte-differentiation screen list) (HE, 2026-11-20)

Written for: SCI (unit C, broad objective), ADV, IT. Same rules, routes and recipe as batches 1 to 6: public sources only, no dose, hypothesis level, not medical advice, "not found by these routes" is not absence. Raw ChEMBL answers outside git with digests in `SHA256SUMS_raw_activities.txt`. Identity: all four NAME_EXACT (benztropine CHEMBL1201203, miconazole CHEMBL91, bexarotene CHEMBL1023; clobetasol CHEMBL1201362 has only 10 activity rows, so the drug ingredient clobetasol propionate CHEMBL1159650, 283 rows, was read separately and is not merged). A shorter sheet than the earlier batches: primary-target rows, a COMPARABLE? line, exposure by one or two searches, label.

## COMPARABLE?
- **Four different mechanisms: no potency comparison across the agents.** Benztropine (muscarinic M1 antagonist, dopamine transporter), miconazole (azole inhibitor of sterol demethylases), clobetasol propionate (glucocorticoid receptor agonist), bexarotene (RXR agonist). Each potency belongs to a different target.
- **Within an agent across sources:** benztropine M1: Ki 0.59 and 0.95 nM (rat brain membranes, [3H]pirenzepine, 1995 to 2001) and 0.13 nM (Ki) or 0.54 nM (IC50) in the DrugMatrix human panel: a 7-fold spread between sources. Clobetasol propionate GR: IC50 3.17 nM (rat liver cytosol, [3H]dexamethasone displacement, 1991) against 0.66 nM Ki (DrugMatrix, human; the same panel gives IC50 1.46 nM (corrected 2026-11-25, HE; see the dated line at the end)): different species and sources. Bexarotene: within one 1997 document (CHEMBL1130267) Ki 5.9 nM (RXR-beta), 8.3 nM (RXR-gamma), 16 nM (RXR-alpha) against 180 nM (RAR-alpha), 50 nM (RAR-beta) and 130 nM (RAR-gamma): an RXR preference of about 3- to 30-fold in that document (only 3- to 8-fold against RAR-beta), which is a comparable contrast (**corrected 2026-11-25, HE:** the first version compared with RAR-alpha alone and said 11- to 30-fold, although the held answer had the other two rows; other held documents report RAR Ki or Kd above 1 microM, and one, CHEMBL1132591, an RAR-alpha EC50 of 6 nM against a Ki of 5.4 microM, not reconciled); other documents give human RXR-alpha EC50 from 2.7 to 149 nM and Kd from 14 to 1,890 nM (measured rows) (corrected 2026-11-25, HE; see the dated line at the end).
- **Miconazole's measured target is not the myelination mechanism read here.** Rows: human CYP51 IC50 200 nM (lanosterol demethylase, Topp 3 cells, 2007); mycobacterial and amoebal CYP51 Kd values; CYP3A4, ABCB1, CYP1A2 and CYP2C19 in the largest row groups. The sterol-pathway mechanism proposed in the literature for oligodendrocyte differentiation is **not found in these rows**; a CYP51 value is not a measurement of that mechanism.

## What the literature titles say (not read beyond titles) about myelination, separate from the potency rows
Benztropine, miconazole, clobetasol and bexarotene are named by their titles in oligodendrocyte or myelin-repair work: miconazole "activates MAPK-driven oligodendrogenesis to promote myelin regeneration..." (PMID 40825461, 2025); clobetasol "promotes remyelination in a mouse model of neuromyelitis optica" (PMID 27117475, 2016) and "Drug-based modulation of endogenous stem cells promotes functional remyelination in vivo" (PMID 25896324, 2015), and chemotherapy-induced MS-like neuropathology rescued by clobetasol (PMID 41388189, 2026); bexarotene: "Retinoid X receptor activation reverses age-related deficiencies in myelin debris phagocytosis and remyelination" (PMID 26463675, 2015). These are efficacy studies by title; none was read here, and none is a potency row in ChEMBL.

## Benztropine (CHEMBL1201203)
- **Potency (299 rows):** M1 as above; sodium-dependent dopamine transporter (17 rows) and serotonin transporter (5 rows) are the other main groups (values not tabulated here). `NOT_ASSESSED` for selectivity.
- **Exposure:** the PubMed pharmacokinetic and brain-distribution hits are for **benztropine analogs** (for example a 2008 GA2-50 paper and chloro-benztropine analog papers, titles read), not for benztropine itself; benztropine in an oligodendrocyte context: 0 records. **Not found by these routes:** a mouse or rat brain concentration of benztropine.
- **Label (openFDA SPL, 3 labels, newest 2026-11-11):** adjunct in parkinsonism and extrapyramidal disorders; the label says it should be used with caution in pediatric patients over three years because of atropine-like effects (text read in part). No dose given here.

## Miconazole (CHEMBL91; the nitrate CHEMBL1559 is separate)
- **Potency (400 rows):** see above. **Exposure:** "miconazole brain concentration mice remyelination" 0 records (a query shape); an oligodendrocyte-precursor search gave 2 records (titles above). **Not found by these routes:** brain or plasma concentration in rodents.
- **Label (openFDA SPL, 3 labels, newest 2025-10-29):** over-the-counter topical antifungal; the pediatric section is empty in the first label. A topical label says nothing about systemic or CNS exposure.

## Clobetasol propionate (CHEMBL1159650)
- **Potency:** glucocorticoid receptor IC50 3.17 nM (rat liver cytosol) and Ki 0.66 nM (DrugMatrix human); cytochrome P450 3A5 (7 rows), 3A4 (4 rows) and bile salt export pump (3 rows) are the other groups (corrected 2026-11-25, HE; see the dated line at the end).
- **Exposure:** a lactoferrin-coated oleosome formulation paper (PMID 39053824, 2024, title read) shows that CNS delivery is a formulation problem for a topical corticosteroid; no rodent brain concentration of plain clobetasol found by these routes.
- **Label (openFDA SPL, 3 labels, newest 2026-08-07):** topical super-high-potency corticosteroid for dermatoses; "safety and effectiveness in pediatric patients have not been established; use in patients under 12 years is not recommended" (text read in part). No dose given here.

## Bexarotene (CHEMBL1023)
- **Potency (811 rows):** RXR-alpha 47 rows, RXR-gamma 19, RXR-beta 18, RAR-beta 12, RAR-alpha 10 (the largest groups). Values above.
- **Exposure:** a mouse plasma and brain LC-MS/MS quantification method with an application (PMID 34840083, 2022, title read, abstract not read): a mouse brain measurement exists in the literature; the numbers were **not read**. Juvenile: not found by these routes.
- **Label (openFDA SPL, 3 labels, newest 2020-04-30):** cutaneous T-cell lymphoma refractory to a prior systemic therapy; "safety and effectiveness in pediatric patients have not been established". No dose given here.

## ISRIB (identity only; trazodone, omaveloxolone, dichloroacetate next)
- `compound_identity.py` returns NOT_FOUND_BY_NAME. By structure: PubChem name lookup returns CID 1011240, 2-(4-chlorophenoxy)-N-[4-[[2-(4-chlorophenoxy)acetyl]amino]cyclohexyl]acetamide, InChIKey HJGMCDHQPXTGAV-UHFFFAOYSA-N, and its synonym list names CHEMBL4303573. Potency rows not yet pulled.

## What changes for SCI's unit C
1. None of the four has a ChEMBL row that measures an oligodendrocyte-differentiation or myelination effect; what links them to the broad objective is literature read at title level.
2. Exposure in rodents: bexarotene has a mouse plasma and brain method paper; the other three have none found by these routes (benztropine only for analogs).
3. Pediatric label status separates them: benztropine "caution over three years", clobetasol "not recommended under 12", bexarotene and miconazole not established or not stated.

## Dated line 2026-11-25: row-by-row re-check against every held row (HE)
Every fold, range and count of this sheet that rests on the held ChEMBL answers was recomputed against all rows of those answers. A first-written wording is kept here so that a copy of it elsewhere can be recognised.
- **7a** first written: "against 0.66 nM Ki (DrugMatrix, human): different species and sources."
- **7b** first written: "cytochrome P450 3A5 and 3A4 rows and bile salt export pump rows (3 each) are the other groups."
- **7c** first written: "other documents give RXR-alpha EC50 28 and 42 nM and Kd 36 nM (1995 and 2002)."
