# COMMIT CANDIDATE — CC-20261019-SCIENTISTD-DEBT-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-d` (stated assumption of the Orchestrator), task `DEBT-WWOX-DIRECT-D-20261019`, branch `task/DEBT-WWOX-DIRECT-D-20261019`, 2026-10-19.
**context_policy:** `QUESTION_DRIVEN` for seven readings, `SOURCE_FIRST` for one (named per paper in `debts_wave_20261019_scientist-d.md`). **Not medical advice.** Class-level statements only; no individual-level record.
**target_wm_version:** `WM_v7.20_2026-10-04` · **Change class:** MINOR (one annotation on one claim record, registry presence for eight papers, queue and debt entries; no status, no baseline claim and no working-model block is touched).

## 0 · Why

Wave 1 named WWOX-direct primaries it had not read: three references of the Liu 2024 oleate paper, the Lo 2015 minireview's primaries, the Carvalho 2022 references and the Sze 2015 commentary's. This candidate reports what happened when they were chased: eight papers read (four complete, four partial), fifteen parked with the cascade run. Per-paper results, manifests and staged receipts are listed in `debts_wave_20261019_scientist-d.md`; all manifests are `PASS` against the shared checkout's `files/`.

## 1 · Ops — `claim_registry_current.md` (one `replace-within`; dry run 2026-10-19 clean, one op, key `CLAIM 009`)

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 009",
  "old": "and the fractionation timing is 48 h in the figure legend against 6 h in the Methods.",
  "new": "and the fractionation timing is 48 h in the figure legend against 6 h in the Methods. **Wave note (2026-10-19, `CC-20261019-SCIENTISTD-DEBT-01`, reading debts of the WWOX-direct primaries):** the mitochondrial-localisation leg of the secondary literature this claim can lean on was traced to its primaries. Hong 2007 (PMID 17567906) has no mitochondrial measurement and points to a then-submitted paper; Lin 2011 (PMID 21901168; Jurkat cells, 10 micromolar PMA, one confocal field per time point, one siRNA experiment with borderline protection statistics) and Huang 2016 (PMID 27339895; MOLT-4 cells, a fractionation blot without a mitochondrial marker row and confocal co-localisation percentages, n = 3) each report WWOX in or leaving a mitochondrial compartment in one T-leukaemia line under a pharmacological stimulus, with overexpression or dominant-negative constructs and no Wwox-null cell. The retinal (PMID 15664696), MPP+ (PMID 18371080) and Zfra/cytochrome c (PMID 18403180) primaries and the Drosophila respiratory-complex primary (Choo 2015, PMID 26390919) are unread (subscription, no repository copy). Nothing read here measures respiration, ROS, ATP or mitophagy after WWOX loss, so the status and the INFERENZA type stand and the leg 'WWOX localises to mitochondria under stress' is carried by single-laboratory leukaemia-line observations."
 }
]
```

The same ops file is kept at the path the Orchestrator can pass to `record_scoped_edit.py apply --ops` (the JSON block above is the file).

## 2 · Registry presence proposed (placeholders; the integrator mints `PAPER` and `LIT` ids, disjoint from peers)

| Placeholder | PMID | Short title | Depth | Registry state found by `registry_records.py get --pmid` |
|---|---|---|---|---|
| D01 | 29675105 | Chen 2018, WWOX rs9926344 and HCC recurrence (J Cancer) | complete | no record |
| D02 | 17567906 | Hong 2007, Zfra, TNF and WOX1 (BMC Mol Biol) | complete | no record |
| D03 | 19366691 | Hsu 2009, TGF-beta1, Hyal-2 and WOX1 (J Biol Chem) | partial (supplement not read) | no identity record (cited by a record) |
| D04 | 29310447 | Huang 2018, WWOX phosphorylation review (Exp Biol Med) | partial (supplementary table not read) | `LIT-0069`, unprocessed corpus stub |
| D05 | 28426730 | Lee 2017, WWOX SNPs and HCC risk (PLoS One) | complete | no record |
| D06 | 21901168 | Lin 2011, MEK1/WOX1 in leukaemia T cells (Genes Cancer) | partial (supplement not read) | no identity record |
| D07 | 27339895 | Huang 2016, IkappaB-alpha/ERK/WWOX in MOLT-4 (J Biol Chem) | partial (supplement and videos not read) | corpus placeholder `CORPUS P229` |
| D08 | 34210081 | Lee 2021, WWOX gene, FRA16D and metabolism review (Cells) | complete | no record |

Receipt event ids: `FTR-20261019-<PMID>-01` for each, staged under `receipt_staging/scientist-d/` (not recorded: the ledger is hash-chained and the Orchestrator records in event-id order).

## 3 · Claim-level observations (all MINOR; none narrows or reverses a baseline claim)

- `CLAIM 009` (mitochondrial quality control, redox, energy; `in observation`, `INFERENZA`): the annotation above. The status does not move.
- The Lo 2015 minireview (read by `scientist-c`) points to Hong 2007 for Zfra and WWOX mitochondrial translocation and cytochrome c release; Hong 2007 contains neither, and cites the Hsu 2008 paper as "submitted". Whoever cites the minireview for this should cite the unread Hsu 2008 primary or say "reported by one laboratory, primary unread".
- The Huang 2018 review's metabolic sentence (null mutations in humans, mice and rats cause metabolic disorders of lipid, cholesterol and glucose) cites two reviews, an editorial and a commentary; its "conditional knockout" sentence cites the Ludes-Meyers 2009 allele paper whose animals are the germline-deleted knockout. Neither adds a human metabolic datum.
- `CLAIM 026` (WWOX co-associates with trafficking proteins): not moved. The Lee 2021 review's pathway sentence for the interactome paper is a restatement of that paper (already receipted).
- HCC SNP papers (Chen 2018, Lee 2017): no WWOX loss-of-function readout; they carry no claim in this repository.

## 4 · Reading debts: parked, with the cascade run (the operator's PDF wishlist, best value first)

Cascade run for all: PubMed identity check (`pubmed_identity_check.py`), Unpaywall, Europe PMC REST (search and full text), OpenAlex locations, CORE API, Internet Archive availability, publisher landing and PDF (curl, with and without a browser-like User-Agent), HAL, Semantic Scholar (HTTP 429, not retried in a loop). No Sci-Hub-type source was queried. No keyed publisher API was used (reserved). Where the table says "free, blocked", the publisher licence is open (Unpaywall/Crossref) but the publisher's bot challenge refuses non-browser clients: the operator can download these in a browser in a minute.

| Order | PMID | Paper | Why it matters | Route status |
|---|---|---|---|---|
| 1 | 26390919 | Choo 2015, Genes Chromosomes Cancer: WWOX moderates the mitochondrial respiratory complex | The only unread Drosophila respiratory-complex primary; cited by three read papers (Chen 2018, Huang 2016, Lee 2021) for WWOX and mitochondrial respiration; theme core | Wiley, closed; OpenAlex lists a University of Adelaide repository handle that returns 404; operator PDF or corresponding author |
| 2 | 25411445 | Mignot 2015, J Med Genet: WWOX-related encephalopathies, phenotype spectrum | One of the three unread primaries the standing brief names; human biallelic-loss clinical series | BMJ, closed; HAL record is a notice with no file; operator PDF |
| 3 | 26345274 | Tabarki 2015, Am J Med Genet A: severe CNS involvement, five new cases | Human biallelic-loss cases, MRI; a Carvalho 2022 reference | Wiley, closed; Scholar Gateway not authorised in this session |
| 4 | 15126504 | Sze 2004, J Biol Chem: WWOX down-regulation and Tau phosphorylation | The third unread primary the standing brief names; basis of the WWOX-tau line | free to read (Unpaywall hybrid), publisher bot challenge; browser download |
| 5 | 18403180 | Hsu 2008, Cell Signal: Zfra, Bcl-2 and cytochrome c | The named source for Zfra/WWOX mitochondrial co-translocation (Hong 2007 "submitted") | Elsevier, closed |
| 6 | 18371080 | Lo 2008, Eur J Neurosci: MPP+ and Tyr33 phosphorylation in rats | In vivo neuronal WWOX mitochondrial claim | Wiley, closed |
| 7 | 15664696 | Chen 2005, Neuroscience: light-induced retinal damage, Tyr33, mitochondrial translocation | The blocked row of the Lo 2015 table | Elsevier, closed |
| 8 | 41442931 | Choi 2026, Pediatr Neurol: vigabatrin-associated MRI abnormalities in two WWOX children | The VABAM anchor of `CLAIM 001`; the selection file's "read" is wrong | Elsevier, closed |
| 9 | 23765596 | Dayan 2013, Genes Chromosomes Cancer: WWOX expression and metabolic reprogramming | Drosophila/HEK293T arm of the WWOX-metabolism chain | Wiley, closed |
| 10 | 34015398 | Yang 2021, Cancer Lett: toosendanin activates WWOX in HCC | Third Liu 2024 gene-direct debt | CC-BY (Unpaywall); ScienceDirect bot challenge; browser download |
| 11 | 15548692 | Aqeilan 2004, Cancer Res: Wwox and AP-2gamma | Second Liu 2024 gene-direct debt (listed in the queue's PDF-font group) | free to read (Unpaywall bronze); AACR bot challenge; browser download |
| 12 | 22202011 | Teng 2012, Front Biosci: WWOX/WOX1 in Alzheimer pathology | Carvalho 2022 reference | closed |
| 13 | 14555208 | Chang 2003, Biochem Pharmacol: WOX1 activation | Carvalho 2022 reference (a review) | closed |
| 14 | 17142102 | Chang 2007, Trends Mol Med: WWOX candidate tumour suppressor | Carvalho 2022 reference (a review) | closed |
| 15 | 28695683 | Lin 2017, Asia Pac J Clin Oncol: WWOX SNPs and chemotherapy outcome | Chen 2018 reference | closed |

Of the Carvalho 2022 list, Huang 2018 (PMID 29310447) was read; Sze 2004, Lo 2008, Teng 2012, Tabarki 2015, Chang 2003 and Chang 2007 are in the table. Of the Sze 2015 debts, Hsu 2009 (PMID 19366691) was read; Sze 2004 and Lo 2008 are parked. The Choi 2026 anchor has no lawful body obtainable here.

## 5 · Queue entries proposed (no Scientist mints `FT` identifiers; the queue is a registry surface)

Open, readable, unread, gene-direct (priority MEDIUM unless stated), found as references of the papers read:
- 25416187 Tabarki commentary on WWOX and the developing brain (PMC author manuscript; a Huang 2018 reference); 19918364 Li 2009 sciatic-nerve WWOX (PLoS One; Lo 2015 and Lin 2011 reference); 19484134 Hong 2009 C1q and WWOX (PLoS One); 27999774 Hsu 2016 Hyal-2/WWOX/Smad4 review; 15266310 Park 2004 WWOX loss in HCC; 27655721 Kozak-sequence variant series; 16219768, 12514174, 11058590, 15629131 and 15580310 Chang-laboratory primaries (the first three each cited by at least two read papers); 22484428 WWOX and the mitochondrial pathway in A549 cells (Spandidos, free to read; not fetched here).
- Resume: 26302329 O'Keefe 2015 (partial receipt in the ledger; open access; WWOX elimination of tumorigenic cells in Drosophila, ROS).

## 6 · Staged leads (not appended to the discovery ledger: one shared file, the Orchestrator appends); all `IPOTESI`

1. **Antibody specificity for the pS14 model.** The Ser14 phosphorylation work (Huang 2016, Huang 2018) uses laboratory-made phospho-site antibodies; blot them on a WWOX-null lysate. Falsifier: bands persist in the null.
2. **Drosophila-style enhancement in mammalian cells.** Test whether WWOX-null cells are more sensitive to a respiratory-chain inhibitor than matched controls at equal passage (the Choo 2015 design transposed). Falsifier: no differential sensitivity.
3. **eQTL allele orientation.** Resolve whether the GTEx "Alt" allele of rs12918952 is the rare A allele of the Taiwanese series (the class sizes imply a 54 percent alternate allele frequency against 5 percent in the controls). Falsifier: they are different alleles and the eQTL trend says nothing about the studied variant.
4. **Mitochondrial purity controls for WWOX fractions.** Re-run the MOLT-4 and Jurkat fractionations with a mitochondrial matrix and a cytosolic marker row and a protease-protection step. Falsifier: WWOX is a cytosolic contaminant of the mitochondrial pellet.

## 7 · Shared surfaces left to the Orchestrator

`pathograph`, `batch_queue`, `coverage_report` and `reading_state` were not regenerated (inputs in flight from three peers; the commits carry `LEGEND_STALE_SURFACES_BECAUSE`).

### LOCATOR TRIPLES FOR BLIND AUDIT
Eight load-bearing triples were audited blind by a separate agent holding only the triples and the source files: six SUPPORTED, one UNDERSHOOT, one OVERSHOOT; the overshoot (Lee 2021, region versus gene) was narrowed in the manifest with a declared `contradicts_locator`. Detail in `debts_wave_20261019_scientist-d.md`, section "Blind audit".
