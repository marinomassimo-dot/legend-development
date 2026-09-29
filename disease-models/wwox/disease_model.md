# WWOX-DEE — Disease Model & Decision Framework

> **Public, de-identified disease-level model.** Derived from the LEGEND working model with the individual clinical record removed (clinical presentation, treatment regimen, and case-specific surveillance are not included). What remains is the disease-level mechanistic synthesis, the genotype-interpretation rules, the literature-anchored data, and the decision-logic framework — all from public literature. **Not medical advice.** Specific variants appear only as decoupled public worked examples — a destabilizing SDR missense on one side, a canonical splice-acceptor variant on the other — never assembled into one person's genotype.

**Current working model:** WM_v7.1 (`BATCH_20260928_001`).

**Model version lineage:** v3.0 (2026-07-14) — a MAJOR baseline reversal (see the repair changelog at the end) illustrating the epistemic discipline in action.

---

## Genotype interpretation rules (method)

- p.Gln230Pro (Q230P) ≠ P47T — do not auto-transfer P47T data across variants.
- Compound heterozygous ≠ null/null — a milder organoid phenotype is expected than in full KO.
- WWOX variants are **not interchangeable**; extrapolation from full-KO models requires explicit caution.
- Q230P (SDR domain): in homozygous fibroblasts of the exact variant, transcript is normal and protein is not detected. The cause remains unresolved — impaired translation, insolubility, or premature degradation. The HSC70/lysosome read-across from P252A is a **bridge hypothesis**, not a demonstrated mechanism for Q230P.
- Genotype class (Gao 2025 framework): an N/M combination (missense + null-predicted splice) sits outside the highest-risk N/N subgroup — but this never authorizes reduced clinical vigilance.

---

## Mechanistic architecture (disease-level)

**Network hyperexcitability.** WWOX-related encephalopathy should not be modeled only as a "seizure disorder" or as a downstream consequence of developmental damage. Evidence supports a **primary disturbance of neocortical network stability**: spontaneous bursting, altered oscillatory organization, increased phase-amplitude coupling, reduced spontaneous inhibition, increased excitatory drive, depolarization, increased firing, rebound-prone physiology. This elevates network-state pathology to core-pathway status. *(CLAIM 021 / Breton 2021.)*

**Prenatal developmental architecture.** In severe null genotypes, onset may begin prenatally, with detectable fetal brain abnormalities. Severe WWOX disease should not be read as purely postnatal epileptic deterioration; a developmental architecture failure may already be active in utero, especially in null-severe presentations. *(CLAIM 022 / paper 216.)*

**WWOX as routing/scaffold protein.** Beyond tumor suppressor / metabolic regulator, WWOX is a routing/scaffold protein that can change partner localization and redirect biological output. Relocalization of p73 is the anchor example: the same protein produces different output depending on where WWOX routes it. *(CLAIM 023 / PAPER 081, PMID 15070730.)* — **Narrowed in `BATCH_20260909_001`:** the word *phosphorylation-sensitive* and the phrase *Tyr33-dependent* are removed, because the primary source tests no relation between phosphorylation and localisation (20 body sentences mention Src; zero also mention localisation). Tyr33 phosphorylation regulates the **binding**, which is unaffected.

**Domain cooperativity.** WW-domain biology depends on WW1–WW2 tandem cooperativity; variant interpretation should consider tandem stability, partner-recognition geometry, and residual interaction architecture — not isolated single-domain logic. *(CLAIM 024 / paper 204.)*

**Metabolic branch.** Beyond a simple HIF1A/Warburg framing, the WWOX/HIF1A axis appears to be a broader state indicator linked to glycolysis, inflammatory tone, Wnt-related signaling, and possibly state-transition biology; one HEK293T interactome co-purifies with trafficking proteins and is annotation-enriched for catabolic pathways. Acetyl-CoA convergence is a pathway-map reading; functional trafficking–metabolism coupling remains untested. An independent non-neural paper supports the VOPP1 interaction limb. *(CLAIM 025 / paper 191; CLAIM 026 / Hussain 2018 and Bonin 2018.)*

> **Integrity exclusion (a worked example of source-integrity discipline):** the HGF/Met–TAZ–WWOX bone-metastasis line does **not** count as independent corroboration — the primary (PMID 28151481) was retracted in 2022 for western-blot control manipulation/reuse, and a review (PMID 28045433) reuses its data/dependencies. The WWOX/HIF1α axis stands only on the independent sources. No baseline claim depended on the invalidated line.

**Research-facing (not yet core).** HYAL-2 / HA / SMAD4 / WWOX — a high-value ECM/membrane-to-nucleus and injury-response branch, retained but not promoted. *(CLAIM 027 / paper 214.)*

**Cross-pathway interpretive principle.** WWOX output is strongly partner- and context-dependent. Expression level alone is insufficient to infer uniform functional benefit — **"more WWOX = better" is not a safe default** across contexts. *(CLAIM 028 / papers 213, 218, 206, 214.)* WWOX may also contribute to ATM-linked DNA-damage-response competence and genome-stability maintenance — a plausible structural-vulnerability branch. *(CLAIM 029 / Abu-Odeh 2014, PAPER 027; murine B-cell repair and tumour observations in PAPER 110/115 remain context-limited and do not transfer to CNS.)*

---

## Literature-anchored data (DATO — WWOX literature)

- VABAM documented in WWOX-DEE with vigabatrin (Choi 2026) — a real safety signal; conflicting with You 2024 (seizure reduction, no documented VABAM).
- Network hyperexcitability + AAV-WWOX rescue in organoids (Steinberg 2024).
- Non-cell-autonomous hypomyelination in neuronal WWOX deletion (Repudi 2021).
- N/N genotype → higher risk of seizures, hypertonia, respiratory complications vs N/M and M/M (Gao 2025, n=50).
- AAV9-hSynI-hWWOX: dose-dependent durable rescue in a Wwox-null murine model, including ECoG/SWD reduction (Obeid 2026).
- Ketogenic diet: three of five patients in one WOREE series are reported as responders; the number exposed is not stated, and the one Q230P carrier has no diet entry (Chong 2023; [[claim_registry_current#CLAIM 042]]).
- In the P47T knock-in mouse, sampled cerebellar regions have fewer calbindin-positive Purkinje profiles than wild type at 80 and 250 days; basket-cell genotype tests are nonsignificant at both ages. This does not test progression within P47T or transfer to Q230P. *(CLAIM 041 / Hussain 2023.)*

### Inferences (INFERENZA)
- Ca²⁺ / network dysregulation as a primary driver of hyperexcitability — plausible, supported.
- Hypomyelination as a possible amplifier — needs imaging confirmation.
- Neuroinflammation as a low-noise modifier, partly downstream of network dysfunction (neuron-specific rescue reduces gliosis).
- Q230P functional endpoint: normal transcript, protein not detected; synthesis/translation vs premature degradation unresolved; residual function cannot be inferred from abundance alone.
- Part of the WWOX-DEE phenotype plausibly grafts onto a prenatal cortical-assembly substrate (defective layering, incomplete maturation, downstream myelin/glial failure), strengthening the interpretive weight of EEG over early MRI.
- GABA remains an axis in tension: GABAergic vulnerability is probable but not reducible to a simple linear deficit. 🔴 **And the two accounts of it are competing, not complementary (2026-09-27, `BATCH_20260927_004`, WM_v7.0):** inhibitory **amplitude hypofunction** is measured in a WWOX system; **depolarizing / immature GABA** is `IPOTESI` with no WWOX datum under it. The clinical positions below **do not move** — they never rested on the mechanism.

---

## Decision-logic framework (disease-level; not medical advice)

*These are disease-level management-reasoning principles synthesized from the literature for WWOX-DEE, to support — never replace — a treating clinical team.*

**Active pathways.**
- *Ca²⁺ / network dysregulation* — network stabilization is the operative target; change one variable at a time, protecting readability of any active titration/trial window.
- *GABAergic vulnerability (SAFETY)* — vigabatrin: strong caution / avoid unless alternatives are exhausted (conflicting evidence: efficacy on spasms vs VABAM risk); phenobarbital: caution; benzodiazepines: appropriate as rescue, chronic high-dose only if essential.

**Surveillance.**
- *Myelination / white matter* — MRI + DTI as a structured baseline; myelination adjuncts only if imaging is suggestive, one variable at a time.
- *Respiratory / dysphagia* — structurally associated with WWOX-DEE (more severe in N/N, present across genotypes); monitor aspiration/dysphagia/respiratory distress during intercurrent infections. EEG remains more sensitive than early MRI for network severity (Sapuppo 2026).
- *Ophthalmology* — visual impairment reported in 4/5 WOREE patients even with non-uniform imaging (Chong 2023); structured evaluation indicated.

**Red flags — when NOT to change anything.** Infection/fever/dehydration; vomiting/diarrhea/reduced intake/unstable ketones; active AED change or titration; multiple new supplements at once; drastic sleep worsening without clear cause.

**Flowchart logic.** (1) Baseline stable? if no → introduce no variables. (2) Minimum dataset (EEG, MRI, genetics)? if no → prioritize. (3) MRI/DTI hypomyelination? if yes → discuss a myelination adjunct (one variable). (4) Strong GABAergics? apply strong caution (VABAM). (5) Focus: network stabilization. (6) Follow-up: N-of-1 endpoints (startle/sleep/EEG). (7) Maintain gene-therapy trial-ready documentation at all times.
**Principles:** don't force decisions; order timing; separate safety from drivers and structural surveillance; prevent multi-variable changes during titration/trial phases.

**Monitoring endpoints (N-of-1 method).** Startle (0–3 score + daily count + triggers); sleep (awakenings/night + wake/sleep differentiation); feeding/posture (events during transitions); EEG (epileptiform density + background organization — prioritized over seizure count alone).

---

## Gene therapy context (public / preclinical)

- A clinical AAV9-WWOX programme is anticipated (2025–2027).
- Steinberg 2024 organoids: AAV9-WWOX normalizes Ca²⁺ transients and hyperexcitability; MYC overexpression identified as a key mechanism.
- Obeid 2026 (Wwox-null murine): AAV9-hSynI-hWWOX — dose-dependent durable rescue (survival, glucose, behavior, myelination, gliosis, SWD/ECoG); neuron-specific targeting; early postnatal ICV delivery.
- **Design principles:** human synapsin promoter (neuron-specific); WPRE removed (avoid overexpression); dose controlled; critical early postnatal window (P0–P5 in mouse).
- **Safety caveat:** DRG / peripheral-organ dose-limiting toxicity at high systemic AAV dose → favors targeted/controlled delivery (a pediatric regulatory concern).
- **Epigenetic option (future / extension):** dCas9/CRISPRa upregulation of endogenous WWOX for **hypomorphic** states — potentially relevant to residual-function missense alleles; not actionable now.
- **First-in-human (background/observation):** a WWOX gene therapy reported given to an infant with WWOX epilepsy (ICV) — the strongest external signal for the GT axis; awaiting peer-reviewed clinical data. NOT a datum.
- Partial restoration remains a testable possibility for measured endpoints. The dose, corrected-cell fraction and treatment time needed for neurological rescue are unknown (CLAIM 032).

---

## Claim registry summary (baseline mirror)

Full canonical status lives in [`registries/claim_registry_current.md`](registries/claim_registry_current.md). Key disease-level claims (ID · title · type · status):

- 001 Vigabatrin → VABAM in WWOX-DEE · DATO · **conflicting evidence**
- 002 WWOX-LoF → hyperexcitability + AAV rescue in organoids · DATO+INF · consolidated
- 003 Neuronal WWOX deletion → non-cell-autonomous hypomyelination · DATO · consolidated
- 004 AAV9-WWOX neuron-targeted multi-domain in-vivo rescue · DATO · consolidated
- 011 AAV9-hSynI-hWWOX dose-dependent durable rescue · DATO(preclinical) · consolidated
- 014/015 Prenatal cortical development perturbation / misassembled substrate · DATO/INF · consolidated
- 019 Q230P in severe compound-het disease; allele-specific interpretation required · DATO+INF · consolidated
- 028 WWOX output partner/context-dependent; expression ≠ uniform benefit · INFERENZA · flagged for review
- 030 Severity tracks residual **function**, not protein abundance · in observation
- 031 It is a **DEE, not an EE**: seizure control does not save development · in observation
- 032 One WWOX copy preserves some observed endpoints; spontaneous tumour excess and absent CNS dose data leave the neurological rescue threshold open · in observation

---

## Repair changelog (the epistemic discipline in action)

**WM v7.0 → v7.1 (2026-09-28) — MINOR, the Mirror ex-post repair batch, under the operator's standing authorisation (*«procedi tu, ti autorizzo su tutto»*).** Two repair candidates written by Scientists after hostile ex-post reviews of the two previous batches were propagated in full, and the batch that propagated them was their verifier, not their author: every anchor was re-measured, every quotation re-checked against the fingerprinted bytes, and five of the producers' own readiness claims were found false, wrong or loose. 🔴 **One inference was withdrawn, and it is the kind of withdrawal this file exists to show.** A registry paragraph had read a pair of patients — same homozygous missense allele, opposite ends of survival — as *strengthening* the rule that severity tracks residual **function**. Re-reading the source's Table 1 first-hand, with the table's own column alignment checked before any value was read across, the two patients are **concordant** on the three severity axes this claim uses — profound intellectual disability, nonverbal speech, non-ambulation — and the discordance that bears on outcome is **survival**. *(Scoped 2026-09-28, Mirror FINDINGS 1 and 2: «every severity axis the table prints» and «survival alone» were both false — the table prints two further examination axes on which the pair differs, `Short stature` and `Ophthalmologic features`. And the three axes they are concordant on are identical in 13 of 13 patients of that table for intellectual disability and ambulation, and in 11 of 13 for speech, so the concordance on those axes is **uninformative by construction** rather than a measured similarity between these two patients. *(Re-scoped 2026-09-28, `CC-20260928-MIRROR002B-REPAIRS-01`, Mirror FINDING 3: the previous wording — «the absence of a discriminating axis in that table» — was the third narrowing of one false universal, and all 12 examination axes measured off the source markup falsify it. Three axes have zero variance across the 13 patients — intellectual disability, ambulation and **axial hypotonia**, 13/13 each — but the table also prints axes that do discriminate: movement disorder takes six distinct values, short stature splits 7/6, scoliosis 9/13, microcephaly and spasticity 10/13, and on two of them the pair itself differs. The neutral reading does not rest on any of this: it follows from the allele-level premise alone, which is the argument named in the next sentence.)*.)* A pair homozygous for one allele cannot discriminate a rule stated over alleles, and a pair concordant on severity is not evidence of two opposite tails: the observation is **neutral**, and the rival explanations — modifier loci, seizure burden, clinical management, individually varying proteostatic capacity, enrolment bias — are named and left open rather than one of them being quietly adopted. What the pair does falsify is the **syntactic variant class** as a predictor of an individual outcome. Counts and units were corrected against their own sources rather than against each other: an mg/ml → mg/dL conversion factor off by a power of ten; a mortality comparison built on **one** death among 44 genotyped individuals, now recorded as a non-measure instead of a non-replication; a cross-reference census that had reported twelve applied links where 23 were applied, one of them left one-directional and now closed. Two corpus-scoped superlatives (*the largest cohort*, *the only published assay*) were scoped to the corpus actually read, a statistical test's sampling unit was recorded as the **region** rather than the animal, and a pharmacological exclusion was corrected from a blanket *no* to the narrow claim its authors make. 🔴 **Nothing clinical moved:** no claim status, no transferability, no BLOCCO 1 field, no therapeutic score — a safety argument's surface was named without its score being touched. Structurally, the source that had bounded a claim while no registry record named it finally has one, and a corpus placeholder deleted by an earlier batch was **restored**: a placeholder promoted to a full record is re-statused, never deleted, because the trail from corpus ordinal to record is the whole point of the placeholder. **Not medical advice.**

**WM v6.1 → v7.0 (2026-09-27) — MAJOR, the wave-2 MAJOR batch, operator-authorised (*«procedi tu, ti autorizzo su tutto»*).** Two attributions inside `consolidated baseline` claims were **withdrawn**, and neither was wrong about a measurement — both were wrong about what the measurement attributes. The neocortical burst's **gap-junction** dependence is withdrawn: carbenoxolone's effect is real and printed, but it does not reverse on washout and the authors themselves write that the compound *«may not be specific to gap junctions»* and *«could block NMDA receptors»*, in a preparation where the NMDAR blocker **alone** abolishes the burst. That is a withdrawal of attribution, **not** a claim that gap junctions are uninvolved: occlusion was never tested. And the organoid model's *immature GABAergic signature* is demoted to `IPOTESI`: the word *signature* means a measured pattern, and all four mentions of depolarising GABA in the source sit in one Discussion paragraph supported by general developmental neuroscience, with the chloride transporters, the perforated-patch method and the pharmacological polarity test appearing **zero** times. The corpus's one functional inhibitory measurement points at reduced **amplitude**, not reversed polarity, and the two accounts compete. 🔴 **Nothing clinical moved.** The GABAergic-drug cautions are byte-identical: they rest on the human safety signal against the human efficacy reports, never on the mechanism — and a caution resting on an unmeasured premise is fragile in the dangerous direction, so removing that premise strengthens it. Four claims were **bounded** rather than reversed (WW-domain cooperativity is not required for every partner; seizure transferability is now stated per axis; the gene-therapy endpoints are split so that no sentence of the form *the phenotype is rescued* survives), one therapeutic safety score moved on a measurable **absence** (the dose-ranging study performs no tumour surveillance at all), and every figure or supplementary value the batch could not re-open stayed a **declared attestation** rather than becoming a quotation. Five blind auditors read the locator triples without knowing whose reading they were; four of their OVERSHOOT verdicts rewrote the wording to the source's own hedged words, and three of them corrected the batch's own inputs. **Not medical advice.**

**WM v6.0 → v6.1 (2026-09-27) — MINOR, the wave-2 readiness batch.** Eighteen queued candidates were verified record by record against the current files and against the locators they cite, and propagated: an **abundance** datum was withdrawn from `CLAIM 016` because the figure it rests on carries one lane per genotype, no n and no test — in **both** directions, so neither "elevated" nor "flat" is assertable; `CLAIM 033`'s mortality association gained the reservation that it does not replicate in an independent registry cohort and that two of the three deaths in the cohort which generates it carry a missense allele; `CLAIM 025` was bounded on the **direction** of its marker, which its newest source calls descriptive and hypothesis-generating; `CLAIM 038` records that an impossible unit is the **source's** defect and that LEGEND's transcription is faithful. The Mirror ex-post review of the previous batch was repaired where it touched a canonical file, and `CLAIM 005`'s prohibition on asserting epileptogenesis as a measured process stayed byte-identical. No claim changed `Status`, and no therapeutic statement moved.

**WM v5.7 → v6.0 (2026-09-27) — MAJOR, a negative withdrawn.** One canonical record said the **audiogenic** phenotype of WWOX rodent models was rat-specific, a second (`consolidated baseline`) said **seizures** in the `Wwox` literature were a rat `lde/lde` phenotype, and the first added that the paper carrying the mouse observation could not be read here — *"no `n`, no strain, no stimulus protocol and no control"* — and that no `Wwox` mouse had ever been audiogenically provoked in any inspectable method, as a standing `PREMISE: NOBODY_LOOKED`. The paper (Mallaret 2014, PMID 24369382) had in fact been read in full from this repository's own full-text directory two weeks earlier: a failed remote retrieval had been recorded as a corpus-level absence. Its Methods and Results carry a protocol (11 and 14 kHz tones, 5–10 min, speakers on three sides of conventional polycarbonate cages, video-recorded), two denominators (3 of 8 constitutive knock-outs at 16 days; per the Results text the four survivors at 20 days, the Fig. 4 legend accounting for three) and a comparator (0 of 8 wild types) — behavioural and **unscored**, one laboratory, no EEG, and handling also provoked seizures *on some occasions*, so the stimulus is not shown to be specifically acoustic. **Withdrawn:** the two false clauses, the premise, the rat-only sentence in the `consolidated baseline` interneuron claim, and four smaller misstatements (a 2020 date for a 2014 record; a "commentary" that is the article's own front-matter summary; the mouse data attributed to the wrong null line; a 2–3-week lifespan against the source's *3 to 4 weeks maximum*). **Unchanged:** the prohibition on asserting **epileptogenesis as a measured process** in any WWOX model — nobody has measured that transition, and a provocation is provoked susceptibility, not epileptogenesis; the kindling-like progression as a rat-only result; every rat datum; both claims' status; and **T3** for any transfer of an audiogenic phenotype to a human genotype. A constitutive biallelic null models neither human missense allele.

*(The withdrawal was written as a candidate, audited blind against the source before propagation, and landed with the operator's authorisation. A negative is a claim, and it is read and retired like one.)*

**WM v2.1 → v3.0 (2026-07-14) — MAJOR baseline reversal.** Withdrew the equation `normal mRNA + absent protein = post-translational degradation`. Johannsen 2018 explicitly states two alternatives: impaired translation **or** premature degradation. Consequences: CLAIM 019 keeps the human datum on the exact variant but downgrades the cause to unresolved; CMA, `LRSVQ`, and the helix-lid model remain hypotheses transferred from P252A/AlphaFold, **not** a demonstrated Q230P mechanism; C299R withdrawn as a validated catalytic/off-lid control; the first experimental gate separates synthesis, insolubility, and turnover, with abundance and function measured together; an SDR stabilizer is `conditional / not design-ready`.

*(This reversal — retracting a plausible, already-consolidated conclusion the moment the evidence no longer uniquely supported it — is a worked example of the [false-negative/premise discipline](../../framework/instruction/epistemic_discipline.md).)*
