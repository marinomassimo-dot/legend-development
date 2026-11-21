# ADV-135 route results (IT, 2026-11-21): reports not held

Plain clients only (Europe PMC REST and the PubMed search and metadata tool); no e-mail address, no contact-address service, no browser-header spoofing, no challenge page met.

## Route 1: Europe PMC full-text search (five queries, WWOX with WOREE, SCAR12 or DEE28, and calcium / lipid / glucose / endocrine-bone / metabolic work-up words)
54 distinct records. Every record that is a human WWOX case report or series was already held; the new records are reviews of other diseases, ataxia classifications, cancer or model-system papers. Result: no held-gap report found by this route.

## Route 2: PubMed, `WWOX AND (epileptic encephalopathy OR WOREE OR SCAR12) AND (case report OR patients)` (48 records) and `WWOX AND (hypocalcemia OR hypoglycemia OR hypolipidemia OR dyslipidemia OR "metabolic work-up") AND (patient OR patients OR infant)` (2 records, both already held and neither a WOREE or SCAR12 report: the metabolic-syndrome review of 2014 and a hypertension susceptibility-gene association study of 2012, Yang et al., PLoS One, DOI 10.1371/journal.pone.0032907, whose abstract mentions WWOX only as "related to hypoglycemia and hyperphosphatemia", a mouse-model attribution, not a human case)
Sixteen PubMed records are not held as full text. Fifteen are human reports of the WOREE or SCAR12 spectrum (listed below); one is the correction notice to the 20-case series of Piard et al. (the series itself is held). Their abstracts (read through the PubMed metadata tool) name none of: calcium, lipid or cholesterol, glycaemia or glucose, a metabolic work-up, cortisol, thyroid. An abstract that omits an analyte is not evidence that the report omits it.

| PMID | Year | Journal | Subject as titled | Europe PMC open full text | Status for ADV-135 |
|---|---|---|---|---|---|
| 42721537 | 2026 | Seizure | WOREE case series of seven patients from Argentina | none | access-limited; abstract only |
| 42190144 | 2026 | Neurology | burst-suppression EEG in early infantile DEE (WWOX named in the record) | none | access-limited; abstract only; not a WWOX-specific report |
| 41442931 | 2026 | Pediatr Neurol | vigabatrin-associated MRI abnormalities in two children with WWOX variants | none | access-limited; abstract only |
| 40875931 | 2025 | Neurology | WWOX-related DEE: expanding the clinical spectrum | none | access-limited; abstract only |
| 39933386 | 2025 | Seizure | infantile epileptic spasms syndrome case series from Argentina (WWOX among causes) | none | access-limited; abstract only |
| 35363364 | 2022 | Eur Rev Med Pharmacol Sci | candidate genes in Saudi epileptic patients | none | access-limited; abstract only |
| 34034642 | 2021 | Neurol Res | six patients with WWOX-related epileptic encephalopathy | none | access-limited; abstract only |
| 32037574 | 2020 | Int J Dev Neurosci | early-onset epileptic encephalopathy, novel compound heterozygous variant | none | access-limited; abstract only |
| 32051108 | 2020 | Epileptic Disord | a Chinese patient with epilepsy and compound heterozygous WWOX variants | none | access-limited; abstract only |
| 31669195 | 2019 | Int J Dev Neurosci | novel compound heterozygous variants, early infantile epileptic encephalopathy | none | access-limited; abstract only |
| 30094525 | 2018 | Neurol Sci | WWOX-associated encephalopathies, phenotypic spectrum and genotype-phenotype correlation | none | access-limited; abstract only |
| 29852413 | 2018 | Seizure | targeted sequencing in children with epileptic encephalopathy (WWOX among causes) | none | access-limited; abstract only |
| 26345274 | 2015 | Am J Med Genet A | severe CNS involvement in WWOX variants, five new cases | none | access-limited; abstract only |
| 25716914 | 2015 | J Hum Genet | WWOX and severe recessive epileptic encephalopathy, a prenatal-period case | none | access-limited; abstract only |
| 25411445 | 2015 | J Med Genet | WWOX-related encephalopathies, phenotypic spectrum and genotype-phenotype correlation | none | access-limited; abstract only |

## What this fixes
These fifteen reports are UNREAD at full-text depth. They are listed as a named access gap, not as "not reported". The remaining tiers of the full-text cascade (a repository copy or a publisher copy) would need an open full text; the cascade's usual DOI-resolver tier asks for a contact e-mail, which this work must never send to any service, so it was not run. The route was stopped here as a route result, not as an absence claim.
