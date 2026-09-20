# Domain-sufficiency in vivo — locator audit of PMID 25649963

**Target proposition under audit:** *"An isolated WWOX domain is sufficient to rescue in vivo."*
**Target of the audit:** discovery-ledger lead `DL-MECH-021` (currently `belief: medio`, held second-hand, no receipt).

| Field | Value |
|---|---|
| Paper | Tsuruwaka Y, Konishi M, Shimada E (2015). *Loss of wwox expression in zebrafish embryos causes edema and alters Ca²⁺ dynamics.* **PeerJ** 3:e727 |
| PMID | **25649963** · PMCID **PMC4312067** · DOI [10.7717/peerj.727](https://doi.org/10.7717/peerj.727) |
| Licence | CC BY 4.0, `is_open_access: true` (confirmed via PubMed copyright check, source `pmc`) |
| Retrieval route | PubMed MCP `get_full_text_article`, `pmc_ids: ["PMC4312067"]` — **succeeded**, non-empty body |
| **Declared read depth** | **FULL TEXT, complete.** Introduction, Materials and Methods (all 7 subsections), Results (3 subsections), Discussion, Conclusion, and all four figure legends were returned and read end to end. This is a full-text read, not an abstract read. |
| **Supplementary** | **NOT obtainable.** The MCP extraction returned no supplementary material and no supplementary file list. PeerJ hosts supplemental information separately from the PMC body; no route to it exists on this surface. Any datum living only in supplementary is unresolved here. |
| **Figure/panel access** | **NONE.** No PDF tooling and no figure images exist in this deployment. Figures 1–4 are available to me **only as their text legends**. I did not and cannot inspect any panel, colour-coded Ca²⁺ map, micrograph or bar chart. Every statement below that depends on a panel is marked `UNRESOLVED — panel-dependent`. |
| Extraction artefact | The MCP extractor **strips italic gene symbols**, figure callouts and reference markers. Quotes below are reproduced exactly as returned; where the stripped token is unambiguous from context I supply it in square brackets as **my** insertion, e.g. `[wwox]`. Square brackets in quotes are always mine, never the authors'. |
| Auditor | Scientist A · read-only toward all canonical files · 2026-09-21 |

> **Framing note, established before any question is answered.** The word **"sufficient" never appears in this paper**, and neither does any discussion of domain structure beyond the sequence alignment in Figure 1. The Discussion is about breast cancer, gastric carcinoma, bone volume and *Wwox*-KO mice. **The authors did not present this as a domain-sufficiency experiment.** The domain restriction of the rescue construct is stated only in Methods and is never mentioned again. This is the single most important structural fact of the audit, and it is established from text alone, independent of any panel.

---

## Q1 — What exactly was done?

**Species and stage.** Zebrafish (*Danio rerio*), wild-type adults from a pet store; embryos from natural crosses; injection at the **single-cell stage**; phenotype scored at **48 hpf (long-pec)**; Ca²⁺ imaged at **30 hpf (prim-15)**.

> "Approximately 3 nL of MOs (1 mM) or siRNA (50 µM) were injected into single-cell zebrafish embryos, and phenotype rescue was achieved by co-injection of a target gene RNA (ADH domain) that does not bind MO or siRNA, as previously described in ZFIN () and." — PMID 25649963, Methods, *Construction of antisense morpholinos (MOs) and small interfering RNA (siRNA)*

**Knockdown method — two reagents, two chemistries.**

> "In these experiments, a[wwox] MO was designed to disrupt[wwox] translation, and[wwox] siRNA was designed to target the N-terminal[wwox] WW domain sequence. MO sequences were as follows: Danio-MO, 5′-TATTTGAGAGCCGCCATTGCGAAAT-3′ (3′-fluorescein), and 5-mis-DanioMO (negative control), 5′-TAaTTGAcAGCgGCgATTGCcAAAT-3′ (3′-fluorescein). The standard MO control 5′-CCTCTTACCTCAGTTACAATTTATA-3′ (3′-fluorescein) was obtained from Gene Tools and was used as a positive control. The[wwox] siRNA sequence was 5′-GAGCAAAGCCCGUGUGGAA-3′." — PMID 25649963, Methods

So: **one ATG/translation-blocking morpholino**, plus **one siRNA** directed at the WW-domain-coding region. These are non-overlapping in target sequence but are *not* two morpholinos (see Q3).

**Rescue constructs — there is exactly ONE, and it is the ADH/SDR region.**

> "RNA rescue experiments were performed after preparing[wwox] mRNA (ADH domain region) by replacing pTAC-2 with the pCS-2 vector. The open reading frame of the ADH domain was inserted between[Bam]HI and[Eco RI] restriction sites located downstream of the SP6 promoter sequence in the pCS2 vector." — PMID 25649963, Methods, *PCR and cDNA cloning*

The domain boundaries are given in the Figure 1 legend:

> "the WW domain (amino acids 18–47 and 59–87, circled with red boxes), the NLS (amino acids 50–55, underlined), the ADH domain (amino acids 121–330, circled with a blue box) and Tyr(*) are shown." — PMID 25649963, Figure 1 legend

**Therefore the rescue construct is approximately aa 121–330: it lacks WW1, WW2 *and* the nuclear localization signal (aa 50–55).**

🔴 **There is no full-length wwox rescue arm. There is no WW-domain-alone arm. There is no point-mutant arm. There is no dose series.** The Methods describe the preparation of exactly one rescue RNA. A sufficiency claim is a *comparative* claim; this design contains nothing to compare against.

**Readouts.** Pericardial edema and its penetrance at 48 hpf; body length; eye diameter; survival; Ca²⁺ FRET imaging (Yellow Cameleon YC2.12) at 30 hpf; whole-mount *in situ* hybridization for expression pattern.

> "Embryos were embedded in 3% methylcellulose ... and body length images were measured from the head to the tail along with body axis in lateral view (= 30) in three independent experiments using RS Image Software. Eye sizes were measured and the longest diameters of eyeballs were recorded. Data are presented as means ± SEM, and differences between groups were identified using Student's-test and were considered significant when< 0.01." — PMID 25649963, Methods, *Microinjection*

**Injection counts.**

> "Numbers of eggs were 2460 in[wwox]MO, 2590 in[wwox]siRNA, and 770 in rescue experiments." — PMID 25649963, Methods, *Microinjection*

⚠️ **Correction to the ledger's use of these numbers.** `DL-MECH-021` records "rescue (n=770)". Per the Methods sentence above, **770 is the number of *eggs injected* in rescue experiments, not a number of scored embryos, and it is not broken down between the MO-rescue and siRNA-rescue arms.** The same applies to 2460 and 2590. These are injection denominators, not outcome n.

⚠️ **Internal unit inconsistency, noted for the record.** "Approximately 3 nL of synthetic mRNA (0.5 ng/mL)" (Methods, *Microinjection*). 0.5 ng/mL × 3 nL = 1.5 femtograms of mRNA, which cannot drive a rescue; the intended unit is almost certainly ng/µL or ng/nL. **The delivered dose of the rescue mRNA is therefore not recoverable from the paper.** No dose is stated anywhere for the rescue arm specifically.

---

## Q2 — Does an isolated domain actually rescue, and which one?

**The entire evidentiary basis for the rescue is one sentence.** Reproduced complete and verbatim:

> "However,[wwox] mRNA rescued the phenotype in MO and siRNA injected embryos (and)." — PMID 25649963, **Results**, *Knockdown and detection of zebrafish [wwox]*

That is the whole of it. The parenthesis `(and)` is the stripped figure callout, pointing to Figures 2C and 2D. The Figure 2 legend describes those panels as:

> "(C) A[wwox] rescued MO-injected embryo (upper, bright-field image; lower, fluorescence image). (D) A[wwox] rescued siRNA-injected embryo." — PMID 25649963, Figure 2 legend

**"A ... embryo" — singular, in both panels.** The legend describes representative single-embryo images, not a scored cohort.

**Which domain.** By the Methods quote in Q1, the injected RNA is the **ADH/SDR region (aa ~121–330)** — i.e. the domain that carries Q230. So the claim as LEGEND recorded it ("the rescue succeeds with the ADH/SDR domain alone") is **factually accurate as to what was injected**.

**Fully / partially / not at all — and quantified or described?**

- The Results sentence says "rescued the phenotype" with **no qualifier**: not "partially", not "fully". It is an undifferentiated assertion.
- 🔴 **The rescue is described, not quantified.** The paper *does* quantify penetrance for the knockdown arms — "with 56% and 62% penetrance of edema in 48 hpf embryos after injections with MOs and siRNA, respectively" (PMID 25649963, Results) — and then gives **no corresponding penetrance, no proportion, no n, no p-value and no statistic of any kind for the rescue arm.** The asymmetry is conspicuous: the authors knew how to report penetrance and did not report it for the rescue.
- The one quantitative panel is Figure 2E, whose legend reads: "(E) Quantification of body lengths and eye sizes of long-pec embryos; 30 embryos were examined in three independent experiments and data are expressed as means ± SEM (< 0.01); WT, wildtype" (PMID 25649963, Figure 2 legend). **The legend does not name a rescue group among the groups plotted.**
  - `UNRESOLVED — panel-dependent`: whether Figure 2E contains a rescue bar cannot be settled from text. I cannot open the panel. If a quantified rescue exists anywhere in this paper, Figure 2E is the only place it could be, and neither the Results text nor the legend says it is there.

**A structural point that no panel could change.** Even a perfectly quantified Figure 2E rescue bar would establish *that the ADH construct rescues*, never *that the ADH domain is sufficient*, because **sufficiency is only meaningful relative to a full-length comparator, and this paper contains none.** With one arm you cannot distinguish "the domain is enough" from "the domain is 30% as good as full length and 30% is enough for this endpoint". That distinction is precisely the therapeutically load-bearing one.

**`D-04` applies directly.** The construct is aa ~121–330 — the SDR **stripped of both WW domains**. Under the standing rule that in WWOX stability is bought with occlusion and occlusion is anti-function, an isolated, non-occluded SDR is exactly the species expected to behave *better* in isolation than the same domain does inside intact WWOX. A rescue by this construct is therefore **not evidence that the SDR is the sufficient module of the intact protein**; it is at most evidence that a de-occluded SDR fragment, overexpressed from injected mRNA, can support this endpoint.

**Endogenous vs injected.** Everything about the rescue is an **overexpression experiment**: capped mRNA injected into the blastodisc of a one-cell embryo, expressed from an SP6/pCS2 cassette at an unstated (and, per the unit error above, unrecoverable) dose. Nothing here reports on the endogenous protein. **Nothing in the paper shows the endogenous Wwox protein at all** (see Q3).

**Inference, labelled as inference, not as finding.** The rescue construct lacks the NLS (aa 50–55, per Figure 1 legend). If the rescue is real, the rescuing species is presumptively excluded from the nucleus — which would point *away from*, not toward, the nuclear/pro-apoptotic WWOX signalling axis that the neurological literature invokes. This is a reading of the construct map, not a result the authors report or test.

---

## Q3 — 🔴 Morpholino-era specificity controls

Assessed against the 2015-contemporary standard (Eisen & Smith 2008; Robu et al. 2007 for the p53 artefact). **Present** and **absent** are both established from Methods text alone and are not panel-dependent.

| Control | Status | Locator |
|---|---|---|
| **Second, non-overlapping morpholino** | ❌ **ABSENT** | Only one *wwox*-targeting MO is described: "Danio-MO, 5′-TATTTGAGAGCCGCCATTGCGAAAT-3′". No second MO (no splice-blocker to pair with the translation-blocker). |
| **Mismatch control MO** | ✅ **PRESENT** | "5-mis-DanioMO (negative control), 5′-TAaTTGAcAGCgGCgATTGCcAAAT-3′ (3′-fluorescein)" — a 5-mismatch control, and its injected phenotype is shown: Figure 2 legend, "(ii)[wwox] negative-control MO-injected embryo". |
| **Standard control MO** | ✅ present, ⚠️ **mislabelled** | "The standard MO control ... was obtained from Gene Tools and **was used as a positive control**." A standard control MO is by construction a **negative** control. Calling it a positive control is either a wording error or a misunderstanding of the control's function; either way it is a flag on the methodological care of the paper. |
| **Rescue by MO-resistant mRNA** | ⚠️ **PRESENT BUT CONFOUNDED** | "phenotype rescue was achieved by co-injection of a target gene RNA (ADH domain) **that does not bind MO or siRNA**". The resistance is real — but it is achieved **by truncation, not by silent-mutation redesign of the target site**. The MO targets the ATG region and the siRNA targets the WW-domain-coding sequence; an aa-121–330 fragment lacks both *by virtue of being a fragment*. 🔴 **The construct's reagent-resistance and its domain identity are therefore inseparably confounded.** The most parsimonious reading of the Methods is that the ADH region was chosen because it was the easiest way to obtain a non-targetable RNA — not in order to test what a domain can do. Nothing in the paper contradicts that reading, and the total absence of any domain discussion in the Discussion supports it. |
| **p53 morpholino co-injection** | ❌ **ABSENT** | The strings "p53", "tp53" and "apopto-" **do not occur anywhere in the retrieved full text** — not in Methods, Results, Discussion or any figure legend. The canonical control for MO off-target p53-dependent apoptosis was not performed, and its absence is not discussed. |
| **Verification that the MO reduced Wwox protein** | ❌ **ABSENT** | No Western blot, no antibody, no protein assay of any kind appears in the Methods. The only RT-PCR is developmental-stage expression profiling ("Expression of zebrafish[wwox] at various developmental stages was determined using RT-PCR", Figure 1B legend), not knockdown verification — and an ATG-blocking MO would not change mRNA in any case. **Knockdown efficacy is asserted, never demonstrated.** |
| **Genetic mutant / stable line corroboration** | ❌ **ABSENT** | No mutant allele, no CRISPR line, no genetic cross. The paper is reagent-only. |
| **Statistics on the edema endpoint** | ❌ **ABSENT** | Penetrance is given as bare percentages (56%, 62%) with no n per clutch, no number of independent clutches, no confidence interval and no test. The stated p<0.01 threshold is attached only to body length and eye size. |

**What is present:** a mismatch control, a standard control MO, and an independent second reagent of a *different chemistry* (siRNA) targeting a *different* part of the transcript, which reproduces the edema at comparable penetrance. That is a genuine and non-trivial specificity argument, and it is the strongest thing this paper has.

**What is absent, stated plainly:** **no second morpholino, no p53 co-injection, no protein-level demonstration of knockdown, no genetic mutant, and no statistics on the phenotype that the rescue is claimed to reverse.** Further, the second reagent is **siRNA in zebrafish embryos**, a knockdown modality with a well-known reputation for unreliability and non-specific early toxicity in this organism; it is a weaker corroborator than a second MO would have been, and weaker again than a mutant.

🔴 **This materially changes how much the rescue result can carry.** A rescue is only as strong as the specificity of the phenotype it reverses. With the p53 control absent and knockdown never verified at the protein level, the possibility that some fraction of the edema/small-eye/short-body triad — a triad that is close to the textbook description of generic morpholino toxicity in zebrafish — is off-target cannot be excluded from within this paper. The siRNA arm mitigates but does not close this, because siRNA in embryos has its own non-specific toxicity profile and because the *same* unverified-knockdown objection applies to it.

---

## Q4 — The Ca²⁺ result: number, trace, statistic, or adjective?

**Adjective.** The ledger's suspicion is confirmed in full. The complete Ca²⁺ Results section, verbatim:

> "Inhibition of[wwox] expression caused morphological abnormalities, and Ca signaling patterns are reportedly altered during zebrafish morphogenesis (;). Therefore, we analyzed intracellular Ca dynamics after edema formation in embryos that had been simultaneous transfected with yellow cameleon, YC2.12, and siRNA. **Patterns of Ca dynamics strikingly differed between[wwox] knockdown embryos and normal fish (), with maximal Ca levels at the boundary between the edema and yolk.**
>
> **Relatively high rates of intracellular Ca dynamics were observed among areas of heart tissue and in putative digestive organs that expressed[wwox]. High Ca levels were observed in putative digestive organs, but no corresponding morphological changes were noted.**" — PMID 25649963, Results, *Analysis of intracellular Ca dynamics after edema formation*

And the figure legend:

> "Comparison of intracellular Ca dynamics in prim-15 stage (30 hpf) embryos. Upper, bright field image; lower, color-coded image; (A) wildtype; (B)[wwox] knockdown produced edema formation and induced altered Ca dynamics; Scale bars, 250 µm. **The color-coded image shows Ca levels as white (high Ca) and blue (low Ca).**" — PMID 25649963, Figure 4 legend

**Inventory of what is and is not there:**

- **Number:** none. No YFP/CFP ratio, no ΔR/R, no absolute or estimated [Ca²⁺], no amplitude, no frequency, no latency, no duration.
- **Trace:** none described. Figure 4 is a pair of static colour-coded images (wildtype vs knockdown), not a time series. YC2.12 is a *ratiometric* FRET sensor — it is built to produce numbers — and the paper reports a colour map instead.
- **Statistic:** none. No n for the imaging experiment, no number of embryos, no test, no p-value, no error term. The word "strikingly" is doing all of the work.
- **Adjectives actually used:** "strikingly differed", "Relatively high rates", "High Ca levels", "maximal".
- `UNRESOLVED — panel-dependent`: I cannot view Figure 4's colour-coded images. But note that **no quantification is recoverable from a qualitative colour map even by a reader who can see it** — a white-to-blue LUT with no calibration bar mentioned in the legend is not a measurement.

🔴 **Two confounds that bear directly on the ledger's use of this result.**

1. **The Ca²⁺ change was measured only in siRNA embryos, and only *after* edema formation.** The section is titled "Analysis of intracellular Ca dynamics **after edema formation**" and the Methods state the embryos were "simultaneous transfected with yellow cameleon, YC2.12, and siRNA". So the Ca²⁺ abnormality sits **downstream of an established gross cardiac/circulatory failure phenotype**. It cannot be separated from the secondary consequences of a failing heart pump. The authors say so themselves:

   > "high levels of Ca were observed in tissues with high[wwox] expression, with the exception of the dorsal region, which was subject to deleterious digestive tract and blood vessel environments that **reflected dysfunctions of the heart pump**." — PMID 25649963, Discussion

   > "Therefore, inhibition of[wwox] could have pointed a **non-cell-autonomous phenotype**." — PMID 25649963, Discussion

2. **The Ca²⁺ signal is peri-edema, cardiac and digestive — it is not neural.** The maximum is "at the boundary between the edema and yolk"; the regions named are "heart tissue" and "putative digestive organs". The only CNS-adjacent expression mentioned anywhere is "weak localized expression was detected in optic nerves" (Figure 3 legend), and **no brain Ca²⁺ measurement is reported at all.** The imaging window was also hard-capped early: "Embryos at prim-15 stage (30 h post fertili[z]ation; hpf) were analyzed because Ca imaging could not be performed after 33 hpf due to the remarkable pigment patterns on zebrafish bodies" (PMID 25649963, Methods) — i.e. the experiment ends before any neural circuit exists to measure.

⚠️ **Correction required to `DL-MECH-021`'s relevance paragraph.** The ledger presents this as "the first *in vivo* datum linking WWOX loss to calcium dysregulation, i.e. a mechanistic bridge toward seizures." **That bridge is not in this paper.** The calcium measured is at an edema/yolk boundary in a 30-hpf embryo with a failing heart, in tissues the authors name as heart and gut, with the authors themselves raising non-cell-autonomy. Re-using it as a substrate-of-network-excitability argument is a category transfer the source does not license.

---

## Q5 — What is the actual endpoint?

| Endpoint measured | Present? | Locator |
|---|---|---|
| **Developmental morphology** — pericardial edema | ✅ primary | "Injections of[wwox] targeting MOs into zebrafish embryos resulted in phenotypic alterations that were characteristic of pericardial edema at 48 hpf during the long-pec stage" (Results) |
| **Morphometry** — body length, eye diameter, backbone | ✅ | "Knockdown of[wwox] caused noticeable reductions in eye sizes and body lengths, and embryos had twisted backbones ()." (Results) |
| **Survival** | ✅ coarse | "Edema was particularly severe around the heart and caused death of embryos within 1 week." (Results) |
| **Ca²⁺ imaging** | ✅ qualitative only | See Q4 |
| **Expression pattern** (ISH) | ✅ | "Strong[wwox] expression was detected in developing hearts at 48 hpf and weak expression was observed in putative digestive organs ()." (Results) |
| **Apoptosis — TUNEL / acridine orange / caspase** | ❌ **ABSENT** | No apoptosis assay of any kind appears in the Methods, Results or legends. |
| **Behaviour** — touch-evoked escape, locomotion, startle | ❌ **ABSENT** | No behavioural assay. |
| **Seizure-like activity** — PTZ challenge, locomotor seizure scoring, electrophysiology | ❌ **ABSENT** | None. |
| **Any neuronal or neurological measure** | ❌ **ABSENT** | The only CNS-adjacent observation in the entire paper is "weak localized expression was detected in optic nerves" (Figure 3 legend) — an expression observation, not a functional one. |

**The endpoint of this paper is developmental morphology in a cardiac-dominant expression field.** The organ the paper is about is the heart:

> "In summary, we demonstrated the utility of the present fish model in studies of[wwox] gene function. **The present data show strong effects of[wwox] knockdown in developing heart tissue** and weaker effects on putative digestive organs." — PMID 25649963, Discussion

🔴 **A developmental-morphology endpoint cannot report neuronal function, and this one does not attempt to.** The rescue, whatever its strength, rescues *pericardial edema in a 48-hpf embryo*. It says nothing about neurons, synapses, myelin, excitability or seizures.

**Abstract-versus-Results check (per standing protocol).** Two observations, in opposite directions:
- The abstract **omits the rescue entirely** — "High Ca levels were observed at the boundary between the edema and yolk in wwox knockdown embryos" is where the abstract ends. The rescue is not an abstract-level claim at all, which is itself informative about how much weight the authors placed on it.
- The abstract does contain one unsupported analogy: "wwox knockdown induced pericardial edema **with similarities to conditions observed in human breast cancer**." Nothing in the Results establishes any similarity between zebrafish embryonic pericardial edema and human breast cancer; the Discussion offers only that *WWOX* is lost in breast cancers and that edema "form[ed] around the pectoral region". **This is an abstract-level claim with no Results-level support** and is logged here as a sixth instance of the abstract-vs-results pattern this repository has been tracking.

---

## VERDICT on *"an isolated WWOX domain is sufficient to rescue in vivo"*

### `PARTIALLY SUPPORTED`

**The narrow version — this is the maximum the source will carry:**

> In zebrafish embryos, co-injection of a capped mRNA encoding only the *wwox* ADH/SDR region (aa ~121–330, lacking both WW domains and the NLS), at an unstated dose, was **asserted by the authors in a single unquantified Results sentence** to rescue the pericardial-edema morphology produced by a single ATG-blocking morpholino and by an siRNA. **No penetrance, no n, no statistic and no full-length comparator accompany the assertion; the construct's reagent-resistance is confounded with its domain identity; and the p53 off-target control, a second morpholino, and any protein-level verification of knockdown are all absent.**

**Why not `SUPPORTED`:** "sufficient" is a comparative claim and **this design has no comparator.** With one rescue arm and no full-length wwox arm, the experiment cannot distinguish complete from partial rescue, and cannot rank the domain against the intact protein. This limitation is structural, established from Methods text, and would survive any panel inspection.

**Why not `NOT SUPPORTED`:** the experiment was performed, the construct is unambiguously the ADH/SDR region, and the authors do report a rescue. The proposition is weakly supported, not contradicted.

**Why not `CANNOT DETERMINE ON THIS SURFACE`:** the decisive facts — one rescue arm only, no full-length comparator, no p53 control, no second MO, no protein-level knockdown verification, and a Results sentence with zero quantification — are all recoverable from text I read in full. Only one subordinate question is surface-limited: **whether Figure 2E contains a quantified rescue group is `UNRESOLVED — panel-dependent`**, and resolving it in the affirmative would move the strength of the rescue but not the verdict, because it could not supply the missing comparator.

**Collateral finding about the field claim.** The premise that this is "the only in-vivo domain-sufficiency experiment in the WWOX field" **does not survive contact with the paper.** This is not a domain-sufficiency experiment. It is an edema-rescue experiment whose rescue reagent happened to be a domain fragment, chosen — on the most natural reading of the Methods — for reagent-resistance rather than for what it would test. The authors never frame it, discuss it, or quantify it as a sufficiency result. **LEGEND should stop describing it as one.**

---

## What this does and does not say about gene-therapy construct scope

**Bearing on `TX-007` (gene therapy, now first-in-human) and `TX-003` (proteostasis lever) — conservative reading.**

**It does NOT say:**
- ❌ That a truncated, SDR-only AAV construct would be therapeutically adequate in a mammal. The rescued endpoint is **pericardial edema in a 48-hpf zebrafish embryo**. There is no neuronal, behavioural, myelin, seizure or survival-beyond-a-week endpoint in this paper. A morphological rescue in a fish embryo is not a neurological rescue in a child, and the distance between them is not a matter of degree.
- ❌ That the SDR is the functionally sufficient module of intact WWOX. `D-04` cuts directly against that inference: the construct is a **de-occluded** SDR. A domain that performs in isolation may perform *because* it has been freed from the WW domains, which is an argument about the fragment, not about the domain's role inside the full-length protein.
- ❌ That WW-domain function is dispensable. **The paper never tested a WW-only construct and never tested full-length.** Absence of a WW arm is not evidence against WW.
- ❌ That construct size can safely be reduced for AAV packaging. **Nothing here licenses a packaging decision.** Full-length human *WWOX* CDS (~414 aa) already fits AAV comfortably; the packaging pressure that would make a truncation attractive is not acute for this transgene, so this weak fish datum should not be permitted to argue for a smaller construct that gives up domains whose necessity is untested.
- ❌ That the rescuing species would even reach the nucleus. The construct lacks the NLS (aa 50–55). If nuclear WWOX function matters for the neurological phenotype — which this paper does not address — an NLS-less fragment is the wrong molecule.

**It does say, weakly:**
- ✅ That an ADH/SDR-region product, **overexpressed from injected mRNA**, was reported to reverse one gross developmental phenotype in one organism. That is a directional hint, of low weight, that the SDR region carries *some* biological activity in vivo.
- ✅ That there exists a **usable in-vivo rig** — one-cell injection, edema + morphometry + YC2.12 Ca²⁺ imaging, with a rescue arm already attempted — into which a human `WWOX-Q230P` mRNA could be injected to ask whether the missense allele rescues where the ADH fragment did. **That platform value is real and is independent of whether the domain claim holds.** It is the durable asset in this paper.

**Net.** For construct-scope purposes this paper is **not decision-grade and should not be cited in a construct-scope argument.** If the question "does an isolated domain suffice" is to bear on `TX-007`, it requires a mammalian experiment with a full-length comparator and a neurological endpoint. No such experiment is in evidence in the model.

---

## Recommendation on `DL-MECH-021`

**`LOWER`** — from `belief: medio` to `belief: basso`, retained (not retired) as a **now-receipted platform description**, with the causal statement `SDR_domain_alone —sufficient_to_rescue→ edema_phenotype` **demoted to an unquantified author assertion**, the Ca²⁺ statement re-tagged **qualitative / cardiac-secondary / non-cell-autonomy acknowledged by the authors / non-neural**, and the entry's "mechanistic bridge toward seizures" framing **withdrawn** — because the rescue rests on a single sentence with no penetrance, no statistic and no full-length comparator; because the p53 morpholino control, a second morpholino and any protein-level verification of knockdown are all absent; and because the calcium was measured only in siRNA embryos *after* edema, at an edema/yolk boundary in heart and gut at 30 hpf, never in brain.

> Not `retire`: the experiment is real, the entry is now first-hand and receipted, and the morphant + Ca²⁺-imaging + rescue rig remains a genuine and immediately usable in-vivo screening platform for testing human `WWOX-Q230P`. Not `hold`: `medio` was set on a second-hand reading that implied a quantified domain-sufficiency result; the primary text contains no such result, and two of the ledger's inferential uses of it (domain sufficiency, calcium-to-seizures) are over-reads that the source does not license.

---

### Audit integrity notes
- This file is an analysis artefact. **No canonical file was read for edit, modified, or queued; no commit candidate was produced; no therapy is proposed.**
- Every finding above carries a verbatim quote attributed to PMID 25649963. Square brackets inside quotes mark **my** reinsertion of gene symbols and restriction-enzyme names stripped by the MCP extractor; empty parentheses are stripped figure/reference callouts, left in place to show the extraction seam.
- **Panels were not inspected and no claim above rests on one.** The two panel-dependent questions are marked `UNRESOLVED — panel-dependent` in Q2 and Q4.
- Source material retrieved from **PubMed** / PubMed Central: Tsuruwaka Y, Konishi M, Shimada E. *Loss of wwox expression in zebrafish embryos causes edema and alters Ca²⁺ dynamics.* PeerJ. 2015;3:e727. PMID 25649963, PMCID PMC4312067, [DOI](https://doi.org/10.7717/peerj.727). © 2015 Tsuruwaka et al., CC BY 4.0.
