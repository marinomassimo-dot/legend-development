# IT5 P5: species, interaction type and quantitative pharmacology on three bounded cases (scientist-b, 2026-10-29)

Non-canonical research material. Not medical advice; no efficacy claim; association is not modulation is not rescue; nothing here changes the four scientific current files. Concentrations and mouse amounts appear only in the TSV tables, as assay conditions of published experiments (research material, not a recommendation); card text carries none. No e-mail address was sent anywhere, no registration, no spend, no keyed API (Guide to Pharmacology was read from the public CSV downloads already in the catalogue cache; ChEMBL REST keyless at one call per second; Europe PMC / PubMed keyless). The Guide-to-Pharmacology web services were not used.

## Tables (TSV; columns identical in the three files)

`case, compound, compound_id, target, target_level, target_species_label, assay_species_or_prep, preparation, assay_type, measure, relation, value, unit, essential_conditions, source_document, source_assay, pubmed_id, source_kind, card, note`

* `target_species_label` is what ChEMBL/GtoPdb attach to the target; `assay_species_or_prep` is what the assay record itself says. They differ in several rows, and that difference is itself a finding (case 1).
* `source_kind`: `primary_paper_curated_by_ChEMBL` (ChEMBL transcribed a paper; the paper was not re-read unless the depth table says so), `patent_or_unpublished_via_ChEMBL`, `review_via_ChEMBL`, `review_cited_by_GtoPdb`, `review_text_read`, `primary_abstract_only`, `primary_text_partial_read`, `computed_from_curated_primary`, `negative_result`.
* Relations and units are conserved as deposited (`=`, `>`; nM as ChEMBL standardises; `/min`, `per mM per min` unchanged). Ki, KI (inactivation), IC50, EC50 and flux/patch-clamp values are never merged; assay type is a column.

| File | Case | Card | Rows |
|---|---|---|---|
| `abat_gabaat_h02.tsv` | 1: vigabatrin, CPP-115, OV329 at GABA-AT | H02 | 29 |
| `ttype_cav3_h01.tsv` | 2: T-type channels, apinocaltamide against ethosuximide (and two comparators) | H01 | 47 |
| `proteostasis_pba_a01.tsv` | 3: 4-phenylbutyrate and bile-acid chaperones, HDAC potency against the concentrations used | A01 | 35 |

## Why these three (chosen by the missing datum)

1. **H02 / ABAT.** The card said CPP-115 has "a lower inhibition constant than vigabatrin (a curated database value, in vitro enzyme level)". Missing: what kind of constant, on which species' enzyme, from which source, and whether the size of the gap is reproduced. This decides how much weight the "sibling" thread can bear.
2. **H01 / T-type (not the GluN2A/GluN2B pair).** The NMDA question was weighed and set aside: F01 asks for a graded block of the whole receptor against perampanel, and its next measurement does not depend on subunit identity, so GluN2A versus GluN2B selectivity would not move it today. H01's whole design rests on ethosuximide being a T-type effect, and nobody had put the two drugs' potencies, species and states side by side. Missing: ethosuximide's potency at Cav3.x and whether the amount given to the pups can be near it; apinocaltamide's isoform spread and state dependence.
3. **A01 / PBA and bile acids.** The card says "Potency ... UNKNOWN" and argues over chaperone versus HDAC action. Missing: any number for either mechanism, and the concentrations the cited papers actually applied.

## Depth of each reading (what was and was not read)

| Source | Depth |
|---|---|
| ChEMBL activity, assay and document records (all three cases) | metadata and deposited values read through REST on 2026-10-28/29; the papers behind them were NOT read unless listed below |
| GtoPdb 2026.3.1 `interactions.csv` (catalogue cache) | rows for ligands 8284, 4821, apinocaltamide, butyric acid etc. read in full |
| Pan et al 2012 (PMID 22128851, PMC3257419) | body read (PubMed full text); supplement not opened |
| Silverman 2012 perspective (PMID 22168767, PMC3266980) | body read |
| Shen et al 2020 (PMID 33062178, PMC7549257) | abstract only (full text returned empty); values taken from ChEMBL (documents CHEMBL4725441) |
| Pan 2003 (PMID 14640537), Choi 2002 (PMID 12238932) | NOT read (closed); values via ChEMBL only; the PMC page for 22128851 was behind a captcha on direct fetch and was not circumvented |
| Gomora 2001 (PMID 11641441), Lacinova 2005 (PMID 16096350) | abstract only |
| Sponsor discovery paper for apinocaltamide (PMID 29116786) | NOT read; values via ChEMBL CHEMBL4177680 |
| Shah 2025, DeLeeuw 2026, Song 2026, Delahanty 2026, Guiberson 2018 | local full texts in `files/fulltext`, sentences naming a concentration located by pattern and read in context; not re-read as whole papers (earlier readings carry receipts) |
| Cheng 2020 ethosuximide amount | repository manifest/card record; not re-read here |

## Case 1: GABA-AT (ABAT), card H02

* **Kind of constant.** For all three compounds the "Ki" values are KI of mechanism-based inactivation (the concentration at half the maximal inactivation rate), paired with kinact and kinact/KI. They are not equilibrium inhibition constants and not IC50s; comparing them with competitive Ki values would be wrong. The only IC50 rows (vigabatrin rat and mouse homogenate, two screening-type papers; OV329, a 2023 review) depend on preincubation and are kept separate.
* **Species and preparation.** Every primary measurement behind the compared constants is pig or rat or mouse brain enzyme, or has no recorded species. GtoPdb labels CPP-115 (9.7 uM) and vigabatrin (850 uM) as "Human"; the CPP-115 figure traces to the Silverman 2012 perspective (a review), and the identical vigabatrin figure traces in ChEMBL to Choi and Silverman 2002 whose assay organism is recorded as Cavia porcellus, with the target mapped to human. ChEMBL's "Homo sapiens" vigabatrin 3.2 mM rows are, in the 2012 paper, a figure quoted from earlier work, and in two other documents patent text. **No measurement on a human enzyme was found for vigabatrin, CPP-115 or OV329.** "Human" in these rows is a target mapping, not an assay species.
* **Reproduction of the ratio.**

| Source (preparation) | vigabatrin KI | CPP-115 KI | KI ratio | efficiency (kinact/KI) ratio |
|---|---|---|---|---|
| Pan 2003 via ChEMBL (pig brain) | 3.2 mM | 31 uM | about 103 | about 52 (5.7 against 0.11 per mM per min) |
| Pan 2012 article (text; "suboptimal pH and temperature") | 3.2 or 10 mM | 31 uM | 103 to 320 | printed as 187 |
| Silverman 2012 perspective (review; "same conditions") | 850 uM | 9.7 uM | about 88 | 187 (52 against 0.28) |
| Shen 2020 via ChEMBL (pig brain, one assay for all) | 290 uM | 59 uM | about 4.9 | CPP-115 kinact not deposited |

  OV329 in the same 2020 assay: KI 10 uM (about six times lower than CPP-115 and about 29 times lower than vigabatrin, KI only; abstract-level for the paper). In every row CPP-115 is the more efficient inactivator, so the direction is reproduced four times. The size is not: the 187 is not obtainable from the numbers the 2003 paper deposited (about 52), and the only same-assay comparison, 2020, gives a five-fold KI gap. In vivo, "1/300 to 1/600 of the vigabatrin dose" in the cocaine models is a dose ratio of pharmacodynamic effects (pharmacokinetics included), not an enzyme potency ratio.
* **Time dependence.** Inactivation is time-dependent and irreversible; the 2012 article says the optimum-pH rate was too fast to measure, so every KI above is condition-bound (pH, temperature, buffer, substrate). The 1977 rat-brain paper cited by GtoPdb for vigabatrin reports a half-life of inactivation at a fixed inhibitor concentration (abstract), not a KI.
* **Decision re-examined: the H02 card's CPP-115 potency statement.** Direction: STRENGTHENED (reproduced in independent sources, one of them a same-assay pig comparison). Size and species: WEAKENED. The card now says the constant is an inactivation KI, that the human label is a mapping, that the magnitude is not reproduced, and that enzyme-level advantage says nothing about brain myelin (the 2012 article itself states that no CPP-115 histology for intramyelinic oedema existed). Net for the card's claims: the sibling thread's central block ("retina-sparing is not myelin-sparing; no brain endpoint exists") is unchanged and slightly better supported; any reading of CPP-115 as "about two orders of magnitude more potent at the human brain enzyme" is not supported. Status of the card: unchanged (controversial).

## Case 2: T-type channels, card H01

* **Apinocaltamide** (sponsor paper via ChEMBL CHEMBL4177680, calcium-flux in HEK293, one laboratory): IC50 6.4, 18 and 7.5 nM at human Cav3.1, 3.2, 3.3 (span under three-fold; "triple blocker" is reproduced as a flux result, but by one source only; GtoPdb repeats the same three numbers from the same paper and is not independent), similar values at rat, mouse and dog orthologues; Cav1.2 flux IC50 2.41 uM (about 130 to 380 times higher); under 20 percent inhibition of Cav1.2, 1.3, 2.1 at 10 uM by patch clamp. Patch clamp on Cav3.3 (CHO): Ki 20 nM for the inactivated state, Kr 1,500 nM for the resting state (about 75-fold state dependence). Functional/binding label: these are functional measures; Ki here is a state-affinity from tail-current inhibition, not a radioligand Ki.
* **Comparators** (separate sponsors' papers, same family of FLIPR assays): suvecaltamide human IC50 1.2/8.2/1.5 nM by flux but 84 nM versus 2,400 nM at Cav3.3 by whole-cell patch clamp at two holding potentials (28-fold), ulixacaltamide (Z944) 37/73/86 nM. Numbers from different assays are listed, not ranked.
* **Ethosuximide** is a different regime: ChEMBL holds only three T-type rows (Cav3.3 IC50 above 5 mM in a FLIPR screen; "unknown origin" IC50 0.6 mM in a 2018 medicinal-chemistry paper that most plausibly repeats the Gomora figure; an activity at a single concentration on Cav3.2); GtoPdb has no ethosuximide row. The only direct cloned-human-channel source is Gomora 2001 (abstract): block is state dependent, with the persistent-current IC50 0.6 mM, and the methsuximide metabolite (not ethosuximide) has inactivated-state KI 0.3 to 1.2 mM; other laboratories failed to see block in rat and cat neurons at therapeutic concentrations. Nominal potency gap to apinocaltamide: four to five orders of magnitude.
* **Exposure.** Cheng 2020 gave ethosuximide intraperitoneally to mice 45 minutes before PTZ (amount in the table); no plasma or brain concentration was measured. Back-of-envelope upper bound, an arithmetic statement and not a measurement: at most about 1.5 mM total drug if the whole amount distributed in total body water without elimination, so the block figures above are neither clearly reachable nor clearly out of reach, and free brain level is unknown.
* **Decision re-examined: "ethosuximide's effect in the Wwox-null mouse is a T-type effect" (premise carried by H01 and needs audit C10).** UNRESOLVED, with the reason made quantitative: ethosuximide's measured T-type potency is in the sub- to low-millimolar, state-dependent range, the reachable concentration is not measured, and the species/preparation of the only direct source is cloned human channels. This weakens "same target class" as an anchor and strengthens the case for the apinocaltamide discriminator being informative in both directions (a negative apinocaltamide result with confirmed brain exposure would count against T-type mediation; a positive one would not exclude ethosuximide's other actions). The H01 mechanism text now records this; status unchanged (hypothesis).
* NMDA GluN2A/GluN2B: not done (see above); the catalogue statement that GtoPdb affinities could be read for subunit selectivity remains open and is the natural next table.

## Case 3: 4-phenylbutyrate and bile-acid chaperones, card A01

* **What was measured for the class.** Only HDAC inhibition has potency numbers. In one ChEMBL document (HeLa nuclear extract, Ki): 4-phenylbutyric acid 2.8 uM, its sodium salt 6.3 uM, butyric acid 136 uM, sodium butyrate 365 uM (IC50 800 uM). In a second (recombinant human HDAC1 to HDAC8, IC50, one paper, same assay): phenylbutyric acid 64 to 260 uM, butyric acid 9 to 16 uM, HDAC4/5/7/9 above 2 mM; a 2022 review repeats the sodium salt at 162 uM (HDAC1). So the two compounds' order reverses between assays and a single number for either is unreliable (fifty-fold range for phenylbutyrate itself). TUDCA: ChEMBL holds receptor and transporter assays only (TGR5 agonist EC50 30 uM; FXR antagonist activity 87 percent at an unstated concentration; PLA2 Kd 10 uM, one paper); nothing on folding or aggregation.
* **Concentrations the cited papers applied.** 0.5 to 2 mM (Delahanty, with 4 mM compromising viability); 2 mM for 24 h (DeLeeuw, Song); 10 mM in HEK293 and 1 mM in fly food (Shah); 5 mM on worm plates (Guiberson); TUDCA 100 uM; butyrate 2 mM and the HDAC inhibitor SAHA 2.5 uM as the comparator arms. Mouse arm of Song: 100 mg/kg/day for 7 days i.p.; brain exposure not measured.
* **Decision re-examined: "type of action debated between chemical chaperone and HDAC inhibition" (A01 mechanism and pharmacology).** The measured HDAC potency (micromolar to sub-millimolar) sits one to three orders of magnitude below the applied 0.5 to 10 mM, so HDAC inhibition is quantitatively available in every cell experiment cited; no quantitative datum exists for the chaperone attribution of either compound. Direction of change: the chaperone reading is WEAKENED as the default (it is the only reading with no number), the HDAC reading is not strengthened as established (no HDAC-readout, acetylation or SAHA-matched comparison is tied to the rescue in these papers by this table), so the mechanism stays UNRESOLVED but the card's "Potency: UNKNOWN" is replaced by this bounded statement. No brain or tissue concentration exists for any arm. Card status unchanged (controversial).
* Not done: proteasome inhibitor class (A02) and the read-through class (B02): the first has no WWOX substrate datum; B02 has no drug assertion supplied. Recorded as not examined, not as negative.

## Cards changed and regeneration

Packets edited: `cards/H02_...`, `cards/H01_...`, `cards/A01_...` (one sentence block each, no dose token); cards rebuilt with `repurposing_bridge.py`; `check_cards.py` 23 packets 0 problems; `repurposing_coverage.py run` and `check` (files match a fresh regeneration); `repurposing_view.py run` for `--source full` and `--source shareable`; `repurposing_join.py handoff --date 2026-10-29` written to `disease-models/wwox/research/repurposing_batch_selection_20261029_module.md`. The committed catalogue and `catalog_build.py` were not touched.

## What would change the readings

* Case 1: a measurement of vigabatrin, CPP-115 and OV329 in one assay on a recombinant human GABA-AT (kinact, KI, partition ratio) at stated pH and temperature; any brain-histology endpoint for CPP-115 or OV329.
* Case 2: free brain ethosuximide in the pups at the time of the PTZ challenge; ethosuximide and apinocaltamide on Cav3.1/3.2/3.3 in one patch-clamp assay with the same holding potentials, at the resting potential of immature neurons.
* Case 3: HDAC activity or acetylation readout, with a matched SAHA arm, in the rescue experiments; a thermal-shift or folding measurement for the bile acid and phenylbutyrate on a purified client.
