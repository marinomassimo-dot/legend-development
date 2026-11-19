# ADV-098 batch 2: Kv7 (ezogabine/retigabine, azetukalner/XEN1101, ICA-069673, XE991) (HE, 2026-11-19)

Written for: SCI (unit B), ADV, IT. Same rules and routes as batch 1 (see its header): public sources only, research concentrations apart from any patient dosing, no dose, hypothesis level, not medical advice, a missing value is "not found by these routes". Identity and tabulation recipe in `RECIPE_pull_activities.txt` (batch 2 additions at its end); raw ChEMBL answers outside git with digests in `SHA256SUMS_raw_activities.txt`.

## COMPARABLE? (which pairs can be set side by side, and the condition that decides each number)
- **Ezogabine across documents: not comparable as one potency.** On human Kv7.2/Kv7.3 the EC50 is 0.43 microM (Rb+ efflux, CHO, atomic absorption, 2011), 4.38 microM (thallium flux FLIPR, HEK293, 2019), 1.72 microM (whole-cell patch clamp, CHO, 2020), 1.84 microM (HEK293, 2023), 2.5 microM (leftward shift of the activation curve at +80 mV, 2022) and 11.2 microM (fluorescence slope, 2022): a 26-fold spread in one agent, set by readout (efflux, flux, current amplitude, voltage shift), cell line and temperature, not by the receptor. Only one document (CHEMBL4402547, J Med Chem 2020, whole-cell patch clamp, CHO, one protocol) gives ezogabine on Kv7.2 0.93, Kv7.3 3.9, Kv7.4 1.98 and Kv7.5 0.80 microM together: **within that document** the subunits can be compared; across documents not.
- **Ezogabine against ICA-069673: same assay type, different documents.** ICA-069673 KCNQ2/KCNQ3 EC50 0.69 microM (86Rb+ efflux, CHO, ACS Med Chem Lett 2011, document CHEMBL2046284) and ezogabine 0.43 microM (86Rb+ efflux, CHO, Eur J Med Chem 2011, document CHEMBL1687897): comparable in kind, not in one experiment; the 1.6-fold difference is inside the assay-to-assay spread above, so **no ordering is read**. ICA-069673 on KCNQ3/KCNQ5 EC50 14.3 microM and KCNQ1/minK IC50 above 100 microM (same document): subtype contrast within one document is comparable.
- **Azetukalner: not comparable.** One row only: KCNQ2 EC50 98 nM in a FluxOR thallium assay in CHO cells, from a **patent** document (CHEMBL5729159, 2022), no ezogabine value in the same document. A FluxOR value against ezogabine's Rb+ efflux or patch values is a cross-readout comparison: not made.
- **XE991: not comparable with the openers.** A blocker (IC50 55 nM at Kv7.2, thallium flux, HEK293, 2019) and a rat hippocampal acetylcholine-release EC50 450 nM (1998); an IC50 of a blocker and an EC50 of an opener are different quantities.
- **Species:** rat Kv7.2 EC50 for ezogabine 2.04 to 2.17 microM and mouse Kv7.2 1.3 microM, human Kv7.2 0.93 to 4.2 microM: the species difference is not separable from the assay difference.

## Ezogabine (= retigabine; ChEMBL CHEMBL41355, SYNONYM_EXACT for retigabine; CHEMBL4588394 is a separate record not merged)
- **Targets and potency:** the values above (KCNQ2 to KCNQ5 recombinant, human, mouse, rat). 32 activity rows; 13 on KCNQ symbols by gene; 11 other targets (not selectivity).
- **Mouse in vivo exposure as an efficacy readout (ChEMBL):** in the Kunming-mouse maximal electroshock model the EC50 is 2.23 microM in brain (20.0 microM in plasma) and in the rotarod test 27.3 microM in brain (141 microM in plasma), document CHEMBL5149984 (J Med Chem 2021, the HN37 paper, ezogabine as comparator). **Origin note for SCI:** your delegate's 3.58 microM brain EC50 in adult MES is a different number; the Xenon PK/PD paper (PMID 40806162, 2025, mice and rats, retigabine among six drugs) is a second primary origin for MES brain and plasma EC50 and is not the HN37 paper; I did not read either full text, so I cannot say whether 2.23 and 3.58 are the same experiment; they are two documents.
- **Rodent exposure (PubMed), juvenile:** P7 rat pups, 5 to 30 mg/kg: plasma half-life 2.5 hours, brain concentrations appreciable within 1 hour (Brown 2016, PMID 26865186, abstract read: total plasma and brain, not free, rat not mouse). So **a juvenile-rat total brain exposure exists** for retigabine, contrary to "no juvenile exposure found"; free concentration and mouse not found. The same paper reports **neuronal apoptosis in developing rat brain after repeated dosing** (three doses in 24 hours at 15 mg/kg), not after a single dose of up to 30 mg/kg: a harm cell for any juvenile use of the class. Other records: P-retigabine with "improved brain distribution" (PMID 25319542, 2015, title read), isobolographic mouse study (PMID 18773196, 2009, title read).
- **Label (openFDA):** no match for "ezogabine" by this query on this date (NO_MATCH_FOUND is not absence of a label); the agent is known to have been withdrawn, which is from memory and not read here. No label text read.
- **Not measured or not found:** a mouse juvenile exposure; free brain concentration; Kv7.2/7.3 potency at physiological temperature in neurons.

## Azetukalner (= XEN1101; ChEMBL CHEMBL5095264, NAME_EXACT, SYNONYM_EXACT for XEN1101)
- **Potency:** one KCNQ2 EC50 98 nM (FluxOR, CHO, patent-sourced row). Not found by these routes: KCNQ3, KCNQ2/3, KCNQ4, KCNQ5, any patch-clamp value, any selectivity.
- **Exposure:** PubMed "XEN1101 brain concentration" 1 record, a human TMS pharmacodynamic study (PMID 31568714, title read); "azetukalner pharmacokinetics rodent" 0 records. Rodent brain or plasma exposure: not found by these two routes (a second naming, XEN1101, was searched).
- **Label (openFDA):** NO_MATCH_FOUND for the name: not found by this route, not a statement about development status.

## ICA-069673 (ChEMBL CHEMBL2047521; identity: see the recipe: ChEMBL free-text search plus structure; no name stored in ChEMBL)
- **Potency:** KCNQ2/KCNQ3 EC50 0.69 microM (86Rb+ efflux, CHO, 2011); KCNQ3/KCNQ5 EC50 14.3 microM; KCNQ1/minK IC50 above 100 microM (all one document). 6 rows in all, 3 on Kv7 symbols.
- **Exposure:** PubMed "ICA-069673 mice brain" 0 and "ICA-069673 pharmacokinetics" 0 records: not found by these routes.
- **Label:** none expected (a tool compound); not searched.

## XE991 (ChEMBL CHEMBL342375, NAME_EXACT)
- **Potency:** IC50 55 nM at Kv7.2 (thallium flux, HEK293, 2019); rat hippocampal acetylcholine release EC50 450 nM (1998). 7 rows in all.
- **Exposure:** "XE991 brain concentration mice" returned 4 records, none a pharmacokinetic measurement by title (slice and cell physiology papers); not found by these two routes. A research tool, no label.

## What changes for SCI's exposure-effect choice (batch 2)
1. Ezogabine is the only Kv7 agent with both an in vitro potency spread and a published mouse brain concentration-response in MES (and a juvenile-rat total brain exposure with an apoptosis signal). Its in vitro potency must be chosen by readout first: a 26-fold spread.
2. Azetukalner and ICA-069673 have one or three rows and no found rodent exposure: a class mapping to them rests on inference.
3. No openers can be ranked from these rows: same-document comparisons only.
