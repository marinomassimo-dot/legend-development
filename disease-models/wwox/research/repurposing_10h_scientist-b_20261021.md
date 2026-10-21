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
| 4B/C | same | chronic ETX: 250 uM no change, 750 uM near-normal burst duration, 2 mM over-suppression of firing | text and p-value table |
| 7B | p.17 embedded raster 1772x1206 | GIRK2+Gbetagamma curves left of the shaded range midpoint; GIRK1/2 to the right | text EC50 values |

**Comparison with the lead.** Axis A: a wild-type arm exists and is floored; this is the clearest published illustration of how a "genotype-specific" drug effect can be a baseline effect. Axis B: strong; the ethosuximide mechanism in a seizure model is contested between T-type, GIRK and unmeasured targets. Axis C: yes. Axis D: none. **Net for DL-MECH-170: narrows the lead's mechanism claim and adds one new falsifier question (the wild-type PTZ-alone baseline).**

**OWED.** A blind locator audit is owed only if a commit candidate cites this paper's floor-effect point to narrow DL-MECH-170; none is written from this reading alone.

