# Sheet batch 11: BATCH11_bridge_Ttype_apinocaltamide_ulixacaltamide_TTA-A2_HE_20261120.md
Each numbered unit is a sentence of the repository sheet, in order. L = line in the sheet.


## ADV-102 batch 11: T-type calcium channel compounds inside the bridge class: apinocaltamide, ulixacaltamide (Z944), TTA-A2 (HE, 2026-11-20)
U11.1 (L5) **Why TTA-A2 and not TTA-P2 (ADV asked for the choice by brain and juvenile or pup data).**
U11.2 (L5) A title-and-abstract search with exact tags (`"TTA-A2"[tiab]` 32 records, `"TTA-P2"[tiab]` 38) found the in vivo central work for TTA-A2 (a mouse arousal and slow-wave sleep study, PMID 20682849, and a mouse maximal-electroshock seizure study, PMID 26456350, both abstracts read) and, for TTA-P2, spinal, peripheral and slice work (pain, entorhinal and thalamic neurons; titles read).
U11.3 (L5) No record for either carries a juvenile, neonatal, pup or postnatal term together with the compound name (one record in all, a 2024 structural paper).
U11.4 (L5) So neither has pup data by these routes; TTA-A2 is chosen because its indexed in vivo record is central (behaviour and seizure endpoints).
U11.5 (L5) TTA-P2 is described as a comparator where its rows add something (below).

## Identity (structure keys first)
U11.6 (L8) | Agent | Resolution | ChEMBL read | Structure key |
U11.7 (L10) | apinocaltamide (ACT-709478) | `compound_identity.py` NAME_EXACT for both names (a ChEMBL and a DGIdb record agree) | CHEMBL4217292, max phase 2 in the molecule record | PubChem CID 118560618, InChIKey LSYANGLAZUZYFX-UHFFFAOYSA-N |
U11.8 (L11) | ulixacaltamide (Z944, PRAX-944) | NAME_EXACT for ulixacaltamide; Z944 resolves to the same structure by PubChem | CHEMBL3934636, max phase 1 in the molecule record (the record lags: a phase 3 registration exists, below) | CID 44540045, InChIKey JOCLITFYIMJMNK-UHFFFAOYSA-N |
U11.9 (L12) | TTA-A2 | not run to the end by name (a request timed out); resolved by structure through PubChem then ChEMBL | CHEMBL1684954 (no preferred name stored) | CID 53317097, InChIKey GEYDMBNDOVPFJL-CYBMUJFWSA-N (the R form) |
U11.10 (L13) | TTA-P2 (comparator) | by structure | CHEMBL488817 (no preferred name stored) | CID 24893979, InChIKey DKNDOKIVCXTFHJ-HNNXBMFYSA-N (the S form) |

## COMPARABLE?
U11.11 (L16) **Each agent's T-type potency is one origin, quoted.**
U11.12 (L16) Apinocaltamide: all 24 ChEMBL rows come from ONE document (CHEMBL4177680, the 2017 discovery paper), so every figure below is that paper's, once.
U11.13 (L16) Ulixacaltamide: IC50 37, 73 and 86 nM (Cav3.1, 3.2, 3.3) appear in three documents (two 2016, one 2023), one as "calcium influx" and one as "manual patch clamp", with identical values: read as the same numbers transcribed into more than one record, **not as two methods agreeing**.
U11.14 (L16) TTA-A2: Cav3.2 92 nM appears again in a 2022 document (a quotation of the 2011 value).
U11.15 (L17) **Across agents: not set in one order from the rows.**
U11.16 (L17) The assays differ (a calcium-flux plate assay with 3 minutes of pre-incubation for apinocaltamide, a calcium-influx assay and a patch clamp for ulixacaltamide, voltage clamp at fixed holding potentials for TTA-A2) and the documents are from different laboratories and years (2008 to 2017).
U11.17 (L17) Cav3.3 (alpha1I) is the one subtype with a plate-assay value for three agents: apinocaltamide 7.5 nM (2017), ulixacaltamide 86 nM (2016), TTA-P2 82 nM (2008); the ordering is suggestive and **not a comparison**, because no document tests two of them.
U11.18 (L18) **One within-document comparison is available and valid: TTA-P2 against the anchor.**
U11.19 (L18) Document CHEMBL1140166 (2008, the same plate assay at alpha1I) holds TTA-P2 at 82 nM and ethosuximide at more than 5 mM (batch 1; ChEMBL flags that value "outside typical range"): at least about 60,000-fold on one channel subtype in one assay.
U11.20 (L18) It says the two differ in potency by orders of magnitude on a T-type channel in that assay; it is not an exposure comparison and not a statement about efficacy.
U11.21 (L19) **State dependence is not comparable across rows.**
U11.22 (L19) TTA-A2: plate assay 9.4 nM at a depolarised state against 384 nM at a hyperpolarised state (about 41-fold, 2010, the direction the 2010 abstract describes: stabilises inactivated channels), but a patch-clamp row for Cav3.3 gives 98 nM at -80 mV and **3.7 nM at -100 mV** (2011), the opposite direction.
U11.23 (L19) The two do not agree in sign and one may be mislabelled: **unresolved, not used**.

## Apinocaltamide (CHEMBL4217292), first
U11.24 (L22) **Potency (24 rows, one document, 2017):** human recombinant Cav3.1, 3.2, 3.3 in HEK293 cells, plate assay with 3 minutes of pre-incubation: IC50 6.4, 18 and 7.5 nM; the same channels in rat 16, 13 and 1.8 nM, in mouse (Cav3.1 6.4, Cav3.2 40 nM), dog (20, 33 and 3.4 nM) and cynomolgus monkey (Cav3.2 19 nM): species values within about 3-fold of the human ones (dog Cav3.1 3.1-fold) except rat Cav3.3 (IC50 4-fold lower than human), the largest difference.
U11.25 (L22) Binding to the inactivated state of human Cav3.3 by whole-cell patch clamp in CHO cells: Ki 20 nM.
U11.26 (L22) **Selectivity as measured:** L-type Cav1.2 IC50 2.41 microM (about 130-fold above Cav3.2); hERG 5.5 microM (patch clamp); cytochrome P450 3A4 46 to 51 microM; other P450 isoforms 14 to above 100 microM.
U11.27 (L22) A panel of other targets was not found by these routes (selectivity beyond these rows is the 2025 abstract's statement of "no relevant activity on other targets", not a row).
U11.28 (L23) **Exposure, human (abstracts read):** healthy adult males, single oral doses (first-in-man, 65 subjects, PMID 31004346): maximum plasma concentration within 3 to 4 hours up to a low dose step and 20 to 28 hours above it; terminal half-life 36 to 43 hours; exposure less than dose-proportional; a 1.6-fold higher peak with food; **saliva correlated with plasma** (a significant correlation).
U11.29 (L23) Multiple dosing (46 healthy adults of both sexes, PMID 31994022): half-life 45 to 53 hours, steady state after 5 to 7 days, accumulation about three-fold.
U11.30 (L23) Matrix is plasma (total concentration; protein binding not read).
U11.31 (L24) **Exposure, animal (what the abstracts say, and what they do not):** the 2017 discovery paper (PMID 29116786) names brain penetration as an optimisation goal ("brain-penetrating"); the 2025 rodent paper (PMID 40165594) says some effects needed a higher concentration.
U11.32 (L24) **Not obtainable by a free route:** species, age, matrix (brain, plasma, CSF), total or free concentration and any juvenile value, because both full texts are not open (Europe PMC: not open access; no PMC copy).
U11.33 (L24) No juvenile or pup study was found.
U11.34 (L25) **Efficacy context (one origin, sponsor-affiliated authors per IT's earlier note):** 2025 rodent paper abstract: suppressed spike-and-wave discharges in two absence models (WAG/Rij and GAERS rats) with efficacy equivalent to or better than first-line monotherapy, reduced severity in an audiogenic mouse model and in a mouse electroshock threshold test "albeit at higher concentration", synergy with valproate, **no effect on focal-onset seizures in a rat kindling model**.
U11.35 (L26) **Harm signals (abstract-level):** most frequent adverse events dizziness, somnolence and headache; a tolerability signal at the first multiple-dose level, handled by starting lower and up-titrating; weak induction of intestinal cytochrome P450 3A4 (midazolam exposure lower, 1-hydroxymidazolam unchanged); no treatment-related effect on vital signs, laboratory tests or ECG in the healthy-subject studies.
U11.36 (L26) Nothing about children.
U11.37 (L27) **Trials (ClinicalTrials.gov API v2, `ACT-709478`: 3 studies; `apinocaltamide`: 0):** two phase 1 healthy-subject studies (completed) and one phase 2 in photosensitive epilepsy (completed, 5 participants, adults 18 years and above).
U11.38 (L27) Results and any pediatric registration were **not found by these routes** (a registry search by name only).
U11.39 (L28) **Label:** none (investigational).

## Ulixacaltamide (Z944, PRAX-944; CHEMBL3934636)
U11.40 (L31) **Potency (9 rows, three documents, one origin):** human Cav3.1, 3.2, 3.3 IC50 37, 73 and 86 nM (see COMPARABLE?).
U11.41 (L31) **Not found by these routes:** a selectivity or off-target panel under this id (all nine rows are the three channels); a species other than the recombinant human channels; a state-dependence row.
U11.42 (L32) **Exposure:** PubMed titles and abstracts: the 2012 absence-seizure paper (PMID 22344687, Z941 and Z944 in GAERS rats; thalamic-slice burst firing attenuated; 85 to 90 per cent seizure suppression) gives efficacy, **no concentration in its abstract**. `(Z944 OR ulixacaltamide) AND (brain OR plasma OR pharmacokinetic OR exposure OR CSF)`: 7 records, none an exposure study by its title.
U11.43 (L32) **Not found by these routes:** any rodent brain or plasma concentration (species, age, matrix, total or free) and any human pharmacokinetic figure; both would need full texts or sponsor documents that are not open.
U11.44 (L33) **Harm signals:** none found (the single safety-tagged record is a 2026 essential-tremor review, title read).
U11.45 (L33) **Off-target note, titles only:** a 2026 paper reports inhibition of Cav1.4 channels by Z944 and ML218 (PMID 41489546, title read, not read further).
U11.46 (L34) **Trials (ClinicalTrials.gov, `PRAX-944`, 3 studies; `Z944` and `ulixacaltamide` by name: 0 and 1):** two phase 2 studies (completed, 24 and 133 participants) and one phase 3 (recruiting, 1,000 participants), all in essential tremor and all adults 18 years and above.
U11.47 (L34) **No epilepsy and no pediatric study was found.**
U11.48 (L34) Results not read.
U11.49 (L35) **Label:** none (investigational).

## TTA-A2 (CHEMBL1684954), preclinical tool
U11.50 (L38) **Potency (17 rows, three documents):** voltage clamp at -80 mV: Cav3.1 89 nM, Cav3.2 92 nM, Cav3.3 98 nM (2011); L-type Cav1.2, P/Q-type Cav2.1, N-type Cav2.2 and R-type Cav2.3 all above 30 microM (about 300-fold selectivity, as the 2010 abstract states); hERG and an L-type binding row above 10 microM; Ki 1.2 nM for binding to Cav3.3 (one binding row, repeated in two documents: one origin).
U11.51 (L38) The 2010 abstract adds use dependence on 3 Hz stimulation and preferential interaction with inactivated channels.
U11.52 (L38) See COMPARABLE? for the unresolved state-dependence rows.
U11.53 (L39) **Exposure (abstracts read, PMIDs 20682849 and 26456350):** central effects in wild-type mice (suppression of active wake and more slow-wave sleep; absent in mice lacking Cav3.1 and Cav3.3; protection against tonic seizures in a maximal-electroshock model, absent in Cav3.2 knockouts) show that the compound reaches the brain functionally.
U11.54 (L39) **Not obtainable by a free route (full texts not open) and not found by these routes:** a measured brain, plasma or CSF concentration, the route and the species ages (the abstracts say "mice"; adult is likely but not stated).
U11.55 (L39) No juvenile or pup study.
U11.56 (L40) **Harm signals:** none found by these routes beyond the selectivity rows above.
U11.57 (L41) **Trials and label:** none (a research tool).

## TTA-P2 (CHEMBL488817), comparator rows only
U11.58 (L44) 8 ChEMBL rows (2008, two documents): alpha1I (Cav3.3) 82 nM in the plate assay; **off-target rows that a within-class comparison should carry:** sigma receptor binding Ki below 100 nM (a ceiling, not a value), sodium-channel site 2 IC50 1.9 microM, hERG 2.9 and 3.8 microM, L-type 6.3 microM, Nav1.5 84 microM.
U11.59 (L44) The sigma-receptor row is the same order of magnitude as the T-type potency: **a measured off-target of the comparator that the other three lack rows for** (their absence is "not found by these routes", not a clean profile).
U11.60 (L44) No central exposure record by title; no juvenile record.

## What changes for the compound-level comparison
U11.61 (L47) **Inside the T-type class, three agents have the same stated target and no common assay**, so a potency ranking cannot be made from the rows; the one valid within-document anchor comparison is TTA-P2 against ethosuximide in one assay (orders of magnitude, on potency only).
U11.62 (L48) **Apinocaltamide has the richest human pharmacokinetic and tolerability data and no open animal exposure figure; ulixacaltamide has none of either by these routes; TTA-A2 has central activity in mice and no concentration.**
U11.63 (L48) The brain-exposure side that SCI's exposure-effect choice needs is therefore **not obtainable by a free route for all three**; the ethosuximide anchor (adult mouse total brain value, batch 1) remains the only measured brain figure in the class.
U11.64 (L49) **Age:** no pup or juvenile record for any of the four; all registered human studies of the first two are adults (18 years and above), and none is pediatric.
U11.65 (L50) **One-origin flags carried:** apinocaltamide potency (one document); ulixacaltamide potency (the same three numbers in three records, two techniques); TTA-A2 Ki 1.2 nM and Cav3.2 92 nM (quoted again).

## Dated addition, 2026-11-20 (HE, after SCI's note that earlier T-type material is already in the repository)
U11.66 (L53) I wrote the sheet from the free routes (ChEMBL, PubMed abstracts, ClinicalTrials.gov, Europe PMC flags) and did not first read the repository's own T-type lane, which is a miss on the "check what is held before saying not found" rule.
U11.67 (L53) The held material is `advisor_pilot_20261113/brainstorm_20261116/adv052_ttype_he_20261118/` (HE, ADV-052: a table of 21 T-type studies including apinocaltamide, PMIDs 31004346 and 40165594, and Z944, PMID 26274319), `adv064` rechecks, card H01 and the Sakkaki 2016 rows in `it_adv051`.
U11.68 (L53) Two things from it belong beside this sheet: (1) **Z944 (ulixacaltamide) was not effective at suppressing seizures in fully kindled adult rats compared with vehicle** (PMID 26274319, Casillas-Espinosa 2015, receipt in `adv052_ttype_he_20261118/receipts_staged/`): an efficacy limit of a focal-onset model that matches apinocaltamide's no-effect-on-focal-seizures statement above, and one this sheet did not carry; (2) that lane's own conclusion: no infant or under-3-year datum for any agent in the set.
U11.69 (L53) Whether any of the held files fills a "not found by these routes" line for brain exposure was not checked by me; SCI is checking and reports each correction with its source.
U11.70 (L53) Nothing above is withdrawn.

## Dated correction, 2026-11-20 (HE, after SCI's comparison and ADV's request): the harm fields of this sheet were searched too narrowly
U11.71 (L56) The harm lines above were searched as the label, the clinical-trial registry and the first papers.
U11.72 (L56) A search with harm terms (sedation, locomotor, ataxia, adverse effect, toxicity, tolerability) over each agent's name, run afterwards, changes three lines.
U11.73 (L56) The original wording above is left as written.
U11.74 (L57) **Ulixacaltamide (Z944): "none found" is wrong.**
U11.75 (L57) Casillas-Espinosa 2015 (PMID 26274319, PLoS One, open full text, PMC4537250; read by me in the full text): in amygdala-kindled adult rats Z944 at 30 mg/kg produced "slight sedation and slow movement" not statistically different from vehicle, and the animals "showed mild adverse effects (score 1)"; SCI reports marked sedation at 100 mg/kg (I read the sentence that the animals were "sedate and with reduced movement around the cage" at the top dose; the dose-by-dose table was not re-read by me).
U11.76 (L57) The same paper adds the efficacy limit already noted above (not effective in fully kindled rats; it slowed kindling progression).
U11.77 (L57) Psychopharmacology 2018 (PMID 30251162, abstract read): at the highest dose of the three tested Z944 alone produced subtle impairments of a touchscreen learning task, and it blocked MK-801-induced hyperlocomotion at a middle dose.
U11.78 (L57) **Within-document ethosuximide arms the sheet did not carry:** (a) Casillas-Espinosa 2015 gave Z944 at four doses, ethosuximide and carbamazepine to the same rats in a randomised crossover (abstract), so Z944 against ethosuximide is comparable inside that document, in adult rat kindling only; (b) Epilepsia Open 2026 (PMID 42274296, abstract read: adult Gabrb3+/D120N mice, a within-subjects crossover of ethosuximide 200 mg/kg, ulixacaltamide 60 mg/kg and cannabidiol; all three reduced atypical-absence seizure incidence and duration; the abstract gives no percentages, SCI reads "-64 per cent incidence for both" and I have not re-read it).
U11.79 (L57) Doses here are animal research doses, not recommendations.
U11.80 (L58) **TTA-A2: "none found" is wrong.**
U11.81 (L58) The 2009 J Clin Invest paper (PMID 19451696, abstract read) reports that TTA-A2 acutely **increased sleep, lowered body core temperature, prevented high-fat-diet weight gain, and in obese rodents reduced body weight and fat mass while increasing lean muscle mass**; Cav3.1-knockout mice were also resistant to diet-induced weight gain.
U11.82 (L58) The 2010 paper's suppression of active wake and promotion of slow-wave sleep (above) is the same central effect.
U11.83 (L58) These are class-level effects of T-type blockade, not tolerability findings of a trial, and they bear on the repository's growth and glycaemia need: a weight or body-temperature effect of a T-type blocker in a pup that is already small is a reading to make before any comparison, not a clean profile.
U11.84 (L59) **Apinocaltamide: unchanged.**
U11.85 (L59) The harm-term search returned three records, all already read (the two phase 1 abstracts, whose adverse events are listed above, and a patent review, title read).
U11.86 (L59) The 2017 discovery abstract names an Ames-negative aminopyrazole metabolite as a design goal; no harm finding followed from it.
U11.87 (L59) No preclinical sedation or motor figure was found by these routes.
U11.88 (L60) **Cards:** no card in `cards/` quotes "no harm signal" for these agents (card H01, apinocaltamide, already carries the tolerability facts: dizziness, somnolence, headache and a dose reduction after a tolerability signal in the first multiple-dose cohort); this correction adds sedation and weight facts for the other two agents that no card holds.
U11.89 (L61) **Pattern, for the next sheets:** a harm field is searched in three passes (label and registry; the agent name with harm terms; the agent name with the in vivo behavioural and metabolic readouts of its target class) and the repository's own earlier lane is read first.

## Second dated correction, 2026-11-20 (HE; items from SCI's message, with what I checked myself)
U11.90 (L64) **TTA-A2, maximal-electroshock line above is misread by me.**
U11.91 (L64) I wrote "protection against tonic seizures in a maximal-electroshock model, absent in Cav3.2 knockouts".
U11.92 (L64) The abstract (PMID 26456350, re-read now) says TTA-A2 was given to mice and protected against tonic seizures, and that "similar results were obtained for Cav3.1-/- mice, which were less prone to develop tonic seizures in the MES test, but not for Cav3.2-/- mice": that is the knockouts' OWN phenotype (Cav3.1-/- less prone, Cav3.2-/- not), not TTA-A2 given to knockouts.
U11.93 (L64) The sentence above stays as written; read it as corrected here.
U11.94 (L64) The arousal paper (PMID 20682849) is different: there the effect was absent in mice lacking Cav3.1 and Cav3.3, which is a drug-in-knockout statement and stands.
U11.95 (L65) **Ulixacaltamide within-document arm and sedation:** as in the first correction; SCI reports the Harman 2026 figure (-64 per cent incidence for ethosuximide and for ulixacaltamide; PMC13395050, Results 3.2) and the dose-dependent sedation (slight at 30, marked at 100 mg/kg) from held full texts: I did not re-read those two passages and they remain SCI's readings.
U11.96 (L66) **TTA-P2:** SCI adds a mouse PTZ record in an ethanol-withdrawal model (Masicampo 2018, PMID 29912275, abstract level); I did not read it.
U11.97 (L66) The TTA-P2 comparator paragraph above lists ChEMBL rows only and is not a complete record of its in vivo use.
