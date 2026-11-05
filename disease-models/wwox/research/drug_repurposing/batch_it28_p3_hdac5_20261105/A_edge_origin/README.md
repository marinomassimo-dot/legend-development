# IT28 P3-A: where the edge HDAC5 -T(+)-> SLC2A1 comes from, and what the source shows

Question (IT27 P7, H1): does the generator's edge reflect HDAC5 catalytic activity, abundance, localisation or scaffold function, and does it transfer to neural cells?

**Headline.** The edge is encoded correctly as to gene (SLC2A1, i.e. GLUT1, not SLC2A4) and sign (positive: lowering HDAC5 lowers SLC2A1), but only at abstract level. Its single origin is one sentence of one muscle paper (PMID 22991226) in which GLUT1 is the secondary, opposite-direction finding. The paper's own message is that HDAC5 *represses* GLUT4 (SLC2A4). The full text of that paper could not be obtained by any free route, so the perturbation method, readout level and controls for the GLUT1 change are **not determinable** here. Nothing in the abstract addresses catalytic activity, localisation or scaffold function.

## 1. Where the edge sits in the repo (provenance)

* Edge data used by the generator: `network_comparison_it7_p3_20261029/inputs/collectri_omnipath_edges.tsv.gz` (read by `generation_it10_p1_20261031/engine_v4/seed_engine_v4.py`, function `read_edges4`, files `signor_omnipath_edges.tsv.gz` and `collectri_omnipath_edges.tsv.gz`). Rows found (columns source, target, sign, type, sources):
  * `HDAC5  SLC2A1  1  transcriptional  CollecTRI;TRRUST_CollecTRI;CollecTRI2;ExTRI2_CollecTRI2;TRRUST_CollecTRI2;TRRUST`
  * `HDAC5  SLC2A4  -1 transcriptional  (same six resource tags)`
  * The SIGNOR file has no HDAC5 -> SLC2A row.
* The shipped TSV carries no reference column (the OmniPath query asked for references, the stored file dropped them; `fetch_log.json`). The reference was recovered in IT21: `qualification_it21_p4a_20261103/edge_records_omnipath.tsv`, row `HDAC5>SLC2A1  transcriptional  ... TRRUST:22991226;CollecTRI2:22991226;CollecTRI:22991226` (three tags, one PMID); also `edge_provenance_it21_p4a.tsv` (ID IT21P2-0006, "1 distinct reference", grade WEAK) and `generation_it21_p2_20261103/results/edge_ref_screen/edge_screen_quotes_p4a6.tsv`.
* The three resource tags (TRRUST, CollecTRI, CollecTRI2/ExTRI2) are aggregators of the same citation: one origin, not three. TRRUST is a text-mining plus curation resource; this is a resource-level fact I did not verify here and is background.
* Gene check: both the SLC2A1 (sign +1) and the SLC2A4 (sign -1) rows exist side by side, as the abstract would predict (knockdown lowers GLUT1, raises GLUT4). That the SLC2A4 row cites the same PMID is likely but **not shown in the repo**: the references were stored only for the chosen edges.

## 2. The original paper

Raichur S, Teh SH, Ohwaki K, Gaur V, Long YC, Hargreaves M, McGee SL, Kusunoki J. "Histone deacetylase 5 regulates glucose uptake and insulin action in muscle cells." J Mol Endocrinol 2012;49(3):203-211. PMID 22991226, DOI 10.1530/JME-12-0095. Lilly Singapore Centre for Drug Discovery with the McGee/Hargreaves muscle groups. Not in PMC, not in Europe PMC full text (inPMC N).

**Reading depth: abstract only (PubMed record, served 2026-11-05 through the PubMed connector).** Routes tried for full text: PMC/Europe PMC (absent); OpenAlex lists a "bronze" publisher PDF, a plain request returned HTTP 403; the university repository copy returned HTTP 401 (restricted). I did not try to circumvent either (an attempt with a browser-style client identity was blocked by the session's guard and not repeated). Unpaywall was not used (it requires an e-mail address, which must never be sent).

Decisive passages (verbatim, Abstract):

* Perturbation, cell type, direction: "Knockdown of HDAC5 in human primary muscle cells increased glucose uptake and was associated with increased GLUT4 (SLC2A4) expression and promoter activity but was associated with reduced GLUT1 (SLC2A1) expression."
* No effect on one comparator: "There was no change in PGC-1α (PPARGC1A) expression."
* Timing control: "The effects of HDAC5 knockdown on glucose metabolism were not due to alterations in the initiation of differentiation, as knockdown of HDAC5 after the onset of differentiation also resulted in increased glucose uptake and insulin-stimulated glycogen synthesis."
* Pharmacology: "we also examined the effects of the pan HDAC inhibitor, Scriptaid, on muscle cell metabolism. In myotubes, Scriptaid increased histone 3 acetylation, GLUT4 expression, glucose uptake and both oxidative and non-oxidative metabolic flux." (Nothing is said about GLUT1 under Scriptaid.)
* Framing: "The class IIa histone deacetylases (HDACs) act as transcriptional repressors by altering chromatin structure through histone deacetylation."

### Answers to the sub-questions

| Question | What the abstract supports | Status |
|---|---|---|
| Perturbation that sustained the SLC2A1 sign | Knockdown of HDAC5 (method, siRNA versus shRNA, number of oligos and rescue: not stated). No knockout, overexpression, catalytic-dead mutant or drug result is reported for GLUT1 | Narrowed to "knockdown only, method undetermined" |
| What was measured | "expression" of GLUT1; level (mRNA or protein) not stated. Promoter activity was reported for GLUT4 only | Undetermined (full text needed) |
| Function (catalytic, localisation, MEF2 binding) | Not addressed in the abstract; no rescue, no localisation, no MEF2 data | Not determinable; the edge cannot be assigned to catalytic activity, abundance or scaffold function |
| Cell type and species | Human primary skeletal muscle cells (myoblast/myotube states both mentioned); Scriptaid in "myotubes" (species not stated in the abstract) | Confirmed: non-neural, muscle |
| Controls | Not visible; PGC-1α unchanged; knockdown repeated after onset of differentiation | Undetermined |
| Sign and gene identity as encoded | Knockdown lowers GLUT1 = HDAC5 positive for SLC2A1: sign and gene match. Not SLC2A4 (that is the opposite-sign, main finding) | Confirmed as encoded, at abstract level |

### What the edge means, and what it does not

* The paper's central observation is repression of SLC2A4 by HDAC5, as a class IIa repressor. A *positive* HDAC5 effect on SLC2A1 is the opposite of the repressor model and was only "associated with" the knockdown. A direct transcriptional action of HDAC5 on the SLC2A1 promoter is therefore **not shown**; an indirect or compensatory effect (for example a reduction of GLUT1 when GLUT4 and glucose uptake rise) is a possible reading, flagged as a hypothesis of mine with no support in the text read. The edge label "transcriptional" (CollecTRI/TRRUST) over-states what a knockdown with an expression readout shows.
* No drug evidence for SLC2A1 exists in the abstract: the one inhibitor tested (Scriptaid, pan-HDAC) is reported to raise GLUT4, and its effect on GLUT1 is not stated. So the step "an HDAC5 inhibitor lowers SLC2A1" is not supported by this source even in muscle.
* Transfer to neural cells: untested here. The repo's own P47T and organoid data go the other way (HDAC5 0.81x with SLC2A1 2.67x in the KO organoid; `qualification_it21_p4a_20261103/edge_provenance_it21_p4a.tsv`), which is association, not a test.

## 3. Papers that republish the observation (not independent)

* TRRUST, CollecTRI, CollecTRI2/ExTRI2: the same single citation (above).
* The 2023 review PMID 37006625 (PMC10050567, read in part) restates Raichur 2012 as: "HDAC5 inhibits the expression of Glut4 and Baf60c, thereby influencing muscle glucose uptake (Raichur et al., 2012; Meng et al., 2017)." It does not mention GLUT1. A secondary source; independent confirmation of nothing. It also records catalytic-site mutants of HDAC4/5 that cannot bind SMRT/NCoR yet induce MEF2 activity (Gaur et al., 2016): relevant to sub-question B, not tested on GLUT1.
* PMID 32771698 (PMC7481569, read in part; Mol Metab 2020, HDAC5 and IL-6 in muscle, mouse KO and C2C12 knockdown) is the same research tradition and cites the GLUT4 finding: "Several studies highlighted the role of ... HDAC5 ... as a negative transcriptional regulator of GLUT4 in the skeletal muscle". The words GLUT1 and Slc2a1 occur nowhere in its text (count 0). It adds an independent GLUT4 observation (higher H3K9ac at the Slc2a4 promoter in knockdown myotubes) and **does not test or replicate the GLUT1 result**.
* Europe PMC lists 36 citing items of 22991226 (list retrieved 2026-11-05); I did not read them beyond titles. Titles suggest GLUT4/exercise (for example PMID 28688716, exercise-induced Glut4 transcription via HDAC4/5 inactivation in mouse muscle) rather than GLUT1; not verified, so absence of a second GLUT1 report is "none found in the titles and the two papers read", not a proven absence.

## 4. Consequence for the IT27 H1 rationale

* **Confirmed:** gene identity (SLC2A1/GLUT1) and sign (HDAC5 knockdown lowers it) are what the abstract says; the edge has exactly one experimental origin, in human primary muscle cells.
* **Narrowed:** the origin is a single knockdown observation reported as secondary and "associated with"; no catalytic, localisation or scaffold dissection; no drug result on GLUT1; the paper's headline is repression of GLUT4. The compound arm (inhibitor lowers SLC2A1) has no support from this source.
* **Refuted:** nothing is refuted outright. The reading "HDAC5 transcriptionally drives SLC2A1, so inhibiting HDAC5 lowers it" is not what the paper establishes; it is a knockdown correlate.
* **Not determinable without the full text:** knockdown method and efficiency, mRNA versus protein, magnitude, statistics, number of donors, controls, whether Scriptaid changed GLUT1, whether any promoter or ChIP work touched SLC2A1. A manual PDF is needed (publisher or inter-library route); the integrator should treat this as a queued item.
* The genetic arm already proposed in H1 (HDAC5 knockdown in hNPC/neurons reading SLC2A1) is exactly the experiment this paper did in muscle; it stays the right first step, with the catalytic-dead rescue as its discriminating element.

## Files

* `README.md` (this file).
* `receipts/FTR-20261105-22991226-04.json` (abstract only), `receipts/FTR-20261105-32771698-04.json` and `receipts/FTR-20261105-37006625-04.json` (partial full text, PMC E-utilities). All pass `framework/scripts/staged_receipt_check.py`; not recorded in the ledger.
