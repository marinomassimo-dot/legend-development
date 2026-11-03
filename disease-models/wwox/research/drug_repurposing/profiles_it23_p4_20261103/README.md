# IT23 P4: CANDO interaction signatures as a multi-protein comparison next to LEGEND's per-target search (2026-11-03)

Non-canonical research material, producer output. Public edition: the WWOX-DEE reference genotype class, never an individual. **Not medical advice.** Zero spend, no registration or account; the only requests made were anonymous downloads and UniProt look-ups by accession; no e-mail address or personal datum was sent anywhere, and none is copied here. Downloads sit in the session scratchpad, never in the repository. No state-changing git command was run; only this folder was written.

## 1. Decision (first)

**WATCH. Not adopted, not rejected.** The matrix is real, openly downloadable, numerically comparable and joins well to LEGEND's catalogue. It nevertheless cannot answer a WWOX question as it stands, for three reasons that are separate and each sufficient:

1. **Meaning.** The score is not an action, a potency or a prediction of binding to the protein. It is `CxP`: for each compound and protein row, the maximum over the ligands *predicted* (COACH) to occupy that protein's pocket of [ECFP4 Dice similarity(compound, ligand) x COACH site confidence] (read from `calc_scores` in `cando.py`). It carries **no direction** (agonist, inhibitor and blocker score alike), no units, no selectivity, no exposure. The sign convention that LEGEND's typed comparison needs does not exist in it.
2. **Identity and coverage of what matters.** The matrix holds only the 2,449 DrugBank *approved* compounds. **Tiratricol, sobetirome, resmetirom and every EZH2 inhibitor of LEGEND's dossiers are absent** (tiratricol and tazemetostat are DrugBank "investigational"; resmetirom is not in the v2.2 compound list at all). So the TR-agonist and EZH2 questions cannot be scored. The disease gene WWOX, NFE2L2, HDAC11, ZHX2 are absent from the 8,385-row human matrix.
3. **Row artefacts.** A protein is one or two PDB chains, not a protein: the same protein, THRB, scores liothyronine 0.950 (rank 1 of 2,449) in one chain and 0.094 (rank 1,569) in the other. The fingerprint is stereo-blind (levothyroxine and dextrothyroxine have identical scores everywhere, cosine 1.000). Metal ions and cofactors dominate pocket-ligand lists (the top neighbours of an "HDAC profile" are zinc, calcium, cobalt, potassium).

**What it could change: nothing in LEGEND's current selection** (section 5). Its one defensible use is a hypothesis seed: "this approved drug resembles a ligand predicted at protein X, and LEGEND's typed table has no value there". That is a similarity statement; it does not transfer any biological evidence.

**Revisit (WATCH to ADOPT-OPTIONAL) if any of these happens:** a licence statement for the data (section 2); the 665 MB "all compounds" matrix or a signature generated for tiratricol/resmetirom/EZH2 inhibitors is obtained (hours of work and a similarity score still); a WWOX question is itself a similarity question (find analogues of a compound with measured effect); a direction-bearing score appears.

## 2. Assets and licences (`assets.tsv`)

| Asset | Where, version | Licence for that asset |
|---|---|---|
| Code | github.com/ram-compbio/CANDO, last push 2026-07-23; releases up to v2.2.1 (2021-08-06) | **BSD-3-Clause.** `LICENSE.md` read in full: "Copyright 2019 William Mangione ... Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:" (three clauses, no non-commercial term) |
| Usable matrix and mapping | Zenodo 17241534 (doi 10.5281/zenodo.17241534), v2.3.X, 2025-10-23; `rd_ecfp4-homo_sapien-v2.5-approved-int_vect-dice-CxP.tsv` 123,262,814 bytes (md5 458e60cf...), `drugbank-v2.5-approved.tsv` 110,370 bytes | **BSD-3-Clause, declared in the record metadata** (`license: {id: bsd-3-clause}`). A declared container licence cannot grant rights in DrugBank-derived identifiers or PDB/COACH ligand content; DrugBank's terms were **not read** here |
| Demonstration matrix | project site `.../cando/data/v2.2+/tutorial/tutorial_matrix-approved.tsv`, 940,800 bytes, Last-Modified 2021-04-09 | **No licence statement found** (landing page, data index; no LICENSE file: HTTP 404). The code's BSD-3 does not cover it |
| Compound map, PDB-to-UniProt map | same site, `cmpds-v2.2.tsv` 757,385 bytes; `pdb_2_uniprot.csv` 30,672,552 bytes | **No licence statement found** |
| "All compounds" matrix | same site, 665,051,204 bytes | not fetched (above the 300 MB cap); no statement either |

Consequence for the repository: only small derived tables are written here (`comparison.tsv`: 8 compounds x 36 protein rows; `identity_join.tsv`: identifiers and names; `coverage*.tsv`), no raw matrix. Whether even those derived score tables may stay in the public tip is a reserved licence question for the operator (release-surface rule: no third-party raw in git), not settled by the Zenodo label. The CANDO publications were not read for this package; every statement about the score comes from the code and the notebook.

## 3. Coverage, identity and meaning (`coverage.tsv`, `coverage_demo64.tsv`, `identity_join.tsv`)

**The 64-protein demonstration matrix** (`coverage_demo64.tsv`): 64 PDB chains of which only **11 are human** (APOE, HSH2D, EXOSC10, PKP2, PPIE, BRD7, STK3, SQSTM1, HEY1, UBAC1, OBSCN); the rest are bacterial, yeast, mouse, archaeal, plant, a designed protein and others. Of 48 genes that a LEGEND package names (`coverage.tsv`), **4 are in it** (STK3 as the Hippo kinase MST2, SQSTM1, BRD7 which is not BRD4, APOE which serves no question). None of HDAC1-11, EZH1/2, BRD4, THRA/THRB, NFE2L2/KEAP1, MAPK1/3, AHR, CDK4/6 is present. It is a technical test set, as the notebook says ("most real matrices contain significantly more proteins"). Its score is `dCxP` (percentile-transformed), a different scale from the Zenodo `CxP`; the two must not be mixed.

**The usable Zenodo matrix:** 8,385 rows x 2,449 compounds, scores 0 to 1 (4.4 % exact zeros). Row ids are PDB chains (5,316) or bare UniProt accessions (3,069, modelled structures); every row maps to at least one UniProt accession; **7,880 distinct human gene symbols**; 60 accessions are unresolved in UniProt today (obsolete) and carry no symbol. Of the 48 genes tested, **43 are present** (HDAC1-10, EZH1, EZH2, BRD4, THRA, THRB, KEAP1, MAPK1/3, AHR, CDK4/6, GSK3B, GRIN1/2B, EGLN1/2, HIF1A, LDHA, PKM, SIRT1-3, KDM1A, DNMT1, HSPA8, LAMP2, WWP1, YAP1, STK3, XIAP, SLC2A1). **Absent: WWOX, HDAC11, NFE2L2, SQSTM1, ZHX2.** Genes with two chains (HDAC6, BRD4, THRB, KEAP1, DNMT1, HSPA8) have two rows and the rows can disagree strongly.

**Column identity.** Columns follow the compound-map order (the approved rows of `cmpds-v2.2` and `drugbank-v2.5-approved` are the same 2,449 ids in the same order, checked). Sanity of that order: vorinostat ranks 4 of 2,449 at the HDAC8 chain and 1 at the HDAC6 chain 5eduB, liothyronine ranks 1 at both THR chains (score 0.950).

**Join to LEGEND (`identity_join.tsv`, key = DrugBank id, then catalogue InChIKey and family; names only reported, never joined on).**

| Outcome | Compounds |
|---|---|
| matched to exactly one catalogue family | **2,168** (2,115 distinct families) |
| matched to several families (ChEMBL family plus an unmerged DGIdb-only record) | 5 |
| no catalogue record with that DrugBank id | 276 |
| with an InChIKey | 2,073 |
| with at least one signed action row in LEGEND's family action table | **847** |
| name differs from the catalogue name (informational: salts, "anhydrous", "ion") | 189 |

Meaning of the zero-action cases: the catalogue never merges records on a name, so a DGIdb-only record of the same drug is a separate family (panobinostat: ChEMBL family `PANOBINOSTAT LACTATE` has targets but no signed action; the signed HDAC rows would sit in the unmerged `Panobinostat` DGIdb family). "0 signed actions" there is a join rule, not an absence of pharmacology.

## 4. The small set (`comparison.tsv`, `profile_similarity.tsv`)

Eight approved compounds, chosen for different roles. Score = CxP, rank of 2,449 in brackets, per protein row used.

| Compound (role) | Desired action at | Preserve / opposing | Matrix result |
|---|---|---|---|
| liothyronine (TR agonist, T3) | THRA 0.950 (1), THRB 0.950 (1) and 0.094 (1569) | none | top because T3 is the pocket ligand itself; identical score at THRA and THRB: **no isoform information** |
| levothyroxine (T4 prohormone) | THRA 0.850 (2), THRB 0.870 (2) | none | typed table has THRB IC50 only |
| dextrothyroxine (D-T4; not in the LEGEND dossier) | identical to levothyroxine | cardiac liability class unknown here | stereo-blind: cannot separate D from L |
| vorinostat (HDAC probe class, HDAC6 lever class) | HDAC1 0.860 (2), HDAC2 (3), HDAC3 (5), HDAC8 (4), HDAC6 0.730 (1) | the EZH2/OPC axis is the thing to preserve; a pan-HDAC inhibitor is the opposite-sign analogue | agrees with typed Ki 1.3 to 5 nM only in kind; a second HDAC6 chain gives rank 580 |
| panobinostat (HDAC, potency contrast) | HDAC1 0.560 (15), HDAC8 0.507 (24) | as above | scores lower than vorinostat at every HDAC; the typed values are EC50, not comparable with vorinostat's Ki, so the matrix ordering is **not** a potency ordering and must not be read as one |
| chloroquine (lysosomal-flux arm) | no row of a lysosomal-flux target was scored | CDK4 0.356 (288) | an unexpected resemblance with no typed or action datum behind it |
| palbociclib (CDK4/6: potential opposing action on OPC cycle exit) | opposing: CDK4 0.710 (2), CDK6 0.690 (7) | EZH2 0.311 (85) | CDK4/6 agrees with typed IC50 11 and 16 nM; the EZH2 rank 85 is similarity to an adenine-like pocket ligand, not EZH2 activity |
| dimethyl fumarate (NRF2 activator, covalent) | KEAP1 0.126 (2052), 0.150 (2037) | none | the mechanism (covalent cysteine modification) is invisible to a similarity score; a worked example of a miss |

Profile similarity over the whole signature (`profile_similarity.tsv`): liothyronine ~ levothyroxine 0.850 (rank 2 of 2,449); vorinostat ~ panobinostat 0.398 over all 8,385 rows but 0.935 over the HDAC-centred 30-gene subset, i.e. the closeness depends on which proteins are chosen; liothyronine ~ vorinostat 0.279 (rank 303) shows that unrelated mechanisms can be "close" on a whole signature. Top neighbours of liothyronine on the TR rows are the retinoids (a nuclear-receptor pocket neighbourhood), of vorinostat on the HDAC rows zinc, calcium, belinostat, cobalt.

Recovery test (`recovery.tsv`): for 12 protein rows where LEGEND has at least two approved compounds with a signed action, the AUC of the matrix for recovering them has median 0.74 (range 0.12 to 1.0). It recovers them when pocket ligands are close analogues (THR 1n46A and 3ilz, CDK4/6, DNMT1: 0.96 to 1.0) and fails otherwise (THRB second chain 0.35, KEAP1 0.18 and 0.24, GSK3B 0.12, NMDAR 0.46 and 0.53). Each row has 2 to 7 known compounds: an indication, not a statistic. Direction is not encoded: the activation-like set (3 rows, all thyroid receptor) and the inhibition-like set (9 rows, median AUC 0.53) differ only through which ligand series the pockets happen to contain.

## 5. Against the existing matching, and what depends on the sign

LEGEND's typed same-measure comparison (`generation_it22_p1_20261103/class_alternatives_it22.py`, run with the catalogue cache for THRA, THRB, HDAC1-8, CDK4/6, KEAP1, EZH2, BRD4; 369 rows) gives, for this set: tiratricol THRB Kd 0.02 nM, T3 THRA Kd 0.1 and THRB Kd 0.079 nM, T4 THRB IC50 3.02, resmetirom THRB 17.8-fold over THRA (EC50 vs EC50), vorinostat Ki 1.3 to 5 nM at HDAC1/2/3/6, panobinostat EC50 3 to 248 nM, palbociclib IC50 11/16 nM.

* **TR class.** The typed table already separates the isoform (resmetirom 17.8x for THRB; T3 none) and ranks tiratricol above T3. The matrix cannot: tiratricol and resmetirom are not in it, THRA and THRB tie for T3, D and L thyroxine tie. **No change to the selection.**
* **HDAC class.** The matrix puts vorinostat above panobinostat; the typed table forbids that comparison (Ki vs EC50). Adopting the matrix ordering would introduce exactly the cross-measure ranking the typed method was built to refuse. **No change.**
* **Opposing action (CDK4/6).** Matrix and typed table agree; the family table already carries the sign. **No new information.**
* **Dependence on the sign convention** (`sign_sensitivity.tsv`). Reading A (high score = resembles a ligand predicted at the pocket) is the only reading the construction supports. Reading B (low score = more of the action) was computed only to measure sensitivity: for all 16 compound-by-subset cases the top 25 of A and of B **do not overlap at all**, and a compound's own rank moves from 1 to 2,449 (vorinostat on HDACs). Any selection made from this matrix therefore rests wholly on the premise that "resembles a ligand" means "has the desired action", which is false for inhibitors versus agonists sharing a pocket series and for covalent and allosteric mechanisms. Nothing in the data tests that premise for WWOX.

"More interactions" is not "more benefit": the number of high-scoring proteins in a signature measures pocket-ligand resemblance across a library dominated by nucleotide, metal and cofactor sites; it is not breadth of useful pharmacology. Similarity to a known compound transfers none of its evidence, and potency, selectivity and exposure are not in this matrix.

## 6. Why the matrix stops here (step 5)

It cannot answer a WWOX question because (coverage) the compounds the questions are about are not in it and WWOX, NFE2L2 and HDAC11 have no row; (identity) a protein is a chain, rows of one protein disagree, stereoisomers collapse, and 276 compounds have no catalogue record; (meaning) the score has no direction, units or potency and was never calibrated to an effect in any WWOX system. Stopped there.

## 7. Files and reproduction

| File | Content |
|---|---|
| `assets.tsv` | assets, versions, sizes, checksums, licence lines read |
| `coverage.tsv`, `coverage_demo64.tsv` | 48 question genes against both matrices; the 64 demo rows with organism |
| `identity_join.tsv` | 2,449 compounds joined by DrugBank id to catalogue id, ChEMBL, InChIKey, family |
| `comparison.tsv` | 8 compounds x protein rows, score, rank, percentile, LEGEND action where present |
| `profile_similarity.tsv`, `sign_sensitivity.tsv`, `recovery.tsv` | section 4 and 5 numbers |
| `cando_profiles_it23_p4.py`, `run_log.txt` | script and its console output (the log is from a re-run without `--fetch`; its first line notes the 60 unresolved accessions) |

```
S=<scratch dir>; export LEGEND_CATALOG_CACHE=disease-models/wwox/research/drug_repurposing/catalog/cache
systemd-run --user --scope -p MemoryMax=4G -p MemorySwapMax=0 \
  python3 cando_profiles_it23_p4.py --work $S --fetch      # fetch caps each download at 300 MB; run twice without --fetch to reuse the cache
```

Limits stated plainly: the CANDO papers and DrugBank, PDB and COACH terms were not read; COACH ligand lists were not inspected (the ion and cofactor claim comes from the neighbours the script prints); the website matrix was compared with the Zenodo copy by size and the first 3 MB only; no signature was generated for absent compounds.
