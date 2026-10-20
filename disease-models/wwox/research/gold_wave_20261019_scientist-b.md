# Gold wave 2026-10-19 — Scientist B — WWOX-direct re-reads of legacy-only and artefact-absent papers

Actor `scientist-b`, task `GOLD-LEGACY-WWOX-B-20261019`, branch `task/GOLD-LEGACY-WWOX-B-20261019`. Mode `PRIMARY_EVIDENCE_READ`; `context_policy` SOURCE_FIRST for 39507621 and the new locators of 39416860, QUESTION_DRIVEN elsewhere (each paper below already had at least one complete earlier read, so no blind first pass was possible). Receipts are staged, not recorded. Public disease-level record; nothing here is medical advice.

## 1 · Result in one table

| PMID | Paper | Depth (staged receipt) | Manifest | What changed |
|---|---|---|---|---|
| 39507621 | Teplyshova 2024, adult WWOX-DEE case | complete | PASS | homozygous call without parental data; no metabolic or autonomic measurement; caption unit error confirmed |
| 36779245 | Oliver 2023, cohort and mortality | partial (two supplement EMF graphics unrendered) | PASS | KD started by 3 of 13, continued by 1; polygraphy channels unanalysed; Figure 1C label versus caption; Figure 4A as drawn; supplement RNA study |
| 34747138 | Repudi 2021, neonatal AAV9 gene therapy | partial (appendix S2-S6 unopened) | PASS | glucose rescue rests on Appendix S1C/D; Figure 1E below stated 60-70 percent; late deaths |
| 30755385 | Abu-Remaileh 2019, muscle Wwox | complete | PASS | GWAS support nominal; "hyperglycemia" is 78 vs 67 mg/dL; deletion developmental; two retracted citations |
| 39416860 | Feng 2024, case report | complete | PASS | assay named three ways; no cause of death; independent re-read agrees with the earlier eleven locators |
| 21075834 | O'Keefe 2011, Drosophila | partial (S1-S4 captions only) | PASS | Idh interaction significant in 2 of 5 and 3 of 5 replicates; pseudoreplicated correlation; one retracted citation |
| 34634460 | Breton 2021, slice electrophysiology | complete | PASS | supplement medians disagree with the main text; 10 mM glucose bath |
| 42422765 | Obeid 2026, neuron-specific gene therapy | partial (figures 2, 4-7 not re-opened) | PASS | glucose panels of Figures 1 and 3; manifest repaired |
| 31340538 | Tochigi 2019, lde rat cortex | partial (figures 3-6 not re-opened) | PASS | no metabolic data; liver highest; heart not quantified |
| 32581702 | Iacomino 2020, neuronal migration | partial (Table 1 numerics unanalysed) | PASS | supplement read: the one human protein test is one fetus against one control (p 0.5714) |
| 25012504 | Abu-Remaileh 2014, glucose and HIF1A | PARKED | n/a | no lawful body reachable, cascade in section 4 |
| 25403906 | Ben-Salem 2015, exon-5 deletion (never read) | PARKED | n/a | closed access, cascade in section 4 |
| 27121845 | Alkhateeb 2016, RARS2 and C10orf2 (never read) | PARKED | n/a | closed access, cascade in section 4 |
| 24871327 | Iatan 2014, HDL | PARKED for figures | n/a | text reachable, figures not |
| 30290271 | Hussain 2019, GABAergic interneurons | PARKED for figures | n/a | text reachable, figures not |

Ten readings, five parked; 15 in all. Not reached (reserve): 18974271, 17803050, 42397075 (see 6). Dossiers: `fulltext_dossiers/PMID<PMID>.md`; manifests: `deepdive_manifests/`; receipts: `receipt_staging/scientist-b/FTR-20261019-<PMID>-01.json`; commit candidates `CC-20261019-SCIENTIST-B-GOLD-CLINICAL-01`, `-GOLD-METAB-01`.

## 2 · What the brief assumed and what the ledger says

The brief expected `first_read` after a legacy reconstruction for 39507621. The ledger holds a contemporaneous complete receipt for it (`FTR-20260804-39507621-01`, after the legacy `FTR-20260726-39507621-01`), so `first_read` would be refused; the staged receipt uses `new_version_or_supplement` with the contemporaneous receipt as parent. Of 362 receipted studies only three are legacy-only (none a WWOX-direct neuro-metabolic paper); `unread_gold.py` lists 149 placeholders of which two are WWOX-direct and clinical (25403906, 27121845, both closed access). The real population of this wave was papers whose declared bytes are absent from `files/` (about 40 manifests): the lot is repair plus whatever the repair surfaces, and the yield was high exactly where the earlier supplement had been recorded unavailable (34634460, 32581702, 36779245) or where only the supplementary glucose panel carried the metabolic claim (34747138).

## 3 · What the lot, read as a set, says

1. **The WWOX metabolic phenotype has opposite signs in different tissues and one tissue of rescue.** Null: hypoglycemia (34747138, 42422765); muscle deletion: higher glucose, insulin resistance (30755385); liver and fat deletions: no fasting-glucose change; neuron-restricted re-expression rescues glucose, growth and survival. No paper separates seizure, feeding and growth from a direct central glucose role.
2. **Glucose correction does not predict survival** (42422765 Figure 1: CMV vector, glucose normal at P14, three of five animals dead by day 32).
3. **Human metabolic genetics is nominal everywhere in this batch** (best T2D variant p 3.78E-06 in 30755385; consistent with the earlier wave).
4. **No human or neural WWOX-DEE measurement of glucose, lactate, ketones, respiratory or autonomic function exists in any paper read** (adult case, 13-patient cohort, 2024 case report): the clinical papers carry hypoglycemia only as a restated mouse finding.
5. **Treatment base rate:** ketogenic diet in the 13-patient cohort: 3 starts, 1 continuation, no outcome; the adult case tried seven ASMs and no diet.
6. **Several panel-versus-text defects of the same kind recur** (Repudi Figure 1E, Oliver Figure 1C, Breton supplement versus text, Tochigi heart), which is a reason to treat extracted percentages from this literature as panel-read, not text-read.

## 4 · Parked and the cascade run

- **25012504 (Cell Death Differ 2014, PMC4211377).** PMC efetch XML is a 7.6 kB stub carrying the publisher comment that XML download is not allowed; PMC HTML served the reCAPTCHA page (no User-Agent); Europe PMC fullTextXML HTTP 500; Europe PMC PDF render 403; OpenAlex and Semantic Scholar both label it bronze OA and point to the publisher PDF URL, which returns the paywalled HTML page (cookie jar, browser User-Agent and referer tried, 320 kB HTML); the PMC open-data bucket has no key for it. The previous PDF and PPT supplement are absent and not found by SHA-256 search of the home directory (`evidence_presence.py --search/--restore`, 0 of 0). Operator wishlist: the PDF and the two supplement files.
- **25403906 (J Mol Neurosci 2015) and 27121845 (Metab Brain Dis 2016).** No PMCID; OpenAlex `closed`, Semantic Scholar `CLOSED`, Europe PMC not indexed; publisher DOI pages are paywalled. Both are never-read WWOX-direct clinical papers (the second carries the mitochondrial genes RARS2 and C10orf2); operator wishlist, high value.
- **24871327 (Circ Cardiovasc Genet 2014) and 30290271 (Neurobiol Dis 2019).** PMC efetch gives the full text but the author-manuscript figures are not served: the bucket holds only the XML and text, PMC `bin/` returns 404, Europe PMC `bin/` returns 403 and its fulltextRepo endpoint 500. A text-level reading is possible; the figure attestations of their earlier manifests cannot be re-pointed, so no PASS manifest was made. Wishlist: the author-manuscript PDFs.

## 5 · Blind locator audit (voluntary; no mandatory trigger was met)

Twelve load-bearing new triples went to two blind auditors (no dossier, no names, no conclusions; sources only). Verdicts: ten SUPPORTS, two PARTIAL, both of which were my overstatements and are corrected and declared (`contradicts_locator` with audit object) before landing: (a) 42422765 Figure 1, my "all CMV-treated animals die by about P35" is wrong, the plot ends at day 35 with 40 percent of five shown alive (possibly censored); (b) 31340538 Figure 1A, "N.D." is defined in the legend as not determined (low beta-actin), not not detected, so the text is qualified, not contradicted. One timing figure in 36779245 Figure 4A was corrected (about 8.3 years, not 9). Two auditor side-findings kept: the 34634460 supplement legend gives 126 bursts for Figure S1G against 119 elsewhere; the 30755385 supplement tables are unlabelled by trait in the text layer (the S1-1 table is read as T2D from the supplement's own caption order, which the auditor could not confirm).

## 6 · Method deviations and DEFAULTS_TAKEN

See the task contract `ledger/tasks/scientist-b/GOLD-LEGACY-WWOX-B-20261019.json`. In brief: reason `new_version_or_supplement` instead of `first_read` (validator-bound); old locators kept and re-pointed (path-only change) rather than re-captured, new locators appended; absent figure renders replaced by regenerated renders with new digests, declared in each manifest note; commits under `LEGEND_STALE_SURFACES_BECAUSE`; reserve papers 18974271 and 17803050 (no PMC for the latter) and the saturated 42397075 not attempted because the context budget of this run went to repair of the ten and the audit; 42422765 and 31340538, 32581702 are partial for figures not re-opened.
