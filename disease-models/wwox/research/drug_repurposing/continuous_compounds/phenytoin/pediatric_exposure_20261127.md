# Phenytoin | Acute pediatric exposure and the WWOX clinical boundary

context_policy: QUESTION_DRIVEN

## Measured systemic exposure

| Record and context | Denominator and timing | Free parent and what it supports |
| --- | --- | --- |
| [Sathe et al., ESETT pharmacokinetic substudy, Methods and Results/Fig. 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC8089035/) | 27 children across three arms, with 44 total blood samples. Eleven children were assigned intravenous fosphenytoin. Median age across the substudy was 4 years (IQR 2.5–6.5). The target windows were 20–50 and 60–120 minutes from infusion start, and some samples were collected outside the windows. The text does not assign all missing protein-binding measurements by arm. | Observed unbound phenytoin 1.0–2.8 µg/mL (3.96–11.10 µM), with 4%–19% free fraction. Ultrafiltration and LC–MS/MS measured the active parent. The two highest free fractions occurred in children with measurable concomitant valproate. Sparse samples and background treatment limit exposure–response inference. |
| [Bohannon et al., retrospective single-load cohort under six months, Methods and Results/Fig. 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC7541024/) | Two load groups of 12 and 29 infants, with mean sampling 2.62 and 2.95 hours after loading. Only those with a free level within six hours were eligible. The groups had low median albumin and different bilirubin distributions. | Mean free serum phenytoin 2.45 and 2.52 µg/mL (9.71 and 9.99 µM). Nine of 41 exceeded 3 µg/mL and 37 exceeded that laboratory's upper reference of 1.6 µg/mL. Free concentrations overlapped between the two groups. The authors found no significant difference in mean free level according to seizure cessation, with limited power and heterogeneous etiologies. |

The observations in these acute cohorts bracket nominal 8 and 10 µM test points at the systemic scale. The 24 µM SCN8A induced-neuron network comparison is 2.16 times the ESETT observed upper unbound **plasma** value. This quotient is a scale check across experiments. The study's sparse sampling prevents treating that upper value as a physiological ceiling. Acute intravenous prodrug exposure in critical illness also does not establish a sustained oral exposure or local brain concentration in WWOX. Keep serum or plasma, extracellular brain and nominal bath concentrations on separate axes. [Replay](pediatric_exposure.tsv) · [FDA pediatric clinical pharmacology review, study 982-028, p. 56](https://www.fda.gov/media/103872/download)

## Clinical observations in WWOX

Oliver et al. list phenytoin in the trialed-antiseizure-medication histories of **2 of 13** individuals in their multicenter WWOX-DEE cohort. The table documents use amid other treatments. It provides no phenytoin-attributed effect, paired exposure, time-matched comparator or stratified response. The count is a measure of documented exposure in this ascertainment series. It does not support a response denominator. [Oliver et al., Table 2, ASMs trialed (current)](https://onlinelibrary.wiley.com/doi/full/10.1111/epi.17542)

## Mechanistic consequence

Evaluate an exposure-verified low-micromolar test in WWOX and corrected preparations, with preserved first excitatory recruitment and evoked inhibition. Test voltage history before assuming that human 5A/5N splicing explains drug sensitivity. The acute SCN8A induced-neuron assay was primarily excitatory and measured the fraction of spikes in bursts. Its reported genotype-by-treatment interaction at 24 µM does not establish maintained PV recruitment, and overall normalized firing did not show a genotype difference in the reported treatment response. Tissue-level pharmacology and clinical exposure remain separate. [Tidball et al., pp. 3027–3028 and 3034–3036, Fig. 7D/F and Supplementary Fig. 5](https://doi.org/10.1093/brain/awaa247)

Run `python3 replay_pediatric_exposure.py` from this directory to regenerate the comparison. The active moiety is the free-acid-equivalent parent with molecular mass 252.268 g/mol. The arithmetic compares observed ranges and means without pooling the two acute cohorts or making a regimen proposal.
