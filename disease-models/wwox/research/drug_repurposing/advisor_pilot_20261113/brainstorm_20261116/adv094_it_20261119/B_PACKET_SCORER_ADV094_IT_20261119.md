# Scoring packet B (hypothesis-level diagnostic; no dose or recommendation for any agent in any person; not medical advice)

You are a scorer. Read ONLY this file. Do not open any other file, do not use any web, search or PubMed tool, do not look anything up: score from what you know of the literature up to each pair's date-cut, and from nothing later. If you recognise a pair and remember how it ended, ignore that: score only from pre-cut information, and never mention or hint at an outcome in your answer. This is a diagnostic of whether four fixed components separate known successes from known failures; a score is not a prediction, not a probability and not a ranking of anything.

Score each of the twelve pairs INDEPENDENTLY, as if it were the only one you had been given: do not compare pairs, do not rank them, do not carry a judgement from one to another.

## Rubric (rewritten by an independent reader; apply as written)
(a) The four components, rewritten

Use these rules for every pair. Score four components for the one row you are given. Each component is 0, 1 or 2.

- Do not add the four scores together.
- Do not weight them.
- Do not produce an overall figure.
- For each component, write one sentence of justification.
- Each sentence must say what kind of evidence you used. Examples: cell-based, animal model, human tissue, human clinical report, trial, a general mechanism textbook fact.
- Do not give a citation that a reader could not check.

Pathway means the biological quantity named in the row. Examples: activity of a channel, activity of mTORC1, intraneuronal chloride, brain fuel supply, availability of a cofactor. The genotype class's effect means what that genotype or disease does to that quantity. Example: it leaves it too low, too high or blocked.

C1 Target engaged. Question: is there evidence that the agent reaches its target and acts on it?
- Matching system is 2. Matching means the human brain or neurons, or a model of this same genotype class, in the tissue where the endpoint arises.
- Adjacent system is 1. Adjacent means evidence that differs from the matching system in at least one of species, cell type, tissue or age. Examples: a dish of cells expressing the channel, a rodent without the genotype, adult tissue when the row concerns neonates.
- Score 0 when there is no evidence, or when the evidence is against. Evidence against includes evidence that the agent does not reach the tissue.

C2 Direction. Question: does the agent push the pathway the opposite way from the genotype class's effect?
- Directly opposite is 2. Example: the pathway is overactive in the class and the agent inhibits that same pathway.
- Indirect is 1. Indirect means the agent acts upstream or downstream, or through a compensating route.
- Mixed is also 1. Mixed means the evidence points both ways.
- Score 0 when the agent moves the pathway the same way as the genotype class.
- Score 0 and flag `unknown` when the direction is not known.

C3 Phenotype relevance. Question: is there evidence that this pathway bears on the endpoint?
- Score 2 if the evidence comes from this genotype class. That means humans with it, or an animal or cell model of it.
- Score 1 if the evidence comes only from another condition.
- Score 0 if there is no evidence.
- This component concerns the pathway, not the agent. Evidence that the agent itself changes the endpoint in humans belongs to C4.

C4 Transfer. Question: is there human evidence in this genotype class and age group?
- Same class and same age group is 2.
- A related class, or a related age group, is 1.
- No human evidence is 0.

The unknown rule applies to every component. Score 0 and flag `unknown` when you cannot place the component. Never round a score up.

Choices I made where the original is ambiguous:

1. "No evidence" versus "cannot place". The original scores both 0.
   - Choice: score 0 with no flag when you looked and found nothing, or found evidence against.
   - Choice: score 0 and add `unknown` when you cannot tell what the pre-cut literature says. Examples: you cannot tell whether matching-system evidence existed, or you do not know the genotype's effect on the pathway.
   - Why: otherwise a flagged 0 and a plain 0 cannot be told apart, and the unknown flag is there to mark exactly that.
2. "Direction unknown" appears in the 0-definition of C2 and also under the unknown rule.
   - Choice: for C2, flag `unknown` when there is no information at all. Use a plain 0 when evidence shows the same direction.
3. Positive evidence and evidence against at the same level of C1.
   - The original is silent.
   - Choice: score the highest level that has positive evidence. If evidence against exists at that same level and is not clearly outweighed, drop one level.
   - Alternatives: flag `unknown`, or ask the author to settle it.
4. Whether unfavourable human evidence counts for C4.
   - Choice: C4 counts human evidence that the agent changes the endpoint favourably in that class and age group.
   - Human evidence of no effect or worsening scores 0, and the sentence says "against". This is parallel to C1's "evidence against = 0".
   - The wording "evidence for" supports this reading.
   - This is the choice two scorers are most likely to make differently. The author should settle it.
5. "Related" class or age group in C4.
   - Choice: related means the same gene family or mechanism, the same clinical syndrome, or an adjacent age band.
   - If both class and age are unrelated, score 0.
6. Whether agent-in-model evidence counts for C3.
   - Choice: yes, if a model of this class shows the pathway or agent changes the endpoint. Any manipulation of the pathway counts.
7. "Matching" in C1.
   - Choice: matching is the system in which the endpoint is measured. It does not require the same species and cell type and age all at once.

## Date-cut rule
Date-cut rule.
- The table prints a year for each pair. Use only information first published on or before 31 December of that year. Use the earlier of the online date and the print date.
- Earlier reports of the same drug in the same class that fall inside the cut stay available. A pair whose outcome had a precedent is scored with that precedent.
- The author did not search for press releases or congress abstracts dated before the cut. They are not excluded. If you rely on one, name its kind.
- Anything you learned later than the cut, such as later trials, reviews or approvals, must not be used.
- If you cannot tell whether a fact was known by the cut, treat it as unavailable. Score the component 0 and flag `unknown`.

## Output format
Return ONE final message (the harness may not keep files you write). First a tab-separated block headed SCORES with the header line id<TAB>c1<TAB>c2<TAB>c3<TAB>c4 and one line per pair in the order HC-01 to HC-12; each cell is 0, 1 or 2, or the word unknown where you flag it (unknown counts as 0; never round up). Then, for each pair in the order given below, four lines C1 to C4 giving the score, the flag if any, and ONE sentence naming the kind of evidence used (not a citation the reader could not check). Do not add the components, do not weight them, do not give an overall figure.

## The twelve pairs (given in a shuffled order; the ids are what you report under)
| id | class-level descriptor (no names, no outcome) | date-cut (31 December of this year) |
|---|---|---|
| HC-06 | A cofactor vitamin that is inactivated by an accumulating lysine-degradation metabolite, in an inborn error of lysine degradation (loss of an aldehyde dehydrogenase) presenting with neonatal seizures; endpoint: seizure freedom on the vitamin. | 2015 |
| HC-02 | An inhibitor of the nutrient-sensing kinase complex mTORC1, as add-on, in a disorder of constitutive overactivation of that complex (loss of a two-protein repressor); ages 2 to 65 years; endpoint: seizure response rate and frequency. | 2014 |
| HC-12 | A loop diuretic that blocks the chloride importer NKCC1 (to lower intraneuronal chloride and restore GABA inhibition), as add-on to a barbiturate, in full-term newborns with electrographic seizures after perinatal asphyxia; endpoint: reduction of electrographic seizure burden. | 2013 |
| HC-07 | A neuroactive-steroid GABA-A positive allosteric modulator, as add-on, in an X-linked developmental and epileptic encephalopathy from loss of a brain-expressed kinase; ages 2 to 21 years; endpoint: major motor seizure frequency. | 2020 |
| HC-11 | Use-dependent sodium-channel blockers in epilepsies from variants of a brain sodium-channel gene whose variants in this subgroup are truncating or loss-of-function; onset from 3 months of age; endpoint: seizure reduction or freedom. | 2015 |
| HC-05 | A medium-odd-chain triglyceride that supplies an anaplerotic brain fuel, in a disorder of impaired glucose transport into the brain; patients over 1 year old not on a ketogenic diet; endpoint: overall seizure frequency. | 2020 |
| HC-03 | A potassium-channel blocker with sodium-channel activity, in epilepsies from gain-of-function variants of a sodium-activated potassium channel; infants and children; endpoint: at least 50 percent seizure reduction. | 2020 |
| HC-01 | Use-dependent sodium-channel blockers in neonatal-onset epilepsies from loss of function of a voltage-gated potassium channel (Kv7 family) that restrains neuronal firing; neonates and infants; endpoint: seizure control and offset. | 2024 |
| HC-04 | A use-dependent sodium-channel blocker, mostly as add-on, in an infant-onset epileptic encephalopathy attributed to sodium-channel haploinsufficiency; children 2 to 18 years; endpoint: change in each seizure type. | 1996 |
| HC-10 | An inhibitor of the brain cholesterol-24-hydroxylase (lowering a glutamatergic-receptor-potentiating oxysterol), as add-on, in an infant-onset epileptic encephalopathy attributed to sodium-channel haploinsufficiency; ages 2 to 21 years; endpoint: monthly convulsive seizure frequency. | 2024 |
| HC-09 | A high-fat, low-carbohydrate diet supplying ketones as an alternative brain fuel, in a disorder of impaired glucose transport into the brain (heterozygous loss of function of the transporter); children, 2 to 5 years of follow-up; endpoint: seizure freedom. | 2003 |
| HC-08 | A GABA-A positive allosteric modulator that also inhibits cytochrome P450 (raising co-administered clobazam and valproate), as add-on, in an infant-onset epileptic encephalopathy attributed to sodium-channel haploinsufficiency; children; endpoint: clonic or tonic-clonic seizure frequency. | 1998 |
