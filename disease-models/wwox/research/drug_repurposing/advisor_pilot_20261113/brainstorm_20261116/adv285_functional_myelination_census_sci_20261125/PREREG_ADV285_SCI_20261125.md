# PREREG ADV-285 (SCI, 2026-11-25): functional myelination readout census, frozen before any search

Hypothesis level; not medical advice; reference genotype class only. Brief: `advisor_pilot_20261113/assignments/ADV-285.md`. Kotler et al., PNAS 2026 (PMID 42485389) is a lead only: PNAS 403, Europe PMC not open access, Zenodo 504 are route results and are never bypassed; the Obeid 2026 classifier stop is untouched; no contact; no e-mail address sent to any service; a challenge page, 403, 429 or 5xx is a route result.

## 1. The question

Does ANY source measure FUNCTIONAL myelination, (a) in a Wwox-deficient model or in WWOX-DEE patients, (b) in adjacent hypomyelinating or leukodystrophy models with a PHARMACOLOGICAL arm and a functional readout whose mechanism (OPC maturation, ER stress or integrated stress response, energy supply) overlaps what the repository holds for Wwox?

## 2. Inclusion rule for "functional" (frozen)

A measurement of signal conduction or timing along myelinated axons or tracts, in vivo or ex vivo, reported as a number with a unit or a proportion: compound action potential (CAP, CNAP) amplitude or area; conduction velocity; latency or interpeak latency of an evoked potential (VEP, ABR, SSEP, MEP, optic-nerve or callosal CAP); nerve conduction study of a central or peripheral tract; propagation success or firing reliability along an axon. NOT functional under this rule: g-ratio, myelin thickness, MBP or PLP levels, nuclei counts, EM, behaviour (rotarod, grip, gait, clasping), EEG power or seizure counts, calcium imaging of somata. A readout counts for question (b) only with a pharmacological arm (a drug, a compound or a diet given to the affected model, with a vehicle or untreated affected comparator).

## 3. Search strings (PubMed standard search, Europe PMC REST with the same words in TITLE_ABS; both public reads, plain GET)

* **S1 (Wwox x function):** `(WWOX OR Wwox) AND ("conduction velocity" OR "compound action potential" OR "evoked potential" OR "evoked potentials" OR "visual evoked" OR "auditory brainstem" OR latency)`
* **S2 (Wwox x myelin):** `(WWOX OR Wwox) AND (myelin* OR oligodendrocyte* OR "white matter" OR hypomyelinat* OR leukodystroph*)`
* **S3 (patients):** `(WWOX OR SCAR12 OR WOREE) AND ("evoked potential" OR "evoked potentials" OR VEP OR ABR OR "nerve conduction" OR "brainstem auditory" OR "visual evoked")`
* **S4 (adjacent models x function):** `(hypomyelinat* OR dysmyelinat* OR leukodystroph* OR "Pelizaeus-Merzbacher" OR shiverer OR "vanishing white matter" OR "Charcot-Marie-Tooth") AND ("compound action potential" OR "conduction velocity" OR "evoked potential" OR "evoked potentials" OR "visual evoked" OR "auditory brainstem")`
* **S5 (drug x myelin x function):** `(clemastine OR miconazole OR benztropine OR clobetasol OR quetiapine OR guanabenz OR sephin1 OR ISRIB OR ibudilast OR "thyroid hormone" OR lactate OR "ketogenic") AND (myelin* OR oligodendrocyte*) AND ("compound action potential" OR "conduction velocity" OR "evoked potential" OR "evoked potentials" OR "visual evoked" OR latency)`

Limits: none by date or species at the search; the language filter is none. Two routes (PubMed, Europe PMC); the count of distinct PMIDs per string and per route, the overlap and the PMIDs found by one route only are recorded before screening.

## 4. Screening (frozen)

Stage 1, by script on abstracts (efetch XML, public read): keep a record when its abstract contains a functional-readout term (S4 list) AND, for question (b), a treatment term (treat*, administ*, inject*, rescue, drug, compound, diet, mg/kg, gavage). Stage 2, by reading: the title and abstract of every Stage 1 record are read and classified INCLUDED (a functional readout in a hypomyelinating or leukodystrophy model with a drug arm, or any readout in a Wwox model or WWOX patients), EXCLUDED-NO-FUNCTIONAL-READOUT, EXCLUDED-NO-DRUG-ARM, EXCLUDED-NOT-A-MYELIN-MODEL, with the reason in one line. Records excluded at Stage 1 are listed with PMID and title in the census file, not discarded silently; the recall limit of the keyword filter is stated. Mechanism overlap is judged from the abstract against three classes the repository holds: OPC maturation or differentiation, ER stress or integrated stress response, energy supply (lactate, glucose, ketones, mitochondrial function).

Access: for each INCLUDED record the access class is recorded (held full text in `files/fulltext`, Europe PMC open-access full text fetched by GET, abstract only, not retrievable) and, for the top rows, the functional readout is read in the full text where held or open.

## 5. Predictions (frozen before any search)

* **P1 (Wwox-deficient animal model with a functional myelination readout, S1 and S2):** 0 (range 0 to 1). **Rejecting observation: one or more Wwox-deficient models with such a readout.**
* **P2 (WWOX patients with a VEP, ABR, SSEP or nerve conduction result in a case report or series, S3):** 1 (range 0 to 4); a reported evoked-potential result is not a myelination readout unless the report states latency or conduction values.
* **P3 (adjacent models, drug arm plus functional readout, INCLUDED after Stage 2, S4 and S5):** 12 papers (range 5 to 30).
* **P4 (of P3, those with a mechanism overlap class and an access class other than "abstract only"):** 3 (range 1 to 8).
* **P5:** the Kotler primary stays unretrievable by the allowed routes (probability 0.9).
* **Step 2 expectation:** the pup design brief (RP-041 v2) carries no functional myelination readout line (0.8); the single measurement that separates the explanations is a conduction readout (optic nerve or callosal CAP, or VEP latency) in the same cohort as the structural readout.

## 6. Delivery

One table (model, species, age, structural readout, functional readout with class and unit, arm, n and unit, effect, source and locator, access); the two-route counts; the Step 2 measurement in the form readout, model, age, comparator, what each explanation predicts, and whether RP-041 carries it; one blind reader (sonnet, effort high, read back from the census) on the final sentences plus the whole table. If no functional readout exists adjacent, that is stated as the missing measurement, not as absence of effect.
