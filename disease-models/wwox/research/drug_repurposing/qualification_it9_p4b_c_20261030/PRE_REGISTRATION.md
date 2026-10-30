# Pre-registration, IT9 P4b-c (written 2026-10-30 before any fetch of the 7 compounds)

Scientist-d3. Compounds: harmine, pomalidomide, defosbarasertib, pinometostat, sirolimus (reference), lenalidomide and AT9283 (artefact controls). Not medical advice.

Decision criteria, fixed now (they apply to the evidence found, whichever way it falls):

* **Identity** is VERIFIED only if the ChEMBL standard InChIKey equals the PubChem record retrieved by InChIKey and the PubChem record retrieved by name carries the same key (or the same 14-character skeleton block with the difference stated). Otherwise it stays UNVERIFIED.
* **Target engagement measures** are kept per target, assay type (B/F/A), species, standard type, relation and units. No value is pooled across types or units; a ratio is formed only between rows of one ChEMBL document on one standard type, both relation "=".
* **Selectivity** (harmine, DYRK1A against MAO-A): reported as same-document ratios where both exist; otherwise "ranges by target, not comparable".
* **Edge plausibility** is judged from the underlying record only (OmniPath/SIGNOR record, its references opened at abstract level at least). An edge is called a **context-free artefact** if (a) its only support is text mining (ProtMapper family) or a non-neural, cancer-line or in-vitro kinase assay, AND (b) its sign refers to a different quantity from the seed (protein stability or phosphorylation versus transcript level). It is called **plausible in neural cells** only if a reference measures it in neural or neural-progenitor cells.
* **Artefact controls** (lenalidomide, AT9283) are confirmed as artefacts if the proposal reaches the seed through a mechanism that the compound does not use (lenalidomide) or through a target set so wide that the MYC edge cannot be attributed (AT9283: more than 5 signed targets with activity under 1 micromolar in ChEMBL). Otherwise they are reported as "not confirmed as artefact".
* **Seed strength** for generating candidates is judged on: number of independent systems showing the direction; number of measurement levels; whether the readout is a within-cell-type contrast; whether the causal link from the seed to a phenotype is tested by a specific (not multi-kinase) intervention; whether the sign of benefit is established. Verdict scale: STRONG / MODERATE / WEAK-DIRECTION-ONLY / INSUFFICIENT.
* Decisions: DROP only with a decisive datum named; KEEP-AS-PROPOSAL only with experiment, readout, control, falsifier; REFERENCE-ONLY for controls and the sirolimus reference; INCONCLUSIVE names the exact missing datum.
* Trials: ClinicalTrials.gov API v2, queries and counts logged with date; a zero is "no hits in this query on this date".
