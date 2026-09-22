# Downstream, WWOX-independent rescue — a bounded census

**Node:** `MECHANISM_DOWNSTREAM_WWOX_INDEPENDENT_RESCUE` · **Date:** 2026-09-21 · **Actor:** Scientist B
**Question answered:** which published interventions rescue a WWOX-loss-of-function phenotype **without requiring functional WWOX to be present**, and which of them rest on a real intervention arm rather than on a correlation or an author's assertion.

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries and
> every ledger. Nothing here changes a claim, a paper record, the working model or the tracking log. Anything
> promotable goes through INGEST → DEEP_DIVE → BATCH_COMMIT.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> **Nothing here is medical advice.** Every compound named is material for discussion with a treating clinical
> team and for nobody else. No dose, schedule or indication is formulated anywhere in this file.

---

## 1. Read depth declared up front

Two surfaces were fetched **in this session** and quoted from the fetched bytes in the same act. Everything else is
quoted from LEGEND's own fingerprinted, receipt-backed locator manifests, and is labelled as such — a locator
manifest is a contemporaneous record of a read, not a memory, but it is also not a fresh fetch and is not
presented as one.

| PMID | Identity | Depth reached **in this session** | Returned body length | Figure access |
|---|---|---|---|---|
| **25012504** | Abu-Remaileh & Aqeilan 2014, *Cell Death Differ* — WWOX/HIF1α/glucose | PMC fetch **attempted and measured**; fell back to LEGEND's manifest (22 locators) + dossier | 🔴 **0 bytes** — `PMC4211377` returns `full_text: ""`. The PMCID exists; the body does not come through this route | none this session. LEGEND's receipt `FTR-20260814-25012504-01` records 33 main + 18 supplementary panels inspected |
| **34634460** | Breton *et al.* 2021, *Neurobiol Dis* — neocortical oscillations, Wwox S-KO | **Full body read this session** (Intro → Results → Discussion → Methods) | non-empty, ≈25 000 characters (approximate; not instrumented) | none — no figure is inspectable here. Panel values below come from LEGEND's manifest `PMID34634460.json` |
| **32000863** | Cheng/Chang *et al.* 2020, *Acta Neuropathol Commun* — Wwox-KO neuropathy, GSK3β, seizures | **Full body read this session** (Intro → Methods → Results → Discussion) | non-empty, ≈24 000 characters (approximate; not instrumented) | none — panel values from LEGEND's manifest `PMID32000863.json` (Fig. 7b/7c/7d read at native 1946×1627) |
| **42397075** | Steinberg/Zonca … Aqeilan 2026, *Brain* — WWOX–MYC organoids | not fetched — **no PMCID exists** (`convert_article_ids` returns pmid + doi only), so the PMC route is unavailable, not untested | n/a | none this session. LEGEND's receipt `FTR-20260810-42397075-04`, manifest with **30 locators**, records Suppl. Fig. 7F–G read at 170 ppi and **re-read at 258 ppi** |
| **34268881** | Steinberg *et al.* 2021, *EMBO Mol Med* — brain organoids | not re-fetched | n/a | LEGEND's `FTR-20260814-34268881-03` records **all 11 figures / 69 panels** inspected |
| 105 further PMIDs | field-wide census (5 PubMed queries) | **titles + abstracts only** for the 69 records carrying no LEGEND receipt | n/a | n/a |

🔴 **Parser warning applied throughout.** The PubMed/PMC extractor deletes italicised tokens. In the Breton body
it deleted the italic `p` from every p-value (`"decreased the frequency of the events by 87% (= 0.008)"`), and in
the Cheng body it deleted every genotype superscript (`Wwox−/−`, `Wwox+/+`, `Wwox+/−` all read as empty) and the
`2+` of `Ca2+`. **No negative in this file rests on a string count from extracted text**, and every genotype token
below is taken from a surface that preserved it.

---

## 2. The direct answer

**Four interventions in the entire literature have been applied to a system in which WWOX is genuinely absent and
have moved a WWOX-dependent phenotype. None of them rescued a disease endpoint.** They are: **digoxin**
(HIF1α inhibition) in the germline *Wwox*-null mouse, endpoint **acute blood glucose at 40 minutes**, `n=3`/group,
at a printed dose of `100 mg/kg` that is pharmacologically implausible and unresolved; **d-APV** (NMDAR block) in
neuron-specific *Wwox* S-KO neocortical slices, endpoint **spontaneous burst frequency driven to zero**, ex vivo,
acute, at an age the authors themselves call late-stage; **ethosuximide** in the germline *Wwox*-null mouse,
endpoint **PTZ-provoked seizure behaviour**, and it is the only one of the four whose effect is genotype-specific
in its own figure; and **A51**, a multi-kinase inhibitor suppressing Wnt and MYC, in human WWOX-KO cerebral
organoids, endpoint **progenitor identity and pan-neuronal marking recovered, layer-neuron output not**. A fifth,
**carbenoxolone**, has an arm in a WWOX-null slice but is not attributable to its nominal target, and a sixth,
the pannexin blocker **BB-FCF**, has an arm and went the wrong way. So: the class is real, it has exactly four
positive arms, **its best in-vivo endpoint is blood glucose and its best human-neural endpoint is a cell-identity
marker — neither is a seizure, a myelin measure or a developmental outcome**, and the one axis LEGEND had never
scored (ethosuximide) turns out to carry the only genotype-specific in-vivo pharmacology in the whole field.
The operator's premise that LEGEND has no HIF1α entry is **incorrect** — `DL-MOL-009`, `DL-MECH-095` and `N-07`
already carry it, already corrected the endpoint, and already classified digoxin as target validation.

---

## 3. The intervention table

`WWOX absent?` is the decisive column. `✅` = the treated system has no functional WWOX. `❌` = the system is
WWOX-replete or WWOX is being supplied/induced, which disqualifies a `DOWNSTREAM WWOX-INDEPENDENT` verdict.

| # | Intervention | Source PMID | System (WWOX absent?) | Endpoint rescued | In vivo? | Dose / route (as printed) | Therapeutic class | Applicable genotype class | Verdict | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Digoxin** (HIF1α inhibitor) | 25012504 | germline *Wwox*-null mouse — ✅ | **acute blood glucose**, +40 min; KO ~10 → ~115 mg/dl | ✅ **yes — a true *Wwox*-null animal, not a xenograft** | `100 mg/kg`, i.p. (printed in HTML **and** PDF; implausible; `REPORTED_DOSE_AMBIGUITY`) | **DOWNSTREAM WWOX-INDEPENDENT** — but see verdict | null/null; CNV/deletion. ⚠️ **not** transferable to residual-protein classes without test (WWOX binds HIF1α via **WW1**, so an SDR missense may retain the brake — `DL-MECH-028`, H-2) | **MECHANISTIC PROBE.** The class is right, the endpoint is a metabolic proxy, `n=3`, one timepoint, no neurological readout, and the compound is a cardiac glycoside | medium-high on the arm; **low** on disease relevance |
| 2 | **shHIF1α** (genetic) | 25012504 | (a) *Wwox*-KO MEFs — ✅ · (b) **xenografts of transformed KO MEFs** — ✅ for WWOX, ❌ for disease relevance | (a) glucose uptake suppressed · (b) **tumour growth** | (b) yes, but **xenograft** | n/a | MECHANISTIC PROBE | null/null | **MECHANISTIC PROBE.** 🔴 A xenograft tumour-growth arm is **not** a WOREE-relevant in-vivo arm | high on the arm; nil on transfer |
| 3 | **d-APV** (NMDAR antagonist, tool) | 34634460 | Synapsin-Cre neuron-specific *Wwox* S-KO mouse neocortical slice, P13–P17 — ✅ | **spontaneous bursting eliminated**; reversible on washout | ❌ ex vivo | `50 μM` in ACSF, bath | **DOWNSTREAM WWOX-INDEPENDENT** | all biallelic LoF (demonstrated in neuronal null); the node is the network, not the allele | **DOWNSTREAM WWOX-INDEPENDENT** — the cleanest arm in the field. But the endpoint is a **network state**, the preparation is acute, and the authors call P13–P17 *"a late-stage disorder"* | **high** for the tool compound; the approved analogue (memantine) has **never** been given to a WWOX system |
| 4 | **Carbenoxolone** (gap-junction, tool) | 34634460 | same — ✅ | burst frequency −87%, duration −18% | ❌ ex vivo | `100 μM`, bath | MECHANISTIC PROBE | — | **MECHANISTIC PROBE, not attributable.** CBX blocks NMDAR and pannexin; and *"This did not return to normal levels after washout"* — an effect surviving washout is not cleanly pharmacological | low |
| 5 | **BB-FCF** (selective pannexin-1 blocker) | 34634460 | same — ✅ | 🔴 **none — the point estimate went the wrong way** (normalised burst frequency ≈2.55 vs baseline 1.0, no significance test drawn) | ❌ ex vivo | `10 μM`, bath | DOWNSTREAM WWOX-INDEPENDENT (class) | — | **NEGATIVE RESULT.** The prose says *"minimal effect"*; the panel shows a 2.5-fold rise. Already LEGEND's `N-16` | medium (no test reported) |
| 6 | **Ethosuximide** (T-type Ca²⁺ blocker) | 32000863 | germline *Wwox*-null mouse (exon-1 and exon-2/3/4 strains) — ✅ | **PTZ-provoked seizure behaviour suppressed**, and **only in the null** | ✅ **yes** | `150 mg/kg` i.p., 45 min before PTZ (`30 mg/kg` i.p.) | **SYMPTOMATIC** (downstream, WWOX-independent mechanism) | null/null | **DOWNSTREAM WWOX-INDEPENDENT, symptomatic.** 🔴 **The only genotype-specific in-vivo pharmacology in this literature** — `n.s.` in `+/+` and `+/−`, significant in `−/−`. ⚠️ But the endpoint is a **provoked** seizure, not spontaneous, and a low-dose-PTZ floor in the controls is an untested alternative explanation | medium |
| 7 | **Lithium chloride** (GSK3β) | 32000863 | same — ✅ | PTZ-provoked seizure suppressed — **in all three genotypes, wild type included** | ✅ yes | `60 mg/kg` i.p. ×3 within 1 h before PTZ | SYMPTOMATIC | — | **REQUIRES NOTHING — AND DEMONSTRATES NOTHING WWOX-SPECIFIC.** Already `N-02` / `DIS-`-adjacent. Directionally **harmful** on the Wnt axis (`DL-MOL-003`) | low (specificity failed) |
| 8 | **A51** (multi-kinase; suppresses Wnt **and** MYC) | 42397075 | **human WWOX-KO cerebral organoids (isogenic null)** — ✅ | SOX2⁺ 60→33 % (`ns` vs WT); SOX2⁺MYC⁺ 72→50 % (`ns` vs WT); NEUN⁺ 6→18 % (`*` vs KO). 🔴 **SATB2⁺ `ns`, CTIP2⁺ `ns` — layer-neuron output not rescued** | ❌ in vitro | `125 nM`, weeks 8→15 in culture | **DOWNSTREAM WWOX-INDEPENDENT** | engineered null/null (the arm was run on clone KO-1B only). The **target** is shared: MYC is up in radial glia of KO, WOREE and SCAR12 at comparable magnitude | **DOWNSTREAM WWOX-INDEPENDENT** — and the **first and only pharmacological intervention in a human WWOX-deficient neural model anywhere in this corpus. ⚠️ The reagent is not MYC-selective**, the experiment is one of the three the paper excludes from independent differentiations, and no randomisation or blinding was applied | medium on the arm; **low** on attribution to MYC |
| 9 | **AAV9-hSynI-WWOX** | 42397075 · 34747138 · 42422765 | *Wwox*-null mouse; WWOX-KO / WOREE / SCAR12 organoids — ✅ | hyperexcitability, survival, myelin, gliosis, SWD/ECoG — **but not radial glia** | ✅ (mouse) | ICV, neonatal | **GENE REPLACEMENT** | all WWOX-LoF | **REQUIRES WWOX** — by construction it supplies it. Included only as the contrast case | high (preclinical) |
| 10 | **Ketogenic diet** | — (rationale from 25012504 · 34268881) | — | — | — | — | DOWNSTREAM WWOX-INDEPENDENT *in principle* | — | 🔴 **NO INTERVENTION ARM EXISTS IN ANY WWOX SYSTEM.** `ketogenic` = zero in both Lodz metabolism papers. The human observations (3/5 improved in one report; listed among ineffective interventions in a severe null/null case) are uncontrolled | not scorable as an arm |
| 11 | **Toosendanin** ("WWOX activation") | 34015398 | hepatocellular carcinoma lines — ❌ **WWOX is being induced** | — | — | — | **NOT TRANSFERABLE** | none | 🔴 **Category error for WOREE.** An agent that works by raising WWOX has nothing to raise in a null | n/a |
| 12 | **Zfra peptides · pTyr33-WWOX peptide · the C1q axis** | 38542478 · 35883580 and the pTyr33 line | WWOX-replete systems; the mechanism **antagonises or consumes WWOX** — ❌ | — | — | — | **NOT TRANSFERABLE** | none | 🔴 **Boundary restated, not revived.** LEGEND already dismissed these (`N-09`, `HYP-20260705-05`, `INSUFFICIENT_EVIDENCE` class). Nothing found in this census changes that and **no `REVIVAL_TRIGGER` is invoked** | n/a |

**What the table does not contain, and the absence is measured.** Across five PubMed queries (148 + 55 + 25 + 19 + 3
records), **no intervention arm in a WWOX-deficient system exists outside rows 1–9.** The narrowest query —
`Wwox AND (mice OR mouse OR rat OR zebrafish OR Drosophila) AND (lithium OR ethosuximide OR pentylenetetrazol OR
digoxin OR metformin OR ketogenic OR rapamycin OR memantine OR bumetanide)` — returns **3 records in the whole of
PubMed**, and LEGEND already holds all three. The neuro-intersection query returns **25 records in total**, of
which the 13 without a LEGEND receipt are, on inspection of every title and abstract, clinical-genetic cohort and
case papers with no intervention arm. **This is a field-density limit, not a gap in the reading.**

---

## 4. The HIF1α verdict

**Verdict: `MECHANISTIC PROBE`, not a therapeutic lead — and LEGEND already said so.** The ledger sentence that
prompted this node (*"inhibition of HIF1α (genetic AND pharmacological) reverts glucose uptake in vitro and in
vivo"*) is a **paraphrase that conflates three different experiments**, and the conflation was already corrected
inside LEGEND on 2026-08-14 by `DL-MECH-095`. The corrections hold. Taking (a)–(e) in order:

**(a) Which inhibitor, what dose, what system.** The pharmacological agent is **digoxin**, given **i.p.**, at a
printed dose of **`100 mg/kg`**, in *Wwox*-null mice, `n=3` per group, read at **40 minutes**. LEGEND's receipt
records that the dose check demanded by `DL-MOL-009` was executed and **closed against the source**: the HTML and
the PDF **both** print `100 mg/kg`. That is pharmacologically implausible for a cardiac glycoside and is almost
certainly a µg/kg typographic error — but *there is no documentary basis to rewrite it*, so it stands as
`REPORTED_DOSE_AMBIGUITY`. The genetic agent is **shHIF1α**, in KO MEFs and in xenografts of transformed KO MEFs.

**(b) Is the in-vivo arm a *Wwox*-knockout animal or a xenograft? — Both, and the distinction is the whole
answer.** The **pharmacological** arm is a genuine germline *Wwox*-knockout animal. The **genetic** arm in vivo is
a **xenograft tumour-growth experiment**, which is not a WOREE-relevant in-vivo arm at all. So the ledger's
"genetic AND pharmacological … in vivo" is true only if one accepts a tumour xenograft as an in-vivo disease arm,
which this node explicitly does not.

**(c) What endpoint was rescued.** **Blood glucose.** Not glucose uptake — that is the `DL-MECH-020` paraphrase
error, already corrected. Not seizures, not EEG, not myelin, not behaviour, not survival, not development.

**(d) Disease endpoint or metabolic proxy?** **Metabolic proxy, and a distal one.** The *Wwox*-null mouse dies at
~4 weeks with lethal hypoglycaemia, so raising its blood glucose for 40 minutes corrects a **systemic peripheral
phenotype of that mouse**, not the neuronal bioenergetic block that the WOREE rationale is about. Two further
panel-level bounds, both from LEGEND's inspected figures: the specificity is asserted rather than tested (Fig. 5C
shows the WT falling visually from ~105 to ~75 mg/dl with **no statistical comparison drawn** for that change),
and the transcript panels attributed to digoxin measure **GLUT1 and PHD3, not PDK1**, at `n=2`/condition with no
inferential statistics shown.

**(e) Any brain, neuron or developmental readout anywhere in it?** **No.** LEGEND's dossier states it flatly:
*"No neurons, brain tissue, seizures, myelination or developmental neurological endpoints."* The independent Lodz
primary on the same axis (`PMID 35328751`) carries the same void: `brain`, `neuron`, `epilep*`, `seizure` all
absent — and that zero is recorded in LEGEND as an **informative** zero because those words are in roman type, not
italic, so the parser could not have deleted them.

**Two further constraints that bear on whether this axis is even WWOX-independent for the right patients.**
WWOX binds HIF1α **via WW1**, not via the SDR (`DL-MECH-028`). A downstream HIF1α lever therefore has **more** to
do in a biallelic null and **possibly less** in a class retaining a folded WW1 — the inverse of the usual
assumption that downstream levers are genotype-agnostic (`H-2`). And the Lodz human arm found the oxidative half
of the Warburg frame **measured and null** (citrate synthase unaffected; PDH activity unchanged in all four
conditions), with glucose uptake **changing sign** between conditions.

**Verbatim locators for this section** are in §5. Two are marked as re-used from LEGEND's manifest rather than
re-fetched, because `PMC4211377` returns an empty body through this deployment's route — a measured
retrievability fact, recorded rather than assumed.

---

## 5. Verbatim locators

### 5.1 Fetched and quoted in this act — PMID 34634460 (Breton 2021)

> "Blocking glutamatergic neurotransmission with d-APV (50 μM) eliminated the spontaneous bursting events, as recorded from an LFP placed in the superficial neocortical layer. Upon washout, the frequency, duration and peak-to-trough amplitude returned to normal. In contrast, CBX (100 μM) decreased the frequency of the events by 87% (= 0.008) and their duration by 18% (= 0.0274, Supplementary Table S1), with no change to their amplitude. This did not return to normal levels after washout. Furthermore, the effects were not recapitulated with BB-FCF (10 μM), indicating that the suppressive effects of CBX were not due to pannexin 1 channel opening."

`surface: body` · Results 2.2, *"Gap junctional blockade reduces, whereas glutamatergic blockade abolishes,
spontaneous bursting activity"* · ⚠️ the italic `p` is deleted by the extractor in both parenthetical p-values;
the numbers are quoted as returned and the missing `p` is stated, not silently restored.

> "Since the recordings were obtained at P13-17, yet these mice die between 3 and 4 postnatal weeks, the chosen age group may mimic a late-stage disorder of WWOX. For this reason, we cannot rule out the possibility that a pannexin 1 blocker could be an anti-epileptic treatment at earlier developmental stages."

`surface: body` · Discussion 3.4.

> "Initial stock solutions of tetrodotoxin (TTX), 2-amino-5-phosphonopentanoic acid (d-APV), carbenoxolone (CBX) and brilliant blue FCF (BB-FCF), dissolved in double-distilled water, were further individually diluted in ACSF for a final concentration of 1 μM TTX, 50 μM d-APV, 100 μM CBX, and 10 μM BB-FCF."

`surface: body` · Methods 5.4, *Pharmacology*.

**Panel counter-reading** (LEGEND manifest `PMID34634460.json` entry 2, receipt `FTR-20260810-34634460-02`,
read at 6× from native pixels; *not* re-inspected here because no figure is inspectable in this environment):
Figure 3D-d1 normalised burst frequency — Base 1.0, d-APV **no bar**, CBX ≈0.15, **BB-FCF ≈2.55**, d-APV-washout
≈1.85, CBX-washout ≈0.25, BB-FCF-washout ≈2.6. The Discussion's *"had minimal effect on the network excitability"*
therefore describes a 2.5-fold rise with no test drawn.

### 5.2 Fetched and quoted in this act — PMID 32000863 (Cheng/Chang 2020)

> "Pretreatment of an antiepileptic drug ethosuximide suppressed PTZ-induced seizure in mice (Fig.b), although ethosuximide pretreatment had no effects on the behavior changes in and mice treated with a low dose of PTZ."

`surface: body` · Results, *"GSK-3β inhibition ameliorates the hypersusceptibility to epileptic seizure due to
loss in mice"*. 🔴 **The genotype tokens are deleted by the extractor** — they are italic superscripts. The
sentence as printed reads `… in Wwox−/− mice … in Wwox+/+ and Wwox+/− mice …`; that restoration is taken from
LEGEND's manifest `PMID32000863.json` entry 1, which captured it from a surface that preserved them, and is
marked as such rather than reconstructed here.

> "Ethosuximide (i.p., 150 mg/kg), a T-type Ca channel blocker that has anticonvulsant activity (Luszczki et al., 2005), was injected into mice 45 min before PTZ-induced clonic seizures. LiCl (i.p., 60 mg/kg) were pretreated three times within 1 h before PTZ injection."

`surface: body` · Methods, *Induction of seizure*. (`Ca2+` → `Ca`: the superscript is deleted.) PTZ itself:
*"For PTZ model, we injected PTZ i.p. to mice at a dose of 30 mg/kg"*.

> "Administration of GSK3β inhibitor lithium chloride effectively ameliorated the seizure susceptibility in mice, and its efficacy is better than the commonly used anticonvulsant drug ethosuximide."

`surface: body` · Discussion. 🔴 **This sentence ranks the two drugs the opposite way from the one that matters
here.** On the paper's own figures, lithium's suppression carries a significance bracket in **all three**
genotypes including wild type (manifest entry 22, Fig. 7d read at native 1946×1627), while ethosuximide is
`n.s.` in `+/+` and `+/−` and significant only in `−/−` (entry 1). **The drug the authors prefer is the one
without genotype specificity.**

> "Future studies, as well as more evaluations, will be needed to test whether GSK3β inhibitors may be promising candidates for treatment of human neurological disorders due to loss or dysfunction of WWOX."

`surface: body` · Discussion, closing sentence. 🔴 **Mood check, as required.** This is the paper's therapeutic
proposal and it is written as an **open question**. Any downstream text rendering it as a finding is re-voicing.

### 5.3 Quoted from LEGEND's receipted manifest — PMID 25012504 (Abu-Remaileh & Aqeilan 2014)

Receipt `FTR-20260814-25012504-01`, `complete_fulltext_read`, source fingerprint `2a0de55a1c…`, 22 locators,
strict PASS. **Not re-fetched in this session**: `PMC4211377` returns `full_text: ""`.

> "Strikingly, treatment with digoxin caused a fast and specific increase in blood glucose levels specifically in KO mice (Figure 5c)"

`surface: body` · Results, *"knocking down HIF1α rescues the metabolic phenotype"*.

> "Concomitantly, lack of WWOX causes a reduction in oxygen consumption (Figure 2b), suggesting that in Wwox-deficient cells glucose is utilized primarily for glycolysis, whereas mitochondrial respiration is inhibited"

`surface: body` · Results, enhanced glycolysis / reduced mitochondrial respiration.

> "Notably, we observed higher levels of Pdk1, which phosphorylates and inhibits pyruvate dehydrogenase, the rate-limiting enzyme that regulates entrance of pyruvate into the TCA cycle"

`surface: body` · Results, *"WWOX directly inhibits expression of HIF1α target genes"*.

> "As seen in Supplementary Figure S6A, only GST-WW1 domain-containing vectors were able to precipitate HIF1α"

`surface: body` · Results, *"WWOX physically interacts with HIF1α"*. This is the WW1 constraint behind `H-2`.

> "Whether WWOX affects PHD2 activity is to be determined."

`surface: body` · Discussion. The proposed degradation route is explicitly unresolved by the authors.

**Panel-level bounds** (same receipt, figures inspected at native resolution; `panel_only`): Fig. 5c — KO ~10 →
~115 mg/dl at 40 min, WT visually ~105 → ~75 with **no test drawn**; Fig. 2f — succinate `P<0.09`, i.e. not
significant; Suppl. Fig. S5 — digoxin transcript arms `n=2`/condition, no inferential statistics shown, and the
panel letters B/C conflict between panel title and legend.

### 5.4 Quoted from LEGEND's receipted manifest — PMID 42397075 (Steinberg … Aqeilan 2026)

Receipt `FTR-20260810-42397075-04`, 30 locators, strict PASS. No PMC deposit exists.

> "we performed a MYC inhibition experiment, using a multi-kinase inhibitor (A51) established to suppress Wnt and MYC expression"

`surface: body` · Results p. 11. Dose `125 nM`, weeks 8→15.

> "Consistently, neuron-targeted AAV9-hSynI-WWOX restoration effectively rescued neuronal functional phenotypes without correcting RG abnormalities, suggesting that optimal therapeutic intervention may require stage and cell-type-specific targeting depending on disease progression."

`surface: body` · Discussion p. 16.

> "Experiments were performed in independent differentiations, except for single-cell RNA-seq, MYC inhibition and NSCs CHIP-Seq, using multiple biological replicates"

`surface: body` · Statistical analysis, supplementary File009.

> "No randomization or blinding was applied in this study."

`surface: body` · Materials and methods, *Statistical analysis*, p. 5.

**Panel-level** (Suppl. Fig. 7F–G, read at 170 ppi and re-read at 258 ppi, `panel_only`): WT-NT / WT-DMSO /
KO-1B / KO-1B+A51 — SOX2⁺ ≈27 / 28 / 60 / 33 (`**`, `**`, `ns` vs WT); SOX2⁺MYC⁺ ≈48 / 45 / 72 / 50; NEUN⁺
≈30 / 22 / 6 / 18 (`*` KO vs A51, `ns` vs WT); **SATB2⁺ ≈1.4 / 1.45 / 0.35 / 0.7 (`ns` KO vs A51)**;
**CTIP2⁺ ≈12.5 / 5.5 / 0.2 / 0.3 (`ns` KO vs A51, still `****` below WT)**.

---

## 6. What LEGEND already knew · what is new

### 6.1 Already in LEGEND before this node opened — do not re-derive

| Already held | Where |
|---|---|
| Digoxin is the only approved drug correcting a *Wwox*-dependent phenotype in vivo; **it is target validation, not a candidate** | `DL-MOL-009` · `N-07` in `mechanism_intervention_map.md` |
| The in-vivo endpoint is **acute blood glucose**, not glucose uptake; the digoxin transcript panels are **GLUT1/PHD3**, not PDK1; the `100 mg/kg` dose is **printed in both HTML and PDF** and cannot be silently rewritten; "specific" describes the KO rise, not a tested WT null effect | `DL-MECH-095`, corrections 1–4 (2026-08-14) |
| WWOX binds HIF1α via **WW1**; the metabolic lever may be worth **less** in a missense-carrying class than in a null class | `DL-MECH-028` · `H-2` |
| The human/Lodz arm measures the oxidative half as **null** (citrate synthase unaffected, PDH activity unchanged), glucose uptake **changes sign** by condition, and the review re-voices a sentence its own primary's Results contradict | `DL-MECH-020` update of 2026-09-21 |
| d-APV abolishes the burst in the WWOX-deficient slice ⇒ **T1 for the tool compound**; CBX is non-attributable; the pannexin blocker went the wrong way (`N-16`) | `therapeutic_translation_second_pass.md` §3.4 · `E-1` discharged |
| Lithium's PTZ suppression is significant in **all three genotypes including wild type** | `N-02` · `DL-MECH-095`-adjacent · manifest `PMID32000863.json` entry 22 |
| A51 is not MYC-selective; the rescue is partial and selective; BLOCK-1 Wnt-suppression-during-corticogenesis question open | **`DL-THER-089`** — which already contains the full Suppl. Fig. 7F–G table |
| Zfra / pTyr33 / WWOX-mimetic peptides are a category error or a rejected safety argument | `N-09` · `DIS-009` · `HYP-20260705-05` |
| Seizure control must not be scored as developmental protection | `N-15` |

### 6.2 New — produced by this node

1. 🔴 **The operator's framing premise is wrong, and the correction is worth more than the lead would have been.**
   "LEGEND's therapeutic portfolio has NO entry for HIF1α inhibition" is **false**: `DL-MOL-009` (2026-07),
   `DL-MECH-095` (2026-08-14) and `N-07` all carry it, and all three already classify it as target validation.
   **This node cannot be scored as a therapeutic-roadmap gain on the HIF1α axis.** Rule 6 (`FLAG FIRST, SCORE
   ONLY AFTER VERIFICATION … whether LEGEND already knows it`) is what caught this.
2. ✅ **Ethosuximide is an unscored entry, and it carries something nothing else in the portfolio has.** It is a
   **genotype-specific in-vivo pharmacological effect in a WWOX-null animal**: `n.s.` in `+/+` and `+/−`,
   significant in `−/−`, at `150 mg/kg` i.p., 45 min before `30 mg/kg` PTZ. Lithium — the entry LEGEND *does*
   carry — **fails exactly the test ethosuximide passes**, in the same figure of the same paper. There is no
   `TX-`, no `R-` and no `HYP-` record for ethosuximide anywhere in the portfolio; `mechanism_intervention_map.md`
   names it only as the contrast that convicts lithium. **Flagged, not scored** — the alternative explanation
   (a low-dose-PTZ floor in the non-null genotypes leaving nothing to suppress) is untested, the endpoint is a
   **provoked** seizure rather than the spontaneous one, and under `N-15` seizure control is not development.
3. ✅ **TX-004's class is decided, and it splits.** "Corrected by rescue" in the Steinberg/Aqeilan organoid work
   is **two different interventions** and TX-004's text does not distinguish them. WWOX restitution
   (AAV9-hSynI-WWOX) → `GENE REPLACEMENT`, **REQUIRES WWOX**, and by the authors' own sentence it *"rescued
   neuronal functional phenotypes without correcting RG abnormalities"*. A51 → **`DOWNSTREAM WWOX-INDEPENDENT`**,
   a real pharmacological arm in a human WWOX-null neural tissue — **but the reagent suppresses Wnt as well as
   MYC, so the axis TX-004 names is not the axis the experiment isolates**, and the rescue stops before the
   layer-neuron output. TX-004's `INFERENCE` tag survives; its *mechanism sentence* does not.
4. ✅ **A field-density measurement for this node.** `Wwox AND (animal model) AND (nine named drugs)` = **3
   PubMed records total**, all three already in LEGEND. The neuro-intervention intersection = **25 records
   total**. **There is no fifth intervention arm to find.** The class is not under-read; it is under-populated.
5. ✅ **Retrievability measured, not assumed.** `PMC4211377` (the HIF1α primary) returns `full_text: ""` through
   this deployment — a PMCID with no body, exactly the case the environment note warns about. `PMC8609180` and
   `PMC6990504` return full bodies. `PMID 42397075` has **no PMCID at all**.

---

## 7. Corrections against prior LEGEND text

| # | Where | What is wrong | What it should say | Severity |
|---|---|---|---|---|
| C-1 | `discovery_ledger_current.md` → `DL-MECH-020`, Finding line | *"L'inibizione di HIF1α (genetica **e** farmacologica) **reverte** l'uptake di glucosio in vitro e **in vivo**."* | The in-vivo **pharmacological** arm measures **acute blood glucose at 40 min in a *Wwox*-null mouse**; the in-vivo **genetic** arm is a **tumour xenograft growth** experiment. Only the **in-vitro** genetic arm measures uptake. `DL-MECH-095` corrected this on 2026-08-14 and the `DL-MECH-020` line was **not** rewritten — the correction lives in a different entry from the sentence that keeps being read | **high** — this exact sentence is what launched this node |
| C-2 | `paper_registry_current.md` → PAPER 094 | *"manifest `deepdive_manifests/PMID42397075.json` (**6 locators**, schema v2, strict PASS, 0 gaps)"* | The manifest on disk contains **30 locators**, and `DL-THER-089` says 30. A reader trusting the registry would under-estimate the evidence behind the A51 finding fivefold | medium |
| C-3 | `full_text_queue_current.md` → FT-059 heading | *"🟡 superficie recuperata, **69 pannelli da leggere**, lettura NON iniziata"* | Stale. `FTR-20260814-34268881-03` records **all 11 figures / 69 panels inspected**, plus all five EV spreadsheets and the 47-page review file; `FTR-20260909-34268881-04` then re-verified every artefact byte-identical. The brief for this node inherited the stale line | medium |
| C-4 | `mechanism_intervention_map.md` → §4 R-04 / §5 N-02, and `therapy_levers.md` A2 | Ethosuximide appears **only** as the contrast that convicts lithium; `therapy_levers.md` A2 still calls lithium *"the strongest repurposing signal"* and says it *"abolishes seizures"* | Ethosuximide is the arm with genotype specificity and has **no record of its own**. `therapy_levers.md` has not absorbed `N-02` at all and still transmits the pre-correction reading | medium |
| C-5 | `therapeutic_strategies_current.md` → TX-004 | *"Steinberg 2024 identifies MYC overexpression as a key node of hyperexcitability in WWOX organoids, **corrected by rescue**"* | Ambiguous in the one place the class turns on. Split it: **WWOX restitution corrects hyperexcitability (requires WWOX)**; **A51 corrects progenitor identity and NEUN, not SATB2/CTIP2, and is not MYC-selective**. Also: MYC is the top upregulated gene in **radial glia**, which is a **neurogenesis** node; "hyperexcitability node" is the wrong compartment for that sentence | medium |
| C-6 | `therapy_levers.md` → C2 | *"In WOREE-derived brain organoids, WWOX re-expression **corrected** cortical/molecular CNS anomalies"* | The rescue is supraphysiological, ubiquitously promoted and **partial**, with a **seventeen-fold spread** in restored WWOX protein across lines (0.4 to 7 × wild type) and markers that **overshoot** rather than normalise (SATB2 up to ~11 × WT; TCF-4 at 0.3 × WT). "Corrected" is the authors' framing, not the panels' | medium |

None of these files was edited. All six are recorded here as material for a commit candidate.

---

## 8. The single best next experiment for this class

> **Deconvolve A51 in the one system where a downstream pharmacological arm has already worked: a four-arm,
> dose–ranged, blinded, independently-differentiated intervention in human WWOX-KO *and* WOREE patient-derived
> cortical organoids, comparing a selective MYC inhibitor, a selective Wnt/tankyrase inhibitor, A51 itself and
> vehicle — with a WT-treated arm at every dose — reading, in the same organoids, both the progenitor endpoint
> A51 moved (SOX2⁺, SOX2⁺MYC⁺, NEUN⁺) and the layer endpoint it did not (SATB2⁺, CTIP2⁺), plus MEA burst
> frequency and phase–amplitude coupling.**

**Why this one and not another.** It is the only experiment that (i) acts on the **single pharmacological arm that
has ever produced rescue in human WWOX-deficient neural tissue**, (ii) resolves the attribution failure that caps
TX-004 at `INFERENCE` — *is the active axis MYC, Wnt, or neither* — (iii) supplies the **dose–response with a
treated wild-type arm** that `DL-THER-089`'s BLOCK-1 question demands before anything moves past `IPOTESI`
(suppressing Wnt during corticogenesis is the mechanism of benefit and the mechanism of harm, and the window
between them is measured nowhere), (iv) repairs the three declared method defects in one pass — **independent
differentiations**, **randomisation and blinding**, and **more than one clone** — and (v) extends the arm from the
engineered null to a **patient** genotype, where the target is already known to be present (MYC is up in radial
glia of KO, WOREE and SCAR12 at comparable magnitude) but the intervention has never been tried.

**What each outcome decides.** Selective MYC inhibitor reproduces A51 ⇒ TX-004's mechanism sentence is correct and
the class is `DOWNSTREAM WWOX-INDEPENDENT` with a named target. Wnt inhibitor reproduces it ⇒ the lever is R-03,
not TX-004, and it inherits R-03's paediatric safety liabilities. Neither reproduces it ⇒ A51's effect is
off-target and the only human-neural pharmacological rescue in this literature dissolves — **a productive
negative, and the cheapest way to learn it.** If any arm moves SATB2⁺/CTIP2⁺, the class gains its first
*developmental-output* endpoint rather than another marker of cell identity.

*Runner-up, already specified inside LEGEND and not displaced by this node:* `E-9`/`E-D2` — memantine
dose–response on MEA in WWOX-null neurons/organoids with parental and rescue lines as internal comparators. It
tests the node with the strongest causal dependence (d-APV → burst frequency zero) using the approved compound
that has **never** been given to a WWOX system. It ranks second here only because the MYC/Wnt arm is the one with
an existing human-neural result to explain.

---

## 9. Source attribution

Retrieved from **PubMed / PubMed Central**. Bibliographic data, abstracts and the two full texts read in this
session were obtained through the PubMed MCP interface; figure-level values are re-used from LEGEND's own
fingerprinted, receipt-backed locator manifests and are labelled as such wherever they appear.

| PMID | Citation | DOI |
|---|---|---|
| 25012504 | Abu-Remaileh M, Aqeilan RI. Tumor suppressor WWOX regulates glucose metabolism via HIF1α modulation. *Cell Death Differ* 2014 | [10.1038/cdd.2014.95](https://doi.org/10.1038/cdd.2014.95) |
| 27308416 | Abu-Remaileh M, Seewaldt VL, Aqeilan RI. *Mol Cell Oncol* 2015 (commentary on the above) | [10.4161/23723548.2014.965640](https://doi.org/10.4161/23723548.2014.965640) |
| 34634460 | Breton VL *et al.* Altered neocortical oscillations and cellular excitability in a Wwox knockout mouse model of epileptic encephalopathy. *Neurobiol Dis* 2021 | [10.1016/j.nbd.2021.105529](https://doi.org/10.1016/j.nbd.2021.105529) |
| 32000863 | Cheng Y-Y *et al.* Wwox deficiency leads to neurodevelopmental and degenerative neuropathies and GSK3β-mediated epileptic seizure activity in mice. *Acta Neuropathol Commun* 2020 | [10.1186/s40478-020-0883-3](https://doi.org/10.1186/s40478-020-0883-3) |
| 42397075 | Steinberg DJ, Zonca A, Abdellatif D *et al.* Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids. *Brain* 2026 | [10.1093/brain/awag239](https://doi.org/10.1093/brain/awag239) |
| 34268881 | Steinberg DJ *et al.* Modeling genetic epileptic encephalopathies using brain organoids. *EMBO Mol Med* 2021 | [10.15252/emmm.202013610](https://doi.org/10.15252/emmm.202013610) |
| 33914858 | Repudi S *et al.* Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects. *Brain* 2021 | [10.1093/brain/awab174](https://doi.org/10.1093/brain/awab174) |
| 34747138 | Repudi S *et al.* *EMBO Mol Med* 2021 (AAV9-hSynI-WWOX) | [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599) |
| 42422765 | Obeid M *et al.* *Mol Ther Adv* 2026 | [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791) |
| 35328751 | Baryła I *et al.* *Int J Mol Sci* 2022 (WWOX/HIF1A, human fibroblast line) | [10.3390/ijms23063326](https://doi.org/10.3390/ijms23063326) |
| 36271927 | Baryła I *et al.* *J Mol Med* 2022 (review, same group) | [10.1007/s00109-022-02265-5](https://doi.org/10.1007/s00109-022-02265-5) |
| 29724996 | Abu-Remaileh M *et al.* *Cell Death Dis* 2018 | [10.1038/s41419-018-0510-4](https://doi.org/10.1038/s41419-018-0510-4) |
| 38542478 | Chang J-Y *et al.* Zfra Overrides WWOX in Suppressing the Progression of Neurodegeneration. *Int J Mol Sci* 2024 — **boundary case, not revived** | [10.3390/ijms25063507](https://doi.org/10.3390/ijms25063507) |
| 36828035 | *Prog Neurobiol* 2023 (Wwox^P47T knock-in) | [10.1016/j.pneurobio.2023.102425](https://doi.org/10.1016/j.pneurobio.2023.102425) |
| 35573960 | Riva A *et al.* *Front Pediatr* 2022 (WOREE null/null case; KD and vigabatrin ineffective) | [10.3389/fped.2022.847549](https://doi.org/10.3389/fped.2022.847549) |
| 39101447 | *Mol Genet Genomic Med* 2024 (WWOX-DEE, vigabatrin) | [10.1002/mgg3.2500](https://doi.org/10.1002/mgg3.2500) |
| 34015398 | "WWOX activation by toosendanin suppresses hepatocellular carcinoma metastasis…" — **WWOX-replete, induction; not transferable**. The ID converter returned **no DOI** for this record | — |

---

**End.** Not medical advice. Read-only toward every canonical file; nothing here was promoted, and nothing here
was committed.

---
---

# WAVE 2 — The mechanism behind the ethosuximide result

**Question:** ethosuximide is a T-type Ca²⁺ blocker and the first-line drug for **absence** epilepsy, whose
signature is the **spike-wave discharge**. Is its genotype-specific efficacy in the *Wwox*-null mouse
**mechanistically predicted** — i.e. do these animals have SWDs, is there a T-type channel abnormality, and is
the human disease an SWD/absence disease?

> Same layer discipline as Wave 1. READ-ONLY toward every canonical file. Nothing promoted, nothing committed.
> **Not medical advice.**

## W2.0 — The one-paragraph answer, before the evidence

**The mouse half of the hypothesis survives and the human half does not.** *Wwox*-null pups **do** have spike-wave
discharges — measured for the first and only time by continuous ECoG from P14 over 7 consecutive days, scored by a
blinded investigator, and suppressed by high-dose neuronal WWOX gene therapy. So ethosuximide's genotype-specific
effect is **consistent with** an SWD-generating network rather than incidental. But three things block the
inference from becoming a mechanism. **First, the SWD is described and never characterised**: the string `Hz` occurs
**zero times** in the whole 48 780-character body of the only paper that reports it, so there is no discharge
frequency, no duration, no spectral analysis — the entity ethosuximide would be predicted to hit has never been
measured as a frequency. **Second, there is no T-type channel evidence of any kind**: `WWOX AND (CACNA1G OR
CACNA1H OR CACNA1I OR "T-type" OR Cav3.1 OR Cav3.2 OR "calcium channel")` returns **one record in the whole of
PubMed**, and that record is a gene-panel cohort that merely lists both genes among forty-odd others. **Third, and
decisively, the human electroclinical picture is not absence epilepsy**: the WWOX-DEE cohort that looked hardest
reports *"they did not show the mandatory EEG hallmark of LGS of <2.5 Hz slow spike–wave"*, the recorded pattern
across cohorts is **hypsarrhythmia / West syndrome / multifocal epileptiform activity**, and the word "absence"
enters the WOREE literature only through a **seizure-type list transmitted twice from the same laboratory's
Introductions**, citing a review, never from any cohort's own EEG. And **ethosuximide has already been given to a
WWOX patient**: one adult WWOX-DEE case lists it among seven antiseizure medications, with *"No sustained positive
effect of treatment was detected."* ⇒ **The lead is real as mouse pharmacology, unexplained as mechanism, and
bounded as translation. It is `SYMPTOMATIC`, and `N-15` bars it from being counted as anything more.**

## W2.1 — Read depth for Wave 2

| PMID | Identity | Depth **this session** | Returned body length | Figure access |
|---|---|---|---|---|
| **42422765** | Obeid *et al.* 2026, *Mol Ther Adv* — dose-ranged neuronal WWOX gene therapy | **full body read in-act** (Intro → Results → Discussion → Methods) | **48 780 characters (measured exactly)** | none. Panel values re-used from LEGEND manifest `PMID42422765.json` (`FTR`-backed, 29 locators) |
| **34747138** | Repudi *et al.* 2021, *EMBO Mol Med* — AAV9-hSynI-WWOX | **full body read in-act** | non-empty, ≈19 000 characters (approximate; not instrumented) | none |
| 32000863 · 36779245 · 39507621 · 33916893 · 19500159 · 31543760 · 25649963 | LEGEND-held reads | **locator manifests + receipts consulted**, not re-fetched | n/a | n/a — all panel values carry their originating receipt |
| — | PubMed query `WWOX AND (CACNA1G OR CACNA1H OR CACNA1I OR "T-type" OR Cav3.1 OR Cav3.2 OR "calcium channel")` | executed | **1 record, `total_count: 1`** | n/a |

⚠️ **Scope of that zero.** It is a **search-index zero** over titles, abstracts and MeSH — not a full-text zero, and
not a biological zero. A T-type signal sitting in a supplementary DEG table is invisible to it. §W2.3 names exactly
where that blind spot is.

## W2.2 — Do *Wwox*-deficient rodents show spike-wave discharges?

### What LEGEND already held, before any search

`CLAIM 011` names **ECoG/SWD** among the rescued domains and is flagged for a separate reason (*"«dose-dependent»
descrive un continuo dove il pannello mostra una soglia"*). The discovery ledger's promoter-comparison entry
records **"SWD ridotti p<0.0001"**. Both trace to **one** paper, `PMID 42422765`. LEGEND's own manifest for it
already carries the panel bounds: **panel 7E — `****` WT-vs-KO, `****` KO-vs-HD, `ns` WT-vs-HD**, and, separately,
**panel 7C prints `0.2000` above the WT-vs-KO bracket for average spikes/day at `n = 5` per group while the running
text calls that same comparison "a significant elevation"** — a text-versus-panel contradiction already recorded.

### What the primary actually says — verbatim, fetched in this act

> "In addition to elevated spike activity, KO pups exhibited prominent spike-wave discharges (SWDs), characterized by rhythmic, high-amplitude spike-wave complexes, which were largely absent in WT animals (D). Notably, neuronal rescue of WWOX in KO pups using HD AAV-mediated gene delivery markedly reduced SWD incidence, restoring network activity toward WT levels (E)."

`surface: body` · Results, *"WWOX deficiency promotes early epileptiform activity, while optimized AAV-mediated
WWOX delivery suppresses spike-wave discharges"* · PMID 42422765.

> "Continuous ECoG monitoring was performed in WT and-null pups beginning at approximately P14 after ICV administration at P0 of RI or AAV9-hSynI-hWWOX, respectively."

`surface: body` · same section. (⚠️ `Wwox` deleted by the extractor before "-null" — italic gene symbol.)

> "At P14, pups were anesthetized with isoflurane (1%–2%, adjusted for low body weight; Terrell, USP, Piramal Critical Care) and positioned in a stereotaxic frame … animals were implanted with a single-channel ECoG transmitter (model A3049F2; Open-Source Instruments, USA) … Two intracranial electrodes were placed epidurally: the recording electrode was positioned above the right dorsal cortex, and the reference electrode was placed contralaterally … Recordings were maintained for 7 consecutive days … ECoG traces were manually screened for interictal spikes and SWDs by a blinded investigator. Events were defined based on amplitude, duration, and morphology criteria established in previous mouse epilepsy models. A subset of events was cross-validated with time-synchronized video recordings to confirm electrographic abnormalities."

`surface: body` · Methods, *Surgery and ECoG data acquisition*.

> "Although based on a limited cohort, these findings support a direct role for WWOX in regulating early neuronal network excitability"

`surface: body` · same Results section — **the authors' own bound, quoted so it is not lost.**

### 🔴 What is measured, and what is only named

| Parameter ethosuximide's mechanism would require | Reported? |
|---|---|
| **Discharge frequency in Hz** | 🔴 **NO.** The string `Hz` occurs **zero times** in the entire body. `Hz` is roman type, so the extractor could not have deleted it — **this is an informative zero on a surface read in full in this act.** |
| Event duration (seconds) | 🔴 **NO numeric value.** The Methods say events were scored on *"amplitude, duration, and morphology criteria established in previous mouse epilepsy models"* — the criteria themselves are **not stated**, and no reference is resolvable from the extracted body |
| Age | ✅ implantation P14, 7 consecutive days |
| Quantification | partial — *"SWD incidence"*; panel 7E carries the brackets, the underlying counts are not in the text |
| Cohort size | not stated for the SWD panel in the body; the sibling spike panel is `n = 5` per group |
| Spectral / PAC analysis | 🔴 **NO** |
| Behavioural correlate of the SWD (arrest, automatism) | 🔴 **NO.** *"A subset of events was cross-validated with time-synchronized video"* — cross-validation that the event is electrographically real, **not** a behavioural classification |

⇒ **`DATO`: *Wwox*-null pups have rhythmic high-amplitude spike-wave complexes on ECoG from P14, largely absent in
wild type, reduced by high-dose neuronal WWOX restoration, in a limited cohort, scored blind.**
⇒ **`NOT DATO`: that these are 3 Hz generalised absence-type SWDs.** The one property that would license the
ethosuximide mechanism — **the frequency** — has never been measured in any WWOX model.

### 🔴 And the other Aqeilan-lab paper has no SWD at all — a provenance correction

`PMID 34747138` is repeatedly cited across LEGEND (`therapy_levers.md` C1, `mechanism_intervention_map.md` R-01,
`CLAIM 004`) as the source of the multi-domain rescue *"including SWD/ECoG"*. **Read in full in this act, it
contains no electrographic recording whatsoever.** Its electrophysiology is:

> "we determined next the neuronal hyperexcitability or epileptic activity in brains of P18-21 wild type (WT), null (KO) either injected with AAV9-mWwox or AAV9-hWWOX, null alone by performing cell-attached electrophysiology recordings"

> "The average firing rate over 30 WT, 30 KO+AAV9-mWwox, 30 KO+AAV9-hWWOX, and 45 KO recorded neurons was about 6-fold higher in KO pups compared to the WT pups."

`surface: body` · Results, *"Neuronal restoration of WWOX decreases hyperexcitability and neuroinflammation"*.
In that body, `SWD` = 0, `spike-wave` = 0, `ECoG` = 0, `EEG` = 0 (all roman-type tokens; informative zeros).
**Cell-attached firing rate from three mice per group is not an EEG phenotype.** All SWD evidence in this
literature comes from **one** paper, **one** cohort, **one** rig.

### The rat is the opposite kind of epilepsy, and LEGEND already established the mouse/rat split

From `PMID 34634460`'s Introduction, read in this act:

> "rats possessing a homozygous frame-shift mutation inshow ~10 Hz interictal spiking activity (~10 Hz) in baseline conditions, sound-evoked fast waves during wild-running, and 5-6 Hz spike and wave complexes with bursts of spikes during the clonic phase of sound-induced seizures ()."

The rat's spike-and-wave is **5–6 Hz, during the clonic phase of an audiogenic convulsion** — a convulsive, not an
absence, context. LEGEND's own read of the primary (`PMID 19500159`, receipt-backed, 30 locators) is sharper still:
*"Interictal spikes (at about 10 Hz) were sporadically observed in all lde/lde rats under non-stimulated
conditions"*; *"Excluding the 3 rats that died, 19 of 20 rats (95%) experienced at least once audiogenic seizure"*;
and its **Table 2** populates the *Epilepsy* row for the rat alone — *"Wild running and tonic–clonic convulsion"* —
leaving it **empty for both mouse models**. That paper also states *"Although neither epileptic seizures nor
abnormal behavior has been reported in Wwox KO (knockout) mice"* — the sentence on which LEGEND's `DIS-011`
already rests.

⇒ **Nothing in the rodent literature describes an absence-type, behaviour-arresting SWD. The rat's is convulsive;
the mouse's is uncharacterised.**

## W2.3 — Is there any T-type Ca²⁺ channel evidence in WWOX deficiency?

**No. And the measurement of that absence is the cleanest result in Wave 2.**

| Probe | Result |
|---|---|
| PubMed: `WWOX AND (CACNA1G OR CACNA1H OR CACNA1I OR "T-type" OR Cav3.1 OR Cav3.2 OR "calcium channel")` | 🔴 **`total_count: 1`.** The single hit is `PMID 41510857`, a drug-resistant-epilepsy WES cohort that lists `CACNA1H` and `WWOX` among ~45 genes mutated in different patients. **It is co-occurrence in a gene list, not a relationship.** |
| LEGEND `discovery_ledger_current.md` · `claim_registry_current.md` · every `analysis/` file | 🔴 **zero** substantive mentions of `CACNA*`, `T-type`, `Cav3` (the only hits are this file's own Wave 1 text) |
| hNPC shRNA transcriptome, `PMID 31543760` (Kośla 2019) | **read by LEGEND** — receipts `FTR-20260811-31543760-01` and `FTR-20260920-31543760-01`, both `partial_fulltext_read`; 10 locators, **none touching a calcium channel**. ⚠️ **`supplementary: not_read` in both receipts** — and the DEG tables are exactly where a T-type transcript would sit. **Declared gap, not a zero.** |
| Human WWOX-KO cerebral organoid transcriptome (`34268881`, GEO GSE156243) | LEGEND's read carries no calcium-channel locator; `DL-MECH-098` independently establishes that **no `E_GABA`, chloride, NKCC1/KCC2, GABA response or GABA pharmacology** is measured anywhere in it. The same is true for calcium channels |
| Zebrafish calcium result, `PMID 25649963` | **Read in full**, receipt `FTR-20260921-25649963-01`. 🔴 **Explicitly not usable here, and LEGEND already says why**: the calcium is *"un aggettivo, non un numero"* — the reported content is *"Patterns of Ca dynamics strikingly differed … with maximal Ca levels at the boundary between the edema and yolk"* and *"Relatively high rates"*, with **no ratio, no ΔR/R, no trace, no n, no p**, measured **only in siRNA embryos, only at 30 hpf, only after oedema had formed**, and **never in brain**. It is peri-oedema, cardiac and intestinal calcium. **It does not support a neuronal calcium-channel claim and is not used as one here.** |

⇒ **`IPOTESI`, unsupported: nobody has ever measured a T-type current, a Cav3 transcript or a Cav3 protein in a
WWOX-deficient neuron.** Ethosuximide's target has never been examined in this disease. Its efficacy in the null
mouse is therefore, at present, **a pharmacological fact without a mechanism** — and calling it "mechanistically
predicted" would be exactly the re-voicing this repository keeps catching.

## W2.4 — What kind of seizures do WOREE children actually have? 🔴 **This is the finding that bounds the lead**

### The one direct test, and it is negative

> "Although our patients had multiple seizure types, they did not show the mandatory EEG hallmark of LGS of <2.5 Hz slow spike–wave, 39 excluding this syndromic diagnosis. It is notable that this EEG feature was not reported for patients previously classified as LGS."

`surface: body` · Discussion, epilepsy-syndrome paragraph · `PMID 36779245` (Oliver *et al.* 2023, *Epilepsia*),
LEGEND receipt-backed, 20 locators. **A dedicated WWOX-DEE cohort looked for spike–wave on EEG and reported its
absence.** The threshold is the LGS hallmark (<2.5 Hz slow spike–wave), not the ~3 Hz generalised SWD of absence —
so this does not formally exclude absence — but it is the **only** cohort statement in this literature that tests
for a spike–wave pattern at all, and it is negative.

### What is recorded instead

> "Patient 2, with the longest follow‐up (21 years), showed progression to a diffuse low‐voltage background without epileptiform abnormalities"

`surface: body` · Results, *Electroencephalography* · `PMID 36779245`. The evolution is from **multifocal**
epileptiform activity to a low-voltage background — not a generalised spike–wave trajectory.

Across `PMID 33916893`'s Table S1, read by LEGEND at the row level, the recurring EEG entry is **hypsarrhythmia**
(*"Hypsarrhythmia/NA"*, *"hypsarrhythmia"*, *"Hypsarrhythmia, West syndrome"*, *"Hypsarrhythmia"* across four
separate genotype rows). In the severe null/null case report LEGEND read this session-series (`PMID 35573960`) the
opposite absence is recorded and is itself informative: `hypsarrhythmia`, `burst`, `spasms`, `West syndrome` all
occur **zero** times — it is not a West-syndrome case, which is why it is not comparable to the
vigabatrin-responsive spasms reported elsewhere.

### Where the word "absence" actually comes from — and it is one sentence, transmitted twice

> "The clinical spectrum of WOREE syndrome includes severe developmental delay, early onset of severe epilepsy with variable seizure manifestations (tonic, clonic, tonic–clonic, myoclonic, infantile spasms, and absence)."

`surface: body` · **Introduction** · `PMID 34747138`, read in this act, citing (Banne, …).

> "…intractable epilepsy, with seizure types such as tonic, clonic, tonic-clonic, myoclonic, infantile spasms, and absence seizures."

`surface: body` · **Introduction** · `PMID 42422765`, read in this act.

🔴 **These are not two observations.** They are the **same list, in the same order, from the same laboratory's
Introductions, five years apart**, both citing a review rather than a cohort. Neither paper measured a seizure type
in a patient. **The only other occurrence of "absence seizures" anywhere in LEGEND is Breton 2021's speculation
about *mouse* heterozygotes** — *"we cannot discount the possibility that heterozygotes have a form of absence
seizures that we are unable to detect visually"* — which is explicitly an admission of non-detection.

⇒ **`DATO`: the human WWOX-DEE electroclinical phenotype, as measured, is infantile epileptic spasms syndrome with
hypsarrhythmia, multifocal epileptiform activity and multiple seizure types.**
⇒ **`NOT DATO`: that it is an absence/spike-wave epilepsy.** The absence entry is a transmitted list; the one
cohort that tested for spike–wave found none. **This is the negative the coordinator asked for, and it holds.**

## W2.5 — Has ethosuximide ever been given to a WWOX patient? 🔴 **Yes. Once, on the record, and it is in LEGEND**

> "Various antiseizure medications have been prescribed: phenobarbital, valproic acid, carbamazepine, topiramate, levetiracetam, ethosuximide, and perampanel. No sustained positive effect of treatment was detected."

`surface: body` · *History of epilepsy* · `PMID 39507621` (Teplyshova *et al.* 2024, *Front Genet*) — LEGEND
receipt-backed, 19 locators. The patient is an adult WWOX-DEE case diagnosed *"38 years after the onset of the
disease"*, with four decades of daily seizures and respiratory decline from age 36.

**Exactly what this does and does not say.** It says ethosuximide was among seven drugs tried, and that **the list
as a whole** produced no sustained effect. It does **not** report a per-drug outcome, a dose, a duration, a seizure
count, or an EEG response to ethosuximide specifically. `n = 1`, adult, retrospective. ⇒ **`DATO`: ethosuximide has
been used in a WWOX-DEE patient and appears in a list of drugs without sustained benefit.** ⇒ **`NOT DATO`: that
ethosuximide specifically failed.** Both statements must travel together, and the first is enough to demolish any
"nobody has tried it" framing.

**Census of the rest.** Across every LEGEND-held cohort manifest queried by row (`33916893`, `36779245`,
`30356099`, `40875931`, `42128308`), the AED entries recorded are **VPA + steroids**, **PB + VGB + ACTH**,
**PB + TPM**, **vigabatrin**, **CBD oil**, **clonazepam**, **clobazam**, **levetiracetam**, **rufinamide**,
**phenobarbital**, **nitrazepam**, **ACTH ×3 cycles**, **ketogenic diet**. **`ethosuximide` appears in exactly one
record in all of LEGEND** — `PMID 39507621`. The published responder rows LEGEND already extracted from
`33916893`'s Table S1 (*"VPA,steroids-yes"*, *"PB,VGB,ACTH-Yes"*, *"PB,TPM-Yes"*) contain no ethosuximide arm.

## W2.6 — Classification, honestly, and the bar that must not be crossed

| Field | Value |
|---|---|
| **Intervention** | Ethosuximide, `150 mg/kg` i.p., 45 min before PTZ `30 mg/kg` i.p. |
| **Therapeutic class (of the seven)** | **`SYMPTOMATIC`.** Its *mechanism of action* is downstream and WWOX-independent — it needs no WWOX to work — but its *demonstrated effect* is suppression of a provoked convulsion. `DOWNSTREAM WWOX-INDEPENDENT` describes the pharmacology; `SYMPTOMATIC` describes what was achieved, and the second is the one that governs the portfolio |
| **Applicable genotype class** | **null/null** only. Demonstrated in germline *Wwox*-null mice of **two independent targeting strains** (exon 1; exons 2/3/4). Not demonstrated in any splice, missense, CNV or residual-protein class, and not extrapolated to one here |
| **Evidence tier (T1–T6, LEGEND's ladder)** | **T1 for the compound in this model** — the intervention was applied to a WWOX-deficient animal and the WWOX-dependent phenotype changed, **with a genotype comparison that was run and reported**. That last clause is what lithium lacks, and it is the whole difference |
| **Verdict** | **FLAG. Not a therapeutic candidate. Not promoted.** |

🔴 **`N-15` is decisive and is not negotiable here.** In published WWOX children, cognitive and psychomotor
impairment **precedes** the epileptic encephalopathy and **does not improve** when epileptic activity is
controlled. Suppressing a chemically provoked convulsion in a mouse is symptomatic at best; even a complete
success would buy safety and quality of life, **not development**. Anyone reading this section as "a drug that
might treat WOREE" has crossed the bar this repository exists to hold.

**Three further bounds, stated rather than buried.** (i) The endpoint is **provoked**, not spontaneous — the mouse
has spontaneous seizures and they were not the readout. (ii) The **floor objection is answered but not eliminated**:
the coordinator is right that lithium's significant suppression in the `+/+` panel of the same figure proves a
suppressible response existed there, so ethosuximide's wild-type negative is a real negative — but the two drugs
were not given at matched effect sizes and no dose–response exists for either. (iii) The paper's own Discussion
ranks the drugs the **other** way — *"Administration of GSK3β inhibitor lithium chloride effectively ameliorated
the seizure susceptibility in mice, and its efficacy is better than the commonly used anticonvulsant drug
ethosuximide"* — and is therefore, on its own figures, **preferring the drug without genotype specificity**.

### What would be needed to move it one rung

1. **A spontaneous-seizure endpoint.** Ethosuximide vs vehicle read on **SWD count per day by continuous ECoG** —
   the endpoint `PMID 42422765` has now shown exists in this model — not on PTZ.
2. **A dose–response with a treated wild-type arm at every dose**, which closes the floor objection completely.
3. **The SWD characterised**: discharge frequency in Hz, duration, and behavioural correlate. Without a frequency,
   there is no absence-epilepsy claim to test.
4. **One T-type measurement in a WWOX-deficient neuron** — current or transcript. Today there are none.
5. **A human electroclinical re-look**: does any WWOX-DEE EEG carry generalised spike–wave? The only cohort that
   asked says no.

## W2.7 — The single best next experiment for WAVE 2

> **Continuous video-ECoG in *Wwox*-null pups from P14 for 7 days on the rig `PMID 42422765` has already built,
> with four arms — vehicle, ethosuximide, a mechanistically distinct comparator ASM, and a wild-type treated
> control — at three ethosuximide doses, blinded scoring, and a pre-specified primary endpoint of SWD events per
> 24 h, with discharge frequency (Hz), event duration and time-locked behavioural correlate reported for every
> discharge scored.**

It converts a provoked-convulsion result into a **spontaneous-network** result on the disease-proximal endpoint;
it supplies, as a by-product of the primary analysis, **the Hz and duration values that do not exist anywhere in
this literature**, which is what makes the absence-epilepsy hypothesis testable at all; it closes the floor
objection with a treated wild-type arm; and the entire apparatus — transmitter, electrode placement, blinded
scoring protocol, video synchronisation — is already validated in this exact model by the same group. **If SWD
count falls only in the null and the discharges are in the 5–7 Hz absence-like band, the mechanism is real and
ethosuximide becomes a genotype-matched symptomatic lever with a measurable endpoint. If SWD count does not fall,
or the discharges are outside that band, the T-type story dies cleanly** — and that is the better outcome to
learn early.

## W2.8 — What LEGEND already knew · what is new in Wave 2

**Already held:** `CLAIM 011` names ECoG/SWD among rescued domains and is already flagged on the
threshold-vs-continuum reading · the `p<0.0001` SWD reduction and the promoter comparison · `PMID 42422765`'s
panel 7C text-versus-panel contradiction and panel 7E bracket set · `DIS-011` (the *Wwox*-null **mouse**
epileptogenesis claim rejected, on Suzuki 2009's own sentence) · the `lde` rat's audiogenic, convulsive phenotype
at 95% penetrance and Table 2's empty mouse *Epilepsy* row · the zebrafish calcium result already demoted to
qualitative, peri-oedema and non-cerebral · Oliver 2023 read with 20 locators · Teplyshova 2024 read with 19
locators, **including the ethosuximide sentence** · `N-15`.

**New in Wave 2:**
1. **The SWD is named and never characterised.** `Hz` = **0** in the full 48 780-character body of the only paper
   that reports SWDs in a WWOX model. **The ethosuximide mechanism has no frequency to stand on.**
2. **A provenance correction on the SWD source.** `PMID 34747138` contains **no ECoG, no EEG and no SWD** — its
   electrophysiology is cell-attached firing rate, ~6-fold, 3 mice per group. All SWD evidence in this literature
   is **one paper, one cohort, one rig** (`PMID 42422765`). Several LEGEND surfaces cite the 2021 paper for a
   phenotype it does not contain.
3. **A measured field-level zero on the drug's target**: `total_count: 1` for WWOX × T-type/Cav3/calcium-channel,
   and that one record is a gene-list co-occurrence.
4. **The "absence" entry is a single sentence transmitted twice** from one laboratory's Introductions, citing a
   review — not a cohort observation, and it is the only textual basis for reading WOREE as an absence epilepsy.
5. **The one direct human test is negative**: `PMID 36779245` reports the `<2.5 Hz` slow spike–wave hallmark
   **absent** in its WWOX-DEE cohort.
6. **Ethosuximide has already reached a WWOX patient** and sits in a list of seven drugs with *"No sustained
   positive effect"* — `n = 1`, adult, no per-drug outcome.

## W2.9 — Corrections, with precise coordinates

**C-1 — the one the coordinator asked for.**

- **File:** `disease-models/wwox/research/discovery_ledger_current.md` · **line 460** (the `**Finding (DATO)**`
  line of `DL-MECH-020`)
- **Exact current text (substring, verbatim):**
  `L'inibizione di HIF1α (genetica *e* farmacologica) **reverte** l'uptake di glucosio in vitro e in vivo.`
- **The correction that already exists elsewhere and was never applied here** — same file, **line 3243**, inside
  `DL-MECH-095`, verbatim:
  `- **Correzione 1 — endpoint:** \`DL-MECH-020\` dice che l’inibizione farmacologica reverte l’uptake di glucosio *in vivo*. Il topo misura invece **glicemia ematica acuta**, 40 minuti dopo una singola iniezione; nessun uptake, flux, durata, sopravvivenza o endpoint neurologico in vivo.`
- **Exact proposed replacement for line 460's substring:**
  `L'inibizione di HIF1α **reverte l'uptake di glucosio solo in vitro** (shHIF1α in MEF Wwox-KO). **In vivo** i due bracci misurano altro: il braccio **genetico** è la crescita di uno **xenograft** di MEF KO trasformati, e il braccio **farmacologico** (digossina) misura la **glicemia ematica acuta a 40 minuti**, n=3/gruppo. ⚠️ Vedi \`DL-MECH-095\` Correzione 1, che questa riga non aveva recepito.`
- **Why it matters:** the corrected statement lives in a **different ledger entry** from the sentence that keeps
  being read. Readers reach line 460 and stop. This is the single sentence that sent Wave 1 chasing a lead LEGEND
  had already bounded a month earlier.

**C-2.**

- **File:** `disease-models/wwox/registries/paper_registry_current.md` · **line 7161** (PAPER 094)
- **Exact current text:**
  `**Evidence depth:** complete_fulltext_read — \`FTR-20260810-42397075-04\`; manifest \`deepdive_manifests/PMID42397075.json\` (6 locators, schema v2, strict PASS, 0 gaps)`
- **Exact proposed replacement:**
  `**Evidence depth:** complete_fulltext_read — \`FTR-20260810-42397075-04\`; manifest \`deepdive_manifests/PMID42397075.json\` (**30 locators**, schema v2, strict PASS, 0 gaps)`
- **Evidence:** the manifest on disk parses to **30** entries; `discovery_ledger_current.md` **line 2333**
  (`DL-THER-089`) independently states `manifest \`PMID42397075.json\`, **30 locator**, \`MANIFEST STRICT PASS\``
  and records that the count was revised upward from 25 on 2026-08-10. The registry line is the outlier.

**C-3.**

- **File:** `disease-models/wwox/research/full_text_queue_current.md` · **line 2471**
- **Exact current text:**
  `## FT-059 — Steinberg 2021, organoidi: 🟡 superficie recuperata, **69 pannelli da leggere**, lettura NON iniziata`
- **Exact proposed replacement:**
  `## FT-059 — Steinberg 2021, organoidi: 🟢 **lettura completata** — 11 figure / 69 pannelli ispezionati (\`FTR-20260814-34268881-03\`), artefatti ri-verificati byte-identici (\`FTR-20260909-34268881-04\`); debito residuo: **Appendix Figs S1–S6 non distribuite dall'editore**`
- **Evidence:** receipt `FTR-20260814-34268881-03` coverage map reads `figures: read`, `methods: read`,
  `results: read`, `discussion: read`, `references: read`, `tables: read`, `supplementary: unavailable`; its
  evidence basis states *"All 11 native article and Expanded View figures were inspected, covering 69 labelled
  panels."* The file already carries an append-only correction at **line 3437**
  (`## CORREZIONE APPEND-ONLY FT-059 …`), but **the heading a reader sees first was never updated** — which is how
  the stale line reached this node's brief.

**C-7 (new in Wave 2).**

- **Files:** `disease-models/wwox/analysis/therapy_levers.md` (§C1) and
  `disease-models/wwox/analysis/mechanism_intervention_map.md` (§4, R-01 `WWOX_DIRECT_EVIDENCE` row)
- **Issue:** both attribute the multi-domain rescue **"including SWD/ECoG"** to Repudi/Aqeilan **2021**
  (`PMID 34747138`). That paper, read in full in this act, contains **no ECoG, no EEG and no SWD** — its
  electrophysiology is cell-attached firing rate. The SWD/ECoG evidence belongs **solely** to `PMID 42422765`
  (Obeid 2026), where it is a single limited cohort.
- **Proposed:** attribute SWD/ECoG to `PMID 42422765` and carry its bounds (P14 onset, 7-day recording,
  limited cohort, no Hz, no duration, panel 7C's `0.2000` printed against the text's "significant elevation").

## W2.10 — Source attribution (Wave 2 additions)

Retrieved from **PubMed / PubMed Central**.

| PMID | Citation | DOI |
|---|---|---|
| 42422765 | Obeid M *et al.* Neuron-specific WWOX gene therapy produces dose-dependent, durable rescue in a model of WWOX-related epileptic encephalopathy. *Mol Ther Adv* 2026 | [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791) |
| 34747138 | Repudi S *et al.* Neonatal neuronal WWOX gene therapy rescues Wwox-null phenotypes. *EMBO Mol Med* 2021 | [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599) |
| 36779245 | Oliver KL *et al.* *Epilepsia* 2023 — WWOX-DEE cohort; LGS excluded on the EEG hallmark | [10.1111/epi.17542](https://doi.org/10.1111/epi.17542) |
| 39507621 | Teplyshova AM *et al.* *Front Genet* 2024 — adult WWOX-DEE case; ethosuximide among seven ASMs | [10.3389/fgene.2024.1477466](https://doi.org/10.3389/fgene.2024.1477466) |
| 19500159 | Suzuki H *et al.* 2009 — *lde/lde* rat; audiogenic seizures, Table 2 species split | via PubMed (`FTR-20260806-19500159-01`; DOI not re-resolved in this session) |
| 31543760 | Kośla K *et al.* *Front Cell Neurosci* 2019 — WWOX-silenced human neural progenitors | [10.3389/fncel.2019.00391](https://doi.org/10.3389/fncel.2019.00391) |
| 32000863 | Cheng Y-Y *et al.* *Acta Neuropathol Commun* 2020 — the ethosuximide/lithium figure | [10.1186/s40478-020-0883-3](https://doi.org/10.1186/s40478-020-0883-3) |
| 34634460 | Breton VL *et al.* *Neurobiol Dis* 2021 | [10.1016/j.nbd.2021.105529](https://doi.org/10.1016/j.nbd.2021.105529) |
| 25649963 | Tsuruwaka Y, Konishi M, Shimada E. *PeerJ* 2015 — zebrafish Ca²⁺, **qualitative, non-cerebral** | [10.7717/peerj.727](https://doi.org/10.7717/peerj.727) |
| 41510857 | *Neurol India* 2026 — drug-resistant epilepsy WES cohort; the **only** PubMed record joining WWOX to a T-type channel gene, and only as a gene-list co-occurrence | [10.4103/neurol-india.Neurol-India-D-24-00886](https://doi.org/10.4103/neurol-india.Neurol-India-D-24-00886) |

---

**End of WAVE 2.** Not medical advice. Read-only toward every canonical file; nothing promoted, nothing committed.
