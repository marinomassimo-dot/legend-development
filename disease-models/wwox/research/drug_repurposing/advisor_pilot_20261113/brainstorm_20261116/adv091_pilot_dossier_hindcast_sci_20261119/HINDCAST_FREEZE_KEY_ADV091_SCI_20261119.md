# Hindcast freeze, KEY file (never shown to a scorer): identities, source sentences, labels (SCI, ADV-091, 2026-11-19)

Hypothesis level. A diagnostic of a scoring method on known outcomes, not a licence for any use of any agent in any person. Not medical advice. No individual-level information is used or recorded.

Seeded shuffle for the disguised ids: random.Random(20261119) over the table order of build_hindcast_freeze.py. Source of each sentence: the abstract text of the paper, copied from Europe PMC by plain GET on 2026-11-19 (copy held outside git; digests below; full texts NOT read). Each sentence was checked by the script as a verbatim substring of its copy.

## Primary set (12 pairs: 6 POS, 6 NEG)

| id | label | pair | design | PMID | year | date-cut | abstract copy sha256 |
|---|---|---|---|---|---|---|---|
| HC-01 | POS | sodium-channel blockers (carbamazepine, oxcarbazepine) in KCNQ2 loss-of-function disorders | retrospective multicentre cohort, 282 individuals; no proportion in the abstract | 42610455 | 2026 | 2024 | `c5078335bf03561c81b7dc2b6887b3cfdd7eae64f1cb9749be78b49de8854ba3` |
| HC-02 | POS | everolimus add-on in tuberous sclerosis complex, focal-onset seizures | randomised placebo-controlled phase 3 (EXIST-3), 366 patients | 27613521 | 2016 | 2014 | `22f71305e12cf171f5db58822be1c2393c68a5ed4c60974e59a4b3d8d358a1f4` |
| HC-03 | NEG | quinidine in KCNT1-related epilepsies | systematic review of 82 patient records from 27 studies (case-level literature) | 35940594 | 2022 | 2020 | `7231151958d7ab16a349240a2a88134c5695cbbfcfe8d5e52c990e1652bc29d0` |
| HC-04 | NEG | lamotrigine in severe myoclonic epilepsy of infancy (Dravet syndrome; by syndrome, the gene is not named in this source) | open case series, 21 patients | 9596203 | 1998 | 1996 | `f07c29c97354a3b52d16dc819f384253a4643de0cbfae093c39fc1e376942c26` |
| HC-05 | NEG | triheptanoin in GLUT1 deficiency syndrome, drug-resistant seizures, not on a ketogenic diet | randomised placebo-controlled trial, 36 patients | 35441706 | 2022 | 2020 | `2aadc4a7f5be47f806e471687c682d3f5d6488f7fac842f5f98e111c96e918dc` |
| HC-06 | POS | pyridoxine in pyridoxine-dependent epilepsy due to ALDH7A1 deficiency | retrospective series, 11 patients (the disease is defined by pyridoxine response: circular by construction) | 27882480 | 2017 | 2015 | `38f71c597d6af1c254af6e4e0af62d062025865bd24f63be02d2624c53049a87` |
| HC-07 | POS | ganaxolone add-on in CDKL5 deficiency disorder | randomised placebo-controlled phase 3 (Marigold), 101 patients | 35429480 | 2022 | 2020 | `e4d7177a7d9a25b2940ca9c191465142eae8167525ca11f3a04b696315299cc9` |
| HC-08 | POS | stiripentol add-on in severe myoclonic epilepsy of infancy (Dravet syndrome; by syndrome, the gene is not named in this source) | randomised placebo-controlled add-on trial, 41 children | 11089822 | 2000 | 1998 | `fdab674213f49797f07ec903a3fa55099be6ec6eb883f3a5a115f79e260d0baf` |
| HC-09 | POS | ketogenic diet in GLUT1 deficiency syndrome | prospective follow-up cohort, 15 children | 16217704 | 2005 | 2003 | `41a0a397f9588591539780255dffedf9a396beae8f793bfa0b3874aabd430a9f` |
| HC-10 | NEG | soticlestat add-on in Dravet syndrome | randomised placebo-controlled phase 3 (SKYLINE), 144 participants; primary endpoint not met (p = .061); borderline | 41784472 | 2026 | 2024 | `540853a2d349871eee53c6fa2ab3428e84169c559df67d7886e0e4c3616256a4` |
| HC-11 | NEG | sodium-channel blockers in SCN2A-related epilepsies with onset from 3 months (loss-of-function class) | retrospective review of 66 patients with SCN2A variants (late-onset, truncating group) | 28379373 | 2017 | 2015 | `7cb511cc31afc23e9ce21f0a280fd8080a4dee9605c97c75ad010b796dee2a1f` |
| HC-12 | NEG | bumetanide add-on to phenobarbital for seizures in neonatal hypoxic-ischaemic encephalopathy (not a genetic class) | open-label phase 1/2 dose-finding trial, 14 infants | 25765333 | 2015 | 2013 | `446fe36e178ffbcea4dbf2bc1fd7af4d2fd731d8ab1a7540d8f7e1dfa66c3b1a` |

## Source sentence per pair (verbatim; the sentence that fixed the label)

* **HC-01** (nachannel_blockers_kcnq2, POS): "SCBs, especially carbamazepine (CBZ) and oxcarbazepine (OXC), emerged as the most effective ASMs in both LOF groups."
* **HC-02** (everolimus_tsc, POS): "The response rate was 15·1% with placebo (95% CI 9·2-22·8; 18 patients) compared with 28·2% for low-exposure everolimus (95% CI 20·3-37·3; 33 patients; p=0·0077) and 40·0% for high-exposure everolimus (95% CI 31·5-49·0; 52 patients; p<0·0001)."
* **HC-03** (quinidine_kcnt1, NEG): "Records of 80 patients with 33 KCNT1 mutations were analysed, of which 20 patients had gained ≥50% seizure reduction due to quinidine therapy."
* **HC-04** (lamotrigine_sme, NEG): "LTG induced worsening in 17 (80%) patients, no change in three, and improvement in one."
* **HC-05** (triheptanoin_glut1, NEG): "A median 12.6% reduction in overall seizure frequency was observed in the triheptanoin arm relative to baseline, and a 13.5% difference was observed relative to placebo (p = .58)."
* **HC-06** (pyridoxine_aldh7a1, POS): "73% of the patients became seizure free on pyridoxine."
* **HC-07** (ganaxolone_cdkl5, POS): "There was a median percentage change in 28-day major motor seizure frequency of -30·7% (IQR -49·5 to -1·9) in the ganaxolone group and of -6·9% (-24·1 to 39·7) in the placebo group (p=0·0036)."
* **HC-08** (stiripentol_dravet, POS): "15 (71%) patients were responders on stiripentol (including nine free of clonic or tonic-clonic seizures), whereas there was only one (5%) on placebo (none were seizure free; stiripentol 95% CI 52.1-90.7 vs placebo 0-14.6)."
* **HC-09** (ketogenic_glut1, POS): "10/15 patients remained seizure-free on the ketogenic diet in monotherapy."
* **HC-10** (soticlestat_dravet, NEG): "Median change from baseline in convulsive seizure frequency over the full treatment period was -8.64% with placebo (n = 71) and -22.16% with soticlestat (n = 73), a difference of -15.64% (p = .061)"
* **HC-11** (nachannel_blockers_scn2a_late, NEG): "In contrast, sodium channel blockers were rarely effective in epilepsies with later onset (≥3 months) and sometimes induced seizure worsening."
* **HC-12** (bumetanide_neonatal_hie, NEG): "The trial was stopped early because of serious adverse reactions and limited evidence for seizure reduction."

## Read and not in the primary set (reserve; not scored unless the sheet's section 1 says so)

* **fenfluramine_dravet** (POS, fenfluramine add-on in Dravet syndrome (same disease as stiripentol: skipped by the one-positive-per-disease rule); randomised placebo-controlled trial, 119 patients; PMID 31862249, 2019): "In Dravet syndrome, fenfluramine provided significantly greater reduction in convulsive seizure frequency compared with placebo and was generally well tolerated, with no observed valvular heart disease or pulmonary arterial hypertension."
* **cannabidiol_dravet** (POS, cannabidiol add-on in Dravet syndrome (same disease as stiripentol: skipped by the one-positive-per-disease rule); randomised placebo-controlled trial, 120 patients; PMID 28538134, 2017): "The median frequency of convulsive seizures per month decreased from 12.4 to 5.9 with cannabidiol, as compared with a decrease from 14.9 to 14.1 with placebo (adjusted median difference between the cannabidiol group and the placebo group in change in seizure frequency, -22.8 percentage points; 95% confidence interval [CI], -41.1 to -5.4; P=0.01)."
* **nachannel_blockers_scn2a_early** (POS, sodium-channel blockers in SCN2A-related early infantile epilepsies (the other half of the SCN2A source: same paper as an included negative, so left out of the primary set); retrospective review of 66 patients with SCN2A variants (early-onset, gain-of-function group); PMID 28379373, 2017): "We find that the use of sodium channel blockers was often associated with clinically relevant seizure reduction or seizure freedom in children with early infantile epilepsies (<3 months), whereas other antiepileptic drugs were less effective."
* **phenytoin_scn8a** (POS, phenytoin in SCN8A-related epilepsy with a missense variant (a second sodium-channel-blocker positive: reserve); case series, 4 patients; PMID 26252990, 2016): "Herein, we describe 4 patients with a missense SCN8A mutation and epilepsy who all show a remarkably good response on high doses of phenytoin and loss of seizure control when phenytoin medication was reduced, while side effects were relatively mild."

## Dropped from the original list of 13 (ADV-091 addendum: number dropped stated)

**1 dropped:** trofinetide on seizures in Rett syndrome. No source sentence stating a seizure outcome for the drug was found by one Europe PMC title search of 2026-11-19 (the hits were a case report, a computational paper and economic or safety papers), and the pivotal trial's endpoints are not seizure frequency, so the pair fails the one-endpoint-class rule as well as the reading rule. Absence of a source here is one route only. **Substituted, not dropped:** the original pair 'sodium-channel blockers in SCN1A' was read as lamotrigine in severe myoclonic epilepsy of infancy (the source names the drug and the syndrome, not the gene). **Added after reading (not on the original list):** soticlestat in Dravet syndrome, triheptanoin in GLUT1 deficiency, quinidine in KCNT1, to give the negatives a count equal to the positives.

