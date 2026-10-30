# P3-20 AT9283 (artefact control; Q6, arm "opposes", edge AURKB -> MYC +1)

Decision: **REFERENCE-ONLY, artefact CONFIRMED.** Pre-registered test (more than 5 signed targets with a ChEMBL value of 1 micromolar or less): **93 human targets** carry an "=" IC50, Ki or Kd of 1,000 nM or less (`measures_by_target_type.tsv`; value types and assay formats mixed, listed only to count targets, not compared). AURKB is not the leading target: AURKB IC50 2.7 nM and Kd 17 nM, against JAK2 IC50 1 nM (Kd 3.3), JAK3 1 (Kd 6.6), GSK3B 1 (Kd 7), RET 1, FGFR2 1, FLT4 1, TYK2 1, AURKA 3, ABL1 4. The MYC effect of such a compound cannot be attributed to AURKB; two of its sub-10 nM targets, GSK3B and JAK2, are themselves Wnt/MYC regulators in the seed paper's discussion (GSK3B) and in cytokine signalling. The catalogue's "14 signed targets" is the curated count; the measured count is larger.

* Identity: CHEMBL495727 (AT-9283), InChIKey LOLPPWBBNUVNQZ-UHFFFAOYSA-N; PubChem by name and key agree; **VERIFIED**. A second child record CHEMBL496311 sits in the family without a name.
* Curated ChEMBL mechanisms: Aurora A and B, ABL, FLT3, JAK2, JAK3 inhibitor (6 rows).
* Human data (abstracts): phase 1 in children and adolescents with solid tumours, 72-h infusion, maximum tolerated dose 18.5 mg/m2/day, haematological toxicity, half-life 4.9 h in children versus 8.4 h in adults, one CNS-PNET partial response (PMID 25370467); phase 1/2 in paediatric acute leukaemia terminated early, tolerable, no clinical responses (PMID 27905678); population model in 39 children and 53 adults (PMID 28177130). CSF or brain levels: not retrieved. Not a medicine; no label.
* Trials (2026-10-30): 5 studies, all haematological or solid-tumour, 2 paediatric; epilepsy, neurodevelopment, WWOX, CNS tumour all 0.
* Edge: as defosbarasertib (single T-ALL record); not attributable to AURKB for this compound.
* Use: negative control for any Aurora B experiment (pan-kinase), never a candidate.
