# ADV-122 producer A: report as delivered (legend-delegate, sonnet, effort medium, one round, no sub-delegation; delivered 2026-11-20; persisted verbatim by SCI from the subagent hand-back, which is the only place it lived; brief: PRODUCER_A_BRIEF_ETX_PK_BY_AGE_SCI_20261120.md). Producer output, NOT yet verified by SCI or a second reader: every number is a producer claim until adjudicated. Hypothesis level; no dose is a recommendation; not medical advice.

# ADV-122 producer A report: ethosuximide PK by age in rodents (hypothesis level; no dose or recommendation; research concentrations and animal doses are findings of the sources; reference genotype class only; not medical advice)

Delegate: sonnet, effort medium, one round, no sub-delegation. No repository file edited. Scratch: /home/desktop/.claude/jobs/53cd1e96/tmp/adv122/producer_a/ (qc.py plus the fetched bytes). Bibliographic data from PubMed (via the PubMed tools and NCBI E-utilities; DOIs given where used). Every quote below was substring-verified (qc.py: strip real tags, unescape, thin and no-break spaces to normal) against bytes I fetched: Europe PMC fullTextXML for PMC3401299 and PMC6394437 and PMC4419386; NCBI efetch pubmed XML for the abstracts. Nothing was sent to any service except PMIDs, PMCIDs and query terms.

**Headline.**
- Item 1 is empty: I found no neonatal, infant, juvenile or weanling rodent ethosuximide concentration or kinetic parameter at any age (two routes).
- Four adult-rodent facts bear on S1, S2, S4 and S5: the mouse half-life, the rat brain-to-plasma ratio (two sources that disagree), dose independence of that ratio, and the anchor's Methods.
- The anchor's Methods (item 6) leave the homogenate unit unresolved by text. A mass-balance check (my own arithmetic, labelled as such) argues against the 2.87 mM branch.

Repository route for every PMID below: `files/fulltext` and `files/supplement` hold nothing for them (only Cheng PMID 32000863, not re-read here); the receipt ledger `status --pmid` returned `[]` for 22315091, 708147, 3400266, 11745910, 590227, 9698055, 8469708, 6802548, 8549027, 816644, 2941808 (36537292 has a ledger entry, not used here).

---
## Item 1. Neonatal, infant, juvenile or weanling rodent ethosuximide concentration or kinetic parameter

No row has a juvenile concentration or parameter. The juvenile cell stays empty. The only juvenile ethosuximide papers found are pharmacodynamic, and none of their abstracts reports a level. They are listed because the sources the S3 to S6 factors lean on cannot be built from them, but the doses and ages matter to the Cheng comparison.

| source | species, strain, age | dose, route | time | matrix, total/free | value as printed | locator and quote | access |
|---|---|---|---|---|---|---|---|
| Velisek and colleagues 1998, Life Sci, PMID 9698055, doi 10.1016/s0024-3205(98)00266-5 | rat (strain not in abstract), 18 and 25 days | 62.5 and 125 mg/kg i.p. | not stated | none reported | no level | Abstract: "studied in immature rats 18 and 25 days old"; "Pretreatment with ESI in doses of 62.5 and 125 mg/kg i.p. suppressed episodes of spike-and-wave rhythm"; "In 18-day-old animals ESI did not exhibit an anticonvulsant effect" (minimal metrazol seizures, 70 mg/kg PTZ) | AB |
| Pharmacology, Biochemistry, Behavior 1993, PMID 8469708, doi 10.1016/0091-3057(93)90034-q | rat, 12, 18, 25, 90 days | 125 or 250 mg/kg i.p. | not stated | none reported | no level | Abstract: "assessed in rats 12, 18, 25, and 90 days old"; "ethosuximide pretreatment increased the incidence of clonic seizures in 12-day-old rats" | AB |
| Mares and Velisek 1986, Physiol Bohemoslov, PMID 2941808 | rat, 7, 12, 18, 90 days | 125 mg/kg i.p. | not stated | none reported | no level | Abstract: "rats aged 7, 12, 18 and 90 days"; "ESI specifically inhibited rhythmic activity in adult rats" | AB |

Searches (PubMed tool, with term lists written before reading hits): ethosuximide AND (immature OR neonatal OR developing OR postnatal OR pup) AND (rat OR mouse) AND (pharmacokinetics OR plasma OR serum OR brain concentration), 22 hits, none a juvenile level; ethosuximide with rat pups, immature rats, developing, ontogeny, age-dependent AND PTZ, flurothyl or seizure, 73 hits; ethosuximide[Title] with development, ontogeny, neonatal, immature or age, 88 hits; a generic anticonvulsant developmental pharmacokinetics query; "succinimide OR ethosuccimide OR Zarontin" with immature or neonatal, 7 hits, none relevant; Europe PMC REST ethosuximide AND postnatal or neonatal or pups or immature AND level or concentration, 97 hits, review and non-rodent noise, none a pup level. Full text of 9698055, 8469708 and 2941808 was not obtained: ScienceDirect and publisher routes returned HTTP 403 challenge pages, and the papers are not in PMC.

What it answers: no pup value exists in the sources reached; the pup-over-adult ratio cannot be taken from data, so S3 to S6 for P12 to P17 remain assumptions. What remains missing: the full texts of the three Czech-school papers (they may print plasma levels in Methods; this is an open route, not an absence). The dose range 125 to 250 mg/kg i.p. in P12 to P25 rats is shared with Cheng's 150 mg/kg.

---
## Item 2. Adult rodent time course (mouse first, rat second)

| source | species, strain, age | dose, route | time | matrix, total/free | value as printed | locator and quote | access |
|---|---|---|---|---|---|---|---|
| El Sayed, Loescher, Frey 1978, PMID 708147 (dog paper) | mouse; "female rats" for the rat; strain, age not in abstract | not in abstract | not in abstract | serum and brain | mouse half-life "hardly 1 hr"; "equilibrated within 10 min" | Abstract: "In female rats, ethosuximide had an average half-life of 10 hr, in mice of hardly 1 hr. Concentrations in serum and brain of mice equilibrated within 10 min." | AB |
| Nygaard 2015, Alzheimers Res Ther, PMID 25945128 (secondary, cites the above as ref 17) | mouse | n/a | n/a | n/a | "1 hour" | Methods: "Owing to the short half-life of ethosuximide in mice (1 hour)" (ref CR17 is El Sayed 1978) | FT of that sentence; not a second origin |
| El Sayed 1978, same paper, dog (context only) | dog | 40 mg/kg i.v. | | serum | half-lives 11 to 25 hr; distribution volume 44 to 66% of body weight; absorption 88 to 95% | Abstract: "the volume of distribution correspond to between 44 and 66% of body weight"; "maximal serum concentrations were reached within 1-4 hr and the absorption amounted to 88-95%" | AB |
| Aguilar-Veiga and colleagues 1991, Res Commun Chem Pathol Pharmacol, PMID 2047576 | rat, Wistar, age not in abstract | 50 mg/kg i.p. single | 5 min to 2 h | brain (cortex, midbrain, cerebellum) and plasma | cortex brain/plasma ratio 2.04 +/- 0.14 at 5 min, 0.14 +/- 0.01 at 2 h | Abstract: "The brain/plasma ratio in the cortex changes drastically from 2.04 +/- 0.14 (5 m after injection) to 0.14 +/- 0.01 (2 h after injection)" | AB |
| Patel, Levy, Rapport 1977, Epilepsia, PMID 590227, doi 10.1111/j.1528-1157.1977.tb05001.x | rat, strain not in abstract | 20, 40, 60, 80 mg/kg i.p. every 12 h for 108 h (chronic) | steady state | cortex, midbrain, cerebellum, pons-medulla vs plasma | tissue/plasma 0.917, 0.942, 0.902, 0.903; plasma 8 to 135 ug/ml | Abstract: "The mean tissue/plasma ratios were 0.917, 0.942, 0.902, and 0.903 for cortex, midbrain, cerebellum, and pons-medulla, respectively" | AB |
| Xenobiotica 1988, PMID 3400266, doi 10.3109/00498258809041673 | rat, male Sprague-Dawley | 35 mg/kg i.v. | followed 75 h | plasma | terminal curve not linear; no numbers in abstract | Abstract: "The plasma disappearance of a single 35 mg/kg dose followed for 75 h was not linear" | AB |
| Biopharm Drug Dispos 2001, PMID 11745910, doi 10.1002/bdd.266 | rat, conscious, strain not in abstract | 40 mg i.v. and i.p. (as printed, mg not mg/kg) | | plasma | (R) cleared faster than (S); no difference in apparent volumes; no numbers in abstract | Abstract: "total body clearance of (R)-ethosuximide was significantly larger than that of (S)-ethosuximide" ; "no significant differences were found between apparent volumes of distribution" | AB |

What it answers: the only mouse timing statement is a one-hour half-life with serum-brain equilibration inside 10 min, from an abstract, one origin (Nygaard repeats it, does not add data). A concentration-against-time table for mouse was not found. With a half-life of about 1 h, 45 min is not on a plateau: it is on the elimination limb (S2). What remains missing: the El Sayed full text (mouse dose, mouse strain, Tmax, any table; not reached: Karger/Arch Int Pharmacodyn is non-OA and not in PMC), full texts of 590227, 2047576, 3400266, 11745910 (non-OA; DOI landing pages return 403 challenge pages; no PMCID exists). Not tried: interlibrary or purchase routes, excluded by the brief.

---
## Item 3. Linearity (two or more doses with matching concentrations; dose-dependent kinetics)

| source | species | dose, route | time | matrix | value as printed | locator and quote | access |
|---|---|---|---|---|---|---|---|
| Patel 1977, PMID 590227 | rat | 20 to 80 mg/kg i.p. chronic | steady state | brain regions/plasma | ratio independent of dose and of plasma 8 to 135 ug/ml | Abstract: "For each brain region, the distribution ratio was independent of dose (20 to 80 mg/kg) and plasma concentration (8 to 135 microgram/ml)" | AB |
| Patel, Levy, Bauer 1975, PMID 816644 | rhesus monkey (not rodent) | 30, 60, 90 mg/kg i.v. and oral | | plasma | volume 0.80 +/- 0.09 L/kg; kinetics linear | Abstract: "there was no evidence of dose-dependent elimination kinetics after intravenous or oral administration" | AB |
| Xenobiotica 1988, PMID 3400266 | rat | 35 mg/kg i.v. single, multiple | 75 h | plasma | non-linearity attributed to enzyme induction, not saturation | Abstract: "A dose-ranging study suggested that the apparent non-linearity of ethosuximide's plasma disappearance might be due to enzyme induction over time" | AB |
| El Sayed 1978, PMID 708147 | dog | 40 mg/kg i.v.; three daily doses | | serum | half-lives seemed prolonged above 100 ug/ml | Abstract: "At serum concentrations above 100 microliter/ml, half-lives seemed prolonged" (unit as printed) | AB |
| Bauer 1982, Clin Pharmacol Ther, PMID 6804151, doi 10.1038/clpt.1982.104 (human, context) | human | oral | steady state | plasma | nonlinear dose-concentration relation in 7 of 10 | Abstract: "Data from seven of the 10 patients showed evidence of a nonlinear relationship when steady-state ethosuximide concentrations were plotted against dose" | AB |

What it answers: no rodent source reports concentrations at two or more doses in the 72 to 150 mg/kg single-dose range. Indirect evidence: the dose-independent brain-to-plasma ratio at 20 to 80 mg/kg (rat chronic), no dose dependence in monkey at 30 to 90 mg/kg, and an enzyme-induction explanation for rat curvature. Counter-evidence: dog half-life prolongation above 100 ug/ml and human nonlinearity at steady state. The anchor's own 134.9 ug/g, scaled linearly to 150 mg/kg (my arithmetic: 134.9 x 150 / 72.3 = 279.9 ug/g, 1.98 mM on the tissue branch), implies concentrations above the 100 ug/ml dog threshold, so the dog statement is not excludable for the S1 high end. S1 therefore stays an assumption; the data support linear for a single dose at moderate concentration but leave a sub-linear branch open. What remains missing: any mouse dose series.

---
## Item 4. Intraperitoneal absorption

| source | species | route | value as printed | locator and quote | access |
|---|---|---|---|---|---|
| El Sayed 1978, PMID 708147 | dog (not rodent) | oral | absorption 88 to 95% | Abstract: "maximal serum concentrations were reached within 1-4 hr and the absorption amounted to 88-95%" | AB |
| El Sayed 1978 | mouse | i.p. (route not stated in abstract) | serum and brain equilibrated within 10 min | see item 2 | AB |
| Patsalos 2005 review, PMID 16302888 (human, context) | human | oral | bioavailability 100% for the group including ethosuximide | Abstract: "Bioavailability is 100% with the exception clonazepam (90%) and topiramate (81-95%)" | AB (quote not re-verified by substring; treat as read from the tool output only) |

What it answers: nothing on rodent i.p. absorption or on any age effect on i.p. absorption. The mouse "equilibrated within 10 min" statement supports fast absorption after parenteral dosing, but the abstract does not say i.p. Two PubMed queries on i.p. absorption (adult and neonatal) returned nothing relevant. S6 stays an assumption (no source).

---
## Item 5. Human reference, label level only

| source | statement | quote | access |
|---|---|---|---|
| US Zarontin label, DailyMed set id 0e008f33-70a1-4bc6-b3a0-d45214418ab6 (also the Mylan and Chartwell ethosuximide solution labels, set ids 19c924c2... and 9812840a...) | The text I fetched contains no pharmacokinetic paragraph (no "half-life" string found in the three labels); the Clinical Pharmacology section is pharmacodynamic only | none | LAB, searched, absent in these three |
| Review: Practical Guide to Treatment of Childhood Absence Epilepsy, PMC6394437 (PMID 30734897) | children: half-life 30 to 40 h; linear kinetics; no auto-induction; hepatic, CYP3A | "The elimination half-life is 30–40 h in children, with linear kinetics and no auto-induction" | FT passage |
| Hvidberg and Dam 1976, PMID 797496, doi 10.2165/00003088-197601030-00001 | adults 2 to 3 days; children shorter | Abstract: "in adults 2 to 3 days; in children shorter" | AB |
| Bartoli and colleagues, Clin Pharmacokinet 1982, PMID 6802548, doi 10.2165/00003088-198207020-00006 | children under 10 years have lower plasma level/dose ratios than adolescents and adults | "Children younger than 10 years had men L/D ratios significantly lower" (typo "men" as printed; first author not confirmed from the abstract, cite by PMID only) | AB |
| Paediatric PK review, PMID 8549027, doi 10.2165/00003088-199529040-00005 | lower C/D ratios under 10 years; well absorbed, minimally protein bound | "Lower C/D ratios are reported in children younger than 10 years old than in older children"; "Ethosuximide is well absorbed, minimally protein bound and slowly eliminated" | AB |

No human brain-to-plasma or brain-to-CSF statement was found for ethosuximide (the dog CSF equilibrium of 20 to 30 min is in 708147). The EU SmPC route was not searched (ethosuximide has no central EU authorisation; the national texts were out of scope). Full paediatric clearance is producer B's item.

---
## Item 6. The anchor's Methods (PMID 22315091, PMC3401299, doi 10.1007/s00702-012-0767-1; FT read in the passage via Europe PMC fullTextXML and the PubMed full-text tool)

Answer: the printed unit is "per g of wet tissue", but the text does not say whether the homogenate dilution was back-corrected, so the 1:2 homogenate question is not resolved by the text. Quotes (verified): "Mice were killed by decapitation at times chosen to coincide with that scheduled for the PTZ test and the whole brains of mice were removed from skulls, weighed, harvested and homogenized in distilled water (1:2, w:v)"; "The total brain AED concentration was expressed in μg/g (VPA, PB and ETS) or ng/g (CZP and TGB) of wet tissue as mean ± SEM of eight (VPA, PB and ETS) or ten (CZP and TGB) separate determinations." No perfusion is mentioned (decapitation, whole brains removed and weighed). Animals: "Male albino Swiss mice weighing 24–30 g were used throughout this study after 1 week of acclimatization"; no age in days or weeks is printed (age missing; weight only). Drugs: ETS was "suspended in 1% solution of Tween 80 ... in saline", given i.p. "in a volume of 10 ml/kg body weight", "ETS 45 min" before the test. Assay: supernatant "analyzed by fluorescence polarization immunoassay using a TDx analyzer" (not chromatography). Table 3 row: "ETS (72.3) + saline 134.9 ± 7.73 µg/g" (n at least 8 per group; sildenafil 40 arm 153.5 ± 7.99, not significant). Same paper, control ED50 for ETS in the s.c. PTZ test: "155.8 (139.7–173.7)" mg/kg (Table 2), which lies close to the Cheng 150 mg/kg.

Mass-balance check (my arithmetic, inference, not a source statement; for the verifier). 72.3 mg/kg at formula mass 141.17 is 0.512 mmol/kg. If the whole dose were in a body-water space of 0.65 L/kg with no elimination, the ceiling is about 0.79 mM (112 ug/ml); at 0.5 L/kg (the dog 44 to 66% range as a proxy) about 1.02 mM. The tissue branch (0.956 mM, 134.9 ug/g) sits at that ceiling or slightly above it; a 3-fold correction of a 1:2 (w:v) homogenate (2.87 mM) would need an apparent distribution volume of about 0.18 L/kg at zero elimination (more with the roughly 1 h half-life), below extracellular water. That argues against the 2.87 mM branch but is not proof (a brain-to-plasma ratio above 1 as in the rat 5-min value, or assay bias in homogenate, would loosen it). Both branches stay in the chain; the "wet tissue" wording is the only textual support.

---
## Conflicts between sources
1. Rat brain-to-plasma ratio: about 0.9 and flat across 20 to 80 mg/kg chronic i.p. (PMID 590227, steady state) vs 2.04 at 5 min falling to 0.14 at 2 h after a single 50 mg/kg i.p. (PMID 2047576, Wistar). Design differs (chronic vs single dose); the 45 min single-dose ratio is not given in either abstract.
2. Half-life by species: mouse about 1 h and rat about 10 h (PMID 708147) vs the rapid fall of rat brain ratio in PMID 2047576; the El Sayed rat value is for female rats and the 1 h mouse value has no stated strain or sex.
3. Linearity: no dose dependence in monkey (816644) and dose-independent brain ratio in rat (590227) vs half-lives prolonged above 100 ug/ml in dog (708147), nonlinearity at steady state in 7 of 10 patients (6804151), and rat curvature attributed to induction (3400266).
4. Pharmacodynamic age profile (the P12, P18 findings of 8469708 and 9698055): ethosuximide was ineffective or paradoxical in 12-day and 18-day rats in some models at 125 to 250 mg/kg, effective in 25-day and adult rats. A reader may take this as a hint of lower exposure in pups; it is not a pharmacokinetic result and does not support any pup-over-adult ratio.

## Where the data are thinnest (five lines)
1. No juvenile ethosuximide level or kinetic parameter in any matrix at any age (items 1, S3 to S6 are assumption-only for P12 to P17).
2. The anchor's unit (per tissue vs per 1:2 homogenate) is unresolved by text and the mass-balance check is only my inference; mouse age, sex-independent strain data and any mouse concentration-time table are missing.
3. Mouse half-life rests on one abstract line (El Sayed, plus Nygaard repeating it); its dose, route, strain and sex were not read, so where 45 min sits on the curve (S2) is a single-origin inference.
4. No rodent dose series spanning 72 to 150 mg/kg; linearity at the Cheng dose (about 280 ug/g by linear scaling, above the dog 100 ug/ml signal) is assumed.
5. Nearly every number is abstract-level (AB) from non-OA 1975 to 2001 papers; the DOI and publisher routes return challenge pages; Europe PMC and PMC offered no text for 3400266, 11745910, 590227, 2047576, 708147, 9698055, 8469708 (the PMC page for two OA-listed rat papers returned a reCAPTCHA, so I stopped that route; efetch returned a publisher no-XML notice for PMC3837503, whose full text is therefore not read).

## Not done
No receipt, no repository edit, no commit; Cheng 2020 (PMID 32000863) was not re-read (age of the seizure test is not in my brief). Mountney 2013 (PMID 23822888, rat TBI, ethosuximide 12.5 to 187.5 mg/kg) might carry plasma levels but its full text was not reachable (PMC returned no text; efetch no-XML). The brief's abstract-only list (17085857, 22789660, 18566800, 16140589) was not re-opened beyond confirming the PMIDs appear in Europe PMC title hits (17085857, 18566800).

Files: /home/desktop/.claude/jobs/53cd1e96/tmp/adv122/producer_a/ (qc.py, anchor.xml, abs2.xml, abs3.xml, cae.xml, PMC4419386.xml, zarontin.txt).
