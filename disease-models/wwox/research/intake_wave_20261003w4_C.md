# Intake wave 4 — 2026-10-03 — Scientist C — group C, theme 5

`context_policy: SOURCE_FIRST`

Reader: Scientist C (ACTOR_ID `scientist`), intake wave 4 dispatched by the Orchestrator.
Branch `task/sci-C-20261003w4` from `main` @ 296cd5b. **Nothing here is medical advice.**

**Theme.** Epilepsy / CNS gene-therapy lessons transferable to a neuron-targeted AAV: promoter
specificity, dose-toxicity, therapeutic window, DRG toxicity and its immune prevention versus the
contradicting source, biomarkers of toxicity.

**Assigned question.** What does each source add to, or limit in, the claim that a neuron-targeted
AAV for a recessive, null-allele CNS disease can be specified with its risks *bounded in advance* —
which cell classes the promoter actually reaches, what the therapeutic window is between too little
and too much transgene, what the DRG and systemic toxicities are, whether they can be prevented or
only monitored, and which biomarker would detect them — and for each of those five parameters, does
the source *measure* it or assume it?

---

## 0 · The structural fact that governs every statement below

**None of the six sources mentions WWOX.** `grep -icE 'wwox|wox1|16q23|fragile site FRA16D'` over
each persisted artefact returns 0, six times out of six. This is not a defect of the selection; it
is the condition of the problem, and it is measurable:

| PubMed query (esearch 2026-10-03, `tool=LEGEND-research`) | Count |
|---|---:|
| `WWOX` | 710 |
| `WWOX AND (adeno-associated OR AAV)` | **2** |
| `WWOX AND dorsal root ganglion` | **2** |
| `WWOX AND neurofilament` | **1** |
| `AAV AND dorsal root ganglion AND toxicity` | 35 |

There is no WWOX AAV-safety literature to read instead. Every one of the five parameters must
therefore be **transferred** from another gene or another species, and the transfer limit must be
carried with it on every line. A lesson from *Gad1*, *SMN*, *DDX3X*, *GBA1* or *SOD1*, in mouse, rat
or macaque, **never bounds a WWOX claim unless that transfer is stated** — and for four of the five
parameters below, the honest conclusion is that it cannot be stated at all yet.

**No canonical claim is touched by this reading.** All four commit candidates are research-layer and
MINOR.

---

## 1 · The answer, in one table

For each parameter: is it measured, by whom, and what does the measurement *not* reach?

| Parameter | Best measurement in this set | Measured or assumed | What it does not reach |
|---|---|---|---|
| **Which cell classes the promoter reaches** | PMID 42349402: a 410-bp mouse *Gad1* cassette (`cmGAD67`) at 92.2 % ± 1.3 % inhibitory-neuron specificity after intravenous AAV-PHP.eB, with the PV bias quantified in both directions (≈85 % of PV⁺ neurons transduced; >60 % of transduced cells PV⁺; SST⁺ 10–15 %; other subtypes ≈25 %) | **MEASURED**, and the best-measured parameter in the group | The ≈8 % off-target fraction is never resolved by cell class. The promoter is **mouse-derived** and no human orthologue is tested. And the measurement is **route-contingent**: the same cassette falls to 63.9 % ± 4.1 % after direct parenchymal injection, which the authors attribute to local vector concentration. Specificity is therefore a property of cassette × route × dose, not of the cassette |
| **The therapeutic window between too little and too much** | PMID 41992613, the only source in the corpus that states it as a two-sided claim and the only one that builds a dose series | **LOWER LIMB MEASURED, UPPER LIMB INFERRED** | The upper limb comes from a *different construct* at a higher dose, and that cohort "did not undergo comprehensive necropsy or histopathological evaluation". The authors themselves write that measuring protein in that arm "would be valuable **to define this therapeutic window**". No window is expressed in units of protein. In primates the highest dose tested became the NOAEL, so **no toxic dose was reached at all** |
| **The systemic (non-CNS) toxicity of a CNS vector** | PMID 42458834: strong ubiquitous expression after an intra-CSF injection in newborn mice killed every high-dose animal within a week from **myocardial degeneration**, with hepatic steatosis and a >1000-fold cardiac *Ifnb1* rise, while a promoter-matched control vector with a different transgene elicited none of it | **MEASURED**, and it is the group's hardest negative | DDX3X's own roles in RIG-I/MAVS signalling, stress granules and *Ddit3* transcription are plausibly the mechanism, so the **magnitude does not transfer** to an arbitrary transgene. n per group is not reported. "The brain was overall unaffected" is a morphology statement: brain *Cxcl10* rose ≈23-fold in the same animals |
| **DRG toxicity: preventable or only monitorable** | **Contested.** PMID 41404412 (Biogen): prophylactic dexamethasone + tacrolimus (± MMF) cut DRG pathology from 10/26 to 1/29 and 11/36 to 1/36 ganglia across three cargos, one of which expresses no protein. PMID 35331006 (Novartis): prednisolone, or rituximab + everolimus, did not mitigate it at all | **MEASURED ON BOTH SIDES, AND THE TWO DISAGREE.** Characterised in § 2; **not decided here** | Neither side measures what a WWOX programme would need: n = 3 per group on one side, n = 2–3 per sex per cell on the other; healthy animals with no efficacy endpoint; longest arm 43 days against a predicted six-month requirement; no infant, no human |
| **Which biomarker would detect it** | PMID 36700120: 260 macaques, 18–21 DRG each, blood and CSF NfL against a peer-reviewed composite histopathology endpoint — **with per-animal operating characteristics**: ROC AUC 0.85 (blood) / 0.81 (CSF) for any finding, 0.95 / 0.94 excluding minimal grade, and sensitivity/specificity at five fold-change cut-offs (1.5× → 0.73/0.71 blood). PMID 41404412 adds CSF CXCL10 and MIP1α as earlier-rising candidates | **MEASURED, for nonclinical use only** | Not clinically validated by the authors' own statement. Post-dose **vehicle-control** NfL rises above pre-dose in both matrices, so the procedure itself moves the marker. Raised NfL "is not disease specific". Only fold-change-from-pre-dose cut-offs exist, which presupposes a stable individual baseline — and under LEGEND_CORE §13 NfL is **Tier 3** with respect to WWOX: it is a biomarker of vector toxicity, never a WWOX disease biomarker, and it belongs in a separate file |

### The answer to the question as asked

**Two of the five parameters can be bounded in advance today; three cannot.**

Bounded: **cell-class reach** (by directly measuring it in the species and by the route intended, as
PMID 42349402 shows how to do) and **a surveillance assay for the dominant class toxicity** (blood
NfL, with the operating characteristics PMID 36700120 supplies, used nonclinically and declared Tier 3).

Not bounded: the **upper limb of the therapeutic window** (no source in this corpus or in wave 3's
corpus measures one; the best attempt explicitly says so); the **systemic organ at risk** (knowable
only per transgene, and the one source that measured it found the risk organ was the heart, not the
brain, after a CSF injection); and **whether DRG toxicity is preventable** (two regulatory-grade
primate datasets disagree, and the disagreement is not yet resolvable from either).

A WWOX programme cannot inherit any of the three unbounded parameters. It can inherit the three
*methods* that would measure them.

---

## 2 · The DRG contradiction, characterised and not decided

PMID 41404412 vs PMID 35331006. The source does part of the work itself: PMID 41404412's **reference
14 is PMID 35331006** (dereferenced by hand from the JATS bibliography), and it names that result as
the one it contradicts.

| Axis | PMID 41404412 (Grubor 2025) | PMID 35331006 (Tukov 2022) |
|---|---|---|
| **Species / strain** | Cynomolgus macaque, 2–4 y (hSMN1) and 2–3 y (hGBA1, mir-SOD1) | Cynomolgus macaque, 13–19 mo (12-month study, Asian origin) and 25–34 mo (13-week mechanistic study, **Mauritius** origin) |
| **Vector / cargo** | AAVhu68-ss-coSMN1; AAV9-hGBA1 (CAGGS + WPRE); **AAV9-mir-SOD1, a non-protein cargo** | scAAV9 onasemnogene abeparvovec (CMV enhancer / chicken-β-actin, human *SMN*) — one cargo only |
| **Dose** | 3.68 × 10¹³ / 3.5 × 10¹³ / 3.0 × 10¹³ / 4.0 × 10¹³ GC per animal; one dose per study | 1.2 / 3.0 / 6.0 × 10¹³ vg per animal (dose series); IT arm of the mechanistic study fixed at 3.0 × 10¹³ |
| **Route** | ICM (three studies) and IT lumbar (one); freehand or fluoroscopy, **no contrast agent** | IT lumbar (both), **0.20 mL Omnipaque 180 iohexol contrast immediately before the vector**; plus a separate 1.1 × 10¹⁴ vg/kg intravenous study |
| **Regimen tested** | Dexamethasone 0.5 mpk SID (CNS-penetrant) **+ tacrolimus 1 mpk SID (calcineurin inhibitor)** ± MMF 50 mpk BID; study #2 from day −2, study #3 from day −3, **study #1 from day 2** | Prednisolone 1 mg/kg/day from day −1; or rituximab 20 mg/kg q2w from day −14 **+ everolimus 0.5 mg/kg/day to day 14**. **No calcineurin inhibitor, no T-cell-directed agent** |
| **Readout** | Graded histopathology of DRG/TG/cord/roots/nerves; electron microscopy; DRG bulk RNA-seq + WGCNA; immune-cell ISH/IHC; CSF and serum cytokines; ELISpot; **serum NF-H (heavy chain)** | Graded histopathology of the same tissues; antisense/sense ISH; **nerve conduction velocity**; serum/plasma and CSF **NfL (light chain)**; lymphocyte immunophenotyping; clinical-trial and pharmacovigilance review |
| **Earliest time point** | **Day 5** (and day 9), i.e. before the lesion exists | **2 weeks**, i.e. after the lesion exists |
| **DRG sampling density** | ~9–12 DRG per animal (26, 29, 36 ganglia across three animals) | Not stated in the main text; per-level tables are in the unfetched supplement |
| **n per comparison** | 3 per group | 3 per sex interim, **2 per sex terminal** |
| **Sponsor** | Biogen (all but two authors; the other two at the contract facility) | Novartis (all authors), studies run to answer an **FDA partial clinical hold** on the sponsor's own product |
| **Result** | Pathology reduced across three cargos, transgene expression unchanged | Pathology unchanged by either regimen, including under 100 % B-cell depletion |

**What the disagreement is not.** It is not prophylactic-versus-therapeutic timing: PMID 35331006's
regimens began on day −1 and day −14, *earlier* than PMID 41404412's weakest arm (day 2). It is not
species. It is not an incompatibility of claims about immunity as such — PMID 35331006 scopes its own
negative to "primary **adaptive** immune responses" and states that "activation of the innate immune
response in transduced cells **was not excluded**".

**The three live explanations, none chosen here.**
1. **Drug class.** PMID 41404412's own reading: tacrolimus, a T-cell/calcineurin inhibitor, is the
   active element, and PMID 35331006 never tested that class. This is the most parsimonious, and it
   is also the self-serving one, offered by the party whose regimen worked.
2. **Power.** PMID 35331006's negative rests on two to three animals per cell with no power
   statement, and in its published female cervical-DRG table the prednisolone arm at day 92 shows
   degeneration in 2 of 2 animals against 1 of 2 unsuppressed — a direction that two animals cannot
   establish either way.
3. **Procedure and sampling.** Contrast agent in one and not the other; ~9–12 versus an unstated
   (supplement-only) number of ganglia per animal; different vector, promoter and cargo.

**Why it matters that it is unresolved.** If (1) holds, DRG toxicity is an *immune* toxicity with a
clinically feasible prophylaxis, and a neuron-targeted AAV's worst class toxicity becomes a
manageable risk. If PMID 35331006's mechanism holds instead — "a consequence of increased vector
genome transduction and/or transgene expression", which **both** papers' data support, since
PMID 36700120 shows empty capsid and promoter-less vectors cause neither lesion nor NfL rise — then
the only levers are dose, promoter and de-targeting, and immunosuppression buys nothing. These imply
opposite risk-mitigation plans, and no source in this group settles which is right.

**Non-independence, which changes how the two poles should be weighed.** PMID 35331006 and
PMID 36700120 are **not** two sources. Same sponsor, four shared authors (Tukov, Meseck, Penraat,
Chand), and PMID 36700120's data were "extracted from the Novartis study data warehouse". Three
descriptors match PMID 35331006's studies specifically: a Mauritius-origin non-GLP cohort, two
studies using Omnipaque 180 contrast, and an intravenous arm at ≈1.0 × 10¹⁴ vg/kg. Neither paper
cross-lists study identifiers, so overlap cannot be *proved* from these artefacts — but it is likely,
and the "two-against-one" appearance of the contradiction is therefore **one sponsor's dataset
against another sponsor's dataset**, not two independent replications against one.

---

## 3 · Per paper

All six: verdict **INGEST** (research layer), `partial_fulltext_read`, no WWOX content, no canonical
claim touched, no prior receipt, `reread_reason: first_read`. All six acquired lawfully and free from
Europe PMC REST `fullTextXML`, HTTP 200 with a body on the first attempt; nothing was paid for.
All six manifests `VERDICT: PASS` under `--verify-artifacts --require-current-schema`.
All six `dependency_integrity.py screen` → `SCREENED_CLEAN` (Retraction Watch snapshot 2026-09-10,
72 476 rows, sha256 `8ff64393b342e18ec2c04b06d54dba834e37e77575913c97fa93c8da41dde3d5`).
No retraction, expression of concern or erratum on any of the six.

| # | PMID | Short identity | New versus held | Receipt JSON |
|---|---|---|---|---|
| C1 | 42349402 | Fukai 2026 *Mol Ther* — 410-bp `cmGAD67` inhibitory-neuron promoter | New: the only quantified promoter-specificity measurement in the group, **and** the route-dependence of specificity. Held: nothing — no prior record | `sciC_42349402_1.json` |
| C2 | 41992613 | Song 2026 *Mol Ther* — EXG001-307, precision-optimised AAV9 for SMA (sponsor) | New: the only two-sided dose claim in the corpus, and the demonstration that its upper limb is unmeasured. Held: nothing | `sciC_41992613_1.json` |
| C3 | 42458834 | Boitnott 2026 *Mol Ther* — DDX3X overexpression toxicity (Gray lab) | New: the organ at risk from a CSF vector was the heart; lethal mouse dose scales to a dose in clinical use. Held: nothing | `sciC_42458834_1.json` |
| C4 | 41404412 | Grubor 2025 *Mol Ther Methods Clin Dev* — immunosuppression reduces DRG pathology (Biogen) | New: the pre-lesion day-5 time course and a three-cargo mitigation. Held: nothing | `sciC_41404412_1.json` |
| C5 | 35331006 | Tukov 2022 *Hum Gene Ther* — intrathecal onasemnogene DRG toxicity (Novartis) | New: the contradicting pole, with its power now measured. Held: nothing | `sciC_35331006_1.json` |
| C6 | 36700120 | Johnson 2022 *Mol Ther Methods Clin Dev* — NfL vs DRG injury, 260 macaques (Novartis) | New: per-animal operating characteristics for the toxicity biomarker wave 3 already carries as a bare threshold. Held: nothing | `sciC_36700120_1.json` |

Dossiers: `research/fulltext_dossiers/PMID{42349402,41992613,42458834,41404412,35331006,36700120}.md`,
each with an explicit "what I did not read". Manifests: the matching `.json` under
`research/deepdive_manifests/`.

### What each paper does NOT say (condensed; the dossiers carry the full lists)

- **C1** — no dose-response (one dose throughout), no toxicology of any kind, no human promoter, no
  chronic model, no large brain; and this is circuit modulation by *adding* GAD65, not restoration of
  a deficient protein.
- **C2** — no histopathology in the arm that defines the dose ceiling; DRG never harvested in mice;
  no window in units of protein; the miRNA de-targeting element is carried unconfirmed by the
  sponsor's own statement.
- **C3** — no graded severity scale in the main text; no cardiac function measurement; no DRG
  assessment; the mechanism "not mechanistically addressed in this paper"; and n per group absent
  from the running text and the deposited captions — but **present inside the Figure 2 and Figure 3
  plot legends** (n = 6 per sex for serum chemistry, n = 3 per group for the qPCR panels), which a
  text-only reading does not see. See § 3b.
- **C4** — no antigen-specific T cells detected; the effector mechanism is a postulate; n = 3 per
  group; no efficacy endpoint; nothing beyond 43 days against a predicted six-month requirement; and
  the authors state the immune mechanism **does not hold in mouse**.
- **C5** — does not state that immunity is uninvolved, only that *adaptive* immunity may not be
  critical; "resolution" explicitly redefined as lower incidence and severity, because neuronal loss
  is not reversible; human relevance declared unknown; no time point before 2 weeks, so it cannot
  see C4's day-5 events.
- **C6** — not clinically validated; no concentration threshold, only fold-change; strata not
  resolved in the main text; no mechanism and no mitigation tested, so it cannot adjudicate § 2.

### 3b · What opening five figure panels changed — including one of my own statements

The first pass of this reading was text-only, which the brief permits but which the ratchet in
`growth_anchors.py` does not: a manifest must declare, per locator, whether a panel bears on it.
Rather than write `text_only` over locators that a panel does bear on — the module's own comment
says "when no admitted value is true, the defect is the enum" — I fetched the five panels that bear
on a locator from the PMC open-data bucket and read them. Four of the five changed something.

| Panel | Relation | What it changed |
|---|---|---|
| C1 Figure 2D/2F | **qualifies the text** | The paper states once, for both cassettes, that "fewer than 50% of SST+ neurons were GFP positive". The panel plots them separately: cmGAD65 SST ≈27 %, but **cmGAD67 SST ≈51 %** — and cmGAD67 is the cassette carried into every therapeutic experiment. Figure 2F is the same shape: the PV enrichment the text calls selective against its own stated threshold of 1.5 sits essentially *on* 1.5 for cmGAD67, with animals from ≈1.2 to 1.8 |
| C2 Figure 5A/5C | **confirms the text** | Vehicle animals carry grade-1 and grade-2 DRG findings in the sacral and lumbar severity plots, so the procedural contribution is visible and not merely asserted; and CSF NfL peaks at day 15 in **all three groups including vehicle** |
| C3 Figure 2 and 3 legends | **panel-only information** | 🔴 **This falsified a statement I had already written.** My first-pass dossier said n per group was "not reported anywhere in the main text or in any figure legend". The group sizes *are* reported — inside the **plotted legends** of Figures 2 and 3, which the JATS caption does not carry: n = 6 per sex for serum chemistry, n = 3 per group for the qPCR panels. A text-only reading of a JATS deposit cannot see them |
| C3 Figure 3D | **qualifies the text** | The brain *Cxcl10* rise is a **single timepoint at the margin** — one bracket, p = 0.044, on the P5 bar, three animals — while the heart and liver brackets on the same axis read p = 0.002 and p < 0.001 on bars one to two orders of magnitude higher, and the brain facets of Figures 3B and 3C carry no bracket at all. The brain signal forbids the unqualified word "unaffected" and is too thin to call an effect |
| C4 Figure 5 | **qualifies the text** | The sentence claims day-5 infiltrates for four cell types. In the day-5 row CD20 shows a discrete focus and CD4 scattered signal, but NCR1, CD303 and CD68 are not visibly above the vehicle row, and the CD8 column is essentially unstained in every row including day 29. The quantification is in an unfetched supplement, so the panel neither confirms nor contradicts — it shows the sentence is not readable off the figure it points to |

**The method lesson, which is the reusable part.** Three of these five findings are invisible to a
JATS text extraction: group sizes inside a plotted legend, a significance bracket on one facet, and
which rows of a representative image actually differ. A reading that declares `figures:
captions_only` is not merely incomplete — it is incomplete in a direction that systematically
favours the authors' summary sentence, because the summary is what the text carries and the
qualification is what the panel carries. Three of the four changes above weakened a summary
sentence. None strengthened one.

**Coverage after this.** 1 of 8 panels opened for C1, 1 of 5 for C2, 2 of 3 for C3, 1 of 8 for C4,
0 of 5 for C5, 0 of 5 for C6. The receipts still declare `figures: captions_only`, which understates
what was done for four papers but is the safe direction and is the closest admitted value; each
receipt's `evidence_basis` names exactly which panels were opened.

### Internal inconsistencies found in the sources (all three are checkable, none is fatal)

1. **C1** — the focal-model dose is 1.0 × 10¹¹ vg/mouse in the body text for both vectors and
   1.0 × 10⁹ / 1.0 × 10¹⁰ vg/mouse in the Figure 8A legend. The focal-model result cannot be tied
   to a dose.
2. **C2** — the rat doses are normalised three incompatible ways (Table 1: 3.0 × 10¹² and
   6.0 × 10¹² vg/kg; Results: 4.3 × 10¹² and 8.5 × 10¹³; Methods: 4.3 × 10¹² and 8.5 × 10¹²), and
   the Results high-dose figure is impossible on its face. In the paper whose thesis is dose
   precision, the rat arm's exposure cannot be stated in vg/kg.
3. **C6** — the intrathecal dose range is 4.8 × 10¹² to 9.2 × 10¹³ vg/animal in Results and Table 3
   but 9.2 × 10¹⁴ in the Discussion; and the clinical-sign denominator is 193 in Results, 185 in the
   Discussion (the difference is the 8 empty-capsid and promoter-less animals).

### Reading-debt discharge (brief § 15)

**None owed and none discharged.** `paper_packet.py packet --pmid` returned, for all six,
"identity: DOI (none recorded) · (no title recorded)", "manifest: none — this is a first reading",
"prior read: depth=none · receipts=0" and "acquisition: no route recorded". No registry statement
anywhere in this repository rests on any of these six PMIDs, so no record id gains a primary from
this reading and no registry text needs correcting. That is also why candidate
`CC-20261003w4-C-REGISTRY-01` is necessary: without it these six become orphan complete-reads and
LINT blocks `BATCH_COMMIT` with `ORPHAN_COMPLETE_READ`.

---

## 4 · Relation to wave 3, and what changes

Read **after** the first pass was written, per `SOURCE_FIRST`:
`CC-20261003W3-C-RESTORATION-SPEC-01`. Three contacts, and all three **corroborate and sharpen** it
rather than overturning anything.

1. **The window negative survives, and is now stronger.** Wave 3 concluded that no therapeutic
   window has been measured for any DEE gene in its set. PMID 41992613 is the closest thing in this
   whole corpus to a two-sided window result — and it still does not measure one. Its upper limb
   confounds dose with construct, received no histopathology, and the authors name the missing
   measurement themselves. **Wave 3's negative now has a positive control that failed**, which is a
   better-supported negative than it was yesterday.
2. **The toxicity biomarker gains operating characteristics.** Wave 3 records PMID 40349107 using
   serum NfL with a threshold of "1,719 pg/mL or greater". PMID 36700120 supplies what that bare
   threshold lacks: a 260-animal denominator, ROC AUC 0.85/0.95, and sensitivity/specificity at five
   cut-offs — expressed as **fold change from pre-dose**, not as a concentration, which is itself a
   constraint on how the wave-3 threshold can be used.
3. **"DRG toxicity is an AAV class effect" is upheld, and its mechanism is contested.** Wave 3
   carries the class effect; this group supplies the live dispute about whether that class effect is
   immune-mediated and preventable. PMID 36700120 adds the constraint both poles must respect:
   empty capsid and promoter-less vectors cause neither lesion nor biomarker rise, so the lesion
   requires transgene expression whatever the effector arm turns out to be.

**One addition wave 3 did not have.** PMID 42458834 adds a *sixth* organ-risk lesson that wave 3's
set did not contain: after an intra-CSF injection the organ that killed the animals was the **heart**,
and the brain was morphologically spared. Wave 3's off-target-organ parameter was populated by DRG,
spinal cord and liver. It should now also carry the heart, and it should carry the reason — a strong
ubiquitous promoter on a dose-sensitive transgene — rather than the organ alone.

---

## 5 · What would change the model if true, and what would falsify this reading

**Would change it.**
- A head-to-head primate study giving dexamethasone + tacrolimus against prednisolone alone, same
  vector, same dose, same route, same contrast protocol, same ganglion sampling density, powered.
  That decides § 2, and § 2 is currently the largest single unknown in specifying a CNS AAV's risk.
- Any dosing study, in any gene, that holds brain transgene **protein** constant and still shows a
  toxicity threshold. That would convert the window's upper limb from inferred to measured.
- A measurement of how much WWOX protein, in which cell classes, is needed. Nothing in this corpus
  or in wave 3's bears on it, and `WWOX AND (adeno-associated OR AAV)` returns 2 records.

**Would falsify statements made here.**
- Evidence that PMID 35331006's immunosuppression arms were adequately powered — the published
  per-cell n of 2–3 is the basis for discounting its negative, and a power analysis showing
  sufficiency would remove that basis and make the contradiction biological rather than
  methodological.
- Study identifiers showing PMID 36700120's nine studies do **not** include PMID 35331006's studies.
  That would restore the two as independent sources and strengthen the "not preventable" pole.
- A WWOX measurement showing WWOX is *not* dose-sensitive, which would make the overexpression
  lessons (C2, C3) irrelevant rather than cautionary. Note that the converse also holds and is not
  assumed here: nothing in this reading shows WWOX *is* dose-sensitive.

---

## 6 · Anything in the brief or the selection that was wrong

| Statement | Verdict against the source |
|---|---|
| Selection on C6: "correlation with severity is not a per-animal detection threshold" | **WRONG.** PMID 36700120 Table 2 gives exactly a per-animal detection threshold: sensitivity and specificity at 1.5×, 2×, 3×, 5× and 10× fold change from pre-dose, in blood and CSF, plus ROC AUC. The threshold exists; what it lacks is clinical validation and a concentration (as opposed to fold-change) cut-off |
| Selection on C4: "prophylactic dexamethasone + tacrolimus" | **PARTLY WRONG.** True of studies #2 (day −2) and #3 (day −3); study #1 started on **day 2**, after dosing, per Methods — and study #1 is the arm with the weakest effect. This also removes "prophylactic timing" as an explanation of the C4/C5 disagreement, since C5's regimens began on day −1 and day −14 |
| Selection on C2: "'no sustained DRG pathology' is a statement about persistence, not absence — check interim time points" | **CORRECT, and now quantified.** Week-4 interim findings exist and are present in **vehicle** animals too (sacral axonopathy 2/4 vehicle, 1/4 low, 3/6 high); incidence is not dose-ordered; all resolved by week 26 |
| Selection on C3: "whether dose-response, n per group and histopathology scoring are fully reported needs checking" | **CHECKED: they are not.** Two doses with survival only; **n per group reported nowhere** in the main text or any figure legend; no graded severity scale in the main text (the pathologist's report is the unfetched Table S1) |
| Selection on C1: "'preferentially' needs a quantified off-target fraction from the body" | **PARTLY SATISFIED.** The PV bias is quantified in both directions, but the ≈8 % non-inhibitory fraction is never resolved by cell class. The more consequential finding the selection did not anticipate is that specificity is **route-dependent** |
| Selection on C5: "the disagreement may be methodological rather than biological — that is precisely what the body must be read to decide" | **Read, and NOT decided** — deliberately. § 2 lays out three live explanations and the evidence for each; the brief instructs characterisation without decision, and the sources do not license a decision |
| Brief § 6: "Do not describe the Orchestrator's selection as fact" | Applied. Six of the seven selection premises above were testable against the sources; two were wrong, one partly wrong |

---

## 7 · Commit candidates

| Candidate | Class | Target | Purpose |
|---|---|---|---|
| `CC-20261003w4-C-REGISTRY-01` | MINOR | `paper_registry_current`, `literature_tracking_log_current` | PAPER and LIT records for all six PMIDs, so none becomes an orphan complete-read |
| `CC-20261003w4-C-DRG-CONTRADICTION-01` | MINOR | `research/research_lines_current.md`, `research/dismissal_ledger_current.md` | The contradiction as a characterised open question, plus the negative that it is not yet decidable, plus the C5/C6 non-independence |
| `CC-20261003w4-C-WINDOW-SPEC-01` | MINOR | `research/research_lines_current.md`, `research/dismissal_ledger_current.md` | The five-parameter specification status, and the heart as a sixth organ-risk lesson for the wave-3 spec |
| `CC-20261003w4-C-TOXBIOMARKER-01` | MINOR | `research/research_lines_current.md`, `research/research_candidates_current.md` | The toxicity-biomarker panel with its operating characteristics, explicitly Tier 3 under LEGEND_CORE §13 and explicitly not a WWOX disease biomarker |

---

## 8 · Gate numbers

| Gate | Result |
|---|---|
| `deepdive_manifest.py --pmid <N> --verify-artifacts --require-current-schema` | **PASS**, 6 of 6, 0 gaps |
| `dependency_integrity.py screen --manifest-block` | **SCREENED_CLEAN**, 6 of 6; 1–4 refs each `UNSCREENABLE_NO_DOI`, 0 flagged; snapshot 2026-09-10, 72 476 rows |
| `fulltext_receipts.py validate` on a throwaway ledger copy with the six receipts appended | **OK: 326 valid receipt(s)** (320 → 326) |
| `fulltext_receipts.py verify` on the real ledger | **OK: 320 chained receipt(s), tail anchored** — untouched, as required |
| `legend_lint.py .` | exit 0, **0** `BLOCK_BATCH_COMMIT` or `BLOCK_SYSTEM` |
| `growth_anchors.py check` | **PASS** — anchors match. One `[BACKLOG] CANDIDATE_BACKLOG` at 20 candidates, expected: new candidates raise the backlog |
| `scripts/public_release_gate.py` | **VERDICT: PASS**, exit 0, **0** `[BLOCK]`; none of the standing `[REVIEW]` lines is in a file this task wrote |
| `scripts/test_section_references.py` | OK, 13 tests |
| `scripts/test_link_targets.py` | OK, 5 tests — **after a fix**: the registry candidate first carried a live wikilink to a `LIT` record it only proposes, which failed both the record-target and the exact-heading test. Now rendered as an instruction |
| `scripts/test_fresh_clone_reader_journey.py` | OK, 5 tests |
| `framework/scripts/test_pathograph.py` | OK, 32 tests |
| `framework/scripts/candidate_tree_freshness.py` | **FRESH**, after regenerating the pathograph with the generator from committed inputs and committing the surface |
| `scripts/run_release_regressions.py` | 136 suites, 682.7 s, `REGRESSION VERDICT: FAIL` with six entries. **None is caused by this branch** — each is diagnosed to its cause below, as the brief requires, and none was accepted as "an environment thing" without being re-run alone |

### The six regression entries, each diagnosed to its cause

| Entry | Cause | Evidence |
|---|---|---|
| `test_mandate_continuity.py` · `test_process_wait.py` · `test_quota_state.py` — "UNATTRIBUTED WRITE of 1 tracked file" | **Self-inflicted concurrency.** All three name the same file, `research/intake_wave_20261003w4_C.md`, written at 11:53:52, 11:53:58 and 11:54:04 — I was editing the analysis note while the battery ran. The runner attributes by timestamp and cannot tell my edit from a suite's | Re-run individually on a quiescent tree: `test_mandate_continuity.py` **OK** (68 tests, 2 skipped), `test_process_wait.py` **OK** (12 tests), `test_quota_state.py` **OK**. The brief's own standing warning covers this case |
| `test_batch_queue.py: exit 1` | **Pre-existing on `main`, and not mine.** `test_coverage_is_not_overstated_against_the_registry` reports `READ_NOT_REGISTERED=['35712340', '37583270', '41153369']` — three of Scientist A's wave-3 PMIDs | `git log main --` on each of the three manifests returns `211c4d3 intake wave 3 2026-10-03 (A)`, and `git merge-base --is-ancestor 211c4d3 main` is true. **None of my six appears**, because my receipts are not yet in the ledger — and `CC-20261003w4-C-REGISTRY-01` exists precisely so they never do appear there |
| `test_paper_packet.py: exit 1` | **Shared gitignored corpus, not this branch.** Two assertions expect no surface on disk for PMID 33914858, and `files/fulltext/PMID33914858_Repudi2021_OUP_browserprint.pdf` is present, with a `_pdftotext.txt` derived at 11:25 today by a concurrent actor. `files/` is gitignored and shared across every checkout | My branch added only the six JATS XMLs and five figure panels listed in `CC-20261003w4-C-REGISTRY-01`; 33914858 is in none of them and I never opened it |
| `test_manifest_receipt_provenance.py: exit 1` | **The transient brief correction 3 predicts**, and it self-closes. Ceiling 15, measured 21; the six extra are exactly my six manifests at `UNKNOWN_EVENT`, because a manifest naming a receipt the ledger does not yet hold is unverifiable by construction | Re-ran the module's own `survey()` with `verdict in mrp.DEFECTS` against two ledgers: live → **21** defects, my six present; live **plus my six receipts** → **15** defects, **my six absent**. Back to the declared ceiling, which is not raised. Script: `scratchpad/sciC/selfclose.py` |

**Landing decision.** Per brief correction 3 the branch is landed, because the one entry attributable
to this work is shown to self-close the moment the Orchestrator appends the receipts. The other five
entries are two concurrency artefacts of my own editing (now green), one pre-existing `main` failure
owned by wave 3, and one shared-corpus artefact. **No ceiling was raised and no suite was exempted.**

**One ratchet was hit and fixed by doing the work rather than by relabelling it.**
`growth_anchors.py` returned `[BLOCK] RATCHET_VIOLATION: 6 new manifests without a panel/text
relation`. The enum admits no value for "a panel bears on this sentence and I did not look", and the
module's own comment says that when no admitted value is true the defect is the enum and forcing one
writes a known falsehood into canonical state. So the five panels that bear on a locator were
fetched and read; see § 3b for what that changed.

## 9 · DEFAULTS_TAKEN · DECISIONS_TAKEN · STOP_LOG

**DEFAULTS_TAKEN**
1. Declared all six readings `partial_fulltext_read` rather than fetching supplements, because
   `complete_fulltext_read` is refused over any `captions_only` section and overclaiming is worse
   than a declared partial. Figure panels and supplementary files are named as unread in every
   dossier and every receipt.
2. Ran `dependency_integrity.py screen` (free, network Crossref) rather than declaring the reference
   lists unscreened, because the manifest schema requires the block and a real screen is better than
   a declaration. Snapshot 2026-09-10 was used because that is what the tool selected; a newer
   2026-10-02 snapshot exists on disk.
3. Used `Tukov FF[au]` as the group-assessment probe for both Novartis papers rather than inventing
   two separate author queries, because the shared author **is** the independence finding.
4. Recorded all four candidates as MINOR, because none narrows or reverses any claim — six sources
   that never mention the gene cannot.
5. Did not run `legend-discovery-method`: the group was assigned as a contradiction to characterise,
   not to resolve.
6. When the panel/text ratchet blocked, fetched and read the five bearing panels rather than
   labelling every locator `text_only`. The default could have been to relabel; relabelling would
   have written a falsehood, and in the event four of the five panels changed something.

**DECISIONS_TAKEN**
1. **Did not decide the DRG contradiction**, as instructed, and recorded it as an open question with
   three live explanations rather than picking the parsimonious one.
2. **Recorded C5/C6 non-independence as likely, not proven**, because the artefacts do not
   cross-list study identifiers. The weaker claim is the one the evidence supports.
3. **Recorded three internal inconsistencies in the sources** rather than silently using the figures
   I judged correct.
4. **Classified NfL, NF-H, CXCL10 and MIP1α as Tier 3 under LEGEND_CORE §13** and routed them to a
   toxicity-surveillance record, not to any WWOX biomarker record.
5. Hardlinked the six artefacts and the five figure panels from the root `files/` into the worktree
   (`ln -f`) rather than symlinking, per brief § 4.
6. **Recorded that one of my own first-pass statements was wrong** rather than silently editing it:
   § 3b names the statement, the pass that produced it and the panel that falsified it. A reading
   that quietly corrects itself teaches the next session nothing about where text-only reading
   fails.

**STOP_LOG**
- **One model safety halt.** My first response in this session was stopped by a safety classifier
  before any tool call completed; the halt occurred at the very start, so no partial work and no
  identifiable content was produced, and I cannot attribute it to a specific passage. Per brief
  § 13 I did not reword and retry the same opening: I restarted from the standing brief and the
  group-C selection and proceeded source by source. No subsequent halt occurred, and no part of the
  assigned reading was abandoned — all six sources were acquired, read and receipted.
- No other stop. No `§21d` RESERVED act was required: nothing was published to a public release
  repository, no history was rewritten, nothing unique was deleted, nothing was spent, and no
  private data was touched.
