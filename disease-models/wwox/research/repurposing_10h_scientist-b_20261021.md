# Group R2 reading note: T-type calcium-channel axis and genotype-specific antiseizure pharmacology

**Scientist B, task `REPURP-10H-R2-B-20261021`, 2026-10-21.** Part of the ten-hour repurposing batch. Public edition, disease-level, class level only. **Not medical advice.** No dose, route or paediatric suitability is stated or implied anywhere in this note; doses that appear in the readings are not reproduced.

**Every paper below except the WWOX-direct confirmation section is NOT WWOX EVIDENCE.** It is a precedent, a mechanism or a design from another gene, another assay or another species, read to ask whether the lead DL-MECH-170 is plausible and what would falsify it. A statement here about a drug in a non-WWOX model is a statement about that model.

`context_policy: QUESTION_DRIVEN` for every reading in this note. The reader opened `DL-MECH-170` and `CLAIM 016` (and the known-roads sections 2.2 and 2.3) before the first paper, as the task required, so the reading context held LEGEND's conclusion about the lead and cannot declare `SOURCE_FIRST`. What was held: the ethosuximide-versus-lithium contrast in the one Wwox three-genotype PTZ assay, the lead's own falsifier, and the group's five questions. Each paper's first pass is recorded in its manifest's locators before the comparison paragraph that follows it.

## 0. The lead, restated so the readings can be scored against it

DL-MECH-170 (IPOTESI, open): in one Wwox experiment, ethosuximide's suppression of a PTZ-provoked seizure was marked not significant in wild type and heterozygous panels and significant in the null panel, while lithium suppressed in all three genotypes. Falsifier written with the lead: the lead dies if a drug-by-genotype interaction test is not significant, if ethosuximide suppresses in wild type as in the null, if the original panel does not reproduce, or (as a mechanism claim) if a T-type blocker of a different chemical class shows no genotype dependence. Transfer limit written with the lead: one experiment, constitutive null, behavioural provoked endpoint, symptomatic class at best.

Scoring axes used below for each paper (so that a reading is not a vote):
- **A. Is a genotype-restricted drug effect reported anywhere in this paper, and was a wild-type arm run on the same endpoint?** (plausibility of the contrast as a kind of finding)
- **B. Does the paper bear on whether ethosuximide's action is T-type block at all?** (mechanism)
- **C. Does it test or show the opposite of what the lead needs?** (negatives)
- **D. Developmental / safety signal for an infant disease.**

## 1. PMID 36300716 (Bleakley 2023): antiseizure drugs in an Hcn1 M294L gain-of-function DEE mouse. NOT WWOX EVIDENCE

Depth: `complete_fulltext_read` (PMC XML body, Figures 1 and 2 as page renders at 200 dpi because the rank tool flagged the pages probably-vector, supplement docx including its one figure read). Manifest `deepdive_manifests/PMID36300716.json` STRICT PASS, 9 locators. Receipt staged `FTR-20261021-36300716-01`.

**What it establishes (DATO, for this model only).** In heterozygous Hcn1 M294L knock-in mice, eight antiseizure drugs were screened with a repeated-measures, counterbalanced design on interictal ECoG spike rate. Ethosuximide, valproate, levetiracetam and diazepam reduced spiking; phenytoin, lamotrigine, retigabine raised it and the last two triggered seizures in a subset; carbamazepine trended up (p = .05). Ethosuximide reduced spiking (N = 14, p = .0004) with no spectral-band signature (Figure 2A).

**What it does not support.**
1. *Axis A.* No wild-type arm exists. Methods: all animals are heterozygous mutants. The paper therefore cannot show that ethosuximide acts in mutants and not in wild type, and nothing in it can be cited for genotype restriction. The R2 selection row wrote it as "the nearest drug-by-genotype design to DL-MECH-170"; that is true of its drug panel and false of its genotype factor. It is a drug-by-drug screen in one genotype.
2. The endpoint is interictal spiking; the authors say spontaneous seizures are too rare to quantify. Supplementary Figure S1A (read as an image) shows saline moving individual animals' spike rates in both directions between the two bins, so the within-animal test-retest scatter is large against a halving of a low mean rate (Table S1 text, extracted from the docx and not locator-verified: about 0.4 to about 0.2 spikes per minute).
3. The direction of an effect tracked drug class, not channel family alone: sodium-channel blockers aggravated. That matters for the lead's falsifier in one specific way: a *seizure-aggravating* drug class exists in a DEE model, so "an antiseizure drug suppresses in the mutant" is not a safe default and a drug-by-genotype contrast needs a harm arm as well as a benefit arm.

**Figure audit.**

| Figure | Surface read | What was seen | Read against |
|---|---|---|---|
| 1B, 1C | page 4 render, 200 dpi | ethosuximide: 14 paired lines, lower cluster after drug, a few animals near baseline; panel C ethosuximide about 60 percent of baseline versus about 15 to 20 percent for levetiracetam and diazepam | legend: ethosuximide p = .0004 (N = 14) |
| 2A | page 6 render | ethosuximide: four spectral bars about 95 to 107 percent, no asterisk | legend: no significant effect on any band |
| S1 A-D | docx image, native 1482x2096 | saline pairs cross both ways; DMSO alone raises spiking (asterisk) | supplementary methods |

**Comparison with the lead (admitted after the first pass).** Axis A: no information; the paper has no wild-type arm. Axis B: no information about the mechanism (ethosuximide shares an effect with valproate, levetiracetam and diazepam, which act by different mechanisms, so a spike reduction in this model is not specific to T-type block). Axis C: partial; shows aggravating drug classes in a DEE. Axis D: none. **Net for DL-MECH-170: none either way; a correction to the selection's description of the paper.**

**Transfer verdict.** To the reference genotype: none directly. A different gene, a gain-of-function channel, mouse, heterozygous, ECoG spikes, acute intraperitoneal pretreatment.

**OWED.** No claim is narrowed here; no blind audit is owed on this reading unless a commit candidate cites it.

## 2. PMID 37275776 (Colombo 2023): Gnb1 K78R mouse, ethosuximide and GIRK channels. NOT WWOX EVIDENCE

Depth: `partial_fulltext_read` (whole PMC XML body read; Figures 4 and 7 opened as 300 ppi embedded rasters; Figures 1, 2, 3, 5, 6 captions only; the supplementary PDF not opened). Owed: those figures and the supplement, none of which bears on the genotype question. Manifest `PMID37275776.json` STRICT PASS, 10 locators. Receipt staged `FTR-20261021-37275776-01`.

**What it establishes (DATO, for this model).** A heterozygous Gnb1 K78R missense mouse has very frequent spike-and-wave discharges (about 1,700 per 24 h) where wild-type littermates have about 12. Acute ethosuximide and valproate nearly abolished them for roughly an hour; phenytoin did not. Chronic ethosuximide in cultured mutant cortical networks normalised bursting at a middle concentration and over-suppressed at the highest. In oocytes, ethosuximide inhibits GIRK channels, much more potently when the channel is Gbetagamma-activated (GIRK2 about 55 micromolar versus about 1.5 to 2 millimolar for basal GIRK1/2), and does so equally for wild-type and K78R Gbeta.

**This paper is the strongest single caution for DL-MECH-170 in the group, for two reasons.**
1. **The floor effect.** Figure 4A, read as an image, has the wild-type arm the lead wants: ethosuximide suppresses in the mutant and "does nothing" in wild type, because wild type has about 3 events at baseline and about 0 after. A genotype-restricted suppression of a seizure endpoint is the default outcome whenever the wild-type baseline is near zero; it is the baseline, not the drug action, that is genotype-specific. The lead is only immune to this if the wild-type PTZ-alone baseline in the Wwox assay is measurably above floor. Lithium significantly suppressing the same wild-type PTZ response (CLAIM 016 boundary note) is itself evidence that the wild-type PTZ baseline was above floor, which argues the floor explanation does not fully apply there. This is an INFERENZA from LEGEND's own record of the figure; the three PTZ-alone wild-type values should be read off Cheng 2020 Figure 7b before the lead keeps that protection (new question, below).
2. **Ethosuximide may not be acting as a T-type blocker at all in a GIRK-driven model.** The authors argue, by elimination, that ethosuximide acted on "a target other than both Na+ channels and T-type Ca2+ channels", and propose GIRK block. They did not measure a Cav3 current in the mutant system: Methods mention Cav3.2 oocyte recordings but no Cav3.2 result appears on the body surface. Valproate abolished SWDs as well, and the paper cites it as inhibiting neither GIRK nor T-type, so SWD abolition is not a mechanism readout of either. Ethosuximide's GIRK block is the same for wild-type and mutant Gbeta in oocytes (Figure 7B), so any genotype dependence has to come from the mutant cell's larger Gbetagamma-GIRK drive, not from the drug.

**What it does not support.** No T-type measurement; no Cav3 involvement shown or excluded; the GIRK argument rests on oocyte expression and on one mouse background; the in-vivo time course (about an hour) is acute pretreatment with SWD counts, not disease course. A heterozygous null of the same gene did not lower the seizure threshold while the missense did, which is a direct caution that null and missense genotypes of one gene do not share phenotype or, by extension, drug response.

**Figure audit.**

| Figure | Surface | Read | Against |
|---|---|---|---|
| 4A | p.13 embedded raster 2008x1617 | ETX mutant about 35 to about 1.5 at 30 min, wild type about 3 to about 0 | text: "nearly abolished SWDs"; legend n per arm |
| 4B/C | same | chronic in-vitro ETX: lowest concentration no change, middle concentration near-normal burst duration, highest concentration over-suppression of firing | text and p-value table |
| 7B | p.17 embedded raster 1772x1206 | GIRK2+Gbetagamma curves left of the shaded range midpoint; GIRK1/2 to the right | text EC50 values |

**Comparison with the lead.** Axis A: a wild-type arm exists and is floored; this is the clearest published illustration of how a "genotype-specific" drug effect can be a baseline effect. Axis B: strong; the ethosuximide mechanism in a seizure model is contested between T-type, GIRK and unmeasured targets. Axis C: yes. Axis D: none. **Net for DL-MECH-170: narrows the lead's mechanism claim and adds one new falsifier question (the wild-type PTZ-alone baseline).**

**OWED.** A blind locator audit is owed only if a commit candidate cites this paper's floor-effect point to narrow DL-MECH-170; none is written from this reading alone.

## 3. PMID 42274296 (Harman 2026): Gabrb3 D120N Lennox-Gastaut mouse, ethosuximide, a Cav3-selective inhibitor and cannabidiol. NOT WWOX EVIDENCE

Depth: `complete_fulltext_read` (PMC XML; all five figures opened as 300 ppi embedded rasters; no supplement deposited). Manifest `PMID42274296.json` STRICT PASS, 11 locators. Receipt staged `FTR-20261021-42274296-01`.

**What it establishes.** Heterozygous knock-in mice have spontaneous atypical absence seizures that untreated wild-type littermates lack entirely (0 of 6 against 7 of 7), and at postnatal day 16 a spasm phenotype (wild type 4 of 11 with some events, knock-in 10 of 10). In a vehicle-controlled Latin-square crossover within the knock-in, ethosuximide and ulixacaltamide (a Cav3-selective compound) each cut seizure incidence by about 64 percent and cannabidiol by about 46 percent; vigabatrin and cannabidiol lowered neonatal spasms.

**Correction to the selection row.** The R2 table described it as a template in which "ethosuximide, a T-type blocker and cannabidiol each separate KI from wild-type littermates in a within-subject crossover". They do not. The crossover is vehicle versus drug within knock-in animals; wild-type animals were never dosed (Methods, locator 2; the spasm arm allocates only knock-in pups). The wild-type arm is an untreated phenotype control. This paper is therefore a design template for the within-subject half of a drug-by-genotype design and an example of its missing half.

**What it does support, for the lead.**
- *Cross-class T-type agreement, in a different model.* Ethosuximide and a structurally unrelated Cav3-selective inhibitor give the same size of reduction in the same knock-in (separate cohorts, n = 9 and n = 11, not compared statistically). This is the only paper in the group in which both sit side by side, and it is a point in favour of the lead's falsifier being answerable: a second T-type blocker of a different class can be run in the same assay. It is not evidence of genotype dependence, because neither was run in wild type. (Axis B, modest support; Axis A, no information.)
- *The baseline is again a zero.* Wild-type atypical absence seizures are 0 of 6. As in the Gnb1 model, a mutant-only drug effect is built into the endpoint. In the Wwox PTZ assay the endpoint is provoked in all three genotypes, which is the one design feature that would let the contrast mean something.
- *Injection stress inflates the vehicle baseline* (about 21 events per hour in vehicle-injected mutants against about 7 in uninjected animals): the authors' own observation, offered as a suggestion. In an acute-injection PTZ design with saline controls, per-genotype baselines can differ by handling, and the drug versus vehicle difference is measured on that elevated baseline.

**What it does not support.** No wild-type drug data; no T-type measurement (the compound agreement is the evidence); spasm scoring is behavioural, un-EEG'd and not controlled for sedation (authors' limitations); the cannabidiol conflict-of-interest statement (a patent and consulting roles) frames the paper's emphasis, not the ethosuximide measurement.

**Figure audit.** Fig 1B/C/E (WT at zero), Fig 2A/B (ethosuximide: 8 of 9 animals fall, one rises about 9 to about 20), Fig 3A/B (ulixacaltamide: two animals near 19 to 22 stay), Fig 4 (cannabidiol, read, not used), Fig 5A/B (WT spasm bar about 1.1, KI about 4.9, treated about 2.7 to 2.9), all as 300 ppi embedded rasters with the text.

**Comparison with the lead.** Axis A: absent wild-type drug arm. Axis B: modest support that a second, selective Cav3 compound matches ethosuximide in a spike-and-wave-type model. Axis C: partial (injection confound, no WT dosing). **Net: none for genotype specificity; it raises the plausibility that the Wwox assay's mechanism could be tested with a second T-type blocker.**

## 4. PMID 37082241 (Harman 2023): a new pan-Cav3 inhibitor in Dravet, 6 Hz and GAERS models. NOT WWOX EVIDENCE

Depth: `partial_fulltext_read` (whole PMC XML body; Figures 5, 6 and 8 as page renders at 170 dpi; Figures 1-4 and 7 captions only; supplementary files not opened; owed sections do not touch the genotype question). Manifest `PMID37082241.json` STRICT PASS, 9 locators. Receipt staged `FTR-20261021-37082241-01`.

**The negative, stated straight.** The compound SB2193, a pan-Cav3 inhibitor of the authors' own new chemotype, (i) protected mice in the 6 Hz acute seizure model at the top dose tested, (ii) did not reduce spontaneous generalised seizures or survival in the Scn1a heterozygous Dravet-model mouse (seizure p = 0.67; survival p = 0.09, and the figure shows the treated curve below the control, about 43 against about 67 percent at postnatal day 30), and (iii) in GAERS, a rat with a Cav3.2 gain-of-function and the textbook ethosuximide-sensitive absence model, appeared to increase the incidence and duration of spike-and-wave discharges at the middle and top doses.

**What the negative is worth, by the authors' own list.** It is **not** a clean demonstration that T-type block does not work or that it aggravates. The authors cannot exclude: sub-IC50 brain exposure in the Dravet arm (1.7 micromolar in brain against a patch-clamp IC50 of 3.5 micromolar, a FLIPR IC50 of 0.75), unmeasured free fraction, human-channel potencies, off-target sodium-channel action (they note sodium-channel blockers aggravate GAERS), and a speculated CB1-active metabolite (the aggravation was delayed beyond the first hour). The brain half-life after injection was about half an hour. The compound was never given to a wild-type or a non-epileptic control on the EEG endpoints, so nothing in it separates a genotype effect from a drug effect.

**What it does constrain, for DL-MECH-170.**
1. *Class effect is not guaranteed.* One new Cav3 compound failed in a genetic DEE-type mouse and aggravated in the best-validated absence model. The lead's own falsifier ("a T-type blocker of a different chemical class shows no genotype dependence") is made harder to read by this: a different-class compound can be inactive or aggravating for reasons unrelated to T-type block, so the second-compound arm of a confirmatory design needs a compound with measured exposure and a measured selectivity panel, and a failure of one compound must not be scored as a failure of the mechanism.
2. *Subtype direction.* The paper cites that Cav3.3 null mice have more spike-and-wave susceptibility, so Cav3.3 inhibition may be proconvulsant; a pan-Cav3 block therefore has an isoform-level argument for moving the wrong way. Ethosuximide's own subtype profile is not addressed here.
3. *Ethosuximide itself in a Dravet-type genotype.* The authors cite (not measure) that ethosuximide was ineffective in an Scn1a zebrafish model. That is a second, cited, datum that ethosuximide's seizure benefit is genotype-dependent in a direction (no effect in Dravet-type, effect in absence-type, effect in HCN1 spike endpoint). It supports the *kind* of finding the lead describes, a genotype-dependent ethosuximide effect, without telling anything about WWOX.
4. *Floors again.* In Figure 6A most Dravet-model animals have zero seizures in the window; the endpoint cannot show a reduction for them.

**Figure audit.** Fig 6A/B (p.9 render): zero-inflated seizure counts, survival curves diverging toward the treated group's disadvantage, log-rank p = 0.09. Fig 8A/B/I (p.11 render): vehicle arm itself rises above baseline over the 4 h window (a time effect in controls), the middle dose has higher raw incidence than vehicle and the top dose does not on raw incidence.

**Comparison with the lead.** Axis A: no wild-type arm. Axis B: weakens confidence that any one non-ethosuximide T-type compound is a clean probe of mechanism. Axis C: this is the negative the selection flagged; it is real but confounded, and it is reported so. Axis D: the compound lowered survival non-significantly in a developmental epilepsy model; at class level a developmental-toxicity or exposure signal for T-type block is not demonstrated here but cannot be excluded. **Net: the lead's mechanism claim should be held at "ethosuximide-specific observation" until a second, characterised T-type compound is run; the negative narrows the falsifier's interpretation but does not refute the lead.**

## 5. PMID 30955423 (Huguenard 2019): spikes, bursts and synchrony in absence epilepsy, a "current controversy" review. NOT WWOX EVIDENCE

Depth: `complete_fulltext_read` of a narrative review (no Methods, Results, tables or supplement to read; both figures opened as images). Manifest `PMID30955423.json` STRICT PASS, 10 locators. Receipt staged `FTR-20261021-30955423-01`. This is secondary literature: it summarises three primary studies and is not primary evidence for any of their measurements.

**What the "challenge" actually is.** The selection called this "the standing challenge to the burst-firing mechanism" and the abstract says burst firing in relay neurons "may not be essential", "bringing into question the proposed mechanism for the antiepileptic drug ethosuximide". Read at body level the claim is narrower and says something different:
- The body names ethosuximide once (the working model: it blocks thalamic Cav3 channels) and describes **no ethosuximide experiment**. The three studies reviewed use optogenetics, silicon probes with a Cav3-selective antagonist, and calcium imaging, in stargazer mice, WAG/Rij and GAERS rats and a gamma-butyrolactone model.
- The challenged item is **where and how** Cav3 acts: relay-cell bursting is intermittent and weaker than the model assumed; reticular-nucleus bursting is robust; local Cav3 antagonism suppressed seizures at every cortical and thalamic site with a regional concentration gradient, which the author attributes to diffusion to the reticular nucleus (and lists an alternative: smaller-nucleus critical-mass effect).
- The review's **conclusion keeps Cav3 central**: thalamic Cav3 "critical for generation of SWD, especially" reticular; blockade in either cell class suppresses absences. So the standing controversy limits the *relay-neuron burst* version of the ethosuximide mechanism and leaves a Cav3-in-thalamus mechanism standing.
- Measurement caveats the author states himself: spike-sorting during the ictal spike under-reports by about 80 percent in his experience; imaging was in primary visual cortex, not the focus; optogenetic rebound induction was proven only in animals already prone to absences.

**Consequence for DL-MECH-170.** None of this tests a Wwox-null circuit or any genotype comparison. What it adds: (a) an ethosuximide effect on seizures in a model need not run through relay-neuron burst firing, so a genotype dependence in the Wwox PTZ assay (a convulsant model, not an absence model, with a behavioural endpoint) cannot be assumed to reflect thalamic T-type burst physiology; (b) the cleanest locus to test a T-type contribution in a null would be a site-resolved manipulation (reticular versus relay), which is far beyond the first experiment the lead needs. Axis A: none. Axis B: narrows the textbook mechanism, does not remove Cav3. Axis C: yes in its limited form. Axis D: none. **Net: the "challenge" is real and narrower than the selection stated; it argues for measuring the T-type contribution in the Wwox system rather than assuming it, which is what the lead's falsifier already asks.**

**Figure audit.** Fig 1 (adapted peri-event histograms, WAG/Rij): firing peaks at the EEG spike across cortex, reticular and most relay nuclei, IAM flat, CL-PC paused. Fig 2: a cartoon with no data.

## 6. PMID 42536722 (Miao 2026): digenic Cacng2/Cacna1a absence mouse, ethosuximide, Cacna1g deletion and PV interneurons. NOT WWOX EVIDENCE

Depth: `partial_fulltext_read` (whole PMC XML body read; Figures 2 and 3 as page renders at 200 dpi because the pages were flagged probably-vector; Figures 1, 4, 5 captions only; supplementary PDF not opened; none of the unread parts concern the ethosuximide or Cacna1g arms). Manifest `PMID42536722.json` STRICT PASS, 9 locators. Receipt staged `FTR-20261021-42536722-01`.

**What it establishes.** In a mouse that is heterozygous for two absence-epilepsy genes (neither heterozygote alone is epileptic), ethosuximide abolished spike-and-wave discharges for about two hours in all twelve mutants and did not correct a social-novelty deficit; deleting Cacna1g (Cav3.1) removed the T-type current and the discharges and also did not correct the deficit; chemogenetic activation of parvalbumin interneurons did both.

**Why it matters for the lead, in two parts.**
1. *A genetic test of T-type dependence runs in the same genotype as the drug.* Removing Cav3.1 prevents the seizure in the mutant, in agreement with ethosuximide: this is the strongest design in the group for "is the drug effect a T-type effect in this genotype", by epistasis rather than by a second compound. It is not a drug-by-genotype test (ethosuximide was not run in wild type on the EEG endpoint, and wild type has no discharges to suppress), and it says nothing of a null allele of an unrelated gene.
2. *Symptomatic, not modifying.* The ethosuximide effect and the Cav3.1 deletion both suppress the seizure and leave the quantified comorbidity untouched. This is the answer to the group's fifth question for this paper: in this model, a T-type effect on seizure does not carry a disease-modifying signal on a measured cognitive-social endpoint. The Wwox lead is already tagged symptomatic-class; this gives a worked example of why that tag must stay.

**Smaller observations.** (a) Ethosuximide produced broad-band cortical power suppression, so the drug has a footprint beyond the spike-wave band that the authors themselves read as going beyond canonical thalamic T-type action; (b) the controls were dosed on the social test and the group difference was unchanged, so a genotype-by-drug contrast does exist on that behavioural endpoint and is null; (c) the effect lasts about two hours with recurrence, consistent with acute pretreatment designs.

**Figure audit.** Fig 2B-F (page 4 render): SWD duration per 30 min near zero in sections 3 to 7 and no difference at section 8; power spectrum halved at the peak; social-novelty group difference present before and after. Fig 3C/E/I/J (page 5 render): rebound spikes and T-type current abolished in the triple mutant; triple mutant still has a social-novelty difference versus its control.

**Comparison with the lead.** Axis A: partially; the behavioural endpoint has a genotype x drug design and is null, the EEG endpoint has no wild-type drug arm. Axis B: supports T-type (Cav3.1) dependence of the seizure in the mutant genetically. Axis C: partly (EEG broad suppression, dissociation). Axis D: none. **Net: increases the plausibility that an ethosuximide seizure effect in a null would be T-type mediated if it exists, and reinforces the symptomatic class.**

