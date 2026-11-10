# IT42 P3 — onfasprodil and NP10679: provenance, roles and what moves them

Non-canonical working note. Not medical advice; no dose, schedule or route. Opportunities for verification, not winners. The primary-source deepening belongs to the science session (SCI42, `glun2b_comparators_sci42_20261110/`); nothing here anticipates its result. Abstract-level reads below were made with the PubMed tools and are not readings.

## Provenance (how each reached the comparison)

| Step | onfasprodil | NP10679 |
|---|---|---|
| Relation that produced it | S1, negative modulation of GluN2B-containing receptors (IT41, fixed in `cases.md` before the search) | same |
| Data already in the repository before IT41 | IT15 target-first relations table (`target_first_it15_qa_nmdar_20261101/relations_qa.tsv`): a ChEMBL activity row (molecule CHEMBL5095074, GRIN1/GRIN2B record, IC50 8.3 nM, human, reference field 27475601), a GtoPdb row (negative, pIC50, `value_nM` 8.3176) and a DGIdb row; also the coverage matrix. Never discussed as a comparator. | the same table: a GtoPdb row (inhibition, `value_nM` 22.9, PMID 34493631) and a raw DGIdb listing under the spelling NP-10679 in `gse156243/kg_lookup/GRIN2A.txt` (not in the same table) |
| Step that brought it into the comparison | `action_search.py` over the GtoPdb interaction table: row type "Allosteric modulator", action "Negative", GluN2B, human; receptor site not recorded | same table: row "Inhibition", GluN2B, human, assay text "at pH 6.9" |
| Qualification verdict (engine) | CANDIDATE with `unknown_fields: receptor_site` | CANDIDATE with `unknown_fields: receptor_site` (assay text present, site not recorded) |
| Identity (Harness) | catalogue record present; table row added in HE42 (CHEMBL5095074); the identity route is Harness's | CHEMBL5095254; same |

## Two corrections this reconstruction forces

* **One datum, three representations.** The IT15 table's `value_nM` of the GtoPdb row (8.3176 nM for onfasprodil; 22.9 nM for NP10679) is the nanomolar form of the GtoPdb pIC50 (10^(9 − 8.08) = 8.32; 10^(9 − 7.64) = 22.9) although the row's `measure_type` says pIC50; the ChEMBL activity row (IC50 8.3 nM) is the same magnitude. Potency and its logarithmic transform are the same datum and must be counted once; whether the ChEMBL and GtoPdb rows are one measurement or two independent ones is for the science session (question O5) to settle from the primary source.
* **An activity identifier is not a PMID.** In the IT15 table the number 27475601 of that ChEMBL activity row is the `activity_id` column (the row's references are ChEMBL document ids); read as a PubMed id it resolves to an unrelated paper (a displacement sensor for spindle metrology). It is a registry identifier and is not to be followed as a PubMed id.

## What the abstracts say (abstract level only)

* onfasprodil (MIJ821): a selective NR2B negative allosteric modulator; a phase 2 study in adults with treatment-resistant depression (PMID 40767837).
* NP10679: a series of GluN2B-selective negative allosteric modulators "with enhanced potency at acidic pH" relative to physiological pH, which the authors relate to ischaemic penumbra and high-frequency synapses; oral bioavailability and brain penetration are claimed for the clinical candidate NP10679 (PMID 34493631); a phase 1 study in healthy volunteers (PMID 36642931). So the pH dependence is stated for this series; the abstracts do not say whether it extends to other ifenprodil-site modulators.

## Roles (from the rationale, not from the catalogue label)

| | Role now | Why |
|---|---|---|
| onfasprodil | **mechanism comparator under verification** (not a therapeutic candidate; not yet a same-site control) | a GluN2B negative modulator with human exposure; its site and maximum effect are not read; a *different* site would make it a different, equally useful comparison (site-separating), the same site a chemotype control; the rationale decides |
| NP10679 | **probe of experimental conditions** (bath pH), not a candidate | its potency depends on pH by design; it shows that every GluN2B-directed arm must state and match pH; promoting it would confuse relevance of pH with relevance of the molecule to the burst |
| neither | not "composto non qualificabile" in the strict sense: both have identity rows and a stated action; what is missing is site, maximum effect and selectivity read at source |

## Open premise and what changes the priority

| | Open premise | Raises priority | Lowers priority | Leaves unresolved |
|---|---|---|---|---|
| onfasprodil | it acts on GluN2B in the preparation as in oocytes; the site is known | primary source: a documented site and a maximum on triheteromers that differs from ifenprodil's (different ceiling at the same site, or a different site) | same site and a similar ceiling (adds a chemotype only) | no primary source |
| NP10679 | pH dependence matters at the slice pH | evidence that the class effect at pH 6.9–7.4 is large enough to change a burst-level reading | a dependence specific to the molecule and small near the slice pH | no slice data |

## Where it is consumed

`compound_view.tsv` items V06 and V07 (research order 7 and 8, kinds "emerged"), the public page (both editions, names only in the full one), `comparisons_it41.md` (how a result moves the alternative), INV-05 `feasibility` ([IT41]). After the science delivery the deltas are applied to these consumers; if no choice changes, that is stated.
