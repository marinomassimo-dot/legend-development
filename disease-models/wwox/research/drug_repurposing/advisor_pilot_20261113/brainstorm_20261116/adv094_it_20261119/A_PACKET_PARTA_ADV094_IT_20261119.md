# Hindcast scoring sheet, Part A (as given to a scorer)

Hypothesis-level diagnostic; never a licence for any use of any agent in any person; no dose or recommendation; not medical advice; no personal information.

## PART A (given to the scorer)

### 1. The pairs
Twelve pairs, each a class-level description of a drug action in a genotype or disease class, with the age group and the endpoint. Names of genes and drugs are not given. The scorer may use only literature dated up to and including the date-cut printed for that pair.

| id | class-level descriptor (no names, no outcome) | date-cut |
|---|---|---|
| HC-01 | Use-dependent sodium-channel blockers in neonatal-onset epilepsies from loss of function of a voltage-gated potassium channel (Kv7 family) that restrains neuronal firing; neonates and infants; endpoint: seizure control and offset. | 2024 |
| HC-02 | An inhibitor of the nutrient-sensing kinase complex mTORC1, as add-on, in a disorder of constitutive overactivation of that complex (loss of a two-protein repressor); ages 2 to 65 years; endpoint: seizure response rate and frequency. | 2014 |
| HC-03 | A potassium-channel blocker with sodium-channel activity, in epilepsies from gain-of-function variants of a sodium-activated potassium channel; infants and children; endpoint: at least 50 percent seizure reduction. | 2020 |
| HC-04 | A use-dependent sodium-channel blocker, mostly as add-on, in an infant-onset epileptic encephalopathy attributed to sodium-channel haploinsufficiency; children 2 to 18 years; endpoint: change in each seizure type. | 1996 |
| HC-05 | A medium-odd-chain triglyceride that supplies an anaplerotic brain fuel, in a disorder of impaired glucose transport into the brain; patients over 1 year old not on a ketogenic diet; endpoint: overall seizure frequency. | 2020 |
| HC-06 | A cofactor vitamin that is inactivated by an accumulating lysine-degradation metabolite, in an inborn error of lysine degradation (loss of an aldehyde dehydrogenase) presenting with neonatal seizures; endpoint: seizure freedom on the vitamin. | 2015 |
| HC-07 | A neuroactive-steroid GABA-A positive allosteric modulator, as add-on, in an X-linked developmental and epileptic encephalopathy from loss of a brain-expressed kinase; ages 2 to 21 years; endpoint: major motor seizure frequency. | 2020 |
| HC-08 | A GABA-A positive allosteric modulator that also inhibits cytochrome P450 (raising co-administered clobazam and valproate), as add-on, in an infant-onset epileptic encephalopathy attributed to sodium-channel haploinsufficiency; children; endpoint: clonic or tonic-clonic seizure frequency. | 1998 |
| HC-09 | A high-fat, low-carbohydrate diet supplying ketones as an alternative brain fuel, in a disorder of impaired glucose transport into the brain (heterozygous loss of function of the transporter); children, 2 to 5 years of follow-up; endpoint: seizure freedom. | 2003 |
| HC-10 | An inhibitor of the brain cholesterol-24-hydroxylase (lowering a glutamatergic-receptor-potentiating oxysterol), as add-on, in an infant-onset epileptic encephalopathy attributed to sodium-channel haploinsufficiency; ages 2 to 21 years; endpoint: monthly convulsive seizure frequency. | 2024 |
| HC-11 | Use-dependent sodium-channel blockers in epilepsies from variants of a brain sodium-channel gene whose variants in this subgroup are truncating or loss-of-function; onset from 3 months of age; endpoint: seizure reduction or freedom. | 2015 |
| HC-12 | A loop diuretic that blocks the chloride importer NKCC1 (to lower intraneuronal chloride and restore GABA inhibition), as add-on to a barbiturate, in full-term newborns with electrographic seizures after perinatal asphyxia; endpoint: reduction of electrographic seizure burden. | 2013 |

### 2. Components, fixed before any scoring
Score each pair on four components, each 0, 1 or 2, from information dated up to the date-cut only. Components are never summed by the scorer and carry no weight. One sentence of justification per component, naming the kind of evidence used (not a citation the scorer cannot check).
* **C1 Target engaged** (the agent reaches and acts on its target in a tissue relevant to the endpoint). 0 = no evidence, or evidence against; 1 = evidence in an adjacent system (another species, cell type, tissue or age); 2 = evidence in the matching system.
* **C2 Direction** (the action moves the pathway the opposite way to the genotype class's effect). 0 = the same way, or the direction is unknown; 1 = indirect or mixed; 2 = directly opposite.
* **C3 Phenotype relevance** (the pathway bears on the endpoint). 0 = no evidence it does; 1 = it does in another condition; 2 = it does in this genotype class (a model or humans).
* **C4 Transfer** (human evidence for this genotype class and age group). 0 = none; 1 = a related class or age group; 2 = the same class and age group.
A component the scorer cannot place is scored 0 and flagged `unknown`; unknown is never rounded up.

### 3. Date-cut rule
The cut is 31 December of the year two years before the year of the paper that fixed the pair's outcome. Why two: a result can be announced, presented or posted a year or more before its paper. What it does not do: earlier reports of the same drug in the same class that fall inside the cut stay available to the scorer (a pair whose outcome had a precedent is scored with that precedent), and a press release or congress abstract before the cut was not searched for.

### 4. Scoring protocol
One fresh context per pair; the scorer receives this Part A and one pair row only, plus the instruction to use only literature up to the date-cut; no tool access to the web; no other pair is visible, so pairs cannot be scored by contrast. The same scorer model, effort and prompt for all twelve pairs, stated in the run record. After all twelve scores are saved, a separate fresh call shows each pair row alone and asks, in one question, "do you recognise this pair, and if so what is the drug, the gene or disease and the outcome you remember?"; the answer is recorded as identified, partly identified or not identified.

### 5. What a score is not
A score is not a prediction of an outcome, not a probability, and not a ranking of any candidate in the Wwox programme. It exists only to test whether the same four components separate known successes from known failures in this set.
