# ADV-122 pre-registration: a prior bound for ethosuximide brain exposure in the P12 to P17 null pup at the Cheng regimen (SCI successor window S, 2026-11-20; hypothesis level; no dose, no schedule, no recommendation for or against any use of any agent in any person; reference genotype class only; not medical advice)

**Frozen before any search and before any number is computed.** Committed to git before `chain_prior_bound.py` exists and before any producer is dispatched; the commit order is the evidence of the freeze.

## 0. What was already seen (disclosure)
* From the repository and the checkpoint: the adult anchor (PMID 22315091: adult Swiss mouse total brain 134.9 ug/g at 72.3 mg/kg i.p., 45 min; 955.6 uM at formula mass 141.17; about 2.87 mM if the printed value is per g of a 1:2 homogenate); the thresholds (0.6 mM persistent T-current IC50 and one unmapped potency row, above 5 mM CACNA1I FLIPR, adult effective band about 2 to 6 mM as held in the ADV message, the 5 mM-class bound); v3.1 6.2 and 6.5.
* From the held Cheng 2020 full text (PMID 32000863, root `files/fulltext/PMID32000863_Cheng2020_PMC_r2.xml`), Methods grep only: **ethosuximide 150 mg/kg i.p., one injection, 45 min before PTZ**; no level reported; the age of the seizure test is not read yet (a producer item). So the regimen is a single dose with the same 45 min interval as the adult anchor: **no accumulation step is needed**, and the chain's time step is a check, not an assumption.
* Not seen: any rodent or paediatric ethosuximide pharmacokinetic value other than the anchor; any ontogeny value for enzymes, BBB or transporters.

## 1. Scope
Input: ADV-122 (message of 2026-11-20; `assignments/ADV-122.md` had not landed at 1ce83035b; re-read when it lands, check perimeter, budget, `deliver_to`, `related_work`). Output: one prior bound, items (1) to (4) of the message, plus the script, the producer reports as delivered, one blind verification of the numbers that decide the range, one result page.

## 2. The chain (steps fixed now; labels may be tightened by the data, never loosened)
Quantity: total brain concentration C_pup(45 min after 150 mg/kg i.p., P12 to P17, null pup), in mM.

| step | statement | label if no source reached |
|---|---|---|
| S0 | adult anchor, 45 min, 72.3 mg/kg: C0 = 0.956 mM (printed per g tissue) or 2.87 mM (printed per g of 1:2 homogenate); the unit reading is a branch, not averaged | data (value), assumption (which branch) |
| S1 | dose scaling 72.3 to 150 mg/kg (factor 2.07) at one timepoint: linear (factor 2.07), with a sub-linear and a super-linear alternative if a source reports non-linearity (saturable metabolism or absorption) | assumption (linearity) until a dose-ranging source is read |
| S2 | time: the anchor time (45 min) equals the Cheng interval (45 min); the adult curve shape (Tmax, t1/2) says whether 45 min sits on a plateau or a slope | inference |
| S3 | pup clearance relative to adult (metabolising enzymes, renal excretion) at P12 to P17: ratio r_CL = CL_pup / CL_adult (lower raises exposure at 45 min only through the elimination phase, which at 45 min is partial) | inference, with paediatric label facts as data |
| S4 | distribution: the pup volume of distribution (total body water fraction; ethosuximide is a small polar drug that distributes in total body water) relative to adult, r_V | inference |
| S5 | brain-to-plasma ratio at P12 to P17 relative to adult, r_BP (BBB and transporter ontogeny, brain water fraction, protein binding is negligible for ethosuximide) | assumption until a neonatal brain-plasma value is read |
| S6 | absorption after i.p. in a pup (peritoneal absorption, injection volume per body weight): r_A for the 45 min value | assumption |
| S7 | result: C_pup = C0 x 2.07^(linearity branch) x r_A x r_V^(-1) x f(r_CL, 45 min) x r_BP, evaluated at low, central and high settings for each factor; both directions reported; a one-at-a-time tornado (script) names the dominant assumption | derived |

The script is the only place arithmetic is done; each factor carries `label` (data / inference / assumption), source id and access level or "no source", a competing explanation and a weakening observation, as a row of a TSV the script reads.

## 3. Readouts fixed in advance
* **The range** [C_low, C_high] with the branch of S0 kept separate (two ranges, not one blend), and the factor that dominates the width (largest swing in the tornado, ties stated).
* **Position against the held thresholds** (0.6 mM, 2 mM at 150 mg/kg as linear scaling of the anchor, 5 mM, adult effective band 2 to 6 mM): for each of the two S0 branches, one of: entirely below 0.6 mM; straddles 0.6 mM; between 0.6 and 5 mM; straddles 5 mM; entirely above 5 mM. Counted in the units of the anchor, not rounded.
* **Reachability in principle** of the two outcome rows (v3.1 6.2 pragmatic null: measured exposure at the Cheng regimen below the potency anchor; 6.5 tolerance-limited: the highest tolerated exposure below the anchor): yes if the prior range reaches the condition at some setting that the sources do not exclude; no only if every setting reaching it is excluded by a data-labelled factor. An assumption never excludes.
* **Minimum measurement** (item 4): matrices, time points, ages, total versus free, derived from which factor dominates the width and which factor is decided by a single measurement.

## 4. Retrieval plan and delegation (delegation_budget.md sections 1 to 3)
Four narrow producers, one active at a time, each `legend-delegate`, model sonnet, effort medium, stated in every dispatch, no sub-delegation, no repository file edited: (a) ethosuximide pharmacokinetics in rodents by age and any neonatal rat or mouse value (t1/2, clearance, volume, brain-to-plasma ratio, linearity, i.p. absorption); (b) paediatric clearance facts (label, papers, CYP involvement, age dependence); (c) rodent ontogeny of the metabolising enzymes and of renal excretion at P12 to P17 as printed; (d) neonatal BBB and transporter ontogeny for a small polar drug, plus brain water fraction by age. Then **one blind verifier** (sonnet, effort high, separate context, sources reachable) on the rows that decide the range, receiving (value, quote, locator) triples without my conclusions. A producer whose brief is satisfied by the previous report is not dispatched (checked before each dispatch). No second verifier unless the first overturns a deciding row.

## 5. Two routes for any "not found" and what a number must carry
Before writing "not found" or "not held": (1) the repository route (`files/fulltext`, `files/supplement` by PMID or PMCID, the receipt ledger) and (2) one external route (PubMed tools, Europe PMC REST, PMC page, efetch); both stated. A fetch failure is not "absent". Every number: source id, access level (FT passage read, AB abstract only, LAB label), a verbatim quote of at most 300 characters taken from fetched bytes (substring-verified by me in `quote_check.py`), species, strain, age, dose, route, time, matrix, total or free, locator. A database transcription is one origin. Adult values are never promoted to juvenile cells; a juvenile cell without a source stays empty and the chain factor is an assumption.

## 6. Stop rule
(1) Stop an item at the first source that answers its stated question or after two routes are exhausted. (2) Stop retrieval when the tornado, computed on the factors already held, shows that the dominant factor is one no retrieval item can fix (then more retrieval on the others cannot narrow the range); I report the bound and the minimum measurement. (3) Hard cap: four producers and one verifier; a fifth delegate needs a written `ESCALATION` line. (4) If the unit reading of S0 cannot be resolved from PMID 22315091 by a second route (Methods text of the anchor), the two branches stay and the width carries them.

## 7. What would change the plan
A neonatal rat or mouse ethosuximide concentration at any age from a primary source would replace S3 to S6 for that age by data (then the chain is rebuilt with the single factor "pup over adult" as a measured ratio, and the chain is kept as the cross-check). A primary source showing non-linear kinetics in the 70 to 150 mg/kg range would replace the linear S1.

## 8. Deliverables
`chain_prior_bound.py`, `chain_factors.tsv`, `OUTPUT_chain.tsv`, `OUTPUT_tornado.txt`, the four producer briefs and the reports as delivered, the verifier brief and report, `quote_check.py` and its output, `RESULT_ADV122_SCI_20261120.md`. A dated line only if ADV asks.
