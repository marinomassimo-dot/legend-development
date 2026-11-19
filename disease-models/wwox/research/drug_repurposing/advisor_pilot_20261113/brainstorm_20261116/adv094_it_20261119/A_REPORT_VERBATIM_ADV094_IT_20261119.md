# Delegate A report, verbatim: rubric rewrite, leak table, recognition probe (ADV-094 item 2)

Delegate A: legend-delegate, claude-sonnet-5-5, effort high (read back from its transcript), fresh, saw only Part A of the scorer sheet (A_PACKET_PARTA_ADV094_IT_20261119.md). Deviation recorded: A was told the probe was coming in the same dispatch as the rewrite (the plan was to ask it after the rewrite returned), and it had seen all twelve rows together. Persisted by IT; not edited. Hypothesis level; not medical advice.

TASK 1 REWRITE

Scope: I read only the Part A sheet. I opened no other file and used no web tool. The probe answers come from memory only.

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

(b) Application instructions, rewritten (sections 3 and 4)

Date-cut rule.
- The table prints a year for each pair. Use only information first published on or before 31 December of that year. Use the earlier of the online date and the print date.
- Earlier reports of the same drug in the same class that fall inside the cut stay available. A pair whose outcome had a precedent is scored with that precedent.
- The author did not search for press releases or congress abstracts dated before the cut. They are not excluded. If you rely on one, name its kind.
- Anything you learned later than the cut, such as later trials, reviews or approvals, must not be used.
- If you cannot tell whether a fact was known by the cut, treat it as unavailable. Score the component 0 and flag `unknown`.
- The author's own derivation is: cut = 31 December of (the year of the paper that fixed the outcome minus two). The reason is that a result can be announced a year or more before its paper. This is the author's setup rule, not something the scorer needs to apply.

Scoring protocol.
- Use one fresh context per pair.
- The scorer receives Part A and one pair row only, plus the instruction to use only literature up to the date-cut. The scorer has no web access and sees no other pair.
- The model, effort and prompt are the same for all twelve pairs. They are stated in the run record.
- Output for each pair is four lines, C1 to C4. Each line gives the score (0, 1 or 2), the `unknown` flag if any, and one sentence with the kind of evidence.
- If you recognise the pair and remember what happened, ignore it. Score only from pre-cut information, and do not mention the outcome. The original does not say this. It is my choice.

Recognition phase.
- The scorer plays no part in this phase.
- After all twelve scores are saved, make a separate fresh call for each row. This is my reading of "each pair row alone".
- Show that row alone, with no section 3. Ask: "do you recognise this pair, and if so what is the drug, the gene or disease and the outcome you remember?"
- Record the answer as identified, partly identified or not identified.
- The original does not define these three classes. My proposed rule:
  - Identified: the drug, the gene or disease, and an outcome are all named, and they are mutually consistent.
  - Partly identified: one or two of the three are named.
  - Not identified: none, or only generic statements.
  - Guessing from the class is not recognition.

Section 5. A score is not a prediction, a probability or a ranking. It only tests whether the four components separate successes from failures.

LEAK TABLE

No row states an outcome in words. A row hints at one only if the quoted words themselves say so, and none do. The entries below are information leaks of other kinds. I list them so that none is mistaken for an outcome.

| Where | Words | Kind of leak |
|---|---|---|
| Sec 3 plus the printed date-cut in every row | "two years before the year of the paper that fixed the pair's outcome" | Arithmetic. Any reader of sec 3 can add 2 to each printed year and get the outcome paper's year. Example: 2014 gives 2016, 2013 gives 2015, 1998 gives 2000. This is the strongest leak. It singles out well-known trials (HC-02, HC-07, HC-08, HC-12) and lets recall fix a specific publication. A scorer who has read sec 3 has it. The recogniser who sees a row alone does not. |
| Sec 3 | "a pair whose outcome had a precedent" | Says some pairs have earlier supporting or failing reports. |
| Sec 3 | "the paper that fixed the pair's outcome" | Confirms every pair has a single outcome paper. |
| Sec 5 | "separate known successes from known failures in this set" | Composition. It tells the scorer the set contains both kinds, which sets a base rate. |
| Sec 1 | "Names of genes and drugs are not given" | The claim is not true as written, and the shortfall can identify pairs. Examples: "Kv7 family", "mTORC1", "NKCC1", "cholesterol-24-hydroxylase", "clobazam and valproate", "loop diuretic", "aldehyde dehydrogenase". |
| HC-11 | "variants in this subgroup are truncating or loss-of-function; onset from 3 months of age" | The subgroup split by variant type and onset age reads like the outcome paper's own stratification. It may be post-cut knowledge, or may sit near the cut. |
| HC-04, HC-08, HC-10 | "attributed to sodium-channel haploinsufficiency" | Hindsight. The cuts are 1996 and 1998. The gene link was not established then, so the descriptor holds post-cut knowledge. |
| HC-04 | "use-dependent sodium-channel blocker ... sodium-channel haploinsufficiency" | The pairing of a blocker with a loss-of-function gene makes the direction visible. This is a mechanism hint, not an outcome. |
| HC-02, 04, 05, 07, 10 | Age ranges "2 to 65 years", "2 to 18 years", "over 1 year old not on a ketogenic diet", "2 to 21 years" | These look like the outcome trial's eligibility criteria. They copy the outcome study's design into the row. |
| HC-09 | "2 to 5 years of follow-up" | Follow-up length is a feature of the outcome report. |
| HC-01 | "seizure control and offset" | Endpoint wording. "Offset" reads as seizures stopping or the agent being withdrawn. |
| HC-06 | "seizure freedom on the vitamin" | The endpoint is worded as if the pair rests on the vitamin working. |
| HC-08 | "(raising co-administered clobazam and valproate)" | Gives a mechanistic reason for an effect. It is not an outcome. |
| HC-10 | "(lowering a glutamatergic-receptor-potentiating oxysterol)" | States the pharmacodynamic action as established. This pre-answers C1 and C2. |
| HC-12 | "to lower intraneuronal chloride and restore GABA inhibition" | States the mechanism as achieved. This pre-answers C2 and C3. |
| HC-01 (cut 2024), HC-10 (cut 2024) | The cut is the end of 2024. | As I recall it, a company announcement of this trial's topline fell within 2024. If so, the cut is after the announcement, and sec 3 says such announcements were not searched for. A scorer with unrestricted recall could be contaminated. I cannot check this without a source. |

TASK 2 PROBE

I answer from memory only, and no lookup was possible. I have seen all twelve rows together, which could not be undone.

| id | classification | what I named | confidence | did other rows help |
|---|---|---|---|---|
| HC-01 | partly identified | Carbamazepine or phenytoin in KCNQ2 neonatal-onset encephalopathy. I remember favourable seizure response in the 2014 to 2019 cohort literature (Pisano and others). I do not recall a specific 2024-or-later paper. The class-level outcome is positive, with seizures controlled in many cases. | Gene and class: high. Specific paper: low. | No. |
| HC-02 | identified | Everolimus add-on in tuberous sclerosis (TSC1/TSC2 loss), phase 3 EXIST-3, Lancet 2016. Outcome: positive. Response rate about 28 to 40 percent on drug versus about 15 percent on placebo, with seizure frequency reduced. | High. | Slightly. The cut 2014 plus 2 = 2016 matched. Alone, the descriptor still points to everolimus in TSC. |
| HC-03 | identified | Quinidine in KCNT1 epilepsy (migrating focal seizures of infancy, ADNFLE). Outcome: disappointing or mixed. Only a minority respond, around 20 to 30 percent in pooled reports. Not convincing as a treatment. | Drug and gene: high. Exact numbers: moderate. | No. |
| HC-04 | identified, with the drug less certain | Lamotrigine, or sodium-channel blockers generally, in Dravet syndrome (SCN1A). Outcome: seizure aggravation, so a negative result. The cut 1996 plus 2 = 1998 matches a report of lamotrigine worsening seizures in severe myoclonic epilepsy of infancy. | Class and outcome: moderate to high. Drug (could be carbamazepine, phenytoin or lamotrigine): moderate. | Yes. HC-08 and HC-10 pinned the disease to Dravet. |
| HC-05 | identified | Triheptanoin in GLUT1 deficiency syndrome. Outcome: the randomised trial missed its primary endpoint of total seizure frequency. Seizures fell, but not significantly versus placebo. | Drug and disease: high. Outcome: moderate to high. | Slightly. HC-09 gave a second GLUT1 anchor. |
| HC-06 | partly identified | Pyridoxine in ALDH7A1 deficiency (pyridoxine-dependent epilepsy, antiquitin deficiency). I know the pair. I do not recall which specific paper the cut points to. Outcome: seizures are controlled in most patients, but neurodevelopmental outcome is often poor and seizure freedom is not universal. | Pair: high. Specific paper and numbers: low. | No. |
| HC-07 | identified | Ganaxolone in CDKL5 deficiency disorder, the Marigold trial, Lancet Neurology 2022. Outcome: positive. Major motor seizure frequency fell about 31 percent versus about 7 percent on placebo. | High. | Slightly. 2020 plus 2 = 2022 matched. |
| HC-08 | identified | Stiripentol with clobazam and valproate in Dravet syndrome (STICLAIR, Lancet 2000). Outcome: positive. Roughly 70 percent responders versus about 5 percent on placebo. | High. | Yes. 1998 plus 2 = 2000. The cross-row contrast with HC-04 helped. |
| HC-09 | identified | Ketogenic diet in GLUT1 deficiency, as in Klepper's reports (2005 or earlier). Outcome: positive. Most children became seizure-free or nearly so. | Class and outcome: high. The exact paper: moderate. | Slightly. The GLUT1 pair gave context. |
| HC-10 | identified | Soticlestat (CH24H inhibitor) add-on in Dravet syndrome (SKYLINE phase 3, ENDYMION extension). I remember a 2024 topline report of a missed primary endpoint, with a non-significant change in convulsive seizure frequency. I am not sure whether a 2026 paper exists. | Drug and class: high. Outcome: moderate to high. | Yes. The Dravet cluster HC-04, HC-08 and HC-10 supported each other. |
| HC-11 | identified | Sodium-channel blockers in SCN2A epilepsy (Wolff and others, Brain 2017). Outcome: in late-onset or loss-of-function SCN2A, blockers do not help and may worsen seizures. They help in early-onset gain-of-function SCN2A. | Gene and class: high. Outcome: moderate to high. | No. |
| HC-12 | identified | Bumetanide with phenobarbital in neonatal asphyxial seizures (NEMO trial, Lancet Neurology 2015). Outcome: negative. No added seizure reduction, with hearing and diuresis safety signals. | High. | Slightly. 2013 plus 2 = 2015 fits. |

Whether the other rows helped:
- Seeing all twelve together helped on HC-04 versus HC-08. The shared Dravet wording made me anchor the disease on all three Dravet rows. In HC-04, the gene is only implied by "attributed to sodium-channel haploinsufficiency". Alone, it could still point at SCN1A, but less sharply.
- The date-cut arithmetic from sec 3 (cut + 2 = paper year) helped on HC-02, HC-04, HC-07, HC-08 and HC-12. A fresh recognition call that shows a row alone, without sec 3, would not have this help.
- I would have recognised HC-02, HC-03, HC-05, HC-07, HC-08, HC-10 and HC-12 from the row alone, with the other rows hidden.
- I recognised HC-01, HC-06, HC-09 and HC-11 at class level only, not by trial.
- The "identified" labels for HC-01, HC-06 and HC-09 rest on class-level literature, not on a specific paper I could name. Treat them as weaker than the rest.
- My recognition of HC-01 and HC-10 is limited by my knowledge cutoff of June 2026.
