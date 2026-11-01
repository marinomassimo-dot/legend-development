# IT15 P4: daily-radar signal PMID 42941930 and a public-data reopen check

Scientist package P4, task IT15, 2026-11-01 (Europe/Rome). Research layer, exploratory, non-canonical. Not medical advice. Reference genotype class only. Nothing recorded in any ledger or registry; no spend, no contact, no e-mail or personal data sent anywhere; no access control circumvented.

## 1. Verdict in one paragraph

PMID 42941930 is a genuine, open-access (CC BY), peer-reviewed paper, but an SH-SY5Y respiratory-inhibitor study; it is NOT a WWOX model and not WWOX evidence by analogy. It adds no datum to any open WWOX question. Its only reusable element is an assay-design precedent (positional 13C-glucose NMR plus PC/PDH capacity assays on the same extracts). CLOSED as "context only, no decision change". No full-text receipt prepared (no decision rests on it). Strand B: no documented reopen condition has changed on a public-data basis today; motivated exclusion (section 5).

## 2. Identity (PubMed via the PubMed tool; Europe PMC REST core record)

| Field | Value | Source |
|---|---|---|
| PMID / PMCID / DOI | 42941930 / PMC13705396 / 10.3390/ijms27209160 | PubMed metadata; Europe PMC `search?query=EXT_ID:42941930` |
| Title | Distinct Post-Exposure Metabolic States Following Pharmacological Perturbation of Mitochondrial Respiratory Complexes I-V in SH-SY5Y Cells: A Positional 13C-NMR Study | same |
| Authors | Hong Li (Rutgers NJMS, Newark); Ahmet Tarik Baykal (Acibadem University, Istanbul) | PubMed authors list |
| Journal | Int J Mol Sci 27(20):9160, issue date 2026 Oct; first publication 2026-10-15 | Europe PMC `firstPublicationDate`, `journalInfo` |
| Preprint relation | none indicated in the Europe PMC core record (no preprint link field populated); not searched further | Europe PMC |
| Radar match | the radar item (`Discovery:pdh-assay`, key `epmc:MED:42941930`, venue Int J Mol Sci, open Y) matches this record | `~/.local/state/legend/scout_daily.json` |

The radar flagged it only because a search for a PDH-specific measure matched "pyruvate dehydrogenase"; the radar itself states "a search hit is the first look (no relevance scoring)".

## 3. Access and licence

* Europe PMC: `isOpenAccess=Y`, `license=cc by`, `inEPMC=Y`; the XML front matter states "Creative Commons Attribution (CC BY) license", copyright 2026 by the authors, MDPI (full-text XML, fetched key-less from Europe PMC REST, locator: article-meta licence block). Reuse with attribution is allowed.
* Data availability (XML section "Data Availability Statement", verbatim): "The per-replicate 13C integral table underlying Table 1, Figure 2 and Supplementary Table S1, together with the analysis script that reproduces the ANOVA, Dunnett contrasts, effect sizes, principal component analysis and PERMANOVA reported here, are provided as Supplementary Data. Raw NMR free induction decays are available from the corresponding author on reasonable request. No other datasets were generated or analysed." No repository accession (no MetaboLights/Metabolomics Workbench deposit); raw FIDs only on request (not requested: contact barred).
* Supplementary file sizes: NOT verified. The publisher URL (mdpi.com `/s1`) returned HTTP 403; the Europe PMC `supplementaryFiles` endpoint returned a truncated or non-zip stream within the time limits in two attempts (528,384 and 53,248 bytes, neither a valid zip). Nothing was added to the shared corpus.
* Funding: "received no external funding"; conflicts: none declared.

## 4. What it measures (from the open full text; all numbers from the PubMed abstract unless a section is named)

* System: undifferentiated SH-SY5Y; five single compounds, one per complex: MPTP (I), 3-nitropropionic acid (II), antimycin A (III), sodium azide (IV), oligomycin (V), each titrated to about 80 percent viability (24 h; 3-NP 12 h); inhibitors washed out, then 24 h [U-13C6]glucose. Concentrations in the text include 1 mM MPTP, 2 mM azide, antimycin A 4 ug/mL (~7.3 uM), oligomycin 1 ug/mL (~1.27 uM).
* Readouts: positional 13C-NMR of intracellular extracts (800 MHz Bruker; 25 C; Section 4.4), medium 13C (Table 3, normalisation "not fully specified" by the authors' own words), and PC and PDH enzyme-capacity assays in parallel extracts (Sections 4.6, 4.7). PDH assay: citrate-synthase-coupled, CoA released titrated with DTNB at 412 nm, extract-level, "activities are expressed relative to control" (no absolute units).
* Replicates and statistics: n = 3 biological replicates per group, six groups, one shared vehicle control; log2 values, one-way ANOVA with Dunnett (error df 12), Hedges' g, PERMANOVA pseudo-F 18.77, p = 0.0001; PCA on 7 complete-case metabolites (PC1 65.9 percent, PC2 19.3 percent).
* Key results: oligomycin glutamate C4 (PDH-associated) 107.2 percent of control (p = 0.971), glutamate C3 (PC-associated) 197.7 percent (p = 0.004), PC capacity about 138 percent (p < 0.01), PDH capacity about 60 percent; azide glutamate C4 31.9 percent (p < 0.001), lactate C3 19.4 percent; 3-NP gives 13C-succinate absent in control; MPTP weakest (most comparisons do not survive the shared-control analysis).
* Authors' own limits (Section 3.11 and Methods): no OCR, ATP, membrane potential, NAD+/NADH, ROS or complex activities measured, so respiratory inhibition is inferred, not shown; one compound per node; compounds not selective; "capacity not flux"; "compound-defined post-exposure metabolic states and not measurements of complex-specific flux"; the lactate/NADH reading is explicitly "not independent mechanistic evidence for a redox interpretation".

## 5. What it is and is not for LEGEND

* NOT a WWOX model: no WWOX perturbation, no WWOX measurement, a neuroblastoma line with pharmacological, washed-out toxin exposure. It cannot support or refute any WWOX statement, even by analogy (rule: a model system is not WWOX evidence by analogy).
* Duplication check against the module (grep and README sections): PDH, lactate and Complex I questions are already worked at literature and design level in `complex_i_ldh_pdh_it3_20261027.md`, cards E02/E03/E04/I01, the P1 subnetwork (glycolysis/PDH/lactate; WWOX-deficient systems), the p2b PDH trace (PMID 35328751 "PDH activity unchanged" neither confirmed nor refuted), and `census_reconciliation_it7_20261029.md` (no deposited flux/metabolite record for a WWOX-deficient neural system; MTBLS12344 unreleased). No SH-SY5Y or 13C-glucose NMR work exists in the module (grep of SH-SY5Y and isotope terms hits only unrelated cards and tables). So the paper duplicates nothing and answers nothing already open.
* What it could still inform (assay design only, hypothesis-grade): (a) a template for how to ask "is glucose carbon entering the TCA cycle through PDH or PC" in a future WWOX-deficient neural culture: glutamate C4 (PDH-associated) versus C3 (PC-associated) from [U-13C6]glucose, with extract-level PDH/PC capacity measured on the same replicates; (b) its own caveat is the useful part: capacity assays do not report phosphorylation state or in-cell flux, so they would not answer the module's closing condition for card I01 (PDH-phosphorylation genotype-by-inhibitor interaction); (c) an inhibitor-washout design shows that post-exposure states differ by node, which warns that a "complex I defect" label (Bouchez-type pharmacology in the module) should not be generalised across nodes. None of this changes a need, card, trigger or ranking.
* Not a dataset for reuse: n = 3, relative-to-control capacity values, one cell line, raw data on request only.

## 6. Strand B: reopen check on public data (checked 2026-11-01, key-less GETs only)

Triggers with a public-data condition were each tested at source. Full table: `reopen_check_it15_p4.tsv`.

* GEO (E-utilities, db=gds): query for WWOX/WOREE/SCAR12/full name returns 303 GSE-type records after de-duplication of series; the newest neural series are GSE158681/82/84/85 (listed with pdat 2026/10/01, already in the module since IT6/IT7: P4 mouse P17, census row 12). Of the 303, 18 series are not mentioned anywhere in `disease-models` or `framework`; none is a WWOX-deficient neural or metabolic dataset (cancer, osteosarcoma, EMT, SNP arrays, nanoparticles, population cohorts). No series with a date after 2026-10-15 exists (MDAT window 2026/09/15 to 2026/11/02 returned 0).
* GSE158684 raw reads (NP3A1): GEO lists SRP285669, but SRA experiment SRX9206272 still returns "is not public" (status `hup`; efetch error) and ENA has no read_run rows for PRJNA666185. Unchanged.
* E-MTAB-14792 (NP3B2): BioStudies `Study not accessible`. Unchanged. MTBLS12344: ws returns 401 "User has no permission". Unchanged (as also recorded by the radar watch).
* ChEMBL (NP1B4): REST `status.json` and `molecule/CHEMBL25.json` return HTTP 500. Condition not met; scripted retry still pending.
* Radar's other items: BRAT1 variant paper (PMID 42930560; different gene, "residual-function chaperone" theme hit only), ToolUniverse v1.5.7 to v1.5.8 (tool release, triage-only), SigCom-LINCS etag and openFDA NDC date changes (mirror/version bumps, no content reading). PubMed WWOX queries returned no new PMIDs.

Decision (strand B): NO trigger is reopened. This is a motivated exclusion, not a negative finding: unknown is not negative; every condition stays NEEDS-DATUM. PDH, HIF, ISR and glia are not reopened (no new element). Suggested next check date for the cheap scripted retries: the next daily radar run (ChEMBL status, SRX9206272 status, E-MTAB-14792, MTBLS12344).

## 7. For the integrator

* No receipt JSON prepared: the full text is open and was read for this triage, but no module decision depends on it; recording a read would add a countable PAPER with no decision behind it. If the integrator wants it on file, it is a "triage read, not a reading of record".
* Triggers: no change. Optional: add a row to the radar disposition (PMID 42941930: CLOSED, context only) and a note on the `pdh-assay` radar theme that an Europe PMC hit on "pyruvate dehydrogenase" finds non-WWOX metabolic papers.
* Could not verify: supplementary file sizes and content; preprint relation beyond the Europe PMC record; whether any SRA read data exist beyond the `hup` status; raw FIDs.
